from pathlib import Path
R=Path(__file__).resolve().parents[2]
s=(R/'scripts/inspect_player_combo_types.py').read_text(encoding='utf-8')
s=s.replace("out=ROOT/'inventory'/'player-combo-type-layouts.json'", "out=ROOT/'inventory'/'player-unknown-08-input-types.json'")
s=s.replace("if __name__=='__main__': main()", "")
scope={'__name__':'input_types_helper'}
exec(compile(s,'scripts/inspect_player_combo_types.py','exec'),scope)
scope['TARGET_NAMES']={'InputAction','InputBehavior','FInputBehaviourStruct','InputCondition','UInputData','UCombinationInputData','FCombinationInput','UInputSequenceData','FInputSequenceStep','FConditionalAttack','FComboNode'}
scope['RELEVANT']=__import__('re').compile('(?!)')
scope['main']()
