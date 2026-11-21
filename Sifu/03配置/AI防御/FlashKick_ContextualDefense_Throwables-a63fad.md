# FlashKick_ContextualDefense_Throwables：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/FlashKick/_MainGame/Generic/FlashKick_ContextualDefense_Throwables.uasset

收录本资产全部 19 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 未保存 | ["FlashKick_ContextualDefense_Throwables.GPStateInfluenceTest_0"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeInvalid_0"] |
| AIInfluence_TestSequence_1 | 3 | ["FlashKick_ContextualDefense_Throwables.BP_IsOrderRunning_InfluenceTest_C_1"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeInvalid_5"] |
| AIInfluence_TestSequence_2 | 9 | ["FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_1"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_5"] |
| AIInfluence_TestSequence_3 | 12 | ["FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_2"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_4 | 15 | ["FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_8"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_2"] |
| AIInfluence_TestSequence_9 | 6 | ["FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_0"] | ["FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_3"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### FlashKick_ContextualDefense_Throwables

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | FlashKick_ContextualDefense_Throwables.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.GPStateInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.BP_IsOrderRunning_InfluenceTest_C_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeInvalid_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_4

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_9

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | FlashKick_ContextualDefense_Throwables.ThrowAttackInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | FlashKick_ContextualDefense_Throwables.DefenseInfluenceNodeAvoid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### BP_IsOrderRunning_InfluenceTest_C_1

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_2

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_3

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_5

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


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


### GPStateInfluenceTest_0

类：/Script/Sifu.GPStateInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eState）[0] | m_eState[0] | EAIGameplayStates::Attacking | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_0

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_WeaponDataTypeToTest）[0] | m_WeaponDataTypeToTest[0] | /Game/Blueprints/LDIngredients/Weapons/MakeShift_OneHandedFamily/BP_WeaponData_MakeShift_OneHandedFamilly.BP_WeaponData_MakeShift_OneHandedFamilly_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_1

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_WeaponDataTypeToTest）[0] | m_WeaponDataTypeToTest[0] | /Game/Blueprints/LDIngredients/Weapons/BatFamily/BP_WeaponData_BatFamily.BP_WeaponData_BatFamily_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_2

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_WeaponDataTypeToTest）[0] | m_WeaponDataTypeToTest[0] | /Game/Blueprints/LDIngredients/Weapons/BladeFamily/BP_WeaponData_BladesFamily.BP_WeaponData_BladesFamily_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### ThrowAttackInfluenceTest_8

类：/Script/Sifu.ThrowAttackInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_WeaponDataTypeToTest）[0] | m_WeaponDataTypeToTest[0] | /Game/Blueprints/LDIngredients/Weapons/TwoHandedFamily/Staff/BP_WeaponData_StaffFamily.BP_WeaponData_StaffFamily_C | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
