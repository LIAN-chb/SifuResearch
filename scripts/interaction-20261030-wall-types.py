from pathlib import Path
import hashlib,json,sys
R=Path(r'E:/ProgrameFiles/SifuResearch')
s=(R/'scripts/inspect_types.py').read_text()
s=s.replace("TARGET_NAMES = {", "TARGET_NAMES = {'UAttackPropertiesResistanceDB','FPushPropertyReaction','FPropertyReaction','FKnockedDownReaction','FKnockDownReaction','FHandleLDCollisionOrderServiceInstance','UHandleLDCollisionOrderService','FBaseOrderServiceInstance','FHitRequest','FApplyImpactStruct','UHitComponent','OrderPushed',")
s=s.replace('if ((attrs >> 2) & 0x7) == 4: q,_=cvnum(data,q)', 'if ((attrs >> 2) & 0x7) in (4,6): q+=4')
s=s.replace("ROOT/'inventory'/'focused_type_layouts.json'","ROOT/'inventory'/'interaction-20261030-wall-types.json'")
exec(compile(s,'adapted-inspect-types','exec'),{'__name__':'__main__'})

# Keep only layouts needed by this branch, while preserving the original reader limits.
import json
p=R/'inventory/interaction-20261030-wall-types.json'
d=json.loads(p.read_text(encoding='utf-8'))
wanted={'UAttackPropertiesResistanceDB','FPushPropertyReaction','FPropertyReaction','FHandleLDCollisionOrderServiceInstance','UHandleLDCollisionOrderService','FBaseOrderServiceInstance','FHitRequest','FApplyImpactStruct','OrderPushed'}
d['layouts']=[x for x in d['layouts'] if x['name'] in wanted]
d['target_names_found']=sorted(wanted & set(d['target_names_found']))
d['target_names_missing']=sorted(wanted-set(d['target_names_found']))
p.write_text(json.dumps(d,ensure_ascii=False,indent=2),encoding='utf-8')
