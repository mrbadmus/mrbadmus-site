# -*- coding: utf-8 -*-
"""Volumes of gases, in the lean shape. New record, no legacy page.
Spec table: ks4-gas-volumes.md (AQA 8462 4.3.5, chemistry only, HT only).

Route TH only. There is no Combined Science (8464) section for this content, so the eyebrow is
"AQA Chemistry (8462) 4.3.5 · Quantitative" and batch_lean.CHEM_EYEBROW carries (None, "4.3.5").
Moles from a mass (8462 4.3.2.1) and the mole ratio from an equation (4.3.2.2) are used as
recall only; each has its own lesson.

The record carries two equations: EQ_N (moles from mass, the same triangle as Moles and
Amounts of substances in equations) and EQ_V (the volume of a gas at room temperature and
pressure). The worked examples chain them as Step 1 and Step 2.
"""

_CFQ_PH = ["anything to convert?", "written out", "numbers in", "work it out", "with unit"]


def _q(lines, conv_ph=None):
    """A Ks4Cfifa question's five lines, in the legacy CFQ shape (as moles.py writes them)."""
    letters = [("C", "Convert"), ("F", "Formula"), ("I", "Insert"), ("F", "Fine-tune"), ("A", "Answer")]
    ph = list(_CFQ_PH)
    if conv_ph:
        ph[0] = conv_ph
    return [{"letter": l, "label": lab, "placeholder": p, "line": ln}
            for (l, lab), p, ln in zip(letters, ph, lines)]


LESSON = {
    "slug": "gas-volumes",
    "start": {
        "setup": "Two balloons are at room temperature and pressure. One holds 1 mol of hydrogen. "
                 "The other holds 1 mol of carbon dioxide.",
        "question": "If you had to guess, which balloon is bigger?",
        "options": [
            ("The carbon dioxide balloon",
             "They are the same size. One mole of any gas takes up the same volume at the same "
             "temperature and pressure: 24 dm³ at room temperature and pressure."),
            ("They are the same size",
             "They are the same size. One mole of any gas takes up the same volume at the same "
             "temperature and pressure: 24 dm³ at room temperature and pressure."),
        ],
        "answer": 1,
    },
    "words": ["room temperature and pressure (RTP)", "dm³ (decimetre cubed)", "amount in moles",
              "volume ratio"],
    "knowledge": [
        {"kind": "card", "title": "Equal moles, equal volumes",
         "body": ["Equal amounts in moles of gases occupy the same volume under the same conditions "
                  "of temperature and pressure.",
                  "This is true for every gas. One mole of hydrogen, H₂, and one mole of carbon "
                  "dioxide, CO₂, take up the same volume at the same temperature and pressure.",
                  "Their masses are different. One mole of H₂ has a mass of 2 g. One mole of CO₂ "
                  "has a mass of 44 g."]},
        {"kind": "card", "title": "One mole of gas at room temperature and pressure",
         "body": ["The volume of one mole of any gas at room temperature and pressure (20 °C and "
                  "1 atmosphere pressure) is 24 dm³.",
                  {"points": ["2 mol of gas takes up 2 × 24 = 48 dm³.",
                              "0.5 mol of gas takes up 0.5 × 24 = 12 dm³."]}]},
        {"kind": "card", "title": "cm³ and dm³",
         "body": ["1 dm³ = 1000 cm³, so 24 dm³ = 24 000 cm³.",
                  {"points": ["To change cm³ into dm³, divide by 1000.",
                              "To change dm³ into cm³, multiply by 1000."]},
                  "A gas syringe measures volume in cm³. Change it into dm³ before you use "
                  "24 dm³."]},
        {"kind": "card", "title": "The equation",
         "body": [{"slot": "triangle:EQ_V"},
                  "Change the subject to find the amount: amount of gas (mol) = volume of gas "
                  "(dm³) ÷ 24."]},
        {"kind": "card", "title": "Volume from a mass",
         "body": ["To find the volume of a gas from its mass, work out the amount in moles first.",
                  {"points": ["Step 1: amount (mol) = mass (g) ÷ M<sub>r</sub>",
                              "Step 2: volume (dm³) = amount (mol) × 24"]},
                  {"slot": "triangle:EQ_N"}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Gas volumes from a balanced equation",
         "body": ["The volumes of gaseous reactants and products can be calculated from the "
                  "balanced equation for the reaction.",
                  "Equal amounts in moles of gases have equal volumes. So for gases, the balancing "
                  "numbers give the ratio of volumes as well as the ratio of moles.",
                  "N₂(g) + 3H₂(g) → 2NH₃(g): 10 dm³ of nitrogen reacts with 30 dm³ of hydrogen to "
                  "make 20 dm³ of ammonia.",
                  "volume wanted = volume given × wanted balancing number ÷ given balancing number",
                  "This only works for gases, with every volume measured at the same temperature "
                  "and pressure."]},
        {"kind": "reveal",
         "title": "Burning 50 cm³ of methane, all volumes at room temperature and pressure: "
                  "CH₄(g) + 2O₂(g) → CO₂(g) + 2H₂O(l)",
         "cols": ["Working", "Volume"],
         "rows": [
             ("Oxygen used", "50 × 2 ÷ 1", "100 cm³"),
             ("Carbon dioxide made", "50 × 1 ÷ 1", "50 cm³"),
             ("Water made", "Water is a liquid at room temperature and pressure", "No gas volume"),
         ]},
        {"kind": "card", "title": "From the mass of a reactant to a volume of gas",
         "body": ["CaCO₃(s) + 2HCl(aq) → CaCl₂(aq) + H₂O(l) + CO₂(g). Find the volume of carbon "
                  "dioxide made from 5.0 g of calcium carbonate (M<sub>r</sub> = 100) at room "
                  "temperature and pressure.",
                  {"points": [
                      "Step 1: amount of CaCO₃ = 5.0 ÷ 100 = 0.050 mol.",
                      "Step 2: the ratio CaCO₃ : CO₂ is 1 : 1, so 0.050 mol of CO₂ is made.",
                      "Step 3: volume of CO₂ = 0.050 × 24 = 1.2 dm³, which is 1200 cm³.",
                  ]}]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("0.3 mol of gas: 0.3 ÷ 24 = 0.0125 dm³.",
              "Multiply: 0.3 × 24 = 7.2 dm³. Every mole takes up 24 dm³."),
             ("A mole of carbon dioxide takes up more room than a mole of hydrogen because it is "
              "heavier.",
              "At the same temperature and pressure, one mole of any gas takes up the same "
              "volume."),
             ("180 cm³ of gas: 180 ÷ 24 = 7.5 mol.",
              "Convert first: 180 cm³ = 0.18 dm³, so 0.18 ÷ 24 = 0.0075 mol."),
             ("N₂ + 3H₂ → 2NH₃, so 15 dm³ of hydrogen makes 15 × 3 ÷ 2 = 22.5 dm³ of ammonia.",
              "Wanted over given: 15 × 2 ÷ 3 = 10 dm³ of ammonia."),
             ("Using 24 dm³ for every substance in the equation.",
              "24 dm³ is for one mole of a gas. Solids, liquids and solutions do not count."),
         ]}]},
    ],
    "key_fact": "Equal amounts in moles of gases occupy the same volume at the same temperature and "
                "pressure. One mole of any gas at room temperature and pressure (20 °C and "
                "1 atmosphere) occupies 24 dm³, so volume of gas (dm³) = amount (mol) × 24.",
    "deeper": [
        {"kind": "card", "title": "Links to other lessons",
         "body": ["Moles from a mass is in Moles.",
                  "Reading the mole ratio from an equation is in Amounts of substances in "
                  "equations."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: write each step with its unit.",
             "<strong>Give your answer in cm³</strong>: work in dm³, then multiply by 1000 at "
             "the end.",
             "<strong>Explain</strong>: link equal amounts in moles to equal volumes of gas.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_V": {"name": "Volume of a gas at room temperature and pressure",
                 "written": "volume of gas (dm³) = amount of gas (mol) × 24",
                 "source": "none",
                 "top": {"s": "V", "name": "volume of gas", "unit": "dm³"},
                 "bottom": [{"s": "n", "name": "amount of gas", "unit": "mol"},
                            {"s": "24", "name": "volume of one mole of gas at room temperature "
                                                "and pressure",
                             "unit": "dm³", "fixed": True}]},
        "EQ_N": {"name": "Moles from mass", "written": "number of moles = mass (g) ÷ Mr",
                 "source": "none",
                 "top": {"s": "m", "name": "mass", "unit": "g"},
                 "bottom": [{"s": "n", "name": "number of moles", "unit": "mol"},
                            {"s": "Mr", "name": "relative formula mass (Ar for an element)",
                             "unit": "no unit"}]},
    },
    "cfifa": {
        "examples": [
            {"tab": "Volume from moles", "eq": "EQ_V", "find": "V",
             "next": "Now the triangle the other way.",
             "head": "Calculate the volume of 0.25 mol of oxygen gas at room temperature and "
                     "pressure.",
             "steps": [["C", "Convert", "Nothing to convert: the amount is in moles."],
                       ["F", "Formula", "V = n × 24"],
                       ["I", "Insert", "V = 0.25 × 24"],
                       ["F", "Fine-tune", "V = 6"],
                       ["A", "Answer", "6 dm³ of oxygen"]]},
            {"tab": "Moles from cm³", "eq": "EQ_V", "find": "n",
             "next": "Now a volume from a mass, in two steps.",
             "head": "A gas syringe collects 360 cm³ of hydrogen at room temperature and pressure. "
                     "Calculate the amount of hydrogen in moles.",
             "steps": [["C", "Convert", "360 cm³ ÷ 1000 = 0.36 dm³",
                        "24 is in dm³, so the volume must be in dm³ too."],
                       ["F", "Formula", "n = V ÷ 24"],
                       ["I", "Insert", "n = 0.36 ÷ 24"],
                       ["F", "Fine-tune", "n = 0.015"],
                       ["A", "Answer", "0.015 mol of hydrogen"]]},
            {"tab": "Step 1: mass to moles", "eq": "EQ_N", "find": "n",
             "next": "Step 2 uses this answer.",
             "head": "Calculate the volume of 8.8 g of carbon dioxide, CO₂, at room temperature "
                     "and pressure (Mr = 44). Step 1: find the amount in moles.",
             "steps": [["C", "Convert", "Nothing to convert: the mass is in grams."],
                       ["F", "Formula", "n = m ÷ Mr"],
                       ["I", "Insert", "n = 8.8 ÷ 44"],
                       ["F", "Fine-tune", "n = 0.2"],
                       ["A", "Answer", "0.2 mol of carbon dioxide"]]},
            {"tab": "Step 2: moles to volume", "eq": "EQ_V", "find": "V",
             "next": "Now yours, below.",
             "head": "Step 2: find the volume of the carbon dioxide at room temperature and "
                     "pressure.",
             "steps": [["C", "Convert", "Nothing to convert. n = 0.2 mol, from Step 1."],
                       ["F", "Formula", "V = n × 24"],
                       ["I", "Insert", "V = 0.2 × 24"],
                       ["F", "Fine-tune", "V = 4.8"],
                       ["A", "Answer", "4.8 dm³ of carbon dioxide"]]},
        ],
        "questions": [
            {"tab": "Question 1", "id": "gv-q1",
             "head": "Calculate the volume of 1.5 mol of nitrogen gas at room temperature and "
                     "pressure.",
             "close": "Each mole takes up 24 dm³, so multiply: 1.5 × 24.",
             "steps": _q(["Nothing to convert.", "V = n × 24", "V = 1.5 × 24", "V = 36",
                          "36 dm³"])},
            {"tab": "Question 2", "id": "gv-q2",
             "head": "Calculate the amount, in moles, of 9.6 dm³ of methane at room temperature "
                     "and pressure.",
             "close": "Cover n: n = V ÷ 24, so 9.6 ÷ 24, not 9.6 × 24.",
             "steps": _q(["Nothing to convert: the volume is in dm³.", "n = V ÷ 24",
                          "n = 9.6 ÷ 24", "n = 0.4", "0.4 mol"])},
            {"tab": "Question 3", "id": "gv-q3",
             "head": "Calculate the volume of 3.2 g of oxygen gas, O₂, at room temperature and "
                     "pressure (Mr = 32).",
             "close": "Turn the mass into moles first: 3.2 ÷ 32 = 0.1 mol. Then 0.1 × 24.",
             "steps": _q(["n = 3.2 ÷ 32 = 0.1 mol", "V = n × 24", "V = 0.1 × 24", "V = 2.4",
                          "2.4 dm³"], "mass to moles first?")},
            {"tab": "Question 4", "id": "gv-q4",
             "head": "A reaction makes 0.004 mol of carbon dioxide. Calculate its volume at room "
                     "temperature and pressure. Give your answer in cm³.",
             "close": "Work in dm³ first: 0.004 × 24 = 0.096 dm³. Then × 1000 for cm³.",
             "steps": _q(["Nothing to convert yet. Change dm³ into cm³ at the end.",
                          "V = n × 24", "V = 0.004 × 24",
                          "V = 0.096 dm³, and 0.096 × 1000 = 96", "96 cm³"])},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State the volume of one mole of any gas at room temperature and pressure.",
             "why": "One mole of any gas at room temperature and pressure occupies 24 dm³.",
             "options": [
                 {"text": "24 dm³", "correct": True},
                 {"text": "24 cm³", "correct": False,
                  "reply": "A cm³ is a thousand times smaller than a dm³, so 24 cm³ is far "
                           "too small. One mole takes up 24 dm³."},
                 {"text": "It depends on which gas it is", "correct": False,
                  "reply": "At the same temperature and pressure, one mole of any gas has the "
                           "same volume."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the temperature and pressure that AQA calls room temperature and "
                       "pressure.",
             "why": "Room temperature and pressure is 20 °C and 1 atmosphere pressure.",
             "options": [
                 {"text": "0 °C and 1 atmosphere", "correct": False,
                  "reply": "Room temperature is 20 °C. Water freezes at 0 °C."},
                 {"text": "20 °C and 24 atmospheres", "correct": False,
                  "reply": "The pressure is 1 atmosphere. 24 is the volume, in dm³, of one mole."},
                 {"text": "20 °C and 1 atmosphere", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 2,
             "prompt": "Calculate the volume of 0.75 mol of carbon dioxide at room temperature and "
                       "pressure. Give your answer in dm³.",
             "convOptions": ["Nothing to convert: it is in mol", "Convert dm³ to cm³: multiply by 1000",
                             "Convert 0.75 mol to grams first"],
             "convAnswer": 0, "answer": 18, "tol": 0.05, "unit": "dm³",
             "units": ["dm³", "cm³", "mol", "g"],
             "right": "0.75 × 24 = 18 dm³.",
             "wrong": "Nothing to convert. Volume = amount × 24 = 0.75 × 24 = 18 dm³.",
             "model": ["C · Nothing to convert", "F · volume = amount × 24",
                       "I · volume = 0.75 × 24", "F · volume = 18", "A · 18 dm³"]},
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "Calculate the volume of 0.68 g of ammonia, NH₃, at room temperature and "
                       "pressure. Give your answer in dm³. Mr of NH₃ = 17.",
             "convOptions": ["Nothing to convert", "Mass to moles first: divide by Mr",
                             "Mass to moles first: multiply by Mr"],
             "convAnswer": 1, "answer": 0.96, "tol": 0.005, "unit": "dm³",
             "units": ["dm³", "cm³", "mol", "g"],
             "right": "0.68 ÷ 17 = 0.04 mol, and 0.04 × 24 = 0.96 dm³.",
             "wrong": "Turn the mass into moles first: 0.68 ÷ 17 = 0.04 mol. Then volume = "
                      "0.04 × 24 = 0.96 dm³.",
             "model": ["C · 0.68 ÷ 17 = 0.04 mol", "F · volume = amount × 24",
                       "I · volume = 0.04 × 24", "F · volume = 0.96", "A · 0.96 dm³"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Calculate", "marks": 3,
             "prompt": "Zinc reacts with excess hydrochloric acid: Zn + 2HCl → ZnCl₂ + H₂. "
                       "Calculate the volume of hydrogen made from 1.3 g of zinc at room "
                       "temperature and pressure (Ar of Zn = 65). Put the links in order.",
             "links": ["Amount of zinc = 1.3 ÷ 65 = 0.020 mol.",
                       "One mole of zinc makes one mole of hydrogen, so 0.020 mol of H₂ is made.",
                       "Volume of hydrogen = 0.020 × 24 = 0.48 dm³."],
             "herrings": [{"text": "Amount of zinc = 65 ÷ 1.3 = 50 mol.",
                           "why": "Amount = mass ÷ Ar, so 1.3 ÷ 65."},
                          {"text": "Two moles of HCl react, so 0.040 mol of H₂ is made.",
                           "why": "Use the balancing numbers of zinc and hydrogen. They are 1 : 1."}]},
            {"kind": "chain", "command": "Calculate", "marks": 3,
             "prompt": "Carbon monoxide burns in oxygen: 2CO(g) + O₂(g) → 2CO₂(g). Calculate the "
                       "volume of oxygen needed to burn 80 cm³ of carbon monoxide. All volumes are "
                       "at room temperature and pressure. Put the links in order.",
             "links": ["The balancing numbers give the mole ratio CO : O₂ = 2 : 1.",
                       "Equal amounts in moles of gases have equal volumes, so the volume ratio is "
                       "also 2 : 1.",
                       "Using the 2 : 1 volume ratio, volume of oxygen = 80 × 1 ÷ 2 = 40 cm³."],
             "herrings": [{"text": "Volume of oxygen = 80 × 2 ÷ 1 = 160 cm³.",
                           "why": "Wanted over given: 1 for oxygen over 2 for carbon monoxide."},
                          {"text": "Turn 80 cm³ into moles by multiplying by 24.",
                           "why": "No moles are needed here. Volumes of gases are in the same "
                                  "ratio as their moles."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Calculate", "marks": 4,
             "prompt": "Sodium hydrogencarbonate decomposes when it is heated: "
                       "2NaHCO₃ → Na₂CO₃ + H₂O + CO₂. A student heats 4.2 g of sodium "
                       "hydrogencarbonate. Calculate the volume of carbon dioxide made, at room "
                       "temperature and pressure. Give your answer in cm³. Mr of NaHCO₃ = 84. "
                       "Show each step.",
             "points": ["Amount of NaHCO₃ = 4.2 ÷ 84 = 0.050 mol.",
                        "The ratio NaHCO₃ : CO₂ is 2 : 1, so 0.050 ÷ 2 = 0.025 mol of CO₂.",
                        "Volume of CO₂ = 0.025 × 24 = 0.60 dm³ (or your amount of CO₂ × 24).",
                        "0.60 dm³ × 1000 = 600 cm³ (or your volume in dm³ × 1000)."],
             "reject": ["For point 2: “0.050 mol of CO₂”. The 2 : 1 ratio is missing.",
                        "For point 3: “0.025 ÷ 24”. Multiply an amount by 24, do not divide."]},
        ],
    },
}
