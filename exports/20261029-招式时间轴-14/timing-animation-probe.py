"""Bounded one-animation extraction and scalar metadata probe, no game writes."""
from pathlib import Path
import sys,re,json,subprocess,hashlib
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
sys.path.insert(0,str(R/'tools'));import local_bounded_packages as q
asset='Sifu/Content/Animations/MainChar/Attacks/Man/Barehands/LightCombo/MainChar_Attack_Man_Barehands_Pressure_Jab_FR'
entries=(R/'inventory/pak-list.txt').read_text(encoding='utf8').splitlines()
selected=[s for s in entries if s in [asset+x for x in ['.uasset','.uexp','.ubulk']]]
assert len(selected)>=2
key=re.search(r'Hex\s+(0x[0-9a-fA-F]{64})',(R/'tools/ContentExtractor.cs').read_text(encoding='utf-8-sig')).group(1)
dest=R/'logs/20261029-招式时间轴-14/timing-animation-extracted'
cmd=[str(R/'tools/repak-v0.2.3/repak.exe'),'--aes-key',key,'unpack',r'E:\Games_Little\Epic\Sifu\Sifu\Content\Paks\pakchunk0-WindowsNoEditor.pak','--output',str(dest),'--quiet']
for p in selected:cmd.extend(['--include',p])
r=subprocess.run(cmd,capture_output=True,text=True);assert r.returncode==0,r.stderr
p=dest/(asset+'.uasset');meta=q.read_package(p,dest);body=p.with_suffix('.uexp').read_bytes()
e=next(e for e in meta['exports'] if e['name']==Path(asset).name);start=e['serialOffset']-p.stat().st_size
raw=body[start:start+e['serialSize']];assert len(raw)==e['serialSize']
props,n=q.tags(raw,meta['names'])
simple={p['name']:p['value'] for p in props if p['name'] in ['NumFrames','SequenceLength','RateScale','bEnableRootMotion','Interpolation']}
report={'asset':asset+'.uasset','scalars':simple,'propertyBytes':n,'nativeSuffixBytes':len(raw)-n,'selected':selected,'files':[{'path':str(dest/s),'bytes':(dest/s).stat().st_size,'sha256':hashlib.sha256((dest/s).read_bytes()).hexdigest()} for s in selected],'command':'repak --aes-key <redacted> unpack <configured game pak> --output <batch>/timing-animation-extracted --quiet '+ ' '.join('--include '+s for s in selected),'limits':['Scalar tagged data only; native suffix and actual playback range not decoded.']}
(O/'timing-animation-probe.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(report['scalars']))
