"""Fixed board with per-variant properties and an exhaustive saved-tree audit."""
from pathlib import Path
import gzip, hashlib, json, collections
from player_graph_model import build_graph
from player_graph_catalog import apply_names,hit_window,supplemental_node
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'exports/20261029-徒手补全与命名-13'
OUT.mkdir(parents=True,exist_ok=True)
def read(p):
    if str(p).endswith('.gz'):
        with gzip.open(ROOT/p,'rt',encoding='utf-8') as f:return json.load(f)
    return json.loads((ROOT/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def prop(ps,k):return next((p for p in ps if p['name']==k),{})
def value(ps,k):return prop(ps,k).get('value')
def nested(ps,k):
    v=value(ps,k)
    return v if isinstance(v,list) else []
def local(ref):return 'Sifu/Content/'+ref[6:].split('.')[0]+'.uasset' if isinstance(ref,str) and ref.startswith('/Game/') else None
def simple(ps):
    out={}
    for p in ps:
        k=p['name']+'['+str(p.get('arrayIndex',0))+']'
        if 'arrayElements' in p:v=[simple(x) for x in p['arrayElements']]
        elif isinstance(p.get('value'),list):v=simple(p['value'])
        else:v=p.get('reference',p.get('tagNames',p.get('value')))
        out[k]=v
    return out
tree=next(t for t in read('inventory/player-combo-graphs.json')['trees'] if t['asset'].endswith('/MainChar_ComboTree.uasset'))
objs=read('inventory/tagged-objects.json.gz');tables=read('inventory/data-tables.json.gz')
attacks={o['asset']:o for o in objs if o['class'].endswith('.AttackDB')}
hits={(t['asset'],r['row']):r for t in tables for r in t['rows']}
names={0:'起身攻击',1:'招架反击·轻击入口',2:'招架反击·轻击（三连打）',4:'重击第2段',5:'重击第3段',7:'轻击第4段',8:'轻击第5段',9:'连续抓击收尾',10:'重击第4段',11:'重轻·抓击后续',12:'重轻重·肘击后续',14:'轻击第3段',15:'轻轻轻重·击倒收尾',16:'停顿后·旋转高踢',17:'三连打后续·第二招',18:'三连打后续·第三招',19:'招架反击·重击',21:'招架反击·长按重击',22:'奔跑攻击·轻击',23:'奔跑攻击·重击',25:'推击后·连续追打',26:'推击后·击倒追打',30:'向前踢击衔接',31:'后前重·扫腿',32:'后前轻·推掌／推踢',33:'长按轻击',36:'前前重·向前踢击',39:'前前轻·向前拳击',40:'前前轻后·轻击追打',44:'轻击第1段',45:'轻击第2段',48:'重击第1段',50:'重击后·变体连打',51:'防御重击·抗打断攻击',52:'拉开距离攻击',54:'拉开后·重击追打',55:'闪避攻击·换位',56:'蓄力重击'}
inputs={'Light':'轻击','Heavy':'重击','LightHold':'长按轻击','HeavyHold':'长按重击','LightAlt':'短按轻击松开·变体','HeavyAlt':'短按重击松开·变体','LightFront':'前轻','HeavyFront':'前重','LightFrontFront':'前前轻','HeavyFrontFront':'前前重','LightBackFront':'后前轻','HeavyBackFront':'后前重','AttackKnockdown':'倒地攻击','AttackKnockdownHold':'长按倒地攻击','Grab':'抓取','LightRushAttack':'奔跑轻击','HeavyRushAttack':'奔跑重击','DodgeAttack':'闪避攻击','LightGuard':'防御轻击','HeavyGuard':'防御重击','Disengage':'拉开距离'}
names.update({11:'重击第2段后·轻击',12:'抓击后·重击肘击',16:'旋转高踢（起手待核）',17:'招架反击·轻击变体甲',18:'招架反击·轻击变体乙',51:'防御重击（效果待核）'})
enum=next(x for x in read('inventory/player-combo-type-layouts.json')['layouts'] if x['name']=='EComboTransition')
enum_names={f['value']:f['name'] for f in enum['fields'] if f['kind']=='enumerator'}
def resolve(i):
    seen=set()
    while tree['nodes'][i].get('m_NodeRedirect[0]',-1)>=0:
        assert i not in seen
        seen.add(i);i=tree['nodes'][i]['m_NodeRedirect[0]']
    return i
def metric(ps,group,flag,field):
    p=nested(ps,group)
    return {'enabled':value(p,flag),'value':value(p,field)}
def attack_info(ref):
    asset=local(ref);o=attacks.get(asset)
    if not o:return {'asset':asset or ref,'parsed':False,'windows':[]}
    a=nested(o['properties'],'m_Attack');windows=[]
    for w in prop(a,'m_HitBoxes').get('arrayElements',[]):
        h=nested(w,'m_HitRow');table=local(prop(h,'DataTable').get('reference'));row=value(h,'RowName');hr=hits.get((table,row));ps=hr['properties'] if hr else []
        windows.append({'table':table,'row':row,'resolved':bool(hr),'damage':metric(ps,'m_OnHitImpact','m_bUseDamage','m_fDamage'),'structure':metric(ps,'m_OnHitImpact','m_bUseStructureDamage','m_fStructureDamage'),'stun':metric(ps,'m_OnHitImpact','m_bUseNbFrameStuned','m_iNbFrameStuned'),'guard':metric(ps,'m_OnGuardImpact','m_bUseStructureDamage','m_fStructureDamage'),'deflect':metric(ps,'m_OnDeflectImpact','m_bUseStructureDamage','m_fStructureDamage'),'push':metric(ps,'m_OnHitImpact','m_bUseKnockBackDistance','m_fKnockBackDistance'),'power':value(ps,'m_eAttackPower'),'reaction':value(ps,'m_eHittedReaction'),'parriable':value(ps,'m_bParriable'),'resilience':{'enabled':value(ps,'m_bOverrideResilience'),'value':value(ps,'m_iOverrideResilienceValue')},'action':prop(ps,'m_hitAction').get('reference'),'raw':simple(ps),'window':simple(w)})
    return {'asset':asset,'parsed':True,'source_sha256':o.get('sha256'),'buildup':value(a,'m_iWantedBuildupFrames'),'range':value(a,'m_fGameplayRange'),'windows':windows,'raw':simple(a)}
used_assets={};nodes={}
for i,n in enumerate(tree['nodes']):
    target=resolve(i);variants=[];info=n.get('m_AttackInfos[0]',{})
    for tier,block in [('基础',info)]+[(f'蓄力档位{j}',b) for j,b in enumerate(info.get('m_ChargedAttacks[0]',[]))]:
        refs=collections.defaultdict(list)
        for k,v in block.items():
            if k.startswith('m_Attacks[') and local(v):refs[v].append(int(k.split('[')[1].split(']')[0]))
        for ref,slots in refs.items():
            asset=local(ref)
            if asset not in used_assets:used_assets[asset]=attack_info(ref)
            variants.append({'tier':tier,'slots':slots,'asset':asset})
    edges=[]
    for ei,e in enumerate(tree['edges']):
        if e['source']!=f'N{i}':continue
        edges.append({'index':ei,'target':resolve(e['target']) if e['target']>=0 else None,'input':inputs.get(e['input'].split('::')[-1],e['input']),'rawInput':e['input'],'conditional':bool(e.get('condition',{}).get('reference')),'condition':e.get('condition'),'key':e.get('condition_result'),'rawTarget':e['target'],'probability':e.get('probability')})
    nodes[str(i)]={'id':i,'target':target,'name':names.get(target,'待确认招式'),'variants':variants,'edges':edges,'tags':n.get('m_RequiredTags[0]',[]),'rawName':n.get('m_Transitions[0]',{}).get('m_ParentNodeName[0]'),'charge':[b.get('m_Infos[0]',{}) for b in info.get('m_BuildUpForChargedAttack[0]',[])],'conditionalOverrides':n.get('m_ConditionalAttacks[0]'),'redirectIgnored':n.get('m_NodeRedirectIgnoredTransitions[0]')}
canonical=[i for i in range(len(tree['nodes'])) if resolve(i)==i]
assert set(canonical)==set(names),(set(canonical)-set(names),set(names)-set(canonical))
groups={'light':[44,45,14,7,8],'heavy':[48,4,5,10],'mixed':[11,12,9,15,30,50],'direction':[39,36,32,31],'charge':[33,56],'situation':[0,1,2,16,17,18,19,21,22,23,25,26,40,51,52,54,55]}
shown=[i for group in groups.values() for i in group]
assert set(shown)==set(canonical) and len(shown)==len(canonical)
defaults=[]
for key,target in tree['defaults'].items():
    idx=int(key.split('[')[1].split(']')[0]);raw=enum_names[idx];actual=target
    if target==-1 and idx in (1,7):actual=tree['defaults'][f'm_DefaultAttacks[{idx-1}]']
    defaults.append({'input':inputs.get(raw,raw),'rawInput':raw,'saved':target,'target':resolve(actual) if actual>=0 else None,'fallback':target!=actual})
starts=[]
for si,s in enumerate(tree['starts']):
    start_name=s.get('m_ComboTransitions[0]',{}).get('m_ParentNodeName[0]','未命名状态')
    for ei,e in enumerate(tree['edges']):
        if e['source']==f'S{si}':starts.append({'start':si,'rawState':start_name,'edge':ei,'input':inputs.get(e['input'].split('::')[-1],e['input']),'target':resolve(e['target']) if e['target']>=0 else None,'condition':e.get('condition'),'key':e.get('condition_result')})
coverage={'nodes':[{'source':i,'target':resolve(i),'display':names[resolve(i)],'status':'单独展示' if resolve(i)==i else '合并重定向（保留证据）'} for i in range(len(tree['nodes']))],'edges':[{'index':i,'source':e['source'],'target':e['target'],'status':'节点详情' if e['source'].startswith('N') else '情境起手表'} for i,e in enumerate(tree['edges'])],'defaults':defaults,'starts':starts,'assets':list(used_assets),'unresolvedAssets':[p for p,a in used_assets.items() if not a['parsed']],'unresolvedHitRows':[{'asset':p,'table':w['table'],'row':w['row']} for p,a in used_assets.items() for w in a['windows'] if not w['resolved']]}
barehands={p:a for p,a in attacks.items() if '/_MainChar/' in p and '/BareHands/' in p}
coverage['outsideTree']=[{'asset':p,'status':'树外候选：可能为条件覆写、旧版、特殊动作或未接通引用','legacy':'/_old/' in p} for p in sorted(set(barehands)-set(used_assets))]
outside_attacks={}
for candidate in coverage['outsideTree']:
    p=candidate['asset']
    candidate['category']='旧版路径' if candidate['legacy'] else ('特殊动作路径' if '/_Special/' in p or '/_SpecialCombo/' in p else '常规路径待接通')
    outside_attacks[p]=attack_info('/Game/'+p.removeprefix('Sifu/Content/').removesuffix('.uasset'))
coverage['outsideTreeCategories']=dict(collections.Counter(x['category'] for x in coverage['outsideTree']))
candidate_names={'MC_GRAB_BL':'抓取动作·变体甲','MC_GRAB_FL':'抓取动作·变体乙','MainChar_GuardBreak_BL':'长按轻击·待核变体','MainChar_DoubleElbowStrike_FL':'双肘击·待核动作','MainChar_ClawsElbow_DoubleHit_FL':'抓击接肘·待核动作','MC_Skill_HighCrush_FL':'高位重击·技能候选'}
candidate_cards=[{'asset':x['asset'],'name':candidate_names[Path(x['asset']).stem]} for x in coverage['outsideTree'] if x['category']=='常规路径待接通']
coverage['outsideTreeUnresolvedRows']=[{'asset':p,'table':w['table'],'row':w['row']} for p,a in outside_attacks.items() for w in a['windows'] if not w['resolved']]
coverage['summary']={'savedNodes':len(tree['nodes']),'displayCards':len(canonical),'mergedNodes':len(tree['nodes'])-len(canonical),'savedEdges':len(tree['edges']),'defaultInputs':len(defaults),'startEdges':len(starts),'treeActionAssets':len(used_assets),'chargedVariants':sum(v['tier']!='基础' for n in nodes.values() for v in n['variants']),'outsideTreeCandidates':len(coverage['outsideTree'])}
data={'nodes':nodes,'groups':groups,'attacks':used_assets,'outsideAttacks':outside_attacks,'candidateCards':candidate_cards,'defaults':defaults,'starts':starts,'source':tree['asset'],'coverage':coverage,'labels':read('exports/player-field-labels.json')}
data['research']=read('inventory/player-unknown-08-display-evidence.json')
data['graph']=build_graph(data)
data['page']='barehands'
data['legacyNodeIds']=[n['id'] for n in data['graph']['nodes']]
data['pages']=[{'label':'徒手 · 招式图','file':'徒手招式板.html','page':'barehands'},{'label':'徒手 · 专注','file':'徒手专注.html','page':'focus'}]
locale=read('exports/20261029-玩家招式名称-12/paired-texts.json')
apply_names(data,locale)
supp=read('exports/20261029-徒手补全与命名-13/actions-data.json')
for i,action in enumerate(supp['supplementaryNodes']):
    official=[{'name':n,'scope':'动作技能','via':'能力输入入口与游戏本地化'} for n in action['officialNames']]
    data['graph']['nodes'].append(supplemental_node(1001+i,action['operationLabel'],action,official,150+240*i,1070))
data['graph']['height']=1190
conditions=read('exports/20261029-徒手补全与命名-13/conditional-attacks.json')
data['completeness']={'supplementaryActions':supp,'conditionalSummary':conditions['summary'],'conditionalAssets':conditions['referenced_previous_outside_candidates'],'menuCoverage':[]}
for row in locale:
    if row['namespace']!='ST_UI_MenuCombo' or not row['key'].startswith(('Command_','Special_','BaseCombo_')) or any('_'+w+'_' in row['key'] for w in ['Bat','Blade','Staff']):continue
    matches=[n['id'] for n in data['graph']['nodes'] if any(o.get('key')==row['key'] or row['zh-Hans']==o['name'] for o in n['official'])]
    assert matches,('uncovered official menu entry',row['key'])
    data['completeness']['menuCoverage'].append({'key':row['key'],'name':row['zh-Hans'],'nodes':matches,'scope':'menu identity; combo titles are not extra attacks'})
skillUI=read('exports/20261029-玩家招式名称-12/skill-ui-links.json')
data['skillNames']={}
for ui in skillUI['skills']:
    entry=ui['fields'].get('Name',{})
    if entry.get('key','').startswith('SkillTitle_Technique_') and '/OLD/' not in ui['asset']:
        data['skillNames'][entry['key'].replace('SkillTitle_Technique_','').lower()]=entry['zh-Hans']
focusSource=read('exports/20261029-徒手补全与命名-13/focus-data.json')
focusData={'page':'focus','pages':data['pages'],'nodes':{},'attacks':{},'outsideAttacks':{},'candidateCards':[],'defaults':[],'starts':[],'source':focusSource['source'],'coverage':coverage,'labels':data['labels'],'research':data['research'],'skillNames':{},'focusSource':focusSource}
focusNodes=[]
for i,f in enumerate(focusSource['nodes']):
    action={**f,'windows':[hit_window(f['hitProperties'],f['hitTable'],f['hitRow'])],'entryText':f['entry'],'kind':'focus'}
    official=[{'name':f['name'],'en':f['en'],'scope':'专注招式','key':f['nameText']['key'],'namespace':f['nameText']['namespace'],'via':'VitalPointData.m_Name直接文本引用'}]
    focusNodes.append(supplemental_node(2001+i,f['name'],action,official,390+240*(i%3),350+240*(i//3)))
focusData['graph']={'width':1180,'height':850,'nodes':focusNodes,'edges':[],'starts':[],'internalEdges':[],'merges':[],'canonicalToDisplay':{},'rawToDisplay':{},'reportedCommonInput':{'targets':[],'provenance':'专注不是普通连招树，后续边尚未接通'}}

template=(ROOT/'scripts/player_graph_template.html').read_text(encoding='utf-8')
template=template.replace('__EDITOR_JS__',(ROOT/'scripts/player_graph_routing.js').read_text(encoding='utf-8')+'\n'+(ROOT/'scripts/player_graph_cells.js').read_text(encoding='utf-8')+'\n'+(ROOT/'scripts/player_graph_editor.js').read_text(encoding='utf-8'))
(OUT/'player-board.html').write_text(template.replace('__DATA__',json.dumps(data,ensure_ascii=False).replace('</','<\\/')),encoding='utf-8')
vault_html=ROOT/'Sifu/03配置/玩家攻击/招式板/徒手招式板.html'
vault_html.parent.mkdir(parents=True,exist_ok=True)
vault_html.write_bytes((OUT/'player-board.html').read_bytes())
focus_html=template.replace('__DATA__',json.dumps(focusData,ensure_ascii=False).replace('</','<\\/'))
(OUT/'focus-board.html').write_text(focus_html,encoding='utf-8')
(vault_html.parent/'徒手专注.html').write_text(focus_html,encoding='utf-8')
(OUT/'徒手招式板.html').write_bytes(vault_html.read_bytes())
(OUT/'徒手专注.html').write_text(focus_html,encoding='utf-8')
(OUT/'focus-board-data.json').write_text(json.dumps(focusData,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'board-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'coverage.json').write_text(json.dumps(coverage,ensure_ascii=False,indent=2),encoding='utf-8')
manifest={'inputs':{p:sha(p) for p in ['inventory/player-combo-graphs.json','inventory/player-combo-type-layouts.json','inventory/tagged-objects.json.gz','inventory/data-tables.json.gz','exports/player-field-labels.json','inventory/player-unknown-08-display-evidence.json']},'scripts':{p:sha(p) for p in ['scripts/build_player_board.py','scripts/player_graph_model.py','scripts/player_graph_template.html','scripts/player_graph_editor.js']},'asset':tree['asset'],'uasset_sha256':tree['uasset_sha256'],'uexp_sha256':tree['uexp_sha256'],'summary':coverage['summary'],'display_graph':{'nodes':len(data['graph']['nodes']),'edges':len(data['graph']['edges']),'merges':data['graph']['merges']},'limits':['static saved tree coverage only','conditional attacks remain opaque','Alt shares short-release gesture with normal input; contextual stack selection applies; quadrant mapping confirmed; attack height classification remains unverified','all saved charge tiers preserved, not inferred final hold times','out-of-tree candidates individually retained; not all classified as playable','common directional entry is user-observed, not a verified all-to-all relation','browser-local layout autosave is not a write to the HTML file; use export/import for backups']}
manifest['scripts']['scripts/player_graph_routing.js']=sha('scripts/player_graph_routing.js')
manifest['scripts']['scripts/player_graph_cells.js']=sha('scripts/player_graph_cells.js')
manifest['scripts']['scripts/player_graph_catalog.py']=sha('scripts/player_graph_catalog.py')
for source in ['exports/20261029-玩家招式名称-12/paired-texts.json','exports/20261029-玩家招式名称-12/skill-ui-links.json','exports/20261029-徒手补全与命名-13/actions-data.json','exports/20261029-徒手补全与命名-13/focus-data.json','exports/20261029-徒手补全与命名-13/conditional-attacks.json']:manifest['inputs'][source]=sha(source)
manifest['limits']=[x for x in manifest['limits'] if x!='conditional attacks remain opaque']+['57 conditional entries decoded as modifiers, not default extra nodes','3 ability actions added without invented combo edges','5 barehand focus actions on own page; combo followups not yet recovered']
(OUT/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(coverage['summary'],ensure_ascii=True))

# Human-readable coverage is generated from the same identity mapping as the tooltips.
by_display={n['id']:n for n in data['graph']['nodes']}
note='# 徒手节点覆盖核对\n\n[[03配置/玩家攻击/徒手招式板小样|图的使用说明]] · [[03配置/玩家攻击/阅读入口|阅读入口]]\n\n'
note+='[打开徒手招式图]('+vault_html.as_uri()+') · [打开徒手专注]('+(vault_html.parent/'徒手专注.html').as_uri()+')\n\n'
note+='13版保留原33个连招位置及全部63条源边，补入抓取后推掷、攻击倒地对手、倒地格挡反击3个独立能力入口，共36节点。独立入口暂未接通与普通节点的具体边，未伪造连线。原布局恢复时保留旧节点格位，新节点补入空格；新增前JSON另存浏览器备份。\n\n'
note+='名称气泡按下表的官方菜单身份对应；整套连招名有范围说明，不代表其中每击有独立官方名。没有找到独立名的节点明确采用操作称呼。\n\n| 官方菜单名称 | 图中位置／操作称呼 |\n|---|---|\n'
for r in data['completeness']['menuCoverage']:
    note+='| '+r['name']+' | '+'、'.join(by_display[i]['label'] for i in r['nodes'])+' |\n'
note+='\n徒手专注另页包含'+ '、'.join(f['name'] for f in focusSource['nodes'])+'，各自列消耗与覆盖命中表。实际弱点对象的m_Name直接指向FocusNames；不能拿旧技能UI的解除武器名套给戳眼。敌人可覆盖参数，表行不是动画整段最终总效果。专注结束的动作许可／具体跟进尚未恢复，未画推测后续边。\n\n'
note+='条件Map已对57原节点完全读取，21非空、57条件条目全部为Attack.Modifiers替换设置，引用70动作，其中51来自先前88树外候选。它们留在原节点的替换配置证据，不作默认新增节点。其余37候选含21旧版、10特殊、6常规；六常规在既有tagged属性范围未查到入口，仍留覆盖审计，不因文件存在就加点。\n\n'
note+='证据底稿：notes/player-completeness-13-conditional.md与notes/player-completeness-13-actions.md；批次数据／验证在exports/20261029-徒手补全与命名-13/。未运行游戏，不宣称完整穷尽所有运行期动作。\n'
(ROOT/'Sifu/03配置/玩家攻击/徒手节点覆盖核对.md').write_text(note,encoding='utf-8')
