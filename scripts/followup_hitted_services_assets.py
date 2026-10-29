"""Target and parse only Hitted availability, recovery and impact-service packages."""
import sys,re,json,hashlib,subprocess,ast,struct
from pathlib import Path
sys.dont_write_bytecode=True
R=Path(r'E:\ProgrameFiles\SifuResearch');sys.path.insert(0,str(R/'tools'))
import local_bounded_packages as q
module=ast.parse((R/'scripts/parse_tagged_exports.py').read_text(encoding='utf-8'))
funcs=ast.Module(body=[x for x in module.body if isinstance(x,ast.FunctionDef) and x.name in ('refname','enrich')],type_ignores=[])
exec(compile(funcs,'bounded-array-helper','exec'),globals())
PAK=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak')
D=R/'logs/followup-hitted-services';X=D/'extracted';X.mkdir(parents=True,exist_ok=True)
paths=[
'Sifu/Content/Animations/System/Orders/Services/Hitted/HittedAvailabilityOrderService',
'Sifu/Content/Animations/System/Orders/Services/Hitted/HittedCancelAvailabilityOrderService',
'Sifu/Content/Animations/System/Orders/Services/Hitted/HittedGetUpNoAttackAvailabilityOrderService',
'Sifu/Content/Animations/System/Orders/Services/Hitted/HittedLDCollisionOrderService',
'Sifu/Content/Animations/System/Orders/Services/Hitted/HittedPushUntargettableOrderService',
'Sifu/Content/Animations/System/Orders/Attacks/Hit/OrderHittedGeneric_HittedOrderService',
'Sifu/Content/Animations/System/Orders/Attacks/Hit/OrderHittedGeneric_HittedOrderService_SettableHitbox',
'Sifu/Content/Animations/System/Orders/Attacks/Hit/BP_OrderHittedFallCondition',
'Sifu/Content/Animations/System/Orders/Services/Hitted/OrderServiceStateCheckForDropWeapon',
'Sifu/Content/Animations/System/Orders/Services/OrderServiceIsPlayerCondition',
'Sifu/Content/Animations/System/Orders/Attacks/Hit/BP_OrderServiceIsPlayerKnockdown',
'Sifu/Content/Animations/System/Orders/Services/Weapons/BP_VariableWeightWeaponIdleCondition',
'Sifu/Content/DB/Inputs/Availability/LayerData/GenericAll',
'Sifu/Content/DB/Inputs/Availability/LayerData/Hitted/Cancel/HittedCancel',
'Sifu/Content/DB/Inputs/Availability/LayerData/NoAttack',
'Sifu/Content/DB/Inputs/Availability/LayerData/Pushed',
]
selected=[p+e for p in paths for e in ('.uasset','.uexp')]
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(R/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
cmd=[str(R/'tools/repak-v0.2.3/repak.exe'),'--aes-key',key,'unpack',str(PAK),'--output',str(X),'--quiet']
for p in selected:cmd+=['--include',p]
res=subprocess.run(cmd,capture_output=True,text=True)
(D/'repak.stdout.txt').write_text(res.stdout,encoding='utf-8');(D/'repak.stderr.txt').write_text(res.stderr,encoding='utf-8')
if res.returncode:raise RuntimeError('Target extraction failed: '+str(res.returncode))
def ref(p,i):
 if not i:return None
 seen=set()
 def go(i):
  if not i:return None
  if i in seen:return '<cycle>'
  seen.add(i)
  o=p['imports'][-i-1] if i<0 else p['exports'][i-1]
  parent=go(o['outer'] if i<0 else o['outerIndex'])
  return (parent+'.' if parent else '')+o['name']
 return go(i)
files=[];objects=[];packages=[];fail=[]
for name in selected:
 f=X/name
 if not f.exists():fail.append({'asset':name,'reason':'missing from targeted extraction'});continue
 files.append({'path':str(f),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
 if not name.endswith('.uasset'):continue
 p=q.read_package(f,X);packages.append(p);body=f.with_suffix('.uexp').read_bytes()
 for idx,e in enumerate(p['exports']):
  begin=e['serialOffset']-f.stat().st_size;end=begin+e['serialSize']
  if not 0<=begin<=end<=len(body):fail.append({'asset':name,'export':e['name'],'reason':'export bounds'});continue
  raw=body[begin:end]
  try:
   props,n=q.tags(raw,p['names']);enrich(props,raw,p)
   if n!=len(raw) and not(n+4==len(raw) and raw[n:]==bytes(4)):raise ValueError(f'tag end {n}/{len(raw)}')
   objects.append({'asset':name,'export':e['name'],'class':ref(p,e['classIndex']),'export_index':idx+1,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'properties':props})
  except Exception as ex:fail.append({'asset':name,'export':e['name'],'class':ref(p,e['classIndex']),'reason':str(ex)})
out={'source_pak':str(PAK),'files':files,'packages':packages,'objects':objects,'failures':fail}
(R/'inventory/followup-hitted-services-assets.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(files),'objects':len(objects),'failures':len(fail),'out':str(R/'inventory/followup-hitted-services-assets.json')},ensure_ascii=False))




