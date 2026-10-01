# Examination — Potable Water and Water Treatment (potable-water) — AQA 8464 5.10.1.2–5.10.1.3 / 8462 4.10.1.2–4.10.1.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/chemistry-5.10.1.2-potable-water.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.10.1.2, 5.10.1.3, 5.3.2.5, required practical 13 (5.10.1.2 and §10.2.13); `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.10.1.2, 4.10.1.3, 4.8.3 (chemistry-only ion tests), required practical 8 (4.10.1.2 and §8.2.8). Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `potable-water` (base, CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. Only the `higher` field has route copies (CF, TF = null). No `[NEW — to be examined]` Convert lines exist in this file (no FIFA).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.10.1.2** | Potable water | base |
| 8464 | **5.10.1.3** | Waste water treatment | base |
| 8462 | **4.10.1.2** | Potable water | base |
| 8462 | **4.10.1.3** | Waste water treatment | base |
| 8464 | **Required practical activity 13** (in 5.10.1.2; §10.2.13) | Analysis and purification of water samples | base — Combined |
| 8462 | **Required practical 8** (in 4.10.1.2; §8.2.8) | Analysis and purification of water samples | base — Chemistry |
| Supporting | 8464 5.3.2.5 / 8462 4.3.2.5 concentration in g/dm³ (base); 8462 4.8.3 ion tests (**chemistry only**) | | |

Spec statements (verbatim, 8464 = 8462):
- 5.10.1.2: "Water of appropriate quality is essential for life. For humans, drinking water should have sufficiently low levels of dissolved salts and microbes. Water that is safe to drink is called potable water. Potable water is not pure water in the chemical sense because it contains dissolved substances. The methods used to produce potable water depend on available supplies of water and local conditions. In the United Kingdom (UK), rain provides water with low levels of dissolved substances (fresh water) that collects in the ground and in lakes and rivers, and most potable water is produced by: • choosing an appropriate source of fresh water • passing the water through filter beds • sterilising. Sterilising agents used for potable water include chlorine, ozone or ultraviolet light. If supplies of fresh water are limited, desalination of salty water or sea water may be required. Desalination can be done by distillation or by processes that use membranes such as reverse osmosis. These processes require large amounts of energy." Students should be able to: "distinguish between potable water and pure water"; "describe the differences in treatment of ground water and salty water"; "give reasons for the steps used to produce potable water."
- RP (8464 RP13 = 8462 RP8): "analysis and purification of water samples from different sources, including pH, dissolved solids and distillation." AT 2 (heating), AT 3 (measuring pH), AT 4 (purify/separate incl. evaporation, distillation). WS 2.3–2.7 (incl. 2.5 sampling).
- 5.10.1.3: "Urban lifestyles and industrial processes produce large amounts of waste water that require treatment before being released into the environment. Sewage and agricultural waste water require removal of organic matter and harmful microbes. Industrial waste water may require removal of organic matter and harmful chemicals. Sewage treatment includes: • screening and grit removal • sedimentation to produce sewage sludge and effluent • anaerobic digestion of sewage sludge • aerobic biological treatment of effluent. Students should be able to comment on the relative ease of obtaining potable water from waste, ground and salt water."

No HT and no chemistry-only content in 5.10.1.2–5.10.1.3 / 4.10.1.2–4.10.1.3.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Potable = safe to drink, low dissolved salts and microbes; not pure (T1; common_mistake; key_note; q1) | base | 5.10.1.2 | all four | OK; health-claim imprecision (C3, C18) |
| R2 | Freshwater share; sources (surface, ground, sea) (T1) | base (context) | 5.10.1.2 | all four | OK |
| R3 | UK treatment: sedimentation/coagulation → filtration → chlorination (T2; key_note) | base | 5.10.1.2 | all four | OK in substance; omits "choosing an appropriate source"; sedimentation/coagulant off-spec (C6) |
| R4 | Sterilising agents chlorine, ozone, UV (T2) | base | 5.10.1.2 | all four | OK |
| R5 | Desalination: distillation, reverse osmosis; large energy cost (T2; key_note) | base | 5.10.1.2 | all four | OK |
| R6 | Waste water types; treatment needed (T3) | base | 5.10.1.3 | all four | OK |
| R7 | Sewage: screening, sedimentation → sludge + effluent, aerobic treatment of effluent, anaerobic digestion of sludge (T3; key_note; q2) | base | 5.10.1.3 | all four | OK; omits grit removal (C12); one muddle (C13) |
| R8 | Biogas, digestate (T3; key_note; q2) | off-spec (true) | — | all four | OFF-SPEC (C15, C22) |
| R9 | Chlorination of sewage effluent before discharge (T3; key_note) | — | — | all four | **WRONG** (C16) |
| R10 | Relative ease of potable water from waste, ground and salt water | base | 5.10.1.3 | — | **GAP** (C17) |
| R11 | RP: analysis and purification of water samples (rp) | base — Combined RP13 / Chemistry RP8 | 5.10.1.2 / 4.10.1.2 | all four | **WRONG as written** (C19) |
| R12 | `higher` (TH, CH): evaluate desalination; RO mechanism; UV/ozone vs chlorine | none — 5.10.1.2 has no HT; desalination and sterilising agents are base | 5.10.1.2 | TH, CH | ROUTE (C20) |
| R13 | q1 | base | 5.10.1.2 | all four | OK — usable |
| R14 | q2 | off-spec (product of anaerobic digestion) | 5.10.1.3 names the step only | all four | OFF-SPEC (C22) |
| — | FIFA, equations, examiner_tip | none | — | — | correct; RP data processing has a calculation (§5) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | potable = safe to drink, sufficiently low dissolved substances and microbes | OK | Spec: "dissolved salts and microbes". | 5.10.1.2 |
| C2 | T1 | pure water = only H₂O; potable is not pure | OK | — | 5.10.1.2 |
| C3 | T1 | dissolved minerals "are actually needed for good health (calcium, magnesium, fluoride etc.)" | IMPRECISE / OFF-SPEC | Diet, not drinking water, is the main mineral source. Spec reason is simply "it contains dissolved substances". Drop the health claim. | 5.10.1.2 |
| C4 | T1 | ~3% of Earth's water fresh; most in ice caps; <1% accessible | OK | (~2.5% fresh; ~1% accessible.) Context. | — |
| C5 | T1 | UK sources: surface water, ground water (aquifers), seawater (desalination expensive) | OK | Spec: rain collects in the ground and in lakes and rivers. | 5.10.1.2 |
| C6 | T2 | Step 1 sedimentation; coagulant (aluminium sulfate) → flocculation | OK / OFF-SPEC | True practice, not a spec step. The spec's three: choose an appropriate source of fresh water; filter beds; sterilise. "Choosing an appropriate source" is missing. | 5.10.1.2 |
| C7 | T2 | sand and gravel filters remove finer particles and some microorganisms | OK | Spec "filter beds". Reason: removes solids. | 5.10.1.2 |
| C8 | T2 | chlorine (or ozone/UV) kills harmful microorganisms; chlorine keeps protecting water in pipes | OK | Spec word "sterilising". | 5.10.1.2 |
| C9 | T2 | desalination: distillation (boil, condense) and reverse osmosis (membranes block salts); energy-intensive | OK | — | 5.10.1.2 |
| C10 | T2 | used in water-scarce regions; not widely used in UK | OK | (The UK has one large plant, Beckton.) | — |
| C11 | T3 | waste water: sewage, agricultural, industrial; must be treated before release | OK | Spec: sewage and agricultural need organic matter and microbes removed; industrial may need organic matter and harmful chemicals removed. | 5.10.1.3 |
| C12 | T3 | Step 1 screening | IMPRECISE (minor) | Spec: "screening and grit removal". Add grit removal. | 5.10.1.3 |
| C13 | T3 | Step 2 sedimentation → sludge and effluent; Step 3 effluent "AEROBIC DIGESTION … → CO₂ + H₂O. Some plants also use anaerobic digestion." | OK / IMPRECISE | Spec: "aerobic biological treatment of effluent". The "some plants also use anaerobic digestion" line blurs the spec's clean pairing (aerobic = effluent; anaerobic = sludge). Drop it. | 5.10.1.3 |
| C14 | T3 | Step 4 sludge → anaerobic digestion | OK | — | 5.10.1.3 |
| C15 | T3 | anaerobic digestion produces biogas (mainly methane), digestate used as fertiliser | OK / OFF-SPEC | True; products not on the spec. Context only. | — |
| C16 | T3; key_note | "FINAL STEP — CHLORINATION: Effluent disinfected with chlorine before discharge to rivers/sea" | **WRONG** | Not a spec step, and not UK practice: treated sewage effluent is not routinely chlorinated before discharge (chlorine residues harm river life; a few sites use UV). Teaching it as the final step would lose the mark in an "order the sewage steps" item. Remove. | 5.10.1.3 |
| C17 | — | relative ease of obtaining potable water from waste, ground and salt water | GAP | Ground water: easiest — low dissolved substances, needs only filtering and sterilising. Waste water: needs many more stages to remove organic matter, microbes and harmful chemicals before it could be made potable. Salt water: dissolved salts must be removed by desalination, which needs large amounts of energy. | 5.10.1.3; 5.10.1.2 |
| C18 | common_mistake | potable ≠ pure; tap water contains calcium, chlorine, fluoride; "Distilled water is pure but not ideal for drinking long-term (lacks minerals)" | OK / IMPRECISE | First part ✓. The distilled-water health claim is contested and off-spec — drop. | 5.10.1.2 |
| C19 | rp (frozen) | "RP8 (Chemistry) — Analysis and purification of water samples from different sources, including testing for pH, dissolved ions (using flame tests or precipitation) and filtering/distillation." | **WRONG** | (a) The spec says **dissolved solids**, not dissolved ions: measured by evaporating a known volume of the sample to dryness and weighing the residue (AT 4 evaporation). (b) Flame tests and precipitation tests are 8462 4.8.3 (**chemistry only**) — not on 8464, so wrong for CF/CH and not part of the RP on TF/TH. (c) "filtering" is not in the RP statement. (d) Only the Chemistry number is given; the Combined number is **RP13**. Correct: **Combined RP13 (8464 5.10.1.2) / Chemistry RP8 (8462 4.10.1.2): analysis and purification of water samples from different sources, including pH, dissolved solids and distillation.** Do not use as written. | 8464 5.10.1.2, §10.2.13; 8462 4.10.1.2, §8.2.8, 4.8.3 |
| C20 | `higher` (TH, CH) | evaluate desalination (energy, scale); RO = "pressure forces water through semi-permeable membrane against osmotic gradient"; UV/ozone "advantages (no by-products)" vs "(cost, no residual protection)" | ROUTE / IMPRECISE | 5.10.1.2 has no HT: desalination methods and their energy cost, and the three sterilising agents, are **base**. RO description is true but beyond spec. "Ozone — no by-products" is wrong as stated (ozonation can form bromate); "no residual protection" ✓. No Higher block; fold the base parts into base teaching. | 5.10.1.2 |
| C21 | q1 key; wx1–wx3 | potable has low dissolved minerals and is safe; pure = H₂O only; boiling not the definition; reversed definitions; potable mainly from rivers/reservoirs/boreholes | OK | — | 5.10.1.2 |
| C22 | q2 key; wx1–wx3 | anaerobic digestion of sludge → biogas (mainly methane), renewable fuel; also digestate | OK / OFF-SPEC | True, but the spec names the step only, not its products. Not assessable from the spec. | 5.10.1.3 |
| C23 | matching (to be replaced) | sedimentation, filtration, chlorination, screening, anaerobic digestion pairs | OK | Being replaced anyway. | — |
| C24 | 05-diagram-library row 13 | `water_treatment()`: reservoir → screen → sediment → filter → chlorinate → tap | OK | Usable; "Chlorinate" stands for "sterilise (chlorine, ozone or UV)". `distillation_flask()` serves desalination and the RP. | 5.10.1.2 |

Count: **2 WRONG** (C16 theory/key_note; C19 frozen rp); OFF-SPEC: C15, C22 (q2); ROUTE: C20; GAP: C17 (and C6, C12 minor omissions); IMPRECISE: C3, C13, C18.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| rp | misstates the RP (ions/flame tests instead of dissolved solids; chemistry-only tests on Combined; Combined number missing) — C19 | **Do not use as written.** Use the spec statement and the numbers Combined RP13 / Chemistry RP8. |
| q1 | correct, base | **Usable on all four routes.** |
| q2 | correct but tests an off-spec product (C22) | Not usable as assessed practice; enrichment at most. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Potable water is pure water" / "pure water is the safest to drink".
- "Filtering kills bacteria" — filtering removes solids; sterilising kills microbes.
- Sterilising agent named as "chlorine gas bubbled into rivers" or "fluoride".
- Desalination described as "filtering out the salt" (filter paper cannot remove dissolved salt).
- In the RP: confusing dissolved solids (left after evaporating) with suspended solids (removed by filtering); heating the distillation flask to dryness.
- Mixing up sludge (anaerobic) and effluent (aerobic).

**Command words**: Describe, Give a reason, Explain, Compare (ground vs salty water), Suggest, Plan (RP), Calculate (RP data).

**Typical questions** ⚑ examiner-drafted
- *What is meant by potable water? [1]* — water that is safe to drink.
- *Explain why potable water is not pure water. [2]* — contains dissolved substances (1); pure water contains only water molecules / a single substance (1).
- *Give the reason for each step: filter beds; sterilising. [2]* — remove solids (1); kill microbes (1).
- *Describe how the treatment of salty water differs from ground water. [3]* — ground water filtered and sterilised (1); salty water must be desalinated (1) by distillation or reverse osmosis (1).
- *RP: Describe how a student could find the mass of dissolved solids in a 50 cm³ water sample. [4]* — weigh empty evaporating basin (1); add measured 50 cm³ sample (1); heat until all water evaporated / to dryness (1); reweigh, mass difference = dissolved solids (1).
- *RP: Describe how to obtain pure water from salt water and check it is pure. [6]* — distillation set-up, heat, vapour condensed in condenser, collect distillate (indicative); check: boils at 100 °C / leaves no residue on evaporation / pH 7.
- *Comment on the relative ease of obtaining potable water from ground water and sea water. [2]*

**Required practical**: **Combined RP13 (8464 5.10.1.2) = Chemistry RP8 (8462 4.10.1.2)**, on all four routes. Method (spec + AT 2/3/4): measure pH of each sample (universal indicator paper/solution against a colour chart, or a pH probe); find mass of dissolved solids (weigh evaporating basin, evaporate a measured volume to dryness, reweigh); purify a salty sample by distillation (heat flask, condenser, collect distillate; distillate pH ≈ 7, no residue on evaporation, boils at 100 °C). Safety: hot apparatus, anti-bumping granules, don't boil dry. Sampling: representative samples (WS 2.5).

**Equations**: concentration (g/dm³) = mass (g) ÷ volume (dm³) — 8464 5.3.2.5 / 8462 4.3.2.5, base; chemistry has no equation sheet → Learn it. Used only if dissolved solids are reported per dm³.

## 6. Verdict
SOURCE HAS ERRORS. The frozen RP line is wrong (dissolved ions by flame test instead of dissolved solids; chemistry-only tests on Combined; Combined RP13 not named) and the theory adds a chlorination step to sewage treatment that is neither on spec nor UK practice. q1 usable everywhere; q2 off-spec. The `higher` field is base material mislabelled — no Higher block. Spec gaps: relative ease of potable water from waste/ground/salt water; "choosing an appropriate source"; grit removal. **For Mide:** nothing — RP numbers and wording are settled by both specs.
