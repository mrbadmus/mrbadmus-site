# -*- coding: utf-8 -*-
"""Instrumental methods and flame emission spectroscopy, in the lean shape. New record, no legacy
page (it replaces the old generate_site_v5 page). Spec table: ks4-instrumental-methods.md (AQA 8462
4.8.3.6 and 4.8.3.7, chemistry only; no 8464 section). Routes TF and TH only; no HT-only lines, so
both routes get the same lesson.

Left out, as beyond 8462: electrons and energy levels, other instruments (mass spectrometry,
infrared, gas chromatography), named wavelengths as facts to learn. The wavelengths in the spectra
figure and the ladder are data given in the question, as the spec's "reference set" asks. Figure
wanted: fig:emission-spectra (BRIEF-AN.md). The practice set reads the route's `quiz` list (K.bank):
quiz-instrumental-methods.json, five per route, both old stems kept."""

LESSON = {
    "slug": "instrumental-methods",
    "start": {
        "setup": "A water company checks its drinking water for tiny amounts of metal ions. It "
                 "tests thousands of samples a week.",
        "question": "If you had to guess, which is the better way to test them?",
        "options": [
            ("With an instrument",
             "With an instrument. Instrumental methods are accurate, sensitive and rapid, so they "
             "can find tiny amounts in many samples quickly."),
            ("With chemical tests in test tubes",
             "With an instrument. Instrumental methods are accurate, sensitive and rapid, so they "
             "can find tiny amounts in many samples quickly."),
        ],
        "answer": 0,
    },
    "words": ["instrumental method", "flame emission spectroscopy", "spectroscope", "line spectrum"],
    "knowledge": [
        {"kind": "card", "title": "Instrumental methods",
         "body": ["Elements and compounds can be detected and identified using instrumental "
                  "methods.",
                  "Instrumental methods are accurate, sensitive and rapid.",
                  "Forensic scientists and drug control scientists rely on them, because the "
                  "amount of chemical to analyse is often very small."]},
        {"kind": "reveal", "title": "Instrumental methods compared with chemical tests",
         "cols": ["Instrumental method", "Chemical test"],
         "rows": [
             ("How small an amount", "Sensitive: it detects very small amounts",
              "Needs enough of the ion to see a colour or a precipitate"),
             ("Speed", "Rapid: many samples quickly", "Slower: one sample and one test at a time"),
             ("Result", "Accurate, and can measure how much is there",
              "Shows which ion is there, not how much"),
             ("Mixtures", "Can identify the metal ions in a mixture",
              "In a flame test, one colour can mask another"),
         ]},
        {"kind": "card", "title": "Flame emission spectroscopy",
         "body": ["Flame emission spectroscopy is an example of an instrumental method used to "
                  "analyse metal ions in solutions.",
                  {"points": [
                      "The sample is put into a flame.",
                      "The light given out is passed through a spectroscope.",
                      "The output is a line spectrum.",
                      "The line spectrum can be analysed to identify the metal ions in the "
                      "solution and measure their concentrations.",
                  ]}]},
        {"kind": "card", "title": "Reading a line spectrum",
         "body": ["Each metal ion gives its own pattern of lines. Compare the sample's spectrum "
                  "with reference spectra of known metal ions.",
                  {"slot": "fig:emission-spectra"},
                  {"points": [
                      "A metal ion is present when every one of its reference lines is in the "
                      "sample's spectrum.",
                      "A sample with two metal ions shows the lines of both.",
                      "The brighter a metal ion's lines, the higher its concentration.",
                  ]}]},
        {"kind": "reveal", "title": "Which metal ions are in each sample",
         "cols": ["Metal ions present"],
         "rows": [
             ("Sample X: lines at 589, 610 and 671\u00a0nm", "Sodium and lithium"),
             ("Sample Y: lines at 404 and 766\u00a0nm", "Potassium only"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Instrumental methods are used because they are cheap.",
              "They are used because they are accurate, sensitive and rapid. The instruments are "
              "expensive."),
             ("A line spectrum only shows which metal ion is there.",
              "It also measures the concentration of each metal ion."),
             ("One matching line is enough to identify a metal ion.",
              "Every line in the metal ion's reference spectrum must be in the sample's "
              "spectrum."),
         ]}]},
    ],
    "key_fact": "Instrumental methods are accurate, sensitive and rapid. In flame emission "
                "spectroscopy, the sample is put into a flame and the light given out is passed "
                "through a spectroscope. The line spectrum identifies the metal ions in the "
                "solution and measures their concentrations.",
    "deeper": [
        {"kind": "card", "title": "Drawbacks of instruments",
         "body": ["The instruments are expensive, and they need trained people to run them.",
                  "They must be checked against samples of known concentration before use."]},
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Flame tests are the chemical test that flame emission spectroscopy replaces. "
                  "A flame test shows one colour, and in a mixture one colour can mask another."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>State</strong> an advantage: accurate, sensitive or rapid.",
             "<strong>Use the spectra</strong>: match every line of each reference spectrum to a "
             "line in the sample's spectrum.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give one advantage of instrumental methods compared with chemical tests.",
             "why": "Instrumental methods are accurate, sensitive and rapid.",
             "options": [
                 {"text": "They are cheaper to set up", "correct": False,
                  "reply": "The instruments are expensive."},
                 {"text": "They are more sensitive", "correct": True},
                 {"text": "They need no electricity", "correct": False,
                  "reply": "Instruments need electricity. Their advantage is accuracy, "
                           "sensitivity and speed."},
             ]},
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "A sample is put into a flame. The light given out is analysed to identify "
                       "the metal ions. What is the light passed through?",
             "why": "The light given out is passed through a spectroscope.",
             "options": [
                 {"text": "A spectroscope", "correct": True},
                 {"text": "A microscope", "correct": False,
                  "reply": "A microscope magnifies. A spectroscope gives a line spectrum."},
                 {"text": "A filter paper", "correct": False,
                  "reply": "Filter paper separates solids from liquids. The light goes through a "
                           "spectroscope."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Use", "marks": 2,
             "prompt": "Reference lines: sodium 589\u00a0nm; potassium 404\u00a0nm and 766\u00a0nm; lithium 610\u00a0nm "
                       "and 671\u00a0nm. A sample's spectrum has lines at 404, 589 and 766\u00a0nm. Which "
                       "metal ions are in the sample?",
             "why": "589\u00a0nm matches sodium, and 404\u00a0nm and 766\u00a0nm match potassium. Lithium's lines "
                    "are missing.",
             "options": [
                 {"text": "Sodium and lithium", "correct": False,
                  "reply": "There are no lines at 610\u00a0nm or 671\u00a0nm, so lithium is not there."},
                 {"text": "Sodium and potassium", "correct": True},
                 {"text": "Potassium only", "correct": False,
                  "reply": "The line at 589\u00a0nm is sodium, so sodium is there too."},
             ]},
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "A solution contains sodium ions and potassium ions. Explain why flame "
                       "emission spectroscopy can identify both, but a flame test may not.",
             "why": "The spectrum shows the lines of both metal ions. In a flame test, sodium's "
                    "yellow can mask potassium's lilac.",
             "options": [
                 {"text": "Its spectrum has lines for both ions, but in a flame test yellow masks "
                          "lilac",
                  "correct": True},
                 {"text": "Its flame is hotter, so the sodium ions burn away before the potassium "
                          "ions",
                  "correct": False,
                  "reply": "The ions do not burn away. Both give their own lines."},
                 {"text": "Its spectrum has one line for the mixture, but a flame test shows two "
                          "colours",
                  "correct": False,
                  "reply": "It is the other way round: the spectrum shows lines for each ion."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how flame emission spectroscopy identifies the metal ions in a "
                       "solution. Put the links in order.",
             "links": ["The sample is put into a flame.",
                       "The light given out is passed through a spectroscope, which gives a line "
                       "spectrum.",
                       "The line spectrum is compared with reference spectra to identify the metal "
                       "ions."],
             "herrings": [{"text": "The sample is passed through a spectroscope, then put into a "
                                   "flame.",
                           "why": "It is the light from the flame that goes through the "
                                  "spectroscope."},
                          {"text": "The colour of the flame is matched by eye.",
                           "why": "That is a flame test. The spectroscope gives a line spectrum."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A drug control scientist tests hundreds of urine samples a day for tiny "
                       "amounts of a banned drug. Explain why an instrumental method is used. Put "
                       "the links in order.",
             "links": ["Each sample may contain only a tiny amount of the drug.",
                       "Instrumental methods are sensitive, so they can detect very small "
                       "amounts.",
                       "They are also rapid and accurate, so many samples can be tested quickly "
                       "and the results trusted."],
             "herrings": [{"text": "Instrumental methods need large samples to work.",
                           "why": "They are sensitive: they work with very small amounts."},
                          {"text": "Chemical tests are always more accurate than instruments.",
                           "why": "Instrumental methods are accurate, sensitive and rapid."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Compare", "marks": 4,
             "prompt": "A scientist must find which metal ions are in a solution, and how much of "
                       "each. Compare using flame tests with using flame emission spectroscopy.",
             "points": ["A flame test gives a colour that identifies some metal ions.",
                        "In a mixture of ions, one flame colour can mask another.",
                        "Flame emission spectroscopy gives a line spectrum, with lines for each "
                        "metal ion in the sample, compared with reference spectra.",
                        "It also measures the concentration of each metal ion; a flame test "
                        "cannot.",
                        "Flame emission spectroscopy is accurate, sensitive and rapid."],
             "reject": ["“A flame test measures how much metal is there.” A flame test "
                        "only identifies the ion.",
                        "“Flame emission spectroscopy can only find one metal ion at a "
                        "time.” The spectrum shows the lines of every metal ion in the "
                        "sample."]},
        ],
    },
}
