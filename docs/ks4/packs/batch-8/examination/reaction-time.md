# Examination — Reaction Time (reaction-time) — AQA 8464 4.5.2 + RP 6 / 8461 4.5.2.1 + RP 7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.2-reaction-time.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1) §4.5.2, §10.2.6 (RP 6), §6.5.4.3.2, Working Scientifically WS 3.7; `AQA-8461-spec.txt` (Biology v1.0) §4.5.2.1, §8.2.7 (RP 7), WS 3.7; `AQA-8463-spec.txt` §4.5.6.3.2. Equation sheets `8464-equation-sheet.txt` and `8463-equation-sheet-Jun26.txt` (June 2026) read: neither prints d = ½gt² or t = √(2d/g). Route audit row `reaction-time` ("4.5.2 (RP6) | 4.5.2.1 (RP7)").

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, which explains option index n (credited answer = index 0). The file's "4.5.2" is the true 8464 ref; the 8461 ref is 4.5.2.1. No `higher` field, no `rp` field (the RP sits in theory 2 and 3).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.2** | The human nervous system: reaction-time MS 4a + **Required practical activity 6** | base |
| 8461 | **4.5.2.1** | Structure and function: reaction-time MS 4a + **Required practical activity 7** | base |
| 8464 / 8461 | 10.2.6 / 8.2.7 | RP 6 / RP 7 apparatus and techniques (AT 1, 3, 4) | base |
| Cross-link | 8464 6.5.4.3.2 / 8463 4.5.6.3.2 | Reaction time (physics, stopping distances) | base |
| Cross-link | 8464/8461 WS 3.7 | random error reduced by "making more measurements and reporting a mean value" | base |

Spec statements (verbatim):
- 8464 4.5.2 / 8461 4.5.2.1: "Students should be able to translate information about reaction times between numerical and graphical forms. [MS 4a]" "Required practical activity 6 [8461: 7]: plan and carry out an investigation into the effect of a factor on human reaction time. AT skills covered by this practical activity: AT 1, 3 and 4."
- 10.2.6 / 8.2.7: "AT 1 – use appropriate apparatus to record time. AT 3 – selecting appropriate apparatus and techniques to measure the process of reaction time. AT 4 – safe and ethical use of humans to measure physiological function of reaction time and responses to a chosen factor." "MS 4a – translate information between numerical and graphical forms."
- 8464 6.5.4.3.2 / 8463 4.5.6.3.2: "Reaction times vary from person to person. Typical values range from 0.2 s to 0.9 s. A driver's reaction time can be affected by tiredness, drugs and alcohol. Distractions may also affect a driver's ability to react. Students should be able to: explain methods used to measure human reaction times and recall typical results; interpret and evaluate measurements from simple methods to measure the different reaction times of students …"

No equation for reaction time appears in any of the four specs or on either June 2026 sheet. AQA biology RP questions on the ruler drop give a ruler-distance → reaction-time conversion table or graph.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Reaction time = time from stimulus to response; whole nervous pathway (theory 1; key_note) | base | 4.5.2 / 4.5.2.1 | all four | OK |
| R2 | Typical 0.2–0.3 s simple stimulus (theory 1) | base | 6.5.4.3.2 / 4.5.6.3.2 (0.2–0.9 s) | all four | OK (C2) |
| R3 | Factors: age, sex, stimulus type, practice, fatigue, drugs/alcohol/caffeine, distraction (theory 1; key_note; matching) | base | 6.5.4.3.2 / 4.5.6.3.2; RP 6/7 "a factor" | all four | OK, sex OFF-SPEC (C5) |
| R4 | Ruler-drop method (theory 2) | base — **RP** | 8464 4.5.2 RP 6 / 8461 4.5.2.1 RP 7; AT 1, 3 | all four | OK |
| R5 | Repeats → mean reduces random variation (theory 2, 3; common_mistake; key_note; q2) | base | WS 3.7; RP | all four | OK, terminology IMPRECISE (C24) |
| R6 | Controls; anticipation; same ruler/person (theory 2, 3) | base — RP | RP 6/7 | all four | OK |
| R7 | Computer-based tests (theory 2) | base — RP (AT 1) | RP 6/7 | all four | OK |
| R8 | Caffeine and distraction investigations; hypotheses; placebo (theory 3) | base — RP | RP 6/7 | all four | OK, mechanism IMPRECISE (C16) |
| R9 | Limitations of ruler drop (theory 3) | base — RP | WS 3.7; 6.5.4.3.2 "interpret and evaluate" | all four | OK |
| R10 | d = ½gt²; t = √(2d/g); cm → m (theory 2; equations; variables; common_mistake; FIFA; q1) | none — **OFF-SPEC** on every route | — (not on any spec or sheet) | all four | OFF-SPEC (F1) |
| R11 | Safe and ethical use of humans (AT 4) | base — RP | RP 6/7 AT 4 | — | not in file — GAP (F2) |
| R12 | Translating reaction-time data numerical ↔ graphical (MS 4a) | base | 4.5.2 / 4.5.2.1; RP | — | not in file — GAP (F2) |
| — | `higher` | none | no HT statement | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | reaction time = time between stimulus detected and response | OK | — | — |
| C2 | theory 1 | typical 0.2–0.3 s for a simple stimulus | OK | Teach alongside AQA's "Typical values range from 0.2 s to 0.9 s" (physics), which pupils on every route also learn. | 6.5.4.3.2 / 4.5.6.3.2 |
| C3 | theory 1 | pathway receptor → sensory → relay → motor → effector | OK | — | 4.5.2 |
| C4 | theory 1 | age increases reaction time | OK | (In adults.) | — |
| C5 | theory 1 | "GENDER — some research suggests small differences" | OK, OFF-SPEC | Hedged correctly; not on spec. Drop or keep as a possible factor to investigate only. | — |
| C6 | theory 1 | sound reactions slightly faster than visual | OK | ≈0.15 s vs ≈0.2 s. | — |
| C7 | theory 1 | practice improves; fatigue slows; depressants slow; caffeine may improve; distraction slows | OK | Spec: "tiredness, drugs and alcohol … Distractions". | 6.5.4.3.2 / 4.5.6.3.2 |
| C8 | theory 2 steps 1–5 | ruler vertical, 0 cm at bottom; catcher's fingers at 0 not touching; dropped without warning; caught; distance measured | OK | Standard AQA method. Read the distance at the top of the thumb (add). | RP 6/7 |
| C9 | theory 2 step 6 | d = ½ × g × t²; t = √(2d/g), g = 10 m/s² | OK physics, **OFF-SPEC** | Correct free-fall kinematics; not on 8461/8464/8463 or either sheet. Exams supply a conversion table. | F1 |
| C10 | theory 2 step 7 | repeat, calculate mean to reduce effect of random variation | OK | Spec wording: random error "reduced by making more measurements and reporting a mean value". | WS 3.7 |
| C11 | theory 2 | "IMPROVING RELIABILITY" | IMPRECISE | AQA (2016 specs) does not use "reliable"; the terms are repeatable / reproducible / precise / reduce random error. | WS 3.7 (F3) |
| C12 | theory 2 | no anticipation; same ruler, position, person | OK | Control variables. | RP 6/7 |
| C13 | theory 2 | computer tests "more accurate"; remove human error in reading the ruler | OK | (Higher resolution, no reading error.) | AT 1 |
| C14 | theory 3 | caffeine hypothesis: decreases reaction time | OK | — | — |
| C15 | theory 3 | before/after caffeine; placebo group; same person, test, time of day; practice effect | OK | Good method. Placebo = decaffeinated drink. | RP 6/7 |
| C16 | theory 3 | "Caffeine is a stimulant — it increases the release of neurotransmitters at synapses." | IMPRECISE | Caffeine blocks adenosine receptors; net effect is more nervous activity. Off-spec mechanism. Say "a stimulant that speeds up nervous activity". | — |
| C17 | theory 3 | distraction hypothesis and method | OK | Matches the physics AT 1 suggestion "Measure the effect of distractions on reaction time". | 4.5.6.3.2 |
| C18 | theory 3 | limitations: random variation, anticipation, reading error; so repeats + mean | OK | — | WS 3.7 |
| C19 | common_mistake | distance in metres; g = 10 m/s² (or 9.8); t = √(2d/g); repeats → mean | OK physics; OFF-SPEC equation | Second half (repeats → mean) is on spec. | F1 |
| C20 | key_note | t = √(2d/g); factors; repeats → mean "for reliability" | OK / IMPRECISE | Equation off-spec; "reliability" → "to reduce the effect of random error" (F3). | — |
| C21 | equations | "d = ½ × g × t²", "t = √(2d ÷ g)" | OK algebra; OFF-SPEC | Rearrangement correct. Label: neither "On the sheet" nor "Learn it". If kept: "Given in the question". | F1 |
| C22 | variables | d m; t s; g "Gravitational field strength", unit "m/s²", symbol blank | OK | m/s² ≡ N/kg. Physics uses g = 9.8 N/kg; 10 m/s² is an accepted rounding when the question gives it. The empty symbol column is a data gap (show "m/s²"). | — |
| C23 | FIFA | 20 cm = 0.20 m; t = √(2 × 0.20 ÷ 10) = √(0.40 ÷ 10) = √0.04 = 0.2 s | OK | Arithmetic ✓. Answer better written 0.20 s (2 s.f. as data). | — |
| C24 | CFIFA Convert `[NEW — to be examined]` | "Distance must be in metres to match g in m/s²: 20 cm = 0.20 m." | **OK** | ✓ Marked examined. (The verbatim I step repeats the conversion; harmless.) The amendment's second example (nothing to convert, e.g. "falls 0.125 m" → 0.158 s ≈ 0.16 s) must be supplied by Design if the calculation is kept. | CFIFA amendment |
| C25 | q1 key | 45 cm → 0.45 m; √(2 × 0.45 ÷ 10) = √0.09 = 0.30 s | OK | ✓. OFF-SPEC equation (F1). | — |
| C26 | q1 opt 1 / wx1 | √(2 × 45 ÷ 10) = √9 = 3.0 s; forgot to convert cm → m | OK | 3.0 ✓. Aligned. | — |
| C27 | q1 opt 2 / wx2 | 0.45 ÷ 10 = 0.045 s; t = d/g is not the formula | OK | 0.045 ✓. Aligned. | — |
| C28 | q1 opt 3 / wx3 | 2 × 0.45 × 10 = 9.0 s; multiplied instead | OK | 9.0 ✓. Aligned. | — |
| C29 | q2 key | random variation between trials; mean gives a "more reliable estimate" | OK, IMPRECISE wording | Science right; "reliable" is not AQA's term (F3). Usable. | WS 3.7 |
| C30 | q2 wx1 | rulers don't wear out; variation is biological | OK | Aligned. | — |
| C31 | q2 wx2 | the person does not calculate during the test | OK | Aligned. | — |
| C32 | q2 wx3 | practice is a confound, but the main reason for repeats is random variation | OK | Aligned. | WS 3.7 |
| C33 | matching (to be replaced) | alcohol, fatigue, distraction increase; caffeine, practice decrease | OK | — | — |

Count: **0 WRONG**; **IMPRECISE**: C11, C16, C20, C29; **OFF-SPEC**: the equation set (C9, C19, C21, FIFA, q1), C5. All 7 calculations rechecked ✓. wrong_explanations: all 6 keys aligned to their own option index.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | tests t = √(2d/g), which is on no spec and no sheet | Usable on all four routes **only if** Design keeps the ruler-drop calculation as taught content (with both CFIFA worked examples first). Otherwise not usable (F1). |
| q2 | "reliable" wording | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "repeat to make it a fair test" (repeats reduce random error; controls make it fair); "a bigger distance means a faster reaction"; "caffeine is a depressant"; "the mean makes it accurate" (it reduces random error; accuracy is closeness to the true value); naming the dependent variable as "the ruler"; forgetting to control the hand used or the drop height.

**Command words**: Plan (6-mark investigation of a factor), Describe (the method), Explain (why repeats/means; why a control), Identify (variables), Use the table / Plot / Translate (MS 4a), Evaluate (ruler vs computer).

**Typical questions** ⚑ examiner-drafted
- *Plan an investigation into the effect of caffeine on reaction time. [6]* — Level 3: ruler drop or computer test; independent variable caffeine (drink with/without, e.g. cola vs decaf); measure distance/time; repeat ≥3–5 times and take a mean; control person, hand, ruler, starting position, time of day, no warning; safety/ethics: consent, limited caffeine dose, exclude anyone sensitive to caffeine; compare means.
- *Give two variables that should be controlled. [2]* — same person catching; same hand; same ruler; same starting height/finger gap; same time of day (any two).
- *Use the conversion table to find the mean reaction time. [2]* — mean distance (1); read the table/graph (1).
- *Suggest why the computer test gives more precise results than the ruler drop. [1]* — records time directly to the millisecond / no reading of the ruler scale.

**Required practical**: **Combined RP 6** (8464 4.5.2; §10.2.6) = **Biology RP 7** (8461 4.5.2.1; §8.2.7). On all four routes. Physics links: 8464 6.5.4.3.2 / 8463 4.5.6.3.2 (not an RP).

## 6. Verdict
SOURCE OK WITH FLAGS. Method, controls, factors, hypotheses and repeats/means are correct and on spec for RP 6/7. All arithmetic is correct and every wrong-explanation is aligned. The CFIFA Convert line is OK. The flags: (1) d = ½gt² / t = √(2d/g), with its FIFA and q1, is correct physics but off-spec on every route and on no sheet; AQA gives a conversion table. (2) The spec's AT 4 (safe and ethical use of humans) and MS 4a (table ↔ graph) are missing. (3) "Reliability" should be AQA's own wording. Nothing for Mide: whether to keep the off-spec calculation as enrichment is a lesson-design choice, not a science question.
