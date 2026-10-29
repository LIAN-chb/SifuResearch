# Avoided与Deflected订单服务

[[03配置/订单与服务/索引|订单索引]] · [[01机制/连续受击与反击追击的系统链|机制]] · [[02实现/连续受击与反击追击的系统链|证据]]

## 订单来源与默认引用

| 对象 | 保存引用／配置 | 边界 |
|---|---|---|
| BP_Grunt_Base.OrderComponent.m_OrderDBs | 全局BP_OrderDB、Grunt_OrderDB | 直接配置已核；具体子类覆写仍需按父链查，不能泛化全敌人 |
| 全局BP_OrderDB | 79个订单引用，包含OrderAvoided、OrderDeflected | 数量是该库引用数，不是独立战斗机制数 |
| Grunt_OrderDB | 1项OrderFallOnSlope | 普通闪避／弹开反应沿全局库可见 |
| 两个订单顶层 | ActivationCondition引用OrderServiceIsPlayerCondition；AvailabilityInfo=AllDefensiveOptions，priority10 | 与下面逐服务条件、GenericNone不是同一字段；顶层条件消费与实际布尔体仍待核 |

## 两个订单的全部服务

两者各3条，配置一致；原始下标为0／1／2。下表保留完整配置差异和角色条件边界。

| 下标／服务 | 施加内容 | 服务级条件／反转 | 范围与启动字段 | 操作／优先级 | 停止处理 |
|---|---|---|---|---|---|
| 0 ForceFightingStateOrderService | EFightingState::Avoided；取角色ResistanceDB；Push duration=-1 | 空条件，反转false | FrameRange=true；两端Open；MissingFromAnim=false | 状态服务，不是许可层运算 | 用返回的状态ID PopFightingState |
| 1 AvailabilityLayerOrderService | GenericNone | OrderServiceIsPlayerCondition，反转true | FrameRange=true；两端Open；MissingFromAnim=false | 原生默认SET；BasicGameplay=0；priority10 | 服务句柄Pop；还受IsPawnMaster等生命周期门槛约束 |
| 2 DeflectedParryCancelAvailabilityOrderService | DeflectedParryCancelAL | OrderServiceIsPlayerCondition，反转false | FrameRange=true；下界Inclusive 8.0，上界Open；MissingFromAnim=false | OR；priority20 | 许可层服务停止路径回收；具体激活条件另核 |

`OrderServiceIsPlayerCondition`的资源名、函数名及IsPlayerControlled引用都已读到，但蓝图返回表达式尚未完整解析；因此表中角色方向仍是配置条件，不写成所有NPC都必定执行／所有玩家都必定跳过。8.0的时间基准未闭合，不改写成8帧或8秒。

## 相关动作掩码

| 资源 | 保存动作列表／选取方式 | 四种AI防御动作的位 | 说明 |
|---|---|---|---|
| GenericNone | 正选：Look、MouseLook、DizzyReduction、ReplayMenu | Avoid、Parry、Guard、Dodge均false | 名为None但保留四项；不能说全部输入关闭 |
| AllDefensiveOptions | Guard、Parry、PrepFocus、Avoid、Look、MouseLook、Dodge | 此资源包含四种防御 | 顶层路径资源，不等于逐服务GenericNone，也不据名字认定整单最终结果 |
| DeflectedParryCancelAL | ParryInterrupt、Parry | 仅列保存动作；完整结果还受OR组合和其他层影响 | 玩家侧候选取消许可，条件与8.0基准仍待核 |

## 状态时长与对象区分

Force服务传-1经PushFightingState的负时长分支写入Infinite标志；服务停止时按句柄Pop。它不是Grunt普通Dizzy的3／1.5秒。OrderAvoided本身的0.666／0.5秒配置、OrderDeflected读取所有者GuardDB的时长，以及后来命中产生的Dizzy时长分别管理。

当Avoided成为最高活动状态时，后续攻击可用其抗性矩阵行；当前Base／Adv配置的[击倒,推开,眩晕]为[0,0,1]，InFight为[2,2,11]。有其他更高状态、命中属性覆写或服务未激活时要另算，不从订单名断定必用哪一行。

来源：`inventory/followup-order-services-packages.json`保留10个定向包及文件哈希、完整导出／数组边界；执行见`notes/order-services-followup.md`和`inventory/followup-order-services-disassembly.json`。已提取、已解析及调用已接通分开记录；未实战验证。
