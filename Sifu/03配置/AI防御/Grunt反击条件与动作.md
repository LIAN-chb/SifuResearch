# Grunt反击条件与动作

[[01机制/敌人AI/敌人如何选择防御|防御机制]] · [[03配置/订单与服务/索引|本轮配置入口]] · [[03配置/AI防御/索引|原情境防御表]]

## 对象方向

| 场景 | 谁防守／谁后续动作 | 本页覆盖 |
|---|---|---|
| 玩家招架敌人攻击 | 玩家防守，原攻击者接受反馈 | 下表实际Grunt攻击行与反馈分流 |
| 敌人招架玩家攻击 | Grunt的ParryDeflect节点成功，可能请求AI反击 | 六条完整父链及成功动作／票据引用 |

两侧事件分开核对，不能用AI成功反击配置解释玩家招架后敌人必定眩晕。

## 实际攻击引用与三种结果配置

| AttackDB／段 | 动画帧区间 | HitBox行 | 可招架／招架眩晕／闪避眩晕 | 普通生命／架势／硬直帧 | 格挡生命／架势／硬直帧 | 弹开生命／架势／硬直帧 |
|---|---|---|---|---|---|---|
| Grunt_Hook / 段0 | 22–26 | Hook_HB01 | 是／否／是 | 开:15.0 / 开:18.0 / 开:20 | 开:0.0 / 开:15.0 / 开:20 | 开:0.0 / 开:12.0 / 开:20 |
| Grunt_BaseballHook / 段0 | 42–45 | BaseballHook_HB01 | 是／否／是 | 开:30.0 / 开:36.0 / 开:25 | 开:0.0 / 开:30.0 / 开:25 | 开:0.0 / 开:24.0 / 开:20 |
| Grunt_Uppercut / 段0 | 22–27 | Uppercut_HB01 | 是／否／是 | 开:30.0 / 开:36.0 / 开:25 | 开:0.0 / 开:30.0 / 开:25 | 开:0.0 / 开:24.0 / 开:20 |

数值是启用位约束下的保存配置，不是最终实战结果；动画帧区间含端点。三行实际在Base／Advanced Combo中被引用。缓存可完整覆写，但本轮没有找到它实际改写这些Grunt招架标志的证据。

## 成功ParryDeflect的全部已解析动作父链

| 杂兵／成功节点索引 | 父链逐层测试（全部需通过） | 成功动作／票据 |
|---|---|---|
| 普通 / 36 | 序列31：['Attack.Specific.BackFrontPush']，记忆10.0秒／计数1／原始掩码3 且 攻击属性['Attack.Specific.BackFrontPush']；反转=原生默认false → 序列34：['Attack.Specific.BackFrontPush']，记忆3.0秒／计数1／原始掩码2 | BP_AiLaunchCounterCombo_Parry；原始票据30 |
| 普通 / 43 | 序列38：['Attack.Specific.BackFrontKD']，记忆10.0秒／计数1／原始掩码3 且 攻击属性['Attack.Specific.BackFrontKD']；反转=原生默认false | BP_AiLaunchCounterCombo_Parry；原始票据31 |
| 普通 / 52 | 序列44：['Attack.Type.Hit']，记忆2.0秒／计数1／原始掩码2 且 攻击属性['Attack.Type.Hit']；反转=原生默认false → 序列50：AI自身GuardRatio ≤ 配置0.4 | BP_AiLaunchCounterCombo_Parry；原始票据30 |
| 进阶 / 36 | 序列31：['Attack.Specific.BackFrontPush']，记忆10.0秒／计数1／原始掩码3 且 攻击属性['Attack.Specific.BackFrontPush']；反转=原生默认false → 序列34：['Attack.Specific.BackFrontPush']，记忆3.0秒／计数1／原始掩码2 | BP_AiLaunchCounterCombo_Parry；原始票据30 |
| 进阶 / 43 | 序列38：['Attack.Specific.BackFrontKD']，记忆10.0秒／计数1／原始掩码3 且 攻击属性['Attack.Specific.BackFrontKD']；反转=原生默认false | BP_AiLaunchCounterCombo_Parry；原始票据31 |
| 进阶 / 55 | 序列44：['Attack.Type.Hit']，记忆2.0秒／计数1／原始掩码2 且 攻击属性['Attack.Type.Hit']；反转=原生默认false → 序列53：AI自身GuardRatio ≤ 配置0.4 | BP_AiLaunchCounterCombo_Parry；原始票据30 |

Push分支两者都经过外层10秒／掩码3，再过内层3秒／掩码2；旧摘录将进阶外层当成内层，已更正。这里的多个记忆测试是串联条件，不能只读其中一个。掩码2／3的精确业务标签未恢复，保留数值。

架势测试读取AI自身的BPF_GetGuardRatio；Inferior分支用小于等于比较，不是严格小于。不将其提前翻译成“剩余架势40%”。

## 反击执行与边界

| 环节 | 本轮接通 | 尚缺 |
|---|---|---|
| 成功动作 | 六条节点均挂BP_AiLaunchCounterCombo_Parry；空动作条件数组不取消父链测试 | 节点最终竞争获选与成功回调现场 |
| 票据到Combo | 原始30／31→Custom Combo 1／2；保存转移概率100% | target-node映射仍opaque，不能据此指认实际首招 |
| 额外条件 | Adv两条start entry带MCDomination条件；Base的31带、30未保存该条件 | 条件的精确语义及实战票据请求结果 |
| 策略收尾 | 对手攻击结束时检查AI owner自己的IsStun；自身不stun且无指定防御记录时取消tactic | 原始记录byte2语义和严格逐帧顺序 |
| Avoid对照 | 当前Grunt Avoid节点未保存同类成功反击动作；Adv额外节点记录FirstAvoid并flush FirstParry | 不能等同全游戏没有闪避反击 |
| 全行覆写 | BPF_SetHitboxRow存在；已扫描包名中BP_FallHitRequest引用该函数 | 图字节码、具体传参、其他native写入尚未穷尽 |

证据：`inventory/followup-parry-ai-assets.json`；`notes/parry-ai-followup.md`；架势比较补证在`inventory/followup-structure-test-disassembly.json`，枚举Inferior=1见`inventory/system-recovery-type-layouts.json`。未运行游戏。
