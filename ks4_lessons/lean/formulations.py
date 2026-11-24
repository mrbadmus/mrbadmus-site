# -*- coding: utf-8 -*-
"""Formulations, in the lean shape. New record, no legacy page (it replaces the old generate_site_v5
page). Spec table: ks4-formulations.md (AQA 8464 5.8.1.2 / 8462 4.8.1.2, word for word the same; no
HT-only or chemistry-only lines). Every route gets the same lesson.

The spec says pupils do not need the names of components in proprietary products, so no brand and
no named additive appears. The practice set reads the route's `quiz` list (K.bank):
quiz-formulations.json, five per route, both old stems kept."""

LESSON = {
    "slug": "formulations",
    "start": {
        "setup": "Paint, a medicine tablet and sea water are all mixtures.",
        "question": "If you had to guess, which one is not a formulation?",
        "options": [
            ("Sea water",
             "Sea water. Nobody designed it. A formulation is a mixture designed as a useful "
             "product, made by mixing measured amounts of each part."),
            ("The medicine tablet",
             "Sea water. Nobody designed it. A formulation is a mixture designed as a useful "
             "product, made by mixing measured amounts of each part."),
        ],
        "answer": 0,
    },
    "words": ["formulation", "mixture", "component", "measured quantities"],
    "knowledge": [
        {"kind": "card", "title": "What a formulation is",
         "body": ["A formulation is a mixture that has been designed as a useful product.",
                  "Many products are complex mixtures in which each chemical has a particular "
                  "purpose. Each chemical in the mixture is called a component."]},
        {"kind": "card", "title": "Carefully measured quantities",
         "body": ["Formulations are made by mixing the components in carefully measured "
                  "quantities. This makes sure that the product has the required properties.",
                  "Change the amounts and the properties change. A tablet with too little of its "
                  "drug does not work. A tablet with too much can be harmful."]},
        {"kind": "card", "title": "Examples",
         "body": ["Formulations include fuels, cleaning agents, paints, medicines, alloys, "
                  "fertilisers and foods.",
                  {"points": [
                      "<strong>Paint</strong>: one component gives the colour, one keeps the "
                      "paint runny, one sticks the colour to the wall.",
                      "<strong>Medicine tablet</strong>: the drug, plus components that hold the "
                      "tablet together.",
                      "<strong>Alloy</strong>: steel is iron mixed with measured amounts of "
                      "carbon and other elements, to make it strong and hard.",
                      "<strong>Fertiliser</strong>: measured amounts of compounds that give "
                      "plants nitrogen, phosphorus and potassium.",
                  ]}]},
        {"kind": "card", "title": "Identifying a formulation",
         "body": ["Use the information you are given. A product is a formulation when:",
                  {"points": [
                      "it is a mixture;",
                      "it was designed as a useful product;",
                      "each component is there in a measured amount, for a purpose.",
                  ]}]},
        {"kind": "reveal", "title": "Formulation or not",
         "cols": ["Formulation", "Reason"],
         "rows": [
             ("Paint", "Yes", "A designed mixture: each component is measured and has a job"),
             ("Sea water", "No", "A mixture, but nobody designed it"),
             ("Distilled water", "No", "A single compound, so not a mixture"),
             ("Fertiliser", "Yes", "Measured amounts of compounds, designed to help crops grow"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Every mixture is a formulation.",
              "A formulation is a mixture designed as a useful product, with measured amounts of "
              "each component."),
             ("A formulation is a single compound.",
              "A formulation is a mixture of several components."),
             ("The amounts in a formulation do not matter.",
              "Each component is mixed in a carefully measured quantity, so the product has the "
              "required properties."),
         ]}]},
    ],
    "key_fact": "A formulation is a mixture that has been designed as a useful product. It is made "
                "by mixing the components in carefully measured quantities, so that the product has "
                "the required properties.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Pure substances shows the chemistry meaning of a mixture.",
                  "Alloys, and why they are harder than pure metals, are in Bonding."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: say which product is a formulation, and give the reason "
             "from the information.",
             "<strong>Explain</strong>: say why the amounts are measured: so the product has the "
             "required properties.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Define", "marks": 1,
             "prompt": "What is a formulation?",
             "why": "A formulation is a mixture that has been designed as a useful product.",
             "options": [
                 {"text": "Any mixture of two or more substances", "correct": False,
                  "reply": "A formulation is a mixture that has been designed as a useful product."},
                 {"text": "A mixture designed as a useful product", "correct": True},
                 {"text": "A single compound made in a factory", "correct": False,
                  "reply": "A formulation is a mixture, not a single compound."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State why the components of a formulation are mixed in measured quantities.",
             "why": "Carefully measured quantities make sure that the product has the required "
                    "properties.",
             "options": [
                 {"text": "So the product has the required properties", "correct": True},
                 {"text": "So that the mixture becomes one compound", "correct": False,
                  "reply": "Mixing does not make a compound. The product stays a mixture."},
                 {"text": "So that the product can be called pure", "correct": False,
                  "reply": "A formulation is a mixture, so it is not a pure substance."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "Which of these is a formulation?",
             "why": "Paint is a mixture designed as a useful product, with a measured amount of "
                    "each component.",
             "options": [
                 {"text": "Sea water taken from a rock pool", "correct": False,
                  "reply": "Sea water is a mixture, but nobody designed it."},
                 {"text": "Distilled water in a lab bottle", "correct": False,
                  "reply": "Distilled water is a single compound, not a mixture."},
                 {"text": "Gloss paint for a front door", "correct": True},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A company changes the amounts of the chemicals in its paint. Explain why "
                       "the paint may no longer do its job.",
             "why": "The properties of a formulation depend on the measured amount of each "
                    "component, so changing the amounts changes the properties.",
             "options": [
                 {"text": "Changing the amounts turns the paint into a pure substance",
                  "correct": False,
                  "reply": "The paint is still a mixture of several components."},
                 {"text": "Its properties depend on the measured amounts of each component",
                  "correct": True},
                 {"text": "The amounts in a formulation never change how it behaves",
                  "correct": False,
                  "reply": "The amounts are measured carefully because they change the "
                           "properties."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A label on a hand cream reads: water 70%, oil 20%, wax 8%, perfume 2%. "
                       "Explain how the label shows that the hand cream is a formulation. Put the "
                       "links in order.",
             "links": ["The label lists four substances, so the hand cream is a mixture.",
                       "This mixture has each substance in a measured amount, given as a "
                       "percentage.",
                       "So it is a mixture designed as a useful product: a formulation."],
             "herrings": [{"text": "The hand cream contains water, so it is a pure substance.",
                           "why": "It contains four substances, so it is a mixture."},
                          {"text": "Any mixture of oil and water is a formulation.",
                           "why": "A formulation is designed, with each component in a measured "
                                  "amount."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a medicine tablet must contain a measured amount of its drug. "
                       "Put the links in order.",
             "links": ["The drug is the component of the tablet that treats the illness.",
                       "So the amount matters: too little and the tablet does not work; too much "
                       "and it can be harmful.",
                       "So the drug is mixed in a carefully measured quantity, to give the tablet "
                       "the required properties."],
             "herrings": [{"text": "Measuring the drug makes the tablet a pure substance.",
                           "why": "A tablet with several components is a mixture."},
                          {"text": "The amount of drug only changes the colour of the tablet.",
                           "why": "The amount of drug changes how well the tablet works and how "
                                  "safe it is."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "A student says: “Sea water and paint are both mixtures, so both are "
                       "formulations.” Explain whether the student is right.",
             "points": ["Both sea water and paint are mixtures.",
                        "A formulation is a mixture that has been designed as a useful product.",
                        "Paint is made by mixing its components in carefully measured quantities, "
                        "so it has the required properties: it is a formulation.",
                        "Sea water was not designed, and its amounts were not measured, so it is "
                        "not a formulation.",
                        "So the student is wrong: only the paint is a formulation."],
             "reject": ["“Paint is a pure substance.” It is a mixture of several "
                        "components.",
                        "“Sea water is a formulation because it is useful.” It was not "
                        "designed and made from measured amounts."]},
        ],
    },
}
