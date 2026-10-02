# Examination — Electrical Charge and Current (electrical-charge-current) — AQA 8463 4.2.1.2 / 8464 6.2.1.2
Verdict: SOURCE HAS ERRORS (the frozen `rp` field describes a practical that is not an AQA required practical)
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-15/04-checked-science-source/physics-6.2.1.2-electrical-charge-current.md`.
Spec sources read as text: `AQA-8464-spec.txt` 6.2.1.2–6.2.2 (incl. RP15), 5.2.2.8; `AQA-8463-spec.txt` 4.2.1.2–4.2.1.4 (incl. RP3); both June 2026 equation sheets.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). One route copy.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.2.1.2** | Electrical charge and current | base |
| 8463 | **4.2.1.2** | Electrical charge and current | base |
| Supporting | 8464 6.2.2 / 8463 4.2.2 (series and parallel; current in parallel); 8464 5.2.2.8 (delocalised electrons carry charge in metals) | | base |

Spec statements (verbatim, 8463 = 8464): "For electrical charge to flow through a closed circuit the circuit must include a source of potential difference. Electric current is a flow of electrical charge. The size of the electric current is the rate of flow of electrical charge. Charge flow, current and time are linked by the equation: charge flow = current × time Q = I t" — "Students should be able to recall and apply this equation." Units: C, A ("amp is acceptable for ampere"), s. "A current has the same value at any point in a single closed loop."

Sheet status: Q = I t is printed on both June 2026 sheets (8464 and 8463), so it is labelled "On the sheet". The spec lists it for recall, so "Write down the equation" questions still apply.

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Closed circuit + source of pd (theory 1) | base | 6.2.1.2 | OK |
| R2 | Current = rate of flow of charge; 1 A = 1 C/s (theory 1; key_note) | base | 6.2.1.2 | OK |
| R3 | Electrons in metals (theory 1) | base (supporting) | 5.2.2.8 | OK |
| R4 | Ions in electrolytes; conventional vs electron flow; 6.24 × 10¹⁸ (theory 1–2) | — | — | OFF-SPEC, harmless (C3, C4, C9) |
| R5 | Q = It; rearrangements; Examples 1–2; min → s (theory 2; equations; variables; FIFA; common_mistake) | base | 6.2.1.2 | OK |
| R6 | Same current anywhere in a single loop (theory 3; common_mistake; q2) | base | 6.2.1.2 | OK |
| R7 | Parallel: current splits, sum; lower-R branch carries more (theory 3; key_note) | base | 6.2.2 | OK — sibling lesson's content (series-parallel-circuits) |
| R8 | `rp` | not an AQA RP | — | **WRONG** (C17) |
| R9 | q1 Q = It with minutes | base | 6.2.1.2 | OK, one imprecise distractor — usable all routes |
| R10 | q2 series ammeter readings | base | 6.2.1.2 | OK — usable all routes |
| — | `higher` | none | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | current = flow of charge; closed circuit and a source of pd needed | OK | Spec wording. | 6.2.1.2 |
| C2 | theory 1 | A; 1 A = 1 C per second | OK | — | 6.2.1.2 |
| C3 | theory 1 | metals: free electrons; electrolytes: ions | OK / OFF-SPEC | Electrons: OK (5.2.2.8). Ions in electrolytes: true, but not in this physics spec section. Optional. | 5.2.2.8 |
| C4 | theory 1 | conventional current + → −; electron flow − → +; convention predates electrons | OFF-SPEC | True, but AQA GCSE does not examine conventional vs electron flow. Optional; leave it out of practice. | — |
| C5 | theory 2 | Q = I × t; C, A, s; I = Q ÷ t; t = Q ÷ I | OK | — | 6.2.1.2 |
| C6 | theory 2 Ex 1 | 2 A × 30 s = 60 C | OK | ✓ (nothing to convert, so this is CFIFA's first worked example) | — |
| C7 | theory 2 Ex 2 | 120 C in 4 min: t = 240 s; I = 0.5 A | OK | ✓ | — |
| C9 | theory 2 | 1 C ≈ 6.24 × 10¹⁸ electrons | OFF-SPEC | Correct (1/1.602 × 10⁻¹⁹), but not on the spec. | — |
| C10 | theory 3 | series: same current everywhere | OK | — | 6.2.1.2; 6.2.2 |
| C11 | theory 3 | parallel: splits; I_total = sum; lower-resistance branch carries more | OK | 6.2.2 content. | 6.2.2 |
| C12 | theory 3 | ammeter in series; very low resistance | OK | — | — |
| C13 | common_mistake | seconds; × 60; current not used up in series | OK | — | 6.2.1.2 |
| C14 | key_note | summary | OK | Conventional/electron flow as C4. | — |
| C15 | FIFA | 0.4 A × 300 s = 120 C | OK | ✓ | — |
| C16 | FIFA Convert `[NEW]` | "minutes → seconds: t = 5 min = 5 × 60 = 300 s (I is already in A, needs no conversion)." | OK | Marked `[NEW — examined ✓]`. The frozen Insert step repeats "5 × 60 = 300 s"; harmless. | CFIFA amendment |
| C17 | rp | "RP15 (Physics) — Set up series and parallel circuits; measure current with ammeters at different positions to verify series current is constant and parallel currents sum to total." | **WRONG** | Not an AQA required practical. 8464 RP15 = 8463 RP3 is "investigate the factors affecting the resistance of electrical circuits… the length of a wire at constant temperature; combinations of resistors in series and parallel", at 6.2.1.3 / 4.2.1.3. The described activity is a good class demo, but it must not carry an RP badge. | 8464 6.2.1.3 / 8463 4.2.1.3 |
| C18 | variables | Q, I, t | OK | — | — |
| C19 | q1 key | 180 C in 2 min: I = 180 ÷ 120 = 1.5 A | OK | ✓ | — |
| C20 | q1 opt 1 / wx1 | 90 A — minutes used | OK, aligned | ✓ | — |
| C21 | q1 opt 2 / wx2 | 360 A — multiplied | OK, aligned | ✓ | — |
| C22 | q1 opt 3 / wx3 | "0.013 A — I = 180 ÷ 14400 (used hours)" / "2 minutes = 120 s (not 14400)" | IMPRECISE | Arithmetic ✓ (0.0125). But 14,400 is not "hours": 2 min = 1/30 h would give 5400 A. The option's stated reason is false, and wx3 does not explain where 14,400 comes from. Still a wrong option, with a correct key, so harmless to the answer. Usable. | — |
| C23 | q2 key | 0.3 A — same everywhere in series | OK | Spec sentence verbatim in spirit. | 6.2.1.2 |
| C24 | q2 opt 1 / wx1 | current not used up; energy is transferred | OK, aligned | — | — |
| C25 | q2 opt 2 / wx2 | cannot increase without a junction | OK, aligned | — | — |
| C26 | q2 opt 3 / wx3 | same at all points regardless of resistances | OK, aligned | — | — |
| C27 | matching (to be replaced) | 60 C = 3 × 20; 0.5 A = 90 ÷ 180 | OK | ✓ | — |

Count: **1 WRONG** (C17, frozen `rp`). **OFF-SPEC**: C3 (ions), C4, C9. **IMPRECISE**: C22.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `rp` | describes a non-AQA practical as RP15 | **Do not use as written.** No RP badge or block on this lesson. |
| q1 | key correct; option 4's "(used hours)" label is false | Usable on all routes (F2). |
| q2 | correct | Usable on all routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: time left in minutes; "current is used up by each lamp"; current confused with charge or energy; mA not converted to A; "amps" written as "amperes per second".

**Typical questions** ⚑ examiner-drafted
- *Write down the equation that links charge flow, current and time. [1]* — Q = I t.
- *A phone charger supplies a current of 1.2 A for 45 minutes. Calculate the charge that flows. [3]* — t = 2700 s (1); Q = 1.2 × 2700 (1); = 3240 C (1).

## 6. Verdict
SOURCE HAS ERRORS. The frozen `rp` names a practical AQA does not set. All 7 calculations check. Both quiz items are usable on all routes (q1 has a mislabelled distractor). The Convert line is examined ✓. Three off-spec asides are harmless and optional.

**For Mide:** nothing.
