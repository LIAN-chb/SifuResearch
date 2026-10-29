# 群体 AI：连段结束与状态反馈（静态取证）

目标 EXE SHA-256：a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254。函数边界由匹配 PDB 提供。未启动游戏。

## 连段结束反馈

FAIAttackHandler::EndCombo（RVA 0x1881e60）会在原持有票据名非 None 的条件下广播 OnComboEnded。FAIAttackTicketManager::OnAttackerComboEnded（0x18598f0）将该 AI 的 Actor 传给 SetIsCandidateAttacking，布尔值 false。

SetIsCandidateAttacking（0x1868480）按 Actor 查找候选者；其 m_bIsAttacking（候选者 +0x90）与新值不同时更新，并维护管理器 +0x2b1 的计数。计数由零变为非零时激活 CandidateAttacking=4 情境；由一降为零时取消该情境。候选者字段由 inventory/stun-state-type-layouts.json 的 FAIAttackCandidate 布局核对。

因此“个体停止连段”存在反馈到群体调度情境的实际接口；这不能直接等同于释放全部票据，更不能推出另一个敌人立即接替。是否绑定到当前管理器、具体接替者和配额仍须结合初始化、候选评分、票据申请及配置核对。

## 目标倒地与起身

OnDefenderFightingStateChanged（0x185c690）只在 EFightingState=3（KnockedDown）分支处理：回调布尔值 true 选择 Joker 情境 11（TargetKnockedDown），false 选择 12（TargetGettingUp），并将第三参数 false 传入 ActivateJokerSituation。这是实际代码映射；该布尔值在上游事件中的完整语义尚未另行追踪。

OnDefenderOrderStateChanged（0x185c6b0）还按订单类型映射多个情境；函数尾部包含跳转表，不能把表数据的反汇编当成指令。此轮不把尚未完整核对的订单类型映射写入知识库。

## 冷却与释放入口

FAIAttackTicket::ResetCooldown（0x1866dd0）读取 FAIManager::GetDifficultyLevelStep，索引小于4时从 FAttackTicketConfig::GetCooldownFromGaugeStep 取得冷却时长及偏移，再调用基础票据的 ResetCooldown。这里的 EMcDominationGaugeSteps 与普通难度枚举 EGameDifficulty 不是同一维度，不能混写。

基础 FAITicket::ResetCooldown（0x1899590）清除 enabled 标记，并依据配置与随机数设置冷却计时。ResetCooldown 存在并不证明每次中断都会调用它。

ReleaseAITicketsInternal（0x18641e0）按票据枚举和持有者 Actor 筛选后调用虚方法；虚方法语义及所有调用入口尚未闭合。ReleaseOwnedTicket（0x1898660）构造参数后走 LaunchCombo；它不是一句直接释放全局队列。此轮不宣称 EndCombo 无条件释放全部攻击票据。

## 原始依据

- inventory/group-ai-state-disassembly.json（7个函数输出，含 EndCombo 两个重载）
- inventory/group-ai-ticket-disassembly.json（4个函数输出）
- inventory/impact-resilience-application-disassembly.json（包含 SetIsCandidateAttacking）
- logs/group-ai-state、logs/group-ai-ticket、logs/impact-resilience-application
- inventory/stun-state-type-layouts.json 的 FAIAttackCandidate、FAITicket、EAIAttackTicketJokerSituation 等布局／枚举。

下一步：初始化绑定 → 票据申请／候选评分 → 所有者释放与冷却 → 具体配置的围攻节奏。先保留已确认的状态反馈，不提前给出全场出手配额。
