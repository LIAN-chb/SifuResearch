# 攻防补证：环境墙撞与倒地累计

本支批次 `20261030-攻防补证-wall-ground`，问题为推击后的墙撞专用命中是否重新进入命中处理，以及普通／进阶 Grunt 倒地累计阈值。完成条件：给出配置字段→代码消费者→后续命中接口的可定位链，未闭合分支具名。写入仅本文件、`inventory/interaction-20261030-wall-*`、`logs/interaction-20261030-wall-*`、独立脚本；共享交接由主代理维护。游戏与存档只读，不启动游戏。

复用：已有 object-and-table-properties CSV、状态计数底稿；因旧产物仅有墙撞配置入口，本次新增有界反汇编。`disassemble_research.py` 每次实际校验 EXE SHA256，符合当前构建 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；PDB匹配由主批核验（GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age 1，SHA256 `5925d79b63df58ff98575454f3d31b07a4e0da44f96dc19461fc5b7e56d1b90c`）。实际命令、版本／哈希、输入与输出在本支 manifest 补记。静态链不证明实战触发。

## 初始断点（以下WG2–WG7为后续已保存结果）

已找到真正消费者 `FHandleLDCollisionOrderServiceInstance::OnBlocked` → `GetWallHit` → `ApplyImpact` → `UHitComponent::HandleImpact`。正在核字段布局、Grunt阈值及近墙分支。

## WG1. 讨论范围与对象

当前事件中，“受推角色”是正在执行移动／受推订单并持有该碰撞服务的 `AFightingCharacter`；“碰撞对象”是 `FHitResult` 的 actor，不能混成受推角色。“原订单目标”从该服务所持订单读出；本支未把它概括为任何时候都等于玩家。

本次把未知边界从“只有墙撞配置入口”推进到“碰撞服务已接通命中管线”。没有启动游戏；不能从静态路径得出具体敌人必在某次推击碰到墙、服务必被挂载或一定生成 Dizzy／KnockedDown。

## WG2. 字段归属与默认墙撞命中选择

布局证据：[布局清单](../inventory/interaction-20261030-wall-types.json)，适配脚本为 `scripts/interaction-20261030-wall-types.py`。沿用16批已识别的 LF_ONEMETHOD 引入虚函数记录固定4字节修正，仅本支内存适配，未修改公共读取器。以下偏移均是当前构建对象偏移：

| 对象／字段 | 偏移 | 本次代码消费者 |
|---|---:|---|
| `UAttackPropertiesResistanceDB.m_PushedReaction` | `+0x390` | `BPE_GetWallHitBox_Implementation` |
| `FPushPropertyReaction.m_WallSplashHit` | `+0` | DB绝对偏移 `+0x390` |
| `FPushPropertyReaction.m_WallSplashCloseHit` | `+0x298` | DB绝对偏移 `+0x628`；本支未恢复其选择消费者 |
| `FPushPropertyReaction.m_WallSplashHitOnWall` | `+0x530` | DB绝对偏移 `+0x8C0`，`ApplyImpact` 第二段 |
| `FPushPropertyReaction.m_HitBox` | `+0x7C8` | DB绝对偏移 `+0xB58`，`BPE_GetHitBox_Implementation` |
| `UHandleLDCollisionOrderService.m_bUseCustomWallHit`／`m_CustomWallHit` | `+0x119`／`+0x120` | `BPE_GetWallHitBox_Implementation` 自定义覆盖 |
| `FBaseOrderServiceInstance.m_Owner` | `+0x40` | 当前受推角色 |
| `FHandleLDCollisionOrderServiceInstance.m_bAlreadyHandled` | `+0xE0` | `OnBlocked` 入／出口去重 |

`GetWallHit` RVA `0x1AFFF80` → `BPE_GetWallHitBox`；默认 native 实现 RVA `0x1AF0C70` 在 `0x1AF0C76` 先检查服务 `m_bUseCustomWallHit`，真则复制自定义 `FHitBox`，否则取传入实例的 owner → `AFightingCharacter+0x12A8` DefenseComponent → 当前 `GetAttackPropertiesResistanceDB()`，从 `DB+0x390` 复制 `m_WallSplashHit`。因此默认选择与受推角色当前抗性DB有关，不是从原攻击者DB选墙撞行。该接口是 Blueprint event，不能把 native 默认实现当作所有派生服务的唯一实现。

原始反汇编均见 `logs/interaction-20261030-wall-code/`；每项的RVA、范围、输出SHA256在[反汇编清单](../inventory/interaction-20261030-wall-code-disassembly.json)。

## WG3. 碰撞触发守卫与一次处理

`OnPersistentInstanceStarted` RVA `0x1B06680` 在 `0x1B06A4B` 清 `m_bAlreadyHandled`；当服务数据 `m_bHandleHittedByEnvironment (+0x28)` 为真，`0x1B06A71` 取 `OnBlocked` 函数地址并建立回调。这里补的是代码消费者；实际订单／服务挂载仍须查配置和激活条件。

`OnBlocked` RVA `0x1B04D50` 本次完整有界反汇编。可直接确认的阶段顺序：

1. `m_bAlreadyHandled` 为真则返回；owner 必须是有效 `AFightingCharacter`。
2. 碰撞对象若为 `ACharacter`，走目标阻挡／移动忽略角色分支并离开本段墙撞路径，不能把撞到另一人直接称为环境墙撞。
3. 若配置启用早期 traversal 检测且 elapsed 仍小于 `m_fDetectTraversalDuration`，成功 `DetectTraversal` 则提前离开；`TryHandleCustomObstacle` 成功也提前离开。
4. 普通环境分支从碰撞法线和当前移动速度取水平方向，要求两方向非近零且点积为负；水平速度长度须达到服务 `m_fWallHitMinVelocity (+0x114)`（低于阈值跳出）。
5. 调 `AngleBetweenVectorHorizontal`，阈值来自 `m_fWallHitMinAngleDeg (+0x110)` 或启用时的 `m_WallHitMinAngleDegOverTime (+0x88)` 按服务 elapsed 求值，再加90度。绝对角度达到阈值可处理；否则还存在左右法线角度累积、二者合成方向再次检验的拐角分支。不能将此条件简化为任意擦墙即触发。
6. 通过后依 `m_bInverseOrientationOnHit` 选择朝向，更新受推角色旋转；`0x1B05516` 调 `GetWallHit`，`0x1B05527` 调服务 `ApplyImpact`，随后 `0x1B05535` 将 `m_bAlreadyHandled` 设真。

`OnPostOrderUpdate` RVA `0x1B09120` 还有 traversal 相关路径调用同样的 `GetWallHit`／`ApplyImpact`（`0x1B093CE`／`0x1B093E1`）。本支仅定位该调用，不以普通墙面 `OnBlocked` 守卫外推该分支全部条件。

## WG4. 受推角色与环境对象分开承受命中

`FHandleLDCollisionOrderServiceInstance::ApplyImpact` RVA `0x1AEF490`：

- `0x1AEF521` 从服务 owner取当前受推角色，`0x1AEF551`附近取其 HitComponent，`0x1AEF57C`取其当前抗性DB。构造 `FHitRequest` 并复制传入墙撞 `FHitBox`。
- `0x1AEF6D1` 写 `FHitRequest.m_Target (+0x104)` 为服务 owner；`0x1AEF6E0` 写 `m_Instigator (+0xE4)` 为从原订单上下文读出的原订单目标。原始攻击／受击角色在此经过新的环境事件映射，不能省略主语。
- `0x1AEF753` 取 `BPE_GetHittedAnimContainer`，若其有动画则设置 forced hitted anim；native默认实现 `0x1AF0B00` 返回空容器，派生BP仍可覆盖。
- `0x1AEFA11` 调当前受推角色 HitComponent 的 `HandleImpact(FHitResult,FHitRequest,FApplyImpactStruct,...)`。这是真正重新进入受击管线的证据，不只是资产引用。
- `0x1AEFA24`复制请求；`0x1AEFA29–0x1AEFAFE` 取当前受推角色DB的 `+0x8C0`，即 `m_PushedReaction.m_WallSplashHitOnWall`，替换新请求的 HitBox。随后查实际碰撞对象的 `UHitComponent`，`IsCompatibleWithTarget` 通过后在 `0x1AEFB88` 调其 `HandleImpact`；后面还有按该HitBox范围查询命中对象并逐个处理的分支。**该配置是打环境／碰撞对象的命中，不能把它的 Damage=100 当受推敌人的墙撞伤害。**

## WG5. 后续仍走 Generate／Filter／Apply；没有固定“墙撞状态”证据

新增反汇编[清单](../inventory/interaction-20261030-wall-more-disassembly.json)与 `logs/interaction-20261030-wall-more/`：`UHitComponent::HandleImpact` 带 ApplyStruct重载 RVA `0x1A61360`，经守卫后在 `0x1A614D0` 调 `GenerateImpact`，`0x1A615A6` 调 DefenseComponent `FilterImpact`，未被拒绝时在 `0x1A615EF` 调 `UHitComponent::ApplyImpact`。另一个重载 `0x1A612E0` 只是构建默认 ApplyStruct再转此函数。

因此墙撞是产生专用命中资料再复用现有命中处理的入口。已经恢复的 `ComputeImpactType → ApplyFightingStateFromImpact／UpdateFightingStateFromImpact` 与订单创建仍适用相应条件；本支不据专用行名发明一个新 FightingState，也不称每次墙撞必进入 Dizzy、必倒地或全部等同普通拳击。

普通／进阶Grunt与BaseResistanceDB的配置均指向：`m_WallSplashHit → WallSplashFar_HB01`；`m_WallSplashCloseHit → WallSplashClose_HB01`；`m_WallSplashHitOnWall → WallSplashOnEnvironment_HB01`。Generic表中的 Far／Close 行均为 `m_eHittedReaction=Hit`、三项 `m_AttackPropertyLevel.m_Level=[0,0,0]`、`m_hitAction=0`。Far行 OnHit 原始数值为 Damage=0（启用）、StructureDamage=24（启用）、NbFrameStuned=25（启用）；Close行为 Damage=30（启用）、StructureDamage=24（启用）、NbFrameStuned=25（启用）。这些是配置，不能充当最终伤害或最终受控时间；状态和伤害仍可能受后续管线影响。

## WG6. 实际 Grunt 倒地累计样本

来源为 `inventory/tagged-objects.json.gz` 的相应 `AttackPropertiesResistanceDB` 导出，并与 `inventory/object-and-table-properties.csv` 按对象、完整字段路径核对。[配置清单](../inventory/interaction-20261030-wall-config.json)保留源文件SHA256、原CSV行号、所选 tagged 字段及原导出SHA256；独立脚本断言4个所选导出阈值一致，成功退出0。

| DB（完整asset路径见清单） | `m_DownReaction.m_Movement.m_fDuration` | `m_fMaxAccumulatedDamage` | `m_iMaxAccumatedHits` | `m_bGroupMaxAccumulatedHitsByAttack` |
|---|---:|---:|---:|---|
| `Grunt_Base_ResistanceDB` | 4 | -1 | 2 | false |
| `Grunt_Adv_ResistanceDB` | 4 | -1 | 2 | false |
| `Grunt_Miniboss_ResistanceDb` | 3 | -1 | 2 | false |
| `BaseResistanceDB` | 0.5 | -1 | 2 | false |

布局：DB `m_DownReaction +0x180`；`FPropertyReaction` 内 maxDamage `+0xA4`、maxHits `+0xA8`、group flag `+0xAC`。以上普通／进阶Grunt样本的倒地**累计伤害退出阈值禁用，累计次数阈值为2且不按攻击名归组**。次数不是直接等于玩家必须打两拳：沿用[事件计数底稿](20261029-rules-hit-count.md)，一次实际伤害命中可分派 `OnDamage → Update → OnHit`，重建状态／两路计数和守卫决定元素实际计数；不能把表值当最终拳数。duration=4同样只是 Movement配置，并非所有倒地最终固定4秒。

Tick退出判定与倒地重建的复制范围复用[状态更新底稿](20261029-rules-state-update.md)及事件计数底稿，本支未重跑其函数体：启用计数阈值时 `hits >= maxHits` 移除，伤害阈值只在 maxDamage>0时启用。倒地旧元素重建特定分支继承次数、不继承旧累计伤害的结论边界保持。

## WG7. 验证、失败与停止位置

- 本支新增12个过程范围的有界反汇编（7+5；包含 HandleImpact两个重载）。脚本每次重核EXE SHA256，退出0，无缺名；输出哈希逐项写入两份反汇编清单。
- PDB类型本支执行两次：首次请求的 `FPushedReaction`／`FKnockedDownReaction`／`FKnockDownReaction` 无匹配；依据DB成员真实类型改用 `FPushPropertyReaction` 与 `FPropertyReaction` 后取得布局。最终只保留本题所需9个布局。缺名是拼写不匹配，不证明游戏不存在倒地／推击逻辑。
- 独立配置脚本复核4个 tagged导出与CSV字段；未重新提取资产，不覆盖旧解析清单。Python与dumpbin实际版本、脚本与输入SHA256、完整命令、输出位置见[执行清单](../inventory/interaction-20261030-wall-manifest.json)。
- 本支只新增底稿／独立清单／原始反汇编；知识库整体验证由主代理在合并后执行。不宣称本支已跑知识库检查器或实战验证。
- 仍缺1：`OrderPushed`或受击派生订单实际配置挂载何种 collision service、激活窗口与BP覆盖。`HittedLDCollisionOrderService`已有包记录含 `BPE_GetWallHitBox` 与 CustomWallSplashHitbox线索，不能只凭名字认定其运行期覆盖结果。
- 仍缺2：近墙 `m_WallSplashCloseHit (DB+0x628)` 选择消费者及近／远判定。当前确认的 default碰撞服务选 Far；不能把该Far链冒称Close链全部恢复。
- 仍缺3：指定场景命中后最终订单／状态与运行时实际触发。下一步应定向解 `HittedLDCollisionOrderService` BP函数／具体订单服务配置，并追 `DB+0x628` 的读取。验收需看完整 guard与命中递交，不能再停在引用名称。

本支不提交、不改共享进度；由主代理归并。用户无需手动操作。
