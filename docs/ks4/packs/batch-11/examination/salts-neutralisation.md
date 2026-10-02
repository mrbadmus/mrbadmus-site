# Examination — Making Salts and Neutralisation (salts-neutralisation) — AQA 8464 5.4.2.2–5.4.2.4 / 8462 4.4.2.2–4.4.2.4 (+ 8462 4.4.2.5, 4.8.3.4–4.8.3.5 chemistry only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-11/04-checked-science-source/chemistry-5.4.2.2-salts-neutralisation.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) 5.4.2.1–5.4.2.5 and RP8; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) 4.4.2.1–4.4.2.6, 4.8.3.4–4.8.3.5, §8.2.1–8.2.3 (RP1–RP3) and the RP-numbering note ("Practicals 1, 3, 4, 5, 6 and 8 are common with … Trilogy … Practicals 2 and 7 are GCSE Chemistry only"). Searched both specs for "precipitat", "insoluble salt", "phenolphthalein": no salt preparation by precipitation anywhere. No equation sheet applies. Route audit read: `ks4-routes/docs/ks4/route-audit/chemistry.md` row `salts-neutralisation` (CF CH TF TH, base; notes the titration route is chemistry-only).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. No route copy differs; every field is served on all four routes.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | 5.4.2.2 / 4.4.2.2 | Neutralisation of acids and salt production | base |
| 8464 / 8462 | **5.4.2.3 / 4.4.2.3** | Soluble salts (+ RP8 Combined / RP1 Chemistry) | base |
| 8464 / 8462 | 5.4.2.4 / 4.4.2.4 | The pH scale and neutralisation (H⁺ + OH⁻ → H₂O) | base |
| 8462 | 4.4.2.5 | Titrations | **(chemistry only)** |
| 8462 | 4.8.3.4, 4.8.3.5 | Halides (AgNO₃), sulfates (BaCl₂) — ion tests | **(chemistry only)** |

Spec statements (verbatim, 8464 = 8462):
5.4.2.3: "Soluble salts can be made from acids by reacting them with solid insoluble substances, such as metals, metal oxides, hydroxides or carbonates. The solid is added to the acid until no more reacts and the excess solid is filtered off to produce a solution of the salt. Salt solutions can be crystallised to produce solid salts. Students should be able to describe how to make pure, dry samples of named soluble salts from information provided."
RP (8464 RP8 = 8462 RP1): "preparation of a pure, dry sample of a soluble salt from an insoluble oxide or carbonate, using a Bunsen burner to heat dilute acid and a water bath or electric heater to evaporate the solution."
5.4.2.2: "Acids are neutralised by alkalis (eg soluble metal hydroxides) and bases (eg insoluble metal hydroxides and metal oxides) to produce salts and water, and by metal carbonates to produce salts, water and carbon dioxide. … hydrochloric acid produces chlorides, nitric acid produces nitrates, sulfuric acid produces sulfates …"
5.4.2.4: "In neutralisation reactions between an acid and an alkali, hydrogen ions react with hydroxide ions to produce water." (H⁺(aq) + OH⁻(aq) → H₂O(l))
8462 4.4.2.5 (chemistry only): "The volumes of acid and alkali solutions that react with each other can be measured by titration using a suitable indicator."
8462 4.8.3.4/4.8.3.5 (chemistry only): "Halide ions in solution produce precipitates with silver nitrate solution in the presence of dilute nitric acid. Silver chloride is white …" "Sulfate ions in solution produce a white precipitate with barium chloride solution in the presence of dilute hydrochloric acid."

## 2. Route table
| # | teachable point (pack location) | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Method 1: excess insoluble solid + acid, filter, crystallise; CuO + H₂SO₄ example (th1; common_mistake; key_note s1) | base | 5.4.2.3 | all four | OK, imprecise on crystallising (C4) |
| R2 | Method 2: titration to make a salt from two soluble reactants (th1; key_note s2) | triple | 8462 4.4.2.5 (chemistry only) | all four | ROUTE (SN-F2) |
| R3 | Insoluble salts by precipitation; BaSO₄ method; AgNO₃ chloride test (th2; key_note s3; equation 3) | off-spec as a preparation; ion tests triple | 8462 4.8.3.4–4.8.3.5 (chemistry only) | all four | OFF-SPEC (SN-F3) |
| R4 | Neutralisation = acid + base → salt + water (th3; equation 2) | base | 5.4.2.2 | all four | OK, omits carbonates (SN-F7) |
| R5 | Ionic equation H⁺ + OH⁻ → H₂O (th3; key_note s4; equation 1) | base | 5.4.2.4 | all four | OK |
| R6 | Titration procedure, phenolphthalein, concordant titres (th3) | triple | 8462 4.4.2.5 (chemistry only) | all four | ROUTE (SN-F2) |
| R7 | `rp` — copper sulfate from copper oxide | base | 5.4.2.3 RP | all four | RP number WRONG (SN-F1) |
| R8 | quiz q1 (why excess solid) | base | 5.4.2.3 | all four | key OK; wx2 WRONG (SN-F5) |
| R9 | quiz q2 (ionic equation) | base | 5.4.2.4 | all four | OK |
| — | `higher` | none in file | — | — | correct: nothing here is HT |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | header | "AQA 5.4.2.2–5.4.2.3" | OK | Plus 5.4.2.4 for the ionic equation. 8462 numbers are 4.4.2.x. | — |
| C2 | th1 | method depends on soluble/insoluble | OK | — | 5.4.2.3 |
| C3 | th1 M1 steps 1–2 | add excess solid so all acid used; filter off excess; salt in solution | OK | Spec: "added to the acid until no more reacts". With a carbonate, "no more fizzing and solid left over" shows excess — worth teaching. | 5.4.2.3 |
| C4 | th1 M1 step 3 | "EVAPORATE the filtrate to crystallise the salt, or leave to crystallise slowly" | IMPRECISE | Heat on a water bath / electric heater until crystals start to form, then leave to cool. Boiling to dryness spits and drives off water of crystallisation (blue CuSO₄·5H₂O → white anhydrous). | RP8/RP1 wording (SN-F4) |
| C5 | th1 M1 step 4 | filter and dry the crystals | OK | Pat dry between filter papers / warm place. | — |
| C6 | th1 example | CuO + H₂SO₄ → CuSO₄ + H₂O; black CuO; warm acid; blue solution and crystals | OK | Balanced ✓. Colours ✓. Warming acid matches the RP's Bunsen step. | RP8/RP1 |
| C7 | th1 M2 | titration for two soluble reactants; NaOH + HCl → NaCl + H₂O; repeat without indicator | OK science; ROUTE | Correct, but titration is chemistry only. AQA's 5.4.2.3 asks only the insoluble-solid method. | 8462 4.4.2.5 |
| C8 | th2 | insoluble salts by mixing two solutions; filter, wash, dry | OFF-SPEC | Correct chemistry; not in 8462 or 8464 (Edexcel/OCR content). | SN-F3 |
| C9 | th2; equation 3 | BaCl₂(aq) + Na₂SO₄(aq) → BaSO₄(s) + 2NaCl(aq); white | OK science; OFF-SPEC here | Balanced ✓. AQA meets this only as the sulfate test (with dilute HCl), chemistry only. | 8462 4.8.3.5 |
| C10 | th2 | AgNO₃ test for chloride → white AgCl | OK science; triple | Spec adds "in the presence of dilute nitric acid". | 8462 4.8.3.4 |
| C11 | th3 | neutralisation = acid + base/alkali → salt + water | OK | Carbonates also give CO₂ — absent (SN-F7). | 5.4.2.2 |
| C12 | th3; key_note; equation 1 | H⁺(aq) + OH⁻(aq) → H₂O(l) | OK | Spec equation, state symbols ✓. | 5.4.2.4 |
| C13 | th3 | titration steps; 25.00 cm³ pipette; phenolphthalein pink in alkali, colourless in acid; end point; concordant; mean titre | OK science; triple | All correct. | 8462 4.4.2.5 |
| C14 | th3 | repeat without indicator — indicator would contaminate the salt | OK | — | — |
| C15 | common_mistake | must use excess so all acid reacts; else product contaminated with acid; salt in filtrate | OK | — | 5.4.2.3 |
| C16 | key_note | four sentences | OK science | s2 triple, s3 off-spec — see R2, R3. | — |
| C17 | rp | "RP3 (Chemistry) — Prepare … hydrated copper sulfate … from copper oxide and sulfuric acid using add-excess-solid method" | WRONG (number) | Chemistry **RP1** (8462 4.4.2.3); Combined **RP8** (8464 5.4.2.3). Chemistry RP3 is electrolysis of aqueous solutions. Method content is correct. | 8462 §8.2.1; 8464 5.4.2.3 (SN-F1) |
| C18 | q1 key | excess so all acid reacts — leftover acid contaminates salt | OK | — | 5.4.2.3 |
| C19 | q1 opt 1 / wx1 | "speed up" / "Excess solid does increase the surface area and reaction rate — but the MAIN reason is …" | IMPRECISE (minor) | Concedes the distractor; acceptable, aligned. | — |
| C20 | q1 opt 2 / wx2 | "increase the yield" / "You cannot add more solid than the acid can react with — excess produces the same yield." | WRONG | First clause is false: adding more solid than the acid can react with is exactly what "excess" means. Correct: "The acid limits how much salt forms — once it is used up, extra solid makes no more salt." Aligned to its option, but not usable as written. | SN-F5 |
| C21 | q1 opt 3 / wx3 | catalyst / excess is filtered off, not a catalyst | OK | Aligned. | — |
| C22 | q2 key | H⁺(aq) + OH⁻(aq) → H₂O(l) | OK | — | 5.4.2.4 |
| C23 | q2 opt 1 / wx1 | word equation | OK | Aligned. | — |
| C24 | q2 opt 2 / wx2 | Na⁺ + Cl⁻ → NaCl(s) / "This is a precipitation ionic equation — it describes salt formation, not neutralisation." | IMPRECISE (minor) | NaCl is soluble and does not precipitate; better: "Na⁺ and Cl⁻ are spectator ions — they do not react in neutralisation." Aligned; usable. | SN-F6 |
| C25 | q2 opt 3 / wx3 | H₂ + O₂ → H₂O burning hydrogen | OK | Aligned (equation is unbalanced as a distractor — harmless). | — |
| C26 | matching (to be replaced) | CuSO₄, NaCl, BaSO₄, ZnCl₂ methods | OK science | NaCl and BaSO₄ rows carry the R2/R3 route issues; ZnCO₃ + HCl ✓. | — |

Count: **2 WRONG** (C17 rp number; C20 q1 wx2). IMPRECISE: C4, C19, C24. No calculations.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx2 states a falsehood (C20) | **Do not use as written.** Design writes a replacement "why excess?" item. |
| q2 | correct, base | Usable on all four routes. |
| equation 3 (BaCl₂ + Na₂SO₄) | off-spec as a salt preparation | Do not teach as core; at most triple context linked to the ion-tests lesson. |
| rp label "RP3" | wrong number | Render as Combined RP8 / Chemistry RP1. |

## 5. For the lesson author
**Misconceptions seen in AQA marking**: not using excess / not saying "until no more reacts"; evaporating to dryness; filtering the crystals before the excess solid ("the salt is in the residue"); naming the wrong salt (sulfuric → sulfate); writing "acid + base → salt + water" for a carbonate and losing CO₂; describing heating the acid with "boil".
**Command words**: Describe (a method to make pure dry crystals of a named salt — a classic 6-mark), Name, Give a reason, Explain why excess is used.
**Required practical**: Combined RP8 / Chemistry RP1, all four routes.

## 6. Verdict
SOURCE HAS ERRORS. Core method and chemistry correct; the RP is mis-numbered (RP3 → RP8/RP1); q1's wx2 is false; titration content is chemistry-only and precipitation of insoluble salts is off-spec, both served on all four routes. Nothing for Mide.
