# pyramids-of-biomass (LEGACY, batch 10)

Sources: AQA 8461 4.7.4.2 "Pyramids of biomass" (in 4.7.4, "biology only"), read from the spec PDF; the losses card is 8461 4.7.4.3. 8464 has neither; the page exists only on TF and TH, so no route gating is needed. Nothing here is HT only. Rainford SOW lesson "Trophic levels in an ecosystem, transfer of biomass" (construct and interpret pyramids of biomass from data; key words pyramid of number, pyramid of biomass).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Pyramids of biomass can be constructed to represent the relative amount of biomass in each level of a food chain | Card: What a pyramid of biomass shows; Key fact; Start here; Rung 1 Q1 | TF TH | ✓ |
| Trophic level 1 is at the bottom of the pyramid | Cards: What a pyramid of biomass shows, Constructing one accurately; Easy mistakes; Key fact; Rung 3 Q1; Practice 4 | TF TH | ✓ |
| MS 2c: construct accurate pyramids of biomass from appropriate data | Cards: Constructing one accurately, Worked example (legacy-fig:pFig), Converting kg to g; Easy mistakes; Rung 2 (two calculations); Rung 3 Q1; Rung 4; Practice 1, 2, 3 | TF TH | ✓ |
| (4.7.4.3) Describe pyramids of biomass; explain how biomass is lost between trophic levels (faeces; carbon dioxide and water in respiration; water and urea in urine; about 10%) | Card: Why each bar is narrower; Rung 3 Q2; Rung 4; Practice 5. Taught in full in Transfer of biomass | TF TH | ✓ |

**Practice set source.** The practice set is the `BANK` array written in the legacy logic (five items, the same on TF and TH). It does not read the subtopic `quiz` list, so every fix is a `logic_edits` pair and there is no quiz-pyramids-of-biomass.json. BANK item 1 is the old subtopic quiz question 2; the old quiz question 1 (pyramid of numbers) was already gone from the live page.

**Audit of every legacy rung and practice item.**

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (what bar width shows) | ok | none |
| Rung 1 Q2 (unit for biomass, g/m²) | ok | none |
| Rung 2 Q1 (calc: 240 ÷ 60 = 4 cm) | ok, recomputed | none |
| Rung 2 Q2 (calc: 1.5 kg/m² = 1500 g/m², ÷ 100 = 15 cm) | ok, recomputed | none |
| Rung 3 Q1 (chain: construct) | ok, one forced order | none |
| Rung 3 Q2 (chain: why biomass falls) | ok, one forced order (link 2 opens "Then") | none |
| Rung 4 (meadow: 900, 180, 18 g/m², scale 1 cm = 90 g/m² → 10, 2, 0.2 cm) | ok, recomputed; "a fifth, then a tenth" is right | none |
| Practice 1 (grasshopper bar, scale 1 cm = 50 g/m²) | Every option carried its own working after a dash, so the one correct sum gave the answer away | logic_edits: question text kept (ID kept); options now 1 cm ✓ / 10 cm (the grass bar) / 0.1 cm (the frog bar) / 50 cm, with feedback naming each slip |
| Practice 2 (600, 120, 30 g/m², scale 60 → 10, 2, 0.5 cm) | ok, recomputed | none |
| Practice 3 (1.2 kg/m², scale 100 g/m² → 12 cm) | ok, recomputed | none |
| Practice 4 (where level 1 goes) | "At the bottom, as the widest bar": the spec says only "at the bottom", and real pyramids of biomass are not always widest at the base | logic_edits: question text kept; credited option "At the bottom"; one reply reworded |
| Practice 5 (how biomass changes, and why) | Credited option 133 characters against at most 45 | logic_edits: question text kept; "It decreases, as some biomass is lost at each level" ✓; distractor 3 reply names the three losses |
| Figure pFig | Correct: 400 ÷ 40 = 10 cm, 80 ÷ 40 = 2 cm, 16 ÷ 40 = 0.4 cm, level 1 at the bottom, bars centred, scale bar and scale written. Checked by rendering it | used, in Card: Worked example |
| Figure bFig | Not used: it draws the pupil's own choices from the removed builder, so with no choices it is empty | none |

**Gaps and mismatches.** None in the legacy page's spec coverage.

**Removed or moved.** Removed with the legacy body: the hook, the "why narrower" pick, the woodland bar-width builder, the "Think again" and the true/false sort. Their teaching is carried by the cards (the woodland's 0.8 kg/m² conversion is now Card: Converting kg to g). Moved to Dive deeper: pyramids of numbers (Rainford key word, not on the spec).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q1 (pyramids-of-biomass#r1-1): two distractors.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r1.0 (pyramids-of-biomass#r1-1): distractors now "The number of organisms at that level", "The mass of one organism at that level". KEY CHANGE (distractors).
- EX2/EX3 NOTE Q5: no change.
