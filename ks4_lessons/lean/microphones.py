# -*- coding: utf-8 -*-
"""Microphones, in the lean shape. Spec table: ks4-microphones.md.

Triple Higher only. AQA Physics 8463 4.7.3.3 (physics only, HT only). The old data's spec field
says 6.7.3.3, but Combined (8464) has no 6.7.3: section 6.7 stops at 6.7.2."""

LESSON = {
    "slug": "microphones",
    "start": {
        "setup": "A moving-coil microphone and a loudspeaker both have a coil and a magnet.",
        "question": "If you had to guess, does the microphone use the motor effect or the "
                    "generator effect?",
        "options": [
            ("The motor effect",
             "The generator effect. Sound moves the coil in a magnetic field, and that induces a "
             "current."),
            ("The generator effect",
             "The generator effect. Sound moves the coil in a magnetic field, and that induces a "
             "current."),
        ],
        "answer": 1,
    },
    "words": ["diaphragm", "generator effect", "pressure variations", "induced current"],
    "knowledge": [
        {"kind": "card", "title": "What a microphone does",
         "body": ["Microphones use the generator effect to convert the pressure variations in "
                  "sound waves into variations in current in electrical circuits."]},
        {"kind": "card", "title": "The parts",
         "body": [{"slot": "fig:microphone"},
                  {"points": ["A diaphragm: a thin sheet that sound waves push on.",
                              "A coil of wire fixed to the diaphragm.",
                              "A permanent magnet. The coil sits in its magnetic field."]},
                  "A moving-coil microphone is also called a dynamic microphone."]},
        {"kind": "card", "title": "How a moving-coil microphone works",
         "body": [{"points": [
             "Sound waves are pressure variations in the air. They make the diaphragm vibrate.",
             "The coil is fixed to the diaphragm, so it moves back and forth in the magnetic field.",
             "The coil moves relative to the magnetic field, so a potential difference is induced "
             "across its ends. This is the generator effect.",
             "The coil is part of a complete circuit, so a current is induced. It reverses each "
             "time the coil changes direction.",
             "The current varies in the same way as the pressure in the sound wave.",
         ]}]},
        {"kind": "card", "title": "Louder and higher",
         "body": ["A louder sound makes the diaphragm move further and faster, so the induced "
                  "current is bigger.",
                  "A sound with a higher frequency makes the diaphragm vibrate more times each "
                  "second, so the current changes direction more often."]},
        {"kind": "reveal", "title": "Microphone and loudspeaker",
         "cols": ["Microphone", "Loudspeaker"],
         "rows": [
             ("Effect it uses", "The generator effect", "The motor effect"),
             ("What goes in", "Sound waves", "A varying current"),
             ("What comes out", "A varying current", "Sound waves"),
             ("What moves the coil", "The diaphragm, pushed by the sound",
              "The force on the current in the magnetic field"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A microphone uses the motor effect.",
              "A microphone uses the generator effect. A loudspeaker uses the motor effect."),
             ("The magnet vibrates to make the current.",
              "In a moving-coil microphone the coil moves. The magnet stays still."),
         ]}]},
    ],
    "key_fact": "Microphones use the generator effect to convert the pressure variations in sound "
                "waves into variations in current in electrical circuits. Sound makes the diaphragm "
                "and coil vibrate in a magnetic field, so a varying current is induced.",
    "deeper": [
        {"kind": "card", "title": "A small signal",
         "body": ["The current from a microphone is very small.",
                  "An amplifier makes it bigger before it drives a loudspeaker."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain how it works</strong>: sound, then diaphragm, then coil in the "
             "magnetic field, then induced p.d., then varying current.",
             "<strong>Compare</strong>: a microphone uses the generator effect, a loudspeaker "
             "uses the motor effect.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the effect a moving-coil microphone uses.",
             "why": "Sound moves the coil in a magnetic field, so a current is induced: the generator effect.",
             "options": [
                 {"text": "The motor effect", "correct": False,
                  "reply": "A loudspeaker uses the motor effect."},
                 {"text": "The heating effect", "correct": False,
                  "reply": "Nothing is being heated. A current is induced."},
                 {"text": "The generator effect", "correct": True},
             ]},
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the part of a moving-coil microphone that the sound waves push on.",
             "why": "Sound waves make the diaphragm vibrate, and the coil is fixed to it.",
             "options": [
                 {"text": "The diaphragm", "correct": True},
                 {"text": "The permanent magnet", "correct": False,
                  "reply": "The magnet stays still. It provides the magnetic field."},
                 {"text": "The split-ring commutator", "correct": False,
                  "reply": "A commutator is in a dynamo or a motor."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "A singer sings the same note more loudly into a microphone. Describe how "
                       "the induced current changes.",
             "why": "A louder sound gives a bigger current. The same note keeps the same frequency.",
             "options": [
                 {"text": "It is bigger, and changes direction more often", "correct": False,
                  "reply": "The note is the same, so it changes direction just as often."},
                 {"text": "It is bigger, and changes direction just as often", "correct": True},
                 {"text": "It is the same size, and changes direction more often", "correct": False,
                  "reply": "A louder sound gives a bigger current at the same frequency."},
                 {"text": "It is smaller, and changes direction less often", "correct": False,
                  "reply": "A louder sound moves the coil further and faster, so the current is bigger."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why a current is induced when sound reaches a moving-coil microphone.",
             "why": "The coil moves relative to the magnetic field, so a p.d. is induced across it. The circuit is complete, so a current flows.",
             "options": [
                 {"text": "Sound waves carry charge into the coil", "correct": False,
                  "reply": "Sound carries no charge. The moving coil has a p.d. induced in it."},
                 {"text": "The magnet vibrates and loses its magnetism", "correct": False,
                  "reply": "The magnet stays still and keeps its magnetism."},
                 {"text": "The coil moves in a magnetic field", "correct": True},
                 {"text": "A current in the coil moves the diaphragm", "correct": False,
                  "reply": "That is how a loudspeaker works."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 4,
             "prompt": "Explain how a moving-coil microphone converts sound into a varying current. "
                       "Put the links in order.",
             "links": ["Pressure variations in the sound wave make the diaphragm vibrate.",
                       "The coil is fixed to the diaphragm, so it moves back and forth in the field "
                       "of the permanent magnet.",
                       "So a potential difference is induced across the coil, and a current is "
                       "induced in the circuit.",
                       "The current varies in the same way as the pressure in the sound wave."],
             "herrings": [{"text": "The current in the coil exerts a force that moves the diaphragm.",
                           "why": "That is the motor effect in a loudspeaker."},
                          {"text": "The sound wave makes the magnet stronger.",
                           "why": "The magnet does not change. The coil moves in its field."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A sound with a higher frequency reaches a microphone. Explain why the "
                       "induced current changes direction more often. Put the links in order.",
             "links": ["The sound has more pressure variations each second, so the diaphragm "
                       "vibrates more times each second.",
                       "The coil is fixed to the diaphragm, so it changes direction more times "
                       "each second.",
                       "The induced current reverses each time the coil changes direction, so the "
                       "current changes direction more often."],
             "herrings": [{"text": "The magnet vibrates faster.",
                           "why": "The magnet stays still. The coil moves."},
                          {"text": "A higher frequency makes the coil move further each time.",
                           "why": "Frequency is how many vibrations each second, not how far."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Explain how a moving-coil microphone works.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "A clear sequence from sound to diaphragm to coil to induced current, naming the generator effect.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two correct steps.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The pressure variations in sound waves make the diaphragm vibrate.",
                        "The coil is fixed to the diaphragm, so it moves in the magnetic field of a permanent magnet.",
                        "A potential difference is induced across the coil: the generator effect.",
                        "A current is induced in the circuit that varies in the same way as the sound wave."],
             "reject": ["“It uses the motor effect.”",
                        "“The magnet vibrates and makes electricity.”"]},
        ],
    },
}
