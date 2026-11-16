# -*- coding: utf-8 -*-
"""The role of biotechnology, in the lean shape. Spec table: ks4-role-of-biotechnology.md.

Legacy lesson (batch 10). The ladder and the practice set stay from the live page; the
logic_edits below fix the faults the audit found (see the table's audit section).
"""

LESSON = {
    "slug": "role-of-biotechnology",
    "start": {
        "setup": "A meat-free nugget is made from mycoprotein.",
        "question": "If you had to guess, what living thing is mycoprotein made from?",
        "options": [
            ("A plant",
             "A fungus. It is called Fusarium, and it is grown in big tanks on glucose syrup."),
            ("A fungus",
             "A fungus. It is called Fusarium, and it is grown in big tanks on glucose syrup."),
        ],
        "answer": 1,
    },
    "words": ["biotechnology", "mycoprotein", "Fusarium", "genetically modified (GM)"],
    "knowledge": [
        {"kind": "card", "title": "Feeding a growing population",
         "body": ["The human population is growing, so more food is needed.",
                  "Biotechnology and genetic modification (GM) are possible solutions.",
                  "Modern biotechnology techniques enable large quantities of microorganisms to "
                  "be cultured for food."]},
        {"kind": "card", "title": "Mycoprotein",
         "body": ["The fungus <em>Fusarium</em> is useful for producing mycoprotein, a "
                  "protein-rich food suitable for vegetarians.",
                  {"slot": "fig:mycoprotein-fermenter"},
                  {"points": [
                      "The fungus is grown on glucose syrup in a large tank called a fermenter.",
                      "Air is bubbled through, so the conditions are aerobic.",
                      "The fungal biomass is harvested and purified.",
                  ]}]},
        {"kind": "card", "title": "Human insulin",
         "body": ["A genetically modified bacterium produces human insulin. When harvested and "
                  "purified, this is used to treat people with diabetes.",
                  {"slot": "fig:insulin-gm-bacteria"},
                  {"points": [
                      "The human gene for insulin is inserted into a bacterium.",
                      "The GM bacteria are grown in a fermenter. They multiply and make human "
                      "insulin.",
                      "The insulin is harvested and purified.",
                  ]}]},
        {"kind": "card", "title": "GM crops",
         "body": ["GM crops could provide more food, or food with an improved nutritional value, "
                  "such as golden rice.",
                  "Golden rice has genes that make it produce beta-carotene. The body turns "
                  "beta-carotene into vitamin A.",
                  "In some regions a lack of vitamin A causes blindness in children.",
                  "Other GM crops resist insect attack or herbicides. GM crops generally show "
                  "increased yields."]},
        {"kind": "card", "title": "Concerns about GM crops",
         "body": [{"points": [
             "The effect on populations of wild flowers and insects. For example, a gene for "
             "herbicide resistance could spread in pollen to wild plants, making weeds that "
             "are hard to kill.",
             "Some people feel the effects of eating GM crops on human health have not been "
             "fully explored.",
             "Some people have ethical objections to genetic modification.",
         ]}]},
        {"kind": "card", "title": "Evaluating a GM crop",
         "body": [{"points": [
             "State the benefit, using any information you are given.",
             "State the concerns and the objections.",
             "Finish with a judgement that weighs the benefit against the risks.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Mycoprotein is made from soya.",
              "Mycoprotein is made from the fungus Fusarium."),
             ("Fusarium is grown without oxygen.",
              "It is grown in aerobic conditions."),
             ("Insulin for diabetes is made by Fusarium.",
              "Human insulin is made by a GM bacterium."),
         ]}]},
    ],
    "key_fact": "The fungus Fusarium is grown on glucose syrup in aerobic conditions, then "
                "harvested and purified, to make mycoprotein. A GM bacterium produces human "
                "insulin to treat diabetes, and GM crops such as golden rice could provide more "
                "food or food with better nutritional value.",
    "deeper": [
        {"kind": "card", "title": "Inside the fermenter",
         "body": ["The fermenter is sterilised before use, so only Fusarium grows in it.",
                  "The temperature, the pH and the oxygen supply are monitored and kept at the "
                  "best levels for growth."]},
        {"kind": "card", "title": "Why mycoprotein is efficient",
         "body": ["Fusarium does not move or keep itself warm. So it turns more of its food into "
                  "biomass than cattle do (see Transfer of biomass)."]},
        {"kind": "card", "title": "How the gene is moved", "routes": ["TH"],
         "body": [{"points": [
             "Enzymes are used to isolate the required gene.",
             "The gene is inserted into a vector, usually a bacterial plasmid or a virus.",
             "The vector is used to insert the gene into the required cells.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: give the steps in order, for mycoprotein or insulin.",
             "<strong>Explain</strong>: say how a method could help feed more people.",
             "<strong>Evaluate</strong>: weigh the benefit of a GM crop against the concerns, "
             "then judge.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-10",
        "logic_edits": [
            # Ladder r2 Q1: credited option 71 characters against 32 and 39.
            ("'A genetically modified bacterium makes it; it is harvested and purified'",
             "'A GM bacterium makes it; it is harvested and purified'"),
            ("['Fusarium makes it in aerobic conditions', 'Fusarium makes mycoprotein.']",
             "['Fusarium makes it in aerobic conditions in a fermenter', 'Fusarium makes mycoprotein.']"),
            ("['It is extracted from golden rice', 'Golden rice makes beta-carotene.']",
             "['It is extracted from the grains of golden rice', 'Golden rice makes beta-carotene.']"),
            # Ladder r2 Q2: credited option 111 characters against 21 and 26.
            ("'A protein-rich food can be made quickly in fermenters from glucose syrup, without the losses of feeding animals'",
             "'Large amounts of protein-rich food are made in fermenters'"),
            ("['It replaces all crops', 'It is one food among many.']",
             "['It means that no crops will ever need to be grown again', 'It is one food among many.']"),
            ("['It is made from waste meat', 'It is a fungus grown on glucose syrup.']",
             "['It is made cheaply from the waste meat left over on farms', 'It is a fungus grown on glucose syrup.']"),
            # Practice set item 1 (stem kept, so its id is kept): dash tails; credited option
            # the longest by 25+ characters; feedback named a species the lesson never teaches.
            ('"The fungus Fusarium — grown in industrial fermenters and processed into a high-protein meat substitute"',
             '"The fungus Fusarium"'),
            ('"Modified soya beans — a GM plant engineered to have higher protein content"',
             '"Soya beans, a plant"'),
            ('"A type of algae grown in open-air ponds using sunlight"',
             '"Algae grown in ponds"'),
            ('"Yeast — the same organism used in bread-making and brewing"',
             '"Yeast used to make bread"'),
            ('"Soya is used as a protein source but is not mycoprotein — mycoprotein specifically refers to Fusarium fungus protein."',
             '"Soya is a plant used in other meat substitutes. Mycoprotein comes from the fungus Fusarium."'),
            ('"Quorn uses a fungus (Fusarium venenatum), not algae — though algae-based proteins are being developed as future food sources."',
             '"Mycoprotein is made from a fungus, not from algae."'),
            ('"Yeast is also a fungus used in food production, but Quorn/mycoprotein is specifically from Fusarium venenatum, not yeast."',
             '"Yeast is a fungus, but mycoprotein is made from the fungus Fusarium."'),
            # Practice set item 2 (stem kept): credited option 146 characters with dash tails;
            # "absorb more herbicide" is arguable (residues are a real question). Blind doubt
            # TF-2 (MED): the key now uses AQA's own concern wording ("the effect on populations
            # of wild flowers and insects", 4.6.2.4, linked from 4.7.5.4) instead of gene flow to
            # weeds; "take over wild habitats" was close to that concern, so it is replaced.
            ('"GM herbicide-resistance genes could spread to wild plant relatives via pollen — creating herbicide-resistant \'superweeds\' that are hard to control"',
             '"They could affect populations of wild flowers and insects"'),
            ('"Herbicide-resistant crops absorb more herbicide into their tissues — making the food more toxic"',
             '"The crops cannot be eaten by people or by any animals"'),
            ('"The crops grow too fast and take over natural habitats"',
             '"The crops give people extra vitamin A in their daily diet"'),
            ('"Herbicide-resistant crops produce less yield than normal crops"',
             '"The crops give a smaller yield than ordinary crops"'),
            ('"Herbicide residues in food are a separate, regulated question. The environmental concern is about GENE FLOW to wild plants."',
             '"GM crops are grown as food. The concern is the effect on wild flowers and insects."'),
            ('"GM herbicide-resistant crops do not inherently grow faster or invade habitats — the specific concern is gene flow via pollen."',
             '"That is what golden rice does, and it is a benefit, not a concern."'),
            ('"GM crops are developed specifically to MAINTAIN or INCREASE yield — not reduce it."',
             '"GM crops generally show increased yields."'),
            # Practice set item 3 (stem kept): credited option 95 characters against 31 to 40.
            ("'Fusarium is grown on glucose syrup in aerobic conditions; the biomass is harvested and purified'",
             "'Fusarium grows aerobically on glucose syrup; it is harvested and purified'"),
            ("['Soya beans are crushed and shaped', 'Mycoprotein is a fungus, not soya.']",
             "['Soya beans are crushed, heated and pressed into shaped meat-free pieces', 'Mycoprotein is a fungus, not soya.']"),
            ("['Fusarium is grown without oxygen on meat', 'Aerobic conditions, on glucose syrup.']",
             "['Fusarium is grown on meat without any oxygen, then it is dried and cut up', 'It is grown in aerobic conditions, on glucose syrup.']"),
            ("['Bacteria make it in a fermenter', 'Bacteria make insulin; a fungus makes mycoprotein.']",
             "['Bacteria are grown in a fermenter on meat, then harvested and purified', 'Bacteria make insulin; a fungus makes mycoprotein.']"),
            # Practice set item 4 (stem kept): credited option 85 characters against 28 to 40.
            ("'A genetically modified bacterium makes human insulin, which is harvested and purified'",
             "'A GM bacterium makes it, then it is harvested and purified'"),
            ("['It is extracted from the fungus Fusarium', 'Fusarium makes mycoprotein.']",
             "['It is extracted from the fungus Fusarium in a fermenter', 'Fusarium makes mycoprotein.']"),
            ("['It is taken from golden rice', 'Golden rice makes beta-carotene.']",
             "['It is taken from the grains of golden rice plants', 'Golden rice makes beta-carotene.']"),
            ("['It is made by selective breeding of pigs', 'A GM bacterium carries the human gene.']",
             "['It is made by selectively breeding pigs and cattle', 'A GM bacterium carries the human gene.']"),
            # Practice set item 5 (stem kept): credited option 73 characters against 16 to 21.
            ("'Improved nutritional value: it makes beta-carotene, a source of vitamin A'",
             "'Improved nutritional value'"),
            ("['A bigger harvest', 'Golden rice is about nutrition, not yield.']",
             "['A bigger harvest of rice', 'Golden rice is about nutrition, not yield.']"),
            ("['Resistance to insects', 'That is a different GM trait.']",
             "['Resistance to insect pests', 'That is a different GM trait.']"),
            ("['It makes insulin', 'Insulin comes from a GM bacterium.']",
             "['It makes human insulin', 'Insulin comes from a GM bacterium.']"),
            # Examiner MUST FIX r1.1 (what the fungus is grown on): the credited option was three times
            # the length of the distractors.
            ("['Glucose syrup', ['Meat', 'No animal is involved.'], ['Soil', 'It grows in a fermenter.']]",
             "['Glucose syrup', ['Waste meat', 'No animal is involved.'], ['Garden soil', 'It grows in a fermenter, not in soil.']]"),
            # Examiner NOTE r4.0 point 5: "certain" overstated the benefit of golden rice.
            ("preventing blindness is a large, certain benefit against uncertain risks",
             "preventing blindness is a large benefit against uncertain risks"),
        ],
    },
}
