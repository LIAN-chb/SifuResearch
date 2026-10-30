# SuperDizzy 累积与 Counter_Hit 建立：新增代码补证

本支属于 `notes/handoffs/20261030-攻防补证-02.md`。问题是恢复 SuperDizzyDamage 的累计、恢复、阈值、Available 写入，以及 Counter_Hit 真正建立入口；完成条件为定位写入者和消费者，不以字段名猜玩法。写入仅本底稿、`inventory/interaction-20261030-dizzy-*`、`logs/interaction-20261030-dizzy-*`；共享正文、进度与交接由主批合并。停止于下述静态链和具名缺口，没有实战验证。

输入复用 `20261030-攻防理解核对.md`、`20261029-rules-state-update.md`、`20261029-rules-hit-count.md`，以及已存在的 GenerateImpact、PushFightingState、普通伤害 lambda、OrderAttack OnStart/OnUpdate。原有产物已经包含写入线索，因此不重新全量扫描／解包；新反汇编只补 gauge、初始化、Counter_Hit 退出函数。`scripts/disassemble_research.py` 本次成功核 EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254` 后生成有界函数体；PDB 输入为该脚本索引所指本机 Epic PDB，主批另核哈希／GUID。地址均为本构建 RVA，汇编绝对地址减 `0x140000000`。

## 1. 这是可累计的独立 gauge，不是普通 Dizzy 抗性逐拳下降

本批确实恢复了一条累计通道：受击者 `UDefenseComponent.m_SuperDizzyGauge (+0x394)` 有独立当前量、最大值和恢复冷却。它与 FightingState 元素的累计伤害／命中退出量分属不同存储，也与普通 Dizzy 效果等级对状态抗性的严格大于比较不同。

PDB 新布局 `inventory/interaction-20261030-dizzy-target-layouts.json` 由已有 `scripts/rules_20261029_count_types.py` 在内存中替换目标集合与输出名后复用读取器生成；未修改旧脚本。布局含七种目标类型，均成功找到。

| DefenseComponent 偏移 | PDB 字段／实际用途 |
|---|---|
| `0x390` | `m_bCanBeSuperDizzy` |
| `0x394` | gauge `m_fMaxValue`，以下记 M |
| `0x398` | gauge `m_fCooldownBeforeRecovery` |
| `0x39C` | gauge `m_fRecoveryRatePerSec`，以下记 R |
| `0x3A0` | gauge PDB 名为 `m_fRecoveryRatePerSecWhenComplete`；本构建 Add/Set **实际把它作为满量时的恢复冷却来源**，不能按名称解释为满量恢复速率 |
| `0x3A4` | gauge `m_fValue`，以下记 V |
| `0x3A8` | gauge `m_fRecoveryCooldown`，以下记 C |
| `0x3AC` | `m_fSuperDizzyGaugeRatioAfterSuperDizzy` |

AI 配置真正的来源由 `UAIFightingComponent::InitAIWithArchetype` RVA `0x18B62B0` 接通。在 `0x18B6599–0x18B65AB` 取难度索引 d；`0x18B662A–0x18B666F` 读取当前 Archetype `m_SuperDizzyPerDifficulty (+0x3C)` 第 d 个 `FAISuperDizzyParams`，步长 `0x18`：

```text
can <- params+0
M <- params+4 (SuperDizzyResistance)
普通冷却 <- params+8
满量冷却 <- params+0xC (SuperDizzyRecoveryCooldownWhenComplete)
事后比例 <- params+0x10
R <- params+0x14
```

同函数 `0x18B670A–0x18B6721` 在一个调用参数开关成立时调用 `FDefenseGauge::Set(0,false)`；这里的 Set 不刷新 C。该开关的调用者覆盖未在本支恢复，不把它写成每次切换阶段必清零。初始化参数来源有代码，但尚未逐敌人核对实际难度行数值。

## 2. 每击量怎样进入当前值

普通命中路径复用 `logs/rules-20261029-count/_lambda_adb39dcd21b9a951ddcd985a86ede030___operator__-0x1a44770.asm.txt`。`ApplyImpact` 默认普通伤害闭包可在 `0x1A47165` 或 `0x1A4739E` 调到它；它先处理健康伤害，再在 `0x1A44883–0x1A448CC`：

1. 受击者 DefenseComponent 有效且 `m_bCanBeSuperDizzy=true`。
2. 查询该受击者 Dizzy 状态；若存在且子状态为 `SuperDizzy=1`，跳过本次 gauge 加量。
3. 否则取本次 `FApplyImpactStruct +0x508`，调用 gauge `Add(amount,true)`。偏移链为 `FApplyImpactStruct.m_HitDescription (+0)` → `FHitDescription.m_ImpactResult (+0x4E0)` → `FImpactResult.m_HitImpact (+0x20)` → `FAppliedHitImpact.m_fSuperDizzyDamage (+8)`。

闭包还受其上游健康有效／可受伤检查和 ApplyImpact 分流约束；不能把“任意碰撞到 HitBox”都算作加量。它不要求生命伤害量大于零才执行末尾 Add；是否抵达此闭包要看实际 Impact 路径。

`FDefenseGauge::Add` RVA `0x194EB00` 的直接算法是：

```text
V <- clamp(V + amount, 0, M)
若 resetCooldown=true：
    若 V >= M：C <- 满量冷却（gauge+0xC）
    否则：C <- 普通冷却（gauge+4）
```

`Set` RVA `0x1968BC0` 则直接写 V，不夹紧；其 bool 为真才按同一满量条件重置冷却。普通加量即使 amount=0，也能因 bool=true 更新冷却；本支没有据此宣称每个零量 Hit 都抵达此调用。

另有防反反馈来源：`logs/system-parry-attack/UAttackComponent__HandleHitResult-0x1939ec0.asm.txt`，`0x193A842–0x193A8C4` 在本次结果 GuardType=`Deflect(2)`、原攻击者 can、相关防守方对象与 GuardDB 有效等条件下，用 `GetSelfSuperDizzyDamage` 的非近零结果对原攻击者 gauge 调 `Add(true)`。这条与普通受击闭包应分别核算，不能将模板基础零量当最终反馈量；本支没有完成所有模板分支是否双路累加的逐场景核验。

## 3. 阈值写入在分类前预测本击后的量

复用 `logs/system-recovery/UHitComponent__GenerateImpact-0x1a5a610.asm.txt`，`0x1A5B1AE–0x1A5B1E8`。对象是**本次受击者** DefenseComponent，结果是本次 `FImpactResult`：

```text
若受击者 can：
    SuperDizzyAlreadyAvailable (+9) <- V >= M
    SuperDizzyAvailable (+0xA) <- V + 本次 AppliedHitImpact.SuperDizzyDamage >= M
```

第二式发生在真正 Add 之前，是本击阈值预测；等于即可满足。这里没有直接 Push SuperDizzy，且没有读取“对方同时命中”。Available 是进入后续分支的输入，不能单独读成已经眩晕。

已恢复的消费者应与最新状态规格合读：`ComputeImpactType` 将 Available 用于已有 Dizzy 的眩晕候选许可；`UpdateFightingStateFromImpact` 的 `T5`（`0x1A70CB6–0x1A70D08`）在所选 T 不是 Dizzy、AvoidDizzy=true 且 Available=true 时额外 Apply Dizzy/SuperDizzy。普通 Dizzy 等级比较本身仍是独立入口。不能从“量满”推成任何命中都自动建立 SuperDizzy；缺少具体命中分类／AvoidDizzy 条件的案例仍不能计算保证拳数。

## 4. 冷却、衰减和进入 SuperDizzy 后重设

`UDefenseComponent::TickComponent` RVA `0x196A130` 的 `0x196A141–0x196A1BF`：全局 `s_bBlockAllSuperDizzyGauges` 为真时跳过此恢复体。否则：

- C>0 时先扣 delta；若扣后 C>=0，本 Tick 不改 V。
- 若跨过零，只用超出冷却的那部分 delta，并将 C 归零；C<=0 时使用整个 delta。
- 有正的可用 delta 时，`V <- clamp(V + delta * R, 0, M)`。R 是配置的有符号值：R<0 才是下降；不能只凭 Recovery 名称推断所有配置都下降。

这段没有额外读 can，也没有检查正在 SuperDizzy。构造函数 `0x194C848–0x194C870` 的默认 M=1、普通冷却=1、R=-1、满量冷却=-1、V=C=0；AI 初始化会覆盖相关配置，默认值不代表具体敌人。

`PushFightingState` RVA `0x1966D90` 的 `0x1966F6C–0x1966FE0`：当新状态为 Dizzy、传入子状态为 SuperDizzy，且该角色 can=true，查询并 Pop 已有 Dizzy 元素（若存在），再设 `V <- 事后比例 * M`、`C <- 0`。它直接重设 gauge，并不保留满量；也不是等待 SuperDizzy 动画结束才重设。随后建立状态与恢复架势阻塞等处理仍照原函数继续。gauge 的满量条件与 SuperDizzy 状态本身的计时／累计退出是两套量。

## 5. Counter_Hit 是攻击订单建立的状态窗口

复用 `logs/hitclock16-disassembly/OrderAttack__OnStart-0x1adc9c0.asm.txt`：非预测（`OrderBase.m_bInPrediction +0x100=false`）路径 `0x1ADDF6C–0x1ADE086` 为**攻击订单所属角色**取得 DefenseComponent，先 PushOpenedState，再 `PushFightingState(state=Counter_Hit(2), 当前抗性DB, duration=-1, maxDamage=-1, accumulatedDamage=0, maxHits=-1, accumulatedHits=0, substate=None)`；保存 handle 到 `OrderAttack.m_iFightingStateHandleCounterHit +0x6B0`，把 `m_bFightingStatePushed +0x6B4` 置真。

因此真实入口不是“同时命中后创建 Counter_Hit”。在该 OrderAttack 正式启动路径中，攻击角色已经持有它，随后若被另一方打中，命中分类可读取这个当前状态对应抗性。Counter_Hit 不等于中断／受击动作已经发生，也不意味着所有订单子类、所有攻击阶段均保留它。

退出也已有代码链：

| 路径 | 行为与精确位置 |
|---|---|
| OrderAttack OnUpdate | `logs/hitclock16-disassembly/OrderAttack__OnUpdate-0x1ae23c0.asm.txt`，非预测分支 `0x1AE270E–0x1AE2726` 在 `OrderAttackInterface` 虚接口 `+0x60` 返回 2 时调用 `OrderAttack::PopFightingState`。 |
| 阶段值恢复 | 新反汇编 `OrderAttack::GetAttackState` RVA `0x1AD35F0`，返回 0/1/2：读取订单进度值，低于 `m_fAttackStrikeStartFrameRatio (+0x5AC)` 为0；在其上且低于 `m_fAttackReleaseStartFrameRatio (+0x5B0)` 为1；达到 release 阈值为2。此函数接收 Interface 子对象，内部字段为 +0x3FC/+0x400。虚槽分派未在本支逐表验证，因此 OnUpdate 的槽名映射保留该一项边界。 |
| OrderAttack OnStop | RVA `0x1AE0C70`，`0x1AE0E48` 调 PopFightingState；订单提前停止也有清理入口。 |
| 真正移除 | `OrderAttack::PopFightingState` RVA `0x1AE5C00`：仅 pushed=true 执行；先置false，再以状态2和 `+0x6B0` 保存的 handle 调 DefenseComponent Pop（`0x1AE5C25–0x1AE5C36`）。重复调用不重复 Pop。 |

`duration=-1` 意味着这个元素不能靠正常 Tick 计时自然结束；上面的显式 Pop 控制攻击窗口。与状态矩阵合读，可以说攻击期间存在一个使用 Counter_Hit 行抗性的机会窗口；不能把“前摇任意一帧被打必大硬直”写成充要规则，仍需本击效果等级、当前最高状态和后续分类／订单分支。当前已核普通／进阶 Grunt Counter_Hit 行 `[击倒0, 推开0, 眩晕1]` 的原配置证据见 `exports/state-resistance-matrices.csv`，它不代表全部敌人。

## 6. 主批续接复核与验证边界

背景支在最终执行清单整理阶段中断；主批续接后保留所有原始输出，另用保存的 `scripts/interaction_20261030_dizzy_types.py` 复现七类型读取，输出 `inventory/interaction-20261030-dizzy-rechecked-layouts.json`，七种均找到；原布局保留不覆盖。执行参数、脚本及输出哈希在 `inventory/interaction-20261030-dizzy-types-batch.json`。

上节C02虚槽缺口已由主批关闭：沿16批public定位，以本轮已核哈希的PE重读OrderAttackInterface虚表RVA0x48883C0的+0x60槽，目标确为0x1AD35F0 GetAttackState；见 `inventory/interaction-20261030-counter-slot.json`。上节表中“虚槽分派未在本支逐表验证”保留作为背景支当时边界，当前总报告采用本轮直接复核结果。

新增构造函数组 `inventory/interaction-20261030-dizzy-defaults-disassembly.json` 还有1项，故本支累计15份新增反汇编输出（下列四组14项之外另加defaults1项）。Archetype构造中三份难度参数原生默认can=true、max150、普通／满量冷却3／3、事后比例0、速率-20；这些不是已确认的Grunt实例值。全CSV精确前缀m_SuperDizzyPerDifficulty检索0项，仅证明此拼写下未导出扁平字段，不证明无序列化覆写。总执行／输出核查在 `inventory/interaction-20261030-batch.json`。

主批发布前再次核对PDB：该成员类型为FAISuperDizzyParams[3]，+0x84起是m_bCanBeSuperDizzy_DEPRECATED等旧字段，不能把构造中连续相似赋值误认成第四难度行。草稿的“四份”已在发布前改成三份；本修订说明保留原误读缘由。

- 新反汇编四组清单：`interaction-20261030-dizzy-core-disassembly.json`（6函数）、`-counter-disassembly.json`（3函数）、`-init-disassembly.json`（3函数）、`-phase-disassembly.json`（2函数）。共14个函数体；EXE哈希由每次脚本实际校验。
- 新类型布局7种目标全部找到。PDB名称/偏移不单独当运行行为证据，上述算法均有指令读取／写入。
- 无新资产提取、游戏／存档写入或实战。没有执行补解包检查；本支未产生补解包批次。知识库及主批链接检查由父代理按最终合并范围执行。
- 一个定向函数名探测 `OrderAttack::OnAnimPhaseChanged` 不在PDB索引，已记在counter清单；随后复用已有 OnUpdate 并找到真实 Pop，不再靠该猜名推进。两次 PowerShell 通配符误传 rg、一次内联Python引号失败均未写入目标文件，随后改为目录+glob／here-string成功。
- 后续最有价值的补证：逐敌人难度参数实际值、普通命中 Available→各强效果选择的完整真值表、Deflect 模板与直接反馈 gauge 是否在同场景双路执行、接口虚槽+0x60与具体 GetAttackState 的分派确认，以及运行时逐帧观察。局部缺口不否定已恢复的累积／恢复算法和 Counter_Hit 的订单建立事实。

用户无需手动操作。本支未自行暂存或提交，交由主批合并并验证。
