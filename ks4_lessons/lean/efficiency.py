# -*- coding: utf-8 -*-
"""Efficiency, in the lean shape. Spec table: docs/lessons/pilot/ks4-efficiency.md."""

LESSON = {
    "slug": "efficiency",
    "start": {
        "setup": "An old filament bulb and an LED light a room equally well.",
        "question": "If you had to guess, which one wastes more energy?",
        "options": [
            ("The LED",
             "The filament bulb. It gets hot, and that heat is energy you didn't want."),
            ("The filament bulb",
             "The filament bulb. It gets hot, and that heat is energy you didn't want."),
        ],
        "answer": 1,
    },
    "words": ["efficiency", "useful energy", "wasted energy", "dissipated"],
    "knowledge": [
        {"kind": "card", "title": "What efficiency means",
         "body": ["Efficiency is how much of the energy you put in is used for the job you want."]},
        {"kind": "card", "title": "Where wasted energy goes",
         "body": ["Wasted energy is not destroyed.",
                  "Most wasted energy is dissipated to the surroundings as heat, warming them "
                  "slightly. It is then stored in less useful ways."]},
        {"kind": "card", "title": "Sankey diagrams",
         "body": ["The width of each arrow shows the amount of energy.",
                  "Energy in = useful energy out + wasted energy out.",
                  {"slot": "sankey"}]},
        {"kind": "card", "title": "The equations",
         "body": ["efficiency = useful output energy transfer ÷ total input energy transfer",
                  "efficiency = useful power output ÷ total power input",
                  "Efficiency has no unit. It is always less than 1. Multiply by 100 to get a "
                  "percentage.",
                  {"slot": "triangle-energy"},
                  {"slot": "triangle-power"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Reducing waste",
         "body": ["Lubrication reduces friction, so less energy is dissipated.",
                  "Thermal insulation reduces the energy lost to the surroundings."]},
        {"kind": "card", "title": "Increasing efficiency", "routes": ["CH", "TH"],
         "body": ["For each way, say what is reduced and where that energy would have gone.",
                  {"points": [
                      "<strong>Lubricate</strong> moving parts: less friction, so less energy "
                      "is wasted as heat.",
                      "<strong>Streamline</strong> vehicles: less air resistance, so less energy "
                      "is transferred to the air.",
                      "<strong>Insulate</strong> hot objects: less energy is transferred to the "
                      "surroundings.",
                      "<strong>Use a better component</strong>: an LED transfers a bigger share "
                      "of its input to light than a filament lamp.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("efficiency = useful ÷ wasted", "Always divide by the total energy in."),
             ("An efficiency of 120%", "Nothing gives out more useful energy than goes in."),
             ("Wasted energy disappears", "It is dissipated to the surroundings."),
         ]}]},
    ],
    "key_fact": "Efficiency compares the useful energy out with the total energy in. Wasted "
                "energy is dissipated to the surroundings, mostly as heat, so no device is 100% "
                "efficient.",
    "deeper": [
        {"kind": "card", "title": "Work out the energy wasted",
         "body": ["Find the useful energy first. Then subtract it from the total.",
                  {"slot": "steps-worked"},
                  {"slot": "steps-attempt"}]},
        {"kind": "card", "title": "Regenerative braking", "routes": ["CH", "TH"],
         "body": ["A hybrid or electric car can store some of its kinetic energy in the battery "
                  "when it brakes. Less energy is wasted as heat in the brakes."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: work out a number and show each line.",
             "<strong>Describe</strong>: say what happens.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": {
        "batch": "batch-4",
        # The first worked example is Mide's. The other two stay as they were.
        "cfifa_first": {
            "tab": "Nothing to convert", "eq": "EQ_E", "find": "eff",
            "head": "A motor is supplied with 200 J and transfers 150 J usefully. Calculate its "
                    "efficiency.",
            "steps": [
                ["C", "Convert", "Nothing to convert: both are in joules."],
                ["F", "Formula", "efficiency = useful output energy transfer ÷ total input "
                                 "energy transfer"],
                ["I", "Insert", "efficiency = 150 ÷ 200"],
                ["F", "Fine-tune", "efficiency = 0.75"],
                ["A", "Answer", "efficiency = 0.75 (75%)"],
            ]},
    },
}
