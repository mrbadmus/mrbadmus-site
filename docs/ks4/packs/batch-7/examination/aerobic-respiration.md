# Examination — Aerobic Respiration (aerobic-respiration) — AQA 8464 4.4.2.1 / 8461 4.4.2.1
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.4.2.1-aerobic-respiration.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.4.2.1; 4.1.1.2 cell structures; 5.5.1.3 bond energies), `AQA-8461-spec.txt` (Biology v1.0, 4.4.2.1; 4.1.1.2). Route audit row `aerobic-respiration` (OK, CF CH TF TH). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; T1–T4 = theory blocks. Route copies: `higher` is null on CF and TF (served CH/TH only). No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired (key n explains opts[n]); no shift.**

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.4.2.1** | Aerobic and anaerobic respiration | base |
| 8461 | **4.4.2.1** | Aerobic and anaerobic respiration | base |
| Supporting | 8464/8461 4.1.1.2 (mitochondria, where aerobic respiration takes place) | | base |

Spec statements (verbatim, 8464 = 8461): "Students should be able to describe cellular respiration as an exothermic reaction which is continuously occurring in living cells. The energy transferred supplies all the energy needed for living processes." "Respiration in cells can take place aerobically (using oxygen) or anaerobically (without oxygen), to transfer energy." "Students should be able to compare the processes of aerobic and anaerobic respiration with regard to the need for oxygen, the differing products and the relative amounts of energy transferred." "Organisms need energy for: chemical reactions to build larger molecules; movement; keeping warm." "Aerobic respiration is represented by the equation: glucose + oxygen → carbon dioxide + water. Students should recognise the chemical symbols: C6H12O6, O2, CO2 and H2O." No HT statement; no biology-only statement.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Respiration in all living cells; continuous; ≠ breathing (T1; common_mistake) | base | 4.4.2.1 | all four | OK |
| R2 | ATP as energy currency; list of uses (T1) | off-spec (ATP); uses = base | 4.4.2.1 | all four | OFF-SPEC (F3), IMPRECISE (F4) |
| R3 | Word equation (T2; equations; key_note) | base | 4.4.2.1 | all four | OK |
| R4 | Symbol equation (T2; equations) | base — recognise symbols only | 4.4.2.1 | all four | OK (do not test writing it) |
| R5 | Mitochondria; high-demand cells have more (T3; q1; q3) | base | 4.1.1.2 | all four | OK |
| R6 | Aerobic transfers far more energy than anaerobic (T4; `higher`) | base | 4.4.2.1 | T4 all four; `higher` CH/TH | OK; `higher` mis-routed (F5); "all energy harvested" WRONG (F2) |
| R7 | Exothermic (key_note only) | base | 4.4.2.1 | all four | GAP — not in theory (F6) |
| R8 | quiz q1 (where), q2 (breathing vs respiration) | base | 4.1.1.2; 4.4.2.1 | all four | OK |
| R9 | quiz q3 (mitochondria in muscle) | base | 4.4.2.1 | all four | wx2 WRONG (F1) |
| — | RP, FIFA, examiner_tip | none | — | — | correct: 4.4.2.1 has no RP or calculation |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | all living cells release energy from glucose | OK | AQA wording "transfer energy"; "release" credited, "make/produce energy" is not. | 4.4.2.1 |
| C2 | T1 | "to produce ATP"; ATP the energy currency | OFF-SPEC | ATP is not in 8461 or 8464. Teach "energy transferred". | — |
| C3 | T1 | "ATENTION" | IMPRECISE | Typo (theory is re-cuttable). | — |
| C4 | T1 | ATP directly powers muscle contraction, active transport, protein synthesis, cell division, maintaining body temperature | IMPRECISE | Body temperature is kept up by energy transferred by heating during respiration, not "powered by ATP". Use the spec's three: building larger molecules, movement, keeping warm. | 4.4.2.1 |
| C5 | T1 | respiration ≠ breathing; continuous day and night | OK | — | 4.4.2.1 |
| C6 | T2 | glucose + oxygen → carbon dioxide + water | OK | Energy is not a product: keep "(energy transferred)" outside the equation. | 4.4.2.1 |
| C7 | T2; equations | C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O | OK | Balanced ✓ (C 6/6, H 12/12, O 18/18). Spec: recognise symbols only. | 4.4.2.1 |
| C8 | T2 | all carbon → CO₂; hydrogen + oxygen → water | OK | — | — |
| C9 | T2; T4; `higher`; key_note | "approximately 36–38 ATP" | OFF-SPEC / IMPRECISE | Off-spec; also an outdated theoretical maximum (current figure ~30–32). Teach "much more energy than anaerobic". | 4.4.2.1 |
| C10 | T3 | aerobic respiration in mitochondria | OK | — | 4.1.1.2 |
| C11 | T3 | cristae increase surface area | OK (off-spec) | True; not examinable. | — |
| C12 | T3 | muscle, liver, sperm, heart cells have many mitochondria | OK | — | 4.1.1.3 |
| C13 | T4 | ~2 ATP from anaerobic | OK (off-spec) | — | — |
| C14 | T4 | "All the chemical energy stored in the C–H bonds of glucose is harvested" | WRONG | Not all of it: much of the energy is transferred by heating (which is how respiration keeps us warm). "Energy stored in bonds" is the chemistry misconception — energy is transferred because bond making releases more than bond breaking takes in. Say "complete oxidation transfers much more energy". | 4.4.2.1; 8464 5.5.1.3 |
| C15 | T4 | without O₂ much energy stays in lactic acid/ethanol | OK | Matches "oxidation of glucose is incomplete". | 4.4.2.1 |
| C16 | T4 | we breathe to supply O₂ for respiration | OK | — | — |
| C17 | `higher` | ATP directly powers…; ~36–38 vs ~2; used for sustained activity | OFF-SPEC (ATP) / OK (relative energy) | No HT content — base, all routes (F5). | 4.4.2.1 |
| C18 | common_mistake | respiration ≠ breathing; mitochondria not nucleus/chloroplasts | OK | — | 4.4.2.1; 4.1.1.2 |
| C19 | key_note | equation; mitochondria; continuous; exothermic | OK | ATP number off-spec (C9). | 4.4.2.1 |
| C20 | matching (to be replaced) | six pairs | OK | "ATP … powers all cell processes" off-spec. | — |
| C21 | q1 key | mitochondria | OK | — | 4.1.1.2 |
| C22 | q1 wx1 | chloroplasts photosynthesise | OK | — | 4.1.1.2 |
| C23 | q1 wx2 | nucleus holds DNA, controls the cell | OK | — | 4.1.1.2 |
| C24 | q1 wx3 | ribosomes make proteins | OK | — | 4.1.1.2 |
| C25 | q2 key | breathing moves air; respiration is chemical, in cells | OK | — | 4.4.2.1 |
| C26 | q2 wx1 | not the same; mechanical vs chemical | OK | — | — |
| C27 | q2 wx2 | ATP from respiration; O₂ from photosynthesis | OK | ATP off-spec, harmless. | — |
| C28 | q2 wx3 | respiration in all living cells | OK | — | 4.4.2.1 |
| C29 | q3 key | muscle cells need more energy → more mitochondria "produce more ATP" | OK | "transfer more energy" preferred (ATP off-spec). | 4.4.2.1 |
| C30 | q3 wx1 | organelles don't sink | OK | — | — |
| C31 | q3 wx2 | "Skin cells are actually similar in size to muscle cells" | WRONG | False: a skeletal muscle cell (fibre) is many times larger than a skin cell (up to centimetres long). The correct rebuttal is that mitochondria number follows energy demand, not cell size. | — |
| C32 | q3 wx3 | driving factor is energy demand, not oxygen | OK | — | — |

Count: **2 WRONG** (C14 theory, re-cuttable; C31 frozen wx). OFF-SPEC: ATP throughout. IMPRECISE: C3, C4, C9.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q3 | wx2 states a false fact (F1) | **Do not use as written.** Key and options are sound; usable only with a replacement wx2 logged in DEPARTURES. |
| q1, q2 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE HAS ERRORS. Core science (equation, mitochondria, respiration ≠ breathing) is correct and base on every route. Two errors: q3 wx2 (frozen) and T4's "all the chemical energy … harvested" (theory). ATP and its numbers are off-spec throughout; the spec asks only for relative energy. The `higher` field holds no HT content but is withheld from CF/TF. "Exothermic" must be taught, not only key-noted. **For Mide:** nothing — all settled facts.
