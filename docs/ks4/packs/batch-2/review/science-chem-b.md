# Science review — batch 2, group chem-b

Reviewer: Opus, acting as a fresh AQA GCSE examiner, 1 Oct 2026. I wrote none of these lessons.
Lessons: percentage-yield, titrations, metal-hydroxides, carbonates-halides-sulfates.

**Evidence used**
- Spec text: AQA 8462 v1.1 (04 Oct 2019), read as text. I checked 4.3.3.1, 4.4.2.5, 4.8.3.1–4.8.3.5, 4.1.1.1 (the "(HT only) … ionic equations" bullet, line 631) and Appendix 8.2.1, 8.2.2 and 8.2.7 (RP1, RP2, RP7). 8464 has none of these four points, so all four are chemistry-only (TF and TH).
- Sources: each `.dc.html`, the template and the whole Component logic, so verdicts, feedback, rung keys, tolerances and marking points are covered.
- Records: `ks4_lessons/batch_2.py`, including the routes and withholds.
- Verbatim quiz data: `shared/ks4-source-batch-2.js`, as built.
- Built pages: all eight, on both routes, read two ways:
  - as prerendered HTML;
  - at runtime in headless Chrome (light scheme, 1280 px, local server on 8714). The text was compared TF against TH. That is how I confirmed which rung, key-note line and bank each route actually gets.

**Route check, all four lessons**
- Every `data-route="higher"` block is present on TH and absent on TF.
- Every `R.isHigher` branch resolves correctly at runtime, covering rung 2, key-note line 6/7/8 and the "Contains Higher" chip.
- No Combined page exists, which is correct.
- Nothing HT reaches a TF pupil through authored text.
- The only HT notation on TF is inside one frozen quiz option (A-7).

---

## 1. percentage-yield — 8462 4.3.3.1 (chemistry only), TF + TH

**Route-by-route**

| route | what ships | check |
|---|---|---|
| TF | Shared sections: hook; yield bench (RP1 context); 108 % misconception; reason sort; Haber explainer; "which working" check; equation; CFIFA (frozen FIFA + kg example + 2 questions). Ladder: r1 frozen q2, rung2 `rungTF` (3.20 kg / 2600 g → 81.25 %), r3 chain, r4 calc + give. Key note: 5 lines. Bank: q2 only. | All base 4.3.3.1. No moles, limiting reactant or n = m ÷ Mr anywhere on the page (confirmed at runtime). |
| TH | All of the TF content, plus: the moles chain on the equation card, `s-theory` (theoretical yield from reactant mass, 2 examples, 2 questions), rung 2 `rungTH` (MgCO₃ → MgO, 80 %), and key-note line 6. | HT bullet of 4.3.3.1, plus 4.3.2.4 (limiting reactant), placed correctly. |

**Arithmetic, re-done by hand**

All correct:
- 8.64 ÷ 8.0 = 108 %
- 8.0 ÷ 6.2 = 129 %; 22.5 % and 0.775 are both right
- 1900 ÷ 2500 = 76 %, and the unconverted 76 000 %
- 34 ÷ 40 = 85 %, with 118 % if the fraction is inverted
- 960 ÷ 1200 = 80 %, and the unconverted 80 000 %
- 2600 ÷ 3200 = 81.25 % (tolerance 0.3 accepts 81)
- CaCO₃: 0.120 mol → 6.72 g → 83.3 %
- CaCO₃ from 1.00 kg: 10.0 mol → 560 g → 85 %, and the unconverted 85 000 %
- Haber: 0.10 mol N₂ → 0.20 mol NH₃ → 3.4 g → 15 %
- Fe₂O₃ (balanced ✓): 100 mol → 200 mol Fe → 11 200 g → 87.5 %, with 175 % if the 1 : 2 ratio is missed
- MgCO₃ (Mr 84 ✓): 0.025 mol → 1.00 g MgO → 80 %
- Rung 4: 9.0 ÷ 12.0 = 75 %
- Bench losses: 0.5 + 0.3 + 0.8 + 0.2 = 1.8 g ✓

**Examination flags, all resolved**
- The catalyst "practical tip", the "impure reactants" reason, "100 % impossible" and the HT moles common_mistake are not used on the page.
- The page now teaches the opposite of the catalyst tip: the sort, the r3 herring and the r4 reject all say a catalyst changes rate, not yield.
- The frozen q1 (bad distractor) is withheld (B2-W8) and confirmed absent from `ks4-source-batch-2.js` on both routes.

**Frozen items still served that should be withheld:** none. q2 is clean.

### REQUIRED
| # | lesson · route | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-1 | percentage-yield · TF, TH | logic `rungs.r4.points[2]` and `points[3]` | OLD `points[2]`: `'Reason: some product is lost when it is separated from the reaction mixture (e.g. left on filter paper or glassware, or in solution).'` → NEW: `'First reason, any one of: some product is lost when it is separated from the reaction mixture (e.g. left on filter paper or glassware, or in solution); the reaction is reversible, so it does not go to completion; some reactants react in a different way (side reactions).'` · OLD `points[3]`: `'Reason: the reaction may not go to completion because it is reversible, or some reactants react in a different way (side reactions).'` → NEW: `'Second reason: a different one of those three.'` | As written, the two reason marks are tied to fixed reasons: mark 3 is separation losses, and mark 4 is reversible OR side reactions. A pupil who answers "it is reversible" and "side reactions" gives two creditworthy reasons but can only tick mark 4, so self-marks 3/4. AQA credits any two of the three spec reasons. | 8462 4.3.3.1 (the three reasons are listed with equal standing) |

### ADVISORY
| # | where | note |
|---|---|---|
| A-1 | `s-reasons` `done-note` | "A catalyst or a powder changes how fast, never how much." If a reaction is stopped before it finishes, a faster rate *can* raise the actual yield. Tighter wording: `… changes how fast, never the maximum mass of product.` The item `why` texts already say this correctly. |
| A-2 | `htExamples[0]` Answer line `'Percentage yield = 83.3%'` | The data are to 2 s.f. (5.6 g), so 83 % is the consistent answer. AQA accepts 83.3 unless a precision is asked for. Optional: `'Percentage yield = 83.3% (83%)'`, matching the style of `rungTF.model`. |

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-1 only).

---

## 2. titrations — 8462 4.4.2.5 (chemistry only) + RP2, TF + TH

**Route-by-route**

| route | what ships | check |
|---|---|---|
| TF | Shared sections: hook (phenolphthalein end point); RP2 method, variables and risks; burette-rinse misconception; indicator choice (UI unsuitable); burette simulation (rough run, accurate runs, concordance picker); mean-titre equation; CFIFA (frozen FIFA + dm³ example + 2 questions). Ladder: r1 frozen q2, `rungTF` (mean titre 22.15), r3 concordance chain, r4 6-mark levels "Describe". Key note: frozen 7 lines. Bank: q1 + q2. | All base 4.4.2.5 / RP2. No n = c × V or mol/dm³ on TF (confirmed at runtime). |
| TH | All of the TF content, plus: `s-conc` (n = c × V, g/dm³ = mol/dm³ × Mr, 2 examples, 2 questions), `rungTH` (HCl/NaOH → 0.0900 mol/dm³), and key-note line 8. | RP2's HT sentence (mol/dm³ **and g/dm³**) is now covered, which closes examination R8. |

**Arithmetic, re-done by hand**

All correct:
- 24.60 / 24.70 / 25.30 → mean 24.65, and 24.87 if the 25.30 outlier is kept
- 17.60 / 17.65 / 17.70 → 17.65 (rough run and 17.95 excluded ✓)
- 18.15 / 18.25 → 18.20 (0.10 cm³ = 0.00010 dm³ ✓)
- 22.10 / 22.15 / 22.20 → 22.15
- 0.100 × 0.0200 ÷ 0.0250 = 0.0800
- H₂SO₄ 0.00200 mol × 2 ÷ 0.02500 = 0.160 mol/dm³ → × 40 = 6.40 g/dm³; 0.0800 if the ratio is missed ✓
- 0.200 × 0.0250 ÷ 0.0200 = 0.250
- KOH (Mr 56 ✓): 0.001875 × 2 ÷ 0.025 = 0.150 → 8.40 g/dm³
- 0.100 × 0.02250 ÷ 0.02500 = 0.0900

**Simulation logic, checked**
- Volumes are integer hundredths.
- The rough run can only end on whole cm³, so it always overshoots (25.00 against an end point of 24.70). The "Larger" verdict is therefore right.
- Run 2 is planted at 25.05.
- `judge()` behaves correctly:
  - excludes the rough run;
  - requires a cluster within 0.10 cm³;
  - rejects a span over 0.10;
  - requires every concordant titre;
  - rounds the mean to 2 dp correctly (24.675 → 24.68).
- The burette scale increases downwards and is read at the bottom of the meniscus.
- The indicator strips are drawn correctly:
  - phenolphthalein: pink → colourless;
  - methyl orange: yellow → red;
  - universal indicator: gradual change, purple → red.
- Rinse logic is correct:
  - water in the burette dilutes the acid → titre too large;
  - the flask is rinsed with distilled water only.

**Examination flags, all resolved**
- "At Foundation level" and "reliability" are not used.
- UI unsuitability is taught.
- Rinsing the flask with water is taught.
- The HT example with g/dm³ is present.

**Frozen items still served that should be withheld:** none. q1 wx1 says "0.50 cm³ away from the other three". That is imprecise (it is 0.45–0.55 from each, or 0.50 from their mean), but not wrong enough to withhold.

### REQUIRED
None.

### ADVISORY
| # | where | note |
|---|---|---|
| A-3 | `s-hook` paragraph | OLD: `For a long time each splash makes a colourless patch that vanishes when the flask is swirled.` → suggested NEW: `Near the end, each splash makes a colourless patch that vanishes when the flask is swirled.` A patch that lingers is the sign the end point is *close*. The page's own simulation flashes only within 0.50 cm³ of the end point, so the hook currently contradicts it. |
| A-4 | gate prompt in `s-bench` | "The rough run goes in a whole 1 cm³ at a time", but the rough run also offers a +5.00 cm³ button. Suggested: `…goes in 1 cm³ or more at a time…`. This is about wording, not science. |

**Verdict: SCIENCE PASS.**

---

## 3. metal-hydroxides — 8462 4.8.3.2 (chemistry only) + RP7, TF + TH

**Route-by-route**

| route | what ships | check |
|---|---|---|
| TF | Shared sections: hook (Cu(OH)₂); explainer; RP7 NaOH method and risks; precipitate bench (6 known + 4 unknown tubes; the Fe(II) "leave to stand" browning); excess-at-once misconception; base word equation; equation forge (CuSO₄ worked; FeCl₃ + 3NaOH and FeSO₄ + 2NaOH to build). Ladder: r1 frozen q1, r2 P/Q/R data table (Al, Fe²⁺, Ca with a flame test), r3 Al vs Mg chain, r4 6-mark Plan. Key note: 5 lines. Bank: q1 + q2. | Full balanced equations are taught as base, which is correct: 4.8.3.2 carries no HT label. That closes examination R3. Combining with the flame test (base, 4.8.3.1) is on TF, which closes R8. |
| TH | All of the TF content, plus: the ionic equation card, `s-ionic` (build Cu²⁺ + 2OH⁻ → Cu(OH)₂(s)), the "Contains Higher" chip, and key-note line 6. | Ionic equations are HT only (8462 4.1.1.1), and are placed correctly. |

**Science checks**
- Colours: Cu²⁺ blue, Fe²⁺ green, Fe³⁺ brown, Al/Ca/Mg white, and only Al(OH)₃ dissolves in excess. All match the verbatim spec.
- Bench verdicts are correct:
  - "No precipitate": all six give one.
  - Unknown Y (Mg) is credited only as "calcium or magnesium", with the flame test named as the decider.
  - A white precipitate cannot be identified before excess has been added.
- Forge keys are correct:
  - Fe(OH)₃, 3NaOH, 3NaCl;
  - Fe(OH)₂, 2NaOH, Na₂SO₄;
  - every distractor `why` is true, including the FeOH₃ bracket error and SO₃ being sulfite.
- Ionic keys are correct: 2 OH⁻ and Cu(OH)₂(s).
- r2 keys are correct: aluminium, iron(II), calcium.
- Not-in-spec material from the source is absent from the page: the aluminate equation (explicitly excluded by the spec), the ammonium test, and the wrong flame-test parenthetical.
- The RP is labelled 7, which is correct; the source said 4.

**Frozen items still served that should be withheld:** none.
- q1 is clean.
- q2's keyed text "amphoteric … aluminate" goes beyond the spec but is true. It does not ask for the excluded equation (A-6).

### REQUIRED
None.

### ADVISORY
| # | where | note |
|---|---|---|
| A-5 | logic `keyLines[0]` | OLD `Fe³⁺ = brown/rust` → NEW `Fe³⁺ = brown`. The page's own `FACT.fe3` tells pupils "in the exam, write brown", and the spec word is "brown". The key card should model the answer to write. |
| A-6 | bank q2 (frozen) | The keyed option names "amphoteric" and "aluminate". Both are beyond 8462, which excludes sodium aluminate equations. They are true and harmless, so keep the item. Noted for Mide's list only. |

**Verdict: SCIENCE PASS.**

---

## 4. carbonates-halides-sulfates — 8462 4.8.3.3–4.8.3.5 (chemistry only) + RP7, TF + TH

**Route-by-route**

| route | what ships | check |
|---|---|---|
| TF | Shared sections: hook (HCl-acidified halide test gives "chloride" five times); explainer; fizz misconception (Mg + acid → H₂); RP7 anion method and risks; test rack (Na₂CO₃, KBr, CuSO₄, CaCl₂, LiI; cation call from a given flame or NaOH result, then anion tests, then name the salt); acid sort (fair test vs false positive); base full equation Na₂CO₃ + 2HCl. Ladder: r1 frozen q2, r2 P/Q/R anion table, r3 "why HCl before BaCl₂" chain, r4 6-mark Plan. Key note: 6 lines. Bank: q2. | All base 4.8.3.1–4.8.3.5. Combining cation and anion tests is on TF, which closes examination R8. "Why acidify" is on TF, which closes R7. |
| TH | All of the TF content, plus: `s-ionic` (spectator strike-out for AgBr, BaSO₄ and CO₃²⁻ + 2H⁺), the "Contains Higher" chip, and key-note line 7. | Ionic equations are HT only (4.1.1.1), and are placed correctly. |

**Science checks**
- Reagents and colours: HNO₃ + AgNO₃ gives white / cream / yellow; HCl + BaCl₂ gives white; acid plus limewater turns milky. All match the verbatim spec.
- The reason for acidifying is given correctly everywhere as **removing carbonate**. The source's wrong claim that nitric acid "removes sulfate" (examination C7/C10) appears nowhere on the page.
- Rack outcomes are all correct:
  - the carbonate fizzes and gives no precipitate under either acidified reagent;
  - CuSO₄ gives no silver-halide precipitate and a white BaSO₄ in blue solution;
  - CaCl₂ gives no BaSO₄;
  - flame colours match 4.8.3.1 (Na yellow, K lilac, Li crimson, Ca orange-red, Cu green).
- All 20 naming-feedback lines and 20 cation-call lines are true.
- The acid sort is correct: HCl + AgNO₃, H₂SO₄ + BaCl₂ and either reagent without acid can each give a false positive.
- Spectator equations are balanced, and the spectator ions are identified correctly.
- r2 keys are correct: carbonate, bromide, sulfate.
- The r4 reject "a flame test tells them apart" is right, because all three are sodium salts.
- The RP is labelled 7, which is correct; the source said 4.

**Frozen items still served that should be withheld:** none beyond B2-W9.
- q1 (wrong "removes sulfate" key) is withheld, and confirmed absent from the built source on both routes.
- q2 is clean in its science (A-7).

### REQUIRED
None.

### ADVISORY
| # | where | note |
|---|---|---|
| A-7 | bank q2 / ladder r1 (frozen), TF | On TF the keyed option text includes the ionic equation `Ba²⁺ + SO₄²⁻ → BaSO₄`, and ionic equations are HT only (4.1.1.1). The item tests a base identification and the equation is only a label, so it is not route-wrong enough to withhold. It is also the lesson's only remaining frozen item. Noted for Mide's list. |
| A-8 | logic `keyLines[3]` | OLD `Always acidify first to remove interfering ions.` → suggested NEW `Always acidify first to remove carbonate ions.` This gives the specific, creditworthy reason, which the rest of the page already teaches. |

**Verdict: SCIENCE PASS.**

---

## Items only Mide can rule on
None. Nothing in these four lessons sets one AQA source against another. A-6 and A-7 are notes for the frozen-item list, not conflicts.

## Verdicts
| lesson | verdict |
|---|---|
| percentage-yield | **SCIENCE PASS AFTER REQUIRED CHANGES** (S-1) |
| titrations | **SCIENCE PASS** |
| metal-hydroxides | **SCIENCE PASS** |
| carbonates-halides-sulfates | **SCIENCE PASS** |

---

## Round 2 — re-review of commit 36fd4c877 (1 Oct 2026)

**How I re-checked**
- Diffed each `.dc.html` from fff50ef58 to 36fd4c877.
- Read every new or changed string and every changed piece of logic.
- Ran all 8 built pages again in headless Chrome: light scheme, port 8714, TF compared with TH.
  - No console errors other than the local CORS health ping.
  - No "undefined". The only "NaN" hits are the substring of NaNO₃.
- Route layering still holds on all four lessons. Higher content appears on TH only, as before. The new TH-only write-it-out sets are confirmed absent from TF.

### percentage-yield
- **S-1 confirmed.** The r4 points now read "First reason, any one of: …" and "Second reason: a different one of those three." Any two of the three spec reasons now score both marks. The new text is present in the built TH page, and the logic is shared by TF.
- **New authored r1 ("Give one reason…")** is correct:
  - The key is "Some product is left behind when it is separated from the mixture", which is a spec reason (4.3.3.1).
  - The distractor replies are all true: atoms are conserved; a catalyst changes the rate, not the maximum mass; the theoretical yield is calculated exactly from the equation.
  - The `why` names all three spec reasons.
- **New TH rearrangement questions** are correct:
  - 72 % × 45 g ÷ 100 = **32.4 g** ✓
  - 2.40 kg → 2400 g; 85 × 2400 ÷ 100 = **2040 g** ✓
  - The close note "Skip the conversion and you get 2.04" is right.
  - Rearranging the % yield equation is legitimate maths-skill use of 4.3.3.1.
- **A-1 applied:** "never the maximum mass of product".
- **A-2 applied:** "83.3% (83%)".
- **Key note:** "Chemistry-only spec point." was dropped. The remaining lines are unchanged and correct.
- **Bench close box** now reads "Theoretical yield 8.0 g · actual yield 6.2 g. Nothing was destroyed." That is correct.

### titrations
- **New sort "Titre too large, too small, or no effect?"**: every verdict and every reason is correct.

  | card | verdict | check |
  |---|---|---|
  | burette rinsed with water | too large | the acid is diluted ✓ |
  | pipette rinsed with water | too small | fewer moles of alkali in 25.00 cm³ ✓ |
  | flask rinsed with distilled water | no effect | the moles of alkali are unchanged ✓ |
  | overshoot | too large | ✓ |
  | final reading at the top of the meniscus | too small | the scale increases downwards, so the top sits at a smaller number ✓ |
  | air bubble in the jet fills during the run | too large | volume is read off the burette but never reaches the flask ✓ |
  | flask walls washed with distilled water | no effect | ✓ |

  The done-note (amount of alkali / strength of acid / reading) is a sound diagnostic.
- **Overshoot handling** is correct.
  - A row is flagged `over` when an accurate run's added volume is more than the end point + 0.05 cm³.
  - Pure drop-by-drop additions always land exactly on the end point, because every value is a multiple of 0.05 cm³. Only a +0.50 cm³ splash or a run-in that is too long can overshoot.
  - `judge()` leaves overshot rows out of the concordance search and refuses any choice that contains one. Its reason ("these titres are too large") is right.
  - "Repeat the rough run" replaces the rough row.
  - With `MAXRUN` = 9 there are 10 `INIT`/`EP` entries, so the indices are safe.
  - The authors' driven mean (24.75 + 24.70) ÷ 2 = 24.725 → 24.73 cm³ is correct.
- **New TH write-it-out numbers** are correct:
  - Q1: 22.95, 23.05 and 23.00 span 0.10, so they are concordant. The rough 23.40 and the 22.60 are excluded. 69.00 ÷ 3 = **23.00 cm³** ✓
  - Q2: 0.02210 / 0.02275 / 0.02200 / 0.02205 dm³ → 22.10 / 22.75 / 22.00 / 22.05 cm³. 22.00–22.10 are concordant; 22.75 is out. 66.15 ÷ 3 = **22.05 cm³** ✓
- **New authored r1 ("drop by drop")** is correct:
  - The key "So that one drop past the end point is not added" is right.
  - The distractor replies (swirling, near-instant indicator, tiny temperature change) are all true.
- **A-3 and A-4 applied.** The key-note line "RP Chemistry 2 (chemistry-only)." is filtered out. That is harmless, because the key-note spec label still names RP2.

### metal-hydroxides
- **A-5 applied:** key-note line 1 now reads "Fe³⁺ = brown". Correct, and it matches 4.8.3.2 word for word.
- The other changes do not touch the science: the route chip, the RP pill wording and "Tube W · identified".

### carbonates-halides-sulfates
- **A-8 applied:** key-note line 4 now reads "Always acidify first to remove carbonate ions." That is correct and is the reason AQA credits.
- **r4 reworded to "Plan tests that would identify each solid. Give the result each one would show."** The levels and marking points are unchanged and still match.
- The other changes do not touch the science: the results log now shows earlier results only, plus the route chip and the pill.

### Round 2 REQUIRED
None.

### Round 2 ADVISORY
| # | where | note |
|---|---|---|
| A-9 | titrations `eItems[4].why` | "the top reads lower" could be read as "lower down the tube", which is the opposite of what is meant. Clearer wording: `The scale increases downwards, so the top of the meniscus sits at a smaller number: the final reading, and the titre, come out too small.` The verdict itself is right. |

A-6 and A-7 (frozen quiz-bank notes for Mide's list) still stand, unchanged.

### Final verdicts (Round 2)
| lesson | verdict |
|---|---|
| percentage-yield | **SCIENCE PASS** |
| titrations | **SCIENCE PASS** |
| metal-hydroxides | **SCIENCE PASS** |
| carbonates-halides-sulfates | **SCIENCE PASS** |
