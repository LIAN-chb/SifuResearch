# 玩家招式名称12：官方本地化取证

用户要求查询实际游戏官方称呼，例“推击接重击＝追亡逐北”，暂不填图。查询展示表在`exports/20261029-玩家招式名称-12/官方招式名称对照.md`。本页只记录来源与边界。

## N01：名称来自当前本机游戏包

源包`E:/Games_Little/Epic/Sifu/Sifu/Content/Paks/pakchunk0-WindowsNoEditor.pak`，复用V11／79253文件索引与31101086834字节包标识。定向提取`Sifu/Content/Localization/Game/`下en/Game.locres、zh-Hans/Game.locres与Game.locmeta，分别209853、178121、43字节，共388017字节。只写12/extracted，提取前断言目录不存在，包size/mtime前后一致。不为查询全读31GB计算包SHA，也不声称重核整个包；逐文件哈希与工具命令（密钥脱敏）见12/extraction-manifest.json。

LocRes版本3。读取魔数、字符串池、namespace/key/source hash和索引，检查两段完全消费至边界／文件尾、无重复键、索引在范围内。英文2690条、简中2648条；namespace/key/source hash完全一致配对2648条。英文独有42条，含8条技能输入action标记。初次假设两语言键集合相同的断言失败，检查后改用精确交集，不把缺失项补成空译文；没有source hash冲突。

格式核对[CUE4Parse LocRes实现](https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Localization/FTextLocalizationResource.cs)与[FTextKey实现](https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Objects/Core/i18N/FTextKey.cs)，只用于读取格式；名称证据来自游戏原文件。源码读取日2026-10-29，自写有界读取器12/read-localization.py，未下载运行第三方库。

## N02：追亡逐北的名字、输入、说明来自同一对象

资产`Sifu/Content/DB/Skills/Techniques/SkillGameplay_Technique_PostPushbackKnockdown.uasset`，SkillUIData_C_0（export3）。uasset SHA256 `8969c14c24910e86bd05e8b0690beed2acc52dc29099180499091a7754d3e40b`；uexp SHA256 `a9c123514c258985d8ccf504f85f7957555174efae73ce2466d5867eeb70e464`。原uasset核对旧metadata，通过export边界与tag valueOffset取每个字段，再核原opaque字段SHA。

| 字段 | uexp偏移 | 文本键 | 官方文本或含义 |
|---|---|---|---|
| Name | 407 | SkillTitle_Technique_PostPushbackKnockdown | 追亡逐北／Chasing Trip Kick |
| Description | 587 | SkillDesc_Technique_PostPushbackKnockdown | 推击后迫步跟进并放倒对手 |
| Inputs | 671 | SkillInput_Technique_PostPushbackKnockdown | action=AttackHeavy，对被推击的对手 |

三字段均FText History11（StringTableEntry），含确切表资产FName与key。字段读取格式核对[CUE4Parse FText实现](https://raw.githubusercontent.com/FabianFG/CUE4Parse/master/CUE4Parse/UE4/Objects/Core/i18N/FText.cs)；只实现观察到的History11和Base0，检查每块完全消费。表分别为ST_UI_SkillTree和ST_UI_SkillTree_Inputs，各key在语言表中均唯一精确对应。

独立菜单namespace ST_UI_MenuCombo、key Special_PostPushedY同为追亡逐北；中文entry offset51911、英文52638。推击后轻击对应另一技能PostPushbackDamage，Name为乘胜追击、Inputs明确AttackLight。因此示例对应不依赖变量名直译。

## N03：覆盖及层级

菜单ST_UI_MenuCombo共68条：52条Command/Special/BaseCombo命名项、16条分类／提示／效果。命名项25条无武器限定、27条武器限定，共43个去重中文名；不是游戏实战动作数。菜单key编码不是独立手势证据；技能UI的action标记为更直接来源。

检查已有46个SkillUIData导出所保存字段：28对象81个StringTable引用接通；另28个Base字段属于14组Name/Description，多为Dummy或占位，单列不混入正式名表；4对象没有这些相关保存字段。28个接通对象中OLD路径2项排除主表，其余13个Technique、13个其他技能／专注。8条简中缺失的输入标记保留英文原文，不伪造译文。

命名要区分：疾风连环是BaseCombo_XXXXX／Light Attacks的整套连段菜单标题，不给每一击套此名；BaseCombo_YYYY的中文确为重击。正背配置归并来自图中位置，一个官方名是否适用每个成员须核动作引用。24个Cheat替换招式标题另列，不混入默认徒手；同名不同英文或武器也不自动归同一招。

官网英文交叉见notes/player-move-names-12-web.md；第三方攻略只作线索，未进入官方名确认表。官网不足以给出完整简中表，中文以本机官方资源为准。

## 停止边界

已经连接正式名称与技能UI输入，尚未验收33图节点的逐配置命名；未恢复菜单蓝图排版／显示条件，未启动游戏。不把每条随包文本当当前可用动作。图HTML、模板、生成器和编辑器前后SHA不变，报告在本批verification.json。
