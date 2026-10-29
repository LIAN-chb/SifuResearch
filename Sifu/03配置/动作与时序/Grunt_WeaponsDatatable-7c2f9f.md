# Grunt_WeaponsDatatable：动画行配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/Grunt_WeaponsDatatable.uasset

收录本表全部 15 条已解析行。动画行不等于 AttackDB，也不等于 HitBox；没有关联不表示该行未使用。这里的帧值是保存参数，不能当成已验证的完整前后摇或取消窗口。

## 全部动画行

| 行 ID | 动画行名 | 最后前摇帧字段 | 命中帧字段 | 动画引用字段 |
|---|---|---|---|---|
| T001 | Grunt_Attack_Bottle_ThrowFar | 28 | 41 | 未保存 |
| T002 | Grunt_attack_PushkickWeapon | 17 | 22 | 未保存 |
| T003 | Grunt_Blunt_UpSmash | 30 | 36 | 未保存 |
| T004 | Grunt_Attack_Blunt_BatSweep | 23 | 33 | 未保存 |
| T005 | Grunt_Attack_Blunt_SmashTgtDown | 20 | 29 | 未保存 |
| T006 | Grunt_Attack_Blunt_2HandedHandleStrike | 15 | 19 | 未保存 |
| T007 | Grunt_Attack_Blunt_WideSwingRight | 48 | 56 | 未保存 |
| T008 | Grunt_Attack_Blunt_WideSwingLeft | 20 | 31 | 未保存 |
| T009 | Grunt_Attack_Blunt_DownSmash | 23 | 31 | 未保存 |
| T010 | Grunt_attack_Blades_WideVerticalSlashDown | 32 | 39 | 未保存 |
| T011 | Grunt_attack_Blades_Horizontal_Slash_Right | 11 | 21 | 未保存 |
| T012 | Grunt_attack_Blades_HorizontalSlashRightEngage | 42 | 46 | 未保存 |
| T013 | Grunt_attack_Blades_StabThrust | 16 | 24 | 未保存 |
| T014 | Grunt_attack_Blades_OneHandedHandleStrike | 17 | 25 | 未保存 |
| T015 | Grunt_Attack_Bottle_HorizontalHeadSmashFar | 45 | 56 | 未保存 |


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
| 允许镜像动作[0] | m_bCanBeMirrored[0] | 否 | 本表全部行 |
| 镜像方法[0] | m_eMirroringMethod[0] | EAttackMirroringMethod::BasedOnQuadrantToTarget | 本表全部行 |
| 镜像采用下一脚步标记阈值[0] | m_fMirrorUseNextFootMarkerThreshold[0] | 0.5 | 本表全部行 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontLeft | T001, T003, T005, T006, T007, T009, T010, T011, T012, T013, T014, T015 |
| 起始姿态象限[0] | m_eStartQuadrant[0] | EQuadrantTypes::FrontRight | T002, T004, T008 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontLeft | T001, T002, T004, T005, T008, T009, T010, T014, T015 |
| 结束姿态象限[0] | m_eEndQuadrant[0] | EQuadrantTypes::FrontRight | T003, T006, T007, T011, T012, T013 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 200.346558 | T001, T015 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 131.421707 | T002 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 130.673065 | T003 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 118.548775 | T004 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 39.441452 | T005 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 79.4599991 | T006 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 266.916382 | T007 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 123.130447 | T008 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 96.3584595 | T009 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 224.358459 | T010 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 105.847221 | T011 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 142.282593 | T012 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 131.2677 | T013 |
| 测量的前向位移[0] | m_fMeasuredForwardMovement[0] | 61.2183342 | T014 |
| 右向位移长度[0] | m_fMovementRightLength[0] | 0 | 本表全部行 |
| 直接跟随右向位移标志[0] | m_bDirectRightMovementFollow[0] | 是 | 本表全部行 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 28 | T001 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 17 | T002, T014 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 30 | T003 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 23 | T004, T009 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 20 | T005, T008 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 15 | T006 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 48 | T007 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 32 | T010 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 11 | T011 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 42 | T012 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 16 | T013 |
| 最后前摇帧字段[0] | m_iLastBuildupFrame[0] | 45 | T015 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 41 | T001 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 22 | T002 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 36 | T003 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 33 | T004 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 29 | T005 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 19 | T006 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 56 | T007, T015 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 31 | T008, T009 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 39 | T010 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 21 | T011 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 46 | T012 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 24 | T013 |
| 动画命中帧字段[0] | m_fHitFrame[0] | 25 | T014 |
| 无打击阶段攻击标志[0] | m_bStrikelessAttack[0] | 否 | 本表全部行 |
| 内部名称[0] | m_Name[0] | EE | T001, T015 |
| 内部名称[0] | m_Name[0] | None | T002 |
| 内部名称[0] | m_Name[0] | Bats | T003, T004, T005, T006, T007, T008, T009 |
| 内部名称[0] | m_Name[0] | Blades | T010, T011, T012, T013, T014 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（75 字节） | T001 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T002 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（75 字节） | T003 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（76 字节） | T004 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（80 字节） | T005 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（87 字节） | T006 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（82 字节） | T007 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（81 字节） | T008 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（77 字节） | T009 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（92 字节） | T010 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（93 字节） | T011 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（97 字节） | T012 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（81 字节） | T013 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（92 字节） | T014 |
| 实际攻击名称字段[0] | m_RealAttackName[0] | 未解码（89 字节） | T015 |


来源：inventory/data-tables.json.gz。与动作、HitBox 的引用关系见 [[03配置/动作与时序/索引]]。
