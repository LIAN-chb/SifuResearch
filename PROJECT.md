# 《师父》解包与机制研究

这是持续跨对话推进的本地研究项目，工作目录为 `E:/ProgrameFiles/SifuResearch`。Codex 项目 `SifuReaserch` 与 Trae 工作区均指向此目录；客户端能力差异见[能力发现与复用](notes/capability-discovery.md)的“客户端能力映射”。

## 目标与边界

从当前本机游戏构建的资产、配置、匹配符号和静态代码中，逐步解释战斗与 AI 机制，产出可定位、可复查的中文知识库。按具体问题推进，完成度由证据和验收范围决定。

阅读目标是从游戏开发者角度恢复系统：定义数据模型、事件接口、状态转移守卫、字段更新与跨模块副作用。玩法现象和连招用于检验模型；正文以核心规格为主，配置、专题和取证作为附录。图中的转换标出条件，未知接口留缺口，判断由条件分支表达。

目前以连续受击、恢复、防御及反击追击的系统链为主线。当前进度：完整源码恢复、全资产解析和实战效果验证仍在推进；已有入口与对应系统的完成度分开记录。游戏与存档保持只读。

## 长期记录入口

| 内容 | 权威记录 |
|---|---|
| 对后续对话生效的协作规则 | [AGENTS.md](AGENTS.md) |
| 用户决定、选择理由、历史关系与复用边界 | [ADR 决策索引](adr/README.md) |
| 给用户浏览的项目全貌 | [项目工作流与规则](Sifu/项目工作流与规则.md) |
| 工具适用条件与失败边界 | [工具能力矩阵](notes/tool-capabilities.md) |
| 执行前如何发现、核实与组合现有能力 | [能力发现与复用](notes/capability-discovery.md) |
| 机制文档的表达规范、骨架与验收 | [机制表达](notes/mechanism-writing.md) |
| 实际方法经验与迁移条件 | [方法复盘](notes/retrospectives/README.md) |
| 本地 Git 范围与批次提交方式 | [版本管理](notes/version-control.md) |
| 接手、复用、失败记录、结论修订与验证流程 | [研究续接流程](notes/research-workflow.md) |
| 各批执行历史、断点和进行中写入范围 | [交接索引](notes/handoffs/README.md) |
| 当前成果、问题与最新下一步 | [研究进度与问题](Sifu/00索引/研究进度与问题.md) |
| 提取／解析／逻辑／实战阶段及解析缺口 | [解包与解析进度](Sifu/00索引/解包与解析进度.md) |
| 系统关系、取证线索与优先级 | [系统线索与关系图](Sifu/00索引/系统线索与关系图.md) |
| 术语、证据等级与解释边界 | [术语与证据说明](Sifu/00索引/术语与证据说明.md) |
| 知识库阅读入口 | [首页](Sifu/00索引/首页.md) |
| 环境、工具和目录说明 | [README.md](README.md) |

研究进度维护在上述进度页；批次执行历史保留在交接记录。本文件作为稳定入口，各批状态见进度页与交接。

## 常用命令

| 用途 | 命令 |
|---|---|
| 知识库检查 | `python scripts/verify_knowledge_vault.py` |
| 规则文风检查 | `python -B scripts/check_rule_style.py` |
| 补解包／系统链 | 先读 `scripts/verify_followup_unpacking.py`、`scripts/verify_system_chain_evidence.py` 的适用范围，再运行 |
| Git 开工检查 | `git status --short --branch` |
| 只读检查 | 按 `notes/research-workflow.md` 第 4 节复制到临时目录，输出写临时路径 |

## 一批工作的验收

按照[研究续接流程](notes/research-workflow.md)建立批次、核查复用条件、完成定向取证和验证，并留下交接。模板位于[批次模板](notes/handoffs/TEMPLATE.md)。静态完成与实战完成分别验收；未解决的问题保留断点并标状态。

## 新对话如何接手

在 `SifuReaserch` 项目打开本目录后新建对话，直接说明本轮目标，后续对话以本地规则、进度及证据为依据；改变研究方向时在对话中说明，并将决定回写到进度页。
