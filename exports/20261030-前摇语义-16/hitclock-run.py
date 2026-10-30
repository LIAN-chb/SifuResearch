from pathlib import Path
import sys,json,hashlib,struct,uuid
sys.dont_write_bytecode=True
root=Path.cwd(); out=root/'exports/20261030-前摇语义-16'; out.mkdir(exist_ok=True)
sys.path.insert(0,str(root/'scripts'))
from index_pdb import Msf,PDB,EXE
m=Msf(PDB); pi=m.stream(1); info={'guid':str(uuid.UUID(bytes_le=pi[12:28])),'age':struct.unpack_from('<I',pi,8)[0]};m.close()
expected=json.loads((root/'inventory/pdb_overview.json').read_text()); assert info==expected['pdb_info']; assert hashlib.sha256(EXE.read_bytes()).hexdigest()==expected['exe_sha256']
code=(root/'scripts/disassemble_research.py').read_text().replace("directory=ROOT/'logs'/group", "directory=ROOT/'logs'/group").replace("(ROOT/'inventory'/(group+'-disassembly.json'))", "(ROOT/'exports/20261030-前摇语义-16'/('hitclock-'+group.removeprefix('hitclock16-')+'-disassembly.json'))")
ns={'__name__':'adapted'};exec(compile(code,'scripts/disassemble_research.py','exec'),ns)
names=['FComboAttack::GetAttackStateAtFrame','FComboAttack::GetHitBoxIndexAtFrameWithPredicate','FComboAttack::GetLastHitFrame','FComboAttack::EnumerateWindowIndexesAtFrame<FHitBox,FHitBox>','OrderAttack::EnumerateActiveHitBoxes','OrderAttack::GetNextHitBoxIndexes','OrderAttack::OnUpdate','OrderAttack::GetTimeFromRatio','OrderAttack::OnStart','OrderAttack::ComputePhaseInfo','OrderAttack::GetAttackState','AnimationHelper::UpdateAnimHelperParams']
report=ns['disassemble'](names,'hitclock16-disassembly')
(root/'exports/20261030-前摇语义-16/hitclock-build.json').write_text(json.dumps({'exe_sha256':expected['exe_sha256'],'live_pdb_info':info,'script_source_sha256':hashlib.sha256((root/'scripts/disassemble_research.py').read_bytes()).hexdigest(),'adaptation':'only report path redirected; output logs/hitclock16-disassembly'},indent=2))
