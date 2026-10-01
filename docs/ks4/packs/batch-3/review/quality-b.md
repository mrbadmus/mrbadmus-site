# Batch 3 quality review: group b (chemistry and biology)

Reviewer: fresh Opus quality reviewer, 1 Oct 2026. Read-only except for this file.

Lessons: microscopy, mixtures, conservation-of-mass, atom-economy, early-atmosphere, greenhouse-gases. Also checked for duplication against the live batch-2 neighbours (atoms-elements-compounds, relative-formula-mass, percentage-yield, using-moles-calculations, eukaryotes-prokaryotes) and against each other.

## How I checked

- **The bar.**
  - Pilot sources read end to end: metallic-bonding (MODEL) and resistors-iv-required-practical (RP, equation block, CFIFA).
  - Pilot blocks read: Ks4Cfifa, Ks4Write, Ks4Ladder.
  - Pilot built pages compared: metallic-bonding and resistors (the resistors RP block measures 143 words as built).
  - Batch-2 quality-b review and the batch-2 neighbour sources read for the duplication check.
  - Laws from `architecture.md`, `AUTHORING-BRIEF.md` and `content_standards.md`.
- **Static pass.**
  - 6 lessons × 2 routes × 390 and 1280 px × light and dark, so 48 page states. The routes were TH plus CF, except atom-economy, which is Triple only and used TF.
  - Dark mode was forced with `mrb-theme=system` plus emulated `prefers-color-scheme`.
  - Every state was clean:
    - no horizontal scroll;
    - no "undefined", "NaN", "{{" or "[object";
    - zero console errors once the expected `/api` CORS noise is filtered;
    - the dark ground renders as `rgb(22,18,14)`.
- **Play-through.** Every activity in every lesson was played to completion twice:
  - TH at 1280 light, **keyboard only** (focus plus Enter on real buttons);
  - the Foundation page at 390 dark, **tap only** (real CDP mouse events).

  In both modes:
  - every hook, flagship, mid-size activity, choice, chain, sort and CFIFA write-it-out reached its done state;
  - all four ladder rungs reached "Score n of 4";
  - every rail node ticked, except the two that are Ks4Sort (S-1).
- **Reduced motion.** I checked the instant swap on the conservation-of-mass flask, the atom-economy strip, the greenhouse bench and the early-atmosphere clock. Each reaches its end state at once, with no SMIL nodes emitted.
- **Ladder parse check.** I typed `1600`, `1,600` and `1 600` into conservation-of-mass rung 2 (CH/TH): see CoM Q-1.
- **Withheld items.** B3-W3/W4, W5 and W6 are absent from the rendered pages on the routes checked.
- **Body prose**, counted from the built pages. All of it is inside ≤ 700 words, and every first commitment is inside ~150 words. The one breach before a later commitment is the microscopy RP block (Q-2).

  | Lesson | Explainer words | Hook words |
  | --- | --- | --- |
  | microscopy | 159 | 54 |
  | mixtures | 150 | 25 |
  | conservation-of-mass | 143 | 49 |
  | atom-economy | 128 | 38 |
  | early-atmosphere | 123 | 33 |
  | greenhouse-gases | 374 | 39 |
- Screenshots and harness stayed in scratch and were deleted.

## Shared finding (not a lesson defect; for the engine owner)

**S-1 · Ks4Sort never ticks its rail stop.** This is the known engine limit. It shows here on `early-atmosphere` `#s-evidence` and `greenhouse-gases` `#s-sources`: both are rail nodes and stay un-ticked after "Every card is where it belongs." Atom-economy's `#s-route` sort is not on its rail, so it is unaffected.

---

## microscopy (QUANTITATIVE + RP1, all routes)

**Assessment**
1. **Laws.**
   - Strong phenomenon hook (300 years without seeing a ribosome).
   - *Resolve it* is predict-gated, plants empty magnification at view 3 and confronts it in three beats at the moment it is born. This is the right instrument for the spec's magnification-vs-resolution point.
   - The bench is predict-gated: eyepiece × objective, then the ×40 view, then counting cells across three fields, then a committed mean with error-specific feedback. That is concrete → diagram → symbol, and the motion has a reduced-motion swap.
   - The unit-slip misconception is confronted again in `#s-think` (12 mm vs 40 µm).
   - The drawing check makes the pupil identify a real RP-drawing error.
   - Production is trained (CFIFA write-it-outs; the r4 method).
   - Law 10 breaks twice: the hook's key distractor gets no feedback (Q-1), and the RP block runs ~200 words before the bench commitment (Q-2).
2. **Budget.**
   - L: bench.
   - M: Resolve it.
   - Micro: draw, think, hook.
   - The family fits.
3. **CFIFA.**
   - The three source FIFAs are verbatim, with a Convert step.
   - Authored convert-first example (µm/mm), plus an nm and standard-form example.
   - The F and H write-it-outs differ, and each opens with the convert decision.
   - Pass.
4. **Ladder.**
   - r1 State 1, verbatim (17 vs 14 words, inside rule `1-length-parity`).
   - r2 Calculate 3: TH 20 nm, CF ×800; both under 1000.
   - r3 Explain 3 chain with two named herrings.
   - r4 Describe 6, levels plus indicative points.
   - Pass.
5. **Redundant text.** Clean apart from advisories.
6. **As built.**
   - Clean in all 8 states.
   - Keyboard and tap complete.
   - The RP chip and the RP1 Combined / RP1 Biology labels are correct.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `hookOptions[0].reply` | `''` → `'More magnification alone gives a bigger blur, not more detail. Resolve it, below, tests this.'` | This distractor is the lesson's central misconception. With an empty reply, Ks4Choice shows only "Locked in." The shared reveal ("first seen in the 1950s, with an electron microscope") then reads as *confirming* "magnify more". Every pilot hook replies to every distractor. | Law 10; pilot `metallic-bonding` hookOptions |
| Q-2 | all | `#s-rp` | **Trim to the pilot's size.** It is 211 words as built, against the pilot RP's 143, and it sits before the bench commitment. (1) Delete the whole paragraph `<strong>Variables.</strong> None to control: this practical is about observing and recording, not testing how one thing affects another.` (2) Risks: `Iodine solution irritates the eyes and stains skin: wear eye protection. Slides and coverslips are thin glass, so handle them by the edges and report any breakage. The microscope lamp can get hot.` → `Iodine solution irritates the eyes and stains skin: wear eye protection. Slides and coverslips are thin glass: hold them by the edges.` (3) Step 2: `Lower a coverslip onto it at an angle, using a mounted needle, so that no air bubbles are trapped.` → `Lower a coverslip at an angle with a mounted needle, so no air bubbles are trapped.` | ≤ ~150 words before every commitment. The Variables line tells the pupil that there is nothing to know. | Law 2; Mide's no-redundant-text rule; pilot resistors `#s-rp` |
| Q-3 | all | `drawSvg()` title, and `drawAlt` | `'Onion epidermis cells ×400'` → `'Onion epidermis cells, seen at ×400'`. In `drawAlt`: `titled Onion epidermis cells ×400` → `titled Onion epidermis cells, seen at ×400` | On CF/TF, the Foundation CFIFA Q1 close says "The drawing's magnification is not the microscope's ×400: it depends on how big you draw." A model drawing titled "×400" teaches the opposite on the same page. | Internal consistency; RP1 drawing conventions |

**ADVISORY**
- A-1. **Duplication with live eukaryotes-prokaryotes.** EP (batch 2) already runs a full magnification CFIFA and equation card:
  - convert-first: bacterium 2 µm shown 12 mm, ×6000;
  - CF Q2: bacterium 3 µm drawn 15 mm, **×5000**;
  - CH Q2: ribosome 25 nm at 5 mm, in standard form;
  - both r2s: actual size in µm from mm.

  Microscopy is the spec home of the calculation (4.1.1.5), and its CFIFA is right. But its authored convert-first example (chloroplast 5 µm, 25 mm, **×5000**) mirrors EP's Q2 shape and answer. Change it, for example to `A chloroplast is 4 µm long. In a drawing it is 30 mm long.` → 30 000 ÷ 4 = ×7500. For the commander: EP's magnification CFIFA could be cut back to its order-of-magnitude content in a later pass, now that microscopy owns this.
- A-2. Key note line 04 is the source's `Magnification = size increase.` Re-cut it as `Magnification = how many times bigger the image is than the real object.` (key_note is not a frozen field; the author already re-cut line 03).
- A-3. In the equation card, `mm —×1000→ µm —×1000→ nm` wraps mid-arrow at 1280 ("… µm —" / "×1000→ nm"). Put each step on its own line, or use non-breaking spaces.
- A-4. Key note "max ×2,000,000" and explainer "×2 000 000" use different number formats on one page.

**Verdict: FIX** (Q-1 to Q-3). The flagship and Resolve it are pilot-grade.

---

## mixtures (CLASSIFY, all routes)

**Assessment**
1. **Laws.**
   - The phenomenon hook (sugar vanishing) commits within 25 words.
   - The desk is predict-gated: the mixture is shown first, and the apparatus is drawn and animated after the pick, with reduced-motion CSS. Every wrong technique has its own corrective reply.
   - The filter-the-salt misconception is confronted as a predict-trap, in three beats.
   - The method chain carries two named herrings.
   - The thermometer-in-the-liquid apparatus check is a good AT 4 practical-skills item, correctly badged "Practical skills", not RP (examination R8).
   - Production: r4 Plan 6.
   - Law 10 breaks on the desk's answer pattern (Q-1).
2. **Budget.**
   - L: desk.
   - M: chain.
   - Micro: think, kit, hook.
   - The family fits.
3. **CFIFA.** No calculation is owned here; the examination §1/R7 gives Rf to `chromatography`. Correct.
4. **Ladder.**
   - r1 Give 1, authored, at parity.
   - r2 Suggest 2 data, with different F and H mixtures.
   - r3 Explain 3.
   - r4 Plan 6, levels plus points plus rejects.
   - Pass.
5. **Redundant text.** See advisories.
6. **As built.** Clean in all 8 states; keyboard and tap complete; the rail ticks fully.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `ROUNDS` | **The desk answers walk straight down the button list.** Round *n*'s answer is button *n* (Filtration, Crystallisation, Simple, Fractional, Chromatography: indices 0, 1, 2, 3, 4), each method is used once, and the order is fixed by "Next mixture". After two rounds the next answer is "the next button down", and round 5 is forced by elimination. **Fix:** reorder `ROUNDS` to `[blue-ink→pure water (a:2), sand (a:0), copper sulfate (a:1), NEW, ethanol (a:3), "The same blue ink" (a:4)]` and insert this NEW round, so that one method repeats: `{ title: 'Muddy pond water', want: 'clear water', a: 0, liquid: '#C9B48A', sand: true, no: ['', 'Crystallisation keeps a dissolved solid and lets the water escape. The mud is not dissolved, and you want the water.', 'Distilling would give water, but slowly and with energy you do not need: the mud does not dissolve, so a filter holds it back.', 'Fractional distillation separates liquids that mix. Mud is an insoluble solid.', 'Chromatography separates dissolved substances a spot at a time. It cannot clean a beaker of water.'], right: 'The mud does not dissolve, so the filter paper holds it back as the residue, and the clear water runs through as the filtrate.' }`. The `no[]` arrays are indexed by technique, so a reorder is safe, and the rail uses `ROUNDS.length`. | No activity solvable by position or elimination. | Law 10; AUTHORING-BRIEF §5 |

**ADVISORY**
- A-1. The second explainer (fractional distillation) restates desk round 4's reveal ("Ethanol, with the lower boiling point, reaches the top first and is collected first") and r3's third link. It then sits directly above a *simple*-distillation activity. Keep only what is new: `In the lab, the column is packed with glass beads: the vapour condenses and boils again many times on its way up. The fractions are collected one after another as the thermometer reading rises, changing the beaker each time.`
- A-2. Desk round 5's reveal ends `How the paper does this, and Rf values, are in the chromatography lesson.` That is a platform signpost, not science. Cut it (the end matter already connects to Chromatography).
- A-3. At 390 px the desk and kit apparatus labels render at about 11 px.

**Verdict: FIX** (Q-1). Otherwise pilot-grade.

---

## conservation-of-mass (QUANTITATIVE, all routes)

**Assessment**
1. **Laws.**
   - The phenomenon hook (sealed flask at 312.48 g) commits within 49 words.
   - The flask is predict-gated: count the atoms, then watch every atom slide to its new partner while the balance reading holds, with a reduced-motion swap.
   - The molecules-not-atoms misconception is confronted in three beats.
   - `#s-write` takes a real word equation through formulae → balancing → state symbols, with feedback on every slip.
   - Production is trained (CFIFA; r4 Write).
2. **Budget.**
   - L: flask.
   - M: word-to-symbol.
   - Micro: think, hook.
   - The family fits.
3. **CFIFA.**
   - The pack has no FIFA.
   - Two authored worked examples: nothing to convert, and kg→g.
   - The F and H write-it-outs differ, and each opens with the convert decision.
   - Pass, apart from the duplications in Q-2.
4. **Ladder.**
   - r1 State 1, authored, at parity.
   - r2 Calculate 2 (F) / 3 (H).
   - r3 Explain 3.
   - r4 Write 4, with points and rejects.
   - The Higher r2 trips the engine's number parser (Q-1).
5. **Redundant text.** Clean.
6. **As built.** Clean in all 8 states; keyboard and tap complete; the rail ticks fully.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | CH, TH | `rungs.r2` (higher branch) | **The answer is 1600 g, and the engine reads "1,600" or "1 600" as 1.** I verified this in the browser: a correct "1,600 g" is marked "Not this time" with the feedback "Convert first…", which is wrong advice to a pupil who did convert. **Change the numbers so the answer is under 1000:** prompt `0.40 kg of methane forms 1.10 kg of carbon dioxide and 0.90 kg of water` → `0.040 kg of methane forms 110 g of carbon dioxide and 90 g of water` (rest of the prompt unchanged); `answer: 1600, tol: 5` → `answer: 160, tol: 1`; `right:` → `'Both products count on the right: 200 g in all, and 40 g of it came from the methane.'`; `wrong:` → `'Convert first: 0.040 kg = 40 g. Then 40 + mass of O₂ = 110 + 90.'`; `model:` → `['C · 0.040 kg = 40 g', 'F · total mass of reactants = total mass of products', 'I · 40 + mass of O₂ = 110 + 90', 'F · mass of O₂ = 200 − 40', 'A · 160 g']`. Stoichiometry: 2.5 mol CH₄ → 110 g CO₂, 90 g H₂O, 160 g O₂. | Known engine limit: an r2 answer ≥ 1000 is a defect. | Common brief (engine limits) |
| Q-2 | CF, TF (Q2); all (worked 1) | `cfQ` Foundation Question 2; `cfEx[0]` | **These duplicate live batch-2 numbers.** (a) Foundation Q2 (`0.50 kg of calcium carbonate … 280 g of calcium oxide`) is relative-formula-mass's live rung 2 scenario (CaO from 0.50 kg CaCO₃ = 280 g). Replace it with: head `'0.84 kg of magnesium carbonate decomposes completely in a closed container: MgCO₃ → MgO + CO₂. 400 g of magnesium oxide forms. Calculate the mass of carbon dioxide, in grams.'`; close `'Without converting, 0.84 − 400 mixes kilograms and grams and makes no sense.'`; steps `qStep('0.84 kg = 840 g', FM, '840 = 400 + mass of CO₂', 'mass of CO₂ = 840 − 400', '440 g')`. (b) Worked example 1 (`10.0 g … 5.6 g of calcium oxide`) shares its 5.6 g CaO with percentage-yield's live worked example (12.0 g CaCO₃ → 5.6 g CaO). Change to `25.0 g of calcium carbonate … 14.0 g of calcium oxide forms`, with Insert `'25.0 = 14.0 + mass of CO₂'`, Fine-tune `'mass of CO₂ = 25.0 − 14.0'` and Answer `'11.0 g'`. Both sets are stoichiometric. | Do not duplicate the live neighbours. (b) also stops the worked answer (4.4 g) repeating as the answer to F Q1 and H Q1. | Reviewer brief; content_standards §2 |

**ADVISORY**
- A-1. `#s-think` uses 2H₂ + O₂ → 2H₂O, which is atoms-elements-compounds' (live) worked balance and H₂O₂ spot-the-flaw. The key fact ("you never change [a small number] to balance") restates AEC's think reveal. The teaching point here (molecule count ≠ mass) is different and good. A fresh equation would avoid the déjà vu: N₂ + 3H₂ → 2NH₃ (four molecules become two; 2 N and 6 H each side). Update r1 option 2's reply and the r3 herring to match.
- A-2. The `#s-flask` h2 "Count the atoms. Then fire the spark." There is no spark control, and the calcium + water run has no spark. Use "Count the atoms. Then run the reaction."
- A-3. The key note is three lines (the pilot has six). Add the multiplier/subscript line and the state-symbol line.
- A-4. **Line-up overlap with atom-economy (same topic).** Both lessons use the same instrument shell: tabbed reactions, predict, timed run, "✓" tabs, "Called it." / "Not this time.", then a Think, a second M and CFIFA. The content differs; consider a different interaction in one of them.
- A-5. The Higher CFIFA Q2 (blast furnace, Fe₂O₃ + 3CO) is the third lesson on that reaction: percentage-yield TH Q2 (live) and atom-economy's strip and worked example also use it.

**Verdict: FIX** (Q-1, Q-2).

---

## atom-economy (QUANTITATIVE, TF/TH)

**Assessment**
1. **Laws.**
   - The two-factories hook commits within 38 words.
   - The mass strip (bar length = n × Mr, products forming in one move) is a real concrete → diagram → symbol instrument. It is predict-gated and has a reduced-motion swap.
   - The forgotten-coefficient misconception is confronted at the moment it is born, right after the iron run.
   - Brine teaches "the top changes with the product you want".
   - The HT pathway block is correctly tagged HT (8462 4.3.3.2), and its sort reads a real data table.
   - Production: CFIFA, and r4 Evaluate 6 / Calculate 4.
2. **Budget.**
   - L: strip.
   - M: brine, plus the route sort (Higher).
   - Micro: think, hook.
   - The family fits.
3. **CFIFA.**
   - The source ethanol FIFA is verbatim with Convert.
   - Every Convert step is "Nothing to convert". That is accepted: the examination §5 rules that atom economy has no unit conversion and forbids inventing one (notes §89).
   - The F and H write-it-outs differ.
   - Worked example 2 repeats the strip (Q-3).
4. **Ladder.**
   - r1 Give 1, authored, at parity.
   - r2 Calculate 3, F and H differ.
   - r3 tariff wrong (Q-1).
   - r4 TH Evaluate 6 levels / TF Calculate 4 points.
5. **Redundant text.** Q-3.
6. **As built.**
   - Clean in all 8 states; keyboard and tap complete; the rail ticks fully.
   - **The bar-divider lines cut through the labels** (Q-2).

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | TF, TH | `rungs.r3` | `marks: 2` → `marks: 3` | The chain has three links. A 2-mark chip on a 3-link chain is the tariff mismatch fixed in batch 2 (concentration Q-3). | Law 7; batch-2 quality-b conc Q-3 |
| Q-2 | TF, TH | `row()`, the per-unit divider | `D.line(xx, y + 6, xx, y + H - 6, 1.5, D.C.stroke)` → `D.line(xx, y + 1, xx, y + 8, 1.5, D.C.stroke) + D.line(xx, y + H - 7, xx, y + H - 1, 1.5, D.C.stroke)` | The full-height dividers are drawn straight through the centred labels in both the strip and the brine figure. Screenshots read "2F\|e", "2 ×\|56", "2Na\|Cl", "2 ×\|58.5", "2H\|₂O" and "2Na\|OH". Short ticks at the top and bottom still show the units without crossing the text. | Law 8 (diagrams legible); pilot figure standard |
| Q-3 | TF, TH | `cfExamples[1]` | Iron worked example → copper: tab `'Copper · numbers count'`; head `'Calculate the percentage atom economy for making copper: 2CuO + C → 2Cu + CO₂. (Mr: CuO = 79.5; Ar: Cu = 63.5, C = 12)'`; Insert `'(2 × 63.5) ÷ (2 × 79.5 + 12) × 100'` with note `'The equation makes 2Cu and uses 2CuO: both numbers go in.'`; Fine-tune `'= 127 ÷ 171 × 100'`; Answer `'74.3%'` with note `'Give the answer to 3 significant figures.'` | The strip's Iron tab has just printed exactly this working: `(2 × 56) ÷ (160 + 3 × 28) × 100 = 45.9%`. Worked example 2 reprints it line for line, and TF r4 is iron again. | Mide's no-redundant-text rule |

**ADVISORY**
- A-1. The strip's three tabs map one-to-one onto the three bands (Ethanol = all, Lime = more than half, Iron = less than half), so the last tab is answerable by elimination. A fourth reaction, or a band reused, would remove that.
- A-2. The brine wrong replies never name the answer (for example, "Cl₂ is 71 of the 153, just under half."). Append `Hydrogen's 2 is the smallest share.` to each.
- A-3. After the run, the brine and strip "Mr: …" lines repeat the numbers printed inside the bars.
- A-4. The Ethanol strip tab computes 46 ÷ 46 × 100, which is the frozen source FIFA (worked example 1) again. Consider an ethene + hydrogen tab (C₂H₄ + H₂ → C₂H₆) for the 100% case.
- A-5. The `#s-think` quote reads "Mr of Na is 23". It is the pupil's own words, but the lesson then prints the wrong term. Use "Ar of Na is 23".
- A-6. In the bank (frozen, verbatim), one TH item's options carry their own reasoning ("75% — calculated incorrectly", "400% — (80 ÷ 20) × 100 (divided desired by waste…)"). That is a Law 10 problem in a frozen field. It is for Mide or the science examiner to withhold or keep, not for the author.
- A-7. Same-topic line-up overlap with conservation-of-mass (see CoM A-4).

**Verdict: FIX** (Q-1 to Q-3).

---

## early-atmosphere (PROCESS, all routes)

**Assessment**
1. **Laws.**
   - The hook is drawn: three planets' air as share bars.
   - *Run the clock* is a six-stage, predict-gated stepper. The scene and the air bar move only after commitment, with a reduced-motion swap, and the option order is hashed.
   - The volcano-oxygen misconception is confronted at stage 1.
   - The respiration/photosynthesis spot-the-flaw is good.
   - The oil-formation chain has three named herrings.
   - The evidence sort trains Evaluate.
   - Production: r4 Describe 6.
2. **Budget.**
   - L: clock.
   - M: oil chain, evidence sort.
   - Micro: equation spot-the-flaw, hook.
   - The family fits.
3. **CFIFA.** No calculation. Correct.
4. **Ladder.**
   - r1 Give 1, verbatim, at parity.
   - r2 Suggest 2, data with a sketch graph.
   - r3 Explain 3.
   - r4 Describe 6, levels.
   - r1 and r2(b) credit the same fact (Q-2).
5. **Redundant text.** Q-1.
6. **As built.**
   - Clean in all 8 states; keyboard and tap complete.
   - `#s-evidence` never ticks (S-1).
   - The hook label overflows (Q-3).

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | First `ks3-explainer` | `AQA examines one <strong>theory</strong> of how Earth's atmosphere formed and changed. Run the clock forward from the Earth's first billion years to today, and predict each change before you see it. The bar under the picture shows each gas's share of the air.` → `AQA examines one <strong>theory</strong> of how Earth's atmosphere formed and changed.` | Sentences 2 and 3 describe the instrument on screen. Each stage already asks before it reveals. The figure is captioned "The air (sketch, not to scale)" and has a five-gas legend. The legal line says "sketch" a third time. | Mide's no-redundant-text rule |
| Q-2 | all | `rungs.r2` part (b), `model[1]`, `wrong` | Part (b) `Suggest why carbon dioxide fell between 4 and 3 billion years ago` (key: dissolved in the oceans) credits the same fact as r1 ("Why did CO₂ levels decrease as Earth's oceans formed?") and clock stage 2. Replace it with a graph-reading part: `{ label: 'Describe how the percentage of oxygen changed from 2.7 billion years ago to today.', options: ['It rose gradually to about 21%', 'It rose suddenly to 21% straight away', 'It stayed at zero until 0.5 billion years ago', 'It fell from about 21% to almost zero'], answer: 0 }`; `model[1]` → `'(b) It rose gradually, from about 0% 2.7 billion years ago to about 21% today (1)'`; `wrong` → `'Read each line from left to right: oxygen leaves zero at about 2.7 billion years ago, then climbs slowly.'` | Two of the four rungs currently score one recall fact. Rung 2's demand is apply/use data. | Law 10; architecture ladder table |
| Q-3 | all | `hookSvg()`, the label call | `if (sg[0]) b += D.T(x + w / 2, r.y + 42, sg[0], 26, { fill: D.C.stroke });` → `if (sg[0]) b += D.T(x + w / 2, r.y + 42, sg[0], w < 120 ? 19 : 26, { fill: D.C.stroke });` | "O₂ 21%" (26 px) is wider than its 89-unit segment and runs over both borders at 1280 and at 390. | Law 8 (diagrams legible) |

**ADVISORY**
- A-1. r3 (nitrogen) re-runs clock stage 6. Its herring "The oceans gave out nitrogen…" has the identical feedback ("The oceans took gases out of the air. The nitrogen came from volcanoes."). The Explain command card also prints r3's chain ("unreactive, so not removed, so it built up"). Consider r3 on how carbon dioxide was removed (photosynthesis → burial → sedimentary rock and fossil fuels), or a generic Explain card.
- A-2. The `#s-equation` eyebrow "Equation · chemistry has no equation sheet" and the chip "Learn it" say the same thing. Use the single chip the other batch-3 chemistry lessons use: `Learn it · no chemistry equation sheet`.
- A-3. The clock gives no position cue across its six stages (the pilot's instruments show "n of 3").
- A-4. Same-topic line-up overlap with greenhouse-gases: the same staged-stepper code ("No: <key>." verdict, confront panels, Next button), a Ks4Sort as M, a data r2 with a figure, and an r4 6-marker.

**Verdict: FIX** (Q-1 to Q-3).

---

## greenhouse-gases (MODEL, all routes)

**Assessment**
1. **Laws.**
   - Strong numerical hook (−18 °C against 15 °C).
   - The radiation bench is a true parameter instrument: none → natural → extra. Each stage is predict-gated; rays are drawn as short or long waves, absorbed and re-emitted with motion, the thermometer rises, and there is a reduced-motion swap.
   - Two misconceptions (reflect; "get rid of the greenhouse effect") are confronted in three beats at the stage where each is born.
   - The sources sort uses natural gas in both bins, so it cannot be solved by word shape.
   - The limits choice is good applied reasoning.
   - r4 Evaluate 6 against a noisy graph is excellent.
   - Law 10 breaks in three places: Q-1, Q-2, Q-3.
2. **Budget.**
   - L: bench.
   - M: sources sort, reports.
   - Micro: effects, limits, hook.
   - The family fits. Five explainers is a lot (374 words), but each sits before its own commitment.
3. **CFIFA.** No calculation. Correct.
4. **Ladder.**
   - r1 Give 1, verbatim, at parity.
   - r2 Use 2, table.
   - r3 Explain 4 chain with three herrings.
   - r4 Evaluate 6, levels with a graph.
   - Pass.
5. **Redundant text.** Q-4.
6. **As built.**
   - Clean in all 8 states; keyboard and tap complete.
   - `#s-sources` never ticks (S-1).

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `hookOptions[*].reply`, `hookReveal` | All four replies are `''`, and the reveal ("…Each run tests one part of your answer.") never says which idea holds. A pupil who picks "reflect the sunlight" or "block ultraviolet like a shield" sees only "Locked in." Replies: A `'Hold that thought, and test it on the bench below.'`; B `'Reflecting is the most common wrong answer in the exam. Watch what the gases really do on the bench.'`; C `'Ozone and ultraviolet are a separate problem from the greenhouse effect.'`; D `'Run the bench and watch where the sunlight goes.'` Reveal: delete the last sentence `Each run tests one part of your answer.` | Every distractor needs feedback (pilot hooks always reply). The replies above correct without pre-empting bench stage 2's prediction. | Law 10; pilot hookOptions |
| Q-2 | all | Third `ks3-explainer` (effects) | `Potential effects include: sea levels rising as land ice melts and seawater expands, flooding low-lying coasts; more frequent and more severe storms; changes to the amount, timing and distribution of rainfall; heat and water stress for people and wildlife; changes to how much food a region can produce; and changes to where species can live. Scientists weigh…` → `Its effects reach the sea, the weather, food and wildlife. Scientists weigh…` (keep the first and last sentences) | `#s-effects` asks which of four effects would *not* earn a mark. Three options are lifted from the list printed directly above, so the key is "the one not in the paragraph": a matching task, not the claimed discrimination (acidification is a CO₂ effect, not a warming effect). The full list still reaches the pupil in `effReveal` and the key note. | Law 10 (no answer visible); AUTHORING-BRIEF §5 |
| Q-3 | all | `REP[2]` | `{ label: 'Which report has been checked by other scientists?', options: ['Report A', 'Report B'], answer: 1, why: … }` → `{ label: 'Report B was peer reviewed. What does that tell you?', options: ['Other experts checked its methods and conclusions before it was published', 'Its conclusion has been proved true and can never change', 'It was paid for by a government, so it cannot be biased', 'Its data cannot contain any errors or uncertainty'], answer: 0, why: 'Peer review is a check by other experts before publication. It makes the work more trustworthy; it does not prove it.' }` | The current item is answered by reading the card row "Checked before publishing: Yes, peer reviewed": checked → checked, a word match. The replacement trains what peer review means (5.9.2.2), and the existing `order()` hashing shuffles the four options. Parity: 11/11/11/8 words. | Law 10; content_standards §1 |
| Q-4 | all | `bHead` | `bHead: su.name` → `bHead: allRun ? 'Compare the three runs.' : su.name` | Once the tabs appear, the h2 repeats the pressed tab's label word for word (an "Extra greenhouse gases" heading directly above an "Extra greenhouse gases" tab). | Mide's no-redundant-text rule |

**ADVISORY**
- A-1. The eyebrow "Radiation bench · predict, then run" carries an instruction the screen already gives. Use "Radiation bench".
- A-2. At 390 px the bench legend and labels render at about 10–11 px. The incoming short-wavelength rays (ending x ≈ 150–270) cross the "Atmosphere" label: move the label to `x = 400` or start the rays further right.
- A-3. The Report B card title ("Global surface temperature since 1900") never mentions carbon dioxide, yet question 4 begins "Report B shows that carbon dioxide and temperature have both risen…". Add a "Data" line covering CO₂.
- A-4. The Explain command card ("short in, long out, absorbed, re-emitted") prints r3's chain. The pilot does the same, so this is not a defect, but consider a generic card.
- A-5. Same-topic line-up overlap with early-atmosphere (see EA A-4).

**Verdict: FIX** (Q-1 to Q-4). The bench and the r4 evaluation are pilot-grade.

---

## Verdicts

| Lesson | Verdict | Required rows |
| --- | --- | --- |
| microscopy | **FIX** | Q-1 hook reply on "magnify more"; Q-2 RP block over budget; Q-3 drawing titled "×400" contradicts the lesson |
| mixtures | **FIX** | Q-1 desk answers run in button order and are solvable by elimination |
| conservation-of-mass | **FIX** | Q-1 Higher r2 = 1600 trips the parser (verified); Q-2 Foundation Q2 and worked example 1 duplicate live RFM/PY numbers |
| atom-economy | **FIX** | Q-1 r3 tariff 2 on a 3-link chain; Q-2 bar dividers cut through labels; Q-3 worked example 2 reprints the strip's iron working |
| early-atmosphere | **FIX** | Q-1 instrument self-description; Q-2 r1 and r2(b) score the same fact; Q-3 "O₂ 21%" label overflow |
| greenhouse-gases | **FIX** | Q-1 hook has no replies; Q-2 effects trap solvable from the paragraph above; Q-3 peer-review item is a word match; Q-4 h2 repeats the tab |

Every required row is a text or constant edit inside the lesson's own `.dc.html`. None touches a frozen field or the shared engine.

---

## Round 2 (commit 2ddea6225, built pages)

**How I checked.** I read the source diff of all six lessons against `d80d3d4be`, then drove the built pages on a fresh server.
- Tap at 390 px: the mixtures desk (CF), the atom-economy strip and brine (TH and TF), and the greenhouse hook, bench and reports (CF).
- Keyboard at 1280 px: the microscopy hook (TH).
- Also checked: the early-atmosphere hook figure (CF) and the conservation-of-mass Higher rung 2 (CH).
- Every page driven was clean: no console errors, no "undefined", "NaN" or "{{", and no horizontal scroll.
- I did not re-run the 390 dark-theme pass: the round-2 drive forced the dark colour scheme but not the theme setting, so those pages rendered light. Round 1 covered dark mode, and these edits are text and drawing changes only.

| Lesson | Row | Confirmed on the built page |
| --- | --- | --- |
| microscopy | Q-1 | Picking "A lens that magnifies far more" now replies "More magnification alone gives a bigger blur, not more detail. Resolve it, below, tests this." |
| microscopy | Q-2 | The Variables paragraph is deleted and the Risks and step 2 cuts are applied as written. The RP block measures 179 words as built (211 before), counting its heading and figure labels. |
| microscopy | Q-3 | The drawing is titled "Onion epidermis cells, seen at ×400", and the alt text matches. Advisories A-1 (×7500 worked example), A-2 (key note) and A-3 (two-line unit chain) were also applied. |
| mixtures | Q-1 | The desk now has six rounds whose answers run 2, 0, 1, 0, 3, 4 (ink, sand, copper sulfate, muddy pond water, ethanol, ink dyes). Filtration repeats, so the last round is no longer forced. All six rounds completed by tap, and the rail ticks. Advisories A-1 and A-2 were applied too. |
| conservation-of-mass | Q-1 | Following the commander's ruling, the Higher rung 2 uses 0.16 kg CH₄ → 0.44 kg CO₂ + 0.36 kg H₂O, with an answer of **640 g**. That is under 1000 and stoichiometric (10 mol). Entering 640 g is marked "Correct." |
| conservation-of-mass | Q-2 | Foundation Q2 is now MgCO₃, 0.84 kg → 400 g MgO → 440 g CO₂. Worked example 1 is now 25.0 g → 14.0 g → 11.0 g. |
| atom-economy | Q-1 | Rung 3 shows "EXPLAIN 3 marks" on both TF and TH. |
| atom-economy | Q-2 | The unit dividers are short ticks at the top and bottom of each bar. Labels such as "2NaCl", "2 × 58.5" and "2NaOH" are no longer crossed (checked at 390 px). |
| atom-economy | Q-3 | Worked example 2 is now "Copper · numbers count", giving 74.3%. |
| atom-economy | (new) | The question-bank section is now hidden when the route's bank is empty (`bankOn`), so no empty practice block renders on TF or TH. |
| early-atmosphere | Q-1 | The first explainer is now the single sentence "AQA examines one theory of how Earth's atmosphere formed and changed." |
| early-atmosphere | Q-2 | Rung 2(b) is the oxygen-trend graph-reading part, with a matching model answer and feedback. Its command chip changed to Describe. Advisories A-1 (Explain card made generic) and A-2 (single "Learn it" chip) were also applied. |
| early-atmosphere | Q-3 | "O₂ 21%" now renders at 19 px inside its segment. |
| greenhouse-gases | Q-1 | All four hook options reply; the reflect option's reply was shown after tapping it. The reveal no longer ends with "Each run tests…". |
| greenhouse-gases | Q-2 | The effects explainer no longer lists the effects, so the trap can't be matched against the paragraph above. |
| greenhouse-gases | Q-3 | The peer-review item asks "What does that tell you?" with four meaning options. Completed, ending on "All four sound. Report B is the stronger evidence." |
| greenhouse-gases | Q-4 | After all three runs, the heading reads "Compare the three runs." instead of repeating the tab. Advisories A-1 and A-3 were applied, and the "Atmosphere" label is now 20 px at x = 10. |

**Redundancy check on the fixes.** None of the fixes added new redundant text. The new early-atmosphere "Give" command card, the mixtures fractional-distillation key-note line and the Report B "carbon dioxide records" line each carry information not shown elsewhere on their screen.

**Still open (engine, not lessons).** S-1 (a Ks4Sort never ticks its rail node) is unchanged.

### Final verdicts

| Lesson | Verdict |
| --- | --- |
| microscopy | **SHIP** |
| mixtures | **SHIP** |
| conservation-of-mass | **SHIP** |
| atom-economy | **SHIP** |
| early-atmosphere | **SHIP** |
| greenhouse-gases | **SHIP** |
