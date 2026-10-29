# 普通受击结束与敌人防御重新评估：静态案例底稿

- 批次：`20261028-case-defense-gate`
- 范围：本机 Epic《师父》普通受击期间，AI 敌人何时重新评估防御。仅静态分析，未运行游戏。
- 构建：EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；PDB `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` / age 1
- 结构化记录：`inventory/case-defense-20261028.json`
- 生成新反汇编：`scripts/disassemble_research.py --group case-defense-init-20261028 ...` 与 `--group case-defense-init2-20261028 ...`；PDB/EXE 一致。主要函数直接复用原哈希清单，不重复生成旧共享manifest。

## 直接结论

有一条静态事件链能解释“普通受击硬直结束后，AI何时重新跑防御查询”：

**敌人 Hitted 订单倒计时 → 满足恢复层条件 → 给敌人加入 `AIHittedRecovery` 动作层 → 广播敌人自己的 `UHitComponent::OnIsStunChanged` → 已在 `UAIFightingComponent::InternalBeginPlay` 绑定的回调查询敌人当前是否仍有“受击中”订单 → 结果为否时，在目标攻击组件字段及防御 handler 条件成立下调用 `FAIDefenseHandler::UpdateDefenseNeed`。**

这里是敌人的防御重新评估入口，不能与玩家受击混为一谈。

## 逐步证据

| 步骤 | 执行对象与判断 | 代码／配置证据 | 结论及边界 |
|---|---|---|---|
| 1 | `OrderHitted::OnUpdate` 递减敌人自身 `m_fHitTimeLeft`；到零后检查是否能开放恢复动作层 | RVA `0x1ae44d0`，`+0x51C`倒计时、`0x1ae46e4–0x1ae4709` | “敌人硬直”这里指订单内部剩余计时，不是动画剩余时长 |
| 2 | 敌人受击数据必须允许恢复层路径：剩余动画时间>0、`m_bInterruptAnimationOnEnd(+0x73B)=false`、非致命命中、`m_bInterruptible(+0x73A)=true` | 同函数 `0x1ae472c–0x1ae4751`；偏移由 `FNetOrderStructHitted.m_HittedAnimContainer` 对应类型布局确认 | 这是添加层的实际代码条件；原生含义优先用两个布尔字段名表达，其他偏移判断不补造中文含义 |
| 3 | 条件满足后敌人取得 `AIHittedRecovery` 可用性层；订单保存返回句柄，再广播自己的 `OnIsStunChanged` | 同函数 `0x1ae4751–0x1ae47b1`；`UHitComponent +0x108` 即 `OnIsStunChanged` | 许可层从此分支被加入；配置本身不能保证其它许可／移动条件通过，也不保证 AI 选中防御 |
| 4 | `UHitComponent::IsStun` 在敌人自己的活动订单中枚举并调用 `IsStunOrder` | RVA `0x1a64340`；读取 AI owner 的 `UHitComponent` 见 `UAIFightingComponent::OnIsStunChanged` `0x18bc520` | 不是查询玩家是否硬直，也不是只读一个布尔值 |
| 5 | Hitted 的“仍受击中”谓词：`OrderBase::m_eOrderState(+0xCA)==Starting(1)` **或** `OrderHitted::m_fHitTimeLeft(+0x51C)>0` | `OrderHitted::IsStunOrder` RVA `0x19fdb50`；`inventory/followup-hitted-type-layouts.json` 中 OrderBase 字段和匹配枚举 | `+0xCA` 是订单状态，不是名为 `m_bIsStunOrder` 的旗标；状态刚 Starting 或剩余计时大于0时谓词为真 |
| 6 | 敌人的 `OnIsStunChanged` 回调在自身谓词为真时不走本回调里的防御重查；谓词为假时，若追踪目标及其 `AttackComponent` 有效，且该**目标攻击组件** `+0xBF1` 字段不大于 1，才调用 `UpdateDefenseNeed` | RVA `0x18bc520`，`0x18bc563–0x18bc5db` | `+0xBF1` 的类型／语义尚未映射；它不是已确认的敌人 defense-handler 状态。该回调链明确受敌人自身 `IsStun()` 控制，但不是唯一已知重评估入口 |
| 7 | `CanApplyDefenseRequest` 检查请求关联对象；两次从其虚表 `+0x298` 取一个字节值，再把值传入敌人角色虚表 `+0x988` 的可用性判断（context 参数为 13） | RVA `0x18ab9c0`，`0x18ab9f7–0x18aba77` | 没有 Hitted 订单ID、`m_fHitTimeLeft` 或 `IsStun` 读取。请求动作的准确语义仍未映射；偏移是 `+0x298`，不是 `+0x2A0` |

### 另一条防御需求重评估入口：目标订单状态改变

`UAIFightingComponent::OnTargetOrderStateChangedInternal`（RVA `0x18bfb30`）也能调用敌人的 `FAIDefenseHandler::UpdateDefenseNeed`。此函数没有读取敌人自己的 `UHitComponent::IsStun()`，也没有读取 Hitted 剩余计时；因此普通 Hitted 期间不能仅凭 `OnIsStunChanged` 路径推断“绝无更早重评估”。该入口的直接条件是：

| 条件 | 代码所见 | 结论边界 |
|---|---|---|
| 订单类型 | 对参数订单调用 vtable `+0x28`，仅返回 `0` 或 `0x28` 时进入后续处理 | PDB 虚函数布局可对应 `OrderBase::GetBaseType`；这两个返回值的具体游戏语义本批不命名 |
| 当前动作可取消 | 查询与 AI 动作标签关联的当前动作；存在时检查 `IsCurrentAttackActionCancellable`／`IsCurrentActionCancellable`，失败则退出 | 这是动作处理条件，不能解释成 Hitted 许可层 |
| 更新防御需求 | 参数订单 `OrderBase::m_eOrderState(+0xCA)==2`，且防御 handler `+0x100` 字节等于 4；随后重置目标攻击信息并调用 `UpdateDefenseNeed` | `+0x100` 的枚举含义以及订单 state=2 的语义未在本批映射；不据此推断结果会执行防御 |

这条函数路径说明：**敌人自身受击状态的变化回调不是所有防御需求更新的总闸门。** 目标订单状态事件可以在满足独立条件时触发更新；静态函数中没见敌人 `IsStun()` 门，是否在实际 Hitted 期间触发仍缺运行时观测。不要把“调用了 `UpdateDefenseNeed`”等同于“敌人已格挡”。

## 为什么“硬直”不只是动画

有两件事同时发生，但代码把它们分开处理：

| 对象 | 负责什么 | 时序证据 |
|---|---|---|
| `OrderPlayAnim` 动画计时 | 维护受击动画的播放／剩余时长 | `OrderHitted::OnUpdate` 先调用父类 `OrderPlayAnim::OnUpdate`，之后再扣自己的 `m_fHitTimeLeft` |
| Hitted 内部受控计时 | 决定是否可进入恢复许可分支，并参与 `IsStunOrder` 谓词 | timer可先到零；若动画仍有剩余时间且其它条件满足，会先加入恢复层并广播通知 |
| AI防御重新评估 | 事件回调检查敌人自身 `IsStun()`，然后可能重查玩家下一次攻击 | 在条件通过后调用 `UpdateDefenseNeed`，不是从动画结束通知直接推出 |

因此能确认：**受击硬直计时结束可以成为敌人重新评估防御的触发点，即使受击动画还有剩余时间。** 这条逻辑比“受击单被取消所以动画切换”更接近连续压制问题。

## 防御许可不等于“直到计时结束才有防御能力”

`HittedAvailabilityOrderService` 的 `GenericAll` 掩码允许 Guard、Parry、Dodge、Avoid 等动作。恢复层添加是上面的明确事件，但 `OnTargetOrderStateChangedInternal` 有独立的 `UpdateDefenseNeed` 调用条件，且静态函数没有读敌人 `IsStun()`。所以本批只能确认：`OnIsStunChanged` 路由在敌人 `IsStun()` 为真时跳过该次防御重查；变假后可按目标攻击组件字段条件重查。不能据此断言所有其它事件都被挡住，也不能证明此前的防御请求必被撤销或动画播放已停止。

另一个容易混淆的代码路径是 AI 自己的连段：`UAIFightingComponent::OnIsStunChanged(true)` 通知 `FAIAttackHandler`；若其配置的 Blackboard ComboEndReason 非无效才以 IsStun(10) 结束该敌人的连段。它解释“敌人被打断时可能停止自己的进攻连段”，不是“敌人因此无法对玩家防御”。

### 防御请求校验与 Guard 节点执行：不是同一条门槛

这部分只接一层：防御候选的可用性校验进入 `ABaseCharacter::IsAvailable` 后，和 Guard 节点的即时执行分别检查什么。

| 阶段 | 调用证据 | 可确认的差异 | 未知 |
|---|---|---|---|
| `UpdateDefenseNeed` 生成／筛选候选 | RVA `0x18c9e50` 的 Guard/Parry/Avoid/Dodge 查询在 `0x18c9fb2–0x18ca018`；传入 `r8=0`、context=13 | `ABaseCharacter::IsAvailable` 的 r8=false 分支选择对象缓存偏移 `+0x38/+0x40` | 两字段的确切含义未解析 |
| `CanApplyDefenseRequest` 执行前复核 | RVA `0x18ab9c0`，`0x18aba6c–0x18aba77`；请求对象虚表 `+0x298` 给出动作字节后传入 `IsAvailable`，r8=true、context=13 | `ABaseCharacter::IsAvailable` 的 NPC 分支选择 `+0x18/+0x20`，与 r8=false 的 `+0x38/+0x40` 不同 | 函数开头虽然在 r8=true 时把同步 tick 加上 `SCGameSettings+0x710`，但 NPC 分支未继续使用这个 tick；不能把它说成 NPC 的执行等待时间 |
| Guard 节点的 Apply | `UDefenseInfluenceNodeGuard::Apply` RVA `0x1879cf0`：先调用基类 `Apply`；基类成功后才调用 `AFightingCharacter::HandleGuard` | 本次已读函数体没有显式敌人 `IsStun()`／`IsAvailable()`／时间延迟检查；`HandleGuard` 中能看到 `IsOrderRunning` 查询、GuardBroken 查询及角色组件有效性分支 | 这不证明底层订单启动必成功，也不证明其它调用路径没有硬直门；`IsOrderRunning` 的具体订单限制需另查 |

`ApplyDefenseRequest` 中请求关联对象的虚表 `+0x2A0` 返回字节，稍后被写入 Blackboard 的 enum key（`0x18a7f30–0x18a7f40`）；`ComputeDefenseRequest` 也用同槽返回值判断候选是否继续（`0x18ac597` 后测试返回值，非零才进入 `OnDefending`）。构建内 `.rdata` 的 Guard vtable 表项与 PDB 符号对齐后，`+0x298` 是 `GetInputAction`，相邻的 `+0x2A0` 指向 `GetAssociatedTactic`（Guard 与 Avoid 的实现均映射到该名称；本构建两者存在函数折叠）。返回字节写入 Blackboard enum，也符合 tactic 返回值用途。**因此 +0x2A0 是读取防御策略标签的方法，不是 Guard/Avoid 的 Apply 执行调用。**

由此能说的是：候选生成和执行前复核使用不同 `IsAvailable` 缓存分支。函数在 r8=true 时会计算配置延迟，但 NPC 分支没有消费该 tick；不能据此称 NPC 执行前存在这项等待。两套缓存哪个代表“预测/当前”仍未知。单看 Guard `Apply` 与 `HandleGuard` 未见显式自身 `IsStun()` 检查。

## 静态案例与最终范围

| 玩家／敌人场景 | 从证据能判断什么 | 尚不能判断什么 |
|---|---|---|
| 玩家打中普通 Grunt，敌人产生普通 Hitted，timer仍>0 | 敌人 `IsStunOrder` 可以仍为真；timer到期通知到达时，若敌人 `IsStunOrder` 仍为真，这一条回调不会通过“false→重查防御”分支 | 当前是否有其他事件仍会发起 defense update；现有排队动作是否执行 |
| 玩家继续攻击，造成旧 Hitted 被新 Hitted 替换 | 旧订单取消并回收其恢复层／服务；新订单有自己的timer。每次命中可能推迟该状态变化事件，取决于新计时 | 具体命中序列每一击的伤害、时长、实例覆盖和实际首次格挡帧 |
| 玩家只打一次并等待 | 订单timer归零且恢复gate通过时会push AIHittedRecovery并广播；之后可条件性重新评估 | AI是否预测到玩家下一击、选了哪个防御候选并真正执行 |

此表是**原生状态／调用路径的静态案例**，不是已实战观察的“第几拳能连”。要变成确切可连/连不上例子，还要与用户指定的实际玩家动作／命中段时序对齐，并在获准运行时观察。

## 剩余缺口与下个最小取证

| 缺口 | 当前状态 | 下一步 |
|---|---|---|
| `UHitComponent+0x108` 的 `OnIsStunChanged` 与 AI 回调订阅关系 | 已由 `UAIFightingComponent::InternalBeginPlay` 确认绑定到同一个 AI 组件的 `OnIsStunChanged` | 无需再查订阅；直接证据为 `0x18b8177–0x18b81b2` |
| `CanApplyDefenseRequest` 请求动作的准确含义 | 请求对象虚表 `+0x298` 返回的字节传入角色 `IsAvailable` 虚调用；尚无足够类型证据给它命名 | 继续核对请求结构、虚表映射和角色可用性参数 |
| 目标订单事件是否在敌人仍 Hitted 时实际触发 | `OnTargetOrderStateChangedInternal` 没有显式检查敌人 `IsStun()`／Hitted timer，但静态证据不证明该事件会在该时段发生 | 追踪订单事件来源和真实调用时机；必要时提供固定实战观测方案，不自行运行 |
| 尚有无其它路径更早更新防御 | 已确认 `OnIsStunChanged` 与 `OnTargetOrderStateChangedInternal` 两条路；其它监听／Tick/BT调用者未做穷尽 | 按 `UpdateDefenseNeed` 调用点继续分类，不把已知两条路视为完整集合 |
| 特定Grunt及招式例 | 普通/进阶Grunt共享部分基础配置，但具体实例、命中段和动画速率未在本批验证 | 与玩家输入追踪agent的新素材合并，建立首例并只引用同一构建的实例资产 |
| `m_bTimeSinceLastHitPrevails` 与连续多击timer | 使用者依旧未定位 | 不作为本批gate成立条件；需要后续单独查真实读者 |

## 证据清单

本批既有函数的原始反汇编和哈希见 `inventory/case-defense-20261028.json`，核心取证位置：

- `logs/stun-ai-defense/FAIDefenseHandler__IsDefenseNeededInternal-0x18b8fc0.asm.txt`
- `logs/stun-ai-defense/FAIDefenseHandler__UpdateDefenseNeed-0x18c9e50.asm.txt`
- `logs/stun-ai-defense/FAIDefenseHandler__CanApplyDefenseRequest-0x18ab9c0.asm.txt`
- `logs/callback-UHitComponent-IsStun.asm.txt`
- `logs/stun-ai-state/OrderHitted__IsStunOrder-0x19fdb50.asm.txt`
- `logs/system-recovery/OrderHitted__OnUpdate-0x1ae44d0.asm.txt`
- `logs/counter-punish/UAIFightingComponent__OnIsStunChanged-0x18bc520.asm.txt`
- `logs/counter-punish/FAIAttackHandler__OnIsStunChanged-0x1893b10.asm.txt`
- `logs/case-defense-events/UAIFightingComponent__InternalBeginPlay-0x18b7e30.asm.txt`：敌人 `AFightingCharacter+0x1328` 的 HitComponent `+0x108` 绑定到本敌人的 `UAIFightingComponent::OnIsStunChanged`（`0x18b8177–0x18b81b2`）
- `logs/case-defense-events/UAIFightingComponent__OnTargetOrderStateChangedInternal-0x18bfb30.asm.txt`：独立目标订单事件重评估路径（`0x18bfbb8–0x18bfcd1`）
- `logs/followup-order-services/ABaseCharacter__IsAvailable-0x19a1af0.asm.txt`：r8 分支及 NPC 缓存读取偏移
- `logs/stun-ai-defense/UDefenseInfluenceNodeGuard__Apply-0x1879cf0.asm.txt` 与 `logs/system-parry/AFightingCharacter__HandleGuard-0x19bfa70.asm.txt`：Guard Apply 的一个近邻执行路径

初始化扫描新产物分别在 `inventory/case-defense-init-20261028-disassembly.json` 和 `inventory/case-defense-init2-20261028-disassembly.json`，原始反汇编分别位于 `logs/case-defense-init-20261028/` 与 `logs/case-defense-init2-20261028/`。所有结论绑定上述 EXE/PDB，未运行游戏。
