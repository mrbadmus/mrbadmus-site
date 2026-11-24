# specific-latent-heat

Sources: AQA 8464 6.3.2.3 (CF CH) / 8463 4.3.2.3 (TF TH), word for word the same. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). No HT-only or physics-only line, no required practical. Skills: MS 1a, 3b, c, d, 4a; WS 3.5; AT 5 "Perform an experiment to measure the latent heat of fusion of water". Rainford KS4 SOW, Year 10 Physics lesson 25 "Specific latent heat"; Physics LO sheet: describe the changes in particle bonding during changes of state; calculate the latent heat of fusion and of vaporisation; measure the latent heat of fusion for water.
Routes: CF CH TF TH.
Legacy status: LEGACY, Design batch 3 (`specific-latent-heat.dc.html`, family Quantitative). Ladder: Ks4Ladder r1..r4 from the page. Worked examples and Your turn: the page's own cfExamples / cfQuestions, placed by the `cfifa` slot. Practice set: K.bank, the route's `quiz` list. Figure kept: `loggerFig` (the cooling curve of Y), placed by a legacy-fig slot and drawn complete by a logic edit. Eyebrow already route-aware ("AQA Combined Science (8464) 6.3.2.3" / "AQA Physics (8463) 4.3.2.3").

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| If a change of state happens: the energy needed for a substance to change state is called latent heat. When a change of state occurs, the energy supplied changes the energy stored (internal energy) but not the temperature. | Start here; Card 'Latent heat' (AQA words); Easy mistakes 1; Key fact; Rung 3 (new: ice in a drink); Practice Q1 | CF CH TF TH | all | ✓ |
| The specific latent heat of a substance is the amount of energy required to change the state of one kilogram of the substance with no change in temperature. | Card 'Specific latent heat' (AQA words); Key fact; Rung 4 (compare); Practice Q4 | CF CH TF TH | all | ✓ |
| energy for a change of state = mass × specific latent heat, E = m L (E in joules, J; m in kilograms, kg; L in joules per kilogram, J/kg). | Card 'The equation' (AQA words, units, triangle EQ_SLH); worked examples and Your turn (legacy cfifa); Card 'Energy from a flat section'; Key fact; Rung 2 (calc); Practice Q1, Q5 | CF CH TF TH | all | ✓ |
| Students should be able to apply this equation, which is given on the Physics equation sheet, to calculate the energy change involved in a change of state (MS 1a, 3b, c, d). | Card 'The equation' ("on the Physics equation sheet ... use it and rearrange it"); cfifa; Card 'Energy from a flat section' (L = E ÷ m); Rung 2; Practice Q1, Q5 | CF CH TF TH | all | ✓ |
| Specific latent heat of fusion: change of state from solid to liquid. Specific latent heat of vaporisation: change of state from liquid to vapour. | Key words; Card 'Specific latent heat' (AQA words); Easy mistakes 3; Rung 1 (name: vaporisation); Practice Q3 | CF CH TF TH | all | ✓ |
| Students should be able to interpret heating and cooling graphs that include changes of state (MS 4a, WS 3.5). | Card 'Heating and cooling graphs' (loggerFig: Y freezing B to C at 50 °C); Card 'Energy from a flat section' (7 minutes at 30 W, L = 210 000 J/kg); Reveal (sloping or flat section); Rung 2 Higher (heating curve of Z) | CF CH TF TH | all | ✓ |
| Students should be able to distinguish between specific heat capacity and specific latent heat. | Reveal 'Specific heat capacity or specific latent heat' (what changes, equation, unit, graph section); Easy mistakes 2; Rung 1 (distractor); Rung 4 (compare); Practice Q4 | CF CH TF TH | all | ✓ |
| AT 5: perform an experiment to measure the latent heat of fusion of water (skills column; not a required practical). | Card 'Measuring the specific latent heat of fusion of water' (heater in a funnel of crushed ice; start timing once water drips steadily; control funnel, whose melting comes from the warm room; joulemeter; L = E ÷ m) | CF CH TF TH | all | ✓ |

**Equations and units.**

| Equation (AQA words) | Symbols | Units | Recall or apply | Equation sheet (8463) |
|---|---|---|---|---|
| energy for a change of state = mass × specific latent heat (the sheet: "thermal energy for a change of state") | E = m L | E in J; m in kg; L in J/kg | apply | On the sheet: equation 9 |
| change in thermal energy = mass × specific heat capacity × temperature change | ΔE = m c Δθ | J; kg; J/kg °C; °C | apply (named here only to tell it from E = m L) | On the sheet: equation 5 |
| energy transferred = power × time | E = P t | J; W; s | recall and apply (used for the flat section and Higher Rung 2) | Not on the sheet: recall list, equation 21 |

**Faults in the current pages and data.**
- The Design page's equation box labelled E = P t "On the sheet". It is a recall equation. That box is not on the lean page.
- Rung 3 asked "Explain why sweating cools the body", the same question as practice Q2 ("Why does sweating cool the body?"), so a pupil met it twice. Logic edit 3 replaces Rung 3 with a chain on ice cooling a drink (latent heat of fusion taken from the drink). Same position, so `ks4:specific-latent-heat:<route>#r3` is kept; its content is new.
- The old key note said the energy goes into "breaking bonds" during a change of state; AQA's words are the energy stored (internal energy). The lean cards use AQA's words.
- Old quiz options carried their working ("1,130,000 J — E = 0.5 × 2,260,000"), which gave the answer away; the sweating correct option was the longest. Options rewritten; stems kept.
- Worked example 1 (`fifas`, all four data files) wrote 334,000 and 668,000 with commas; now spaces (334 000 J/kg, 668 000 J). The kept quiz stem "Lv = 2,260,000" is unchanged.

**Gaps and mismatches.**
- The Design page did not teach the AT 5 experiment (latent heat of fusion of water), which is both an AQA skills item and a Rainford LO. Added as a Key knowledge card.
- Rainford LO "Describe the changes in particle bonding during changes of state": not AQA wording. The cards speak of internal energy, as the spec does; internal-energy covers the particles' potential energy.

**Unsure (left out until checked).**
- The funnel method for the latent heat of fusion of water is the usual school method; AQA names no method. Check the card's wording (control funnel subtracted) is how Rainford runs it.
- Practice Q1's kept stem writes "Lv = 2,260,000 J/kg" and "100°C" (no space); the symbol Lv is not AQA's. Kept, because changing the stem changes its ks4q: id; the science is right.

**Removed or moved.**
- Pupil walk at 390 px (24 Nov 2026): curve() redrawn 460 wide, a number at every minute, letters off the line, so Rung 2's graph of Z (3 and 10 minutes) and the card's cooling curve of Y fit a phone. The card states E = m L once in symbols and the Key fact once in words. Soft hyphens in the reveal table; no-break spaces in numbers, units and short equations.
- Removed from the page: the energy ledger bench (ledgerFig, commit and equation picks), the equation boxes, the data-logger steps and the L entry, the Key note and the video. Their teaching is in the cards. Their activity ids go: `#ans`, `#gate`, `#ltext`, `#picks`, on all four routes.
- Removed: the classic matching cards (ks4c:specific-latent-heat:match-1..5).
- Removed: "ponds freeze from the surface down" and "Lv > Lf because fully separating particles" (batch-3 DEPARTURES: imprecise, not in the spec; never shown).
- Moved to Dive deeper: water's two values (334 000 and 2 260 000 J/kg), three-stage problems, why sweating cools you (so practice Q2 still has its teaching), command words.
- `activity_save_drive` case `ks4-form-latent` (`#picks-1`, `#ltext`) will need retiring with absent-marker proof.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `aa03205726` | How much energy is released when 0.5 kg of steam at 100°C condenses to water at 100°C? (Lv = 2,260,000 J/kg) | 1 130 000 J |
| 2 | kept (stem unchanged, options rewritten) | `472834d444` | Why does sweating cool the body? | Sweat evaporates, and the energy needed to evaporate it is transferred from the skin |
| 3 | new | `559a89de24` | Which change of state does the specific latent heat of fusion describe? | Solid to liquid |
| 4 | new | `553390ac59` | What is the unit of specific latent heat? | J/kg |
| 5 | new | `3de384e6b3` | 0.20 kg of water at 100 °C boils away. How much energy did it take? (specific latent heat of vaporisation of water = 2 260 000 J/kg) | 452 000 J |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept. Rung 1 (name: vaporisation), Rung 2 (calc; Foundation: 2.5 g of ice, 835 J; Higher: heating curve of Z at 50 W, 0.25 kg) and Rung 4 (compare c and L, 4 marks) unchanged. Rung 3 rewritten through a logic edit:

| Item | Prompt | Links in order |
|---|---|---|
| Rung 3 chain (new) | Ice at 0 °C is put into a drink at 20 °C. Explain why the drink cools as the ice melts. | The ice melts: solid to liquid at 0 °C. → As it melts, the ice needs energy, the latent heat of fusion, and this energy is transferred from the drink to the ice. → So the drink's internal energy decreases, and its temperature falls. Herrings: "The ice gives its cold to the drink"; "Melting ice releases energy into the drink". |

**Assignment pool.** 64 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
