# 受击状态的累计命中与退出条件

> 当前结论绑定本机 Epic 版 `Sifu-Win64-Shipping.exe` / PDB。本文解释两个事件如何更新 `UDefenseComponent` 中每个持续战斗状态的累计字段。字段名和静态路径已核；不同状态实际收到的阈值、事件是否命中其配置分支仍须逐调用者确认。

## 先看结论

| 问题 | 已确认规则 | 边界 |
|---|---|---|
| 什么会累加累计伤害？ | 绑定到角色 `UHealthComponent.m_OnDamage` 的 `UDefenseComponent::OnDamage`，在该状态 `最大累计伤害 > 0` 时把事件参数中的伤害值加到累计伤害。 | 它不检查回调的 `bApplied` 参数；不是只有生命值真正下降时才计入。 |
| 什么会累加命中次数？ | `UHitComponent.OnHitDetection` 触发 `OnHit`；`UHealthComponent.m_OnDamage` 触发 `OnDamage`。两条计数来源都能由一个 Impact 引发。 | 两次回调之间还会更新状态；它们未必修改同一个状态元素，因此不能说一次命中必给同一个计数器加二。 |
| “按攻击名归组”对哪一路生效？ | 仅对 `OnHit` 这一路；同一个非空攻击名已记录时，后续相同名不再由 `OnHit` 增计。 | `OnDamage` 不检查攻击名或归组开关，仍每次回调加一。归组不是全局去重。 |
| 什么时候退出状态？ | 状态更新 Tick 中，经过时长、累计伤害、累计次数三个退出条件中的任意一个成立就 Pop。 | 计数回调只更新字段，不当场退出；暂停或无限状态会跳过整段计时与阈值检查。 |

## 两类回调如何进入状态字段

| 事件 | 角色组件字段 | 初始化时绑定 | 状态字段更新 | 代码证据 |
|---|---|---|---|---|
| Impact／受击通知 | `AFightingCharacter.m_HitComponent`（+`0x1328`，`UHitComponent*`）；其 `OnHitDetection`（+`0xE0`） | `UDefenseComponent::InitializeComponent` 将该动态委托绑定到本组件 `OnHit` | 对每个 `最大累计命中数 > 0` 的状态更新次数；按条件检查攻击名 | `InitializeComponent` RVA `0x19600C0`；`UHitComponent::OnHitDetection` 广播见 `ApplyImpact` RVA `0x1A46D90`、`0x1A484B9–0x1A484C8`；`OnHit` RVA `0x19653B0` |
| 生命伤害通知 | `AFightingCharacter.m_HealthComponent`（+`0x1350`，派生类 `UCharacterHealthComponent*`）；其基类 `UHealthComponent.m_OnDamage`（+`0xC8`） | 同一初始化函数将它绑定到 `UDefenseComponent::OnDamage` | 对每个 `最大累计伤害 > 0` 的状态加上事件传入伤害；对 `最大累计命中数 > 0` 的状态每次加一 | `InitializeComponent` RVA `0x19600C0`；`UHealthComponent::InternalApplyDamage` RVA `0x1A62E60`；`OnDamage` RVA `0x1965280` |
| 死亡通知（对照） | `UHealthComponent.m_OnDeath`（+`0x128`） | 绑定到 `UDefenseComponent::OnDeath` | 不更新本文两项累计字段 | `InitializeComponent` RVA `0x19600C0`；PDB 布局见下 |

PDB 类型布局确认：`AFightingCharacter` 的 +`0x1328` 是 `UHitComponent* m_HitComponent`，+`0x1350` 是 `UCharacterHealthComponent* m_HealthComponent`；`UCharacterHealthComponent` 以 `UHealthComponent` 为基类。基类委托字段为 `m_OnDamage` +`0xC8`、`m_OnDamageReceived` +`0xD8`、`m_OnDeath` +`0x128`。初始化函数绑定的是 `m_OnDamage`，不是相邻的 `m_OnDamageReceived`。

### 普通生命伤害 Impact 可同时走两路

| 顺序 | 静态执行路径 | 直接支持的结论 |
|---|---|---|
| 1 | `UHitComponent::ApplyImpact` 取得目标 `UHealthComponent`；当其伤害分支条件通过时，调用普通伤害闭包。调用点 `0x1A47165` 默认进入 lambda `0x1A44770`。 | 命中处理会把生命伤害送到目标健康组件，但需要该 Impact 的伤害分支条件成立。 |
| 2 | 闭包检查健康组件可受伤条件，构造 `FDamageInfos`，经虚函数槽 +`0x430` 调用健康组件的 `InternalApplyDamage`。 | 普通受击使用的对象实际是 `UCharacterHealthComponent`，调用经过派生覆盖。 |
| 3 | `UCharacterHealthComponent::InternalApplyDamage` 在 RVA `0x1A62AE0` 的开头先调用基类 `UHealthComponent::InternalApplyDamage`（`0x1A62B1F`），再处理派生层死亡／倒地逻辑。 | 派生实现没有绕过父类受伤委托，也未在父类调用前解除 `OnDamage` 绑定。 |
| 4 | 父类 `InternalApplyDamage` 在对应伤害事件分支广播 `m_OnDamage`：无实际应用路径在 `0x1A62EA6`（参数 `bApplied=false`）；常规应用路径在 `0x1A63095`（`bApplied=true`）。 | 两类广播都会调用 `UDefenseComponent::OnDamage`；其函数体不读取 `bApplied`。 |
| 5 | `ApplyImpact` 在健康伤害闭包之后、Hit 通知之前调用 `UpdateFightingStateFromImpact`（`0x1A47C7F`）；末段再于 `0x1A484C8` 广播目标 `UHitComponent.OnHitDetection`。 | `OnDamage` 先更新当时已有状态；Impact 随后可能退出、改写或重建状态；`OnHit` 再处理状态数组当时的内容。两次回调不是天然落在同一个 `FFightingStateElement` 上。 |

**因此，对于确实通过该生命伤害闭包、进入 `UCharacterHealthComponent::InternalApplyDamage`，并继续到 `ApplyImpact` 末段的普通伤害 Impact，两路委托可能都被派发，顺序是 `OnDamage → UpdateFightingStateFromImpact → OnHit`。** 但中间的状态更新可能更换当前状态元素：两次事件只有在同一累计元素被保留，或相关累计值被特定分支带入新元素时，才可能叠加到同一计数器。Dizzy 同态命中和 KnockDown 的字段传递已有不同分支，不能把任意状态切换简化成“每次命中必加二”。具体状态要按 `ApplyFightingStateFromImpact` 实际分支核查。不能把此结论推广到所有被称为“命中”的结果：零生命伤害、不可受伤、Impact 前置分流或未到达广播末段时，哪一路触发需看具体 Impact 分支。当前静态分析没有发现名为 `OnDamageNotFromHit` 的独立函数；这不等于证明不存在所有蓝图或外部调用造成的非战斗伤害事件。

状态重建会让这两项累计值采用不同的继承方式。已接到的分支证据显示：Dizzy 同态再次受击可把旧累计信息带入新状态；KnockDown 路径则在特定条件下只传入旧累计次数，没有同时传入旧累计伤害。因此，即使一个 Impact 先触发 `OnDamage` 再触发 `OnHit`，也需分别核对 `UpdateFightingStateFromImpact` 为当前状态选中的推入参数，确认两路回调是否落在同一累计元素上。定位：`UHitComponent::ApplyFightingStateFromImpact` RVA `0x1A46990`，状态参数组装 `0x1A46BEB–0x1A46D5C`；具体记录与 Push 布局见本批汇编及 PDB 类型表。

## 攻击名去重的精确边界

| 条件 | `UDefenseComponent::OnHit` 的行为 |
|---|---|
| `最大累计命中数 <= 0` | 不增加此状态的累计次数。 |
| 归组开关为 false | 每次 `OnHit` 回调增加一次。 |
| 归组开关为 true，攻击名与上次不同 | 增加一次，并记录本次攻击名。 |
| 归组开关为 true，攻击名与上次相同且非空 | 不增加。 |
| 归组开关为 true，名称为 `None` | 分支把 `None` 特殊处理；普通 `None` 名称不会按“同名攻击”去重，静态比较后仍增加。不要把缺省名称视作一个有效攻击组。 |
| 任一条件下进入 `OnDamage` | 如果 `最大累计命中数 > 0`，每次回调都增加一次；函数不读取归组开关、攻击名或 `bApplied`。 |

`OnHit` 的攻击名来自 `FHitDescription` 中 `m_Request.m_AttackRequest.m_AttackName`；嵌套 PDB 字段偏移为 `0x14`。`FFightingStateElement` 的“最后攻击名”字段位于元素 +`0x24`。

所以，归组只能减少一条来源的重复次数。例如相同命名攻击连续命中时，`OnHit` 可不重复加数；若同一状态元素仍存在，每次健康伤害回调仍可从 `OnDamage` 加数。**配置中的最大命中数不等于玩家可打的拳数，也不一定等于独立攻击数。**

## 每个状态元素与何时退出

`UDefenseComponent` 在 +`0x440` 保存状态数组；`FFightingStateElement` 每项大小 `0x90`。以下均为元素内偏移：

| 字段 | 偏移 | 作用 |
|---|---:|---|
| `m_fStateDuration`（状态时长） | `+0x04` | Tick 中与累计经过时间比较。 |
| `m_fElapsedTime`（已过时间） | `+0x08` | 非暂停、非无限状态每 Tick 增加 DeltaTime。 |
| `m_bInfinite`（无限状态） | `+0x0C` | 为真时跳过该状态的时间和阈值退出检查。 |
| `m_fMaxAccumulatedDamages`（最大累计伤害） | `+0x10` | 大于 0 时启用累计伤害退出阈值。 |
| `m_fAccumulatedDamages`（累计伤害） | `+0x14` | 由 `OnDamage` 增加。 |
| `m_iMaxAccumulatedHits`（最大累计命中数） | `+0x18` | 大于 -1 时启用累计次数退出阈值。 |
| `m_bGroupMaxAccumulatedHitsByAttack`（按攻击名归组） | `+0x1C` | 只被 `OnHit` 的名字比较读取。 |
| `m_iAccumulatedHits`（累计命中数） | `+0x20` | 可由两路事件分别增加。 |
| `m_LastAttackName`（上次攻击名） | `+0x24` | `OnHit` 用于同名比较。 |

| Tick 检查 | Pop 条件 | 比较边界 |
|---|---|---|
| 暂停／无限 | `m_bPause` 或 `m_bInfinite` 为真时跳过整段有限状态处理。 | 不是只暂停计时；伤害和次数的退出检查也一并跳过。 |
| 时间 | `m_fElapsedTime > m_fStateDuration` | 严格大于；相等时尚未满足。 |
| 累计伤害 | `m_fMaxAccumulatedDamages > 0` 且 `m_fAccumulatedDamages > m_fMaxAccumulatedDamages` | 严格大于；达到相等值尚未满足。 |
| 累计次数 | `m_iMaxAccumulatedHits > -1` 且 `m_iAccumulatedHits >= m_iMaxAccumulatedHits` | 大于等于。`-1` 禁用次数阈值。 |

检查入口为 `UDefenseComponent::TickComponent` RVA `0x196A130`，状态数组循环和 `PopFightingState` 调用位于 `0x196A2C0–0x196A326`。满足任一可用条件，Tick 才调用 `PopFightingState`；两个回调自身没有直接 Pop。`PushFightingState` RVA `0x1966D90` 初始化默认值后会用调用参数覆盖累计伤害／次数等字段，具体状态应回到该状态的实际调用方核参数，不能把默认值当全局规则。

## 证据索引与结论层级

| 对象 | 定位 |
|---|---|
| 本批 EXE／PDB 构建 | `inventory/rules-20261029-count-batch.json`；EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`，PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age 1。 |
| 类型与字段偏移 | `inventory/rules-20261029-count-target-layouts.json`；PDB 仅证明布局及委托／函数类型，不单独证明触发。 |
| 注册、命中通知、健康事件、状态进入与退出 | `logs/rules-20261029-count/` 下的 `UDefenseComponent__InitializeComponent`、`UHitComponent__ApplyImpact`、`UCharacterHealthComponent__InternalApplyDamage`、`UHealthComponent__InternalApplyDamage`、`UDefenseComponent__OnHit`、`UDefenseComponent__OnDamage`、`UDefenseComponent__TickComponent`、`UDefenseComponent__PushFightingState` 汇编。 |

- **已解析／已接通静态逻辑**：PDB 字段布局；两条委托的初始化绑定；`ApplyImpact → UCharacterHealthComponent::InternalApplyDamage → UHealthComponent::InternalApplyDamage → OnDamage` 与 `ApplyImpact → OnHitDetection → OnHit` 两条链；分别更新哪些字段；Tick 的 Pop 条件。
- **尚未实战验证**：每个敌人和每个招式的实际分支、某次 Impact 是否同时走生命伤害与末段通知、最终恢复时刻。需要运行时验证时，应观测同一状态元素的累计值与两类委托调用，而不是把屏幕上看见的“打中一次”直接当一个内部计数单位。
- **适用边界**：任何配置的伤害阈值、计数阈值、攻击名分组开关都属于特定状态调用参数；需按调用者与资产覆盖逐例核对。这里不推导固定拳数、普遍防无限连机制或 AI 选招原因。
