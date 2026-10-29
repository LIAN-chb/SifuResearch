"""Read only complete CDO properties for DB/Abilities defense-related assets."""
import gzip,json,struct,sys,hashlib
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(r'E:\ProgrameFiles\SifuResearch');sys.path.insert(0,str(R/'tools'));import local_bounded_packages as q
with gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8') as f:pkgs=json.load(f)
def ref(p,i):
 if i==0:return None
 x=p['imports'][-i-1] if i<0 else p['exports'][i-1];parent=ref(p,x['outer'] if i<0 else x['outerIndex'])
 return (parent+'.' if parent else '')+x['name']
def refs(ps,p,prefix=''):
 out=[]
 for x in ps:
  key=prefix+x['name']+'['+str(x.get('arrayIndex',0))+']'
  if isinstance(x.get('value'),list):out+=refs(x['value'],p,key+'.')
  elif x['type']=='ObjectProperty':out.append({'property':key,'ref':ref(p,x['value'])})
 return out
out=[];errors=[]
for p in pkgs:
 if not p['path'].startswith('Sifu/Content/DB/Abilities/'):continue
 path=R/'extracted'/p['path'];payload=path.with_suffix('.uexp').read_bytes()
 for e in p['exports']:
  if not e['name'].startswith('Default__') or e['classIndex']<=0 or not int(e['flags'],16)&0x10:continue
  begin=e['serialOffset']-path.stat().st_size;end=begin+e['serialSize']
  if not 0<=begin<=end<=len(payload):raise ValueError('Bounds')
  try:
   props,n=q.tags(payload[begin:end],p['names'])
   if n!=end-begin:raise ValueError('Incomplete CDO')
   out.append({'asset':p['path'],'export':e['name'],'class':ref(p,e['classIndex']),'properties':props,'object_references':refs(props,p),'uasset_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'uexp_sha256':hashlib.sha256(payload).hexdigest()})
  except (ValueError,struct.error) as ex:errors.append({'asset':p['path'],'export':e['name'],'error':str(ex)})
(R/'inventory/system-defense-ability-cdos.json').write_text(json.dumps({'objects':out,'failures':errors},ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
print(json.dumps({'decoded':len(out),'failures':errors,'assets':[x['asset'] for x in out]},ensure_ascii=True))
