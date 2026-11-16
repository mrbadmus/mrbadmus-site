# adaptations

Sources: AQA spec 4.7.1.4 Adaptations (and the 4.7.1.1 line "suggest how organisms are adapted to the conditions in which they live"), read from spec-8464.txt (CF CH) and spec-8461.txt (TF TH). Word for word the same in both, no HT-only or Biology-only lines. Rainford KS4 Biology Unit 7 lessons "Animal adaptations" and "Plant adaptations and extremophiles" (structural, behavioural and functional adaptations in a range of organisms; define extremophile and give general examples; key words extremophile, surface area, adaptation). LEGACY page (batch 10).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Explain how organisms are adapted to live in their natural environment, given appropriate information | Card: Explain an adaptation from information; Card: Keeping warm and keeping cool; Card: Plants in the desert; Rung 2; Rung 3 chain 2; Rung 4; Quiz Q2, Q4, Q5 | CF CH TF TH | ✓ |
| (4.7.1.1) Suggest how organisms are adapted to the conditions in which they live, given information | Card: Explain an adaptation from information; Rung 4; Quiz Q4 | CF CH TF TH | ✓ |
| Organisms have features (adaptations) that enable them to survive in the conditions in which they normally live | Card: What an adaptation is; Key fact; Start here | CF CH TF TH | ✓ |
| These adaptations may be structural, behavioural or functional | Card: What an adaptation is; Reveal: Three types of adaptation; Key fact; Easy mistakes; Rung 1 Q1; Rung 2 Q1; Quiz Q1, Q4 | CF CH TF TH | ✓ |
| Some organisms live in environments that are very extreme, such as at high temperature, pressure, or salt concentration. These organisms are called extremophiles | Card: Extremophiles (AQA's words); Key fact; Quiz Q3 | CF CH TF TH | ✓ |
| Bacteria living in deep sea vents are extremophiles | Card: Extremophiles; Key fact; Rung 1 Q2; Quiz Q3 | CF CH TF TH | ✓ |
| (SOW) surface area; plant adaptations | Card: Keeping warm and keeping cool; Card: Plants in the desert | CF CH TF TH | ✓ |

**Gaps and mismatches.** None in the spec lines. Rung 3 chain 1 (arctic hares) tests natural selection, which is 4.6.2 Evolution, not 4.7.1.4; the record teaches it in one short card, "Where adaptations come from", so the rung is answerable. Surface area to volume is used as an idea only; the calculation belongs to Transport in cells.

**Practice set source.** The page's own `BANK` (`BANK.map((q) => K.item(q))`), the same five on every route; it does not read the subtopic `quiz` list. Fixes are `logic_edits`. No quiz-adaptations.json. No stem edited, so all five IDs survive.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Type that is something it does | ok |
| Rung 1 Q2 Example of an extremophile | Fault: credited option visibly longest (+21); a reply said "in the spec's sense". Fix: "A polar bear living on Arctic ice" (reply "A polar bear is adapted to the cold, but it is not an extremophile."), "A rabbit living in a grassy field". |
| Rung 2 Q1 Jerboa, functional adaptation | ok |
| Rung 2 Q2 Large body, small ears | Fault: credited option visibly longest (+23). Fix: "It has a large surface area compared with its volume, so more heat is kept"; "Small ears hold more blood, so they store more heat"; replies adjusted to match. |
| Rung 3 chain 1 Arctic hares, white fur | ok. One forced order (variation, then survival and breeding, then many generations). |
| Rung 3 chain 2 Cactus | ok. One forced order: each link refers back to the one before ("that water", "the stored water"). |
| Rung 4 Camel, 4 marks | ok |
| Quiz Q1 Polar bear fur and blubber | ok (rendered labels are the four one-word types) |
| Quiz Q2 Fennec fox ears | Fault: "Large ears help the animal hear predators from further away" was arguable (its own feedback said hearing is enhanced too). Fix: "Large ears reduce the surface area for heat loss", feedback "Large ears give a large surface area, so more heat is lost, not less." Stem kept. |
| Quiz Q3 Deep sea vent bacteria | ok |
| Quiz Q4 Antarctic fish antifreeze | Fault: credited option visibly longest (+28). Fix: "It swims faster to keep warm; a behavioural adaptation" / "It is hidden against the ice; a structural adaptation" / "Its blood stays warmer than the water; a structural adaptation"; feedback kept. Stem kept. |
| Quiz Q5 Musk ox | ok |

**Removed or moved.**
- Removed: the type tap cards (now a reveal table); the two-foxes classifier (anFig and its eight feature buttons; the foxes are now one line in "Keeping warm and keeping cool"); the inline checks on extremophiles and the sand cat (the sand cat is now the worked "Explain an adaptation" card); the Think again choice (now an Easy mistake); the Sort; the Command words grid; the Key note; the video.
- Not kept: `tFig` (three boxes with small icons and the same words as the reveal table) and `anFig` (one fox at a time; at its first state only the Arctic fox shows). No figure is needed for this lesson.
- Added to Dive deeper: other extremophiles (hot springs, very salty lakes), in general terms only.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q1 (adaptations#r2-1): credited option; Rung 3 Q2, cactus chain (adaptations#r3-2): links and one herring; Practice Q4, Antarctic fish (quiz-CF-4, all routes): credited option.
- New id (stem changed): None.
- Rung prompts reworded, position kept (id kept): Rung 3 Q2 (adaptations#r3-2): prompt reworded.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r2.0 (adaptations#r2-1): credited option trimmed to "Concentrated urine". KEY CHANGE.
- EX2 SHOULD r3.1 (adaptations#r3-2): cactus chain rewritten in place as one causal chain (spines, smaller surface area, less water lost, keeps enough water); position kept. Changed the examiner's second herring ("The spines take up water from the air") to "The spines store water for the dry season", because some cactus spines do collect fog droplets, so the examiner's herring was not definitely wrong. KEY CHANGE.
- EX3 NOTE practice Q1 (quiz-CF-1): all three explanations rewritten plainly (examiner gave 1; 2 and 3 had the same caps/dash faults). Options unchanged.
- EX4 NOTE practice Q4 (quiz-CF-4): credited option trimmed to "Its blood does not freeze below 0 °C; a functional adaptation" (59 against 62). KEY CHANGE.
