# Examination — Blood Glucose Control and Diabetes (blood-glucose-diabetes) — AQA 8464 4.5.3.2 / 8461 4.5.3.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.3-blood-glucose-diabetes.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.5.1; 4.5.3.2), `AQA-8461-spec.txt` (Biology v1.0, 4.5.3.2). Architecture CFIFA amendment (24 Sep 2026) and the 2 Oct four lesson rules. Route audit row `blood-glucose-diabetes` (OK, CF CH TF TH; HT layer glucagon).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n (explains `opts[n]`, 0-based; key always option 0). T1–T4 = theory blocks. Route copies: `higher` null on CF and TF (served CH/TH only). One FIFA (+ its CFIFA form with one `[NEW — to be examined]` Convert line). **wx alignment checked: all three items correctly paired; no shift.**

**Spec ref:** the file and site label "4.5.3"; true ref **4.5.3.2** in both specs (identical text).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.3.2** | Control of blood glucose concentration | base, with two **(HT only)** statements (glucagon; negative feedback cycle) |
| 8461 | **4.5.3.2** | Control of blood glucose concentration | same |
| Supporting | 4.5.1 (pancreas as a coordination centre); 4.2.2.1 (proteases digest protein — why insulin is injected) | | base |

Spec statements (verbatim, 8464 = 8461): "Blood glucose concentration is monitored and controlled by the pancreas. If the blood glucose concentration is too high, the pancreas produces the hormone insulin that causes glucose to move from the blood into the cells. In liver and muscle cells excess glucose is converted to glycogen for storage. Students should be able to explain how insulin controls blood glucose (sugar) levels in the body. Type 1 diabetes is a disorder in which the pancreas fails to produce sufficient insulin. It is characterised by uncontrolled high blood glucose levels and is normally treated with insulin injections. In Type 2 diabetes the body cells no longer respond to insulin produced by the pancreas. A carbohydrate controlled diet and an exercise regime are common treatments. Obesity is a risk factor for Type 2 diabetes. Students should be able to compare Type 1 and Type 2 diabetes and explain how they can be treated. Students should be able to extract information and interpret data from graphs that show the effect of insulin in blood glucose levels in both people with diabetes and people without diabetes." "(HT only) If the blood glucose concentration is too low, the pancreas produces the hormone glucagon that causes glycogen to be converted into glucose and released into the blood. (HT only) Students should be able to explain how glucagon interacts with insulin in a negative feedback cycle to control blood glucose (sugar) levels in the body." WS 1.3: obesity and diabetes, recommendations.

Note: in both specs the phrase "negative feedback" appears only in (HT only) statements (here, thyroxine, ADH). 4.5.1's base model is receptor → coordination centre → effector, responses that "restore optimum levels".

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Why control matters; hypo/hyperglycaemia (T1) | base (context) | 4.5.1 | all four | OK (off-spec detail) |
| R2 | Pancreas monitors and controls (T1) | base | 4.5.3.2 | all four | OK |
| R3 | Insulin → glucose into cells; glycogen in liver and muscle (T2; key_note; FIFA; q1) | base | 4.5.3.2 | all four | IMPRECISE (F3) |
| R4 | "This is NEGATIVE FEEDBACK" (T2 last line) | **higher** (term) | 4.5.3.2 (HT only) | all four | ROUTE (F1) |
| R5 | Glucagon, glycogen → glucose (T3; common_mistake; key_note; `higher`) | **higher** | 4.5.3.2 (HT only) | all four | ROUTE (F1) |
| R6 | Type 1 and Type 2: cause, treatment, risk factors (T4; q2; q3) | base | 4.5.3.2 | all four | OK; metformin IMPRECISE (F4) |
| R7 | Graph interpretation, with and without diabetes | base | 4.5.3.2 (MS 2c) | **missing** | GAP (F2) |
| R8 | Obesity–diabetes evaluation (WS 1.3) | base (skill) | 4.5.3.2 | partly (risk factors only) | GAP (F2) |
| R9 | FIFA "Blood Glucose Negative Feedback" | base (insulin arm); title and "A" wording HT term | 4.5.3.2 | all four | OK as science; not a calculation (F5) |
| R10 | q1, q2, q3 | base | 4.5.3.2 | all four | OK |
| — | RP, equations | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | narrow range ≈ 4–6 mmol/L | OK (off-spec) | Typical fasting range; context only. | — |
| C2 | T1 | too low: brain deprived → confusion, coma; brain relies almost entirely on glucose | OK (off-spec) | — | — |
| C3 | T1 | too high long-term: water drawn from cells by osmosis; vessel and nerve damage; blindness, kidney failure, heart attack, stroke | OK (off-spec) | — | — |
| C4 | T1 | pancreas monitors and regulates; contains cells that detect glucose | OK | Spec wording. | 4.5.3.2 |
| C5 | T2 | after a meal glucose rises; beta cells detect; insulin released | OK | Beta cells off-spec. | 4.5.3.2 |
| C6 | T2 | "Insulin travels to the LIVER and MUSCLE CELLS and causes them to: Absorb MORE glucose … Convert glucose → GLYCOGEN" | IMPRECISE | Spec: insulin "causes glucose to move from the blood into the cells" (body cells generally); then "in liver and muscle cells excess glucose is converted to glycogen". Two steps; the first is not limited to liver and muscle. | 4.5.3.2 |
| C7 | T2 | glucose falls back to the set point; "NEGATIVE FEEDBACK" | OK, term **HT** | — | 4.5.3.2 (HT only) |
| C8 | T3 | between meals glucose falls; alpha cells release glucagon; liver breaks glycogen → glucose, released into blood | OK, **HT** | Spec wording; alpha cells, "glycogenolysis" off-spec. | 4.5.3.2 (HT only) |
| C9 | T4 | Type 1: immune system destroys beta cells; little or no insulin | OK | Spec: "pancreas fails to produce sufficient insulin". Autoimmune cause off-spec but true. | 4.5.3.2 |
| C10 | T4 | Type 1 onset usually childhood/adolescence | OK (off-spec) | Typical; can begin at any age. | — |
| C11 | T4 | insulin injections or pump; not a tablet because protein is digested | OK | — | 4.5.3.2; 4.2.2.1 |
| C12 | T4 | Type 2: cells resistant to insulin; pancreas may still make it | OK | Spec: "body cells no longer respond to insulin". | 4.5.3.2 |
| C13 | T4 | risk factors: obesity, inactivity, diet, family history, age | OK | Spec names obesity. | 4.5.3.2 |
| C14 | T4 | treatment: weight loss, exercise, healthier diet | OK | Spec: "carbohydrate controlled diet and an exercise regime". | 4.5.3.2 |
| C15 | T4 | "Metformin (increases cell sensitivity to insulin)" | IMPRECISE (off-spec) | Metformin mainly reduces glucose release by the liver (and improves sensitivity). Off-spec: drop, or "tablets such as metformin". | — |
| C16 | `higher` | glycogenesis, glycogenolysis, **gluconeogenesis** | OK, terms off-spec | Gluconeogenesis is A-level; do not show. | — |
| C17 | `higher` | 4–6 mmol/L negative feedback; Type 1/Type 2 summary | OK | — | 4.5.3.2 |
| C18 | common_mistake | insulin → storage; glucagon → breakdown; "INsulin = INto storage" | OK, glucagon half **HT** | — | 4.5.3.2 |
| C19 | key_note | as above | OK | Glucagon clause HT. | 4.5.3.2 |
| C20 | FIFA F | carbs digested → glucose absorbed → glucose rises | OK | — | 4.2.2.1; 4.5.3.2 |
| C21 | FIFA I | beta cells detect rise → insulin into blood | OK | — | 4.5.3.2 |
| C22 | FIFA F | insulin to liver and muscles → glucose → glycogen | IMPRECISE | Same omission as C6: "glucose moves from the blood into cells" is the spec's first effect. | 4.5.3.2 |
| C23 | FIFA A | falls back to ~5 mmol/L — "negative feedback complete" | OK, term HT | On CF/TF say "back to normal". | 4.5.3.2 (HT only) |
| C24 | CFIFA Convert `[NEW]` | "Nothing to convert — no numerical values or units are involved; this is a descriptive biology process answer." | OK | True as written → `[NEW — examined ✓]`. But see F5: this is not a calculation and should not be mounted in the CFIFA block. | CFIFA amendment |
| C25 | matching (to be replaced) | five pairs | OK | Glucagon pairs HT. | — |
| C26 | q1 key | insulin, beta cells, glucose → glycogen in liver | OK | — | 4.5.3.2 |
| C27 | q1 wx1 | glucagon released when glucose too low; would worsen the rise | OK | HT fact in an explanation of a distractor; acceptable on all routes. | 4.5.3.2 (HT only) |
| C28 | q1 wx2 | adrenaline raises glucose but is not the routine response to eating | OK | — | 4.5.3.6/4.5.3.7 |
| C29 | q1 wx3 | thyroxine controls metabolic rate, not glucose directly | OK | — | 4.5.3.6/4.5.3.7 |
| C30 | q2 key | insulin is a protein, digested by proteases in the gut | OK | — | 4.2.2.1 |
| C31 | q2 wx1 | oral insulin is being researched; real reason is digestion | OK | — | — |
| C32 | q2 wx2 | not speed; protein broken into amino acids by digestive enzymes | OK | — | 4.2.2.1 |
| C33 | q2 wx3 | insulin acts on liver and muscle, not in the pancreas | OK | — | 4.5.3.2 |
| C34 | q3 key | "Type 1: pancreas produces no insulin (autoimmune). Type 2: cells become resistant to insulin (lifestyle-related)." | OK | Spec says "fails to produce sufficient insulin"; "no insulin" is the standard simplification, credited. | 4.5.3.2 |
| C35 | q3 wx1 | Type 2 ≈ 90% of cases | OK | UK ~90%. | — |
| C36 | q3 wx2 | reversed treatments | OK | — | 4.5.3.2 |
| C37 | q3 wx3 | only Type 1 is autoimmune | OK | — | — |

Count: **0 WRONG**. IMPRECISE: C6, C15, C22. ROUTE: glucagon and "negative feedback" served on every route (F1). GAP: graph interpretation (MS 2c) and obesity evaluation (F2).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | Key is base; options 2–3 name glucagon and adrenaline (HT), but only as wrong options and the key needs base knowledge only | Usable on all four routes. |
| q2, q3 | correct, base | Usable on all four routes. |

## 5. CFIFA note
The single FIFA is a four-step description of the insulin response, not a calculation; the Convert line is correct ("nothing to convert"). Rule 3 and the CFIFA block exist for calculations. Recommend Design teaches this as a PROCESS sequence (stimulus → detection → hormone → effect → back to normal), not in the CFIFA block (F5). No calculation is on this lesson's spec; the quantitative skill is graph reading (F2).

## 6. Verdict
SOURCE OK WITH FLAGS. No wrong science. The insulin step skips the spec's first effect (glucose moves from blood into cells). Glucagon and the term "negative feedback" are HT and sit on every route today. The spec's graph-interpretation statement (base, MS 2c) has no material at all. **For Mide:** nothing.
