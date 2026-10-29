"""Read-only PE/PDB indexer. MSF 7 / CodeView format; outputs research metadata only.
References: https://llvm.org/docs/PDB/MsfFile.html ; https://llvm.org/docs/PDB/CodeViewSymbols.html
"""
import argparse,collections,csv,hashlib,json,re,struct,uuid
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
GAME=Path(r'E:\Games_Little\Epic\Sifu')
EXE=GAME/'Sifu/Binaries/Win64/Sifu-Win64-Shipping.exe'
PDB=EXE.with_suffix('.pdb')
PAT=re.compile(r'AIController|AIComponent|AISystem|AIDirector|AIAttack|AICombat|AISlot|AIGroup|Combat|Stun|Stagger|Impact|Poise|Resilien|StructureDamage|HitReact|HitResponse|SuperArmor|HyperArmor|AttackToken|AttackSlot|Crowd|Squad|Threat|TargetSelection|Aggress|Tension',re.I)
class Msf:
 def __init__(self,path):
  self.f=path.open('rb');h=self.f.read(56)
  if not h.startswith(b'Microsoft C/C++ MSF 7.00'):raise ValueError('Unsupported PDB')
  self.bs,_,_,dsz,_,bm=struct.unpack_from('<6I',h,32)
  n=(dsz+self.bs-1)//self.bs
  bmap=self.at(bm*self.bs,n*4)
  ids=struct.unpack('<'+'I'*n,bmap)
  d=b''.join(self.at(i*self.bs,self.bs) for i in ids)[:dsz]
  ns=struct.unpack_from('<I',d)[0];self.sizes=struct.unpack_from('<'+'I'*ns,d,4)
  pos=4+4*ns;self.blocks=[]
  for size in self.sizes:
   nb=0 if size==0xffffffff else (size+self.bs-1)//self.bs
   self.blocks.append(struct.unpack_from('<'+'I'*nb,d,pos));pos+=nb*4
 def at(self,off,n):self.f.seek(off);return self.f.read(n)
 def stream(self,i):return b''.join(self.at(b*self.bs,self.bs) for b in self.blocks[i])[:self.sizes[i]]
 def close(self):self.f.close()
def zstr(b,pos):
 end=b.find(b'\0',pos)
 if end<0:return ''
 return b[pos:end].decode('utf-8','replace')
def numeric_skip(b,pos):
 n=struct.unpack_from('<H',b,pos)[0]
 if n<0x8000:return pos+2,n
 lens={0x8000:1,0x8001:2,0x8002:2,0x8003:4,0x8004:4,0x8009:8,0x800a:8}
 sz=lens.get(n)
 return (pos+2+sz,None) if sz else (None,None)
def csvout(name,fields,rows):
 with (ROOT/'inventory'/name).open('w',encoding='utf-8-sig',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(rows)
def main():
 out=ROOT/'inventory';out.mkdir(exist_ok=True)
 exe=EXE.read_bytes();pe=struct.unpack_from('<I',exe,0x3c)[0];nsec=struct.unpack_from('<H',exe,pe+6)[0];optsize=struct.unpack_from('<H',exe,pe+20)[0]
 op=pe+24;dd=op+(112 if struct.unpack_from('<H',exe,op)[0]==0x20b else 96)
 sections=[]
 for i in range(nsec):
  p=pe+24+optsize+40*i;vs,va,rs,rp=struct.unpack_from('<4I',exe,p+8);sections.append((va,max(vs,rs),rp))
 def rvaoff(rva):
  for va,sz,rp in sections:
   if va<=rva<va+sz:return rp+rva-va
  raise ValueError('RVA not found')
 dr,ds=struct.unpack_from('<II',exe,dd+6*8);debug=[]
 for i in range(ds//28):
  p=rvaoff(dr)+i*28;typ,size,addr,ptr=struct.unpack_from('<4I',exe,p+12)
  if typ==2 and exe[ptr:ptr+4]==b'RSDS':debug.append({'guid':str(uuid.UUID(bytes_le=exe[ptr+4:ptr+20])),'age':struct.unpack_from('<I',exe,ptr+20)[0],'pdb':zstr(exe,ptr+24)})
 m=Msf(PDB);pi=m.stream(1);pdbinfo={'guid':str(uuid.UUID(bytes_le=pi[12:28])),'age':struct.unpack_from('<I',pi,8)[0]}
 dbi=m.stream(3);symstream=struct.unpack_from('<H',dbi,20)[0];modsz=struct.unpack_from('<i',dbi,24)[0]
 pos=64;mods=[]
 while pos+64<=64+modsz:
  s,syms,c11,c13=struct.unpack_from('<HIII',dbi,pos+34)
  a=dbi.index(b'\0',pos+64);b=dbi.index(b'\0',a+1)
  mods.append({'module':dbi[pos+64:a].decode('utf-8','replace'),'object':dbi[a+1:b].decode('utf-8','replace'),'stream':s,'symbol_bytes':syms,'c13_line_bytes':c13});pos=(b+4)&~3
 csvout('pdb_modules.csv',['module','object','stream','symbol_bytes','c13_line_bytes'],mods)
 sy=m.stream(symstream);pos=0;counts=collections.Counter();hits=[];public=0
 while pos+4<=len(sy):
  ln,kind=struct.unpack_from('<HH',sy,pos)
  if ln<2 or pos+ln+2>len(sy):raise ValueError(f'Bad symbol record at {pos}')
  counts[f'0x{kind:04x}']+=1
  if kind==0x110e and ln>=12:
   public+=1;name=zstr(sy,pos+14)
   if PAT.search(name):
    flags,off,seg=struct.unpack_from('<IIH',sy,pos+4);rva=sections[seg-1][0]+off if 1<=seg<=len(sections) else None
    hits.append({'mangled_name':name,'rva':hex(rva) if rva is not None else '', 'section':seg,'offset':hex(off),'flags':flags})
  pos+=ln+2
 csvout('pdb_candidate_symbols.csv',['mangled_name','rva','section','offset','flags'],hits)
 del sy
 ti=m.stream(2);hdrsz,start,end,recsz=struct.unpack_from('<4I',ti,4);pos=hdrsz;idx=start;types=[]
 while pos+4<=len(ti) and idx<end:
  ln,kind=struct.unpack_from('<HH',ti,pos);rec=ti[pos+4:pos+ln+2];name='';size=None
  if kind in (0x1504,0x1505) and len(rec)>=18:
   np,size=numeric_skip(rec,16)
   if np is not None:name=zstr(rec,np)
  elif kind==0x1506 and len(rec)>=10:
   np,size=numeric_skip(rec,8)
   if np is not None:name=zstr(rec,np)
  elif kind==0x1507 and len(rec)>=12:name=zstr(rec,12)
  if name and PAT.search(name):types.append({'type_index':hex(idx),'kind':hex(kind),'name':name,'size':size})
  pos+=ln+2;idx+=1
 csvout('pdb_candidate_types.csv',['type_index','kind','name','size'],types)
 report={'game_root':str(GAME),'exe':str(EXE),'pdb':str(PDB),'exe_sha256':hashlib.sha256(exe).hexdigest(),'exe_debug':debug,'pdb_info':pdbinfo,'pdb_matches_exe':any(d['guid']==pdbinfo['guid'] and d['age']==pdbinfo['age'] for d in debug),'pdb_size':PDB.stat().st_size,'pdb_stream_count':len(m.sizes),'module_count':len(mods),'public_symbol_count':public,'candidate_symbol_count':len(hits),'candidate_type_count':len(types),'symbol_record_counts':dict(counts),'note':'Symbol/type names establish presence only; behavior, parameter meaning and runtime values require further evidence.'}
 (out/'pdb_overview.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
 m.close();print(json.dumps(report,ensure_ascii=False,indent=2))
 print('TYPE_EXAMPLES',json.dumps([t for t in types if not t['name'].startswith(('TArray','TSet','TMap','TBase','TWeak','TShared','TUnique','TSubclass'))][:45],ensure_ascii=False))
if __name__=='__main__':main()
