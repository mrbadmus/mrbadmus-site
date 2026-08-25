"""P11 lesson 01 — Density: twelve questions (MRB-223).

Written against Design's page. The pan balance, the six-material league
table and the triangle are hers.

The discriminations, in the order the lesson builds them:

  · a density needs TWO measurements and one division;
  · the units come in matched pairs, and a mismatched pair converts
    first (`PART-16`'s neighbour — the arithmetic half);
  · density belongs to the MATERIAL, so cutting changes nothing
    (`PART-16`) and two samples of one substance share it;
  · heavy is not dense (`PART-14`) and light is not why things float
    (`PART-15`) — the harder band sits on the 1.00 g/cm³ line.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NEITHER MARKED RUNG IS RESTATED: the 240 g stone on 80 cm³ and the
2 kg oak against 50 g of gold are the ladder's, and nothing here reuses
either. `h01` is a mass-and-volume verdict on a crown rather than a
displacement method, which is rung 3's.
"""

UNIT = "P11"
LESSON = "density"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p11-01-e01",
        "band": "easier",
        "text": "What two measurements do you need before you can work out a "
                "density?",
        "options": [
            {"text": "A mass and a volume", "correct": True},
            {"text": "A mass and a temperature", "correct": False,
             "why": "Temperature does change a density a little, but you "
                    "cannot work one out from it. Density is a mass divided "
                    "by a volume."},
            {"text": "A volume and a temperature", "correct": False,
             "why": "A volume on its own says how big something is, not what "
                    "it is made of. You need the mass as well."},
            {"text": "A mass and a weight", "correct": False,
             "why": "Weight is a force, and it is not part of this "
                    "calculation. What is missing is the volume."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e02",
        "band": "easier",
        "text": "Which of these is a real unit of density?",
        "options": [
            {"text": "kg/cm³", "correct": False,
             "why": "Kilograms pair with cubic metres, not with cubic "
                    "centimetres. This is the mismatched pair a question "
                    "makes you convert."},
            {"text": "g/cm³", "correct": True},
            {"text": "g/m³", "correct": False,
             "why": "Grams pair with cubic centimetres. Grams with cubic "
                    "metres is the other mismatched pair."},
            {"text": "cm³/g", "correct": False,
             "why": "That is the division upside down — volume for every "
                    "gram. Density is mass for every cubic centimetre."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e03",
        "band": "easier",
        "text": "A material has a density of 0.80 g/cm³. Dropped into water, "
                "what does it do?",
        "options": [
            {"text": "Sinks, because 0.80 is a small number", "correct": False,
             "why": "Less dense than water is exactly what floats. Below "
                    "1.00 g/cm³ a material floats however big the lump is."},
            {"text": "It depends how big the lump is", "correct": False,
             "why": "Size makes no difference. A cubic centimetre of it is "
                    "lighter than a cubic centimetre of water whatever the "
                    "total volume."},
            {"text": "Floats", "correct": True},
            {"text": "Stays wherever you put it", "correct": False,
             "why": "That happens only at exactly 1.00 g/cm³, which is the "
                    "density of water itself."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e04",
        "band": "easier",
        "text": "Which sentence describes density correctly?",
        "options": [
            {"text": "How heavy an object is", "correct": False,
             "why": "Heavy is about the particular object. A paving slab and "
                    "a chip of the same stone are equally dense, and only one "
                    "of them is heavy."},
            {"text": "How much space an object takes up when you measure it",
             "correct": False,
             "why": "That is the volume. Density is the mass divided by that "
                    "volume."},
            {"text": "How much matter an object contains", "correct": False,
             "why": "That is the mass. Density compares that mass with the "
                    "space it fills."},
            {"text": "How much mass is packed into each unit of volume",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p11-01-s01",
        "band": "standard",
        "text": "A sample of oil has a mass of 92 g and a volume of 115 cm³. "
                "What is its density?",
        "options": [
            {"text": "1.25 g/cm³", "correct": False,
             "why": "That is 115 ÷ 92 — the division the wrong way up. The "
                    "mass goes on top."},
            {"text": "0.80 g/cm³", "correct": True},
            {"text": "10 580 g/cm³", "correct": False,
             "why": "That is 92 × 115. Cover d on the triangle and the mass "
                    "sits over the volume, so you divide."},
            {"text": "23 g/cm³", "correct": False,
             "why": "That is 115 − 92. A density is a division, not a "
                    "difference."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s02",
        "band": "standard",
        "text": "A gold bar and a gold ring are both pure gold. Which "
                "statement is true?",
        "options": [
            {"text": "The bar is denser, because it has more mass",
             "correct": False,
             "why": "More mass in proportionally more volume. The ratio "
                    "between them is what density is, and it has not moved."},
            {"text": "The ring is denser, because the metal in it is packed "
                     "tighter", "correct": False,
             "why": "Nothing has packed it tighter. Both are the same "
                    "material with the same spacing of atoms."},
            {"text": "They have the same density; only the mass and the "
                     "volume differ", "correct": True},
            {"text": "You cannot compare them without weighing both",
             "correct": False,
             "why": "You can. Density belongs to the material, so any two "
                    "samples of pure gold share it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s03",
        "band": "standard",
        "text": "A cube of metal is 2.0 cm along each edge and has a mass of "
                "21.6 g. What is its density?",
        "options": [
            {"text": "10.8 g/cm³ — the mass divided by the edge length",
             "correct": False,
             "why": "The edge is a length, not a volume. Cube it first: "
                    "2.0 × 2.0 × 2.0 = 8.0 cm³."},
            {"text": "172.8 g/cm³ — the mass multiplied by the volume",
             "correct": False,
             "why": "Multiplying gives a number with no meaning. Cover d on "
                    "the triangle and you divide."},
            {"text": "0.37 g/cm³ — the volume divided by the mass",
             "correct": False,
             "why": "That is the division upside down. Density is how much "
                    "mass sits in each cubic centimetre."},
            {"text": "2.70 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s04",
        "band": "standard",
        "text": "A student has a mass in kilograms and a volume in cubic "
                "centimetres, and wants a density in g/cm³. What must they do "
                "first?",
        "options": [
            {"text": "Convert the mass into grams, so it pairs with cm³",
             "correct": True},
            {"text": "Divide straight away and write the answer as kg/cm³",
             "correct": False,
             "why": "There is no such unit as kg/cm³. Kilograms pair with "
                    "cubic metres and grams pair with cubic centimetres."},
            {"text": "Nothing — the units do not matter as long as the "
                     "arithmetic is right", "correct": False,
             "why": "They matter completely. A mass in kilograms over a "
                    "volume in cubic centimetres gives an answer a thousand "
                    "times out."},
            {"text": "Multiply the two together instead of dividing",
             "correct": False,
             "why": "The operation is not the problem. Density is still "
                    "mass ÷ volume; it is the pair of units that has to be "
                    "fixed first."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p11-01-h01",
        "band": "harder",
        "text": "A crown has a mass of 1930 g and a volume of 125 cm³. Pure "
                "gold has a density of 19.30 g/cm³. What can be concluded?",
        "options": [
            {"text": "It is pure gold, because 1930 carries the same digits "
                     "as 19.30", "correct": False,
             "why": "A mass in grams is not a density. Divide by the volume: "
                    "1930 ÷ 125 = 15.44 g/cm³."},
            {"text": "It is pure gold, because that is a large enough mass",
             "correct": False,
             "why": "A big mass only means there is a lot of it. A crown "
                    "twice the size would have twice the mass at the same "
                    "density."},
            {"text": "It is not pure gold: its density is 15.44 g/cm³, well "
                     "below 19.30", "correct": True},
            {"text": "Nothing can be concluded without melting it down",
             "correct": False,
             "why": "Nothing needs melting. A mass and a volume are enough, "
                    "which is the whole point of measuring a density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h02",
        "band": "harder",
        "text": "1.00 g/cm³ is the same density as which of these?",
        "options": [
            {"text": "1 kg/m³", "correct": False,
             "why": "A cubic metre is a million cubic centimetres, so "
                    "1.00 g/cm³ is a thousand kilograms in one."},
            {"text": "100 kg/m³", "correct": False,
             "why": "The factor is a thousand, not a hundred. One cubic metre "
                    "of water has a mass of 1000 kg."},
            {"text": "10 000 kg/m³", "correct": False,
             "why": "That is ten times too big, and it would make water "
                    "denser than iron."},
            {"text": "1000 kg/m³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h03",
        "band": "harder",
        "text": "Two liquids that do not mix are poured into one jar: liquid "
                "A at 0.79 g/cm³ and liquid B at 1.03 g/cm³. What happens?",
        "options": [
            {"text": "A settles on top of B, because A is the less dense of "
                     "the two", "correct": True},
            {"text": "B settles on top of A, because B has the bigger number",
             "correct": False,
             "why": "The bigger number is the denser liquid, and the denser "
                    "one sinks. B ends up underneath."},
            {"text": "They stay wherever they were poured, because both are "
                     "liquids", "correct": False,
             "why": "Being liquid is what lets them move past each other. The "
                    "less dense one rises."},
            {"text": "It depends which one was poured in first",
             "correct": False,
             "why": "It does not. Whichever order they go in, they settle "
                    "with the less dense one on top."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h04",
        "band": "harder",
        "text": "A sealed bag of air is squeezed to half its volume. What "
                "happens to the density of the air inside?",
        "options": [
            {"text": "It halves, because the bag is smaller", "correct": False,
             "why": "The volume halved and the mass did not, so the mass in "
                    "each cubic centimetre went up rather than down."},
            {"text": "It doubles, because the same mass is now in half the "
                     "volume", "correct": True},
            {"text": "It stays the same, because nothing was added or taken "
                     "away", "correct": False,
             "why": "Nothing was added, which is why the mass is unchanged — "
                    "but the volume changed, and density is the ratio of the "
                    "two."},
            {"text": "It cannot be worked out without knowing the mass",
             "correct": False,
             "why": "You do not need the figure. The same mass in half the "
                    "volume is twice the density whatever the mass was."},
        ],
        "figure": None,
    },
]
