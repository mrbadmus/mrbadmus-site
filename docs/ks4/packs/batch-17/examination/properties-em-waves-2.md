# Examination — Properties of Electromagnetic Waves 2 and Hazards (properties-em-waves-2) — AQA 8464 6.6.2.3 / 8463 4.6.2.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-17/04-checked-science-source/physics-6.6.2.3-properties-em-waves-2.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.6.2.1–6.6.2.4, §5.9.2 (greenhouse, chemistry); `AQA-8463-spec.txt` (v1.1) §4.6.2.1–4.6.2.4, §4.6.3; `AQA-8462-spec.txt` §4.9.2. Route audit `physics.md` row `properties-em-waves-2`. Batch-3 `types-of-em-waves`, batch-4 `uses-em-waves`, for boundaries.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. Quiz identical on all four routes. `higher` differs: TH copy vs CF/TF copy (identical to each other); CH serves TH's.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.6.2.3** | Properties of electromagnetic waves 2 | base; two lines (HT only) |
| 8463 | **4.6.2.3** | Properties of electromagnetic waves 2 | base; two lines (HT only) |
| Strayed into | 8464 6.6.2.2 (HT) interactions; 8463 4.6.3.1 IR from all bodies (physics only); 8464 5.9.2 / 8462 4.9.2 greenhouse (chemistry) | | |

Spec statements (verbatim, 8464 = 8463): "(HT only) Radio waves can be produced by oscillations in electrical circuits. (HT only) When radio waves are absorbed they may create an alternating current with the same frequency as the radio wave itself, so radio waves can themselves induce oscillations in an electrical circuit. Changes in atoms and the nuclei of atoms can result in electromagnetic waves being generated or absorbed over a wide frequency range. Gamma rays originate from changes in the nucleus of an atom. Ultraviolet waves, X-rays and gamma rays can have hazardous effects on human body tissue. The effects depend on the type of radiation and the size of the dose. Radiation dose (in sieverts) is a measure of the risk of harm resulting from an exposure of the body to the radiation. 1000 millisieverts (mSv) = 1 sievert (Sv). Students will not be required to recall the unit of radiation dose. Students should be able to draw conclusions from given data about the risks and consequences of exposure to radiation. Ultraviolet waves can cause skin to age prematurely and increase the risk of skin cancer. X-rays and gamma rays are ionising radiation that can cause the mutation of genes and cancer."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Hazard rises with frequency (T1; key_note) | base (generalisation) | 6.6.2.3 | all four | OK |
| R2 | Radio/microwave/IR/visible hazards (T1; matching IR) | base context | — (spec lists only UV, X, gamma) | all four | OK as context |
| R3 | UV: sunburn, skin cancer, eye damage; protection (T2; key_note) | base | 6.6.2.3 | all four | OK; premature ageing missing (F4) |
| R4 | X-rays and gamma: ionising → mutation, cancer; dose kept low (T2; key_note; q1) | base | 6.6.2.3 | all four | OK |
| R5 | "Ionising radiation (UV, X-ray, gamma)" (T2; common_mistake) | base | 6.6.2.3 | all four | IMPRECISE (F3) |
| R6 | Gamma from radioactive materials (T2) | base | 6.6.2.3 ("from changes in the nucleus") | all four | OK, incomplete (F4) |
| R7 | Changes in atoms and nuclei generate/absorb EM over a wide range | base | 6.6.2.3 | absent | GAP (F4) |
| R8 | Dose in sieverts; 1000 mSv = 1 Sv; conclusions from risk data | base | 6.6.2.3 | absent | GAP (F4) |
| R9 | Radio from oscillating circuits; absorbed → AC same frequency (T3; key_note; `higher` TH; CF/TF copy) | **higher** | 6.6.2.3 (HT only) | all four (T3 as base; CF/TF copy on Foundation) | ROUTE (F5) |
| R10 | Absorb / transmit / reflect / refract summary (T3) | higher — home `properties-em-waves-1` | 6.6.2.2 (HT only) | all four | ROUTE (F5) |
| R11 | `higher` TH: "gamma from nuclear decay, X-rays from electron deceleration, UV from very hot objects, IR from all objects above absolute zero" | mixed | gamma = base 6.6.2.3; IR from all objects = triple 8463 4.6.3.1; X-ray / UV production off-spec | CH TH | ROUTE / OFF-SPEC (F6) |
| R12 | `higher` CF/TF copy: radio (HT); greenhouse effect; climate models | HT on Foundation; greenhouse = chemistry base / physics triple-higher | 6.6.2.3 (HT); 8464 5.9.2; 8463 4.6.3.2 | CF TF | ROUTE (F6) — do not use |
| R13 | q1 — X-rays vs infrared harm | base | 6.6.2.3 | all four | OK |
| R14 | q2 — which part of sunlight damages DNA | base | 6.6.2.3 | all four | wx1 WRONG (F1) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | hazard depends on frequency (energy per photon); higher f = more energy = more potentially harmful | OK | "Photon" is beyond the spec; fine as context. | 6.6.2.3 |
| C2 | T1 | radio/microwave low risk; microwaves can heat tissue; mobile phones no confirmed harm at normal levels | OK | Context. | — |
| C3 | T1 | IR absorbed by skin → burns at high intensity; thermal cameras | OK | Context (6.6.2.4 cameras). | — |
| C4 | T1 | intense visible light can damage the retina | OK | Context. | — |
| C5 | T2 | UV: sunburn; skin cancer via DNA damage; eye damage (cataracts, photokeratitis); sunscreen, sunglasses | OK | Missing the spec's "cause skin to age prematurely". | 6.6.2.3 (F4) |
| C6 | T2 | X-rays penetrate soft tissue, absorbed by bone/metal; imaging; "Can IONISE cells — damage DNA → cancer risk"; dose minimised | OK / IMPRECISE (minor) | Ionise atoms (in cells), not "cells". | 6.6.2.3 |
| C7 | T2 | gamma highest energy, most penetrating, most ionising (of the EM spectrum); from radioactive materials; sickness at high dose, cancer at lower; radiotherapy | OK | "Most ionising" compares EM types only (alpha is more ionising). Spec: "originate from changes in the nucleus". | 6.6.2.3 |
| C8 | T2 last line; common_mistake | "Ionising radiation (UV, X-ray, gamma)"; "UV, X-rays and gamma rays are all IONISING" | IMPRECISE | The spec names only X-rays and gamma as ionising; it gives UV its own effects (premature skin ageing, skin cancer). Most UV reaching the skin damages DNA directly, not by ionising. Teach to the spec. | 6.6.2.3 (F3) |
| C9 | T3 | radio from AC in a transmitter aerial; f(wave) = f(oscillation) | OK (HT) | — | 6.6.2.3 (HT) |
| C10 | T3 | absorbed by aerial → AC at same frequency; receivers | OK (HT) | — | 6.6.2.3 (HT) |
| C11 | T3 | absorbed / transmitted / reflected / refracted; depends on wavelength and material | OK (HT) | Belongs to 6.6.2.2 (HT) on `properties-em-waves-1`. | (F5) |
| C12 | `higher` TH | radio production and induction | OK | HT. | 6.6.2.3 (HT) |
| C13 | `higher` TH | "gamma from nuclear decay" | OK, but base not HT | — | 6.6.2.3 (F6) |
| C14 | `higher` TH | "X-rays from electron deceleration" | OFF-SPEC | True (bremsstrahlung), not on spec. | (F6) |
| C15 | `higher` TH | "UV from very hot objects" | OFF-SPEC / IMPRECISE | Very hot objects do emit UV; the spec says only "changes in atoms… generated… over a wide frequency range". | (F6) |
| C16 | `higher` TH | "IR from all objects above absolute zero" | OK, but triple not HT | "All bodies (objects), no matter what temperature, emit and absorb infrared radiation." | 8463 4.6.3.1 (physics only) (F6) |
| C17 | `higher` CF/TF | radio production/induction "used in radio reception" | OK science; ROUTE | HT content on Foundation routes. | 6.6.2.3 (HT) (F6) |
| C18 | `higher` CF/TF | greenhouse effect: IR absorption and re-emission; climate models and predictions | ROUTE | Not this section. Chemistry base (8464 5.9.2.1–5.9.2.2); physics triple-higher (8463 4.6.3.2) on `radiation-balance-temperature`. | (F6) |
| C19 | key_note | hazards increase with frequency; IR burns; UV sunburn, skin cancer, eye; X-ray ionising; gamma most ionising; radio clause; "Ionising radiation damages DNA → mutations" | OK | Radio clause HT. | 6.6.2.3 |
| C20 | q1 key | X-rays ionising — remove electrons, damage DNA; IR only heats | OK | — | 6.6.2.3 |
| C21 | q1 opt 2 / wx1 | all EM same speed in vacuum; speed irrelevant | OK | Aligned. | 6.6.2.1 |
| C22 | q1 opt 3 / wx2 | penetration a factor, ionisation the reason | OK | Aligned. | — |
| C23 | q1 opt 4 / wx3 | X-rays shorter λ, higher f, more energy | OK | Aligned. | 6.6.2.1 |
| C24 | q2 key | UV damages skin-cell DNA, causing mutations | OK | — | 6.6.2.3 |
| C25 | q2 opt 2 / wx1 | "Infrared causes thermal effects (sunburn/heat) — but DNA damage specifically comes from UV ionising radiation." | **WRONG** | Sunburn is caused by UV, not infrared (the source's own theory 2 says so). It also calls UV "ionising" (F3). Correct wx1: "Infrared from the Sun warms your skin, but it does not damage DNA. Sunburn and the DNA damage that can lead to skin cancer are caused by ultraviolet." | 6.6.2.3 (F1) |
| C26 | q2 opt 3 / wx2 | visible light can damage eyes, not skin DNA significantly | OK | Aligned. | — |
| C27 | q2 opt 4 / wx3 | UV specifically; SPF sunscreens block UV | OK | Aligned. | — |
| C28 | matching (to be replaced) | four hazard pairs | OK | IR row context only. | — |

Count: **1 WRONG** (q2 wx1); **IMPRECISE**: C6 (minor), C8, C15; **OFF-SPEC**: C14, C15; **ROUTE**: T3 radio and both `higher` copies; **GAP**: atoms/nuclei, dose and sieverts, data conclusions, premature ageing. No calculations in the source; the spec's mSv ↔ Sv conversion is missing.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | wx1 says infrared causes sunburn | **Do not use as written** (F1). Usable on all four routes with wx1 replaced. |
| `higher` CF/TF copy | HT content on Foundation; greenhouse/climate belong elsewhere | Do not use (F6). |
| `higher` TH | only the radio sentence is this section's HT | Use the radio sentence only (F6). |
| q1 | none | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Radiation" means "ionising" — microwaves and radio from phones treated as cancer-causing.
- "Sunburn is caused by the heat (infrared) of the Sun."
- "X-rays are dangerous because they are fast / penetrating" — the mark is for ionising → mutation → cancer.
- Dose read as amount of radiation emitted rather than risk of harm; mSv and Sv mixed up when comparing data.
- "UV is ionising like X-rays" — on AQA's spec, UV = premature skin ageing + skin cancer risk; X-rays and gamma = ionising.

**Command words**: Give (one effect), Explain (why harmful), Use the data / Draw a conclusion, Compare (doses), Evaluate (risk vs benefit).

**Typical questions** ⚑ examiner-drafted
- *Give two effects of ultraviolet radiation on the skin. [2]* — ages skin prematurely (1); increases the risk of skin cancer (1).
- *Explain why X-rays can cause cancer. [2]* — ionising (1); cause mutation of genes / damage DNA (1).
- *A CT scan gives a dose of 8 mSv; a chest X-ray 0.02 mSv. How many chest X-rays give the same dose as one CT scan? [2]* — 8 ÷ 0.02 (1) = 400 (1).
- *(HT) Describe how radio waves produce a signal in a receiving aerial. [2]* — radio waves are absorbed (1); create an alternating current with the same frequency as the wave (1).

**Required practical**: none.

**Equations**: none. Conversion 1000 mSv = 1 Sv (given in the spec; not on the equation sheet; unit not required to be recalled).

**Boundaries**: interaction with matter → `properties-em-waves-1`; uses → `uses-em-waves`; spectrum order → `types-of-em-waves`; greenhouse → chemistry `greenhouse-gases` and `radiation-balance-temperature` (TH).

## 6. Verdict
SOURCE HAS ERRORS. q2's wx1 blames infrared for sunburn (q2 not usable as written). The source labels UV ionising, against the spec's wording. Large spec gaps: atoms and nuclei generating EM, radiation dose in sieverts and drawing conclusions from risk data, and UV's premature ageing. The radio content (the section's only HT) is taught as base, and both `higher` copies stray — the CF/TF copy puts HT radio and chemistry's greenhouse/climate content on Foundation routes.

**For Mide:** none — UV is settled by the spec's own wording (F3).
