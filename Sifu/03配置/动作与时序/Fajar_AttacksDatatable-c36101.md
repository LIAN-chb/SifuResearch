# Fajar_AttacksDatatable：动画行配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Fajar/Attacks/Fajar_AttacksDatatable.uasset

收录本表全部 18 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。

## 全部动画行

| 行 ID | 动画行名 | 最后前摇帧字段 | 命中帧字段 | 动画引用字段 |
|---|---|---|---|---|
| T001 | Fajar_Attack_Barehands_Light01_01_Front | 18 | 20 | 未保存 |
| T002 | Fajar_Attack_Barehands_Light01_02_Front | 8 | 12 | 未保存 |
| T003 | Fajar_Attack_Barehands_Light01_03_Front | 14 | 16 | 未保存 |
| T004 | Fajar_Attack_Barehands_Light01_04_Front | 22 | 24 | 未保存 |
| T005 | Fajar_Attack_Barehands_Light01_05_Front | 14 | 16 | 未保存 |
| T006 | Fajar_attack_barehands_Head_Palm | 16 | 18 | 未保存 |
| T007 | Fajar_attack_barehands_Swiping_Mantis | 24 | 26 | 未保存 |
| T008 | Fajar_attack_barehands_Rising_Falcon | 24 | 26 | 未保存 |
| T009 | Fajar_attack_barehands_Cobra_Double_Bite | 27 | 36 | 未保存 |
| T010 | Fajar_attack_barehands_Naja_Reverse_Lash | 28 | 34 | 未保存 |
| T011 | Fajar_attack_barehands_Reaper_Deadly_Waltz | 21 | 29 | 未保存 |
| T012 | Fajar_attack_barehands_Knee_Smash | 34 | 36 | 未保存 |
| T013 | Fajar_attack_barehands_Rhino_Trample | 18 | 23 | 未保存 |
| T014 | Fajar_attack_weapons_LeapingSlash | 66 | 67 | 未保存 |
| T015 | Fajar_attack_weapons_Flurry_First | 28 | 29 | 未保存 |
| T016 | Fajar_attack_weapons_Flurry_Second | 18 | 19 | 未保存 |
| T017 | Fajar_attack_weapons_Flurry_Third | 10 | 11 | 未保存 |
| T018 | Fajar_attack_weapons_Razor_Leaf | 46 | 48 | 未保存 |


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
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T015 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T016 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T017 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T018 |
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 是 | T001, T002, T003, T004, T005, T006, T007, T008, T009, T010, T011, T012, T013 |
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 否 | T014, T015, T016, T017, T018 |
| 镜像方法[0] | m_eMirroringMethod[0] | EAttackMirroringMethod::BasedOnQuadrantToTarget | 本表全部行 |
| 镜像采用下一脚步标记阈值[0] | m_fMirrorUseNextFootMarkerThreshold[0] | 0.5 | 本表全部行 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontRight | T001, T002, T003, T006, T007, T008, T010, T015, T016, T017, T018 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::BackRight | T004 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::BackLeft | T005 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontLeft | T009, T011, T012, T013, T014 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontRight | T001, T002, T005, T006, T007, T008, T009, T012, T013, T014, T015, T016, T017, T018 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::BackRight | T003 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::BackLeft | T004 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontLeft | T010, T011 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 154.30748 | T001 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | -8.29386902 | T002 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 64.3676758 | T003 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 105.417389 | T004 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 139.461884 | T005 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 177.918564 | T006 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 208.38002 | T007 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 97.0517578 | T008 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 209.327515 | T009 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 60.8890991 | T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 155.657593 | T011 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 146.821899 | T012 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 59.7197189 | T013 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 391.590485 | T014 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 95.403862 | T015 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 64.6836929 | T016 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 124.144714 | T017 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 39.6697464 | T018 |
| 右向位移长度[0] | m_fMovementRightLength[0] | 0 | 本表全部行 |
| 直接跟随右向位移标志[0] | m_bDirectRightMovementFollow[0] | 是 | 本表全部行 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 18 | T001, T013, T016 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 8 | T002 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 14 | T003, T005 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 22 | T004 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 16 | T006 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 24 | T007, T008 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 27 | T009 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 28 | T010, T015 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 21 | T011 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 34 | T012 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 66 | T014 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 10 | T017 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 46 | T018 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 20 | T001 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 12 | T002 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 16 | T003, T005 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 24 | T004 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 18 | T006 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 26 | T007, T008 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 36 | T009, T012 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 34 | T010 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 29 | T011, T015 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 23 | T013 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 67 | T014 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 19 | T016 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 11 | T017 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 48 | T018 |
| 无打击阶段攻击标志[0] | m_bStrikelessAttack[0] | 否 | 本表全部行 |
| 内部名称[0] | m_Name[0] | None | T001, T002, T003, T004, T005 |
| 内部名称[0] | m_Name[0] | Heavy | T006, T007, T008, T009, T010, T011, T012, T013, T014, T015, T016, T017, T018 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（74 字节） | T001 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（71 字节） | T002 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（73 字节） | T003 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（72 字节） | T004 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（72 字节） | T005 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（72 字节） | T006 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（77 字节） | T007 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T008 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（80 字节） | T009 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（80 字节） | T010 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（82 字节） | T011 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（73 字节） | T012 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T013 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T014 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（75 字节） | T015 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T016 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（75 字节） | T017 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（73 字节） | T018 |


来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 [[03配置/动作与时序/索引]]。
