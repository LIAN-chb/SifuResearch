# 通用规则整理：交互结果、攻击效果与状态许可

批次20261029-通用状态规则-01。只针对当前本机匹配EXE/PDB；本批输出先在对话解释，不重写阅读篇。规则句用攻击方/受击方确定主语；玩家与敌人共享组件不代表输入/配置/AI对称。

## R01：防守结果限定效果判定路径

直接证据：logs/system-recovery/UHitComponent__ComputeImpactType-0x1a51f10.asm.txt，函数RVA0x1a51f10。inventory/followup-hitted-type-layouts.json确认FImpactResult+0x1e=m_eGuardType，EGuardType None0/Guard1/Deflect2；+0xbf=m_bAvoidDizzy。

0x1a51fbb–0x1a51fcd把AvoidDizzy布尔转为预置结果0(Hit)或7(Dizzy)。0x1a51fd1判断GuardType；None走0x1a51ff3起后续，非None只GetAttackPropertyLevel然后直接跳0x1a521d6，跳过0x1a52103–0x1a521d3的效果等级比较和优先级选择。因此格挡/弹开时不能直接套攻击基础推开等级与对手抗性来保证Push。特定预置结果/后续反馈仍存在，不能夸成所有防御下都没有任何效果。

GenerateImpact先按GuardType调用FHitBox::GetHitImpact（0x1a5a9d7–0x1a5aa0a），使普通命中/Guard/Deflect采用不同FHitImpact；相关MakeAppliedImpact和架势反馈另读各自参数。后续破架势/反击反馈可另产生Impact，不与原命中路径混为一项。普通格挡仍有位置退让、伤害/架势、动画等，不等于推开FightingState。

## R02：当前状态参与双方效果选择，数值比较只是必要环节

ComputeImpactType 0x1a51fa1读取受击方HighestActiveFightingState；FHitboxDataRow::GetAttackPropertyLevel可按受击方状态选攻击侧覆写，不只改变受击方抗性。0x1a52103–0x1a52133中三个等级只有严格大于对应抗性才设候选bit。候选后按Push、KnockDown、Dizzy先后选择，仍有当前Dizzy、禁止叠加与特殊可用量等判断。

另外0x1a51fa9–0x1a51fb8在本击GuardBreak=true且AlreadyGuardBroken=false时临时用StructureBroken(7)行做抗性比较，不要求该持久状态已经推入。这是事件中间结果先影响判定的分支。故不能将‘攻击等级>抗性’简写为一定进入某状态，也不能无条件在当前状态保留/刷新。

## R03：状态剩余时间也可反过来改变本次命中类型

ComputeImpactType 0x1a52200–0x1a52233：选出KnockDown/Push/Dizzy后，若该次AttackPropertyLevel启用m_bKeepCurrentStateDuration(+0x15)，查询对应状态；状态存在、剩余时间小于m_fKeepCurrentStateThresold(+0x18)且不是无限状态时，将本次结果降为Hit。若剩余时间>=阈值或状态标记为无限，则该降级不发生。

这是命中类型筛选阶段的条件，不只是PushFightingState中重新算秒数。字段名‘保留时长’不足以解释其全部作用。上轮LowKick_HB01/RushSweep_HB01针对KnockedDown的Map覆写keep=true,threshold2实例仅作配置佐证；通则不绑定具体扫击。

## R04：动作限制的存续与普通受击处理分开

复用E20/E23：Dizzy Reaction引用GenericNone，经PushFightingState建立BasicGameplay priority1上下文并SET掩码。NPC IsAvailable消费首个上下文，四防御动作false→防御评估退出。Pop该状态触发所存回调回收对应上下文；不保证所有其他限制消失，也不保证AI立刻防御。

普通Hitted计时到零且恢复条件通过时加入恢复层并广播；订阅到AI回调后，AI自身不再IsStun且目标攻击信息满足条件，可重新评估防御。但目标订单/许可变化还有独立入口，不存在已证明的全局‘timer>0就禁止一切防御’规则。

## 未解边界

- 防守判定内部与攻击命中、伤害应用、状态回调的全部实际帧顺序尚未穷尽；本批时序图画因果关系，不伪装精确时间。
- 新状态/重复状态的计时及累计量更新由并行state底稿核，OnDamage/OnHit事件身份由count底稿核。
- 动作可选、输入可接受、AI选中、请求执行和最终格挡成功是不同事件，不合并写‘可以防御’。

R03复核修订：BPF_GetFightingStateTimeLeft第三输出是infinite，不是paused；此前按上下文猜成暂停已撤回。暂停只可能经Tick影响elapsed，不能作为本函数直接豁免条件。直接wrapper RVA0x194ffa0见logs/rules-state-update-20261029/。
## R05：事件顺序决定累计值属于哪份状态

`UHitComponent::ApplyImpact` RVA `0x1A46D90` 中已接通的一条普通生命伤害路径，依次执行：伤害闭包（`0x1A47165`）→ `UpdateFightingStateFromImpact`（`0x1A47C7F`）→ 目标 `OnHitDetection` 广播（`0x1A484C8`）。伤害闭包经 `UCharacterHealthComponent::InternalApplyDamage` 调基类，再广播初始化时已绑定到 `UDefenseComponent::OnDamage` 的委托；命中通知绑定到 `OnHit`。

这不是“每拳固定增加两次”：伤害通知更新当时的旧状态；中间处理可能移除、重建或更换状态；命中通知更新随后实际存在的状态。只有相关分支保留／转移了累计数据，两种来源才可能叠到同一份累计记录。回调是否派发仍受伤害路径前提限制。

`OnDamage` 与 `OnHit` 有各自更新条件，攻击名归组只在后者判断，并非全局去重。精确字段、绑定、派生类中间层与缺口见 `notes/20261029-rules-hit-count.md`。源汇编见 `logs/system-recovery/UHitComponent__ApplyImpact-0x1a46d90.asm.txt`，补充清单见 `inventory/rules-20261029-count-disassembly.json`。

## R06：重复受击要分别问“时间怎样变”和“累计怎样变”

`UpdateFightingStateFromImpact` / `ApplyFightingStateFromImpact` 没有一个对所有状态统一的刷新操作。部分普通 Dizzy + Hit 分支将旧累计命中、累计伤害及子状态带入新建状态；KnockedDown 的特定分支则只带入旧累计次数，不能推广为整份记录保留。SuperDizzy 具有单独子状态／反应配置，不能套普通 Dizzy 限额。

新元素 elapsed 从零开始，不等于总受控时间必定从完整初始值开始：duration 可能来自动画、攻击覆写、旧剩余时间、目标反应或特殊子状态分支。计算 duration 与决定累计字段继承是两组决策。确切分支和未确认部分见 `notes/20261029-rules-state-update.md`，新证据清单见 `inventory/rules-state-update-20261029-disassembly.json`。

## R07：持续状态有自动退出检查；退出与能实际防御仍是两件事

`UDefenseComponent::TickComponent` RVA `0x196A130` 对有限且未暂停的状态增加 elapsed，检查 elapsed > duration、启用时的累计伤害 > 上限、启用时的累计命中 >= 上限，任一成立就移除该元素。无限和暂停会跳过这整段自动检查，不只是跳过时间累加。其他显式移除路径不因此失效。

移除状态会回收其拥有的动作许可上下文，但其他许可限制、当前动作执行限制及 AI 选择仍须成立。因此不能从“眩晕结束”直接跳到“敌人本帧必格挡”，也不能把普通 Hitted 动作计时当作所有受控状态的统一禁防倒计时。源汇编：`logs/stun-ai-state/UDefenseComponent__TickComponent-0x196a130.asm.txt`。许可与 AI 接线复用 E20/E23；本批未证明普通受击期间的所有防御执行门。

## 面向对话的完整讲述

一次交互先确定玩家攻击面对的是普通命中，还是敌人的防守结果。只有在相应结算路径中，才比较攻击效果和敌人当前状态所对应的抗性；足以推开不等于能穿过一次已经成立的格挡。敌人当前状态还可能同时改变攻击采用的效果配置与敌人采用的抗性。

结算之后，系统按结果更新敌人的受控状态。已核对的眩晕许可配置会禁止敌人格挡、招架及躲避；只要这份限制仍生效，玩家追击不一定要紧贴上一段普通受击动作的恢复点。普通受击动作、持续眩晕及动作许可应分开识别，不能只凭角色在播放受击动画判断能否防御。

玩家下一击到来时，系统会依据敌人此刻的状态重新判定；命中并不保证把完整受控时长重新发一遍。系统可能保留剩余时间、换用其他时长、带走旧累计记录，或只继承其中一部分。部分配置还会在旧状态剩余时间过短时，把本来候选的推开／击倒／眩晕改成普通命中。

在攻击之间，状态更新检查时间和已启用累计上限。符合退出条件时，该状态和其拥有的限制被移除。敌人随后只是可能重新获得某项动作许可；AI 仍须判断这次来袭、选择防御，并满足执行条件。玩家与敌人的逻辑还会交叉：敌人当前状态／订单可被玩家的招式条件查询，影响玩家能选到哪种起手；双方不应被视作互不相干的两套说明。

这条链已能解释通用职责与条件分工；还不能据此声称所有普通连续攻击都会在固定拳数后被格挡。下一项必要取证是普通 Hitted 期间，防御评估结果如何变成实际执行，以及动作／许可变化何时让执行门通过。
