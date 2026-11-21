# 任务清单：敌人 AI 攻击票据调度闭环（20261102-敌人AI票据-01）

## 阶段一：登记与取证

- [x] T1 新建 `notes/handoffs/20261102-敌人AI票据-01.md`（按 `TEMPLATE.md`）。
- [x] T2 在 `notes/handoffs/README.md` 追加本批索引行。
- [x] T3 运行 `python scripts/disassemble_research.py --group ai-ticket-20261102 --name ...`（16 个核心函数），确认退出码 0。

## 阶段二：静态链路

- [x] T4 申请与评估：`RequestPassiveTicket`、`RequestPassiveTicketInternal`、`EvaluateCandidates`、`EvaluateCanditatPerTicket`、`FilterCandidates`、`ComputeTestFactors`、`OnEvaluationFinished`。
- [x] T5 创建与持有：`CreateAllAttackTickets`、`AddAndSetupTicket`、`SetTicketEnabled`、`GetCandidateOwnedTickets`、`CanOverrideWithTicket`。
- [x] T6 释放：`ReleaseAITicketsInternal`、`ReleaseOwnedTicket`，确认虚方法语义与释放范围。
- [x] T7 冷却：`TickCooldown`、`SetTicketsCooldownTimer`，交叉核对 `exports/ai-attack-tickets.json` 的难度槽位。
- [x] T8 交叉核对角色掩码与 50 套票据分布，标注已证实位含义与未知项。

## 阶段三：落盘

- [x] T9 写 `notes/20261102-攻击票据调度.md`（证据、推断、替代解释、反证、未知）。
- [x] T10 写 `Sifu/02实现/攻击票据调度闭环.md`（函数＋RVA＋哈希＋调用关系）。
- [x] T11 写 `Sifu/01机制/敌人AI/攻击票据调度闭环.md`（自然语言＋分层流程图，单篇主读）。
- [x] T12 写 `Sifu/01机制/敌人AI/00阅读入口.md`。
- [x] T13 改 `Sifu/01机制/群体AI与状态反馈.md`：专题附录横幅＋指向新主读篇。
- [x] T14 更新 `Sifu/03配置/群体票据/索引.md`、`Sifu/03配置/覆盖范围与读表说明.md`。
- [x] T15 更新 `Sifu/00索引/首页.md`、`研究进度与问题.md`、`系统线索与关系图.md`（S16）。
- [x] T16 更新 `inventory/vault-layout.json` 的 `directories`、`documents`、`topics`。

## 阶段四：验证与收尾

- [x] T17 运行 `python scripts/verify_knowledge_vault.py`，修复至通过。
- [x] T18 回填交接的执行与产物、证据变化、失败与验证、断点与下一步。
- [x] T19 `git status --short` 核对后仅显式暂存本批文件。
