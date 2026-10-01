# Examination — Atmospheric Pollutants from Fuels (atmospheric-pollutants) — AQA 8464 5.9.3.1–5.9.3.2 / 8462 4.9.3.1–4.9.3.2
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-4/04-checked-science-source/chemistry-5.9.3.1-atmospheric-pollutants.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.9.3.1–5.9.3.2, 5.4.2.5; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.9.3.1–4.9.3.2, 4.4.2.6. Route audit `ks4-routes/docs/ks4/route-audit/chemistry.md` row `atmospheric-pollutants` (base, CF CH TF TH).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n (= opts index n). T1–T3 = theory chunks. Only the `higher` field has route copies (CF, TF = null).

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | **5.9.3.1** | Atmospheric pollutants from fuels | base |
| 8464 | **5.9.3.2** | Properties and effects of atmospheric pollutants | base |
| 8462 | **4.9.3.1** | Atmospheric pollutants from fuels | base |
| 8462 | **4.9.3.2** | Properties and effects of atmospheric pollutants | base |
| Supporting | 8464 5.4.2.3 / 8462 4.4.2.2 (acid + metal carbonate); 8464 5.4.2.5 / 8462 4.4.2.6 (pH factor of 10, **HT only**) | | |

Spec statements (verbatim, 8464 = 8462):
- 5.9.3.1: "The combustion of fuels is a major source of atmospheric pollutants. Most fuels, including coal, contain carbon and/or hydrogen and may also contain some sulfur. The gases released into the atmosphere when a fuel is burned may include carbon dioxide, water vapour, carbon monoxide, sulfur dioxide and oxides of nitrogen. Solid particles and unburned hydrocarbons may also be released that form particulates in the atmosphere." Students should be able to: "describe how carbon monoxide, soot (carbon particles), sulfur dioxide and oxides of nitrogen are produced by burning fuels"; "predict the products of combustion of a fuel given appropriate information about the composition of the fuel and the conditions in which it is used." (WS 1.2)
- 5.9.3.2: "Carbon monoxide is a toxic gas. It is colourless and odourless and so is not easily detected. Sulfur dioxide and oxides of nitrogen cause respiratory problems in humans and cause acid rain. Particulates cause global dimming and health problems for humans." Students should be able to "describe and explain the problems caused by increased amounts of these pollutants in the air." (WS 1.4)

Neither spec has HT or chemistry-only content in 5.9.3 / 4.9.3. Neither spec mentions catalytic converters, scrubbers, desulfurisation, smog, ozone or the chemistry of acid formation.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Fuels contain C and/or H, may contain S; combustion is a major pollutant source (T1 intro) | base | 5.9.3.1 | all four | OK |
| R2 | CO from incomplete combustion; toxic, colourless, odourless (T1; common_mistake; key_note) | base | 5.9.3.1–2 | all four | OK |
| R3 | CO binds haemoglobin, stops O₂ transport (T1; q1) | base (context) | 5.9.3.2 "toxic" | all four | OK in T1; q1 says "irreversibly" — WRONG (C21) |
| R4 | SO₂ from sulfur impurities; S + O₂ → SO₂ (T1; eq 1) | base | 5.9.3.1 | all four | OK |
| R5 | SO₂ → acid rain, respiratory problems (T1, T2) | base | 5.9.3.2 | all four | OK |
| R6 | SO₂/SO₃ + H₂O → sulfurous/sulfuric acid (T1); acid-formation equations (T2) | off-spec | — | all four | OFF-SPEC (true) |
| R7 | NOₓ from N₂ + O₂ at high engine temperature; N₂ + O₂ → 2NO (T1; eq 2) | base | 5.9.3.1 | all four | OK |
| R8 | NOₓ → acid rain, respiratory problems (T1, T2) | base | 5.9.3.2 | all four | OK |
| R9 | NOₓ → smog, low-level ozone (T1) | off-spec | — | all four | OFF-SPEC (true) |
| R10 | Particulates (soot) from incomplete combustion; lungs; global dimming (T1) | base | 5.9.3.1–2 | all four | OK; omits unburned hydrocarbons (C8); typo (C9) |
| R11 | Acid rain effects: limestone buildings, lakes, trees (T2; key_note; eq 4) | base (context — "explain the problems caused") | 5.9.3.2; 5.4.2.3 | all four | OK |
| R12 | Rain pH ~5.6, acid rain pH 4–5, "10×–100× more acidic" (T2) | off-spec; the factor-of-10 idea is HT | 5.4.2.5 (HT only) | all four | IMPRECISE (C12) |
| R13 | Desulfurisation, scrubbers, catalytic converters, particulate filters, EVs, engine design, agreements (T2, T3; eq 3; key_note last clause) | off-spec | — | all four | OFF-SPEC; one WRONG claim (C17) |
| R14 | `higher`: evaluate pollution control | off-spec — not HT | — | TH, CH | OFF-SPEC (C24) |
| R15 | Predict combustion products from fuel composition and conditions | base | 5.9.3.1 (WS 1.2) | — | **GAP — not in the source** (C25) |
| R16 | q1 | base | 5.9.3.2 | all four | WRONG key wording (C21) |
| R17 | q2 | off-spec | — | all four | OFF-SPEC (C23) |
| — | RP, FIFA, examiner_tip | none | — | — | correct: 5.9.3 has none |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | T1 | burning fossil fuels releases pollutants besides CO₂ and water | OK | — | 5.9.3.1 |
| C2 | T1 | CO from incomplete combustion — insufficient oxygen | OK | — | 5.9.3.1 |
| C3 | T1 | CO colourless, odourless, toxic | OK | Spec wording; add "so is not easily detected". | 5.9.3.2 |
| C4 | T1 | CO binds to haemoglobin, prevents O₂ transport, can be fatal | OK | Beyond the chemistry spec but correct. | — |
| C5 | T1; eq 1 | S + O₂ → SO₂ | OK | Balanced. | 5.9.3.1 |
| C6 | T1 | SO₂ + H₂O → H₂SO₃; SO₃ + H₂O → H₂SO₄ | OK / OFF-SPEC | Both balanced. Not on spec; do not assess. | — |
| C7 | T1; eq 2 | N₂ + O₂ → 2NO at engine temperatures, then oxidised to NO₂ | OK | Balanced. Spec: "oxides of nitrogen", produced when nitrogen and oxygen from the air react at high temperature. | 5.9.3.1 |
| C8 | T1 | particulates "from incomplete combustion of fuels" | IMPRECISE (minor) | Spec: solid particles **and unburned hydrocarbons** form particulates. Add unburned hydrocarbons. | 5.9.3.1 |
| C9 | T1 | "Consciously contribute to GLOBAL DIMMING" | IMPRECISE (typo) | "Particulates also contribute to global dimming — less sunlight reaching the Earth's surface." | 5.9.3.2 |
| C10 | T1 | NOₓ → smog and low-level ozone | OFF-SPEC | True; not on spec. | — |
| C11 | T2 | SO₂ + H₂O + ½O₂ → H₂SO₄; 4NO₂ + O₂ + 2H₂O → 4HNO₃ | OK / OFF-SPEC | Both balanced (checked atom by atom). Not on spec. | — |
| C12 | T2 | normal rain pH ~5.6; acid rain pH 4–5, "10× to 100× more acidic" | IMPRECISE | pH 5.6 ✓. pH 4–5 is about 4× to 40× the H⁺ concentration of pH 5.6, not 10×–100×. The factor-of-10-per-pH-unit idea is HT (8464 5.4.2.5). Drop the multiplier; "acid rain has a lower pH than normal rain" is enough. | 5.4.2.5 (HT only) |
| C13 | T2; eq 4 | CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂ | OK | Balanced. Acid + carbonate is base chemistry. | 5.4.2.3 |
| C14 | T2 | lakes too acidic → fish die; soil acidification releases aluminium ions → trees die | OK | Aluminium-ion mechanism off-spec, true. | — |
| C15 | T2 | SO₂ and NO₂ irritate respiratory system | OK | Spec: "cause respiratory problems". | 5.9.3.2 |
| C16 | T2 | solutions: desulfurisation; catalytic converters; scrubbers spray calcium hydroxide | OK / OFF-SPEC | Scrubbers usually use a limestone (CaCO₃) or lime slurry; "calcium hydroxide" is one form. Not on spec. | — |
| C17 | T3 | catalytic converter "Reduces: CO (toxic), NOₓ (acid rain, smog) **and particulates**" | WRONG (theory, re-cuttable) | A catalytic converter does not remove particulates — that is the separate particulate filter. The source contradicts itself: q2 wx1 says the same. Drop "and particulates". Off-spec in any case. | — |
| C18 | T3; eq 3 | Pt/Rh catalysts; 2CO + 2NO → 2CO₂ + N₂; hydrocarbons + O₂ → CO₂ + H₂O | OK / OFF-SPEC | Balanced. Not on spec. | — |
| C19 | T3; common_mistake | catalytic converters increase CO₂ (CO → CO₂) | OK / OFF-SPEC | True. | — |
| C20 | common_mistake | CO from incomplete, CO₂ from complete combustion; both colourless; CO toxic, CO₂ not at normal concentrations | OK | (Incomplete combustion also makes some CO₂ — fine as stated.) | 5.9.3.1–2 |
| C21 | q1 key | "CO binds **irreversibly** to haemoglobin … causing suffocation even in small concentrations" | **WRONG** | CO binding to haemoglobin is **reversible**: it binds about 200–250 times more strongly than oxygen and is released slowly, which is why CO poisoning is treated with high-concentration oxygen. "Irreversibly" is a textbook myth. The spec's answer to "why is CO dangerous" is that it is **toxic, colourless and odourless, so not easily detected** — the key does not say that at all. Do not use as written. | 5.9.3.2 |
| C22 | q1 wx1–wx3 | CO colourless/odourless; density similar to air; CO does not form carbonic acid | OK | M(CO) = 28, mean M(air) ≈ 29 ✓. wx1 is the spec's own point and is the best line in the item. | 5.9.3.2 |
| C23 | q2 key, wx1–wx3 | catalytic converters convert CO and NOₓ to CO₂ and N₂ with Pt/Rh; not filters; increase CO₂; no added oxygen | OK / OFF-SPEC | All true. Catalytic converters are not on 8462 or 8464; not usable as assessed practice. | — |
| C24 | `higher` (TH, CH) | evaluate pollution control, EVs, life-cycle view | OFF-SPEC | 5.9.3 has no HT content. Life-cycle assessment is a separate base lesson (5.10.2.1). CF/TF copies are already null; nothing to move. Do not render as a Higher layer. | 5.9.3; 5.10.2.1 |
| C25 | — | predict products of combustion from fuel composition and conditions | GAP | Not taught anywhere in the source. See source file's "Spec core missing" section and flag ATMOSPHERIC-POLLUTANTS-F5. | 5.9.3.1 |
| C26 | key_note | summary as above; "Catalytic converters: convert CO + NOₓ → CO₂ + N₂" | OK / OFF-SPEC (last clause) | — | — |
| C27 | equations | 4 equations | OK | All four balanced. Eq 1, 2 base; eq 4 base context; eq 3 off-spec. No formula equations, so no Convert lines exist in this file. | — |

Count: **2 WRONG** (C17 theory, re-cuttable; C21 frozen quiz key). IMPRECISE: C8, C9, C12. OFF-SPEC: C6, C10, C11, C16, C18, C23, C24. GAP: C25.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | Key states CO binds "irreversibly" — false; misses the spec's answer (toxic, colourless, odourless → not easily detected) | **Do not use as written** on any route. |
| q2 | Catalytic converters are not on either spec | Not usable as assessed practice on any route. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**
- CO and CO₂ confused ("CO₂ is the poisonous gas from a faulty boiler").
- "Carbon dioxide causes acid rain" / "acid rain causes global warming" — acid rain is SO₂ and NOₓ.
- Nitrogen oxides come "from nitrogen in the fuel" — it is nitrogen from the **air**, at high temperature.
- Sulfur dioxide comes "from the air" — it comes from sulfur **in the fuel**.
- Global dimming confused with global warming or the ozone hole.
- "Particulates are a gas."

**Command words**: Describe how … is produced; Explain why … is dangerous; Predict the products; Give one effect.

**Typical questions** ⚑ examiner-drafted
- *Explain why carbon monoxide is dangerous. [2]* — toxic (1); colourless and odourless so not easily detected (1).
- *Describe how oxides of nitrogen are produced when petrol burns in a car engine. [2]* — nitrogen and oxygen from the air (1); react at the high temperature in the engine (1).
- *A fuel contains carbon, hydrogen and sulfur. It is burned in a limited supply of air. Name three pollutants produced. [3]* — carbon monoxide / soot (carbon) / sulfur dioxide (any three incl. unburned hydrocarbons).
- *Give one effect of particulates. [1]* — global dimming / health problems (lungs).

**Required practical**: none.

**Equations**: chemical equations only (S + O₂ → SO₂; N₂ + O₂ → 2NO). No formula equations; no equation-sheet entries.

## 6. Verdict
SOURCE HAS ERRORS. The spec core (CO, SO₂, NOₓ, particulates — source and effect) is present and correct in the theory, but: frozen q1's key carries a false word ("irreversibly") and misses the spec's answer; q2 is off-spec; the theory wrongly says catalytic converters remove particulates; and the spec's "predict the products of combustion" skill is not taught at all. About half the theory (acid formation equations, smog, catalytic converters, scrubbers, the `higher` evaluation) is off-spec enrichment. **Zero frozen quiz items usable** — Design writes the whole practice bank.

**For Mide:** nothing. All points are settled science.
