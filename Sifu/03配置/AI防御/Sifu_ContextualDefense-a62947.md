# Sifu_ContextualDefense：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人AI/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Sifu/Sifu_ContextualDefense.uasset

收录本资产全部 76 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Sifu_ContextualDefense.AIInfluence_TestSequence_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Sifu_ContextualDefense.AIInfluence_TestSequence_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Sifu_ContextualDefense.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Sifu_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Sifu_ContextualDefense.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Sifu_ContextualDefense.AIInfluence_TestSequence_29 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Sifu_ContextualDefense.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_1 | 未保存 | ["Sifu_ContextualDefense.AttackPropertiesInfluenceTest_12"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_1"] |
| AIInfluence_TestSequence_10 | 15 | ["Sifu_ContextualDefense.AttackPropertiesInfluenceTest_2"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_7"] |
| AIInfluence_TestSequence_12 | 21 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_10"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeDodge_4"] |
| AIInfluence_TestSequence_15 | 9 | ["Sifu_ContextualDefense.AttackPropertiesInfluenceTest_13"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_16"] |
| AIInfluence_TestSequence_16 | 11 | ["Sifu_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_5","Sifu_ContextualDefense.AttackMemoryInfluenceTest_13"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_2"] |
| AIInfluence_TestSequence_2 | 58 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_15","Sifu_ContextualDefense.AttackPropertiesInfluenceTest_11"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_6"] |
| AIInfluence_TestSequence_25 | 65 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_1"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeGuard_1"] |
| AIInfluence_TestSequence_29 | 32 | ["Sifu_ContextualDefense.GameDifficultyInfluenceTest_4"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_30","Sifu_ContextualDefense.AIInfluence_TestSequence_32","Sifu_ContextualDefense.AIInfluence_TestSequence_34","Sifu_ContextualDefense.AIInfluence_TestSequence_31","Sifu_ContextualDefense.AIInfluence_TestSequence_33"] |
| AIInfluence_TestSequence_30 | 34 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_33","Sifu_ContextualDefense.AttackMemoryInfluenceTest_34"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_9"] |
| AIInfluence_TestSequence_31 | 45 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_35","Sifu_ContextualDefense.BP_Random_InfluenceTest_C_4"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_7"] |
| AIInfluence_TestSequence_32 | 38 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_36","Sifu_ContextualDefense.AttackPropertiesInfluenceTest_6"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_10"] |
| AIInfluence_TestSequence_33 | 49 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_37"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeGuard_4"] |
| AIInfluence_TestSequence_34 | 42 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_38"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_8"] |
| AIInfluence_TestSequence_36 | 3 | ["Sifu_ContextualDefense.AttackPropertiesInfluenceTest_9"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_39"] |
| AIInfluence_TestSequence_39 | 5 | ["Sifu_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_0","Sifu_ContextualDefense.AttackMemoryInfluenceTest_9"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_3"] |
| AIInfluence_TestSequence_46 | 62 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_7"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_9"] |
| AIInfluence_TestSequence_5 | 54 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_2","Sifu_ContextualDefense.AttackMemoryInfluenceTest_17"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_6 | 18 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_6","Sifu_ContextualDefense.AttackPropertiesInfluenceTest_14"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_12","Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_15"] |
| AIInfluence_TestSequence_7 | 25 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_8","Sifu_ContextualDefense.AttackPropertiesInfluenceTest_0"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_8","Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_1"] |
| AIInfluence_TestSequence_8 | 28 | ["Sifu_ContextualDefense.AttackMemoryInfluenceTest_11"] | ["Sifu_ContextualDefense.DefenseInfluenceNodeDodge_3"] |
| AIInfluence_TestSequence_9 | 52 | ["Sifu_ContextualDefense.GameDifficultyInfluenceTest_0"] | ["Sifu_ContextualDefense.AIInfluence_TestSequence_5","Sifu_ContextualDefense.AIInfluence_TestSequence_2","Sifu_ContextualDefense.AIInfluence_TestSequence_46","Sifu_ContextualDefense.AIInfluence_TestSequence_25"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_1 | 10 | 未保存 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_10 | 10 | 1 | ["Attack.Specific.BackFrontPush"] | 4 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_11 | 10 | 1 | ["Attack.Specific.BackFrontKD"] | 4 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_13 | 20 | 1 | ["Attack.Specific.BackFrontKD"] | 1 | 是 | 未保存 |
| AttackMemoryInfluenceTest_15 | 10 | 1 | ["Attack.Type.Hit"] | 4 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_17 | 10 | 1 | ["AI.BoringLoop"] | 7 | 是 | 是 |
| AttackMemoryInfluenceTest_2 | 10 | 2 | 未保存 | 4 | 未保存 | 是 |
| AttackMemoryInfluenceTest_33 | 10 | 2 | 未保存 | 4 | 未保存 | 是 |
| AttackMemoryInfluenceTest_34 | 10 | 1 | ["AI.BoringLoop"] | 7 | 是 | 是 |
| AttackMemoryInfluenceTest_35 | 15 | 1 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_36 | 10 | 1 | ["Attack.Type.Hit"] | 4 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_37 | 10 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_38 | 15 | 2 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_6 | 10 | 1 | ["Attack.Specific.BackFrontPush"] | 3 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_7 | 15 | 2 | ["Attack.Type.Hit"] | 2 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_8 | 10 | 1 | ["Attack.Specific.BackFrontKD"] | 3 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_9 | 20 | 1 | ["Attack.Specific.BackFrontPush"] | 1 | 是 | 未保存 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Sifu_ContextualDefense

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Sifu_ContextualDefense.AIInfluence_TestSequence_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Sifu_ContextualDefense.AIInfluence_TestSequence_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Sifu_ContextualDefense.AIInfluence_TestSequence_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Sifu_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Sifu_ContextualDefense.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Sifu_ContextualDefense.AIInfluence_TestSequence_29 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Sifu_ContextualDefense.AIInfluence_TestSequence_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][8] | m_Nodes[0][8] | Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_1 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_10

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_12

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeDodge_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_15

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_16 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_16

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 58 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_25

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeGuard_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 65 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_29

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.GameDifficultyInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_30 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Sifu_ContextualDefense.AIInfluence_TestSequence_32 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Sifu_ContextualDefense.AIInfluence_TestSequence_34 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Sifu_ContextualDefense.AIInfluence_TestSequence_31 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][4] | m_LinkedNodes[0][4] | Sifu_ContextualDefense.AIInfluence_TestSequence_33 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_30

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_33 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_34 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_31

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_35 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.BP_Random_InfluenceTest_C_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 45 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_32

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_36 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_33

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_37 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeGuard_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 49 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_34

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_38 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 42 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_36

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_39 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_39

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.BP_IsOrderRunning_InfluenceTest_C_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeInvalid_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_46

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_9 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 62 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_17 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 54 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_14 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_12 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_7

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Sifu_ContextualDefense.AttackPropertiesInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_8

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.AttackMemoryInfluenceTest_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.DefenseInfluenceNodeDodge_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_9

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Sifu_ContextualDefense.GameDifficultyInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Sifu_ContextualDefense.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Sifu_ContextualDefense.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][2] | m_LinkedNodes[0][2] | Sifu_ContextualDefense.AIInfluence_TestSequence_46 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][3] | m_LinkedNodes[0][3] | Sifu_ContextualDefense.AIInfluence_TestSequence_25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 52 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_1

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 66 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_10

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_11

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_13

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_15

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 59 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_17

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.BoringLoop | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 56 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_2

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 55 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_33

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_34

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | AI.BoringLoop | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bDodged）[0] | m_bDodged[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_35

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 46 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_36

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_37

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 50 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_38

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 43 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_6

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_7

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 15 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 63 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_8

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_9

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 20 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bInverted）[0] | m_bInverted[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_0

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_11

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 60 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_12

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_13

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_14

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_2

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_6

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 40 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_9

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator30 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator10 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator10 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### DefenseInfluenceNodeAvoid_0.BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator10 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_AiLaunchCounterCombo_C_0

类：/Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Parameters）[0] → 未核中文义（m_Ticket）[0] → 枚举保存项[0] | m_Parameters[0].m_Ticket[0].m_Value[0] | BP_AIAttackTIcketNames::NewEnumerator10 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |


### BP_IsOrderRunning_InfluenceTest_C_0

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### BP_IsOrderRunning_InfluenceTest_C_5

类：/Game/DB/AI/_Shared/InfluenceTests/BP_IsOrderRunning_InfluenceTest.BP_IsOrderRunning_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### BP_Random_InfluenceTest_C_4

类：/Game/DB/AI/_Shared/InfluenceTests/BP_Random_InfluenceTest.BP_Random_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（Random）[0] | Random[0] | 0.25 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 47 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.BoringLoop | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_0.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 57 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_1

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_10

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 41 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_6

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 61 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_7

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_9

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToRaiseOnSuccess）[0][0] | m_TagsToRaiseOnSuccess[0][0] | AI.BoringLoop | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeAvoid_9.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_3

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Specific.BackFrontPush | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_4

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Specific.BackFrontPush | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_1

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 67 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_4

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 51 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 68 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_1

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_3

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_15

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_15.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_7

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_7.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 48 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_8

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_8.DefenseInfluenceNodeAvoid_0.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 44 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeParryDeflect_9

类：/Script/Sifu.DefenseInfluenceNodeParryDeflect

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bLaunchDefaultActions）[0] | m_bLaunchDefaultActions[0] | 否 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/Blueprints/AI/Actions/Defense/CounterCombo/BP_AiLaunchCounterCombo.BP_AiLaunchCounterCombo_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Sifu_ContextualDefense.DefenseInfluenceNodeParryDeflect_9.BP_AiLaunchCounterCombo_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 64 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_0

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 53 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_4

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
