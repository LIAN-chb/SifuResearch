from pathlib import Path
root=Path.cwd()
code=(root/'scripts/inspect_types.py').read_text()
code=code.replace("TARGET_NAMES = {", "TARGET_NAMES = {'AnimationHelperParams','OrderAttack','UPlayerAnim','EAttackStates','FAnimContainer','TRange<float>','TRangeBound<float>',")
code=code.replace("out=ROOT/'inventory'/'focused_type_layouts.json'", "out=ROOT/'exports/20261030-前摇语义-16/hitclock-types.json'")
ns={'__name__':'adapted'};exec(compile(code,'scripts/inspect_types.py','exec'),ns); ns['main']()
