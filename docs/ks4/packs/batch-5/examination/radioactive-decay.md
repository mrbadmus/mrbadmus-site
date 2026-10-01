# Examination — Radioactive Decay and Nuclear Radiation (radioactive-decay) — AQA 8464 6.4.2.1 / 8463 4.4.2.1
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/physics-6.4.2.1-radioactive-decay.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.4.2.1–6.4.2.4; `AQA-8463-spec.txt` (v1.1) §4.4.2.1–4.4.2.4, 4.4.3.1–4.4.3.3. Equation sheets: none apply. Route audit row `radioactive-decay` (base / base, OK). Site lessons that neighbour this one: `uses-of-nuclear-radiation` (TF TH), `radioactive-contamination` (CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. No route copies differ; no `[NEW — to be examined]` lines (no fifas).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.4.2.1** | Radioactive decay and nuclear radiation | base |
| 8463 | **4.4.2.1** | same | base |
| Supporting | 8464 6.4.2.4 / 8463 4.4.2.4 (irradiation; precautions) | | base |
| Layer | 8463 **4.4.3.3** Uses of nuclear radiation (medical) | | physics only |

Spec statements (verbatim, 8463 = 8464): "Some atomic nuclei are unstable. The nucleus gives out radiation as it changes to become more stable. This is a random process called radioactive decay. Activity is the rate at which a source of unstable nuclei decays. Activity is measured in becquerel (Bq). Count-rate is the number of decays recorded each second by a detector (eg Geiger-Muller tube). The nuclear radiation emitted may be: an alpha particle (α) – this consists of two neutrons and two protons, it is the same as a helium nucleus; a beta particle (β) – a high speed electron ejected from the nucleus as a neutron turns into a proton; a gamma ray (γ) – electromagnetic radiation from the nucleus; a neutron (n)." "Required knowledge of the properties of alpha particles, beta particles and gamma rays is limited to their penetration through materials, their range in air and ionising power." "Students should be able to apply their knowledge to the uses of radiation and evaluate the best sources of radiation to use in a given situation." 8463 4.4.3.3 (physics only): "Nuclear radiations are used in medicine for the: exploration of internal organs; control or destruction of unwanted tissue."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Unstable nuclei; random decay (T1; key_note) | base | 6.4.2.1 | all four | OK |
| R2 | Activity in Bq; count-rate by GM tube (T1; q2) | base | 6.4.2.1 | all four | OK in theory; q2 conflates (F2) |
| R3 | α, β, γ composition (T1, T2) | base | 6.4.2.1 | all four | GAP — neutron, β mechanism (F3) |
| R4 | Penetration, range in air, ionising power (T2; common_mistake; key_note; matching; q1) | base | 6.4.2.1 | all four | OK (wording — F6) |
| R5 | Uses: smoke detector, paper thickness, sterilising/food irradiation, industrial gauges/leak tracing (T3) | base | 6.4.2.1 (apply to uses); 6.4.2.4 | all four | OK |
| R6 | Medical: gamma imaging, radiotherapy (T3; key_note "cancer treatment") | **triple** | 8463 4.4.3.3 (physics only) | all four | **ROUTE** (F4) |
| R7 | Damage to cells; α worst inside, γ worst outside (T3; common_mistake; q1) | base | 6.4.2.1; 6.4.2.4 | all four | OK |
| R8 | Protection: distance, shielding, time, dosimeters (T3) | base | 6.4.2.4 | all four | "inverse square law" off-spec (F5) |
| — | rp, higher, equations, fifas | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | unstable nuclei emit radiation to become more stable; random | OK | — | 6.4.2.1 |
| C2 | T1 | activity = rate of decay, Bq; 1 Bq = 1 decay per second | OK | — | 6.4.2.1 |
| C3 | T1 | count rate = decays recorded per second by a detector | OK | — | 6.4.2.1 |
| C4 | T1 | three main types α, β, γ | GAP | Spec lists a fourth: a neutron (n). | 6.4.2.1 |
| C5 | T1, T2 | β = fast electron from the nucleus | IMPRECISE | Spec: "a high speed electron ejected from the nucleus as a neutron turns into a proton". | 6.4.2.1 |
| C6 | T2 | α: 2p + 2n, ⁴₂He, charge +2, "Mass: 4 amu" | IMPRECISE | "Relative mass 4"; "amu" not AQA's term. | 6.4.2.1 |
| C7 | T2 | α range a few cm in air; stopped by paper/skin; strongly ionising | OK | — | 6.4.2.1 |
| C8 | T2 | β: ⁰₋₁e, −1, negligible mass; range "a few metres"; stopped by a few mm aluminium; moderately ionising | IMPRECISE (minor) | Range depends on energy; AQA-endorsed texts give about 1 m. "Up to about a metre" is the safer figure. | 6.4.2.1 |
| C9 | T2 | γ: EM wave, charge 0, mass 0; range "effectively unlimited"; reduced by several cm lead / metres concrete; weakly ionising | OK | "Very large range" is the usual wording. | 6.4.2.1 |
| C10 | T2 | GM tube + counter | OK | — | 6.4.2.1 |
| C11 | T3 | smoke detector: α ionises air, current; smoke absorbs α, current drops, alarm | OK | — | 6.4.2.1 (application) |
| C12 | T3 | β paper thickness monitoring | OK | — | 6.4.2.1 |
| C13 | T3 | γ medical imaging, radiotherapy | OK (science) / ROUTE | Physics-only content. | 8463 4.4.3.3 |
| C14 | T3 | γ sterilising equipment, food irradiation | OK | Irradiated object does not become radioactive (6.4.2.4). | 6.4.2.4 |
| C15 | T3 | γ/β industrial gauges, pipeline fault detection | OK | — | — |
| C16 | T3 | ionising radiation damages DNA → mutation → cancer; high dose → cell death, radiation sickness | OK | — | 6.4.2.1; 6.4.2.4 |
| C17 | T3 | α most dangerous inside; γ most dangerous outside; β penetrates skin, absorbed by soft tissue | OK | Mark schemes accept "β and γ are the hazard outside the body". | 6.4.2.4 |
| C18 | T3 | "Distance — inverse square law applies" | OFF-SPEC / IMPRECISE | Not on the GCSE spec; strictly true only for γ from a point source. α and β simply have short ranges in air. | — |
| C19 | T3 | shielding paper/aluminium/lead; time; dosimeters | OK | — | 6.4.2.4 |
| C20 | common_mistake | α most ionising, least penetrating; γ least ionising, most penetrating; α inside, γ outside | OK | — | 6.4.2.1 |
| C21 | key_note | as above; "cancer treatment/sterilisation (γ)" | OK / ROUTE | Cancer treatment = triple layer (C13). | — |
| C22 | matching (to be replaced) | five pairs | OK | — | — |
| C23 | q1 key | α highly ionising, dense damage nearby, cannot escape the body | OK | — | 6.4.2.1 |
| C24 | q1 wx1 | "Alpha does not have the highest energy — gamma photons have very high energies too." | **WRONG** | Alpha particles from common sources carry about 4–9 MeV, usually more than the beta or gamma from common sources (~0.01–3 MeV). Energy is not the reason; ionising power is. | — |
| C25 | q1 wx2 | α slowest; "its high mass means it interacts strongly with matter" | IMPRECISE (minor) | Slowest ✓. Strong interaction is mainly its +2 charge and low speed; not worth a separate flag. | — |
| C26 | q1 wx3 | α least penetrating, stopped by a few cm of air; ionisation deposited nearby | OK | — | 6.4.2.1 |
| C27 | q2 stem | "A Geiger counter measures 340 Bq from a radioactive source." | **WRONG** | A GM tube records count-rate (counts per second), not activity — the spec separates the two, and a detector catches only a fraction of the decays. | 6.4.2.1 |
| C28 | q2 key | 340 nuclei decaying per second | OK only for activity | True if 340 Bq is the source's activity — not what a Geiger counter reads. | 6.4.2.1 |
| C29 | q2 wx1 | "Activity = total number of radioactive atoms remaining, not the rate." | **WRONG** (as written) | Read literally it defines activity as the number of atoms remaining. Intended: "That would be the number of unstable nuclei left; activity is the rate of decay." | 6.4.2.1 |
| C30 | q2 wx2, wx3 | Bq is not joules; not a duration | OK | — | — |

Count: **3 WRONG** (C24 in q1; C27 and C29 in q2); IMPRECISE C5, C6, C8, C25; OFF-SPEC C18; GAP C4; ROUTE C13/C21.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx1 states a false fact (alpha does not have the highest energy) | Do not use as written (RADIOACTIVE-DECAY-F1). Key correct; usable once wx1 is replaced. |
| q2 | stem says a Geiger counter measures Bq; wx1 misdefines activity | Do not use as written (RADIOACTIVE-DECAY-F2). Usable with the corrected stem and wx1. |

## 5. Verdict
SOURCE HAS ERRORS. Theory is sound apart from the missing neutron emission and β mechanism, and medical uses that belong to a physics-only layer. Both frozen quiz items have errors and neither is usable as written.

**For Mide:** nothing — all settled from the spec.
