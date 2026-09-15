"""Physics · Energy — the MRB-338 expansion of `energy-changes-in-systems`.

One leaf only: AQA 8463 6.1.1.3, specific heat capacity. The original twelve
rows in `energy.py` state the definition once, substitute into
E = m x c x temperature change three times, rearrange it for the temperature
change and for c, diagnose the final-temperature-instead-of-the-change error,
compare water with copper at equal mass, add a pan to its water, time a kettle
and suggest why a measured value comes out too high. This file takes what they
leave: the unit and the shape of the equation, rearrangement for the MASS, the
cooling direction (energy released rather than supplied), the gram and litre
conversions, the consequences of water's unusually high value in five real
contexts, and RP14 as a method - the measurements, the order, the variables,
the lagging, the reading still climbing after the heater goes off, and what a
deliberately-accounted-for leak does to the arithmetic.

The weight follows the CONTENT. `easier` stays at eight because recall here is
one definition, one unit, one equation and one meaning of "temperature change",
and asking any of them a second way is the same question wearing a new stem.
The demand in this subtopic lives in the substituting and the rearranging, which
is why the twenty-two-row bands carry the conversions, the two-substance
comparisons, the multi-step work from a heater's power and time, and the
evaluations.

Substances are spread deliberately - water, copper, aluminium, iron, lead,
concrete, cooking oil, ethanol, clay, sauna stone - and every c value a row
needs is stated in that row's own stem, so no stem depends on a table, a
diagram or a remembered list. Nothing here touches Ek, Ep, power, efficiency,
dissipation or the comparison of insulating materials; those are other leaves'
questions and would be those leaves' questions wearing this leaf's slug.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05-e12 ═════════════════════════════════════════════════
    # The unit, the shape of the equation, the meaning of a stated c value,
    # the meaning of "temperature change", the RP14 measurement list, one
    # application, and two one-step substitutions.
    {
        "id": "ks4-energy-changes-in-systems-e05",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the unit of specific heat capacity.",
        "options": [
            "J/degrees C",
            "J/kg degrees C",
            "J",
            "J/kg",
        ],
        "correct_index": 1,
        "why": "Specific heat capacity is an energy for each kilogram and for "
               "each degree of temperature change, so its unit carries both a "
               "mass and a temperature.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e06",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the equation that links the energy transferred to a "
                "substance, its mass, its specific heat capacity and its "
                "temperature change.",
        "options": [
            "energy = specific heat capacity x temperature change / mass",
            "energy = mass x temperature change / specific heat capacity",
            "energy = mass x specific heat capacity x temperature change",
            "energy = mass x specific heat capacity / temperature change",
        ],
        "correct_index": 2,
        "why": "Doubling the mass, the specific heat capacity or the "
               "temperature change each doubles the energy needed, so all "
               "three are multiplied together.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e07",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg copper bar is warmed by 10 degrees C. Calculate the "
                "energy transferred to the bar. (c = 385 J/kg degrees C)",
        "options": [
            "3850 J",
            "770 J",
            "77 000 J",
            "7700 J",
        ],
        "correct_index": 3,
        "why": "E = m x c x temperature change = 2.0 x 385 x 10 = 7700 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e08",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the energy needed to warm 0.50 kg of water through "
                "5.0 degrees C. (c = 4200 J/kg degrees C)",
        "options": [
            "10 500 J",
            "2100 J",
            "21 000 J",
            "1050 J",
        ],
        "correct_index": 0,
        "why": "E = m x c x temperature change = 0.50 x 4200 x 5.0 = 10 500 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e09",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The specific heat capacity of iron is 450 J/kg degrees C. "
                "State what that value tells you about iron.",
        "options": [
            "450 J raises the temperature of 1 kg of iron by 1 degree C",
            "450 J raises the temperature of 1 g of iron by 1 degree C",
            "450 J is needed to melt 1 kg of iron once it has reached its "
            "melting point",
            "1 kg of iron holds a total of 450 J in its thermal store once it "
            "has been warmed",
        ],
        "correct_index": 0,
        "why": "Specific heat capacity is the energy needed for each kilogram "
               "for each degree of rise, so 450 J/kg degrees C means 450 J for "
               "every kilogram and every degree.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e10",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the temperature change means when the energy "
                "needed to heat a substance is being worked out.",
        "options": [
            "The final temperature the substance reaches once the heating has "
            "been stopped",
            "The final temperature minus the starting temperature",
            "The starting temperature of the substance before it is heated",
            "The two temperatures added together and then halved",
        ],
        "correct_index": 1,
        "why": "The temperature change is a difference, so water taken from "
               "20 degrees C to 60 degrees C has a change of 40 degrees C and "
               "not 60 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e11",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the three measurements needed to determine the specific "
                "heat capacity of a metal block that is warmed by an electric "
                "heater.",
        "options": [
            "The volume of the block, the energy supplied and the final "
            "temperature",
            "The mass of the block, the energy supplied and the temperature "
            "change",
            "The mass of the block, its volume and the time for which the "
            "heater is switched on",
            "The temperature of the room, the mass of the block and the "
            "current in the heater circuit",
        ],
        "correct_index": 1,
        "why": "Rearranging gives c = energy / (mass x temperature change), so "
               "those three quantities are exactly what has to be measured.",
    },
    {
        "id": "ks4-energy-changes-in-systems-e12",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State why a hot-water bottle is filled with water rather than "
                "with the same mass of dry sand.",
        "options": [
            "Water has a much higher melting point than dry sand, so the "
            "bottle stays warm in the bed for far longer",
            "Water is a liquid, so it holds no energy in its thermal store "
            "until it has been poured out",
            "Water has a higher specific heat capacity, so it stores more "
            "energy for each degree it cools",
            "Water has a lower specific heat capacity than sand, so its "
            "temperature falls much more slowly",
        ],
        "correct_index": 2,
        "why": "Water's specific heat capacity of 4200 J/kg degrees C is over "
               "five times that of sand, so each kilogram carries far more "
               "energy for each degree it cools through.",
    },

    # ══ standard · s05-s26 ═══════════════════════════════════════════════
    # Familiar contexts with a conversion or a rearrangement, the cooling
    # direction, the applications of water's high value, and RP14 as a method.
    {
        "id": "ks4-energy-changes-in-systems-s05",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beaker holds 500 g of water. Calculate the energy that must "
                "be supplied to raise its temperature by 30 degrees C. "
                "(c = 4200 J/kg degrees C)",
        "options": [
            "126 000 J",
            "6300 J",
            "63 000 J",
            "63 000 000 J",
        ],
        "correct_index": 2,
        "why": "Convert the mass first: 500 g = 0.50 kg, so E = 0.50 x 4200 x "
               "30 = 63 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s06",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A blacksmith's horseshoe of mass 0.80 kg cools from "
                "520 degrees C to 20 degrees C. Calculate the energy it "
                "releases. (c for iron = 450 J/kg degrees C)",
        "options": [
            "187 200 J",
            "180 000 J",
            "7200 J",
            "225 000 J",
        ],
        "correct_index": 1,
        "why": "The temperature change is 520 - 20 = 500 degrees C, so "
               "E = 0.80 x 450 x 500 = 180 000 J released.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s07",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "81 000 J is transferred to a 2.0 kg aluminium bar. Calculate "
                "the rise in its temperature. (c = 900 J/kg degrees C)",
        "options": [
            "22.5 degrees C",
            "4.5 degrees C",
            "90 degrees C",
            "45 degrees C",
        ],
        "correct_index": 3,
        "why": "Rearranged, temperature change = E / (m x c) = 81 000 / "
               "(2.0 x 900) = 81 000 / 1800 = 45 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s08",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg pane of glass in a greenhouse absorbs 26 800 J of "
                "energy from the Sun, and its temperature rises by "
                "20 degrees C. Determine the specific heat capacity of the "
                "glass.",
        "options": [
            "13 400 J/kg degrees C",
            "1 072 000 J/kg degrees C",
            "670 J/kg degrees C",
            "1340 J/kg degrees C",
        ],
        "correct_index": 2,
        "why": "Rearranged, c = E / (m x temperature change) = 26 800 / "
               "(2.0 x 20) = 26 800 / 40 = 670 J/kg degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s09",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "735 000 J warms a sample of water by 25 degrees C. Calculate "
                "the mass of the sample. (c = 4200 J/kg degrees C)",
        "options": [
            "7.0 kg",
            "175 kg",
            "0.14 kg",
            "70 kg",
        ],
        "correct_index": 0,
        "why": "Rearranged, m = E / (c x temperature change) = 735 000 / "
               "(4200 x 25) = 735 000 / 105 000 = 7.0 kg.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s10",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Fruit growers often plant an orchard beside a large lake "
                "because the trees suffer less frost damage on cold nights. "
                "Explain this using the specific heat capacity of water.",
        "options": [
            "The lake's water has a high specific heat capacity, so it gives "
            "out a lot of energy to the air above it while its own "
            "temperature falls only slightly",
            "The lake's water has a low specific heat capacity, so its "
            "temperature drops sharply after dark and it pulls the colder air "
            "away from the rows of trees",
            "Water freezes solid as soon as the air falls below 0 degrees C, "
            "and the sheet of ice that then forms holds the orchard's warmth "
            "in for the night",
            "The lake has a very large mass, so through the night it takes in "
            "energy from the trees themselves, and losing that energy is what "
            "stops the fruit freezing",
        ],
        "correct_index": 0,
        "why": "Water's high specific heat capacity means each kilogram "
               "releases a great deal of energy for a small fall in "
               "temperature, so the lake keeps the air beside it warmer "
               "through the night than open ground would.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s11",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater is warmed overnight and releases energy "
                "through the next day. Explain why the blocks inside it are "
                "made of a material with a high specific heat capacity.",
        "options": [
            "A high specific heat capacity lets the blocks reach a far higher "
            "temperature than the heater's element does",
            "A high specific heat capacity means each kilogram stores more "
            "energy for every degree it is heated",
            "A high specific heat capacity stops energy escaping from the "
            "blocks until the heater is switched on again",
            "A high specific heat capacity means the blocks need very little "
            "energy overnight, which is what makes the heater cheap to run",
        ],
        "correct_index": 1,
        "why": "Energy stored is m x c x temperature change, so a large c puts "
               "more joules into the same mass for the same rise, ready to be "
               "released as the blocks cool.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s12",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "On a sunny spring day the sand on a beach becomes hot while "
                "the sea stays cold. Explain this in terms of specific heat "
                "capacity.",
        "options": [
            "Sunlight reaches the sand first, so the sea receives almost no "
            "energy from the Sun during the day",
            "The sea has a much larger specific heat capacity, so the same "
            "energy per kilogram gives a smaller rise",
            "The sea has a much smaller specific heat capacity, so it needs "
            "far more energy for every degree of temperature rise",
            "Sea water is salty, so its specific heat capacity falls to almost "
            "nothing once the salt has dissolved",
        ],
        "correct_index": 1,
        "why": "Temperature change = E / (m x c), so for the same energy on "
               "the same mass the substance with the larger c warms by less.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s13",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Give the correct order of steps for determining the specific "
                "heat capacity of a metal block with an electric heater.",
        "options": [
            "Record the starting temperature, switch on the heater, find the "
            "mass of the block, then record the energy supplied",
            "Switch on the heater, find the mass of the block, record the "
            "final temperature, then record the starting temperature",
            "Find the mass of the block, record its starting temperature, "
            "switch on the heater and record the energy supplied, then record "
            "the final temperature",
            "Find the mass of the block, switch on the heater, record the "
            "final temperature, then calculate the energy from the mass alone",
        ],
        "correct_index": 2,
        "why": "The mass and the starting temperature must both be known "
               "before any energy is supplied, and the final temperature can "
               "be read afterwards.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s14",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A metal block is warmed by an electric heater and readings "
                "are taken as the energy supplied builds up. Identify the "
                "independent and dependent variables.",
        "options": [
            "Independent: the mass of the block. Dependent: its specific heat "
            "capacity",
            "Independent: the temperature of the block. Dependent: the energy "
            "the heater has to supply to it",
            "Independent: the energy supplied. Dependent: the temperature of "
            "the block",
            "Independent: the specific heat capacity of the metal. Dependent: "
            "the mass of the block",
        ],
        "correct_index": 2,
        "why": "The experimenter chooses how much energy to supply and then "
               "reads the temperature that results, so the energy is "
               "independent and the temperature dependent.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s15",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a metal block is wrapped in lagging before its "
                "specific heat capacity is determined.",
        "options": [
            "The lagging holds the block still, which keeps the thermometer "
            "pressed against the hot metal",
            "The lagging adds mass to the block, so the temperature rise "
            "measured is larger and easier to read",
            "The lagging warms the block on its own, so less energy has to be "
            "supplied by the electric heater",
            "The lagging reduces the energy escaping to the surroundings, so "
            "more of the energy supplied reaches the block",
        ],
        "correct_index": 3,
        "why": "The calculation assumes every joule supplied went into the "
               "block, so cutting the leak to the surroundings brings the "
               "measured value closer to the true one.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s16",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student works out the energy needed to warm 300 g of water "
                "by 10 degrees C and writes down 12 600 000 J. Identify the "
                "mistake. (c = 4200 J/kg degrees C)",
        "options": [
            "The temperature change was doubled, because a rise and a fall "
            "were added together",
            "The mass was left in grams instead of being converted into "
            "kilograms",
            "The specific heat capacity of water was used when the value for "
            "ice was needed",
            "The energy was multiplied by the temperature change when it "
            "should have been divided by it",
        ],
        "correct_index": 1,
        "why": "The equation needs kilograms: 300 g = 0.30 kg gives "
               "0.30 x 4200 x 10 = 12 600 J, a thousand times smaller than "
               "the student's answer.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s17",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Warming 1.0 kg of water by 5.0 degrees C needs 21 000 J. "
                "Determine the energy needed to warm 4.0 kg of water by "
                "5.0 degrees C.",
        "options": [
            "5250 J",
            "336 000 J",
            "84 000 J",
            "21 000 J",
        ],
        "correct_index": 2,
        "why": "Energy is proportional to mass when c and the temperature "
               "change are fixed, so four times the mass needs 4 x 21 000 = "
               "84 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s18",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "1.0 kg of water and 1.0 kg of concrete are each given "
                "16 800 J. Calculate the temperature rise of each. "
                "(c = 4200 J/kg degrees C for water, 800 J/kg degrees C for "
                "concrete)",
        "options": [
            "Water 21 degrees C and concrete 4.0 degrees C",
            "Water 8.0 degrees C and concrete 42 degrees C",
            "Water 4.0 degrees C and concrete 4.0 degrees C",
            "Water 4.0 degrees C and concrete 21 degrees C",
        ],
        "correct_index": 3,
        "why": "Temperature change = E / (m x c): the water rises 16 800 / "
               "4200 = 4.0 degrees C and the concrete 16 800 / 800 = "
               "21 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s19",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 400 g lead fishing weight is warmed by 50 degrees C. "
                "Calculate the energy transferred to it. "
                "(c = 130 J/kg degrees C)",
        "options": [
            "2 600 000 J",
            "6500 J",
            "2600 J",
            "260 J",
        ],
        "correct_index": 2,
        "why": "400 g = 0.40 kg, so E = 0.40 x 130 x 50 = 2600 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s20",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A shower warms 12 kg of water from 15 degrees C to "
                "40 degrees C. Calculate the energy the water gains. "
                "(c = 4200 J/kg degrees C)",
        "options": [
            "2 016 000 J",
            "1 260 000 J",
            "105 000 J",
            "126 000 J",
        ],
        "correct_index": 1,
        "why": "The temperature change is 40 - 15 = 25 degrees C, so "
               "E = 12 x 4200 x 25 = 1 260 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s21",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sauna heater holds 25 kg of stones and warms them from "
                "20 degrees C to 120 degrees C. Calculate the energy the "
                "stones gain. (c for the stone = 800 J/kg degrees C)",
        "options": [
            "2 000 000 J",
            "2 400 000 J",
            "80 000 J",
            "200 000 J",
        ],
        "correct_index": 0,
        "why": "The temperature change is 120 - 20 = 100 degrees C, so "
               "E = 25 x 800 x 100 = 2 000 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s22",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.60 kg copper pipe cools from 90 degrees C to "
                "20 degrees C. Calculate the energy it releases. "
                "(c = 385 J/kg degrees C)",
        "options": [
            "4620 J",
            "26 950 J",
            "20 790 J",
            "16 170 J",
        ],
        "correct_index": 3,
        "why": "The temperature change is 90 - 20 = 70 degrees C, so "
               "E = 0.60 x 385 x 70 = 16 170 J released.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s23",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "One litre of water has a mass of 1.0 kg. Determine the energy "
                "needed to heat 1.5 litres of water in a jug through "
                "25 degrees C. (c = 4200 J/kg degrees C)",
        "options": [
            "157 500 J",
            "105 000 J",
            "15 750 J",
            "157 500 000 J",
        ],
        "correct_index": 0,
        "why": "1.5 litres of water has a mass of 1.5 kg, so E = 1.5 x 4200 x "
               "25 = 157 500 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s24",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 5.0 kg concrete slab in the sunshine warms from "
                "12 degrees C to 32 degrees C. Calculate the energy it "
                "absorbs. (c = 800 J/kg degrees C)",
        "options": [
            "128 000 J",
            "16 000 J",
            "8000 J",
            "80 000 J",
        ],
        "correct_index": 3,
        "why": "The temperature change is 32 - 12 = 20 degrees C, so "
               "E = 5.0 x 800 x 20 = 80 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s25",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot-water bottle holding 0.25 kg of water cools overnight "
                "from 70 degrees C to 30 degrees C. Calculate the energy it "
                "releases. (c = 4200 J/kg degrees C)",
        "options": [
            "73 500 J",
            "42 000 J",
            "31 500 J",
            "168 000 J",
        ],
        "correct_index": 1,
        "why": "The temperature change is 70 - 30 = 40 degrees C, so "
               "E = 0.25 x 4200 x 40 = 42 000 J released.",
    },
    {
        "id": "ks4-energy-changes-in-systems-s26",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An immersion heater warms a metal block. State the two "
                "quantities that have to be measured to find the energy the "
                "heater supplies.",
        "options": [
            "The mass of the block and the temperature it reaches at the end "
            "of the heating",
            "The power of the heater and the time for which it is switched on",
            "The temperature of the room and the mass of the metal block being "
            "warmed",
            "The volume of the block and the temperature rise produced by the "
            "heater in it",
        ],
        "correct_index": 1,
        "why": "Energy supplied is the power multiplied by the time, which is "
               "then used as the energy in E = m x c x temperature change.",
    },

    # ══ harder · h05-h26 ═════════════════════════════════════════════════
    # Unfamiliar contexts, multi-step work from a heater's power and time,
    # rearrangement for the mass, two-substance comparisons, and the
    # evaluations RP14 asks for.
    {
        "id": "ks4-energy-changes-in-systems-h05",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 210 W immersion heater is switched on for 140 s in 0.20 kg "
                "of water. Calculate the temperature rise, assuming all the "
                "energy reaches the water. (c = 4200 J/kg degrees C)",
        "options": [
            "7.0 degrees C",
            "3.5 degrees C",
            "35 degrees C",
            "0.25 degrees C",
        ],
        "correct_index": 2,
        "why": "The heater supplies 210 x 140 = 29 400 J, so the temperature "
               "change is 29 400 / (0.20 x 4200) = 29 400 / 840 = "
               "35 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h06",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 30 W heater runs for 400 s in 0.50 kg of ethanol, whose "
                "temperature rises by 10 degrees C. Calculate the specific "
                "heat capacity of ethanol.",
        "options": [
            "1200 J/kg degrees C",
            "60 000 J/kg degrees C",
            "24 000 J/kg degrees C",
            "2400 J/kg degrees C",
        ],
        "correct_index": 3,
        "why": "The heater supplies 30 x 400 = 12 000 J, so c = 12 000 / "
               "(0.50 x 10) = 12 000 / 5.0 = 2400 J/kg degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h07",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Equal masses of water and cooking oil are each warmed by "
                "20 degrees C. Determine which needs more energy, and by what "
                "factor. (c = 4200 J/kg degrees C for water, "
                "2000 J/kg degrees C for oil)",
        "options": [
            "The oil, by a factor of 2.1",
            "The water, by a factor of 2.1",
            "The water, by a factor of 4.2",
            "The water, by a factor of 2200",
        ],
        "correct_index": 1,
        "why": "With the mass and the temperature change equal, the energy is "
               "proportional to c, and 4200 / 2000 = 2.1.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h08",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student repeats a determination of the specific heat "
                "capacity of a metal block, this time with the block lagged "
                "and a lid over the apparatus. Evaluate the effect on the "
                "value obtained.",
        "options": [
            "The value obtained falls and moves closer to the true value, "
            "because less of the energy supplied escapes",
            "The value obtained rises above the true value, because the "
            "lagging supplies extra energy of its own to the block",
            "The value obtained is unchanged, because the lagging keeps the "
            "warmth of the room away from the thermometer",
            "The value obtained falls well below the true value, because the "
            "lid stops the block from ever reaching its final temperature",
        ],
        "correct_index": 0,
        "why": "An unlagged block loses energy to the surroundings, so the "
               "energy supplied overstates the energy gained and c comes out "
               "too high; cutting the loss reduces that overstatement.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h09",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student obtains 1080 J/kg degrees C for a metal whose true "
                "specific heat capacity is 900 J/kg degrees C. Calculate the "
                "percentage by which the value is too high.",
        "options": [
            "17%",
            "83%",
            "1.2%",
            "20%",
        ],
        "correct_index": 3,
        "why": "The difference is 1080 - 900 = 180 J/kg degrees C, and 180 / "
               "900 = 0.20, which is 20 per cent of the true value.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h10",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hot aluminium block is dropped into 1.0 kg of water in an "
                "insulated container. The water warms by 12 degrees C as the "
                "block cools by 80 degrees C. Calculate the mass of the block. "
                "(c = 4200 J/kg degrees C for water, 900 J/kg degrees C for "
                "aluminium)",
        "options": [
            "0.15 kg",
            "4.7 kg",
            "0.70 kg",
            "1.4 kg",
        ],
        "correct_index": 2,
        "why": "The water gains 1.0 x 4200 x 12 = 50 400 J, so the block's "
               "mass is 50 400 / (900 x 80) = 50 400 / 72 000 = 0.70 kg.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h11",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A swimming pool contains 50 000 kg of water, warmed from "
                "18 degrees C to 26 degrees C. Calculate the energy needed. "
                "(c = 4200 J/kg degrees C)",
        "options": [
            "5 460 000 000 J",
            "210 000 000 J",
            "1 680 000 000 J",
            "168 000 000 J",
        ],
        "correct_index": 2,
        "why": "The temperature change is 26 - 18 = 8 degrees C, so "
               "E = 50 000 x 4200 x 8 = 1 680 000 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h12",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A deep-fat fryer is made of 0.50 kg of steel and holds "
                "0.80 kg of oil, both at 20 degrees C. Determine the energy "
                "needed to bring the whole fryer to 120 degrees C. "
                "(c = 450 J/kg degrees C for steel, 2000 J/kg degrees C for "
                "oil)",
        "options": [
            "160 000 J",
            "182 500 J",
            "22 500 J",
            "245 000 J",
        ],
        "correct_index": 1,
        "why": "Both rise by 100 degrees C: the steel needs 0.50 x 450 x 100 = "
               "22 500 J and the oil 0.80 x 2000 x 100 = 160 000 J, giving "
               "182 500 J in total.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h13",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.20 kg iron rivet at 800 degrees C is quenched in water "
                "and ends at 20 degrees C. Calculate the energy the rivet "
                "transfers away. (c = 450 J/kg degrees C)",
        "options": [
            "70 200 J",
            "1800 J",
            "351 000 J",
            "72 000 J",
        ],
        "correct_index": 0,
        "why": "The temperature change is 800 - 20 = 780 degrees C, so "
               "E = 0.20 x 450 x 780 = 70 200 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h14",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A determination of specific heat capacity is repeated with a "
                "block of the same metal but twice the mass, using the same "
                "heater for the same time. Predict the effect on the "
                "temperature rise and on the value calculated for c.",
        "options": [
            "The temperature rise halves and the value calculated for c is "
            "unchanged",
            "The temperature rise halves and the value calculated for c halves "
            "with it",
            "The temperature rise is unchanged and the value calculated for c "
            "doubles",
            "The temperature rise doubles and the value calculated for c is "
            "halved by the extra mass",
        ],
        "correct_index": 0,
        "why": "Doubling m halves the temperature change for the same energy, "
               "and c = E / (m x temperature change) is a property of the "
               "metal, so the two changes cancel.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h15",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why a car cooling system is filled with a water-based "
                "mixture rather than with oil, even though oil boils at a much "
                "higher temperature. (c = 4200 J/kg degrees C for water, "
                "2000 J/kg degrees C for oil)",
        "options": [
            "Oil holds no thermal store of its own, so it would leave the "
            "engine block hot however fast it was pumped",
            "Oil has the larger specific heat capacity, so it would have to be "
            "pumped round more than twice as fast",
            "Each kilogram of water carries about twice as much energy away "
            "for the same temperature rise",
            "Water boils more easily, and the boiling itself is what removes "
            "the energy from the engine block",
        ],
        "correct_index": 2,
        "why": "4200 is about twice 2000, so for the same mass and the same "
               "rise the water removes about twice the energy, which is the "
               "property a coolant is chosen for.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h16",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A storage heater holds 60 kg of clay blocks at "
                "180 degrees C. Calculate the energy released as the blocks "
                "cool to 20 degrees C. (c = 800 J/kg degrees C)",
        "options": [
            "8 640 000 J",
            "960 000 J",
            "128 000 J",
            "7 680 000 J",
        ],
        "correct_index": 3,
        "why": "The temperature change is 180 - 20 = 160 degrees C, so "
               "E = 60 x 800 x 160 = 7 680 000 J released.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h17",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radiator gives 630 000 J to a room while the water inside "
                "it cools by 25 degrees C. Calculate the mass of that water. "
                "(c = 4200 J/kg degrees C)",
        "options": [
            "150 kg",
            "0.17 kg",
            "60 kg",
            "6.0 kg",
        ],
        "correct_index": 3,
        "why": "Rearranged, m = E / (c x temperature change) = 630 000 / "
               "(4200 x 25) = 630 000 / 105 000 = 6.0 kg.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h18",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare warming 2.0 kg of water by 10 degrees C with warming "
                "5.0 kg of aluminium by 10 degrees C. Determine which needs "
                "more energy, and by how much. (c = 4200 J/kg degrees C for "
                "water, 900 J/kg degrees C for aluminium)",
        "options": [
            "The aluminium, by 39 000 J",
            "The water, by 129 000 J",
            "The aluminium, by 3900 J",
            "The water, by 39 000 J",
        ],
        "correct_index": 3,
        "why": "The water needs 2.0 x 4200 x 10 = 84 000 J and the aluminium "
               "5.0 x 900 x 10 = 45 000 J, so the water needs 39 000 J more.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h19",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Warming the water in a tank by 10 degrees C needs "
                "1 050 000 J. Predict the energy needed to warm the same tank "
                "of water by 25 degrees C.",
        "options": [
            "26 250 000 J",
            "1 312 500 J",
            "105 000 J",
            "2 625 000 J",
        ],
        "correct_index": 3,
        "why": "Energy is proportional to the temperature change when m and c "
               "are fixed, so 25 / 10 = 2.5 and 2.5 x 1 050 000 = "
               "2 625 000 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h20",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a determination of specific heat capacity the temperature "
                "of a metal block carries on rising for a minute after the "
                "heater has been switched off. Explain what a student should "
                "do about this.",
        "options": [
            "Record the reading taken at the instant the heater was switched "
            "off, since the block cannot warm any further once it is off",
            "Record the highest temperature the block reaches, because energy "
            "is still spreading through the metal",
            "Record the temperature of the room instead, because the block is "
            "no longer being warmed by the heater",
            "Record the first reading that falls, because the block reaches "
            "its true temperature as it cools",
        ],
        "correct_index": 1,
        "why": "Energy already supplied is still conducting through the block, "
               "so the largest reading is the temperature that energy actually "
               "produced.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h21",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 kg block is given 20 000 J, of which 2000 J escapes to "
                "the surroundings, and the block warms by 30 degrees C. "
                "Calculate the specific heat capacity of the block.",
        "options": [
            "1330 J/kg degrees C",
            "600 J/kg degrees C",
            "1200 J/kg degrees C",
            "120 J/kg degrees C",
        ],
        "correct_index": 2,
        "why": "Only 20 000 - 2000 = 18 000 J reached the block, so c = "
               "18 000 / (0.50 x 30) = 18 000 / 15 = 1200 J/kg degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h22",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg iron pan starts at 25 degrees C and is given "
                "45 000 J. Determine the temperature it reaches. "
                "(c = 450 J/kg degrees C)",
        "options": [
            "50 degrees C",
            "75 degrees C",
            "125 degrees C",
            "525 degrees C",
        ],
        "correct_index": 1,
        "why": "The temperature change is 45 000 / (2.0 x 450) = 50 degrees C, "
               "and the pan started at 25 degrees C, so it reaches "
               "75 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h23",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A concrete path and a pond hold the same mass and absorb the "
                "same energy from the Sun one afternoon. Predict which ends up "
                "at the higher temperature and explain why. "
                "(c = 800 J/kg degrees C for concrete, 4200 J/kg degrees C "
                "for water)",
        "options": [
            "The pond, because water needs less energy for each degree of "
            "temperature rise",
            "The concrete, because its smaller specific heat capacity gives a "
            "larger rise for the same energy",
            "The pond, because a liquid can reach a higher temperature than a "
            "solid of the same mass",
            "Both reach the same temperature, because the same energy was "
            "absorbed by the same mass",
        ],
        "correct_index": 1,
        "why": "Temperature change = E / (m x c), so with E and m equal the "
               "concrete rises 4200 / 800 = 5.25 times as much as the water.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h24",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A tank holds 25 kg of water. A 1.2 kW electric heater runs "
                "for 35 minutes with no energy escaping. Determine the rise in "
                "the water temperature. (c = 4200 J/kg degrees C)",
        "options": [
            "600 degrees C",
            "2.4 degrees C",
            "24 degrees C",
            "0.40 degrees C",
        ],
        "correct_index": 2,
        "why": "35 minutes is 2100 s, so the heater supplies 1200 x 2100 = "
               "2 520 000 J, and the rise is 2 520 000 / (25 x 4200) = "
               "24 degrees C.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h25",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "1.0 kg of copper and 1.0 kg of aluminium leave the same oven "
                "at 200 degrees C and both cool to 20 degrees C. Calculate the "
                "difference between the energies they release. "
                "(c = 385 J/kg degrees C for copper, 900 J/kg degrees C for "
                "aluminium)",
        "options": [
            "92 700 J",
            "231 300 J",
            "103 000 J",
            "9270 J",
        ],
        "correct_index": 0,
        "why": "Both fall by 180 degrees C: the copper releases 69 300 J and "
               "the aluminium 162 000 J, a difference of 92 700 J.",
    },
    {
        "id": "ks4-energy-changes-in-systems-h26",
        "subtopic_slug": "energy-changes-in-systems",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate the claim that a substance with a high specific heat "
                "capacity warms up quickly when it is heated.",
        "options": [
            "It is correct, because a high specific heat capacity means the "
            "substance takes in energy from its surroundings at a greater rate",
            "It is correct, because a high specific heat capacity raises the "
            "temperature the substance can reach",
            "It is wrong, because a high specific heat capacity needs more "
            "energy for each degree, so the rise is slower",
            "It is wrong, because a high specific heat capacity stops the "
            "substance warming by even one degree",
        ],
        "correct_index": 2,
        "why": "For a given supply of energy the temperature change is E / "
               "(m x c), so a larger c gives a smaller rise and therefore "
               "slower warming.",
    },
]
