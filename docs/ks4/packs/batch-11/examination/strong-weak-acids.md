# Examination — Strong and Weak Acids (strong-weak-acids) — AQA 8464 5.4.2.5 (HT only) / 8462 4.4.2.6 (HT only)
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.4.2.5-strong-weak-acids.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1) 5.4.2.4, 5.4.2.5; `AQA-8462-spec.txt` (v1.1) 4.4.2.4, 4.4.2.6 (8462 numbers this clause 4.4.2.6, not 4.4.2.5 — 4.4.2.5 is Titrations). No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `strong-weak-acids` (CH TH, HT, OK).

Conventions: q1–q2 quiz items; wx n = `wrong_explanations` key n; th1–th3 theory chunks. Served on CH TH only; no route copy differs.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.4.2.5 / 4.4.2.6** | Strong and weak acids | **(HT only)** |
| 8464 / 8462 | 5.4.2.4 / 4.4.2.4 | The pH scale and neutralisation (prerequisite) | base |

Spec statements (verbatim, 8464 = 8462): "A strong acid is completely ionised in aqueous solution. Examples of strong acids are hydrochloric, nitric and sulfuric acids. A weak acid is only partially ionised in aqueous solution. Examples of weak acids are ethanoic, citric and carbonic acids. For a given concentration of aqueous solutions, the stronger an acid, the lower the pH. As the pH decreases by one unit, the hydrogen ion concentration of the solution increases by a factor of 10. Students should be able to: use and explain the terms dilute and concentrated (in terms of amount of substance), and weak and strong (in terms of the degree of ionisation) in relation to acids; describe neutrality and relative acidity in terms of the effect on hydrogen ion concentration and the numerical value of pH (whole numbers only)." MS 2h "Make order of magnitude calculations." Skills: "An opportunity to measure the pH of different acids at different concentrations."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Strong = fully ionised; weak = partially ionised; → vs ⇌ (th1; key_note; equations) | higher | 5.4.2.5 | CH TH | OK |
| R2 | Named strong (HCl, HNO₃, H₂SO₄) and weak (ethanoic, carbonic, citric) acids; HF, lactic (th1) | higher (HF, lactic = context) | 5.4.2.5 | CH TH | OK |
| R3 | Same concentration → strong has lower pH; 0.1 HCl pH 1 vs 0.1 CH₃COOH pH 3 (th2; key_note) | higher | 5.4.2.5 | CH TH | OK |
| R4 | Same pH → weak acid more concentrated (th2; key_note) | higher | 5.4.2.5 | CH TH | OK |
| R5 | Dilution shifts weak-acid equilibrium right (th2) | not in spec (A-level) | — | CH TH | OFF-SPEC (SWA-F2) |
| R6 | Rates with Mg / Na₂CO₃; same total gas; conductivity (th3) | higher (context; links 5.6.1) | 5.4.2.5 | CH TH | WRONG condition (SWA-F1) |
| R7 | Strong ≠ concentrated; dilute/concentrated = amount of substance (common_mistake; key_note) | higher | 5.4.2.5 | CH TH | OK |
| R8 | ×10 [H⁺] per pH unit; relative acidity from whole-number pH | higher | 5.4.2.5 | **absent** | GAP (SWA-F3) |
| R9 | quiz q1, q2 | higher | 5.4.2.5 | CH TH | OK |
| — | `higher` field, RP | none | — | — | correct: whole lesson is HT |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | all acids produce H⁺ in water | OK | — | 5.4.2.4 |
| C2 | th1 | strong acids fully ionise "into H⁺ and the conjugate base" | IMPRECISE (minor) | "Conjugate base" is A-level; say "into H⁺ ions and negative ions". | SWA-F4 |
| C3 | th1; equations | HCl → H⁺ + Cl⁻; H₂SO₄ → 2H⁺ + SO₄²⁻; HNO₃ → H⁺ + NO₃⁻ | OK | Balanced, charges ✓. Treating H₂SO₄'s second ionisation as complete is the GCSE convention. | 5.4.2.5 |
| C4 | th1 | strong acid has maximum possible H⁺ at a given concentration | OK | — | — |
| C5 | th1; equations | CH₃COOH ⇌ CH₃COO⁻ + H⁺ (~1% ionised); H₂CO₃ ⇌ H⁺ + HCO₃⁻; HF ⇌ H⁺ + F⁻ | OK | ~1% holds at ~0.1 mol/dm³ (≈1.3%). HF is not a spec example — context. | 5.4.2.5 |
| C6 | th1 | citric, lactic acids weak, in foods | OK | Citric is a spec example. | 5.4.2.5 |
| C7 | th2 | same concentration → strong lower pH | OK | Spec sentence. | 5.4.2.5 |
| C8 | th2 | 0.1 mol/dm³ HCl → [H⁺] ≈ 0.1 → pH ≈ 1 | OK | ✓ | — |
| C9 | th2 | 0.1 mol/dm³ CH₃COOH, ~1% → [H⁺] ≈ 0.001 → pH ≈ 3 | OK | 0.1 × 0.01 = 0.001 ✓; true pH 2.9. Two pH units = 100× fewer H⁺ — a ready-made order-of-magnitude example for the GAP. | MS 2h |
| C10 | th2 | "Adding water → equilibrium shifts RIGHT (more ionisation) → slightly more H⁺. Weak acids become relatively more ionised on dilution." | OFF-SPEC; IMPRECISE | A-level. "Slightly more H⁺" is misleading: the fraction ionised rises but the H⁺ **concentration falls** and pH rises. | SWA-F2 |
| C11 | th2 | same pH → weak acid more concentrated | OK | — | 5.4.2.5 |
| C12 | th3 | same concentration → strong reacts more vigorously (higher [H⁺]); Mg fizzing vigorous vs gentle | OK | — | 5.4.2.5; 5.6.1 |
| C13 | th3 | "if EXCESS acid is used, both eventually produce the SAME amount of H₂. Why: both have the same TOTAL number of acid molecules — weak acid eventually fully reacts." | WRONG | The condition is backwards. Same total H₂ for that reason when the **magnesium is in excess** and equal volumes of equal-concentration acids are used: the acid is limiting, and the weak acid keeps ionising as H⁺ is used up. With excess acid the metal limits, and the stated reason is irrelevant. | SWA-F1 |
| C14 | th3 | Na₂CO₃: strong faster, "same total CO₂ ultimately" | WRONG (same defect) | Same total CO₂ only when the carbonate is in excess and equal amounts of acid are used. | SWA-F1 |
| C15 | th3 | strong acid better conductor (more ions) | OK | Context. | — |
| C16 | common_mistake | strong ≠ concentrated; 0.001 mol/dm³ HCl dilute strong; 5 mol/dm³ CH₃COOH concentrated weak | OK | — | 5.4.2.5 |
| C17 | key_note | as above | OK | — | 5.4.2.5 |
| C18 | q1 key | HCl fully ionises, [H⁺] ≈ 0.1; CH₃COOH partially | OK | — | 5.4.2.5 |
| C19 | q1 opt 1 / wx1 | CH₃COOH more reactive / weak acids produce fewer H⁺ | OK | Aligned. | — |
| C20 | q1 opt 2 / wx2 | same pH because same concentration / degree of ionisation decides [H⁺] | OK | Aligned. | — |
| C21 | q1 opt 3 / wx3 | larger molecules / "one H⁺ per molecule (monoprotic) — … COMPLETE ionisation, not molecule size" | OK | Aligned. "Monoprotic" is A-level vocabulary but bracketed — usable. | SWA-F4 |
| C22 | q2 key | dilute strong acid possible; 0.001 mol/dm³ HCl | OK | — | 5.4.2.5 |
| C23 | q2 opt 1–3 / wx1–3 | must be concentrated / dilution makes weak / catalyst | OK | All aligned and correct. | — |
| C24 | matching (to be replaced) | HCl, HNO₃, H₂SO₄ strong; CH₃COOH, H₂CO₃ weak | OK | — | 5.4.2.5 |

Count: **1 WRONG** (C13/C14, one theory defect, re-cuttable — theory is not frozen). OFF-SPEC: C10. Calculations: order-of-magnitude [H⁺] from whole-number pH (HT); no equation.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1, q2 | correct, HT, served CH TH | Usable on CH TH (2 per route). |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: "strong means concentrated"; "weak acids don't produce H⁺"; "a weak acid can never have a low pH"; "pH 1 is ten times more acidic than pH 3" (should be 100×); defining strong as "reacts more" instead of "completely ionised"; using "dissolves" for "ionises".
**Command words**: Explain the difference between (strong/concentrated); Compare; Calculate how many times greater the H⁺ concentration is.

## 6. Verdict
SOURCE OK WITH FLAGS. Core HT science and both quiz items correct; one wrong condition in theory 3 (excess acid → should be excess metal/carbonate); an A-level dilution paragraph; and the spec's own "factor of 10 per pH unit" statement is missing from this lesson (it sits in `ph-scale` on all four routes) — added from the spec. Nothing for Mide.
