# -*- coding: utf-8 -*-
"""Farming techniques, in the lean shape. Spec table: ks4-farming-techniques.md.

Legacy lesson (batch 10). The ladder and the practice set stay from the live page; the
logic_edits below fix the faults the audit found (see the table's audit section).
"""

LESSON = {
    "slug": "farming-techniques",
    "start": {
        "setup": "Two chickens get the same feed. One lives in a warm shed with little room. "
                 "The other runs about outside.",
        "question": "If you had to guess, which one gains more body mass?",
        "options": [
            ("The chicken outside",
             "The chicken in the shed. It moves less and loses less heat, so less of its feed "
             "is used in respiration."),
            ("The chicken in the shed",
             "The chicken in the shed. It moves less and loses less heat, so less of its feed "
             "is used in respiration."),
        ],
        "answer": 1,
    },
    "words": ["intensive farming", "efficiency", "respiration", "ethical objection"],
    "knowledge": [
        {"kind": "card", "title": "Making food production more efficient",
         "body": ["The efficiency of food production can be improved by restricting energy "
                  "transfer from food animals to the environment.",
                  "Less of the animals' food is then used in respiration, so more of it becomes "
                  "body mass. That means more meat from the same feed."]},
        {"kind": "reveal", "title": "Two ways to cut energy transfer",
         "cols": ["What the farmer does", "Why more feed becomes body mass"],
         "rows": [("Limiting movement",
                   "Keeps the animals in pens or cages with little room",
                   "Less muscle activity, so less glucose is used in respiration"),
                  ("Controlling the temperature",
                   "Keeps the animals in a warm shed",
                   "Less energy is transferred to the surroundings as heat, so less glucose is "
                   "used in respiration to keep warm")]},
        {"kind": "card", "title": "High-protein food",
         "body": ["Some animals are fed high-protein foods to increase growth."]},
        {"kind": "card", "title": "Intensive farming",
         "body": ["Farming like this is called intensive farming, or factory farming.",
                  "Examples are chickens kept in sheds and pigs kept indoors in pens."]},
        {"kind": "reveal", "title": "Intensive farming: for and against",
         "cols": ["Point"],
         "rows": [("Advantage", "More meat from the same amount of feed"),
                  ("Advantage", "Less feed for each kilogram of meat, so the meat is cheaper"),
                  ("Disadvantage", "The animals cannot behave naturally. Some people have "
                                   "ethical objections to this."),
                  ("Disadvantage", "Disease spreads quickly between animals kept close "
                                   "together")]},
        {"kind": "card", "title": "Disease and antibiotics",
         "body": ["Pathogens spread quickly when many animals are kept close together.",
                  "Farmers may use antibiotics to control the disease. Antibiotics kill "
                  "bacteria, not viruses.",
                  "Using antibiotics a lot helps antibiotic-resistant bacteria to develop. So "
                  "the agricultural use of antibiotics should be restricted."]},
        {"kind": "card", "title": "Evaluating a farming method",
         "body": [{"points": [
             "Give the advantages, using any numbers you are given.",
             "Give the disadvantages: welfare, ethical objections, disease and antibiotics.",
             "Finish with a judgement that weighs one side against the other.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Penned animals grow because they are lazy.",
              "They move less, so less of their food is used in respiration."),
             ("Animals in a warm shed eat more, so they grow more.",
              "The feed is the same. Less of it is used in respiration to keep warm."),
             ("Antibiotics kill the viruses that spread on farms.",
              "Antibiotics kill bacteria, not viruses."),
         ]}]},
    ],
    "key_fact": "Limiting animals' movement and controlling the temperature of their surroundings "
                "restricts energy transfer to the environment. Less of their food is used in "
                "respiration, so more becomes body mass. Some people have ethical objections to "
                "these intensive methods.",
    "deeper": [
        {"kind": "card", "title": "Link to transfer of biomass",
         "body": ["Only about 10% of the biomass at one trophic level reaches the next.",
                  "Cutting the energy an animal transfers to the surroundings raises the share "
                  "of its feed that becomes meat."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: say how limiting movement or controlling temperature "
             "means less respiration and more body mass.",
             "<strong>Evaluate</strong>: give advantages and disadvantages from the "
             "information, then a judgement.",
             "<strong>Describe</strong>: say what the ethical objections are.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Ladder r1 Q1 reply: no "spec" talk on a pupil page.
            ("'The spec’s two are movement and temperature.'",
             "'The two ways are limiting movement and controlling temperature.'"),
            # Ladder r2 Q1: credited option 90 characters against 31 and 32.
            ("'Less energy is used to keep its body temperature up, so more of the feed becomes body mass'",
             "'It respires less to keep warm, so more feed becomes body mass'"),
            ("['It eats more because it is bored', 'The feed is the same.']",
             "['It eats a lot more food, because it is bored in the warm shed', 'The feed is the same.']"),
            ("['The shed air is more nutritious', 'Air is not food.']",
             "['The warm air in the shed gives it extra nutrients for growth', 'Air is not food.']"),
            # Ladder r2 Q2: credited option 64 characters against 20 and 33.
            ("'Crowded birds cannot behave naturally and disease spreads faster'",
             "'The birds are crowded, so disease spreads faster'"),
            ("['It gives less meat per kg of feed', 'It gives more: 2 kg against 1.3 kg.']",
             "['It gives less meat from each kilogram of feed', 'It gives more: 2 kg against 1.3 kg.']"),
            ("['It is more expensive', 'Less feed per kg of meat makes it cheaper.']",
             "['The birds move about more, so they respire more', 'Shed birds have little room, so they move less.']"),
            # Practice set item 1 (stem kept, so its id is kept): credited option 136
            # characters with "psychological suffering"; dash tails; egg quality, water use
            # and greenhouse gases are all arguable objections.
            ('"Intensively farmed chickens cannot exhibit natural behaviours and are kept in conditions that cause physical and psychological suffering"',
             '"The chickens cannot behave naturally in crowded sheds"'),
            ('"Intensively farmed chickens produce lower-quality eggs — ethical concern about food standards"',
             '"The chickens have too much space to move about in the shed"'),
            ('"Intensive farming uses more water than free-range farming — wasteful of resources"',
             '"The chickens are kept much too cold during the winter"'),
            ('"Intensive farming produces more greenhouse gases than other methods"',
             '"The meat from the chickens costs a lot more to buy"'),
            ('"Egg quality varies by diet and conditions, but the PRIMARY ethical objection is about ANIMAL WELFARE — inability to move, spread wings or behave naturally."',
             '"Intensive sheds are crowded. Each chicken has little space."'),
            ('"Water use may be a concern but is not the primary ethical objection to intensive farming."',
             '"Intensive sheds are kept warm all year."'),
            ('"Greenhouse gas emissions are an environmental concern — the ethical objection specifically is about animal welfare and suffering."',
             '"Intensive farming makes meat cheaper, not dearer."'),
            # Practice set item 2 (stem kept): credited option 117 characters against 19 to 40.
            ("'Less energy is used to keep their body temperature up, so less is lost as heat and more of the feed becomes body mass'",
             "'They respire less to keep warm, so more feed becomes body mass'"),
            ("['The heat makes the pigs eat more', 'The feed is the same; less of it is respired.']",
             "['The heat makes the pigs eat a lot more of their food each day', 'The feed is the same; less of it is respired.']"),
            ("['The pigs grow because heat is a nutrient', 'Heat is not a nutrient.']",
             "['Heat acts as a nutrient that helps the pigs to grow bigger', 'Heat is not a nutrient.']"),
            ("['Warm pigs move more', 'Warm, enclosed pigs move less and lose less heat.']",
             "['Warm pigs move about more, so they build up more muscle mass', 'Warm, enclosed pigs move less and lose less heat.']"),
            # Practice set item 4 (stem kept): credited option 127 characters against 28 to 35.
            ("'Shed cattle are more efficient, but crowding spreads disease and more antibiotic use drives resistance, so there is a real cost'",
             "'Shed cattle use less feed per kg, but need more antibiotics'"),
            ("['Shed cattle are better in every way', 'Disease and antibiotic use are disadvantages.']",
             "['Shed cattle are better in every way, with no downside', 'Disease and antibiotic use are disadvantages.']"),
            ("['Field cattle are more efficient', '9 kg of feed per kg is less efficient than 6 kg.']",
             "['Field cattle gain more mass from each kg of feed', '9 kg of feed per kg is less efficient than 6 kg.']"),
            ("['Antibiotics have no downside', 'Agricultural antibiotic use should be restricted because of resistance.']",
             "['Antibiotic use has no downside, so the shed is best', 'Agricultural antibiotic use should be restricted because of resistance.']"),
            # Practice set item 5 (stem kept): credited option 67 characters against 24 to 38;
            # "grow too fast" is arguable (antibiotics have been used as growth promoters).
            ("'Routine use drives the development of antibiotic-resistant bacteria'",
             "'To slow the development of resistant bacteria'"),
            ("['Antibiotics make animals grow too fast', 'The concern is resistance.']",
             "['Antibiotics are a source of protein for animals', 'Antibiotics are medicines, not food. The concern is resistance.']"),
            ("['Antibiotics kill viruses', 'They do not; and that is not the reason.']",
             "['Antibiotics would kill all the viruses on farms', 'Antibiotics do not kill viruses.']"),
            ("['Antibiotics are too cheap', 'Cost is not the reason; resistance is.']",
             "['Antibiotics make the meat taste worse', 'Taste is not the reason; resistance is.']"),
            # Examiner MUST FIX r1.1 (why some people object): the credited option was far the longest.
            ("['The meat is cheaper', 'That is an advantage.'], ['The animals grow faster', 'That is the aim, not the objection.']",
             "['The meat is cheaper to buy in shops', 'That is an advantage.'], ['The animals grow faster on less feed', 'That is the aim, not the objection.']"),
        ],
    },
}
