# -*- coding: utf-8 -*-
"""Electric motors, in the lean shape. Rebuilt from the old format.
Spec table: ks4-electric-motors.md.

AQA 6.7.2.3 (8464) / 4.7.2.3 (8463), HT only. The lesson exists on CH and TH only, and the
wording is the same in both specs, so no card is route-specific.

The split-ring commutator is not a spec sentence. It is taught here because it is the standard
answer to why a d.c. motor keeps turning the same way, and Rainford's SOW lists it as a key word.
No rung or quiz question tests it (it is not on 8464, and the quiz is served on CH)."""

LESSON = {
    "slug": "electric-motors",
    "start": {
        "setup": "A coil of wire carrying a current sits between the poles of a magnet.",
        "question": "If you had to guess, what does the coil do?",
        "options": [
            ("It turns",
             "It turns. The forces on its two sides act in opposite directions."),
            ("It stays still",
             "It turns. The forces on its two sides act in opposite directions."),
        ],
        "answer": 0,
    },
    "words": ["motor effect", "coil", "split-ring commutator", "direct current (d.c.)"],
    "knowledge": [
        {"kind": "card", "title": "A coil in a magnetic field",
         "body": ["A coil of wire carrying a current in a magnetic field tends to rotate.",
                  "This is the basis of an electric motor.",
                  {"slot": "fig:dc-motor"},
                  "Look at the force on each side of the coil."]},
        {"kind": "card", "title": "Why the coil turns",
         "body": [{"points": [
             "The current flows along one side of the coil and back along the other side.",
             "So the current in the two sides flows in opposite directions.",
             "Each side is a conductor carrying a current in a magnetic field, so a force acts on "
             "each side. This is the motor effect.",
             "By Fleming's left-hand rule, the forces on the two sides act in opposite directions: "
             "one side is pushed up and the other side is pushed down.",
             "These two forces make the coil turn."]},
                  "For each side at right angles to the field, the size of the force is F = BIl."]},
        {"kind": "card", "title": "Keeping it turning: the split-ring commutator",
         "body": ["After half a turn, the two sides of the coil have swapped places.",
                  "If the current did not change, the forces would now turn the coil back the "
                  "other way.",
                  "The split-ring commutator reverses the current in the coil every half turn.",
                  "So the side of the coil next to each pole is always pushed the same way, and the "
                  "coil keeps turning in the same direction.",
                  "The brushes press against the commutator and connect it to the d.c. supply."]},
        {"kind": "card", "title": "Faster, or the other way",
         "body": ["The forces on the coil are bigger, so the motor turns faster, if you:",
                  {"points": ["increase the current",
                              "use a stronger magnet (a bigger magnetic flux density)",
                              "put more turns of wire on the coil"]},
                  "To make the motor turn the other way, reverse the current or reverse the "
                  "magnetic field."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Both sides of the coil are pushed the same way.",
              "The current in the two sides flows in opposite directions, so the forces act in "
              "opposite directions."),
             ("The commutator changes a.c. into d.c.",
              "The commutator reverses the current in the coil every half turn."),
             ("The magnet attracts the coil.",
              "The coil is copper, which is not a magnetic material. The force comes from the "
              "current in the magnetic field."),
         ]}]},
    ],
    "key_fact": "A coil of wire carrying a current in a magnetic field tends to rotate, which is the "
                "basis of an electric motor. The current flows in opposite directions along the two "
                "sides of the coil, so the forces on the two sides act in opposite directions and "
                "turn the coil.",
    "deeper": [
        {"kind": "card", "title": "Real motors",
         "body": ["A real motor has many coils wound on an iron core.",
                  "This gives a stronger and smoother turn than one coil."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: say which way the current flows in each side, which way "
             "each force acts, and that the forces turn the coil.",
             "<strong>Calculate</strong>: use F = BIl for one side of the coil.",
             "<strong>Describe</strong>: say what the motor does when you make a change.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give what a coil of wire carrying a current in a magnetic field tends to do.",
             "why": "A coil of wire carrying a current in a magnetic field tends to rotate. This is the basis of an electric motor.",
             "options": [
                 {"text": "Become a permanent magnet", "correct": False, "reply": "The coil only has a magnetic field while the current flows."},
                 {"text": "Stay still", "correct": False, "reply": "A force acts on each side of the coil."},
                 {"text": "Rotate", "correct": True},
                 {"text": "Heat the magnet", "correct": False, "reply": "The forces on the coil make it turn."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give how the direction of the current in one side of a motor coil compares with the other side.",
             "why": "The current flows along one side and back along the other, so the directions are opposite.",
             "options": [
                 {"text": "Opposite", "correct": True},
                 {"text": "The same", "correct": False, "reply": "The current goes along one side and comes back along the other."},
                 {"text": "Current flows in one side only", "correct": False, "reply": "The coil is one loop, so the same current flows through both sides."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "The current in an electric motor is reversed. Describe what happens to the coil.",
             "why": "Reversing the current reverses the force on each side, so the coil turns the other way.",
             "options": [
                 {"text": "It stops turning", "correct": False, "reply": "There is still a force on each side, so it still turns."},
                 {"text": "It turns the other way", "correct": True},
                 {"text": "It turns the same way, faster", "correct": False, "reply": "The size of the current has not changed, so the forces are the same size."},
                 {"text": "It turns the same way, at the same speed", "correct": False, "reply": "Reversing the current reverses the forces."},
             ]},
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "One side of a motor coil has 0.050 m of wire at right angles to a magnetic field of flux density 0.20 T. The current is 3.0 A. Calculate the force on this side of the coil.",
             "convOptions": ["Nothing to convert", "Convert m to cm: multiply by 100", "Convert A to mA: multiply by 1000"],
             "convAnswer": 0, "answer": 0.03, "tol": 0.0005, "unit": "N", "units": ["N", "T", "A", "J"],
             "right": "0.20 × 3.0 × 0.050 = 0.030 N.",
             "wrong": "Nothing to convert. F = B I l = 0.20 × 3.0 × 0.050 = 0.030 N.",
             "model": ["C · Nothing to convert", "F · F = B I l", "I · F = 0.20 × 3.0 × 0.050", "F · F = 0.030", "A · 0.030 N"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 4,
             "prompt": "Explain how the force on a conductor in a magnetic field makes the coil of an electric motor turn. Put the links in order.",
             "links": ["A current flows through the coil, which sits in a magnetic field.",
                       "So a force acts on each side of the coil. This is the motor effect.",
                       "The current flows in opposite directions in the two sides, so these forces act in opposite directions.",
                       "One side is pushed up and the other is pushed down, so the coil turns."],
             "herrings": [{"text": "The magnet attracts the copper coil.", "why": "Copper is not a magnetic material. The force comes from the current in the field."},
                          {"text": "The forces on the two sides act in the same direction.", "why": "The currents in the two sides are opposite, so the forces are opposite."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "The connections to the d.c. supply of a motor are swapped. Explain what happens. Put the links in order.",
             "links": ["The current in each side of the coil reverses.",
                       "The magnetic field has not changed, so by Fleming's left-hand rule the force on each side reverses.",
                       "So the coil turns the other way."],
             "herrings": [{"text": "The magnet's poles swap over.", "why": "Swapping the supply changes the current, not the magnet."},
                          {"text": "The forces get bigger.", "why": "The size of the current is the same, so the forces are the same size."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Explain how the force on a conductor in a magnetic field causes the coil of an electric motor to rotate.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "Links the current in each side of the coil, in a magnetic field, to forces in opposite directions that turn the coil.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "Says there is a force on the coil, or that the coil turns, with little linking.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The coil carries a current and sits in a magnetic field.",
                        "A force acts on each side of the coil. This is the motor effect.",
                        "The current in the two sides of the coil flows in opposite directions.",
                        "So, by Fleming's left-hand rule, the forces on the two sides act in opposite directions.",
                        "One side is pushed up and the other down, so the coil rotates."],
             "reject": ["“The magnet attracts the coil.”", "“The forces on both sides push the same way.”"]},
        ],
    },
}
