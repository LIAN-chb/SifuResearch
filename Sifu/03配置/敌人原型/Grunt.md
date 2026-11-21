# Grunt：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/状态与眩晕/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H1-e42a8c\|BP_Grunt_ArchetypeDB_H1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Adv_Master-eec0b4\|/Game/DB/AI/Archetypes/Grunt/_MainGame/Generic/BP_Grunt_ArchetypeDB_Adv_Master.BP_Grunt_ArchetypeDB_Adv_Master_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2-9c9ac7\|BP_Grunt_ArchetypeDB_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H1-e42a8c\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout1/BP_Grunt_ArchetypeDB_H1.BP_Grunt_ArchetypeDB_H1_C]] | 210 | 315 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2_Faction-d37d33\|BP_Grunt_ArchetypeDB_H2_Faction]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2-9c9ac7\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2.BP_Grunt_ArchetypeDB_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3-f86e9e\|BP_Grunt_ArchetypeDB_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2-9c9ac7\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2.BP_Grunt_ArchetypeDB_H2_C]] | 220 | 330 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3_Mute-48df6d\|BP_Grunt_ArchetypeDB_H3_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3-f86e9e\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3.BP_Grunt_ArchetypeDB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3_Mute_NoLowStructure-8a55cd\|BP_Grunt_ArchetypeDB_H3_Mute_NoLowStructure]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3_Mute-48df6d\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3_Mute.BP_Grunt_ArchetypeDB_H3_Mute_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H4-99463a\|BP_Grunt_ArchetypeDB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3-f86e9e\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3.BP_Grunt_ArchetypeDB_H3_C]] | 230 | 345 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Climb_ArchetypeDB_H4-3ad07e\|BP_Grunt_Climb_ArchetypeDB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H4-99463a\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_ArchetypeDB_H4.BP_Grunt_ArchetypeDB_H4_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H5-d1e06f\|BP_Grunt_ArchetypeDB_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H4-99463a\|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_ArchetypeDB_H4.BP_Grunt_ArchetypeDB_H4_C]] | 240 | 360 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_ArenaAdv-885218\|BP_Grunt_ArchetypeDB_ArenaAdv]] | 竞技场 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Adv_Master-eec0b4\|/Game/DB/AI/Archetypes/Grunt/_MainGame/Generic/BP_Grunt_ArchetypeDB_Adv_Master.BP_Grunt_ArchetypeDB_Adv_Master_C]] | 220 | 330 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_ArenaBase-f35cc4\|BP_Grunt_ArchetypeDB_ArenaBase]] | 竞技场 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_ArenaMiniboss-13e35f\|BP_Grunt_ArchetypeDB_ArenaMiniboss]] | 竞技场 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]] | 330 | 495 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastManDB_Arena-110af2\|BP_Grunt_LastManDB_Arena]] | 竞技场 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|BP_Grunt_ArchetypeDB_Base]] | 路径未专门标注；使用情况待查 | /Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C | 100 | 150 | [[03配置/受击与抗性/Grunt_Base_ResistanceDB-5fd6b9\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB]] | [[03配置/AI防御/Grunt_Base_ContextualDefense-4f1dab\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Base_ContextualDefense.Grunt_Base_ContextualDefense]] |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Qiaoge_Phase1-ac345a\|BP_Grunt_ArchetypeDB_Qiaoge_Phase1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 120 | 200 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Qiaoge_Phase2-5559d0\|BP_Grunt_ArchetypeDB_Qiaoge_Phase2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Qiaoge_Phase1-ac345a\|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout0/Special/BP_Grunt_ArchetypeDB_Qiaoge_Phase1.BP_Grunt_ArchetypeDB_Qiaoge_Phase1_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H1-883678\|BP_Grunt_ArchetypeDB_Base_H1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_Faction_H2-b128ea\|BP_Grunt_ArchetypeDB_Base_Faction_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H2-3a44aa\|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout2/BP_Grunt_ArchetypeDB_Base_H2.BP_Grunt_ArchetypeDB_Base_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H2-3a44aa\|BP_Grunt_ArchetypeDB_Base_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H3-30342c\|BP_Grunt_ArchetypeDB_Base_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H3_Mute-bd23dc\|BP_Grunt_ArchetypeDB_Base_H3_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H3-30342c\|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_H3.BP_Grunt_ArchetypeDB_Base_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_Mute-2eca5f\|BP_Grunt_ArchetypeDB_Base_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_Mute_NoLowStructure-148802\|BP_Grunt_ArchetypeDB_Base_Mute_NoLowStructure]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_Mute-2eca5f\|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_Mute.BP_Grunt_ArchetypeDB_Base_Mute_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H4-c37a60\|BP_Grunt_ArchetypeDB_Base_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Climb_ArchetypeDB_H4_Base-48c974\|BP_Grunt_Climb_ArchetypeDB_H4_Base]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H4-c37a60\|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout4/BP_Grunt_ArchetypeDB_Base_H4.BP_Grunt_ArchetypeDB_Base_H4_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H5-500a75\|BP_Grunt_ArchetypeDB_Base_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Adv_Master-eec0b4\|BP_Grunt_ArchetypeDB_Adv_Master]] | 主流程目录 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 200 | 300 | [[03配置/受击与抗性/Grunt_Adv_ResistanceDB-a07f01\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB]] | [[03配置/AI防御/Grunt_Adv_ContextualDefense-df9d13\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense]] |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|BP_Grunt_Miniboss_DB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 160 | 240 | [[03配置/受击与抗性/Grunt_Miniboss_ResistanceDb-f607a5\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ResistanceDb.Grunt_Miniboss_ResistanceDb]] | [[03配置/AI防御/Grunt_Adv_ContextualDefense-df9d13\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense]] |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db_H1-907f11\|BP_Grunt_LastMan_Db_H1]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db_H2-bbea93\|BP_Grunt_LastMan_Db_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H2-074c80\|BP_Grunt_Miniboss_DB_H2]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]] | 310 | 465 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db_H3-53e3bd\|BP_Grunt_LastMan_Db_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H3-c48551\|BP_Grunt_Miniboss_DB_H3]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]] | 320 | 480 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H3_Mute-d67634\|BP_Grunt_Miniboss_DB_H3_Mute]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H3-c48551\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout3/BP_Grunt_Miniboss_DB_H3.BP_Grunt_Miniboss_DB_H3_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Climb_ArchetypeDB_H4_Miniboss-105a44\|BP_Grunt_Climb_ArchetypeDB_H4_Miniboss]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H4-ae6af1\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Miniboss_DB_H4.BP_Grunt_Miniboss_DB_H4_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db_H4-671c25\|BP_Grunt_LastMan_Db_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H4-ae6af1\|BP_Grunt_Miniboss_DB_H4]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]] | 330 | 495 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db_H5-89e338\|BP_Grunt_LastMan_Db_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H5-7c7340\|BP_Grunt_Miniboss_DB_H5]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H4-ae6af1\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Miniboss_DB_H4.BP_Grunt_Miniboss_DB_H4_C]] | 340 | 510 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d\|BP_Grunt_LastMan_Db]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]] | 300 | 450 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Grunt_ArchetypeDB_H1-e42a8c

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout1/BP_Grunt_ArchetypeDB_H1.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Adv_Master-eec0b4|/Game/DB/AI/Archetypes/Grunt/_MainGame/Generic/BP_Grunt_ArchetypeDB_Adv_Master.BP_Grunt_ArchetypeDB_Adv_Master_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_Grunt_ArchetypeDB_H2-9c9ac7

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H1-e42a8c|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout1/BP_Grunt_ArchetypeDB_H1.BP_Grunt_ArchetypeDB_H1_C]]

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
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H2.Barks_Grunt_H2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 210 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 315 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_H2_Faction-d37d33

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2_Faction.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2-9c9ac7|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2.BP_Grunt_ArchetypeDB_H2_C]]

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


## BP_Grunt_ArchetypeDB_H3-f86e9e

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H2-9c9ac7|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout2/BP_Grunt_ArchetypeDB_H2.BP_Grunt_ArchetypeDB_H2_C]]

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 70 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H3.Barks_Grunt_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 220 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 330 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_H3_Mute-48df6d

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3_Mute.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3-f86e9e|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3.BP_Grunt_ArchetypeDB_H3_C]]

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


## BP_Grunt_ArchetypeDB_H3_Mute_NoLowStructure-8a55cd

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3_Mute_NoLowStructure.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3_Mute-48df6d|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3_Mute.BP_Grunt_ArchetypeDB_H3_Mute_C]]

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
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_H4-99463a

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H3-f86e9e|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout3/BP_Grunt_ArchetypeDB_H3.BP_Grunt_ArchetypeDB_H3_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 230 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 345 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Climb_ArchetypeDB_H4-3ad07e

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_Climb_ArchetypeDB_H4.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H4-99463a|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_ArchetypeDB_H4.BP_Grunt_ArchetypeDB_H4_C]]

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
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_H5-d1e06f

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Hideout5/BP_Grunt_ArchetypeDB_H5.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_H4-99463a|/Game/DB/AI/Archetypes/Grunt/_Advanced/Hideout4/BP_Grunt_ArchetypeDB_H4.BP_Grunt_ArchetypeDB_H4_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 190 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 140 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 190 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 80 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H5.Barks_Grunt_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 240 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 360 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_ArenaAdv-885218

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Arena/Generic/BP_Grunt_ArchetypeDB_ArenaAdv.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Adv_Master-eec0b4|/Game/DB/AI/Archetypes/Grunt/_MainGame/Generic/BP_Grunt_ArchetypeDB_Adv_Master.BP_Grunt_ArchetypeDB_Adv_Master_C]]

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
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 220 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 330 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_ArenaBase-f35cc4

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Arena/Generic/BP_Grunt_ArchetypeDB_ArenaBase.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_Grunt_ArchetypeDB_ArenaMiniboss-13e35f

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Arena/Generic/BP_Grunt_ArchetypeDB_ArenaMiniboss.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 260 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 495 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastManDB_Arena-110af2

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Arena/Generic/BP_Grunt_LastManDB_Arena.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_Grunt_ArchetypeDB_Base-f90983

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.uasset

父类：/Game/DB/AI/_Shared/BP_Base_ArchetypeDB.BP_Base_ArchetypeDB_C

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Grunt_Base_ResistanceDB-5fd6b9\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Grunt_Base_ResistanceDB-5fd6b9\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Grunt_Base_ResistanceDB-5fd6b9\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Grunt_Base_ContextualDefense-4f1dab\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Base_ContextualDefense.Grunt_Base_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Grunt | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.Grunt_Base_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Grunt/GruntStructureRegenByHealth.GruntStructureRegenByHealth | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Base_ContextualDefense.Grunt_Base_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（3986 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（541 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 700 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eNearFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eNearFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 500 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Grunt | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（154 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_All.Barks_Grunt_All | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDBArena）[0] | m_BarksDBArena[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_Arena.Barks_Grunt_Arena | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationContainers）[0] | m_JiggleAnimationContainers[0] | 未解码（1064 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间下界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].LowerBound[0].Value[0] | 0.899999976 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_JiggleAnimationsRateModifierRange）[0] → 区间上界[0] → 端点保存值[0] | m_JiggleAnimationsRateModifierRange[0].UpperBound[0].Value[0] | 1.10000002 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 150 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Qiaoge_Phase1-ac345a

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout0/Special/BP_Grunt_ArchetypeDB_Qiaoge_Phase1.uasset

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
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::NonOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 200 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Qiaoge_Phase2-5559d0

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout0/Special/BP_Grunt_ArchetypeDB_Qiaoge_Phase2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Qiaoge_Phase1-ac345a|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout0/Special/BP_Grunt_ArchetypeDB_Qiaoge_Phase1.BP_Grunt_ArchetypeDB_Qiaoge_Phase1_C]]

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
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_H1-883678

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout1/BP_Grunt_ArchetypeDB_Base_H1.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H1.Barks_Grunt_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_Faction_H2-b128ea

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout2/BP_Grunt_ArchetypeDB_Base_Faction_H2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H2-3a44aa|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout2/BP_Grunt_ArchetypeDB_Base_H2.BP_Grunt_ArchetypeDB_Base_H2_C]]

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


## BP_Grunt_ArchetypeDB_Base_H2-3a44aa

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout2/BP_Grunt_ArchetypeDB_Base_H2.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H2.Barks_Grunt_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_H3-30342c

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_H3.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H3.Barks_Grunt_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_H3_Mute-bd23dc

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_H3_Mute.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H3-30342c|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_H3.BP_Grunt_ArchetypeDB_Base_H3_C]]

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


## BP_Grunt_ArchetypeDB_Base_Mute-2eca5f

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_Mute.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_Mute_NoLowStructure-148802

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_Mute_NoLowStructure.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_Mute-2eca5f|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout3/BP_Grunt_ArchetypeDB_Base_Mute.BP_Grunt_ArchetypeDB_Base_Mute_C]]

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
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_H4-c37a60

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout4/BP_Grunt_ArchetypeDB_Base_H4.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Climb_ArchetypeDB_H4_Base-48c974

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout4/BP_Grunt_Climb_ArchetypeDB_H4_Base.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base_H4-c37a60|/Game/DB/AI/Archetypes/Grunt/_Base/Hideout4/BP_Grunt_ArchetypeDB_Base_H4.BP_Grunt_ArchetypeDB_Base_H4_C]]

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
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbDrop_QueryFilter.VaultClimbDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Base_H5-500a75

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Hideout5/BP_Grunt_ArchetypeDB_Base_H5.uasset

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H5.Barks_Grunt_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_ArchetypeDB_Adv_Master-eec0b4

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_MainGame/Generic/BP_Grunt_ArchetypeDB_Adv_Master.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Grunt_Adv_ResistanceDB-a07f01\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Grunt_Adv_ResistanceDB-a07f01\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Grunt_Adv_ResistanceDB-a07f01\|/Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Grunt_Adv_ContextualDefense-df9d13\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsAdvancedArchetype）[0] | IsAdvancedArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.Grunt_Adv_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 60 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（3950 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H1.Barks_Grunt_H1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 300 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB-d441a2

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Grunt_Miniboss_ResistanceDb-f607a5\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ResistanceDb.Grunt_Miniboss_ResistanceDb]] |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | [[03配置/受击与抗性/Grunt_Miniboss_ResistanceDb-f607a5\|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ResistanceDb.Grunt_Miniboss_ResistanceDb]] |
| 情境防御 | [[03配置/AI防御/Grunt_Adv_ContextualDefense-df9d13\|/Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（IsMinibossArchetype）[0] | IsMinibossArchetype[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 150 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ResistanceDb.Grunt_Miniboss_ResistanceDb | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ResistanceDb.Grunt_Miniboss_ResistanceDb | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 250 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLowStructureOnSpawn）[0] | m_bLowStructureOnSpawn[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.Grunt_Adv_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | /Game/DB/AI/Archetypes/Grunt/_Miniboss/Grunt_Miniboss_ContextualDefense_Throwables.Grunt_Miniboss_ContextualDefense_Throwables | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（3950 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableThrowablesFromGround）[0] | m_UsableThrowablesFromGround[0] | 未解码（8 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（597 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceVariationsSwitchValuesPerGenderMap）[0] | m_VoiceVariationsSwitchValuesPerGenderMap[0] | 未解码（16 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 240 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastMan_Db_H1-907f11

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout1/BP_Grunt_LastMan_Db_H1.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H1.Barks_Grunt_H1 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastMan_Db_H2-bbea93

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout2/BP_Grunt_LastMan_Db_H2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H2.Barks_Grunt_H2 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB_H2-074c80

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout2/BP_Grunt_Miniboss_DB_H2.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H2.Barks_Grunt_H2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 310 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 465 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastMan_Db_H3-53e3bd

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout3/BP_Grunt_LastMan_Db_H3.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H3.Barks_Grunt_H3 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB_H3-c48551

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout3/BP_Grunt_Miniboss_DB_H3.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 260 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H3.Barks_Grunt_H3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 320 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 480 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB_H3_Mute-d67634

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout3/BP_Grunt_Miniboss_DB_H3_Mute.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H3-c48551|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout3/BP_Grunt_Miniboss_DB_H3.BP_Grunt_Miniboss_DB_H3_C]]

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


## BP_Grunt_Climb_ArchetypeDB_H4_Miniboss-105a44

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Climb_ArchetypeDB_H4_Miniboss.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H4-ae6af1|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Miniboss_DB_H4.BP_Grunt_Miniboss_DB_H4_C]]

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


## BP_Grunt_LastMan_Db_H4-671c25

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_LastMan_Db_H4.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB_H4-ae6af1

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Miniboss_DB_H4.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]]

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
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[0].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iXPBonus）[0] | m_iXPBonus[0] | 260 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H4.Barks_Grunt_H4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 330 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 495 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastMan_Db_H5-89e338

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout5/BP_Grunt_LastMan_Db_H5.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_LastMan_Db-efb37d|/Game/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.BP_Grunt_LastMan_Db_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H5.Barks_Grunt_H5 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_Miniboss_DB_H5-7c7340

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/Hideout5/BP_Grunt_Miniboss_DB_H5.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB_H4-ae6af1|/Game/DB/AI/Archetypes/Grunt/_Miniboss/Hideout4/BP_Grunt_Miniboss_DB_H4.BP_Grunt_Miniboss_DB_H4_C]]

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
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Grunt/Barks/Barks_Grunt_H5.Barks_Grunt_H5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 340 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 510 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_LastMan_Db-efb37d

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/_Miniboss/LastMan/BP_Grunt_LastMan_Db.uasset

父类：[[03配置/敌人原型/Grunt.md#BP_Grunt_Miniboss_DB-d441a2|/Game/DB/AI/Archetypes/Grunt/_Miniboss/BP_Grunt_Miniboss_DB.BP_Grunt_Miniboss_DB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | LM_Boss | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 120 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDropAnyWeaponAtStart）[0] | m_bDropAnyWeaponAtStart[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eRoleAffinity）[0] | m_eRoleAffinity[0] | ESCAICombatRoles::DirectOpponent | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 450 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
