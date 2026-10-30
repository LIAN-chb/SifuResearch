from pathlib import Path
import sys,struct,json,subprocess,hashlib
R=Path('E:/ProgrameFiles/SifuResearch');sys.path.insert(0,str(R/'scripts'));from index_pdb import Msf,PDB,EXE
m=Msf(PDB);db=m.stream(3);sy=m.stream(struct.unpack_from('<H',db,20)[0]);m.close();data=EXE.read_bytes();pe=struct.unpack_from('<I',data,0x3c)[0];o=struct.unpack_from('<H',data,pe+20)[0];ns=struct.unpack_from('<H',data,pe+6)[0];sects=[]
for i in range(ns):
 p=pe+24+o+40*i;vs,va,rs,rp=struct.unpack_from('<4I',data,p+8);sects.append((va,max(vs,rs),rp))
def off(r):
 for va,sz,rp in sects:
  if va<=r<va+sz:return rp+r-va
p=0;hits=[]
while p+4<=len(sy):
 n,k=struct.unpack_from('<HH',sy,p)
 if k==0x110e:
  end=sy.find(b'\0',p+14);name=sy[p+14:end].decode('utf-8','replace')
  if 'GetFinalPlayRate@FAnimContainer' in name or name=='??_7OrderAttack@@6BOrderAttackInterface@@@':
   flags,adr,seg=struct.unpack_from('<IIH',sy,p+4);r=sects[seg-1][0]+adr;hits.append(dict(name=name,rva=hex(r)))
   if name.startswith('??_7'):hits[-1]['vtable']=[hex(struct.unpack_from('<Q',data,off(r)+i*8)[0]-0x140000000) for i in range(16)]
   else:
    dest=R/'logs/20261030-前摇语义-16/buildup-clock/buildup-GetFinalPlayRate.asm.txt';subprocess.run([r'C:/new_software/Microsoft Visual Studio/18/Community/VC/Tools/MSVC/14.51.36231/bin/Hostx64/x64/dumpbin.exe','/nologo','/disasm:nobytes',f'/range:0x{0x140000000+r:x},0x{0x140000000+r+100:x}',f'/out:{dest}',str(EXE)],check=True,capture_output=True)
 p+=n+2
(R/'exports/20261030-前摇语义-16/buildup-publics.json').write_text(json.dumps(hits,indent=2));print(hits)
