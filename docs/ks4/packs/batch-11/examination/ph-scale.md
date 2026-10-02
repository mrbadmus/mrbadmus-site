# Examination — The pH Scale and Neutralisation (ph-scale) — AQA 8464 5.4.2.4 / 8462 4.4.2.4 (+ HT 8464 5.4.2.5 / 8462 4.4.2.6)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.4.2.4-ph-scale.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.4.2.4, 5.4.2.5 (HT only); `AQA-8462-spec.txt` (v1.1) 4.4.2.4, 4.4.2.5 (chemistry only), 4.4.2.6 (HT only). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `ph-scale` (CF CH TF TH, base; notes the `higher` field duplicates strong/weak acids). The audit did not tag the HT "factor of 10" content that sits in the theory and q1.

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n; th1–th3 theory chunks. CF and TF copies differ only in `higher` (`null`), so `higher` is served on CH TH.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.4.2.4 / 4.4.2.4** | The pH scale and neutralisation | base |
| 8464 / 8462 | 5.4.2.5 / 4.4.2.6 | Strong and weak acids | **(HT only)** |
| 8462 | 4.4.2.5 | Titrations (indicators for titration) | **(chemistry only)** |

Spec statements (verbatim, 8464 = 8462):
5.4.2.4: "Acids produce hydrogen ions (H+) in aqueous solutions. Aqueous solutions of alkalis contain hydroxide ions (OH–). The pH scale, from 0 to 14, is a measure of the acidity or alkalinity of a solution, and can be measured using universal indicator or a pH probe. A solution with pH 7 is neutral. Aqueous solutions of acids have pH values of less than 7 and aqueous solutions of alkalis have pH values greater than 7. In neutralisation reactions between an acid and an alkali, hydrogen ions react with hydroxide ions to produce water. [H+(aq) + OH–(aq) → H2O(l)] Students should be able to: describe the use of universal indicator or a wide range indicator to measure the approximate pH of a solution; use the pH scale to identify acidic or alkaline solutions." Skills column: "AT 3 This is an opportunity to investigate pH changes when a strong acid neutralises a strong alkali."
5.4.2.5 (HT only): "As the pH decreases by one unit, the hydrogen ion concentration of the solution increases by a factor of 10. … describe neutrality and relative acidity in terms of the effect on hydrogen ion concentration and the numerical value of pH (whole numbers only)." MS 2h.

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | pH 0–14 measures acidity/alkalinity; 7 neutral; acids < 7, alkalis > 7 (th1; key_note; common_mistake) | base | 5.4.2.4 | all four | OK, banding imprecise (PH-F2) |
| R2 | Acids give H⁺; alkalis contain OH⁻ (th1) | base | 5.4.2.4 | all four | OK |
| R3 | pH measures H⁺ concentration; more H⁺ → lower pH (th1 l1; th2 last block; common_mistake s1) | higher | 5.4.2.5 (HT only) | all four | ROUTE (PH-F1) |
| R4 | "Logarithmic"; ×10 per pH unit; pH 3 vs 5 = 100× (th1; key_note) | higher | 5.4.2.5 (HT only) | all four | ROUTE (PH-F1) |
| R5 | Typical pH values (th1) | base (context) | — | all four | one IMPRECISE (PH-F3) |
| R6 | Universal indicator colours, approximate pH; pH probe precise (th2; key_note) | base | 5.4.2.4 | all four | OK |
| R7 | Litmus (th2) | not in spec (KS3 recall) | — | all four | OFF-SPEC (PH-F4) |
| R8 | Phenolphthalein for titrations (th2; key_note) | triple | 8462 4.4.2.5 (chemistry only) | all four | ROUTE (PH-F4) |
| R9 | Dilution raises pH towards 7 (th2) | base (outcome); the H⁺-concentration reason is HT | 5.4.2.4; 5.4.2.5 | all four | OK |
| R10 | pH change as acid neutralises alkali; sharp fall near end point; 7 at neutral (th3) | base (AT 3 opportunity) | 5.4.2.4 | all four | OK; "why" paragraph beyond spec (PH-F4) |
| R11 | `higher` — strong/weak acids | higher | 5.4.2.5 (HT only) | CH TH | correct layer; it is the core of `strong-weak-acids` (CH TH) |
| R12 | quiz q1 (pH 2 vs 4: 100×) | higher | 5.4.2.5 (HT only) | all four | ROUTE (PH-F1) |
| R13 | quiz q2 (dilution) | base | 5.4.2.4 | all four | OK |
| R14 | H⁺ + OH⁻ → H₂O | base | 5.4.2.4 | **absent** | GAP (PH-F5) |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | pH measures H⁺ concentration; how acidic/alkaline | OK (HT clause) | Base wording: "a measure of the acidity or alkalinity". | 5.4.2.4; 5.4.2.5 |
| C2 | th1 | range 0–14, values slightly outside possible | OK | — | 5.4.2.4 |
| C3 | th1; key_note | "pH 0–6: ACIDIC … pH 8–14: ALKALINE" | IMPRECISE | Acids are **below 7**, alkalis **above 7** (pH 6.5 is acidic). | 5.4.2.4 (PH-F2) |
| C4 | th1 | pH 7 neutral, equal H⁺ and OH⁻, pure water at 25 °C | OK | — | — |
| C5 | th1; key_note | logarithmic; pH 3 has 10× H⁺ of pH 4, 100× of pH 5 | OK science; HT | ✓ arithmetic. "Logarithmic" is not a spec word; spec: "increases by a factor of 10". | 5.4.2.5 (PH-F1) |
| C6 | th1 | "Hydrochloric acid (conc.): pH ~0–1" | IMPRECISE | Concentrated HCl (~12 mol/dm³) is below pH 0; pH ~0–1 is dilute bench HCl (0.1–1 mol/dm³). | PH-F3 |
| C7 | th1 | vinegar ~3; coffee ~5; water 7; baking soda ~9; NaOH ~13–14 | OK | Baking soda solution ≈ 8.3; "~9" acceptable. | — |
| C8 | th2 | UI is a mixture; red → orange → yellow → green → blue → purple; approximate pH | OK | — | 5.4.2.4 |
| C9 | th2 | litmus red/blue/purple; phenolphthalein colourless/pink | OK science | Litmus off-spec; phenolphthalein is a titration indicator (chemistry only). | PH-F4 |
| C10 | th2 | pH probe precise, more accurate | OK | — | 5.4.2.4 |
| C11 | th2 | more H⁺ → lower pH; more OH⁻ → higher pH; dilution → pH up towards 7 | OK | First two are HT framing (R3). | 5.4.2.5 |
| C12 | th3 | adding base raises pH; adding acid lowers pH | OK | — | 5.4.2.4 |
| C13 | th3 | curve: starts ~13, falls slowly, drops rapidly near end point, 7 for strong/strong, continues to fall | OK | Correct shape. Text conflates "end point" (indicator change) and "equivalence point". | AT 3 (PH-F4) |
| C14 | th3 | "very little OH⁻ left to absorb the H⁺ … large change in H⁺ concentration" | OFF-SPEC | Correct in outline, but explaining the steep section needs the log scale and is beyond GCSE. | PH-F4 |
| C15 | higher | strong fully / weak partially dissociate; CH₃COOH ⇌ CH₃COO⁻ + H⁺; same concentration → strong lower pH; strong ≠ concentrated | OK | Correct, HT. Duplicates `strong-weak-acids`. | 5.4.2.5 |
| C16 | common_mistake | lower pH = more acidic = more H⁺; pH 2 vs 12; pH 7 neutral; not all pH 7 solutions are water | OK | H⁺ clause HT. | 5.4.2.4–5.4.2.5 |
| C17 | q1 key | pH 2 has 100× the H⁺ of pH 4 | OK | 10² ✓. HT. | 5.4.2.5 |
| C18 | q1 opt 1 / wx1 | "twice" / log scale, 10² = 100 | OK | Aligned. | — |
| C19 | q1 opt 2 / wx2 | pH 4 has more / lower pH more H⁺ | OK | Aligned. | — |
| C20 | q1 opt 3 / wx3 | same / both acidic but very different | OK | Aligned. | — |
| C21 | q2 key | pH increases towards 7; dilution reduces H⁺ concentration | OK | — | 5.4.2.4 |
| C22 | q2 opt 1 / wx1 | pH decreases / water does not make acid stronger | OK | Aligned. | — |
| C23 | q2 opt 2 / wx2 | stays same / water reduces H⁺ concentration | OK | Aligned. | — |
| C24 | q2 opt 3 / wx3 | jumps to 7 / "Unless you add enormous amounts of water, the pH approaches 7 gradually but never quite reaches it" | IMPRECISE (minor) | "Unless …" implies enough water reaches 7; an acid diluted with water never reaches or passes 7. Aligned; usable. | PH-F6 |
| C25 | matching (to be replaced) | "pH 4 — black coffee or tomato juice" | IMPRECISE (minor) | Black coffee ≈ 5. Matching is replaced anyway. | — |

Count: **0 WRONG**. IMPRECISE: C3, C6, C24, C25. ROUTE: HT ×10 content on all four routes. No calculations at base; the ×10 / ×100 comparison is an HT order-of-magnitude calculation (MS 2h).

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | HT content (5.4.2.5) served on CF TF | Usable on **CH TH only**. |
| q2 | base | Usable on all four routes. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "pH 12 is a strong acid"; "the higher the pH, the more acidic"; "universal indicator gives the exact pH"; "diluting an acid makes it neutral"; "adding water to an alkali raises its pH"; describing UI use without "compare the colour with a colour chart".
**Command words**: Describe how to use universal indicator to find the pH; Identify (acid/alkali from pH); Complete the ionic equation.

## 6. Verdict
SOURCE OK WITH FLAGS. Science correct throughout; the "factor of 10 per pH unit" content (and q1) is HT but served on all four routes; acid/alkali banding stated as 0–6 / 8–14; the lesson's own spec equation (H⁺ + OH⁻ → H₂O) is absent and has been added from the spec. Nothing for Mide.
