# -*- coding: utf-8 -*-
"""Acid + metal, in the lean shape. Spec table: docs/lessons/wave2/ks3-acid-plus-metal.md."""

LESSON = {
    "slug": "acid-plus-metal",
    "start": {
        "setup": "A strip of magnesium is dropped into dilute hydrochloric acid. "
                 "It fizzes, and the magnesium disappears.",
        "question": "If you had to guess, did the gas come from the metal, or from the acid?",
        "options": [
            ("From the metal",
             "The metal has dissolved into the liquid as a salt. The gas is hydrogen from the acid."),
            ("From the acid",
             "Right. Every acid contains hydrogen. The metal takes its place, and the hydrogen bubbles off."),
        ],
        "answer": 1,
    },
    "words": ["salt", "hydrogen", "reactive", "squeaky pop test"],
    "word_defs": {
        "salt": "The compound made when a metal takes the place of the hydrogen in an acid.",
        "hydrogen": "The gas given off when a metal reacts with an acid.",
        "reactive": "Reacts easily. The more reactive a metal is, the faster it reacts.",
        "squeaky pop test": "The test for hydrogen. A lit splint at the mouth of a tube of it makes a squeaky pop.",
    },
    "knowledge": [
        {"kind": "card", "title": "What you see",
         "body": ["Drop a piece of magnesium into dilute hydrochloric acid.",
                  {"points": ["Bubbles of gas fizz off the metal.",
                              "The metal gets smaller, then disappears.",
                              "The tube gets warm."]},
                  "The gas is hydrogen."]},
        {"kind": "card", "title": "The general equation",
         "body": ["Reactive metals all react with acids in the same way.",
                  {"figure": "c6-word-metal-acid"},
                  "The salt is made from the metal and part of the acid.",
                  "The hydrogen comes from the acid."]},
        {"kind": "card", "title": "Where the metal goes",
         "body": ["The metal does not turn into a gas.",
                  "It dissolves in the liquid as part of the salt.",
                  "Evaporate the water, and the salt is left behind as crystals.",
                  "Magnesium and hydrochloric acid leave white crystals of magnesium chloride."]},
        {"kind": "card", "title": "Naming the salt",
         "body": ["The first word of the salt's name is the metal.",
                  "The second word comes from the acid.",
                  {"points": ["Hydrochloric acid makes chlorides.",
                              "Sulfuric acid makes sulfates."]},
                  "So zinc and sulfuric acid make zinc sulfate and hydrogen."]},
        {"kind": "reveal", "title": "Word equations with hydrochloric acid",
         "cols": ["Products"],
         "rows": [
             ("magnesium + hydrochloric acid", "magnesium chloride + hydrogen"),
             ("zinc + hydrochloric acid", "zinc chloride + hydrogen"),
             ("iron + hydrochloric acid", "iron chloride + hydrogen"),
             ("copper + hydrochloric acid", "No reaction"),
         ]},
        {"kind": "card", "title": "Some metals react faster",
         "body": ["In dilute hydrochloric acid, the more reactive the metal, the faster it fizzes.",
                  {"points": ["Magnesium fizzes fast, and the tube gets warm.",
                              "Zinc fizzes steadily.",
                              "Iron fizzes slowly.",
                              "Copper does not react at all."]},
                  "Copper is below hydrogen in the reactivity series.",
                  "So it cannot push hydrogen out of a dilute acid."]},
        {"kind": "card", "title": "Testing for hydrogen",
         "body": [{"figure": "c6-squeaky-pop"},
                  {"points": ["Hold an empty test tube upside down over the reaction.",
                              "Hydrogen is less dense than air, so it rises into the tube.",
                              "Close the tube with a bung. Move it away from the reaction.",
                              "Take out the bung and hold a lit splint at the mouth."]},
                  "A squeaky pop shows the gas is hydrogen.",
                  "The pop is hydrogen burning quickly with oxygen in the air. It makes water."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The bubbles are the metal turning into a gas.",
              "The bubbles are hydrogen from the acid. The metal dissolves as a salt.",
              "ACID-07"),
             ("Every metal reacts with dilute acids.",
              "Copper does not react with dilute hydrochloric or sulfuric acid."),
             ("A metal and an acid make a salt and water.",
              "A metal and an acid make a salt and hydrogen."),
             ("Hydrochloric acid makes sulfates.",
              "Hydrochloric acid makes chlorides. Sulfuric acid makes sulfates."),
         ]}]},
    ],
    "key_fact": "A metal reacts with an acid to make a salt and hydrogen. The hydrogen comes from the "
                "acid. A lit splint at the mouth of a tube of hydrogen gives a squeaky pop.",
    "deeper": [
        {"kind": "card", "title": "Why copper does not react",
         "body": ["Metals can be put in order, from most reactive to least reactive.",
                  "This order is the reactivity series. Hydrogen is often put in it too.",
                  "A metal above hydrogen can take the place of hydrogen in an acid.",
                  "Copper, silver and gold are below hydrogen.",
                  "So they do not react with dilute hydrochloric or sulfuric acid."]},
        {"kind": "card", "title": "Too reactive for the lab",
         "body": ["Sodium and potassium react with acids violently.",
                  "The hydrogen can catch fire. So they are never added to acid in school."]},
        {"kind": "card", "title": "Why acids are not kept in metal cans",
         "body": ["Acids are kept in glass or plastic bottles.",
                  "Many metals would react with the acid and give off hydrogen.",
                  "Hydrogen mixed with air can explode if it meets a flame."]},
    ],
    "try": None,
    "tutor_body": "Want to practise writing word equations for metals and acids?",
    "safety_note": "Wear eye protection. Dilute acids can harm your eyes and skin. Only test small "
                   "amounts of hydrogen, away from the reaction. Hydrogen mixed with air can explode.",
    # the classic heading "Next in this unit" named lessons that are not next (Unit 3 walk)
    "connects_heading": None,
    "ks4_becomes": "Metals with acids explained using ions and electrons, and the reactivity series "
                   "in more detail.",
    "figures": [
        {"id": "c6-word-metal-acid", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The general equation for a metal and an acid",
         "desc": "Metal plus acid at the top, labelled reactants. A drawn arrow points down to salt "
                 "plus hydrogen, labelled products.",
         "caption": "Every reactive metal gives a salt and hydrogen with an acid.",
         "eq": {"left": ["metal", "acid"], "right": ["salt", "hydrogen"]}},
        {"id": "c6-squeaky-pop", "kind": "diagram", "status": "drawn", "art": "c6-squeaky-pop",
         "title": "The squeaky pop test for hydrogen",
         "desc": "Three steps, one under another. Step 1, Collect: magnesium ribbon fizzes in acid "
                 "in an upright test tube. An empty test tube is held upside down over its mouth, "
                 "and bubbles of hydrogen rise into it. Step 2, Stopper: the full tube, still upside "
                 "down, is closed with a bung, and an arrow shows it moved away. Step 3, Test: the "
                 "bung is out and a lit splint is held at the tube's mouth. Short lines burst from "
                 "the mouth, labelled squeaky pop.",
         "caption": "Collect the gas, close the tube, then test it away from the reaction.",
         "data": {
             "labels": {"metal": "magnesium", "acid": "acid", "hydrogen": "hydrogen",
                        "pop": "squeaky pop"},
             "steps": [
                 {"title": "Collect", "lines": ["Hold an empty tube", "upside down over the",
                                                "reaction. Hydrogen", "rises into it."]},
                 {"title": "Stopper", "lines": ["Put a bung in.", "Move the tube away",
                                                "from the reaction."]},
                 {"title": "Test", "lines": ["Hold a lit splint at", "the mouth. A squeaky",
                                             "pop means hydrogen."]},
             ]}},
    ],
    "ladder_stem": {
        "explain": "Magnesium is dropped into dilute hydrochloric acid. Describe what you would see. "
                   "Name both products. Explain where the gas comes from.",
        "produce": "You have four unlabelled metals and some dilute hydrochloric acid. Explain how "
                   "you would put the metals in order of reactivity. Say how you would make it a "
                   "fair test.",
    },
    "ladder_feedback": {
        "recall": {
            0: "Chlorides come from hydrochloric acid. Sulfuric acid makes sulfates.",
            1: "A metal and an acid give off hydrogen. No water is made.",
            2: "Sulfuric acid makes a sulfate. A metal and an acid give off hydrogen.",
        },
        "apply": {
            1: "Warming does not help. Copper is too unreactive to give off hydrogen.",
            2: "Copper is a metal. It is a very unreactive one.",
            3: "Waiting longer does not help. Copper is too unreactive to give off hydrogen.",
        },
    },
}
