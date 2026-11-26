# -*- coding: utf-8 -*-
"""Chemical change vs physical change, in the lean shape. Spec table: docs/lessons/wave2/ks3-chemical-vs-physical-change.md."""

LESSON = {
    "slug": "chemical-vs-physical-change",
    "start": {
        "setup": "Both changes were caused by heat. Melting chocolate is a physical change. "
                 "Frying an egg is a chemical change.",
        "question": "If you had to guess, what makes frying an egg a chemical change: the change "
                    "of colour, or that something new is made?",
        "options": [
            ("The change of colour",
             "Colour is only a clue. Food colouring in water changes colour, but nothing new is made."),
            ("Something new is made",
             "Right. Cooked egg white is a new substance. It is firm and white, not runny and clear."),
        ],
        "answer": 1,
    },
    "words": ["substance", "physical change", "chemical change", "chemical reaction"],
    "word_defs": {
        "substance": "One kind of material with its own properties, such as water, iron or salt.",
        "physical change": "A change that makes no new substance. The same substances are still there.",
        "chemical change": "A change that makes at least one new substance.",
        "chemical reaction": "A change that rearranges atoms to make new substances. Another name for a chemical change.",
    },
    "knowledge": [
        {"kind": "card", "title": "Physical change",
         "body": ["In a physical change, no new substance is made.",
                  "The same substances are still there. They have changed state, shape or place, "
                  "or been mixed.",
                  {"points": ["Melted ice is still water, now a liquid.",
                              "Sugar dissolving in tea is still sugar, spread through the water.",
                              "A smashed glass is still glass, in pieces."]},
                  "Melting, freezing, boiling, dissolving and breaking are all physical changes."]},
        {"kind": "card", "title": "Chemical change",
         "body": ["In a chemical change, at least one new substance is made.",
                  "The new substance has different properties from what you started with.",
                  "A chemical change is also called a chemical reaction.",
                  {"points": ["Wax burning makes carbon dioxide and water vapour.",
                              "An iron nail rusting makes rust, a new substance.",
                              "Frying an egg makes cooked egg white, which stays firm.",
                              "Marble chips fizzing in acid make carbon dioxide gas."]}]},
        {"kind": "card", "title": "What happens to the particles",
         "body": [{"figure": "c4-change-particles"},
                  "When ice melts, the water particles move around more. They are still water particles.",
                  "When hydrogen burns, its atoms join up with oxygen atoms in a new way.",
                  "They make new particles of water, a new substance."]},
        {"kind": "card", "title": "Signs of a chemical change",
         "body": ["These signs show that a chemical change may have happened:",
                  {"points": ["Bubbles of gas are given off, so it fizzes.",
                              "The colour changes.",
                              "It gets hot or cold.",
                              "Light is given out, or a flame.",
                              "There is a new smell.",
                              "A solid appears when two solutions are mixed."]},
                  "Each sign is only a clue. Some physical changes show them too.",
                  "Boiling water bubbles. Mixing two paints changes colour.",
                  "The test is whether a new substance has been made."]},
        {"kind": "reveal", "title": "Physical or chemical",
         "cols": ["Kind of change", "Why"],
         "rows": [
             ("Ice melting", "Physical", "It is still water, now a liquid"),
             ("Sugar dissolving in tea", "Physical", "Evaporate the water and the sugar is left"),
             ("A glass smashing", "Physical", "The pieces are still glass"),
             ("Chocolate melting", "Physical", "It sets back into chocolate as it cools"),
             ("Sugar melting in a hot pan", "Physical", "It is still sugar, and sets solid as it cools"),
             ("Sugar turning brown in a hot pan", "Chemical",
              "New substances form, with a new colour and smell"),
             ("Wax burning", "Chemical", "It makes carbon dioxide and water vapour"),
             ("An iron nail rusting", "Chemical", "It makes rust, a new substance"),
             ("Frying an egg", "Chemical", "Cooked egg white is a new substance"),
         ]},
        {"kind": "card", "title": "Undoing a change",
         "body": ["Most physical changes are easy to reverse. Cool melted wax and it sets again.",
                  "Most chemical changes are hard to reverse.",
                  "But undoing is only a clue. It does not decide the kind of change.",
                  "A smashed glass cannot be put back together. It is still a physical change.",
                  "Rusting is a chemical change. Yet a blast furnace can get iron back from iron oxide."]},
        {"kind": "card", "title": "Two things that seem to dissolve",
         "body": ["Salt stirred into water and marble chips in acid both seem to vanish.",
                  "Salt dissolving is a physical change. Evaporate the water and the salt comes back.",
                  "Marble chips in acid is a chemical change. The chips fizz and make carbon dioxide.",
                  "Evaporate that liquid and you get a different white solid, not marble."]},
        {"kind": "reveal", "title": "Physical and chemical changes compared",
         "cols": ["Physical change", "Chemical change"],
         "rows": [
             ("New substance made", "No", "Yes, at least one"),
             ("The particles", "The same particles, moved or mixed", "Atoms joined up in new particles"),
             ("Easy to reverse", "Usually", "Usually not"),
             ("Examples", "Melting, boiling, dissolving, breaking",
              "Burning, rusting, cooking, marble in acid"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("If a change cannot be undone, it must be chemical.",
              "A smashed glass cannot be put back, but it is still glass. It is physical.",
              "REACT-01"),
             ("Anything that vanishes into a liquid is the same kind of change.",
              "Salt in water is physical. Marble fizzing away in acid is chemical.",
              "REACT-02"),
             ("A colour change always means a chemical change.",
              "Food colouring in water changes colour, but nothing new is made."),
             ("Bubbles always mean a new gas has been made.",
              "Boiling water bubbles too. Those bubbles are water as a gas."),
         ]}]},
    ],
    "key_fact": "A chemical change makes at least one new substance. A physical change makes no new "
                "substance, so the same substances are still there.",
    "deeper": [
        {"kind": "card", "title": "Changes in the kitchen",
         "body": ["Cooking uses heat, but not every change in a pan is chemical.",
                  "Melting butter in a pan is physical. It sets again in the fridge.",
                  "Toasting bread is chemical. New substances give toast its brown colour and smell.",
                  "Whipping cream is physical. Whip it too far and the fat clumps into butter.",
                  "Nothing new is made in the butter. The fat was in the cream all along."]},
        {"kind": "card", "title": "Writing a comparison",
         "body": ["To compare two changes, link them with whereas.",
                  "Melting wax is physical as nothing new forms, whereas burning wax makes new substances."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why a change you cannot undo can still be physical?",
    "connects_heading": None,
    "ks4_becomes": "Energy changes in reactions, and bond breaking and bond making.",
    "figures": [
        {"id": "c4-change-particles", "kind": "diagram", "status": "drawn",
         "art": "c4-change-particles",
         "title": "A physical change and a chemical change, as particles",
         "desc": "Two rows. Top row, labelled Physical change: ice melts. A box labelled Ice holds six "
                 "water particles in two neat rows, all facing the same way. Each water particle is a "
                 "red oxygen atom with two small white hydrogen atoms joined to it. A drawn arrow points "
                 "to a box labelled Liquid water, holding the same six water particles at different "
                 "angles. Under it: still water particles. Bottom row, labelled Chemical change: "
                 "hydrogen burns. A box labelled Hydrogen + oxygen holds two pairs of joined white "
                 "hydrogen atoms and one pair of joined red oxygen atoms. A drawn arrow points to a "
                 "box labelled Water, holding two water particles. Under it: atoms joined up in new "
                 "particles. A key at the bottom: red circle, oxygen atom; white circle, hydrogen atom.",
         "caption": "Melting moves the same particles. A reaction joins the atoms up in new particles.",
         "data": {
             "rows": [
                 {"label": "Physical change: ice melts",
                  "left": {"label": "Ice", "layout": "rows", "mols": ["H2O"] * 6},
                  "right": {"label": "Liquid water", "layout": "jumble", "mols": ["H2O"] * 6},
                  "note": "still water particles"},
                 {"label": "Chemical change: hydrogen burns",
                  "left": {"label": "Hydrogen + oxygen", "layout": "jumble", "mols": ["H2", "H2", "O2"]},
                  "right": {"label": "Water", "layout": "jumble", "mols": ["H2O", "H2O"]},
                  "note": "atoms joined up in new particles"},
             ],
             "legend": [["O", "oxygen atom"], ["H", "hydrogen atom"]],
         }},
    ],
    "ladder_stem": {
        "explain": "A student heats sugar in a pan. First it melts to a clear syrup. Then it turns "
                   "brown and smells of caramel. They say it was all one change. Explain how many "
                   "changes happened, and which kind each was. Give your evidence.",
        "produce": "A cook says cooking is just heating food up. Pick one physical change and one "
                   "chemical change from a kitchen. Use them to explain why the cook is wrong. Say "
                   "why the idea is easy to believe.",
    },
    "ladder_ticks": [
        ["Says melting is a physical change — still sugar, and it would set back to sugar on cooling.",
         "Says melting is a physical change. It is still sugar, and sets solid again on cooling."],
        ["Makes the comparison linked, not two separate descriptions — for example using \"whereas\".",
         "Links the two changes in one comparison, for example using whereas."],
        ["Explains why the sentence is tempting — heat is involved in both, and both look dramatic.",
         "Explains why the idea is easy to believe. Heat is used in both, and both look dramatic."],
        ["Notes that one of them can be undone and the other cannot, and that this is a consequence rather than the definition.",
         "Notes that undoing is only a clue, not the test for a chemical change."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "A smashed glass cannot be put back together, but it is physical. Undoing is only a clue.",
            1: "Colour is only a clue. Food colouring in water changes colour, but nothing new is made.",
            3: "Melting needs heat and makes nothing new. Rusting needs no heating at all.",
        },
        "apply": {
            0: "The marble fizzes and makes carbon dioxide. That is a new substance, so it is chemical.",
            1: "The salt is not destroyed. Evaporate the water and the salt comes back.",
            3: "That is the wrong way round. Salt comes back from the water. Marble makes a new gas.",
        },
    },
}
