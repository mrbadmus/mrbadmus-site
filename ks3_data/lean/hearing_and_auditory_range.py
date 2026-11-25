# -*- coding: utf-8 -*-
"""Hearing and auditory range, in the lean shape.
Spec table: docs/lessons/wave2/ks3-hearing-and-auditory-range.md."""

LESSON = {
    "slug": "hearing-and-auditory-range",
    "start": {
        "setup": "A dog whistle is blown hard in a quiet room. No person hears it, but the dog does.",
        "question": "If you had to guess, is the whistle too quiet for people to hear, or too high?",
        "options": [
            ("Too quiet",
             "A microphone shows the sound is loud. It is too high for human ears."),
            ("Too high",
             "Right. Its frequency is above 20 000 Hz, the top of the human range."),
        ],
        "answer": 1,
    },
    "words": ["cochlea", "auditory range", "infrasound", "ultrasound"],
    "word_defs": {
        "cochlea": "A coiled tube of liquid in the inner ear. It turns vibrations into electrical impulses.",
        "auditory range": "The range of frequencies an ear can hear, from the lowest to the highest.",
        "infrasound": "Sound below about 20 Hz. It is too low for humans to hear.",
        "ultrasound": "Sound above about 20 000 Hz. It is too high for humans to hear.",
    },
    "knowledge": [
        {"kind": "card", "title": "How the ear hears",
         "body": [{"figure": "p6-ear-parts"},
                  "Sound waves travel into the ear and make the eardrum vibrate.",
                  "Each part passes the vibration on to the next.",
                  "In the cochlea, the vibrations are turned into electrical impulses.",
                  "The auditory nerve carries the impulses to the brain.",
                  "The brain turns the impulses into the sound you hear."]},
        {"kind": "reveal", "title": "What each part of the ear does",
         "cols": ["What it does"],
         "rows": [
             ("Outer ear", "Collects sound waves and funnels them into the ear canal."),
             ("Ear canal", "Carries the sound waves to the eardrum."),
             ("Eardrum", "A thin skin that vibrates when sound waves hit it."),
             ("Ossicles", "Three tiny bones. They pass the vibrations on and make them stronger."),
             ("Cochlea", "Tiny hair cells in its liquid turn vibrations into electrical impulses."),
             ("Auditory nerve", "Carries the electrical impulses to the brain."),
         ]},
        {"kind": "reveal", "title": "Problems that affect hearing",
         "cols": ["What goes wrong"],
         "rows": [
             ("Very loud sounds", "Damage the hair cells in the cochlea. This hearing loss is permanent."),
             ("Getting older", "Hair cells are lost, so the highest frequencies go first."),
             ("A burst eardrum", "A loud bang or an infection can tear the eardrum. It usually heals."),
             ("Ear wax", "A build up of wax blocks the ear canal, so sounds are muffled."),
             ("An ear infection", "Liquid fills the space behind the eardrum, so sounds are muffled."),
         ]},
        {"kind": "card", "title": "Protecting your hearing",
         "body": ["Wear ear defenders or earplugs near loud machines and at concerts.",
                  "Keep the volume on your headphones low.",
                  "A hearing aid makes sounds louder for someone with hearing loss."]},
        {"kind": "card", "title": "Your auditory range",
         "body": [{"figure": "p6-ear-range-human"},
                  "Your auditory range is the range of frequencies you can hear.",
                  "A healthy young person hears from about 20 Hz to 20 000 Hz.",
                  "Sound below 20 Hz is infrasound. Sound above 20 000 Hz is ultrasound.",
                  "Both are real sound waves. Human ears cannot detect them.",
                  "As you get older, the top of your range comes down."]},
        {"kind": "reveal", "title": "What kind of sound is it",
         "cols": ["Kind of sound"],
         "rows": [
             ("10 Hz", "Infrasound, because it is below 20 Hz."),
             ("1000 Hz", "Sound humans can hear."),
             ("18 000 Hz", "Sound a young person can hear. Many older people cannot."),
             ("50 000 Hz", "Ultrasound, because it is above 20 000 Hz."),
         ]},
        {"kind": "card", "title": "Animals hear different ranges",
         "body": [{"figure": "p6-ear-range-animals"},
                  "A dog hears up to about 45 000 Hz, so it hears a dog whistle.",
                  "A bat hears up to about 110 000 Hz.",
                  "An elephant hears down to about 16 Hz. It only hears up to about 12 000 Hz.",
                  "So no animal hears every frequency. Each range sits in a different place."]},
        {"kind": "card", "title": "Why bats use ultrasound",
         "body": ["Bats find insects in the dark using echoes.",
                  "A higher frequency sound has a shorter wavelength.",
                  "Short wavelengths reflect well off small things, like a moth.",
                  "So bats call with ultrasound, and their ears can hear the echoes."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A dog whistle makes no sound.",
              "It makes a loud sound. Its frequency is too high for human ears.", "WAVE-29"),
             ("Losing the top of your range just makes everything quieter.",
              "You stop hearing high frequencies, so some speech sounds are hard to tell apart.",
              "WAVE-30"),
             ("Ultrasound is a different kind of wave from ordinary sound.",
              "Ultrasound is ordinary sound, at a frequency too high for humans to hear.", "WAVE-31"),
             ("Animals hear better than people do.",
              "Animals hear different ranges. An elephant hears lower than us, but not as high.",
              "WAVE-32"),
             ("Everyone can hear up to 20 000 Hz.",
              "That is for young people. The top of the range falls with age."),
         ]}]},
    ],
    "key_fact": "In the cochlea, the ear turns vibrations into electrical impulses. "
                "The auditory nerve carries them to the brain. "
                "Young people hear from about 20 Hz to 20 000 Hz. "
                "Sound below 20 Hz is infrasound, and sound above 20 000 Hz is ultrasound.",
    "deeper": [
        {"kind": "card", "title": "Noise damage lasts",
         "body": ["Hair cells in the cochlea do not grow back in humans.",
                  "Loud noise damages the ones that detect high frequencies first.",
                  "Ringing in your ears after a concert, called tinnitus, is a warning sign."]},
        {"kind": "card", "title": "Cochlear implants",
         "body": ["Some people have hair cells that are too damaged for a hearing aid to help.",
                  "A cochlear implant sends electrical signals straight to the auditory nerve.",
                  "The brain learns to turn these signals into sounds."]},
    ],
    "try": None,
    "tutor_body": "Want to check which animals could hear a particular frequency?",
    "ks4_becomes": None,      # AQA teaches the hearing range and ultrasound in GCSE Physics only, not every route
    "figures": [
        {"id": "p6-ear-parts", "kind": "diagram", "status": "drawn", "art": "p6-ear-parts",
         "title": "The parts of the ear",
         "desc": "A side-on sketch of the ear. From left to right: the outer ear flap, the ear canal with an "
                 "arrow showing sound coming in, the eardrum, three tiny linked bones called the ossicles, "
                 "the coiled cochlea, and the auditory nerve running up to the brain. Each part is "
                 "labelled.",
         "caption": "Sound goes in through the ear canal. The auditory nerve carries impulses to the brain.",
         "data": {"labels": {"outer": "outer ear", "canal": "ear canal", "eardrum": "eardrum",
                             "bones": "ossicles", "cochlea": "cochlea", "nerve": "auditory nerve",
                             "brain": "brain"}}},
        {"id": "p6-ear-range-human", "kind": "diagram", "status": "drawn", "art": "p6-ear-range",
         "title": "The human auditory range",
         "desc": "A frequency scale from 1 Hz to 300 000 Hz, where each mark is ten times the one before: "
                 "1, 10, 100, 1000, 10 000 and 100 000 Hz. A dashed line at 20 Hz and a dashed line at "
                 "20 000 Hz split it into three zones: infrasound below 20 Hz, humans hear in the middle, "
                 "ultrasound above 20 000 Hz. A bar for a young person runs from 20 Hz to 20 000 Hz. A bar "
                 "for a person aged about 50 runs from 20 Hz to 12 000 Hz.",
         "caption": "Each mark on the scale is ten times the one before.",
         "data": {"zones": {"infra": "Infrasound", "human": "Humans hear", "ultra": "Ultrasound"},
                  "axis": "Frequency (Hz)", "note": "Each mark is ten times the one before",
                  "rows": [{"label": "Young person", "lo": 20, "hi": 20000},
                           {"label": "Person aged 50", "lo": 20, "hi": 12000}]}},
        {"id": "p6-ear-range-animals", "kind": "diagram", "status": "drawn", "art": "p6-ear-range",
         "title": "Auditory ranges of people and animals",
         "desc": "The same frequency scale, with the infrasound and ultrasound zones marked at 20 Hz and "
                 "20 000 Hz. Four bars: elephant from 16 Hz to 12 000 Hz; young person from 20 Hz to "
                 "20 000 Hz; dog from 67 Hz to 45 000 Hz; bat from 2000 Hz to 110 000 Hz.",
         "caption": "Each animal hears a different range of frequencies.",
         "data": {"zones": {"infra": "Infrasound", "human": "Humans hear", "ultra": "Ultrasound"},
                  "axis": "Frequency (Hz)", "note": "Each mark is ten times the one before",
                  "rows": [{"label": "Elephant", "lo": 16, "hi": 12000},
                           {"label": "Young person", "lo": 20, "hi": 20000},
                           {"label": "Dog", "lo": 67, "hi": 45000},
                           {"label": "Bat", "lo": 2000, "hi": 110000}]}},
    ],
    "figure_caption": {"p6-ear-range-animals": None},     # the card text already says it
    "ladder_stem": {
        "produce": "Some shops have fitted a device outside the door. It sounds a constant tone at "
                   "about 17 000 Hz. Explain who is likely to hear it and who is not. Give one reason "
                   "people have argued about whether these devices should be allowed.",
    },
    "ladder_ticks": [
        ["Says the tone reaches everyone in the street, not only the people it is aimed at — including babies and people who happen to be passing.",
         "Says the tone reaches everyone nearby, such as babies and people walking past."],
    ],
    "ladder_feedback": {
        "recall": {
            1: "Ultrasound is real sound. A dog hears up to about 45 000 Hz, so it hears this.",
            2: "An elephant hears up to only about 12 000 Hz. It cannot hear 30 000 Hz.",
            3: "How far a sound carries does not matter. Above an ear's range, it hears nothing.",
        },
        "apply": {
            0: "The tone is loud. Turning it up would not help, because it is too high.",
            1: "All sounds travel at the same speed in air. The frequency is what matters.",
            2: "A microphone picks up a loud tone. The whistle does make a sound.",
        },
    },
}
