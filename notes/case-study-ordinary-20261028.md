# 普通受击案例：根线程证据复核与边界

批次20261028-受击案例-03；静态，本机Epic EXE SHA256 a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254，PDB fdd64e0f-b9ed-4479-8fd8-efe0038b919d age1。

## E23：普通硬直结束能引发防御重评估

1. 复核logs/system-recovery/OrderHitted__OnUpdate-0x1ae44d0.asm.txt，timer<=0且handle==-1、HittedDB及recovery layer存在，动画剩余>0、nonlethal、FHittedAnimContainer.m_bInterruptible=true且m_bInterruptAnimationOnEnd=false，才在0x1ae4751–0x1ae47b1生成/Push层并Broadcast。容器位于FNetOrderStructHitted+0x720，两个bool位于+0x1a/+0x1b，所以全结构+0x73a/+0x73b。类型来源inventory/followup-hitted-type-layouts.json，fields而非members。
2. 相同类型清单确认UHitComponent+0x108=OnIsStunChanged；OrderBase+0xca=m_eOrderState，EOrderState Starting=1。OrderHitted::IsStunOrder返回Starting或HitTimeLeft>0。所有active stun订单的聚合与回调分支见notes/case-study-defense-20261028.md。
3. 新定位订阅：scripts/case_find_xrefs.py扫描.text的E8/E9/RIP-relative LEA模式只生成候选，inventory/case-xrefs.json保存候选与EXE/脚本哈希。候选RVA0x18b818c位于UAIFightingComponent::InternalBeginPlay，按PDB边界反汇编到logs/case-defense-events/UAIFightingComponent__InternalBeginPlay-0x18b7e30.asm.txt。
4. 0x18b8177从owner+0x1328读HitComponent；0x18b818c取OnIsStunChanged函数指针；0x18b81a3把委托地址推进+0x108；0x18b81af r8=rdi（本AI对象），0x18b81b2 AddUObject。结合函数前段r15=owner与rdi=this核对。dumpbin AddUObject模板显示AFightingPlayerController是ICF别名，不代表绑定玩家Controller；实际函数指针、对象寄存器和字段明确。
5. 回调logs/counter-punish/UAIFightingComponent__OnIsStunChanged-0x18bc520.asm.txt，0x18bc563读取AI owner自己HitComponent并IsStun，false才走目标查询；0x18bc5be从tracked target（玩家）+0x1308读取AttackComponent，再比较+0xbf1<=1并在0x18bc5db UpdateDefenseNeed。这一字节业务名称本批未知，不写作AI handler字段。
6. 所以已接通“特定普通Hitted恢复分支→通知→敌人重新评估玩家攻击”的条件链。它不证明单一全局anti-infinite计数器，也不证明计时前不能防御。

## E24：反证过强的‘计时前全禁防’叙述

- 原Hitted服务GenericAll不移除Guard/Parry/Avoid/Dodge，这是已有配置反证；仅存在AIHittedRecovery不能推出之前四防御必false。
- logs/case-defense-events/UAIFightingComponent__OnTargetOrderStateChangedInternal-0x18bfb30.asm.txt 0x18bfcd1有另一UpdateDefenseNeed入口：需目标订单base type0/0x28、当前AI action可取消、订单state2等条件；本函数没有本方IsStun/HitTimeLeft判断。0x28的业务枚举未在本批核，不补名。
- logs/case-defense-events/FAIDefenseHandler__OnAvailabilityChanged-0x18ba4a0.asm.txt尾跳UpdateDefenseNeed；其他间接调用未穷尽。
- logs/case-movement/UFightingMovementComponent__IsAvailable-0x1ab1820.asm.txt，只有movementmode3才查额外数组1410/1418，其余true。因此该函数不是普通地面受击的单独禁防证据；mode3名称本批未查，不补名称。
- ABaseCharacter::IsAvailable按r8bool选择两个mask缓存，NPC仍读BasicGameplay第一上下文；CanApply请求对IsAvailable传true而need查询传false。两缓存的精确预测语义未解，不将mask近似当成相同运行时值。

## C01/C02固定数据与修订

inventory/player-combo-graphs.json仅选asset=Sifu/Content/DB/_MainChar/Combos/MainChar_ComboTree.uasset。N44槽0/1 Jab_FR、2/3 Hook_BL；N45槽0/1 ThroatPlexus_DoubleHit_FR、2/3 GroinHead_DoubleHit_BL。N44 L→45，H→47。N44及45存在1067字节未解码ConditionalAttacks，不能保证运行时基础选择。

exports/hit-impact-values.csv里Jab_HB01普通stun8，ThroatPlexus_HB01为5、HB02为15；源表MainChar_HitBoxData。player graph与源包uasset/uexp SHA在inventory/case-study-documents.json及原graph中记录。只核当前选用输入，未重复全量解析。

早期agent暂误读其他同名节点导致N44四槽全FR，复核精确asset/nodes[44]后已撤回，最终notes/case-study-inputs-20261028.md正确；未传播到阅读页。不同姿态不能混算。

## 最小未解问题与续接

首例尚未构成实战‘紧接必连/延迟必防’结论。下一步从OnTargetOrderStateChangedInternal→UpdateDefenseNeed→ComputeDefenseRequest/ApplyDefenseRequest→候选节点的输入动作(+0x298)、GetAssociatedTactic战术值(+0x2a0，本批vtable已直接核对)以及Guard::Apply→HandleGuard后的订单启动与动作调度开始，寻找Hitted期间实际限制、预测/当前mask的差别，以及受击时已有防御请求的取消。先检实际调用消费者再查新资产，不再大范围枚举配置。

第二步对齐C01时间轴：MainChar_Jab_FR与MainChar_ThroatPlexus_DoubleHit_FR的启动、WantedBuildup、帧窗口、播放速率、冻结、被选受击容器；不能用不同动画14/22帧号相减。完整窗口和条件覆写不足时记录具体观测值，不编造可连结果。

停止边界：不运行游戏。最小运行时方案在案例篇，仅作为后续授权观测设计。

## E25：实际动作期韧性样本

notes/case-study-resilience-20261028.md及inventory/case-resilience-notifies-20261028.json补齐普通/进阶Grunt KneeStrike/SpinKick组合引用、动画服务默认对象及通知窗口。服务m_iBonus=4/2，配置动画时间窗0.001660836–0.669203639s和0.116411872–0.392183691s。实际当前韧性仍缺，不能把敌人自身攻击的Medium/Strong当成玩家攻击的比较值。动作通知窗口不等于墙钟执行时长。C07已据此从仅有规则提升为实际动作配置案例，仍未实战。
