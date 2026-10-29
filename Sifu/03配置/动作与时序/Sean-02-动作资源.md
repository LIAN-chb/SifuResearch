# Sean-02：全部已解析动作资源

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

本页列出 6 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。

## 动作索引

| 动作资源 | 路径范围标签 | 动画行表 | 动画行名 | 保存帧率 | 期望前摇帧字段 | 已解析命中窗口数 | 已解析许可窗口数 |
|---|---|---|---|---|---|---|---|
| [[03配置/动作与时序/Sean-02-动作资源.md#A001-Sean_attack_staff_TigerSwing_Burst\|A001 Sean_attack_staff_TigerSwing_Burst]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Tiger_Swing | 60 | 20 | 1 | 2 |
| [[03配置/动作与时序/Sean-02-动作资源.md#A002-Sean_attack_staff_Tornado\|A002 Sean_attack_staff_Tornado]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Tornado | 60 | 25 | 5 | 2 |
| [[03配置/动作与时序/Sean-02-动作资源.md#A003-Sean_attack_staff_Tornado_Burst\|A003 Sean_attack_staff_Tornado_Burst]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Tornado | 60 | 16 | 4 | 2 |
| [[03配置/动作与时序/Sean-02-动作资源.md#A004-Sean_attack_staff_Waterfall\|A004 Sean_attack_staff_Waterfall]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Waterfall | 60.0000038 | 33 | 1 | 2 |
| [[03配置/动作与时序/Sean-02-动作资源.md#A005-Sean_attack_staff_Waterfall_Burst\|A005 Sean_attack_staff_Waterfall_Burst]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Waterfall | 60.0000038 | 29 | 2 | 2 |
| [[03配置/动作与时序/Sean-02-动作资源.md#A006-Sean_attack_staff_Waterfall_Burst_Combo\|A006 Sean_attack_staff_Waterfall_Burst_Combo]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/Sean_AttacksDatatable-63620e\|/Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable]] | Sean_attack_staff_Waterfall_Combo | 60.0000038 | 29 | 2 | 2 |


## A001-Sean_attack_staff_TigerSwing_Burst

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/TigerSwing/Sean_attack_staff_TigerSwing_Burst.uasset

导出对象：Sean_attack_staff_TigerSwing_Burst

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | TigerSwing_Burst_StaffAttack | Inclusive: 27 → Inclusive: 32 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 60 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 34 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Tiger_Swing | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/TigerSwing/Sean_attacks_staff_TigerSwing.Sean_attacks_staff_TigerSwing | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/TigerSwing/Sean_attacks_staff_TigerSwing_Weapon.Sean_attacks_staff_TigerSwing_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 300 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | TigerSwing_Burst_StaffAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 27 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 32 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A002-Sean_attack_staff_Tornado

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/Tornado/Sean_attack_staff_Tornado.uasset

导出对象：Sean_attack_staff_Tornado

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_01 | Inclusive: 34 → Inclusive: 37 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Right | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_02 | Inclusive: 63 → Inclusive: 68 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_03 | Inclusive: 101 → Inclusive: 104 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":-10,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNormal.BP_HitboxCondition_DifficultyIsNormal_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 3 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_03_Hard | Inclusive: 101 → Inclusive: 104 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":-9,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 4 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_03_Easy | Inclusive: 101 → Inclusive: 104 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":-8,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsEasy.BP_HitboxCondition_DifficultyIsEasy_C"},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 166 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 120 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Tornado | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/Tornado/Sean_attacks_staff_Tornado.Sean_attacks_staff_Tornado | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/Tornado/Sean_attacks_staff_Tornado_Weapon.Sean_attacks_staff_Tornado_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 25 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 400 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Tornado_StaffAttack_01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
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
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | Tornado_StaffAttack_02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 63 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 68 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNormal.BP_HitboxCondition_DifficultyIsNormal_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | Tornado_StaffAttack_03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 101 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].RowName[0] | Tornado_StaffAttack_03_Hard | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 101 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][3].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsEasy.BP_HitboxCondition_DifficultyIsEasy_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][4].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][4].m_HitRow[0].RowName[0] | Tornado_StaffAttack_03_Easy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 101 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][4].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][4].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][4].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][4] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][4].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 166 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 120 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 32 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 36 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][0].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][0].m_eAvoidType[0] | EAvoidType::Duck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][0].m_AvoidPropertyDB[0] | /Game/DB/Avoid/AvoidPropertyDB/SpecialAbility/SpecialDuck.SpecialDuck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 68 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][1].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][1].m_eAvoidType[0] | EAvoidType::Duck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][1].m_AvoidPropertyDB[0] | /Game/DB/Avoid/AvoidPropertyDB/SpecialAbility/SpecialDuck.SpecialDuck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 99 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][2].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][2].m_eAvoidType[0] | EAvoidType::None | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][2].m_AvoidPropertyDB[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Specific.SeanBraseroHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A003-Sean_attack_staff_Tornado_Burst

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/Tornado/Sean_attack_staff_Tornado_Burst.uasset

导出对象：Sean_attack_staff_Tornado_Burst

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_01_Burst | Inclusive: 34 → Inclusive: 37 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Right | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_02_Burst | Inclusive: 63 → Inclusive: 68 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_03_Burst | Inclusive: 101 → Inclusive: 104 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":-9,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 3 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Tornado_StaffAttack_03_Burst_Hard | Inclusive: 101 → Inclusive: 104 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":-8,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 160 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 133 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Tornado | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/Tornado/Sean_attacks_staff_Tornado.Sean_attacks_staff_Tornado | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/Tornado/Sean_attacks_staff_Tornado_Weapon.Sean_attacks_staff_Tornado_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 16 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 400 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Tornado_StaffAttack_01_Burst | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
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
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | Tornado_StaffAttack_02_Burst | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 63 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 68 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | Tornado_StaffAttack_03_Burst | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 101 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][3].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][3].m_HitRow[0].RowName[0] | Tornado_StaffAttack_03_Burst_Hard | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 101 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][3].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 104 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][3].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][3].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eMovementType[0] | EAttackMovementType::Horizontal | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][3] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][3].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 160 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 133 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 32 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 36 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][0].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][0].m_eAvoidType[0] | EAvoidType::Duck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][0] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][0].m_AvoidPropertyDB[0] | /Game/DB/Avoid/AvoidPropertyDB/SpecialAbility/SpecialDuck.SpecialDuck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 59 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 66 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][1].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][1].m_eAvoidType[0] | EAvoidType::Duck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][1] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][1].m_AvoidPropertyDB[0] | /Game/DB/Avoid/AvoidPropertyDB/SpecialAbility/SpecialDuck.SpecialDuck | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 97 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvoidWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 102 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_iAvoidID）[0] | m_Attack[0].m_AvoidWindows[0][2].m_iAvoidID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_eAvoidType）[0] | m_Attack[0].m_AvoidWindows[0][2].m_eAvoidType[0] | EAvoidType::None | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 未核中文义（m_AvoidWindows）[0][2] → 未核中文义（m_AvoidPropertyDB）[0] | m_Attack[0].m_AvoidWindows[0][2].m_AvoidPropertyDB[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Specific.SeanBraseroHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A004-Sean_attack_staff_Waterfall

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/WaterFall/Sean_attack_staff_Waterfall.uasset

导出对象：Sean_attack_staff_Waterfall

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Waterfall_StaffAttack | Inclusive: 34 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 61 → 无界（保存值 0 不作端点） | 25 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 45 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Waterfall | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall.Sean_attacks_staff_Waterfall | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall_Weapon.Sean_attacks_staff_Waterfall_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60.0000038 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666657 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 33 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 300 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Waterfall_StaffAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 25 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 61 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 45 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Specific.SeanBraseroHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A005-Sean_attack_staff_Waterfall_Burst

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/WaterFall/Sean_attack_staff_Waterfall_Burst.uasset

导出对象：Sean_attack_staff_Waterfall_Burst

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Waterfall_Burst_StaffAttack | Inclusive: 34 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-8,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Waterfall_Burst_StaffAttack_Hard | Inclusive: 34 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-7,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 90 → 无界（保存值 0 不作端点） | 25 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 60 → 无界（保存值 0 不作端点） | 22 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Waterfall | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall.Sean_attacks_staff_Waterfall | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall_Weapon.Sean_attacks_staff_Waterfall_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60.0000038 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666657 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 29 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 300 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Waterfall_Burst_StaffAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | Waterfall_Burst_StaffAttack_Hard | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 25 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 90 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 22 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Specific.SeanBraseroHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A006-Sean_attack_staff_Waterfall_Burst_Combo

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Attacks/StaffAttacks/WaterFall/Sean_attack_staff_Waterfall_Burst_Combo.uasset

导出对象：Sean_attack_staff_Waterfall_Burst_Combo

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Waterfall_Burst_StaffAttack | Inclusive: 34 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-8,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/敌人攻击/Sean_HitBoxData-5539e6\|/Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData]] | Waterfall_Burst_StaffAttack_Hard | Inclusive: 34 → Inclusive: 40 | EAttackTarget::High | EAttackMovementType::Vertical | EAttackOrigin::Up | {"m_DefaultClassObject[0]":{"index":-7,"reference":"/Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C"},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 90 → 无界（保存值 0 不作端点） | 25 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 60 → 无界（保存值 0 不作端点） | 22 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Attacks/Sean_AttacksDatatable.Sean_AttacksDatatable | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | Sean_attack_staff_Waterfall_Combo | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall_Combo.Sean_attacks_staff_Waterfall_Combo | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 关联武器动画信息[0] → 关联武器动画[0] | m_Attack[0].m_weaponAnimInfoAssociated[0].m_weaponAnimAssociated[0] | /Game/Animations/Sean/Attacks/Staff/Waterfall/Sean_attacks_staff_Waterfall_Combo_Weapon.Sean_attacks_staff_Waterfall_Combo_Weapon | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60.0000038 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666657 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 29 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 350 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsNotHard.BP_HitboxCondition_DifficultyIsNotHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | Waterfall_Burst_StaffAttack | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/_Shared/Conditions/BP_HitboxCondition_DifficultyIsHard.BP_HitboxCondition_DifficultyIsHard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/Sean/Sean_HitBoxData.Sean_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | Waterfall_Burst_StaffAttack_Hard | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/SeanStaffHitDetection/SeanTwoHandedWeaponAll.SeanTwoHandedWeaponAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Vertical | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Up | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 25 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 90 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 22 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Specific.SeanBraseroHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。
