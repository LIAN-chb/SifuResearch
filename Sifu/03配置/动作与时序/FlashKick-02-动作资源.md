# FlashKick-02：全部已解析动作资源

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

本页列出 1 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。

## 动作索引

| 动作资源 | 路径范围标签 | 动画行表 | 动画行名 | 保存帧率 | 期望前摇帧字段 | 已解析命中窗口数 | 已解析许可窗口数 |
|---|---|---|---|---|---|---|---|
| [[03配置/动作与时序/FlashKick-02-动作资源.md#A001-FlashKick_Heavy_ReverseKick\|A001 FlashKick_Heavy_ReverseKick]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/FlashKick_AttackData-81f5d7\|/Game/DB/AI/Archetypes/FlashKick/Attacks/FlashKick_AttackData.FlashKick_AttackData]] | FlashKick_attack_barehands_feint_reverse_kick | 60 | 20 | 1 | 2 |


## A001-FlashKick_Heavy_ReverseKick

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/Attacks/BareHands/Light/OldAttacks/FlashKick_Heavy_ReverseKick.uasset

导出对象：FlashKick_Heavy_ReverseKick

### 保存的命中窗口与效果行关联

| 序号 | HitBox 表 | 行名 | 帧区间与端点类型 | 命中目标高度字段 | 动作类型字段 | 来源方向字段 | 激活条件原值 |
|---|---|---|---|---|---|---|---|
| 0 | [[03配置/敌人攻击/Flashkick_HitBoxData-8fe837\|/Game/DB/AI/Archetypes/FlashKick/Attacks/Flashkick_HitBoxData.FlashKick_HitBoxData]] | ReverseKick | Inclusive: 26 → Inclusive: 29 | EAttackTarget::Mid_1 | EAttackMovementType::Thrust | EAttackOrigin::Left | {"m_DefaultClassObject[0]":{"index":0,"reference":null},"m_Instance[0]":{"index":0,"reference":null}} |


### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Exclusive: 58 → 无界（保存值 37 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |
| 1 | Inclusive: 40 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/AI/Archetypes/FlashKick/Attacks/FlashKick_AttackData.FlashKick_AttackData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | FlashKick_attack_barehands_feint_reverse_kick | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/FlashKick/Attacks/Barehands/Light/FlashKick_attack_barehands_feint_reverse_kick.FlashKick_attack_barehands_feint_reverse_kick | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
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
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据表引用[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].DataTable[0] | /Game/DB/AI/Archetypes/FlashKick/Attacks/Flashkick_HitBoxData.FlashKick_HitBoxData | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击效果行引用[0] → 数据行名称[0] | m_Attack[0].m_HitBoxes[0][0].m_HitRow[0].RowName[0] | ReverseKick | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 26 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_HitBoxes[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 29 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中检测配置[0] | m_Attack[0].m_HitBoxes[0][0].m_HitDetectionDB[0] | /Game/DB/_Shared/HitDetection/LeftLegHitDetection.LeftLegHitDetection | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 备用命中部位类别[0] | m_Attack[0].m_HitBoxes[0][0].m_eAltHitTarget[0] | EAttackTarget::Mid_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 瞄准目标类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAimTarget[0] | EIKAnimTargetTypes::Target | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击运动类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eMovementType[0] | EAttackMovementType::Thrust | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → 攻击来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eOrigin[0] | EAttackOrigin::Left | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义来源方向[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomOrigin[0] | EAttackOrigin::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义命中部位[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomHitTarget[0] | EAttackTarget::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 命中窗口列表[0][0] → Avoid 自定义动作类型[0] | m_Attack[0].m_HitBoxes[0][0].m_eAvoidCustomMovementType[0] | EAttackMovementType::None | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Exclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 58 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/AIs/AI_Attacks_GenericFollowUp.AI_Attacks_GenericFollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。
