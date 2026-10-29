# Sifu matched-PDB type layout findings

## Scope and method

This is a static CodeView TPI read of the locally matched Sifu PDB. The PDB GUID/Age matches the game executable (verified by the parent task); the TPI stream is 317,909,600 bytes with type indices `0x1000..0x430207`. `scripts/inspect_types.py` reuses the existing `scripts/index_pdb.py` `Msf` reader and emits `inventory/focused_type_layouts.json`. It reads type records only; it does not run the game, modify game files, or infer runtime behavior from a field name.

The JSON records member byte offsets and UDT sizes. For array members it deliberately keeps `byte_length`, `element_size_bytes`, and `element_count` distinct. Forward declarations are resolved to complete same-name UDT sizes where available. The compiler layout says `m_Cooldowns` is 32 bytes of 8-byte `FTimerAndOffset` = 4 elements; `m_iCountPerDifficulty` is 12 bytes of 4-byte integers = 3; and `m_CooldownsPerDifficulty` is 96 bytes of 32-byte `FAITicketCooldowns` = 3. `FAITicketCooldowns` itself contains 32 bytes of `FTimerAndOffset` = 4 elements. This agrees with the parent task’s local serialized-asset inspection: 4 cooldown slots, with 3 difficulty entries each containing 4 slots. The TPI does not reveal the semantic labels for the four slots or names for the three difficulty tiers; leave those indices unmapped.

## Verified state-to-Joker binding

TPI enum values:

- `EFightingState::KnockedDown = 3` (`EFightingState` also contains OutOfFight=0, InFight=1, Counter_Hit=2, Dizzy=4, Pushed=5, Avoided=6, StructureBroken=7, Parried=8, Count=9, None=10).
- `EAIAttackTicketJokerSituation::TargetKnockedDown = 11` and `TargetGettingUp = 12` (`TargetDizzy=14`, `Count=17`, `None=18`; other values are in the JSON).

The parent’s static disassembly at `logs/OnDefenderFightingStateChanged.asm.txt` gives direct code evidence for the relationship: it compares the state byte to 3, chooses Joker situation 11 or 12 based on the `r8b` boolean, clears `r8d`, then tail-jumps to `ActivateJokerSituation`. Taken together with the enum definitions, this verifies the callback maps the KnockedDown state to TargetKnockedDown or TargetGettingUp (selector details are the callback’s boolean argument). This is behavior evidence from disassembly, unlike a mere declaration or enum co-occurrence.

## Group attack-ticket mechanism surface

`FAttackTicketConfig` is 288 bytes. Relevant members: `m_eBehavior` +0; always-available flag +1; combat role +2; combat-role mask +4; count +8; four `FTimerAndOffset` cooldowns +12; per-difficulty counters flag +44; three integer counts +48; three per-difficulty cooldown groups +60; synchronized-fire cooldown offset/tolerance +156/+160; forced cooldown after direct-opponent death +164; repeat flag and range +168/+172; min-distance toggle/value +188/+192; ineligible timer on release +196; “not used in combo” +197; move-to timeout +200; behavior against Joker +204; fallback ticket +208. The config’s field names expose likely tuning controls but do not alone prove how the engine applies them.

`FAIAttackTicketManager` (696 bytes) extends `FAITicketManagerT<...>` and has a defender weak pointer at +560, Joker-situation map at +568, callbacks for defender order/rush/death/fighting-state changes at +648..+680, direct-opponent-died flag +688 and `m_uiNbOfAttackingCandidates` byte +689. The latter is a candidate-count field; its name/position alone is not evidence of a hard simultaneous-attacker cap. Method declarations include `AddAttacker`, `RemoveAttacker`, `GetNumberOfAttackers`, `CreateAllAttackTickets`, `ReleaseAITickets`, `ReleaseAITicket`, `ResetTicketsCooldown`, `GetTicketCooldownRemaining`, passive-ticket checks/requests, and attacker/defender event callbacks.

`FAIAttackCandidate` (232 bytes) contains an attacker weak pointer (+88), delegates for combat-role, combo change/start/end, next attack, combo-asset change (+96..+136), `m_bIsAttacking` (+144), and a ticket blacklist timer map (+152). `FAIAttackTicket` (456 bytes) includes defender pointer +48, ticket enum +56, display name +136, config +144, minimum-distance squared +432, cooldown-paused and always-available flags +436/+437, and potential owners array +440. `UAIAttackTicketData` (344 bytes) embeds config at +48 and a serialize-version integer at +336. These declarations establish state/configuration surfaces, not scheduling policy or exact runtime attack concurrency.

`ESCAICombatRoles` is None=0, DirectOpponent=1, IndirectOpponent=2, NonOpponent=3, Num=4. The role names and manager declarations support investigation of opponent grouping; actual membership rules and attack admission require code/data cross-reference.

## Impact, structure, stun, and fighting-state layouts

`FAppliedHitImpact` (24 bytes): damage +0, structure damage +4, super-dizzy damage +8, stun frame count byte +12, use-knockback-distance bool +13, knockback distance +16, freeze frames +20.

`FImpactResult` (192 bytes) carries damage +4, guard-break/super-dizzy availability booleans +8..+10, applied hit impact +32, applied deflect impact +56, instigator structure before impact +96, elapsed hit-animation time during freeze +100, lethal +104, knockback position +108, impact location/direction +124/+136, instigator freeze duration +148, stun time +152, impact time +160, resilience impact +168, plus victim/impact classification, bone, sound/VFX and avoid-dizzy flags. `FHitOrderServiceImpactInfos` embeds that result at +0 and defense result at +192, with hit-success bool +208.

`FDeflectImpact` (72 bytes) derives from `FHitImpact`; it adds dynamic knockback curve +48, self-structure guard-break/use flags +56/+57, value +60, self-super-dizzy use flag +64 and value +68. `FAppliedDeflectImpact` (40 bytes) derives from `FAppliedHitImpact`; curve +24, self structure damage +32, self super-dizzy damage +36.

`FFightingStateElement` (144 bytes) has state duration/elapsed/infinite at +4/+8/+12; max and current accumulated damage +16/+20; max/current accumulated hits +24/+32; whether max hits group by attack +28; last attack name +36; fighting state +44, substate +45, handle +48, removal callback +64, special-resistance DB weak pointer +128. `FSuperDizzyReaction` contains mandatory duration +0, max accumulated damage +4 and max accumulated hits +8. `FDizzyReaction` inherits `FPropertyReaction`, then contains loop animation +208, mirrorable +232 and allow-on-top-of-dizzy +233. `FStructureBrokenReaction` inherits `FBaseFightingStateBehavior`, with duration +16, loop animation +24, mirrorable +48, guard coefficient restored at end +52 and guard restored +56. These fields show distinct damage/structure/dizzy/hit-count/state-reaction concepts and should not be collapsed into one “stun” parameter.

`FApplyImpactStruct` (1,648 bytes) embeds `FHitDescription` at +0, forced hit animation enable/data at +1440/+1448, play-order/ragdoll/drop-weapon flags +1552..+1555, resistance DB +1560, forced fighting-state animation flag/data +1569/+1576, structure-broken instant/forced-recovery flags +1600/+1601 and recovery animation +1608. The `FHitDescription` layout is available in the JSON and should be cross-referenced before interpreting a particular impact asset.

For attack timing, `FAttackDataRow` (120 bytes) derives from `FBaseAttackDataRow` (40 bytes). The base carries row name +8 and real attack name +16. Derived members include animation reference +40; mirror flags/method +80/+84; next-foot-marker threshold +88; start/end quadrants +92/+93; measured forward/right movement +96/+100; direct-right-follow flag +104; last buildup frame integer +108; hit frame float +112; strikeless flag +116. This confirms the serialized attack-table timing fields have a corresponding native row layout. It does not identify the meaning of `WantedBuildupFrames`, curves, or cancellation windows without their asset declarations and consumers.

## Conditional stun/combo-end path from parent disassembly

Parent static disassembly reports `UAIFightingComponent::OnIsStunChanged` calls `UHitComponent::IsStun` and forwards the boolean to `FAIAttackHandler::OnIsStunChanged`. In the latter, false returns; true reads a Blackboard enum and only if that enum is nonzero calls `EndCombo` with reason `0x0A`. I did not recover the `EComboEndReason` enumerator name for value 10, so leave it numeric. This supports a conditional stun-to-combo-end path, not a claim that every stun ends every combo. See parent outputs `logs/callback-UAIFightingComponent-OnIsStunChanged.asm.txt` and `logs/callback-FAIAttackHandler-OnIsStunChanged.asm.txt`.

## Limits and unresolved names

The requested spellings `FAttackDB`, `FAttackData`, `FHitBoxData`, `FHitReaction`, `FPlaybackRate`, and `FTimedImpact` were not found as selected TPI definitions. `UAttackDB` was present. A missing native declaration does not imply the cooked asset/property is absent; the parent’s tagged-object and DataTable extracts remain authoritative for serialized gameplay values.

`FHitImpact` is present (48 bytes), but its direct member list was not recovered by this reader; some generated/unknown CodeView field-list records stop parsing. Four generic ticket evaluator/filter types also stop at a zero/padding record (`leaf=0x0`) in their member lists. The script retains the stop location/prefix in JSON, and leaves already decoded fields intact. Treat missing trailing members as unresolved. Inherited members are represented by base subobjects and are not flattened into derived offsets.

No runtime behavior is claimed solely because a method, enum, field, or callback appears in TPI. For behavior claims, use the callback disassembly evidence and asset/serialization cross-reference. Cooldown slot names and difficulty tier labels remain unknown.
