"""Integrity checks for the bounded 20261029 rules batch; never asserts gameplay behavior."""
from pathlib import Path
import json,hashlib,ast,sys,datetime,re
R=Path(__file__).resolve().parents[1];checks=[];errors=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(p,expected=None):
 p=Path(p);ok=p.is_file() and (expected is None or sha(p)==expected)
 checks.append({'path':str(p.relative_to(R)) if p.is_relative_to(R) else str(p),'sha256':sha(p) if p.is_file() else None,'passed':ok})
 if not ok:errors.append('Missing/hash mismatch '+str(p))
expected='a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254'
exe=Path(json.loads((R/'inventory/pdb_overview.json').read_text(encoding='utf-8'))['exe']);check(exe,expected)
for n in ['notes/20261029-rules-resolution.md','notes/20261029-rules-hit-count.md','notes/20261029-rules-state-update.md']:
 p=R/n;check(p)
 if p.is_file():
  for ref in re.findall(r'(?:logs|inventory|scripts)/[\w./-]+\.(?:json|py|txt)',p.read_text(encoding='utf-8')):check(R/ref)
manifest_checks=[];partial_queries=[]
for p in sorted((R/'inventory').glob('*20261029*disassembly.json')):
 a=json.loads(p.read_text(encoding='utf-8-sig'))
 if a.get('exe_sha256')!=expected:errors.append('EXE manifest mismatch '+p.name)
 for x in a.get('procedures',[]):
  if x.get('status')=='disassembled':check(Path(x['file']),x['assembly_sha256'])
  elif x.get('status')=='not-in-index' and x.get('name')=='UDefenseComponent::GetFightingStateTimeLeft':
   partial_queries.append({'manifest':p.name,'name':x['name'],'status':x['status'],'resolution':'The exact BPF_GetFightingStateTimeLeft wrapper was found and inspected instead; the absent spelling remains an unsuccessful query.'})
  else:errors.append('Unresolved procedure '+str(x.get('name')))
 manifest_checks.append(p.name)
# Assert the exact source identities used to interpret the guard-result branch.
a=json.loads((R/'inventory/followup-hitted-type-layouts.json').read_text(encoding='utf-8'))
for name,member,offset in [('FImpactResult','m_eGuardType',30),('FImpactResult','m_bAvoidDizzy',191)]:
 t=next(x for x in a['layouts'] if x['name']==name)
 f=next(x for x in t['fields'] if x.get('name')==member)
 if f.get('offset_bytes')!=offset:errors.append('Type identity mismatch '+name+'.'+member)
syntax=[]
for p in sorted((R/'scripts').glob('rules*.py')):
 try:ast.parse(p.read_text(encoding='utf-8-sig'),filename=str(p));syntax.append({'path':str(p.relative_to(R)),'sha256':sha(p)})
 except SyntaxError as e:errors.append(str(e))
a=json.loads((R/'inventory/20261029-parry-condition.json').read_text(encoding='utf-8'))
for ext,key in [('.uasset','uasset_sha256'),('.uexp','uexp_sha256')]:check((R/'extracted'/a['asset']).with_suffix(ext),a[key])
if (a['serialized_bytes'],a['vm_bytes'])!=(1517,985):errors.append('Previous bounded BP decode scope changed')
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'passed' if not errors else 'failed','command':r'D:\Programes\PY\python.exe scripts/rules_verify_20261029.py','python':sys.version,'script_sha256':sha(Path(__file__)),'checks':checks,'disassembly_manifests':manifest_checks,'unsuccessful_queries':partial_queries,'syntax':syntax,'errors':errors,'not_verified':['Gameplay or exact frame ordering','All possible character state/default overrides','Mermaid visual rendering','Any unresolved rule explicitly retained in the notes']}
(R/'inventory/rules-20261029-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps({'status':report['status'],'checks':len(checks),'manifests':len(manifest_checks),'scripts':len(syntax),'errors':errors},ensure_ascii=True));raise SystemExit(bool(errors))
