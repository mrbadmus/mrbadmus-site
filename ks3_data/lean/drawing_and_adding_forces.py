# -*- coding: utf-8 -*-
"""Drawing and adding forces, in the lean shape. Spec table: docs/lessons/wave1/ks3-drawing-and-adding-forces.md."""

LESSON = {
    "slug": "drawing-and-adding-forces",
    "start": {
        "setup": "A sledge sits on ice. One rope pulls it right with 40 N. Another pulls it left with 25 N.",
        "question": "If you had to guess, how hard is the sledge pulled overall?",
        "options": [
            ("15 N to the right",
             "15 N to the right. The 25 N pull cancels 25 N of the 40 N pull."),
            ("40 N to the right",
             "15 N to the right. The 25 N pull cancels 25 N of the 40 N pull."),
        ],
        "answer": 0,
    },
    "words": ["force arrow", "resultant force", "kilonewton"],
    "word_defs": {
        "force arrow": "An arrow that shows a force. Its length shows the size of the force.",
        "resultant force": "The single force that has the same effect as all the forces acting together.",
        "kilonewton": "1000 newtons. Its symbol is kN.",
    },
    "knowledge": [
        {"kind": "card", "title": "Drawing a force arrow",
         "body": [{"figure": "p4-sledge-arrows"},
                  "Draw each force as an arrow.",
                  "The arrow starts on the object the force acts on.",
                  "It points the way the force acts.",
                  "Its length shows the size, so a bigger force gets a longer arrow.",
                  "Label each arrow with its size in newtons."]},
        {"kind": "card", "title": "Drawing to scale",
         "body": ["Choose a scale, such as 1 cm for every 10 N.",
                  "Then a 40 N force is an arrow 4 cm long.",
                  "A 25 N force is an arrow 2.5 cm long.",
                  "Use the same scale for every arrow on one diagram."]},
        {"kind": "card", "title": "Forces in the same direction",
         "body": ["Forces that point the same way add up.",
                  "Two people push a car forwards, one with 200 N and one with 150 N.",
                  "The resultant force is 200 N + 150 N = 350 N forwards."]},
        {"kind": "card", "title": "Forces in opposite directions",
         "body": [{"figure": "p4-resultant-beam-recap"},
                  "Forces that point opposite ways subtract.",
                  "Take the smaller force away from the bigger one.",
                  "The resultant points the same way as the bigger force."]},
        {"kind": "card", "title": "Worked example: two units",
         "body": ["One tug pulls a barge right with 1.2 kN. Another pulls it left with 400 N. "
                  "Find the resultant force.",
                  {"points": ["Convert: 1.2 kN × 1000 = 1200 N",
                              "Formula: resultant = bigger force − smaller force",
                              "Insert: resultant = 1200 N − 400 N",
                              "Fine-tune: 1200 − 400 = 800",
                              "Answer: 800 N to the right"]},
                  "Always give the size, the unit and the direction."]},
        {"kind": "reveal", "title": "Find the resultant",
         "cols": ["Add or subtract", "Resultant"],
         "rows": [
             ("30 N right and 20 N right", "Same way, so add", "50 N to the right"),
             ("30 N right and 20 N left", "Opposite, so subtract", "10 N to the right"),
             ("500 N up and 700 N down", "Opposite, so subtract", "200 N down"),
             ("100 N forwards, with 30 N and 20 N backwards", "Add the two backward forces, then subtract",
              "50 N forwards"),
         ]},
        {"kind": "card", "title": "What the resultant does",
         "body": ["A resultant of 0 N means the forces are balanced.",
                  "With balanced forces, a still object stays still.",
                  "With balanced forces, a moving object keeps a steady speed in a straight line.",
                  "A resultant on a still object makes it start to move.",
                  "A resultant in the direction of motion makes the object speed up.",
                  "A resultant against the motion makes it slow down.",
                  "It keeps moving the same way while it slows.",
                  "A sideways resultant changes the direction of motion."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The bigger force wins, so the resultant is the bigger force.",
              "The smaller force cancels part of the bigger one. Only the difference is left."),
             ("Equal and opposite forces on one object stop existing.",
              "Both forces still act. Only their resultant is zero."),
             ("Draw every arrow the same length so the diagram looks tidy.",
              "A longer arrow means a bigger force. Draw the arrows to scale."),
             ("Kilonewtons and newtons can go straight into one sum.",
              "Change kilonewtons into newtons first. Multiply by a thousand."),
         ]}]},
    ],
    "key_fact": "Draw a force as an arrow. Its length shows the size, and it points the way the "
                "force acts. Forces in the same direction add. Forces in opposite directions subtract. "
                "The resultant force is what is left, with a size in newtons and a direction.",
    "deeper": [
        {"kind": "card", "title": "Where the arrow starts",
         "body": ["Two equal and opposite forces along one line give no resultant.",
                  "Push up on one side of a steering wheel and down on the other.",
                  "The forces are balanced, but the wheel turns.",
                  "So where each arrow starts is part of the diagram too."]},
        {"kind": "card", "title": "Free-body diagrams",
         "body": ["A diagram showing every force on one object is called a free-body diagram.",
                  "It leaves out the forces that object puts on other things."]},
    ],
    "try": None,
    "figure_caption": {
        "p4-resultant-beam-recap": "The 25 N pull cancels 25 N of the 40 N pull. 15 N is left.",
    },
    "figures": [
        {"id": "p4-sledge-arrows", "kind": "diagram", "status": "drawn", "art": "force-arrows",
         "title": "Two pulls on a sledge, drawn to scale",
         "desc": "A sledge drawn as a box. An arrow from its right side points right, labelled 40 N. An "
                 "arrow from its left side points left, labelled 25 N. The 40 N arrow is longer, in the "
                 "ratio 40 to 25. A scale bar below shows the length for 10 N.",
         "caption": "The 40 N pull and the 25 N pull, drawn to the same scale.",
         "data": {"layout": "one", "object": "Sledge", "scale_N": 10,
                  "arrows": [{"dir": "right", "N": 40, "label": "40 N"},
                             {"dir": "left", "N": 25, "label": "25 N"}]}},
    ],
    "ladder_stem": {
        "apply": "Two forces act on a box. One pushes it to the left with 30 N. The other pushes it "
                 "to the right with 30 N. What is true?",
        "explain": "A trolley is pulled forwards with 60 N. Friction drags it backwards with 20 N. "
                   "Work out the resultant force, with its size and direction. Explain why the friction "
                   "does not just disappear. Say what the resultant does to a trolley that starts at rest.",
        "produce": "A parachutist is falling. Gravity pulls down with 700 N. Air resistance pushes up "
                   "with 700 N. Then the parachutist pulls a cord and the parachute opens. Now the air pushes "
                   "up with 760 N. Work out the resultant force in each case. Say what happens to the "
                   "parachutist's motion each time.",
    },
    "ladder_ticks": [
        ["Says the friction is still acting: it cancels 20 N of the pull rather than vanishing.",
         "Says friction still acts. It cancels 20 N of the pull."],
        ["Says a resultant of 40 N forwards makes a trolley at rest start to move forwards and speed up.",
         "Says the 40 N forwards resultant makes the trolley start moving and speed up."],
        ["Says the direction of the resultant is upwards in the second case, using the direction of the bigger force.",
         "Says the second resultant is upwards, the direction of the bigger force."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "That is 90 + 34. Forces pointing opposite ways subtract.",
            1: "The size is right. The resultant points the way of the bigger force, forwards.",
            3: "Friction still acts. It cancels 34 N of the push.",
        },
        "apply": {
            0: "Both forces act, but they are equal and opposite. The resultant is 0 N, so a still box stays still.",
            1: "Opposite forces subtract. 30 N − 30 N = 0 N.",
            2: "Both forces still act. Only the resultant is 0 N.",
        },
    },
}
