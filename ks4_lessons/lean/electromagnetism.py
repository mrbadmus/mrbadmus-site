# -*- coding: utf-8 -*-
"""Electromagnetism, in the lean shape. New record, no legacy page.
Spec table: ks4-electromagnetism.md (AQA 8464 6.7.2.1 / 8463 4.7.2.1).
The motor effect, F = BIl and Fleming's left-hand rule have their own lessons and stay out of this one."""

LESSON = {
    "slug": "electromagnetism",
    "start": {
        "setup": "A compass sits next to a wire. The current in the wire is switched on.",
        "question": "If you had to guess, what does the compass needle do?",
        "options": [
            ("It moves",
             "It moves. A current in a wire produces a magnetic field around the wire, and the "
             "needle lines up with it."),
            ("It stays still",
             "It moves. A current in a wire produces a magnetic field around the wire, and the "
             "needle lines up with it."),
        ],
        "answer": 0,
    },
    "words": ["solenoid", "uniform field", "iron core", "electromagnet"],
    "knowledge": [
        {"kind": "card", "title": "A current makes a magnetic field",
         "body": ["When a current flows through a conducting wire, a magnetic field is produced "
                  "around the wire.",
                  "The strength of the magnetic field depends on the current through the wire and "
                  "the distance from the wire. A bigger current gives a stronger field. The field "
                  "is weaker further from the wire."]},
        {"kind": "card", "title": "Showing the magnetic effect of a current",
         "body": [{"points": [
             "Put a plotting compass next to a wire in a circuit.",
             "Switch on the current. The compass needle moves to line up with the field of the wire.",
             "Switch off the current. The needle goes back to lining up with the Earth's field.",
             "Reverse the current. The needle turns the other way.",
         ]}]},
        {"kind": "card", "title": "The field around a straight wire",
         "body": ["Look at the arrows on the circles.",
                  {"slot": "fig:wire-field"},
                  {"points": [
                      "The field lines are circles around the wire, with the wire at the centre.",
                      "The circles get further apart further from the wire, where the field is "
                      "weaker.",
                      "Reverse the current and the direction of the field reverses.",
                  ]},
                  "To find the direction, grip the wire in your right hand with your thumb "
                  "pointing the way the current flows. Your fingers curl the way the field goes.",
                  "This is the right-hand grip rule."]},
        {"kind": "card", "title": "The solenoid",
         "body": ["A solenoid is a wire wound into a long coil.",
                  "Shaping a wire to form a solenoid increases the strength of the magnetic field "
                  "created by a current through the wire.",
                  "The magnetic field inside a solenoid is strong and uniform. Uniform means the "
                  "same strength and direction everywhere: the lines inside are straight, parallel "
                  "and equally spaced.",
                  "The magnetic field around a solenoid has a similar shape to that of a bar magnet.",
                  {"slot": "fig:solenoid-field"}]},
        {"kind": "card", "title": "Why a solenoid makes the field stronger",
         "body": [{"points": [
             "Each turn of the coil has its own magnetic field.",
             "Inside the coil, the fields of all the turns point the same way, so they add together.",
             "This makes the field inside the solenoid strong and uniform.",
         ]}]},
        {"kind": "card", "title": "Which end is the north pole",
         "body": ["Curl the fingers of your right hand the way the current goes round the turns. "
                  "Your thumb points to the north pole end.",
                  "Outside the solenoid, the field lines go from the north pole end to the south "
                  "pole end, as they do for a bar magnet.",
                  "Reverse the current and the two poles swap ends."]},
        {"kind": "card", "title": "The electromagnet",
         "body": ["Adding an iron core increases the strength of the magnetic field of a solenoid.",
                  "An electromagnet is a solenoid with an iron core.",
                  "The iron core is in the field of the solenoid, so it becomes an induced magnet. "
                  "Its field adds to the field of the solenoid.",
                  "When the current is switched off, the iron loses most or all of its magnetism "
                  "quickly, so the electromagnet switches off.",
                  "Iron is used for the core, not steel. Steel keeps more of its magnetism than "
                  "iron when the current stops, so the electromagnet would not switch off "
                  "properly."]},
        {"kind": "card", "title": "Making an electromagnet stronger",
         "body": [{"points": [
             "Increase the current.",
             "Add an iron core.",
             "Wind more turns of wire into the same length of coil.",
         ]}]},
        {"kind": "card", "title": "Reading a device diagram: the electric bell",
         "routes": ["TF", "TH"],
         "body": ["Find the electromagnet first. Then ask what it attracts when the current is on, "
                  "and what happens when the current stops.",
                  {"slot": "fig:electric-bell"},
                  {"points": [
                      "1. Press the switch. A current flows through the coil of the electromagnet.",
                      "2. The electromagnet attracts the iron armature. The hammer on the armature "
                      "hits the gong.",
                      "3. As the armature moves, it pulls away from the contact screw. The circuit "
                      "is broken and the current stops.",
                      "4. The electromagnet loses its magnetism, so the spring pulls the armature "
                      "back.",
                      "5. The armature touches the contact screw again. The current flows again "
                      "and the cycle repeats while the switch is pressed.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The field lines around a wire run along the wire.",
              "They are circles around the wire."),
             ("The field around a wire is the same strength everywhere.",
              "It is strongest close to the wire and weaker further away."),
             ("An electromagnet is a coil of wire.",
              "An electromagnet is a solenoid with an iron core."),
         ]}]},
    ],
    "key_fact": "A current in a wire produces a magnetic field around it, which is stronger with a "
                "bigger current and weaker further from the wire. Shaping the wire into a solenoid "
                "makes the field inside strong and uniform, and adding an iron core makes an "
                "electromagnet with a stronger field still.",
    "deeper": [
        {"kind": "card", "title": "Why electromagnets are useful",
         "body": ["An electromagnet can be switched on and off.",
                  "Its strength can be changed by changing the current.",
                  "A scrapyard crane uses an electromagnet to lift iron and steel, then drops it "
                  "when the current is switched off."]},
        {"kind": "card", "title": "Current into or out of the page",
         "body": ["A dot in a circle means the current comes out of the page, towards you. The "
                  "field goes anticlockwise.",
                  "A cross in a circle means the current goes into the page, away from you. The "
                  "field goes clockwise."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Draw</strong>: field lines with arrows on every line.",
             "<strong>Describe how to demonstrate</strong>: say what you set up, what you do and "
             "what you would see.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State the shape of the magnetic field lines around a straight wire "
                       "carrying a current.",
             "why": "The field lines are circles around the wire, with the wire at the centre.",
             "options": [
                 {"text": "Straight lines along the wire", "correct": False,
                  "reply": "The field goes round the wire, not along it."},
                 {"text": "Circles around the wire", "correct": True},
                 {"text": "Straight lines out from the wire", "correct": False,
                  "reply": "The field lines go round the wire in circles."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what an electromagnet is.",
             "why": "AQA's wording: an electromagnet is a solenoid with an iron core.",
             "options": [
                 {"text": "A bar magnet made of steel", "correct": False,
                  "reply": "That is a permanent magnet."},
                 {"text": "A straight wire carrying a current", "correct": False,
                  "reply": "This has a magnetic field, but it is not an electromagnet."},
                 {"text": "A solenoid with an iron core", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "Describe how the magnetic effect of a current can be demonstrated.",
             "why": "With the current on, the wire has a magnetic field, so a compass needle next "
                    "to it moves.",
             "options": [
                 {"text": "Put a compass next to a wire and switch on the current. The needle "
                          "moves.", "correct": True},
                 {"text": "Put a compass next to a wire with no current. The needle moves.",
                  "correct": False,
                  "reply": "With no current, the wire has no magnetic field."},
                 {"text": "Put a lamp in the circuit and switch on the current. The lamp lights.",
                  "correct": False,
                  "reply": "That shows a current flows, not that it makes a magnetic field."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why a wire wound into a solenoid gives a stronger magnetic field "
                       "than the same wire laid out straight, with the same current.",
             "why": "Inside the coil, the fields of all the turns point the same way and add "
                    "together.",
             "options": [
                 {"text": "Coiling the wire lowers its resistance, so more current flows",
                  "correct": False,
                  "reply": "Coiling a wire does not change its resistance. The current is the same."},
                 {"text": "The fields of all the turns add together inside the coil",
                  "correct": True},
                 {"text": "The coil turns into a permanent magnet", "correct": False,
                  "reply": "The field is only there while the current flows."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why adding an iron core makes the magnetic field of a solenoid "
                       "stronger. Put the links in order.",
             "links": ["The current in the solenoid produces a magnetic field inside the coil.",
                       "The iron core is in this field, so it becomes an induced magnet.",
                       "The field of the iron core adds to the field of the solenoid, so the field "
                       "is stronger."],
             "herrings": [{"text": "The iron core lets more current flow through the wire.",
                           "why": "The current flows in the wire, not in the core."},
                          {"text": "The iron core becomes a permanent magnet.",
                           "why": "It is an induced magnet. It loses most of its magnetism "
                                  "quickly when the current stops."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "An electromagnet holds up a piece of scrap steel. Explain what happens "
                       "when the current is switched off. Put the links in order.",
             "links": ["The current stops, so the solenoid no longer produces a magnetic field.",
                       "The iron core loses most or all of its magnetism quickly.",
                       "The magnetic force on the steel is now too small to hold it up, so the "
                       "steel falls."],
             "herrings": [{"text": "The steel is repelled by the electromagnet.",
                           "why": "The force between a magnet and a magnetic material is always "
                                  "one of attraction."},
                          {"text": "The iron core stays strongly magnetic.",
                           "why": "Iron loses most or all of its magnetism quickly."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "A student winds a long wire into a solenoid and puts an iron core inside "
                       "it. Explain how the solenoid and the iron core each make the magnetic "
                       "field stronger than the field of the straight wire with the same current.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Explains why the solenoid makes the field "
                  "stronger (the fields of the turns add together inside) and why the iron core "
                  "makes it stronger (it becomes an induced magnet whose field adds on), in a "
                  "logical order.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Explains one of the two clearly, or states "
                  "both with little explanation.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "States one correct fact about the field of a "
                  "wire, a solenoid or an iron core.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["A current in a wire produces a magnetic field around the wire.",
                        "Each turn of the solenoid produces its own magnetic field.",
                        "Inside the solenoid, the fields of all the turns point the same way and "
                        "add together.",
                        "So the field inside the solenoid is strong and uniform.",
                        "The iron core is in this field, so it becomes an induced magnet.",
                        "The field of the iron core adds to the field of the solenoid, so the "
                        "field is stronger still. This is an electromagnet."],
             "reject": ["“The iron core carries more current.”",
                        "“Coiling the wire lowers its resistance.”"]},
        ],
    },
}
