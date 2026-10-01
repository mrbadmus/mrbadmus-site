# Examination — Viral Diseases (viral-diseases) — AQA 8464 4.3.1.2 / 8461 4.3.1.2
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.3.1.2-viral-diseases.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.3.1.1, 4.3.1.2, 4.3.1.7, 4.3.1.8; `AQA-8461-spec.txt` (v1.0) same sections. Route audit `biology.md` row 43 (4.3.1.2; CF CH TF TH; OK). No equation sheet applies.

Conventions: q1–q3 = quiz items in file order; "wx n" = `wrong_explanations` key n, attached by `generate_site_v5.py` to option index n (option 0 is the key).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.3.1.2** | Viral diseases | base |
| Supporting | 4.3.1.1 (viruses reproduce inside cells); 4.3.1.8 (antibiotics cannot kill viral pathogens) | | base |

Verbatim (8464 = 8461): "Measles is a viral disease showing symptoms of fever and a red skin rash. Measles is a serious illness that can be fatal if complications arise. For this reason most young children are vaccinated against measles. The measles virus is spread by inhalation of droplets from sneezes and coughs. HIV initially causes a flu-like illness. Unless successfully controlled with antiretroviral drugs the virus attacks the body's immune cells. Late stage HIV infection, or AIDS, occurs when the body's immune system becomes so badly damaged it can no longer deal with other infections or cancers. HIV is spread by sexual contact or exchange of body fluids such as blood which occurs when drug users share needles. Tobacco mosaic virus (TMV) is a widespread plant pathogen affecting many species of plants including tomatoes. It gives a distinctive 'mosaic' pattern of discolouration on the leaves which affects the growth of the plant due to lack of photosynthesis."

No "(HT only)" or "(biology only)" label.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Virus structure; reproduce inside host cells; cell damage (theory 1) | base | 4.3.1.1 | all four | OK, one IMPRECISE (C2) |
| R2 | Measles: cause, droplets, fever + rash, complications, vaccination (theory 2; q3) | base | 4.3.1.2 | all four | OK |
| R3 | HIV: spread, attacks immune cells, AIDS, ARVs (theory 3; q1; common_mistake; key_note) | base | 4.3.1.2 | all four | OK, one GAP (C9), one IMPRECISE (C10) |
| R4 | TMV: mosaic, less chlorophyll → less photosynthesis → poor growth (theory 4; q2) | base | 4.3.1.2 | all four | OK, one IMPRECISE (C13) |
| R5 | Antibiotics do not treat viruses (common_mistake; q3) | base | 4.3.1.8 | all four | OK |
| — | higher, equations, FIFA, RP, examiner_tip | none | — | — | correct: none exist and none are owed |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | viruses not cells; DNA or RNA in a protein coat; must invade a host cell to reproduce | OK | — | 4.3.1.1 |
| C2 | theory 1 | "This process destroys the host cell when new virus particles burst out." | IMPRECISE (minor) | Not always (HIV buds out). Spec: "causing cell damage". Say "often destroys the host cell". | 4.3.1.1 |
| C3 | theory 1 | symptoms partly the immune response; disrupting organ function | OK | — | — |
| C4 | theory 2 | measles virus "(a paramyxovirus)" | OK (off-spec detail) | True (family Paramyxoviridae). Not examined; keep out of questions. | — |
| C5 | theory 2 | spread by airborne droplets — coughing, sneezing | OK | Spec: "inhalation of droplets from sneezes and coughs". | 4.3.1.2 |
| C6 | theory 2 | high fever; red blotchy rash face → body; runny nose, cough, red eyes; Koplik's spots | OK | Spec examines fever + red skin rash; the rest is context. | 4.3.1.2 |
| C7 | theory 2 | complications pneumonia, encephalitis, death | OK | Spec: "can be fatal if complications arise". | 4.3.1.2 |
| C8 | theory 2 | MMR, two doses in childhood; no specific antiviral, rest/fluids/paracetamol | OK | Spec: "students do not need to know details of vaccination schedules" (4.3.1.7) — "two doses" is context only. | 4.3.1.7; 4.3.1.8 |
| C9 | theory 3 | HIV course | GAP | Missing spec statement: "HIV initially causes a flu-like illness." | 4.3.1.2 |
| C10 | theory 3 | AIDS → "OPPORTUNISTIC INFECTIONS — infections that a healthy immune system would easily fight off (e.g. rare pneumonias, certain cancers)" | IMPRECISE | Cancers are not infections. Spec: "can no longer deal with other infections or cancers". | 4.3.1.2 |
| C11 | theory 3 | HIV a retrovirus; destroys CD4+ T-helper lymphocytes; spread by sex, needles, transfusions, mother to baby; prevention; ARVs stop replication, no cure, for life | OK | "CD4+ T-helper" beyond GCSE; spec says "immune cells" / lymphocytes are credited. | 4.3.1.2 |
| C12 | theory 4 | TMV affects tobacco, tomatoes, peppers, cucumbers; mosaic pattern; leaves distorted | OK | Spec names tomatoes. | 4.3.1.2 |
| C13 | theory 4 | TMV transmission includes "insects feeding on plants"; prevention "controlling insect vectors" | IMPRECISE | TMV has no known insect vector; it spreads by contact (sap on hands, tools, plant-to-plant). Insects carry it only mechanically, rarely. Lead with contact; drop "insect vectors" from prevention. | 4.3.1.1 (direct contact) |
| C14 | theory 4 | infected cells make less chlorophyll → less photosynthesis → poor growth/yield | OK | Spec: "affects the growth of the plant due to lack of photosynthesis". | 4.3.1.2 |
| C15 | common_mistake | HIV ≠ AIDS; HIV for years without AIDS if treated with ARVs; antibiotics don't treat viral infections | OK | — | 4.3.1.2; 4.3.1.8 |
| C16 | key_note | measles / HIV / TMV summaries | OK | — | 4.3.1.2 |
| C17 | q1 key | "HIV destroys T-lymphocytes — the immune system becomes too weak to fight off infections" | OK | — | 4.3.1.2 |
| C18 | q1 wx1 ↔ opt1 (toxins damage all organs) | targets immune cells, no toxins | OK, aligned | — | — |
| C19 | q1 wx2 ↔ opt2 (overproduce WBCs) | destroys lymphocytes | OK, aligned | — | — |
| C20 | q1 wx3 ↔ opt3 ("converts into the AIDS virus") | AIDS is a condition, not a virus | OK, aligned | — | 4.3.1.2 |
| C21 | q2 key | disrupts chlorophyll production; mosaic; less photosynthesis | OK | — | 4.3.1.2 |
| C22 | q2 wx1 ↔ opt1 (blocks xylem) | affects leaf cells, not xylem | OK, aligned | — | — |
| C23 | q2 wx2 ↔ opt2 (root cells die) | infects leaves, not roots | OK, aligned | TMV is systemic (it moves through the plant) but the examined effect is on leaves; fine. | — |
| C24 | q2 wx3 ↔ opt3 (toxins kill cells) | disrupts chlorophyll, no toxin | OK, aligned | — | — |
| C25 | q3 key | measles is viral; antibiotics only kill bacteria | OK | — | 4.3.1.8 |
| C26 | q3 wx1 ↔ opt1 (rash worse) | reason is antibiotics target bacterial structures viruses lack | OK, aligned | — | 4.3.1.8 |
| C27 | q3 wx2 ↔ opt2 (too young) | pathogen type decides, not age | OK, aligned | — | — |
| C28 | q3 wx3 ↔ opt3 (paracetamol stronger) | paracetamol treats symptoms | OK, aligned | — | 4.3.1.8 |
| C29 | matching (to be replaced) | three rows | OK | Row 3 "Contact/tools" correct. Replace per architecture. | — |

wrong_explanations alignment: all 9 keys (q1–q3 × keys 1–3) explain the option at the same index. No shift.

Count: **0 WRONG**; GAP 1 (C9); IMPRECISE 3 (C2, C10, C13).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1–q3 correct and base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "HIV and AIDS are the same" / "HIV turns into AIDS".
- "AIDS kills you" (the infections or cancers the damaged immune system cannot deal with do).
- "Antibiotics cure measles / HIV".
- TMV "kills the plant" or "stops water uptake"; the credited link is mosaic → less chlorophyll → less photosynthesis → less growth.
- Measles "spread by touch / blood" instead of droplets.

**Command words**: Describe (symptoms, spread), Explain (why TMV reduces growth; why young children are vaccinated; why HIV leads to AIDS), Give.

**Typical questions** ⚑ examiner-drafted
- *Explain why tomato plants infected with TMV grow less well. [3]* — mosaic discolouration / less chlorophyll (1); less light absorbed / less photosynthesis (1); less glucose for growth (1).
- *Describe how HIV leads to AIDS. [2]* — HIV attacks immune cells / lymphocytes (1); immune system so damaged it cannot deal with other infections or cancers (1).
- *Give one reason most young children are vaccinated against measles. [1]* — measles can be fatal if complications arise.

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All quiz keys and wrong_explanations correct and aligned. One spec statement missing (flu-like first stage of HIV). Three re-cuttable theory imprecisions: hosts always burst; cancers called infections; TMV insect vectors.

**For Mide:** nothing.
