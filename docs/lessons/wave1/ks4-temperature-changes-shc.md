# temperature-changes-shc

Sources: AQA 8464 6.3.2.2 (CF CH) / 8463 4.3.2.2 (TF TH), word for word the same. Read from the 2016 specification PDFs on Mide's Mac (AQA-8464-SP-2016.pdf v1.1, AQA-8463-SP-2016.pdf v1.1). No HT-only or physics-only line. Skills: MS 1a, 3b, c, d. 6.3.2.2 / 4.3.2.2 says the equation and specific heat capacity "are also included in Energy changes in systems": the specific heat capacity practical is listed there, as **Required practical activity 14 in 8464 (6.1.1.3)** and **Required practical activity 1 in 8463 (4.1.1.3)**, AT 1 and 5. Rainford KS4 SOW, Year 10 Physics lessons 23 "Specific heat capacity" and 24 "Specific heat capacity RP" (rainford_sow.py maps both here); Physics LO sheet: the effect of changing each factor in the equation; calculate the energy to change a temperature; measure c and find a mean; evaluate the results.
Routes: CF CH TF TH.
Legacy status: LEGACY, Design batch 3 (`temperature-changes-shc.dc.html`, family Quantitative). Ladder: Ks4Ladder r1..r4 from the page. Worked examples and Your turn: the page's own cfExamples / cfQuestions, placed by the `cfifa` slot. Practice set: K.bank, the route's `quiz` list. The page's eyebrow ("AQA Combined Science (8464) 6.3.2.2" / "AQA Physics (8463) 4.3.2.2") and its header chip "Required practical {{ rpNum }}" (14 on Combined, 1 on Triple) are already right and are kept.

| Spec statement (AQA wording) | Where it is covered | Route | Flag | Ticked |
|---|---|---|---|---|
| If the temperature of the system increases, the increase in temperature depends on the mass of the substance heated, the type of material and the energy input to the system. | Start here; Card 'What decides the temperature rise' (AQA words); Practice Q4 | CF CH TF TH | all | ✓ |
| change in thermal energy = mass × specific heat capacity × temperature change, ΔE = m c Δθ (ΔE in joules, J; m in kilograms, kg; c in joules per kilogram per degree Celsius, J/kg °C; Δθ in degrees Celsius, °C). | Card 'The equation' (AQA words, units, triangle EQ_SHC); Card 'The temperature change'; Key fact; Practice Q1, Q3, Q5 | CF CH TF TH | all | ✓ |
| Students should be able to apply this equation, which is given on the Physics equation sheet, to calculate the energy change involved when the temperature of a material changes (MS 1a, 3b, c, d). | Card 'The equation' ("on the Physics equation sheet ... use it and rearrange it"); worked examples and Your turn (legacy cfifa); Card 'Energy from a heater' (E = P t); Rung 2 (calc); Rung 3; Practice Q1, Q5 | CF CH TF TH | all | ✓ |
| The specific heat capacity of a substance is the amount of energy required to raise the temperature of one kilogram of the substance by one degree Celsius. | Card 'Specific heat capacity' (AQA words; water 4200, aluminium 900); Key fact; Easy mistakes 3; Rung 1 (define); Practice Q2 | CF CH TF TH | all | ✓ |
| Required practical (8464 RP 14 at 6.1.1.3 / 8463 RP 1 at 4.1.1.3): an investigation to determine the specific heat capacity of one or more materials, linking the decrease of one energy store (or work done) to the increase in temperature and subsequent increase in thermal energy stored (AT 1, 5). | Card 'Required practical 14: specific heat capacity' (CF CH) and 'Required practical 1: specific heat capacity' (TF TH): method, energy from a joulemeter or E = P t, the error from energy dissipated to the surroundings, safety; header chip; Rung 3 (value too high); Rung 4 (describe a method) | CF CH TF TH | all; each route's own RP number | ✓ |

**Equations and units.**

| Equation (AQA words) | Symbols | Units | Recall or apply | Equation sheet (8463) |
|---|---|---|---|---|
| change in thermal energy = mass × specific heat capacity × temperature change | ΔE = m c Δθ | ΔE in J; m in kg; c in J/kg °C; Δθ in °C | apply | On the sheet: equation 5 |
| energy transferred = power × time | E = P t | E in J; P in W; t in s | recall and apply (8463 4.2.4.2 / 8464 6.2.4.2; used in the practical and Higher Rung 2) | Not on the sheet: recall list, equation 21 |

**Faults in the current pages and data.**
- Worked example 1 (`fifas`, all four data files) wrote 336,000 and 168,000 with commas; now spaces (336 000, 168 000 J).
- The Design page's equation box labelled E = P t "On the sheet". It is a recall equation. That box is not on the lean page; the card 'Energy from a heater' says it must be remembered.
- The old `rp` field and key note say "RP14" on every route. That is the 8464 number; 8463 numbers it 1. Not rendered on the lean page (the header chip and the two route cards carry the right numbers).
- Old quiz options carried their working ("135,000 J — ΔE = 2 × 450 × 150 = 135,000 J (Δθ = 200 − 50 = 150°C)"), which gave the answer away; the water-coolant correct option was the longest. Options rewritten; stems kept.

**Gaps and mismatches.**
- None in the content lines.
- The practical is taught twice: here (the Rainford lesson that teaches it) and in energy-changes-in-systems (where AQA lists it). Both cards give the same route numbers. Dive deeper links the two.

**Unsure (left out until checked).**
- "1 kg of water needs more than four times as much energy as 1 kg of aluminium to warm by 1 °C" (4200 ÷ 900 = 4.7). Correct for these data values; real values vary slightly with temperature.
- The Start here says seawater; the explanation uses water's specific heat capacity. Seawater's is a little lower (about 3900 J/kg °C), still far above dry sand's (about 800 J/kg °C). No number is given on the page.

**Removed or moved.**
- Removed from the page: the temperature-rise race (raceFig, ranking), the equation boxes, the practical bench (gate, rigFig, graphFig, off-pick, c entry, the without-lagging rerun), the Think again "Just put the numbers straight in" (Ks4Choice), the Key note and the video. Their teaching is in the cards. Their activity ids go: `#choice-1`, `#ctext`, `#gate`, `#offpick`, `#order`, on all four routes.
- Removed: the classic matching cards (ks4c:temperature-changes-shc:match-1..4).
- Removed: "Cast iron pans heat up quickly" and "higher SHC heats up and cools down more slowly" (batch-3 DEPARTURES: imprecise; never shown).
- `activity_save_drive` case `ks4-form-shc` (`#order`, `#offpick`, `#ctext`) will need retiring with absent-marker proof.

**Practice set source.** `K.bank(slug, R.route)`: the route's `quiz` list in all_subtopics_physics*.py. Five per route, the same on every route; correct option first (the build shuffles).

| Q | Origin | ks4q: id | Stem | Credited |
|---|---|---|---|---|
| 1 | kept (stem unchanged, options rewritten) | `c58182799d` | A 2 kg iron block (c = 450 J/kg°C) cools from 200°C to 50°C. How much energy is released? | 135 000 J |
| 2 | kept (stem unchanged, options rewritten) | `a3fe1a5cf3` | Why is water used as the coolant in car engines rather than a cheaper fluid? | It has a high specific heat capacity, so it warms up less for the energy it takes in |
| 3 | new | `e76ffb23b3` | What is the unit of specific heat capacity? | J/kg °C |
| 4 | new | `8de9d34763` | The temperature rise of a heated object depends on three things. Which three? | Its mass, its material and the energy put in |
| 5 | new | `3ff745a322` | How much energy is needed to raise the temperature of 0.5 kg of water by 10 °C? (c = 4200 J/kg °C) | 21 000 J |

**Ladder.** Ks4Ladder r1..r4 from the Design page, positions kept, unchanged: Rung 1 define c; Rung 2 calc (Foundation: 40 g copper spoon, 770 J; Higher: 60 W for 4.0 minutes on 2.0 kg copper, 18.7 °C); Rung 3 chain (measured c too high: energy to the surroundings); Rung 4 (6 marks: describe the method with an immersion heater and a joulemeter).

**Assignment pool.** 64 rows for this slug in ks4_data/questions/physics/particle_model*.py (12 at positions 0–11, the auto window). None is changed here.
