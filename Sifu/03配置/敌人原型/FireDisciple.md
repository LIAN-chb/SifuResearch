# FireDisciple：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_ArenaAdv-263d90\|BP_FireDisciple_ArchetypeDB_ArenaAdv]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 280 | 560 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_ArenaBase-4e8995\|BP_FireDisciple_ArchetypeDB_ArenaBase]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_ArenaMiniBoss-c0dbf5\|BP_FireDisciple_ArchetypeDB_ArenaMiniBoss]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H2_Mute_Arena-f625e8\|BP_FireDisciple_ArchetypeDB_Base_H2_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H2-7d99d1\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_H2.BP_FireDisciple_ArchetypeDB_Base_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2_Mute_Arena-d6dbd1\|BP_FireDisciple_ArchetypeDB_H2_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2-a704b1\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H2.BP_FireDisciple_ArchetypeDB_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H2_Mute_Arena-a78480\|BP_FireDisciple_ArchetypeDB_MiniBoss_H2_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H2-2c1b90\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H2.BP_FireDisciple_ArchetypeDB_MiniBoss_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|BP_FireDisciple_ArchetypeDB_Adv_Master]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]] | 270 | 540 | [[03配置/受击与抗性/FireDisciple_Adv_ResistanceDB-056f37\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Adv_ResistanceDB.FireDisciple_Adv_ResistanceDB]] | [[03配置/AI防御/FireDisciple_Adv_ContextualDefense-dc460d\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Adv_ContextualDefense.FireDisciple_Adv_ContextualDefense]] |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H2-7d99d1\|BP_FireDisciple_ArchetypeDB_Base_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H3-65bedb\|BP_FireDisciple_ArchetypeDB_Base_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H5-1343d6\|BP_FireDisciple_ArchetypeDB_Base_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126\|BP_FireDisciple_ArchetypeDB_Base_Master]] | 路径未专门标注；使用情况待查 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 160 | 320 | [[03配置/受击与抗性/FireDisciple_Base_ResistanceDB-486b1f\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Base_ResistanceDB.FireDisciple_Base_ResistanceDB]] | [[03配置/AI防御/FireDisciple_Base_ContextualDefense-76722e\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Base_ContextualDefense.FireDisciple_Base_ContextualDefense]] |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2-a704b1\|BP_FireDisciple_ArchetypeDB_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H3-6c2798\|BP_FireDisciple_ArchetypeDB_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 280 | 560 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H4-08decc\|BP_FireDisciple_ArchetypeDB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 290 | 580 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H5-00f0ef\|BP_FireDisciple_ArchetypeDB_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 300 | 600 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H2-2c1b90\|BP_FireDisciple_ArchetypeDB_MiniBoss_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H3-505ba1\|BP_FireDisciple_ArchetypeDB_MiniBoss_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H4-87a118\|BP_FireDisciple_ArchetypeDB_MiniBoss_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H5-35487e\|BP_FireDisciple_ArchetypeDB_MiniBoss_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0\|BP_FireDisciple_ArchetypeDB_MiniBoss_Master]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]] | 400 | 800 | [[03配置/受击与抗性/FireDisciple_MiniBoss_ResistanceDB-6e2656\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_MiniBoss_ResistanceDB.FireDisciple_MiniBoss_ResistanceDB]] | 本资产未保存；可能继承 |


## BP_FireDisciple_ArchetypeDB_ArenaAdv-263d90

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Generic/BP_FireDisciple_ArchetypeDB_ArenaAdv.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 110 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 280 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 560 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_ArenaBase-4e8995

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Generic/BP_FireDisciple_ArchetypeDB_ArenaBase.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FireDisciple_ArchetypeDB_ArenaMiniBoss-c0dbf5

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Generic/BP_FireDisciple_ArchetypeDB_ArenaMiniBoss.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 110 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 210 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Base_H2_Mute_Arena-f625e8

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Specific/Mute/BP_FireDisciple_ArchetypeDB_Base_H2_Mute_Arena.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_H2-7d99d1|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_H2.BP_FireDisciple_ArchetypeDB_Base_H2_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_H2_Mute_Arena-d6dbd1

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Specific/Mute/BP_FireDisciple_ArchetypeDB_H2_Mute_Arena.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2-a704b1|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H2.BP_FireDisciple_ArchetypeDB_H2_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_H2_Mute_Arena-a78480

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/_Arena/Specific/Mute/BP_FireDisciple_ArchetypeDB_MiniBoss_H2_Mute_Arena.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_H2-2c1b90|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H2.BP_FireDisciple_ArchetypeDB_MiniBoss_H2_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FireDisciple_Adv_ResistanceDB-056f37\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Adv_ResistanceDB.FireDisciple_Adv_ResistanceDB]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/FireDisciple_Adv_ResistanceDB-056f37\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Adv_ResistanceDB.FireDisciple_Adv_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/FireDisciple_Adv_ContextualDefense-dc460d\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Adv_ContextualDefense.FireDisciple_Adv_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Adv_ResistanceDB.FireDisciple_Adv_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Adv_ResistanceDB.FireDisciple_Adv_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Adv_ContextualDefense.FireDisciple_Adv_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Adv_ContextualDefense_Throwable.FireDisciple_Adv_ContextualDefense_Throwable | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1352 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H2.Barks_FireDisciple_H2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 270 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 540 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Base_H2-7d99d1

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_H2.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H2.Barks_FireDisciple_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Base_H3-65bedb

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_H3.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H3.Barks_FireDisciple_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Base_H5-1343d6

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_H5.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Base_Master-e71126|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.BP_FireDisciple_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H5.Barks_FireDisciple_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_Base_Master-e71126

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Base_Master.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FireDisciple_Base_ResistanceDB-486b1f\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Base_ResistanceDB.FireDisciple_Base_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/FireDisciple_Easy_ResistanceDB-79a759\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Easy_ResistanceDB.FireDisciple_Easy_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/FireDisciple_Base_ResistanceDB-486b1f\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Base_ResistanceDB.FireDisciple_Base_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/FireDisciple_Base_ContextualDefense-76722e\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Base_ContextualDefense.FireDisciple_Base_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Firedisciple | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Base_ResistanceDB.FireDisciple_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Easy_ResistanceDB.FireDisciple_Easy_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_Base_ResistanceDB.FireDisciple_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/FireDisciple_BaseMovementDB.FireDisciple_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_Base_ContextualDefense.FireDisciple_Base_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1352 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iArchetypeDifficulty）[0] | m_iArchetypeDifficulty[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | FireDisciple | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（130 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_All.Barks_FireDisciple_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_Arena.Barks_FireDisciple_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/FireDisciple/VitalPointsDBs/FireDisciple_VitalPointDefinitionDataAsset.FireDisciple_VitalPointDefinitionDataAsset | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（56 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fJiggleDelayRange）[0] | m_fJiggleDelayRange[0] | 未解码（548 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationContainers）[0] | m_JiggleAnimationContainers[0] | 未解码（1064 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[3] | m_FidgetDBs[3] | /Game/DB/Fidget/AI/Combat/FireDiscipleCombatFidgetDB.FireDiscipleCombatFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1.10000002 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 320 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_H2-a704b1

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FireDisciple_ArchetypeDB_H3-6c2798

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 110 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H3.Barks_FireDisciple_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 280 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 560 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_H4-08decc

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H4.Barks_FireDisciple_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 290 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 580 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_H5-00f0ef

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 130 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H5.Barks_FireDisciple_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 600 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_H2-2c1b90

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H2.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H2.Barks_FireDisciple_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_H3-505ba1

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H3.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 110 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 210 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H3.Barks_FireDisciple_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_H4-87a118

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H4.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 220 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H4.Barks_FireDisciple_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_H5-35487e

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_H5.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.BP_FireDisciple_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 130 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 230 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_ArchetypeDB_MiniBoss_Master-b148f0

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_MiniBoss_Master.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_Adv_Master-04caf4|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_Adv_Master.BP_FireDisciple_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FireDisciple_MiniBoss_ResistanceDB-6e2656\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_MiniBoss_ResistanceDB.FireDisciple_MiniBoss_ResistanceDB]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/FireDisciple_MiniBoss_ResistanceDB-6e2656\|/Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_MiniBoss_ResistanceDB.FireDisciple_MiniBoss_ResistanceDB]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_MiniBoss_ResistanceDB.FireDisciple_MiniBoss_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FireDisciple/GenericData/FireDisciple_MiniBoss_ResistanceDB.FireDisciple_MiniBoss_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_MiniBoss_ContextualDefense_Throwable.FireDisciple_MiniBoss_ContextualDefense_Throwable | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1352 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FireDisciple/Barks/Barks_FireDisciple_H5.Barks_FireDisciple_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 800 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
