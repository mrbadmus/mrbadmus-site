# -*- coding: utf-8 -*-
"""How sound is made, in the lean shape. Spec table: docs/lessons/wave2/ks3-how-sound-is-made.md."""

LESSON = {
    "slug": "how-sound-is-made",
    "start": {
        "setup": "Put two fingers on the front of your throat and hum. Then stop humming and just breathe out.",
        "question": "If you had to guess, what makes the humming sound: air "
                    "rushing past, or something shaking?",
        "options": [
            ("Air rushing past",
             "Breathing out moves even more air, and it makes no note. Moving air is not enough."),
            ("Something shaking",
             "Yes. Two folds in your throat vibrate. You can feel it under your fingers."),
        ],
        "answer": 1,
    },
    "words": ["vibrating", "loudspeaker", "diaphragm", "eardrum"],
    "word_defs": {
        "vibrating": "Moving quickly to and fro about one place.",
        "loudspeaker": "A device with a cone that vibrates to turn an electrical signal into sound.",
        "diaphragm": "The thin sheet in a microphone that vibrates when sound reaches it.",
        "eardrum": "The thin sheet in your ear that vibrates when sound reaches it.",
    },
    "knowledge": [
        {"kind": "card", "title": "Every sound starts with a vibration",
         "body": ["Every sound is made by something vibrating.",
                  "Vibrating means moving quickly to and fro about one place.",
                  "A guitar string vibrates when you pluck it.",
                  "A loudspeaker cone vibrates when an electrical signal drives it.",
                  "Your vocal folds vibrate when you speak or hum.",
                  "When the vibration stops, the sound stops."]},
        {"kind": "card", "title": "From source to listener",
         "body": [{"figure": "p6-03-chain"},
                  "The vibrating object pushes and pulls on the air next to it.",
                  "Each layer of air pushes on the next, so the vibration travels.",
                  "The air does not travel to you. Only the vibration does."]},
        {"kind": "card", "title": "Detecting sound",
         "body": ["When sound reaches a thin sheet, it makes the sheet vibrate too.",
                  "In your ear, the thin sheet is the eardrum.",
                  "Your ear turns these vibrations into nerve signals, which go to your brain.",
                  "In a microphone, the thin sheet is the diaphragm.",
                  "The microphone turns its vibrations into an electrical signal."]},
        {"kind": "reveal", "title": "Loudspeaker and microphone",
         "cols": ["Loudspeaker", "Microphone"],
         "rows": [
             ("What goes in", "An electrical signal", "Sound"),
             ("What vibrates", "A cone", "A diaphragm"),
             ("What comes out", "Sound", "An electrical signal"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Sound is made by the air.",
              "Sound is made by a vibrating object. The air carries it.", "WAVE-09"),
             ("An object you cannot see moving is not vibrating.",
              "Many vibrations are too small or too fast to see. You can often feel them.", "WAVE-10"),
             ("A microphone is a quiet loudspeaker.",
              "A microphone turns sound into an electrical signal. A loudspeaker does the reverse.", "WAVE-11"),
             ("Sound is stored inside an object until it gets out.",
              "Sound only exists while something vibrates. Stop the vibration and the sound stops.", "WAVE-12"),
         ]}]},
    ],
    "key_fact": "Sound is produced by vibrating objects. The vibration travels through the air and makes "
                "your eardrum, or a microphone's diaphragm, vibrate.",
    "deeper": [
        {"kind": "card", "title": "A tuning fork on a table",
         "body": ["A tuning fork held in the air sounds quiet.",
                  "Its thin prongs push very little air.",
                  "Stand its base on a table and it sounds much louder.",
                  "Now the whole table top vibrates and pushes on the air."]},
        {"kind": "card", "title": "One part, two jobs",
         "body": ["A loudspeaker can work as a microphone.",
                  "Talk into it and it makes a small electrical signal.",
                  "Some intercoms use one speaker for both jobs."]},
    ],
    "try": None,
    "tutor_body": "Want to trace how a sound gets from its source to your ear?",
    "ks4_becomes": "Sound waves in solids, liquids and gases, and the range of human hearing.",
    "figures": [
        {"id": "p6-03-chain", "kind": "diagram", "status": "drawn", "art": "p6-sound-chain",
         "title": "How a sound gets from its source to a listener",
         "desc": "Four numbered steps down the page, joined by arrows. Step 1, a source vibrates, drawn as a "
                 "plucked string at both ends of its swing. Step 2, the air passes it on, drawn as layers of "
                 "air bunched together then spread out. Step 3, a thin sheet vibrates, drawn as a curved "
                 "sheet with a double arrow. Step 4, it becomes a signal, drawn as a zigzag signal along a wire.",
         "caption": "Every sound follows these four steps.",
         "data": {"steps": [
             {"title": "A source vibrates",
              "lines": ["a string, a loudspeaker cone,", "or the vocal folds in your throat"]},
             {"title": "The air passes it on",
              "lines": ["the source pushes on the air,", "and each layer pushes the next"]},
             {"title": "A thin sheet vibrates",
              "lines": ["your eardrum, or the diaphragm", "inside a microphone"]},
             {"title": "It becomes a signal",
              "lines": ["a nerve signal to your brain,", "or an electrical signal"]},
         ]}},
    ],
    "figure_caption": {"p6-03-chain": None},     # the card text already says it
    "ladder_ticks": [
        ["Says the plucked string vibrates — moves quickly to and fro.",
         "Says the plucked string vibrates, moving quickly to and fro."],
        ["Says the eardrum passes the pattern on as nerve signals to the brain.",
         "Says the ear turns the eardrum's vibrations into nerve signals for the brain."],
    ],
    "ladder_feedback": {
        "recall": {
            1: "The sound leaves the glass through the air. The grip stops the glass vibrating.",
            2: "Sound is not stored in the glass. It only exists while the glass vibrates.",
            3: "The air in the room is unchanged. The grip takes energy from the glass itself.",
        },
        "apply": {
            0: "Neither one stores sound. Both convert between sound and an electrical signal.",
            1: "That is the wrong way round. A loudspeaker makes sound and a microphone detects it.",
            2: "A microphone takes sound in and gives out an electrical signal.",
        },
    },
}
