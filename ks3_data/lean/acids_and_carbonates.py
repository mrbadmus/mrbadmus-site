# -*- coding: utf-8 -*-
"""Acids and carbonates, in the lean shape. Spec table: docs/lessons/wave2/ks3-acids-and-carbonates.md."""

LESSON = {
    "slug": "acids-and-carbonates",
    "start": {
        "setup": "Marble is calcium carbonate. A marble chip fizzes in dilute hydrochloric acid "
                 "and gives off carbon dioxide.",
        "question": "If you had to guess, does the gas come out of the rock, or out of the acid?",
        "options": [
            ("Out of the rock",
             "Right. Carbon dioxide contains carbon. Only the calcium carbonate has carbon in it."),
            ("Out of the acid",
             "Hydrochloric acid has no carbon in it. The carbon and oxygen come from the carbonate."),
        ],
        "answer": 0,
    },
    "words": ["metal carbonate", "carbon dioxide", "limewater", "delivery tube"],
    "word_defs": {
        "metal carbonate": "A compound of a metal with carbon and oxygen, such as calcium carbonate.",
        "carbon dioxide": "The gas given off when a metal carbonate reacts with an acid.",
        "limewater": "A clear solution that turns milky when carbon dioxide bubbles through it.",
        "delivery tube": "A tube that carries a gas from a reaction into another tube.",
    },
    "knowledge": [
        {"kind": "card", "title": "What you see",
         "body": ["Add dilute hydrochloric acid to marble chips.",
                  {"points": ["The chips fizz as bubbles of gas form.",
                              "The chips get smaller.",
                              "The gas is carbon dioxide."]},
                  "Chalk, limestone and marble are mainly calcium carbonate.",
                  "They all fizz with acid in the same way."]},
        {"kind": "card", "title": "The general equation",
         "body": ["Every metal carbonate reacts with an acid in the same way.",
                  {"figure": "c6-word-carbonate-acid"},
                  "There are three products.",
                  "The carbonate uses up the acid, so the acid is neutralised.",
                  "The carbon dioxide comes from the carbonate."]},
        {"kind": "card", "title": "Naming the salt",
         "body": ["The salt's first word is the metal from the carbonate.",
                  "Its second word comes from the acid.",
                  {"points": ["Hydrochloric acid makes chlorides.",
                              "Sulfuric acid makes sulfates.",
                              "Nitric acid makes nitrates."]},
                  "So calcium carbonate and nitric acid make calcium nitrate, water and carbon dioxide."]},
        {"kind": "reveal", "title": "Word equations with hydrochloric acid",
         "cols": ["Products"],
         "rows": [
             ("calcium carbonate + hydrochloric acid", "calcium chloride + water + carbon dioxide"),
             ("magnesium carbonate + hydrochloric acid",
              "magnesium chloride + water + carbon dioxide"),
             ("copper carbonate + hydrochloric acid", "copper chloride + water + carbon dioxide"),
             ("sodium carbonate + hydrochloric acid", "sodium chloride + water + carbon dioxide"),
         ]},
        {"kind": "card", "title": "The limewater test",
         "body": [{"figure": "c6-limewater-test"},
                  {"points": ["Put the carbonate and the acid in a boiling tube.",
                              "Fit a bung and delivery tube straight away.",
                              "Put the end of the delivery tube under the surface of the limewater.",
                              "Watch the limewater."]},
                  "Carbon dioxide turns limewater from clear to milky.",
                  "This is the test for carbon dioxide."]},
        {"kind": "card", "title": "Why a splint is not enough",
         "body": ["Carbon dioxide puts out a lit splint.",
                  "So do many other gases, such as nitrogen.",
                  "So a splint going out does not show the gas is carbon dioxide.",
                  "Use limewater. If it turns milky, the gas is carbon dioxide."]},
        {"kind": "reveal", "title": "A metal or a carbonate with an acid",
         "cols": ["Metal", "Metal carbonate"],
         "rows": [
             ("Products", "salt + hydrogen", "salt + water + carbon dioxide"),
             ("The gas", "Hydrogen", "Carbon dioxide"),
             ("Test for the gas", "A lit splint gives a squeaky pop", "Limewater turns milky"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A gas that puts out a lit splint is carbon dioxide.",
              "Many gases put out a splint. Limewater turning milky is the test for carbon dioxide.",
              "ACID-08"),
             ("A carbonate and an acid make a salt and hydrogen.",
              "A carbonate and an acid make a salt, water and carbon dioxide."),
             ("Copper carbonate does not react with dilute acid.",
              "Copper carbonate fizzes with acid. It is copper metal that does not react."),
         ]}]},
    ],
    "key_fact": "A metal carbonate reacts with an acid to make a salt, water and carbon dioxide. "
                "Carbon dioxide turns limewater milky.",
    "deeper": [
        {"kind": "card", "title": "What limewater is",
         "body": ["Limewater is calcium hydroxide dissolved in water.",
                  "Carbon dioxide reacts with it to make calcium carbonate.",
                  "Calcium carbonate does not dissolve. Its tiny white specks make the limewater milky."]},
        {"kind": "card", "title": "Too much carbon dioxide",
         "body": ["Keep bubbling carbon dioxide through, and milky limewater goes clear again.",
                  "The extra carbon dioxide makes the white specks dissolve.",
                  "So the result is the change to milky. Watch for it as it happens."]},
        {"kind": "card", "title": "Acid rain and limestone",
         "body": ["Rain is slightly acidic. Acid rain is more acidic.",
                  "Limestone and marble are mainly calcium carbonate, so the acid slowly reacts with them.",
                  "Over many years, statues and buildings made of them wear away."]},
    ],
    "try": None,
    "tutor_body": "Want to practise the word equations for carbonates and acids?",
    "safety_note": "Wear eye protection. A carbonate fizzes hard in acid and can spit liquid out of "
                   "the tube. Limewater is an alkali, so wash it off your skin.",
    "ks4_becomes": "Tests for gases and for carbonates, and the reactions of acids in more detail.",
    "figures": [
        {"id": "c6-word-carbonate-acid", "kind": "diagram", "status": "drawn", "art": "word-equation",
         "title": "The general equation for a metal carbonate and an acid",
         "desc": "Metal carbonate plus acid at the top, labelled reactants. A drawn arrow points "
                 "down to salt plus water plus carbon dioxide, labelled products.",
         "caption": "Every metal carbonate gives a salt, water and carbon dioxide with an acid.",
         "eq": {"left": ["metal carbonate", "acid"], "right": ["salt", "water", "carbon dioxide"]}},
        {"id": "c6-limewater-test", "kind": "diagram", "status": "drawn", "art": "c6-limewater-test",
         "title": "The limewater test for carbon dioxide",
         "desc": "On the left, a boiling tube holds marble chips in dilute hydrochloric acid, with "
                 "bubbles rising. A bung closes it. A delivery tube runs up from the bung, across, "
                 "and down into a second tube of limewater on the right. The end of the delivery "
                 "tube is under the surface, bubbles rise from it, and the limewater is milky. "
                 "Below, labelled The result: a tube of clear limewater marked before, an arrow, "
                 "and a tube of milky limewater marked after.",
         "caption": "The end of the delivery tube must be under the limewater.",
         "data": {
             "colours": {"milky": "#ECE8DF"},
             "labels": {"bung": "bung", "delivery": "delivery tube",
                        "acid": ["dilute", "hydrochloric acid"],
                        "chips": ["marble chips", "(calcium carbonate)"],
                        "limewater": ["limewater", "turns milky"],
                        "end": ["end under", "the surface"],
                        "result": "The result", "before": "before: clear", "after": "after: milky"},
         }},
    ],
    "ladder_stem": {
        "explain": "Marble chips are dropped into dilute hydrochloric acid. Describe what you would "
                   "see. Name all three products. Explain how you would show the gas is carbon dioxide.",
        "produce": "Two white powders are on the bench. One is a carbonate and one is not. You must "
                   "not taste or touch them. Plan a test to tell them apart. Say what result would "
                   "show which one is the carbonate.",
    },
    "ladder_feedback": {
        "recall": {
            0: "Hydrogen comes from a metal and an acid. A carbonate gives water and carbon dioxide.",
            1: "No hydrogen is made. The gas from a carbonate is carbon dioxide.",
            3: "A salt is always made. No hydrogen is made with a carbonate.",
        },
        "apply": {
            0: "That is the test for oxygen, and no splint was used. Clear limewater only rules out carbon dioxide.",
            2: "Carbon dioxide turns limewater milky. Clear limewater means the gas is not carbon dioxide.",
            3: "Hydrogen does leave it clear, but so do many gases. Only carbon dioxide is ruled out.",
        },
    },
}
