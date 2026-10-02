# Examination — Structure and Formulae of Alkenes (structure-of-alkenes) — AQA 8462 4.7.2.1 (chemistry only)
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-13/04-checked-science-source/chemistry-4.7.2.1-structure-of-alkenes.md`.
Spec sources read as text: AQA-8462 (v1.1) §4.7.2.1, 4.7.2.2, 4.7.1.1, 4.7.1.4, 4.7.3.1; AQA-8464 (v1.1) §5.7.1.4 (confirms no Combined equivalent). Route audit `route-audit/chemistry.md` row 82 (chem-only, OK).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n, read against option n. `higher` TF copy `null` → served on TH only.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 | — | none (8464 5.7.1.4: "Students do not need to know the formulae or names of individual alkenes.") | — |
| 8462 | **4.7.2.1** | Structure and formulae of alkenes — under 4.7.2 "Reactions of alkenes and alcohols (chemistry only)" | triple |
| Supporting | 8462 4.7.1.4 (bromine-water test, cracking — base); 4.7.2.2 (functional group C=C — triple) | | base / triple |

Spec statements (verbatim): "Alkenes are hydrocarbons with a double carbon-carbon bond. The general formula for the homologous series of alkenes is CnH2n" "Alkene molecules are unsaturated because they contain two fewer hydrogen atoms than the alkane with the same number of carbon atoms." "The first four members of the homologous series of alkenes are ethene, propene, butene and pentene." "Alkene molecules can be represented in the following forms: C3H6 or [displayed formula]." "Students do not need to know the names of individual alkenes other than ethene, propene, butene and pentene." Skills: "Recognise substances that are alkenes from their names or from given formulae in these forms." MS 5b.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Alkene = hydrocarbon with C=C; CₙH₂ₙ (theory 1; equation; key_note) | triple | 4.7.2.1 | TF TH | OK |
| R2 | Unsaturated = two fewer H than the alkane (theory 1; common_mistake) | triple | 4.7.2.1 | TF TH | OK |
| R3 | First four: ethene, propene, butene, pentene (theory 1, 2) | triple | 4.7.2.1 | TF TH | OK |
| R4 | More reactive than alkanes; functional group C=C (theory 1) | triple (reactivity also base 4.7.1.4) | 4.7.2.2; 4.7.1.4 | TF TH | OK |
| R5 | Representations: molecular, displayed (theory 2) | triple | 4.7.2.1 | TF TH | WRONG label (C6) |
| R6 | Skeletal formula (theory 2) | none | — | TF TH | OFF-SPEC (C7) |
| R7 | Bromine-water test (theory 2; common_mistake; q2) | base (taught on every route in cracking-alkenes) | 4.7.1.4 | TF TH | OK |
| R8 | Homologous series features (theory 3) | triple (series defined 4.7.1.1 base) | 4.7.2.1; 4.7.1.1 | TF TH | OK |
| R9 | Alkane vs alkene comparison; cracking produces alkenes; poly(ethene) (theory 3) | base / triple | 4.7.1.4; 4.7.3.1 | TF TH | OK |
| R10 | `higher`: pi bond weaker than sigma | none (A-level) | — | TH | OFF-SPEC (F4) |
| R11 | `higher`: structural isomers; IUPAC position of double bond | none | — ("do not need to know the names of individual alkenes other than ethene, propene, butene and pentene") | TH | OFF-SPEC (F4) |
| R12 | q1 (butene formula) | triple | 4.7.2.1 | TF TH | key OK; wx3 WRONG (C17) |
| R13 | q2 (ethene vs ethane, bromine water) | base | 4.7.1.4 | TF TH | key OK; wx2 WRONG (C20) |
| — | rp, fifas, examiner_tip | none | — | — | correct; 4.7.2.1 has no HT content |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | theory 1 | hydrocarbons with C=C; CₙH₂ₙ; C₂H₄, C₃H₆, C₄H₈, C₅H₁₀ | OK | ✓ | 4.7.2.1 |
| C2 | theory 1 | unsaturated: fewer H than maximum; two fewer than the alkane | OK | Spec wording is the second clause — lead with it. | 4.7.2.1 |
| C3 | theory 1 | ethane C₂H₆ vs ethene C₂H₄ | OK | — | — |
| C4 | theory 1 | much more reactive; alkanes relatively inert; addition reactions | OK | — | 4.7.1.4; 4.7.2.2 |
| C5 | theory 1 | C=C is the functional group; all alkenes react similarly | OK | Spec: "It is the generality of reactions of functional groups that determine the reactions of organic compounds." | 4.7.2.2 |
| C6 | theory 2 | "DISPLAYED FORMULA (structural formula): shows all bonds and atoms. Ethene: H₂C=CH₂ … Propene: CH₃-CH=CH₂" | WRONG | H₂C=CH₂ and CH₃-CH=CH₂ are condensed **structural** formulae, not displayed formulae. A displayed formula draws every atom and every bond (each C–H as a line). AQA does not credit a condensed formula where a displayed formula is asked for. Design draws true displayed formulae (figlib `displayed_formula`). | 4.7.2.1; 4.7.2.2 ("draw fully displayed structural formulae") |
| C7 | theory 2 | SKELETAL FORMULA | OFF-SPEC | Not an AQA GCSE representation. Cut. | 4.7.2.1 |
| C8 | theory 2 | propene double bond C1–C2; butene positional | OK | Beyond spec, true. Butene isomers not required. | — |
| C9 | theory 2 | bromine water orange/yellow → colourless with alkene; no change with alkane | OK | AQA: "orange to colourless"; "clear" not credited. | 4.7.1.4 |
| C10 | theory 3 | homologous series: same general formula, same functional group, similar chemical properties, gradual physical change, differ by CH₂ | OK | — | 4.7.1.1 |
| C11 | theory 3 | bp and density increase with chain length | OK | — | — |
| C12 | theory 3 | alkanes fuels; alkenes for polymers and other chemicals | OK | — | 4.7.1.4 |
| C13 | theory 3 | cracking → shorter alkanes + alkenes; ethene → poly(ethene) | OK | — | 4.7.1.4; 4.7.3.1 |
| C14 | common_mistake; key_note | as above | OK | — | — |
| C15 | q1 key | butene C₄H₈ | OK | ✓ | 4.7.2.1 |
| C16 | q1 wx1 ↔ opt 1 (C₄H₁₀) / wx2 ↔ opt 2 (C₄H₆) | butane; two double bonds → C₄H₆ | OK | Aligned ✓ (C₄H₆ = two C=C ✓) | — |
| C17 | q1 wx3 ↔ opt 3 (C₄H₄) | "C₄H₄ would require two double bonds or a ring" | WRONG | Aligned, but false: two C=C gives C₄H₆ (wx2 says so); a ring alone gives C₄H₈. C₄H₄ needs three such features. Correct line: "C₄H₄ has four too few hydrogens — one C=C gives CₙH₂ₙ = C₄H₈." Do not use q1 as written. | 4.7.2.1 |
| C18 | q2 key | ethene decolourises orange bromine water; ethane no effect | OK | ✓ | 4.7.1.4 |
| C19 | q2 wx1 ↔ opt 1 | alkanes unreactive, don't decolourise | OK | Aligned ✓ | — |
| C20 | q2 wx2 ↔ opt 2 ("Both decolourise … ethene reacts faster") | "Both alkenes AND alkanes would decolourise — but the test is specific to the C=C double bond which ONLY alkenes have." | WRONG | Aligned, but the opening clause states the misconception as fact (alkanes do **not** decolourise bromine water) and then contradicts itself. Correct line: "Ethane does not decolourise bromine water at all — only C=C reacts." Do not use q2 as written. | 4.7.1.4 |
| C21 | q2 wx3 ↔ opt 3 | bromine water is the standard test | OK | Aligned ✓ | — |
| C22 | matching (to be replaced) | ethene, propene ("polypropylene" — AQA writes poly(propene)) | OK | Use "poly(propene)". | 4.7.3.1 |

No `[NEW — to be examined]` Convert lines in this file. Count: **3 WRONG** (C6 theory, re-cuttable; C17 and C20 frozen wx → neither quiz item usable as written); OFF-SPEC C7 and `higher`.

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| q1 | wx3 false (C₄H₄ "two double bonds or a ring") | Do not use as written (F1). |
| q2 | wx2 opens by asserting alkanes decolourise bromine water | Do not use as written (F2). |

## 5. Verdict
SOURCE HAS ERRORS. Core science right (CₙH₂ₙ, unsaturated, first four, bromine water). Theory mislabels condensed formulae as displayed formulae — the exact representation the spec demands. Both frozen quiz items carry a false wrong-explanation, so **0 of 2 usable as written**. `higher` is A-level/off-spec; 4.7.2.1 has no HT content. Nothing for Mide.
