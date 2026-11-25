# -*- coding: utf-8 -*-
"""Thermal decomposition, in the lean shape. Spec table: docs/lessons/wave2/ks3-thermal-decomposition.md."""

LESSON = {
    "slug": "thermal-decomposition",
    "start": {
        "setup": "A green powder is heated in a test tube. It turns black. "
                 "A gas comes off that turns limewater milky.",
        "question": "If you had to guess, once the heating is over, does what is left in the "
                    "tube weigh more than before, or less?",
        "options": [
            ("Less than before",
             "Right. Carbon dioxide gas escapes from the tube. The black solid left behind weighs less."),
            ("More than before",
             "Nothing joins the powder. Part of it leaves as a gas, so the solid gets lighter."),
        ],
        "answer": 0,
    },
    "words": ["thermal decomposition", "metal carbonate", "metal oxide", "limewater"],
    "word_defs": {
        "thermal decomposition": "Using heat to break down one compound into two or more substances.",
        "metal carbonate": "A compound of a metal with carbon and oxygen, such as copper carbonate.",
        "metal oxide": "A compound of a metal with oxygen, such as copper oxide.",
        "limewater": "A clear solution that turns milky when carbon dioxide bubbles through it.",
    },
    "knowledge": [
        {"kind": "card", "title": "What thermal decomposition is",
         "body": ["Thermal means heat. Decomposition means breaking down.",
                  "In thermal decomposition, heat breaks one compound into two or more substances.",
                  "There is only one reactant. Nothing else is added.",
                  "It needs heat all the time. Take the flame away and it stops."]},
        {"kind": "card", "title": "Heating copper carbonate",
         "body": [{"figure": "c5-heating-carbonate"},
                  {"points": ["The green powder turns black.",
                              "A gas comes off and turns the limewater milky.",
                              "So the gas is carbon dioxide.",
                              "The black solid left in the tube is copper oxide."]}]},
        {"kind": "card", "title": "The general equation",
         "body": ["Many metal carbonates break down like this when they are heated.",
                  {"figure": "c5-word-carbonate-heat"},
                  "The metal oxide stays in the tube. The carbon dioxide escapes."]},
        {"kind": "reveal", "title": "Word equations for heating metal carbonates",
         "cols": ["Products"],
         "rows": [
             ("copper carbonate", "copper oxide + carbon dioxide"),
             ("calcium carbonate", "calcium oxide + carbon dioxide"),
             ("zinc carbonate", "zinc oxide + carbon dioxide"),
             ("magnesium carbonate", "magnesium oxide + carbon dioxide"),
         ]},
        {"kind": "card", "title": "Why the mass goes down",
         "body": ["Weigh the tube of powder before and after heating.",
                  "The solid left behind weighs less.",
                  "No mass is destroyed. The carbon dioxide has escaped into the air.",
                  "Collect and weigh the gas too, and the total mass stays the same."]},
        {"kind": "card", "title": "It is not burning",
         "body": ["Burning needs oxygen from the air. Thermal decomposition does not.",
                  "Copper carbonate breaks down even in a tube with no air in it.",
                  "When a metal burns, it gains oxygen and gets heavier.",
                  "Here the solid gets lighter.",
                  "The black solid is copper oxide. It is not soot."]},
        {"kind": "card", "title": "Limestone and cement",
         "body": ["Limestone is mainly calcium carbonate.",
                  "Cement is made by heating limestone with clay in a very hot kiln.",
                  "In the kiln, the calcium carbonate breaks down and gives off carbon dioxide.",
                  "This carbon dioxide comes from the limestone itself.",
                  "So changing the fuel that heats the kiln cannot stop it."]},
        {"kind": "card", "title": "Testing for gases",
         "body": [{"figure": "c5-gas-tests"},
                  "Each test shows that one gas is there."]},
        {"kind": "reveal", "title": "The three gas tests",
         "cols": ["Test", "Positive result"],
         "rows": [
             ("Oxygen", "Put a glowing splint into the gas", "The splint relights"),
             ("Hydrogen", "Hold a lit splint at the mouth of the tube", "A squeaky pop"),
             ("Carbon dioxide", "Bubble the gas through limewater",
              "The limewater turns from clear to milky"),
         ]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The powder went black, so it burnt.",
              "Nothing burnt. The black solid is copper oxide, made with no oxygen from the air.",
              "REACT-12"),
             ("When the tube cools, the copper oxide turns back into copper carbonate.",
              "The copper oxide stays black. The carbon dioxide has gone, so the change does not reverse.",
              "REACT-13"),
             ("A gas that puts out a lit splint is carbon dioxide.",
              "Many gases put out a splint. Limewater turning milky is the test for carbon dioxide."),
             ("The squeaky pop test uses a glowing splint.",
              "The squeaky pop test uses a lit splint. A glowing splint is the oxygen test."),
         ]}]},
    ],
    "key_fact": "Thermal decomposition uses heat to break one compound into two or more substances. "
                "Heating a metal carbonate gives a metal oxide and carbon dioxide.",
    "deeper": [
        {"kind": "card", "title": "Baking soda and cakes",
         "body": ["Baking soda is sodium hydrogencarbonate.",
                  "It breaks down in a hot oven and gives off carbon dioxide.",
                  "The gas makes bubbles in the mixture, so the cake rises."]},
        {"kind": "card", "title": "Not every carbonate breaks down",
         "body": ["Sodium carbonate and potassium carbonate do not break down in a Bunsen flame.",
                  "Calcium carbonate needs a very hot flame for a long time.",
                  "Copper carbonate breaks down easily, so it is used in school."]},
    ],
    "try": None,
    "tutor_body": "Still not sure why nothing burnt in the tube?",
    "safety_note": "Wear eye protection. Take the delivery tube out of the limewater before you "
                   "stop heating. If you do not, cold limewater is sucked back and the hot tube "
                   "can crack.",
    "ks4_becomes": "Endothermic reactions and reaction profiles, and the tests for gases.",
    "figures": [
        {"id": "c5-heating-carbonate", "kind": "diagram", "status": "drawn",
         "art": "c5-heating-carbonate",
         "title": "Heating copper carbonate and testing the gas",
         "desc": "On the left, a boiling tube holds green copper carbonate powder at the bottom. "
                 "A Bunsen burner flame heats it from below. A bung closes the tube. A delivery "
                 "tube runs up from the bung, across, and down into a tube of limewater on the "
                 "right. The end of the delivery tube is under the surface, bubbles rise from it, "
                 "and the limewater is milky. Below, labelled The result: a tube of green copper "
                 "carbonate marked before, an arrow, and a tube of black copper oxide marked after.",
         "caption": "The gas turns limewater milky, so it is carbon dioxide.",
         "data": {
             "colours": {"powder": "#4E9A6B", "oxide": "#2A2623", "milky": "#ECE8DF"},
             "labels": {"bung": "bung", "delivery": "delivery tube",
                        "powder": ["copper", "carbonate"], "heat": "heat",
                        "limewater": ["limewater", "turns milky"],
                        "result": "The result",
                        "before": ["before:", "green"], "after": ["after:", "black"]},
         }},
        {"id": "c5-word-carbonate-heat", "kind": "diagram", "status": "drawn", "art": "c4-word-row",
         "title": "The general equation for heating a metal carbonate",
         "desc": "Written left to right. On the left, under the tag Reactant: metal carbonate. "
                 "In the middle, a drawn arrow pointing right, with the word heat written above "
                 "it. On the right, under the tag Products: metal oxide, then a plus sign, then "
                 "carbon dioxide.",
         "caption": "One reactant breaks down into two products. Heating goes on all the time.",
         "data": {"left": ["metal carbonate"], "right": ["metal oxide", "carbon dioxide"],
                  "over": "heat"}},
        {"id": "c5-gas-tests", "kind": "diagram", "status": "drawn", "art": "c5-gas-tests",
         "title": "The tests for oxygen, hydrogen and carbon dioxide",
         "desc": "Three rows. Oxygen: a glowing splint is pushed into an upright tube of the gas, "
                 "and its tip bursts into flame. Hydrogen: a lit splint is held at the mouth of "
                 "an upside down tube of the gas, and short lines burst from the mouth for the "
                 "squeaky pop. Carbon dioxide: the gas bubbles from a delivery tube into "
                 "limewater, which is milky.",
         "caption": "Oxygen relights a glowing splint. Hydrogen pops. Carbon dioxide turns "
                    "limewater milky.",
         "data": {
             "colours": {"milky": "#ECE8DF"},
             "rows": [
                 {"title": "Oxygen", "label": "oxygen",
                  "lines": ["Put a glowing splint", "into the gas.", "It relights."]},
                 {"title": "Hydrogen", "label": "hydrogen",
                  "lines": ["Hold a lit splint at", "the tube's mouth.", "A squeaky pop."]},
                 {"title": "Carbon dioxide", "label": "limewater",
                  "lines": ["Bubble the gas", "through limewater.", "It turns milky."]},
             ]}},
    ],
    "ladder_stem": {
        "explain": "A student heats copper carbonate. They say it went black because it burnt. "
                   "Give two pieces of evidence that show they are wrong. Say what the black "
                   "solid is.",
        "produce": "Cement is made by heating limestone in a kiln. Explain why this gives off "
                   "carbon dioxide, even if the kiln is heated using electricity from wind "
                   "turbines. Explain why that makes the emissions hard to remove.",
    },
    "ladder_ticks": [
        ["Suggests what would be needed instead — capturing the gas, or a different material "
         "altogether.",
         "Suggests what could be done instead, such as capturing the gas or using a different "
         "material."],
    ],
    "ladder_feedback": {
        "recall": {
            0: "Joining substances is the opposite. Thermal decomposition breaks one compound down.",
            1: "That is melting, a physical change. No new substance is made.",
            2: "That is oxidation. Thermal decomposition needs no oxygen at all.",
        },
        "apply": {
            0: "No oxygen from the air joins in. The solid gets lighter as carbon dioxide escapes.",
            2: "Mass is conserved, but the carbon dioxide has left the tube. The balance cannot weigh it.",
            3: "No mass is destroyed. It left the tube as carbon dioxide gas.",
        },
    },
}
