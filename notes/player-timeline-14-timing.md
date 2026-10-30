# 招式时间轴14：动画标记、时长边界及特殊命中引用

## 讨论范围与方法

本批只读当前13版动作、已解析数据表和匹配EXE，研究主图61个树内动作与88个树外候选。脚本 `exports/20261029-招式时间轴-14/timing-extract.py` 生成同目录 `timing-data.json`，149项动画表引用逐项接通；报告含输入SHA。配置解析不等于运行时触发。

本次定向反汇编由 `scripts/disassemble_research.py --group timeline14-timing --name OrderAttack::OnStart --name OrderAttack::GetAnimSequenceNumFrames --name OrderAttack::GetAnimHelperParams` 执行，退出0。工具先重算EXE SHA256并与PDB索引构建核对：`a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`。PDB GUID/age匹配依据 `inventory/pdb_overview.json` 及08批构建记录，本次未重新逐字节计算PDB哈希。

工具硬编码输出原在 logs/timeline14-timing、inventory/timeline14-timing-disassembly.json，执行后移入本批 `logs/20261029-招式时间轴-14/timing-disassembly/` 及 `exports/20261029-招式时间轴-14/timing-disassembly.json`，报告file路径随迁移修正。此为实际工具适配限制，不将旧路径列为仍存在。

## T1：动画坐标与表标记可直接展示

2026-10-30修订入口：16批`notes/player-timing-16-buildup.md`与`notes/player-timing-16-hitclock.md`已接通Wanted/LastBuildup分段变速与HitFrame空间取样用途。下文T2/T2a的未知和“追helper+154（order+314）”是旧停止位置，已由新证据取代：GetInitialPlayRate的this为接口子对象+1B0，实际字段是完整order+4C4，不是helper+154。原日志保留；当前解释见知识库《招式时序字段与播放机制》。

动作AttackDB的 `m_fAnimFrameRate[0]`、`m_fAnimFrameDeltaTime[0]` 指定配置坐标，`m_iWantedBuildupFrames[0]` 是期望前摇参数；`m_AnimationRow[0]` 连接动画表的 `m_iLastBuildupFrame` 与 `m_fHitFrame`。149个动作引用都能找到表行。

判定窗口 `m_FrameRange[0].m_Anim[0]` 的 `LowerBound[0]` / `UpperBound[0]` 各含 `Type[0]` / `Value[0]`。无界端为Open，不能以其保存的0当作结束帧。图旧实现访问 `l.Value` / `u.Type` 与实际键不一致，不能据HTML里存在timeline函数认定窗口已画出。

例如正面刺拳WantedBuildup=8、动画表前摇末标记13、命中标记20、判定22–23是不同字段，分别画参数和标记，不将8替换成动画轴第8帧，不将22/60称为按键至命中时间。

## T2：动画结束与实际秒数仍缺

`OrderAttack::GetAnimSequenceNumFrames` RVA `0x1ad34b0` 在动画弱引用有效时读取UAnimSequence对象+0xC0的整数并转浮点；无有效动画则返回0。`OrderAttack::GetAnimHelperParams` RVA `0x19f4dc0` 返回order+0x1C0。`OrderAttack::OnStart` RVA `0x1adc9c0`，区段 `0x1add604–0x1add664` 将动画配置整数字段和GetLastHitFrame结果分别除以动画帧数，用于归一化控制数据。这并非“每一动画帧耗时固定”的证据。

现有tagged对象中未覆盖 `/Animations/MainChar/` 的AnimSequence，首轮未解帧数和动作播放起止。不能仅凭库存无记录推断工具不支持：后续复查发现已有 `scripts/decode_case_resilience_serialized.py` 已成功用相同有界读取器读Grunt动画的NumFrames与SequenceLength，因此首轮停止依据不足，按T2a补作代表样本。先前 `UpdatePlayRate` RVA `0x1aeb630` 已证实运行时管理倍率相乘，但+0x314初始速率的完整写入链未闭合。故报告 `animationEndFrame` 与 `elapsedSeconds` 明确为null。最晚有限窗口只是已知数据范围，不是动画结束。

下一步：定向补提取／解码所需AnimSequence帧数及SequenceLength，核对播放器实际起止和初始速率写入者；未完成前，不计算实战前摇或总收招时间。前摇未知只限制实际时间换算，不否定判定窗口的保存动画坐标。

### T2a：Jab源动画代表样本已恢复

复用repak 0.2.3和local_bounded_packages.read_package/tags，只提取 `Sifu/Content/Animations/MainChar/Attacks/Man/Barehands/LightCombo/MainChar_Attack_Man_Barehands_Pressure_Jab_FR` 的uasset/uexp，不提取整个目录。生成源 `timing-animation-probe.py`，命令 `python -B exports/20261029-招式时间轴-14/timing-animation-probe.py` 退出0；报告同目录JSON逐文件记录字节数、SHA、脱敏命令和未消费native后缀。读取主导出的标量：NumFrames=126、SequenceLength=2.0999999046325684秒、bEnableRootMotion=true。126/2.1≈60，与动作配置60fps一致。此为**源动画长度**，不证明动作完整播放至126帧，也不代表126是闭区间最后采样序号。

报告按asset追加sourceAnimation，仍保留animationEndFrame=null，避免把源动画长度当动作实际终点。代表样本成功说明能力可复用，其他动作尚未提取，不推149条全覆盖。

补取证4函数（同工具group timeline14-timing-extra，退出0）：两个OrderAttack构造入口、UPlayAnimSubAnimInstance::Initialize RVA0x193c850、AnimationHelper::InitParamsFromSequence RVA0x190ba90。原始与清单移到本批timing-extra-disassembly目录／JSON。OnStart在0x1add3d8检查helper已初始化标记，未初始化才调用InitParamsFromSequence；0x1add457从动画+0x90装载长度进入order+0x490/+0x4c8。helper在0x190bb0f检查context+0x31，成立取context+0x34，否则以(1-context+0x3c)乘源动画+0x90，并写helper+0x2c/+0x30等控制字段。这证明播放控制存在上下文覆盖，不能只由SequenceLength推最终时长。该上下文字段完整类型与上游赋值未恢复，因此不命名为确定的“截断／起始百分比”。

Initialize在0x193c86b经order虚函数+0x158取参数；本函数只接续拥有者与IK等初始化，没有直接确定初始倍率。下一步应追helper速率字段+0x154（order+0x314）的写入及每帧更新消费者，而不是重复搜索此Initialize函数。

## T3：特殊命中动作引用

树内5条launcher引用落在4个节点：10重击第4段的FallHitActionLauncher；12抓击后重击肘击的正面／背面同步命中动作；21招架反击长按重击的CrookedFoot同步动作；55闪避攻击换位的InvertPosition同步动作。逐项资产、段号、类引用及节点在报告specialHitActions中。其余7条为树外动作引用，不能归作已确认可用招式。

这是命中行保存的启动器配置，不证明所有对手和状态下都触发；具体敌人兼容与启动条件未核。成品可准确写“特殊命中动作配置”，不可无条件写“必定击倒／抓取”。

## T4：候选配置，不擅自全加

候选包括距离参数、最大追踪角度、贴近距离与出手阶段贴近／回位、动作标签、判定段激活条件和许可窗口命中条件。详见报告candidates。每项应先按使用意义说明，并由用户选择是否展示；距离配置不当必然命中距离。

## 验证及边界

运行 `python -B exports/20261029-招式时间轴-14/timing-extract.py` 退出0：149动作、149动画行、12特殊命中launcher引用。脚本保留原始边界，不填充缺少的结束或时间；未进行游戏实测。初次rg使用PowerShell通配路径发生os error 123，已改目录加glob，未损失数据。
