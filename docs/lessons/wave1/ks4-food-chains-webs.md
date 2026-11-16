# food-chains-webs

Sources: AQA spec 4.7.2.1 Levels of organisation (producers, food chains, consumers, predators and prey), read from spec-8464.txt (CF CH) and spec-8461.txt (TF TH). Word for word the same in both for these lines, no HT-only line. Rainford KS4 Biology Unit 7 lesson "Levels of organisation" (explain what a food web shows and the interdependence of organisms; photosynthetic organisms are the producers of biomass; identify producers, primary, secondary and tertiary consumers; key words tertiary, trophic level, producer). LEGACY page (batch 10). The quadrat, transect and mean/mode/median lines of 4.7.2.1 are in Sampling techniques; the predator–prey cycle lines are in Population and competition.

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Photosynthetic organisms are the producers of biomass for life on Earth | Card: Producers | CF CH TF TH | ✓ |
| Feeding relationships within a community can be represented by food chains | Card: Food chains (legacy-fig:chFig) | CF CH TF TH | ✓ |
| All food chains begin with a producer which synthesises molecules. This is usually a green plant or alga which makes glucose by photosynthesis | Card: Producers; Reveal: A pond food chain; Key fact; Easy mistakes; Rung 1 Q1; Quiz (shared) Q3 | CF CH TF TH | ✓ |
| Producers are eaten by primary consumers, which in turn may be eaten by secondary consumers and then tertiary consumers | Card: Food chains; Reveal: A pond food chain; Quiz Q5 (Combined) | CF CH TF TH | ✓ |
| Consumers that kill and eat other animals are predators, and those eaten are prey | Card: Predators and prey | CF CH TF TH | ✓ |
| (SOW) what a food web shows and the interdependence of organisms | Card: Food webs (legacy-fig:wFig); Card: Follow the arrows; Key fact; Easy mistakes; Start here; Rung 2 Q1; Rung 3; Rung 4; Quiz (shared) Q1, Q4 | CF CH TF TH | ✓ |
| (8461 4.7.4.1, 4.7.4.3, biology only) trophic levels numbered from level 1, producers; only approximately 10% of the biomass from each trophic level is transferred to the level above it | Dive deeper: Trophic levels (routes TF TH); Quiz Triple Q1 | TF TH | ✓ |

**Gaps and mismatches.** The arrow convention (from the food to the eater, the direction biomass is transferred) is not written in the spec but every mark scheme credits it, so it stays. The Triple-only lines are 8461 4.7.4 Trophic levels in an ecosystem (biology only), checked in the full re-extracted spec-8461.txt: 4.7.4.1 numbers the trophic levels from level 1 (plants and algae, producers), and 4.7.4.3 says "Only approximately 10 % of the biomass from each trophic level is transferred to the level above it." They sit in Dive deeper on TF and TH only, as the legacy page had them, because the Triple practice-set Q1 tests them; they are taught in full in Trophic levels and Transfer of biomass.

**Practice set source.** The page's own `BANK`, route-aware: Triple routes get Triple Q1 + the four shared items; Combined routes get the four shared items + Combined Q5. It does not read the subtopic `quiz` list. Fixes are `logic_edits`. No quiz-food-chains-webs.json. No stem edited, so all six IDs survive.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Start of every food chain | ok |
| Rung 1 Q2 What the arrows show | ok |
| Rung 2 Q1 Rabbits killed, effect on foxes | ok |
| Rung 2 Q2 Oak leaves chain, arrows reversed | Fault: credited option visibly longest (+34). Fix: "Put the sparrowhawk first and the oak leaves last"; "Remove the oak leaves and start with the caterpillar"; replies kept. |
| Rung 3 chain 1 Foxes die, effect on grass | ok. One forced order. |
| Rung 3 chain 2 Herons leave, water fleas | ok. One forced order. |
| Rung 4 Grasshoppers die out, 4 marks | ok |
| Quiz Triple Q1 Why chains are short | Fault: used "energy" where the Triple spec uses biomass; "Producers cannot support more than 4 levels of consumers" was arguable; feedback said "thermodynamic" and "cognitive". Fix: "Only about 10% of the biomass passes to each next level" ✓ / "Top predators are too large to find enough food" / "Longer food chains would have too many predators" / "Producers can only be eaten by four kinds of animal", plain feedback. Stem kept. |
| Quiz shared Q1 Foxes killed, the grass | ok for the options; feedback 1 was muddled ("reduced decomposition adds some nutrients"). Fix: "Fewer foxes means more rabbits survive, and more rabbits eat more grass, so the grass decreases." |
| Quiz shared Q2 Chain written backwards | Fault: credited option visibly longest (+48); "The grass should be at the end" and "The fox should be first" described what the pupil had already written. Fix: "The arrows point the wrong way" ✓ / "The grass should be in the middle" / "Nothing is wrong" / "The rabbit should be first", feedback adjusted. Stem kept. |
| Quiz shared Q3 Which can be a producer | ok |
| Quiz shared Q4 Shrews die out, owls | ok |
| Quiz Combined Q5 Secondary consumer | ok |

**Removed or moved.**
- Removed: the inline checks "What does the arrow mean?" and "Grasshoppers die out, what happens to the owls?"; the web change buttons and notes (one change, the foxes, is now the "Follow the arrows" card; the grasshopper change is not taught because Rung 4 asks exactly that); the Think again choice (now an Easy mistake); the Sort (now the pond-chain reveal table); the Command words grid; the Key note; the video.
- Moved: the Triple preview section (trophic levels and the 10% rule) is now a Dive deeper card on TF and TH.
- Kept: `legacy-fig:chFig` (grass, rabbit, fox, eagle with roles; on Triple routes it adds "level 1" to "level 4"; arrows from food to eater; checked against its drawer) and `legacy-fig:wFig` (the field web at its first state, "No change": grass to rabbits and grasshoppers, rabbits to foxes, grasshoppers to shrews, shrews to owls and to foxes; checked against its drawer, all arrows from food to eater).
- Not mine: the assignment-bank item `ks4-food-chains-webs-h13` is listed in docs/b2c/QUESTION-AUDIT.md (describes a drawn chain in words). It is not on this page; the lead handles it.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q1 (food-chains-webs#r2-1): one distractor; Practice producer item (Q3 on CF/CH, Q4 on TF/TH; blind id food-chains-webs#quiz-CF-3): three distractors.
- New id (stem changed): None.
- Rung prompts reworded, position kept (id kept): Rung 2 Q1 (food-chains-webs#r2-1): prompt no longer describes the web in words; asks for the most likely effect.
- Builder: `legacy-fig:chFig` must not show "level N" labels on CF/CH. A logic edit now makes `chFig` read the route itself unless it is given a boolean, so call `chFig()` with no argument (or with a state number), or pass `chFig(isTriple)`: `false` on CF/CH, `true` on TF/TH. Never pass `true` on CF/CH. Tested: CF draws no labels, TH draws four.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST practice Q3 CF/CH, Q4 TF/TH (quiz-CF-3, quiz-TF-4): distractors lengthened ("A rabbit in a field", "A fungus on a log", "An owl in a barn"); credited "Algae in a pond" kept. KEY CHANGE (distractors).
- EX2 SHOULD r2.0 (food-chains-webs#r2-1) + BLIND LOW r2-1: prompt now "Foxes eat rabbits and shrews. A disease kills most of the rabbits. Explain the most likely effect on the foxes." (no web described in words; "most likely" because foxes can switch to shrews). Distractor "Foxes are unaffected" became "Foxes are unaffected by the rabbits dying", reply "The foxes have lost part of their food." Position kept. KEY CHANGE.
- EX3 SHOULD card "Follow the arrows": legacy-fig:wFig moved from "Food webs" to the top of "Follow the arrows", so "In this web" points at it.
- EX4 SHOULD practice Q1 CF/CH, Q2 TF/TH (quiz-CF-1, quiz-TF-2): explanations 2 and 3 rewritten (no shouting, no mutualism). Options unchanged.
- EX5 NOTE / lead item 6 chFig: logic edit makes chFig read the route itself unless given a boolean (`if (typeof T !== 'boolean') T = this.flags().T;`). Tested: CF with no argument or 0 draws no "level N" labels; TH draws 4. Builder: call chFig() with no argument or pass chFig(isTriple), false on CF/CH; never pass true on CF/CH.
- EX6 NOTE r2.1 / Q2 arrow wording: no change (testing arrow direction needs it).
