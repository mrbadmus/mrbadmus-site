# Examination — Extraction of Metals and Reduction (extraction-of-metals) — AQA 8464 5.4.1.3 / 8462 4.4.1.3
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-5/04-checked-science-source/chemistry-5.4.1.3-extraction-of-metals.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.4.1.1–5.4.1.4, 5.4.3.3, 5.4.3.5, 5.10.1.4; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.4.1.1–4.4.1.4, 4.4.3.3, 4.10.1.4. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `extraction-of-metals` (base, CF CH TF TH; "Phytomining/bioleaching in `higher` field belongs to 5.10.1.4"). `site-routes.tsv`: electrolysis-extraction (5.4.3.3), half-equations (5.4.3.5, CH TH), oxidation-reduction (5.4.1.4), alternative-metal-extraction (5.10.1.4, CH TH) are separate lessons.

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks; eq1–eq3 = `equations`. Only the `higher` field has route copies (CF, TF = null). No `[NEW — to be examined]` Convert lines exist in this file (no FIFA, no calculation).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.4.1.3** | Extraction of metals and reduction | base |
| 8462 | **4.4.1.3** | Extraction of metals and reduction | base |
| Supporting | 5.4.1.1 / 4.4.1.1 (oxidation/reduction as gain/loss of oxygen), 5.4.1.2 / 4.4.1.2 (reactivity series incl. carbon) — base; 5.4.3.3 / 4.4.3.3 electrolysis to extract metals — base, own lesson; 5.4.3.5 / 4.4.3.5 half equations — **HT only**, own lesson; 5.10.1.4 / 4.10.1.4 phytomining, bioleaching — **HT only**, own lesson | | |

Spec statements (verbatim, 8464 = 8462): "Unreactive metals such as gold are found in the Earth as the metal itself but most metals are found as compounds that require chemical reactions to extract the metal. Metals less reactive than carbon can be extracted from their oxides by reduction with carbon. Reduction involves the loss of oxygen. Knowledge and understanding are limited to the reduction of oxides using carbon. Knowledge of the details of processes used in the extraction of metals is not required." Students should be able to: "interpret or evaluate specific metal extraction processes when given appropriate information"; "identify the substances which are oxidised or reduced in terms of gain or loss of oxygen."
5.4.3.3 (supporting): "Electrolysis is used if the metal is too reactive to be extracted by reduction with carbon or if the metal reacts with carbon. … Aluminium is manufactured by the electrolysis of a molten mixture of aluminium oxide and cryolite using carbon as the positive electrode (anode)."

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Ores; unreactive metals found native; most need extracting (T1) | base | 5.4.1.3 | all four | OK; one imprecision (C2) |
| R2 | Method depends on position relative to carbon (T1; common_mistake; key_note) | base | 5.4.1.3; 5.4.1.2 | all four | OK |
| R3 | Below carbon → heat oxide with carbon (reduction) (T1, T2) | base | 5.4.1.3 | all four | OK |
| R4 | Reduction = loss of oxygen; identify what is oxidised/reduced | base | 5.4.1.3; 5.4.1.1 | q2 only | **GAP in theory** (C20) |
| R5 | Blast furnace detail: coke, limestone, C → CO₂ → CO, CO reduces Fe₂O₃, molten iron tapped (T2; eq1) | off-spec ("details … not required") | 5.4.1.3 | all four | OFF-SPEC, equations balanced (C6–C9) |
| R6 | Zinc: ZnO + C → Zn + CO₂ (T2; eq2; matching) | base | 5.4.1.3 | all four | **WRONG — unbalanced** (C10) |
| R7 | Above carbon → electrolysis of molten compound (T1, T3; common_mistake; q1) | base | 5.4.3.3 | all four | OK — the contrast belongs here; the process detail is the electrolysis-extraction lesson |
| R8 | Al₂O₃ in cryolite lowers melting point; anodes replaced; energy cost (T3) | base (own lesson) | 5.4.3.3 | all four | OK |
| R9 | Electrode half equations (T3) | **higher** | 5.4.3.5 (HT only) | all four | anode equation **WRONG** (C14); HT content shown on CF/TF |
| R10 | 2Al₂O₃ → 4Al + 3O₂ (eq3) | base | 5.4.3.3 | all four | OK |
| R11 | "Aluminium once more expensive than gold" (T3) | off-spec | — | all four | IMPRECISE anecdote (C17) |
| R12 | `higher` (TH, CH): evaluate costs; phytomining, bioleaching | none here — 5.10.1.4 (HT only), own lesson | 5.10.1.4 | TH, CH | ROUTE (C26) |
| R13 | Interpret/evaluate a given extraction process | base | 5.4.1.3 | — | GAP (C21) |
| R14 | q1 | base | 5.4.1.3; 5.4.3.3 | all four | OK — usable |
| R15 | q2 | base | 5.4.1.3; 5.4.1.1 | all four | OK — usable |
| — | RP, FIFA, examiner_tip | none | — | — | correct: 5.4.1.3 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | ores = rocks containing metal compounds (oxides, sulfides, carbonates) | OK | — | 5.4.1.3 |
| C2 | T1 | "Only very UNREACTIVE metals (gold, platinum, silver) are found as pure elements … too unreactive to form compounds with oxygen or sulfur" | IMPRECISE | Silver is mined mostly as its sulfide (Ag₂S) and copper is also found native. Spec: "Unreactive metals such as gold are found in the Earth as the metal itself." | 5.4.1.3 |
| C3 | T1 | K, Na, Ca, Mg, Al above carbon → electrolysis of molten compounds | OK | — | 5.4.1.2; 5.4.3.3 |
| C4 | T1 | Zn, Fe, Sn, Pb below carbon → heat oxide with carbon | OK | — | 5.4.1.3 |
| C5 | T1 | Cu, Ag, Au found native or by simple reduction or displacement | OK | (Displacement of Cu by scrap iron is 5.10.1.4 HT; a passing mention.) | — |
| C6 | T2 | carbon reduction ("smelting") works below carbon; carbon is more reactive | OK | — | 5.4.1.3 |
| C7 | T2 | C + O₂ → CO₂ | OK | Balanced. Off-spec detail. | — |
| C8 | T2 | CO₂ + C → 2CO | OK | Balanced. Off-spec detail. | — |
| C9 | T2; eq1 | Fe₂O₃ + 3CO → 2Fe + 3CO₂ | OK | Balanced (Fe 2/2, O 6/6, C 3/3). Off-spec detail ("details of processes … not required"; "limited to the reduction of oxides using carbon"). The on-spec form is with carbon: 2Fe₂O₃ + 3C → 4Fe + 3CO₂ (balanced). | 5.4.1.3 |
| C10 | T2; eq2; matching (Zinc) | ZnO + C → Zn + CO₂ | **WRONG** | Unbalanced: O 1 left, 2 right. Correct: **2ZnO + C → 2Zn + CO₂** (or ZnO + C → Zn + CO). Frozen equation — do not use as written. | 5.4.1.3 |
| C11 | T2 | molten iron sinks and is tapped off; Al cannot be extracted this way | OK | — | — |
| C12 | T3 | electrolysis for metals more reactive than carbon (K, Na, Li, Ca, Mg, Al); electrical energy decomposes the molten compound | OK | Spec also: "or if the metal reacts with carbon". | 5.4.3.3 |
| C13 | T3 | Al₂O₃ dissolved in molten cryolite lowers the melting point from ~2000 °C to ~950 °C | OK | Al₂O₃ m.p. ≈ 2070 °C; cell ≈ 950–980 °C. Answers the spec's "explain why a mixture is used". | 5.4.3.3 |
| C14 | T3 | cathode Al³⁺ + 3e⁻ → Al; anode "O²⁻ → O₂" | **WRONG** (anode) | Anode equation is unbalanced and has no electrons. Correct: **2O²⁻ → O₂ + 4e⁻** (as `figlib` `electrolysis(setup="molten_Al2O3")` already prints). Cathode ✓. Both are HT (5.4.3.5). | 5.4.3.5 (HT only) |
| C15 | T3 | molten Al sinks and is tapped off | OK | — | — |
| C16 | T3 | costly: electrical energy; continuous high temperature; carbon anodes react with oxygen and are replaced | OK | Spec: "explain why the positive electrode must be continually replaced" — carbon anode reacts with oxygen to form CO₂. | 5.4.3.3 |
| C17 | T3 | "aluminium was once more expensive than gold — before cheap electricity" | IMPRECISE / OFF-SPEC | Popular anecdote; the price fall followed the 1886 electrolytic process. Not assessable; drop. | — |
| C18 | eq3 | 2Al₂O₃ → 4Al + 3O₂ | OK | Balanced (Al 4/4, O 6/6). | 5.4.3.3 |
| C19 | common_mistake; key_note | Al above carbon → electrolysis; below carbon → carbon/CO; native unreactive; Fe by CO in blast furnace; Al in cryolite | OK | "carbon/CO" fine; on-spec wording is "reduction with carbon". | 5.4.1.3 |
| C20 | — | "Reduction involves the loss of oxygen"; identify which substance is oxidised or reduced | GAP | Not stated in theory — only q2's key carries it. Teach: in 2CuO + C → 2Cu + CO₂, copper oxide loses oxygen (reduced), carbon gains oxygen (oxidised). | 5.4.1.3; 5.4.1.1 |
| C21 | — | interpret or evaluate a specific extraction process given information | GAP | No given-information item. The blast-furnace and zinc material is the natural vehicle — as information supplied, not facts to learn. | 5.4.1.3 |
| C22 | q1 key | Al more reactive than carbon, carbon cannot displace it from Al₂O₃ | OK | — | 5.4.1.3; 5.4.3.3 |
| C23 | q1 wx1, wx3 | carbon only reduces oxides of metals less reactive than it; electrolysis is expensive, "the reason is purely reactivity-based" | OK / IMPRECISE (minor) | "Purely" overstates: 5.4.3.3 also gives "or if the metal reacts with carbon". Item usable. | 5.4.3.3 |
| C24 | q1 wx2 | "Carbon and aluminium do not form harmful alloys under these conditions" | IMPRECISE (minor) | At high temperature Al and C form aluminium carbide (a compound, not an alloy) — the reason 5.4.3.3 adds "or if the metal reacts with carbon". The distractor is still wrong; item usable. | 5.4.3.3 |
| C25 | q2 key; wx1–wx3 | iron oxide loses oxygen (reduced), CO gains oxygen (oxidised); not neutralisation; not electrolysis | OK | Matches the spec skill. Option 2 ("iron oxide gains electrons" labelled oxidation) is correctly rejected; for HT pupils note gaining electrons IS reduction (5.4.1.4) — wx1 explains in oxygen terms, which is right for this lesson. | 5.4.1.3 |
| C26 | `higher` (TH, CH) | evaluate energy/environmental costs; phytomining, bioleaching vs traditional methods | ROUTE / OFF-SPEC | 5.4.1.3 has no HT. Phytomining/bioleaching = 5.10.1.4 (HT only), its own lesson (alternative-metal-extraction, CH TH). No Higher block here. | 5.10.1.4 (HT only) |
| C27 | matching (to be replaced) | Fe, Al, Au, Zn, Na pairs | OK except Zn | Zn pair carries the unbalanced equation (C10). Being replaced anyway. | — |

Count: **2 WRONG** (C10 frozen eq2; C14 theory); OFF-SPEC: R5 detail; ROUTE: C26, R9; GAP: C20, C21; IMPRECISE: C2, C17, C23, C24.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| eq2 "ZnO + C → Zn + CO₂" | unbalanced (C10) | **Do not use as written.** Show 2ZnO + C → 2Zn + CO₂. |
| eq1 "Fe₂O₃ + 3CO → 2Fe + 3CO₂" | correct, but CO-based furnace detail is beyond the spec's "limited to the reduction of oxides using carbon" | Usable as given information only; teach with carbon (2Fe₂O₃ + 3C → 4Fe + 3CO₂). |
| eq3 "2Al₂O₃ → 4Al + 3O₂" | correct; belongs to 5.4.3.3 | Usable as the contrast. |
| q1, q2 | correct, base | **Usable on all four routes.** |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- "Carbon can extract any metal from its oxide."
- "Reduction means the metal gains oxygen" / reversing oxidised and reduced.
- Naming the metal oxide as "oxidised" because it contains oxygen.
- "Electrolysis is used because it is cheaper" (it is the expensive route).
- Unbalanced carbon-reduction equations (the source's own eq2).

**Command words**: Explain, Identify, Give, Suggest, Evaluate (with given information), Complete the equation.

**Typical questions** ⚑ examiner-drafted
- *Explain why iron can be extracted from iron oxide by heating with carbon. [2]* — carbon is more reactive than iron (1); so carbon removes oxygen from iron oxide / reduces it (1).
- *2CuO + C → 2Cu + CO₂. Which substance is reduced? Give a reason. [2]* — copper oxide (1); it loses oxygen (1).
- *Explain why aluminium cannot be extracted by heating aluminium oxide with carbon. [1]* — aluminium is more reactive than carbon.
- *Given a table of metals, positions and costs, suggest the method for metal X. [2]*

**Required practical**: none.

**Equations**: chemical equations only; no calculation.

## 6. Verdict
SOURCE HAS ERRORS. Frozen equation eq2 (zinc) is unbalanced; theory's anode half equation is unbalanced and HT-only. Both quiz items are correct and usable on all four routes. The spec's core definition (reduction = loss of oxygen; identify oxidised/reduced) is only implicit — must be taught. Blast-furnace and Hall–Héroult detail is off-spec here (given information at most); the `higher` field belongs to 5.10.1.4. **For Mide:** nothing.
