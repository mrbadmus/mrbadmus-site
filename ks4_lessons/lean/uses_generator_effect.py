# -*- coding: utf-8 -*-
"""Uses of the generator effect (alternators and dynamos), in the lean shape.
Spec table: ks4-uses-generator-effect.md.

Triple Higher only. AQA Physics 8463 4.7.3.2 (physics only, HT only). The old data's spec field
says 6.7.3.2, but Combined (8464) has no 6.7.3: section 6.7 stops at 6.7.2."""

LESSON = {
    "slug": "uses-generator-effect",
    "start": {
        "setup": None,
        "question": "If you had to guess, does a coil spinning in a magnetic field make a.c. or d.c. "
                    "on its own?",
        "options": [
            ("a.c.",
             "a.c. Each side of the coil moves one way then the other through the field, so the "
             "induced p.d. reverses every half turn."),
            ("d.c.",
             "a.c. Each side of the coil moves one way then the other through the field, so the "
             "induced p.d. reverses every half turn."),
        ],
        "answer": 0,
    },
    "words": ["alternator", "dynamo", "slip rings", "split-ring commutator"],
    "knowledge": [
        {"kind": "card", "title": "A spinning coil",
         "body": ["A coil turns in a magnetic field.",
                  "As it turns, the magnetic field through the coil keeps changing, so a potential "
                  "difference (p.d.) is induced across its ends. This is the generator effect.",
                  "Each side of the coil moves one way through the field, then back the other way. "
                  "So the induced p.d. in the coil reverses every half turn."]},
        {"kind": "card", "title": "An alternator generates a.c.",
         "body": ["The coil is connected to the circuit through slip rings and brushes.",
                  "The slip rings turn with the coil, so each end of the coil stays connected to "
                  "the same side of the circuit.",
                  "The output reverses every half turn, just like the p.d. in the coil. This is "
                  "alternating current (a.c.)."]},
        {"kind": "card", "title": "A dynamo generates d.c.",
         "body": ["The coil is connected to the circuit through a split-ring commutator and brushes.",
                  "The commutator swaps the connections every half turn, at the moment the p.d. in "
                  "the coil reverses.",
                  "So the output never reverses. This is direct current (d.c.)."]},
        {"kind": "card", "title": "Reading graphs of p.d. against time",
         "body": [{"slot": "fig:ac-dc-output"},
                  {"points": ["Alternator: the p.d. goes above and below zero. One turn of the "
                              "coil gives one full cycle.",
                              "Dynamo: the p.d. rises and falls but never goes below zero. One turn "
                              "of the coil gives two humps.",
                              "The peak p.d. is the highest point on the graph.",
                              "Read the time for one turn from the time axis.",
                              "The time for one cycle is the period."]}]},
        {"kind": "reveal", "title": "Changing the output",
         "cols": ["Peak p.d.", "Time for one turn"],
         "rows": [
             ("Turn the coil faster", "Bigger", "Shorter, so the peaks are closer together"),
             ("Use a stronger magnet", "Bigger", "No change"),
             ("Use a coil with more turns", "Bigger", "No change"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("An alternator uses a split-ring commutator.",
              "Alternator: slip rings, a.c. Dynamo: split-ring commutator, d.c."),
             ("Turning faster only makes the peaks higher.",
              "It also puts them closer together, because each turn takes less time."),
             ("A dynamo's d.c. is a flat line.",
              "It rises and falls, but it never goes below zero."),
         ]}]},
    ],
    "key_fact": "The generator effect is used in an alternator to generate a.c. and in a dynamo to "
                "generate d.c. An alternator's slip rings keep the same connections, so its output "
                "reverses every half turn; a dynamo's split-ring commutator swaps the connections "
                "every half turn, so its output never reverses.",
    "deeper": [
        {"kind": "card", "title": "Power stations",
         "body": ["The generators in power stations are alternators.",
                  "That is why mains electricity is a.c."]},
        {"kind": "card", "title": "A dynamo and a d.c. motor",
         "body": ["A d.c. motor uses a split-ring commutator too.",
                  "In a motor, a current makes the coil turn (the motor effect).",
                  "In a dynamo, turning the coil makes a current (the generator effect)."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: the coil turns, the field changes, a p.d. is induced, then "
             "what the slip rings or commutator do to it.",
             "<strong>Sketch</strong>: p.d. on the vertical axis, time on the horizontal axis, and "
             "the right shape.",
             "<strong>Compare</strong>: say how the two machines are the same and how they differ.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the part that lets a dynamo generate d.c.",
             "why": "The split-ring commutator swaps the connections every half turn.",
             "options": [
                 {"text": "Slip rings and brushes", "correct": False,
                  "reply": "Slip rings are in an alternator, which generates a.c."},
                 {"text": "Split-ring commutator", "correct": True},
                 {"text": "Iron core", "correct": False,
                  "reply": "An iron core is in a transformer."},
                 {"text": "Diaphragm", "correct": False,
                  "reply": "A diaphragm is in a microphone."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the type of current an alternator generates.",
             "why": "An alternator generates alternating current (a.c.).",
             "options": [
                 {"text": "Direct current (d.c.)", "correct": False,
                  "reply": "A dynamo generates d.c."},
                 {"text": "Alternating current (a.c.)", "correct": True},
                 {"text": "No current", "correct": False,
                  "reply": "The turning coil has a p.d. induced, so in a complete circuit there is a current."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "The coil of an alternator turns twice as fast. Describe two changes to its "
                       "graph of p.d. against time.",
             "why": "The field changes faster, so the peaks are higher. Each turn takes less time, so they are closer together.",
             "options": [
                 {"text": "The peaks are higher and closer together", "correct": True},
                 {"text": "The peaks are higher and further apart", "correct": False,
                  "reply": "Each turn takes less time, so the peaks are closer together."},
                 {"text": "The peaks are the same height and closer together", "correct": False,
                  "reply": "The field changes faster, so the peaks are higher."},
                 {"text": "The graph stays above zero", "correct": False,
                  "reply": "An alternator's output still goes above and below zero."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why the output of a dynamo never goes below zero.",
             "why": "The commutator swaps the connections every half turn, as the p.d. in the coil reverses.",
             "options": [
                 {"text": "The slip rings keep each end of the coil on the same side of the circuit", "correct": False,
                  "reply": "That is an alternator, and its output does go below zero."},
                 {"text": "The commutator swaps the connections each time the p.d. in the coil reverses", "correct": True},
                 {"text": "The magnet is turned round every half turn", "correct": False,
                  "reply": "The magnet stays still. The commutator does the swapping."},
                 {"text": "The coil turns half way and then stops", "correct": False,
                  "reply": "The coil keeps turning all the way round."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how an alternator generates a.c. Put the links in order.",
             "links": ["The coil turns in the magnetic field, so a potential difference is induced "
                       "across its ends.",
                       "Each side of the coil moves one way then the other, so the induced p.d. "
                       "reverses every half turn.",
                       "The slip rings keep each end of the coil connected to the same side of the "
                       "circuit, so the output is a.c."],
             "herrings": [{"text": "A split-ring commutator swaps the connections every half turn.",
                           "why": "That is a dynamo, which generates d.c."},
                          {"text": "The poles of the magnet swap every half turn.",
                           "why": "The magnet stays the same. The coil's movement reverses."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how a dynamo generates d.c. Put the links in order.",
             "links": ["The coil turns in the magnetic field, so a potential difference is induced "
                       "across its ends.",
                       "The p.d. in the coil reverses every half turn, and at that moment the "
                       "split-ring commutator swaps the connections.",
                       "So the output p.d. is always in the same direction, which is d.c."],
             "herrings": [{"text": "Slip rings keep the connections the same.",
                           "why": "That is an alternator, which generates a.c."},
                          {"text": "The coil only turns half way, then turns back.",
                           "why": "The coil keeps turning the same way."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Compare", "marks": 6,
             "prompt": "Compare how an alternator and a dynamo use the generator effect. Include the "
                       "shape of each graph of p.d. against time.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Explains the generator effect in the coil and why each machine gives a.c. or d.c., with the shape of each graph.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Explains one machine fully, or both with some missing detail.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant points.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["In both, a coil turns in a magnetic field, so a p.d. is induced.",
                        "The p.d. in the coil reverses every half turn.",
                        "An alternator uses slip rings, so the connections never swap.",
                        "So an alternator gives a.c.: the graph goes above and below zero.",
                        "A dynamo uses a split-ring commutator, which swaps the connections every half turn.",
                        "So a dynamo gives d.c.: the graph rises and falls but never goes below zero."],
             "reject": ["“An alternator uses a split-ring commutator.”",
                        "“A dynamo's graph is a flat line.”"]},
        ],
    },
}
