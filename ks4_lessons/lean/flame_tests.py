# -*- coding: utf-8 -*-
"""Flame tests, in the lean shape. New record, no legacy page (it replaces the old generate_site_v5
page). Spec table: ks4-flame-tests.md (AQA 8462 4.8.3.1, chemistry only; no 8464 section). Routes
TF and TH only; no HT-only lines, so both routes get the same lesson.

The five flame colours are AQA's own words. Flame colours of other metal ions are not required, so
none is taught. The electron explanation of flame colours is not in 8462 4.8.3.1 and is left out.
Required practical 7 (8462) is named here and taught in full with Metal hydroxides and Tests for
carbonates, halides and sulfates. The practice set reads the route's `quiz` list (K.bank):
quiz-flame-tests.json, five per route, both old stems kept."""

LESSON = {
    "slug": "flame-tests",
    "start": {
        "setup": "A clean wire loop is dipped in a white solid and held in a blue Bunsen flame. The "
                 "flame turns lilac.",
        "question": "If you had to guess, which metal ion is in the solid?",
        "options": [
            ("Potassium",
             "Potassium. Potassium compounds give a lilac flame. Sodium compounds give a yellow "
             "flame."),
            ("Sodium",
             "Potassium. Potassium compounds give a lilac flame. Sodium compounds give a yellow "
             "flame."),
        ],
        "answer": 0,
    },
    "words": ["flame test", "metal ion (cation)", "masked"],
    "knowledge": [
        {"kind": "card", "title": "What a flame test shows",
         "body": ["Flame tests can be used to identify some metal ions (cations).",
                  "Lithium, sodium, potassium, calcium and copper compounds produce distinctive "
                  "colours in flame tests."]},
        {"kind": "reveal", "title": "The five flame colours",
         "cols": ["Flame colour"],
         "rows": [
             ("Lithium compounds", "Crimson"),
             ("Sodium compounds", "Yellow"),
             ("Potassium compounds", "Lilac"),
             ("Calcium compounds", "Orange-red"),
             ("Copper compounds", "Green"),
         ]},
        {"kind": "card", "title": "How to do a flame test",
         "body": [{"points": [
             "1. Clean a wire loop: dip it in dilute hydrochloric acid, then hold it in a hot, "
             "blue Bunsen flame until the flame shows no colour.",
             "2. Dip the clean loop into the solid sample.",
             "3. Hold the loop at the edge of the blue flame.",
             "4. Record the colour of the flame.",
         ]},
                  "Clean the loop again before the next sample, so the last sample does not change "
                  "the colour."]},
        {"kind": "card", "title": "Mixtures can mask colours",
         "body": ["If a sample containing a mixture of ions is used, some flame colours can be "
                  "masked.",
                  "Sodium's yellow flame is very bright. It can hide the lilac flame of potassium."]},
        {"kind": "card", "title": "Required practical 7",
         "body": ["Use chemical tests to identify the ions in unknown single ionic compounds.",
                  "A flame test identifies some metal ions. Sodium hydroxide solution identifies "
                  "others. Then a test for the negative ion: carbonate, halide or sulfate.",
                  "Example: a white solid gives a yellow flame. With dilute nitric acid and silver "
                  "nitrate solution it gives a white precipitate. It contains sodium ions and "
                  "chloride ions, so it is sodium chloride."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Sodium gives a red flame.",
              "Sodium gives a yellow flame. Lithium gives a crimson flame."),
             ("Potassium gives a yellow flame.",
              "Potassium gives a lilac flame."),
             ("Lithium and calcium give the same colour.",
              "Lithium is crimson. Calcium is orange-red."),
             ("A flame test shows every metal ion in a mixture.",
              "In a mixture of ions, one colour can mask another."),
         ]}]},
    ],
    "key_fact": "Flame tests identify some metal ions: lithium compounds give a crimson flame, "
                "sodium yellow, potassium lilac, calcium orange-red and copper green. In a sample "
                "with a mixture of ions, some flame colours can be masked.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Flame emission spectroscopy is an instrumental version of the flame test. It "
                  "can identify the metal ions in a mixture. It is in Instrumental methods.",
                  "Calcium and magnesium both give a white precipitate with sodium hydroxide. A "
                  "flame test tells them apart: Metal hydroxides."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Identify</strong>: name the metal ion from the flame colour.",
             "<strong>Describe</strong> the test: clean loop, sample, blue flame, colour.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State the flame colour of lithium compounds.",
             "why": "Lithium compounds result in a crimson flame.",
             "options": [
                 {"text": "Yellow", "correct": False,
                  "reply": "Yellow is sodium. Lithium is crimson."},
                 {"text": "Lilac", "correct": False,
                  "reply": "Lilac is potassium. Lithium is crimson."},
                 {"text": "Crimson", "correct": True},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "A compound gives an orange-red flame. Identify the metal ion it contains.",
             "why": "Calcium compounds result in an orange-red flame.",
             "options": [
                 {"text": "Calcium", "correct": True},
                 {"text": "Copper", "correct": False,
                  "reply": "Copper compounds give a green flame."},
                 {"text": "Lithium", "correct": False,
                  "reply": "Lithium compounds give a crimson flame."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "Solid A gives a green flame. Solid B gives a yellow flame. Solid C gives a "
                       "lilac flame. Identify the metal ion in each solid.",
             "why": "Green is copper, yellow is sodium and lilac is potassium.",
             "options": [
                 {"text": "A copper, B potassium, C sodium", "correct": False,
                  "reply": "Yellow is sodium and lilac is potassium."},
                 {"text": "A copper, B sodium, C potassium", "correct": True},
                 {"text": "A calcium, B sodium, C lithium", "correct": False,
                  "reply": "Calcium is orange-red and lithium is crimson."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A solid contains sodium ions and potassium ions. Its flame test shows only a "
                       "yellow flame. Explain why.",
             "why": "The bright yellow flame of sodium masks the lilac flame of potassium.",
             "options": [
                 {"text": "Potassium ions give no colour in a flame", "correct": False,
                  "reply": "Potassium compounds give a lilac flame."},
                 {"text": "Sodium's yellow masks potassium's lilac", "correct": True},
                 {"text": "Potassium ions turn into sodium ions in the flame", "correct": False,
                  "reply": "A flame test does not change one metal ion into another."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how to carry out a flame test on a solid. Put the links in order.",
             "links": ["Clean a wire loop until it gives no colour in the flame.",
                       "Dip the clean loop into the solid, then hold it in a blue Bunsen flame.",
                       "Record the flame colour and compare it with the known colours."],
             "herrings": [{"text": "Hold the solid in the yellow safety flame.",
                           "why": "The yellow flame would hide the colours. Use a hot, blue flame."},
                          {"text": "Use the same loop for every sample without cleaning it.",
                           "why": "Some of the last sample would be left on the loop and change "
                                  "the colour."}]},
            {"kind": "chain", "command": "Identify", "marks": 3,
             "prompt": "A white solid gives a crimson flame. With dilute nitric acid and silver "
                       "nitrate solution it gives a yellow precipitate. Identify the compound. Put "
                       "the links in order.",
             "links": ["The flame test identifies the metal ion: a crimson flame is lithium.",
                       "The silver nitrate test then identifies the negative ion: yellow is "
                       "iodide.",
                       "Lithium ions with iodide ions make lithium iodide."],
             "herrings": [{"text": "A crimson flame is sodium.",
                           "why": "Sodium gives a yellow flame. Crimson is lithium."},
                          {"text": "A yellow precipitate is bromide.",
                           "why": "Bromide gives a cream precipitate. Yellow is iodide."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "A technician has three unlabelled white solids: lithium chloride, sodium "
                       "chloride and potassium chloride. Describe how flame tests could identify "
                       "each one. Give the result for each.",
             "points": ["Clean a wire loop (dilute hydrochloric acid, then a hot flame) before "
                        "each sample.",
                        "Dip the loop in the solid and hold it in a blue Bunsen flame.",
                        "Lithium chloride gives a crimson flame.",
                        "Sodium chloride gives a yellow flame.",
                        "Potassium chloride gives a lilac flame."],
             "reject": ["“Sodium chloride gives an orange-red flame.” Orange-red is "
                        "calcium.",
                        "“All three give the same colour, because they are all "
                        "chlorides.” The flame colour comes from the metal ion."]},
        ],
    },
}
