# 前摇语义16：标记消费者与HitBox动画时钟

## 范围、输入与执行

本底稿只覆盖当前本机构建静态代码，不含实战观测。受父批次委派，写入限于本文件、`exports/20261030-前摇语义-16/hitclock-*`、`logs/hitclock16-*`，共享进度/交接由父批归并。

已读 PROJECT、AGENTS、research-workflow、tool-capabilities、capability-discovery、ADR索引及14批timing底稿。复用 `scripts/disassemble_research.py`：只改清单落点以避免共享inventory写入，保留定向PDB范围与EXE哈希门禁。`hitclock-run.py`重新核EXE SHA256=`a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；实时读取PDB stream1确认GUID=`fdd64e0f-b9ed-4479-8fd8-efe0038b919d`、age=1与既有EXE调试目录索引一致；未全量重哈希PDB。游戏/存档只读。

命令（cwd研究根目录）：`python -B exports/20261030-前摇语义-16/hitclock-run.py`、`python -B exports/20261030-前摇语义-16/hitclock-extra.py` 均退出0，分别12、4个过程无缺失。`hitclock-types.py`复用inspect_types输出412布局，退出0；OrderAttack字段列表在已有解析器范围内只到方法，未据此伪造私有字段名。类型直接复用/抽查 `inventory/player-combo-type-layouts.json` 的 FAttackDataRow/FComboAttack/FHitBox/FFrameRange，与新 `hitclock-types.json` 的AnimationHelperParams/EAttackStates/TRange一致。

原始反汇编见 `logs/hitclock16-disassembly/` 与 `logs/hitclock16-extra/`；逐过程范围/哈希见本批两个hitclock-*-disassembly.json。build报告见hitclock-build.json。本文RVA均=反汇编VA减0x140000000。

## H1：m_fHitFrame不是GetLastHitFrame的来源

PDB：FAttackDataRow+0x6C=`m_iLastBuildupFrame`，+0x70=`m_fHitFrame`；FComboAttack+0xE8=`m_HitBoxes`，FHitBox+0x30=`m_FrameRange`，其m_Anim下界Type/Value=+30/+34，上界=+38/+3C，stride=0x298。

`FComboAttack::GetLastHitFrame` RVA0x195C7F0：

1. 解析动画表行成功则以表+6C LastBuildup初始化结果；缺行初值0（195C913）。
2. 动画引用必须为有效UAnimSequence，否则返回该初值。
3. 遍历该ComboAttack的全部HitBoxes，调用`IsActivationConditionValid`，无效者跳过（195C970–980）。
4. 有效者上界Type!=2时取+3C Value；Type=2取动画的帧数虚函数（195C982–99F）；对结果取max（195C9A2）。

所以该函数求“至少LastBuildup、且考虑当前参与者激活条件的最晚HitBox上界”，不是读取表m_fHitFrame。类型2为Open。不能把LastHitFrame与m_fHitFrame同名化。

OnStart RVA0x1ADC9C0，1ADD604–664以及ComputePhaseInfo RVA0x1ACAD90，1ACAE8A–AF0A：写order+5AC=LastBuildup/NumFrames；order+5B0=GetLastHitFrame/NumFrames。这些字段按OrderAttack完整对象基址，接口子对象基址须减0x1B0。后者不是表20/126。

## H2：已接通的m_fHitFrame用途是空间/位移取样参考

OnStart 1ADDA19读取动画表+70，除NumFrames存order+4C0；随后调用`UAttackComponent::ComputeAttackAnimReachAndIntermediaryTranslationLengths`。

该函数FAttackDataRow重载RVA0x192E480在192E4C5直接读表+70，除NumFrames，转发float重载RVA0x192E4F0。float重载：

- 在ratio=1抽取根轨道变换，减helper初始根变换某前向分量，写第一个输出（192E552–590）。
- 在m_fHitFrame/NumFrames处抽取根轨道变换，减相同初始根分量，写第二个输出（192E5B0–5D4）。
- 从全局FName 0x145CC3940查骨骼索引，在同ratio调用GetBoneTransformInComponentSpace，再组合变换，取骨骼相对该ratio根骨前向分量，写第三个输出（192E6CD–72A）。骨名本批未恢复，不能确定称手骨。

OnStart三个输出位置=order+4B0/+4B8/+4B4，1ADDA63–A94又参与攻击位移比例计算。OnUpdate 1AE26A0比较当前播放ratio与+4C0，超过后置+582=1。该布尔完整字段名由父批继续恢复，本文只报告比较与写入，不擅自命名“已命中”。

这证明m_fHitFrame至少服务于攻击触及/位移的动画取样参考与一个过点标志；不能从该字段20推导“第20帧碰撞/命中”。尚未穷举全部消费者。

## H3：HitBox直接比较动画帧，未先转换成固定实时时间

`AnimationHelperParams::GetCurrentFrame` RVA0x1906E60，1906E82–EBB：

`frame = NumFrames * clamp(1 - m_fGlobalTimeLeft / m_fGlobalDuration, 0, 1)`；动画弱引用无效则返回0。PDB offsets：helper+30 GlobalDuration，+34 GlobalTimeLeft，+38 PreviousGlobalTimeLeft，+44 RatioAtStart。

`AnimationHelper::UpdateAnimHelperParams` RVA0x191AAB0，191AD97–DB0：保存oldLeft到+38，写+34=max(0,oldLeft-effectiveDT)。

`OrderAttack::OnUpdate` RVA0x1AE23C0，1AE2877先取旧动画帧；1AE28D6传入有效动画增量更新helper；1AE28E2再取新动画帧；1AE2930写动画组件对象+858（普通路径）或+860（预测路径）。交叉核父批修正解析器生成的`exports/20261030-前摇语义-16/buildup-types.json`：完整OrderAttack+494=`m_AttackComponent`，类型为`TWeakObjectPtr<UAttackComponent,FWeakObjectPtr>`。因此这里是UAttackComponent+858/+860；本稿未恢复这两个float的声明字段名。

`OrderAttack::EnumerateActiveHitBoxes` RVA0x1AD0490（此函数this为接口子对象）：读UAttackComponent+858当前动画帧，枚举order+AC8缓存HitBoxes。接口this在+1B0，函数内weak偏移+2E4，相加恰为完整OrderAttack+494，与父批新布局m_AttackComponent相符。调用模板`FComboAttack::EnumerateWindowIndexesAtFrame<FHitBox,FHitBox>` RVA0x1AC2C00：直接对每个m_FrameRange.m_Anim做边界Contains。Type=2为无界；Type=1为包含；其余已观察Type=0为排除，故[22,23]是动画帧范围包含关系，不是“22除60后的固定墙钟区间”。该模板只筛窗口；callback后仍有激活条件等规则，窗口存在不等于实际成功命中。

OnStart复制/缓存HitBox条目见1ADD007–08C；本次未发现把缓存+30/+38端点按分段倍率改写成实时时间的代码。正面命中检测还处理跨帧区间与补采样：`UpdateExtraSamplingHitBoxes` RVA0x1AE9E70，将本次旧/新动画帧细分，计算细分区间与窗口交集（1AEA072–0B3），交集端点再经`GetRatioFromFrame`用于位置取样（1AEA11B/12F）。因此不应把逐tick离散采样视为“低帧率必然错过22–23”。完整碰撞/发送链本稿未重做。

## H4：变速、起点、冻结影响的是抵达动画坐标的过程

OnUpdate在1AE25D8起使用order+490/+4C8控制的播放ratio；存在freeze栈时1AE2675把局部倍率置0；普通路径1AE26F9取`FAnimContainer::GetFinalPlayRate`，乘本次受剩余长度限制的delta（1AE2709），最后传helper.Update。因此动画标尺端点仍是22–23，抵达这些点的墙钟时间随播放进度改变。

同一函数1AE2683用播放ratio>LastBuildup/NumFrames置order+581，并将局部倍率回1。这是“13末”与之后阶段速度的真实消费者之一；不能据此把14–21称不存在的空白状态。

起点由helper GlobalTimeLeft/Duration决定；GetCurrentFrame没有另外给HitBox端点减RatioAtStart。旧14批InitParamsFromSequence对上下文覆盖的证据仍适用；实际选用起点与初始赋值由父批其他取证负责。这里仅证明比较坐标和时钟推进，不假设本次Jab总从0起。

## H5：对13末、20参考点、22首次窗口的可支持解释

`FComboAttack::GetAttackStateAtFrame` RVA0x195AE00：先将输入动画帧截断成int；<=LastBuildup(13)时返回BuildUp=0（195AF9B–FA6）；>GetLastHitFrame时返回Release=2（195AFC3–FD7）；中间路径调用窗口查找后返回Strike=1（195AFDC–B05D）。PDB枚举0/1/2明确对应BuildUp/Strike/Release。该状态函数调用GetLastHitFrame时把第二Actor参数置null（195AFB3），不同于OnStart传入两个Actor；有依赖该Actor的激活条件时两处最晚窗阈值不能未经核对视为相同。换言之，实际执行中**Strike状态并不要求当前帧正在HitBox窗口内**。

因此配置13到22的距离是两个独立作者数据定义之间的间隔：13用于分段/状态与变速边界，20是空间取样参考，22才是该HitBox动画下界。14–21可处于程序Strike状态，同时没有该HitBox的判定窗口。不能将该程序状态直接翻译为玩家帧表“攻击判定生效”。

这不是把术语套回数据：状态分支明确允许此间隔。仍未知的是作者为何把该招这些标记选在13/20/22（例如手臂动画、距离对齐、美术或碰撞体设计）；没有编辑器源数据/运行时观测，本稿不给动机猜测。动画窗口静态22也不能单独证明玩家按键后第22个游戏帧首次伤害。

## 验证边界与断点

自动执行验证了输入EXE哈希、实时PDB GUID/age、所列过程存在与反汇编成功；布局核对用于字段归属。未实战测试、未证明当前条件必激活、未穷举所有m_fHitFrame消费者。收尾交叉布局核查未重跑大范围PDB解析；只读取父批新布局的OrderAttack+494并复核接口调偏。父批可复核此处算法并合并用户阅读解释；下一步如需完整墙钟时间，应接通实际helper起点、最终倍率/冻结、预测上下文，并观察当前Jab执行路径。无用户手动操作要求。
