# -*- coding: utf-8 -*-
"""The gas exchange system, in the lean shape. Spec table: docs/lessons/pilot/ks3-the-gas-exchange-system.md."""

LESSON = {
    "slug": "the-gas-exchange-system",
    "start": {
        "setup": None,
        "question": "If you had to guess, how much of the oxygen in a breath is still there when you breathe it out?",
        "options": [
            ("Most of it", "Most of it. Air you breathe out is still about 16% oxygen."),
            ("Hardly any of it", "Most of it. Air you breathe out is still about 16% oxygen."),
        ],
        "answer": 0,
    },
    "words": ["trachea", "bronchioles", "alveoli", "gas exchange"],
    "knowledge": [
        {"kind": "card", "title": "The gas exchange system",
         "body": ["Air travels down a branching set of tubes to the alveoli.",
                  {"figure": "b4-gas-exchange-labelled"}]},
        {"kind": "reveal", "title": "The parts and what they do",
         "cols": ["What it is", "What it does"],
         "rows": [
             ("Nose and mouth", "Where air enters", "Warm, moisten and filter the air"),
             ("Trachea", "A tube held open by rings of cartilage", "Carries air towards the lungs"),
             ("Bronchi", "Two tubes, one to each lung", "Carry air into the lungs"),
             ("Bronchioles", "Narrower tubes that keep dividing", "Carry air to the alveoli"),
             ("Alveoli", "About 500 million tiny air sacs", "Where gas exchange happens"),
             ("Ribs", "Bones around the lungs", "Protect the lungs and move during breathing"),
             ("Diaphragm and intercostals", "Muscles", "Change the volume of the chest"),
         ]},
        {"kind": "card", "title": "Keeping the airways clean",
         "body": ["Mucus in the airways traps dust and bacteria.",
                  "Cilia are tiny hairs on the cells of the airway.",
                  "They sweep the mucus up and out of the lungs."]},
        {"kind": "reveal", "title": "Three words to keep apart",
         "cols": ["What it is", "Where it happens"],
         "rows": [
             ("Breathing", "Air moving in and out of the lungs", "The chest and lungs"),
             ("Gas exchange", "Oxygen moves into the blood and carbon dioxide moves out",
              "The alveoli"),
             ("Respiration", "A chemical reaction that releases energy from glucose",
              "Every living cell"),
         ]},
        {"kind": "reveal", "title": "Air in and air out",
         "cols": ["Air breathed in", "Air breathed out"],
         "rows": [
             ("Nitrogen", "78%", "78%"),
             ("Oxygen", "21%", "16%"),
             ("Carbon dioxide", "0.04%", "4%"),
             ("Water vapour", "Varies", "Much more"),
             ("Temperature", "Cooler", "Warmer"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("We breathe in oxygen and breathe out carbon dioxide.",
              "Air in and air out are both mostly nitrogen. Air out has less oxygen and more "
              "carbon dioxide."),
             ("Breathing and respiration are the same thing.",
              "Breathing moves air. Respiration is a chemical reaction in cells."),
         ]}]},
    ],
    "key_fact": "Air travels down the trachea, bronchi and bronchioles to the alveoli. In the "
                "alveoli, oxygen moves into the blood and carbon dioxide moves out.",
    "deeper": [
        {"kind": "card", "title": "Why mouth-to-mouth works",
         "body": ["Air you breathe out is still about 16% oxygen.",
                  "That is enough oxygen to keep another person alive."]},
        {"kind": "card", "title": "Why the trachea has rings",
         "body": ["Rings of cartilage hold the trachea open.",
                  "They stop it closing when the pressure inside falls."]},
        {"kind": "card", "title": "How many branches",
         "body": ["The airways divide about 23 times between the trachea and the alveoli."]},
    ],
    "try": None,
    # render-only overlays (ks3_data/lean/__init__.py, build_ks3.py): nothing here reaches the question mirror
    "convention_note": "These are typical values for a person at rest.",
    "figure_caption": {"b4-gas-exchange-labelled":
                       "Air travels from 01 to 05. Gas exchange happens only in the air sacs."},
    "ladder_stem": {
        "explain": "A student writes: \u201cWe breathe in oxygen and breathe out carbon dioxide.\u201d Explain "
                   "what is wrong with this statement about the air. Then write a correct version. "
                   "Use figures.",
    },
    "ladder_ticks": [
        ["Gives the inhaled figures \u2014 about 21% oxygen and 0.04% carbon dioxide.",
         "Gives the inhaled figures: about 21% oxygen and 0.04% carbon dioxide."],
        ["Gives the exhaled figures \u2014 about 16% oxygen and 4% carbon dioxide.",
         "Gives the exhaled figures: about 16% oxygen and 4% carbon dioxide."],
        ["Correctly assigns the raised rate to breathing, driven by the products of respiration \u2014 not to gas exchange failing.",
         "Correctly says the raised rate is a change in breathing, driven by the products of respiration. Gas exchange has not failed."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Plants have no muscles to move air, so they do not breathe.",
            2: "Gases do move through the leaf. But respiration in the cells makes the carbon dioxide.",
            3: "A plant never breathes. Breathing needs muscles and an airway.",
        },
        "apply": {
            1: "Only about 4%. It goes up, but it is still a small share.",
            2: "Oxygen comes second, at about 16%.",
            3: "Air out has more water vapour, but it is only a few per cent.",
        },
    },
}
