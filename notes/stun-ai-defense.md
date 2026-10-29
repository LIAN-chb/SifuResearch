# Sifu AI defense, attack memory, and stun recovery

## Scope and method

Static inspection only. `scripts/trace_ai_defense.py` reuses the parent’s SHA-verified `scripts/disassemble_research.py` helper to export bounded procedures from the matched Sifu shipping EXE/PDB to `logs/stun-ai-defense/`. The resulting PDB RVAs and disassembly file hashes are indexed in `inventory/stun-ai-defense-disassembly.json`. No game code was run and no game files were changed.

Data cross-reference uses the parent’s `exports/grunt-contextual-defense.json`, which contains serialized properties from `Grunt_Base_ContextualDefense` and `Grunt_Adv_ContextualDefense`. The machine-code evidence below describes compiled branches; the asset evidence describes authored graph values and links. A field name by itself is not treated as behavior proof.

## How enemy defense requests are selected

`FAIDefenseHandler::UpdateDefenseNeed` (RVA `0x18c9e50`) obtains the relevant actor and its `UAttackComponent`, fetches an early hitbox, and calls `IsDefenseNeededInternal` before continuing. That internal function (RVA `0x18b8fc0`) consults the target’s current attack data and calls `UFightingCharacterHelpers::ComputeIncomingAttackPrediction`. If the prediction path says no defense is needed, the update exits without selecting a node. When it continues, the handler queries the defender’s highest active fighting state and current `UAIContextualDefense`, then constructs/picks and validates a `FAIDefenseRequest` before applying it.

`UAIContextualDefense::PickContextualDefense` (RVA `0x1895070`) iterates its authored node list and calls `TestNodeForContextualDefense` on each candidate using the influence-test results and context. The serialized `AIInfluence_TestSequence` assets store explicit test arrays and linked-node arrays; examples below are concrete authored branches, not an inference from names alone.

When `ComputeDefenseRequest` (RVA `0x18ac4e0`) switches to a different selected node, it calls `FAIAttackHandler::OnDefending` and cancels pending AI actions before setting up the new request. This is a concrete point where the AI abandons pending attack/action work to defend against an incoming attack. The exact contents of each pending action are runtime-dependent.

## Attack memory is linked to defensive adaptation

The code connects recent received attacks to the authored defense tests:

- `UAIFightingComponent::UpdateAttackReceivedMemory` (RVA `0x18c9b80`) calls `AIMainMemory::UpdateMemoryWithPredicate` with memory-type byte `3`.
- `UAttackMemoryInfluenceTest::RunTest` (RVA `0x18ef840`) reads full memory type `3`, iterates its 32-byte memory units, filters by the configured `m_fMemoryLimit` and attack/flag predicates, counts matches, and returns whether the count reaches `m_uiHitsCount`.
- `UAIFightingComponent::TickComponent` passes TickComponent DeltaTime into `AIMainMemory::UpdateMemory`. That routine increments each unit’s float at `+0x18` by DeltaTime and prunes units when the manager lifetime is reached. `RunTest` skips a unit if configured `m_fMemoryLimit` is less than this accumulated age. This is accumulated per-tick age, not timestamp subtraction. Unreal `TickComponent` DeltaTime is seconds, so authored limits 2/3/5/10 are second-scale memory windows.
- `UAIFightingComponent::UpdateMemoryUnitForTargetDodgeOrAvoidSuccess` updates memory type `2`, separately from received-attack memory type `3`.

Thus AttackMemoryInfluenceTest consumes the same type of memory that UpdateAttackReceivedMemory records. The entries expose attack history to the contextual defense graph. The compiled path treats `m_HitTypes` as a mask/selector. Its symbolic labels are still unresolved; do not confuse these values with `EHitType` (the separate impact-source enum in the parent’s state-type inventory), and leave masks numeric.

`UAIInfluence_TestSequence::RunTests` evaluates its `m_Tests` in order and fails the sequence if any test result, after applying that test’s `m_bInverted`, fails. `TestNodeForContextualDefense` only traverses a sequence’s linked nodes after `RunTests` succeeds. The top-level graph also has probability and traversal selection, so a listed linked node is an eligible edge after its sequence passes, not a guaranteed defense outcome.

Examples from the extracted Grunt graphs. Omitted inversion fields remain absent in the serialized record; the native base-test default has since been mapped to false in recovery-system-chain.md. Explicit asset overrides still apply.

| Source asset / sequence | Test order and authored settings | Linked edge if the sequence passes | What the evidence establishes |
|---|---|---|---|
| `Grunt_Base_ContextualDefense`, sequence 5 (node index 34) | `AttackMemoryInfluenceTest_0` only: `Attack.Specific.BackFrontPush`, 3s, 1 hit, mask 2, `m_bInverted` omitted; native base-test default false confirmed in recovery-system-chain.md | `DefenseInfluenceNodeParryDeflect_3` | A recent matching BackFrontPush record is sufficient for this sequence; other graph candidates may still win |
| `Grunt_Adv_ContextualDefense`, sequence 9 (index 34) | `AttackMemoryInfluenceTest_10` only: BackFrontPush, 3s, 1 hit, mask 2, `m_bInverted` omitted; native base-test default false confirmed in recovery-system-chain.md | `DefenseInfluenceNodeParryDeflect_3` | Inner gate matches Base at 3s/mask2; both also have an outer 10s/mask3 gate, see parry-ai-followup.md |
| `Grunt_Base_ContextualDefense`, sequence 19 (index 18) | `AttackMemoryInfluenceTest_13` then `AttackPropertiesInfluenceTest_13`: `Attack.Type.Hit`, 5s, 5 hits, mask 1, `m_bInverted` omitted; native base-test default false confirmed in recovery-system-chain.md | `DefenseInfluenceNodeDodge_4` | Both tests must pass before this sequence can yield the dodge edge |
| `Grunt_Adv_ContextualDefense`, sequence 14 (index 57) | `AttackMemoryInfluenceTest_12` then `AttackPropertiesInfluenceTest_12`: `Attack.Specific.HoldDizzy`, 5s, 1 hit, mask 7, `m_bDodged=true`, `m_bInverted` omitted; native base-test default false confirmed in recovery-system-chain.md | `DefenseInfluenceNodeGuard_0` | Both tests must pass before this guard edge is eligible |
| `Grunt_Base_ContextualDefense`, sequence 16 (index 14) | `BP_IsOrderRunning_InfluenceTest_C_2` then `AttackMemoryInfluenceTest_1`: BackFrontKD, 5s, 1 hit, mask 1, `m_bInverted=true` | `DefenseInfluenceNodeInvalid_4` | This is an inverted memory gate to an invalid node, not evidence of a defensive counter branch |

These examples support an authored adaptation mechanism: recent attack patterns can influence whether a Grunt graph selects guard, parry/deflect, dodge, or avoid behavior. They do not prove every repeated move causes a specific counter, because all other tests, probability, traversal, and competing candidates remain relevant. Base and advanced Grunt graphs differ in authored windows and tests.
## Guard/parry application and recovery timing

`UDefenseInfluenceNodeGuard::Apply` (RVA `0x1879cf0`) first invokes the base contextual node Apply. On success it calls `AFightingCharacter::HandleGuard` with `EGuardType::Guard=1` and order-type byte `4`. `UDefenseInfluenceNodeParryDeflect::Apply` (RVA `0x1879d80`) uses `HandleGuard` with `EGuardType::Deflect=2` in its first branch, then `EGuardType::None=0` in a later branch. These enum names/values are confirmed by the parent matched-PDB enum extract.

The node callbacks provide direct cleanup evidence:

- `UDefenseInfluenceNodeGuard::OnIsStunFinished` constructs the FName `Stun finished` and tail-calls `FAIDefenseHandler::OnDefenseFinished`.
- `UDefenseInfluenceNodeGuard::OnTargetAttackEnded` similarly reports `Target Attack Ended` to `OnDefenseFinished`.
- `OnDefenseFinished` clears the current defense actions/Blackboard value, informs the current target handler, cancels/re-schedules conditioned actions, and releases its temporary action data.
- `UDefenseInfluenceNodeParryDeflect::OnTargetAttackEnded` checks `UHitComponent::IsStun`. When the AI owner is still stunned, that path skips the ordinary cancellation block; otherwise it scans active contextual-defense records for the parry/deflect kind and cancels the current tactic if none remains. The owner attribution comes from loading `[UAIFightingComponent+0xB0]`, validating it as `AFightingCharacter`, and calling `IsStun` on its `UHitComponent` at `+0x1328`; the same owner-pointer pattern appears in `UAIFightingComponent::OnIsStunChanged`.

This shows defense tactics are event-driven around stun completion and target attack end, rather than guarded by a single fixed recovery delay. It also shows a parry/deflect response may be preserved while the AI owner remains stunned. The guard callback’s `Stun finished` event is the code-level point at which that node reports completion; the subsequent time at which another defense request is selected depends on the next update and current prediction/context.

`FAIDefenseHandler::OnOrderFightingStateTimeLeftReachedZero` (RVA `0x18bd1a0`) additionally gates recovery actions on registered AI actions and `IsDefending`, obtains the impact-type-specific `FPropertyReaction` from the resistance DB, and schedules its conditioned actions. If any conditioned action schedules successfully, the callback sets the associated `OrderPlayAnim` time-left to 0.5 seconds and writes `false` through the callback bool reference, vetoing the current zero-time expiration. If no action schedules, this callback does not veto expiration. This is a conditional recovery-action path; parent’s state-lifecycle report documents how fighting-state lifetime and accumulation end.

## Stun-triggered combo interruption

`UAIFightingComponent::OnIsStunChanged` checks `IsStun` on the AI owner’s `UHitComponent`, then forwards the result to `FAIAttackHandler::OnIsStunChanged`. The handler returns immediately when the bool is false. When true, it reads a Blackboard enum and only when that value is nonzero does it call `EndCombo` with reason byte `0x0A`. The parent’s matched-PDB enum extract identifies `EComboEndReason::IsStun=10`. This is evidence for a conditional stun-triggered combo end; it does not show that every stun ends every combo.

The native `InternalConstructor<UAttackMemoryInfluenceTest>` zeros byte `[object+0x48]`, but this branch did not independently map that byte to `m_bInverted` through a class layout, so omitted serialized inversion flags remain unresolved here.

## Guard and parry graph actions

The extracted Grunt assets include `DefenseInfluenceNodeParryDeflect` entries with `m_bLaunchDefaultActions=false` and an `m_ActionsOnSuccess` entry referencing `BP_AiLaunchCounterCombo_Parry`. Some entries also raise `AI.Grunt.FirstParry`. This means those authored nodes replace the default follow-up with a parry counter-combo action under their success path. It does not establish the timing/eligibility of the Blueprint action beyond its serialized attachment; the Blueprint body was not statically traced in this branch.

`DefenseInfluenceNodeGuard` entries in the base and advanced assets primarily carry their node index, with guard request implementation in C++. They are selected through the contextual graph rather than continuously blocking every incoming attack.

## Caveats

- This is one locally installed Sifu build and its matching PDB. Other releases may differ.
- `m_HitTypes` values remain numeric because their symbolic mask labels are unresolved; do not substitute the separate `EHitType` names for them.
- The memory test reads recent received-attack entries and combines multiple predicates. A matching attack-memory test alone is not proof that the linked node always wins graph selection.
- `OnDefenseFinished` calls and graph links establish event flow; they do not prove the exact next-frame scheduling or every AI archetype’s behavior.
- Disassembly output can include compiler padding or embedded data within PDB symbol ranges. The helper records this limitation and verifies the executable hash before producing each batch.



## 2026-10-28 综合研究接续

最新证据和先前归属／默认值修正见 `notes/parry-system-chain.md`、`notes/avoid-system-chain.md`、`notes/recovery-system-chain.md`；用户阅读入口为知识库综合系统篇。未闭合处以新底稿的具体缺口为准。
