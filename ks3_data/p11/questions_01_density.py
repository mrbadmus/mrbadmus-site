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
]
