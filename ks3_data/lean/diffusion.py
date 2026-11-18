# -*- coding: utf-8 -*-
"""Diffusion, in the lean shape. Spec table: docs/lessons/wave1/ks3-diffusion.md."""

LESSON = {
    "slug": "diffusion",
    "start": {
        "setup": "Perfume is opened at one end of a room. The air is completely still.",
        "question": "If you had to guess, will the smell ever reach the far end?",
        "options": [
            ("Yes, in the end",
             "It gets there in the end. The perfume particles spread out on their own."),
            ("No, it needs a draught",
             "It gets there in the end. The perfume particles spread out on their own."),
        ],
        "answer": 0,
    },
    "words": ["diffusion", "concentration", "random"],
    "word_defs": {
        "diffusion": "The net spreading of particles from a high concentration to a low one.",
        "concentration": "How many particles of a substance there are in a certain space.",
        "random": "With no pattern and no set direction.",
    },
    "knowledge": [
        {"kind": "card", "title": "What diffusion is",
         "body": [{"figure": "c1-spreading"},
                  "Particles in liquids and gases are always moving in random directions.",
                  "So they spread from where there are many to where there are few.",
                  "Nothing has to push them. Diffusion happens in liquids and in gases."]},
        {"kind": "card", "title": "Why more go one way",
         "body": ["Particles do not aim for empty space. Nothing attracts them there.",
                  "At first, many more particles are on the crowded side.",
                  "So more of them cross from that side than from the other.",
                  "The difference between the two is the net movement.",
                  "Suppose 480 cross to the right and 310 cross back.",
                  "The net movement is 170 to the right.",
                  "Once the spread is even, equal numbers cross each way. The particles keep moving."]},
        {"kind": "card", "title": "Why it is slow",
         "body": ["Gas particles move at hundreds of metres per second.",
                  "But a perfume particle collides with air particles billions of times a second.",
                  "Each collision sends it off in a new direction.",
                  "So its path is a long zigzag, and it gets across a room very slowly.",
                  "In a real room, draughts carry a smell most of the way."]},
        {"kind": "card", "title": "Faster when warmer",
         "body": ["In a warmer liquid or gas, the particles move faster.",
                  "So diffusion happens faster.",
                  "Each particle still moves in random directions.",
                  "Diffusion is faster in a gas than in a liquid.",
                  "Gas particles move faster, with more space between them."]},
        {"kind": "card", "title": "Short distances only",
         "body": ["Diffusion is fast over tiny distances, such as across a cell.",
                  "It is very slow over long distances.",
                  "So every cell in your body is close to a blood vessel."]},
        {"kind": "card", "title": "Brownian motion",
         "body": [{"figure": "c1-brownian"},
                  "Under a microscope, specks of smoke in air jiggle at random. This is Brownian motion.",
                  "Air particles hit each speck from every side.",
                  "The air particles are far too small to see. Only the specks can be seen.",
                  "At any moment, more hit one side than the other, so the speck is pushed.",
                  "It is evidence that gas particles are always moving."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Diffusion needs a draught or stirring.",
              "Particles spread on their own. Stirring moves whole parts of a liquid at once.", "PART-10"),
             ("Particles move to fill the empty space on purpose.",
              "They move at random, in all directions. More start on the crowded side, so more leave it.", "PART-11"),
             ("When the colour is even, the particles stop.",
              "They keep moving. Equal numbers cross each way."),
             ("Heating changes the direction particles move.",
              "It makes them faster. Their directions stay random."),
         ]}]},
    ],
    "key_fact": "Diffusion is caused by the particles' own random movement. Nothing needs to push them. "
                "More particles leave a crowded place than arrive, so they spread out.",
    "deeper": [
        {"kind": "card", "title": "Pollen in water",
         "body": ["In 1827 Robert Brown saw tiny grains from pollen jiggling in water.",
                  "Nobody could explain it for almost eighty years.",
                  "In 1905 Einstein showed that water particles hitting the grains would cause it.",
                  "Measurements soon matched his predictions. This was strong evidence that atoms exist."]},
    ],
    "try": None,
    "ladder_stem": {
        "explain": "Perfume particles move at hundreds of metres per second. Yet diffusion alone is slow "
                   "across a room. Explain how they move through the air, and why it is so slow.",
        "produce": "A drop of food colouring goes into cold water. An identical drop goes into hot water. "
                   "The hot one spreads much faster. Explain why. Then explain why the cold one still "
                   "spreads completely if you wait.",
    },
    "ladder_ticks": [
        ["Says each collision sends them off in a new direction, so the path is not straight.",
         "Says each collision sends it off in a new direction, so its path zigzags."],
        ["Says the actual distance travelled is enormous compared with the straight-line distance across the room.",
         "Says its zigzag path is far longer than the straight line across the room."],
        ["Says faster movement means the colouring is jostled further in a given time.",
         "Says faster movement spreads the colouring further in the same time."],
        ["Says neither needs stirring — stirring is a different process that moves whole regions of liquid at once.",
         "Says neither needs stirring. Stirring moves whole parts of the liquid at once."],
    ],
    "figures": [
        {"id": "c1-spreading", "kind": "diagram", "status": "drawn",
         "art": "particle-picture",
         "title": "Dye particles spreading through water",
         "desc": "Three boxes, one above the other, each holding sixteen dye particles drawn as coloured "
                 "circles. In the top box, labelled At the start, they are crowded together at the left "
                 "end. In the middle box, labelled Later, they are spread over the left two thirds, more "
                 "of them towards the left. In the bottom box, labelled Evened out, they are spread evenly "
                 "across the whole box. Under the top two boxes, an arrow points right, labelled Net movement.",
         "caption": "The particles spread from a high concentration to a low concentration.",
         "data": {"boxes": [
             {"label": "At the start", "layout": "spread", "n": 16, "where": "left", "net_arrow": "Net movement"},
             {"label": "Later", "layout": "spread", "n": 16, "where": "middle", "net_arrow": "Net movement"},
             {"label": "Evened out", "layout": "spread", "n": 16, "where": "even"},
         ]}},
        {"id": "c1-brownian", "kind": "diagram", "status": "drawn",
         "art": "brownian-path",
         "title": "The path of a smoke speck in air",
         "desc": "A box holding one larger shaded circle, labelled Smoke speck, with small plain circles, "
                 "labelled Air particles, scattered through the box. Behind the speck, a dotted line of "
                 "short straight steps changes direction at random, showing the path it has taken. The "
                 "two labels sit under the box, each joined to its part by a short line.",
         "caption": "Air particles hit the speck unevenly, so it moves in a random path.",
         "data": {"speck_label": "Smoke speck", "air_label": "Air particles", "steps": 14, "air": 18}},
    ],
    "figure_caption": {"c1-spreading": None,     # the key word above it says it
                       "c1-brownian": "Not to scale. The air particles are thousands of times smaller and cannot be seen."},
    "ladder_feedback": {
        "recall": {
            0: "Warmth changes how fast diffusion happens. It does not set the direction.",
            1: "Height does not matter. Diffusion goes from crowded to less crowded, in any direction.",
            2: "Mass changes how fast particles move. It does not set the direction.",
        },
        "apply": {
            1: "Particles never stop moving. Equal numbers now cross each way.",
            2: "Water particles keep hitting the dye particles, so they keep moving.",
            3: "Their movement stays random, in every direction.",
        },
    },
}
