# -*- coding: utf-8 -*-
"""Sound waves and hearing, in the lean shape. LEGACY record: the Design batch-3 page keeps its
ladder (Ks4Ladder) and practice set, so their question ids survive. Spec table:
ks4-sound-waves-hearing.md (AQA 8463 4.6.1.4, physics only, HT only). TH only.

The practice set reads the route's quiz list (K.bank): both old quiz questions (SONAR echo time;
ultrasound against X-rays for scanning) are 4.6.1.5 content, not hearing, so both are replaced in
quiz-sound-waves-hearing.json. The page's worked examples (sound passing between air, water,
steel) are the (Physics only) 4.6.1.2 statement, which TH also studies.

logic_edits:
  1. pathFig drew the hearing path only stage by stage through the (removed) "From air to ear"
     bench: drawn always, complete (air, ear drum, small bones, cochlea, nerve), at 500 Hz.
  2. "as on the equation sheet": v = f λ is a recall equation, not on the sheet."""

LESSON = {
    "slug": "sound-waves-hearing",
    "start": {
        "setup": "A dog whistle is blown right next to your ear. You hear nothing, but the dog "
                 "comes running.",
        "question": "If you had to guess, why can you not hear it?",
        "options": [
            ("It is too quiet",
             "Its note is too high. Its frequency is above the limit of human hearing, but not "
             "above a dog's."),
            ("Its note is too high",
             "Its note is too high. Its frequency is above the limit of human hearing, but not "
             "above a dog's."),
        ],
        "answer": 1,
    },
    "words": ["vibration", "ear drum", "frequency", "range of hearing"],
    "knowledge": [
        {"kind": "card", "title": "Sound waves make solids vibrate",
         "body": ["Sound waves can travel through solids causing vibrations in the solid.",
                  {"points": [
                      "A loud lorry going past makes a shop window vibrate: sound waves into "
                      "vibrations of a solid.",
                      "A loudspeaker cone or a plucked guitar string vibrates and pushes on the "
                      "air: vibrations of a solid into sound waves.",
                  ]}]},
        {"kind": "card", "title": "Inside the ear",
         "body": ["Within the ear, sound waves cause the ear drum and other parts to vibrate, "
                  "which causes the sensation of sound.",
                  {"slot": "legacy-fig:pathFig"},
                  {"points": [
                      "Each compression pushes the ear drum in. Each rarefaction lets it move "
                      "out. So it vibrates at the same frequency as the sound.",
                      "Small bones pass the vibrations on to the cochlea, which sends signals "
                      "along a nerve to the brain.",
                  ]}]},
        {"kind": "card", "title": "The limits of hearing",
         "body": ["The conversion of sound waves to vibrations of solids works over a limited "
                  "frequency range. This restricts the limits of human hearing.",
                  "The range of normal human hearing is from 20 Hz to 20 kHz.",
                  "20 kHz = 20 000 Hz."]},
        {"kind": "reveal", "title": "Heard or not",
         "cols": ["Can a person hear it"],
         "rows": [
             ("12 Hz", "No: below 20 Hz"),
             ("800 Hz", "Yes"),
             ("15 000 Hz", "Yes"),
             ("25 kHz", "No: 25 000 Hz is above 20 kHz"),
         ]},
        {"kind": "card", "title": "Sound in different materials",
         "body": ["When sound passes from one material into another, its frequency stays the same. "
                  "Its speed changes, so its wavelength changes too: v = f λ.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The ear drum hears the sound.",
              "The ear drum vibrates. The parts behind it cause the sensation of sound."),
             ("20 kHz = 2000 Hz.", "20 kHz = 20 000 Hz."),
             ("You cannot hear a 30 kHz sound because it is too quiet.",
              "The limit is frequency: 30 kHz is above 20 kHz."),
         ]}]},
    ],
    "key_fact": "Sound waves can make solids vibrate: within the ear, sound waves cause the ear "
                "drum and other parts to vibrate, which causes the sensation of sound. This "
                "conversion only works over a limited frequency range, so normal human hearing is "
                "from 20 Hz to 20 kHz.",
    "deeper": [
        {"kind": "card", "title": "Above 20 kHz",
         "body": ["Sound above the upper limit of human hearing is ultrasound. It is used for "
                  "scanning and for echo sounding, in the lesson on waves for detection and "
                  "exploration."]},
        {"kind": "card", "title": "Microphones",
         "body": ["A microphone works like an ear drum. Sound waves make its thin diaphragm "
                  "vibrate at the same frequency as the sound."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> how a sound is heard: sound waves, ear drum vibrates, "
             "other parts vibrate, sensation of sound.",
             "<strong>Explain</strong> why a sound cannot be heard: the conversion only works "
             "over a limited range, and compare the frequency with 20 Hz to 20 kHz.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-3",
        "logic_edits": [
            ("pathFig: ready ? K.fig(this.pathSvg(fig), '') : null,",
             "pathFig: ready ? K.fig(this.pathSvg({ airOn: true, drumOn: true, inner: true, "
             "hz: 500 }), '') : null,"),
            ("placeholder: 'as on the equation sheet'", "placeholder: 'write the equation'"),
            # Blind-pass fixes (blind/RESULT.md), applied after the edits above.
            ("'40 kHz is above the upper limit of 20 kHz, so the ear drum does not vibrate enough.'",
             "'40 kHz is above the upper limit of 20 kHz, so it is outside the range the ear can convert.'"),
        ],
    },
}
