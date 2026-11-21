# Fajar_ContextualDefense_Phase2：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/Defense/Fajar_ContextualDefense_Phase2.uasset

收录本资产全部 83 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_26 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_17 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 42 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_3"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_9","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_1"] |
| AIInfluence_TestSequence_1 | 未保存 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_6","Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_12"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_11 | 55 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_19"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_2"] |
| AIInfluence_TestSequence_14 | 48 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_16"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_35","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_0"] |
| AIInfluence_TestSequence_16 | 15 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_1"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_18"] |
| AIInfluence_TestSequence_17 | 40 | ["Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_3"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_0","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_14"] |
| AIInfluence_TestSequence_18 | 17 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_13"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeDodge_3"] |
| AIInfluence_TestSequence_2 | 52 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_20"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_1"] |
| AIInfluence_TestSequence_20 | 28 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_2"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_21","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_3"] |
| AIInfluence_TestSequence_21 | 30 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_4"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_23","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_22","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_4"] |
| AIInfluence_TestSequence_22 | 35 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_5"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_6"] |
| AIInfluence_TestSequence_23 | 32 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_7"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_5"] |
| AIInfluence_TestSequence_24 | 22 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_5"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_25","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_4"] |
| AIInfluence_TestSequence_25 | 24 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_17"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_1"] |
| AIInfluence_TestSequence_26 | 20 | ["Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_1"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_24","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_20"] |
| AIInfluence_TestSequence_27 | 65 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_10"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_28","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_5"] |
| AIInfluence_TestSequence_28 | 67 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_11"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_30","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_29","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_6"] |
| AIInfluence_TestSequence_29 | 72 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_12"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_7"] |
| AIInfluence_TestSequence_3 | 10 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_10"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_5","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_0"] |
| AIInfluence_TestSequence_30 | 69 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_14"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_7"] |
| AIInfluence_TestSequence_31 | 60 | ["Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_2"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_32","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_27"] |
| AIInfluence_TestSequence_32 | 62 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_2"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_3"] |
| AIInfluence_TestSequence_35 | 50 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_18"] | ["Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_2","Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_11","Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_9"] |
| AIInfluence_TestSequence_5 | 12 | 未保存 | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeDodge_6"] |
| AIInfluence_TestSequence_6 | 7 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_6"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_3"] |
| AIInfluence_TestSequence_7 | 4 | ["Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_7"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_5"] |
| AIInfluence_TestSequence_9 | 44 | ["Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_21"] | ["Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_0"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_10 | 6 | 未保存 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_11 | 7 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_12 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_13 | 10 | 1 | ["Attack.Type.Hit","Attack.Specific.HoldDizzyMax","Attack.Specific.HoldDizzy"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_14 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_16 | 6 | 未保存 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_17 | 20 | 2 | ["Attack.Specific.3Hits"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_18 | 7 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_19 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_2 | 10 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_20 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_21 | 20 | 1 | ["Attack.Specific.3Hits"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_4 | 10 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_5 | 10 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_6 | 5 | 5 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_7 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Fajar_ContextualDefense_Phase2

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_26 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_17 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 42 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_11

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 55 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_14

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_35 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 48 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_16

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_18 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_17

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 40 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_18

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeDodge_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 52 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_20

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_21 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_21

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_23 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_22 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_22

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_23

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_24

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_25

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_17 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_26

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_24 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_27

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_28 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeGuard_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 65 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_28

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_30 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_29 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 67 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_29

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 72 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_30

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 69 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_31

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.GameDifficultyInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_32 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_27 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 60 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_32

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 62 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_35

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_18 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Fajar_ContextualDefense_Phase2.AIInfluence_TestSequence_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 50 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fProbability）[0] | m_fProbability[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeDodge_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_7

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackPropertiesInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeParryDeflect_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_9

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Fajar_ContextualDefense_Phase2.AttackMemoryInfluenceTest_21 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 44 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_10

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 66 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_11

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 68 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_12

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 73 | 该字段暂保留原名；中文语义待核。 |


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
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_14

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 70 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_16

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 49 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_17

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_18

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 51 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_19

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 56 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_2

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_20

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 53 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_21

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 45 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_4

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_5

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_6

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_7

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_1

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_10

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_12

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_2

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 63 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_3

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 43 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_5

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_6

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_7

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator32 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiActionLaunchCombo_C_0

类：/Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_0.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_1

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_1.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 54 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_4

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_5

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/BP_AiActionLaunchCombo.BP_AiActionLaunchCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_5.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_6

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 75 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_7

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
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Fajar_ContextualDefense_Phase2.DefenseInfluenceNodeAvoid_7.BP_AiActionLaunchCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 71 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_9

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_InfluenceNodeName）[0] | m_InfluenceNodeName[0] | Hit - Counter (Avoid combo /w sidestep) | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 58 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_3

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_6

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_0

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 59 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_1

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 47 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_3

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_4

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_5

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 76 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Specific.3Hits | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 46 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_1

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Specific.3Hits | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 77 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_3

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 64 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_0

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_2

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 57 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_3

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_5

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_6

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_7

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 74 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_1

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_2

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 61 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_3

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 41 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
