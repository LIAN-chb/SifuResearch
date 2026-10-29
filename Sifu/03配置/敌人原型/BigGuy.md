# BigGuy：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_ArenaAdv-c928e3\|BP_BigGuy_ArchetypeDB_ArenaAdv]] | 竞技场 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]] | 330 | 390 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_ArenaBase-4bece1\|BP_BigGuy_ArchetypeDB_ArenaBase]] | 竞技场 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_ArenaMiniboss-117a88\|BP_BigGuy_ArchetypeDB_ArenaMiniboss]] | 竞技场 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArenaThePit_RagingBull_ArchetypeDB_Adv-57b21e\|BP_BigGuy_ArenaThePit_RagingBull_ArchetypeDB_Adv]] | 竞技场 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | [[03配置/AI防御/BigGuy_MiniBoss_ContextualDefense-3a17c2\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense]] |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a\|BP_BigGuy_ArchetypeDB_Adv_Master]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 310 | 370 | [[03配置/受击与抗性/BigGuy_Advanced_ResistanceDB-9d15e5\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB]] | [[03配置/AI防御/BigGuy_Advanced_ContextualDefense-cae4ad\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ContextualDefense.BigGuy_Advanced_ContextualDefense]] |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|BP_BigGuy_ArchetypeDB_Base_Master]] | 主流程目录 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 210 | 250 | [[03配置/受击与抗性/BigGuy_Base_ResistanceDB-746e1d\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB]] | [[03配置/AI防御/BigGuy_Base_ContextualDefense-49632c\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ContextualDefense.BigGuy_Base_ContextualDefense]] |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|BP_BigGuy_ArchetypeDB_Miniboss_Master]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H5_ArchetypeDB-49ad58\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H5_ArchetypeDB.BP_BigGuy_H5_ArchetypeDB_C]] | 440 | 520 | [[03配置/受击与抗性/BigGuy_MiniBossResistanceDB-51484f\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBossResistanceDB.BigGuy_MiniBossResistanceDB]] | [[03配置/AI防御/BigGuy_MiniBoss_ContextualDefense-3a17c2\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense]] |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H1-62a9c6\|BP_BigGuy_Base_ArchetypeDB_H1]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H2-144efa\|BP_BigGuy_Base_ArchetypeDB_H2]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3-bf425a\|BP_BigGuy_Base_ArchetypeDB_H3]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H4-b399dd\|BP_BigGuy_Base_ArchetypeDB_H4]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H5-fc05f3\|BP_BigGuy_Base_ArchetypeDB_H5]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H1_ArchetypeDB-4ae534\|BP_BigGuy_H1_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_ArchetypeDB-76cc13\|BP_BigGuy_H2_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H1_ArchetypeDB-4ae534\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H1_ArchetypeDB.BP_BigGuy_H1_ArchetypeDB_C]] | 320 | 380 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e\|BP_BigGuy_H3_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_ArchetypeDB-76cc13\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H2_ArchetypeDB.BP_BigGuy_H2_ArchetypeDB_C]] | 330 | 390 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H4_ArchetypeDB-1138f2\|BP_BigGuy_H4_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]] | 340 | 400 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H5_ArchetypeDB-49ad58\|BP_BigGuy_H5_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H4_ArchetypeDB-1138f2\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H4_ArchetypeDB.BP_BigGuy_H4_ArchetypeDB_C]] | 350 | 420 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H1_ArchetypeDB-e62d6c\|BP_BigGuy_Miniboss_H1_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H2_ArchetypeDB-5593e4\|BP_BigGuy_Miniboss_H2_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H3_ArchetypeDB-56241e\|BP_BigGuy_Miniboss_H3_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H4_ArchetypeDB-67ada6\|BP_BigGuy_Miniboss_H4_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H5_ArchetypeDB-3ba86b\|BP_BigGuy_Miniboss_H5_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_Faction_ArchetypeDB-5f0b72\|BP_BigGuy_H2_Faction_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_ArchetypeDB-76cc13\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H2_ArchetypeDB.BP_BigGuy_H2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3_Mute-d43128\|BP_BigGuy_Base_ArchetypeDB_H3_Mute]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3-bf425a\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H3.BP_BigGuy_Base_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_Mute_ArchetypeDB-927dc5\|BP_BigGuy_H3_Mute_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H3_Mute_ArchetypeDB-e99135\|BP_BigGuy_Miniboss_H3_Mute_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H3_ArchetypeDB-56241e\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H3_ArchetypeDB.BP_BigGuy_Miniboss_H3_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3_RagingBull-1212ba\|BP_BigGuy_Base_ArchetypeDB_H3_RagingBull]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3-bf425a\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H3.BP_BigGuy_Base_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_RagingBull_ArchetypeDB-02c60c\|BP_BigGuy_H3_RagingBull_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_BigGuy_ArchetypeDB_ArenaAdv-c928e3

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_Arena/Generic/BP_BigGuy_ArchetypeDB_ArenaAdv.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_All.Barks_BigGuy_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 390 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_ArchetypeDB_ArenaBase-4bece1

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_Arena/Generic/BP_BigGuy_ArchetypeDB_ArenaBase.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_BigGuy_ArchetypeDB_ArenaMiniboss-117a88

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_Arena/Generic/BP_BigGuy_ArchetypeDB_ArenaMiniboss.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_BigGuy_ArenaThePit_RagingBull_ArchetypeDB_Adv-57b21e

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_Arena/Specific/ThePitRagingBull/BP_BigGuy_ArenaThePit_RagingBull_ArchetypeDB_Adv.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | [[03配置/AI防御/BigGuy_MiniBoss_ContextualDefense-3a17c2\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1141 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_All.Barks_BigGuy_All | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/BigGuy_Advanced_ResistanceDB-9d15e5\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/BigGuy_Advanced_ResistanceDB-9d15e5\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/BigGuy_Advanced_ContextualDefense-cae4ad\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ContextualDefense.BigGuy_Advanced_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ContextualDefense.BigGuy_Advanced_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ContextualDefense_Throwables.BigGuy_Advanced_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H1.Barks_BigGuy_H1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 310 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 370 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/BigGuy_Base_ResistanceDB-746e1d\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/BigGuy_Base_ResistanceDB-746e1d\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/BigGuy_Base_ResistanceDB-746e1d\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/BigGuy_Base_ContextualDefense-49632c\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ContextualDefense.BigGuy_Base_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::BigGuy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Big Guy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ResistanceDB.BigGuy_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 60 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 60 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ContextualDefense.BigGuy_Base_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Base_ContextualDefense_Throwables.BigGuy_Base_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 2500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eFarFromGoalSpeedState[0] | ESpeedState::V2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eFarFromGoalSpeedState[0] | ESpeedState::V2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/ClimbLowDrop_QueryFilter.ClimbLowDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 64 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 64 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iArchetypeDifficulty）[0] | m_iArchetypeDifficulty[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | BigGuy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（130 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_All.Barks_BigGuy_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_Arena.Barks_BigGuy_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/BigGuy/VitalPointsDBs/VitalPointDefinitionDataAsset_BigGuy.VitalPointDefinitionDataAsset_BigGuy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[2] | m_FidgetDBs[2] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[3] | m_FidgetDBs[3] | /Game/DB/Fidget/AI/Combat/BigGuyCombatFidgetDB.BigGuyCombatFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 210 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1.10000002 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.29999995 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H5_ArchetypeDB-49ad58|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H5_ArchetypeDB.BP_BigGuy_H5_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/BigGuy_MiniBossResistanceDB-51484f\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBossResistanceDB.BigGuy_MiniBossResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/BigGuy_Advanced_ResistanceDB-9d15e5\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/BigGuy_MiniBossResistanceDB-51484f\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBossResistanceDB.BigGuy_MiniBossResistanceDB]] |
| 情境防御 | [[03配置/AI防御/BigGuy_MiniBoss_ContextualDefense-3a17c2\|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBossResistanceDB.BigGuy_MiniBossResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_Advanced_ResistanceDB.BigGuy_Advanced_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBossResistanceDB.BigGuy_MiniBossResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BigGuy_MiniBoss_ContextualDefense.BigGuy_MiniBoss_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_All.Barks_BigGuy_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 440 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 520 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H1-62a9c6

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H1.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H1.Barks_BigGuy_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H2-144efa

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H2.Barks_BigGuy_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H3-bf425a

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H3.Barks_BigGuy_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H4-b399dd

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H4.Barks_BigGuy_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H5-fc05f3

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Base_Master-e0ffbb|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Base_Master.BP_BigGuy_ArchetypeDB_Base_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H5.Barks_BigGuy_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H1_ArchetypeDB-4ae534

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Adv_Master-58ac0a|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Adv_Master.BP_BigGuy_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_BigGuy_H2_ArchetypeDB-76cc13

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H1_ArchetypeDB-4ae534|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H1_ArchetypeDB.BP_BigGuy_H1_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H2.Barks_BigGuy_H2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 320 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 380 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H3_ArchetypeDB-1f484e

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_ArchetypeDB-76cc13|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H2_ArchetypeDB.BP_BigGuy_H2_ArchetypeDB_C]]

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H3.Barks_BigGuy_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 390 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H4_ArchetypeDB-1138f2

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H4_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（729 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H4.Barks_BigGuy_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 340 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 400 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H5_ArchetypeDB-49ad58

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H5_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H4_ArchetypeDB-1138f2|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H4_ArchetypeDB.BP_BigGuy_H4_ArchetypeDB_C]]

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H5.Barks_BigGuy_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 350 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 420 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Miniboss_H1_ArchetypeDB-e62d6c

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H1.Barks_BigGuy_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Miniboss_H2_ArchetypeDB-5593e4

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H2.Barks_BigGuy_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Miniboss_H3_ArchetypeDB-56241e

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H3_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H3.Barks_BigGuy_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Miniboss_H4_ArchetypeDB-67ada6

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H4_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H4.Barks_BigGuy_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Miniboss_H5_ArchetypeDB-3ba86b

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H5_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_ArchetypeDB_Miniboss_Master-53ec70|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_ArchetypeDB_Miniboss_Master.BP_BigGuy_ArchetypeDB_Miniboss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_H5.Barks_BigGuy_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H2_Faction_ArchetypeDB-5f0b72

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H2Faction/BP_BigGuy_H2_Faction_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H2_ArchetypeDB-76cc13|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H2_ArchetypeDB.BP_BigGuy_H2_ArchetypeDB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInvincible）[0] | m_bInvincible[0] | 是 | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H3_Mute-d43128

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H3Mute/BP_BigGuy_Base_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3-bf425a|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H3.BP_BigGuy_Base_ArchetypeDB_H3_C]]

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


## BP_BigGuy_H3_Mute_ArchetypeDB-927dc5

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H3Mute/BP_BigGuy_H3_Mute_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]]

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


## BP_BigGuy_Miniboss_H3_Mute_ArchetypeDB-e99135

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H3Mute/BP_BigGuy_Miniboss_H3_Mute_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_Miniboss_H3_ArchetypeDB-56241e|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Miniboss_H3_ArchetypeDB.BP_BigGuy_Miniboss_H3_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/BigGuy/Barks/Barks_BigGuy_All.Barks_BigGuy_All | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_Base_ArchetypeDB_H3_RagingBull-1212ba

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H3RagingBull/BP_BigGuy_Base_ArchetypeDB_H3_RagingBull.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_Base_ArchetypeDB_H3-bf425a|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_Base_ArchetypeDB_H3.BP_BigGuy_Base_ArchetypeDB_H3_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（531 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_BigGuy_H3_RagingBull_ArchetypeDB-02c60c

来源资产：Sifu/Content/DB/AI/Archetypes/BigGuy/_MainGame/Specific/H3RagingBull/BP_BigGuy_H3_RagingBull_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BigGuy.md#BP_BigGuy_H3_ArchetypeDB-1f484e|/Game/DB/AI/Archetypes/BigGuy/_MainGame/Generic/BP_BigGuy_H3_ArchetypeDB.BP_BigGuy_H3_ArchetypeDB_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（531 字节） | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
