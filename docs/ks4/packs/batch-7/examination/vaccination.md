# Examination — Vaccination (vaccination) — AQA 8464 4.3.1.7 / 8461 4.3.1.7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.3.2-vaccination.md`.
Spec sources read: `AQA-8464-spec.txt` (Trilogy v1.1, 4.3.1.6–4.3.1.7), `AQA-8461-spec.txt` (Biology v1.0, 4.3.1.6–4.3.1.7). No equations, so no equation sheet applies. Route audit: `ks4-routes/docs/ks4/route-audit/biology.md` row `vaccination` (CF CH TF TH, OK).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, which `generate_site_v5.py` pairs with option index n (option 0 is the key). T1–T4 = theory chunks.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **4.3.1.7** | Vaccination | base |
| 8461 | **4.3.1.7** | Vaccination | base |
| Supporting | 4.3.1.6 Human defence systems (white blood cells: phagocytosis, antibody production, antitoxin production) | | base |

The file header says "AQA 4.3.2". That is the site's internal numbering; there is no 4.3.2 vaccination in either spec (8461 4.3.2 is monoclonal antibodies). Cite **4.3.1.7**.

Spec statements (verbatim, 8464 = 8461): "Students should be able to explain how vaccination will prevent illness in an individual, and how the spread of pathogens can be reduced by immunising a large proportion of the population." "Vaccination involves introducing small quantities of dead or inactive forms of a pathogen into the body to stimulate the white blood cells to produce antibodies. If the same pathogen re-enters the body the white blood cells respond quickly to produce the correct antibodies, preventing infection." "Students do not need to know details of vaccination schedules and side effects associated with specific vaccines." Skills: "WS 1.4 Evaluate the global use of vaccination in the prevention of disease."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Vaccine = small quantity of dead/inactive pathogen → white blood cells make antibodies (T1; key_note) | base | 4.3.1.7 | all four | OK (T1 adds attenuated/antigen/mRNA types — enrichment) |
| R2 | Re-infection → quick antibody response → no illness; memory cells (T1; key_note; q1) | base | 4.3.1.7 | all four | OK |
| R3 | Immunising a large proportion reduces spread; herd immunity (T2; q2) | base | 4.3.1.7 | all four | OK |
| R4 | Global use of vaccination — smallpox, polio, flu, measles outbreaks (T2, T3; q3) | base | 4.3.1.7 WS 1.4 | all four | OK; MMR schedule ages off-spec (F2) |
| R5 | Vaccine safety, trials, side effects (T4) | base (context) | 4.3.1.7 excludes specific side effects; trials = 4.3.1.9 | all four | OK as context |
| R6 | `higher` (TH and CH copy): threshold, data evaluation, mRNA | **base** (threshold, data); off-spec (mRNA mechanism) | 4.3.1.7 WS 1.4 — no HT label | CH TH only | ROUTE (F1) |
| R7 | common_mistake: vaccines don't give you the disease | base | 4.3.1.7 | all four | IMPRECISE (F3) |
| R8 | quiz q1, q2, q3 | base | 4.3.1.7 | all four | all usable |
| — | RP, equations, FIFA | none | — | — | correct: 4.3.1.7 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | vaccine = small harmless amount of pathogen (or part) → immune response without the disease | OK | Spec words: "small quantities of dead or inactive forms of a pathogen". | 4.3.1.7 |
| C2 | T1 | vaccine types: dead/inactivated; attenuated live; antigen only; mRNA | OK (enrichment) | Only "dead or inactive" is spec. Attenuated "can cause very mild illness" sits badly beside common_mistake's "cannot cause the actual disease" (F3). | 4.3.1.7 |
| C3 | T1 | phagocytes engulf; lymphocytes make specific antibodies; memory cells persist; rapid, large response on re-infection | OK | "Memory cells" is not spec wording but AQA mark schemes credit it. Spec wording: "white blood cells respond quickly to produce the correct antibodies". | 4.3.1.6; 4.3.1.7 |
| C4 | T2 | herd immunity definition; chain of transmission broken | OK | Spec: "spread of pathogens can be reduced by immunising a large proportion of the population". | 4.3.1.7 |
| C5 | T2 | who cannot be vaccinated: newborns, immunocompromised, some allergies | OK | — | — |
| C6 | T2 | measles ~95%; polio ~80–85% | OK | Standard published thresholds (measles 95% two-dose coverage; polio ~80–86%). | — |
| C7 | T2 | measles outbreaks after false MMR concerns | OK | — | — |
| C8 | T3 | MMR "given at 12–15 months and again at 3–5 years" | OFF-SPEC / IMPRECISE | Spec: "Students do not need to know details of vaccination schedules". The ages quoted are not the UK schedule (UK: 1 year and 3 years 4 months; the UK moved to MMRV at 12 and 18 months from January 2026). Drop the ages. | 4.3.1.7 |
| C9 | T3 | smallpox only human disease eradicated; last natural case 1977 | OK | Last natural case Somalia, Oct 1977; WHO declared eradication 1980. | — |
| C10 | T3 | polio nearly eradicated; still circulating in a few countries | OK | Wild polio endemic in Pakistan and Afghanistan. | — |
| C11 | T3 | flu vaccine updated yearly because influenza mutates | OK | — | — |
| C12 | T3 | COVID-19 mRNA vaccines 2020–21 | OK | — | — |
| C13 | T3 | HPV causes most cervical cancers; given to teenagers | OK | UK offers it at 12–13. Off-spec context. | — |
| C14 | T4 | testing: lab, animals, phase 1–3, MHRA/FDA; common mild side effects; serious effects rare | OK (context) | Trials are 4.3.1.9's content; spec excludes specific vaccines' side effects. Keep brief. | 4.3.1.7; 4.3.1.9 |
| C15 | `higher` | "Herd immunity requires a threshold proportion … measles ~95%" | OK science / ROUTE | Base, not HT (4.3.1.7 has no HT label). | 4.3.1.7 |
| C16 | `higher` | "evaluate data on vaccination programmes and the incidence of disease, including interpreting graphs" | OK / ROUTE | Base on every route: WS 1.4 "Evaluate the global use of vaccination". | 4.3.1.7 WS 1.4 |
| C17 | `higher` | "mRNA vaccines … triggering an immune response without using any viral material" | IMPRECISE / OFF-SPEC | The mRNA carries a copy of the viral gene for one antigen; there is no live or killed virus, but "no viral material" is not accurate. Off-spec — not an HT layer. | — |
| C18 | common_mistake | vaccines "cannot cause the actual disease"; fever and soreness are a normal immune reaction | IMPRECISE | True for dead/inactive vaccines (the spec's wording). Live attenuated vaccines can rarely cause disease in people with weak immune systems, and T1 says attenuated vaccines may cause "very mild illness". Say: "a vaccine of dead or inactive pathogen cannot give you the disease". | 4.3.1.7 |
| C19 | key_note | as T1–T3 | OK | — | 4.3.1.7 |
| C20 | q1 key | stimulates immune response and memory cells → rapid response | OK | — | 4.3.1.7 |
| C21 | q1 wx1 ↔ opt 1 "kills any pathogen … rest of your life" | not a permanent killing effect | OK, paired | — | — |
| C22 | q1 wx2 ↔ opt 2 "strengthens all aspects … permanently" | immunity is specific to one pathogen | OK, paired | — | 4.3.1.7 ("correct antibodies") |
| C23 | q1 wx3 ↔ opt 3 "prevents the pathogen from ever entering" | pathogens still enter; destroyed fast | OK, paired | — | — |
| C24 | q2 key | enough immune that pathogen cannot spread — protects unvaccinated | OK | — | 4.3.1.7 |
| C25 | q2 wx1–wx3 ↔ opts 1–3 | not 100%; "herd" = any population; natural immunity contributes | OK, paired | — | — |
| C26 | q3 key | flu mutates, surface antigens change | OK | Antigen change is beyond spec wording but follows from "correct antibodies" (specificity); the theory teaches it. | — |
| C27 | q3 wx1 ↔ opt 1 | memory cells last years; issue is mutation | OK, paired | — | — |
| C28 | q3 wx2 ↔ opt 2 "contain live viruses that must be freshly prepared" | "Many flu vaccines use inactivated (killed) viruses — not live ones" | OK (minor IMPRECISE) | True as worded ("many"), but the UK children's nasal flu vaccine is live attenuated — never write "flu vaccines are not live" as a blanket line. Item usable. | — |
| C29 | q3 wx3 ↔ opt 3 | composition follows surveillance of circulating strains | OK, paired | — | — |
| C30 | matching (to be replaced) | pairs | OK | MMR pair repeats "two doses in childhood" — fine (no ages). | — |

wrong_explanations alignment: all 9 keys explain their own option (no shift). Count: **0 WRONG**; IMPRECISE/OFF-SPEC: C8, C17, C18, C28 (minor). No Convert lines (no FIFA).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1–q3 are correct and base | usable on all four routes (q1 Recall/Explain, q2 Recall, q3 Apply) |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "the vaccine contains antibodies" (it contains antigen/dead pathogen; the body makes the antibodies); "vaccines kill the pathogen"; "you become immune to all diseases"; "white blood cells remember" with no mention of fast antibody production; "antibodies stay in the blood for life" (memory cells do; antibody level falls); herd immunity explained as "everyone is vaccinated".

**Command words**: Explain (how vaccination prevents illness — 3–4 marks: dead/inactive pathogen → white blood cells produce antibodies → on re-infection antibodies made quickly → pathogen destroyed before symptoms), Evaluate (global use, from data), Suggest.

**Required practical**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All science correct for GCSE; all three quiz items usable on every route. Fix in re-cut: the `higher` box is base content (no Higher badge), the MMR schedule ages go, and the "cannot cause the disease" line is tied to dead/inactive vaccines. No Mide call.
