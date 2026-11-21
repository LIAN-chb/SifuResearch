# Bodyguard_Miniboss_ContextualDefense：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/_Miniboss/Bodyguard_Miniboss_ContextualDefense.uasset

收录本资产全部 55 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_21 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 5 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_8"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_4","Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_37"] |
| AIInfluence_TestSequence_1 | 43 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_28"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_19","Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_3"] |
| AIInfluence_TestSequence_10 | 35 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_27"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_2","Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_12","Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_1","Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_3"] |
| AIInfluence_TestSequence_12 | 40 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_2"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_4"] |
| AIInfluence_TestSequence_16 | 20 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_12"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_1"] |
| AIInfluence_TestSequence_19 | 45 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_0"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_1"] |
| AIInfluence_TestSequence_2 | 37 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_1"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_21 | 12 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_30"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_38"] |
| AIInfluence_TestSequence_26 | 16 | 未保存 | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_3"] |
| AIInfluence_TestSequence_3 | 29 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_0","Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_6"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_0"] |
| AIInfluence_TestSequence_35 | 2 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_5"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_2"] |
| AIInfluence_TestSequence_36 | 未保存 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_7"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_35"] |
| AIInfluence_TestSequence_37 | 10 | 未保存 | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_6"] |
| AIInfluence_TestSequence_38 | 14 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_6"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_26"] |
| AIInfluence_TestSequence_4 | 7 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_3"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeDodge_2"] |
| AIInfluence_TestSequence_5 | 33 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_26"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_10","Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_1"] |
| AIInfluence_TestSequence_6 | 18 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_4"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_16","Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_5"] |
| AIInfluence_TestSequence_8 | 24 | ["Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_5"] | ["Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_9","Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_3"] |
| AIInfluence_TestSequence_9 | 26 | ["Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_17"] | ["Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeInvalid_2"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_0 | 5 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_1 | 1.5 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_12 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_17 | 20 | 1 | ["AI.FireDisciple.3HitsAvoided"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_2 | 20 | 1 | ["AI.Grunt.FirstAvoid"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_26 | 5 | 1 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_27 | 7 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_28 | 20 | 1 | ["AI.Grunt.FirstParry"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_3 | 10 | 1 | ["Attack.Specific.BackFrontKD"] | 7 | 未保存 | 是 |
| AttackMemoryInfluenceTest_5 | 10 | 1 | ["Attack.Specific.GuardBreaker"] | 7 | 是 | 是 |
| AttackMemoryInfluenceTest_6 | 10 | 1 | ["Attack.Specific.BackFrontPush"] | 7 | 是 | 是 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Bodyguard_Miniboss_ContextualDefense

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_21 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_37 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_28 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 43 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_10

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_27 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_12

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 40 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_16

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_19

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 45 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_21

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_30 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_38 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_26

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fProbability）[0] | m_fProbability[0] | 0.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_35

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_36

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_35 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_37

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fProbability）[0] | m_fProbability[0] | 0.699999988 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_38

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_26 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_4

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeDodge_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_26 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeGuard_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeAvoid_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_8

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackPropertiesInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Bodyguard_Miniboss_ContextualDefense.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_9

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Bodyguard_Miniboss_ContextualDefense.AttackMemoryInfluenceTest_17 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_0

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_1

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 1.5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_12

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_17

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.FireDisciple.3HitsAvoided | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_2

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstAvoid | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 41 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_26

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_27

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_28

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.Grunt.FirstParry | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 44 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_3

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_5

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.GuardBreaker | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_6

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_0

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.SkillMultiHits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 46 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_30

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_4

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_5

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_6

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_7

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.GuardBreaker | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_8

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator12 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_1

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Bodyguard/Dash/BP_AiAction_Dash_S_Bodyguard.BP_AiAction_Dash_S_Bodyguard_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | 对象索引 0；未解析引用 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_3

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_1.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 48 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_5

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_2

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bOverrideDirection）[0] | m_bOverrideDirection[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Back | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_0

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.FireDisciple.3HitsAvoided | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_1

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 50 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_2

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_3

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_6

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 51 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.FireDisciple.3HitsAvoided | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_1

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_1.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 47 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_3

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.Grunt.FirstParry | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 49 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_4

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | AI.Grunt.FirstAvoid | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_fMemoryFlushLimit）[0] | m_fMemoryFlushLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Bodyguard_Miniboss_ContextualDefense.DefenseInfluenceNodeParryDeflect_4.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 42 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
