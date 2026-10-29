# 玩家招式待核08：朝向槽与时间边界

## 构建与输入

当前EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；反汇编工具在每次执行前重算核对。当前PDB stream1 GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d`、age1、字节970231808已重读，与inventory/pdb_overview.json匹配；记录inventory/player-unknown-08-build.json。静态调用与保存配置，不是实战验证。

## Q1：四个槽的含义已经闭合

定向读取PDB类型，产物 `inventory/player-unknown-08-quadrant-types.json`：`EQuadrantTypes`的编译器枚举明确为0=FrontLeft、1=FrontRight、2=BackRight、3=BackLeft，Count4、None5。`FComboNodeAttackInfos.m_Attacks`为偏移0的FName[4]。

`FComboNode::GetAttackName` RVA `0x195ac00` 先调用GetAttackInfos，再检查quadrant<4；基础路径`0x195ad57–0x195ad5f`直接按`r15+quadrant*8`取FName，蓄力路径`0x195ad31–0x195ad50`按档位与quadrant索引取名。因此不是仅按FL/BL资产后缀猜槽位。原始有界反汇编在 `logs/player-unknown-08-quadrant/FComboNode__GetAttackName-0x195ac00.asm.txt`。

`AFightingCharacter::ComputeQuadrant` RVA `0x19b7e30` 由目标方向与骨盆方向调用 `UGameMathTools::ComputeQuadrantFromDirectionVectors`（RVA `0x1b8baa0`）；含缓存／强制状态分支。朝向为对目标的身体／骨盆象限，不保证等同于摄像机前后或玩家单凭移动方向理解的正背。后者函数的正负水平夹角分为四象限；见08-quadrant与08-math目录。

当前保存树全部变体只出现槽[0,1]、[2,3]或[0,1,2,3]：可分别标“正面”“背面”“正背通用”，证据区保留确切前左／前右／后右／后左。左右镜像仍需区分：`UAttackComponent::GetAttackQuadrant` RVA `0x1933c60`镜像时0↔1、2↔3，不跨正背；`USCTools::GetAttackQuadrant` RVA `0x1b92d90`跳转复用此函数。不能把每个资产后缀当成当时未镜像的实际朝向。

## Q2：条件配置比原先不透明摘要更明确，但具体内容仍待恢复

PDB `FComboNode.m_ConditionalAttacks`偏移96，明确类型为`TMap<FGameplayTag,FComboNodeAttackInfos,...>`。`FComboNode::GetAttackInfos` RVA `0x195a9c0`遍历该map，用角色AbilitySystem拥有标签接口测试键，首个命中返回对应Infos；无命中或无角色则返回基础`node+0x20`。这证明条件不是任意数字姿态槽，而是标签选择另一套攻击配置。多键优先级是容器遍历次序，不可编造统一高低优先级。原始反汇编08-quadrant目录；具体保存的标签键／动作集合交由input分支定向解码，未解前保留缺口。

## Q3：前摇保存帧仍不能直接叫实测前摇

例：槽0/1的`MainChar_Jab_FR`引用Jab_HB01，WantedBuildupFrames=8，但命中窗动画坐标为Inclusive22–23。两者不同，不能用22/60代替按键至首次命中。

`OrderAttack::UpdatePlayRate` RVA `0x1aeb630`重新将当前速率设为1，再遍历管理集合相乘，并在变化时更新播放器；`GetInitialPlayRate` RVA `0x19f5b60`读order+0x314。该字段的完整初始化来源尚未追通，不是WantedBuildup消费者的完整闭合。原始在`logs/player-unknown-08-timing/`。所以本次继续显示“前摇配置（实际起手待核）”，不推最终时间；下一定向对象为OrderAttack初始化+0x314的写入者、WantedBuildup配置消费者和击中窗播放器换算。

## 修订范围

07及此前“姿态槽正背面待核”已被Q1静态槽映射缩小：图中树内引用可标正背，实际镜像／摄像机含义不扩张。攻击高度与输入结论见同批height/input底稿，展示生成逻辑应分别采用证据，不能拿目标部位或攻击强度替代上中下段。
