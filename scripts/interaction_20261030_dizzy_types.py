"""Reproduce interrupted branch's seven selected CodeView layouts, preserving its original output."""
from pathlib import Path
import re,sys,json,hashlib
R=Path(__file__).resolve().parents[1];sys.path.insert(0,str(R/'scripts'))
targets={'FAISuperDizzyParams','FAppliedHitImpact','FApplyImpactStruct','FDefenseGauge','OrderAttack','OrderBase','UArchetypeAsset'}
s=(R/'scripts/rules_20261029_count_types.py').read_text(encoding='utf-8')
s=re.sub(r'TARGET_NAMES = .*?\nRELEVANT = .*?\n','TARGET_NAMES = '+repr(targets)+'\nRELEVANT = re.compile(r"(?!)")\n',s,count=1)
s=s.replace('if ((attrs >> 2) & 0x7) == 4: q,_=cvnum(data,q)','if ((attrs >> 2) & 0x7) in (4,6): q+=4')
s=s.replace('rules-20261029-count-target-layouts.json','interaction-20261030-dizzy-rechecked-layouts.json')
assert 'interaction-20261030-dizzy-rechecked-layouts.json' in s
exec(compile(s,'rechecked-dizzy-types','exec'),{'__name__':'__main__'})
out=R/'inventory/interaction-20261030-dizzy-rechecked-layouts.json'
a=json.loads(out.read_text(encoding='utf-8'));assert set(a['target_names_found'])==targets
def sha(p):
    with Path(p).open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()
batch=dict(cwd=str(R),command='D:/Programes/PY/python.exe scripts/interaction_20261030_dizzy_types.py',exit_code=0,python=sys.version,script_sha256=sha(__file__),reader_sha256=sha(R/'scripts/rules_20261029_count_types.py'),input_build='inventory/interaction-20261030-defense-batch.json',output=str(out.relative_to(R)),output_sha256=sha(out),reason='Background branch stopped before final execution manifest; rerun only this seven-type reader with saved exact adapter. Original branch output preserved.',limitations=['PDB declaration only; methods independently verified in named disassembly.','Known LF_ONEMETHOD fixed-width adaptation applied in memory.'])
(R/'inventory/interaction-20261030-dizzy-types-batch.json').write_text(json.dumps(batch,ensure_ascii=False,indent=2),encoding='utf-8')
