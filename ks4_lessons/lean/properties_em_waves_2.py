# -*- coding: utf-8 -*-
"""Properties of electromagnetic waves 2, in the lean shape. New record, no legacy page.
Spec table: ks4-properties-em-waves-2.md (AQA 8464 6.6.2.3 / 8463 4.6.2.3, word for word the
same).

The two (HT only) radio wave statements are on CH TH only: the old built page showed them on
Foundation. The spec says pupils will not be required to recall the unit of radiation dose, so no
rung or quiz question asks for it; every dose question gives 1000 mSv = 1 Sv."""

LESSON = {
    "slug": "properties-em-waves-2",
    "start": {
        "setup": None,
        "question": "If you had to guess, which is more harmful to your skin: ultraviolet or "
                    "visible light?",
        "options": [
            ("Ultraviolet",
             "Ultraviolet. It can make skin age prematurely and increases the risk of skin "
             "cancer."),
            ("Visible light",
             "Ultraviolet. It can make skin age prematurely and increases the risk of skin "
             "cancer."),
        ],
        "answer": 0,
    },
    "words": ["ionising radiation", "mutation", "radiation dose", "sievert"],
    "knowledge": [
        {"kind": "card", "title": "Where electromagnetic waves come from",
         "body": ["Changes in atoms and the nuclei of atoms can result in electromagnetic waves "
                  "being generated or absorbed over a wide frequency range.",
                  "Gamma rays originate from changes in the nucleus of an atom."]},
        {"kind": "card", "title": "Radio waves and electrical circuits", "routes": ["CH", "TH"],
         "body": ["Radio waves can be produced by oscillations in electrical circuits.",
                  "When radio waves are absorbed they may create an alternating current with the "
                  "same frequency as the radio wave itself. So radio waves can themselves induce "
                  "oscillations in an electrical circuit.",
                  {"points": [
                      "<strong>Transmitter</strong>: an alternating current in the aerial makes "
                      "radio waves of the same frequency.",
                      "<strong>Receiver</strong>: the radio waves induce an alternating current "
                      "in the aerial, at the same frequency.",
                  ]}]},
        {"kind": "card", "title": "Hazards to the body",
         "body": ["Ultraviolet waves, X-rays and gamma rays can have hazardous effects on human "
                  "body tissue.",
                  "The effects depend on the type of radiation and the size of the dose."]},
        {"kind": "reveal", "title": "What each one can do",
         "cols": ["Hazard"],
         "rows": [
             ("Ultraviolet", "Can cause skin to age prematurely and increase the risk of skin "
                             "cancer"),
             ("X-rays", "Ionising radiation that can cause the mutation of genes and cancer"),
             ("Gamma rays", "Ionising radiation that can cause the mutation of genes and cancer"),
         ]},
        {"kind": "card", "title": "Radiation dose",
         "body": ["Radiation dose (in sieverts) is a measure of the risk of harm resulting from "
                  "an exposure of the body to the radiation.",
                  "1000 millisieverts (mSv) = 1 sievert (Sv)",
                  "To change millisieverts into sieverts, divide by 1000. For example, "
                  "2.4 mSv = 2.4 ÷ 1000 = 0.0024 Sv.",
                  "You will be given the unit in a question. You do not need to remember it."]},
        {"kind": "card", "title": "Using dose data",
         "body": ["Questions give you doses and ask what they show. Made-up data for practice:",
                  {"points": ["Scan A: 0.02 mSv", "Scan B: 2 mSv", "Scan C: 0.01 Sv"]},
                  {"points": [
                      "Put every dose in the same unit first: scan C is 0.01 Sv = 10 mSv.",
                      "The bigger the dose, the bigger the risk of harm.",
                      "So scan C carries the biggest risk, and scan A the smallest.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Gamma rays come from the electrons around an atom.",
              "Gamma rays originate from changes in the nucleus of an atom."),
             ("1 Sv = 100 mSv.", "1 Sv = 1000 mSv."),
             ("The harm depends only on the type of radiation.",
              "It depends on the type of radiation and the size of the dose."),
         ]}]},
    ],
    "key_fact": "Ultraviolet waves can cause skin to age prematurely and increase the risk of skin "
                "cancer. X-rays and gamma rays are ionising radiation that can cause the mutation "
                "of genes and cancer. The effects depend on the type of radiation and the size of "
                "the dose, and radiation dose (in sieverts) is a measure of the risk of harm.",
    "deeper": [
        {"kind": "card", "title": "Keeping exposure low",
         "body": [{"points": [
             "Radiographers stand behind a screen, or leave the room, while an X-ray is taken. "
             "They take many X-rays each day.",
             "Sunscreen and clothing reduce the ultraviolet that reaches the skin.",
         ]}]},
        {"kind": "card", "title": "Gamma rays and the nucleus",
         "body": ["Gamma rays come from changes in the nucleus. You meet them again in the topic "
                  "on atomic structure and radioactive decay."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Draw conclusions</strong> from data: put the doses in the same unit, "
             "compare them, then say what they show about the risk.",
             "<strong>Explain</strong> a hazard: say which radiation, what it can do to the body, "
             "and what the effect depends on.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the type of electromagnetic wave that originates from changes in the "
                       "nucleus of an atom.",
             "why": "Gamma rays originate from changes in the nucleus of an atom.",
             "options": [
                 {"text": "Radio waves", "correct": False,
                  "reply": "Gamma rays come from the nucleus."},
                 {"text": "Gamma rays", "correct": True},
                 {"text": "Infrared", "correct": False,
                  "reply": "Gamma rays come from the nucleus."},
                 {"text": "Visible light", "correct": False,
                  "reply": "Gamma rays come from the nucleus."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give one hazardous effect of ultraviolet waves on the body.",
             "why": "Ultraviolet can cause skin to age prematurely and increases the risk of skin "
                    "cancer.",
             "options": [
                 {"text": "It increases the risk of skin cancer", "correct": True},
                 {"text": "It makes skin age more slowly", "correct": False,
                  "reply": "The opposite: it can make skin age prematurely."},
                 {"text": "It heats organs deep inside the body", "correct": False,
                  "reply": "Its hazards are to the skin: premature ageing and skin cancer."},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "A scan gives a patient a radiation dose of 0.8 mSv. 1000 mSv = 1 Sv. "
                       "Calculate the dose in sieverts.",
             "convOptions": ["Nothing to convert", "Convert mSv to Sv: divide by 1000",
                             "Convert mSv to Sv: multiply by 1000"],
             "convAnswer": 1, "answer": 0.0008, "tol": 0.00001, "unit": "Sv",
             "units": ["Sv", "mSv", "Hz", "J"],
             "right": "0.8 ÷ 1000 = 0.0008 Sv.",
             "wrong": "1000 mSv = 1 Sv, so divide by 1000: 0.8 ÷ 1000 = 0.0008 Sv.",
             "model": ["C · 1000 mSv = 1 Sv", "F · dose in Sv = dose in mSv ÷ 1000",
                       "I · dose = 0.8 ÷ 1000", "F · dose = 0.0008", "A · 0.0008 Sv"]},
            {"kind": "mcq", "command": "Compare", "marks": 2,
             "prompt": "Scan A gives a dose of 0.02 mSv. Scan B gives a dose of 2 mSv. Which "
                       "conclusion is correct?",
             "why": "Radiation dose is a measure of the risk of harm, so the bigger dose carries "
                    "the bigger risk.",
             "options": [
                 {"text": "Scan B carries the bigger risk of harm, because its dose is bigger",
                  "correct": True},
                 {"text": "Scan A carries the bigger risk of harm, because its number is smaller",
                  "correct": False,
                  "reply": "Both are in mSv, so compare the numbers: 2 is bigger than 0.02."},
                 {"text": "They carry the same risk, because they are both scans", "correct": False,
                  "reply": "The risk depends on the size of the dose."},
             ]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how X-rays can cause cancer. Put the links in order.",
             "links": ["X-rays pass into the body and some are absorbed by its cells.",
                       "X-rays are ionising radiation, so they can cause the mutation of genes in "
                       "those cells.",
                       "Mutated genes can lead to cancer."],
             "herrings": [{"text": "X-rays heat the cells until they burn.",
                           "why": "The hazard is ionisation: the mutation of genes and cancer."},
                          {"text": "X-rays are harmless because they all pass straight through.",
                           "why": "Some are absorbed, and those can cause mutations."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why people are advised to use sunscreen. Put the links in order.",
             "links": ["Sunlight contains ultraviolet waves.",
                       "Ultraviolet absorbed by the skin can make it age prematurely and "
                       "increases the risk of skin cancer.",
                       "Sunscreen reduces the ultraviolet reaching the skin, so it lowers the "
                       "risk."],
             "herrings": [{"text": "Sunscreen blocks the infrared that causes skin cancer.",
                           "why": "The skin cancer risk comes from ultraviolet."},
                          {"text": "Sunscreen makes the skin reflect X-rays from the Sun.",
                           "why": "The hazard in sunlight here is ultraviolet."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Ultraviolet, X-rays and gamma rays can all harm the body. Describe the "
                       "harm each can do, and what the size of the effect depends on.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "The effects of ultraviolet and of X-rays and "
                  "gamma rays described correctly, with what the effect depends on.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two correct effects.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Ultraviolet can cause skin to age prematurely.",
                        "Ultraviolet increases the risk of skin cancer.",
                        "X-rays and gamma rays are ionising radiation.",
                        "They can cause the mutation of genes and cancer.",
                        "The effects depend on the type of radiation and the size of the dose."],
             "reject": ["“All electromagnetic waves cause cancer.”",
                        "“The effect is the same whatever the dose.”"]},
        ],
    },
}
