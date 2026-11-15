# deforestation

Sources: AQA spec 4.7.3.4, read from the 8464 and 8461 PDFs on Mide's Mac (also checked against spec-8461.txt in this folder, which holds this section). The content is word for word the same in 8464 and 8461, with no HT-only and no "(biology only)" line. Rainford KS4 Biology Unit 7 lesson "Waste management & Land use" (why vast tropical areas have been cleared of trees; how deforestation increases carbon dioxide in the atmosphere and leads to a reduction in biodiversity). No required practical. Combined routes (CF, CH) use 8464. Triple routes (TF, TH) use 8461.

Legacy lesson (batch 10). The ladder (Ks4Practice rungs) and the practice set stay from the Design page with their ids. **The practice set is the `BANK` array written inside the legacy logic, not K.bank, so every practice-set fix is a `logic_edits` pair, and there is no quiz-deforestation.json.**

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Large-scale deforestation in tropical areas has occurred to provide land for cattle and rice fields | Card: Why tropical forest is cleared; Key fact; Reveal table (Gain: food); Rung 1; Practice set Q3 | CF CH TF TH | ✓ |
| Large-scale deforestation in tropical areas has occurred to grow crops for biofuels | Card: Why tropical forest is cleared; Key fact; Reveal table (Gain: fuel); Rung 1; Rung 4; Practice set Q5 | CF CH TF TH | ✓ |
| WS 1.4: evaluate the environmental implications of deforestation | Reveal table: Weighing up deforestation; Card: Evaluating deforestation; Rung 4 (6-mark evaluate); Practice set Q5 | CF CH TF TH | ✓ |
| SOW: how deforestation increases the amount of carbon dioxide in the atmosphere | Start here; Card: Two reasons carbon dioxide rises (legacy-fig:fFig); Easy mistakes; Key fact; Rung 1; Rung 2; Rung 3; Practice set Q1, Q2 | CF CH TF TH | ✓ |
| SOW: deforestation leads to a reduction in biodiversity | Card: What happens to biodiversity; Key fact; Rung 2; Practice set Q4 | CF CH TF TH | ✓ |

**Gaps and mismatches.** None on the spec. The legacy page's eyebrow reads "AQA Biology 4.7.3.4" on every route; the number is right for both specs.

**Removed or moved.**
- Removed from the page: the hook, the three reason cards, the forest standing/cleared switch, the "select both reasons" and "why does decay release" checks, the gains-and-costs cards with the 2000 km² evaluate check, Think again, the reason-or-consequence sort, the video and the key-fact list. Their teaching is carried by the cards and the reveal table.
- Kept: the Design figure `fFig`, through `legacy-fig:fFig`. It had a switch; with the switch gone, a logic edit draws the cleared state, which shows the small photosynthesis arrow, burning and decay together. I rendered it and checked every arrow and label.
- Moved to Dive deeper: species lost before their value is known (medicines); cattle and rice fields give off methane (link to Global warming).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q2 (deforestation#r2-2): one distractor; Practice Q4 (quiz-CF-4, all routes): two distractors.
- New id (stem changed): None.

## Audit of the legacy ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (Give one reason tropical forest has been cleared) | ok | none |
| Rung 1 Q2 (Name the process by which trees take carbon dioxide out) | ok | none |
| Rung 2 Q1 (Explain why burning felled trees raises carbon dioxide) | ok | none |
| Rung 2 Q2 (Explain why clearing a forest reduces biodiversity) | ok | none |
| Rung 3 chain 1 (How deforestation raises carbon dioxide) | Fault: the three links were three parallel reasons (less photosynthesis, burning, decay), held in order only by "As well as that" and "Then". Any order is scientifically right, which breaks Mide's chain rule, and the chain component has no `orders` support in this worktree | logic_edits: prompt now "Explain how clearing a forest by cutting and burning the trees releases carbon dioxide into the atmosphere"; links now cut and burned → burning releases the stored carbon → microorganisms then decay what is left and release more. One forced order. Same position, same id. The photosynthesis reason stays in Rung 1 Q2, the cards and Practice set Q1 |
| Rung 3 chain 2 (Why felled wood left to rot releases carbon dioxide) | ok, one forced order | none |
| Rung 4 (Evaluate the 2000 km² biofuel plan, 6 marks) | ok | none |
| Practice set Q1 ("How does deforestation lead to LESS carbon dioxide…") | Fault: distractor "Deforestation increases the number of decomposers" is arguable (felled wood feeds decomposers); feedback had dashes | logic_edits: distractor now "Cattle on the cleared land take in carbon dioxide" with its own feedback; dash removed from feedback 2. Stem unchanged, id kept |
| Practice set Q2 ("…Why does decay release CO₂?") | Fault: distractor "Only burning releases CO₂ — decay does not" had a dash tail and contradicted the stem; feedback had dashes | logic_edits: distractor now "Decay releases oxygen, not carbon dioxide"; all three feedback lines rewritten without dashes. Stem unchanged, id kept |
| Practice set Q3 (Which is a reason large areas of tropical forest have been cleared?) | Fault: the right option (42 characters) was visibly the longest (others 18 to 24) | logic_edits: distractors now "To plant new forests in their place" / "To reduce the carbon dioxide in the air" / "To make more space for rare species". Stem unchanged, id kept |
| Practice set Q4 (Why does deforestation reduce biodiversity?) | Fault: the right option (81 characters) was visibly the longest | logic_edits: right option now "The habitats of many species are destroyed". Stem unchanged, id kept |
| Practice set Q5 (Give one benefit and one cost) | Fault: the right option (86 characters) was visibly the longest; "Benefit: lower carbon dioxide" is arguable for a biofuel | logic_edits: right option now "Benefit: fuel. Cost: habitat is lost"; that distractor now "Benefit: more habitat. Cost: less fuel". Stem unchanged, id kept |

No practice-set stem changed, so every practice-set id survives.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r2.1 (deforestation#r2-2): distractor now "The carbon dioxide from burning kills the animals". KEY CHANGE (distractor).
- EX2 MUST practice Q4 (quiz-CF-4): distractors now "Cattle on the cleared land eat the animals" and "Biodiversity is not affected by clearing". KEY CHANGE (distractors).
- EX4 NOTE r4.0 (deforestation#r4-1): judgement point now credits any reasoned judgement that weighs the 1% saving against the costs.
- EX3/EX5/EX6 NOTEs: no change (Q1/Q2 within tolerance; fFig kept; md sentence on spec-8461 corrected).
