# mixtures

Sources: AQA 8464 5.1.1.2 (CF, CH) and 8462 4.1.1.2 (TF, TH), word for word the same. No HT-only or "(chemistry only)" lines. AT 4 (safe use of equipment to separate mixtures). No required practical.

Old page: Design batch-3 (`mixtures.dc.html`), family Classify, routes CF CH TF TH. **Practice set = the route's subtopic `quiz` list via `K.bank(slug, R.route)`; no K.find.** Rung 2 differs for Higher and Foundation. The practice-set fixes and two new items are quiz-data edits in `all_subtopics_chemistry*.py` (all four routes carry the same items; `patches/_subtopic_edits_a.json`). The eyebrow is bound per route by the page's own logic (5.1.1.2 / 4.1.1.2).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| A mixture consists of two or more elements or compounds not chemically combined together | Card 'What a mixture is'; Key fact; Rung 1 | CF CH TF TH | ✓ |
| The chemical properties of each substance in the mixture are unchanged | Card 'What a mixture is'; Easy mistakes; Start here; practice Q4 (new) | CF CH TF TH | ✓ |
| Mixtures can be separated by physical processes such as filtration, crystallisation, simple distillation, fractional distillation and chromatography | Reveal 'Choosing a method'; cards 'Filtration' (fig:mix-filtration), 'Crystallisation' (fig:mix-crystallisation), 'Simple distillation' (fig:mix-simple-distillation), 'Fractional distillation' (fig:mix-fractional-distillation), 'Chromatography' (fig:chromatogram) | CF CH TF TH | ✓ |
| These physical processes do not involve chemical reactions and no new substances are made | Card 'What a mixture is'; Easy mistakes; Key fact | CF CH TF TH | ✓ |
| Describe, explain and give examples of the specified processes of separation | The five technique cards; card 'A soluble solid mixed with sand'; Rung 3; Rung 4; practice Q1, Q3, Q5 | CF CH TF TH | ✓ |
| Suggest suitable separation and purification techniques for mixtures when given appropriate information | Reveal 'Choosing a method'; Rung 2; practice Q1, Q5 | CF CH TF TH | ✓ |
| AT 4: safe use of a range of equipment to separate chemical mixtures | Figures; Dive deeper 'Setting up a distillation', 'Why not boil it dry' | CF CH TF TH | ✓ |

**Misconceptions taught against (Easy mistakes).** A fine enough filter paper catches dissolved salt; evaporating salt water collects the water; separating a mixture makes new substances.

**Gaps and mismatches.** None in the content lines. Practice Q2 is an Rf calculation, which is 5.8.1.3 / 4.8.1.3 (Chromatography, all four routes), not this spec point. It is kept (its id is a child's saved answer) and the chromatography card names the Chromatography lesson.

**Practice set source.** Subtopic quiz list, three items, identical on all four routes; two added, so the set is five on every route.

**Audit of the ladder and practice set (faults found and fixed).**
- Quiz Q1 (pure water from seawater): the credited label "Simple distillation" was the longest of four technique names; "Chromatography" is replaced by "Fractional distillation" (a real confusion: two kinds of distillation). Replies rewritten without capitals or dashes. Stem kept.
- Quiz Q2 (Rf): replies shouted "WRONG WAY". Rewritten with the working, 4.5 ÷ 9.0 = 0.50. Stem and options kept.
- Quiz Q3 (crude oil): credited label "Crude oil contains many liquids ..." was the longest (61 against 59). Now "It is a mixture of many liquids with different boiling points" (61) and the energy distractor is 67. Replies rewritten. Stem kept.
- **Added** quiz Q4 "Salt is stirred into water until it dissolves. Which statement is correct?" (new id `ks4q:mixtures:18c89cf708`): "chemical properties unchanged" had no practice item.
- **Added** quiz Q5 "A student wants dry crystals of copper sulfate from copper sulfate solution. Which technique should they use?" (new id `ks4q:mixtures:9c3e3aac30`): crystallisation had no practice item.
- Rung 1 (meaning of mixture): credited option the longest (67 against 61, 57, 61). Two distractors reworded by logic edits (70 and 68). Same answer.
- Rung 3 (ethanol and water): links 2 and 3 could be swapped. Link 3 now starts "So a fractionating column is used instead". One order.
- Rung 2 (both versions) and Rung 4: checked, no fault. Methanol boils at 65 °C and ethanol at 78 °C (64.7 and 78.4), close together, so fractional distillation.

**Old subtopic data.** spec "5.1.1.2" ✓. Its `key_note` lines are read by the Design logic for the key note, which is not on the lean page.

**Unsure (left out until checked).** Whether Mide wants the Rf item (Q2) kept here or retired in favour of the Chromatography lesson; kept for now because its id is live.

**Removed or moved.**
- Design benches: the separation desk (six mixtures), Think again (fine filter paper), Build the method chain, Set up the apparatus (spot the thermometer fault), the command-word list, and the fractional distillation lab paragraph: off the page. Their teaching is in the five technique cards, the method card and Easy mistakes.
- Thermometer position, condenser water, anti-bumping granules, not boiling dry: Dive deeper.
- Command words: Dive deeper.

**Words.** Design page about 2,068 (approximate: template text plus the desk's strings in the logic, an over-count); lean teaching text 528, plus 134 in Dive deeper.

**Examiner fix round (26 Nov 2026).**
- M1: card 'Chromatography' now ends 'Rf = distance moved by substance ÷ distance moved by solvent. In the diagram, Rf = 3.6 ÷ 8.0 = 0.45.' (the chromatogram figure draws the solvent front at 8.0 cm and the lane B spot at 3.6 cm; 3.6 ÷ 8.0 = 0.45). Practice Q2 uses 4.5 and 9.0 cm, so the card does not answer it. 'Chromatography has its own lesson' removed.
- S9: the credited options of practice Q1, Q2, Q3 and Q5 start their feedback tail with a capital (Q2's 'Rf' already did). Stems and ids unchanged.
