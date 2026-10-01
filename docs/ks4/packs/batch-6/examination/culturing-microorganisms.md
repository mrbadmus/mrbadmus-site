# Examination — Culturing Microorganisms (culturing-microorganisms) — AQA 8461 4.1.1.6 (biology only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-6/04-checked-science-source/biology-4.1.2-culturing-microorganisms.md`.
Spec sources read as text: `AQA-8461-spec.txt` (Biology v1.0, 4.1.1.6 Culturing microorganisms (biology only); Required practical activity 2 and §8.2.2 "Required practical activity 2 (biology only)"; RP list 1–10), `AQA-8464-spec.txt` (checked: 4.1.1.6 is absent from Combined Trilogy; Combined RPs 1–7 contain no microbiology practical). Route audit row `culturing-microorganisms` (OK, TF TH; "HT layer: answers in standard form. RP2 in 8461"). Architecture CFIFA amendment (24 Sep 2026) and rule 3 (2 Oct 2026) read. Runtime convention checked in `generate_site_v5.py` (`render_quiz`): `wrong_explanations` key n is shown for `opts[n]` (0-based).

Conventions: q1–q3 = quiz items; "wx n" = `wrong_explanations` key n, shown for `opts[n]`; T1–T3 = theory blocks. No route copy differs. One FIFA, one `[NEW — to be examined]` Convert line. **wx alignment checked: all three items correctly paired; no one-option-late shift.**

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8461 | **4.1.1.6** | Culturing microorganisms | **biology only**; one **(HT only)** sentence |
| 8461 | Required practical activity 2 | antiseptics/antibiotics and zones of inhibition | biology only (§8.2.2) |
| 8464 | — | not in Combined Trilogy | — |
| Supporting | 8461 4.3.1.8 Antibiotics and painkillers (spec's own link: "There are links with this practical to Antibiotics and painkillers") | | base |

The source's header ref "4.1.2" is wrong: 8461 4.1.2 is Cell division. (BATCH-PLAN already notes it.)

Spec statements (8461 4.1.1.6, verbatim): "Bacteria multiply by simple cell division (binary fission) as often as once every 20 minutes if they have enough nutrients and a suitable temperature. Bacteria can be grown in a nutrient broth solution or as colonies on an agar gel plate. Uncontaminated cultures of microorganisms are required for investigating the action of disinfectants and antibiotics. Students should be able to describe how to prepare an uncontaminated culture using aseptic technique. They should be able to explain why: Petri dishes and culture media must be sterilised before use; inoculating loops used to transfer microorganisms to the media must be sterilised by passing them through a flame; the lid of the Petri dish should be secured with adhesive tape and stored upside down; in school laboratories, cultures should generally be incubated at 25°C. Students should be able to calculate cross-sectional areas of colonies or clear areas around colonies using πr². Students should be able to calculate the number of bacteria in a population after a certain time if given the mean division time. (HT only) Students should be able to express the answer in standard form." RP2: "investigate the effect of antiseptics or antibiotics on bacterial growth using agar plates and measuring zones of inhibition."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Why culture microorganisms; culture medium; agar plates (T1) | triple | 4.1.1.6 | TF TH | OK (F6 bread); nutrient broth missing (F3) |
| R2 | Binary fission, every 20 minutes given nutrients and a suitable temperature | triple | 4.1.1.6 | — | **GAP — spec core missing** (F3) |
| R3 | Aseptic technique: sterilise dishes and media; flame loop; lid; work near Bunsen (T2; q3) | triple | 4.1.1.6 | TF TH | F4 WRONG (glass loops/beakers); F5 IMPRECISE (tape) |
| R4 | Lid taped and stored upside down — and why | triple | 4.1.1.6 | half (tape only) | **GAP** (F3, F5) |
| R5 | Incubate at 25 °C in school, and why (T2; common_mistake; key_note; q1) | triple | 4.1.1.6 | TF TH | OK |
| R6 | RP: antibiotic/antiseptic discs, zones of inhibition, control disc (T3; rp; q2) | triple | 8461 RP2 (biology only) | TF TH | OK; **rp number WRONG** (F1) |
| R7 | Area of clear zone or colony = πr² (T3; equations; FIFA) | triple | 4.1.1.6 MS 5c | TF TH | OK |
| R8 | Number of bacteria after a time, given mean division time | triple | 4.1.1.6 | — | **GAP — spec core missing** (F3) |
| R9 | Express that number in standard form | **triple-higher** | 4.1.1.6 "(HT only)" | — | **GAP + ROUTE** (F3) |
| R10 | q1, q2, q3 | triple | 4.1.1.6; RP2 | TF TH | all usable |
| — | `higher` field | none in file | — | — | the HT layer (R9) has no content in the source |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | header | "AQA 4.1.2" | **WRONG** | 8461 4.1.1.6 (biology only). F2. | 8461 |
| C2 | T1 | uses: testing antibiotics/antiseptics, studying pathogens, medicines, foods, drugs | OK | — | 4.1.1.6 |
| C3 | T1 | "Culturing bacteria is essential for … foods (yoghurt, bread, cheese)" | IMPRECISE | Bread is made with yeast, a fungus, not bacteria. F6. | — |
| C4 | T1 | medium: carbon source for energy, nitrogen source, minerals, vitamins | OK | Beyond spec, true. | — |
| C5 | T1 | agar from seaweed; poured warm, sets; colonies on the surface | OK | Spec also names nutrient broth (F3). | 4.1.1.6 |
| C6 | T2 | contamination gives false results, may introduce pathogens | OK | — | 4.1.1.6 |
| C7 | T2 | autoclave, high-pressure steam, 121 °C, kills spores | OK | Standard 121 °C / ~15 min. | 4.1.1.6 |
| C8 | T2 | "Glass equipment (beakers, loops) can be sterilised by heating in a Bunsen flame." | **WRONG** | Inoculating loops are metal wire, flamed until red hot; beakers and other glassware are not flamed — they are autoclaved or oven-sterilised. F4. | 4.1.1.6 |
| C9 | T2 | work near a Bunsen; rising air carries contaminants away | OK | Standard school practice. | — |
| C10 | T2 | flame loop red hot before and after | OK | Spec: "passing them through a flame". | 4.1.1.6 |
| C11 | T2 | flame the neck of the culture bottle | OK | — | — |
| C12 | T2 | lift lid slightly and briefly | OK | — | — |
| C13 | T2 | "Seal Petri dishes with tape after inoculation — prevents airborne contamination" | IMPRECISE | Spec: lid "secured with adhesive tape and stored upside down". Taped with a few strips, not sealed all round, so oxygen gets in and anaerobic bacteria (more likely pathogens) do not grow; stored upside down so condensation does not drip onto the agar. F5. | 4.1.1.6 |
| C14 | T2 | 25 °C maximum in school; 37 °C favours human pathogens | OK | Spec: "generally incubated at 25°C". | 4.1.1.6 |
| C15 | T3 | method: lawn, discs, incubate 25 °C 24–48 h, measure clear zones | OK | Matches RP2. | RP2 |
| C16 | T3 | antibiotic/antiseptic diffuses out and kills or inhibits bacteria | OK | — | — |
| C17 | T3 | larger zone = more effective; no zone = bacteria resistant | IMPRECISE | Fair comparison needs same disc size, same concentration and same time. "Resistant" is the antibiotic word; for an antiseptic, no zone means it does not kill these bacteria at that concentration. F7. | RP2 |
| C18 | T3 | control disc in distilled water | OK | (Or the antiseptic's solvent.) | RP2 |
| C19 | equations | Area of inhibition zone = π × r² | OK | Spec: "using πr²". | 4.1.1.6 MS 5c |
| C20 | FIFA F | Area = π × r² | OK | — | — |
| C21 | FIFA I | diameter 18 mm → radius 9 mm; π × 9² | OK | ✓ | — |
| C22 | FIFA F | π × 81 = 254.47… | OK | π × 81 = 254.469 ✓ | — |
| C23 | FIFA A | ≈ 254 mm² | OK | ✓ units mm² ✓ | — |
| C24 | CFIFA Convert `[NEW]` | "Nothing to convert — the diameter is given in millimetres (mm) … no unit conversion is needed." | OK | Halving the diameter is not a unit conversion; it stays in the verbatim I step. → `[NEW — examined ✓]`. CFIFA's second worked example needs a conversion (e.g. diameter given in cm → mm, or division time in minutes against a time in hours). | CFIFA amendment |
| C25 | rp | "RP6 — Required practical: investigate the effect of antiseptics or antibiotics on bacterial growth using agar plates and measuring inhibition zones." | **WRONG (number)** | This is 8461 **Required practical activity 2** (biology only). 8461 RP6 is light intensity and photosynthesis; it has no Combined number. Method text is correct. F1. | 8461 RP2, §8.2.2 |
| C26 | common_mistake | 25 °C not 37 °C; larger zone more effective; no zone = resistant | OK (C17 caveat) | — | 4.1.1.6 |
| C27 | key_note | summary | OK | — | — |
| C28 | q1 key | safety: 37 °C favours human pathogens | OK | — | 4.1.1.6 |
| C29 | q1 wx1–wx3 | faster at higher temperature; agar melts ~85 °C; antibiotic not temperature-dependent here | OK | Agar melts at ~85 °C ✓. Paired correctly. | — |
| C30 | q2 key | large zone = antibiotic highly effective, diffuses out | OK | — | RP2 |
| C31 | q2 wx1–wx3 | resistant bacteria show no zone; discs absorb antibiotic not bacteria; agar sets evenly | OK | Paired correctly. | — |
| C32 | q3 key | flame to sterilise before and after | OK | — | 4.1.1.6 |
| C33 | q3 wx1–wx3 | warming doesn't sterilise; loop doesn't melt agar; no "activation" | OK | Paired correctly. | — |
| C34 | matching (to be replaced) | six pairs | OK | "Seal with tape" pair has C13's caveat. | — |
| C35 | (absent) | binary fission; broth; upside-down storage; bacteria-number calculation; HT standard form | **GAP** | Spec core missing — written into the source file. F3. | 4.1.1.6 |

Count: **3 WRONG** (C1 header ref; C8 theory; C25 rp number); IMPRECISE: C3, C13, C17; GAP: C35. All four FIFA steps and the Convert line are correct; all three quiz items correct and correctly paired.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| rp field | Number "RP6" is wrong; it is 8461 RP2. | Keep the method text; **label it "Required practical 2 (Biology)"**, not RP6 (F1). |
| q1–q3, FIFA, equation | Correct. | All usable on TF and TH. |

## 5. Verdict
SOURCE HAS ERRORS. What is there is mostly right: aseptic technique, 25 °C, the zones-of-inhibition practical, the πr² worked example and all three quiz items. But the RP is mislabelled RP6 (it is Biology RP2, not on Combined), the spec ref is wrong (4.1.1.6, not 4.1.2), "glass loops and beakers are flamed" is false, and half the spec point is missing: binary fission, broth, storing plates upside down, and the bacterial-growth calculation with its HT standard-form layer. Nothing for Mide.
