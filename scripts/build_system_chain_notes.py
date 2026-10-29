import json,hashlib,datetime,shutil
from pathlib import Path
R=Path(r'E:\ProgrameFiles\SifuResearch'); V=R/'Sifu'
backup=R/'notes'/'vault-backups'/'system-chain-20261028'; backup.mkdir(parents=True,exist_ok=True)
changed=[]
def put(rel,text):
 # The integrated pages are now owned by the readable-rules sources.
 reader_sources={'01机制/连续受击与反击追击的系统链.md':'mechanism.md',
                 '02实现/连续受击与反击追击的系统链.md':'implementation.md'}
 if rel in reader_sources:
  current=R/'notes/reader-sources/20261029-state-spec'/reader_sources[rel]
  if not current.is_file(): current=R/'notes/reader-sources/20261029-rules'/reader_sources[rel]
  if current.is_file(): text=current.read_text(encoding='utf-8')
 p=V/rel
 if p.exists():
  b=backup/rel; b.parent.mkdir(parents=True,exist_ok=True)
  if not b.exists(): shutil.copy2(p,b)
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text.strip()+'\n',encoding='utf-8',newline='\n');changed.append(rel)
put('01机制/连续受击与反击追击的系统链.md',r'''
# 连续受击与反击追击的系统链

[[00索引/首页|首页]] · [[02实现/连续受击与反击追击的系统链|对应实现与证据]] · [[00索引/系统线索与关系图|系统线索与关系图]]

“敌人为何脱离连打”与“防反／闪避反击后为何能追击”共享命中、受击和状态管理，但入口存在分流。当前最明确的新连接是：**特定攻击被成功闪避后，会选择一套让后续命中附加眩晕的配置；成功闪避与反击命中分工不同。** 不能把所有防反、闪避和普通受击归为固定几次命中的防无限连规则。

本文的“确认”指本机静态代码／配置，未运行游戏验证。玩家实测“防反／闪避反击后能稳定接部分连招”保留为待完整解释的现象。

## 样本与版本固定

| 项目 | 固定内容 | 边界 |
|---|---|---|
| 游戏构建 | 本机Epic安装的Shipping EXE，SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；匹配PDB age1 | 其他更新不能直接套用 |
| 敌人 | Grunt_Base与Grunt_Adv，徒手；普通难度Normal0为比较目标 | 尚未运行关卡确认所遇实例、额外修正和当前状态 |
| 普通追击样本 | 徒手图N44，姿态槽0/1，MainChar_Jab_FR，命中段0→Jab_HB01 | 不与槽2/3的Hook_BL混算；输入L及实际条件见原图 |
| 多段反击样本 | MC_3Punches_FR，命中段0/1/2→3Punches_HB01/02/03 | 名称PostParry不是实际触发许可的充分证据；不能把三段数值并成一击 |
| 配置版本 | 本次提取的原表、CDO与匹配代码；完整路径／哈希见实现篇 | 保留原有玩家图与全量表，不重新合并姿态伤害 |

入口：[[03配置/玩家攻击/输入衔接图-徒手]]、[[03配置/动作与时序/玩家-BareHands-LightCombo-动作资源]]、[[03配置/动作与时序/玩家-BareHands-PostParry-动作资源]]。

## 三种场景的分工与共用流程

| 环节 | 普通命中后连打 | 成功招架后反击／追击 | 成功闪避后反击／追击 |
|---|---|---|---|
| 首次事件 | 玩家攻击实际命中敌人 | 防御判定成功，还要区分可弹开、招式属性和破架势 | 来袭攻击与当前有效闪避匹配 |
| 入口分流 | 普通Hit、特殊状态候选；韧性可能绕过普通受击订单 | 允许且将破架势→破架势反馈；否则CanDeflect且来袭DizzyOnParry→专用眩晕命中；其余仍有反馈处理 | 来袭DizzyOnAvoid为真时，可换用可惩罚闪避配置 |
| 是否立即等于长眩晕 | 否，取决于等级、状态抗性及其他gate | 否，专用眩晕是有条件分支 | 否；特殊配置使之后的命中产生AvoidDizzy，不能提前把成功闪避本身写成眩晕 |
| 后续命中 | 继续计算冲击力、抗性、伤害、硬直并更新状态 | 专用反馈或玩家后续攻击再进入命中／状态管线 | 命中时读到AvoidDizzy→在允许路径中进入Dizzy |
| 持续受控 | 依具体状态的时间、伤害、命中数及刷新策略 | 进入Dizzy等状态后使用共同状态系统；特殊模板可取动画时长 | 进入Dizzy后使用共同状态系统；前置Avoided订单窗口与之后Dizzy持续时间分开 |
| 恢复防御 | Hitted恢复层、持续状态／恢复订单和AI请求分别核对 | 同左；不能把主角GuardDB的0.6秒套成敌人统一窗口 | 同左；0.666／0.5是特定profile配置值，不是已验证可连击总时长 |
| 尚缺 | 连续命中如何刷新各计时、实际下一次防御时序 | 固定敌方实际命中行／缓存覆写，闭合普通招架的具体反馈 | 已闭合原攻击者订单保存与倒计时；具体招式引用、外部提前取消及完整追击许可仍待核对 |

## 普通受击为什么会有结束点

| 层次 | 已确认规则 | 对脱离的含义 |
|---|---|---|
| 普通硬直 | OrderHitted有独立受击计时；到期且满足订单／状态条件时添加HitRecoveryAvailability | 敌人可能在受击动画还在时走恢复许可路径；不能只看动画判断能否格挡 |
| 恢复许可 | 临时可用性层有句柄；Hitted停止时移除。AI与玩家恢复层不同 | 一层允许某动作不代表其他层和订单允许，许可也不等于AI已经选择 |
| 持续状态 | 非暂停、非无限时，超过持续时长，或启用的累计伤害超过上限，或启用的命中数达到上限，可退出对应状态 | 存在数值退出机制，但只针对具体状态／启用条件；不是每次普通挨打都数到相同次数 |
| 计数口径 | 有按攻击名归组的配置，并记录上次攻击名 | 一次招式可多段；“四次计数”不能直接翻译成“四拳” |
| 状态刷新 | 新命中可更新／替换状态；已有Dizzy的时间与计数并非一概清零 | 不能假设每一击无限重置窗口；具体刷新分支仍需补齐 |
| AI反应动作 | 状态订单到零时，若成功调度条件反应，可把关联动画订单延后0.5秒并否决本次到期 | 这是条件调度分支，不是所有敌人固定多硬直半秒 |
| AI防御选择 | 来袭预测→当前最高状态与防御图→测试／记忆／候选→验证执行 | 恢复后面对下一击，AI才可能选择格挡、弹开、躲避或反击；尚未证明必然哪一帧执行 |

### 普通／进阶杂兵的已落实差异

| 配置 | 普通Grunt | 进阶Grunt | 可得结论 |
|---|---:|---:|---|
| 基础受击DB | GruntHittedDB | 同一DB | 不能从此DB推断两者普通硬直必有差异 |
| Dizzy累计伤害上限 | 100 | 70 | 同一Dizzy限制配置下，进阶阈值较低；不是最终生命伤害公式 |
| Dizzy累计命中上限 | 4 | 3 | 开启该条件时影响退出；按攻击归组，不能直接等于拳数 |
| Dizzy允许叠在Dizzy上 | false | false | 普通眩晕候选可能回落Hit；SuperDizzy可用性另参与分支 |
| InFight抗性[击倒,推开,眩晕] | [2,2,11] | [2,2,11] | 这部分矩阵相同 |
| Dizzy／Counter_Hit／Avoided／Parried／StructureBroken抗性 | [0,0,1] | [0,0,1] | 当前状态会影响后续命中结果；列在表里不代表该状态本场景一定进入 |
| Pushed抗性 | [0,100,1] | [0,100,1] | 推开通道阈值与上述状态不同 |
| 情境防御图 | Base图 | Adv图 | 攻击记忆时限、测试与边不同；不能单凭某个记忆测试保证反击 |

## 状态与攻击效果怎样互相影响

特殊效果等级要**严格大于**当前状态对应抗性；代码先检查推开，再检查击倒，再检查眩晕。等级和冲击力是两套判断，不是伤害大小的别名。

| 玩家HitBox行 | 等级[击倒,推开,眩晕] | 对InFight的候选 | 对Dizzy的候选 | 限制 |
|---|---:|---|---|---|
| Jab_HB01 | [0,0,0] | 普通Hit | 普通Hit | 普通硬直另算 |
| PalmStrike_HB01 | [0,3,0] | Push | Push | 还要命中、韧性等前置条件通过 |
| 3Punches_HB03 | [0,0,14] | Dizzy | Dizzy候选 | 已Dizzy且禁顶层眩晕、无SuperDizzy可用时回落普通Hit |
| JumpingKick_HB01 | [0,1,0] | 普通Hit | Push候选 | 原表值；需要核对当前动作版本的实际引用 |
| ParryDizzy_HB01 | [0,0,1000] | Dizzy候选 | 仍受现态分支约束 | 防反专用模板，不能替代普通追击行 |

因此，“进入更容易被推开／击倒的状态”与“该状态不允许继续叠眩晕”可以同时存在。不能把低抗性理解成无限续硬直。动作期间临时韧性另外影响正常受击订单是否建立，详见[[01机制/攻击冲击力韧性与伤害]]。

## 闪避机会的已知入口

| 步骤 | 证据支持的规则 | 对实测现象的解释范围 |
|---|---|---|
| 匹配来袭攻击 | GetActiveAvoidMatchingAttack读取来袭命中行DizzyOnAvoid | 是否可惩罚与敌方具体招式／命中段有关 |
| 替换闪避属性配置 | 为真时从当前AvoidPropertyDB选AvoidDBOnDizzyAttack；玩家普通闪避引用MainChar_Avoid_AvoidPunishable | 特殊入口来源于被闪避的攻击，不只是玩家后续用了更强招式 |
| 可惩罚配置 | MainChar_Avoid_AvoidPunishable的AvoidedEnterDizzyOnAttacked=true，duration配置0.666秒；攻击期间另有MainChar_Attack_AvoidPunishable，0.5秒 | 两份profile分别列出；已找到时长写入原攻击者Avoided订单、按delta倒计时并到零RequestStop；仍可能提前取消 |
| 后续反击命中 | 成功闪避后在原攻击者安排Avoided订单并保存所选DB；玩家后续命中时，GenerateImpact从受击目标的该订单读回DB，标记AvoidDizzy；满足状态条件后施加Dizzy | 找到了“成功闪避→特定反击命中→持续受控”的直接代码桥 |
| 机会维持与结束 | 进入持续状态后又受Dizzy限制／硬直更新／许可影响 | 前置反击窗口和整套追击窗口不是同一个时钟；完整长度待证 |

Grunt原始命中表有区分：Hook、Uppercut、RushFrontKick等DizzyOnAvoid=true，而Jab、Knee、Elbow等false。不能将同一敌人所有攻击一概处理；原表与实际缓存行也要区分。

## 招架为何需要进一步分流

| 情况 | 静态确认 | 尚不能归因的部分 |
|---|---|---|
| 反馈导致架势崩溃 | 有独立StructureBrokenHit及破架势状态路径 | 与普通招架后追击分别比较，固定初始架势 |
| 来袭攻击允许专用眩晕反馈 | CanDeflect且DizzyOnParry等条件通过时，能力施加ParryDizzy模板；眩晕等级1000、UseHitAnimDuration=true | 模板20帧普通stun不等于眩晕总时间 |
| 普通反馈 | 反馈量可由来袭覆盖或防守者GuardDB默认计算，架势反馈另受属性加成 | Grunt原始20行DizzyOnParry全false；还不能拿专用模板解释用户所有普通招架现象 |
| Deflected订单 | 读取订单所有者的GuardDB，能改变攻击播放比例并清理相关句柄 | 主角配置0.6秒，Grunt配置0；不能移植成敌人的统一禁止防御时间 |

## 最小实战验证方案（尚未执行）

先补静态实际引用与计时写入；若仍触及边界，再由你决定是否实测。此处仅列观测设计，不启动游戏。

| 对照 | 固定变量 | 只需记录 | 用来区分 |
|---|---|---|---|
| 普通／进阶 × 普通命中 | 普通难度、徒手、同成长／技能、同一N44姿态版本、同起始生命架势 | 每段命中／首次格挡、是否推开倒地眩晕、输入与命中时刻 | 普通硬直恢复、持续状态限制与AI选择 |
| 闪避Jab对照Hook | 同一敌人，固定来袭命中段；成功闪避后以同一反击，分短／较长延迟 | 反击是否命中、是否出现持续眩晕、后续首次防御 | 攻击属性选择profile的作用；不是先假定所有闪避相同 |
| 招架Jab对照Hook／Uppercut | 固定架势远离崩溃，再加接近崩溃一组 | 是否立即打断、是否架势崩溃、同一后续攻击可否命中 | 普通反馈、专用眩晕与架势崩溃分流 |
| 同一眩晕后的多段／单段追击 | 同起手状态、分别固定攻击版本与段数 | 首次脱离前的攻击名与实际命中段数、累计伤害 | 归组计数与“固定几拳”假说 |

暂不报告精确可连几击、窗口帧数或必反击招式。未解问题已缩到实际命中行／覆写、刷新读取点、订单提前取消及AI最终调度，见[[00索引/系统线索与关系图]]。
''')
put('02实现/连续受击与反击追击的系统链.md',r'''
# 连续受击与反击追击的系统链

[[01机制/连续受击与反击追击的系统链|机制与场景对照]] · [[00索引/系统线索与关系图|线索与未解问题]]

本篇只留数据入口与关键分支。完整寄存器、RVA、反汇编和提取过程分别在研究根目录的 `notes/recovery-system-chain.md`、`notes/parry-system-chain.md`、`notes/avoid-system-chain.md`。这些是本机构建静态证据，不是运行测试。

## 数据与代码连接

| 编号 | 因果连接 | 代码定位（RVA） | 本地配置／复核入口 |
|---|---|---|---|
| E01 | 攻击属性等级与当前状态抗性比较→候选受击类型 | UHitComponent::ComputeImpactType `0x1a51f10`；FHitboxDataRow::GetAttackPropertyLevel `0x197d3c0` | `exports/state-resistance-matrices.csv`；`inventory/system-recovery-grunt-state-matrix.json`；`inventory/system-recovery-hitbox-state-candidates.json`；`notes/resilience-damage.md` |
| E02 | 临时韧性修改→冲击力比较→可绕过常规Hitted／状态订单路径 | GenerateImpact `0x1a5a610`、ApplyImpact `0x1a46d90` | `notes/resilience-damage.md`；具体动作挂载与加值还缺 |
| E03 | 普通硬直剩余时间→条件式Push恢复许可；停止→Pop同一句柄 | OrderHitted::OnUpdate `0x1ae44d0`、OnStop `0x1ae1a40` | GruntHittedDB→AIHittedDB→AIHittedRecovery，`inventory/stun-state-data.json`；`inventory/system-recovery-disassembly.json` |
| E04 | 已有Hitted时，LongestStun或AlreadyGuardBroken→本次stun与既有剩余时间取max | GenerateImpact `0x1a5b545–0x1a5b578` | UHittedDB+0x75、FImpactResult+0x1a/+0x98、OrderHitted+0x51c；Grunt最长策略false。false不证明“新击总覆盖旧击” |
| E05 | 持续状态时间／伤害／计数退出，影响后续状态与恢复订单 | UDefenseComponent::TickComponent `0x196a130`、OnDamage `0x1965280`、OnHit `0x19653b0`；ApplyFightingStateFromImpact `0x1a46990` | `notes/研究报告.md`、`notes/recovery-system-chain.md`；`inventory/stun-state-data.json` |
| E06 | 状态订单到期→条件反应调度／veto延期；非必然立刻恢复 | FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero `0x18bd1a0`；OrderFightingState::OnStart `0x1a074f0`、OnStop `0x1a07ed0` | `notes/recovery-system-chain.md`；状态／恢复动画来自当前ResistanceDB |
| E07 | 来袭预测、最高状态、防御图与记忆→候选验证／执行 | UpdateDefenseNeed `0x18c9e50`、IsDefenseNeededInternal `0x18b8fc0`、PickContextualDefense `0x1895070` | `exports/grunt-contextual-defense.json`；`notes/stun-ai-defense.md`。序列测试反转、概率和竞争候选分开 |
| E08 | 防反结果→条件破架势模板／眩晕模板→给原攻击者施加Impact | UGuardAbility::OnHitDefense `0x1a025f0` | `inventory/system-defense-ability-cdos.json` BP_GuardAbility；Generic_HitBoxData/ParryStructureBroken_HB01、ParryDizzy_HB01；`notes/parry-system-chain.md` |
| E09 | 招架反馈量取覆盖／GuardDB默认／属性加成 | GetSelfStructureDamage `0x197fda0`、GetSelfSuperDizzyDamage `0x1980000` | `inventory/system-deflect-getters-disassembly.json`；MC_GuardDB的50/10须满足调用分支，不能直接当任意来袭反馈 |
| E10 | 闪避匹配来袭行→选择特殊AvoidDB→存入防御结果 | FilterHit `0x1957ff0`，GetActiveAvoidMatchingAttack `0x195a360` | `inventory/system-avoid-config-samples.csv`；MainChar_Avoid_AvoidDB→MainChar_Avoid_AvoidPunishable |
| E11 | 本次命中结算读取目标Avoided订单携带的DB→AvoidDizzy→条件Dizzy | GenerateImpact `0x1a5b1eb–0x1a5b2ad`；UpdateFightingStateFromImpact `0x1a70cb6–0x1a70d08` | 目标GetOrderFromType(5)→order+0x48→NetStruct+0x28的DefenseResult→AvoidDB+0x61；排除ImpactType4/10并检查SuperDizzyAvailable；FilterHit→原攻击者ScheduleOrderOverAttack→HandleOrderOverAttack(0x19c0590)→PlayOrder(5)，订单保存原结果；Start(0x1ade250)设时长，Update(0x1ae3a30)到零RequestStop |
| E12 | Deflected订单按所有者GuardDB影响攻击播放 | OrderDeflected::OnStart `0x1ade500`、OnUpdate `0x1ae3ba0`、OnStop `0x1ae14e0` | `inventory/system-parry-attack-disassembly.json`；Grunt duration0，MC duration0.6；不可跨所有者套数值 |
| E13 | HitBox可变缓存行优先于原表 | FHitBox::GetRow `0x197fbe0`、GetMutableRow `0x197eaa0` | `inventory/system-hitbox-override-disassembly.json`；因此固定原表行还不足以固定最终运行值 |

## 本轮消除的歧义

| 旧问题 | 本轮结论 | 仍保留的边界 |
|---|---|---|
| 未保存m_bInverted是否默认false | 基础UAIInfluenceTest构造RVA `0x1bf9870`写+0x48为0；PDB基类／派生尺寸及属性反射共同支持默认false | 类型FieldList未直接列出该成员，以组合证据定位；不能排除具体资产显式覆写。见`inventory/system-recovery-type-layouts.json`及底稿 |
| 两个HittedDB时间标志是否都找到用途 | LongestStun的消费已找到；TimeSinceLastHit的+0x74消费者仍缺 | 不借字段名推断连续命中最终计时 |
| 防反模板数值是否等于反馈最终数值 | 代码会覆写架势／SuperDizzy基础值 | 生命、架势、普通stun与Dizzy时长各自区分 |
| AvoidDB的0.666／0.5是否等于敌人眩晕时长 | 否；已找到它写入原攻击者Avoided订单，按delta倒计时；之后Dizzy由状态管线及目标ResistanceDB决定 | 订单保存与倒计时已闭合；仍需实际招式引用、提前取消及状态时间对应 |
| 防反后的Hitted通知属于谁 | 模板Impact作用于原攻击者，但其后Hitted调用对象为原防守者 | 不用这个Hitted回调重复证明攻击者受击 |
| IsStunChanged是否检查无效枚举哨兵 | 既有机器码确认非零判断，不能写成已知无效哨兵 | 该分支限制保留；检查对象为AI自身 |

## 构建与复核

| 项目 | 记录 |
|---|---|
| EXE SHA256 | `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254` |
| PDB | GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d`，age1 |
| 本轮能力CDO | 34对象，完整消费字节检查与原文件哈希保存在`inventory/system-defense-ability-cdos.json` |
| 分支取证 | `inventory/system-recovery-disassembly.json`、`inventory/system-avoid-disassembly.json`、`inventory/system-parry-disassembly.json`及同前缀其他清单 |
| 自动检查 | `scripts/verify_knowledge_vault.py`：知识库清单、链接、证据路径、Python语法、反汇编哈希与EXE哈希 |
| 不属于自动检查的内容 | 实际Normal0实例、最终伤害、窗口长度、逐帧AI选择与游戏行为 |
''')
put('00索引/系统线索与关系图.md',r'''
# 系统线索与关系图

[[00索引/首页|首页]] · [[01机制/连续受击与反击追击的系统链|综合机制]] · [[02实现/连续受击与反击追击的系统链|证据编号E01–E13]]

同一因素重复出现时更新本表，不拆成互不关联的待办。阻塞主线先追到能解释该子链；直接关联完成当前子链后展开；其他线索只保留证据和入口。本表不表示全部线索都已解释实战效果。

## 系统关系图

实线为已核对的代码／数据连接；虚线为仍需接通的具体桥。节点属于某条分支，不代表每次命中全经过。

```mermaid
flowchart TD
  A[实际攻击版本与命中段] --> B[HitBox原表或可变缓存]
  B --> C[命中结算]
  R[当前状态与抗性矩阵] --> C
  T[当前韧性与临时服务] --> C
  C --> H[普通Hitted硬直分支]
  C --> S[持续状态分支]
  H --> L[条件式恢复许可层]
  S --> R
  S --> Q[计时/伤害/命中数退出与恢复订单]
  Q --> K[条件反应调度和到期veto]
  P[来袭预测/状态/记忆/情境防御图] --> D[验证并执行防御请求]
  L -. 具体AI查询与帧序待接 .-> D
  Q -. 与最终选择时序待接 .-> P
  B --> V[成功闪避的特殊DB选择]
  V --> O[受击目标的Avoided订单]
  O --> X[命中时读取DB与AvoidDizzy条件]
  X --> S
  G[成功防御判定] --> G1[破架势或专用眩晕等反馈分支]
  B --> G1
  G1 --> C
  G --> G2[Deflected攻击播放调整]
  Q -. 个体状态到群体调度的完整反馈待接 .-> F[攻击票据/角色分工/冷却]
```

## 线索索引

| ID／因素与作用位置 | 发现依据与已知作用 | 输入／关联输出 | 未解问题与下一项必要取证 | 优先级／回查入口 |
|---|---|---|---|---|
| S01 普通硬直刷新 | E03/E04；LongestStun为真或AlreadyGuardBroken时与既有剩余时间取max，Grunt策略false | 本次stun、既有Hitted→恢复许可时机 | HittedDB+0x74消费者、订单替换／计时写入；先沿ApplyImpact到Hitted订单更新定位 | **阻塞主线**；recovery底稿、综合机制普通受击表 |
| S02 状态累计限制 | E05；Dizzy有时间、伤害、命中限制，按攻击名归组 | 命中／伤害事件→状态退出、抗性变化 | 新命中保留／转移计数的全部分支；固定攻击名与段数对照 | **阻塞主线**；受击硬直与脱离、recovery底稿 |
| S03 恢复许可与AI选择 | E03/E06/E07；Push/Pop恢复层与情境防御请求是不同环节 | 状态／订单→层；来袭预测／记忆→候选 | AI消费层的具体调用与最终帧序；查AIHittedRecovery的动作许可查询 | **阻塞主线**；综合实现E03/E06/E07 |
| S04 闪避按攻击分流 | E10/E11；DizzyOnAvoid选特殊DB，命中结算读目标Avoided订单DB可置AvoidDizzy | 来袭HitBox→避免结果／订单DB→后续Impact→Dizzy | 订单保存与期限消费已闭合；继续固定Hook与Jab实际引用、外部停止和命中当刻SuperDizzy条件 | **阻塞主线**；avoid底稿与system-avoid-config-samples.csv |
| S05 招架按反馈分流 | E08/E09；破架势与条件专用眩晕模板不同 | 防守者GuardDB／来袭属性／当前架势→原攻击者Impact | Grunt原表DizzyOnParry全false，追实际AttackDB／缓存覆写；不能直接套模板 | **阻塞主线**；parry底稿 |
| S06 当前状态抗性 | E01；Base/Adv矩阵相同，InFight与Dizzy不同 | 当前最高状态→命中属性效果 | 9条状态差异候选的实际动作引用、Dizzy禁止顶层与SuperDizzy分支 | 直接关联；system-recovery-hitbox-state-candidates.json |
| S07 动作期间临时韧性 | E02；服务加减当前韧性，可绕过正常受击订单路径 | 服务bonus／起止→当前韧性→冲击力判定 | 普通／进阶具体动作的挂载、数值与时间段 | 直接关联；攻击冲击力韧性与伤害 |
| S08 受击动画决定状态时长 | E05/E08；ParryDizzy使用UseHitAnimDuration，普通stun20帧另列 | 命中模板／动画选择→持续状态时长 | 具体敌人／方向命中动画与最终duration | 直接关联；parry、recovery底稿 |
| S09 SuperDizzy量及可用性 | E09/E11；反馈量与状态gate都涉及它 | 防反反馈、目标gauge→是否可附加／重施眩晕 | 当前值、消耗／恢复消费者及分支语义；不把名称当结论 | 直接关联；avoid与resilience底稿 |
| S10 命中记忆与图反转 | E07；received memory类型3，avoid-success memory类型2；默认反转false已补证 | 近期攻击／闪避→候选测试 | 不同掩码的真实标签、竞争候选与成功反击蓝图条件 | 直接关联；敌人如何选择防御、recovery底稿 |
| S11 Deflected播放调整 | E12；读所有者GuardDB，按曲线影响攻击播放并收尾 | 反馈结果／原攻击订单→恢复时序 | EndOfStrike延迟、Grunt duration0路径；不能用主角0.6补值 | 直接关联；parry底稿 |
| S12 技能／神龛／覆盖 | E09；架势反馈读取ParryImpactOnStructureBonus；攻击组件可覆盖 | 角色属性／来袭数据→最终反馈量 | 固定成长版本和各覆盖写入者，再给最终数值 | 后续扩展；parry底稿 |
| S13 姿态／命中段／缓存版本 | E13；N44不同槽指不同动作；缓存优先原表 | 输入节点、姿态、AttackDB→实际HitBox | 固定具体槽／条件覆写与缓存生命周期；避免合并两种伤害 | 直接关联；玩家输入图、版本表 |
| S14 成功闪避后的玩家输入层 | MainChar_Avoid_AvoidDB：AllDefensiveOptions，延迟0.08秒Punishable_AvoidSuccess | 玩家成功闪避→玩家动作许可 | 层具体覆盖与反击节点条件；不推导敌方不能防御 | 直接关联；avoid底稿 |
| S15 架势崩溃独立分支 | E08/E09；能直接改变反馈与状态路径，且有独立最长stun条件 | 当前架势／反馈→崩溃状态与恢复 | 相同招式不同初始架势对照；查guardbreak状态时间／动作 | 直接关联；综合机制招架分流 |
| S16 群体票据与状态反馈 | 已有EndCombo清理、倒地／起身和冷却接口 | 个体状态／连段结束→票据或角色调度入口 | 完整配额、评分、释放与接替，待个体主链后展开 | 后续扩展；群体AI与状态反馈、notes/group-ai-state.md |
| S17 同数值不同枚举 | EHitDismissReason输出11，EComboEndReason也有11但不同类型 | Hit过滤→下游消费 | 前者PDB无成员，需真正枚举身份／消费者；不能据此说结束PunishableAvoided连段 | 后续扩展；avoid底稿 |

“底稿”对应研究根目录 `notes/recovery-system-chain.md`、`notes/parry-system-chain.md`、`notes/avoid-system-chain.md`。证据编号与准确RVA集中在[[02实现/连续受击与反击追击的系统链]]。

## 当轮验收与下一项工作

| 验收项 | 本轮状态 | 下一项必要取证 |
|---|---|---|
| 脱离原因 | 状态退出、Hitted恢复层、AI选择各自入口明确；最终连续命中刷新／AI消费许可链未全闭合 | S01→S03，先找Hitted计时更新和层查询 |
| 追击原因 | 闪避特殊DB与AvoidDizzy、招架模板和反馈分流已定位 | S04／S05，闪避订单保存与计时已闭合；继续固定实际命中行、提前取消及状态刷新 |
| 共享与分流 | 共用Impact／状态／恢复逻辑；三入口差异单独列出 | 固定同一追击版本，避免拿不同招式解释状态差异 |
| 敌人差异 | 同受击DB、同矩阵；不同Dizzy限制和情境图 | 对上Normal0实际原型及其动作引用，运行实例仍未观测 |
| 扩展线索 | 统一登记作用、证据、关联、缺口和优先级 | 随新证据合并条目；不把S12/S16/S17升级成本轮必须解决 |
| 实战 | 方案已写入综合机制，未执行 | 静态仍可推进；不会自行启动运行时操作 |
''')
# Surface the integrated chain from the existing themes without replacing detailed user content.
for topic in ['受击硬直与脱离','敌人如何选择防御','防反与闪避反击后的追击','攻击冲击力韧性与伤害','群体AI与状态反馈']:
 for folder,other in [('01机制','02实现'),('02实现','01机制')]:
  rel=folder+'/'+topic+'.md';p=V/rel;s=p.read_text(encoding='utf-8-sig')
  marker='## 综合系统研究更新'
  if marker not in s:
   s+='\n'+marker+'\n\n本主题与其他机制的共同流程、实际分流及本轮证据更新，集中见[['+folder+'/连续受击与反击追击的系统链]]；扩展因素见[[00索引/系统线索与关系图]]。正文中的早期待解项以综合页最新证据为准。\n'
   put(rel,s)
home='00索引/首页.md';s=(V/home).read_text(encoding='utf-8-sig');s=s.replace('## 阅读入口','''## 当前主线

| 阅读内容 | 入口 |
|---|---|
| 连打脱离、招架追击、闪避追击的共享与分流 | [[01机制/连续受击与反击追击的系统链]] |
| 对应数据与简要执行逻辑 | [[02实现/连续受击与反击追击的系统链]] |
| 所有已遇因素、确定／候选连接、未解问题与优先级 | [[00索引/系统线索与关系图]] |

已补到条件式招架反馈、闪避属性分流、持续状态限制、最长硬直策略及恢复许可回收。连续命中最终刷新、普通招架实际配置和恢复后AI最终时序仍未全闭合；见系统索引的验收表。未启动游戏。

## 阅读入口''',1)
s=s.replace('有防御成功施加受击结果的分支；具体状态和窗口未解','招架模板分流与闪避AvoidDizzy入口已定位；实际订单／窗口仍需核对')
put(home,s)
progress='00索引/研究进度与问题.md';s=(V/progress).read_text(encoding='utf-8-sig')
s=s.replace('## 当前成果','''## 综合主线的最新进度

当前按[[01机制/连续受击与反击追击的系统链]]推进，逐项验收、线索优先级与下一项取证见[[00索引/系统线索与关系图]]。以下早期列表保留历史范围；本轮已补证的内容包括LongestStun消费、恢复层Push/Pop、基础测试反转默认false、条件招架反馈模板与闪避AvoidDB分流。尚未完整闭合的静态调用继续保留，不用运行时猜测补齐。

## 当前成果''',1)
s=s.replace('| AI 记忆测试的部分反转字段缺省值 | 不补默认 false，不写成确定攻略 |','| AI 测试反转缺省值 | 已由基础类构造／反射／布局补证默认false；具体资产显式覆写与其他竞争条件仍需核对 |')
put(progress,s)
# Add the newly encountered level-override factor, preserving the static-candidate boundary.
rel='00索引/系统线索与关系图.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('“底稿”对应研究根目录', '| S18 按状态覆写攻击效果等级 | FHitboxDataRow.m_AttackPropertyLevelOverrides，PDB偏移+472；GetAttackPropertyLevel参与读取；原导出部分Map仍保留未解码原始摘要 | 当前状态不只影响防守抗性，也可能选择攻击侧等级覆写 | 对具体样本确认映射为空或解码；未解析的不能按基础等级保证结果 | 直接关联；E01与玩家字段中文说明 |\n\n“底稿”对应研究根目录')
put(rel,s)
rel='01机制/连续受击与反击追击的系统链.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('等级和冲击力是两套判断，不是伤害大小的别名。','等级和冲击力是两套判断，不是伤害大小的别名。下表按已提取基础等级列候选；按状态的攻击等级覆写、HitBox缓存及运行时状态未核清时，不当作最终结果。')
s=s.replace('| 状态刷新 |','| 普通硬直合并策略 | 已有Hitted时，最长硬直策略或AlreadyGuardBroken可取本次stun与旧剩余时间的最大值；Grunt最长策略为false | 该分支已核对，但不证明每次新击都覆盖旧计时；TimeSinceLastHit消费者仍缺 |\n| 状态刷新 |')
put(rel,s)
# Correct known inaccurate owner/condition claims in prior technical notes; preserve backups.
for rel in ['notes/counter-punish.md','notes/stun-ai-defense.md']:
 p=R/rel;s=p.read_text(encoding='utf-8-sig');b=backup/Path(rel);b.parent.mkdir(parents=True,exist_ok=True)
 if not b.exists():shutil.copy2(p,b)
 if rel.endswith('counter-punish.md'):
  s=s.replace('（传入目标的 `UAttackPropertiesResistanceDB`），随后 `ApplyImpact` 并调用目标 `AFightingCharacter::Hitted`','（resistance override 实参为 null，由函数内部查询），随后在原攻击者组件上 `ApplyImpact`；紧随其后的 `AFightingCharacter::Hitted` 调用对象则是原防守者')
 else:
  s=s.replace('only when that value is not Unreal’s invalid enum sentinel','only when that value is nonzero')
  s=s.replace('while the target remains stunned','while the AI owner remains stunned')
  s=s.replace('`m_bInverted` omitted; value not independently verified','`m_bInverted` omitted; native base-test default false confirmed in recovery-system-chain.md')
 s+='\n\n## 2026-10-28 综合研究接续\n\n最新证据和先前归属／默认值修正见 `notes/parry-system-chain.md`、`notes/avoid-system-chain.md`、`notes/recovery-system-chain.md`；用户阅读入口为知识库综合系统篇。未闭合处以新底稿的具体缺口为准。\n'
 p.write_text(s,encoding='utf-8',newline='\n')
layoutp=R/'inventory/vault-layout.json';layout=json.loads(layoutp.read_text(encoding='utf-8'))
for rel in changed:
 if rel not in layout['documents']:layout['documents'].append(rel)
topic='连续受击与反击追击的系统链'
if topic not in layout['topics']:layout['topics'].append(topic)
layoutp.write_text(json.dumps(layout,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
report={'updated':datetime.datetime.now().astimezone().isoformat(),'documents':sorted(set(changed)),'backups':str(backup),'not_run':['game','runtime tracing','LIAN modification']}
(R/'inventory/system-chain-notes-manifest.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps(report,ensure_ascii=True))
