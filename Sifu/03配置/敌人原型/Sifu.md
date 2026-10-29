# Sifu：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena-c73975\|BP_Sifu_P1_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB-f1d197\|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P1_ArchetypeDB.BP_Sifu_P1_ArchetypeDB_C]] | 900 | 1500 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac\|BP_Sifu_P2_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB-96dd01\|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB.BP_Sifu_P2_ArchetypeDB_C]] | 1000 | 1700 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena_RedRoom06-6f3614\|BP_Sifu_P1_ArchetypeDB_Arena_RedRoom06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena-c73975\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P1_ArchetypeDB_Arena.BP_Sifu_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena_RedRoom06-bdf24c\|BP_Sifu_P2_ArchetypeDB_Arena_RedRoom06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena_ThePark06-c848fd\|BP_Sifu_P2_ArchetypeDB_Arena_ThePark06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P3_ArchetypeDB_Arena_ThePark06-d3e892\|BP_Sifu_P3_ArchetypeDB_Arena_ThePark06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena_Wuguan06-4e1d13\|BP_Sifu_P1_ArchetypeDB_Arena_Wuguan06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena-c73975\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P1_ArchetypeDB_Arena.BP_Sifu_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena_Wuguan06-d52ed0\|BP_Sifu_P2_ArchetypeDB_Arena_Wuguan06]] | 竞技场 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac\|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB-f1d197\|BP_Sifu_P1_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 400 | 500 | [[03配置/受击与抗性/Sifu_ResistanceDB-2fc4fb\|/Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB]] | [[03配置/AI防御/Sifu_ContextualDefense-a62947\|/Game/DB/AI/Archetypes/Sifu/Sifu_ContextualDefense.Sifu_ContextualDefense]] |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB-96dd01\|BP_Sifu_P2_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB-f1d197\|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P1_ArchetypeDB.BP_Sifu_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_NoAttack-2ef8ec\|BP_Sifu_P2_ArchetypeDB_NoAttack]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB-96dd01\|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB.BP_Sifu_P2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Sifu_P1_ArchetypeDB_Arena-c73975

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P1_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB-f1d197|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P1_ArchetypeDB.BP_Sifu_P1_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 900 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1500 | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB_Arena-24e0ac

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB-96dd01|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB.BP_Sifu_P2_ArchetypeDB_C]]

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
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（DisplayStandardLifeGauge）[0] | DisplayStandardLifeGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1000 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1700 | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P1_ArchetypeDB_Arena_RedRoom06-6f3614

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/RedRoom06/BP_Sifu_P1_ArchetypeDB_Arena_RedRoom06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena-c73975|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P1_ArchetypeDB_Arena.BP_Sifu_P1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB_Arena_RedRoom06-bdf24c

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/RedRoom06/BP_Sifu_P2_ArchetypeDB_Arena_RedRoom06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB_Arena_ThePark06-c848fd

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/ThePark06/BP_Sifu_P2_ArchetypeDB_Arena_ThePark06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P3_ArchetypeDB_Arena_ThePark06-d3e892

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/ThePark06/BP_Sifu_P3_ArchetypeDB_Arena_ThePark06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（HideBossUI）[0] | HideBossUI[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Sifu_Phase3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInfiniteStructure）[0] | m_bInfiniteStructure[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInvincible）[0] | m_bInvincible[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P1_ArchetypeDB_Arena_Wuguan06-4e1d13

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/Wuguan06/BP_Sifu_P1_ArchetypeDB_Arena_Wuguan06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB_Arena-c73975|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P1_ArchetypeDB_Arena.BP_Sifu_P1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB_Arena_Wuguan06-d52ed0

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/_Arena/Specific/Wuguan06/BP_Sifu_P2_ArchetypeDB_Arena_Wuguan06.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB_Arena-24e0ac|/Game/DB/AI/Archetypes/Sifu/_Arena/BP_Sifu_P2_ArchetypeDB_Arena.BP_Sifu_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P1_ArchetypeDB-f1d197

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/BP_Sifu_P1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Sifu_ResistanceDB-2fc4fb\|/Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Sifu_ResistanceDB-2fc4fb\|/Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Sifu_ResistanceDB-2fc4fb\|/Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Sifu_ContextualDefense-a62947\|/Game/DB/AI/Archetypes/Sifu/Sifu_ContextualDefense.Sifu_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Sifu_Phase1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Sifu/Sifu_ResistanceDB.Sifu_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Sifu/Sifu_ContextualDefense.Sifu_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageReceivedToDifficultyBonus）[0] | m_fDamageReceivedToDifficultyBonus[0] | 1.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageDealtToDifficultyMalus）[0] | m_fDamageDealtToDifficultyMalus[0] | 2.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCAvoidBonus）[0] | m_fSuccessfulMCAvoidBonus[0] | 30 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | LiuChou | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Sifu/Barks/Barks_Sifu_P2.Barks_Sifu_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::DirectOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（20 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（3330 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 500 | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB-96dd01

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P1_ArchetypeDB-f1d197|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P1_ArchetypeDB.BP_Sifu_P1_ArchetypeDB_C]]

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
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sifu_P2_ArchetypeDB_NoAttack-2ef8ec

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB_NoAttack.uasset

父类：[[03配置/敌人原型/Sifu.md#BP_Sifu_P2_ArchetypeDB-96dd01|/Game/DB/AI/Archetypes/Sifu/BP_Sifu_P2_ArchetypeDB.BP_Sifu_P2_ArchetypeDB_C]]

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
| 未核中文义（m_bCanDefend）[0] | m_bCanDefend[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（20 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（4991 字节） | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
