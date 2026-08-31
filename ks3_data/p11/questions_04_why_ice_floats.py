"""P11 lesson 04 — Why ice floats: twelve questions (MRB-223).

Written against Design's page. The glass of ice cubes, the four
substances weighed as a solid and as their own melt, and the comparison
line at 1.00 g/cm³ are hers.

The discriminations, in the order the lesson builds them:

  · the two densities, and which way round they go;
  · what happens to almost EVERY other substance, which is what makes
    water the exception worth a lesson;
  · why the expansion happens — bigger gaps, not bigger molecules
    (`PART-03` re-confronted);
  · what follows for a pond, and for anything sealed and full of water.

⚠️ POSITION IS AUTHORED — 0,1,2,3 · 1,2,3,0 · 2,3,0,1, three of each.

⚠️ NEITHER MARKED RUNG IS RESTATED: the iceberg's 8% and "cold things
float" are the ladder's. `h04` asks what the fraction DEPENDS ON rather
than what it is, which is the one place the two are adjacent, and `h03`
is the counterfactual her rung 4 asks a student to write rather than
choose.
"""

UNIT = "P11"
LESSON = "why-ice-floats"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p11-04-e01",
        "band": "easier",
        "text": "How does the density of ice compare with the density of "
                "liquid water?",
        "options": [
            {"text": "Less: 0.92 g/cm³ against 1.00", "correct": True},
            {"text": "More: 1.08 g/cm³ against 1.00", "correct": False,
             "why": "If ice were the denser of the two it would sink, and ice "
                    "cubes float."},
            {"text": "Exactly the same, 1.00 g/cm³", "correct": False,
             "why": "Then it would neither float nor sink. Ice sits with a "
                    "dome above the surface."},
            {"text": "It depends how cold the ice is", "correct": False,
             "why": "Ice does change very slightly with temperature, nothing "
                    "like enough to change the answer. It is about 0.92 "
                    "throughout."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e02",
        "band": "easier",
        "text": "What happens to most substances when they freeze?",
        "options": [
            {"text": "They expand as they freeze, just as water does",
             "correct": False,
             "why": "Water is the exception, not the rule. Almost everything "
                    "else contracts."},
            {"text": "They contract, so the solid is denser than the liquid",
             "correct": True},
            {"text": "Their mass goes down as the particles pack in",
             "correct": False,
             "why": "Nothing is lost. The same particles are there before and "
                    "after, however closely they pack."},
            {"text": "Their density stays the same as the liquid's",
             "correct": False,
             "why": "The particles settle closer together, so the same mass "
                    "takes up less room."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e03",
        "band": "easier",
        "text": "Roughly how much does water expand when it freezes?",
        "options": [
            {"text": "About 50%", "correct": False,
             "why": "Far too much. An ice cube is not half as big again as "
                    "the water it came from."},
            {"text": "About 1%", "correct": False,
             "why": "Too little to split a bottle. The figure is closer to a "
                    "tenth."},
            {"text": "About 9%", "correct": True},
            {"text": "It does not expand at all", "correct": False,
             "why": "It does, and that is why a full bottle of water splits "
                    "in a freezer."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e04",
        "band": "easier",
        "text": "Why does a pond freeze from the top down?",
        "options": [
            {"text": "Because the bottom is kept warm by the ground beneath "
                     "it", "correct": False,
             "why": "The ground helps a little. What keeps the ice on top is "
                    "that it is less dense than the water."},
            {"text": "Because the cold air pushes the ice downwards as soon "
                     "as it forms", "correct": False,
             "why": "Air does not push ice down. The ice stays up because it "
                    "floats."},
            {"text": "Because the water at the bottom is saltier and freezes "
                     "last", "correct": False,
             "why": "A freshwater pond is not salty at the bottom. What "
                    "decides it is density."},
            {"text": "Because ice forms at the surface and floats there "
                     "instead of sinking", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p11-04-s01",
        "band": "standard",
        "text": "Liquid water is at its densest at which temperature?",
        "options": [
            {"text": "0 °C, just as it freezes", "correct": False,
             "why": "Between 0 °C and 4 °C water expands as it cools, so "
                    "0 °C is not the densest it gets."},
            {"text": "About 4 °C", "correct": True},
            {"text": "100 °C, just as it boils", "correct": False,
             "why": "Water expands as it warms above 4 °C, so it is at its "
                    "least dense near boiling."},
            {"text": "Water has the same density at every temperature",
             "correct": False,
             "why": "It does not, and the narrow band between 0 °C and 4 °C "
                    "is the whole reason a pond survives a winter."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s02",
        "band": "standard",
        "text": "A lump of solid candle wax is dropped into melted wax at the "
                "same temperature. What happens?",
        "options": [
            {"text": "It floats, the way ice floats on top of water",
             "correct": False,
             "why": "Wax is an ordinary substance: the solid is denser than "
                    "the melt, so it sinks."},
            {"text": "It stays put, because both of them are wax",
             "correct": False,
             "why": "Being the same substance does not make the two densities "
                    "equal. Solid wax is about 0.93 and the melt about "
                    "0.90."},
            {"text": "It sinks, because solid wax is denser than melted wax",
             "correct": True},
            {"text": "It dissolves into the melt straight away",
             "correct": False,
             "why": "It melts rather than dissolves, and while it is still "
                    "solid it sinks."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s03",
        "band": "standard",
        "text": "What causes water to expand as it freezes?",
        "options": [
            {"text": "The molecules themselves get bigger as they cool",
             "correct": False,
             "why": "The molecules are exactly the same size before and "
                    "after. What changes is how far apart they sit."},
            {"text": "Air gets trapped between the molecules and pushes them "
                     "apart", "correct": False,
             "why": "Pure bubble-free ice still floats. The expansion happens "
                    "with no air at all."},
            {"text": "The molecules gain mass as they cool and take up more "
                     "room", "correct": False,
             "why": "Nothing gains mass. The volume does grow, but the mass "
                    "is exactly the same before and after."},
            {"text": "The molecules lock into an open cage that holds them "
                     "further apart", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s04",
        "band": "standard",
        "text": "A sealed glass bottle is filled to the brim with water and "
                "left in a freezer. What is the risk?",
        "options": [
            {"text": "The water expands as it freezes and can split the "
                     "bottle", "correct": True},
            {"text": "The water contracts and pulls the bottle inwards",
             "correct": False,
             "why": "Water expands on freezing. Almost every other substance "
                    "would contract."},
            {"text": "Nothing, because sealing it holds the water in place",
             "correct": False,
             "why": "Sealing it is what causes the problem. The ice needs "
                    "about 9% more room and the glass cannot give it."},
            {"text": "The glass melts where the ice presses against it",
             "correct": False,
             "why": "A freezer is nowhere near hot enough to melt glass. What "
                    "breaks it is the ice pushing outwards."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p11-04-h01",
        "band": "harder",
        "text": "Solid iron has a density of 7.87 g/cm³ and molten iron "
                "6.98 g/cm³. What happens to a lump of solid iron dropped "
                "into the melt?",
        "options": [
            {"text": "It floats, because 7.87 is the bigger number",
             "correct": False,
             "why": "The bigger number is the denser one, and the denser one "
                    "sinks."},
            {"text": "It floats, because a solid always floats on its own "
                     "liquid", "correct": False,
             "why": "Water is the only common substance where that happens. "
                    "Three of the four on the bench sink."},
            {"text": "It sinks, because the solid is the denser of the two",
             "correct": True},
            {"text": "It stays wherever it is put, because both are iron",
             "correct": False,
             "why": "One substance, two different densities. The denser one "
                    "goes to the bottom."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h02",
        "band": "harder",
        "text": "Why does the layer of ice on a pond help the fish under it?",
        "options": [
            {"text": "The ice makes new energy as it forms, and that warms "
                     "the water below", "correct": False,
             "why": "Nothing makes energy. Freezing releases energy the water "
                    "already had, and it does not warm the pond."},
            {"text": "The ice lets the cold air through to the water below "
                     "it", "correct": False,
             "why": "It does the opposite — it gets in the way, which is what "
                    "protects the water."},
            {"text": "The ice holds the water below at exactly 0 °C all "
                     "winter", "correct": False,
             "why": "The water below is generally a little warmer than 0 °C, "
                    "with the densest water at 4 °C at the bottom."},
            {"text": "The ice insulates the water below, so the pond does not "
                     "freeze solid", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h03",
        "band": "harder",
        "text": "Suppose ice were denser than liquid water. What would happen "
                "to a pond in a hard winter?",
        "options": [
            {"text": "The ice would sink, a new layer would freeze on top, "
                     "and the pond would freeze solid", "correct": True},
            {"text": "Nothing would change, because the ice would still form "
                     "at the surface", "correct": False,
             "why": "It would form at the surface and then sink, leaving the "
                    "surface bare to freeze again."},
            {"text": "The pond would freeze from the bottom upwards only, "
                     "and the top would stay liquid", "correct": False,
             "why": "The freezing still starts where the water meets the cold "
                    "air, which is at the top."},
            {"text": "The pond would not freeze at all, because the ice would "
                     "sink out of the way", "correct": False,
             "why": "It would freeze more thoroughly, not less: nothing would "
                    "be left floating to insulate the water."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h04",
        "band": "harder",
        "text": "An iceberg floats with most of its volume below the surface. "
                "What sets that fraction?",
        "options": [
            {"text": "The temperature of the sea", "correct": False,
             "why": "Temperature changes both densities very slightly. What "
                    "sets the fraction is the ratio between them."},
            {"text": "The ratio of the density of ice to the density of the "
                     "water it floats in", "correct": True},
            {"text": "The mass of the iceberg, because a heavier one sits "
                     "lower in the water", "correct": False,
             "why": "A bigger iceberg pushes aside more water in the same "
                    "proportion, so the fraction does not change with size."},
            {"text": "The shape of the iceberg", "correct": False,
             "why": "Shape decides which way up it sits, not what fraction of "
                    "it is under the water."},
        ],
        "figure": None,
    },
]
