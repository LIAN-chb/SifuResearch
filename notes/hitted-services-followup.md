# Hitted 服务与 AI 防御许可补充取证

## 范围与结论

本文补记 Hitted 订单可用性服务、AI 防御查询，以及 Grunt 普通／进阶 Dizzy 状态附带的 `m_SuperAvailabilityLayer`。证据来自本机 Sifu 构建的提取资产、匹配 PDB 与 Shipping EXE 静态反汇编；未运行游戏。资产配置代表序列化值，不单独证明对应服务在某一运行时刻已激活。

| 结论 | 证据强度 | 限定 |
|---|---|---|
| Hitted 订单挂有多个 BasicGameplay 可用性层；其具体 action mask 不会移除 AI 防御查询用的 Avoid、Parry、Guard、Dodge 四个动作 | 配置、原生构造、mask 生成与 NPC wrapper 已接通 | 其他服务、movement 层、AI 条件仍可禁止防御 |
| AI 的 `UpdateDefenseNeed` 明确接受 Dizzy 与 Avoided 状态，但还受上下文防御、动作可用性、攻击准备等条件约束 | Shipping 代码反汇编 | 不是“进入白名单就一定防御” |
| Grunt Base/Adv 的 Dizzy reaction 都引用 `GenericNone`；`PushFightingState` 会把该层以 SET 推入 BasicGameplay 的 priority=1 `FightingState` 上下文。新上下文按优先级降序插到首项，故 NPC AI wrapper 查询时首先读到这层。它只允许 Look、MouseLook、DizzyReduction、ReplayMenu，四个 AI 防御动作均为 false | 配置、原生调用及原始数组解码 | 解释 Dizzy 中 AI 防御动作暂不可用；具体层的退出仍要结合 FightingState Pop／替换条件确认 |
| 因此，`Avoided` 状态结束后若仍处于 Grunt Dizzy，敌人不能通过 AI 防御查询用的 Avoid／Parry／Guard／Dodge 回防：priority=1 的 Dizzy SuperAvailabilityLayer 被插到 BasicGameplay 首项并以 SET 清除这些动作位。`PopFightingState` 调用捕获的回调并 `PopAvailabilityLayerContext(BasicGameplay)`，因此状态弹出时该层回收 | 配置、PushFightingState、context 插入顺序、NPC wrapper、AI defense gate 与 Pop 回调已接通 | 运行时确切剩余时间仍取决于状态实际 duration 与 Pop／替换时刻 |

## Hitted 订单服务与许可

`OrderHitted_C` 序列化配置的相关服务（索引为 `m_Services` 数组下标）：

| 下标 | 服务／层 | 配置 | 对动作可用性的含义 |
|---:|---|---|---|
| 5 | `HittedAvailabilityOrderService` → `GenericAll` | 启用；无 activation condition；非 frame-range 激活 | `GenericAll` 为反选 mask：允许除 Cancel、AttackLightAlt、AttackHeavyAlt、DodgeAttack、GuardInterruptNoParry 之外的动作。因此 Avoid、Parry、Guard、Dodge 不被该层移除。 |
| 9 | `HittedCancelAvailabilityOrderService` → `HittedCancel` | 启用；引用 `OrderServiceIsPlayerCondition`；operation=OR | `HittedCancel` 是正选 mask，包含 Dodge、Parry、FallInterrupt；对象引用显示条件门，但蓝图条件体未反编译，不能据引用宣称精确激活范围。 |
| 21 | `AvailabilityLayerOrderService` → `Pushed` | 启用；frame-range 模式；序列化边界为 open/open；operation=OR | `Pushed` 添加 PushbackCancel、Look、MouseLook。open/open 不构成有限时段证据。 |
| 28 | `HittedGetUpNoAttackAvailabilityOrderService` → `NoAttack` | 启用；operation=AND；priority=1 | `NoAttack` 只将 AttackLight、AttackHeavy 两项置为 false；不移除四种 AI 防御动作。 |

Availability mask 与上下文选择的原生语义：

- `UAvailabilityLayerData::GenerateAvailabilityLayer` RVA `0x199da70` 先以 `m_bInvertSelection` 初始化 208 个动作位，再将列表项改成相反值。故反选层的列表是禁用清单；普通正选层的列表是允许清单。
- `UAvailabilityLayerData` native `InternalConstructor` RVA `0x1c1fd20` 将 `m_eContext`（字段 +0x30）置 0。匹配 PDB 的 `InputContext::BasicGameplay=0`。这些资产未序列化覆写 context，因此落在 BasicGameplay。
- `UAvailabilityLayerOrderService` native `InternalConstructor` RVA `0x1c1fd90` 将 operation（+0x30）默认置 SET(0)，priority（+0x34）置 0；表内服务的 OR/AND/priority 是资产覆写。`CombineAvailabilityLayers` RVA `0x1996780` 中 SET=0、AND=1、OR=2。
- `FAvailabilityLayerOrderServiceInstance::OnStart` RVA `0x1b0b470` 对 owner 做 `AFightingCharacter` 类型检查，生成 layer mask，并把 layer、operation、context 与 service instance 传给 `PushAvailabilityLayer`。因此服务资源进入生命周期时可作用于玩家或 NPC `AFightingCharacter`；本处没有 Player-only 检查。
- `OnStop` RVA `0x1b0de10` 在 Pop 前还检查 `USCCoreTools::IsPawnMaster(owner)`，其谓词语义尚未闭合。因此不能仅凭该代码声称所有 NPC 上的层必定按同一条件移除。

## NPC 查询如何消费 BasicGameplay 层

AI 防御函数传入 `InputContext::Invalid=13`，但这不代表 NPC 查询绕过 Hitted 的 BasicGameplay 层：

1. `FAIDefenseHandler::UpdateDefenseNeed` RVA `0x18c9e50` 依次检查 `IsDefenseNeededInternal`、最高 FightingState、handler 状态、非空 contextual defense，以及动作可用性。
2. 它的状态白名单为 InFight(1)、Counter_Hit(2)、KnockedDown(3)、Dizzy(4)、Avoided(6)；Pushed(5)、StructureBroken(7)、Parried(8)、OutOfFight(0) 不在其中。
3. 对 Avoid(10)、Parry(9)、Guard(6)、Dodge(7) 调用 `AFightingCharacter::IsAvailable`，传入 context 13。`AFightingCharacter::IsAvailable` RVA `0x19c17d0` 先查 movement component，再转到 `ABaseCharacter::IsAvailable`。
4. `ABaseCharacter::IsAvailable` RVA `0x19a1af0`：若不是 `AFightingPlayerController` 角色，就直接读取对象 +0x758/+0x760 中 BasicGameplay context 的首个 priority layer 并查动作位；不会把传入的 13 交给 manager。玩家 controller 分支才走 contexts-stack 遍历。
5. 数组的索引是 InputContext，因此第 0 项是 BasicGameplay；其内部又有按 `EALPriority` 降序排列的 FightingState 等 layer context。`AvailabilityLayerManager::Reinit` RVA `0x19ab970` 重建每个 InputContext 的 priority=0 DefaultLayer context。随后 `PushAvailabilityLayerContext` RVA `0x19ab240` 在首个 existing priority<=新 priority 处插入；priority=0 的 DefaultLayer 遇到新 priority=1 时立即命中，随后被 `memmove` 后移，新 FightingState 写在 index0。NPC wrapper 读取 BasicGameplay 的首个 context，故实际查询首见 Dizzy 的 FightingState 层。
6. `UpdateDefenseNeed` 还会因 `FAIAttackHandler::IsPreparingAttack(false)` 为真而退出；只有其余门槛通过才继续构造 influence context、计算并应用请求。

代码中未发现 `UpdateDefenseNeed` 或 `IsAnyDefenseInputActionAvailable` 直接按 `OrderType::Hitted`、`m_bIsStunOrder` 或剩余 Hitted stun time 禁止 AI 防御。Hitted 对防御的影响可经 availability mask、最高 fighting state、当前 contextual defense、`IsDefenseNeededInternal` 等间接发生。

直接调用侧，`UAIDefenseBTTask::OnCharacterAvailabilityChanged` RVA `0x18e9620` 调 `FAIDefenseHandler::IsAnyDefenseInputActionAvailable`，再看 `IsDefenseNeeded` 并走任务结果分支；它自身也监视配置的 InputActions 可用性。这能证明 BT Task 消费这些许可变化，但静态反汇编不足以把每个返回整数映射成完整的动画／行为结果。

## Grunt Dizzy 的 SuperAvailabilityLayer

配置、解析与默认值：

| 字段 | Grunt Base | Grunt Advanced | 解释 |
|---|---|---|---|
| `m_DizzyReaction[0].m_bIsPersistent` | true | true | 状态行为在配置上为 persistent；不等于不受任何清除／替换条件影响。 |
| `m_DizzyReaction[0].m_SuperAvailabilityLayer` | `/Game/DB/Inputs/Availability/LayerData/GenericNone.GenericNone` | 同左 | `object-and-table-properties.csv` 中分别以 import `-9` 表示；资源路径一致。 |
| `m_DizzyReaction[0].m_Movement[0].m_fDuration` | 3.0s | 1.5s | 是普通 Dizzy 配置基础时长，不包含 Impact duration 修正及状态计时／覆盖规则。 |

调用链：

- 匹配 PDB 的 `FBaseFightingStateBehavior` 大小 16，`m_SuperAvailabilityLayer` 位于 +8；`FPropertyReaction` 继承该基类；`FDizzyReaction` 再继承 `FPropertyReaction`。`PushFightingState` 中 `GetFightingStateBehavior(state)` 返回此 reaction/behavior。
- `UDefenseComponent::PushFightingState` RVA `0x1966d90` 在 behavior 存在且 +8 指针非空时，调用 `ABaseCharacter::PushAvailabilityLayerContext`，传入 context=0（BasicGameplay）、priority=1、name=`FightingState`。接着对该层调用 `GenerateAvailabilityLayer`，再调 `PushAvailabilityLayerWithinLayerContext`。按函数签名逐参：`r8d=0` 是 `EALBinaryOperation::SET`；stack+0x20 是 BasicGameplay，+0x28 是刚返回的 context ID，+0x30 是名字，+0x38 的 2 才是 `EPredictionBehavior`。因此 Grunt Dizzy 这条引用不是闲置字段：状态推入路径会消费并将 mask SET 到新 FightingState layer context。
- 用既有解包的原始 `GenericNone.uexp` 数组解码（可复核记录见 `inventory/followup-hitted-services-genericnone.json`）：`m_inputActionArray` 是 4 项：`InputAction::Look`、`MouseLook`、`DizzyReduction`、`ReplayMenu`。默认 `m_bInvertSelection=false`，由 `UAvailabilityLayerData` 构造确认。因此生成 mask 在 BasicGameplay 只将这四项设为 true，再由 SET 写入该 FightingState context。
- `UpdateDefenseNeed` 对 Dizzy=4 仍在状态白名单里；`GenericNone` 的生成 mask 对 Avoid、Parry、Guard、Dodge、AttackLight、AttackHeavy 都是 false；`PushFightingState` 把它 SET 到新建的 BasicGameplay priority=1 `FightingState` 上下文，因此该层会拒绝这些动作。priority=1 context 插在 priority=0 DefaultLayer 前面；NPC wrapper 读取首个 context，所以 AI 防御 gate 确实消费这条 Dizzy 层。

因此，“成功闪避后反击把敌人打入 Dizzy，随后还能继续追击”已可由明确的许可链解释：Dizzy state whitelist 本身允许 defense handler 继续计算，但 Dizzy 的 `GenericNone` SuperAvailabilityLayer 通过 `PushFightingState` 以 SET 推入 BasicGameplay priority=1 `FightingState` context；该高优先级 context 被插到 priority=0 默认层之前，NPC `IsAvailable` 读首项时会见到 Avoid、Parry、Guard、Dodge 全为 unavailable。`UpdateDefenseNeed` 因而在防御动作许可检查处退出，敌人不能在这段 Dizzy 状态内通过这四种动作格挡／闪避／招架玩家后续攻击。此解释持续到该 FightingState layer 被 Pop；Dizzy 基础配置时长 Base=3.0s、Advanced=1.5s，最终运行时窗口仍受 duration 修正和状态移除逻辑影响。

## 证据文件与复查入口

| 证据 | 定位 |
|---|---|
| Hitted 订单服务列表和引用 | `inventory/followup-hitted-assets.json`，`OrderHitted_CDO.m_OrderServices.m_Services` |
| 本轮定向服务资产及哈希 | `inventory/followup-hitted-services-assets.json` |
| 订单服务 lifecycle 汇编 | `logs/followup-hitted-services/` 与 `logs/followup-hitted-services-2/` |
| GenericNone 资源 | `extracted/Sifu/Content/DB/Inputs/Availability/LayerData/GenericNone.uasset` 与 `.uexp`；数组解码/hash 在 `inventory/followup-hitted-services-genericnone.json`；原始标签背景在 `inventory/tagged-objects.json.gz` 及 `inventory/object-and-table-properties.csv` |
| GenericNone、Grunt 抗性配置与属性标签 | `inventory/object-and-table-properties.csv`，资产 `Grunt_Base_ResistanceDB.uasset`、`Grunt_Adv_ResistanceDB.uasset`、`GenericNone.uasset` |
| AI defense consumer 与 wrapper | `logs/followup-hitted-services-2/`、`logs/followup-hitted-services-3/`；重点 `FAIDefenseHandler::UpdateDefenseNeed 0x18c9e50`、`AFightingCharacter::IsAvailable 0x19c17d0`、`ABaseCharacter::IsAvailable 0x19a1af0` |
| state layer push与pop | `logs/stun-ai-state/UDefenseComponent__PushFightingState-0x1966d90.asm.txt`；上下文创建／排序与 NPC 查询 `logs/followup-hitted-services-4/`；状态层回收 `inventory/followup-state-availability-disassembly.json`、`inventory/followup-state-removal-disassembly.json` |
| enum、struct 与 offset | `inventory/action-resilience-type-layouts.json`、`inventory/followup-hitted-services-types.json` |
| Dizzy 时长与修正边界 | `notes/avoid-system-chain.md` 第 120–125 行附近 |

状态层回收：`PushFightingState` RVA `0x1966d90` 保存回调 thunk（`0x1951b20`）与 lambda（`0x194dd30`）；`PopFightingState` RVA `0x19662ad` 触发 lambda，lambda 检查捕获的 context ID 非 0 后调用 `PopAvailabilityLayerContext(BasicGameplay=0)`（`0x194de94–0x194ded4`）。证据清单：`inventory/followup-state-availability-disassembly.json`、`inventory/followup-state-removal-disassembly.json`。因此 Dizzy 的 state layer 在该 fighting state 弹出时回收。

## 尚缺证据

| 缺口 | 为什么重要 | 下一步 |
|---|---|---|
| `OrderServiceIsPlayerCondition` 蓝图函数体 | 无法精确判定 index9 服务是否对 NPC 跳过 | 定向解析该条件的蓝图图表/字节码，确认它是玩家条件还是其他 predicate |
| `IsPawnMaster` 对 NPC 的实际语义与生命周期 | 决定 `OnStop` 是否真的 Pop NPC 上的 order service 层 | 从匹配 PDB/调用者追一次 predicate；若仍是 native opaque，则保留运行时缺口 |
| 普通实战事件中各 layer 是否仍存活、谁先被 pop | 配置+调用链不含现场 layer stack | 只有在用户后续授权运行时观测后才能闭合；本轮不启动游戏 |
| Dizzy 期间触发 `UpdateDefenseNeed` 的上下文与行为树分支 | 白名单只证明“准入”，不证明会选择防御 | 继续核对 `IsDefenseNeededInternal`、contextual defense 和 BT 条件；按直接调用收窄 |
| Dizzy state 的 Push/Pop、同状态重击与计时器重置 | 基础 `m_fDuration` 不是实战最终剩余窗口 | 结合现有 `PushFightingState` 后续代码和状态更新/pop 路径补链，再决定是否需要动态观测 |

## 提取完整性与边界

本补充复用既有导出包与工具；`GenericNone.uexp` 数组长度为 36 字节，按声明的 4 字节元素数及四个 8 字节 FName 项解码，并与资产名映射一致。字段配置、native defaults、调用消费三层分别报告。Blueprint 条件实现与运行时激活情况没有从静态资产推断。所有结论限于匹配 PDB 的本机 Sifu 构建。
