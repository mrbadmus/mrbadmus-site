# Science review: batch 3, group chem-bio

Reviewer: a fresh AQA GCSE examiner (Opus), 1 Oct 2026. I wrote none of these lessons.

Lessons reviewed:
- `microscopy` (8461/8464 4.1.1.5)
- `mixtures` (8462 4.1.1.2 / 8464 5.1.1.2)
- `conservation-of-mass` (8462 4.3.1.1 / 8464 5.3.1.1)
- `atom-economy` (8462 4.3.3.2, Triple only)
- `early-atmosphere` (8462 4.9.1.2–4 / 8464 5.9.1.2–4)
- `greenhouse-gases` (8462 4.9.2.1–4 / 8464 5.9.2.1–4)

The source examination files in `docs/ks4/packs/batch-3/examination/` were my starting evidence. I re-checked every point in them rather than taking them on trust.

## Method

- **Sources.** I read every lesson source in full: the template and all of the Component logic. That covers stage tables, `reply`/`why`/`r` texts, figure geometry, CFIFA steps, rungs, levels, reject lines, key-note assembly and the bank call.
- **Frozen data.** I extracted the frozen data actually served from `shared/ks4-source-batch-3.js`: quiz per route, key_note, FIFAs and equations. I checked it against the `withhold` list in `ks4_lessons/batch_3.py`. The withheld items are absent from the served quiz on every route: microscopy q1 and q2, conservation q2, atom-economy q2.
- **Browser drive.** I drove all 22 built pages in headless Chrome on :8723 with `prefers-color-scheme: light`: 5 lessons × CF/CH/TF/TH, plus atom-economy × TF/TH. I captured the client-rendered text (ladder, CFIFA, key note, practice set) and diffed every route against Triple Higher.
  - The only console errors are the expected localhost CORS block on `/api/health`.
  - On atom-economy, I also committed the brine prediction on TF and TH to check that the by-products line is Higher-only.
- **Arithmetic.** I re-did every calculation by hand: Mr totals, atom economies, missing masses, magnifications, unit conversions and standard form. I also checked the stoichiometric realism of every invented mass set (for example 2NaHCO₃ 168 → 106 + 18 + 44 against 16.8 → 10.6 + 1.8 + 4.4).

**Route behaviour, verified in the built pages:**
- **conservation-of-mass.** The mole sentence (`data-route="higher"`, 5.3.2.2 HT) is absent on CF/TF. It is badged HIGHER on CH/TH.
- **atom-economy.** On TF, the "Choose a route" block, the brine "all three products are sold" line and the Evaluate command word are all absent. The 6-mark Evaluate rung becomes a Calculate + Give rung. All of these are present and badged on TH (8462 4.3.3.2 bullet 2, HT only).
- **The other four lessons.** No content is route-tagged, which is correct because all their content is base. Routes differ only in the spec eyebrow and key-note label (8461/8462 vs 8464) and in the tiered calculation numbers.
- **The pack's `higher` fields.** These held mis-tiered material: Miller–Urey, carbon-footprint calculation, atom economy on Combined, and SEM/TEM. No lesson renders them.

**The four points the commander asked me to check with care:**
- **microscopy, resolution.** The explainer says: "Resolution is the ability to distinguish two points that are close together as separate points." The key note's frozen "Resolution = sharpness." is mapped to "Resolution = the ability to distinguish two points that are close together." "Sharpness" occurs nowhere in the rendered text of any of the four routes. The Explain rung, the Resolve-it views and the command-word card all use the same creditable definition. **Confirmed.**
- **atom-economy, AQA's form.** The reactants form (desired-product Mr from the equation ÷ sum of Mr of all reactants × 100) is used in the following places:
  - the equation block, with Σ reactants = Σ products shown as an equivalence;
  - key-note line 1 (the frozen products line is dropped);
  - the iron worked example;
  - all four CFIFA questions;
  - both calculation rungs, the strip workings, the brine workings and the Think-again.

  Two frozen exceptions remain. The FIFA's own Formula step still prints the products form, with an authored note under it reconciling it to AQA's (see A-7). The bank's q1 keyed text still uses the products form (see S-3). The reaction-pathway layer is Higher-only (verified above). **Confirmed, subject to S-3.**
- **greenhouse-gases, the three gases and the footprint definition.** Only water vapour, carbon dioxide and methane are named, in the hook, the bench legend and key-note line 1. N₂O appears nowhere on any route. The carbon-footprint definition is the spec's verbatim "total amount of carbon dioxide and other greenhouse gases emitted over the full life cycle of a product, service or event", in the explainer and the key note. Rung 2 and the Limits activity test the full-life-cycle point. **Confirmed.**
- **early-atmosphere, wording and fossil fuels.** The lesson's own text says "algae", then "plants", throughout: stage 3, the volcano confrontation, the key note and the rung-4 points. Stage 3 explains once that books call the first organisms cyanobacteria and that AQA calls them algae. Fossil-fuel formation is taught in four places:
  - stage 5: buried before full decay, mud keeps oxygen out; shells → limestone, plants → coal, plankton → crude oil and natural gas;
  - the crude-oil chain, with a coal herring;
  - the key note: "locked in sedimentary rocks (limestone) and fossil fuels (coal, crude oil, natural gas)";
  - the rung-4 points.

  The spec's "O₂ rose to a level that enabled animals to evolve" is in stage 4 and the key note. **Confirmed.**

---

## 1. microscopy (8461/8464 4.1.1.5; RP1 on both)

**Route-by-route.** CF, CH, TF and TH are identical apart from the spec eyebrow and the key-note label. Foundation also gets its own CFIFA question 1 and rung 2: onion cell ×500, and guard cell ×800. Higher gets nucleus 11 µm, mitochondrion 3 × 10⁴ and ribosome 20 nm. Standard form and nm are base (4.1.1.5). They are taught to every route in the explainer and in the "nm · standard form" worked example. Practice set on all routes: q3, q4 and q5 (ribosomes, magnification vs resolution, 50 µm × 400). The withheld q1 and q2 are absent.

**Verified correct.**
- **Explainer.** LM ×2000 and 200 nm; EM (1930s) ×2 000 000 and 0.1 nm; vacuum, so dead specimens. Magnification and resolution definitions.
- **Hook.** Hooke in 1665; ribosomes about 20 nm, first seen in the 1950s with the EM; "nearly 300 years".
- **Resolve-it views.** 2 µm = 2000 nm, ten times the 200 nm limit. Ribosomes 40 nm apart merge. Enlarging the image adds no detail. EM separation at 0.1 nm.
- **Bench.** Eyepiece ×10 with objectives ×4/×10/×40 (examination C28's ×200 error is gone). Total ×100, and the "add / objective alone" distractors are diagnosed correctly. A 0.45 mm field at ×400. Counts 3/4/3, mean 3.3, 0.45 ÷ 3.3 = 0.14 mm = 140 µm. Every distractor's arithmetic checks: 0.45 ÷ 3 = 150 µm; 0.45 ÷ 4 = 110 µm (2 s.f.); ×10 000 slip = 1400 µm, longer than the 450 µm view.
- **RP1.** Method order (lowest power first, watch from the side, coarse then fine, fine only at high power), drawing conventions, "no variables" and risks all match the examination's RP1 content. Toluidine blue and the "staining kills cells" claim are gone.
- **Drawing check.** Chloroplasts are absent from onion epidermis.
- **Think-again.** 12 000 ÷ 40 = ×300; ×30 from the 1 mm = 100 µm slip.
- **CFIFA.**
  - 25 000 ÷ 5 = 5000.
  - Frozen FIFA 2: 0.15 µm = 1.5 × 10⁻¹ µm.
  - Membrane 7 nm vs 0.35 mm: 350 000 ÷ 7 = 5 × 10⁴.
  - Q1 (H): 33 ÷ 3000 = 0.011 mm = 11 µm; 33 × 3000 mm = 99 m.
  - Q2 (H): 45 000 ÷ 1.5 = 3 × 10⁴.
  - Q1 (F): 70 ÷ 0.14 = 500.
  - Q2 (F): 45 000 ÷ 60 = 750; 45 ÷ 60 = 0.75.
- **Rungs.**
  - r2 Higher: 600 000 nm ÷ 30 000 = 20 nm.
  - r2 Foundation: 32 000 ÷ 40 = 800. Both answers are below 1000, so the calc-rung parse limit is not tripped.
  - r3 chain and herrings.
  - r4: the RP1 6-marker levels and points.
- **Key note.** Lines 05–07 are added, with RP1 numbered correctly for both specs.

### REQUIRED
None.

### ADVISORY

| # | where | note |
|---|---|---|
| A-1 | rung 1 (frozen q4) | The keyed text is "resolution = how clearly fine detail can be distinguished". This is creditable (examination C35), but it sits a little awkwardly beside the command-word card's "not 'clearer'". It is not wrong. Leave it. |
| A-2 | CFIFA tab "Actual size" (frozen FIFA 2) | A mitochondrion of 0.15 µm is unrealistically small (real ones are about 0.5–1 µm wide and 1–several µm long; examination C20). The arithmetic is right and the item is frozen. If the commander wants realistic scale throughout, drop this tab: the authored examples and Higher Q1/Q2 already cover "find actual size". |
| A-3 | `s-think` option "×3.3" reply | "That divides the wrong way: real size ÷ image size." 40 ÷ 12 is inverted **and** still unconverted. Optional fix: "That divides the wrong way, real ÷ image, and still mixes µm with mm." |

**Frozen items still served that should be withheld:** none.

**Verdict: SCIENCE PASS.**

---

## 2. mixtures (8462 4.1.1.2 / 8464 5.1.1.2)

**Route-by-route.** The routes are identical apart from the eyebrow, the key-note label and rung 2. Higher rung 2: sugar-solution water → simple distillation; methanol 65 °C / ethanol 78 °C → fractional. Foundation rung 2: chalk → filtration; copper chloride → crystallisation. Everything is base, so this split is acceptable. The wrong `rp` (RP1 chromatography) is not shown anywhere. The block is labelled "Practical skills · setting up apparatus", not "Required practical". The Rf FIFA and the Rf equation are not shown. The key note's Rf clause is cut ("Chromatography: dissolved substances."). Practice set on all routes: q1, q2 (Rf) and q3.

**Verified correct.**
- **Definition and processes.** The definition of a mixture is the spec's wording, and the GAP is closed in the explainer, the hook reveal, key-note line 1 and rung 1. The lesson names the five spec processes.
- **Lab fractional distillation.** Taught correctly: a column of glass beads, the lowest boiling point reaches the top first, liquids collected one after another as the temperature rises (examination C9 fixed).
- **Crystallisation.** "Heat to evaporate some of the water, then leave to cool" (examination C6 fixed).
- **Figures.**
  - Simple distillation: bulb at the side arm, water in at the bottom of the condenser.
  - The kit check: bulb in the liquid is the fault.
  - Chromatography: pencil line above the solvent.
  - Fractional: thermometer at 78 °C.
- **Ethanol/water.** Reasoning uses "close boiling points".
- **Copper sulfate chain.** Dissolve → filter → evaporate some water and cool → filter and dry. The herrings are diagnosed correctly.
- **Rungs.** r3 chain with the "heaviest molecules" herring. r4 rock-salt plan levels and points (thermometer reads 100 °C).
- **Legal line.** The note on the ethanol–water azeotrope is accurate.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-1 | mixtures · CF CH TF TH | `ROUNDS[0].no[2]`: the reply when a pupil picks **Simple distillation** for "Sand stirred into water" | "Boiling off all the water would leave the sand, but slowly, and the water is lost. A filter catches insoluble sand in seconds." → "Distilling off all the water would leave the sand behind, but it takes a long time and a lot of energy. A filter catches insoluble sand in seconds." | Simple distillation condenses and **collects** the water, so "the water is lost" is false for the method the pupil chose. It is also the exact confusion the lesson fights elsewhere: round 3 ("its vapour is cooled in the condenser… pure water"), rung 4's reject line ("Evaporated water escapes… collecting it needs a condenser"), and the examination §5 misconception "evaporate to get pure water". The current reply describes evaporation, not distillation. | 8462 4.1.1.2 / 8464 5.1.1.2 (simple distillation) |

### ADVISORY

| # | where | note |
|---|---|---|
| A-4 | key note line 05 (frozen key_note, verbatim) | "Fractional distillation: liquids with different boiling points." This is true, but the lesson's own teaching point is boiling points **close together** (round 4, rung 3), and simple distillation also separates liquids with different boiling points. Optional: map this line like the chromatography line, to "Fractional distillation: liquids whose boiling points are close together." |
| A-5 | practice set q2 (Rf) | Served on all routes although the lesson defers Rf to `chromatography` and cuts it from the key note. The science is correct, and the examination allowed it to stay in the bank. Withholding it, or moving it to `chromatography`'s bank, would avoid testing an untaught calculation. Commander's call. |
| A-6 | practice set q3 wx1 (frozen) | "simple distillation collects one fraction at a time but cannot separate all components simultaneously" is imprecise (examination C27). Not false enough to withhold, and the lesson's own text gives the "close boiling points" reason. Keep. |

**Frozen items still served that should be withheld:** none.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES (S-1).**

---

## 3. conservation-of-mass (8462 4.3.1.1 / 8464 5.3.1.1)

**Route-by-route.**
- **CF/TF.** No mole sentence and no "Amounts of substances in equations" connect link. Foundation CFIFA questions: ZnCO₃ and 0.50 kg CaCO₃. Foundation rung 2: CuCO₃, 2.2 g, 2 marks.
- **CH/TH.** The mole sentence is shown and badged HIGHER. This is correct on both pathways: 5.3.2.2 / 4.3.2.2 are HT in both specs. Higher CFIFA questions: NaHCO₃ and the blast furnace. Higher rung 2: methane, 3 marks.
- **All routes.** The pack's `higher` field (yield and atom economy, chemistry-only) is not rendered on any route (examination R7/R8 fixed). Practice set: q1 and q3. q2 is withheld.

**Verified correct.**
- **Flask animation, methane.** CH₄ + 2O₂ → CO₂ + 2H₂O. Atom tracks: one CO₂ (O–C–O), two waters, 9 atoms in and 9 out. Ledger 1 C · 4 H · 4 O on each side.
- **Flask animation, calcium.** Ca + 2H₂O → Ca(OH)₂ + H₂: 1 Ca · 2 O · 4 H. The "(OH)₂ doubles everything inside" reply is right.
- **Word → symbol.** CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂. The balance reply (1 Ca, 1 C, 3 O, 2 H, 2 Cl each side) is right, and so are the state symbols (s)(aq)(aq)(l)(g), including the "(aq) for water itself" reason.
- **Missing masses.** Every one checks:
  - 10.0 − 5.6 = 4.4 g
  - 2000 − 1200 = 800 g
  - 16.8 − 10.6 − 1.8 = 4.4 g (6.2 g if the water is left out)
  - 2440 − 1120 = 1320 g (480 g if the CO is left out)
  - 12.5 − 8.1 = 4.4 g
  - 500 − 280 = 220 g
  - 6.2 − 4.0 = 2.2 g

  Every mass set is consistent with the Mr ratios of its equation.
- **Rungs.** r1 keyed definition and distractor replies. r3 chain. r4 Mg + 2HCl with state symbols and its reject lines.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-2 | conservation-of-mass · CH TH | `rungs.r2` (Higher calc rung) | **prompt:** "…0.40 kg of methane forms 1.10 kg of carbon dioxide and 0.90 kg of water…" → "…0.16 kg of methane forms 0.44 kg of carbon dioxide and 0.36 kg of water…" · **answer:** 1600 → 640 · **tol:** 5 → 2 · **right:** "Both products count on the right: 2000 g in all, and 400 g of it came from the methane." → "Both products count on the right: 800 g in all, and 160 g of it came from the methane." · **wrong:** "Convert first: 400 g, 1100 g and 900 g. Then 400 + mass of O₂ = 1100 + 900." → "Convert first: 160 g, 440 g and 360 g. Then 160 + mass of O₂ = 440 + 360." · **model:** "C · 0.40 kg = 400 g · 1.10 kg = 1100 g · 0.90 kg = 900 g" → "C · 0.16 kg = 160 g · 0.44 kg = 440 g · 0.36 kg = 360 g"; "I · 400 + mass of O₂ = 1100 + 900" → "I · 160 + mass of O₂ = 440 + 360"; "F · mass of O₂ = 2000 − 400" → "F · mass of O₂ = 800 − 160"; "A · 1600 g" → "A · 640 g" | The keyed answer, 1600, trips the known calc-rung limit: "1,600" or "1 600" parses as 1. A Higher pupil who writes a correct answer in normal exam form is marked wrong. The new numbers keep the kg → g conversion and both products, and are stoichiometric: CH₄ 16 : O₂ 64 : CO₂ 44 : H₂O 36 = 160 : 640 : 440 : 360 g. 160 + 640 = 800 = 440 + 360 ✓. | 8462 4.3.1.1 / 8464 5.3.1.1; review_common_b3 (engine limits) |

### ADVISORY
None.

**Frozen items still served that should be withheld:** none.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES (S-2).**

---

## 4. atom-economy (8462 4.3.3.2; TF and TH only; not in 8464)

**Route-by-route.** The lesson is published on TF and TH only, which is correct, because "atom economy" is absent from 8464.
- **TH only (verified as absent on TF):**
  - the "Choose a route" table and sort (atom economy with yield, rate, equilibrium position and by-product usefulness: the full spec list; "Atom economy alone never decides it");
  - the brine by-products line;
  - the Evaluate command word;
  - the 6-mark Evaluate rung 4;
  - the ammonia and methane–steam CFIFA questions;
  - the TiCl₄ rung 2.
- **TF:** the water-electrolysis and Mg + HCl CFIFA questions, the CuCO₃ rung 2, and a Calculate + Give rung 4.
- **Fixes from the examination, all done:**
  - the 45.9 % "high" / 56 % "low" labels are gone;
  - the frozen common_mistake (WRONG) is not displayed;
  - the frozen `equations[0]` (products form) is not displayed;
  - "pharmaceutical", "green chemistry" and substitution/elimination are absent.
- **Practice set:** q1 only, since q2 is withheld. See S-3.

**Verified correct.**
- **Fermentation.** 92/180 = 51.1 %; CO₂ carries 88/180 ≈ 49 %, "almost half".
- **Strip.**
  - Ethanol: 46/46 = 100 %.
  - Lime: 56/100 = 56 %, "more than half".
  - Iron: 112/244 = 45.9 %, "less than half"; 3CO₂ = 132 > 2Fe = 112.
- **Think-again.** 2NaCl = 117; 23/117 = 19.7 %; 46/117 = 39.3 %; inverted, 117/23 = 509 %.
- **Brine.** 153 = 117 + 36 = 80 + 71 + 2. NaOH 52.3 %, Cl₂ 46.4 %, H₂ 1.3 %; the lowest is H₂.
- **CFIFA.**
  - NH₃: 34/181 = 18.8 %; 17/127.5 = 13.3 %.
  - H₂ from methane: 6/34 = 17.6 %; 2/34 = 5.9 %.
  - H₂ from water: 4/36 = 11.1 %; 2/36 = 5.6 %.
  - MgCl₂: 95/97 = 97.9 %; 95/60.5 = 157 %.
- **Rungs.**
  - Ti: 48/238 = 20.2 %; MgCl₂ is 190/238 ≈ 80 %, "four-fifths".
  - CuSO₄: 159.5/221.5 = 72.0 %; the remainder 62/221.5 = 28 %.
  - 2Fe₂O₃ + 3C: 224/356 = 62.9 % (balanced ✓).
- **Route table.** Fermentation about 30 °C at normal pressure, batch, dilute product, CO₂. Hydration 300 °C at 60–70 atm, continuous. Raw materials renewable vs finite. Every sort placement is defensible, and the done-note correctly says "rows are not votes".
- **Rest of the page.** r1 definition and the yield distractor. r3 chain (addition → one product → no waste). Key-note line 1 in AQA's form.

### REQUIRED

| # | lesson · routes | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-3 | atom-economy · TF TH | `ks4_lessons/batch_3.py` atom-economy `withhold` | add `W("A reaction produces 80 g of desired product and 20 g of waste product", "B3-W<n>")` (frozen quiz q1; withhold on all routes, i.e. TF and TH) | The **credited** option reads "80% — desired product Mr = 80, total products = 80 + 20 = 100". 80 g is a mass, not an Mr, so the keyed text states something false. It also computes atom economy from product masses with a products denominator. That is the opposite of the AQA reactants form the lesson teaches everywhere else, and of the lesson's own rung-1 feedback ("Atom economy comes from the equation, not from what you collect"). Distractor D is labelled "(calculated waste not yield)", which mixes the two terms the lesson separates. Distractor C ("calculated incorrectly") names no misconception. The source examination (C20, C22, C24) kept q1 in the bank. I depart from that because it is now the only bank item, and its keyed explanation teaches a false label. Precedent: B2-W5/W8 (a frozen option label that is false). **Consequence:** atom-economy's practice set would have no items. The commander should confirm that `Ks4QuizBank` renders cleanly with an empty list, or hides itself. | 8462 4.3.3.2 ("calculated using the balanced equation… sum of relative formula masses of all reactants from equation") |

### ADVISORY

| # | where | note |
|---|---|---|
| A-7 | CFIFA tab "Ethanol · addition" (frozen FIFA) | The frozen Formula step still prints "Atom economy = (Mr desired product ÷ sum Mr all products) × 100". The authored note directly under it reconciles this: "AQA divides by the reactants: C₂H₄ + H₂O = 28 + 18 = 46. Mass is conserved, so the products' total is the same 46." That is acceptable under the frozen policy. If the commander prefers AQA's form to be the only form on screen, replace this tab with an authored ethanol example (the 46 ÷ (28 + 18) working is already in the strip). |

**Frozen items still served that should be withheld:** q1 (see S-3).

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES (S-3).**

---

## 5. early-atmosphere (8462 4.9.1.2–4 / 8464 5.9.1.2–4)

**Route-by-route.** The routes are identical apart from the eyebrow and the key-note label, which is correct because all of this content is base. Evaluating evidence for the theory is taught as base on every route: the explainer plus the Mars evidence sort (examination R8 fixed). Miller–Urey, banded iron, the ozone/UV story and isotopes are all absent. The frozen key_note (cyanobacteria, no fossil fuels) is not used: the key note is authored in full. Practice set on all routes: q1 and q2.

**Verified correct.**
- **Hook figure.** Venus CO₂ 96 %, Mars 95 %, Earth N₂ 78 % / O₂ 21 % / CO₂ about 0.04 %.
- **Clock stages.** The spec sequence:
  1. volcanoes: CO₂, H₂O and N₂, maybe CH₄ and NH₃, little or no O₂;
  2. cooling, condensation and oceans, with CO₂ dissolving and carbonates precipitating as sediment (examination R3 fixed);
  3. algae at about 2.7 bn years, with photosynthesis giving O₂;
  4. plants evolve, O₂ rises gradually, and this enables animals to evolve (R5 gap closed);
  5. burial before full decay forms limestone, coal, crude oil and natural gas (R6 gap closed);
  6. N₂ released by volcanoes and unreactive, rising to about 80 % (examination C14 fixed).

  "100 °C" is gone (C11). Every distractor reply is true.
- **Equation and spot-the-flaw.** The photosynthesis equation is balanced. The spot-the-flaw correctly identifies the student's line as respiration.
- **Crude-oil chain.** Plankton → mud keeps oxygen out → heat and pressure → millions of years. The coal and dinosaur herrings are right.
- **Evidence sort.** All six placements are defensible, and the done-note gives a judgement.
- **Rungs.** r2 sketch graph: O₂ leaves zero at about 2.7 bn years, and the fall in CO₂ at 4–3 bn years is caused by the oceans, not plants. r3 nitrogen chain. r4 levels and points.

### REQUIRED
None.

### ADVISORY

| # | where | note |
|---|---|---|
| A-8 | rung 1 (frozen q2) wx1 | "Acid rain does form but that's CO₂ dissolved in falling water". In AQA's usage, acid rain is caused by SO₂ and NOₓ (5.9.3.2; examination C27). It is minor, and the examination said keep. It is served as rung-1 feedback on all routes. Keep. |
| A-9 | `s-hook` h2 | "Venus and Mars still have the kind of air Earth started with." The spec says the early atmosphere "**may** have been like the atmospheres of Mars and Venus today". The next sentence ("Scientists think…") hedges it, but the heading is assertive in a lesson that later asks pupils to evaluate exactly this idea. Optional: "Venus and Mars may still have the kind of air Earth started with." |

**Frozen items still served that should be withheld:** none. q1's key says "cyanobacteria", but the credited point is photosynthesis, and stage 3 tells pupils that AQA calls these organisms algae.

**Verdict: SCIENCE PASS.**

---

## 6. greenhouse-gases (8462 4.9.2.1–4 / 8464 5.9.2.1–4)

**Route-by-route.** The routes are identical apart from the eyebrow and the key-note label, which is correct because all of this content is base. Peer review and evidence quality (5.9.2.2) and why actions are limited (5.9.2.4) are taught on all four routes: explainers, the two-report activity, the bus Limits activity and rung 4 (examination R5/R8 fixed). The footprint calculation is not taught. Rung 2 only reads and adds a data table, which is base. N₂O, "anthropogenic" and "enhanced greenhouse effect" are absent. Ocean acidification appears only as the exam-trap answer, correctly explained as a CO₂ effect rather than a temperature effect (C14). Practice set on all routes: q1 and q2.

**Verified correct.**
- **Hook.** −18 °C vs 15 °C.
- **Radiation mechanism.** The short-wavelength → surface → long-wavelength (infrared) → absorb → re-emit in all directions chain appears in the explainer, the bench, the "reflect" confrontation, rung 3 and the key note.
- **Bench geometry.** In set-up 2, one ray escapes, one is re-emitted downward and one upward. In set-up 3, two of three are re-emitted downward. The thermometer rises at each set-up. Every bench distractor reply is right, including the ozone separation.
- **Sources sort.** Burning natural gas → CO₂; leaks → CH₄; rice paddies → CH₄. The done-note gives the spec's two activities per gas.
- **Effects.** The six effects match the spec's examined list. Sea level rise is attributed to land ice and thermal expansion.
- **Reports.** Sample/time span, funding bias, peer review, and correlation vs a tested mechanism.
- **Footprint.** Reduction actions include carbon taxes and offsetting. The limits list covers the six credited reasons.
- **Bus Limits activity.** EVs only help with low-carbon electricity; a footprint covers the full life cycle.
- **Rung 2.** Growing the cotton, 2.1 kg, is the largest stage. The total is 2.1 + 1.3 + 0.2 + 1.9 + 0.1 = 5.6 kg. "1.3 kg counts one stage" is the right key.
- **Rung 4.** Weather vs climate, the trend with variation, mechanism, and source/bias. The sketch graph matches its alt text.

### REQUIRED
None.

### ADVISORY

| # | where | note |
|---|---|---|
| A-10 | explainer 3 ("…and natural gas is itself methane") and the sort `why` lines ("Natural gas is methane…", "Unburned natural gas is methane…") | Natural gas is **mainly** methane. Optional: "natural gas is mainly methane" in all three places. Not mark-bearing. |
| A-11 | explainer 1 ("most of its radiation is short wavelength: visible light, with some ultraviolet") | This leaves out the Sun's near-infrared. It is the standard GCSE simplification, and mark schemes credit "short wavelength" without listing bands. No change needed. Noted only so it is not "fixed" into something less clear. |

**Frozen items still served that should be withheld:** none.

**Verdict: SCIENCE PASS.**

---

## Summary

| lesson | REQUIRED | verdict |
|---|---|---|
| microscopy | none | SCIENCE PASS |
| mixtures | S-1 | SCIENCE PASS AFTER REQUIRED CHANGES |
| conservation-of-mass | S-2 | SCIENCE PASS AFTER REQUIRED CHANGES |
| atom-economy | S-3 (withhold frozen q1) | SCIENCE PASS AFTER REQUIRED CHANGES |
| early-atmosphere | none | SCIENCE PASS |
| greenhouse-gases | none | SCIENCE PASS |

**Frozen items still served that should be withheld:** atom-economy q1 (S-3) only.

**Items only Mide can rule on:** none. Where the spec texts overlap (8461/8464 4.1.1.5; 8462/8464 for the chemistry), they are word-for-word identical. "Algae" vs "cyanobacteria" and AQA's reactants form for atom economy are both settled by the spec's own text.

---

## Round 2 (commit 2ddea6225)

I re-checked the source diff from d80d3d4be to 2ddea6225 for all six lessons, and the batch_3.py `withhold` list. I spot-checked the built pages (CF, CH, TF and TH as relevant) and `shared/ks4-source-batch-3.js`. No browser run: the logic was readable directly.

**Required rows: all three applied correctly.**
- **S-1 (mixtures).** The distillation reply now reads "Distilling off all the water would leave the sand behind, but it takes a long time and a lot of energy…". ✓
- **S-2 (conservation-of-mass, CH and TH).** Rung 2 now uses 0.16 / 0.44 / 0.36 kg and has answer 640, tol 2. The right, wrong and model lines all match. It is live on CH and TH. ✓
- **S-3 (atom-economy).** The frozen q1 is withheld as B3-W9 and is absent from the served source. `bankOn = ready && bankList.length > 0`, so the empty practice section is not rendered. ✓

**New changes, science-checked.**
- **conservation-of-mass, Foundation CFIFA Q2.**
  - The sum: 0.84 kg MgCO₃ → 400 g MgO, CO₂ = 840 − 400 = 440 g.
  - It is stoichiometric: MgCO₃ 84 → MgO 40 + CO₂ 44, × 10 g. ✓
  - The close line "0.84 − 400 mixes kilograms and grams" is right. ✓
- **conservation-of-mass, worked example 1.**
  - The sum: 25.0 g CaCO₃ → 14.0 g CaO, CO₂ = 11.0 g.
  - It is stoichiometric: 100 : 56 : 44 × 0.25. ✓
- **atom-economy, worked example 2.**
  - The equation 2CuO + C → 2Cu + CO₂ is balanced: Cu 2/2, O 2/2, C 1/1. ✓
  - Mr: CuO = 63.5 + 16 = 79.5. ✓
  - The sum: 2 × 63.5 = 127; 2 × 79.5 + 12 = 171; 127 ÷ 171 × 100 = 74.27 → 74.3 % (3 s.f.). ✓
  - The note "the equation makes 2Cu and uses 2CuO: both numbers go in" is right. ✓
- **atom-economy, rung 3 at 3 marks.** It has three links (addition, then one product, then all atoms in the desired product), so it is consistent with the examination's 2-mark scheme plus the equation. ✓
- **mixtures, desk reorder.** Every round keeps its correct key and replies. ✓
- **mixtures, new "Muddy pond water" round.**
  - The key is filtration; mud is insoluble, so it is the residue and the clear water is the filtrate. ✓
  - All four distractor replies are true. ✓
  - The round asks only for "clear" water, not "pure" water, which is the right word: the filtrate is not pure. ✓
- **mixtures, fractional distillation explainer.** Trimming it is fine. "Collected one after another as the thermometer reading rises" is kept. The "lowest boiling point reaches the top first" point is still taught in desk round 4 and rung 3. ✓
- **mixtures, key note.** "Fractional distillation: liquids whose boiling points are close together." closes A-4. ✓
- **microscopy.**
  - New hook reply: "More magnification alone gives a bigger blur, not more detail." ✓
  - The RP block was trimmed (Variables and lamp line removed). Nothing false is left. The 'no variables' point is not examined content. ✓
  - The drawing title "Onion epidermis cells, seen at ×400" is right. ✓
  - The ×3.3 reply closes A-3. ✓
  - New convert-first example: chloroplast 4 µm, drawing 30 mm, so 30 000 ÷ 4 = ×7500. A 4 µm chloroplast is realistic. ✓
  - Key-note line: "Magnification = how many times bigger the image is than the real object." ✓
  - The unit ladder reads mm ×1000 → µm, µm ×1000 → nm. ✓
- **early-atmosphere.**
  - Hook heading now says "Venus and Mars may still have…" (closes A-9). ✓
  - New rung 2(b): "Describe how the percentage of oxygen changed from 2.7 billion years ago to today". The keyed option "rose gradually to about 21%" matches the sketch graph, which is 0 at 2.7 bn and rises steadily to 21 at 0. All three distractors contradict the graph. ✓
  - The ocean herring reply "Oceans dissolve gases from the air; they did not supply the nitrogen" is true. ✓
  - The command-word card change (Give replaces Suggest) is not a science matter. ✓
- **greenhouse-gases.**
  - Hook replies: "reflecting is the most common wrong answer" and "ozone and ultraviolet are a separate problem" are both true. ✓
  - New peer-review item: the key is "Other experts checked its methods and conclusions before it was published". The why line, "trustworthy… does not prove it", matches 5.9.2.2. Distractors (proved forever, government funding means no bias, no errors) are correctly wrong. ✓
  - Report B now carries "plus carbon dioxide records", which supports the correlation question. ✓
  - "Natural gas is mainly methane" in all three places closes A-10. ✓

### ADVISORY (round 2)

| # | where | note |
|---|---|---|
| A-12 | greenhouse-gases, explainer 3 (climate change) | The list of effects was cut to "Its effects reach the sea, the weather, food and wildlife." The spec asks pupils to "describe briefly four potential effects" (5.9.2.3). The specific effects are now only in key-note line 04 and the exam-trap options. That is still taught, so this is not required. Optional: restore one short concrete list, e.g. "rising sea levels, more severe storms, changes in rainfall, less food in some regions, and species moving or dying out". |

A-1, A-2, A-5, A-6, A-7, A-8 and A-11 stand as written (all optional).

### Final verdicts (round 2)

| lesson | verdict |
|---|---|
| microscopy | SCIENCE PASS |
| mixtures | SCIENCE PASS |
| conservation-of-mass | SCIENCE PASS |
| atom-economy | SCIENCE PASS |
| early-atmosphere | SCIENCE PASS |
| greenhouse-gases | SCIENCE PASS |

**Frozen items still served that should be withheld:** none.

**Items for Mide:** none.
