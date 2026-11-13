# -*- coding: utf-8 -*-
"""Induced potential (the generator effect), in the lean shape. Spec table: ks4-induced-potential.md.

Triple Higher only. AQA Physics 8463 4.7.3.1 (physics only, HT only). The old data's spec field
says 6.7.3.1, but Combined (8464) has no 6.7.3: section 6.7 stops at 6.7.2."""

LESSON = {
    "slug": "induced-potential",
    "start": {
        "setup": "A magnet rests inside a coil of wire. The coil is connected to an ammeter.",
        "question": "If you had to guess, does the ammeter show a current?",
        "options": [
            ("Yes, a steady current",
             "No current. A current is only induced while the magnet moves or the field around "
             "the coil changes."),
            ("No current",
             "No current. A current is only induced while the magnet moves or the field around "
             "the coil changes."),
        ],
        "answer": 1,
    },
    "words": ["generator effect", "induced potential difference", "induced current"],
    "knowledge": [
        {"kind": "card", "title": "The generator effect",
         "body": ["If a conductor moves relative to a magnetic field, or the magnetic field around "
                  "a conductor changes, a potential difference (p.d.) is induced across the ends "
                  "of the conductor.",
                  "If the conductor is part of a complete circuit, a current is induced in it.",
                  "This is called the generator effect.",
                  {"slot": "fig:induced-current"},
                  "Look at the ammeter while the magnet moves in."]},
        {"kind": "reveal", "title": "A magnet and a coil",
         "cols": ["What the ammeter shows"],
         "rows": [
             ("Push the magnet into the coil", "A current. The needle moves one way."),
             ("Hold the magnet still in the coil", "No current. Nothing is changing."),
             ("Pull the magnet out of the coil", "A current. The needle moves the other way."),
         ]},
        {"kind": "card", "title": "The size of the induced p.d.",
         "body": ["Any of these makes the induced p.d., and so the induced current, bigger:",
                  {"points": ["moving the magnet or the wire faster",
                              "using a stronger magnet",
                              "using a coil with more turns"]}]},
        {"kind": "card", "title": "The direction of the induced p.d.",
         "body": ["Either of these reverses the induced p.d. and the induced current:",
                  {"points": ["reversing the direction of movement, for example pulling the "
                              "magnet out instead of pushing it in",
                              "reversing the magnetic field, for example turning the magnet round "
                              "so the other pole goes in first"]},
                  "Reverse both and the direction stays the same."]},
        {"kind": "card", "title": "The induced current opposes the change",
         "body": ["An induced current generates a magnetic field that opposes the original change, "
                  "either the movement of the conductor or the change in magnetic field.",
                  "Push a north pole into a coil. The induced current makes that end of the coil "
                  "a north pole. Like poles repel, so the coil pushes back on the magnet.",
                  "Pull the magnet out. That end of the coil becomes a south pole. It attracts the "
                  "magnet, which opposes it leaving.",
                  "So you have to do work to move the magnet."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A strong magnet held in a coil induces a current.",
              "A current is only induced while something moves or the field changes."),
             ("The induced current helps the magnet move.",
              "Its magnetic field opposes the movement that caused it."),
             ("No circuit means nothing is induced.",
              "A p.d. is still induced across the ends. A current needs a complete circuit."),
         ]}]},
    ],
    "key_fact": "When a conductor moves relative to a magnetic field, or the field around it "
                "changes, a potential difference is induced across its ends. In a complete circuit "
                "this induces a current, and that current generates a magnetic field that opposes "
                "the original change.",
    "deeper": [
        {"kind": "card", "title": "Across, not along",
         "body": ["A straight wire has a p.d. induced when it moves across the field lines.",
                  "Moving it along the field lines induces nothing."]},
        {"kind": "card", "title": "Where the generator effect is used",
         "body": [{"points": ["Alternators and dynamos: a spinning coil generates a.c. or d.c.",
                              "Microphones: sound moves a coil in a magnetic field.",
                              "Transformers: a changing field in an iron core induces a p.d. in a "
                              "second coil."]},
                  "Each has its own lesson in this unit."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Give</strong>: the factors that change the size or direction, as a short list.",
             "<strong>Describe</strong>: what the ammeter shows at each stage.",
             "<strong>Explain</strong>: what changes, so what is induced, and which way the "
             "induced field acts.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "A wire moves through a magnetic field and a p.d. is induced across its ends. "
                       "Name this effect.",
             "why": "Inducing a p.d. by moving a conductor in a magnetic field is the generator effect.",
             "options": [
                 {"text": "The motor effect", "correct": False,
                  "reply": "The motor effect is a force on a wire carrying a current."},
                 {"text": "The generator effect", "correct": True},
                 {"text": "The heating effect", "correct": False,
                  "reply": "Nothing is being heated. A p.d. is induced."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give what the magnetic field of an induced current does.",
             "why": "An induced current generates a magnetic field that opposes the original change.",
             "options": [
                 {"text": "It adds to the original change", "correct": False,
                  "reply": "It acts against the change, not with it."},
                 {"text": "It has no effect on the magnet", "correct": False,
                  "reply": "It pushes or pulls on the magnet."},
                 {"text": "It opposes the original change", "correct": True},
                 {"text": "It makes the magnet lose its magnetism", "correct": False,
                  "reply": "The magnet keeps its magnetism. The induced field opposes the change."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "A magnet is pushed into a coil and an ammeter needle moves to the right. "
                       "The magnet is then pulled out at the same speed. Describe what the needle does.",
             "why": "Reversing the direction of movement reverses the induced current.",
             "options": [
                 {"text": "It moves to the left", "correct": True},
                 {"text": "It moves to the right again", "correct": False,
                  "reply": "The movement is reversed, so the current is reversed."},
                 {"text": "It stays at zero", "correct": False,
                  "reply": "The magnet is moving, so a current is induced."},
                 {"text": "It moves further to the right", "correct": False,
                  "reply": "The speed is the same and the direction is reversed."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 2,
             "prompt": "A student wants a bigger induced current from a magnet and a coil. "
                       "Give two changes that would each make the current bigger.",
             "why": "Moving the magnet faster and adding turns to the coil both increase the induced p.d.",
             "options": [
                 {"text": "Move the magnet slower and use fewer turns", "correct": False,
                  "reply": "Both of these make the current smaller."},
                 {"text": "Move the magnet faster and use more turns", "correct": True},
                 {"text": "Use a weaker magnet and move it faster", "correct": False,
                  "reply": "A weaker magnet makes the current smaller."},
                 {"text": "Hold the magnet still and use more turns", "correct": False,
                  "reply": "A magnet held still induces no current at all."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A north pole is pushed into a coil that is part of a complete circuit. "
                       "Explain why the coil pushes back on the magnet. Put the links in order.",
             "links": ["The moving magnet changes the magnetic field around the coil, so a current "
                       "is induced.",
                       "The induced current generates a magnetic field that makes the end of the "
                       "coil nearest the magnet a north pole.",
                       "Like poles repel, so the coil pushes back against the magnet."],
             "herrings": [{"text": "The end of the coil nearest the magnet becomes a south pole.",
                           "why": "A south pole would attract the magnet and help the change. The induced field opposes it."},
                          {"text": "The magnet loses its magnetism inside the coil.",
                           "why": "A permanent magnet keeps its magnetism."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why moving the magnet into the coil faster gives a bigger reading on "
                       "the ammeter. Put the links in order.",
             "links": ["Moving the magnet faster makes the magnetic field around the coil change faster.",
                       "So a bigger potential difference is induced across the coil.",
                       "The circuit is complete, so a bigger current flows through the ammeter."],
             "herrings": [{"text": "A faster magnet has a stronger magnetic field.",
                           "why": "The magnet's strength does not change with its speed."},
                          {"text": "Moving faster heats the wire, and the heat makes the current.",
                           "why": "The current is induced by the changing field, not by heating."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 6,
             "prompt": "A student has a bar magnet, a coil of wire and a sensitive ammeter. Describe "
                       "how she could show the generator effect, and how she could change the size "
                       "and the direction of the induced current.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Shows the generator effect, gives factors for the size and for the direction, with what the ammeter shows.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Shows the generator effect and gives factors for the size or for the direction.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant points.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Connect the coil to the ammeter to make a complete circuit.",
                        "Push the magnet into the coil: the ammeter shows a current.",
                        "Hold the magnet still: the reading is zero.",
                        "Pull the magnet out: the needle moves the other way.",
                        "A bigger current: move the magnet faster, use a stronger magnet or use more turns.",
                        "Reverse the current: reverse the movement or turn the magnet round."],
             "reject": ["“A magnet held still in the coil gives a steady current.”",
                        "“A stronger magnet reverses the current.”"]},
        ],
    },
}
