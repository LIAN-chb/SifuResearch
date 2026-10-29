import hashlib,json,re,subprocess,time
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
PAK=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak')
TOOL=ROOT/'tools/repak-v0.2.3/repak.exe'
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(ROOT/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
paths=(ROOT/'inventory/pak-list.txt').read_text(encoding='utf-8').splitlines()
prefixes=['Sifu/Content/DB/','Sifu/Content/Blueprints/AI/','Sifu/Config/']
project=[p for p in paths if p.endswith('.uproject')]
selected=[p for p in paths if any(p.startswith(x) for x in prefixes) or p in project]
if not selected:raise ValueError('No selected paths')
cmd=[str(TOOL),'--aes-key',key,'unpack',str(PAK),'--output',str(ROOT/'extracted'),'--quiet']
for p in prefixes+project:cmd.extend(['--include',p])
t0=time.monotonic();p=subprocess.run(cmd,capture_output=True,text=True)
(ROOT/'logs/repak-extract.stdout.txt').write_text(p.stdout,encoding='utf-8')
(ROOT/'logs/repak-extract.stderr.txt').write_text(p.stderr,encoding='utf-8')
if p.returncode:raise RuntimeError(f'Extraction failed: {p.stderr[:1500]}')
manifest=[];missing=[]
for name in selected:
 dest=ROOT/'extracted'/name
 if not dest.is_file():missing.append(name);continue
 manifest.append({'path':name,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()})
(ROOT/'inventory/extracted-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
report={'selected_prefixes':prefixes,'selected_paths':len(selected),'extracted_files':len(manifest),'extracted_bytes':sum(x['bytes'] for x in manifest),'missing_paths':missing,'elapsed_seconds':round(time.monotonic()-t0,2),'original_game_modified':False,'note':'Successful read/extraction is not equivalent to semantic parsing or runtime validation.'}
(ROOT/'inventory/extraction-overview.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(report,ensure_ascii=False,indent=2))
