# Science review — batch 2, group `bio-phys`

Lessons: `decomposition`, `changes-in-energy`, `internal-energy`, `lenses`.
Reviewer: fresh AQA examiner (Opus), 1 Oct 2026. I wrote none of these lessons.

**What I checked.** For each lesson I read the authored source (`ks4_lessons/authored/batch-2/<slug>.dc.html`: the template and all of the Component logic, meaning every verdict, reply, `why`, rung, level and marking point), the frozen route data in `shared/ks4-source-batch-2.js`, the records and withholds in `ks4_lessons/batch_2.py`, and the source examination and author's notes. I then served `mrbadmus_site/` on port 8712 and loaded all 14 built pages (4 + 4 + 4 + 2) in headless Chrome (light scheme forced). I dumped each page's visible text route by route and diffed the routes. I drove these instruments end to end and inspected screenshots:
- the lens bench (all 7 set-ups), the ray constructor, the eye figure and the focus figure;
- the heating bench (all 4 stages) and the cooling curve;
- the store bench (all 4 changes).

There were no console errors apart from the expected CORS-blocked `/api/health`.

**Spec sources.** These were downloaded from AQA and read as text, then deleted:
- AQA-8463-SP-2016 (v1.1), including Appendix A;
- AQA-8464-SP-2016 (v1.1);
- AQA-8461-SP-2016 (v1.0);
- the two June 2026 equation sheets that `KS4.EQ_BY_YEAR[2026]` links to, `AQA-8464-8465-FS-INS-2025` and `AQA-8463-FS-INS-2025`. Both are headed "FOR USE IN JUNE 2026 ONLY".

---

## Ruling requested: Ee = ½ke², and the sheet status of Ek, Ep and Ee

**1. Ee = ½ k e² is BASE on all four routes. It is not HT.**
- The 8463 4.1.1.2 and 8464 6.1.1.2 text is identical: "Students should be able to apply this equation which is given on the Physics equation sheet". The section has no HT marker.
- 8463 4.5.3 repeats it with no HT marker: "calculate work done in stretching (or compressing) a spring (up to the limit of proportionality) using the equation Ee = ½ke² … given on the Physics equation sheet".
- 8463 Appendix A puts Ee on the "select and apply from the sheet" list as equation 4. It has **no** HT flag, while equations 1, 3, 8, 10 and 11 on that same list do.
- On the June 2026 sheets, the key reads "HT = Higher Tier only equations".
  - The 8464/8465 sheet marks only Vp Ip = Vs Is, p = m v and F = B I l as HT.
  - The 8463 sheet marks only p = hρg, p = m v, F = mΔv/Δt, F = B I l, Vp/Vs = np/ns and Vp Ip = Vs Is as HT.
  - Ee is printed unmarked on both.

So `docs/ks4/findings-for-mide.md` item 3 ("Ee = ½ke² — HT-only") is **wrong as a statement about the specification**. At most it describes how one frozen question (`ks4-forces-elasticity-h01`) is flagged. The changes-in-energy author's handling (Ee taught on CF/CH/TF/TH) is correct. I recommend correcting that findings row so it does not get applied to another lesson.

**2. The "Equation sheet" chip on all three cards is correct for June 2026.**
- In the specification, Ek = ½mv² and Ep = mgh are "recall and apply". They are equations 10 and 11 on the Appendix A recall list.
- However, **both** June 2026 sheets print Ek, Ee and Ep on page 1 ("kinetic energy = 0.5 × mass × (speed)²", "elastic potential energy = 0.5 × spring constant × (extension)²", "gravitational potential energy = mass × gravitational field strength × height").

The sheet is the operative exam document for this cohort. The pilot already ruled exactly this case: `resistors-C9` gives V = I R, a recall equation in Appendix A, the Equation-sheet chip because it is on the 2026 sheets. This is not a conflict between AQA sources that needs Mide. A 2026 concession sheet and the base spec answer different questions, and precedent decides the page. A note for the record: once AQA stops issuing the full sheet, these two chips must go back to "Learn it". `KS4.EQ_YEAR` is the switch, and the author flagged it. See advisory A-1.

---

## changes-in-energy — 8464 6.1.1.2 / 8463 4.1.1.2 (base; no HT, no physics-only)

**Route check**

| route | what renders | verdict |
|---|---|---|
| CF | All base content. CFIFA F set (Ee convert 15 cm → 0.45 J; Ep 470 J; Ek 600 g → 67.5 J). r2 F (300 g, 2.4 J). Eyebrow and key-note spec read 8464 6.1.1.2. The sheet link is the 8464/8465 PDF. | OK |
| CH | Same as CF, with the H set: Ep→Ek chain v = 7.9 m/s; v = 20 m/s; k = 500 N/m; r2 90 kJ → 15 m/s. | OK |
| TF | Same as CF. Eyebrow 8463 4.1.1.2. The sheet link is the 8463 PDF. | OK |
| TH | Same as CH, with the 8463 labels. | OK |

There are no route tags, and none are needed. Tier differences are numbers and rearranging only, and Foundation loses no base content.

**Rechecked (all correct):**
- hook (50 000 → 200 000 J);
- bench, all four changes: 29.4/58.8 J, 0.25/1.0 J, 140/1260 J, 1260/2520 J. Bar ratios and every option reply are true. The squaring panel triggers on the unsquared pick only.
- units sort, all 8 bins;
- the equation cards and their rearrangements. "Valid up to the limit of proportionality" corrects the frozen "elastic limit" (C10).
- spot-the-flaw: 588 J, 2.04 kg, 60 J, and the 600 J reply;
- every CFIFA line and close note: 7840 J, 4500 J (×10 000), 0.05 N/m, 67 500 J;
- r1 (frozen q2, 2 J);
- r2 (tolerances bracket 2.4 and 15);
- r3 links and both herrings (the √2 speed point is right).

**Diagrams.** The store bench drawings are physically sound. The extension is measured from the unstretched end, and each pair of bars is to scale.

**REQUIRED**

| # | route(s) | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-1 | CF CH TF TH | `batch_2.py`, changes-in-energy record (frozen q1 is served in the practice set, `K.bank`) | Add `withhold=[W("An 800 kg car travels at 20 m/s", "B2-W<n>")]`. Alternatively, Mide rules a generated-copy edit as follows. Option 4 label: "16,000 J — used speed not speed squared: ½ × 800 × 40" → "16,000 J — doubled the speed instead of squaring it: ½ × 800 × 40". wx3 → "16,000 comes from ½ × 800 × 40: 40 is 20 × 2. Squaring means 20 × 20 = 400." wx1 → "½ × 800 × 20 = 8000 is what you get if you forget to square: 20² = 400 first." | The distractor label is visible before answering, and it states a false diagnosis: 40 is not the speed, and "used speed" is what option 2 (8000 J) did. The wx3 explanation ("if v = √40") misnames the error, and wx1 reads as an instruction to compute ½ × 800 × 20. This is the same bar as B2-W7 (feedback that contradicts itself), which was withheld. If withheld, the bank keeps q2 (k = 400 N/m), which is clean and is already r1. | examination C21, C23, C24 |
| S-2 | all | logic `rungs.r4.points[5]` | OLD: "Some energy is dissipated to the thermal store of the surroundings by air resistance, so the total stays the same." → NEW: "Some energy is dissipated to the thermal store of the surroundings by air resistance. The total energy stays the same." | This is a mark point that models a false causal link. Energy is conserved whether or not any of it is dissipated; the dissipation is not the reason. | 8464 6.1.2.1 / 8463 4.1.2.1 (conservation of energy) |

**ADVISORY**
- **A-1.** The Ek and Ep cards. The chip is right for June 2026 (see the ruling above). Consider adding one line, "Spec: recall this equation", under each card, so pupils also learn the two equations AQA expects them to know. This also makes the later `EQ_YEAR` switch to "Learn it" painless. Not required.
- **A-2.** Key-note line 6, "All three equations need mass in kg and distance in m", is frozen and imprecise: Ee contains no mass (examination C14). It is harmless, but worth a DEPARTURES ruling if Mide edits key notes: "Mass in kg, heights and extensions in m."
- **A-3.** r4 point 4: "The cord slows her down, so her kinetic store decreases…". Strictly, she keeps speeding up after the cord starts to stretch, until the cord's pull equals her weight. AQA marking accepts the simplified sequence, so this is optional. The precise version would be: "Once the cord pulls up harder than her weight, she slows down: her kinetic store decreases while the elastic store keeps increasing."

**Frozen items still served that should be withheld:** q1 (S-1).
**For Mide:** none. Item 3 of `findings-for-mide.md` needs correcting; see the ruling above.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-1, S-2).

---

## internal-energy — 8464 6.3.2.1 / 8463 4.3.2.1 (base), with 4.3.2.3 and 4.3.3.1 as support

**Route check:** CF, CH, TF and TH render identical bodies. The only differences are the eyebrow and key-note spec number (8464 6.3.2.1 against 8463 4.3.2.1) and the practice-set label. There is no HT or physics-only content, and that is correct. No CFIFA or equation block is needed, because there is no calculation. ΔE = mcΔθ and E = mL are named as "on the equation sheet", and both are on both 2026 sheets.

**Rechecked (correct):**
- hook and reveal;
- all four stage `why` lines and every REPLY entry;
- the confront panel ("Temperature follows the particles' average kinetic energy");
- all 5 compare items and the done-note;
- the cooling curve (A–F) and all 5 section placements;
- r1 (frozen q1, keyed change of state);
- r2: 20 °C melting point, liquid at 50 °C, average KE constant on D–E;
- r3 links and herrings;
- r4 levels and points 1–6.

**REQUIRED**

| # | route(s) | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-3 | all | logic `thinkOptions[0].text` (the keyed answer to the iceberg spot-the-flaw) | OLD: "Temperature is linked to the average energy of one particle. Internal energy adds up every particle, and the iceberg has vastly more." → NEW: "Temperature is linked to the average kinetic energy of the particles. Internal energy adds up the kinetic and potential energy of every particle, and the iceberg has vastly more." | Temperature tracks average **kinetic** energy, not average total energy. Potential energy is part of a particle's energy and does not set the temperature: that is the whole point of the bench's flat sections. The keyed answer must not blur it. | 8463 4.3.3.1 "temperature … related to the average kinetic energy"; 4.3.2.3 |
| S-4 | all | logic `rungs.r4.reject[0]` | OLD: "“The bonds inside the water molecules break when the ice melts.” Melting separates the molecules; it does not break them." → NEW: "“The bonds inside the water molecules break when the ice melts.” Melting overcomes the forces between the molecules; the molecules themselves do not break." | For **ice → water** specifically, the molecules move *closer* together on melting (water is denser than ice), so "separates the molecules" is false for the very substance in the question. "Forces between particles overcome" is the wording the bench already uses and the wording AQA credits. | 8463 4.3.2.3; examination C4 |
| S-5 | all | logic `STAGES[].t0/t1`, `HEAT_PTS`, the heating-curve `notes`, and the unused `heatTemp()` | Currently ice warms 10 °C in 2 time units (5 °C per unit) and water warms 100 °C in 5 units (20 °C per unit), so the solid line is drawn **four times shallower** than the liquid line. NEW: STAGES t-values `[0,0.5]`, `[0.5,3]`, `[3,13]`, `[13,15]`; `HEAT_PTS = [[0,-10],[0.5,0],[3,0],[13,100],[15,100]]`; notes `{at:3, x:1.75, T:0, t:'melting'}` and `{at:15, x:14, T:100, t:'boiling'}`. Update or delete `heatTemp()` to match. The minimum acceptable fix is that the ice line is **at least as steep** as the water line. | At constant power the gradient is proportional to 1/(mc). Ice (c ≈ 2100 J/kg °C) warms about twice as fast as water (c ≈ 4200 J/kg °C), so the curve is drawn the wrong way round. The legal line excuses durations ("time axis not to scale"), but not a reversed comparison of gradients on a curve labelled with water's real temperatures. AQA asks pupils to interpret heating graphs, and gradient-vs-SHC is a standard Higher-paper question. The new values give a 2:1 ratio. | 8463 4.3.2.2, 4.3.2.3 ("interpret heating and cooling graphs") |

**ADVISORY**
- **A-4.** Key-note line 3, "Temperature = average KE per particle", is frozen. The spec says "related to". It is acceptable at GCSE; no change needed.
- **A-5.** Frozen q2 is served in the bank. wx2 ("Internal energy depends on temperature, mass AND specific heat capacity") is imprecise (examination C23), and wx3 uses "EXTENSIVE property", which is not in the spec. Neither is false enough to withhold under the B2 bar. Optional generated-copy ruling for wx2: "Internal energy depends on how many particles there are (the mass) and what they are, not on temperature alone."
- **A-6.** The frozen q1 key says "to break intermolecular bonds" while the page says "forces between particles" throughout. AQA physics mark schemes credit "bonds between particles break", so it is acceptable as served.
- **A-7.** (Not science.) The author's notes say the header keeps the equation-sheet link. The template has no link, unlike changes-in-energy and lenses. Worth the commander's eye.

**Frozen items still served that should be withheld:** none.
**For Mide:** none.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-3, S-4, S-5).

---

## lenses — 8463 4.6.2.5 (physics only; not in 8464), with spectacles from 8461 4.5.2.3 (biology only)

**Route check**

| route | what renders | verdict |
|---|---|---|
| TF | Everything except the H numbers. Ray diagrams for both lenses are taught. That is correct: 4.6.2.5 carries no HT, and the frozen `higher` field's tag was wrong. CFIFA F (2.5; 0.35; 4.0; 0.25). r2 F 0.60 "no unit". | OK |
| TH | As TF, with the H numbers (6.0 cm; 6.5; 7.5 cm; 2.4 cm; r2 3.5 mm). | OK |
| CF/CH | The lesson is not built for them, which is correct: there is no lens section in 8464. | OK |

**Rechecked (all correct):**
- Bench geometry, thin lens with v = uf/(u − f):
  - convex 30 → v 15, m 0.5;
  - 20 → 20, m 1;
  - 15 → 30, m 2;
  - 10 → parallel;
  - 6 → v −15, h 10, m 2.5;
  - concave 30 → −7.5, m 0.25;
  - concave 6 → −3.75, m 0.625.
- Every verdict (`truthOf`) and `WHY` line.
- The rays, from screenshots. The parallel ray goes through F, or appears to come from near-side F for the concave lens. The centre ray is undeviated. The F ray leaves parallel at y = −H₀f/(u − f). The virtual image is found by dashed back-extensions, and the virtual-image arrow is dashed.
- AQA lens symbols: convex has arrowheads pointing outward, concave inward.
- The focus figure (the concave rays trace back to F) and the eye figure (focus in front of the retina).
- All constructor replies and all 7 sort items.
- The spectacles text gives both causes for each defect, which matches 8461 4.5.2.3.
- The units card ("no unit; same unit mm or cm").
- The r3 chain and r4 compare points.

**REQUIRED**

| # | route(s) | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-6 | TH | logic `cfExamples[1]` (H "Convert first"), the Convert-step note (6th argument of `ST`) | OLD: "Both heights must be in the same unit. Unconverted, 2.6 ÷ 4.0 gives 0.65: a diminished image, which a magnifying glass never makes." → NEW: "Both heights must be in the same unit. Unconverted, 2.6 ÷ 4.0 gives 0.65: a diminished image, but the wing looks bigger through the glass, not smaller." | A magnifying glass is a convex lens, and it **does** form diminished images: the lesson's own hook (the window at arm's length) and the bench at 30 cm both show it. As written, this note teaches the misconception the bench confronts ("convex lenses always magnify"). | 8463 4.6.2.5 ("the image produced by a convex lens can be either real or virtual"); examination §5 misconception list |

**ADVISORY**
- **A-8.** Explainer 1: "one parallel to the axis, which leaves through F". This follows the concave sentence, so a pupil may apply it to both lenses. Suggest: "…one parallel to the axis, which a convex lens bends through F (a concave lens bends it as if it came from F on the near side)…".
- **A-9.** In `eyeOptions[2]`, the reply "The eye cannot push the focus back far enough for distant objects" is loose. In 8461 terms: "Even with the ciliary muscles relaxed and the lens pulled thin, the eye still focuses distant light in front of the retina."
- **A-10.** Frozen q2 wx3 ("typically worsens over time") is imprecise but harmless (examination C31). Keep it.
- **A-11.** The bench readout shows "magnification = 2.5 ÷ 4.0 = 0.63" for 0.625. That is fine to 2 s.f. A cosmetic point: at 6 cm the "object" label overlaps the rays.

**Frozen items still served that should be withheld:** none. q1 and q2 are both correct on TF and TH. q2 is biology content (8461 4.5.2.3), but it is Triple on both routes.
**For Mide:** none.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-6).

---

## decomposition — 8464/8461 4.7.2.2 (base) + 8461 4.7.2.3 and RP10 (biology only)

**Route check**

| route | what renders | verdict |
|---|---|---|
| CF | Hook, explainer, "Follow the leaf" (4.7.2.2), spot-the-flaw (respiration), key fact, Combined ladder (Name / Identify / Explain chain / 4-mark Explain), key-note lines 1–4. Every `data-route="triple"` section (Triple explainer, compost, RP10, simulator, pink, equations, CFIFA) is **absent** from the rendered page. There is no RP pill, and the eyebrow reads 8464 4.7.2.2. Frozen q2 (refrigerator) is correctly withheld (B2-W6). | OK |
| CH | Identical to CF. | OK |
| TF | Everything above, plus the Triple layer badged TRIPLE: decay factors (temperature up to an optimum, water, oxygen), compost, methane and biogas, the RP10 milk/lipase/pH method, the simulator, the pink misconception, the equations, CFIFA F. Triple ladder: r1 = q2, r2 80 → 50 g in 6 weeks = 5 g/week, r3 compost holes, r4 RP10 6-mark. Key note 1–7. | OK |
| TH | As TF, with the H numbers (54 ÷ 12 = 4.5 weeks; 900 g ÷ 6 = 150 g/week; r2 84 ÷ 6 = 14 g/week). | OK |

The frozen RP7 bread/mould/respirometer text is not displayed anywhere. The RP block is correctly 8461 **RP10**, "investigate the effect of temperature on the rate of decay of fresh milk by measuring pH change", which I confirmed in the spec text. Every number is right:
- 9, 21 and 3 g/day;
- 6, 7, 4.5 and 150;
- 0.15 kg/week;
- 1/150 ≈ 0.007 s⁻¹.

The simulator's model times (430/260/150/230 s, denatured at 60 °C) give the correct U-shaped time graph with its minimum near 40 °C. The improvement key ("more temperatures between 30 and 50 °C") is right. The compost sort, all six items, is right. The method, variables and risks match the AQA handbook practical. The direction of the indicator change (pink → colourless) is right everywhere.

**REQUIRED**

| # | route(s) | where | OLD → NEW | reason | citation |
|---|---|---|---|---|---|
| S-7 | TF TH | logic `pinkOptions[0].reply` | OLD: "In ten minutes, that would barely start. The acid comes from the enzyme you added." → NEW: "In ten minutes, that would barely start. The acid comes from the fat in the milk, broken down by the lipase you added." | The enzyme is not the source of the acid. The fatty acids come from the milk's fat (the lipase's substrate). The reveal says this correctly, but this reply contradicts it, and this exact error is what the panel exists to fix. | 8461 4.2.2.1 (lipase → fatty acids + glycerol); RP10 |

**ADVISORY**
- **A-12. For Mide.** Frozen q1 ("What is the difference between decomposers and detritivores?") is served in the practice set on **all four routes**. It is correct science, but detritivores are in neither 8461 nor 8464 (I checked: no occurrence of "detritiv" or "earthworm" in either spec), and the page itself never teaches the word. On CF/CH it is the **only** practice item. The batch precedent (enzymes q4: correct but not a named factor, so kept, not a rung) says keep it. I recommend withholding it on all routes, because a pupil is being drilled on a term the lesson deliberately cut. If it is withheld, check that `Ks4QuizBank` renders an empty Combined bank sensibly.
- **A-13.** In `thinkOptions[0].reply`, "Nothing burns on a woodland floor" is overstated (forest fires happen). Suggest: "The leaves are not burning. Decay is done by living microorganisms."
- **A-14.** In `pinkReveal`, "which is why the time measures the rate of decay" is loose. The time is inversely related to the rate. Suggest: "…the sooner the pink goes, so 1 ÷ time measures the rate of decay."

**Frozen items still served that should be withheld:** possibly q1 (A-12, Mide's call). q2 is already withheld on CF/CH, as required, and I confirmed this in the build.
**For Mide:** A-12 only. There is no conflict between AQA sources: 8464 simply has no 4.7.2.3 and no decay practical.
**Verdict: SCIENCE PASS AFTER REQUIRED CHANGES** (S-7).

---

## Summary

| lesson | REQUIRED | verdict |
|---|---|---|
| changes-in-energy | S-1 (withhold frozen q1), S-2 | SCIENCE PASS AFTER REQUIRED CHANGES |
| internal-energy | S-3, S-4, S-5 | SCIENCE PASS AFTER REQUIRED CHANGES |
| lenses | S-6 | SCIENCE PASS AFTER REQUIRED CHANGES |
| decomposition | S-7 | SCIENCE PASS AFTER REQUIRED CHANGES |

The Ee ruling stands as stated: Ee is base on every route and on the sheet, and `findings-for-mide.md` item 3 is wrong about the spec. The Ek/Ep "Equation sheet" chips are correct for June 2026 under the resistors-C9 precedent.

---

## Round 2 — re-review of commit 36fd4c877

Same reviewer, same rules. For each lesson I read the source diff `fff50ef58..36fd4c877` and the "Review fixes" section of its notes file. I loaded the rebuilt pages on port 8712 (light scheme, reduced motion). I dumped the visible text for CF and TH, plus TF for lenses. I drove these, with screenshots:
- the lens ray constructor: one wrong tap and then the right tap at every step;
- the heating bench: all four stages.

There were no console errors apart from the expected `/api/health` CORS block.

### Required rows: all fixed correctly

| row | verified |
|---|---|
| S-1 | `batch_2.py` withholds "An 800 kg car travels at 20 m/s" (B2-W10). The built practice set shows 1 item (the spring) on CF and on TH. Rung 1 is still the spring item. ✓ |
| S-2 | r4 point 6 reads "…by air resistance. The total energy stays the same." A-3 was also applied: point 4 now says she slows "once the cord pulls up harder than her weight". ✓ |
| S-3 | The keyed iceberg option reads "Temperature follows the average kinetic energy per particle. Internal energy totals every particle's kinetic and potential energy; the iceberg has far more." It is correct and renders on CF. ✓ |
| S-4 | The r4 reject line reads "Melting overcomes the forces between the molecules; the molecules themselves do not break." ✓ |
| S-5 | STAGES `0–0.5 / 0.5–3 / 3–13 / 13–15`; HEAT_PTS `[[0,−10],[0.5,0],[3,0],[13,100],[15,100]]`; notes at x 1.75 and 14; `heatTemp()` deleted. On the rendered curve, ice rises at 20 °C/unit and water at 10 °C/unit, the 2:1 ratio that matches c_water ≈ 2 c_ice. ✓ |
| S-6 | The Higher convert note reads "…0.65: a diminished image, but the wing looks bigger through the glass, not smaller." ✓ |
| S-7 | The pink reply reads "The acid comes from the fat in the milk, broken down by the lipase you added." ✓ |

### New and changed science, checked

**changes-in-energy**
- Explainer: the squaring sentence was removed. The remaining text is correct.
- Bench asks were trimmed. Each round's title still states the change, so the questions remain answerable and true.
- Hook replies are now empty, and the reveal is unchanged and correct.
- The Foundation convert Insert line is `Ee = ½ × 40 × 0.15²`, and Fine-tune gives 0.0225 → 0.45 J ✓.
- The after-bar label was removed; the working line still states the value.

No new issues.

**internal-energy**
- The three distractors were lengthened. Each is still a single, clearly false misconception, and each reply is unchanged and true.
- The hook reveal is now "It stays at 100 °C, and the water boils away faster…", which is correct.
- The explainer sentence was cut. The rest is correct.
- The equation-sheet link was added to the header.

No new issues.

**lenses: the tap-on-diagram constructor.** I checked every target against thin-lens geometry (f = 10 cm, object 4 cm tall), drove it, and inspected the screenshots.

- **Step 1** (u = 25, ray 1 leaves the lens at (0, 4)):
  - F (10, 0): correct ✓.
  - 2F (20, 0): wrong ✓.
  - (25, 4) "straight on": wrong ✓.
  - Near-side F (−10, 0): wrong ✓.
  - The wrong-ray preview is drawn from the lens point to the tapped point and extended, which is right. Each reply is true.
- **Step 2** (ray 2 through the centre, from (−25, 4)):
  - (25, −4): correct ✓. This is exactly the undeviated continuation, since the direction is (25, −4).
  - F: wrong ✓.
  - The axis point (25, 0): wrong ✓.
- **Step 3**:
  - (50/3, −8/3): correct ✓. This is the true image top: v = uf/(u − f) = 16.67 cm, h = −4 × 16.67/25 = −2.67 cm, and it sits exactly on both drawn rays (seen on screen).
  - F, 2F and the ray-1 lens point are wrong, with true replies ✓.
- **Step 4** (u = 5):
  - (−10, 8): correct ✓. v = −10 cm and h = +8 cm, a virtual, upright, magnified image. The completion figure draws the dashed back-extensions meeting there and a dashed image arrow.
  - F far side: wrong ✓.
  - (32, −12) "edge": wrong ✓.
  - "No image: the rays never meet": wrong, with a true reply (that happens only at F) ✓.

Other lens changes:
- The trimmed WHY lines are still all true. The verdict boxes carry real/virtual, size and way up.
- The "No image" verdict wording is right.
- A-8 and A-9 were applied, and their wording is correct.

**decomposition**
- **New hook (all routes).** A compost heap is over 50 °C inside on a frosty day. The keyed answer, "Living things in the heap, releasing energy as they feed", is correct. Microbial (largely thermophilic) respiration releases energy and heats the heap; respiration is base (4.4.2). The reveal is correct. The sunlight reply (heap hottest in the middle, where no light reaches) and the burning reply (no ash or smoke) are true.
- **Stepper step 1** now asks where most of the carbon goes. The key "Into the air, as carbon dioxide" and its replies are correct.
- **New base sort "Air, soil, or locked away?"**:
  - leaf sugars → air ✓;
  - nitrate in droppings → soil ✓;
  - fern buried in mud before it could rot → locked away, becoming coal ✓ (decomposition prevented; fossil fuels are carbon-cycle context);
  - magnesium from a leaf → soil, as a mineral ion ✓;
  - carbon in a feeding fungus → air ✓ (it respires, and is itself decomposed);
  - nitrogen compounds in a dead mouse → soil, as mineral ions such as nitrate ✓.

  Every `why` is true and the done-note is correct. The sort cites 4.7.2.2, which is base, so it is correctly untagged. On CF/CH the Triple layer is still absent.
- **Plot**: 60 °C is now a "> 600 s" marker, not joined to the curve. That is correct handling of a result with no end point.
- The rate prompts are correct (unit s⁻¹).
- A-13 and A-14 were applied, with correct wording.

### Round 2 advisories (not blocking)
- **R2-A1 (decomposition hook):** the "warmth rising from the ground" reply says "Frozen ground is colder than the heap", but the stem only says the air is below 0 °C. Suggest: "The ground is far colder than the middle of the heap, so heat flows out of the heap, not in."
- **R2-A2 (decomposition, not science):** the explainer that follows the hook still says "every atom in the leaf ends up somewhere". With the hook now about a compost heap, "the leaf" has nothing to refer to until the stepper starts. Suggest "every atom in dead material ends up somewhere. Follow one leaf…".
- A-12 (detritivore q1 in the bank) was kept by commander ruling. I note it and do not reopen it.

### Final verdicts

| lesson | verdict |
|---|---|
| changes-in-energy | **SCIENCE PASS** |
| internal-energy | **SCIENCE PASS** |
| lenses | **SCIENCE PASS** |
| decomposition | **SCIENCE PASS** |

---

## Round 3 — commit 7c1710936 (lenses and decomposition)

**What I checked:**
- the source diff `36fd4c877..7c1710936`;
- that the branch tip (330e78396) is identical to it for both files;
- the rebuilt pages on port 8712.

On TF and TH I pressed every ring in every constructor step, in its new order, until the correct one advanced.

**Lenses: ray task.** Coordinates are unchanged except for one new target. The sort is by x, then y, which changes only the order. The positional labels from `where()` all describe their points accurately, and none gives the answer away.

| step | target (cm) | label | expected | driven |
|---|---|---|---|---|
| 1 | (−10, 0) | on the axis, at F, object's side | wrong | wrong ✓ |
| 1 | (10, 0) | on the axis, at F, far side | **correct**: the parallel ray goes through F | correct ✓ |
| 1 | (20, 0) / (25, 4) | at 2F, far side / above the axis, beyond 2F | wrong | (source) ✓ |
| 2 | (10, 0) / (25, 0) | at F / on the axis, beyond 2F | wrong | wrong ✓ |
| 2 | (25, −4) | below the axis, beyond 2F, far side | **correct**: the undeviated line from (−25, 4) through (0, 0) | correct ✓ |
| 3 | (0, 4) / (10, 0) | above the axis, at the lens / at F | wrong | wrong ✓ |
| 3 | (16.67, −2.67) | below the axis, between F and 2F, far side | **correct**: v = 16.67 cm, h = −2.67 cm | correct ✓ |
| 3 | (20, 0) | at 2F, far side | wrong | (source) ✓ |
| 4 | **(−20, 0) NEW** | on the axis, at 2F, object's side | wrong. The traced-back rays pass (−20, 12) and (−20, 16), so nothing meets there, and the feedback "Nothing meets at 2F. Trace both rays back until they cross." is true. | wrong ✓ |
| 4 | (−10, 8) | above the axis, at F, object's side | **correct**: virtual image at v = −10 cm, h = +8 cm | correct ✓ |
| 4 | (10, 0) / (32, −12) | at F / below the axis, beyond 2F | wrong | (source) ✓ |

Nearest-ring tap selection (within 40 px) cannot change which point is correct. The closest ring pair, the step-3 crossing and 2F, is about 52 plate px apart, and step 4's correct ring is about 155 px from the new 2F ring. There were no console errors on TF or TH.

**Decomposition**
- "Sugar in a leaf that has fallen and died" → air. Why: "respire the sugar, releasing its carbon as carbon dioxide" ✓.
- Nitrate in droppings → soil ✓.
- Fern buried before it could rot → locked away ✓.
- "Magnesium in a fallen leaf" → soil ✓.
- Fungus on a log → air ✓.
- Nitrogen compounds in a dead mouse → soil ✓.
- Prompt "Each one starts in a living thing." True for all six.
- Explainer "every atom in a dead leaf… Follow one fallen leaf" ✓. This resolves R2-A2.
- Hook reply "The ground under the heap is colder than its middle, so heat flows out of the heap, not in." ✓. This resolves R2-A1.
- The new text renders on CF.

No new issues.

### Final verdicts (round 3)

| lesson | verdict |
|---|---|
| lenses | **SCIENCE PASS** |
| decomposition | **SCIENCE PASS** |

(changes-in-energy and internal-energy are unchanged since round 2: **SCIENCE PASS**.)
