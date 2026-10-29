# MainChar_Throwables：动画行配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/_MainChar/Combos/MainChar_Throwables.uasset

收录本表全部 21 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。

## 全部动画行

| 行 ID | 动画行名 | 最后前摇帧字段 | 命中帧字段 | 动画引用字段 |
|---|---|---|---|---|
| T001 | MC_man_throwable_light_low_FL | 16 | 18 | 未保存 |
| T002 | MC_man_throwable_light_low_BR | 16 | 18 | 未保存 |
| T003 | MC_man_throwable_light_mid_FL | 9 | 11 | 未保存 |
| T004 | MC_man_throwable_light_mid_BR | 9 | 11 | 未保存 |
| T005 | MC_man_throwable_heavy_low_FL | 18 | 20 | 未保存 |
| T006 | MC_man_throwable_heavy_low_BR | 22 | 24 | 未保存 |
| T007 | MC_man_throwable_light_closeRange_low_FR | 12 | 16 | 未保存 |
| T008 | MC_man_throwable_light_closeRange_low_BR | 12 | 16 | 未保存 |
| T009 | MC_man_throwable_heavy_closeRange_low_FL | 19 | 21 | 未保存 |
| T010 | MC_man_throwable_heavy_closeRange_low_BL | 19 | 21 | 未保存 |
| T011 | MC_man_throwable_fromPickup_bottle_FL | 11 | 18 | 未保存 |
| T012 | MC_man_throwable_fromPickup_bottle_BR | 11 | 20 | 未保存 |
| T013 | MC_man_throwable_fromPickup_bats_FL | 11 | 18 | 未保存 |
| T014 | MC_man_throwable_fromPickup_staff_FL | 11 | 18 | 未保存 |
| T015 | MC_man_throwable_fromPickup_staff_BL | 11 | 18 | 未保存 |
| T016 | MC_man_throwable_light_closeRangeFromPickup_low_FR | 12 | 16 | 未保存 |
| T017 | MC_man_throwable_light_closeRangeFromPickup_low_BR | 12 | 16 | 未保存 |
| T018 | MC_man_throwable_Staff_low_FL | 16 | 18 | 未保存 |
| T019 | MC_man_throwable_Staff_low_BR | 16 | 18 | 未保存 |
| T020 | MC_man_throwable_Staff_mid_FL | 9 | 11 | 未保存 |
| T021 | MC_man_throwable_Staff_mid_BR | 9 | 11 | 未保存 |


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
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T019 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T020 |
| 动画帧区间[0] | m_Anim[0] | 未解码（12 字节） | T021 |
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 是 | 本表全部行 |
| 镜像方法[0] | m_eMirroringMethod[0] | EAttackMirroringMethod::BasedOnQuadrantToTarget | 本表全部行 |
| 镜像采用下一脚步标记阈值[0] | m_fMirrorUseNextFootMarkerThreshold[0] | 0.5 | 本表全部行 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontLeft | T001, T003, T005, T009, T011, T013, T014, T018, T020 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::BackRight | T002, T004, T006, T008, T015, T017, T019, T021 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontRight | T007, T016 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::BackLeft | T010, T012 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontLeft | T001, T002, T003, T004, T006, T007, T008, T009, T011, T013, T014, T015, T016, T017, T018, T019, T020, T021 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontRight | T005, T010, T012 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 40.9094162 | T001, T018 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 82.0273743 | T002, T019 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 71.7759323 | T003 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 60.7942429 | T004, T012 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 80.4450836 | T005 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 63.5595818 | T006, T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 152.655884 | T007, T016 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 152.098953 | T008, T017 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 61.9381676 | T009 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 73.9501266 | T011, T013 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 52.2134476 | T014 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 87.1369934 | T015 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 0 | T020, T021 |
| 右向位移长度[0] | m_fMovementRightLength[0] | 0 | 本表全部行 |
| 直接跟随右向位移标志[0] | m_bDirectRightMovementFollow[0] | 是 | 本表全部行 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 16 | T001, T002, T018, T019 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 9 | T003, T004, T020, T021 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 18 | T005 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 22 | T006 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 12 | T007, T008, T016, T017 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 19 | T009, T010 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 11 | T011, T012, T013, T014, T015 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 18 | T001, T002, T011, T013, T014, T015, T018, T019 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 11 | T003, T004, T020, T021 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 20 | T005, T012 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 24 | T006 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 16 | T007, T008, T016, T017 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 21 | T009, T010 |
| 无打击阶段攻击标志[0] | m_bStrikelessAttack[0] | 否 | 本表全部行 |
| 内部名称[0] | m_Name[0] | Throwable | 本表全部行 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T001 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T002 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T003 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T004 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T005 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T006 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（104 字节） | T007, T016 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（104 字节） | T008, T017 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（104 字节） | T009 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（104 字节） | T010 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（101 字节） | T011 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（101 字节） | T012 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（99 字节） | T013 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（100 字节） | T014 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（100 字节） | T015 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T018 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T019 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T020 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T021 |


来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 [[03配置/动作与时序/索引]]。
