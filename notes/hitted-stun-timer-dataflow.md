# Hitted 订单中的 stun time 与 hit timer 数据流

## 范围与结论

对象为本机构建的 Sifu-Win64-Shipping.exe / 匹配 PDB，问题限定为：普通受击生成的 `FImpactResult.m_fStunTime` 是否写入 `OrderHitted.m_fHitTimeLeft`，以及新受击怎样处理已有 Hitted order。

`m_fStunTime` 会间接进入订单计时：`ApplyImpact` 用当前同步时间加上 impact 的冻结时间，再加受击时长（通常来自 `m_fStunTime`；若选中的受击动画容器提供覆盖时长，则使用覆盖值）生成 `FNetOrderStructHitted.m_iTimeOfEnd`。`OrderHitted::OnStart` 再以这个结束时刻计算基础计时，并扣除冻结帧数在受击动画播放速率下对应的时间，得到 `m_fHitTimeLeft`。因此两字段不是直接赋值关系，但对普通未覆盖情形，确有可追的 `m_fStunTime → m_iTimeOfEnd → m_fHitDuration → m_fHitTimeLeft` 链。

## 结构映射

| 对象 / 字段 | 偏移或类型 | 含义与证据边界 |
|---|---:|---|
| `FImpactResult.m_fStunTime` | `FImpactResult +0x98` | PDB 类型布局；在 `GenerateImpact` 中从命中动画受击帧数换算成秒后写入。 |
| `FNetOrderStructHitted.m_ImpactResult` | 结构内 `+0x5C0` | PDB 类型布局：该结构大小 1936 bytes，继承 `FNetOrderStructPlayAnim`。 |
| `FNetOrderStructHitted.m_iTimeOfEnd` | 结构内 `+0x160` | PDB 类型布局；`ApplyImpact` 生成的结束时刻字段。 |
| `FHittedAnimContainer.m_bOverrideHitDuration` / `m_fOverrideHitDuration` | 容器内 `+0x5C` / `+0x60`，在订单结构中为 `+0x77C` / `+0x780` | PDB 类型布局；开关有效时，`OnStart` 直接使用覆盖秒数作为基础 `m_fHitDuration`。 |
| `OrderHitted.m_fHitDuration` | 对象 `+0x518` | PDB 类型布局。`OnStart` 根据订单的结束时刻计算/校正。 |
| `OrderHitted.m_fHitTimeLeft` | 对象 `+0x51C` | PDB 类型布局。`OnStart` 初始化；`OnUpdate` 递减；到零后进入条件性的恢复许可逻辑。 |
| `UHitComponent.m_fHittedFrozenPlayRate` | 组件 `+0x1C0` | PDB 类型布局；`OnStart` 将其读入公式。 |

注意：`FNetOrderStructHitted.m_ImpactResult.m_fStunTime` 的网络结构绝对偏移为 `+0x658`。这与订单对象自己的 `m_fHitTimeLeft +0x51C` 不是同一字段/偏移空间。

## 因果链与已证实分支

| 阶段 | 观察到的实现 | 结论 |
|---|---|---|
| 1. 本次命中计算 | `UHitComponent::GenerateImpact` RVA `0x1A5A610`，约 `0x1A5B48F–0x1A5B4C6`：从受击帧数换算秒写 `FImpactResult+0x98`。 | `m_fStunTime` 在命中结果阶段生成。 |
| 2. 与旧订单合并 | 同函数约 `0x1A5B545–0x1A5B578`：若查询到旧 Hitted order，且 `UHittedDB+0x75` 为真或本次 `FImpactResult+0x1A` 的 guard-broken 标志为真，则写回 `max(本次 m_fStunTime, 旧 OrderHitted+0x51C)`。 | 这是“最长硬直优先”对**本次结果值**的合并，不是直接写旧订单内存。Grunt 的该 DB 标志为 false；普通命中不走策略开启条件，但 guard-break 条件独立存在。 |
| 3. 生成订单结束时刻 | `UHitComponent::ApplyImpact` RVA `0x1A46D90`：在 `0x1A47100` 先取当前同步时间；`0x1A47B0C–0x1A47B3D` 将 `FImpactResult.m_fInstigatorFreezeDuration`（ApplyImpact 输入结构 `+0x574`）加到该时间。随后 `0x1A47E85–0x1A47ED9` 对这份时间再加受击时长：普通 fallback 读取输入结构 `+0x578`，即 `FImpactResult.m_fStunTime`；当受击动画容器/配置允许时，改用其虚调用返回的覆盖时长。结果保存到网络结构的栈位置 `+0x440`，按结构映射即 `FNetOrderStructHitted.m_iTimeOfEnd (+0x160)`。 | 对未触发动画覆盖的普通路径：`m_iTimeOfEnd = 当前同步时间 + m_fInstigatorFreezeDuration + m_fStunTime`。若动画覆盖条件成立，第二项时长来自覆盖值而非 `m_fStunTime`。 |
| 4. Hitted 网络订单构造 | `ApplyImpact` 约 `0x1A47C95–0x1A47D8C` 构造 `FNetOrderStructHitted`，将 `m_iTimeOfEnd` 存在 `+0x160`，并将完整 `FImpactResult` 复制到 `m_ImpactResult (+0x5C0)`。 | 若前序已执行 longest-stun max，复制的是已修正结果；同时结束时刻已根据修正后的 stun time 计算（除动画时长覆盖路径）。 |
| 5. 请求播放订单 | `ApplyImpact` 约 `0x1A47F5E` 调 `AFightingCharacter::PlayOrderWithType`。其 RVA `0x19C8220` 依据 `FOrderType` 转发至 `AFightingCharacter::PlayOrder` RVA `0x19C7AA0`。 | 这是请求播放一个 Hitted 类型订单的链路；该点没有表现为对旧 order 的 `UpdateOrder` 调用。 |
| 5. 新订单分配与数据设置 | `UOrderComponent::PlayOrder` RVA `0x1AE4F20`：调用 `OrderManager::CreateOrder` 后，经 order 的虚函数槽 `+0x38` 传入 `FNetOrderStruct`；随后交 `OrderManager::PlayOrder`。 | 证实请求路径会创建 order 实例并传入网络结构。它本身尚不足以判断旧订单是并行保留、被队列策略取消，还是被 Manager 其他生命周期规则替换。 |
| 6. 新 Hitted order 启动计时 | `OrderHitted::OnStart` RVA `0x1ADF720`：`0x1ADF95A–0x1ADF9B9` 用 `m_iTimeOfEnd (+0x160) - 当前同步时刻` 算基础值；若 `FHittedAnimContainer.m_bOverrideHitDuration (+0x77C)` 为真，则改用 `m_fOverrideHitDuration (+0x780)`。随后先从该基础值扣除 `m_HitImpact.m_iFreezeFrames/30`，下限夹到 `1/30` 秒并写入 `m_fHitDuration (+0x518)`。仅当 `FImpactResult.m_bLethal (NetStruct+0x628)` 为真，或计时不满足“近似小于等于零”的检查时，才进入后续赋值；否则请求停止并不执行此处 `m_fHitTimeLeft` 写入。进入该分支时，`0x1ADFC3B–0x1ADFC6C` 再写 `m_fHitTimeLeft (+0x51C) = m_fHitDuration - (m_iFreezeFrames/30 × UHitComponent.m_fHittedFrozenPlayRate(+0x1C0))`。NetStruct `+0x5F4` 是 `FImpactResult.m_HitImpact.m_iFreezeFrames`（相对 FImpactResult `+0x34`，即 `FAppliedHitImpact+0x14`）。 | 普通未覆盖路径：`m_fHitDuration = max(1/30, m_iTimeOfEnd - 当前同步时刻 - m_iFreezeFrames/30)`；刚构造订单时，EndTime 通常是当前同步时间加 `m_fInstigatorFreezeDuration + m_fStunTime`，所以基础项约为冻结时长与 stun time 之和，再扣一份 freeze frames。后续条件赋值再扣 `m_iFreezeFrames/30 × m_fHittedFrozenPlayRate`。反汇编呈现两次扣减，本文只记录算式，不推断设计意图。若动画容器覆写命中时长，基础项改用覆盖秒数。 |
| 7. 订单推进与恢复层 | `OrderHitted::OnUpdate` RVA `0x1AE44D0` 递减 `+0x51C`；计时到零且状态检查满足时才 Push `HitRecoveryAvailability`。`OnStop` RVA `0x1AE1A40` 在有效句柄存在时 Pop。 | 内部 hit timer 控制恢复许可层的添加条件；AI 实际消费许可和逐帧顺序尚未证明。 |

## 关于旧订单刷新/替换：本次边界

可确认：

- `GenerateImpact` 会先查询既有 Hitted order，并在满足上述条件时读取其 `+0x51C` 作为 max 比较值。
- `ApplyImpact` 的正常受控路径构造一份 `FNetOrderStructHitted`，调用 `PlayOrderWithType`；`UOrderComponent::PlayOrder` 实际调用 `CreateOrder`，并随后调用 `OrderManager::PlayOrder`。
- `OrderHitted::GetTimeOfEnd` RVA `0x1AD7060` 直接返回订单 net struct 的 `+0x160`；`CreateNetOrderStruct` / `CopyNetOrderStruct` 通过 `FNetOrderStructHitted` 复制构造，没有另行计算 `+0x518`。
- 当前已检查的这一条调用链没有显示它直接调用旧 order 的 `OnNetStructUpdated` / `MultiCastUpdateOrder` 来更新 `+0x51C`。`OnNetStructUpdated` 的已导出实现（RVA `0x1ADBFB0`）主要在特定网络/角色条件下更新骨盆信息，没有刷新 `+0x51C` 的写入。

仍不能确认：

- `OrderManager::PlayOrder` / OrderDB 队列替换和取消策略如何作用于“已有 Hitted + 新 Hitted”；`UOrderComponent::PlayOrder` 的通用 queue replace / cancel 分支依赖 OrderDB 与 `FPlayOrderInfos` 参数，不能从通用代码直接推断该 Hitted 配置的具体策略。
- 订单从 `CreateOrder` 到 `OnStart` 之间，是否存在另一个异步网络或 Manager 分支更改同类型旧单，以及这个更改是否能触发 `OnNetStructUpdated`。
- `m_bTimeSinceLastHitPrevails`（HittedDB `+0x74`）的消费者依旧未定位。本次数据流没有发现其参与 `m_fHitTimeLeft` 赋值。
- `m_fHitTimeLeft` 与视觉上敌人“还能否被打断/何时可防御”的精确运行时对应关系仍缺实测；代码只证明它被递减，并门控某条恢复许可生成分支。

因此，严谨描述应为：**新命中会计算 `m_fStunTime`；特定策略/guard-break 条件会把它与旧 Hitted timer 取 max；修正后的值被写入 Hitted 网络结构，并在没有动画时长覆盖时参与 `m_iTimeOfEnd`。`OnStart` 通过该结束时刻初始化 `m_fHitDuration`，再扣除受击动画冻结帧补偿，得出 `m_fHitTimeLeft`。旧单的实际保留、取消或重叠策略仍待查，因此不能概括为“每次后命中都覆盖旧硬直”。**

## 回查文件

| 证据 | 路径 / RVA |
|---|---|
| 命中 stun time 生成与最长值合并 | `logs/system-recovery/UHitComponent__GenerateImpact-0x1a5a610.asm.txt`，RVA `0x1A5A610`，指令约 `0x1A5B48F–0x1A5B578` |
| 当前时间、冻结时长、StunTime/动画覆盖时长生成 EndTime，以及 NetStruct 复制与播放 | `logs/system-recovery/UHitComponent__ApplyImpact-0x1a46d90.asm.txt`，RVA `0x1A46D90`，`0x1A47100`、`0x1A47B0C–0x1A47B3D`、`0x1A47E85–0x1A47ED9`、`0x1A47C95–0x1A47F5E` |
| `FOrderType` 转发 | `logs/system-recovery/AFightingCharacter__PlayOrderWithType-0x19c8220.asm.txt`，RVA `0x19C8220` |
| 角色订单选择路径 | `logs/system-recovery/AFightingCharacter__PlayOrder-0x19c7aa0.asm.txt`，RVA `0x19C7AA0` |
| CreateOrder、设置 NetStruct、调用 manager | `logs/system-recovery/UOrderComponent__PlayOrder-0x1ae4f20.asm.txt`，RVA `0x1AE4F20`，约 `0x1AE4F84–0x1AE4F93` 和 `0x1AE556B` |
| 内部计时初始化及冻结帧补偿 | `logs/system-recovery/OrderHitted__OnStart-0x1adf720.asm.txt`，RVA `0x1ADF720`，关键指令 `0x1ADF95A–0x1ADF9B9`、`0x1ADFC3B–0x1ADFC6C` |
| 结束时刻 accessor / NetStruct 克隆 | `logs/system-recovery-deep/OrderHitted__GetTimeOfEnd-0x1ad7060.asm.txt`、`OrderHitted__CreateNetOrderStruct-*`、`OrderHitted__CopyNetOrderStruct-0x19ec9b0.asm.txt` |
| 字段映射 | `inventory/stun-state-type-layouts.json`：`FImpactResult.m_fStunTime=+0x98`、`m_fInstigatorFreezeDuration=+0x94`、`m_HitImpact.m_iFreezeFrames=+0x34`；`FNetOrderStructHitted.m_iTimeOfEnd=+0x160`、`m_ImpactResult=+0x5C0`；`FHittedAnimContainer.m_bOverrideHitDuration/m_fOverrideHitDuration=+0x5C/+0x60`；`OrderHitted.m_fHitDuration/m_fHitTimeLeft=+0x518/+0x51C`；`UHitComponent.m_fHittedFrozenPlayRate=+0x1C0` |

所有结论针对这份本地 EXE 与匹配 PDB；是静态控制流证据，不是运行时观测。
