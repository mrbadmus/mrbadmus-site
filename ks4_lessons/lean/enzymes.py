# -*- coding: utf-8 -*-
"""Enzymes, in the lean shape. Spec table: ks4-enzymes.md (AQA 8464 4.2.2.1 / 8461 4.2.2.1, word for
word the same; the amylase practical is 8464 RP 4 / 8461 RP 5). Organs, sites of production,
bile and food tests are on The digestive system (the same spec point).

LEGACY (batch 2). The ladder and the practice set stay from the Design page. The practice set
and Rung 1 come from the route's subtopic quiz list (K.bank, and K.find with the needle "After an
enzyme-catalysed reaction"), so their fixes are in quiz-enzymes.json (quiz_org.py), not here.
This batch's logic is written with literal Unicode (no \\u escapes), so targets are plain text.

logic_edits:
  1. The eyebrow said "AQA Biology (8464)" on Combined routes: 8464 is Combined Science.
     The same edit binds `notTriple` by name, so lean_ks4's route-flag check sees it for the
     Combined-only practical card (R already carries it).
  2. Rung 3 link 3: "fewer enzyme–substrate complexes form" (beyond the spec's words) becomes
     "the substrate no longer fits the active site".
  3. The four CFIFA "Your turn" Formula placeholders said "learn it": rate = 1 ÷ time is a step
     for processing the practical's results, not an AQA equation to learn.
"""

LOGIC_EDITS = [
    ("eyebrow: R.isTriple ? 'AQA Biology (8461) 4.2.2.1 · Required practical' : 'AQA Biology (8464) 4.2.2.1 · Required practical',",
     "notTriple: !R.isTriple,\n      eyebrow: R.isTriple ? 'AQA Biology (8461) 4.2.2.1 · Required practical' : 'AQA Combined Science (8464) 4.2.2.1 · Required practical',"),
    ("'The substrate no longer fits, so fewer enzyme–substrate complexes form and the rate falls.'",
     "'The substrate no longer fits the active site, so the rate falls.'"),
    ("placeholder: 'learn it', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: '… = 1 ÷ time'",
     "placeholder: 'rate = …', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: '… = 1 ÷ time'"),
    ("placeholder: 'learn it', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 195'",
     "placeholder: 'rate = …', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 195'"),
    ("placeholder: 'learn it', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 60'",
     "placeholder: 'rate = …', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 60'"),
    ("placeholder: 'learn it', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 240'",
     "placeholder: 'rate = …', line: 'rate = 1 ÷ time' }, { letter: 'I', label: 'Insert', placeholder: 'rate = 1 ÷ …', line: 'rate = 1 ÷ 240'"),
]

_RP = [
    {"slot": "legacy-fig:rigFig"},
    {"points": [
        "Put amylase solution with a pH buffer in one tube, and starch solution in another. Stand "
        "both in a water bath, for example at 35 °C, so they reach the same temperature.",
        "Put a drop of iodine solution in each well of a spotting tile.",
        "Mix the amylase and the starch, and start a stopwatch.",
        "Every 30 seconds, put a drop of the mixture into a new well of iodine.",
        "When the iodine stays orange-brown, all the starch has been digested. Record the time.",
        "Repeat with buffers at different pH values. Keep the temperature, and the volumes and "
        "concentrations of amylase and starch, the same.",
    ]},
]

# Examiner pass (EXAMINER.md) and blind pass, 18 Nov 2026. Each old string is the logic AFTER the
# edits above, and occurs exactly once (validate.py checks).
LOGIC_EDITS += [
    ("links: ['Above the optimum temperature, the enzyme is denatured.', 'The shape of the active site changes.', 'The substrate no longer fits the active site, so the rate falls.'],",
     "links: ['The temperature rises above the optimum.', 'The shape of the active site changes, so the enzyme is denatured.', 'The substrate no longer fits the active site, so the rate falls.'],"),
    ("prompt: 'At pH 6, the iodine stayed orange-brown after 120 s. Calculate the rate of reaction.",
     "prompt: 'At pH 6, the iodine first stayed orange-brown at 120 s: all the starch had been digested. Calculate the rate of reaction in ' + S1 + '."),
    ("head: 'At pH 6, the iodine stayed orange-brown after 75 s. Calculate the rate of reaction.",
     "head: 'At pH 6, the iodine first stayed orange-brown at 75 s: all the starch had been digested. Calculate the rate of reaction in ' + S1 + '."),
    ("head: 'At pH 7, the iodine stayed orange-brown after 90 s. Calculate the rate of reaction.",
     "head: 'At pH 7, the iodine first stayed orange-brown at 90 s: all the starch had been digested. Calculate the rate of reaction in ' + S1 + '."),
]

LESSON = {
    "slug": "enzymes",
    "start": {
        "setup": "Amylase digests starch quickly at body temperature.",
        "question": "If you had to guess, what happens if you boil the amylase first?",
        "options": [
            ("It digests the starch faster",
             "It stops working. Boiling changes the shape of its active site, so the enzyme is "
             "denatured and the starch no longer fits."),
            ("It stops working",
             "It stops working. Boiling changes the shape of its active site, so the enzyme is "
             "denatured and the starch no longer fits."),
        ],
        "answer": 1,
    },
    "words": ["enzyme", "active site", "denatured", "optimum"],
    "knowledge": [
        {"kind": "card", "title": "What enzymes are",
         "body": ["Enzymes are biological catalysts. They speed up reactions in living organisms "
                  "and are not used up.",
                  "Enzymes are large protein molecules. Each one has an active site with a "
                  "particular shape.",
                  "Enzymes catalyse specific reactions in living organisms due to the shape of "
                  "their active site."]},
        {"kind": "card", "title": "The lock and key model",
         "body": ["The substrate fits into the active site like a key in a lock.",
                  {"slot": "legacy-fig:fitFig"},
                  "Only P has the right shape to fit this active site, so only P is broken down.",
                  {"points": [
                      "The substrate binds to the active site.",
                      "The enzyme breaks it down into products.",
                      "The products are released. The enzyme is unchanged, so it can be used "
                      "again.",
                  ]},
                  "The lock and key theory is a simplified model of how enzymes work."]},
        {"kind": "card", "title": "Temperature",
         "body": [{"slot": "fig:enzyme-rate-temperature"},
                  {"points": [
                      "Up to the optimum, a higher temperature makes the molecules move faster, so "
                      "the substrate and the active site collide more often. The rate increases.",
                      "Above the optimum, the shape of the active site changes, so the substrate "
                      "no longer fits. The enzyme is denatured and the rate falls quickly.",
                  ]},
                  "Many enzymes in the human body work best at about 37 °C."]},
        {"kind": "card", "title": "pH",
         "body": [{"slot": "fig:enzyme-rate-ph"},
                  "Each enzyme works best at its optimum pH. At a pH far above or below it, the "
                  "shape of the active site changes and the enzyme is denatured.",
                  "Different enzymes have different optimum pH values. The protease made in the "
                  "stomach works best in acid conditions."]},
        {"kind": "card", "title": "Required practical 4: pH and amylase", "routes": ["CF", "CH"],
         "body": _RP},
        {"kind": "card", "title": "Required practical 5: pH and amylase", "routes": ["TF", "TH"],
         "body": _RP},
        {"kind": "card", "title": "Calculating the rate",
         "body": ["To process the results, rate = 1 ÷ time, with the time in seconds. The unit is "
                  "s⁻¹, which means per second.",
                  "The shortest time gives the fastest rate. Of the pH values tested, that one is closest to the optimum.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A high temperature kills the enzyme.",
              "Enzymes are not alive. A high temperature denatures them."),
             ("The enzyme is used up in the reaction.",
              "The enzyme is unchanged, so it can be used again."),
             ("Every enzyme works best at pH 7.",
              "Different enzymes have different optimum pH values."),
         ]}]},
    ],
    "key_fact": "Enzymes are biological catalysts. Each one catalyses a specific reaction, because "
                "only a substrate with the right shape fits its active site. Above the optimum "
                "temperature, or far from the optimum pH, the active site changes shape and the "
                "enzyme is denatured, so the rate falls.",
    "deeper": [
        {"kind": "card", "title": "Enzymes and metabolism",
         "body": ["Metabolism is the sum of all the reactions in a cell or the body. Enzymes "
                  "control these reactions. Metabolism has the details."]},
        {"kind": "card", "title": "Where the model is too simple",
         "body": ["In a real enzyme, the active site changes shape slightly as the substrate "
                  "binds. The lock and key model leaves this out."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Explain</strong> a fall in rate: name the change in the active site, then "
             "say the substrate no longer fits.",
             "<strong>Describe</strong> the practical: buffer, water bath, iodine every 30 "
             "seconds, record the time.",
             "<strong>Calculate</strong> the rate: time in seconds first, then 1 ÷ time.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-2", "logic_edits": LOGIC_EDITS},
}
