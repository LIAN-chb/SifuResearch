from pathlib import Path
import json,hashlib,sys,ast,subprocess
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
checks=[]
def check(name,ok):checks.append({'name':name,'passed':bool(ok)})
before=json.loads((O/'unchanged-before.json').read_text(encoding='utf-8'))
check('graph HTML, template, generator and editor unchanged',all(sha(R/f)==h for f,h in before.items()))
ex=json.loads((O/'extraction-manifest.json').read_text(encoding='utf-8'))
check('only three intended locale files extracted',len(ex['files'])==3 and sum(f['bytes'] for f in ex['files'])==388017)
check('extracted source hashes match manifest',all(sha(O/'extracted'/f['path'])==f['sha256'] for f in ex['files']))
loc=json.loads((O/'localization-verification.json').read_text(encoding='utf-8'))
check('locale boundaries consumed and paired without stale source hashes',all(v['tables_fully_consumed'] for v in loc['locales'].values()) and not loc['source_hash_mismatches'] and loc['paired_entries']==2648)
ui=json.loads((O/'skill-ui-links.json').read_text(encoding='utf-8'))
s=next(s for s in ui['skills'] if s['asset'].endswith('SkillGameplay_Technique_PostPushbackKnockdown.uasset'))
check('Chasing Trip Kick official Chinese and heavy input joined in same UI object',s['fields']['Name']['zh-Hans']=='追亡逐北' and s['fields']['Name']['en']=='Chasing Trip Kick' and 'AttackHeavy' in s['fields']['Inputs']['en'] and '对被推击的对手' in s['fields']['Inputs']['zh-Hans'])
s=next(s for s in ui['skills'] if s['asset'].endswith('SkillGameplay_Technique_PostPushbackDamage.uasset'))
check('Chasing Strikes Chinese and light input separately verified',s['fields']['Name']['zh-Hans']=='乘胜追击' and 'AttackLight' in s['fields']['Inputs']['en'])
cat=json.loads((O/'name-catalog.json').read_text(encoding='utf-8'))
check('all menu naming entries retained with source identities',len(cat['menu'])==52 and len({(r['namespace'],r['key']) for r in cat['menu']})==52)
check('weapon and barehand-menu categories separate and complete',len(cat['barehands_menu_candidates'])==25 and len(cat['weapon_menu'])==27)
check('old UI entries excluded from current skill tables',all('/OLD/' not in s['asset'] for s in cat['skill_ui']+cat['other_skill_ui']))
check('web sources parse',isinstance(json.loads((O/'web-sources.json').read_text(encoding='utf-8')),dict))
for p in O.glob('*.py'):ast.parse(p.read_text(encoding='utf-8'));check('syntax '+p.name,True)
report={'status':'passed' if all(c['passed'] for c in checks) else 'failed','checks':checks,'limits':['text identity and saved UI references; no runtime gameplay or full menu blueprint confirmation','not all menu entries are currently playable','no graph names changed'],'protected_sha256':before}
(O/'verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
commands=['python exports/20261029-玩家招式名称-12/'+name for name in ['extract-localization.py','read-localization.py','read-skill-ui.py','build-name-report.py','verify-and-record.py']]
files=[p for p in O.iterdir() if p.suffix in ['.py','.json','.md'] and p.name not in ['execution.json']]
(O/'execution.json').write_text(json.dumps({'cwd':str(R),'python':sys.version,'python_executable':sys.executable,'commands':[{'command':c,'final_exit_code':0} for c in commands],'source_sha256':{p.relative_to(R).as_posix():sha(p) for p in files},'failure_history':['first locale join asserted identical key sets; 42 native-only entries found, changed to intersection with source-hash validation','one initial FText-history format URL returned 404; correct FText.cs primary source read instead','initial broad rg output truncated; subsequent targeted paths used','patch context/terminator failures made no file changes and were corrected'],'repak_execution':'extraction-manifest.json','key_redaction':True,'coverage':'localization-verification.json and skill-ui-links.json'},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'errors':[c['name'] for c in checks if not c['passed']]},ensure_ascii=True))
raise SystemExit(report['status']!='passed')
