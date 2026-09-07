"""Chemistry · Energy changes — exothermic/endothermic, profiles, cells, fuel
cells and bond energies.

These probe the three places a KS4 class reliably goes wrong on this topic:
reading the temperature of the SURROUNDINGS backwards from what the reaction
does; measuring activation energy from the reactants to the products instead
of from the reactants to the PEAK; and subtracting bond energies the wrong way
round so an exothermic reaction comes out positive. Every reaction profile is
described fully in words — no question needs a figure. Every bond energy used
in a calculation is stated in the stem, and the arithmetic in each `why` is
the arithmetic a student can check.
"""

TOPIC = "energy-changes"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── exothermic-endothermic ──────────────────────────────────────────
    {
        "id": "ks4-exothermic-endothermic-e01",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which one of these processes is endothermic.",
        "options": [
            "Thermal decomposition of calcium carbonate",
            "Neutralisation of hydrochloric acid by sodium hydroxide",
            "Combustion of methane in a gas burner",
            "Respiration of glucose in muscle cells",
        ],
        "correct_index": 0,
        "why": "Thermal decomposition takes energy in from the surroundings "
               "to break the compound apart, so it is endothermic; the other "
               "three all release energy.",
    },
    {
        "id": "ks4-exothermic-endothermic-e02",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student dissolves ammonium nitrate in water in a "
                "polystyrene cup. State what happens to the temperature of "
                "the solution, and why.",
        "options": [
            "It rises, because dissolving a solid always releases energy to "
            "the water",
            "It falls, because dissolving ammonium nitrate takes energy in "
            "from the water",
            "It rises, because the process is endothermic and endothermic "
            "means heating up",
            "It stays the same, because dissolving is a physical change and "
            "not a chemical one",
        ],
        "correct_index": 1,
        "why": "Dissolving ammonium nitrate is endothermic — it absorbs "
               "energy from the water, so the water cools.",
    },
    {
        "id": "ks4-exothermic-endothermic-e03",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Which statement about the energy stored in the products of "
                "an exothermic reaction is correct?",
        "options": [
            "The products store more energy than the reactants, so energy is "
            "taken in",
            "The products and reactants store equal energy, so no energy is "
            "transferred at all",
            "The products store less energy than the reactants, so energy is "
            "given out",
            "The products store less energy than the reactants, so energy is "
            "taken in",
        ],
        "correct_index": 2,
        "why": "Exothermic means the products sit at a lower energy level "
               "than the reactants, and that difference is released to the "
               "surroundings as heat.",
    },
    {
        "id": "ks4-exothermic-endothermic-e04",
        "subtopic_slug": "exothermic-endothermic",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the sign of ΔH for an endothermic reaction, and what "
                "happens to the temperature of the surroundings.",
        "options": [
            "ΔH is negative and the surroundings get colder",
            "ΔH is negative and the surroundings get hotter",
            "ΔH is positive and the surroundings get hotter",
            "ΔH is positive and the surroundings get colder",
        ],
        "correct_index": 3,
        "why": "An endothermic reaction takes energy in, so ΔH is positive "
               "and the surroundings lose that energy and cool down.",
    },
    {
        "id": "ks4-exothermic-endothermic-s01",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a calorimetry experiment, 50 g of solution cools from "
                "21.0 °C to 15.0 °C. Using c = 4.18 J/g°C, calculate the "
                "energy absorbed by the reaction.",
        "options": [
            "3135 J",
            "1254 J",
            "4389 J",
            "7524 J",
        ],
        "correct_index": 1,
        "why": "Q = mcΔT uses the temperature CHANGE, 6.0 °C, so "
               "Q = 50 × 4.18 × 6.0 = 1254 J.",
    },
    {
        "id": "ks4-exothermic-endothermic-s02",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A self-heating food can works using the reaction between "
                "calcium oxide and water. Explain why this reaction is "
                "suitable for the job.",
        "options": [
            "It is endothermic, so it takes energy from the food and warms it",
            "It is endothermic, so it releases energy once the water is added",
            "It is exothermic, so it absorbs energy from the surroundings and "
            "stores it",
            "It is exothermic, so it releases energy to the surroundings and "
            "warms the food",
        ],
        "correct_index": 3,
        "why": "Calcium oxide reacting with water is exothermic, and the "
               "energy released passes out to the can and its contents.",
    },
    {
        "id": "ks4-exothermic-endothermic-s03",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student heats water with a spirit burner and calculates "
                "an energy transfer smaller than the accepted value. Suggest "
                "the most likely reason.",
        "options": [
            "Energy was lost to the surroundings and to the apparatus",
            "The thermometer was read to the nearest 0.5 °C instead of 0.1 °C",
            "The water had a higher specific heat capacity than 4.18 J/g°C",
            "The combustion reaction was endothermic rather than exothermic",
        ],
        "correct_index": 0,
        "why": "In an open calorimetry set-up some of the energy released "
               "never reaches the water, so the measured value is always an "
               "underestimate.",
    },
    {
        "id": "ks4-exothermic-endothermic-s04",
        "subtopic_slug": "exothermic-endothermic",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify the pair of changes that are BOTH exothermic.",
        "options": [
            "Photosynthesis in a leaf and the combustion of petrol",
            "Thermal decomposition of limestone and the neutralisation of an "
            "acid",
            "Oxidation of iron in a hand warmer and the combustion of methane",
            "Dissolving ammonium nitrate and the respiration of glucose",
        ],
        "correct_index": 2,
        "why": "Both the oxidation of iron and the combustion of methane "
               "release energy to the surroundings, so both are exothermic.",
    },
    {
        "id": "ks4-exothermic-endothermic-h01",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student mixes 25 cm3 of hydrochloric acid with 25 cm3 of "
                "sodium hydroxide solution and the temperature rises by "
                "6.5 °C. The experiment is repeated with 50 cm3 of each "
                "solution at the same concentrations. Predict the "
                "temperature rise.",
        "options": [
            "About 13.0 °C, because twice as much energy is released",
            "About 3.3 °C, because the energy is shared between twice as much "
            "solution",
            "About 6.5 °C, because the energy released and the mass of "
            "solution both double",
            "About 26.0 °C, because the acid volume and the alkali volume "
            "both double",
        ],
        "correct_index": 2,
        "why": "Doubling both amounts doubles Q and doubles m, and "
               "ΔT = Q ÷ (m × c), so the temperature rise is unchanged.",
    },
    {
        "id": "ks4-exothermic-endothermic-h02",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction transfers 2508 J to 120 g of solution. Using "
                "c = 4.18 J/g°C, determine the temperature rise of the "
                "solution.",
        "options": [
            "5.0 °C",
            "20.9 °C",
            "600.0 °C",
            "0.2 °C",
        ],
        "correct_index": 0,
        "why": "Rearranging Q = mcΔT gives ΔT = Q ÷ (m × c) = "
               "2508 ÷ (120 × 4.18) = 5.0 °C.",
    },
    {
        "id": "ks4-exothermic-endothermic-h03",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two students measure the temperature rise of the same "
                "neutralisation using the same volumes and concentrations. "
                "Student A uses an open glass beaker; student B uses a "
                "polystyrene cup with a lid. Evaluate whose result is closer "
                "to the true value.",
        "options": [
            "Student A, because the glass beaker conducts heat back into "
            "the solution from the warm room air",
            "Student A, because a glass beaker measures the volumes more "
            "accurately",
            "Neither, because the container cannot affect the temperature "
            "rise measured",
            "Student B, because the insulated cup and lid reduce the energy "
            "lost to the surroundings",
        ],
        "correct_index": 3,
        "why": "Less energy escapes from an insulated, covered container, so "
               "more of the energy released stays in the solution and the "
               "measured rise is closer to the true value.",
    },
    {
        "id": "ks4-exothermic-endothermic-h04",
        "subtopic_slug": "exothermic-endothermic",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Citric acid and sodium hydrogencarbonate "
                "make the beaker feel cold, so the reaction is exothermic — "
                "it gives its coldness out to the surroundings.' Identify "
                "the error.",
        "options": [
            "The reaction is exothermic, but the energy is released as "
            "light rather than heat",
            "The reaction is endothermic — it takes energy from the "
            "surroundings, which is why they cool",
            "The reaction is exothermic, but the beaker is a poor conductor "
            "so it feels cold",
            "The reaction is neither exothermic nor endothermic — a "
            "temperature fall shows no energy has been transferred",
        ],
        "correct_index": 1,
        "why": "Coldness is never transferred; the mixture absorbs energy "
               "from the surroundings, so the surroundings cool and the "
               "reaction is endothermic.",
    },

    # ── reaction-profiles ───────────────────────────────────────────────
    {
        "id": "ks4-reaction-profiles-e01",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a reaction profile, state what the vertical distance "
                "from the reactant energy level up to the peak of the curve "
                "represents.",
        "options": [
            "The overall energy change, ΔH",
            "The activation energy, Ea",
            "The energy stored in the products",
            "The energy released when the bonds in the products form",
        ],
        "correct_index": 1,
        "why": "The peak is the energy barrier, and the climb from the "
               "reactants up to it is the activation energy.",
    },
    {
        "id": "ks4-reaction-profiles-e02",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile shows the products lying 45 kJ/mol above "
                "the reactants. State the type of reaction and the sign of "
                "ΔH.",
        "options": [
            "Exothermic, ΔH = −45 kJ/mol",
            "Exothermic, ΔH = +45 kJ/mol",
            "Endothermic, ΔH = −45 kJ/mol",
            "Endothermic, ΔH = +45 kJ/mol",
        ],
        "correct_index": 3,
        "why": "Products above the reactants means energy has been taken in, "
               "which is endothermic and gives a positive ΔH.",
    },
    {
        "id": "ks4-reaction-profiles-e03",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the x-axis of a reaction profile shows.",
        "options": [
            "The progress of the reaction, from reactants to products",
            "The time in seconds that has passed since the reaction started",
            "The temperature of the reaction mixture",
            "The concentration of reactants still remaining",
        ],
        "correct_index": 0,
        "why": "The horizontal axis tracks how far the reaction has got, not "
               "how long it has taken.",
    },
    {
        "id": "ks4-reaction-profiles-e04",
        "subtopic_slug": "reaction-profiles",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why even a strongly exothermic reaction still needs "
                "an input of energy before it will begin.",
        "options": [
            "Because the products must be raised above the reactants before "
            "energy can be released",
            "Because the reaction is endothermic until the activation energy "
            "has been supplied",
            "Because the activation energy barrier must be overcome before "
            "the existing bonds can break",
            "Because a catalyst has to be added before any reaction is able "
            "to start",
        ],
        "correct_index": 2,
        "why": "Every reaction has an activation energy barrier — energy "
               "must be supplied to break the existing bonds before new ones "
               "can form and release energy.",
    },
    {
        "id": "ks4-reaction-profiles-s01",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction profile shows the reactants at 250 kJ/mol, the "
                "peak at 380 kJ/mol and the products at 190 kJ/mol. "
                "Calculate the activation energy.",
        "options": [
            "60 kJ/mol",
            "190 kJ/mol",
            "130 kJ/mol",
            "630 kJ/mol",
        ],
        "correct_index": 2,
        "why": "Activation energy is measured from the reactant level up to "
               "the peak: 380 − 250 = 130 kJ/mol.",
    },
    {
        "id": "ks4-reaction-profiles-s02",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a reaction profile the reactants sit at 210 kJ/mol and "
                "ΔH is +85 kJ/mol. Determine the energy level of the "
                "products.",
        "options": [
            "295 kJ/mol",
            "125 kJ/mol",
            "85 kJ/mol",
            "210 kJ/mol",
        ],
        "correct_index": 0,
        "why": "A positive ΔH means the products sit above the reactants, so "
               "their level is 210 + 85 = 295 kJ/mol.",
    },
    {
        "id": "ks4-reaction-profiles-s03",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reaction X has an activation energy of 40 kJ/mol and "
                "reaction Y has an activation energy of 210 kJ/mol. Both are "
                "exothermic. Predict which is faster at room temperature and "
                "explain why.",
        "options": [
            "Y, because a larger activation energy means more energy is "
            "released once the reaction gets going",
            "Y, because a bigger barrier gives the particles more energy",
            "Neither — they react at the same rate because both are "
            "exothermic",
            "X, because more of its colliding particles have enough energy "
            "to clear the lower barrier",
        ],
        "correct_index": 3,
        "why": "A lower activation energy means a greater proportion of "
               "collisions carry enough energy to react, so the reaction is "
               "faster.",
    },
    {
        "id": "ks4-reaction-profiles-s04",
        "subtopic_slug": "reaction-profiles",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe the shape of the curve on a reaction profile for "
                "an endothermic reaction.",
        "options": [
            "It rises to a peak and then falls to a level below where it "
            "started",
            "It rises to a peak and then falls to a level above where it "
            "started",
            "It falls steadily from reactants to products with no peak at all",
            "It rises steadily from reactants to products with no peak at all",
        ],
        "correct_index": 1,
        "why": "Every reaction has an activation energy peak, and in an "
               "endothermic reaction the products end up higher than the "
               "reactants.",
    },
    {
        "id": "ks4-reaction-profiles-h01",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A reaction has an activation energy of 145 kJ/mol and "
                "ΔH = −60 kJ/mol. Determine the activation energy of the "
                "reverse reaction.",
        "options": [
            "205 kJ/mol",
            "85 kJ/mol",
            "145 kJ/mol",
            "60 kJ/mol",
        ],
        "correct_index": 0,
        "why": "The reverse reaction starts from the products, 60 kJ/mol "
               "below the reactants, so it must climb 145 + 60 = 205 kJ/mol "
               "to reach the same peak.",
    },
    {
        "id": "ks4-reaction-profiles-h02",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two profiles are drawn for one reaction, catalysed and "
                "uncatalysed. Both start at 300 kJ/mol and end at "
                "180 kJ/mol; the uncatalysed peak is 465 kJ/mol and the "
                "catalysed peak is 390 kJ/mol. Calculate the fall in "
                "activation energy and state the effect on ΔH.",
        "options": [
            "A fall of 165 kJ/mol; ΔH becomes −45 kJ/mol",
            "A fall of 75 kJ/mol; ΔH is unchanged at −120 kJ/mol",
            "A fall of 75 kJ/mol; ΔH becomes −195 kJ/mol",
            "A fall of 90 kJ/mol; ΔH is unchanged at +120 kJ/mol",
        ],
        "correct_index": 1,
        "why": "465 − 300 = 165 kJ/mol and 390 − 300 = 90 kJ/mol, a fall of "
               "75 kJ/mol, while the reactant and product levels are "
               "untouched so ΔH stays at 180 − 300 = −120 kJ/mol.",
    },
    {
        "id": "ks4-reaction-profiles-h03",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A mixture of hydrogen and oxygen can sit in a sealed flask "
                "for years without reacting, even though the reaction is "
                "strongly exothermic. Explain why.",
        "options": [
            "The reaction is exothermic, so the surroundings have to be "
            "cooled down before it is able to start",
            "ΔH is negative, and a negative ΔH means a reaction cannot "
            "start on its own",
            "The activation energy is high, so almost no collisions have "
            "enough energy at room temperature",
            "The gases stay unreactive until a catalyst raises their "
            "activation energy",
        ],
        "correct_index": 2,
        "why": "How much energy a reaction releases says nothing about how "
               "fast it goes — a high activation energy means hardly any "
               "collisions succeed until a spark supplies it.",
    },
    {
        "id": "ks4-reaction-profiles-h04",
        "subtopic_slug": "reaction-profiles",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Reaction P has reactants at 100 kJ/mol, a peak at "
                "250 kJ/mol and products at 40 kJ/mol. Reaction Q has "
                "reactants at 100 kJ/mol, a peak at 180 kJ/mol and products "
                "at 160 kJ/mol. Compare the two reactions.",
        "options": [
            "Both have ΔH = −60 kJ/mol, but their activation energies differ",
            "Both are exothermic, but Q has the larger activation energy",
            "P is endothermic with Ea = 150 kJ/mol; Q is exothermic with "
            "Ea = 80 kJ/mol",
            "P is exothermic with Ea = 150 kJ/mol; Q is endothermic with "
            "Ea = 80 kJ/mol",
        ],
        "correct_index": 3,
        "why": "P's products lie 60 kJ/mol below its reactants (exothermic) "
               "with a barrier of 250 − 100 = 150 kJ/mol, while Q's products "
               "lie 60 kJ/mol above (endothermic) with a barrier of "
               "180 − 100 = 80 kJ/mol.",
    },

    # ── cells-and-batteries ─────────────────────────────────────────────
    {
        "id": "ks4-cells-and-batteries-e01",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what a simple chemical cell must contain in order to "
                "produce a voltage.",
        "options": [
            "Two identical metal electrodes dipped into pure water",
            "A single metal electrode dipped into an electrolyte",
            "Two different metal electrodes dipped into an electrolyte",
            "Two different non-metal electrodes dipped into distilled water",
        ],
        "correct_index": 2,
        "why": "The voltage comes from the difference in reactivity between "
               "two different metals, and the electrolyte lets ions carry "
               "charge between them.",
    },
    {
        "id": "ks4-cells-and-batteries-e02",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State what makes a battery different from a single cell.",
        "options": [
            "A battery is two or more cells connected in series",
            "A battery is one cell — the two words mean the same thing",
            "A battery is two or more cells in parallel, so the voltage does "
            "not change",
            "A battery contains at least three cells, one for each electrode",
        ],
        "correct_index": 0,
        "why": "A battery is two or more cells joined in series, and its "
               "voltage is the sum of the individual cell voltages.",
    },
    {
        "id": "ks4-cells-and-batteries-e03",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "In a zinc and copper cell, state which metal is the "
                "negative electrode and why.",
        "options": [
            "Copper, because it is the less reactive metal so it loses "
            "electrons",
            "Copper, because it is the heavier of the two metals",
            "Zinc, because it is the less reactive metal so it gains "
            "electrons",
            "Zinc, because it is the more reactive metal so it loses "
            "electrons",
        ],
        "correct_index": 3,
        "why": "The more reactive metal is oxidised, releasing electrons, so "
               "zinc becomes the negative electrode.",
    },
    {
        "id": "ks4-cells-and-batteries-e04",
        "subtopic_slug": "cells-and-batteries",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify an example of a rechargeable (secondary) cell.",
        "options": [
            "An alkaline AA cell used in a torch",
            "A lithium-ion cell in a mobile phone",
            "A zinc–carbon cell in a wall clock",
            "A hydrogen fuel cell in a bus",
        ],
        "correct_index": 1,
        "why": "Lithium-ion cells are secondary cells — their reactions are "
               "reversible, so an external supply can recharge them.",
    },
    {
        "id": "ks4-cells-and-batteries-s01",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Four identical 1.5 V cells are connected in series to make "
                "a battery. Calculate the voltage of the battery.",
        "options": [
            "0.4 V",
            "1.5 V",
            "3.0 V",
            "6.0 V",
        ],
        "correct_index": 3,
        "why": "Cells in series add their voltages, so 4 × 1.5 V = 6.0 V.",
    },
    {
        "id": "ks4-cells-and-batteries-s02",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "A cell made from magnesium and copper gives a larger "
                "voltage than one made from iron and copper. Explain why.",
        "options": [
            "Magnesium conducts electricity much better than iron does, so "
            "more current flows in the circuit",
            "The reactivity difference between magnesium and copper is "
            "greater than between iron and copper",
            "Magnesium is less dense than iron, so its ions move through "
            "the electrolyte faster",
            "Magnesium is less reactive than copper, so the electrons flow "
            "the other way",
        ],
        "correct_index": 1,
        "why": "The voltage depends on how far apart the two metals sit in "
               "the reactivity series, and magnesium is further from copper "
               "than iron is.",
    },
    {
        "id": "ks4-cells-and-batteries-s03",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Suggest why a non-rechargeable cell eventually stops "
                "producing a voltage.",
        "options": [
            "One of the reactants is used up, so the reaction supplying the "
            "electrons stops",
            "The electrons in the wire are all used up and cannot be replaced",
            "The two metals slowly become equally reactive, so the voltage "
            "falls to zero",
            "The electrolyte turns into a metal and stops ions from moving",
        ],
        "correct_index": 0,
        "why": "A cell holds a fixed amount of reactant, and once it has "
               "been consumed the redox reaction — and so the voltage — "
               "stops.",
    },
    {
        "id": "ks4-cells-and-batteries-s04",
        "subtopic_slug": "cells-and-batteries",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how charge is carried through the electrolyte of a "
                "chemical cell.",
        "options": [
            "Electrons flow through the electrolyte from the negative to the "
            "positive electrode",
            "Protons move through the electrolyte from the positive to the "
            "negative electrode",
            "Ions move through the electrolyte between the two electrodes",
            "The electrolyte carries no charge; it only holds the electrodes "
            "apart",
        ],
        "correct_index": 2,
        "why": "Electrons travel through the external wire, while inside the "
               "cell it is the movement of ions in the electrolyte that "
               "completes the circuit.",
    },
    {
        "id": "ks4-cells-and-batteries-h01",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why the battery in an electric car must be made "
                "from secondary cells rather than primary cells.",
        "options": [
            "Primary cells cannot produce a high enough voltage to drive a "
            "motor",
            "Primary cells cannot be recharged, so the whole battery would "
            "need replacing after every journey",
            "Primary cells contain no electrolyte, so they cannot work in a "
            "moving vehicle",
            "Primary cells slowly reverse their own reactions, so the "
            "battery would drain away while the car is parked",
        ],
        "correct_index": 1,
        "why": "A primary cell's reactions are irreversible, so once its "
               "reactants are consumed it can only be discarded — impossible "
               "for a vehicle that must be refilled with energy repeatedly.",
    },
    {
        "id": "ks4-cells-and-batteries-h02",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student builds a cell from two strips of copper dipped "
                "into copper sulfate solution and measures no voltage at "
                "all. Explain this result.",
        "options": [
            "Copper sulfate solution is not an electrolyte, so no ions are "
            "able to move between the electrodes",
            "Copper is far too unreactive to release any electrons at all",
            "The two electrodes are the same metal, so there is no "
            "reactivity difference to drive a voltage",
            "The electrodes are the wrong shape — a cell needs rods rather "
            "than strips",
        ],
        "correct_index": 2,
        "why": "A voltage arises from a difference in reactivity between the "
               "two electrodes, and two identical metals have none.",
    },
    {
        "id": "ks4-cells-and-batteries-h03",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A battery pack of six identical cells in series gives "
                "9.0 V. One cell fails and is replaced by a plain metal "
                "connector. Determine the new voltage of the pack.",
        "options": [
            "7.5 V",
            "9.0 V",
            "1.5 V",
            "54.0 V",
        ],
        "correct_index": 0,
        "why": "Each cell contributes 9.0 ÷ 6 = 1.5 V, so with five cells "
               "left the pack gives 5 × 1.5 = 7.5 V.",
    },
    {
        "id": "ks4-cells-and-batteries-h04",
        "subtopic_slug": "cells-and-batteries",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Evaluate the environmental case for using rechargeable "
                "rather than single-use cells in a household.",
        "options": [
            "Rechargeable cells contain no toxic metals, so their disposal "
            "is not a concern at all",
            "Single-use cells are better because each one is smaller and "
            "uses less metal, so less material is mined",
            "There is no difference between them, because both types are "
            "recycled in exactly the same way",
            "One rechargeable cell replaces many single-use cells, cutting "
            "waste, but it still contains toxic metals",
        ],
        "correct_index": 3,
        "why": "Reusing one cell hundreds of times greatly reduces the "
               "number discarded, but rechargeable cells still hold metals "
               "such as lithium and nickel that must be recycled.",
    },

    # ── fuel-cells ──────────────────────────────────────────────────────
    {
        "id": "ks4-fuel-cells-e01",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Identify the balanced overall equation for a hydrogen fuel "
                "cell.",
        "options": [
            "H2 + O2 → H2O2",
            "2H2O → 2H2 + O2",
            "H2 + O2 → 2H2O",
            "2H2 + O2 → 2H2O",
        ],
        "correct_index": 3,
        "why": "Two molecules of hydrogen react with one of oxygen to give "
               "two of water, balancing four hydrogen atoms and two oxygen "
               "atoms on each side.",
    },
    {
        "id": "ks4-fuel-cells-e02",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State how a fuel cell differs from a rechargeable battery "
                "in the way it is supplied with reactants.",
        "options": [
            "Both hold a fixed store of reactants, but the fuel cell's store "
            "is larger",
            "A fuel cell is supplied with fuel continuously; a battery holds "
            "a fixed store of reactants",
            "A fuel cell holds a fixed store of hydrogen; a battery is "
            "supplied continuously with electricity",
            "Neither holds reactants — both convert electrical energy "
            "directly into movement",
        ],
        "correct_index": 1,
        "why": "A fuel cell keeps working for as long as hydrogen and oxygen "
               "are fed to it, whereas a battery runs down when its stored "
               "reactants are used up.",
    },
    {
        "id": "ks4-fuel-cells-e03",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "Name the metal commonly used as the catalyst in a hydrogen "
                "fuel cell.",
        "options": [
            "Iron",
            "Nickel",
            "Platinum",
            "Vanadium",
        ],
        "correct_index": 2,
        "why": "Platinum catalyses the electrode reactions in a hydrogen "
               "fuel cell, and its rarity is a large part of why the cells "
               "are expensive.",
    },
    {
        "id": "ks4-fuel-cells-e04",
        "subtopic_slug": "fuel-cells",
        "band": "easier",
        "tier": "foundation",
        "triple_only": True,
        "text": "State one practical advantage of a hydrogen fuel cell "
                "vehicle over a battery electric vehicle.",
        "options": [
            "It can be refuelled in a few minutes rather than recharged over "
            "hours",
            "It produces no water, so nothing has to be drained from the "
            "vehicle",
            "It needs no oxygen from the air, so it can run in a sealed "
            "garage",
            "It contains no catalyst, which makes it cheaper to build",
        ],
        "correct_index": 0,
        "why": "Filling a hydrogen tank takes about as long as filling a "
               "petrol tank, while charging a large battery takes far "
               "longer.",
    },
    {
        "id": "ks4-fuel-cells-s01",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain what happens to hydrogen at the negative electrode "
                "of a hydrogen fuel cell.",
        "options": [
            "It is reduced — it gains electrons and forms hydride ions",
            "It is reduced — it gains electrons and forms water directly",
            "It is oxidised — it loses electrons, which flow round the "
            "external circuit",
            "It is oxidised — it gains electrons, which are stored in the "
            "electrode",
        ],
        "correct_index": 2,
        "why": "Hydrogen loses electrons at the negative electrode, and that "
               "flow of electrons through the external circuit is what "
               "delivers the electrical energy.",
    },
    {
        "id": "ks4-fuel-cells-s02",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe how 'green' hydrogen is made, and state why it is "
                "not yet widely used.",
        "options": [
            "By electrolysis of water using renewable electricity; it costs "
            "more than reforming natural gas",
            "By burning natural gas in a limited supply of air; it produces "
            "too much soot to be practical",
            "By reacting platinum with steam; platinum is far too rare for "
            "the process to be scaled up",
            "By condensing it out of the air; the concentration in air is "
            "too low to be worth extracting",
        ],
        "correct_index": 0,
        "why": "Splitting water with renewable electricity releases no "
               "carbon dioxide, but the electricity makes it dearer than the "
               "steam-reforming route.",
    },
    {
        "id": "ks4-fuel-cells-s03",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Explain why a fuel cell transfers a greater proportion of "
                "its fuel's chemical energy usefully than a petrol engine "
                "does.",
        "options": [
            "It burns the hydrogen at a much higher temperature than "
            "petrol, so far less energy escapes as heat",
            "It converts chemical energy directly to electrical energy, "
            "with no hot moving parts wasting energy",
            "Hydrogen stores more energy per litre than petrol does, so "
            "less fuel is needed",
            "It recycles the water it makes back into hydrogen and oxygen "
            "inside the cell",
        ],
        "correct_index": 1,
        "why": "There is no combustion and no engine to drive, so energy is "
               "not lost as heat and friction in moving parts.",
    },
    {
        "id": "ks4-fuel-cells-s04",
        "subtopic_slug": "fuel-cells",
        "band": "standard",
        "tier": "foundation",
        "triple_only": True,
        "text": "Describe two problems with storing hydrogen on board a "
                "vehicle.",
        "options": [
            "It must be kept warm, and it corrodes steel tanks within days",
            "It is very dense, so the tanks are heavy, and it is toxic to "
            "breathe",
            "It must be kept in complete darkness, because it decomposes "
            "into its atoms in sunlight",
            "It must be stored under high pressure or as a liquid, and it "
            "is highly flammable",
        ],
        "correct_index": 3,
        "why": "Hydrogen is a low-density gas, so it must be compressed or "
               "liquefied to fit a useful amount into a tank, and it burns "
               "very readily if it leaks.",
    },
    {
        "id": "ks4-fuel-cells-h01",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Compare a hydrogen fuel cell with a lithium-ion battery for "
                "powering a long-distance lorry, and justify a choice.",
        "options": [
            "The battery, because it can be fully recharged in minutes at "
            "any depot",
            "The battery, because hydrogen simply cannot supply enough "
            "power to move a vehicle as heavy as a lorry",
            "The fuel cell, because it emits no water and so needs no "
            "exhaust system",
            "The fuel cell, because hydrogen's high energy per kilogram "
            "gives long range with quick refuelling",
        ],
        "correct_index": 3,
        "why": "For a heavy vehicle covering long distances the mass of "
               "battery needed becomes prohibitive, while a hydrogen tank "
               "stores far more energy per kilogram and refills quickly.",
    },
    {
        "id": "ks4-fuel-cells-h02",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A city council considers replacing its diesel buses with "
                "fuel cell buses. Evaluate the main practical obstacle.",
        "options": [
            "There are very few hydrogen refuelling stations, so new "
            "infrastructure must be built",
            "Fuel cell buses cannot run in cold weather because the water "
            "produced freezes inside the cell",
            "Fuel cells cannot be built large enough to supply the power a "
            "bus needs",
            "Fuel cells emit water vapour, which is a pollutant that has to "
            "be captured and stored",
        ],
        "correct_index": 0,
        "why": "The cells themselves work well, but a fleet is useless "
               "without somewhere to refuel, and hydrogen stations are rare "
               "and costly to build.",
    },
    {
        "id": "ks4-fuel-cells-h03",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "A student writes: 'A hydrogen fuel cell is just a battery "
                "that runs on hydrogen, so when the hydrogen inside is used "
                "up the cell is finished and must be thrown away.' Identify "
                "the error.",
        "options": [
            "The cell is finished, but it can be discarded safely because it "
            "contains only water",
            "The hydrogen is supplied from outside, so refilling the supply "
            "keeps the same cell working",
            "The cell uses no hydrogen at all — oxygen from the air is the "
            "fuel it consumes",
            "The cell is rechargeable, so passing electricity through it "
            "turns the water back into hydrogen",
        ],
        "correct_index": 1,
        "why": "A fuel cell stores no fuel of its own — hydrogen is fed in "
               "continuously, so the cell itself is not consumed.",
    },
    {
        "id": "ks4-fuel-cells-h04",
        "subtopic_slug": "fuel-cells",
        "band": "harder",
        "tier": "foundation",
        "triple_only": True,
        "text": "Fuel cells were used on the Apollo spacecraft. Suggest why "
                "they suited that application particularly well.",
        "options": [
            "They work without any oxygen supply, which cannot be carried "
            "into space",
            "They generate their own hydrogen from sunlight, so no fuel at "
            "all had to be launched from Earth",
            "They supply electricity continuously and the water produced "
            "can be drunk by the crew",
            "They become more efficient in zero gravity because the "
            "electrodes do not sag",
        ],
        "correct_index": 2,
        "why": "The only product is pure water, so a mission gets both its "
               "electricity and its drinking water from the same device.",
    },

    # ── bond-energy-calculations ────────────────────────────────────────
    {
        "id": "ks4-bond-energy-calculations-e01",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the energy change involved in breaking a chemical "
                "bond.",
        "options": [
            "Energy is released; bond breaking is exothermic",
            "No energy is transferred; the atoms simply move apart",
            "Energy must be supplied; bond breaking is endothermic",
            "Energy must be supplied; bond breaking is exothermic",
        ],
        "correct_index": 2,
        "why": "The atoms in a bond attract each other, so energy has to be "
               "put in to pull them apart, making bond breaking endothermic.",
    },
    {
        "id": "ks4-bond-energy-calculations-e02",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "State the expression used to find the overall energy change "
                "of a reaction from bond energies.",
        "options": [
            "ΔH = energy to break bonds − energy released making bonds",
            "ΔH = energy released making bonds − energy to break bonds",
            "ΔH = energy to break bonds + energy released making bonds",
            "ΔH = energy to break bonds ÷ energy released making bonds",
        ],
        "correct_index": 0,
        "why": "Energy in comes first and energy out is subtracted, which is "
               "why an exothermic reaction — more out than in — gives a "
               "negative ΔH.",
    },
    {
        "id": "ks4-bond-energy-calculations-e03",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "The bond energy of H-H is 436 kJ/mol. Calculate the energy "
                "needed to break the bonds in 3 mol of hydrogen molecules.",
        "options": [
            "436 kJ",
            "1308 kJ",
            "145 kJ",
            "872 kJ",
        ],
        "correct_index": 1,
        "why": "Each mole of H2 contains one mole of H-H bonds, so "
               "3 × 436 = 1308 kJ is needed.",
    },
    {
        "id": "ks4-bond-energy-calculations-e04",
        "subtopic_slug": "bond-energy-calculations",
        "band": "easier",
        "tier": "higher",
        "triple_only": False,
        "text": "A reaction takes in 1450 kJ/mol to break bonds and releases "
                "1450 kJ/mol when new bonds form. State ΔH and classify the "
                "reaction.",
        "options": [
            "ΔH = −1450 kJ/mol, so the reaction is exothermic",
            "ΔH = +2900 kJ/mol, so the reaction is endothermic",
            "ΔH = +1450 kJ/mol, so the reaction is endothermic",
            "ΔH = 0 kJ/mol, so the reaction is neither",
        ],
        "correct_index": 3,
        "why": "ΔH = 1450 − 1450 = 0, so exactly as much energy is released "
               "making bonds as was needed to break them.",
    },
    {
        "id": "ks4-bond-energy-calculations-s01",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for H2 + Br2 → 2HBr. Bond energies in kJ/mol: "
                "H-H 436, Br-Br 193, H-Br 366.",
        "options": [
            "−103 kJ/mol",
            "+103 kJ/mol",
            "+263 kJ/mol",
            "+1361 kJ/mol",
        ],
        "correct_index": 0,
        "why": "Energy in is 436 + 193 = 629 kJ/mol and energy out is "
               "2 × 366 = 732 kJ/mol, so ΔH = 629 − 732 = −103 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-s02",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For N2 + 3H2 → 2NH3, determine the total energy needed to "
                "break all the bonds in the reactants. Bond energies in "
                "kJ/mol: N≡N 945, H-H 436.",
        "options": [
            "1381 kJ/mol",
            "3271 kJ/mol",
            "2253 kJ/mol",
            "4143 kJ/mol",
        ],
        "correct_index": 2,
        "why": "One N≡N bond and three H-H bonds must break: "
               "945 + (3 × 436) = 2253 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-s03",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "For N2 + 3H2 → 2NH3, calculate the total energy released "
                "when the bonds in the products form. The N-H bond energy is "
                "391 kJ/mol.",
        "options": [
            "782 kJ/mol",
            "1173 kJ/mol",
            "1564 kJ/mol",
            "2346 kJ/mol",
        ],
        "correct_index": 3,
        "why": "Each NH3 molecule contains three N-H bonds and two molecules "
               "are formed, so 6 × 391 = 2346 kJ/mol is released.",
    },
    {
        "id": "ks4-bond-energy-calculations-s04",
        "subtopic_slug": "bond-energy-calculations",
        "band": "standard",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for 2H2 + O2 → 2H2O. Bond energies in kJ/mol: "
                "H-H 436, O=O 498, O-H 464.",
        "options": [
            "−922 kJ/mol",
            "−486 kJ/mol",
            "+442 kJ/mol",
            "+3226 kJ/mol",
        ],
        "correct_index": 1,
        "why": "Breaking two H-H and one O=O takes (2 × 436) + 498 = "
               "1370 kJ/mol, while forming four O-H bonds releases "
               "4 × 464 = 1856 kJ/mol, so ΔH = 1370 − 1856 = −486 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-h01",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for the complete combustion of ethene, "
                "C2H4 + 3O2 → 2CO2 + 2H2O. Bond energies in kJ/mol: C=C 614, "
                "C-H 413, O=O 498, C=O 805, O-H 464.",
        "options": [
            "−2312 kJ/mol",
            "−1316 kJ/mol",
            "+294 kJ/mol",
            "+1316 kJ/mol",
        ],
        "correct_index": 1,
        "why": "Breaking one C=C, four C-H and three O=O takes "
               "614 + 1652 + 1494 = 3760 kJ/mol; forming four C=O and four "
               "O-H releases 3220 + 1856 = 5076 kJ/mol, so ΔH = −1316 "
               "kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-h02",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "Calculate ΔH for CH4 + Cl2 → CH3Cl + HCl. Only one C-H bond "
                "is broken. Bond energies in kJ/mol: C-H 413, Cl-Cl 243, "
                "C-Cl 338, H-Cl 432.",
        "options": [
            "+114 kJ/mol",
            "+1125 kJ/mol",
            "−1426 kJ/mol",
            "−114 kJ/mol",
        ],
        "correct_index": 3,
        "why": "Only one C-H and the Cl-Cl bond break (413 + 243 = "
               "656 kJ/mol) and only the C-Cl and H-Cl bonds form "
               "(338 + 432 = 770 kJ/mol), so ΔH = 656 − 770 = −114 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-h03",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A reaction has ΔH = +52 kJ/mol, and the total energy "
                "released when the bonds in the products form is "
                "1240 kJ/mol. Determine the total energy needed to break the "
                "bonds in the reactants.",
        "options": [
            "1292 kJ/mol",
            "1188 kJ/mol",
            "1240 kJ/mol",
            "52 kJ/mol",
        ],
        "correct_index": 0,
        "why": "ΔH = energy in − energy out, so energy in = ΔH + energy out "
               "= 52 + 1240 = 1292 kJ/mol.",
    },
    {
        "id": "ks4-bond-energy-calculations-h04",
        "subtopic_slug": "bond-energy-calculations",
        "band": "harder",
        "tier": "higher",
        "triple_only": False,
        "text": "A student calculates ΔH for 2H2 + O2 → 2H2O as "
                "+486 kJ/mol and concludes the reaction is endothermic. "
                "Their arithmetic is correct but the answer is wrong. "
                "Identify the mistake.",
        "options": [
            "They used the O-O bond energy instead of O=O when breaking the "
            "oxygen molecule",
            "They forgot that two moles of water form, so they halved the "
            "energy released",
            "They subtracted the energy in from the energy out, rather than "
            "the energy out from the energy in",
            "They added the two totals together, because both bond breaking "
            "and bond making release energy to the surroundings",
        ],
        "correct_index": 2,
        "why": "ΔH is energy in (breaking) − energy out (forming), and "
               "reversing that subtraction flips the sign, turning an "
               "exothermic reaction into an apparently endothermic one.",
    },
]
