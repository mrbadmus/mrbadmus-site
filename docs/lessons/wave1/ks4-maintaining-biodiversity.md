# maintaining-biodiversity

Sources: AQA spec 4.7.3.6, read from the 8464 and 8461 PDFs on Mide's Mac (also checked against spec-8461.txt in this folder, which holds this section). The content is word for word the same in 8464 and 8461, with no HT-only and no "(biology only)" line. Rainford KS4 Biology Unit 7 lesson "Biodiversity & maintaining biodiversity" (the five programmes, with rare habitats such as coral reefs, mangroves and heathland; explain and evaluate conflicting pressures). No required practical. Combined routes (CF, CH) use 8464. Triple routes (TF, TH) use 8461.

Legacy lesson (batch 10). The ladder and the practice set stay from the Design page with their ids. **The practice set is the `BANK` array written inside the legacy logic, not K.bank, so every practice-set fix is a `logic_edits` pair, and there is no quiz-maintaining-biodiversity.json.**

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Describe both positive and negative human interactions in an ecosystem and explain their impact on biodiversity | Reveal table: Human interactions that harm or help; Rung 3 chain 1; Practice set Q5 | CF CH TF TH | ✓ |
| Scientists and concerned citizens have put in place programmes to reduce the negative effects of humans on ecosystems and biodiversity | Card: The programmes; Key fact | CF CH TF TH | ✓ |
| Breeding programmes for endangered species | Card: The programmes; Easy mistakes; Rung 1; Rung 3 chain 2 | CF CH TF TH | ✓ |
| Protection and regeneration of rare habitats | Card: The programmes; Dive deeper: Examples of rare habitats | CF CH TF TH | ✓ |
| Reintroduction of field margins and hedgerows in agricultural areas where farmers grow only one type of crop | Start here; Card: The programmes; Card: Hedgerows and field margins (legacy-fig:hFig); Rung 2; Rung 4; Practice set Q1 | CF CH TF TH | ✓ |
| Reduction of deforestation and carbon dioxide emissions by some governments | Card: The programmes; Rung 2 | CF CH TF TH | ✓ |
| Recycling resources rather than dumping waste in landfill | Card: The programmes; Rung 3 chain 1; Practice set Q4 | CF CH TF TH | ✓ |
| WS 1.4, 1.5: evaluate given information about methods to tackle problems caused by human impacts; explain and evaluate the conflicting pressures on maintaining biodiversity | Card: Conflicting pressures; Dive deeper: Using data to evaluate; Rung 1 Q2; Rung 4 (6-mark evaluate); Practice set Q2, Q3 | CF CH TF TH | ✓ |

**Gaps and mismatches.** None on the spec.

**Removed or moved.**
- Removed from the page: the hook, the six harm-or-help switches, the with/without-hedgerows switch, the programme cards, the parrot check, the hedgerow evaluate check, Think again, the programme-or-pressure sort, the video and the key-fact list. Their teaching is carried by the reveal table and the cards.
- Kept: the Design figure `hFig`, through `legacy-fig:hFig`. It had a switch; with the switch gone, logic edits draw the farm with hedgerows and margins, replace the label "17 bird species" (a made-up count shown with no "made up" mark) with "one crop: wheat", and remove three unlabelled black marks in the wheat. I rendered it and checked it: hedgerow labelled, both field margins labelled, one-crop field labelled.
- Moved to Dive deeper: coral reefs, mangroves and heathland (SOW examples); a worked percentage change from the Rung 4 data (28 ÷ 400 × 100 = 7%).
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q1 (maintaining-biodiversity#r1-1): two distractors; Rung 1 Q2 (maintaining-biodiversity#r1-2): one distractor; Practice Q1 hedgerows (quiz-CF-1, all routes): credited option; Practice Q2 conflict (quiz-CF-2, all routes): credited option.
- New id (stem changed): None.

## Audit of the legacy ladder and practice set

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (Give one programme) | ok (right option 14 characters longer than the longest distractor, inside the limit) | none |
| Rung 1 Q2 (State one human need that conflicts with protecting a habitat) | Fault: distractor "Clean water" is arguable (reservoirs for water supply flood habitats) | logic_edits: distractor now "Recycling more waste", reply "Recycling helps biodiversity. It does not conflict with it." |
| Rung 2 Q1 (How field margins increase biodiversity) | Fault: right option visibly the longest (52 against 28 and 19); "They increase the crop yield" is arguable (margins hold pollinators and pest predators) | logic_edits: right option "They give wildlife food and shelter"; distractors "They let the farmer grow more of the crop" / "They remove all the pests from the farm", with replies |
| Rung 2 Q2 (Government reduces deforestation) | Fault: right option visibly the longest (47 against 29 and 20) | logic_edits: right option "Forest habitats and their species survive"; distractors "More land is cleared for cattle ranches" / "Carbon dioxide in the atmosphere rises", with replies |
| Rung 3 chain 1 (Landfill reduces biodiversity; how recycling helps) | ok, one forced order | none |
| Rung 3 chain 2 (Evaluate a village nature reserve) | Fault: an evaluation's gain and cost can come in either order, so two orders were scientifically right; only the word "But" forced one. The chain component has no `orders` support in this worktree | logic_edits: rewritten as "A zoo breeds an endangered bird and releases the young into the wild. Explain how this helps maintain biodiversity": breed in captivity, numbers rise → young released into a suitable habitat → wild population grows, less likely to become extinct. One forced order. Same position, same id. Evaluation stays in Rung 4 |
| Rung 4 (Evaluate the hedgerow scheme, 6 marks) | ok. Data checked: 9 to 17 species; 400 to 372 t is a 7% fall; £18 000 half paid by the government leaves £9 000 for the farmer | none |
| Practice set Q1 (hedgerows on a single-crop farm) | Fault: distractor "They increase the yield of the single crop" arguable; feedback dashes | logic_edits: distractor now "They let the farmer plant more of the single crop"; feedback 1 and 3 rewritten. Stem unchanged, id kept |
| Practice set Q2 (conservation conflict) | Feedback dashes only; options ok | logic_edits: feedback 2 and 3 without dashes. Stem and options unchanged, id kept |
| Practice set Q3 (town nature reserve, made-up data) | Fault: right option (95 characters) visibly the longest | logic_edits: right option "Species rose by 90, but 300 homes were not built" (210 − 120 = 90); distractors lengthened to match, with feedback. Stem unchanged, id kept |
| Practice set Q4 (How does recycling help) | Fault: right option (75) visibly the longest; "It increases carbon dioxide" arguable (recycling uses energy) | logic_edits: right option "Less land is used for landfill sites"; distractors "It provides food for endangered species" / "It removes all pollution from rivers" / "It makes hedgerows grow back on farms". Stem unchanged, id kept |
| Practice set Q5 (negative human interaction) | ok | none |

No practice-set stem changed, so every practice-set id survives.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r1.0 (maintaining-biodiversity#r1-1): distractors now "Clearing tropical forest to make new farmland", "Dumping more household waste in landfill". KEY CHANGE (distractors).
- EX2 MUST practice Q1 (quiz-CF-1): credited option now "They give food and shelter to more species". KEY CHANGE.
- EX3 MUST practice Q2 (quiz-CF-2): credited option now "Protecting a habitat leaves less land for farms". KEY CHANGE.
- EX4 SHOULD r4.0 (maintaining-biodiversity#r4-1): point now "a 7% fall in the harvest" (not income).
- EX5 SHOULD r1.1 (maintaining-biodiversity#r1-2): distractor now "More wild species living there". KEY CHANGE (distractor).
- EX6 NOTE r4.0: judgement point now credits any reasoned judgement.
- EX7 NOTE hFig: the two meaningless red dots removed (logic edit); figure renders.
