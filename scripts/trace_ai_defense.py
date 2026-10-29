"""Reproduce the selected static AI-defense disassemblies using the shared verified helper."""
import sys
from pathlib import Path
ROOT = Path(r'E:\ProgrameFiles\SifuResearch')
sys.path.insert(0, str(ROOT/'scripts'))
sys.dont_write_bytecode = True
from disassemble_research import disassemble

NAMES = [
 'FAIDefenseHandler::Initialize', 'FAIDefenseHandler::IsDefenseNeededInternal',
 'FAIDefenseHandler::ComputeDefenseRequest', 'FAIDefenseHandler::CanApplyDefenseRequest',
 'FAIDefenseHandler::ApplyDefenseRequest', 'FAIDefenseHandler::UpdateDefenseNeed',
 'FAIDefenseHandler::OnDefenseFilteredImpact', 'FAIDefenseHandler::OnDefenseFinished',
 'FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero', 'FAIDefenseHandler::OnTargetAttackEnded',
 'FAIDefenseHandler::ResetTargetAttackInfos', 'UAttackMemoryInfluenceTest::RunTest',
 'UAIFightingComponent::AddReccordedGameplayStateToMemory', 'UAIFightingComponent::UpdateAttackReceivedMemory',
 'UAIFightingComponent::GetFullMemoryOfType', 'UAIFightingComponent::GetHitCountFromMemory',
 'UAIFightingComponent::GetDamageFromMemory', 'UAIFightingComponent::GetDamageRatioFromMemory',
 'UAIFightingComponent::UpdateMemoryUnitForDodgeOrAvoidSuccess', 'UAIFightingComponent::UpdateMemoryUnitForTargetDodgeOrAvoidSuccess',
 'UAIFightingComponent::OnIsStunChanged', 'UAIFightingComponent::TickComponent', 'FAIAttackHandler::OnIsStunChanged',
 'TestNodeForContextualDefense', 'InternalConstructor<UAttackMemoryInfluenceTest>', 'UAIInfluence_TestSequence::RunTests',
 'UDefenseInfluenceNodeGuard::OnIsStunFinished',
 'UDefenseInfluenceNodeGuard::OnTargetAttackEnded', 'UDefenseInfluenceNodeGuard::Apply',
 'UDefenseInfluenceNodeParryDeflect::Apply', 'UDefenseInfluenceNodeParryDeflect::OnNonDismissedHit',
 'UDefenseInfluenceNodeParryDeflect::OnTargetAttackEnded', 'AIMainMemory::GetFullMemoryOfType',
 'AIMainMemory::RegisterMemoryUnit', 'AIMainMemory::UpdateLastMemoryUnitWithPredicate',
 'AIMainMemory::UpdateMemory', 'AIMainMemory::UpdateMemoryWithPredicate',
 'AIMainMemory::GetMemoriesOfType<TInlineAllocator<32,TSizedDefaultAllocator<32> > >',
 'UDefenseInfluenceNodeDodge::Prepare',
 'UDefenseInfluenceNodeDodge::OnNonDismissedHit', 'UAIContextualDefense::PickContextualDefense',
]
if __name__ == '__main__':
    disassemble(NAMES, 'stun-ai-defense')





