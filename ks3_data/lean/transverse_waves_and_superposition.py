# -*- coding: utf-8 -*-
"""Transverse waves and superposition, in the lean shape.
Spec table: docs/lessons/wave2/ks3-transverse-waves-and-superposition.md."""

LESSON = {
    "slug": "transverse-waves-and-superposition",
    "start": {
        "setup": "Drop two stones into still water at the same moment, a metre apart. "
                 "Two sets of rings spread out and run into each other.",
        "question": "If you had to guess, where two ripples meet, do they add "
                    "together, or bounce off each other?",
        "options": [
            ("Add together",
             "Yes. Where they overlap, their heights add. Two lifts make a bigger lift."),
            ("Bounce off each other",
             "Ripples pass through each other. Where they overlap, their heights add."),
        ],
        "answer": 0,
    },
    "words": ["transverse", "displacement", "reflection", "superposition"],
    "word_defs": {
        "transverse": "A wave where the material moves at right angles to the direction of travel.",
        "displacement": "How far the surface is above or below the rest line at one point.",
        "reflection": "A wave bouncing back off a barrier.",
        "superposition": "Adding the displacements of two waves where they overlap.",
    },
    "knowledge": [
        {"kind": "card", "title": "Transverse waves",
         "body": [{"figure": "p6-02-transverse"},
                  "In a transverse wave, the material moves at right angles to the direction of travel.",
                  "On water, the surface moves up and down. The wave moves across.",
                  "A rope shaken up and down carries a transverse wave too.",
                  "Light is also a transverse wave."]},
        {"kind": "card", "title": "Displacement",
         "body": ["Displacement is how far the surface is from the rest line at one point.",
                  "Above the rest line counts as up. Below it counts as down.",
                  "At a crest, the displacement is the same as the amplitude."]},
        {"kind": "card", "title": "Waves reflect",
         "body": ["A wave that hits a barrier bounces back. This is reflection.",
                  "The reflected wave travels back the other way.",
                  "It keeps the same wavelength."]},
        {"kind": "card", "title": "When two waves meet",
         "body": [{"figure": "p6-02-superpose"},
                  "Where two waves overlap, their displacements add. This is superposition.",
                  "Crest on crest makes a bigger crest. The waves add.",
                  "Crest on trough of the same size makes flat water. The waves cancel.",
                  "After they pass, both waves carry on as they were."]},
        {"kind": "card", "title": "Worked example: crest on crest",
         "body": ["Two ripples meet crest on crest. One is 8 mm high and the other is 5 mm. "
                  "Find the height of the water where they meet.",
                  {"points": ["Convert: nothing. Both heights are in millimetres.",
                              "Formula: height where they meet = first height + second height",
                              "Insert: height = 8 mm + 5 mm",
                              "Fine-tune: 8 + 5 = 13",
                              "Answer: height = 13 mm"]},
                  "For crest on trough, take the smaller height away from the bigger one."]},
        {"kind": "card", "title": "Worked example: different units",
         "body": ["A crest 1.2 cm high meets a crest 7 mm high. Find the height where they meet.",
                  {"points": ["Convert: 1.2 cm × 10 = 12 mm",
                              "Formula: height where they meet = first height + second height",
                              "Insert: height = 12 mm + 7 mm",
                              "Fine-tune: 12 + 7 = 19",
                              "Answer: height = 19 mm"]},
                  "Add 1.2 to 7 without converting, and the answer is wrong."]},
        {"kind": "reveal", "title": "Add or cancel",
         "cols": ["Working", "Where they meet"],
         "rows": [
             ("Crest 5 mm on crest 3 mm", "5 + 3", "A crest 8 mm high"),
             ("Crest 5 mm on trough 5 mm", "5 − 5", "Flat water"),
             ("Crest 7 mm on trough 2 mm", "7 − 2", "A crest 5 mm high"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("When two waves cancel, they destroy each other.",
              "Both waves carry on past the overlap, unchanged.", "WAVE-05"),
             ("If the water is flat, the energy has gone.",
              "The energy is still there. It carries on with both waves.", "WAVE-06"),
             ("Two waves meeting take the average of their heights.",
              "Their displacements add. 8 mm on 5 mm makes 13 mm.", "WAVE-07"),
             ("The stronger wave wins, and the weaker one disappears.",
              "Both waves add where they meet. Then both carry on.", "WAVE-08"),
             ("A 1.2 cm crest on a 7 mm crest makes 8.2 mm.",
              "Change both to millimetres first. 12 mm + 7 mm = 19 mm."),
         ]}]},
    ],
    "key_fact": "Where two waves overlap, their displacements add, so crest on crest makes a bigger crest. "
                "A crest on an equal trough cancels it, and both waves then carry on.",
    "deeper": [
        {"kind": "card", "title": "Noise-cancelling headphones",
         "body": ["Superposition works for sound waves too.",
                  "Noise-cancelling headphones play a sound that cancels the noise outside.",
                  "Where the two waves meet, they add up to almost nothing."]},
        {"kind": "card", "title": "Reflection and superposition together",
         "body": ["Send waves down a tank with a wall at the far end.",
                  "The reflected waves run back through the waves still coming in.",
                  "Where they overlap, some points stay still and others move a lot."]},
    ],
    "try": {"label": "Wave Motion Lab", "href": "/simulations/physics/wave-motion-lab/"},
    "tutor_body": "Got a pattern of crossing ripples you cannot explain?",
    "connects_heading": None,
    "ks4_becomes": "The wave equation and wave speed. GCSE Physics adds reflection at a boundary.",
    "figures": [
        {"id": "p6-02-transverse", "kind": "diagram", "status": "drawn", "art": "p6-transverse-wave",
         "title": "A transverse wave",
         "desc": "A wave drawn on a dashed rest line, with an arrow along the top showing the direction "
                 "of travel, to the right. One point on the surface is marked with a dot. A double arrow "
                 "through the dot points up and down. Words under the wave say the surface moves up and "
                 "down, and the wave travels across, at right angles to this.",
         "caption": "The surface moves up and down. The wave travels across.",
         "data": {"show": "motion", "motion_label": "The surface moves up and down."}},
        {"id": "p6-02-superpose", "kind": "diagram", "status": "drawn", "art": "p6-superposition",
         "title": "Two waves adding and cancelling",
         "desc": "Two columns, drawn to one scale. Left, crest on crest: a wave 8 mm high and a wave 5 mm "
                 "high, crest lined up with crest. Where they meet, the water makes a wave 13 mm high. "
                 "Under it: 8 + 5 = 13 mm. Right, crest on trough: two waves each 6 mm high, one with its "
                 "crest where the other has its trough. Where they meet, the water is flat. "
                 "Under it: 6 minus 6 = 0 mm.",
         "caption": "Crest on crest adds. Crest on trough of the same size cancels.",
         "data": {"cases": [{"title": "Crest on crest", "a": 8, "b": 5, "sign": 1},
                            {"title": "Crest on trough", "a": 6, "b": 6, "sign": -1}]}},
    ],
    "figure_caption": {"p6-02-transverse": None, "p6-02-superpose": None},   # the card text already says it
    "ladder_ticks": [
        ["Says which patch is which depends on how far each ripple has had to travel to get there.",
         "Says flat patches are where one ripple's crest always meets the other's trough."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Waves do not average. Both lift the surface at once, so add the heights.",
            2: "Two waves acting at once are added. Multiplying them is never right.",
            3: "Subtract only for crest on trough. Crest on crest, the heights add.",
        },
        "apply": {
            0: "Waves are not destroyed. Both carry on past the overlap at 7 mm.",
            1: "The water is flat only where they overlap. Elsewhere each wave is still 7 mm.",
            3: "Waves do not absorb each other. Both carry on past the overlap at 7 mm.",
        },
    },
}
