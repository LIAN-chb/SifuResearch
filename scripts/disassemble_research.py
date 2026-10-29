"""Read-only bounded disassembly of named, PDB-indexed local Sifu procedures."""
import argparse,hashlib,json,re,struct,subprocess
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
EXE=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Binaries\Win64\Sifu-Win64-Shipping.exe')
TOOL=Path(r'C:\new_software\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\dumpbin.exe')
def disassemble(names,group):
 if not re.fullmatch('[a-z0-9_-]+',group):raise ValueError('Invalid output group')
 original=json.loads((ROOT/'inventory/pdb_overview.json').read_text(encoding='utf-8'))
 data=EXE.read_bytes();digest=hashlib.sha256(data).hexdigest()
 if digest!=original['exe_sha256']:raise ValueError('EXE changed; re-index the matching PDB before analysis')
 pe=struct.unpack_from('<I',data,0x3c)[0];imagebase=struct.unpack_from('<Q',data,pe+48)[0]
 procs=json.loads((ROOT/'inventory/game-procedures.json').read_text(encoding='utf-8'));directory=ROOT/'logs'/group;directory.mkdir(exist_ok=True)
 output=[]
 for name in names:
  matches=[p for p in procs if p['name']==name]
  if not matches:output.append({'name':name,'status':'not-in-index'});continue
  seen=set()
  for p in matches:
   if (p['rva'],p['length']) in seen:continue
   seen.add((p['rva'],p['length']));rv=int(p['rva'],16);length=p['length']
   if not 0<length<=1000000:raise ValueError('Procedure length limit')
   label=re.sub('[^a-zA-Z0-9_-]','_',name)[:150]+'-'+p['rva']+'.asm.txt';dest=directory/label
   result=subprocess.run([str(TOOL),'/nologo','/disasm:nobytes',f'/range:0x{imagebase+rv:x},0x{imagebase+rv+length-1:x}',f'/out:{dest}',str(EXE)],capture_output=True,text=True)
   if result.returncode:raise RuntimeError(result.stdout+result.stderr)
   output.append({**p,'status':'disassembled','file':str(dest),'assembly_sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
 report={'exe_sha256':digest,'image_base':hex(imagebase),'tool':str(TOOL),'procedures':output,'limitations':['PDB exact ranges can include embedded tables/padding; those are not automatically executable instructions.','Disassembly is not runtime validation.']}
 (ROOT/'inventory'/(group+'-disassembly.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'group':group,'disassembled':sum(x['status']=='disassembled' for x in output),'missing':[x['name'] for x in output if x['status']!='disassembled']},ensure_ascii=False))
 return report
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--group',required=True);p.add_argument('--name',action='append',required=True);a=p.parse_args();disassemble(a.name,a.group)
