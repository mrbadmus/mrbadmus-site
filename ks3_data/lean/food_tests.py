# -*- coding: utf-8 -*-
"""Food tests, in the lean shape. Spec table: docs/lessons/wave2/ks3-food-tests.md."""

LESSON = {
    "slug": "food-tests",
    "start": {
        "setup": "Two tubes hold the same milk and Benedict's solution, in one hot water bath. "
                 "Tube 1 is heated for five minutes and turns brick red. "
                 "Tube 2 is heated for thirty seconds and stays blue.",
        "question": "If you had to guess, what does tube 2 on its own tell you about the milk?",
        "options": [
            ("It has no sugar in it",
             "Tube 1 shows the milk does contain sugar. Tube 2 was not heated for long enough."),
            ("Nothing either way",
             "Right. Thirty seconds is too short for the test to work. So tube 2 proves nothing."),
        ],
        "answer": 1,
    },
    "words": ["food test", "reagent", "positive result", "emulsion"],
    "word_defs": {
        "food test": "A test that shows whether a food contains a particular nutrient.",
        "reagent": "A chemical you add in a test. It changes colour if the substance is there.",
        "positive result": "The colour change that shows the nutrient is there.",
        "emulsion": "A cloudy mixture of tiny drops of one liquid spread through another.",
    },
    "knowledge": [
        {"kind": "card", "title": "What a food test does",
         "body": ["A food test shows whether a nutrient is in a food.",
                  "You add a reagent to the food. If the nutrient is there, the colour changes.",
                  "That colour change is a positive result.",
                  "Each test finds one nutrient only."]},
        {"kind": "card", "title": "Getting the food ready",
         "body": ["Crush a solid food with a little water, using a pestle and mortar.",
                  "Let the bits settle, or filter it. Test the liquid.",
                  "Use a clean test tube and a fresh sample for each test."]},
        {"kind": "card", "title": "The four tests",
         "body": [{"figure": "b3-food-test-colours"}]},
        {"kind": "reveal", "title": "The four food tests",
         # two answer columns, not three: at 390 px a third column split "Orange-brown" before
         # its hyphen and left a comma alone on a line (Wave 2 walk, 24 Nov 2026)
         "cols": ["Reagent", "Colour change if positive"],
         "rows": [
             ("Starch", "Iodine solution", "Orange-brown to blue-black"),
             ("Sugar", "Benedict's solution, then heat",
              "Blue to green, yellow, orange or brick red"),
             ("Protein", "Biuret solution", "Blue to purple (lilac)"),
             ("Fat", "Ethanol, then pour into water", "Clear to cloudy white"),
         ]},
        {"kind": "card", "title": "Testing for starch",
         "body": ["Add a few drops of iodine solution to the food.",
                  "Iodine solution is orange-brown.",
                  "If starch is there, it turns blue-black. No heating is needed."]},
        {"kind": "card", "title": "Testing for sugar",
         "body": ["Add Benedict's solution to the food solution. It is blue.",
                  "Heat the tube in a hot water bath for about five minutes.",
                  "If sugar is there, it turns green, yellow, orange or brick red.",
                  "Without heating, Benedict's solution stays blue."]},
        {"kind": "card", "title": "Testing for protein",
         "body": ["Add Biuret solution to the food solution. It is blue.",
                  "If protein is there, it turns purple. Some books call this lilac.",
                  "No heating is needed."]},
        {"kind": "card", "title": "Testing for fat",
         "body": ["Shake the food with ethanol. Let it settle.",
                  "Pour the ethanol into a tube of water.",
                  "If fat is there, a cloudy white layer forms. This is an emulsion.",
                  "If there is no fat, the water stays clear."]},
        {"kind": "card", "title": "A negative result",
         "body": ["No colour change means the test did not detect the nutrient.",
                  "A small amount may still be there. It can be too little to show.",
                  "Potato is about 2% protein, but Biuret solution usually stays blue.",
                  "So write ‘protein was not detected’, and not ‘there is no protein’.",
                  "Chewed bread can test positive for sugar.",
                  "Saliva has broken some of the starch down into sugar."]},
        {"kind": "card", "title": "A test shows if, not exactly how much",
         "body": ["A food test shows whether a nutrient is there.",
                  "Benedict's colours give a rough idea of the amount of sugar.",
                  "Green means a little sugar. Brick red means a lot.",
                  "This only works if every tube is heated for the same time.",
                  "No food test measures exactly how much is there."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A darker colour always means more of the nutrient.",
              "The colour also depends on heating time and how much reagent you add.",
              "DIET-04"),
             ("No colour change proves the nutrient is not there.",
              "A small amount can be too little for the test to detect.", "DIET-05"),
             ("Benedict's solution works without heating.",
              "Benedict's solution must be heated in a hot water bath."),
             ("Iodine solution turns blue-black with sugar.",
              "Iodine solution turns blue-black with starch. Benedict's is the sugar test."),
         ]}]},
    ],
    "key_fact": "Starch turns iodine solution blue-black. Sugar turns heated Benedict's solution from "
                "blue to green, yellow, orange or brick red. Protein turns Biuret solution purple. Fat gives a cloudy white "
                "emulsion with ethanol and water.",
    "deeper": [
        {"kind": "card", "title": "Not every sugar shows up",
         "body": ["Benedict's solution finds sugars such as glucose.",
                  "Table sugar does not change its colour, even when heated.",
                  "Boil table sugar with a little acid first. It splits into glucose and another sugar.",
                  "Neutralise the acid, then add Benedict's solution.",
                  "Now it gives a positive result."]},
        {"kind": "card", "title": "Comparing amounts fairly",
         "body": ["To compare the sugar in two foods, keep everything else the same.",
                  "Use the same volumes, the same water bath and the same heating time.",
                  "Compare the colours with tubes that hold known amounts of sugar."]},
    ],
    "try": None,
    # "Connects to" notes in a plain voice (the authored ones were abstract, with dashes)
    "connects": {
        "Testing the model": "That lesson asks what a result can prove, but about a model, not a tube.",
    },
    "tutor_body": "Unsure what a negative result lets you write down?",
    "safety_note": "Wear eye protection. Biuret solution contains sodium hydroxide, which can harm "
                   "your eyes and skin. Ethanol catches fire easily, so keep it away from flames. "
                   "Never taste anything in the lab.",
    "ks4_becomes": "The food tests as a required practical, with the same reagents and colours.",
    "figures": [
        {"id": "b3-food-test-colours", "kind": "diagram", "status": "drawn", "art": "b3-food-test-colours",
         "title": "The four food tests, before and after",
         "desc": "Four rows, one for each test. Each row shows a test tube at its start colour, an arrow, "
                 "and the positive result. Starch, iodine solution: orange-brown turns blue-black, with "
                 "no heating. Sugar, Benedict's solution: blue turns green, yellow, orange or brick red, "
                 "after five minutes in a hot water bath; four tubes show those four colours. Protein, "
                 "Biuret solution: blue turns purple, with no heating. Fat, ethanol then water: clear "
                 "turns cloudy white.",
         "caption": "Each test finds one nutrient. The right-hand tubes show a positive result.",
         "data": {"rows": [
             {"nutrient": "Starch", "reagent": "iodine solution", "note": "No heating.",
              "start": {"name": "orange-brown", "colour": "#B4762A"},
              "positive": [{"colour": "#1B1B3A"}], "positive_name": "blue-black"},
             {"nutrient": "Sugar", "reagent": "Benedict's solution",
              "note": "Heat in a hot water bath for about 5 minutes.",
              "start": {"name": "blue", "colour": "#2E63B8"},
              "positive": [{"colour": "#5F9E3A"}, {"colour": "#E2C23A"}, {"colour": "#E07B24"},
                           {"colour": "#B03A16"}],
              "positive_name": "green, yellow, orange or brick red"},
             {"nutrient": "Protein", "reagent": "Biuret solution", "note": "No heating.",
              "start": {"name": "blue", "colour": "#3E7ACB"},
              "positive": [{"colour": "#7B4CA8"}], "positive_name": "purple"},
             {"nutrient": "Fat", "reagent": "ethanol, then water",
              "note": "Shake with ethanol, then pour into water.",
              "start": {"name": "clear", "colour": "#E6EEF0"},
              "positive": [{"colour": "#FAFAF5"}], "positive_name": "cloudy white", "cloudy": True},
         ]}},
    ],
    "ladder_stem": {
        "explain": "A group tests potato with Biuret solution. It stays blue. They write ‘potato "
                   "contains no protein’. Potato is about 2% protein. Explain what is wrong with their "
                   "conclusion. Write a better one. Say what you would change to detect the protein.",
        "produce": "A cereal bar says it is ‘protein-packed and sugar-free’. You have iodine, "
                   "Benedict's, ethanol and Biuret. Say which tests you would run. Say what result "
                   "would support each claim. Say which claim these tests could never fully check.",
    },
    "ladder_ticks": [
        ["Suggests a workable change — more concentrated sample, larger mass of potato in less "
         "water, or a more sensitive method.",
         "Suggests a change, such as crushing more potato in less water."],
        ["Does not claim the test was done wrongly; the method was followed correctly and still "
         "gave a false negative.",
         "Does not blame the method. A correct test can still miss a small amount."],
        ["States that a lilac Biuret result supports protein being present but not ‘packed’, "
         "because the test gives no amount.",
         "Says purple shows protein is there, but not how much."],
        ["Identifies ‘protein-packed’ as the claim that cannot be checked, since it is a quantity "
         "claim and these tests are qualitative.",
         "Says ‘protein-packed’ cannot be checked, as these tests do not measure exact amounts."],
        ["Notes that a blue Benedict’s does not prove sugar-free either — sucrose is not a reducing "
         "sugar and would not show up.",
         "Says a blue Benedict's result does not prove there is no sugar."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "The test shows fat is there. It does not measure how much.",
            1: "This test says nothing about protein. That needs the Biuret test.",
            3: "A food test shows a nutrient is there. It says nothing about health.",
        },
        "apply": {
            0: "The same iodine was used both times. The bread changed, not the reagent.",
            1: "Crushing food helps a test work. It cannot make sugar appear.",
            3: "Iodine still detects starch in solution. Some starch has been turned into sugar.",
        },
    },
}
