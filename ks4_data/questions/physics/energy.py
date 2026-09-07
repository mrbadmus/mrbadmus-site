"""Physics · Energy — the eight subtopics of AQA 8463 §6.1.

Ninety-six assignment questions across stores and systems, the three energy
equations, specific heat capacity, power, dissipation, efficiency, energy
resources and (Triple only) thermal conductivity.

The distractors are built from the declared misconceptions in each
subtopic's brief: store-versus-pathway confusion ('heat store', 'light
store'), failing to square v or e, using the final temperature instead of
the temperature change, leaving time in minutes, dividing useful output by
wasted energy rather than by total input, and 'renewable means no
environmental impact'. Calculation distractors are always the arithmetic a
real error produces, never noise, so a marker can read a wrong answer and
name the mistake.

Nothing here restates a lesson page's own "Test yourself" question — those
belong to a different pool under the one-pool-per-surface law.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ energy-stores-systems ════════════════════════════════════════════
    {
        "id": "ks4-energy-stores-systems-e01",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A catapult's rubber band is pulled back ready to fire. "
                "State the energy store that is filled.",
        "options": [
            "The elastic potential store of the rubber band",
            "The kinetic store, because the band moves as it is pulled "
            "back",
            "The thermal store, because stretching the rubber warms it",
            "The magnetic store, because the frame of the catapult is "
            "metal",
        ],
        "correct_index": 0,
        "why": "Stretching an elastic object fills its elastic "
               "potential store, which empties again the moment it is "
               "released.",
    },
    {
        "id": "ks4-energy-stores-systems-e02",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal block is warmed by an electric heater and its "
                "temperature rises. State which store of the block has been "
                "filled.",
        "options": [
            "The heat store, because heat is exactly what the block has "
            "gained from the heater element",
            "The chemical store, because the heater burns energy in the block",
            "The thermal store, because the energy is now in the random "
            "motion of its particles",
            "The electrostatic store, because the heater runs on electricity",
        ],
        "correct_index": 2,
        "why": "Energy held in the random motion of a substance's particles "
               "is its thermal store; 'heat' names a pathway, not a store.",
    },
    {
        "id": "ks4-energy-stores-systems-e03",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist pushes on the pedals to speed up. Name the "
                "pathway by which energy is transferred to the kinetic store "
                "of the bicycle.",
        "options": [
            "Heating",
            "Radiation",
            "Electrical work",
            "Mechanical work",
        ],
        "correct_index": 3,
        "why": "A force acting through a distance transfers energy by "
               "mechanical work — the pedals push the cranks round.",
    },
    {
        "id": "ks4-energy-stores-systems-e04",
        "subtopic_slug": "energy-stores-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A torch is switched on. State the store that empties as the "
                "lamp lights.",
        "options": [
            "The thermal store of the surroundings",
            "The chemical store of the cells",
            "The electrical store of the connecting wires",
            "The light store of the lamp",
        ],
        "correct_index": 1,
        "why": "The cells hold energy in a chemical store; electrical work "
               "is the pathway that carries it to the lamp, not a store.",
    },
    {
        "id": "ks4-energy-stores-systems-s01",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An archer draws a bow and then releases the arrow. Describe "
                "the sequence of stores involved.",
        "options": [
            "Elastic potential store of the bow → chemical store of the "
            "archer → kinetic store of the arrow",
            "Kinetic store of the arrow → elastic potential store of the bow "
            "→ thermal store of the air",
            "Chemical store of the archer → kinetic store of the arrow → "
            "elastic potential store of the bow",
            "Chemical store of the archer → elastic potential store of the "
            "bow → kinetic store of the arrow",
        ],
        "correct_index": 3,
        "why": "The archer's muscles empty a chemical store to bend the bow, "
               "filling its elastic potential store, which then fills the "
               "arrow's kinetic store on release.",
    },
    {
        "id": "ks4-energy-stores-systems-s02",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skydiver falls at a constant speed. Describe what happens "
                "to the energy leaving her gravitational potential store.",
        "options": [
            "It fills her kinetic store, which therefore keeps increasing",
            "It is transferred to the thermal store of the surrounding air, "
            "and her kinetic store stays constant",
            "It is destroyed by the air resistance acting on her",
            "It stays in her gravitational potential store, because "
            "neither her speed nor her mass is changing at all",
        ],
        "correct_index": 1,
        "why": "At constant speed the kinetic store cannot grow, so every "
               "joule leaving the gravitational store is dissipated to the "
               "thermal store of the air.",
    },
    {
        "id": "ks4-energy-stores-systems-s03",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two bar magnets are pushed together with like poles facing "
                "and then held still. Identify the store that has been "
                "filled.",
        "options": [
            "The elastic potential store, because the magnets are being "
            "squashed together against a force",
            "The kinetic store, because the magnets were moved to get there",
            "The magnetic store, because energy is held in the field between "
            "the repelling poles",
            "The electrostatic store, because the two poles carry opposite "
            "charges",
        ],
        "correct_index": 2,
        "why": "Work done against a magnetic force fills a magnetic store — "
               "energy held in the field, released when the magnets spring "
               "apart.",
    },
    {
        "id": "ks4-energy-stores-systems-s04",
        "subtopic_slug": "energy-stores-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A phone is plugged into the mains and charges. Identify the "
                "main pathway and the store being filled.",
        "options": [
            "Electrical work, filling the chemical store of the battery",
            "Heating, filling the thermal store of the battery",
            "Electrical work, filling the electrostatic store of the battery",
            "Radiation, filling the chemical store of the battery",
        ],
        "correct_index": 0,
        "why": "Charge moving through a potential difference transfers energy "
               "by electrical work, and a rechargeable cell stores it "
               "chemically.",
    },
    {
        "id": "ks4-energy-stores-systems-h01",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball is dropped and rebounds to a lower height after every "
                "bounce. Explain what conservation of energy tells you about "
                "the gravitational potential energy that is missing.",
        "options": [
            "An equal amount has been destroyed at each impact by the "
            "collision, so the total energy of the system falls every "
            "single bounce",
            "An equal amount has been transferred to the thermal stores of "
            "the ball, the floor and the air, so the total is unchanged",
            "It remains in the ball's elastic potential store and is released "
            "on the final bounce",
            "It was never in the gravitational store, because the ball was "
            "falling rather than being raised",
        ],
        "correct_index": 1,
        "why": "Energy is never destroyed — the shortfall in height measures "
               "exactly what has been dissipated to the surroundings.",
    },
    {
        "id": "ks4-energy-stores-systems-h02",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wind-up torch and a battery torch each light an identical "
                "lamp. Compare the store that empties in each case.",
        "options": [
            "Elastic potential in the wind-up torch and chemical in the "
            "battery torch; both end as light radiation and thermal stores",
            "Kinetic in the wind-up torch and electrical in the battery "
            "torch; both of them end up filling the light store of the "
            "lamp and nothing else",
            "Elastic potential in both, because the cell is compressed inside "
            "the casing of the battery torch",
            "Chemical in both, because every torch is ultimately driven by a "
            "stored chemical supply",
        ],
        "correct_index": 0,
        "why": "The wind-up torch stores energy elastically in a wound "
               "spring; the battery stores it chemically; both finish as "
               "light radiation and warmed surroundings.",
    },
    {
        "id": "ks4-energy-stores-systems-h03",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pumped-storage station pumps water uphill overnight and "
                "releases it through turbines at midday. Explain why it "
                "cannot return all of the energy used to pump the water.",
        "options": [
            "Energy is destroyed by friction in the pipes, the pumps and "
            "the turbines, so the total energy of the system falls a "
            "little over every cycle",
            "The gravitational potential store shrinks on its own while the "
            "water sits in the upper reservoir overnight",
            "Some energy is dissipated to the thermal stores of the pumps "
            "and pipes, so less returns usefully although the total is "
            "unchanged",
            "The water gains mass as it falls through the pipes, so the "
            "energy returned cannot be predicted from the energy put in",
        ],
        "correct_index": 2,
        "why": "Conservation of energy still holds — the shortfall has been "
               "dissipated into the surroundings, where it is too spread out "
               "to be useful.",
    },
    {
        "id": "ks4-energy-stores-systems-h04",
        "subtopic_slug": "energy-stores-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wind turbine drives a generator that lights a lamp in a "
                "house. Describe the complete chain of stores and pathways.",
        "options": [
            "Kinetic store of the air → mechanical work → chemical store of "
            "the generator → electrical work → light radiation from the "
            "lamp and from its shade",
            "Kinetic store of the air → electrical work → kinetic store of "
            "the turbine → heating → thermal store of the lamp",
            "Thermal store of the air → mechanical work → kinetic store of "
            "the turbine → electrical work → light radiation from the lamp",
            "Kinetic store of the air → mechanical work → kinetic store of "
            "the turbine → electrical work → light radiation and thermal "
            "store of the lamp",
        ],
        "correct_index": 3,
        "why": "Moving air holds a kinetic store; the blades transfer it by "
               "mechanical work, and the generator transfers it onward by "
               "electrical work to the lamp.",
    },

    # ══ changes-in-energy ════════════════════════════════════════════════
    {
        "id": "ks4-changes-in-energy-e01",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 12 kg toolbox is raised 2.5 m onto a shelf. "
                "Calculate the gravitational potential energy it gains. "
                "(g = 9.8 N/kg)",
        "options": [
            "30 J",
            "118 J",
            "294 J",
            "147 J",
        ],
        "correct_index": 2,
        "why": "Ep = mgh = 12 × 9.8 × 2.5 = 294 J — all three "
               "quantities are multiplied together.",
    },
    {
        "id": "ks4-changes-in-energy-e02",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring with a spring constant of 250 N/m is stretched by "
                "0.20 m. Calculate the elastic potential energy stored.",
        "options": [
            "5.0 J",
            "10.0 J",
            "25.0 J",
            "50.0 J",
        ],
        "correct_index": 0,
        "why": "Ee = ½ke² = ½ × 250 × 0.20² = ½ × 250 × 0.040 = 5.0 J — "
               "square the extension before anything else.",
    },
    {
        "id": "ks4-changes-in-energy-e03",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the kinetic energy of a car when its "
                "speed is doubled and its mass stays the same.",
        "options": [
            "It doubles",
            "It becomes four times greater",
            "It stays the same, because the mass has not changed",
            "It becomes eight times greater",
        ],
        "correct_index": 1,
        "why": "Ek depends on v², so doubling the speed multiplies the "
               "kinetic energy by 2² = 4.",
    },
    {
        "id": "ks4-changes-in-energy-e04",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg ball moves at 8.0 m/s. Calculate its kinetic "
                "energy.",
        "options": [
            "2.0 J",
            "4.0 J",
            "32 J",
            "16 J",
        ],
        "correct_index": 3,
        "why": "Ek = ½mv² = ½ × 0.50 × 8.0² = ½ × 0.50 × 64 = 16 J.",
    },
    {
        "id": "ks4-changes-in-energy-s01",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 600 g stone is thrown at 12 m/s. Calculate its kinetic "
                "energy.",
        "options": [
            "3.6 J",
            "43.2 J",
            "86.4 J",
            "43 200 J",
        ],
        "correct_index": 1,
        "why": "Convert first: 600 g = 0.600 kg, so Ek = ½ × 0.600 × 12² = "
               "½ × 0.600 × 144 = 43.2 J.",
    },
    {
        "id": "ks4-changes-in-energy-s02",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cyclist and bicycle have a combined mass of 80 kg and "
                "travel at 36 km/h. Calculate their kinetic energy.",
        "options": [
            "400 J",
            "8000 J",
            "51 840 J",
            "4000 J",
        ],
        "correct_index": 3,
        "why": "36 km/h is 10 m/s, so Ek = ½ × 80 × 10² = ½ × 80 × 100 = "
               "4000 J.",
    },
    {
        "id": "ks4-changes-in-energy-s03",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg mass gains 98 J of gravitational potential energy "
                "when it is raised. Calculate the height it was raised. "
                "(g = 9.8 N/kg)",
        "options": [
            "5.0 m",
            "10.0 m",
            "49.0 m",
            "0.20 m",
        ],
        "correct_index": 0,
        "why": "Rearranging Ep = mgh gives h = Ep ÷ (m × g) = 98 ÷ (2.0 × "
               "9.8) = 98 ÷ 19.6 = 5.0 m.",
    },
    {
        "id": "ks4-changes-in-energy-s04",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring stores 8.0 J of elastic potential energy when it is "
                "extended by 0.40 m. Calculate its spring constant.",
        "options": [
            "20 N/m",
            "50 N/m",
            "100 N/m",
            "40 N/m",
        ],
        "correct_index": 2,
        "why": "Rearranging Ee = ½ke² gives k = 2Ee ÷ e² = 16 ÷ 0.16 = "
               "100 N/m.",
    },
    {
        "id": "ks4-changes-in-energy-h01",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball is dropped from a height of 1.8 m. Assuming no energy "
                "is dissipated, calculate its speed just before it lands. "
                "(g = 9.8 N/kg)",
        "options": [
            "4.2 m/s",
            "17.6 m/s",
            "35.3 m/s",
            "5.9 m/s",
        ],
        "correct_index": 3,
        "why": "All the gravitational potential energy becomes kinetic, so "
               "mgh = ½mv²; the mass cancels and v = √(2gh) = √35.28 = "
               "5.9 m/s.",
    },
    {
        "id": "ks4-changes-in-energy-h02",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Car A has a mass of 1000 kg and travels at 30 m/s. Car B has "
                "a mass of 2000 kg and travels at 15 m/s. Compare their "
                "kinetic energies.",
        "options": [
            "They are equal, because doubling the mass makes up for halving "
            "the speed",
            "B has twice the kinetic energy of A, because it has twice the "
            "mass",
            "A has twice the kinetic energy of B, because the speed is "
            "squared but the mass is not",
            "A has four times the kinetic energy of B, because its speed is "
            "twice as great",
        ],
        "correct_index": 2,
        "why": "A stores ½ × 1000 × 900 = 450 000 J and B stores ½ × 2000 × "
               "225 = 225 000 J — halving the speed cuts Ek by four, which "
               "doubling the mass only halves back.",
    },
    {
        "id": "ks4-changes-in-energy-h03",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bow stores 50 J of elastic potential energy. When it "
                "is released, 80% of that energy fills the kinetic "
                "store of a 0.20 kg arrow. Calculate the speed of the "
                "arrow.",
        "options": [
            "20 m/s",
            "22 m/s",
            "200 m/s",
            "400 m/s",
        ],
        "correct_index": 0,
        "why": "The arrow receives 0.80 × 50 = 40 J, so v = √(2Ek ÷ m) "
               "= √(80 ÷ 0.20) = √400 = 20 m/s.",
    },
    {
        "id": "ks4-changes-in-energy-h04",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the kinetic energy of a 1500 kg lorry "
                "travelling at 90 km/h as ½ × 1500 × 90² = 6 075 000 J. "
                "Identify the error and give the correct value.",
        "options": [
            "The mass was not converted to tonnes; 1500 kg is 1.5 t, giving "
            "6075 J",
            "The speed was not converted to m/s; 90 km/h is 25 m/s, giving "
            "468 750 J",
            "The ½ should not be in the equation; the correct value is "
            "12 150 000 J",
            "The speed should not be squared; the correct value is 67 500 J",
        ],
        "correct_index": 1,
        "why": "Ek = ½mv² only works with speed in m/s: 90 km/h ÷ 3.6 = "
               "25 m/s, so Ek = ½ × 1500 × 625 = 468 750 J.",
    },

    # ══ energy-changes-in-systems ════════════════════════════════════════
    {
        "id": "ks4-energy-changes-in-systems-e01",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the specific heat capacity of a substance tells "
                "you.",
        "options": [
            "The energy needed to melt 1 kg of the substance",
            "The energy needed to raise the temperature of 1 kg of the "
            "substance by 1 °C",
            "The temperature the substance reaches when 1 J is supplied",
            "The total thermal energy stored in 1 kg of the substance at "
            "0 °C",
        ],
        "correct_index": 1,
        "why": "Specific heat capacity is energy per kilogram per degree — "
               "which is why its unit is J/kg°C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e02",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the energy needed to raise the temperature of "
                "3.0 kg of water by 20 °C. (c = 4200 J/kg°C)",
        "options": [
            "12 600 J",
            "25 200 J",
            "84 000 J",
            "252 000 J",
        ],
        "correct_index": 3,
        "why": "ΔE = mcΔθ = 3.0 × 4200 × 20 = 252 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e03",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg aluminium block is heated from 18 °C to 38 °C. "
                "Calculate the energy transferred to it. (c = 900 J/kg°C)",
        "options": [
            "9000 J",
            "8100 J",
            "17 100 J",
            "18 000 J",
        ],
        "correct_index": 0,
        "why": "Δθ is the change, 38 − 18 = 20 °C, so ΔE = 0.50 × 900 × 20 = "
               "9000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e04",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water has a specific heat capacity of 4200 J/kg°C, "
                "aluminium 900 J/kg°C, iron 450 J/kg°C and copper "
                "385 J/kg°C. State which needs the most energy to raise 1 kg "
                "of it by 1 °C, and why.",
        "options": [
            "Copper, because it is the best thermal conductor of the four",
            "Iron, because it is the densest of the four materials",
            "Water, because it has the highest specific heat capacity of the "
            "four",
            "Aluminium, because it heats up fastest when used in a saucepan",
        ],
        "correct_index": 2,
        "why": "Specific heat capacity is exactly the energy per kilogram per "
               "degree, so the largest value needs the most energy.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s01",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 200 g copper block is heated from 20 °C to 70 °C. "
                "Calculate the energy transferred. (c = 385 J/kg°C)",
        "options": [
            "1540 J",
            "5390 J",
            "3850 J",
            "3 850 000 J",
        ],
        "correct_index": 2,
        "why": "Convert the mass first: 200 g = 0.200 kg, and Δθ = 50 °C, so "
               "ΔE = 0.200 × 385 × 50 = 3850 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s02",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "5040 J of energy is transferred to 0.60 kg of water. "
                "Calculate the rise in its temperature. (c = 4200 J/kg°C)",
        "options": [
            "2.0 °C",
            "1.2 °C",
            "0.50 °C",
            "8400 °C",
        ],
        "correct_index": 0,
        "why": "Rearranging ΔE = mcΔθ gives Δθ = ΔE ÷ (m × c) = 5040 ÷ "
               "(0.60 × 4200) = 5040 ÷ 2520 = 2.0 °C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s03",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric heater transfers 27 000 J to a 1.5 kg sample of "
                "metal and its temperature rises from 15 °C to 55 °C. "
                "Calculate the specific heat capacity of the metal.",
        "options": [
            "675 J/kg°C",
            "327 J/kg°C",
            "18 000 J/kg°C",
            "450 J/kg°C",
        ],
        "correct_index": 3,
        "why": "Δθ = 55 − 15 = 40 °C, so c = ΔE ÷ (m × Δθ) = 27 000 ÷ (1.5 × "
               "40) = 450 J/kg°C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s04",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the required practical a student measures the specific "
                "heat capacity of an aluminium block and obtains a value "
                "higher than the true 900 J/kg°C. Suggest the reason.",
        "options": [
            "The block was heated for too short a time, so the temperature "
            "rise was too small to measure accurately",
            "Energy was transferred to the surroundings, so more energy was "
            "supplied than the block actually gained",
            "The thermometer was reading the temperature of the room rather "
            "than the temperature of the block",
            "Aluminium expands when it is heated, so its specific heat "
            "capacity rises as the experiment goes on",
        ],
        "correct_index": 1,
        "why": "c is calculated from the energy supplied, so any energy that "
               "escapes to the surroundings makes the measured c too large — "
               "lagging the block reduces the error.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h01",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kW kettle heats 1.5 kg of water from 20 °C to 100 °C. "
                "Assuming no energy is dissipated, calculate the minimum time "
                "this takes. (c = 4200 J/kg°C)",
        "options": [
            "252 s",
            "315 s",
            "15 120 s",
            "252 000 s",
        ],
        "correct_index": 0,
        "why": "ΔE = 1.5 × 4200 × 80 = 504 000 J, and t = E ÷ P = 504 000 ÷ "
               "2000 = 252 s.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h02",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal masses of water (c = 4200 J/kg°C) and copper "
                "(c = 385 J/kg°C) are each supplied with the same amount of "
                "energy. Compare their temperature rises.",
        "options": [
            "Both rise by the same amount, because the energy supplied is the "
            "same",
            "The copper rises about 11 times as much, because its specific "
            "heat capacity is about 11 times smaller",
            "The water rises about 11 times as much, because it can hold far "
            "more thermal energy",
            "The copper rises about 11 times as much, because it is a much "
            "better thermal conductor than water",
        ],
        "correct_index": 1,
        "why": "Δθ = ΔE ÷ (mc), so with m and ΔE fixed the temperature rise "
               "is inversely proportional to c: 4200 ÷ 385 ≈ 11.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h03",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.40 kg aluminium pan (c = 900 J/kg°C) holds 1.2 kg of "
                "water (c = 4200 J/kg°C). Both are heated from 18 °C to "
                "78 °C. Calculate the total energy transferred.",
        "options": [
            "302 400 J",
            "21 600 J",
            "421 200 J",
            "324 000 J",
        ],
        "correct_index": 3,
        "why": "Δθ = 60 °C for both: the pan takes 0.40 × 900 × 60 = 21 600 J "
               "and the water 1.2 × 4200 × 60 = 302 400 J, giving 324 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h04",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The water is heated from 25 °C to 75 °C, "
                "so Δθ = 75 °C and 2.0 kg of it needs 630 000 J.' Determine "
                "the correct energy transferred. (c = 4200 J/kg°C)",
        "options": [
            "630 000 J — the student is right, because the water reaches "
            "75 °C",
            "210 000 J — Δθ should be 25 °C, the temperature the water "
            "started at",
            "420 000 J — Δθ is 50 °C, the difference between the two "
            "temperatures",
            "840 000 J — Δθ should be 100 °C, the two temperatures added "
            "together",
        ],
        "correct_index": 2,
        "why": "Δθ always means final minus initial: 75 − 25 = 50 °C, so "
               "ΔE = 2.0 × 4200 × 50 = 420 000 J.",
    },

    # ══ power ════════════════════════════════════════════════════════════
    {
        "id": "ks4-power-e01",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the definition of power.",
        "options": [
            "The total amount of energy transferred by a device while it is "
            "in use",
            "The size of the force a device can produce",
            "The amount of energy stored inside a device",
            "The rate at which energy is transferred or work is done",
        ],
        "correct_index": 3,
        "why": "Power is a rate — how many joules are transferred each second "
               "— not how many joules there are in total.",
    },
    {
        "id": "ks4-power-e02",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp transfers 1800 J of energy in 30 s. Calculate its "
                "power.",
        "options": [
            "54 000 W",
            "60 W",
            "1.0 W",
            "0.017 W",
        ],
        "correct_index": 1,
        "why": "P = E ÷ t = 1800 ÷ 30 = 60 W, which means 60 joules are "
               "transferred every second.",
    },
    {
        "id": "ks4-power-e03",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of power and what one unit is equivalent to.",
        "options": [
            "The joule (J), equal to 1 watt per second",
            "The newton (N), equal to 1 joule per metre",
            "The watt (W), equal to 1 joule per second",
            "The kilowatt-hour (kWh), equal to 1 joule per hour",
        ],
        "correct_index": 2,
        "why": "Power is energy divided by time, so its unit is joules per "
               "second, given the name watt.",
    },
    {
        "id": "ks4-power-e04",
        "subtopic_slug": "power",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 60 W lamp is switched on for 20 s. Calculate the energy it "
                "transfers.",
        "options": [
            "1200 J",
            "3.0 J",
            "0.33 J",
            "72 000 J",
        ],
        "correct_index": 0,
        "why": "E = Pt = 60 × 20 = 1200 J.",
    },
    {
        "id": "ks4-power-s01",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor transfers 90 000 J of energy in 5.0 minutes. "
                "Calculate its power.",
        "options": [
            "300 W",
            "18 000 W",
            "1500 W",
            "27 000 000 W",
        ],
        "correct_index": 0,
        "why": "Convert the time first: 5.0 minutes = 300 s, so P = 90 000 ÷ "
               "300 = 300 W.",
    },
    {
        "id": "ks4-power-s02",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An 1800 W hairdryer is used for 2.5 minutes. Calculate "
                "the energy transferred.",
        "options": [
            "4500 J",
            "720 J",
            "270 000 J",
            "16 200 000 J",
        ],
        "correct_index": 2,
        "why": "2.5 minutes = 150 s, so E = Pt = 1800 × 150 = 270 000 "
               "J.",
    },
    {
        "id": "ks4-power-s03",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crane lifts a 250 kg load through 12 m in 40 s. Calculate "
                "its useful power output. (g = 9.8 N/kg)",
        "options": [
            "29 400 W",
            "735 W",
            "75 W",
            "1 176 000 W",
        ],
        "correct_index": 1,
        "why": "The work done is mgh = 250 × 9.8 × 12 = 29 400 J, so P = "
               "29 400 ÷ 40 = 735 W.",
    },
    {
        "id": "ks4-power-s04",
        "subtopic_slug": "power",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Machine X transfers 24 000 J in 40 s. Machine Y transfers "
                "36 000 J in 90 s. Determine which is the more powerful, and "
                "by how much.",
        "options": [
            "Y, by 12 000 W, because it transfers more energy in total",
            "Y, by 200 W, because it keeps running for more than twice as "
            "long",
            "They are equally powerful, because the extra time balances the "
            "extra energy",
            "X, by 200 W, because X is 600 W and Y is only 400 W",
        ],
        "correct_index": 3,
        "why": "Power is energy per second: 24 000 ÷ 40 = 600 W for X and "
               "36 000 ÷ 90 = 400 W for Y, so X leads by 200 W.",
    },
    {
        "id": "ks4-power-h01",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift motor raises a 420 kg lift car through 18 m in 24 s. "
                "Calculate the minimum power of the motor. (g = 9.8 N/kg)",
        "options": [
            "74 100 W",
            "315 W",
            "3090 W",
            "172 W",
        ],
        "correct_index": 2,
        "why": "Work done = mgh = 420 × 9.8 × 18 = 74 088 J, and P = W ÷ t = "
               "74 088 ÷ 24 = 3090 W to 3 s.f.",
    },
    {
        "id": "ks4-power-h02",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric motor rated at 750 W must transfer 54 kJ of "
                "energy. Calculate how long it must run, in minutes.",
        "options": [
            "72 minutes",
            "4320 minutes",
            "0.014 minutes",
            "1.2 minutes",
        ],
        "correct_index": 3,
        "why": "t = E ÷ P = 54 000 ÷ 750 = 72 s, and 72 s ÷ 60 = 1.2 minutes.",
    },
    {
        "id": "ks4-power-h03",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kW heater and a 3.0 kW heater each transfer 180 kJ of "
                "energy to a room. Compare the times taken and the amount of "
                "electricity each uses.",
        "options": [
            "The 3.0 kW heater takes 60 s and the 2.0 kW heater 90 s, but "
            "both transfer the same energy, so both use the same amount",
            "The 3.0 kW heater takes 60 s and uses more electricity, because "
            "it draws more power from the mains for every second that it "
            "is switched on",
            "The 2.0 kW heater takes 90 s and uses more electricity, because "
            "it is switched on for longer",
            "Both take the same time, because the energy transferred is the "
            "same in each case",
        ],
        "correct_index": 0,
        "why": "t = E ÷ P gives 90 s and 60 s, but the energy — and so the "
               "electricity used — is 180 kJ either way.",
    },
    {
        "id": "ks4-power-h04",
        "subtopic_slug": "power",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student calculates the power of a pump that raises 300 kg "
                "of water through 8.0 m in 2.0 minutes as 300 × 9.8 × 8.0 ÷ "
                "2.0 = 11 760 W. Identify the error and give the correct "
                "power. (g = 9.8 N/kg)",
        "options": [
            "The value of g is wrong; using g = 10 N/kg gives a power of "
            "12 000 W",
            "The time was left in minutes; 2.0 minutes is 120 s, so the power "
            "is 196 W",
            "The mass should have been converted to grams; the correct power "
            "is 11.76 W",
            "The work done should not include g; the correct power is 1200 W",
        ],
        "correct_index": 1,
        "why": "P = E ÷ t needs time in seconds: 23 520 J ÷ 120 s = 196 W.",
    },

    # ══ energy-transfers-in-a-system ═════════════════════════════════════
    {
        "id": "ks4-energy-transfers-in-a-system-e01",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to energy that is dissipated from a "
                "system.",
        "options": [
            "It is transferred to the thermal stores of the surroundings and "
            "spreads out",
            "It is destroyed by the friction involved, so the total energy "
            "of the system falls",
            "It is stored inside the object, ready to be used again later",
            "It is used up by the moving parts of the machine",
        ],
        "correct_index": 0,
        "why": "Dissipated energy is still there — it has simply spread into "
               "the surroundings, where it is too thinly spread to be "
               "useful.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e02",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two dry metal surfaces rub together inside a machine. "
                "State the store that is filled by the energy wasted at "
                "those surfaces.",
        "options": [
            "The elastic potential store of the two surfaces",
            "The chemical store of the metal",
            "The kinetic store of the machine",
            "The thermal store of the surfaces and the surrounding air",
        ],
        "correct_index": 3,
        "why": "Friction transfers energy by heating, filling the "
               "thermal stores of the surfaces and their surroundings, "
               "where it is too spread out to be useful.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e03",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A filament lamp transfers 100 J of energy electrically and "
                "produces 10 J of light. State how much energy is wasted and "
                "where it goes.",
        "options": [
            "10 J, dissipated to the thermal store of the surroundings",
            "90 J, dissipated to the thermal store of the surroundings",
            "90 J, destroyed by the resistance of the filament",
            "110 J, made up of the light output added to the input",
        ],
        "correct_index": 1,
        "why": "Wasted energy is total input minus useful output: 100 − 10 = "
               "90 J, which warms the lamp and the room.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-e04",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the process by which energy becomes less useful as it "
                "spreads out into the surroundings.",
        "options": [
            "Conservation",
            "Conduction",
            "Dissipation",
            "Insulation",
        ],
        "correct_index": 2,
        "why": "Dissipation is the name for energy spreading into less useful "
               "stores — usually the thermal stores of the surroundings.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s01",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a bouncing ball reaches a lower height after "
                "every bounce.",
        "options": [
            "Gravity becomes stronger as the ball slows down, pulling it back "
            "to the floor sooner each time",
            "Some of the ball's energy is destroyed by the collision each "
            "time it strikes the floor, so there is less of it left to "
            "lift the ball",
            "Some energy is dissipated to thermal stores of the ball, floor "
            "and air at each bounce, leaving less to lift it",
            "The ball loses a little mass each time it is squashed on impact, "
            "so it cannot rise as far",
        ],
        "correct_index": 2,
        "why": "Each impact and each pass through the air moves energy out of "
               "the ball's stores into the surroundings, so less is available "
               "to lift it.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s02",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car is redesigned with a more streamlined shape. Explain "
                "the effect on the energy transferred from the chemical store "
                "of its fuel.",
        "options": [
            "Less fuel is needed, because a streamlined car must have a "
            "smaller mass",
            "Less energy is dissipated to the air, so more of the fuel's "
            "energy fills the useful kinetic store",
            "More energy is dissipated, because the air flows over a "
            "streamlined car faster",
            "There is no change at all, because energy cannot be created or "
            "destroyed whatever shape the car is given",
        ],
        "correct_index": 1,
        "why": "Streamlining cuts the work done against air resistance, so a "
               "larger share of each litre of fuel ends up as useful motion.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s03",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toy car is pushed and rolls to a stop on a level carpet. "
                "Describe the energy transfers, treating the car, carpet and "
                "air as one closed system.",
        "options": [
            "The kinetic store empties and the total energy of the system "
            "falls to zero",
            "The kinetic store empties into the car's chemical store, ready "
            "for the next push",
            "The kinetic store empties and the gravitational potential store "
            "fills instead, even though the carpet it rolls on is "
            "perfectly level",
            "The kinetic store empties into the thermal stores of the carpet, "
            "wheels and air, and the total energy is unchanged",
        ],
        "correct_index": 3,
        "why": "In a closed system the total never changes — the kinetic "
               "store simply drains into thermal stores that are harder to "
               "use.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-s04",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why thick copper cables are used to carry "
                "electricity over long distances.",
        "options": [
            "Thicker cables have a lower resistance, so less energy is "
            "dissipated to the thermal store of the surroundings",
            "Thicker cables have a higher resistance, so more of the energy "
            "is pushed along to the far end of the transmission line",
            "Thicker cables store more electrical energy inside them, so more "
            "is available at the far end",
            "Thicker cables are heavier, so they sag less and lose less "
            "energy to the moving air",
        ],
        "correct_index": 0,
        "why": "Lower resistance means less heating in the cable, so more of "
               "the energy sent actually arrives.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h01",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pendulum hangs from a frictionless pivot inside a sealed "
                "vacuum chamber and is set swinging. Predict what happens to "
                "the height of each swing, and explain.",
        "options": [
            "It stops within a few swings, because energy is always destroyed "
            "as an object moves",
            "It swings a little higher each time, because energy gradually "
            "builds up inside its gravitational potential store",
            "It stops almost immediately, because there is no air left to "
            "push the pendulum along",
            "It keeps swinging to the same height, because there is nothing "
            "to dissipate energy from the closed system",
        ],
        "correct_index": 3,
        "why": "With no air resistance and no friction there is no pathway "
               "out of the system, so energy simply cycles between the "
               "kinetic and gravitational potential stores.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h02",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says: 'A machine cannot run forever because "
                "friction destroys energy.' Evaluate this statement.",
        "options": [
            "The conclusion is right but the reason is wrong — friction "
            "dissipates energy to the surroundings rather than destroying it",
            "Both the conclusion and the reason are right — friction really "
            "does destroy energy as heat",
            "The conclusion is wrong — a machine with no friction at all "
            "would create energy as it ran",
            "The conclusion is wrong — conservation of energy means a machine "
            "can run forever and still deliver useful energy",
        ],
        "correct_index": 0,
        "why": "Energy is never destroyed; friction moves it to the thermal "
               "stores of the surroundings, where it is too spread out to "
               "drive the machine again.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h03",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two identical electric drills do exactly the same useful "
                "work. One has dry, worn bearings and the other has freshly "
                "oiled bearings. Compare the total electrical energy each "
                "one needs.",
        "options": [
            "Both need the same total energy, because the useful work done is "
            "identical",
            "The oiled drill needs more, because the oil adds mass that has "
            "to be moved as well",
            "The dry drill needs more, because more energy is dissipated to "
            "thermal stores at the bearings",
            "The dry drill needs less, because friction helps the bit to grip "
            "and turn the material",
        ],
        "correct_index": 2,
        "why": "The useful output is fixed, so the drill that wastes more at "
               "its bearings must be supplied with more in total.",
    },
    {
        "id": "ks4-energy-transfers-in-a-system-h04",
        "subtopic_slug": "energy-transfers-in-a-system",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a homeowner who already has cavity wall "
                "insulation may decide not to pay for a second layer.",
        "options": [
            "A second layer would trap so much energy that the walls "
            "themselves would overheat",
            "Each extra layer saves less energy than the one before, so the "
            "cost eventually outweighs the saving",
            "A second layer would reverse the direction of the energy "
            "transfer through the wall",
            "Insulation only works as a single layer; a second one conducts "
            "the energy straight back out",
        ],
        "correct_index": 1,
        "why": "The first layer removes the largest share of the transfer; "
               "each further layer cuts a smaller amount, so there is a point "
               "where more insulation is not worth the money.",
    },

    # ══ efficiency ═══════════════════════════════════════════════════════
    {
        "id": "ks4-efficiency-e01",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation for the efficiency of a device.",
        "options": [
            "efficiency = useful output energy ÷ wasted energy",
            "efficiency = total input energy ÷ useful output energy",
            "efficiency = useful output energy ÷ total input energy",
            "efficiency = wasted energy ÷ total input energy",
        ],
        "correct_index": 2,
        "why": "Efficiency is the fraction of everything put in that comes "
               "out usefully, so the denominator is always the total input.",
    },
    {
        "id": "ks4-efficiency-e02",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A motor is supplied with 400 J of energy and does 320 J of "
                "useful work. Calculate its efficiency as a percentage.",
        "options": [
            "125%",
            "80%",
            "20%",
            "0.80%",
        ],
        "correct_index": 1,
        "why": "efficiency = 320 ÷ 400 = 0.80, and 0.80 × 100 = 80%.",
    },
    {
        "id": "ks4-efficiency-e03",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the maximum possible efficiency of any device, and "
                "why.",
        "options": [
            "It depends entirely on the device — some of them can be a good "
            "deal more than 100% efficient",
            "About 90%, because no device can beat a modern LED lamp",
            "0%, because every device eventually wastes all of its energy",
            "1, or 100%, because a device can never usefully output more "
            "energy than it takes in",
        ],
        "correct_index": 3,
        "why": "Energy cannot be created, so the useful output can at best "
               "equal the input — and in practice some is always dissipated.",
    },
    {
        "id": "ks4-efficiency-e04",
        "subtopic_slug": "efficiency",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A kettle is supplied with 250 kJ of energy and 200 kJ "
                "usefully heats the water. Calculate the energy wasted.",
        "options": [
            "50 kJ",
            "200 kJ",
            "450 kJ",
            "0.80 kJ",
        ],
        "correct_index": 0,
        "why": "Wasted energy = total input − useful output = 250 − 200 = "
               "50 kJ.",
    },
    {
        "id": "ks4-efficiency-s01",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lamp has a power input of 60 W and a useful light output "
                "of 9.0 W. Calculate its efficiency as a decimal.",
        "options": [
            "6.7",
            "0.15",
            "0.85",
            "15",
        ],
        "correct_index": 1,
        "why": "Efficiency works with powers just as it does with energies: "
               "9.0 ÷ 60 = 0.15, and a decimal efficiency can never exceed 1.",
    },
    {
        "id": "ks4-efficiency-s02",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electric winch is supplied with 6000 J of energy and the "
                "load it lifts gains 4500 J of gravitational potential "
                "energy. Calculate the efficiency as a percentage.",
        "options": [
            "75%",
            "133%",
            "25%",
            "0.75%",
        ],
        "correct_index": 0,
        "why": "The gain in gravitational potential energy is the useful "
               "output: 4500 ÷ 6000 = 0.75 = 75%.",
    },
    {
        "id": "ks4-efficiency-s03",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A device has an efficiency of 0.40 and produces 120 J of "
                "useful output. Calculate the total energy supplied to it.",
        "options": [
            "48 J",
            "180 J",
            "300 J",
            "168 J",
        ],
        "correct_index": 2,
        "why": "Rearranging efficiency = useful ÷ total gives total = 120 ÷ "
               "0.40 = 300 J — the input must always be larger than the "
               "useful output.",
    },
    {
        "id": "ks4-efficiency-s04",
        "subtopic_slug": "efficiency",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bedroom lamp uses a filament bulb. Suggest the change that "
                "would most increase its efficiency.",
        "options": [
            "Fit a higher power filament bulb so that more light is produced",
            "Fit a lampshade so that less of the light escapes upwards",
            "Leave the lamp switched on for longer so less energy is wasted "
            "warming it up",
            "Replace the filament bulb with an LED, which wastes far less "
            "energy by heating",
        ],
        "correct_index": 3,
        "why": "A filament bulb turns roughly 90% of its input into heating; "
               "an LED turns a far larger share into the useful output, "
               "light.",
    },
    {
        "id": "ks4-efficiency-h01",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station releases 800 MJ of energy from fuel each "
                "second and generates 320 MJ of electrical energy each "
                "second. Cooling water carries away 180 MJ each second. "
                "Calculate the efficiency and the energy wasted each second "
                "in all other ways.",
        "options": [
            "40% efficient, with 300 MJ wasted each second in other ways",
            "40% efficient, with 480 MJ wasted each second in other ways",
            "52% efficient, with 300 MJ wasted each second in other ways",
            "250% efficient, with 180 MJ wasted each second in other ways",
        ],
        "correct_index": 0,
        "why": "Efficiency = 320 ÷ 800 = 0.40, and the total waste of 480 MJ "
               "less the 180 MJ in the cooling water leaves 300 MJ.",
    },
    {
        "id": "ks4-efficiency-h02",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Motor P draws 500 W and delivers 350 W usefully. Motor Q "
                "draws 1200 W and delivers 900 W usefully. Determine which "
                "motor is the more efficient.",
        "options": [
            "P, because it wastes only 150 W while Q wastes twice as much",
            "P, because it uses less electrical power in total than Q does",
            "They are equally efficient, because both waste some energy by "
            "heating",
            "Q, because its efficiency is 0.75 compared with P's 0.70",
        ],
        "correct_index": 3,
        "why": "Efficiency compares useful output with input, not with the "
               "waste: 900 ÷ 1200 = 0.75 beats 350 ÷ 500 = 0.70.",
    },
    {
        "id": "ks4-efficiency-h03",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain how regenerative braking increases the efficiency of "
                "a hybrid car on a journey with many stops.",
        "options": [
            "It removes friction from the brakes completely, so no energy at "
            "all is dissipated whenever the car slows down",
            "Kinetic energy that would be dissipated by heating in the "
            "brakes is stored in the battery instead and reused",
            "It generates extra energy every time the car slows, so the "
            "efficiency can rise above 100%",
            "It reduces the mass of the car, so less energy is needed to "
            "accelerate away from each stop",
        ],
        "correct_index": 1,
        "why": "Recovering braking energy into the battery means a larger "
               "share of the fuel's energy ends up moving the car rather than "
               "warming the brakes.",
    },
    {
        "id": "ks4-efficiency-h04",
        "subtopic_slug": "efficiency",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A machine produces 2400 J of useful output and wastes "
                "1800 J. A student calculates its efficiency as 2400 ÷ 1800 = "
                "1.33. Identify the error and give the correct efficiency.",
        "options": [
            "There is no error — 1.33 is right because the useful output is "
            "larger than the waste",
            "The wasted energy should have been on top; the efficiency is "
            "0.75",
            "The denominator should be the total input of 4200 J, giving an "
            "efficiency of 0.57",
            "The denominator should be the useful output, giving an "
            "efficiency of 1.00",
        ],
        "correct_index": 2,
        "why": "The total input is useful plus wasted, 2400 + 1800 = 4200 J, "
               "so efficiency = 2400 ÷ 4200 = 0.57 — never more than 1.",
    },

    # ══ energy-resources ═════════════════════════════════════════════════
    {
        "id": "ks4-energy-resources-e01",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by describing an energy resource "
                "as renewable.",
        "options": [
            "It releases no carbon dioxide at any point in its use",
            "It is replaced as fast as it is used, so it will not run "
            "out",
            "It can be used to generate electricity anywhere in the "
            "world",
            "It can be stored and then used at whatever moment it is "
            "needed",
        ],
        "correct_index": 1,
        "why": "A renewable resource is replenished at least as fast as "
               "it is being used — a statement about supply, not about "
               "pollution.",
    },
    {
        "id": "ks4-energy-resources-e02",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which resource generates electricity without using a "
                "turbine.",
        "options": [
            "Solar photovoltaic cells",
            "Wind farms",
            "Tidal barrages",
            "Coal-fired power stations",
        ],
        "correct_index": 0,
        "why": "Photovoltaic cells convert light directly into electricity; "
               "every other method here spins a turbine that drives a "
               "generator.",
    },
    {
        "id": "ks4-energy-resources-e03",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Name the gas released when fossil fuels are burned that adds "
                "most to the greenhouse effect.",
        "options": [
            "Sulfur dioxide",
            "Nitrogen",
            "Carbon dioxide",
            "Oxygen",
        ],
        "correct_index": 2,
        "why": "Burning the carbon in coal, oil and gas releases carbon "
               "dioxide, the greenhouse gas driving climate change.",
    },
    {
        "id": "ks4-energy-resources-e04",
        "subtopic_slug": "energy-resources",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the source of the energy used in a geothermal "
                "power station.",
        "options": [
            "Sunlight warming the surface of the ground during the day",
            "Natural gas that is trapped in the rocks underground",
            "The tides forcing sea water through underground channels",
            "Hot rock deep underground, heated from inside the Earth",
        ],
        "correct_index": 3,
        "why": "Geothermal stations pump water down to hot rock; the "
               "inside of the Earth keeps that rock hot, so the supply "
               "is renewable.",
    },
    {
        "id": "ks4-energy-resources-s01",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why bio-fuels are classed as renewable.",
        "options": [
            "They release no carbon dioxide at all when they are burned",
            "They are made only from waste, so no new material is ever needed",
            "They are refined from crude oil, which is replaced continuously "
            "underground",
            "The crops they are made from can be regrown within a human "
            "lifetime",
        ],
        "correct_index": 3,
        "why": "A resource is renewable when it is replenished as fast as it "
               "is used, and a bio-fuel crop can simply be planted again.",
    },
    {
        "id": "ks4-energy-resources-s02",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the sequence of energy transfers in a coal-fired "
                "power station.",
        "options": [
            "Chemical store of coal → electrical work → thermal store of the "
            "water → kinetic store of the turbine blades",
            "Thermal store of coal → radiation → chemical store of the steam "
            "→ kinetic store of the generator",
            "Chemical store of coal → thermal store of water → kinetic store "
            "of the turbine and generator → electrical work",
            "Nuclear store of coal → thermal store of water → kinetic store "
            "of the turbine → electrical work",
        ],
        "correct_index": 2,
        "why": "Burning coal empties a chemical store into the thermal store "
               "of water, the steam spins the turbine, and the generator "
               "transfers the energy on by electrical work.",
    },
    {
        "id": "ks4-energy-resources-s03",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a country that has built many wind farms still "
                "keeps its gas-fired power stations.",
        "options": [
            "Gas stations can be switched on whenever there is little wind, "
            "so demand is always met",
            "Gas stations release less carbon dioxide per unit of electricity "
            "than wind farms do",
            "Wind farms are not able to supply electricity to the national "
            "grid",
            "Gas is a renewable resource, so keeping it costs the country "
            "nothing",
        ],
        "correct_index": 0,
        "why": "Wind is intermittent, so a resource that can be turned up on "
               "demand is still needed to guarantee supply.",
    },
    {
        "id": "ks4-energy-resources-s04",
        "subtopic_slug": "energy-resources",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the environmental impact of a hydroelectric dam with "
                "that of a gas-fired power station.",
        "options": [
            "Both release similar amounts of carbon dioxide, but the dam is "
            "much cheaper to build and run",
            "The dam emits no carbon dioxide but floods land and destroys "
            "habitats; the gas station emits carbon dioxide but uses less "
            "land",
            "The dam has no environmental impact at all, because "
            "hydroelectricity is a renewable resource",
            "The gas station has no environmental impact at all, because the "
            "carbon dioxide that it releases is all reabsorbed again by "
            "the plants and trees growing nearby",
        ],
        "correct_index": 1,
        "why": "Renewable does not mean impact-free — a dam's cost is paid in "
               "flooded habitat rather than in carbon dioxide.",
    },
    {
        "id": "ks4-energy-resources-h01",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that replacing every coal-fired power "
                "station with solar farms would immediately solve a "
                "country's electricity problems.",
        "options": [
            "The claim is correct, because solar farms release no carbon "
            "dioxide and so have no drawbacks",
            "The claim is wrong, because solar panels release far more "
            "carbon dioxide over their whole lifetime than a coal-fired "
            "station ever does",
            "The claim is too simple, because solar output is intermittent, "
            "so storage or backup is still needed at night and in winter",
            "The claim is wrong, because electricity from solar farms cannot "
            "be fed into the national grid",
        ],
        "correct_index": 2,
        "why": "Solar cuts carbon dioxide sharply, but demand does not stop "
               "when the sun sets, so a reliable supply still needs storage "
               "or another resource behind it.",
    },
    {
        "id": "ks4-energy-resources-h02",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A power station switches from coal to bio-fuel and "
                "claims that its carbon dioxide emissions are now zero. "
                "Evaluate this claim.",
        "options": [
            "Correct — burning a bio-fuel releases no carbon dioxide at "
            "all",
            "Wrong — burning it does release carbon dioxide, but "
            "roughly as much as the crop absorbed while growing, so "
            "little is added overall",
            "Correct — the growing crop absorbs the carbon dioxide at "
            "the moment it leaves the chimney",
            "Wrong — bio-fuel releases far more carbon dioxide for each "
            "joule than coal does, and nothing absorbs any of it",
        ],
        "correct_index": 1,
        "why": "Carbon neutral means the carbon released was taken out "
               "of the air recently by the crop — not that no carbon "
               "dioxide leaves the chimney.",
    },
    {
        "id": "ks4-energy-resources-h03",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A remote island has strong, steady tides, frequent thick "
                "cloud and only light winds. Determine the most suitable "
                "renewable resource for its electricity, and justify your "
                "choice.",
        "options": [
            "Solar, because photovoltaic cells still work well on cloudy days",
            "Wind, because the turbines can always be built taller in order "
            "to reach the faster moving air higher up",
            "Geothermal, because every island sits on hot volcanic rock",
            "Tidal, because the tides there are strong and predictable, so "
            "the output can be relied on",
        ],
        "correct_index": 3,
        "why": "Tides are driven by the Moon rather than the weather, so on "
               "this island they are the one renewable resource whose output "
               "can be predicted.",
    },
    {
        "id": "ks4-energy-resources-h04",
        "subtopic_slug": "energy-resources",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why electricity from a wind farm is not free of "
                "environmental impact, even though no fuel is burned.",
        "options": [
            "Manufacturing and installing the turbines uses energy and "
            "materials, and they cause noise, visual impact and a risk to "
            "birds",
            "The turbines burn a small amount of fuel to start themselves "
            "turning, which releases carbon dioxide into the air",
            "The turbines have no impact at all once they are installed, so "
            "the statement being explained is simply incorrect",
            "The turbines must be backed by a coal station running at all "
            "times somewhere on the grid, and that is their only real "
            "environmental impact",
        ],
        "correct_index": 0,
        "why": "Every resource carries some impact — for wind it lies in "
               "building the turbines and in what they do to the landscape "
               "and wildlife, not in emissions while generating.",
    },

    # ══ thermal-conductivity (Triple Science only) ═══════════════════════
    {
        "id": "ks4-thermal-conductivity-e01",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what the thermal conductivity of a material measures.",
        "options": [
            "The temperature the material can reach before it melts",
            "The amount of thermal energy the material can store",
            "The thickness of the material needed to stop energy transfer",
            "How quickly the material transfers thermal energy by conduction",
        ],
        "correct_index": 3,
        "why": "Thermal conductivity is a rate property — the higher it is, "
               "the faster energy passes through for the same thickness and "
               "temperature difference.",
    },
    {
        "id": "ks4-thermal-conductivity-e02",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect on the rate of energy transfer "
                "through the wall of a house when the temperature "
                "difference between the inside and the outside becomes "
                "larger.",
        "options": [
            "It decreases, because the wall takes longer to warm "
            "through",
            "It stays the same, because the thickness of the wall has "
            "not changed",
            "It increases, because a larger temperature difference "
            "drives a faster transfer",
            "It falls to zero, because the wall acts as an insulator",
        ],
        "correct_index": 2,
        "why": "For the same wall, the rate of transfer by conduction "
               "rises as the temperature difference across it rises — "
               "which is why a house cools fastest on the coldest days.",
    },
    {
        "id": "ks4-thermal-conductivity-e03",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the unit of thermal conductivity.",
        "options": [
            "W/m·K",
            "J/kg°C",
            "J/s",
            "W/m²",
        ],
        "correct_index": 0,
        "why": "Thermal conductivity is watts transferred per metre of "
               "thickness per kelvin of temperature difference, so its unit "
               "is W/m·K.",
    },
    {
        "id": "ks4-thermal-conductivity-e04",
        "subtopic_slug": "thermal-conductivity",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State the effect of making a layer of loft insulation "
                "thicker.",
        "options": [
            "More energy is transferred through the roof each second",
            "Less energy is transferred through the roof each second",
            "The rate of energy transfer is unchanged, because the material "
            "is the same",
            "Energy transfer through the roof stops completely",
        ],
        "correct_index": 1,
        "why": "For the same temperature difference, a greater thickness of "
               "the same material slows the rate of transfer — though it "
               "never reduces it to zero.",
    },
    {
        "id": "ks4-thermal-conductivity-s01",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A metal spoon and a wooden spoon are left standing in a pan "
                "of hot soup. Explain why the handle of the metal spoon feels "
                "hotter after a minute.",
        "options": [
            "Metal has a far higher thermal conductivity, so energy is "
            "transferred along it to the handle much faster",
            "Metal has a far higher specific heat capacity, so it stores a "
            "great deal more energy in every kilogram of the spoon",
            "Metal is denser than wood, so it holds more of the soup's "
            "thermal energy inside it",
            "Metal absorbs more infrared radiation from the soup because its "
            "surface is shiny",
        ],
        "correct_index": 0,
        "why": "Free electrons in the metal carry energy to the handle within "
               "seconds; wood has none, so its handle stays cool.",
    },
    {
        "id": "ks4-thermal-conductivity-s02",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain how filling a cavity wall with foam reduces the rate "
                "of energy transfer out of a house.",
        "options": [
            "The foam reflects the thermal radiation back into the house so "
            "that no energy at all can escape out through the wall",
            "The foam traps small pockets of air, which has a very low "
            "thermal conductivity and cannot circulate by convection",
            "The foam has a high specific heat capacity, so it absorbs all of "
            "the energy that reaches it",
            "The foam seals the wall completely, which stops thermal energy "
            "transfer altogether",
        ],
        "correct_index": 1,
        "why": "Air is one of the best insulators there is, and holding it in "
               "small pockets stops convection currents carrying the energy "
               "across the cavity.",
    },
    {
        "id": "ks4-thermal-conductivity-s03",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A hot water tank is fitted with a foam jacket. Describe how "
                "the rate of energy transfer changes as the jacket is made "
                "thicker and thicker.",
        "options": [
            "The rate rises steadily, because a thicker jacket has more "
            "particles available to carry the energy",
            "The rate falls to zero once the jacket is thick enough, because "
            "the tank is then perfectly insulated",
            "The rate is unchanged, because only the temperature difference "
            "matters and not the thickness",
            "The rate falls as the jacket gets thicker, but never reaches "
            "zero, because no material is a perfect insulator",
        ],
        "correct_index": 3,
        "why": "Insulation slows conduction rather than stopping it, so a "
               "thicker jacket always leaks a little energy, just more "
               "slowly.",
    },
    {
        "id": "ks4-thermal-conductivity-s04",
        "subtopic_slug": "thermal-conductivity",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "In the required practical on insulators, a student wraps "
                "identical beakers of hot water in different materials and "
                "records the temperature each minute. State the variables "
                "that must be controlled for a fair comparison.",
        "options": [
            "The type of insulating material used and the colour of each "
            "beaker",
            "The temperature of the room only, since the apparatus fixes "
            "everything else",
            "The starting temperature, the volume of water, the thickness of "
            "the material and the surface area",
            "The final temperature reached by each beaker and the length of "
            "time that each one is left standing",
        ],
        "correct_index": 2,
        "why": "The material is the independent variable, so everything else "
               "that could change the rate of cooling has to be kept the "
               "same.",
    },
    {
        "id": "ks4-thermal-conductivity-h01",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Two identical houses are kept at the same inside "
                "temperature on the same cold day. House A has 100 mm of loft "
                "insulation and House B has 200 mm of the same material. "
                "Compare the rate of energy transfer through the two roofs.",
        "options": [
            "The rates are the same, because the temperature difference "
            "across both roofs is identical",
            "House B loses energy through its roof at about half the rate, "
            "because doubling the thickness roughly halves the rate",
            "House B loses energy at about twice the rate, because there is "
            "twice as much material to carry the energy through",
            "House B loses no energy through its roof, because 200 mm is "
            "enough to stop conduction completely",
        ],
        "correct_index": 1,
        "why": "For the same material and temperature difference the rate of "
               "transfer is inversely proportional to thickness, so twice the "
               "insulation roughly halves the loss.",
    },
    {
        "id": "ks4-thermal-conductivity-h02",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A vacuum flask has a vacuum sealed between its double walls. "
                "Explain why this is so effective at keeping a drink hot.",
        "options": [
            "The vacuum reflects thermal radiation from the drink straight "
            "back into the liquid",
            "The vacuum has a very high specific heat capacity, so it "
            "absorbs hardly any energy from the hot drink itself",
            "There are almost no particles in the vacuum, so there is almost "
            "no conduction or convection across the gap",
            "The vacuum is at a very low temperature, so energy is "
            "transferred into it extremely slowly",
        ],
        "correct_index": 2,
        "why": "Conduction and convection both need particles to carry the "
               "energy, and a vacuum has almost none.",
    },
    {
        "id": "ks4-thermal-conductivity-h03",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "In an insulation investigation, water in a beaker wrapped in "
                "bubble wrap cooled from 80 °C to 62 °C in 10 minutes. An "
                "identical beaker wrapped in newspaper cooled from 80 °C to "
                "55 °C in the same time. Determine the better insulator and "
                "justify your answer.",
        "options": [
            "Bubble wrap, because its rate of cooling is 1.8 °C per minute "
            "compared with 2.5 °C per minute for the newspaper",
            "Newspaper, because its water reached the lower temperature, "
            "showing that it released more energy",
            "Bubble wrap, because it is the thicker material and therefore "
            "holds more thermal energy inside it",
            "Neither, because the two materials have different masses and so "
            "the comparison cannot fairly be made at all here",
        ],
        "correct_index": 0,
        "why": "The better insulator is the one that lets energy out more "
               "slowly, so the smaller rate of cooling wins.",
    },
    {
        "id": "ks4-thermal-conductivity-h04",
        "subtopic_slug": "thermal-conductivity",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'Fibreglass insulates well because glass "
                "fibres are poor conductors and they stop the energy "
                "escaping.' Identify what is wrong with this explanation.",
        "options": [
            "Nothing is wrong — the glass fibres themselves are the whole "
            "reason that fibreglass insulates a cold loft so very well",
            "Glass is a good conductor, so fibreglass insulates only because "
            "it is laid in a thick layer",
            "The fibres do stop the energy, but the real reason is that glass "
            "reflects infrared radiation",
            "Insulators slow energy transfer rather than stop it, and most "
            "of the effect comes from air trapped between the fibres",
        ],
        "correct_index": 3,
        "why": "Fibreglass works mainly by holding still air, whose thermal "
               "conductivity is about 40 times lower than glass — and even "
               "then it only slows the transfer.",
    },
]
