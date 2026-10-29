# MainChar_Staff_HitBoxData：攻击效果配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/_MainChar/Combos/MainChar_Staff_HitBoxData.uasset

本页收录本表全部 30 条已解析 HitBox 行，覆盖普通命中、格挡、弹开三种配置。行 ID 只在本页内定位，不代表独立招式；所有值均非最终实战结果。

## 行索引与韧性相关配置

| 行 ID | HitBox 行名 | 命中种类 | 攻击强度 | 韧性覆盖 | 可招架标志 | Parry 时眩晕标志 | Avoid 时眩晕标志 |
|---|---|---|---|---|---|---|---|
| H001 | HeadMill | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H002 | VerticalCruche | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H003 | LongSweep | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H004 | KneeFlick | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 否 | 否 | 是 |
| H005 | FastStrike_HB01 | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：3 | 是 | 否 | 是 |
| H006 | FastStrike_HB02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 是 | 否 | 是 |
| H007 | VerticalSink | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：3 | 否 | 否 | 是 |
| H008 | LightFinisher | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H009 | GroinPlexus_HB01 | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：5 | 是 | 否 | 是 |
| H010 | GroinPlexus_HB02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 是 | 否 | 是 |
| H011 | StaffKnockdown | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H012 | MillEstoc | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 否 | 否 | 是 |
| H013 | HorizontalMill | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 否 | 否 | 是 |
| H014 | DelayPushback | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H015 | Knockdown | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H016 | RangedSync_HB01 | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H017 | RangedSync_HB02 | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：5 | 否 | 否 | 是 |
| H018 | RangedSync_HB03 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H019 | Disengage | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：3 | 否 | 否 | 是 |
| H020 | Engage | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：5 | 否 | 否 | 是 |
| H021 | ChargedSweep_Lv1 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H022 | ChargedSweep_Lv2 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H023 | SlideHeadStrike | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：3 | 否 | 否 | 是 |
| H024 | PlexusEstoc | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 否 | 否 | 是 |
| H025 | PlantedTurn | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：3 | 否 | 否 | 是 |
| H026 | LightFinisher_BT | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H027 | HeadMillCrush | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H028 | HorizontalSink | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H029 | LongSweep_BT | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H030 | ChargedSweep_Lv0 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：3 | 否 | 否 | 是 |

“Parry／Avoid 时眩晕”列仅报告字段，不足以断言用户的防反／闪避反击追击窗口已经解释完成。

## 普通命中效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：25 | 开：36 | 开：38 | 开：25 | 开：130 | 开：3 |
| H002 | 开：25 | 开：36 | 开：38 | 开：25 | 开：150 | 开：4 |
| H003 | 开：35 | 开：54 | 开：53 | 开：30 | 关（保存 0） | 开：6 |
| H004 | 开：10 | 开：18 | 开：15 | 开：12 | 关（保存 0） | 开：3 |
| H005 | 开：5 | 开：12 | 开：8 | 开：10 | 关（保存 0） | 开：2 |
| H006 | 开：10 | 开：18 | 开：15 | 开：25 | 开：120 | 开：3 |
| H007 | 开：20 | 开：30 | 开：30 | 开：25 | 开：120 | 开：4 |
| H008 | 开：25 | 开：36 | 开：38 | 开：30 | 开：150 | 开：5 |
| H009 | 开：5 | 开：12 | 开：8 | 开：12 | 开：55 | 开：0 |
| H010 | 开：10 | 开：18 | 开：15 | 开：25 | 开：40 | 开：0 |
| H011 | 开：40 | 开：60 | 开：60 | 开：30 | 关（保存 0） | 开：5 |
| H012 | 开：15 | 开：24 | 开：23 | 开：25 | 开：120 | 开：0 |
| H013 | 开：20 | 开：30 | 开：30 | 开：20 | 关（保存 0） | 开：4 |
| H014 | 开：15 | 开：36 | 开：23 | 开：40 | 关（保存 0） | 开：6 |
| H015 | 开：25 | 开：42 | 开：38 | 开：30 | 关（保存 0） | 开：6 |
| H016 | 开：5 | 开：12 | 开：8 | 开：20 | 关（保存 0） | 开：4 |
| H017 | 开：10 | 开：18 | 开：15 | 开：12 | 关（保存 0） | 开：2 |
| H018 | 开：10 | 开：18 | 开：15 | 开：10 | 关（保存 0） | 开：5 |
| H019 | 开：10 | 开：24 | 开：15 | 开：20 | 关（保存 0） | 开：3 |
| H020 | 开：15 | 开：24 | 开：23 | 开：25 | 关（保存 0） | 开：5 |
| H021 | 开：25 | 开：42 | 开：38 | 开：25 | 关（保存 0） | 开：5 |
| H022 | 开：40 | 开：60 | 开：60 | 开：30 | 关（保存 0） | 开：5 |
| H023 | 开：15 | 开：24 | 开：23 | 开：10 | 关（保存 0） | 开：2 |
| H024 | 开：15 | 开：24 | 开：23 | 开：25 | 开：120 | 开：0 |
| H025 | 开：20 | 开：30 | 开：30 | 开：30 | 开：150 | 开：5 |
| H026 | 开：25 | 开：36 | 开：38 | 开：25 | 开：120 | 开：4 |
| H027 | 开：25 | 开：36 | 开：38 | 开：25 | 开：120 | 开：4 |
| H028 | 开：25 | 开：36 | 开：38 | 开：25 | 开：150 | 开：4 |
| H029 | 开：35 | 开：54 | 开：53 | 开：30 | 关（保存 0） | 开：6 |
| H030 | 开：25 | 开：42 | 开：38 | 开：25 | 关（保存 0） | 开：5 |


## 格挡效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：130 | 开：3 |
| H002 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：120 | 开：4 |
| H003 | 关（保存 0） | 开：45 | 关（保存 0） | 开：30 | 开：150 | 开：6 |
| H004 | 关（保存 0） | 开：15 | 关（保存 0） | 开：12 | 开：50 | 开：3 |
| H005 | 关（保存 0） | 开：10 | 关（保存 0） | 开：10 | 开：30 | 开：2 |
| H006 | 关（保存 0） | 开：15 | 关（保存 0） | 开：25 | 开：100 | 开：3 |
| H007 | 关（保存 0） | 开：25 | 关（保存 0） | 开：25 | 开：100 | 开：4 |
| H008 | 关（保存 0） | 开：30 | 关（保存 0） | 开：30 | 开：150 | 开：5 |
| H009 | 关（保存 0） | 开：10 | 关（保存 0） | 开：12 | 开：55 | 开：0 |
| H010 | 关（保存 0） | 开：15 | 关（保存 0） | 开：25 | 开：40 | 开：0 |
| H011 | 关（保存 0） | 开：50 | 关（保存 0） | 开：30 | 开：150 | 开：5 |
| H012 | 关（保存 0） | 开：20 | 关（保存 0） | 开：25 | 开：120 | 开：0 |
| H013 | 关（保存 0） | 开：25 | 关（保存 0） | 开：20 | 开：80 | 开：4 |
| H014 | 关（保存 0） | 开：30 | 关（保存 0） | 开：40 | 开：180 | 开：6 |
| H015 | 关（保存 0） | 开：35 | 关（保存 0） | 开：30 | 开：150 | 开：6 |
| H016 | 关（保存 0） | 开：10 | 关（保存 0） | 开：20 | 开：100 | 开：4 |
| H017 | 关（保存 0） | 开：15 | 关（保存 0） | 开：12 | 开：50 | 开：2 |
| H018 | 关（保存 0） | 开：15 | 关（保存 0） | 开：10 | 开：30 | 开：5 |
| H019 | 关（保存 0） | 开：20 | 关（保存 0） | 开：20 | 开：50 | 开：3 |
| H020 | 关（保存 0） | 开：20 | 关（保存 0） | 开：25 | 开：100 | 开：5 |
| H021 | 关（保存 0） | 开：35 | 关（保存 0） | 开：25 | 开：120 | 开：5 |
| H022 | 关（保存 0） | 开：50 | 关（保存 0） | 开：30 | 开：150 | 开：5 |
| H023 | 关（保存 0） | 开：20 | 关（保存 0） | 开：10 | 开：30 | 开：2 |
| H024 | 关（保存 0） | 开：20 | 关（保存 0） | 开：25 | 开：120 | 开：0 |
| H025 | 关（保存 0） | 开：25 | 关（保存 0） | 开：30 | 开：150 | 开：5 |
| H026 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：100 | 开：4 |
| H027 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：130 | 开：4 |
| H028 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：120 | 开：4 |
| H029 | 关（保存 0） | 开：45 | 关（保存 0） | 开：30 | 开：150 | 开：6 |
| H030 | 关（保存 0） | 开：35 | 关（保存 0） | 开：25 | 开：120 | 开：5 |


## 弹开效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：130 | 关（保存 0） |
| H002 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H003 | 关（保存 0） | 开：36 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H004 | 关（保存 0） | 开：12 | 关（保存 0） | 开：12 | 开：50 | 关（保存 0） |
| H005 | 关（保存 0） | 开：8 | 关（保存 0） | 开：10 | 开：30 | 关（保存 0） |
| H006 | 关（保存 0） | 开：12 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H007 | 关（保存 0） | 开：20 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H008 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H009 | 关（保存 0） | 开：8 | 关（保存 0） | 开：12 | 开：55 | 关（保存 0） |
| H010 | 关（保存 0） | 开：12 | 关（保存 0） | 开：20 | 开：40 | 关（保存 0） |
| H011 | 关（保存 0） | 开：40 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H012 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H013 | 关（保存 0） | 开：20 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |
| H014 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H015 | 关（保存 0） | 开：28 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H016 | 关（保存 0） | 开：8 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H017 | 关（保存 0） | 开：12 | 关（保存 0） | 开：12 | 开：50 | 关（保存 0） |
| H018 | 关（保存 0） | 开：12 | 关（保存 0） | 开：10 | 开：30 | 关（保存 0） |
| H019 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：50 | 关（保存 0） |
| H020 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H021 | 关（保存 0） | 开：28 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H022 | 关（保存 0） | 开：40 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H023 | 关（保存 0） | 开：16 | 关（保存 0） | 开：10 | 开：30 | 关（保存 0） |
| H024 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H025 | 关（保存 0） | 开：20 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H026 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H027 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：130 | 关（保存 0） |
| H028 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H029 | 关（保存 0） | 开：36 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H030 | 关（保存 0） | 开：28 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |


## 弹开结果中的自身影响字段

Self 的具体作用对象应结合命中执行路径，不能直接把它加到被击者伤害上。

| 行 ID | 自身架势伤害字段 | 自身特殊眩晕伤害字段 | 自身架势伤害可破防标志 | 动态击退模式原值 |
|---|---|---|---|---|
| H001 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H002 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H003 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H004 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H005 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H006 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H007 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H008 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H009 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H010 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H011 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H012 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H013 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H014 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H015 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H016 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H017 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H018 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H019 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H020 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H021 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H022 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H023 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H024 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H025 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H026 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H027 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H028 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H029 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H030 | 关（保存 0） | 关（保存 0） | 是 | 0 |


## 其他保存参数与特殊反应配置

同值参数按适用行 ID 合并；包含攻击属性等级、持续时间／距离开关、状态覆盖、命中筛选、击退行为和防御矩阵等已保存字段。未解码项明确保留。以下也补留各命中结果中未在前表显示的字段。

| 中文标识 | 原字段路径 | 配置值 | 适用行 ID |
|---|---|---|---|
| 命中盒组编号[0] | m_iHitboxGroupID[0] | -1 | 本表全部行 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 180 | 本表全部行 |
| 穿透时忽略冲击角限制[0] | m_bIgnoreImpactAngleWhenPenetrating[0] | 是 | 本表全部行 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 3 | 本表全部行 |
| 命中盒玩法标签[0] | m_HitboxGameplayTags[0] | [] | H001, H002, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H016, H017, H018, H019, H020, H023, H024, H025, H026, H027, H028 |
| 仅命中具有要求标签的角色[0] | m_bOnlyHitCharacterWithRequiredHitboxGameplayTags[0] | 否 | 本表全部行 |
| 附加到目标的命中盒标签[0] | m_AdditionalHitboxGameplayTagsOnTarget[0] | [] | 本表全部行 |
| 要求的玩法标签[0] | m_RequiredGameplayTags[0] | [] | 本表全部行 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H011, H012, H013, H014, H015, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 是 | H009, H010, H016, H017, H018 |
| 忽略锁定目标标志[0] | m_bIgnoreTarget[0] | 否 | 本表全部行 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H011, H012, H013, H014, H015, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 否 | H009, H010, H016, H017, H018 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H011, H012, H013, H014, H015, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 否 | H009, H010, H016, H017, H018 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 是 | H001, H002, H003, H004, H006, H007, H008, H010, H011, H012, H013, H014, H015, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 否 | H005, H009, H016, H017 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 是 | H001, H002, H003, H004, H006, H007, H008, H010, H011, H012, H013, H014, H015, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 否 | H005, H009, H016, H017 |
| 命中时动态击退配置引用[0] | m_KnockBackDynamicOnHit[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 弹开结果配置[0] → 动态击退配置引用[0] | m_OnDeflectImpact[0].m_KnockBackDynamic[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害可触发破防[0] | m_OnDeflectImpact[0].m_bSelfStructureDamageCanGuardBreak[0] | 是 | 本表全部行 |
| 弹开结果配置[0] → 启用自身架势伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfStructureDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 0 | 本表全部行 |
| 弹开结果配置[0] → 启用自身特殊眩晕伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfSuperDizzyDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身特殊眩晕伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfSuperDizzyDamage[0] | 0 | 本表全部行 |
| 受击反应类型[0] | m_eHittedReaction[0] | EHittedReaction::Hit | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 受击反应类型[0] | m_eHittedReaction[0] | EHittedReaction::Action | H016 |
| 命中动作引用[0] | m_hitAction[0] | 对象索引 0；未解析引用 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 命中动作引用[0] | m_hitAction[0] | /Game/DB/_MainChar/Combos/Attacks/Weapons/Staff/Hold/Dizzy/MainChar_Staff_HoldRanged_SynchronizedHitAction.MainChar_Staff_HoldRanged_SynchronizedHitAction_C | H016 |
| 命中动作中发送受击通知[0] | m_bNotifyHittedOnHitAction[0] | 是 | 本表全部行 |
| 命中动作中应用停顿帧[0] | m_bApplyFreezeFramesOnHitAction[0] | 是 | 本表全部行 |
| 命中动作中播放震动[0] | m_bPlayRumbleOnHitAction[0] | 是 | 本表全部行 |
| 普通命中时播放震动[0] | m_bPlayRumbleOnNormalHit[0] | 是 | 本表全部行 |
| 命中情境[0] → 枚举资源[0] | m_HitContext[0].m_Enum[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 命中情境[0] → 缺省枚举索引[0] | m_HitContext[0].m_iDefaultEnumValue[0] | -1 | 本表全部行 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H011, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator12 | H010, H012 |
| 播放 Avoided 订单标志[0] | m_bPlayAvoidedOrder[0] | 是 | 本表全部行 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 0 | H001, H002, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H016, H017, H018, H019, H020, H023, H024, H025, H026, H027, H028 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 5 | H003, H011, H015, H022, H029 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 3 | H021 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 1 | H030 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 5 | H014 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H011, H012, H013, H014, H015, H016, H017, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 14 | H010, H018 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 4 | H019 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 2 | H020 |
| 特殊反应攻击等级[0] → 启用自定义持续时间[0] | m_AttackPropertyLevel[0].m_bUseCustomDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 自定义持续时间值[0] | m_AttackPropertyLevel[0].m_fCustomDuration[0] | 0 | 本表全部行 |
| 特殊反应攻击等级[0] → 使用受击动画时长[0] | m_AttackPropertyLevel[0].m_bUseHitAnimDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 保留当前状态剩余时长[0] | m_AttackPropertyLevel[0].m_bKeepCurrentStateDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 保留当前状态时长阈值[0] | m_AttackPropertyLevel[0].m_fKeepCurrentStateThresold[0] | 1 | 本表全部行 |
| 特殊反应攻击等级[0] → 启用自定义距离[0] | m_AttackPropertyLevel[0].m_bUseCustomDistance[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 自定义距离值[0] | m_AttackPropertyLevel[0].m_fCustomDistance[0] | 0 | 本表全部行 |
| 按状态覆盖的攻击等级[0] | m_AttackPropertyLevelOverrides[0] | 未解码（8 字节） | 本表全部行 |
| 命中后的最小击退角[0] | m_fMinKnockbackAngleFromHit[0] | 0 | 本表全部行 |
| 击退行为[0] | m_eKnockBackBehavior[0] | EKnockbackBehavior::Regular | 本表全部行 |
| 东西方向击退角[0] | m_fKnockbackEastWestAngle[0] | 45 | 本表全部行 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 7 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H023, H024, H025, H026, H027, H028, H029, H030 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 3 | H022 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 12 | H001, H002, H006, H007, H012, H014, H016, H019, H020, H024, H026, H027 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 1 | H003, H009, H011, H015, H021, H022, H029, H030 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 2 | H004, H005, H008, H010, H013, H018, H023, H025, H028 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 0 | H017 |
| 命中盒玩法标签[0][0] | m_HitboxGameplayTags[0][0] | Hitbox.KnockdownHit | H003, H011, H015, H021, H022, H029, H030 |


原始行与字段见 inventory/data-tables.json.gz；三结果数值导出见 exports/hit-impact-values.csv。表名和资源类别仅用于查找，当前是否实战调用需沿动作引用核对。
