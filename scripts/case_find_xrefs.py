"""Bounded static RIP-relative references to the two case-study functions; candidates require instruction review."""
from pathlib import Path
import json,hashlib,struct,bisect,sys
R=Path(__file__).resolve().parents[1];overview=json.loads((R/'inventory/pdb_overview.json').read_text(encoding='utf-8'));exe=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Binaries\Win64\Sifu-Win64-Shipping.exe');b=exe.read_bytes();digest=hashlib.sha256(b).hexdigest();assert digest==overview['exe_sha256']
pe=struct.unpack_from('<I',b,0x3c)[0];n=struct.unpack_from('<H',b,pe+6)[0];op=struct.unpack_from('<H',b,pe+20)[0];base=struct.unpack_from('<Q',b,pe+48)[0];secs=[]
for i in range(n):
 o=pe+24+op+i*40;name=b[o:o+8].rstrip(b'\0').decode();vs,va,sz,raw=struct.unpack_from('<IIII',b,o+8)
 if name=='.text':secs.append((raw,sz,va))
procs=json.loads((R/'inventory/game-procedures.json').read_text(encoding='utf-8'));procs.sort(key=lambda x:int(x['rva'],16));starts=[int(x['rva'],16) for x in procs]
def owner(rva):
 k=bisect.bisect_right(starts,rva)-1
 return procs[k]['name'] if k>=0 and rva<starts[k]+procs[k]['length'] else None
out=[]
for raw,sz,va in secs:
 text=b[raw:raw+sz]
 for target,name in [(0x18bc520,'UAIFightingComponent::OnIsStunChanged'),(0x18c9e50,'FAIDefenseHandler::UpdateDefenseNeed')]:
  patterns=[bytes([x]) for x in [0xe8,0xe9]]+[bytes([0x48,0x8d,x]) for x in [5,13,21,29,37,45,53,61]]
  for pat in patterns:
   pos=0
   while True:
    p=text.find(pat,pos)
    if p<0:break
    pos=p+1;end=p+len(pat)+4
    if end>len(text):break
    disp=struct.unpack_from('<i',text,p+len(pat))[0]
    if va+end+disp==target:out.append({'target':name,'rva':hex(va+p),'pattern':pat.hex(),'owner':owner(va+p),'status':'candidate-needs-disassembly'})
report={'exe_sha256':digest,'python':sys.version,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'command':r'D:\Programes\PY\python.exe scripts/case_find_xrefs.py','candidates':out,'limits':['Pattern scan can include non-instruction bytes; confirm each match in PDB-bounded disassembly.','No indirect-call completeness claim.']}
(R/'inventory/case-xrefs.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print(json.dumps(out,ensure_ascii=False))
