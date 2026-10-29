from pathlib import Path
import re,json,subprocess,hashlib,sys
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
PAK=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak')
tool=R/'tools/repak-v0.2.3/repak.exe'
paths=['Sifu/Content/Localization/Game/en/Game.locres','Sifu/Content/Localization/Game/zh-Hans/Game.locres','Sifu/Content/Localization/Game/Game.locmeta']
listed=set((R/'inventory/pak-list.txt').read_text(encoding='utf-8').splitlines());assert set(paths)<=listed
dest=O/'extracted'
assert not dest.exists(),'Do not overwrite an earlier extraction'
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(R/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
args=[str(tool),'--aes-key',key,'unpack',str(PAK),'--output',str(dest),'--quiet']
for p in paths:args+=['--include',p]
before={'bytes':PAK.stat().st_size,'mtime_ns':PAK.stat().st_mtime_ns}
result=subprocess.run(args,capture_output=True,text=True)
(O/'extract.stdout.txt').write_text(result.stdout,encoding='utf-8');(O/'extract.stderr.txt').write_text(result.stderr,encoding='utf-8')
assert result.returncode==0,result.stderr
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
files=[{'path':p,'bytes':(dest/p).stat().st_size,'sha256':sha(dest/p)} for p in paths]
assert before=={'bytes':PAK.stat().st_size,'mtime_ns':PAK.stat().st_mtime_ns}
report={'pak':str(PAK),'pak_identity':before,'pak_full_sha256':'not recomputed; bounded extraction, pak list and metadata reused','tool_sha256':sha(tool),'tool_version':subprocess.run([str(tool),'--version'],capture_output=True,text=True,check=True).stdout.strip(),'command':[a if a!=key else '<key from tools/ContentExtractor.cs; redacted>' for a in args],'exit_code':result.returncode,'python':sys.version,'script_sha256':sha(Path(__file__)),'files':files,'scope':'two game locale files and localization metadata only; no game file writes'}
(O/'extraction-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'files':len(files),'bytes':sum(x['bytes'] for x in files),'status':'extracted'},ensure_ascii=True))
