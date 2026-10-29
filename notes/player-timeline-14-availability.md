# 徒手时间轴14：动作许可层取证

## 范围与构建

玩家正在执行当前徒手攻击动作时，以下规则描述攻击窗口向玩家动作许可系统添加的层。未运行游戏，不等同最终实战取消时序。当前 EXE SHA256 每次由 `scripts/disassemble_research.py` 与 `inventory/pdb_overview.json` 严格比对；实际构建和过程范围见 `inventory/timeline14-availability-disassembly.json`、`inventory/timeline14-availability-core-disassembly.json`、`inventory/timeline14-callback-disassembly.json`、`inventory/timeline14-input-disassembly.json`、`inventory/timeline14-selection-disassembly.json`。

## A14-1：攻击窗口重叠按 OR 合成

`OrderAttack::UpdateAvailabilityLayers` RVA 0x1AE99B0 调 `FComboAttack::EnumerateAvailabilityLayerChanges` RVA 0x1957C60。后者逐窗口检查帧区间和命中条件，比较新旧状态，仅对活动变化发回调。回调 caller RVA 0x1AC7B20 跳转 lambda RVA 0x1AC5E60。进入分支在 0x1AC5E90 将 r8b 设为2，0x1AC5EAF 调 `AFightingCharacter::PushAvailabilityLayer`，参数类型明确为 EALBinaryOperation。既有 `CombineAvailabilityLayers` RVA 0x1996780 将2解释为 OR。因此攻击窗口之间添加允许动作，重叠不采用后层覆盖或交集。

退出分支 0x1AC5EE9 起按 LayerData 找保存的 handle，0x1AC5F67 调 PopAvailabilityLayer 并移除记录。`OrderAttack::OnStop` 0x1AE0D89 调 `ClearAvailabilityLayers`，后者0x1AC8843逐handle Pop。因此 open上界只表示配置没有有限上界，不表示订单结束后仍永久生效。

原始代码：`logs/timeline14-availability-core/`、`logs/timeline14-callback/`、`logs/timeline14-input/`。同一层在同一动作多次出现时回调以LayerData作Map键；当前数据若有重叠同层，需单独核查handle替换，不能仅靠理论并集掩盖生命周期。

## A14-2：掩码与命中条件

`UAvailabilityLayerData::GenerateAvailabilityLayer` RVA 0x199DA70 先按invert初始化全部位，再翻转列出位；正选清单是允许项，反选清单是排除项。构造缺省invert=false/context=BasicGameplay，原始证据见 `logs/followup-order-services/` 与 `notes/hitted-services-followup.md`。

`availability-decode.py` 对13版树内及树外动作引用的17层，核uasset与已有清单哈希、导出尾部及enum数组精确消费；输出 `exports/20261029-招式时间轴-14/availability-layers.json`。每层包含原始资产、双文件哈希、invert、listedActions（去InputAction前缀）、listMeaning、context。

窗口条件在0x1957D54–0x1957D82按 FAvailabilityLayerState +4 状态和+5标志选 bit：状态0→2，1→8，2→4，其他且标志false→1、true→16。掩码31覆盖全部分支。各状态符号未在本分支恢复，不给其编造“命中/格挡”等名字；非31窗口必须保留条件限制。

## A14-3：输入与最终执行边界

普通/Alt是不同逻辑InputAction，现有08批 GetInputAction/GetTransition 双向映射复用于JSON的 inputTransitionMapping。LightGuard、HeavyGuard、DodgeAttack的该映射返回None，不得借名称强接对应后继。普通/Alt短按松键共用手势、兄弟清栈配置见 `notes/player-unknown-08-input.md`；不能解释为额外按键。

本轮重新取得 `InputStack::HandleAction/UpdateStack/ConsumeStack`、`UInputManager::GetBestActions/IsBestAction/HandleStackedInputs`。GetBestActions读取 InputStack::GetActionsOnTop；HandleStackedInputs遍历票据、经传入回调测试返回真才ConsumeStack。因此许可不代表最终选中或启动。尚缺：GetActionsOnTop的完整优先级与普通/Alt选择、调用该回调的具体动作准入、当前玩家所有其他许可context和movement限制。仅按窗口OR生成的轴应称“动作许可（静态）”，说明“当前攻击层允许；仍受其他许可层、输入选择及动作启动条件约束”。不得称已实测有效取消窗口。

## 执行与复用

运行 `python -B exports/20261029-招式时间轴-14/availability-decode.py` 返回0、17层；执行 `python scripts/disassemble_research.py --group timeline14-availability --name OrderAttack::UpdateAvailabilityLayers --name OrderAttack::OnStop --name InputStack::ConsumeStack --name InputStack::HandleAction --name InputStack::UpdateStack` 返回0，6过程；core组2过程、callback组8过程、input组2过程、selection组3过程。命令参数及SHA见各inventory报告。callback组按PDB含lambda名选择时带出折叠模板别名，只有上述精确RVA用于语义结论。没有重新解包、修改游戏或存档。

父任务负责共享文档、进度及交接。本分支只写独立层JSON/源码与本底稿；未宣称完成最终执行链或浏览器/实战验收。

## A14-4：继续追到攻击Ability的选择与准入

上文A14-3的“完整普通/Alt选择尚缺”已由本次续查缩小；以下取代其笼统缺口，最终执行仍有明确边界。

- `InputStack::GetActionsOnTop` RVA 0x1A5D000：读取最后票据+0x20字段，并返回所有该字段相同的票据动作。`UInputManager::IsBestAction` RVA 0x1A634F0同样比较目标票据与最后票据的+0x20；无匹配票据时回退 `UInputPad::IsActionActive`。该字段的符号名本分支未恢复，不擅称最后一项单独获胜。
- `UAttackAbility::GetBestAttackAction` RVA 0x19BB340：0x19BB3E1取GetBestActions；0x19BB400–0x19BB493遍历，按角色虚表+0x988、context=13及不预测参数调用许可查询，返回false的候选被删除。签名、参数及角色方法对应 `AFightingCharacter::IsAvailable`，独立取证见 `logs/timeline14-launch/`。
- 同函数0x19BB4A7起遍历Ability+0x448数组，每项步长0x50，输入位位于项+0；从该表顺序挑选仍在候选集的输入，调用GetLazyTargetForInput；若没有有效目标且项+0x30要求目标，并且+0x38条件Evaluate为真则跳过此项，否则选中。不能简化为所有攻击都必须有目标。
- 13批已精确解出的 `actions-ability-cdos.json` 中 BP_AttackAbility `m_Inputs[0]` 是此输入配置；本轮再次核对原uasset、uexp双哈希。完整数组输出到14层JSON的 `attackAbilityInputsInPriorityOrder`。顺序为：AttackLightGuard、AttackHeavyGuard、LightRushAttack、HeavyRushAttack、AttackLightBackFront、AttackLightFrontFront、AttackHeavyBackFront、AttackHeavyAlt、AttackHeavyFrontFront、AttackLightAlt、AttackLight、AttackLightHold、AttackHeavyHold、AttackHeavy、DodgeAttack、Disengage。因此当普通与Alt都在同组有效候选且前面的更高优先输入未选中时，LightAlt先于Light、HeavyAlt先于Heavy；不是任意后层覆盖，也不是额外物理按键。
- `UAttackAbility::CanExecuteAction` RVA 0x19B6D90：必须由ComboManager::GetNextAttackNode返回非空节点；普通节点再用IsValidAttackNode检查；有效蓄力节点要求存在InputCondition，且其+0x20或+0x38状态非零。状态具体符号名未恢复，保持字段级限定。
- `UComboManager::GetNextAttackNode` RVA 0x1937900将输入经BPF_GetTransitionFromInput转为转换类型，调用EvaluateNextAttackState_Internal，必要时走GetTransitionFallback再评估。故图中源边是候选，不能忽略fallback、条件和节点有效性断言必接。
- `UAttackAbility::TryLaunchNewAttack` RVA 0x19CE3B0调用GetBestAttackAction及节点/攻击名选择，后续经Ability虚调用成功路径推进ActionState，末尾0x19CEA99 ConsumeStack并0x19CEAA1 ResetStack。`UAttackComponent::PrepareToLaunchAttack` RVA 0x1943EB0最终0x1944495调角色PlayOrder并保存返回结果；`LaunchAttack` RVA 0x193D710是订单启动后的激活和旧攻击撤销，不是独立“输入允许”判定。

### 玩家许可上下文与移动层

`AFightingCharacter::IsAvailable` RVA 0x19C17D0先调用UFightingMovementComponent::IsAvailable，返回false直接拒绝，再调ABaseCharacter::IsAvailable。movement RVA 0x1AB1820在MovementMode(+0x178)=3时读+0x1410掩码，动作索引越界或位false拒绝；其他mode放行此门。本分支不恢复该mode资产掩码内容。

`ABaseCharacter::IsAvailable` RVA 0x19A1AF0：玩家显式context<12读取该context首个层结果；context13时取UInputManager::GetContextsStack，自末向前遍历，找到有效context结果后返回其动作位，context5直接拒绝；没有有效阻挡项则默认允许。过程中有context虚调用的模式条件；折叠符号名不是可靠语义，本分支未将其编造成AND。其他context不是简单地全部取交集；“当前攻击窗口OR”只对其自身BasicGameplay层合成成立。

### 最终仍缺及为何影响有效取消区间

现在已知普通/Alt候选的表序优先、许可过滤和节点准入入口，不能继续笼统称“完全不知道如何选”。尚未恢复的具体部分：SCGameplayAbility完整激活／打断守卫、各输入BaseCondition蓝图体（如奔跑与方向目标条件）、当前玩家运行时context栈及高优先上下文、movement模式3对应掩码、ComboManager评估内部fallback与运行时节点状态。它们分别影响“许可帧内是否实际启动”“同一按键选择哪个特殊候选”“是否有高层限制”“后继是哪一招”。所以窗口区间可作为已接通OR语义的动作许可，仍不能宣称任意场景下最终有效取消。

Guard、GuardInterrupt和GuardInterruptNoParry是不同InputAction位；当前证据没有互换规则。展示应明确“防御输入许可”而非把Guard直接解释成“防御打断当前动作已成功”。映射返回None的三个transition继续保持未映射。

新增报告：`inventory/timeline14-selection2-disassembly.json`（3过程）、`timeline14-launch-disassembly.json`（5）、`timeline14-action-disassembly.json`（3）、`timeline14-attackability-disassembly.json`（4）、`timeline14-combomanager-disassembly.json`（2），均由同一构建hash检查脚本成功取得。未执行蓝图反编译或实战验证。新增查询出现一次PowerShell通配路径不被rg接受及一个不存在的旧脚本名，已用目录实际文件 `actions-focus-research.py` 与已有CDO JSON替代，未覆盖其历史输出。
