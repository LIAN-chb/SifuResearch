# FlashKick：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaAdv-1c8cbb\|BP_FlashKick_ArchetypeDB_ArenaAdv]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]] | 240 | 420 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaBase-de62cf\|BP_FlashKick_ArchetypeDB_ArenaBase]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaMiniBoss-ba2b55\|BP_FlashKick_ArchetypeDB_ArenaMiniBoss]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4-b1156c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4.BP_FlashKick_ArchetypeDB_H4_C]] | 400 | 700 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaGhost-01cff8\|BP_FlashKick_ArchetypeDB_ArenaGhost]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 1 | 1 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaMiniBoss_Mute-3273ab\|BP_FlashKick_ArchetypeDB_ArenaMiniBoss_Mute]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaMiniBoss-ba2b55\|/Game/DB/AI/Archetypes/FlashKick/_Arena/Generic/BP_FlashKick_ArchetypeDB_ArenaMiniBoss.BP_FlashKick_ArchetypeDB_ArenaMiniBoss_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute_Arena-7b9075\|BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3_MiniBoss.BP_FlashKick_ArchetypeDB_H3_MiniBoss_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_Mute_Arena-2b2ad4\|BP_FlashKick_ArchetypeDB_H3_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3_Mute_Arena-6ec95c\|BP_FlashKick_Base_ArchetypeDB_H3_Mute_Arena]] | 竞技场 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3-85f952\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H3.BP_FlashKick_Base_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_Adv_Master-597b2b\|BP_FlashKick_ArchetypeDB_Adv_Master]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 230 | 400 | [[03配置/受击与抗性/FlashKick_ResistanceDB_Adv-95f73a\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB_Adv.FlashKick_ResistanceDB_Adv]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c\|BP_FlashKick_ArchetypeDB_H2]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_Adv_Master-597b2b\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_Adv_Master.BP_FlashKick_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2_MiniBoss-74a97c\|BP_FlashKick_ArchetypeDB_H2_MiniBoss]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|BP_FlashKick_ArchetypeDB_H3]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]] | 240 | 420 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a\|BP_FlashKick_ArchetypeDB_H3_MiniBoss]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4-b1156c\|BP_FlashKick_ArchetypeDB_H4]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]] | 250 | 435 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4_MiniBoss-d72b3e\|BP_FlashKick_ArchetypeDB_H4_MiniBoss]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H5-d65f77\|BP_FlashKick_ArchetypeDB_H5]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4-b1156c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4.BP_FlashKick_ArchetypeDB_H4_C]] | 260 | 455 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H5_MiniBoss-f702db\|BP_FlashKick_ArchetypeDB_H5_MiniBoss]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166\|BP_FlashKick_ArchetypeDB_MiniBoss_Master]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_Adv_Master-597b2b\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_Adv_Master.BP_FlashKick_ArchetypeDB_Adv_Master_C]] | 400 | 700 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|BP_FlashKick_Base_ArchetypeDB]] | 主流程目录 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 未保存 | 210 | [[03配置/受击与抗性/FlashKick_ResistanceDB-90c7a9\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB]] | [[03配置/AI防御/FlashKick_ContextualDefense-d58632\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ContextualDefense.FlashKick_ContextualDefense]] |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H2-ddb0c3\|BP_FlashKick_Base_ArchetypeDB_H2]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3-85f952\|BP_FlashKick_Base_ArchetypeDB_H3]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H4-556f07\|BP_FlashKick_Base_ArchetypeDB_H4]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H5-402210\|BP_FlashKick_Base_ArchetypeDB_H5]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed-1be87f\|BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]] | 180 | 290 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Base-3a6c52\|BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Base]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H2-ddb0c3\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H2.BP_FlashKick_Base_ArchetypeDB_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Miniboss-a49c38\|BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Miniboss]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2_MiniBoss-74a97c\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2_MiniBoss.BP_FlashKick_ArchetypeDB_H2_MiniBoss_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashBlade_ArchetypeDB-88970f\|BP_FlashBlade_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]] | 220 | 385 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashBlade_Base_ArchetypeDB-e425ef\|BP_FlashBlade_Base_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]] | 180 | 315 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashBlade_MiniBoss_ArchetypeDB-6ddbc7\|BP_FlashBlade_MiniBoss_ArchetypeDB]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashBlade_ArchetypeDB-88970f\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/BP_FlashBlade_ArchetypeDB.BP_FlashBlade_ArchetypeDB_C]] | 400 | 700 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute-60ee32\|BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3_MiniBoss.BP_FlashKick_ArchetypeDB_H3_MiniBoss_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_Mute-fc91b7\|BP_FlashKick_ArchetypeDB_H3_Mute]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3_Mute-ab47b4\|BP_FlashKick_Base_ArchetypeDB_H3_Mute]] | 主流程目录 | [[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3-85f952\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H3.BP_FlashKick_Base_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_FlashKick_ArchetypeDB_ArenaAdv-1c8cbb

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Generic/BP_FlashKick_ArchetypeDB_ArenaAdv.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]]

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
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 240 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 420 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_ArenaBase-de62cf

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Generic/BP_FlashKick_ArchetypeDB_ArenaBase.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FlashKick_ArchetypeDB_ArenaMiniBoss-ba2b55

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Generic/BP_FlashKick_ArchetypeDB_ArenaMiniBoss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4-b1156c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4.BP_FlashKick_ArchetypeDB_H4_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H3.Barks_Flashkick_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 700 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_ArenaGhost-01cff8

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Specific/Ghost/BP_FlashKick_ArchetypeDB_ArenaGhost.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

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
| 未核中文义（m_bHideHealthGauge）[0] | m_bHideHealthGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bHideStructureGauge）[0] | m_bHideStructureGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H3.Barks_Flashkick_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_ArenaMiniBoss_Mute-3273ab

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Specific/MinibossMute/BP_FlashKick_ArchetypeDB_ArenaMiniBoss_Mute.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_ArenaMiniBoss-ba2b55|/Game/DB/AI/Archetypes/FlashKick/_Arena/Generic/BP_FlashKick_ArchetypeDB_ArenaMiniBoss.BP_FlashKick_ArchetypeDB_ArenaMiniBoss_C]]

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


## BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute_Arena-7b9075

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Specific/Mute/BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute_Arena.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3_MiniBoss.BP_FlashKick_ArchetypeDB_H3_MiniBoss_C]]

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


## BP_FlashKick_ArchetypeDB_H3_Mute_Arena-2b2ad4

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Specific/Mute/BP_FlashKick_ArchetypeDB_H3_Mute_Arena.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]]

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


## BP_FlashKick_Base_ArchetypeDB_H3_Mute_Arena-6ec95c

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_Arena/Specific/Mute/BP_FlashKick_Base_ArchetypeDB_H3_Mute_Arena.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3-85f952|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H3.BP_FlashKick_Base_ArchetypeDB_H3_C]]

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


## BP_FlashKick_ArchetypeDB_Adv_Master-597b2b

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_Adv_Master.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FlashKick_ResistanceDB_Adv-95f73a\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB_Adv.FlashKick_ResistanceDB_Adv]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/FlashKick_ResistanceDB_Adv-95f73a\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB_Adv.FlashKick_ResistanceDB_Adv]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB_Adv.FlashKick_ResistanceDB_Adv | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB_Adv.FlashKick_ResistanceDB_Adv | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ContextualDefense_Throwables.FlashKick_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1009 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（85 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H2.Barks_Flashkick_H2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 230 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 400 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H2-384e2c

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_Adv_Master-597b2b|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_Adv_Master.BP_FlashKick_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FlashKick_ArchetypeDB_H2_MiniBoss-74a97c

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2_MiniBoss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FlashKick_ArchetypeDB_H3-18ba60

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H3.Barks_Flashkick_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 240 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 420 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3_MiniBoss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H3.Barks_Flashkick_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H4-b1156c

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H4.Barks_Flashkick_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 435 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H4_MiniBoss-d72b3e

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4_MiniBoss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H4.Barks_Flashkick_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H5-d65f77

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H4-b1156c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H4.BP_FlashKick_ArchetypeDB_H4_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H5.Barks_Flashkick_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 260 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 455 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H5_MiniBoss-f702db

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H5_MiniBoss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.BP_FlashKick_ArchetypeDB_MiniBoss_Master_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H5.Barks_Flashkick_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_MiniBoss_Master-cb8166

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_MiniBoss_Master.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_Adv_Master-597b2b|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_Adv_Master.BP_FlashKick_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Flashkick_ResistanceDB_Miniboss-60525e\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/Flashkick_ResistanceDB_Miniboss.Flashkick_ResistanceDB_Miniboss | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 700 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_Base_ArchetypeDB-15df04

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FlashKick_ResistanceDB-90c7a9\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/FlashKick_ResistanceDB-90c7a9\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/FlashKick_ResistanceDB-90c7a9\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/FlashKick_ContextualDefense-d58632\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ContextualDefense.FlashKick_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Flashkick | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ResistanceDB.FlashKick_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/FlashkickStructureRegenByHealth.FlashkickStructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/FlashKick/FlashkickStructureRegenByHealth.FlashkickStructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/FlashkickStructureRegenByHealth.FlashkickStructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ContextualDefense.FlashKick_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableThrowablesFromGround）[0] | m_UsableThrowablesFromGround[0] | 未解码（12 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（465 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（963 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 700 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Flashkick | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（130 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_All.Barks_Flashkick_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_Arena.Barks_Flashkick_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（20 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fJiggleDelayRange）[0] | m_fJiggleDelayRange[0] | 未解码（548 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationContainers）[0] | m_JiggleAnimationContainers[0] | 未解码（2075 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间下界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].LowerBound[0].Value[0] | 0.899999976 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间上界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].UpperBound[0].Value[0] | 1.10000002 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_FidgetDBs）[3] | m_FidgetDBs[3] | /Game/DB/Fidget/AI/Combat/FlashKickCombatFidgetDB.FlashKickCombatFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[2] | m_fHealthMultiplier[2] | 1.29999995 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 210 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.29999995 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_Base_ArchetypeDB_H2-ddb0c3

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H2.Barks_Flashkick_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_Base_ArchetypeDB_H3-85f952

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H3.Barks_Flashkick_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_Base_ArchetypeDB_H4-556f07

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H4.Barks_Flashkick_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_Base_ArchetypeDB_H5-402210

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB-15df04|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB.BP_FlashKick_Base_ArchetypeDB_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/FlashKick/Barks/Barks_Flashkick_H5.Barks_Flashkick_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed-1be87f

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H2Dancefloor/BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2-384e2c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2.BP_FlashKick_ArchetypeDB_H2_C]]

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
| 未核中文义（m_fDamageMultiplier）[0] | m_fDamageMultiplier[0] | 1.05999994 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 170 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 290 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Base-3a6c52

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H2Dancefloor/BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Base.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H2-ddb0c3|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H2.BP_FlashKick_Base_ArchetypeDB_H2_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1009 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Miniboss-a49c38

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H2Dancefloor/BP_FlashKick_ArchetypeDB_DanceFloor_AllTraversalAllowed_Miniboss.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H2_MiniBoss-74a97c|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H2_MiniBoss.BP_FlashKick_ArchetypeDB_H2_MiniBoss_C]]

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
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashBlade_ArchetypeDB-88970f

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/BP_FlashBlade_ArchetypeDB.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/Sounds/Dialogs/DBs/Barks/Flashkick/AdditionalBarks_Flashkick_Hideout3.AdditionalBarks_Flashkick_Hideout3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 220 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 385 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashBlade_Base_ArchetypeDB-e425ef

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/BP_FlashBlade_Base_ArchetypeDB.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/FlashBlade_ResistanceDB-291805\|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB]] |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/FlashBlade_ResistanceDB.FlashBlade_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/Sounds/Dialogs/DBs/Barks/Flashkick/AdditionalBarks_Flashkick_Hideout3.AdditionalBarks_Flashkick_Hideout3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 315 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashBlade_MiniBoss_ArchetypeDB-6ddbc7

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/BP_FlashBlade_MiniBoss_ArchetypeDB.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashBlade_ArchetypeDB-88970f|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Flashblade/BP_FlashBlade_ArchetypeDB.BP_FlashBlade_ArchetypeDB_C]]

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 700 | 该字段暂保留原名；中文语义待核。 |


## BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute-60ee32

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Mute/BP_FlashKick_ArchetypeDB_H3_MiniBoss_Mute.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3_MiniBoss-b31f8a|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3_MiniBoss.BP_FlashKick_ArchetypeDB_H3_MiniBoss_C]]

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


## BP_FlashKick_ArchetypeDB_H3_Mute-fc91b7

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Mute/BP_FlashKick_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_ArchetypeDB_H3-18ba60|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_ArchetypeDB_H3.BP_FlashKick_ArchetypeDB_H3_C]]

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


## BP_FlashKick_Base_ArchetypeDB_H3_Mute-ab47b4

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Specific/H3Mute/BP_FlashKick_Base_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/FlashKick.md#BP_FlashKick_Base_ArchetypeDB_H3-85f952|/Game/DB/AI/Archetypes/FlashKick/_MainGame/Generic/BP_FlashKick_Base_ArchetypeDB_H3.BP_FlashKick_Base_ArchetypeDB_H3_C]]

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


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
