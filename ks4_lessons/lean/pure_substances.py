# -*- coding: utf-8 -*-
"""Pure substances, in the lean shape. New record, no legacy page (it replaces the old
generate_site_v5 page). Spec table: ks4-pure-substances.md (AQA 8464 5.8.1.1 / 8462 4.8.1.1, word
for word the same; no HT-only or chemistry-only lines). Every route gets the same lesson.

The practice set reads the route's `quiz` list (K.bank): quiz-pure-substances.json, five per route,
both old stems kept."""

LESSON = {
    "slug": "pure-substances",
    "start": {
        "setup": "A carton of orange juice says “100% pure” on the front.",
        "question": "If you had to guess, is the juice a pure substance in chemistry?",
        "options": [
            ("Yes",
             "No. It is a mixture of water, sugars, acids and many other compounds. In chemistry, "
             "a pure substance is a single element or compound."),
            ("No",
             "No. It is a mixture of water, sugars, acids and many other compounds. In chemistry, "
             "a pure substance is a single element or compound."),
        ],
        "answer": 1,
    },
    "words": ["pure substance", "mixture", "melting point", "boiling point"],
    "knowledge": [
        {"kind": "card", "title": "Pure in chemistry",
         "body": ["In chemistry, a pure substance is a single element or compound, not mixed with "
                  "any other substance.",
                  {"points": [
                      "Oxygen gas is a pure element.",
                      "Distilled water is a pure compound: it is only water.",
                      "Sea water is a mixture: water with salts dissolved in it.",
                  ]}]},
        {"kind": "card", "title": "Pure in everyday language",
         "body": ["In everyday language, a pure substance can mean a substance that has had nothing "
                  "added to it, so it is unadulterated and in its natural state, for example pure "
                  "milk.",
                  "Pure milk is still a mixture of water, fats, proteins and sugars. In chemistry, "
                  "it is not a pure substance."]},
        {"kind": "card", "title": "Melting and boiling points",
         "body": ["Pure elements and compounds melt and boil at specific temperatures.",
                  {"points": [
                      "Pure water melts at 0\u00a0°C and boils at 100\u00a0°C.",
                      "A mixture melts and boils over a range of temperatures.",
                  ]},
                  "So melting point and boiling point data can be used to distinguish pure "
                  "substances from mixtures."]},
        {"kind": "reveal", "title": "Pure substance or mixture",
         "cols": ["Pure substance", "Mixture"],
         "rows": [
             ("What it contains", "One element or one compound",
              "Two or more substances, not chemically combined"),
             ("How it melts", "At a specific temperature", "Over a range of temperatures"),
             ("How it boils", "At a specific temperature", "Over a range of temperatures"),
             ("Example", "Distilled water", "Sea water"),
         ]},
        {"kind": "card", "title": "Using melting point data",
         "body": ["Compare the melting point you measure with the melting point of the pure "
                  "substance.",
                  "Pure compound X melts at 122\u00a0°C. Two samples are tested.",
                  {"points": [
                      "Sample A melts at 122\u00a0°C. It is pure X.",
                      "Sample B melts from 115\u00a0°C to 119\u00a0°C. It melts over a range, so "
                      "it is impure: a mixture.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Natural means pure.",
              "In chemistry, pure means a single element or compound. Natural orange juice is a "
              "mixture."),
             ("Mixing two pure substances gives a pure substance.",
              "Mixing two substances gives a mixture."),
             ("A pure substance melts over a range of temperatures.",
              "A pure substance melts at a specific temperature. A mixture melts over a range."),
         ]}]},
    ],
    "key_fact": "In chemistry, a pure substance is a single element or compound, not mixed with any "
                "other substance. Pure elements and compounds melt and boil at specific "
                "temperatures, so melting point and boiling point data can be used to tell pure "
                "substances from mixtures.",
    "deeper": [
        {"kind": "card", "title": "Impurities and melting point",
         "body": ["An impurity usually lowers the melting point of a substance and makes it melt "
                  "over a range of temperatures.",
                  "An impurity usually raises the boiling point."]},
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Chromatography gives another test: a pure compound gives a single spot in every "
                  "solvent.",
                  "Formulations are mixtures made on purpose, as useful products."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Use the data</strong>: compare the measured melting or boiling point with "
             "the value for the pure substance.",
             "<strong>Explain</strong>: say whether it melts at one specific temperature or over a "
             "range, and what that shows.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Define", "marks": 1,
             "prompt": "Define a pure substance in chemistry.",
             "why": "In chemistry, a pure substance is a single element or compound, not mixed with "
                    "any other substance.",
             "options": [
                 {"text": "A natural substance that has had nothing added to it at all",
                  "correct": False,
                  "reply": "That is the everyday meaning. In chemistry, it means a single element "
                           "or compound."},
                 {"text": "A single element or compound, not mixed with any other substance",
                  "correct": True},
                 {"text": "Any mixture of elements that has been filtered to remove solids",
                  "correct": False,
                  "reply": "A filtered mixture is still a mixture."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State how a pure substance melts.",
             "why": "Pure elements and compounds melt at a specific temperature.",
             "options": [
                 {"text": "Over a range of temperatures", "correct": False,
                  "reply": "That is how a mixture melts."},
                 {"text": "At a specific temperature", "correct": True},
                 {"text": "At any temperature above 0\u00a0°C", "correct": False,
                  "reply": "Each pure substance has its own melting point. 0\u00a0°C is the "
                           "melting point of water."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Use", "marks": 2,
             "prompt": "Pure compound Y melts at 81\u00a0°C. Sample P melts at 81\u00a0°C. Sample Q "
                       "melts from 74\u00a0°C to 78\u00a0°C. Which statement is correct?",
             "why": "P melts at the specific melting point of Y, so it is pure Y. Q melts over a "
                    "range, so it is impure.",
             "options": [
                 {"text": "P is pure Y, and Q is impure", "correct": True},
                 {"text": "Q is pure Y, and P is impure", "correct": False,
                  "reply": "This is the wrong way round. A pure substance melts at one specific "
                           "temperature."},
                 {"text": "Both are pure, because both melt", "correct": False,
                  "reply": "Every solid melts if it is hot enough. Q melts over a range, so it is "
                           "a mixture."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A shop sells “pure honey”. Explain why a chemist would not call it "
                       "a pure substance.",
             "why": "Honey is a mixture of several compounds, such as sugars and water. A pure "
                    "substance is a single element or compound.",
             "options": [
                 {"text": "Honey is natural, and natural things are never pure substances",
                  "correct": False,
                  "reply": "Natural is not the test. Oxygen in the air is natural, and oxygen is a "
                           "pure element."},
                 {"text": "Honey is a mixture of several compounds, such as sugars and water",
                  "correct": True},
                 {"text": "Honey is a single compound that has been made by bees",
                  "correct": False,
                  "reply": "Honey contains several compounds, so it is a mixture."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Pure compound Z melts at 136\u00a0°C. A student heats a white solid that is "
                       "thought to be Z. It starts to melt at 128\u00a0°C and has all melted at "
                       "133\u00a0°C. Explain what her results show. Put the links in order.",
             "links": ["The solid starts to melt at 128\u00a0°C and has all melted at 133\u00a0°C.",
                       "So it melts over a range of temperatures, not at one specific temperature.",
                       "So the solid is a mixture: it is not pure Z."],
             "herrings": [{"text": "The solid melts at 136\u00a0°C, so it is pure Z.",
                           "why": "It melts from 128\u00a0°C to 133\u00a0°C, never at 136\u00a0°C."},
                          {"text": "Melting over a range shows that the solid is pure.",
                           "why": "A pure substance melts at one specific temperature."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A colourless liquid is thought to be pure water. Explain how its boiling "
                       "point shows whether it is pure. Put the links in order.",
             "links": ["Heat the liquid and measure the temperature at which it boils.",
                       "Compare it with the boiling point of pure water, 100\u00a0°C.",
                       "If it boils at 100\u00a0°C it is pure water; if it boils over a range of "
                       "temperatures it is a mixture."],
             "herrings": [{"text": "It is colourless, so it must be pure water.",
                           "why": "Many mixtures, such as salt water, are colourless."},
                          {"text": "Pure water boils over a range of temperatures.",
                           "why": "A pure substance boils at a specific temperature."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Two bottles are labelled “pure water”. One holds distilled water. "
                       "The other holds spring water, which has minerals dissolved in it. Explain "
                       "which one is a pure substance in chemistry, and how boiling point data "
                       "could show this.",
             "points": ["In chemistry, a pure substance is a single element or compound, not mixed "
                        "with any other substance.",
                        "Distilled water is only water, so it is a pure substance.",
                        "Spring water has minerals dissolved in it, so it is a mixture.",
                        "Pure water boils at a specific temperature, 100\u00a0°C.",
                        "The spring water boils over a range of temperatures, not at exactly "
                        "100\u00a0°C."],
             "reject": ["“Spring water is purer because it is natural.” Natural does not "
                        "mean pure in chemistry.",
                        "“Both are pure, because the labels say so.” The labels use the "
                        "everyday meaning."]},
        ],
    },
}
