# Examination — Homeostasis (homeostasis) — AQA 8464 4.5.1 / 8461 4.5.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-8/04-checked-science-source/biology-4.5.1-homeostasis.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1) §4.5.1, §4.5.3.2, §4.5.3.6; `AQA-8461-spec.txt` (Biology v1.0) §4.5.1, §4.5.2.4, §4.5.3.2, §4.5.3.3, §4.5.3.7. Route audit `ks4-routes/docs/ks4/route-audit/biology.md` row `homeostasis`. No equation sheet applies (biology).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, which explains option index n (credited answer = index 0). The file's own "4.5.1" is the true AQA ref on both specs. `higher` CF and TF copies are `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.5.1** | Homeostasis | base |
| 8461 | **4.5.1** | Homeostasis | base |
| 8464 | 4.5.3.2 (last two statements) / 4.5.3.6 | Glucagon + insulin "negative feedback cycle"; Feedback systems | **(HT only)** |
| 8461 | 4.5.3.2 (last two statements) / 4.5.3.7 | as above; Negative feedback | **(HT only)** |
| 8461 | 4.5.2.4 | Control of body temperature | (biology only) — mechanism detail belongs to `thermoregulation` |
| 8461 | 4.5.3.3 | Water and nitrogen balance; ADH "controlled by negative feedback" | (biology only), ADH lines (HT only) |

Spec statements (verbatim, 8464 = 8461 4.5.1): "Students should be able to explain that homeostasis is the regulation of the internal conditions of a cell or organism to maintain optimum conditions for function in response to internal and external changes. Homeostasis maintains optimal conditions for enzyme action and all cell functions. In the human body, these include control of: blood glucose concentration; body temperature; water levels. These automatic control systems may involve nervous responses or chemical responses. All control systems include: cells called receptors, which detect stimuli (changes in the environment); coordination centres (such as the brain, spinal cord and pancreas) that receive and process information from receptors; effectors, muscles or glands, which bring about responses which restore optimum levels."

The term **negative feedback** does not appear in 4.5.1. It appears only in HT-labelled statements: 8464 4.5.3.2 / 8461 4.5.3.2 "(HT only) … glucagon interacts with insulin in a negative feedback cycle"; 8464 4.5.3.6 / 8461 4.5.3.7 "(HT only) … Thyroxine levels are controlled by negative feedback … Interpret and explain simple diagrams of negative feedback control."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Definition of homeostasis; internal + external changes (theory 1; key_note; q1 first clause) | base | 4.5.1 | all four | OK |
| R2 | Controlled: blood glucose, body temperature, water (theory 1; key_note) | base | 4.5.1 | all four | OK |
| R3 | Optimal conditions for enzyme action and cell function (theory 4; key_note; q2) | base | 4.5.1 | all four | OK |
| R4 | Receptor → coordination centre → effector; effectors are muscles or glands; response restores optimum (theory 3; key_note) | base | 4.5.1 | all four | OK (C9–C12) |
| R5 | Nervous or chemical responses | base | 4.5.1 | all four | not in file — GAP (F4) |
| R6 | The NAME "negative feedback"; response opposes the change; oscillation round a set point (theory 2; common_mistake; key_note; q1 key wording; q3) | **higher** | 8464 4.5.3.6 / 8461 4.5.3.7; 4.5.3.2 (HT) | all four (theory/quiz), CH TH (`higher`) | ROUTE (F1) |
| R7 | Constructing/interpreting feedback-loop diagrams (`higher`) | **higher** | 8464 4.5.3.6 / 8461 4.5.3.7 (WS: "Interpret and explain simple diagrams") | CH TH | OK, "construct" over-reaches (C21) |
| R8 | Positive feedback; clotting, labour (`higher`) | none — OFF-SPEC | — | CH TH | OFF-SPEC (F2) |
| R9 | Glucagon / raising low glucose (q3; q3 wx2) | **higher** | 4.5.3.2 (HT only) | all four | ROUTE (F1) |
| R10 | Thermoreceptors, hypothalamus, shivering, sweat glands as examples (theory 3) | triple (mechanism) | 8461 4.5.2.4 (biology only) | all four | OK as named examples only (C10) |
| R11 | Osmoreceptors in the hypothalamus (theory 3) | none — OFF-SPEC | (8461 4.5.3.3 names the pituitary and ADH only) | all four | OFF-SPEC detail (C10) |
| R12 | Consequences: denaturation, hypo/hyperglycaemia, cells shrink/swell (theory 4) | base (context) | 4.5.1; 4.1.3.2 osmosis; 4.5.3.2 diabetes | all four | OK, one IMPRECISE (C16) |
| — | RP, equations, FIFA | none | — | — | correct: 4.5.1 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | "maintenance of a stable internal environment despite changes in external conditions or internal activity" | OK | Accepted paraphrase; spec wording "regulation of the internal conditions … to maintain optimum conditions for function in response to internal and external changes" is the one to teach. | 4.5.1 |
| C2 | theory 1 | body temperature ~37 °C for optimal enzyme activity | OK | — | 4.5.1 |
| C3 | theory 1 | blood glucose ~5 mmol/L | OK | Correct (normal fasting ≈ 4–6 mmol/L); not required. | — |
| C4 | theory 1 | water content controlled to stop cells shrinking/swelling | OK | (osmosis) | 4.1.3.2 |
| C5 | theory 1 | "warm-blooded animals … Arctic … desert" | OK | Context. | — |
| C6 | theory 2 | "All homeostatic control systems use NEGATIVE FEEDBACK" | OK (HT term) | True; but the term is HT only (R6). Base wording: "the effector's response reverses the change and restores the optimum level". | 4.5.1; 4.5.3.6/4.5.3.7 |
| C7 | theory 2 | 'negative' = response opposes the change | OK | — | — |
| C8 | theory 2 | oscillates slightly around a set point | OK | "Set point" is not a spec term but is standard and correct. | — |
| C9 | theory 3 | receptor detects changes | OK | — | 4.5.1 |
| C10 | theory 3 | receptor "generates a signal proportional to the degree of change"; examples: thermoreceptors in skin, osmoreceptors in hypothalamus, glucose receptors in pancreas | IMPRECISE / OFF-SPEC detail | "Proportional" is not a GCSE claim and not generally true — drop it. Osmoreceptors are off-spec (8461 4.5.3.3 names only the pituitary releasing ADH). Skin temperature receptors and the pancreas monitoring glucose are on spec (8461 4.5.2.4; 4.5.3.2 "monitored and controlled by the pancreas"). | 4.5.3.2; 8461 4.5.2.4 |
| C11 | theory 3 | coordination centre compares with set point; hypothalamus (temperature, water), pancreas (glucose) | OK | Spec examples are "brain, spinal cord and pancreas"; 8461 4.5.2.4 calls the temperature one "the thermoregulatory centre in the brain". "Hypothalamus" is accepted, not required. | 4.5.1 |
| C12 | theory 3 | effector = muscle or gland; shivering, sweat glands, endocrine glands | OK | Shivering/sweating are 8461 4.5.2.4 (biology only) — fine as named examples on every route; their mechanism belongs to `thermoregulation` (TF TH). | 4.5.1; 8461 4.5.2.4 |
| C13 | theory 3 | effector's response reduces the original stimulus | OK | — | 4.5.1 "restore optimum levels" |
| C14 | theory 4 | enzymes sensitive to temperature, pH, concentration | OK | — | 4.2.2.1 |
| C15 | theory 4 | temperature too high → enzymes denature → active site shape changes permanently | OK | — | 4.2.2.1 |
| C16 | theory 4 | "Body temperature above ~40°C causes proteins to denature → organ failure → death." | IMPRECISE | Above ~40 °C is dangerous (heat stroke) but most enzymes are not yet denatured there. Say "a few degrees above 37 °C enzymes start to work less well; much above about 40 °C they begin to denature, and this can be fatal." | — |
| C17 | theory 4 | hypoglycaemia → confusion, unconsciousness, coma; hyperglycaemia long-term damage | OK | Correct; context only. | 4.5.3.2 (diabetes) |
| C18 | theory 4 | too little water → cells shrink; too much → animal cells swell, can burst | OK | — | 4.1.3.2 |
| C19 | `higher` | negative feedback opposes change | OK, HT | — | 4.5.3.6/4.5.3.7 |
| C20 | `higher` | "Positive feedback amplifies a change (e.g. blood clotting, uterine contractions during labour)" | OFF-SPEC | True science, not in 8461 or 8464 on any tier. Do not show (F2). | — |
| C21 | `higher` | "construct and interpret diagrams of negative feedback loops" | IMPRECISE | Spec skill is "Interpret and explain simple diagrams of negative feedback control". | 4.5.3.6/4.5.3.7 |
| C22 | common_mistake | 'negative' ≠ harmful; opposes the change | OK | Usable on higher layer; on base layer re-cut without the term or introduce it as a name only (F1). | — |
| C23 | key_note | summary | OK | Uses "negative feedback" (HT term) — same note. | — |
| C24 | q1 key | "Maintaining a stable internal environment using negative feedback mechanisms" | OK, ROUTE | Correct; key carries the HT term (F1). | 4.5.1 |
| C25 | q1 opt 1 / wx1 | raising temperature when hot makes it worse; homeostasis cools | OK | Aligned (key 1 ↔ option 1). | — |
| C26 | q1 opt 2 / wx2 | excretion is not the definition | OK | Aligned. | — |
| C27 | q1 opt 3 / wx3 | growth rate controlled by hormones and genetics, not homeostasis | OK | Aligned. | — |
| C28 | q2 key | enzymes work best at 37 °C; deviations slow or denature | OK | Spec's own reason. | 4.5.1 |
| C29 | q2 wx1 | bacteria survive at 37 °C; ideal for many pathogens (Staphylococcus) | OK | Aligned. | — |
| C30 | q2 wx2 | heart muscle contracts across a range of temperatures | OK | Aligned. | — |
| C31 | q2 wx3 | red blood cells function across a range | OK | Aligned. | — |
| C32 | q3 key | glucose too low → negative feedback raises it back to set point | OK, HT | Raising low glucose is glucagon (HT only). | 4.5.3.2 (HT) |
| C33 | q3 wx1 | positive feedback would make it worse; more insulin when low is dangerous | OK | Aligned. "Positive feedback" used only as a wrong option — acceptable. | — |
| C34 | q3 wx2 | "The pancreas and liver continuously monitor … receptors in the pancreas detect low glucose and release glucagon." | IMPRECISE | The pancreas monitors; the liver is the glucagon target (glycogen → glucose), not a monitor at GCSE. Aligned. | 4.5.3.2 |
| C35 | q3 wx3 | temperature and glucose regulated independently | OK | Aligned. | — |

Count: **0 WRONG**; **IMPRECISE**: C10, C16, C21, C34; **OFF-SPEC**: C20 (`higher`), C10 osmoreceptors. wrong_explanations: all 9 keys aligned to their own option index. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | key names "negative feedback" (HT term) | Usable on all four routes provided the base layer gives "negative feedback" as the name for "restore optimum levels" before q1; otherwise CH TH only. |
| q2 | — | Usable on all four routes. |
| q3 | raising low glucose = glucagon, HT only; wx2 imprecise about the liver | **CH TH only** (F1, F3). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "negative feedback means a bad response"; "homeostasis keeps things exactly constant"; receptor/effector swapped; effector given as "the brain"; "the pancreas is the effector" (it is the coordination centre for glucose, and also a gland); "homeostasis is only about temperature".

**Command words**: Define / Explain (what homeostasis is, why it matters), Name (the three components; the three conditions), Describe (the sequence), Interpret (feedback diagrams, HT).

**Typical questions** ⚑ examiner-drafted
- *What is meant by homeostasis? [2]* — regulation of internal conditions (1); to maintain optimum conditions for function / for enzyme action (1).
- *Name the three types of component in every control system. [3]* — receptor; coordination centre; effector.
- *Give two conditions controlled by homeostasis in the human body. [2]* — blood glucose concentration; body temperature; water level (any two).
- *(HT) Explain what is meant by negative feedback. [2]* — a change from the normal level is detected (1); the response reverses the change / returns it to normal (1).

**Required practical**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All base facts correct; three quiz items correct with aligned explanations. Route problem: "negative feedback" runs through theory 2, common_mistake, key_note, q1 and q3 on every route, but on both specs the term exists only in HT statements; base needs "the response restores the optimum level". `higher` field carries off-spec positive feedback. Spec's "nervous or chemical responses" is missing. Nothing for Mide.
