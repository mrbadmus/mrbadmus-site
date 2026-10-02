# Examination — Work Done and Energy Transfer (work-done-energy-transfer) — AQA 8464 6.5.2 / 8463 4.5.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.5.2-work-done-energy-transfer.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 6.5.2, 6.5.1.3, 6.1.1.2, 6.1.1.4; `AQA-8463-spec.txt` (v1.1, 30 Sep 2019) 4.5.2 (identical wording). Equation sheets read: `8464-equation-sheet.txt` and `8463-equation-sheet-Jun26.txt` (both June 2026) — both print W = Fs, W = mg, Ep = mgh, P = W/t. Route audit read: `ks4-routes/docs/ks4/route-audit/physics.md` row `work-done-energy-transfer`.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. All four route copies identical (no `higher`).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.5.2** | Work done and energy transfer | base |
| 8463 | **4.5.2** | Work done and energy transfer | base |
| Supporting | 8464 6.5.1.3 / 8463 4.5.1.3 W = mg; 6.1.1.2 / 4.1.1.2 Ep = mgh; 6.1.1.4 / 4.1.1.4 P = W/t | | base |

Spec statements (verbatim, 8464 = 8463):
- "When a force causes an object to move through a distance work is done on the object. So a force does work on an object when the force causes a displacement of the object."
- "work done = force × distance moved along the line of action of the force  W = F s" — "Students should be able to recall and apply this equation." W in J, F in N, s in metres.
- "One joule of work is done when a force of one newton causes a displacement of one metre. 1 joule = 1 newton-metre"
- "Students should be able to describe the energy transfer involved when work is done."
- "Students should be able to convert between newton-metres and joules."
- "Work done against the frictional forces acting on an object causes a rise in the temperature of the object."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Force moves object through distance → work done; work = energy transfer (th1, th2; key_note) | base | 6.5.2 | all four | OK |
| R2 | W = Fs; units J, N, m; distance along line of action (th1; equations; variables; FIFA) | base | 6.5.2 | all four | OK |
| R3 | 1 J = 1 N m (th1, th3; key_note) | base | 6.5.2 | all four | OK |
| R4 | Force ⟂ motion → no work by that force (th1; common_mistake; q1) | base | 6.5.2 ("line of action") | all four | OK |
| R5 | Energy transfers by work: friction, lifting, spring, braking (th2) | base | 6.5.2; 6.5.3; 6.1.1.1 | all four | OK, one IMPRECISE (C6) |
| R6 | Rearranging s = W/F (th2 Ex 2; q2) | base | 6.5.2 | all four | OK |
| R7 | P = W/t = Fv (th2; key_note) | P = W/t base; P = Fv off-spec | 6.1.1.4 | all four | OFF-SPEC (F1) |
| R8 | Lifting: F = mg, W = mgh = Ep gained (th3) | base | 6.5.1.3; 6.5.2; 6.1.1.2 | all four | OK — chained calculation (rule 3) |
| R9 | Friction does "negative work" (th3) | off-spec wording | 6.5.2 | all four | IMPRECISE (F2) |
| R10 | Holding a weight still does no work (common_mistake) | base | 6.5.2 | all four | OK |
| — | `higher`, rp | none | — | — | correct: 6.5.2 has no HT or physics-only content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | force moves object through distance → work done | OK | — | 6.5.2 |
| C2 | th1 | work transfers energy between stores | OK | — | 6.5.2; 6.1.1.1 |
| C3 | th1 | W = F × s; s along line of action; 1 J = 1 N·m | OK | — | 6.5.2 |
| C4 | th1 | force ⟂ motion → no work; carrying a bag horizontally, weight does no work | OK | — | 6.5.2 |
| C5 | th2 | work done = energy transferred | OK | — | 6.5.2 |
| C6 | th2 | "Pushing a box… work done against friction → kinetic energy of box + thermal energy" | IMPRECISE | Work done against friction → thermal energy (temperature rise). Only any extra work beyond that goes to the kinetic store. At steady speed, none goes to kinetic. | 6.5.2 |
| C7 | th2 | lifting → GPE; compressing spring → elastic PE; braking → KE → thermal | OK | — | 6.1.1.1; 6.5.3 |
| C8 | th2 Ex 1 | 500 N × 4 m = 2000 J | OK | ✓ | — |
| C9 | th2 Ex 2 | s = 1000 ÷ 200 = 5 m | OK | ✓ | — |
| C10 | th2 | "P = W ÷ t = F × s ÷ t = F × v" | OFF-SPEC | P = Fv is not in 8464 or 8463 and not on either sheet. Algebra correct. | 6.1.1.4 |
| C11 | th3 | 1 J = 1 N × 1 m; why work and energy share units | OK | — | 6.5.2 |
| C12 | th3 | "W = F × h (where F = weight = mg…) Combined with W = mg: W = mgh" | IMPRECISE | Two different W's (work, weight) in one line. Write "weight = mg, so work done = mg × h". | 6.5.1.3; 6.5.2 |
| C13 | th3 | 5 kg lifted 2 m: weight 49 N; W = 98 J = Ep = 5 × 9.8 × 2 | OK | ✓ (g = 9.8 N/kg; spec: g is always given) | 6.1.1.2 |
| C14 | th3 | friction "always does NEGATIVE work" | IMPRECISE | Sign of work is not GCSE. Spec: "Work done against the frictional forces acting on an object causes a rise in the temperature of the object." | 6.5.2 |
| C15 | th3 | machines with friction need continuous energy input | OK | — | — |
| C16 | common_mistake | holding still → no work; W is work not weight | OK | — | 6.5.2 |
| C17 | key_note | "P = Fv" | OFF-SPEC | drop | — |
| C18 | key_note | rest | OK | — | — |
| C19 | FIFA | 300 N × 6 m = 1800 J | OK | ✓ | 6.5.2 |
| C20 | FIFA Convert `[NEW]` | "Nothing to convert — force is already in newtons and distance is already in metres (SI)." | OK | ✓. Second CFIFA example needs a real conversion (cm → m or kN → N); no frozen example has one. | CFIFA amendment |
| C21 | q1 key | 0 J: gravity ⟂ horizontal motion | OK | — | 6.5.2 |
| C22 | q1 opt 2 / wx1 | 1960 J = 20 × 9.8 × 10 | OK aligned | ✓ | — |
| C23 | q1 opt 3 / wx2 | 2000 J (g = 10); "Same error" | OK aligned | ✓ | — |
| C24 | q1 opt 4 / wx3 | 196 J = mg; forgot distance | OK aligned | ✓ | — |
| C25 | q2 key | 3200 ÷ 400 = 8 m | OK | ✓ | — |
| C26 | q2 opt 2 / wx1 | 3200 × 400 = 1,280,000 | OK aligned | ✓ | — |
| C27 | q2 opt 3 / wx2 | 400 ÷ 3200 = 0.125 | OK aligned | ✓ | — |
| C28 | q2 opt 4 / wx3 | 3200 + 400 = 3600 | OK aligned | ✓ | — |
| C29 | matching (to be replaced) | 2000 J, 98 J, 0 J, 5 m | OK | ✓ | — |
| C30 | spec point not in source | "convert between newton-metres and joules"; "rise in the temperature of the object" | GAP (minor) | th1/th3 state 1 J = 1 N m but do not practise the conversion; the temperature-rise wording is absent (F3) | 6.5.2 |

Count: **0 WRONG**; OFF-SPEC 1 (P = Fv); IMPRECISE 3 (C6, C12, C14); GAP 1 (C30). wrong_explanations: all 6 read and aligned. All 11 arithmetic results rechecked ✓.

## 4. Frozen items wrong for their route
None. q1 and q2 base, usable on all four routes.

## 5. Calculations (rule 3)
- W = Fs and its rearrangements (F = W/s, s = W/F). Not chained. Convert: cm → m, km → m, kN → N, kJ → J. Base.
- Lifting: **chained** — Step 1 weight W = mg; Step 2 work done = weight × height (= Ep gained). Base. Needs its own Step 1 / Step 2 worked example (th3's 5 kg × 2 m example is ready-made) before any pupil does one.
- Work done → power (P = W/t) appears only as a link; if Design sets a W = Fs → P = W/t question, that is a second chain (Step 1 W = Fs; Step 2 P = W/t; Convert minutes → s) and needs its own worked example.

## 6. Verdict
SOURCE OK WITH FLAGS. All arithmetic and both quiz items correct and base. One off-spec link (P = Fv), three imprecisions (friction → kinetic; W used for work and weight in one line; "negative work"), and the spec's friction → temperature rise and N m ↔ J conversion are thin. No Mide call.
