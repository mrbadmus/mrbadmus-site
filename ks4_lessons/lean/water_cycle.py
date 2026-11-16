# -*- coding: utf-8 -*-
"""The water cycle, in the lean shape. New record, no legacy page.
Spec table: ks4-water-cycle.md (AQA 8464 4.7.2.2 / 8461 4.7.2.2, word for word the same)."""

LESSON = {
    "slug": "water-cycle",
    "start": {
        "setup": "Sea water is salty. Rain is not.",
        "question": "If you had to guess, where does the salt go when sea water evaporates?",
        "options": [
            ("It rises into the clouds",
             "It stays in the sea. Only the water evaporates, so rain falls as fresh water."),
            ("It stays in the sea",
             "It stays in the sea. Only the water evaporates, so rain falls as fresh water."),
        ],
        "answer": 1,
    },
    "words": ["evaporation", "condensation", "precipitation", "transpiration"],
    "knowledge": [
        {"kind": "card", "title": "Water is recycled",
         "body": ["Water is one of the materials that cycle through the living and non-living "
                  "parts of an ecosystem.",
                  "The water cycle provides fresh water for plants and animals on land before "
                  "draining into the seas.",
                  "Water is continuously evaporated and precipitated."]},
        {"kind": "reveal", "title": "Round the water cycle",
         "cols": ["What happens"],
         "rows": [("Evaporation", "The Sun heats water in the sea, lakes and soil. The water "
                                  "turns into water vapour and rises."),
                  ("Condensation", "The water vapour cools as it rises. It turns back into tiny "
                                   "droplets of liquid water, which form clouds."),
                  ("Precipitation", "Water falls from the clouds as rain, snow or hail."),
                  ("Run-off", "Water flows over the ground into streams and rivers, and back to "
                              "the sea."),
                  ("Percolation", "Water soaks down through the soil and rock. It drains slowly "
                                  "to rivers and the sea."),
                  ("Transpiration", "Plants take up water through their roots and lose water "
                                    "vapour from their leaves.")]},
        {"kind": "card", "title": "The water cycle diagram",
         "body": ["Follow the arrows from the sea, over the land and back to the sea.",
                  {"slot": "fig:water-cycle"}]},
        {"kind": "card", "title": "Why the rain is fresh",
         "body": ["When sea water evaporates, only the water turns into vapour. The salt stays "
                  "behind in the sea.",
                  "So the water that falls as precipitation is fresh water."]},
        {"kind": "card", "title": "Why the water cycle matters",
         "body": [{"points": [
             "Plants on land need fresh water for photosynthesis.",
             "Animals on land need fresh water to drink.",
             "The water cycle keeps bringing fresh water onto the land. Then it drains back "
             "into the seas, and the cycle carries on.",
         ]}]},
        {"kind": "card", "title": "Living things in the water cycle",
         "body": ["Plants take up water from the soil through their roots. They lose water "
                  "vapour from their leaves. This is transpiration.",
                  "Animals take in water when they drink and eat. They return it in urine and "
                  "faeces, and as water vapour when they breathe out."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Condensation turns liquid water into water vapour.",
              "Evaporation turns liquid water into vapour. Condensation turns vapour back into "
              "liquid."),
             ("Rain is salty because it came from the sea.",
              "The salt stays in the sea when the water evaporates."),
             ("Precipitation only means rain.",
              "Precipitation is rain, snow or hail."),
             ("Transpiration is water evaporating from the soil.",
              "Transpiration is water vapour lost from plant leaves."),
         ]}]},
    ],
    "key_fact": "Water is continuously evaporated and precipitated. The water cycle provides "
                "fresh water for plants and animals on land before draining into the seas.",
    "deeper": [
        {"kind": "card", "title": "Link to Chemistry",
         "body": ["As the early Earth cooled, water vapour in the atmosphere condensed to form "
                  "the oceans. The same change, condensation, makes clouds today."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: name each stage in order, from the sea back to the "
             "sea.",
             "<strong>Explain</strong>: say what happens and why, for example that water vapour "
             "condenses because it cools.",
             "<strong>Interpret a diagram</strong>: name the process on each arrow.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the process in which water vapour cools and turns into droplets of "
                       "liquid water.",
             "why": "This is condensation. It forms clouds.",
             "options": [
                 {"text": "Evaporation", "correct": False,
                  "reply": "Evaporation turns liquid water into vapour."},
                 {"text": "Condensation", "correct": True},
                 {"text": "Precipitation", "correct": False,
                  "reply": "Precipitation is water falling from clouds."},
                 {"text": "Transpiration", "correct": False,
                  "reply": "Transpiration is water vapour lost from plant leaves."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Which of these is precipitation?",
             "why": "Precipitation is water falling from clouds as rain, snow or hail.",
             "options": [
                 {"text": "Water vapour rising from the sea", "correct": False,
                  "reply": "That is evaporation."},
                 {"text": "Snow falling from a cloud", "correct": True},
                 {"text": "Water soaking into the soil", "correct": False,
                  "reply": "That is percolation."},
                 {"text": "Water vapour lost from leaves", "correct": False,
                  "reply": "That is transpiration."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why clouds form high above the ground.",
             "why": "Water vapour cools as it rises. It condenses into tiny droplets, which form "
                    "clouds.",
             "options": [
                 {"text": "Water vapour warms as it rises, so it evaporates into droplets",
                  "correct": False,
                  "reply": "Higher up it is colder. Water vapour condenses when it cools."},
                 {"text": "Water vapour cools as it rises, so it condenses into droplets",
                  "correct": True},
                 {"text": "Plants push water vapour upwards and turn it into droplets",
                  "correct": False,
                  "reply": "Plants release water vapour. Cooling turns it into droplets."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why the water cycle is important to animals that live on land.",
             "why": "Precipitation brings fresh water onto the land. Animals need fresh water to "
                    "drink.",
             "options": [
                 {"text": "It brings salty sea water onto the land for them", "correct": False,
                  "reply": "Rain is fresh water. The salt stays in the sea."},
                 {"text": "It keeps all the water locked up in the clouds", "correct": False,
                  "reply": "Water falls from clouds as precipitation, onto the land."},
                 {"text": "It brings fresh water onto the land for them to drink",
                  "correct": True},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how water from the sea becomes fresh water in a river. Put the "
                       "links in order.",
             "links": ["The Sun heats the sea and water evaporates, leaving the salt behind.",
                       "The water vapour rises, cools and condenses into droplets, forming "
                       "clouds.",
                       "The water falls as rain on the land and runs off into a river."],
             "herrings": [{"text": "The salt evaporates with the water and falls in the rain.",
                           "why": "The salt stays in the sea. Rain is fresh water."},
                          {"text": "The water vapour warms up as it rises, so it condenses.",
                           "why": "Water vapour condenses when it cools."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how water in the soil can end up in a cloud. Put the links in "
                       "order.",
             "links": ["A tree's roots take up water from the soil.",
                       "The tree loses water vapour from its leaves by transpiration.",
                       "The water vapour rises, cools and condenses to form a cloud."],
             "herrings": [{"text": "The leaves give out liquid water, which rises into the sky.",
                           "why": "Leaves lose water as water vapour."},
                          {"text": "The water vapour condenses because the Sun warms it.",
                           "why": "Water vapour condenses when it cools."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "Describe the water cycle. Explain why it is important to plants and "
                       "animals that live on land.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "The stages in a logical order with the "
                  "right words (evaporation, condensation, precipitation), and a clear "
                  "explanation of why fresh water on land matters to plants and animals.",
                  "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Most stages, with some order, and some "
                  "link to living things.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two correct stages or statements.",
                  "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The Sun heats the sea and water evaporates.",
                        "The salt is left behind, so the water vapour is fresh water.",
                        "The water vapour rises and cools.",
                        "It condenses into droplets that form clouds.",
                        "Water falls as precipitation (rain, snow or hail) onto the land.",
                        "This provides fresh water: plants use it for photosynthesis and "
                        "animals drink it.",
                        "Plants take up water through their roots and lose water vapour from "
                        "their leaves by transpiration.",
                        "Water drains through rivers back into the sea, and the cycle carries "
                        "on."],
             "reject": ["“Condensation is when water turns into water vapour.”",
                        "“Rain is salty because it comes from the sea.”"]},
        ],
    },
}
