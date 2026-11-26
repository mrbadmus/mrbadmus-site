# -*- coding: utf-8 -*-
"""Oxidation, in the lean shape. Spec table: docs/lessons/wave2/ks3-oxidation.md."""

LESSON = {
    "slug": "oxidation",
    "start": {
        "setup": "A strip of magnesium burns with a bright white flame. "
                 "It leaves a white powder.",
        "question": "If you had to guess, would all the powder left from burning magnesium "
                    "weigh more than the metal did, or less?",
        "options": [
            ("More",
             "Right. The magnesium joins with oxygen from the air. The powder is magnesium "
             "plus that oxygen."),
            ("Less",
             "Burning wood leaves less, because gases escape. Magnesium takes in oxygen and "
             "keeps it."),
        ],
        "answer": 0,
    },
    "words": ["oxidation", "metal oxide", "rust", "corrosion"],
    "word_defs": {
        "oxidation": "A reaction in which a substance gains oxygen.",
        "metal oxide": "A compound of a metal with oxygen, made when the metal is oxidised.",
        "rust": "Hydrated iron oxide. Iron and steel rust when they meet oxygen and water.",
        "corrosion": "A metal being slowly worn away by reacting with substances around it.",
    },
    "knowledge": [
        {"kind": "card", "title": "What oxidation is",
         "body": ["Oxidation is a reaction in which a substance gains oxygen.",
                  "A metal reacts with oxygen to make a metal oxide.",
                  {"figure": "c5-word-metal-oxygen"},
                  "The oxygen usually comes from the air."]},
        {"kind": "card", "title": "Burning magnesium",
         "body": [{"figure": "c5-word-magnesium"},
                  "Magnesium burns with a bright white flame.",
                  "It leaves a white powder, which is magnesium oxide.",
                  "The powder weighs more than the magnesium did.",
                  "The extra mass is the oxygen it gained from the air."]},
        {"kind": "reveal", "title": "Metals reacting with oxygen",
         "cols": ["Product", "What you see"],
         "rows": [
             ("magnesium + oxygen", "magnesium oxide", "A bright white flame and a white powder"),
             ("copper + oxygen", "copper oxide", "A black layer forms on the hot copper"),
             ("iron + oxygen", "iron oxide", "Hot iron wool glows and gives off sparks"),
         ]},
        {"kind": "card", "title": "Fast and slow oxidation",
         "body": ["When a fuel burns, it gains oxygen.",
                  "So combustion is an oxidation reaction. It is fast and gives out heat and light.",
                  "Rusting is an oxidation reaction too. It is slow and can take years."]},
        {"kind": "card", "title": "Rusting",
         "body": ["Rusting is the oxidation of iron.",
                  {"figure": "c5-word-rust"},
                  "Iron needs both oxygen and water to rust.",
                  "Only iron and steel rust. Other metals corrode.",
                  "Rust is weak and flaky. It falls off, so the iron underneath keeps rusting."]},
        {"kind": "card", "title": "Four tubes, four nails",
         "body": [{"figure": "c5-rust-tubes"},
                  {"points": ["Tube 1 has air and water. The nail rusts.",
                              "Tube 2 has air but no water. A drying agent takes the water out.",
                              "Tube 3 has water but no air. Boiling took the air out of the water, and oil keeps air out.",
                              "Tube 4 has air and salt water. The nail rusts fastest."]},
                  "One tube on its own cannot show what rusting needs.",
                  "Only tube 1 rusts. Tubes 2 and 3 do not.",
                  "So rusting needs both oxygen and water.",
                  "Tube 4 shows that salt makes rusting faster."]},
        {"kind": "card", "title": "Aluminium and its oxide layer",
         "body": ["Aluminium reacts with oxygen in the air straight away.",
                  "A thin layer of aluminium oxide forms on its surface.",
                  "The layer sticks tightly and stops air reaching the metal underneath.",
                  "So aluminium window frames last for many years outdoors."]},
        {"kind": "card", "title": "Stopping rust",
         "body": [{"points": ["Paint, oil or grease keeps oxygen and water away from the iron.",
                              "Galvanising coats the iron with a layer of zinc.",
                              "Blocks of zinc are bolted to a ship's steel hull."]},
                  "Zinc is more reactive than iron, so the zinc corrodes instead of the iron.",
                  "This is called sacrificial protection.",
                  "The zinc blocks slowly wear away, so they must be checked and replaced."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Aluminium does not react with air, so it never corrodes.",
              "Aluminium oxidises straight away. Its oxide layer protects the metal underneath.",
              "REACT-14"),
             ("Rusting needs only water, or only air.",
              "Rusting needs oxygen and water together.",
              "REACT-15"),
             ("Rusting makes iron lighter.",
              "Rust weighs more than the iron it came from. Oxygen and water have joined it."),
             ("Every metal rusts.",
              "Only iron and steel rust. Other metals corrode."),
             ("Salt is needed for rusting.",
              "Salt is not needed. It makes rusting happen faster."),
         ]}]},
    ],
    "key_fact": "Oxidation is a reaction in which a substance gains oxygen, so the product weighs "
                "more. Iron rusts only when it has both oxygen and water.",
    "deeper": [
        {"kind": "card", "title": "Oxidation in your cells",
         "body": ["Respiration is an oxidation reaction.",
                  "Glucose reacts with oxygen to make carbon dioxide and water.",
                  "It happens in small steps, so your cells can use the energy."]},
        {"kind": "card", "title": "Losing oxygen",
         "body": ["The opposite of oxidation is reduction.",
                  "In reduction, a substance loses oxygen.",
                  "Many metals are extracted from their ores by reduction."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why tubes 2 and 3 are the important ones?",
    "safety_note": "Wear eye protection. Never look straight at burning magnesium. "
                   "Its bright light can damage your eyes.",
    "connects_heading": None,
    "ks4_becomes": "Oxidation and reduction, corrosion and how to prevent it, and the reactivity "
                   "series explained.",
    "figures": [
        {"id": "c5-word-metal-oxygen", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "The general equation for oxidising a metal",
         "desc": "Written left to right. On the left, under the tag Reactants: metal, then a "
                 "plus sign, then oxygen. In the middle, a drawn arrow pointing right. On the "
                 "right, under the tag Product: metal oxide.",
         "caption": "A metal gains oxygen and becomes a metal oxide.",
         "data": {"left": ["metal", "oxygen"], "right": ["metal oxide"]}},
        {"id": "c5-word-magnesium", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "Burning magnesium",
         "desc": "Written left to right. On the left, under the tag Reactants: magnesium, then "
                 "a plus sign, then oxygen. In the middle, a drawn arrow pointing right. On the "
                 "right, under the tag Product: magnesium oxide.",
         "caption": "Magnesium gains oxygen from the air.",
         "data": {"left": ["magnesium", "oxygen"], "right": ["magnesium oxide"]}},
        {"id": "c5-word-rust", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "Iron rusting",
         "desc": "Written left to right. On the left, under the tag Reactants: iron, plus "
                 "oxygen, plus water. In the middle, a drawn arrow pointing right. On the right, "
                 "under the tag Product: rust.",
         "caption": "Rust is hydrated iron oxide.",
         "data": {"left": ["iron", "oxygen", "water"], "right": ["rust"]}},
        {"id": "c5-rust-tubes", "kind": "diagram", "status": "drawn", "art": "c5-rust-tubes",
         "title": "Four tubes that show what rusting needs",
         "desc": "Four test tubes in a row, numbered 1 to 4, each with an iron nail. Tube 1 is "
                 "open and has water in the bottom half. The nail is rusty at the water line. "
                 "Tube 2 has a bung and a drying agent at the bottom, and the nail is in dry air. "
                 "It has no rust. Tube 3 has a bung, boiled water almost to the top, and a layer "
                 "of oil on the water. The nail has no rust. Tube 4 is open and has salt water in "
                 "the bottom half. The nail is very rusty.",
         "caption": "Only the tubes with both air and water rust.",
         "data": {
             "colours": {"water": "#D6E6EE", "oil": "#E9C46A", "rust": "#A0461E",
                         "salt": "#DCE4E6"},
             "tubes": [
                 {"label": ["air", "and water"], "result": ["rusts"]},
                 {"label": ["dry air", "no water"], "result": ["no rust"]},
                 {"label": ["water", "no air"], "result": ["no rust"]},
                 {"label": ["air and", "salt water"], "result": ["rusts", "fastest"]},
             ]}},
    ],
    "ladder_stem": {
        "explain": "In the four-tube experiment, tube 1 shows that a nail rusts. Explain why "
                   "tubes 2 and 3 are also needed. State the conclusion from all four tubes. "
                   "Say what tube 4 adds.",
        "produce": "A boat owner is told to bolt blocks of a more reactive metal to the hull. "
                   "He says that sounds like the worst idea. Explain why the method works. Say "
                   "what happens to the blocks, and why they must be checked.",
    },
    "ladder_feedback": {
        "recall": {
            1: "Oxidation is named after oxygen. Gaining water is not oxidation.",
            2: "Splitting apart using heat is thermal decomposition. Oxidation adds oxygen.",
            3: "Mixing makes no new substance. In oxidation, oxygen joins the substance.",
        },
        "apply": {
            1: "A nail in air and water does rust. So water does not stop rusting.",
            2: "This nail had no air and did not rust. That fits air being needed.",
            3: "A nail in air and plain water still rusts. Salt only makes rusting faster.",
        },
    },
}
