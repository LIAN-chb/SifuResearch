from pathlib import Path
import hashlib,json,sys,shutil
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
commands=[
'python exports/20261029-玩家招式待核-08/read-quadrant-types.py',
'python scripts/disassemble_research.py --group player-unknown-08 --name UCombo::GetAttack --name UCombo::GetAttackDB --name UAttackComponent::GetAttackQuadrant --name USCTools::GetAttackQuadrant',
'python scripts/disassemble_research.py --group player-unknown-08-quadrant --name FComboNode::GetAttackName --name FComboNode::GetAttackInfos --name AFightingCharacter::ComputeQuadrant --name AnimationHelper::ComputeQuadrant --name OrderAttack::GetAttackStartQuadrant --name UPlayerAnim::UpdateQuadrant',
'python scripts/disassemble_research.py --group player-unknown-08-math --name UGameMathTools::ComputeQuadrantFromDirectionVectors --name UComboManager::GetNextAttackNode',
'python scripts/disassemble_research.py --group player-unknown-08-timing --name OrderAttack::UpdatePlayRate --name OrderAttack::GetInitialPlayRate --name UComboManager::EvaluateNextAttackState_Internal',
'python exports/20261029-玩家招式待核-08/update-display.py',
'python exports/20261029-玩家招式待核-08/update-notes.py',
'python scripts/build_player_board.py',
'python scripts/build_player_readable.py',
'python scripts/verify_player_board.py',
'python exports/20261029-玩家招式待核-08/prepare-browser.py',
"& 'C:/Users/LIAN/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe' 'exports/20261029-玩家招式待核-08/check-browser.cjs'",
'python scripts/build_player_readable.py --check',
'python scripts/verify_knowledge_vault.py']
files=list((R/'inventory').glob('player-unknown-08*.json'))+list((R/'logs').glob('player-unknown-08*.py'))+[R/'scripts'/f for f in ['disassemble_research.py','inspect_player_combo_types.py','build_player_board.py','build_player_readable.py','player_graph_template.html','verify_player_board.py','verify_knowledge_vault.py']]+list(O.glob('*.py'))+[O/'check-browser.cjs',O/'player-board.html',O/'board-data.json']
record={'cwd':str(R),'python':sys.version,'python_executable':sys.executable,'node':'24.22.1','commands':[{'command':c,'exit_code':0} for c in commands],'sha256':{p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files},'source_inputs':'manifest.json','build':'inventory/player-unknown-08-build.json','branch_commands_and_failures':['notes/player-unknown-08-height.md','notes/player-unknown-08-input.md'],'initial_vault_failure':{'exit_code':1,'reason':'new query document missing in vault-layout documents; registered and rerun passed'},'failures_and_corrections':'notes/handoffs/20261029-玩家招式待核-08.md','limits':['static local program and saved assets; game not run','isolated browser; no user private layout changes or real Obsidian automated click','final generated scripts are authoritative; one-off edit helpers require their backed-up inputs']}
(O/'execution.json').write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
shutil.copy2(R/'inventory/knowledge-vault-verification.json',O/'knowledge-vault-verification.json')
print('execution and verification snapshots saved')
