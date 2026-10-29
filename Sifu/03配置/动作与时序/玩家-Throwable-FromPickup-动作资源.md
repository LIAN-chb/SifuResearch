# 玩家-Throwable-FromPickup：全部已解析动作资源

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

本页列出 5 个 AttackDB 对象，保留旧路径和测试标记。资源对象不等于独立可输入招式，实际可用性、中文招式名与当前调用状态尚未全部核对；输入衔接图另见玩家攻击目录。动作许可层窗口不直接称为取消窗口。

## 动作索引

| 动作资源 | 路径范围标签 | 动画行表 | 动画行名 | 保存帧率 | 期望前摇帧字段 | 已解析命中窗口数 | 已解析许可窗口数 |
|---|---|---|---|---|---|---|---|
| [[03配置/动作与时序/玩家-Throwable-FromPickup-动作资源.md#A001-MC_Throwable_FromPickup_Bats_FL\|A001 MC_Throwable_FromPickup_Bats_FL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Throwables-bc7e18\|/Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables]] | MC_man_throwable_fromPickup_bats_FL | 120 | 11 | 未保存／未解码 | 2 |
| [[03配置/动作与时序/玩家-Throwable-FromPickup-动作资源.md#A002-MC_Throwable_FromPickup_Bottle_BR\|A002 MC_Throwable_FromPickup_Bottle_BR]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Throwables-bc7e18\|/Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables]] | MC_man_throwable_fromPickup_bottle_BR | 60 | 11 | 未保存／未解码 | 2 |
| [[03配置/动作与时序/玩家-Throwable-FromPickup-动作资源.md#A003-MC_Throwable_FromPickup_Bottle_FL\|A003 MC_Throwable_FromPickup_Bottle_FL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Throwables-bc7e18\|/Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables]] | MC_man_throwable_fromPickup_bottle_FL | 120 | 11 | 未保存／未解码 | 2 |
| [[03配置/动作与时序/玩家-Throwable-FromPickup-动作资源.md#A004-MC_Throwable_FromPickup_Staff_BL\|A004 MC_Throwable_FromPickup_Staff_BL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Throwables-bc7e18\|/Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables]] | MC_man_throwable_fromPickup_staff_BL | 60 | 5 | 未保存／未解码 | 2 |
| [[03配置/动作与时序/玩家-Throwable-FromPickup-动作资源.md#A005-MC_Throwable_FromPickup_Staff_FL\|A005 MC_Throwable_FromPickup_Staff_FL]] | 路径未专门标注；使用情况待查 | [[03配置/动作与时序/MainChar_Throwables-bc7e18\|/Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables]] | MC_man_throwable_fromPickup_staff_FL | 60 | 5 | 未保存／未解码 | 2 |


## A001-MC_Throwable_FromPickup_Bats_FL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/Throwable/FromPickup/Bats/MC_Throwable_FromPickup_Bats_FL.uasset

导出对象：MC_Throwable_FromPickup_Bats_FL

### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 37 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp |
| 1 | Inclusive: 40 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_man_throwable_fromPickup_bats_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Throwable/Man/FromPickup/Bats/MC_man_throwable_fromPickup_bats_FL.MC_man_throwable_fromPickup_bats_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 120 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.00833333377 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 181.279037 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A002-MC_Throwable_FromPickup_Bottle_BR

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/Throwable/FromPickup/Bottle/MC_Throwable_FromPickup_Bottle_BR.uasset

导出对象：MC_Throwable_FromPickup_Bottle_BR

### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 14 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp |
| 1 | Inclusive: 28 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_man_throwable_fromPickup_bottle_BR | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Throwable/Man/FromPickup/Bottle/MC_man_throwable_fromPickup_bottle_BR.MC_man_throwable_fromPickup_bottle_BR | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 213.526596 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 14 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 28 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A003-MC_Throwable_FromPickup_Bottle_FL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/Throwable/FromPickup/Bottle/MC_Throwable_FromPickup_Bottle_FL.uasset

导出对象：MC_Throwable_FromPickup_Bottle_FL

### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 37 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp |
| 1 | Inclusive: 40 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_man_throwable_fromPickup_bottle_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Throwable/Man/FromPickup/Bottle/MC_man_throwable_fromPickup_bottle_FL.MC_man_throwable_fromPickup_bottle_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 120 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.00833333377 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 11 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 181.279053 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 37 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 40 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A004-MC_Throwable_FromPickup_Staff_BL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/Throwable/FromPickup/Staff/MC_Throwable_FromPickup_Staff_BL.uasset

导出对象：MC_Throwable_FromPickup_Staff_BL

### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 18 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp |
| 1 | Inclusive: 20 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_man_throwable_fromPickup_staff_BL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Throwable/Man/FromPickup/Staff/MC_man_throwable_fromPickup_staff_BL.MC_man_throwable_fromPickup_staff_BL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 213.605682 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 18 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## A005-MC_Throwable_FromPickup_Staff_FL

来源资产：Sifu/Content/DB/_MainChar/Combos/Attacks/Throwable/FromPickup/Staff/MC_Throwable_FromPickup_Staff_FL.uasset

导出对象：MC_Throwable_FromPickup_Staff_FL

### 保存的动作许可窗口

| 序号 | 帧区间与端点类型 | 命中条件掩码原值 | 动作层引用 |
|---|---|---|---|
| 0 | Inclusive: 18 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp |
| 1 | Inclusive: 20 → 无界（保存值 0 不作端点） | 31 | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll |


### 本对象全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击数据[0] → 动画数据行引用[0] → 数据表引用[0] | m_Attack[0].m_AnimationRow[0].DataTable[0] | /Game/DB/_MainChar/Combos/MainChar_Throwables.MainChar_Throwables | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画数据行引用[0] → 数据行名称[0] | m_Attack[0].m_AnimationRow[0].RowName[0] | MC_man_throwable_fromPickup_staff_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画资源[0] | m_Attack[0].m_Animation[0] | /Game/Animations/MainChar/Throwable/Man/FromPickup/Staff/MC_man_throwable_fromPickup_staff_FL.MC_man_throwable_fromPickup_staff_FL | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画配置帧率[0] | m_Attack[0].m_fAnimFrameRate[0] | 60 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动画每帧时长[0] | m_Attack[0].m_fAnimFrameDeltaTime[0] | 0.0166666675 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 期望前摇帧数[0] | m_Attack[0].m_iWantedBuildupFrames[0] | 5 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 玩法攻击距离[0] | m_Attack[0].m_fGameplayRange[0] | 164.590561 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 向后贴合余量[0] | m_Attack[0].m_fSnapbackMargin[0] | 100 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 请求贴合目标[0] | m_Attack[0].m_bWantSnap[0] | 否 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 18 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][0] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][0].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/Attacks/MC/MC_Attacks_Throwable_FollowUp.MC_Attacks_Throwable_FollowUp | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 命中条件掩码[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_uiHitConditions[0] | 31 | 原始条件掩码尚未全部翻译，不改写成确定命中攻略。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Type[0] | ERangeBoundTypes::Inclusive | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间下界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].LowerBound[0].Value[0] | 20 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点类型[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Type[0] | ERangeBoundTypes::Open | Inclusive=包含，Exclusive=不包含，Open=无界。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 帧范围[0] → 动画帧区间[0] → 区间上界[0] → 端点保存值[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_FrameRange[0].m_Anim[0].UpperBound[0].Value[0] | 0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击数据[0] → 动作许可层窗口[0][1] → 动作许可层[0] | m_Attack[0].m_AvailabilityLayerWindows[0][1].m_Layer[0] | /Game/DB/Inputs/Availability/LayerData/GenericAll.GenericAll | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 配置版本号[0] | m_iVersionNumber[0] | 1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/tagged-objects.json.gz。未保存、空数组和未解码数组分别按原数据保留；开放端点不将保存的 0 当作终点。
