# environmental-change (LEGACY, batch 10)

Sources: AQA 8461 4.7.2.4 "Impact of environmental change (biology only) (HT only)", read from the spec PDF. 8464 has no such section; the page exists only on TH, which matches the spec exactly, so no route gating is needed. Rainford SOW lesson "Impact of environmental change".

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Evaluate the impact of environmental changes on the distribution of species in an ecosystem given appropriate information | Card: Evaluating given information; Easy mistakes; Rung 2 Q1; Rung 3 Q2; Rung 4; Practice 2, 3, 4 | TH | ✓ |
| Environmental changes affect the distribution of species in an ecosystem | Cards: Three environmental changes, How a species can respond; Key fact; Start here; Rung 3 Q1 | TH | ✓ |
| These changes include temperature, availability of water, composition of atmospheric gases | Cards: Three environmental changes, An example of each change; Key fact; Rung 1 Q1; Rung 2 Q2; Practice 5 | TH | ✓ |
| The changes may be seasonal, geographic or caused by human interaction | Reveal: Three kinds of cause; Easy mistakes; Key fact; Rung 1 Q2 | TH | ✓ |

**Practice set source.** The practice set is the `BANK` array written in the legacy logic (five items). It does not read the subtopic `quiz` list, so every fix is a `logic_edits` pair and there is no quiz-environmental-change.json. BANK item 1 is the old subtopic quiz question 2; the old mayfly question 1 was already rewritten as BANK item 2 on the live page.

**Audit of every legacy rung and practice item.**

| Item | Verdict | Fix |
|---|---|---|
| Rung 1 Q1 (state the three changes) | Distractor "Light, soil pH, wind" is arguable: they are abiotic factors that can also change a distribution. The writer's replacement "Seasonal changes, geographic changes and human interaction" uses the spec's own words, so a pupil can defend it (blind check, HIGH). Credited option visibly the longest | logic_edits: credited option "Temperature, availability of water and atmospheric gases" (why line keeps the full spec wording); distractors "Photosynthesis, respiration and decay by microorganisms" and three trophic levels. Key change |
| Rung 1 Q2 (the three kinds of cause) | Distractor "Natural, artificial, random" is arguable (human interaction is artificial), and its reply "Not the spec's terms" teaches nothing | logic_edits: replaced with "Temperature, water, atmospheric gases" (the changes, not the causes) |
| Rung 2 Q1 (butterfly 11 → 21 squares) | Credited option visibly the longest (75 against 13 and 15 characters) | logic_edits: two same-shape distractors |
| Rung 2 Q2 (lichen and sulfur dioxide) | Credited option the longest (30 against 14 and 9) | logic_edits: distractors lengthened, same meaning |
| Rung 3 Q1 (chain, was fertiliser, algae, oxygen, fish) | Tested eutrophication, which the lean page does not teach and which is not in 4.7.2.4 (examiner MUST FIX; blind MED) | logic_edits, same position (id kept): "As the climate warms, a butterfly is now found further north than before. Explain why." Links: warming raises temperatures; places further north become warm enough; it spreads there, so its distribution extends north. One forced order. Key change |
| Rung 3 Q2 (chain: evaluate a northward spread) | Two orders were defensible: data first, or claim first (blind MED) | logic_edits, same position: each link now refers back to the one before ("This suggests…", "To test those other factors…"), so only data, interpretation, further data is right. Key change |
| Rung 4 (river flow and fish, evaluate) | ok; data self-contained | none |
| Practice 1 (UK birds breeding earlier) | Credited option 104 characters with a dash tail; distractor "Birds have evolved…" is arguable (some change in breeding time may be evolutionary) | logic_edits: question text kept (ID kept); options "Rising spring temperatures" ✓ / "Selective breeding by conservationists" / "Shorter days in spring" / "Colder winters"; feedback rewritten |
| Practice 2 (mayfly larvae below a farm pipe) | Credited option 106 characters against at most 40. Then (examiner, blind MED): "Oxygen is probably too low below the pipe" claims more than the data show, since anything below the pipe that kills them would give the same result | logic_edits: question text kept (id kept); "Low oxygen below the pipe could explain it, but is not proven" ✓; distractors "The farm is definitely poisoning the river with toxic chemicals", "Mayflies have evolved to avoid water near farms", "Nothing at all can be concluded from this information". Key change |
| Practice 3 (mountain plant 200 m uphill) | Credited option 63 against at most 29; distractor "The temperature had no effect" cannot be judged from the data either way. After the first fix the credited option was still the longest by 9 | logic_edits: question text kept; "Its range moved about 200 m uphill" ✓ with same-shape distractors. Key change |
| Practice 4 (oak, caterpillar, bird timing) | Credited option 84 against at most 50 | logic_edits: question text kept; "Fewer chicks survive, as the caterpillars peak too early" ✓, same-length distractors |
| Practice 5 (a change in atmospheric gases) | Credited option 62 against at most 27 | logic_edits: question text kept; "More sulfur dioxide in the air" ✓ |
| Figure mFig | Not used: it is a 1980/2020 toggle, and the lean page has no toggle, so it would only ever show 1980 | none needed: the rungs that use the data carry it in their text |

**Gaps and mismatches.** None in the legacy page's spec coverage.

**Removed or moved.** Removed with the legacy body: the hook, the six tap cards, the swallow pick, the butterfly map with its two evaluation picks, the river and lake information boxes with their picks, the "Think again" and the sort. Their teaching is carried by the cards (three changes, the causes reveal table with examples, how species respond, an example of each change, the five-step evaluation). The Command words box moved to Dive deeper.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 1 Q1 (environmental-change#r1-1): credited option and one distractor; Rung 3 Q1 (environmental-change#r3-1): links and herrings (new chain); Rung 3 Q2 (environmental-change#r3-2): links; Practice Q2, mayfly (quiz-TH-2): all four options; Practice Q3, mountain plant (quiz-TH-3): credited option.
- New id (stem changed): None.
- Rung prompts reworded, position kept (id kept): Rung 3 Q1 (environmental-change#r3-1): prompt now the butterfly; Start here (environmental-change#start): question and both options replaced (now about distribution).

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- BLIND HIGH r1-1 + EX2 MUST r1.0 (environmental-change#r1-1): distractor A (spec's own words for the kinds of cause) replaced by "Photosynthesis, respiration and decay by microorganisms"; credited option shortened to "Temperature, availability of water and atmospheric gases" (56 against 55 and 52; why line keeps the full spec wording). Not the examiner's lengthened distractor, which kept the spec words the blind solver could defend. KEY CHANGE.
- EX1 MUST r3.0 (environmental-change#r3-1) + BLIND MED r3-1: eutrophication chain replaced in place by the examiner's butterfly chain (warming, north becomes suitable, distribution extends north); herrings "The butterfly evolves to live in the cold", "Places further south become colder". Position kept. KEY CHANGE.
- BLIND MED r3-2 (environmental-change#r3-2): links rewritten so each refers back to the one before ("This suggests…", "To test those other factors…"); only data, then interpretation, then further data now works. Position kept. KEY CHANGE.
- EX3 MUST practice Q2 + BLIND MED quiz-TH-2: key now "Low oxygen below the pipe could explain it, but is not proven" (the absence does not show low oxygen); distractors "The farm is definitely poisoning the river with toxic chemicals", "Mayflies have evolved to avoid water near farms", "Nothing at all can be concluded from this information", replies rewritten to match. Stem kept (id kept). KEY CHANGE.
- EX4 MUST practice Q3 (quiz-TH-3): credited option now "Its range moved about 200 m uphill". KEY CHANGE.
- EX5 SHOULD Start here (environmental-change#start): now hooks distribution: "If you had to guess, as the UK has warmed, have many species been found further north or further south than before?" Further north / Further south, same reply. NEW TEXT.
- EX6 NOTE r3.1 order, EX7 NOTE timing card: superseded by r3-2 rewrite / kept.
