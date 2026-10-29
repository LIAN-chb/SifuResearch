# 案例输入与攻击引用核对（2026-10-28）

## 范围与复用决定

只读复核现有知识库配置和解析产物；没有重新提取、解析或运行游戏。目标是确定可作为“玩家出招→敌人受击”的静态例子的输入路径，并区分输入衔接、攻击资产引用和敌人是否被持续压制。以下图索引来自`inventory/player-combo-graphs.json`，详细配置见徒手输入图、动作与时序配置及伤害对照页。

## 案例 A：徒手组合图里的刺拳与后续攻击

精确图身份：`inventory/player-combo-graphs.json`的`trees[3]`，资产`Sifu/Content/DB/_MainChar/Combos/MainChar_ComboTree.uasset`；UAsset SHA256 `163c06dbf916c1767a97b137563155295a348e9be550e50d945d5d45295c904e`，UExp SHA256 `516ec6083566f852183da455194d99e3b8f931d6a5acb134466d9c288df0f3a2`。以下Node编号仅指此徒手图。

| 环节 | 精确配置 | 能支持的结论 |
|---|---|---|
| N44节点身份 | `trees[3].nodes[44]`，名`Jab(new)`。姿态槽0/1（`m_Attacks[0/1]`）指`MainChar_Jab_FR`；槽2/3（`m_Attacks[2/3]`）指`MainChar_Hook_BL` | 同名节点按姿态分两组；不能将四个槽都写成刺拳 |
| N44输入边 | Light→N45、Heavy→N47；条件引用为空，保存概率均100% | 是输入图转换路径；概率不是命中率或连续压制概率 |
| 槽0/1刺拳命中 | `MainChar_Jab_FR`段0→`Jab_HB01`，Inclusive 22–23；`Pressure_Jab_FR`约60fps、WantedBuildupFrames=8；该HitBox普通命中生命10、架势12、硬直配置8帧 | 攻击、命中行及时序配置可定位；保存帧数不等于敌人禁止防御的时长，也不证明实际命中 |
| N45节点身份 | `trees[3].nodes[45]`，名`ThroatPlexus`。姿态槽0/1指`MainChar_ThroatPlexus_DoubleHit_FR`；槽2/3指`MainChar_GroinHead_DoubleHit_BL` | 后续攻击也依姿态变化 |
| N45输入边 | Light→N14、Heavy→N46；条件引用为空，保存概率均100% | 可继续沿图查输入路径，不能由此推出敌人来不及防御 |
| 刺拳动作许可范围 | `MainChar_Jab_FR`另存GenericFollowUp从动画帧25起、Alt在40–78、GenericAll从78起的许可窗口；命中条件掩码保存值31 | 这是玩家攻击自身的许可配置；敌人防御许可属于另一对象与调用路径 |

可用例子：在徒手组合图N44，姿态槽0/1是刺拳，Light输入转到N45；N45槽0/1是ThroatPlexus双击，仍可继续转N14或N46。N44槽2/3则是Hook_BL，N45换成GroinHead双击。输入图说明玩家可选路径，不证明敌人会被连住。

## 案例 B：S3轻击分支中的三连拳候选

精确图身份同上：`trees[3]` / `MainChar_ComboTree.uasset`。

| 环节 | 精确配置 | 能支持的结论 |
|---|---|---|
| 起始入口 | `trees[3].starts[3]`保存枚举原值`BP_MainCharComboStartStates::NewEnumerator12`；徒手输入图称其S3。Light边到Node1，条件对象名含`BP_TargetIsParryVictim`，保存概率100% | 路径由带条件的S3轻击边进入Node1。仅凭资源名不能断言条件蓝图返回语义，也不能说招架后必走此边 |
| 过渡节点选择 | `trees[3].nodes[1]`的Light边：33%→Node2 `3Hits_01`；34%→Node17 `3Hits_02`；33%→Node18 `3Hits_03`。三条边的条件引用为空 | 三连拳系列是三个保存分支之一；MC_3Punches_FR并非唯一或必选项。权重尚未运行时验证 |
| FR候选 | Node2名`3Hits_01`，姿态槽0–3均引用`MC_3Punches_FR`；Heavy边指向Node3 | 只有实际进入Node2，才套用FR攻击数据 |
| 其他分支 | Node17引用`MC_3Punches_02_FL`，Node18引用`MC_3Punches_03_FL` | 两者须按自己的命中段和时序分析，不能套用FR数值 |
| FR三段命中 | 段0/1/2分别为`3Punches_HB01/02/03`，窗口Exclusive 5–Inclusive 8、Exclusive 11–Inclusive 15、Exclusive 19–Exclusive 24。末段基础眩晕等级14；普通／进阶Grunt InFight眩晕抗性11 | FR末段构成眩晕候选；仍需命中、状态覆写及其他条件通过 |

可用例子：从S3 Light条件边进入Node1后，若Light分支选到Node2，再检查`3Punches_HB03`是否令敌人眩晕。Node1保存权重33/34/33，不能写成必定使用FR。招架事件反馈与三连拳攻击自身命中造成的状态须分开。

未闭合：S3条件蓝图的实际返回表达式、三个分支运行时选择、用户实测是否走Node2、HitBox运行时覆写及敌人是否在各段间恢复防御。

## 案例 C：同一普通杂兵的Hook与StraightJab被闪避

按`notes/avoid-system-chain.md`里的普通Grunt组合引用：

| 敌方招式 | 组合节点 | HitBox行 | `DizzyOnAvoid` | 对照意义 |
|---|---|---|---|---|
| Hook | `Grunt_Base_Combo.m_Nodes[0].element[1]` | `Hook_HB01` | True | 成功闪避后可选择闪避惩罚配置的候选 |
| StraightJab | `Grunt_Base_Combo.m_Nodes[0].element[11]` | `Jab_HB01` | False | 同一普通Grunt资源中的对照；不会因该标记选择相同分支 |

这是“只变更敌方来袭招式”的配置对照。它证明组合资产引用了相应AttackDB/HitBox行，不证明AI实战必选该节点。验证时固定玩家后续攻击、位置和敌人初始状态，分别成功闪避Hook与StraightJab，观察反击是否命中、原攻击者是否眩晕；不要把成功闪避和反击命中合成一个事件。

## 三种“接上”的判断

| 判断层 | 本批证据 | 缺少什么 |
|---|---|---|
| 玩家可以出招 | N44→N45输入边和姿态版本已在徒手ComboTree中确认 | 实际输入缓冲、方向／状态条件是否生效 |
| 玩家下一招可以命中 | AttackDB、HitBox行与窗口已知 | 距离、朝向、敌人位移、防御、韧性及运行时缓存值 |
| 玩家可以连续压制 | 本批资产不能单独证明 | 敌人Hitted期间有效防御许可、AI决策与执行时刻、下一击命中相对时序 |

## 推荐案例顺序

1. 徒手N44→N45：按槽0/1刺拳路径与槽2/3 Hook路径分别核对，后续攻击也依姿态分开。
2. 相同连段的紧接／延迟对照：先静态核玩家可出招窗口及敌人恢复许可；没有可证明的时序时标为运行时观测。
3. 闪避普通Grunt Hook与StraightJab，固定玩家反击：核对DizzyOnAvoid分流。
4. S3→Node1的轻击分支：记录33/34/33三个子节点；仅选中Node2时分析MC_3Punches_FR。

## 续接断点

本批已把玩家输入图接到确切姿态槽、Node、攻击资产和命中行；敌人普通受击侧尚不能回答为何在某次下一击前恢复防御。下一步仍需查敌人普通Hitted期间Guard许可来源、恢复许可如何影响AI查询，以及AI何时选择并执行防御。保存的输入概率、攻击帧和硬直配置均不能直接给出连续命中保证。
