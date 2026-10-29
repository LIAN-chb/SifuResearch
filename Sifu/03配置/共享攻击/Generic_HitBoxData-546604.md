# Generic_HitBoxData：攻击效果配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/_Shared/HitBox/Generic_HitBoxData.uasset

本页收录本表全部 32 条已解析 HitBox 行，覆盖普通命中、格挡、弹开三种配置。行 ID 只在本页内定位，不代表独立招式；所有值均非最终实战结果。

## 行索引与韧性相关配置

| 行 ID | HitBox 行名 | 命中种类 | 攻击强度 | 韧性覆盖 | 可招架标志 | Parry 时眩晕标志 | Avoid 时眩晕标志 |
|---|---|---|---|---|---|---|---|
| H001 | PushedChara_HB01 | EHitType::Barehands | EAttackPowers::Medium | 关（保存 0） | 否 | 是 | 否 |
| H002 | WallSplashFar_HB01 | EHitType::Barehands | EAttackPowers::Medium | 关（保存 0） | 否 | 是 | 否 |
| H003 | WallSplashClose_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H004 | WallSplashOnEnvironment_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H005 | FallFromPushed_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H006 | ShoulderPush_HB01 | EHitType::Barehands | EAttackPowers::Light | 关（保存 0） | 否 | 是 | 否 |
| H007 | 360Push_HB01 | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H008 | CharacterDown_HB01 | EHitType::Barehands | EAttackPowers::Medium | 关（保存 0） | 否 | 是 | 否 |
| H009 | ParryStructureBroken_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H010 | TakedownHitOnEnvironment_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H011 | ParryDizzy_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H012 | DropDown_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H013 | SlopeToGround_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H014 | GroundToSlope_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 是 | 否 |
| H015 | TableSplashClose_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 否 |
| H016 | H3_Pendulum_HB01 | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H017 | PunchingBags_HB01 | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H018 | TraversalPush_HB01 | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H019 | TrippedOn | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H020 | PushedSmallObstacle | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H021 | SuperPushedChara_HB01 | EHitType::Barehands | EAttackPowers::Medium | 开：5 | 否 | 否 | 否 |
| H022 | SuperPushedWallSplash_HB01 | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H023 | ToLastMan_FromDown | EHitType::Barehands | EAttackPowers::Strong | 开：5 | 否 | 否 | 否 |
| H024 | WallSplashClose_MC_HB01 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 否 |
| H025 | Arena_Bubble | EHitType::Barehands | EAttackPowers::Medium | 关（保存 0） | 否 | 否 | 否 |
| H026 | GroundToSlope_HB02 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 否 |
| H027 | SlopeToGround_HB02 | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 否 |
| H028 | Cheat_AvoidDamage | EHitType::None | EAttackPowers::Light | 开：-1 | 否 | 否 | 否 |
| H029 | Cheat_EnvironmentDamage | EHitType::None | EAttackPowers::Light | 开：-1 | 否 | 否 | 否 |
| H030 | Cheat_FirewalkDamage | EHitType::None | EAttackPowers::Light | 开：-1 | 否 | 否 | 否 |
| H031 | LoseLionHead | EHitType::Barehands | EAttackPowers::Medium | 关（保存 0） | 否 | 否 | 否 |
| H032 | Cheat_Lifeline | EHitType::None | EAttackPowers::Light | 关（保存 0） | 否 | 否 | 否 |

“Parry／Avoid 时眩晕”列仅报告字段，不足以断言用户的防反／闪避反击追击窗口已经解释完成。

## 普通命中效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：0 | 开：0 | 关（保存 0） | 开：40 | 开：120 | 开：0 |
| H002 | 开：0 | 开：24 | 关（保存 0） | 开：25 | 开：0 | 开：4 |
| H003 | 开：30 | 开：42 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H004 | 开：100 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H005 | 开：50 | 开：120 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H006 | 开：0 | 开：0 | 关（保存 0） | 开：18 | 开：60 | 开：0 |
| H007 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：100 | 开：0 |
| H008 | 开：0 | 开：36 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H009 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：90 | 开：2 |
| H010 | 开：100 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H011 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：0 | 开：2 |
| H012 | 开：0 | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H013 | 开：0 | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H014 | 开：0 | 开：24 | 关（保存 0） | 开：40 | 开：0 | 开：4 |
| H015 | 开：30 | 开：42 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H016 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：60 | 开：0 |
| H017 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：60 | 开：0 |
| H018 | 开：0 | 开：0 | 关（保存 0） | 开：20 | 开：100 | 开：0 |
| H019 | 开：10 | 开：12 | 关（保存 0） | 开：12 | 关（保存 0） | 开：0 |
| H020 | 开：10 | 开：12 | 关（保存 0） | 开：12 | 关（保存 0） | 开：0 |
| H021 | 开：30 | 开：36 | 关（保存 0） | 开：40 | 开：120 | 开：0 |
| H022 | 开：100 | 开：144 | 关（保存 0） | 开：25 | 开：0 | 开：4 |
| H023 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H024 | 开：10 | 开：36 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H025 | 开：0 | 开：0 | 关（保存 0） | 开：25 | 开：100 | 开：0 |
| H026 | 开：0 | 开：24 | 关（保存 0） | 开：40 | 开：0 | 开：4 |
| H027 | 开：0 | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H028 | 开：19 | 开：10 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H029 | 开：10 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H030 | 开：1 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H031 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H032 | 开：9999 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |


## 格挡效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 关（保存 0） | 开：0 | 关（保存 0） | 开：40 | 开：120 | 开：0 |
| H002 | 关（保存 0） | 开：20 | 关（保存 0） | 开：25 | 开：0 | 开：4 |
| H003 | 关（保存 0） | 开：35 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H004 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H005 | 关（保存 0） | 开：100 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H006 | 关（保存 0） | 开：0 | 关（保存 0） | 开：18 | 开：60 | 开：0 |
| H007 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：100 | 开：0 |
| H008 | 关（保存 0） | 开：30 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H009 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：90 | 开：2 |
| H010 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H011 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：0 | 开：2 |
| H012 | 关（保存 0） | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H013 | 关（保存 0） | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H014 | 关（保存 0） | 开：20 | 关（保存 0） | 开：40 | 开：0 | 开：4 |
| H015 | 关（保存 0） | 开：35 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H016 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：60 | 开：0 |
| H017 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：60 | 开：0 |
| H018 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：100 | 开：0 |
| H019 | 关（保存 0） | 开：10 | 关（保存 0） | 开：12 | 开：60 | 开：0 |
| H020 | 关（保存 0） | 开：10 | 关（保存 0） | 开：12 | 关（保存 0） | 开：0 |
| H021 | 关（保存 0） | 开：30 | 关（保存 0） | 开：40 | 开：120 | 开：0 |
| H022 | 关（保存 0） | 开：120 | 关（保存 0） | 开：25 | 开：0 | 开：4 |
| H023 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H024 | 关（保存 0） | 开：30 | 关（保存 0） | 开：25 | 开：0 | 开：6 |
| H025 | 关（保存 0） | 开：0 | 关（保存 0） | 开：25 | 开：100 | 开：0 |
| H026 | 关（保存 0） | 开：20 | 关（保存 0） | 开：40 | 开：0 | 开：4 |
| H027 | 关（保存 0） | 开：0 | 关（保存 0） | 开：40 | 开：0 | 开：0 |
| H028 | 关（保存 0） | 开：8 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H029 | 开：10 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H030 | 开：1 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H031 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |
| H032 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 开：0 |


## 弹开效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H002 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H003 | 关（保存 0） | 开：28 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H004 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H005 | 关（保存 0） | 开：80 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H006 | 关（保存 0） | 开：0 | 关（保存 0） | 开：18 | 开：60 | 关（保存 0） |
| H007 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H008 | 关（保存 0） | 开：24 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H009 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：90 | 关（保存 0） |
| H010 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H011 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H012 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H013 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H014 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H015 | 关（保存 0） | 开：28 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H016 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：60 | 关（保存 0） |
| H017 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：60 | 关（保存 0） |
| H018 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H019 | 关（保存 0） | 开：8 | 关（保存 0） | 开：12 | 开：60 | 关（保存 0） |
| H020 | 关（保存 0） | 开：8 | 关（保存 0） | 开：12 | 关（保存 0） | 关（保存 0） |
| H021 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：120 | 关（保存 0） |
| H022 | 关（保存 0） | 开：96 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H023 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H024 | 关（保存 0） | 开：24 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H025 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H026 | 关（保存 0） | 开：16 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H027 | 关（保存 0） | 开：0 | 关（保存 0） | 开：20 | 开：0 | 关（保存 0） |
| H028 | 关（保存 0） | 开：6 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H029 | 开：10 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H030 | 开：1 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H031 | 开：0 | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |
| H032 | 关（保存 0） | 开：0 | 关（保存 0） | 开：0 | 开：0 | 关（保存 0） |


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
| H031 | 关（保存 0） | 关（保存 0） | 是 | 0 |
| H032 | 关（保存 0） | 关（保存 0） | 是 | 0 |


## 其他保存参数与特殊反应配置

同值参数按适用行 ID 合并；包含攻击属性等级、持续时间／距离开关、状态覆盖、命中筛选、击退行为和防御矩阵等已保存字段。未解码项明确保留。以下也补留各命中结果中未在前表显示的字段。

| 中文标识 | 原字段路径 | 配置值 | 适用行 ID |
|---|---|---|---|
| 命中盒组编号[0] | m_iHitboxGroupID[0] | -1 | 本表全部行 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 60 | H001, H016, H017, H018, H021, H025, H031 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 180 | H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H019, H020, H022, H023, H024, H026, H027, H028, H029, H032 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 0 | H030 |
| 穿透时忽略冲击角限制[0] | m_bIgnoreImpactAngleWhenPenetrating[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 穿透时忽略冲击角限制[0] | m_bIgnoreImpactAngleWhenPenetrating[0] | 否 | H016 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 3 | H001, H005, H016, H017, H019, H020, H021, H023, H025, H031 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 1 | H002, H003, H006, H007, H008, H009, H011, H012, H013, H014, H015, H018, H022, H024, H026, H027, H028, H029, H030, H032 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 2 | H004, H010 |
| 命中盒玩法标签[0] | m_HitboxGameplayTags[0] | [] | H001, H002, H003, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 仅命中具有要求标签的角色[0] | m_bOnlyHitCharacterWithRequiredHitboxGameplayTags[0] | 否 | 本表全部行 |
| 附加到目标的命中盒标签[0] | m_AdditionalHitboxGameplayTagsOnTarget[0] | [] | 本表全部行 |
| 要求的玩法标签[0] | m_RequiredGameplayTags[0] | [] | H001, H002, H003, H004, H005, H006, H007, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 是 | H028, H029, H030, H031, H032 |
| 忽略锁定目标标志[0] | m_bIgnoreTarget[0] | 否 | 本表全部行 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H026, H027, H028, H029, H030, H031, H032 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 是 | H025 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 否 | H028, H029, H030, H031, H032 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 否 | H001, H002, H006, H007, H008, H009, H011, H013, H014, H016, H017, H018, H023, H025, H026, H027, H031 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 是 | H003, H004, H005, H010, H012, H015, H019, H020, H021, H022, H024, H028, H029, H030, H032 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 否 | H001, H019, H020, H023, H025, H028, H029, H030, H031, H032 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 是 | H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H021, H022, H024, H026, H027 |
| 命中时动态击退配置引用[0] | m_KnockBackDynamicOnHit[0] | 对象索引 0；未解析引用 | H001, H002, H003, H004, H005, H006, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 命中时动态击退配置引用[0] | m_KnockBackDynamicOnHit[0] | /Game/DB/Hit/KnockBackDynamicHitByTraversalChara.KnockBackDynamicHitByTraversalChara | H007 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | 对象索引 0；未解析引用 | H001, H002, H003, H004, H005, H006, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | /Game/DB/Hit/KnockBackDynamicHitByTraversalChara.KnockBackDynamicHitByTraversalChara | H007 |
| 弹开结果配置[0] → 动态击退配置引用[0] | m_OnDeflectImpact[0].m_KnockBackDynamic[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害可触发破防[0] | m_OnDeflectImpact[0].m_bSelfStructureDamageCanGuardBreak[0] | 是 | 本表全部行 |
| 弹开结果配置[0] → 启用自身架势伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfStructureDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 0 | 本表全部行 |
| 弹开结果配置[0] → 启用自身特殊眩晕伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfSuperDizzyDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身特殊眩晕伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfSuperDizzyDamage[0] | 0 | 本表全部行 |
| 受击反应类型[0] | m_eHittedReaction[0] | EHittedReaction::Hit | H001, H002, H003, H004, H005, H006, H007, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H031, H032 |
| 受击反应类型[0] | m_eHittedReaction[0] | EHittedReaction::Action | H008, H028, H029, H030 |
| 命中动作引用[0] | m_hitAction[0] | 对象索引 0；未解析引用 | H001, H002, H003, H004, H005, H006, H007, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 命中动作引用[0] | m_hitAction[0] | /Game/DB/_Shared/HitBox/BP_FallHitActionLauncher.BP_FallHitActionLauncher_C | H008 |
| 命中动作中发送受击通知[0] | m_bNotifyHittedOnHitAction[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H031, H032 |
| 命中动作中发送受击通知[0] | m_bNotifyHittedOnHitAction[0] | 否 | H028, H029, H030 |
| 命中动作中应用停顿帧[0] | m_bApplyFreezeFramesOnHitAction[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H031, H032 |
| 命中动作中应用停顿帧[0] | m_bApplyFreezeFramesOnHitAction[0] | 否 | H028, H029, H030 |
| 命中动作中播放震动[0] | m_bPlayRumbleOnHitAction[0] | 是 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H031, H032 |
| 命中动作中播放震动[0] | m_bPlayRumbleOnHitAction[0] | 否 | H028, H029, H030 |
| 普通命中时播放震动[0] | m_bPlayRumbleOnNormalHit[0] | 是 | H001, H003, H004, H006, H007, H008, H009, H010, H011, H015, H016, H017, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 普通命中时播放震动[0] | m_bPlayRumbleOnNormalHit[0] | 否 | H002, H005, H012, H013, H014, H018 |
| 命中情境[0] → 枚举资源[0] | m_HitContext[0].m_Enum[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 命中情境[0] → 缺省枚举索引[0] | m_HitContext[0].m_iDefaultEnumValue[0] | -1 | 本表全部行 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator6 | H001, H007, H016, H017, H018, H025 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator1 | H002, H022 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator5 | H003, H015, H024 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator0 | H004, H009, H010, H011, H019, H020, H021, H023, H028, H029, H030, H031, H032 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator4 | H005, H012 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator7 | H006 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator2 | H008 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator9 | H013, H027 |
| 命中情境[0] → 枚举保存项[0] | m_HitContext[0].m_Value[0] | HitContexts::NewEnumerator10 | H014, H026 |
| 播放 Avoided 订单标志[0] | m_bPlayAvoidedOrder[0] | 是 | H001, H002, H003, H004, H005, H006, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H031, H032 |
| 播放 Avoided 订单标志[0] | m_bPlayAvoidedOrder[0] | 否 | H007, H028, H029, H030 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 0 | H001, H002, H003, H004, H006, H007, H008, H009, H010, H011, H016, H017, H018, H022, H024, H025, H028, H029, H030, H031, H032 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 5 | H005, H012, H013, H014, H015, H019, H020, H026, H027 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 1000 | H021, H023 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 0 | 本表全部行 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 12 | H001, H017, H031 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 0 | H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H015, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H032 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 1000 | H011 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 14 | H016 |
| 特殊反应攻击等级[0] → 启用自定义持续时间[0] | m_AttackPropertyLevel[0].m_bUseCustomDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 自定义持续时间值[0] | m_AttackPropertyLevel[0].m_fCustomDuration[0] | 0 | 本表全部行 |
| 特殊反应攻击等级[0] → 使用受击动画时长[0] | m_AttackPropertyLevel[0].m_bUseHitAnimDuration[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 特殊反应攻击等级[0] → 使用受击动画时长[0] | m_AttackPropertyLevel[0].m_bUseHitAnimDuration[0] | 是 | H011 |
| 特殊反应攻击等级[0] → 保留当前状态剩余时长[0] | m_AttackPropertyLevel[0].m_bKeepCurrentStateDuration[0] | 否 | 本表全部行 |
| 特殊反应攻击等级[0] → 保留当前状态时长阈值[0] | m_AttackPropertyLevel[0].m_fKeepCurrentStateThresold[0] | 1 | 本表全部行 |
| 特殊反应攻击等级[0] → 启用自定义距离[0] | m_AttackPropertyLevel[0].m_bUseCustomDistance[0] | 否 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 特殊反应攻击等级[0] → 启用自定义距离[0] | m_AttackPropertyLevel[0].m_bUseCustomDistance[0] | 是 | H011 |
| 特殊反应攻击等级[0] → 自定义距离值[0] | m_AttackPropertyLevel[0].m_fCustomDistance[0] | 0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H029, H030, H031, H032 |
| 特殊反应攻击等级[0] → 自定义距离值[0] | m_AttackPropertyLevel[0].m_fCustomDistance[0] | -20 | H011 |
| 按状态覆盖的攻击等级[0] | m_AttackPropertyLevelOverrides[0] | 未解码（8 字节） | 本表全部行 |
| 命中后的最小击退角[0] | m_fMinKnockbackAngleFromHit[0] | 60 | H001, H016, H017, H018, H021, H025, H031 |
| 命中后的最小击退角[0] | m_fMinKnockbackAngleFromHit[0] | 0 | H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H019, H020, H022, H023, H024, H026, H027, H028, H029, H030, H032 |
| 击退行为[0] | m_eKnockBackBehavior[0] | EKnockbackBehavior::Regular | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H025, H026, H027, H028, H031 |
| 击退行为[0] | m_eKnockBackBehavior[0] | EKnockbackBehavior::None | H029, H030, H032 |
| 东西方向击退角[0] | m_fKnockbackEastWestAngle[0] | 45 | 本表全部行 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 1 | H001, H006, H017, H018, H021, H031 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 0 | H002, H003, H004, H005, H007, H008, H009, H010, H011, H012, H013, H014, H015, H019, H020, H022, H023, H024, H026, H027, H028, H029, H030, H032 |
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 7 | H016, H025 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 0 | H001, H002, H003, H004, H005, H006, H007, H008, H009, H010, H011, H012, H013, H014, H015, H016, H017, H018, H019, H020, H021, H022, H023, H024, H026, H027, H028, H029, H030, H031, H032 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 2 | H025 |
| 命中盒玩法标签[0][0] | m_HitboxGameplayTags[0][0] | Hitbox.WallSplashHitOnWall | H004 |
| 命中盒玩法标签[0][0] | m_HitboxGameplayTags[0][0] | Hitbox.KnockdownHit | H019 |
| 要求的玩法标签[0][0] | m_RequiredGameplayTags[0][0] | State.Pushed.CanFall | H008 |


原始行与字段见 inventory/data-tables.json.gz；三结果数值导出见 exports/hit-impact-values.csv。表名和资源类别仅用于查找，当前是否实战调用需沿动作引用核对。
