# 招式待核08：攻击高度与可避方向

结论：已明确防御／可避方向掩码及其枚举，不能据此将每个动作压成唯一上／中／下段。建议详情显示“可避方向（配置）”，逐命中段保留；攻击高度继续待核。EAttackTarget::High也应保留“命中目标部位”的语义，尚无消费者证据把它等同玩家可下潜的上段。

## H01 构建与主来源

当前EXE只读SHA256为a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254，与inventory/pdb_overview.json一致。该索引记录EXE CodeView与PDB info GUID fdd64e0f-b9ed-4479-8fd8-efe0038b919d、age1匹配。本子任务未重新计算PDB全文件哈希；类型输出仍绑定该路径和970231808字节PDB。脚本与输出见inventory/player-unknown-08-height-enums.json和各*-disassembly.json；反汇编器每次核EXE哈希后才运行。

## H02 字段与枚举

现有inventory/player-combo-type-layouts.json → FHitboxDataRow：m_iHitboxDefenseMatrix偏移564(0x234)，m_iAvoidableDefenseMatrix偏移568(0x238)，均32位整数字段。07图每个window.raw已有这两个保存值，不需重新解包。

TPI定向查EAvoidableDefenseMatrix、EHitBoxDefenseMatrix均未找到，失败记录为inventory/player-unknown-08-height-types.json；logs/player-unknown-08-height-types.py是定向改输出路径的原类型读取器副本，不覆盖旧索引。

改由匹配EXE的反射注册表恢复枚举。logs/player-unknown-08-height-enums.py核哈希后读取PE节映射、精确枚举名字符串的VA引用及相邻int64。连续FEnumeratorParam数组为VA0x1449c5ba0(5项)、0x1449c5cc0(4项)。注册函数Z_Construct_UEnum_Sifu_EAvoidableDefenseMatrix RVA0x1c7ece0传FEnumParams VA0x145a0ce90；另一函数RVA0x1c7ee30传VA0x145a0ced0；两者Params+32明确引用对应数组，形成注册参数→连续枚举数组→字符串/值证据链。

| 枚举 | 位值 |
|---|---|
| EAvoidableDefenseMatrix::None | 0 |
| Jump | 1 |
| Duck | 2 |
| SideLeft | 4 |
| SideRight | 8 |
| EHitBoxDefenseMatrix::None | 0 |
| Dodge | 1 |
| Deflect | 2 |
| Guard | 4 |

logs/player-unknown-08-height/UHitboxHelper__execBPF_MirrorAvoidDefenseMatrix-0x1c7f5e0.asm.txt中RVA0x1c7f6da～0x1c7f6f3：启用镜像时保留mask&3，4映到8，8映到4。支持左右为侧向位、低两位不随镜像变化。不能根据数字14的大小判断攻击高低。

07树内61动作90窗口分布：防御mask／可避mask为7/12共35、7/14共22、7/2共18、0/0共6、7/1共4、1/14共3、7/0共2。完整资产/表行/值见枚举JSON tree_windows。12=左右侧闪，14=下潜与左右侧闪，2=下潜，1=跳避，0=无这些保存方向；这些是配置位的解码，不保证绕过其他条件即可实战成功。防御mask7为Dodge/Deflect/Guard三位齐全，不能等同所有攻击必定可防。

## H03 消费者与未闭合处

UDefenseComponent::GetActiveAvoidMatchingAttack两个重载RVA0x195a360、0x195a5d0读取活动窗口和候选闪避类型，调用UAvoidDB::AreAvoidAndAttackMatching。该函数RVA0x1928450还检查方向及调用UAvoidMatchCondition::BPE_DoesAvoidMatch；短重载RVA0x1928880在类型小于7时直接分派这个事件。底稿见logs/player-unknown-08-height-consumer与-height-match。这条链未证明某个Jump位就是唯一“下段”，需接具体AvoidMatchCondition蓝图／默认对象和指令实现。FilterHit在RVA0x195828c与0x195846a测试命中表+0x234的Dodge位，进一步支持防御mask是能力通道而非高度分类。

按parent提示额外查询UMenuDB::BPF_GetAttackAvoidIcon精确函数不在PDB过程索引（height-icon-disassembly.json已留失败）；exec包装存在，RVA0x1caa8b0，读取小于7的输入枚举后按40字节条目取[rsi+index*40+0x958]软引用图标（height-icon-exec日志）。它是按闪避类型取图标，未见Jump/Duck到“上段/下段”文字映射，不能扩大结论。

## 执行与边界

命令：python logs/player-unknown-08-height-types.py；python logs/player-unknown-08-height-enums.py；python scripts/disassemble_research.py --group player-unknown-08-height --name Z_Construct_UEnum_Sifu_EAvoidableDefenseMatrix --name Z_Construct_UEnum_Sifu_EHitBoxDefenseMatrix --name UHitboxHelper::execBPF_MirrorAvoidDefenseMatrix；另外group后缀consumer、match、icon、icon-exec分别查本文上述函数。成功反汇编均退出0；精确非exec图标查询记录missing；一次参数表偏移假设+24断言失败，实际检查修正为+32并重跑通过；未覆盖旧研究结果。一次交互python exec缺__file__失败，后改正式脚本执行。原始日志有SHA与工具路径，当前Python版本记录在枚举JSON。

仅写本底稿及player-unknown-08-height前缀原始输出，不改主图／进度，不运行游戏、不声称实战完成。可供parent使用的是明确枚举和值、逐表行mask；唯一上／中／下段判定仍未闭合。
