# Examination — Communicable Diseases and Human Defence Systems (communicable-diseases-defence) — AQA 8464 4.3.1.1 + 4.3.1.6 / 8461 4.3.1.1 + 4.3.1.6
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.3.1-communicable-diseases-defence.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 4.3, 4.3.1.1–4.3.1.8, 4.6.3.4; `AQA-8461-spec.txt` (v1.0) 4.3, 4.3.1.1–4.3.1.8. Route audit `ks4-routes/docs/ks4/route-audit/biology.md` row 42 (4.3.1.1, 4.3.1.6; CF CH TF TH; OK). No equation sheet applies (no equations).

Conventions: q1–q4 = quiz items in file order; "wx n" = `wrong_explanations` key n, which `generate_site_v5.py` attaches to option index n (0-based; option 0 is the key). Header's "AQA 4.3.1" is the section heading; the lesson's statements are 4.3.1.1 and 4.3.1.6. 8461 and 8464 numbering and wording are identical for every statement used.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.3.1.1** | Communicable (infectious) diseases | base |
| 8464 / 8461 | **4.3.1.6** | Human defence systems | base |
| Supporting | 4.3.1.5 (vector), 4.3.1.7 (memory response), 4.3.1.8 (antibiotics vs viruses) | | base |

Verbatim (8464 = 8461):
- 4.3.1.1: "Students should be able to explain how diseases caused by viruses, bacteria, protists and fungi are spread in animals and plants. Students should be able to explain how the spread of diseases can be reduced or prevented. Pathogens are microorganisms that cause infectious disease. Pathogens may be viruses, bacteria, protists or fungi. They may infect plants or animals and can be spread by direct contact, by water or by air. Bacteria and viruses may reproduce rapidly inside the body. Bacteria may produce poisons (toxins) that damage tissues and make us feel ill. Viruses live and reproduce inside cells, causing cell damage."
- 4.3.1.6: "Students should be able to describe the non-specific defence systems of the human body against pathogens, including the: skin; nose; trachea and bronchi; stomach. Students should be able to explain the role of the immune system in the defence against disease. If a pathogen enters the body the immune system tries to destroy the pathogen. White blood cells help to defend against pathogens by: phagocytosis; antibody production; antitoxin production."
- 4.3.1.7 (supporting): "If the same pathogen re-enters the body the white blood cells respond quickly to produce the correct antibodies, preventing infection."

Neither statement carries "(HT only)" or "(biology only)".

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Communicable disease, pathogen; four pathogen types (theory 1) | base | 4.3.1.1 | all four | OK (C1–C6) |
| R2 | Spread: air, water, direct contact, vectors, food, blood (theory 2) | base | 4.3.1.1; 4.3.1.5 | all four | OK, one IMPRECISE (C9) |
| R3 | Reducing/preventing spread | base | 4.3.1.1 | absent | GAP (F3) |
| R4 | Non-specific defences: skin, nose (mucus), trachea/bronchi (cilia), stomach (acid) (theory 3; key_note) | base | 4.3.1.6 | all four | OK |
| R5 | Phagocytosis; antibodies (theory 4; common_mistake; key_note) | base | 4.3.1.6 | all four | OK |
| R6 | Antitoxin production | base | 4.3.1.6 | absent | GAP (F2) |
| R7 | Memory cells, fast re-response (theory 4; key_note) | base | 4.3.1.7 | all four | OK (vaccination lesson owns it) |
| R8 | Antibiotics do not kill viruses (common_mistake) | base | 4.3.1.8 | all four | OK |
| R9 | `higher`: secondary response; memory B-cells → plasma cells | none | — | CH, TH | ROUTE / OFF-SPEC (F1) |
| R10 | q1 phagocyte vs lymphocyte | base | 4.3.1.6 | all four | OK |
| R11 | q2 memory cells | base | 4.3.1.7 | all four | OK |
| R12 | q3 mosquito as vector | base | 4.3.1.1; 4.3.1.5 | all four | OK |
| R13 | q4 mucus | base | 4.3.1.6 (nose; trachea and bronchi) | all four | OK |
| — | equations, FIFA, RP, examiner_tip | none | — | — | correct: none exist and none are owed |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | communicable = infectious; caused by a pathogen, a microorganism that infects and harms the host | OK | — | 4.3.1.1 |
| C2 | theory 1 | spread directly or through a vector | OK | Spec routes are direct contact, water, air; vector is 4.3.1.5's word. | 4.3.1.1; 4.3.1.5 |
| C3 | theory 1 | bacteria: single-celled prokaryotes, binary fission, "mainly by producing TOXINS" | OK | Spec: "may produce poisons (toxins)". | 4.3.1.1 |
| C4 | theory 1 | bacteria examples "Salmonella, Gonorrhoea, Tuberculosis" | IMPRECISE (minor) | Mixes a pathogen name (Salmonella) with disease names. Say "Salmonella food poisoning, gonorrhoea, tuberculosis". | 4.3.1.3 |
| C5 | theory 1 | viruses not true cells, much smaller, replicate inside host cells, destroying them | OK | Spec: "live and reproduce inside cells, causing cell damage". | 4.3.1.1 |
| C6 | theory 1 | fungi eukaryotic (athlete's foot, rose black spot); protists single-celled eukaryotes (Plasmodium) | OK | — | 4.3.1.4; 4.3.1.5 |
| C7 | theory 2 | droplets: influenza, measles, COVID-19, TB | OK | — | 4.3.1.2 (measles) |
| C8 | theory 2 | water: cholera, typhoid; food: Salmonella; blood: HIV, hepatitis B | OK | — | 4.3.1.2; 4.3.1.3 |
| C9 | theory 2 | direct contact: "rose black spot (plant contact)" | IMPRECISE | Spec: rose black spot "is spread in the environment by water or wind". Use TMV (contact) as the plant direct-contact example. | 4.3.1.4 |
| C10 | theory 2 | vector carries the pathogen but doesn't cause the disease; Anopheles injects Plasmodium | OK | — | 4.3.1.5 |
| C11 | theory 3 | skin: tough continuous barrier; slightly acidic secretions inhibit bacteria | OK | Mark schemes also credit "scabs seal cuts" and "antimicrobial secretions". | 4.3.1.6 |
| C12 | theory 3 | mucus (goblet cells) traps pathogens in nose and airways | OK | "Goblet cells" beyond GCSE; harmless. Spec item is "nose": hairs and mucus trap. | 4.3.1.6 |
| C13 | theory 3 | cilia on trachea and bronchi sweep mucus up to the throat, swallowed; "stomach acid then kills any pathogens" | IMPRECISE (minor) | "kills most pathogens" (theory 3's own next paragraph says "most"). | 4.3.1.6 |
| C14 | theory 3 | stomach HCl, pH ~2, kills most swallowed pathogens | OK | — | 4.3.1.6 |
| C15 | theory 4 | phagocytes engulf and digest pathogens; non-specific | OK | — | 4.3.1.6 |
| C16 | theory 4 | lymphocytes produce antibodies with a specific shape that bind antigens; one antibody per antigen | OK | — | 4.3.1.6; 4.3.1.7 |
| C17 | theory 4 | antibodies neutralise, mark, clump pathogens | OK | Beyond spec wording; correct. | — |
| C18 | theory 4 | antitoxins | GAP | Not mentioned anywhere in the file. Spec lists antitoxin production as one of three WBC defences: antitoxins neutralise the toxins bacteria release. | 4.3.1.6 |
| C19 | theory 4; key_note | memory cells remain; rapid, large antibody production on re-infection = immunity | OK | Spec wording is "white blood cells respond quickly"; "memory cells" is credited. | 4.3.1.7 |
| C20 | higher (CH, TH) | secondary response faster and larger; "memory B-cells rapidly differentiate into plasma cells" | OFF-SPEC / ROUTE | No HT statement in 4.3.1.1–4.3.1.7. B-cells and plasma cells are A-level. The faster response itself is base vaccination content. | 4.3.1.6; 4.3.1.7 |
| C21 | common_mistake | antibiotics kill bacteria only, no effect on viruses; flu is viral; phagocytes engulf, lymphocytes make antibodies | OK | — | 4.3.1.8; 4.3.1.6 |
| C22 | key_note | barriers; phagocytes; lymphocytes; memory cells | OK | Omits antitoxins (C18). | — |
| C23 | q1 key | phagocytes engulf non-specifically; lymphocytes produce specific antibodies | OK | — | 4.3.1.6 |
| C24 | q1 wx1 ↔ opt1 (roles reversed) | "exactly the wrong way around" | OK, aligned | — | — |
| C25 | q1 wx2 ↔ opt2 (both engulf, same type) | different functions | OK, aligned | — | — |
| C26 | q1 wx3 ↔ opt3 (bacteria only / viruses only) | both act against a wide range | OK, aligned | — | — |
| C27 | q2 key | memory cells remain; rapid, large antibody response on re-exposure | OK | — | 4.3.1.7 |
| C28 | q2 wx1 ↔ opt1 (block entry) | that is skin, mucus, cilia | OK, aligned | — | — |
| C29 | q2 wx2 ↔ opt2 (produce antibiotics) | antibiotics are medicines; memory cells → antibodies | OK, aligned | — | 4.3.1.8 |
| C30 | q2 wx3 ↔ opt3 (replace damaged cells) | that is stem cells / cell division | OK, aligned | — | — |
| C31 | q3 key | mosquito is the vector, carries Plasmodium, injects it on biting | OK | — | 4.3.1.5 |
| C32 | q3 wx1 ↔ opt1 (mosquito is pathogen) | mosquito = vector, Plasmodium = pathogen | OK, aligned | — | 4.3.1.5 |
| C33 | q3 wx2 ↔ opt2 (bacteria from air) | protist, not bacteria; injected | OK, aligned | — | 4.3.1.5 |
| C34 | q3 wx3 ↔ opt3 (contaminates water) | bites, not water; cholera is waterborne | OK, aligned | — | — |
| C35 | q4 key | mucus traps inhaled pathogens and particles; cilia sweep it up to be swallowed | OK | — | 4.3.1.6 |
| C36 | q4 wx1 ↔ opt1 (gas exchange) | gas exchange is in the alveoli | OK, aligned | — | 4.2.2.1 |
| C37 | q4 wx2 ↔ opt2 (produces antibodies) | lymphocytes make antibodies | OK, aligned | — | 4.3.1.6 |
| C38 | q4 wx3 ↔ opt3 (stop drying in cold weather) | "secondary benefit" | OK, aligned | Distractor is false as worded ("in cold weather"); fine. | — |
| C39 | matching (to be replaced) | six pairs | OK | All correct; replace per architecture. | — |

wrong_explanations alignment: all 12 keys (q1–q4 × keys 1–3) explain the option at the same index. No shift.

Count: **0 WRONG**; OFF-SPEC/ROUTE 1 (C20); GAP 2 (C18, spread prevention); IMPRECISE 3 minor (C4, C9, C13).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| `higher` (CH and TH copies) | No HT content exists in this lesson's statements; B-/plasma cells off-spec. | Do not show. No higher layer on any route (F1). |
| q1–q4 | All correct, all base. | Usable on all four routes (q2 overlaps vaccination; fine). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Phagocytes make antibodies" / roles swapped.
- "White blood cells eat the antibodies" or "antibodies eat the pathogen".
- "Antibiotics kill viruses" / "take antibiotics for flu".
- "Cilia kill pathogens" (they sweep mucus; acid or WBCs kill).
- "Skin produces antibodies" — non-specific barriers confused with the immune response.
- Antitoxins forgotten; "antitoxins kill bacteria" (they neutralise toxins).

**Command words**: Describe (non-specific defences), Explain (how a defence prevents infection; how spread is reduced), Give, Name.

**Typical questions** ⚑ examiner-drafted
- *Describe how the trachea and bronchi defend the body against pathogens. [2]* — mucus traps pathogens (1); cilia move mucus up / out of airways (1).
- *Give three ways white blood cells defend the body. [3]* — phagocytosis / engulf; antibodies; antitoxins (1 each).
- *Explain how the spread of a disease spread by droplets can be reduced. [2]* — e.g. isolate infected people / cover mouth / hand-washing (1) so fewer pathogens reach others (1).

**Required practical**: none.
**Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. All frozen quiz items and every wrong_explanation correct and aligned. The `higher` text shipped on CH and TH is off-spec and has no HT home (F1). Two spec statements are missing: antitoxin production (F2) and how spread is reduced or prevented (F3).

**For Mide:** nothing. All points are settled spec facts.
