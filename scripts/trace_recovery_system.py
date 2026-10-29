"""Reproduce bounded static evidence for the Sifu hit-to-recovery chain."""
import sys, json, hashlib, csv
from pathlib import Path
ROOT=Path(r'E:\ProgrameFiles\SifuResearch')
sys.path.insert(0,str(ROOT/'scripts'))
sys.dont_write_bytecode=True
from disassemble_research import disassemble
NAMES=[
 'OrderHitted::OnStart','OrderHitted::OnUpdate','OrderHitted::OnStop','UHitComponent::GenerateImpact',
 'InternalConstructor<UAIInfluenceTest>','InternalConstructor<UAttackMemoryInfluenceTest>',
 'OrderFightingState::OnStart','OrderFightingState::OnStop',
 'OrderFightingState::OnTimeLeftReachedZero','OrderFightingState::PopFightingState',
 'OrderFightingStateRecovery::OnStart','UHitComponent::ApplyFightingStateFromImpact',
 'UHitComponent::UpdateFightingStateFromImpact','UHitComponent::ApplyImpact','UHitComponent::ComputeImpactType','UHitComponent::LaunchImpactInternal',
 'UHitComponent::LaunchFightingStateOrder','UHitComponent::LaunchFightingStateRecovery',
 'UOrderComponent::PlayOrder','UOrderComponent::MultiCastPlayOrder_Implementation',
 'UOrderComponent::MultiCastUpdateOrder_Implementation','UOrderComponent::OnOrderStarted',
 'UOrderComponent::OnOrderStarting','UOrderComponent::OnOrderEnded','UOrderComponent::UpdateOrderOnNetwork',
 'AFightingCharacter::PlayOrder','AFightingCharacter::PlayOrderWithType',
 'OrderManager::PlayOrder','OrderManager::GetOrderFromType','OrderManager::GetOrdersFromType',
 'OrderHitted::OnNetStructUpdated','OrderHitted::OnCancelledBeforeStart','OrderHitted::OnTargetChanged',
 'FHitboxDataRow::GetAttackPropertyLevel','AFightingCharacter::Hitted_Implementation',
 'FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero',
 'FAIDefenseHandler::UpdateDefenseNeed']

def main():
    report=disassemble(NAMES,'system-recovery')
    data=json.loads((ROOT/'inventory/stun-state-data.json').read_text(encoding='utf-8'))
    grunt=[x for x in data['hitted_assets'] if x['asset'].endswith('/Grunt/HitsAnims/GruntHittedDB.uasset')]
    if len(grunt)!=1: raise RuntimeError(f'Expected one GruntHittedDB, got {len(grunt)}')
    wanted=['asset','m_bTimeSinceLastHitPrevails[0]','m_bLongestStunPrevailsBetweenHits[0]','m_HitRecoveryAvailability[0]','m_Parent[0]','m_HitAnimationRequest[0]']
    entry={k:grunt[0].get(k) for k in wanted}
    (ROOT/'inventory/system-recovery-grunt-hitteddb.json').write_text(json.dumps(entry,ensure_ascii=False,indent=2),encoding='utf-8')
    matrix=[]
    with (ROOT/'exports/state-resistance-matrices.csv').open(encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            if any(tag in row['asset'] for tag in ('Grunt_Base_ResistanceDB','Grunt_Adv_ResistanceDB')):
                matrix.append({k:row[k] for k in ('asset','state','knockdown_resistance_col0','push_resistance_col1','dizzy_resistance_col2')})
    (ROOT/'inventory/system-recovery-grunt-state-matrix.json').write_text(json.dumps(matrix,ensure_ascii=False,indent=2),encoding='utf-8')
    levels={}
    with (ROOT/'inventory/object-and-table-properties.csv').open(encoding='utf-8-sig',newline='') as f:
        for row in csv.DictReader(f):
            if not row['asset'].endswith('MainChar_HitBoxData.uasset') or '.m_Level[' not in row['property']: continue
            idx=int(row['property'].split('.m_Level[')[1].split(']')[0])
            levels.setdefault(row['export_or_row'],[0,0,0])[idx]=int(float(row['value']))
    def candidate(v,thresholds):
        for i,name in ((1,'Push'),(0,'KnockDown'),(2,'Dizzy')):
            if v[i]>thresholds[i]: return name
        return 'Hit'
    candidates=[]
    for row_name,v in levels.items():
        infight=candidate(v,(2,2,11)); dizzy=candidate(v,(0,0,1))
        if infight!=dizzy:
            candidates.append({'hitbox_row':row_name,'attack_levels':v,'InFight_candidate':infight,'Dizzy_candidate_before_top-dizzy_exception':dizzy,'threshold_comparison':'strict greater-than; priority KnockDown/Push/Dizzy per ComputeImpactType; special current-Dizzy gate may downgrade to Hit'})
    (ROOT/'inventory/system-recovery-hitbox-state-candidates.json').write_text(json.dumps(candidates,ensure_ascii=False,indent=2),encoding='utf-8')
    paths=[Path(x['file']) for x in report['procedures'] if x.get('file')]
    manifest={'exe_sha256':report['exe_sha256'],'matched_pdb':json.loads((ROOT/'inventory/pdb_overview.json').read_text(encoding='utf-8')).get('pdb_path'),'procedure_count':len(paths),'procedures':[{'file':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in paths], 'asset_evidence':['inventory/stun-state-data.json:hitted_assets[GruntHittedDB]','exports/state-resistance-matrices.csv:Grunt_Base/Adv rows','inventory/system-recovery-grunt-state-matrix.json','inventory/system-recovery-hitbox-state-candidates.json'],'limitations':['Static disassembly is not runtime validation.','FNetOrderStruct/state field offsets and enum values require matching PDB layout; raw offsets alone are not labels.','The two HittedDB policy flags have not yet been traced to their consuming merge/update branch.']}
    (ROOT/'inventory/system-recovery-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'disassemblies':len(paths),'grunt_asset':entry['asset'],'state_rows':len(matrix),'candidate_hitboxes':len(candidates),'manifest':'inventory/system-recovery-manifest.json'},ensure_ascii=False))
if __name__=='__main__': main()
