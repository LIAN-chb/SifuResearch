# Yang：原型配置与引用

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/受击硬直与脱离|基础机制]]

纳入依据是已解析元数据的父类链到 /Script/Sifu.ArchetypeAsset，不只按文件名猜测。下表只列各资产自己保存的覆盖值，尚未合并父类或运行期修正；未保存不等于零。范围标签只来自路径，不证明某变体已在主流程使用。

## 原型差异总表

| 原型 | 路径范围标签 | 父类 | 本层生命字段 | 本层架势字段 | 普通难度抗性引用 | 情境防御引用 |
|---|---|---|---|---|---|---|
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566\|BP_Yang_P1_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena-32aa1b\|BP_Yang_P2_ArchetypeDB_Arena]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB-b3bf75\|/Game/DB/AI/Archetypes/Yang/_DB/Phase2/BP_Yang_P2_ArchetypeDB.BP_Yang_P2_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena_RedRoom08-cbaeda\|BP_Yang_P1_ArchetypeDB_Arena_RedRoom08]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena_RedRoom10-63cd29\|BP_Yang_P1_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena_RedRoom10-c0164f\|BP_Yang_P2_ArchetypeDB_Arena_RedRoom10]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena-32aa1b\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P2_ArchetypeDB_Arena.BP_Yang_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena_Rooftop07-1fe0af\|BP_Yang_P1_ArchetypeDB_Arena_Rooftop07]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena_Wuguan06-49cf21\|BP_Yang_P1_ArchetypeDB_Arena_Wuguan06]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena_Wuguan06-8a4504\|BP_Yang_P2_ArchetypeDB_Arena_Wuguan06]] | 竞技场 | [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena-32aa1b\|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P2_ArchetypeDB_Arena.BP_Yang_P2_ArchetypeDB_Arena_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|BP_Yang_P1_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557\|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]] | 1100 | 1400 | [[03配置/受击与抗性/Yang_ResistanceDB-f4c255\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB.Yang_ResistanceDB]] | [[03配置/AI防御/Yang_P1_Offense_ContextualDefense-413744\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Offense_ContextualDefense.Yang_P1_Offense_ContextualDefense]] |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_Defense_ArchetypeDB-c2469c\|BP_Yang_P1_Defense_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | [[03配置/AI防御/Yang_P1_Defense_ContextualDefense-5ac126\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Defense_ContextualDefense.Yang_P1_Defense_ContextualDefense]] |
| [[03配置/敌人原型/Yang.md#BP_Yang_P1_Offense_ArchetypeDB-4083b2\|BP_Yang_P1_Offense_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]] | 未保存 | 未保存 | 本资产未保存；可能继承 | 本资产未保存；可能继承 |
| [[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB-b3bf75\|BP_Yang_P2_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]] | 1300 | 1650 | 本资产未保存；可能继承 | [[03配置/AI防御/Yang_P2_ContextualDefense-0c79f1\|/Game/DB/AI/Archetypes/Yang/_DB/Phase2/Yang_P2_ContextualDefense.Yang_P2_ContextualDefense]] |
| [[03配置/敌人原型/Yang.md#BP_Yang_P3_Wude_ArchetypeDB-3f629f\|BP_Yang_P3_Wude_ArchetypeDB]] | 路径未专门标注；使用情况待查 | [[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]] | 1 | 700 | [[03配置/受击与抗性/Yang_Phase3_ResistanceDB-793950\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB]] | [[03配置/AI防御/Yang_P3_ContextualDefense-d96c4e\|/Game/DB/AI/Archetypes/Yang/_DB/Phase3/Yang_P3_ContextualDefense.Yang_P3_ContextualDefense]] |


## BP_Yang_P1_ArchetypeDB_Arena-a46566

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]]

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
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Yang_P2_ArchetypeDB_Arena-32aa1b

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P2_ArchetypeDB_Arena.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB-b3bf75|/Game/DB/AI/Archetypes/Yang/_DB/Phase2/BP_Yang_P2_ArchetypeDB.BP_Yang_P2_ArchetypeDB_C]]

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
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Yang_Phase2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1767 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 条件或对象实例[0] | m_SpareCondition[0].m_Instance[0] | Default__BP_Yang_P2_ArchetypeDB_Arena_C.BP_BossSpareStructureBrokenCountAndTagCheckCondition_C_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## BP_Yang_P1_ArchetypeDB_Arena_RedRoom08-cbaeda

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/RedRoom08/BP_Yang_P1_ArchetypeDB_Arena_RedRoom08.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]]

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


## BP_Yang_P1_ArchetypeDB_Arena_RedRoom10-63cd29

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/RedRoom10/BP_Yang_P1_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]]

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


## BP_Yang_P2_ArchetypeDB_Arena_RedRoom10-c0164f

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/RedRoom10/BP_Yang_P2_ArchetypeDB_Arena_RedRoom10.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena-32aa1b|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P2_ArchetypeDB_Arena.BP_Yang_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1767 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 条件或对象实例[0] | m_SpareCondition[0].m_Instance[0] | Default__BP_Yang_P2_ArchetypeDB_Arena_RedRoom10_C.BP_BossSpareStructureBrokenCountAndTagCheckCondition_C_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## BP_Yang_P1_ArchetypeDB_Arena_Rooftop07-1fe0af

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/Rooftop07/BP_Yang_P1_ArchetypeDB_Arena_Rooftop07.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_bHideHealthGauge）[0] | m_bHideHealthGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bHideStructureGauge）[0] | m_bHideStructureGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanAttack）[0] | m_bCanAttack[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanUseReactionActions）[0] | m_bCanUseReactionActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（53 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Yang_P1_ArchetypeDB_Arena_Wuguan06-49cf21

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/Wuguan06/BP_Yang_P1_ArchetypeDB_Arena_Wuguan06.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB_Arena-a46566|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P1_ArchetypeDB_Arena.BP_Yang_P1_ArchetypeDB_Arena_C]]

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


## BP_Yang_P2_ArchetypeDB_Arena_Wuguan06-8a4504

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_Arena/Specific/Wuguan06/BP_Yang_P2_ArchetypeDB_Arena_Wuguan06.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P2_ArchetypeDB_Arena-32aa1b|/Game/DB/AI/Archetypes/Yang/_Arena/BP_Yang_P2_ArchetypeDB_Arena.BP_Yang_P2_ArchetypeDB_Arena_C]]

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
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1767 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 条件或对象实例[0] | m_SpareCondition[0].m_Instance[0] | Default__BP_Yang_P2_ArchetypeDB_Arena_Wuguan06_C.BP_BossSpareStructureBrokenCountAndTagCheckCondition_C_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


## BP_Yang_P1_ArchetypeDB-05c96a

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.uasset

父类：[[03配置/敌人原型/BP_BossArchetypeDB.uasset.md#BP_BossArchetypeDB-246557|/Game/DB/AI/Archetypes/BP_BossArchetypeDB.BP_BossArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Yang_ResistanceDB-f4c255\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB.Yang_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Yang_ResistanceDB_Easy-ae8ea8\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB_Easy.Yang_ResistanceDB_Easy]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Yang_ResistanceDB_Hard-925806\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB_Hard.Yang_ResistanceDB_Hard]] |
| 情境防御 | [[03配置/AI防御/Yang_P1_Offense_ContextualDefense-413744\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Offense_ContextualDefense.Yang_P1_Offense_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（TakedownLeft）[0] | TakedownLeft[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eAIArchetype）[0] | m_eAIArchetype[0] | EAIArchetype::Yang | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_archetypeName）[0] | m_archetypeName[0] | Wuguan_AI_Yang_Phase1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bForceTargetWidgetDisplay）[0] | m_bForceTargetWidgetDisplay[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDismissDeathForTakedown）[0] | m_bDismissDeathForTakedown[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fGrabbableStructureRatio）[0] | m_fGrabbableStructureRatio[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyResistance[0] | 200 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryCooldown[0] | 8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[1].m_fSuperDizzyRecoveryPerSec[0] | -10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[2].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyResistance）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyResistance[0] | 350 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldown）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldown[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryCooldownWhenComplete）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryCooldownWhenComplete[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[2] → 未核中文义（m_fSuperDizzyRecoveryPerSec）[0] | m_SuperDizzyPerDifficulty[2].m_fSuperDizzyRecoveryPerSec[0] | -25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAICanSeeForever）[0] | m_bAICanSeeForever[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB.Yang_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB_Easy.Yang_ResistanceDB_Easy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_ResistanceDB_Hard.Yang_ResistanceDB_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_MovementDB）[0] | m_MovementDB[0] | /Game/DB/Movement/Archetypes/Yang_BaseMovementDB.Yang_BaseMovementDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/_Shared/Structure/AIStructureRegenByHealth_Hard.AIStructureRegenByHealth_Hard | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fParriedDuration）[0] | m_fParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureBrokenParriedDuration）[0] | m_fStructureBrokenParriedDuration[0] | 180 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Offense_ContextualDefense.Yang_P1_Offense_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1289 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（409 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[0] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[0].m_fDistToGoalThresold[0] | 400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[1] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[1].m_fDistToGoalThresold[0] | 800 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LocomotionPaceSelector）[0] → 未核中文义（m_speedStateFromGoalDistSelectors）[2] → 未核中文义（m_fDistToGoalThresold）[0] | m_LocomotionPaceSelector[0].m_speedStateFromGoalDistSelectors[2].m_fDistToGoalThresold[0] | 300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_NavigationQueryFilter）[0] | m_NavigationQueryFilter[0] | /Game/Blueprints/AI/Navigation/QueryFilters/VaultClimbLowDrop_QueryFilter.VaultClimbLowDrop_QueryFilter_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHelpSignalTriggers）[0] | m_uiHelpSignalTriggers[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiLostAttackTicketCause）[0] | m_uiLostAttackTicketCause[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fDamageReceivedToDifficultyBonus）[0] | m_fDamageReceivedToDifficultyBonus[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fTakedownDominationBonus）[0] | m_fTakedownDominationBonus[0] | 0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCParryBonus）[0] | m_fSuccessfulMCParryBonus[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fSuccessfulMCAvoidBonus）[0] | m_fSuccessfulMCAvoidBonus[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Behavior）[0] | m_Behavior[0] | /Game/Blueprints/AI/BehaviorTree/AiTreeWuguan.AiTreeWuguan | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Blackboard）[0] | m_Blackboard[0] | /Game/Blueprints/AI/Bosses/Yang/BehaviorTree/AIBlackBoard_Yang.AIBlackBoard_Yang | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VoiceArchetypeSwitchName）[0] | m_VoiceArchetypeSwitchName[0] | Yang | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Yang/Barks/Barks_Yang_P1.Barks_Yang_P1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_VitalPointDB）[0] | m_VitalPointDB[0] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_VitalPointDefinition.Yang_VitalPointDefinition | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（32 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1685 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[0] | m_FidgetDBs[0] | /Game/DB/Fidget/MC/MCExploFidgetDB.MCExploFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_FidgetDBs）[3] | m_FidgetDBs[3] | /Game/DB/Fidget/MC/MCFightFidgetDB.MCFightFidgetDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1100 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealthMultiplier）[1] | m_fHealthMultiplier[1] | 0.800000012 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1400 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructureMultiplier）[2] | m_fStructureMultiplier[2] | 1.29999995 | 该字段暂保留原名；中文语义待核。 |


## BP_Yang_P1_Defense_ArchetypeDB-c2469c

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_Defense_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | [[03配置/AI防御/Yang_P1_Defense_ContextualDefense-5ac126\|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Defense_ContextualDefense.Yang_P1_Defense_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Defense_ContextualDefense.Yang_P1_Defense_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1701 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionActions）[0] | m_ReactionActions[0] | 未解码（765 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |


## BP_Yang_P1_Offense_ArchetypeDB-4083b2

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_Offense_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]]

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


## BP_Yang_P2_ArchetypeDB-b3bf75

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase2/BP_Yang_P2_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | 本资产未保存；可能继承 |
| 简单 Easy=1 | 本资产未保存；可能继承 |
| 困难 Hard=2 | 本资产未保存；可能继承 |
| 情境防御 | [[03配置/AI防御/Yang_P2_ContextualDefense-0c79f1\|/Game/DB/AI/Archetypes/Yang/_DB/Phase2/Yang_P2_ContextualDefense.Yang_P2_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase2/Yang_P2_ContextualDefense.Yang_P2_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ReactionAttacks）[0] | m_ReactionAttacks[0] | 未解码（1767 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Yang/Barks/Barks_Yang_P2.Barks_Yang_P2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iCirclePerCombatRoles）[0] | m_iCirclePerCombatRoles[0] | 未解码（44 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bCanBeSpared）[0] | m_bCanBeSpared[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SpareCondition）[0] → 类默认对象[0] | m_SpareCondition[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Yang/BP_BossSpareStructureBrokenCountAndTagCheckCondition.BP_BossSpareStructureBrokenCountAndTagCheckCondition_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_SpareCondition）[0] → 条件或对象实例[0] | m_SpareCondition[0].m_Instance[0] | Default__BP_Yang_P2_ArchetypeDB_C.BP_BossSpareStructureBrokenCountAndTagCheckCondition_C_1 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1300 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 1650 | 该字段暂保留原名；中文语义待核。 |


## BP_Yang_P3_Wude_ArchetypeDB-3f629f

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase3/BP_Yang_P3_Wude_ArchetypeDB.uasset

父类：[[03配置/敌人原型/Yang.md#BP_Yang_P1_ArchetypeDB-05c96a|/Game/DB/AI/Archetypes/Yang/_DB/Phase1/BP_Yang_P1_ArchetypeDB.BP_Yang_P1_ArchetypeDB_C]]

### 难度抗性与防御引用

| 字段／难度 | 本层保存的引用 |
|---|---|
| 普通 Normal=0 | [[03配置/受击与抗性/Yang_Phase3_ResistanceDB-793950\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB]] |
| 简单 Easy=1 | [[03配置/受击与抗性/Yang_Phase3_ResistanceDB-793950\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB]] |
| 困难 Hard=2 | [[03配置/受击与抗性/Yang_Phase3_ResistanceDB-793950\|/Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB]] |
| 情境防御 | [[03配置/AI防御/Yang_P3_ContextualDefense-d96c4e\|/Game/DB/AI/Archetypes/Yang/_DB/Phase3/Yang_P3_ContextualDefense.Yang_P3_ContextualDefense]] |


### 本层全部已解析保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_SuperDizzyPerDifficulty）[0] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[0].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_SuperDizzyPerDifficulty）[1] → 未核中文义（m_bCanBeSuperDizzy）[0] | m_SuperDizzyPerDifficulty[1].m_bCanBeSuperDizzy[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInvincible）[0] | m_bInvincible[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bHideHealthGauge）[0] | m_bHideHealthGauge[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[0] | m_AttackPropertyResistanceDBPerDifficulty[0] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[1] | m_AttackPropertyResistanceDBPerDifficulty[1] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_AttackPropertyResistanceDBPerDifficulty）[2] | m_AttackPropertyResistanceDBPerDifficulty[2] | /Game/DB/AI/Archetypes/Yang/_DB/Generic/Yang_Phase3_ResistanceDB.Yang_Phase3_ResistanceDB | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[0] | m_GuardRecoveryRateByLifePerDifficulty[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase3/Curve_YangP3StructureRegen.Curve_YangP3StructureRegen | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[1] | m_GuardRecoveryRateByLifePerDifficulty[1] | /Game/DB/AI/Archetypes/Yang/_DB/Phase3/Curve_YangP3StructureRegen.Curve_YangP3StructureRegen | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_GuardRecoveryRateByLifePerDifficulty）[2] | m_GuardRecoveryRateByLifePerDifficulty[2] | /Game/DB/AI/Archetypes/Yang/_DB/Phase3/Curve_YangP3StructureRegen.Curve_YangP3StructureRegen | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ContextualDefense）[0] | m_ContextualDefense[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase3/Yang_P3_ContextualDefense.Yang_P3_ContextualDefense | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_difficultyLevels）[0] | m_difficultyLevels[0] | 未解码（463 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_BarksDb）[0] | m_BarksDb[0] | /Game/DB/AI/Archetypes/Yang/Barks/Barks_Yang_P3.Barks_Yang_P3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_PerRolePerCircleCombatPositionRange）[0] | m_PerRolePerCircleCombatPositionRange[0] | 未解码（1669 字节） | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fHealth）[0] | m_fHealth[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fStructure）[0] | m_fStructure[0] | 700 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/stun-ai-default-objects.json.gz（CDO 保存字段）及 inventory/package-metadata.json.gz（父类关系）。完整有效值还要递归合并父类，当前总表不冒充最终敌人属性表。
