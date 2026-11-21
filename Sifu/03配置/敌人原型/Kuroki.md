# Kuroki：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf\|BP_Kuroki_P1_ArchetypeDB_Melee_Arena]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee-0e9223\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Melee.BP_Kuroki_P1_ArchetypeDB_Melee_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb\|BP_Kuroki_P1_ArchetypeDB_Ranged_Arena]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged-b3760e\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Ranged.BP_Kuroki_P1_ArchetypeDB_Ranged_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena-4aaf73\|BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena-fb6691\|BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged-50efed\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged.BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Arena_RedRoom08-48f12f\|BP_Kuroki_P1_ArchetypeDB_Arena_RedRoom08]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena_RedRoom10-9378fb\|BP_Kuroki_P1_ArchetypeDB_Melee_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Melee_Arena.BP_Kuroki_P1_ArchetypeDB_Melee_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_RedRoom10-6a4b0a\|BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_RedRoom10-3efb3b\|BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena-4aaf73\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_RedRoom10-6f2718\|BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena-fb6691\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena.BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena_SnowGarden06-1aeb4e\|BP_Kuroki_P1_ArchetypeDB_Melee_Arena_SnowGarden06]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Melee_Arena.BP_Kuroki_P1_ArchetypeDB_Melee_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_SnowGarden06-010863\|BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_SnowGarden06]] | 竞技场 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb\|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee-0e9223\|BP_Kuroki_P1_ArchetypeDB_Melee]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 1200 | 1400 | [[03配置/受击与抗性/Kuroki_ResistanceDB-3dd000\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB.Kuroki_ResistanceDB]] | [[03配置/AI防御/Kuroki_ContextualDefense-62b844\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ContextualDefense.Kuroki_ContextualDefense]] |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged-b3760e\|BP_Kuroki_P1_ArchetypeDB_Ranged]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee-0e9223\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Melee.BP_Kuroki_P1_ArchetypeDB_Melee_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e\|BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 1200 | 1100 | [[03配置/受击与抗性/Shiroizu_ResistanceDB-a286af\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB.Shiroizu_ResistanceDB]] | [[03配置/AI防御/Shiroizu_ContextualDefense-b35f28\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ContextualDefense.Shiroizu_ContextualDefense]] |
| [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged-50efed\|BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e\|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Melee_Arena.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee-0e9223|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Melee.BP_Kuroki_P1_ArchetypeDB_Melee_C]]

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


## BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged-b3760e|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Ranged.BP_Kuroki_P1_ArchetypeDB_Ranged_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena-4aaf73

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Shiroizu_Arena | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena-fb6691

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged-50efed|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged.BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Shiroizu_Arena | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P1_ArchetypeDB_Arena_RedRoom08-48f12f

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/RedRoom08/BP_Kuroki_P1_ArchetypeDB_Arena_RedRoom08.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]]

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
| 未核中文义（m_fDamageMultiplier）[0] | m_fDamageMultiplier[0] | 0.600000024 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（531 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P1_ArchetypeDB_Melee_Arena_RedRoom10-9378fb

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/RedRoom10/BP_Kuroki_P1_ArchetypeDB_Melee_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Melee_Arena.BP_Kuroki_P1_ArchetypeDB_Melee_Arena_C]]

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


## BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_RedRoom10-6a4b0a

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/RedRoom10/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]]

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


## BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_RedRoom10-3efb3b

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/RedRoom10/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena-4aaf73|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_Arena_C]]

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


## BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_RedRoom10-6f2718

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/RedRoom10/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena-fb6691|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena.BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged_Arena_C]]

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


## BP_Kuroki_P1_ArchetypeDB_Melee_Arena_SnowGarden06-1aeb4e

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/SnowGarden06/BP_Kuroki_P1_ArchetypeDB_Melee_Arena_SnowGarden06.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee_Arena-3b0adf|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Melee_Arena.BP_Kuroki_P1_ArchetypeDB_Melee_Arena_C]]

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


## BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_SnowGarden06-010863

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/_Arena/Specific/SnowGarden06/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_SnowGarden06.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Ranged_Arena-e3d2eb|/Game/DB/AI/Archetypes/Kuroki/_Arena/BP_Kuroki_P1_ArchetypeDB_Ranged_Arena.BP_Kuroki_P1_ArchetypeDB_Ranged_Arena_C]]

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


## BP_Kuroki_P1_ArchetypeDB_Melee-0e9223

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Melee.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Kuroki_ResistanceDB-3dd000\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB.Kuroki_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Kuroki_ResistanceDB_Easy-0b99c6\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB_Easy.Kuroki_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Kuroki_ResistanceDB_Hard-81024a\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB_Hard.Kuroki_ResistanceDB_Hard]] |
| 情境防御 | [[03配置/AI防御/Kuroki_ContextualDefense-62b844\|/Game/DB/AI/Archetypes/Kuroki/Kuroki_ContextualDefense.Kuroki_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldown[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryPerSec[0] | -10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB.Kuroki_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB_Easy.Kuroki_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_ResistanceDB_Hard.Kuroki_ResistanceDB_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Kuroki/KurokiGuardGaugeRecoveryRateByLife.KurokiGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/Kuroki/KurokiGuardGaugeRecoveryRateByLife.KurokiGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/Kuroki/KurokiGuardGaugeRecoveryRateByLife.KurokiGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Kuroki/Kuroki_ContextualDefense.Kuroki_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AvoidDB）[0] | m_AvoidDB[0] | /Game/DB/Abilities/BP_AvoidAbility_AI_Kuroki.BP_AvoidAbility_AI_Kuroki_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | /Game/Blueprints/LDIngredients/Weapons/TwoHandedFamily/TriStaff/BP_KurokiTriStaff.BP_KurokiTriStaff_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（877 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbLowDrop_QueryFilter.VaultClimbLowDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Kuroki/Barks/Barks_Kuroki_P1.Barks_Kuroki_P1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/Kuroki/VitalPointsDBs/VitalPointDefinitionDataAsset_Kuroki.VitalPointDefinitionDataAsset_Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::DirectOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（3330 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[1] | m_fHealthMultiplier[1] | 0.800000012 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[1] | m_fStructureMultiplier[1] | 0.800000012 | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P1_ArchetypeDB_Ranged-b3760e

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Ranged.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P1_ArchetypeDB_Melee-0e9223|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P1_ArchetypeDB_Melee.BP_Kuroki_P1_ArchetypeDB_Melee_C]]

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
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Shiroizu_ResistanceDB-a286af\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB.Shiroizu_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Shiroizu_ResistanceDB_Easy-988960\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB_Easy.Shiroizu_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Shiroizu_ResistanceDB_Hard-2f90f4\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB_Hard.Shiroizu_ResistanceDB_Hard]] |
| 情境防御 | [[03配置/AI防御/Shiroizu_ContextualDefense-b35f28\|/Game/DB/AI/Archetypes/Kuroki/Shiroizu_ContextualDefense.Shiroizu_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldown[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyGaugeRatioAfterSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyGaugeRatioAfterSuperDizzy[0] | 0.200000003 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryPerSec[0] | -2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyGaugeRatioAfterSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyGaugeRatioAfterSuperDizzy[0] | 0.200000003 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyGaugeRatioAfterSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyGaugeRatioAfterSuperDizzy[0] | 0.200000003 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB.Shiroizu_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB_Easy.Shiroizu_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Kuroki/Shiroizu_ResistanceDB_Hard.Shiroizu_ResistanceDB_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 1500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/ShiroizuKurokiP2_BaseMovementDB.ShiroizuKurokiP2_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Kuroki/ShiroizuGuardGaugeRecoveryRateByLife.ShiroizuGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/Kuroki/ShiroizuGuardGaugeRecoveryRateByLife.ShiroizuGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/Kuroki/ShiroizuGuardGaugeRecoveryRateByLife.ShiroizuGuardGaugeRecoveryRateByLife | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Kuroki/Shiroizu_ContextualDefense.Shiroizu_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDropAnyWeaponAtStart）[0] | m_bDropAnyWeaponAtStart[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eNearFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eFarFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eFarFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbLowDrop_QueryFilter.VaultClimbLowDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageReceivedToDifficultyBonus）[0] | m_fDamageReceivedToDifficultyBonus[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageDealtToDifficultyMalus）[0] | m_fDamageDealtToDifficultyMalus[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Shiroizu | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Kuroki/Barks/Barks_Kuroki_P2.Barks_Kuroki_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/Kuroki/VitalPointsDBs/VitalPointDefinitionDataAsset_Kuroki.VitalPointDefinitionDataAsset_Kuroki | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::DirectOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（3330 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanBeSpared）[0] | m_bCanBeSpared[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 类默认对象[0] | m_SpareCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Shared/BP_BossSpareStructureBrokenCountCondition.BP_BossSpareStructureBrokenCountCondition_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.20000005 | 该字段暂保留原名；中文语义待核。 |


## BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged-50efed

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuRanged.uasset

父类：[[03配置/敌人原型/Kuroki.md#BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee-e9dd9e|/Game/DB/AI/Archetypes/Kuroki/BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee.BP_Kuroki_P2_ArchetypeDB_ShiroizuMelee_C]]

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
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（3330 字节） | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
