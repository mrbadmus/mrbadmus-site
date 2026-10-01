# Examination — Fungal and Protist Diseases (fungal-protist-diseases) — AQA 8464 4.3.1.4–4.3.1.5 / 8461 4.3.1.4–4.3.1.5
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-7/04-checked-science-source/biology-4.3.1.4-fungal-protist-diseases.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 4.3.1.1, 4.3.1.4, 4.3.1.5; `AQA-8461-spec.txt` (v1.0) same. Route audit `biology.md` row 45 (4.3.1.4–5; CF CH TF TH; OK). No equation sheet applies.

Conventions: q1–q2 = quiz items in file order; "wx n" = `wrong_explanations` key n, attached by `generate_site_v5.py` to option index n (option 0 is the key). Header's "AQA 4.3.1.4" omits 4.3.1.5 (malaria); the lesson covers both.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8461 | **4.3.1.4** | Fungal diseases | base |
| 8464 / 8461 | **4.3.1.5** | Protist diseases | base |
| Supporting | 4.3.1.1 (spread by water, air; vectors) | | base |

Verbatim (8464 = 8461):
- 4.3.1.4: "Rose black spot is a fungal disease where purple or black spots develop on leaves, which often turn yellow and drop early. It affects the growth of the plant as photosynthesis is reduced. It is spread in the environment by water or wind. Rose black spot can be treated by using fungicides and/or removing and destroying the affected leaves."
- 4.3.1.5: "The pathogens that cause malaria are protists. The malarial protist has a life cycle that includes the mosquito. Malaria causes recurrent episodes of fever and can be fatal. The spread of malaria is controlled by preventing the vectors, mosquitos, from breeding and by using mosquito nets to avoid being bitten."

No "(HT only)" or "(biology only)" label.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Rose black spot: fungus, symptoms, spread, effect on growth, treatment (theory 1, 3; q1; key_note) | base | 4.3.1.4 | all four | OK |
| R2 | Malaria: protist, mosquito vector, life cycle, recurrent fever, fatal, control (theory 2, 3; q2; common_mistake; key_note) | base | 4.3.1.5 | all four | OK, one IMPRECISE (C7) |
| R3 | Vector vs pathogen (common_mistake; q2) | base | 4.3.1.5; 4.3.1.1 | all four | OK |
| — | higher, equations, FIFA, RP, examiner_tip | none | — | — | correct: none exist and none are owed |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | cause *Diplocarpon rosae*, a fungus | OK | Species name is context. | 4.3.1.4 |
| C2 | theory 1 | spores spread by water (rain splash) and wind; germinate warm and wet | OK | Spec: "by water or wind". | 4.3.1.4 |
| C3 | theory 1 | purple or black spots; yellowing; early leaf drop (defoliation) | OK | Spec wording. | 4.3.1.4 |
| C4 | theory 1 | fewer leaves → less photosynthesis → poor growth, fewer flowers; may die | OK | Spec: "affects the growth of the plant as photosynthesis is reduced". | 4.3.1.4 |
| C5 | theory 1 | remove and destroy infected leaves (not compost); fungicide; resistant varieties; avoid overhead watering | OK | Spec's two treatments present. | 4.3.1.4 |
| C6 | theory 2 | Plasmodium, a single-celled eukaryotic protist; *P. falciparum* most deadly | OK | — | 4.3.1.5 |
| C7 | theory 2 | female Anopheles "bites infected humans, picks up Plasmodium, and injects it into the next person she bites" | IMPRECISE | Reads as if the mosquito is a passive syringe. Spec: "The malarial protist has a life cycle that includes the mosquito" — the protist develops and reproduces inside the mosquito before it can infect the next person. Add one line. | 4.3.1.5 |
| C8 | theory 2 | injected → liver, multiplies → infects and destroys red blood cells in cycles → recurring fever | OK | Spec: "recurrent episodes of fever". | 4.3.1.5 |
| C9 | theory 2 | symptoms; severe: anaemia, kidney failure, cerebral malaria, coma, death | OK | Spec: "can be fatal". | 4.3.1.5 |
| C10 | theory 2 | prevention: nets (ITNs), insecticide, drain standing water, anti-malarials for travellers | OK | Spec's two controls (stop breeding; nets) present; draining water = stopping breeding. | 4.3.1.5 |
| C11 | theory 2 | treatment artemisinin-based combinations; resistance emerging | OK | Context. | — |
| C12 | theory 3 | comparison table; "Host: Humans (and other primates)" | OK | — | — |
| C13 | common_mistake | mosquito is the vector, Plasmodium the pathogen; rose black spot is a fungus | OK | — | 4.3.1.4; 4.3.1.5 |
| C14 | key_note | summaries | OK | — | — |
| C15 | q1 key | spots, leaves fall, less leaf area → less photosynthesis → less glucose for growth | OK | — | 4.3.1.4 |
| C16 | q1 wx1 ↔ opt1 (blocks xylem) | infects leaf cells | OK, aligned | — | — |
| C17 | q1 wx2 ↔ opt2 (toxins kill root cells) | leaf disease, not roots | OK, aligned | — | — |
| C18 | q1 wx3 ↔ opt3 (spores block stomata) | "not the primary mechanism" | OK, aligned | "not the primary mechanism" hedges a false option; harmless, but "this is not how black spot harms the plant" would be cleaner. Frozen; usable. | — |
| C19 | q2 key | vector; carries Plasmodium between humans when biting | OK | — | 4.3.1.5 |
| C20 | q2 wx1 ↔ opt1 (mosquito is the pathogen) | pathogen is Plasmodium | OK, aligned | — | 4.3.1.5 |
| C21 | q2 wx2 ↔ opt2 (saliva toxin) | disease caused by Plasmodium, not saliva | OK, aligned | — | — |
| C22 | q2 wx3 ↔ opt3 (only in tropical countries) | role as vector is the same wherever it lives | OK, aligned | — | — |
| C23 | matching (to be replaced) | six rows | OK | Replace per architecture. | — |

wrong_explanations alignment: all 6 keys (q1–q2 × keys 1–3) explain the option at the same index. No shift.

Count: **0 WRONG**; IMPRECISE 1 (C7).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| none | q1, q2 correct and base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Mosquitoes cause malaria" / "malaria is a virus / bacterium".
- "Rose black spot is spread by insects" (water or wind).
- "Black spot kills the plant by poisoning it" — the credited chain is leaf loss → less photosynthesis → less growth.
- Malaria control answered as "vaccinate" or "antibiotics"; the spec's controls are stopping mosquitoes breeding and nets.

**Command words**: Describe, Explain (why black spot reduces growth; how nets/draining water reduce malaria), Give, Name (the type of pathogen).

**Typical questions** ⚑ examiner-drafted
- *Explain why rose black spot reduces the growth of a rose plant. [3]* — leaves drop / fewer leaves (1); less photosynthesis (1); less glucose for growth (1).
- *Name the type of pathogen that causes malaria. [1]* — protist.
- *Explain how draining standing water reduces the spread of malaria. [2]* — mosquitoes cannot breed / fewer vectors (1); so fewer people bitten / Plasmodium passed on less (1).

**Required practical**: none. **Equations**: none.

## 6. Verdict
SOURCE OK WITH FLAGS. Science correct; both quiz items and all wrong_explanations correct and aligned. One minor imprecision: the mosquito's part in the protist's life cycle.

**For Mide:** nothing.
