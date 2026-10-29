"""Apply inspected bounded UE4 package reader; preserve opaque data and failures.
Parser provenance: oiiiwjh/rea-exploration-notes sifu_ana/structure/read_packages.py.
"""
import collections,csv,gzip,importlib.util,json,re,struct
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch');EXTRACTED=ROOT/'extracted'
spec=importlib.util.spec_from_file_location('bounded_external',ROOT/'tools/external_read_packages.py');parser=importlib.util.module_from_spec(spec);spec.loader.exec_module(parser)
packages=[];fail=[];flat=[]
def flatten(props,path,prefix=''):
 for prop in props:
  name=prefix+prop['name']+'['+str(prop['arrayIndex'])+']';v=prop['value']
  if isinstance(v,list):flatten(v,path,name+'.')
  else:flat.append({'asset':path,'property':name,'type':prop['type'],'value':v if not isinstance(v,dict) else json.dumps(v,separators=(',',':'))})
for path in sorted(EXTRACTED.rglob('*.uasset')):
 try:
  pkg=parser.read_package(path,EXTRACTED);packages.append(pkg);flatten(pkg.get('properties',[]),pkg['path'])
 except (ValueError,struct.error,UnicodeError) as e:fail.append({'path':path.relative_to(EXTRACTED).as_posix(),'error':str(e)})
with gzip.open(ROOT/'inventory/package-metadata.json.gz','wt',encoding='utf-8') as f:json.dump(packages,f,ensure_ascii=False,separators=(',',':'))
with (ROOT/'inventory/serialized-properties.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['asset','property','type','value']);w.writeheader();w.writerows(flat)
interesting=[p for p in packages if re.search(r'/Tickets/|ContextualDefense|Grunt.*ArchetypeDB|Grunt_GuardDB|MC_GuardDB|Impact|StunDB|DizzyDB|AttackData',p['path'],re.I)]
(ROOT/'inventory/focused-asset-metadata.json').write_text(json.dumps(interesting,ensure_ascii=False,indent=2),encoding='utf-8')
summary={'packages_read':len(packages),'summary_failures':fail,'property_parse_counts':dict(collections.Counter(p['propertyDecoding'].split(':')[0] for p in packages)),'serialized_leaf_property_count':len(flat),'limitations':['Metadata parser supports only the observed UE4 -7/zero custom-version cooked layout.','Single-export tagged assets are decoded only when all properties and terminator agree.','Multi-export blueprints, native DataTables and unknown arrays/structs are not interpreted.','Absent property is not zero: defaults may live in native class or parent asset.','A stored value is not proof of its runtime formula, units, active difficulty or references.']}
(ROOT/'inventory/package-parse-overview.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='summary_failures'},ensure_ascii=False,indent=2));print('failure_count',len(fail));print('failure_examples',json.dumps(fail[:5],ensure_ascii=False))
for pkg in interesting:
 if '/Tickets/' in pkg['path'] and pkg.get('properties'):
  print('TICKET',pkg['path'],json.dumps(pkg['properties'],ensure_ascii=False)[:2200])
  break

