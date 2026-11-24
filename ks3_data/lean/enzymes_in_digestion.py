# -*- coding: utf-8 -*-
"""Enzymes in digestion, in the lean shape. Spec table: docs/lessons/wave2/ks3-enzymes-in-digestion.md.

NC B13 asks for enzymes "simply as biological catalysts". Rainford 16a also asks how enzymes
function, so the page teaches the enzyme's shape fitting one substrate, and what heat and pH do
to it (Rung 2 tests denaturing; Rung 3 tests pH). Two new phone-width figures.
"""

LESSON = {
    "slug": "enzymes-in-digestion",
    "start": {
        "setup": "Mix a teaspoon of amylase with a kilogram of starch. Wait, and the starch is all gone.",
        "question": "If you had to guess, is the amylase still there once the starch has gone?",
        "options": [
            ("Yes, all of it",
             "Yes. An enzyme is a catalyst. It speeds up the reaction without being used up."),
            ("No, it gets used up",
             "All of it is still there. An enzyme is not used up, so it can work again."),
        ],
        "answer": 0,
    },
    "words": ["enzyme", "catalyst", "substrate", "denatured"],
    "word_defs": {
        "enzyme": "A protein, made by living cells, that speeds up a reaction.",
        "catalyst": "Something that speeds up a reaction without being used up.",
        "substrate": "The substance an enzyme works on.",
        "denatured": "Describes an enzyme whose shape has changed for good, so it no longer works.",
    },
    "knowledge": [
        {"kind": "card", "title": "Enzymes are biological catalysts",
         "body": ["A catalyst speeds up a reaction. It is not used up or changed by the reaction.",
                  "Enzymes are catalysts made by living cells. They are proteins.",
                  "So enzymes are called biological catalysts.",
                  "One enzyme molecule can be used again and again.",
                  "So a small amount of enzyme can digest a lot of food."]},
        {"kind": "card", "title": "The role of enzymes in digestion",
         "body": ["Large food molecules are too big to be absorbed into the blood.",
                  "Digestive enzymes break them into small molecules that can be absorbed.",
                  "Without enzymes, this would happen far too slowly.",
                  {"figure": "b3-enzyme-breakdown"}]},
        {"kind": "reveal", "title": "The three digestive enzymes",
         "cols": ["Breaks down", "Into"],
         "rows": [
             ("Carbohydrase (amylase)", "Starch", "Simple sugars, such as glucose"),
             ("Protease", "Protein", "Amino acids"),
             ("Lipase", "Lipids (fats and oils)", "Fatty acids and glycerol"),
         ]},
        {"kind": "card", "title": "Where the enzymes are made",
         "body": [{"points": ["Carbohydrase: the salivary glands, the pancreas and the small intestine.",
                              "Protease: the stomach, the pancreas and the small intestine.",
                              "Lipase: the pancreas and the small intestine."]},
                  "All three work in the small intestine. That is where digestion is finished."]},
        {"kind": "card", "title": "How an enzyme works",
         "body": [{"figure": "b3-enzyme-cycle"},
                  "Each enzyme has a special shape.",
                  "Only one kind of substance fits that shape. This is its substrate.",
                  "So each enzyme works on one substrate. Amylase breaks down starch, but not protein.",
                  "The products leave, and the enzyme is ready to work again."]},
        {"kind": "card", "title": "Temperature",
         "body": ["Enzymes in the body work fastest at body temperature, about 37 °C.",
                  "In the cold they work slowly. Warm them up and they work again.",
                  "Too much heat changes the enzyme's shape for good. It is denatured.",
                  "The substrate no longer fits, so the enzyme stops working.",
                  "Cooling it down again does not bring the shape back."]},
        {"kind": "card", "title": "pH",
         "body": ["Each enzyme works best at one pH.",
                  {"points": ["Mouth: about pH 7, neutral. Amylase in saliva works well here.",
                              "Stomach: about pH 2, very acidic. The protease made here works best "
                              "in acid. Amylase stops working.",
                              "Small intestine: slightly alkaline. Amylase, protease and lipase from "
                              "the pancreas work here."]},
                  "The pancreas also releases an alkali. Bile helps too.",
                  "Together they neutralise the stomach acid in the small intestine."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Enzymes are killed by heat.",
              "Enzymes were never alive. Heat changes their shape, so they are denatured.",
              "DIET-13"),
             ("The enzyme gets used up as the food is digested.",
              "Enzymes are not used up. Each one works again and again.", "DIET-14"),
             ("Cold destroys enzymes.",
              "Cold only slows enzymes down. Warm them up and they work again."),
             ("One enzyme can digest any food.",
              "Each enzyme works on one substrate. Lipase digests fats, but not starch."),
         ]}]},
    ],
    "key_fact": "Enzymes are biological catalysts. They speed up the breakdown of large food "
                "molecules into small ones. They are not used up.",
    "deeper": [
        {"kind": "card", "title": "Enzymes in washing powder",
         "body": ["Biological washing powder contains protease and lipase.",
                  "They digest stains made of protein, such as blood, and grease.",
                  "That is why they are used in a cool wash, not a very hot one.",
                  "A very hot wash would denature the enzymes."]},
        {"kind": "card", "title": "Pineapple and jelly",
         "body": ["Fresh pineapple contains a protease.",
                  "Jelly is set by a protein called gelatin. The protease breaks it down.",
                  "So jelly made with fresh pineapple does not set.",
                  "Tinned pineapple has been heated, which denatures the protease. Its jelly sets."]},
    ],
    "try": None,
    "tutor_body": "Want to talk through why a denatured enzyme stops working?",
    "ks4_becomes": "The active site, and how temperature and pH change the rate of an enzyme reaction.",
    "figures": [
        {"id": "b3-enzyme-breakdown", "kind": "diagram", "status": "drawn", "art": "b3-enzyme-breakdown",
         "title": "Three digestive enzymes breaking large molecules into small ones",
         "desc": "Three rows, each with an arrow from a large molecule on the left to small molecules "
                 "on the right. Carbohydrase: a chain of six linked hexagons, labelled starch, becomes "
                 "six separate hexagons, labelled sugars (glucose). Protease: a chain of six linked "
                 "beads, labelled protein, becomes six separate beads, labelled amino acids. Lipase: a "
                 "short bar with three zigzag tails attached, labelled lipid (fat), becomes the bar on "
                 "its own, labelled glycerol, and three separate tails, labelled fatty acids.",
         "caption": "Each enzyme breaks one kind of large molecule into small ones.",
         "data": {"rows": [
             {"enzyme": "Carbohydrase", "kind": "carbohydrate", "before": "starch",
              "after": "sugars (glucose)"},
             {"enzyme": "Protease", "kind": "protein", "before": "protein", "after": "amino acids"},
             {"enzyme": "Lipase", "kind": "lipid", "before": "lipid (fat)",
              "after": ["glycerol", "fatty acids"]},
         ]}},
        {"id": "b3-enzyme-cycle", "kind": "diagram", "status": "drawn", "art": "b3-enzyme-cycle",
         "title": "How an enzyme works, in three steps",
         "desc": "Three numbered steps, one under another. Each shows the same enzyme, a rounded block "
                 "with a notch cut into its top edge. Step 1: a substrate made of two joined squares "
                 "sits above the notch, with an arrow down. It is shaped to fit the notch. Text: the "
                 "substrate fits the enzyme's shape. Step 2: the substrate sits in the notch, with a "
                 "zigzag mark where the two squares join. Text: the enzyme breaks the substrate apart. "
                 "Step 3: the two squares, now labelled products, move away from the enzyme. The notch "
                 "is empty and the same shape as before. Text: the products leave. The enzyme is "
                 "unchanged, and can work again.",
         "caption": "The enzyme is the same at the end as at the start.",
         "data": {"labels": {"enzyme": "enzyme", "substrate": "substrate", "products": "products"},
                  "steps": [["The substrate fits", "the enzyme's shape."],
                            ["The enzyme breaks", "the substrate apart."],
                            ["The products leave.", "The enzyme is", "unchanged, and can",
                             "work again."]]}},
    ],
    "ladder_stem": {
        "explain": "Amylase from saliva works in the mouth but stops in the stomach. Starch digestion "
                   "starts again in the small intestine. Explain all three stages. Say what the "
                   "pancreas adds besides enzymes.",
        "produce": "A biological washing powder claims to work at any temperature. Predict what its "
                   "enzymes do at 20 °C, at 40 °C and at 90 °C. Then plan a fair test of the claim.",
    },
    "ladder_ticks": [
        ["Says the pancreas also supplies an alkali that neutralises the stomach acid, raising the pH "
         "to around 8.",
         "Says the pancreas also adds an alkali that neutralises the stomach acid."],
        ["Makes clear that the amylase which entered the stomach does not recover — the resumed "
         "digestion uses new enzyme.",
         "Says saliva's amylase does not work again after the stomach acid."],
        ["Predicts slow action at 20 °C — enzymes work, but the rate is low.",
         "Predicts slow cleaning at 20 °C. The enzymes work, but slowly."],
        ["Predicts little or no enzyme action at 90 °C because the enzymes are denatured, while "
         "noting hot water alone still removes some dirt.",
         "Predicts little or no enzyme action at 90 °C, as the enzymes are denatured."],
        ["Describes a fair test: identical stains, identical fabric, same mass of powder, same time, "
         "only the temperature changed.",
         "Plans a fair test: same stain, fabric, mass of powder and time. Only temperature changes."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Enzymes are catalysts, so they are not used up. All of it is left.",
            1: "None is lost. Each enzyme molecule is ready to work again after each job.",
            2: "The amount of enzyme stays the same, however much starch it breaks down.",
        },
        "apply": {
            0: "37 °C is body temperature, so it is warm enough. The enzyme itself has changed.",
            1: "Enzymes were never alive, so they cannot be killed. Heat denatures them.",
            2: "Starch is not denatured. The heat changed the shape of the enzyme.",
        },
    },
}
