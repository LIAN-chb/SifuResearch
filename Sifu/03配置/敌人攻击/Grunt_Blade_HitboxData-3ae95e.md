# Grunt_Blade_HitboxData：攻击效果配置

[[03配置/配置索引|返回配置索引]] · [[03配置/覆盖范围与读表说明|覆盖范围与读表说明]] · [[01机制/攻击冲击力韧性与伤害|基础机制]]

来源资产：Sifu/Content/DB/AI/Archetypes/Grunt/Attacks/Weapons/Blades/Grunt_Blade_HitboxData.uasset

本页收录本表全部 7 条已解析 HitBox 行，覆盖普通命中、格挡、弹开三种配置。行 ID 只在本页内定位，不代表独立招式；所有值均非最终实战结果。

## 行索引与韧性相关配置

| 行 ID | HitBox 行名 | 命中种类 | 攻击强度 | 韧性覆盖 | 可招架标志 | Parry 时眩晕标志 | Avoid 时眩晕标志 |
|---|---|---|---|---|---|---|---|
| H001 | WideVerticalSlashDown | EHitType::Weapon_Cut | EAttackPowers::Medium | 关（保存 0） | 否 | 否 | 是 |
| H002 | HorizontalSlashRight | EHitType::Weapon_Cut | EAttackPowers::Strong | 关（保存 0） | 是 | 否 | 是 |
| H003 | PushkickWeapon | EHitType::Barehands | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 是 |
| H004 | Stab | EHitType::Weapon_Cut | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 是 |
| H005 | HorizontalSlashRightEngage_01 | EHitType::Weapon_Cut | EAttackPowers::Strong | 关（保存 0） | 是 | 否 | 否 |
| H006 | HorizontalSlashRightEngage_02 | EHitType::Weapon_Cut | EAttackPowers::Strong | 关（保存 0） | 否 | 否 | 是 |
| H007 | OneHandedHandleStrike | EHitType::Weapon_Blunt | EAttackPowers::Strong | 关（保存 0） | 是 | 否 | 否 |

“Parry／Avoid 时眩晕”列仅报告字段，不足以断言用户的防反／闪避反击追击窗口已经解释完成。

## 普通命中效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：20 | 开：24 | 关（保存 0） | 开：25 | 关（保存 0） | 开：2 |
| H002 | 开：25 | 开：30 | 关（保存 0） | 开：25 | 关（保存 0） | 开：2 |
| H003 | 开：10 | 开：90 | 关（保存 0） | 开：25 | 关（保存 0） | 开：6 |
| H004 | 开：35 | 开：90 | 关（保存 0） | 开：25 | 关（保存 0） | 开：4 |
| H005 | 开：15 | 开：18 | 关（保存 0） | 开：25 | 关（保存 0） | 开：2 |
| H006 | 开：20 | 开：24 | 关（保存 0） | 开：25 | 关（保存 0） | 开：2 |
| H007 | 开：10 | 开：90 | 关（保存 0） | 开：25 | 关（保存 0） | 开：2 |


## 格挡效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：5 | 开：20 | 关（保存 0） | 开：25 | 开：100 | 开：2 |
| H002 | 开：6 | 开：25 | 关（保存 0） | 开：25 | 开：80 | 开：2 |
| H003 | 开：0 | 开：90 | 关（保存 0） | 开：25 | 开：160 | 开：6 |
| H004 | 开：9 | 开：90 | 关（保存 0） | 开：25 | 开：80 | 开：6 |
| H005 | 开：4 | 开：15 | 关（保存 0） | 开：25 | 开：80 | 开：2 |
| H006 | 开：5 | 开：20 | 关（保存 0） | 开：25 | 开：80 | 开：2 |
| H007 | 开：0 | 开：90 | 关（保存 0） | 开：25 | 开：80 | 开：2 |


## 弹开效果

| 行 ID | 生命伤害 | 架势伤害 | 特殊眩晕伤害字段 | 受击帧 | 击退距离字段 | 停顿帧 |
|---|---|---|---|---|---|---|
| H001 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：100 | 关（保存 0） |
| H002 | 开：0 | 开：20 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |
| H003 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：160 | 关（保存 0） |
| H004 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |
| H005 | 开：0 | 开：12 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |
| H006 | 开：0 | 开：16 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |
| H007 | 开：0 | 开：40 | 关（保存 0） | 开：20 | 开：80 | 关（保存 0） |


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


## 其他保存参数与特殊反应配置

同值参数按适用行 ID 合并；包含攻击属性等级、持续时间／距离开关、状态覆盖、命中筛选、击退行为和防御矩阵等已保存字段。未解码项明确保留。以下也补留各命中结果中未在前表显示的字段。

| 中文标识 | 原字段路径 | 配置值 | 适用行 ID |
|---|---|---|---|
| 命中盒组编号[0] | m_iHitboxGroupID[0] | -1 | 本表全部行 |
| 最大冲击角[0] | m_fMaxImpactAngle[0] | 180 | 本表全部行 |
| 穿透时忽略冲击角限制[0] | m_bIgnoreImpactAngleWhenPenetrating[0] | 是 | 本表全部行 |
| 目标筛选掩码[0] | m_uiTargetFilters[0] | 3 | 本表全部行 |
| 命中盒玩法标签[0] | m_HitboxGameplayTags[0] | [] | 本表全部行 |
| 仅命中具有要求标签的角色[0] | m_bOnlyHitCharacterWithRequiredHitboxGameplayTags[0] | 否 | 本表全部行 |
| 附加到目标的命中盒标签[0] | m_AdditionalHitboxGameplayTagsOnTarget[0] | [] | 本表全部行 |
| 要求的玩法标签[0] | m_RequiredGameplayTags[0] | [] | 本表全部行 |
| 仅命中锁定目标[0] | m_bHitTargetOnly[0] | 是 | 本表全部行 |
| 忽略锁定目标标志[0] | m_bIgnoreTarget[0] | 否 | 本表全部行 |
| Avoid 时可命中任意角色标志[0] | m_bHitAnyCharacterOnAvoid[0] | 是 | 本表全部行 |
| 允许同时命中多个目标[0] | m_bCanTouchMultipleTargetAtOnce[0] | 是 | 本表全部行 |
| 允许致命命中[0] | m_bCanBeLethal[0] | 是 | 本表全部行 |
| 允许破坏架势[0] | m_bCanBreakStructure[0] | 是 | 本表全部行 |
| 命中时动态击退配置引用[0] | m_KnockBackDynamicOnHit[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 格挡时动态击退配置引用[0] | m_KnockBackDynamicOnGuard[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 弹开结果配置[0] → 动态击退配置引用[0] | m_OnDeflectImpact[0].m_KnockBackDynamic[0] | 对象索引 0；未解析引用 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害可触发破防[0] | m_OnDeflectImpact[0].m_bSelfStructureDamageCanGuardBreak[0] | 是 | 本表全部行 |
| 弹开结果配置[0] → 启用自身架势伤害参数[0] | m_OnDeflectImpact[0].m_bUseSelfStructureDamage[0] | 否 | 本表全部行 |
| 弹开结果配置[0] → 自身架势伤害保存值[0] | m_OnDeflectImpact[0].m_fSelfStructureDamage[0] | 0 | 本表全部行 |
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
| 特殊反应攻击等级[0] → 特殊反应等级分量[0] | m_AttackPropertyLevel[0].m_Level[0] | 0 | 本表全部行 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 0 | H001, H002, H004, H005, H006, H007 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[1] | m_AttackPropertyLevel[0].m_Level[1] | 5 | H003 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 0 | H001, H002, H003, H004, H005, H006 |
| 特殊反应攻击等级[0] → 特殊反应等级分量[2] | m_AttackPropertyLevel[0].m_Level[2] | 1 | H007 |
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
| 命中盒防御矩阵原值[0] | m_iHitboxDefenseMatrix[0] | 7 | 本表全部行 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 14 | H001 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 2 | H002, H005, H006, H007 |
| 可闪避防御矩阵原值[0] | m_iAvoidableDefenseMatrix[0] | 12 | H003, H004 |


原始行与字段见 inventory/data-tables.json.gz；三结果数值导出见 exports/hit-impact-values.csv。表名和资源类别仅用于查找，当前是否实战调用需沿动作引用核对。
