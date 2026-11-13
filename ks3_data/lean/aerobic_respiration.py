# -*- coding: utf-8 -*-
"""Aerobic respiration, in the lean shape. Spec table: docs/lessons/wave1/ks3-aerobic-respiration.md."""

LESSON = {
    "slug": "aerobic-respiration",
    "start": {
        "setup": "A person loses 10 kg of fat over a year.",
        "question": "If you had to guess, how does most of that fat leave the body?",
        "options": [
            ("Out through the lungs", "Out through the lungs. Most of it leaves as carbon dioxide in your breath."),
            ("In sweat and urine", "Out through the lungs. Most of it leaves as carbon dioxide in your breath."),
        ],
        "answer": 0,
    },
    "words": ["aerobic respiration", "mitochondria", "glucose", "breathing"],
    "word_defs": {
        "aerobic respiration": "Respiration that uses oxygen. It releases energy from glucose.",
        "mitochondria": "Tiny parts of a cell where aerobic respiration happens.",
        "glucose": "A sugar. It is the fuel cells use in respiration.",
        "breathing": "Moving air in and out of the lungs. It is not respiration.",
    },
    "knowledge": [
        {"kind": "card", "title": "The word summary",
         "body": [{"figure": "b8-word-aerobic"},
                  "Glucose and oxygen are the reactants.",
                  "Carbon dioxide and water are the products.",
                  "The reaction releases energy. Energy is not a substance, so it is not a product."]},
        {"kind": "card", "title": "Why organisms respire",
         "body": ["Every living cell needs energy, all the time.",
                  "Respiration releases the energy stored in glucose.",
                  "Cells use this energy for:",
                  {"points": ["moving, such as muscles contracting",
                              "keeping warm",
                              "building larger molecules for growth and repair",
                              "taking in substances by active transport"]},
                  "Respiration never stops. A cell that stops respiring soon dies."]},
        {"kind": "card", "title": "Where it happens",
         "body": ["Aerobic respiration happens in the mitochondria.",
                  "Almost every cell has mitochondria, in plants and in animals.",
                  "Cells that need a lot of energy, like muscle cells, have many."]},
        {"kind": "reveal", "title": "Breathing and respiration",
         "cols": ["Breathing", "Aerobic respiration"],
         "rows": [
             ("What it is", "Moving air in and out of the lungs",
              "A chemical reaction that releases energy from glucose"),
             ("Where it happens", "In the lungs", "In the mitochondria of cells"),
             ("What does it", "The diaphragm and intercostal muscles", "Almost every living cell"),
             ("Which organisms", "Animals with lungs", "All living organisms"),
         ]},
        {"kind": "card", "title": "During exercise",
         "body": ["Working muscles need more energy, so they respire faster.",
                  "They use more glucose and oxygen, and make more carbon dioxide.",
                  "You breathe faster and deeper to take in oxygen and remove carbon dioxide.",
                  "Your heart beats faster to carry blood to the muscles faster."]},
        {"kind": "card", "title": "Where the mass goes",
         "body": ["Atoms are not made or destroyed in a reaction.",
                  "25 g of glucose reacts with 26.7 g of oxygen.",
                  "This makes 36.7 g of carbon dioxide and 15.0 g of water.",
                  "So 51.7 g goes in and 51.7 g comes out.",
                  "When you lose fat, most of its mass is breathed out as carbon dioxide."]},
        {"kind": "card", "title": "Germinating seeds respire",
         "body": ["Germinating seeds respire fast, to release energy for growth.",
                  "In a sealed flask, they warm up, because respiration releases some energy as heat.",
                  "They use up oxygen and give out carbon dioxide.",
                  "Boiled seeds are dead. Nothing changes in their flask."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Respiration means breathing.",
              "Respiration is a reaction in cells. Breathing brings in the oxygen it uses."),
             ("Respiration makes energy.",
              "Energy cannot be made. Respiration releases energy stored in glucose."),
             ("Fat turns into energy and disappears.",
              "Its atoms leave the body, mostly as carbon dioxide you breathe out."),
             ("Plants do not respire.",
              "Plants respire all the time, just like animals."),
         ]}]},
    ],
    "key_fact": "Aerobic respiration is a reaction in the mitochondria of cells. Glucose and oxygen "
                "react to make carbon dioxide and water. This releases the energy cells need to stay alive.",
    "deeper": [
        {"kind": "card", "title": "Respiration is not burning",
         "body": ["Burning glucose releases its energy all at once, as heat and light.",
                  "Respiration releases it in many small steps, at body temperature.",
                  "Enzymes control each step."]},
        {"kind": "card", "title": "Cells with no mitochondria",
         "body": ["Red blood cells have no mitochondria.",
                  "They carry oxygen, but cannot use it for aerobic respiration."]},
    ],
    "try": None,
    "ks4_becomes": "The balanced symbol equation, and how respiration links to metabolism.",
    "figure_caption": {"b8-word-aerobic": None},      # the card text already says it
    "ladder_stem": {
        "produce": "Germinating peas are sealed in a flask with a thermometer. A second flask holds peas "
                   "that were boiled, cooled and disinfected. Both are left overnight. Predict what happens to the "
                   "temperature, oxygen and carbon dioxide in each flask. Explain why the boiled peas "
                   "are there.",
    },
    "ladder_ticks": [
        ["Says faster respiration uses up glucose and oxygen more quickly and makes carbon dioxide more quickly.",
         "Says faster respiration uses glucose and oxygen faster, and makes carbon dioxide faster."],
        ["Says breathing faster and deeper gets more oxygen into the blood and removes carbon dioxide from it.",
         "Says faster, deeper breathing gets more oxygen into the blood and removes carbon dioxide."],
        ["Makes clear that breathing and respiration are two different things — breathing supplies the "
         "reaction, it is not the reaction.",
         "Makes clear that breathing is not respiration. Breathing supplies the oxygen for it."],
        ["Predicts the living peas warm up, because respiration transfers energy and not all of it does useful work.",
         "Predicts the living peas warm up. Respiration releases energy, and some heats the flask."],
        ["Predicts no change of any kind in the boiled flask, because those peas are dead and are not respiring.",
         "Predicts no change in the boiled flask. Those peas are dead, so they do not respire."],
        ["Says the boiled peas are the control — they rule out warming or gas changes caused by anything "
         "other than living cells.",
         "Says the boiled peas are the control. Any change must come from living cells."],
    ],
    "figures": [
        {"id": "b8-word-aerobic", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The word summary for aerobic respiration",
         "desc": "Glucose plus oxygen at the top, labelled reactants. A drawn arrow points down to "
                 "carbon dioxide plus water, labelled products.",
         "caption": "The word summary for aerobic respiration.",
         "eq": {"left": ["glucose", "oxygen"], "right": ["carbon dioxide", "water"]}},
    ],
    "ladder_feedback": {
        "recall": {
            1: "That is photosynthesis. Respiration goes the other way.",
            2: "Glucose is missing, and so is water.",
            3: "Energy is not a substance. The products are carbon dioxide and water.",
        },
        "apply": {
            0: "Mass cannot become energy in a reaction. The atoms leave the body.",
            2: "Some water leaves this way. Most of the mass is breathed out as carbon dioxide.",
            3: "The mass leaves the body. Most of it is breathed out.",
        },
    },
}
