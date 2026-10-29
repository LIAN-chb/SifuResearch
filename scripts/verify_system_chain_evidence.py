import hashlib,json,re,datetime
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
a=json.loads((R/'inventory/system-defense-ability-cdos.json').read_text(encoding='utf-8'));errors=[];checks=[]
for x in a['objects']:
 for suffix,field in [('.uasset','uasset_sha256'),('.uexp','uexp_sha256')]:
  p=(R/'extracted'/x['asset']).with_suffix(suffix);ok=p.is_file() and sha(p)==x[field]
  checks.append({'path':str(p),'passed':ok})
  if not ok:errors.append(str(p))
order=json.loads((R/'inventory/system-avoid-orderdb.json').read_text(encoding='utf-8'))
p=R/'logs/system-avoid/orderdb'/order['path'];ok=sha(p)==order['uassetSha256'];checks.append({'path':str(p),'passed':ok})
if not ok:errors.append(str(p))
# Check table source shape only on this task's new/rewritten notes.
tables=[]
for rel in ['00索引/系统线索与关系图.md','01机制/连续受击与反击追击的系统链.md','02实现/连续受击与反击追击的系统链.md','01机制/防反与闪避反击后的追击.md','02实现/防反与闪避反击后的追击.md']:
 lines=(V/rel).read_text(encoding='utf-8').splitlines();last=None
 for i,line in enumerate(lines,1):
  if line.startswith('|'):
   cols=len(re.findall(r'(?<!\\)\|',line))-1
   if last is not None and cols!=last:errors.append(f'Table columns {rel}:{i}: {cols} != {last}')
   if last is None:tables.append({'file':rel,'start':i,'columns':cols})
   last=cols
  else:last=None
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'passed' if not errors else 'failed','asset_hash_checks':checks,'tables_checked':tables,'errors':errors,'not_verified':['Mermaid rendering in Obsidian','Runtime gameplay','Conditional layer composition on concrete enemy instances']}
(R/'inventory/system-chain-evidence-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'status':report['status'],'asset_hashes':len(checks),'tables':len(tables),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))