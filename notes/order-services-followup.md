# OrderAvoided / OrderDeflected 服务与 Grunt 默认订单引用

> 范围：静态分析 Sifu 本机当前构建的 Grunt 基类默认 OrderDB、OrderAvoided／OrderDeflected 服务配置与执行入口。此记录补充主线；配置字段不等同于运行时最终效果。未启动游戏，也未改动游戏、存档或 LIAN。

## 结论摘要

| 结论 | 状态 | 证据边界 |
|---|---|---|
| `BP_Grunt_Base` 的 `OrderComponent.m_OrderDBs` 显式引用全局 `BP_OrderDB` 和 `Grunt_OrderDB`。全局库含 79 个订单引用，Grunt 库当前只有 `OrderFallOnSlope` 一项。 | 已解析配置 | 只证明 Grunt 基类直接配置；具体子类是否覆写需逐个核对。 |
| `OrderAvoided` 与 `OrderDeflected` 均配置 3 个服务：强制 `EFightingState::Avoided`、NPC 用的 GenericNone 可用性层、玩家用的招架取消层（DeflectedParryCancelAL）。 | 已解析配置 | 两个订单的服务数组相同；DeflectedParryCancel 的范围从含端点的 8.0 起。 |
| 强制状态服务启动时把状态、角色的 `UAttackPropertiesResistanceDB` 和 `-1.0f` 时长传给 `UDefenseComponent::PushFightingState`，停止时按返回 ID 弹出。 | 已接通调用 | `-1.0f` 是传参事实；其在被调用函数中的精确定义，以及状态如何影响每一类抗性，仍需追下去。 |
| GenericNone 服务的构造默认操作是 `SET`、层数据上下文是 0；其生成的掩码只将 Look、MouseLook、DizzyReduction、ReplayMenu 置为允许。非玩家 `ABaseCharacter::IsAvailable` 直接读第 0 层，因此 AI 的该查询路径会看见这层掩码。 | 原生执行链已接通，最终 AI 行为未实战验证 | 仍需接通具体 AI 选择节点是否对 Guard/Avoid 等调用 `IsAvailable`，以及订单服务实际何时启动。不能据此概括所有 AI 防御路径。 |
| 目前没有证据支持“OrderAvoided/Deflected 总会禁格挡”或“某个敌人必然选择闪避／反击”。 | 未确认 | 下文区分配置和最终行为。 |

## 1. Grunt 的默认 OrderDB

| 资源 | 字段／内容 | 解析结果 |
|---|---|---|
| `/Game/Blueprints/AI/Grunt/BP_Grunt_Base` | `OrderComponent.m_OrderDBs` | 按序引用 `/Game/Animations/System/Orders/BP_OrderDB` 与 `/Game/DB/AI/Archetypes/Grunt/Grunt_OrderDB`。 |
| `/Game/Animations/System/Orders/BP_OrderDB` CDO | `m_Orders` | 79 个订单类引用，其中包含 `/Game/Animations/System/Orders/Attacks/OrderAvoided` 与 `OrderDeflected`。 |
| `/Game/DB/AI/Archetypes/Grunt/Grunt_OrderDB` CDO | `m_Orders` | 1 个订单类引用：`/Game/Animations/System/Orders/States/FallOnSlope/OrderFallOnSlope`。 |

因此，OrderAvoided/Deflected 并不是 Grunt 专有订单，而是全局库可见、由 Grunt 基类组件加载的订单类型。仍需查具体子类的组件覆写/继承关系，才能把此结论推广到普通与进阶杂兵全部蓝图。

执行侧，`UOrderComponent::InternalInitialize`（RVA `0x1ad9900`）执行组件初始化；`UOrderComponent::GenerateOrderInstances`（`0x1ad32a0`）、`GetOrderDB`（`0x1ac72b0`）及 `OrderManager::GetOrderFromType`／`GetOrdersFromType`（`0x1afdc00`／`0x1afe550`）是后续生成与查找路径。当前已核配置引用和主要函数入口，尚未将每个 DB 订单引用到运行时实例构造的所有分支逐条复原。

## 2. OrderAvoided 与 OrderDeflected 的服务配置

两个订单 CDO 的 `m_OrderServices.m_Services` 均是完整解析的 3 元素 `FOrderServiceInfos` 数组（解码消费 2213 字节，数组边界校验通过）。服务按以下配置出现：

| 服务 | 两订单中的配置 | 条件与范围 | 直接可确认的含义 |
|---|---|---|---|
| `ForceFightingStateOrderService` | 启用；`m_bActivateFromFrameRange=true`；`m_bActivateWhenMissingFromAnim=false`；内联实例 `m_eFightingState=EFightingState::Avoided` | 无服务级 ActivationCondition；帧范围上下界均 Open | 在服务被激活时施加 Avoided 战斗状态；无显式数值帧界。 |
| `AvailabilityLayerOrderService` | 启用；`m_bActivateFromFrameRange=true`；缺少动画时不激活；内联实例 `m_availabilityLayerData=GenericNone`，`m_iPriority=10`；未序列化 operation 覆写 | `OrderServiceIsPlayerCondition`，`m_bInvertCondition=true`；上下界均 Open | 配置意图指向非玩家对象；native operation 默认 `SET`。 |
| `DeflectedParryCancelAvailabilityOrderService_C` | 启用；`m_bActivateFromFrameRange=true`；缺少动画时不激活；CDO 使用 `DeflectedParryCancelAL`、operation `OR`、priority 20 | `OrderServiceIsPlayerCondition`，不反转；下界 Inclusive 8.0，上界 Open | 配置意图指向玩家，从该服务范围下界开始加入招架取消动作许可。8.0 的单位/运行时映射尚未由本批证据确定。 |

两个订单本身另有顶层 `m_ActivationCondition=OrderServiceIsPlayerCondition_C` 和 `m_AvailabilityInfo=AllDefensiveOptions`（priority 10）；顶层反转字段没有序列化覆写，因而按当前构造/默认值记录为 false。此顶层条件与 `m_AvailabilityInfo` 的准确消费调用尚未接通，不能与上表逐服务的 condition 混为一谈。

### 条件函数的证据界限

`OrderServiceIsPlayerCondition` 资产包含 `BPE_CanActivate`，其父类是 `UOrderServiceActivationConditions`；CDO 本身没有字段。名称表包含 `BaseCharacter`、`IsPlayerControlled` 及对应调用返回值名，说明蓝图逻辑涉及玩家控制判断，但目前还没有解出足以证明返回值表达式和所有输入参数的字节码。因此，本记录把“条件 + 是否反转”的角色方向标成配置意图，未当作已证明的布尔真值。native `UOrderServiceActivationConditions::CanActivate`（RVA `0x1c74f00`）是转发到蓝图虚函数的入口。

## 3. GenericNone 如何进入 AI 可用性检查

### 配置掩码和组合操作

| 数据/执行点 | 证据 | 结果 |
|---|---|---|
| `GenericNone` 资产 | `m_inputActionArray`：Look、MouseLook、DizzyReduction、ReplayMenu；未覆写 context 与 invert | native 默认 context=0、invert=false。 |
| `UAvailabilityLayerData::GenerateAvailabilityLayer`（RVA `0x199da70`） | 先以 invert 值初始化动作掩码，再把数组列出的动作置为反值 | 对 GenericNone，只有列出的四类动作得到允许值；Guard、Parry、Avoid、Dodge 等未列动作得到 false。 |
| `UAvailabilityLayerOrderService` 构造函数（RVA `0x1c1fd90`） | operation 和 priority 默认清零 | `EALBinaryOperation` 的 0 为 SET；GenericNone inline service 未序列化覆写 operation，因此使用 SET，priority 则由资产设为 10。 |
| `FAvailabilityLayerOrderServiceInstance::OnStart`（RVA `0x1b0b470`） | 生成掩码，并把 operation、instance context、资产 context=0、名字等传给 `AFightingCharacter::PushAvailabilityLayer` | 服务启动时向战斗角色可用性系统推入 context 0 的层，并保存返回 ID。 |
| `AvailabilityLayerManager::PushAvailabilityLayer`（RVA `0x19aae70`） | 校验 context 小于 12 后存储/组合层 | context 0 是有效输入。 |
| `CombineAvailabilityLayers`（RVA `0x1996780`） | 操作 0 将左侧掩码复制成结果 | 在此层的组合语义下，SET 替换当前掩码。 |
| `FAvailabilityLayerOrderServiceInstance::OnStop`（RVA `0x1b0de10`） | 用保存的 ID 调用 `ABaseCharacter::PopAvailabilityLayer` | 服务停止时移除该层。 |

### AI 查询路径及边界

`ABaseCharacter::IsAvailable`（RVA `0x19a1af0`）有玩家控制器与非玩家路径。非玩家对象在 RVA `0x19a1ce9` 后直接读可用性第 0 层；该分支不把调用参数 context=13 直接转给 `AvailabilityLayerManager::IsAvailable`。所以不能把 manager 的 context 范围检查或传入的 13 推导成 NPC 绕过 GenericNone。反过来，静态证据也只证明该查询函数会读取第一层掩码，不证明每个 AI 选择分支都调用它。

外部交叉点：`FAIDefenseHandler::IsAnyDefenseInputActionAvailable`（RVA `0x18b8d80`）对 Avoid=10、Parry=9、Guard=6、Dodge=7 发起可用性查询，参数 context=13。判断最终结果时必须经过 NPC 的 `ABaseCharacter::IsAvailable` 包装路径；不能只单看 raw manager 查询。下一步需追从 `FAIDefenseHandler` 到对应 `ABaseCharacter::IsAvailable` 调用的具体分支，再确认 order 服务在这些查询前已 Push 且未 Pop。

`AllDefensiveOptions` 资产确实列出 Guard、Parry、PrepFocus、Avoid、Look、MouseLook、Dodge，但这是另一个 mask 资产；不能据其名称称为禁用防御。它可能参与订单顶层 `m_AvailabilityInfo` 路径，其调用点仍待查。

## 4. Avoided 状态的生命周期与抗性连接

| 阶段 | 函数 / RVA | 已证实的调用事实 |
|---|---|---|
| 创建服务实例 | `UForceFightingStateOrderService::CreateInstance`，`0x1af61a0` | 使用此 service class 创建对应运行时实例。 |
| 服务启动 | `FForceFightingStateOrderServiceInstance::OnStart`，`0x1b0bc90` | 校验 FightingCharacter；取 `UDefenseComponent`，再取该组件的 `UAttackPropertiesResistanceDB`；从内联配置读取 Avoided；调用 `PushFightingState`，传入 `-1.0f` 时长；保存返回 ID 到实例 `+0x88`。 |
| 服务停止 | `FForceFightingStateOrderServiceInstance::OnStop`，`0x1b0e3a0` | 取相同 DefenseComponent，以配置状态和保存 ID 调 `PopFightingState`。 |
| 服务调度 | `OrderBase::InitOrderServices`，`0x1b02c40`；`FOrderServiceInfos::InitializeInstance`，`0x1b03170`；`OrderBase::UpdateServices`，`0x1b1a1d0`；`OrderBase::StopServices`，`0x1b16bc0` | OrderBase 初始化并逐帧更新服务信息；订单停止时有统一 StopServices 入口。 |

这把“订单窗口内服务可推送 Avoided 状态”和“服务停止时撤销它”接成了静态生命周期链。PushFightingState 明确收到抗性数据库，因此状态系统与抗性配置存在调用连接；尚未解释 DB 如何修改招架、闪避反击、格挡或受击抗性，也未确认服务激活帧与玩家实测追击窗口完全重合。`-1.0f` 不能仅凭浮点常量被解释为无限持续；这里只能确认服务 OnStart 传入该值，服务 OnStop 负责 Pop。

## 5. DeflectedParryCancelAL：玩家侧配置

| 属性 | 解析值 | 限制 |
|---|---|---|
| 服务 condition | `OrderServiceIsPlayerCondition`，不反转 | 条件实际布尔语义待解。 |
| frame range | lower Inclusive 8.0，upper Open；`m_bActivateFromFrameRange=true` | 不能把 8.0 直接说成秒或动画帧。 |
| Layer 数据 | `ParryInterrupt`、`Parry` | 这是数组条目；经 `GenerateAvailabilityLayer` 生成的完整布尔 mask 以及执行时组合结果还需接通。 |
| 操作 / 优先级 | OR / 20 | CDO 明确序列化。 |

该配置提供了“Deflected 订单可对玩家侧加入招架及招架打断动作许可”的静态机制线索；但条件函数的确切返回值、8.0 的单位、服务生命周期与玩家招架窗口的运行时对应都尚未验证。不能只凭资产名断言追击一定稳定命中。

## 6. 因果链视图

```text
Grunt Base OrderComponent.m_OrderDBs
  ├─ Global BP_OrderDB ── OrderAvoided / OrderDeflected
  └─ Grunt_OrderDB ───── OrderFallOnSlope

OrderAvoided / OrderDeflected 生效
  ├─ ForceFightingState service ── PushFightingState(Avoided, ResistanceDB, -1)
  │                                  └─ service stop → PopFightingState(id)
  ├─ 非玩家条件(反转配置) → AvailabilityLayer service(GenericNone, SET, context 0, priority 10)
  │                                  └─ NPC IsAvailable → 读取第 0 层
  └─ 玩家条件(不反转) + lower bound 8 → DeflectedParryCancelAL(OR, priority 20)
                                       └─ {ParryInterrupt, Parry}
```

图中箭头表示资产引用或 native 直接调用；条件真假、服务实际启动时刻、抗性变化以及具体 AI 决策尚有待证边。

## 7. 证据与可复核入口

| 证据对象 | 路径 / 定位 | 用途 |
|---|---|---|
| 定向包解析结果 | `inventory/followup-order-services-packages.json` | 10 个指定包的资源路径、sha256、imports/exports、属性及 3 元素 service 数组解码结果；每数组 `arrayDecodeValid=true` 且完整消费 2213 bytes。 |
| 原生函数清单 | `inventory/followup-order-services-disassembly.json` | 匹配 EXE/PDB 的 RVA、函数长度、输出路径和逐文件 sha256；当前 EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`。 |
| OrderAvoided 生命周期 | `logs/followup-order-services/OrderAvoided__OnStart-0x1ade250.asm.txt`、`OrderAvoided__OnStop-0x1ae1340.asm.txt`、`OrderAvoided__OnUpdate-0x1ae3a30.asm.txt` | 避开行为的订单层处理与通知；需与 OrderBase service 调度区别。 |
| OrderDeflected 生命周期 | `logs/followup-order-services/OrderDeflected__OnStart-0x1ade500.asm.txt`、`OrderDeflected__OnStop-0x1ae14e0.asm.txt`、`OrderDeflected__OnUpdate-0x1ae3ba0.asm.txt` | 订单自身处理入口。 |
| 服务执行 | `FForceFightingStateOrderServiceInstance__OnStart-0x1b0bc90.asm.txt`、`...OnStop-0x1b0e3a0.asm.txt`、`FAvailabilityLayerOrderServiceInstance__OnStart-0x1b0b470.asm.txt`、`...OnStop-0x1b0de10.asm.txt` | Push/Pop 状态和可用性层。 |
| 层语义 | `UAvailabilityLayerData__GenerateAvailabilityLayer-0x199da70.asm.txt`、`CombineAvailabilityLayers-0x1996780.asm.txt`、`AvailabilityLayerManager__PushAvailabilityLayer-0x19aae70.asm.txt` | mask 生成、组合、推入。 |
| NPC许可查询 | `ABaseCharacter__IsAvailable-0x19a1af0.asm.txt` | 非玩家对象直接读取第 0 层的分支。 |
| OrderBase 调度 | `OrderBase__InitOrderServices-0x1b02c40.asm.txt`、`OrderBase__UpdateServices-0x1b1a1d0.asm.txt`、`OrderBase__StopServices-0x1b16bc0.asm.txt`、`OrderBase__Stop-0x1b168e0.asm.txt` | 服务初始化、更新和停止入口。 |

所有日志均限定于 `logs/followup-order-services/`。包解析只覆盖上述定向资源；native dumpbin 反汇编依赖当前匹配 PDB 的函数范围。反汇编不是运行时验证。

## 8. 未解问题与下一步取证

| 优先级 | 缺口 | 下一步最小取证 |
|---|---|---|
| 阻塞主线 | `OrderServiceIsPlayerCondition::BPE_CanActivate` 的确切返回表达式和服务对象/owner 参数 | 定向解其 Kismet bytecode，确认条件返回和 `OrderBase::UpdateServices` 传入的角色对象。 |
| 阻塞主线 | ForceFightingState 推入 Avoided 后，`UAttackPropertiesResistanceDB` 如何改变招架、闪避反击、格挡与受击反馈 | 追 `UDefenseComponent::PushFightingState`、`PopFightingState` 与 resistance DB 查值函数；仅报告实际读取/覆盖字段。 |
| 直接关联 | 玩家 deflected 层的 8.0 单位和真正生效区间 | 追 OrderServiceFrameRange 的时间基准、动画通知/帧进度映射及 service 起停代码。 |
| 直接关联 | NPC GenericNone 是否在具体 AI 防御选择中阻止 Guard/Avoid 等候选 | 追 `FAIDefenseHandler::IsAnyDefenseInputActionAvailable`（RVA `0x18b8d80`）到 `ABaseCharacter::IsAvailable` 的实际调用，并核对订单服务存续时机。 |
| 后续 | 顶层 `m_ActivationCondition` 和 `m_AvailabilityInfo=AllDefensiveOptions` 的消费位置 | 追 OrderBase 订单激活/可用性信息路径，区分订单许可与 per-service condition。 |
| 后续 | Grunt 普通/进阶具体子类是否继承或覆写 OrderDB | 对相关蓝图的父类链、组件默认值逐一比对；不要从 Base 直接外推。 |

## 解包与解析批次

- 当前本机 Sifu 包，精确资源列表见 `inventory/followup-order-services-packages.json`；包及可执行文件哈希作为本批构建锚点记录。
- `scripts/followup_order_services_decode.py` 对定向包解析字段及内联 `m_OrderServices.m_Services`，含结构数组消费长度检查；仅复用现成有界读取器，不全量导出资产。
- `scripts/disassemble_research.py --group followup-order-services` 按 PDB 唯一命名函数分组输出。原生函数当前均已解析到 PDB 项并生成反汇编，清单 `missing=[]`。
- 证据层级：订单/服务“已提取、已解析”；状态与许可层“已接通 native 调用链”；运行时激活、敌人实际选择、玩家可追击结果“未实战验证”。

## 集成复核补充

ForceFightingState传入duration=-1的无限位已由PushFightingState `0x196716e` 与Tick `0x196a2c7` 接通；其状态生命周期经OnStop／Pop回收，不使用Dizzy3／1.5秒。NPC动作许可实际包装查询及AI gate见综合实现E20。服务自身IsPlayer条件仍未解，不能将Dizzy状态层的确定结论直接移植为所有Avoided服务必定激活。
