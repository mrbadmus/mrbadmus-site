# -*- coding: utf-8 -*-
"""Absorption and the small intestine, in the lean shape.
Spec table: docs/lessons/wave2/ks3-absorption-and-the-small-intestine.md.

Rainford 16c (Visking tubing) has no page of its own. It is taught here, as a drawn model of
the gut wall: starch stays in, glucose passes out. It is the evidence for 15b's "why food needs
to be digested". Both figures are new and phone width.
"""

LESSON = {
    "slug": "absorption-and-the-small-intestine",
    "start": {
        "setup": "A garden hose and your small intestine are about the same length and width.",
        "question": "If you had to guess, how does the intestine get sixty times the surface of a hose?",
        "options": [
            ("It is coiled up",
             "Coiling a tube does not add any inside surface. The wall itself is folded."),
            ("Its wall is folded",
             "Yes. The wall is folded, and the folds are covered in tiny villi."),
        ],
        "answer": 1,
    },
    "words": ["absorption", "villi", "diffusion", "surface area"],
    "word_defs": {
        "absorption": "Small food molecules passing from the gut into the blood.",
        "villi": "Tiny finger-like parts that cover the inside wall of the small intestine.",
        "diffusion": "Particles spreading from a high concentration to a low concentration.",
        "surface area": "The total area of a surface. A bigger area means faster absorption.",
    },
    "knowledge": [
        {"kind": "card", "title": "Why food must be digested first",
         "body": ["Starch, protein and fat molecules are large. They cannot pass through the gut wall.",
                  "Digestion breaks them into small, soluble molecules.",
                  "Only these small molecules can pass into the blood."]},
        {"kind": "card", "title": "Absorption",
         "body": ["Absorption is small food molecules passing from the gut into the blood.",
                  "Almost all of it happens in the small intestine.",
                  "The molecules cross the wall by diffusion.",
                  "They move from high concentration in the gut to low concentration in the blood.",
                  "The blood then carries them around the body, to every cell."]},
        {"kind": "card", "title": "Villi",
         "body": ["The inside wall of the small intestine is covered in millions of villi.",
                  "Each villus is a tiny, finger-like part of the wall.",
                  {"figure": "b3-villus-lean"}]},
        {"kind": "reveal", "title": "How villi are adapted for absorption",
         "cols": ["What it is like", "How it helps"],
         "rows": [
             ("Surface area", "Very large, from folds, villi and microvilli.",
              "More molecules can be absorbed at the same time."),
             ("Wall", "Only one cell thick.", "Molecules only have a short distance to diffuse."),
             ("Blood supply", "Capillaries run through every villus.",
              "Blood carries food molecules away. This keeps the concentration low in the blood."),
         ]},
        {"kind": "card", "title": "Folds on folds",
         "body": ["The inside wall of the small intestine is folded.",
                  "The folds are covered in villi.",
                  "The cells on each villus have even smaller parts, called microvilli.",
                  "Together they give about 30 m² of surface to absorb food.",
                  "That is about 60 times the inside of a smooth tube the same size."]},
        {"kind": "card", "title": "The Visking tubing model",
         "body": ["Visking tubing has tiny holes. Small molecules can pass through. Large molecules cannot.",
                  {"points": ["Put a mixture of starch and glucose solution in a bag of Visking tubing.",
                              "Rinse the outside, then hang the bag in a beaker of water.",
                              "After 15 minutes, test the water for starch and for glucose."]},
                  {"figure": "b3-visking"}]},
        {"kind": "reveal", "title": "Testing the water outside the tubing",
         "cols": ["Result", "What it shows"],
         "rows": [
             ("Iodine test for starch", "No colour change.", "No starch got out. Its molecules are too big."),
             ("Benedict's test for glucose", "Turns from blue to green, yellow, orange or brick red when heated.",
              "Glucose got out. Its molecules are small enough."),
         ]},
        {"kind": "reveal", "title": "What the model stands for",
         "cols": ["In the model"],
         "rows": [
             ("The wall of the small intestine", "The Visking tubing."),
             ("Food in the small intestine", "The starch and glucose inside the bag."),
             ("The blood", "The water outside the bag."),
         ]},
        {"kind": "card", "title": "What the model shows",
         "body": ["Glucose is small, so it passes through the tubing. Starch is too big, so it stays in.",
                  "In the same way, starch cannot pass through the gut wall.",
                  "It must be digested into sugars first. Then it can be absorbed."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Villi make the intestine longer.",
              "Villi add surface area. The length stays the same.", "DIET-15"),
             ("The muscles push the food through the gut wall into the blood.",
              "Food molecules cross the wall by diffusion. Muscles only move food along the gut.",
              "DIET-16"),
             ("Starch can pass through the gut wall.",
              "Starch molecules are too big. Starch must be digested into sugars first."),
             ("Most food is absorbed in the stomach.",
              "Most food is absorbed in the small intestine."),
         ]}]},
    ],
    "key_fact": "Digested food is absorbed into the blood in the small intestine, by diffusion. "
                "Villi give a large surface area, a thin wall and a good blood supply.",
    "deeper": [
        {"kind": "card", "title": "Where the model is not like the gut",
         "body": ["The tubing is not alive. It has no villi and no folds.",
                  "In the body, blood flows past and carries the glucose away.",
                  "In the model, the water stays still. Glucose builds up in it.",
                  "So in the model, glucose moves out more and more slowly."]},
        {"kind": "card", "title": "Other exchange surfaces",
         "body": ["Lungs and the gills of fish work the same way.",
                  "Each has a large surface area, a thin wall and a good blood supply."]},
    ],
    "try": None,
    "tutor_body": "Want to work through why blood flow keeps absorption going?",
    "ks4_becomes": "Exchange surfaces, surface area to volume ratio, and active transport.",
    "figures": [
        {"id": "b3-villus-lean", "kind": "diagram", "status": "drawn", "art": "b3-villus-lean",
         "title": "Villi on the wall of the small intestine, and one villus magnified",
         "desc": "Top: a strip of the small intestine wall with seven finger-shaped villi standing up "
                 "from it. Small circles above them are digested food molecules in the gut. One villus "
                 "is outlined in orange. Caption: millions of villi cover the wall. Bottom, in a dashed "
                 "frame: that villus magnified and cut through. Its wall is a single row of cells, "
                 "labelled wall one cell thick. Tiny bristles on the outside of the cells are labelled "
                 "microvilli. A blue loop inside is labelled capillary (blood). Two arrows labelled "
                 "glucose and amino acids go from the gut, through the wall, into the capillary. "
                 "Underneath: food molecules diffuse into the blood.",
         "caption": "Every villus has a thin wall and a capillary close behind it.",
         "data": {"labels": {
             "strip": "SMALL INTESTINE WALL", "strip_note": "Millions of villi cover the wall.",
             "close": "ONE VILLUS, MAGNIFIED", "microvilli": ["Microvilli"],
             "wall": ["Wall one", "cell thick"], "capillary": ["Capillary", "(blood)"],
             "crossing": ["glucose", "amino acids"],
             "foot": "Food molecules diffuse into the blood."}}},
        {"id": "b3-visking", "kind": "diagram", "status": "drawn", "art": "b3-visking",
         "title": "The Visking tubing model, after 15 minutes",
         "desc": "A beaker of water with a glass rod across the top. A bag of Visking tubing hangs from "
                 "the rod on a thread, under the water. The bag holds starch, drawn as chains of five "
                 "linked hexagons, and glucose, drawn as single hexagons. Some single glucose hexagons "
                 "are now in the water outside the bag, and two arrows show glucose crossing the tubing "
                 "out into the water. Every starch chain is still inside the bag. Labels: Visking tubing "
                 "(the gut wall); starch and glucose solution; glucose gets out; starch stays in; water "
                 "(the blood). A key shows a chain of hexagons as starch and one hexagon as glucose.",
         "caption": "Glucose passes through the tubing. Starch does not.",
         "data": {"labels": {
             "heading": "AFTER 15 MINUTES", "tubing": ["Visking tubing", "(the gut wall)"],
             "inside": ["Starch and", "glucose solution"], "water": ["Water", "(the blood)"],
             "out": "Glucose gets out", "in": "Starch stays in",
             "key_starch": "starch", "key_glucose": "glucose"}}},
    ],
    "ladder_stem": {
        "explain": "Explain how villi absorb a meal quickly. Say what the large surface area, the thin "
                   "wall and the blood supply each do. Say why one alone would not be enough.",
        "produce": "In coeliac disease, the body reacts to gluten in food, and the villi become flattened. "
                   "Predict what a patient would notice. Explain it using this lesson. Say why they "
                   "might be short of iron, even when they eat plenty of it.",
    },
    "ladder_ticks": [
        ["Names diffusion as the process, and says it happens because of a concentration difference "
         "rather than a push.",
         "Names diffusion, from a high to a low concentration."],
        ["Explains why one alone is not enough — e.g. a huge area with no blood flow still stops once "
         "the two sides equalise.",
         "Says why one is not enough. A large area with no blood flow soon stops absorbing."],
        ["Explains it as a loss of surface area — the folding is gone, so far fewer molecules can cross.",
         "Says flattened villi give less surface area, so far fewer molecules are absorbed."],
        ["Connects this to the earlier lesson: a deficiency with an adequate diet, caused by the gut "
         "rather than the plate.",
         "Links to deficiency diseases: the diet has the iron, but the gut absorbs too little."],
        ["Says iron is eaten but not absorbed, so it never reaches the blood.",
         "Says iron is eaten but less is absorbed, so less reaches the blood."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Villi do not add any length. They add surface area.",
            1: "Villi do not add volume. They give a bigger surface for absorbing food.",
            3: "Villi do not make muscles stronger. They give a bigger surface for absorbing food.",
        },
        "apply": {
            0: "Diffusion needs a concentration difference. Without blood flow, that difference disappears.",
            1: "Nothing pushes glucose back. Once both sides are equal, it stops moving across overall.",
            2: "Blood carrying glucose away keeps absorption going. Without it, absorption stops.",
        },
    },
}
