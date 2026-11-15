# -*- coding: utf-8 -*-
"""Land use, in the lean shape. New record, no legacy page.
Spec table: ks4-land-use.md (AQA 8464 4.7.3.3 / 8461 4.7.3.3, the same content in both)."""

LESSON = {
    "slug": "land-use",
    "start": {
        "setup": "Peat is dug out of bogs and sold as garden compost.",
        "question": "If you had to guess, does digging up peat add carbon dioxide to the air?",
        "options": [
            ("Yes",
             "Yes. When the peat decays or is burned, its carbon is released as carbon dioxide."),
            ("No",
             "Yes. When the peat decays or is burned, its carbon is released as carbon dioxide."),
        ],
        "answer": 0,
    },
    "words": ["peat bog", "habitat", "compost", "biodiversity"],
    "knowledge": [
        {"kind": "card", "title": "How humans use land",
         "body": ["Humans reduce the amount of land available for other animals and plants by:",
                  {"points": ["building", "quarrying", "farming", "dumping waste"]},
                  "Each one destroys habitats, so there is less space for wild species."]},
        {"kind": "card", "title": "What peat is",
         "body": ["Peat bogs are wet, waterlogged places.",
                  "There is very little oxygen, so dead plants decay very slowly and only partly.",
                  "Over thousands of years the partly decayed plants build up as peat.",
                  "Peat holds a lot of carbon that came from those plants."]},
        {"kind": "card", "title": "Why peat is dug up",
         "body": ["Peat is dug up to produce garden compost. It is cheap and helps plants grow.",
                  "In some places peat is also burned as a fuel."]},
        {"kind": "reveal", "title": "What destroying peat bogs does",
         "cols": ["What happens"],
         "rows": [
             ("To the habitat",
              "The area of this habitat is reduced."),
             ("To biodiversity",
              "The variety of different plant, animal and microorganism species that live there "
              "falls."),
             ("To the atmosphere",
              "The decay or burning of the peat releases carbon dioxide into the atmosphere."),
         ]},
        {"kind": "card", "title": "The conflict over peat",
         "body": [{"points": [
             "<strong>The need for compost</strong>: cheap, available compost helps increase food "
             "production.",
             "<strong>The need to conserve peat bogs</strong>: they are habitats for biodiversity, "
             "and keeping the peat in the ground reduces carbon dioxide emissions.",
         ]},
         "Peat-free compost, made from things such as garden waste or bark, reduces the demand for "
         "peat."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Peat only releases carbon dioxide when it is burned.",
              "The decay of peat releases carbon dioxide too."),
             ("Destroying a peat bog only harms plants.",
              "It reduces the variety of plant, animal and microorganism species."),
             ("Peat grows back quickly.",
              "Peat builds up very slowly, over thousands of years."),
         ]}]},
    ],
    "key_fact": "Building, quarrying, farming and dumping waste reduce the land available for other "
                "animals and plants. Destroying peat bogs to produce garden compost reduces this habitat "
                "and its biodiversity, and the decay or burning of the peat releases carbon dioxide "
                "into the atmosphere.",
    "deeper": [
        {"kind": "card", "title": "Why drained peat decays",
         "body": ["Draining a bog lets air into the peat.",
                  "With oxygen, microorganisms can decay the peat faster.",
                  "They respire, and respiration releases carbon dioxide."]},
        {"kind": "card", "title": "Links",
         "body": ["Carbon dioxide is one of the gases whose rising levels contribute to global warming. "
                  "See Global warming.",
                  "Decay is carried out by microorganisms. See the carbon cycle."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: say what happens and why.",
             "<strong>Evaluate</strong>: give the benefit and the cost, then make a judgement.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give one way humans reduce the land available for other animals and plants.",
             "why": "Building, quarrying, farming and dumping waste all take land.",
             "options": [
                 {"text": "Recycling", "correct": False,
                  "reply": "Recycling means less waste is dumped, so it saves land."},
                 {"text": "Quarrying", "correct": True},
                 {"text": "Planting hedgerows", "correct": False,
                  "reply": "Hedgerows give wildlife food and shelter."},
             ]},
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the gas released when peat decays or is burned.",
             "why": "The decay or burning of the peat releases carbon dioxide into the atmosphere.",
             "options": [
                 {"text": "Oxygen", "correct": False,
                  "reply": "Decay and burning use oxygen. They release carbon dioxide."},
                 {"text": "Nitrogen", "correct": False,
                  "reply": "The carbon in the peat is released as carbon dioxide."},
                 {"text": "Carbon dioxide", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why destroying a peat bog reduces biodiversity.",
             "why": "The area of the habitat is reduced, so fewer different plant, animal and "
                    "microorganism species can live there.",
             "options": [
                 {"text": "The habitat is lost, so fewer species can live there", "correct": True},
                 {"text": "The peat gives off oxygen, which kills the species", "correct": False,
                  "reply": "Destroying peat releases carbon dioxide. Species are lost because the habitat goes."},
                 {"text": "New species move in to replace every one lost", "correct": False,
                  "reply": "The species that need the bog have nowhere else to live."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why gardeners are asked to buy peat-free compost.",
             "why": "Less peat is dug up, so peat bogs are conserved as habitats and less carbon "
                    "dioxide is released.",
             "options": [
                 {"text": "Peat compost is poisonous to plants", "correct": False,
                  "reply": "Peat compost helps plants grow. The problem is the bog that is destroyed."},
                 {"text": "Less peat is dug up, so peat bogs are conserved", "correct": True},
                 {"text": "Peat bogs are not a habitat for any species", "correct": False,
                  "reply": "Peat bogs are a habitat for many plant, animal and microorganism species."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how digging up peat for compost increases the carbon dioxide in the "
                       "atmosphere. Put the links in order.",
             "links": ["Peat holds carbon from plants that only partly decayed.",
                       "Once the peat is dug up and used as compost, microorganisms decay it.",
                       "As the microorganisms respire, carbon dioxide is released into the atmosphere."],
             "herrings": [{"text": "Digging up peat makes it take in carbon dioxide.",
                           "why": "Peat that decays releases carbon dioxide."},
                          {"text": "The decay of peat releases oxygen.",
                           "why": "Decay releases carbon dioxide."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A housing estate is built on woodland. Explain how this can reduce "
                       "biodiversity. Put the links in order.",
             "links": ["Building on the land destroys the habitats there.",
                       "Plants and animals lose their food and shelter.",
                       "Fewer different species can live in the area, so biodiversity falls."],
             "herrings": [{"text": "Building adds new habitats for wild species.",
                           "why": "Building reduces the land available for other animals and plants."},
                          {"text": "Houses increase the land available for wildlife.",
                           "why": "Houses take land away from wildlife."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Evaluate", "marks": 6,
             "prompt": "Peat is a cheap compost that helps grow food. Evaluate the use of peat as "
                       "compost.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Gives the benefit and both costs, explained, "
                  "and ends in a judgement.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Gives a benefit and a cost, with a limited "
                  "judgement.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Gives one relevant point.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Benefit: peat is a cheap, available compost that helps increase food "
                        "production.",
                        "Cost: destroying peat bogs reduces the area of this habitat.",
                        "So the variety of plant, animal and microorganism species living there "
                        "(biodiversity) falls.",
                        "Cost: the decay or burning of the peat releases carbon dioxide into the "
                        "atmosphere, which contributes to global warming.",
                        "Peat builds up very slowly, so a bog cannot quickly be replaced.",
                        "Judgement: any reasoned judgement that weighs the food benefit against the "
                        "loss of habitat and the carbon dioxide; for example, peat-free compost can "
                        "be used instead, so the costs of digging up peat bogs are hard to "
                        "justify."],
             "reject": ["“Peat only releases carbon dioxide if it is burned.”",
                        "“Peat grows back quickly, so it does not matter.”"]},
        ],
    },
}
