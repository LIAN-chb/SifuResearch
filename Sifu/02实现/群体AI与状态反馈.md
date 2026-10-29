# 群体AI与状态反馈：简要实现

[[00索引/首页|返回首页]] · [[00索引/术语与证据说明|术语与证据]] · [[01机制/群体AI与状态反馈|阅读机制]]

本页保留理解机制所需的数据与执行入口，详细反汇编和偏移留在研究底稿。静态核对不等于实战验证。

对应：[[01机制/群体AI与状态反馈|机制说明]]。

`FAIAttackTicketManager` 的目标战斗状态变化回调，明确将倒地状态映射到目标倒地／目标起身情境。已核对本地枚举与实际分支。

新增核对：`OnAttackerComboEnded` 调用 `SetIsCandidateAttacking(false)`；后者按 Actor 更新候选者标记并维护正在攻击的数量，在零与非零之间切换 CandidateAttacking 情境。该接口不等同于释放全部票据，也不保证别人马上接替。

50 个攻击票据资产中保存了数量、角色掩码、冷却等。票据重置冷却还会按 `EMcDominationGaugeSteps` 选配置，这与普通／简单／困难难度不是同一个索引。全局同时出手数、申请和释放时点、情境对配额的具体修改尚未完整恢复。

定位见研究目录 `notes/group-ai-state.md` 及 `inventory/group-ai-state-disassembly.json`、`inventory/group-ai-ticket-disassembly.json`。

本机难度枚举顺序是 Normal=0、Easy=1、Hard=2，不能凭常见排列猜测数组索引。

## 群体反馈的简要调用关系

| 事件 | 接口 | 已核对的结果 |
|---|---|---|
| 攻击者连段结束 | OnAttackerComboEnded → SetIsCandidateAttacking(false) | 按 Actor 查候选者，更新 m_bIsAttacking 与计数 |
| 计数零 → 非零 | ActivateJokerSituation(CandidateAttacking) | 激活有关情境 |
| 计数一 → 零 | DeactivateJokerSituation(CandidateAttacking) | 取消有关情境 |
| 目标倒地状态变化 | OnDefenderFightingStateChanged | KnockedDown=3 分支按回调布尔值选 TargetKnockedDown=11／TargetGettingUp=12 |
| 票据冷却重置 | FAIAttackTicket::ResetCooldown | 按 domination 阶段配置选时长与偏移，再调用基础票据逻辑 |
| 所有者释放入口 | ReleaseOwnedTicket、ReleaseAITicketsInternal | 存在筛选、间接调用及 LaunchCombo 参数路径；未闭合完整释放语义 |

EndCombo 的结束广播还受原票据名等条件限制。票据管理器的注册绑定、申请、释放、冷却触发与最终候选评分，需要继续核对；“结束广播”不能直接改写为“所有票据无条件释放”。

## 两类索引分开记录

| 索引 | 已知取值／作用 | 不应混用 |
|---|---|---|
| EGameDifficulty | Normal=0、Easy=1、Hard=2 | 普通／简单／困难配置 |
| EMcDominationGaugeSteps | 冷却重置按相应阶段取配置；本分支检查索引小于 4 | 不能当成上面的难度数组 |
| EAIAttackTicketJokerSituation | 倒地、起身、候选者攻击中等情境 | 是情境类型，不是同时出手人数 |

## 证据入口

| 文件 | 用途 |
|---|---|
| notes/group-ai-state.md | 已核对的群体状态、连段结束、冷却与释放边界 |
| inventory/group-ai-state-disassembly.json | 状态与连段相关函数 |
| inventory/group-ai-ticket-disassembly.json | 结束反馈与冷却函数 |
| inventory/impact-resilience-application-disassembly.json | 包含 SetIsCandidateAttacking |
| exports/ai-attack-tickets.json | 已提取的攻击票据配置 |
| inventory/stun-state-type-layouts.json | 候选者、票据和情境枚举布局 |

先补个体受击／恢复，再追票据调度，是为了把“敌人不出手”区分为自身受控、没有动作许可、没被选中或票据仍在冷却等不同原因；后面这些具体场景还没有全部证实。

## 不同配置查表

本篇解释基础规则。不同角色、武器、动作与状态的保存配置单独维护，不再只靠正文少量例子表达覆盖范围。

| 配置集合 | 查找内容 |
|---|---|
| [[03配置/群体票据/索引]] | 50 个攻击票据的数量、角色掩码和冷却配置 |
| [[03配置/敌人原型/索引]] | 各原型本层保存的群体／动作配置 |

统一边界见 [[03配置/覆盖范围与读表说明]]。保存值、最终实战值和未解码项分别标记。

## 综合系统研究更新

本主题与其他机制的共同流程、实际分流及本轮证据更新，集中见[[02实现/连续受击与反击追击的系统链]]；扩展因素见[[00索引/系统线索与关系图]]。正文中的早期待解项以综合页最新证据为准。
