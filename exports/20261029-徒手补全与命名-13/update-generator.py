from pathlib import Path
R=Path(__file__).resolve().parents[2]
p=R/'scripts/build_player_board.py';s=p.read_text(encoding='utf-8').replace('20261029-玩家招式图-10','20261029-徒手补全与命名-13')
s=s.replace('from player_graph_model import build_graph','from player_graph_model import build_graph\nfrom player_graph_catalog import apply_names,hit_window,supplemental_node')
needle="data['graph']=build_graph(data)"
addition='''data['graph']=build_graph(data)
data['page']='barehands'
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
'''
assert needle in s;s=s.replace(needle,addition)
needle="vault_html.write_bytes((OUT/'player-board.html').read_bytes())"
addition=needle+"\nfocus_html=template.replace('__DATA__',json.dumps(focusData,ensure_ascii=False).replace('</','<\\\\/'))\n(OUT/'focus-board.html').write_text(focus_html,encoding='utf-8')\n(vault_html.parent/'徒手专注.html').write_text(focus_html,encoding='utf-8')\n(OUT/'focus-data.json').write_text(json.dumps(focusData,ensure_ascii=False,indent=2),encoding='utf-8')"
s=s.replace(needle,addition)
s=s.replace("manifest['scripts']['scripts/player_graph_cells.js']=sha('scripts/player_graph_cells.js')", "manifest['scripts']['scripts/player_graph_cells.js']=sha('scripts/player_graph_cells.js')\nmanifest['scripts']['scripts/player_graph_catalog.py']=sha('scripts/player_graph_catalog.py')\nfor source in ['exports/20261029-玩家招式名称-12/paired-texts.json','exports/20261029-玩家招式名称-12/skill-ui-links.json','exports/20261029-徒手补全与命名-13/actions-data.json','exports/20261029-徒手补全与命名-13/focus-data.json','exports/20261029-徒手补全与命名-13/conditional-attacks.json']:manifest['inputs'][source]=sha(source)\nmanifest['limits']=[x for x in manifest['limits'] if x!='conditional attacks remain opaque']+['57 conditional entries decoded as modifiers, not default extra nodes','3 ability actions added without invented combo edges','5 barehand focus actions on own page; combo followups not yet recovered']")
p.write_text(s,encoding='utf-8')
