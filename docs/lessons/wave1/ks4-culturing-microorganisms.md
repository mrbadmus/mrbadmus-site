# culturing-microorganisms

Sources: AQA 8461 4.1.1.6 Culturing microorganisms **(biology only)**: Triple routes only (TF, TH); 8464 has no such section. One line is **(HT only)**: "express the answer in standard form" (TH). **Required practical activity 2 (8461)**: "investigate the effect of antiseptics or antibiotics on bacterial growth using agar plates and measuring zones of inhibition" (AT 1, 3, 4 and 8). Skills: MS 1a, 1b, 1d, 2a, 2h (number of bacteria from the mean division time); MS 5c (πr²); WS 2.2, 2.4. Links to Antibiotics and painkillers.

Old page: Design batch-6 (`ks4-biology-4.1.1.6-culturing-microorganisms.dc.html`), family Quantitative, routes TF TH. Practice set = hard-coded bank: four shared items plus a fifth per route (TH standard form, TF taping the lid).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| Bacteria multiply by simple cell division (binary fission) as often as once every 20 minutes if they have enough nutrients and a suitable temperature | Card 'How bacteria multiply'; Key fact; Rung 1 | TF TH | ✓ |
| Bacteria can be grown in a nutrient broth solution or as colonies on an agar gel plate | Card 'How bacteria multiply' | TF TH | ✓ |
| Uncontaminated cultures are required for investigating the action of disinfectants and antibiotics | Card 'Why a culture must be pure' | TF TH | ✓ |
| Describe how to prepare an uncontaminated culture using aseptic technique | Reveal 'Aseptic technique'; RP card; Rung 4 | TF TH | ✓ |
| Explain why Petri dishes and culture media must be sterilised before use | Reveal 'Aseptic technique' | TF TH | ✓ |
| Explain why inoculating loops must be sterilised by passing them through a flame | Reveal; practice Q3 | TF TH | ✓ |
| Explain why the lid should be secured with adhesive tape and stored upside down | Reveal; Rung 3 (i); practice Q5 (TF) | TF TH | ✓ |
| Explain why, in school laboratories, cultures should generally be incubated at 25 °C | Reveal; Easy mistakes; Rung 1; practice Q1 | TF TH | ✓ |
| Calculate cross-sectional areas of colonies or clear areas around colonies using πr² | Card 'Area of a clear zone' (triangle:EQ_AREA, CFIFA); Easy mistakes; Rung 2 (i) | TF TH | ✓ |
| Calculate the number of bacteria in a population after a certain time if given the mean division time | Card 'Number of bacteria after a time' (triangle:EQ_DIV, cm-w, cm-a); Rung 2 (ii); practice Q4 | TF TH | ✓ |
| (HT only) Express the answer in standard form | Card 'Higher: standard form' (TH only); practice Q5 (TH) | TH | ✓ |
| RP 2: antiseptics or antibiotics, agar plates, zones of inhibition | Card 'Required practical 2: antibiotics and antiseptics' (fig:agar-plate-zones); Rung 3 (ii); Rung 4; practice Q2 | TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** Incubate at 37 °C; each division adds 2; putting the diameter into πr².

**Gaps and mismatches.** None. The Higher standard-form card is gated on TH; the standard-form answers inside the worked steps were already TH-only on the Design page (`H`).

**Practice set source.** Hard-coded bank, five items per route (four shared). Every stem kept.

**Audit of the ladder and practice set (faults found and fixed).**
- Q1 (25 °C), Q2 (large clear zone), Q3 (flaming the loop): each credited option the longest (+50 to +60), with dashes. Options and replies rewritten to equal length.
- Q5 TF (taping the lid): credited the longest (+24). Options rewritten.
- Rung 3 (i): its three links (tape keeps microbes out; a few strips let oxygen in; upside down stops condensation) were three separate facts that fit in any order. Now one chain about storing the dish upside down, one order; the taping reasons are in the Aseptic technique table. Prompt reworded; the rung keeps its position.
- Worked example 1: Convert line wordy with a dash; Insert repeated the halving. Shortened; same numbers.
- The page returned a bare `return {`; a logic edit makes it `Object.assign({}, R, {` so the per-route eyebrow and the record's two triangles bind. The page's own keys come after R, so nothing it set changes. The pre-load fallback route gains `isTriple: true`.
- Numbers checked: π × 9² = 254.47 ≈ 254 mm²; 2.4 cm = 24 mm, r = 12, π × 144 = 452.39 ≈ 452 mm²; Your turn π × 7² = 153.94 ≈ 154 mm² (π × 14² = 615.75 ≈ 616 if not halved); 1.6 cm = 16 mm, r = 8, π × 64 = 201.06 ≈ 201 mm² (π × 0.8² = 2.01 cm² if left in cm); Rung 2 (i) 2.0 cm = 20 mm, r = 10, π × 100 = 314.16 ≈ 314 mm²; 3 h = 180 min, 180 ÷ 20 = 9, 2⁹ = 512 = 5.12 × 10²; 2 h = 120 min, 120 ÷ 30 = 4, 50 × 2⁴ = 800 = 8 × 10²; Rung 2 (ii) 120 ÷ 20 = 6, 10 × 2⁶ = 640 = 6.4 × 10²; practice Q4 60 ÷ 20 = 3, 2³ = 8; practice Q5 TH 2 560 000 = 2.56 × 10⁶.

**Old subtopic data.** spec "4.1.2" on TF/TH: wrong (want 4.1.1.6; `BIO_EYEBROW` is what the page uses).

**Unsure (left out until checked).** "A few strips of tape, not all the way round, so oxygen gets in and harmful anaerobic bacteria do not grow" is the standard AQA practical-handbook reason, not spec wording. Kept, in the table and in TF practice Q5.

**Removed or moved.**
- Design benches (divide button, tap the discs), Think again, sort: off the page. The plate is drawn (`figlib/ks4lean_cell.py`) with the Design page's zones (A 18 mm, B 28 mm, C and the control W none).
- The control disc's reasoning: Dive deeper (and Rung 3 (ii)). Link to Antibiotics and painkillers: Dive deeper. Command words: Dive deeper.

**Examiner fix round (26 Nov 2026).**
- Practice Q4 reply for '6': '6 is 3 × 2. Bacteria double at each division: 1 → 2 → 4 → 8.'
- Rung 2 (ii) (blind check CU-07): a pupil working in hours could defend 'Nothing to convert'. That conversion choice is now 'Convert hours to minutes: divide by 60' (wrong). Key unchanged: 'Convert hours to minutes: multiply by 60', 640 bacteria. ('Convert minutes to hours: divide by 60' was not used: it is a correct conversion that also gives 6 divisions.)
