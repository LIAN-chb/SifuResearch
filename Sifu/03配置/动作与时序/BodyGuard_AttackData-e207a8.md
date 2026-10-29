# BodyGuard_AttackData：动画行配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Bodyguard/Attacks/BodyGuard_AttackData.uasset

收录本表全部 14 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。

## 全部动画行

| 行 ID | 动画行名 | 最后前摇帧字段 | 命中帧字段 | 动画引用字段 |
|---|---|---|---|---|
| T001 | BodyGuard_attack_barehands_hook_front_01 | 30 | 40 | 未保存 |
| T002 | BodyGuard_attack_barehands_stomachPunch_front_02 | 7 | 12 | 未保存 |
| T003 | BodyGuard_attack_barehands_stomachPunchFinisher_front_03 | 18 | 26 | 未保存 |
| T004 | BodyGuard_attack_barehands_KneeGrab_front_04 | 30 | 40 | 未保存 |
| T005 | BodyGuard_attack_barehands_SpinningElbow_front_01 | 28 | 32 | 未保存 |
| T006 | BodyGuard_attack_barehands_SpinningElbowFollow_front_01 | 10 | 14 | 未保存 |
| T007 | BodyGuard_attack_barehands_DoubleSpinningElbow_front | 28 | 32 | 未保存 |
| T008 | BodyGuard_attack_barehands_GrabTakedown | 24 | 30 | 未保存 |
| T009 | BodyGuard_attack_barehands_DoubleHitUppercut_front | 26 | 30 | 未保存 |
| T010 | BodyGuard_attack_barehands_GroundAttack | 20 | 24 | 未保存 |
| T011 | BodyGuard_attack_barehands_LowKick | 20 | 28 | 未保存 |
| T012 | BodyGuard_Attack_barehands_UshiroYokoGeri | 33 | 38 | 未保存 |
| T013 | BodyGuard_attack_barehands_Disarm | 22 | 24 | 未保存 |
| T014 | BodyGuard_Attack_Barehands_KneeSmash | 28 | 30 | 未保存 |


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
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T012 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T013 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T014 |
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 是 | 本表全部行 |
| 镜像方法[0] | m_eMirroringMethod[0] | EAttackMirroringMethod::BasedOnQuadrantToTarget | 本表全部行 |
| 镜像采用下一脚步标记阈值[0] | m_fMirrorUseNextFootMarkerThreshold[0] | 0.5 | 本表全部行 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontLeft | T001, T003, T004, T005, T007, T008, T009, T010, T011 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontRight | T002, T012, T013, T014 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::BackLeft | T006 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontRight | T001, T005, T010, T012, T013 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontLeft | T002, T003, T004, T006, T007, T008, T009, T011, T014 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 152.020981 | T001 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 95.5596313 | T002 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 72.4939499 | T003 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 142.324097 | T004 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 6.49094439 | T005 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 12.8378716 | T006 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 176.876236 | T007 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 397.565491 | T008 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 187.967865 | T009 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 49.97155 | T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 50.2697372 | T011 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 303.47937 | T012 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 129.70993 | T013 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 0 | T014 |
| 右向位移长度[0] | m_fMovementRightLength[0] | 0 | 本表全部行 |
| 直接跟随右向位移标志[0] | m_bDirectRightMovementFollow[0] | 是 | 本表全部行 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 30 | T001, T004 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 7 | T002 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 18 | T003 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 28 | T005, T007, T014 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 10 | T006 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 24 | T008 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 26 | T009 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 20 | T010, T011 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 33 | T012 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 22 | T013 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 40 | T001, T004 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 12 | T002 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 26 | T003 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 32 | T005, T007 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 14 | T006 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 30 | T008, T009, T014 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 24 | T010, T013 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 28 | T011 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 38 | T012 |
| 无打击阶段攻击标志[0] | m_bStrikelessAttack[0] | 否 | 本表全部行 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_hook_front_01 | T001 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_stomachPunch_front_02 | T002 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_stomachPunchFinisher_front_03 | T003 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_KneeGrab_front_04 | T004 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_SpinningElbow_front_01 | T005 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_SpinningElbowFollow_front_01 | T006 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_DoubleSpinningElbow_front | T007 |
| 内部名称[0] | m_Name[0] | None | T008, T013 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_DoubleHitUppercut_front | T009 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_GroundAttack | T010 |
| 内部名称[0] | m_Name[0] | BodyGuard_attack_barehands_LowKick | T011 |
| 内部名称[0] | m_Name[0] | BodyGuard_Attack_barehands_UshiroYokoGeri | T012 |
| 内部名称[0] | m_Name[0] | BodyGuard_Attack_Barehands_KneeSmash | T014 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（114 字节） | T001 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（130 字节） | T002 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（147 字节） | T003 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（131 字节） | T004 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（118 字节） | T005 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（130 字节） | T006 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（127 字节） | T007 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（72 字节） | T008 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（123 字节） | T009 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（107 字节） | T010 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（97 字节） | T011 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（105 字节） | T012 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（66 字节） | T013 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（80 字节） | T014 |


来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 [[03配置/动作与时序/索引]]。
