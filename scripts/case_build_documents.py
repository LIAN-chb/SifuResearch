"""Generate this batch's reader-facing case studies from reviewed local evidence.
Owns the new case pages and the integrated mechanism page; other pages get named sections only.
"""
from pathlib import Path
import json,hashlib,datetime,csv
R=Path(__file__).resolve().parents[1];V=R/'Sifu';B=R/'notes/vault-backups/20261028-cases-03';B.mkdir(parents=True,exist_ok=True);changed=[]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(rel,body):
 # Preserve the current integrated explanation when replaying this older batch.
 reader_sources={'01机制/连续受击与反击追击的系统链.md':'mechanism.md',
                 '02实现/连续受击与反击追击的系统链.md':'implementation.md'}
 if rel in reader_sources:
  current=R/'notes/reader-sources/20261029-state-spec'/reader_sources[rel]
  if not current.is_file(): current=R/'notes/reader-sources/20261029-rules'/reader_sources[rel]
  if current.is_file(): body=current.read_text(encoding='utf-8')
 p=V/rel
 if p.exists():
  backup=B/(sha(p)[:12]+'-'+p.name)
  if not backup.exists():backup.write_bytes(p.read_bytes())
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body.strip()+'\n',encoding='utf-8',newline='\n');changed.append(rel)
def section(s,t,b):
 mark='\n## '+t+'\n'
 if mark not in s:return s.rstrip()+mark+'\n'+b.strip()+'\n'
 a=s.index(mark);e=s.find('\n## ',a+len(mark));return s[:a]+mark+'\n'+b.strip()+'\n'+('' if e<0 else s[e:])
def update(rel,t,b):put(rel,section((V/rel).read_text(encoding='utf-8-sig'),t,b))
put('01机制/连续受击与反击追击的系统链.md','''# 连续受击与反击追击的系统链

[[00索引/首页|首页]] · [[01机制/受击与追击案例|先看具体案例]] · [[02实现/连续受击与反击追击的系统链|简要实现与证据]]

**核心问题仍是：玩家连续攻击时，敌人在什么条件下可以防住下一击？** 目前已接通普通硬直计时引发防御重新评估的一条路径，以及眩晕阻止敌人防御的路径；尚未证明某套玩家连招在普通受击下必连或必断。

本文固定玩家出招、敌人受击。玩家自己受击不在此混讲。“受击处理”是内部OrderHitted对象，管理计时、动画与相关逻辑，不只是播放动画。

## 先分清三个问题

| 判断 | 看什么 | 不能替代的判断 |
|---|---|---|
| 玩家可以出招吗 | 输入、姿态、技能与动作衔接窗口 | 出得来不保证打得中 |
| 玩家下一击能命中吗 | 距离、朝向、位移、命中时刻与敌人防御 | 一次命中不保证后续都能命中 |
| 玩家能连续压制吗 | 敌人是否能在下一击前恢复并有效应对 | 输入图有连线不等于不可防御的连续命中 |

## 玩家这一击命中后，有哪些不同处理

| 分支 | 判断对象与结果 | 如何影响后续追击 | 当前边界 |
|---|---|---|---|
| 韧性抵抗 | 敌人当前韧性严格高于本次攻击采用的强度值，且相关条件通过 | 非致命、未破防的对应应用分支可绕过正常受击处理；敌人可能没有按普通挨打方式被打断 | 不能说免伤；膝击+4／旋踢+2与动画通知已定位；实际命中结果仍需核 |
| 普通受击 | 本次命中进入正常受击处理 | 敌人有独立硬直计时；到期可能开放恢复动作并重新评估防御 | 不是直接套眩晕的3秒或命中上限 |
| 推开／击倒／眩晕 | 玩家攻击的对应等级与敌人当前状态抗性等条件比较通过 | 敌人反应、位置和后续状态改变，追击条件也改变 | 不同效果不能统一翻译成更长的普通硬直；还受状态优先顺序等条件影响 |
| 架势崩溃等特殊反馈 | 敌人架势与命中／招架反馈满足对应条件 | 进入另外的受控与恢复路径 | 与普通招架、普通受击分别解释 |

这些分支是关键处理的概览，不是全部代码判断的执行顺序。精确条件回查实现篇；具体数值见[[03配置/受击案例配置对照]]。

## 普通硬直怎样走向防御重新评估

下面只展开“已经进入普通受击处理”的路径。框内的“敌人”始终是挨打的杂兵。

```mermaid
flowchart TD
  A[玩家命中敌人并进入普通受击处理] --> B[建立敌人本次硬直计时]
  B --> C{敌人硬直计时仍大于零吗}
  C -->|是| D[该受击处理仍被识别为硬直中]
  D --> E{玩家下一击先命中吗}
  E -->|是 且仍走正常受击| F[结算新命中并替换符合条件的旧受击处理]
  F --> B
  E -->|没有新命中| C
  C -->|否| G{动画仍有剩余且允许提前恢复等条件通过吗}
  G -->|是| H[加入敌人恢复动作许可并广播硬直变化]
  H --> I{敌人还有其他被识别为硬直的处理吗}
  I -->|没有 且玩家攻击信息条件通过| J[敌人重新评估对玩家攻击的防御]
  I -->|还有| K[这条回调不触发防御重评估]
  G -->|否| L[不走本次提前恢复分支 按停止或其他路径继续]
  J --> M{敌人动作许可和AI候选条件通过吗}
  M -->|是| N[继续验证和调度防御请求]
  M -->|否| O[不由这次评估执行防御]
  N -. 具体帧序和执行结果待确认 .-> P[玩家下一击命中或被防住]
```

| 读图时容易误解的点 | 正确理解 |
|---|---|
| 硬直结束是否必须等动画播完 | 不必须；提前恢复分支明确要求动画还有剩余时间 |
| “提前恢复条件”是什么 | 硬直计时≤0、尚未添加该恢复层、恢复层资源存在、命中非致命、受击动画容器允许中断且没有要求到期中断动画等；不满足时不能强行走同一箭头 |
| 第二击怎样影响第一击 | 正常无前置请求会安排取消旧动画绑定处理、排入新处理；旧恢复层与服务随生命周期回收，新处理按本次结果计时。不是无条件累加时长 |
| 为什么能重新评估防御 | 初始化确实订阅了敌人自身的硬直变化通知；回调会检查敌人是否仍硬直，并读取玩家的攻击信息，再条件性调用防御评估 |
| 能否据此说硬直未结束绝不防御 | 不能。玩家攻击状态变化、动作许可变化也有防御评估入口；普通受击下所有入口的共同阻断尚未闭合 |
| 恢复许可是否等于立刻格挡 | 不是。还要预测玩家来袭、检查敌人动作许可与攻击准备状态、筛选候选并验证执行 |

证据：实现E23及[[02实现/受击与追击案例]]。这是一条已接通的条件路径，不能冒充“整个普通连打脱离原因已经解决”。

## 为什么眩晕后的追击要单独解释

| 环节 | 普通受击 | 敌人已经进入当前Grunt配置的眩晕 |
|---|---|---|
| 核心控制 | 普通受击处理的计时、恢复与相关动作条件 | 持续眩晕状态及它推入的高优先级动作限制 |
| 已确认的防御影响 | 硬直结束可触发防御重新评估；未证明所有提前评估都被禁止 | 有效眩晕上下文只保留少数非防御动作，AI检查的格挡、招架、躲避四项均不可用 |
| 后续命中影响 | 本次结算可产生新的受击处理 | 同时还可能更新眩晕的时间／累计伤害／归组命中数等 |
| 机会结束 | 需核对计时、许可、来袭与AI执行的完整时序 | 状态被移除会回收该限制；敌人之后是否立刻防御仍需AI选择 |

因此，防御能力不是每次受击后从零创造；敌人已有防御系统，当前条件决定是否允许及是否触发。眩晕的禁止链较明确，普通硬直的所有防御入口还需补齐。其他同／更高优先上下文、具体变体覆写仍需核对。

## 招架与闪避不是同一个入口

| 玩家操作 | 敌人发生什么 | 必须分开的阶段 |
|---|---|---|
| 玩家成功闪避某些敌方招式 | 敌人可携带一段特殊反击判定配置；玩家及时反击命中后，才可能把敌人打入眩晕 | 闪避成功、反击命中、之后眩晕维持分别解释 |
| 玩家成功招架 | 敌人按来袭属性、架势和反馈条件分流；不保证直接眩晕 | 普通反馈、架势崩溃、专用眩晕反馈、玩家后续招式自身制造眩晕分别解释 |

当前三个实际敌方攻击行Hook／BaseballHook／Uppercut均保存DizzyOnParry=false、DizzyOnAvoid=true。不能用专用招架眩晕模板解释所有招架追击；运行时覆写仍需核对。逐例见[[01机制/受击与追击案例]]。

## 当前最重要的未解问题

1. 普通敌人正在硬直时，玩家下一招触发另一条防御评估入口后，哪个实际条件阻止或允许防御执行？
2. N44刺拳接N45双段攻击时，玩家各段实际命中相对敌人恢复处在什么时刻？需要补动作启动、播放速率、受击动画选择与条件覆写，不能直接相减两张表的帧号。
3. 由此才能判定：某次被防住是攻击间有空隙、累计条件改变，还是下一击没有产生同样的受控效果。

下一步先追第1项，再对齐第2项；案例中能确认的部分与未知分开写。保持静态研究，未进行实战窗口验证。
''')
put('01机制/受击与追击案例.md','''# 受击与追击案例

[[00索引/首页|首页]] · [[01机制/连续受击与反击追击的系统链|先看总流程]] · [[02实现/受击与追击案例|证据与执行位置]] · [[03配置/受击案例配置对照|案例配置]]

本文固定玩家攻击、敌人受击。例子用于解释具体条件，不把静态配置写成已经看到的实战结果。“能接”拆成能出招、能命中、能连续压制。以下均以本机Epic构建、普通难度目标、徒手Grunt_Base为基线；没有运行游戏核对实际关卡实例。变化项在各例单列。

## 案例总览

| 例子 | 要改变的条件 | 目前能回答什么 | 可连／不可连是否已确定 |
|---|---|---|---|
| C01 刺拳接双段轻击 | 玩家紧接或延迟输入 | 输入路径和敌人硬直结束重评估路径 | 尚不能判定整套连续压制 |
| C02 双段攻击中的前后命中 | 实际命中段及当前剩余硬直 | 后一击会重新计算受击处理，不只是接动画 | 没有固定首次被防住的段数 |
| C03 闪避Hook与StraightJab | 敌人来袭招式及反击延迟 | 哪个保存行允许闪避反击进入眩晕的特殊路径 | 只确认分流，不保证反击能命中 |
| C04 招架未破架势与破架势 | 敌人初始架势，使反馈是否触发崩溃不同 | 招架反馈入口不同，不能统一解释成普通眩晕 | 具体追击序列仍待判定 |
| C05 三连拳的前两段与末段 | 实际命中段 | 末段具备制造眩晕的基础等级，前两段没有同等级 | 候选已定位，不保证末段必眩晕 |
| C06 眩晕追击及退出 | 时间、累计伤害、归组计数、重新眩晕条件 | 眩晕期间防御许可受限；退出条件有多个 | 防御限制可解释，整套必连尚未验证 |
| C07 敌人顶住攻击 | 同一动作通知窗内／外 | KneeStrike加4、SpinKick加2及配置区间已解析 | 实际阈值与命中结果尚未闭合 |
| C08 推开与倒地对追击的影响 | 敌人当前状态／攻击效果 | 能解释特殊反应候选与普通硬直不同 | 位置与后续命中尚缺；倒地案例未闭合 |
| C09 普通与进阶杂兵 | 仅替换敌人配置 | 同入口下眩晕时长／上限有实际差异 | 不能直接换算可连拳数 |

## C01：玩家刺拳后紧接／延迟轻击

| 项目 | 固定内容 |
|---|---|
| 玩家操作 | 徒手图处于N44刺拳节点时再输入轻击L，图保存N44→N45。如何从当前战斗情境进入N44仍受起始节点和条件影响，不把任意两次L等同本例 |
| 实际动作 | 姿态槽0/1的基础选择：MainChar_Jab_FR→MainChar_ThroatPlexus_DoubleHit_FR；不混入槽2/3的勾拳与另一双段动作 |
| 命中段 | 刺拳段0 Jab_HB01；随后双段为ThroatPlexus_HB01／02 |
| 敌人 | 普通徒手杂兵，初始站立战斗状态，非眩晕／倒地／破架势；本次确实进入普通受击路径 |
| 对照 | A尽早输入后续轻击；B延迟输入，但仍须在允许出招的窗口内。延迟到不能出招是另一个问题 |

| 判断 | A紧接 | B延迟 | 不能提前得出的结论 |
|---|---|---|---|
| 玩家可以出招 | 图存在L转移，仍需动作窗口与条件覆写允许 | 同样需在窗口内 | 保存100%不等于任何时刻按L都生效 |
| 玩家可以命中 | 尚缺实际距离、姿态变化、启动与命中时序 | 同样缺这些条件 | 不把“按得快”直接等同命中 |
| 玩家可以连续压制 | 尚未证明 | 尚未证明 | 不能宣称A必连、B必被格挡 |

**决定问题的过程：**玩家刺拳命中→敌人建立普通受击计时→玩家准备下一招→敌人计时若先到零且恢复条件通过，会获得恢复层并发出通知→敌人不再被识别为硬直且玩家攻击信息符合条件时，AI重新评估防御。初始化订阅、通知与回调已接通。

这说明延迟可能让一次恢复评估发生在后续命中前；但“可能”不是本例已证实的结果。玩家下一招本身也会触发敌人另一条防御评估路径，目前尚未找到所有路径在普通硬直期间共享的禁止条件。

**本例停止位置：**不能诚实地给A／B写“必连／必断”。最小缺口是敌人普通硬直中的防御执行条件，以及两个玩家动作的实际命中间隔。见总流程图及实现C01。

## C02：同一双段攻击，第一段和第二段为什么不能当成一个硬直

| 项目 | 本例内容 |
|---|---|
| 玩家输入与动作 | 沿C01的N44后L进入N45，固定姿态槽0/1基础动作MainChar_ThroatPlexus_DoubleHit_FR |
| 两段配置 | 段0窗口[14,15]、普通硬直配置5帧；段1窗口[22,24]、普通硬直配置15帧；均为各自命中段 |
| 敌人情况 | 两段都确实打中、非破架势、无特殊反应或韧性抵抗，且正常无前置受击请求成立 |
| 已确认的变化 | 每次命中重新结算。后一次正常请求安排取消旧受击处理，建立新的处理与计时；旧恢复层随旧处理回收 |
| 不能这样算 | 5+15=连续硬直20帧；或第二段必定覆盖成实战15帧；或第二段必命中 |

这个例子能解释“同一动作为什么有不止一个硬直配置”，也显示连续命中不是只换动画。Grunt普通最长策略关闭，但AlreadyGuardBroken另有取最大值分支。冻结、动画时长覆盖和实际处理时序仍影响有效计时。

**能否连上：未确定。** 两段窗口位于同一动画的不同位置；5帧与窗口间隔不能直接证明中间必被防住，因为实际播放速率、冻结和受击动画覆盖尚未对齐。长硬直后短硬直的独立对照尚未固定到完整输入序列，不用掌击的特殊推开结果冒充纯时长对照。

## C03：玩家闪避Hook，和闪避StraightJab之后再打敌人

| 项目 | Hook对照 | StraightJab对照 |
|---|---|---|
| 敌人实际入口 | 普通Grunt组合图节点1，Grunt_Hook→Hook_HB01 | 同图节点11，StraightJab→Jab_HB01 |
| 玩家操作 | 成功闪避敌人该命中段，然后以同一指定动作反击；记录反击命中延迟 | 同左 |
| 保存的闪避惩罚开关 | DizzyOnAvoid=true | DizzyOnAvoid=false |
| 已确认的分流 | 为真时可选择特殊闪避配置；敌人携带的Avoided处理保存该配置，及时反击命中可产生AvoidDizzy候选 | 不通过该开关选取同一特殊配置；不代表其他来源绝不能使敌人眩晕 |
| 后续能压制的解释 | 若反击确实使敌人进入Dizzy，其有效状态许可层禁止四项AI防御动作 | 不能从本例推出同等的眩晕防御限制 |

玩家反击可先固定为N44槽0刺拳，但必须确认当时输入实际选中它；未确认前只作为观测方案，不宣称这是闪避后必选招式。前置订单配置0.666秒／0.5秒不等于之后眩晕总时长。

**对照限制：**换Hook与Jab同时改变了招式时序、位置等属性，不是只修改一个布尔字段的严格实验；代码对DizzyOnAvoid的读取支持该分流解释，实战仍需控制反击时刻和位置。不能把Hook下的空挥或反击未命中误判为惩罚开关无效。

## C04：同一敌招被玩家招架，敌人架势是否崩溃

| 项目 | 本例内容 |
|---|---|
| 固定敌招 | Grunt_Hook段0→Hook_HB01，保存可招架，DizzyOnParry=false |
| 玩家操作 | 对同一命中段成功招架；分别固定敌人架势远离崩溃、接近崩溃，然后尝试同一后续攻击 |
| 分流条件 | 反馈允许且将导致架势崩溃时，走独立破架势反馈；不能因为招架成功就套专用眩晕模板 |
| 已知与未知 | 来袭保存行不满足专用DizzyOnParry眩晕分支；运行时覆写、反馈修正和崩溃条件仍须固定 |
| 能否连续压制 | 两组后续能出什么、是否命中、是否被防御仍需分别核对，当前不写必连 |

这个例子解释“同样是玩家招架，敌人的后续受控为什么可能不同”。它还没有证明用户实测的稳定追击由破架势造成。玩家后续选择三连拳时，应另看C05，不能把三连拳制造的状态归给招架事件。

## C05：三连拳末段制造的眩晕，可能与招架本身不同

| 项目 | 本例内容 |
|---|---|
| 输入关联 | 徒手图S3轻击经过BP_TargetIsParryVictim条件对象到Node1；再输入轻击，Node1保存三个加权分支。条件对象的实际返回、起始状态选择及权重执行仍需核 |
| 本例固定分支 | Node2／3Hits_01→MC_3Punches_FR；不是每次该输入必选FR；Node17／18是其他三连拳版本 |
| 前两段 | 3Punches_HB01／02，基础眩晕等级0 |
| 末段 | 3Punches_HB03，基础眩晕等级14；普通／进阶Grunt站立InFight眩晕抗性11 |
| 条件判断 | 14>11形成眩晕候选；命中、韧性、效果优先分支、状态覆写和既有眩晕条件仍须通过 |

**能确认：**该动作末段有前两段没有的基础眩晕候选能力。**不能确认：**它就是用户实测的反击动作，或末段一定命中并使敌人眩晕。若末段进入Dizzy，之后的防御限制见C06；这是“后续攻击制造状态”的机制，不等于“玩家招架那一刻已制造该状态”。

## C06：敌人已经眩晕，为何能追击、又为何会恢复

| 因素 | 具体例子／条件对照 | 能解释什么 | 缺口 |
|---|---|---|---|
| 动作许可 | C03反击或C05末段确实让普通Grunt进入Dizzy；其有效上下文采用GenericNone | 敌人格挡／招架／躲避等四项AI防御动作均不可用，不是等AI随机决定不防御 | 仍需下一击距离、时序、韧性等允许命中；其他竞争上下文单独核 |
| 持续时间 | 同一Dizzy经过时间到期，与尚未到期对照 | 非暂停、非无限等条件下，时间可以触发状态退出 | 普通3秒是基础值；最终覆盖与修正需固定 |
| 累计伤害 | 普通Grunt该状态启用伤害限制时，累计伤害超过100与不超过100对照 | 有独立退出检查，不能只看时间 | 未找到能单独跨阈值而不同时触发其他退出的完整实战招式序列 |
| 归组命中数 | 普通Grunt启用计数限制时，按既有攻击名归组规则达到4与未达到4对照 | 有命中计数退出条件，不等于第四拳必恢复 | 事件归组、刷新／转移与多段攻击计数仍需固定；不是已实战例 |
| 不能无限重施同种眩晕 | C05末段等级14再次命中已经Dizzy的Grunt | 配置不允许普通Dizzy叠在Dizzy上；对应分支无SuperDizzy可用等条件时可回落普通Hit | 不能据此说所有再次眩晕都失败；特殊量表与分支另核 |
| 状态移除 | 退出时回收该Dizzy动作限制上下文 | 敌人恢复防御评估的许可条件可能改变 | 不保证退出同帧必格挡；恢复订单和AI决策仍存在 |

伤害上限和计数行目前是**配置边界例**，不是已经完成的“某套输入第几击退出”案例。没有为了凑每因素一例而伪造招式序列。时间、伤害、计数同时满足时，不能用现场一次恢复单独证明其中某一个。

## C07：玩家刺拳打中敌人膝击／旋踢的动作期间

| 项目 | 固定内容与已确认配置 |
|---|---|
| 玩家攻击 | C01的N44槽0刺拳Jab_HB01，韧性比较采用覆盖值1；不是生命伤害10，也不是眩晕等级 |
| 敌人动作例A | Grunt_KneeStrike膝击，普通与进阶组合都引用；动画通知关联Super服务，临时韧性增量+4 |
| 敌人动作例B | Grunt_SpinKick旋踢，普通与进阶组合都引用；通知关联普通服务，临时韧性增量+2 |
| 动画配置窗口 | 膝击约0.00166–0.66920秒；旋踢约0.11641–0.39218秒，均是动画时间坐标；播放速率／冻结等会影响实际墙钟时间 |
| 成对比较 | 先固定同一种敌人动作，比较玩家同一刺拳落在其服务有效区间／区间外；不是先换敌人动作就把差异全归给加值 |

**因果链：**敌人播放该动作，通知若实际启动服务→在敌人当前韧性上加4或加2→玩家刺拳命中时，用敌人当时韧性与刺拳覆盖值1比较→敌人韧性严格大于1且相关条件通过，会形成韧性抵抗；非致命、未破防的应用分支绕过正常受击处理→这次刺拳不能依赖正常受击处理来打断敌人。服务停止时撤销相同增量。

| 能否接上 | 当前能确认到哪里 |
|---|---|
| 玩家能出招 | 仍由玩家自己的输入和动作窗口决定，与敌人的加韧性服务不是同一个许可 |
| 玩家能命中 | 仍需距离、朝向、碰撞与时序成立；“敌人顶住”不等于刺拳打空 |
| 玩家能连续压制 | 韧性抵抗分支若实际成立，本次正常受击打断不会建立；是否还有其他状态反应仍需分别核 |
| 哪组实际会出现差别 | 敌人命中当刻的原有韧性和其他修正尚未查清；若原有韧性已高于1，区间外也可能抵抗，不能保证窗内外必有差异 |

目前已经有真实敌人动作、加值和配置区间，**不是只按类名猜“霸体”**；但没有把它写成已实测的必定打不断。敌人膝击自己用Medium还是Strong，是敌人打玩家的属性，不能拿来替代玩家刺拳的比较值。

## C08：更强的反应不等于更容易接下一击

| 项目 | 本例内容 |
|---|---|
| 掌击候选 | 徒手N32槽0/1基础动作MC_PalmStrike_FR段0→PalmStrike_HB01；基础推开等级3，高于Grunt InFight推开抗性2 |
| 分支解释 | 条件通过时形成推开候选，敌人位置可随反应改变；不能仅因硬直配置25帧大于刺拳8帧就断言更容易原地连打 |
| 状态抗性对照 | JumpingKick_HB01基础推开等级1，对InFight抗性2不够，对Dizzy抗性0形成候选；实际玩家动作输入／覆写尚未固定，因此只作为配置对照 |
| 倒地 | 尚未固定普通杂兵的完整输入→击倒→起身／后续命中案例；保留缺口，不借推开案例代替 |
| 可连性结论 | 产生特殊反应的候选有证据；后续是否出招、够不够距离、敌人是否恢复仍未闭合 |

这里涉及两个因素：反应判定与空间位置。当前没有位置／位移量完整证据，不能写成掌击后某招必空挥。

## C09：同一眩晕入口，普通与进阶杂兵为什么可能不同

| 固定／变化 | 内容 |
|---|---|
| 固定入口 | C03同一敌招闪避后，用同一玩家攻击、相同延迟命中，并确认实际进入同种Dizzy；成长／难度／初始生命架势固定 |
| 唯一角色变化 | Grunt_Base换为Grunt_Adv；不能把所有关卡杂兵外观直接当成这两个具体配置 |
| 相同项 | 这里所查基础受击DB、状态抗性矩阵、Dizzy禁止四项防御的动作层相同 |
| 不同项 | 普通Dizzy基础时间3／1.5秒；伤害限制100／70；归组计数4／3；情境防御图也有不同 |
| 可解释范围 | 即使共享受击入口，状态可能维持不同时间，退出后的选择也可能不同 |
| 不能得出 | 进阶只能连三拳、普通必多连一拳；具体生效退出条件和当前修正仍需固定 |

此对照同时改变角色多项配置，用来展示实际变体差异；不能用它单独实验某一个时长字段。

## 最小实战观测方案（未执行）

| 顺序 | 固定操作 | 记录事件 | 结果怎样判断 |
|---|---|---|---|
| 1 | 普通难度、同一普通杂兵、同成长，固定C01输入／姿态版本，紧接与延迟各一组 | 玩家各段出招与命中，敌人首次格挡／闪避、受击或特殊反应 | 先区分没出招、空挥、被防住；不能都记为断连 |
| 2 | 在第一组基础上观察可定位的内部值（需要另行授权运行时方式） | 敌人硬直计时、IsStun、恢复层、实际受击动画、四项防御许可及防御请求触发来源 | 区分计时先到期、许可变化、其他入口评估和下一击分流 |
| 3 | Hook与StraightJab闪避后，固定同一反击版本和命中延迟 | 玩家闪避成功、反击命中、敌人何时进入／退出Dizzy | 区分前置反击机会与持续眩晕；换招带来的位置差异单列 |

不用仅凭录像外观断言内部状态。静态分析继续先查普通受击中的实际执行限制；本页没有启动游戏或修改游戏／存档。
''')
put('02实现/受击与追击案例.md','''# 受击与追击案例：简要实现

[[01机制/受击与追击案例|案例与操作说明]] · [[02实现/连续受击与反击追击的系统链|既有E01–E23证据]] · [[03配置/受击案例配置对照|案例配置]]

| 案例 | 已定位的代码／配置 | 未闭合连接 |
|---|---|---|
| C01 普通连打 | MainChar_ComboTree节点44→45、槽0/1；OrderHitted::IsStunOrder `0x19fdb50`：Starting或HitTimeLeft>0；OnUpdate `0x1ae44d0`恢复分支；UAIFightingComponent::InternalBeginPlay `0x18b7e30`订阅OnIsStunChanged；同名回调`0x18bc520`条件性调用UpdateDefenseNeed | 玩家实际攻击间隔、受击动画选择；其他防御评估入口在普通硬直中是否可执行 |
| C02 后一击 | ApplyImpact、UOrderComponent::PlayOrder与取消生命周期（E17）；ThroatPlexus_HB01／02独立命中配置 | 最终计时覆盖／冻结、实际命中次序与首次防御 |
| C03 闪避入口 | FilterHit `0x1957ff0`、GetActiveAvoidMatchingAttack `0x195a360`、GenerateImpact与AvoidDizzy（E10/E11）；Grunt_Base_Combo节点1／11 | 同一反击输入实际选择、提前取消、缓存覆写 |
| C04 招架入口 | UGuardAbility::OnHitDefense `0x1a025f0`、实际Hook攻击行（E08/E09/E22） | 当前架势、反馈倍率及最终分支，后续攻击时序 |
| C05 三连拳末段 | MainChar_ComboTree.starts[3]→Node1→Node2／17／18；Node2的MC_3Punches_FR；HB03基础等级14与InFight抗性11 | BP_TargetIsParryVictim返回、启动状态、权重运行、条件覆写与命中结果 |
| C06 眩晕 | 状态时间／伤害／计数（E05）；Dizzy高优先上下文→AI许可查询→移除回收（E20） | 归组计数和刷新各分支；单一退出因素的完整动作序列 |
| C07 韧性 | GenerateImpact `0x1a5a610`、ApplyImpact `0x1a46d90`对应绕过分支（E02）；UResilienceOrderService.m_iBonus加减 | KneeStrike+4／SpinKick+2及通知区间已解析；当前韧性与实际触发仍缺 |
| C08 特殊反应 | ComputeImpactType `0x1a51f10`、GetAttackPropertyLevel `0x197d3c0`及保存效果等级／状态矩阵（E01） | 实际输入、状态覆写、位移和下一击空间关系；倒地完整例 |
| C09 变体 | Base／Adv ResistanceDB与HittedDB、情境防御图（E16/E20/E22） | 实际Normal0实例和附加修正 |

## 普通硬直事件链新增定位

| 环节 | 精确定位 | 主语与边界 |
|---|---|---|
| 谁被判硬直 | OrderHitted::IsStunOrder `0x19fdb50`；OrderBase+0xCA=EOrderState，1=Starting；OrderHitted+0x51C=HitTimeLeft | 敌人自己的活动受击处理；不是玩家硬直 |
| 恢复分支 | OnUpdate `0x1ae46e4–0x1ae47b1`，FHittedAnimContainer+0x1A=m_bInterruptible、+0x1B=m_bInterruptAnimationOnEnd | 计时、动画余时、非致命、层资源／已有句柄等条件共同作用 |
| 订阅已确认 | InternalBeginPlay `0x18b8177–0x18b81b2`，读取owner+0x1328的HitComponent，给+0x108委托AddUObject本AI对象及OnIsStunChanged | AddUObject被编译折叠时可显示其他模板类型名；实际函数指针及r8=this共同确认，不按别名误认玩家Controller |
| 通知后评估 | OnIsStunChanged `0x18bc563–0x18bc5db`，自身IsStun=false后查跟踪目标（玩家）与玩家AttackComponent+0xBF1等条件，调用UpdateDefenseNeed | +0xBF1的精确类型本批未命名，不称敌人handler字段 |
| 其他入口 | OnTargetOrderStateChangedInternal `0x18bfb30`中`0x18bfcd1`；OnAvailabilityChanged `0x18ba4a0`尾跳 | 玩家攻击订单变化与敌人动作许可变化可引发评估；这正是不能宣称计时前绝对禁防的原因 |
| 移动层排查 | UFightingMovementComponent::IsAvailable `0x1ab1820`，mode==3才按额外mask筛选，其余分支返回true | 本函数不能独自解释普通地面受击的防御禁止 |

本批原始输出：`inventory/case-movement-disassembly.json`、`inventory/case-defense-events-disassembly.json`；复用与失败记录：`inventory/case-defense-20261028.json`；xref候选扫描：`inventory/case-xrefs.json`。候选已在上述函数边界内核对，扫描不宣称间接调用完备。

详细推理：`notes/case-study-defense-20261028.md`、`notes/case-study-inputs-20261028.md`、`notes/case-study-ordinary-20261028.md`。案例页与配置页由`scripts/case_build_documents.py`维护，既有大配置目录不整体重跑。构建EXE SHA256为`a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`，匹配PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age1；未实战验证。
''')
# Recover precise base-input data directly, not from a same-named node in another tree.
g=json.loads((R/'inventory/player-combo-graphs.json').read_text(encoding='utf-8'))
t=next(x for x in g['trees'] if x['asset']=='Sifu/Content/DB/_MainChar/Combos/MainChar_ComboTree.uasset')
assert t['nodes'][44]['m_AttackInfos[0]']['m_Attacks[2]'].endswith('MainChar_Hook_BL.MainChar_Hook_BL')
rows=list(csv.DictReader((R/'exports/hit-impact-values.csv').open(encoding='utf-8-sig',newline='')))
selected=[x for x in rows if x['asset']=='Sifu/Content/DB/_MainChar/Combos/MainChar_HitBoxData.uasset' and x['row'] in ['Jab_HB01','ThroatPlexus_HB01','ThroatPlexus_HB02','3Punches_HB01','3Punches_HB02','3Punches_HB03','PalmStrike_HB01'] and x['outcome']=='m_OnHitImpact']
# Outcome label is copied exactly from the CSV; inspect and fail instead of silently publishing empty facts.
if not selected:
 selected=[x for x in rows if x['asset'].endswith('/MainChar_HitBoxData.uasset') and x['row'] in ['Jab_HB01','ThroatPlexus_HB01','ThroatPlexus_HB02','3Punches_HB01','3Punches_HB02','3Punches_HB03','PalmStrike_HB01'] and 'Hit' in x['outcome']]
assert len(selected)==7,(len(selected),[x['outcome'] for x in rows[:3]])
config='''# 受击案例配置对照

[[01机制/受击与追击案例|案例说明]] · [[02实现/受击与追击案例|简要实现]] · [[03配置/配置索引|配置索引]]

这些是本机构建保存的基础配置；不是最终伤害或保证无法行动时间。玩家输入路径固定MainChar_ComboTree，N44轻击→N45；仅槽0/1采用本表前两招基础版本。N44／45各有未解码的条件攻击覆写，因此运行时选择仍须核。

## 玩家实际命中行

| 中文动作／段 | HitBox行 | 启用生命／配置值 | 启用架势／配置值 | 启用硬直帧／配置值 |
|---|---|---|---|---|
'''
labels={'Jab_HB01':'刺拳 段0','ThroatPlexus_HB01':'咽喉／躯干双击 段0','ThroatPlexus_HB02':'咽喉／躯干双击 段1','3Punches_HB01':'三连拳 段0','3Punches_HB02':'三连拳 段1','3Punches_HB03':'三连拳 段2','PalmStrike_HB01':'掌击 段0'}
for row in selected:
 config+='| '+labels[row['row']]+' | '+row['row']+' | '+row['m_bUseDamage']+'／'+row['m_fDamage']+' | '+row['m_bUseStructureDamage']+'／'+row['m_fStructureDamage']+' | '+row['m_bUseNbFrameStuned']+'／'+row['m_iNbFrameStuned']+' |\n'
config+='''
来源：`exports/hit-impact-values.csv`，源表MainChar_HitBoxData；输入与命中资源引用见[[03配置/玩家攻击/输入衔接图-徒手]]。刺拳的22–23、双击14–15／22–24属于各自动画坐标，不能相减作跨动作命中间隔；受击配置帧经代码按60换算后仍可能修正。

## 敌人配置与恢复条件

| 因素 | 普通Grunt | 进阶Grunt | 适用说明 |
|---|---|---|---|
| 受击DB | GruntHittedDB | 同一DB | 普通最长硬直策略false，破架势另有分支 |
| 普通Dizzy基础时间 | 3秒 | 1.5秒 | 不是普通受击计时 |
| Dizzy伤害退出阈值 | 超过100 | 超过70 | 条件启用且未暂停／非无限等才按对应路径检查 |
| Dizzy归组计数阈值 | 达到4 | 达到3 | 不直接等于拳数 |
| InFight抗性[击倒,推开,眩晕] | [2,2,11] | 同左 | 比较攻击对应等级，需严格大于 |
| Dizzy抗性 | [0,0,1] | 同左 | 仍有禁止普通眩晕叠加等条件 |
| Dizzy动作层 | GenericNone | 同左 | 当前有效上下文只允许Look／MouseLook／DizzyReduction／ReplayMenu，四项防御不在其中 |
| 普通受击提前恢复 | 计时≤0、恢复层未添加且存在、动画余时>0、允许中断、未要求到期中断动画、非致命等 | 同代码 | 添加AIHittedRecovery并广播通知，不等于保证立即防御 |

完整来源分别见[[03配置/受击与抗性/索引]]、[[03配置/受击恢复/索引]]及既有综合实现E05/E16/E20。

## 特殊入口与效果等级

| 对象 | 保存配置／引用 | 说明 |
|---|---|---|
| Grunt Hook段0／StraightJab段0 | Hook_HB01的DizzyOnAvoid=true；Jab_HB01=false | 同普通敌人两种来袭招式的配置分流，不是只改变一项数值的实战实验 |
| Grunt Hook／BaseballHook／Uppercut | 可招架=true，DizzyOnParry=false，DizzyOnAvoid=true | 当前保存行不直接满足专用招架眩晕分支；缓存可覆写 |
| 三连拳末段 | 3Punches_HB03基础眩晕等级14 | 高于InFight基础眩晕抗性11仍只是候选 |
| 掌击段0 | PalmStrike_HB01基础推开等级3 | 高于InFight推开抗性2；后续空间关系另核 |
| 跳踢配置行 | JumpingKick_HB01基础推开等级1 | 对InFight2不足、Dizzy0可形成候选；完整输入案例未闭合 |

详见[[03配置/AI防御/Grunt反击条件与动作]]与[[01机制/连续受击与反击追击的系统链]]。韧性已定位膝击／旋踢实际动作、增量与动画通知，见下表；倒地完整案例仍未闭合，不用理论数字凑实战案例。
'''
config+='''

## 敌人动作的临时韧性配置

| 敌人动作／动画 | 服务CDO的韧性增量 | 动画通知开始／结束秒 | 通知持续秒 | Base／Adv引用 |
|---|---:|---|---:|---|
| Grunt_KneeStrike／Grunt_Attack_Barehands_KneeStrike | +4 | 0.001660836 → 0.669203639 | 0.667542815 | 两套组合都有 |
| Grunt_SpinKick／Grunt_Attack_Barehands_SpinKick | +2 | 0.116411872 → 0.392183691 | 0.275771827 | 两套组合都有 |

表中时间为序列链接坐标，读取器保留TriggerTimeOffset与EndTriggerTimeOffset；不是运行时保证区间。精确浮点值与字段边界见`inventory/case-resilience-notifies-20261028.json`。以上显示值为小数截取；精确浮点值以JSON为准。

服务字段为UResilienceOrderService.m_iBonus，普通CDO=2、Super CDO=4。OnStart加到敌人当前韧性、OnStop撤销同一值。服务继承与当前默认对象均已核对；具体场景的当前韧性和通知触发仍未知。不要用敌人自身攻击的Medium／Strong当作玩家攻击强度。原始引用及来源哈希见`inventory/case-resilience-config-20261028.json`、`inventory/case-resilience-extraction-20261028.json`；底稿`notes/case-study-resilience-20261028.md`。
'''
put('03配置/受击案例配置对照.md',config)
layoutp=R/'inventory/vault-layout.json';layout=json.loads(layoutp.read_text(encoding='utf-8'))
for rel in changed:
 if rel not in layout['documents']:layout['documents'].append(rel)
if '受击与追击案例' not in layout['topics']:layout['topics'].append('受击与追击案例')
if not (B/'vault-layout.json').exists():(B/'vault-layout.json').write_bytes(layoutp.read_bytes())
layoutp.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8')
update('02实现/连续受击与反击追击的系统链.md','案例化改写与普通硬直事件E23','''阅读主线已改为明确玩家／敌人主语的分支说明，实例见[[01机制/受击与追击案例]]；原E01–E22作为既有证据编目保留，不据编目数量宣称场景闭合。

| 编号 | 本批连接 | 原始定位与边界 |
|---|---|---|
| E23 | 普通Hitted计时→恢复层／硬直通知→订阅回调→条件防御重新评估 | OrderHitted::IsStunOrder `0x19fdb50`；OnUpdate `0x1ae46e4–0x1ae47b1`；UAIFightingComponent::InternalBeginPlay `0x18b8177–0x18b81b2`订阅；回调`0x18bc563–0x18bc5db`。详细见[[02实现/受击与追击案例]]及`notes/case-study-ordinary-20261028.md`。其他目标订单／可用性变化也能触发评估，普通硬直的全入口禁防未证明 |
''')
update('01机制/受击硬直与脱离.md','以案例为主的阅读更新','''先读[[01机制/受击与追击案例]]的C01／C02，再看[[01机制/连续受击与反击追击的系统链]]的普通硬直分支图。已接通的是硬直结束条件性引发防御重新评估，不是证明“硬直计时未结束时所有防御入口都被禁止”。眩晕的累计限制不能用来解释所有普通连打。''')
for rel in ['00索引/首页.md','00索引/研究进度与问题.md','00索引/解包与解析进度.md']:
 update(rel,'20261028受击案例批次','''| 项目 | 当前结果 |
|---|---|
| 阅读入口 | [[01机制/受击与追击案例]]列C01–C09；[[01机制/连续受击与反击追击的系统链]]重写普通硬直分支，主语固定玩家／敌人 |
| 新接通 | 硬直计时→有条件恢复层与广播→初始化订阅→敌人不再硬直时条件性重评估防御（E23） |
| 实际配置 | N44槽0/1刺拳→N45双段轻击；三连拳加权入口；Hook／StraightJab闪避分流；[[03配置/受击案例配置对照]]附中文数值 |
| 四阶段 | 本批主要复用已提取／已解析资源，新增代码接线与案例解释；未实战验证。不能说普通连打完整案例已经闭合 |
| 修订 | 普通恢复层存在不证明此前全禁防；输入图转移不等于命中或连续压制；Hook/Jab换招不构成严格单属性实验 |
| 下一项最小取证 | 先追玩家攻击订单变化／敌人许可变化触发防御评估后，普通受击中实际执行限制；随后对齐C01两动作实际命中间隔与受击动画选择 |
| 暂缺案例 | 伤害／计数阈值尚无单因素完整招式序列；普通杂兵膝击+4／旋踢+2及动画通知已解析，但基础韧性／实际命中结果与倒地追击仍未闭合；不以假设补足 |

本批命令、检查、失败与续接见研究根目录`notes/handoffs/20261028-受击案例-03.md`。未启动游戏；当前无需用户操作。''')
update('00索引/系统线索与关系图.md','案例研究补充S25','''| 因素与位置 | 证据及已知作用 | 关联 | 缺口／下一步 | 优先级／入口 |
|---|---|---|---|---|
| S25 普通硬直结束的事件通知 | E23；计时到零且恢复条件通过，加入恢复层并广播OnIsStunChanged；InternalBeginPlay已订阅到AI自身回调 | 自身受击谓词→跟踪玩家攻击信息→防御重新评估 | 其他目标订单／许可变化也触发更新；须核普通受击中的最终执行限制，不能把本回调当全局禁防 | **阻塞主线**；[[01机制/受击与追击案例]]C01／C02 |
| S26 输入图与命中时序分层 | N44→45仅证明保存输入路径；槽0/1／2/3动作不同，条件覆写尚未解 | 玩家出招→命中事件→敌人受击更新 | 两动画帧号不能跨动作直接相减；需动作启动、播放速率、冻结、受击动画与覆写 | **阻塞主线**；案例C01及配置对照 |

原图中普通恢复层到防御查询的箭头表示可达路径，不表示计时未结束时所有入口禁防。最新主线与带判断节点的分支图见[[01机制/连续受击与反击追击的系统链]]。S01/S03的下一步以本批为准：先普通受击实际执行限制，不再优先扩展反击首招映射。''')
update('03配置/配置索引.md','案例配置阅读入口','[[03配置/受击案例配置对照]]按C01–C09列玩家命中段、硬直帧、状态抗性与敌人差异；对应[[01机制/受击与追击案例]]。')

for rel in ['01机制/攻击冲击力韧性与伤害.md','02实现/攻击冲击力韧性与伤害.md']:
 update(rel,'实际敌人动作样本补充','普通与进阶Grunt组合均引用膝击Grunt_KneeStrike与旋踢Grunt_SpinKick；动画通知分别关联临时韧性+4／+2。配置区间约0.00166–0.66920秒／0.11641–0.39218秒，均为动画时间坐标。详见[[01机制/受击与追击案例]]C07与[[03配置/受击案例配置对照]]；当前基础韧性与实战触发未核，不宣称一定霸体。')
rel='01机制/受击硬直与脱离.md';x=(V/rel).read_text(encoding='utf-8')
x=x.replace('普通、进阶杂兵的哪些具体动作使用该服务，当前尚未确认，也不能用它概括所有脱离现象。','已找到普通／进阶杂兵膝击+4、旋踢+2的服务与动画通知区间，见案例C07；但不能用它概括所有脱离现象。')
x=x.replace('| 临时韧性服务挂载动作 | 待确认 | 待确认 | 尚不能列出动作名称、加值和区间 |','| 临时韧性服务挂载动作 | 膝击+4／旋踢+2 | 同样引用 | 动画通知区间见C07；当前韧性与实际触发待核 |')
x=x.replace('代码分支已确认，具体杂兵动作待查','膝击／旋踢服务与区间已核，实际阈值及命中结果待查');put(rel,x)
rel='02实现/攻击冲击力韧性与伤害.md';x=(V/rel).read_text(encoding='utf-8').replace('具体杂兵动作的服务引用仍待查。','本批已定位膝击与旋踢的服务引用、CDO与通知区间，见下方补充。').replace('| 具体动作挂载 | 在当前已解码对象、CDO 和元数据中未检出该服务记录 | 不能证明游戏不存在；需按需补提取或追调用者 |','| 具体动作挂载 | 旧批次未检出，本批已补膝击+4／旋踢+2及通知区间 | 见C07；实际运行与当前韧性仍待核 |');put(rel,x)
rel='00索引/系统线索与关系图.md';x=(V/rel).read_text(encoding='utf-8').replace('普通／进阶具体动作的挂载、数值与时间段','KneeStrike+4／SpinKick+2及动画通知已核；剩基础韧性、实例修正和实际命中结果');put(rel,x)


rel='00索引/首页.md';x=(V/rel).read_text(encoding='utf-8')
if '| 从具体招式与现象理解受击／追击 |' not in x:
 x=x.replace('| 连打脱离、招架追击、闪避追击的共享与分流 |','| 从具体招式与现象理解受击／追击 | [[01机制/受击与追击案例]] |\n| 连打脱离、招架追击、闪避追击的共享与分流 |')
put(rel,x)
for rel in ['00索引/研究进度与问题.md','00索引/解包与解析进度.md']:
 x=(V/rel).read_text(encoding='utf-8');link='最新续接：[['+rel.removesuffix('.md')+'#20261028受击案例批次|受击案例批次与下一步]]。前文旧批次清单保留历史范围，研究优先级以该节为准。'
 if link not in x:
  h=x.find('\n');x=x[:h+1]+'\n'+link+'\n'+x[h+1:]
 x=x.replace('## 按顺序继续的问题','## 早期问题列表（以最新批次为准）');put(rel,x)

(R/'inventory/case-study-documents.json').write_text(json.dumps({'batch':'20261028-受击案例-03','documents':changed,'backup_root':str(B),'source_graph':t['asset'],'base_nodes':{'44':t['nodes'][44],'45':t['nodes'][45]},'selected_impact_rows':selected,'sources':[{ 'path':str(p.relative_to(R)).replace('\\','/'),'sha256':sha(p)} for p in [R/'inventory/player-combo-graphs.json',R/'exports/hit-impact-values.csv',R/'exports/mainchar-attackdb-timing.csv',R/'notes/case-study-inputs-20261028.md',R/'inventory/case-resilience-notifies-20261028.json',R/'inventory/case-resilience-config-20261028.json']], 'runtime_verified':False},ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({'updated_documents':len(changed),'new_vault_total':len(layout['documents']),'impact_rows':len(selected)},ensure_ascii=True))
