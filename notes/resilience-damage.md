# 韧性动作修正与玩家攻击样本（静态证据）

## 构建与方法

目标为本地《师父》Shipping EXE：`E:\Games_Little\Epic\Sifu\Sifu\Binaries\Win64\Sifu-Win64-Shipping.exe`，研究脚本核对的 SHA-256 为 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`。反汇编使用本机已安装的 Visual Studio `dumpbin`，程序范围来自匹配 PDB 的 `game-procedures.json`；分析只读静态数据，未启动游戏，也没有运行时验证。相关原始片段见 `logs/resilience-damage/`，脚本索引为 `inventory/resilience-damage-disassembly.json`。

## 动作期间韧性变化：已确认

`FResilienceOrderServiceInstance::OnStart`（RVA `0x1b41be0`）和 `OnStop`（`0x1b423b0`）仅在弱引用的角色对象有效且属于 `AFightingCharacter` 时执行。两者从实例持有的数据对象读取同一配置字段（对象偏移 `+0x28`，作为整数），再访问角色的 `UDefenseComponent`（角色字段偏移 `+0x12a8`）：OnStart 对 `UDefenseComponent.m_iResilience`（组件偏移 `+0x3d4`）加该量；OnStop 从同一字段减去同一量。`UDefenseComponent` PDB 布局确认 `m_iResilience` 是 `+980` 字节，`m_iResilienceAttackBonus` 是 `+984` 字节。以上两个回调没有写 `m_iResilienceAttackBonus`。

这说明服务实例的生命周期可让角色在某个订单／动作期间获得临时韧性加值，并在停止时撤销该加值。它是“按原值加减”而非保存整份基线后重置；并发实例、回调异常或加值期间其他系统写入是否会产生边界影响，尚未追踪。偏移 `+0x28` 的业务属性名和该服务具体挂载到哪些动作配置，当前资产属性清单无法直接命名，后续要从该服务的 UClass 反射属性或引用它的订单资产补证。

`UHitComponent::GenerateImpact`（`0x1a5a610`）的相关分支读取受击者防御组件 `+0x3d4`，再看攻击 HitBox：若 `m_bOverrideResilience` 为真，用 `m_iOverrideResilienceValue`；否则用 `m_eAttackPower`。当受击者韧性严格大于该攻击值、且受击者没有处于 guard-broken 条件时，设置 `FImpactResult.m_bResilienceImpact`（局部结果偏移 `+0xa8`）。平局不会走这个“韧性更高”分支。该标志接入后续受击流程；本次没有把整个后续所有状态转移穷尽，因此不把这一分支单独等同于“绝对不受击／免疫”。这直接支持的机制解释是：目标处于带韧性加成的攻击动作期间，较低的攻击阈值更可能被韧性判定压过，形成动作期间的抗打断窗口；是否出现反击或格挡由其他状态与 AI 选择共同决定。

两个 Blueprint getter 的执行桩分别直接读取组件 `+0x3d4`（`BPF_GetResilience`）和 `+0x3d8`（`BPF_GetResilienceBonusFromAttack`）。这证实攻击附加韧性是独立字段，但不证明当前 `GenerateImpact` 这处比较会把两者相加；它实际比较的是 `+0x3d4`。

## 主角攻击数据样本：配置值，不等于实战最终值

数据来源：`inventory/object-and-table-properties.csv` 中的本地解包属性，资源均为 `Sifu/Content/DB/_MainChar/Combos/` 下 HitBoxData：

| 资源／行 | 攻击强度 | 覆盖韧性 | 普通命中伤害 | 架势伤害 | 受击帧参数 | 格挡架势伤害 | 弹反架势伤害 |
|---|---|---|---:|---:|---:|---:|---:|
| `MainChar_HitBoxData.uasset` / `Jab_HB01` | Light | 开，1 | 10（Use=true） | 12（Use=true） | 8（Use=true） | 10 | 8 |
| `MainChar_Bats_HitBoxData.uasset` / `Heavy01_HB01` | Strong | 开，5 | 20（Use=true） | 36（Use=true） | 24（Use=true） | 30 | 24 |

数值来自配置字段 `m_OnHitImpact`、`m_OnGuardImpact`、`m_OnDeflectImpact`。`FHitboxDataRow` 布局将它们分别放在 `+0x88`、`+0xc0`、`+0xf8`；`FHitImpact` 内伤害、架势伤害是浮点，是否使用由各自布尔开关控制；受击时长参数是无符号字节帧数。样本说明主角的攻击会同时携带攻击等级、覆盖韧性阈值、普通生命伤害、架势伤害和配置化受击帧数，不能把“冲击力”当作一个统一数值。

`GenerateImpact` 调用 `ApplyDamagesMultipliers`；该函数确实查找并处理角色 `BarehandsDamageMultiplier` 与 `WeaponDamageMultiplier` 属性，并接收武器覆写信息及命中请求。因此表中 10／20 等是命中配置，不足以直接断言等于 UI 生命条上最终扣除量；武器、角色属性、命中类别和运行时分支的全部倍率尚未完整反编译。防守结果还会走 Hit／Guard／Deflect 不同 `FHitImpact` 配置，不能用普通命中数值代表格挡或弹反。

## 证据索引与待补

- `logs/resilience-damage/FResilienceOrderServiceInstance__OnStart-0x1b41be0.asm.txt`
- `logs/resilience-damage/FResilienceOrderServiceInstance__OnStop-0x1b423b0.asm.txt`
- `logs/resilience-damage/FOrderServiceInstance_UResilienceOrderService___Init-0x1b36ba0.asm.txt`
- `logs/resilience-damage/UHitComponent__GenerateImpact-0x1a5a610.asm.txt`
- `logs/resilience-damage/ApplyDamagesMultipliers-0x1a462f0.asm.txt`
- `inventory/stun-state-type-layouts.json`：`UDefenseComponent`、`FHitboxDataRow`、`FHitImpact` 字段布局。
- `inventory/object-and-table-properties.csv`：上述主角攻击样本。

下一步应找出 `UResilienceOrderService` 偏移 `+0x28` 对应的反射字段名，以及关联到具体敌人攻击动作的订单服务配置；之后再把 `m_bResilienceImpact` 如何影响受击／状态退出补成一条可验证链。伤害方面后续只需挑少数代表招式追 `ApplyDamagesMultipliers` 的必要分支，不承诺全游戏伤害公式。

## 补核：字段名称与韧性命中的实际应用

后续由 scripts/inspect_action_resilience_types.py 再读匹配 PDB，生成 inventory/action-resilience-type-layouts.json。UResilienceOrderService 的 +0x28 字段已确认名为 m_iBonus（因此上文“字段名未命名”的缺口现已补齐）。EAttackPowers 为 Light=0、Medium=1、Strong=2；覆盖值可以绕开这三级的数值。当前已解码的 tagged-objects、CDO 与 package-metadata 未检出该服务的具体资产记录，故普通／进阶 Grunt 哪些动作实际挂载此服务仍未确认。

UHitComponent::ApplyImpact（RVA 0x1a46d90）提供了比标志推断更直接的证据。PDB 布局：FApplyImpactStruct 起始为 FHitDescription，其中 FImpactResult 位于 +0x4e0，故 m_bResilienceImpact 为外层 +0x588、m_bLethal 为 +0x548、m_bGuardBreak 为 +0x4e8。0x1a47109 起检查：韧性标志为真、非致命、未破防时进入专门分支；调用 StaminaImpact、条件性的动画震动、Hitted 回调，随后跳到 0x1a482ab，绕过后面的普通 FNetOrderStructHitted 构造与受控状态订单路径。因此这一分支确实不通过本函数的正常受击订单来打断角色。后续仍可能处理命中停顿等效果，不能称为完全免伤、完全不受影响或所有系统绝对无法中断。

重要更正：GenerateImpact 中 0x1a5b4be 已先把普通配置受击帧数乘 1/60 写入 m_fStunTime；0x1a5b6de 的韧性非致命分支跳过的是后续的一部分计算，不能据此说硬直时间被清零。实际“没有进入正常受击订单”的证据来自 ApplyImpact 分支，不是凭 m_fStunTime 推断。8帧／24帧在这处初步换算为约0.133／0.400秒，后续仍可能修正，不能当成实战不可行动时间。

新增证据：inventory/impact-resilience-application-disassembly.json；logs/impact-resilience-application/UHitComponent__ApplyImpact-0x1a46d90.asm.txt。

## 20261028案例批次修订：真实动作与通知已找到

上文“未找到实际动作挂载”的历史缺口已由定向动画提取和bounded解析部分消除：Grunt Base/Advanced组合均引用KneeStrike/SpinKick；服务CDO的m_iBonus分别4/2，动画通知区间分别约0.00166–0.66920s和0.11641–0.39218s。精确证据见notes/case-study-resilience-20261028.md及inventory/case-resilience-notifies-20261028.json；早期零检出不表示不存在。仍缺基础韧性、具体选招/通知实际触发与玩家命中结果，不能写成必定霸体。
