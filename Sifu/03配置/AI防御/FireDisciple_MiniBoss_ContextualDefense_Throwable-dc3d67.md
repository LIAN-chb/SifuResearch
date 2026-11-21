# FireDisciple_MiniBoss_ContextualDefense_Throwable：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Variations/Defense/FireDisciple_MiniBoss_ContextualDefense_Throwable.uasset

收录本资产全部 13 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 6 | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.ThrowAttackInfluenceTest_2"] | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeAvoid_3"] |
| AIInfluence_TestSequence_1 | 未保存 | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.GPStateInfluenceTest_1"] | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeInvalid_0"] |
| AIInfluence_TestSequence_2 | 3 | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.BP_IsOrderRunning_InfluenceTest_C_0"] | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeInvalid_5"] |
| AIInfluence_TestSequence_4 | 9 | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.ThrowAttackInfluenceTest_4"] | ["FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeAvoid_2"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### FireDisciple_MiniBoss_ContextualDefense_Throwable

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | FireDisciple_MiniBoss_ContextualDefense_Throwable.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.ThrowAttackInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeAvoid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.GPStateInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.BP_IsOrderRunning_InfluenceTest_C_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeInvalid_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_4

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.ThrowAttackInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FireDisciple_MiniBoss_ContextualDefense_Throwable.DefenseInfluenceNodeAvoid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### BP_IsOrderRunning_InfluenceTest_C_0

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_2

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_3

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_5

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### GPStateInfluenceTest_1

类：/Script/Sifu.GPStateInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eState）[0] | m_eState[0] | EAIGameplayStates::Attacking | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_2

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ThrowableTypeToTest）[0] | m_ThrowableTypeToTest[0] | /Game/Blueprints/LDIngredients/Throwable/HeavyLow/BP_Throwable_HeavyLow_Master.BP_Throwable_HeavyLow_Master_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_4

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_WeaponDataTypeToTest）[0] | m_WeaponDataTypeToTest[0] | /Game/Blueprints/LDIngredients/Weapons/BP_WeaponData.BP_WeaponData_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
