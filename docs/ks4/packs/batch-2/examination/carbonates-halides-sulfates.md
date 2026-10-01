# Examination — Tests for Carbonates, Halides and Sulfates (carbonates-halides-sulfates) — not in 8464 · AQA 8462 4.8.3.3–4.8.3.5 (chemistry only) + Required practical 7
Verdict: SOURCE OK WITH FLAGS
Examiner: Opus, 1 Oct 2026. Pack examined: `docs/ks4/packs/batch-2/chemistry-4.8.3.3-carbonates-halides-sulfates.md`.
Spec sources fetched from filestore.aqa.org.uk and read as text: AQA-8462-SP-2016.PDF and AQA-8464-SP-2016.PDF, both Version 1.1, 04 Oct 2019. 8464 has the CO₂ *gas* test (5.8.2.3, limewater) but no anion tests.
Route copies, checked directly: the record exists only in TF and TH. They differ only in `higher` (TF `null`).

Conventions: q1–q2 = quiz items; "wx n" = `wrong_explanations` key n; th1–th3 = theory chunks.

## 1. Spec reference
| spec | section | title | page | label |
|---|---|---|---|---|
| 8464 | — | **not in 8464** (only the gas test for CO₂, 5.8.2.3, is shared) | — | — |
| 8462 | **4.8.3.3** | Carbonates | p.74 | triple |
| 8462 | **4.8.3.4** | Halides | p.74 | triple |
| 8462 | **4.8.3.5** | Sulfates | p.74 | triple |
| 8462 | **RP7** (Appendix 8.2.7) | "use of chemical tests to identify the ions in unknown single ionic compounds covering the ions from sections Flame tests … to Sulfates" | p.74; p.107 | triple |
| 8462 | 4.8.2.3 / 8464 5.8.2.3 | Test for carbon dioxide (limewater) | — | base, both specs |
| 8462 | 4.1.1.1 | "(HT only) … ionic equations" | p.18 | triple-higher here |

BATCH-PLAN ("— · 8462 4.8.3.3–4.8.3.5 · TF TH · REQUIRED PRACTICAL") is right.

Spec statements (verbatim):
- 4.8.3.3: "Carbonates react with dilute acids to form carbon dioxide gas. Carbon dioxide can be identified with limewater."
- 4.8.3.4: "Halide ions in solution produce precipitates with silver nitrate solution in the presence of dilute nitric acid. Silver chloride is white, silver bromide is cream and silver iodide is yellow."
- 4.8.3.5: "Sulfate ions in solution produce a white precipitate with barium chloride solution in the presence of dilute hydrochloric acid."

**`rp` field:** "RP Chemistry 4 (chemistry-only)" is the **wrong number**. The practical is **8462 Required practical 7**. RP4 is temperature changes. There is no Combined equivalent.

## 2. Route table
| # | teachable point | true layer | spec | live route copy | verdict |
|---|---|---|---|---|---|
| R1 | Carbonate test: dilute acid → fizzing → CO₂ → limewater milky (th1; key_note; matching) | triple (the limewater test itself is base in both specs) | 4.8.3.3; 4.8.2.3 | TF, TH | OK |
| R2 | Full symbol equations: Na₂CO₃ + 2HCl → …; CO₂ + Ca(OH)₂ → CaCO₃ + H₂O (th1) | triple | 4.1.1.1 ("write formulae and balanced chemical equations for the reactions in this specification") | TF, TH | OK |
| R3 | Sulfite / SO₂ paragraph (th1) | **NOT-IN-SPEC**, and partly wrong (C5) | — | TF, TH | Cut. |
| R4 | Halide test: HNO₃ then AgNO₃; white / cream / yellow (th2; common_mistake; key_note; matching) | triple | 4.8.3.4 | TF, TH | OK |
| R5 | Sulfate test: HCl then BaCl₂ → white BaSO₄ (th3; key_note; q2) | triple | 4.8.3.5 | TF, TH | OK |
| R6 | Ionic equations Ag⁺ + X⁻ → AgX; Ba²⁺ + SO₄²⁻ → BaSO₄; CO₃²⁻ + 2H⁺ → H₂O + CO₂ (th2; th3; equations; `higher`) | **triple-higher** | 4.1.1.1 (HT only) | th2, th3 and equations: TF and TH. `higher`: TH. | **HT content shown as base on TF.** Tag it `triple-higher`. |
| R7 | Why acidify first (th2; th3; q1; common_mistake; `higher` "Explain the need for acidification") | **triple** (base) | 4.8.3.4–4.8.3.5 ("in the presence of dilute nitric / hydrochloric acid"); RP7 | th2, th3 and q1: TF and TH ✓. `higher` copy: TH only. | The TH-only `higher` sentence is base content withheld from TF. It is harmless, since th2/th3 already teach it to TF. Tag it `triple`. |
| R8 | Identifying an unknown compound by combining cation and anion tests (`higher`) | **triple** (base) | 4.8.3.1 ("identify species from the results of the tests in 4.8.3.1 to 4.8.3.5"); RP7 | TH only | **Base content withheld from TF.** This is the RP7 task itself. |

## 3. Check table
| # | item | claim | verdict | correction / note | citation |
|---|---|---|---|---|---|
| C1 | th1 | add dilute HCl (or another dilute acid); fizzing → CO₂; bubble through limewater (calcium hydroxide solution); milky / cloudy | OK | — | 4.8.3.3; 4.8.2.3 |
| C2 | th1 | Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂ | OK | It is balanced. | 4.1.1.1 |
| C3 | th1 | CO₂ + Ca(OH)₂ → CaCO₃ + H₂O | OK | It is balanced. This equation is beyond the spec's demand (4.8.2.3 needs only the observation), but correct. | 4.8.2.3 |
| C4 | th1 | "sulfites (SO₃²⁻) — they produce SO₂ with acid, which also turns limewater cloudy" | OK (chemistry) / NOT-IN-SPEC | SO₂ does turn limewater milky (CaSO₃). This is beyond the spec. | — |
| C5 | th1 | "To distinguish: use acidified silver nitrate solution (sulfite gives precipitate in different conditions)." | **WRONG** | This is not a valid or meaningful way to tell sulfite from carbonate. The standard method uses SO₂'s reducing action, for example decolourising acidified potassium manganate(VII). None of it is in the AQA spec. Cut the whole sulfite paragraph. | — |
| C6 | th2 steps | acidify with dilute nitric acid; add silver nitrate; colour | OK | — | 4.8.3.4 |
| C7 | th2 | "acidify to remove interfering ions like CO₃²⁻ or SO₄²⁻" | **WRONG (sulfate)** | Dilute nitric acid removes **carbonate** (as CO₂), and any hydroxide ions. It does **not** remove sulfate ions: there is no reaction, and sulfate stays in solution. AQA mark schemes credit "to remove carbonate ions", or "to react with carbonate ions, which would also give a precipitate with silver nitrate". | 4.8.3.4; 4.8.3.3 |
| C8 | th2 | AgCl white, AgBr cream, AgI yellow | OK | Verbatim spec. | 4.8.3.4 |
| C9 | th2 | ionic equations Ag⁺ + Cl⁻/Br⁻/I⁻ → AgX(s) | OK (science) / route **triple-higher** | See R6. | 4.1.1.1 HT |
| C10 | th2 | "Why nitric acid first? To remove CO₃²⁻ and SO₄²⁻…" | **WRONG (sulfate)** | Same as C7. | 4.8.3.4 |
| C11 | th3 steps | acidify with dilute HCl; add BaCl₂; white BaSO₄ | OK | — | 4.8.3.5 |
| C12 | th3 | Ba²⁺ + SO₄²⁻ → BaSO₄ | OK / triple-higher | — | 4.1.1.1 HT |
| C13 | th3 | "Carbonate ions also form a white precipitate with Ba²⁺ (BaCO₃). Adding HCl removes carbonate as CO₂ first" | OK | This is the correct reason. | 4.8.3.5 |
| C14 | th3 summary | five-line summary | OK | — | 4.8.3.3–4.8.3.5 |
| C15 | `higher` | ionic equations including CO₃²⁻ + 2H⁺ → H₂O + CO₂ | OK / triple-higher | All are balanced. | 4.1.1.1 HT |
| C16 | `higher` | "Identify an unknown ionic compound from a combination of systematic cation and anion tests" | OK (science) / route **triple** (base) | See R8. | 4.8.3.1; RP7 |
| C17 | `higher` | "Explain the need for acidification at each stage" | OK / route **triple** | See R7. | 4.8.3.4–4.8.3.5 |
| C18 | common_mistake | always acidify first; use HNO₃ for halides, not HCl (adds Cl⁻); HCl for sulfates (removes carbonates) | OK | Add the parallel trap: never acidify the sulfate test with **sulfuric** acid, because it adds sulfate ions. | 4.8.3.4–4.8.3.5 |
| C19 | key_note | "Always acidify first to remove interfering ions" | OK | It does not repeat the sulfate error. | — |
| C20 | equations 1 | "Carbonate: acid + CO₃²⁻ → CO₂ (turns limewater milky)" | IMPRECISE | This is not a balanced equation. Present it as a test summary, not in the `equation` block. | — |
| C21 | equations 2–3 | Ag⁺ + X⁻ → AgX; Ba²⁺ + SO₄²⁻ → BaSO₄ | OK / triple-higher | — | 4.1.1.1 HT |
| C22 | rp | "RP Chemistry 4 … Test for anions…" | **WRONG (number)** | 8462 **RP7**. The content description is right. | 8462 p.74; Appendix 8.2.7 |
| C23 | matching (to be replaced) | five anion rows | OK | — | — |
| C24 | q1 key | "To remove carbonate **and sulfate** ions that would also form precipitates with silver nitrate…" | **WRONG (in part)** | Nitric acid does not remove sulfate (C7). It is still the best option of the four, but its stated reason is half false. | 4.8.3.4 |
| C25 | q1 wx1 | "its role is REMOVAL OF INTERFERING IONS (carbonates, sulfates)" | **WRONG (in part)** | Same error. | — |
| C26 | q1 wx2, wx3 | AgNO₃ is stable in solution; nitric acid contains no silver | OK | — | — |
| C27 | q2 key | white precipitate with BaCl₂ after acidification → sulfate | OK | — | 4.8.3.5 |
| C28 | q2 wx1 | acidification removes carbonate as CO₂ | OK | — | 4.8.3.5 |
| C29 | q2 wx2, wx3 | BaCl₂ soluble; BaBr₂ soluble | OK | — | — |

## 4. Frozen items wrong for their route
| item | why | recommendation |
|---|---|---|
| TF, TH · q1 · "Why must solutions be acidified with nitric acid before adding silver nitrate…" | The keyed answer and wx1 both state that nitric acid removes **sulfate** ions, which is false. A pupil who learns the keyed reason would write a half-wrong answer. | Keep verbatim. **Do not use it as a ladder rung on either route, and do not quote it in the body.** Teach the reason ("to remove carbonate ions, which would also form a precipitate") in new text and a new check item. |
| TF, TH · q2 · "A white precipitate forms when barium chloride is added to an acidified solution…" | Clean. | Usable as rung 1 or 2 on both routes. |

No frozen item is route-wrong. Both are triple. The route issues are all in theory, `higher` and equations (R6–R8).

## 5. For the lesson author

**Misconceptions commonly seen**
- **Acidifying the halide test with HCl** (adds Cl⁻, so every sample "contains chloride"), or the sulfate test with H₂SO₄ (adds SO₄²⁻).
- **"The acid removes sulfate"**, which the source itself teaches (C7).
- **Adding limewater to the solid or the solution**, instead of bubbling the gas through it.
- **"Fizzing proves a carbonate."** A reactive metal also fizzes (H₂). The *gas* must be tested.
- **Cream vs yellow confusion** (bromide vs iodide). Pupils also learn "silver chloride is white" but write "silver precipitate".
- **Writing "silver nitrate turns white"** instead of "a white precipitate forms".
- **Thinking the anion tests identify the metal**, or the reverse: that NaOH identifies the anion.

**Command words:** Describe (test and result), Give, Identify, Explain (why acidify / why a particular acid), Suggest, Plan (RP7), Write (equation; ionic is HT).

**Typical questions (⚑ examiner-drafted)**
- ⚑ examiner-drafted, 3 marks, Describe, **triple**: *"Describe a test to show that a solution contains bromide ions. Give the result."*
  - (1) Add dilute nitric acid.
  - (1) Add silver nitrate solution.
  - (1) A cream precipitate.
- ⚑ examiner-drafted, 2 marks, Explain, **triple**: *"Explain why dilute hydrochloric acid is added before barium chloride solution in the test for sulfate ions."*
  - (1) To remove, or react with, carbonate ions.
  - (1) Carbonate would also form a white precipitate (barium carbonate) with barium chloride, giving a false positive.
- ⚑ examiner-drafted, 1 mark, Explain, **triple**: *"Why is hydrochloric acid not used to acidify the halide test?"*
  - (1) It contains or adds chloride ions, which would give a white precipitate whatever the sample.
- ⚑ examiner-drafted, 2 marks, Write, **triple-higher**: *"Write the ionic equation for the reaction in a positive sulfate test."*
  - (1) Ba²⁺ + SO₄²⁻ → BaSO₄.
  - (1) State symbols: (aq) + (aq) → (s).
- ⚑ examiner-drafted, 6 marks, levels of response, Plan, **triple** (RP7): *"A student has three white solids: sodium carbonate, sodium sulfate and sodium iodide. Describe tests the student could use to identify each solid. Give the results."*
  - Level 3 (5–6): a logical sequence that identifies all three, with correct reagents, including the acidification step and the correct acid, and correct results.
  - Level 2 (3–4): identifies two correctly with results, or all three with minor omissions (for example missing acidification).
  - Level 1 (1–2): one correct test or result.
  - Indicative content:
    - dissolve each in distilled water
    - dilute acid: only the carbonate fizzes; the gas turns limewater milky
    - dilute HNO₃ + AgNO₃: a yellow precipitate shows iodide
    - dilute HCl + BaCl₂: a white precipitate shows sulfate
    - separate fresh samples for each test
    - (sodium shared by all: yellow flame; not needed to distinguish them)

**Required practical: 8462 RP7** (anion part)
- **Method:**
  - Dissolve a small amount of each solid in distilled water.
  - **Carbonate:** add dilute HCl in a test tube fitted with a delivery tube, and bubble the gas through limewater.
  - **Halide:** add a few drops of dilute HNO₃, then a few drops of AgNO₃(aq), and record the precipitate colour.
  - **Sulfate:** add a few drops of dilute HCl, then a few drops of BaCl₂(aq), and look for a white precipitate.
  - Use fresh samples for each test.
- **Variables:** not a variables investigation. Control the use of small volumes and separate samples, and do not cross-contaminate droppers.
- **Risks:**

  | hazard | control |
  |---|---|
  | barium chloride is toxic if swallowed | avoid ingestion, wash hands |
  | silver nitrate stains skin and is an irritant (corrosive at higher concentration) | wear gloves or avoid skin contact |
  | dilute acids are irritants | wear eye protection |
  | a stoppered tube with gas evolving can build pressure | use a delivery tube, never a sealed tube |

- **Typical results:** Na₂CO₃ fizzes, and limewater turns milky within seconds. Halides give white / cream / yellow precipitates; cream and yellow can look similar in poor light, so compare them side by side. Sulfate gives a dense white precipitate.

**Equations to learn (recalled)**
- Full: Na₂CO₃ + 2HCl → 2NaCl + H₂O + CO₂ (and the like). **Triple.** The test observations themselves are also triple.
- Ionic: Ag⁺ + X⁻ → AgX; Ba²⁺ + SO₄²⁻ → BaSO₄; CO₃²⁻ + 2H⁺ → H₂O + CO₂, with state symbols. **Triple-higher.**

## 6. Verdict
**SOURCE OK WITH FLAGS.**
- **Route corrections (3).**
  - Ionic equations are shown as base on TF.
  - "Identify an unknown compound by combining tests" is base RP7 content, but is withheld from TF in `higher`.
  - "Explain acidification" is also in the TH-only `higher` field, though th2/th3 already cover it for TF.
- **WRONG (5).**
  - "Nitric acid removes sulfate", in th2 twice, the q1 key and q1 wx1. The q1 instances are frozen.
  - The sulfite distinguishing method.
  - The `rp` number: RP4, which should be RP7.
- **NOT-IN-SPEC (1).** The sulfite paragraph.
- **IMPRECISE (1).** The carbonate "equation" in the equations field.
- **The `rp` field:** a real AQA RP with the **wrong number**. It is 8462 RP7, and there is no Combined equivalent.

Only Mide can rule: **none.**

Note for the commander: there is no `examiner_tip`.
