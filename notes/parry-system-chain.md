# 招架／弹开反馈到原攻击者：本机构建静态证据

更新：2026-10-28。仅静态；EXE SHA256 `a603e29f9a0a4b06e43f662ec6a67f41bea37a57216fb454e106e9e64af28254`，PDB GUID `fdd64e0f-b9ed-4479-8fd8-efe0038b919d` age 1。

## 已证实的分流

| 连接 | 机器码与数据 | 可支持的结论 |
|---|---|---|
| 防御成功 → 原攻击者反馈 | `UGuardAbility::OnHitDefense` RVA `0x1a025f0`，见 `logs/counter-punish/UGuardAbility__OnHitDefense-0x1a025f0.asm.txt` | 并非仅通知成功；相关分支会给原攻击者 GenerateImpact / ApplyImpact。 |
| CanDeflect 且允许反馈破架势、即将破架势 → StructureBrokenHit | 分支 `0x1a028c9–0x1a02d87`，能力 +0x568；`BP_GuardAbility` CDO 引用 `Generic_HitBoxData/ParryStructureBroken_HB01` | 破架势反馈必须单独记录，不能与普通招架后眩晕混同。 |
| 未进破架势分支，CanDeflect 且来袭行 m_bDizzyOnParry → ParryDizzyHit | 来袭行 +0x1b1；分支 `0x1a03072–0x1a03225`；能力 +0x800 | 条件式专用命中，不是所有成功招架的必然结果。 |
| 专用反馈 → 实际 Impact | 模板拷贝后覆写 OnHit.m_bUseStructureDamage / m_fStructureDamage 和 SuperDizzyDamage，来源为本次 AppliedDeflectImpact 的 self 值；目标为原攻击者、施加者为原防守者 | 模板表中的零伤害不能当最终反馈数值；普通生命伤害、架势反馈与 SuperDizzy 量须分开。 |
| 反馈量来源 | `FDeflectImpact::GetSelfStructureDamage` RVA `0x197fda0`、`GetSelfSuperDizzyDamage` RVA `0x1980000`，清单 `inventory/system-deflect-getters-disassembly.json` | 命中行若有显式覆盖则用覆盖；否则 incoming m_bParriable=true 时从防守者 GuardDB 的 ParryAttackerStructureDamage / SuperDizzyDamage 取；否则从其默认 DeflectImpact 取。架势反馈还读取 ParryImpactOnStructureBonus 属性。 |
| 可变 HitBox 行 | `FHitBox::GetRow` RVA `0x197fbe0`，`GetMutableRow` RVA `0x197eaa0` | useCached=true 且已有缓存时返回缓存行；否则数据表行，失败再游戏默认表／默认对象。原始表不能保证本次运行行未被覆写。 |

## 本地配置与适用范围

能力 CDO 完整导出：`inventory/system-defense-ability-cdos.json`，34 个对象、零解析失败；保留原文件路径与 uasset/uexp 哈希。字段布局：`inventory/system-parry-type-layouts.json`。原始表：`inventory/data-tables.json.gz`，通过表路径与行名定位。

| 对象／行 | 本机保存值 | 使用边界 |
|---|---|---|
| BP_GuardAbility | m_bEnableNewGuard=true；m_bEnableDeflectInterruptOnDeflectNonInterrupt=true；两个 HitBox 模板引用如上 | 实例／技能覆写另查。 |
| ParryDizzy_HB01 | Dizzy 等级1000；Strong冲击力2；stun20帧；UseHitAnimDuration=true；普通生命伤害0；架势、SuperDizzy基础0 | 后两项由代码覆写。20帧不等于完整Dizzy时长；持续时长可取受击动画。 |
| ParryStructureBroken_HB01 | 等级0/0/0；Strong2；stun20帧；UseHitAnimDuration=false；knockback90 | 对应破架势分支；不能拿此行证明普通Dizzy。 |
| MC_GuardDB | ParryAttackerStructureDamage50，SuperDizzyDamage10；DeflectedDuration0.6秒 | 50/10的取值仍取决于显式覆盖和incoming m_bParriable。0.6是该GuardDB所有者的Deflected配置。 |
| Grunt_GuardDB | 上述两个Parry反馈基础值0；DeflectedDuration0 | OrderDeflected读取订单所有者自己的GuardDB，不能把主角0.6秒套到敌人身上。 |
| Grunt_HitBoxData 20行 | m_bDizzyOnParry均false；m_bParriable仅Hook_HB01、BaseballHook_HB01、Uppercut_HB01为true | 这些是原始表行。未证明所有实际攻击均引用此表、缓存未改；因此本次不能用专用ParryDizzy模板解释全部杂兵招架现象。 |

## 其他原攻击者反馈

`UAttackComponent::HandleDeflectedImpact` RVA `0x1939630` 对攻击者施加反馈架势／SuperDizzy量；在允许破架势并达到阈值时 PushGuardBreakFightingState，启动相应状态订单。`HandleHitResult` RVA `0x1939ec0` 还有反馈与订单处理。`OrderDeflected::OnStart` RVA `0x1ade500` 从订单所有者 GuardDB 读取 DeflectedDuration、AttackScaleCurve；Update `0x1ae3ba0`递减并按曲线修改攻击播放比例，Stop `0x1ae14e0`回收修改与相关许可句柄。这条分支不能直接写成固定不能防御的眩晕时钟。

`AFightingCharacter::OnOrderParryInstigatorStarted` RVA `0x19c5300` 构造命中描述并广播；该函数本身没有生成新的Impact。事件名不等于确认已进入独立Parried持续状态。

## 对旧笔记的精确修正

旧 `notes/counter-punish.md` 中将模板反馈后 `Hitted` 回调归给目标、并认为 GenerateImpact 显式传入目标ResistanceDB的解释不准确。寄存器归属：rdi是原防守者，模板GenerateImpact/ApplyImpact的组件属于原攻击者；紧随其后的Hitted调用对象为rdi。GenerateImpact该次resistance override实参为null，内部正常查询，不是这里显式传入DB。只据ApplyImpact说明模板作用对象；不据后续Hitted调用重复证明攻击者受击。

旧 `notes/stun-ai-defense.md` 里的 IsStunChanged Blackboard 条件也需修正：比较的是非零分支，不是已经证明的Unreal无效枚举哨兵；ParryDeflect的IsStun检查对象是AI所有者，不是玩家。综合页以这些更精确的归属为准。

## 未闭合点与下一项取证

1. 固定Grunt实际发出的Hook/Jab命中段，核对AttackDB→HitBox行及缓存覆写写入者，确定哪些招架实际进入专用Dizzy分支。静态入口已缩到FHitBox缓存行与能力两个模板分支。
2. 不走专用Dizzy时，沿HandleHitResult/Deflected订单的启动延迟、原攻击订单的EndOfStrike收尾及GuardDB所有者还原可追击时间。原始Grunt DeflectedDuration=0，不能用MC的0.6补齐。
3. 将技能ParryImpactOnStructureBonus和攻击组件反馈覆盖作为独立因素；尚未固定角色成长／神龛版本，不报告最终架势反馈数值。