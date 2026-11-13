# -*- coding: utf-8 -*-
"""Loudspeakers and headphones, in the lean shape. Rebuilt from the old format.
Spec table: ks4-loudspeakers-headphones.md.

AQA 4.7.2.4 (8463), Physics only, HT only. The lesson exists on TH only."""

LESSON = {
    "slug": "loudspeakers-headphones",
    "start": {
        "setup": None,
        "question": "If you had to guess, what is the current in a loudspeaker coil like while it plays a note?",
        "options": [
            ("It keeps changing direction",
             "It keeps changing direction. Each time the current reverses, the force on the coil "
             "reverses and the cone moves the other way."),
            ("It flows steadily one way",
             "It keeps changing direction. Each time the current reverses, the force on the coil "
             "reverses and the cone moves the other way."),
        ],
        "answer": 0,
    },
    "words": ["motor effect", "moving coil", "cone", "pressure variations"],
    "knowledge": [
        {"kind": "card", "title": "What a loudspeaker does",
         "body": ["Loudspeakers and headphones use the motor effect to convert variations in current "
                  "in electrical circuits to the pressure variations in sound waves.",
                  {"slot": "fig:loudspeaker"},
                  "Find the permanent magnet, the coil and the cone."]},
        {"kind": "reveal", "title": "The parts of a moving-coil loudspeaker",
         "cols": ["What it does"],
         "rows": [
             ("Permanent magnet", "Makes a magnetic field around the coil. It does not move."),
             ("Coil", "Carries the changing current from the circuit. It sits in the magnetic field "
                      "and is fixed to the cone."),
             ("Cone", "Moves with the coil. It pushes and pulls on the air."),
         ]},
        {"kind": "card", "title": "How it works",
         "body": [{"points": [
             "An alternating current (a.c.) flows through the coil. It keeps changing direction.",
             "The coil is in the magnetic field of the permanent magnet, so a force acts on the "
             "coil. This is the motor effect.",
             "When the current changes direction, the force changes direction.",
             "So the coil and the cone move backwards and forwards. They vibrate.",
             "The cone pushes and pulls the air. This makes compressions and rarefactions, which "
             "are the pressure variations in a sound wave."]}]},
        {"kind": "card", "title": "Frequency and amplitude",
         "body": ["The cone vibrates at the same frequency as the current. A higher frequency "
                  "current gives a higher frequency sound, which has a higher pitch.",
                  "A bigger current gives a bigger force, so the cone moves further. The sound wave "
                  "has a bigger amplitude, so it is louder."]},
        {"kind": "card", "title": "Headphones",
         "body": ["Headphones work in the same way as a loudspeaker.",
                  "Each earpiece has a small permanent magnet, a coil and a thin diaphragm that does "
                  "the job of the cone."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The magnet vibrates to make the sound.",
              "The magnet stays still. The coil and the cone vibrate."),
             ("A steady direct current makes a steady note.",
              "A steady current gives a force in one direction. The cone moves once and stays "
              "there, so no note is made."),
             ("A loudspeaker uses the generator effect.",
              "A loudspeaker uses the motor effect. A microphone uses the generator effect."),
         ]}]},
    ],
    "key_fact": "Loudspeakers and headphones use the motor effect to convert variations in current "
                "in electrical circuits to the pressure variations in sound waves. The changing "
                "current in the coil causes a changing force on it, so the coil and cone vibrate "
                "and make the air vibrate.",
    "deeper": [
        {"kind": "card", "title": "Microphones",
         "body": ["A moving-coil microphone is built like a loudspeaker but works the other way round.",
                  "Sound waves move the diaphragm and the coil. The generator effect then converts "
                  "the pressure variations into variations in current.",
                  "You meet microphones later in this unit."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong>: link the current, the force on the coil, the movement of "
             "the cone and the pressure variations in the air, in that order.",
             "<strong>Describe</strong>: say what each part does.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the effect that a loudspeaker uses.",
             "why": "A force acts on the current-carrying coil in the magnet's field. This is the motor effect.",
             "options": [
                 {"text": "The generator effect", "correct": False, "reply": "A microphone uses the generator effect."},
                 {"text": "The motor effect", "correct": True},
                 {"text": "The heating effect of a current", "correct": False, "reply": "The sound comes from the force on the coil, not from heating."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "A loudspeaker converts variations in current in electrical circuits. Give what it converts them to.",
             "why": "AQA's words: variations in current are converted to the pressure variations in sound waves.",
             "options": [
                 {"text": "Pressure variations in sound waves", "correct": True},
                 {"text": "Changes in the strength of the permanent magnet", "correct": False, "reply": "The permanent magnet's field does not change."},
                 {"text": "Changes in the temperature of the air", "correct": False, "reply": "The cone moves the air. It does not heat it."},
                 {"text": "Light waves", "correct": False, "reply": "A loudspeaker makes sound, not light."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "The current in a loudspeaker coil changes direction. Describe what happens to the force on the coil.",
             "why": "Reversing the current reverses the force, so the coil and cone move the other way.",
             "options": [
                 {"text": "It keeps the same direction", "correct": False, "reply": "Reversing the current reverses the force."},
                 {"text": "It reverses", "correct": True},
                 {"text": "It stops for good", "correct": False, "reply": "There is still a current in a magnetic field, so there is still a force."},
                 {"text": "It doubles in size", "correct": False, "reply": "The direction changes, not the size."},
             ]},
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "The frequency of the current in a loudspeaker coil is doubled. Describe what happens to the cone.",
             "why": "The cone vibrates at the same frequency as the current.",
             "options": [
                 {"text": "It vibrates twice as many times each second", "correct": True},
                 {"text": "It vibrates half as many times each second", "correct": False, "reply": "The cone follows the current, so its frequency doubles too."},
                 {"text": "It stops vibrating", "correct": False, "reply": "The current still keeps changing direction."},
                 {"text": "It vibrates with twice the amplitude at the same frequency", "correct": False, "reply": "The frequency of the cone follows the frequency of the current."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 4,
             "prompt": "Explain how a moving-coil loudspeaker produces a sound. Put the links in order.",
             "links": ["A changing current flows through the coil.",
                       "The coil is in a magnetic field, so a force acts on it. This is the motor effect.",
                       "As the current changes direction, the force changes direction, so the coil and cone vibrate.",
                       "The cone pushes and pulls the air, making the pressure variations of a sound wave."],
             "herrings": [{"text": "The magnet vibrates and pushes the air.", "why": "The magnet stays still. The coil and cone move."},
                          {"text": "The current heats the air, which then expands.", "why": "The sound comes from the cone moving the air."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "The size of the current in a loudspeaker coil is increased. Explain why the sound gets louder. Put the links in order.",
             "links": ["A bigger current gives a bigger force on the coil.",
                       "So the coil and the cone move further backwards and forwards.",
                       "So the pressure variations in the air are bigger, and the sound is louder."],
             "herrings": [{"text": "The cone vibrates more times each second.", "why": "That depends on the frequency of the current, not its size."},
                          {"text": "The permanent magnet becomes stronger.", "why": "The magnet's field does not change."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "Explain how a moving-coil loudspeaker converts variations in current into sound.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "A linked explanation: changing current, force on the coil from the motor effect, the force reversing, the cone vibrating and making pressure variations in the air.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant points, such as a force on the coil or the cone vibrating.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["The coil is fixed to the cone and sits in the field of a permanent magnet.",
                        "A changing current flows in the coil.",
                        "A force acts on the coil. This is the motor effect.",
                        "When the current reverses, the force reverses, so the coil and cone vibrate.",
                        "The cone makes the air vibrate, producing pressure variations: a sound wave.",
                        "The sound has the same frequency as the current."],
             "reject": ["“The magnet vibrates.”", "“The current is turned into sound in the wire.”"]},
        ],
    },
}
