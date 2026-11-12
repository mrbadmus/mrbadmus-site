# -*- coding: utf-8 -*-
"""The photosynthesis reaction, in the lean shape. Spec table: docs/lessons/wave1/ks3-the-photosynthesis-reaction.md."""

LESSON = {
    "slug": "the-photosynthesis-reaction",
    "start": {
        "setup": "Van Helmont grew a willow tree in a pot of soil for five years.",
        "question": "If you had to guess, was the soil much lighter, or about the same?",
        "options": [
            ("A lot lighter", "Almost the same. The soil lost about 57 g, but the tree gained about 74 kg."),
            ("Almost the same", "Almost the same. The soil lost about 57 g, but the tree gained about 74 kg."),
        ],
        "answer": 1,
    },
    "words": ["photosynthesis", "reactant", "product", "chlorophyll"],
    "word_defs": {
        "photosynthesis": "How plants make glucose from carbon dioxide and water, using light energy.",
        "reactant": "A substance used up in a reaction. It goes on the left of the arrow.",
        "product": "A substance made in a reaction. It goes on the right of the arrow.",
        "chlorophyll": "The green pigment in chloroplasts. It absorbs light energy.",
    },
    "knowledge": [
        {"kind": "card", "title": "The word summary",
         "body": [{"figure": "b7-word-summary"},
                  "Carbon dioxide and water are the reactants.",
                  "Glucose and oxygen are the products.",
                  "Light is not a reactant. It gives the energy, so it goes above the arrow."]},
        {"kind": "card", "title": "Where photosynthesis happens",
         "body": ["Photosynthesis happens mainly in the leaves, inside chloroplasts.",
                  "Chloroplasts contain chlorophyll, a green pigment.",
                  "Chlorophyll absorbs the light energy the reaction needs."]},
        {"kind": "reveal", "title": "Where each substance comes from and goes",
         "cols": ["Reactant or product", "Comes from or goes to"],
         "rows": [
             ("Carbon dioxide", "Reactant", "From the air, through tiny holes in the leaf called stomata"),
             ("Water", "Reactant", "From the soil, through the roots"),
             ("Glucose", "Product", "Stays in the plant, to be used or stored"),
             ("Oxygen", "Product", "Out of the leaf through the stomata, into the air"),
         ]},
        {"kind": "card", "title": "What the plant does with glucose",
         "body": ["Glucose is a sugar. It is a store of energy.",
                  {"points": ["It is used in respiration to release energy.",
                              "It is turned into starch and stored.",
                              "It is used to make cellulose for new cell walls."]}]},
        {"kind": "card", "title": "What a plant takes from the soil",
         "body": ["Roots take in water and mineral nutrients from the soil.",
                  "Minerals are needed in small amounts to keep the plant healthy.",
                  "For example, a plant needs magnesium to make chlorophyll.",
                  "Minerals are not food. A plant makes its own food by photosynthesis."]},
        {"kind": "card", "title": "Where a plant's mass comes from",
         "body": ["Van Helmont's tree gained about 74 kg. The soil lost only about 57 g.",
                  "So the tree was not built from the soil.",
                  "Dry mass is the mass left when all the water is removed.",
                  "Most of a plant's dry mass is built from carbon dioxide from the air."]},
        {"kind": "card", "title": "Showing that light is needed",
         "body": ["A plant stores the glucose it makes as starch.",
                  "Iodine solution turns from orange-brown to blue-black when starch is there.",
                  "First, destarch a plant by keeping it in the dark for two days.",
                  "Cover part of one leaf with foil. Leave the plant in the light for a day.",
                  "The uncovered part turns blue-black with iodine. It made starch.",
                  "The covered part stays orange-brown. It made none.",
                  "So light is needed for photosynthesis."]},
        {"kind": "card", "title": "Showing that chlorophyll is needed",
         "body": ["A variegated leaf is green in some parts and white in others.",
                  "The white parts have no chlorophyll.",
                  "Destarch the plant. Then leave it in the light for a day.",
                  "Only the green parts turn blue-black with iodine.",
                  "Both parts are on one leaf. They get the same light, water and carbon dioxide.",
                  "So chlorophyll is needed for photosynthesis."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Plants get their food from the soil.",
              "Plants make their own food, glucose, by photosynthesis."),
             ("Light is a reactant.",
              "Light gives the energy. It is written above the arrow."),
             ("Photosynthesis makes energy.",
              "Energy cannot be made. Energy from light is stored in glucose."),
         ]}]},
    ],
    "key_fact": "Photosynthesis happens in the chloroplasts of leaves. Carbon dioxide and water react "
                "to make glucose and oxygen. Chlorophyll absorbs the light energy the reaction needs.",
    "deeper": [
        {"kind": "card", "title": "Why growers add carbon dioxide",
         "body": ["Air is only about 0.04% carbon dioxide.",
                  "In a bright, warm, well-watered greenhouse, this often holds growth back.",
                  "So growers pump extra carbon dioxide into their greenhouses.",
                  "At GCSE, you will call this a limiting factor."]},
        {"kind": "card", "title": "Plants respire too",
         "body": ["Plants respire all the time, day and night.",
                  "In bright light, photosynthesis is faster than respiration.",
                  "So in bright light a plant gives out more oxygen than it takes in."]},
        {"kind": "card", "title": "What van Helmont got wrong",
         "body": ["Van Helmont thought his tree was made from the water he gave it.",
                  "He did not know that carbon dioxide in the air was involved.",
                  "Later scientists showed that the carbon came from the air."]},
    ],
    "try": None,
    "figure_caption": {"b7-word-summary": None},      # the card text already says it
    "ladder_stem": {
        "recall": "Which line shows the reactants and products of photosynthesis?",
        "apply": "A sunflower seed of 0.1 g grows into a large plant. The plant is dried out. "
                 "Its dry mass is 300 g. Where did almost all of this dry mass come from?",
        "explain": "A leaf is green in the middle and white at the edges. The plant is kept in the dark "
                   "for two days. This destarches it. Then it is left in bright light for a day. "
                   "The leaf is tested with iodine. The middle turns blue-black. The edges stay "
                   "orange-brown. Explain these results. Say why one leaf is a fairer test than two "
                   "separate plants.",
        "produce": "A grower has tomatoes in a greenhouse. It is June, so it is bright and warm. The plants "
                   "have good soil and plenty of water. But the crop has stopped growing any faster. She "
                   "can buy one upgrade. Her choices are mineral feed, extra lights, carbon dioxide or bigger "
                   "pots. Which would you advise, and why? How would you test your advice first?",
    },
    "ladder_ticks": [
        ["Says the green parts therefore made glucose, which was stored as starch, so iodine turned blue-black there.",
         "Says the green parts made glucose and stored it as starch, so iodine turned blue-black."],
        ["Says the white parts made no glucose and so had no starch, leaving the iodine orange-brown.",
         "Says the white parts made no glucose, so had no starch. Iodine stayed orange-brown."],
        ["Says both parts had identical light, carbon dioxide, water and temperature because they are on one leaf, "
         "so chlorophyll is the only variable — which two plants could not guarantee.",
         "Says both parts had the same light, water, carbon dioxide and temperature. So chlorophyll "
         "is the only difference. Two plants could differ in other ways."],
        ["Identifies carbon dioxide as the most likely factor holding the rate back, because air is only about "
         "0.04% carbon dioxide while light, water and warmth are already plentiful in June.",
         "Picks the carbon dioxide supply. Light, water and warmth are already plentiful."],
        ["Rules out extra lighting on the grounds that light is already plentiful at that time of year.",
         "Rules out extra lights, because light is already plentiful in June."],
        ["Rules out more minerals and bigger pots by explaining that minerals are needed in tiny amounts and are "
         "not the raw material for photosynthesis.",
         "Rules out minerals and bigger pots, because the soil is already good."],
        ["Proposes testing on part of the greenhouse only, with the rest left unchanged as a comparison.",
         "Tests the upgrade on part of the greenhouse first, leaving the rest unchanged to compare."],
        ["Says the two sections must otherwise be treated identically, and that yield should be measured the same "
         "way in both.",
         "Keeps everything else the same in both parts, and measures the crop the same way."],
    ],
    "figures": [
        {"id": "b7-word-summary", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word summary for photosynthesis",
         "desc": "Carbon dioxide plus water at the top, labelled reactants. A drawn arrow points down to "
                 "glucose plus oxygen, labelled products. The words light energy sit beside the arrow.",
         "caption": "The word summary for photosynthesis.",
         "eq": {"left": ["carbon dioxide", "water"], "right": ["glucose", "oxygen"], "over": "light energy"}},
    ],
    "ladder_feedback": {
        "recall": {
            0: "That is respiration. It has the same substances, the other way round.",
            1: "Light is needed, but it is not a reactant. It goes above the arrow.",
            2: "Minerals are not a reactant. The reactants are carbon dioxide and water.",
        },
        "apply": {
            1: "The soil hardly loses any mass. Van Helmont showed this with his willow.",
            2: "Water supplies only a small part of the dry mass. Most comes from carbon dioxide.",
            3: "Light carries energy, not mass. It cannot become plant material.",
        },
    },
}
