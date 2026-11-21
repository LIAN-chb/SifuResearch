# Fajar：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027\|BP_Fajar_Phase1_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522\|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.BP_Fajar_Phase1_Offensive_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB_Arena-056ea3\|BP_Fajar_Phase2_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB-a0bc14\|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase2_ArchetypeDB.BP_Fajar_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena_Hangar08-6c196b\|BP_Fajar_Phase1_ArchetypeDB_Arena_Hangar08]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027\|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom08-a6e3bd\|BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom08]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027\|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom10-984050\|BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027\|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB_Arena_RedRoom10-40a2d8\|BP_Fajar_Phase2_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB_Arena-056ea3\|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase2_ArchetypeDB_Arena.BP_Fajar_Phase2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522\|BP_Fajar_Phase1_Offensive_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 800 | 1200 | [[03配置/受击与抗性/Fajar_ResistanceDb-add80e\|/Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb.Fajar_ResistanceDb]] | [[03配置/AI防御/Fajar_ContextualDefense_Phase1_Offensive-7e5337\|/Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase1_Offensive.Fajar_ContextualDefense_Phase1_Offensive]] |
| [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB-a0bc14\|BP_Fajar_Phase2_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522\|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.BP_Fajar_Phase1_Offensive_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | [[03配置/AI防御/Fajar_ContextualDefense_Phase2-b1376b\|/Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase2.Fajar_ContextualDefense_Phase2]] |


## BP_Fajar_Phase1_ArchetypeDB_Arena-55c027

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.BP_Fajar_Phase1_Offensive_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Fajar_Arena_Phase1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase2_ArchetypeDB_Arena-056ea3

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase2_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB-a0bc14|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase2_ArchetypeDB.BP_Fajar_Phase2_ArchetypeDB_C]]

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
| 未核中文义（ElementID）[0] | ElementID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Fajar_Arena_Phase2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDropAnyWeaponAtStart）[0] | m_bDropAnyWeaponAtStart[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | /Game/Blueprints/LDIngredients/Weapons/BladeFamily/Machete/Fajar/BP_Weapon_Machete_Fajar.BP_Weapon_Machete_Fajar_C | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase1_ArchetypeDB_Arena_Hangar08-6c196b

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/Specific/Hangar08/BP_Fajar_Phase1_ArchetypeDB_Arena_Hangar08.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom08-a6e3bd

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/Specific/RedRoom08/BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom08.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]]

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
| 未核中文义（DisplayStandardLifeGauge）[0] | DisplayStandardLifeGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom10-984050

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/Specific/RedRoom10/BP_Fajar_Phase1_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_ArchetypeDB_Arena-55c027|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase1_ArchetypeDB_Arena.BP_Fajar_Phase1_ArchetypeDB_Arena_C]]

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
| 未核中文义（DisplayStandardLifeGauge）[0] | DisplayStandardLifeGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase2_ArchetypeDB_Arena_RedRoom10-40a2d8

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/_Arena/Specific/RedRoom10/BP_Fajar_Phase2_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase2_ArchetypeDB_Arena-056ea3|/Game/DB/AI/Archetypes/Fajar/_Arena/BP_Fajar_Phase2_ArchetypeDB_Arena.BP_Fajar_Phase2_ArchetypeDB_Arena_C]]

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
| 未核中文义（DisplayStandardLifeGauge）[0] | DisplayStandardLifeGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Fajar_ResistanceDb-add80e\|/Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb.Fajar_ResistanceDb]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Fajar_ResistanceDb_Easy-ba06f2\|/Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb_Easy.Fajar_ResistanceDb_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Fajar_ResistanceDb_Hard-3a287f\|/Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb_Hard.Fajar_ResistanceDb_Hard]] |
| 情境防御 | [[03配置/AI防御/Fajar_ContextualDefense_Phase1_Offensive-7e5337\|/Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase1_Offensive.Fajar_ContextualDefense_Phase1_Offensive]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Fajar | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fajar_Phase1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 350 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb.Fajar_ResistanceDb | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb_Easy.Fajar_ResistanceDb_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Fajar/Fajar_ResistanceDb_Hard.Fajar_ResistanceDb_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Fajar/Fajar_StructureRegenByHealth.Fajar_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/Fajar/Fajar_StructureRegenByHealth.Fajar_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/Fajar/Fajar_StructureRegenByHealth.Fajar_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase1_Offensive.Fajar_ContextualDefense_Phase1_Offensive | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/Fajar/Fajar_ContextualDefense_Throwables.Fajar_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1487 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/Fajar_Vault_QueryFilter.Fajar_Vault_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCAvoidBonus）[0] | m_fSuccessfulMCAvoidBonus[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Behavior）[0] | m_Behavior[0] | /Game/Blueprints/AI/BehaviorTree/AiTreeWuguan.AiTreeWuguan | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Blackboard）[0] | m_Blackboard[0] | /Game/Blueprints/AI/Bosses/Fajar/AIBlackBoard_Fajar.AIBlackBoard_Fajar | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Fajar | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Fajar/Barks/Barks_Fajar_P1.Barks_Fajar_P1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.20000005 | 该字段暂保留原名；中文语义待核。 |


## BP_Fajar_Phase2_ArchetypeDB-a0bc14

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.BP_Fajar_Phase1_Offensive_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | [[03配置/AI防御/Fajar_ContextualDefense_Phase2-b1376b\|/Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase2.Fajar_ContextualDefense_Phase2]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fajar_Phase2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 1500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase2.Fajar_ContextualDefense_Phase2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Fajar/Barks/Barks_Fajar_P2.Barks_Fajar_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanBeSpared）[0] | m_bCanBeSpared[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 类默认对象[0] | m_SpareCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Shared/BP_BossSpareStructureBrokenCountCondition.BP_BossSpareStructureBrokenCountCondition_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
