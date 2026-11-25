# -*- coding: utf-8 -*-
"""Acids and alkalis, in the lean shape. Spec table: docs/lessons/wave2/ks3-acids-and-alkalis.md.

Universal indicator bands are the same in all three C6 lane A lessons: pH 0 to 2 red,
3 to 6 orange or yellow, 7 green, 8 to 10 blue, 11 to 14 purple.
"""

_BANDS = [
    {"from": 0, "to": 2, "colour": "red", "means": "strongly acidic"},
    {"from": 3, "to": 6, "colour": "orange or yellow", "means": "weakly acidic"},
    {"from": 7, "to": 7, "colour": "green", "means": "neutral"},
    {"from": 8, "to": 10, "colour": "blue", "means": "weakly alkaline"},
    {"from": 11, "to": 14, "colour": "purple", "means": "strongly alkaline"},
]

LESSON = {
    "slug": "acids-and-alkalis",
    "start": {
        "setup": "Two clear, colourless liquids have lost their labels. One is an acid. "
                 "The other is an alkali.",
        "question": "If you had to guess, which would show you which one is the acid: "
                    "weighing each, or adding a few drops of a dye?",
        "options": [
            ("Weigh each one",
             "An acid is not always heavier than an alkali. Weighing cannot show which is which."),
            ("Add a dye",
             "Right. A dye called an indicator turns one colour in acid and another in alkali."),
        ],
        "answer": 1,
    },
    "words": ["acid", "alkali", "base", "neutral"],
    "word_defs": {
        "acid": "A substance that dissolves in water to make a solution with a pH below 7.",
        "alkali": "A base that dissolves in water. Its solution has a pH above 7.",
        "base": "A substance that neutralises an acid.",
        "neutral": "Neither acidic nor alkaline. A neutral solution has a pH of exactly 7.",
    },
    "knowledge": [
        {"kind": "card", "title": "Acids",
         "body": ["An acid dissolves in water to make a solution with a pH below 7.",
                  "Vinegar, orange juice and lemon juice contain acids.",
                  "Your stomach makes hydrochloric acid.",
                  "In the lab you use hydrochloric acid, sulfuric acid and nitric acid."]},
        {"kind": "card", "title": "Alkalis and bases",
         "body": ["A base is a substance that neutralises an acid.",
                  "An alkali is a base that dissolves in water.",
                  "Alkalis make solutions with a pH above 7.",
                  "Sodium hydroxide and calcium hydroxide are alkalis.",
                  "When an acid and an alkali react, they cancel each other out. This is neutralisation.",
                  "Gardeners spread lime (calcium hydroxide) on soil that is too acidic.",
                  "Too much lime would make the soil alkaline."]},
        {"kind": "card", "title": "Neutral",
         "body": ["A neutral substance is neither acidic nor alkaline.",
                  "Its pH is exactly 7.",
                  "Pure water is neutral. So is salt (sodium chloride) dissolved in water."]},
        {"kind": "card", "title": "The pH scale",
         "body": ["The pH scale runs from 0 to 14.",
                  "Below 7 is acidic. 7 is neutral. Above 7 is alkaline.",
                  "The further the pH is from 7, the more strongly acidic or alkaline it is.",
                  "Universal indicator turns a different colour for each part of the scale.",
                  {"figure": "c6-ph-scale-acids"}]},
        {"kind": "reveal", "title": "Acid, alkali or neutral",
         "cols": ["Acid, alkali or neutral", "pH (about)"],
         "rows": [
             ("Dilute hydrochloric acid", "Acid", "1"),
             ("Vinegar", "Acid", "3"),
             ("Orange juice", "Acid", "4"),
             ("Pure water", "Neutral", "7"),
             ("Salt dissolved in water", "Neutral", "7"),
             ("Baking soda in water", "Alkali", "8"),
             ("Bleach", "Alkali", "12"),
             ("Oven cleaner", "Alkali", "13"),
         ]},
        {"kind": "card", "title": "Hazards",
         "body": ["Being an acid or an alkali does not tell you how dangerous something is.",
                  "Orange juice is weakly acidic. It is safe to drink.",
                  "Oven cleaner contains sodium hydroxide. It is strongly alkaline and burns skin.",
                  "Strong alkalis are as dangerous as strong acids. Both are corrosive.",
                  "Corrosive means it destroys skin, eyes and other materials.",
                  "Alkalis feel soapy and may not sting at first.",
                  "So wash any splash off at once, with lots of cold water."]},
        {"kind": "card", "title": "Concentrated and dilute",
         "body": ["A concentrated acid has a lot of acid in a small volume of water.",
                  "Adding water makes the acid dilute.",
                  "A dilute acid is still an acid. Its pH is still below 7.",
                  "Diluting moves the pH closer to 7, but never past it.",
                  "A dilute acid is less harmful, but it can still hurt your eyes."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Only acids are dangerous. Alkalis are safe to handle.",
              "Strong alkalis are corrosive too, such as sodium hydroxide in oven cleaner.",
              "ACID-01"),
             ("A dilute acid is no longer an acid.",
              "A dilute acid is still an acid. Its pH is still below 7.", "ACID-02"),
             ("Every base is an alkali.",
              "Only a base that dissolves in water is an alkali."),
             ("You can tell an acid from an alkali by looking at it.",
              "Many look like water. You need an indicator to tell them apart."),
         ]}]},
    ],
    "key_fact": "Acids have a pH below 7. Alkalis have a pH above 7. Neutral is exactly 7. "
                "A base neutralises an acid, and an alkali is a base that dissolves in water.",
    "deeper": [
        {"kind": "card", "title": "Bases that do not dissolve",
         "body": ["Copper oxide and zinc oxide neutralise acids.",
                  "So they are bases.",
                  "They do not dissolve in water, so they are not alkalis.",
                  "To use one, you warm the acid and stir in the solid powder."]},
        {"kind": "card", "title": "Metal and non-metal oxides",
         "body": ["Many metal oxides are bases. Some dissolve in water to make alkalis.",
                  "Many non-metal oxides dissolve in water to make acids.",
                  "Carbon dioxide and sulfur dioxide are non-metal oxides.",
                  "Sulfur dioxide in the air helps make acid rain."]},
    ],
    "try": None,
    "tutor_body": "Still unsure why a base is not always an alkali?",
    "safety_note": "Wear eye protection. Strong acids and strong alkalis are corrosive. "
                   "A strong alkali may not hurt at first, so wash any splash off at once with "
                   "plenty of water. Test a few drops, never the whole bottle. Never taste or "
                   "touch anything in the lab.",
    # the classic heading "Next in this unit" named lessons that are not next (Unit 3 walk)
    "connects_heading": None,
    "ks4_becomes": "Acids as sources of hydrogen ions (H⁺) and alkalis as sources of "
                   "hydroxide ions (OH⁻), and the difference between strong and "
                   "concentrated acids.",
    "figures": [
        {"id": "c6-ph-scale-acids", "kind": "diagram", "status": "drawn", "art": "c6-ph-bands",
         "title": "The pH scale with universal indicator colours",
         "desc": "Fifteen coloured cells in a row, numbered 0 to 14. Acidic is written above the "
                 "left end, neutral above 7 and alkaline above the right end. Brackets under the "
                 "numbers group them into five bands. A key below: pH 0 to 2 red, strongly acidic. "
                 "pH 3 to 6 orange or yellow, weakly acidic. pH 7 green, neutral. pH 8 to 10 blue, "
                 "weakly alkaline. pH 11 to 14 purple, strongly alkaline.",
         "caption": "Below 7 is acidic, 7 is neutral and above 7 is alkaline.",
         "data": {"bands": _BANDS}},
    ],
    "ladder_stem": {
        "explain": "You have two unlabelled colourless liquids. One is an acid and one is an "
                   "alkali. Explain how you would find out which is which. Say why looking at "
                   "them cannot tell you.",
        "produce": "A gardener's soil is too acidic for the crop they want to grow. Explain what "
                   "they should add and why it works. Say what could go wrong if they add far "
                   "too much.",
    },
    "ladder_feedback": {
        "recall": {
            1: "That describes an acid. An alkali has a pH above 7.",
            2: "A base that does not dissolve is not an alkali. Alkalis are above 7.",
            3: "A pH of exactly 7 is neutral. An alkali has a pH above 7.",
        },
        "apply": {
            0: "Orange juice is an acid. It contains citric acid and has a pH below 7.",
            2: "Not every acid is dangerous. Weakly acidic orange juice is safe to drink.",
            3: "Orange juice has a pH below 7, so it is acidic, not neutral.",
        },
    },
}
