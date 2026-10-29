"""Read tagged exports and DataTable rows without instantiating game objects.
Extends inspected parser with bounded primitive arrays; unknown data stays opaque.
"""
import collections,csv,gzip,importlib.util,json,re,struct
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch');BASE=ROOT/'extracted'
spec=importlib.util.spec_from_file_location('bounded',ROOT/'tools/external_read_packages.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
packages=json.load(gzip.open(ROOT/'inventory/package-metadata.json.gz','rt',encoding='utf-8'))
objects=[];tables=[];failures=[];flat=[]
def refname(p,i,seen=None):
 if i==0:return None
 seen=set() if seen is None else set(seen)
 if i in seen:return '<cycle>'
 seen.add(i)
 if i<0:
  if -i>len(p['imports']):return '<invalid-import>'
  x=p['imports'][-i-1];outer=refname(p,x['outer'],seen)
  return (outer+'.' if outer else '')+x['name']
 if i>len(p['exports']):return '<invalid-export>'
 x=p['exports'][i-1];outer=refname(p,x['outerIndex'],seen)
 return (outer+'.' if outer else '')+x['name']
def enrich(props,raw,p):
 for x in props:
  v=x['value'];chunk=raw[x['valueOffset']:x['valueOffset']+x['size']]
  if isinstance(v,list):enrich(v,chunk,p)
  elif x['type']=='ObjectProperty' and isinstance(v,int):x['reference']=refname(p,v)
  elif x['type']=='StructProperty' and x.get('struct') in ('GameplayTag','GameplayTagContainer'):
   try:
    rr=q.Reader(chunk,p['names'])
    n=1 if x['struct']=='GameplayTag' else rr.number('i')
    if 0<=n<=10000 and len(chunk)-rr.position==n*8:x['tagNames']=[rr.name() for _ in range(n)]
   except (ValueError,struct.error,UnicodeError):pass
  elif x['type']=='ArrayProperty' and len(chunk)>=4:
   n=struct.unpack_from('<i',chunk)[0]
   if not 0<=n<=100000:continue
   inner=x.get('inner')
   fmts={'IntProperty':('i',4),'UInt32Property':('I',4),'FloatProperty':('f',4),'ObjectProperty':('i',4),'ByteProperty':('B',1)}
   if inner in fmts and len(chunk)==4+n*fmts[inner][1]:
    vals=list(struct.unpack_from('<'+fmts[inner][0]*n,chunk,4));x['arrayValues']=vals
    if inner=='ObjectProperty':x['arrayReferences']=[refname(p,i) for i in vals]
   elif inner=='NameProperty' and len(chunk)==4+n*8:
    rr=q.Reader(chunk,p['names'],4);x['arrayValues']=[rr.name() for _ in range(n)]
   elif inner=='StructProperty':
    try:
     rr=q.Reader(chunk,p['names'],4)
     an=rr.name();at=rr.name();sz=rr.number('i');ai=rr.number('i');st=rr.name();rr.take(16);hg=rr.number('B')
     if hg==1:rr.take(16)
     elif hg!=0:raise ValueError('GUID flag')
     if an!=x['name'] or at!='StructProperty' or ai!=0 or sz!=len(chunk)-rr.position:raise ValueError('Array inner-tag bounds')
     elements=[]
     for _ in range(n):
      eraw=chunk[rr.position:];ep,en=q.tags(eraw,p['names']);enrich(ep,eraw,p);elements.append(ep);rr.position+=en
     if rr.position!=len(chunk):raise ValueError('Array trailing bytes')
     x['arrayStruct']=st;x['arrayElements']=elements
    except (ValueError,struct.error,UnicodeError):pass
def flatten(props,asset,obj,prefix=''):
 for x in props:
  path=prefix+x['name']+'['+str(x['arrayIndex'])+']';v=x['value']
  if isinstance(v,list):flatten(v,asset,obj,path+'.')
  elif 'arrayElements' in x:
   for i,element in enumerate(x['arrayElements']):flatten(element,asset,obj,path+f'.element[{i}].')
  else:
   if isinstance(v,dict):v=json.dumps(x.get('arrayValues',x.get('tagNames',v)),ensure_ascii=False,separators=(',',':'))
   flat.append({'asset':asset,'export_or_row':obj,'property':path,'type':x['type'],'value':v,'reference':x.get('reference','')})
for p in packages:
 f=BASE/p['path'];ef=f.with_suffix('.uexp')
 if not ef.exists():continue
 b=ef.read_bytes();hs=f.stat().st_size
 for idx,e in enumerate(p['exports']):
  cls=refname(p,e['classIndex']) or ''
  if e['classIndex']>=0 or any(s in cls for s in ('BlueprintGeneratedClass','BlueprintGeneratedStruct','BlueprintGeneratedEnum','Function','AnimBlueprintGeneratedClass')):continue
  st=e['serialOffset']-hs;end=st+e['serialSize']
  if not 0<=st<=end<=len(b):failures.append({'asset':p['path'],'export':e['name'],'error':'bounds'});continue
  raw=b[st:end]
  try:
   props,n=q.tags(raw,p['names']);enrich(props,raw,p)
   if raw[n:n+4]!=b'\0'*4:raise ValueError('Missing zero UObject GUID')
   obj={'asset':p['path'],'export':e['name'],'class':cls,'export_index':idx+1,'sha256':p['uassetSha256'],'properties':props}
   if n+4==len(raw):
    objects.append(obj);flatten(props,p['path'],e['name'])
   elif cls.endswith('.DataTable'):
    rr=q.Reader(raw,p['names'],n+4);count=rr.number('i')
    if not 0<=count<=100000:raise ValueError('Row count bounds')
    rows=[]
    for _ in range(count):
     rn=rr.name();rowraw=raw[rr.position:];rp,nr=q.tags(rowraw,p['names']);enrich(rp,rowraw,p);rr.position+=nr;rows.append({'row':rn,'properties':rp})
    if rr.position!=len(raw):raise ValueError('DataTable unconsumed bytes')
    obj['rows']=rows;obj['row_count']=count;tables.append(obj)
    for row in rows:flatten(row['properties'],p['path'],row['row'])
   else:raise ValueError('Native suffix left opaque')
  except (ValueError,struct.error,UnicodeError) as ex:failures.append({'asset':p['path'],'export':e['name'],'class':cls,'error':str(ex)})
for name,data in [('tagged-objects.json.gz',objects),('data-tables.json.gz',tables)]:
 with gzip.open(ROOT/'inventory'/name,'wt',encoding='utf-8') as f:json.dump(data,f,ensure_ascii=False,separators=(',',':'))
with (ROOT/'inventory/object-and-table-properties.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['asset','export_or_row','property','type','value','reference']);w.writeheader();w.writerows(flat)
focus=[o for o in objects if re.search(r'/Tickets/|Grunt_Base_ContextualDefense|Grunt_Adv_ContextualDefense|Hit/|Impact',o['asset'],re.I)]
(ROOT/'exports/ai-and-impact-objects.json').write_text(json.dumps(focus,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'tagged_objects':len(objects),'data_tables':len(tables),'data_table_rows':sum(t['row_count'] for t in tables),'leaf_properties':len(flat),'opaque_or_unsupported_export_count':len(failures),'limitations':['Only complete tagged object bodies with zero GUID and complete DataTable row bodies are admitted.','Object arrays/primitive arrays decoded only when declared count exactly matches byte size.','Tagged struct arrays admitted only when inner tag and all element boundaries agree. Native complex types, code and blueprint bytecode not decoded.','Values may be overrides; native and parent defaults must be resolved before computing behavior.']}
(ROOT/'inventory/deep-parse-overview.json').write_text(json.dumps({**summary,'failures':failures},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(summary,ensure_ascii=False,indent=2))
print('Context-defense object classes:',dict(collections.Counter(o['class'] for o in objects if o['asset'].endswith('Grunt_Base_ContextualDefense.uasset'))))
