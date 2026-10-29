# Sean：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB_Arena-8dabce\|BP_Sean_Burst_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB-06eedf\|/Game/DB/AI/Archetypes/Sean/BP_Sean_Burst_ArchetypeDB.BP_Sean_Burst_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938\|BP_Sean_P1_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB_Arena-f87328\|BP_Sean_P2_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB-1974bc\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P2_ArchetypeDB.BP_Sean_P2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena_DanceFloor09-4d1e08\|BP_Sean_P1_ArchetypeDB_Arena_DanceFloor09]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938\|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena_RedRoom08-0528cd\|BP_Sean_P1_ArchetypeDB_Arena_RedRoom08]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938\|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB_Arena_RedRoom10-630c1a\|BP_Sean_Burst_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB_Arena-8dabce\|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_Burst_ArchetypeDB_Arena.BP_Sean_Burst_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena_RedRoom10-7c0dd4\|BP_Sean_P1_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938\|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB_Arena_RedRoom10-0bddf5\|BP_Sean_P2_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB_Arena-f87328\|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P2_ArchetypeDB_Arena.BP_Sean_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB-06eedf\|BP_Sean_Burst_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB-1974bc\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P2_ArchetypeDB.BP_Sean_P2_ArchetypeDB_C]] | 未保存 | 未保存 | [[03配置/受击与抗性/Sean_Burst_ResistanceDB-963937\|/Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|BP_Sean_P1_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 1000 | 1350 | [[03配置/受击与抗性/Sean_ResistanceDB-6910b9\|/Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB.Sean_ResistanceDB]] | [[03配置/AI防御/Sean_ContextualDefense-78c00b\|/Game/DB/AI/Archetypes/Sean/Defenses/Sean_ContextualDefense.Sean_ContextualDefense]] |
| [[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB-1974bc\|BP_Sean_P2_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 1600 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_P3_ArchetypeDB-48b29a\|BP_Sean_P3_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_Transition_ArchetypeDB_-945a64\|BP_Sean_Transition_ArchetypeDB_]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Sean.md#BP_Sean_H0_ArchetypeDB_NoAttack-396ab0\|BP_Sean_H0_ArchetypeDB_NoAttack]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Sean_Burst_ArchetypeDB_Arena-8dabce

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/BP_Sean_Burst_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB-06eedf|/Game/DB/AI/Archetypes/Sean/BP_Sean_Burst_ArchetypeDB.BP_Sean_Burst_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_Sean_P1_ArchetypeDB_Arena-e56938

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]]

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


## BP_Sean_P2_ArchetypeDB_Arena-f87328

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P2_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB-1974bc|/Game/DB/AI/Archetypes/Sean/BP_Sean_P2_ArchetypeDB.BP_Sean_P2_ArchetypeDB_C]]

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


## BP_Sean_P1_ArchetypeDB_Arena_DanceFloor09-4d1e08

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/Specific/DanceFloor09/BP_Sean_P1_ArchetypeDB_Arena_DanceFloor09.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_bInfiniteStructure）[0] | m_bInfiniteStructure[0] | 是 | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_P1_ArchetypeDB_Arena_RedRoom08-0528cd

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/Specific/RedRoom08/BP_Sean_P1_ArchetypeDB_Arena_RedRoom08.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_Burst_ArchetypeDB_Arena_RedRoom10-630c1a

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/Specific/RedRoom10/BP_Sean_Burst_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_Burst_ArchetypeDB_Arena-8dabce|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_Burst_ArchetypeDB_Arena.BP_Sean_Burst_ArchetypeDB_Arena_C]]

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


## BP_Sean_P1_ArchetypeDB_Arena_RedRoom10-7c0dd4

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/Specific/RedRoom10/BP_Sean_P1_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB_Arena-e56938|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P1_ArchetypeDB_Arena.BP_Sean_P1_ArchetypeDB_Arena_C]]

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


## BP_Sean_P2_ArchetypeDB_Arena_RedRoom10-0bddf5

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/_Arena/Specific/RedRoom10/BP_Sean_P2_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB_Arena-f87328|/Game/DB/AI/Archetypes/Sean/_Arena/BP_Sean_P2_ArchetypeDB_Arena.BP_Sean_P2_ArchetypeDB_Arena_C]]

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


## BP_Sean_Burst_ArchetypeDB-06eedf

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/BP_Sean_Burst_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P2_ArchetypeDB-1974bc|/Game/DB/AI/Archetypes/Sean/BP_Sean_P2_ArchetypeDB.BP_Sean_P2_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Sean_Burst_ResistanceDB-963937\|/Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Sean_Burst_ResistanceDB-963937\|/Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Sean_Burst_ResistanceDB-963937\|/Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Sean/Sean_Burst_ResistanceDB.Sean_Burst_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_P1_ArchetypeDB-dc8b0d

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Sean_ResistanceDB-6910b9\|/Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB.Sean_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Sean_ResistanceDB_Easy-8f074f\|/Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB_Easy.Sean_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Sean_ResistanceDB_Hard-75b7f7\|/Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB_Hard.Sean_ResistanceDB_Hard]] |
| 情境防御 | [[03配置/AI防御/Sean_ContextualDefense-78c00b\|/Game/DB/AI/Archetypes/Sean/Defenses/Sean_ContextualDefense.Sean_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（ElementID）[0] | ElementID[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Sean | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldown[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyRecoveryPerSec[0] | -10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB.Sean_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB_Easy.Sean_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Sean/Sean_ResistanceDB_Hard.Sean_ResistanceDB_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/SeanStaff_BaseMovementDB.SeanStaff_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Sean/Sean_StructureRegenByHealth.Sean_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/Sean/Sean_StructureRegenByHealth.Sean_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/Sean/Sean_StructureRegenByHealth.Sean_StructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Sean/Defenses/Sean_ContextualDefense.Sean_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AvoidDB）[0] | m_AvoidDB[0] | /Game/DB/AI/_Shared/Avoid/BP_AvoidAbility_AI_Sean.BP_AvoidAbility_AI_Sean_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/Sean/Sean_ContextualDefense_Throwables.Sean_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | /Game/Blueprints/LDIngredients/Weapons/TwoHandedFamily/SeanStaff/BP_SeanStaff.BP_SeanStaff_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eFarFromGoalSpeedState[0] | ESpeedState::V3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fTakedownDominationBonus）[0] | m_fTakedownDominationBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCAvoidBonus）[0] | m_fSuccessfulMCAvoidBonus[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Sean | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Sean/Barks/Barks_Sean_P1.Barks_Sean_P1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/Sean/VitalPointsDBs/VitalPointDefinitionDataAsset_Sean.VitalPointDefinitionDataAsset_Sean | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（3330 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1000 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1350 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.20000005 | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_P2_ArchetypeDB-1974bc

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/BP_Sean_P2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]]

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 1500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Sean/Barks/Barks_Sean_P2.Barks_Sean_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（4991 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanBeSpared）[0] | m_bCanBeSpared[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 类默认对象[0] | m_SpareCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Shared/BP_BossSpareStructureBrokenCountCondition.BP_BossSpareStructureBrokenCountCondition_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1600 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1 | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_P3_ArchetypeDB-48b29a

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/BP_Sean_P3_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]]

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
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/SeanBarehands_BaseMovementDB.SeanBarehands_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDropAnyWeaponAtStart）[0] | m_bDropAnyWeaponAtStart[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Sean/Barks/Barks_Sean_P2.Barks_Sean_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（4991 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_Transition_ArchetypeDB_-945a64

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/BP_Sean_Transition_ArchetypeDB_.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]]

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


## BP_Sean_H0_ArchetypeDB_NoAttack-396ab0

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Variant/Hideout0/BP_Sean_H0_ArchetypeDB_NoAttack.uasset

父类：[[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]]

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
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
