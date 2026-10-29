# Kuroki-03：全部已解析动作资源

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

本页列出 7 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。

## 动作索引

| 动作资源 | 路径范围标签 | 动画行表 | 动画行名 | 保存帧率 | 期望前摇帧字段 | 已解析命中窗口数 | 已解析许可窗口数 |
|---|---|---|---|---|---|---|---|
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A001-Kuroki_TriStaff_attack_CircleDance_loop02\|A001 Kuroki_TriStaff_attack_CircleDance_loop02]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_CircleDance_Loop02 | 60 | 2 | 5 | 2 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A002-Kuroki_TriStaff_attack_CircleDance_loop03\|A002 Kuroki_TriStaff_attack_CircleDance_loop03]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_CircleDance_Loop03 | 60 | 3 | 7 | 2 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A003-Kuroki_TriStaff_attack_CircleDanceBuildUp\|A003 Kuroki_TriStaff_attack_CircleDanceBuildUp]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_CircleDance_Buildup | 60 | 30 | 2 | 1 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A004-Kuroki_TriStaff_attack_Disengage\|A004 Kuroki_TriStaff_attack_Disengage]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_Disengage | 59.9999962 | 17 | 3 | 2 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A005-Kuroki_TriStaff_attack_GroundAttack\|A005 Kuroki_TriStaff_attack_GroundAttack]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_GroundAttack | 59.9999962 | 43 | 2 | 2 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A006-Kuroki_TriStaff_attack_GroundAttackBlunt\|A006 Kuroki_TriStaff_attack_GroundAttackBlunt]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_GroundAttack | 59.9999962 | 43 | 1 | 2 |
| [[03配置/动作与时序/Kuroki-03-动作资源.md#A007-Kuroki_TriStaff_attack_PostDisengage\|A007 Kuroki_TriStaff_attack_PostDisengage]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Kuroki_AttacksDatatable-6c83c5\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable]] | Kuroki_TriStaff_attack_PostDisengage | 60 | 8 | 5 | 2 |


## A001-Kuroki_TriStaff_attack_CircleDance_loop02

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_loop02.uasset

导出对象：Kuroki_TriStaff_attack_CircleDance_Loop02

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_1 | Inclusive: 6 → Inclusive: 7 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_2 | Inclusive: 15 → Inclusive: 16 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_3 | Inclusive: 24 → Inclusive: 25 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 3 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_4 | Inclusive: 33 → Inclusive: 34 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 4 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_5 | Inclusive: 42 → Inclusive: 43 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 44 → Inclusive: 45 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |
| 1 | Inclusive: 45 → Inclusive: 45 | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_CircleDance_Loop02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Loop02.Kuroki_TriStaff_attack_CircleDance_Loop02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Loop02_TriStaff.Kuroki_TriStaff_attack_CircleDance_Loop02_TriStaff | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | -606.505859 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 忽略攻击范围限制[0] | m_Attack[0].m_bIgnoreRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 140 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | CircleDance_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 6 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 7 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | CircleDance_2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 15 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 16 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | CircleDance_3 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 24 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 25 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].RowName[0] | CircleDance_4 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 33 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][3].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].RowName[0] | CircleDance_5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 42 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 43 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][4].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 44 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 45 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 45 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 45 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A002-Kuroki_TriStaff_attack_CircleDance_loop03

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_loop03.uasset

导出对象：Kuroki_TriStaff_attack_CircleDance_Loop03

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_1 | Inclusive: 5 → Inclusive: 7 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Right | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_2 | Inclusive: 14 → Inclusive: 16 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_3 | Inclusive: 22 → Inclusive: 24 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 3 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_4 | Inclusive: 31 → Inclusive: 33 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 4 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_5 | Inclusive: 40 → Inclusive: 42 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 5 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_6 | Inclusive: 49 → Inclusive: 51 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 6 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_7 | Inclusive: 58 → Inclusive: 60 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 60 → Inclusive: 61 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |
| 1 | Inclusive: 61 → Inclusive: 61 | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_CircleDance_Loop03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Loop03.Kuroki_TriStaff_attack_CircleDance_Loop03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Loop03_TriStaff.Kuroki_TriStaff_attack_CircleDance_Loop03_TriStaff | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 3 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | -985.602905 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 忽略攻击范围限制[0] | m_Attack[0].m_bIgnoreRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 140 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | CircleDance_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 7 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceLong_HitDetection.Kuroki_CircleDanceLong_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Right | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | CircleDance_2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 14 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 16 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceLong_HitDetection.Kuroki_CircleDanceLong_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | CircleDance_3 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 22 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 24 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceLong_HitDetection.Kuroki_CircleDanceLong_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].RowName[0] | CircleDance_4 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 33 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][3].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceLong_HitDetection.Kuroki_CircleDanceLong_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].RowName[0] | CircleDance_5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 42 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][4].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][5].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][5].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][5].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][5].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][5].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][5].m_HitRow[0].RowName[0] | CircleDance_6 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][5].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][5].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 49 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][5].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][5].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 51 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][5].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceShort_HitDetection.Kuroki_CircleDanceShort_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][5].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][5].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][5].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][5].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][5].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][5].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][5].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][5] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][5].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][6].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][6].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][6].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][6].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][6].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][6].m_HitRow[0].RowName[0] | CircleDance_7 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][6].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][6].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 58 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][6].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][6].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][6].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceLong_HitDetection.Kuroki_CircleDanceLong_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][6].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][6].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][6].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][6].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][6].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][6].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][6].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][6] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][6].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A003-Kuroki_TriStaff_attack_CircleDanceBuildUp

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDanceBuildUp.uasset

导出对象：Kuroki_TriStaff_attack_CircleDanceBuildUp

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_1 | Inclusive: 30 → Inclusive: 32 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | CircleDance_2 | Inclusive: 38 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 41 → Inclusive: 42 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp_NoDefense.AI_Attacks_GenericFollowUp_NoDefense |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_CircleDance_Buildup | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Buildup.Kuroki_TriStaff_attack_CircleDance_Buildup | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/CircleDance/Kuroki_TriStaff_attack_CircleDance_Buildup_Tristaff.Kuroki_TriStaff_attack_CircleDance_Buildup_Tristaff | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | -1.16790771 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 忽略攻击范围限制[0] | m_Attack[0].m_bIgnoreRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 140 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | CircleDance_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 32 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceBuildUp_HitDetection.Kuroki_CircleDanceBuildUp_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | CircleDance_2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 38 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_CircleDanceCloseLeft_HitDetection.Kuroki_CircleDanceCloseLeft_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 41 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 42 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp_NoDefense.AI_Attacks_GenericFollowUp_NoDefense | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A004-Kuroki_TriStaff_attack_Disengage

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/Disengage/Kuroki_TriStaff_attack_Disengage.uasset

导出对象：Kuroki_TriStaff_attack_Disengage

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | BackstepSwipeBlade | Inclusive: 39 → Inclusive: 41 | EAttackTarget::Mid_1 | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | BackstepSwipeBlade | Inclusive: 56 → Inclusive: 58 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | BackstepSwipeBlade | Inclusive: 86 → Inclusive: 88 | EAttackTarget::Low | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 100 → Inclusive: 120 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp_NoDefense.AI_Attacks_GenericFollowUp_NoDefense |
| 1 | Inclusive: 120 → Inclusive: 158 | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_Disengage | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/Disengage/Kuroki_TriStaff_attack_Disengage.Kuroki_TriStaff_attack_Disengage | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/Disengage/Kuroki_TriStaff_attack_Disengage_Weapon.Kuroki_TriStaff_attack_Disengage_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 59.9999962 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 17 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 6.89840698 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 忽略攻击范围限制[0] | m_Attack[0].m_bIgnoreRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | BackstepSwipeBlade | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 39 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 41 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_DisengageHit1_HitDetection.Kuroki_DisengageHit1_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | BackstepSwipeBlade | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 56 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 58 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_DisengageHit2_HitDetection.Kuroki_DisengageHit2_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | BackstepSwipeBlade | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 86 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 88 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_DisengageHit3_HitDetection.Kuroki_DisengageHit3_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 120 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp_NoDefense.AI_Attacks_GenericFollowUp_NoDefense | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 120 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 158 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A005-Kuroki_TriStaff_attack_GroundAttack

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/GroundAttack/Kuroki_TriStaff_attack_GroundAttack.uasset

导出对象：Kuroki_TriStaff_attack_GroundAttack

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | DeathSpinBlade | Inclusive: 59 → Inclusive: 61 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-8,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotEasy.BP_HitboxCondition_DifficultyIsNotEasy_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | DeathSpinBlade_Easy | Inclusive: 59 → Inclusive: 61 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-7,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsEasy.BP_HitboxCondition_DifficultyIsEasy_C"},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 135 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 104 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_GroundAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/GroundAttack/Kuroki_TriStaff_attack_GroundAttack.Kuroki_TriStaff_attack_GroundAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/GroundAttack/Kuroki_TriStaff_attack_GroundAttack_Weapon.Kuroki_TriStaff_attack_GroundAttack_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 59.9999962 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 43 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 352.956299 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotEasy.BP_HitboxCondition_DifficultyIsNotEasy_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | DeathSpinBlade | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 59 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_GroundAttack_HitDetection.Kuroki_GroundAttack_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsEasy.BP_HitboxCondition_DifficultyIsEasy_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | DeathSpinBlade_Easy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 59 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_GroundAttack_HitDetection.Kuroki_GroundAttack_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 135 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A006-Kuroki_TriStaff_attack_GroundAttackBlunt

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/GroundAttack/Tuto/Kuroki_TriStaff_attack_GroundAttackBlunt.uasset

导出对象：Kuroki_TriStaff_attack_GroundAttackBlunt

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | DeathSpin | Inclusive: 59 → Inclusive: 61 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 135 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 104 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_GroundAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/GroundAttack/Kuroki_TriStaff_attack_GroundAttack.Kuroki_TriStaff_attack_GroundAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/GroundAttack/Kuroki_TriStaff_attack_GroundAttack_Weapon.Kuroki_TriStaff_attack_GroundAttack_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 59.9999962 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 43 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 352.956299 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | DeathSpin | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 59 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_GroundAttack_HitDetection.Kuroki_GroundAttack_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 135 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A007-Kuroki_TriStaff_attack_PostDisengage

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Attacks/TriStaff/SpecialMoves/PostDisengage/Kuroki_TriStaff_attack_PostDisengage.uasset

导出对象：Kuroki_TriStaff_attack_PostDisengage

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | Post-disengage_Hit1 | Inclusive: 16 → Inclusive: 18 | EAttackTarget::Low | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | Post-disengage_Hit1 | Inclusive: 21 → Inclusive: 23 | EAttackTarget::Low | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | Post-disengage_Hit2 | Inclusive: 53 → Inclusive: 55 | EAttackTarget::Mid_1 | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 3 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | Post-disengage_Hit2 | Inclusive: 63 → Inclusive: 65 | EAttackTarget::Mid_1 | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 4 | [[03配置/敌人攻击/Kuroki_HitBoxData-155ce2\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData]] | Post-disengage_Hit3 | Inclusive: 90 → Inclusive: 92 | EAttackTarget::Mid_1 | EAttackMovementType::Vertical | EAttackOrigin::Down | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Exclusive: 118 → Inclusive: 152 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |
| 1 | Inclusive: 152 → Inclusive: 170 | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_AttacksDatatable.Kuroki_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Kuroki_TriStaff_attack_PostDisengage | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/PostDisengage/Kuroki_TriStaff_attack_PostDisengage.Kuroki_TriStaff_attack_PostDisengage | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Kuroki/Attack/TriStaff/SpecialMoves/PostDisengage/Kuroki_TriStaff_attack_PostDisengage_Weapon.Kuroki_TriStaff_attack_PostDisengage_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 8 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 149.769592 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 忽略攻击范围限制[0] | m_Attack[0].m_bIgnoreRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Post-disengage_Hit1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 16 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 18 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_PostDisengageHit1_HitDetection.Kuroki_PostDisengageHit1_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | Post-disengage_Hit1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 21 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 23 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_PostDisengageHit1_HitDetection.Kuroki_PostDisengageHit1_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::Low | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | Post-disengage_Hit2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 53 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 55 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_PostDisengageHit2_HitDetection.Kuroki_PostDisengageHit2_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].RowName[0] | Post-disengage_Hit2 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 63 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 65 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][3].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_PostDisengageHit2Bis_HitDetection.Kuroki_PostDisengageHit2Bis_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_HitBoxData.Kuroki_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].RowName[0] | Post-disengage_Hit3 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 90 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 92 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][4].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/KurokiTristaffAndKunaiHitDetection/ComboHitboxes/Kuroki_PostDisengageHit3_HitDetection.Kuroki_PostDisengageHit3_HitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eOrigin[0] | EAttackOrigin::Down | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 118 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 152 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 152 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 170 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。
