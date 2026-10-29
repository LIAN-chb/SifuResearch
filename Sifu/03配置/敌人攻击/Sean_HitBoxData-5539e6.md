# Sean_HitBoxData：攻击效果配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Sean/Sean_HitBoxData.uasset

本页收录本表全部 61 条已解析 HitBox 行，覆盖普通命中、格挡、弹开三种配置。行 ID 只在本页内定位，不代表独立招式；所有值均非最终实战结果。

## 行索引与韧性相关配置

| 行 ID | HitBox 行名 | 命中种类 | 攻击强度 | 韧性覆盖 | 可招架标志 | Parry 时眩晕标志 | Avoid 时眩晕标志 |
|---|---|---|---|---|---|---|---|
| H001 | Thrust_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H002 | Tornado_StaffAttack_01 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H003 | Tornado_StaffAttack_02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H004 | Tornado_StaffAttack_03 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H005 | LowSwipe_HighSwipe_01 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H006 | LowSwipe_HighSwipe_02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H007 | TigerSwing_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H008 | ReversalCrane_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H009 | Waterfall_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H010 | ScorpionStab_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H011 | BearBlow_Counter | EHitType::Barehands | EAttackPowers::Light | 开：5 | 否 | 否 | 否 |
| H012 | EagleSlaughter_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H013 | DragonFist_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H014 | Tornado_StaffAttack_01_Burst | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H015 | Tornado_StaffAttack_02_Burst | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H016 | Tornado_StaffAttack_03_Burst | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H017 | Waterfall_Burst_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H018 | Thrust_Burst_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H019 | DragonFist_Burst_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H020 | LowSwipe_HighSwipe_Burst_StaffAttack_01 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H021 | LowSwipe_HighSwipe_Burst_StaffAttack_02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H022 | TigerSwing_Burst_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H023 | ReversalCrane_Burst_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H024 | BearBlow_Burst_Counter | EHitType::Barehands | EAttackPowers::Light | 开：5 | 否 | 否 | 否 |
| H025 | EagleSlaughter_Burst_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H026 | Combo03_Starter | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H027 | Combo03_ThrustFollowUp | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H028 | Combo03_DoubleHit_01 | EHitType::Weapon_Blunt | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H029 | Combo03_DoubleHit_02 | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H030 | Rising_Slash | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H031 | Slam | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H032 | SnakeBite_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H033 | ReverseSlash_StaffAttack | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H034 | Blast_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H035 | HeatBlast_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 是 | 否 | 是 |
| H036 | ColdBack_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H037 | HeatBack_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 是 | 否 | 否 |
| H038 | ElbowStrike_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H039 | HeatElbowStrike_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H040 | ExplosionBrasero | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H041 | FallingBrasero | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H042 | DivingHawk_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H043 | DivingHawkBurst_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H044 | GokuBurst_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H045 | BurstTransition | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H046 | RavenClaw_Hit-1_BarehandsAttack | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H047 | RavenClaw_Hit-2_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H048 | SwanSoar_BarehandsAttack | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H049 | Tornado_StaffAttack_03_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H050 | LowSwipe_HighSwipe_01_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H051 | Tornado_StaffAttack_03_Burst_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H052 | LowSwipe_HighSwipe_Burst_StaffAttack_01_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H053 | Combo03_ThrustFollowUp_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H054 | Thrust_Burst_StaffAttack_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H055 | LowSwipe_HighSwipe_Burst_StaffAttack_02_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H056 | Waterfall_Burst_StaffAttack_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H057 | Rising_Slash_Hard | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H058 | Tornado_StaffAttack_03_Easy | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 否 | 否 | 是 |
| H059 | DragonFist_BarehandsAttack_Easy | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 是 | 否 | 是 |
| H060 | EagleSlaughter_StaffAttack_Easy | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 是 | 否 | 否 |
| H061 | Rising_Slash_Easy | EHitType::Weapon_Blunt | EAttackPowers::Strong | 开：5 | 是 | 否 | 是 |

“Parry／Avoid 时眩晕”列仅报告字段，不足以断言用户的防反／闪避反击追击窗口已经解释完成。

## 普通命中效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：15 | 开：42 | 关（保存 0） | 开：30 | 关（保存 300） | 开：4 |
| H002 | 开：15 | 开：36 | 关（保存 0） | 开：25 | 开：175 | 开：2 |
| H003 | 开：15 | 开：36 | 关（保存 0） | 开：30 | 开：225 | 开：2 |
| H004 | 开：20 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H005 | 开：10 | 开：24 | 关（保存 0） | 开：20 | 关（保存 150） | 开：2 |
| H006 | 开：15 | 开：36 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H007 | 开：10 | 开：30 | 关（保存 0） | 开：30 | 开：130 | 开：3 |
| H008 | 开：10 | 开：30 | 关（保存 0） | 开：30 | 开：175 | 开：2 |
| H009 | 开：20 | 开：85 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H010 | 开：20 | 开：60 | 关（保存 0） | 开：30 | 关（保存 90） | 开：3 |
| H011 | 开：10 | 开：36 | 关（保存 0） | 开：35 | 关（保存 200） | 开：6 |
| H012 | 开：7 | 开：32 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H013 | 开：25 | 开：90 | 关（保存 0） | 开：35 | 关（保存 200） | 开：6 |
| H014 | 开：20 | 开：48 | 关（保存 0） | 开：25 | 开：175 | 开：2 |
| H015 | 开：20 | 开：48 | 关（保存 0） | 开：30 | 开：225 | 开：2 |
| H016 | 开：25 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H017 | 开：25 | 开：85 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H018 | 开：20 | 开：54 | 关（保存 0） | 开：30 | 关（保存 0） | 开：4 |
| H019 | 开：25 | 开：175 | 关（保存 0） | 开：35 | 关（保存 0） | 开：6 |
| H020 | 开：10 | 开：24 | 关（保存 0） | 开：20 | 关（保存 0） | 开：2 |
| H021 | 开：20 | 开：48 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H022 | 开：15 | 开：36 | 关（保存 0） | 开：30 | 开：130 | 开：3 |
| H023 | 开：15 | 开：36 | 关（保存 0） | 开：30 | 开：175 | 开：2 |
| H024 | 开：10 | 开：36 | 关（保存 0） | 开：35 | 关（保存 0） | 开：6 |
| H025 | 开：10 | 开：36 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H026 | 开：10 | 开：30 | 关（保存 0） | 开：30 | 开：200 | 开：3 |
| H027 | 开：20 | 开：90 | 关（保存 0） | 开：30 | 关（保存 0） | 开：6 |
| H028 | 开：15 | 开：36 | 关（保存 0） | 开：15 | 关（保存 0） | 开：3 |
| H029 | 开：15 | 开：36 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H030 | 开：20 | 开：85 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H031 | 开：20 | 开：36 | 关（保存 0） | 开：20 | 关（保存 0） | 开：4 |
| H032 | 开：25 | 开：54 | 关（保存 0） | 开：20 | 关（保存 0） | 开：4 |
| H033 | 开：25 | 开：54 | 关（保存 0） | 开：20 | 关（保存 0） | 开：4 |
| H034 | 开：25 | 开：30 | 关（保存 0） | 开：20 | 关（保存 0） | 开：6 |
| H035 | 开：25 | 开：30 | 关（保存 0） | 开：30 | 关（保存 0） | 开：6 |
| H036 | 开：20 | 开：24 | 关（保存 0） | 开：15 | 关（保存 0） | 开：6 |
| H037 | 开：20 | 开：24 | 关（保存 0） | 开：25 | 关（保存 0） | 开：6 |
| H038 | 开：25 | 开：30 | 关（保存 0） | 开：15 | 关（保存 0） | 开：4 |
| H039 | 开：25 | 开：30 | 关（保存 0） | 开：25 | 关（保存 0） | 开：4 |
| H040 | 开：25 | 开：30 | 关（保存 0） | 开：20 | 关（保存 0） | 开：6 |
| H041 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 关（保存 0） | 开：6 |
| H042 | 开：30 | 开：36 | 关（保存 0） | 开：40 | 关（保存 0） | 开：4 |
| H043 | 开：30 | 开：36 | 关（保存 0） | 开：40 | 关（保存 0） | 开：4 |
| H044 | 开：25 | 开：30 | 关（保存 0） | 开：30 | 关（保存 0） | 开：4 |
| H045 | 开：0 | 开：0 | 关（保存 0） | 开：15 | 关（保存 0） | 开：6 |
| H046 | 开：25 | 开：30 | 关（保存 0） | 开：15 | 关（保存 0） | 开：6 |
| H047 | 开：25 | 开：30 | 关（保存 0） | 开：15 | 关（保存 0） | 开：6 |
| H048 | 开：25 | 开：30 | 关（保存 0） | 开：20 | 关（保存 0） | 开：6 |
| H049 | 开：20 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H050 | 开：25 | 开：42 | 关（保存 0） | 开：20 | 关（保存 0） | 开：2 |
| H051 | 开：25 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H052 | 开：10 | 开：24 | 关（保存 0） | 开：20 | 关（保存 0） | 开：2 |
| H053 | 开：20 | 开：90 | 关（保存 0） | 开：30 | 关（保存 0） | 开：6 |
| H054 | 开：25 | 开：60 | 关（保存 0） | 开：30 | 关（保存 0） | 开：4 |
| H055 | 开：20 | 开：48 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H056 | 开：30 | 开：90 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H057 | 开：25 | 开：90 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H058 | 开：15 | 开：165 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H059 | 开：25 | 开：90 | 关（保存 0） | 开：35 | 关（保存 0） | 开：6 |
| H060 | 开：7 | 开：32 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H061 | 开：15 | 开：80 | 关（保存 0） | 开：35 | 开：200 | 开：6 |


## 格挡效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：0 | 开：35 | 关（保存 0） | 开：30 | 开：175 | 开：4 |
| H002 | 开：0 | 开：30 | 关（保存 0） | 开：25 | 开：175 | 开：2 |
| H003 | 开：0 | 开：30 | 关（保存 0） | 开：30 | 开：225 | 开：2 |
| H004 | 开：0 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H005 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：150 | 开：2 |
| H006 | 开：0 | 开：30 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H007 | 开：0 | 开：25 | 关（保存 0） | 开：30 | 开：130 | 开：3 |
| H008 | 开：0 | 开：25 | 关（保存 0） | 开：30 | 开：175 | 开：2 |
| H009 | 开：0 | 开：85 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H010 | 开：0 | 开：50 | 关（保存 0） | 开：30 | 开：100 | 开：3 |
| H011 | 开：0 | 开：30 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H012 | 开：0 | 开：27 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H013 | 开：0 | 开：90 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H014 | 开：0 | 开：40 | 关（保存 0） | 开：25 | 开：175 | 开：2 |
| H015 | 开：0 | 开：40 | 关（保存 0） | 开：30 | 开：225 | 开：2 |
| H016 | 开：0 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H017 | 开：0 | 开：85 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H018 | 开：0 | 开：45 | 关（保存 0） | 开：30 | 开：175 | 开：4 |
| H019 | 开：0 | 开：175 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H020 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：150 | 开：2 |
| H021 | 开：0 | 开：40 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H022 | 开：0 | 开：30 | 关（保存 0） | 开：30 | 开：130 | 开：3 |
| H023 | 开：0 | 开：30 | 关（保存 0） | 开：30 | 开：175 | 开：2 |
| H024 | 开：0 | 开：30 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H025 | 开：0 | 开：30 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H026 | 开：0 | 开：25 | 关（保存 0） | 开：30 | 开：200 | 开：3 |
| H027 | 开：0 | 开：90 | 关（保存 0） | 开：30 | 开：200 | 开：6 |
| H028 | 开：0 | 开：30 | 关（保存 0） | 开：15 | 开：60 | 开：3 |
| H029 | 开：0 | 开：30 | 关（保存 0） | 开：25 | 开：175 | 开：4 |
| H030 | 开：0 | 开：85 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H031 | 开：0 | 开：30 | 关（保存 0） | 开：20 | 开：120 | 开：4 |
| H032 | 开：0 | 开：45 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H033 | 开：0 | 开：45 | 关（保存 0） | 开：20 | 开：90 | 开：4 |
| H034 | 开：0 | 开：25 | 关（保存 0） | 开：20 | 开：100 | 开：6 |
| H035 | 开：0 | 开：25 | 关（保存 0） | 开：30 | 开：100 | 开：6 |
| H036 | 开：0 | 开：20 | 关（保存 0） | 开：15 | 开：100 | 开：6 |
| H037 | 开：0 | 开：20 | 关（保存 0） | 开：25 | 开：100 | 开：6 |
| H038 | 开：0 | 开：25 | 关（保存 0） | 开：15 | 开：200 | 开：4 |
| H039 | 开：0 | 开：25 | 关（保存 0） | 开：25 | 开：200 | 开：4 |
| H040 | 开：0 | 开：25 | 关（保存 0） | 开：20 | 开：300 | 开：6 |
| H041 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：300 | 开：6 |
| H042 | 开：0 | 开：30 | 关（保存 0） | 开：40 | 开：100 | 开：4 |
| H043 | 开：0 | 开：30 | 关（保存 0） | 开：40 | 开：100 | 开：4 |
| H044 | 开：0 | 开：25 | 关（保存 0） | 开：30 | 开：200 | 开：4 |
| H045 | 开：0 | 开：0 | 关（保存 0） | 开：15 | 开：300 | 开：6 |
| H046 | 开：0 | 开：25 | 关（保存 0） | 开：15 | 开：100 | 开：6 |
| H047 | 开：0 | 开：25 | 关（保存 0） | 开：15 | 开：100 | 开：6 |
| H048 | 开：0 | 开：25 | 关（保存 0） | 开：20 | 开：100 | 开：6 |
| H049 | 开：0 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H050 | 开：0 | 开：35 | 关（保存 0） | 开：20 | 开：150 | 开：2 |
| H051 | 开：0 | 开：170 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H052 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：150 | 开：2 |
| H053 | 开：0 | 开：90 | 关（保存 0） | 开：30 | 开：200 | 开：6 |
| H054 | 开：0 | 开：50 | 关（保存 0） | 开：30 | 开：175 | 开：4 |
| H055 | 开：0 | 开：40 | 关（保存 0） | 开：25 | 开：150 | 开：4 |
| H056 | 开：0 | 开：90 | 关（保存 0） | 开：20 | 开：150 | 开：4 |
| H057 | 开：0 | 开：90 | 关（保存 0） | 开：35 | 开：200 | 开：6 |
| H058 | 开：0 | 开：165 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H059 | 开：0 | 开：90 | 关（保存 0） | 开：35 | 开：250 | 开：6 |
| H060 | 开：0 | 开：27 | 关（保存 0） | 开：35 | 开：200 | 开：3 |
| H061 | 开：0 | 开：80 | 关（保存 0） | 开：35 | 开：200 | 开：6 |


## 弹开效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：0 | 开：28 | 关（保存 0） | 开：20 | 开：160 | 关（保存 4） |
| H002 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H003 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H004 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H005 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H006 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H007 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：130 | 关（保存 0） |
| H008 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H009 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H010 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H011 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H012 | 开：0 | 开：22 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H013 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H014 | 开：0 | 开：32 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H015 | 开：0 | 开：32 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H016 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H017 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H018 | 开：0 | 开：36 | 关（保存 0） | 开：20 | 开：160 | 关（保存 4） |
| H019 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H020 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H021 | 开：0 | 开：32 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H022 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：130 | 关（保存 0） |
| H023 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H024 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H025 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H026 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H027 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H028 | 开：0 | 开：24 | 关（保存 0） | 开：15 | 开：60 | 关（保存 0） |
| H029 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H030 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H031 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H032 | 开：0 | 开：36 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H033 | 开：0 | 开：36 | 关（保存 0） | 开：20 | 开：90 | 开：0 |
| H034 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H035 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H036 | 开：0 | 开：16 | 关（保存 0） | 开：15 | 开：100 | 关（保存 0） |
| H037 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H038 | 开：0 | 开：20 | 关（保存 0） | 开：15 | 开：160 | 关（保存 0） |
| H039 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H040 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H041 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：160 | 关（保存 0） |
| H042 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H043 | 开：0 | 开：24 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H044 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H045 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H046 | 开：0 | 开：20 | 关（保存 0） | 开：15 | 开：100 | 关（保存 0） |
| H047 | 开：0 | 开：20 | 关（保存 0） | 开：15 | 开：100 | 关（保存 0） |
| H048 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H049 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H050 | 开：0 | 开：28 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H051 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H052 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H053 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H054 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H055 | 开：0 | 开：32 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H056 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：150 | 关（保存 0） |
| H057 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H058 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H059 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H060 | 开：0 | 开：22 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H061 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |


## 弹开结果中的自身影响字段

Self 的具体作用对象应结合命中执行路径，不能直接把它加到被击者伤害上。

| 行 ID | 自身架势伤害字段 | 自身特殊眩晕伤害字段 | 自身架势伤害可破防标志 | 动态击退模式原值 |
|---|---|---|---|---|
| H001 | 开：35 | 关（保存 0） | 是 | 0 |
| H002 | 关（保存 20） | 关（保存 0） | 是 | 0 |
| H003 | 关（保存 20） | 关（保存 0） | 是 | 0 |
| H004 | 开：40 | 关（保存 0） | 是 | -2 |
| H005 | 开：35 | 关（保存 0） | 是 | 0 |
| H006 | 开：35 | 关（保存 0） | 是 | 0 |
| H007 | 关（保存 20） | 关（保存 0） | 是 | 0 |
| H008 | 关（保存 20） | 关（保存 0） | 是 | 0 |
| H009 | 开：40 | 关（保存 0） | 是 | 0 |
| H010 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H011 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H012 | 关（保存 20） | 关（保存 0） | 是 | 0 |
| H013 | 开：35 | 关（保存 0） | 是 | -2 |
| H014 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H015 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H016 | 开：50 | 关（保存 0） | 是 | 0 |
| H017 | 开：50 | 关（保存 0） | 是 | 0 |
| H018 | 开：45 | 关（保存 0） | 是 | 0 |
| H019 | 开：35 | 关（保存 0） | 是 | -2 |
| H020 | 开：45 | 关（保存 0） | 是 | 0 |
| H021 | 开：45 | 关（保存 0） | 是 | 0 |
| H022 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H023 | 关（保存 35） | 关（保存 0） | 是 | 0 |
| H024 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H025 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H026 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H027 | 开：35 | 关（保存 0） | 是 | 0 |
| H028 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H029 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H030 | 开：40 | 关（保存 0） | 是 | 0 |
| H031 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H032 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H033 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H034 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H035 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H036 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H037 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H038 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H039 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H040 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H041 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H042 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H043 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H044 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H045 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H046 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H047 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H048 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H049 | 关（保存 40） | 关（保存 0） | 是 | 0 |
| H050 | 关（保存 35） | 关（保存 0） | 是 | 0 |
| H051 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H052 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H053 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H054 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H055 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H056 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H057 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H058 | 开：60 | 关（保存 0） | 是 | 0 |
| H059 | 开：35 | 关（保存 0） | 是 | 0 |
| H060 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H061 | 开：40 | 关（保存 0） | 是 | 0 |


## 其他保存参数与特殊反应配置

同值参数按适用行 ID 合并；包含攻击属性等级、持续时间／距离开关、状态覆盖、命中筛选、击退行为和防御矩阵等已保存字段。未解码项明确保留。以下也补留各命中结果中未在前表显示的字段。

| 中文标识 | 原字段路径 | 配置值 | 适用行 ID |
|---|---|---|---|
| 命中盒组编号[0] | m_iHitboxGroupID[0] | -1 | 本表全部行 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 180 | 本表全部行 |
| 穿透时忽略冲击角限制[0] | m_bIgnoreImpactAngleWhenPenetrating[0] | 是 | 本表全部行 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 3 | 本表全部行 |
| 命中盒玩法标签[0] | m_HitboxGameplayTags[0] | [] | H001, H002, H003, H004, H007, H008, H011, H012, H013, H014, H015, H016, H018, H019, H022, H023, H024, H025, H027, H028, H029, H030, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 仅命中具有要求标签的角色[0] | m_bOnlyHitCharacterWithRequiredHitboxGameplayTags[0] | 否 | 本表全部行 |
| 附加到目标的命中盒标签[0] | m_AdditionalHitboxGameplayTagsOnTarget[0] | [] | 本表全部行 |
| 要求的玩法标签[0] | m_RequiredGameplayTags[0] | [] | 本表全部行 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H042, H043, H044, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 否 | H040, H041, H045 |
| 忽略锁定目标标志[0] | m_bIgnoreTarget[0] | 否 | 本表全部行 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 是 | H031 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 否 | H031 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 否 | H011, H024, H045 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 否 | H045 |
| 命中时动态击退配置引用[0] | m_KnockBackDynamicOnHit[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | 对象索引 0；未解析引用 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H014, H015, H016, H017, H018, H020, H021, H022, H023, H024, H025, H026, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | /Game/DB/_Shared/HitDynamic/UnparryableKnockBackDynamic.UnparryableKnockBackDynamic | H013, H019, H027 |
| 弹开结果配置[0] → 动态击退配置引用[0] | m_OnDeflectImpact[0].m_KnockBackDynamic[0] | 对象索引 0；未解析引用 | H001, H002, H003, H005, H006, H007, H008, H009, H010, H011, H012, H014, H015, H016, H017, H018, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 弹开结果配置[0] → 动态击退配置引用[0] | m_OnDeflectImpact[0].m_KnockBackDynamic[0] | /Game/DB/_Shared/HitDynamic/UnparryableKnockBackDynamic.UnparryableKnockBackDynamic | H004, H013, H019 |
| 弹开结果配置[0] → 自身架势伤害可触发破防[0] | m_OnDeflectImpact[0].m_bSelfStructureDamageCanGuardBreak[0] | 是 | 本表全部行 |
| 弹开结果配置[0] → 启用自身架势伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfStructureDamage[0] | 是 | H001, H004, H005, H006, H009, H013, H016, H017, H018, H019, H020, H021, H027, H030, H058, H059, H061 |
| 弹开结果配置[0] → 启用自身架势伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfStructureDamage[0] | 否 | H002, H003, H007, H008, H010, H011, H012, H014, H015, H022, H023, H024, H025, H026, H028, H029, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H060 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 35 | H001, H005, H006, H013, H019, H023, H027, H050, H059 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 20 | H002, H003, H007, H008, H012 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 40 | H004, H009, H030, H049, H061 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 0 | H010, H011, H014, H015, H022, H024, H025, H026, H028, H029, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H051, H052, H053, H054, H055, H056, H057, H060 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 50 | H016, H017 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 45 | H018, H020, H021 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 60 | H058 |
| 弹开结果配置[0] → 启用自身特殊眩晕伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfSuperDizzyDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身特殊眩晕伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfSuperDizzyDamage[0] | 0 | 本表全部行 |
| 受击反应类型[0] | m_eHittedReaction[0] | EHittedReaction::Hit | 本表全部行 |
| 命中动作引用[0] | m_hitAction[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 命中动作中发送受击通知[0] | m_bNotifyHittedOnHitAction[0] | 是 | 本表全部行 |
| 命中动作中应用停顿帧[0] | m_bApplyFreezeFramesOnHitAction[0] | 是 | 本表全部行 |
| 命中动作中播放震动[0] | m_bPlayRumbleOnHitAction[0] | 是 | 本表全部行 |
| 普通命中时播放震动[0] | m_bPlayRumbleOnNormalHit[0] | 是 | 本表全部行 |
| 命中情境[0] → 枚举资源[0] | m_HitContext[0].m_Enum[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 命中情境[0] → 缺省枚举索引[0] | m_HitContext[0].m_iDefaultEnumValue[0] | -1 | 本表全部行 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator0 | 本表全部行 |
| 播放 Avoided 订单标志[0] | m_bPlayAvoidedOrder[0] | 是 | 本表全部行 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 0 | H001, H002, H003, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H017, H018, H019, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H032, H033, H034, H036, H037, H038, H039, H041, H042, H043, H044, H045, H046, H047, H048, H053, H054, H055, H056, H057, H059, H060, H061 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 1 | H004, H005, H016, H020, H031, H035, H040, H049, H050, H051, H052, H058 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 1 | H001, H011, H013, H018, H019, H024, H027, H037, H044, H045, H053, H054, H059 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 0 | H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H014, H015, H016, H017, H020, H021, H022, H023, H025, H026, H028, H029, H030, H031, H032, H033, H034, H035, H036, H038, H039, H040, H041, H042, H043, H046, H047, H048, H049, H050, H051, H052, H055, H056, H057, H058, H060, H061 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 1 | H039 |
| 特殊反应攻击等级[0] → 启用自定义持续时间[0] | m_AttackPropertyLevel[0].m_bUseCustomDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 自定义持续时间值[0] | m_AttackPropertyLevel[0].m_fCustomDuration[0] | 0 | 本表全部行 |
| 特殊反应攻击等级[0] → 使用受击动画时长[0] | m_AttackPropertyLevel[0].m_bUseHitAnimDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 保留当前状态剩余时长[0] | m_AttackPropertyLevel[0].m_bKeepCurrentStateDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 保留当前状态时长阈值[0] | m_AttackPropertyLevel[0].m_fKeepCurrentStateThresold[0] | 1 | 本表全部行 |
| 特殊反应攻击等级[0] → 启用自定义距离[0] | m_AttackPropertyLevel[0].m_bUseCustomDistance[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 自定义距离值[0] | m_AttackPropertyLevel[0].m_fCustomDistance[0] | 0 | 本表全部行 |
| 按状态覆盖的攻击等级[0] | m_AttackPropertyLevelOverrides[0] | 未解码（8 字节） | H001, H002, H003, H004, H005, H007, H008, H009, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H035, H036, H037, H038, H039, H040, H041, H042, H043, H044, H045, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 按状态覆盖的攻击等级[0] | m_AttackPropertyLevelOverrides[0] | 未解码（302 字节） | H006, H010 |
| 命中后的最小击退角[0] | m_fMinKnockbackAngleFromHit[0] | 0 | 本表全部行 |
| 击退行为[0] | m_eKnockBackBehavior[0] | EKnockbackBehavior::Regular | 本表全部行 |
| 东西方向击退角[0] | m_fKnockbackEastWestAngle[0] | 45 | 本表全部行 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 7 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032, H033, H034, H036, H037, H038, H039, H041, H042, H043, H046, H047, H048, H049, H050, H051, H052, H053, H054, H055, H056, H057, H058, H059, H060, H061 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 3 | H035 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 2 | H040, H045 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 1 | H044 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 12 | H001, H006, H008, H009, H011, H013, H017, H018, H019, H021, H023, H024, H026, H027, H029, H030, H031, H032, H033, H034, H035, H038, H039, H041, H044, H045, H048, H053, H054, H055, H056, H057, H059, H061 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 2 | H002, H003, H004, H007, H012, H014, H015, H016, H022, H025, H028, H046, H047, H049, H051, H058, H060 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 1 | H005, H020, H050, H052 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 13 | H010 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 0 | H036, H037, H040, H042, H043 |
| 命中盒玩法标签[0][0] | m_HitboxGameplayTags[0][0] | Hitbox.KnockdownHit | H005, H006, H009, H010, H017, H020, H021, H026, H031 |


原始行与字段见 inventory/data-tables.json.gz；三结果数值导出见 exports/hit-impact-values.csv。表名和资源类别仅用于查找，当前是否实战调用需沿动作引用核对。
