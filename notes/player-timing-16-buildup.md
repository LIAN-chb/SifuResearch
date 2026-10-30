# 前摇语义16：期望帧数、源动画标记与播放倍率

## 批次与范围

- 问题：恢复 `m_iWantedBuildupFrames` 与 `m_iLastBuildupFrame` 如何共同决定 OrderAttack 实际起手，不将名称直接当机制。
- 完成条件：匹配构建下，恢复字段布局、倍率生成、消费者、阶段切换、上下文类型及确有代码依据的例外。
- 写入范围：本文件，`exports/20261030-前摇语义-16/buildup-*`，`logs/20261030-前摇语义-16/buildup-*`；共享页由主任务合并。
- 开工Git已有其他批次交接改动，不触碰。主任务维护总交接与提交。
- 证据阶段：匹配PDB字段与EXE静态代码链；没有游戏运行时观测。

## B16-1 构建和复用

`exports/20261030-前摇语义-16/buildup-build.json` 为本批重核：

- EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`。
- PDB SHA256 `5925d79b63df58ff98575454f3d31b07a4e0da44f96dc19461fc5b7e56d1b90c`。
- PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d`，age 1，与现有EXE debug记录一致；EXE全文件哈希同时与原索引一致。
- `buildup-probe.py` 复用 `inspect_types.py` 和 `index_pdb.Msf`，输出独立路径。
- `buildup-disassemble.py` 复用 `disassemble_research.py`，仅改内存中的输出路径，按已有PDB过程边界取证。运行时EXE哈希仍由原脚本核对。
- `buildup-publics.py` 在过程索引不含 `FAnimContainer::GetFinalPlayRate` 时只读匹配PDB public stream，定位所需符号与接口虚表；没有停在索引缺项，也未全量反汇编。其100字节窗口包含下一函数；本批只解释 `0xBE08E0–0xBE08FB`，之后为填充与无关函数。
- 14批 OnStart、helper初始化和构造函数日志复用：本批输入哈希一致，按需重读对应指令；不以旧摘要代替指令核对。

执行：`python -B exports/20261030-前摇语义-16/buildup-probe.py`、`python -B exports/20261030-前摇语义-16/buildup-disassemble.py`（不同目标参数版本）、`python -B exports/20261030-前摇语义-16/buildup-publics.py` 均最终退出0。原始程序过程边界、路径和汇编SHA见同目录 `buildup-*-disassembly.json`。完整命令工作目录均为研究根目录。最终脚本改为 `--group <组名> --name <过程名>` 可重放入口；实际目标分组和Python版本、脚本SHA见 `buildup-verification.json`。dumpbin实测FileVersion/ProductVersion均为14.51.36243.0，安装路径中的14.51.36231不是该二进制文件版本。

### 类型读取器的真实失败与修正边界

原 `inspect_types.py` 对 `LF_ONEMETHOD` 的 introducing-virtual vtable offset 使用 `cvnum`，但该位置为固定4字节值，导致 `OrderAttack` 在 `GetSubAnimStateActive` 后未读到成员。本批只在 `buildup-probe.py` 的内存适配中改为 mprop 4或6时 `q+=4`；重跑后能恢复 `OrderAttack` 后半完整成员。未批改公共脚本。能力仅验证本构建所选类型，其他类型条目仍须留意原读取器的停止标识。旧输出没有成员不等于PDB没有字段。

首次PowerShell调用中Python双引号嵌套报ParserError，没有运行取证；改here-string后成功。一次默认GBK读取UTF8批次脚本失败，改显式encoding后成功。`rg`使用路径通配符报123，改目录+glob后成功。以上没有更改游戏输入或覆盖共享原件。

## B16-2 布局与 this 调整：撤回 helper+154 初始倍率猜测

匹配类型见 `buildup-types.json`：

|对象|偏移|字段|
|---|---:|---|
|FComboAttack|0xAC|m_fAnimFrameRate|
|FComboAttack|0xB0|m_fAnimFrameDeltaTime|
|FComboAttack|0xB4|m_iWantedBuildupFrames|
|FAttackDataRow|0x6C|m_iLastBuildupFrame|
|UDefenseComponent|0x1F8|m_fBuildUpFramesMultiplicator|
|OrderBase|0x100|m_bInPrediction|
|OrderAttack|0x1B0|OrderAttackInterface基类子对象|
|OrderAttack|0x1C0|m_HelperParams|
|OrderAttack|0x490|m_fAttackDuration|
|OrderAttack|0x49C|m_fPlayRateOverrideMultiplierTotal|
|OrderAttack|0x4A0|m_fPlayRate|
|OrderAttack|0x4C4|m_fInitialPlayRate|
|OrderAttack|0x4C8|m_fAttackTimeLeft|
|OrderAttack|0x581|m_bBuildUpOver|
|OrderAttack|0x584|m_Target|
|OrderAttack|0x59C|m_AttackAnimGraph|
|OrderAttack|0x5A8|m_fBuildUpScale|
|OrderAttack|0x5AC|m_fAttackStrikeStartFrameRatio|
|OrderAttack|0x5B0|m_fAttackReleaseStartFrameRatio|
|OrderAttack|0x5B4|m_AttackStateAppliedDuration[4]|
|OrderAttack|0x5D0|m_FreezeStack|
|OrderAttack|0x5E0|m_bNewFrozenState|
|OrderAttack|0xAB8|m_bPlayRateManagedOutside|
|FNetOrderStructAttack|0xF0|m_fStartRatio|
|UAnimSequenceBase|0x90|SequenceLength|
|UAnimSequenceBase|0x94|RateScale|

`GetInitialPlayRate` RVA `0x19F5B60` 的 `[rcx+0x314]` 使用的是接口子对象指针：完整OrderAttack的实际字段是 `0x1B0+0x314=0x4C4`。不是 helper+0x154。

证据独立闭合：

1. 构造函数 `0x1AC4825–0x1AC4833` 在order+1B0写入OrderAttackInterface虚表。
2. 本批从PDB public定位虚表RVA `0x48883C0`；`buildup-publics.json` 实际读取：slot+0x30=`0x19F5B60`，+0x38=`0x1AE7760`，+0x40=`0x19E2020`。
3. OnStart `0x1ADD943–0x1ADD95B` 明确 `lea rcx,[rsi+1B0h]` 调slot+38，即SetPlayRate。
4. SetPlayRate `0x1AE776A` 写接口+2F0，等于完整order+4A0；接口+3EC等于完整order+59C，正好是动画子实例弱引用。
5. GetPlayRate（完整对象this）`0x1AD5210–0x1AD5220` 返回order+4A0乘order+49C，吻合上述解释。

完整OrderAttack构造函数 `0x1AC4855–0x1AC4896` 分别初始化额外倍率1、阶段倍率1、initial倍率1。默认initial=1不能解释Wanted前摇；Wanted主链实际在+5A8。

## B16-3 从Wanted到源动画段：真实算式

`OrderAttack::OnStart` RVA `0x1ADC9C0`，复用 `logs/20261029-招式时间轴-14/timing-disassembly/OrderAttack__OnStart-0x1adc9c0.asm.txt`：

- `0x1ADD604–0x1ADD62A`：`strikeStartRatio = LastBuildupFrame / NumFrames`，写order+5AC。
- `0x1ADD642–0x1ADD664`：`releaseStartRatio = GetLastHitFrame(attacker,target) / NumFrames`，写order+5B0。不是动画表单个HitFrame。
- `0x1ADD687–0x1ADD6E4`：取ComboAttack.Wanted；若order.Target是FightingCharacter且其DefenseComponent存在，乘 **目标防御组件** 的BuildUpFramesMultiplicator，再CVTTSS2SI向零截断。
- `0x1ADD6E8–0x1ADD710`：结果至少1，然后 `buildUpScale = LastBuildupFrame / effectiveWanted`，写order+5A8。
- `0x1ADD7D7–0x1ADD7ED`：前摇AppliedDuration=effectiveWanted * AnimFrameDeltaTime。
- `0x1ADD831–0x1ADD840`：下一阶段AppliedDuration=(GetLastHitFrame−LastBuildupFrame)*AnimFrameDeltaTime。
- `0x1ADD858–0x1ADD897`：恢复阶段AppliedDuration=(NumFrames−GetLastHitFrame)*AnimFrameDeltaTime。
- `0x1ADD8AD` 清BuildUpOver和HitFrameOver；`0x1ADD953–0x1ADD95B` 把buildUpScale传入SetPlayRate。

`ComputePhaseInfo` RVA `0x1ACAD90` 在 `0x1ACAE8A–0x1ACB172` 恢复同一组算式，并有客户端追赶分支。不是仅OnStart保存未消费的配置。

可靠伪代码（排除下面具名例外，正常起点）：

```cpp
int effectiveWanted = combo.m_iWantedBuildupFrames;
if (FightingCharacter* targetFC = Cast<FightingCharacter>(order.m_Target))
    if (auto* targetDefense = targetFC->GetDefenseComponent())
        effectiveWanted = truncToInt(float(effectiveWanted)
                           * targetDefense->m_fBuildUpFramesMultiplicator);
effectiveWanted = max(1, effectiveWanted);
order.m_fBuildUpScale = float(animRow.m_iLastBuildupFrame) / effectiveWanted;
order.m_fAttackStrikeStartFrameRatio = float(animRow.m_iLastBuildupFrame) / sequence.NumFrames;
order.m_fAttackReleaseStartFrameRatio = combo.GetLastHitFrame(attacker,target) / sequence.NumFrames;
order.m_bBuildUpOver = false;
order.SetPlayRate(order.m_fBuildUpScale); // 接口this已调整
```

这里Wanted是用于重定时前摇段的期望帧数；LastBuildupFrame确定该段在源动画坐标中的边界，两者做除法生成播放倍率。L=13、W=8在有效目标倍率1时产生13/8=1.625倍前摇段倍率，而不是跳过源动画前5帧、也不是把源动画的第8帧当结束。

## B16-4 实际消费者、边界与普通分支

`OrderAttack::SetPlayRate` RVA `0x1AE7760`：保存阶段倍率p到完整order+4A0；动画子实例有效时写SubAnim+0x644=`p*order.m_fPlayRateOverrideMultiplierTotal`。`UpdatePlayRate` RVA `0x1AEB630` 从1重新相乘额外倍率集合，结果写order+49C（`0x1AEB80A–0x1AEB81E`）；总值改变则以当前阶段倍率再次调SetPlayRate（`0x1AEB82D–0x1AEB848`）。它改变真实播放倍率，不改Wanted本身。

本批 `OrderAttack::OnUpdate` RVA `0x1AE23C0`，`buildup-update`日志：

1. `0x1AE25D8–0x1AE2624`：`q=1-clamp(AttackTimeLeft/AttackDuration,0,1)`，`dtClipped=min(dt,AttackTimeLeft)`；读取当前阶段倍率p。
2. 正常无冻结分支 `0x1AE267A–0x1AE2693`：若还未BuildUpOver并且 **q > L/N**，设置BuildUpOver=true，p=1。比较是严格大于，且在该tick推进helper之前发生。
3. `0x1AE26B0–0x1AE26D0`：只有 `!m_bInPrediction && !m_bPlayRateManagedOutside` 才向SetPlayRate写本地p。
4. 非预测 `0x1AE26E6–0x1AE2709`：取子实例AnimContainer最终倍率，乘dtClipped得到实际helper推进量。
5. `0x1AE28CB–0x1AE28D6` 将推进量传入AnimationHelper::UpdateAnimHelperParams。
6. helper更新函数RVA `0x191AAB0`，`0x191AD97–0x191ADB0` 保存旧globalTimeLeft，然后 `globalTimeLeft=max(0,globalTimeLeft−推进量)`。

FAnimContainer::GetFinalPlayRate RVA `0xBE08E0–0xBE08FB`，见 `buildup-clock/buildup-GetFinalPlayRate.asm.txt`：有源动画时，最终倍率=`AnimContainer.m_fPlayRate * sequence.RateScale`；无动画则只返回容器倍率。UAnimSequenceBase+94的RateScale已由PDB类型核实。

因此普通路径的实际倍率为：前摇 `L/W_eff * overrideProduct * sequence.RateScale`，前摇结束后 `1 * overrideProduct * sequence.RateScale`。这是本函数链的倍率分解，未声明任何实战场景中额外倍率恒定为1。

连续时间、正常起点、无冻结/外部管理/追赶、倍率恒定的理想模型：

```text
前摇段时间 = (L/N)*SequenceLength / (L/W_eff * overrideProduct * RateScale)
           = W_eff*SequenceLength/N / (overrideProduct*RateScale)  // L>0
若首判定源动画帧F>=L：
到F时间 = [W_eff + (F-L)] * SequenceLength/N / (overrideProduct*RateScale)
```

当SequenceLength/N=1/60，L13、W_eff8、首判定22且两额外倍率均1，连续模型结果为17个60Hz时间单位（约0.2833秒）。代码实际逐tick推进、严格>才切段，且可能有跨界超进，因此该数值不是已验证实战帧数。上述普通OnStart链另有准入条件 **L>0**，不能将L=0代入并推断该入口会以0倍率播放；具体入口差异见下面B16-4a。

`AnimationHelperParams::GetCurrentFrame` RVA `0x1906E60`，`0x1906E82–0x1906EBB` 返回 `N*clamp(1−GlobalTimeLeft/GlobalDuration,0,1)`，表明判定消费者读取的是推进后的helper动画坐标，而不是Wanted计数器。

### B16-4a 修订：LastBuildupFrame非正值的入口差异

先前本底稿曾将算式直接延伸为“L=0代码直接得到前摇倍率0”，忽略OnStart上游准入；现撤回该笼统表述，以本节取代。

OnStart `0x1ADD130` 明确 `xor edi,edi`；随后至 `0x1ADD346` 没有改写EDI，期间调用按Windows x64约定保存RDI。`0x1ADD33F` 读取m_CurrentAttackData，`0x1ADD346` 比较其+6C（LastBuildupFrame）与EDI=0，`0x1ADD349` 的有符号 `jle 0x1ADE23F` 覆盖L<=0。目的地 `0x1ADE23F–0x1ADE245` 将xmm1清0并调用 `OrderBase::RequestStop(0)`，然后退出OnStart。因此L<=0在这个入口跳过helper初始化、倍率/阶段数据计算及播放设置，并请求停止订单，不能描述成“0倍率播放”。L>0是本节普通OnStart公式的真实适用条件。

另一个函数ComputePhaseInfo RVA `0x1ACAD90` 的入口不同：`0x1ACADA9–0x1ACAE84` 检查m_CurrentAttackData存在并能解析为UAnimSequence，未见OnStart同样的L>0门；通过这些条件后，`0x1ACAFA2–0x1ACAFB8` 直接读取L并除以至少1的effectiveWanted。**仅在该函数已被调用且进入其计算区的条件下**，L=0会将m_fBuildUpScale写为0。函数局部赋值不证明该订单之后以0倍率进入实际播放；本轮不扩查L<=0输入能否经其调用者到达、以及后续生命周期，不把另一入口的局部结果替代OnStart准入结论。

## B16-5 有证据的相关分支

### 目标倍率与整型化

倍率归属于当前攻击的目标防御组件，不是攻击者防御组件。非FightingCharacter目标或没有DefenseComponent时不乘。代码先截断后max1，不能写成浮点Wanted直接参与除法。防御构造默认1由主任务另取 `UDefenseComponent` ctor RVA194C4E0，194C6AB写+1F8=1；这是构造值，不证明全部运行时实例永远1。

### 客户端追赶

OnStart `0x1ADD720–0x1ADD7CF`：仅 `NetMode==3 && !IsPawnMaster(attacker)` 进入。设T=`effectiveWanted*AnimFrameDeltaTime`，elapsed为订单开始tick到当前同步tick的秒差，cap=`attacker+0x880`整数乘AnimFrameDeltaTime；若elapsed>0且 `T−min(cap,elapsed)>0`，额外 `buildUpScale *= T/(T−min(cap,elapsed))`。其余保留原倍率。

ComputePhaseInfo `0x1ACAFC8–0x1ACB097` 还有其入参bool为真的门，再执行同样远端客户端追赶。攻击者+880的正式字段名未在本分支恢复，因此只按偏移陈述cap输入；不擅称网络延迟固定帧数。该分支不是所有本地主控动作的默认前摇。

### 预测与外部倍率管理

`m_bInPrediction` 为OrderBase+100。非预测才读真实动画容器最终倍率；预测分支 `0x1AE27E9–0x1AE280E` 按当前阶段倍率p推进，p负时以BuildUpOver?1:buildUpScale作为替代。预测不会调用SetPlayRate写渲染容器。

`m_bPlayRateManagedOutside` 为完整order+AB8；ActivatePlayRateManagedOutside RVA19E2020 用接口this+908写入，仍需加基类偏移1B0。该标志阻止本地SetPlayRate覆盖，但非预测仍读取容器的实际最终倍率。因此不把正常本地自动前摇公式覆盖到外部管理者行为。

### 冻结栈

`PushFreezeOrder` RVA1AE63C0把ID和m_fRatioOfFreeze附加到栈，并将NewFrozenState=true；`PopFreezeOrder` RVA1AE5C50按ID移除，栈清空才设置NewFrozenState=true。OnUpdate `0x1AE2611–0x1AE2678`：新冻结时若最后freezeRatio尚未落后于当前q，先设置阶段倍率使本tick推进至该比例；已有非空栈时倍率0；释放为无栈的新状态则倍率1。冻结处理优先于正常BuildUpOver切换。不能将含冻结的耗时按Wanted直接算出，也不能假设解冻必定恢复原buildUpScale。

### 非零起点

FNetOrderStructAttack::ctor RVA `0x19218A0`，`0x1921948` 将m_fStartRatio(+F0)初始化0。

OnStart `0x1ADE0EC–0x1ADE177` 检查abs(NetAttack.m_fStartRatio)>约1e-8：成立就从AttackTimeLeft减 `SequenceLength*startRatio`，以相同源秒量预推进helper；默认0则不预推进。这里的起点来自NetAttack，不是下述SequenceContext custom length。同一资产可以由不同订单起点播放，不能把源动画第0帧至判定帧的模型无条件视为按键耗时。

## B16-6 AnimationHelper上下文的已恢复类型

14底稿T2a保留的context+31/+34/+3C现在有匹配类型：

- +31 `m_bUseCustomLength`。
- +34 `m_fCustomSequenceLength`。
- +3C `m_fStartRatio`。
- +38 `m_bUseRootMotion`，+39 `m_bDirectRightMovement`，+3A `m_bMirror`。

SequenceContext构造 RVA `0x1AC4160`：`0x1AC41AA` 清custom-length bool，`0x1AC41AE` customlength=0，`0x1AC41B4` startRatio=0；root motion默认true，DirectRight默认false。

InitParamsFromSequence RVA `0x190BA90`，`0x190BB0F–0x190BB68` 明确：`duration = useCustomLength ? customLength : (1−startRatio)*sequence.SequenceLength`；写helper SequenceLength(+2C)、GlobalDuration(+30)、GlobalTimeLeft(+34)、PreviousGlobalTimeLeft(+38)、NotifyGlobalTimeLeft(+3C)，并在0x190BBB0把context.startRatio保存到helper+44。

正常OrderAttack::OnStart `0x1ADD3E1–0x1ADD43E` 构造默认context，设置镜像DB、directRight、mirror、order owner id后初始化helper；该调用点没有写custom length/startRatio。因此本调用未初始化helper时使用默认custom=false/start=0。若helper已有Init标志，OnStart跳过重新初始化；不能只凭当前构造点否定其他预初始化来源。

## 验证边界与停止位置

完成：本构建字段、虚表this调整、Wanted→倍率→阶段切换→helper动画坐标的静态主链；匹配EXE/PDB全哈希；独立原始日志与结构化布局。未进行游戏实测；未证明149个动作的RateScale、runtime额外倍率、冻结与外部管理分布。

由主任务合并14底稿修订、工具矩阵/复盘与共享进度；本文件不覆盖共享文件。下一步若要产出真正实战帧表，应对指定动作核源动画RateScale与startRatio、实际更新频率和倍率/冻结事件，并比较helper帧推进与命中事件。当前无需用户手工操作。

收尾自动核验：`python -B exports/20261030-前摇语义-16/buildup-verify.py` 最终退出0，检查选定类型字段偏移、Python AST并对32项产物/源脚本计算SHA256。首次核验因某些field条目无name键失败，按field是否含name过滤后通过；不影响此前原始布局产物。知识库全库检查由主任务合并后统一执行，本分支未运行。
