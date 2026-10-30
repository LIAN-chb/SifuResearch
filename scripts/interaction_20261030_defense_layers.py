"""Second bounded defense probe: cache ownership and layer update methods."""
from pathlib import Path
import sys,json,re,hashlib,struct
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'scripts'))
from disassemble_research import disassemble
from index_pdb import Msf,PDB,EXE
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
names=['AvailabilityLayerManager::Update','AvailabilityLayerManager::AvailabilityLayerStack::UpdateResultLayers','UFightingMovementComponent::IsAvailable','FAIDefenseHandler::ComputeDefenseRequest']
report=disassemble(names,'interaction-20261030-defense-layers')
s=(R/'scripts/inspect_types.py').read_text(encoding='utf-8')
targets={'AvailabilityLayerManager::AvailabilityLayerContextStack','AvailabilityLayerManager::AvailabilityLayerStack','AvailabilityLayerManager::AvailabilityLayerContext','AvailabilityLayerManager::AvailabilityLayer','UFightingMovementComponent','FInputLayer','FInputLayerStack'}
s=re.sub(r'TARGET_NAMES = \{.*?\n\}','TARGET_NAMES = '+repr(targets),s,count=1,flags=re.S)
s=re.sub(r'RELEVANT = re.compile\(.*?\n','RELEVANT = re.compile(r"(?!)")\n',s,count=1)
s=s.replace('if ((attrs >> 2) & 0x7) == 4: q,_=cvnum(data,q)','if ((attrs >> 2) & 0x7) in (4,6): q+=4')
s=s.replace("ROOT/'inventory'/'focused_type_layouts.json'","ROOT/'inventory'/'interaction-20261030-defense-layers-types.json'")
exec(compile(s,'adapted-layer-types','exec'),{'__name__':'__main__'})
# Primary-vptr symbols may explicitly name the ABaseCharacter subobject.
m=Msf(PDB);d=m.stream(3);sy=m.stream(struct.unpack_from('<H',d,20)[0]);m.close();hits=[];p=0
while p+4<=len(sy):
 n,k=struct.unpack_from('<HH',sy,p)
 if k==0x110e:
  end=sy.find(b'\0',p+14);name=sy[p+14:end].decode('utf-8','replace')
  if name.startswith('??_7AFightingCharacter@@6B'):
   flags,adr,seg=struct.unpack_from('<IIH',sy,p+4);hits.append(dict(name=name,section=seg,offset=adr))
 p+=n+2
batch=dict(command='D:/Programes/PY/python.exe scripts/interaction_20261030_defense_layers.py',cwd=str(Path.cwd()),python=sys.version,script_sha256=sha(__file__),type_reader_sha256=sha(R/'scripts/inspect_types.py'),source_build='inventory/interaction-20261030-defense-batch.json',character_vtable_symbols=hits,outputs=[dict(path=str(p.relative_to(R)),sha256=sha(p)) for p in [R/'inventory/interaction-20261030-defense-layers-disassembly.json',R/'inventory/interaction-20261030-defense-layers-types.json']])
(R/'inventory/interaction-20261030-defense-layers-batch.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf-8')
print('character vtables',hits)
