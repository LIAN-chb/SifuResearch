"""Create source-addressable Obsidian configuration catalogs from existing static exports."""
import argparse,collections,csv,datetime,gzip,hashlib,json,re,sys
sys.dont_write_bytecode=True
from player_labels import field_label,field_note
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch');VAULT=ROOT/'Sifu';OUT='03配置'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def gz(name):
 with gzip.open(ROOT/'inventory'/name,'rt',encoding='utf-8') as f:return json.load(f)
def readcsv(name):
 with (ROOT/'exports'/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def cell(v):
 if v is None or v=='':return '未保存'
 if isinstance(v,bool):return '是' if v else '否'
 if isinstance(v,float):return format(v,'.9g')
 if isinstance(v,(dict,list)):return json.dumps(v,ensure_ascii=False,separators=(',',':')).replace('|',r'\|').replace('\n','<br>')
 return str(v).replace('|',r'\|').replace('\n','<br>').replace('\r','')
def tab(headers,rows):return '\n| '+' | '.join(headers)+' |\n|'+'|'.join(['---']*len(headers))+'|\n'+''.join('| '+' | '.join(cell(v) for v in row)+' |\n' for row in rows)+'\n'
def wl(path,label=None):return '[['+path.removesuffix('.md')+('|' + label if label else '')+']]'
def name(asset):return Path(asset).stem
def group(asset):
 if '/_MainChar/' in asset:return '玩家'
 if '/Archetypes/' in asset:return asset.split('/Archetypes/')[1].split('/')[0]
 return '共享'
def scope(asset):
 tags=[('竞技场','/_Arena/'),('旧路径','/_old/'),('测试','/_Tests/'),('主流程目录','/_MainGame/')]
 found=[label for label,s in tags if s.lower() in asset.lower()]
 return '、'.join(found) if found else '路径未专门标注；使用情况待查'
def gamepath(asset):return '/Game/'+asset.split('Sifu/Content/',1)[1].removesuffix('.uasset')
def localref(ref):
 if isinstance(ref,str) and ref.startswith('/Game/'):return 'Sifu/Content/'+ref[6:].split('.')[0]+'.uasset'
 return None
def prop(ps,n,idx=0):return next((p for p in ps if p['name']==n and p.get('arrayIndex',0)==idx),None)
def raw(ps,n,idx=0):
 p=prop(ps,n,idx);return p.get('value') if p else None
def nested(ps,n):
 p=prop(ps,n);return p['value'] if p and isinstance(p.get('value'),list) else []
def normalize(ps,refmap=None,prefix=''):
 result={}
 for p in ps:
  k=p['name']+'['+str(p.get('arrayIndex',0))+']';path=prefix+k;v=p.get('value')
  if isinstance(v,list):value=normalize(v,refmap,path+'.')
  elif 'arrayElements' in p:value=[normalize(e,refmap,path+'.'+str(i)+'.') for i,e in enumerate(p['arrayElements'])]
  elif 'tagNames' in p:value=p['tagNames']
  elif 'reference' in p:value={'index':v,'reference':p['reference']}
  elif 'arrayReferences' in p:value=p['arrayReferences']
  elif 'arrayValues' in p:value=p['arrayValues']
  else:value=v
  if refmap and path in refmap:value={'index':v,'reference':refmap[path]}
  result[k]=value
 return result
def leaves(v,prefix=''):
 if isinstance(v,dict) and not any(k in v for k in ['decoded','reference','index']):
  for k,x in v.items():yield from leaves(x,prefix+'.'+k if prefix else k)
 elif isinstance(v,list):
  if not v:yield prefix,[]
  else:
   for i,x in enumerate(v):yield from leaves(x,prefix+'['+str(i)+']')
 else:yield prefix,v
def compact(v):
 if isinstance(v,dict) and v.get('decoded') is False:return '未解码（'+str(v.get('bytes','?'))+' 字节）'
 if isinstance(v,dict) and 'reference' in v:
  ref=v.get('reference')
  if ref:return ref
  return '对象索引 '+str(v.get('index'))+'；未解析引用'
 return cell(v)
def prop_table(data):return tab(['中文标识','原字段路径','保存值／引用','中文说明'],[(field_label(k),k,compact(v),field_note(k)) for k,v in leaves(data)]) if data else '本对象没有保存可列出的覆盖字段；不代表全部数值为零。\n'
def distribution(entries,exclude=()):
 # Lossless membership for all displayed saved leaf fields; repeated values share an explicit row-ID list.
 groups=collections.defaultdict(lambda:collections.defaultdict(list));values={}
 for ident,data in entries:
  for k,v in leaves(data):
   if any(k.startswith(e) for e in exclude):continue
   sig=json.dumps(v,ensure_ascii=False,sort_keys=True);groups[k][sig].append(ident);values[(k,sig)]=v
 rows=[]
 for k,buckets in groups.items():
  for sig,ids in buckets.items():
   rows.append([field_label(k),k,compact(values[(k,sig)]),'本表全部行' if len(ids)==len(entries) else ', '.join(ids)])
 return tab(['中文标识','原字段路径','配置值','适用行 ID'],rows)
def outcome_value(d,flag,value):
 if flag not in d:return '未保存'
 f=d[flag]
 if f is True or str(f).lower()=='true':return '开：'+cell(d.get(value))
 if f is False or str(f).lower()=='false':return '关（保存 '+cell(d.get(value))+'）'
 return '开关未知；保存 '+cell(d.get(value))
def stripkeys(ps):return {p['name']:p.get('value') for p in ps}
def subkey(data,path,default=None):
 for k in path:
  if not isinstance(data,dict) or k not in data:return default
  data=data[k]
 return data
def bound(v):
 if not isinstance(v,dict):return '未保存'
 typ=v.get('Type[0]');value=v.get('Value[0]')
 if typ=='ERangeBoundTypes::Open':return '无界（保存值 '+cell(value)+' 不作端点）'
 return str(typ).split('::')[-1]+': '+cell(value)
def frame_range(v):
 a=v.get('m_FrameRange[0]',{}) if isinstance(v,dict) else {}
 anim=a.get('m_Anim[0]',{})
 return bound(anim.get('LowerBound[0]'))+' → '+bound(anim.get('UpperBound[0]'))
def normalrow(ps):return normalize(ps)
def resolve_index(pkg,index):
 if not index:return None
 if index<0:
  item=pkg['imports'][-index-1]
  if item['outer']==0:return item['name']
  outer=resolve_index(pkg,item['outer'])
  return (outer+'.' if outer else '')+item['name']
 item=pkg['exports'][index-1]
 return gamepath(pkg['path'])+'.'+item['name']
parser=argparse.ArgumentParser();parser.add_argument('--check',action='store_true');args=parser.parse_args()
tables=gz('data-tables.json.gz');objects=gz('tagged-objects.json.gz');cdos=gz('stun-ai-default-objects.json.gz');packages=gz('package-metadata.json.gz')
reactions=readcsv('state-reaction-settings.csv');matrices=readcsv('state-resistance-matrices.csv')
pkgmap={p['path']:p for p in packages};byasset=collections.defaultdict(list)
for o in objects:byasset[o['asset']].append(o)
hit_tables=[t for t in tables if any(p.get('reference')=='/Script/Sifu.HitboxDataRow' for p in t['properties'])]
anim_tables=[t for t in tables if any(p.get('reference')=='/Script/Sifu.AttackDataRow' for p in t['properties'])]
attack_objects=[o for o in objects if o['class'].endswith('.AttackDB')]
resistance=[o for o in objects if o['class'].endswith('.AttackPropertiesResistanceDB')]
contexts=[o for o in objects if o['class'].endswith('.AIContextualDefense')]
tickets=json.loads((ROOT/'exports/ai-attack-tickets.json').read_text(encoding='utf-8'))
hitted=[o for o in objects if o['class'].endswith('.HittedDB')]
parents={}
for pkg in packages:
 for e in pkg['exports']:
  if e['name'].endswith('_C') and e.get('superIndex'):
   parents[gamepath(pkg['path'])+'.'+e['name']]=resolve_index(pkg,e['superIndex'])
def ancestry(ref):
 seen=set();chain=[]
 while ref and ref not in seen:
  seen.add(ref);chain.append(ref);ref=parents.get(ref)
 return chain
archetypes=[]
for o in cdos:
 cls=gamepath(o['asset'])+'.'+o['class']
 if '/Script/Sifu.ArchetypeAsset' in ancestry(cls):
  archetypes.append(o)
docs={};stats={};catalog_map={};records={};source_assets={}
categories=collections.defaultdict(list)
def add(path,text,counts=None):
 if path in docs:raise ValueError('Duplicate document '+path)
 docs[path]=text.rstrip()+'\n'
 if counts:records[path]=counts
def docpath(category,asset):return OUT+'/'+category+'/'+name(asset)+'-'+hashlib.sha256(asset.encode()).hexdigest()[:6]+'.md'
def nav(mechanism=None):
 s=wl(OUT+'/配置索引','返回配置索引')+' · '+wl(OUT+'/覆盖范围与读表说明','覆盖范围与读表说明')
 if mechanism:s+=' · '+wl('01机制/'+mechanism,'基础机制')
 return s+'\n\n'
for t in hit_tables:
 category='玩家攻击' if group(t['asset'])=='玩家' else ('共享攻击' if group(t['asset'])=='共享' else '敌人攻击')
 p=docpath(category,t['asset']);catalog_map[t['asset']]=p;categories[category].append((t['asset'],p,len(t['rows'])))
for o in resistance:
 p=docpath('受击与抗性',o['asset']);catalog_map[o['asset']]=p;categories['受击与抗性'].append((o['asset'],p,1))
for o in contexts:
 p=docpath('AI防御',o['asset']);catalog_map[o['asset']]=p;categories['AI防御'].append((o['asset'],p,len(byasset[o['asset']])))
for t in anim_tables:
 p=docpath('动作与时序',t['asset']);catalog_map[t['asset']]=p;categories['动画配置表'].append((t['asset'],p,len(t['rows'])))
def linkedref(ref):
 asset=localref(ref)
 return wl(catalog_map[asset],ref) if asset in catalog_map else (ref or '本资产未保存；可能继承')
# Hitbox catalogs: every decoded hit row, all three outcomes, complete remaining saved fields.
hit_keys=set();hit_outcome_keys=set()
for t in hit_tables:
 p=catalog_map[t['asset']];rows=t['rows'];normalized=[(f'H{i+1:03}',r['row'],normalize(r['properties'])) for i,r in enumerate(rows)]
 text='# '+name(t['asset'])+'：攻击效果配置\n\n'+nav('攻击冲击力韧性与伤害')
 text+='来源资产：'+t['asset']+'\n\n本页收录本表全部 '+str(len(rows))+' 条已解析 HitBox 行，覆盖普通命中、格挡、弹开三种配置。行 ID 只在本页内定位，不代表独立招式；所有值均非最终实战结果。\n'
 base=[]
 for ident,n,d in normalized:
  hit_keys.add((t['asset'],n))
  base.append([ident,n,d.get('m_eHitType[0]'),d.get('m_eAttackPower[0]'),outcome_value({k.removesuffix('[0]'):v for k,v in d.items()},'m_bOverrideResilience','m_iOverrideResilienceValue'),d.get('m_bParriable[0]'),d.get('m_bDizzyOnParry[0]'),d.get('m_bDizzyOnAvoid[0]')])
 text+='\n## 行索引与韧性相关配置\n'+tab(['行 ID','HitBox 行名','命中种类','攻击强度','韧性覆盖','可招架标志','Parry 时眩晕标志','Avoid 时眩晕标志'],base)
 text+='“Parry／Avoid 时眩晕”列仅报告字段，不足以断言用户的防反／闪避反击追击窗口已经解释完成。\n'
 for field,title in [('m_OnHitImpact','普通命中'),('m_OnGuardImpact','格挡'),('m_OnDeflectImpact','弹开')]:
  out=[]
  for ident,n,d in normalized:
   src=next(r for r in rows if r['row']==n);ps=nested(src['properties'],field);v=stripkeys(ps)
   if ps:hit_outcome_keys.add((t['asset'],n,field))
   out.append([ident,outcome_value(v,'m_bUseDamage','m_fDamage'),outcome_value(v,'m_bUseStructureDamage','m_fStructureDamage'),outcome_value(v,'m_bUseSuperDizzyDamage','m_fSuperDizzyDamage'),outcome_value(v,'m_bUseNbFrameStuned','m_iNbFrameStuned'),outcome_value(v,'m_bUseKnockBackDistance','m_fKnockBackDistance'),outcome_value(v,'m_bUseFreezeFrames','m_iFreezeFrames')])
  text+='\n## '+title+'效果\n'+tab(['行 ID','生命伤害','架势伤害','特殊眩晕伤害字段','受击帧','击退距离字段','停顿帧'],out)
  if field=='m_OnDeflectImpact':
   out=[]
   for ident,n,d in normalized:
    v=stripkeys(nested(next(r for r in rows if r['row']==n)['properties'],field))
    out.append([ident,outcome_value(v,'m_bUseSelfStructureDamage','m_fSelfStructureDamage'),outcome_value(v,'m_bUseSelfSuperDizzyDamage','m_fSelfSuperDizzyDamage'),v.get('m_bSelfStructureDamageCanGuardBreak'),v.get('m_KnockBackDynamic')])
   text+='\n## 弹开结果中的自身影响字段\n\nSelf 的具体作用对象应结合命中执行路径，不能直接把它加到被击者伤害上。\n'+tab(['行 ID','自身架势伤害字段','自身特殊眩晕伤害字段','自身架势伤害可破防标志','动态击退模式原值'],out)
 # Full serialized fields grouped by exact source value; scalar outcomes displayed above are excluded only if already represented.
 text+='\n## 其他保存参数与特殊反应配置\n\n同值参数按适用行 ID 合并；包含攻击属性等级、持续时间／距离开关、状态覆盖、命中筛选、击退行为和防御矩阵等已保存字段。未解码项明确保留。以下也补留各命中结果中未在前表显示的字段。\n'
 summary_exclude=['m_eHitType[0]','m_eAttackPower[0]','m_bOverrideResilience[0]','m_iOverrideResilienceValue[0]','m_bParriable[0]','m_bDizzyOnParry[0]','m_bDizzyOnAvoid[0]']
 shown=['m_bUseDamage','m_fDamage','m_bUseStructureDamage','m_fStructureDamage','m_bUseSuperDizzyDamage','m_fSuperDizzyDamage','m_bUseNbFrameStuned','m_iNbFrameStuned','m_bUseKnockBackDistance','m_fKnockBackDistance','m_bUseFreezeFrames','m_iFreezeFrames']
 summary_exclude += [x+'[0].'+k+'[0]' for x in ['m_OnHitImpact','m_OnGuardImpact','m_OnDeflectImpact'] for k in shown]
 text+=distribution([(i,d) for i,n,d in normalized],summary_exclude)
 text+='\n原始行与字段见 inventory/data-tables.json.gz；三结果数值导出见 exports/hit-impact-values.csv。表名和资源类别仅用于查找，当前是否实战调用需沿动作引用核对。\n'
 add(p,text,{'kind':'hitbox','asset':t['asset'],'rows':len(rows),'outcomes':sum(1 for a,n,k in hit_outcome_keys if a==t['asset'])})
# Resistance, full saved reaction trees plus 9-row matrices and scalar comparison.
reaction_names={'m_DownReaction':'倒地','m_DizzyReaction':'眩晕','m_PushedReaction':'推退','m_SuperDizzyReaction':'特殊眩晕','m_StructureBrokenReaction':'架势破坏'}
for o in resistance:
 asset=o['asset'];p=catalog_map[asset];rr=[x for x in reactions if x['asset']==asset];mm=[x for x in matrices if x['asset']==asset]
 text='# '+name(asset)+'：受击与抗性配置\n\n'+nav('受击硬直与脱离')+'来源资产：'+asset+'\n\n这是资产自身保存的配置，不是每个引用者最终生效值；命中计数不能直接换算为拳数，普通硬直不套用眩晕计数。\n'
 text+='\n## 反应限制对照\n'+tab(['反应','累计伤害上限原值','累计命中上限原值','按攻击名合并','保留当前持续时间','持久标志','允许普通眩晕叠加','强制时长字段','时长字段'],[[reaction_names.get(x['reaction'],x['reaction']),x.get('m_fMaxAccumulatedDamage'),x.get('m_iMaxAccumatedHits'),x.get('m_bGroupMaxAccumulatedHitsByAttack'),x.get('m_bAlwayKeepCurrentStateDurationOnHit'),x.get('m_bIsPersistent'),x.get('m_bAllowDizzyOnTopOfDizzy'),x.get('m_fMandatoryDuration'),x.get('m_fDuration')] for x in rr])
 text+='伤害上限 >0 才启用相应累计伤害退出检查；命中上限的更新与递增条件不完全相同。-1 等原值保留，具体解释见基础机制，不能把未保存字段补成 0。\n'
 text+='\n## 按当前状态的抗性矩阵\n'+tab(['状态','倒地抗性','推退抗性','眩晕抗性','自定义时长开关／值','使用受击动画时长','保留当前状态时长','保留阈值','自定义距离开关／值'],[[x['state'],x['knockdown_resistance_col0'],x['push_resistance_col1'],x['dizzy_resistance_col2'],str(x.get('m_bUseCustomDuration'))+' / '+str(x.get('m_fCustomDuration')),x.get('m_bUseHitAnimDuration'),x.get('m_bKeepCurrentStateDuration'),x.get('m_fKeepCurrentStateThresold'),str(x.get('m_bUseCustomDistance'))+' / '+str(x.get('m_fCustomDistance'))] for x in mm])
 text+='\n## 本资产全部已解析保存字段\n\n包含前表未展开的恢复动作、条件、图引用和其他字段。对象索引若尚未解析，不把索引当数值参数。\n'+prop_table(normalize(o['properties']))
 text+='\n来源：inventory/tagged-objects.json.gz；exports/state-reaction-settings.csv；exports/state-resistance-matrices.csv。引用到具体敌人的关系见 '+wl(OUT+'/敌人原型/索引')+'。\n'
 add(p,text,{'kind':'resistance','asset':asset,'reaction_rows':len(rr),'matrix_rows':len(mm)})
# Defense configuration graphs: root nodes, every test sequence, every object's saved fields.
context_objects=0;memory_tests=0;sequence_count=0
for o in contexts:
 asset=o['asset'];p=catalog_map[asset];allobj=byasset[asset];seq=[x for x in allobj if x['class'].endswith('.AIInfluence_TestSequence')];mem=[x for x in allobj if x['class'].endswith('.AttackMemoryInfluenceTest')]
 context_objects+=len(allobj);memory_tests+=len(mem);sequence_count+=len(seq)
 text='# '+name(asset)+'：AI 防御配置\n\n'+nav('敌人如何选择防御')+'来源资产：'+asset+'\n\n收录本资产全部 '+str(len(allobj))+' 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。\n'
 text+='\n## 图入口保存字段\n'+prop_table(normalize(o['properties']))
 text+='\n## 全部测试序列与连接\n'+tab(['序列对象','节点索引','测试引用（需共同通过，含各自反转）','关联后继节点'],[[x['export'],raw(x['properties'],'m_iNodeIndex'),compact(normalize(x['properties']).get('m_Tests[0]')),compact(normalize(x['properties']).get('m_LinkedNodes[0]'))] for x in seq])
 text+='\n## 全部攻击记忆测试\n'+tab(['对象','记忆时间字段','计数阈值','攻击标签','命中掩码原值','反转字段','闪避标志'],[[x['export'],raw(x['properties'],'m_fMemoryLimit'),raw(x['properties'],'m_uiHitsCount'),compact(normalize(x['properties']).get('m_AttackProperties[0]')),raw(x['properties'],'m_HitTypes'),raw(x['properties'],'m_bInverted'),raw(x['properties'],'m_bDodged')] for x in mem])
 text+='\n## 全部对象的保存配置\n\n下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。\n'
 for x in allobj:
  text+='\n### '+x['export']+'\n\n类：'+x['class']+'\n'+prop_table(normalize(x['properties']))
 text+='\n来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。\n'
 add(p,text,{'kind':'context','asset':asset,'objects':len(allobj),'sequences':len(seq),'memory_tests':len(mem)})
# Archetype catalogs: establish actual class ancestry rather than filename heuristic.
archetype_groups=collections.defaultdict(list)
for o in archetypes:archetype_groups[group(o['asset'])].append(o)
for g,items in archetype_groups.items():
 for o in items:
  catalog_map[o['asset']]=OUT+'/敌人原型/'+g+'.md#'+name(o['asset'])+'-'+hashlib.sha256(o['asset'].encode()).hexdigest()[:6]
for g,items in sorted(archetype_groups.items()):
 p=OUT+'/敌人原型/'+g+'.md';categories['敌人原型'].append((g,p,len(items)))
 def objanchor(o):return name(o['asset'])+'-'+hashlib.sha256(o['asset'].encode()).hexdigest()[:6]
 for o in items:catalog_map[o['asset']]=p+'#'+objanchor(o)
 text='# '+g+'：原型配置与引用\n\n'+nav('受击硬直与脱离')
 text+='纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。\n'
 rows=[]
 for o in items:
  refs={x['property']:x['ref'] for x in o.get('object_references',[])}
  cls=gamepath(o['asset'])+'.'+o['class'];parent=parents.get(cls)
  rows.append([wl(p+'#'+objanchor(o),name(o['asset'])),scope(o['asset']),linkedref(parent),raw(o['properties'],'m_fHealth'),raw(o['properties'],'m_fStructure'),linkedref(refs.get('m_AttackPropertyResistanceDBPerDifficulty[0]')),linkedref(refs.get('m_ContextualDefense[0]'))])
 text+='\n## 原型差异总表\n'+tab(['原型','路径范围标签','父类','本层生命字段','本层架势字段','普通难度抗性引用','情境防御引用'],rows)
 for o in items:
  refs={x['property']:x['ref'] for x in o.get('object_references',[])}
  text+='\n## '+objanchor(o)+'\n\n来源资产：'+o['asset']+'\n\n父类：'+linkedref(parents.get(gamepath(o['asset'])+'.'+o['class']))+'\n'
  text+='\n### 难度抗性与防御引用\n'+tab(['字段／难度','本层保存的引用'],[[label,linkedref(refs.get(key))] for label,key in [('普通 Normal=0','m_AttackPropertyResistanceDBPerDifficulty[0]'),('简单 Easy=1','m_AttackPropertyResistanceDBPerDifficulty[1]'),('困难 Hard=2','m_AttackPropertyResistanceDBPerDifficulty[2]'),('情境防御','m_ContextualDefense[0]')]])
  text+='\n### 本层全部已解析保存字段\n'+prop_table(normalize(o['properties'],refs))
 text+='\n来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。\n'
 add(p,text,{'kind':'archetype','objects':len(items)})
# AttackDB resources: every decoded player and enemy object, all saved Attack fields and timing windows.
ungrouped=collections.defaultdict(list)
for o in attack_objects:
 g=group(o['asset'])
 if g=='玩家':
  parts=o['asset'].split('/Combos/Attacks/',1)[-1].split('/')
  g='玩家-'+('-'.join(parts[:2]) if len(parts)>2 else parts[0])
 ungrouped[g].append(o)
attack_groups={}
for g,items in sorted(ungrouped.items()):
 for offset in range(0,len(items),20):
  label=g if len(items)<=20 else g+'-'+str(offset//20+1).zfill(2)
  attack_groups[label]=items[offset:offset+20]
attack_hitbox_links=[];attack_rows=set();attack_window_count=0;availability_count=0
for g,items in sorted(attack_groups.items()):
 p=OUT+'/动作与时序/'+g+'-动作资源.md';categories['动作资源'].append((g,p,len(items)))
 text='# '+g+'：全部已解析动作资源\n\n'+nav('攻击冲击力韧性与伤害')
 text+='本页列出 '+str(len(items))+' 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。\n'
 info=[];details=[]
 for i,o in enumerate(items):
  ident=f'A{i+1:03}';a=nested(o['properties'],'m_Attack');d=normalize(a);rh=d.get('m_AnimationRow[0]',{});animref=subkey(rh,['DataTable[0]','reference']);animrow=rh.get('RowName[0]')
  boxes=prop(a,'m_HitBoxes');boxitems=boxes.get('arrayElements',[]) if boxes else [];wins=prop(a,'m_AvailabilityLayerWindows');winitems=wins.get('arrayElements',[]) if wins else []
  attack_window_count+=len(boxitems);availability_count+=len(winitems);attack_rows.add(o['asset'])
  anchor=ident+'-'+name(o['asset'])
  info.append([wl(p+'#'+anchor,ident+' '+name(o['asset'])),scope(o['asset']),linkedref(animref),animrow,raw(a,'m_fAnimFrameRate'),raw(a,'m_iWantedBuildupFrames'),len(boxitems) if boxes and 'arrayElements' in boxes else '未保存／未解码',len(winitems) if wins and 'arrayElements' in wins else '未保存／未解码'])
  part='\n## '+anchor+'\n\n来源资产：'+o['asset']+'\n\n导出对象：'+o['export']+'\n'
  if boxitems:
   rr=[]
   for j,props in enumerate(boxitems):
    box=normalize(props);hit=box.get('m_HitRow[0]',{});ref=subkey(hit,['DataTable[0]','reference']);row=hit.get('RowName[0]');asset=localref(ref)
    attack_hitbox_links.append({'attack':o['asset'],'index':j,'hitbox_asset':asset,'row':row,'parsed_target':(asset,row) in hit_keys})
    rr.append([j,linkedref(ref),row,frame_range(box),box.get('m_eHitTarget[0]'),box.get('m_eMovementType[0]'),box.get('m_eOrigin[0]'),compact(box.get('m_activationCondition[0]'))])
   part+='\n### 保存的命中窗口与效果行关联\n'+tab(['序号','HitBox 表','行名','帧区间与端点类型','命中目标高度字段','动作类型字段','来源方向字段','激活条件原值'],rr)
  if winitems:
   rr=[]
   for j,props in enumerate(winitems):
    win=normalize(props);ref=subkey(win,['m_Layer[0]','reference'])
    rr.append([j,frame_range(win),win.get('m_uiHitConditions[0]'),linkedref(ref)])
   part+='\n### 保存的动作许可窗口\n'+tab(['序号','帧区间与端点类型','命中条件掩码原值','动作层引用'],rr)
  part+='\n### 本对象全部已解析保存字段\n'+prop_table(normalize(o['properties']))
  details.append(part)
 text+='\n## 动作索引\n'+tab(['动作资源','路径范围标签','动画行表','动画行名','保存帧率','期望前摇帧字段','已解析命中窗口数','已解析许可窗口数'],info)+''.join(details)
 text+='\n来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。\n'
 add(p,text,{'kind':'attackdb','objects':len(items)})
# Animation-row data tables: all 17 tables, not just the two example attacks.
for t in anim_tables:
 p=catalog_map[t['asset']];entries=[];summary=[]
 text='# '+name(t['asset'])+'：动画行配置\n\n'+nav('攻击冲击力韧性与伤害')+'来源资产：'+t['asset']+'\n\n收录本表全部 '+str(len(t['rows']))+' 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。\n'
 for i,r in enumerate(t['rows']):
  ident=f'T{i+1:03}';d=normalize(r['properties']);entries.append((ident,d));summary.append([ident,r['row'],d.get('m_iLastBuildupFrame[0]'),d.get('m_fHitFrame[0]'),compact(d.get('m_Animation[0]'))])
 text+='\n## 全部动画行\n'+tab(['行 ID','动画行名','最后前摇帧字段','命中帧字段','动画引用字段'],summary)
 text+='\n## 全部保存字段的配置分布\n\n同值字段按适用行 ID 合并，保留全部已解析字段。行 ID 在本页内有效。\n'+distribution(entries)
 text+='\n来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 '+wl(OUT+'/动作与时序/索引')+'。\n'
 add(p,text,{'kind':'animation','asset':t['asset'],'rows':len(t['rows'])})
# Shared hitted/recovery configuration, full saved fields.
p=OUT+'/受击恢复/受击与恢复配置.md'
text='# 受击与恢复配置\n\n'+nav('受击硬直与脱离')
text+='收录所有已解析的 HittedDB 对象及已经独立核对的两套动作恢复白名单。动画选择、硬直计时与持续状态分开理解，引用原值不等于已恢复完整选择算法。\n'
text+=tab(['受击数据库','族群','来源资产'],[[wl(p+'#'+name(o['asset']),name(o['asset'])),group(o['asset']),o['asset']] for o in hitted])
for o in hitted:text+='\n## '+name(o['asset'])+'\n\n来源资产：'+o['asset']+'\n'+prop_table(normalize(o['properties']))
stun=json.loads((ROOT/'inventory/stun-state-data.json').read_text(encoding='utf-8'))
text+='\n## 已核对的恢复动作层\n'+tab(['资产','动作名单','掩码含义','范围'],[[x['asset'],', '.join(x['actions']),'非反选白名单；SET 加入当前上下文','其他上下文仍可能限制最终许可'] for x in stun['recovery_layers']])
text+='\n来源：inventory/tagged-objects.json.gz；inventory/stun-state-data.json；inventory/stun-ai-layer-semantics-disassembly.json。\n'
add(p,text,{'kind':'hitted','objects':len(hitted),'verified_layers':len(stun['recovery_layers'])});categories['受击恢复'].append(('HittedDB 与动作恢复层',p,len(hitted)))
# Ticket configs, all 50 assets.
p=OUT+'/群体票据/攻击票据配置.md';text='# 全部已提取攻击票据配置\n\n'+nav('群体AI与状态反馈')
text+='收录全部 '+str(len(tickets))+' 个已提取票据配置。难度索引和 domination 阶段分别保留；单票据 count 不能解释全场同时攻击人数，原始角色掩码与 Joker 行为不提前翻译成已证实的调度结论。\n'
text+='\n## 票据对照\n'+tab(['票据','行为','角色掩码原值','基础数量','普通数量','简单数量','困难数量','来源资产'],[[wl(p+'#'+name(x['asset']),name(x['asset'])),x['config'].get('m_eBehavior[0]'),x['config'].get('m_eCombatRolesMask[0]'),x['config'].get('m_iCount[0]'),x['config'].get('m_iCountPerDifficulty[0]'),x['config'].get('m_iCountPerDifficulty[1]'),x['config'].get('m_iCountPerDifficulty[2]'),x['asset']] for x in tickets])
for x in tickets:text+='\n## '+name(x['asset'])+'\n\n来源资产：'+x['asset']+'\n'+prop_table(x['config'])
text+='\n来源：exports/ai-attack-tickets.json。保存字段均已列出；未保存字段不补零，冷却最终何时触发仍须结合基础机制中的调用链。\n'
add(p,text,{'kind':'tickets','objects':len(tickets)});categories['群体票据'].append(('全部攻击票据',p,len(tickets)))
# Per-category indexes, explicit IDs, paths and complete counts.
for category,entries in categories.items():
 directory='动作与时序' if category in ['动作资源','动画配置表'] else category
 if category in ['动作资源','动画配置表']:continue
 p=OUT+'/'+directory+'/索引.md'
 text='# '+category+'配置索引\n\n'+nav()
 if category=='玩家攻击':text+='优先阅读：'+wl(OUT+'/玩家攻击/阅读入口','输入衔接图、中文字段与招式伤害对照')+'。\n\n'
 text+='以下列出当前已解析集合的全部条目。资源名、目录范围和配置事实不自动等于实战中文招式名、敌人最终属性或当前调用状态。\n'
 text+=tab(['资源／组','族群','条目／对象数','路径范围标签','详细配置'],[[a,group(a) if a.endswith('.uasset') else a,n,scope(a) if a.endswith('.uasset') else '组内逐项标记',wl(path,'打开配置')] for a,path,n in entries])
 add(p,text)
p=OUT+'/动作与时序/索引.md'
text='# 动作资源与动画表索引\n\n'+nav()+'动作资源、动画行、HitBox 行是三个层次，分别列出，避免把多段命中行数当作招式数。玩家输入衔接图另见玩家攻击目录，保留配置连接与运行时边界的区别。\n'
for cat in ['动作资源','动画配置表']:
 text+='\n## '+cat+'\n'+tab(['资源／组','对象／行数','详细配置'],[[a,n,wl(path,'打开配置')] for a,path,n in categories[cat]])
add(p,text)
# Coverage is computed against the admitted parsed collection, not filename guesses or all shipping content.
csv_hit=readcsv('hit-impact-values.csv');csv_keys={(x['asset'],x['row'],x['outcome']) for x in csv_hit}
assert csv_keys==hit_outcome_keys, 'CSV and tagged HitBox outcomes differ'
assert len(hit_keys)==sum(len(t['rows']) for t in hit_tables),'Duplicate HitBox row identity'
assert len(attack_rows)==len(attack_objects),'Duplicate AttackDB asset identity'
source_paths=['inventory/data-tables.json.gz','inventory/tagged-objects.json.gz','inventory/stun-ai-default-objects.json.gz','inventory/package-metadata.json.gz','inventory/deep-parse-overview.json','exports/hit-impact-values.csv','exports/state-reaction-settings.csv','exports/state-resistance-matrices.csv','exports/ai-attack-tickets.json','inventory/stun-state-data.json','exports/player-field-labels.json']
inputs={p:sha(ROOT/p) for p in source_paths}
stats={'hitbox_tables':len(hit_tables),'hitbox_rows':len(hit_keys),'hitbox_outcome_rows':len(hit_outcome_keys),'player_hitbox_rows':sum(len(t['rows']) for t in hit_tables if group(t['asset'])=='玩家'),'enemy_hitbox_rows':sum(len(t['rows']) for t in hit_tables if group(t['asset']) not in ['玩家','共享']),'shared_hitbox_rows':sum(len(t['rows']) for t in hit_tables if group(t['asset'])=='共享'),'attackdb_objects':len(attack_objects),'player_attackdb_objects':sum(1 for o in attack_objects if group(o['asset'])=='玩家'),'enemy_attackdb_objects':sum(1 for o in attack_objects if group(o['asset']) not in ['玩家','共享']),'parsed_hitbox_windows':attack_window_count,'parsed_availability_windows':availability_count,'animation_tables':len(anim_tables),'animation_rows':sum(len(t['rows']) for t in anim_tables),'resistance_assets':len(resistance),'reaction_rows':len(reactions),'matrix_rows':len(matrices),'contextual_defense_assets':len(contexts),'contextual_defense_objects':context_objects,'attack_memory_tests':memory_tests,'test_sequences':sequence_count,'archetype_cdos_with_verified_ancestry':len(archetypes),'attack_ticket_assets':len(tickets),'hitted_db_objects':len(hitted),'unresolved_attack_hitbox_links':sum(not x['parsed_target'] for x in attack_hitbox_links)}
overview=json.loads((ROOT/'inventory/deep-parse-overview.json').read_text(encoding='utf-8'))
coverage='# 覆盖范围与读表说明\n\n'+nav()+'## 已收录范围\n'
coverage+=tab(['对象集合','当前数量','“完整”适用于哪个范围'],[
['攻击效果表／HitBox 行／三结果配置',str(stats['hitbox_tables'])+' / '+str(stats['hitbox_rows'])+' / '+str(stats['hitbox_outcome_rows']),'全部已解析 HitboxDataRow 表，按资产＋行＋结果逐项核对'],
['玩家／敌人／共享 HitBox 行',str(stats['player_hitbox_rows'])+' / '+str(stats['enemy_hitbox_rows'])+' / '+str(stats['shared_hitbox_rows']),'按资源路径分类，不等于独立招式数量'],
['动作资源 AttackDB',str(len(attack_objects))+'（玩家 '+str(stats['player_attackdb_objects'])+'）','全部解析成功的该类对象；保留旧版和测试等资源'],
['已解析命中／动作许可窗口',str(attack_window_count)+' / '+str(availability_count),'来自上述全部 AttackDB 的可解码结构数组'],
['动画表／动画行',str(len(anim_tables))+' / '+str(stats['animation_rows']),'全部解析成功的 AttackDataRow 表'],
['受击／抗性资产、反应组、矩阵行',str(len(resistance))+' / '+str(len(reactions))+' / '+str(len(matrices)),'当前已解析集合全量'],
['情境防御图／图内对象／测试序列',str(len(contexts))+' / '+str(context_objects)+' / '+str(sequence_count),'对应资产内全部已解析对象；图可达性和最终选择未穷尽'],
['攻击记忆测试',memory_tests,'上述情境图中该类型的全部已解析对象'],
['原型 CDO',len(archetypes),'元数据父类链确认为 ArchetypeAsset，列本层覆盖而非合并后最终值'],
['攻击票据／受击数据库',str(len(tickets))+' / '+str(len(hitted)),'当前已提取票据及已解析 HittedDB']])
coverage+='## 统一读表约定\n'+tab(['标记／列','含义'],[
['开：数值','保存的启用开关为真；仍不是最终实战结果'],
['关（保存 数值）','开关为假，保留其保存值供比较；不能把该值直接套到结果'],
['未保存','当前对象没有该字段；可能继承默认值，不能补零'],
['未解码（N 字节）','存在保存数据，但当前解析器不能解释内部结构'],
['对象索引 N；未解析引用','这是对象引用索引，不能当成状态、伤害或时间'],
['行 ID','只用于当前表内定位；与原始行名一起使用'],
['同值字段按适用行合并','列明全部适用 ID，不省略不同配置；不是运行时合并'],
['浮点显示','使用紧凑数值显示；完整二进制转出的数值留在外部原始数据'],
['帧与范围端点','保留 Inclusive／Exclusive／Open；Open 的保存数值不是有效端点'],
['原型本层字段','未合并父类，父类关系和引用另列'],
['路径范围标签','只说明旧目录、测试、竞技场等路径特征，不认定当前实际启用'],
['资源英文名','尚未全部映射中文招式／敌人显示名，保留可追溯原名']])
coverage+='## 尚未覆盖或未验证\n'+tab(['缺口','目前情况／后续工作'],[
['全部游戏资源','当前解析集合不是整包所有逻辑；早期全体解析记录仍有 '+str(overview.get('opaque_or_unsupported_export_count'))+' 个不透明或不支持的导出记录，不能将该数直接当本目录缺失的招式数'],
['敌人有效属性','已建立原型父类链与本层配置；父级、原生默认值和运行期修正仍未统一求值'],
['未解码数组、映射与复杂结构','逐处保留标记；按问题补解析，不猜具体内容'],
['动作到 HitBox 关联缺口',str(stats['unresolved_attack_hitbox_links'])+' 条已解析命中窗口尚未对上当前 HitBox 集合；可为缺少引用、空引用或未解析目标，详见外部覆盖报告'],
['所有中文招式名和实际可用性','需要逐项映射；旧路径与测试资源不当现行招式'],
['临时韧性服务的具体挂载','已有机制证据，但当前配置集合仍未接到所有具体动作'],
['防反与闪避反击的追击窗口','新目录列出差异配置，尚不证明完整起止机制'],
['实战数值','未运行游戏；伤害、硬直、架势、冷却等保存值不冒充实战验收']])
coverage+='## 尚未对上的动作命中引用\n'+tab(['动作资源','窗口序号','引用表','行名','路径范围标签'],[[x['attack'],x['index'],x['hitbox_asset'],x['row'],scope(x['attack'])] for x in attack_hitbox_links if not x['parsed_target']])
coverage+='## 原始依据\n'+tab(['研究根目录中的文件','用途'],[[p,'生成时记录 SHA-256；详见 inventory/configuration-catalog-coverage.json'] for p in source_paths])
coverage+='自动检查还会比较全部 855 条 HitBox 行及三种结果的身份集合、生成文本与源数据的一致性、文档链接和原型筛选依据。它不验证游戏行为。\n'
add(OUT+'/覆盖范围与读表说明.md',coverage)
index='# 机制配置索引\n\n'+wl('00索引/首页','返回首页')+' · '+wl(OUT+'/覆盖范围与读表说明','覆盖范围与读表说明')+'\n\n基础机制解释规则，本目录记录同一规则下不同角色、武器、状态、动作与 AI 图的配置差异。所有“全量”仅指当前解析成功的对应集合，未把少数样本当全部招式。\n'
index+=tab(['配置主题','收录内容','入口','对应基础机制'],[
['玩家攻击',str(stats['player_hitbox_rows'])+' 条 HitBox 行，按效果表分组',wl(OUT+'/玩家攻击/索引'),wl('01机制/攻击冲击力韧性与伤害')],
['敌人攻击',str(stats['enemy_hitbox_rows'])+' 条 HitBox 行，按族群／武器分组',wl(OUT+'/敌人攻击/索引'),wl('01机制/攻击冲击力韧性与伤害')],
['共享攻击',str(stats['shared_hitbox_rows'])+' 条共享／Focus／通用效果行',wl(OUT+'/共享攻击/索引'),wl('01机制/攻击冲击力韧性与伤害')],
['动作与时序',str(len(attack_objects))+' 个动作资源、'+str(stats['animation_rows'])+' 条动画行及保存的命中／许可窗口',wl(OUT+'/动作与时序/索引'),wl('01机制/攻击冲击力韧性与伤害')],
['受击与抗性',str(len(resistance))+' 套反应配置与状态矩阵',wl(OUT+'/受击与抗性/索引'),wl('01机制/受击硬直与脱离')],
['敌人原型',str(len(archetypes))+' 个父类链已核对的原型，含本层属性与配置引用',wl(OUT+'/敌人原型/索引'),wl('01机制/受击硬直与脱离')],
['AI 防御',str(len(contexts))+' 套情境图、全部测试／节点配置',wl(OUT+'/AI防御/索引'),wl('01机制/敌人如何选择防御')],
['受击恢复',str(len(hitted))+' 套 HittedDB 及已核对的动作恢复层',wl(OUT+'/受击恢复/索引'),wl('01机制/受击硬直与脱离')],
['群体票据',str(len(tickets))+' 套攻击票据，难度与阶段冷却分别保留',wl(OUT+'/群体票据/索引'),wl('01机制/群体AI与状态反馈')]])
index+='## 建议查找方式\n'+tab(['想查什么','从哪里开始'],[
['玩家某个攻击的伤害／硬直／韧性阈值','先查动作资源中的 HitBox 引用，再去对应效果表按原始行名定位'],
['普通与进阶杂兵为何表现不同','先查 Grunt 原型本层和父类引用，再对照抗性数据库与情境图'],
['某敌人招架、闪避或记忆条件','查该敌人情境防御图的全部序列、测试和节点字段'],
['眩晕或倒地怎样退出','查受击抗性对应资产的反应上限、状态矩阵及恢复动作字段'],
['为什么有字段空白或未解码','先读覆盖范围与说明，不将缺省值当零，也不把对象索引当数值']])
index+='更新：2026-10-28。生成脚本：scripts/build_configuration_catalog.py。原始明细和覆盖报告仍保留在研究目录。\n'
add(OUT+'/配置索引.md',index)
# All links must point to an existing/new document and heading, checked again by shared verifier.
sources={p:sha(ROOT/p) for p in source_paths}
catalog_report={'date':'2026-10-28','scope':'All admitted objects/rows of the listed parsed collections, not all shipped moves or effective runtime configs.','statistics':stats,'input_sha256':sources,'documents':{p:{'sha256':hashlib.sha256(s.encode('utf-8')).hexdigest(),'bytes':len(s.encode('utf-8')),**records.get(p,{})} for p,s in docs.items()},'attack_hitbox_references':attack_hitbox_links,'evidence_assertions':{'hitbox_row_outcome_identity_sets_match_existing_csv':csv_keys==hit_outcome_keys,'archetypes_verified_by_class_ancestry':True},'runtime_verified':False}
manifest=ROOT/'inventory/configuration-catalog-coverage.json'
if args.check:
 saved=json.loads(manifest.read_text(encoding='utf-8'));failures=[]
 if saved['input_sha256']!=sources:failures.append('Source data changed since generation')
 if saved['statistics']!=stats:failures.append('Coverage statistics differ')
 for p,s in docs.items():
  target=VAULT/p
  if not target.is_file() or target.read_text(encoding='utf-8')!=s:failures.append('Generated content differs: '+p)
 if set(saved['documents'])!=set(docs):failures.append('Catalog document set differs')
 print(json.dumps({'status':'passed' if not failures else 'failed','generated_documents_checked':len(docs),'statistics':stats,'errors':failures},ensure_ascii=True))
 raise SystemExit(bool(failures))
old_report=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else None
obsolete=set(old_report['documents'])-set(docs) if old_report else set()
for oldpath in obsolete:
 target=VAULT/oldpath
 if not target.resolve().is_relative_to((VAULT/OUT).resolve()):raise RuntimeError('Unsafe obsolete path')
 if not target.is_file() or hashlib.sha256(target.read_text(encoding='utf-8').encode('utf-8')).hexdigest()!=old_report['documents'][oldpath]['sha256']:raise RuntimeError('Protect edited obsolete file: '+oldpath)

for p,s in docs.items():
 target=VAULT/p
 if not target.resolve().is_relative_to((VAULT/OUT).resolve()):raise ValueError('Outside catalog')
 if target.exists() and (not old_report or p not in old_report['documents'] or hashlib.sha256(target.read_text(encoding='utf-8').encode('utf-8')).hexdigest()!=old_report['documents'][p]['sha256']):raise RuntimeError('Protect user-edited catalog: '+p)
for p,s in docs.items():
 target=VAULT/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s,encoding='utf-8',newline=chr(10))
for oldpath in obsolete:(VAULT/oldpath).unlink()
manifest.write_text(json.dumps(catalog_report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':'generated','documents':len(docs),'statistics':stats},ensure_ascii=True))
