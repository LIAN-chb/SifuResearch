# Hitted订单与服务配置

[[03配置/订单与服务/索引|返回订单索引]] · [[01机制/连续受击与反击追击的系统链|综合机制]] · [[02实现/连续受击与反击追击的系统链|执行证据]]

这里只列本机构建这两份订单默认对象及其全部33条服务；保存值不等于每次受击都激活。父类、条件、动画通知和实例引用需要分别核对。序号保留原始数组下标。

## 本层订单设置

| 订单 | 类型 | 父类 | 启动动作状态 | 停止时弹出动作状态 | 是否标记硬直订单 | 进入／订单间／退出混合时长配置 |
|---|---|---|---|---|---|---|
| OrderHitted | EOrderType::Hitted | /Script/Sifu.OrderHittedDB | EFightingActionState::Hit | 否 | 未保存 | [0.0, 0.0, 0.4000000059604645] |
| OrderHittedGeneric | EOrderType::HittedGeneric | /Script/Sifu.OrderHittedGenericDB | 未保存 | 未保存 | 是 | ['未保存', '未保存', '未保存'] |

`EFightingActionState::Hit`是此字段的准确枚举类型；不要直接视作持续状态`EFightingState::Dizzy`。未保存字段不补成false或0。

## OrderHitted：全部服务

| 下标 | 服务类 | 实例覆写 | 禁用 | 按帧区间启动 | 动画缺少该服务时启动 | 激活条件／反转 | 保存范围／绑定动画 | 冻结处理 |
|---|---|---|---|---|---|---|---|---|
| 0 | DisableGravityOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 1 | HittedLDCollisionOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 2 | KnockdownDisableCollisionOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 3 | JustPushedFromAttackLDCollisionOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 4 | KnockdownUntargettableOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 5 | HittedAvailabilityOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 6 | HitOnGuardALOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 7 | BP_DetectFallOrderService_C | BP_DetectFallOrderService_C_0 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 8 | DisableWalkOffLedgesOrderService | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 9 | HittedCancelAvailabilityOrderService_C | 无 | 否 | 否 | 否 | OrderServiceIsPlayerCondition_C／反转=否 | 无界（保存4） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 10 | KnockdownHitOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 11 | KnockdownDefenseOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 12 | KnockdownALOrderService_MCOffense_C | 无 | 否 | 否 | 否 | OrderServiceIsPlayerCondition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 13 | KnockdownALOrderService_MCDefense_C | 无 | 否 | 否 | 否 | OrderServiceIsPlayerCondition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 14 | KnockdownHitGetUpRedirectOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 15 | RootForPelvisComputationOrderService_C | 无 | 否 | 否 | 否 | OrderServiceIsPlayerCondition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 16 | FallInterruptAvailablityOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 17 | ActivateLookAtOrderService | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 18 | KnockdownSafeZoneOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 19 | HandleSlopeOrderService | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 20 | KnockdownPhysicAnimOrderService_C | 无 | 否 | 是 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 21 | AvailabilityLayerOrderService | AvailabilityLayerOrderService_0 | 否 | 是 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 22 | PushedFromGrabGameplayTags_C | 无 | 否 | 是 | 否 | BP_OrderHittedFallCondition_C／反转=否 | Inclusive:8 → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 23 | AddVariableWeightOrderService | AddVariableWeightOrderService_2 | 否 | 是 | 否 | BP_VariableWeightWeaponIdleCondition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::IgnoreFreezeFrame |
| 24 | DropWeaponOrderService | DropWeaponOrderService_0 | 否 | 是 | 否 | OrderServiceStateCheckForDropWeapon_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 25 | ComboStartStateOrderService | ComboStartStateOrderService_0 | 否 | 是 | 否 | BP_OrderServiceIsPlayerKnockdown_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 26 | HittedPushUntargettableOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 27 | DistFromFloorOrderService | 无 | 否 | 是 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 28 | HittedGetUpNoAttackAvailabilityOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 29 | DisableWalkOffLedgesOrderService | 无 | 否 | 是 | 否 | BP_OwnerDead_Condition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |

## OrderHittedGeneric：全部服务

| 下标 | 服务类 | 实例覆写 | 禁用 | 按帧区间启动 | 动画缺少该服务时启动 | 激活条件／反转 | 保存范围／绑定动画 | 冻结处理 |
|---|---|---|---|---|---|---|---|---|
| 0 | OrderHittedGeneric_HittedOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 1 | KnockdownPhysicAnimOrderService_C | 无 | 否 | 否 | 否 | 无／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |
| 2 | AddVariableWeightOrderService | AddVariableWeightOrderService_0 | 否 | 是 | 否 | BP_VariableWeightWeaponIdleCondition_C／反转=否 | 无界（保存0） → 无界（保存0）；绑定=否 | EOrderServiceFreezeFrameHandling::Freeze |

## 订单内的实例覆写

| 订单／实例 | 本层字段（中文） | 原字段 | 保存值或引用 |
|---|---|---|---|
| OrderHitted.uasset:AddVariableWeightOrderService_2 | 变量权重层枚举 | m_EnumLayer.m_Value | VariableWeightLayers::NewEnumerator4 |
| OrderHitted.uasset:AddVariableWeightOrderService_2 | 骨骼遮罩 | m_BoneMask | /Game/Animations/System/BlendProfiles/Weapon/BlendProfile_Weapon_Generic_RightHand.BlendProfile_Weapon_Generic_RightHand |
| OrderHitted.uasset:AddVariableWeightOrderService_2 | 服务停止时移除 | m_bRemoveOnOrderServiceStop | 否 |
| OrderHitted.uasset:AvailabilityLayerOrderService_0 | 动作许可层数据 | m_availabilityLayerData | /Game/DB/Inputs/Availability/LayerData/Pushed.Pushed |
| OrderHitted.uasset:AvailabilityLayerOrderService_0 | 许可层组合运算 | m_eOperation | EALBinaryOperation::OR |
| OrderHitted.uasset:BP_DetectFallOrderService_C_0 | 进入／离开斜坡命中激活延迟 | m_fEnterLeaveSlopeHitActivationDelay | 0.1 |
| OrderHitted.uasset:BP_DetectFallOrderService_C_0 | 进入斜坡时有命中 | m_bHasHitOnEnterSlope | 是 |
| OrderHitted.uasset:BP_DetectFallOrderService_C_0 | 离开斜坡时有命中 | m_bHasHitOnLeaveSlope | 是 |
| OrderHitted.uasset:ComboStartStateOrderService_0 | 连招起始状态名 | m_ComboStartName | KnockedDown |
| OrderHitted.uasset:DropWeaponOrderService_0 | 掉落原因 | m_eDropReason | EDropReason::FromHit |
| OrderHittedGeneric.uasset:AddVariableWeightOrderService_0 | 变量权重层枚举 | m_EnumLayer.m_Value | VariableWeightLayers::NewEnumerator4 |
| OrderHittedGeneric.uasset:AddVariableWeightOrderService_0 | 骨骼遮罩 | m_BoneMask | /Game/Animations/System/BlendProfiles/Weapon/BlendProfile_Weapon_Generic_RightHand.BlendProfile_Weapon_Generic_RightHand |

## 来源与覆盖

`inventory/followup-hitted-assets.json`保存完整路径、引用、边界和源文件SHA；`inventory/followup-hitted-catalog-table.json`保留上表每行字段及完整引用。提取副本在`logs/followup-hitted/extracted/`。两份类导出含native后缀，未伪称其字节码已经解析；8份默认／子对象的tagged边界已完整核对。

配置里的禁用、帧范围启动、缺动画时启动和激活条件是不同开关。范围无界时保存的0不是有效端点；按帧启动为否也不等于服务永不执行，需继续看动画通知／订单服务生命周期。
