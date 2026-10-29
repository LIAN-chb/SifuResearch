# Sifu：外部研究与工具线索

日期：2026-10-27（Asia/Shanghai）

## 范围与结论

用户本机对象是 Epic 安装版《师父》。本笔记汇总可用于本机构建分析的外部路线、待验证字段及逆向边界；外部作者报告和社区工具说明均是线索来源，不能代替对本机 EXE、PDB、PAK 和资源的复核。

建议从两条线并行做静态研究：

1. 用可选择提取的社区 Moveset 工具作为资源路径/字段名导航，重点查看敌人 AttackDB、ArchetypeDB、ContextualDefense 和共享数据库。
2. 利用本机已经核对匹配的 EXE/PDB 定位实际 C++ 群体调度与命中反应逻辑；优先检验 AI ticket 管理器的申请、发放、释放、限额及角色间关系。

目前有足够证据认为用户关注的系统有很好的研究入口，但没有证据证明存在“同一时刻只能一名敌人攻击”这样的单一规则；攻击票据命名本身不能证明排他性、轮转、公平性或冷却机制。

## 资源与战斗字段的外部线索

独立社区项目 [Sifu Custom Moveset Maker](https://github.com/ChorlsChu/Custom-Moveset-Maker--Sifu-Mod-) 声称能对 Sifu PAK 选择提取部分资源，并以敌人与 Boss 的 ComboTree、AttackDB、ArchetypeDB、ContextDefense 为主要功能。其 README 描述：

- `ComboNode` 连接攻击动画，`ComboEdge` 表示输入方向；`AttackDB` 引用动画和 `AttackDataRow`。
- `AttackDataRow` 含 `m_HitFrame`/`m_fHitFrame` 等命中时间字段；该工具还暴露攻击蓄力帧 `m_iWantedBuildupFrames`、攻击距离 `m_fGameplayRange`。
- 敌人 `ArchetypeDB` 可读生命值和 Structure（姿态/架势量表）。README 称量表满时会 stagger，之后随时间重置；这个精确行为需结合实际资产和本机代码确认。
- 实验性 `ContextualDefense` UI 暴露 `Memory Limit`、`Hits Count`、`Flush Limit`，并解释为 AI 防御记忆时长、记忆窗口内命中次数及防御后的间隔。字段名/映射来自工具作者；README 明确标为 experimental，尚不是对本机运行行为的独立证明。
- README 称可针对 `DB/AI/Archetypes/*/Attacks/`、`DB/AI/_Shared/`、`DB/Movement/` 和 `Animations/` 选择性提取；提取量约 1.2 GB（工具不同章节估值不一致，约 0.5–1.2 GB）。

来源：[工具 README（数据模型、字段、提取方式）](https://github.com/ChorlsChu/Custom-Moveset-Maker--Sifu-Mod-/blob/main/README.md)。这是具体工具作者对自己程序和测试结果的描述，项目状态注明 prototype/work in progress。可先把 README 中的资产路径当搜索路径清单，不假定工具适配任意 Sifu 版本或必然能在本机自动成功。

## AI 与群体协同线索

独立逆向报告 [用 REA 分析与重构 Sifu](https://github.com/oiiiwjh/rea-exploration-notes/blob/main/wiki/sifu-analysis.html) 标出了群体 AI 的符号入口：`FAIAttackTicketManager`、`AICombatRolesTicketManager`、`AIPhaseScenario`。作者报告查询过 7 个 ticket 管理函数及 DB 图关系，但明确说尚未完整重构调度策略。报告将“ticket 调度的申请/释放/公平性”列为待恢复事项。因此最稳妥的解释是：代码中有与攻击/战斗角色协调相关的 ticket 子系统，调用和数据关系值得跟踪；它具体如何影响多个敌人同时攻击、围攻、等待、换位或出招冷却，仍需本机证据。

这份报告也提到部分 GuardDB 的 parry 相关字段，但其中示例对象是 `MC_GuardDB`（玩家）而非敌人通用值。作者列出的数值包括 `m_fParryFreezeFrames=4`、`m_fParrySBFreezeFrames=2`、`m_ParryAttackerStructureDamage=50`、`m_ParryAttackerSuperDizzyDamage=10`、`m_fForcedGuardDuration=24`。报告提醒这些只是单个 DB 的序列化值，未接入完整运行时判定，单位/场景覆盖关系仍需确认；**不可将它们视为敌方攻击的冲击力、削韧或命中硬直表**。

来源：[研究报告的项目索引、引擎身份、群体 AI 状态、GuardDB 边界和待恢复部分](https://github.com/oiiiwjh/rea-exploration-notes/blob/main/wiki/sifu-analysis.html)。该作者给出工具链、摘要清单及可复现材料链接，具有较好的定位价值，但属于另一台机器/另一游戏构建的逆向记录。其报告明确承认没有完整恢复 AI 调度、完整伤害链或全游戏源码。

## 版本与可复用性边界

外部逆向报告的目标是 UE4.26 / Win64 Shipping。其记录的 EXE 为 100,491,264 bytes，主 PAK 为 31,100,859,986 bytes；报告所用 EXE/PDB GUID、age 只匹配该作者的目标构建。

用户本机 Epic 安装的 PAK 为 31,101,086,834 bytes；本机 EXE 约 102,850,048 bytes，并已在本机核对 EXE/PDB 的 GUID 与 age 匹配。PAK 和 EXE 均与公开研究报告尺寸不同。这说明外部已发布的 AES key 派生结果、RVA、成员偏移、资产原始散列值和参数读取结果都不能不加核对地照搬。可以复用的是符号名称和资产路径作为本机查询的导航提示；本机 PDB、代码调用、文件版本与数据对象仍须互相验证。

外部报告对自己构建的 PAK v11 `pakchunk0-WindowsNoEditor.pak` 记录为索引与条目载荷均加密，并从匹配 EXE 的 `FEncryptionKeyRegistration::Callback` 逐字节取出 32-byte key；材料没有把明文 key 发布到仓库。用户本机当前只确认 PAK v11 且索引加密；本机 AES key 和每条载荷的加密情况仍应仅从**本机匹配版本**确认，不能从同名 PAK 或类似大小假定。

## 硬直、冲击力与削韧研究拆分

建议对每一招记录这些不同量，避免把一个数值误称“冲击力”：

| 问题 | 优先定位证据 | 关键边界 |
|---|---|---|
| 伤害 | AttackDataRow、Damage/Hit 函数、目标减伤属性 | 攻击基础值不一定是最终扣血量 |
| 姿态／架势削减 | AttackDB/攻击行、Structure/Guard 组件、格挡/招架路径 | 玩家与敌人可能用不同 DB；招架对攻击者造成的 Structure damage 不等于攻击者普通攻击削敌人姿态 |
| 命中硬直 | Hit reaction、stagger/super-dizzy/forced guard 逻辑、动画/Notify | 动画播放时长与禁止输入时长可能不同；逐帧 TAE 窗口不能直接推成总硬直 |
| 冲击/击退/HitStop | 外力或 knockback 字段、实际 ApplyImpact 路径和 Freeze 函数 | 视觉命中停顿、位移、姿态损伤和硬直是相邻但不同效果 |
| 攻击时序 | `m_fHitFrame`、`m_iWantedBuildupFrames`、ComboTree 与动画事件 | 动画 hit frame 不证明碰撞、伤害或硬直在该帧如何结算 |
| 敌方 AI 防御 | ContextualDefense、敌人 ArchetypeDB、PDB 对字段的读取点 | 资源值需要追到被哪个原生函数读取、何时重置并影响何种决策 |
| 群体协调 | ticket manager 的所有申请/确认/取消/释放调用点与共享状态 | 类名提示含义，不说明团队上限、距离/视线条件、公平性或每个敌人主动性 |

以上是本次研究建议的数据采集表，不是《师父》的已确认机制公式。

## 工具与执行注意事项

- 首选先审查现有工具的开源源码和版本记录，再决定是否使用提取功能。社区 Moveset Maker 的源码 README 提供了可行的选择提取范围；不必一开始复制整包或全部 31 GB 资源。
- 如果使用 UnrealPak/FModel/CUE4Parse 等通用 UE 工具，先验证用户本机版本。加密索引没解开之前，工具看不到路径；UE 资源解析器识别出 UE4.26 也不等于它自动处理项目定制序列化、加密或所有 cooked assets。
- 单独把“列出包目录、导出少数目标资源、读取字段、追 C++ 使用点”逐步验证。每一步保存目标文件 SHA-256、EXE/PDB GUID-age、软件版本、输入/输出清单和校验状态；密钥与原始游戏资产留在本机，不写进公开文档或提交。
- 资源解析时记录未知字节/字段为未解析，避免按常见 Unreal 布局猜默认值。先选一个攻击/敌人做端到端样本，字段语义稳定后再扩展类别。
- 静态分析无法证明实战中最后生效的值。难度、角色阶段、敌人家族、动画事件、蓝图/原生代码覆盖，以及状态机时序，都可能改变最终结果；必要时再设计 PIE 或游戏内受控验证。

## 对外部数据的下一步验证顺序

1. 检查当前本机 PDB 的 ticket manager、AICombatRoles 和 AIPhaseScenario 符号及其交叉引用，记录每个函数的申请、授权、取消、释放和状态字段。
2. 检查本机所需的敌人家族资产路径是否存在，选择 1–2 种敌人，追 `ContextualDefense` 字段到实际代码读取点。
3. 选定一招敌人攻击，串起 ComboTree → AttackDB → AttackDataRow → 动画命中事件 → 命中处理/目标反应，并区分伤害、Structure、击退、HitStop、硬直各自数值。
4. 做一个群体AI可观察情境的手动验证设计，例如对照场上 1、2、3 名普通敌人的决策和交替攻击，标清纯静态推断与实际行为证据。

## 来源

- [Sifu Custom Moveset Maker README](https://github.com/ChorlsChu/Custom-Moveset-Maker--Sifu-Mod-/blob/main/README.md) — 提取范围、攻击数据路径、敌方 Structure 与实验性 ContextualDefense 字段。工具作者声明项目仍处 prototype/work in progress。
- [Sifu REA 逆向整合报告](https://github.com/oiiiwjh/rea-exploration-notes/blob/main/wiki/sifu-analysis.html) — 不同构建的 AI ticket manager 导航、战斗资产部分读取、验证覆盖和明确恢复缺口。
- [Microsoft: Symbols and Symbol Files](https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/symbols-and-symbol-files) — PDB 符号文件可包含函数入口与变量/类型等调试信息；符号文件不等于原始源码。
- [Epic Games: Packaging Your Project](https://dev.epicgames.com/documentation/unreal-engine/packaging-your-project) — UE 打包包含 C++ build、资产 cook 与 staging；提供 cooked assets 的格式语境。
