from pathlib import Path
import json,gzip,struct,hashlib,sys,importlib.util
R=Path(__file__).resolve().parents[2]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads((R/p).read_text(encoding='utf-8'))
overview=read('inventory/pdb_overview.json');exe=Path(overview['exe']);b=exe.read_bytes();assert hashlib.sha256(b).hexdigest()==overview['exe_sha256']
pe=struct.unpack_from('<I',b,0x3c)[0];sections=[]
for i in range(struct.unpack_from('<H',b,pe+6)[0]):
 o=pe+24+struct.unpack_from('<H',b,pe+20)[0]+40*i
 vs,va,sz,ptr=struct.unpack_from('<4I',b,o+8);sections.append((va,max(vs,sz),ptr))
def off(rv):
 for va,sz,ptr in sections:
  if va<=rv<va+sz:return ptr+rv-va
 raise ValueError(hex(rv))
def u32(rv):return struct.unpack_from('<I',b,off(rv))[0]
def returned(rv):
 code=b[off(rv):off(rv)+3]
 if code==b'\x32\xc0\xc3':return 0
 if code[0]==0xb0 and code[2]==0xc3:return code[1]
 raise ValueError(code.hex())
types=read('inventory/player-unknown-08-input-types.json');enums={x['name']:{f['value']:f['name'] for f in x['fields'] if f['kind']=='enumerator'} for x in types['layouts'] if x['leaf']=='0x1507'}
trans=next(x for x in read('inventory/player-combo-type-layouts.json')['layouts'] if x['name']=='EComboTransition');trans={f['value']:f['name'] for f in trans['fields']}
mapping=[]
for t in range(21):
 target=u32(0x1950234+t*4);i=returned(target)
 if i<=0xae:
  inverse_index=b[off(0x1950670+i)];inverse_target=u32(0x1950618+inverse_index*4);back=returned(inverse_target)
  assert back==t
 else:inverse_target=0x1950614;back=22
 mapping.append({'transition':trans[t],'transition_value':t,'input':enums['InputAction'][i],'input_value':i,'get_input_case_rva':hex(target),'get_transition_case_rva':hex(inverse_target),'inverse_matches':back==t})
all_assets=json.load(gzip.open(R/'inventory/tagged-objects.json.gz','rt',encoding='utf-8'))
selected=[]
for x in all_assets:
 if '/DB/Inputs/' not in x['asset']:continue
 if any(k in x['asset'] for k in ['AttackLight.','AttackHeavy.','AttackLightAlt.','AttackHeavyAlt.','AttackLightFrontFront.','AttackHeavyFrontFront.','AttackLightBackFront.','AttackHeavyBackFront.','DirBackFront.','DirFrontFront.','AttackLightHold.','AttackHeavyHold.']):selected.append(x)
spec=importlib.util.spec_from_file_location('input_bounded_reader',R/'tools/external_read_packages.py');q=importlib.util.module_from_spec(spec);spec.loader.exec_module(q)
packages={p['path']:p for p in json.load(gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8'))}
for x in selected:
 pkg=packages[x['asset']];p=R/'extracted'/x['asset'];payload=p.with_suffix('.uexp').read_bytes();exp=pkg['exports'][x['export_index']-1];start=exp['serialOffset']-p.stat().st_size;end=start+exp['serialSize'];raw=payload[start:end]
 for prop in x['properties']:
  if prop['name'] in ['m_StackSiblings','m_StackResetSiblings']:
   rr=q.Reader(raw[prop['valueOffset']:prop['valueOffset']+prop['size']],pkg['names'])
   count=rr.number('i');assert 0<=count<=100
   prop['enumValues']=[rr.name() for _ in range(count)];assert rr.position==prop['size']
contexts=[]
for x in all_assets:
 refs=[]
 for p in x.get('properties',[]):
  if p['name']=='m_inputActions':refs=p.get('arrayReferences',[])
 if any('/AttackLightAlt.' in str(r) or '/AttackHeavyAlt.' in str(r) for r in refs):contexts.append({'asset':x['asset'],'export':x['export'],'sha256':x['sha256'],'m_inputActions':refs})
hashes={}
for x in selected+contexts:
 for ext in ['.uasset','.uexp']:
  p=(R/'extracted'/x['asset']).with_suffix(ext)
  if p.exists():hashes[str(p.relative_to(R))]=sha(p)
out={'exe_sha256':overview['exe_sha256'],'pdb_build':'inventory/player-unknown-08-build.json','mapping':mapping,'assets':selected,'contexts':contexts,'source_sha256':{str(p.relative_to(R)):sha(p) for p in [R/'inventory/tagged-objects.json.gz',R/'inventory/player-unknown-08-input-types.json',R/'inventory/player-combo-type-layouts.json']},'extracted_hashes':hashes,'script_sha256':sha(Path(__file__)),'python':sys.version,'checks':{'all_mapped_inputs_round_trip':all(x['inverse_matches'] for x in mapping if x['input_value']<=0xae)},'limits':['static mapping and saved InputData; actual runtime availability and user keybindings remain contextual','JustReleasedBefore is short hold then release, not simultaneous or alternating light/heavy','direction-combination sequences may depend on reference orientation; not established from asset names']}
out['tool_sha256']={f:sha(R/f) for f in ['scripts/disassemble_research.py','scripts/inspect_player_combo_types.py','tools/external_read_packages.py','exports/20261029-玩家招式待核-08/input-types.py']}
(R/'inventory/player-unknown-08-input-evidence.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'mapping':mapping,'contexts':[x['asset'] for x in contexts],'assets':len(selected)},ensure_ascii=False,indent=2))
