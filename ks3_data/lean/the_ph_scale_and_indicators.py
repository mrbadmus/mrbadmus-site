# -*- coding: utf-8 -*-
"""The pH scale and indicators, in the lean shape.
Spec table: docs/lessons/wave2/ks3-the-ph-scale-and-indicators.md.

Rainford 18c (making an indicator) and 19c (identify the pH) have no page of their own and
are taught here. Universal indicator bands are the same as in acids-and-alkalis.
"""

_BANDS = [
    {"from": 0, "to": 2, "colour": "red", "means": "strongly acidic"},
    {"from": 3, "to": 6, "colour": "orange or yellow", "means": "weakly acidic"},
    {"from": 7, "to": 7, "colour": "green", "means": "neutral"},
    {"from": 8, "to": 10, "colour": "blue", "means": "weakly alkaline"},
    {"from": 11, "to": 14, "colour": "purple", "means": "strongly alkaline"},
]

LESSON = {
    "slug": "the-ph-scale-and-indicators",
    "start": {
        "setup": "Red cabbage is soaked in hot water, and the purple water is kept. "
                 "A few drops go into six different clear liquids. "
                 "It turns red, pink, purple, blue, green or yellow.",
        "question": "If you had to guess, would juice squeezed from blackberries change colour "
                    "like this too, or only the cabbage water?",
        "options": [
            ("Blackberry juice would too",
             "Right. Blackberries hold the same kind of dye as red cabbage. It is an indicator too."),
            ("Only the cabbage water",
             "Blackberries hold the same kind of dye. It changes colour in acids and alkalis too."),
        ],
        "answer": 0,
    },
    "words": ["indicator", "litmus", "universal indicator", "pH scale"],
    "word_defs": {
        "indicator": "A dye that changes colour in acids and alkalis.",
        "litmus": "An indicator that turns red in acid and blue in alkali.",
        "universal indicator": "A mixture of dyes. Its colour shows the pH of a solution.",
        "pH scale": "A scale from 0 to 14 that shows how acidic or alkaline a solution is.",
    },
    "knowledge": [
        {"kind": "card", "title": "What an indicator does",
         "body": ["An indicator is a dye that changes colour in acids and alkalis.",
                  "Many acids and alkalis look just like water.",
                  "An indicator shows which is which."]},
        {"kind": "card", "title": "Litmus",
         "body": ["Litmus is red in an acid and blue in an alkali.",
                  "Blue litmus paper turns red in acid. Red litmus paper turns blue in alkali.",
                  "In a neutral solution, neither paper changes colour.",
                  "Litmus shows only whether a solution is acidic or alkaline."]},
        {"kind": "card", "title": "Universal indicator",
         "body": ["Universal indicator is a mixture of dyes.",
                  "It turns a different colour across the whole pH scale.",
                  "You match its colour to a chart to read the pH.",
                  {"figure": "c6-ph-scale-colours"},
                  "So universal indicator shows how strongly acidic or alkaline a solution is.",
                  "Litmus cannot show that."]},
        {"kind": "reveal", "title": "Universal indicator colours",
         "cols": ["Colour", "What it tells you"],
         "rows": [
             ("pH 0 to 2", "Red", "Strongly acidic"),
             ("pH 3 to 6", "Orange or yellow", "Weakly acidic"),
             ("pH 7", "Green", "Neutral"),
             ("pH 8 to 10", "Blue", "Weakly alkaline"),
             ("pH 11 to 14", "Purple", "Strongly alkaline"),
         ]},
        {"kind": "card", "title": "The pH scale",
         "body": ["The pH scale runs from 0 to 14.",
                  "Below 7 is acidic. 7 is neutral. Above 7 is alkaline.",
                  "The lower the pH, the more acidic the solution.",
                  "The higher the pH, the more alkaline the solution.",
                  "Each step of 1 down the scale is ten times more acidic.",
                  "So pH 3 is 10 times more acidic than pH 4.",
                  "And pH 2 is 100 times more acidic than pH 4."]},
        {"kind": "reveal", "title": "Litmus or universal indicator",
         "cols": ["Litmus", "Universal indicator"],
         "rows": [
             ("In an acid", "Red", "Red, orange or yellow"),
             ("In a neutral solution", "No change", "Green"),
             ("In an alkali", "Blue", "Blue or purple"),
             ("Gives a pH number", "No", "Yes"),
         ]},
        {"kind": "card", "title": "Finding the pH of a solution",
         "body": [{"points": ["Put a little of the solution in a test tube or a spotting tile.",
                              "Add two or three drops of universal indicator.",
                              "Or dip a strip of universal indicator paper into it.",
                              "Match the colour to the pH chart. Write down the pH.",
                              "Rinse the dropper before the next sample."]},
                  "Adding more indicator makes the colour deeper. It does not change the pH.",
                  "A pH meter measures pH with a probe. It gives a more precise reading."]},
        {"kind": "card", "title": "Making a red cabbage indicator",
         "body": [{"points": ["Chop some red cabbage into small pieces.",
                              "Cover it with hot water and leave it for ten minutes. Stir it.",
                              "Filter or strain the liquid. It is purple.",
                              "Add a few drops to each solution you want to test."]},
                  {"figure": "c6-cabbage-colours"},
                  "In acid, red cabbage indicator turns red or pink.",
                  "When neutral, it is purple.",
                  "In alkali, it turns blue, green or yellow.",
                  "Many coloured plants hold the same kind of dye, such as blackberries and beetroot."]},
        {"kind": "card", "title": "Why pH is measured",
         "body": [{"points": ["Gardeners and farmers test soil. Different plants grow best at different pH.",
                              "To test soil, shake it with distilled water. Let it settle, then test the liquid.",
                              "Lime is added to soil that is too acidic.",
                              "Fish farmers keep pond water close to neutral.",
                              "Tooth enamel starts to dissolve below about pH 5.5."]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("pH 2 is twice as acidic as pH 4.",
              "Each step is ten times. pH 2 is 100 times more acidic than pH 4.", "ACID-03"),
             ("Adding more indicator changes the pH.",
              "More indicator only makes the colour deeper. The pH stays the same.", "ACID-04"),
             ("Litmus can tell you the pH number.",
              "Litmus shows only acid or alkali. Universal indicator gives the pH."),
             ("A higher pH means a solution is more acidic.",
              "A lower pH means more acidic. A higher pH means more alkaline."),
         ]}]},
    ],
    "key_fact": "Universal indicator changes colour across the whole pH scale, so it gives the pH "
                "number. Below 7 is acidic, 7 is neutral and above 7 is alkaline. Litmus shows "
                "only acid or alkali.",
    "deeper": [
        {"kind": "card", "title": "Indicators from plants",
         "body": ["Litmus comes from lichens, which grow on rocks and walls.",
                  "Hydrangea flower colour depends on the pH of the soil.",
                  "Hydrangeas flower blue in acidic soil and pink in alkaline soil."]},
        {"kind": "card", "title": "pH meters",
         "body": ["Many labs measure pH with a pH meter instead of by eye.",
                  "A probe goes into the solution. The meter shows the pH as a number.",
                  "It can read to one or two decimal places.",
                  "It gives the same reading for anyone, including people who are colour blind."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why each step on the scale is ten times?",
    "safety_note": "Wear eye protection. Some solutions you test may be corrosive. Test a few "
                   "drops in a tube or on a tile, never in the bottle. Take care with hot water "
                   "when you make the cabbage indicator.",
    "ks4_becomes": "pH as a measure of hydrogen ion concentration, why each step is a factor of "
                   "ten, and choosing an indicator for a titration.",
    "figures": [
        {"id": "c6-ph-scale-colours", "kind": "diagram", "status": "drawn", "art": "c6-ph-bands",
         "title": "Universal indicator colours on the pH scale",
         "desc": "Fifteen coloured cells in a row, numbered 0 to 14. Acidic is written above the "
                 "left end, neutral above 7 and alkaline above the right end. Brackets under the "
                 "numbers group them into five bands. A key below: pH 0 to 2 red, strongly acidic. "
                 "pH 3 to 6 orange or yellow, weakly acidic. pH 7 green, neutral. pH 8 to 10 blue, "
                 "weakly alkaline. pH 11 to 14 purple, strongly alkaline.",
         "caption": "Match the colour to the chart, then read the pH number.",
         "data": {"bands": _BANDS}},
        {"id": "c6-cabbage-colours", "kind": "diagram", "status": "drawn",
         "art": "c6-cabbage-colours",
         "title": "Red cabbage indicator in six solutions",
         "desc": "Six test tubes in a row, from most acidic on the left to most alkaline on the "
                 "right. The liquids are red, pink, purple, blue, green and yellow, and each colour "
                 "is named under its tube. A bracket groups red and pink as acid, purple alone as "
                 "neutral, and blue, green and yellow as alkali. An arrow runs from more acidic to "
                 "more alkaline.",
         "caption": "Red cabbage indicator in acid, neutral and alkaline solutions.",
         "data": {"tubes": [{"colour": "red", "hex": "#C62839"},
                            {"colour": "pink", "hex": "#E07AA6"},
                            {"colour": "purple", "hex": "#7E4FA0"},
                            {"colour": "blue", "hex": "#3F6FC2"},
                            {"colour": "green", "hex": "#4E9A5A"},
                            {"colour": "yellow", "hex": "#E3CB3C"}],
                  "groups": [{"label": "acid", "first": 0, "last": 1},
                             {"label": "neutral", "first": 2, "last": 2},
                             {"label": "alkali", "first": 3, "last": 5}]}},
    ],
    "ladder_ticks": [
        ["Says an out-of-range result tells the gardener what to add — lime for acid soil.",
         "Says an acidic result tells the gardener to add lime."],
        ["Notes that pH alone does not settle it — how long the drink stays on the teeth matters too.",
         "Says pH is not the whole story. How long the drink stays on teeth matters too."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Both indicators need a solution. Dissolve a solid in water before you test it.",
            1: "Neither indicator measures danger. Universal indicator shows the pH.",
            3: "Both indicators change back if the solution changes. Neither colour is permanent.",
        },
        "apply": {
            0: "Neutral is one point, pH 7. A solution cannot be more neutral than that.",
            1: "The colour stayed green, so the pH is still 7. It has not become alkaline.",
            2: "Adding indicator does not concentrate the solution. Only the colour changes.",
        },
    },
}
