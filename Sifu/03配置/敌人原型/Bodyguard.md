# Bodyguard：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_ArchetypeDB-0ef3dd\|Bodyguard_H3_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_Adv_Master-079d6a\|/Game/DB/AI/Archetypes/Bodyguard/_MainGame/Generic/Bodyguard_ArchetypeDB_Adv_Master.Bodyguard_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_Mute_ArchetypeDB-baa6ec\|Bodyguard_H3_Mute_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_ArchetypeDB-0ef3dd\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_ArchetypeDB.Bodyguard_H3_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H4_ArchetypeDB-f4a462\|BP_Bodyguard_H4_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_ArchetypeDB-0ef3dd\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_ArchetypeDB.Bodyguard_H3_ArchetypeDB_C]] | 330 | 660 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H5_ArchetypeDB-5a1c27\|BP_Bodyguard_H5_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H4_ArchetypeDB-f4a462\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout4/BP_Bodyguard_H4_ArchetypeDB.BP_Bodyguard_H4_ArchetypeDB_C]] | 340 | 680 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_ArenaAdv-256e5b\|Bodyguard_ArchetypeDB_ArenaAdv]] | 竞技场 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_Adv_Master-079d6a\|/Game/DB/AI/Archetypes/Bodyguard/_MainGame/Generic/Bodyguard_ArchetypeDB_Adv_Master.Bodyguard_ArchetypeDB_Adv_Master_C]] | 330 | 660 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_ArenaBase-c0ec5b\|Bodyguard_ArchetypeDB_ArenaBase]] | 竞技场 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_ArenaMiniboss-afbfe2\|Bodyguard_ArchetypeDB_ArenaMiniboss]] | 竞技场 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|Bodyguard_Base_ArchetypeDB]] | 路径未专门标注；使用情况待查 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 200 | 400 | [[03配置/受击与抗性/Bodyguard_Base_ResistanceDB-0db597\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_Base_ResistanceDB.Bodyguard_Base_ResistanceDB]] | [[03配置/AI防御/Bodyguard_Base_ContextualDefense-8d5d14\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ContextualDefense.Bodyguard_Base_ContextualDefense]] |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H3-ff7ac1\|Bodyguard_Base_ArchetypeDB_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H3_Mute-389821\|Bodyguard_Base_ArchetypeDB_H3_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H3-ff7ac1\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Hideout3/Bodyguard_Base_ArchetypeDB_H3.Bodyguard_Base_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H4-e3d7dd\|Bodyguard_Base_ArchetypeDB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H5-5edbe3\|Bodyguard_Base_ArchetypeDB_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_Adv_Master-079d6a\|Bodyguard_ArchetypeDB_Adv_Master]] | 主流程目录 | [[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]] | 320 | 640 | [[03配置/受击与抗性/Bodyguard_ResistanceDB-6fe911\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB.Bodyguard_ResistanceDB]] | [[03配置/AI防御/Bodyguard_Advanced_ContextualDefense-4f4c9a\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Bodyguard_Advanced_ContextualDefense.Bodyguard_Advanced_ContextualDefense]] |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99\|BP_Bodyguard_Miniboss_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H5_ArchetypeDB-5a1c27\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout5/BP_Bodyguard_H5_ArchetypeDB.BP_Bodyguard_H5_ArchetypeDB_C]] | 500 | 800 | [[03配置/受击与抗性/Bodyguard_MiniBoss_ResistanceDB-2a19b7\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_MiniBoss_ResistanceDB.Bodyguard_MiniBoss_ResistanceDB]] | [[03配置/AI防御/Bodyguard_Miniboss_ContextualDefense-82364d\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/Bodyguard_Miniboss_ContextualDefense.Bodyguard_Miniboss_ContextualDefense]] |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H3_ArchetypeDB-820f8c\|BP_Bodyguard_Miniboss_H3_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H3_Mute_ArchetypeDB-1d4e7d\|BP_Bodyguard_Miniboss_H3_Mute_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H3_ArchetypeDB-820f8c\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout3/BP_Bodyguard_Miniboss_H3_ArchetypeDB.BP_Bodyguard_Miniboss_H3_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H4_ArchetypeDB-504fd7\|BP_Bodyguard_Miniboss_H4_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H5_ArchetypeDB-18acdd\|BP_Bodyguard_Miniboss_H5_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## Bodyguard_H3_ArchetypeDB-0ef3dd

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_Adv_Master-079d6a|/Game/DB/AI/Archetypes/Bodyguard/_MainGame/Generic/Bodyguard_ArchetypeDB_Adv_Master.Bodyguard_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## Bodyguard_H3_Mute_ArchetypeDB-baa6ec

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_Mute_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_ArchetypeDB-0ef3dd|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_ArchetypeDB.Bodyguard_H3_ArchetypeDB_C]]

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


## BP_Bodyguard_H4_ArchetypeDB-f4a462

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout4/BP_Bodyguard_H4_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_H3_ArchetypeDB-0ef3dd|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout3/Bodyguard_H3_ArchetypeDB.Bodyguard_H3_ArchetypeDB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 280 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 280 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 280 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H4.Barks_Bodyguard_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PatrolActivities）[0] | m_PatrolActivities[0] | 未解码（283 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 660 | 该字段暂保留原名；中文语义待核。 |


## BP_Bodyguard_H5_ArchetypeDB-5a1c27

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout5/BP_Bodyguard_H5_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H4_ArchetypeDB-f4a462|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout4/BP_Bodyguard_H4_ArchetypeDB.BP_Bodyguard_H4_ArchetypeDB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 290 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 290 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 290 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H5.Barks_Bodyguard_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 340 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 680 | 该字段暂保留原名；中文语义待核。 |


## Bodyguard_ArchetypeDB_ArenaAdv-256e5b

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Arena/Generic/Bodyguard_ArchetypeDB_ArenaAdv.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_ArchetypeDB_Adv_Master-079d6a|/Game/DB/AI/Archetypes/Bodyguard/_MainGame/Generic/Bodyguard_ArchetypeDB_Adv_Master.Bodyguard_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 660 | 该字段暂保留原名；中文语义待核。 |


## Bodyguard_ArchetypeDB_ArenaBase-c0ec5b

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Arena/Generic/Bodyguard_ArchetypeDB_ArenaBase.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## Bodyguard_ArchetypeDB_ArenaMiniboss-afbfe2

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Arena/Generic/Bodyguard_ArchetypeDB_ArenaMiniboss.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## Bodyguard_Base_ArchetypeDB-42c0bc

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Bodyguard_Base_ResistanceDB-0db597\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_Base_ResistanceDB.Bodyguard_Base_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Bodyguard_ResistanceDB_Easy-cb8606\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB_Easy.Bodyguard_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Bodyguard_Base_ResistanceDB-0db597\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_Base_ResistanceDB.Bodyguard_Base_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Bodyguard_Base_ContextualDefense-8d5d14\|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ContextualDefense.Bodyguard_Base_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Bodyguard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Bodyguard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_Base_ResistanceDB.Bodyguard_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB_Easy.Bodyguard_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_Base_ResistanceDB.Bodyguard_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ContextualDefense.Bodyguard_Base_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ContextualDefense_Throwables.Bodyguard_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageReceivedToDifficultyBonus）[0] | m_fDamageReceivedToDifficultyBonus[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | BodyGuard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（130 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H3.Barks_Bodyguard_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_Arena.Barks_Bodyguard_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[3] | m_FidgetDBs[3] | /Game/DB/Fidget/AI/Combat/BodyguardCombatFidgetDB.BodyguardCombatFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 400 | 该字段暂保留原名；中文语义待核。 |


## Bodyguard_Base_ArchetypeDB_H3-ff7ac1

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Base/Hideout3/Bodyguard_Base_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## Bodyguard_Base_ArchetypeDB_H3_Mute-389821

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Base/Hideout3/Bodyguard_Base_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB_H3-ff7ac1|/Game/DB/AI/Archetypes/Bodyguard/_Base/Hideout3/Bodyguard_Base_ArchetypeDB_H3.Bodyguard_Base_ArchetypeDB_H3_C]]

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


## Bodyguard_Base_ArchetypeDB_H4-e3d7dd

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Base/Hideout4/Bodyguard_Base_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H4.Barks_Bodyguard_H4 | 该字段暂保留原名；中文语义待核。 |


## Bodyguard_Base_ArchetypeDB_H5-5edbe3

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Base/Hideout5/Bodyguard_Base_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H5.Barks_Bodyguard_H5 | 该字段暂保留原名；中文语义待核。 |


## Bodyguard_ArchetypeDB_Adv_Master-079d6a

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_MainGame/Generic/Bodyguard_ArchetypeDB_Adv_Master.uasset

父类：[[03配置/敌人原型/Bodyguard.md#Bodyguard_Base_ArchetypeDB-42c0bc|/Game/DB/AI/Archetypes/Bodyguard/_Base/Bodyguard_Base_ArchetypeDB.Bodyguard_Base_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Bodyguard_ResistanceDB-6fe911\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB.Bodyguard_ResistanceDB]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Bodyguard_ResistanceDB-6fe911\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB.Bodyguard_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Bodyguard_Advanced_ContextualDefense-4f4c9a\|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Bodyguard_Advanced_ContextualDefense.Bodyguard_Advanced_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB.Bodyguard_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_ResistanceDB.Bodyguard_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Bodyguard/_Advanced/Bodyguard_Advanced_ContextualDefense.Bodyguard_Advanced_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 320 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 640 | 该字段暂保留原名；中文语义待核。 |


## BP_Bodyguard_Miniboss_ArchetypeDB-106a99

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_H5_ArchetypeDB-5a1c27|/Game/DB/AI/Archetypes/Bodyguard/_Advanced/Hideout5/BP_Bodyguard_H5_ArchetypeDB.BP_Bodyguard_H5_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Bodyguard_MiniBoss_ResistanceDB-2a19b7\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_MiniBoss_ResistanceDB.Bodyguard_MiniBoss_ResistanceDB]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Bodyguard_MiniBoss_ResistanceDB-2a19b7\|/Game/DB/AI/Archetypes/Bodyguard/Bodyguard_MiniBoss_ResistanceDB.Bodyguard_MiniBoss_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Bodyguard_Miniboss_ContextualDefense-82364d\|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/Bodyguard_Miniboss_ContextualDefense.Bodyguard_Miniboss_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_MiniBoss_ResistanceDB.Bodyguard_MiniBoss_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Bodyguard/Bodyguard_MiniBoss_ResistanceDB.Bodyguard_MiniBoss_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Bodyguard/_Miniboss/Bodyguard_Miniboss_ContextualDefense.Bodyguard_Miniboss_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 800 | 该字段暂保留原名；中文语义待核。 |


## BP_Bodyguard_Miniboss_H3_ArchetypeDB-820f8c

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout3/BP_Bodyguard_Miniboss_H3_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H3.Barks_Bodyguard_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_Bodyguard_Miniboss_H3_Mute_ArchetypeDB-1d4e7d

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout3/BP_Bodyguard_Miniboss_H3_Mute_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_H3_ArchetypeDB-820f8c|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout3/BP_Bodyguard_Miniboss_H3_ArchetypeDB.BP_Bodyguard_Miniboss_H3_ArchetypeDB_C]]

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


## BP_Bodyguard_Miniboss_H4_ArchetypeDB-504fd7

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout4/BP_Bodyguard_Miniboss_H4_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Bodyguard/Barks/Barks_Bodyguard_H4.Barks_Bodyguard_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_Bodyguard_Miniboss_H5_ArchetypeDB-18acdd

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/Hideout5/BP_Bodyguard_Miniboss_H5_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Bodyguard.md#BP_Bodyguard_Miniboss_ArchetypeDB-106a99|/Game/DB/AI/Archetypes/Bodyguard/_Miniboss/BP_Bodyguard_Miniboss_ArchetypeDB.BP_Bodyguard_Miniboss_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
