# sampling-techniques

Sources: AQA spec 4.7.2.1 Levels of organisation (the transect, quadrat and abundance lines) and its required practical, read from spec-8464.txt (CF CH) and spec-8461.txt (TF TH). The content lines are word for word the same; the practical is "Required practical activity 7" in 8464 and "Required practical activity 9" in 8461, same wording. No HT-only or Biology-only lines. Rainford KS4 Biology Unit 7 lessons "Random sampling" (quadrat, transect, evaluate data, calculate area, mean, median, mode and range, why sample size matters) and "Systematic sampling and required practical" (plan a valid method to estimate a plant population; key words transect, bias, population). LEGACY page (batch 10).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| A range of experimental methods using transects and quadrats are used by ecologists to determine the distribution and abundance of species in an ecosystem | Card: Quadrats and transects; Reveal: Random quadrats or a transect?; Key fact | CF CH TF TH | ✓ |
| Understand the terms mean, mode and median (MS 2b) | Reveal: Daisies in ten quadrats; Rung 1 Q2; Quiz Q3 | CF CH TF TH | ✓ |
| Calculate arithmetic means (MS 2b) | Reveal (mean); Card: From raw counts (steps-worked, steps-attempt); Card: Worked examples (cfifa); Rung 2 | CF CH TF TH | ✓ |
| Plot and draw appropriate graphs selecting appropriate scales for the axes (MS 4a, 4c) | Card: Plotting the results; Reveal: Daisies along the transect | CF CH TF TH | ✓ |
| Required practical activity 7 (8464): measure the population size of a common species in a habitat; use sampling techniques to investigate the effect of a factor on the distribution of this species | Card: Required practical activity 7 (routes CF CH); Card: Estimating a population with random quadrats (fig:random-quadrats); Card: Distribution along a transect (legacy-fig:trFig); Rung 3; Rung 4 | CF CH | ✓ |
| Required practical activity 9 (8461): the same wording | Card: Required practical activity 9 (routes TF TH); the same cards and rungs | TF TH | ✓ |
| MS 2f (estimating population size from a sample) | Card: Scaling up (triangle:EQ_POP); Card: Worked examples; Rung 2; Quiz Q1, Q5; Easy mistakes | CF CH TF TH | ✓ |
| (SOW) bias, random sampling, sample size, range, area of a quadrat, evaluate data | Card: Why random, and why many; Reveal (range); Card: Scaling up; Dive deeper: Evaluating your results; Rung 3 chain 1; Quiz Q2, Q5 | CF CH TF TH | ✓ |

**Gaps and mismatches.** The legacy page labelled the continuous belt transect "Triple only"; neither spec says so, and neither spec names either kind of belt transect. Both kinds are now in Dive deeper on every route. The legacy page never named the range, which the SOW asks for; it is now a row of the averages table. "Abundance" and "distribution" are the spec's own words and are now key words.

**Practice set source.** The page's own `BANK` (`BANK.map((q) => K.item(q))`), the same five on every route; it does not read the subtopic `quiz` list. Fixes are `logic_edits`. No quiz-sampling-techniques.json. No stem edited, so all five IDs survive.

**Equation and worked examples.** The record defines EQ_POP (identical to the legacy page's EQ_P) and places its triangle with `triangle:EQ_POP`. The CFIFA examples and questions (`cfifa`) and the two Step widgets (`steps-worked`, `steps-attempt`) are the legacy page's own. Every number checked: 4 × 500 = 2000; 3 ÷ 0.25 = 12, 12 × 200 = 2400; 6 × 800 = 4800; 2 ÷ 0.25 = 8, 8 × 150 = 1200; (2+5+3+4+6+3+5+4+2+6) = 40, 40 ÷ 10 = 4, 4 × 600 = 2400; (3+1+2+4+2+3+1+0) = 16, 16 ÷ 8 = 2, 2 ÷ 0.25 = 8, 8 × 120 = 960. The record's averages table: sum 40, mean 4, mode 2, median 3.5, range 7.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Apparatus for light intensity | ok |
| Rung 1 Q2 What the mode is | ok |
| Rung 2 calc 1 1 m² quadrats, 5 × 350 | ok (1750 daisies) |
| Rung 2 calc 2 50 cm quadrat | ok for the answer (400 dandelions). Fault: the credited Convert choice was the only one carrying the whole working. Fix: "Convert 50 cm to 0.5 m, so the area is 0.25 m²" / "Convert 50 cm to 5 m, so the area is 25 m²"; same index and answer. |
| Rung 3 chain 1 Biased placement | ok. One forced order. |
| Rung 3 chain 2 Transect method | ok. One forced order: the tape comes first, the quadrats need the tape, and the last link ends with plotting. |
| Rung 4 Estimate dandelions, 6 marks | ok |
| Quiz Q1 Dandelion estimate | ok (rendered labels are the four numbers) |
| Quiz Q2 Why random | ok |
| Quiz Q3 Snail mode and median | ok (0, 1, 1, 1, 3, 4, 4: mode 1, median 1, mean 2) |
| Quiz Q4 Bluebell transect | Fault: credited option visibly longest (+60). Fix: "Most bluebells are found at a medium light intensity" / "Bluebells increase steadily as light increases" / "Light intensity has no effect on bluebells" / "Bluebells grow best in the deepest shade"; feedback kept. Stem kept. |
| Quiz Q5 50 cm quadrat area | ok |

**Removed or moved.**
- Removed: the method stepper and its gate questions (now the ordered method card); the "thrown over the shoulder" check (now "Why random, and why many" and an Easy mistake); the mode and median checks (now the reveal table); the transect distance buttons and their notes (now the data table); the "what does the transect show" check; the Think again choice (now an Easy mistake); the Sort (now the reveal table "Random quadrats or a transect?"); the Command words grid; the Key note; the video.
- Not kept: `rpFig`. At its first state it draws only the two tapes and no quadrats. A new figure is asked for: `fig:random-quadrats` (see the report).
- Kept: `legacy-fig:trFig` at its first state: hedge, tape, six quadrats at 0 to 10 m with dots for the daisies in each (0, 1, 3, 6, 9, 11), and a box with the 0 m reading (150 lux, 0 daisies). Checked against its drawer and the TR data; the record's table gives the full readings.
- Moved to Dive deeper: interrupted and continuous belt transects (every route).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. None.
- New id (stem changed): None.
- Rung prompts reworded, position kept (id kept): Rung 2 calc 2 (sampling-techniques#r2-2): "A quadrat with sides of 50 cm" (no option change).

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- BLIND MED r2-2 (sampling-techniques#r2-2): prompt now "A quadrat with sides of 50 cm gives a mean of 1 dandelion per quadrat." Position kept (id kept). The same wording applied to the CFIFA worked example and CFIFA question 2 (cfifa slot), and to the Easy mistakes card.
- EX1 SHOULD fig:random-quadrats: already drawn (lead); slot kept, no change.
- EX2 NOTE practice Q2 (quiz-CF-2): all three explanations rewritten plainly (examiner gave 2 and 3; 1 had a dash aside too). Options unchanged.
- EX3 NOTE Q4 +6: no change.
