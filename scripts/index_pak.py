import collections,hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
PAK=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak')
TOOL=ROOT/'tools/repak-v0.2.3/repak.exe'
source=(ROOT/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')
keymatch=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',source)
if not keymatch:raise ValueError('No key found in inspected tool source')
key=keymatch.group(1)
version=subprocess.run([str(TOOL),'--version'],capture_output=True,text=True,check=True).stdout.strip()
outputs={}
for cmd in ('info','list'):
 p=subprocess.run([str(TOOL),'--aes-key',key,cmd,str(PAK)],capture_output=True,text=True)
 (ROOT/'logs'/f'repak-{cmd}.stderr.txt').write_text(p.stderr,encoding='utf-8')
 (ROOT/'inventory'/f'pak-{cmd}.txt').write_text(p.stdout,encoding='utf-8')
 if p.returncode:raise RuntimeError(f'repak {cmd} failed: {p.stderr[:1500]}')
 outputs[cmd]=p.stdout
paths=[s for s in outputs['list'].splitlines() if s.strip()]
hints=[s for s in paths if re.search(r'/DB/AI/|/AI/|Attack|Impact|Stun|Dizzy|Guard|Structure|HitReaction|ContextDefense|ContextualDefense|Domination|Ticket|CombatRole',s,re.I)]
(ROOT/'inventory/pak-research-candidates.txt').write_text('\n'.join(hints)+'\n',encoding='utf-8')
report={'pak':str(PAK),'pak_size':PAK.stat().st_size,'repak':version,'list_entry_count':len(paths),'candidate_path_count':len(hints),'decryption_key_source':'ChorlsChu/Custom-Moveset-Maker--Sifu-Mod- main/Setup/ContentExtractor.cs','public_key_test':'Accepted by repak; index parsed successfully for this local PAK','path_extensions':dict(collections.Counter(Path(s).suffix for s in paths)),'info':outputs['info']}
(ROOT/'inventory/pak-overview.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
print('CANDIDATE_EXAMPLES',json.dumps(hints[:45],ensure_ascii=False))
