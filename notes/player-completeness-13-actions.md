# 徒手补全13：独立动作入口与徒手专注

本分支只研究并输出独立数据，未改共享图脚本、模板、进度或Git暂存。静态配置与文本引用，不是游戏实测；没有执行新解包或反汇编。交接由主批notes/handoffs/20261029-徒手补全与命名-13.md维护。

## A01：三项独立Ability入口可以补到图中

读取已有package-metadata和原始uasset/uexp，按export serialOffset减uasset文件大小定位CDO。先核uasset SHA与元数据，再用local_bounded_packages.tags读属性；对m_Inputs StructProperty数组核count、内层header长度、每元素终止和末尾精确消费。五个选中CDO均完全消费，没有尾余。原始字段与源SHA见13/actions-ability-cdos.json，简明建议见actions-data.json。

| 建议显示动作 | 保存入口 | 作用主体与对象 | 已定位来源与边界 |
|---|---|---|---|
| 抓取后推掷；官方名抛掷 | BP_PushAbility CDO m_Inputs=InputAction::PushFromGrab，target=PushVictim，requiresTarget=true | 玩家作为推掷方，对可推掷敌人使用该动作 | CDO引用m_PushConfiguration到同包BP_PushConfiguration_C_0；SkillTree的Action_ThrowCharacter名称为抛掷，输入文本同为PushFromGrab。该名称未匹配到现有SkillUI导出，JSON标明仅本地化条目对应，不能说已追到同一UI对象。 |
| 攻击倒地对手（无独立官方名证据） | BP_KnockdownAttackAbility CDO m_Inputs含AttackKnockdown和AttackKnockdownHold，target=KnockdownAttack | 玩家仍站立或可攻击状态，攻击已倒地敌人 | CDO保存普通与重型施放者／受击者两组OTG动画。区别于图已有“玩家起身攻击”；两输入保留在一个动作节点的不同配置中。 |
| 倒地格挡反击；官方名扭转乾坤 | BP_ParryFromDownAbility CDO m_Inputs=ParryFromDown | 玩家自己倒地时，对敌方来袭做反击 | ActivationRequiredTags确为Skills.Actions.OTGParryCounter；12技能UI的Name/Inputs同对象为扭转乾坤/ParryFromDown。m_bLaunchDownRecovery=false只按字段保留，不推实际恢复流程。 |

这三项独立Ability入口不在原ComboTree的默认有效攻击节点中，不应为它们伪造普通连段边。入口CDO字段足以支持将它们作为“独立动作入口”显示；玩家具体能力注册、可推掷条件消费者及运行期目标资格本分支未接通。可读属性应说明同步动作／效果字段未恢复，不能填伤害0或套普通拳脚表行。

玩家执行后两项时，CDO m_AvailabilityLayersWhileActive均引用GenericNone，该字段归属于玩家当前Ability激活期间，不是敌人倒地或受击后禁止行动的证据。

## A02：不要重复补的既有动作

图中node55已有默认DodgeAttack，引用MC_Skill_InvertPosition_connect_FR；技能UI明确官方名斗转星移和对被击中敌人使用DodgeAttack。它属于现有节点补名，不要再做第二个“斗转星移”节点。node0的North/South配置是玩家自己的起身攻击，已经有KnockedDown情境入口；不能和“攻击倒地敌人”合并。

MC_GRAB_FL/BL两份树外AttackDB未找到本分支可证明的BP_PushAbility引用，保持unboundTreeExternalCandidates，不凭Grab资源名将其绑定到抛掷。PushConfiguration的PushEnvCloseHitbox是特定环境推掷配置，不能当普通抛掷统一伤害。其他六个常规树外候选亦不可仅因存在AttackDB就新增普通边。

## F01：徒手专注有五个共享弱点配置

来源是Sifu/Content/DB/AI/_Shared/Focus下VitalPointData，不是普通AttackDB。每项m_Name为FText History11/StringTableEntry；本分支按原字段SHA、FName表与FString key精确消费，并在官方en/zh-Hans本地化中核同namespace/key/source hash。名称直接来自FocusNames，不借旧技能UI推定。

| 显示名 | 英文名 | VitalPointData资产尾部 | 保存消耗 | 命中表行 |
|---|---|---|---|---|
| 戳眼 | Eye Strike | Damage/VitalPointDataTemple | 1 | Throat_HB01 |
| 中线连打 | Vertical Strikes | Dizzy/VitalPointDataBelly | 2 | Dizzy_HB02 |
| 扫堂腿 | Strong Sweep | Down/VitalPointDataKnee | 1 | Knee_HB01 |
| 双冲掌 | Double Palm | Pushback/VitalPointDataPlexus | 2 | Pushback_HB01 |
| 嘲讽 | Calbot | Taunt/VitalPointDataTaunt | 1 | Taunt |

各资产.m_SyncAnimToPlay直接分别引用玩家施放者动画与敌方受击者动画；m_FocusAttackEffect.m_HitBox.m_HitRow引用同一Shared/Focus/VitalPoint_HitBoxData表的各行。附加抵抗DB、敌人循环／致死受击动画、条件蓝图与parent字段保留，不把它们当玩家普通连段。全部属性和准确源SHA、uexp名字偏移在13/focus-data.json，root可直接将其作为独立页面节点数据。

专注消耗只标保存配置；敌人的VitalPointData可有变体覆写，例如FireDisciple有自己的Belly配置。当前共享值不能当每个敌人的最终表现。FocusNames/Temple的戳眼确为正式文本，不能拿12批InitialSkills/SkillGameplay_Focus_AttackDamage中旧UI“解除武器专注攻击”当当前戳眼的名称。

## F02：专注衔接没有形成可画普通实线的证据

现有MainChar_ComboTree的21类默认输入和63保存边不含Focus模式／执行入口；本分支识别的五个专注来自VitalPointData同步动作链。BP_FocusAbility_C继承SCGameplayAbility，CDO保存PrepFocusHold输入和ActivationRequiredTags=Skills.Focus；其包imports包括StartFocus/StopFocus/ValidateFocus等接口，但imports只证明引用，不是执行路径闭合。

因此focus-data.json的edges为空，followupStatus明确“本保存ComboTree中无对应边，专注结束后的动作许可／跟进路径未恢复”。这不表示实战专注后不能接招。若要画专注接普通招式的线，下一步须恢复BP_FocusAbility执行／结束分支、同步攻击订单结束及玩家动作许可层的启停，并核目标敌人专注造成的受击状态，之后才谈可接窗口。

## 执行与验证

命令：python exports/20261029-徒手补全与命名-13/actions-focus-research.py；actions-recommend.py；actions-verify.py。均最终退出0，Python、工具与输入SHA见actions-verification.json。14项通过，覆盖五项专注的实际名字／源文件／命中表行、5 CDO完全消费、3入口分类、技能tag、两类倒地敌人攻击输入和脚本语法。只核本分支数据，不包含图渲染或用户布局验证。

失败与修正：首轮抛掷名称查找假设存在对应SkillUI导出而StopIteration；实查无匹配后改记录明确的本地化条目对应，不伪造对象链。root首轮生成页面时与focus-data.json源文件命名冲突，覆盖为视图数据，验证报缺edges；协调将生成视图改名focus-board-data.json，随后重跑本分支源脚本恢复5源节点，14项检查通过。没有覆盖旧批次证据。

写入结束。可用JSON为actions-data.json和focus-data.json；原始CDO及读取源码单独保存。后续页面生成不应写回上述源JSON。
