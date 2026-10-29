from pathlib import Path
import gzip,json,hashlib,importlib.util,struct
R=Path(__file__).resolve().parents[2]
spec=importlib.util.spec_from_file_location('bounded13',R/'tools/local_bounded_packages.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
pkgs=json.loads(gzip.decompress((R/'inventory/package-metadata.json.gz').read_bytes()))
pkg=next(p for p in pkgs if p['path'].endswith('/MainChar_ComboTree.uasset'))
asset=R/'extracted'/pkg['path'];b=asset.with_suffix('.uexp').read_bytes();e=next(e for e in pkg['exports'] if e['name']=='MainChar_ComboTree');raw=b[e['serialOffset']-asset.stat().st_size:e['serialOffset']-asset.stat().st_size+e['serialSize']]
ps,n=q.tags(raw,pkg['names']);arr=next(p for p in ps if p['name']=='m_Nodes');chunk=raw[arr['valueOffset']:arr['valueOffset']+arr['size']]
r=q.Reader(chunk,pkg['names']);count=r.number('i');name=r.name();typ=r.name();size=r.number('i');idx=r.number('i');st=r.name();r.take(16);has=r.number('B');assert has==0
print('header',count,name,typ,size,st,r.position)
nodes=[]
for i in range(count):
 start=r.position;node,n=q.tags(chunk[start:],pkg['names']);r.position+=n
 p=next(p for p in node if p['name']=='m_ConditionalAttacks');data=chunk[start+p['valueOffset']:start+p['valueOffset']+p['size']]
 nodes.append((i,data,p))
 if len(data)>8:
  print('node',i,'size',len(data),'start',data[:100].hex(),'types',p.get('key'),p.get('value'))
  rr=q.Reader(data,pkg['names']);print('counts',rr.number('i'),rr.number('i'))
  try:
   kp,kn=q.tags(data[8:],pkg['names']); print('key-tag',kp,kn); vp,vn=q.tags(data[8+kn:],pkg['names']); print('value',[(x['name'],x['type'],x['size'],x['value']) for x in vp],vn)
  except Exception as ex:print(type(ex).__name__,str(ex))
assert r.position==len(chunk)
