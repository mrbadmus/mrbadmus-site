# -*- coding: utf-8 -*-
"""Chemical measurements (uncertainty), in the lean shape. Spec table: ks4-chemical-measurements.md.

LEGACY (batch 11). AQA 8464 5.3.1.4 and 8462 4.3.1.4 (the brief named 5.3.1.3 / 4.3.1.3; those are
the mass-changes statements). The ladder (Ks4Practice, 2·2·2·1) and the practice set stay from the
Design page. The practice set is the page's own hard-coded BANK (`BANK.map((q) => K.item(q))`,
the same five on every route); it does not read the subtopic `quiz` list, so its fixes are
logic_edits below and there is no quiz JSON. The number-line figure (nlFig), the CFIFA examples
and questions, and the Step 1, 2, 3 attempt widget are the page's own. The worked Step widget is
not placed: its heading is template text ("Three titres: ...") and titration is chemistry only.

Builder seam (for the lead): the spec eyebrow is the template literal
"AQA Chemistry 5.3.1.4 · Combined and Triple", the 8464 number on the Triple routes too.
"""

LOGIC_EDITS = [
    # Titration is chemistry only (8462 4.4.2.5); 8464 never says titre, pipette or burette, and
    # this BANK and these rungs are shown on every route.
    # Practice set Q1: "titres" in the stem. NEW ID (stem changed). Options unchanged.
    ("Q('Three titres are 22.40, 22.60 and 22.50 cm³.",
     "Q('Three readings of a volume are 22.40, 22.60 and 22.50 cm³."),
    # Practice set Q4, stem kept: the credited option was visibly the longest (70 characters
    # against 22 to 36). AQA: random errors "can be reduced by making more measurements and
    # reporting a mean value". KEY CHANGE.
    ("'It reduces random error, because unpredictable variations partly cancel'",
     "'It reduces random error'"),
    # Practice set Q5, stem kept: the answer was a pipette and a distractor a burette, both
    # chemistry-only apparatus on a Combined page. Now measuring cylinders, which every route
    # uses: the smallest cylinder that holds 25 cm³ has the closest marks. KEY CHANGE.
    ("'A 25 cm³ pipette', [['A 250 cm³ measuring cylinder', 'Large graduations: large uncertainty "
     "for 25 cm³.'], ['A 250 cm³ beaker', 'Beakers are not for measuring.'], ['A 50 cm³ burette, "
     "read once', 'A burette gives a variable volume from two readings; the pipette is made for "
     "this one volume.']]",
     "'A 25 cm³ measuring cylinder', [['A 250 cm³ measuring cylinder', 'Its marks are much further "
     "apart, so the uncertainty for 25 cm³ is larger.'], ['A 250 cm³ beaker', 'Beakers are not "
     "for measuring volumes.'], ['A 100 cm³ measuring cylinder', 'Its marks are further apart "
     "than on a 25 cm³ cylinder, so the uncertainty is larger.']]"),
    # Rung 2 calc 1: "titres" in the prompt. Position kept (id kept).
    ("CALC('Three titres are 19.80, 20.00 and 19.90 cm³.",
     "CALC('Three volumes are 19.80, 20.00 and 19.90 cm³."),
    # Rung 3 chain 2: a pipette for a titration, chemistry-only on every route. Rewritten on
    # measuring cylinders, with one forced order (each link starts "So" from the one before).
    # Position kept (id kept).
    ("CHAIN('Explain', 'Explain why a pipette is used rather than a measuring cylinder to measure "
     "25.0 cm³ of alkali for a titration. Put the links in order.',\n            ['A pipette is "
     "made to deliver one fixed volume, 25.0 cm³.', 'Its uncertainty for that volume is much "
     "smaller than a cylinder’s, whose graduations are far apart.', 'A smaller uncertainty in the "
     "volume gives a more accurate result.'],\n            [['A pipette holds more liquid.', 'It "
     "holds one fixed volume.'], ['A cylinder cannot be read.', 'It can, from the bottom of the "
     "meniscus, but with a larger uncertainty.']])",
     "CHAIN('Explain', 'Explain why a student uses a 10 cm³ measuring cylinder rather than a "
     "100 cm³ measuring cylinder to measure 8.0 cm³ of acid. Put the links in order.',\n"
     "            ['The 10 cm³ cylinder has its scale marks much closer together.', 'So the "
     "volume can be read to a smaller fraction of a cm³.', 'So the uncertainty in the 8.0 cm³ "
     "is smaller.'],\n            [['The 10 cm³ cylinder holds more liquid.', 'It holds less. "
     "Its marks are closer together.'], ['A bigger cylinder always gives a smaller uncertainty.', "
     "'A bigger cylinder has its marks further apart, so its uncertainty is bigger.']])"),
    # CFIFA question 2 (cfifa slot): "titres". Its id ('cm-q2') is explicit, so it survives.
    ("head: 'A set of titres has a mean of 23.45 cm³",
     "head: 'A set of volume readings has a mean of 23.45 cm³"),
    # nlFig's alt text (read aloud by screen readers) said "titres".
    ("'Three titres 24.10, 24.30 and 24.20 on a number line;",
     "'Three readings 24.10, 24.30 and 24.20 cm³ on a number line;"),
    # Blind fix (c): rung 3 chain 1, link 1 starts 'So' so link 0 must come first. Prompt unchanged (id kept).
    ("'It is anomalous: most likely caused by a mistake or a one-off random error.'",
     "'So it is anomalous: most likely caused by a mistake or a one-off random error.'"),
]

LESSON = {
    "slug": "chemical-measurements",
    "start": {
        "setup": "One jug has a mark every 100 mL. The other has a mark every 10 mL. You need "
                 "30 mL of milk.",
        "question": "If you had to guess, which jug gets you closer to 30 mL?",
        "options": [
            ("The jug marked every 100 mL",
             "The jug marked every 10 mL. The closer the marks, the smaller the uncertainty in "
             "your reading."),
            ("The jug marked every 10 mL",
             "The jug marked every 10 mL. The closer the marks, the smaller the uncertainty in "
             "your reading."),
        ],
        "answer": 1,
    },
    "words": ["uncertainty", "mean", "range", "anomalous"],
    "knowledge": [
        {"kind": "card", "title": "There is always uncertainty",
         "body": ["Whenever a measurement is made there is always some uncertainty about the "
                  "result obtained.",
                  "So you repeat a measurement and look at how the results are spread out."]},
        {"kind": "card", "title": "The range about the mean",
         "body": ["Use the range of a set of measurements about the mean as a measure of "
                  "uncertainty.",
                  {"points": [
                      "mean = sum of the readings ÷ number of readings",
                      "range = largest reading − smallest reading",
                      "uncertainty = ± half the range",
                      "Write the result as mean ± uncertainty.",
                  ]}]},
        {"kind": "reveal", "title": "Readings of 24.10, 24.30 and 24.20 cm³",
         "cols": ["Working", "Answer"],
         "rows": [
             ("Mean", "(24.10 + 24.30 + 24.20) ÷ 3", "24.20 cm³"),
             ("Range", "24.30 − 24.10", "0.20 cm³"),
             ("Uncertainty", "0.20 ÷ 2", "± 0.10 cm³"),
             ("Result", "mean ± uncertainty", "24.20 ± 0.10 cm³"),
         ]},
        {"kind": "card", "title": "Showing the spread",
         "body": ["Plot the readings on a number line to show how they are spread. The mean sits "
                  "in the middle, and the uncertainty reaches half the range on each side.",
                  {"slot": "fig:measurement-number-line"}]},
        {"kind": "card", "title": "Worked examples",
         "body": ["Convert first if the readings are in different units: 1 dm³ = 1000 cm³.",
                  {"slot": "cfifa"}]},
        {"kind": "card", "title": "Anomalous results",
         "body": ["A result that is far from the others is anomalous.",
                  "Look for its cause. If it came from a poor measurement, leave it out of the "
                  "mean and the range.",
                  {"slot": "steps-attempt"}]},
        {"kind": "reveal", "title": "Four words, used exactly",
         "cols": ["Meaning"],
         "rows": [
             ("Accurate", "An accurate measurement is one that is close to the true value."),
             ("Precise", "Measurements are precise if they cluster closely."),
             ("Repeatable", "Repetition, under the same conditions by the same investigator, "
              "gives similar results."),
             ("Reproducible", "Similar results are obtained by different investigators with "
              "different equipment."),
         ]},
        {"kind": "card", "title": "Random and systematic error",
         "body": [{"points": [
             "<strong>Random error</strong>: results vary in unpredictable ways. Making more "
             "measurements and reporting a mean value reduces it.",
             "<strong>Systematic error</strong>: every result differs from the true value by the "
             "same amount, such as a balance that was not zeroed. Repeating does not remove it.",
         ]}]},
        {"kind": "card", "title": "Reading a measuring cylinder",
         "body": ["Choose a cylinder close in size to the volume you need. Its marks are closer "
                  "together, so the uncertainty is smaller.",
                  "Read the bottom of the curved surface of the liquid (the meniscus), with your "
                  "eye level with it."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Readings 12.4, 12.8 and 12.6: the uncertainty is ± 0.4.",
              "0.4 is the whole range. The uncertainty is half of it: 12.6 ± 0.2."),
             ("Every reading goes into the mean, even one far from the rest.",
              "Leave an anomalous result out of the mean and the range."),
             ("Repeating the measurement removes systematic error.",
              "Repeats reduce random error. A systematic error is in every reading."),
         ]}]},
    ],
    "key_fact": "Whenever a measurement is made there is always some uncertainty about the result "
                "obtained. Use the range of a set of measurements about the mean as a measure of "
                "uncertainty: leave out anomalies and give the result as the mean ± half the "
                "range.",
    "deeper": [
        {"kind": "card", "title": "Burettes and pipettes", "routes": ["TF", "TH"],
         "body": ["In a titration you use a pipette to measure one fixed volume, such as "
                  "25.0 cm³, and a burette to add a volume you do not know in advance.",
                  "A burette's scale runs downwards. The volume added is the final reading minus "
                  "the first reading.",
                  {"slot": "fig:volume-apparatus"}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: the mean, leaving out anomalies, or the uncertainty as "
             "half the range.",
             "<strong>Explain</strong>: why repeats reduce random error, or why a result is "
             "anomalous.",
             "<strong>Suggest</strong>: apparatus that gives a smaller uncertainty.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-11", "logic_edits": LOGIC_EDITS},
}
