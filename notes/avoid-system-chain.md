# 闪避后的可追击链：HitBox 标记、避免属性与眩晕状态

## 本轮结论

已确认一条按攻击 HitBox 分流的静态因果链：**玩家成功避免某个敌方攻击时，防御过滤会按该攻击 HitBox 的 `m_bDizzyOnAvoid` 选择 `UAvoidPropertyDB`，并把它存进避免结果。确认成功后，`UAttackComponent::ScheduleOrderOverAttack` 将 Avoided 订单安排到原攻击者；`AFightingCharacter::HandleOrderOverAttack` 随后在原攻击者上 `PlayOrder(EOrderType::Avoided=5)`，把包含原 `FHitDefenseResult` 的数据和 DB 时长写进订单。之后原攻击者受击时，`UHitComponent::GenerateImpact` 从该受击者当前的 Avoided 订单中取回原避免 DB。若 DB 的 `m_bAvoidedEnterDizzyOnAttacked` 为真，Impact 带上 AvoidDizzy；满足状态条件后，该受击者进入 `EFightingState::Dizzy`。因此被眩晕的是仍处于 Avoided 订单窗口内、受到玩家后续命中的原攻击者；成功 Avoid 回调本身不会直接推入 Dizzy。

这条链解释了为什么部分被避开的敌招会在反击命中时附加眩晕，并给出一个有配置时长的原攻击者反应窗口；不能推广成所有攻击、所有敌人都必然眩晕。用户的“闪避反击”是操作描述；内部避免成功、原攻击者的 Avoided 订单、HitBox 标记和后续命中后的 `Dizzy` 状态分属不同环节。

## 已确认因果链

```mermaid
flowchart TD
    A[玩家避免敌方攻击成功] --> B[按该攻击 HitBox 选择 AvoidPropertyDB]
    B -->|m_bDizzyOnAvoid = true| C[取 DB.m_AvoidDBOnDizzyAttack]
    B -->|false| C0[保留普通 AvoidPropertyDB]
    C --> D[FilterHit 将 DB 存入 FHitDefenseResult]
    C0 --> D
    D --> E[在原攻击者 UAttackComponent 排队 Avoided order]
    E --> F[成功后在原攻击者 PlayOrder(5)]
    F --> G[订单保存原 DefenseResult 与反应时长]
    G --> H[原攻击者在 Avoided 订单期间受击]
    H --> I[GenerateImpact 从目标当前订单取回原 Avoid DB]
    I -->|m_bAvoidedEnterDizzyOnAttacked = true| J[FImpactResult.m_bAvoidDizzy = true]
    J --> K{ImpactType != 4/10 且 m_bSuperDizzyAvailable}
    K -->|满足| L[ApplyFightingStateFromImpact: EFightingState::Dizzy]
    L --> M[按目标 AttackPropertiesResistanceDB 推入有时长的状态]
    M --> N[状态时间到期/停止回调，AI 防御处理器收到到期通知]
```

| 环节 | 直接证据 | 可下的结论 | 边界 |
|---|---|---|---|
| Avoid 成功传递及原攻击者订单 | `UDefenseComponent::FilterHit` RVA `0x1957FF0` 从 `FHitRequest.m_Instigator`（偏移 `0xE4`）取原攻击者；在其 `UAttackComponent`（角色偏移 `0x1308`）调用 `ScheduleOrderOverAttack`，参数 `EOrderType=5`，并保存 HitRequest/DefenseResult。避免成功后对同一原攻击者调用 `HandleOrderOverAttack` | `HandleOrderOverAttack` 从保存的 FHitDefenseResult 读取 DB，在原攻击者上 `PlayOrder(5)` | 成功避免只建立 Avoided 订单，不在回调里直接进入 Dizzy |
| HitBox 分流 | `UDefenseComponent::FilterHit` RVA `0x1957FF0` 于 `0x19584B6` 调用 `GetActiveAvoidMatchingAttack`；该函数 RVA `0x195A360` 的签名输出 `UAvoidPropertyDB*&`，在 `0x195A3FC–0x195A410` 取 HitBox 行并检查 `[row+0x1B0]`；真时将输出 DB 换成 `[currentDB+0x68]`。`FilterHit` 随后将 DB 写入 `FHitDefenseResult.m_DB`（偏移 +8），设置类型/是否命中被消解，并进入成功通知 | `FHitboxDataRow.m_bDizzyOnAvoid`（布局偏移 432）为真时选择 `UAvoidPropertyDB.m_AvoidDBOnDizzyAttack`（偏移 104）；字段名相近但各自作用不同 | 返回的 `EAvoidType`、具体 HitBox 和 DB 必须与实际攻击匹配；本轮没运行游戏验证具体招式时序 |
| Avoided 订单与计时 | `AFightingCharacter::HandleOrderOverAttack` RVA `0x19C0590` 调 `PlayOrder` 类型 5；复制 `UAvoidPropertyDB.m_fAvoidedDuration`（偏移 `0x50`）到 `FNetOrderStructAvoided.m_fAvoidDuration`（偏移 `0x4A0`）。`OrderAvoided::OnStart` RVA `0x1ADE250` 将值写到订单总时长/剩余时长（`+0x1B0/+0x1B4`）；`OnUpdate` RVA `0x1AE3A30` 按 delta 递减，剩余时间到 0 时 `RequestStop` | `m_fAvoidedDuration` 是原攻击者 Avoided 反应订单的总时长，不是 Dizzy 状态时长；订单运行时使用 `m_AvoidedAttackScaleCurves` 更新匹配的攻击订单 | 只有所选 Profile 与原攻击 HitBox 匹配时才应用对应值；可能被外部取消提前停止 |
| 避免属性 | `FHitDefenseResult::GetAvoidDB` 返回 `UAvoidPropertyDB`；`FilterHit` 已确认该 DB 被写到结果 `m_DB`（偏移 +8）；订单 `FNetOrderStructAvoided` 保存 `FOrderOverAttackInfo`，命中结算从当前 Avoided 订单读回原 DefenseResult | DB 从原攻击者 Avoided 订单进入该受击者的 `GenerateImpact`，连接原避免事件与后续命中 | Profile 选择仍受活跃 Avoid、方向和攻击匹配影响 |
| 后续命中附加标记 | `UHitComponent::GenerateImpact` RVA `0x1A5A610` 查询当前受击目标的 `EOrderType=5`（`0x1A5B1F0–0x1A5B205`），从 OrderBase `+0x48` 取 FNetOrderStruct，再从结构内取原 `FHitDefenseResult` 调 `GetAvoidDB`；`[db+0x61]` 为真时写 `FImpactResult.m_bAvoidDizzy`（偏移 191 / `+0xBF`） | `UAvoidPropertyDB.m_bAvoidedEnterDizzyOnAttacked`（偏移 97）参与生成 Impact 标记；当前受击目标正是原 Avoided 订单持有者 | 不是 HitBox 字段直接写入 Impact；HitBox 字段先选择原 Avoid DB |
| 状态转移 | `UHitComponent::UpdateFightingStateFromImpact` RVA `0x1A70A70` 在 `0x1A70CB6–0x1A70D08` 检查 `m_bAvoidDizzy`、`m_bSuperDizzyAvailable`，满足条件并排除 ImpactType 数值 4、10 后调用 `ApplyFightingStateFromImpact`；参数里的 FightingState 为 4 | 按匹配 PDB 枚举，`EFightingState::Dizzy=4`；这一步作用于刚才从当前 Avoided 订单取回 DB 的受击者，即原攻击者 | 标记为真仍不足以保证眩晕：ImpactType 与 SuperDizzy 条件会分流 |
| 眩晕持续与恢复 | `UHitComponent::ApplyFightingStateFromImpact` RVA `0x1A46990` 取得目标 `UAttackPropertiesResistanceDB`，查询状态反应/时长并通过 `UDefenseComponent::PushFightingState` 写入状态；`UHitComponent::LaunchFightingStateOrder` RVA `0x1A64610` 读取状态动画、动态 Blend 与恢复动画；`FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero` RVA `0x18BD1A0` 处理状态到期通知 | 眩晕是一个有目标抗性配置时长和恢复/到期路径的战斗状态，不等同于 Avoid DB 的 `m_fAvoidedDuration` | 普通／进阶杂兵各自最终时长、状态是否被打断，以及到期后具体 AI 选择仍需把对应抗性资产与行为条件映射完 |

## 本机构建的配置依据

来源为本地提取表 `inventory/object-and-table-properties.csv`；本轮选出的行另存于 [system-avoid-config-samples.csv](../inventory/system-avoid-config-samples.csv)。配置值证明资产中存了什么，不单独证明某次实战触发。

| 配置对象 | 字段 | 值／引用 | 含义 |
|---|---|---|---|
| `MainChar_Avoid_AvoidDB` | `m_AvoidDBOnDizzyAttack` | `MainChar_Avoid_AvoidPunishable` | 玩家普通 Avoid 配置可按敌方 HitBox 标记切换到特殊属性 DB |
| `MainChar_Avoid_AvoidPunishable` | `m_bAvoidedEnterDizzyOnAttacked` | `True` | 命中影响结算读到该属性结果且满足条件时，Impact 可标为 AvoidDizzy |
| 同上 | `m_fAvoidedDuration` | `0.6660000086` 秒 | 写入原攻击者 Avoided 订单的总/剩余反应时间；该值不是敌人 Dizzy 状态时长 |
| `MainChar_Attack_AvoidDB` | `m_AvoidDBOnDizzyAttack` | `MainChar_Attack_AvoidPunishable` | 玩家攻击能力使用另一条 Avoid 配置分支 |
| `MainChar_Attack_AvoidPunishable` | `m_bAvoidedEnterDizzyOnAttacked` | `True` | 若该 AvoidPropertyDB 作为原避免结果 DB 被存入 OrderAvoided，后续对原攻击者的命中可设置 AvoidDizzy；其 `m_fAvoidedDuration=0.5` 秒写入该订单的时长字段 |
| `MainChar_Avoid_AvoidDB` | 成功后输入层 | 立即推 `AllDefensiveOptions`；延迟 `0.08` 秒推 `Punishable_AvoidSuccess` | 这是玩家可用输入层，不能解释成敌方防御许可被关闭 |
| 普通 Grunt HitBox 表 | `m_bDizzyOnAvoid` | `Hook_HB01=True`，`Jab_HB01=False`，`Knee_HB01=False`，`Elbow_HB01=False`，`BaseballHook_HB01=True`，`FalconPunch_HB01=True` 等 | 同一套普通杂兵攻击里已经有按招式分流；例如 Hook 与 Jab 的配置不同 |

`MainChar_Avoid_AvoidPunishable.m_bShouldEndCombo=False`。`OrderAvoided::OnStart`（RVA `0x1ADE250`，`0x1ADE49A–0x1ADE4C3`）另有逻辑：只有 HitBox `m_bDizzyOnAvoid` 为真且所用 DB 的 `m_bShouldEndCombo` 也为真，才调用 `UPlayerFightingComponent::EndCombo`。本机构建的该玩家 Punishable DB 不满足第二条件，因此这个分支不会结束玩家连招；它与敌方的 Dizzy 状态链不是同一个机制。

## AI 感知、ComboEnd 枚举与反击的区别

| 线索 | 证据及作用 | 当前判定 |
|---|---|---|
| AI 收到玩家避免成功 | `UAIFightingComponent::OnOrderAvoidedStarted` RVA `0x18BCFD0` 解出 `FNetOrderStructAvoided` 中 HitRequest 并广播；`OnTargetAvoidSuccess` 更新目标 Dodge/Avoid 成功的 AI memory | 证明 AI 会收到事件并记忆，不证明它直接进入 Dizzy 或关掉格挡 |
| `EHitDismissReason=11` | `UDefenseInfluenceNodeAvoid::OnNonDismissedHit` RVA `0x1893F50` 在 DefenseHandler 条件满足时写 `0x0B`；参数确为 `EHitDismissReason`，但匹配 PDB 的 `EHitDismissReason` 类型记录没有枚举成员 | **实际成员名无法从这份 PDB 得出**。不要将其解释为 `PunishableAvoided` |
| `EComboEndReason::PunishableAvoided=11` | 枚举本身在匹配 PDB 类型记录中存在；但当前避免分流链没有证明 `OnNonDismissedHit` 写的 byte 被作为该 ComboEndReason 消费 | 同数值不同枚举，不能据此建立调用因果 |
| 防御回调 | `FAIAttackHandler::OnDefending`（RVA `0x1890F40`）以 `EComboEndReason::Defending=6` 结束 AI combo；`EndCombo` 清理攻击准备、当前 AI action、trace 请求和有效条件记忆 | 这是 AI 决定防御时的 Combo 清理路径；不是成功 Avoid 的通用结果 |

## 系统线索登记

| 因素与作用位置 | 依据／已知作用 | 关联与缺口 | 优先级／回查入口 |
|---|---|---|---|
| 攻击 HitBox `m_bDizzyOnAvoid`：避免 DB 选择 | `GetActiveAvoidMatchingAttack` 的 RVA 与偏移检查；普通 Grunt HitBox 表含 true/false 混合 | 要将玩家观察到的敌人招式映射到具体命中段，核对普通/进阶是否复用该行 | 直接关联；本篇“HitBox 分流”与样本 CSV |
| `UAvoidPropertyDB`：避免后的结果与允许输入 | `MainChar_Avoid_AvoidDB -> MainChar_Avoid_AvoidPunishable`；Avoid 成功函数还推输入可用层 | 输入层只证明玩家哪些输入被开放；不能推出敌方失去防御许可。需结合玩家招式命中时序 | 直接关联；本篇配置表与 `HandleAvoidSuccessful` 反汇编 |
| `m_bAvoidedEnterDizzyOnAttacked`：后续命中生成状态标记 | `GenerateImpact -> FImpactResult.m_bAvoidDizzy -> UpdateFightingStateFromImpact`，目标是原 Avoided 订单持有者/原攻击者 | 还缺具体敌人 `m_bSuperDizzyAvailable` 与抗性配置的普通/进阶映射 | 直接关联；本篇“状态转移” |
| AI Avoid 成功记忆 | `OnOrderAvoidedStarted`、`OnTargetAvoidSuccess`、`UpdateMemoryUnitForTargetDodgeOrAvoidSuccess` | 可能影响之后的 AI 选招/决策；本轮没有把 memory 读取点接到防御决策 | 直接关联但不阻塞当前眩晕链；`logs/system-avoid/UAIFightingComponent_*` |
| `m_bDizzyOnParry` 和 GuardAbility | `BP_GuardAbility` 的 `m_ParryDizzyHit` 配置引用 `ParryDizzy_HB01`，HitBox 行可见 `m_bDizzyOnParry=True`；父任务在查相应 GuardAbility 回调 | 与本篇避免路径同构但使用 Parry 字段和防反 Impact，不能把两者并为同一配置 | 后续对照；避免在本篇替代防反研究结论 |
| `EHitDismissReason` byte 11 | PDB 有类型名但无 enumerator | 缺真正成员名及其下游消费点 | 记录缺口；若找到类型生成数据/源码再扩展；不阻塞 Avoid→Dizzy 结论 |

## 静态边界与最小验证

静态分析已闭合从避开攻击、原攻击者 Avoided 订单，到后续命中读取同一 Avoid DB 并可能进入 Dizzy 的代码路径；仍未证明普通/进阶敌人具体招式、命中段与玩家实战现象一一对应。要对应用户说的“某些连招”，最小运行时验证应在普通难度下选两条共享敌人的攻击：一条 `m_bDizzyOnAvoid=True`，一条为 `False`；每条只做“成功避开后立即用同一徒手招式命中”，观察命中的是谁、第一击是否进入眩晕动画／状态、后续是否可被普通格挡，以及状态何时恢复。需同时记录命中段、当时武器/姿态和第一击是否被挡，避免把没有命中等同于防御许可差异。本轮未启动游戏，也未做运行时操作。

后续静态取证的最小缺口是：把普通／进阶 Grunt 当前可用攻击引用到 HitBox 行，再把两者 `UAttackPropertiesResistanceDB` 的 `Dizzy` 时长/动态响应接到同一个 `PushFightingState` 路径。随后再查 Dizzy 期间 Guard/Deflect 许可是否单独变化，以及 `OnOrderFightingStateTimeLeftReachedZero` 之后由哪些 AI 票据恢复出招。实战只需先对比一条 `m_bDizzyOnAvoid=True` 与一条 False 的敌招，记录成功 Avoid 后原攻击者的 Avoided 动画/减速窗口，以及后续命中是否进入 Dizzy；不要把 0.5/0.666 秒当作 Dizzy 时长。

本轮匹配构建为 `Sifu-Win64-Shipping.exe` / PDB，哈希 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；反汇编清单 `inventory/system-avoid-disassembly.json` 记录工具、函数范围与哈希。只读本机构建数据与代码；没有运行游戏，没有修改游戏、存档或 LIAN。

## 补证：攻击订单绑定、许可层和普通／进阶招式映射

> 本节补齐上文“最小缺口”里已经由本轮静态证据解决的部分。较早段落中“仍需映射攻击行”的说法，以本节表格为准。

### 避免订单是否匹配原攻击

`OrderAvoided::OnUpdate`（RVA `0x1AE3A30`）每帧查询角色当前 `OrderAttackInterface`（调用 `GetOrderWithInterface`，`0x1AE3AED`），从接口取当前订单 ID 字节（虚调用后 `[rax+0x38]`），与 Avoided 网络数据保存的原攻击订单 ID（`FNetOrderStructAvoided+0x409`）比较（`0x1AE3B03–0x1AE3B0D`）。相同才从 DB 曲线取值并写回该 OrderAttack 的时间缩放（`0x1AE3B16–0x1AE3B50`）；不匹配或找不到曲线时不调用缩放 setter。这确认了**时间缩放曲线只针对原攻击订单**。

但 `UHitComponent::GenerateImpact`（RVA `0x1A5A610`，`0x1A5B1F0–0x1A5B205`）的惩罚标记读取只要求当前受击目标有 `EOrderType::Avoided=5`，再由订单 payload 取回 DB；这里没有将本次命中攻击 ID 与原避免攻击 ID 比较。因此“原攻击匹配”只证明减速作用对象，不证明后续惩罚命中也必须是同一招式/同一攻击订单。

### Avoided 许可层及其生命周期

| 阶段 | 证据与对象 | 已确认作用 | 尚未确定 |
|---|---|---|---|
| 生成并推入 | `UDefenseComponent::FilterHit` RVA `0x1957FF0`：从 `FHitRequest+0xE4` 解析原始 instigator；`0x19585A1–0x19585EF` 取 `UOrderAvoidedDB` 并读取 `+0x108`，调用 `GenerateAvailabilityLayer`；`0x195862A–0x1958631` 对解析出的原始攻击者调用 `AFightingCharacter::PushAvailabilityLayer` | 许可层施加在原攻击者；返回 handle 存进排队的 `FOrderOverAttackInfo+0x474`，context 为 `+0x478` | `UOrderAvoidedDB` 本机具体实例/CDO 的 `m_AvailabilityInfo` 内容尚未解出，不能把作用细化成 Guard、Deflect 或特定 AI 动作禁用 |
| DB 字段定义 | 匹配 PDB 的 `UOrderAvoidedDB` 类型布局：`m_AvailabilityInfo` 偏移 264（`+0x108`），类型 `FAvailabilityLayerContainer`；反汇编读取位置一致 | 这层由订单 DB 的 AvailabilityInfo 提供，而非玩家 AvoidPropertyDB 的成功输入层 | 容器最终生成哪些许可 bit，及 AI 行为系统如何消费，需追相应 LayerData 与许可查询 |
| 订单结束撤销 | `OrderAvoided::OnStop` RVA `0x1AE1340`：`0x1AE13AD–0x1AE13D7` 从 `FNetOrderStructAvoided+0x4A4/+0x4A8` 读 handle/context，在订单 owner 上调用 `PopAvailabilityLayer`。新订单替换旧 queued record 时，`HandleOrderOverAttack` RVA `0x19C0590` 的 `0x19C0643–0x19C065C` 也 Pop 旧 handle | 许可层具有订单/队列生命周期，不是永久旗标 | 是否有其他并行层延长或覆盖它，需看其他订单及层优先级 |
| 与惩罚标记的关系 | `GenerateImpact` 对当前 `OrderType::Avoided` 的查询和 DB 读取；OnUpdate 到时 `RequestStop`（`0x1AE3B83–0x1AE3B8B`），OnStop 做 Pop | 当前证据支持：Avoided 订单存在时可取 DB 生成 AvoidDizzy；订单结束后没有独立永久 punishable 标志可从此路径读取 | OrderComponent 将订单标为非运行/移出可查询集合的精确时序及同帧边界，需追通用订单停止实现或运行时观测 |

这层与 `AFightingCharacter::HandleAvoidSuccessful`（RVA `0x19BE620`）中玩家角色获得的成功输入层不同：Avoided 订单用的是 `UOrderAvoidedDB.m_AvailabilityInfo`；玩家避免成功路径则从自身 `UAvoidPropertyDB` 的成功/延迟层配置操作。不要用 `Punishable_AvoidSuccess` 资产解释 AI 原攻击者的许可。

### 普通／进阶裸手 Hook 与 Jab 的实际引用

以下为本地配置表中的组合节点到具体攻击资源的引用。`m_Attacks[*]` 数组的同节点四个位置引用相同攻击资产；同一个共享攻击资产再通过敌人 HitBox 表取行。

| 敌人组合配置 | 节点 | 实际攻击资源 | 对应 HitBox 行 | `m_bDizzyOnAvoid` |
|---|---|---|---|---|
| 普通：`Sifu/Content/DB/AI/Archetypes/Grunt/_Base/Grunt_Base_Combo.uasset` | `m_Nodes[0].element[1].m_AttackInfos[0].m_Attacks[*]` | `/Game/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_Hook.Grunt_Hook` | `Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/Grunt_HitBoxData.uasset` → `Hook_HB01` | `True` |
| 普通：同上 | `m_Nodes[0].element[11].m_AttackInfos[0].m_Attacks[*]` | `/Game/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_StraightJab.Grunt_StraightJab` | 同表 → `Jab_HB01` | `False` |
| 进阶：`Sifu/Content/DB/AI/Archetypes/Grunt/_Advanced/Grunt_Advanced_Combo.uasset` | `m_Nodes[0].element[1].m_AttackInfos[0].m_Attacks[*]` | `/Game/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_Hook.Grunt_Hook` | 同表 → `Hook_HB01` | `True` |
| 进阶：同上 | `m_Nodes[0].element[17].m_AttackInfos[0].m_Attacks[*]` | `/Game/DB/AI/Archetypes/Grunt/Attacks/BareHands/Grunt_StraightJab.Grunt_StraightJab` | 同表 → `Jab_HB01` | `False` |

上述是“组合资源确实引用共享 Hook/Jab，并且共享 HitBox 行如何配置”的静态证据；并不证明普通难度实战必定在指定时刻选中节点，也未覆盖所有变体/分支。完整关键行筛选保存在 [system-avoid-specific-config.csv](../inventory/system-avoid-specific-config.csv)。

### Dizzy 相关时间字段（资产配置值）

| 抗性资源 | 状态矩阵 `InFight` 的 Dizzy resistance | `Dizzy` 行的 Dizzy resistance | `m_DizzyReaction[0].m_Movement[0].m_fDuration` | `m_SuperDizzyReaction[0].m_fMandatoryDuration` |
|---|---:|---:|---:|---:|
| `Sifu/Content/DB/AI/Archetypes/Grunt/Resistance/Grunt_Base_ResistanceDB.uasset` | 11 | 1 | 3.0 秒 | 5.0 秒 |
| `Sifu/Content/DB/AI/Archetypes/Grunt/Resistance/Grunt_Adv_ResistanceDB.uasset` | 11 | 1 | 1.5 秒 | 5.0 秒 |

匹配 PDB 布局将 `UAttackPropertiesResistanceDB.m_DizzyReaction` 定位在 +0x290，`FPropertyReaction.m_Movement` 在 reaction +0x10；`UAttackPropertiesResistanceDB::GetDurationOfFightingState` RVA `0x19F58B0` 对 `EFightingState::Dizzy=4` 取对象 +0x290，再读 reaction +0x1C，即本机布局与配置表的 `m_DizzyReaction[0].m_Movement[0].m_fDuration`。`UDefenseComponent::GetDurationOfFightingState` RVA `0x195BD30` 在目标当前状态不同于请求状态时透传该值；相同则返回 -1。`UHitComponent::ApplyFightingStateFromImpact` RVA `0x1A46990` 将该返回值与 Impact 的额外 duration 修正相加，再传给 `PushFightingState`（call RVA `0x1A46D5C`）。因此普通 Grunt 3.0 秒、进阶 Grunt 1.5 秒是普通 Dizzy 的配置基础时长；最终值还可能包含 Impact duration 修正，且相同状态重复命中存在特殊 -1/维持逻辑。`m_fMandatoryDuration` 属 SuperDizzyReaction，不能套给普通 Dizzy。具体场景的修正值与计时器叠加/重置边界仍待确认。

### 本轮精确回查入口

- `logs/system-avoid/UDefenseComponent__FilterHit-0x1957ff0.asm.txt`
- `logs/system-avoid/AFightingCharacter__HandleOrderOverAttack-0x19c0590.asm.txt`
- `logs/system-avoid/OrderAvoided__OnStart-0x1ade250.asm.txt`
- `logs/system-avoid/OrderAvoided__OnUpdate-0x1ae3a30.asm.txt`
- `logs/system-avoid/OrderAvoided__OnStop-0x1ae1340.asm.txt`
- `inventory/system-parry-type-layouts.json` → `UOrderAvoidedDB::m_AvailabilityInfo`
- `inventory/system-avoid-specific-config.csv`

### OrderAvoided 的本机默认许可层已补出

本轮按包清单提取 `Sifu/Content/Animations/System/Orders/Attacks/OrderAvoided.uasset/.uexp`，只写入 `logs/system-avoid/orderdb/`；使用本地有界 UE4 读取器按导出边界解析，不运行游戏。`Default__OrderAvoided_C` 的 `m_AvailabilityInfo` 解析为：`m_availabilityLayerData = /Game/DB/Inputs/Availability/LayerData/Guard/AllDefensiveOptions`，`m_iPriority = 10`；`m_ActivationCondition` 指向 `OrderServiceIsPlayerCondition_C`。故原攻击者上的 OrderAvoided 层数据是 `AllDefensiveOptions`，而不是 `Punishable_AvoidSuccess`。ActivationCondition 名称指向玩家条件，但目前只直接确认资源引用，尚未静态确认条件服务对所有订单实例的执行时机；因此不把它扩大解释成所有 AI 都恢复 Guard/Deflect。

同一 CDO 的 `m_OrderServices` 数组保持 opaque；导入表包含 `AvailabilityLayerOrderService`、`ForceFightingStateOrderService`、`OrderServiceIsPlayerCondition_C` 和 `DeflectedParryCancelAvailabilityOrderService_C`。这些导入只能作为后续回查入口，不足以断言每项服务的触发效果。订单 DB 的 CDO 解码结果与原始包元数据分别保存在 [system-avoid-orderdb-exports.json](../inventory/system-avoid-orderdb-exports.json) 和 [system-avoid-orderdb.json](../inventory/system-avoid-orderdb.json)；原包提取副本在 `logs/system-avoid/orderdb/Sifu/Content/Animations/System/Orders/Attacks/`。
