# Examination — The Digestive System (digestive-system) — AQA 8464 4.2.2.1 / 8461 4.2.2.1
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.2.2.1-digestive-system.md`.
Spec sources read as text: `AQA-8464-spec.txt` (Combined Trilogy v1.1: 4.2.2.1; Required practical activities 3 and 4; 10.2.3; 4.1.3.1 exchange surfaces), `AQA-8461-spec.txt` (Biology v1.0: 4.2.2.1; Required practical activities 4 and 5; 8.2.4; 4.1.3.1). Route audit row `digestive-system` (OK, CF CH TF TH, 4.2.2.1). Sibling lesson on the site: `enzymes` (lock and key, temperature/pH, the amylase-pH RP). Runtime convention checked in `generate_site_v5.py`: `wrong_explanations` key n is shown for `opts[n]`.

**RP numbers settled (looked up, not escalated).** Food tests ("use qualitative reagents to test for a range of carbohydrates, lipids and proteins. To include: Benedict's test for sugars; iodine test for starch; and Biuret reagent for protein.") is **Required practical activity 3 in 8464** (Combined) and **Required practical activity 4 in 8461** (Biology). The frozen label "RP4" is right for Triple only; on Combined, RP4 is the amylase–pH practical. No conflict between AQA sources.

Conventions: q1–q5 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T5 = theory blocks. Route copies identical except `higher`, which is `null` on CF and TF.

**wrong_explanations alignment (batch-5 defect check):** all 15 keys in q1–q5 checked; every key n explains `opts[n]`. No shift.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.2.2.1** | The human digestive system | base |
| 8461 | **4.2.2.1** | The human digestive system | base |
| 8464 | RP3 | Food tests | base |
| 8461 | RP4 | Food tests | base |
| Supporting | 4.1.3.1 (small intestine as an exchange surface — villi); enzymes half of 4.2.2.1 (lock and key, pH/temperature, rate calculations, amylase–pH RP = 8464 RP4 / 8461 RP5) taught in `enzymes` | | base |

Spec statements (verbatim, 8464 = 8461): "The digestive system is an example of an organ system in which several organs work together to digest and absorb food." "Students should be able to recall the sites of production and the action of amylase, proteases and lipases." "Students should be able to understand simple word equations but no chemical symbol equations are required. Digestive enzymes convert food into small soluble molecules that can be absorbed into the bloodstream. Carbohydrases break down carbohydrates to simple sugars. Amylase is a carbohydrase which breaks down starch. Proteases break down proteins to amino acids. Lipases break down lipids (fats) to glycerol and fatty acids. The products of digestion are used to build new carbohydrates, lipids and proteins. Some glucose is used in respiration. Bile is made in the liver and stored in the gall bladder. It is alkaline to neutralise hydrochloric acid from the stomach. It also emulsifies fat to form small droplets which increases the surface area. The alkaline conditions and large surface area increase the rate of fat breakdown by lipase."
RP: "Required practical activity 3 [8461: 4]: use qualitative reagents to test for a range of carbohydrates, lipids and proteins. To include: Benedict's test for sugars; iodine test for starch; and Biuret reagent for protein." AT 2 (8461: AT 2 and 8): "safe use of a Bunsen burner and a boiling water bath".
4.1.3.1 (supporting): "Students should be able to explain how the small intestine and lungs in mammals … are adapted for exchanging materials … The effectiveness of an exchange surface is increased by: having a large surface area; a membrane that is thin, to provide a short diffusion path; (in animals) having an efficient blood supply".

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Large insoluble → small soluble molecules; mechanical vs chemical digestion (T1) | base | 4.2.2.1 | all four | OK |
| R2 | Mouth: teeth, salivary amylase starch → maltose, bolus, peristalsis (T2; q5) | base (KS3-assumed context + sites of production) | 4.2.2.1 | all four | OK |
| R3 | Stomach: HCl pH ~2, pepsin (protease), churning (T3; q3) | base | 4.2.2.1 | all four | OK |
| R4 | Pancreas: amylase, proteases, lipase into small intestine (T4; key_note) | base | 4.2.2.1 | all four | IMPRECISE — small intestine also a site of production (F2) |
| R5 | Bile: liver, gall bladder, alkaline neutralises acid, emulsifies (T4; common_mistake; q1; `higher`) | base | 4.2.2.1 | all four (theory); CH TH (`higher`) | OK; `higher` is base → ROUTE (F1) |
| R6 | Absorption; villi: large SA, thin wall, blood supply (T4; q2; `higher`) | base | 4.1.3.1 | all four (theory); CH TH (`higher`) | OK; ROUTE (F1) |
| R7 | Large intestine absorbs water; rectum, anus (T5; q4) | base (KS3-assumed) | 4.2.2.1 | all four | OK |
| R8 | Food tests RP (rp) | base | 8464 RP3; 8461 RP4 | all four | RP label route-dependent (F3); imprecise (F4) |
| R9 | Carbohydrases → simple sugars; word equations; products of digestion used to build new molecules / glucose for respiration | base | 4.2.2.1 | — (absent) | GAP (F5) |
| R10 | Lock and key, active site, pH/temperature, rate calculations, amylase–pH RP | base | 4.2.2.1 | — | in sibling `enzymes`; link, do not duplicate |
| R11 | `higher`: microvilli | OFF-SPEC (detail) | — | CH TH | harmless; do not assess |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | starch, proteins, fats large and insoluble; digestion → small soluble molecules | OK | Spec: "small soluble molecules that can be absorbed into the bloodstream". | 4.2.2.1 |
| C2 | T1 | mechanical digestion increases surface area for enzymes | OK | — | — |
| C3 | T2 | salivary amylase: starch → maltose | OK | Spec: amylase breaks down starch; carbohydrases → simple sugars. Maltose is fine. | 4.2.2.1 |
| C4 | T2 | mucus, bolus, oesophagus, peristalsis | OK | KS3 context; not assessed at GCSE. | — |
| C5 | T3 | HCl, pH ~2, kills most bacteria, optimum pH for pepsin | OK | — | 4.2.2.1 |
| C6 | T3 | pepsin breaks proteins into shorter chains | OK | Spec end-point: proteases → amino acids (said in T4). | 4.2.2.1 |
| C7 | T3 | chyme; pyloric sphincter | OK | Beyond spec; context only. | — |
| C8 | T4 | pancreatic amylase, proteases, lipase (fats → fatty acids + glycerol) | OK | — | 4.2.2.1 |
| C9 | T4; key_note "Small intestine: all three enzymes from pancreas" | sites of production given as salivary glands, stomach, pancreas only | IMPRECISE | AQA credits the **small intestine** as a site of production of amylase (carbohydrases), proteases and lipase. Sites: amylase — salivary glands, pancreas, small intestine; protease — stomach, pancreas, small intestine; lipase — pancreas, small intestine. | 4.2.2.1 ("recall the sites of production") |
| C10 | T4; common_mistake | bile made in liver, stored in gall bladder; alkaline, neutralises stomach acid; emulsifies — physical, not an enzyme | OK | Spec wording. | 4.2.2.1 |
| C11 | T4 | villi: large SA, wall one cell thick, rich blood supply maintains gradient | OK | — | 4.1.3.1 |
| C12 | T4 | glucose, amino acids, fatty acids, glycerol absorbed into the blood | OK | GCSE level (lymph route for fats is beyond spec). | 4.2.2.1 |
| C13 | T5 | large intestine absorbs water; too little → diarrhoea, too much → constipation | OK | Simplified; context only. | — |
| C14 | T5 | faeces: fibre, dead cells, bacteria, bile pigments | OK | Context. | — |
| C15 | rp | "RP4 — Food tests" | ROUTE | 8464 RP3 (Combined); 8461 RP4 (Biology). | 8464/8461 RP lists |
| C16 | rp | iodine → blue-black; Biuret → purple | OK | Start colours: iodine orange-brown; Biuret blue. | RP |
| C17 | rp | "Benedict's solution tests for glucose (brick red = positive)" | IMPRECISE | Spec: "Benedict's test for **sugars**" (reducing sugars such as glucose); must be **heated** in a boiling/hot water bath (AT 2); blue → green/yellow/orange/brick-red depending on amount. | RP; AT 2 |
| C18 | rp | ethanol emulsion test for fat — cloudy white | OK | Lipid test not named in spec ("a range of … lipids"); ethanol emulsion (or Sudan III, red layer) both standard. | RP |
| C19 | `higher` | bile, alkaline, villi + microvilli, adaptations | ROUTE | No HT in 4.2.2.1 / 4.1.3.1 — all base. Microvilli beyond spec. | 4.2.2.1 |
| C20 | q1 key; wx1–3 | bile emulsifies; wx1 lipase digests; wx2 bile alkaline; wx3 proteases | OK | — | 4.2.2.1 |
| C21 | q2 key | villi → large surface area for absorption | OK | — | 4.1.3.1 |
| C22 | q2 wx1 | "Digestive enzymes in the small intestine come from the PANCREAS" | IMPRECISE | Also from the small intestine wall (C9). Use q2 with wx1 replaced. | 4.2.2.1 |
| C23 | q2 wx2, wx3 | bile neutralises; bile stored in gall bladder | OK | — | 4.2.2.1 |
| C24 | q3 key; wx1–3 | proteins first digested in stomach by pepsin; amylase not protein; bacteria; bile fats | OK | — | 4.2.2.1 |
| C25 | q4 key; wx1–2 | large intestine absorbs water; glucose, amino acids absorbed in small intestine | OK | — | 4.2.2.1 |
| C26 | q4 wx3 | fatty acids and glycerol into "lacteals (lymph vessels in villi)" | OK (beyond spec) | True; extra detail, harmless. | — |
| C27 | q5 key; wx1–3 | salivary glands make amylase; pepsin stomach; lipase pancreas; bile not an enzyme | OK | wx2 "Lipase is produced by the PANCREAS" — also small intestine; still answers the stem. | 4.2.2.1 |
| C28 | matching (to be replaced) | six organ–role pairs | OK | Pancreas pair repeats C9's omission. | — |

Count: **0 WRONG**; IMPRECISE: C9, C17, C22; ROUTE: C15 (RP label), C19 (`higher`); GAP: carbohydrases, word equations, use of products (F5).

## 4. Verdict
SOURCE OK WITH FLAGS. Science correct. Fix the RP label per route (RP3 Combined / RP4 Biology), name the small intestine as an enzyme source, teach Benedict's as "sugars, heated". Nothing for Mide.
