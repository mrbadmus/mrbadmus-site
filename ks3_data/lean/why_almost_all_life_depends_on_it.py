# -*- coding: utf-8 -*-
"""Why almost all life depends on it, in the lean shape. Spec table: docs/lessons/wave1/ks3-why-almost-all-life-depends-on-it.md."""

LESSON = {
    "slug": "why-almost-all-life-depends-on-it",
    "start": {
        "setup": "A mushroom is not green. It grows on rotting wood, often in the dark.",
        "question": "If you had to guess, where does a mushroom's food come from?",
        "options": [
            ("Food a plant made", "Food a plant made. It feeds on dead plant material, which a plant built."),
            ("Food it makes itself", "Food a plant made. It feeds on dead plant material, which a plant built."),
        ],
        "answer": 0,
    },
    "words": ["producer", "consumer", "algae", "decomposer"],
    "word_defs": {
        "producer": "An organism that makes its own food by photosynthesis.",
        "consumer": "An organism that gets its food by eating other organisms.",
        "algae": "Simple organisms that photosynthesise. Many live in water.",
        "decomposer": "A fungus or bacterium that feeds on dead material and breaks it down.",
    },
    "knowledge": [
        {"kind": "card", "title": "Producers and consumers",
         "body": ["A producer makes its own food by photosynthesis.",
                  "Plants and algae are producers.",
                  "Animals cannot make their own food. They are consumers.",
                  "Consumers get their food by eating other organisms."]},
        {"kind": "card", "title": "Food chains start with a producer",
         "body": [{"figure": "b7-food-chain-grass"},
                  "The arrows show the direction the energy moves.",
                  "Chlorophyll in the grass absorbs light. Photosynthesis stores its energy in glucose.",
                  "The cow uses much of this energy in respiration.",
                  "Only a small part is stored in its body and passed on."]},
        {"kind": "reveal", "title": "What photosynthesis does for life on Earth",
         "cols": ["What photosynthesis does", "Without photosynthesis"],
         "rows": [
             ("Food", "Makes glucose, an energy store that feeds food chains",
              "Food chains would have no energy coming in"),
             ("Oxygen", "Releases oxygen into the air",
              "Respiration would use up the oxygen, and none would replace it"),
             ("Carbon dioxide", "Takes carbon dioxide out of the air",
              "Carbon dioxide from respiration and burning would keep building up"),
         ]},
        {"kind": "card", "title": "Algae count too",
         "body": ["Tiny algae called phytoplankton float near the surface of the sea.",
                  "They photosynthesise, just like plants.",
                  "About half of the world's photosynthesis happens in the sea.",
                  "So most sea food chains start with algae."]},
        {"kind": "card", "title": "Decomposers depend on it too",
         "body": ["A mushroom is a fungus. It has no chlorophyll, so it cannot photosynthesise.",
                  "It feeds on dead plant material.",
                  "That material was built by photosynthesis, so the mushroom depends on it too.",
                  "Fungi and bacteria that feed on dead material are decomposers."]},
        {"kind": "card", "title": "Coal is ancient sunlight",
         "body": ["Coal formed from plants that died hundreds of millions of years ago.",
                  "They were buried before they could rot.",
                  "The carbon in coal came from carbon dioxide in the air back then.",
                  "The energy in coal was captured from sunlight by those plants.",
                  "Burning coal puts that carbon dioxide back into the air."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Plants make oxygen for animals to breathe.",
              "Oxygen is a waste product. Plants and animals both use it in respiration."),
             ("Only plants photosynthesise.",
              "Algae do too. About half of all photosynthesis happens in the sea."),
             ("A producer is at the top of a food chain.",
              "A producer is always at the start of a food chain."),
         ]}]},
    ],
    "key_fact": "Almost all life depends on photosynthesis. Plants and algae use sunlight to build "
                "glucose, an energy store for food chains. Photosynthesis also adds oxygen to the air "
                "and removes carbon dioxide.",
    "deeper": [
        {"kind": "card", "title": "Life without sunlight",
         "body": ["Deep in the ocean, no light reaches the sea floor.",
                  "Near hot vents there, some bacteria make food using energy from chemical reactions.",
                  "Whole communities of animals feed on them.",
                  "So not quite all life depends on photosynthesis."]},
    ],
    "try": None,
    "ks4_becomes": "Trophic levels, biomass, the carbon cycle, and how humans change carbon dioxide levels.",
    "figure_caption": {"b7-food-chain-grass": None},      # the card text already says it
    "ladder_stem": {
        "produce": "People call coal “ancient sunlight”. Explain what that means. Say where the "
                   "carbon in coal came from. Say what burning coal does to the air.",
    },
    "ladder_ticks": [
        ["Says light energy from the Sun was absorbed by chlorophyll in grass leaves.",
         "Says chlorophyll in the grass, or other plants the cow ate, absorbed light energy."],
        ["Says photosynthesis used that energy to build glucose from carbon dioxide and water — so the "
         "grass is the producer.",
         "Says photosynthesis used it to build glucose, so the grass is the producer."],
        ["Says the cow ate the grass and used some of that energy, storing the rest in its own tissues.",
         "Says the cow ate the grass and stored some of the energy in its body."],
        ["Says most of what the cow ate was released again by respiration rather than passed on, which is why "
         "a field feeds far more people as wheat than as beef.",
         "Says the cow used much of the energy in respiration, so less was passed on."],
        ["Says the carbon in those plants came from carbon dioxide in the atmosphere of the time.",
         "Says the carbon in those plants came from carbon dioxide in the air then."],
        ["Says the plant material was buried before it could fully decay, so the carbon was locked away "
         "instead of returning to the air.",
         "Says the plants were buried before they could rot, so the carbon stayed locked away."],
        ["Says burning it returns that carbon dioxide to the atmosphere — releasing in a moment what was "
         "removed over millions of years, faster than photosynthesis can take it back out.",
         "Says burning coal quickly puts that carbon dioxide back into the air."],
    ],
    "figures": [
        {"id": "b7-food-chain-grass", "kind": "diagram", "status": "drawn", "art": "food-chain",
         "title": "A food chain: grass, cow, human",
         "desc": "Three boxes one above another, joined by arrows pointing down. Grass at the top, "
                 "labelled producer. Then cow, labelled consumer. Then human, labelled consumer. "
                 "The first arrow is labelled energy.",
         "caption": "A food chain starts with a producer.",
         "chain": [["grass", "producer"], ["cow", "consumer"], ["human", "consumer"]],
         "arrow_label": "energy"},
    ],
    "ladder_feedback": {
        "recall": {
            1: "Oxygen is a waste product. A producer makes its own food.",
            2: "Producer is about making food, not about offspring.",
            3: "A producer is at the start of a food chain, not the top.",
        },
        "apply": {
            0: "A mushroom digests food it did not make. It cannot photosynthesise.",
            1: "Minerals are not food. The mushroom feeds on dead plant material.",
            3: "Dead plant material was still built by photosynthesis.",
        },
    },
}
