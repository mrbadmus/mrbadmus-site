# Examination — Factors Affecting Food Security (factors-affecting-food-security) — AQA 8461 4.7.5.1 (biology only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.7.5.1-factors-affecting-food-security.md`.
Spec sources read as text: `AQA-8461-spec.txt` (Biology v1.0, 4.7.5 Food production (biology only): 4.7.5.1–4.7.5.4; 4.7.4.3 transfer of biomass), `AQA-8464-spec.txt` (checked: 4.7.5 is absent from Combined Trilogy). Route audit row `factors-affecting-food-security` (OK, TF TH, 8461 4.7.5.1 (biology only)). Runtime convention checked in `generate_site_v5.py` (`render_quiz`): `wrong_explanations` key n is shown for `opts[n]` (0-based; opt 0 is the key).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. Only `higher` has a route copy (TF = null). No `[NEW — to be examined]` lines (no FIFA). **wx alignment checked: both items correctly paired (wx n rebuts opt n); no one-option-late shift.**

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8461 | **4.7.5.1** | Factors affecting food security | biology only (heading 4.7.5 "Food production (biology only)") |
| 8464 | — | not in Combined Trilogy | — |
| Supporting | 8461 4.7.4.3 Transfer of biomass (base) — why meat is inefficient; 4.7.5.2 Farming techniques, 4.7.5.4 Role of biotechnology (biology only) — the "solutions" | | base / triple |

Spec statements (8461 4.7.5.1, verbatim): "Students should be able to describe some of the biological factors affecting levels of food security. Food security is having enough food to feed a population. Biological factors which are threatening food security include: the increasing birth rate has threatened food security in some countries; changing diets in developed countries means scarce food resources are transported around the world; new pests and pathogens that affect farming; environmental changes that affect food production, such as widespread famine occurring in some countries if rains fail; the cost of agricultural inputs; conflicts that have arisen in some parts of the world which affect the availability of water or food. Sustainable methods must be found to feed all people on Earth." Skills: "WS 1.4 Interpret population and food production statistics to evaluate food security."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Food security = enough food to feed a population; access, affordability, distribution (T1; common_mistake; key_note) | triple | 8461 4.7.5.1 | TF TH | OK |
| R2 | Increasing birth rate (T2.1; key_note) | triple | 4.7.5.1 | TF TH | OK |
| R3 | Changing diets in developed countries; scarce food transported around the world (T2.2) | triple | 4.7.5.1 | TF TH | OK |
| R4 | Meat less efficient than plant food (T2.2; q1) | triple (uses base 4.7.4.3 biomass loss) | 4.7.5.1 + 4.7.4.3 | TF TH | OK (IMPRECISE framing, F3) |
| R5 | New pests and pathogens (T2.3; q2 key) | triple | 4.7.5.1 | TF TH | OK |
| R6 | Environmental change, climate, rains failing (T2.4) | triple | 4.7.5.1 | TF TH | OK; spec's example missing (F4) |
| R7 | Conflict (T2.5) | triple | 4.7.5.1 | TF TH | OK |
| R8 | Cost of agricultural inputs (T2.6) | triple | 4.7.5.1 | TF TH | OK |
| R9 | Solutions: high-yield / GM crops, irrigation, fertilisers, waste, diets, distribution (T3) | triple (context; owned by 4.7.5.2 / 4.7.5.4) | 8461 4.7.5.1 "sustainable methods"; 4.7.5.2; 4.7.5.4 | TF TH | OK as context |
| R10 | Interpret population and food production statistics (`higher` field: "Evaluate … using data") | **triple** (no HT label) | 8461 4.7.5.1 WS 1.4 | TH only (TF copy null) | **ROUTE** (F2) |
| R11 | `higher` remainder: ethics of solutions, production vs biodiversity trade-offs, global distribution | not in 4.7.5.1 (enrichment; links 4.7.5.2 WS 1.3, 4.7.3) | — | TH only | OK as enrichment; not examinable here |
| R12 | q1 | triple | 4.7.5.1 + 4.7.4.3 | TF TH | usable |
| R13 | q2 | triple | 4.7.5.1 | TF TH | **WRONG** (F1) |
| — | equations, FIFA, RP | none | — | — | correct: 4.7.5.1 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | food security = enough food to feed a population | OK | Spec definition. | 4.7.5.1 |
| C2 | T1 | access to sufficient, safe and nutritious food | OK | FAO definition; beyond spec, true. | — |
| C3 | T1 | insecurity: too little produced, unequal distribution, unaffordable | OK | — | — |
| C4 | T1 | world population over 8 billion and growing | OK | Passed 8 billion Nov 2022 (UN). | — |
| C5 | T2.1 | increasing birth rate → more food needed | OK | — | 4.7.5.1 |
| C6 | T2.2 | developed diets shift to more meat/dairy; meat needs more land, water, grain | OK | Biomass lost at each trophic level. | 4.7.4.3 |
| C7 | T2.2 | scarce food resources transported around the world | OK | Spec's own wording. | 4.7.5.1 |
| C8 | T2.3 | wheat rust (fungus), blight (oomycete), foot-and-mouth in cattle | OK | Potato blight *Phytophthora* is an oomycete ✓; foot-and-mouth is viral. | — |
| C9 | T2.3 | trade and travel spread pests faster | OK | — | — |
| C10 | T2.4 | climate change changes rainfall, temperature, seasons; sea level; floods, droughts | OK | Spec example "widespread famine … if rains fail" not used — F4. | 4.7.5.1 |
| C11 | T2.5 | war and instability disrupt farming and distribution | OK | Spec: "conflicts … which affect the availability of water or food". | 4.7.5.1 |
| C12 | T2.6 | fertilisers, pesticides, machinery expensive | OK | = spec's "cost of agricultural inputs". | 4.7.5.1 |
| C13 | T2 heading | "Biological Factors Threatening Food Security" over all six | OK | The spec itself files conflict and cost under "biological factors". | 4.7.5.1 |
| C14 | T3 | high-yield, GM, irrigation, fertilisers, pesticides, intensive farming, waste, plant diets, insect farming, aid | OK | All true; insect farming converts feed to protein more efficiently than livestock ✓. | 4.7.5.2, 4.7.5.4 |
| C15 | `higher` | evaluate threats using data; ethics; trade-offs | ROUTE | Data interpretation is triple, not HT — F2. | WS 1.4 |
| C16 | common_mistake | food security is about having enough, not just producing; distribution and access matter | OK | — | 4.7.5.1 |
| C17 | key_note | summary list | OK | — | — |
| C18 | q1 stem | "shift towards more meat-based diets in **developing** countries" | IMPRECISE | Spec names "changing diets in **developed** countries". The science in the key holds either way; usable. F3. | 4.7.5.1 |
| C19 | q1 key | meat far less efficient — more land, water, grain per unit nutrition | OK | — | 4.7.4.3 |
| C20 | q1 wx1 (opt 1 "fewer nutrients") | meat is nutritious; problem is inefficiency | OK | Paired correctly. | — |
| C21 | q1 wx2 (opt 2 "spoils faster") | primary concern is land and resource use | OK | Paired correctly. | — |
| C22 | q1 wx3 (opt 3 "reduce birth rates") | not linked; resource efficiency | OK | Paired correctly. | — |
| C23 | q2 key | new pathogen destroying wheat = biological factor | OK | — | 4.7.5.1 |
| C24 | q2 opt 2 / wx2 | "Rising fuel costs …" — "an ECONOMIC factor — not biological" | **WRONG** | The spec's own list of biological factors includes "the cost of agricultural inputs" (fuel for farm machinery is one). A pupil who learnt the spec list is marked wrong. | 4.7.5.1 |
| C25 | q2 opt 3 / wx3 | "Political instability preventing farmers from accessing markets" — "POLITICAL/SOCIAL factor — not biological" | **WRONG** | The spec lists "conflicts … which affect the availability of water or food" as a biological factor. Contradicts the spec and the page's own T2.5. | 4.7.5.1 |
| C26 | q2 opt 1 / wx1 | trade tariffs = economic/political | OK in isolation | Not on the spec list; but see F1 — the item's premise (biological vs economic/political) is not the spec's distinction. | — |
| C27 | matching (to be replaced) | four threat–description pairs | OK | — | 4.7.5.1 |

Count: **1 WRONG item** (q2: C24, C25); IMPRECISE: C18. Theory, common_mistake and key_note: no errors.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Two distractors are on the spec's own list of "biological factors", and their explanations say they are not biological. | **Do not use as written** (F1). Rebuild with distractors that are not threats at all. |
| q1 | Correct; stem says "developing" where the spec says "developed". | Usable on TF and TH. |

## 5. Verdict
SOURCE OK WITH FLAGS. The theory is accurate and covers all six spec factors. q2 contradicts the spec's list (cost of inputs and conflict are named as biological factors) and is not usable. The `higher` field's data-evaluation skill is triple, not HT, so belongs on TF too. Nothing for Mide.
