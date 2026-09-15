"""Chemistry · Quantitative chemistry — the MRB-338 expansion for
`concentration-of-solutions`.

AQA 4.3.4.1 at Foundation depth: concentration in g/dm³ as mass of solute per
volume of SOLUTION, the formula used forwards and both ways round, and the
cm³-to-dm³ conversion that decides whether an answer is out by a factor of a
thousand. Around the arithmetic sit the ideas: dilution keeps the solute and
adds volume, evaporation keeps the solute and removes volume, mixing two
solutions of one solute adds their solutes, and concentration does not change
when a sample is poured out. Harder rows go two and three steps — dilute then
sample, evaporate then scale, mix two strengths — and separate 'concentrated'
from 'more solute'.

⚠️ FOUNDATION TIER. Concentration here is in g/dm³ only. No mole appears in any
stem, option or `why`; mol/dm³ is Higher-tier and belongs to
`using-moles-calculations`.
"""

TOPIC = "quantitative"
SUBJECT = "chemistry"

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "ks4-concentration-of-solutions-e05",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution's concentration in g/dm³ can be worked out from "
                "two measured quantities. Identify the correct calculation.",
        "options": [
            "mass of solute (g) ÷ volume of solution (dm³)",
            "volume of solution (dm³) ÷ mass of solute (g)",
            "mass of solute (g) × volume of solution (dm³) all over one "
            "thousand",
            "mass of solute (g) ÷ volume of water added (cm³)",
        ],
        "correct_index": 0,
        "why": "Concentration in g/dm³ is how many grams of solute there are in "
               "each cubic decimetre of solution.",
    },
    {
        "id": "ks4-concentration-of-solutions-e06",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 0.50 dm³ solution contains 10 g of dissolved salt. "
                "Calculate its concentration in g/dm³.",
        "options": [
            "5.0 g/dm³",
            "20 g/dm³",
            "10 g/dm³",
            "0.050 g/dm³",
        ],
        "correct_index": 1,
        "why": "10 ÷ 0.50 = 20 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-e07",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to the concentration of a solution when "
                "more water is stirred into it.",
        "options": [
            "It rises, because there is now more solution in the beaker",
            "It stays the same, because the solute has not been changed in any "
            "way",
            "It falls, because the same solute is spread through more solution",
            "It falls, because some of the solute turns back into a solid",
        ],
        "correct_index": 2,
        "why": "Dilution adds volume without adding solute, so the mass of "
               "solute in each dm³ goes down.",
    },
    {
        "id": "ks4-concentration-of-solutions-e08",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beaker holds 0.40 dm³ of a solution labelled 30 g/dm³. "
                "Calculate the mass of dissolved solid it contains.",
        "options": [
            "75 g",
            "0.013 g",
            "30 g",
            "12 g",
        ],
        "correct_index": 3,
        "why": "mass = concentration × volume = 30 × 0.40 = 12 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-e09",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which volume is used in the concentration formula: the "
                "volume of water added, or the volume of the final solution.",
        "options": [
            "The volume of the final solution",
            "The volume of the water added",
            "The larger of the two volumes",
            "The volume of the solid dissolved",
        ],
        "correct_index": 0,
        "why": "Concentration is defined per volume of solution, which is why a "
                "standard solution is made up to the mark after the solid has "
                "dissolved.",
    },
    {
        "id": "ks4-concentration-of-solutions-e10",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Two beakers each hold 250 cm³ of sugar solution. One was made "
                "with 5 g of sugar and the other with 20 g. Identify the more "
                "dilute solution.",
        "options": [
            "The 20 g solution, because more sugar means more spreading out",
            "The 5 g solution, because it holds less sugar in the same volume",
            "Neither, because the volumes of the two solutions are the same as "
            "each other",
            "The 20 g solution, because a heavier solution is a weaker one",
        ],
        "correct_index": 1,
        "why": "Dilute means little solute per unit volume, and 5 g in 250 cm³ "
               "is a quarter of the concentration of 20 g in 250 cm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-e11",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the concentration in g/dm³ of a solution holding "
                "45 g of solute in 1.5 dm³.",
        "options": [
            "67.5 g/dm³",
            "0.033 g/dm³",
            "30 g/dm³",
            "43.5 g/dm³",
        ],
        "correct_index": 2,
        "why": "45 ÷ 1.5 = 30 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-e12",
        "subtopic_slug": "concentration-of-solutions",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what the unit g/dm³ means.",
        "options": [
            "Grams of solvent per solution",
            "Grams of solute per gram of water",
            "Grams of solid left after drying",
            "Grams of solute in every cubic decimetre of solution",
        ],
        "correct_index": 3,
        "why": "The unit is read straight off the formula: grams of solute "
               "divided by cubic decimetres of solution.",
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "ks4-concentration-of-solutions-s05",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "8.0 g of potassium chloride is dissolved in water and the "
                "solution made up to 400 cm³. Calculate the concentration in "
                "g/dm³.",
        "options": [
            "0.020 g/dm³",
            "3.2 g/dm³",
            "20 g/dm³",
            "50 g/dm³",
        ],
        "correct_index": 2,
        "why": "400 cm³ is 0.400 dm³, so the concentration is "
               "8.0 ÷ 0.400 = 20 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s06",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A laboratory needs 500 cm³ of sodium chloride solution at "
                "24 g/dm³. Determine the mass of sodium chloride that must "
                "be weighed out.",
        "options": [
            "48 g",
            "12 000 g",
            "24 g",
            "12 g",
        ],
        "correct_index": 3,
        "why": "500 cm³ is 0.500 dm³, so the mass is 24 × 0.500 = 12 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-s07",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "6.0 g of solid dissolves completely to give a 40 g/dm³ "
                "solution. Determine the volume of that solution, in cm³.",
        "options": [
            "150 cm³",
            "240 cm³",
            "6.7 cm³",
            "0.15 cm³",
        ],
        "correct_index": 0,
        "why": "6.0 ÷ 40 = 0.15 dm³, which is 150 cm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s08",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A technician takes 100 cm³ of 50 g/dm³ solution and adds "
                "water until the volume reaches 500 cm³. Calculate the "
                "concentration of the diluted solution.",
        "options": [
            "250 g/dm³",
            "10 g/dm³",
            "5.0 g/dm³",
            "40 g/dm³",
        ],
        "correct_index": 1,
        "why": "The solute stays at 50 × 0.100 = 5.0 g, now spread through "
               "0.500 dm³, giving 10 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s09",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the volume of the solution is used in the "
                "concentration formula rather than the volume of water added.",
        "options": [
            "Because water is a liquid and its volume cannot be measured "
            "accurately at all",
            "Because the dissolved solid changes the volume, so the two are "
            "not equal",
            "Because the water evaporates while the solution is being made up",
            "Because the solid takes up no room once it has dissolved fully",
        ],
        "correct_index": 1,
        "why": "Adding solute to water alters the total volume, so only the "
               "final volume of solution gives a concentration that can be "
               "relied on.",
    },
    {
        "id": "ks4-concentration-of-solutions-s10",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student dissolves 15 g of copper sulfate in water and makes "
                "the solution up to 250 cm³. Calculate the concentration in "
                "g/dm³.",
        "options": [
            "0.060 g/dm³",
            "3.75 g/dm³",
            "16.7 g/dm³",
            "60 g/dm³",
        ],
        "correct_index": 3,
        "why": "250 cm³ is 0.250 dm³, so the concentration is "
               "15 ÷ 0.250 = 60 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s11",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the mass of glucose in 2.5 dm³ of a solution of "
                "concentration 16 g/dm³.",
        "options": [
            "6.4 g",
            "40 g",
            "0.16 g",
            "18.5 g",
        ],
        "correct_index": 1,
        "why": "16 × 2.5 = 40 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-s12",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student boils a solution until half of the water has gone. "
                "Predict the effect on the concentration.",
        "options": [
            "It halves, because half of the solution has been driven off",
            "It stays the same, because the solute and the water leave together",
            "It doubles, because the same solute is now in half the volume",
            "It falls to nothing, because boiling destroys the dissolved solute",
        ],
        "correct_index": 2,
        "why": "Water leaves as vapour but solute does not, so the mass of "
               "solute per dm³ doubles when the volume halves.",
    },
    {
        "id": "ks4-concentration-of-solutions-s13",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "100 cm³ of a 12 g/dm³ solution is mixed with 100 cm³ of pure "
                "water. Calculate the concentration of the mixture.",
        "options": [
            "24 g/dm³",
            "12 g/dm³",
            "1.2 g/dm³",
            "6.0 g/dm³",
        ],
        "correct_index": 3,
        "why": "The 1.2 g of solute now occupies 0.200 dm³, so the "
               "concentration is 1.2 ÷ 0.200 = 6.0 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s14",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'I dissolved 5 g to make 250 cm³, so the "
                "concentration is 5 ÷ 250 = 0.02 g/dm³.' Identify the error "
                "and give the correct value.",
        "options": [
            "The mass should have been divided by 1000; it is 0.005 g/dm³",
            "The two values were divided the wrong way round; it is 50 g/dm³",
            "The volume was left in cm³ instead of dm³; it is 20 g/dm³",
            "Nothing is wrong, because the volume was given in cm³ already",
        ],
        "correct_index": 2,
        "why": "250 cm³ is 0.250 dm³, so the concentration is "
               "5 ÷ 0.250 = 20 g/dm³ — a thousand times the value written.",
    },
    {
        "id": "ks4-concentration-of-solutions-s15",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Calculate the volume of a solution of concentration 25 g/dm³ "
                "that contains 10 g of solute.",
        "options": [
            "0.40 dm³",
            "2.5 dm³",
            "250 dm³",
            "0.025 dm³",
        ],
        "correct_index": 0,
        "why": "volume = mass ÷ concentration = 10 ÷ 25 = 0.40 dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s16",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which is the more concentrated: 14 g of solute in "
                "200 cm³, or 30 g of solute in 500 cm³.",
        "options": [
            "The 30 g solution, because it holds more solute in total",
            "The 14 g solution, at 70 g/dm³ against 60 g/dm³",
            "They are equally concentrated, at 70 g/dm³ each",
            "The 30 g solution, at 60 g/dm³ against 28 g/dm³",
        ],
        "correct_index": 1,
        "why": "14 ÷ 0.200 = 70 g/dm³ and 30 ÷ 0.500 = 60 g/dm³, so the "
               "smaller sample is the stronger solution.",
    },
    {
        "id": "ks4-concentration-of-solutions-s17",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 2.0 dm³ jug of squash holds 24 g of dissolved sugar. "
                "Calculate the mass of sugar in a 250 cm³ glass poured from "
                "the jug.",
        "options": [
            "12 g",
            "6.0 g",
            "3.0 g",
            "48 g",
        ],
        "correct_index": 2,
        "why": "The squash is 24 ÷ 2.0 = 12 g/dm³, so 0.250 dm³ holds "
               "12 × 0.250 = 3.0 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-s18",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why the concentration of a solution does not change "
                "when a small sample is poured out of a large bottle.",
        "options": [
            "Because the bottle is refilled by air taking the place of the "
            "liquid poured",
            "Because concentration is fixed by the label on the bottle rather "
            "than measured",
            "Because the solute and the volume both fall in the same "
            "proportion",
            "Because the solute settles towards the bottom and stays in the "
            "bottle",
        ],
        "correct_index": 2,
        "why": "Concentration is a ratio, so taking a tenth of the solution "
               "takes a tenth of the solute with it and leaves the ratio "
               "alone.",
    },
    {
        "id": "ks4-concentration-of-solutions-s19",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A chemist dissolves 0.60 g of salt, then tops the mixture "
                "up to a final volume of 50 cm³. Determine its "
                "concentration, in g/dm³.",
        "options": [
            "0.012 g/dm³",
            "1.2 g/dm³",
            "12 g/dm³",
            "30 g/dm³",
        ],
        "correct_index": 2,
        "why": "50 cm³ is 0.050 dm³, so the concentration is "
               "0.60 ÷ 0.050 = 12 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s20",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student needs 2.0 dm³ of a solution of concentration "
                "15 g/dm³. Determine the mass of solid to weigh out.",
        "options": [
            "7.5 g",
            "15 g",
            "30 g",
            "0.13 g",
        ],
        "correct_index": 2,
        "why": "mass = 15 × 2.0 = 30 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-s21",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the volume of water that must be added to 100 cm³ "
                "of a 60 g/dm³ solution to bring it to 20 g/dm³.",
        "options": [
            "300 cm³",
            "100 cm³",
            "600 cm³",
            "200 cm³",
        ],
        "correct_index": 3,
        "why": "The 6.0 g of solute must fill 0.300 dm³ to read 20 g/dm³, so "
               "200 cm³ of water is added to the 100 cm³ already there.",
    },
    {
        "id": "ks4-concentration-of-solutions-s22",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A bottle is labelled '5 g of solute per 100 cm³ of solution'. "
                "Determine this concentration in g/dm³.",
        "options": [
            "0.05 g/dm³",
            "5 g/dm³",
            "50 g/dm³",
            "500 g/dm³",
        ],
        "correct_index": 2,
        "why": "1 dm³ is ten lots of 100 cm³, so it holds ten lots of 5 g, "
               "which is 50 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s23",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a saturated solution of a salt has a fixed "
                "concentration at a given temperature.",
        "options": [
            "Because a saturated solution holds exactly one gram in every "
            "cubic decimetre",
            "Because the salt stops dissolving once the water has been used up "
            "entirely",
            "Because no further salt can dissolve, so the mass per dm³ is at "
            "its maximum",
            "Because a saturated solution has the same concentration as the "
            "solid salt does",
        ],
        "correct_index": 2,
        "why": "Saturation means the solution already holds as much solute as "
               "it can at that temperature, which fixes the mass in each dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s24",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "50 cm³ of a solution is evaporated to dryness and 0.75 g of "
                "solid is left behind. Calculate the concentration of the "
                "original solution.",
        "options": [
            "0.015 g/dm³",
            "1.5 g/dm³",
            "37.5 g/dm³",
            "15 g/dm³",
        ],
        "correct_index": 3,
        "why": "All the solute is left behind, so the concentration is "
               "0.75 ÷ 0.050 = 15 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s25",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "6 g more solute is stirred into 500 cm³ of a solution already "
                "at 20 g/dm³, and the volume does not change. Determine the "
                "new concentration.",
        "options": [
            "26 g/dm³",
            "32 g/dm³",
            "12 g/dm³",
            "20 g/dm³",
        ],
        "correct_index": 1,
        "why": "The solution held 20 × 0.500 = 10 g, and 16 g in 0.500 dm³ is "
               "32 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-s26",
        "subtopic_slug": "concentration-of-solutions",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which change leaves a solution's concentration "
                "unchanged.",
        "options": [
            "Stirring more water into it",
            "Boiling some water off it",
            "Dissolving more solid in it",
            "Pouring half of the solution away down the sink",
        ],
        "correct_index": 3,
        "why": "Pouring some away removes solute and volume in the same "
               "proportion, so the mass of solute in each dm³ is untouched.",
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "ks4-concentration-of-solutions-h05",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "300 cm³ of a 40 g/dm³ solution is mixed with 200 cm³ of a "
                "15 g/dm³ solution of the same solute. Calculate the "
                "concentration of the mixture.",
        "options": [
            "55 g/dm³",
            "30 g/dm³",
            "27.5 g/dm³",
            "15 g/dm³",
        ],
        "correct_index": 1,
        "why": "The solutes add to 12 + 3 = 15 g in a total of 0.500 dm³, "
               "giving 30 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h06",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "500 cm³ of 20 g/dm³ solution is to be made by diluting a "
                "much stronger stock at 250 g/dm³. Calculate what volume of "
                "the stock should be measured out.",
        "options": [
            "10 cm³",
            "25 cm³",
            "40 cm³",
            "125 cm³",
        ],
        "correct_index": 2,
        "why": "500 cm³ at 20 g/dm³ needs 10 g of solute, and 10 ÷ 250 = "
               "0.040 dm³, which is 40 cm³ of stock.",
    },
    {
        "id": "ks4-concentration-of-solutions-h07",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution of concentration 100 g/dm³ is diluted tenfold, and "
                "the result is then diluted tenfold again. Determine the final "
                "concentration.",
        "options": [
            "10 g/dm³",
            "5 g/dm³",
            "0.1 g/dm³",
            "1 g/dm³",
        ],
        "correct_index": 3,
        "why": "Each tenfold dilution divides the concentration by ten, so "
               "100 becomes 10 and then 1 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h08",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "20 cm³ of a solution is evaporated to dryness and leaves "
                "0.36 g of solid. Determine the mass of solid in 1.5 dm³ of "
                "the same solution.",
        "options": [
            "0.54 g",
            "18 g",
            "27 g",
            "7.2 g",
        ],
        "correct_index": 2,
        "why": "The concentration is 0.36 ÷ 0.020 = 18 g/dm³, so 1.5 dm³ holds "
               "18 × 1.5 = 27 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-h09",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A 96 g/dm³ solution is made weaker by transferring 25 cm³ "
                "of it into a flask and making the contents up to 300 cm³. "
                "Calculate the resulting concentration.",
        "options": [
            "1152 g/dm³",
            "12 g/dm³",
            "24 g/dm³",
            "8 g/dm³",
        ],
        "correct_index": 3,
        "why": "The solute is 96 × 0.025 = 2.4 g, and 2.4 ÷ 0.300 = 8 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h10",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution holds 9.0 g of solute in 300 cm³. Determine the "
                "volume of water that must be evaporated off to raise the "
                "concentration to 45 g/dm³.",
        "options": [
            "200 cm³",
            "150 cm³",
            "100 cm³",
            "50 cm³",
        ],
        "correct_index": 2,
        "why": "9.0 g at 45 g/dm³ occupies 0.200 dm³, so 300 − 200 = 100 cm³ of "
               "water must go.",
    },
    {
        "id": "ks4-concentration-of-solutions-h11",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "One student dissolves 6 g of solid in 200 cm³ of water; "
                "another dissolves 6 g of the same solid and makes the "
                "solution up to 200 cm³. Determine whose concentration is "
                "known exactly.",
        "options": [
            "The first student's, because 200 cm³ was measured before "
            "anything dissolved",
            "The second student's, because the volume of solution is the "
                "200 cm³",
            "Both, because the same mass of solid was used each time",
            "Neither, without evaporating the water off first",
        ],
        "correct_index": 1,
        "why": "Concentration is per volume of solution, and only the second "
               "student knows that volume; adding solid to 200 cm³ of water "
               "gives slightly more than 200 cm³ of solution.",
    },
    {
        "id": "ks4-concentration-of-solutions-h12",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student reports a concentration of 0.048 g/dm³ for 12 g of "
                "solute in 250 cm³ of solution. Identify the error and give "
                "the correct value.",
        "options": [
            "The mass and volume were swapped over; it is 20.8 g/dm³",
            "The volume was used in cm³ rather than dm³; it is 48 g/dm³",
            "The mass should be in kilograms; it is 0.000048 g/dm³",
            "The answer needed multiplying by 100; it is 4.8 g/dm³",
        ],
        "correct_index": 1,
        "why": "12 ÷ 250 uses cm³; dividing by 0.250 dm³ gives 48 g/dm³, a "
               "thousand times larger.",
    },
    {
        "id": "ks4-concentration-of-solutions-h13",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "500 cm³ of a solution of concentration 32 g/dm³ is left "
                "uncovered and 100 cm³ of water evaporates. Calculate the new "
                "concentration.",
        "options": [
            "26 g/dm³",
            "32 g/dm³",
            "160 g/dm³",
            "40 g/dm³",
        ],
        "correct_index": 3,
        "why": "The 16 g of solute now fills 0.400 dm³, so the concentration is "
               "16 ÷ 0.400 = 40 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h14",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "50 cm³ of a stock solution of concentration 180 g/dm³ is "
                "diluted to 750 cm³. Determine the mass of solute in the whole "
                "of the diluted solution.",
        "options": [
            "135 g",
            "12 g",
            "9.0 g",
            "0.60 g",
        ],
        "correct_index": 2,
        "why": "Dilution adds no solute, so the diluted solution still holds "
               "180 × 0.050 = 9.0 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-h15",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student needs 250 cm³ of a 4.0 g/dm³ solution, but the "
                "balance cannot weigh less than 0.5 g reliably. Determine the "
                "best method.",
        "options": [
            "Weigh out 1.0 g anyway and accept the large uncertainty in it",
            "Weigh out 0.5 g and make it up to 250 cm³ as the method says",
            "Make a stronger solution from a larger mass, then dilute it",
            "Use a measuring cylinder instead, since volumes are easier to read",
        ],
        "correct_index": 2,
        "why": "Weighing 4.0 g and making 1 dm³, then taking 250 cm³, gives the "
               "same concentration from a mass the balance can handle well.",
    },
    {
        "id": "ks4-concentration-of-solutions-h16",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare the concentration of 3 g of salt in 100 cm³ of "
                "solution with that of 30 g of salt in 1 dm³.",
        "options": [
            "The first is ten times the second",
            "The second is ten times the first",
            "The second is three times the first",
            "They are equal, at 30 g/dm³ each",
        ],
        "correct_index": 3,
        "why": "3 ÷ 0.100 = 30 g/dm³ and 30 ÷ 1 = 30 g/dm³, so the two "
               "solutions are the same strength.",
    },
    {
        "id": "ks4-concentration-of-solutions-h17",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A solution has a concentration of 25 g/dm³. Determine the "
                "volume of it, in cm³, that contains 2.0 g of solute.",
        "options": [
            "80 cm³",
            "50 cm³",
            "12.5 cm³",
            "800 cm³",
        ],
        "correct_index": 0,
        "why": "2.0 ÷ 25 = 0.080 dm³, which is 80 cm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h18",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student mixes 400 cm³ of a 10 g/dm³ solution with 100 cm³ of "
                "pure water and says the concentration has halved. Evaluate "
                "this claim.",
        "options": [
            "Correct, because water was added to the solution",
            "Wrong: the 4.0 g of solute now fills 0.500 dm³, so it is 8 g/dm³",
            "Wrong: dissolved solid cannot have its concentration changed",
            "Correct, because a fifth of the total volume added was water",
        ],
        "correct_index": 1,
        "why": "The volume rose by a quarter, not by a half, so the "
               "concentration falls from 10 to 8 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h19",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine the concentration in g/dm³ of a solution made by "
                "dissolving 0.25 kg of solute in enough water to give 5.0 dm³ "
                "of solution.",
        "options": [
            "0.050 g/dm³",
            "20 g/dm³",
            "50 g/dm³",
            "1250 g/dm³",
        ],
        "correct_index": 2,
        "why": "0.25 kg is 250 g, so the concentration is "
               "250 ÷ 5.0 = 50 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h20",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "1.0 dm³ of water is added to 2.0 dm³ of a solution of "
                "concentration 45 g/dm³. Determine the mass of solute in "
                "500 cm³ of the diluted solution.",
        "options": [
            "22.5 g",
            "45 g",
            "7.5 g",
            "15 g",
        ],
        "correct_index": 3,
        "why": "The 90 g of solute now fills 3.0 dm³, giving 30 g/dm³, so "
               "0.500 dm³ holds 15 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-h21",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why doubling both the mass of solute and the volume "
                "of solution leaves the concentration unchanged.",
        "options": [
            "The mass cancels, because doubling it twice returns it to normal",
            "The volume cancels, because a doubled volume dilutes a doubled mass equally",
            "Two doublings undo each other only when the solute is the same substance",
            "Concentration is a ratio, and both parts of it have doubled",
        ],
        "correct_index": 3,
        "why": "Dividing twice the mass by twice the volume gives the same "
               "number of grams in every cubic decimetre.",
    },
    {
        "id": "ks4-concentration-of-solutions-h22",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "4.0 g of solute is dissolved to give 160 cm³ of solution. "
                "Determine the mass needed to make 2.0 dm³ of a solution of "
                "the same concentration.",
        "options": [
            "25 g",
            "50 g",
            "8.0 g",
            "320 g",
        ],
        "correct_index": 1,
        "why": "The concentration is 4.0 ÷ 0.160 = 25 g/dm³, so 2.0 dm³ needs "
               "25 × 2.0 = 50 g.",
    },
    {
        "id": "ks4-concentration-of-solutions-h23",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "125 cm³ is taken from a bottle labelled 80 g/dm³ and diluted "
                "to a total volume of 1.0 dm³. Determine the concentration of "
                "the diluted solution.",
        "options": [
            "6.4 g/dm³",
            "10 g/dm³",
            "80 g/dm³",
            "16 g/dm³",
        ],
        "correct_index": 1,
        "why": "The sample holds 80 × 0.125 = 10 g of solute, which in 1.0 dm³ "
               "is 10 g/dm³.",
    },
    {
        "id": "ks4-concentration-of-solutions-h24",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Determine which pair of solutions has the same concentration.",
        "options": [
            "4 g in 100 cm³ and 8 g in 400 cm³",
            "10 g in 250 cm³ and 20 g in 1000 cm³",
            "6 g in 200 cm³ and 15 g in 500 cm³",
            "5 g in 50 cm³ and 5 g in 500 cm³",
        ],
        "correct_index": 2,
        "why": "6 ÷ 0.200 and 15 ÷ 0.500 both come to 30 g/dm³; each of the "
               "other pairs differs by a factor of two or more.",
    },
    {
        "id": "ks4-concentration-of-solutions-h25",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "250 cm³ of sea water is evaporated to dryness and leaves "
                "8.75 g of dissolved salts. Determine the mass of salts in "
                "1.0 m³ of the same sea water, given that 1 m³ is 1000 dm³.",
        "options": [
            "8.75 kg",
            "35 kg",
            "350 kg",
            "3.5 kg",
        ],
        "correct_index": 1,
        "why": "The concentration is 8.75 ÷ 0.250 = 35 g/dm³, so 1000 dm³ holds "
               "35 000 g, which is 35 kg.",
    },
    {
        "id": "ks4-concentration-of-solutions-h26",
        "subtopic_slug": "concentration-of-solutions",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Evaluate this statement: 'A concentrated solution must contain "
                "more solute than a dilute one.'",
        "options": [
            "Correct, because concentrated means that more solute has been "
            "dissolved in it",
            "Correct, because a dilute solution holds hardly any solute at all",
            "Wrong, because a large volume of dilute solution can hold more "
            "solute",
            "Wrong, because concentrated and dilute describe the solvent and "
            "not the solute",
        ],
        "correct_index": 2,
        "why": "Concentration is solute per unit volume, so 10 dm³ at 5 g/dm³ "
               "holds 50 g while 100 cm³ at 200 g/dm³ holds only 20 g.",
    },
]
