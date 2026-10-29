# 状态机制规格：精确条件复核与前版修订

本批20261029-机制规格-02，不运行游戏。绑定当前EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`、PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age1。已有函数原文复用匹配清单，不重跑反汇编。

## P1：状态集合和查询顺序

`GetHighestActiveFightingState` RVA `0x195C370`读取状态数组，按常量区RVA `0x4876A28`的9字节搜索。当前EXE重新核SHA后读取：`7,4,3,2,6,8,5,1,0`；对应类型以 `inventory/followup-hitted-type-layouts.json` 枚举核对，Counter_Hit=2，Parried=8。完整小产物 `inventory/state-spec-20261029-priority.json`。顺序是查询投影，不是数组覆盖／互斥规则。

## P2：旧眩晕重建的完整前置守卫

`UpdateFightingStateFromImpact` RVA `0x1A70A70`：`0x1A70B86–0x1A70BF1`。

先定义newGuardBreak=`Impact+8 && !Impact+0x1A`。已有Dizzy、候选不是KnockedDown、且〔旧subtype!=1或newGuardBreak〕才进入旧Dizzy处理体。处理体内ImpactType==0时搬运n/d/subtype，可能由全局StructureOnly先加n，令候选Dizzy；随后不论此处是否为Hit都Pop命中组件跟踪的Dizzy句柄。条件假则跳过此处理体。Pop受句柄匹配条件约束，不声称任意Dizzy元素都被删。

`0x1A70BF8–0x1A70C6D`随后重新检查KnockedDown，故此处Dizzy是否存在是T1之后的事实。倒地继承次数要求候选KnockedDown、仍无Dizzy、GuardBreak=false及AlreadyGuardBroken=false；两个false不能弱化为newGuardBreak=false。

`0x1A70C6D–0x1A70D5D`：新破架势先建相应状态；候选None提前结束新命中状态Apply；否则候选非Dizzy且AvoidDizzy及SuperDizzyAvailable均真时先额外Apply Dizzy/SuperDizzy，然后仍Apply原候选。不能把函数概括为“只给一个新状态赋值”。

## P3：保时长开启但旧状态不存在，不回退默认时长

`ApplyFightingStateFromImpact` RVA `0x1A46990`，普通局部duration在 `0x1A46AB9`置0。攻击侧keep分支 `0x1A46B4F–0x1A46B83`，查询不存在时 `0x1A46B76`直接跳 `0x1A46BDF`，绕过 `0x1A46BBC`默认计算和 `0x1A46BD7`外部offset相加。因此普通基线仍为0，之后仍可受倒地/Dizzy余时、StructureBroken保持等附加处理改变，不称最终所有配置时长都0。

旧底稿时长树E行曾写“没有可用当前状态则GetDuration”，这是误读，现修正，并保留本段缘由。目标Reaction keep的F行未找到旧状态才回退默认计算，不能把E/F合成同一回退。

## P4：动画分支的条件和两个时间来源

匹配PDB字段：FImpactResult+0x1D=`m_eImpactType`；+0x94=`m_fInstigatorFreezeDuration`；+0x0A=`m_bSuperDizzyAvailable`。与FAttackPropertyLevel+8眩晕等级结合：有有效动画容器、T=Dizzy、且〔眩晕等级为0或ImpactType=Hit〕时，`0x1A46AF6–0x1A46B2E`优先走GetAnimDuration＋攻击方冻结时间。不是按未映射的“动画开关”概括。

动画路径在 `0x1A46B25`加Impact+0x94，跳 `0x1A46BDF`；自定义路径也直接跳该点，所以自定义值不再走 `0x1A46BD7`的函数入参offset相加。SuperDizzy mandatory路径单独加该函数入参offset。规格分别命名A、F、τ，避免合并。

## P5：许可是有效上下文的输出，非状态名称自带常量

复用E20：Push状态创建上下文；NPC IsAvailable消费首个排序后的BasicGameplay上下文；GenericNone实际被选用时，四项防御许可不允许。不能简化为“任何Dizzy存在都无条件压过所有并存上下文”。Pop回收自己的上下文，后续有效输出需重新解析。此处不新增更高优先上下文运行时实例。

## 证据覆盖与修订传播

本次逐分支复读Update完整函数、Apply相关时长及参数组装段、OnDamage/OnHit完整函数、Tick退出段和Highest函数；未完整恢复ComputeImpactType所有候选选择、GetDuration内部、最终动作准入。

规格T0–T6／D1–D9／U1–U7／A1–A6与上述函数段对应。正文和简要实现以新源 `notes/reader-sources/20261029-state-spec` 为准；旧状态底稿E行同步修正；前版阅读源和页面保留备份身份，不作为当前权威规则。配置释义补充许可有效上下文前提和准确时长回退。
