# changes-of-state

Sources: AQA 8464 6.3.1.2 (CF CH) / 8463 4.3.1.2 (TF TH), word for word the same. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). No HT-only or physics-only line, no equation, no required practical. Rainford KS4 SOW, Year 10 Physics lessons 20 "Changing states of matter" and 21 "Changing states of matter - Investigation"; Physics LO sheet: melting and boiling points of a pure substance are fixed; find a melting or boiling point by a graphical technique; describe in detail the behaviour of the particles during changes of state.
Routes: CF CH TF TH.
Legacy status: none (old generate_site_v5 page; no Design batch holds this slug). NEW lean FULL record. Eyebrow derived: "AQA Combined Science (8464) 6.3.1.2 · Model" / "AQA Physics (8463) 4.3.1.2 · Model".

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| Students should be able to describe how, when substances change state (melt, freeze, boil, evaporate, condense or sublimate), mass is conserved. | Card 'The changes of state' (fig:state-changes names all six); Card 'Mass is conserved' (AQA words; 100 g of ice; open pan); Key fact (all six named); Easy mistakes 1; Rung 1 (both); Rung 2 (first, dry ice in a sealed bag); Rung 3 (first); Rung 4; Practice Q1, Q3, Q5 | CF CH TF TH | all | ✓ |
| Changes of state are physical changes which differ from chemical changes because the material recovers its original properties if the change is reversed. | Start here; Card 'Physical, not chemical' (AQA words; wax, burning paper); Reveal 'Physical or chemical'; Easy mistakes 3; Key fact; Rung 2 (second); Rung 3 (second); Rung 4; Practice Q2, Q4 | CF CH TF TH | all | ✓ |

**Equations and units.**
None in this spec point.

**Faults in the current pages and data.**
- The old page taught "deposition" (gas straight to solid). AQA names six changes (melt, freeze, boil, evaporate, condense, sublimate) and not deposition. Left out.
- Old page: "No new chemical bonds are formed or broken between different types of molecule" and "Strong intermolecular forces hold them together" (solids), "Very weak intermolecular forces (effectively none)" (gases). Intermolecular forces are not in 4.3.1.2; internal-energy teaches the potential energy of the particles.
- Old page: "Chemical change: usually irreversible". The spec's test is whether the material recovers its original properties; the lean card says that.
- Old quiz options carried their explanations ("200 g — mass is conserved during changes of state; no particles are created or destroyed"), which gave the answer away. Options rewritten; stems kept.

**Gaps and mismatches.**
- None in the content lines. The old page had no particle diagram and no diagram of the changes: fig:particle-states and fig:state-changes are new (figlib/ks4lean_pm.py).
- Rainford LO "State that the melting and boiling points of a pure substance are fixed; find a melting or boiling point by a graphical technique" is not in 6.3.1.2 / 4.3.1.2. Reading a flat section of a heating or cooling curve is taught in internal-energy (cooling curve card) and specific-latent-heat (heating and cooling graphs card); fixed melting points of pure substances are 8462/8464 chemistry (pure-substances). Named here, not repeated.
- Rainford's lesson 21 "Changing states of matter - Investigation" has no AQA required practical behind it; the cooling-curve reading it needs is in internal-energy.

**Unsure (left out until checked).**
- "Melting, boiling, evaporating and sublimating happen when energy is transferred to the substance; freezing and condensing when energy is transferred away." Beyond the words of 4.3.1.2 (it is the 4.3.2.1 idea); kept as one line each in 'The changes of state' because the diagram needs a direction. Check it is wanted here.
- Dry ice (solid carbon dioxide) as the sublimation example: it sublimates at room pressure; the spec names no example.

**Removed or moved.**
- Pupil walk at 390 px (24 Nov 2026): the "boiling or evaporating" label in fig:state-changes moved up beside the gas box, clear of the right edge.
- Removed: deposition; intermolecular forces; "H₂O molecules are still H₂O" (formula detail); the long particle descriptions of each state (the figure and one line replace them).
- Removed: the classic matching activity (ks4c:changes-of-state:match-1..5).
- Moved to Dive deeper: boiling against evaporating (where and at what temperature), links to internal energy, latent heat and density.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `49265d50d3` | 200 g of water is placed in a freezer and completely freezes. What is the mass of the ice formed? | 200 g |
| 2 | kept (stem unchanged, options rewritten) | `4188d2c796` | Why is melting a physical change rather than a chemical change? | The material gets its original properties back if it is frozen again |
| 3 | new | `a1a6566a10` | What is the name for the change of state from a liquid to a solid? | Freezing |
| 4 | new | `10855afe3d` | Which of these is a chemical change, not a change of state? | Wood burning to ash |
| 5 | new | `83024869c7` | A puddle of water evaporates on a sunny day. What happens to the water particles? | They escape into the air as a gas |

**Ladder (Ks4Practice, 2·2·2·1, new).**

| Item | Prompt | Answer |
|---|---|---|
| Rung 1 (first) mcq | Name the change of state from a solid straight to a gas. | Sublimating |
| Rung 1 (second) mcq | Name the change of state from a gas to a liquid. | Condensing |
| Rung 2 (first) mcq | A 20 g piece of dry ice is sealed in a bag and turns straight into a gas. Which statement is correct? | It sublimates, and the mass in the bag stays 20 g |
| Rung 2 (second) mcq | Which change gives back the material with its original properties when it is reversed? | Steam condensing to water |
| Rung 3 (first) chain | Ice in a sealed bag melts. Explain why the mass of the bag stays the same. | particles leave fixed positions but stay in the bag → same number, same mass each → total mass conserved |
| Rung 3 (second) chain | Wax is melted and then left to cool until solid. Explain why this is a physical change. | same particles move around each other → back into fixed positions → original properties back, physical |
| Rung 4 (first) write | Steam condenses on a cold window. Describe the particles; explain why it is physical and mass is conserved. | 5 marking points |

Every chain has one right order: each link uses what the link before it established.

**Assignment pool.** 63 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
