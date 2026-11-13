# farming-techniques

Sources: AQA 8461 4.7.5.2 Farming techniques (biology only), read from `~/Desktop/Rainford/Curriculum/AQA/AQA-8461-SP-2016.pdf` (also checked against the SCRATCH `spec-8461.txt`, which holds this section). 8461 4.6.3.7 for "the agricultural use of antibiotics should be restricted". Rainford SOW, Biology Unit 7, "Food production, farming techniques, sustainable fisheries". Routes: TF, TH only. No HT-only lines. No required practical.

Kind: LEGACY (batch 10). Ladder and practice set stay from the live page. The practice set is the hard-coded `BANK` in the legacy logic, so its fixes are `logic_edits`, not a quiz JSON.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| The efficiency of food production can be improved by restricting energy transfer from food animals to the environment | Card: Making food production more efficient; Key fact | TF TH | ✓ |
| This can be done by limiting their movement and by controlling the temperature of their surroundings | Reveal: Two ways to cut energy transfer; Key fact | TF TH | ✓ |
| Some animals are fed high protein foods to increase growth | Card: High-protein food | TF TH | ✓ |
| WS 1.3: understand that some people have ethical objections to some modern intensive farming methods | Reveal: Intensive farming: for and against; Key fact | TF TH | ✓ |
| WS 1.4: evaluate the advantages and disadvantages of modern farming techniques | Reveal: for and against; Card: Disease and antibiotics; Card: Evaluating a farming method | TF TH | ✓ |
| (4.6.3.7, linked) the agricultural use of antibiotics should be restricted | Card: Disease and antibiotics | TF TH | ✓ |

SOW rows: "Explain how restricting the movement of animals and controlling the temperature of their surroundings improves efficiency of food production" ✓; "Define the term factory farming and give examples of animals farmed in this way" ✓ (Card: Intensive farming: chickens in sheds, pigs indoors in pens); "Evaluate modern farming techniques" ✓.

## Audit of the kept ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (State two ways) | Science ok; the reply said "The spec’s two are…" | logic_edits: "The two ways are limiting movement and controlling temperature." |
| Rung 1 Q2 (Give one objection) | ok | |
| Rung 2 Q1 (warm shed vs outdoors in winter) | Credited option 90 characters against 31 and 32 | logic_edits: credited "It respires less to keep warm, so more feed becomes body mass"; distractors lengthened to the same idea |
| Rung 2 Q2 (fair disadvantage of the shed) | Credited option 64 characters against 20 and 33; "It is more expensive" relied on prices the prompt does not give | logic_edits: credited "The birds are crowded, so disease spreads faster"; distractors "It gives less meat from each kilogram of feed", "The birds move about more, so they respire more" |
| Rung 3 Q1 (chain: limiting movement) | ok; one forced order | |
| Rung 3 Q2 (chain: disease → antibiotics → resistance) | ok; one forced order. Taught in the new "Disease and antibiotics" card (4.6.3.7). | |
| Rung 4 (6-mark evaluate, shed vs free range) | ok; figures checked (2.0 vs 1.3 kg per 4 kg feed, £3 vs £6 per kg) | |
| Practice 1 "Why do some people have ethical objections to intensive farming of chickens?" | Credited option 136 characters ("physical and psychological suffering"), dash tails; egg quality, water use and greenhouse gases are each an arguable objection | Stem kept (id kept). logic_edits: credited "The chickens cannot behave naturally in crowded sheds"; distractors "…too much space in the shed", "…kept too cold in the winter", "The meat from the chickens costs more to buy", with new explanations |
| Practice 2 "Explain how keeping pigs in a heated shed improves…" | Credited option 117 characters against 19 to 40 | Stem kept. logic_edits: credited "They respire less to keep warm, so more feed becomes body mass"; distractors lengthened |
| Practice 3 (high-protein food) | ok | |
| Practice 4 (shed vs field cattle, made-up data) | Credited option 127 characters against 28 to 35 | Stem kept. logic_edits: credited "Shed cattle use less feed per kg, but need more antibiotics"; distractors lengthened. 1 kg per 6 kg feed beats 1 kg per 9 kg ✓ |
| Practice 5 "Why should the agricultural use of antibiotics be restricted?" | Credited option 67 against 24 to 38; "Antibiotics make animals grow too fast" is arguable (antibiotics have been used as growth promoters) | Stem kept. logic_edits: credited "To slow the development of resistant bacteria"; distractors "Antibiotics are a source of protein for animals", "Antibiotics would kill all the viruses on farms", "Antibiotics make the meat taste worse" |

Chains: both have one forced order; no `orders` needed.

**Gaps and mismatches.** The old generator page went well past 4.7.5.2: crop methods (pesticides, herbicides, fertilisers, greenhouses, monoculture), eutrophication, methane from cattle, organic farming, and a whole section on biological control (ladybirds, Bt, sterile insects). None of these is in 8461 4.7.5.2 (biological control and eutrophication appear nowhere in 8461), so none is carried over. Its line that antibiotics speed growth by "less energy lost to fighting infection" is not AQA's and is gone; the record uses 4.6.3.7's wording instead. The live Design page's interactive chicken figure (cFig) is not kept: it is drawn from a two-button toggle, so outside its section it would show only the indoor shed. The two-way comparison is now a reveal table, so no new figure is needed.

**Removed or moved.** Removed from the live page: the hook (replaced by Start here), video, the two-chicken toggle and figure, the "Why does limiting movement…" pick, the evaluation pick and its made-up data box (the same data is in Rung 4), the Ks4Choice "lazy?" (now an Easy mistakes line), the Ks4Sort (its content is the for-and-against reveal), the Key note, and the Command words block (moved to Dive deeper). The link to Transfer of biomass moved to Dive deeper.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q2 (farming-techniques#r1-2): two distractors; Rung 2 Q1 (farming-techniques#r2-1): two distractors; Practice Q1 (quiz-TF-1, TF TH): three distractors; Practice Q2 (quiz-TF-2, TF TH): three distractors.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r1.1 (farming-techniques#r1-2): distractors now "The meat is cheaper to buy in shops", "The animals grow faster on less feed". KEY CHANGE (distractors).
- EX2 MUST r2.0 (farming-techniques#r2-1): distractors now "It eats a lot more food, because it is bored in the warm shed", "The warm air in the shed gives it extra nutrients for growth" (edits #3–#4 new text). KEY CHANGE (distractors).
- EX3 MUST practice Q1 (quiz-TF-1): distractors now "The chickens have too much space to move about in the shed", "The chickens are kept much too cold during the winter", "The meat from the chickens costs a lot more to buy" (edits #9–#11). KEY CHANGE (distractors).
- EX4 MUST practice Q2 (quiz-TF-2): distractors now "The heat makes the pigs eat a lot more of their food each day", "Heat acts as a nutrient that helps the pigs to grow bigger", "Warm pigs move about more, so they build up more muscle mass" (edits #16–#18). KEY CHANGE (distractors).
- EX5/EX6 NOTEs: no change.
