# 连续受击与反击追击的系统链

[[01机制/连续受击与反击追击的系统链|机制与场景对照]] · [[00索引/系统线索与关系图|线索与未解问题]]

本篇只留数据入口与关键分支。完整寄存器、RVA、反汇编和提取过程分别在研究根目录的 `notes/recovery-system-chain.md`、`notes/hitted-stun-timer-dataflow.md`、`notes/parry-system-chain.md`、`notes/avoid-system-chain.md`。这些是本机构建静态证据，不是运行测试。

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
| E14 | 本次stun→结束时刻→Hitted内部计时 | ApplyImpact `0x1a47b0c–0x1a47b3d`、`0x1a47e85–0x1a47ed9`；OnStart `0x1adf95a–0x1adf9b9`、`0x1adfc3b–0x1adfc6c` | `notes/hitted-stun-timer-dataflow.md`；NetStruct.m_iTimeOfEnd+0x160。未覆盖时结束时刻含当前时间+instigatorFreeze+stun；OnStart用同步差／容器覆盖，减freezeFrames/30并下限1/30；后续有效分支再减freezeFrames/30×HittedFrozenPlayRate→HitTimeLeft。记录机器码，不推测两次扣减意图 |
| E15 | 原攻击者Avoided临时层添加与回收 | FilterHit `0x19585a1–0x1958688`；OnStop `0x1ae13ad–0x1ae13d7`；HandleOrderOverAttack `0x19c0590` | `inventory/system-avoid-orderdb.json`、`inventory/system-avoid-orderdb-exports.json`；OrderAvoided CDO.AvailabilityInfo→Guard/AllDefensiveOptions，priority10，另有条件及服务；Grunt_Base默认组件引用已对上；服务条件字节码与实际激活仍待证（E21） |

| E16 | 普通Dizzy基础时长→状态duration参数 | UAttackPropertiesResistanceDB::GetDurationOfFightingState `0x19f58b0`；UDefenseComponent同名getter `0x195bd30`；ApplyFightingStateFromImpact `0x1a46bc9–0x1a46bd7`、`0x1a46d35–0x1a46d5c` | `notes/avoid-system-chain.md`；Base/Adv m_DizzyReaction.m_Movement.m_fDuration=3.0/1.5秒，getter读取Reaction+0x1c；本次状态／动画覆盖与duration修正、旧状态保留另走分支，不能用基础值保证实战窗口 |

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
## 后续补解包与执行证据

| 编号 | 连接 | 精确入口与范围 |
|---|---|---|
| E17 | 普通无前置Hitted：构造新单→取消目标集合→旧单回收→新计时 | ApplyImpact `0x1a47eff–0x1a47f5e`；AFightingCharacter::PlayOrder `0x19c801a`；UOrderComponent::PlayOrder `0x1ae5027–0x1ae5144`、`0x1ae52b6/0x1ae52cb`、`0x1ae556b`；GatherActionTypeOrderIDs `0x1afa580`，谓词`0x1af24a0`；OrderBase::Process `0x1b121f6–0x1b12205`，OnCancel `0x1a006c0`→OnStop虚槽。详见`notes/hitted-queue-followup.md`及`inventory/followup-hitted-type-layouts.json` |
| E18 | 订单服务数组由不透明变为完整配置记录 | `inventory/followup-hitted-assets.json`：OrderHitted与OrderHittedGeneric的默认对象服务数30／3，8份tagged数据导出完整，2份类native后缀保持未解码。解析采用元素计数、内层tag和导出边界校验；服务实际激活需另核。阅读表见[[03配置/订单与服务/Hitted订单与服务]] |
| E19 | 历史解析失败与缺包分开 | `inventory/followup-gap-classification.json`：旧825条中696条为旧读取器未支持delegate属性tag、129条为native后缀；按Grunt／主角路径重试296条，289条字段边界完整、7份语音资源仍仅前缀且不阻塞主线。内部delegate／native数据仍可不透明；不是289条游戏逻辑已恢复 |

注意：PDB的GetSubType虚槽是+0x70，枚举2为BoundToAnimState；GetBaseType是另一槽+0x28。编译器折叠函数时dumpbin可展示别的共享符号别名，以匹配PDB范围和虚槽共同定位。

## 状态许可与AI的新增桥

| 编号 | 已接通连接 | 证据与仍缺内容 |
|---|---|---|
| E20 | Dizzy配置→优先级1上下文SET GenericNone→NPC首上下文查询→四项防御全禁时退出→状态移除回收上下文 | `notes/hitted-services-followup.md`；PushFightingState `0x1966d90`，推上下文`0x1966efc`、SET `0x1966f3c`、写入`0x1966f51`；上下文排序`0x19ab240`；AFightingCharacter::IsAvailable `0x19c17d0`→ABaseCharacter `0x19a1af0`的NPC分支`0x19a1ce9`；UpdateDefenseNeed `0x18c9e50`。PopFightingState入口`0x1966130`，回调调用点`0x19662ad`→lambda `0x194dd30`，`0x194de94–0x194ded4`回收所存上下文。清单`inventory/followup-state-availability-disassembly.json`、`inventory/followup-state-removal-disassembly.json`、`inventory/followup-availability-wrapper-disassembly.json`；仍缺实际并存上下文与逐帧观测 |
| E21 | Grunt默认OrderDB→Avoided／Deflected各3项服务→状态／许可挂载 | `notes/order-services-followup.md`、`inventory/followup-order-services-packages.json`；配置见[[03配置/订单与服务/Avoided与Deflected订单服务]]。ForceFightingState OnStart `0x1b0bc90`、OnStop `0x1b0e3a0`；duration=-1由PushFightingState `0x196716e`设置无限位，Tick `0x196a2c7`跳过有限状态的到期检查，结束由Pop等生命周期控制；不能套用Dizzy3／1.5秒。IsPlayer条件实际字节码、8.0区间单位、各实例覆写仍缺 |
| E22 | 实际攻击引用／缓存写入口／反击父路径与AI自身测试 | `notes/parry-ai-followup.md`、`inventory/followup-parry-ai-assets.json`；表见[[03配置/AI防御/Grunt反击条件与动作]]。execBPF_SetHitboxRow `0x1c7fda0`；UStructureInfluenceTest::GetFloatValue `0x18e53a0`读取AI自身GuardRatio，UFloatInfluenceTest::RunTest `0x18f29f0`的Inferior为≤（setbe）。OnTargetAttackEnded `0x1894b90`检查AI所有者自身IsStun。尚未解实际缓存写参、CustomCombo首个攻击映射和票据运行时选择 |

上下文优先级与上下文内各层优先级是两级排序；不能将服务priority10／20和状态上下文priority1直接比较。配置服务的存在、native调用可达、运行时真正激活分别记录。以上为本机构建的静态连接，实战未执行。
## 案例化改写与普通硬直事件E23

阅读主线已改为明确玩家／敌人主语的分支说明，实例见[[01机制/受击与追击案例]]；原E01–E22作为既有证据编目保留，不据编目数量宣称场景闭合。

| 编号 | 本批连接 | 原始定位与边界 |
|---|---|---|
| E23 | 普通Hitted计时→恢复层／硬直通知→订阅回调→条件防御重新评估 | OrderHitted::IsStunOrder `0x19fdb50`；OnUpdate `0x1ae46e4–0x1ae47b1`；UAIFightingComponent::InternalBeginPlay `0x18b8177–0x18b81b2`订阅；回调`0x18bc563–0x18bc5db`。详细见[[02实现/受击与追击案例]]及`notes/case-study-ordinary-20261028.md`。其他目标订单／可用性变化也能触发评估，普通硬直的全入口禁防未证明 |
