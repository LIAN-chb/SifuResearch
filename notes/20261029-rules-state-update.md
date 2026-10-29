# 新命中如何更新已有 FightingState

## 范围与读法

本文回答一个通用规则问题：**敌人已经处于受控状态时，新命中会沿什么分支保留、刷新、替换或结束这个状态？**这里的“敌人”是 `UHitComponent` 所在的受击角色；实际执行对象由 `UHitComponent` 取得该角色的 `UDefenseComponent`。本文不是具体连招案例，也不把静态条件当成实际战斗结果。

先区分两层：

| 层 | 作用 | 关键函数 |
|---|---|---|
| 命中分类 | 把这次命中归为 `Hit`、`KnockDown`、`Push`、`Dizzy` 等 `EImpactType` | `UHitComponent::ComputeImpactType` |
| 状态更新 | 根据分类和已有状态，决定旧状态是否先 Pop、旧计数是否转移，再创建新状态 | `UpdateFightingStateFromImpact` → `ApplyFightingStateFromImpact` → `PushFightingState` |
| 状态退出 | 按计时、累计伤害或累计命中上限移除元素；移除会触发相应 Pop 流程 | `UDefenseComponent::TickComponent` → `PopFightingState` |

**不能把“产生同一种动画/受击反应”直接等同于“旧状态原地续时”。**`PushFightingState` 会追加新的 `FFightingStateElement`；何时删掉旧元素，主要由上层 `Update/Apply` 的分支决定。

## 关键数据字段

以下偏移以相应类型为基准，不混用相对偏移空间。

| 对象 / 字段 | 偏移 | 类型 | 中文标识／本批用途 |
|---|---:|---|---|
| `FImpactResult.m_eGuardType` | `+0x1E` | `EGuardType` | 本次结果中的防御类型；`None=0`，`Guard=1`，`Deflect=2`。分类函数只用它判断是否非 None。 |
| `FAttackPropertyLevel.m_bKeepCurrentStateDuration` | `+0x15` | `bool` | 攻击属性等级是否走“已有状态时间”处理分支；不只影响时长，也参与命中分类降级。 |
| `FAttackPropertyLevel.m_fKeepCurrentStateThresold` | `+0x18` | `float` | 当前状态剩余时间的阈值；类型布局保留原字段拼写 `Thresold`。 |
| `FAttackPropertyLevel.m_bUseCustomDuration` / `m_fCustomDuration` | `+0x0C / +0x10` | `bool / float` | 命中属性等级是否直接提供自定义状态时长。 |
| `FAttackPropertyLevel.m_bUseHitAnimDuration` | `+0x14` | `bool` | 是否优先从命中动画容器计算受控时长的条件之一。 |
| `FPropertyReaction.m_bAlwayKeepCurrentStateDurationOnHit` | `+0xA0` | `bool` | `PropertyReaction` 的另一种“有旧状态时尽量保留较长时间”开关；与攻击属性等级的 `+0x15` 不同。 |
| `FPropertyReaction.m_bHoldDuringStructureBroken` | `+0xA2` | `bool` | 针对结构崩溃状态的时长延续分支。 |
| `FPropertyReaction.m_fMaxAccumulatedDamage` | `+0xA4` | `float` | 状态累计伤害上限来源之一，写入新状态元素。 |
| `FPropertyReaction.m_iMaxAccumatedHits` | `+0xA8` | `int` | 状态累计命中上限来源之一；原字段名拼写为 `Accumated`。 |
| `FPropertyReaction.m_bGroupMaxAccumulatedHitsByAttack` | `+0xAC` | `bool` | “按攻击名归组”标记；具体计数事件在另一批 `受击计数事件` 中追。 |
| `FSuperDizzyReaction.m_fMandatoryDuration / m_fMaxAccumulatedDamage / m_iMaxAccumatedHits` | 子结构内 `+0x00 / +0x04 / +0x08`；`UAttackPropertiesResistanceDB` 内子结构基址 `+0x380` | `float / float / int` | SuperDizzy 使用单独的必需时长与累计伤害／命中上限；不能拿普通 Dizzy 的 `FPropertyReaction` 计数阈值代表全部 Dizzy。 |
| `FFightingStateElement.m_bPause` | `+0x00` | `bool` | Tick 遇到该标志时跳过 elapsed 累加及该元素的累计伤害／命中阈值检查。 |
| `FFightingStateElement.m_fStateDuration / m_fElapsedTime` | `+0x04 / +0x08` | `float / float` | 状态持续时长与累计经过时间。 |
| `FFightingStateElement.m_bInfinite` | `+0x0C` | `bool` | 该状态是否跳过 Tick 中的时长与累计阈值退出检查。`PushFightingState` 由负时长设置为真；其他显式 Pop 路径仍可能移除它。 |
| `FFightingStateElement.m_fMaxAccumulatedDamages / m_fAccumulatedDamages` | `+0x10 / +0x14` | `float / float` | 累计伤害退出阈值和当前累计量。 |
| `FFightingStateElement.m_iMaxAccumulatedHits / m_iAccumulatedHits` | `+0x18 / +0x20` | `int / int` | 累计命中退出阈值和当前计数。 |
| `FFightingStateElement.m_bGroupMaxAccumulatedHitsByAttack` | `+0x1C` | `bool` | 状态元素保存的归组设置。 |
| `FFightingStateElement.m_LastAttackName` | `+0x24` | `FName` | `OnHit` 归组计数使用的上一攻击名。 |
| `FFightingStateElement.m_eState / m_eSubFightingState` | `+0x2C / +0x2D` | `EFightingState / ESubFightingState` | 状态主类与子类。 |
| `FFightingStateElement.m_iHandleID` | `+0x30` | `int` | Pop 时定位元素的句柄。 |
| `FBaseFightingStateBehavior.m_bIsPersistent / m_iPersistencePriority` | `+0x00 / +0x04` | `bool / int` | PDB 能识别的“持久／持久优先级”字段；本批检视的更新、tick、highest-state 函数没有读取它们，行为消费者仍未定位。 |
| `FBaseFightingStateBehavior.m_SuperAvailabilityLayer` | `+0x08` | 对象指针 | `PushFightingState` 若取到非空值，会为该 FightingState 添加一层可用性上下文。 |

`EFightingState` / `EImpactType` 的关键枚举值：

| `EImpactType` | 值 | 本批可确认的状态更新映射 |
|---|---:|---|
| `Hit` | 0 | 普通命中；若目标当前有 `Dizzy`，更新函数有保留并重建该状态、转移累计字段的分支。 |
| `KnockDown` | 5 | 映射到 `EFightingState.KnockedDown (3)`。 |
| `Push` | 6 | 映射到 `EFightingState.Pushed (5)`。 |
| `Dizzy` | 7 | 映射到 `EFightingState.Dizzy (4)`。 |

## 命中分类：阈值并非单纯“保留动画时长”

`ComputeImpactType` 的一条重要分支会在分类结果返回前复查旧状态：

| 输入条件 | 分类函数的处理 | 可以下的结论 |
|---|---|---|
| `FImpactResult.m_eGuardType != EGuardType.None` | 仍从本次命中行取得 `FAttackPropertyLevel`，然后跳过正常的“攻击效果等级 vs 目标抗性”比较及其效果优先分支，转入后段阈值检查。 | 非 None 的 GuardType 改变命中分类路径；具体输出仍取决于后续字段和条件，不能只凭 GuardType 名称解释。 |
| `m_eGuardType == None` 且命中／防御组件有效 | 比较攻击属性等级的三项数值与目标 `UAttackPropertiesResistanceDB` 中对应抗性，构造位标记，再依据已有 `EFightingState` 选择分类。 | 分类由攻击属性、目标抗性和已有状态共同决定；本批未把三项 lane 的资产覆盖与所有效果优先条件列全。 |
| 初步输出类型为 `KnockDown(5)`、`Push(6)` 或 `Dizzy(7)`，且 `m_bKeepCurrentStateDuration=true` | 分别查询当前 `KnockedDown(3)`、`Pushed(5)` 或 `Dizzy(4)` 的时间；若找到该状态、剩余时间 `< m_fKeepCurrentStateThresold`、且该元素不是无限状态，就把本次 `EImpactType` 改为 `Hit(0)`。 | 这个字段组合有机会把再次产生的强受击分类降为普通 Hit；这是分类改变，不是仅仅把动画时长取 max。后续怎么更新旧状态还要经过 `UpdateFightingStateFromImpact`。 |

### 时间阈值分支的准确谓词

`BPF_GetFightingStateTimeLeft` 的直接实现只在防御组件状态数组中查找指定 `EFightingState`：找到后返回 `m_fStateDuration - m_fElapsedTime`，并分别输出“找到状态”和 `m_bInfinite`；找不到时两个输出均为 false、返回 0。

| 谓词 | 直接实现读什么 | 解释 |
|---|---|---|
| `active` | 是否找到对应状态元素 | 不是 AI 当前动作，也不是输入许可。 |
| `remaining` | `状态时长 - 已经过时间` | 源自 `FFightingStateElement` 两个 float。 |
| `infinite` | 状态元素 `+0x0C` | 由 `PushFightingState` 根据负时长写出。 |
| `paused` | 本 wrapper 和 `ComputeImpactType` 阈值分支都没有读取 `m_bPause (+0x00)` | 因此此处不能加“必须未暂停”的条件。Tick 会跳过 paused 元素的 elapsed 累加和累计阈值检查；分类分支只检查 active、剩余时间和 infinite。 |

分类降级条件可写作：

```text
攻击属性等级.m_bKeepCurrentStateDuration
且初步类型 ∈ {KnockDown, Push, Dizzy}
且对应状态存在
且状态剩余时间 < 攻击属性等级.m_fKeepCurrentStateThresold
且状态不是无限时长
→ 本次类型改为 Hit
```

例如，静态代码可以判定“剩余时间在阈值以下且有限的既有 Dizzy 会触发该类型降级分支”。它不能单独证明某个实际敌人、某招攻击配置或一次实战命中满足上述输入。

## 状态更新：首次、重复和切换

`UpdateFightingStateFromImpact` 先根据 `EImpactType` 决定目标 `EFightingState` 与角色 `UHitComponent` 内的句柄槽，再检查已有状态。它最终调用 `ApplyFightingStateFromImpact`；后者会在必要时 Pop 旧元素，计算新时长并调用 `PushFightingState`。

| 输入当前状态 / 新命中 | 更新前判断 | 旧元素处理与数据转移 | 新状态动作 | 证据边界 |
|---|---|---|---|---|
| 无对应状态 / 首次 `KnockDown`、`Push`、`Dizzy` | 对应 `GetFightingStateInfos` 未找到元素。 | 没有同类 handle 可 Pop；没有旧元素累计值可转移。 | `ApplyFightingStateFromImpact` 计算持续时间，然后 `PushFightingState` 追加新的 `FFightingStateElement`。 | 新元素还会读取目标抗性表中该状态的 `FPropertyReaction`；准确数值取决于具体资源配置。 |
| 已有 `KnockedDown` / 再次 `KnockDown` | `Update` 选择状态 3 和 `UHitComponent` 的 knocked-down handle 槽。 | `ApplyFightingStateFromImpact` 明确先 `PopFightingState(KnockedDown, 旧handle)` 并把槽清零。 | 随后 `PushFightingState` 新建元素，elapsed 重新从 0 开始；不是对旧数组元素原地加时。 | Apply 的状态 3 分支还会查询 `Dizzy(4)`；若该状态存在且非 infinite，会将当前局部时长与它的 remaining 比较取 max。 |
| 已有 `Dizzy` / 新命中 `Hit` | `Update` 发现 Dizzy 元素且新 `EImpactType==Hit`。若旧元素子状态是 `SuperDizzy`，仅在本次 guard-break 条件为真时走同一搬运分支。 | 复制当前元素的 `m_iAccumulatedHits (+0x20)`、`m_fAccumulatedDamages (+0x14)` 和子状态信息到下一次 Apply 参数；若 `s_bHasStructureOnly` 全局开关为真，先额外增加一次 hit count。随后 Pop 旧 Dizzy 并清空句柄。 | 以 `EFightingState.Dizzy` 再次调用 Apply/Push，创建新元素但带入转移的累计值／子状态。**没有读旧 `m_LastAttackName (+0x24)`，也没有把它作为 Push 参数传递。** | 直接证明代码有这条保留／重建分支；普通伤害 Impact 两路回调顺序已接通，但是否计到同一新元素仍取决于状态重建路径。 |
| 已有 `Dizzy` / 新命中为其他分类 | `Update` 发现 Dizzy 且新分类不是普通 Hit 的保留分支。 | 先 Pop 旧 Dizzy 并清 handle。 | 按新分类继续：可能创建 KnockedDown、Pushed 或新的 Dizzy，也可能不创建 FightingState。 | 具体结果取决于本次 `EImpactType` 与后续条件，不能概括成总是被新状态覆盖。 |
| 已有 `KnockedDown` / 新分类不是 `KnockDown` | 检查旧 KnockedDown 是否活动；同时检查 `FImpactResult.m_bGuardBreak (+0x08)`、`m_bAlreadyGuardBroken (+0x1A)` 和是否已有 Dizzy。 | 若没有 Dizzy 且两个标志都为 false，KnockedDown 分支可把旧 hit count 传入后续 Push；跨到非 KnockDown 时通常 Pop 旧状态，但这些状态／命中标志会改变分支。 | 然后按新类型执行 Apply 或普通命中路径。 | 字段语义已由 `FImpactResult` 类型布局核实；不得将这个分支推广为全部跨状态命中。 |
| 已有 `Dizzy` / 新强分类经阈值降为 `Hit` | `ComputeImpactType` 先把输出改成 Hit；进入 `Update` 后，命中的是“Dizzy + Hit”特殊分支。 | 转移累计命中／伤害和子状态，再 Pop 旧 Dizzy。 | 重建一个 Dizzy 状态元素，而不是把已过阈值的 KnockDown/Push/Dizzy 分类原样传下去。 | 这是“分类降级”与“旧状态更新”接在一起的静态链。当前缺具体资产配置实例和运行时观察。 |

### `PushFightingState` 与新旧元素

| 行为 | 汇编直接证据 | 解释 |
|---|---|---|
| 新增元素 | `UDefenseComponent::PushFightingState` 增加 `m_FightingStates` 数组计数，元素步长 `0x90`，写入新状态、handle、持续时间、累计阈值等。 | Push 自身不是按状态枚举覆盖旧元素。是否先 Pop 是上层决定。 |
| 计时初始化 | 新元素 elapsed `+0x08` 置 0；duration 写入 `+0x04`。 | 新建即重置 elapsed。 |
| 无限时长 | 对传入 duration 做 `< 0` 比较，并把结果写进 `m_bInfinite (+0x0C)`。`ApplyFightingStateFromImpact` 的默认局部时长初始化为 `-1`，但该默认值是否到达某条实际配置路径需由调用分支决定。 | 可确认“负时长会标无限”；不能把某个状态一概称为无限。`TickComponent` 遇到 infinite 元素会跳过时长和累计伤害／命中阈值检查；其他外部 Pop 路径仍可能移除它。 |
| 累计阈值 | Push 将调用参数写入 `FFightingStateElement` 中的最大伤害、累计伤害、最大次数、归组标记及当前次数。 | 这些值由调用链和状态的 Reaction 配置共同决定；字段存在不等于当前值已知。 |
| 可用性层 | `GetFightingStateBehavior(state)` 返回行为结构；Push 只在 `m_SuperAvailabilityLayer (+0x08)` 非空时，生成名为 `FightingState` 的可用性层上下文，并将其推入角色。 | 这是状态影响可用动作的一个真实接口；本批未确认不同 state 的配置内容或具体对玩家／敌人哪些动作起作用。 |
| Pop | `PopFightingState(state, handle)` 根据状态与 handle 定位元素并移除；已检查实现还调用元素绑定的移除回调，并在活动最高状态改变等条件下发变化事件。 | 旧状态移除可能连带清理回调／可用性状态；不只是数组删除。具体回调由谁绑定需沿其资源/代码再查。 |

### 同一状态再次命中时，哪些字段延续

`PushFightingState` 追加新元素，因此下表描述的是“旧元素被删、按参数新建”，不是对同一内存元素原地续写。

| 字段 | `Dizzy + Hit` 特例 | 同状态 `KnockDown` 重复命中 | 直接证据／边界 |
|---|---|---|---|
| `m_fStateDuration (+0x04)` | 重新走 Apply 的时长计算；是否把旧 remaining 纳入，取决于当前攻击等级的 keep flag 或 Reaction 的 always-keep flag。 | 同样重算；Apply 会 Pop 旧 KnockedDown 后创建新元素。 | 不保证总是沿用旧 duration。 |
| `m_fElapsedTime (+0x08)` | 新元素中直接写 0。 | 新元素中直接写 0。 | `PushFightingState` 初始化字段；计时从新元素重新开始。 |
| `m_fAccumulatedDamages (+0x14)` | `Update` 从旧元素读值，作为参数传入 Apply/Push；Push 将参数写入新元素。 | 该路径没有读取旧 KnockedDown 累计伤害；传入值来自 `Update` 初始 0 局部量。 | 只对已看到的 KnockDown 更新路径成立；不外推所有状态。 |
| `m_iAccumulatedHits (+0x20)` | 从旧 Dizzy 读值并传入；`s_bHasStructureOnly` 为真时，在搬运前额外 `+1`。Push 再写入新元素。 | 若旧 KnockedDown active、没有 Dizzy、且 `m_bGuardBreak` 与 `m_bAlreadyGuardBroken` 均为 false，则从旧 KnockedDown 复制 hit count；否则保留初始 0。 | 后续 `OnHit` / `OnDamage` 可由同一个普通伤害 Impact 按 `OnDamage → Update → OnHit` 顺序派发；中间状态重建会决定它们是否改到同一个新元素，见 `notes/20261029-rules-hit-count.md`。 |
| `m_LastAttackName (+0x24)` | `Update` 未从旧 Dizzy 读取该 FName，Push 调用也没有该参数。 | 未从旧 KnockedDown 读取或传入该 FName。 | `OnHit` 在 maxHits>0 时可能将当前 `FHitDescription+0x14` 写入此字段；Push 的默认构造如何初始化 FName 未在本批核实，不声称新建后必为 None。 |
| max damage / max hits / group flag | Push 按本次调用参数重写阈值，并从本次目标 Reaction 读取归组配置；没有整块复制旧元素。 | 一样由本次调用参数／目标 Reaction 写入。 | Push 的字段写入偏移 `+0x10/+0x18/+0x1C` 及调用参数已核。 |

字段写入端（只用于接续状态计数）：`UDefenseComponent::OnHit` 在元素 `maxHits (+0x18)>0` 时处理；归组开关 `+0x1C` 影响与 `m_LastAttackName (+0x24)` 的比较，进入计数路径后令 `m_iAccumulatedHits (+0x20)++` 并记录本次 `FHitDescription+0x14` 的攻击名。`OnDamage` 在 `maxAccumulatedDamage (+0x10)>0` 时将 damage 加到 `+0x14`；另在 `maxHits (+0x18)>0` 时将 `+0x20` 加一。OnDamage 不写 `m_LastAttackName`。已完成的 `notes/20261029-rules-hit-count.md` 证明普通伤害 Impact 可按 `OnDamage → UpdateFightingStateFromImpact → OnHit` 顺序派发两路回调；由于中间会改状态，不能说两路必然更新同一个 `FFightingStateElement`。

**SuperDizzy 不能并入上面的普通 Dizzy 计数结论。**`ESubFightingState.SuperDizzy=1`。`FImpactResult` 中 `m_bGuardBreak (+0x08)` 与 `m_bAlreadyGuardBroken (+0x1A)` 均为 bool；Update 开头仅当 guard-break 为真且 already-guard-broken 为假时令内部条件为真。已有 SuperDizzy 在该条件不成立时绕过普通 Dizzy+Hit 的搬运分支。进入对应 Apply 分支时，目标 `UAttackPropertiesResistanceDB.m_SuperDizzyReaction (+0x380)` 的子字段会单独提供 `mandatory duration (+0x00)`、max accumulated damage (`+0x04`) 和 max accumulated hits (`+0x08`)。这是代码和 PDB 类型能确认的不同配置入口；没有逐个 enemy resistance DB 核实其运行期实例值。

## 持续时间如何被保留或重算

不能按字段名排出“自定义 > 动画 > 保留 > 默认”的抽象优先级；`ApplyFightingStateFromImpact` 先按状态和传入容器走分支，下面是本函数的短路顺序。某些条件里使用的 `xmm6` 是分支局部时长，不一定是新抗性时长。

| 顺序／位置 | 条件／输入 | 实际选择 | 直接读写与边界 |
|---:|---|---|---|
| A `0x1A46AC1` | 当前待建状态是 Dizzy，且 Update 传入的特殊 guard-break 子条件为真 | 从目标 `UAttackPropertiesResistanceDB.m_SuperDizzyReaction (+0x380)` 读取 `m_fMandatoryDuration (+0x00)`，加本次 impact 时长偏移；之后继续创建 SuperDizzy。 | 这是 SuperDizzy 特殊入口，不等于普通 Dizzy duration。 |
| B `0x1A46AF6–0x1A46B2E` | 有可用的受击动画容器，并满足 Dizzy 相关门控 | 通过 `GetAnimDuration` 取动画时长，再加传入的 impact 偏移。 | 此分支早于自定义时长字段检查，具体容器 gating 需按输入类型读，不能概括为所有 Dizzy 均优先动画。 |
| C `0x1A46B33–0x1A46B3E` | 未被前两条接管，且 `m_bUseCustomDuration (+0x0C)` 为真 | 取 `m_fCustomDuration (+0x10)`。 | 后续走公共收尾路径；不要把字段排序误读成对 A/B 的全局优先级。 |
| D `0x1A46B43–0x1A46B2E` | 自定义时长没接管，`m_bUseHitAnimDuration (+0x14)` 为真且容器可用 | 取 `GetAnimDuration`，再加 impact 偏移。 | 若字段为真但没有容器，代码仍会落入后续判断。 |
| E `0x1A46B4F–0x1A46BBE` | 前述分支未接管，`m_bKeepCurrentStateDuration (+0x15)` 为真 | 查同类 FightingState 的 remaining/active/infinite。找到有限状态时，`max(remaining, xmm6)`；普通路径里 `xmm6` 初始为 0，不是已算好的新 duration。若查询未找到同类状态，0x1A46B76直接跳0x1A46BDF，保留普通局部0基线，不调用GetDuration，也不走公共offset加法。此前将此项写为默认回退是误读，修订见 `notes/20261029-state-spec-refinements.md` P3。 | 本字段在另一个函数 `ComputeImpactType` 还参与阈值降级；这里不是“旧剩余 vs 新抗性时长取 max”。无限状态、Reaction 与动画组合有额外分支。 |
| F `0x1A46B85–0x1A46BDA` | 上述攻击属性等级 keep 分支未接管，且目标 `FPropertyReaction.m_bAlwayKeepCurrentStateDurationOnHit (+0xA0)` 为真 | 查同类状态；找到时取 `max(remaining, xmm6)`，未找到时才调用 `GetDurationOfFightingState`。随后公共路径处理 impact offset。 | 普通路径中 `xmm6` 为 0；不能说它与“已新计算 duration”比较。它是 Reaction 层回退分支，和攻击属性等级 `+0x15` 不同。 |
| G `0x1A46BBC–0x1A46BDD` | 上述来源均未决定 duration | 调 `GetDurationOfFightingState`，使用目标 resistance DB 与当前状态计算；随后加本次 impact 时长偏移。 | 这是本函数的常规配置计算路径。 |
| H `0x1A46CA9–0x1A46CE6` | `m_bHoldDuringStructureBroken (+0xA2)` 为真 | 查当前 StructureBroken；若其 infinite 则令新 duration 为 `-1`，否则把其 remaining 与当前已选时长取 max。 | 这是附加的结构崩溃状态保留规则，限定于该反应分支。 |

### 重要区别：两个“保留当前状态时长”字段

| 字段 | 所属结构 | 对应层 | 不应混淆的效果 |
|---|---|---|---|
| `FAttackPropertyLevel.m_bKeepCurrentStateDuration (+0x15)` 和 `m_fKeepCurrentStateThresold (+0x18)` | 每个攻击属性等级 | 分类层 + 时长层 | 分类层检查旧状态剩余时间是否低于 threshold，可能把强效果分类降为 `Hit`；Apply 层另外用它进入当前状态时间分支。该 Apply 分支的普通路径把 remaining 与初始为 0 的 `xmm6` 比较，并非与重新计算出的 resistance duration 比较。 |
| `FPropertyReaction.m_bAlwayKeepCurrentStateDurationOnHit (+0xA0)` | 目标抗性表内的属性反应 | 时长计算层 | 在攻击等级 keep 分支未接管时，允许 Apply 在已有状态时使用 `max(remaining, xmm6)`；普通路径中 `xmm6` 为 0。它没有在本批找到分类降级消费者。 |

两者不等于“动画表现替换策略”。前者会在 `ComputeImpactType` 改变 `EImpactType`，并在 Apply 中控制是否查询旧状态时间；后者只影响 Apply 的另一个时长分支。Apply 中的动画、SuperDizzy、自定义、状态时间、Reaction 与默认抗性计算是有条件的分支树，不是所有配置都依次执行。最终选中的 duration 才被写进新的状态元素。

## 状态怎样退出

`UDefenseComponent::TickComponent` 遍历状态数组。以下是一个元素触发 Pop 的直接条件：

| 条件 | 必须满足的前置条件 | 代码判断 | 结果 |
|---|---|---|---|
| 时长到期 | `m_bInfinite==false` 且 `m_bPause==false` | 每 Tick 将 delta time 加进 elapsed；当 `elapsed > duration` 时调用 Pop。 | 结束该状态；只暂停元素或设为无限都会跳过这条时间路径。 |
| 累计伤害超过上限 | 状态元素未因 infinite/pause 提前跳过检查；`m_fMaxAccumulatedDamages > 0` | 当 `m_fAccumulatedDamages > m_fMaxAccumulatedDamages` 时 Pop。 | 这是严格大于；字段 0 或负数不启用该条阈值。 |
| 累计命中达到上限 | 状态元素未因 infinite/pause 提前跳过检查；`m_iMaxAccumulatedHits > -1` | 当 `m_iAccumulatedHits >= m_iMaxAccumulatedHits` 时 Pop。 | `-1` 及更小值不启用次数上限；达到上限即可 Pop。 |

**pause 与 infinite 的差异：**`TickComponent` 在检查顺序一开始就跳过 paused 或 infinite 元素，因此两者都不会继续执行该元素的计时和累计阈值移除。这里的“无限”只描述这段 Tick 的退出门，不代表其他显式 Pop 路径无法移除元素。

## 状态优先级与持久字段：当前能说到哪里

| 问题 | 已检查证据 | 结论／边界 |
|---|---|---|
| `GetHighestActiveFightingState` 如何选“最高”状态？ | 新增函数体完整反汇编：读 `UDefenseComponent+0x440` 状态数组，按代码中的固定 9 字节状态序列依次查找，找到第一个存在的状态即返回。 | 该函数不是按元素创建顺序，也没有读取 `m_iPersistencePriority`；本构建静态顺序来自 `EFightingState` 枚举 ID：StructureBroken → Dizzy → KnockedDown → Counter_Hit → Avoided → Parried → Pushed → InFight → OutOfFight。 |
| `m_bIsPersistent (+0)` 是否使状态不超时？ | PDB 确认字段是 bool；本批检查的 `PushFightingState`、`TickComponent`、`GetHighestActiveFightingState` 没有读取该字段。 | 未定位消费者，因此**不能**说它会让状态无限，也不能说它无效。 |
| `m_iPersistencePriority (+4)` 是否决定状态互相覆盖？ | PDB 确认字段是 int；同三函数中没有看到读取。最高状态来自硬编码 enum 顺序。 | 可能另有消费者；本批不把“priority”字段名当成实现机制。 |
| 状态元素的 `m_bInfinite` 与 `m_bIsPersistent` 是同一机制吗？ | 前者由 Push 的负时长写入，Tick 明确读取；后者在本批代码中未找到消费者。 | 不是可以互换的证据。 |

## 可复用的条件决策表

| 输入当前状态 / 事件 | 判断顺序 | 更新内容 | 对后续许可／压制的已知影响 |
|---|---|---|---|
| 新命中分类为 KnockDown/Push/Dizzy | 先由 `ComputeImpactType` 用输入结果、攻击等级、目标抗性与状态决定分类；keep-duration 阈值可能降为 Hit。 | 进入 `Update` 后选择相应 FightingState；需要时 Pop 当前 handle，再由 Apply 算时长并 Push 新元素。 | 新元素可附带 `m_SuperAvailabilityLayer` 对应的 availability context；这说明状态可能改变动作可用层，但具体攻击/防御请求的许可仍要另查。 |
| 新命中为 Hit，敌人已有 Dizzy | `Update` 特判现有 Dizzy。 | 把旧计数／累计伤害／子状态送往新元素参数，Pop 旧 Dizzy，Apply/Push 重建 Dizzy。 | 说明普通命中期间状态可被重建且累计值可能被带入；不能仅按单次时长算整个压制期。 |
| 目标有同类 FightingState，且时长规则允许保留 | Apply 查状态 remaining / active / infinite，并按实际控制流选择后续路径。 | 若走状态时间分支，`max` 比较对象是当前 remaining 与局部 baseline（普通路径为 0）；只有 StructureBroken 特例会把 remaining 与之前选定的时长作 max。 | 不存在“所有状态一律以旧剩余和新算 duration 取 max”的通则；最终能否连上仍取决于动作/许可/AI与具体命中。 |
| 新状态元素累计阈值达到 / 超过 | Tick 检查 max damage / max hits。 | Pop 元素并触发移除流程。 | 可成为压制窗口结束路径；具体累计数据何时记入以 `受击计数事件` 批次为准。 |
| 状态计时超过 duration | 元素非 pause 且非 infinite。 | elapsed 超过 duration 后 Pop。 | 单纯“攻击命中后还能接几拳”不能从 duration 字段直接换算；还需连接动作可用、距离/时序和 AI 选择。 |

## 本批证据索引

构建：本地 `Sifu-Win64-Shipping.exe` SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；匹配 PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d`，age 1。准确输入／输出哈希及命令见 [`inventory/rules-20261029-state-update.json`](../inventory/rules-20261029-state-update.json)。

| 证据 | 位置 | 本文使用点 |
|---|---|---|
| `UHitComponent::ComputeImpactType` | RVA `0x1A51F10`；`logs/system-recovery/UHitComponent__ComputeImpactType-0x1a51f10.asm.txt`，`0x1A51FD1–0x1A52233` | GuardType 分支、效果等级／抗性比较、当前状态优先和 keep-duration threshold 降级。 |
| `UHitComponent::UpdateFightingStateFromImpact` | RVA `0x1A70A70`；`logs/system-recovery/UHitComponent__UpdateFightingStateFromImpact-0x1a70a70.asm.txt` | 状态枚举映射、当前 Dizzy/KnockedDown 检查、旧 handle Pop、计数／子状态转移及调用 Apply。 |
| `UHitComponent::ApplyFightingStateFromImpact` | RVA `0x1A46990`；`logs/system-recovery/UHitComponent__ApplyFightingStateFromImpact-0x1a46990.asm.txt` | 状态特定的时长分支、已有状态剩余时间、StructureBroken 保持、同 KnockedDown Pop。 |
| `UDefenseComponent::PushFightingState` | RVA `0x1966D90`；`logs/followup-state-availability/UDefenseComponent__PushFightingState-0x1966d90.asm.txt` | append 新元素、duration/infinite、阈值/计数写入、可用性层。 |
| `UDefenseComponent::PopFightingState` | RVA `0x1966130`；`logs/stun-ai-state/UDefenseComponent__PopFightingState-0x1966130.asm.txt` | 按 state + handle 删除、移除回调与状态变化通知。 |
| `UDefenseComponent::TickComponent` | RVA `0x196A130`；`logs/stun-ai-state/UDefenseComponent__TickComponent-0x196a130.asm.txt` | pause/infinite 门、elapsed、damage 与 hit 上限 Pop。 |
| `UDefenseComponent::OnHit` / `OnDamage` | RVA `0x19653B0` / `0x1965280`；`logs/rules-20261029-count/UDefenseComponent__OnHit-0x19653b0.asm.txt`、`UDefenseComponent__OnDamage-0x1965280.asm.txt` | 命中次数、攻击名写入，以及累计伤害／次数更新入口；普通伤害 Impact 的两路顺序见 `notes/20261029-rules-hit-count.md`，是否改到同一状态元素仍看状态迁移分支。 |
| `UDefenseComponent::GetHighestActiveFightingState` | RVA `0x195C370`；本批新反汇编 `logs/rules-state-update-20261029/UDefenseComponent__GetHighestActiveFightingState-0x195c370.asm.txt` | 固定状态顺序，不读取持久优先级字段。 |
| `UDefenseComponent::BPF_GetFightingStateTimeLeft` | RVA `0x194FFA0`；本批新反汇编 `logs/rules-state-update-20261029/UDefenseComponent__BPF_GetFightingStateTimeLeft-0x194ffa0.asm.txt` | 查询剩余时间，输出 found / infinite；无 pause 检查。 |
| 类型与偏移 | `inventory/action-resilience-type-layouts.json`，目标 PDB 与当前 EXE 匹配 | 结构字段、bool/float/int 类型与枚举值。 |

## 明确未闭合的问题

| 缺口 | 不允许据此得出的说法 | 下一步最小取证 |
|---|---|---|
| `m_bIsPersistent` 和 `m_iPersistencePriority` 的真实消费者 | “persistent 一定无限”或“priority 决定本次状态覆盖顺序” | 对 PDB 字段布局定位可能持有 `FBaseFightingStateBehavior` 的数据访问函数／序列化后读取者，再对命中函数做单独反汇编。 |
| guard-break 结果标志在 KnockedDown→其他状态路径中的来源与作用 | 不能把条件外推成所有跨状态必 Pop／必保留 | 偏移已映射为 `FImpactResult.m_bGuardBreak` 和 `m_bAlreadyGuardBroken`；若主线需要解释产生条件，再沿 `GenerateImpact` 写者追它们的写入点。 |
| Reaction 和 AttackPropertyLevel 的实际配置引用 | 不能把代码分支当成普通/进阶杂兵的实用规则 | 定向取实际招式 hit row、目标 resistance DB、父级默认和难度覆写，并各自标明提取/解析/逻辑状态。 |
| 累计命中／伤害如何在具体普通命中上进账 | 不能把 `Push` 中有计数器等同于“每次攻击都会+1” | 与 `20261029-受击计数事件-01` 进行合并，确认委托触发对象和分组门。 |
| 屏幕表现和敌人 AI/可防御窗口的对应时刻 | 不能用状态剩余时间直接换算保证连段拳数 | 静态因果链闭合后，再给固定动作/难度/角色配置的最小实战观察方案；本批未启动游戏。 |

## 结论摘要

本构建中，新命中不是“每次硬直字段覆盖上一次”的单一规则。流程分三次决策：**分类函数**先结合 GuardType、攻击属性等级、目标抗性和当前状态，必要时用剩余时间阈值将强效果分类降为 Hit；**更新函数**再决定旧 Dizzy/KnockedDown 状态和累计信息如何 Pop、转移或重建；**Apply/Push**最后选时长并新增状态元素；**Tick/Pop**按时间、累计伤害、累计命中和 pause/infinite 条件结束元素。

因此可把“敌人不被无限连”拆成可查的状态维持、分类降级和退出条件，但这个系统本身还没有回答玩家可否出招、后续是否能命中、敌人 AI 是否实际格挡/反击。后续应以某一个真实启用的攻击配置与一个普通／进阶敌人配置接入这张规则表，而不是先按字段名给出通用连击结论。
