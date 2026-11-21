# Fengjie：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca\|BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB-29f9d1\|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_LongRange_ArchetypeDB.BP_Fengjie_Phase1_LongRange_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena-70fcab\|BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB-ef3efd\|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ShortRange_ArchetypeDB.BP_Fengjie_Phase1_ShortRange_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena-5d6b00\|BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB-8e8b24\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_LongRange_ArchetypeDB.BP_Fengjie_Phase2_LongRange_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena-d336eb\|BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB-4bf701\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ShortRange_ArchetypeDB.BP_Fengjie_Phase2_ShortRange_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB_Arena_RedRoom08-1aed43\|BP_Fengjie_Phase1_ArchetypeDB_Arena_RedRoom08]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca\|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_RedRoom10-aca2dc\|BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca\|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_RedRoom10-345837\|BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena-70fcab\|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_RedRoom10-7b853a\|BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena-5d6b00\|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_RedRoom10-df47dd\|BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena-d336eb\|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena.BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084\|BP_Fengjie_Phase1_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 550 | 700 | [[03配置/受击与抗性/Fengjie_ResistanceDB-dcd434\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB.Fengjie_ResistanceDB]] | [[03配置/AI防御/Fengjie_Phase1_ContextualDefense-bc212f\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_Phase1_ContextualDefense.Fengjie_Phase1_ContextualDefense]] |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB-29f9d1\|BP_Fengjie_Phase1_LongRange_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084\|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB-ef3efd\|BP_Fengjie_Phase1_ShortRange_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084\|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|BP_Fengjie_Phase2_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084\|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]] | 750 | 850 | 本资产未保存；可能继承 | [[03配置/AI防御/Fengjie_Phase2_ContextualDefense-153c91\|/Game/DB/AI/Archetypes/Fengjie/Phase2/Fengjie_Phase2_ContextualDefense.Fengjie_Phase2_ContextualDefense]] |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB-8e8b24\|BP_Fengjie_Phase2_LongRange_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB-4bf701\|BP_Fengjie_Phase2_ShortRange_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Test_FarGrab_ArchetypeDB-600d38\|BP_Fengjie_Test_FarGrab_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Test_NewCombos_ArchetypeDB-c56040\|BP_Fengjie_Test_NewCombos_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Test_Shockwave_ArchetypeDB-363fb2\|BP_Fengjie_Test_Shockwave_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004\|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB-29f9d1|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_LongRange_ArchetypeDB.BP_Fengjie_Phase1_LongRange_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena-70fcab

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB-ef3efd|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ShortRange_ArchetypeDB.BP_Fengjie_Phase1_ShortRange_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena-5d6b00

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB-8e8b24|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_LongRange_ArchetypeDB.BP_Fengjie_Phase2_LongRange_ArchetypeDB_C]]

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
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena-d336eb

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB-4bf701|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ShortRange_ArchetypeDB.BP_Fengjie_Phase2_ShortRange_ArchetypeDB_C]]

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
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_ArchetypeDB_Arena_RedRoom08-1aed43

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/Specific/RedRoom08/BP_Fengjie_Phase1_ArchetypeDB_Arena_RedRoom08.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1355 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanUseReactionActions）[0] | m_bCanUseReactionActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（28 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（4991 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_RedRoom10-aca2dc

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/Specific/RedRoom10/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena-6da2ca|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_LongRange_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_RedRoom10-345837

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/Specific/RedRoom10/BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena-70fcab|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena.BP_Fengjie_Phase1_ShortRange_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_RedRoom10-7b853a

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/Specific/RedRoom10/BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena-5d6b00|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena.BP_Fengjie_Phase2_LongRange_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_RedRoom10-df47dd

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/_Arena/Specific/RedRoom10/BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena-d336eb|/Game/DB/AI/Archetypes/Fengjie/_Arena/BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena.BP_Fengjie_Phase2_ShortRange_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_ArchetypeDB-757084

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Fengjie_ResistanceDB-dcd434\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB.Fengjie_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Fengjie_ResistanceDB_Easy-cc2277\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB_Easy.Fengjie_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Fengjie_ResistanceDB_Hard-122a2a\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB_Hard.Fengjie_ResistanceDB_Hard]] |
| 情境防御 | [[03配置/AI防御/Fengjie_Phase1_ContextualDefense-bc212f\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_Phase1_ContextualDefense.Fengjie_Phase1_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Fengjie | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Fengjie | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryPerSec[0] | -10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAICanSeeForever）[0] | m_bAICanSeeForever[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB.Fengjie_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB_Easy.Fengjie_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB_Hard.Fengjie_ResistanceDB_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/Fengjie_BaseMovementDB.Fengjie_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/_Shared/Structure/AIStructureRegenByHealth_Hard.AIStructureRegenByHealth_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_Phase1_ContextualDefense.Fengjie_Phase1_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AvoidDB）[0] | m_AvoidDB[0] | /Game/DB/Abilities/BP_AvoidAbility_AI_Fengjie.BP_AvoidAbility_AI_Fengjie_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | /Game/Blueprints/LDIngredients/Weapons/MeteorHammerFamily/Fengjie/BP_Weapon_FengjieBolas.BP_Weapon_FengjieBolas_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2245 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 64 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 64 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageReceivedToDifficultyBonus）[0] | m_fDamageReceivedToDifficultyBonus[0] | 2.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageDealtToDifficultyMalus）[0] | m_fDamageDealtToDifficultyMalus[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Blackboard）[0] | m_Blackboard[0] | /Game/Blueprints/AI/Bosses/Fengjie/BehaviorTree/AIBlackBoard_Fengjie.AIBlackBoard_Fengjie | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Fengjie | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Fengjie/Barks/Barks_Fengjie_P1.Barks_Fengjie_P1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/Fengjie/VitalPointsDBs/VitalPointDefinitionDataAsset_Fengjie.VitalPointDefinitionDataAsset_Fengjie | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::DirectOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fJiggleDelayRange）[0] | m_fJiggleDelayRange[0] | 未解码（24 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fJiggleMovementMinDist）[0] | m_fJiggleMovementMinDist[0] | 未解码（24 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 550 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1.20000005 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 700 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.29999995 | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_LongRange_ArchetypeDB-29f9d1

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_LongRange_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fengjie_Phase1_LongRange | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（52 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRangeInPauseOverride）[0] | m_PerRolePerCircleCombatPositionRangeInPauseOverride[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase1_ShortRange_ArchetypeDB-ef3efd

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ShortRange_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fengjie_Phase1_ShortRange | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_ArchetypeDB-8b9004

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase1_ArchetypeDB-757084|/Game/DB/AI/Archetypes/Fengjie/Phase1/BP_Fengjie_Phase1_ArchetypeDB.BP_Fengjie_Phase1_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Fengjie_ResistanceDB-dcd434\|/Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB.Fengjie_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Fengjie_Phase2_ContextualDefense-153c91\|/Game/DB/AI/Archetypes/Fengjie/Phase2/Fengjie_Phase2_ContextualDefense.Fengjie_Phase2_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldown[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryPerSec[0] | -15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Fengjie/Phase1/Fengjie_ResistanceDB.Fengjie_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 1500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Fengjie/Phase2/Fengjie_Phase2_ContextualDefense.Fengjie_Phase2_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Fengjie/Barks/Barks_Fengjie_P2.Barks_Fengjie_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（28 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanBeSpared）[0] | m_bCanBeSpared[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 类默认对象[0] | m_SpareCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Shared/BP_BossSpareStructureBrokenCountCondition.BP_BossSpareStructureBrokenCountCondition_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 750 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 850 | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_LongRange_ArchetypeDB-8e8b24

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_LongRange_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fengjie_Phase2_LongRange | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（2657 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Phase2_ShortRange_ArchetypeDB-4bf701

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ShortRange_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Fengjie_Phase2_ShortRange | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（52 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Test_FarGrab_ArchetypeDB-600d38

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/PhaseForReview/BP_Fengjie_Test_FarGrab_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1437 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（36 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Test_NewCombos_ArchetypeDB-c56040

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/PhaseForReview/BP_Fengjie_Test_NewCombos_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1437 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（36 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Fengjie_Test_Shockwave_ArchetypeDB-363fb2

来源资产：Sifu/Content/DB/AI/Archetypes/Fengjie/PhaseForReview/BP_Fengjie_Test_Shockwave_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Fengjie.md#BP_Fengjie_Phase2_ArchetypeDB-8b9004|/Game/DB/AI/Archetypes/Fengjie/Phase2/BP_Fengjie_Phase2_ArchetypeDB.BP_Fengjie_Phase2_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1437 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（36 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
