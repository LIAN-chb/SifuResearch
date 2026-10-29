# Hitted 新旧订单替换与回收：后续静态取证

更新：2026-10-28。仅本机匹配 Shipping EXE/PDB；不运行游戏。与 `notes/hitted-stun-timer-dataflow.md` 的关系：此前已接通计时生成，本篇补齐正常无前置 Hitted 请求的取消目标与生命周期。

## 结论及适用条件

**普通受击不是不断给同一个 Hitted 对象加时间。** 已确认的正常请求先构造新订单；当 `m_uiAfterOrder=0` 且未绕过取消逻辑时，Hitted 的 `BoundToAnimState` 类别会收集当前 Running/Pending 中仍处于 Starting/Processing 的同类别订单 ID，安排取消，再排入新订单。旧 Hitted 属于这个取消集合。取消被处理后，运行中的旧 Hitted 经 `OnCancel → OnStop` 回收其恢复许可层，订单服务也有统一停止路径。

这是有条件的执行链，不扩展为“任何命中都会取消全部订单”：韧性绕过正常 Hitted、其他特殊受击类型、有前置订单的序列、预测/网络、已停止/已取消及尚未实际执行的请求都须分别看待。

## 精确因果链

| 环节 | 静态证据 | 能直接下的结论 |
|---|---|---|
| 本次普通受击构造播放参数 | `UHitComponent::ApplyImpact` RVA `0x1a46d90`，`0x1a47eff–0x1a47f5e`：栈上 `FPlayOrderInfos` 的 afterOrder=0、delay=0，随后 PlayOrderWithType | 当前分支是无前置、零延迟的新请求，不能用“等待旧 Hitted 自然结束”补齐它。 |
| 区分订单类别 | `OrderBase` PDB 的 GetSubType 引入虚函数槽 `+0x70`；`OrderHitted::GetSubType` RVA `0x8a8bd0` 返回2；匹配枚举 `EOrderSubType::BoundToAnimState=2` | Hitted 是绑定动画状态的类别。**GetBaseType 是另一个槽 +0x28**，不能把 +0x70 混称基础类型。 |
| 进入取消收集分支 | `AFightingCharacter::PlayOrder` RVA `0x19c7aa0`，`0x19c801a` 对下层该参数传0；`UOrderComponent::PlayOrder` RVA `0x1ae4f20`，`0x1ae4fe2–0x1ae5144` 先检查跳过分支，再检查 GetSubType==2；afterOrder为0时调用 `GatherActionTypeOrderIDs` | 正常角色播放分支不会因该参数跳过此取消逻辑；有前置订单时走另一个序列收集分支。 |
| 实际收集谓词 | `OrderManager::GatherActionTypeOrderIDs` RVA `0x1afa580` 使用访问模式2；其 lambda RVA `0x1af24a0` 检查 GetSubType==2 且 state为1/2，才保存ID。PDB：访问模式2=RunningOrPending，state1=Starting、2=Processing | 目标不仅限同一个Hitted类型，还包括符合谓词的动画绑定动作；旧活动Hitted必符合类别与状态条件。已Stopped/Cancelled不在该谓词集合。 |
| 避免重复取消与安排取消 | `UOrderComponent::PlayOrder` `0x1ae50d0–0x1ae5177` 剔除已pending cancel的ID；`0x1ae52b6/0x1ae52cb` 将余下列表交给 `OrderManager::CancelOrderByID`，之后才 `0x1ae556b` Manager.PlayOrder | 取消旧单和排入新单是两类命令；“请求已发出”不等同于已经在同一帧执行回收。 |
| 取消命令真正执行 | `OrderManager::CancelOrder` float重载 RVA `0x1af2cc0` 构造取消命令；`ProcessDelayedCommands` RVA `0x1b12660` 处理期限/依赖；`LaunchDelayedOrder` RVA `0x1b040f0` 的取消分支最终在 `0x1b0440c` 调 bool重载 | 旧单按延迟命令流程执行取消，不是直接把旧内存的HitTimeLeft写成新值。 |
| 改变旧订单状态 | bool重载 `OrderManager::CancelOrder` RVA `0x1af2a60`，`0x1af2aa7–0x1af2aad`：若旧状态<3，设为Cancelled4；标记相关pending命令已取消；另有依赖取消 | 活动旧Hitted进入取消生命周期；尚未启动的订单有OnCancelledBeforeStart分支，不能与运行后停止完全等同。 |
| 运行旧单回收 | `OrderBase::Process` RVA `0x1b11d40` 在Cancelled分支 `0x1b121f6` 调虚槽+0x1b0=OnCancel；`OrderBase::OnCancel` RVA `0x1a006c0` 跳到虚槽+0x1a8=OnStop；紧随 `0x1b12205` StopServices | OnCancel可复用具体订单的OnStop；OrderHitted无自身OnCancel覆写的匹配方法证据，正常继承路径调用其OnStop；服务停止不是仅靠动画结束。 |
| 受击恢复许可回收 | 已有 `OrderHitted::OnStop` RVA `0x1ae1a40`，`0x1ae1c89–0x1ae1cba` 对有效句柄Pop HitRecoveryAvailability并置无效 | 旧订单曾开放的恢复层随该生命周期回收，新订单自己再按其计时/条件建立恢复层。此事实不保证AI立即选防御。 |

## 对连续命中解释的改变

| 问题 | 已可解释 | 尚未由此证明 |
|---|---|---|
| 新的一击会不会影响已有普通硬直 | 先计算本次结果，特定最长策略/AlreadyGuardBroken读取旧剩余量取max；之后正常请求取消旧动画绑定订单并创建新的Hitted计时 | 不是一律累加时间，也不是所有情况一律取最长。 |
| Grunt最长硬直策略false意味着什么 | 该普通策略分支不会自动保护旧长硬直；新订单仍按本次结束时刻、动画覆盖和冻结补偿计算 | 不能只凭false就说最终时长一定变短／覆盖成配置帧数。 |
| 连打为何不保证无限续控 | 新普通Hitted可替换旧单，但Dizzy等持续状态另有时间、伤害与按攻击归组计数、禁止重复眩晕等规则 | 尚不能用本篇证明某一招第N击必被格挡；还缺具体命中/状态/可用层与AI决策组合。 |
| 顺序能确定到哪一层 | 请求路径中先安排取消，后入新播放命令；取消处理有状态切换和回收，基类处理新单启动 | 不声称所有回调固定同帧、忽略冻结/预测/依赖。 |

## 新增解包范围

`inventory/followup-hitted-assets.json` 保留源pak路径、4份定向提取文件SHA、包元数据、完整tagged导出和未解码项。提取的是 `Animations/System/Orders/Attacks/OrderHitted` 与 `OrderHittedGeneric`，分别具有30/3条完整解码的服务记录。8份数据对象／子对象完成边界解析；2份BlueprintGeneratedClass的native后缀仅保留元数据，不误称属性解析成功。

`m_OrderServices` 从不透明数据变为标准结构数组后，完整核对了元素数、内层tag大小、每个None终止、导出边界与可选4字节零UObject GUID。服务是否真正启动还要结合各自禁用、条件、帧范围和动画通知；“列在CDO中”不等于当前场景生效。

代码清单：`inventory/followup-hitted-disassembly.json`、`inventory/followup-hitted-process-disassembly.json`、`inventory/followup-hitted-cancel-disassembly.json`、`inventory/followup-hitted-routing-disassembly.json`。类型与虚槽：`inventory/followup-hitted-type-layouts.json`。编译器可能折叠相同函数，dumpbin展示的共享符号名可与PDB请求名不同，以清单的精确范围、类型与指令共同核对，不能根据显示的其他别名解释本次作用。

## 剩余具体问题

1. `m_bTimeSinceLastHitPrevails` +0x74尚未定位读取者；正常新旧订单链已不依赖这个字段才能解释，不再用名字猜含义。
2. 固定Grunt实例如何采用这份订单DB，及30项服务中哪些影响恢复/许可/状态，由后续默认订单与服务分支核对。
3. 依赖afterOrder非0、预测、冻结与同一Tick多命中的最末请求选择，保留为明确条件分支；最小实战应固定同招姿态和命中段，比较单击、两击短间隔、长硬直后短硬直的首次可防御时刻。本轮未执行。