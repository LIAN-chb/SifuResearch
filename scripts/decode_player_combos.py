"""Bounded focused decoding of player Combo trees and byte->node target maps."""
import collections,gzip,hashlib,importlib.util,json,struct,sys
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(r'E:\ProgrameFiles\SifuResearch')
spec=importlib.util.spec_from_file_location('bounded_combo_reader',R/'tools/external_read_packages.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
with gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8') as f:packages=json.load(f)
with gzip.open(R/'inventory/tagged-objects.json.gz','rt',encoding='utf-8') as f:objects=json.load(f)
wanted=[o for o in objects if o['class']=='/Script/Sifu.Combo' and ('/_MainChar/' in o['asset'] or '/DB/Weapons/Combo/' in o['asset'])]
pkgmap={p['path']:p for p in packages};proofs=[];stats=collections.Counter()
def ref(pkg,i):
 if i==0:return None
 if i<0:
  x=pkg['imports'][-i-1];outer=ref(pkg,x['outer'])
  return (outer+'.' if outer else '')+x['name']
 x=pkg['exports'][i-1];outer=ref(pkg,x['outerIndex'])
 return (outer+'.' if outer else '')+x['name']
def primitive(rr,typ):
 if typ=='ByteProperty':return rr.number('B')
 if typ=='IntProperty':return rr.number('i')
 if typ=='NameProperty':return rr.name()
 raise ValueError('Unsupported map member '+typ)
def enrich(ps,data,pkg):
 for p in ps:
  raw=data[p['valueOffset']:p['valueOffset']+p['size']];v=p.get('value')
  if isinstance(v,list):enrich(v,raw,pkg)
  elif p['type']=='ObjectProperty':p['reference']=ref(pkg,v)
  elif p.get('struct') in ['GameplayTag','GameplayTagContainer']:
   rr=q.Reader(raw,pkg['names']);n=1 if p['struct']=='GameplayTag' else rr.number('i')
   if 0<=n<=10000 and len(raw)-rr.position==n*8:p['tagNames']=[rr.name() for _ in range(n)]
  elif p['type']=='MapProperty':
   rr=q.Reader(data,pkg['names'],p['offset']);assert rr.name()==p['name'];assert rr.name()=='MapProperty';rr.take(8)
   key,value=rr.name(),rr.name();p['mapValueType']=value
   if key in ['ByteProperty','NameProperty'] and value=='IntProperty':
    rr=q.Reader(raw,pkg['names']);removed_count=rr.number('i')
    if not 0<=removed_count<=10000:raise ValueError('Map removed count')
    removed=[primitive(rr,key) for _ in range(removed_count)];n=rr.number('i')
    if not 0<=n<=10000:raise ValueError('Map count')
    pairs=[{'key':primitive(rr,key),'value':rr.number('i')} for _ in range(n)]
    if rr.position!=len(raw):raise ValueError('Unconsumed map bytes')
    p['mapEntries']=pairs;p['mapRemovedKeys']=removed
    if p['name']=='m_TargetNodes':
     stats['target_maps']+=1;stats['target_entries']+=n
     proofs.append({'asset':pkg['path'],'field':p['name'],'key_type':key,'value_type':value,'bytes':len(raw),'sha256':hashlib.sha256(raw).hexdigest(),'removed_keys':removed,'pairs':pairs})
  elif p['type']=='ArrayProperty':
   rr=q.Reader(raw,pkg['names']);n=rr.number('i')
   if not 0<=n<=100000:raise ValueError('Array count')
   inner=p.get('inner')
   if inner=='StructProperty':
    try:
     an,at=rr.name(),rr.name();size,idx=rr.number('i'),rr.number('i');st=rr.name();rr.take(16);guid=rr.number('B')
     if guid==1:rr.take(16)
     elif guid!=0:raise ValueError('GUID')
     if an!=p['name'] or at!='StructProperty' or idx!=0 or size!=len(raw)-rr.position:raise ValueError('Array inner bounds')
     elements=[]
     for _ in range(n):
      payload=raw[rr.position:];ep,en=q.tags(payload,pkg['names']);enrich(ep,payload,pkg);elements.append(ep);rr.position+=en
     if rr.position!=len(raw):raise ValueError('Array trailing bytes')
     p['arrayElements']=elements;p['arrayStruct']=st
    except (ValueError,struct.error):stats['opaque_struct_arrays']+=1
   elif inner=='IntProperty' and len(raw)==4+n*4:p['arrayValues']=[rr.number('i') for _ in range(n)]
   elif inner=='NameProperty' and len(raw)==4+n*8:p['arrayValues']=[rr.name() for _ in range(n)]
def norm(ps):
 out={}
 for p in ps:
  k=p['name']+'['+str(p.get('arrayIndex',0))+']';v=p.get('value')
  if isinstance(v,list):v=norm(v)
  elif 'arrayElements' in p:v=[norm(x) for x in p['arrayElements']]
  elif 'mapEntries' in p:v={'entries':p['mapEntries'],'removed':p['mapRemovedKeys']}
  elif 'reference' in p:v={'index':v,'reference':p['reference']}
  elif 'tagNames' in p:v=p['tagNames']
  elif 'arrayValues' in p:v=p['arrayValues']
  out[k]=v
 return out
trees=[]
for o in wanted:
 pkg=pkgmap[o['asset']];p=R/'extracted'/o['asset'];payload=p.with_suffix('.uexp').read_bytes();exp=pkg['exports'][o['export_index']-1];start=exp['serialOffset']-p.stat().st_size;end=start+exp['serialSize']
 if not 0<=start<=end<=len(payload):raise ValueError('Export bounds')
 raw=payload[start:end];ps,n=q.tags(raw,pkg['names'])
 if raw[n:]!=b'\0'*4:raise ValueError('UObject suffix')
 enrich(ps,raw,pkg);d=norm(ps);nodes=d['m_Nodes[0]'];edges=[]
 def emit(source,container):
  for ti,t in enumerate(container.get('m_Transitions[0]',[])):
   target=t.get('m_TargetNodes[0]',{})
   if 'entries' not in target:raise ValueError('Undecoded target map')
   for e in target['entries']:
    idx=e['value']
    if idx!=-1 and not 0<=idx<len(nodes):raise ValueError('Target node outside array')
    edges.append({'source':source,'input':t.get('m_eInputTransition[0]'),'condition':t.get('m_ConditionInstance[0]'),'condition_result':e['key'],'target':idx,'probability':t.get('m_fProbability[0]'),'transition_index':ti})
 for i,node in enumerate(nodes):emit('N'+str(i),node.get('m_Transitions[0]',{}))
 starts=d.get('m_ComboStartNodesContainer[0]',[])
 for i,x in enumerate(starts):emit('S'+str(i),x.get('m_ComboTransitions[0]',{}))
 tree={'asset':o['asset'],'uasset_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'uexp_sha256':hashlib.sha256(payload).hexdigest(),'nodes':nodes,'starts':starts,'edges':edges,'defaults':{k:v for k,v in d.items() if k.startswith('m_DefaultAttacks[')},'root':d}
 trees.append(tree);stats['trees']+=1;stats['nodes']+=len(nodes);stats['edges']+=len(edges)
out={'method':'Map headers confirm ByteProperty->IntProperty; matched PDB confirms TMap<unsigned char,int>. Every map consumed exactly and every nonnegative target is in bounds. Edges are authored config, not proof of runtime availability.','statistics':dict(stats),'trees':trees,'target_map_proofs':proofs,'type_evidence':'inventory/player-combo-type-layouts.json','runtime_verified':False}
(R/'inventory/player-combo-graphs.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8',newline=chr(10))
print(json.dumps({'statistics':dict(stats),'trees':[{'asset':x['asset'],'nodes':len(x['nodes']),'edges':len(x['edges'])} for x in trees]},ensure_ascii=True))
