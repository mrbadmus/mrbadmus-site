# abiotic-biotic-factors

Sources: AQA spec 4.7.1.2 Abiotic factors and 4.7.1.3 Biotic factors, read from spec-8464.txt (CF CH) and spec-8461.txt (TF TH). Word for word the same in both, no HT-only or Biology-only lines. Rainford KS4 Biology Unit 7 lesson "Ecosystems, biodiversity, biotic and abiotic factors" (name abiotic factors and explain how a change affects a community) and "Competition and interdependence" (name biotic factors). LEGACY page (batch 10).

| Spec statement | Where it is covered | Route | Ticked |
|---|---|---|---|
| Explain how a change in an abiotic factor would affect a given community given appropriate data or context | Reveal: How each abiotic factor affects organisms; Card: Explain a change from data; Rung 2 Q1; Rung 3 chain 1; Rung 4; Quiz Q1, Q3, Q4 | CF CH TF TH | ✓ |
| Abiotic factors: light intensity; temperature; moisture levels; soil pH and mineral content; wind intensity and direction; carbon dioxide levels for plants; oxygen levels for aquatic animals | Card: Abiotic factors (the list, in AQA's words); Reveal; Key fact; Easy mistakes; Start here; Rung 1 Q2 | CF CH TF TH | ✓ |
| Extract and interpret information from charts, graphs and tables relating to the effect of abiotic factors (MS 2c, 4a) | Card: Explain a change from data; Rung 2 Q1; Rung 4; Quiz Q3 | CF CH TF TH | ✓ |
| Explain how a change in a biotic factor might affect a given community given appropriate data or context | Reveal: How each biotic factor affects a community; Rung 2 Q2; Rung 3 chain 2; Quiz Q2, Q5 | CF CH TF TH | ✓ |
| Biotic factors: availability of food; new predators arriving; new pathogens; one species outcompeting another so the numbers are no longer sufficient to breed | Card: Biotic factors (the list, in AQA's words); Reveal; Key fact; Easy mistakes; Rung 1 Q1 | CF CH TF TH | ✓ |
| Extract and interpret information relating to the effect of biotic factors (MS 2c, 4a) | Rung 2 Q2; Rung 3 chain 2; Quiz Q5 | CF CH TF TH | ✓ |

**Gaps and mismatches.** None in the legacy page's coverage of the lists. The legacy page's data section used the factory-stream data that Rung 4 also uses; the record's data card uses the hedge light data instead, so Rung 4 is not answered on the page. "A pathogen is a microorganism that causes disease" follows AQA 4.3.1.1 ("Pathogens are microorganisms that cause infectious disease").

**Practice set source.** The page's own `BANK` (`BANK.map((q) => K.item(q))`), the same five on every route; it does not read the subtopic `quiz` list. Fixes are `logic_edits`. No quiz-abiotic-biotic-factors.json. No stem edited, so all five IDs survive.

**Audit of the ladder and practice set.**

| Item | Verdict |
|---|---|
| Rung 1 Q1 Which is biotic | ok |
| Rung 1 Q2 Abiotic factor for aquatic animals | Fault: "the abiotic factor that matters most for aquatic animals" is arguable (temperature also matters a lot). Fix: prompt "Name the abiotic factor in water that fish need for respiration."; Carbon dioxide reply "Respiration uses oxygen. Carbon dioxide levels are listed for plants." Same credited option. |
| Rung 2 Q1 Dry summer, soil moisture | Fault: credited option visibly longest (+28). Fix: "A new predator arrived and ate most of the meadow plants"; "The plant species are the abiotic factor that fell"; replies kept. |
| Rung 2 Q2 Mink and water voles | ok |
| Rung 3 chain 1 Fertiliser, oxygen, fish | ok. One forced order. |
| Rung 3 chain 2 Grey and red squirrels | ok. One forced order. |
| Rung 4 Factory stream, 4 marks | ok |
| Quiz Q1 Polluted river, oxygen | Fault: stored option "Disease — bacteria cause the oxygen to fall" carries a claim that is true of sewage pollution. Fix: the option is now just "Disease" (its feedback already says disease is biotic). Rendered labels unchanged in kind. |
| Quiz Q2 Grey squirrels | Fault: the two "Biotic" options turned on "interspecific"/"intraspecific", which this lesson does not teach; feedback in capitals with "=" shorthand. Fix: "Biotic: competition between two different species" ✓ / "Abiotic: the grey squirrels changed the temperature" / "Biotic: competition within one species" / "Abiotic: the grey squirrels changed the soil", plain feedback. Stem kept. |
| Quiz Q3 Warm pond | Fault: credited option visibly longest (+22). Fix: "The fish made heat that warmed the pond water"; "The fish are the abiotic factor that changed"; feedback kept. |
| Quiz Q4 Trees lean away from the sea | Fault in feedback: "trees have no predators of that kind" is untrue. Fix: "A predator is biotic, and it would not make trees lean one way." |
| Quiz Q5 Ash trees and a new fungus | ok |

**Removed or moved.**
- Removed: the tap cards (now a card plus a reveal table for each list); the inline checks "Which biotic factor is a new disease?", the stream question and the hedge question (the hedge data is now the data card); the Think again choice; the Sort (abiotic or biotic, which only repeated the two lists); the Command words grid; the Key note; the video.
- Not kept: `aFig`. It is a drawn text list of the same eleven factors, so it repeats the cards word for word.
- Added to Dive deeper: measuring abiotic factors (light meter, thermometer, pH), with a pointer to Sampling techniques.
- Key changes (13 Nov fixes): these options were reworded with no `{stored}` text, so their answers get new keys, which the knowledge-point top-up re-places. Rung 2 Q1 (abiotic-biotic-factors#r2-1): credited option; Practice Q3, pond warms (quiz-CF-3, all routes): credited option; Practice Q4, trees lean (quiz-CF-4, all routes): distractors.
- New id (stem changed): None.

**Fixes after the examiner and blind checks (13 Nov).** One line per finding (EX = examiner item number in EXAMINER.md, BLIND = blind/notes.md). Where this list and an audit row above disagree, this list is current.

- EX1 MUST r2.0 (abiotic-biotic-factors#r2-1): credited option now "The soil was drier, so fewer plant species survived". KEY CHANGE.
- EX2 MUST practice Q3 (quiz-CF-3): credited option now "Warm water held less oxygen, so fish died" (41 against 45; shorter than the examiner's 51-character text, which was still 6 longer). KEY CHANGE.
- EX3 MUST practice Q4 (quiz-CF-4): every distractor in AQA's phrasing ("Soil pH and mineral content", "New predators arriving", "Oxygen levels for aquatic animals"); replies 1 and 3 extended to cover the new words. KEY CHANGE (distractors only; credited text kept).
- EX4 SHOULD practice Q1 (quiz-CF-1): three explanations rewritten plainly; options unchanged.
