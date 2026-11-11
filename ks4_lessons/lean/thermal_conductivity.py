# -*- coding: utf-8 -*-
"""Thermal conductivity, in the lean shape. Spec table: docs/lessons/pilot/ks4-thermal-conductivity.md.

Combined pages use 8464 6.1.2.1. Triple pages use 8463 4.1.2.1, which adds Required practical 2."""

LESSON = {
    "slug": "thermal-conductivity",
    "start": {
        "setup": "A metal spoon and a wooden spoon are put into the same pan of hot soup.",
        "question": "If you had to guess, which handle gets hot first?",
        "options": [
            ("The metal spoon", "The metal spoon. Metal has a higher thermal conductivity, so energy is conducted up it faster."),
            ("The wooden spoon", "The metal spoon. Metal has a higher thermal conductivity, so energy is conducted up it faster."),
        ],
        "answer": 0,
    },
    "words": ["thermal conductivity", "conduction", "thermal insulator", "rate of cooling"],
    "knowledge": [
        {"kind": "card", "title": "Thermal conductivity",
         "body": ["The higher the thermal conductivity of a material, the higher the rate of "
                  "energy transfer by conduction across the material.",
                  "Metals have a high thermal conductivity.",
                  "Wood, plastic, wool and air have a low thermal conductivity. They make good "
                  "thermal insulators."]},
        {"kind": "reveal", "title": "How fast a building cools",
         "cols": ["Cools more slowly", "Cools more quickly"],
         "rows": [
             ("Wall thickness", "Thicker walls", "Thinner walls"),
             ("Thermal conductivity of the walls", "Lower", "Higher"),
         ]},
        {"kind": "card", "title": "Reducing unwanted energy transfers",
         "body": [{"points": [
             "<strong>Lubrication</strong>: oil reduces friction between moving parts, so less "
             "energy is dissipated.",
             "<strong>Loft insulation</strong>: a thick layer of fibreglass slows energy transfer "
             "through the roof.",
             "<strong>Cavity wall insulation</strong>: foam traps air in small pockets. Trapped "
             "air is a very poor conductor.",
             "<strong>Double glazing</strong>: a layer of air or gas between two panes conducts "
             "far less than glass alone.",
         ]}]},
        {"kind": "card", "title": "Required practical 2: thermal insulators", "routes": ["TF", "TH"],
         "body": [{"slot": "rp-fig"},
                  {"points": [
                      "Put a small beaker inside a larger one.",
                      "Pack the gap with one insulating material.",
                      "Pour the same volume of hot water into the small beaker.",
                      "Fit a lid with a hole for the thermometer.",
                      "Record the temperature at the start and every few minutes.",
                      "Repeat with each material, starting at the same temperature.",
                      "To test thickness, change the number of layers of one material and keep "
                      "everything else the same.",
                  ]},
                  "The smaller the temperature drop in the same time, the better the insulator."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("The metal bench is at a lower temperature than the wooden bench.",
              "They are at the same temperature. Metal transfers energy from your hand faster."),
             ("Insulation stops energy transfer.",
              "Insulation slows energy transfer. It does not stop it."),
         ]}]},
    ],
    "key_fact": "The higher the thermal conductivity of a material, the higher the rate of energy "
                "transfer by conduction across it. A building cools more slowly if its walls are "
                "thicker and have a lower thermal conductivity.",
    "deeper": [
        {"kind": "card", "title": "Why metals conduct well",
         "body": ["Metals have free electrons. These carry energy through the metal quickly.",
                  {"slot": "particle-fig"}]},
        {"kind": "card", "title": "Why trapped air insulates",
         "body": ["Air particles are far apart, so energy is passed on slowly.",
                  "Trapped in small pockets, air also cannot form convection currents."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say how the rate of cooling changes with thickness and "
             "with conductivity.",
             "<strong>Explain</strong>: give the property of the material, then the rate of "
             "energy transfer, then the result.",
             "<strong>Suggest</strong>: apply the idea to something new, such as a flask or a "
             "cool bag.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-4"},
}
