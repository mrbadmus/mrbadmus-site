# -*- coding: utf-8 -*-
"""Transformers, in the lean shape. Spec table: ks4-transformers.md.

Triple Higher only. AQA Physics 8463 4.7.3.4 (physics only, HT only), with the National Grid link
from 4.2.4.3. The old data's spec field says 6.7.3.4, but Combined (8464) has no 6.7.3: section 6.7
stops at 6.7.2.

No formula triangle on this page. Vp / Vs = np / ns is a ratio of four quantities and
Vs × Is = Vp × Ip has four quantities, so neither fits a three-cell triangle. Both are
sheet equations (name, written, source "sheet"): no triangle, and the CFIFA Formula step
shows the written form."""

LESSON = {
    "slug": "transformers",
    "start": {
        "setup": "A transformer has more turns on its secondary coil than on its primary coil.",
        "question": "If you had to guess, is the p.d. across the secondary coil bigger or smaller "
                    "than the p.d. across the primary coil?",
        "options": [
            ("Bigger",
             "Bigger. More turns on the secondary coil gives a bigger p.d. This is a step-up "
             "transformer."),
            ("Smaller",
             "Bigger. More turns on the secondary coil gives a bigger p.d. This is a step-up "
             "transformer."),
        ],
        "answer": 0,
    },
    "words": ["primary coil", "secondary coil", "step-up transformer", "step-down transformer"],
    "knowledge": [
        {"kind": "card", "title": "What a transformer is",
         "body": ["A basic transformer consists of a primary coil and a secondary coil wound on an "
                  "iron core.",
                  "Iron is used as it is easily magnetised.",
                  {"slot": "fig:transformer"}]},
        {"kind": "card", "title": "How it works",
         "body": [{"points": [
             "An alternating current in the primary coil produces a magnetic field in the iron "
             "core that keeps changing.",
             "The iron core carries this changing magnetic field through the secondary coil.",
             "The changing field induces a potential difference (p.d.) across the secondary coil. "
             "If the secondary coil is part of a complete circuit, a current is induced in it.",
         ]},
             "No current flows through the core from one coil to the other. The changing magnetic "
             "field does the job.",
             "A steady direct current makes a field that does not change, so nothing is induced. "
             "Transformers need a.c."]},
        {"kind": "card", "title": "The p.d.s and the turns",
         "body": ["The ratio of the p.d.s across the primary and secondary coils depends on the "
                  "ratio of the number of turns on each coil.",
                  "V<sub>p</sub> / V<sub>s</sub> = n<sub>p</sub> / n<sub>s</sub>",
                  {"points": ["V<sub>p</sub>: p.d. across the primary coil, in volts (V)",
                              "V<sub>s</sub>: p.d. across the secondary coil, in volts (V)",
                              "n<sub>p</sub>: number of turns on the primary coil",
                              "n<sub>s</sub>: number of turns on the secondary coil"]},
                  "This equation is on the equation sheet."]},
        {"kind": "reveal", "title": "Step-up and step-down",
         "cols": ["Step-up", "Step-down"],
         "rows": [
             ("p.d.", "Vₛ > Vₚ", "Vₛ < Vₚ"),
             ("Turns", "More turns on the secondary coil", "Fewer turns on the secondary coil"),
             ("Current (100% efficient)", "Smaller in the secondary coil",
              "Bigger in the secondary coil"),
         ]},
        {"kind": "card", "title": "Power in and power out",
         "body": ["If transformers were 100% efficient, the electrical power output would equal "
                  "the electrical power input.",
                  "V<sub>s</sub> × I<sub>s</sub> = V<sub>p</sub> × I<sub>p</sub>",
                  {"points": ["V<sub>s</sub> × I<sub>s</sub> is the power output (secondary coil), "
                              "in watts (W)",
                              "V<sub>p</sub> × I<sub>p</sub> is the power input (primary coil), "
                              "in watts (W)",
                              "I<sub>p</sub> and I<sub>s</sub>: currents in the primary and "
                              "secondary coils, in amps (A)"]},
                  "This equation is on the equation sheet.",
                  "A step-up transformer increases the p.d. and decreases the current. A step-down "
                  "transformer decreases the p.d. and increases the current."]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Why the National Grid uses a high p.d.",
         "body": [{"points": [
             "Step-up transformers increase the p.d. from the power station to the transmission "
             "cables.",
             "For the same power, V<sub>s</sub> × I<sub>s</sub> = V<sub>p</sub> × I<sub>p</sub>, "
             "so a higher p.d. means a smaller current in the cables.",
             "A smaller current heats the cables less, so less energy is dissipated to the "
             "surroundings.",
             "Step-down transformers then decrease the p.d., to a much lower value, for "
             "domestic use.",
         ]},
             "This is why the National Grid is an efficient way to transfer energy."]},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("A step-up transformer increases the power.",
              "It increases the p.d. and decreases the current. Power out is never more than power in."),
             ("25 kV ÷ 1000 = 0.025 V.",
              "25 kV × 1000 = 25 000 V. Kilo means a thousand."),
             ("Transformers work on d.c.",
              "They need a.c. Only a changing magnetic field induces a p.d."),
         ]}]},
    ],
    "key_fact": "An alternating current in the primary coil makes a changing magnetic field in the "
                "iron core, which induces a potential difference across the secondary coil. "
                "Vₚ / Vₛ = nₚ / nₛ, and for a 100% efficient transformer "
                "Vₛ × Iₛ = Vₚ × Iₚ.",
    "deeper": [
        {"kind": "card", "title": "A quick check",
         "body": ["If the secondary coil has 10 times as many turns as the primary, the p.d. is "
                  "10 times bigger.",
                  "For a 100% efficient transformer, the current is then 10 times smaller."]},
        {"kind": "card", "title": "Real transformers",
         "body": ["Real transformers are very efficient, but not 100%.",
                  "Some energy is dissipated to the surroundings, so the power output is a little "
                  "less than the power input."]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: convert, write the equation, substitute, rearrange, "
             "then give the answer with its unit.",
             "<strong>Explain</strong> how it works: a.c. in the primary, changing field in the "
             "core, p.d. induced in the secondary.",
             "<strong>Explain</strong> the National Grid: higher p.d., smaller current, less "
             "heating, less energy wasted.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_TURNS": {"name": "Transformer p.d.s and turns",
                     "written": "Vₚ / Vₛ = nₚ / nₛ",
                     "source": "sheet"},
        "EQ_TPOWER": {"name": "Transformer power",
                      "written": "Vₛ × Iₛ = Vₚ × Iₚ",
                      "source": "sheet"},
    },
    "cfifa": {
        "examples": [
            {"tab": "Step 1: the p.d.", "eq": "EQ_TURNS", "find": "Vₛ",
             "next": "Step 2 uses this answer.",
             "head": "A power station transformer has 1000 turns on its primary coil and 16 000 "
                     "turns on its secondary coil. The p.d. across the primary coil is 25 kV. "
                     "Calculate the p.d. across the secondary coil.",
             "steps": [["C", "Convert", "25 kV × 1000 = 25 000 V"],
                       ["F", "Formula", "Vₚ / Vₛ = nₚ / nₛ"],
                       ["I", "Insert", "25 000 / Vₛ = 1000 / 16 000"],
                       ["F", "Fine-tune", "Vₛ = 25 000 × 16 000 ÷ 1000 = 400 000",
                        "Rearrange: multiply both sides by Vₛ and by 16 000, then divide by 1000."],
                       ["A", "Answer", "Vₛ = 400 000 V (400 kV)"]]},
            {"tab": "Step 2: the current", "eq": "EQ_TPOWER", "find": "Iₛ",
             "head": "The current in the primary coil of the same transformer is 4000 A. Assume "
                     "it is 100% efficient. Calculate the current in the secondary coil.",
             "steps": [["C", "Convert", "Vₚ = 25 000 V. Vₛ = 400 000 V, from Step 1."],
                       ["F", "Formula", "Vₛ × Iₛ = Vₚ × Iₚ"],
                       ["I", "Insert", "400 000 × Iₛ = 25 000 × 4000"],
                       ["F", "Fine-tune", "Iₛ = 25 000 × 4000 ÷ 400 000 = 250",
                        "Rearrange: divide both sides by 400 000."],
                       ["A", "Answer", "Iₛ = 250 A"]]},
            {"tab": "Current from the supply", "eq": "EQ_TPOWER", "find": "Iₚ",
             "head": "A transformer is connected to the 230 V mains. It supplies 36 W to a 12 V "
                     "lamp. Assume it is 100% efficient. Calculate the current drawn from the "
                     "mains supply.",
             "steps": [["C", "Convert", "Nothing to convert. Power output = 36 W."],
                       ["F", "Formula", "Vₛ × Iₛ = Vₚ × Iₚ, and Vₛ × Iₛ is the power output"],
                       ["I", "Insert", "36 = 230 × Iₚ"],
                       ["F", "Fine-tune", "Iₚ = 36 ÷ 230 = 0.157",
                        "Rearrange: divide both sides by 230."],
                       ["A", "Answer", "Iₚ = 0.16 A (2 s.f.)"]]},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "Give the reason the core of a transformer is made of iron.",
             "why": "Iron is used as it is easily magnetised.",
             "options": [
                 {"text": "Iron does not conduct electricity", "correct": False,
                  "reply": "Iron does conduct electricity. It is used because it is easily magnetised."},
                 {"text": "Iron is easily magnetised", "correct": True},
                 {"text": "Iron carries the current from one coil to the other", "correct": False,
                  "reply": "No current flows between the coils. The changing magnetic field induces it."},
                 {"text": "Iron stays magnetised when the current stops", "correct": False,
                  "reply": "Iron loses its magnetism quickly. It is used because it is easily magnetised."},
             ]},
            {"kind": "mcq", "command": "Give", "marks": 1,
             "prompt": "In a step-down transformer, how does Vₛ compare with Vₚ?",
             "why": "In a step-down transformer Vₛ < Vₚ.",
             "options": [
                 {"text": "Vₛ > Vₚ", "correct": False,
                  "reply": "That is a step-up transformer."},
                 {"text": "Vₛ = Vₚ", "correct": False,
                  "reply": "Then the p.d. would not be stepped down at all."},
                 {"text": "Vₛ < Vₚ", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "A transformer steps 11 kV down to 230 V. The primary coil has 4400 turns. "
                       "Calculate the number of turns on the secondary coil.",
             "convOptions": ["Nothing to convert", "Convert kV to V: multiply by 1000",
                             "Convert kV to V: divide by 1000"],
             "convAnswer": 1, "answer": 92, "tol": 0.5, "unit": "no unit",
             "units": ["no unit", "V", "A", "W"],
             "right": "nₛ = 4400 × 230 ÷ 11 000 = 92 turns.",
             "wrong": "11 kV = 11 000 V. Vₚ / Vₛ = nₚ / nₛ, so nₛ = nₚ × Vₛ ÷ Vₚ = 4400 × 230 ÷ 11 000 = 92.",
             "model": ["C · 11 kV × 1000 = 11 000 V", "F · Vₚ / Vₛ = nₚ / nₛ",
                       "I · 11 000 / 230 = 4400 / nₛ", "F · nₛ = 4400 × 230 ÷ 11 000 = 92",
                       "A · 92 turns"]},
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "A 100% efficient transformer has a p.d. of 230 V across its primary coil. "
                       "Its secondary coil supplies 12 V and 500 mA. Calculate the current in the "
                       "primary coil.",
             "convOptions": ["Nothing to convert", "Convert mA to A: divide by 1000",
                             "Convert mA to A: multiply by 1000"],
             "convAnswer": 1, "answer": 0.026, "tol": 0.0005, "unit": "A",
             "units": ["A", "mA", "V", "W"],
             "right": "12 × 0.5 = 6 W, and 6 ÷ 230 = 0.026 A.",
             "wrong": "500 mA = 0.5 A. Vₛ × Iₛ = Vₚ × Iₚ, so Iₚ = 12 × 0.5 ÷ 230 = 0.026 A.",
             "model": ["C · 500 mA ÷ 1000 = 0.5 A", "F · Vₛ × Iₛ = Vₚ × Iₚ",
                       "I · 12 × 0.5 = 230 × Iₚ", "F · Iₚ = 6 ÷ 230 = 0.026",
                       "A · 0.026 A"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain how a transformer produces a p.d. across its secondary coil. "
                       "Put the links in order.",
             "links": ["An alternating current flows in the primary coil.",
                       "This produces a changing magnetic field in the iron core.",
                       "The changing field passes through the secondary coil and induces a p.d. "
                       "across it."],
             "herrings": [{"text": "Current flows through the iron core to the secondary coil.",
                           "why": "No current passes between the coils. The changing magnetic field induces it."},
                          {"text": "A steady direct current in the primary coil works just as well.",
                           "why": "A steady current makes a field that does not change, so nothing is induced."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why the National Grid transmits electricity at a high potential "
                       "difference. Put the links in order.",
             "links": ["A step-up transformer increases the p.d. from the power station.",
                       "For the same power, Vₛ × Iₛ = Vₚ × Iₚ, so a higher p.d. means a smaller "
                       "current in the cables.",
                       "A smaller current heats the cables less, so less energy is dissipated and "
                       "the transfer is more efficient."],
             "herrings": [{"text": "A high p.d. makes the electricity travel faster.",
                           "why": "Speed is not the reason. A smaller current wastes less energy."},
                          {"text": "A step-up transformer increases the power.",
                           "why": "Power out is never more than power in."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Explain", "marks": 6,
             "prompt": "A step-up transformer is used at a power station. Explain how it works and "
                       "why it is used.",
             "levels": [
                 {"label": "Level 3 · 5–6", "text": "Explains how the transformer induces a bigger p.d., and links the smaller current to less energy lost in the cables.", "max": 6},
                 {"label": "Level 2 · 3–4", "text": "Explains how it works or why it is used, with some missing detail.", "max": 4},
                 {"label": "Level 1 · 1–2", "text": "One or two relevant points.", "max": 2},
                 {"label": "No relevant content · 0", "text": "", "max": 0}],
             "points": ["A primary coil and a secondary coil are wound on an iron core, which is easily magnetised.",
                        "An alternating current in the primary coil makes a changing magnetic field in the core.",
                        "The changing field induces a p.d. across the secondary coil.",
                        "The secondary coil has more turns, so Vₛ > Vₚ (Vₚ / Vₛ = nₚ / nₛ).",
                        "Vₛ × Iₛ = Vₚ × Iₚ, so the current in the transmission cables is smaller.",
                        "A smaller current heats the cables less, so less energy is dissipated."],
             "reject": ["“It steps up the power.”",
                        "“The current flows through the core to the secondary coil.”"]},
        ],
    },
}
