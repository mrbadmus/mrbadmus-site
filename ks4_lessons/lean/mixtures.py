# -*- coding: utf-8 -*-
"""Mixtures and separation techniques, in the lean shape. Spec table: ks4-mixtures.md (AQA 8464
5.1.1.2 / 8462 4.1.1.2, word for word the same; no HT-only or Chemistry-only lines; AT 4).

LEGACY (batch 3). The ladder (Ks4Ladder, four rungs, Rung 2 differs for Higher and Foundation) and
the practice set stay from the Design page. The practice set is the route's subtopic `quiz` list
(K.bank, the same items on all four routes), so its fixes and its two new items are quiz-data edits
in all_subtopics_chemistry*.py (patches/_subtopic_edits_a.json), not here. The eyebrow is bound per
route by the page's own logic (specRef 5.1.1.2 / 4.1.1.2).

logic_edits:
  1. Rung 1 (meaning of mixture): the credited option was the longest of the four (67 characters
     against 61, 57 and 61). Two distractors are reworded, same meaning, so it no longer is.
  2. Rung 3 (ethanol from water): links 2 and 3 could be swapped and still read. Link 3 now starts
     from the failure of simple distillation ("So a fractionating column is used instead"), so the
     chain has one order.
"""

LOGIC_EDITS = [
    ("{ text: 'Two or more elements chemically combined in fixed proportions', correct: false,",
     "{ text: 'Two or more elements that are chemically combined in fixed proportions', correct: false,"),
    ("{ text: 'One substance that contains only one type of atom throughout', correct: false,",
     "{ text: 'One substance that contains only one type of atom all the way through', correct: false,"),
    ("'In the column the vapour condenses and boils again many times, so ethanol, with the lower "
     "boiling point, reaches the top first and is collected first.'",
     "'So a fractionating column is used instead: ethanol, with the lower boiling point, reaches the "
     "top first and is collected first.'"),
]

LESSON = {
    "slug": "mixtures",
    "start": {
        "setup": "Sugar is stirred into hot water. The crystals disappear, but the water tastes sweet.",
        "question": "If you had to guess, is it still sugar in the water, or something new?",
        "options": [
            ("Still sugar",
             "It is still sugar, spread through the water. Evaporate the water and the sugar comes "
             "back unchanged."),
            ("Something new",
             "It is still sugar, spread through the water. Evaporate the water and the sugar comes "
             "back unchanged."),
        ],
        "answer": 0,
    },
    "words": ["mixture", "physical process", "filtrate", "distillate"],
    "knowledge": [
        {"kind": "card", "title": "What a mixture is",
         "body": ["A mixture consists of two or more elements or compounds not chemically combined "
                  "together.",
                  "The chemical properties of each substance in the mixture are unchanged.",
                  "Mixtures can be separated by physical processes: filtration, crystallisation, "
                  "simple distillation, fractional distillation and chromatography. These do not "
                  "involve chemical reactions, and no new substances are made."]},
        {"kind": "reveal", "title": "Choosing a method",
         "cols": ["What it separates", "Example"],
         "rows": [
             ("Filtration", "An insoluble solid from a liquid", "Sand from water"),
             ("Crys\u00adtal\u00adli\u00adsa\u00adtion", "A dissolved solid from its solution",
              "Copper sulfate crystals from copper sulfate solution"),
             ("Simple distillation", "A liquid from a solution", "Pure water from salt water"),
             ("Fractional distillation", "Liquids that mix, with different boiling points",
              "Ethanol from water"),
             ("Chro\u00adma\u00adtog\u00adra\u00adphy", "Dissolved substances from each other", "The dyes in ink"),
         ]},
        {"kind": "card", "title": "Filtration",
         "body": [{"slot": "fig:mix-filtration"},
                  "The filter paper holds back the insoluble solid, called the residue. The liquid "
                  "that runs through is the filtrate.",
                  "A dissolved solid passes through the paper with the water."]},
        {"kind": "card", "title": "Crystallisation",
         "body": [{"slot": "fig:mix-crystallisation"},
                  "Heat the solution in an evaporating basin so that some of the water evaporates. "
                  "Leave it to cool, and crystals form. Filter off the crystals and dry them."]},
        {"kind": "card", "title": "Simple distillation",
         "body": [{"slot": "fig:mix-simple-distillation"},
                  "Heat the solution. The water boils, and its vapour is cooled in the condenser. It "
                  "condenses back to a liquid, the distillate. The dissolved salt stays in the flask."]},
        {"kind": "card", "title": "Fractional distillation",
         "body": [{"slot": "fig:mix-fractional-distillation"},
                  "This separates liquids that mix and have different boiling points.",
                  "The vapour rises up the fractionating column. The liquid with the lowest boiling "
                  "point reaches the top first and is collected first. Ethanol boils at 78 °C and "
                  "water at 100 °C, so ethanol is collected first."]},
        {"kind": "card", "title": "Chromatography",
         "body": [{"slot": "fig:chromatogram"},
                  "Chromatography separates dissolved substances, such as the dyes in ink. Each "
                  "substance moves a different distance up the paper, so they separate into spots. "
                  "Rf = distance moved by substance ÷ distance moved by solvent. In the diagram, "
                  "Rf = 3.6 ÷ 8.0 = 0.45."]},
        {"kind": "card", "title": "A soluble solid mixed with sand",
         "body": ["To get pure, dry copper sulfate crystals from copper sulfate mixed with sand:",
                  {"points": [
                      "1. Add water and stir, so the copper sulfate dissolves.",
                      "2. Filter. The sand stays on the paper as the residue.",
                      "3. Heat the filtrate to evaporate some of the water, then leave it to cool so "
                      "crystals form.",
                      "4. Filter off the crystals and dry them between filter papers.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A fine enough filter paper catches dissolved salt.",
              "Dissolved substances pass through any filter paper. Crystallise to get the salt back."),
             ("Evaporating salt water collects the water.",
              "The water escapes into the air. Distil it to collect the water."),
             ("Separating a mixture makes new substances.",
              "Physical processes make no new substances. Each substance comes back unchanged."),
         ]}]},
    ],
    "key_fact": "A mixture is two or more elements or compounds that are not chemically combined, so "
                "each substance keeps its own chemical properties. Physical processes, such as "
                "filtration, crystallisation, distillation and chromatography, separate a mixture "
                "without making any new substances.",
    "deeper": [
        {"kind": "card", "title": "Setting up a distillation",
         "body": [{"points": [
             "The thermometer bulb sits level with the side arm, so it reads the temperature of the "
             "vapour that is being collected.",
             "Cold water goes into the condenser at the bottom and out at the top, so the condenser "
             "stays full of cold water.",
             "Anti-bumping granules in the flask make the liquid boil smoothly.",
         ]}]},
        {"kind": "card", "title": "Why not boil it dry",
         "body": ["Boiling a solution until it is dry can make it spit, and leaves a powder instead "
                  "of crystals. Evaporate only some of the water, then let it cool."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Suggest</strong>: use the information you are given, such as boiling points, "
             "to choose a method.",
             "<strong>Plan</strong>: the steps in order, the apparatus, and what you end up with.",
             "<strong>Explain</strong>: name the property that is different, then say what it lets "
             "you collect.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
}
