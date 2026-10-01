# Examination — Response to Exercise (response-to-exercise) — AQA 8464 4.4.2.2 / 8461 4.4.2.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.4.2.3-response-to-exercise.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.4.2.2; 4.5.3.2), `AQA-8461-spec.txt` (Biology v1.0, 4.4.2.2; 4.5.2.4; 4.5.3.2). Route audit row `response-to-exercise` (OK, CF CH TF TH; "HT layer: lactic acid to liver, oxygen debt"). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n; T1–T4 = theory blocks. No route copy differs; no `higher` field — so every HT point is served on every route. No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all three items correctly paired; no shift.**

**Spec ref:** the file and site label 4.4.2.3; true ref **4.4.2.2** in both specs (F5).

**Oxygen debt — HT check (as asked).** The base paragraph names it: "The incomplete oxidation of glucose causes a build up of lactic acid and creates an oxygen debt." The **definition** of oxygen debt, and lactic acid carried to the liver and converted back to glucose, are the **(HT only)** paragraph. So: the term = base; what it is and how it is repaid = higher.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.4.2.2** | Response to exercise | base + one **(HT only)** paragraph |
| 8461 | **4.4.2.2** | Response to exercise | base + one **(HT only)** paragraph |
| Supporting | 8464/8461 4.5.3.2 (glycogen stored in liver and muscle cells) | | base |

Spec statements (verbatim, 8464 = 8461): "During exercise the human body reacts to the increased demand for energy. The heart rate, breathing rate and breath volume increase during exercise to supply the muscles with more oxygenated blood. If insufficient oxygen is supplied anaerobic respiration takes place in muscles. The incomplete oxidation of glucose causes a build up of lactic acid and creates an oxygen debt. During long periods of vigorous activity muscles become fatigued and stop contracting efficiently." "(HT only) Blood flowing through the muscles transports the lactic acid to the liver where it is converted back into glucose. Oxygen debt is the amount of extra oxygen the body needs after exercise to react with the accumulated lactic acid and remove it from the cells." Skills: "AT 1, 3, 4 Investigations into the effect of exercise on the body" (not a required practical).

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Exercise → more energy demand; more O₂ and glucose (T1) | base | 4.4.2.2 | all four | OK |
| R2 | Heart rate up; breathing rate and depth up (T2; q1; matching) | base | 4.4.2.2 | all four | OK |
| R3 | Stroke volume, vasodilation, blood redistribution (T1, T2) | off-spec | — | all four | OK (true) |
| R4 | Glycogen → glucose in liver and muscles (T2) | base (link) | 4.5.3.2 | all four | OK |
| R5 | Insufficient O₂ → anaerobic → lactic acid; fatigue (T3; key_note) | base | 4.4.2.2 | all four | OK |
| R6 | "creates an oxygen debt" (the term) | base | 4.4.2.2 | all four | OK |
| R7 | Oxygen debt defined; lactic acid → liver → glucose (T3; common_mistake; key_note; matching 5) | **higher** | 4.4.2.2 (HT only) | all four | ROUTE (F1) |
| R8 | EPOC (T3) | off-spec | — | all four | IMPRECISE (F2) |
| R9 | Training adaptations (T4) | off-spec | — | all four | IMPRECISE (F3) |
| R10 | q1 | base | 4.4.2.2 | all four | OK |
| R11 | q2, q3 | **higher** | 4.4.2.2 (HT only) | all four | ROUTE (F1) |
| — | RP | none — "Investigations into the effect of exercise" is an AT skills opportunity, not an RP | 4.4.2.2 | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | muscles need more glucose, more O₂, faster removal of CO₂ and lactic acid | OK | — | 4.4.2.2 |
| C2 | T1 | heart, lungs, blood vessels respond | OK | Vessels off-spec. | — |
| C3 | T2 | heart beats faster and more strongly (stroke volume) | OK | Stroke volume off-spec. | 4.4.2.2 |
| C4 | T2 | more O₂ and glucose delivered, more CO₂ removed | OK | Spec: "to supply the muscles with more oxygenated blood". | 4.4.2.2 |
| C5 | T2 | breathing faster and deeper; maintains alveolar gradients | OK | Spec says "breath volume"; use that phrase too. | 4.4.2.2; 4.2.2.1 |
| C6 | T2 | vasodilation to muscles; reduced flow to gut | OK (off-spec) | True. | — |
| C7 | T2 | "Skin flushes (more blood near surface for cooling)" | OK (off-spec) | Skin vasodilation is thermoregulation, 8461 4.5.2.4 (biology only); off-topic here. | 8461 4.5.2.4 |
| C8 | T2 | glycogen in liver and muscles → glucose | OK | — | 4.5.3.2 |
| C9 | T3 | intense exercise → O₂ not supplied fast enough → anaerobic; glucose → lactic acid | OK | — | 4.4.2.2; 4.4.2.1 |
| C10 | T3 | lactic acid lowers pH, disrupts enzymes, burning, fatigue | OK (GCSE convention) | AQA credits lactic acid → fatigue. | 4.4.2.2 |
| C11 | T3 | "OXYGEN DEBT (also called EPOC …)" | IMPRECISE | EPOC is wider than AQA's oxygen debt (also restores O₂ stores, raised temperature and metabolism). Drop "EPOC". | 4.4.2.2 |
| C12 | T3 | extra O₂ after exercise processes lactic acid; to liver; converted back to glucose; amount = oxygen debt | OK, **HT** | Matches the HT paragraph. | 4.4.2.2 (HT only) |
| C13 | T3 | harder exercise → more lactic acid → bigger debt → longer recovery | OK | — | — |
| C14 | T4 | stronger heart, larger stroke volume, lower resting heart rate | OK (off-spec) | — | — |
| C15 | T4 | more mitochondria, larger glycogen stores, more capillaries | OK (off-spec) | — | — |
| C16 | T4 | "Larger lung capacity" | IMPRECISE | Training does not reliably increase lung capacity; breathing muscles strengthen. Drop. | — |
| C17 | T4 | "Higher red blood cell count … more O₂ carried per litre of blood" | IMPRECISE | Endurance training raises total red cell mass but plasma volume rises too, so O₂ per litre often does not rise. Drop or say "more blood volume". | — |
| C18 | common_mistake | oxygen debt = extra O₂ needed after exercise for lactic acid, not lack of O₂ during | OK, **HT** | — | 4.4.2.2 (HT only) |
| C19 | key_note | exercise → HR, breathing, vasodilation; anaerobic → lactic acid → fatigue; after → oxygen debt → lactic acid → glucose in liver | OK | Last clause HT. | 4.4.2.2 |
| C20 | matching (to be replaced) | five pairs | OK | Pair 5 HT. | 4.4.2.2 |
| C21 | q1 key | deliver more O₂ and glucose, remove CO₂ and lactic acid faster | OK | — | 4.4.2.2 |
| C22 | q1 wx1 | temperature rise is a consequence, not the purpose | OK | — | — |
| C23 | q1 wx2 | new red blood cells take days | OK | — | — |
| C24 | q1 wx3 | O₂ doesn't enter through human skin; skin blood flow is for cooling | OK | Cutaneous uptake is negligible. | — |
| C25 | q2 key | repaying oxygen debt — extra O₂ to convert lactic acid back to glucose in liver | OK, **HT** | — | 4.4.2.2 (HT only) |
| C26 | q2 wx1 | lungs respond to chemical signals; slow as CO₂/lactic acid normalise | OK | Off-spec (brain controls breathing), acceptable. | — |
| C27 | q2 wx2 | "All the oxygen used during exercise was already replaced during exercise" | IMPRECISE | Muddled — oxygen is not "replaced"; it was supplied as used. Key unaffected. | 4.4.2.2 |
| C28 | q2 wx3 | "Lactic acid in the blood does stimulate breathing — but…" | IMPRECISE | Concedes the distractor is partly true; lactic acid does not stimulate the lungs directly. Key unaffected. | — |
| C29 | q3 key | extra O₂ after exercise to convert lactic acid back to glucose in the liver | OK, **HT** | Spec: "to react with the accumulated lactic acid and remove it from the cells". | 4.4.2.2 (HT only) |
| C30 | q3 wx1 | lack of O₂ during exercise causes anaerobic; debt is post-exercise | OK | — | 4.4.2.2 |
| C31 | q3 wx2 | inhaled–used difference ≠ oxygen debt | OK | — | — |
| C32 | q3 wx3 | myoglobin stores O₂; debt is post-exercise recovery | OK (off-spec) | — | — |

Count: **0 WRONG**. ROUTE: HT on all routes (F1). IMPRECISE: C11, C16, C17, C27, C28.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2, q3 | HT content (oxygen debt definition; liver) | **Usable on CH and TH only.** Not on CF/TF. |
| q1 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. All spec science correct. The oxygen-debt definition and the liver conversion are HT and are currently served to Foundation; Foundation keeps the term only ("lactic acid build-up creates an oxygen debt"). EPOC and the training block overreach (two shaky claims). q2's wx2/wx3 are loose but the key is AQA-correct. Ref should read 4.4.2.2. **For Mide:** nothing.
