# Yang_P1_Defense_ContextualDefense：AI 防御配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/敌人如何选择防御|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Yang/_DB/Phase1/Yang_P1_Defense_ContextualDefense.uasset

收录本资产全部 9 个已解析对象。图节点存在不代表可达或必定被选中；部分测试反转字段未保存，缺省值仍待确认。原始掩码不借用其他枚举解释。

## 图入口保存字段

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Yang_P1_Defense_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Yang_P1_Defense_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |


## 全部测试序列与连接

| 序列对象 | 节点索引 | 测试引用（需共同通过，含各自反转） | 关联后继节点 |
|---|---|---|---|
| AIInfluence_TestSequence_0 | 未保存 | ["Yang_P1_Defense_ContextualDefense.GameDifficultyInfluenceTest_1"] | ["Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeAvoid_0"] |
| AIInfluence_TestSequence_1 | 3 | ["Yang_P1_Defense_ContextualDefense.GameDifficultyInfluenceTest_0"] | ["Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeGuard_0"] |


## 全部攻击记忆测试

| 对象 | 记忆时间字段 | 计数阈值 | 攻击标签 | 命中掩码原值 | 反转字段 | 闪避标志 |
|---|---|---|---|---|---|---|


## 全部对象的保存配置

下面完整列出当前解析成功的对象字段，便于查看其他测试、概率、动作成功回调、闪避和招架的不同配置。没有补全父类或原生默认值。

### Yang_P1_Defense_ContextualDefense

类：/Script/Sifu.AIContextualDefense

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Nodes）[0][0] | m_Nodes[0][0] | Yang_P1_Defense_ContextualDefense.AIInfluence_TestSequence_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_Nodes）[0][1] | m_Nodes[0][1] | Yang_P1_Defense_ContextualDefense.AIInfluence_TestSequence_1 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_0

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Yang_P1_Defense_ContextualDefense.GameDifficultyInfluenceTest_1 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeAvoid_0 | 该字段暂保留原名；中文语义待核。 |


### AIInfluence_TestSequence_1

类：/Script/Sifu.AIInfluence_TestSequence

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_Tests）[0][0] | m_Tests[0][0] | Yang_P1_Defense_ContextualDefense.GameDifficultyInfluenceTest_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_LinkedNodes）[0][0] | m_LinkedNodes[0][0] | Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeGuard_0 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 3 | 该字段暂保留原名；中文语义待核。 |


### BP_AiActionChangePhase_Yang_OffensivePhase_C_0

类：/Game/DB/AI/Archetypes/Yang/_DB/Phase1/ChangePhase/BP_AiActionChangePhase_Yang_OffensivePhase.BP_AiActionChangePhase_Yang_OffensivePhase_C
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

### DefenseInfluenceNodeAvoid_0.BP_AiActionChangePhase_Yang_OffensivePhase_C_0

类：/Game/DB/AI/Archetypes/Yang/_DB/Phase1/ChangePhase/BP_AiActionChangePhase_Yang_OffensivePhase.BP_AiActionChangePhase_Yang_OffensivePhase_C
本对象没有保存可列出的覆盖字段；不代表全部数值为零。

### DefenseInfluenceNodeAvoid_0

类：/Script/Sifu.DefenseInfluenceNodeAvoid

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase1/ChangePhase/BP_AiActionChangePhase_Yang_OffensivePhase.BP_AiActionChangePhase_Yang_OffensivePhase_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeAvoid_0.BP_AiActionChangePhase_Yang_OffensivePhase_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 2 | 该字段暂保留原名；中文语义待核。 |


### DefenseInfluenceNodeGuard_0

类：/Script/Sifu.DefenseInfluenceNodeGuard

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_ConditionsArray）[0] | m_ActionsOnSuccess[0][0].m_ConditionsArray[0] | [] | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 类默认对象[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_DefaultClassObject[0] | /Game/DB/AI/Archetypes/Yang/_DB/Phase1/ChangePhase/BP_AiActionChangePhase_Yang_OffensivePhase.BP_AiActionChangePhase_Yang_OffensivePhase_C | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_ActionsOnSuccess）[0][0] → 未核中文义（m_Action）[0] → 条件或对象实例[0] | m_ActionsOnSuccess[0][0].m_Action[0].m_Instance[0] | Yang_P1_Defense_ContextualDefense.DefenseInfluenceNodeGuard_0.DefenseInfluenceNodeAvoid_0.BP_AiActionChangePhase_Yang_OffensivePhase_C_0 | 中文名称按字段含义翻译；未单独追通的运行期语义以基础机制和原始字段为准。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 5 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_0

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 2 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 4 | 该字段暂保留原名；中文语义待核。 |


### GameDifficultyInfluenceTest_1

类：/Script/Sifu.GameDifficultyInfluenceTest

| 中文标识 | 原字段路径 | 保存值／引用 | 中文说明 |
|---|---|---|---|
| 未核中文义（m_uiGameDifficultyFlags）[0] | m_uiGameDifficultyFlags[0] | 5 | 该字段暂保留原名；中文语义待核。 |
| 未核中文义（m_iNodeIndex）[0] | m_iNodeIndex[0] | 1 | 该字段暂保留原名；中文语义待核。 |


来源：inventory/tagged-objects.json.gz。已确认的选取／执行逻辑见对应基础机制；本页只将全图配置展开，不将图连接自动改写成实战攻略。
