# Servant：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Arena-638090\|BP_Servant_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|BP_Servant_ArchetypeDB]] | 路径未专门标注；使用情况待查 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 60 | 80 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] | [[03配置/AI防御/Servant_ContextualDefense-6866f3\|/Game/DB/AI/Archetypes/Servant/Servant_ContextualDefense.Servant_ContextualDefense]] |
| [[03配置/敌人原型/Servant.md#BP_ServantFaction_ArchetypeDB-21183b\|BP_ServantFaction_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_H0_TrainingEntry_ArchetypeDB-486a84\|BP_H0_TrainingEntry_ArchetypeDB]] | 路径未专门标注；使用情况待查 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 150 | 70 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] | [[03配置/AI防御/Servant_H0_TrainingEntry_ContextualDefense-6a0ae5\|/Game/DB/AI/Archetypes/Servant/Variants/Hideout0/Servant_H0_TrainingEntry_ContextualDefense.Servant_H0_TrainingEntry_ContextualDefense]] |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_NoXP-43a80a\|BP_Servant_ArchetypeDB_NoXP]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_NoXP_Spectator-181e24\|BP_Servant_ArchetypeDB_NoXP_Spectator]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_NoXP-43a80a\|/Game/DB/AI/Archetypes/Servant/Variants/Hideout0/BP_Servant_ArchetypeDB_NoXP.BP_Servant_ArchetypeDB_NoXP_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H1-8be566\|BP_Servant_ArchetypeDB_H1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Stronger_H1-be16bb\|BP_Servant_ArchetypeDB_Stronger_H1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H2-690b2d\|BP_Servant_ArchetypeDB_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Stronger_H2-3c1dce\|BP_Servant_ArchetypeDB_Stronger_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_ServantFaction_ArchetypeDB_H2-998845\|BP_ServantFaction_ArchetypeDB_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_ServantFaction_ArchetypeDB-21183b\|/Game/DB/AI/Archetypes/Servant/BP_ServantFaction_ArchetypeDB.BP_ServantFaction_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H3-bed929\|BP_Servant_ArchetypeDB_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H3_Mute-cb229c\|BP_Servant_ArchetypeDB_H3_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Stronger_H3-ef8934\|BP_Servant_ArchetypeDB_Stronger_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_Pacifist_NoAttack_NoXP_OneShot_Mute_DB-e29807\|BP_Servant_Pacifist_NoAttack_NoXP_OneShot_Mute_DB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/_Tests.md#BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB-05e4ea\|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB.BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H4-44de5c\|BP_Servant_ArchetypeDB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Stronger_H4-652d21\|BP_Servant_ArchetypeDB_Stronger_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_H5-086ebf\|BP_Servant_ArchetypeDB_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_Stronger_H5-df4ed2\|BP_Servant_ArchetypeDB_Stronger_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Servant_ArchetypeDB_Arena-638090

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/_Arena/Generic/BP_Servant_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB-efb8d4

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Servant_ContextualDefense-6866f3\|/Game/DB/AI/Archetypes/Servant/Servant_ContextualDefense.Servant_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageMultiplier）[0] | m_fDamageMultiplier[0] | 0.600000024 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Servant/Servant_ContextualDefense.Servant_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（2687 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 700 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（154 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_All.Barks_Servant_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_Arena.Barks_Servant_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PatrolActivities）[0] | m_PatrolActivities[0] | 未解码（283 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationContainers）[0] | m_JiggleAnimationContainers[0] | 未解码（1064 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间下界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].LowerBound[0].Value[0] | 0.899999976 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间上界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].UpperBound[0].Value[0] | 1.10000002 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 60 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 80 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1 | 该字段暂保留原名；中文语义待核。 |


## BP_ServantFaction_ArchetypeDB-21183b

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/BP_ServantFaction_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bInfiniteStructure）[0] | m_bInfiniteStructure[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInvincible）[0] | m_bInvincible[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_H0_TrainingEntry_ArchetypeDB-486a84

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout0/BP_H0_TrainingEntry_ArchetypeDB.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Servant_ResistanceDB-47121f\|/Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Servant_H0_TrainingEntry_ContextualDefense-6a0ae5\|/Game/DB/AI/Archetypes/Servant/Variants/Hideout0/Servant_H0_TrainingEntry_ContextualDefense.Servant_H0_TrainingEntry_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fDamageMultiplier）[0] | m_fDamageMultiplier[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bHideHealthGauge）[0] | m_bHideHealthGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Servant/Servant_ResistanceDB.Servant_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Servant/Variants/Hideout0/Servant_H0_TrainingEntry_ContextualDefense.Servant_H0_TrainingEntry_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 70 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_NoXP-43a80a

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout0/BP_Servant_ArchetypeDB_NoXP.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H0.Barks_Servant_H0 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_NoXP_Spectator-181e24

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout0/BP_Servant_ArchetypeDB_NoXP_Spectator.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB_NoXP-43a80a|/Game/DB/AI/Archetypes/Servant/Variants/Hideout0/BP_Servant_ArchetypeDB_NoXP.BP_Servant_ArchetypeDB_NoXP_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H1-8be566

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout1/BP_Servant_ArchetypeDB_H1.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H1.Barks_Servant_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_Stronger_H1-be16bb

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout1/BP_Servant_ArchetypeDB_Stronger_H1.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H1.Barks_Grunt_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H2-690b2d

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout2/BP_Servant_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H2.Barks_Servant_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_Stronger_H2-3c1dce

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout2/BP_Servant_ArchetypeDB_Stronger_H2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H2.Barks_Grunt_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_ServantFaction_ArchetypeDB_H2-998845

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout2/BP_ServantFaction_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/Servant.md#BP_ServantFaction_ArchetypeDB-21183b|/Game/DB/AI/Archetypes/Servant/BP_ServantFaction_ArchetypeDB.BP_ServantFaction_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H2.Barks_Servant_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H3-bed929

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout3/BP_Servant_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H3.Barks_Servant_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H3_Mute-cb229c

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout3/BP_Servant_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_Stronger_H3-ef8934

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout3/BP_Servant_ArchetypeDB_Stronger_H3.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H3.Barks_Grunt_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_Pacifist_NoAttack_NoXP_OneShot_Mute_DB-e29807

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout3/BP_Servant_Pacifist_NoAttack_NoXP_OneShot_Mute_DB.uasset

父类：[[03配置/敌人原型/_Tests.md#BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB-05e4ea|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB.BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H4-44de5c

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout4/BP_Servant_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H4.Barks_Servant_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_Stronger_H4-652d21

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout4/BP_Servant_ArchetypeDB_Stronger_H4.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_H5-086ebf

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout5/BP_Servant_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Servant/Barks/Barks_Servant_H5.Barks_Servant_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_ArchetypeDB_Stronger_H5-df4ed2

来源资产：Sifu/Content/DB/AI/Archetypes/Servant/Variants/Hideout5/BP_Servant_ArchetypeDB_Stronger_H5.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Servant | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H5.Barks_Grunt_H5 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
