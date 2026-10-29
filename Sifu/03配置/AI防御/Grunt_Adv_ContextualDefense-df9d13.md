# Grunt_Adv_ContextualDefense：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/Defense/Grunt_Adv_ContextualDefense.uasset

收录本资产全部 66 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_35 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][9] | m_Nodes[0][9] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][10] | m_Nodes[0][10] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_1 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 53 | ["Grunt_Adv_ContextualDefense.StructureInfluenceTest_1"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_4"] |
| AIInfluence_TestSequence_1 | 27 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_8"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_10 | 38 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_6","Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_1"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_11","Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_2"] |
| AIInfluence_TestSequence_11 | 41 | 未保存 | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_0"] |
| AIInfluence_TestSequence_12 | 24 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_7"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_3"] |
| AIInfluence_TestSequence_13 | 22 | ["Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_2"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_12","Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_1","Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_2"] |
| AIInfluence_TestSequence_14 | 57 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_12","Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_12"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeGuard_0"] |
| AIInfluence_TestSequence_15 | 12 | ["Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_4"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_16"] |
| AIInfluence_TestSequence_16 | 14 | ["Grunt_Adv_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_2","Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_1"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_4"] |
| AIInfluence_TestSequence_19 | 18 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_3","Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_7"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_4"] |
| AIInfluence_TestSequence_3 | 50 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_15"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_1"] |
| AIInfluence_TestSequence_35 | 44 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_25","Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_28"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_5","Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_3","Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_0","Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_1"] |
| AIInfluence_TestSequence_39 | 8 | ["Grunt_Adv_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_1","Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_9"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_0"] |
| AIInfluence_TestSequence_4 | 3 | ["Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_15"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_2"] |
| AIInfluence_TestSequence_5 | 47 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_4"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_3"] |
| AIInfluence_TestSequence_6 | 6 | ["Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_3"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_39"] |
| AIInfluence_TestSequence_7 | 未保存 | ["Grunt_Adv_ContextualDefense.DifficultyInfluenceTest_0"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_5"] |
| AIInfluence_TestSequence_8 | 31 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_5","Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_0"] | ["Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_9","Grunt_Adv_ContextualDefense.DefenseInfluenceNodeGuard_1"] |
| AIInfluence_TestSequence_9 | 34 | ["Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_10"] | ["Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_3"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_1 | 5 | 1 | ["Attack.Specific.BackFrontKD"] | 1 | 是 | 未保存 |
| AttackMemoryInfluenceTest_10 | 3 | 1 | ["Attack.Specific.BackFrontPush"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_12 | 4 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_15 | 5 | 1 | ["AI.Grunt.FirstParry"] | 4 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_25 | 2 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_3 | 5 | 5 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_4 | 5 | 1 | ["AI.Grunt.FirstAvoid"] | 未保存 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_5 | 10 | 1 | ["Attack.Specific.BackFrontPush"] | 3 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_6 | 10 | 1 | ["Attack.Specific.BackFrontKD"] | 3 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_7 | 5 | 1 | ["Attack.Specific.HoldDizzy"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_8 | 5 | 1 | ["Attack.Specific.HoldDizzyMax"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_9 | 5 | 1 | ["Attack.Specific.BackFrontPush"] | 1 | 是 | 未保存 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Grunt_Adv_ContextualDefense

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_35 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][9] | m_Nodes[0][9] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][10] | m_Nodes[0][10] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_1 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.StructureInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 53 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_10

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_11

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fProbability）[0] | m_fProbability[0] | 0.699999988 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 41 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_12

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_13

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_14

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeGuard_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 57 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_15

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_16

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_19

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeDodge_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeAvoid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 50 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_35

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_28 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 44 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_39

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_4

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 47 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_39 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_7

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.DifficultyInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeInvalid_5 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_8

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Grunt_Adv_ContextualDefense.AttackPropertiesInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeGuard_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_9

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Grunt_Adv_ContextualDefense.AttackMemoryInfluenceTest_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_1

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_10

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_12

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 58 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_15

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 51 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_25

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 45 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_3

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_4

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 48 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_5

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_6

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_7

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_8

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_9

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_0

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_1

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 40 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_12

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 59 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_15

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_2

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_28

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 46 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_3

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_4

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_7

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### BP_AiLaunchCounterCombo_Parry_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator31 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_Parry_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_Parry_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_IsOrderRunning_InfluenceTest_C_1

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### BP_IsOrderRunning_InfluenceTest_C_2

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_1

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 52 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_3

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_0

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 42 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_2

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_4

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_0

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 60 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_1

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_1

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 61 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_3

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 49 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_4

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_5

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_1

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 56 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_2

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_2.BP_AiLaunchCounterCombo_Parry_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 43 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_3

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_3.BP_AiLaunchCounterCombo_Parry_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_4

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo_Parry.BP_AiLaunchCounterCombo_Parry_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Grunt_Adv_ContextualDefense.DefenseInfluenceNodeParryDeflect_4.BP_AiLaunchCounterCombo_Parry_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 55 | 该字段暂保留原名；中文语义待核。 |


### DifficultyInfluenceTest_0

类：/Script/Sifu.DifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eTestType）[0] | m_eTestType[0] | EAIInfluenceTest::Inferior | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fValueMin）[0] | m_fValueMin[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fValueMax）[0] | m_fValueMax[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### StructureInfluenceTest_1

类：/Script/Sifu.StructureInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eTestType）[0] | m_eTestType[0] | EAIInfluenceTest::Inferior | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fValueMax）[0] | m_fValueMax[0] | 0.400000006 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 54 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
