# -*- coding: utf-8 -*-
"""Transfer of biomass, in the lean shape. Spec table: ks4-transfer-of-biomass.md.

Legacy lesson (batch 10). The ladder and the practice set stay from the live page; the
logic_edits below fix the faults the audit found (see the table's audit section).
"""

LESSON = {
    "slug": "transfer-of-biomass",
    "start": {
        "setup": "A rabbit eats 1000 g of grass.",
        "question": "If you had to guess, how much of that grass becomes new rabbit?",
        "options": [
            ("About 900 g",
             "About 100 g. Most of the grass leaves as faeces, or is lost in respiration and "
             "in urine."),
            ("About 100 g",
             "About 100 g. Most of the grass leaves as faeces, or is lost in respiration and "
             "in urine."),
        ],
        "answer": 1,
    },
    "words": ["biomass", "trophic level", "efficiency", "egested"],
    "knowledge": [
        {"kind": "card", "title": "Light into producers",
         "body": ["Producers are mostly plants and algae.",
                  "They transfer about 1% of the incident energy from light for photosynthesis."]},
        {"kind": "card", "title": "About 10% is passed on",
         "body": ["Only approximately 10% of the biomass from each trophic level is transferred "
                  "to the level above it.",
                  {"slot": "fig:rabbit-biomass-losses"}]},
        {"kind": "card", "title": "Where the rest goes",
         "body": [{"points": [
                      "Not all the ingested material is absorbed. Some is egested as faeces.",
                      "Some absorbed material is lost as waste: carbon dioxide and water in "
                      "respiration, and water and urea in urine.",
                      "Large amounts of glucose are used in respiration.",
                  ]},
                  "Only the biomass that becomes part of the animal's body can pass to the next "
                  "trophic level."]},
        {"kind": "reveal", "title": "Egested and excreted",
         "cols": ["Egested or excreted", "Why"],
         "rows": [("Faeces", "Egested", "It was eaten but never absorbed."),
                  ("Carbon dioxide from respiration", "Excreted", "It is waste made in the body."),
                  ("Urea in urine", "Excreted", "It is waste made in the body.")]},
        {"kind": "card", "title": "Efficiency of biomass transfer",
         "body": ["efficiency = biomass at the next level ÷ biomass at this level",
                  "Give the answer as a fraction, or multiply by 100 for a percentage.",
                  "Both biomasses must be in the same unit before you divide.",
                  "An answer over 100% means you divided the wrong way round.",
                  {"slot": "triangle:EQ_BIO"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Pyramids of biomass",
         "body": ["A pyramid of biomass represents the relative amount of biomass in each "
                  "trophic level of a food chain. Trophic level 1 is at the bottom.",
                  "Only about 10% is passed on each time, so each trophic level has less "
                  "biomass than the level below it."]},
        {"kind": "card", "title": "Fewer organisms higher up",
         "body": ["Less biomass can support fewer organisms. So there are usually fewer organisms "
                  "at each level going up a food chain.",
                  "After a few transfers, too little biomass is left to support another level. "
                  "So food chains rarely have more than four or five trophic levels."]},
        {"kind": "card", "title": "Eating lower down the chain",
         "body": ["Grain eaten by people is one transfer. Grain fed to cattle, then beef eaten by "
                  "people, is two transfers.",
                  "Two transfers pass on about 10% of 10%, which is 1%.",
                  "So eating the grain passes about ten times more biomass to people."]},
        {"kind": "card", "title": "Farm animals",
         "body": ["Farmers limit how much their animals move and keep them warm.",
                  "Less of the animals' food is used in respiration, so more of it becomes body "
                  "mass."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Biomass is lost as heat.",
              "Energy is lost as heat. Biomass leaves as faeces, carbon dioxide, water and urea."),
             ("Faeces are excreted.",
              "Faeces are egested. They were never absorbed."),
             ("4000 g/m² ÷ 320 g/m² × 100 = 1250%",
              "Divide the next level by this level: 320 ÷ 4000 × 100 = 8%."),
             ("Two transfers of 10% pass on 20%.",
              "Multiply them: 10% of 10% is 1%."),
         ]}]},
    ],
    "key_fact": "Only about 10% of the biomass at one trophic level is transferred to the level "
                "above. The rest is egested as faeces, or lost as carbon dioxide and water in "
                "respiration and as water and urea in urine.",
    "deeper": [
        {"kind": "card", "title": "Two transfers in a row",
         "body": ["Work out each efficiency. Then multiply them to find the share that reaches "
                  "the top.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: work out the efficiency, as a percentage or a "
             "fraction, and show each line.",
             "<strong>Describe</strong>: say what happens, using the 1% and the 10%.",
             "<strong>Explain</strong>: say how biomass is lost, and how that affects the number "
             "of organisms at each level.",
         ]}]},
    ],
    "try": None,
    "equations": {
        # The same equation as the legacy page's EQ_E, so the triangle can sit in a card.
        "EQ_BIO": {"name": "Efficiency of biomass transfer",
                   "written": "efficiency = biomass at the next level ÷ biomass at this level",
                   "source": "none",
                   "top": {"s": "B₂", "name": "biomass at the next level",
                           "unit": "g/m², kg/m² or kg (same unit for both)"},
                   "bottom": [{"s": "E", "name": "efficiency (as a decimal)",
                               "unit": "× 100 for %"},
                              {"s": "B₁", "name": "biomass at this level",
                               "unit": "g/m², kg/m² or kg (same unit for both)"}]},
    },
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # cfQuestions Q3: the "close" line was garbled.
            ("'1500 ÷ 12 = 125 divides; the next level is efficiency (as a decimal) × this level.'",
             "'Do not divide by 12. Next level = efficiency as a decimal × this level = 0.12 × 1500.'"),
            # Ladder r4 level text: no "spec" talk on a pupil page.
            ("'All three losses in the spec’s words, the 10% figure, and the effect on numbers and chain length.'",
             "'All three losses, the 10% figure, and the effect on numbers and chain length.'"),
            # Practice set item 1 (stem kept, so its id is kept): the credited option was the
            # longest by 70 characters, options carried dash tails, two distractors were arguable.
            ('"Less movement means less energy used in respiration for muscle activity — more energy retained as body mass (biomass for humans to eat)"',
             '"Less of the food is respired, so more becomes body mass"'),
            ('"Restricted movement prevents disease spreading between animals"',
             '"It stops diseases spreading from one animal to another"'),
            ('"Animals that move less eat less food — reducing farming costs"',
             '"The animals take in more oxygen, so they grow faster"'),
            ('"Restricted movement makes animals heavier due to water retention"',
             '"Their bodies hold more water, so they weigh more"'),
            ('"Disease prevention may be a concern but is not the reason for restricting movement in the context of energy efficiency."',
             '"Crowded animals spread disease more easily, not less. The reason is less respiration."'),
            ('"Animals that move less may eat slightly less, but the key reason is that energy from food is retained as BIOMASS rather than used in movement."',
             '"Moving less does not mean taking in more oxygen. Less of the food is used in respiration."'),
            ('"Body mass increase is due to biomass accumulation — not water retention. The mechanism is reduced respiration for movement."',
             '"The extra mass is body mass, not water. Less of the food is used in respiration."'),
            # Practice set item 4: the credited option carried its working, so it was the longest.
            ("'1%: 10% of 10%'", "'1%'"),
            # Practice set item 5 (stem kept): credited option 113 characters against 18 to 41;
            # "leaves most of the rabbit uneaten" is a real loss, so it was arguable.
            ("'Some is egested as faeces; some is lost as carbon dioxide and water in respiration and as urea and water in urine'",
             "'Egested as faeces, and lost in respiration and urine'"),
            ("['It is lost as heat', 'Energy is lost as heat; biomass leaves as substances.']",
             "['It is all turned into heat as the fox runs about', 'Energy is lost as heat. Biomass leaves as faeces, carbon dioxide, water and urea.']"),
            ("['The fox leaves most of the rabbit uneaten', 'A fox eats most of a rabbit. The main losses are inside the fox: faeces, respiration, urine.']",
             "['The fox gains more biomass than the rabbit it eats', 'Only about 10% of what the fox eats becomes fox.']"),
            ("['No biomass is lost', 'Only about 10% is passed on.']",
             "['None is lost: all of the rabbit’s biomass becomes fox', 'Only about 10% is passed on.']"),
        ],
        # The first worked example: same numbers as the live page, written the way the other
        # two examples and the ladder write the equation (the old one said "current level",
        # had a dash tail and an Insert line that inserted nothing).
        "cfifa_first": {
            "tab": "Matching units", "eq": "EQ_E", "find": "E",
            "next": "Now one with a unit to convert.",
            "head": "Grass has a biomass of 2000 g/m². Rabbits eating this grass have a biomass "
                    "of 160 g/m². Calculate the efficiency of transfer as a percentage.",
            "steps": [
                ["C", "Convert", "Nothing to convert: both are in g/m²."],
                ["F", "Formula", "efficiency = biomass at the next level ÷ biomass at this "
                                 "level, × 100"],
                ["I", "Insert", "efficiency = 160 ÷ 2000 × 100"],
                ["F", "Fine-tune", "efficiency = 0.08 × 100 = 8"],
                ["A", "Answer", "8%"],
            ]},
    },
}
