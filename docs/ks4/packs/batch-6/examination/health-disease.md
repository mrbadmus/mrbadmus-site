# Examination — Health, Disease and Risk Factors (health-disease) — AQA 8464 4.2.2.5–4.2.2.6 / 8461 4.2.2.5–4.2.2.6
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.4-health-disease.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1: 4.2.2.5 Health issues; 4.2.2.6 The effect of lifestyle on some non-communicable diseases; 6.6.2.3 for UV), `AQA-8461-spec.txt` (Biology v1.0, same sections). Route audit row `health-disease` (OK, CF CH TF TH, 4.2.2.5–6). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**Spec reference settled.** The frozen spec field "4.2.4" is the site's internal numbering. The AQA references are **4.2.2.5 Health issues** and **4.2.2.6 The effect of lifestyle on some non-communicable diseases**, identical in 8464 and 8461. No conflict.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T4 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

**wrong_explanations alignment (batch-5 defect check):** all 9 keys in q1–q3 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.2.2.5** | Health issues | base |
| 8464 / 8461 | **4.2.2.6** | The effect of lifestyle on some non-communicable diseases | base |
| Supporting | 4.3.1.1 communicable diseases (pathogens); 4.2.2.7 cancer; 6.6.2.3 (8463 4.6.2.3) UV and skin cancer | | base |

Spec statements (verbatim, 8464 = 8461), 4.2.2.5: "Students should be able to describe the relationship between health and disease and the interactions between different types of disease. Health is the state of physical and mental well-being. Diseases, both communicable and non-communicable, are major causes of ill health. Other factors including diet, stress and life situations may have a profound effect on both physical and mental health. Different types of disease may interact. • Defects in the immune system mean that an individual is more likely to suffer from infectious diseases. • Viruses living in cells can be the trigger for cancers. • Immune reactions initially caused by a pathogen can trigger allergies such as skin rashes and asthma. • Severe physical ill health can lead to depression and other mental illness." Skills: "translate disease incidence information between graphical and numerical forms, construct and interpret frequency tables and diagrams, bar charts and histograms, and use a scatter diagram to identify a correlation between two variables" (MS 2c, 2g, 4a); "principles of sampling as applied to scientific data, including epidemiological data" (MS 2d).
4.2.2.6: "Students should be able to: • discuss the human and financial cost of these non-communicable diseases to an individual, a local community, a nation or globally • explain the effect of lifestyle factors including diet, alcohol and smoking on the incidence of non-communicable diseases at local, national and global levels. Risk factors are linked to an increased rate of a disease. They can be: • aspects of a person's lifestyle • substances in the person's body or environment. A causal mechanism has been proven for some risk factors, but not in others. • The effects of diet, smoking and exercise on cardiovascular disease. • Obesity as a risk factor for Type 2 diabetes. • The effect of alcohol on the liver and brain function. • The effect of smoking on lung disease and lung cancer. • The effects of smoking and alcohol on unborn babies. • Carcinogens, including ionising radiation, as risk factors in cancer. Many diseases are caused by the interaction of a number of factors." Skills: WS 1.4, WS 1.5 ("Interpret data about risk factors for specified diseases"), MS 2c, 2d, 2g, 4a.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Definition of health (T1) | base | 4.2.2.5 | all four | IMPRECISE (F1) |
| R2 | Communicable vs non-communicable; examples (T2; key_note; q1) | base | 4.2.2.5; 4.3.1.1 | all four | OK |
| R3 | Interactions between diseases (T2) | base | 4.2.2.5 | all four | GAP — 3 of 4 spec interactions missing (F2) |
| R4 | Risk factor = increased probability; correlation vs causation (T3; common_mistake; q2) | base | 4.2.2.6 (WS 1.5; MS 2g) | all four | OK |
| R5 | Risk-factor categories: lifestyle, environmental, genetic (T3; q3) | base | 4.2.2.6 | all four | OK |
| R6 | Smoking, alcohol, diet, exercise, obesity, UV → named NCDs (T4) | base | 4.2.2.6; 6.6.2.3 | all four | OK (C14 imprecise) |
| R7 | `higher`: evaluate evidence; correlation ≠ causation; confounding; modifiable vs non-modifiable; large samples | base (WS 1.5, MS 2d, 2g) | 4.2.2.5–6 | CH TH only | ROUTE (F4) |
| R8 | Smoking and alcohol on unborn babies; ionising radiation as carcinogen; human and financial cost; incidence local→global; "other factors … diet, stress and life situations" | base | 4.2.2.5–6 | — (absent) | GAP (F3) |
| R9 | Data skills: scatter diagrams, frequency tables, histograms, sampling | base | 4.2.2.5–6 MS 2c, 2d, 2g, 4a | — (absent) | GAP (F5) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | WHO: "complete physical, mental and social wellbeing — not merely the absence of disease" | IMPRECISE | AQA's definition: "Health is the state of physical and mental well-being." The WHO wording is a fair context line, but "social" is not required and the mark scheme credits physical + mental. | 4.2.2.5 |
| C2 | T2 | communicable = caused by pathogens (bacteria, viruses, fungi, protists), can spread | OK | — | 4.3.1.1 |
| C3 | T2 | examples: influenza, HIV, TB, measles, malaria, salmonella | OK | — | 4.3.1 |
| C4 | T2 | non-communicable: CHD, type 2 diabetes, most cancers, asthma | OK | "Most" cancers is right — some are virus-triggered (4.2.2.5). | 4.2.2.5 |
| C5 | T2 | HIV weakens the immune system → other infections | OK | Spec bullet 1. | 4.2.2.5 |
| C6 | T2 | chemotherapy suppresses immunity → more infections | OK | Instance of bullet 1; chemotherapy itself is off-spec. | 4.2.2.5 |
| C7 | T2 | diabetes increases CVD risk | OK | True; not a spec interaction. | — |
| C8 | T3 | risk factor increases probability, not certainty | OK | Spec: "linked to an increased rate of a disease". | 4.2.2.6 |
| C9 | T3 | correlation vs causation; smoking–lung cancer causal | OK | Spec: "A causal mechanism has been proven for some risk factors, but not in others." | 4.2.2.6 |
| C10 | T3 | lifestyle / environmental / genetic categories | OK | Spec groups: lifestyle; substances in body or environment. Genetic covered by 4.2.2.7. | 4.2.2.6; 4.2.2.7 |
| C11 | T4 | "Non-communicable diseases are increasingly common in wealthy countries" | IMPRECISE (minor) | NCDs are rising worldwide, including low- and middle-income countries; spec asks for local, national and global incidence. | 4.2.2.6 |
| C12 | T4 | smoking → lung, mouth, throat, bladder cancer, CHD, COPD | OK | — | 4.2.2.6 |
| C13 | T4 | alcohol → cirrhosis, liver cancer, mouth cancer, brain damage | OK | Spec: "alcohol on the liver and brain function". | 4.2.2.6 |
| C14 | T4 | "High sugar diet → type 2 diabetes, obesity" | IMPRECISE | Spec link is obesity → type 2 diabetes. Say: a high-energy (sugar/fat) diet with too little exercise → obesity → raised risk of type 2 diabetes. | 4.2.2.6 |
| C15 | T4 | saturated fat → cholesterol → CHD; low fibre → bowel cancer; inactivity; obesity BMI > 30 | OK | — | 4.2.2.6 |
| C16 | T4 | "UV radiation … Causes skin cancer (including melanoma — the most dangerous type)" | OK | Spec: "increase the risk of skin cancer". | 6.6.2.3 |
| C17 | `higher` | evaluating evidence, confounding, modifiable/non-modifiable, large samples | ROUTE | All base (WS 1.5; MS 2d, 2g). | 4.2.2.5–6 |
| C18 | q1 key; wx1–3 | communicable = pathogens, spread; NCDs cannot | OK | — | 4.2.2.5 |
| C19 | q2 key; wx1–3 | red meat / bowel cancer = correlation; causation needs more research | OK | wx2's wording on reverse causation is clumsy but correct. | 4.2.2.6 WS 1.5 |
| C20 | q3 key; wx1–3 | smoking = lifestyle; age, family history, motorway air = not lifestyle | OK | — | 4.2.2.6 |
| C21 | matching (to be replaced) | six disease classifications | OK | — | — |

Count: **0 WRONG**; IMPRECISE: C1, C11, C14; ROUTE: C17; GAP: three spec interactions, unborn babies, ionising radiation, costs, data skills.

## 4. Verdict
SOURCE OK WITH FLAGS. Correct as far as it goes, but it leaves out a good part of the spec core (written out in the source under "Spec core missing"). All three quiz items usable on all routes. Nothing for Mide.
