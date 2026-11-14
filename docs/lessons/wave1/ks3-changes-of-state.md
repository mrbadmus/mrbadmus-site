# changes-of-state

Sources: Rainford Year 7 Chem 1, lessons 5b "Changing states" and 5c "Stearic acid and risk assessment"; National Curriculum C2, C6, C20, P50, P54, P55, P57. KS3 has one route.

| Source | Statement | Where it is covered | Ticked |
|---|---|---|---|
| NC C2 | changes of state in terms of the particle model | Card: What the particles do; Card: The temperature stops rising (drawn heating curve); Card: Evaporating and boiling | ✓ |
| NC C6 | conservation of mass in changes of state | Card: Mass is conserved; Start here; Key fact | ✓ |
| NC C20 | energy changes on changes of state (qualitative) | Card: Energy in, energy out; Card: The temperature stops rising | ✓ |
| NC P50 | conservation of material and of mass, and reversibility, in melting, freezing, evaporation, sublimation, condensation, dissolving | Reveal table: Changes of state (all five changes); Card: Mass is conserved; Card: Melting or dissolving (5 g + 100 g = 105 g; evaporate to get the sugar back) | ✓ |
| NC P54 | the difference between chemical and physical changes | Reveal table: Physical or chemical change; Key fact | ✓ |
| NC P55 | arrangements, motion and closeness of particles explaining changes of state | Card: What the particles do | ✓ |
| NC P57 | changes with temperature in motion and spacing of particles | Card: What the particles do; Card: The temperature stops rising | ✓ |
| SOW 5b | Name the changes of state | Reveal table: Changes of state; Key words | ✓ |
| SOW 5b | Use melting points and boiling points to identify the state a substance is in | Card: Melting point and boiling point; Reveal table: Which state at room temperature | ✓ |
| SOW 5b activity | Y7 Melting ice | Start here (sealed bag); Card: The temperature stops rising | ✓ |
| SOW 5c | Risk assess the stearic acid practical | Card: A cooling curve (hazard, risk, control line); safety note | ✓ |

**Gaps and mismatches.** Rainford 5c is a practical and risk-assessment lesson with no site page; it is a card here. Rainford tags 5c with C20, P50, P55, P57, all ticked above.

**Question audit fixes (docs/b2c/QUESTION-AUDIT.md).**
- `ks3-c1-changes-of-state-produce` (the towel drying at 8 °C): now Card: Evaporating and boiling. It says particles in a liquid move at different speeds, fast surface particles escape at any temperature, the liquid left behind cools, and boiling happens throughout at one temperature.
- Bank `c1-03-s01` (bubbles are not air), `s02` (steam is invisible), `s03` (boiling takes about seven times the energy of melting) and `s04` (freezing gives energy out) each have a card line.

**Quiz notes.** Rung 3 and 4 stems rewritten into sentences of 15 words or fewer (render only). Four ticks rewritten: tick 1 (dash, and "average kinetic energy" said plainly), tick 2 (melting does not "break the particles apart"; it overcomes the forces holding them in place), tick 5 (dash), Rung 4 tick 5 (over 15 words). Feedback written for every wrong option of Rungs 1 and 2. Rung 2's stored option B is "Nothing — it is being lost to the room"; the option-label rule shows it as "Nothing" (see NOTES).

**Checked numbers.** Specific latent heats of water: fusion 334 J/g, vaporisation 2260 J/g, ratio 6.8 ("about seven times"). The heating curve is drawn to scale in energy: ice −20 to 0 °C 42 J/g, melting 334, water 0 to 100 °C 418, boiling 2260, steam 100 to 120 °C 40. Melting and boiling points: oxygen −218 °C and −183 °C; mercury −39 °C and 357 °C; iron 1538 °C and 2862 °C. Stearic acid melts at about 69 °C.

**Left out because unsure.** Sugar's melting point (about 186 °C) and its browning. The old "steam gives back seven times the energy" comparison on skin (Dive deeper keeps only "a lot of energy"). Water's high heat capacity and the sea.

**Removed or moved.** Removed: the heating bench (`the-heating-bench`), the bubble commit (`the-bubble`, now Card: Evaporating and boiling), the melt-or-dissolve sorter (`melt-or-dissolve`, now Card: Melting or dissolving), the key note, the opening paragraph. Moved to Dive deeper: steam burns, sweating. New: drawn heating curve (c1-heating-curve), cooling-curve practical card, melting and boiling point card, physical or chemical table.

**Review fixes (examiner pass and blind pass, 14 Nov).**
- Temperature is no longer retyped. The card line and Rung 3 tick 1 use the dash-free short form for `ks3_data/quantities.py` ("a measure of the average kinetic energy of the particles"); the integrator wires them to `TEMPERATURE_SHORT` and `TEMPERATURE_CRITERION_SHORT` (see NOTES). The card adds "That is the energy they have because they are moving."
- Key fact says "a pure substance". Evaporating is defined as from the surface, at any temperature. Sublimation names dry ice and is listed as taking in energy.
- Dissolving now "needs two substances, such as sugar and water". Melting "needs only one substance, and energy from heating".
- Method: stearic acid in a test tube standing in hot water; one hazard, risk and control line added.
- Early small bubbles are dissolved air (added after "They are not air").
- Rung 2 feedback for the shortened option "Nothing" now answers what the pupil sees; feedback for "Warming the beaker" now says the beaker stays near 0 °C.
- Start question now "how much will the water weigh?" (matches its two options). Safety note and GCSE line now under 15 words a sentence.
