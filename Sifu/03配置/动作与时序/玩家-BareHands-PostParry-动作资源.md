# 玩家-BareHands-PostParry：全部已解析动作资源

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

本页列出 4 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。

## 动作索引

| 动作资源 | 路径范围标签 | 动画行表 | 动画行名 | 保存帧率 | 期望前摇帧字段 | 已解析命中窗口数 | 已解析许可窗口数 |
|---|---|---|---|---|---|---|---|
| [[03配置/动作与时序/玩家-BareHands-PostParry-动作资源.md#A001-MC_3Punches_02_FL\|A001 MC_3Punches_02_FL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Attacks-4293b7\|/Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks]] | MC_TripleHit_02 | 60 | 11 | 3 | 3 |
| [[03配置/动作与时序/玩家-BareHands-PostParry-动作资源.md#A002-MC_3Punches_03_FL\|A002 MC_3Punches_03_FL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Attacks-4293b7\|/Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks]] | MC_TripleHit_03 | 60 | 10 | 3 | 3 |
| [[03配置/动作与时序/玩家-BareHands-PostParry-动作资源.md#A003-MC_3Punches_FR\|A003 MC_3Punches_FR]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Attacks-4293b7\|/Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks]] | MC_TripleHit | 59.9999962 | 5 | 3 | 3 |
| [[03配置/动作与时序/玩家-BareHands-PostParry-动作资源.md#A004-MainChar_CrookedFoot_Thrust_FR\|A004 MainChar_CrookedFoot_Thrust_FR]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Attacks-4293b7\|/Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks]] | PunishKD_CrookedFoot_Thrust | 60 | 8 | 1 | 2 |


## A001-MC_3Punches_02_FL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/PostParry/PostParry_Dizzy/MC_3Punches_02_FL.uasset

导出对象：MC_3Punches_02_FL

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_02_HB01 | Exclusive: 12 → Inclusive: 14 | EAttackTarget::Mid_1 | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_02_HB02 | Exclusive: 18 → Inclusive: 20 | EAttackTarget::High | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_02_HB03 | Exclusive: 26 → Exclusive: 29 | EAttackTarget::High | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 34 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp |
| 1 | Inclusive: 40 → Inclusive: 80 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt |
| 2 | Inclusive: 80 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_TripleHit_02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Attacks/Man/Barehands/PostParry/PostParry_Dizzy/MainChar_Attack_Man_Barehands_FollowUp_TripleHit_02_FL.MainChar_Attack_Man_Barehands_FollowUp_TripleHit_02_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 90 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 200 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | 3Punches_02_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 12 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 14 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | 3Punches_02_HB02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 18 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/RightArmHitDetection.RightArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | 3Punches_02_HB03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 26 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 29 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 80 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 80 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Speed.Fast | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][1] | m_Attack[0].m_AttackProperties[0][1] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][2] | m_Attack[0].m_AttackProperties[0][2] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][3] | m_Attack[0].m_AttackProperties[0][3] | Attack.HitProperties.Stun | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A002-MC_3Punches_03_FL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/PostParry/PostParry_Dizzy/MC_3Punches_03_FL.uasset

导出对象：MC_3Punches_03_FL

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_03_HB01 | Exclusive: 11 → Inclusive: 13 | EAttackTarget::High | EAttackMovementType::Horizontal | EAttackOrigin::Right | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_03_HB02 | Exclusive: 17 → Inclusive: 19 | EAttackTarget::High | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_03_HB03 | Exclusive: 31 → Exclusive: 34 | EAttackTarget::Mid_1 | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 37 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp |
| 1 | Inclusive: 42 → Inclusive: 82 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt |
| 2 | Inclusive: 81 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_TripleHit_03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Attacks/Man/Barehands/PostParry/PostParry_Dizzy/MainChar_Attack_Man_Barehands_FollowUp_TripleHit_03_FL.MainChar_Attack_Man_Barehands_FollowUp_TripleHit_03_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 10 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 95 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 200 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | 3Punches_03_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 13 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
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
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | 3Punches_03_HB02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 17 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 19 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/RightArmHitDetection.RightArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | 3Punches_03_HB03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 34 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 42 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 82 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 81 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Speed.Fast | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][1] | m_Attack[0].m_AttackProperties[0][1] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][2] | m_Attack[0].m_AttackProperties[0][2] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][3] | m_Attack[0].m_AttackProperties[0][3] | Attack.HitProperties.Stun | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A003-MC_3Punches_FR

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/PostParry/PostParry_Dizzy/MC_3Punches_FR.uasset

导出对象：MC_3Punches_FR

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_HB01 | Exclusive: 5 → Inclusive: 8 | EAttackTarget::High | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 1 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_HB02 | Exclusive: 11 → Inclusive: 15 | EAttackTarget::High | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |
| 2 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | 3Punches_HB03 | Exclusive: 19 → Exclusive: 24 | EAttackTarget::Mid_1 | EAttackMovementType::Thrust | EAttackOrigin::Middle | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 31 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp |
| 1 | Inclusive: 41 → Inclusive: 81 | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt |
| 2 | Inclusive: 81 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_TripleHit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Attacks/Man/Barehands/PostParry/PostParry_Dizzy/MainChar_Attack_Man_Barehands_FollowUp_TripleHit_FL.MainChar_Attack_Man_Barehands_FollowUp_TripleHit_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 59.9999962 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 200 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 200 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | 3Punches_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 8 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][1].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][1].m_HitRow[0].RowName[0] | 3Punches_HB02 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 15 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][1].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/_PlaceHolders/RightArmHitDetection_For3Hits.RightArmHitDetection_For3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][1].m_eAltHitTarget[0] | EAttackTarget::High | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][1] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][1].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][2].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][2].m_HitRow[0].RowName[0] | 3Punches_HB03 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 19 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 24 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][2].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][2].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eOrigin[0] | EAttackOrigin::Middle | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][2] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][2].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 41 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 81 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Alt.MC_Attacks_Alt | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 81 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][2] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][2].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Speed.Fast | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][1] | m_Attack[0].m_AttackProperties[0][1] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][2] | m_Attack[0].m_AttackProperties[0][2] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][3] | m_Attack[0].m_AttackProperties[0][3] | Attack.HitProperties.Stun | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A004-MainChar_CrookedFoot_Thrust_FR

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/BareHands/PostParry/PostParry_Knockdown/MainChar_CrookedFoot_Thrust_FR.uasset

导出对象：MainChar_CrookedFoot_Thrust_FR

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/玩家攻击/MainChar_HitBoxData-5b12fa\|/Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData]] | CrookedFoot_Thrust_HB01 | Inclusive: 11 → Inclusive: 16 | EAttackTarget::Mid_1 | EAttackMovementType::Thrust | EAttackOrigin::Down | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 28 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 22 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Attacks.MainChar_Attacks | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | PunishKD_CrookedFoot_Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Attacks/Man/Barehands/PostParry/PostParry_Knockdown/MainChar_Attack_Man_Barehands_PunishKD_CrookedFoot_Thrust.MainChar_Attack_Man_Barehands_PunishKD_CrookedFoot_Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 8 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 覆盖动画范围[0] | m_Attack[0].m_bOverrideAnimRange[0] | 是 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 140 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 激活条件[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_activationCondition[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 类默认对象[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_DefaultClassObject[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 附加元数据[0] → 条件或对象实例[0] | m_Attack[0].m_HitBoxes[0][0].m_MetaData[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_HitBoxData.MainChar_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | CrookedFoot_Thrust_HB01 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 16 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftArmHitDetection.LeftArmHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Down | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 28 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 22 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_GenericFollowUp.MC_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][0] | m_Attack[0].m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][1] | m_Attack[0].m_AttackProperties[0][1] | Attack.Speed.Fast | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][2] | m_Attack[0].m_AttackProperties[0][2] | Attack.Combo.Finisher | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 攻击属性标签[0][3] | m_Attack[0].m_AttackProperties[0][3] | Attack.HitProperties.KnockDown | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。
