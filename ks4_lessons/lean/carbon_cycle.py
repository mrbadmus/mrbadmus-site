# -*- coding: utf-8 -*-
"""The carbon cycle, in the lean shape. New record, no legacy page.
Spec table: ks4-carbon-cycle.md (AQA 8464 4.7.2.2 / 8461 4.7.2.2, word for word the same)."""

LESSON = {
    "slug": "carbon-cycle",
    "start": {
        "setup": "A tree takes in carbon dioxide all its life. Then it dies and falls over in a wood.",
        "question": "If you had to guess, what happens to the carbon in the dead tree?",
        "options": [
            ("It stays in the wood for ever",
             "It goes back into the air. Microorganisms decay the wood and respire, releasing the "
             "carbon as carbon dioxide."),
            ("It goes back into the air",
             "It goes back into the air. Microorganisms decay the wood and respire, releasing the "
             "carbon as carbon dioxide."),
        ],
        "answer": 1,
    },
    "words": ["carbon cycle", "photosynthesis", "respiration", "combustion"],
    "knowledge": [
        {"kind": "card", "title": "Materials are recycled",
         "body": ["Many different materials cycle through the living (biotic) and non-living "
                  "(abiotic) parts of an ecosystem.",
                  "All materials in the living world are recycled to provide the building blocks "
                  "for future organisms.",
                  "Carbon is one of these materials. The carbon cycle shows how it moves."]},
        {"kind": "card", "title": "Taking carbon out of the air",
         "body": ["Plants and algae take in carbon dioxide from the atmosphere for "
                  "photosynthesis.",
                  "The carbon becomes part of glucose. The plant uses the glucose to make its "
                  "other carbon compounds, such as starch, cellulose, proteins and fats."]},
        {"kind": "card", "title": "Passing carbon along",
         "body": ["When an animal eats a plant, the carbon compounds in the plant pass into the "
                  "animal.",
                  "When that animal is eaten, the carbon passes on again."]},
        {"kind": "card", "title": "Putting carbon back into the air",
         "body": ["Three processes return carbon to the atmosphere as carbon dioxide.",
                  {"points": [
                      "<strong>Respiration</strong> by plants, animals and microorganisms.",
                      "<strong>Decay</strong>: microorganisms feed on dead plants, dead animals "
                      "and animal waste. As they respire, they release the carbon as carbon "
                      "dioxide.",
                      "<strong>Combustion</strong>: burning wood or fossil fuels.",
                  ]}]},
        {"kind": "card", "title": "Fossil fuels",
         "body": ["Some dead organisms did not decay, because the conditions needed for decay "
                  "were missing.",
                  "Over millions of years their remains became fossil fuels: coal, oil and gas.",
                  "Burning fossil fuels releases this carbon into the atmosphere as carbon "
                  "dioxide."]},
        {"kind": "card", "title": "Reading a carbon cycle diagram",
         "body": ["Each arrow shows carbon moving. Name the process on each arrow.",
                  {"slot": "fig:carbon-cycle"}]},
        {"kind": "reveal", "title": "Where the carbon goes",
         "cols": ["Carbon moves from", "Carbon moves to"],
         "rows": [("Photosynthesis", "Carbon dioxide in the air", "Plants and algae"),
                  ("Feeding", "Plants", "Animals"),
                  ("Respiration", "Plants, animals and microorganisms",
                   "Carbon dioxide in the air"),
                  ("Death and waste", "Plants and animals", "Dead material in the soil"),
                  ("Decay", "Dead material, through the respiration of microorganisms",
                   "Carbon dioxide in the air"),
                  ("Combustion", "Wood and fossil fuels", "Carbon dioxide in the air")]},
        {"kind": "card", "title": "Why the carbon cycle matters",
         "body": ["The carbon cycle returns carbon from organisms to the atmosphere as carbon "
                  "dioxide, to be used by plants in photosynthesis.",
                  "Plants need that carbon dioxide to make glucose. Every animal depends on the "
                  "food that plants make.",
                  "Without decay, the carbon would stay locked in dead organisms."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Plants take in carbon dioxide but never give it out.",
              "Plants respire all the time, day and night, so they also release carbon "
              "dioxide."),
             ("Decay takes carbon dioxide out of the air.",
              "Decay releases carbon dioxide, because the microorganisms respire."),
             ("Plants get their carbon from the soil.",
              "Plants get their carbon from carbon dioxide in the air."),
             ("Carbon is used up when an organism dies.",
              "Carbon is never used up. It is recycled."),
         ]}]},
    ],
    "key_fact": "The carbon cycle returns carbon from organisms to the atmosphere as carbon "
                "dioxide, by respiration, decay and combustion. Plants take in the carbon dioxide "
                "for photosynthesis, so the same carbon is used again and again.",
    "deeper": [
        {"kind": "card", "title": "People and the carbon cycle",
         "body": ["Burning fossil fuels releases carbon that was locked away for millions of "
                  "years.",
                  "Cutting down and burning forests releases carbon dioxide, and leaves fewer "
                  "trees to take it in.",
                  "Both raise the level of carbon dioxide in the atmosphere. The Global warming "
                  "lesson explains why that matters."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say how the carbon moves, naming each process.",
             "<strong>Explain</strong>: say what happens and why, for example that decay "
             "releases carbon dioxide because microorganisms respire.",
             "<strong>Interpret a diagram</strong>: name the process on each arrow and say "
             "which way the carbon moves.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the process that removes carbon dioxide from the atmosphere.",
             "why": "Plants and algae take in carbon dioxide for photosynthesis.",
             "options": [
                 {"text": "Respiration", "correct": False,
                  "reply": "Respiration releases carbon dioxide."},
                 {"text": "Photosynthesis", "correct": True},
                 {"text": "Combustion", "correct": False,
                  "reply": "Burning releases carbon dioxide."},
                 {"text": "Decay", "correct": False,
                  "reply": "Decay releases carbon dioxide, because the microorganisms respire."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Identify the organisms that return the carbon in dead leaves to the "
                       "atmosphere.",
             "why": "Bacteria and fungi are the microorganisms that decay dead leaves. They "
                    "respire, releasing carbon dioxide.",
             "options": [
                 {"text": "Green plants and algae", "correct": False,
                  "reply": "Plants and algae take carbon dioxide out of the air."},
                 {"text": "Bacteria and fungi", "correct": True},
                 {"text": "Herbivores that eat living plants", "correct": False,
                  "reply": "Herbivores eat living plants, not dead leaves."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain how carbon in a rabbit's body can get back into the atmosphere.",
             "why": "The rabbit respires while it is alive. When it dies, microorganisms decay "
                    "its body and respire. Both release carbon dioxide.",
             "options": [
                 {"text": "Only by combustion, when its body is burned after it dies",
                  "correct": False,
                  "reply": "Respiration and decay return carbon too. Most dead animals are never "
                           "burned."},
                 {"text": "By its respiration, and by microorganisms respiring as they decay it",
                  "correct": True},
                 {"text": "By photosynthesis in its cells, which gives out carbon dioxide",
                  "correct": False,
                  "reply": "Animals do not photosynthesise. Photosynthesis takes carbon dioxide "
                           "in."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why the carbon cycle is important to plants.",
             "why": "The carbon cycle returns carbon dioxide to the atmosphere. Plants need it "
                    "for photosynthesis.",
             "options": [
                 {"text": "It returns carbon dioxide to the air for photosynthesis",
                  "correct": True},
                 {"text": "It removes carbon dioxide, which is poisonous to plants",
                  "correct": False,
                  "reply": "Plants need carbon dioxide for photosynthesis."},
                 {"text": "It gives plants carbon from the soil through their roots",
                  "correct": False,
                  "reply": "Plants get their carbon from carbon dioxide in the air."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how carbon in the air can end up in a fox. Put the links in "
                       "order.",
             "links": ["Grass takes in carbon dioxide and uses the carbon to make glucose by "
                       "photosynthesis.",
                       "A rabbit eats the grass, so the carbon compounds pass into the rabbit.",
                       "A fox eats the rabbit, so the carbon passes into the fox."],
             "herrings": [{"text": "The fox breathes in carbon dioxide and uses it to grow.",
                           "why": "Animals cannot use carbon dioxide. They get carbon from "
                                  "their food."},
                          {"text": "The grass takes in carbon from the soil through its roots.",
                           "why": "Plants get their carbon from carbon dioxide in the air."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how the carbon in a dead tree can be used again by plants. Put "
                       "the links in order.",
             "links": ["Microorganisms feed on the dead tree and decay it.",
                       "The microorganisms respire, releasing the carbon into the atmosphere as "
                       "carbon dioxide.",
                       "Plants take in the carbon dioxide for photosynthesis."],
             "herrings": [{"text": "The microorganisms photosynthesise and release oxygen.",
                           "why": "Microorganisms that cause decay respire. They release "
                                  "carbon dioxide."},
                          {"text": "The carbon is destroyed as the tree decays.",
                           "why": "Carbon is never destroyed. It is recycled."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "Describe how carbon moves between the atmosphere and living organisms in "
                       "the carbon cycle. Explain why the carbon cycle is important to living "
                       "organisms.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear account that names photosynthesis, "
                  "feeding, respiration and decay in a logical order, and explains why "
                  "returning carbon dioxide matters to living organisms.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Several correct processes, with some "
                  "linking, or a correct cycle with no explanation of its importance.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two correct processes or statements.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Plants and algae take in carbon dioxide from the atmosphere for "
                        "photosynthesis.",
                        "The carbon becomes part of glucose and other carbon compounds in the "
                        "plant.",
                        "Animals eat the plants, so the carbon compounds pass to the animals.",
                        "Plants and animals respire, releasing carbon dioxide into the "
                        "atmosphere.",
                        "When organisms die, microorganisms decay them and respire, returning "
                        "the carbon to the atmosphere as carbon dioxide.",
                        "Burning wood or fossil fuels (combustion) also releases carbon dioxide.",
                        "The cycle returns carbon dioxide for plants to use in photosynthesis.",
                        "Materials are recycled to provide the building blocks for future "
                        "organisms; without decay, carbon would stay locked in dead organisms."],
             "reject": ["“Decay takes carbon dioxide out of the air.”",
                        "“Plants do not respire.”"]},
        ],
    },
}
