# -*- coding: utf-8 -*-
"""Testing a leaf for starch, in the lean shape. Spec table: docs/lessons/wave1/ks3-testing-a-leaf-for-starch.md."""

LESSON = {
    "slug": "testing-a-leaf-for-starch",
    "start": {
        "setup": "In the starch test, the leaf is boiled in ethanol, an alcohol.",
        "question": "If you had to guess, does the alcohol remove the green, or clean the leaf?",
        "options": [
            ("To remove its green", "To remove its green. Ethanol dissolves the chlorophyll, so the colour change can be seen."),
            ("To wash it clean", "To remove its green. Ethanol dissolves the chlorophyll, so the colour change can be seen."),
        ],
        "answer": 0,
    },
    "words": ["starch", "iodine solution", "destarch", "ethanol"],
    "word_defs": {
        "starch": "The store of glucose in a plant. It does not dissolve in water.",
        "iodine solution": "An orange-brown liquid. It turns blue-black when starch is there.",
        "destarch": "Keep a plant in the dark so it uses up its stored starch.",
        "ethanol": "A kind of alcohol. Hot ethanol dissolves chlorophyll out of a leaf.",
    },
    "knowledge": [
        {"kind": "card", "title": "Why the test looks for starch",
         "body": ["Photosynthesis makes glucose. Glucose dissolves and is used up quickly.",
                  "The plant joins glucose together to make starch, and stores it.",
                  "Starch does not dissolve, so it stays in the leaf.",
                  "So starch in a destarched leaf shows it photosynthesised during the experiment."]},
        {"kind": "reveal", "title": "The method, step by step",
         "cols": ["How", "Why"],
         "rows": [
             ("1. Destarch the plant", "Keep it in the dark for two days",
              "It uses up its starch. Any starch found later is new."),
             ("2. Boil the leaf in water", "For about a minute",
              "Kills the cells and lets the iodine get in"),
             ("3. Boil it in ethanol", "In a tube stood in a beaker of hot water",
              "Removes the chlorophyll, so the colour change can be seen"),
             ("4. Dip it in hot water", "For a few seconds",
              "Softens the brittle leaf so it can be spread flat"),
             ("5. Add iodine solution", "Spread the leaf on a white tile first",
              "Blue-black means starch. Orange-brown means no starch."),
         ]},
        {"kind": "card", "title": "Staying safe with ethanol",
         "body": ["Ethanol is highly flammable.",
                  "Never heat it over a Bunsen flame.",
                  "Turn the Bunsen off. Then stand the tube of ethanol in a beaker of hot water.",
                  "Wear eye protection."]},
        {"kind": "reveal", "title": "Testing what photosynthesis needs",
         "cols": ["How you take it away", "Result"],
         "rows": [
             ("Light", "Cover part of a leaf with foil", "The covered part stays orange-brown"),
             ("Carbon dioxide", "Seal the plant in a bag with soda lime, which absorbs carbon dioxide",
              "The leaves stay orange-brown"),
             ("Chlorophyll", "Use a variegated leaf, which has white parts", "The white parts stay orange-brown"),
         ]},
        {"kind": "card", "title": "Making it a fair test",
         "body": ["Start with destarched plants.",
                  "Take away one thing only. Keep everything else the same.",
                  "Compare with a leaf, or part of a leaf, that still has it.",
                  "For carbon dioxide, seal a second plant in a bag with no soda lime.",
                  "Keep both in the same light for the same time.",
                  "Only the leaf from the plant with carbon dioxide turns blue-black."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Iodine turns blue-black because it reacts with chlorophyll.",
              "Iodine tests for starch. The ethanol has already removed the chlorophyll."),
             ("You can test any leaf straight from the plant.",
              "Destarch the plant first. Otherwise old starch spoils the result."),
         ]}]},
    ],
    "key_fact": "Iodine solution turns from orange-brown to blue-black when starch is present. Starch "
                "in a destarched leaf shows it photosynthesised. Boil the leaf in ethanol, in a water "
                "bath, to remove the chlorophyll.",
    "deeper": [
        {"kind": "card", "title": "How destarching works",
         "body": ["In the dark, a plant cannot photosynthesise.",
                  "It still respires, so it breaks down its stored starch.",
                  "After two days, the leaves have almost no starch left."]},
        {"kind": "card", "title": "The same test on food",
         "body": ["Iodine solution turns bread and potato blue-black too.",
                  "They contain starch that a plant made and stored."]},
    ],
    "try": None,
    "ladder_stem": {
        "apply": "A leaf is picked from a plant on a windowsill. The plant was not destarched. The "
                 "leaf is tested and goes blue-black. What does this show about when the starch was made?",
        "explain": "Write a method to find out if a leaf made starch during an experiment. Give a "
                   "reason for each step. "
                   "Include the safety point.",
        "produce": "Design an investigation to show that photosynthesis needs carbon dioxide. Use the "
                   "starch test. Describe your two set-ups. Say what you keep the same. Say what result "
                   "would support your idea.",
    },
    "ladder_ticks": [
        ["Destarch the whole plant in the dark for about two days, and says this is so any starch found was "
         "made during the experiment.",
         "Destarch the plant in the dark for two days. Then any starch found is new."],
        ["Boil the leaf in water, and says this kills the cells and makes them permeable to iodine.",
         "Boil the leaf in water. This kills the cells and lets the iodine in."],
        ["Boil in ethanol, and says this removes the chlorophyll so the colour change can be seen.",
         "Boil in ethanol. This removes the chlorophyll, so the colour change can be seen."],
        ["Says the ethanol is heated in a water bath because it is highly flammable — no naked flame.",
         "Heats the ethanol in a water bath, with no flame. Ethanol is highly flammable."],
        ["Dip in hot water to soften, spread on a white tile, add iodine; blue-black means starch, orange-brown "
         "means none.",
         "Softens it in hot water, spreads it on a white tile, adds iodine. Blue-black means starch."],
        ["Puts one plant in a sealed container with soda lime to absorb the carbon dioxide, and one in a sealed "
         "container without it.",
         "Seals both plants in bags. Only one bag has soda lime to absorb carbon dioxide."],
        ["Leaves both in bright light for the same length of time, then tests a leaf from each in the same way.",
         "Leaves both in bright light for the same time. Tests a leaf from each the same way."],
        ["States the result that would support the hypothesis: blue-black from the plant with carbon dioxide, "
         "orange-brown from the one without.",
         "Expects blue-black from the plant with carbon dioxide, and orange-brown from the one without."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Boiling in water kills the cells. The ethanol removes the green.",
            1: "Starch does not dissolve in ethanol. The ethanol removes the chlorophyll.",
            3: "Germs do not affect this test. The green colour would hide the result.",
        },
        "apply": {
            0: "Starch is stored for days. It could have been made before today.",
            1: "Iodine tests for starch, not chlorophyll. The chlorophyll was removed.",
            2: "There was no comparison with a leaf kept in the dark.",
        },
    },
}
