# -*- coding: utf-8 -*-
"""The particle model, in the lean shape. Spec table: docs/lessons/wave1/ks3-particle-model.md."""

LESSON = {
    "slug": "particle-model",
    "start": {
        "setup": "Mix 50 ml of water with 50 ml of alcohol. The total is about 97 ml.",
        "question": "If you had to guess, where did the missing 3 ml go?",
        "options": [
            ("It evaporated away",
             "Nothing is lost. The small particles of one liquid fit into gaps between the other's."),
            ("It squeezed into gaps",
             "Nothing is lost. The small particles of one liquid fit into gaps between the other's."),
        ],
        "answer": 1,
    },
    "words": ["particle", "matter", "model"],
    "word_defs": {
        "particle": "A tiny piece of matter, far too small to see.",
        "matter": "Anything that has mass and takes up space.",
        "model": "A simple picture that helps explain something we cannot see.",
    },
    "knowledge": [
        {"kind": "card", "title": "The particle model",
         "body": ["The particle model says three things about all matter.",
                  {"points": ["It is made of tiny particles, far too small to see.",
                              "There is empty space between the particles.",
                              "The particles are always moving."]},
                  "The particles can be atoms or molecules. You meet these in the next unit."]},
        {"kind": "card", "title": "Gaps between particles",
         "body": [{"figure": "c1-mixing"},
                  "Alcohol particles are bigger than water particles.",
                  "If the gaps were already full, 50 ml and 50 ml would make 100 ml."]},
        {"kind": "reveal", "title": "Evidence for the model",
         "cols": ["What it shows"],
         "rows": [
             ("Water and alcohol mix to less than 100 ml", "There are gaps between particles"),
             ("A gas can be squashed into a smaller space", "A gas is mostly empty space"),
             ("A smell spreads across a still room", "Particles move on their own"),
         ]},
        {"kind": "card", "title": "Nothing between the particles",
         "body": ["The gaps between particles hold nothing at all.",
                  "Air in the gaps would itself be particles, with gaps of its own.",
                  "So each gap is empty space, far too small to see.",
                  "Squashing a gas makes these empty spaces smaller. The particles stay the same."]},
        {"kind": "card", "title": "How far can you cut",
         "body": ["Cut a sugar cube so each piece is half as wide as the last.",
                  "After about 24 of these halvings, the piece is one sugar particle.",
                  "Near the end, the piece is only a few particles across.",
                  "A sugar particle can be broken up, but only by a chemical change.",
                  "What comes out is new substances. It is no longer sugar.",
                  "So one particle is the smallest possible piece of sugar."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The gaps between particles are full of air.",
              "Air is made of particles too. The gaps hold nothing.", "PART-02"),
             ("A sharper knife could cut sugar smaller forever.",
              "One particle is the smallest piece of sugar.", "PART-01"),
             ("Matter is all one piece, with no gaps in it.",
              "Matter is made of separate particles with empty space between them."),
         ]}]},
    ],
    "key_fact": "All matter is made of particles, far too small to see. There is empty space "
                "between the particles, and they are always moving.",
    "deeper": [
        {"kind": "card", "title": "An old idea",
         "body": ["Around 400 BC, Democritus argued that cutting must stop somewhere.",
                  "He called the last piece atomos, which means uncuttable.",
                  "He had no evidence. Measurements came over two thousand years later."]},
        {"kind": "card", "title": "How small",
         "body": ["A sugar particle is about a millionth of a millimetre across.",
                  "A human hair is about a hundred thousand times wider."]},
    ],
    "try": None,
    "before_this": "Nothing. This is where the unit starts.",
    "ladder_stem": {
        "explain": "Water and alcohol, 50 ml of each, make about 97 ml, not 100 ml. Explain why, "
                   "using the particle model.",
        "produce": "A student says the gaps between gas particles must be full of air. \"Otherwise there "
                   "would be a vacuum in there,\" they say. \"You cannot have a vacuum in the middle of a "
                   "room.\" Reply to them.",
    },
    "ladder_ticks": [
        ["Says no particles are lost or destroyed — the total amount of matter is unchanged.",
         "Says no particles are lost or destroyed. The amount of matter is unchanged."],
        ["Says the volume drops because the particles pack more closely, not because anything disappears.",
         "Says the volume drops because the particles pack more closely."],
        ["Says that filling the gaps with air only pushes the same question down a level, and never ends.",
         "Says air in the gaps would need gaps of its own, forever."],
        ["Uses evidence: a gas can be squashed, which would be impossible if the space were already full.",
         "Uses evidence: a gas can be squashed. It could not be if the gaps were full."],
        ["Notes that this is not a vacuum you could stand in — each empty space is far too small for anything to be 'in', millions of times thinner than a hair.",
         "Says the gaps are tiny. There is no big vacuum in the room."],
    ],
    "figures": [
        {"id": "c1-mixing", "kind": "diagram", "status": "drawn",
         "art": "particle-picture",
         "title": "Water and alcohol particles, before and after mixing",
         "desc": "Three boxes, one above the other, each holding plain circles. The top box, labelled "
                 "Alcohol, holds large circles touching in a jumble, with a line under it reading 50 ml. "
                 "The middle box, labelled Water, holds small circles touching in a jumble, with 50 ml "
                 "under it. The bottom box, labelled Mixed, holds the same number of large circles mixed "
                 "with the small circles, which sit in the gaps between them. A dashed line labelled "
                 "100 ml marks where the two levels above would add up to, and the mixture stands below "
                 "it. Words inside the box say Drop exaggerated. The line under it reads About 97 ml, "
                 "not 100 ml.",
         "caption": "The small particles fit into gaps between the big ones.",
         "data": {"boxes": [
             {"label": "Alcohol", "layout": "liquid", "size": "big", "n": 12, "count": "50 ml"},
             {"label": "Water", "layout": "liquid", "size": "small", "n": 23, "count": "50 ml"},
             {"label": "Mixed", "layout": "mix", "big": 12, "small": 23,
              "sum_label": "100 ml", "note": "Drop exaggerated",
              "count": "About 97 ml, not 100 ml"},
         ]}},
    ],
    "figure_caption": {"c1-mixing": None},      # the Start reply already says it
    "ladder_feedback": {
        "recall": {
            1: "Air is made of particles too. Its particles would have gaps of their own.",
            2: "Any gas is made of particles with gaps between them. The gaps hold nothing.",
            3: "Dust is made of particles too. Between particles there is only empty space.",
        },
        "apply": {
            0: "Particles can be split. But splitting a sugar particle makes new substances.",
            1: "Hardness belongs to a lump of sugar, not to one particle.",
            3: "Every particle has mass. Splitting one makes new substances, not smaller sugar.",
        },
    },
}
