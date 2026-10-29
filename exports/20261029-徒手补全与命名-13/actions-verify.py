from pathlib import Path
import json,gzip,hashlib,sys,ast
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
f=json.loads((O/'focus-data.json').read_text(encoding='utf-8'));a=json.loads((O/'actions-data.json').read_text(encoding='utf-8'));cs=json.loads((O/'actions-ability-cdos.json').read_text(encoding='utf-8'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(n,b):checks.append({'name':n,'passed':bool(b)})
check('five barehand shared focus definitions',len(f['nodes'])==5 and {n['en'] for n in f['nodes']}=={'Eye Strike','Vertical Strikes','Strong Sweep','Double Palm','Calbot'})
check('no claimed focus combo edges',f['edges']==[] and all(n['followups']==[] for n in f['nodes']))
check('all focus definitions bind real hit rows',all(n['hitTable'].endswith('VitalPoint_HitBoxData.uasset') and n['hitRow'] and n['hitProperties'] for n in f['nodes']))
check('all focus names exact FText references',all(n['nameText']['namespace']=='FocusNames' and n['nameText']['uexp_offset']>=0 for n in f['nodes']))
check('focus source files unchanged',all(sha(R/'extracted'/n['asset'])==n['source_sha256'] and sha((R/'extracted'/n['asset']).with_suffix('.uexp'))==n['uexp_sha256'] for n in f['nodes']))
check('five selected ability CDOs fully consumed',len(cs)==5 and all(c['consumed']==c['bytes'] and not c['trailing_hex'] for c in cs))
check('ability original hashes unchanged',all(sha(R/'extracted'/c['asset'])==c['source_sha256'] and sha((R/'extracted'/c['asset']).with_suffix('.uexp'))==c['uexp_sha256'] for c in cs))
check('three separate action entries',len(a['supplementaryNodes'])==3 and {n['key'] for n in a['supplementaryNodes']}=={'directional-throw','downed-target-attack','ground-parry-counter'})
check('no invented AttackDB or combo edges for ability entries',all(n['attackAssets']==[] and n['edges']==[] for n in a['supplementaryNodes']))
ground=next(n for n in a['supplementaryNodes'] if n['key']=='ground-parry-counter')
check('ground counter requires saved skill tag',ground['abilityProperties']['ActivationRequiredTags[0]']==['Skills.Actions.OTGParryCounter'])
check('downed-target normal and hold both retained',len(next(n for n in a['supplementaryNodes'] if n['key']=='downed-target-attack')['inputEntries'])==2)
for p in O.glob('actions-*.py'):ast.parse(p.read_text(encoding='utf-8'));check('syntax '+p.name,True)
sources=['inventory/tagged-objects.json.gz','inventory/package-metadata.json.gz','inventory/data-tables.json.gz','tools/local_bounded_packages.py','exports/20261029-玩家招式名称-12/paired-texts.json','exports/20261029-玩家招式名称-12/skill-ui-links.json']
report={'status':'passed' if all(c['passed'] for c in checks) else 'failed','checks':checks,'python':sys.version,'commands':['python exports/20261029-徒手补全与命名-13/actions-focus-research.py','python exports/20261029-徒手补全与命名-13/actions-recommend.py','python exports/20261029-徒手补全与命名-13/actions-verify.py'],'source_sha256':{p:sha(R/p) for p in sources},'script_sha256':{p.name:sha(p) for p in O.glob('actions-*.py')},'limits':['saved shared config, not runtime validation','player ability registration and post-focus action availability not restored','no new game extraction or code disassembly']}
(O/'actions-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'failed':[c['name'] for c in checks if not c['passed']]}))
raise SystemExit(report['status']!='passed')
