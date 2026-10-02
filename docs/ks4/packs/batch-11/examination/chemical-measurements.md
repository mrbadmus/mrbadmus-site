# Examination — Chemical Measurements (chemical-measurements) — AQA 8464 5.3.1.4 / 8462 4.3.1.4
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.3.1.4-chemical-measurements.md`.
Spec sources read as text: `AQA-8462-spec.txt` 4.3.1.4, Working Scientifically WS 3.4 and WS 3.7 (definitions of accurate, precise, repeatable, reproducible, random and systematic error); `AQA-8464-spec.txt` 5.3.1.4 (identical). Both specs searched for "percentage uncertainty": absent. No equation sheet applies (chemistry). Route audit read: `chemistry.md` row `chemical-measurements` (OK, base, CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. All four route copies identical; no `higher` field.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.3.1.4** | Chemical measurements | base |
| 8462 | **4.3.1.4** | Chemical measurements | base |
| Supporting | WS 3.4 (uncertainty); WS 3.7 (accuracy, precision, repeatability, reproducibility, random/systematic error) | | base |

Spec statement (verbatim, 8464 = 8462): "Whenever a measurement is made there is always some uncertainty about the result obtained. Students should be able to: represent the distribution of results and make estimations of uncertainty; use the range of a set of measurements about the mean as a measure of uncertainty."

WS 3.7 (verbatim): "An accurate measurement is one that is close to the true value. Measurements are precise if they cluster closely. Measurements are repeatable when repetition, under the same conditions by the same investigator, gives similar results. Measurements are reproducible if similar results are obtained by different investigators with different equipment. Measurements are affected by random error due to results varying in unpredictable ways; these errors can be reduced by making more measurements and reporting a mean value. Systematic error is due to measurement results differing from the true value by a consistent amount each time."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | Accuracy vs precision (th1; key_note) | base | WS 3.7 | IMPRECISE (C1) |
| R2 | Units: g, cm³, dm³, °C, s; 1 dm³ = 1000 cm³ (th1) | base | MS / 5.3.2.5 context | OK |
| R3 | Every measurement has uncertainty (th2) | base | 5.3.1.4 | OK |
| R4 | Random and systematic error; repeat and mean (th2; th3) | base | WS 3.7 | OK |
| R5 | % uncertainty equation, FIFA, q1 | **not in spec** (A-level) | — | OFF-SPEC |
| R6 | Range about the mean as uncertainty | base | 5.3.1.4 | **MISSING from the data** (GAP) |
| R7 | Apparatus: balance, burette, pipette, measuring cylinder, thermometer; meniscus; parallax; tare (th3; common_mistake) | base | AT 1; WS 3.7 | OK except C9 |
| R8 | q1 burette vs cylinder % uncertainty | base idea, off-spec calculation | WS 3.7 | usable as extension |
| R9 | q2 where to read a meniscus | base | AT 1 | wx1 WRONG for a burette |
| — | rp, `higher` | none | — | correct (RP titration is 8462 4.4.2.5, chemistry only, elsewhere) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1; key_note | "PRECISION — how reproducible/consistent measurements are" | IMPRECISE | AQA: "Measurements are precise if they cluster closely." Reproducible is a different term (different investigators, different equipment). th3 "Repeat and average for reliability" — "reliability" is not an AQA term; say repeatable. | WS 3.7 |
| C2 | th1 | precise-not-accurate / accurate-not-precise | OK | — | WS 3.7 |
| C3 | th1 | 1 dm³ = 1 litre = 1000 cm³; 1 cm³ = 0.001 dm³ = 1 mL | OK | ✓ | — |
| C4 | th2 | reading error; systematic = consistent bias; random = unpredictable scatter | OK | Matches WS 3.7. | WS 3.7 |
| C5 | th2 | reduce uncertainty: more precise apparatus; repeats and mean | OK | — | WS 3.7 |
| C6 | th2; equations; variables; key_note | % uncertainty = (uncertainty ÷ measured value) × 100; larger measurement → smaller % | OFF-SPEC | Arithmetic and idea correct, but not in 8462/8464. The spec's quantitative demand — range about the mean — is absent from all of the frozen data. | 5.3.1.4 |
| C7 | th3 | balance ±0.01 g / ±0.001 g; burette 0.1 cm³ graduations read to ±0.05 cm³; pipette fixed 25.00 cm³; thermometer ±1 / ±0.5 °C | OK | Typical values ✓. (A titre is two readings, so ±0.10 cm³.) | — |
| C8 | th3; key_note | "Burette: ±0.05 cm³ — most precise for volumes" | IMPRECISE | A pipette delivers its one fixed volume with the smallest uncertainty; a burette is the precise way to deliver a variable volume. | — |
| C9 | common_mistake | "Reading from the top overestimates the volume." | IMPRECISE | True for a measuring cylinder; false for a burette, whose scale reads downward (top of meniscus gives a smaller reading). | AT 1 |
| C10 | th3; common_mistake | bottom of meniscus at eye level; parallax; tare the balance; failing to tare = systematic error | OK | ✓ | WS 3.7 |
| C11 | FIFA | 0.5 ÷ 25.0 = 0.02; × 100 = 2.0 % | OK (OFF-SPEC calc) | ✓ | — |
| C12 | Convert (NEW) | "Nothing to convert — the measured volume and its uncertainty are both already in cm³, the same unit." | OK | Examined ✓ | CFIFA amendment |
| C13 | q1 key | burette 0.05 ÷ 25 × 100 = 0.2 %; cylinder 1 ÷ 25 × 100 = 4 % | OK | ✓ both | — |
| C14 | q1 opt1 / wx1 | "larger equipment is always more accurate" / "Equipment size doesn't determine accuracy — precision depends on the uncertainty relative to the measurement" | IMPRECISE | Aligned ✓. Conflates accuracy, precision and % uncertainty (C1). | WS 3.7 |
| C15 | q1 opt2 / wx2 | same volume, different uncertainties | OK | Aligned ✓ | — |
| C16 | q1 opt3 / wx3 | cylinder has the LARGER absolute uncertainty | OK | Aligned ✓ | — |
| C17 | q2 key | bottom of the meniscus; water's surface is concave | OK | ✓ | AT 1 |
| C18 | q2 opt1 / wx1 | "From the top — this gives the largest volume reading" / "Reading from the TOP of the meniscus gives an overestimate" | **WRONG** (for a burette) | Aligned ✓, but the stem names "a burette or measuring cylinder". On a burette the top of the meniscus gives the SMALLER reading. True only for the cylinder. | AT 1 |
| C19 | q2 opt2 / wx2 | middle of the meniscus | OK | Aligned ✓ | — |
| C20 | q2 opt3 / wx3 | wrong part → systematic error | OK | Aligned ✓ (consistent offset = systematic). | WS 3.7 |
| C21 | matching (to be replaced) | burette, pipette, cylinder, balance, thermometer | OK | — | — |

Count: **1 WRONG** (C18, frozen quiz). OFF-SPEC: C6/C11 (% uncertainty). IMPRECISE: C1, C8, C9, C14. GAP: the spec's range-about-the-mean core is missing (written into the source file from the spec).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | wx1 / option 1 false for a burette | **Do not use as written.** |
| q1 | correct, but a % uncertainty calculation (off-spec) | Usable on all routes only as an extension item, labelled so; not an Apply rung of spec demand. |
| FIFA / equation | off-spec | Keep as an extension; the lesson's core CFIFA must be mean ± half the range. |

## 5. Calculations and chains (rule 3)
- **Core (missing from the data):** mean of repeats, then uncertainty = ± range ÷ 2. Chain: Step 1 mean = sum ÷ number of readings; Step 2 range = largest − smallest; Step 3 uncertainty = ± range ÷ 2; report mean ± uncertainty. Leave out anomalies first. Example: titres 24.10, 24.30, 24.20 cm³ → mean 24.20 cm³; range 0.20 cm³; 24.20 ± 0.10 cm³.
- **Extension:** % uncertainty — one step, no chain.
- **Convert:** dm³ ↔ cm³ (× 1000), mL = cm³ — the natural "wrong unit" worked example (e.g. 0.025 dm³ → 25 cm³).

## 6. Verdict
SOURCE HAS ERRORS — one frozen quiz item wrong for half its stem (q2, burette); the lesson's only calculation (% uncertainty) is off-spec while the spec's own demand (range about the mean) is missing. Definitions should follow WS 3.7. Nothing for Mide.
