# Shiroizu_ContextualDefense：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Kuroki/Shiroizu_ContextualDefense.uasset

收录本资产全部 41 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_41 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Shiroizu_ContextualDefense.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 26 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_6","Shiroizu_ContextualDefense.BP_Random_InfluenceTest_C_2"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_19"] |
| AIInfluence_TestSequence_1 | 6 | ["Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_1","Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_3"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_0"] |
| AIInfluence_TestSequence_11 | 3 | ["Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_11"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_1"] |
| AIInfluence_TestSequence_13 | 未保存 | ["Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_5"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeInvalid_0"] |
| AIInfluence_TestSequence_2 | 21 | ["Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_1"] | ["Shiroizu_ContextualDefense.AIInfluence_TestSequence_40","Shiroizu_ContextualDefense.AIInfluence_TestSequence_0"] |
| AIInfluence_TestSequence_3 | 30 | ["Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_2"] | ["Shiroizu_ContextualDefense.AIInfluence_TestSequence_5","Shiroizu_ContextualDefense.AIInfluence_TestSequence_6"] |
| AIInfluence_TestSequence_4 | 13 | ["Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_0"] | ["Shiroizu_ContextualDefense.AIInfluence_TestSequence_7","Shiroizu_ContextualDefense.AIInfluence_TestSequence_8"] |
| AIInfluence_TestSequence_40 | 23 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_5"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_19"] |
| AIInfluence_TestSequence_41 | 10 | ["Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_3"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_5 | 32 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_0"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_2"] |
| AIInfluence_TestSequence_6 | 35 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_2","Shiroizu_ContextualDefense.BP_Random_InfluenceTest_C_0"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_1"] |
| AIInfluence_TestSequence_7 | 15 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_1"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_3"] |
| AIInfluence_TestSequence_8 | 18 | ["Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_4"] | ["Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_2"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|
| AttackMemoryInfluenceTest_0 | 10 | 1 | ["Attack.Type.Hit"] | 未保存 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_1 | 10 | 1 | ["Attack.Type.Hit"] | 未保存 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_2 | 5 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_3 | 5 | 1 | ["Attack.Specific.GuardBreaker","Attack.Specific.HoldDizzy","Attack.Specific.HoldDizzyMax"] | 未保存 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_4 | 5 | 1 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_5 | 10 | 1 | ["Attack.Type.Hit"] | 未保存 | 未保存 | 未保存 |
| AttackMemoryInfluenceTest_6 | 5 | 2 | ["Attack.Type.Hit"] | 1 | 未保存 | 未保存 |


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Shiroizu_ContextualDefense

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_13 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][2] | m_Nodes[0][2] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][3] | m_Nodes[0][3] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_41 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][4] | m_Nodes[0][4] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][5] | m_Nodes[0][5] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][6] | m_Nodes[0][6] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][7] | m_Nodes[0][7] | Shiroizu_ContextualDefense.DefenseInfluenceNodeInvalid_2 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Shiroizu_ContextualDefense.BP_Random_InfluenceTest_C_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 26 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 6 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_11

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_11 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_13

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeInvalid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_2

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_40 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 21 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_3

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_6 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 30 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_4

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.GameDifficultyInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_7 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][1] | m_LinkedNodes[0][1] | Shiroizu_ContextualDefense.AIInfluence_TestSequence_8 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 13 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_40

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_19 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 23 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_41

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackPropertiesInfluenceTest_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 10 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_5

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 32 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_6

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Tests）[0][1] | m_Tests[0][1] | Shiroizu_ContextualDefense.BP_Random_InfluenceTest_C_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 35 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_7

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeDodge_3 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 15 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_8

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Shiroizu_ContextualDefense.AttackMemoryInfluenceTest_4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Shiroizu_ContextualDefense.DefenseInfluenceNodeAvoid_2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 18 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_0

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 33 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_1

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 16 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_2

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 36 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_3

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.GuardBreaker | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][2] | m_AttackProperties[0][2] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 8 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_4

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 19 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_5

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 10 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_bAvoided）[0] | m_bAvoided[0] | 是 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 24 | 该字段暂保留原名；中文语义待核。 |


### AttackMemoryInfluenceTest_6

类：/Script/Sifu.AttackMemoryInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Type.Hit | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_fMemoryLimit）[0] | m_fMemoryLimit[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_uiHitsCount）[0] | m_uiHitsCount[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_HitTypes）[0] | m_HitTypes[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 27 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_1

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.GuardBreaker | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][2] | m_AttackProperties[0][2] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 7 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_11

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.BackFrontKD | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.BackFrontPush | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_3

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.GuardBreaker | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][1] | m_AttackProperties[0][1] | Attack.Specific.HoldDizzy | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 攻击属性标签[0][2] | m_AttackProperties[0][2] | Attack.Specific.HoldDizzyMax | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 11 | 该字段暂保留原名；中文语义待核。 |


### AttackPropertiesInfluenceTest_5

类：/Script/Sifu.AttackPropertiesInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 攻击属性标签[0][0] | m_AttackProperties[0][0] | Attack.Specific.3Hits | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


### BP_Random_InfluenceTest_C_0

类：/Game/DB/AI/_Shared/InfluenceTests/BP_Random_InfluenceTest.BP_Random_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（Random）[0] | Random[0] | 65 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 37 | 该字段暂保留原名；中文语义待核。 |


### BP_Random_InfluenceTest_C_2

类：/Game/DB/AI/_Shared/InfluenceTests/BP_Random_InfluenceTest.BP_Random_InfluenceTest_C

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（Random）[0] | Random[0] | 75 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 28 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 12 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_1

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 38 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_19

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 29 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeAvoid_2

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 20 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_0

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Count | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Specific.GuardBreaker | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][2] | m_TagsToFlushOnSuccess[0][2] | Attack.Specific.HoldDizzy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][3] | m_TagsToFlushOnSuccess[0][3] | Attack.Specific.HoldDizzyMax | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 9 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_1

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Count | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_19

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Count | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Specific.GuardBreaker | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][2] | m_TagsToFlushOnSuccess[0][2] | Attack.Specific.HoldDizzy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][3] | m_TagsToFlushOnSuccess[0][3] | Attack.Specific.HoldDizzyMax | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 25 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_2

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Count | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Specific.GuardBreaker | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][2] | m_TagsToFlushOnSuccess[0][2] | Attack.Specific.HoldDizzy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][3] | m_TagsToFlushOnSuccess[0][3] | Attack.Specific.HoldDizzyMax | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 34 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeDodge_3

类：/Script/Sifu.DefenseInfluenceNodeDodge

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_eDirectionTypeOverride）[0] | m_eDirectionTypeOverride[0] | EDodgeDirectionType::Count | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][0] | m_TagsToFlushOnSuccess[0][0] | Attack.Type.Hit | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][1] | m_TagsToFlushOnSuccess[0][1] | Attack.Specific.GuardBreaker | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][2] | m_TagsToFlushOnSuccess[0][2] | Attack.Specific.HoldDizzy | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_TagsToFlushOnSuccess）[0][3] | m_TagsToFlushOnSuccess[0][3] | Attack.Specific.HoldDizzyMax | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 17 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_0

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeInvalid_2

类：/Script/Sifu.DefenseInfluenceNodeInvalid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 39 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_0

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 4 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 14 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_1

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 22 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_2

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 31 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
