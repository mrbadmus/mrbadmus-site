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
        "Record the starting temperature. Switch on the heater for a set time, for example "
        "10\u00a0minutes.",
        "Record the energy supplied, from a joulemeter or from E\u00a0=\u00a0P\u00a0t. Record the highest "
        "temperature the block reaches.",
        "Work out Δθ, then c\u00a0=\u00a0ΔE\u00a0÷\u00a0(m\u00a0×\u00a0Δθ).",
    ]},
    "Some energy is dissipated to the surroundings, so the temperature rise is smaller than it "
    "should be and the value of c comes out too high. The insulation reduces this.",
    "The heater and the block get hot enough to burn. Let them cool before you touch them.",
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): in the CH/TH Your turn, "27 000 J" wrapped as "27 / 000 J"
# (a no-break space inside the number now), and the answer placeholder was clipped to
# "final temperature = … wit" (shortened).
LOGIC_EDITS = [
    ("27 000", "27\u00a0000"),
    ("placeholder: 'final temperature = … with unit'", "placeholder: 'final = … with unit'"),
]

# ⊕ 24 Nov 2026 (pupil walk at 390 px): numbers, number-and-unit pairs and short equations in the
# page's worked examples and Your turn questions broke across lines ("27 / 000 J", "100 / °C",
# "E = m / L"). No-break spaces (U+00A0) inside them, in the worked-example text only: no rung,
# option or answer key is touched. Written by the same rule as the cards (docs table, M3).
LOGIC_EDITS += [
    ("head: 'A 500 g copper pan is given 7.7 kJ of energy. Calculate its temperature rise. (c = 385 J/kg °C)'",
     "head: 'A 500\xa0g copper pan is given 7.7\xa0kJ of energy. Calculate its temperature rise. (c = 385\xa0J/kg\xa0°C)'"),
    ("line: '500 g ÷ 1000 = 0.5 kg; 7.7 kJ × 1000 = 7700 J'",
     "line: '500\xa0g ÷ 1000 = 0.5\xa0kg; 7.7\xa0kJ × 1000 = 7700\xa0J'"),
    ("line: 'ΔE = m × c × Δθ'",
     "line: 'ΔE\xa0=\xa0m\xa0×\xa0c\xa0×\xa0Δθ'"),
    ("line: 'Δθ = 40 °C'",
     "line: 'Δθ = 40\xa0°C'"),
    ("note: 'Left in kJ, 7.7 ÷ 192.5 = 0.04 °C: a thousand times too small.'",
     "note: 'Left in kJ, 7.7 ÷ 192.5 = 0.04\xa0°C: a thousand times too small.'"),
    ("head: '250 g of water is heated from 18 °C to 65 °C. Calculate the energy needed. (c = 4200 J/kg °C)'",
     "head: '250\xa0g of water is heated from 18\xa0°C to 65\xa0°C. Calculate the energy needed. (c = 4200\xa0J/kg\xa0°C)'"),
    ("line: '250 g ÷ 1000 = 0.25 kg'",
     "line: '250\xa0g ÷ 1000 = 0.25\xa0kg'"),
    ("line: 'm = 0.25 kg, c = 4200, Δθ = 65 − 18 = 47 °C'",
     "line: 'm = 0.25\xa0kg, c = 4200, Δθ = 65 − 18 = 47\xa0°C'"),
    ("line: 'ΔE = 49 350 J'",
     "line: 'ΔE = 49\xa0350\xa0J'"),
    ("note: 'Left in grams, 250 × 4200 × 47 = 49 350 000 J: a thousand times too big.'",
     "note: 'Left in grams, 250 × 4200 × 47 = 49\xa0350\xa0000\xa0J: a thousand times too big.'"),
    ("head: 'A 1.5 kg iron block at 20 °C is supplied with 27\xa0000 J. Calculate its final temperature. (c = 450 J/kg °C)'",
     "head: 'A 1.5\xa0kg iron block at 20\xa0°C is supplied with 27\xa0000\xa0J. Calculate its final temperature. (c = 450\xa0J/kg\xa0°C)'"),
    ("close: '40 °C is the rise, not the answer: add it to the starting 20 °C.'",
     "close: '40\xa0°C is the rise, not the answer: add it to the starting 20\xa0°C.'"),
    ("line: 'Nothing to convert: kg, J and J/kg °C already.'",
     "line: 'Nothing to convert: kg, J and J/kg\xa0°C already.'"),
    ("line: 'Δθ = 27\xa0000 ÷ 675 = 40 °C'",
     "line: 'Δθ = 27\xa0000 ÷ 675 = 40\xa0°C'"),
    ("line: 'Final temperature = 20 + 40 = 60 °C'",
     "line: 'Final temperature = 20 + 40 = 60\xa0°C'"),
    ("head: 'A 50 W heater runs for 5.0 minutes and raises the temperature of a 1.2 kg metal block by 13 °C. Assume all the energy heats the block. Calculate the specific heat capacity of the metal.'",
     "head: 'A 50\xa0W heater runs for 5.0\xa0minutes and raises the temperature of a 1.2\xa0kg metal block by 13\xa0°C. Assume all the energy heats the block. Calculate the specific heat capacity of the metal.'"),
    ("close: 'Left in minutes, E comes out 250 J and c sixty times too small.'",
     "close: 'Left in minutes, E comes out 250\xa0J and c sixty times too small.'"),
    ("line: '5.0 min × 60 = 300 s'",
     "line: '5.0\xa0min × 60 = 300\xa0s'"),
    ("line: 'E = P t, then ΔE = m × c × Δθ'",
     "line: 'E\xa0=\xa0P\xa0t, then ΔE\xa0=\xa0m\xa0×\xa0c\xa0×\xa0Δθ'"),
    ("line: 'E = 50 × 300 = 15 000 J; 15 000 = 1.2 × c × 13'",
     "line: 'E = 50 × 300 = 15\xa0000\xa0J; 15\xa0000 = 1.2 × c × 13'"),
    ("line: 'c = 15 000 ÷ (1.2 × 13) = 15 000 ÷ 15.6 = 962'",
     "line: 'c = 15\xa0000 ÷ (1.2 × 13) = 15\xa0000 ÷ 15.6 = 962'"),
    ("line: 'c = 962 J/kg °C (3 significant figures)'",
     "line: 'c = 962\xa0J/kg\xa0°C (3 significant figures)'"),
    ("head: 'A 2.0 kg aluminium block is heated from 15 °C to 35 °C. Calculate the energy supplied. (c = 900 J/kg °C)'",
     "head: 'A 2.0\xa0kg aluminium block is heated from 15\xa0°C to 35\xa0°C. Calculate the energy supplied. (c = 900\xa0J/kg\xa0°C)'"),
    ("close: 'Using 35 °C as Δθ gives 63 000 J: the commonest lost mark.'",
     "close: 'Using 35\xa0°C as Δθ gives 63\xa0000\xa0J: the commonest lost mark.'"),
    ("line: 'Nothing to convert: kg, J/kg °C and °C already.'",
     "line: 'Nothing to convert: kg, J/kg\xa0°C and °C already.'"),
    ("line: 'm = 2.0 kg, c = 900, Δθ = 35 − 15 = 20 °C'",
     "line: 'm = 2.0\xa0kg, c = 900, Δθ = 35 − 15 = 20\xa0°C'"),
    ("line: 'ΔE = 36 000 J'",
     "line: 'ΔE = 36\xa0000\xa0J'"),
    ("head: '800 g of water cools from 70 °C to 25 °C. Calculate the energy it transfers to the surroundings. (c = 4200 J/kg °C)'",
     "head: '800\xa0g of water cools from 70\xa0°C to 25\xa0°C. Calculate the energy it transfers to the surroundings. (c = 4200\xa0J/kg\xa0°C)'"),
    ("close: 'Cooling: Δθ is the size of the drop, 70 − 25 = 45 °C.'",
     "close: 'Cooling: Δθ is the size of the drop, 70 − 25 = 45\xa0°C.'"),
    ("line: '800 g ÷ 1000 = 0.80 kg'",
     "line: '800\xa0g ÷ 1000 = 0.80\xa0kg'"),
    ("line: 'm = 0.80 kg, c = 4200, Δθ = 70 − 25 = 45 °C'",
     "line: 'm = 0.80\xa0kg, c = 4200, Δθ = 70 − 25 = 45\xa0°C'"),
    ("line: 'ΔE = 151 200 J'",
     "line: 'ΔE = 151\xa0200\xa0J'"),
]

# ⊕ 24 Nov 2026 (re-walk at 390 px): rung STEMS only get no-break spaces inside numbers and
# number-unit pairs ("(c = 385 J/kg °C)", "a drink at 20 °C" split across lines). Rung ids are by
# position, so the ids hold; no option text or answer key is touched.
LOGIC_EDITS += [
    ("prompt: 'A 2.0 kg copper block is heated by a 60 W heater for 4.0 minutes. All the energy goes into the block. Calculate its temperature rise. (c = 385 J/kg °C) Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'A 2.0\xa0kg copper block is heated by a 60\xa0W heater for 4.0\xa0minutes. All the energy goes into the block. Calculate its temperature rise. (c = 385\xa0J/kg\xa0°C) Work it on paper, then choose the conversion and give the answer and unit.'"),
    ("prompt: 'A 40 g copper spoon warms from 20 °C to 70 °C in a hot drink. Calculate the energy it takes in. (c = 385 J/kg °C) Work it on paper, then choose the conversion and give the answer and unit.'",
     "prompt: 'A 40\xa0g copper spoon warms from 20\xa0°C to 70\xa0°C in a hot drink. Calculate the energy it takes in. (c = 385\xa0J/kg\xa0°C) Work it on paper, then choose the conversion and give the answer and unit.'"),
]

LESSON = {
    "slug": "temperature-changes-shc",
    "start": {
        "setup": "1\u00a0kg of dry sand and 1\u00a0kg of seawater get the same energy from the Sun.",
        "question": "If you had to guess, which one warms up more?",
        "options": [
            ("The sand",
             "The sand. Water needs far more energy to raise the temperature of each kilogram by "
             "1\u00a0°C, so the same energy warms it much less."),
            ("The seawater",
             "The sand. Water needs far more energy to raise the temperature of each kilogram by "
             "1\u00a0°C, so the same energy warms it much less."),
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
                  "Water's is 4200\u00a0J/kg\u00a0°C. Aluminium's is 900\u00a0J/kg\u00a0°C. So 1\u00a0kg of water needs "
                  "more than four times as much energy as 1\u00a0kg of aluminium to warm by 1\u00a0°C."]},
        {"kind": "card", "title": "The equation",
         "body": ["ΔE\u00a0=\u00a0m\u00a0c\u00a0Δθ",
                  {"points": ["change in thermal energy, ΔE, in joules (J)",
                              "mass, m, in kilograms (kg)",
                              "specific heat capacity, c, in joules per kilogram per degree "
                              "Celsius (J/kg\u00a0°C)",
                              "temperature change, Δθ, in degrees Celsius (°C)"]},
                  "This equation is on the Physics equation sheet. You need to be able to use it "
                  "and rearrange it.",
                  {"slot": "triangle:EQ_SHC"}]},
        {"kind": "card", "title": "The temperature change",
         "body": ["Δθ is a change: the final temperature minus the starting temperature.",
                  "When something cools, Δθ is the size of the drop. Water cooling from 80\u00a0°C to "
                  "30\u00a0°C has Δθ = 50\u00a0°C."]},
        {"kind": "card", "title": "Energy from a heater",
         "body": ["The energy from an electric heater is measured with a joulemeter, or worked out "
                  "from energy transferred = power × time, E\u00a0=\u00a0P\u00a0t, with P in watts and t in "
                  "seconds.",
                  "You need to remember E\u00a0=\u00a0P\u00a0t: it is not on the equation sheet."]},
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
                "temperature of 1\u00a0kg of it by 1\u00a0°C. Change in thermal energy = mass × specific "
                "heat capacity × temperature change.",
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
             "<strong>Define</strong>: give the exact meaning. For c: energy, 1\u00a0kg and 1\u00a0°C.",
             "<strong>Calculate</strong>: convert, write the equation, put the numbers in, "
             "rearrange, then give the answer with its unit.",
             "<strong>Describe a method</strong>: the equipment, what you measure and how, in "
             "order, and how you work out c.",
             "<strong>Explain</strong>: link cause to effect, for example where the energy went "
             "and what that did to Δθ and to c.",
         ]}]},
    ],
    "try": None,
    "legacy": {"batch": "batch-3", "logic_edits": LOGIC_EDITS},
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
