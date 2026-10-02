# Examination — Electric Motors (electric-motors) — AQA 8464 6.7.2.3 / 8463 4.7.2.3 (HT only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.2.3-electric-motors.md`.
Spec sources read: `AQA-8464-spec.txt` 6.7.2.2–6.7.2.3; `AQA-8463-spec.txt` 4.7.2.2–4.7.3.2; route audit `physics.md` row `electric-motors` (CH TH, CH TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. No route copies differ; no `higher` field (the whole lesson is HT).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.7.2.3** | Electric motors | HT only |
| 8463 | **4.7.2.3** | Electric motors | HT only |
| Supporting | 8464 6.7.2.2 (motor effect, F = BIl, LHR) | | HT only |
| Related (not this lesson) | 8463 4.7.3.1 Induced potential; 4.7.3.2 Uses of the generator effect | | physics only, HT only |

Spec statements (verbatim, 8463 = 8464): "A coil of wire carrying a current in a magnetic field tends to rotate. This is the basis of an electric motor. Students should be able to explain how the force on a conductor in a magnetic field causes the rotation of the coil in an electric motor."

Note: the spec does not name the split-ring commutator in 6.7.2.3. It is the standard explanation of why the coil keeps turning one way, appears in 8463 4.7.3.2 (the dynamo), and is safe to teach at CH TH; it is not required for the spec's explanation, which is the force pair on the two sides.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Coil, magnet, commutator, brushes (theory 1; matching) | higher | 6.7.2.3 | OK |
| R2 | Forces on opposite sides in opposite directions → turning effect → rotation (theory 1) | higher | 6.7.2.3 | OK — the spec's core point |
| R3 | Commutator reverses current each half turn → continuous rotation (theory 1; common_mistake; key_note) | higher | 6.7.2.3 | OK |
| R4 | Energy: electrical → kinetic (theory 1) | higher (context) | 6.1 | IMPRECISE (F3) |
| R5 | Faster/more turning effect: current, B, turns (theory 2) | higher | 6.7.2.2–6.7.2.3 | OK |
| R6 | Iron core, armature (theory 2) | not in spec | — | OK |
| R7 | Applications, efficiencies (theory 3) | not in spec | — | OK |
| R8 | Regenerative braking (theory 3; key_note; q2) | triple-higher | 8463 4.7.3.1–4.7.3.2 | ROUTE (F2) |
| R9 | "commutator is unique to DC motors" (common_mistake) | not in spec | — | IMPRECISE (F4) |
| R10 | q1 (why a split-ring commutator) | higher | 6.7.2.3 | wx2 WRONG (F1) — do not use as written |
| R11 | q2 (regenerative braking energy transfer) | triple-higher | 8463 4.7.3.1 | TH only; wx2 misaligned (F2) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "converts electrical energy into kinetic energy (rotation)" | IMPRECISE | AQA language: energy is transferred electrically to the kinetic store of the coil (some dissipated as thermal). (F3) | 6.1.1.1 |
| C2 | theory 1 | components: rectangular coil, split-ring commutator, carbon brushes | OK | — | 6.7.2.3 |
| C3 | theory 1 | steps 1–4: current → force on each side (F = BIl) → opposite directions → turning force → rotates | OK | The spec's explanation. | 6.7.2.2–6.7.2.3 |
| C4 | theory 1 | without commutator, at vertical the forces lie in the coil's plane → no turning effect → coil oscillates | OK | At vertical the forces still act but pass through the axis, so no turning effect; the coil overshoots, is pushed back and rocks. "No more torque" is fine. | — |
| C5 | theory 1 | commutator swaps current every half turn → same rotation direction | OK | — | 6.7.2.3 |
| C6 | theory 2 | more current, stronger field, more turns → more turning force, faster | OK | Follows from the factors in 6.7.2.2. | 6.7.2.2 |
| C7 | theory 2 | iron core concentrates the field; real motors use an armature, many coils | OK | Enrichment. | — |
| C8 | theory 3 | applications list; EV zero direct emissions | OK | Context. | — |
| C9 | theory 3 | electric motors >90 % efficient vs ~25–35 % petrol | OK | Order of magnitude right; context. | — |
| C10 | theory 3 | regenerative braking: motor acts as generator; "recovers KE back to electrical store"; "KE → electrical energy → stored in battery" | ROUTE + IMPRECISE | Generator effect = 8463 4.7.3.1 (physics only)(HT only) — not on CH. "Electrical store" is not a store: kinetic store → transferred electrically → chemical store of the battery. (F2, F3) | 8463 4.7.3.1 |
| C11 | common_mistake | commutator → continuous rotation; without it the coil rocks | OK | — | 6.7.2.3 |
| C12 | common_mistake | "The commutator is unique to DC motors — AC motors use a different mechanism." | IMPRECISE | Universal (AC/DC) motors in drills and vacuum cleaners also use commutators. Off-spec; cut. (F4) | — |
| C13 | key_note | as theory; "Regenerative braking: motor acts as generator" | ROUTE | As C10. | 8463 4.7.3.1 |
| C14 | q1 key | reverses current every half turn → forces always rotate the coil the same way | OK | — | 6.7.2.3 |
| C15 | q1 opt 1 / wx1 | increases field / doesn't affect field strength | OK | Aligned. | — |
| C16 | q1 opt 2 / wx2 | "converts AC to DC" / "A commutator converts DC to pulsed DC in the coil — it's not an AC-to-DC converter (that's a rectifier)" | WRONG | In a motor the commutator reverses the current in the coil every half turn, so the current in the coil ALTERNATES — it is not "pulsed DC". (Pulsed DC is what a dynamo's commutator gives out — the reverse device.) wx2 contradicts the key. (F1) | 6.7.2.3; 8463 4.7.3.2 |
| C17 | q1 opt 3 / wx3 | "connects the motor to the power supply — without it no current would flow" / brushes connect, commutator reverses | IMPRECISE | The option is partly true: current does reach the coil through the commutator. It is a weak distractor, not a false statement. (F1) | — |
| C18 | q2 key | KE → electrical; motor runs as a generator, charging the battery | OK science, ROUTE | TH only. (F2) | 8463 4.7.3.1 |
| C19 | q2 opt 1 / wx1 | electrical → kinetic / regenerative braking takes energy from the motion | OK | Aligned. | — |
| C20 | q2 opt 2 / wx2 | "Chemical energy → thermal energy" / "Conventional friction brakes do convert KE to thermal…" | IMPRECISE | wx2 never says why "chemical" is wrong; it answers option 3's idea. (F2) | — |
| C21 | q2 opt 3 / wx3 | KE → thermal by friction / both happen, regenerative = electrical recovery | OK | Aligned. | — |
| C22 | matching (to be replaced) | coil, magnet, commutator, brushes | OK | — | 6.7.2.3 |

Count: **1 WRONG** (C16, q1 wx2); ROUTE: C10, C13, C18 (regenerative braking); IMPRECISE: C1, C10, C12, C17, C20.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 wrong; option 3 partly true (F1) | Do not use as written on CH or TH. |
| q2 | Generator effect = physics-only HT (F2); wx2 misaligned | Not on CH. Usable on TH only (wx2 does not rebut its option — Design's feedback must). |

## 5. For the lesson author
**Misconceptions seen in AQA marking:** "the commutator makes the current" or "changes AC to DC"; "both sides of the coil are pushed the same way"; "the coil stops at vertical because the force disappears"; "the brushes turn with the coil"; forgetting that reversing BOTH current and field leaves the direction unchanged.
**Command words:** Explain how the force on a conductor causes the coil to rotate; Give two ways to make the motor spin faster; Explain why the coil keeps rotating in the same direction.
**Required practical:** none.
**Equations:** none new (F = BIl is the previous lesson's; On the sheet, HT).

## 6. Verdict
SOURCE HAS ERRORS. Core motor explanation correct. q1's wx2 is wrong ("pulsed DC in the coil" — it alternates) — do not use as written. Regenerative braking is the generator effect, physics-only HT: TH layer at most, never CH; q2 therefore TH only. **For Mide:** nothing.
