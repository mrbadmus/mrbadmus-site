# -*- coding: utf-8 -*-
"""Density of materials, in the lean shape. New record, no legacy page (it replaces the old
generate_site_v5 page). Spec table: ks4-density-of-materials.md (AQA 8464 6.3.1.1 + Required
practical activity 17 / 8463 4.3.1.1 + Required practical activity 5, word for word the same apart
from the practical's number). No HT-only or physics-only line. Every route gets the same lesson,
except the practical card, which carries each spec's own number.

density = mass ÷ volume is a recall equation: it is NOT on the Physics equation sheet (8463
Appendix: it is equation 23 of the "recall and apply" list), so it has a triangle and source "none".
The old data's "RP17 (Physics)" label is right for Combined only; 8463 numbers it 5.

The practice set reads the route's `quiz` list (K.bank): five per route, the same on every route,
both old stems kept word for word (so their ks4q: ids survive)."""

_CFQ_PH = ["anything to convert?", "written out", "numbers in", "work it out", "with unit"]


def _q(lines, conv_ph=None):
    """A Ks4Cfifa question's five lines, in the legacy CFQ shape."""
    letters = [("C", "Convert"), ("F", "Formula"), ("I", "Insert"), ("F", "Fine-tune"), ("A", "Answer")]
    ph = list(_CFQ_PH)
    if conv_ph:
        ph[0] = conv_ph
    return [{"letter": l, "label": lab, "placeholder": p, "line": ln}
            for (l, lab), p, ln in zip(letters, ph, lines)]


_RP_BODY = [
    "Use appropriate apparatus to make and record the measurements needed to determine the "
    "densities of regular and irregular solid objects and liquids.",
    "<strong>A regular solid</strong>, such as a cuboid",
    {"points": [
        "Measure its mass on a balance.",
        "Measure its length, width and height with a ruler, Vernier callipers or a micrometer.",
        "Volume = length × width × height.",
    ]},
    "<strong>An irregular solid</strong>, such as a stone",
    {"points": [
        "Measure its mass on a balance.",
        "Find its volume by the displacement method.",
    ]},
    "<strong>A liquid</strong>",
    {"points": [
        "Put an empty measuring cylinder on a balance and set the balance to zero.",
        "Pour in some of the liquid and read its volume.",
        "Read the mass of the liquid from the balance.",
    ]},
    "Work out each density from its mass and volume.",
    "Read a measuring cylinder at eye level, from the bottom of the curved surface (the meniscus).",
]

LESSON = {
    "slug": "density-of-materials",
    "start": {
        "setup": "A 1\u00a0kg bag of feathers and a 1\u00a0kg block of steel sit side by side.",
        "question": "If you had to guess, which one has the greater density?",
        "options": [
            ("The feathers",
             "The steel. Both have the same mass, but the steel takes up far less volume, so more "
             "mass is packed into each cubic metre."),
            ("The steel",
             "The steel. Both have the same mass, but the steel takes up far less volume, so more "
             "mass is packed into each cubic metre."),
        ],
        "answer": 1,
    },
    "words": ["density", "mass", "volume", "displacement"],
    "knowledge": [
        {"kind": "card", "title": "What density means",
         "body": ["Density tells you how much mass is packed into a given volume.",
                  "The density of a material is defined by the equation:",
                  "ρ\u00a0=\u00a0m\u00a0÷\u00a0V",
                  {"points": ["density, ρ, in kilograms per metre cubed (kg/m³)",
                              "mass, m, in kilograms (kg)",
                              "volume, V, in metres cubed (m³)"]},
                  "ρ is the Greek letter rho. You need to remember this equation: it is not on "
                  "the equation sheet.",
                  {"slot": "triangle:EQ_RHO"}]},
        {"kind": "card", "title": "Units",
         "body": ["Keep the units matched: mass in kg with volume in m³ gives kg/m³. Mass in g "
                  "with volume in cm³ gives g/cm³.",
                  {"points": ["1\u00a0kg = 1000\u00a0g",
                              "1\u00a0m³ = 1\u00a0000\u00a0000\u00a0cm³",
                              "1\u00a0g/cm³ = 1000\u00a0kg/m³ (water is 1\u00a0g/cm³, or 1000\u00a0kg/m³)"]}]},
        {"kind": "card", "title": "Density and the particle model",
         "body": [{"slot": "fig:particle-states"},
                  "The particle model can be used to explain the different states of matter and "
                  "the differences in density.",
                  "In a gas the particles are far apart, so the same mass takes up a much bigger "
                  "volume: a much lower density.",
                  "For most substances the solid is a little denser than the liquid. Water is "
                  "different: ice is less dense than water, so it floats."]},
        {"kind": "reveal", "title": "Solid, liquid and gas",
         "cols": ["Solid", "Liquid", "Gas"],
         "rows": [
             ("How close", "Touch\u00ading", "Touch\u00ading", "Far apart"),
             ("Arrange\u00adment", "Regular pattern", "No regular pattern", "Ran\u00addom"),
             ("Move\u00adment", "Vibrate about fixed positions", "Move around each other",
              "Move quickly in all directions"),
             ("Density", "High", "High", "Low"),
         ]},
        {"kind": "card", "title": "When the mass stays the same",
         "body": ["If the mass does not change but the volume does, the density changes.",
                  {"points": [
                      "0.012\u00a0kg of air fills 0.010\u00a0m³. Its density is 0.012 ÷ 0.010 = 1.2\u00a0kg/m³.",
                      "The same air is squeezed into 0.0050\u00a0m³. Its density is 0.012 ÷ 0.0050 = "
                      "2.4\u00a0kg/m³.",
                  ]},
                  "In a change of state the mass stays the same, so the density changes because "
                  "the volume changes."]},
        {"kind": "card", "title": "The displacement method",
         "body": ["An irregular object has no sides to measure, so find its volume from the water "
                  "it pushes aside.",
                  {"slot": "fig:displacement-volume"},
                  {"points": [
                      "Part fill a measuring cylinder with water and read the volume.",
                      "Lower the object into the water on a thread and read the new volume.",
                      "The rise in the volume is the volume of the object.",
                  ]}]},
        {"kind": "card", "title": "Worked examples",
         "body": [{"slot": "cfifa"}]},
        {"kind": "card", "title": "Required practical 17: density", "routes": ["CF", "CH"],
         "body": _RP_BODY},
        {"kind": "card", "title": "Required practical 5: density", "routes": ["TF", "TH"],
         "body": _RP_BODY},
        {"kind": "card", "title": "Easy mistakes",
         "body": [{"mistakes": [
             ("Density = volume ÷ mass.",
              "Density = mass ÷ volume. Mass goes on top."),
             ("Heavy objects are always dense.",
              "A big log is heavy but floats on water, because its density is less than water's."),
             ("Gas particles have no mass.",
              "Gas particles have mass. They are far apart, so a gas has a low density."),
             ("Mass in grams with volume in m³.",
              "Use kg with m³, or g with cm³."),
         ]}]},
    ],
    "key_fact": "Density = mass ÷ volume, measured in kg/m³. Solids and liquids are "
                "dense because their particles are close together. A gas has a low density because "
                "its particles are far apart.",
    "deeper": [
        {"kind": "card", "title": "Floating and sinking",
         "body": ["An object floats on a liquid if its density is less than the liquid's. Ice, at "
                  "about 920\u00a0kg/m³, floats on water at 1000\u00a0kg/m³. A steel block, at about "
                  "7800\u00a0kg/m³, sinks."]},
        {"kind": "card", "title": "A better value",
         "body": [{"points": [
             "Repeat each measurement and take a mean.",
             "Use a measuring cylinder with a scale that fits the volume: a 10\u00a0cm³ cylinder for a "
             "small object.",
             "Knock off any air bubbles stuck to the object, or the volume will read too high.",
         ]}]},
        {"kind": "card", "title": "Command words",
         "body": [{"points": [
             "<strong>Calculate</strong>: convert, write the equation, put the numbers in, "
             "rearrange, then give the answer with its unit.",
             "<strong>Describe</strong> a method: the equipment, what you measure and how, in "
             "order, and how you work out the density.",
             "<strong>Explain</strong>: link the arrangement of the particles to the density.",
         ]}]},
    ],
    "try": None,
    "legacy": None,
    "equations": {
        "EQ_RHO": {"name": "Density", "written": "density = mass ÷ volume",
                   "source": "none",
                   "top": {"s": "m", "name": "mass", "unit": "kg"},
                   "bottom": [{"s": "ρ", "name": "density", "unit": "kg/m³"},
                              {"s": "V", "name": "volume", "unit": "m³"}]},
    },
    "cfifa": {
        "examples": [
            {"tab": "Nothing to convert", "eq": "EQ_RHO", "find": "ρ",
             "head": "A metal block has a mass of 5.4\u00a0kg and a volume of 0.0020\u00a0m³. Calculate its "
                     "density.",
             "steps": [["C", "Convert", "Nothing to convert: kg and m³."],
                       ["F", "Formula", "ρ\u00a0=\u00a0m\u00a0÷\u00a0V"],
                       ["I", "Insert", "ρ = 5.4 ÷ 0.0020"],
                       ["F", "Fine-tune", "ρ = 2700"],
                       ["A", "Answer", "ρ = 2700\u00a0kg/m³"]]},
            {"tab": "Convert first", "eq": "EQ_RHO", "find": "ρ",
             "head": "The stone in the measuring cylinder has a mass of 30\u00a0g and a volume of "
                     "12\u00a0cm³. Calculate its density in kg/m³.",
             "steps": [["C", "Convert", "30\u00a0g ÷ 1000 = 0.030\u00a0kg; 12\u00a0cm³ ÷ 1\u00a0000\u00a0000 = 0.000012\u00a0m³"],
                       ["F", "Formula", "ρ\u00a0=\u00a0m\u00a0÷\u00a0V"],
                       ["I", "Insert", "ρ = 0.030 ÷ 0.000012"],
                       ["F", "Fine-tune", "ρ = 2500"],
                       ["A", "Answer", "ρ = 2500\u00a0kg/m³",
                        "Check in g/cm³: 30 ÷ 12 = 2.5\u00a0g/cm³, and 2.5\u00a0g/cm³ = 2500\u00a0kg/m³."]]},
            {"tab": "Find a mass", "eq": "EQ_RHO", "find": "m",
             "head": "Water has a density of 1000\u00a0kg/m³. Calculate the mass of 0.25\u00a0m³ of water.",
             "steps": [["C", "Convert", "Nothing to convert: kg/m³ and m³."],
                       ["F", "Formula", "ρ\u00a0=\u00a0m\u00a0÷\u00a0V"],
                       ["I", "Insert", "1000 = m ÷ 0.25"],
                       ["F", "Fine-tune", "m = 1000 × 0.25 = 250",
                        "Rearrange: multiply both sides by V."],
                       ["A", "Answer", "m = 250\u00a0kg"]]},
        ],
        "questions": [
            {"tab": "Question 1", "id": "dm-q1",
             "head": "A liquid has a mass of 0.84\u00a0kg and a volume of 0.0010\u00a0m³. Calculate its "
                     "density.",
             "close": "Less than 1000\u00a0kg/m³, so this liquid would float on water.",
             "steps": _q(["Nothing to convert: kg and m³.", "ρ\u00a0=\u00a0m\u00a0÷\u00a0V", "ρ = 0.84 ÷ 0.0010",
                          "ρ = 840", "ρ = 840\u00a0kg/m³"])},
            {"tab": "Question 2", "id": "dm-q2",
             "head": "A metal cube has sides of 2.0 cm. Its mass is 72\u00a0g. Calculate its density "
                     "in g/cm³.",
             "close": "9.0\u00a0g/cm³ is 9000\u00a0kg/m³, about the density of copper.",
             "steps": _q(["Volume = 2.0 × 2.0 × 2.0 = 8.0\u00a0cm³", "ρ\u00a0=\u00a0m\u00a0÷\u00a0V", "ρ = 72 ÷ 8.0",
                          "ρ = 9.0", "ρ = 9.0\u00a0g/cm³"], "the volume first?")},
        ],
    },
    "rungs": {
        "r1": [
            {"kind": "mcq", "command": "State", "marks": 1,
             "prompt": "State the equation that links density, mass and volume.",
             "why": "density = mass ÷ volume, ρ = m ÷ V.",
             "options": [
                 {"text": "density = volume ÷ mass", "correct": False,
                  "reply": "That is upside down. Mass goes on top."},
                 {"text": "density = mass ÷ volume", "correct": True},
                 {"text": "density = mass × volume", "correct": False,
                  "reply": "Density is mass divided by volume, not multiplied."},
             ]},
            {"kind": "mcq", "command": "Identify", "marks": 1,
             "prompt": "Identify the state of matter that has the lowest density for the same "
                       "substance.",
             "why": "In a gas the particles are far apart, so the same mass takes up the biggest "
                    "volume.",
             "options": [
                 {"text": "Solid", "correct": False,
                  "reply": "The particles in a solid are close together, so its density is high."},
                 {"text": "Liquid", "correct": False,
                  "reply": "The particles in a liquid are still close together."},
                 {"text": "Gas", "correct": True},
             ]},
        ],
        "r2": [
            {"kind": "mcq", "command": "Explain", "marks": 2,
             "prompt": "Explain why steam has a much lower density than the same mass of liquid "
                       "water.",
             "why": "The particles in steam are far apart, so the same mass takes up a much bigger "
                    "volume. Density = mass ÷ volume.",
             "options": [
                 {"text": "Its particles are far apart, so the same mass takes up a bigger volume",
                  "correct": True},
                 {"text": "Its particles are much smaller than the particles in liquid water",
                  "correct": False,
                  "reply": "The particles are the same water particles. They are further apart."},
                 {"text": "Its particles have lost most of their mass by turning into a gas",
                  "correct": False,
                  "reply": "Mass is conserved in a change of state. The volume is what changes."},
             ]},
            {"kind": "calc", "command": "Calculate", "marks": 3,
             "prompt": "A stone has a mass of 0.24 kg. It is lowered into a measuring cylinder of "
                       "water, and the reading rises from 40 cm³ to 120 cm³. Calculate the "
                       "density of the stone in kg/m³. Work it on paper, then choose the "
                       "conversion and give the answer and unit.",
             "convOptions": ["Nothing to convert",
                             "Convert the rise in volume to m³: divide by 1 000 000",
                             "Convert the rise in volume to m³: multiply by 1 000 000"],
             "convAnswer": 1, "answer": 3000, "tol": 10, "unit": "kg/m³",
             "units": ["kg/m³", "kg", "m³", "g/cm³"],
             "right": "V = 120 − 40 = 80 cm³ = 0.000080 m³, and ρ = 0.24 ÷ 0.000080 = 3000 kg/m³.",
             "wrong": "The volume of the stone is the rise: 120 − 40 = 80 cm³. Divide by 1 000 000 "
                      "to get 0.000080 m³. Then ρ = m ÷ V.",
             "model": ["C · V = 120 − 40 = 80 cm³; 80 ÷ 1 000 000 = 0.000080 m³",
                       "F · ρ = m ÷ V", "I · ρ = 0.24 ÷ 0.000080",
                       "F · ρ = 3000", "A · ρ = 3000 kg/m³"]},
        ],
        "r3": [
            {"kind": "chain", "command": "Describe", "marks": 3,
             "prompt": "The mass of a stone has been measured. Describe how to find its volume, "
                       "and then its density. Put the links in order.",
             "links": ["Part fill a measuring cylinder with water and read the volume.",
                       "Lower the stone into the water on a thread and read the new volume.",
                       "The rise in the volume is the volume of the stone, so density = mass ÷ "
                       "that volume."],
             "herrings": [{"text": "Measure the stone's length, width and height with a ruler.",
                           "why": "That only works for a regular shape, such as a cuboid."},
                          {"text": "Read the volume from the top of the curved water surface.",
                           "why": "Read from the bottom of the meniscus, at eye level."}]},
            {"kind": "chain", "command": "Explain", "marks": 3,
             "prompt": "Explain why a substance has a much lower density as a gas than as a "
                       "solid. Put the links in order.",
             "links": ["When the substance changes state, its mass stays the same.",
                       "In the gas the particles are far apart, so that same mass takes up a much "
                       "bigger volume.",
                       "Density = mass ÷ volume, so a bigger volume for the same mass gives a "
                       "lower density."],
             "herrings": [{"text": "The particles get bigger when the substance becomes a gas.",
                           "why": "The particles stay the same size. They move further apart."},
                          {"text": "The gas has less mass than the solid.",
                           "why": "Mass is conserved when a substance changes state."}]},
        ],
        "r4": [
            {"kind": "write", "command": "Describe", "marks": 4,
             "prompt": "Describe how to determine the density of a liquid, using a balance and a "
                       "measuring cylinder.",
             "points": ["Put the empty measuring cylinder on the balance and set it to zero (or "
                        "record its mass).",
                        "Pour in some of the liquid and read its volume at eye level, from the "
                        "bottom of the meniscus.",
                        "Read the mass of the liquid from the balance (or subtract the mass of the "
                        "empty cylinder).",
                        "Calculate the density: density = mass ÷ volume.",
                        "Repeat with different volumes of the liquid and find a mean."],
             "reject": ["“Measure the volume with a ruler.” A ruler is for the sides of a "
                        "regular solid.",
                        "“Density = volume ÷ mass.” Mass goes on top."]},
        ],
    },
}
