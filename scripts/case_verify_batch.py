"""Validate the case-study batch's tables, inputs and exact evidence files. No gameplay claims."""
from pathlib import Path
import json,hashlib,re,datetime,sys,ast
R=Path(__file__).resolve().parents[1];V=R/'Sifu';errors=[];checks=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(p,expected=None):
 p=Path(p);ok=p.is_file() and (expected is None or sha(p)==expected);checks.append({'path':str(p),'passed':ok,'sha256':sha(p) if p.is_file() else None})
 if not ok:errors.append('Missing/hash mismatch '+str(p))
m=json.loads((R/'inventory/case-study-documents.json').read_text(encoding='utf-8'))
for f in m['sources']:check(R/f['path'],f['sha256'])
t=json.loads((R/'inventory/player-combo-graphs.json').read_text(encoding='utf-8'));t=next(x for x in t['trees'] if x['asset']==m['source_graph'])
for ext,key in [('.uasset','uasset_sha256'),('.uexp','uexp_sha256')]:check((R/'extracted'/t['asset']).with_suffix(ext),t[key])
for f in ['inventory/case-movement-disassembly.json','inventory/case-defense-events-disassembly.json','inventory/case-defense-init-20261028-disassembly.json','inventory/case-defense-init2-20261028-disassembly.json']:
 p=R/f
 if not p.exists():continue
 a=json.loads(p.read_text(encoding='utf-8-sig'))
 for x in a['procedures']:
  if x['status']=='disassembled':check(Path(x['file']),x['assembly_sha256'])
  else:errors.append('Unresolved case function '+x['name'])
a=json.loads((R/'inventory/case-defense-20261028.json').read_text(encoding='utf-8'))
for x in a.get('existing_primary_evidence',[]):check(R/x['file'],x['sha256'])
# Validate the specifically extracted packages and the newly decoded service/notify values.
a=json.loads((R/'inventory/case-resilience-extraction-20261028.json').read_text(encoding='utf-8'))
for x in a['files']:check(x['path'],x['sha256'])
if a['missing']:errors.append('Missing targeted resilience files')
a=json.loads((R/'inventory/case-resilience-notifies-20261028.json').read_text(encoding='utf-8'))
if sorted(x['m_iBonus'] for x in a['services'])!=[2,4]:errors.append('Service bonus evidence changed')
if len(a['animations'])!=2:errors.append('Expected two targeted notification samples')
for x in a['animations']:
 for n in x['orderServiceNotifyEvents']:
  if abs((n['endLinkValue']-n['startLinkValue'])-n['duration'])>1e-6:errors.append('Notify link/duration mismatch '+x['path'])

# Independent paragraph and table consistency, not mechanism validity.
tables=0
for rel in m['documents']:
 p=V/rel;check(p);prev=None
 for no,line in enumerate(p.read_text(encoding='utf-8').splitlines(),1):
  if line.startswith('|'):
   n=len(re.findall(r'(?<!\\)\|',line))-1
   if prev is not None and n!=prev:errors.append(f'Table column mismatch {rel}:{no}')
   if prev is None:tables+=1
   prev=n
  else:prev=None
s=(V/'01机制/受击与追击案例.md').read_text(encoding='utf-8')
for i in range(1,10):
 if not re.search(r'^## C'+str(i).zfill(2)+r'：',s,re.M):errors.append('Missing case C'+str(i).zfill(2))
if len(m['selected_impact_rows'])!=7:errors.append('Selected impact source rows changed')
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'passed' if not errors else 'failed','python':sys.version,'command':r'D:\Programes\PY\python.exe scripts/case_verify_batch.py','script_sha256':sha(Path(__file__)),'source_and_output_checks':checks,'tables':tables,'case_count':9,'errors':errors,'not_verified':['Gameplay continuity or first block frame','Normal-difficulty encounter instance selection','Obsidian Mermaid visual rendering','All indirect callers of defense update']}
(R/'inventory/case-study-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'status':report['status'],'checks':len(checks),'tables':tables,'cases':9,'errors':errors},ensure_ascii=True));raise SystemExit(bool(errors))
