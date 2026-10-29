# 工具能力矩阵

用于按输入条件选工具，能力来自已有脚本与产物；2026-10-29 初建。本次检查源码和报告，没有重新运行解包或反汇编，也未逐项重验历史资产。版本未知的部分明确保留，迁移到其他项目先做小样。

| 工具／入口 | 输入与依赖 | 已有能力证据 | 限制与失败特征 | 新任务最小检查 |
|---|---|---|---|---|
| repak CLI 0.2.3；`scripts/index_pak.py`、`scripts/extract_research_assets.py` | 本机 PAK、适用密钥及已审阅工具 | `inventory/pak-overview.json` 记录当前 V11 PAK 索引成功，79253条文件项；仅为该构建历史记录 | 不解析资产语义；换包版本、加密方式或压缩配置须重验；脚本路径绑定本机 | 核包标识与工具版本，先试索引和一个目标包；不要先全量解出 |
| `tools/local_bounded_packages.py`；`scripts/parse_research_assets.py` | 观察到的 UE4 cooked 包头、uasset／uexp | `inventory/package-parse-overview.json` 记录3456包元数据及1656条边界完整结果 | 仅支持已观察的 -7／零 custom-version 布局；多导出、原生结构和未知数组不保证解码；缺字段不等于零 | 用当前包检查导出偏移、属性终止及剩余字节；脚本无独立发布版本，执行时记 SHA256 |
| `scripts/parse_tagged_exports.py` 与现有有界读表逻辑 | 已提取包、类型／引用元数据 | `inventory/deep-parse-overview.json` 历史记录17714对象、69表，825条 opaque／不支持导出 | 计数不是游戏完整覆盖；原生复杂类型、蓝图字节码仍可能不透明 | 固定对象做边界与引用检查；只接受大小／元素数一致的解析 |
| `scripts/followup_classify_gaps.py` | 旧失败记录、当前读取器、现有包元数据与提取结果 | `inventory/followup-gap-classification.json` 和重试对象清单 | tagged 边界完整不等于委托或 native payload 语义已解；历史／测试路径不等于必定废弃 | 先分类失败，再针对当前研究对象重试；输入不变不重复盲试 |
| `scripts/index_pdb.py` | 本机构建的 PE／匹配 MSF7 PDB | `inventory/pdb_overview.json` 记录 GUID／构建匹配、符号与类型入口 | 有符号不代表源码／行为已恢复；无符号项目不能照搬该路线 | 核 EXE／PDB 匹配及所需字段／函数范围；换构建重新分组 |
| VS dumpbin；`scripts/disassemble_research.py` | 本地 VS 路径、PDB函数边界、匹配EXE | `inventory/*disassembly.json` 留构建哈希、过程范围、输出哈希 | 当前源码路径含 MSVC 14.51.36231；不是本次运行版本探测。跳转表／填充可能被当指令；静态可达不等于实际执行 | 检查工具路径与版本、EXE哈希、函数范围；按问题指定 group 和 name |
| 知识库检查器 `scripts/verify_knowledge_vault.py` | 布局清单、知识库、静态证据和本机EXE | 历史报告 `inventory/knowledge-vault-verification.json`；本批会重新检查 | 验证链接、清单、语法及已覆盖哈希；不证明机制、图形渲染或实战正确 | 看覆盖范围，保留旧报告，再运行；不为无关管理文档例行重跑 |
| Git 2.49.0.windows.1 | 本地文本、脚本、选定清单；本批实测版本 | 本批初始化、基线提交和状态核查见交接及报告 | Git只保存纳入提交的内容；不是原始资产备份，当前无远程备份 | 用 status／diff 查看范围，逐路径提交；检查 ignore 是否遗漏需保存的源文件 |

## 维护规则

新工具、工具升级、格式变化或新失败出现时更新相应行，关联批次和复盘。优先描述输入、能证明什么、失败特征与重试条件；不能仅列“可用”。本机版本、脚本哈希和工具来源仍记录在执行批次，本表只索引，避免重复维护大清单。

新项目先确认封装／引擎、构建指纹、符号可用性和目标问题，再挑一个代表样本验证读表／代码路径。只有当前案例证据的能力标为项目样本能力，不称通用兼容。
