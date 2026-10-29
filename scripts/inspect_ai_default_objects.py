"""Read complete property-only default-object exports; no blueprint bytecode execution."""
import gzip,json,struct,sys
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch');BASE=R/'extracted';sys.path.insert(0,str(R/'tools'));import local_bounded_packages as q
ps=json.load(gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8'));out=[];fail=[]
def ref(p,i,seen=None):
 if i==0:return None
 seen=set() if seen is None else set(seen)
 if i in seen:return '<cycle>'
 seen.add(i)
 if i<0:
  if -i>len(p['imports']):return '<bad>'
  x=p['imports'][-i-1];prefix=ref(p,x['outer'],seen);name=x['name']
 else:
  if i>len(p['exports']):return '<bad>'
  x=p['exports'][i-1];prefix=ref(p,x['outerIndex'],seen);name=x['name']
 return (prefix+'.' if prefix else '')+name
def refs(props,p,prefix=''):
 result=[]
 for x in props:
  name=prefix+x['name']+'['+str(x['arrayIndex'])+']'
  if isinstance(x['value'],list):result+=refs(x['value'],p,name+'.')
  elif x['type']=='ObjectProperty' and isinstance(x['value'],int):result.append({'property':name,'ref':ref(p,x['value'])})
 return result
for p in ps:
 if not p['path'].startswith(('Sifu/Content/DB/AI/Archetypes/','Sifu/Content/Blueprints/AI/')):continue
 f=BASE/p['path'];ef=f.with_suffix('.uexp')
 if not ef.exists():continue
 b=ef.read_bytes();hs=f.stat().st_size
 for e in p['exports']:
  if not e['name'].startswith('Default__') or e['classIndex']<=0 or not (int(e['flags'],16)&0x10):continue
  st=e['serialOffset']-hs;end=st+e['serialSize']
  if not 0<=st<=end<=len(b):continue
  try:
   props,n=q.tags(b[st:end],p['names'])
   if st+n!=end:raise ValueError('Not complete CDO property body')
   out.append({'asset':p['path'],'export':e['name'],'class':ref(p,e['classIndex']),'properties':props,'object_references':refs(props,p),'uasset_sha256':p['uassetSha256']})
  except (ValueError,struct.error,UnicodeError) as ex:fail.append({'asset':p['path'],'export':e['name'],'reason':str(ex)})
with gzip.open(R/'inventory/stun-ai-default-objects.json.gz','wt',encoding='utf-8') as f:json.dump(out,f,ensure_ascii=False,separators=(',',':'))
(R/'inventory/stun-ai-default-object-results.json').write_text(json.dumps({'decoded':len(out),'unsupported':fail},ensure_ascii=False,indent=2),encoding='utf-8')
print('Decoded',len(out),'Unsupported',len(fail))
for x in out:
 if 'Grunt' in x['asset'] and any(s in x['asset'] for s in ('BP_Grunt_Base.uasset','ArchetypeDB_Base_Master')):
  print(x['asset'],x['export'],json.dumps(x['object_references'],ensure_ascii=False))

