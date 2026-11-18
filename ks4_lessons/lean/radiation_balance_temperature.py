# -*- coding: utf-8 -*-
"""Radiation balance and the Earth's temperature, in the lean shape. New record, no legacy page.
Spec table: ks4-radiation-balance-temperature.md (AQA 8463 4.6.3.2 (physics only) (HT only)).
TH only. Not on 8464. The old spec field "6.6.5.4" is not a real point.

The lead's ruling: this page owns the 4.6.3.2 (HT only) statements; infrared-black-bodies only
points here. Greenhouse gas detail belongs to chemistry (8462 4.9.2): one line in Dive deeper.
"Thermal equilibrium" (Rainford SOW) is not spec wording: left out. Both old quiz questions
(molecular vibrations of greenhouse gases; −18 °C without a greenhouse effect) were beyond this
spec point and are replaced."""

LESSON = {
    "slug": "radiation-balance-temperature",
    "start": {
        "setup": "A rock sits in the sunshine. Its temperature has stopped changing.",
        "question": "If you had to guess, is the rock still absorbing radiation from the Sun?",
        "options": [
            ("Yes, as fast as it emits it",
             "Yes. A body at constant temperature is absorbing radiation at the same rate as it "
             "is emitting radiation."),
            ("No, it has stopped",
             "Yes. A body at constant temperature is absorbing radiation at the same rate as it "
             "is emitting radiation."),
        ],
        "answer": 0,
    },
    "words": ["absorb", "emit", "reflect", "constant temperature"],
    "knowledge": [
        {"kind": "card", "title": "Every body absorbs and emits",
         "body": ["All bodies emit and absorb infrared radiation, whatever their temperature.",
                  "The hotter the body, the more infrared radiation it radiates in a given time."]},
        {"kind": "reveal", "title": "The balance",
         "cols": ["What happens to its temperature"],
         "rows": [
             ("Absorbs radiation faster than it emits", "The temperature increases"),
             ("Absorbs and emits at the same rate", "The temperature stays constant"),
             ("Emits radiation faster than it absorbs", "The temperature decreases"),
         ]},
        {"kind": "card", "title": "An everyday example",
         "body": [{"points": [
             "A car is parked in strong sunshine. It absorbs radiation faster than it emits it, "
             "so its temperature increases.",
             "As it gets hotter, it emits more radiation each second.",
             "When it emits radiation at the same rate as it absorbs it, its temperature stays "
             "constant.",
         ]}]},
        {"kind": "card", "title": "The Earth's temperature",
         "body": ["The temperature of the Earth depends on many factors, including the rates of "
                  "absorption and emission of radiation, and reflection of radiation into space.",
                  {"slot": "fig:earth-radiation-balance"},
                  {"points": [
                      "Some radiation from the Sun is reflected back into space, for example by "
                      "ice and snow. It does not warm the Earth.",
                      "The rest is absorbed by the Earth's surface and atmosphere, which warms "
                      "them.",
                      "The Earth's surface emits infrared radiation. Some escapes into space.",
                      "Some is absorbed by the atmosphere, which emits infrared radiation back "
                      "towards the surface.",
                  ]}]},
        {"kind": "card", "title": "When the balance changes",
         "body": [{"points": [
             "If the Earth absorbs radiation faster than it emits radiation into space, its "
             "temperature increases.",
             "If the two rates are equal, its temperature stays constant.",
         ]}]},
        {"kind": "reveal", "title": "What changes the Earth's temperature",
         "cols": ["Effect on the temperature"],
         "rows": [
             ("More of the Earth is covered in ice and snow, so more radiation is reflected into "
              "space", "Less radiation is absorbed, so the temperature falls"),
             ("Ice and snow melt, so less radiation is reflected into space",
              "More radiation is absorbed, so the temperature rises"),
             ("The atmosphere absorbs more of the infrared emitted by the surface",
              "Less radiation escapes into space, so the temperature rises"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A body at constant temperature has stopped emitting radiation.",
              "It is still emitting, at the same rate as it absorbs."),
             ("Only hot objects emit radiation.",
              "All bodies emit radiation, whatever their temperature."),
             ("Radiation reflected into space warms the Earth.",
              "Reflected radiation is not absorbed, so it does not warm the Earth."),
         ]}]},
    ],
    "key_fact": "A body at constant temperature is absorbing radiation at the same rate as it is "
                "emitting radiation, and its temperature increases when it absorbs radiation "
                "faster than it emits radiation. The temperature of the Earth depends on the "
                "rates of absorption and emission of radiation, and on how much radiation is "
                "reflected into space.",
    "deeper": [
        {"kind": "card", "title": "The greenhouse effect",
         # Reworded 16 Nov 2026 on Mide's ruling: as close to AQA's own wording as the lesson
         # allows (8462 4.9.2.1, the chemistry spec point named below), nothing beyond it.
         "body": ["Greenhouse gases in the atmosphere maintain temperatures on Earth high enough "
                  "to support life. Water vapour, carbon dioxide and methane are greenhouse gases.",
                  "The greenhouse effect is about short and long wavelength radiation: short "
                  "wavelength radiation from the Sun passes through the atmosphere, and greenhouse "
                  "gases absorb some of the long wavelength (infrared) radiation the Earth emits.",
                  "You meet this in chemistry, in the topic on the atmosphere."]},
        {"kind": "card", "title": "Reading a radiation diagram",
         "body": [{"points": [
             "Follow each arrow from the Sun and say whether it is reflected into space or "
             "absorbed.",
             "Follow each arrow from the surface and say whether it escapes into space or is "
             "absorbed by the atmosphere.",
             "Then compare: radiation absorbed against radiation emitted into space.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong> a change in temperature: compare the rate of absorbing "
             "radiation with the rate of emitting it.",
             "<strong>Use the diagram</strong>: name what is reflected, absorbed and emitted.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what is true of a body at constant temperature.",
             "why": "A body at constant temperature is absorbing radiation at the same rate as it "
                    "is emitting radiation.",
             "options": [
                 {"text": "It absorbs and emits at the same rate", "correct": True},
                 {"text": "It has stopped absorbing radiation", "correct": False,
                  "reply": "It is still absorbing, at the same rate as it emits."},
                 {"text": "It has stopped emitting radiation", "correct": False,
                  "reply": "All bodies emit radiation, whatever their temperature."},
                 {"text": "It emits radiation faster than it absorbs it", "correct": False,
                  "reply": "Then its temperature would decrease."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give what happens to the temperature of a body that absorbs radiation "
                       "faster than it emits radiation.",
             "why": "The temperature of a body increases when it absorbs radiation faster than it "
                    "emits radiation.",
             "options": [
                 {"text": "It decreases", "correct": False,
                  "reply": "It gains energy faster than it loses it, so it gets hotter."},
                 {"text": "It increases", "correct": True},
                 {"text": "It stays constant", "correct": False,
                  "reply": "It stays constant only when the two rates are equal."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "In the morning a rock absorbs 300 J of radiation each second and emits "
                       "200 J each second. At midday it absorbs 300 J and emits 300 J each second. "
                       "Describe its temperature at each time.",
             "why": "Absorbing faster than emitting makes the temperature rise. Equal rates keep "
                    "it constant.",
             "options": [
                 {"text": "Rising in the morning, constant at midday", "correct": True},
                 {"text": "Constant in the morning, rising at midday", "correct": False,
                  "reply": "In the morning it absorbs faster than it emits, so it is warming up."},
                 {"text": "Falling in the morning, constant at midday", "correct": False,
                  "reply": "It absorbs more than it emits, so it cannot be cooling."},
                 {"text": "Rising at both times", "correct": False,
                  "reply": "At midday the rates are equal, so the temperature is constant."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Ice and snow melt, so less of the Sun's radiation is reflected into space. "
                       "Identify the effect on the Earth.",
             "why": "Less reflected means more absorbed, so the temperature rises.",
             "options": [
                 {"text": "More radiation is absorbed, so the temperature rises", "correct": True},
                 {"text": "Less radiation is absorbed, so the temperature falls", "correct": False,
                  "reply": "Radiation that is not reflected is absorbed instead."},
                 {"text": "The Earth stops emitting radiation", "correct": False,
                  "reply": "The Earth always emits infrared radiation."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a car left in the sunshine stops getting hotter after a "
                       "while. Put the links in order.",
             "links": ["At first the car absorbs radiation faster than it emits it, so its "
                       "temperature rises.",
                       "As its temperature rises, it emits more radiation each second.",
                       "When it emits radiation as fast as it absorbs it, its temperature stays "
                       "constant."],
             "herrings": [{"text": "The car stops absorbing radiation once it is hot.",
                           "why": "It keeps absorbing. It now emits just as fast."},
                          {"text": "The car stops emitting radiation in the sunshine.",
                           "why": "All bodies emit radiation, and a hotter car emits more."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why the Earth's temperature rises if the atmosphere absorbs more "
                       "of the infrared emitted by the Earth's surface. Put the links in order.",
             "links": ["The atmosphere absorbs more of the infrared emitted by the surface.",
                       "So less radiation escapes into space each second.",
                       "The Earth now absorbs radiation faster than it emits it into space, so its "
                       "temperature increases."],
             "herrings": [{"text": "The atmosphere reflects more of the Sun's radiation into "
                                   "space.",
                           "why": "That would mean less is absorbed, which would cool the Earth."},
                          {"text": "The Earth's surface stops emitting infrared.",
                           "why": "The surface keeps emitting. Less of it escapes into space."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "Explain how the temperature of the Earth depends on the radiation it "
                       "absorbs, reflects and emits.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear, linked account of reflection, "
                  "absorption and emission, related to the balance that sets the temperature.",
                  "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Two of reflection, absorption and emission "
                  "described, with some link to the temperature.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant points.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Some radiation from the Sun is reflected into space and does not warm the "
                        "Earth.",
                        "The rest is absorbed by the surface and the atmosphere, which warms them.",
                        "The Earth's surface emits infrared radiation.",
                        "Some escapes into space; some is absorbed by the atmosphere and emitted "
                        "back towards the surface.",
                        "If the Earth absorbs radiation faster than it emits it into space, its "
                        "temperature rises.",
                        "If the two rates are equal, its temperature stays constant."],
             "reject": ["“Reflected radiation heats the Earth.”",
                        "“The Earth only emits radiation at night.”"]},
        ],
    },
}
