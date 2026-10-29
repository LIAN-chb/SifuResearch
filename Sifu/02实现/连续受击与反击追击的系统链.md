# 战斗状态与事件：实现映射

[[01机制/连续受击与反击追击的系统链|系统规格正文]] · [[03配置/受击案例配置对照#通用规则的字段中文说明|字段中文说明]]

正文是唯一顺序阅读主线。本页把同一套规则编号映射到数据和函数，不另讲一套机制；旧专题作为证据／配置附录。

| 正文编号 | 对象／函数（RVA） | 输入→输出与准确证据 |
|---|---|---|
| 状态模型、选择顺序 | `UDefenseComponent`状态数组；`FFightingStateElement`；`GetHighestActiveFightingState` `0x195C370` | 多记录→固定顺序选一个存在的类型。`inventory/followup-hitted-type-layouts.json`、`inventory/state-spec-20261029-priority.json` |
| E2→E3→E4局部顺序 | `UHitComponent::ApplyImpact` `0x1A46D90` | 普通伤害调用 `0x1A47165`→状态更新 `0x1A47C7F`→末尾命中广播 `0x1A484C8`；`notes/20261029-rules-hit-count.md` |
| T0–T6转移 | `UpdateFightingStateFromImpact` `0x1A70A70` | Impact＋旧集合／句柄→新集合／累计搬运。T1段 `0x1A70B86–0x1A70BF1`，T2段 `0x1A70BF8–0x1A70C6D`，T3–T6段 `0x1A70C6D–0x1A70D5D`；`notes/20261029-state-spec-refinements.md` P2 |
| D1–D9时长树 | `ApplyFightingStateFromImpact` `0x1A46990` | 攻击配置、容器、旧状态、目标反应和两个时间来源→新D。保时长无旧状态跳转 `0x1A46B76→0x1A46BDF`；`notes/20261029-state-spec-refinements.md` P3/P4 |
| 新记录构造 | `PushFightingState` `0x1966D90` | D、上限、累计、子类型及回调→新元素／句柄／相关上下文。来源 `logs/followup-state-availability/UDefenseComponent__PushFightingState-0x1966d90.asm.txt` |
| U1/U2 | `OnDamage` `0x1965280` | 逐元素按maxDamage>0加伤害，按maxHits>0加次数；无攻击名归组过滤 |
| U3 | `OnHit` `0x19653B0` | 逐元素按maxHits及攻击名归组更新次数／名称。与U1/U2同在 `notes/20261029-rules-hit-count.md` |
| U4–U7 | `TickComponent` `0x196A130` | `0x196A2C0–0x196A326`：先跳过pause/infinite，再elapsed累加、时间／伤害／次数顺序判定，调用Pop |
| A1–A5 | `PushFightingState`、`PopFightingState` `0x1966130`、NPC `IsAvailable`、`UpdateDefenseNeed` | 状态持有上下文→首有效上下文的查询结果→四项全false时评估退出；Pop回收自身。既有E20，`notes/hitted-services-followup.md` |
| 普通受击恢复通知 | `OrderHitted::IsStunOrder` `0x19FDB50`；OnUpdate `0x1AE46E4–0x1AE47B1` | 计时和恢复守卫→推层／广播→AI条件性重评估；既有E23，`notes/case-study-ordinary-20261028.md` |
| C1–C3分类器接口 | `ComputeImpactType` `0x1A51F10` | 状态／效果／防守结果→ImpactType；严格比较、GuardType跳过候选选择、后段保时长阈值。`notes/20261029-rules-resolution.md` R01–R03；完整候选树未恢复 |
| C4/C5其他输入 | Avoid链、目标被招架条件蓝图 | `notes/avoid-system-chain.md`、`inventory/20261029-parry-condition.json`；订单记录不自动等于FightingState |

## 本次修订与未完成接口

旧版按“受击、眩晕、退出、AI”分章的说明已被替换为同一事件处理模型。新增复核只收窄和补齐已有函数守卫，不声称恢复完整游戏逻辑。

- 时长keep无旧状态的跳转，以新P3为准，前版“默认回退”撤回。
- 动画时间使用攻击方冻结时长，不能与函数入参额外时间混同。
- 精确缺口统一在正文第9节：分类器、默认时长内部、动作准入、初始字段、非命中调用者、Opened接口、Tick时间输入和返回标签消费。

构建：EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`；PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age1。补充底稿 `notes/20261029-state-spec-refinements.md`；本批清单 `inventory/state-spec-20261029-batch.json`。静态规格，未实战验证。
