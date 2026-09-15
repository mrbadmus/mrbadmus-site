"""Physics · Energy — the MRB-338 expansion of `changes-in-energy`.

One leaf only: AQA 8463 §4.1.1.2, the three energy-change equations —
Ek = 1/2 m v^2, Ep = m g h and Ee = 1/2 k e^2 — their substitutions, their
rearrangements, the unit conversions they need and the way each one behaves
when a quantity is doubled. The original twelve rows in `energy.py` already
own one substitution of each equation, the doubling-speed recall, the g-to-kg
and km/h-to-m/s conversions, the rearrangements for h and for k, the falling
ball solved for speed, the bow-and-arrow chain and one mass-against-speed
comparison. This file takes everything those twelve leave: the remaining
recall, the cm-to-m conversion, the third-and-fourth substitutions in named
real contexts, the rearrangements for m, for e, for v and for g, the
proportional behaviour of all three equations in both directions, and the
error-diagnosis rows where a pupil has squared the wrong thing.

The weight follows the CONTENT. `easier` stays at twelve because recall in
this leaf is three equations, one field strength, one squared quantity and
two proportionalities, and asking any of them a second way would be the same
question with different nouns. The demand lives in `standard` and `harder`,
where a substitution needs a conversion first and then a rearrangement, or
two stores have to be set equal to each other, so that is where the
twenty-six-row bands sit.

Nothing here does conservation bookkeeping — a store falls by this, another
rises by that, account for the difference. That is `energy-stores-systems`,
and specific heat capacity, power, dissipation, efficiency and the energy
resources are each a different leaf again.
"""

TOPIC = "energy"
SUBJECT = "physics"

QUESTIONS = [
    # ══ easier · e05–e12 ═════════════════════════════════════════════════
    # The recall the original four never ask — what each equation depends
    # on, g at the Earth's surface, which quantity is squared, and the
    # elastic doubling — plus one fresh substitution of each equation.
    {
        "id": "ks4-changes-in-energy-e05",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two quantities that the kinetic energy of a moving "
                "object depends on.",
        "options": [
            "Its mass and its speed",
            "Its mass and the height it has been raised to",
            "Its weight and the distance it has travelled",
            "Its speed and the length of time it has been moving for",
        ],
        "correct_index": 0,
        "why": "Ek = 1/2 m v^2 contains mass and speed and nothing else, so "
               "height, distance and time cannot appear in the answer.",
    },
    {
        "id": "ks4-changes-in-energy-e06",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A jogger of mass 45 kg runs at 4.0 m/s. Calculate the kinetic "
                "energy stored.",
        "options": [
            "90 J",
            "180 J",
            "360 J",
            "720 J",
        ],
        "correct_index": 2,
        "why": "Ek = 1/2 m v^2 = 0.5 x 45 x 4.0^2 = 0.5 x 45 x 16 = 360 J, "
               "squaring the speed before multiplying.",
    },
    {
        "id": "ks4-changes-in-energy-e07",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the value of the gravitational field strength at the "
                "surface of the Earth.",
        "options": [
            "0.98 N/kg",
            "9.8 N/kg",
            "98 N/kg",
            "980 N/kg",
        ],
        "correct_index": 1,
        "why": "On Earth g = 9.8 N/kg, and it is this value that is "
               "substituted into Ep = m g h unless a question names another "
               "planet.",
    },
    {
        "id": "ks4-changes-in-energy-e08",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A sack of sand of mass 5.0 kg is hauled 4.0 m up a scaffold. "
                "Calculate the gravitational potential energy stored. "
                "(g = 9.8 N/kg)",
        "options": [
            "20.0 J",
            "39.2 J",
            "49.0 J",
            "196 J",
        ],
        "correct_index": 3,
        "why": "Ep = m g h = 5.0 x 9.8 x 4.0 = 196 J, with all three "
               "quantities multiplied together.",
    },
    {
        "id": "ks4-changes-in-energy-e09",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring is stretched twice as far as before. Describe what "
                "happens to the elastic potential energy it stores.",
        "options": [
            "It is four times greater than before",
            "It is twice as great as before",
            "It is eight times greater than before",
            "It is unchanged, because the energy depends on the spring "
            "constant alone",
        ],
        "correct_index": 0,
        "why": "Ee = 1/2 k e^2 depends on the extension squared, so doubling "
               "the extension multiplies the energy stored by 2^2 = 4.",
    },
    {
        "id": "ks4-changes-in-energy-e10",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pinball machine's launch spring has a spring constant of "
                "600 N/m. Determine the elastic potential energy stored in it "
                "when it is pulled back by 0.20 m.",
        "options": [
            "60.0 J",
            "12.0 J",
            "120.0 J",
            "24.0 J",
        ],
        "correct_index": 1,
        "why": "Ee = 1/2 k e^2 = 0.5 x 600 x 0.20^2 = 0.5 x 600 x 0.040 = "
               "12.0 J. The extension is squared before the half is applied.",
    },
    {
        "id": "ks4-changes-in-energy-e11",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "In the equation Ek = 1/2 m v^2, state which quantity has to "
                "be squared.",
        "options": [
            "The mass of the object",
            "The kinetic energy in joules",
            "The speed of the object",
            "Both the mass and the speed, since both are raised to the power "
            "two",
        ],
        "correct_index": 2,
        "why": "The index 2 sits on v, so the speed is squared first and the "
               "result is then multiplied by the mass and by a half.",
    },
    {
        "id": "ks4-changes-in-energy-e12",
        "subtopic_slug": "changes-in-energy",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "The head of a hammer has a mass of 0.80 kg and is moving at "
                "10 m/s as it reaches a nail. Calculate its kinetic energy.",
        "options": [
            "4.0 J",
            "8.0 J",
            "80.0 J",
            "40.0 J",
        ],
        "correct_index": 3,
        "why": "Ek = 1/2 m v^2 = 0.5 x 0.80 x 10^2 = 0.5 x 0.80 x 100 = "
               "40.0 J.",
    },

    # ══ standard · s05–s26 ═══════════════════════════════════════════════
    # Each equation applied in a named context, with one conversion or one
    # proportional step in front of the substitution, plus the two
    # error-diagnosis rows a pupil meets in their own marking.
    {
        "id": "ks4-changes-in-energy-s05",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A squash ball of mass 250 g is served at 16 m/s. Calculate "
                "its kinetic energy.",
        "options": [
            "2.0 J",
            "32 J",
            "64 J",
            "32 000 J",
        ],
        "correct_index": 1,
        "why": "Convert first: 250 g = 0.250 kg, so Ek = 0.5 x 0.250 x 16^2 = "
               "0.5 x 0.250 x 256 = 32 J.",
    },
    {
        "id": "ks4-changes-in-energy-s06",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The spring inside a kitchen scale has a spring constant of "
                "800 N/m and is compressed by 5.0 cm. Calculate the elastic "
                "potential energy stored.",
        "options": [
            "1.0 J",
            "2.0 J",
            "20 J",
            "10 000 J",
        ],
        "correct_index": 0,
        "why": "5.0 cm = 0.050 m, so Ee = 0.5 x 800 x 0.050^2 = 0.5 x 800 x "
               "0.0025 = 1.0 J.",
    },
    {
        "id": "ks4-changes-in-energy-s07",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A textbook of mass 2.0 kg is lifted from the floor onto a "
                "desk 50 cm above it. Calculate the gravitational potential "
                "energy gained. (g = 9.8 N/kg)",
        "options": [
            "1.0 J",
            "4.9 J",
            "9.8 J",
            "980 J",
        ],
        "correct_index": 2,
        "why": "50 cm = 0.50 m, so Ep = 2.0 x 9.8 x 0.50 = 9.8 J; leaving the "
               "height in centimetres multiplies the answer by 100.",
    },
    {
        "id": "ks4-changes-in-energy-s08",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bucket holding 750 g of water is raised 4.0 m from the "
                "bottom of a well. Calculate the gravitational potential "
                "energy the water gains. (g = 9.8 N/kg)",
        "options": [
            "3.0 J",
            "7.4 J",
            "29 400 J",
            "29.4 J",
        ],
        "correct_index": 3,
        "why": "750 g = 0.750 kg, so Ep = 0.750 x 9.8 x 4.0 = 29.4 J.",
    },
    {
        "id": "ks4-changes-in-energy-s09",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A delivery van of mass 1200 kg travels at 54 km/h. Calculate "
                "its kinetic energy.",
        "options": [
            "9000 J",
            "135 000 J",
            "270 000 J",
            "1 749 600 J",
        ],
        "correct_index": 1,
        "why": "54 km/h divided by 3.6 is 15 m/s, so Ek = 0.5 x 1200 x 15^2 = "
               "0.5 x 1200 x 225 = 135 000 J.",
    },
    {
        "id": "ks4-changes-in-energy-s10",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A diver of mass 60 kg climbs from the 4.0 m board up to the "
                "9.0 m board. Calculate the extra gravitational potential "
                "energy she gains. (g = 9.8 N/kg)",
        "options": [
            "2940 J",
            "300 J",
            "5292 J",
            "7644 J",
        ],
        "correct_index": 0,
        "why": "The rise is 9.0 - 4.0 = 5.0 m, so Ep = 60 x 9.8 x 5.0 = "
               "2940 J; h is the change in height, not the final height.",
    },
    {
        "id": "ks4-changes-in-energy-s11",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lorry of mass 8000 kg and a car of mass 1000 kg travel "
                "along the same road at 18 m/s. Compare their kinetic "
                "energies.",
        "options": [
            "They store the same amount, because the speed decides the energy",
            "The car stores eight times as much, because the smaller mass is "
            "divided into the energy",
            "The lorry stores eight times as much, because Ek is proportional "
            "to mass",
            "The lorry stores 64 times as much, because the mass is squared "
            "as well",
        ],
        "correct_index": 2,
        "why": "At the same speed Ek is proportional to mass, and 8000 / 1000 "
               "= 8, so the lorry stores eight times as much.",
    },
    {
        "id": "ks4-changes-in-energy-s12",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car stores 400 kJ of kinetic energy when it travels at "
                "30 m/s. Calculate the kinetic energy it stores at 15 m/s.",
        "options": [
            "400 kJ",
            "800 kJ",
            "200 kJ",
            "100 kJ",
        ],
        "correct_index": 3,
        "why": "Ek is proportional to the speed squared, so halving the speed "
               "divides the energy by 2^2 = 4, giving 400 / 4 = 100 kJ.",
    },
    {
        "id": "ks4-changes-in-energy-s13",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Stretching a spring by 0.20 m fills its elastic store with "
                "3.0 J. Determine the energy in that store once the same "
                "spring has been stretched by 0.60 m.",
        "options": [
            "9.0 J",
            "27 J",
            "5.4 J",
            "81 J",
        ],
        "correct_index": 1,
        "why": "The extension is three times greater and Ee depends on the "
               "extension squared, so the energy is 3^2 = 9 times greater: "
               "3.0 x 9 = 27 J.",
    },
    {
        "id": "ks4-changes-in-energy-s14",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Spring P has a spring constant of 150 N/m and spring Q has a "
                "spring constant of 450 N/m. Both are extended by 0.20 m. "
                "Compare the energy each one stores.",
        "options": [
            "Q stores three times as much as P, because Ee is proportional "
            "to k",
            "Q stores nine times as much as P, because the spring constant is "
            "squared",
            "P and Q store the same, because their extensions are equal",
            "P stores three times as much as Q, because a softer spring holds "
            "more energy at the same extension",
        ],
        "correct_index": 0,
        "why": "At the same extension Ee is proportional to k: P stores 0.5 x "
               "150 x 0.040 = 3.0 J and Q stores 0.5 x 450 x 0.040 = 9.0 J.",
    },
    {
        "id": "ks4-changes-in-energy-s15",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil works out the kinetic energy of a 4.0 kg mass moving "
                "at 6.0 m/s as 1/2 x 4.0 x 6.0 = 12 J. Calculate the correct "
                "value.",
        "options": [
            "12 J",
            "24 J",
            "72 J",
            "144 J",
        ],
        "correct_index": 2,
        "why": "The speed has to be squared first: Ek = 0.5 x 4.0 x 6.0^2 = "
               "0.5 x 4.0 x 36 = 72 J.",
    },
    {
        "id": "ks4-changes-in-energy-s16",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rock of mass 2.0 kg is raised 6.0 m above the surface of "
                "Mars, where the gravitational field strength is 3.7 N/kg. "
                "Calculate the gravitational potential energy gained.",
        "options": [
            "12.0 J",
            "22.2 J",
            "117.6 J",
            "44.4 J",
        ],
        "correct_index": 3,
        "why": "Ep = m g h uses the field strength of the planet named, so "
               "Ep = 2.0 x 3.7 x 6.0 = 44.4 J rather than the Earth value.",
    },
    {
        "id": "ks4-changes-in-energy-s17",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "The head of a sledgehammer has a mass of 2.5 kg. It is "
                "lifted 1.6 m and then swung down. Calculate the "
                "gravitational potential energy it had at the top. "
                "(g = 9.8 N/kg)",
        "options": [
            "15.7 J",
            "39.2 J",
            "4.0 J",
            "24.5 J",
        ],
        "correct_index": 1,
        "why": "Ep = m g h = 2.5 x 9.8 x 1.6 = 39.2 J.",
    },
    {
        "id": "ks4-changes-in-energy-s18",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A child of mass 30 kg slides down a playground slide from a "
                "height of 2.0 m. Calculate the gravitational potential "
                "energy she loses. (g = 9.8 N/kg)",
        "options": [
            "588 J",
            "60.0 J",
            "294 J",
            "19.6 J",
        ],
        "correct_index": 0,
        "why": "Ep = m g h = 30 x 9.8 x 2.0 = 588 J, and the store empties by "
               "that amount as she descends.",
    },
    {
        "id": "ks4-changes-in-energy-s19",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A lift car of mass 800 kg rises 12 m up a shaft. Determine "
                "the increase in its gravitational potential store. "
                "(g = 9.8 N/kg)",
        "options": [
            "117.6 J",
            "7840 J",
            "94 080 J",
            "9600 J",
        ],
        "correct_index": 2,
        "why": "Ep = m g h = 800 x 9.8 x 12 = 94 080 J.",
    },
    {
        "id": "ks4-changes-in-energy-s20",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A skateboarder of total mass 55 kg rolls along a level path "
                "at 6.0 m/s. Calculate the kinetic energy stored.",
        "options": [
            "165 J",
            "330 J",
            "1980 J",
            "990 J",
        ],
        "correct_index": 3,
        "why": "Ek = 0.5 x 55 x 6.0^2 = 0.5 x 55 x 36 = 990 J.",
    },
    {
        "id": "ks4-changes-in-energy-s21",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 1.0 kg bag of sand and a 4.0 kg bag of sand are each raised "
                "2.0 m. Calculate the difference between the gravitational "
                "potential energies they gain. (g = 9.8 N/kg)",
        "options": [
            "19.6 J",
            "58.8 J",
            "78.4 J",
            "98.0 J",
        ],
        "correct_index": 1,
        "why": "The difference in mass is 3.0 kg, so the difference in energy "
               "is 3.0 x 9.8 x 2.0 = 58.8 J.",
    },
    {
        "id": "ks4-changes-in-energy-s22",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A football of mass 0.44 kg leaves a boot at 25 m/s. "
                "Calculate its kinetic energy.",
        "options": [
            "137.5 J",
            "11.0 J",
            "275.0 J",
            "5.5 J",
        ],
        "correct_index": 0,
        "why": "Ek = 0.5 x 0.44 x 25^2 = 0.5 x 0.44 x 625 = 137.5 J.",
    },
    {
        "id": "ks4-changes-in-energy-s23",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A catapult's rubber band has a spring constant of 160 N/m. "
                "Determine the energy in its elastic store after the band has "
                "been pulled back 0.30 m.",
        "options": [
            "24.0 J",
            "14.4 J",
            "7.2 J",
            "48.0 J",
        ],
        "correct_index": 2,
        "why": "Ee = 0.5 x 160 x 0.30^2 = 0.5 x 160 x 0.090 = 7.2 J.",
    },
    {
        "id": "ks4-changes-in-energy-s24",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil works out the elastic potential energy of a spring "
                "with a spring constant of 50 N/m extended by 0.20 m as "
                "1/2 x 50 x 50 x 0.20 = 250 J. Calculate the correct value.",
        "options": [
            "10.0 J",
            "250 J",
            "5.0 J",
            "1.0 J",
        ],
        "correct_index": 3,
        "why": "It is the extension that is squared, not the spring constant: "
               "Ee = 0.5 x 50 x 0.20^2 = 0.5 x 50 x 0.040 = 1.0 J.",
    },
    {
        "id": "ks4-changes-in-energy-s25",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trolley stores 108 J of kinetic energy while it is moving "
                "at 6.0 m/s. Calculate its mass.",
        "options": [
            "36.0 kg",
            "6.0 kg",
            "18.0 kg",
            "3.0 kg",
        ],
        "correct_index": 1,
        "why": "Rearranging Ek = 1/2 m v^2 gives m = 2Ek / v^2 = 216 / 36 = "
               "6.0 kg.",
    },
    {
        "id": "ks4-changes-in-energy-s26",
        "subtopic_slug": "changes-in-energy",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A hiker of mass 65 kg climbs a hill that rises 300 m. "
                "Calculate the gravitational potential energy gained. "
                "(g = 9.8 N/kg)",
        "options": [
            "191 100 J",
            "19 110 J",
            "637 J",
            "19 500 J",
        ],
        "correct_index": 0,
        "why": "Ep = m g h = 65 x 9.8 x 300 = 191 100 J.",
    },

    # ══ harder · h05–h26 ═════════════════════════════════════════════════
    # Rearrangements for the quantities the frozen twelve never solve for,
    # one store set equal to another, and the comparisons, predictions and
    # evaluations the three equations support.
    {
        "id": "ks4-changes-in-energy-h05",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A trampoline mat stores 1764 J of elastic potential energy. "
                "All of it is transferred to the gravitational potential "
                "store of a 40 kg gymnast. Calculate the height she rises. "
                "(g = 9.8 N/kg)",
        "options": [
            "0.22 m",
            "44.1 m",
            "4.5 m",
            "180 m",
        ],
        "correct_index": 2,
        "why": "Set Ee = m g h, so h = 1764 / (40 x 9.8) = 1764 / 392 = "
               "4.5 m.",
    },
    {
        "id": "ks4-changes-in-energy-h06",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball is thrown straight upwards at 14 m/s. Calculate the "
                "greatest height it reaches, assuming nothing is dissipated. "
                "(g = 9.8 N/kg)",
        "options": [
            "20.0 m",
            "1.4 m",
            "196 m",
            "10.0 m",
        ],
        "correct_index": 3,
        "why": "The kinetic store empties into the gravitational store, so "
               "1/2 m v^2 = m g h; the mass cancels and h = 14^2 / (2 x 9.8) "
               "= 196 / 19.6 = 10.0 m.",
    },
    {
        "id": "ks4-changes-in-energy-h07",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A roof tile comes loose and reaches the pavement at 9.8 m/s. "
                "Determine the height it fell from, assuming nothing is "
                "dissipated. (g = 9.8 N/kg)",
        "options": [
            "4.9 m",
            "1.0 m",
            "9.8 m",
            "96.0 m",
        ],
        "correct_index": 0,
        "why": "m g h = 1/2 m v^2, so h = v^2 / (2 x 9.8) = 96.04 / 19.6 = "
               "4.9 m.",
    },
    {
        "id": "ks4-changes-in-energy-h08",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring with a spring constant of 320 N/m stores 10 J of "
                "elastic potential energy. Determine its extension.",
        "options": [
            "0.063 m",
            "0.25 m",
            "0.031 m",
            "0.18 m",
        ],
        "correct_index": 1,
        "why": "Rearranging Ee = 1/2 k e^2 gives e^2 = 2Ee / k = 20 / 320 = "
               "0.0625, and the square root of 0.0625 is 0.25 m.",
    },
    {
        "id": "ks4-changes-in-energy-h09",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which stores more kinetic energy: an 8000 kg lorry "
                "moving at 12 m/s, or a 2000 kg car moving at 24 m/s.",
        "options": [
            "The lorry stores four times as much, because only the mass "
            "matters at these speeds",
            "The car stores four times as much, because speed counts for more "
            "than mass",
            "They store the same amount, because the mass is four times "
            "greater while the speed is halved",
            "The lorry stores twice as much, because its mass counts twice "
            "over in the equation",
        ],
        "correct_index": 2,
        "why": "The lorry stores 0.5 x 8000 x 144 = 576 000 J and the car "
               "stores 0.5 x 2000 x 576 = 576 000 J, because squaring the "
               "speed exactly undoes the four times larger mass.",
    },
    {
        "id": "ks4-changes-in-energy-h10",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toy's spring is compressed by 0.10 m and then raises a "
                "0.50 kg ball to a height of 2.0 m. Determine the spring "
                "constant, assuming nothing is dissipated. (g = 9.8 N/kg)",
        "options": [
            "196 N/m",
            "980 N/m",
            "19 600 N/m",
            "1960 N/m",
        ],
        "correct_index": 3,
        "why": "The ball gains 0.50 x 9.8 x 2.0 = 9.8 J, so 1/2 k e^2 = 9.8 "
               "and k = 19.6 / 0.010 = 1960 N/m.",
    },
    {
        "id": "ks4-changes-in-energy-h11",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A train stores 500 kJ of kinetic energy at a steady speed. "
                "Predict the kinetic energy it stores when its speed is three "
                "times greater.",
        "options": [
            "4500 kJ",
            "1500 kJ",
            "13 500 kJ",
            "3000 kJ",
        ],
        "correct_index": 0,
        "why": "Ek is proportional to the speed squared, so tripling the "
               "speed multiplies the energy by 3^2 = 9: 500 x 9 = 4500 kJ.",
    },
    {
        "id": "ks4-changes-in-energy-h12",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Spring P has a spring constant of 200 N/m and spring Q has a "
                "spring constant of 800 N/m. Each stores 4.0 J of elastic "
                "potential energy. Compare their extensions.",
        "options": [
            "Q is extended twice as far as P, because a stiffer spring "
            "stretches further",
            "P is extended twice as far as Q, because it is the softer spring",
            "They are extended by the same amount, because they store the "
            "same energy",
            "P is extended four times as far as Q, because the extension is "
            "proportional to the spring constant",
        ],
        "correct_index": 1,
        "why": "e^2 = 2Ee / k, so P extends by the square root of 8 / 200 = "
               "0.20 m and Q by the square root of 8 / 800 = 0.10 m.",
    },
    {
        "id": "ks4-changes-in-energy-h13",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A toy of mass 0.25 kg leaves a spring launcher at 12 m/s. "
                "Determine the elastic potential energy the spring must have "
                "stored, assuming none of it is dissipated.",
        "options": [
            "1.5 J",
            "3.0 J",
            "18.0 J",
            "36.0 J",
        ],
        "correct_index": 2,
        "why": "The elastic store empties entirely into the kinetic store, so "
               "Ee = 0.5 x 0.25 x 12^2 = 0.5 x 0.25 x 144 = 18.0 J.",
    },
    {
        "id": "ks4-changes-in-energy-h14",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An apple of mass 250 g falls 40 cm from a branch to the "
                "ground. Determine its kinetic energy just before it lands. "
                "(g = 9.8 N/kg)",
        "options": [
            "980 J",
            "98.0 J",
            "98 000 J",
            "0.98 J",
        ],
        "correct_index": 3,
        "why": "Both quantities need converting: 250 g = 0.250 kg and 40 cm = "
               "0.40 m, so the energy transferred is 0.250 x 9.8 x 0.40 = "
               "0.98 J.",
    },
    {
        "id": "ks4-changes-in-energy-h15",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 kg ball and a 0.50 kg ball are released from the same "
                "height. Explain, using the two energy equations, why they "
                "reach the ground at the same speed when air resistance is "
                "ignored.",
        "options": [
            "m g h equals 1/2 m v^2, so the mass cancels from both sides and "
            "the speed depends only on the height fallen",
            "The heavier ball gains more energy, so it needs a longer time to "
            "reach the ground below",
            "Both balls have the same weight once they are falling, however "
            "much mass they have",
            "The lighter ball has to fall faster in order to make up for its "
            "smaller mass",
        ],
        "correct_index": 0,
        "why": "Setting the two stores equal gives v^2 = 2 g h, in which the "
               "mass does not appear at all, so both balls arrive at the same "
               "speed.",
    },
    {
        "id": "ks4-changes-in-energy-h16",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A crate of sand gains 1470 J of gravitational potential "
                "energy as a crane lifts it 6.0 m. Determine its mass. "
                "(g = 9.8 N/kg)",
        "options": [
            "245 kg",
            "25.0 kg",
            "150 kg",
            "8820 kg",
        ],
        "correct_index": 1,
        "why": "Rearranging Ep = m g h gives m = Ep / (g x h) = 1470 / "
               "(9.8 x 6.0) = 1470 / 58.8 = 25.0 kg.",
    },
    {
        "id": "ks4-changes-in-energy-h17",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A rock of mass 4.0 kg raised 3.0 m on another planet gains "
                "45.6 J of gravitational potential energy. Determine the "
                "gravitational field strength on that planet.",
        "options": [
            "15.2 N/kg",
            "11.4 N/kg",
            "3.8 N/kg",
            "547 N/kg",
        ],
        "correct_index": 2,
        "why": "Rearranging Ep = m g h gives g = Ep / (m x h) = 45.6 / 12 = "
               "3.8 N/kg.",
    },
    {
        "id": "ks4-changes-in-energy-h18",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball of mass 0.40 kg is dropped from a height of 6.0 m. "
                "Determine its kinetic energy after it has fallen the first "
                "2.0 m. (g = 9.8 N/kg)",
        "options": [
            "15.7 J",
            "0.80 J",
            "23.5 J",
            "7.84 J",
        ],
        "correct_index": 3,
        "why": "Only the 2.0 m already fallen has emptied the gravitational "
               "store, so the kinetic energy is 0.40 x 9.8 x 2.0 = 7.84 J.",
    },
    {
        "id": "ks4-changes-in-energy-h19",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bungee cord has a spring constant of 60 N/m. At the lowest "
                "point of a jump it is extended 20 m. Determine the energy in "
                "its elastic store.",
        "options": [
            "12 000 J",
            "1200 J",
            "600 J",
            "24 000 J",
        ],
        "correct_index": 0,
        "why": "Ee = 0.5 x 60 x 20^2 = 0.5 x 60 x 400 = 12 000 J.",
    },
    {
        "id": "ks4-changes-in-energy-h20",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A car of mass 900 kg stores 180 kJ of kinetic energy. "
                "Determine its speed in km/h.",
        "options": [
            "5.6 km/h",
            "72.0 km/h",
            "20.0 km/h",
            "400 km/h",
        ],
        "correct_index": 1,
        "why": "v^2 = 2Ek / m = 360 000 / 900 = 400, so v = 20 m/s, and "
               "20 x 3.6 = 72.0 km/h.",
    },
    {
        "id": "ks4-changes-in-energy-h21",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A spring is stretched further until it stores nine times as "
                "much elastic potential energy as before. Determine the "
                "factor by which its extension has increased.",
        "options": [
            "1.5 times",
            "9.0 times",
            "3.0 times",
            "4.5 times",
        ],
        "correct_index": 2,
        "why": "Ee is proportional to the extension squared, so a nine times "
               "larger store needs an extension larger by the square root of "
               "9, which is 3.0 times.",
    },
    {
        "id": "ks4-changes-in-energy-h22",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.20 kg ball and a 0.80 kg ball are dropped from the same "
                "height of 2.0 m. Compare the kinetic energy each one has "
                "just before it lands.",
        "options": [
            "The 0.80 kg ball has twice as much, because it lands at twice "
            "the speed",
            "They have the same amount, because the height alone decides the "
            "energy",
            "The 0.20 kg ball has four times as much, because a lighter "
            "object speeds up sooner as it falls",
            "The 0.80 kg ball has four times as much, because the energy is "
            "proportional to mass",
        ],
        "correct_index": 3,
        "why": "Each ball's kinetic energy equals m g h, so 0.20 x 9.8 x 2.0 "
               "= 3.92 J against 0.80 x 9.8 x 2.0 = 15.68 J, a factor of "
               "four.",
    },
    {
        "id": "ks4-changes-in-energy-h23",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "The mass of a loaded van is doubled and its speed is doubled "
                "as well. Determine the factor by which its kinetic energy "
                "increases.",
        "options": [
            "8.0 times",
            "6.0 times",
            "4.0 times",
            "16.0 times",
        ],
        "correct_index": 0,
        "why": "Ek is proportional to mass and to the speed squared, so the "
               "energy grows by 2 for the mass and by 2^2 = 4 for the speed, "
               "which is 8.0 times in total.",
    },
    {
        "id": "ks4-changes-in-energy-h24",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 20 kg bag of cement is raised 3.0 m to the first floor of "
                "a building, and then a further 3.0 m to the second floor. "
                "Compare the gravitational potential energy gained in each of "
                "the two stages. (g = 9.8 N/kg)",
        "options": [
            "The second stage gains 1176 J, because the rise doubles on the "
            "way up",
            "Each stage gains 588 J, because the mass and the rise are the "
            "same",
            "The second stage gains 2352 J, because the height is squared",
            "The first stage gains 1176 J, because starting from the floor "
            "needs a larger push",
        ],
        "correct_index": 1,
        "why": "Ep = m g h uses the CHANGE in height, and that change is "
               "3.0 m each time, so each stage gains 20 x 9.8 x 3.0 = 588 J.",
    },
    {
        "id": "ks4-changes-in-energy-h25",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A pupil states that a spring with twice the spring constant "
                "stores twice the energy at the same extension. Evaluate this "
                "statement.",
        "options": [
            "It is wrong: the energy would be four times greater, because the "
            "spring constant is squared",
            "It is correct, because the energy stored does not depend on the "
            "extension",
            "It is correct, because the energy stored is proportional to the "
            "spring constant",
            "It is wrong: the energy would be halved, because a stiffer "
            "spring stretches less",
        ],
        "correct_index": 2,
        "why": "In Ee = 1/2 k e^2 the spring constant appears to the power "
               "one, so at a fixed extension doubling k doubles the energy "
               "stored.",
    },
    {
        "id": "ks4-changes-in-energy-h26",
        "subtopic_slug": "changes-in-energy",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ball of mass 0.40 kg hits a wall at 25 m/s and rebounds at "
                "15 m/s. Calculate the change in its kinetic energy.",
        "options": [
            "20.0 J",
            "45.0 J",
            "170 J",
            "80.0 J",
        ],
        "correct_index": 3,
        "why": "Before the bounce Ek = 0.5 x 0.40 x 625 = 125 J and after it "
               "Ek = 0.5 x 0.40 x 225 = 45 J, so the change is 125 - 45 = "
               "80.0 J.",
    },
]
