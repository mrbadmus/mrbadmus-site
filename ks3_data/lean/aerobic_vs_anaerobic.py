# -*- coding: utf-8 -*-
"""Aerobic vs anaerobic, in the lean shape. Spec table: docs/lessons/wave1/ks3-aerobic-vs-anaerobic.md."""

LESSON = {
    "slug": "aerobic-vs-anaerobic",
    "start": {
        "setup": "Cells can release energy from glucose with oxygen, or without it.",
        "question": "If you had to guess, which way releases energy faster?",
        "options": [
            ("The one using oxygen", "The one without oxygen. It releases energy faster, but much less of it."),
            ("The one without oxygen", "The one without oxygen. It releases energy faster, but much less of it."),
        ],
        "answer": 1,
    },
    "words": ["aerobic respiration", "anaerobic respiration", "mitochondria", "cytoplasm"],
    "word_defs": {
        "aerobic respiration": "Respiration that uses oxygen. It releases energy from glucose.",
        "anaerobic respiration": "Respiration without oxygen. It releases much less energy from each glucose.",
        "mitochondria": "Tiny parts of a cell where aerobic respiration happens.",
        "cytoplasm": "The jelly inside a cell, where many reactions happen.",
    },
    "knowledge": [
        {"kind": "reveal", "title": "Aerobic and anaerobic side by side",
         "cols": ["Aerobic", "Anaerobic"],
         "rows": [
             ("Reactants", "Glucose and oxygen", "Glucose only"),
             ("Glucose", "Broken down completely", "Broken down only partly"),
             ("Products", "Carbon dioxide and water",
              "Lactic acid in humans. Ethanol and carbon dioxide in yeast and plants."),
             ("Energy from each glucose", "Much more", "Much less"),
             ("How fast energy is released", "Slower", "Faster"),
             ("Where in the cell", "In the mito­chondria", "In the cytoplasm"),
         ]},
        {"kind": "card", "title": "What they have in common",
         "body": ["Both are respiration.",
                  "Both break down glucose.",
                  "Both release energy that the cell can use.",
                  "Both are chemical reactions controlled by enzymes."]},
        {"kind": "card", "title": "Sprint or marathon",
         "body": ["Most of the time, your cells respire aerobically.",
                  "In a sprint, anaerobic respiration releases extra energy quickly. Lactic acid builds up.",
                  "For ten seconds, that is fine.",
                  "A marathon runner paces the race, so the oxygen supply keeps up.",
                  "They stay mostly aerobic, so lactic acid does not build up.",
                  "Aerobic respiration gets much more energy from each glucose, which suits a long race."]},
        {"kind": "card", "title": "Life without oxygen",
         "body": ["Some bacteria are killed by oxygen. They live in places with none, such as mud.",
                  "They respire only anaerobically, so they get little energy from each glucose.",
                  "So they need more food for the same work, or they are less active.",
                  "Early Earth had almost no oxygen in the air.",
                  "So anaerobic respiration is probably the older process.",
                  "The oxygen in the air was added later, by photosynthesis."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Anaerobic respiration releases more energy.",
              "It releases energy faster, but much less from each glucose."),
             ("In humans, both kinds make carbon dioxide.",
              "Anaerobic respiration in humans makes lactic acid only."),
             ("Anaerobic respiration only happens when something goes wrong.",
              "Yeast uses it whenever oxygen is short. Some bacteria use it all the time."),
         ]}]},
    ],
    "key_fact": "Aerobic respiration uses oxygen and breaks glucose down completely. It releases much "
                "more energy from each glucose. Anaerobic respiration needs no oxygen. It releases much "
                "less energy, but it releases it faster. Aerobic makes carbon dioxide and water. Anaerobic "
                "makes lactic acid, or ethanol and carbon dioxide.",
    "deeper": [
        {"kind": "card", "title": "Why anaerobic is faster",
         "body": ["Anaerobic respiration has fewer steps.",
                  "It does not have to wait for oxygen to arrive from the blood.",
                  "So it can release energy quickly, for a short time."]},
        {"kind": "card", "title": "Cells with no mitochondria",
         "body": ["Anaerobic respiration happens outside the mitochondria.",
                  "So red blood cells, which have none, still release energy this way."]},
    ],
    "try": None,
    "tutor_body": "Want to check which kind of respiration is running?",
    "ladder_stem": {
        "explain": "A sprinter and a marathon runner both respire aerobically and anaerobically. Explain "
                   "why their races depend on these so differently. Explain why the marathon runner "
                   "paces the race.",
        "produce": "Some bacteria are killed by oxygen. They live only where there is none, such as in mud. "
                   "Explain how they can live without oxygen. Say what they give up. Say what they suggest "
                   "about which kind of respiration came first on Earth.",
    },
    "ladder_ticks": [
        ["Says the sprinter needs energy far faster than oxygen can be delivered, so a large part comes "
         "anaerobically.",
         "Says the sprinter needs energy faster than oxygen arrives, so much comes anaerobically."],
        ["Says this produces lactic acid, which builds up and forces them to slow down — tolerable over "
         "ten seconds.",
         "Says this makes lactic acid, which is fine for a ten-second race."],
        ["Says the marathon runner cannot do this, because lactic acid would accumulate long before the finish.",
         "Says the marathon runner cannot do this, as lactic acid would build up too soon."],
        ["Says aerobic respiration gets about twenty times more energy from each glucose, so it is the only "
         "affordable route over two hours.",
         "Says aerobic respiration gets much more energy from each glucose, so suits long races."],
        ["Concludes that pacing means holding a speed at which the oxygen supply still covers the demand.",
         "Says pacing keeps the speed low enough for the oxygen supply to keep up."],
        ["Says they must therefore use much more food for the same amount of work, or live at a low rate of "
         "activity.",
         "Says they need much more food for the same work, or must be less active."],
        ["Says anaerobic respiration must be the older process, because for a long period early in Earth’s "
         "history there was almost no oxygen in the atmosphere.",
         "Says anaerobic respiration is probably older. Early Earth had almost no oxygen in the air."],
        ["Links the appearance of oxygen to photosynthesis — the oxygen these organisms avoid was put there "
         "by other living things.",
         "Says the oxygen in the air was added later, by photosynthesis."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Both kinds release energy from glucose. That is not a difference.",
            1: "Anaerobic respiration happens in the cytoplasm, not the mitochondria.",
            3: "In humans, anaerobic respiration makes lactic acid, not carbon dioxide.",
        },
        "apply": {
            0: "That is the wrong way round. Anaerobic is faster, but gets less.",
            1: "Anaerobic respiration releases much less energy from each glucose.",
            2: "Aerobic respiration releases much more energy from each glucose.",
        },
    },
}
