# -*- coding: utf-8 -*-
"""Alveoli built for exchange, in the lean shape. Spec table: docs/lessons/pilot/ks3-alveoli-built-for-exchange.md."""

LESSON = {
    "slug": "alveoli-built-for-exchange",
    "start": {
        "setup": None,
        "question": "If you had to guess, how big is the inside surface of your lungs?",
        "options": [
            ("About the size of a desk",
             "About half a tennis court. Millions of tiny air sacs make a huge surface."),
            ("About half a tennis court",
             "About half a tennis court. Millions of tiny air sacs make a huge surface."),
        ],
        "answer": 1,
    },
    "words": ["alveolus", "diffusion", "capillary", "concentration"],
    "knowledge": [
        {"kind": "card", "title": "Gas exchange in the alveoli",
         "body": ["Air in the alveoli has a high concentration of oxygen.",
                  "Blood arriving at the lungs has a low concentration of oxygen.",
                  "So oxygen diffuses from the alveoli into the blood.",
                  "Carbon dioxide diffuses the other way, from the blood into the alveoli."]},
        {"kind": "reveal", "title": "How alveoli are adapted",
         "cols": ["The feature", "Why it helps"],
         "rows": [
             ("Large surface area", "About 500 million alveoli, around 70 m²",
              "More gas can diffuse at once"),
             ("Thin walls", "Each alveolus has a wall one cell thick",
              "Gases have a short distance to diffuse"),
             ("Good blood supply", "Each alveolus is wrapped in capillaries",
              "Blood carries oxygen away, which keeps the concentration difference high"),
             ("Moist lining", "A thin film of liquid lines each alveolus",
              "Gases dissolve before they diffuse across"),
         ]},
        {"kind": "card", "title": "Why breathing and blood flow both matter",
         "body": ["Breathing brings fresh air into the alveoli.",
                  "Blood flow carries oxygen away from them.",
                  "Together they keep the concentration difference high.",
                  "If either one stops, oxygen stops entering the blood overall."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Oxygen is pumped into the blood.",
              "Oxygen moves by diffusion. No pump is involved."),
             ("Oxygen moves because it wants to spread out.",
              "Particles move randomly. More cross from the high concentration side."),
             ("Gases only cross in one direction.",
              "Particles cross both ways. The overall movement follows the concentration "
              "difference."),
         ]}]},
    ],
    "key_fact": "Alveoli have a large surface area, thin walls and a good blood supply. Oxygen "
                "diffuses into the blood and carbon dioxide diffuses out.",
    "deeper": [
        {"kind": "card", "title": "The same features in the gut",
         "body": ["The small intestine absorbs food in the same way.",
                  "It also has a large surface area, thin walls and a good blood supply."]},
        {"kind": "card", "title": "High up a mountain",
         "body": ["Air on a mountain is still 21% oxygen.",
                  "But the air is less dense, so each breath holds less oxygen.",
                  "The concentration difference is smaller, so less oxygen diffuses into the blood.",
                  "Breathing faster helps a little, but it cannot make the air denser."]},
    ],
    "try": None,
    "ladder_feedback": {
        "recall": {
            0: "The volume is the same in this question. Only the surface is different.",
            1: "Mass does not matter here. Surface area does.",
            2: "Air is replaced about twelve times a minute, so it is not stored.",
        },
        "apply": {
            0: "The particles keep moving and keep crossing the wall.",
            1: "Particles do not try to do anything. Oxygen now crosses equally both ways.",
            3: "The wall is unchanged. The concentration difference has gone.",
        },
    },
    "ladder_stem": {
        "produce": "At the top of a high mountain the air still contains 21% oxygen, yet climbers "
                   "become short of oxygen. Using what you have learnt, explain why — and why "
                   "breathing faster helps a little but does not solve it.",
    },
}
