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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Floats, less dense than water", "correct": True},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p11-01-e05",
        "band": "easier",
        "text": "Density is worked out by…",
        "options": [
            {"text": "dividing the mass by the volume", "correct": True},
            {"text": "dividing the volume by the mass", "correct": False,
             "why": "That is the ratio upside down, and it would be measured "
                    "in cm³ per gram."},
            {"text": "multiplying the mass by the volume", "correct": False,
             "why": "Multiplying gives a much larger number with no useful "
                    "meaning."},
            {"text": "adding the mass to the volume", "correct": False,
             "why": "Grams and cubic centimetres are different quantities and "
                    "cannot be added."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e06",
        "band": "easier",
        "text": "Which unit of volume goes with a mass in grams?",
        "options": [            {"text": "Cubic metres", "correct": False,
             "why": "Cubic metres pair with kilograms; grams go with cubic "
                    "centimetres."},
            {"text": "Kilograms", "correct": False,
             "why": "A kilogram is a mass, and the pair needs a volume."},
            {"text": "Metres", "correct": False,
             "why": "A metre is a length, not a volume."},
            {"text": "Cubic centimetres", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e07",
        "band": "easier",
        "text": "A material has a density of 1.20 g/cm³. Dropped into water, "
                "it…",
        "options": [            {"text": "floats", "correct": False,
             "why": "Floating needs a density below 1.00 g/cm³, and this is "
                    "above it."},
            {"text": "dissolves", "correct": False,
             "why": "Dissolving is a separate matter and has nothing to do "
                    "with density."},
            {"text": "hangs in the middle without moving", "correct": False,
             "why": "That happens only at exactly 1.00 g/cm³, the same as the "
                    "water."},
            {"text": "sinks", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e08",
        "band": "easier",
        "text": "1000 kg/m³ is the same density as…",
        "options": [
            {"text": "1000 g/cm³", "correct": False,
             "why": "That is a million times too dense — denser than any "
                    "material on Earth."},
            {"text": "0.001 g/cm³", "correct": False,
             "why": "That is a thousand times too small, and about the "
                    "density of air."},
            {"text": "1.00 g/cm³", "correct": True},
            {"text": "100 g/cm³", "correct": False,
             "why": "That is a hundred times too dense; the conversion is a "
                    "factor of a thousand."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e09",
        "band": "easier",
        "text": "A block of copper is cut exactly in half. What happens to "
                "the density of each half?",
        "options": [
            {"text": "It halves", "correct": False,
             "why": "Both the mass and the volume halve, so the division "
                    "gives the same answer."},
            {"text": "It doubles", "correct": False,
             "why": "Nothing about cutting makes a material more tightly "
                    "packed."},
            {"text": "It stays the same", "correct": True},
            {"text": "It cannot be worked out until the pieces are weighed "
                     "again",
             "correct": False,
             "why": "Weighing confirms it, but density belongs to the "
                    "material and does not change."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e10",
        "band": "easier",
        "text": "How is the volume of a small irregular stone found?",
        "options": [
            {"text": "By measuring its longest side and cubing it",
             "correct": False,
             "why": "That would only work for a cube, and a stone is not "
                    "one."},
            {"text": "By weighing it on a balance", "correct": False,
             "why": "A balance gives the mass. The volume needs a separate "
                    "measurement."},
            {"text": "By lowering it into water and reading the rise",
             "correct": True},
            {"text": "By dividing its mass by its density", "correct": False,
             "why": "That works only if the density is already known, and "
                    "here it is what you are trying to find."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e11",
        "band": "easier",
        "text": "A sample has a mass of 60 g and a volume of 20 cm³. What is "
                "its density?",
        "options": [
            {"text": "1200 g/cm³", "correct": False,
             "why": "That is 60 × 20; density is the mass DIVIDED by the "
                    "volume."},
            {"text": "0.33 g/cm³", "correct": False,
             "why": "That is 20 ÷ 60, the ratio the wrong way up."},
            {"text": "80 g/cm³", "correct": False,
             "why": "That adds the two, and a mass cannot be added to a "
                    "volume."},
            {"text": "3.0 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e12",
        "band": "easier",
        "text": "Which of these is NOT a unit of density you would use?",
        "options": [
            {"text": "g/cm³", "correct": False,
             "why": "That is the standard pairing for grams and cubic "
                    "centimetres."},
            {"text": "kg/m³", "correct": False,
             "why": "That is the standard pairing for kilograms and cubic "
                    "metres."},
            {"text": "kg/cm³", "correct": True},
            {"text": "g/mL", "correct": False,
             "why": "A millilitre is the same as a cubic centimetre, so this "
                    "is g/cm³ written another way."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e13",
        "band": "easier",
        "text": "Density is a property of…",
        "options": [            {"text": "the object, so a bigger object is denser",
             "correct": False,
             "why": "A bigger object has more mass AND more volume, so the "
                    "division comes out the same."},
            {"text": "how hard the material is", "correct": False,
             "why": "Hardness is a different property; lead is soft and very "
                    "dense."},
            {"text": "how heavy something feels to lift", "correct": False,
             "why": "How heavy it feels is its weight, which depends on how "
                    "much of it there is."},
            {"text": "the material something is made of", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p11-01-s05",
        "band": "standard",
        "text": "A sample has a mass of 150 g and a volume of 60 cm³. What is "
                "its density?",
        "options": [            {"text": "9000 g/cm³", "correct": False,
             "why": "That multiplies the two; density divides."},
            {"text": "210 g/cm³", "correct": False,
             "why": "That adds the mass to the volume, which cannot be done."},
            {"text": "0.40 g/cm³", "correct": False,
             "why": "That is 60 ÷ 150, the division upside down."},
            {"text": "2.5 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s06",
        "band": "standard",
        "text": "A block has a density of 8.0 g/cm³ and a volume of 25 cm³. "
                "What is its mass?",
        "options": [
            {"text": "0.32 g", "correct": False,
             "why": "That is 8.0 ÷ 25, dividing where the rearrangement "
                    "multiplies."},
            {"text": "3.1 g", "correct": False,
             "why": "That is 25 ÷ 8.0, which gives neither a mass nor "
                    "anything usable."},
            {"text": "33 g", "correct": False,
             "why": "That adds the two, and a density cannot be added to a "
                    "volume."},
            {"text": "200 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s07",
        "band": "standard",
        "text": "A liquid of density 1.2 g/cm³ has a mass of 300 g. What "
                "volume does it occupy?",
        "options": [
            {"text": "250 cm³", "correct": True},
            {"text": "360 cm³", "correct": False,
             "why": "That is 300 × 1.2; to find a volume you divide the mass "
                    "by the density."},
            {"text": "0.004 cm³", "correct": False,
             "why": "That is 1.2 ÷ 300, the division the wrong way round."},
            {"text": "301 cm³", "correct": False,
             "why": "That adds the density on, and the two quantities cannot "
                    "be added."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s08",
        "band": "standard",
        "text": "A stone of mass 180 g is lowered into a cylinder and the "
                "level rises from 40 cm³ to 100 cm³. What is its density?",
        "options": [
            {"text": "1.8 g/cm³, using the final reading", "correct": False,
             "why": "The volume is the RISE, which is 60 cm³, not the final "
                    "level of 100 cm³."},
            {"text": "4.5 g/cm³, using the first reading", "correct": False,
             "why": "The first reading is the water alone; the stone's volume "
                    "is the difference."},
            {"text": "3.0 g/cm³", "correct": True},
            {"text": "0.33 g/cm³", "correct": False,
             "why": "That is 60 ÷ 180, the ratio upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s09",
        "band": "standard",
        "text": "Two blocks have exactly the same volume, but one has twice "
                "the mass of the other. Compare their densities.",
        "options": [
            {"text": "The heavier one is twice as dense", "correct": True},
            {"text": "They have the same density, because the volumes match",
             "correct": False,
             "why": "Equal volumes with different masses give different "
                    "densities — that is what the division shows."},
            {"text": "The heavier one is half as dense", "correct": False,
             "why": "More mass in the same space means MORE densely packed, "
                    "not less."},
            {"text": "The lighter one is twice as dense", "correct": False,
             "why": "The lighter block has less mass in the same space, so it "
                    "is the less dense of the two."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s10",
        "band": "standard",
        "text": "Why must a mass in kilograms be converted before it is "
                "divided by a volume in cubic centimetres?",
        "options": [            {"text": "Because kilograms are too large to divide accurately",
             "correct": False,
             "why": "Size is not the difficulty; the pairing of the units "
                    "is."},
            {"text": "Because the answer would come out negative",
             "correct": False,
             "why": "Nothing about mixed units makes an answer negative; it "
                    "makes it meaningless."},
            {"text": "Because cubic centimetres cannot be used for a solid",
             "correct": False,
             "why": "They are used for solids constantly, alongside grams."},
            {"text": "Because the units must be a matched pair, which kg/cm³ "
                     "is not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s11",
        "band": "standard",
        "text": "A cube measures 3.0 cm along each edge and has a mass of "
                "54 g. What is its density?",
        "options": [
            {"text": "18 g/cm³, using 3.0 cm as the volume", "correct": False,
             "why": "3.0 cm is a length. The volume of the cube is 3.0 × 3.0 "
                    "× 3.0."},
            {"text": "6.0 g/cm³, using 9.0 cm² as the volume",
             "correct": False,
             "why": "9.0 cm² is the area of one face; a volume needs all "
                    "three edges."},
            {"text": "2.0 g/cm³", "correct": True},
            {"text": "1458 g/cm³", "correct": False,
             "why": "That multiplies the mass by the volume instead of "
                    "dividing."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s12",
        "band": "standard",
        "text": "A block floats on water. What must be true of its density?",
        "options": [            {"text": "It is greater than 1.00 g/cm³", "correct": False,
             "why": "Anything denser than water sinks in it."},
            {"text": "It cannot be told without knowing the block's mass",
             "correct": False,
             "why": "Floating tells you the density directly, whatever the "
                    "mass happens to be."},
            {"text": "It is exactly 1.00 g/cm³", "correct": False,
             "why": "At exactly that value it hangs level with the surface "
                    "rather than floating on it."},
            {"text": "It is less than 1.00 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s13",
        "band": "standard",
        "text": "Why does the rise in the water level measure a stone's "
                "volume?",
        "options": [
            {"text": "Because water is denser than most stones",
             "correct": False,
             "why": "Most stones are the denser of the two, and it would not "
                    "matter either way."},
            {"text": "Because the stone absorbs its own volume of water as it "
                     "sinks",
             "correct": False,
             "why": "A stone that soaked water up would give a reading that "
                    "was too small."},
            {"text": "Because the water pushed aside fills the stone's space",
             "correct": True},
            {"text": "Because the stone's mass pushes the water up",
             "correct": False,
             "why": "How heavy it is makes no difference; the space it "
                    "occupies is what displaces the water."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p11-01-h05",
        "band": "harder",
        "text": "A block of mass 500 g and volume 250 cm³ is cut into five "
                "equal pieces. What is each piece's density?",
        "options": [            {"text": "2.0 g/cm³, the same as the whole block",
             "correct": True},
            {"text": "0.40 g/cm³, a fifth of the original", "correct": False,
             "why": "Both the mass and the volume are divided by five, so the "
                    "ratio is unchanged."},
            {"text": "10 g/cm³, five times the original", "correct": False,
             "why": "Cutting cannot pack a material more tightly."},
            {"text": "It depends which piece, since they may differ",
             "correct": False,
             "why": "They are the same material throughout, so all five share "
                    "one density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h06",
        "band": "harder",
        "text": "A sample has a mass of 0.50 kg and a volume of 200 cm³. What "
                "is its density in g/cm³?",
        "options": [
            {"text": "0.0025 g/cm³", "correct": False,
             "why": "That divides 0.50 kg by 200 without turning the "
                    "kilograms into grams."},
            {"text": "400 g/cm³", "correct": False,
             "why": "That is 200 ÷ 0.50, which inverts the ratio as well as "
                    "leaving the units mixed."},
            {"text": "100 g/cm³", "correct": False,
             "why": "That multiplies 0.50 by 200 instead of dividing."},
            {"text": "2.5 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h07",
        "band": "harder",
        "text": "Three liquids that do not mix are poured into one jar: "
                "0.79 g/cm³, 1.00 g/cm³ and 1.26 g/cm³. What is the order "
                "from the bottom up?",
        "options": [            {"text": "0.79, then 1.00, then 1.26", "correct": False,
             "why": "That puts the least dense at the bottom; it floats on "
                    "the others instead."},
            {"text": "They mix into one layer of average density",
             "correct": False,
             "why": "The question says they do not mix, so they settle in "
                    "order."},
            {"text": "1.00, then 1.26, then 0.79", "correct": False,
             "why": "1.26 is the densest of the three, so nothing sits below "
                    "it."},
            {"text": "1.26, then 1.00, then 0.79", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h08",
        "band": "harder",
        "text": "A sealed balloon is carried up a mountain and expands. What "
                "happens to the density of the gas inside it?",
        "options": [            {"text": "It falls, because the same mass now fills more space",
             "correct": True},
            {"text": "It rises, because the gas is colder up there",
             "correct": False,
             "why": "Cooling would shrink it; the balloon has grown, so the "
                    "same mass fills more space."},
            {"text": "It stays the same, because no gas has escaped",
             "correct": False,
             "why": "The mass is unchanged, but the volume is not, so the "
                    "division changes."},
            {"text": "It falls, because some of the gas has leaked out",
             "correct": False,
             "why": "The balloon is sealed, so nothing has escaped — the "
                    "volume is what changed."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h09",
        "band": "harder",
        "text": "Why is a gas so much less dense than the same substance as a "
                "liquid?",
        "options": [
            {"text": "Because the particles themselves shrink when it "
                     "evaporates",
             "correct": False,
             "why": "The particles are unchanged; only their spacing is "
                    "different."},
            {"text": "Because there are far fewer particles in a gas",
             "correct": False,
             "why": "Every particle is still there; they are simply spread "
                    "much further apart."},
            {"text": "Because the particles are far further apart, so it "
                     "fills more space",
             "correct": True},
            {"text": "Because a gas has no mass worth measuring",
             "correct": False,
             "why": "A gas certainly has mass — that is why the atmosphere "
                    "presses on us."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h10",
        "band": "harder",
        "text": "Two cubes are made of the same metal, one twice as long "
                "along each edge. How do their masses compare?",
        "options": [
            {"text": "The larger has twice the mass", "correct": False,
             "why": "Doubling every edge multiplies the VOLUME by eight, not "
                    "by two."},
            {"text": "The larger has four times the mass", "correct": False,
             "why": "Four times is what happens to the surface area, not to "
                    "the volume."},
            {"text": "The larger has eight times the mass", "correct": True},
            {"text": "They have the same mass, since it is the same metal",
             "correct": False,
             "why": "The same metal means the same DENSITY, and the larger "
                    "cube holds much more of it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h11",
        "band": "harder",
        "text": "A stone gives 240 g and 80 cm³. A larger stone of the same "
                "rock gives 480 g and 160 cm³. What does that show?",
        "options": [            {"text": "That the larger stone is twice as dense",
             "correct": False,
             "why": "Both come out at 3.0 g/cm³; the mass and the volume have "
                    "doubled together."},
            {"text": "That the larger stone is half as dense", "correct": False,
             "why": "Neither is denser: the ratio is identical for both."},
            {"text": "That one of the two measurements must be wrong",
             "correct": False,
             "why": "Both are entirely consistent, which is exactly the "
                    "point."},
            {"text": "That density belongs to the rock, not to the piece",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h12",
        "band": "harder",
        "text": "A cylinder reads to the nearest 1 cm³ and a small stone "
                "displaces about 5 cm³. Why is that a poor measurement, and "
                "what would fix it?",
        "options": [
            {"text": "The reading is fine, since density does not depend on "
                     "the size of the sample",
             "correct": False,
             "why": "The density does not, but the UNCERTAINTY in this "
                    "measurement of it certainly does."},
            {"text": "The stone is too heavy for the cylinder; use a balance "
                     "instead",
             "correct": False,
             "why": "The balance gives the mass; the cylinder is still needed "
                    "for the volume."},
            {"text": "The uncertainty is a big share of 5 cm³; use a bigger "
                     "stone",
             "correct": True},
            {"text": "Water is the wrong liquid; a denser one would read more "
                     "accurately",
             "correct": False,
             "why": "The rise depends on the stone's volume, not on which "
                    "liquid it is lowered into."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h13",
        "band": "harder",
        "text": "Why is a density in kg/m³ a number a thousand times larger "
                "than the same density in g/cm³?",
        "options": [            {"text": "Because a cubic metre is a million cubic centimetres "
                     "and a kilogram is a thousand grams",
             "correct": True},
            {"text": "Because a kilogram is a thousand grams, and that is the "
                     "whole difference",
             "correct": False,
             "why": "That is half of it; the volume unit changes by a million "
                    "at the same time."},
            {"text": "Because a cubic metre is a hundred cubic centimetres",
             "correct": False,
             "why": "A hundred is the LENGTH conversion; a volume needs it "
                    "cubed, giving a million."},
            {"text": "Because the two are different quantities that happen to "
                     "look alike",
             "correct": False,
             "why": "They are the same quantity in different units, which is "
                    "why one converts into the other."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p11-01-e14",
        "band": "easier",
        "text": "Which of these bench materials floats on water: oak, at "
                "0.65 g/cm³, or gold, at 19.30 g/cm³?",
        "options": [
            {"text": "Oak", "correct": True},
            {"text": "Gold", "correct": False,
             "why": "Gold's density is far above 1.00 g/cm³, so it sinks."},
            {"text": "Both float", "correct": False,
             "why": "Only densities below 1.00 g/cm³ float; gold's is "
                    "nineteen times that."},
            {"text": "Neither floats", "correct": False,
             "why": "Oak's density of 0.65 g/cm³ is below water's, so it does "
                    "float."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e15",
        "band": "easier",
        "text": "Which of these bench materials sinks in water: ice, at "
                "0.92 g/cm³, or iron, at 7.87 g/cm³?",
        "options": [
            {"text": "Ice", "correct": False,
             "why": "0.92 g/cm³ is below water's 1.00, so ice floats rather "
                    "than sinks."},
            {"text": "Iron", "correct": True},
            {"text": "Both sink", "correct": False,
             "why": "Ice's density is below water's, so it floats instead."},
            {"text": "Neither sinks", "correct": False,
             "why": "Iron's density of 7.87 g/cm³ is well above water's, so "
                    "it does sink."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e16",
        "band": "easier",
        "text": "A jeweller weighs a small pebble at 45 g; it takes up 9 cm³ "
                "of space. Work out the pebble's density.",
        "options": [
            {"text": "405 g/cm³", "correct": False,
             "why": "That multiplies the two numbers; density divides mass "
                    "by volume."},
            {"text": "0.20 g/cm³", "correct": False,
             "why": "That is 9 ÷ 45, the division upside down."},
            {"text": "5.0 g/cm³", "correct": True},
            {"text": "36 g/cm³", "correct": False,
             "why": "That subtracts the volume from the mass, and density is "
                    "not found by subtracting."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e17",
        "band": "easier",
        "text": "Osmium, the densest natural element, has a density of about "
                "22.6 g/cm³. Is osmium denser or less dense than gold, at "
                "19.30 g/cm³?",
        "options": [
            {"text": "Less dense, because osmium has a smaller mass number",
             "correct": False,
             "why": "Mass number is not what is being compared here; the two "
                    "densities themselves are."},
            {"text": "The same, because both are metals", "correct": False,
             "why": "Being a metal does not fix a density; the two values "
                    "given are different."},
            {"text": "It cannot be told without knowing the sample sizes",
             "correct": False,
             "why": "Density does not depend on how much of a sample you "
                    "take, so the two numbers compare directly."},
            {"text": "Denser", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e18",
        "band": "easier",
        "text": "Lithium has a density of about 0.53 g/cm³. Based on density "
                "alone, would a lump of lithium float or sink in water?",
        "options": [
            {"text": "Float", "correct": True},
            {"text": "Sink, because all metals sink in water", "correct": False,
             "why": "Not all metals do; a metal below 1.00 g/cm³ floats just "
                    "as any other material would."},
            {"text": "Neither — it hangs halfway down", "correct": False,
             "why": "Hanging in the middle needs a density matching water's "
                    "exactly; 0.53 g/cm³ is below 1.00, so it floats."},
            {"text": "Sink, because 0.53 is a small number", "correct": False,
             "why": "A small number is a low density, and low density is "
                    "exactly what makes something float."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e19",
        "band": "easier",
        "text": "A large iron girder and a small iron nail are cut from the "
                "same batch of iron. Which is denser?",
        "options": [
            {"text": "The girder, because it has a far bigger mass",
             "correct": False,
             "why": "Mass is not density; the girder's much bigger volume "
                    "grows to match, so the ratio stays the same."},
            {"text": "They have the same density", "correct": True},
            {"text": "The nail, because it is more tightly packed into a "
                     "small shape", "correct": False,
             "why": "Cutting a shape smaller does not pack a material's atoms "
                    "any closer together."},
            {"text": "It cannot be told without weighing both", "correct": False,
             "why": "It can — same material, from the same batch, shares one "
                    "density whatever the sizes."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e20",
        "band": "easier",
        "text": "Iron has a density of 7.87 g/cm³. What is the mass of a "
                "1 cm³ sample of it?",
        "options": [
            {"text": "1 g", "correct": False,
             "why": "That ignores the density figure altogether and just uses "
                    "the volume."},
            {"text": "0.13 g", "correct": False,
             "why": "That is 1 ÷ 7.87, the division upside down."},
            {"text": "7.87 g", "correct": True},
            {"text": "7.87 cm³", "correct": False,
             "why": "That keeps the wrong unit; a mass is measured in grams, "
                    "not cubic centimetres."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e21",
        "band": "easier",
        "text": "A cube measures 1 cm along every edge. If its mass is "
                "2.70 g, what is its density?",
        "options": [
            {"text": "0.37 g/cm³", "correct": False,
             "why": "That is 1 ÷ 2.70, the ratio upside down."},
            {"text": "1 g/cm³", "correct": False,
             "why": "That ignores the mass and just uses the volume of the "
                    "cube."},
            {"text": "8.10 g/cm³", "correct": False,
             "why": "That multiplies the mass by the three edge lengths added "
                    "together, 1 + 1 + 1, instead of dividing by the 1 cm³ of "
                    "volume they give."},
            {"text": "2.70 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e22",
        "band": "easier",
        "text": "A certain plastic has been measured at exactly 1.00 g/cm³. "
                "Lowered gently into a bowl of water, what will it do?",
        "options": [
            {"text": "It stays where it is put, neither floating nor sinking",
             "correct": True},
            {"text": "It floats, because 1.00 is a small number",
             "correct": False,
             "why": "1.00 is not below water's own density, so nothing about "
                    "it makes the material float."},
            {"text": "It sinks, because it has some mass", "correct": False,
             "why": "Everything has mass; what decides floating or sinking is "
                    "density, not simply having mass."},
            {"text": "It dissolves into the water", "correct": False,
             "why": "Dissolving is unrelated to matching densities; most "
                    "materials at 1.00 g/cm³ do not dissolve at all."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e23",
        "band": "easier",
        "text": "According to the story, Archimedes solved a density problem "
                "while sitting in a bath. What was the mixed-metal crown's "
                "real problem?",
        "options": [
            {"text": "It weighed more than a pure gold crown of the same "
                     "size", "correct": False,
             "why": "Mixing silver into gold lowers the density, so the same "
                    "size of crown would weigh less, not more."},
            {"text": "It had a slightly bigger volume than a pure gold crown "
                     "of the same mass", "correct": True},
            {"text": "It melted at a lower temperature than pure gold",
             "correct": False,
             "why": "Melting point plays no part in the story; the test used "
                    "mass and volume alone."},
            {"text": "It floated, while a pure gold crown would sink",
             "correct": False,
             "why": "Gold and most metal mixtures are all far denser than "
                    "water, so both crowns would sink."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e24",
        "band": "easier",
        "text": "A block of copper and a block of lead have the same volume. "
                "Which has the greater mass, given that lead is the denser of "
                "the two?",
        "options": [
            {"text": "The copper block", "correct": False,
             "why": "At equal volumes, the denser material is the one that "
                    "packs in more mass."},
            {"text": "Neither — equal volumes always give equal masses",
             "correct": False,
             "why": "Equal volumes give equal masses only when the materials "
                    "are equally dense, and lead and copper are not."},
            {"text": "The lead block", "correct": True},
            {"text": "It cannot be told without knowing both densities "
                     "exactly", "correct": False,
             "why": "Knowing which one is denser is already enough to say "
                    "which has the greater mass at equal volume."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e25",
        "band": "easier",
        "text": "A small clay tile has a mass of 12 g and takes up 4 cm³ of "
                "space. Work out its density.",
        "options": [
            {"text": "48 g/cm³", "correct": False,
             "why": "That multiplies the mass by the volume instead of "
                    "dividing."},
            {"text": "0.33 g/cm³", "correct": False,
             "why": "That is 4 ÷ 12, the division the wrong way up."},
            {"text": "8 g/cm³", "correct": False,
             "why": "That subtracts the volume from the mass, and density is "
                    "a division, not a difference."},
            {"text": "3.0 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e26",
        "band": "easier",
        "text": "Which of these six bench materials has the greatest density: "
                "oak, water, aluminium or gold?",
        "options": [
            {"text": "Gold", "correct": True},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium's 2.70 g/cm³ is far below gold's 19.30."},
            {"text": "Water", "correct": False,
             "why": "Water's 1.00 g/cm³ is the lowest of the four named here "
                    "except oak."},
            {"text": "Oak", "correct": False,
             "why": "Oak is the least dense material on the whole bench, at "
                    "0.65 g/cm³."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e27",
        "band": "easier",
        "text": "A tiny metal pellet takes up 2 cm³ of space and has a "
                "density of 9.0 g/cm³. What mass does the pellet have?",
        "options": [
            {"text": "4.5 g", "correct": False,
             "why": "That is 9.0 ÷ 2, dividing where the rearrangement "
                    "multiplies."},
            {"text": "18 g", "correct": True},
            {"text": "11 g", "correct": False,
             "why": "That adds the volume to the density, and the two cannot "
                    "be added together."},
            {"text": "0.22 g", "correct": False,
             "why": "That is 2 ÷ 9.0, inverted as well as divided instead of "
                    "multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e28",
        "band": "easier",
        "text": "A liquid is poured into a cylinder and 5 cm³ of it has a mass "
                "of 5 g. What is its density?",
        "options": [
            {"text": "25 g/cm³", "correct": False,
             "why": "That multiplies the two numbers instead of dividing."},
            {"text": "0.5 g/cm³", "correct": False,
             "why": "Halving does not follow from these figures; the correct "
                    "division gives a different answer."},
            {"text": "1.0 g/cm³", "correct": True},
            {"text": "10 g/cm³", "correct": False,
             "why": "That adds the two numbers, and density is a division, "
                    "not a sum."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e29",
        "band": "easier",
        "text": "A machined offcut has a mass of 100 g and a density of "
                "4.0 g/cm³. How much space does it take up?",
        "options": [
            {"text": "400 cm³", "correct": False,
             "why": "That multiplies the mass by the density instead of "
                    "dividing."},
            {"text": "0.04 cm³", "correct": False,
             "why": "That is 4.0 ÷ 100, the division the wrong way round."},
            {"text": "96 cm³", "correct": False,
             "why": "That subtracts the density from the mass, and volume is "
                    "found by dividing."},
            {"text": "25 cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-e30",
        "band": "easier",
        "text": "Two blocks are made of the same plastic. Block A has twice "
                "the mass of block B, and twice the volume as well. Compare "
                "their densities.",
        "options": [
            {"text": "They are the same", "correct": True},
            {"text": "Block A is twice as dense", "correct": False,
             "why": "Doubling the mass AND the volume together leaves the "
                    "ratio between them unchanged."},
            {"text": "Block A is half as dense", "correct": False,
             "why": "Nothing here divides the density; both the mass and the "
                    "volume scaled up by the same factor."},
            {"text": "It cannot be told without knowing the actual numbers",
             "correct": False,
             "why": "The actual numbers are not needed — doubling both mass "
                    "and volume together always leaves the ratio the same."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p11-01-s14",
        "band": "standard",
        "text": "A rectangular block measures 5 cm by 4 cm by 2 cm and has a "
                "mass of 200 g. What is its density?",
        "options": [
            {"text": "8000 g/cm³", "correct": False,
             "why": "That multiplies the mass by the volume instead of "
                    "dividing by it."},
            {"text": "5.0 g/cm³", "correct": True},
            {"text": "0.20 g/cm³", "correct": False,
             "why": "That is the volume divided by the mass, the ratio "
                    "upside down."},
            {"text": "18 g/cm³", "correct": False,
             "why": "That adds the three edge lengths, 5 + 4 + 2 = 11, and "
                    "divides by that instead of multiplying them to find the "
                    "volume."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s15",
        "band": "standard",
        "text": "A manufacturer casts two components, A and B, from two "
                "different plastics. Component A weighs the same as component "
                "B, but is moulded into twice the volume. What can be said "
                "about their densities?",
        "options": [
            {"text": "A is twice as dense as B", "correct": False,
             "why": "A bigger volume for the same mass gives a lower "
                    "density, not a higher one."},
            {"text": "Neither — different volumes always mean different "
                     "materials", "correct": False,
             "why": "A volume on its own names no material; two quite "
                    "different plastics can be moulded to any volume you "
                    "like."},
            {"text": "A is half as dense as B", "correct": True},
            {"text": "They are equally dense, since the two weigh the "
                     "same", "correct": False,
             "why": "Equal masses do not give equal densities; A spreads that "
                    "same mass through twice as much space."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s16",
        "band": "standard",
        "text": "A sample of osmium has a volume of 10 cm³. Its density is "
                "about 22.6 g/cm³. What is its approximate mass?",
        "options": [
            {"text": "2.26 g", "correct": False,
             "why": "That is 22.6 ÷ 10, dividing where the rearrangement "
                    "multiplies."},
            {"text": "12.6 g", "correct": False,
             "why": "That subtracts the volume from the density rather than "
                    "multiplying them."},
            {"text": "32.6 g", "correct": False,
             "why": "That adds the volume to the density, and mass is found "
                    "by multiplying, not adding."},
            {"text": "226 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s17",
        "band": "standard",
        "text": "A student measures a stone's mass as 168 g and its volume by "
                "displacement as 60 cm³. What is its density?",
        "options": [
            {"text": "2.8 g/cm³", "correct": True},
            {"text": "0.36 g/cm³", "correct": False,
             "why": "That is 60 ÷ 168, the ratio upside down."},
            {"text": "10 080 g/cm³", "correct": False,
             "why": "That multiplies the two figures; density divides the "
                    "mass by the volume."},
            {"text": "108 g/cm³", "correct": False,
             "why": "That subtracts the volume from the mass, and a density "
                    "is not found by subtracting."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s18",
        "band": "standard",
        "text": "A crown of mass 965 g is suspected of being mixed with "
                "silver rather than pure gold. Pure gold has a density of "
                "19.30 g/cm³. If the crown's volume is measured at 65 cm³, "
                "what does that show?",
        "options": [
            {"text": "It is pure gold, because 965 divides evenly by 65",
             "correct": False,
             "why": "How evenly the numbers divide has no bearing on the "
                    "science; only the resulting density matters."},
            {"text": "It is not pure gold: its density works out at about "
                     "14.8 g/cm³, well below 19.30", "correct": True},
            {"text": "It is pure gold, because the mass is large enough",
             "correct": False,
             "why": "A large mass only means there is a lot of it; the ratio "
                    "to its volume is what a density compares."},
            {"text": "Nothing can be concluded without melting the crown "
                     "down", "correct": False,
             "why": "Nothing needs melting; the mass and volume together are "
                    "already enough to find the density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s19",
        "band": "standard",
        "text": "A bottle holds 250 cm³ of a certain oil, whose density is "
                "0.90 g/cm³. What mass of oil is in the bottle?",
        "options": [
            {"text": "277.8 g", "correct": False,
             "why": "That is 250 ÷ 0.90, the division the wrong way round."},
            {"text": "249.1 g", "correct": False,
             "why": "That subtracts the density from the volume rather than "
                    "multiplying them."},
            {"text": "225 g", "correct": True},
            {"text": "250.9 g", "correct": False,
             "why": "That adds the density to the volume, and a mass is "
                    "found by multiplying, not adding."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s20",
        "band": "standard",
        "text": "Two spheres are cast from the same metal. Sphere A has three "
                "times the volume of sphere B. Compare their masses.",
        "options": [
            {"text": "A has a third of B's mass", "correct": False,
             "why": "A bigger volume of the same material holds more mass, "
                    "not less."},
            {"text": "They are equal, since they are made of the same metal",
             "correct": False,
             "why": "Being the same metal fixes their density, not their "
                    "mass, which still depends on how much of it there is."},
            {"text": "It cannot be told without knowing the density",
             "correct": False,
             "why": "It can — whatever the density, three times the volume "
                    "of the same material gives three times the mass."},
            {"text": "A has three times B's mass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s21",
        "band": "standard",
        "text": "A student converts a mass of 3.4 kg into grams before "
                "dividing by a volume in cm³. Why is that step necessary?",
        "options": [
            {"text": "Because grams pair with cubic centimetres, and "
                     "kilograms do not", "correct": True},
            {"text": "Because kilograms are too large a unit to use in any "
                     "calculation", "correct": False,
             "why": "Size is not the issue; kilograms are used constantly, "
                    "just paired with cubic metres rather than cubic "
                    "centimetres."},
            {"text": "Because the answer would otherwise come out negative",
             "correct": False,
             "why": "Mixing kg with cm³ gives an answer a thousand times too "
                    "small, not a negative one."},
            {"text": "Because a calculator cannot divide by a volume in cm³",
             "correct": False,
             "why": "A calculator divides by any number; the problem is that "
                    "the units would not form a real density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s22",
        "band": "standard",
        "text": "A liquid's density is 0.79 g/cm³. What volume does 158 g of "
                "it occupy?",
        "options": [
            {"text": "124.8 cm³", "correct": False,
             "why": "That multiplies the mass by the density; a volume is "
                    "found by dividing."},
            {"text": "200 cm³", "correct": True},
            {"text": "158.79 cm³", "correct": False,
             "why": "That adds the density onto the mass, and the two cannot "
                    "be added."},
            {"text": "0.005 cm³", "correct": False,
             "why": "That is 0.79 ÷ 158, the division inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s23",
        "band": "standard",
        "text": "A metal sphere weighs in at 540 g and has a density of "
                "9.0 g/cm³. How much space does the sphere occupy?",
        "options": [
            {"text": "4860 cm³", "correct": False,
             "why": "That multiplies the mass by the density instead of "
                    "dividing."},
            {"text": "0.017 cm³", "correct": False,
             "why": "That is 9.0 ÷ 540, the ratio inverted as well as "
                    "dividing the wrong way."},
            {"text": "60 cm³", "correct": True},
            {"text": "531 cm³", "correct": False,
             "why": "That subtracts the density from the mass, and volume is "
                    "found by dividing, not subtracting."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s24",
        "band": "standard",
        "text": "Liquid Q, at 1.05 g/cm³, is poured on top of liquid P, at "
                "0.88 g/cm³, in the same jar, and the two are left to settle. "
                "What happens?",
        "options": [
            {"text": "They stay as poured, with Q remaining on top",
             "correct": False,
             "why": "The denser liquid does not stay on top; it sinks below "
                    "the less dense one once they are left to settle."},
            {"text": "They mix completely into one layer", "correct": False,
             "why": "The two do not mix; each settles into its own layer, "
                    "ordered by density."},
            {"text": "Q rises further, since it was poured second",
             "correct": False,
             "why": "Pouring order makes no difference to the final "
                    "arrangement; density does."},
            {"text": "They swap, with P rising above Q", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s25",
        "band": "standard",
        "text": "A 2.0 kg mass of a liquid occupies 2500 cm³. What is its "
                "density in g/cm³?",
        "options": [
            {"text": "0.80 g/cm³", "correct": True},
            {"text": "1.25 g/cm³", "correct": False,
             "why": "That is 2500 ÷ 2000, the ratio upside down."},
            {"text": "5 000 000 g/cm³", "correct": False,
             "why": "That multiplies the mass in grams by the volume; "
                    "density divides one by the other."},
            {"text": "0.0008 g/cm³", "correct": False,
             "why": "That divides the mass in kilograms directly by the "
                    "volume, without converting to grams first."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s26",
        "band": "standard",
        "text": "A student has a density in kg/m³ and wants it in g/cm³. What "
                "must be done?",
        "options": [
            {"text": "Multiply by 1000", "correct": False,
             "why": "Multiplying by 1000 alone ignores that the volume unit "
                    "is also changing, by a much bigger factor."},
            {"text": "Divide by 1000", "correct": True},
            {"text": "Divide by a million", "correct": False,
             "why": "Dividing by a million alone ignores that the kilograms "
                    "also need converting into grams."},
            {"text": "Leave the number exactly as it is", "correct": False,
             "why": "kg/m³ and g/cm³ are not the same size of unit; the "
                    "number must change to match."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s27",
        "band": "standard",
        "text": "A sample's mass is measured as 88 g and its volume as "
                "40 cm³. A second measurement of the same sample gives 89 g "
                "and 41 cm³. Which pair gives the higher density?",
        "options": [
            {"text": "The second pair, since both its numbers are bigger",
             "correct": False,
             "why": "Bigger numbers alone do not mean a bigger ratio; here "
                    "the second pair's ratio is actually the smaller one."},
            {"text": "Both pairs give exactly the same density",
             "correct": False,
             "why": "88 ÷ 40 and 89 ÷ 41 are not quite equal; they come out "
                    "at 2.20 and about 2.17."},
            {"text": "The first pair", "correct": True},
            {"text": "It cannot be told without repeating the measurement a "
                     "third time", "correct": False,
             "why": "The two densities can be worked out and compared "
                    "directly from the figures already given."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s28",
        "band": "standard",
        "text": "A block of density 6.0 g/cm³ is cut into three equal pieces. "
                "What is the density of each piece?",
        "options": [
            {"text": "2.0 g/cm³", "correct": False,
             "why": "Cutting divides the mass and the volume together, so "
                    "the ratio between them is unchanged, not divided by "
                    "three."},
            {"text": "18 g/cm³", "correct": False,
             "why": "Cutting cannot triple how tightly a material is "
                    "packed."},
            {"text": "It depends which piece is measured", "correct": False,
             "why": "All three pieces are the same material in the same "
                    "state, so all three share one density."},
            {"text": "6.0 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s29",
        "band": "standard",
        "text": "A liquid of unknown density has a mass of 156 g and a "
                "volume of 120 cm³. Which of the bench's six materials is it "
                "closest to?",
        "options": [
            {"text": "Water, at 1.00 g/cm³", "correct": True},
            {"text": "Aluminium, at 2.70 g/cm³", "correct": False,
             "why": "1.30 g/cm³ is far closer to water's 1.00 than to "
                    "aluminium's 2.70."},
            {"text": "Ice, at 0.92 g/cm³", "correct": False,
             "why": "1.30 g/cm³ sits closer to 1.00 than to 0.92, if only "
                    "just."},
            {"text": "Oak, at 0.65 g/cm³", "correct": False,
             "why": "1.30 g/cm³ is roughly double oak's density, and far "
                    "closer to water's."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-s30",
        "band": "standard",
        "text": "A sample has a mass of 217 g and a volume of 31 cm³. Which "
                "of the bench's materials does this most resemble?",
        "options": [
            {"text": "Aluminium, at 2.70 g/cm³", "correct": False,
             "why": "7.0 g/cm³ is far above aluminium's density and much "
                    "closer to iron's."},
            {"text": "Iron, at 7.87 g/cm³", "correct": True},
            {"text": "Gold, at 19.30 g/cm³", "correct": False,
             "why": "7.0 g/cm³ is well below half of gold's density."},
            {"text": "Water, at 1.00 g/cm³", "correct": False,
             "why": "7.0 g/cm³ is seven times water's density, and nowhere "
                    "near it."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p11-01-h14",
        "band": "harder",
        "text": "A crown of mass 900 g is claimed to be pure gold, density "
                "19.30 g/cm³. If the crown really were pure gold, what volume "
                "should it have?",
        "options": [
            {"text": "17 370 cm³", "correct": False,
             "why": "That multiplies the mass by the density instead of "
                    "dividing."},
            {"text": "85.8 cm³", "correct": False,
             "why": "That uses silver's density instead of gold's; this "
                    "version of the question is about a crown that IS pure "
                    "gold."},
            {"text": "About 46.6 cm³", "correct": True},
            {"text": "0.021 cm³", "correct": False,
             "why": "That is the density divided by the mass, the ratio "
                    "inverted."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h15",
        "band": "harder",
        "text": "A student measures a crown's volume as 52 cm³ and its mass "
                "as 900 g. Is the crown consistent with being pure gold, at "
                "19.30 g/cm³?",
        "options": [
            {"text": "Yes, because 900 and 52 are both plausible numbers for "
                     "a crown", "correct": False,
             "why": "Whether the numbers seem plausible says nothing; only "
                    "the density they give matters."},
            {"text": "Yes, because the density comes out close to 19",
             "correct": False,
             "why": "17.3 is noticeably below 19.30, a bigger gap than "
                    "measurement error would explain."},
            {"text": "It cannot be judged without melting the crown down",
             "correct": False,
             "why": "Nothing needs melting; the mass and volume already give "
                    "a density to compare."},
            {"text": "No — its density works out at about 17.3 g/cm³, below "
                     "pure gold's 19.30", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h16",
        "band": "harder",
        "text": "An iron sphere is melted down and recast as a hollow casting "
                "that takes up twice as much room overall, using exactly the "
                "same mass of iron. Iron itself has a density of 7.87 g/cm³. "
                "What is the AVERAGE density of the casting, counting the "
                "empty space inside it?",
        "options": [
            {"text": "About 3.94 g/cm³", "correct": True},
            {"text": "7.87 g/cm³, unchanged", "correct": False,
             "why": "That is the density of the iron itself. The question "
                    "asks for the average across the whole casting, and half "
                    "of that room is now empty space."},
            {"text": "15.74 g/cm³, doubled", "correct": False,
             "why": "Doubling the volume for the same mass halves the "
                    "density; it does not double it."},
            {"text": "2.70 g/cm³, the same as aluminium", "correct": False,
             "why": "The new shape is still iron; nothing here has turned it "
                    "into aluminium."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h17",
        "band": "harder",
        "text": "A liquid mixture is made by combining 100 cm³ of a liquid at "
                "0.80 g/cm³ with 100 cm³ of a liquid at 1.20 g/cm³, and the "
                "two mix completely with no change in total volume. What is "
                "the density of the mixture?",
        "options": [
            {"text": "0.80 g/cm³", "correct": False,
             "why": "That takes only the lighter liquid's density and "
                    "ignores the heavier one entirely."},
            {"text": "1.00 g/cm³", "correct": True},
            {"text": "2.00 g/cm³", "correct": False,
             "why": "That adds the two densities together rather than "
                    "finding the combined mass and volume."},
            {"text": "1.20 g/cm³", "correct": False,
             "why": "That takes only the denser liquid's density and ignores "
                    "the lighter one entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h18",
        "band": "harder",
        "text": "Two identical-sized cubes are tied together by a very light "
                "thread and dropped into water: one cube is oak, at "
                "0.65 g/cm³, and the other is iron, at 7.87 g/cm³. What "
                "happens to the pair?",
        "options": [
            {"text": "They float, because oak floats on its own",
             "correct": False,
             "why": "Tied together, the very dense iron cube outweighs what "
                    "the oak alone could keep afloat."},
            {"text": "The pair hangs level with the surface", "correct": False,
             "why": "That would need the combined density to sit at exactly "
                    "1.00 g/cm³, and iron alone is nearly eight times that."},
            {"text": "They sink together", "correct": True},
            {"text": "Each behaves independently, so one floats while the "
                     "thread stretches", "correct": False,
             "why": "A thread tying them together forces them to move as one "
                    "combined object, not two separate ones."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h19",
        "band": "harder",
        "text": "A perfumer blends 300 cm³ of a carrier oil at 0.75 g/cm³ "
                "with 100 cm³ of a fragrance concentrate at 1.15 g/cm³, and "
                "the two combine with no change in total volume. What is the "
                "density of the finished blend?",
        "options": [
            {"text": "0.95 g/cm³", "correct": False,
             "why": "That averages the two densities equally, ignoring that "
                    "there is three times as much of the lighter liquid."},
            {"text": "1.90 g/cm³", "correct": False,
             "why": "That adds the two densities together rather than "
                    "combining the actual masses and volumes."},
            {"text": "0.75 g/cm³", "correct": False,
             "why": "That takes only the larger liquid's density and ignores "
                    "the smaller one's contribution completely."},
            {"text": "0.85 g/cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h20",
        "band": "harder",
        "text": "A metal ingot weighs 2.4 kg and measures 10 cm by 8 cm by "
                "5 cm. Find its density in g/cm³.",
        "options": [
            {"text": "6.0 g/cm³", "correct": True},
            {"text": "0.17 g/cm³", "correct": False,
             "why": "That is the volume divided by the mass in grams, the "
                    "ratio upside down."},
            {"text": "960 000 g/cm³", "correct": False,
             "why": "That multiplies the mass in grams by the volume instead "
                    "of dividing."},
            {"text": "0.006 g/cm³", "correct": False,
             "why": "That divides the mass in kilograms directly by the "
                    "volume, without converting to grams first."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h21",
        "band": "harder",
        "text": "A cylindrical rod is 20 cm long with a cross-sectional area "
                "of 3 cm², and has a mass of 126 g. What is its density?",
        "options": [
            {"text": "7560 g/cm³", "correct": False,
             "why": "That multiplies the mass by the volume instead of "
                    "dividing."},
            {"text": "2.1 g/cm³", "correct": True},
            {"text": "0.48 g/cm³", "correct": False,
             "why": "That is the volume divided by the mass, the ratio "
                    "upside down."},
            {"text": "42 g/cm³", "correct": False,
             "why": "That divides the mass by the cross-sectional area alone, "
                    "leaving out the length needed to find the volume."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h22",
        "band": "harder",
        "text": "A liquid has a density of 1.05 g/cm³. On warming, its volume "
                "expands slightly while its mass stays exactly the same. "
                "What happens to its density?",
        "options": [
            {"text": "It rises, because warming adds energy to the liquid",
             "correct": False,
             "why": "Adding energy changes how the particles move, not how "
                    "much mass or volume is present at that instant — what "
                    "decides density here is the volume change."},
            {"text": "It stays at 1.05 g/cm³, since the mass has not changed",
             "correct": False,
             "why": "The mass staying fixed does not mean the density is "
                    "fixed too; the volume has grown, and density depends on "
                    "both."},
            {"text": "It falls slightly, because the same mass now fills "
                     "more space", "correct": True},
            {"text": "It cannot be predicted without knowing the new "
                     "temperature exactly", "correct": False,
             "why": "The direction of the change can be told without an "
                    "exact figure — expanding the volume with the mass fixed "
                    "always lowers the density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h23",
        "band": "harder",
        "text": "A metal alloy is made by melting together equal MASSES of "
                "copper, at 8.96 g/cm³, and zinc, at 7.13 g/cm³. Is the "
                "alloy's resulting density closer to copper's, closer to "
                "zinc's, or exactly halfway between the two?",
        "options": [
            {"text": "Closer to copper's density", "correct": False,
             "why": "Equal masses give the less dense metal the bigger "
                    "volume, which pulls the mixture's density toward zinc, "
                    "not copper."},
            {"text": "Exactly halfway between the two", "correct": False,
             "why": "Exactly halfway would only follow from mixing equal "
                    "volumes; here the masses are equal instead, and the "
                    "less dense metal then takes up more of the total "
                    "volume."},
            {"text": "It cannot be judged without knowing the actual masses "
                     "used", "correct": False,
             "why": "The actual mass used does not change which way the "
                    "mixture leans — equal masses always give the less dense "
                    "metal the greater share of the volume."},
            {"text": "Closer to zinc's density", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h24",
        "band": "harder",
        "text": "A solid block has a mass of 60 g. Cut into two unequal "
                "pieces, one piece has a volume of 8 cm³ and a mass of 24 g. "
                "What is the volume of the other piece?",
        "options": [
            {"text": "12 cm³", "correct": True},
            {"text": "8 cm³", "correct": False,
             "why": "That copies the first piece's volume rather than "
                    "working out the second piece's from its own mass."},
            {"text": "20 cm³", "correct": False,
             "why": "That is the volume of the WHOLE block, 60 g ÷ 3 g/cm³; "
                    "the first piece's 8 cm³ still has to be taken off."},
            {"text": "36 cm³", "correct": False,
             "why": "That treats the remaining mass in grams as if it "
                    "already were the volume in cm³."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h25",
        "band": "harder",
        "text": "A hot air balloon's envelope holds 2000 m³ of hot air at a "
                "density of 0.90 kg/m³, while the same volume of the cooler "
                "air outside has a density of 1.20 kg/m³. What is the "
                "difference in mass between the hot air inside and the same "
                "volume of the cold air outside?",
        "options": [
            {"text": "6000 kg", "correct": False,
             "why": "That multiplies the volume by the difference in density "
                    "with an extra factor of ten error."},
            {"text": "600 kg", "correct": True},
            {"text": "1800 kg", "correct": False,
             "why": "That is the mass of the hot air alone, not the "
                    "difference between the two."},
            {"text": "2400 kg", "correct": False,
             "why": "That is the mass of the cold air alone, not the "
                    "difference between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h26",
        "band": "harder",
        "text": "A gemstone is being tested to see whether it is genuine "
                "turquoise (density about 2.6-2.8 g/cm³) or a common glass "
                "imitation (density about 2.4 g/cm³). A sample has a mass of "
                "15 g and a volume of 5.6 cm³. Which is it more likely to "
                "be?",
        "options": [
            {"text": "The glass imitation, because 2.68 is closer to 2.4 "
                     "than the numbers first suggest", "correct": False,
             "why": "2.68 g/cm³ sits inside the range quoted for turquoise "
                    "and well above the glass imitation's typical 2.4."},
            {"text": "It cannot be identified from density alone",
             "correct": False,
             "why": "Here it can — the sample's density falls squarely "
                    "inside turquoise's quoted range and clearly above the "
                    "glass imitation's."},
            {"text": "Genuine turquoise, since 2.68 g/cm³ falls inside its "
                     "quoted range", "correct": True},
            {"text": "Neither — the density is too high for both",
             "correct": False,
             "why": "2.68 g/cm³ is comfortably inside the range quoted for "
                    "turquoise, not above it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h27",
        "band": "harder",
        "text": "A fisherman's lead weight has a mass of 45 g and displaces "
                "4 cm³ of water when lowered into a measuring cylinder. Lead "
                "has a density of about 11.3 g/cm³. Is this weight likely to "
                "be solid lead, or does it have a hollow centre?",
        "options": [
            {"text": "It must be hollow, because the numbers do not match "
                     "exactly", "correct": False,
             "why": "11.25 g/cm³ is close enough to 11.3 to be the same "
                    "material, allowing for ordinary measurement rounding."},
            {"text": "It cannot be judged without weighing it in air as well "
                     "as in water", "correct": False,
             "why": "The mass and the displaced volume already give a "
                    "density close enough to lead's to judge this."},
            {"text": "It must contain gold, since the density is unusually "
                     "high", "correct": False,
             "why": "11.25 g/cm³ is far below gold's 19.30, and matches lead "
                    "closely instead."},
            {"text": "It is consistent with being solid lead, since "
                     "11.25 g/cm³ is very close to 11.3", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h28",
        "band": "harder",
        "text": "A sample's mass and volume are both measured twice, giving "
                "densities of 3.02 g/cm³ and 2.98 g/cm³. What best explains "
                "the small difference between the two results?",
        "options": [
            {"text": "Ordinary measurement uncertainty in reading the "
                     "balance and the cylinder", "correct": True},
            {"text": "The material's density genuinely changed between the "
                     "two measurements", "correct": False,
             "why": "An ordinary solid's density does not drift between two "
                    "measurements taken moments apart; the difference is in "
                    "the readings, not the material."},
            {"text": "The sample must have absorbed water between "
                     "measurements", "correct": False,
             "why": "Nothing here suggests the sample changed at all; small "
                    "differences like this are typical of reading two "
                    "separate instruments."},
            {"text": "One of the two results must be a different substance "
                     "entirely", "correct": False,
             "why": "Two results this close together, on the same sample, "
                    "point to measurement uncertainty rather than to two "
                    "different materials."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h29",
        "band": "harder",
        "text": "A metal bar of density 8.4 g/cm³ is drawn out into a much "
                "longer, thinner wire of exactly the same mass. What happens "
                "to the wire's density compared with the bar's?",
        "options": [
            {"text": "It rises, because the wire is thinner and more "
                     "concentrated", "correct": False,
             "why": "\"Thinner\" is not the same as \"denser\" — the same "
                    "mass has simply been reshaped, and density depends on "
                    "the mass-to-volume ratio, not on shape."},
            {"text": "It stays at 8.4 g/cm³, since the mass and the material "
                     "are unchanged", "correct": True},
            {"text": "It falls, because stretching a shape thinner increases "
                     "its overall volume", "correct": False,
             "why": "Drawing a bar into a wire keeps the metal's total "
                    "volume the same; only its shape changes."},
            {"text": "It cannot be known without measuring the new wire's "
                     "volume directly", "correct": False,
             "why": "It is already known from the reasoning alone — "
                    "reshaping a fixed mass of one material never changes "
                    "its density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-01-h30",
        "band": "harder",
        "text": "A recipe calls for a mixture with an overall density of "
                "exactly 1.50 g/cm³, made by combining equal MASSES of two "
                "liquids: one at 1.00 g/cm³ and one at 2.00 g/cm³. Will "
                "equal masses of these two actually give 1.50 g/cm³?",
        "options": [
            {"text": "Yes, because equal masses always average to the "
                     "midpoint density", "correct": False,
             "why": "Equal masses do not average to the simple midpoint; "
                    "that only happens when equal volumes are combined."},
            {"text": "Yes, because density is unaffected by how the two "
                     "liquids are combined", "correct": False,
             "why": "How the two are combined changes the result — equal "
                    "masses give a different answer from equal volumes."},
            {"text": "No — equal masses give a lower value than 1.50 g/cm³, "
                     "closer to about 1.33", "correct": True},
            {"text": "No — equal masses give a higher value than 1.50 g/cm³",
             "correct": False,
             "why": "Equal masses skew the result toward the less dense "
                    "liquid, which pulls the density down, not up."},
        ],
        "figure": None,
    },
]
