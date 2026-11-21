# 规格：敌人 AI 攻击票据调度闭环（批次 20261102-敌人AI票据-01）

## 目标

不写入游戏安装目录／存档，用本机匹配 PDB 的静态反汇编与已解析配置，接通“票据申请 → 候选资格／评分 → 持有 → 释放 → 冷却”的最小闭环，并落盘为知识库正文、实现证据、配置说明与批次交接。

## 已确认前提

- EXE SHA-256：`a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`（`inventory/pdb_overview.json` 记录的匹配构建）。
- 已解析 50 个攻击票据配置：`exports/ai-attack-tickets.json`。
- 已有类型布局：`notes/pdb-type-findings.md`（配置 288 字节、攻击票据管理器 696 字节、攻击票据 456 字节等）。
- 已有部分调用证据：`notes/group-ai-state.md`（连段结束、倒地／起身映射、冷却读取、释放入口）。

## 用户已定决策

1. **文档结构**：在机制二级目录下新建；实现篇由本批决定。
   - 新建 `Sifu/01机制/敌人AI/00阅读入口.md`
   - 新建 `Sifu/01机制/敌人AI/攻击票据调度闭环.md`（主读篇）
   - 新建 `Sifu/02实现/攻击票据调度闭环.md`（与既有 `02实现` 平铺约定一致）
   - 修改 `Sifu/01机制/群体AI与状态反馈.md`：加“专题附录”横幅，指向新主读篇
2. **共享文件**：全部允许修改首页、进度页、线索页与 `inventory/vault-layout.json`。
3. **取证范围**：先做核心 16 个函数（申请、评估、创建、启用、释放、冷却），角色票据管理器与其余符号留待后续批次。

## “反汇编”在此的含义

用 `scripts/disassemble_research.py` 读取 PDB 记录的地址与长度，让 dumpbin 只反汇编这些函数对应的机器码。得到的是汇编文本，用来确认函数实际比较了哪些常量、走了哪个分支、调用了谁；不是运行游戏，也不是导出配置。

## 反汇编清单（组名 ai-ticket-20261102，16 个）

| 函数 | RVA |
|---|---:|
| FAIAttackTicketManager::RequestPassiveTicket | 0x1865730 |
| FAIAttackTicketManager::RequestPassiveTicketInternal | 0x18657d0 |
| FAIAttackTicketManager::OnEvaluationFinished | 0x185d6a0 |
| FAITicketManager::EvaluateCandidates | 0x18829e0 |
| FAITicketManager::EvaluateCanditatPerTicket | 0x1882ee0 |
| FAITicketManager::FilterCandidates | 0x1884a40 |
| FAIAttackCandidate::ComputeTestFactors | 0x184a9a0 |
| FAIAttackTicketManager::CreateAllAttackTickets | 0x184b3a0 |
| FAIAttackTicketManager::AddAndSetupTicket | 0x18414f0 |
| FAIAttackTicketManager::SetTicketEnabled | 0x1868c40 |
| FAIAttackTicketManager::GetCandidateOwnedTickets | 0x1851200 |
| FAIAttackTicketManager::ReleaseAITicketsInternal | 0x18641e0 |
| FAIAttackHandler::CanOverrideWithTicket | 0x187c280 |
| FAIAttackHandler::ReleaseOwnedTicket | 0x1898660 |
| FAIAttackTicket::TickCooldown | 0x186dc60 |
| FAIAttackTicketManager::SetTicketsCooldownTimer | 0x1868e70 |

## 写入范围

| 文件 | 动作 |
|---|---|
| `notes/handoffs/20261102-敌人AI票据-01.md` | 新建批次交接 |
| `notes/handoffs/README.md` | 追加本批索引行 |
| `notes/20261102-攻击票据调度.md` | 新建取证底稿 |
| `Sifu/01机制/敌人AI/00阅读入口.md` | 新建 |
| `Sifu/01机制/敌人AI/攻击票据调度闭环.md` | 新建主读篇 |
| `Sifu/02实现/攻击票据调度闭环.md` | 新建实现证据篇 |
| `Sifu/01机制/群体AI与状态反馈.md` | 加专题附录横幅与指向 |
| `Sifu/03配置/群体票据/索引.md` | 补票据字段说明入口 |
| `Sifu/03配置/覆盖范围与读表说明.md` | 补票据字段口径 |
| `Sifu/00索引/首页.md` | 加 AI 目录入口 |
| `Sifu/00索引/研究进度与问题.md` | 更新群体 AI 行与下一步 |
| `Sifu/00索引/系统线索与关系图.md` | 更新 S16 |
| `inventory/vault-layout.json` | 同步新文档与新目录 |

产物：`logs/ai-ticket-20261102/`、`inventory/ai-ticket-20261102-disassembly.json`。

## 完成条件

- 每条结论绑定函数名＋RVA＋构建哈希，或资产路径＋字段名。
- 分别回答：
  - 申请的调用者与前置条件；
  - 候选筛选／评分的可证实顺序（不把字段名当策略）；
  - 票据持有的写入点与查询点；
  - 释放入口的虚方法语义，以及“是否等于全员释放”的边界；
  - 冷却计时的难度槽位与重置触发点；
  - 角色掩码位含义（能证实多少写多少）。
- 列出未闭合分支及其可推翻证据形态。
- 四阶段（已提取／已解析／已接通逻辑／已实战验证）逐条标注；本批不启动游戏。

## 不在本批范围

- 行为树／EQS／AI 动作资产全文解析。
- 武器票据、位置票据专题。
- 角色票据管理器完整评分（`FAICombatRoleTicketManager`）。
- 运行时实战与数值实测。
- 移动既有 `敌人如何选择防御.md`、`群体AI与状态反馈.md` 的物理位置。

## 验证步骤

1. `python scripts/disassemble_research.py --group ai-ticket-20261102 --name <逐个函数>` 退出码 0；`inventory/ai-ticket-20261102-disassembly.json` 记录 `exe_sha256` 与每段 `assembly_sha256`。
2. 逐段核对 `logs/ai-ticket-20261102/*.asm.txt` 中的比较常量、跳转与调用目标。
3. `python scripts/verify_knowledge_vault.py` 通过。
4. `git status --short` 确认只暂存本批文件。

## 待批准

以上结构与 16 个函数的取证范围确认后开始执行。
