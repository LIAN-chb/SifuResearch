# _Tests：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/_Tests.md#BP_Fajar_Phase1_NoAttack_DB-fb1a6d\|BP_Fajar_Phase1_NoAttack_DB]] | 测试 | [[03配置/敌人原型/Fajar.md#BP_Fajar_Phase1_Offensive_ArchetypeDB-32c522\|/Game/DB/AI/Archetypes/Fajar/DB/BP_Fajar_Phase1_Offensive_ArchetypeDB.BP_Fajar_Phase1_Offensive_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB-bd48de\|BP_FireDisciple_NoAttack_DB]] | 测试 | [[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2-a704b1\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H2.BP_FireDisciple_ArchetypeDB_H2_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | [[03配置/AI防御/FireDisciple_NoAttack_ContextualDefense-634ca1\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_NoAttack_ContextualDefense.FireDisciple_NoAttack_ContextualDefense]] |
| [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2-a5b224\|BP_FireDisciple_NoAttack_DB_H2]] | 测试 | [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB-bd48de\|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB.BP_FireDisciple_NoAttack_DB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2_Base-8d449b\|BP_FireDisciple_NoAttack_DB_H2_Base]] | 测试 | [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2-a5b224\|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2.BP_FireDisciple_NoAttack_DB_H2_C]] | 160 | 320 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2_Miniboss-10c7dd\|BP_FireDisciple_NoAttack_DB_H2_Miniboss]] | 测试 | [[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2-a5b224\|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2.BP_FireDisciple_NoAttack_DB_H2_C]] | 400 | 800 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_Grunt_NoAttack_DB-3ac598\|BP_Grunt_NoAttack_DB]] | 测试 | [[03配置/敌人原型/Grunt.md#BP_Grunt_ArchetypeDB_Base-f90983\|/Game/DB/AI/Archetypes/Grunt/_Base/BP_Grunt_ArchetypeDB_Base.BP_Grunt_ArchetypeDB_Base_C]] | 75 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_Sean_P1_ArchetypeDB_NoAttack-b53b29\|BP_Sean_P1_ArchetypeDB_NoAttack]] | 测试 | [[03配置/敌人原型/Sean.md#BP_Sean_P1_ArchetypeDB-dc8b0d\|/Game/DB/AI/Archetypes/Sean/BP_Sean_P1_ArchetypeDB.BP_Sean_P1_ArchetypeDB_C]] | 未保存 | 1600 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/_Tests.md#BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB-05e4ea\|BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB]] | 测试 | [[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4\|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]] | 0.100000001 | 0.100000001 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |


## BP_Fajar_Phase1_NoAttack_DB-fb1a6d

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_Fajar_Phase1_NoAttack_DB.uasset

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
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_WeaponToEquipAtStart）[0] | m_WeaponToEquipAtStart[0] | /Game/Blueprints/LDIngredients/Weapons/BladeFamily/Machete/Fajar/BP_Weapon_Machete_Fajar.BP_Weapon_Machete_Fajar_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_UsableWeapons）[0] | m_UsableWeapons[0] | 未解码（1282 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_NoAttack_DB-bd48de

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB.uasset

父类：[[03配置/敌人原型/FireDisciple.md#BP_FireDisciple_ArchetypeDB_H2-a704b1|/Game/DB/AI/Archetypes/FireDisciple/Variations/Archetype/BP_FireDisciple_ArchetypeDB_H2.BP_FireDisciple_ArchetypeDB_H2_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | [[03配置/AI防御/FireDisciple_NoAttack_ContextualDefense-634ca1\|/Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_NoAttack_ContextualDefense.FireDisciple_NoAttack_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_NoAttack_ContextualDefense.FireDisciple_NoAttack_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_eFarFromGoalSpeedState）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_eFarFromGoalSpeedState[0] | ESpeedState::V1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCAvoidBonus）[0] | m_fSuccessfulMCAvoidBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRolesInPauseOverride）[0] | m_iCirclePerCombatRolesInPauseOverride[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_NoAttack_DB_H2-a5b224

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2.uasset

父类：[[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB-bd48de|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB.BP_FireDisciple_NoAttack_DB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | 本资产未保存；可能继承 |


### 本层全部已解析保存字段
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

## BP_FireDisciple_NoAttack_DB_H2_Base-8d449b

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2_Base.uasset

父类：[[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2-a5b224|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2.BP_FireDisciple_NoAttack_DB_H2_C]]

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
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 160 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 320 | 该字段暂保留原名；中文语义待核。 |


## BP_FireDisciple_NoAttack_DB_H2_Miniboss-10c7dd

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2_Miniboss.uasset

父类：[[03配置/敌人原型/_Tests.md#BP_FireDisciple_NoAttack_DB_H2-a5b224|/Game/DB/AI/Archetypes/_Tests/NoAttack/BP_FireDisciple_NoAttack_DB_H2.BP_FireDisciple_NoAttack_DB_H2_C]]

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
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 800 | 该字段暂保留原名；中文语义待核。 |


## BP_Grunt_NoAttack_DB-3ac598

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_Grunt_NoAttack_DB.uasset

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
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（531 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 75 | 该字段暂保留原名；中文语义待核。 |


## BP_Sean_P1_ArchetypeDB_NoAttack-b53b29

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_Sean_P1_ArchetypeDB_NoAttack.uasset

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
| 未核中文义（m_bCanDefend）[0] | m_bCanDefend[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefenseAgainstThrowables）[0] | m_ContextualDefenseAgainstThrowables[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1600 | 该字段暂保留原名；中文语义待核。 |


## BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB-05e4ea

来源资产：Sifu/Content/DB/AI/Archetypes/_Tests/NoAttack/BP_Servant_Pacifist_NoAttack_NoXP_OneShot_DB.uasset

父类：[[03配置/敌人原型/Servant.md#BP_Servant_ArchetypeDB-efb8d4|/Game/DB/AI/Archetypes/Servant/BP_Servant_ArchetypeDB.BP_Servant_ArchetypeDB_C]]

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
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（475 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanLeaveAbandon）[0] | m_bCanLeaveAbandon[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | 对象索引 0；未解析引用 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 0.100000001 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 0.100000001 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
