"""Read-only exact-build defense gates and vtable/type probe; outputs independent evidence."""
from pathlib import Path
import sys, struct, json, hashlib, uuid, subprocess, platform, re
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R/'scripts'))
from index_pdb import Msf,PDB,EXE
from disassemble_research import disassemble,TOOL
GROUP='interaction-20261030-defense'
OUT=R/'inventory'
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
def main():
    old=json.loads((OUT/'pdb_overview.json').read_text(encoding='utf-8'))
    m=Msf(PDB); info=m.stream(1)
    build=dict(exe_sha256=sha(EXE),pdb_sha256=sha(PDB),guid=str(uuid.UUID(bytes_le=info[12:28])),age=struct.unpack_from('<I',info,8)[0])
    assert build['exe_sha256']==old['exe_sha256'] and build['guid']==old['pdb_info']['guid'] and build['age']==old['pdb_info']['age']
    db=m.stream(3); sy=m.stream(struct.unpack_from('<H',db,20)[0]);m.close()
    data=EXE.read_bytes();pe=struct.unpack_from('<I',data,0x3c)[0];o=struct.unpack_from('<H',data,pe+20)[0]
    sections=[]
    for i in range(struct.unpack_from('<H',data,pe+6)[0]):
        p=pe+24+o+40*i;vs,va,rs,rp=struct.unpack_from('<4I',data,p+8);sections.append((va,max(vs,rs),rp))
    def off(r):
        for va,sz,rp in sections:
            if va<=r<va+sz:return rp+r-va
        raise ValueError(hex(r))
    procs=json.loads((OUT/'game-procedures.json').read_text(encoding='utf-8'));byr={}
    for x in procs:byr.setdefault(int(x['rva'],16),[]).append(x['name'])
    wanted={'??_7UDefenseInfluenceNodeGuard@@6B@':[0x298,0x2a0], '??_7UDefenseInfluenceNodeParryDeflect@@6B@':[0x298,0x2a0], '??_7UDefenseInfluenceNodeAvoid@@6B@':[0x298,0x2a0], '??_7UDefenseInfluenceNodeDodge@@6B@':[0x298,0x2a0], '??_7AFightingCharacter@@6B@':[0x988]}
    hits=[];p=0
    while p+4<=len(sy):
        n,k=struct.unpack_from('<HH',sy,p)
        if k==0x110e:
            end=sy.find(b'\0',p+14);name=sy[p+14:end].decode('utf-8','replace')
            if name in wanted:
                flags,adr,seg=struct.unpack_from('<IIH',sy,p+4);r=sections[seg-1][0]+adr
                slots=[]
                for slot in wanted[name]:
                    target=struct.unpack_from('<Q',data,off(r)+slot)[0]-0x140000000
                    slots.append(dict(slot=hex(slot),target_rva=hex(target),indexed_names=byr.get(target,[])))
                hits.append(dict(symbol=name,rva=hex(r),slots=slots))
        p+=n+2
    (OUT/(GROUP+'-vtables.json')).write_text(json.dumps(hits,ensure_ascii=False,indent=2),encoding='utf-8')
    names=['UDefenseInfluenceNodeGuard::GetInputAction','UDefenseInfluenceNodeParryDeflect::GetInputAction','UDefenseInfluenceNodeAvoid::GetInputAction','UDefenseInfluenceNodeDodge::GetInputAction','AFightingCharacter::IsAvailable','AvailabilityLayerManager::IsAvailable','UContextualDefenseInfluenceNode::Apply','FAIDefenseHandler::CanApplyDefenseRequest','FAIDefenseHandler::ApplyDefenseRequest','UDefenseInfluenceNodeGuard::Apply','UDefenseInfluenceNodeParryDeflect::Apply']
    report=disassemble(names,GROUP)
    source=(R/'scripts/inspect_types.py').read_text(encoding='utf-8')
    targets={'InputAction','InputContext','EOrderType','FAIDefenseRequest','UContextualDefenseInfluenceNode','UDefenseInfluenceNodeGuard','UDefenseInfluenceNodeParryDeflect','ABaseCharacter','AFightingCharacter','FAvailabilityContext','FAvailabilityLayer','AvailabilityLayerManager','FPlayOrderInfos'}
    source=re.sub(r'TARGET_NAMES = \{.*?\n\}', 'TARGET_NAMES = '+repr(targets),source,count=1,flags=re.S)
    source=re.sub(r'RELEVANT = re.compile\(.*?\n','RELEVANT = re.compile(r"(?!)")\n',source,count=1)
    source=source.replace('if ((attrs >> 2) & 0x7) == 4: q,_=cvnum(data,q)','if ((attrs >> 2) & 0x7) in (4,6): q+=4')
    source=source.replace("ROOT/'inventory'/'focused_type_layouts.json'", "ROOT/'inventory'/'"+GROUP+"-types.json'")
    exec(compile(source,'adapted-defense-types','exec'),{'__name__':'__main__'})
    files=[OUT/(GROUP+'-vtables.json'),OUT/(GROUP+'-types.json'),OUT/(GROUP+'-disassembly.json')]
    batch=dict(build=build,python=sys.version,platform=platform.platform(),cwd=str(Path.cwd()),command='D:/Programes/PY/python.exe scripts/interaction_20261030_defense_probe.py',script_sha256=sha(__file__),type_reader_sha256=sha(R/'scripts/inspect_types.py'),disassembler_sha256=sha(R/'scripts/disassemble_research.py'),tool=str(TOOL),tool_sha256=sha(TOOL),outputs=[dict(path=str(p.relative_to(R)),sha256=sha(p)) for p in files],limitations=['Exact-build static evidence only; no runtime or game mutation.','Type reader applies the previously documented fixed-width LF_ONEMETHOD adaptation in memory.'])
    (OUT/(GROUP+'-batch.json')).write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(hits,ensure_ascii=False));print('build',build)
if __name__=='__main__':main()
