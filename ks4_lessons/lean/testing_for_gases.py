# -*- coding: utf-8 -*-
"""Testing for gases, in the lean shape. New record, no legacy page (it replaces the old
generate_site_v5 page). Spec table: ks4-testing-for-gases.md (AQA 8464 5.8.2.1 to 5.8.2.4 / 8462
4.8.2.1 to 4.8.2.4, word for word the same; no HT-only or chemistry-only lines). Every route gets the
same lesson. The four tests and results are AQA's own words.

The practice set reads the route's `quiz` list (K.bank): quiz-testing-for-gases.json, five per
route, both old stems kept. Figure wanted: fig:limewater-test (BRIEF-AN.md)."""

LESSON = {
    "slug": "testing-for-gases",
    "start": {
        "setup": "A glowing splint is pushed into a test tube of gas. It bursts back into flame.",
        "question": "If you had to guess, which gas is in the tube?",
        "options": [
            ("Oxygen",
             "Oxygen. A glowing splint relights in oxygen. Hydrogen is tested with a burning "
             "splint, and it burns with a pop."),
            ("Hydrogen",
             "Oxygen. A glowing splint relights in oxygen. Hydrogen is tested with a burning "
             "splint, and it burns with a pop."),
        ],
        "answer": 0,
    },
    "words": ["burning splint", "glowing splint", "limewater", "damp litmus paper"],
    "knowledge": [
        {"kind": "reveal", "title": "The four gas tests",
         "cols": ["Test", "Result"],
         "rows": [
             ("Hydrogen", "A burning splint held at the open end of a test tube of the gas",
              "The hydrogen burns rapidly with a pop sound"),
             ("Oxygen", "A glowing splint put into a test tube of the gas",
              "The splint relights"),
             ("Carbon dioxide", "Shake the gas with limewater, or bubble it through limewater",
              "The limewater turns milky (cloudy)"),
             ("Chlorine", "Put damp litmus paper into the gas",
              "The litmus paper is bleached and turns white"),
         ]},
        {"kind": "card", "title": "Hydrogen",
         "body": ["The test for hydrogen uses a burning splint held at the open end of a test tube "
                  "of the gas.",
                  "Hydrogen burns rapidly with a pop sound, often called a squeaky pop."]},
        {"kind": "card", "title": "Oxygen",
         "body": ["The test for oxygen uses a glowing splint inserted into a test tube of the gas.",
                  "A glowing splint has been lit and blown out, so it is still red but has no "
                  "flame. The splint relights in oxygen."]},
        {"kind": "card", "title": "Carbon dioxide",
         "body": ["The test for carbon dioxide uses an aqueous solution of calcium hydroxide, "
                  "called limewater.",
                  "When carbon dioxide is shaken with or bubbled through limewater, the limewater "
                  "turns milky (cloudy).",
                  {"slot": "fig:limewater-test"}]},
        {"kind": "card", "title": "Chlorine",
         "body": ["The test for chlorine uses litmus paper.",
                  "When damp litmus paper is put into chlorine gas, the litmus paper is bleached "
                  "and turns white.",
                  "Chlorine is toxic. Do this test in a fume cupboard."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A glowing splint pops in hydrogen.",
              "Hydrogen: a burning splint, and it burns with a pop. Oxygen: a glowing splint, and "
              "it relights."),
             ("Carbon dioxide turns limewater clear.",
              "Limewater starts clear. Carbon dioxide turns it milky (cloudy)."),
             ("Chlorine turns litmus paper blue.",
              "Chlorine bleaches damp litmus paper and turns it white."),
             ("A gas that puts out a burning splint is carbon dioxide.",
              "Other gases put out a flame too. The test for carbon dioxide is limewater."),
         ]}]},
    ],
    "key_fact": "Hydrogen burns rapidly with a pop when a burning splint is held at the open end of "
                "the test tube. Oxygen relights a glowing splint. Carbon dioxide turns limewater "
                "milky (cloudy). Chlorine bleaches damp litmus paper and turns it white.",
    "deeper": [
        {"kind": "card", "title": "Why limewater turns milky",
         "body": ["Carbon dioxide reacts with the calcium hydroxide in limewater. It makes calcium "
                  "carbonate, which is insoluble, so it forms tiny white solid particles.",
                  "Ca(OH)₂ + CO₂ → CaCO₃ + H₂O"]},
        {"kind": "card", "title": "Where these gases come from",
         "body": [{"points": [
             "Hydrogen: a metal such as magnesium or zinc reacting with a dilute acid.",
             "Carbon dioxide: a carbonate reacting with a dilute acid.",
             "Chlorine: the positive electrode when sodium chloride solution is electrolysed.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong> a test: say what you do and the result you would see.",
             "<strong>Identify</strong>: name the gas from the result.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Describe", "marks": 1,
             "prompt": "Describe the result of the test for oxygen.",
             "why": "The test for oxygen uses a glowing splint. The splint relights in oxygen.",
             "options": [
                 {"text": "A burning splint gives a pop", "correct": False,
                  "reply": "That is the result for hydrogen."},
                 {"text": "A glowing splint relights", "correct": True},
                 {"text": "Limewater turns milky", "correct": False,
                  "reply": "That is the result for carbon dioxide."},
             ]},
            {"kind": "mcq", "command": "Name", "marks": 1,
             "prompt": "Name the solution used to test for carbon dioxide.",
             "why": "Limewater, an aqueous solution of calcium hydroxide.",
             "options": [
                 {"text": "Silver nitrate solution", "correct": False,
                  "reply": "Silver nitrate tests for halide ions."},
                 {"text": "Sodium hydroxide solution", "correct": False,
                  "reply": "Sodium hydroxide tests for some metal ions."},
                 {"text": "Limewater", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Identify", "marks": 2,
             "prompt": "A gas has no effect on damp litmus paper or on limewater. A glowing splint "
                       "put into the gas relights. Identify the gas.",
             "why": "A glowing splint relights in oxygen.",
             "options": [
                 {"text": "Oxygen", "correct": True},
                 {"text": "Chlorine", "correct": False,
                  "reply": "Chlorine would bleach the damp litmus paper."},
                 {"text": "Carbon dioxide", "correct": False,
                  "reply": "Carbon dioxide would turn the limewater milky."},
             ]},
            {"kind": "mcq", "command": "Describe", "marks": 2,
             "prompt": "Zinc reacts with dilute hydrochloric acid and gives off a gas. Describe how "
                       "to show that the gas is hydrogen.",
             "why": "Hold a burning splint at the open end of the tube. Hydrogen burns rapidly with "
                    "a pop.",
             "options": [
                 {"text": "Put a glowing splint into the tube: the splint relights",
                  "correct": False,
                  "reply": "That is the test for oxygen."},
                 {"text": "Hold a burning splint at the mouth of the tube: it pops",
                  "correct": True},
                 {"text": "Bubble the gas through limewater: the limewater turns milky",
                  "correct": False,
                  "reply": "That is the test for carbon dioxide."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Hydrogen peroxide breaks down to give a gas. Describe how to show that the "
                       "gas is oxygen. Put the links in order.",
             "links": ["Light a splint, then blow it out so that it is only glowing.",
                       "Put the glowing splint into the test tube of gas.",
                       "The splint relights, so the gas is oxygen."],
             "herrings": [{"text": "Hold a burning splint at the open end: a pop shows oxygen.",
                           "why": "A pop with a burning splint shows hydrogen."},
                          {"text": "The splint goes out, so the gas is oxygen.",
                           "why": "Oxygen relights a glowing splint."}]},
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "Describe how to show that a gas given off by a reaction is carbon dioxide. "
                       "Put the links in order.",
             "links": ["Collect the gas, or pass it through a delivery tube.",
                       "Bubble the gas through limewater, or shake it with limewater.",
                       "The limewater turns milky (cloudy), so the gas is carbon dioxide."],
             "herrings": [{"text": "Hold a burning splint in the gas: a pop shows carbon dioxide.",
                           "why": "A pop shows hydrogen."},
                          {"text": "Put damp litmus paper in the gas: it turns white with carbon "
                                   "dioxide.",
                           "why": "Damp litmus paper is bleached by chlorine."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Four test tubes each hold a different gas: hydrogen, oxygen, carbon dioxide "
                       "and chlorine. Describe a test to identify each gas, and give the result for "
                       "each.",
             "points": ["Hydrogen: a burning splint at the open end of the tube; the gas burns "
                        "with a pop.",
                        "Oxygen: a glowing splint put into the tube; the splint relights.",
                        "Carbon dioxide: bubble through or shake with limewater; the limewater "
                        "turns milky (cloudy).",
                        "Chlorine: damp litmus paper; the paper is bleached and turns white."],
             "reject": ["“Oxygen: a burning splint gives a pop.” The pop is hydrogen; "
                        "oxygen relights a glowing splint.",
                        "“Chlorine: limewater turns milky.” Chlorine bleaches damp "
                        "litmus paper."]},
        ],
    },
}
