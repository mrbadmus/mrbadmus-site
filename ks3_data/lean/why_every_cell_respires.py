# -*- coding: utf-8 -*-
"""Why every cell respires, in the lean shape. Spec table: docs/lessons/wave1/ks3-why-every-cell-respires.md."""

LESSON = {
    "slug": "why-every-cell-respires",
    "start": {
        "setup": "You can live for weeks without food, but only minutes without oxygen.",
        "question": "If you had to guess, how much spare oxygen does the body store?",
        "options": [
            ("A big spare supply", "Only a few minutes' worth. The body stores weeks of fuel as fat."),
            ("Hardly any", "Only a few minutes' worth. The body stores weeks of fuel as fat."),
        ],
        "answer": 1,
    },
    "words": ["respiration", "diffusion", "active transport", "mitochondria"],
    "word_defs": {
        "respiration": "A reaction in every living cell. It releases energy from glucose.",
        "diffusion": "A substance spreading from a high to a low concentration. It needs no energy.",
        "active transport": "Moving a substance from a low to a high concentration. It needs energy.",
        "mitochondria": "Tiny parts of a cell where aerobic respiration happens.",
    },
    "knowledge": [
        {"kind": "card", "title": "Every cell respires",
         "body": ["Every living cell respires, all the time.",
                  "This includes plant cells in the roots, stems and leaves.",
                  "Plants respire in the light and in the dark.",
                  "You respire fastest when you exercise. But respiration never stops, even when you sleep."]},
        {"kind": "reveal", "title": "What the energy is used for",
         "cols": ["What it means", "Example"],
         "rows": [
             ("Movement", "Muscles contracting, or whole cells moving", "A sperm cell swimming"),
             ("Building large molecules", "Joining small molecules into big ones, for growth and repair",
              "A plant joining glucose into starch"),
             ("Active transport", "Moving substances where diffusion cannot",
              "A root hair cell taking in minerals"),
             ("Keeping warm", "Keeping body temperature steady in mammals and birds",
              "Your body staying at about 37 °C"),
         ]},
        {"kind": "card", "title": "Active transport needs energy",
         "body": ["Diffusion moves substances from a high to a low concentration. It needs no energy.",
                  "Active transport moves substances from a low to a high concentration.",
                  "This needs energy from respiration.",
                  "Root hair cells take in minerals from the soil by active transport.",
                  "Water moves into the root without needing energy."]},
        {"kind": "card", "title": "Busy cells have more mitochondria",
         "body": ["Muscle cells, sperm cells and root hair cells all need a lot of energy.",
                  "So they have many mitochondria."]},
        {"kind": "card", "title": "Roots need oxygen too",
         "body": ["Root cells respire, so they need oxygen.",
                  "They get it from air spaces between soil particles.",
                  "In waterlogged soil, water fills these air spaces.",
                  "The roots cannot respire aerobically, so they start to die.",
                  "Dead roots cannot take up water."]},
        {"kind": "card", "title": "No store of oxygen",
         "body": ["The body stores enough fat to last for weeks.",
                  "It stores only a few minutes' worth of oxygen.",
                  "Without oxygen, brain cells start to die within a few minutes."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Plants photosynthesise and animals respire.",
              "Plants do both. Every living cell respires."),
             ("Plants only respire at night.",
              "Plants respire day and night. Photosynthesis only happens in the light."),
             ("You only respire when you exercise.",
              "You respire all the time. Exercise makes it faster."),
         ]}]},
    ],
    "key_fact": "Every living cell respires all the time, in plants and in animals. Respiration releases "
                "the energy for movement, building larger molecules, active transport and keeping warm.",
    "deeper": [
        {"kind": "card", "title": "Hibernation",
         "body": ["In winter, a hibernating dormouse lets its body cool down.",
                  "Its respiration slows right down.",
                  "So its store of fat lasts until spring."]},
        {"kind": "card", "title": "Why a lizard eats less",
         "body": ["A lizard does not use energy from respiration to keep warm.",
                  "It warms itself in the sun instead.",
                  "So it needs far less food than a mammal of the same size."]},
    ],
    "try": None,
    "ladder_stem": {
        "recall": "Which of these processes needs energy released by respiration to make it happen?",
        "apply": "A potted plant has been in a dark cupboard for a day. Which statement about its cells "
                 "is fully correct?",
        "explain": "A root hair cell takes in minerals from the soil. The soil has a lower concentration "
                   "of these minerals than the cell. Explain why this needs respiration. Explain why a "
                   "root hair cell has many mitochondria.",
        "produce": "A houseplant is watered too often. Its leaves go yellow and droop, as if it were short "
                   "of water. Gardeners say the roots have “drowned”. Explain what has happened, "
                   "using respiration.",
    },
    "ladder_ticks": [
        ["Says the mineral ions are more concentrated inside the cell than in the soil water.",
         "Says the minerals must move into the cell from a low to a high concentration."],
        ["Says diffusion moves substances the other way, from high to low, so it cannot do this job.",
         "Says diffusion only moves substances from high to low, so it cannot do this."],
        ["Concludes that the cell holds many mitochondria because active transport is its main and continuous "
         "activity.",
         "Says its many mitochondria release the energy that active transport needs."],
        ["Says without oxygen the root cells cannot respire aerobically, so they have little or no energy "
         "available.",
         "Says without oxygen, root cells cannot respire aerobically, so they have little energy."],
        ["Explains the apparent contradiction: dead or dying roots cannot take up water, so a plant standing in "
         "water shows exactly the symptoms of a plant with none.",
         "Says dying roots cannot take up water, so the plant looks short of water."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Water moves into roots without needing energy.",
            1: "Oxygen diffuses into the blood. Diffusion needs no energy.",
            2: "Carbon dioxide diffuses out of cells. That needs no energy.",
        },
        "apply": {
            0: "The plant is alive, so its cells keep respiring.",
            1: "Plants do not swap. They respire all the time, in light and dark.",
            3: "Every living cell respires, including leaf cells.",
        },
    },
}
