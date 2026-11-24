# internal-energy

Sources: AQA 8464 6.3.2.1 (CF CH) / 8463 4.3.2.1 (TF TH), word for word the same. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). No HT-only or physics-only line, no equation, no required practical. Rainford KS4 SOW, Year 10 Physics lesson 22 "Internal energy"; Physics LO sheet: describe how the behaviour of particles changes as the energy of a system increases; use kinetic and potential energy to explain changes in internal energy; describe the changes in the size of intermolecular forces during changes of state.
Routes: CF CH TF TH.
Legacy status: LEGACY, Design batch 2 (`internal-energy.dc.html`, family Model). Ladder: Ks4Ladder r1..r4 from the page. Practice set: K.bank, the route's `quiz` list. Figure kept: `coolFig` (the cooling curve, drawn with no state), placed by a legacy-fig slot. The page binds its own eyebrow (`eyebrowText`); the Combined one is corrected by a logic edit (see Faults).

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| Energy is stored inside a system by the particles (atoms and molecules) that make up the system. This is called internal energy. | Card 'Energy stored by particles' (AQA words) | CF CH TF TH | all | ✓ |
| Internal energy is the total kinetic energy and potential energy of all the particles (atoms and molecules) that make up a system. | Card 'Energy stored by particles' (AQA words; kinetic from moving, potential from the forces between them); Card 'Temperature and internal energy'; Easy mistakes 1, 3; Key fact; Rung 1 (new: define internal energy); Rung 4; Practice Q2, Q5 | CF CH TF TH | all | ✓ |
| Heating changes the energy stored within the system by increasing the energy of the particles that make up the system. This either raises the temperature of the system or produces a change of state. | Start here; Card 'What heating does' (AQA words; kinetic for a rise, potential for a change of state); Reveal 'Heating ice until it boils'; Card 'Reading a cooling curve' (coolFig); Easy mistakes 2; Key fact; Rung 2 (heating curve of X); Rung 3 (stearic acid freezing); Rung 4; Practice Q1, Q3, Q4 | CF CH TF TH | all | ✓ |

**Equations and units.**
None in this spec point. Dive deeper points to ΔE = m c Δθ (temperature-changes-shc) and E = m L (specific-latent-heat).

**Faults in the current pages and data.**
- The Combined eyebrow read "AQA Physics (8464) 6.3.2.1 · Model" (live on CF and CH). 8464 is AQA Combined Science. Fixed by logic edit 1: "AQA Combined Science (8464) 6.3.2.1 · Model".
- Rung 1 was practice Q1 (K.find, "Its temperature stays constant for several minutes"), so a pupil met the same question twice on the page. Logic edit 2 makes Rung 1 its own question through K.item: "Define the internal energy of a system." Position kept, so `ks4:internal-energy:<route>#r1` is kept; its options and answer key are new.
- Old quiz option "A change of state — energy is increasing potential energy to break intermolecular bonds": "break intermolecular bonds" is not AQA's wording, and the option was far the longest. Old distractor "losing heat to the surroundings at exactly the same rate as energy is supplied" describes a real steady state, so it was arguable. Options rewritten; stems kept.

**Gaps and mismatches.**
- None in the content lines.
- Rainford LO "Describe the changes in the size of intermolecular forces during changes of state": not AQA wording at GCSE (the spec speaks of the particles' potential energy). Not taught as forces changing size; the card says the potential energy depends on how far apart the particles are.
- "Temperature is related to the average kinetic energy of the particles" is AQA's wording for gases (4.3.3.1). The Design page used it for every state, and so does the lean card 'Temperature and internal energy'. It is the standard GCSE model.

**Unsure (left out until checked).**
- Practice Q2's kept stem has an em dash ("A large cool swimming pool and a small hot cup of tea — which has greater internal energy?"). Changing it would change its ks4q: id, so it is kept as it is; the science is right.

**Removed or moved.**
- Removed from the page: the heating bench (four stages, partFig, curveFig), the Think again "Hotter is not more" (Ks4Choice), the Compare sort and the cooling-curve sort (Ks4Sort), the Key note and the video. Their teaching is in the cards and the reveal table. Their activity ids go: `#choice-1`, `#picks`, `#sort-1-1..5`, `#sort-2-1..5`, on all four routes.
- Removed: the classic matching cards (ks4c:internal-energy:match-1..4).
- The page's Ks4End `legal` line (about the bench and graphs being a model) is emptied by lean_ks4, since no bench is on the page.
- `activity_save_drive` case `ks4-form-internal` (`#picks-1`) will need retiring with absent-marker proof, as in earlier units.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `c67e1fabc3` | A substance is heated at constant power. Its temperature stays constant for several minutes. What is happening? | It is changing state |
| 2 | kept (stem unchanged, options rewritten) | `bd88e6a2b3` | A large cool swimming pool and a small hot cup of tea — which has greater internal energy? | The swimming pool |
| 3 | new | `0ccdc1b32b` | Ice at 0 °C is heated and melts into water at 0 °C. What happens to its internal energy? | It increases |
| 4 | new | `718e050b9b` | Water is heated from 20 °C to 50 °C. Which energy of its particles increases? | Their kinetic energy |
| 5 | new | `3864801a2e` | Which has more internal energy: 1 kg of steam at 100 °C or 1 kg of water at 100 °C? | The steam |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept. Rung 1 rewritten through a logic edit (Define internal energy; K.item; ids kept). Rung 2 (data: heating curve of X, melting point 20 °C, liquid at 50 °C, average kinetic energy unchanged from D to E), Rung 4 (6 marks: ice at −10 °C to water at 20 °C) are unchanged. Rung 3 (chain: stearic acid freezing at 69 °C): its first two links could be swapped, so a logic edit makes link 2 read "While it freezes, energy is still transferred to the surroundings, so its internal energy decreases." One right order; id kept.

**Assignment pool.** 64 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
