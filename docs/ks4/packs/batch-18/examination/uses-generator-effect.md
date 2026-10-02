# Examination — Uses of the Generator Effect (uses-generator-effect) — AQA 8463 4.7.3.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-18/04-checked-science-source/physics-6.7.3.2-uses-generator-effect.md`.
Spec sources read as text: `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) §4.7.3, 4.7.3.1–4.7.3.2, 4.7.2.3; `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §6.7 (no generator content) and 6.2.3.1 (UK mains 50 Hz); both June 2026 equation sheets. Route audit `ks4-routes/docs/ks4/route-audit/physics.md` row 87.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n. One route copy (TH).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8463 | **4.7.3.2** | Uses of the generator effect | **(HT only)**, under 4.7.3 "(physics only) (HT only)" |
| 8464 | — | not in Combined | — |
| Supporting | 8463 4.7.3.1 (generator effect); 8464 6.2.3.1 / 8463 4.2.3.1 (ac/dc; UK mains 50 Hz, 230 V — base) | | |

Spec statements (verbatim, 8463 4.7.3.2): "The generator effect is used in an alternator to generate ac and in a dynamo to generate dc." "Students should be able to: • explain how the generator effect is used in an alternator to generate ac and in a dynamo to generate dc • draw/interpret graphs of potential difference generated in the coil against time."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Alternator: rotating coil, slip rings and brushes → ac (theory 1; common_mistake; key_note; `higher`; q1) | triple-higher | 4.7.3.2 | OK |
| R2 | Dynamo: split-ring commutator swaps connections each half-turn → dc (pulsing) (theory 2; common_mistake; q1) | triple-higher | 4.7.3.2 | OK |
| R3 | ac frequency = rotation frequency; UK mains 50 Hz (theory 1) | triple-higher (50 Hz itself base, 6.2.3.1) | 4.7.3.2; 8464 6.2.3.1 | OK (F3 imprecise) |
| R4 | pd–time graphs for alternator and dynamo | triple-higher | 4.7.3.2 | **GAP** — described in words only (F2) |
| R5 | Uses: power stations, cars, wind, bicycles (theory 1–3) | context | — | OK, bicycle example IMPRECISE (F4) |
| R6 | Rotating-magnet generators; gearboxes; hydro efficiency; capacitor smoothing (theory 2–3) | not in spec (context) | — | OFF-SPEC (F5) |
| R7 | Back-emf (theory 3; `higher`; key_note; matching; q2) | not in spec | — | OFF-SPEC (F1) |
| R8 | q1 | triple-higher | 4.7.3.2 | usable |
| R9 | q2 | not in spec | — | **not usable** (F1) |
| — | equations, FIFA, RP, examiner_tip | none | — | correct: none in 4.7.3.2 |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | alternator = ac generator; coil rotating in field; slip rings and brushes; slip rings rotate with coil so connections never reverse → ac | OK | — | 4.7.3.2 |
| C2 | theory 1 | sinusoidal output; frequency = rotation frequency | OK | — | 4.7.3.2 |
| C3 | theory 1 | "UK mains: 50 Hz — the alternator must rotate at 50 revolutions per second (or 3000 rpm)" | IMPRECISE | True for the simple one-coil (two-pole) generator the spec models; real multi-pole generators turn slower. 50 × 60 = 3000 ✓. Add "for this simple generator". | F3; 8464 6.2.3.1 |
| C4 | theory 1 | uses: power stations, car alternators charge battery, wind turbines | OK | — | — |
| C5 | theory 2 | dynamo uses a split-ring commutator; ring split in two halves; connections swap every half-rotation → current one way | OK | — | 4.7.3.2 |
| C6 | theory 2 | "Pulsing DC — voltage varies from 0 to maximum, never reverses" | OK | The pd–time graph: all-positive humps, zero twice per turn. | 4.7.3.2 |
| C7 | theory 2 | "usually smoothed with capacitors" | OFF-SPEC | Omit. | F5 |
| C8 | theory 2 | "Bicycle dynamos: wheel drives a small permanent magnet generator → powers lights" as a dc-dynamo use | IMPRECISE | Bicycle "dynamos" (bottle and hub types) are rotating-magnet machines with no commutator — they give ac. Do not use as the example of dc. | F4 |
| C9 | theory 2 | alternator: slip rings → ac; dynamo: commutator → pulsing dc; both rotating coil (or rotating magnet) | OK | — | 4.7.3.2 |
| C10 | theory 3 | rotating magnet inside fixed coil; no slip rings for the output | OK (context) | True; not required. | F5 |
| C11 | theory 3 | wind turbines, gearbox, direct-drive PM generators | OK (context) | — | F5 |
| C12 | theory 3 | hydro "Very efficient (~90%): gravitational PE → kinetic → electrical" | OK (context) | Stores wording: gravitational potential energy store → kinetic store → transferred electrically. | 8463 4.1.1.1 |
| C13 | theory 3 | fission/burning gas → steam → turbine → alternator; 50 Hz ac | OK | — | 8464 6.1.3 |
| C14 | theory 3 | back-emf: zero at start-up (high current), near supply at full speed (low current) | OFF-SPEC | True in outline; not in 8463. | F1 |
| C15 | `higher` | "Describe back-emf in electric motors" | OFF-SPEC | Drop that sentence. | F1 |
| C16 | common_mistake | alternator slip rings → ac; dynamo commutator → dc; type of connection decides; rotating magnet still induces | OK | — | 4.7.3.2 |
| C17 | key_note | as theory; back-emf | OK except back-emf (F1) | — | — |
| C18 | q1 key | alternator slip rings → no reversal → ac; dynamo commutator swaps each half-turn → pulsing dc | OK | Model answer. | 4.7.3.2 |
| C19 | q1 opt 1 / wx1 | magnet strength affects size, not ac/dc | OK | Aligned. | 4.7.3.1 |
| C20 | q1 opt 2 / wx2 | speed affects frequency and size, not ac/dc | OK | Aligned. | 4.7.3.1–4.7.3.2 |
| C21 | q1 opt 3 / wx3 | turns affect size, not ac/dc | OK | Aligned. | 4.7.3.1 |
| C22 | q2 (whole item) | "What is 'back-emf' in an electric motor…" | OFF-SPEC | Science broadly right; wx1–wx3 aligned with options 1–3; but the topic is outside 8463. **Do not use.** | F1 |
| C23 | matching (to be replaced) | four pairs incl. back-emf | OK / OFF-SPEC (back-emf pair) | — | — |

Count: **0 WRONG**; IMPRECISE: C3, C8; OFF-SPEC: C7, C14, C15, C22 (+ context C10–C11).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Off-spec (back-emf), not wrong | Do not use on TH. |
q1 usable on TH.

## 5. Gaps (spec core added to the source file)
The second spec bullet — draw/interpret pd–time graphs — is the most-examined part of 4.7.3.2 and has no graph in the frozen data. Added to the source file as "Spec core missing from the frozen data".

## 6. Verdict
SOURCE OK WITH FLAGS. Alternator/dynamo physics correct; one usable quiz item; the back-emf strand (theory, `higher`, q2) is off-spec; the pd–time graph skill is missing; the bicycle-dynamo example is the wrong way round for dc.

**For Mide:** nothing.
