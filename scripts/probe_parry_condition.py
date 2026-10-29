"""Decode only the observed BP_TargetIsParryVictim function opcodes; fail closed on unknown tokens."""
import sys,struct,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'tools'));import local_bounded_packages as q
base=R/'extracted';p=base/'Sifu/Content/DB/AI/_Shared/ComboConditions/BP_TargetIsParryVictim.uasset';m=q.read_package(p,base);payload=p.with_suffix('.uexp').read_bytes();e=m['exports'][0];raw=payload[e['serialOffset']-p.stat().st_size:e['serialOffset']-p.stat().st_size+e['serialSize']]
# Exact observed UStruct script header: logical bytes=985, serialized bytes=1517; bounds checked.
assert struct.unpack_from('<ii',raw,1213)==(985,1517)
code=raw[1221:2738];assert code[-1]==0x53
pos=0;delta=0

def num(fmt):
 global pos
 v=struct.unpack_from('<'+fmt,code,pos)[0];pos+=struct.calcsize('<'+fmt);return v

def name():
 i=num('i');n=num('i');return m['names'][i]+(':'+str(n) if n else '')
def obj():
 global delta
 i=num('i');delta+=4
 return m['imports'][-i-1]['name'] if i<0 else ('self:'+m['exports'][i-1]['name'] if i else 'None')
def field():
 global delta
 start=pos;n=num('i')
 if not 0<=n<=8:raise ValueError('field count '+str(n))
 ns=[name() for _ in range(n)];i=num('i');owner=m['imports'][-i-1]['name'] if i<0 else ('self:'+m['exports'][i-1]['name'] if i else 'None');delta+=8-(pos-start)
 return '.'.join(ns)+'@'+owner

def ex(depth=0):
 global pos,delta
 start=pos;o=num('B')
 if depth>40:raise ValueError('depth')
 if o in [0,1,0x48]:v=['var',field()]
 elif o==0xf:v=['let',field(),ex(depth+1),ex(depth+1)]
 elif o in [0x5f,0x14]:v=['assign',ex(depth+1),ex(depth+1)]
 elif o==0x2f:
  ty=obj();sz=num('i');xs=[]
  while code[pos]!=0x30:xs.append(ex(depth+1))
  num('B');v=['struct',ty,sz,xs]
 elif o==0x2e:v=['cast',obj(),ex(depth+1)]
 elif o==0x38:v=['primitivecast',num('B'),ex(depth+1)]
 elif o in [0x19,0x1a]:
  who=ex(depth+1);skip=num('I');f=field();v=['context',who,skip,f,ex(depth+1)]
 elif o in [0x1c,0x68,0x1b]:
  fn=name() if o==0x1b else obj();xs=[]
  while code[pos]!=0x16:xs.append(ex(depth+1))
  num('B');v=['call',fn,xs]
 elif o in [0x42,0x4c]:v=['member',field(),ex(depth+1)]
 elif o==7:v=['jumpifnot',num('I'),ex(depth+1)]
 elif o==6:v=['jump',num('I')]
 elif o==4:v=['return',ex(depth+1)]
 elif o==0x20:v=['object',obj()]
 elif o==0x21:
  v=['name',name()];delta+=4  # FScriptName in VM occupies 12 bytes versus serialized 8.
 elif o==0x24:v=['byte',num('B')]
 elif o==0x1d:v=['int',num('i')]
 elif o in [0xb,0x17,0x25,0x26,0x27,0x28,0x2a,0x53]:v={0xb:'nothing',0x17:'self',0x25:0,0x26:1,0x27:True,0x28:False,0x2a:'NoObject',0x53:'EndScript'}[o]
 else:raise ValueError('unknown '+hex(o)+' at '+str(start)+' '+code[start:start+22].hex())
 return v
statements=[]
try:
 while pos<len(code):
  st=pos;vm=pos+delta;v=ex();statements.append({'serialized':st,'vm':vm,'ast':v})
 print('boundary',pos,pos+delta)
 for x in statements:print(x['vm'],json.dumps(x['ast'],ensure_ascii=False))
 assert pos==1517 and pos+delta==985
 valid={x['vm'] for x in statements}
 for x in statements:
  if isinstance(x['ast'],list) and x['ast'][0] in ['jumpifnot','jump']:assert x['ast'][1] in valid,(x['ast'][1],valid)
 report={'asset':m['path'],'uasset_sha256':m['uassetSha256'],'uexp_sha256':hashlib.sha256(payload).hexdigest(),'function':'BPE_GetTargetNode','script_header_offset':1213,'serialized_bytes':pos,'vm_bytes':pos+delta,'statements':statements,'validation':'all serialized bytes and logical VM length consumed; all branch destinations are statement boundaries','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'limits':['Only this observed function/opcode subset; no generic blueprint decoder claim','Static expression/control-flow reconstruction, no runtime execution']}
 (R/'inventory/20261029-parry-condition.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
except Exception as err:print('FAILED',pos,str(err));raise
