from pathlib import Path
import re
R=Path(__file__).resolve().parents[2]
s=(R/'scripts/inspect_player_combo_types.py').read_text(encoding='utf-8')
s=s.replace("'player-combo-type-layouts.json'","'player-unknown-08-quadrant-types.json'")
s=s.replace("if __name__=='__main__': main()", "TARGET_NAMES={'EQuadrantTypes','FComboNode','FComboNodeAttackInfos','FChargedAttackNameByQuadrants','FChargedBuildUpStructByQuadrant','FComboAttack','FAttackData','UAttackComponent','OrderAttack','FConditionalAttack','FConditionalAttackInfos'}\nRELEVANT=re.compile(r'^$')\nmain()")
exec(compile(s,str(R/'scripts/inspect_player_combo_types.py'),'exec'))
