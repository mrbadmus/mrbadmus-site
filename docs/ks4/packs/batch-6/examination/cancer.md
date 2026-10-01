# Examination — Cancer (cancer) — AQA 8464 4.2.2.7 / 8461 4.2.2.7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.4.1-cancer.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1: 4.2.2.7 Cancer; 4.2.2.5–6 for risk factors and virus-triggered cancers; 6.6.2.3 for UV, X-rays, gamma), `AQA-8461-spec.txt` (Biology v1.0, same sections). Route audit row `cancer` (OK, CF CH TF TH, 4.2.2.7). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**Spec reference settled.** The frozen spec field "4.2.4.1" is the site's internal numbering. The AQA reference is **4.2.2.7 Cancer** in both 8464 and 8461. No conflict.

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T4 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

**wrong_explanations alignment (batch-5 defect check):** all 9 keys in q1–q3 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.2.2.7** | Cancer | base |
| Supporting | 4.2.2.5 ("Viruses living in cells can be the trigger for cancers"); 4.2.2.6 ("Carcinogens, including ionising radiation, as risk factors in cancer"; smoking → lung cancer); 8464 6.6.2.3 / 8463 4.6.2.3 (UV → skin cancer; X-rays and gamma → mutation and cancer) | | base |

Spec statements (verbatim, 8464 = 8461), 4.2.2.7: "Students should be able to describe cancer as the result of changes in cells that lead to uncontrolled growth and division. Benign tumours are growths of abnormal cells which are contained in one area, usually within a membrane. They do not invade other parts of the body. Malignant tumour cells are cancers. They invade neighbouring tissues and spread to different parts of the body in the blood where they form secondary tumours. Scientists have identified lifestyle risk factors for various types of cancer. There are also genetic risk factors for some cancers."
6.6.2.3 (supporting): "Ultraviolet waves can cause skin to age prematurely and increase the risk of skin cancer. X-rays and gamma rays are ionising radiation that can cause the mutation of genes and cancer."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Cancer = uncontrolled cell division from mutations; tumour (T1; key_note) | base | 4.2.2.7 | all four | OK |
| R2 | Benign vs malignant; spread in blood; secondary tumours (T2; common_mistake; q1; matching) | base | 4.2.2.7 | all four | OK (C5 imprecise) |
| R3 | Lifestyle risk factors (T3) | base | 4.2.2.7; 4.2.2.6 | all four | OK |
| R4 | Environmental: UV, ionising radiation, asbestos, chemicals (T3; q2) | base | 4.2.2.6; 6.6.2.3 | all four | OK (C9 imprecise) |
| R5 | Genetic risk factors, BRCA1/2 (T3) | base | 4.2.2.7 | all four | OK |
| R6 | Viral triggers: HPV, hepatitis B/C (T3) | base | 4.2.2.5 | all four | OK |
| R7 | Treatment: surgery, radiotherapy, chemotherapy and side effects (T4; summary; key_note; common_mistake; q3) | **OFF-SPEC** | — (not in 4.2.2.7; radiotherapy is 8463 4.4.3.3 physics only) | all four | context only (F2) |
| R8 | `higher`: benign/malignant, risk factors, chemo/radiotherapy side effects | base / OFF-SPEC | 4.2.2.7 | CH TH only | ROUTE (F1) |
| — | RP, equations, FIFA | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | cancer = uncontrolled cell division | OK | Spec: "changes in cells that lead to uncontrolled growth and division". | 4.2.2.7 |
| C2 | T1 | mutations in genes regulating the cell cycle; stop signals ignored | OK | Beyond spec, consistent with it. | 4.2.2.7 |
| C3 | T2 | benign: slow, one place, capsule, does not invade or spread, usually not life-threatening, can press on structures | OK | Spec: "contained in one area, usually within a membrane". | 4.2.2.7 |
| C4 | T2 | malignant: invades neighbouring tissues, cells break away, travel in blood or lymph | OK | Spec says blood; lymph is a correct extra. | 4.2.2.7 |
| C5 | T2; key_note; common_mistake | "form NEW TUMOURS — this spread is called METASTASIS" | IMPRECISE | Spec term is **secondary tumours**; "metastasis" is beyond spec. Teach "secondary tumours" as the term to write. | 4.2.2.7 |
| C6 | T3 | smoking: lung, mouth, throat, bladder; carcinogens in smoke damage DNA | OK | — | 4.2.2.6 |
| C7 | T3 | alcohol, obesity, poor diet links | OK | — | 4.2.2.6–7 |
| C8 | T3 | UV damages DNA in skin cells; ionising radiation damages DNA | OK | — | 6.6.2.3; 4.2.2.6 |
| C9 | T3 | "Asbestos — fibres lodge in lung tissue and damage cells → mesothelioma (lung cancer)" | IMPRECISE | Mesothelioma is cancer of the lining around the lungs (pleura) or abdomen, not lung cancer; asbestos also raises lung-cancer risk. Off-spec detail either way. | — |
| C10 | T3 | BRCA1/2 inherited mutations in tumour suppressor genes raise breast/ovarian risk | OK | Spec: "genetic risk factors for some cancers". | 4.2.2.7 |
| C11 | T3 | HPV causes most cervical cancer; hepatitis B and C → liver cancer | OK | Spec: "Viruses living in cells can be the trigger for cancers." | 4.2.2.5 |
| C12 | T4 | surgery, radiotherapy (gamma/X-rays damage DNA), chemotherapy (rapidly dividing cells) and side effects | OFF-SPEC | Science correct; not in 4.2.2.7 on either spec. | — |
| C13 | key_note | "radiotherapy (gamma rays)" | IMPRECISE (minor) | Most radiotherapy uses high-energy X-rays; gamma is also used. Off-spec anyway. | — |
| C14 | `higher` | as R8 | ROUTE | No HT in 4.2.2.7. | 4.2.2.7 |
| C15 | q1 key; wx1–3 | benign stays, malignant spreads; wx1 malignant faster; wx2 both causes; wx3 surgery/chemo | OK | wx3 mentions treatment (off-spec) but only to rebut; usable. | 4.2.2.7 |
| C16 | q2 key; wx1, wx3 | UV damages DNA → mutations in division-control genes | OK | — | 6.6.2.3 |
| C17 | q2 wx2 | "UV radiation doesn't work by heat — it carries photons that directly interact with and damage DNA" | IMPRECISE (minor) | UV *is* photons; "carries photons" is loose. Meaning is right; usable. | — |
| C18 | q3 key; wx1–3 | chemotherapy damages all rapidly dividing cells → hair loss | OFF-SPEC | Science correct; the item tests treatment, which is not on 4.2.2.7. | — |
| C19 | matching (to be replaced) | benign / malignant / both pairs | OK | "Both — caused by uncontrolled cell division due to gene mutation" is right. | 4.2.2.7 |

Count: **0 WRONG**; IMPRECISE: C5, C9, C13, C17; OFF-SPEC: C12, C18 (treatment, q3); ROUTE: C14.

## 4. Verdict
SOURCE OK WITH FLAGS. The spec core (benign/malignant, secondary tumours, lifestyle and genetic risk) is present and correct. The treatment section and q3 are off-spec. q1 and q2 usable on all routes. Nothing for Mide.
