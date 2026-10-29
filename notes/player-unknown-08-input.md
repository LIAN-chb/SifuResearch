# 玩家招式待核08：输入Alt、方向组合与条件覆写

本底稿是本地程序及资产的静态查询，不是游戏实测。匹配构建为EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d`、age 1、970231808 bytes，本批父任务核验见 `inventory/player-unknown-08-build.json`。每次有界反汇编由原有脚本再次核EXE SHA。证据结构化汇总及资产哈希见 `inventory/player-unknown-08-input-evidence.json`，类型见 `inventory/player-unknown-08-input-types.json`。

## I01：Alt是同一攻击键的短按松开条件，不是独立轻重手势

| 保存输入资产 | 键映射名 | 行为 | 时间参数 | 输入栈寿命 |
|---|---|---|---|---|
| `DB/Inputs/Actions/Attacks/Lights/AttackLight.uasset` | Attack1 | JustReleasedBefore | 0.2 | 0.35 |
| 同目录 `AttackLightAlt.uasset` | Attack1 | JustReleasedBefore | 0.2 | 0.35 |
| `DB/Inputs/Actions/Attacks/Heavy/AttackHeavy.uasset` | Attack2 | JustReleasedBefore | 0.2 | 0.35 |
| 同目录 `AttackHeavyAlt.uasset` | Attack2 | JustReleasedBefore | 0.2 | 0.35 |
| Lights/AttackLightHold.uasset | Attack1 | Pressed | 0.2 | 0.35 |
| Heavy/AttackHeavyHold.uasset | Attack2 | Pressed | 0.2 | 0.35 |

字段是 `m_unrealAction`、`m_BehaviourStruct.m_behavior`、`.m_fTimePressed`、`m_fLifeSpan`。保存浮点0.2实际为0.20000000298023224，0.35为0.3499999940395355；显示时可四舍五入，不能据此变成精确实战帧数。Hold的 `m_bAutoReset=true`。普通Light/Heavy也用松键条件，因此不能写成“普通是按下、Alt是松开”。

两组普通／Alt互列 `m_StackSiblings`：Light中为AttackLightAlt、LightAlt中为AttackLight；Heavy中为AttackHeavyAlt、HeavyAlt中为AttackHeavy。数组均12 bytes（count4＋FName8），本批按各资产自己的name map读取、检查字节耗尽。不同包的同一raw hash可对应不同FName，不能直接跨包对比裸索引。两种逻辑输入共用同一物理短按松键条件；本批没有追完输入栈消费优先级和Availability筛选，不能保证一次松键会在任何状态同时执行两招。

注册引用：`DB/Inputs/Contexts/BasicGameplay.uasset`、`BulletTime.uasset`、`Focus.uasset` 的 `m_inputActions` 均直接引用这两类Alt资产。见结构化证据contexts条目。此处证明配置入口存在，不证明所有情境都许可该动作。

### 消费者代码

- `InputCondition::SetDataDB` RVA `0x1a6be90`：复制UInputData `+0xc8` 的行为结构到InputCondition `+0x3c`，按 `m_unrealAction +0xc0` 查询键映射。类型中 `FInputBehaviourStruct.m_behavior +0`、`m_fTimePressed +4`；InputCondition `m_fTimePressed +0x10`、`m_BehaviorStruct +0x3c`。
- `InputBehavior` 枚举：JustPressed=0、Pressed=1、PressedShorterThan=2、JustReleased=3、JustReleasedBefore=4。
- `InputCondition::UpdateAction` RVA `0x1a6f230`，`0x1a6f3e2`读取行为值，3和4进入共同松键分支；`0x1a6f463`调用WasJustReleased；行为4在`0x1a6f485–0x1a6f48e`比较按压累计和阈值，`setbe`允许累计≤阈值，随后要求刚松开且未重置等状态，才设Active。行为1（Pressed）进入`0x1a6f5e8`一带按持续时间判断，不是用松键作为触发。
- `InputCondition::UpdateFramePressed` RVA `0x1a70dc0`：按传入DeltaTime累加m_fTimePressed，另记帧计数。冻结／输入栈状态会另记计时，不能把保存0.2概括为任何情境恒定12渲染帧。
- 完整输出：`logs/player-unknown-08-input-runtime/`、`logs/player-unknown-08-input-timer/`；对应inventory同名前缀disassembly清单含函数范围和SHA。

可安全展示为“短按轻击松开·变体”“短按重击松开·变体”，详情注明保存阈值≤0.2秒，与普通轻／重共用按键条件，实际消费仍受输入栈及动作许可影响。它不提供“轻重快速连按／同时按”对应Alt的证据。

## I02：InputAction到ComboTransition的真实映射

`UComboTransitionHelper::BPF_GetTransitionFromInput` RVA `0x19505b0`、`BPF_GetInputFromTransition` RVA `0x19501e0`，由匹配PDB命名的有界函数。反汇编末尾含跳表字节，不能把表的伪指令当代码；本批从EXE原字节按PE节RVA读取表。

LightAlt=2 ↔ InputAction::AttackLightAlt=2；HeavyAlt=8 ↔ AttackHeavyAlt=5。LightFrontFront=4 ↔ AttackLightFrontFront=110；LightBackFront=5 ↔ AttackLightBackFront=109；重击两者对应113／112。全部21种转换的逐项表含case RVA保存于结构化证据mapping；18种有InputAction映射者通过双向回查。

边界：DodgeAttack、LightGuard、HeavyGuard在GetInputFromTransition返回InputAction::None=209；不能因为另一个函数接受某输入而假设两者普遍双向。这个结果也不证明这些动作不可用，它们可能通过专门路径构造。

## I03：方向输入确认到组合配置，绝对朝向和全招接入仍缺

`AttackLightFrontFront` 引用 `AttackLight` 与 `DirFrontFront`；HeavyFrontFront引用HeavyJustPress与DirFrontFront；Light／HeavyBackFront分别引用对应JustPress与DirBackFront。相应 `CombinationInputData.m_IncludedInputs` 含方向项寿命0.4、攻击项0；组合本身m_fLifeSpan0.35。不可将这些寿命相加称为“玩家有0.75秒窗口”。这些是输入缓存与组合配置，不是整招时间。

DirBackFront是AnalogInputSequenceData，两步；DirFrontFront三步。两者 `m_bUseRawVectorInputs=true`，首步 `m_bIsReferenceDirection=true`、`m_eReferenceDirBehavior=UpdateWithInputDir`，后续标结果方向。DirBackFront首步最大有效0.25，DirFrontFront首两步各0.1。完整角度／幅度／速度／保持时间边界保留于证据assets，未把名字直接当世界前后或敌人朝向。

本次没有追完AnalogInputSequenceCondition::UpdateAction与CombinationInputCondition的具体时间消费、参照向量转换、和每一招Availability。因此仍不把“方向招通常任意招后可接”的用户观察提升为逐节点逻辑证明。

2026-10-29修订导航：14批已补17种许可层、OR进入/退出和攻击Ability候选/表序/节点准入链；详见[player-timeline-14-availability](player-timeline-14-availability.md) A14-1至A14-4。旧“尚未追完”缩小到该文具名的激活/打断、输入条件蓝图、context与fallback内部缺口，不再概括为许可选择全未解；方向参照和最终运行时接招仍保留原边界。

## I04：条件覆写是Tag映射，具体条目仍未解码

PDB `FComboNode`：m_AttackInfos位于`+0x20`；m_ConditionalAttacks位于`+0x60`，类型为`TMap<FGameplayTag,FComboNodeAttackInfos>`，并非独立FConditionalAttack结构。

`FComboNode::GetAttackInfos` RVA `0x195a9c0`遍历条件Map；`0x195aba5`取得角色AbilitySystemComponent，调用其tag查询接口，命中返回当前entry+8的AttackInfos；无角色、空map或均不命中则`0x195abd7`返回node+0x20基础配置。该虚调用具体实现与多tag同时命中的顺序优先未进一步追通，不能把Map遍历顺序称为设计上的固定优先级。

`MainChar_ComboTree.uasset`节点44的m_ConditionalAttacks保存**1067 bytes**，sha256 `463565a669459a57272cc816e0c10089d14624c5fd6f449712f39187600db5b9`，标记decoded=false。它不是空Map；当前展示没有列出其中条件替换动作，不代表不存在。需按GameplayTag key＋FComboNodeAttackInfos value定向解码完整Map并检查耗尽，再连接角色tag的实际授予来源。本批未把六个常规树外候选强行配给它。

## 执行、失败和断点

工作目录均为研究根。执行命令：

1. `python scripts/disassemble_research.py --group player-unknown-08-input --name UComboTransitionHelper::BPF_GetTransitionFromInput --name UComboTransitionHelper::BPF_GetInputFromTransition`（退出0）
2. `python scripts/disassemble_research.py --group player-unknown-08-input-runtime --name InputCondition::UpdateAction --name InputCondition::GetTimePressedToActivate --name InputCondition::SetDataDB`（退出0）
3. `python scripts/disassemble_research.py --group player-unknown-08-input-conditional --name FComboNode::GetAttackInfos`（退出0）
4. `python scripts/disassemble_research.py --group player-unknown-08-input-timer --name InputCondition::UpdateFramePressed`（退出0）
5. `python exports/20261029-玩家招式待核-08/input-types.py`（退出0，最终10类型，FConditionalAttack未找到）
6. `python exports/20261029-玩家招式待核-08/input-evidence.py`（退出0，12资产与3上下文，18有映射转换双向核验，enum数组字节耗尽；生成input-evidence.json）

解释器版本和脚本／原输入／资产SHA见结构化证据。类型脚本复用原TPI reader，但仅改目标名字和独立输出路径，不覆盖共享类型清单。曾请求InputBehaviourStruct缺F前缀未找到，按成员真实类型修为FInputBehaviourStruct；另一次Python内联输出括号SyntaxError未写文件。首轮映射检查错误地期待全部21项双向回查，到DodgeAttack的None越界时失败；复查函数分支后区分18有映射和3无逆映射，不把失败掩盖成全通过。

未访问存档、未启动游戏、未重新解包。未改共享模板和知识库页，结果交父任务整合。下一步：解节点44等条件Map；追输入栈siblings消费与Availability；追方向参照和组合条件消费者。当前不需要用户做手动操作。

13批后续修订：用户已授权执行徒手补全和名称标注。57节点条件Map现已精确读取，57条全部为Attack.Modifiers替换配置；具体Tag与四槽资产见exports/20261029-徒手补全与命名-13/conditional-attacks.json和notes/player-completeness-13-conditional.md。此前该部分未解表述保留历史身份，运行期应用及其他未解分支不扩大结论。
