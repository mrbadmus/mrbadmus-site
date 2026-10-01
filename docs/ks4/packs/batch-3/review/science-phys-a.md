# Science review: batch 3, group phys-a

Examiner: Opus, a fresh reviewer, 1 Oct 2026. Lessons: `temperature-changes-shc`, `specific-latent-heat`, `particle-motion-pressure`, `power`.

## Evidence used

- **Spec.** The examination files' verbatim AQA text for 8463 and 8464, re-read against my own knowledge of the specifications.
- **Equation sheets.** Both June 2026 sheets were downloaded from the URLs in `ks4-lib.js` `EQ_BY_YEAR[2026]` and read in full as text (now deleted):
  - 8464/8465 prints ΔE = m c Δθ, P = E/t, P = W/t, E = P t, E = m L and Ep = m g h.
  - 8463 prints all of these, plus **p V = constant with no HT mark**.
  - Neither sheet carries any kelvin or p/T equation.
- **Sources read.** Every lesson's `.dc.html` (template and Component logic, line by line), `batch_3.py`, the served `shared/ks4-source-batch-3.js` for these four slugs, the examinations and the author's notes.
- **Built pages.** All 16 were driven in headless Chrome (light scheme, reduced motion, port 8721):
  - Each lesson's main instrument path, plus a wrong-pick path where it matters.
  - Rendered text was read for every section on every route.
  - Instrument figures were captured.
  - The only console errors were the expected localhost CORS errors on `/api/health`.
  - The server and Chrome were killed and the scratch files deleted.
- **Arithmetic.** Every number on every page was recomputed by hand, including the simulation models (SHC rig: 45.4 °C / c = 1147 lagged and 1500 unlagged; gas bench: 196 kPa, ×1.40 / ×1.40; piston: 50 kPa, and 132 kPa after the fast push). Everything checks except the item in S-1.

---

## 1. temperature-changes-shc: 8464 6.3.2.2 / 8463 4.3.2.2, RP14 / RP1

**Route-by-route.** Neither spec point has HT or physics-only content, so all four routes get the whole lesson. Only numbers and demand differ by tier.

| route | header / RP pill / key-note spec | withheld | Higher-only variants | check |
|---|---|---|---|---|
| CF | 8464 6.3.2.2 · "Required practical 14" · "RP14" | q1 (iron block, "900 J" distractor): absent ✓; bank = q2 only | — | ✓ |
| CH | same as CF | ✓ | CFIFA ex 2 (copper pan, Δθ = 40 °C), Q1/Q2 (rearrange; E = Pt chain → 962 J/kg °C), r2 (60 W × 240 s → 18.7 °C) | ✓ |
| TF | 8463 4.3.2.2 · "Required practical 1" · "RP1" | ✓ | — | ✓ |
| TH | as TF | ✓ | as CH | ✓ |

**Checked and correct.**
- Definition of c (spec wording) and units.
- Ranking: Q 46.7 > S 20 > P 10 > R 5 °C. All six pair explanations are true.
- Hook: sand is about a fifth of water's c (about 800–840 against 4200).
- RP method, variables and risks, which match 8463 §8.2.1 RP1 (AT 1, 5).
- Sim model:
  - Lag peak about 95 s after switch-off ("over a minute" ✓).
  - Δθ-as-final gives 634 ("c too small" ✓).
  - The comparison text is right: energy is lost, so Δθ is smaller and c bigger.
- Flaw reveal: 84 000 J, and 126 000 000 is 1500 × 84 000.
- All CFIFA lines and closes: 49 350 000; 0.04 °C; 63 000; 250 J and "sixty times".
- r1 distractor replies.
- r3 herrings: a larger Δθ gives a smaller c.
- r4 levels and points.
- Chips: ΔE = m c Δθ and E = P t are both on both June 2026 sheets.
- r2 answers are below 1000 (770 J; 18.7 °C), so the calc parser limit is not tripped.

**REQUIRED:** none.

**ADVISORY**
- **S-A1** · CH, TH · CFIFA H Question 2 head.
  - OLD: "A 50 W heater runs for 5.0 minutes and raises the temperature of a 1.2 kg metal block by 13 °C. Calculate the specific heat capacity of the metal."
  - NEW: "A 50 W heater runs for 5.0 minutes and raises the temperature of a 1.2 kg metal block by 13 °C. Assume all the energy heats the block. Calculate the specific heat capacity of the metal."
  - Reason: r2 H states this assumption, and this question needs it too; the page itself teaches that some energy is always lost.
- **S-A2** · all routes · `#s-rp` step 3 offers "an ammeter and a voltmeter", but no line says how E is then found.
  - Suggestion: step 5, "Record the energy supplied" → "Record the energy supplied (the joulemeter reading, or E = V × I × t)".
  - Reason: completeness of the AQA method (8463 §8.2.1).
- **S-A3** · all routes · key note line "Water c = 4200 J/kg°C (highest common)". This is frozen text and examination C4 calls it minor. Recorded for completeness; no change.

**Frozen items still served that should be withheld:** none. q1 is correctly withheld (B3-W1). q2 is correct and served on all four routes.

**For Mide:** none.

**Verdict: SCIENCE PASS.**

---

## 2. specific-latent-heat: 8464 6.3.2.3 / 8463 4.3.2.3

**Route-by-route.** The spec point has no HT or physics-only content, and no RP badge (correct: AT 5 is an opportunity only).

| route | header / key-note spec | bank | Higher-only variants | check |
|---|---|---|---|---|
| CF | 8464 6.3.2.3 | q1 (steam 0.5 kg) and q2 (sweat), both served | — | ✓ |
| CH | 8464 6.3.2.3 | same | CFIFA ex 2 (45.2 kJ, rearrange for m), Q1 (L = 395 000), Q2 (two-stage, 519 200 J), r2 heating curve of Z (m = 0.25 kg) | **S-1** |
| TF | 8463 4.3.2.3 | same | — | ✓ |
| TH | 8463 4.3.2.3 | same | as CH | **S-1** |

**Checked and correct.**
- Explainer: internal energy changes and temperature does not (spec wording); definition; fusion/vaporisation; reverse changes release energy; 334 000 / 2 260 000 J/kg.
- Ledger: 2646 J, 22 600 J, 25 246 J, ratio 9.5; equation-choice replies; the "constant temperature, no energy" confrontation.
- Cooling curve Y:
  - plateau 3–10 min, so 420 s, E = 12 600 J and L = 210 000 J/kg;
  - error codes 3500, 12 600 and 210;
  - the implied c of liquid (2250) and solid (2000) are plausible;
  - "a pure substance freezes and melts at the same temperature".
- Other arithmetic: CF CFIFA (83 500; 3 390 000; 133 600) and r2 F (835 J).
- Ladder: r1 options, r3 chain and herrings (evaporation takes energy in), r4 Compare points.
- Chips: E = m L, ΔE = m c Δθ and E = P t, all on both June 2026 sheets.
- Rendered curves are physically right: the teal trace has flats at the plateau, and the tube shows freezing.

**REQUIRED**
- **S-1** · CH, TH · CFIFA example 2 (Higher, "Convert first"), step A `note`.
  - OLD: `Mixing kJ with MJ/kg gives 0.02 g: a thousand times too small.`
  - NEW: `Converting only L gives 45.2 ÷ 2 260 000 = 0.00002 kg (0.02 g): a thousand times too small.`
  - Reason: the note's arithmetic is mis-labelled. Kilojoules with MJ/kg is 45.2 ÷ 2.26 = 20, which read as kilograms is a thousand times too **big**. The 0.02 g comes from kJ with **J/kg**. The pupil is told a false working.
  - Citation: arithmetic, CFIFA convert step.

**ADVISORY**
- **S-A4** · CF, TF · CFIFA example 2 (Foundation, 250 g ice), step A `note`.
  - OLD: `Left as 250 × 334, the answer is 83 500 with no idea which unit it is in.`
  - NEW: `Convert only the mass and you get 0.25 × 334 = 83.5: that is in kJ, not J. Convert both.`
  - Reason: g × kJ/kg is in fact J, so 250 × 334 = 83 500 J is the right answer. The current note implies a wrong outcome where there is none.
- **S-A5** · all routes · `#s-ledger` figure (`ledgerSvg`). The caption "energy given to the skin" is clipped at the right edge at 1280 px, and the legend's "condensing" runs into the "cooling" swatch. This is a legibility issue, not a science one; it is passed to the quality reviewer.
- **S-A6** · all routes · frozen bank q1 option labels: "(used L as mass)", and 168 000 J with no derivation (examination C18/C20). The keyed answer and all three explanations are correct, so it stays served. If Mide permits a DEPARTURES text fix, option 2 → "4,520,000 J — used 2 kg instead of 0.5 kg".
- **S-A7** · key note line "energy goes into PE (breaking bonds)". This is frozen. On freezing and condensing the energy is released; explainer 1 already says so. No change.

**Frozen items still served that should be withheld:** none.

**For Mide:** none.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-1).

---

## 3. particle-motion-pressure: 8464 6.3.3.1 / 8463 4.3.3.1, + 4.3.3.2 (physics only), + 4.3.3.3 (physics only, HT only)

**Route-by-route.** This is the specific brief, checked on the rendered pages and in the logic.

| check | CF | CH | TF | TH |
|---|---|---|---|---|
| Kelvin, absolute zero, "273", p ÷ T, p ∝ T taught anywhere (rendered text, key note, equation card, logic strings) | none | none | none | none |
| Key note: kelvin and absolute-zero lines filtered (`/kelvin\|Absolute zero/` matches the frozen strings "T in kelvin…" and "Absolute zero = 0 K…") | ✓ 2 lines | ✓ 2 lines | ✓ 4 lines | ✓ 4 lines |
| p V = constant: equation card, CFIFA, key-note line 4, "Calculate" command word, P3 verdict, Triple r2/r3 | absent ✓ | absent ✓ | present, badged TRIPLE ✓ | present ✓ |
| Net force at right angles; volume–pressure particle explanation (4.3.3.2) | absent ✓ | absent ✓ | present ✓ | present ✓ |
| Bicycle-pump layer: P4 stage, "warmer" thermometer, the TH r4 6-mark question, legal clause | absent ✓ | absent ✓ | absent ✓ (P4 buttons never render) | present, badged HIGHER · TRIPLE ✓ |
| Withheld q2 (27 °C → 327 °C) | absent ✓ | absent ✓ | absent ✓ | absent ✓ |
| Header / key-note spec | 8464 6.3.3.1 | 8464 6.3.3.1 | 8463 4.3.3.1–4.3.3.2 | 8463 4.3.3.1–4.3.3.3 |

- **Numbers that silently follow p/T.** The bench shows 100 → 196 kPa for 20 → 300 °C. The Combined r2 data tables (92/99/105/112 kPa and 95/105/109 kPa) were generated from p ∝ (θ + 273).
  - In every case the pupil predicts by **extending the linear trend in °C**: "about 7 kPa per 20 °C" → 119 kPa, and "about 1 kPa per 3 °C" → 126 kPa. Both are correct predictions from the data.
  - Kelvin is never needed or mentioned.
  - The CH part (a) asks only whether p is proportional to the temperature **in °C**. The answer is "no, it would not be zero at 0 °C", which is a data/maths-skills judgement, not the p/T law.
  - This is acceptable under the brief.
- **pV tier.** pV is taught as Foundation-tier Triple content (TF and TH), never badged Higher. That is correct: 4.3.3.2 has no HT mark, and the 8463 sheet prints it unmarked.

**Checked and correct.**
- Bench stage replies, including "crossing the can sooner means getting back to a wall sooner".
- Both confrontations: molecules do not get bigger; molecule–molecule collisions do not push on the walls.
- Wall-hit bars ×1.4 / ×1.4 (√(573/293) = 1.40, product 1.96).
- Examiner sort: all 8 rulings match AQA credit (KE, speed, more frequent wall hits, more force per hit).
- P3: the halving explanation.
- P4: work done by the moving piston raises internal energy and so temperature; friction is not the reason; the gauge reads 132 kPa, above the earlier 100 kPa at 60 cm³.
- CFIFA:
  - TF: 600, 400, 10 cm³, 80 kPa, 4.0 m³ and their closes;
  - TH: 1.0 m³, 25 cm³ = 2.5 × 10⁻⁵ m³, 1.2 m³, 30 cm³; close 0.03 cm³ ✓.
- Ladder: r1; r2 TF (250 kPa); r3 cooling-tyre and expansion chains with herrings; r4 4-mark points; TH 6-mark levels and rejects.

**REQUIRED**
- **S-2** · TH · `rungs.r2` (Triple Higher calc rung).
  - Defect: `answer: 360000`. The ladder's calc rung parses with `parseFloat(s.replace(',', '.'))`, so a pupil who types "360 000" or "360,000" is read as 360 and marked wrong. The prompt does not ask for plain digits. This is the known engine limit the brief names: "a rung-2 answer of 1000 or more is a defect unless the prompt makes plain-digit entry obvious".
  - Fix, either of:
    - **(a)** Append to the prompt: OLD `…Calculate the new pressure in pascals. Work it on paper, then choose the conversion and give the answer and unit.` → NEW `…Calculate the new pressure in pascals. Work it on paper, then choose the conversion and give the answer and unit. Type the number as digits only, with no spaces or commas.`
    - **(b)** Keep a conversion but bring the answer under 1000. Make p₁ = "1.0 × 10⁵ Pa" and ask for "the new pressure in kilopascals". Set `convOptions: ['Nothing to convert', 'Convert 1.0 × 10⁵ Pa to 100 kPa; the cm³ can stay', 'Convert both volumes to m³; the Pa can stay']`, `convAnswer: 1`, `answer: 360`, `tol: 1`, `unit: 'kPa'`. Update the `right`, `wrong` and `model` lines to match: 100 × 90 = p₂ × 25, so p₂ = 360 kPa.
  - Citation: review_common_b3 known engine limits; `Ks4Ladder.dc.html` line 208.

**ADVISORY**
- **S-A8** · TF, TH · key note line 04 "Boyle's Law: pV = constant." This is frozen text, shown verbatim. "Boyle's law" is not an AQA term, and the line omits "fixed mass, constant temperature" (examination C8/C9). The equation card states the conditions, so no change is needed. A further option is to filter it like the kelvin lines, but the frozen line is not wrong.
- **S-A9** · TF, TH · Triple explainer: "…for the gas to stay at the same temperature: its molecules keep the same speeds." → "…its molecules keep the same average speed." Reason: individual speeds still change in collisions. Precision only.
- **S-A10** · TH · CFIFA H Question 1 ("A gas cylinder holds 0.050 m³ of gas at 2400 kPa… Calculate the volume the gas fills at 100 kPa."). 1.2 m³ is the total volume at 100 kPa, cylinder included; the balloon itself gets 1.15 m³. This is the conventional GCSE idealisation and the wording ("the volume the gas fills") is defensible. Optional: "Calculate the volume the gas would occupy at 100 kPa."

**Frozen items still served that should be withheld:** none. q2 is withheld on all four routes (B3-W8). q1 (tyre) is base and correct on all four. The `higher` field and the two non-spec `equations` lines are not rendered.

**For Mide:** none. The spec text settles every route question here.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-2: an engine-limit defect on the TH rung; the science on all four routes is right).

---

## 4. power: 8464 6.1.1.4 / 8463 4.1.1.4

**Route-by-route.** The spec point has no HT and no physics-only content. Every route gets the whole lesson; tiers differ in numbers.

| route | header / key-note spec | bank | Higher-only variants | check |
|---|---|---|---|---|
| CF | 8464 6.1.1.4 | q1 (2000 W, 3 min) and q2 (two students), both served | — | ✓ |
| CH | 8464 6.1.1.4 | same | CFIFA ex 2 (W = Pt, 60 000 J), ex 3 (kW and kJ, t = 150 s), Q1 (Ep then t = 29.4 s), Q2 (MJ, min → 1.5 kW), r2 (1.2 kW, 2.5 min) | **S-3** |
| TF | 8463 4.1.1.4 | same | — | ✓ |
| TH | 8463 4.1.1.4 | same | as CH | **S-3** |

**Checked and correct.**
- Definition: spec wording; 1 W = 1 J/s.
- Hook: the same energy from each kettle; legal line says all of it goes to the water.
- Lift races: 588 J; 147 / 73.5 W; C has twice A's power; winch 4.9 W. The distractors are exactly what their labels say (294 = 588 ÷ 2; 70 560 = 588 × 120; 0.20 = 120 ÷ 588). Every reply is true.
- Flaw ("power is not force") and its reveal.
- CFIFA: every line and close (18 000, 0.15 s / 150 000 s, 58 800 J, 0.09).
- Rate sort: all 8 cards (1200, 30 000, 500, 1200, 300, 18 000, 150, about 6700 W) are in the right bins.
- Ladder: r1; r3 chain and herrings; r4 stair-climb method, using vertical height and weight = m g.
- Chips: P = E/t and P = W/t are on both June 2026 sheets. The "label by the sheet the page links to" ruling applies.

**REQUIRED**
- **S-3** · CH, TH · `rungs.r2` (Higher calc rung).
  - Defect: `answer: 180000`. This is the same engine limit as S-2: "180 000" or "180,000" parses as 180 and is marked wrong.
  - Fix, either of:
    - **(a)** OLD prompt `…Calculate the energy it transfers. Work it on paper, then choose the conversion and give the answer and unit.` → NEW `…Calculate the energy it transfers. Work it on paper, then choose the conversion and give the answer and unit. Type the number as digits only, with no spaces or commas.`
    - **(b)** Ask for the time instead. "A 1.2 kW microwave oven transfers 180 kJ of energy. Calculate how long it is used for, in seconds." Set `convOptions` as now, `convAnswer: 1` ("Convert kW to W (× 1000) and kJ to J (× 1000)"), `answer: 150`, `tol: 1`, `unit: 's'`, and update the model lines.
  - Citation: review_common_b3 known engine limits; `Ks4Ladder.dc.html` line 208.

**ADVISORY**
- **S-A11** · CH, TH · Q1 uses Ep = m g h, but the equation block shows only P = E/t and P = W/t. Ep = m g h is on both June 2026 sheets. Optional: a third card, "On the sheet · Ep = m g h · gravitational potential energy (J) = mass (kg) × g (N/kg) × height (m)", or a pointer in the explainer. Not a science error.

**Frozen items still served that should be withheld:** none. Both bank items are correct on all routes.

**For Mide:** none. The spec-recall versus June 2026 sheet question for these equations is already settled by the pilot's resistors-C9 ruling.

**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-3: an engine-limit defect on the Higher rung).

---

## Summary

| lesson | REQUIRED | ADVISORY | verdict |
|---|---|---|---|
| temperature-changes-shc | — | S-A1, S-A2, S-A3 | **SCIENCE PASS** |
| specific-latent-heat | S-1 | S-A4 – S-A7 | **SCIENCE PASS AFTER REQUIRED CHANGES** |
| particle-motion-pressure | S-2 | S-A8 – S-A10 | **SCIENCE PASS AFTER REQUIRED CHANGES** |
| power | S-3 | S-A11 | **SCIENCE PASS AFTER REQUIRED CHANGES** |

---

## Round 2: commit 2ddea6225 (feat/ks4-batches)

**Method.** I read the source diffs `d80d3d4be → 2ddea6225` for all four lessons, and grepped the built pages (they are current) for each changed string.
- The browser was not re-driven. Every change is copy, numbers or a logic constant, so reading them is enough.
- On the PMP TH page, "kelvin" still appears once. It is the key-note filter regex in the logic, not text shown to pupils.

### REQUIRED rows

| row | status | check |
|---|---|---|
| **S-1** (SLH H, convert-example note) | **Closed.** | It now reads "Converting only L gives 45.2 ÷ 2 260 000 = 0.00002 kg (0.02 g): a thousand times too small." The arithmetic and the label are both right. |
| **S-2** (PMP TH rung 2) | **Closed.** | The rung now starts at 0.0090 m³, 100 kPa, and ends at 2500 cm³ at constant temperature.<br>• Arithmetic: 2500 cm³ ÷ 10⁶ = 0.0025 m³, so p₂ = 0.90 ÷ 0.0025 = **360 kPa** ✓.<br>• Answer 360, tolerance 1, unit kPa: below 1000, so the parser limit is cleared.<br>• Conversion key ("divide by 1 000 000") ✓; the model, right and wrong lines all agree.<br>• The rung is pV, so it stays Triple only.<br>• Advisory: converting V₁ to 9000 cm³ instead is equally valid, and that pupil can still pick the keyed option. No change needed. |
| **S-3** (power H rung 2) | **Closed.** | The rung is now 1.2 kW × 150 s = **180 kJ**.<br>• kW × s = kJ ✓.<br>• Conversion key "minutes to seconds: × 60" ✓.<br>• Answer 180, tolerance 1, unit kJ; below 1000.<br>• Model and right/wrong lines are correct. |

### Changed pieces, science-checked

**temperature-changes-shc**
- RP step 5 now reads "Record the energy supplied (the joulemeter reading, or E = V × I × t)…" ✓. This closes S-A2.
- New key fact: "ΔE = m c Δθ, with Δθ = final − initial. Specific heat capacity is the energy needed to raise the temperature of 1 kg by 1 °C." ✓. The definition uses the spec's wording. Δθ = final − initial is the same convention as the frozen key note; the `#s-flaw` reveal and F Q2 cover cooling.
- CFIFA H Q2 now says "Assume all the energy heats the block." ✓ This closes S-A1.
- Aluminium's 900 J/kg °C was removed from the explainer. It is still given in the ranking lead and the sim gate. ✓
- The sim's "Your lagged run" heading, the moved graph labels and the unlagged-path gating change no science. The off-verdict no longer names 45.4 °C, but "Process your data" still states it. ✓

**specific-latent-heat**
- Foundation convert example now gives Lf = 334 000 J/kg, so only the mass converts. Note: "Left in grams, 250 × 334 000 = 83 500 000 J: a thousand times too big." ✓ This closes S-A4.
- New logger step: "Which section of the graph does E = m L describe?" The key is B to C, where Y freezes at constant temperature ✓. The A–B and C–D replies say liquid cooling and solid cooling, so m c Δθ ✓.
  - The freezing-time step (7 min) and the L calculation (210 000 J/kg) are unchanged. The cooling graph is still interpreted quantitatively, so the spec's "interpret heating and cooling graphs" is still met.
- New key fact ✓. The spec definition of specific latent heat is verbatim in sense, and the rule for choosing an equation is correct.
- Confrontation now reads "come together and are held by the forces between them, which releases energy" ✓. That is AQA-acceptable language.
- Explainer 2 lost its cooling-graph sentence. The explainer's "Freezing and condensing give the same energy back" covers the release of energy. ✓
- H rung 2 dropped "in kilograms". The unit buttons still require kg ✓.
- Ledger caption and legend moved inside the figure. This closes S-A5. Layout only.

**particle-motion-pressure**
- New hook replies:
  - "Molecules do not change size when they are heated." ✓
  - "Even a can holding only air would burst. The danger is the push of the hot gas." ✓
  - "The metal is not what changes most: the gas pushing on it is." ✓
  - The reveal is unchanged in substance.
- "Same average speed" ✓. This closes S-A9.
- CFIFA H Q1 now says "would occupy" ✓. This closes S-A10.
- Verdict and bar visibility gating changed. No text changed.
- The round-1 route checks still hold:
  - kelvin, absolute zero and p/T are not taught;
  - pV appears on TF and TH only;
  - the bicycle-pump layer appears on TH only;
  - q2 is withheld.
- S-A8 (frozen "Boyle's Law" key-note line) is unchanged. It is acceptable as frozen text.

**power**
- New card "On the sheet · Ep = m g h": gravitational potential energy (J) = mass (kg) × gravitational field strength (N/kg) × height (m). Ep = m g h is printed on both June 2026 sheets ✓. This closes S-A11.
- New hook replies:
  - "More watts means faster, not more." ✓
  - "Running longer at a lower rate ends at the same total energy." ✓
  - "The times only say how fast the energy went in, not how much." ✓
  - The reveal is unchanged in substance.

### Final verdicts, round 2

| lesson | verdict |
|---|---|
| temperature-changes-shc | **SCIENCE PASS** |
| specific-latent-heat | **SCIENCE PASS** (S-1 closed) |
| particle-motion-pressure | **SCIENCE PASS** (S-2 closed) |
| power | **SCIENCE PASS** (S-3 closed) |

No new REQUIRED rows. Nothing for Mide.
