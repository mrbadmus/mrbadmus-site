# population-competition

Sources: AQA spec 4.7.1.1 Communities (competition) and 4.7.2.1 Levels of organisation (predators, prey and their cycles), read from spec-8464.txt (CF CH) and spec-8461.txt (TF TH). The two specs are word for word the same for these lines, with no HT-only or Biology-only lines. Rainford KS4 Biology Unit 7 lesson "Competition and interdependence" (describe resources plants and animals compete for; key words intraspecific, interspecific, interdependence) and "Levels of organisation" (interpret population curves: hare and lynx, red and grey squirrels, native and American crayfish). LEGACY page (batch 10).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe the importance of competition in a community | Card: Within and between species (grey and red squirrels); Card: What limits a population; Rung 3 chain 2 | CF CH TF TH | ✓ |
| Suggest the factors for which organisms are competing in a given habitat (given information) | Card: Suggest what they compete for; Rung 2 Q2; Quiz Q4 | CF CH TF TH | ✓ |
| Plants in a community or habitat often compete with each other for light and space, and for water and mineral ions from the soil | Card: What plants compete for (legacy-fig:cFig); Key fact; Easy mistakes; Start here; Rung 1 Q1 | CF CH TF TH | ✓ |
| Animals often compete with each other for food, mates and territory | Card: What animals compete for; Key fact; Easy mistakes | CF CH TF TH | ✓ |
| Consumers that kill and eat other animals are predators, and those eaten are prey | Card: Predators and prey | CF CH TF TH | ✓ |
| In a stable community the numbers of predators and prey rise and fall in cycles | Card: Predators and prey (legacy-fig:gFig); Key fact; Rung 3 chain 1; Rung 4; Quiz Q1 | CF CH TF TH | ✓ |
| Interpret graphs used to model these cycles (WS 1.2, MS 4a) | Card: Reading a predator–prey graph; Rung 2 Q1; Quiz Q3 | CF CH TF TH | ✓ |
| MS 2c, 4a: extract and interpret information from charts, graphs and tables relating to the interaction of organisms within a community | Card: Reading a predator–prey graph; Rung 2 Q1; Quiz Q3 | CF CH TF TH | ✓ |
| (4.7.1.3, taught in full in Abiotic and biotic factors) one species outcompeting another so the numbers are no longer sufficient to breed | Card: Within and between species; Rung 3 chain 2; Quiz Q2 (red and grey squirrels) | CF CH TF TH | ✓ |
| (SOW) intraspecific and interspecific competition (terms only) | Card: Within and between species | CF CH TF TH | ✓ |
| (SOW) red and grey squirrels; native and American crayfish | Card: Within and between species; Dive deeper: Native and American crayfish | CF CH TF TH | ✓ |

**Gaps and mismatches.** "Intraspecific" and "interspecific" are Rainford SOW key words, not AQA spec words; they stay in one card as terms only. Practice-set Q2 used to assert that intraspecific competition is more intense than interspecific; that is not in 8464 or 8461 4.7, so the item was replaced (see below). "What limits a population" is not a separate AQA statement: it is the biotic factors (food, predators, pathogens) plus water and space; it stays because Rung 1 Q2 and Quiz Q5 test it.

**Practice set source.** The page's own `BANK` (`BANK.map((q) => K.item(q))`), the same five on every route; it does not read the subtopic `quiz` list. Fixes are `logic_edits`. No quiz-population-competition.json. Q2 is replaced (new id, see below); the other four stems are unchanged, so their ids survive.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Two things plants compete for | ok |
| Rung 1 Q2 Disease and population | ok |
| Rung 2 Q1 Mice and owls peaks | ok |
| Rung 2 Q2 Marram grass | Fault: credited option visibly longest (+27). Fix: distractors "Food from the other plants", "Territory and nest sites"; replies kept. |
| Rung 3 chain 1 Predators fall after prey | ok. One forced order. |
| Rung 3 chain 2 Grey and red squirrels | ok. One forced order. |
| Rung 4 Predator–prey cycle, 4 marks | ok |
| Quiz Q1 Predator peak after prey peak | ok for the options (rendered labels are short and the credited one is not the longest). Feedback 3 rewritten: "Predators do not need to move away. Their numbers rise later because they take time to breed." |
| Quiz Q2 Intraspecific more intense | Fault: the stem states an off-spec generalisation as fact (not in 8464 or 8461 4.7; blind HIGH), and no change to the options can remove a premise in the stem. Fix: whole item replaced by "Grey squirrels moved into a wood where red squirrels live. Both eat the same nuts. Suggest why the number of red squirrels fell." ✓ "The grey squirrels competed with them for food". New id |
| Quiz Q3 Lag between peaks | ok |
| Quiz Q4 Pondweed competes for | Fault: credited option visibly longest (+17). Fix: "Food from the soil" / "Mates and territory" / "The newts and frogs"; stem kept. |
| Quiz Q5 What limits rabbits | ok |

**Removed or moved.**
- Removed: the tap cards (CC, LC) as separate widgets, now cards; the hedgerow inline check (now the worked "Suggest" card); the year buttons on the graph and their notes; the inline checks "Why does the predator peak come later?" and "What happens to the lynx?"; the Think again choice; the Sort; the Command words grid; the Key note; the video.
- Kept: `legacy-fig:cFig` (plants compete for light, space, water and mineral ions; animals for food, mates, territory; checked against its drawer, matches the spec lists) and `legacy-fig:gFig` (hare and lynx graph, drawn at year 0). Checked against its drawer: hare curve peaks at year 2, lynx curve peaks at year 3.5, a dashed line at each peak and a "lag" arrow between them; legend hares (prey) green, lynx (predator) red. At year 0 the blue year-marker sits on the y-axis; harmless.
- Added to Dive deeper: native and American crayfish (SOW example).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q2 (population-competition#r2-2): credited option.
- New id (stem changed): Practice Q2 (population-competition#quiz-CF-2, all routes): whole item replaced; new stem "Grey squirrels moved into a wood where red squirrels live. Both eat the same nuts. Suggest why the number of red squirrels fell.".
- Builder: `legacy-fig:gFig` now sits in the card "Reading a predator–prey graph". If it can, render it without the year-0 cursor line.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- BLIND HIGH quiz-CF-2 + EX3 SHOULD Q2: the stem itself asserts the off-spec premise (intraspecific more intense), so no option fix could make it on-spec. Whole item replaced: "Grey squirrels moved into a wood where red squirrels live. Both eat the same nuts. Suggest why the number of red squirrels fell." Key: "The grey squirrels competed with them for food" (4.7.1.1 animals compete for food; 4.7.1.3 one species outcompeting another; SOW red/grey squirrels). NEW ID. The writer's two earlier Q2 option edits are removed (superseded).
- EX1 MUST r2.1 (population-competition#r2-2): credited option trimmed to "Water and mineral ions". KEY CHANGE.
- EX2 SHOULD practice Q1 (quiz-CF-1): explanations 1 and 2 rewritten plainly; options unchanged.
- EX4 SHOULD card "Reading a predator–prey graph": legacy-fig:gFig moved into this card after its first line, so "this graph" points at it.
- EX5 NOTE gFig cursor: builder note (render without the year-0 cursor if it can). EX6 NOTE cFig: kept.
