from pathlib import Path
import json,hashlib,datetime
R=Path(r'E:\ProgrameFiles\SifuResearch');V=R/'Sifu';B=R/'notes/vault-backups/followup-unpacking-20261028'
changed=[]
def put(rel,s):
 p=V/rel;old=p.read_bytes();b=B/(hashlib.sha256(old).hexdigest()[:10]+'-'+p.name)
 if not b.exists():b.write_bytes(old)
 p.write_text(s.rstrip()+'\n',encoding='utf-8',newline='\n');changed.append(rel)
def section(s,t,b):
 mark='\n## '+t+'\n'
 if mark not in s:return s.rstrip()+mark+'\n'+b.strip()+'\n'
 a=s.index(mark);e=s.find('\n## ',a+len(mark));return s[:a]+mark+'\n'+b.strip()+'\n'+('' if e<0 else s[e:])
rel='01机制/连续受击与反击追击的系统链.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('当前最明确的新连接是：**特定攻击被成功闪避后，会选择一套让后续命中附加眩晕的配置；成功闪避与反击命中分工不同。**','现在已接通一条完整的条件链：**特定攻击被成功闪避→后续反击可施加Dizzy→Grunt的Dizzy动作许可上下文让AI防御查询退出→移除Dizzy时回收该上下文。** 普通连续受击另有取消旧Hitted、创建新Hitted与开放恢复许可的管线；两种计时不能混为一体。')
s=s.replace('| 尚缺        | 连续命中如何刷新各计时、实际下一次防御时序        | 固定敌方实际命中行／缓存覆写，闭合普通招架的具体反馈                                | 已闭合原攻击者订单保存与倒计时；具体招式引用、外部提前取消及完整追击许可仍待核对     |','| 尚缺 | 特殊刷新／预测分支与实际首次防御帧序 | 当前三份实际攻击引用已核；缓存写入与普通反馈的完整时序仍缺 | Dizzy至AI防御许可链已闭合；Avoided服务条件字节码、外部提前取消及命中当刻状态仍缺 |')
s=s.replace('  E -. 具体动作许可与调度时序待接 .-> AI[AI预测下一击并选防御候选]\n  L -. 具体AI查询待接 .-> AI','  S --> N[Dizzy上下文以GenericNone覆盖动作许可]\n  N --> Z[四项防御动作均不可用时AI退出防御更新]\n  E --> U[移除该状态上下文]\n  U --> AI[AI预测下一击并经过许可与防御图筛选]\n  L --> AI')
s=s.replace('该分支已核对，但不证明每次新击都覆盖旧计时；TimeSinceLastHit消费者仍缺','正常无前置Hitted的旧单取消／新单建立已确认；TimeSinceLastHit消费者与特殊序列仍缺')
s=s.replace('正常无前置Hitted的取消／新建已接通；特殊序列、冻结／预测及AI消费许可仍需分别核对','正常无前置Hitted的取消／新建与AI消费许可已接通；特殊序列、冻结／预测及逐帧调度仍需分别核对')
s=s.replace('该订单DB是否被具体Grunt实例采用、条件与服务怎样叠加，仍需追默认订单选择和服务执行。','Grunt_Base组件明确同时引用全局BP_OrderDB与Grunt_OrderDB；全局表包含Avoided／Deflected。两订单各有3项服务，包括GenericNone覆盖层；但IsPlayerCondition实际返回字节码尚未解码，不能仅凭条件名保证该层在所有具体NPC实例激活。详见[[03配置/订单与服务/Avoided与Deflected订单服务]]。')
s=s.replace('未解问题已缩到实际命中行／覆写、特殊刷新分支、订单提前取消及AI最终调度','未解问题已缩到条件字节码／运行时覆写、特殊刷新分支、订单提前取消及AI最终调度')
s=section(s,'眩晕如何阻止防御，退出后为何仍不是必然反击','''以下链条对当前Grunt_Base／Adv的Dizzy配置成立；它补上了“进入眩晕”和“AI不能选择防御”之间的桥，未将所有硬直都归为Dizzy。

| 环节 | 已确认规则 | 对追击／脱离的含义 |
|---|---|---|
| 状态推入 | Dizzy的SuperAvailabilityLayer指向GenericNone；PushFightingState创建BasicGameplay动作许可上下文，优先级1，并用SET写入掩码 | 默认上下文优先级0；新状态层排在它前面，不是把默认全部动作与限制做OR合并 |
| 哪些动作保留 | GenericNone只保留Look、MouseLook、DizzyReduction、ReplayMenu | Guard／Parry／Dodge／Avoid都不在其中；DizzyReduction的名字不证明玩家或AI实际如何缩短眩晕 |
| AI实际读哪一层 | NPC的角色IsAvailable包装函数先检查移动组件，再读取BasicGameplay当前首个上下文；AI传入的Invalid上下文13不会在此直接当成“全允许” | 这条路径确实会读到上述状态上下文，不能绕过角色包装去解释原始管理器 |
| 防御更新怎样退出 | UpdateDefenseNeed先有来袭预测、最高状态白名单等条件；四项防御动作全不可用时返回；正在准备攻击另有退出分支 | Dizzy本身在状态白名单中，但动作许可仍可把它挡住；“状态允许评估”不等于“可以防御” |
| 机会怎样结束 | 移除Dizzy时，状态保存的回调回收它创建的上下文；退出还可能包含恢复订单／条件调度 | 时间、启用的伤害／命中限制及其他移除路径会结束该限制；不保证退出同帧就格挡 |
| 恢复后怎样选择 | 下一次来袭预测→状态／动作许可／准备攻击检查→防御图候选与测试→验证请求 | 恢复许可只是必要环节；实际格挡还是反击还取决于记忆、条件、竞争候选和调度 |

本链前提是该Dizzy上下文仍为实际优先读取上下文；其他同／更高优先级上下文与具体实例覆写应单独核对。详见对应实现E20。普通Dizzy的Base3秒／Adv1.5秒是基础配置，不是最终保证时长。

**两段机会现在可以分开解释**：Avoided订单保存特殊配置的短窗口决定反击能否进入Dizzy；进入后，Dizzy自己的持续与累计退出条件决定其状态许可层保留多久。第一个订单结束，不自动令第二个状态及其许可层同刻消失。''')
s=section(s,'实际招架样本与敌人反击候选','''| 核对对象 | 本轮结果 | 解释边界 |
|---|---|---|
| Grunt Hook／BaseballHook／Uppercut实际攻击引用 | AttackDB、对应命中段和HitBox已对上；三行均可招架、DizzyOnParry=false、DizzyOnAvoid=true、PlayAvoidedOrder=true | 当前保存配置不满足专用招架眩晕模板分支；运行时缓存可被写入，不能说永远没有覆写 |
| Base／Adv防御成功反击 | 各3条动作父路径已展开；Push分支两者均为外层10秒／raw mask3，内层3秒／raw mask2 | 已纠正旧表把Adv内层误记为10秒；掩码不补造标签，记忆时间不等于追击窗口 |
| 普通Hit路径的架势测试 | 测试读AI自身GuardRatio，Inferior分支为≤，配置阈值0.4 | 不把GuardRatio翻译为“剩余架势40%”，也不说只要过阈值必反击 |
| 成功反击动作 | 指向Parry反击组合蓝图，含票据30／31和CustomCombo入口 | 图内100%转移不保证票据被接受；入口后首个实际攻击映射尚未解码 |
| 攻击结束回调里的IsStun | 检查AI所有者自身；不是玩家是否硬直 | 不能用它证明“玩家硬直时敌人必定继续反击” |

逐行数值与全部6条父路径见[[03配置/AI防御/Grunt反击条件与动作]]；简要执行位置见对应实现E22。''')
put(rel,s)
rel='02实现/连续受击与反击追击的系统链.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('具体Grunt默认订单引用与服务叠加待证','Grunt_Base默认组件引用已对上；服务条件字节码与实际激活仍待证（E21）')
s += '''
## 状态许可与AI的新增桥

| 编号 | 已接通连接 | 证据与仍缺内容 |
|---|---|---|
| E20 | Dizzy配置→优先级1上下文SET GenericNone→NPC首上下文查询→四项防御全禁时退出→状态移除回收上下文 | `notes/hitted-services-followup.md`；PushFightingState `0x1966d90`，推上下文`0x1966efc`、SET `0x1966f3c`、写入`0x1966f51`；上下文排序`0x19ab240`；AFightingCharacter::IsAvailable `0x19c17d0`→ABaseCharacter `0x19a1af0`的NPC分支`0x19a1ce9`；UpdateDefenseNeed `0x18c9e50`。PopFightingState入口`0x1966130`，回调调用点`0x19662ad`→lambda `0x194dd30`，`0x194de94–0x194ded4`回收所存上下文。清单`inventory/followup-state-availability-disassembly.json`、`inventory/followup-state-removal-disassembly.json`、`inventory/followup-availability-wrapper-disassembly.json`；仍缺实际并存上下文与逐帧观测 |
| E21 | Grunt默认OrderDB→Avoided／Deflected各3项服务→状态／许可挂载 | `notes/order-services-followup.md`、`inventory/followup-order-services-packages.json`；配置见[[03配置/订单与服务/Avoided与Deflected订单服务]]。ForceFightingState OnStart `0x1b0bc90`、OnStop `0x1b0e3a0`；duration=-1由PushFightingState `0x196716e`设置无限位，Tick `0x196a2c7`跳过有限状态的到期检查，结束由Pop等生命周期控制；不能套用Dizzy3／1.5秒。IsPlayer条件实际字节码、8.0区间单位、各实例覆写仍缺 |
| E22 | 实际攻击引用／缓存写入口／反击父路径与AI自身测试 | `notes/parry-ai-followup.md`、`inventory/followup-parry-ai-assets.json`；表见[[03配置/AI防御/Grunt反击条件与动作]]。execBPF_SetHitboxRow `0x1c7fda0`；UStructureInfluenceTest::GetFloatValue `0x18e53a0`读取AI自身GuardRatio，UFloatInfluenceTest::RunTest `0x18f29f0`的Inferior为≤（setbe）。OnTargetAttackEnded `0x1894b90`检查AI所有者自身IsStun。尚未解实际缓存写参、CustomCombo首个攻击映射和票据运行时选择 |

上下文优先级与上下文内各层优先级是两级排序；不能将服务priority10／20和状态上下文priority1直接比较。配置服务的存在、native调用可达、运行时真正激活分别记录。以上为本机构建的静态连接，实战未执行。
'''
put(rel,s)
rel='00索引/系统线索与关系图.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('证据编号E01–E16','证据编号E01–E22')
s=s.replace('  L -. 具体AI查询与帧序待接 .-> D\n  Q -. 与最终选择时序待接 .-> P','  L --> AV[角色动作许可查询]\n  S --> SN[Dizzy优先上下文SET GenericNone]\n  SN --> AV\n  Q --> POP[回收状态上下文]\n  POP --> AV\n  AV --> DG[防御动作许可及准备攻击检查]\n  DG --> D\n  Q -. 实际下一次防御帧序待观测 .-> P')
s=s.replace('AI消费层的具体调用与最终帧序；查AIHittedRecovery的动作许可查询','E20已闭合NPC首上下文→四项防御动作gate；剩实际并存上下文、恢复层激活条件及最终帧序')
s=s.replace('正常无前置Hitted取消／新建与回收已闭合E17；剩+0x74消费者、特殊前置序列／冻结／预测及AI层查询','正常无前置Hitted取消／新建与回收已闭合E17；AI查询已接E20；剩+0x74消费者、特殊前置序列／冻结／预测')
s=s.replace('继续固定Hook与Jab实际引用、外部停止和命中当刻SuperDizzy条件','Hook等3份引用已对上E22；剩Jab对照、外部停止、缓存覆写和命中当刻SuperDizzy条件')
s=s.replace('追实际AttackDB／缓存覆写；不能直接套模板','3份实际AttackDB已核E22；继续追缓存写参／普通反馈；不能直接套模板')
s=s.replace('不同掩码的真实标签、竞争候选与成功反击蓝图条件','成功动作6条父路径已接E22（Push内层Base／Adv均3秒mask2）；剩掩码标签、竞争候选、组合首攻击与票据接受')
s=s.replace('对上Grunt实际订单DB、激活条件与服务运行；不能把层名翻成禁止格挡','默认组件引用与6服务已接E21；剩IsPlayer条件字节码、8.0单位及具体实例激活；不能把顶层AllDefensiveOptions翻成禁止格挡')
anchor='\n“底稿”对应研究根目录'
a=s.index(anchor)
s=s[:a]+'''\n| S21 状态许可上下文与防御gate | E20；Dizzy→priority1／SET GenericNone；NPC实际读首上下文，四项防御全禁则退出更新 | 状态推入／移除→动作许可→防御请求 | 实际并存的同／更高优先上下文与首次防御帧序；不将Invalid13误当NPC全允许 | **阻塞主线已部分闭合**；综合机制“眩晕如何阻止防御” |
| S22 订单服务条件和时间基准 | E21；Avoided／Deflected各3服务，Force状态duration=-1，许可层有IsPlayer条件 | 服务范围／条件→Avoided状态、GenericNone或Parry取消层 | 解BPE_CanActivate实际返回及8.0范围单位；上下文与层内优先级分开 | **阻塞主线**；订单服务配置与order-services底稿 |
| S23 反击组合票据与入口映射 | E22；成功防御动作关联票据30／31、CustomCombo1／2 | 防御图→动作→组合入口→实际攻击 | 解首攻击映射与票据接受；不能把图内100%等同必反击 | 直接关联；Grunt反击条件与动作 |
| S24 DizzyReduction可用项 | E20；GenericNone允许此动作，但无本轮消费者证明 | Dizzy许可掩码→候选缩短状态接口 | 找到输入／AI消费者后才解释是否能缩短；当前不借名字归因 | 后续扩展；hitted-services底稿 |
'''+s[a:]
s=s.replace('特殊分支与AI消费许可链未全闭合','Dizzy至AI许可gate已闭合；特殊分支与实际首次防御帧序仍缺')
s=s.replace('继续查具体服务／条件与AI层查询','优先解IsPlayer服务条件，随后核8.0时间基准与实际上下文')
s=s.replace('继续固定实际命中行、提前取消及状态刷新','已核3份实际攻击行；继续缓存写参、提前取消及状态刷新')
s=s.replace('`inventory/system-chain-evidence-verification.json`','`inventory/system-chain-evidence-verification.json`；本批新增核查见`inventory/followup-unpacking-verification.json`')
put(rel,s)
rel='00索引/解包与解析进度.md';s=(V/rel).read_text(encoding='utf-8')
s=s.replace('| Grunt默认订单／Avoided与Deflected服务 | 复用已提取订单，按引用补父级／服务 | 以独立分支证据清单记录 | 对上具体Grunt引用和服务条件后才升级为确认 | 否 |','| Grunt默认订单／Avoided与Deflected服务 | 定向10份包及其引用清单，保留哈希 | 两订单各3服务、默认DB引用与条件字段已解析 | Force状态／许可层native生命周期已接；IsPlayer实际字节码和8.0单位未解 | 否 |')
s=s.replace('| 招架／AI反击动作 | 复用能力、实际AttackDB与动作，按需补蓝图 | 对象引用与字节码分别记录覆盖范围 | 防反模板分流与AI实际成功动作分别核对 | 否 |','| 招架／AI反击动作 | 实际AttackDB、命中表、条件与动作定向补取 | 3份攻击引用、Base／Adv各3条完整反击父路径 | AI自身GuardRatio≤0.4测试、缓存写入口已接；首攻击映射和缓存实际写参未解 | 否 |\n| Dizzy状态许可与AI防御 | 复用Base／Adv状态DB与许可资产 | GenericNone四项白名单、默认上下文和SET参数已核 | 状态上下文→NPC首上下文查询→防御gate→移除回收闭合；运行时竞争层未观测 | 否 |\n| 动画／通知时序 | 复用已提取动作资源与服务范围字段 | 保存范围可读；所有相关通知尚未定向补齐 | 8.0单位及具体服务生效区间仍待追，未称动画时序已接通 | 否 |')
s=section(s,'本批新增阅读入口','''| 阅读内容 | 入口 |
|---|---|
| 共用状态、许可与AI链 | [[01机制/连续受击与反击追击的系统链]] |
| 33条受击服务 | [[03配置/订单与服务/Hitted订单与服务]] |
| 6条闪避／弹开订单服务 | [[03配置/订单与服务/Avoided与Deflected订单服务]] |
| 实际攻击与6条反击父路径 | [[03配置/AI防御/Grunt反击条件与动作]] |

下一批最小取证：IsPlayerCondition的Kismet返回表达式与owner来源→OrderServiceFrameRange时间基准／通知→反击组合入口首攻击映射；遇到缺包仍先定向补取父级与直接依赖。主线之外的技能覆写、群体票据后续展开，不因本批查到入口就宣称完成。''')
put(rel,s)
for rel in ['00索引/首页.md','00索引/研究进度与问题.md']:
 s=(V/rel).read_text(encoding='utf-8');s=section(s,'本批补解包结论与下一步','''| 已完成的静态连接 | 阅读入口 |
|---|---|
| 普通无前置Hitted取消旧单、排新单、回收旧恢复层与服务 | [[01机制/连续受击与反击追击的系统链]] |
| Grunt Dizzy动作许可上下文阻断AI防御，并在状态移除时回收 | 同上“眩晕如何阻止防御” |
| 两份Hitted共33服务、Avoided／Deflected共6服务及Grunt默认引用 | [[03配置/订单与服务/索引]] |
| 3份实际招架／闪避攻击行、6条反击父路径与AI自身架势测试 | [[03配置/AI防御/Grunt反击条件与动作]] |

提取、解析、逻辑和实战四阶段分别列于[[00索引/解包与解析进度]]。优先余项是IsPlayer条件字节码、服务范围8.0的单位、缓存实际写入及反击组合首攻击映射。未运行游戏；不需要你现在操作。''');put(rel,s)
rel='03配置/配置索引.md';s=(V/rel).read_text(encoding='utf-8');s=section(s,'AI防御配置补充','实际攻击引用、命中段和6条成功反击父路径见[[03配置/AI防御/Grunt反击条件与动作]]；记忆窗口与受击／眩晕窗口分开阅读。');put(rel,s)
# Update evidence notes only with additional verified cross-links; preserve original analysis.
p=R/'notes/order-services-followup.md';s=p.read_text(encoding='utf-8');s+='''\n## 集成复核补充\n\nForceFightingState传入duration=-1的无限位已由PushFightingState `0x196716e` 与Tick `0x196a2c7` 接通；其状态生命周期经OnStop／Pop回收，不使用Dizzy3／1.5秒。NPC动作许可实际包装查询及AI gate见综合实现E20。服务自身IsPlayer条件仍未解，不能将Dizzy状态层的确定结论直接移植为所有Avoided服务必定激活。\n''';p.write_text(s,encoding='utf-8',newline='\n')
p=R/'inventory/followup-unpacking-documents.json';m=json.loads(p.read_text(encoding='utf-8'));m['documents']=sorted(set(m['documents']+changed));m['updated']=datetime.datetime.now().astimezone().isoformat();p.write_text(json.dumps(m,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({'updated_notes':len(changed)},ensure_ascii=True))
