from pathlib import Path
import json,hashlib,datetime
R=Path(r'E:\ProgrameFiles\SifuResearch')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
exe=Path(r'E:\Games_Little\Epic\Sifu\Sifu\Binaries\Win64\Sifu-Win64-Shipping.exe')
pdb=json.loads((R/'inventory/pdb_overview.json').read_text(encoding='utf-8'))
assert pdb['pdb_matches_exe'] and sha(exe)==pdb['exe_sha256']
old=json.loads((R/'inventory/stun-ai-defense-disassembly.json').read_text(encoding='utf-8'))
procs={x['name']:x for x in old['procedures']}
want=['FAIDefenseHandler::IsDefenseNeededInternal','FAIDefenseHandler::UpdateDefenseNeed','FAIDefenseHandler::CanApplyDefenseRequest','FAIDefenseHandler::ApplyDefenseRequest','UAIFightingComponent::OnIsStunChanged','FAIAttackHandler::OnIsStunChanged']
refs=[]
for name in want:
 x=procs[name];p=Path(x['file']); assert p.is_file() and sha(p)==x['assembly_sha256'];refs.append({'function':name,'rva':x['rva'],'file':str(p.relative_to(R)).replace('\\','/'),'sha256':x['assembly_sha256'],'source_manifest':'inventory/stun-ai-defense-disassembly.json'})
for name in ['UHitComponent::IsStun','OrderHitted::IsStunOrder','OrderHitted::OnUpdate']:
 pattern={'UHitComponent::IsStun':'callback-UHitComponent-IsStun.asm.txt','OrderHitted::IsStunOrder':'OrderHitted__IsStunOrder-0x19fdb50.asm.txt','OrderHitted::OnUpdate':'OrderHitted__OnUpdate-0x1ae44d0.asm.txt'}[name]
 cands=list((R/'logs').rglob(pattern))
 if not cands: raise FileNotFoundError(name)
 p=cands[0];rv={'UHitComponent::IsStun':'0x1a64340','OrderHitted::IsStunOrder':'0x19fdb50','OrderHitted::OnUpdate':'0x1ae44d0'}[name];refs.append({'function':name,'rva':rv,'file':str(p.relative_to(R)).replace('\\','/'),'sha256':sha(p),'source_manifest':'existing evidence; see referenced inventory group'})
groups=[]
for n in ['case-defense-init-20261028-disassembly.json','case-defense-init2-20261028-disassembly.json']:
 p=R/'inventory'/n
 a=json.loads(p.read_text(encoding='utf-8')); assert a['exe_sha256']==pdb['exe_sha256']
 groups.append({'manifest':str(p.relative_to(R)).replace('\\','/'),'manifest_sha256':sha(p),'procedures':[{'name':x['name'],'rva':x['rva'],'status':x['status'],'assembly':str(Path(x['file']).relative_to(R)).replace('\\','/'),'sha256':x['assembly_sha256']} for x in a['procedures']]})
rows=[
 {'question':'Does IsDefenseNeededInternal gate on the AI enemy being stunned or having Hitted active?','finding':'No direct such predicate in this function. It validates a tracked target actor/attack component, compares target attack-info snapshots, and calls ComputeIncomingAttackPrediction.','evidence':'FAIDefenseHandler::IsDefenseNeededInternal RVA 0x18b8fc0; existing manifest and assembly.'},
 {'question':'What does UHitComponent::IsStun inspect?','finding':'It enumerates active orders on the AI owner and invokes their virtual IsStunOrder predicate.','evidence':'UHitComponent::IsStun RVA 0x1a64340; owner HitComponent at AFightingCharacter +0x1328 in UAIFightingComponent::OnIsStunChanged.'},
 {'question':'When is an active Hitted order considered a stun order?','finding':'OrderHitted::IsStunOrder returns true if OrderBase m_eOrderState (+0xCA) equals Starting (1), or m_fHitTimeLeft (+0x51C) is strictly greater than zero. State Starting is confirmed by matching PDB enum layout.','evidence':'OrderHitted::IsStunOrder RVA 0x19fdb50; inventory/followup-hitted-type-layouts.json.'},
 {'question':'What happens when AI-owner stun changes?','finding':'UAIFightingComponent::OnIsStunChanged checks the owning AI character hit component. If true, this callback skips its UpdateDefenseNeed route and notifies the AI attack handler. If false, then when tracked target and its AttackComponent are valid and the target AttackComponent +0xBF1 byte is <=1, it calls FAIDefenseHandler::UpdateDefenseNeed. The field type/meaning is unresolved; it is not confirmed as an AI DefenseHandler state.','evidence':'UAIFightingComponent::OnIsStunChanged RVA 0x18bc520; FAIAttackHandler::OnIsStunChanged RVA 0x1893b10.'},
 {'question':'When does Hitted add AIHittedRecovery and emit the changed notification?','finding':'After the timer is <=0, OnUpdate requires a valid layer resource/handle slot, animation time remaining >0, m_bInterruptAnimationOnEnd (+0x73B)=false, nonlethal impact, and m_bInterruptible (+0x73A)=true. It generates and pushes the AIHittedRecovery layer, stores the returned handle, then broadcasts UHitComponent::OnIsStunChanged at +0x108. PDB maps the net struct bytes to FHittedAnimContainer members.','evidence':'OrderHitted::OnUpdate RVA 0x1ae44d0, assembly 0x1ae46e4–0x1ae47b1; inventory/followup-hitted-type-layouts.json.'},
 {'question':'Does this prove AI cannot defend until the Hitted timer expires?','finding':'It proves one event route: the IsStunChanged notification triggered by this recovery push re-evaluates defense after the AI owner IsStun predicate becomes false. It does not prove that no other attack/behavior-tree event can call UpdateDefenseNeed earlier, or that an already queued defense cannot execute. GenericAll Hitted availability mask by itself allows Guard/Parry/Dodge/Avoid.','evidence':'UpdateDefenseNeed action-availability calls plus hitted-services-followup.md mask decoding.'},
 {'question':'What additional gate is in CanApplyDefenseRequest?','finding':'After defense need/candidate generation, this checks request-associated weak-object/action state and asks the AI owner character IsAvailable for a mapped action in a context. This is execution-application validation, not an explicit Hitted timer/IsStun check in the disassembly. The request object vtable +0x298 return byte is passed into the AI owner vtable +0x988 availability check with context 13; the requested action mapping remains unresolved.','evidence':'FAIDefenseHandler::CanApplyDefenseRequest RVA 0x18ab9c0; no IsStun, OrderHitted or hit-time access in function.'},
 {'question':'Is stun-change delegate subscription fully located?','finding':'Yes. UAIFightingComponent::InternalBeginPlay binds AFightingCharacter+0x1328 HitComponent delegate +0x108 to this UAIFightingComponent instance OnIsStunChanged via AddUObject.','evidence':'UAIFightingComponent::InternalBeginPlay RVA 0x18b7e30, 0x18b8177–0x18b81b2; inventory/case-defense-events-disassembly.json.'},
 {'question':'What does AI owner stun do to its own attack combo?','finding':'A separate path: OnIsStunChanged(true) forwards to FAIAttackHandler; that handler only calls EndCombo(reason=10 IsStun) if its configured Blackboard ComboEndReason is non-invalid/nonzero. This stops/ends a combo conditionally; it is not proof of a defense block.','evidence':'FAIAttackHandler::OnIsStunChanged RVA 0x1893b10; notes/counter-punish.md.'},
]
report={'batch':'20261028-case-defense-gate','updated_at':datetime.datetime.now().astimezone().isoformat(),'status':'static partial; no runtime','question':'For an enemy under ordinary Hitted, what gates AI defense re-evaluation and application?','sample_actor':'AI enemy (Grunt intended; native function paths are general and Grunt asset specialization is not runtime-proven here).','build':{'exe_sha256':pdb['exe_sha256'],'pdb_guid':pdb['pdb_info']['guid'],'pdb_age':pdb['pdb_info']['age'],'pdb_matches_exe':True},'existing_primary_evidence':refs,'new_disassembly_groups':groups,'findings':rows,'limitations':['No runtime trigger observed.','No proof other events cannot call UpdateDefenseNeed while Hitted predicate remains true.','No proof that queued/active defense execution is cancelled solely by Hitted.','Recovery-layer boolean gates were read from native code and PDB offsets; user-facing semantics are limited to mapped interruptibility fields.','OnTargetOrderStateChangedInternal is a distinct UpdateDefenseNeed route with no explicit AI-owner IsStun/Hitted-timer test; actual occurrence during Hitted is not runtime-verified.'],'unmodified':['game files','save files','Obsidian vault','LIAN project']}
out=R/'inventory/case-defense-20261028.json';out.write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
# save a concise evidence note; primary code blocks and sources remain in original hashed logs/manifests.
note='''# 普通受击结束与敌人防御重新评估：静态案例底稿

- 批次：`20261028-case-defense-gate`
- 范围：本机 Epic《师父》普通受击期间，AI 敌人何时重新评估防御。仅静态分析，未运行游戏。
- 构建：EXE SHA256 `'''+pdb['exe_sha256']+'''`；PDB `'''+pdb['pdb_info']['guid']+'''` / age '''+str(pdb['pdb_info']['age'])+'''
- 结构化记录：`inventory/case-defense-20261028.json`
- 生成新反汇编：`scripts/disassemble_research.py --group case-defense-init-20261028 ...` 与 `--group case-defense-init2-20261028 ...`；PDB/EXE 一致。主要函数直接复用原哈希清单，不重复生成旧共享manifest。

## 直接结论

有一条静态事件链能解释“普通受击硬直结束后，AI何时重新跑防御查询”：

**敌人 Hitted 订单倒计时 → 满足恢复层条件 → 给敌人加入 `AIHittedRecovery` 动作层 → 广播敌人自己的 `UHitComponent::OnIsStunChanged` → 已绑定的回调查询敌人当前是否仍有“受击中”订单 → 结果为否时，在目标攻击组件字段及防御 handler 条件成立下调用 `FAIDefenseHandler::UpdateDefenseNeed`。**

这里是敌人的防御重新评估入口，不能与玩家受击混为一谈。

## 逐步证据

| 步骤 | 执行对象与判断 | 代码／配置证据 | 结论及边界 |
|---|---|---|---|
| 1 | `OrderHitted::OnUpdate` 递减敌人自身 `m_fHitTimeLeft`；到零后检查是否能开放恢复动作层 | RVA `0x1ae44d0`，`+0x51C`倒计时、`0x1ae46e4–0x1ae4709` | “敌人硬直”这里指订单内部剩余计时，不是动画剩余时长 |
| 2 | 敌人受击数据必须允许恢复层路径：剩余动画时间>0、`m_bInterruptAnimationOnEnd(+0x73B)=false`、非致命命中、`m_bInterruptible(+0x73A)=true` | 同函数 `0x1ae472c–0x1ae4751`；偏移由 `FNetOrderStructHitted.m_HittedAnimContainer` 对应类型布局确认 | 这是添加层的实际代码条件；原生含义优先用两个布尔字段名表达，其他偏移判断不补造中文含义 |
| 3 | 条件满足后敌人取得 `AIHittedRecovery` 可用性层；订单保存返回句柄，再广播自己的 `OnIsStunChanged` | 同函数 `0x1ae4751–0x1ae47b1`；`UHitComponent +0x108` 即 `OnIsStunChanged` | 许可层从此分支被加入；配置本身不能保证其它许可／移动条件通过，也不保证 AI 选中防御 |
| 4 | `UHitComponent::IsStun` 在敌人自己的活动订单中枚举并调用 `IsStunOrder` | RVA `0x1a64340`；读取 AI owner 的 `UHitComponent` 见 `UAIFightingComponent::OnIsStunChanged` `0x18bc520` | 不是查询玩家是否硬直，也不是只读一个布尔值 |
| 5 | Hitted 的“仍受击中”谓词：`OrderBase::m_eOrderState(+0xCA)==Starting(1)` **或** `OrderHitted::m_fHitTimeLeft(+0x51C)>0` | `OrderHitted::IsStunOrder` RVA `0x19fdb50`；`inventory/followup-hitted-type-layouts.json` 中 OrderBase 字段和匹配枚举 | `+0xCA` 是订单状态，不是名为 `m_bIsStunOrder` 的旗标；状态刚 Starting 或剩余计时大于0时谓词为真 |
| 6 | 敌人的 `OnIsStunChanged` 回调在自身谓词为真时不走本回调里的防御重查；谓词为假时，若追踪目标及其 `AttackComponent` 有效且该**目标攻击组件** `+0xBF1` 字段不大于1，才调用 `UpdateDefenseNeed` | RVA `0x18bc520`，`0x18bc563–0x18bc5db` | `+0xBF1` 类型／语义未映射；它不是已确认的敌人防御 handler 状态。该回调受敌人自身 `IsStun()` 控制，但不是唯一已知重评估入口 |
| 7 | 更新需求时再检测敌人最高战斗状态、情境防御、敌人自身是否正准备攻击，并查询 Guard/Parry/Avoid/Dodge 是否可用；候选成立后 `CanApplyDefenseRequest` 再检查请求动作状态／可用性 | `UpdateDefenseNeed 0x18c9e50`、`CanApplyDefenseRequest 0x18ab9c0` | 当前函数里没有 Hitted 订单ID、`m_fHitTimeLeft` 或 `IsStun` 检查；`CanApply` 从请求对象虚表`+0x298`取字节并传入角色虚表`+0x988`可用性判断，动作语义尚未映射 |

### 目标订单状态变化的另一条防御需求更新入口

`UAIFightingComponent::OnTargetOrderStateChangedInternal`（RVA `0x18bfb30`）也能调用 `FAIDefenseHandler::UpdateDefenseNeed`。该函数没有读敌人自己的 `IsStun()` 或 Hitted timer。其调用分支要求订单 `GetBaseType` 返回 `0` 或 `0x28`、相关当前动作可取消、订单 `m_eOrderState(+0xCA)==2`，并且 DefenseHandler `+0x100` 字节为 4。各枚举／字节的语义本批未映射；也没有运行时证据证明该事件会在敌人 Hitted 时发生。它说明 `OnIsStunChanged` 不是唯一静态入口，调用更新不等于实际格挡。

## 为什么“硬直”不只是动画

有两件事同时发生，但代码把它们分开处理：

| 对象 | 负责什么 | 时序证据 |
|---|---|---|
| `OrderPlayAnim` 动画计时 | 维护受击动画的播放／剩余时长 | `OrderHitted::OnUpdate` 先调用父类 `OrderPlayAnim::OnUpdate`，之后再扣自己的 `m_fHitTimeLeft` |
| Hitted 内部受控计时 | 决定是否可进入恢复许可分支，并参与 `IsStunOrder` 谓词 | timer可先到零；若动画仍有剩余时间且其它条件满足，会先加入恢复层并广播通知 |
| AI防御重新评估 | 事件回调检查敌人自身 `IsStun()`，然后可能重查玩家下一次攻击 | 在条件通过后调用 `UpdateDefenseNeed`，不是从动画结束通知直接推出 |

因此能确认：**受击硬直计时结束可以成为敌人重新评估防御的触发点，即使受击动画还有剩余时间。** 这条逻辑比“受击单被取消所以动画切换”更接近连续压制问题。

## 防御许可不等于“直到计时结束才有防御能力”

`HittedAvailabilityOrderService` 的 `GenericAll` 掩码允许 Guard、Parry、Dodge、Avoid 等动作。恢复层添加是上面的明确事件，但 `OnTargetOrderStateChangedInternal` 有独立的 `UpdateDefenseNeed` 调用条件，且静态函数没有读敌人 `IsStun()`。所以本批只能确认：`OnIsStunChanged` 路由在敌人 `IsStun()` 为真时跳过该次防御重查；变假后可按目标攻击组件字段条件重查。目标订单事件另有更新入口，静态函数里没有敌人 `IsStun()` 门。不能据此断言其它事件都被挡住，也不能证明此前的防御请求必被撤销或动画播放已停止。

另一个容易混淆的代码路径是 AI 自己的连段：`UAIFightingComponent::OnIsStunChanged(true)` 通知 `FAIAttackHandler`；若其配置的 Blackboard ComboEndReason 非无效才以 IsStun(10) 结束该敌人的连段。它解释“敌人被打断时可能停止自己的进攻连段”，不是“敌人因此无法对玩家防御”。

### 防御请求校验与 Guard 节点执行：不是同一条门槛

`UpdateDefenseNeed` 的动作候选查询传 `r8=false`／context 13，`CanApplyDefenseRequest` 复核传 `r8=true`／context 13。NPC `ABaseCharacter::IsAvailable` 分别读取缓存 `+0x38/+0x40` 与 `+0x18/+0x20`；字段语义未解析。r8=true时函数开头计算了加 `SCGameSettings+0x710` 的同步 tick，但 NPC 分支不消费该 tick，不能把它称为敌人实际执行等待时间。

`ApplyDefenseRequest` 对请求对象调用 vtable `+0x2A0`，返回字节随后写入 Blackboard enum；`ComputeDefenseRequest` 用同一返回值决定候选是否继续。匹配构建的 `.rdata` vtable 对齐 PDB 符号后，`+0x298` 是 `GetInputAction`，相邻 `+0x2A0` 是 `GetAssociatedTactic`（Guard/Avoid 实现存在函数折叠）。该槽读出策略标签，不是 Apply 执行调用。Guard 的最近执行消费者是 `UDefenseInfluenceNodeGuard::Apply`：基类 Apply 成功后调用 `AFightingCharacter::HandleGuard`。这条路径未见显式 AI-owner `IsStun()` 或 `IsAvailable`/delay 检查；`HandleGuard` 可见订单运行状态、GuardBroken 与组件有效性判断。此发现只覆盖该执行入口。

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
| `CanApplyDefenseRequest` 请求动作映射 | 该函数把请求附带动作值送入 enemy `IsAvailable`，未看到 stun字段读取；虚槽语义未由本批直接映射 | 结合 request/PDB类型及 AFightingCharacter vtable slot 提取解析 |
| 目标订单事件是否会在敌人仍Hitted时触发防御更新 | IsStunChanged路线于 true 时跳过；其它监听／Tick/BT调用者未做穷尽 | 先查 BT Task/动作可用性事件和 UpdateDefenseNeed xrefs，再决定是否要求运行时验证 |
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

初始化扫描新产物分别在 `inventory/case-defense-init-20261028-disassembly.json` 和 `inventory/case-defense-init2-20261028-disassembly.json`，原始反汇编分别位于 `logs/case-defense-init-20261028/` 与 `logs/case-defense-init2-20261028/`。所有结论绑定上述 EXE/PDB，未运行游戏。
'''
p=R/'notes/case-study-defense-20261028.md';p.write_text(note,encoding='utf-8',newline='\n')
print(json.dumps({'note':str(p),'manifest':str(out),'procedures_reused':len(refs),'new_groups':len(groups),'checks':['EXE SHA matches PDB overview','all reused assembly hashes match their original manifest','new disassembly manifests match the same EXE']},ensure_ascii=False))
