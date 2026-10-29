"""Readable Chinese player attack tables and input-labelled authored Combo graphs."""
import argparse,collections,gzip,hashlib,html,json,re,sys
from pathlib import Path
sys.dont_write_bytecode=True
from player_labels import LABELS
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu';BASE='03配置/玩家攻击'
a=argparse.ArgumentParser();a.add_argument('--check',action='store_true');args=a.parse_args()
def loadgz(f):
 with gzip.open(R/'inventory'/f,'rt',encoding='utf-8') as h:return json.load(h)
objs=loadgz('tagged-objects.json.gz');tables=loadgz('data-tables.json.gz')
graphs=json.loads((R/'inventory/player-combo-graphs.json').read_text(encoding='utf-8'))
types=json.loads((R/'inventory/player-combo-type-layouts.json').read_text(encoding='utf-8'))
def prop(ps,k,idx=0):return next((p for p in ps if p['name']==k and p.get('arrayIndex',0)==idx),None)
def nested(ps,k):
 p=prop(ps,k);return p['value'] if p and isinstance(p.get('value'),list) else []
def val(ps,k):
 p=prop(ps,k);return p.get('value') if p else None
def norm(ps):
 d={}
 for p in ps:
  k=p['name']+'['+str(p.get('arrayIndex',0))+']';x=p.get('value')
  if isinstance(x,list):x=norm(x)
  elif 'arrayElements' in p:x=[norm(v) for v in p['arrayElements']]
  elif 'reference' in p:x={'index':x,'reference':p['reference']}
  elif 'tagNames' in p:x=p['tagNames']
  elif 'arrayValues' in p:x=p['arrayValues']
  d[k]=x
 return d
def local(ref):
 return 'Sifu/Content/'+ref[6:].split('.')[0]+'.uasset' if isinstance(ref,str) and ref.startswith('/Game/') else None
def wl(path,label=None):return '[['+path.removesuffix('.md')+('|' +label if label else '')+']]'
def fmt(v):
 if v is None:return '未保存'
 if isinstance(v,bool):return '是' if v else '否'
 if isinstance(v,float):return format(v,'.9g')
 if isinstance(v,(dict,list)):return json.dumps(v,ensure_ascii=False,separators=(',',':'))
 return str(v)
def table(h,rows):
 esc=lambda x:fmt(x).replace('|',chr(92)+'|').replace('\n','<br>')
 return '\n| '+' | '.join(h)+' |\n|'+'|'.join(['---']*len(h))+'|\n'+''.join('| '+' | '.join(esc(v) for v in row)+' |\n' for row in rows)+'\n'
def effect(ps,kind,flag,field):
 s=nested(ps,kind);on=val(s,flag);n=val(s,field)
 return ('开：'+fmt(n)) if on is True else ('未启用（保存 '+fmt(n)+'）' if on is False else '未保存')
def nav():return wl(BASE+'/阅读入口','玩家攻击阅读入口')+' · '+wl(BASE+'/字段中文说明','字段中文说明')+'\n\n'
FOCUS_LINK='[在浏览器打开徒手专注（HTML）]('+(V/BASE/'招式板/徒手专注.html').as_uri()+')'
BOARD_LINK='[在浏览器打开徒手招式图（HTML）]('+(V/BASE/'招式板/徒手招式板.html').as_uri()+')'
WORDS={'Main':'','Char':'','MainChar':'','MC':'','HB':'命中段','Jab':'刺拳','Hook':'勾拳','Punch':'拳击','Punches':'连续拳','Kick':'踢击','Kicks':'连续踢','Palm':'掌击','Elbow':'肘击','Thrust':'突刺','Throat':'咽喉','Plexus':'躯干','Front':'前向','Back':'后向','High':'高位','Low':'低位','Heavy':'重击','Light':'轻击','Combo':'连招','Finisher':'收尾','Finish':'收尾','Charged':'蓄力','Charge':'蓄力','Sweep':'扫击','Head':'头部','Body':'身体','Ground':'地面','Grounded':'倒地目标','Get':'起身','Up':'向上','Down':'向下','Double':'双段','Triple':'三段','Multi':'多段','Hit':'命中','Hits':'连续命中','Spin':'旋转','Spinning':'旋转','Spinny':'旋转','Side':'侧向','Uppercut':'上勾拳','Reverse':'反向','Belly':'腹部','Shin':'胫部','Foot':'脚部','Crooked':'勾绊','Grab':'抓取','Throw':'投掷','Push':'推击','Pushback':'推退','Knockdown':'击倒','KnockDown':'击倒','KD':'击倒','Dizzy':'眩晕','Post':'后续','Parry':'招架','PostParry':'招架后','Rush':'突进','Engage':'接近','Disengage':'拉开','Delay':'延迟','Attack':'攻击','Attacks':'攻击','Special':'特殊','Skill':'技能','Skills':'技能','Barehands':'徒手','BareHands':'徒手','Bats':'球棒','Bat':'球棒','Staff':'长棍','Blades':'刀刃','Blade':'刀刃','Slash':'斩击','Stroke':'打击','Strike':'打击','Crush':'重砸','Vertical':'垂直','Horizontal':'水平','Wide':'大幅','Fast':'快速','Quick':'快速','Long':'长距离','Straight':'直线','Ribs':'肋部','Rib':'肋部','Hips':'髋部','Hip':'髋部','Knee':'膝击','Flick':'挑击','Mill':'回转','Estoc':'突刺','Poke':'点刺','Pommel':'柄击','Turn':'转身','Dust':'扬尘','Blow':'击打','Slide':'滑步','Sync':'同步','Hold':'按住','Claws':'爪击','Ext':'延伸','End':'结束','Old':'旧版','old':'旧版','Base':'基础','New':'新版','new':'新版'}
def literal(s):
 phrases={'MainChar':'','Mainchar':'','MC':'','FollowUp':'后续','GetUp':'起身','GetUpAttack':'起身攻击','Backturned':'背向','BareHands':'徒手','PostParry':'招架后','KnockDown':'击倒','Knockdown':'击倒','ChargedPunch':'蓄力拳','GroundedPunch':'倒地目标拳击','GroundPunches':'地面连续拳'}
 parts=[]
 for chunk in re.split(r'[_\s]+',s):
  if chunk in phrases:parts.append(phrases[chunk]);continue
  words=re.findall(r'[A-Z]+(?=[A-Z][a-z]|\d|\b)|[A-Z]?[a-z]+|\d+',chunk)
  parts.extend(WORDS.get(x,x) for x in words)
 return '·'.join(x for x in parts if x) or s
NODES={'GetUp Attack':'起身攻击','Conduit':'过渡节点','ShinKick':'胫部踢击','ThroatPunch':'咽喉拳击','Palm02':'掌击节点02','TripleHit':'三段命中','MultiHitClaws':'多段爪击','DoubleElbow':'双肘击','ClawsElbow':'爪击接肘','ElbowSync':'同步肘击','Ext02':'延伸节点02','AoeKnockdown':'范围击倒','DelaySpinHighKick':'延迟旋转高踢','CrookedFoot':'勾绊脚','Rush Attack Light':'轻击突进攻击','Rush Attack Heavy':'重击突进攻击','PostPushback Damage':'推退后伤害分支','PostPushback Knockdown':'推退后击倒分支','FrontKick':'正踢','LowKick':'低踢','Palm Strike':'掌击','GuardBreak':'破防节点','Thrust Kick':'突踢','GroundPunch':'地面拳击','PostGround':'地面攻击后续','Jab(new)':'刺拳（新版节点）','ThroatPlexus':'咽喉／躯干打击','BellyPalm':'腹部掌击','MultiHit':'多段命中','ResilientAttack':'韧性攻击节点','Disengage ':'拉开距离','SpinHighKickFollowUp':'旋转高踢后续','Invert':'反向攻击节点','Dizzy':'眩晕相关攻击','KnockDown':'击倒相关攻击','Pushback':'推退','RibsStroke':'肋部打击','VerticalCrush':'垂直重砸','HeavyPlexusEstoc':'重击躯干突刺','Pushkick':'推踢','HipsHead':'髋部／头部打击','HeadStroke':'头部打击','Reverse Slash':'反向挥击','PlexusEstoc':'躯干突刺','Head Poke':'头部点刺','BatSweep':'球棒扫击','HighDamage':'高伤害节点','SpinnySpeedBoy':'旋转快速节点','Pushback Palm':'推退掌击','Thrust Kick Slash':'突踢接斩','SlashPommelStroke':'斩击接柄击','Charged':'蓄力节点','PostParryKnockDown':'招架后击倒','GroinPlexusEstoc':'下部／躯干突刺','Horizontal Mill':'水平回转','DisengageDelay':'拉开后延迟','EngageDelay':'接近后延迟','Duck Push':'下潜推击'}
def node_label(n):
 raw=n.get('m_Transitions[0]',{}).get('m_ParentNodeName[0]','未命名')
 return NODES.get(raw,literal(raw))+' / '+raw
INPUT={'Light':('L','轻击'),'Heavy':('H','重击'),'LightHold':('按住L','长按轻击'),'HeavyHold':('按住H','长按重击'),'LightAlt':('L-Alt','轻击短按松开变体（≤0.2秒；与普通输入同手势，受输入栈限制）'),'HeavyAlt':('H-Alt','重击短按松开变体（≤0.2秒；与普通输入同手势，受输入栈限制）'),'LightFront':('前向+L','前向轻击输入类型'),'HeavyFront':('前向+H','前向重击输入类型'),'LightFrontFront':('前前+L','双前向轻击输入类型'),'HeavyFrontFront':('前前+H','双前向重击输入类型'),'LightBackFront':('后前+L','后前轻击输入类型'),'HeavyBackFront':('后前+H','后前重击输入类型'),'AttackKnockdown':('倒地攻击','倒地攻击输入类型'),'AttackKnockdownHold':('按住倒地攻击','长按倒地攻击输入类型'),'Grab':('抓取','抓取输入类型'),'LightRushAttack':('突进+L','轻击突进输入类型'),'HeavyRushAttack':('突进+H','重击突进输入类型'),'DodgeAttack':('闪避攻击','闪避攻击输入类型'),'LightGuard':('防御+L','防御轻击输入类型'),'HeavyGuard':('防御+H','防御重击输入类型'),'Disengage':('拉开','拉开输入类型')}
input_enum=next(x for x in types['layouts'] if x['name']=='EComboTransition')
enum_by_id={x['value']:x['name'] for x in input_enum['fields'] if x['kind']=='enumerator'}
def input_label(s):
 k=str(s).split('::')[-1];x=INPUT.get(k,(k,k));return x[0]+' '+x[1]
tree_names={'MainChar_ComboTree':'徒手','MainChar_Bats_ComboTree':'球棒','MainChar_Blades_ComboTree':'刀刃','MainChar_Staff_ComboTree':'长棍','EnvironmentalElement_OneHanded_ComboTree':'单手环境物'}
hit_lookup={}
for t in tables:
 for row in t['rows']:
  if prop(row['properties'],'m_OnHitImpact'):hit_lookup[(t['asset'],row['row'])]=row
attack_lookup={o['asset']:o for o in objs if o['class'].endswith('.AttackDB')}
catalog=json.loads((R/'inventory/configuration-catalog-coverage.json').read_text(encoding='utf-8'))
asset_pages={v['asset']:p for p,v in catalog['documents'].items() if 'asset' in v}
attack_pages={}
for p,meta in catalog['documents'].items():
 if meta.get('kind')=='attackdb':
  text=(V/p).read_text(encoding='utf-8')
  for heading,asset in re.findall(r'^## (A\d{3}-.+)\n\n来源资产：([^\n]+)',text,re.M):attack_pages[asset]=p+'#'+heading
def aref(asset,label=None):return wl(attack_pages[asset],label or Path(asset).stem) if asset in attack_pages else (label or asset)
def hitref(asset,row):return wl(asset_pages[asset],row) if asset in asset_pages else row
def windows(asset):
 o=attack_lookup.get(asset)
 if not o:return []
 p=prop(nested(o['properties'],'m_Attack'),'m_HitBoxes')
 return [norm(v) for v in p.get('arrayElements',[])] if p else []
def gethit(w):
 h=w.get('m_HitRow[0]',{});ref=h.get('DataTable[0]',{}).get('reference');row=h.get('RowName[0]')
 return local(ref),row,hit_lookup.get((local(ref),row))
def rangetext(w):
 a=w.get('m_FrameRange[0]',{}).get('m_Anim[0]',{})
 def one(k):
  b=a.get(k,{})
  return '无界' if b.get('Type[0]')=='ERangeBoundTypes::Open' else str(b.get('Type[0]','?')).split('::')[-1]+':'+fmt(b.get('Value[0]'))
 return one('LowerBound[0]')+' → '+one('UpperBound[0]')
def damagerows(asset,with_asset=False):
 rr=[]
 for i,w in enumerate(windows(asset)):
  ha,hn,hr=gethit(w);ps=hr['properties'] if hr else []
  row=[i,hitref(ha,hn or '未保存行名'),effect(ps,'m_OnHitImpact','m_bUseDamage','m_fDamage'),effect(ps,'m_OnHitImpact','m_bUseStructureDamage','m_fStructureDamage'),effect(ps,'m_OnHitImpact','m_bUseNbFrameStuned','m_iNbFrameStuned'),effect(ps,'m_OnGuardImpact','m_bUseStructureDamage','m_fStructureDamage'),effect(ps,'m_OnDeflectImpact','m_bUseStructureDamage','m_fStructureDamage'),rangetext(w)]
  rr.append(([aref(asset,literal(Path(asset).stem)),Path(asset).stem] if with_asset else [])+row)
 return rr
docs={}
def add(p,s):docs[p]=s.rstrip()+'\n'
# Every stored player attack/animation field receives a Chinese identifier, tested by source names.
field_counts=collections.Counter()
def walk(ps):
 for p in ps:
  field_counts[p['name']]+=1
  if isinstance(p.get('value'),list):walk(p['value'])
  for e in p.get('arrayElements',[]):walk(e)
for o in objs:
 if '/_MainChar/' in o['asset'] and o['class'].endswith('.AttackDB'):walk(o['properties'])
for t in tables:
 if '/_MainChar/' in t['asset']:
  for row in t['rows']:walk(row['properties'])
missing=set(field_counts)-set(LABELS)
if missing:raise ValueError('Missing Chinese field labels '+repr(missing))
text='# 玩家攻击字段中文说明\n\n'+nav()
text+='每个原字段都保留，中文名用于阅读和搜索。名称是字段译文，不代表对应运行期语义已全部确认。索引 [0] 等是保存结构的数组索引，不是招式输入顺序。\n'
text+=table(['中文标识','原字段','中文解释／边界','出现次数'],[[LABELS[k]['label'],k,LABELS[k]['note'],field_counts[k]] for k in sorted(field_counts)])
text+='## 命中表怎样看\n'+table(['显示','读法'],[['开：10','该结果启用了参数，保存值为10；最终扣血仍可能修正'],['未启用（保存10）','保存了10，但此开关为假，不能直接计入伤害'],['未保存','不能当作零，可能来自继承或其他配置'],['一次动作多个命中段','分别看每个窗口／HitBox，不能在未确认重复命中规则时把所有行相加'],['Self 自身伤害字段','作用对象须结合执行路径确认，不直接加到被击者身上'],['韧性覆盖值','用于当前比较；不是已确认的每击累计削韧量']])
add(BASE+'/字段中文说明.md',text)
# Complete action -> hitbox -> damage lookup, split by weapon/resource family.
groups=collections.defaultdict(list)
for o in objs:
 if '/_MainChar/' not in o['asset'] or not o['class'].endswith('.AttackDB'):continue
 asset=o['asset']
 group='徒手' if '/BareHands/' in asset else ('球棒' if '/Bats/' in asset else ('刀刃' if '/Blades/' in asset else ('长棍' if '/Staff/' in asset else ('投掷' if '/Throwable/' in asset else '其他'))))
 groups[group].append(o)
window_refs=0
for group,items in groups.items():
 items.sort(key=lambda o:('/_old/' in o['asset'],'/_Special' in o['asset'],o['asset']))
 p=BASE+'/招式伤害对照-'+group+'.md'
 text='# '+group+'：招式资源与伤害对照\n\n'+nav()
 text+='本页把动作资源和实际引用的命中段放在一起，避免只看到资产名却找不到伤害。中文名称是资源直译，尚未逐项映射官方招式名。旧资源、特殊变体和当前调用未知项保留。保存值不等于最终实战伤害。\n'
 text+='## 全部动作索引\n'+table(['资源直译（辅助标识）','原始资源名','本资源已解析命中窗口数','路径范围','详情'],[[literal(Path(o['asset']).stem),Path(o['asset']).stem,len(windows(o['asset'])),'旧路径' if '/_old/' in o['asset'] else '当前调用情况待核',wl(p+'#'+Path(o['asset']).stem,'查看命中段')] for o in items])
 for o in items:
  asset=o['asset'];rr=damagerows(asset);window_refs+=len(rr)
  text+='\n## '+Path(asset).stem+'\n\n中文辅助标识：'+literal(Path(asset).stem)+'。\n\n来源：'+asset+'\n\n原配置：'+aref(asset)+'。\n'
  text+=table(['命中段序号','HitBox 行','普通命中生命伤害','普通命中架势伤害','受击硬直帧','被格挡时架势伤害','被弹开时架势伤害','命中窗口（配置帧）'],rr) if rr else '当前可解码的命中窗口列表为空或未保存；不等于该动作没有伤害。可能走其他动作、条件配置或特殊逻辑。\n'
  text+='各结果还有停顿、击退、特殊眩晕等独立参数，点击 HitBox 行打开全部配置；不在这里把普通命中值套到格挡或弹开。\n'
 add(p,text)
# All 313 player hitbox rows can be found directly even if not reached from an admitted AttackDB.
rows=[]
for (asset,name),row in hit_lookup.items():
 if '/_MainChar/' not in asset:continue
 ps=row['properties']
 rows.append([literal(name),name,hitref(asset,name),effect(ps,'m_OnHitImpact','m_bUseDamage','m_fDamage'),effect(ps,'m_OnHitImpact','m_bUseStructureDamage','m_fStructureDamage'),effect(ps,'m_OnHitImpact','m_bUseNbFrameStuned','m_iNbFrameStuned'),Path(asset).stem])
add(BASE+'/命中段与伤害总表.md','# 玩家全部命中段与伤害总表\n\n'+nav()+'覆盖313条已解析玩家 HitBox 行。这里是命中段，不是313种独立招式。中文为原名直译；动作到命中段的关联见各武器招式伤害对照。\n'+table(['中文辅助标识','原始行名','完整配置入口','生命伤害配置','架势伤害配置','硬直帧配置','来源表'],rows))
# Input labels keep distinctions visible without inventing current keyboard/controller bindings.
intro='# 玩家输入与连招图读法\n\n'+nav()
intro+='L、H 在本库分别表示轻击、重击动作输入，不代表某个固定键盘键／手柄键；自定义键位无需改变图的连接。方向词先按内部输入类型翻译，Alt与普通同键共用≤0.2秒短按松键，互为输入栈兄弟，不能当额外轻重组合；具体方向参照和运行期选择仍保留边界。\n'
intro+=table(['原始转换类型','图中标记','中文说明'],[[k,INPUT[k][0],INPUT[k][1]] for i,k in sorted(enum_by_id.items()) if k in INPUT])
intro+='## 图例与范围\n'+table(['图中内容','含义／限制'],[['实线箭头','资产中保存了对应输入和目标节点；仍需动作许可、技能和运行时条件'],['虚线默认入口','GetDefaultAttackID 按输入枚举取默认攻击；不是任意状态都能立即执行'],['虚线重定向','节点保存了重定向目标；被忽略输入和动作层等规则仍影响使用'],['条件分支键','来自 Byte→节点编号映射，保留0、1、2等原始键；不能一律翻译为是／否'],['几率字段','保存的选择概率参数，不当作已经实测的频率'],['姿态槽0～3','0前左、1前右、2后右、3后左；按身体／骨盆相对目标选槽，镜像交换左右；不是四次命中'],['所需技能标签','保存的标签要求会限制节点资格；不能省略成人人可接'],['条件攻击覆写','仍有未解码项；节点基本动作并非保证是最终所选动作'],['图中生命／架势配置','标注基本动作各命中段的保存值集合，不求和，不是最终伤害或同一输入的累计值'],['连续命中保证','连招树只证明配置衔接，不证明敌人在整串期间无法格挡、闪避或恢复'],['长按默认回退','GetDefaultAttackID 的 LightHold／HeavyHold 若保存-1，会分别回退到 Light／Heavy 默认节点']])
intro+='默认入口索引与转换枚举的关系已核对本机代码；证据见 inventory/player-combo-default-input-disassembly.json。目标映射类型见 inventory/player-combo-type-layouts.json，原始映射的完整消费与节点边界检查见 inventory/player-combo-graphs.json。\n'
add(BASE+'/输入与衔接图读法.md',intro)
def edge_label(e):
 s=input_label(e['input']);condition=e.get('condition') or {}
 if condition.get('reference'):s+='；条件分支键'+str(e['condition_result'])
 if e.get('probability')!=100:s+='；几率字段'+fmt(e.get('probability'))
 return s
def node_damage_summary(node):
 life=set();structure=set()
 for key,ref in node.get('m_AttackInfos[0]',{}).items():
  if not key.startswith('m_Attacks['):continue
  for w in windows(local(ref)):
   ha,hn,hr=gethit(w)
   if not hr:continue
   ps=nested(hr['properties'],'m_OnHitImpact')
   if val(ps,'m_bUseDamage') is True:life.add(val(ps,'m_fDamage'))
   if val(ps,'m_bUseStructureDamage') is True:structure.add(val(ps,'m_fStructureDamage'))
 def show(values):return '/'.join(fmt(x) for x in sorted(values)) if len(values)<=4 else '多种，见表'
 return '命中段生命配置:'+show(life)+'；架势配置:'+show(structure) if life or structure else ''

def graphtext(tree,subset=None,default_indices=None,with_starts=True):
 ns=tree['nodes'];edges=[e for e in tree['edges'] if e['target']>=0 and (subset is None or (e['source'].startswith('N') and int(e['source'][1:]) in subset and e['target'] in subset))]
 used=set(range(len(ns))) if subset is None else set(subset)
 lines=['flowchart LR']
 for i in sorted(used):
  label='N'+str(i)+' '+node_label(ns[i])
  damage=node_damage_summary(ns[i])
  if damage:label+='<br/>'+damage
  if ns[i].get('m_RequiredTags[0]'):label+='<br/>需技能标签'
  if ns[i].get('m_bSkip[0]'):label+='<br/>跳过／过渡标志'
  lines.append('  N'+str(i)+'["'+html.escape(label,quote=True).replace('&lt;br/&gt;','<br/>')+'"]')
 sources=sorted({e['source'] for e in edges if e['source'].startswith('S')}) if with_starts else []
 for src in sources:
  entry=tree['starts'][int(src[1:])];name=entry.get('m_ComboTransitions[0]',{}).get('m_ParentNodeName[0]','未命名入口')
  lines.append('  '+src+'(["起手状态：'+html.escape(literal(name)+' / '+name,quote=True)+'"])')
 for e in edges:
  if not with_starts and e['source'].startswith('S'):continue
  lines.append('  '+e['source']+' -->|"'+html.escape(edge_label(e),quote=True)+'"| N'+str(e['target']))
 for i in sorted(used):
  target=ns[i].get('m_NodeRedirect[0]',-1)
  if isinstance(target,int) and target>=0 and target in used:lines.append('  N'+str(i)+' -.->|"节点重定向"| N'+str(target))
 for k,target in tree['defaults'].items():
  idx=int(re.search(r'\[(\d+)\]',k).group(1))
  if target<0 or (default_indices is not None and idx not in default_indices) or target not in used:continue
  label=input_label(enum_by_id.get(idx,str(idx)))
  lines+=['  D'+str(idx)+'(["默认回退入口"])','  D'+str(idx)+' -.->|"'+html.escape(label,quote=True)+'"| N'+str(target)]
 return '\n'.join(lines)
tree_stats=[];graph_paths=[]
for tree in graphs['trees']:
 label=tree_names.get(Path(tree['asset']).stem,Path(tree['asset']).stem);p=BASE+'/输入衔接图-'+label+'.md';graph_paths.append((label,p))
 ns=tree['nodes'];text='# '+label+'：输入关联的招式衔接图\n\n'+nav()+wl(BASE+'/输入与衔接图读法','先看输入和图例说明')+'\n\n中文为内部节点与资源的辅助译名，原名、节点编号和条件均保留。图依据资产保存的连接生成，不把它当成稳定命中保证。来源：'+tree['asset']+'。\n'
 if label=='徒手':
  text+='\n'+FOCUS_LINK+'。\n'+BOARD_LINK+'。单画布以轻重两行为中心，点节点看前后高亮和右侧详情。编辑时一格放一个居中节点，占用格禁止放入、不交换；阅读隐藏格子。当前浏览器自动保存，支持导入／导出及迁移前原布局备份。\n'
  subset={v for k,v in tree['defaults'].items() if k in ['m_DefaultAttacks[0]','m_DefaultAttacks[6]'] and v>=0}
  for depth in range(5):
   more={e['target'] for e in tree['edges'] if e['source'].startswith('N') and int(e['source'][1:]) in subset and e['target']>=0 and e['input'] in ['EComboTransition::Light','EComboTransition::Heavy']}
   more|={ns[i].get('m_NodeRedirect[0]',-1) for i in subset};subset|={x for x in more if isinstance(x,int) and x>=0}
  text+='\n## 徒手轻重击阅读图\n\n从轻击和重击的默认回退节点展开五轮已保存的轻重连接；完整起手状态、特殊输入和标签见后面的全图与表。\n\n~~~mermaid\n'+graphtext(tree,subset,{0,6},False)+'\n~~~\n'
 text+='\n## 完整配置衔接图\n\n~~~mermaid\n'+graphtext(tree)+'\n~~~\n'
 text+='\n## 默认输入入口对照\n'
 rr=[]
 for key,target in tree['defaults'].items():
  idx=int(re.search(r'\[(\d+)\]',key).group(1));derived=target;note='直接保存'
  if target==-1 and idx in [1,7]:derived=tree['defaults'].get('m_DefaultAttacks['+str(idx-1)+']',-1);note='长按默认入口未配置，代码回退到对应普通轻／重输入'
  rr.append([idx,input_label(enum_by_id.get(idx,str(idx))),target,('N'+str(derived)+' '+node_label(ns[derived])) if isinstance(derived,int) and derived>=0 else '无默认节点',note])
 text+=table(['转换枚举索引','输入标识','保存节点编号','默认选择或回退结果','说明'],rr)
 text+='\n## 每条保存的输入衔接\n'+table(['当前节点／入口','输入','目标节点','条件对象','分支键原值','几率字段'],[[e['source'],input_label(e['input']),('N'+str(e['target'])+' '+node_label(ns[e['target']])) if e['target']>=0 else '无目标',e.get('condition',{}).get('reference') or '未配置额外条件',e['condition_result'],e.get('probability')] for e in tree['edges']])
 text+='\n## 节点到动作与伤害\n'
 node_attack_count=0;resolved=0
 for i,node in enumerate(ns):
  header='N'+str(i)+' '+node_label(node);text+='\n### '+header+'\n'
  text+=table(['节点属性','保存内容'],[['所需技能标签',node.get('m_RequiredTags[0]')],['节点重定向目标',node.get('m_NodeRedirect[0]')],['跳过节点标志',node.get('m_bSkip[0]')],['条件攻击覆写',node.get('m_ConditionalAttacks[0]')],['提示','下表为基本动作槽；条件覆写、蓄力变体和运行时许可仍可能改变选择']])
  slots=collections.defaultdict(list)
  for key,ref in node.get('m_AttackInfos[0]',{}).items():
   if key.startswith('m_Attacks[') and isinstance(ref,str) and ref.startswith('/Game/'):slots[local(ref)].append(int(re.search(r'\[(\d+)\]',key).group(1)))
  if not slots:text+='没有保存基本攻击动作引用；可能是过渡／重定向节点，不能把它当作独立攻击。\n'
  for asset,indices in slots.items():
   node_attack_count+=1;resolved+=int(asset in attack_lookup)
   text+='\n姿态槽 '+','.join(map(str,indices))+'：'+aref(asset,literal(Path(asset).stem)+' / '+Path(asset).stem)+'。\n'
   text+=table(['命中段序号','HitBox 行','生命伤害配置','架势伤害配置','硬直帧配置','格挡架势配置','弹开架势配置','命中窗口'],damagerows(asset)) if windows(asset) else '该动作未在当前集合中解析出可列的命中窗口，保留引用，不补造伤害。\n'
 text+='\n### 图的证据与未解部分\n\n输入边来自精确消费字节的目标映射；重定向来自节点字段；默认输入入口另经代码核对。条件对象的内部判定、条件攻击覆写、技能解锁与完整运行时衔接时机尚未穷尽。不同姿态槽不是重复命中次数，不将其伤害相加。\n'
 text+='来源：inventory/player-combo-graphs.json；inventory/player-combo-type-layouts.json；inventory/player-combo-input-disassembly.json；inventory/player-combo-default-input-disassembly.json。\n'
 add(p,text);tree_stats.append({'label':label,'nodes':len(ns),'authored_input_edges':len(tree['edges']),'basic_attack_variants':node_attack_count,'resolved_basic_attack_variants':resolved,'document':p})
index='# 玩家攻击阅读入口\n\n'+wl('00索引/首页','返回首页')+' · '+wl('03配置/配置索引','返回配置索引')+'\n\n先用带输入的图看衔接，再在同页查节点引用的命中段和伤害。字段均附中文标识，保留原名；中文招式名称当前为辅助直译，不冒充已核对的官方名称。\n'
index+=wl(BASE+'/招式待核项与已确认信息','朝向、输入和可避方向的查询结果')+'\n\n'
index+=FOCUS_LINK+'：左上角可切换徒手图／专注；'+wl(BASE+'/徒手节点覆盖核对','节点与官方名覆盖核对')+'。\n\n'
index+='## 徒手招式图\n\n'+BOARD_LINK+'。单图以连续轻重两行为中心，节点仅用操作称呼；前驱后继相同的配置归并，输入／条件／属性在右侧抽屉分别保留。支持前后高亮、缩放及阅读／编辑切换；布局可拖动、多选对齐／等距、撤销重做，自动保存到当前浏览器并可导出备份。\n\n'+wl(BASE+'/徒手招式板小样','使用说明与覆盖边界')+'：57个保存节点收纳为33个连招节点，另补3个独立能力入口；63条源连接与21类默认输入保留。官方名见悬浮气泡，详情保留操作称呼及配置差异；条件替换已解码但不作为默认新增节点。\n\n'
index+='## 输入关联的衔接图\n'+table(['武器／范围','入口','配置节点','保存输入边'],[[s['label'],wl(s['document'],'打开衔接图与节点伤害'),s['nodes'],s['authored_input_edges']] for s in tree_stats])
index+='## 查伤害与参数\n'+table(['内容','入口'],[['全部玩家字段中文标识与解释',wl(BASE+'/字段中文说明')],['输入标记、条件、方向与默认回退的读法',wl(BASE+'/输入与衔接图读法')],['全部313条命中段的伤害总表',wl(BASE+'/命中段与伤害总表')]]+[[group+'全部动作到伤害的对照',wl(BASE+'/招式伤害对照-'+group)] for group in groups])
index+='## 数据范围\n\n5套连招树的126个节点与128条保存输入边均已纳入；255个已解析玩家 AttackDB 和314个玩家命中窗口可从伤害页查找。图中直线不表示敌人无法脱离；技能标签、条件分支、旧资源、未知中文名和未解码覆写均保留提示。本阶段未运行游戏。\n'
add(BASE+'/阅读入口.md',index)
report={'field_names':len(field_counts),'fields_without_chinese_labels':sorted(missing),'player_hitbox_rows_in_readable_table':len(rows),'player_attackdb_objects':sum(len(x) for x in groups.values()),'player_hitbox_windows_joined':window_refs,'trees':tree_stats,'input_enum_values':enum_by_id,'documents':{p:{'sha256':hashlib.sha256(s.encode()).hexdigest(),'bytes':len(s.encode())} for p,s in docs.items()},'source_hashes':{p:hashlib.sha256((R/p).read_bytes()).hexdigest() for p in ['inventory/player-combo-graphs.json','exports/player-field-labels.json','inventory/tagged-objects.json.gz','inventory/data-tables.json.gz']},'runtime_verified':False}
manifest=R/'inventory/player-readable-catalog.json'
if args.check:
 old=json.loads(manifest.read_text(encoding='utf-8'));errors=[]
 if old['source_hashes']!=report['source_hashes']:errors.append('source hashes changed')
 for p,s in docs.items():
  if not (V/p).is_file() or (V/p).read_text(encoding='utf-8')!=s:errors.append(p)
 print(json.dumps({'status':'passed' if not errors else 'failed','documents':len(docs),'fields_without_labels':sorted(missing),'trees':tree_stats,'errors':errors},ensure_ascii=True));raise SystemExit(bool(errors))
old=json.loads(manifest.read_text(encoding='utf-8')) if manifest.exists() else None
for p,s in docs.items():
 target=V/p
 if target.exists() and (not old or p not in old['documents'] or hashlib.sha256(target.read_text(encoding='utf-8').encode()).hexdigest()!=old['documents'][p]['sha256']):raise RuntimeError('Protect existing note '+p)
for p,s in docs.items():
 target=V/p;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(s,encoding='utf-8',newline=chr(10))
manifest.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
print(json.dumps({'documents':len(docs),'field_names':len(field_counts),'player_attackdb_objects':report['player_attackdb_objects'],'player_hitbox_windows_joined':window_refs,'trees':tree_stats},ensure_ascii=True))
