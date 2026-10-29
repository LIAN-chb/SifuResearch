from pathlib import Path
import re,subprocess,hashlib,json,datetime
R=Path(r'E:\ProgrameFiles\SifuResearch');pak=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak');tool=R/'tools/repak-v0.2.3/repak.exe';out=R/'logs/case-resilience/extracted'
paths=[x for x in (R/'inventory/pak-list.txt').read_text(encoding='utf-8').splitlines()
       if x.startswith('Sifu/Content/Animations/Grunt/Attacks/Barehands/') and x.endswith('.uasset') and '/_old/' not in x]
paths += ['Sifu/Content/Animations/System/Orders/Services/Attack/BP_ResilienceOrderService.uasset','Sifu/Content/Animations/System/Orders/Services/Attack/BP_ResilienceOrderService_Base.uasset','Sifu/Content/Animations/System/Orders/Services/Attack/BP_SuperResilienceOrderService.uasset']
out.mkdir(parents=True,exist_ok=True)
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(R/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
cmd=[str(tool),'--aes-key',key,'unpack',str(pak),'--output',str(out),'--quiet']
for p in paths:
 for ext in ['.uasset','.uexp']:cmd.extend(['--include',str(Path(p).with_suffix(ext))])
expected=[out/Path(a).with_suffix(ext) for a in paths for ext in ['.uasset','.uexp']]
if all(x.is_file() for x in expected):
 rc=0
else:
 p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace');rc=p.returncode
 if rc:raise RuntimeError(f'Targeted repak failed rc={rc}: {(p.stderr or p.stdout or '')[:1000]}')
files=[];missing=[]
for asset in paths:
 for ext in ['.uasset','.uexp']:
  path=out/Path(asset).with_suffix(ext)
  if path.is_file():files.append({'path':str(path),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'status':'extracted'})
  else:missing.append(str(path))
paksha=hashlib.sha256(pak.read_bytes()).hexdigest()
report={'batch':'case-resilience-20261028','sourcePak':str(pak),'sourcePakSha256':paksha,'selectedAssets':paths,'files':files,'missing':missing,'exitCode':rc,'tool':str(tool),'limitations':['Extraction does not parse animation notify semantics.','No runtime execution.']}
(R/'inventory/case-resilience-extraction-20261028.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'exitCode':rc,'files':len(files),'missing':missing,'pakSha256':paksha},ensure_ascii=False))
