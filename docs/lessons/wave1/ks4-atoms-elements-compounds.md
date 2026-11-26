# atoms-elements-compounds

Sources: AQA 8464 5.1.1.1 (CF, CH) and 8462 4.1.1.1 (TF, TH), word for word the same. One HT-only line ("write balanced half equations and ionic equations where appropriate"), taught on CH and TH only. No "(chemistry only)" lines. No required practical.

Old page: Design batch-2 (`atoms-elements-compounds.dc.html`), family Classify, routes CF CH TF TH. **Practice set = the route's subtopic `quiz` list via `K.bank(slug, R.route)`; Rung 1 = `K.find(slug, route, 'Which of these is a mixture')`, falling back to `'key difference between a compound and a mixture'`.** So the practice-set fixes are quiz-data edits in `all_subtopics_chemistry*.py` (all four routes carry the same items; `patches/_subtopic_edits_a.json`), and both needles survive in exactly one stem per route. The eyebrow is bound per route by the page's own logic (5.1.1.1 / 4.1.1.1).

| Spec statement | Where it is covered (lean record) | Route | Ticked |
|---|---|---|---|
| All substances are made of atoms. An atom is the smallest part of an element that can exist | Card 'Atoms and elements' | CF CH TF TH | ✓ |
| Atoms of each element are represented by a chemical symbol, eg O, Na | Card 'Atoms and elements'; Dive deeper 'Symbols you need' | CF CH TF TH | ✓ |
| There are about 100 different elements. Elements are shown in the periodic table | Card 'Atoms and elements' | CF CH TF TH | ✓ |
| Compounds are formed from elements by chemical reactions | Card 'Compounds'; Rung 4; practice Q2 | CF CH TF TH | ✓ |
| Chemical reactions always involve the formation of one or more new substances, and often involve a detectable energy change | Card 'Chemical reactions'; Start here | CF CH TF TH | ✓ |
| Compounds contain two or more elements chemically combined in fixed proportions and can be represented by formulae | Cards 'Compounds', 'Element, compound or mixture' (fig:aec-particle-boxes), 'Formulae'; reveal 'Compound and mixture compared'; Key fact; practice Q1 | CF CH TF TH | ✓ |
| Compounds can only be separated into elements by chemical reactions | Card 'Compounds'; reveal; Easy mistakes; Key fact | CF CH TF TH | ✓ |
| Chemical reactions can be represented by word equations or equations using symbols and formulae | Card 'Word and symbol equations'; Rung 2 | CF CH TF TH | ✓ |
| Use the names and symbols of the first 20 elements, Groups 1 and 7 and other elements in the spec | Card 'Atoms and elements'; Dive deeper 'Symbols you need' | CF CH TF TH | ✓ |
| Name compounds of these elements from given formulae or symbol equations | Card 'Naming compounds'; Rung 2 (sodium chloride); practice Q5 (new) | CF CH TF TH | ✓ |
| Write word equations | Card 'Word and symbol equations' | CF CH TF TH | ✓ |
| Write formulae and balanced chemical equations | Cards 'Formulae', 'Balancing an equation' (fig:aec-balance-water); Easy mistakes; Rung 2; practice Q3 | CF CH TF TH | ✓ |
| (HT only) Write balanced half equations and ionic equations where appropriate | Card 'Half equations and ionic equations (Higher)' | CH TH | ✓ |

**Misconceptions taught against (Easy mistakes).** O₂ is a compound because it has two atoms; balancing water by writing H₂O₂; bronze (metal with metal) is a compound; a compound can be separated by filtering or distilling.

**Gaps and mismatches.** None. "An element contains only one type of atom" is not a 4.1.1.1 sentence, but it is how every particle-diagram question is marked, so it is in card 'Atoms and elements'.

**Practice set source.** Subtopic quiz list, four items, identical on all four routes; a fifth added (naming a compound from its formula), so the set is five on every route.

**Audit of the ladder and practice set (faults found and fixed).**
- Quiz Q1 (the fallback K.find needle, 'key difference between a compound and a mixture'): credited option said "chemically bonded", replies used capitals ("ELEMENT") and "fundamentally". Credited option now says "chemically combined ... separated by physical processes" (spec words); replies rewritten plainly. Stem kept.
- Quiz Q2 (iron and sulfur): replies with dashes. Rewritten plainly; stem and options kept.
- Quiz Q3 (balancing water): replies with dashes and "The question asks about water formation". Rewritten; stem and options kept.
- Quiz Q4 (the Rung 1 needle, 'Which of these is a mixture'): credited option said "not chemically bonded", replies shouted "COMPOUND". Option now "not chemically combined"; replies rewritten. Stem kept, so Rung 1 is unchanged and still finds it.
- **Added** quiz Q5 "What is the name of the compound with the formula CaCl₂?" (new id `ks4q:atoms-elements-compounds:b4824ae86e`): the spec's "name compounds from given formulae" had no practice item. Four options of equal length (chloride, chlorine, chlorate, chlorite).
- Rung 3 (air is a mixture): links 2 and 3 both followed from link 1, so two orders were valid. Fixed by a logic edit: link 2 names each gas's boiling point and link 3 uses "those different boiling points". One order.
- Rungs 1, 2, 4: checked, no fault. Rung 2: 2Na + Cl₂ → 2NaCl, 2 Na and 2 Cl on each side.
- Option-length check (the label a pupil sees, before any " — "): no credited option is the longest on any item.

**Old subtopic data.** spec "5.1.1.1" ✓. `theory` and `key_note` say "118 known elements" and "chemically bonded"; neither is shown on the lean page (the key note section is not on it). `common_mistake` uses capitals; not shown.

**Unsure (left out until checked).** None in the content.

**Removed or moved.**
- Design benches: Zoom in and classify (six particle boxes), Sort the substances, Think again (H₂O₂), the Balance it stepper with three equations, the command-word list: off the page. Their teaching is in the cards, the two figures and Easy mistakes.
- "118 are known today": Dive deeper.
- Command words: Dive deeper.

**Words.** Design page about 1,826 (approximate: template text plus the bench strings in the logic, so an over-count); lean teaching text 770, plus 105 in Dive deeper.

**Parent's fix round (26 Nov 2026).** Practice Q2's credited option carried a second dash in its feedback tail ('A compound — iron sulfide — formed by chemical bonding ...'). It now reads 'A compound — iron sulfide, made by a chemical reaction between iron and sulfur': the label shown is still 'A compound' (KS4.item shows the text before ' — ' and moves the rest into the feedback). Stem and key unchanged.

**Iron sulfide colour (26 Nov 2026, coordinator's ruling).** The practice item said "a grey solid" and Rung 4 "a black solid". The practice stem is kept exactly, so `ks4q:atoms-elements-compounds:bab5f37818` keeps its id; Rung 4 now says "a grey solid" too (a logic edit; rung ids are positional, so its id is kept). AQA accepts grey or dark grey for iron sulfide made from iron and sulfur.

**Examiner fix round (26 Nov 2026).**
- B4 (new logic edit, blind flag): Rung 1 was K.find of the quiz item 'Which of these is a mixture?', the same words and options as practice Q4. Rung 1 (id #r1, positional, kept) now asks 'Identify which of these substances is a mixture.' with Pure water, Sea water (credited), Carbon dioxide, Magnesium oxide. Sea water is not in Rung 3's chain (air). The practice stem and its id are unchanged. The quiz needles still exist in the data, so build_ks4's rung-1 needle check (which reads Design's raw logic) is unaffected.
- S6: 'Mixtures has its own lesson.' removed. S7: Dive deeper 'About 100 elements is the number to learn.'
- S9: the credited options of practice Q1, Q2 and Q4 start their feedback tail with a capital. Stems and ids unchanged.
