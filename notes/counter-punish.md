# 防反／闪避反击后的追击窗口：静态取证记录

## 范围与结论

目标问题是：玩家成功防御／闪避后，为什么敌人会稳定吃某些连招？静态检查可确认“部分防御会让 AI 攻击连招结束”，以及闪避相关事件会传入命中回调或写入 AI 记忆；当前还不能确认一个通用、固定时长的敌人脆弱窗口，也未证明该窗口由某个同名 `Parried` / `Avoided` 状态、抗性归零或防御许可关闭造成。玩家实测仍是需要由具体敌人、动作和输入时序验证的现象。

这里的“闪避反击”是玩家操作描述。`OrderAvoided`、`EFightingState::Avoided`、`EComboEndReason::PunishableAvoided` 是不同层次的内部标识，现有证据不足以把它们视为同一事件或状态。

## 已确认路径

1. **AI 防御逻辑可以结束正在进行的攻击连招。** `FAIAttackHandler::OnDefending` 直接调用 `EndCombo`，传入 `EComboEndReason::Defending`（6）。确认了这条回调路径；尚未证明所有挡住玩家攻击的情况都会调用它。见 [FAIAttackHandler__OnDefending-0x1890f40.asm.txt](../logs/counter-punish/FAIAttackHandler__OnDefending-0x1890f40.asm.txt)。

2. **结束连招会清理多个攻击侧状态。** `FAIAttackHandler::EndCombo` 结束 `UComboManager` 连招、abort 攻击准备、取消当前 `USCAiAction`（若有效）、移除异步 trace 请求、清理已验证条件记忆并重置若干弱引用；某些分支还调用防御结束回调。它没有在这段通用清理中直接设置一个固定“可被连招”时长。见 [FAIAttackHandler__EndCombo-0x1881e60.asm.txt](../logs/counter-punish/FAIAttackHandler__EndCombo-0x1881e60.asm.txt)。

3. **硬直可结束 AI 连招，但受条件限制。** `UAIFightingComponent::OnIsStunChanged` 读取所属角色 `UHitComponent::IsStun()`；只有变为 true 时才继续通知攻击 handler。`FAIAttackHandler::OnIsStunChanged` 还要求 Blackboard 上的 ComboEndReason 枚举值非零，才以 `IsStun`（10）结束连招。不能据此推导任何短暂受击或所有敌人都会结束连招。见 [UAIFightingComponent__OnIsStunChanged-0x18bc520.asm.txt](../logs/counter-punish/UAIFightingComponent__OnIsStunChanged-0x18bc520.asm.txt) 与 [FAIAttackHandler__OnIsStunChanged-0x1893b10.asm.txt](../logs/counter-punish/FAIAttackHandler__OnIsStunChanged-0x1893b10.asm.txt)。

4. **防反节点先提交 Deflect 请求，条件未满足时再尝试 None。** `UDefenseInfluenceNodeParryDeflect::Apply` 先过上下文影响节点的基础测试，再调用 `AFightingCharacter::HandleGuard`，参数中的 GuardType 为 Deflect（2）；特定条件继续通过后，会再调用一次 GuardType None（0）。它也会读取/设置 Order/Blackboard 相关字段。当前这段静态代码不足以完整解释两次调用的所有配置条件、敌人何时进入受击状态及持续时间。见 [UDefenseInfluenceNodeParryDeflect__Apply-0x1879d80.asm.txt](../logs/counter-punish/UDefenseInfluenceNodeParryDeflect__Apply-0x1879d80.asm.txt)。`EGuardType` 枚举来源为 `inventory/stun-state-type-layouts.json`。

5. **闪避节点的 Apply 会激活角色的待处理闪避窗口。** `UDefenseInfluenceNodeAvoid::Apply` 先要求父类上下文测试成功，随后对 `AFightingCharacter` 调用 `UDefenseComponent::ActivatePendingAvoidWindows`。这证明 AI／战斗上下文中存在窗口激活动作，但不等于它本身给目标敌人施加硬直或锁住防御。见 [UDefenseInfluenceNodeAvoid__Apply-0x1879c40.asm.txt](../logs/counter-punish/UDefenseInfluenceNodeAvoid__Apply-0x1879c40.asm.txt)。

6. **Avoided 订单会广播关联攻击信息，AI 侧也更新记忆。** `OrderAvoided::OnStart` 调用 `AFightingCharacter::OnAvoided`、确认 `OnConfirmedOnOrderAvoidSuccessful`，并结束该执行角色自己的玩家连招；`AFightingCharacter::OnAvoided` 再广播 `FOrderOverAttackInfo`。AI 回调 `UAIFightingComponent::OnOrderAvoidedStarted` 取出 `FNetOrderStructAvoided` 中的命中请求并广播，且在特定 order-type 下加难度变化。`OnTargetAvoidSuccess` 会把 AI memory type 数值 2 的一条记录按谓词更新。这个路径证明“成功闪避的信息会被传播/记忆”，没有证明目标敌人必定进入长硬直或普遍丧失格挡。见 [OrderAvoided__OnStart-0x1ade250.asm.txt](../logs/counter-punish/OrderAvoided__OnStart-0x1ade250.asm.txt)、[AFightingCharacter__OnAvoided-0x19c4010.asm.txt](../logs/counter-punish/AFightingCharacter__OnAvoided-0x19c4010.asm.txt)、[UAIFightingComponent__OnOrderAvoidedStarted-0x18bcfd0.asm.txt](../logs/counter-punish/UAIFightingComponent__OnOrderAvoidedStarted-0x18bcfd0.asm.txt)、[UAIFightingComponent__OnTargetAvoidSuccess-0x18bf640.asm.txt](../logs/counter-punish/UAIFightingComponent__OnTargetAvoidSuccess-0x18bf640.asm.txt) 与 [UAIFightingComponent__UpdateMemoryUnitForTargetDodgeOrAvoidSuccess-0x18cb0b0.asm.txt](../logs/counter-punish/UAIFightingComponent__UpdateMemoryUnitForTargetDodgeOrAvoidSuccess-0x18cb0b0.asm.txt)。

7. **击中处理存在 `PunishableAvoided` 数值，但 enum 身份未确认。** `UDefenseInfluenceNodeAvoid::OnNonDismissedHit` 在 DefenseHandler 的两个字段条件满足时，将一个输出字节写成 `0x0B`。它的参数类型是 `EHitDismissReason`。虽然 `EComboEndReason::PunishableAvoided` 也等于 11，但这不是同一枚举；不能凭数值相同断言这个回调调用 `EndCombo(PunishableAvoided)` 或者给敌人打开追击窗口。见 [UDefenseInfluenceNodeAvoid__OnNonDismissedHit-0x1893f50.asm.txt](../logs/counter-punish/UDefenseInfluenceNodeAvoid__OnNonDismissedHit-0x1893f50.asm.txt)。

8. **防御结束回调可重置/重排防御行为。** `UDefenseInfluenceNodeParryDeflect::OnTargetAttackEnded` 检查的是 AI 所属角色是否仍处于 `IsStun`；仍硬直就不走普通取消分支，未硬直时根据防御 handler 的活动记录检查决定是否 `CancelCurrentDefenseTactic`。因此不能把“玩家攻击结束”简单等同于“敌人硬直结束”。`FAIDefenseHandler::OnDefenseFinished` 与 `OnOrderFightingStateTimeLeftReachedZero` 展示了防御完成和 fighting-state 时间到期时的行动调度路径，但本次未把具体 `Parried/Avoided` profile 时长映射到 Grunt 资产。对应反汇编分别为 [UDefenseInfluenceNodeParryDeflect__OnTargetAttackEnded-0x1894b90.asm.txt](../logs/counter-punish/UDefenseInfluenceNodeParryDeflect__OnTargetAttackEnded-0x1894b90.asm.txt)、[FAIDefenseHandler__OnDefenseFinished-0x18baf10.asm.txt](../logs/counter-punish/FAIDefenseHandler__OnDefenseFinished-0x18baf10.asm.txt)、[FAIDefenseHandler__OnOrderFightingStateTimeLeftReachedZero-0x18bd1a0.asm.txt](../logs/counter-punish/FAIDefenseHandler__OnOrderFightingStateTimeLeftReachedZero-0x18bd1a0.asm.txt)。

## 枚举事实（不是行为证明）

本地匹配 PDB 的类型记录确认：

- `EComboEndReason`: `Defending=6`, `Parried=9`, `IsStun=10`, `PunishableAvoided=11`。
- `EFightingState`: `Counter_Hit=2`, `Avoided=6`, `Parried=8`。
- `EGuardType`: `None=0`, `Guard=1`, `Deflect=2`。

这些名字和值只说明构建包含这些枚举项，具体执行须由对应调用路径证明。`EHitDismissReason` 的成员列表并未出现在本次使用的 `stun-state-type-layouts.json` 中。

## 未解决的“稳定连招窗口”问题

当前代码路径没有给出一个所有 Grunt 通用的定时器或“防御许可关闭”的结论。未证实的关键点：

- 哪些玩家输入/招式会让敌人走 `EndCombo(Parried=9)` 或 `EndCombo(PunishableAvoided=11)`；本轮直接确认的是 `OnDefending -> EndCombo(Defending=6)`。
- 普通与进阶 Grunt 的防御图、受击 profile、`Counter_Hit`/`Parried`/`Avoided` 订单与状态配置，及 Normal0 下各自的长度。
- 玩家追击窗口的结束条件究竟是状态计时、动作退出、抗性恢复、重新允许 Guard/Deflect，还是多者组合。
- `OnOrderParryInstigatorStarted` 会在成功防御订单上构造并广播 HitRequest，但本轮未进一步解开该请求如何映射到目标的具体 profile/硬直时间。

下一步应将 Normal0 下普通/进阶 Grunt 使用的 order/profile/AI Defense asset 与对应 `EHitType`、状态剩余时间和可否防御字段相连；对照上述 code callbacks 找具体 EndCombo reason 的调用点。之后才适合用用户已观察到的固定连招作为可证伪的实战检查。

## 取证产物

反汇编由 `scripts/disassemble_research.py` 对本机构建匹配 PDB 的命名函数范围生成。清单与 SHA 信息见 `inventory/counter-punish-disassembly.json`；游戏二进制只读，未运行游戏、修改游戏文件或写入 LIAN 项目。反汇编不能证明运行期每一条路径实际发生，也不能代替 Normal0 实测。

## 补充：玩家 GuardAbility 的命中处理

`UGuardAbility::OnHitDefense` 是比订单名更靠近判定结果的回调：它从 ability owner 取得 `UDefenseComponent` / `UGuardDB`，调用 `BPE_OnDefense`，再从 `FHitRequest` 解析目标；若目标是 `AFightingCharacter`，路径会读取目标 GuardDB 与其当前攻击订单，按条件选择防御影响。已确认的分支会调用 `UHitComponent::GenerateImpact`（resistance override 实参为 null，由函数内部查询），随后在原攻击者组件上 `ApplyImpact`；紧随其后的 `AFightingCharacter::Hitted` 调用对象则是原防守者；之后会构造 `FNetOrderStructDefenseSuccess` 并调用 `PlayOrder`。这说明防反处理可能对原攻击者实际施加一个经其抗性库计算的命中结果，是解释追击窗口的直接候选因果链；但尚未解开该命中的具体 Impact 数值、状态时长或订单类型映射，所以不能断言这就是用户连招窗口的充分原因。见 [UGuardAbility__OnHitDefense-0x1a025f0.asm.txt](../logs/counter-punish/UGuardAbility__OnHitDefense-0x1a025f0.asm.txt)。

`UGuardAbility::ProcessForPlayer` 会依据 `FindDefenseOrder` 结果记录 GuardType，并在组件某个防御状态值为 2 时调用 `BPF_SetGuardType(Guard=1)`；它同时根据玩家输入与当前订单继续处理。此处证明 GuardAbility 维护防御许可/类型，但尚不能把该玩家侧字段变化等同于敌人不能格挡玩家后续攻击。见 [UGuardAbility__ProcessForPlayer-0x1a0cb00.asm.txt](../logs/counter-punish/UGuardAbility__ProcessForPlayer-0x1a0cb00.asm.txt)。`OrderParry::OnStart` 主要从 ParryAnimRequest 选择动画并进入 `OrderPlayAnim::OnStart`，本身没有出现敌人抗性或固定追击计时器；见 [OrderParry__OnStart-0x1b0cb60.asm.txt](../logs/counter-punish/OrderParry__OnStart-0x1b0cb60.asm.txt)。


## 2026-10-28 综合研究接续

最新证据和先前归属／默认值修正见 `notes/parry-system-chain.md`、`notes/avoid-system-chain.md`、`notes/recovery-system-chain.md`；用户阅读入口为知识库综合系统篇。未闭合处以新底稿的具体缺口为准。
