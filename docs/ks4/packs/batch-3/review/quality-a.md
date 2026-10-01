# Batch 3 — quality review, group A

Reviewer: fresh Opus quality reviewer, 1 Oct 2026. Lessons: temperature-changes-shc, specific-latent-heat, particle-motion-pressure, power, types-of-em-waves, sound-waves-hearing, waves-detection-exploration.

## What I compared against

- **Pilot.** I read resistors-iv (REQUIRED PRACTICAL, CFIFA) end to end in Design's source. I read series-parallel-circuits, metallic-bonding and states-of-matter for template and line-up. I drove the built resistors page for figure and panel anatomy.
- **Batch 2 (live).** I read quality-a, both rounds, and DEPARTURES.md, plus the source of internal-energy and changes-in-energy, the two batch-2 lessons that share a topic with this group.
- **Laws and sources.** architecture.md, AUTHORING-BRIEF.md, each lesson's `.dc.html`, its notes, its KS4SRC record in `shared/ks4-source-batch-3.js` and `ks4_lessons/batch_3.py`.

## How the pages were driven

Built pages were served from `mrbadmus_site/` on port 8724 and driven in headless Chrome through `ks3_browser.py`. The theme was forced through `MRBTheme.set()` plus emulated `prefers-color-scheme`, so each run was explicitly light or dark.

A generic player pressed every control: it filled inputs, chose units, wrote 12+ words into Ks4Write and self-marked. The flagship states it skips past were driven again with targeted scripts:

- the SHC practical: switch-off pick, the "Δθ = final temperature" entry that opens the confrontation, the unlagged run;
- the SLH ledger: a wrong pick at stage 2;
- the PMP examiner sort, solved with one card misplaced.

Runs:

| lesson | runs |
|---|---|
| shc, slh, pmp | TH 390 light by tap with motion; TH 1280 dark by keyboard with reduced motion; a Foundation page (CF; TF for pmp) at 390 dark by keyboard and at 1280 light by tap |
| power, em-waves | TH 390 light by tap; CF 1280 dark by keyboard with reduced motion |
| sound-waves, waves-detection (TH only) | TH 390, one theme each (dark/keyboard; light/tap) |

**Machine checks, every run:**

- zero console errors (the CORS-blocked `onrender.com/api/health` call is filtered out);
- no `undefined`, `NaN`, `{{`, `[object` or `null` text;
- no sideways scroll at 390 px (`scrollWidth == clientWidth`);
- no clickable non-button element;
- `data-theme` follows the control.

Every rail stop ticks except the Ks4Sort stops (pmp MARK, power RATE, sound SORT, waves SORT), which is the known engine limit.

**Not checked:** I did not browser-drive types-of-em-waves, sound-waves-hearing or waves-detection-exploration at 1280 light, and I did not drive power on a Foundation page at 390. My session was cut short. They were read in source.

**Prose, counted on the built page.** "Max run" is the longest stretch of hook + explainer + section lead before the next commitment. "Total" is that prose across the lesson. Reference blocks (equation, RP method, command words) are not counted, as in the pilot notes.

| lesson | max run | total |
|---|---|---|
| temperature-changes-shc | 113 | 145 |
| specific-latent-heat | 94 | 215 |
| particle-motion-pressure | 101 | 127 (CF) / 203 (TH) |
| power, em, sound, waves | all under 150 / 700 (read in source; each has a single explainer of 60–110 words before its bench) | |

Every lesson is inside both budgets.

**Particle-model siblings vs internal-energy (batch 2, live).**

- **Hooks are distinct:** sand vs sea (shc), steam burn (slh), aerosol warning (pmp), against internal-energy's boiling-pan hob.
- **Flagships are distinct:** RP heater simulation; energy ledger; gas-molecule bench with a piston. Against internal-energy's heating bench.
- **Line-ups differ from each other.**
- **One real overlap: specific-latent-heat's `s-logger` re-runs internal-energy's cooling-curve beat** (Q-SLH4).
- slh's ledger reuses the internal-energy bench's staged predict → transfer → "Next stage" mechanics with different content. That is acceptable (advisory A-SLH4).

**Cross-lesson issues to fix in one pass.**

- **Q-X1:** particle-motion-pressure and power ship a hook whose wrong options carry no correction (Q-PMP1, Q-PW1).
- **Q-X2:** two Higher r2 answers are ≥ 1000 and will be mis-marked by the ladder's parser (Q-PMP2, Q-PW2).

---

## temperature-changes-shc — QUANTITATIVE (RP14 / RP1)

1. **Laws.**
   - Strong. Phenomenon first (sand vs sea).
   - The rank-the-rises instrument is predict-gated, with animated thermometers and per-pair corrections.
   - The RP simulation is predict-gated twice (c vs 900; which temperature to record). The thermometer visibly rises after switch-off, and the pupil types c.
   - The "Δθ = final temperature" confrontation opens in three beats at the exact moment a pupil makes that error, and every pupil meets it again in `s-flaw`.
   - The reduced-motion swap works (driven).
   - Command words are taught; the RP number is route-aware (14 / 1).
   - No examiner tip exists on any route, so the omitted slot is correct.
2. **Budget.** RP simulation L, ranking M, flaw micro. Fits QUANTITATIVE.
3. **CFIFA.**
   - The source FIFA is verbatim behind "Nothing to convert".
   - The convert example differs by tier (F g→kg; H g→kg + kJ→J with a rearrangement).
   - Both attempts open with the convert decision.
   - Foundation and Higher numbers differ, and H Q2 chains E = P t. Pass.
4. **Ladder.** r1 Define (parity OK), r2 Calculate 3 marks (F 770 J, H 18.7 °C, both < 1000), r3 chain with two corrected herrings, r4 Describe 6 marks with levels. Pass.
5. **Redundant text.** One row.
6. **Built page.** Clean on all four runs. Figures use the pilot's KS4D plate and serif labels.

REQUIRED

- **Q-SHC1** · all routes · logic `offVerdictText`
  - OLD: `'The heater was hotter than the block when it switched off, so energy kept flowing into the block for over a minute. Record the highest temperature, ' + HI.lag.toFixed(1) + ' °C.'`
  - NEW: `'The heater was hotter than the block when it switched off, so energy kept flowing into the block for over a minute. Record the highest temperature.'`
  - Why: the "Process your data" line directly beneath prints `Highest temperature 45.4 °C`, so the same number appears twice in a row (seen on CF and TH).
  - Cite: no-redundant-text rule.

ADVISORY

- **A-SHC1:** there is no Key fact block (pilot anatomy; same as batch-2 A-IE1). Suggested: "ΔE = m c Δθ. Δθ is final − initial. Specific heat capacity is the energy to raise 1 kg by 1 °C."
- **A-SHC2:** the explainer gives water 4200 and aluminium 900, and the `s-race` lead repeats both two blocks later. Keep them at the point of use (the race) and drop "Aluminium’s is 900 J/kg °C." from the explainer.
- **A-SHC3:** "Run it again without lagging" switches `run` to `'bare'`. That hides the pupil's lagged c, the off-question and the comparison, so `bareText` ("even further above 900") is read without the lagged value beside it. Keep the lagged result visible.
- **A-SHC4:** once the ranking is revealed, the pupil's own order disappears and only the pair corrections remain. Consider keeping the placed slots visible (locked).
- **A-SHC5:** the graph's "no lagging" label sits on the 11–12 min crosses at 390 px.

**VERDICT: FIX** (Q-SHC1, a one-line text edit).

---

## specific-latent-heat — QUANTITATIVE

1. **Laws.**
   - Phenomenon first (steam vs boiling-water burn).
   - The ledger is predict-gated: an energy ratio first, then an equation choice at each of three stages, with particles condensing and bars growing.
   - The "constant temperature, so no energy" confrontation is three beats at stage 2.
   - The logger makes the pupil read a cooling curve, convert minutes and compute L, with named errors detected. Production is trained.
   - Reduced motion is honoured.
2. **Budget.** Ledger L, logger M. Fits.
3. **CFIFA.**
   - The source FIFA is verbatim behind "Nothing to convert".
   - Both attempts open with the convert decision, and tiers differ (H rearranges and does two-stage heating + boiling).
   - **Both convert examples are defective** (Q-SLH2, Q-SLH3).
4. **Ladder.** r1 Name (parity OK), r2 Calculate (F 835 J; H graph-reading 0.25 kg), r3 sweating chain, r4 Compare 4 marks with points. Pass.
5. **Redundant text.** See the rows.
6. **Built page.** The ledger figure clips its own title and overlaps its legend at every width (Q-SLH1). The logger graph is illegible on a phone (Q-SLH5).

REQUIRED

- **Q-SLH1** · all routes, 390 and 1280 · `ledgerSvg` title and legend
  - Defect: the plate title `energy given to the skin` runs off the right edge ("…to the skin" is cut). The legend text `condensing` runs into the `cooling` swatch.
  - Fix:
    1. Anchor the title `end` at x ≈ 630, or set it at font ≤ 22.
    2. Move the `cooling` swatch and label at least 30 units right, or stack the two legend entries.
  - Cite: brief §5 "works at 390 px"; Law 8.
- **Q-SLH2** · CH, TH · `cfExamples[1]` (Higher) Answer note
  - OLD: `Mixing kJ with MJ/kg gives 0.02 g: a thousand times too small.`
  - NEW: `Leaving E in kJ while L is in J/kg gives 0.000 02 kg (0.02 g): a thousand times too small.`
  - Why: kJ ÷ MJ/kg gives 45.2 ÷ 2.26 = 20, not 0.02 g. The 0.02 g figure only comes from mixing kJ with **J/kg**, so as written the note is false arithmetic.
  - Cite: Law 10 (feedback must correct); CFIFA amendment.
- **Q-SLH3** · CF, TF · `cfExamples[1]` (Foundation)
  - Defect: the two conversions (g→kg and kJ/kg→J/kg) cancel. The note concedes it: "Left as 250 × 334, the answer is 83 500 with no idea which unit it is in". So the example teaches that converting changes nothing.
  - NEW: head `Calculate the energy needed to melt 250 g of ice at 0 °C. (Lf = 334 000 J/kg)`; Convert `250 g ÷ 1000 = 0.25 kg` (note `L is in joules per kilogram, so the mass goes in kilograms.`); Insert and Fine-tune unchanged; Answer note `Left in grams, 250 × 334 000 = 83 500 000 J: a thousand times too big.`
  - Cite: architecture CFIFA amendment (a convert example must show why the conversion matters).
- **Q-SLH4** · all routes · `s-logger` + the second `.ks3-explainer` (cross-lesson duplication with internal-energy, live)
  - Defect, three overlaps with internal-energy:
    - The explainer sentence `Run it backwards on a cooling graph, and the flat sections are where the substance condenses or freezes, giving energy out.` restates internal-energy's `Cooling runs the heating curve backwards… the flat sections are where the substance condenses or freezes.`
    - The eyebrow `Read the cooling curve` is identical to internal-energy's `s-cool`.
    - Logger step 1 ("Determine · The melting point of Y") is internal-energy's `s-cool` and r2-part-1 demand again.
  - Rainford teaches the two lessons back to back.
  - NEW:
    - Delete that explainer sentence.
    - Eyebrow `Energy from a flat section`.
    - Replace `steps[0]` with `Determine · Which section of the graph does E = m L describe?`, options `['A to B', 'B to C', 'C to D']`, `truth: 1`, replies `['Sloping: Y is a liquid cooling, so that is m c Δθ.', '', 'Sloping: solid Y is cooling, so that is m c Δθ.']`, right `B to C: the flat section, where Y freezes at constant temperature.`
    - Keep step 2 (duration) and the calculation.
  - Cite: architecture "two lessons… identical… only because the content needs it"; batch-2 Q-D1 precedent.
- **Q-SLH5** · all routes, 390 px · `curve()` (logger, and r2-H figure)
  - Defect: the axis tick numbers (0–100 °C, 0–12 min) render at about 7 px on a phone. Both Determine steps depend on reading 50 °C, 3 and 10 minutes.
  - Fix: tick labels ≥ 24 in the 640 plate; label every 20 °C and every 2 min only.
  - Cite: brief §5; batch-2 Q-EP4 (labels ≥ 26 in the 640 plate).

ADVISORY

- **A-SLH1 (for the science examiner / commander):** the stage-2 confrontation says "the bonds between them form". Batch-2 internal-energy (live, same topic) was re-cut to "forces between particles" by its examiner (DEPARTURES, internal-energy theory 1/3). The batch-3 examination accepts "bonds". The two adjacent lessons should use one wording.
- **A-SLH2:** the r2-H prompt says "Calculate the mass of Z, in kilograms", which hands over the unit mark. Drop "in kilograms".
- **A-SLH3:** `hookReveal` ends "The ledger below counts both.", a signpost with no information. Cut it.
- **A-SLH4:** the ledger reuses the internal-energy bench's staged skeleton. The content differs, so this is acceptable. Noted for the family review.
- **A-SLH5:** there is no Key fact block.

**VERDICT: FIX** (Q-SLH1–5; Q-SLH4 is structural, Q-SLH2 is an arithmetic error on the page).

---

## particle-motion-pressure — MODEL (Combined 6.3.3.1; Triple + 4.3.3.2, HT 4.3.3.3)

1. **Laws.**
   - Phenomenon first (the aerosol warning).
   - The gas bench animates sixteen molecules, a gauge and ×-factor bars, predict-gated at both stages.
   - "Molecules get bigger" and "they bump each other more" are each confronted in three beats at the moment of the wrong pick.
   - The examiner-marking sort is a good production-adjacent task, not solvable by word shape.
   - The Triple piston bench (Boyle) and the TH fast-push stage (work done raises temperature) are predict-gated, and route layers render correctly.
   - The Key fact block is present.
   - **But the hook's wrong options get no correction** (Q-PMP1).
2. **Budget.**
   - Combined: bench L, examiner sort M.
   - Triple: + piston M.
   - Fits MODEL.
3. **CFIFA (Triple only, as the spec requires).**
   - The source Boyle's-law FIFA is verbatim behind "Nothing to convert".
   - The convert examples are Pa↔kPa (F) and Pa↔kPa with a cm³→m³ answer (H). Both attempts open with the convert decision, and tiers differ. Pass.
4. **Ladder.**
   - Rungs are route-aware. CF/CH r2 is a data Predict, legitimately, since there is no calculation in 6.3.3.1. TF r2 is 250 kPa.
   - **TH r2 is 360 000 Pa** (Q-PMP2).
   - r4: 6-mark levels on TH; 4-mark points elsewhere.
5. **Redundant text.** No required rows.
6. **Built page.**
   - Clean on all four runs.
   - On TH, the stage-3 verdict and bars ("Compared with the gas at 60 cm³") stay on screen under the stage-4 figure after the fast push (A-PMP1).

REQUIRED

- **Q-PMP1 (Q-X1)** · all routes · `hookOptions`
  - OLD: all four `reply: ''`.
  - NEW:
    - [0] `'Molecules do not change size when they are heated. They move faster.'`
    - [1] `''` (the key)
    - [2] `'Even a can holding only air would burst. The danger is the push of the hot gas.'`
    - [3] `'The push of the gas does not stay normal: it grows as the gas heats up.'`
  - Why: driven at 390 px, picking A ("particles swell…") shows "Locked in." and the reveal only. The pupil is never told their idea was wrong; the bench confronts it only if they pick "bigger" there too. C and D are never corrected anywhere.
  - Cite: Law 10 (every distractor carries feedback that corrects it); the pilot's hooks reply on every distractor.
- **Q-PMP2 (Q-X2)** · TH · `rungs.r2`
  - Defect: answer 360 000 Pa. The ladder parses "360,000" / "360 000" as 360, so a correct pupil is marked wrong.
  - NEW:
    - prompt `A balloon holds 0.0090 m³ of air at 100 kPa. It is squeezed slowly, at constant temperature, until its volume is 2500 cm³. Calculate the new pressure in kPa. Work it on paper, then choose the conversion and give the answer and unit.`
    - convOptions `['Nothing to convert', 'Convert 2500 cm³ to m³: divide by 1 000 000', 'Convert 2500 cm³ to m³: multiply by 1 000 000']`, convAnswer 1
    - answer 360, tol 1, unit `kPa`, units `['kPa', 'Pa', 'm³', 'N']`
    - model `['C · 2500 cm³ ÷ 1 000 000 = 0.0025 m³', 'F · p₁V₁ = p₂V₂', 'I · 100 × 0.0090 = p₂ × 0.0025', 'F · p₂ = 0.90 ÷ 0.0025 = 360', 'A · p₂ = 360 kPa']`
  - Cite: known engine limit (commander brief); CFIFA amendment (Apply rung converts).

ADVISORY

- **A-PMP1:** on TH, hide or dim the stage-3 verdict and bars once stage 4 runs. As it stands, "The temperature has not changed" sits under a figure where it has.
- **A-PMP2:** at stage 2, a pick of "More bumps into each other…" shows "Watch what happened instead." with no text (the confrontation follows). Give it a short line, or drop the word line when the confrontation opens.
- **A-PMP3:** the CF/CH page links "View the full equation sheet" but has no equation on that route.

**VERDICT: FIX** (Q-PMP1, Q-PMP2).

---

## power — QUANTITATIVE

1. **Laws.**
   - Phenomenon first (two kettles, same energy).
   - The lift test has three predict-gated races with animated crates and readouts. Race 3 traps "minutes left in" and confronts it in three beats.
   - The power-is-not-force flaw has corrected distractors at parity.
   - The rate sort makes the pupil compute P for eight cards. It cannot be solved by unit shape, and the done-note says so.
   - The Key fact block is present; command words are taught.
   - **But the hook's wrong options get no correction** (Q-PW1).
2. **Budget.** Lift bench L, rate sort M, flaw micro. Fits.
3. **CFIFA.**
   - The source stair-climb FIFA is verbatim behind "Nothing to convert".
   - There is a second nothing-to-convert example (H: rearranged W = P t).
   - Convert examples: F min→s; H kW→W and kJ→J for t.
   - Attempts open with the convert decision, and tiers differ. Pass.
4. **Ladder.** r1 Define (parity OK), r3 chain, r4 Describe 4 marks with points. F r2 is 600 W. **H r2 is 180 000 J** (Q-PW2).
5. **Redundant text.** No required rows.
6. **Built page.** Clean on TH 390 light by tap and CF 1280 dark by keyboard in reduced motion.

REQUIRED

- **Q-PW1 (Q-X1)** · all routes · `hookOptions`
  - OLD: all four `reply: ''`.
  - NEW:
    - [0] `'More watts means faster, not more: both lots of water need the same energy.'`
    - [1] `'Running longer at a lower rate ends at the same total energy.'`
    - [2] `''` (the key)
    - [3] `'The energy depends on the water and its temperature rise, which are the same for both.'`
  - Cite: Law 10; pilot hook convention.
- **Q-PW2 (Q-X2)** · CH, TH · `rungs.r2` (Higher)
  - Defect: answer 180 000 J, mis-parsed when typed with a separator.
  - NEW:
    - prompt `A 1.2 kW microwave oven runs for 2.5 minutes. Calculate the energy it transfers, in kilojoules. Work it on paper, then choose the conversion and give the answer and unit.`
    - convOptions `['Nothing to convert', 'Convert minutes to seconds: multiply by 60', 'Convert minutes to seconds: divide by 60']`, convAnswer 1
    - answer 180, tol 1, unit `kJ`, units `['kJ', 'J', 'W', 's']`
    - right `'1.2 kW × 150 s = 180 kJ: kilowatts × seconds give kilojoules.'`
    - model `['C · 2.5 min × 60 = 150 s', 'F · E = P × t', 'I · E = 1.2 × 150', 'F · E = 180', 'A · E = 180 kJ']`
  - Cite: known engine limit.

ADVISORY

- **A-PW1:** the line-up (round bench → flaw Choice → equation → CFIFA → Sort) resembles batch-2 changes-in-energy in the same topic. It is not identical (the sort sits after CFIFA, and the demands differ). Recorded for the family review.
- **A-PW2:** the race-3 `r` for "70 560 W" ("That multiplies the energy by the time") could add "and leaves the minutes as seconds", because 588 × 120 = 70 560.

**VERDICT: FIX** (Q-PW1, Q-PW2).

---

## types-of-em-waves — MODEL

1. **Laws.**
   - Phenomenon first (the phone's unseen wave).
   - The spectrum bench has the pupil order seven groups, then compare pairs on wavelength, frequency and speed, with a drawn wave strip on a fixed-point marker.
   - "Higher frequency means faster" is confronted in three beats.
   - The energy chain (`s-energy`) has corrected herrings. Hook distractors all carry corrections.
   - The Key fact block is present.
2. **Budget.** Spectrum bench L, energy chain M. Fits.
3. **CFIFA.**
   - The source has no FIFA, so all examples are authored. There is a nothing-to-convert and a convert example per tier (F MHz/kHz; H cm→m), and attempts open with the convert decision.
   - Tiers differ: F computes speed, H rearranges for f and λ.
   - F's examples and questions write speed as 300 000 000 m/s; H uses standard form. This is appropriate. Pass.
4. **Ladder.** r1 is a frozen item via `K.find` (Give), r2 is 3 marks (F 3 m; H 12.5 cm), r3 chain, r4 Describe 4 marks. Pass.
5. **Redundant text.** No required rows.
6. **Built page.** Clean on TH 390 light by tap and CF 1280 dark by keyboard.

ADVISORY

- **A-EM1:** under the spectrum figure, the paragraph "From radio waves to gamma rays, each group's wavelength is shorter than the last" restates the figure's own heading "Same speed: shorter λ, higher frequency". Trim it to "The groups join with no gaps: one continuous spectrum."
- **A-EM2:** a wrong order lists only a few placement notes (3 of 6 misplaced in my run). That is acceptable, because the reveal figure shows the full order.
- **A-EM3:** H r2 `tol: 0.55` on 12.5 cm also accepts 12 and 13. That is reasonable for rounding, but tighter than the F rung.

**VERDICT: SHIP.**

---

## sound-waves-hearing — PROCESS (Triple Higher only, 8463 4.6.1.4)

1. **Laws.**
   - Phenomenon first (the dog whistle; hook distractors corrected).
   - The air-to-ear stepper is predict-gated at every step: particles vibrate, the ear drum follows the frequency, the small bones, then five tones to classify against the 20 Hz–20 kHz range with kHz conversions.
   - "The ear drum hears the sound" is confronted in three beats.
   - The chain (build the path) and the in/out sort are a real watch-then-do pair.
2. **Budget.** Stepper L, chain M, sort M. Fits PROCESS.
3. **CFIFA.**
   - v = f λ across media, with a nothing-to-convert and a kHz convert example, and both attempts open with the convert decision.
   - The source's SONAR FIFA is deliberately used in waves-detection-exploration (4.6.1.5 content), as the notes record.
   - A single route, so there is no tier difference to make. Pass.
4. **Ladder.** r1 State (parity OK), r2 1.7 m, r3 chain, r4 Describe 4 marks. Pass.
5. **Redundant text.** No required rows.
6. **Built page.** Clean on TH 390 dark by keyboard. The PATH rail stop did not tick in my generic run only because the player could not tell the five identical "Heard / Not heard" rows apart. That is a harness artefact, not a defect (see A-SW2).

ADVISORY

- **A-SW1:** `hookReveal` ends "Below, you find out how the ear does it, and where its range ends." That is a signpost. Cut it.
- **A-SW2:** each tone row's buttons are labelled only "Heard" / "Not heard". Give each one `aria-label="15 000 Hz: heard"` (etc.) so a screen-reader user knows which tone a button answers.
- **A-SW3:** step 4's prompt states the hearing range, and r1 then asks for it. Recall of what was just taught is acceptable, but the commander may prefer the step to say "the normal range of human hearing" without the numbers. The hook reveal and the explainer already give them.

**VERDICT: SHIP.**

---

## waves-detection-exploration — INVESTIGATION (Triple Higher only, 8463 4.6.1.5)

1. **Laws.**
   - Phenomenon first (no one has seen the core; hook distractors corrected).
   - The "read the Earth" bench is four predict-gated steps on drawn ray paths with recorded/not-recorded stations: solid Earth → S shadow → P refraction → bigger core. It is the evidence skill the family names.
   - "S-waves can't pass through the core" (imprecise) and "ultrasound bounces straight back off the first thing" are each confronted in three beats.
   - The P/S/both sort has corrected items, not solvable by word shape.
   - The ultrasound scan bench is predict-gated on echo count and depth scaling.
2. **Budget.** Quake bench L, scan bench M, sort M. Fits.
3. **CFIFA.**
   - The SONAR FIFA, read from the sound-waves-hearing slug, sits verbatim behind "Nothing to convert".
   - The convert example (ms→s) and both attempts open with the convert decision. Pass.
4. **Ladder.** r1 frozen via `K.find`, r2 120 m (ms→s), r3 a 4-mark chain, r4 Explain 6 marks. Pass.
5. **Redundant text.** No required rows.
6. **Built page.** Clean on TH 390 light by tap.

ADVISORY

- **A-WD1:** at step 4 (bigger core), the earlier S paths still end at the original outer-core edge, and the 90° station still shows "S recorded". Those lines sit inside the dashed bigger core, beside the new grazing ray and its 78° tick, so the moved edge is hard to read. Dim the step-3 rays and stations when the bigger core is drawn.
- **A-WD2:** `hookReveal` ends "Below, you read them yourself." That is a signpost. Cut it.

**VERDICT: SHIP.**

---

## Verdicts

| lesson | verdict |
|---|---|
| temperature-changes-shc | **FIX**: Q-SHC1 (a one-line duplicate number) |
| specific-latent-heat | **FIX**: Q-SLH1–5 (ledger figure clipped and overlapping; a false CFIFA note; a convert example whose conversions cancel; the cooling-curve beat duplicates live internal-energy; logger graph illegible at 390 px) |
| particle-motion-pressure | **FIX**: Q-PMP1 (hook distractors uncorrected), Q-PMP2 (TH r2 answer 360 000 mis-parsed) |
| power | **FIX**: Q-PW1 (hook distractors uncorrected), Q-PW2 (H r2 answer 180 000 mis-parsed) |
| types-of-em-waves | **SHIP** |
| sound-waves-hearing | **SHIP** |
| waves-detection-exploration | **SHIP** |
