# Batch 2 quality review: group b (chemistry)

Reviewer: fresh Opus quality reviewer, 1 Oct 2026. Read-only except for this file.

Lessons: atoms-elements-compounds, relative-formula-mass, using-moles-calculations, concentration-of-solutions, percentage-yield, titrations, metal-hydroxides, carbonates-halides-sulfates.

## How I checked

- **The pilot bar.** I read three pilot lessons end to end, in Design's source and as built pages: metallic-bonding (MODEL), resistors-iv-required-practical (REQUIRED PRACTICAL, with CFIFA and an RP simulation) and the Ks4Ladder, Ks4Cfifa, Ks4Sort, Ks4Chain and Ks4Write blocks. I compared them against `architecture.md`, `AUTHORING-BRIEF.md` and `content_standards.md`.
- **Static pass.** 8 lessons × 2 routes (TH plus one Foundation route; for using-moles, CH because it is Higher-only) × 390 and 1280 px × light and dark (dark was forced through `mrb-theme=system` plus emulated `prefers-color-scheme`). On every page:
  - no horizontal scroll;
  - no "undefined", "NaN", "{{" or "[object";
  - zero console errors, apart from the expected CORS block on `/api/health` from localhost.
- **Prose, counted from the built pages.**

  | Lesson | Explainer words | Hook words |
  | --- | --- | --- |
  | aec | 206 | 46 |
  | rfm | 216 | 37 |
  | moles | 141 | 46 |
  | conc | 77 (+52 on TH) | 47 |
  | py | 67 (+72 on TH) | 47 |
  | tit | 0 explainer (RP block) | 62 |
  | mh | 70 | 40 |
  | chs | 86 | 45 |

  Every lesson is well inside ≤150 words before a commitment and ≤700 words of body prose.
- **Play-through.** Every activity on every lesson was played to completion twice:
  - TH at 1280 light, **keyboard only** (focus plus Enter);
  - the Foundation (or CH) page at 390 dark, **tap only** (real mouse events).

  Every lesson's flagship, mid-size activities, choices, CFIFA and all four ladder rungs reached their done state in both modes. The one exception, sorts not ticking the rail, is a shared-engine issue below.
- **Rail.** After each play-through I checked the rail's done markers.
- **Scratch.** Screenshots and harness stayed in scratch and were deleted.

## Shared finding (not a lesson defect; for the engine owner)

**S-1 · Ks4Sort never ticks its rail stop.** A sort solved to "Every card is where it belongs." leaves its rail item un-done. This happens on all six sorts here: aec `s-sort`, moles `s-sort`, conc `s-convert`, py `s-reasons`, chs `s-acid`. It also happens on the **live pilot**: `metallic-bonding` `s-sort`, driven the same way.

The lessons all wire it the pilot's way (`on-done="{{ onSort }}"` → `setState({sort:true})`), so the defect is in how the compiled runtime forwards Ks4Sort's `onDone`. It is not in any of these lessons. Fix it once in the runtime, and check it against the pilot.

---

## atoms-elements-compounds (CLASSIFY)

**Assessment**
1. **Laws.**
   - Strong phenomenon hook (sodium + chlorine → salt).
   - The flagship particle boxes are predict-gated and animated, with a reduced-motion swap.
   - Mixtures slide apart, and the FeS 1:1 tracing and bronze ringing are excellent concrete→diagram moves.
   - The diatomic and alloy misconceptions are confronted at the box where they are born.
   - Balancing is taught watch-then-do (three worked steps, then three equations), with the H₂O₂ spot-the-flaw just before it.
   - Production is trained (balancing; the r4 write).
   - Two Law-10 problems: the sort can be solved by label shape (Q-3), and rung 1 fails length parity (Q-4).
2. **Budget.**
   - L: zoom.
   - M: sort.
   - Watch/do: balancer.
   - Micro: think, hook.
   - The family fits, and the line-up differs from chemical-bonds.
3. **CFIFA.** No calculation, so none is needed. Correct.
4. **Ladder.**
   - r1 Give 1 · r2 Complete 3 · r3 Explain 3 (chain with two named herrings) · r4 Explain 4 with marking points and rejects.
   - All rungs are scored and every chip is shown.
5. **Redundant text.** Q-1, Q-2 and Q-5 below.
6. **As built.**
   - Clean at 390 and 1280, light and dark, keyboard and tap. No overflow, no console errors.
   - There is **no route chip at all** under the big question (Q-6). The pilot shows "TRIPLE SCIENCE · HIGHER TIER".

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `#s-zoom` eyebrow | `Zoom in · {{ zoomStep }}` → `Zoom in` (delete the `zoomStep` constant) | "box 3 of 6" repeats `zoomProgress` ("2 of 6 called") and the prompt "Is box 3 an element…". The same box number is shown three times on one screen. | Mide's no-redundant-text rule |
| Q-2 | all | `#s-balance`, the `<p>{{ balLine }}</p>` under the steppers | Delete the line and the `balLine` constant | It reprints exactly the coefficients and formulae the stepper row directly above already shows (e.g. "2Mg + O₂ → 2MgO"). | Mide's rule |
| Q-3 | all | `#s-sort` `sortItems` | Make the label shape stop giving the bin away. Today every mixture is the only card with no formula (Air, Seawater, Crude oil, Bronze), and elements and compounds are given away by their formulae. Change `{ text: 'Seawater', … }` → `{ text: 'Salt water, NaCl in H₂O', bin: 'm', why: 'Two compounds, salt and water, not combined with each other: a mixture.' }` and `{ text: 'Gold, Au', … }` → `{ text: 'Graphite', bin: 'e', why: 'Graphite is pure carbon: one type of atom.' }`. Add one name-only compound, `{ text: 'Rust (iron oxide)', bin: 'c', why: 'Iron and oxygen chemically combined.' }`, in place of `Magnesium oxide, MgO`. | "No sort solvable by word shape" | Law 10; AUTHORING-BRIEF §5 |
| Q-4 | all | `rungs.r1` | `K.find(slug, R.route, 'key difference between a compound and a mixture')` → `K.find(slug, R.route, 'Which of these is a mixture')` (keep the current r1 as the fallback) | Option-length parity fails. The correct option is 21 words against a longest distractor of 15 (1.4×), so the longest line wins. The fallback item ("Bronze — …") is at parity. Frozen text cannot be edited, so choose the item that passes. | Law 10; content_standards §1 rule `1-length-parity` |
| Q-5 | all | `#s-sort` `done-note="{{ cmText }}"` | Replace with authored house-style text: `done-note="Name the test you used: one type of atom is an element; two or more elements chemically combined in fixed proportions is a compound; anything not chemically combined is a mixture."` | The verbatim `common_mistake` is printed in shouty capitals ("A COMPOUND is NOT a mixture… CHEMICALLY BONDED… In a MIXTURE…"), unlike any pilot text. It also re-explains electrolysis, which this lesson never teaches. `common_mistake` is not on the frozen list, so it may be re-cut. | AUTHORING-BRIEF §3 (frozen list); pilot visual language |
| Q-6 | all | lesson head, after `ks3-bigq` | Add the route chip exactly as in `using-moles-calculations.dc.html` lines 38–45 (`<details class="ks3-route-switch">… {{ routeWords }} … {{ routeSwitchOptions }}`), and add `routeWords: R.route, routeSwitchOptions: []` defaults to the fallback `R`. Eyebrow: `AQA Chemistry {{ specRef }} · Classify` → `AQA Chemistry ({{ specCode }}) {{ specRef }} · Classify`, with `specCode = R.isTriple ? '8462' : '8464'`. | Every pilot page as built, and four batch-2 lessons, show the route the pupil is on. This one shows none, and the eyebrow drops the qualification code. | Pilot built pages (e.g. `triple/higher/chemistry/bonding/metallic-bonding.html`) |

**ADVISORY**
- A-1. `#s-zoom` `zoomLog` chips ("Box 2 · element (you said compound)") repeat the verdict panel for the current box. Keep the log, but consider omitting the current box from it.
- A-2. The `#s-balance` tally chips ("O · 2 left · 1 right") and the "Not yet." verdict ("O: 2 on the left, 1 on the right") say the same thing. The verdict could just say "Not balanced yet."
- A-3. At 390 px the lattice boxes (FeS, bronze) scale to about 310 px wide, so the Cu/Sn/Fe/S letters render at about 7 px. Colour carries the distinction, but consider fewer, larger atoms (for example a 6×4 lattice).
- A-4. The `#s-balance` heading says "balance three yourself", but done fires at two.

**Verdict: FIX.** Fix the label-shape sort (Q-3), the rung-1 length parity (Q-4), the shouty done-note (Q-5), the missing route chip (Q-6) and the two redundant strings (Q-1, Q-2). The teaching design itself is pilot-grade.

---

## relative-formula-mass (QUANTITATIVE)

**Assessment**
1. **Laws.**
   - Hook (H₂O against O₂) gives commitment within 37 words.
   - The unpacker is predict-gated, with named counting-error distractors.
   - The bracket misconception is confronted at Mg(OH)₂.
   - The pans: predict, then produce both totals, then animated loading.
   - The Higher reacting-mass micro sits inline.
   - The mass bar on a fixed scale is real concrete→diagram→symbol.
   - Laws met.
2. **Budget.**
   - L: unpacker.
   - M: pans.
   - Micro: hook, the Higher choice.
   - Fits.
3. **CFIFA.**
   - The source FIFA (H₂SO₄) is verbatim with "Nothing to convert".
   - Worked: percentage, nothing to convert; kg→g conversion; plus a Higher reacting-masses example.
   - Two write-it-out attempts per tier, each opening with the convert decision.
   - F and H numbers differ.
   - Pass.
4. **Ladder.** r1 Calculate 1 (frozen) · r2 Calculate 2 (F) / 3 (H) with a convert chooser and units · r3 Explain 3 chain · r4 Explain 4 with points and rejects. Pass.
5. **Redundant text.** Q-1, Q-2 and Q-3.
6. **As built.**
   - Clean in all four states, keyboard and tap.
   - No route chip (Q-4).

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `#s-unpack` eyebrow; `#s-pans` eyebrow | `The formula unpacker · {{ upStep }}` → `The formula unpacker`; `Load the pans · {{ panStep }}` → `Load the pans` (delete `upStep` and `panStep`) | "4 of 4" / "equation 1 of 2" repeat the progress line beside them ("4 of 4 unpacked", "0 of 2 loaded"). | Mide's rule |
| Q-2 | all | `#s-unpack` confront panel, third paragraph `<p style="margin: 0;">{{ cmText }}</p>` | Delete the paragraph | The panel already has its three beats (quote; why, 42 not 58; the correct count). The verbatim common_mistake then restates the bracket rule a fourth time, in capitals ("BRACKETS… MULTIPLY…"). | Mide's rule; three-beat format, content_standards §3 |
| Q-3 | all | Key fact | `Percentage by mass of an element = Aᵣ × number of its atoms ÷ Mᵣ × 100. In magnesium oxide, MgO, that is 24 ÷ 40 × 100 = 60 % magnesium.` → `A number after a bracket multiplies everything inside it: Mg(OH)₂ is one Mg, two O and two H, Mᵣ = 58. Mᵣ has no units.` | The old key fact repeats the equation card directly above it word for word, and the MgO 60 % worked example. The bracket rule is the lesson's misconception and appears nowhere in the summary blocks. | Mide's rule |
| Q-4 | all | lesson head | Add the route chip and the qualification code as in AEC Q-6 | Route honesty and pilot parity. | Pilot built pages |

**ADVISORY**
- A-1. Rung 1 (Mᵣ of CaCO₃ = 100) repeats a number the Foundation pupil has just calculated (CFIFA Q1 "Mᵣ = 40 + 12 + 48 = 100"). The Higher r2 also starts from Mᵣ(CaCO₃). Consider the frozen H₂SO₄ or another Mᵣ item if the pool has one.
- A-2. The unpacker figure prints "Mᵣ = 342" on the bar, and the tally beside it ends "Mᵣ = … = 342". One of the two would do.
- A-3. In the unpacker's SVG title, the subscripts in "Al₂(SO₄)₃" render as small digits sitting on the baseline. Compare with how the pilot's diagrams set formulae.

**Verdict: FIX.** All four rows are small text edits. The teaching is pilot-grade.

---

## using-moles-calculations (QUANTITATIVE, CH/TH only)

**Assessment**
1. **Laws.**
   - The hook is the real problem.
   - The reaction bench is predict-gated, steps the reaction one formula unit at a time, plants the fewer-moles trap in Mix A, and has a reduced-motion swap.
   - The 1 : 1.5 rounding error is confronted.
   - The Triple solution micro is inline.
   - Pass.
2. **Budget.** L: bench. M: sort. Micro: think, solution, hook. Fits.
3. **CFIFA.**
   - Balance with nothing to convert; balance with kg→g; the verbatim source FIFA as the third example.
   - Q1 has nothing to convert; Q2 converts kg.
   - Higher-only lesson, so there is no F/H split. Pass.
4. **Ladder.** r1 State 1 (authored; parity fine) · r2 Calculate 3 · r3 Explain 3 · r4 Calculate 6 with six marking points. Pass.
5. **Redundant text.** Q-2.
6. **As built.**
   - Clean in all four states, keyboard and tap.
   - The route chip is present.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | CH, TH | `<h1>`, `Ks4Chrome title=`, `Ks4KeyNote title=` | `Using Moles — Calculations and Limiting Reactants` → `Using moles: calculations and limiting reactants` (all three) | Title Case. Every pilot lesson, and the lesson record (`title="Using moles — calculations and limiting reactants"`), use sentence case. | Pilot visual language; `ks4_lessons/batch_2.py` |
| Q-2 | CH, TH | `#s-bench` `loadLine` | When `s.mix === 2`, return `''` (or hide the `<p>`) | On "Your mix" the steppers already show "Magnesium 0.06 mol" and "Hydrogen chloride 0.08 mol", and the line under them reprints both values. | Mide's rule |

**ADVISORY**
- A-1. `hookReveal` gives the whole worked solution (n = 0.1 and 0.1, needs 0.2, HCl runs out). The same numbers then return as CFIFA worked example 3. Consider ending the reveal at "Each Mg needs two HCl: compare the moles with the ratio, not with each other", and letting the bench and CFIFA show the arithmetic.
- A-2. This lesson and concentration-of-solutions share nearly the same line-up (hook → explainer → predict-then-animate bench → Ks4Sort → think → route-tagged Choice section → equation → CFIFA → authored r1 MCQ). They differ in content, but the shape is one template. Consider a different M in one of them.

**Verdict: FIX** (Q-1 and Q-2 only; both trivial).

---

## concentration-of-solutions (QUANTITATIVE)

**Assessment**
1. **Laws.**
   - The hook commits on a real label.
   - The bench is predict-gated. Its four options are built from named slips (unconverted, multiplied, inverted), with error-specific feedback.
   - The cm³ misconception is confronted at birth.
   - The HT "explain mass/volume link" is a correct route layer with its own misconception.
   - Pass.
2. **Budget.** L: bench. M: convert sort (plus the Higher pour pair). Fits.
3. **CFIFA.** Verbatim source FIFA with the conversion in front, plus nothing-to-convert and rearrange examples. F and H numbers and demands differ. Pass.
4. **Ladder.** r1 State 1 · r2 Calculate 2/3 · r3 · r4 Describe 4 with points. r3 is defective on Higher (Q-3).
5. **Redundant text.** Q-2.
6. **As built.** Clean in all four states, keyboard and tap.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | all | `<h1>`, `Ks4Chrome title=`, `Ks4KeyNote title=` | `Concentration of Solutions` → `Concentration of solutions` | Title Case; the record and the pilot use sentence case. | Pilot; `batch_2.py` |
| Q-2 | all | `#s-bench` `madeLines` | Exclude the solution just made while its verdict is showing: `s.made.slice(0, madeNow ? -1 : undefined).map(…)` | After each make, "20 g ÷ 0.5 dm³ = 40 g/dm³" (verdict) and "20 g in 500 cm³ → 40 g/dm³" (log) show the same result twice, one above the other. | Mide's rule |
| Q-3 | CH, TH | `rungs.r3` (Higher branch) | `marks: 2` → `marks: 3`, and make it at least as demanding as the Foundation r3. For example: `prompt: 'Solution A: 6.0 g of salt in 150 cm³. Solution B: 10 g of salt in 250 cm³. Explain which is more concentrated. Put the links in order.'`, with the links: convert both volumes to dm³ (0.150 and 0.250); A = 40 g/dm³, B = 40 g/dm³; so they are equally concentrated, because concentration is mass per dm³, not total mass. | Today the Higher rung is a 2-mark chip on a 3-link chain (tariff does not match the chain), and it is *easier* than Foundation's r3 (5 g in 100 against 200 cm³, no conversion). "Same page, harder badge" in reverse. | Law 7; content_standards §5 |

**ADVISORY**
- A-1. The command-word card "Give the unit" is not an AQA command word. The pilot only lists real ones. Fold it into "Calculate".
- A-2. Three Foundation results are 30 g/dm³: worked example 1, the source FIFA, and Q1. Change Q1 (e.g. 9.0 g in 0.25 dm³ = 36 g/dm³) so the expected answer is not familiar.
- A-3. The `hookReveal` working ("250 cm³ ÷ 1000 = 0.25 dm³") is repeated in the explainer straight after it ("250 cm³ = 0.250 dm³").

**Verdict: FIX** (Q-1 to Q-3).

---

## percentage-yield (QUANTITATIVE, Triple only)

**Assessment**
1. **Laws.**
   - Phenomenon-first hook, the verbatim source scenario.
   - The yield bench gates each RP1 step and makes "where did the mass go" concrete.
   - The >100 % misconception is confronted.
   - The sort separates the three spec reasons from the catalyst/powder misconception.
   - The HT theoretical-yield block is inline.
   - Pass, with an advisory on the bench's binary demand.
2. **Budget.** L: bench. M: sort. Micro: which, think, hook. Fits.
3. **CFIFA.**
   - Verbatim source FIFA plus a kg→g example.
   - The Higher block has nothing-to-convert and kg examples, and two attempts.
   - **But the base write-it-out questions are identical on TF and TH** (Q-4).
4. **Ladder.** r1 Give 1 (fails parity, Q-3) · r2 Calculate 2 (TF, kg) / 3 (TH, moles chain) · r3 Explain 3 · r4 Calculate·Give 4 with points. Otherwise pass.
5. **Redundant text.** Q-1 and Q-2.
6. **As built.**
   - Clean in all four states, keyboard and tap.
   - Hard-coded "Triple / Foundation · Higher" pills (Q-5).

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | TF, TH | `#s-bench`, the `benchDone` paragraph | `<strong>Theoretical yield 8.0 g. Actual yield 6.2 g.</strong> Every gram is accounted for: the missing 1.8 g was left behind in four places, not destroyed.` → `<strong>Theoretical yield 8.0 g · actual yield 6.2 g.</strong> Nothing was destroyed.` | 6.2 g is already on screen three times: the balance drawing, "The balance now reads 6.2 g" and "6.2 g of 8.0 g". The four places are listed directly above. | Mide's rule |
| Q-2 | TF, TH | `keyBase` | Delete `'Chemistry-only spec point.'` | Not revision content. The route chip, the eyebrow and the key-note spec line ("AQA 4.3.3.1 (chemistry only)") already say it. | Mide's rule |
| Q-3 | TF, TH | `rungs.r1` | Replace `Object.assign(K.find(slug, R.route, 'Why is the actual yield') …)` with an authored State/Give MCQ at parity. For example: prompt `Give one reason why the actual yield of a reaction is less than the theoretical yield.`; options `Some product is left behind when it is separated from the mixture` (correct), `Some of the atoms are destroyed during the chemical reaction` (reply: atoms are conserved), `The catalyst was not added in a large enough amount` (reply: a catalyst changes rate, not yield), `The theoretical yield always rounds the answer upwards` (reply: it is calculated exactly from the equation). | The frozen item's correct option is 20 words against 11: the longest line wins. | Law 10; content_standards §1 |
| Q-4 | TF, TH | `cfQuestions` | Split by tier. Keep the current two for TF. For TH use numbers that differ and need rearranging, e.g. Q1 `A reaction has a percentage yield of 85%. The theoretical yield is 40 g. Calculate the actual yield.`; Q2 `A batch should give 2.50 kg of product. The percentage yield is 76%. Calculate the mass collected, in grams.` | The same two attempts appear on Foundation and Higher. | content_standards §2 ("same examples on F and H is a defect"); reviewer brief item 3 |
| Q-5 | TF, TH | lesson head | Replace the two hard-coded pills (`Triple`, `Foundation · Higher`) with the route chip as in AEC Q-6. Eyebrow: `AQA Chemistry 4.3.3.1 (chemistry only) · Quantitative` → `AQA Chemistry (8462) 4.3.3.1 · Quantitative` | On the Triple Foundation page, a pill saying "Foundation · Higher" is not true of that URL. The pilot shows the one route ("TRIPLE SCIENCE · FOUNDATION TIER") with the switcher. | AUTHORING-BRIEF §1; pilot built pages |

**ADVISORY**
- A-1. The bench's commit is binary ("Some is lost here / None"), and 4 of the 5 answers are "some". After step 1 the pattern is obvious. Consider committing to *where* the loss happens, or *how much*: rank the four losses largest first.
- A-2. The stage name "5 · Dry and weigh" repeats the number in "5 of 5 steps run".
- A-3. `#s-which` asks for 6.2 ÷ 8.0 × 100, and CFIFA worked example 1, immediately below, is the same calculation. Consider putting `#s-which` after the worked example, as the first "do".

**Verdict: FIX** (Q-1 to Q-5).

---

## titrations (REQUIRED PRACTICAL, Triple only)

**Assessment**
1. **Laws.**
   - Excellent RP lesson.
   - The phenomenon hook is right. The RP method, variables and risks are all there.
   - The rinse misconception is confronted before the bench.
   - The indicator choice is read from drawn strips.
   - The burette simulation is predict-gated. It has a rough run, run-in, dropwise, a meniscus close-up, varied initial readings and a planted anomalous run, then a concordance pick with error-specific feedback.
   - The flagship has one logic defect (Q-1).
2. **Budget.**
   - L: bench.
   - Micro: rinse, indicator, hook.
   - **No mid-size activity** (Q-4). CFIFA is a watch/do pair and does not count.
3. **CFIFA.**
   - Verbatim mean-titre FIFA plus a dm³→cm³ example.
   - The HT block (n = c × V) has nothing-to-convert and convert examples, with two attempts.
   - Base questions are identical on TF and TH (Q-3).
4. **Ladder.** r1 Give 1 (fails parity, Q-2) · r2 Calculate 2/3 · r3 Explain 3 · r4 Describe 6 with a levels descriptor and points. Otherwise pass.
5. **Redundant text.** Q-5.
6. **As built.** Clean in all four states, keyboard and tap.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | TF, TH | `#s-bench` logic: `judge()` / `onRecord` | **Logic bug.** Reproduced by tap at 1280: rough run to 24.00, then +5.00 → 29.00, recorded. Each accurate run's "Run in to 1 cm³ below the rough titre" then goes to 28.00, already past every end point (~24.70). All three accurate runs record 28.00. "Check the titres I chose" answers **"Concordant. Mean titre = … = 28.00 cm³."** and marks the bench done. **Fix:** on record, store `over: x.added > EP[x.run] + 5`. In `judge()`, before the concordance test, reject any chosen row with `over`: `{ ok:false, word:'These runs overshot.', note:'The run-in went past the end point, so these titres are too large. Do another rough run, and stop adding 5 cm³ once the flask flashes colourless.' }`. Also offer a "Repeat the rough run" path. | The flagship rewards a wrong mean as "Concordant", which teaches the opposite of the RP's point. | Law 10 (the activity must exercise the demand it claims) |
| Q-2 | TF, TH | `rungs.r1` | Replace `K.find(slug, R.route, 'added dropwise')` with an authored rung at parity. For example: prompt `Give the reason the acid is added drop by drop near the end point.`; options `So that one drop past the end point is not added` (correct), `So that the acid does not splash out of the flask` (reply: swirling prevents splashing; dropwise is about accuracy), `So that the indicator has time to react` (reply: indicators change instantly), `So that the mixture does not get too hot` (reply: the temperature change is tiny). | The frozen item's correct option is 17 words against 10: the longest line wins. | Law 10; content_standards §1 |
| Q-3 | TF, TH | `cfQuestions` | Split by tier. Keep the current two for TF. For TH, use a set with a rough run and an anomaly where the answer must be given to 2 d.p. from three concordant titres. For example: `Rough 23.40 cm³, then 22.95, 23.05, 22.60 and 23.00 cm³` → concordant 22.95, 23.05, 23.00 → mean 23.00 cm³. | The same two attempts appear on Foundation and Higher. | content_standards §2; reviewer brief item 3 |
| Q-4 | TF, TH | after `#s-bench` | Add one mid-size activity. The natural one is a `Ks4Sort`, "Titre too large, too small, or no effect?", with cards confronting the rinse misconception at scale: burette rinsed with water (too large); conical flask rinsed with water (no effect); overshooting the end point (too large); reading the top of the meniscus on the final reading (too small); air bubble in the burette jet that fills during the run (too large); pipette rinsed with water (too small). Each card gets its `why`. | The budget requires one or two mid-size activities, and the pilot RP lesson has one (the variables sort). | architecture §"Instrument budget" |
| Q-5 | TF, TH | lesson head | Replace the `Triple` and `Foundation · Higher` pills with the route chip (as in AEC Q-6). Keep the RP pill as the pilot does: `Required practical 2 · titration` → `Required practical · titration`. Eyebrow → `AQA Chemistry (8462) 4.4.2.5 · Required practical`. | On the head, "chemistry only" plus "Triple" plus "Required practical" (eyebrow) plus "Required practical 2" (pill) say two things twice. "Foundation · Higher" is untrue on a single-route URL. The pilot RP head is: eyebrow "· Required practical", route chip, one RP pill. | Mide's rule; pilot `resistors` as built |

**ADVISORY**
- A-1. `keyBase` (verbatim key_note) ends "RP Chemistry 2 (chemistry-only)." It sits directly under the key-note spec line "AQA 4.4.2.5 · RP2 (chemistry only)". The key note is not frozen, so the duplicate can be dropped.
- A-2. At 1280 the bench's third column is narrow, so "BURETTE NOW 25.00 cm³" wraps to two lines. Consider stacking the two readouts.

**Verdict: FIX.** Q-1 is a flagship logic bug. The others are Q-2 to Q-5. Otherwise this is the strongest lesson in the group.

---

## metal-hydroxides (CLASSIFY, Triple only)

**Assessment**
1. **Laws.**
   - Hook with a drawn figure.
   - A precipitate bench with a commit before every tube, a second commit before excess on the white ones, an iron(II) "leave to stand" messy observation, and unknowns W–Z that refuse a white identification made before excess.
   - The excess-at-once misconception is confronted.
   - Equation forge: watch one, then build two, with per-option corrections.
   - The HT ionic build is inline.
   - Laws met.
2. **Budget.**
   - L: bench.
   - M: forge (labelled Mid in the notes; it is a worked/do pair, but its two builds are production with per-distractor feedback).
   - Micro: think, ionic, hook.
   - Acceptable.
3. **CFIFA.** No calculation. Correct.
4. **Ladder.** r1 Identify 1 · r2 Identify 3 from a drawn results table · r3 Explain 3 · r4 Plan 6 with levels and points. Pass.
5. **Redundant text.** Q-1.
6. **As built.** Clean in all four states, keyboard and tap. The ten tube tabs wrap to five rows at 390 px; acceptable.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | TF, TH | lesson head | Delete the `Triple` and `Foundation · Higher` pills, and the `<sc-if value="{{ isHigher }}">…Contains Higher…</sc-if>` pill. Add the route chip as in AEC Q-6. Keep the RP pill in the pilot's form: `Required practical 7 · identifying ions` → `Required practical · identifying ions`. Eyebrow: `AQA Chemistry 4.8.3.2 (chemistry only) · Classify` → `AQA Chemistry (8462) 4.8.3.2 · Classify` | "Contains Higher" repeats the inline Higher badges the build already puts on each Higher block. "Foundation · Higher" is untrue on a single-route URL. "chemistry only" repeats the Triple chip. | Mide's rule; AUTHORING-BRIEF §1 |

**ADVISORY**
- A-1. `benchTitle` ("Copper(II) sulfate · call it, then add the sodium hydroxide") repeats the commit prompt under it ("Commit first. A few drops of sodium hydroxide go in. What forms?"). After identification it still reads "Tube Z · run the test, then name the ion". The pilot has the same title-plus-prompt pattern, so this is advisory. A done state ("Tube Z · identified") would help.
- A-2. The ladder is a near-clone of carbonates-halides-sulfates in the same topic. r2 is "A student tested three solutions, P, Q and R. Use the results to identify…" from a drawn table, and r4 is a 6-mark Plan with the same levels wording. Vary one of them, e.g. make this lesson's r2 "Complete the balanced equation for iron(III) chloride + sodium hydroxide", which uses the forge skill.

**Verdict: FIX** (Q-1 only).

---

## carbonates-halides-sulfates (REQUIRED PRACTICAL, Triple only)

**Assessment**
1. **Laws.**
   - The hook is a real false positive (HCl acidified, so everything reads "chloride").
   - The fizz misconception is confronted with a drawn Mg-in-acid tube.
   - The RP method and risks are there.
   - The test rack gates on calling the metal ion first, then running anion tests on unknowns, then naming the salt. Each wrong name is a named error, and the cream/yellow and blue-solution observations are messy.
   - The acid-choice sort works.
   - The HT spectator-ion strike-out is inline.
   - Strong.
2. **Budget.** L: rack. M: acid sort. Micro: hook, think, ionic. Fits.
3. **CFIFA.** No calculation. Correct.
4. **Ladder.** r1 Identify 1 · r2 Identify 3 from a table · r3 Explain 3 · r4 6 marks with levels. The r4 chip and question disagree (Q-2).
5. **Redundant text.** Q-3.
6. **As built.** Clean in all four states, keyboard and tap.

**REQUIRED**

| # | Route(s) | Where | Old → New | Reason | Citation |
| --- | --- | --- | --- | --- | --- |
| Q-1 | TF, TH | lesson head | As metal-hydroxides Q-1: remove the `Triple`, `Foundation · Higher` and `Contains Higher` pills; add the route chip; `Required practical 7 · identifying ions` → `Required practical · identifying ions`; eyebrow `AQA Chemistry 4.8.3.3–4.8.3.5 (chemistry only) · Required practical` → `AQA Chemistry (8462) 4.8.3.3–4.8.3.5 · Required practical` | Same reasons. | Mide's rule; pilot RP head |
| Q-2 | TF, TH | `rungs.r4` | `command: 'Plan'` with question `Describe tests the student could use to identify each solid. Give the results.` → question `Plan tests that would identify each solid. Give the result each one would show.` (keep `Plan`) | The command chip says Plan but the question says Describe, so the exam word being taught contradicts itself. | Law 7 |
| Q-3 | TF, TH | `#s-rack` result | The last test's result shows three times: the figure caption ("no precipitate"), the result line "Hydrochloric acid + barium chloride: No precipitate." and the log row "Hydrochloric acid + barium chloride · No precipitate.". Fix: `logOn` shows only rows *other than* `r.last` (`TESTS.filter((x) => runs[x.k] === 'done' && x.k !== r.last)`), with `logHead` `'Salt ' + S.id + ' · earlier results'`. | Mide's rule |

**ADVISORY**
- A-1. The anion test results are revealed without a bet (Law 4). The salt name is the commitment, so this is acceptable for an RP identification. A cheap upgrade: before the first anion test on each salt, "Which test do you expect to be positive?" (three buttons).
- A-2. `rackTitle` ("Salt 3 · call the metal ion first") repeats the prompt under it ("Call it first. Which metal ion is in this salt?"). This is the pilot's pattern too.
- A-3. See metal-hydroxides A-2: the two analysis lessons share their r2/r4 shape.

**Verdict: FIX** (Q-1 to Q-3).

---

## Summary

| Lesson | Verdict | Required |
| --- | --- | --- |
| atoms-elements-compounds | FIX | Q-1…Q-6 (sort word-shape, r1 parity, shouty done-note, route chip, 2 redundant strings) |
| relative-formula-mass | FIX | Q-1…Q-4 (redundant counters, confront 4th beat, key fact repeats equation, route chip) |
| using-moles-calculations | FIX | Q-1, Q-2 (Title Case, duplicate load line) |
| concentration-of-solutions | FIX | Q-1…Q-3 (Title Case, duplicate result line, Higher r3 tariff/demand) |
| percentage-yield | FIX | Q-1…Q-5 (redundant done box and key line, r1 parity, F/H CFIFA identical, header pills) |
| titrations | FIX | Q-1…Q-5 (**overshoot accepted as concordant**, r1 parity, F/H CFIFA identical, no M activity, header pills) |
| metal-hydroxides | FIX | Q-1 (header pills) |
| carbonates-halides-sulfates | FIX | Q-1…Q-3 (header pills, r4 command mismatch, result shown three times) |

Shared, outside the lessons: S-1, Ks4Sort's onDone does not reach the rail (pilot affected too).

---

## Round 2 (re-review of commit 36fd4c877)

I re-checked commit 36fd4c877 in a browser on the same rules: built pages from port 8716 in headless Chrome, read-only.

- **Built pages are current:** `ks4_batch_check --batch batch-2` reports all 52 pages clean.
- **Routes and modes:** each lesson was driven on TH at 1280 light by keyboard, and on a Foundation route (CH for using-moles) at 390 dark by tap.
- **Page health:** no horizontal scroll, no undefined/NaN/`{{`, and zero console errors on any page. The one exception is the expected `/api/health` CORS block from localhost.
- **Out of scope:** S-1 (the Ks4Sort rail tick) is out of scope by commander decision. It still affects every sort, including the new `#s-errors`.

### Titrations overshoot (Q-1): reproduced and now refused

I replayed the original failing sequence by **tap** at 390 on TF, and again by **keyboard** at 1280 on TH:
- rough run to 24.00, then +5.00 → 29.00, recorded;
- three accurate runs, each "Run in to 1 cm³ below the rough titre", all at 28.00.

What the bench does now:
- The rows read "RUN n · OVERSHOT".
- Choosing runs 1–3 gives **"These runs overshot. The run-in or a splash went past the end point, so these titres are too large. Leave them out. …"**, and the rail stays un-done.
- "Repeat the rough run" works. A careful rough run (25.00) and two dropwise runs, chosen together, give "Concordant. Mean titre = (24.75 + 24.70) ÷ 2 = 24.73 cm³", and the bench ticks done.

**Confirmed.**

### New titrations sort (`#s-errors`, Q-4)

- **Structure:** 7 cards in 3 bins (too large / too small / no effect), each with a `why`. I solved it by tap and by keyboard.
- **No word-shape giveaway:** "rinsed with water" appears in all three bins (burette, pipette, flask), so the wording does not give the bin away.
- **Done-note:** a single useful question ("does the slip change the amount of alkali in the flask, the strength of the acid, or the reading?").
- **Real mid-size activity.** `block_map` now has `"s-errors": "check"`.

### Required rows, confirmed in the built pages

| Lesson | Rows | Status |
| --- | --- | --- |
| atoms-elements-compounds | Q-1 eyebrow "Zoom in" · Q-2 `balLine` gone · Q-3 Graphite / Rust (iron oxide) / Salt water, NaCl in H₂O, so each bin now mixes formula and no-formula cards · Q-4 r1 is "Which of these is a mixture?" (11 vs 9 words, passes) · Q-5 authored done-note, no caps · Q-6 route chip, "(8462) 4.1.1.1" / "(8464) 5.1.1.1" | all confirmed |
| relative-formula-mass | Q-1 eyebrows without counters · Q-2 confront panel has its three beats, no caps paragraph · Q-3 bracket-rule key fact · Q-4 route chip and code | all confirmed |
| using-moles-calculations | Q-1 sentence-case `<title>`, `<h1>`, chrome and key note · Q-2 no load line on "Your mix" | all confirmed |
| concentration-of-solutions | Q-1 sentence case · Q-2 the current solution shows once (verdict); the log lists only earlier ones · Q-3 Higher r3 is 3 marks, 6.0 g/150 cm³ against 10 g/250 cm³ with conversion, harder than Foundation's | all confirmed |
| percentage-yield | Q-1 closing box "… actual yield 6.2 g. Nothing was destroyed." · Q-2 key-note line gone · Q-3 authored r1 at parity · Q-4 TH write-it-out questions are rearrangements (72 % of 45 g; 85 % of 2.40 kg), TF unchanged · Q-5 route chip, "(8462) 4.3.3.1" | all confirmed |
| titrations | Q-1 above · Q-2 authored r1 at parity · Q-3 TH Q1 is the rough-plus-anomaly set to 2 d.p.; TF unchanged · Q-4 above · Q-5 route chip plus one pill "Required practical · titration" | all confirmed |
| metal-hydroxides | Q-1 pills replaced by the route chip plus "Required practical · identifying ions"; "Contains Higher" gone | confirmed |
| carbonates-halides-sulfates | Q-1 as metal-hydroxides · Q-2 r4 reads "Plan tests that would identify each solid…" under a PLAN chip · Q-3 log is "Salt N · earlier results" without the latest test | all confirmed |

### New-redundancy sweep

None of the fixes added redundant text:
- The "OVERSHOT" row label marks the record. The flask line describes only the run in progress.
- The concentration bench now shows each result once.
- The carbonates rack shows the latest result once (the result line), plus the drawn tube caption.

### Advisory (round 2, not blocking)

- R2-A1. The eyebrow subject label is inconsistent on Combined pages:
  - atoms-elements-compounds and relative-formula-mass read "AQA Chemistry (8464) …";
  - using-moles and concentration read "AQA Combined Science (8464) …".

  Pick one form batch-wide. The science reviewer's "Combined Science (8464)" is the more accurate.
- R2-A2. The titrations transcript rows are `<button>`s whose `aria-pressed` is only emitted when true. This matches the shared runtime, and the selected state still shows visually.

### Final verdicts

| Lesson | Verdict |
| --- | --- |
| atoms-elements-compounds | **SHIP**: all six required rows fixed and verified |
| relative-formula-mass | **SHIP**: all four required rows fixed and verified |
| using-moles-calculations | **SHIP**: both required rows fixed; A-2 line-up accepted by the commander |
| concentration-of-solutions | **SHIP**: all three required rows fixed and verified |
| percentage-yield | **SHIP**: all five required rows fixed and verified |
| titrations | **SHIP**: overshoot now refused (reproduced by tap and keyboard), mid-size sort added, other rows fixed |
| metal-hydroxides | **SHIP**: header fixed |
| carbonates-halides-sulfates | **SHIP**: all three required rows fixed and verified |
