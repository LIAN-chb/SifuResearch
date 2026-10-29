# 徒手补全13：条件攻击Map有界解码

本分支只查`MainChar_ComboTree.m_Nodes[*].m_ConditionalAttacks`，不改共享图或生成器。结果在`exports/20261029-徒手补全与命名-13/conditional-attacks.json`；读取器`conditional-decode.py`可复现。游戏和存档只读，复用现有提取原件，没有新提取或新代码取证。

## 输入及结构

使用`inventory/package-metadata.json.gz`定位`Sifu/Content/DB/_MainChar/Combos/MainChar_ComboTree.uasset`，精确选名为`MainChar_ComboTree`的export14。当前uasset和uexp SHA分别与`inventory/player-combo-graphs.json`原树记录核对相同；全部57个原有opaque Map字段的原始块SHA也逐一一致。具体哈希见输出source和每节点记录，不另复制长哈希。

原类型证据`inventory/player-unknown-08-quadrant-types.json`的`FComboNode.m_ConditionalAttacks`明确为`TMap<FGameplayTag,FComboNodeAttackInfos,...>`，其值只有四象限攻击名称、蓄力攻击及蓄力过程字段，不含节点过渡。08批`FComboNode::GetAttackInfos` RVA0x195a9c0已静态接通按角色标签选择Infos，未命中回基础Infos；本次没有重反汇编该函数。该语义继承08构建边界，本次只增加确切Map保存内容。

Map payload布局：int32 removed-key数量、按数量保存的tagged GameplayTag、int32 entry数量；每项为一个tagged GameplayTag key，后跟一个tagged FComboNodeAttackInfos value。观察到的GameplayTag key恰41字节：TagName/NameProperty值FName及None终止；Infos value恰312字节，四个m_Attacks NameProperty、两空Struct数组及None终止。节点Map 1067字节即8+3×(41+312)，361字节即8+1×(41+312)，空Map8字节。不能把tagged GameplayTag直接当裸8字节FName。

读取检查：顶级导出properties终止后只余4个零字节；57节点Struct数组头／声明大小及数组完全消费；每Map的key/value类型头StructProperty→StructProperty；removed与entry计数范围；每键有且仅有TagName NameProperty；每value基础槽恰0/1/2/3；两Struct数组声明大小／计数／尾部精确消费；最后每Map完全消费且SHA对应原opaque块。每条结果保留node、tag、slot→asset变体、原归一化Infos、entry及Map的uexp绝对偏移／大小／哈希。

## 已查明的覆盖

| 项目 | 数量 |
|---|---|
| 已核Map节点 | 57 |
| 非空Map节点 | 21 |
| 条件条目 | 57 |
| 唯一引用动作资产 | 70 |
| 已在基础树61资产中的引用 | 19 |
| 先前88树外候选中被条件引用 | 51 |
| 不在原树或88候选中的新资产 | 0 |
| 条件蓄力档位 | 0 |

所有保存键以`Attack.Modifiers.`开头。ComboPakMei10条、ComboBrawler11条、ComboAgile10条，其余26条分属FarGrab、DeadlyWaltz、BounceKick、GSPKickRunning、RushJumpKick、GrabTakedown、540JumpKick、Sweep、LowKick360、FrontKick、ThrustPalm、ShoulderStrike、TripleHitPunish、FalconPunch、HammerKick、TornadoKick、CobraDoubleBite、SpinTrickKicks、GroundPunch（2条）、RisingFalcon、NajaReverseLash、ElbowStrike、JumpKnee、DoubleHitUppercut、GSPKick。完整逐键位置见JSON。

例node44的1067字节Map：

- `Attack.Modifiers.ComboPakMei`：四槽统一引用`_SpecialCombo/AltPakMei/MainChar_Special_Combo_AltPakMei_HeadExtPunch`。
- `Attack.Modifiers.ComboBrawler`：0/1=MainChar_Jab_FR，2/3=MainChar_Hook_BL，仍是当前基础显示中的两套资源。
- `Attack.Modifiers.ComboAgile`：四槽统一引用`_SpecialCombo/Agile/Mainchar_Special_Combo_Agile_HighSlightKickEngage`。

这解释了相当部分树外特殊动作候选的引用归属，但不等于它们成为默认徒手新节点。它们占据原节点的Infos位置，仍用原节点过渡；展示时适合作为原节点的条件配置。是否当前启用某Tag仍需角色／修改器状态，不能只凭随包存在就默认启用。若单独提供替换招式视图，也应保留原位置、条件和替换身份，不添加没有保存的新衔接。

## 没有因此闭合的候选

原88树外候选中剩37个未由此Map引用：21旧路径、10特殊路径、6常规路径。六张旧候选卡（抓取两个变体、GuardBreak_BL、DoubleElbowStrike_FL、ClawsElbow_DoubleHit_FL、HighCrush技能候选）均未被本Map连接。不能将这次“51个树外候选已找到条件归属”扩大为所有树外动作已查全；这六项的独立入口仍须由对应能力／订单／Grab等路径核对。

## 执行、失败和边界

执行命令`python exports/20261029-徒手补全与命名-13/conditional-decode.py`，退出0。Python版本、读取器和bounded parser SHA在输出；原始uasset、uexp和57块Map SHA覆盖实际字节。父批可复核或直接复用输出。

探索先误选export1，`StopIteration`（没有m_Nodes）后按确切export名改为14；又先试裸FName键，读到TagName并使下一tag类型落在资源名上，说明其假设错误；改按tagged GameplayTag+tagged Infos后所有块精确消费。探索脚本`conditional-inspect.py`保留，未覆盖旧生成器或证据。最终读取器不依赖跳过异常，也不猜数组尾部。

本批没有声称运行时触发或技能可用性；也不以键名 alone 证明某个修改器的解锁方式。已直接确认的是每个角色标签下保存的四槽替换及其原节点归属。当前默认图完整性应另查六常规候选与树外系统动作，而非把这51个特殊替换无条件加入默认图。
