"""Index local game procedure ranges from matched PDB and disassemble selected callbacks."""
import csv,json,re,struct,subprocess
from pathlib import Path
from index_pdb import Msf,EXE,PDB,ROOT,zstr
mods=list(csv.DictReader((ROOT/'inventory/pdb_modules.csv').open(encoding='utf-8-sig')))
exe=EXE.read_bytes();pe=struct.unpack_from('<I',exe,0x3c)[0];ns=struct.unpack_from('<H',exe,pe+6)[0];opsize=struct.unpack_from('<H',exe,pe+20)[0];base=struct.unpack_from('<Q',exe,pe+24+24)[0]
secs=[]
for i in range(ns):secs.append(struct.unpack_from('<I',exe,pe+24+opsize+i*40+12)[0])
m=Msf(PDB);rows=[]
for mod in mods:
 if not re.search(r'\\Sifu\\Module\.Sifu\.',mod['module']):continue
 sid=int(mod['stream']);limit=int(mod['symbol_bytes'])
 if sid==65535 or limit<4:continue
 data=m.stream(sid);pos=4
 while pos+4<=min(limit,len(data)):
  ln,kind=struct.unpack_from('<HH',data,pos)
  if ln<2 or pos+ln+2>len(data):raise ValueError('Bad procedure record bounds')
  if kind in (0x110f,0x1110,0x1146,0x1147):
   d=data[pos+4:pos+ln+2]
   if len(d)>=36:
    length=struct.unpack_from('<I',d,12)[0];off=struct.unpack_from('<I',d,28)[0];seg=struct.unpack_from('<H',d,32)[0];name=zstr(d,35)
    if 1<=seg<=len(secs):rows.append({'name':name,'rva':hex(secs[seg-1]+off),'length':length,'module':mod['module'],'stream':sid,'record_offset':pos})
  pos+=ln+2
m.close()
(ROOT/'inventory/game-procedures.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf-8')
wanted=['FAIAttackTicketManager::OnDefenderFightingStateChanged','FAIAttackTicketManager::OnDefenderOrderStateChanged','FAIAttackTicketManager::IsJokerSituationActive','UAIFightingComponent::OnIsStunChanged','FAIAttackHandler::OnIsStunChanged','UHitComponent::IsStun']
tool=Path(r'C:\new_software\Microsoft Visual Studio\18\Community\VC\Tools\MSVC\14.51.36231\bin\Hostx64\x64\dumpbin.exe')
outputs=[]
for name in wanted:
 hits=[x for x in rows if x['name']==name]
 if not hits:outputs.append({'name':name,'status':'procedure not found'});continue
 p=hits[0];rva=int(p['rva'],16);length=p['length'];dest=ROOT/'logs'/('callback-'+name.replace('::','-')+'.asm.txt')
 result=subprocess.run([str(tool),'/nologo','/disasm:nobytes',f'/range:0x{base+rva:x},0x{base+rva+length-1:x}',f'/out:{dest}',str(EXE)],capture_output=True,text=True)
 if result.returncode:raise RuntimeError('dumpbin failed: '+result.stdout+result.stderr)
 outputs.append({**p,'status':'disassembled','output':str(dest)})
(ROOT/'inventory/callback-disassembly.json').write_text(json.dumps({'tool':str(tool),'image_base':hex(base),'procedures':outputs},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'game_procedures':len(rows),'callbacks':outputs},ensure_ascii=False,indent=2))
