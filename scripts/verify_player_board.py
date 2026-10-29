"""Check source coverage and in-vault file links for the player board."""
from pathlib import Path
from urllib.parse import urlparse,unquote
import json,re,hashlib
R=Path(__file__).resolve().parents[1];O=R/'exports/20261029-玩家招式图-10'
d=json.loads((O/'board-data.json').read_text(encoding='utf-8'))
t=next(t for t in json.loads((R/'inventory/player-combo-graphs.json').read_text(encoding='utf-8'))['trees'] if t['asset'].endswith('/MainChar_ComboTree.uasset'))
errors=[];checks=[]
def check(name,ok):
    checks.append({'name':name,'passed':bool(ok)})
    if not ok:errors.append(name)
check('every source node registered',set(d['nodes'])=={str(i) for i in range(len(t['nodes']))})
represented=[e['index'] for n in d['nodes'].values() for e in n['edges']]+[e['edge'] for e in d['starts']]
check('every saved edge registered exactly once',sorted(represented)==list(range(len(t['edges']))))
check('every default input registered',len(d['defaults'])==len(t['defaults']))
for i,n in enumerate(t['nodes']):
    refs=[];info=n.get('m_AttackInfos[0]',{})
    for block in [info]+info.get('m_ChargedAttacks[0]',[]):
        refs.extend(v for k,v in block.items() if k.startswith('m_Attacks[') and isinstance(v,str) and v.startswith('/Game/'))
    expected={'Sifu/Content/'+r[6:].split('.')[0]+'.uasset' for r in refs}
    check('all base/charge references at node '+str(i),expected=={v['asset'] for v in d['nodes'][str(i)]['variants']})
cards=[i for row in d['groups'].values() for i in row]
check('canonical cards exactly once',len(cards)==len(set(cards)) and set(cards)=={n['target'] for n in d['nodes'].values()})
check('no referenced tree action missing',not d['coverage']['unresolvedAssets'])
check('no referenced tree hit row missing',not d['coverage']['unresolvedHitRows'])
check('all tree-external candidates carry parsed attributes',set(d['outsideAttacks'])=={x['asset'] for x in d['coverage']['outsideTree']} and all(a['parsed'] for a in d['outsideAttacks'].values()))
links=[]
for rel in ['阅读入口.md','输入衔接图-徒手.md','徒手招式板小样.md']:
    p=R/'Sifu/03配置/玩家攻击'/rel;s=p.read_text(encoding='utf-8')
    targets=re.findall(r'\]\((file:///[^)]+\.html)\)',s)
    check('direct HTML link '+rel,bool(targets))
    for uri in targets:
        target=Path(unquote(urlparse(uri).path).lstrip('/'))
        check('link target exists '+rel,target.is_file());links.append({'page':str(p.relative_to(R)),'uri':uri,'target':str(target)})
check('vault and export HTML match',(R/'Sifu/03配置/玩家攻击/招式板/徒手招式板.html').read_bytes()==(O/'player-board.html').read_bytes())
report={'status':'failed' if errors else 'passed','checks':checks,'errors':errors,'links':links,'summary':d['coverage']['summary'],'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limitations':['Static saved input coverage, not runtime completeness','Conditional overrides and input gestures not decoded by this check']}
g=d['graph']
check('all original nodes mapped into the graph',sorted(i for n in g['nodes'] for i in n['rawNodes'])==list(range(len(t['nodes']))))
check('all canonical configurations retained',sorted(i for n in g['nodes'] for i in n['configs'])==sorted({n['target'] for n in d['nodes'].values()}))
graph_edges=[v['index'] for e in g['edges'] for v in e['variants']]+[e['index'] for e in g['internalEdges']]+[e['edge'] for e in g['starts']]
check('display grouping preserves all 63 input edge identities',sorted(graph_edges)==list(range(len(t['edges']))))
check('expected neighbour-equivalent configurations merged',{tuple(x['members']) for x in g['merges'] if x['kind']=='equal-neighbours'}=={(2,17,18),(22,23),(25,26)})
check('routing-only entry is not shown as another attack',g['rawToDisplay']['1']==g['rawToDisplay']['2'])
check('unknown isolated relationships do not merge distinct inputs',len({g['rawToDisplay'][str(i)] for i in [31,51,55,56]})==4)
check('no graph node contains numerical properties in its label',all(not any(w in n['label'] for w in ['生命','架势','硬直','伤害','m_']) for n in g['nodes']))
check('layout node centres are unique',len({(n['x'],n['y']) for n in g['nodes']})==len(g['nodes']))
check('common directional entry keeps user provenance',g['reportedCommonInput']['targets']==[31,32,36,39] and '用户观察' in g['reportedCommonInput']['provenance'])
check('drawing model does not invent shared-entry source edges',all('sourceEdgeIndices' in e and all(i in range(len(t['edges'])) for i in e['sourceEdgeIndices']) for e in g['edges']))
prior=json.loads((R/'exports/20261029-玩家招式图-03/board-data.json').read_text(encoding='utf-8'))
prior=json.loads(json.dumps(prior,ensure_ascii=False).replace('轻击变体（手势待核）','短按轻击松开·变体').replace('重击变体（手势待核）','短按重击松开·变体'))
check('only researched labels and evidence added; all graph/config values preserved',{k:v for k,v in d.items() if k!='research'}==prior)
check('quadrant enum order confirmed',[d['research']['quadrants'][str(i)] for i in range(4)]==['FrontLeft','FrontRight','BackRight','BackLeft'])
check('avoid enum bits confirmed',[d['research']['avoidBits'][str(i)] for i in [1,2,4,8]]==['Jump','Duck','SideLeft','SideRight'])
check('display evidence sources unchanged',all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in d['research']['sources'].items()))
report.update(status='failed' if errors else 'passed',checks=checks,errors=errors,graph_nodes=len(g['nodes']))
(O/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))
