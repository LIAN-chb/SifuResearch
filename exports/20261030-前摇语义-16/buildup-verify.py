from pathlib import Path
import json,hashlib,sys,ast,platform
R=Path('E:/ProgrameFiles/SifuResearch');out=R/'exports/20261030-前摇语义-16'
d=json.loads((out/'buildup-types.json').read_text(encoding='utf-8'))
expected={'OrderAttack':{'m_fInitialPlayRate':0x4c4,'m_fBuildUpScale':0x5a8,'m_HelperParams':0x1c0,'m_bPlayRateManagedOutside':0xab8},'FComboAttack':{'m_iWantedBuildupFrames':0xb4},'FAttackDataRow':{'m_iLastBuildupFrame':0x6c},'UDefenseComponent':{'m_fBuildUpFramesMultiplicator':0x1f8},'OrderBase':{'m_bInPrediction':0x100},'FNetOrderStructAttack':{'m_fStartRatio':0xf0},'UAnimSequenceBase':{'RateScale':0x94}}
for name,fields in expected.items():
 x=next(x for x in d['layouts'] if x['name']==name);got={f['name']:f.get('offset_bytes') for f in x['fields'] if 'name' in f};assert all(got[k]==v for k,v in fields.items())
paths=[R/'scripts/inspect_types.py',R/'scripts/disassemble_research.py',R/'scripts/index_pdb.py',*out.glob('buildup-*'),*(R/'logs/20261030-前摇语义-16').glob('buildup-*/*.txt'),R/'notes/player-timing-16-buildup.md']
items=[]
for p in paths:
 if not p.is_file() or p.name=='buildup-verification.json':continue
 if p.suffix=='.py':ast.parse(p.read_text(encoding='utf-8-sig'))
 items.append({'path':str(p.relative_to(R)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
manifest={'python':sys.version,'platform':platform.platform(),'cwd':str(R),'scope':'static code/type correspondence only; no runtime verification','checks':{'selected_layout_offsets':'passed','python_ast':'passed','artifacts_hashed':len(items)},'files':items,'disassembly_groups':{'buildup-first':['OrderAttack::GetInitialPlayRate','OrderAttack::SetPlayRate','OrderAttack::UpdatePlayRate','AnimationHelperSequenceContext::AnimationHelperSequenceContext'],'buildup-update':['OrderAttack::OnUpdate','OrderAttack::ComputePhaseInfo'],'buildup-clock':['OrderAttack::GetPlayRate','AnimationHelperParams::GetCurrentFrame','AnimationHelperParams::GetCurrentAnimRatio','AnimationHelper::UpdateAnimHelperParams','OrderAttack::ActivatePlayRateManagedOutside'],'buildup-branches':['FNetOrderStructAttack::FNetOrderStructAttack','OrderAttack::PushFreezeOrder','OrderAttack::PopFreezeOrder','OrderAttack::OnNetStructUpdated']},'missing_index_names':['OrderAttack::Init','OrderAttack::PreStart','OrderAttack::OnPreStart','FComboAttack::ConvertAnimFrameToGameplay','FComboAttack::ConvertGameplayFrameToAnim'],'next_step':'No retry of missing names required: actual consumer path and conversion arithmetic recovered from OnStart/OnUpdate/ComputePhaseInfo.'}
(out/'buildup-verification.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8');print(manifest['checks'])
