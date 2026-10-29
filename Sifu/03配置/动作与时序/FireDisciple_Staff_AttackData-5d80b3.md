# FireDisciple_Staff_AttackData：动画行配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/FireDisciple/Attacks/FireDisciple_Staff_AttackData.uasset

收录本表全部 11 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。

## 全部动画行

| 行 ID | 动画行名 | 最后前摇帧字段 | 命中帧字段 | 动画引用字段 |
|---|---|---|---|---|
| T001 | Disciple_Attack_Staff_Combo_EngageSlashes | 21 | 30 | 未保存 |
| T002 | Disciple_Attack_Staff_Combo_DirectAttack | 18 | 25 | 未保存 |
| T003 | Disciple_Attack_Staff_Combo_LowSweep | 26 | 32 | 未保存 |
| T004 | Disciple_Attack_Staff_SlamOTG | 34 | 43 | 未保存 |
| T005 | Disciple_Attack_Staff_ChopDisengage | 21 | 28 | 未保存 |
| T006 | Disciple_Attack_Staff_Push | 20 | 24 | 未保存 |
| T007 | Disciple_Attack_Staff_DownSlash | 20 | 26 | 未保存 |
| T008 | Disciple_Attack_Staff_Thrust | 18 | 26 | 未保存 |
| T009 | Disciple_Attack_Staff_Combo_DoubleHitEngage | 21 | 31 | 未保存 |
| T010 | FireDisciple_Staff_Combo02_FallingVerticalCrush | 30 | 39 | 未保存 |
| T011 | FireDisciple_Staff_Combo02_DoubleHitFinisher | 20 | 27 | 未保存 |


## 全部保存字段的配置分布

同值字段按适用行 ID 合并，保留全部已解析字段。行 ID 在本页内有效。

| 中文标识 | 原字段路径 | 配置值 | 适用行 ID |
|---|---|---|---|
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T001 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T002 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T003 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T004 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T005 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T006 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T007 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T008 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T009 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T010 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T011 |
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 否 | 本表全部行 |
| 镜像方法[0] | m_eMirroringMethod[0] | EAttackMirroringMethod::BasedOnQuadrantToTarget | 本表全部行 |
| 镜像采用下一脚步标记阈值[0] | m_fMirrorUseNextFootMarkerThreshold[0] | 0.5 | 本表全部行 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontRight | T001, T002, T003, T004, T005, T006, T007, T008, T009 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontLeft | T010, T011 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontRight | T001, T002, T003, T004, T005, T006, T007, T008, T009, T011 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontLeft | T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 327.619171 | T001 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 152.782974 | T002 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 197.057037 | T003 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 207.541855 | T004 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | -152.334778 | T005 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 37.7795944 | T006 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 80.5964203 | T007 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 53.8620796 | T008 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 322.666351 | T009 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 178.015152 | T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 54.3030396 | T011 |
| 右向位移长度[0] | m_fMovementRightLength[0] | 0 | 本表全部行 |
| 直接跟随右向位移标志[0] | m_bDirectRightMovementFollow[0] | 是 | 本表全部行 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 21 | T001, T005, T009 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 18 | T002, T008 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 26 | T003 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 34 | T004 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 20 | T006, T007, T011 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 30 | T010 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 30 | T001 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 25 | T002 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 32 | T003 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 43 | T004 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 28 | T005 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 24 | T006 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 26 | T007, T008 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 31 | T009 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 39 | T010 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 27 | T011 |
| 无打击阶段攻击标志[0] | m_bStrikelessAttack[0] | 否 | 本表全部行 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Combo_EngageSlashes | T001 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Combo_DirectAttack | T002 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Combo_LowSweep | T003 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_SlamOTG | T004 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_ChopDisengage | T005 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Push | T006 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_DownSlash | T007 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Thrust | T008 |
| 内部名称[0] | m_Name[0] | Disciple_Attack_Staff_Combo_DoubleHitEngage | T009 |
| 内部名称[0] | m_Name[0] | FireDisciple_Staff_Combo02_FallingVerticalCrush | T010 |
| 内部名称[0] | m_Name[0] | FireDisciple_Staff_Combo02_DoubleHitFinisher | T011 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（119 字节） | T001 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（117 字节） | T002 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（109 字节） | T003 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（101 字节） | T004 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（113 字节） | T005 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（95 字节） | T006 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（105 字节） | T007 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（99 字节） | T008 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（123 字节） | T009 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（121 字节） | T010 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（124 字节） | T011 |


来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 [[03配置/动作与时序/索引]]。
