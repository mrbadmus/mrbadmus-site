# -*- coding: utf-8 -*-
"""Energy transfers in a system, in the lean shape. Rebuilt from the old format.
Spec table: docs/lessons/pilot/ks4-energy-transfers-in-a-system.md."""

LESSON = {
    "slug": "energy-transfers-in-a-system",
    "start": {
        "setup": "A bouncing ball rises a little less after each bounce.",
        "question": "If you had to guess, where does the energy go?",
        "options": [
            ("It is destroyed",
             "Into the surroundings. It is dissipated, so it is stored in less useful ways."),
            ("Into the surroundings",
             "Into the surroundings. It is dissipated, so it is stored in less useful ways."),
        ],
        "answer": 1,
    },
    "words": ["conservation of energy", "closed system", "dissipated", "wasted"],
    "knowledge": [
        {"kind": "card", "title": "Conservation of energy",
         "body": ["Energy can be transferred usefully, stored or dissipated, but cannot be "
                  "created or destroyed."]},
        {"kind": "card", "title": "Closed systems",
         "body": ["In a closed system, there is no net change to the total energy.",
                  "Energy moves between stores, but the total stays the same.",
                  "For example, a swinging pendulum with no air resistance moves energy between "
                  "its kinetic and gravitational potential stores. The total stays the same."]},
        {"kind": "card", "title": "Dissipation",
         "body": ["In all system changes, energy is dissipated, so that it is stored in less "
                  "useful ways.",
                  "This energy is often described as wasted."]},
        {"kind": "reveal", "title": "Useful and wasted energy",
         "cols": ["Useful", "Wasted"],
         "rows": [
             ("Car engine", "Kinetic store of the car", "Thermal stores of the engine and surroundings"),
             ("Filament lamp", "Light", "Heating the surroundings"),
             ("Phone charging", "Chemical store of the battery", "Thermal store of the phone"),
             ("Electric kettle", "Thermal store of the water", "Thermal stores of the kettle and surroundings"),
         ]},
        {"kind": "card", "title": "Reducing unwanted energy transfers",
         "body": [{"points": [
             "<strong>Lubrication</strong>: oil reduces friction between moving parts, so less "
             "energy is dissipated.",
             "<strong>Thermal insulation</strong>: reduces the energy transferred to the "
             "surroundings.",
         ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Energy gets used up.",
              "Energy is transferred or dissipated. It cannot be destroyed."),
             ("Wasted energy has disappeared.",
              "It is still there, stored in less useful ways in the surroundings."),
         ]}]},
    ],
    "key_fact": "Energy can be transferred usefully, stored or dissipated, but cannot be created "
                "or destroyed. Dissipated energy is stored in less useful ways and is often "
                "described as wasted.",
    "deeper": [
        {"kind": "card", "title": "A bouncing ball",
         "body": ["Each bounce transfers some energy to the thermal stores of the ball and the "
                  "ground.",
                  "So each bounce leaves less energy for the next one."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Describe</strong>: say what happens, with an example.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State what happens to the total energy in a closed system.",
             "why": "In a closed system there is no net change to the total energy.",
             "options": [
                 {"text": "It decreases over time", "correct": False, "reply": "Energy cannot be destroyed, so the total does not fall."},
                 {"text": "It increases when the system is heated", "correct": False, "reply": "A closed system has no energy entering or leaving."},
                 {"text": "There is no net change", "correct": True},
             ]},
            {"kind": "mcq", "command": "Complete", "marks": 1,
             "prompt": "Energy that is dissipated is…",
             "why": "Dissipated energy is stored in less useful ways.",
             "options": [
                 {"text": "stored in less useful ways", "correct": True},
                 {"text": "destroyed", "correct": False, "reply": "Energy cannot be destroyed."},
                 {"text": "returned to the original store", "correct": False, "reply": "It spreads out and is hard to use again."},
                 {"text": "turned into a force", "correct": False, "reply": "Energy is not turned into a force."},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give one way of reducing unwanted energy transfers in a bicycle.",
             "why": "Lubrication reduces friction between the moving parts.",
             "options": [
                 {"text": "Pump more air into the saddle", "correct": False, "reply": "This does not reduce friction between moving parts."},
                 {"text": "Lubricate the chain", "correct": True},
                 {"text": "Paint the frame", "correct": False, "reply": "Paint does not change the friction in the moving parts."},
             ]},
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "A kettle is supplied with 300 kJ. The thermal store of the water gains 270 kJ. Calculate the energy dissipated to the surroundings, in joules.",
             "convOptions": ["Nothing to convert", "Convert kJ to J: multiply by 1000", "Convert kJ to J: divide by 1000"],
             "convAnswer": 1, "answer": 30000, "tol": 1, "unit": "J", "units": ["J", "kJ", "W", "no unit"],
             "right": "300 − 270 = 30 kJ = 30 000 J.",
             "wrong": "300 − 270 = 30 kJ. Multiply by 1000 to get 30 000 J.",
             "model": ["C · kJ × 1000 = J", "F · energy dissipated = energy supplied − useful energy", "I · energy dissipated = 300 000 − 270 000", "F · energy dissipated = 30 000", "A · 30 000 J"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a bouncing ball does not return to its starting height. Put the links in order.",
             "links": ["Each time the ball hits the ground, energy is transferred to the thermal stores of the ball and the ground.",
                       "This energy is dissipated to the surroundings and stored in less useful ways.",
                       "So less energy is in the ball's gravitational potential store at the top of each bounce."],
             "herrings": [{"text": "The energy is destroyed when the ball hits the ground.", "why": "Energy cannot be destroyed."},
                          {"text": "Gravity gets weaker with each bounce.", "why": "Gravitational field strength does not change."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how loft insulation reduces the energy a house transfers to the surroundings. Put the links in order.",
             "links": ["Loft insulation has a low thermal conductivity.",
                       "It reduces the rate of energy transfer by conduction through the roof.",
                       "So less energy is dissipated to the surroundings."],
             "herrings": [{"text": "Loft insulation adds energy to the house.", "why": "Insulation only slows the transfer."},
                          {"text": "Loft insulation destroys the heat.", "why": "Energy cannot be destroyed."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 4,
             "prompt": "A student says, “When a car brakes, its energy is lost.” Explain why this is not correct, and describe what happens to the energy.",
             "levels": [
                 {"label": "Level 2 · 3–4", "text": "States energy cannot be destroyed, and describes the transfer and dissipation.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One correct idea, such as energy cannot be destroyed.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Energy cannot be created or destroyed.",
                        "The kinetic store of the car decreases.",
                        "The thermal store of the brakes increases.",
                        "The energy is dissipated to the surroundings and stored in less useful ways."],
             "reject": ["“The energy disappears.”", "“The brakes use the energy up.”"]},
        ],
    },
}
