# Examination — Radioactive Contamination (radioactive-contamination) — AQA 8464 6.4.2.4 / 8463 4.4.2.4
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-16/04-checked-science-source/physics-6.4.2.4-radioactive-contamination.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) §6.4.2.1–6.4.2.4, §6.6.2.3–6.6.2.4 (X-rays); `AQA-8463-spec.txt` (v1.1) §4.4.2.1–4.4.3.3. Equation sheets: none apply. Route audit row `radioactive-contamination` (base / base, OK). Neighbour: batch 5 `radioactive-decay` (properties of α, β, γ; batch 5 flagged the same inverse-square line).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; T1–T3 = theory chunks. No route copies differ; no fifas, no `[NEW — to be examined]` lines.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **6.4.2.4** | Radioactive contamination | base |
| 8463 | **4.4.2.4** | same | base |
| Supporting | 8464 6.4.2.1 / 8463 4.4.2.1 (penetration, range, ionising power) | | base |

Spec statements (verbatim, 8463 = 8464): "Radioactive contamination is the unwanted presence of materials containing radioactive atoms on other materials. The hazard from contamination is due to the decay of the contaminating atoms. The type of radiation emitted affects the level of hazard. Irradiation is the process of exposing an object to nuclear radiation. **The irradiated object does not become radioactive.**" "Students should be able to compare the hazards associated with contamination and irradiation." "Suitable precautions must be taken to protect against any hazard that the radioactive source used in the process of irradiation may present." "Students should understand that it is important for the findings of studies into the effects of radiation on humans to be published and shared with other scientists so that the findings can be checked by peer review." (WS 1.5, 1.6)

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Contamination vs irradiation definitions; source stays with you vs exposure stops (T1; common_mistake; key_note) | base | 6.4.2.4 | all four | OK; X-ray example imprecise (F2) |
| R2 | Irradiated object does not become radioactive | base | 6.4.2.4 | — | **GAP — missing** (F1) |
| R3 | Hazard depends on radiation type: α worst inside, γ (and β) outside (T2; common_mistake; key_note; q1) | base | 6.4.2.4; 6.4.2.1 | all four | OK |
| R4 | DNA damage → mutation → cancer; high dose → cell death (T2) | base | 6.4.2.1 context | all four | OK |
| R5 | Precautions vs contamination: tongs, gloves, ventilation, no eating, sealed containers (T3) | base | 6.4.2.4 | all four | OK |
| R6 | Precautions vs irradiation: distance, shielding, time, dosimeters, lead-lined storage (T3; q2) | base | 6.4.2.4 | all four | OK; inverse-square line off-spec (F3) |
| R7 | Benefits vs risks of medical use (T3) | base (general WS 1.5); medical uses detail = triple 8463 4.4.3.3 | 6.4.2.4 | all four | OK |
| R8 | Peer review of studies of radiation effects on humans | base | 6.4.2.4 (WS 1.6) | — | **GAP — missing** (F1) |
| R9 | q1 (inhaled α emitter) | base | 6.4.2.4 | all four | OK — usable |
| R10 | q2 (radiographer, X-rays) | base (irradiation) | 6.4.2.4; 6.6.2.4 | all four | OK — usable; X-rays not nuclear (F2) |
| — | rp, higher, equations, fifas, examiner_tip | none | — | — | correct |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | contamination = radioactive material deposited on/in a person or object; keeps emitting | OK | Spec: "unwanted presence of materials containing radioactive atoms on other materials". | 6.4.2.4 |
| C2 | T1 | examples: radon inhaled, dust swallowed, material on skin | OK | — | — |
| C3 | T1 | irradiation = exposed to radiation from a source not attached; stops when you move away | OK | — | 6.4.2.4 |
| C4 | T1 | irradiation examples: near a source; "medical X-ray"; radiotherapy | IMPRECISE | The spec defines irradiation as exposure to **nuclear** radiation. An X-ray comes from a machine, not a radioactive source. Better: standing near a gamma source; gamma-sterilised syringes. | 6.4.2.4 |
| C5 | T1 | no statement that the irradiated object does not become radioactive | GAP | A spec sentence and the most common exam point in this section. | 6.4.2.4 |
| C6 | T2 | α worst as internal contaminant: highly ionising, short range, energy deposited in nearby cells | OK | — | 6.4.2.1 |
| C7 | T2 | α on the skin less dangerous — cannot penetrate skin | OK | — | — |
| C8 | T2 | β and γ internal contamination also serious | OK | — | — |
| C9 | T2 | γ most dangerous external; external α relatively safe; β penetrates skin | OK | Mark schemes credit "β and γ are the hazard outside the body". | 6.4.2.1 |
| C10 | T2 | DNA damage, mutations, cancer; acute dose → sickness, cell death; eyes, marrow, gonads sensitive | OK | Last clause beyond spec; true. | — |
| C11 | T3 | contamination precautions (tongs, gloves, ventilation, no eating, sealed containers) | OK | — | 6.4.2.4 |
| C12 | T3 | "DISTANCE — intensity follows inverse square law; doubling distance reduces dose by ¾" | OFF-SPEC / IMPRECISE | Arithmetic is right for a γ point source (¼ remains). Not on the GCSE spec, and α and β are limited by range in air, not by an inverse-square law. Say "further away → lower dose; α and β have a short range in air". | — |
| C13 | T3 | shielding: paper α, aluminium β, lead/concrete γ; time; dosimeters | OK | — | 6.4.2.1; 6.4.2.4 |
| C14 | T3 | dose limits, monitoring, lead-lined storage | OK | — | 6.4.2.4 |
| C15 | T3 | benefits vs risks; risk managed not eliminated | OK | — | WS 1.5 |
| C16 | — | no peer-review statement | GAP | Spec WS 1.6 statement. | 6.4.2.4 |
| C17 | common_mistake | as R1, R3 | OK | — | — |
| C18 | key_note | as above | OK | — | — |
| C19 | matching (to be replaced) | "Medical X-ray — irradiation" | IMPRECISE | As C4. | — |
| C20 | q1 key | inhaled α: highly ionising, energy deposited in nearby lung tissue | OK | — | 6.4.2.4 |
| C21 | q1 opt 2 / wx1 | α does not travel far — short range | OK | Aligned. | 6.4.2.1 |
| C22 | q1 opt 3 / wx2 | dust lodges in the lung, keeps emitting | OK | Aligned. | — |
| C23 | q1 opt 4 / wx3 | radiation type does not change | OK | Aligned. | — |
| C24 | q2 stem/key | radiographer leaves the room (distance + lead-lined wall) | OK | Science right. X-rays are ionising and an irradiation hazard (6.6.2.4), but not nuclear radiation — so it tests irradiation, not this spec's radioactive source. Key grammar "distance and … wall reduces" (reduce). | 6.4.2.4; 6.6.2.4 |
| C25 | q2 opt 2 / wx1 | lead apron doesn't cover all of the body | OK | Aligned. The option's claim "lead blocks all radiation types" is the false belief; wx1 does not name it — acceptable. | — |
| C26 | q2 opt 3 / wx2 | X-rays are not inhaled; irradiation not contamination | OK | Aligned. | — |
| C27 | q2 opt 4 / wx3 | X-rays don't contaminate surfaces | OK | Aligned. | — |

Count: **0 WRONG**. IMPRECISE: C4, C19, C24 (context). OFF-SPEC: C12. GAP: C5, C16.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1 correct and base; q2 correct (X-ray context, not a nuclear source) | Both usable on all four routes. Design should add an item where the irradiation source **is** radioactive and one on "an irradiated object does not become radioactive". |

## 5. Verdict
SOURCE OK WITH FLAGS. The comparison of hazards is sound. Two spec sentences are missing — "the irradiated object does not become radioactive" and peer review — and are added to the source under "Spec core missing". The X-ray examples should give way to a nuclear source; the inverse-square line is off-spec.

**For Mide:** nothing — all settled from the spec.
