from pathlib import Path
import sys, re, hashlib, json, struct, uuid
R=Path('E:/ProgrameFiles/SifuResearch');sys.path.insert(0,str(R/'scripts'))
from index_pdb import Msf,PDB,EXE
out=R/'exports/20261030-前摇语义-16'
m=Msf(PDB);info=m.stream(1);guid=str(uuid.UUID(bytes_le=info[12:28]));age=struct.unpack_from('<I',info,8)[0];m.close()
old=json.loads((R/'inventory/pdb_overview.json').read_text());eh=hashlib.sha256(EXE.read_bytes()).hexdigest();ph=hashlib.file_digest(PDB.open('rb'),'sha256').hexdigest()
assert eh==old['exe_sha256'] and guid==old['pdb_info']['guid'] and age==old['pdb_info']['age']
(out/'buildup-build.json').write_text(json.dumps(dict(exe_sha256=eh,pdb_sha256=ph,guid=guid,age=age),indent=2))
s=(R/'scripts/inspect_types.py').read_text();s=s.replace("TARGET_NAMES = {", "TARGET_NAMES = {'AnimationHelperParams','AnimationHelperSequenceContext','OrderAttack','FComboAttack','FAttackDataRow','OrderAttackInterface','UDefenseComponent','FAnimContainer','OrderBase','FNetOrderStructAttack','UAnimSequenceBase','OrderAttack::FreezeStruct',")
s=s.replace('if ((attrs >> 2) & 0x7) == 4: q,_=cvnum(data,q)', 'if ((attrs >> 2) & 0x7) in (4,6): q+=4')
s=s.replace("ROOT/'inventory'/'focused_type_layouts.json'","ROOT/'exports/20261030-前摇语义-16'/'buildup-types.json'")
exec(compile(s,'adapted-inspect-types','exec'),{'__name__':'__main__'})
