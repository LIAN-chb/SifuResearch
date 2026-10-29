# 连续受击到恢复与 AI 防御：静态证据链

## 范围和结论状态

对象限于本地 Sifu 构建中的普通徒手 Grunt（`Grunt_Base`、`Grunt_Adv`），重点为普通连续命中后何时重新获得受击恢复许可、何时 AI 可选防御。仅静态分析匹配的 Shipping EXE/PDB 与已提取配置；不运行游戏，不改游戏、存档或 LIAN 项目。

| 标记 | 含义 |
|---|---|
| 已确认 | PDB 符号范围内的指令或本机构建资产明确支持 |
| 部分确认 | 主体分支明确，但准确字段语义、动态顺序或运行时结果还缺证 |
| 未闭合 | 需要继续追调用、字段或运行时观测，不以名字推断 |

**目前能确认的是多条有条件的通路，而不是一个统一“打几下就防御”的计数器。** `OrderHitted` 的受击恢复许可由受击剩余计时及多项状态条件共同控制；持续 fighting state 的存续另由时间、伤害和命中数策略管理；AI 防御再依据来袭攻击预测、当前状态、上下文防御图和攻击记忆决定请求。三者之间存在接口，但没有证据证明每次受击许可到期都会紧接 AI 格挡/反击。

## 核心因果链

| 环节 | 当前证据支持的行为 | 结论状态与缺口 | 主要证据 |
|---|---|---|---|
| 受击订单启动 | `OrderHitted::OnStart` 在生效分支生成 `FHitDescription` 并调用角色 `Hitted`；它还初始化受击订单服务。命中/受击处理由该订单启动路径承载。 | 已确认代码调用关系；哪个碰撞事件先排入订单、与其他事件的逐帧顺序未在此追踪。 | `logs/system-recovery/OrderHitted__OnStart-0x1adf720.asm.txt`，RVA `0x1adf720` 起；`AFightingCharacter::Hitted_Implementation` RVA `0x19c0b20`。 |
| 硬直计时递减 | `OrderHitted::OnUpdate` 先调用 `OrderPlayAnim::OnUpdate`；之后对内部受击计时按 DeltaTime 递减。受击计时仍大于 0 时不会进入其计时到期许可分支。 | 已确认这一计时用途；`m_fHitTimeLeft` 等字段映射依赖 PDB/对象布局，具体资产字段是否进入此计时尚未闭合。 | `OrderHitted::OnUpdate` RVA `0x1ae44d0`，约 `0x1ae46e4–0x1ae4709`。 |
| 恢复可用层 | 计时到期且该订单仍活动时，分支检查状态字段与角色能力；满足路径才调用 `UAvailabilityLayerData::GenerateAvailabilityLayer`，再调用角色 `PushAvailabilityLayer`，名称参数为 `HitRecoveryAvailability`，并把返回句柄存入订单。该路径之后广播受击组件委托。 | 已确认许可是临时层、可条件性添加；静态代码不能证明层何时被玩家/AI输入查询消费，也不能把它等同于“动画结束”。 | `OrderHitted::OnUpdate` RVA `0x1ae44d0`，尤其 `0x1ae4702–0x1ae47b1`。 |
| 许可撤销/订单停止 | `OrderHitted::OnStop` 检查存储句柄是否为无效哨兵；有效时用该句柄、订单自身和 `HitRecoveryAvailability` 名称调用 `ABaseCharacter::PopAvailabilityLayer`，随后将句柄重置为无效值。 | 已确认该许可层随 Hitted 订单停止而移除；订单何时停止仍由订单本身的结束条件决定。 | `OrderHitted::OnStop` RVA `0x1ae1a40`，约 `0x1ae1c89–0x1ae1cba`；`OrderHitted::OnUpdate` RVA `0x1ae44d0`。 |
| 持续 fighting state 进入 | `UHitComponent::ApplyFightingStateFromImpact` 根据影响类型/抗性反应、既有状态的剩余时间/配置及命中参数准备时间与状态参数，最后调用 `UDefenseComponent::PushFightingState`，并将返回标识写回订单侧结构。它在特定 state 分支可先 Pop 一个已有状态，再查询另一个状态并比较剩余时间。 | 已确认会有 Push；精确各 `EFightingState` 数值和每个输入字段语义需结合类型布局与抗性行继续标注，不从裸枚举值猜名称。 | `UHitComponent::ApplyFightingStateFromImpact` RVA `0x1a46990`，`0x1a46b05–0x1a46d69`。 |
| 状态订单生命周期 | `OrderFightingState::OnStart` 对 AI/有 DefenseComponent 的角色调用 `BPF_GetFightingStateTimeLeft`；若查询有效则以查询所得时间初始化动画/订单时长，否则请求停止。订单生命周期到停止路径后，`OnStop` 在对应 virtual gate/订单标志允许时调用 `PopFightingState`；另有显式 `PopFightingState()` 路径以同样的状态标识/handle 执行 Pop。 | 已确认 fighting-state recovery order 借用已存在状态剩余时间、停止时有条件 Pop；这段 `OrderFightingState` 生命周期函数未见其 Push `HitRecoveryAvailability`，该许可属于独立 Hitted 订单路径。静态未证明动画、状态变化和 AI 回调的事件先后帧。 | `OrderFightingState::OnStart` RVA `0x1a074f0`；`OnStop` RVA `0x1a07ed0`；`PopFightingState` RVA `0x1a0b440`。 |
| Recovery 动画来源 | `OrderFightingStateRecovery::OnStart` 获取 DefenseComponent 与 `UAttackPropertiesResistanceDB`；读取状态/象限后调用 `GetRecoveryAnimOfFightingState` 取得动画容器，再进入 `OrderPlayAnim::OnStart`。 | 已确认恢复动画由当前 FightingState 与方向象限映射到抗性 DB；动画是否完成即意味着防御/攻击输入许可恢复，需要另查 Availability 与订单状态。 | `OrderFightingStateRecovery::OnStart` RVA `0x1a075c0`，`0x1a0909–0x1a0924` 附近。 |
| AI 恢复动作回调 | `FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero` 会查找已注册/当前防御相关动作、按 impact type 查询 `FPropertyReaction` 的条件动作并尝试调度；成功安排时延长关联播放动画订单的 time-left `0.5s` 并 veto 此次零时到期处理。 | 已确认是条件式反应动作和延期路径，不是固定恢复时长。没有成功安排时该回调不 veto；并不能直接推出随即格挡。 | RVA `0x18bd1a0`，见 `logs/system-recovery/FAIDefenseHandler__OnOrderFightingStateTimeLeftReachedZero-0x18bd1a0.asm.txt`。 |
| AI 选防御 | `UpdateDefenseNeed` 经 `IsDefenseNeededInternal` 和 incoming-attack prediction 后再读取最高 active fighting state/ContextualDefense，生成并验证请求。情境防御会按节点测试、攻击记忆、概率/遍历等选项。 | 已确认分支不是单纯按受击次数。Base/Adv 的具体图测试/边见既有 [AI 防御与攻击记忆笔记](stun-ai-defense.md)。 | `FAIDefenseHandler::UpdateDefenseNeed` RVA `0x18c9e50`；`IsDefenseNeededInternal` RVA `0x18b8fc0`；`UAIContextualDefense::PickContextualDefense` RVA `0x1895070`。 |

## Grunt 配置对照

本表为资产配置值，不代表命中后实战必然出现的结果。构建内提取见 `inventory/stun-state-data.json` 的 `hitted_assets` 记录；Grunt 自身对象继承 `AIHittedDB`，而不是直接继承通用 HittedDB。其命中恢复许可指向 AI 专用层。

| 对象 | `GruntHittedDB` 父对象 | 时间优先标志 `m_bTimeSinceLastHitPrevails` | 多次受击取最长硬直 `m_bLongestStunPrevailsBetweenHits` | Hit Recovery Availability | 状态/动画请求 |
|---|---|---:|---:|---|---|
| Grunt_Base 与 Adv 共用的基础 HittedDB | `/Game/DB/Hit/AIHittedDB` | `false` | `false` | `AIHittedRecovery` | `BP_GruntHitAnims` |
| 当前主角 HittedDB 对照 | `/Game/DB/Hit/HittedDB` | `false` | `false` | `HittedRecovery` | `BP_MainCharHitAnims` |

两个 Grunt 变体共用 HittedDB；该表没有证明任何仅属于 Base 或 Adv 的受击硬直差异。Base/Adv 的 fighting-state resistance 实际矩阵同值；contextual defense authored graph 有差异，分别记录在原研究底稿。两个 HittedDB 布尔策略的名字和序列化值已确认。`m_bLongestStunPrevailsBetweenHits` 的读取与 max 刷新分支已确认；`m_bTimeSinceLastHitPrevails` 的消费点在本轮已检查的相关命中计算反汇编中仍未定位，故暂不为它的 false 写出行为释义。

## 状态与时序解读边界

| 事项 | 可写结论 | 暂时不能写成的结论 |
|---|---|---|
| 硬直/动画 | 内部受击计时到零会开放一条有条件的 `HitRecoveryAvailability` 添加路径；动画更新是并行先调用的逻辑。 | “动画结束就能防御”或“硬直计时必等于动画剩余时间”。 |
| 连续命中 | 新的 hit impact 可再次走 `ApplyFightingStateFromImpact` 并 Push fighting state；状态系统另有按时长/伤害/命中数停止持续状态的机制（此前已由父级底稿整理）。 | “第 N 下固定解除受控”“所有攻击被某个全局反无限连计数器挡住”。 |
| AI 格挡/反击 | 防御图读取来袭攻击预测、当前状态与近期攻击记忆；受击后的恢复动作调度还可能推迟播放订单到期。 | “恢复许可到期马上格挡/反击”或“连续同招必触发特定应对”。 |
| 状态回收 | fighting-state order 的停止路径在条件成立时 Pop 对应状态；impact 路径本身也可能按分支先 Pop 再 Push/查询。 | “所有状态只在动画结束后 Pop”或“Pop 就意味着 AI 立刻空闲”。 |

**事件先后缺口：** 这些函数足以组成调用/状态链，但不足以恢复受击、广播、组件委托、AI 下一次 Tick、状态订单停止及新防御请求的严格逐帧顺序。本轮没有 PDB/代码证据可以断言某个 callback 必定先于某个 AI 选择或同帧发生。

## 系统线索（便于继续展开）

| 因素与作用位置 | 证据 / 已知作用 | 未解问题 | 优先级 / 回查入口 |
|---|---|---|---|
| `m_bTimeSinceLastHitPrevails` 时间策略 | Grunt 配置 false，PDB 偏移 `+116`；本次已查的 GenerateImpact、ApplyImpact、Hitted OnStart/Stop/Update、状态更新反汇编中没有该数据库对象 `+0x74` 的读取。 | 消费者可能在未覆盖的函数或 Blueprint 路径；目前没有行为解释，不能从名字补语义。 | 阻塞项但不妨碍陈述最长硬直分支；后续按 asset getter/调用链继续查。 |
| `m_bLongestStunPrevailsBetweenHits` 最长硬直策略 | Grunt 配置 false；`GenerateImpact` 在既有 Hitted order 时读取 HittedDB `+0x75`，在策略 true 或本次已 guard-broken 时 max(本次 stun, 旧订单剩余 stun)。 | 常规 Grunt hit 不受此 max 规则影响；guard-broken 分支仍可能触发。 | 已闭合常规策略，保留特殊 guard-break 边界。 |
| `HitRecoveryAvailability` | 受击到期时按层数据生成许可并 Push；`OrderHitted::OnStop` 有句柄时 Pop，Grunt 使用 `AIHittedRecovery`。 | AI/输入消费点及 Pop 相对下一次 AI Tick 的逐帧时序未闭合。 | 直接关联主线；已完成层生命周期，后续查 Availability 查询端。 |
| FightingState 恢复动画 | ResistanceDB 用 FightingState+象限查 `FAnimContainer`；状态订单到期 callback 可调度 reaction action 并 veto/延迟结束。 | 对应 Base/Adv 实际 Reaction/动画行；哪些 action 改变可防御许可，播放订单的最终退出点。 | 直接关联主线；补本构建资产行与 `OnTimeLeftReachedZero`。 |
| AI 攻击记忆与防御图 | 已有证据表明最新命中模式可影响 contextual defense 节点选择，Base 与 Adv 图不同。 | 普通连续攻击的具体候选节点，受击到攻击记忆登记的顺序和当前图所有竞争条件。 | 后续直接展开；复用 [AI 防御笔记](stun-ai-defense.md) 的记忆与图索引。 |
| `m_bInverted` 默认值 | PDB 布局显示 UAIInfluenceTest 为 80 字节并继承 72 字节 UAIInfluenceNode；反射属性记录 `m_bInverted`；InternalConstructor 在 `object+0x48` 写 0。 | 原生默认 false 已由父类/派生尺寸、属性反射和构造共同确认；FieldList 未直接列字段，未作运行时验证。 | 已闭合；可用于解释省略该属性的 AttackMemoryInfluenceTest 配置。 |

## 本轮取证和复现

- 复现入口：[trace_recovery_system.py](../scripts/trace_recovery_system.py)；匹配 PDB 的影响测试继承布局与 default-field 核验由 [trace_recovery_types.py](../scripts/trace_recovery_types.py) 生成。它复用 SHA 校验的 `disassemble_research.py`，把命名 PDB procedure 输出到 `logs/system-recovery/`；生成 [system-recovery-manifest.json](../inventory/system-recovery-manifest.json) 和 [Grunt HittedDB 摘要](../inventory/system-recovery-grunt-hitteddb.json)。
- 本次反汇编覆盖 22 个过程，清单记录本地 EXE SHA256、PDB、每份 `.asm.txt` 的 SHA256 与限制。需将具体结论回查到表中 RVA 与文件，不把反汇编当作运行验证。
- 两个 Grunt 难度变体实际共用同一 `GruntHittedDB` 配置；这证明共享引用，不证明游戏内所有变体或版本相同。

## 下一步取证

1. `m_bLongestStunPrevailsBetweenHits` 已证明会控制新受击 stun time 与已有 Hitted order 剩余时间的 max 合并；继续追 `m_bTimeSinceLastHitPrevails` 的消费者。`OrderHitted::OnUpdate` 的恢复许可计时与层生命周期已定位，但时间优先字段是否调整动画/受击计时仍未闭合。
2. 层移除已由 `OrderHitted::OnStop` 直接证实；后续定位 AI/输入侧查询 `AIHittedRecovery` 的动作请求路径。
3. 追 `OrderFightingState::OnTimeLeftReachedZero`、`OrderFightingStateRecovery` 的订单添加/停止调用，补齐状态、动画和 callback 的先后条件。
4. `m_bInverted` 原生默认 false 已由 `scripts/trace_recovery_types.py` 与构造函数 RVA `0x1bf9870` 闭合。
5. 只在前三条调用闭合后，将普通命中、招架后追击、闪避后追击按同一链路比较；此笔记当前只闭合普通连续命中的静态结构。


## 新增因素：当前 FightingState 会改变后续命中的抗性配置

父级研究新增了 Base/Adv ResistanceDB 对照，故把它纳入这条共享系统。两套配置在本研究的矩阵行上完全相同；状态切换可能改变同一普通追击走到的状态效果分支，这是“连续打击脱离”与“防反/闪避追击窗口”之间的关键候选共同因素。

| 当前 FightingState | 击倒抗性列 | 推开抗性列 | 眩晕抗性列 | 本轮可说的事实 |
|---|---:|---:|---:|---|
| `InFight` | 2 | 2 | 11 | Grunt_Base 与 Grunt_Adv 的序列化矩阵值相同 |
| `Dizzy` | 0 | 0 | 1 | 三列配置值均低于 `InFight` 对应列 |
| `Counter_Hit` | 0 | 0 | 1 | 与 Dizzy 对应列相同 |
| `Avoided` / `Parried` / `StructureBroken` | 0 | 0 | 1 | 这几种状态的眩晕抗性列为 1，击倒/推开列为 0 |
| `Pushed` | 0 | 100 | 1 | 推开抗性列为 100；是否可视为不可推开以及持续时段需看代码消费规则 |

来源：`exports/state-resistance-matrices.csv`，派生到 `inventory/system-recovery-grunt-state-matrix.json`。矩阵列名是导出脚本根据属性结构整理的抗性通道，**这些值不是“还可挨几拳”的直接保证，也不能仅凭 11/1 断言具体攻击数**。要回答“普通追击在 Dizzy 可再击倒/推开/眩晕，而站立 InFight 不可”的实战条件，仍需查明具体 hitbox 的攻击等级以及受击/韧性路径是否截断同一攻击。

| 关系点 | 证据 | 状态 |
|---|---|---|
| 命中结果可以绕过普通受击订单 | 既有 [韧性与伤害笔记](resilience-damage.md) 记录 `UHitComponent::ApplyImpact` RVA `0x1a46d90`：`m_bResilienceImpact` 为真、非致命、未破防时走专门分支并跳过常规 `FNetOrderStructHitted` 构造路径。 | 这条韧性路径独立于 FightingState 抗性矩阵；目标韧性与当前动画服务仍需关联到具体敌人动作配置。 |
| 防反后眩晕命中是条件路径 | 已定位的父级证据：GuardAbility 的 `m_ParryDizzyHit` 使用 `Generic_HitBoxData/ParryDizzy_HB01`，眩晕等级 1000、`UseHitAnimDuration=true`；`OnHitDefense` 仅在 `CanDeflect` 且来袭 HitBox 的 `m_bDizzyOnParry` 为真时调用该命中。 | 不能把“成功防反”泛化为必定施加该眩晕 hitbox；普通命中与这个反击命中要分开建模。 |
| 普通追击在 FightingState 间的分流 | Base/Adv 的矩阵相同，`InFight` 对击倒/推开/眩晕的列值为 2/2/11；`Dizzy` 为 0/0/1。 | 已确认配置差异；命中属性到状态转移的阈值消费、状态记数刷新规则尚未闭合，不能据此直接声称 Dizzy 下必定能重施状态。 |

**展开优先级：直接关联主线。** 抗性消费顺序已由前序静态分析确认；本轮应优先抽取徒手 ordinary follow-up 的攻击等级行，按 `InFight` 与 `Dizzy` 矩阵模拟候选状态转移，并把配置候选与运行时命中结果分列。防反专用 `ParryDizzy_HB01` 保持单独一类，不并入普通 follow-up。

### 徒手普通追击的配置候选：InFight 与 Dizzy 的分流

按 `ComputeImpactType` 已确认的严格比较 (`攻击等级 > 当前状态抗性`) 和优先级 Push → KnockDown → Dizzy，把已提取的 `MainChar_HitBoxData` 行与 Grunt 两状态矩阵交叉，122 行中发现 9 个状态候选结果不同。这里列的是全局命中数据表里的攻击 HitBox 行；是否由某个实际招式/命中段引用，需再沿招式配置映射核对，不能称作实战必然。

| HitBox 行 | 配置等级 `[击倒, 推开, 眩晕]` | 当前 `InFight` 候选 | 当前 `Dizzy` 候选 | 解释 / 限制 |
|---|---:|---|---|---|
| `GroundedPunch_HB01` | `[0,0,2]` | 普通 Hit | Dizzy 候选 | Dizzy 现态的眩晕抗性为 1，等级 2 严格大于 1；若该状态禁止顶层眩晕且没有 SuperDizzy 可用，代码会将结果回落普通 Hit。 |
| `GroundedPunch_BT_HB01` | `[0,0,4]` | 普通 Hit | Dizzy 候选 | 同上，效应级别更高但仍受 Dizzy 顶层分支约束。 |
| `ChargedPunch_Base_HB01` | `[0,0,4]` | 普通 Hit | Dizzy 候选 | 数据行候选；需核对它被哪些难度/姿态配置引用。 |
| `JumpingKick_HB01` | `[0,1,0]` | 普通 Hit | Push 候选 | `Push=1` 未超过 InFight 的 2，但超过 Dizzy 的 0；若命中路径没有其他 gate，则静态候选在两状态之间不同。 |
| `AoeKnockdown` / `BackHookKick` | `[1,0,0]` | 普通 Hit | KnockDown 候选 | 需要确认这两行是否属于此处的徒手普通追击/其实际引用角色；数据表本身只证明行值。 |
| `Jab_HB01` / `PalmStrike_HB01` / `3Punches_HB03` | `[0,0,0]` / `[0,3,0]` / `[0,0,14]` | 普通 Hit / Push / Dizzy | 普通 Hit / Push / Dizzy 候选 | 这些代表值并非都产生状态差异：PalmStrike 的 Push 同时超过两状态阈值；3Punches 末段的 Dizzy等级同时超过两者阈值。 |

派生候选清单：`inventory/system-recovery-hitbox-state-candidates.json`；原始属性：`inventory/object-and-table-properties.csv` 中 `MainChar_HitBoxData.uasset` 的对应行；矩阵：`exports/state-resistance-matrices.csv`。状态等级数值和通道优先级均是静态配置/代码事实；上述“候选”尚未证明命中实际发生、该数据表行被当前动作引用、目标状态当帧未变，或前置 Hitted/韧性检查允许通过。

这批值已给出下一步具体入口：先反查 `GroundedPunch_HB01`、`GroundedPunch_BT_HB01`、`JumpingKick_HB01` 的引用招式与难度条件，再核对 `m_bAllowDizzyOnTop`、`SuperDizzyAvailable` 及状态订单是否会在追击命中前退出。这样可比较 `InFight` 站立与 `Dizzy` 的同一普通攻击路径，而不是拿不同招式或专用防反眩晕数据作类比。

## 补闭合：最长硬直刷新策略与订单恢复层生命周期

`UHitComponent::GenerateImpact`（RVA `0x1a5a610`）把当前命中配置的受击帧数换算为秒写入 `FImpactResult.m_StunTime`（结构偏移 `+0x98`）。已有进行中的 Hitted order 时，代码通过 `UHitComponent.m_HittedDB`（`UHitComponent` PDB 偏移 `+0x1d0`）读取 `UHittedDB.m_bLongestStunPrevailsBetweenHits`（`UHittedDB` 偏移 `+0x75`）。当该配置为 true，或当前 `FImpactResult.m_bAlreadyGuardBroken`（偏移 `+0x1a`）为 true 时，计算 `max(本次 m_StunTime, 现有 OrderHitted.m_fHitTimeLeft[+0x51c])` 并写回本次结果；否则该条件分支不取二者最大值。

对 Grunt 的实际配置 `false` 而言，可确认的是**常规命中不会因这条“最长硬直优先”规则而把本次 m_StunTime 与现有剩余时间取 max**。但有独立 guard-break 条件时仍会走 max；此外本轮没有追完订单替换/刷新或其他路径是否重写剩余时间，不能概括为“后命中总会覆盖旧硬直”。这一策略不等于普通硬直不会刷新，也不说明重复受击是否会阻止 `OrderHitted` 停止。

| 因素 | 证据与作用 | 未闭合处 |
|---|---|---|
| `m_bLongestStunPrevailsBetweenHits` | `GenerateImpact` RVA `0x1a5a610`，约 `0x1a5b545–0x1a5b578`：命中 HittedDB 的 `+0x75`；由当前已 GuardBroken 标志或该字段开启时，将本次 `m_StunTime` 与已有 Hitted order 的 `m_fHitTimeLeft` 取 max。Grunt = false。 | 继续追现有订单的定位/替换规则，以及 GuardBroken 这条独立 max 路径对主线的影响范围。 |
| `m_bTimeSinceLastHitPrevails` | Grunt DB = false，PDB 字段偏移 `+0x74`。 | 在本轮已导出的 `GenerateImpact`、`ApplyImpact`、订单 Start/Stop/Update 和 FightingState 更新路径中，没发现针对 HittedDB `+0x74` 的读取；不能据字段名推断具体时间字段或更新优先级。可能消费者在其他函数/Blueprint路径，静态缺口留待调用链定位。 |
| `HitRecoveryAvailability` | Hitted 订单计时归零时满足状态条件后生成许可层并 Push；订单停止时如句柄有效，`OrderHitted::OnStop` 使用同一层名和句柄 Pop，随后重置句柄为无效值。 | AI/输入何时采样这层与订单停止/AI 下一次 Tick 的严格逐帧关系没有静态保证。 |
| FightingState recovery order | `OrderFightingState::OnStart` 查询 DefenseComponent 当前 state time-left；无有效 state 时请求订单停止。`OnTimeLeftReachedZero` 遍历注册回调，只有没人 veto 才继续父类 `OrderPlayAnim::OnTimeLeftReachedZero`。`OnStop` 按回调的 virtual gate 和内部状态标志决定是否 Pop FightingState。此订单本身没有 Push `HitRecoveryAvailability`。 | 一个 state order 自然到零、AI 条件 recovery action 被调度、订单停止和下一次防御选择之间的帧序未闭合。 |
| `m_bInverted` 默认 | PDB `UAIInfluenceNode` size72；`UAIInfluenceTest` size80 继承它；反射属性 metadata 有 `m_bInverted`；`InternalConstructor<UAIInfluenceTest>` RVA `0x1bf9870` 在 `object+0x48` 写零。该字段为基础 test 类继承字段，所以 `UAttackMemoryInfluenceTest` 的未序列化默认 inversion 为 false。 | PDB 输出的 FieldList 未直接显示成员表项；映射来自派生类尺寸、属性反射、基础类构造写入共同支持。没有运行时实例验证。 |

以上核验到的最强证据各自闭合单个代码分支；AI 是否在该许可或状态到期之后立即防御仍不确定。contextual-defense 选择仍需同时满足预测、有效候选、序列测试与概率/遍历结果，因此不能从“层 Push/Pop”或“state 结束”推出必然格挡。
