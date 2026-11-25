# -*- coding: utf-8 -*-
"""Charging by rubbing, in the lean shape. Spec table: docs/lessons/wave2/ks3-charging-by-rubbing.md."""

LESSON = {
    "slug": "charging-by-rubbing",
    "start": {
        "setup": "A polythene rod is rubbed with a woollen duster. The rod ends up negatively charged.",
        "question": "If you had to guess, what charge does the duster have now?",
        "options": [
            ("Still neutral",
             "It is positive. The rod's extra electrons came off the duster."),
            ("Positive",
             "Yes. The duster lost the electrons the rod gained, so it is positive."),
        ],
        "answer": 1,
    },
    "words": ["electron", "neutral", "charge", "insulator"],
    "word_defs": {
        "electron": "A tiny particle with a negative charge. Electrons are on the outside of every atom.",
        "neutral": "Having no overall charge. The positive and negative charges are equal.",
        "charge": "Protons and electrons carry charge. An object is charged when it gains or loses electrons.",
        "insulator": "A material that charge cannot flow through, such as plastic, wool or glass.",
    },
    "knowledge": [
        {"kind": "card", "title": "Two types of charge",
         "body": ["There are two types of charge: positive and negative.",
                  "Every atom has protons in its nucleus. Protons have a positive charge.",
                  "Electrons are around the outside of the atom. Electrons have a negative charge.",
                  "Most objects have equal numbers of protons and electrons.",
                  "The charges cancel out, so the object is neutral."]},
        {"kind": "card", "title": "Charging by rubbing",
         "body": [{"figure": "p9-rub-rod-duster"},
                  "Rubbing two insulators together moves electrons from one to the other.",
                  "Only electrons move. Protons are held in the nucleus and cannot move.",
                  "The object that gains electrons has more electrons than protons.",
                  "So it becomes negatively charged.",
                  "The object that loses electrons has fewer electrons than protons.",
                  "So it becomes positively charged."]},
        {"kind": "reveal", "title": "Gaining and losing electrons",
         "cols": ["Gains electrons", "Loses electrons"],
         "rows": [
             ("Charge it ends up with", "Negative", "Positive"),
             ("Electrons and protons", "More electrons than protons", "Fewer electrons than protons"),
             ("Polythene rod and wool duster", "The polythene rod", "The wool duster"),
             ("Acetate strip and cloth", "The cloth", "The acetate strip"),
             ("Balloon and your hair", "The balloon", "Your hair"),
         ]},
        {"kind": "card", "title": "No charge is made",
         "body": ["Rubbing does not make charge. It only moves electrons.",
                  "Every electron the rod gains comes off the duster.",
                  "So the rod and the duster get equal and opposite charges.",
                  "Add the two charges together and the total is still zero."]},
        {"kind": "card", "title": "Which way the electrons go",
         "body": ["Some materials hold on to their electrons more tightly than others.",
                  "When two are rubbed, the one that holds electrons more tightly gains them.",
                  "So the same material can end up positive or negative.",
                  "A cloth gives electrons to polythene, so the cloth becomes positive.",
                  "A cloth takes electrons from acetate, so the cloth becomes negative."]},
        {"kind": "card", "title": "Why only insulators stay charged",
         "body": ["In an insulator, electrons cannot flow. They stay where they were rubbed on or off.",
                  "A metal is a conductor. Electrons flow through it easily.",
                  "Rub a metal rod held in your hand, and charge flows through you.",
                  "So the metal rod does not stay charged."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Rubbing makes new charge.",
              "Rubbing only moves electrons from one object to the other.", "CHRG-01"),
             ("A positive object has gained positive charge.",
              "A positive object has lost electrons. Protons never move.", "CHRG-02"),
             ("Only the rubbed rod becomes charged.",
              "Both objects become charged, with equal and opposite charges.", "CHRG-03"),
             ("A material always gets the same charge, whatever rubs it.",
              "It depends on the pair. A cloth can end up positive or negative.", "CHRG-04"),
             ("A metal rod held in your hand stays charged after rubbing.",
              "Charge flows through your hand, so the rod does not stay charged."),
         ]}]},
    ],
    "key_fact": "There are two types of charge, positive and negative. "
                "Rubbing two insulators moves electrons from one to the other. "
                "The object that gains electrons becomes negative. "
                "The object that loses electrons becomes positive, by the same amount.",
    "deeper": [
        {"kind": "card", "title": "Static at home",
         "body": ["Clothes from a tumble dryer rub together, so they cling.",
                  "Walk across a nylon carpet and you can pick up a charge.",
                  "Touch a metal door handle, and the charge jumps across as a small spark."]},
        {"kind": "card", "title": "Fuel and sparks",
         "body": ["Fuel flowing through a pipe rubs against it, so charge builds up.",
                  "A spark near fuel vapour could start a fire.",
                  "So a fuel tanker is joined to the ground by a metal wire first.",
                  "The charge flows away through the wire instead of building up.",
                  "This is called earthing."]},
    ],
    "try": None,
    "tutor_body": "Got two materials and want to know which one ends up negative?",
    "ks4_becomes": "Sparks, earthing, and the uses and dangers of static charge.",
    "figures": [
        {"id": "p9-rub-rod-duster", "kind": "diagram", "status": "drawn", "art": "p9-rub",
         "title": "A polythene rod and a wool duster, before and after rubbing",
         "desc": "Two rows. Before rubbing, a polythene rod and a wool duster each hold four plus signs "
                 "for protons and four minus signs for electrons, and each is labelled neutral. "
                 "After rubbing, an arrow labelled electrons move points from the duster to the rod. "
                 "The rod now holds four plus signs and six minus signs and is labelled negative. "
                 "The duster holds four plus signs and two minus signs and is labelled positive.",
         "caption": "Two electrons move from the duster to the rod. The protons stay where they are.",
         "data": {"rod": "polythene rod", "cloth": "wool duster", "protons": 4,
                  "panels": [{"title": "Before rubbing", "rod": 4, "cloth": 4},
                             {"title": "After rubbing", "rod": 6, "cloth": 2,
                              "arrow": "electrons move"}]}},
    ],
    "ladder_stem": {
        "explain": "A polythene rod is rubbed with a woollen duster. The rod ends up negatively charged. "
                   "Explain what has happened. Name what moves and what does not. "
                   "Say what charge the duster has now.",
        "produce": "A fuel tanker is joined to a metal spike in the ground before any fuel is pumped. "
                   "Pumping stops if the wire comes off. Explain what this prevents. "
                   "Explain why doing the same to a plastic bottle of water would be pointless.",
    },
    "ladder_feedback": {
        "recall": {
            1: "That is the wrong way round. Glass holds electrons less tightly, so glass loses them.",
            2: "Protons never move. The glass is positive because electrons have left it.",
            3: "Both objects become charged. The electrons the glass loses land on the wool.",
        },
        "apply": {
            0: "Friction does not make charge. The balloon's extra electrons came off the jumper.",
            1: "No charge was made, but the two charges are opposite. The jumper is positive.",
            3: "Nothing was made. The jumper is positive because it lost electrons to the balloon.",
        },
    },
}
