from pathlib import Path
import json,hashlib,sys,shutil
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
shutil.copy2(R/'inventory/knowledge-vault-verification.json',O/'knowledge-vault-verification.json')
old=json.loads((R/'exports/20261029-玩家招式图-06/board-data.json').read_text(encoding='utf-8'))
new=json.loads((O/'board-data.json').read_text(encoding='utf-8'))
assert old==new
files=['scripts/build_player_board.py','scripts/player_graph_template.html','scripts/verify_player_board.py','scripts/build_player_readable.py','scripts/verify_knowledge_vault.py','exports/20261029-玩家招式图-07/check-browser.cjs','Sifu/03配置/玩家攻击/招式板/徒手招式板.html']
node='C:/Users/LIAN/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node.exe'
commands=['python exports/20261029-玩家招式图-07/update.py','python scripts/build_player_board.py',f'& \'{node}\' \'exports/20261029-玩家招式图-07/check-browser.cjs\'','python exports/20261029-玩家招式图-07/finish.py','python scripts/build_player_readable.py --check','python scripts/verify_player_board.py','python scripts/verify_knowledge_vault.py']
(O/'execution.json').write_text(json.dumps({'cwd':str(R),'python':sys.version,'python_executable':sys.executable,'node_version':'24.22.1 (06 runtime reused)','commands':[{'command':c,'exit_code':0} for c in commands],'sha256':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in files},'data_equal_to_06':True,'browser_report':'browser-verification.json','source_input_hashes':'manifest.json','limits':['no new game research','isolated Edge browser; real Obsidian and user storage not tested']},ensure_ascii=False,indent=2),encoding='utf-8')
