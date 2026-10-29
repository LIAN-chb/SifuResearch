"""Bounded decoding of layers referenced by current barehand actions."""
import gzip,json,hashlib,sys
from pathlib import Path
R=Path(__file__).resolve().parents[2];O=Path(__file__).parent
sys.path.insert(0,str(R/'tools'));import external_read_packages as q
def read(p):return json.loads((R/p).read_text(encoding='utf-8'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
d=read('exports/20261029-徒手补全与命名-13/board-data.json')
refs={w['m_Layer[0]'] for a in [*d['attacks'].values(),*d['outsideAttacks'].values()] for w in a['raw'].get('m_AvailabilityLayerWindows[0]',[])}
pkgs={p['path']:p for p in json.load(gzip.open(R/'inventory/package-metadata.json.gz','rt',encoding='utf-8'))}
layers={}
for ref in sorted(refs):
 path=ref.split('.')[0].replace('/Game/','Sifu/Content/')+'.uasset';p=pkgs[path];f=R/'extracted'/path
 assert sha(f)==p['uassetSha256']
 e=p['exports'][0];start=e['serialOffset']-f.stat().st_size;raw=f.with_suffix('.uexp').read_bytes()[start:start+e['serialSize']]
 ps,n=q.tags(raw,p['names']);assert n+4==len(raw) and raw[n:]==b'\0'*4
 prop=next(x for x in ps if x['name']=='m_inputActionArray');v=raw[prop['valueOffset']:prop['valueOffset']+prop['size']];reader=q.Reader(v,p['names']);count=reader.number('i');assert len(v)==4+count*8
 actions=[reader.name().split('::')[-1] for _ in range(count)];assert reader.position==len(v)
 invert=next((x['value'] for x in ps if x['name']=='m_bInvertSelection'),False)
 layers[ref]={'asset':path,'uasset_sha256':sha(f),'uexp_sha256':sha(f.with_suffix('.uexp')),'invert':invert,'listedActions':actions,'listMeaning':'excluded' if invert else 'allowed','context':next((x['value'] for x in ps if x['name']=='m_eContext'),0),'stage':'parsed-and-mask-generation-linked'}
out={'layers':layers,'attackWindowOperation':'OR','operationEvidence':{'function':'<lambda_7cb6b301a3c0853722a3f97a5ad63bb6>::operator()','rva':'0x1AC5E60','pushCall':'0x1AC5EAF','operationAssignment':'0x1AC5E90 r8b=2'},'limits':['OR describes attack windows in their context, not bypass of all other contexts, movement, input selection or action start checks.','No runtime verification.'],'script_sha256':sha(Path(__file__))}
out['inputTransitionMapping']=read('inventory/player-unknown-08-input-evidence.json')['mapping']
ability=next(a for a in read('exports/20261029-徒手补全与命名-13/actions-ability-cdos.json') if a['asset'].endswith('/BP_AttackAbility.uasset'))
assert sha(R/'extracted'/ability['asset'])==ability['source_sha256']
assert sha((R/'extracted'/ability['asset']).with_suffix('.uexp'))==ability['uexp_sha256']
out['attackAbilityInputsInPriorityOrder']=ability['properties']['m_Inputs[0]']
out['selectionEvidence']={'function':'UAttackAbility::GetBestAttackAction','rva':'0x19BB340','filterCall':'0x19BB42E','priorityScan':'0x19BB4A7-0x19BB575','rule':'available stack-top actions are scanned in Ability m_Inputs order, first surviving target requirement wins','limits':['Base-condition validation, valid next combo node and ability activation remain required; priority alone does not guarantee successful execution.']}
out['conditionMaskRule']={'state0':2,'state1':8,'state2':4,'otherStateFlagFalse':1,'otherStateFlagTrue':16,'evidence':'FComboAttack::EnumerateAvailabilityLayerChanges RVA 0x1957C60, 0x1957D54-0x1957D82','labelsStatus':'state enum symbolic names not recovered here; mask31 accepts all five branches'}
(O/'availability-layers.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8');print(len(layers))
