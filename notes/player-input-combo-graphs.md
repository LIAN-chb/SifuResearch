# 玩家字段中文化、输入衔接图与伤害关联

## 范围与依据

本轮优先处理玩家攻击。字段译名用于阅读，不将字面译名当作已经穷尽的运行期语义；招式中文名是资源／节点的辅助直译，不冒充官方名称。原字段名、资源路径和节点编号均保留。

| 项目 | 处理 |
|---|---|
| 玩家字段 | 当前玩家 AttackDB 与动画／HitBox 表中共133个不同保存字段，全部附中文标识和说明 |
| 动作到伤害 | 255个玩家 AttackDB、314个可解析命中窗口，关联到具体HitBox行，分别显示命中生命／架势、硬直帧和格挡／弹开架势配置 |
| 输入图 | 5套已解析Combo树，126节点、128条保存的输入映射；另显示节点重定向与默认输入入口 |
| 姿态槽 | FComboNodeAttackInfos.m_Attacks为4项FName数组，同节点的槽位不作为重复命中次数累加 |
| 条件覆写 | 原始复杂映射仍有不透明项，基本动作槽不保证就是实际最终动作 |
| 运行期验证 | 未运行游戏 |

## 新增有界解码

decode_player_combos.py从现有提取的uasset／uexp和包元数据读取Combo对象，校验序列范围、UObject尾部、数组内标记和结构元素边界。针对m_TargetNodes读取原始属性头，确认ByteProperty→IntProperty，解析removed-key列表与映射对，要求精确消耗字段字节且所有非负目标编号落在当前节点数组内。

115个目标映射共128条目标记录均通过边界检查，未出现移除键。原始映射字节长度和SHA保存在inventory/player-combo-graphs.json；源码只读游戏产物，输出研究文件。

PDB布局独立确认FComboTransition.m_TargetNodes为TMap<unsigned char,int>，而非按长度猜测其元素结构。条件分支键实际出现255、0、1、2，不能把它们全部套成Yes／No。

## 输入与默认节点

| 代码 | 直接证据 |
|---|---|
| UCombo::GetDefaultAttackID，RVA 0x195bc70 | 输入转换枚举小于21时按索引读取默认节点；LightHold=1若为-1回退到Light=0，HeavyHold=7若为-1回退到Heavy=6 |
| UComboTransitionHelper::BPF_GetInputFromTransition，0x19501e0 | 输入转换存在到InputAction的分派；尾部跳转表不作为指令解释 |
| FComboTransition::GetTargetNodeID，0x195eaf0 | 条件实例、目标与后续映射参与节点选择；原始分支键不直接等同于最终布尔结果 |

这里只恢复了配置连接和输入类型。图中L/H指轻／重动作输入，不固定键盘或手柄键。Front、Alt等具体手势、参考方向和阈值未核时保留内部名；不凭名字补写延迟／搓招手势。

## 文档与脚本

| 文件 | 用途 |
|---|---|
| exports/player-field-labels.json | 中文标识与边界说明 |
| scripts/player_labels.py | 中文字段路径和说明渲染 |
| scripts/build_player_readable.py | 玩家伤害对照、字段说明、五套输入图和节点伤害 |
| inventory/player-readable-catalog.json | 生成文档哈希、覆盖统计与源数据哈希 |
| inventory/player-combo-type-layouts.json | 连招节点、输入、结果枚举等PDB布局 |
| inventory/player-combo-input-disassembly.json | 输入转换与目标节点选择的代码边界及输出哈希 |
| inventory/player-combo-default-input-disassembly.json | 默认输入入口与长按回退的代码证据 |

本轮生成器发现4篇旧配置笔记与之前哈希不符；经重建上一版输出、逐单元格规范化后，确认只是表格对齐变化，正文与数值一致。已先备份到notes/vault-backups/table-format-20261028-092203，再接受格式变化后更新中文渲染，不覆盖实质性修改。

## 未完成

| 问题 | 当前边界 |
|---|---|
| 官方招式中文名／实际输入手势 | 未逐项校对，中文名保持辅助直译；输入类型保留原文 |
| 连段是否稳定命中 | 图不是防无限连、追击窗口或手感的运行时验收 |
| 条件攻击、蓄力与技能全部替换 | 有不透明结构，基本动作槽只表明保存引用 |
| 完整单手环境攻击逻辑 | 当前保存Combo图只有1个节点，不能据此宣称环境武器只有一种攻击 |
| Mermaid展示 | 已检查数据连接与引用；图的实际Obsidian布局需要在阅读视图查看，不伪称实战或渲染验收 |
