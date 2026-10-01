# Batch 2 — quality review, group A

Reviewer: fresh Opus quality reviewer, 1 Oct 2026. Lessons: chromosomes-mitosis, eukaryotes-prokaryotes, enzymes, carbon-cycle, decomposition, changes-in-energy, internal-energy, lenses.

**What I compared against.** The pilot: metallic-bonding, resistors-iv (RP, CFIFA) and series-parallel-circuits, read end to end in Design's source and as built pages. Also architecture.md, AUTHORING-BRIEF.md, content_standards.md, every lesson's `.dc.html`, its notes, its examination file, and the KS4SRC record in `shared/ks4-source-batch-2.js`.

**How each page was driven.** Built pages were served from `mrbadmus_site/` on port 8715 and driven in headless Chrome through `ks3_browser.py`:

- **Triple Higher:** 390 px light by tap (real CDP mouse events), and 1280 px dark by keyboard (focus, then Enter or Space through CDP key events).
- **Foundation (CF, or TF for lenses):** 390 px dark by keyboard, and 1280 px light by tap.
- **The other four width × theme combinations:** load-and-audit only.

A generic player pressed every control, solved every Ks4Sort and Ks4Chain, filled every input and self-marked every Ks4Write.

The two required-practical sims depend on timing, so I drove them with dedicated scripts to full completion: enzymes all five pH values → anomaly → mean → graph, by keyboard in reduced motion; decomposition all five temperatures → rate → graph → Suggest, by tap with motion on.

**Machine checks, all 8 lessons, all four routes:**

- zero console errors (only the CORS-blocked `onrender.com/api/health` call that every localhost page makes);
- no `undefined`, `NaN`, `{{`, `[object` or `null` text;
- no sideways scroll at 390 px;
- no clickable non-button element;
- theme follows `html[data-theme]`.

**Two non-defects, ruled out:**

- *A sideways scroll at 390 px in early runs.* My player had typed a 30-character unbroken string into the CFIFA inputs, and the shared Ks4Cfifa "You wrote:" echo did not wrap it. Engine-level, see A-E1. It is not a lesson defect.
- *"Sampling…" apparently stuck at 9:30 in the enzymes RP.* The screenshot was taken mid-run; a timed re-drive completes normally.

**Prose, counted on the built page.** "Max run" is the longest stretch of explainer and hook prose before the next commitment. "Total" is explainer plus hook words:

| lesson | max run | total |
|---|---|---|
| chromosomes-mitosis | 91 | 292 |
| eukaryotes-prokaryotes | 74 | 202 (TH) |
| enzymes | 74 | 184 |
| carbon-cycle | 85 | 193 |
| decomposition | 72 | 154 (TH) |
| changes-in-energy | 81 | 156 |
| internal-energy | 97 | 241 |
| lenses | 128 | 171 |

Every lesson is inside both budgets (150 before a commitment, 700 total). Prose length is not a problem anywhere in this group.

**Cross-lesson issues to fix in one pass.**

- **Q-X1:** four lessons hard-code route pills. See Q-C1, Q-CE1, Q-IE1 and Q-L1.
- **Q-X2:** carbon-cycle and decomposition open with the same hook. See Q-D1.

---

## chromosomes-mitosis — PROCESS

1. **Laws.** Phenomenon first (one egg, trillions of cells). Every stage of the stepper is predict-gated, and 92-vs-46 and mitosis-vs-meiosis are confronted at the stage where each error is born. The chain and sort form a real watch-then-do pair, with production in the r4 6-marker, and the DNA-mass graph is drawn as it grows. Command words are taught and the reduced-motion swap is present. There is no examiner tip in the source, so the slot is correctly omitted.
2. **Budget.** Stepper L, chain M, sort M, cancer Choice micro. Fits PROCESS.
3. **CFIFA.** Not applicable.
4. **Ladder.** Four rungs scored, each with a tariff and command word. r4 is 6 marks with levels.
5. **Redundant text.** See the rows.
6. **Built page.** Clean on every route, by tap and by keyboard, light and dark. Figure text is small at 390 px (A-C1).

REQUIRED
- **Q-CM1** · all routes · `s-cancer` logic `cancerReveal`
  - OLD: `The cell cycle normally runs under control. When changes in a cell remove that control, it keeps dividing and forms a tumour. Benign tumours stay in one area; malignant ones spread in the blood and form secondary tumours.`
  - NEW: `Mitosis is normal; losing control of it is the disease.`
  - Why: the explainer immediately above already states the benign/malignant sentence word for word.
  - Cite: Mide's no-redundant-text rule.
- **Q-CM2** · all routes · `STAGES[0].qs[1].opts`
  - OLD: `['8 chromosomes', '4 chromosomes, each now two copies', '2 chromosomes']`
  - NEW: `['8 chromosomes, each one copy', '4 chromosomes, each two copies', '2 chromosomes, each four copies']`
  - Why: the key is the only long option, so it can be picked by length. The `why[0]` and `why[2]` texts still fit.
  - Cite: Law 10; content_standards §1 length parity.
- **Q-CM3** · all routes · `cellFig()` header text
  - OLD: the in-figure titles `'Two cells · 4 chromosomes each'` / `'One set of chromosomes to each end · two nuclei'` / `'Bigger, more organelles, every chromosome copied'`, each shown together with `cellCaps` (`'After stage 3 · two new cells'` etc.) and the verdict text.
  - NEW: delete the `D.T(320, 28|34, …)` title line from `cellFig` stages 1–3 and keep the figcaption.
  - Why: each state is captioned twice and then restated in the verdict.
  - Cite: no-redundant-text rule.

ADVISORY
- **A-CM1:** the source key note says `Cancer = uncontrolled mitosis caused by mutation in regulatory genes.` That sits beside the lesson's own `"Cancer is caused by mitosis."` flaw-spotter and uses "mutation" where the spec says "changes in cells". Either override `keyLines` with the 4.2.2.7 wording or flag it to the examiner.
- **A-CM2:** the meiosis box sentence `You meet it in Inheritance, on both tiers.` tells a pupil nothing they need now. Cut it.

**VERDICT: FIX** (Q-CM1–3, all small text and logic edits).

---

## eukaryotes-prokaryotes — CONTRAST

1. **Laws.** The flagship structure-builder is predict-gated, with confrontations for "bacteria have a nucleus" and "cellulose wall". The scale estimator is a strong concrete→diagram step. CFIFA and the ladder are good. **But the flagship's answers are given away before it starts** (Q-EP1).
2. **Budget.** Builder L, estimator M. Fits.
3. **CFIFA.** Two source FIFAs verbatim behind a Convert step, plus a third "convert first" example. The two attempts open with the convert decision, and Foundation and Higher numbers differ (Higher has the rearrangement). Pass.
4. **Ladder.** Pass. r4 Compare is 4 marks with points.
5. **Redundant text.** See the rows.
6. **Built page.** Clean on every route. Two estimator figures do not read at 390 px (Q-EP4).

REQUIRED
- **Q-EP1** · all routes · logic `hookReveal` and the first `.ks3-explainer`
  - Hook OLD: `A bacterium has no nucleus. Its genetic material is a single DNA loop in the cytoplasm, and it may also have one or more small rings of DNA called plasmids. Whether the genetic material is enclosed in a nucleus is the difference between the two kinds of cell.`
  - Hook NEW: `Not in a nucleus: a bacterium has none. Its DNA is loose in the cytoplasm. What else differs, you decide below.`
  - Explainer: delete `They are much smaller, and their genetic material is not enclosed in a nucleus.`
  - Why: builder items 1 (nucleus), 4 (DNA loop) and 5 (plasmids) are answered in the two blocks the pupil reads just before the builder, so its predictions are recall of text above, not prediction.
  - Cite: Laws 4 and 10.
- **Q-EP2** · all routes · `hookOptions[0].reply` and `hookOptions[1].reply`
  - OLD: `Hold that thought: the builder below tests it.` (on both)
  - NEW: `''` (empty)
  - Why: the reveal answers it in the same panel straight away, so the line is false.
  - Cite: no-redundant-text rule.
- **Q-EP3** · all routes · `s-hook` paragraph
  - OLD: `Both are living cells, and both need DNA to make their proteins. The cheek cell is about 20 µm across. The bacterium is about 2 µm long.`
  - NEW: `Both are living cells, and both need DNA to make their proteins.`
  - Why: both sizes are printed in the figure directly below.
  - Cite: no-redundant-text rule.
- **Q-EP4** · all routes · `fitFig` k=1 and k=2
  - Defect: at 390 px the 100 ribosomes and 100 animal cells shrink to a hairline and the "2 mm" label renders at about 6 px. The reveal shows nothing the pupil can see.
  - Fix: add a magnified inset of the first five units with a "×100" count label, and set label font ≥ 26 in the 640 plate.
  - Cite: Laws 8 and 9; brief §5 "works at 390 px".
- **Q-EP5** · all routes · logic `fText` (right answer)
  - OLD: `FIT_OPTS[fit.a] + ': convert, then divide.'`
  - NEW: comparison 1 → `'×10: both already in µm, so just divide.'`; comparisons 2–3 → `FIT_OPTS[fit.a] + ': convert, then divide.'`
  - Why: comparison 1 has nothing to convert, so the feedback teaches a false step.
- **Q-EP6** · all routes · `s-scale` eyebrow
  - OLD: `Estimate · how many fit across? · {{ fName }}`
  - NEW: `Estimate · {{ fName }}`
  - Why: the commit prompt below already asks "How many fit across…".
  - Cite: no-redundant-text rule.

ADVISORY
- **A-EP1:** builder verdicts join `why` and `yes`. Ribosomes then reads "make proteins too … Both cells make proteins". Make `why` the correction only.
- **A-EP2:** builder labels "DNA loop" and "mitochondria" sit on top of drawn lines, and the animal cell's ribosomes are unlabelled.
- **A-EP3:** the Triple explainer "Bacteria multiply fast…" is 4.1.1.6 content stranded with no activity. Move it to culturing-microorganisms.

**VERDICT: FIX** (Q-EP1–6; Q-EP1 is the substantive one).

---

## enzymes — REQUIRED PRACTICAL

1. **Laws.** Strong:
   - the lock-and-key bench animates complementary fit, denaturing and the products counter, under predictions;
   - the RP sim is predict-gated and makes the pupil judge the end point (wrong taps get named corrections), find a planted anomaly, compute a mean and see the graph;
   - the reduced-motion swap works (driven).
2. **Budget.** RP sim L, bench M, variables sort M, flaw-spotter and sketch picker micro. Fits.
3. **CFIFA.** min→s conversions, Foundation and Higher numbers differ, Higher rearranges. Pass.
4. **Ladder.** Pass. r4 is a 6-mark method with levels.
5. **Redundant text.** See the rows.
6. **Built page.** Clean. The RP was driven to completion by keyboard in reduced motion, and with motion by tap.

REQUIRED
- **Q-EN1** · all routes · `thinkReveal`
  - OLD (last sentence): `Cold is different: it slows an enzyme down without changing its shape, and warming it again restores the rate.`
  - NEW: delete it.
  - Why: the bench's final reply (`Cold would only have slowed it; heat changed its shape.`) and `curveTexts[3]` already say this. It is the third telling on one screen.
  - Cite: no-redundant-text rule.
- **Q-EN2** · all routes · `keyLines`
  - OLD: the appended line `Above the optimum temperature, or at an extreme pH, the active site changes shape, so the substrate no longer fits.`
  - NEW: delete it.
  - Why: it repeats the source line `Denaturation is permanent — caused by high temperature or extreme pH.` that sits directly above it on the card.
  - Cite: no-redundant-text rule.
- **Q-EN3** · all routes · `hookOptions[0].reply`
  - OLD: `Hold that. The lesson names the something, then tests it.`
  - NEW: `''`
  - Why: the reveal directly below names amylase at once, so the line is false.

ADVISORY
- **A-EN1:** the graph label "not digested" overlaps the y-axis at 390 px.
- **A-EN2:** the curve of best fit is drawn through a rate of 0 at pH 4, where nothing was measured ("> 600"). An examiner would not join an unmeasured point. Draw the curve from pH 5 to 8 only.

**VERDICT: FIX** (Q-EN1–3, text only).

---

## carbon-cycle — PROCESS

1. **Laws.** The one-atom trace is an excellent flagship: animated, predict-gated, with feeding and decay confrontations at the step where each error is born. The arrow-labelling task is the right "do". The plants-respire Predict is good.
2. **Budget.** Trace L, label M, sort M. Fits.
3. **CFIFA.** Not applicable.
4. **Ladder.** Pass. r2 is a "Name" data rung on a new diagram (a pond), which is good.
5. **Redundant text.** See the rows.
6. **Built page.** Clean on every route. At 390 px the 800×530 plate's store sub-labels render at about 5 px (A-C1). The page header does not match the pilot (Q-C1).

REQUIRED
- **Q-C1 (Q-X1)** · all routes · header
  - OLD: `<span …>Combined · Triple</span><span …>Foundation · Higher</span>`
  - NEW: the route chip block used by chromosomes-mitosis (`<details class="ks3-route-switch">…{{ routeWords }}…</details>`).
  - Why: the built pilot pages and four sibling batch lessons show the route chip. These static pills list all four routes on a one-route page, so they carry no information.
  - Cite: brief §1; batch-engine §2.
- **Q-C2** · all routes · logic `tReplyText`
  - OLD: `committed ? st.opts[pick].r : ''`
  - NEW: `committed && !right ? st.opts[pick].r : ''`
  - Why: on a right answer the reply and `tReveal` say the same thing back to back. For example `Yes. Combustion joins the carbon to oxygen as carbon dioxide.` followed by `Combustion. Carbon locked away…`, and the step-2 and step-4 repeats. The pilot's correct path shows the explanation only once.
  - Cite: no-redundant-text rule.
- **Q-C3** · all routes · `rungs.r2.parts[1].options`
  - OLD: `['Photosynthesis', 'Respiration by microorganisms', 'Combustion', 'Fossilisation']`
  - NEW: `['Photosynthesis by algae', 'Respiration by microorganisms', 'Combustion of the remains', 'Fossilisation of the remains']`
  - Why: the key is the only three-word option.
  - Cite: Law 10; content_standards §1.
- **Q-C4** · all routes · `keyLines`
  - OLD: `K.keyLines(slug).concat([...])`. The source card lists `decomposition` as its own CO₂-returning process, beside "dissolution in oceans" and "volcanic activity".
  - NEW: authored lines, as decomposition does:
    - "Photosynthesis takes carbon dioxide out of the air."
    - "Feeding passes carbon compounds along food chains."
    - "Respiration by plants, animals and decomposers returns carbon dioxide."
    - "Combustion of fossil fuels returns carbon locked away for millions of years."
    - "Deforestation and burning add carbon dioxide faster than it is removed."
  - Why: the revision card re-teaches the exact error the lesson confronts ("Decomposers release carbon dioxide by decomposing…") and contradicts the lesson's own scope note about oceans, rocks and volcanoes. The source key note is not on the frozen list.
- **Q-D1 (Q-X2)** applies here as well: this lesson keeps its hook; decomposition changes.

ADVISORY
- **A-C1:** the trace and label plates are illegible at 390 px, and the nine selects scroll the diagram off screen. Consider a sticky diagram, or one select under the diagram that steps through the arrows.
- **A-C2:** the explainer sentence `Oceans and rocks hold carbon too, and you meet those in chemistry.` duplicates the `legal` line. Keep one.

**VERDICT: FIX** (Q-C1–4).

---

## decomposition — REQUIRED PRACTICAL (Triple) / PROCESS slice (Combined)

1. **Laws.**
   - **Triple** is strong. The milk RP makes the pupil judge a colour end point (an early stop is refused with the rule), 60 °C never clears, and the pupil computes the rate from their own time, sees the graph and makes a Suggest choice.
   - **Combined** is the leaf stepper plus one flaw-spotter only.
2. **Budget.**
   - Triple: RP L, leaf stepper M, compost sort M. Fits.
   - **Combined: no mid-size activity at all** (Q-D2).
3. **CFIFA.** Triple only, days→weeks and kg→g, tiers differ, Higher rearranges. Pass.
4. **Ladder.** Both ladders pass (Combined r4 is 4 marks with points; Triple r4 is 6 marks with levels).
5. **Redundant text.** See the rows.
6. **Built page.**
   - The RP was completed with motion on by tap, and the rest was driven on CF by keyboard. Clean.
   - On CF/CH the practice bank holds one item, and it is about detritivores, which the lesson does not teach (A-D2).

REQUIRED
- **Q-D1 (Q-X2)** · all routes · `s-hook` (h2, paragraph, prompt, `hookOptions`, `hookReveal`)
  - Defect: the hook is the same phenomenon, question and options as carbon-cycle's. Carbon-cycle has "A fallen leaf rots away… where did the leaf's carbon go?"; this lesson has "A leaf falls in autumn… Where did most of the leaf's carbon go?". Both offer "into the air as CO₂ / into the soil / destroyed / coal or worms". Rainford teaches the two lessons back to back.
  - The hook reveal also pre-answers stepper step 1 and the `s-think` flaw. The respiration answer is then given three times before the pupil is asked.
  - NEW: a different phenomenon, for example a compost heap steaming on a frosty morning. Ask "Where does the heat come from?", with the answer "decomposers respiring". Keep the reveal to that one fact. The carbon question then belongs to stepper step 1.
  - Cite: architecture "two lessons… identical… only because the content needs it"; Laws 1, 4 and 10.
- **Q-D2** · CF, CH
  - Defect: Combined pupils get one instrument (the stepper) and no M.
  - NEW: add one base-tagged mid-size sort, "Returned to the air / returned to the soil / stays locked away".
    - Items: carbon in a leaf's sugars, nitrate in droppings, carbon in a buried fern, ammonium in a dead mouse, carbon in a fungus's own cells (respired), magnesium in a leaf.
    - Each item carries a corrective `why`.
  - Cite: the instrument budget (one L, one or two M).
- **Q-D3** · TF, TH · logic `rateLabel`
  - OLD: `'Calculate the rate at 40 °C from your time: rate = 1 ÷ ' + own[40] + ' s.'`
  - NEW: `'Calculate the rate at 40 °C from your time.'`
  - Why: the label already writes the Insert line, so the pupil only presses divide. The value then appears three times: label, `rateText` and the table.
  - Cite: Laws 6 and 10; no-redundant-text rule.
- **Q-D4** · TF, TH · logic `rateText` (wrong answer)
  - OLD: `'Divide 1 by your time in seconds. The answer is small: about 0.007.'`
  - NEW: `'Divide 1 by your time in seconds; the unit is s⁻¹.'`
  - Why: "about 0.007" is the answer for most pupils, whose 40 °C time is about 142 s.
  - Cite: Law 10.
- **Q-D5** · TF, TH · `s-sim` caption
  - OLD: `Your times for the pink to go, in seconds.`
  - NEW: delete it.
  - Why: the table header already says `TIME / S`, and the aria-label stays.
  - Cite: no-redundant-text rule.

ADVISORY
- **A-D1:** the curve of best fit runs up to an unmeasured "> 600" point at 60 °C, and the "still pink" label is clipped at the plate edge at 390 px.
- **A-D2:** the CF/CH bank is one frozen detritivores question (detritivores are not in AQA 4.7.2.2). Add it to Mide's list as a bank-size and scope issue (content_standards §1 floor of 5).

**VERDICT: FIX** (Q-D1–5; Q-D1 and Q-D2 are structural).

---

## changes-in-energy — QUANTITATIVE

1. **Laws.** Good structure: hook (twice the speed), store bench with ×-factor predictions and animated bars, units sort, weight-is-not-mass flaw, CFIFA.
   - The bench's predictions are pre-answered by the explainer (Q-CE2).
   - **Law 7 is broken:** Ek and Ep are labelled "Equation sheet", but both are learn-it equations (Q-CE3).
2. **Budget.** Bench L, units sort M, flaw-spotter micro. Fits.
3. **CFIFA.** Two source FIFAs verbatim behind "Nothing to convert", plus a convert example; Higher's is a strong Ep→Ek chain. Attempts open with the convert decision, and tiers differ. Pass, apart from the placeholder in Q-CE3.
4. **Ladder.** Rungs pass, but r1 is a Calculate item, not Recall (A-CE2). r4 is 6 marks with levels.
5. **Redundant text.** See the rows.
6. **Built page.** Clean on every route, both input modes and reduced motion. The header does not match the pilot (Q-CE1).

REQUIRED
- **Q-CE1 (Q-X1)** · header
  - Replace the static `Combined · Triple` / `Foundation · Higher` pills with the route chip, as in Q-C1.
- **Q-CE2** · all routes · first `.ks3-explainer`
  - OLD: `Each equation multiplies quantities together, but two of them square one quantity: speed in the kinetic equation, extension in the elastic one.`
  - NEW: delete it.
  - Why: bench rounds 2 and 3 ask exactly which factor gets squared, so this sentence answers them in advance. The hook reveal has already covered speed.
  - Cite: Laws 4 and 10.
- **Q-CE3** · all routes · `s-equation`, plus CFIFA question `Formula` placeholders
  - OLD: `<span …>Equation sheet</span>` on the Eₖ = ½ m v² card and the Eₚ = m g h card; `placeholder: 'as on the equation sheet'` in `ce-q1` (Higher and Foundation) and `ce-q2` (Foundation Eₖ).
  - NEW: `Learn it` on the Eₖ and Eₚ cards (keep `Equation sheet` on Eₑ); placeholder `'learn it'` on every Eₖ or Eₚ question.
  - Why: the lesson's own examination C15 says "Ek learn it (8463 Appendix A recall list, eq 10); Ep learn it (eq 11); Ee on the sheet (eq 4)". As written, the page tells pupils a recall equation will be given to them.
  - Cite: Law 7; brief §4 "Equation blocks label each equation".
- **Q-CE4** · all routes · `ROUNDS[0].ask` and `ROUNDS[1].ask`
  - OLD: `The height doubles. What happens to…` / `The extension doubles. What happens to…`
  - NEW: `What happens to the energy in the gravitational potential store?` / `What happens to the energy in the elastic potential store?`
  - Why: the h2 directly above already says "twice as high" / "twice as far".
  - Cite: no-redundant-text rule.

ADVISORY
- **A-CE1:** there is no Key fact block. All 14 pilot lessons and most of the batch have one.
- **A-CE2:** r1 (`k = 400 N/m`) is a 1-mark calculation, not recall. Use a State item, for example the factor by which Eₖ changes when v doubles.
- **A-CE3:** in the Foundation convert example the Insert line `k = 40 N/m, e = 0.15 m` lists values instead of substituting them. Make it `Ee = ½ × 40 × 0.15²` and let Fine-tune square it.
- **A-CE4:** the bar labels (`1260 J` / `2520 J`) repeat the working lines' results on the same screen. Consider dropping the bar labels.

**VERDICT: FIX** (Q-CE1–4; Q-CE3 is an exam-visibility error).

---

## internal-energy — MODEL

1. **Laws.** Strong. The heating bench shows particles, a kinetic/potential bar and a live temperature–time curve, with a prediction at each regime change and the "keep heating, keeps getting hotter" confrontation where that error is born. The compare sort and cooling-curve reading are good mid-size do-tasks. The Determine data rung reads a graph.
2. **Budget.** Bench L, two sorts M. Fits.
3. **CFIFA.** Not applicable (no calculation, by spec).
4. **Ladder.** Pass. r4 is 6 marks with levels.
5. **Redundant text.** See the rows.
6. **Built page.** Clean on every route, both input modes. The header does not match the pilot (Q-IE1).

REQUIRED
- **Q-IE1 (Q-X1)** · header
  - Replace the static pills with the route chip, as in Q-C1.
- **Q-IE2** · all routes · second `.ks3-explainer`
  - OLD: `So a large object at a low temperature can hold far more internal energy than a small hot one.`
  - NEW: delete it.
  - Why: the very next block asks the pupil to spot that exact flaw (iceberg vs coffee), so the answer is printed directly above the question.
  - Cite: Laws 3, 4 and 10.
- **Q-IE3** · all routes · `thinkOptions[0].text`
  - OLD: `Temperature is linked to the average energy of one particle. Internal energy adds up every particle, and the iceberg has vastly more.` (23 words; the longest distractor has 17)
  - NEW: `Temperature tracks the average particle; internal energy is the total, and the iceberg has far more particles.`
  - Why: the key is the longest option and can be picked by length.
  - Cite: Law 10; content_standards §1 rule `1-length-parity` (≥ 4 words longer).

ADVISORY
- **A-IE1:** there is no Key fact block (pilot anatomy), and no equation-sheet link, although the explainer cites two sheet equations.
- **A-IE2:** the hook reveal fully answers bench stage 4 (boiling). Consider ending the reveal at "It stays at 100 °C." and letting the bench say why.

**VERDICT: FIX** (Q-IE1–3).

---

## lenses — MODEL (Triple only)

1. **Laws.** The lens bench is a fine flagship:
   - two lenses and seven set-ups;
   - three predictions per set-up, then rays drawn with motion and a reduced-motion swap;
   - the misconception "A convex lens always forms a real image" is confronted at the inside-F set-up.

   **But the "Complete the ray diagram" do-task trains recognition, not drawing** (Q-L2).
2. **Budget.** Bench L, ray-diagram stepper M, sort M, eye Choice micro. Fits.
3. **CFIFA.** Foundation and Higher examples and attempts differ, cm↔mm conversions are present, Higher rearranges. "On the sheet" is correct for magnification. Pass.
4. **Ladder.** Pass. r4 Compare is 4 marks with points.
5. **Redundant text.** See the rows.
6. **Built page.**
   - Clean on TF and TH, both input modes, light and dark. My first 1280-dark keyboard run timed out under server load; the re-run was clean.
   - The header does not match the pilot (Q-L1).
   - When the pupil predicts "No image", the unasked Size and Way-up verdicts render in the alert (wrong) style (A-L1).

REQUIRED
- **Q-L1 (Q-X1)** · header
  - OLD: `Triple · physics only` + `Foundation · Higher` pills
  - NEW: the route chip, as in Q-C1.
- **Q-L2** · TF, TH · `s-build` (`C_STEPS`, `cOpts`)
  - Defect: the section claims "Your turn · complete the ray diagram" (the AQA command word), but each step is a four-option text MCQ, a recognition demand. Law 5 names ray diagrams explicitly as a drawing the pupil must produce.
  - NEW: make the choices tap targets on `buildFig` itself: F, 2F, the lens centre, the far edge and the crossing point for steps 1–3, and the traced-back point for step 4. Draw the ray to the tapped point, then show the existing `r` feedback.
  - Cite: Laws 5, 6 and 10.
- **Q-L3** · TF, TH · logic `WHY`
  - OLD (for example cx30): `Beyond 2F, the rays cross between F and 2F on the far side: a real, inverted, diminished image. That is the window you saw at arm’s length.`
  - NEW: `Beyond 2F, the rays cross between F and 2F on the far side. That is the window you saw at arm’s length.`
  - Same trim for cx20, cx15, cx6, cv30 and cv6: drop the "real/virtual, upright/inverted, magnified/diminished" list.
  - Why: the three verdict lines above each WHY already state those words.
  - Cite: no-redundant-text rule.
- **Q-L4** · TF, TH · logic `posLabel`
  - OLD: `'Object ' + u + ' cm from the lens · F is 10 cm'`
  - NEW: `'Object distance · F is 10 cm'`
  - Why: the h2 already reads "Convex lens, object 30 cm away". Keep the full text in `aria-valuetext`.
  - Cite: no-redundant-text rule.

ADVISORY
- **A-L1:** after a "No image" prediction, give the unasked Size and Way-up verdicts a neutral style rather than the alert style.
- **A-L2:** `s-eye` teaches Biology 4.5.2.3 inside a Physics lesson, and the eyebrow says so. It is fine on Triple routes, but the examiner should confirm the intent.

**VERDICT: FIX** (Q-L1–4; Q-L2 is the substantive one).

---

## Engine-level (not batch-lesson defects, for the commander)
- **A-E1:** Ks4Cfifa's "You wrote:" echo has no `overflow-wrap:anywhere`. An unbroken pupil entry of 30 or more characters scrolls the page sideways at 390 px.
- **A-E2:** `K.fig(svg, '')` wraps every figure in `<div role="img" aria-label="">`, an empty-named image around a correctly labelled SVG. This happens in the pilot too.

## Verdicts
| lesson | verdict |
|---|---|
| chromosomes-mitosis | FIX — Q-CM1–3 (small) |
| eukaryotes-prokaryotes | FIX — Q-EP1–6 |
| enzymes | FIX — Q-EN1–3 (small) |
| carbon-cycle | FIX — Q-C1–4 |
| decomposition | FIX — Q-D1–5 (hook duplicates carbon-cycle; Combined has no mid-size activity) |
| changes-in-energy | FIX — Q-CE1–4 (Eₖ/Eₚ mislabelled "Equation sheet") |
| internal-energy | FIX — Q-IE1–3 |
| lenses | FIX — Q-L1–4 (ray-diagram do-task is recognition, not production) |
