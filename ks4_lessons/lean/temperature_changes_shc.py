# -*- coding: utf-8 -*-
"""Temperature changes and specific heat capacity, in the lean shape. Spec table:
ks4-temperature-changes-shc.md (AQA 8464 6.3.2.2 / 8463 4.3.2.2, word for word the same). No
HT-only or physics-only line. AQA puts the specific heat capacity practical under Energy changes in
systems (8464 6.1.1.3, Required practical activity 14; 8463 4.1.1.3, Required practical activity 1)
and says the equation and specific heat capacity "are also included" there. The Rainford scheme of
work teaches the practical in this lesson ("Specific heat capacity RP"), so the card is here, with
each spec's own number; energy-changes-in-systems carries the same practical.

LEGACY (batch 3, Ks4Ladder). The ladder (r1..r4), the worked examples and Your turn questions
(cfExamples / cfQuestions, placed by the `cfifa` slot) and the practice set stay from the Design
page. The page's own header chip, "Required practical {{ rpNum }}", already reads 14 on Combined and
1 on Triple, and its eyebrow is route-aware (8464 6.3.2.2 / 8463 4.3.2.2), so neither is edited.
The practice set reads the route's `quiz` list (K.bank): five per route, both old stems kept word
for word.

ΔE = m c Δθ is on the Physics equation sheet (8463 Appendix, sheet equation 5). E = P t is a
recall equation (8463 Appendix, recall equation 21); the Design page's "On the sheet" chip on E = P t
was wrong, and that equation box is not on the lean page."""

_RP_BODY = [
    "An investigation to determine the specific heat capacity of one or more materials.",
    {"points": [
        "Measure the mass of a metal block on a balance.",
        "Put an electric heater and a thermometer in the holes in the block. Wrap the block in "
        "insulation.",
        "Record the starting temperature. Switch on the heater for a set time, for example 10 "
        "minutes.",
        "Record the energy supplied, from a joulemeter or from E = P t. Record the highest "
        "temperature the block reaches.",
        "Work out Δθ, then c = ΔE ÷ (m × Δθ).",
    ]},
    "Some energy is dissipated to the surroundings, so the temperature rise is smaller than it "
    "should be and the value of c comes out too high. The insulation reduces this.",
    "The heater and the block get hot enough to burn. Let them cool before you touch them.",
]

LESSON = {
    "slug": "temperature-changes-shc",
    "start": {
        "setup": "1 kg of dry sand and 1 kg of seawater get the same energy from the Sun.",
        "question": "If you had to guess, which one warms up more?",
        "options": [
            ("The sand",
             "The sand. Water needs far more energy to raise the temperature of each kilogram by "
             "1 °C, so the same energy warms it much less."),
            ("The seawater",
             "The sand. Water needs far more energy to raise the temperature of each kilogram by "
             "1 °C, so the same energy warms it much less."),
        ],
        "answer": 0,
    },
    "words": ["specific heat capacity", "temperature change", "thermal energy"],
    "knowledge": [
        {"kind": "card", "title": "What decides the temperature rise",
         "body": ["If the temperature of a system increases, the increase depends on:",
                  {"points": ["the mass of the substance heated",
                              "the type of material",
                              "the energy input to the system."]},
                  "The same energy gives a smaller rise in a bigger mass, or in a material with a "
                  "higher specific heat capacity."]},
        {"kind": "card", "title": "Specific heat capacity",
         "body": ["The specific heat capacity of a substance is the amount of energy required to "
                  "raise the temperature of one kilogram of the substance by one degree Celsius.",
                  "Water's is 4200 J/kg °C. Aluminium's is 900 J/kg °C. So 1 kg of water needs "
                  "more than four times as much energy as 1 kg of aluminium to warm by 1 °C."]},
        {"kind": "card", "title": "The equation",
         "body": ["change in thermal energy = mass × specific heat capacity × temperature change",
                  "ΔE = m c Δθ",
                  {"points": ["change in thermal energy, ΔE, in joules (J)",
                              "mass, m, in kilograms (kg)",
                              "specific heat capacity, c, in joules per kilogram per degree "
                              "Celsius (J/kg °C)",
                              "temperature change, Δθ, in degrees Celsius (°C)"]},
                  "This equation is on the Physics equation sheet. You need to be able to use it "
                  "and rearrange it.",
                  {"slot": "triangle:EQ_SHC"}]},
        {"kind": "card", "title": "The temperature change",
         "body": ["Δθ is a change: the final temperature minus the starting temperature.",
                  "When something cools, Δθ is the size of the drop. Water cooling from 80 °C to "
                  "30 °C has Δθ = 50 °C."]},
        {"kind": "card", "title": "Energy from a heater",
         "body": ["The energy from an electric heater is measured with a joulemeter, or worked out "
                  "from energy transferred = power × time, E = P t, with P in watts and t in "
                  "seconds.",
                  "You need to remember E = P t: it is not on the equation sheet."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Required practical 14: specific heat capacity",
         "routes": ["CF", "CH"], "body": _RP_BODY},
        {"kind": "card", "title": "Required practical 1: specific heat capacity",
         "routes": ["TF", "TH"], "body": _RP_BODY},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Using the final temperature as Δθ.",
              "Δθ is the change: the final temperature minus the starting temperature."),
             ("Putting a mass in grams into the equation.",
              "Convert it to kilograms first: divide by 1000."),
             ("A high specific heat capacity means a substance heats up quickly.",
              "It needs more energy for each degree, so the same energy warms it less."),
         ]}]},
    ],
    "key_fact": "The specific heat capacity of a substance is the energy needed to raise the "
                "temperature of 1 kg of it by 1 °C. Change in thermal energy = mass × specific "
                "heat capacity × temperature change: ΔE = m c Δθ.",
    "deeper": [
        {"kind": "card", "title": "Why water is used for heating and cooling",
         "body": ["Water has a high specific heat capacity, so each kilogram carries a lot of "
                  "energy for each degree its temperature changes. That is why water is used in "
                  "central heating radiators and to cool car engines."]},
        {"kind": "card", "title": "Links to other lessons",
         "body": [{"points": [
             "Energy changes in systems: the same equation and the same practical.",
             "Specific latent heat: the energy for a change of state, when the temperature does "
             "not change.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Define</strong>: give the exact meaning. For c: energy, 1 kg and 1 °C.",
             "<strong>Calculate</strong>: convert, write the equation, put the numbers in, "
             "rearrange, then give the answer with its unit.",
             "<strong>Describe a method</strong>: the equipment, what you measure and how, in "
             "order, and how you work out c.",
             "<strong>Explain</strong>: link cause to effect, for example where the energy went "
             "and what that did to Δθ and to c.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3"},
    "equations": {
        "EQ_SHC": {"name": "Specific heat capacity",
                   "written": "change in thermal energy = mass × specific heat capacity × "
                              "temperature change",
                   "source": "none",
                   "top": {"s": "ΔE", "name": "change in thermal energy", "unit": "J"},
                   "bottom": [{"s": "m", "name": "mass", "unit": "kg"},
                              {"s": "c", "name": "specific heat capacity", "unit": "J/kg °C"},
                              {"s": "Δθ", "name": "temperature change", "unit": "°C"}]},
    },
}
