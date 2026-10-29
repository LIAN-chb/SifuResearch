from pathlib import Path
import json,hashlib,sys
R=Path(__file__).resolve().parents[2];O=Path(__file__).resolve().parent
cdos=json.loads((O/'actions-ability-cdos.json').read_text(encoding='utf-8'));by={c['asset'].split('/')[-1]:c for c in cdos}
ui=json.loads((R/'exports/20261029-玩家招式名称-12/skill-ui-links.json').read_text(encoding='utf-8'))['skills']
locale=json.loads((R/'exports/20261029-玩家招式名称-12/paired-texts.json').read_text(encoding='utf-8'))
def skill(suffix):
 s=next((s for s in ui if s['asset'].endswith(suffix) or s['fields'].get('Name',{}).get('key')==suffix),None)
 if s:return {'asset':s['asset'],'fields':s['fields'],'source_sha256':s['uasset_sha256'],'binding':'same SkillUI export'}
 title=next(r for r in locale if r['namespace']=='SkillTree' and r['key']==suffix);fields={'Name':title}
 for k,label in [('SkillInput_','Inputs'),('SkillDesc_','Description')]:
  entry=next((r for r in locale if r['namespace']=='SkillTree' and r['key']==suffix.replace('SkillTitle_',k)),None)
  if entry:fields[label]=entry
 return {'asset':None,'fields':fields,'binding':'locale entries only; matching SkillUI object not recovered'}
def record(key,op,name,ability,input_names,why,skill_suffix=None):
 c=by[ability];entries=[e for e in c['properties']['m_Inputs[0]'] if e['m_eInput[0]'] in input_names];assert len(entries)==len(input_names)
 return {'key':key,'operationLabel':op,'officialNames':[name] if name else [],'kind':'ability-entry','sourceAsset':c['asset'],'sourceObject':c['object'],'source_sha256':c['source_sha256'],'uexp_sha256':c['uexp_sha256'],'inputEntries':entries,'abilityProperties':c['properties'],'skillUI':skill(skill_suffix) if skill_suffix else None,'entry':why,'attackAssets':[],'edges':[],'canAddAsSupplementaryNode':True,'limits':['独立Ability输入入口，不属于原ComboTree保存边','上游角色能力注册及具体运行期可用性本批未追通','没有把MC_GRAB等同名树外AttackDB自动绑定为此动作','无单独Damage/Structure表行证据，不填0或套普通攻击数值']}
nodes=[record('directional-throw','抓取后推掷','抛掷','BP_PushAbility.uasset',['InputAction::PushFromGrab'],'抓取/可推掷状态→PushFromGrab；技能UI输入同为PushFromGrab','SkillTitle_Action_ThrowCharacter'),]
nodes.append(record('downed-target-attack','攻击倒地对手',None,'BP_KnockdownAttackAbility.uasset',['InputAction::AttackKnockdown','InputAction::AttackKnockdownHold'],'对手倒地且可作KnockdownAttack目标；短按/长按两入口保留，CDO有轻/重双方动画'))
nodes.append(record('ground-parry-counter','倒地格挡反击','扭转乾坤','BP_ParryFromDownAbility.uasset',['InputAction::ParryFromDown'],'玩家倒地时格挡输入；技能UI同为ParryFromDown，区别于现有起身攻击','SkillTitle_Action_DownCounter'))
out={'supplementaryNodes':nodes,'alreadyCovered':[{'label':'斗转星移','sourceNode':55,'reason':'MainChar_ComboTree默认DodgeAttack已接55，引用MC_Skill_InvertPosition_connect_FR；无需重复补一个同输入节点','skillUI':skill('SkillTitle_Technique_InvertPosition')},{'label':'起身攻击','sourceNode':0,'reason':'保存树已有KnockedDown情境入口及North/South配置；不同于攻击倒地敌人或倒地招架反击'}],'unboundTreeExternalCandidates':['Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/Grab/MC_GRAB_FL.uasset','Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/Grab/MC_GRAB_BL.uasset'],'rootIntegration':'Supplementary entry nodes may be shown in the map with ability source badge; do not invent ordinary combo edges. Attribute sections should state synchronized action/config not recovered rather than use zeros.','python':sys.version,'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(O/'actions-data.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'supplementary_nodes':len(nodes),'existing_nodes_not_duplicated':len(out['alreadyCovered'])},ensure_ascii=True))
