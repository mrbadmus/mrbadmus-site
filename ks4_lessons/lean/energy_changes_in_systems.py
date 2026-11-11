# -*- coding: utf-8 -*-
"""Energy changes in systems (specific heat capacity), in the lean shape. Rebuilt from the old format.
Spec table: docs/lessons/pilot/ks4-energy-changes-in-systems.md.

The required practical has a different number on each spec: 14 in 8464 (Combined), 1 in 8463 (Triple)."""

_RP_STEPS = [
    "Measure the mass of the block.",
    "Put a heater and a thermometer in the block and wrap it in insulation.",
    "Record the starting temperature.",
    "Switch on the heater and measure the energy transferred.",
    "Record the final temperature and work out the temperature change.",
    "Use c = ΔE ÷ (m × Δθ) to find the specific heat capacity.",
]
_RP_ERROR = ("Some energy is dissipated to the surroundings. This makes the measured value higher "
             "than the true value. Insulating the block reduces this.")

LESSON = {
    "slug": "energy-changes-in-systems",
    "start": {
        "setup": "You heat the same mass of water and of aluminium with the same heater.",
        "question": "If you had to guess, which one warms up faster?",
        "options": [
            ("The water",
             "The aluminium. Water needs more energy to raise its temperature by the same amount."),
            ("The aluminium",
             "The aluminium. Water needs more energy to raise its temperature by the same amount."),
        ],
        "answer": 1,
    },
    "words": ["specific heat capacity", "thermal energy", "temperature change"],
    "knowledge": [
        {"kind": "card", "title": "What specific heat capacity means",
         "body": ["The specific heat capacity of a substance is the amount of energy required to "
                  "raise the temperature of one kilogram of the substance by one degree Celsius."]},
        {"kind": "card", "title": "The equation",
         "body": ["change in thermal energy = mass × specific heat capacity × temperature change",
                  "ΔE = m c Δθ",
                  {"points": ["change in thermal energy, ΔE, in joules (J)",
                              "mass, m, in kilograms (kg)",
                              "specific heat capacity, c, in joules per kilogram per degree "
                              "Celsius (J/kg °C)",
                              "temperature change, Δθ, in degrees Celsius (°C)"]},
                  "This equation is on the equation sheet.",
                  {"slot": "triangle:EQ_SHC"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Required practical 14: specific heat capacity",
         "routes": ["CF", "CH"],
         "body": [{"points": _RP_STEPS}, _RP_ERROR]},
        {"kind": "card", "title": "Required practical 1: specific heat capacity",
         "routes": ["TF", "TH"],
         "body": [{"points": _RP_STEPS}, _RP_ERROR]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Using the final temperature as Δθ.",
              "Δθ is final temperature minus starting temperature."),
             ("Putting a mass in grams into the equation.",
              "Convert to kilograms first. Divide by 1000."),
         ]}]},
    ],
    "key_fact": "The specific heat capacity of a substance is the energy required to raise the "
                "temperature of 1 kg of it by 1 °C. Change in thermal energy = mass × specific "
                "heat capacity × temperature change.",
    "deeper": [
        {"kind": "card", "title": "Why water is used in radiators",
         "body": ["Water has a high specific heat capacity of 4200 J/kg °C.",
                  "Each kilogram carries a lot of energy for each degree it cools."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: work out a number and show each line.",
             "<strong>Describe</strong>: give the steps of a method in order.",
             "<strong>Explain</strong>: say what happens and why.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_SHC": {"name": "Specific heat capacity",
                   "written": "change in thermal energy = mass × specific heat capacity × temperature change",
                   "source": "none",
                   "top": {"s": "ΔE", "name": "change in thermal energy", "unit": "J"},
                   "bottom": [{"s": "m", "name": "mass", "unit": "kg"},
                              {"s": "c", "name": "specific heat capacity", "unit": "J/kg °C"},
                              {"s": "Δθ", "name": "temperature change", "unit": "°C"}]},
    },
    "cfifa": {
        "examples": [
            {"tab": "Nothing to convert", "eq": "EQ_SHC", "find": "ΔE",
             "head": "Calculate the energy needed to heat 2 kg of water from 20 °C to 100 °C. The specific heat capacity of water is 4200 J/kg °C.",
             "steps": [["C", "Convert", "Nothing to convert. Δθ = 100 − 20 = 80 °C"],
                       ["F", "Formula", "ΔE = m c Δθ"],
                       ["I", "Insert", "ΔE = 2 × 4200 × 80"],
                       ["F", "Fine-tune", "ΔE = 672 000"],
                       ["A", "Answer", "ΔE = 672 000 J"]]},
            {"tab": "Convert first", "eq": "EQ_SHC", "find": "ΔE",
             "head": "A 500 g aluminium block is heated by 40 °C. The specific heat capacity of aluminium is 900 J/kg °C. Calculate the energy transferred.",
             "steps": [["C", "Convert", "500 g ÷ 1000 = 0.5 kg"],
                       ["F", "Formula", "ΔE = m c Δθ"],
                       ["I", "Insert", "ΔE = 0.5 × 900 × 40"],
                       ["F", "Fine-tune", "ΔE = 18 000"],
                       ["A", "Answer", "ΔE = 18 000 J"]]},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1, "prompt": "Give the unit of specific heat capacity.",
             "why": "Specific heat capacity is energy per kilogram per degree Celsius.",
             "options": [
                 {"text": "J/kg °C", "correct": True},
                 {"text": "J/°C", "correct": False, "reply": "This leaves out the mass."},
                 {"text": "J/kg", "correct": False, "reply": "This leaves out the temperature change."},
                 {"text": "W/kg °C", "correct": False, "reply": "Watts measure power. It is an amount of energy."},
             ]},
            {"kind": "mcq", "command": "Define", "marks": 1, "prompt": "Define specific heat capacity.",
             "why": "It is the energy required to raise the temperature of one kilogram of the substance by one degree Celsius.",
             "options": [
                 {"text": "The energy stored in a substance at room temperature", "correct": False, "reply": "It is about the energy needed for a temperature rise."},
                 {"text": "The temperature a substance reaches when it is heated", "correct": False, "reply": "It is an amount of energy, not a temperature."},
                 {"text": "The energy required to raise the temperature of 1 kg of a substance by 1 °C", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "Calculate the energy needed to raise the temperature of 2.0 kg of water by 30 °C. The specific heat capacity of water is 4200 J/kg °C.",
             "convOptions": ["Nothing to convert", "Convert kg to g: multiply by 1000", "Convert °C to kelvin"],
             "convAnswer": 0, "answer": 252000, "tol": 1, "unit": "J", "units": ["J", "kJ", "W", "no unit"],
             "right": "2.0 × 4200 × 30 = 252 000 J.",
             "wrong": "Nothing to convert. ΔE = m c Δθ = 2.0 × 4200 × 30 = 252 000 J.",
             "model": ["C · Nothing to convert", "F · ΔE = m c Δθ", "I · ΔE = 2.0 × 4200 × 30", "F · ΔE = 252 000", "A · 252 000 J"]},
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "A 500 g block of aluminium is heated from 20 °C to 70 °C. The specific heat capacity of aluminium is 900 J/kg °C. Calculate the energy transferred.",
             "convOptions": ["Nothing to convert", "Convert g to kg: divide by 1000", "Convert g to kg: multiply by 1000"],
             "convAnswer": 1, "answer": 22500, "tol": 1, "unit": "J", "units": ["J", "kJ", "W", "no unit"],
             "right": "0.5 × 900 × 50 = 22 500 J.",
             "wrong": "500 g ÷ 1000 = 0.5 kg. Δθ = 70 − 20 = 50 °C. ΔE = 0.5 × 900 × 50.",
             "model": ["C · 500 g ÷ 1000 = 0.5 kg", "F · ΔE = m c Δθ", "I · ΔE = 0.5 × 900 × 50", "F · ΔE = 22 500", "A · 22 500 J"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "A student measures the specific heat capacity of a metal block. Their value is higher than the true value. Explain why. Put the links in order.",
             "links": ["Some energy from the heater is dissipated to the surroundings.",
                       "So the temperature of the block rises by less than it should.",
                       "c = ΔE ÷ (m × Δθ), so a smaller Δθ gives a larger value of c."],
             "herrings": [{"text": "The block gained extra energy from the air.", "why": "The block is hotter than the air, so energy moves out of it."},
                          {"text": "The student used too much mass.", "why": "The mass is measured and used in the equation."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "The same heater warms equal masses of water and aluminium. Explain why the water takes longer to warm by 10 °C. Put the links in order.",
             "links": ["Water has a higher specific heat capacity than aluminium.",
                       "So more energy is required to raise the temperature of each kilogram of water by 1 °C.",
                       "The heater transfers energy at the same rate, so the water takes longer."],
             "herrings": [{"text": "Water is a liquid, so it cannot warm up quickly.", "why": "The state is not the reason. Specific heat capacity is."},
                          {"text": "The aluminium has less mass.", "why": "The masses are equal in the question."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 6,
             "prompt": "Describe a method to find the specific heat capacity of a metal block using an electric heater.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "A clear, logical method: measurements, how energy is found, and how c is calculated.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Most steps present, with some missing detail.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant steps.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["Measure the mass of the block with a balance.",
                        "Insulate the block and put a heater and thermometer in it.",
                        "Record the starting temperature, then heat for a measured time.",
                        "Measure the energy transferred, for example with a joulemeter.",
                        "Record the final temperature and calculate the temperature change.",
                        "Calculate c = ΔE ÷ (m × Δθ)."],
             "reject": ["“Heat the block until it is hot.”", "“Measure the temperature of the room.”"]},
        ],
    },
}
