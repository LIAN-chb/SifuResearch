"""Verify this incremental unpacking batch; does not assert runtime behavior."""
from pathlib import Path
import json,hashlib,re,datetime
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
errors=[];checks=[];inputs=[]
for filename in ['followup-hitted-assets.json','followup-hitted-services-assets.json']:
 p=R/'inventory'/filename
 if not p.is_file():continue
 a=json.loads(p.read_text(encoding='utf-8'));inputs.append({'file':str(p),'sha256':sha(p)})
 for f in a['files']:
  q=Path(f['path']);ok=q.is_file() and sha(q)==f['sha256'];checks.append({'file':str(q),'passed':ok})
  if not ok:errors.append('Extracted source hash '+str(q))
# Supplement source manifests from the two independently researched branches.
def check_asset(rel,ext,digest):
 candidates=[R/'extracted'/rel,R/'logs/followup-order-services/extracted'/rel]
 for base in candidates:
  q=base.with_suffix(ext)
  if q.is_file() and sha(q)==digest:
   checks.append({'file':str(q),'passed':True});return
 errors.append('Source absent or hash mismatch '+rel+ext)
for a in json.loads((R/'inventory/followup-order-services-packages.json').read_text(encoding='utf-8')):
 for ext,key in [('.uasset','uassetSha256'),('.uexp','uexpSha256')]:
  if key in a:check_asset(a['path'],ext,a[key])
for a in json.loads((R/'inventory/followup-parry-ai-assets.json').read_text(encoding='utf-8'))['source_asset_hashes']:
 for ext,f in a['files'].items():check_asset(a['asset'],ext,f['sha256'])

g=json.loads((R/'inventory/followup-gap-classification.json').read_text(encoding='utf-8'))
if len(g['records'])!=825:errors.append('Historical gap inventory changed')
for x in g['records']:
 if 'uasset_sha256' not in x:continue
 p=R/'extracted'/x['asset']
 for f,key in [(p,'uasset_sha256'),(p.with_suffix('.uexp'),'uexp_sha256')]:
  ok=f.is_file() and sha(f)==x[key];checks.append({'file':str(f),'passed':ok})
  if not ok:errors.append('Reparse source hash '+str(f))
if len(g['unmatched_hitbox_references'])!=13:errors.append('Unmatched reference inventory changed')
source=json.loads((R/'inventory/followup-hitted-assets.json').read_text(encoding='utf-8'));catalog=json.loads((R/'inventory/followup-hitted-catalog-table.json').read_text(encoding='utf-8'));expected=[]
for o in source['objects']:
 if not o['export'].startswith('Default__'):continue
 ar=next(f for f in o['properties'] if f['name']=='m_OrderServices')['value'][0]
 if 'arrayElements' not in ar:errors.append('Opaque Hitted service array')
 order=o['asset'].split('/')[-1].removesuffix('.uasset')
 expected +=[(order,i) for i in range(len(ar.get('arrayElements',[])))]
if sorted(expected)!=sorted((x['order'],x['index']) for x in catalog):errors.append('Catalog service identity mismatch')
if len(expected)!=33:errors.append('Expected 30+3 service config records')
# Validate the shape of this batch's new notes; general vault checker owns wiki-links and assemblies.
notes=[p for p in (V/'03配置/订单与服务').glob('*.md')]+[V/'00索引/解包与解析进度.md',V/'03配置/AI防御/Grunt反击条件与动作.md',V/'00索引/系统线索与关系图.md',V/'01机制/连续受击与反击追击的系统链.md',V/'02实现/连续受击与反击追击的系统链.md']
tables=[]
for p in notes:
 last=None
 for i,line in enumerate(p.read_text(encoding='utf-8-sig').splitlines(),1):
  if line.startswith('|'):
   cols=len(re.findall(r'(?<!\\)\|',line))-1
   if last is not None and cols!=last:errors.append(f'Table columns {p}:{i}: {cols}!={last}')
   if last is None:tables.append({'note':str(p),'line':i,'columns':cols})
   last=cols
  else:last=None
report={'checked_at':datetime.datetime.now().astimezone().isoformat(),'status':'passed' if not errors else 'failed','inputs':inputs,'source_hash_checks':checks,'unique_source_files':len({x['file'] for x in checks}),'hitted_services_checked':len(expected),'tables':tables,'errors':errors,'not_verified':['Runtime gameplay','Exact per-frame ordering under prediction/freeze','Obsidian Mermaid visual rendering']}
(R/'inventory/followup-unpacking-verification.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'status':report['status'],'source_hash_checks':len(checks),'unique_sources':report['unique_source_files'],'hitted_services':len(expected),'tables':len(tables),'errors':errors},ensure_ascii=True))
raise SystemExit(bool(errors))