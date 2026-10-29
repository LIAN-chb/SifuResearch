# 连续受击与反击追击的系统链

[[01机制/连续受击与反击追击的系统链|返回完整规则主文]] · [[03配置/受击案例配置对照#通用规则的字段中文说明|字段中文说明]]

本篇只回答规则在哪实现。玩家是攻击方、敌人是受击方；招架／闪避入口另注明。字段可读、静态路径接通与实际触发分别看待。

## 规则与实现定位

| 机制主文中的规则 | 当前构建的执行入口 | 已核对范围／取证底稿 |
|---|---|---|
| 防守结果改变效果判定；当前状态影响攻击覆写与抗性；剩余时间可能使效果降为普通Hit | `UHitComponent::ComputeImpactType` RVA `0x1A51F10`；`FHitboxDataRow::GetAttackPropertyLevel` RVA `0x197D3C0` | `notes/20261029-rules-resolution.md` R01–R03；先看GuardType，再看其实际进入的分支，不能只比较基础等级 |
| 生成普通／格挡／弹开对应攻击参数 | `UHitComponent::GenerateImpact` RVA `0x1A5A610` | 同底稿R01；普通格挡退让与Pushed状态分开 |
| 普通伤害先通知旧状态，再更新状态，最后通知此时的状态 | `UHitComponent::ApplyImpact` RVA `0x1A46D90`：调用点 `0x1A47165`→`0x1A47C7F`→`0x1A484C8` | `notes/20261029-rules-hit-count.md`；健康组件派生覆盖先调基类，委托绑定已接，不推广所有Impact |
| 累计伤害与次数分别更新；归组只约束命中通知一路 | `UDefenseComponent::OnDamage` RVA `0x1965280`；`OnHit` RVA `0x19653B0`；`InitializeComponent` RVA `0x19600C0` | 同计数底稿；OnDamage不读取攻击名、归组开关或bApplied，不将两路广播直接换算拳数 |
| 重复命中按状态和子状态转移旧累计，并重算时长 | `UHitComponent::UpdateFightingStateFromImpact` RVA `0x1A70A70`；`ApplyFightingStateFromImpact` RVA `0x1A46990` | `notes/20261029-rules-state-update.md`；duration来源与累计字段继承分开；特殊眩晕另有配置入口 |
| 状态剩余时间是duration减elapsed | `UDefenseComponent::BPF_GetFightingStateTimeLeft` RVA `0x194FFA0` | 同状态底稿；两个bool输出为存在／无限，不是存在／暂停 |
| 有限、未暂停状态按时间／累计条件自动移除 | `UDefenseComponent::TickComponent` RVA `0x196A130` | 同状态底稿；时间和伤害使用严格大于，次数使用达到；暂停／无限跳过该段检查 |
| 状态建立／移除时附加／回收自身许可上下文（既有E20） | `PushFightingState` RVA `0x1966D90`；`PopFightingState` RVA `0x1966130`；NPC `IsAvailable` 与 `UpdateDefenseNeed` | `notes/hitted-services-followup.md`；已核对Dizzy反应引用GenericNone，不推为所有敌人／子状态共用配置 |
| 普通受击恢复条件性通知AI（既有E23） | `OrderHitted::IsStunOrder` RVA `0x19FDB50`；`OnUpdate` 的 `0x1AE46E4–0x1AE47B1`；AI初始化订阅 `0x18B8177–0x18B81B2` | `notes/case-study-ordinary-20261028.md`；不是所有防御执行门的完整恢复 |
| 玩家闪避→敌人保留反应记录→后续玩家命中可进入眩晕 | `FilterHit` RVA `0x1957FF0`；`HandleOrderOverAttack` RVA `0x19C0590`；`OrderAvoided::OnStart` RVA `0x1ADE250`；后接GenerateImpact／状态更新 | `notes/avoid-system-chain.md`；敌人原命中段标记先选择AvoidDB，后续命中再读回，不把反应时间当眩晕时长 |
| 敌人的受招架记录可以参与玩家特殊选招条件 | `BP_TargetIsParryVictim.BPE_GetTargetNode` 有界字节码 | `inventory/20261029-parry-condition.json`；查询目标的ParryVictim，或目标Hitted中指定反馈命中行；不以此断言整套输入最终选招 |

## 数据如何对应

| 阅读概念 | 数据入口 | 注意事项 |
|---|---|---|
| 每个命中段的伤害、普通硬直与效果等级 | HitBox行及其中普通／Guard／Deflect参数；`FAttackPropertyLevel` 与按目标状态覆写 | 不同命中段、姿态版本、结果参数分别核对 |
| 敌人各状态的抗性、反应、许可与上限 | `UAttackPropertiesResistanceDB` 的状态抗性、`FPropertyReaction`、`FSuperDizzyReaction` | 父级、实例覆写与子状态均可能改变实际采用值 |
| 正在运行的状态记录 | `FFightingStateElement` | 保存duration、elapsed、pause／infinite、累计值与上限、攻击名、状态和子状态；它是动态记录，不是原始配置表 |
| 普通受击动作与恢复 | Hitted订单及其DB、恢复许可层和服务 | 与FightingState记录有关联，但不是同一对象 |

配置中文释义和既有普通／进阶数值位于[[03配置/受击案例配置对照]]。本批没有新增配置值，也没有把旧配置值认定为最终实战窗口。

## 尚未接通的执行条件

| 缺口 | 下一步必须核什么 |
|---|---|
| 普通Hitted期间，AI选定防御后实际能否启动 | 防御请求到动作／订单准入：具体拒绝条件及所属角色；与其他评估触发入口区分 |
| 状态重建后攻击名的初始值 | 新元素构造／初始化与后续OnHit写入；不能仅从没有传参就断定None |
| 持续性字段的作用 | 定位实际消费者，不凭Persistent／Priority字段名解释退出或覆盖 |
| 实战精确时序 | 玩家动作版本、实际命中段、命中时刻、敌人状态／许可／防御启动；静态结果不自动给出固定拳数 |

## 构建与证据保留

- EXE SHA256：`a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`。
- 匹配PDB GUID：`fdd64e0f-b9ed-4479-8fd8-efe0038b919d`，age 1。
- 本次规则证据汇总：`inventory/rules-20261029-batch.json`；计数／状态子批清单分别为 `inventory/rules-20261029-count-batch.json` 和 `inventory/rules-20261029-state-update.json`。
- 原E01–E23实现编目全文作为历史底稿保留于 `notes/reader-sources/20261029-rules/legacy-implementation.md`，详细偏移不再塞入规则正文。已有原始证据保留，未实战验证。
