# Examination — Anaerobic Respiration (anaerobic-respiration) — AQA 8464 4.4.2.1 / 8461 4.4.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.4.2.2-anaerobic-respiration.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Trilogy v1.1, 4.4.2.1, 4.4.2.2), `AQA-8461-spec.txt` (Biology v1.0, 4.4.2.1, 4.4.2.2). Route audit row `anaerobic-respiration` (OK, CF CH TF TH, 4.4.2.1). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q4 = quiz items; "wx n" = `wrong_explanations` key n; T1–T4 = theory blocks. No route copy differs; no `higher` field. No FIFA, no `[NEW — to be examined]` line. **wx alignment checked: all four items correctly paired; no shift.**

**Spec ref:** the file and the site label this lesson 4.4.2.2. The true ref is **4.4.2.1** — AQA covers aerobic and anaerobic respiration in one section (8464 and 8461 alike); 4.4.2.2 is Response to exercise (F5).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.4.2.1** | Aerobic and anaerobic respiration | base |
| 8461 | **4.4.2.1** | Aerobic and anaerobic respiration | base |
| Supporting | 8464/8461 4.4.2.2 Response to exercise (lactic acid, fatigue; HT: liver) | | base + HT |

Spec statements (verbatim, 8464 = 8461): "Respiration in cells can take place aerobically (using oxygen) or anaerobically (without oxygen), to transfer energy." "Students should be able to compare the processes of aerobic and anaerobic respiration with regard to the need for oxygen, the differing products and the relative amounts of energy transferred." "Anaerobic respiration in muscles is represented by the equation: glucose → lactic acid. As the oxidation of glucose is incomplete in anaerobic respiration much less energy is transferred than in aerobic respiration. Anaerobic respiration in plant and yeast cells is represented by the equation: glucose → ethanol + carbon dioxide. Anaerobic respiration in yeast cells is called fermentation and has economic importance in the manufacture of bread and alcoholic drinks." 4.4.2.2: "During long periods of vigorous activity muscles become fatigued and stop contracting efficiently. (HT only) Blood flowing through the muscles transports the lactic acid to the liver where it is converted back into glucose."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Anaerobic = no O₂; used when O₂ supply short (T1; q3) | base | 4.4.2.1; 4.4.2.2 | all four | OK |
| R2 | Much less energy (T1, T4; q4) | base (relative); ATP numbers off-spec | 4.4.2.1 | all four | OK / OFF-SPEC (F1) |
| R3 | Muscles: glucose → lactic acid; incomplete breakdown (T2; equations) | base | 4.4.2.1 | all four | OK |
| R4 | Lactic acid → fatigue (T2; key_note) | base | 4.4.2.2 | all four | OK (GCSE convention) |
| R5 | Lactic acid to liver → glucose (T2 last line) | **higher** | 4.4.2.2 (HT only) | all four | ROUTE (F2) |
| R6 | Yeast/plants: glucose → ethanol + CO₂; fermentation (T3; equations; q1) | base | 4.4.2.1 | all four | OK; naming imprecise (F4) |
| R7 | Bread, alcoholic drinks (T3; q2) | base | 4.4.2.1 | all four | OK; "fizzy drinks" imprecise (F3) |
| R8 | Biofuels (T3) | off-spec (context) | — | all four | OK |
| R9 | Comparison table (T4) | base | 4.4.2.1 | all four | OK; omits plants (F4) |
| R10 | q1–q3 | base | 4.4.2.1; 4.4.2.2 | all four | OK |
| R11 | q4 (ATP per glucose) | off-spec construct | 4.4.2.1 | all four | OFF-SPEC (F1) |
| — | RP, FIFA, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | anaerobic = without oxygen; when O₂ in short supply | OK | — | 4.4.2.1; 4.4.2.2 |
| C2 | T1 | starts with glucose | OK | — | 4.4.2.1 |
| C3 | T1; T4; key_note; q3 wx1; q4 | ~2 ATP vs ~36(–38) | OFF-SPEC | ATP not on 8461/8464; 36–38 is outdated (~30–32). Spec: "much less energy is transferred". | 4.4.2.1 |
| C4 | T1 | different waste products by organism; short-term | OK | — | 4.4.2.1 |
| C5 | T2 | muscles (and some bacteria): glucose → lactic acid | OK | Bacteria true (lactic acid bacteria), off-spec. | 4.4.2.1 |
| C6 | T2 | lactic acid = incomplete breakdown product | OK | Spec: "oxidation of glucose is incomplete". | 4.4.2.1 |
| C7 | T2 | lactic acid lowers pH → enzymes disrupted → burning, fatigue | OK (GCSE convention) | AQA credits "lactic acid build-up → fatigue"; spec's own wording: "long periods of vigorous activity … muscles become fatigued and stop contracting efficiently". | 4.4.2.2 |
| C8 | T2 | lactic acid to liver → glucose (or respired aerobically) | OK, **HT** | HT only; served on all routes (F2). "Respired aerobically" true, off-spec. | 4.4.2.2 (HT only) |
| C9 | T3 | yeast and plants (waterlogged): glucose → ethanol + CO₂ | OK | — | 4.4.2.1 |
| C10 | T3 | "This process is called FERMENTATION" (after yeast and plants) | IMPRECISE | Spec reserves "fermentation" for yeast cells. | 4.4.2.1 |
| C11 | T3 | bread: CO₂ makes dough rise; ethanol evaporates in baking | OK | — | 4.4.2.1 |
| C12 | T3 | beer (grain), wine (grapes), cider; ethanol accumulates | OK | — | 4.4.2.1 |
| C13 | T3 | "CO₂ also produced → gives fizzy drinks their bubbles" | IMPRECISE | Only some alcoholic drinks (beer, sparkling wine, cider) get fizz from fermentation; soft drinks are carbonated by adding CO₂. | — |
| C14 | T3 | bioethanol biofuel | OK (off-spec) | — | — |
| C15 | T4 | aerobic: O₂ yes; CO₂ + water; mitochondria | OK | — | 4.4.2.1; 4.1.1.2 |
| C16 | T4 | anaerobic (animals): lactic acid; cytoplasm | OK | Cytoplasm off-spec, true. | — |
| C17 | T4 | anaerobic (yeast): ethanol + CO₂ | OK | Plants missing from the row (F4). | 4.4.2.1 |
| C18 | common_mistake | animals → lactic acid; yeast → ethanol + CO₂ | OK | Add plants to the yeast side. | 4.4.2.1 |
| C19 | key_note | as above | OK | — | 4.4.2.1 |
| C20 | equations | glucose → lactic acid; glucose → ethanol + carbon dioxide | OK | Spec wording exactly. | 4.4.2.1 |
| C21 | matching (to be replaced) | five pairs | OK | "~36 ATP" off-spec. | — |
| C22 | q1 key | yeast → ethanol + CO₂ | OK | — | 4.4.2.1 |
| C23 | q1 wx1 | lactic acid is animal muscle | OK | — | 4.4.2.1 |
| C24 | q1 wx2 | glucose and O₂ are reactants of aerobic | OK | — | 4.4.2.1 |
| C25 | q1 wx3 | CO₂ + water = aerobic | OK | — | 4.4.2.1 |
| C26 | q2 key | CO₂ bubbles make dough expand | OK | — | 4.4.2.1 |
| C27 | q2 wx1 | yeast makes CO₂ + ethanol, not O₂; ethanol evaporates | OK | — | — |
| C28 | q2 wx2 | yeast absorbs sugars, not significant water | OK | — | — |
| C29 | q2 wx3 | yeast makes ethanol + CO₂, not lactic acid | OK | Wording "Yeast (not animals)" clunky, accurate. | 4.4.2.1 |
| C30 | q3 key | O₂ not delivered fast enough → anaerobic | OK | Spec: "If insufficient oxygen is supplied anaerobic respiration takes place in muscles". | 4.4.2.2 |
| C31 | q3 wx1 | anaerobic gives far less energy per glucose; not chosen | OK | ATP numbers off-spec. | 4.4.2.1 |
| C32 | q3 wx2 | lungs work harder, still can't keep up | OK | — | 4.4.2.2 |
| C33 | q3 wx3 | glucose from glycogen; "hitting the wall" different | OK | Off-spec aside, true. | 4.5.3.2 |
| C34 | q4 key | "Aerobic — approximately 36–38 ATP compared to 2 ATP" | OFF-SPEC | Answer (aerobic) right; the construct (ATP) and number are off-spec, and 36–38 is outdated. | 4.4.2.1 |
| C35 | q4 wx1 | anaerobic faster per unit time, far less per glucose | OK | True (off-spec nuance). | — |
| C36 | q4 wx2 | different efficiencies | OK | — | — |
| C37 | q4 wx3 | lactic acid retains energy; only ~2 ATP usable | OK | Matches "incomplete oxidation". | 4.4.2.1 |

Count: **0 WRONG**. OFF-SPEC: ATP throughout, q4. IMPRECISE: C10, C13. ROUTE: C8.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q4 | Tests ATP numbers — off-spec and outdated (F1) | **Do not use as written.** Design writes a replacement on "which transfers more energy per glucose, and why (complete vs incomplete oxidation)". |
| q1, q2, q3 | correct, base | Usable on all four routes. |

## 5. Verdict
SOURCE OK WITH FLAGS. All spec science correct. q4 is off-spec (ATP). The liver line is HT and belongs on the HT layer (and properly to Response to exercise). Plants make ethanol + CO₂ too — the comparison must say so. "Fizzy drinks" overreaches. The page ref should read 4.4.2.1. **For Mide:** nothing.
