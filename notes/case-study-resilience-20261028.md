# 敌人攻击动作中的临时韧性：资产级样本

## 结论先看

| 已确认 | 目前不能确认 |
|---|---|
| Grunt 的若干徒手攻击动画资产确实导入 `BP_ResilienceOrderService_C` 或 `BP_SuperResilienceOrderService_C`，并导出 `OrderServiceNotifyState`。这不是仅靠资源名猜测。 | 服务 CDO 与通知时间已解出：普通服务 `m_iBonus=2`、Super 服务 `m_iBonus=4`。但基础韧性未知，因此这些加值是否越过任一玩家攻击等级仍不能判定；具体遭遇是否运行该动作也未验证。 |
| 普通型与进阶型 Grunt 的组合数据都引用 `Grunt_KneeStrike` 和 `Grunt_SpinKick`，它们所指动画分别挂有 Super 与普通韧性服务通知。 | 因此现在只能说“攻击动作期间存在临时加韧性的已配置路径”；还不能说这两个动作一定在某个战斗片段里让玩家攻击打不断，也不能给出必定免打断的玩家攻击等级或实战持续秒数；动画配置窗口已列在下表。 |

这为“玩家攻击命中敌人但没有打断”提供了具体可回查的因素样本，但不是已经闭合的实战案例。它把动作期韧性从推测推进到具体服务值和时间窗；结合命中比较逻辑可给出条件化预测，但敌人的动作运行时选择与基础韧性仍未验证。

## 样本范围与证据

固定研究构建：EXE SHA-256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；PDB GUID-age `fdd64e0f-b9ed-4479-8fd8-efe0038b919d / 1`。源 Pak 为本机 Epic Sifu `pakchunk0-WindowsNoEditor.pak`，SHA-256 `497e7e81fc3bba196d19f7f9fd84597c506fd4dc547905f6989847b1510ff2be`。

| Grunt 攻击资源 | 动画行与命中行 | 动画里挂载的通知服务 | Base / Advanced 组合引用 | 解释边界 |
|---|---|---|---|---|
| `Grunt_KneeStrike.uasset` | `Grunt_Attack_Barehands_KneeStrike` / `Knee_HB01` | `BP_SuperResilienceOrderService_C`，`m_iBonus=4`；通知窗约 0.00166–0.66920 秒（60 fps 下约第 0–40.15 帧） | 两套组合都引用 | 配置窗口已解；运行时是否触发、基础韧性未知 |
| `Grunt_SpinKick.uasset` | `Grunt_Attack_Barehands_SpinKick` / `SpinKick_HB01` | `BP_ResilienceOrderService_C`，`m_iBonus=2`；通知窗约 0.11641–0.39218 秒（60 fps 下约第 6.98–23.53 帧） | 两套组合都引用 | 配置窗口已解；运行时是否触发、基础韧性未知 |
| `Grunt_FalconPunch.uasset` | `Grunt_Attack_Barehands_FalconPunch` / `FalconPunch_HB01` | `BP_SuperResilienceOrderService_C`，`m_iBonus=4`；动画通知轨道已定位，未单独解时间窗 | 两套组合都引用 | Base / Advanced 都可达；这里只深解析 KneeStrike / SpinKick 时间窗 |
| `Grunt_540Kick.uasset` | `Grunt_Attack_Barehands_540Kick` / `540Kick_HB01` | `BP_ResilienceOrderService_C`，导出 `OrderServiceNotifyState_0` | 没在这两份 Base / Advanced 组合中找到 | Grunt 攻击 DB 和动画挂载已确认；不能推成普通杂兵常用动作 |
| `Grunt_BodyKick.uasset` | `Grunt_Attack_Barehands_BodyKick` / `BodyKick_HB01` | `BP_SuperResilienceOrderService_C`，导出 `OrderServiceNotifyState_0` | 没在这两份 Grunt 组合中找到 | 名称位于 Grunt DB 不足以证明 Grunt Base / Advanced 会选它；另有 Bodyguard 组合引用 |
| `Grunt_JumpKick.uasset` | `Grunt_Attack_Barehands_JumpKick` / `JumpKick_HB01` | `BP_SuperResilienceOrderService_C`，导出 `OrderServiceNotifyState_1` | 没在这两份 Grunt 组合中找到 | 不能泛化到普通杂兵 |

这里的 `Base / Advanced` 指资产路径 `DB/AI/Archetypes/Grunt/_Base/Grunt_Base_Combo.uasset` 与 `.../_Advanced/Grunt_Advanced_Combo.uasset`。组合节点的 `m_Attacks[]` 直接引用 `Grunt_KneeStrike`、`Grunt_SpinKick`、`Grunt_FalconPunch` 等攻击 DB；攻击 DB 的 `m_AnimationRow` 指向对应动画行；动画包的 Import / Export 表将通知状态类指向韧性服务类。这条静态引用链不等于随机选择概率或特定遭遇的运行时执行记录。

服务 CDO 与两条动画通知区间的结构化解析见 [`inventory/case-resilience-notifies-20261028.json`](../inventory/case-resilience-notifies-20261028.json)。攻击表、命中行、组合引用及源哈希见 [`inventory/case-resilience-config-20261028.json`](../inventory/case-resilience-config-20261028.json)。本批动画资源只定向提取当前 Grunt 徒手攻击目录内的非 `_old` 动画，以及相关韧性服务 Blueprint；文件清单和哈希见 [`inventory/case-resilience-extraction-20261028.json`](../inventory/case-resilience-extraction-20261028.json)。UAsset 表解析结果见 [`inventory/case-resilience-packages-20261028.json`](../inventory/case-resilience-packages-20261028.json)。

## 这个因素怎样可能影响“连续攻击打不断敌人”

已有代码底稿 [`notes/resilience-damage.md`](resilience-damage.md) 记录了以下已接通静态逻辑：

1. `FResilienceOrderServiceInstance::OnStart` 将服务配置字段 `m_iBonus` 加到角色的 `UDefenseComponent.m_iResilience`；`OnStop` 减去同一个值。代码定位分别为 RVA `0x1b41be0` 与 `0x1b423b0`。
2. 命中计算 `UHitComponent::GenerateImpact`（RVA `0x1a5a610`）比较受击者的当前韧性与玩家 HitBox 的攻击等级，或其覆盖阈值。韧性严格更高且未破防时，会标记韧性命中。
3. `UHitComponent::ApplyImpact`（RVA `0x1a46d90`）在韧性命中、非致命、未破防时走专门分支，绕过本函数后续正常 Hitted 订单的构造路径。

可检验的具体规则是：玩家攻击命中时，若 Grunt 当前韧性（原有值加本动作通知临时增量）严格高于玩家 HitBox 的攻击等级／覆写阈值，且 Grunt 未处于 guard break，`GenerateImpact` 会标记韧性命中；已接通的 `ApplyImpact` 分支不会构造普通 Hitted 订单。玩家攻击是否仍造成生命或架势等其他效果，以及 Grunt 随后是否防御／反击，要分别沿后续流程查。KneeStrike 提供 `+4`、约 0.668 秒的具体条件样本，SpinKick 提供 `+2`、约 0.276 秒的样本；但 Grunt 基础韧性和具体遭遇何时选中这些动作还没查明，所以这些是配置级案例，不是“必定霸体”的实测结论。

## 敌人动作自己的命中配置（不要当成玩家来招）

| 命中行 | 攻击等级 | 覆盖韧性 | 普通生命伤害配置 | 架势伤害配置 | 备注 |
|---|---|---|---:|---:|---|
| `Knee_HB01` | Medium | 关 | 15 | 18 | 普通 Grunt Base / Advanced 均引用的候选对照 |
| `SpinKick_HB01` | Strong | 关 | 30 | 36 | 普通 Grunt Base / Advanced 均引用的候选对照 |
| `FalconPunch_HB01` | Strong | 关 | 25 | 42 | 普通 Grunt Base / Advanced 均引用的候选对照 |
| `540Kick_HB01` | Strong | 关 | 30 | 90 | 仅有攻击资源链，当前两份组合未找到引用 |

上表的 `EAttackPowers` 是 Grunt 对玩家出招时使用的攻击等级；它不是玩家攻击 Grunt 时参与韧性比较的输入。这些生命／架势值也与 Grunt 当前韧性无关。玩家 HitBox 的等级或 `m_iOverrideResilienceValue` 才是比较输入。Grunt 攻击表只用于说明样本确实是具体攻击动作，不应把表内 Strong 误读为玩家会被什么等级挡住。

## 为什么还不能回答“哪些能连、哪些连不上”

| 缺口 | 现状 | 关闭缺口所需证据 |
|---|---|---|
| 服务加值 | 两个服务 CDO 已解析：普通 `m_iBonus=2`，Super `m_iBonus=4`；二者继承 `BP_ResilienceOrderService_Base_C`，其父类引用 native `ResilienceOrderService` | 两个数值对应的 OnStart/OnStop 加减逻辑已由匹配 PDB 接通；尚缺 Grunt 的基础韧性默认值 |
| 通知状态区间 | KneeStrike / SpinKick 的 `AnimSequence.Notifies` 已解：服务时间窗分别约 0.00166–0.66920 秒、0.11641–0.39218 秒；`Duration` 与链接起止值吻合 | 已核动画 60 fps 和序列长度；仍需核运行时是否选中相应动作及是否有外层动画覆写 |
| 实际是否采用 | Base / Advanced 组合有静态引用 | 实战中记录敌人动画行、动作开始帧、玩家命中帧与韧性反应；或完整接通选择逻辑与遭遇配置 |
| 玩家招式对照 | 代码比较分支和一部分 HitBox 值已知 | 补齐 Base / Advanced Grunt 的基础韧性，随后选择玩家 Light / Medium / Strong HitBox 与对应时间窗核对条件命中分支 |
| 后续敌人行为 | 韧性分支绕过普通 Hitted 订单已证；敌人随后是否可格挡、闪避或反击还需接 AI 许可／选择链 | 把同一时间线上动画恢复状态、许可查询和 AI 决策条件连起来 |

## 状态与下一项取证

| 阶段 | 状态 |
|---|---|
| 已提取 | 21 个动画／服务资产的 `.uasset` 与 `.uexp` 文件对（非 `_old` Grunt 徒手攻击样本，加韧性服务资源）；缺失 0 |
| 已解析 | 所选包的 UAsset 名称、Import、Export；两服务 CDO 的 `m_iBonus`；KneeStrike / SpinKick 的 `AnimNotifyEvent` 起止时间；攻击／命中字段来自本地属性清单 |
| 已接通逻辑 | 服务 OnStart / OnStop、韧性判定、非致命韧性分支绕过普通 Hitted 订单，见旧底稿 RVA |
| 已实战验证 | 无，本批没有运行游戏 |

下一步先查 Grunt Base / Advanced 对应角色蓝图的基础 `m_iResilience` 默认值与难度覆写，再把普通／进阶敌人的同一来招按“通知窗内／窗外”对照。随后把 `+2`／`+4` 与玩家 Light / Medium / Strong 来招相比较，按代码严格大于规则判断哪些配置组合会走韧性分支。之后仍需实战观测确认具体遭遇是否按静态路径运行；本批没有运行游戏。


