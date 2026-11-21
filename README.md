# SifuResearch

本目录是《师父》解包与机制研究的长期工作区；原游戏只读。

跨对话入口见 [PROJECT.md](PROJECT.md)，协作规则见 [AGENTS.md](AGENTS.md)。当前成果与下一步以 [研究进度与问题](Sifu/00索引/研究进度与问题.md) 和 [解包与解析进度](Sifu/00索引/解包与解析进度.md) 的最新记录为准。

首次了解历史背景可读 [研究报告](notes/研究报告.md)；续接研究先查 [批次交接索引](notes/handoffs/README.md)，按 [研究续接流程](notes/research-workflow.md) 判断复用与重跑。外部来源见 [external-research.md](notes/external-research.md)。

- tools/：已下载并审阅的工具、源码、发布信息与校验文件。既有Python/Visual Studio仅作为运行环境复用。
- scripts/：可重复执行的本地只读分析脚本，写入仅指向此研究目录。
- extracted/：按需解出的原始配置和资产。
- inventory/：版本标识、清单、哈希、符号、类型和解析中间结果。
- exports/：面向研究主题的CSV/JSON。
- notes/：报告、范围、证据与未验证事项。
- notes/batches/<批次ID>/：批次规格、任务与验收清单；已归档攻击票据批次见 [规格](notes/batches/20261102-敌人AI票据-01/spec.md)。
- adr/：用户决策、选择理由、适用边界与历史关系；见 [决策索引](adr/README.md)。
- 研究管理：见 [工具矩阵](notes/tool-capabilities.md)、[方法复盘](notes/retrospectives/README.md)、[版本管理](notes/version-control.md)；阅读版见 [项目工作流与规则](Sifu/项目工作流与规则.md)。
- logs/：工具输出与静态反汇编。

根目录的文件归属与迁移验收见 [工作区目录约定](notes/workspace-layout.md)；协作规则的分层与维护见 [规则维护流程](notes/rule-maintenance.md)。

重跑：使用 `D:\Programes\PY\python.exe` 执行 scripts 中相应脚本；无须启动游戏。脚本内游戏路径绑定本机Epic安装路径。索引/导出脚本会更新本研究目录的同名生成结果；repak提取脚本不启用强制覆盖，重复提取需先确认已有输出范围。不要对其他构建复用这里的EXE地址。

执行顺序：index_pdb.py、index_pak.py、extract_research_assets.py、parse_research_assets.py、parse_tagged_exports.py、export_findings.py。inspect_types.py生成类型布局，inspect_callbacks.py生成有真实PDB范围的反汇编；无需全量重跑才能查看已有结果。

目前以静态取证推进，完整源码恢复、完整 AI 算法重构和实战数值验证尚未完成。后续任务从进度页续接。
