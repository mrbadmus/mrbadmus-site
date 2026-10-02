# Examination — Testing for Gases (testing-for-gases) — AQA 8464 5.8.2.1–5.8.2.4 / 8462 4.8.2.1–4.8.2.4
Verdict: SOURCE HAS ERRORS
Examiner: Opus, 2 Oct 2026. Pack examined: `docs/ks4/packs/batch-14/04-checked-science-source/chemistry-5.8.2.1-testing-for-gases.md`.
Spec sources read as text: `AQA-8464-spec.txt` (v1.1, 04 Oct 2019) §5.8.2.1–5.8.2.4; `AQA-8462-spec.txt` (v1.1, 04 Oct 2019) §4.8.2.1–4.8.2.4, §4.8.3.3. Route audit row `testing-for-gases` (CF CH TF TH, base).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks. Both `higher` route copies are `null`.

## 1. Spec reference
| spec | section | title | label |
|---|---|---|---|
| 8464 / 8462 | **5.8.2.1 / 4.8.2.1** | Test for hydrogen | base |
| 8464 / 8462 | **5.8.2.2 / 4.8.2.2** | Test for oxygen | base |
| 8464 / 8462 | **5.8.2.3 / 4.8.2.3** | Test for carbon dioxide | base |
| 8464 / 8462 | **5.8.2.4 / 4.8.2.4** | Test for chlorine | base |
| Supporting | 8464 5.1.1.1 / 8462 4.1.1.1 (balanced symbol equations) | | base |

Spec statements (verbatim, 8464 = 8462): "The test for hydrogen uses a burning splint held at the open end of a test tube of the gas. Hydrogen burns rapidly with a pop sound." · "The test for oxygen uses a glowing splint inserted into a test tube of the gas. The splint relights in oxygen." · "The test for carbon dioxide uses an aqueous solution of calcium hydroxide (lime water). When carbon dioxide is shaken with or bubbled through limewater the limewater turns milky (cloudy)." · "The test for chlorine uses litmus paper. When damp litmus paper is put into chlorine gas the litmus paper is bleached and turns white."

## 2. Route table
| # | teachable point | true layer | spec | verdict |
|---|---|---|---|---|
| R1 | H₂: burning splint → pop (th1, th3, common_mistake, key_note) | base | 5.8.2.1 / 4.8.2.1 | OK; equation WRONG (TG-F1) |
| R2 | O₂: glowing splint → relights (th1, th3, common_mistake, key_note, q1) | base | 5.8.2.2 / 4.8.2.2 | OK |
| R3 | CO₂: limewater → milky (th2, th3, key_note, equations 1) | base | 5.8.2.3 / 4.8.2.3 | OK |
| R4 | Cl₂: damp litmus → bleached white (th2, th3, common_mistake, key_note, q2) | base | 5.8.2.4 / 4.8.2.4 | OK |
| R5 | Why: CO₂ + Ca(OH)₂ → CaCO₃ + H₂O; 2H₂ + O₂ → 2H₂O (th1, th2, equations, `higher`) | base (balanced equations) | 5.1.1.1 / 4.1.1.1 | OK where balanced |
| R6 | Why: Cl₂ + H₂O → HCl + HClO; excess CO₂ re-clears limewater (th2, equations 2, q2 key) | off-spec enrichment, any route | — | OFF-SPEC (TG-F4) |
| R7 | `higher`: ionic equation; bleaching mechanism; combustion; identify unknowns | **not a layer**. No HT statement in 5.8.2 | 5.8.2 | ROUTE (TG-F3) |

True page routes: CF CH TF TH, all base, no HT or triple layer. Matches what the site ships.

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | lit splint near the mouth → squeaky pop | OK | Spec: burning splint at the open end; "pop". "Squeaky pop" is accepted. | 5.8.2.1 |
| C2 | th1 | "H₂ + O₂ → H₂O (explosive combustion)" | WRONG | Not balanced. 2H₂ + O₂ → 2H₂O (the `higher` field has it right). | 5.1.1.1 (TG-F1) |
| C3 | th1 | "Hydrogen is the lightest gas — produces a very fast, audible pop" | IMPRECISE | Being light is not why it pops. The pop is the rapid combustion of the hydrogen–air mixture. | 5.8.2.1 (TG-F2) |
| C4 | th1 | glowing splint relights in oxygen; a lit splint just burns brighter | OK | — | 5.8.2.2 |
| C5 | th2 | limewater = calcium hydroxide solution; turns milky; CO₂ + Ca(OH)₂ → CaCO₃ + H₂O; CaCO₃ insoluble white precipitate | OK | Balanced ✓. | 5.8.2.3 |
| C6 | th2 | excess CO₂ re-dissolves the precipitate: CaCO₃ + H₂O + CO₂ → Ca(HCO₃)₂ | OK, OFF-SPEC | Correct and balanced, but not on the spec. | (TG-F4) |
| C7 | th2 | damp litmus (or damp universal indicator) paper bleached white | OK | Spec names litmus. Teach litmus. | 5.8.2.4 |
| C8 | th2; equations 2 | Cl₂ + H₂O → HCl + HClO; HClO is the bleach; paper must be damp | OK, OFF-SPEC | Balanced ✓ and correct. The equation is not on the spec. "Damp" is. | 5.8.2.4 (TG-F4) |
| C9 | th3 | summary table; common confusions | OK | — | 5.8.2 |
| C10 | `higher` | "ionic equation: Ca²⁺ + CO₃²⁻ → CaCO₃" | IMPRECISE / OFF-SPEC | Limewater contains no carbonate ions until CO₂ reacts with OH⁻. Not on the spec, and not HT. | (TG-F3) |
| C11 | `higher` | 2H₂ + O₂ → 2H₂O | OK | Base, not HT. | 5.1.1.1 |
| C12 | common_mistake | "limewater turns milky with CO₂, not just any acidic gas" | IMPRECISE (minor) | Sulfur dioxide also turns limewater milky. At GCSE limewater is the CO₂ test. Drop "not just any acidic gas". | 5.8.2.3 |
| C13 | key_note | four tests | OK | — | 5.8.2 |
| C14 | equations 1, 2 | as C5, C8 | OK | Both balanced. | — |
| C15 | q1 key | glowing splint relights → oxygen | OK | — | 5.8.2.2 |
| C16 | q1 opt 1 / wx1 | hydrogen uses a lit splint, gives a pop | OK | Aligned ✓. | 5.8.2.1 |
| C17 | q1 opt 2 / wx2 | CO₂ does not support combustion | OK | Aligned ✓. | — |
| C18 | q1 opt 3 / wx3 | "it doesn't reliably relight a glowing splint" | OK (minor wording) | Aligned ✓. "reliably" is a needless hedge. Usable. | 5.8.2.4 |
| C19 | q2 key | Cl₂ must dissolve in water to form HClO, the bleaching agent | OK | Correct. HClO is beyond the spec, but the creditable point ("needs water") is right. Usable on every route. | 5.8.2.4 |
| C20 | q2 opt 1 / wx1 | chlorine is not flammable | OK | Aligned ✓. | — |
| C21 | q2 opt 2 / wx2 | denser than air is not why it must be damp | OK | Aligned ✓. | — |
| C22 | q2 opt 3 / wx3 | water is needed chemically | OK | Aligned ✓. | — |
| C23 | matching (to be replaced) | all pairs | OK | — | — |

Count: **1 WRONG** (C2, theory, re-cuttable). IMPRECISE: C3, C10, C12. OFF-SPEC: C6, C8 (correct enrichment). ROUTE: `higher` field.

## 4. Frozen items wrong for their route
None. **q1 and q2 are usable on all four routes.**

## 5. For the lesson author
**Misconceptions seen in AQA marking:** lit vs glowing splint swapped; "the splint goes out with a pop" (no mark); "limewater turns cloudy" given as the CO₂ test without naming limewater; "litmus turns red" for chlorine (the mark is bleached/white); dry litmus; "chlorine turns litmus blue".

**Command words:** Describe a test for… (test + result, 2 marks), Identify the gas, Give the result.

**Typical questions** ⚑ examiner-drafted
- *Describe a test for oxygen. Give the result. [2]* — glowing splint (1); relights (1).
- *Describe the test for chlorine. [2]* — damp litmus paper (1); bleached / turns white (1).
- *A gas turns limewater milky. Name the gas. [1]* — carbon dioxide.

## 6. Verdict
SOURCE HAS ERRORS, but only in re-cuttable theory: the unbalanced H₂ combustion equation (TG-F1). All four spec tests are present and correct, and both quiz items work on every route. The `higher` field is not a Higher layer (TG-F3). The Cl₂/HClO and excess-CO₂ equations are correct but off-spec (TG-F4). No question for Mide.
