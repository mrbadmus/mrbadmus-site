# Examination — Bacterial Diseases (bacterial-diseases) — AQA 8464 4.3.1.3 / 8461 4.3.1.3
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.3.1.3-bacterial-diseases.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.3.1.1, 4.3.1.3, 4.3.1.8, 4.6.3.4; `AQA-8461-spec.txt` (v1.0) 4.3.1.1, 4.3.1.3, 4.3.1.8, 4.6.3.7. Route audit `biology.md` row 44 (4.3.1.3; CF CH TF TH; OK). No equation sheet applies.

Conventions: q1–q2 = quiz items in file order; "wx n" = `wrong_explanations` key n, attached by `generate_site_v5.py` to option index n (option 0 is the key).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.3.1.3** | Bacterial diseases | base |
| Supporting | 4.3.1.1 (toxins; rapid reproduction); 4.3.1.8 (antibiotics); 8464 4.6.3.4 / 8461 4.6.3.7 Resistant bacteria | | base |

Verbatim (8464 = 8461): "Salmonella food poisoning is spread by bacteria ingested in food, or on food prepared in unhygienic conditions. In the UK, poultry are vaccinated against Salmonella to control the spread. Fever, abdominal cramps, vomiting and diarrhoea are caused by the bacteria and the toxins they secrete. Gonorrhoea is a sexually transmitted disease (STD) with symptoms of a thick yellow or green discharge from the vagina or penis and pain on urinating. It is caused by a bacterium and was easily treated with the antibiotic penicillin until many resistant strains appeared. Gonorrhoea is spread by sexual contact. The spread can be controlled by treatment with antibiotics or the use of a barrier method of contraception such as a condom."

8464 4.6.3.4 (supporting): "Mutations of bacterial pathogens produce new strains. Some strains might be resistant to antibiotics, and so are not killed. They survive and reproduce, so the population of the resistant strain rises."

No "(HT only)" or "(biology only)" label.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Bacteria reproduce rapidly; toxins; direct damage; antibiotics target bacteria (theory 1) | base | 4.3.1.1; 4.3.1.8 | all four | OK |
| R2 | Salmonella: spread, symptoms, toxins, prevention incl. poultry vaccination (theory 2; q1; key_note) | base | 4.3.1.3 | all four | OK |
| R3 | Gonorrhoea: STD, symptoms, condoms, antibiotics (theory 3; key_note; common_mistake) | base | 4.3.1.3 | all four | OK; penicillin missing (C11) |
| R4 | Resistance by natural selection (theory 3; q2) | base | 8464 4.6.3.4 / 8461 4.6.3.7 | all four | OK |
| — | higher, equations, FIFA, RP, examiner_tip | none | — | — | correct: none exist and none are owed |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | single-celled prokaryotes; doubling every 20 min in ideal conditions | OK | — | 4.3.1.1 |
| C2 | theory 1 | disease by toxins and by direct cell damage | OK | — | 4.3.1.1 |
| C3 | theory 1 | antibiotics target bacterial structures (e.g. cell walls) human cells lack | OK | — | 4.3.1.8 |
| C4 | theory 2 | spread by eating contaminated food (undercooked poultry, raw eggs, unpasteurised milk); poor hygiene, cross-contamination | OK | Spec: "ingested in food, or on food prepared in unhygienic conditions". | 4.3.1.3 |
| C5 | theory 2 | symptoms 12–72 h after eating: fever, cramps, vomiting, diarrhoea; last 4–7 days | OK | Spec's four symptoms all present. Timings are context. | 4.3.1.3 |
| C6 | theory 2 | survive under-cooking, colonise gut, produce toxins → symptoms | OK | Spec: symptoms "caused by the bacteria and the toxins they secrete". | 4.3.1.3 |
| C7 | theory 2 | prevention: cook thoroughly, hygiene, refrigeration, pasteurisation, vaccination of poultry | OK | Poultry vaccination is the spec's named control. | 4.3.1.3 |
| C8 | theory 2 | most cases resolve without antibiotics | OK | — | — |
| C9 | theory 3 | Neisseria gonorrhoeae; STI by sexual contact; thick yellow/green discharge, pain urinating; often asymptomatic in females | OK | — | 4.3.1.3 |
| C10 | theory 3 | complications PID → infertility; HIV risk; newborn eye infection; prevention condoms | OK | — | 4.3.1.3 |
| C11 | theory 3 | treatment antibiotics; resistant strains emerged | OK, GAP | Spec names **penicillin**: "was easily treated with the antibiotic penicillin until many resistant strains appeared". Add. | 4.3.1.3 |
| C12 | theory 3 | resistance by natural selection: random mutation → resistant survive → reproduce → population resistant | OK | Matches 4.6.3.4. | 8464 4.6.3.4 |
| C13 | common_mistake | gonorrhoea is treatable, resistance growing; Salmonella "primarily through TOXINS" | OK | Spec gives "bacteria and the toxins they secrete"; teach both. | 4.3.1.3 |
| C14 | key_note | Salmonella / gonorrhoea summaries | OK | — | — |
| C15 | q1 key | cooking, hygiene, refrigeration, hand-washing | OK | — | 4.3.1.3 |
| C16 | q1 wx1 ↔ opt1 (antibiotics before eating) | promotes resistance, no benefit | OK, aligned | — | 8464 4.6.3.4 |
| C17 | q1 wx2 ↔ opt2 (avoid all animal products) | cooking makes them safe | OK, aligned | — | — |
| C18 | q1 wx3 ↔ opt3 (vaccinate all humans) | not routine; UK vaccinates poultry | OK, aligned | — | 4.3.1.3 |
| C19 | q2 key | resistant strains evolved; survivors pass on resistance | OK | — | 8464 4.6.3.4 |
| C20 | q2 wx1 ↔ opt1 (mutated into a virus) | bacteria cannot become viruses | OK, aligned | — | — |
| C21 | q2 opt2 (false) + wx2 | opt2: "New strains produce proteins that destroy antibiotic molecules before they can work"; wx2: "Some resistant bacteria do produce enzymes (like beta-lactamases) that break down antibiotics — this is one mechanism of resistance…" | **WRONG** | Opt 2 is a true answer to the question asked. Penicillinase-producing *N. gonorrhoeae* is a documented cause of gonorrhoea's penicillin resistance, and wx2 concedes it. A pupil who picks it is marked wrong for a true statement; two defensible keys. Aligned (wx2 does explain opt2), but the item fails. | 4.3.1.3; 8464 4.6.3.4 |
| C22 | q2 wx3 ↔ opt3 (people immune to antibiotics) | resistance is a property of the bacteria | OK, aligned | — | 8464 4.6.3.4 |
| C23 | matching (to be replaced) | five rows | OK | Replace per architecture. | — |

wrong_explanations alignment: all 6 keys (q1–q2 × keys 1–3) explain the option at the same index. No shift.

Count: **1 WRONG** (C21, q2); GAP 1 (C11 penicillin).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q2 | Distractor 2 is true (enzyme-producing resistant strains); two defensible keys. | **Do not use as written** (F1). |
| q1 | Correct, base. | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "The body / the patient becomes resistant to antibiotics" (it is the bacteria).
- "Bacteria mutate because of the antibiotic" (mutations are random; the antibiotic selects).
- "Salmonella is a virus" / "gonorrhoea can be prevented by a vaccine".
- "Gonorrhoea can't be treated."
- Salmonella control answered as "wash hands" only; the spec's named UK control is vaccinating poultry.

**Command words**: Describe (symptoms, spread), Explain (how resistance arises; how spread is controlled), Give.

**Typical questions** ⚑ examiner-drafted
- *Give two symptoms of Salmonella food poisoning. [2]* — any two of fever, abdominal cramps, vomiting, diarrhoea.
- *Explain why gonorrhoea is now harder to treat with penicillin. [3]* — mutation produced resistant strain (1); resistant bacteria not killed / survive (1); reproduce so resistant population increases (1).
- *Suggest two ways the spread of gonorrhoea can be controlled. [2]* — condom / barrier contraception (1); treat infected people with antibiotics (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. Theory correct throughout; penicillin, named in the spec, is missing. q2 has a true distractor and must not be used as written. q1 usable on all routes.

**For Mide:** nothing. That an enzyme mechanism (penicillinase) is real for gonorrhoea is a settled fact; it is not a conflict between AQA sources.
