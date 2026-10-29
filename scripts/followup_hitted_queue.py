"""Targeted Hitted order assets and matched-code evidence; game files are read only."""
import sys,re,json,hashlib,subprocess,ast,struct
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(r'E:\ProgrameFiles\SifuResearch');sys.path.insert(0,str(R/'tools'));sys.path.insert(0,str(R/'scripts'))
import local_bounded_packages as q
from disassemble_research import disassemble
module=ast.parse((R/'scripts/parse_tagged_exports.py').read_text(encoding='utf-8'))
functions=ast.Module(body=[x for x in module.body if isinstance(x,ast.FunctionDef) and x.name in ('refname','enrich')],type_ignores=[])
exec(compile(functions,'bounded-array-helper','exec'),globals())
D=R/'logs/followup-hitted';D.mkdir(exist_ok=True);X=D/'extracted';X.mkdir(exist_ok=True)
PAK=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak')
selected=[f'Sifu/Content/Animations/System/Orders/Attacks/{stem}{ext}' for stem in ['OrderHitted','OrderHittedGeneric'] for ext in ['.uasset','.uexp']]
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(R/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
cmd=[str(R/'tools/repak-v0.2.3/repak.exe'),'--aes-key',key,'unpack',str(PAK),'--output',str(X),'--quiet']
for p in selected:cmd+=['--include',p]
res=subprocess.run(cmd,capture_output=True,text=True)
if res.returncode:raise ValueError('Targeted extraction failed, return '+str(res.returncode))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p,i):
 if not i:return None
 o=p['imports'][-i-1] if i<0 else p['exports'][i-1]
 parent=ref(p,o['outer'] if i<0 else o['outerIndex'])
 return (parent+'.' if parent else '')+o['name']
objects=[];packages=[];fail=[];files=[]
for name in selected:
 p=X/name
 if not p.is_file():raise ValueError('Missing '+name)
 files.append({'path':str(p),'sha256':sha(p),'bytes':p.stat().st_size})
 if not name.endswith('.uasset'):continue
 meta=q.read_package(p,X);packages.append(meta);body=p.with_suffix('.uexp').read_bytes()
 for e in meta['exports']:
  begin=e['serialOffset']-p.stat().st_size;end=begin+e['serialSize']
  if not 0<=begin<=end<=len(body):fail.append({'asset':name,'export':e['name'],'reason':'outside export bounds'});continue
  try:
   props,n=q.tags(body[begin:end],meta['names'])
   if n!=end-begin and not (n+4==end-begin and body[begin+n:end]==bytes(4)):raise ValueError('Partial tagged export '+str(n)+'/'+str(end-begin))
   enrich(props,body[begin:end],meta)
   objects.append({'asset':name,'export':e['name'],'class':ref(meta,e['classIndex']),'flags':e['flags'],'properties':props,'consumed':n,'bytes':end-begin,'references':{str(i):ref(meta,i) for i in range(-len(meta['imports']),len(meta['exports'])+1) if i}})
  except (ValueError,IndexError) as ex:fail.append({'asset':name,'export':e['name'],'class':ref(meta,e['classIndex']),'reason':str(ex),'bytes':end-begin})
(R/'inventory/followup-hitted-assets.json').write_text(json.dumps({'source_pak':str(PAK),'files':files,'packages':packages,'objects':objects,'unparsed_exports':fail},ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'extracted':len(files),'parsed_exports':len(objects),'unparsed_exports':len(fail)},ensure_ascii=True))
disassemble(['OrderManager::PlayOrder','OrderManager::ReplaceOrderInQueue','OrderManager::CancelOrder','UOrderComponent::BPF_GetOrderDB','UOrderComponent::PlayOrder'], 'followup-hitted')