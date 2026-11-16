# -*- coding: utf-8 -*-
"""Waste management, in the lean shape. New record, no legacy page.
Spec table: ks4-waste-management.md (AQA 8464 4.7.3.2 / 8461 4.7.3.2, the same words in both)."""

LESSON = {
    "slug": "waste-management",
    "start": {
        "setup": "The number of people in the world is growing quickly.",
        "question": "If you had to guess, what happens to the amount of waste the world produces?",
        "options": [
            ("It increases",
             "It increases. More people use more resources and produce more waste."),
            ("It stays the same",
             "It increases. More people use more resources and produce more waste."),
        ],
        "answer": 0,
    },
    "words": ["pollution", "standard of living", "landfill", "toxic chemicals"],
    "knowledge": [
        {"kind": "card", "title": "Why there is more waste",
         "body": ["Rapid growth in the human population and an increase in the standard of living mean "
                  "that more and more resources are used and more waste is produced.",
                  "A higher standard of living means each person uses more resources and throws more "
                  "away.",
                  "Unless waste and chemical materials are properly handled, more pollution will be "
                  "caused."]},
        {"kind": "reveal", "title": "Where pollution happens",
         "cols": ["What causes it"],
         "rows": [
             ("In water", "Sewage, fertiliser or toxic chemicals."),
             ("In air", "Smoke and acidic gases."),
             ("On land", "Landfill and toxic chemicals."),
         ]},
        {"kind": "card", "title": "What the pollutants are",
         "body": [{"points": [
             "<strong>Sewage</strong>: human waste from toilets, if it reaches rivers or the sea "
             "untreated.",
             "<strong>Fertiliser</strong>: washed off farm fields into rivers and lakes by rain.",
             "<strong>Smoke</strong>: tiny solid particles from burning fuels.",
             "<strong>Acidic gases</strong>: such as sulfur dioxide from burning fuels. They cause "
             "acid rain.",
             "<strong>Landfill</strong>: rubbish buried in the ground. It takes up land.",
             "<strong>Toxic chemicals</strong>: poisons such as some pesticides and herbicides, on "
             "land or in water.",
         ]}]},
        {"kind": "card", "title": "Pollution and biodiversity",
         "body": ["Pollution kills plants and animals, which can reduce biodiversity.",
                  "Handling waste properly reduces pollution. For example, sewage is treated before "
                  "the water goes back into rivers."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Only a bigger population makes more waste.",
              "A higher standard of living makes more waste too."),
             ("Fertiliser is not a pollutant, because it helps plants grow.",
              "Fertiliser washed into water is a water pollutant."),
             ("Pollution is just the litter you can see.",
              "Sewage, fertiliser, smoke and acidic gases are pollution too."),
         ]}]},
    ],
    "key_fact": "More people and a higher standard of living mean more resources are used and more "
                "waste is produced. Unless it is handled properly, waste pollutes water, air and land, "
                "and pollution kills plants and animals, which can reduce biodiversity.",
    "deeper": [
        {"kind": "card", "title": "How fertiliser in a lake can kill fish",
         "body": [{"points": [
             "Fertiliser in the water makes algae grow very fast.",
             "The algae cover the surface and block the light, so plants under the water die.",
             "Bacteria break down the dead plants. They respire and use up the oxygen in the water.",
             "Fish and other animals die because there is not enough oxygen.",
         ]}]},
        {"kind": "card", "title": "Smoke and plants",
         "body": ["Smoke particles can settle on leaves. Less light reaches the leaf, so the plant "
                  "photosynthesises less.",
                  "Smoke also blackens buildings and can harm people's lungs."]},
        {"kind": "card", "title": "Links to chemistry",
         "body": ["In chemistry you meet the same air pollutants: sulfur dioxide and oxides of "
                  "nitrogen cause acid rain and breathing problems."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what happens, for example where each pollutant comes "
             "from.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give one source of water pollution.",
             "why": "Water is polluted by sewage, fertiliser or toxic chemicals.",
             "options": [
                 {"text": "Smoke", "correct": False, "reply": "Smoke pollutes the air."},
                 {"text": "Sewage", "correct": True},
                 {"text": "Acidic gases", "correct": False, "reply": "Acidic gases pollute the air."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Which pair are both sources of air pollution?",
             "why": "Air is polluted by smoke and acidic gases.",
             "options": [
                 {"text": "Sewage and fertiliser", "correct": False,
                  "reply": "Sewage and fertiliser pollute water."},
                 {"text": "Sewage and chemicals in rivers", "correct": False,
                  "reply": "These pollute water."},
                 {"text": "Smoke and acidic gases", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why a rising standard of living increases pollution.",
             "why": "Each person uses more resources and produces more waste. Waste that is not handled "
                    "properly causes pollution.",
             "options": [
                 {"text": "Each person uses more and throws more away", "correct": True},
                 {"text": "Each person uses fewer resources than before", "correct": False,
                  "reply": "A higher standard of living means more resources are used, not fewer."},
                 {"text": "It stops waste from being recycled", "correct": False,
                  "reply": "Recycling can still happen. Each person uses more and throws more away."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Fertiliser washes off a field into a river. Explain how this can reduce "
                       "biodiversity in the river.",
             "why": "The fertiliser pollutes the water. Pollution kills plants and animals, so fewer "
                    "species survive.",
             "options": [
                 {"text": "It makes every species in the river grow more", "correct": False,
                  "reply": "Fertiliser in water is a pollutant. It harms the river."},
                 {"text": "It pollutes the water and kills plants and animals", "correct": True},
                 {"text": "It pollutes the air above the river", "correct": False,
                  "reply": "Fertiliser washed into a river pollutes the water."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how a growing human population can reduce biodiversity. Put the links "
                       "in order.",
             "links": ["A growing population uses more resources and produces more waste.",
                       "Waste that is not handled properly pollutes water, air and land.",
                       "The pollution kills plants and animals, so biodiversity can be reduced."],
             "herrings": [{"text": "A growing population uses fewer resources.",
                           "why": "More people use more resources."},
                          {"text": "Pollution only harms humans.",
                           "why": "Pollution kills plants and animals too."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Untreated sewage is let into a river. Explain how this can reduce biodiversity. "
                       "Put the links in order.",
             "links": ["The sewage pollutes the river water.",
                       "The pollution kills plants and animals in the river.",
                       "Fewer different species are left, so biodiversity is reduced."],
             "herrings": [{"text": "The sewage pollutes the air above the river.",
                           "why": "Sewage in a river is water pollution."},
                          {"text": "More species can live in the river.",
                           "why": "Pollution kills plants and animals."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe how humans pollute water, air and land, and how this affects "
                       "biodiversity.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Gives sources of pollution for at least two of "
                  "water, air and land, and links pollution to a fall in biodiversity.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Gives one source of pollution or one effect.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Water is polluted by sewage, fertiliser or toxic chemicals.",
                        "Air is polluted by smoke and acidic gases.",
                        "Land is polluted by landfill and toxic chemicals.",
                        "Pollution kills plants and animals.",
                        "This can reduce biodiversity."],
             "reject": ["“Fertiliser is not a pollutant because it helps plants grow.”",
                        "“Pollution only affects humans.”"]},
        ],
    },
}
