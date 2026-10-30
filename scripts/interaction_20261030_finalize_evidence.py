"""Verify persisted independent evidence, close Counter_Hit virtual slot, save reproducible manifest."""
from pathlib import Path
import sys,json,struct,hashlib,uuid,csv,datetime,subprocess
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'scripts'))
from index_pdb import Msf,PDB,EXE
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
old=json.loads((R/'inventory/pdb_overview.json').read_text(encoding='utf-8'))
m=Msf(PDB);info=m.stream(1);m.close()
build=dict(exe_sha256=sha(EXE),pdb_sha256=sha(PDB),guid=str(uuid.UUID(bytes_le=info[12:28])),age=struct.unpack_from('<I',info,8)[0])
assert build['exe_sha256']==old['exe_sha256'] and build['guid']==old['pdb_info']['guid'] and build['age']==old['pdb_info']['age']
data=EXE.read_bytes();pe=struct.unpack_from('<I',data,60)[0];op=struct.unpack_from('<H',data,pe+20)[0]
def off(r):
    for i in range(struct.unpack_from('<H',data,pe+6)[0]):
        p=pe+24+op+40*i;vs,va,rs,rp=struct.unpack_from('<4I',data,p+8)
        if va<=r<va+max(vs,rs):return rp+r-va
    raise ValueError(hex(r))
slot=struct.unpack_from('<Q',data,off(0x48883c0)+0x60)[0]-0x140000000
assert slot==0x1ad35f0
slot_result=dict(source_symbols='exports/20261030-前摇语义-16/buildup-publics.json',source_sha256=sha(R/'exports/20261030-前摇语义-16/buildup-publics.json'),vtable_rva='0x48883c0',symbol='??_7OrderAttack@@6BOrderAttackInterface@@@',slot='0x60',target_rva=hex(slot),interpretation='GetAttackState; PE slot re-read in the current exact build',build=build)
(R/'inventory/interaction-20261030-counter-slot.json').write_text(json.dumps(slot_result,ensure_ascii=False,indent=2),encoding='utf-8')
manifests=[];failures=[];unique={};reproduce=[]
for p in sorted((R/'inventory').glob('interaction-20261030-*-disassembly.json')):
    a=json.loads(p.read_text(encoding='utf-8'));assert a['exe_sha256']==build['exe_sha256']
    for x in a['procedures']:
        if x['status']!='disassembled':failures.append(dict(manifest=p.name,**x));continue
        q=Path(x['file']);assert sha(q)==x['assembly_sha256'],str(q)
        unique[str(q)]=dict(path=str(q.relative_to(R)),sha256=sha(q),function=x['name'],rva=x['rva'],status='verified')
    names=list(dict.fromkeys(x['name'] for x in a['procedures']))
    reproduce.append(dict(manifest=p.name,command=[str(Path(sys.executable)),'scripts/disassemble_research.py','--group',p.name.removesuffix('-disassembly.json'),*[v for n in names for v in ['--name',n]]],origin='Reconstructed argument vector from persisted manifest, not a claim that this finalizer reran the command.'))
    manifests.append(dict(path=str(p.relative_to(R)),sha256=sha(p)))
# Exact lookup was attempted, but no flattened property exists under this spelling.
src=R/'inventory/object-and-table-properties.csv';rows=[]
with src.open(encoding='utf-8-sig') as f:
    for i,x in enumerate(csv.DictReader(f),2):
        if x['property'].startswith('m_SuperDizzyPerDifficulty'):rows.append(dict(csv_line=i,**x))
scripts=[p for p in (R/'scripts').glob('interaction*20261030*.py')]
types=json.loads((R/'inventory/interaction-20261030-dizzy-rechecked-layouts.json').read_text(encoding='utf-8'))
archetype=next(v for v in types['layouts'] if v['name']=='UArchetypeAsset')
array=next(f for f in archetype['fields'] if f.get('name')=='m_SuperDizzyPerDifficulty')
assert array['offset_bytes']==0x3c and array['type']['name']=='FAISuperDizzyParams[3]'
deprecated=next(f for f in archetype['fields'] if f.get('name')=='m_bCanBeSuperDizzy_DEPRECATED')
assert deprecated['offset_bytes']==0x84
report=dict(checked_at=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).isoformat(),cwd=str(R),command='D:/Programes/PY/python.exe scripts/interaction_20261030_finalize_evidence.py',python=sys.version,build=build,script_sha256=sha(__file__),scripts=[dict(path=str(p.relative_to(R)),sha256=sha(p)) for p in sorted(scripts)],manifests=manifests,verified_assemblies=list(unique.values()),missing_procedures=failures,reproduction_arguments=reproduce,counter_slot=slot_result,difficulty_array=dict(source='inventory/interaction-20261030-dizzy-rechecked-layouts.json',source_sha256=sha(R/'inventory/interaction-20261030-dizzy-rechecked-layouts.json'),type=array['type']['name'],offset=array['offset_bytes'],deprecated_block_offset=deprecated['offset_bytes']),configuration_lookup=dict(source=str(src.relative_to(R)),sha256=sha(src),prefix='m_SuperDizzyPerDifficulty',matches=len(rows),limitation='No matching flattened property under this spelling; this does not prove no serialized override or no usable default.'),limitations=['Background branches stopped before final response; persisted outputs were independently hash-checked here.','All static evidence; no gameplay or final frame timing verified.'])
(R/'inventory/interaction-20261030-batch.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(status='passed',assemblies=len(unique),manifests=len(manifests),missing=[x['name'] for x in failures],counter_slot=hex(slot),configuration_prefix_matches=len(rows))))
