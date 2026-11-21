# Fajar_ContextualDefense_Phase1_Offensive：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase1_Offensive.uasset

收录本资产全部 78 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_55 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_28 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_49 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_10 | 未保存 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_0"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeInvalid_1"] |
| AIInfluence_TestSequence_16 | 14 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_1"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_18"] |
| AIInfluence_TestSequence_18 | 16 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_13"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeDodge_3"] |
| AIInfluence_TestSequence_28 | 37 | ["Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_7"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_33"] |
| AIInfluence_TestSequence_29 | 43 | ["Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_6","Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_47"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_3"] |
| AIInfluence_TestSequence_3 | 9 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_10"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_5","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_0"] |
| AIInfluence_TestSequence_30 | 47 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_46"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_7"] |
| AIInfluence_TestSequence_31 | 50 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_45"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_8"] |
| AIInfluence_TestSequence_32 | 41 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_44"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_29","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_30","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_31","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_8"] |
| AIInfluence_TestSequence_33 | 39 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_43"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_32","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_4"] |
| AIInfluence_TestSequence_41 | 57 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_33"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_42","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_6"] |
| AIInfluence_TestSequence_42 | 59 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_34"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_48","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_47","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_46","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_11"] |
| AIInfluence_TestSequence_46 | 68 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_35"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_10"] |
| AIInfluence_TestSequence_47 | 65 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_36"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_12"] |
| AIInfluence_TestSequence_48 | 61 | ["Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_4","Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_37"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_5"] |
| AIInfluence_TestSequence_49 | 55 | ["Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_5"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_41"] |
| AIInfluence_TestSequence_5 | 11 | 未保存 | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeDodge_6"] |
| AIInfluence_TestSequence_50 | 21 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_38"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_51","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_9"] |
| AIInfluence_TestSequence_51 | 23 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_39"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_54","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_53","Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_52","Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_13"] |
| AIInfluence_TestSequence_52 | 32 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_40"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_11"] |
| AIInfluence_TestSequence_53 | 29 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_41"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_14"] |
| AIInfluence_TestSequence_54 | 25 | ["Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_5","Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_42"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_6"] |
| AIInfluence_TestSequence_55 | 19 | ["Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_6"] | ["Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_50"] |
| AIInfluence_TestSequence_6 | 6 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_6"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_3"] |
| AIInfluence_TestSequence_7 | 3 | ["Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_7"] | ["Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_5"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_13 | 10 | 1 | ["Attack.Type.Hit","Attack.Specific.HoldDizzyMax","Attack.Specific.HoldDizzy"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_33 | 6 | 未保存 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_34 | 5 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_35 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_36 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_37 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_38 | 10 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_39 | 10 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_40 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_41 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_42 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_43 | 6 | 未保存 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_44 | 7 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_45 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_46 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_47 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Fajar_ContextualDefense_Phase1_Offensive

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_55 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_28 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_49 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_10

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeInvalid_1 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_16

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_18 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_18

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeDodge_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_28

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_33 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_29

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_47 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 43 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_30

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_46 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 47 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_31

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_45 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 50 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_32

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_44 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_29 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_30 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 41 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_33

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_43 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_32 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_41

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_33 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_42 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 57 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_42

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_34 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_48 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_47 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_46 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 59 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_46

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_35 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 68 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_47

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 65 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_48

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_37 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 61 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_49

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_41 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 55 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fProbability）[0] | m_fProbability[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeDodge_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_50

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_38 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_51 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeGuard_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_51

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_39 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_54 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_53 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_52 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_52

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_40 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_53

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_41 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_54

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.TraversalEvasionInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Fajar_ContextualDefense_Phase1_Offensive.AttackMemoryInfluenceTest_42 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeTraversalEvasion_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_55

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.GameDifficultyInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AIInfluence_TestSequence_50 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_7

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase1_Offensive.AttackPropertiesInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeParryDeflect_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_13

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][2] | m_AttackProperties[0][2] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_33

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 58 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_34

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 60 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_35

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 69 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_36

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 66 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_37

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 63 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_38

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_39

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_40

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_41

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_42

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_43

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 40 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_44

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 42 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_45

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 51 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_46

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 48 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_47

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 45 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_0

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_1

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_10

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_6

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_7

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### DefenseInfluenceNodeAvoid_11

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 71 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_12

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][2] | m_TagsToFlushOnSuccess[0][2] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_12.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 67 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_13

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_14

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_14.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_7

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase1_Offensive.DefenseInfluenceNodeAvoid_7.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 49 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_8

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 53 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_3

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_6

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_4

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 54 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_6

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 72 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_9

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_1

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 73 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_0

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_10

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 70 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_11

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_3

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_5

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_8

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 52 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeTraversalEvasion_3

类：/Script/Sifu.DefenseInfluenceNodeTraversalEvasion

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 46 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeTraversalEvasion_5

类：/Script/Sifu.DefenseInfluenceNodeTraversalEvasion

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 64 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeTraversalEvasion_6

类：/Script/Sifu.DefenseInfluenceNodeTraversalEvasion

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_5

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 56 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_6

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_7

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### TraversalEvasionInfluenceTest_4

类：/Script/Sifu.TraversalEvasionInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eTraversalEntry）[0] | m_eTraversalEntry[0] | ETraversalEntryType::Below | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 62 | 该字段暂保留原名；中文语义待核。 |


### TraversalEvasionInfluenceTest_5

类：/Script/Sifu.TraversalEvasionInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eTraversalEntry）[0] | m_eTraversalEntry[0] | ETraversalEntryType::Below | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### TraversalEvasionInfluenceTest_6

类：/Script/Sifu.TraversalEvasionInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eTraversalEntry）[0] | m_eTraversalEntry[0] | ETraversalEntryType::Below | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 44 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
