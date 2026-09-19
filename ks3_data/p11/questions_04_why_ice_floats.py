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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p11-04-e05",
        "band": "easier",
        "text": "The density of ice is about…",
        "options": [
            {"text": "0.92 g/cm³", "correct": True},
            {"text": "1.00 g/cm³", "correct": False,
             "why": "That is the density of liquid water; ice is a little "
                    "less."},
            {"text": "1.09 g/cm³", "correct": False,
             "why": "That would be denser than water, and ice would sink."},
            {"text": "0.09 g/cm³", "correct": False,
             "why": "That is ten times too small — an iceberg would sit "
                    "almost entirely above the surface."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e06",
        "band": "easier",
        "text": "Water expands on freezing by about…",
        "options": [
            {"text": "0.9%", "correct": False,
             "why": "That is ten times too small to burst a pipe or float an "
                    "iceberg the way ice does."},
            {"text": "9%", "correct": True},
            {"text": "50%", "correct": False,
             "why": "That would make ice about half the density of water, and "
                    "icebergs would ride far higher."},
            {"text": "90%", "correct": False,
             "why": "Ice would be almost as light as air, which it plainly is "
                    "not."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e07",
        "band": "easier",
        "text": "When almost any substance freezes, it becomes…",
        "options": [
            {"text": "less dense than its own liquid", "correct": False,
             "why": "That is water's odd behaviour, and it is the exception "
                    "rather than the rule."},
            {"text": "denser than its own liquid", "correct": True},
            {"text": "exactly as dense as its own liquid", "correct": False,
             "why": "The particles pack closer on freezing, so the density "
                    "changes."},
            {"text": "lighter, because cold things weigh less",
             "correct": False,
             "why": "Cooling does not change a mass; it changes the volume it "
                    "occupies."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e08",
        "band": "easier",
        "text": "A lump of solid candle wax is dropped into melted wax at the "
                "same temperature. What does it do?",
        "options": [
            {"text": "Floats, like ice on water", "correct": False,
             "why": "Wax follows the normal rule: its solid is denser than "
                    "its liquid."},
            {"text": "Sinks straight to the bottom", "correct": True},
            {"text": "Hangs level, halfway down", "correct": False,
             "why": "That would need the two densities to be identical, and "
                    "they are not."},
            {"text": "Melts instantly and mixes in", "correct": False,
             "why": "Both are at the same temperature, so nothing drives it "
                    "to melt."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e09",
        "band": "easier",
        "text": "Which substance is unusual in being LESS dense as a solid "
                "than as a liquid?",
        "options": [
            {"text": "Iron", "correct": False,
             "why": "Solid iron sinks in molten iron, following the normal "
                    "rule."},
            {"text": "Wax", "correct": False,
             "why": "Solid wax sinks in melted wax, as most solids do in "
                    "their own melt."},
            {"text": "Water", "correct": True},
            {"text": "Lead", "correct": False,
             "why": "Solid lead is denser than molten lead and sinks in it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e10",
        "band": "easier",
        "text": "As water freezes, its molecules lock into a structure that "
                "is…",
        "options": [
            {"text": "packed tighter than in the liquid", "correct": False,
             "why": "Tighter packing would make ice denser, and it sinks in "
                    "that case."},
            {"text": "open and six-sided, holding them further apart",
             "correct": True},
            {"text": "completely random, like a liquid", "correct": False,
             "why": "A solid's particles are in a fixed arrangement, not a "
                    "random one."},
            {"text": "the same as in the liquid, only colder", "correct": False,
             "why": "If nothing changed about the arrangement, the density "
                    "would not change either."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e11",
        "band": "easier",
        "text": "Roughly what fraction of a floating iceberg is BELOW the "
                "surface?",
        "options": [
            {"text": "About 8%", "correct": False,
             "why": "That is the fraction ABOVE the surface, which is what is "
                    "left over."},
            {"text": "About 50%", "correct": False,
             "why": "Half and half would need ice to be half water's density, "
                    "and it is 0.92."},
            {"text": "About 92%", "correct": True},
            {"text": "All of it", "correct": False,
             "why": "A fully submerged berg would not be floating at all."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e12",
        "band": "easier",
        "text": "Freeze–thaw weathering breaks rock apart because water in a "
                "crack…",
        "options": [
            {"text": "dissolves the rock as it freezes", "correct": False,
             "why": "Dissolving is a chemical effect; this one is the water "
                    "pushing the crack wider."},
            {"text": "expands as it freezes and widens the crack",
             "correct": True},
            {"text": "shrinks as it freezes and pulls the crack open",
             "correct": False,
             "why": "Shrinking would leave a gap and pull nothing; water "
                    "expands on freezing."},
            {"text": "makes the rock softer as it warms", "correct": False,
             "why": "Rock does not soften at those temperatures; the ice does "
                    "the work."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e13",
        "band": "easier",
        "text": "A glass bottle filled to the brim with water is left in a "
                "freezer. What may happen?",
        "options": [
            {"text": "Nothing, because water shrinks as it freezes",
             "correct": False,
             "why": "Water is the exception: it expands, which is what "
                    "threatens the bottle."},
            {"text": "It splits as the ice expands", "correct": True},
            {"text": "The water leaks out through the glass", "correct": False,
             "why": "Glass does not let water through; the pressure of the "
                    "expanding ice is the danger."},
            {"text": "The bottle shrinks around the ice", "correct": False,
             "why": "The glass barely changes size, and the ice pushes "
                    "outwards against it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p11-04-s05",
        "band": "standard",
        "text": "What is anomalous about water between 0 °C and 4 °C?",
        "options": [
            {"text": "It freezes and melts at the same time", "correct": False,
             "why": "It is liquid throughout that range; the oddity is what "
                    "its volume does."},
            {"text": "Cooling it makes it expand instead of contract",
             "correct": True},
            {"text": "It boils at a lower temperature than usual",
             "correct": False,
             "why": "Boiling is nowhere near this range; the anomaly is about "
                    "density."},
            {"text": "It stops conducting energy altogether", "correct": False,
             "why": "It conducts as usual; the change is in how tightly it "
                    "packs."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s06",
        "band": "standard",
        "text": "Solid lead is denser than molten lead. What happens to a "
                "lump of solid lead dropped into molten lead?",
        "options": [
            {"text": "It floats, as ice does on water", "correct": False,
             "why": "Ice is the exception; lead follows the ordinary rule and "
                    "sinks."},
            {"text": "It sinks, as most solids do", "correct": True},
            {"text": "It hangs level with the surface", "correct": False,
             "why": "That needs the two densities to be equal, and they are "
                    "not."},
            {"text": "It expands and then floats", "correct": False,
             "why": "Solid lead does not expand on being placed in its own "
                    "melt."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s07",
        "band": "standard",
        "text": "Why does ice float with MOST of itself below the surface?",
        "options": [
            {"text": "Because ice is much less dense than water",
             "correct": False,
             "why": "It is only a little less dense — 0.92 against 1.00 — "
                    "which is why so much sits under."},
            {"text": "Because its density is only a little below water's",
             "correct": True},
            {"text": "Because water pushes down on the top of it",
             "correct": False,
             "why": "The water pushes UP on it; that is what holds it "
                    "afloat."},
            {"text": "Because ice absorbs water as it floats", "correct": False,
             "why": "It does not soak anything up; the fraction is set by the "
                    "two densities."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s08",
        "band": "standard",
        "text": "A bottle of cooking oil left in the freezer does not split. "
                "Why not?",
        "options": [
            {"text": "Because oil never becomes solid", "correct": False,
             "why": "It does thicken and set; what matters is that it "
                    "contracts as it does."},
            {"text": "Because oil contracts as it solidifies, like most "
                     "substances",
             "correct": True},
            {"text": "Because oil is less dense than water", "correct": False,
             "why": "It is, but that is about floating rather than about "
                    "bursting a bottle."},
            {"text": "Because oil freezes at a far lower temperature than "
                     "water ever does",
             "correct": False,
             "why": "Even when it does set, it takes up less space rather "
                    "than more."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s09",
        "band": "standard",
        "text": "Why is saying ice floats because it is lighter a poor "
                "answer?",
        "options": [
            {"text": "Because ice is actually heavier than water",
             "correct": False,
             "why": "A given volume of ice IS lighter; the trouble is the "
                    "word rather than the fact."},
            {"text": "Because a berg outweighs a cup of water; density "
                     "decides",
             "correct": True},
            {"text": "Because floating has nothing at all to do with an "
                     "object's weight",
             "correct": False,
             "why": "Weight is one of the two forces involved; it is comparing "
                    "raw weights that fails."},
            {"text": "Because ice and water weigh exactly the same",
             "correct": False,
             "why": "That depends entirely on how much of each you take, "
                    "which is the point."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s10",
        "band": "standard",
        "text": "A student says cold things float on warm things, which is "
                "why ice sits on top. What is right?",
        "options": [
            {"text": "They are right — cold water always rises",
             "correct": False,
             "why": "Cold water sinks, right down to 4 °C, which is the "
                    "opposite of the claim."},
            {"text": "Being cold is not what floats it; being less dense is",
             "correct": True},
            {"text": "They are right, but only for water", "correct": False,
             "why": "It is not right for water either: the ice floats because "
                    "of its density."},
            {"text": "Temperature decides it, and 0 °C is the floating point",
             "correct": False,
             "why": "Water at 1 °C does not float on water at 5 °C; density "
                    "is what settles it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s11",
        "band": "standard",
        "text": "A sealed metal pipe full of water freezes and bursts. What "
                "has happened?",
        "options": [
            {"text": "The ice contracted and pulled the pipe apart",
             "correct": False,
             "why": "Contracting would leave a gap, not split the walls."},
            {"text": "The water expanded on freezing and had nowhere to go",
             "correct": True},
            {"text": "The metal shrank in the cold and crushed the ice",
             "correct": False,
             "why": "The metal does contract slightly, but the pipe splits "
                    "outwards under the ice."},
            {"text": "The water dissolved the pipe from the inside",
             "correct": False,
             "why": "The failure is sudden and mechanical, not a slow "
                    "chemical one."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s12",
        "band": "standard",
        "text": "What happens to the density of water as it is cooled from "
                "20 °C to 4 °C?",
        "options": [
            {"text": "It falls steadily", "correct": False,
             "why": "It rises over this range; the fall only begins below "
                    "4 °C."},
            {"text": "It rises", "correct": True},
            {"text": "It stays exactly the same", "correct": False,
             "why": "It changes measurably, which is why 4 °C is worth "
                    "naming."},
            {"text": "It rises and then falls again before 4 °C",
             "correct": False,
             "why": "The turning point is at 4 °C itself, not before it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s13",
        "band": "standard",
        "text": "Why does the coldest water in a deep pond NOT sit at the "
                "bottom in winter?",
        "options": [
            {"text": "Because cold water always rises", "correct": False,
             "why": "It sinks down to 4 °C; only below that does it become "
                    "less dense again."},
            {"text": "Because water is densest at 4 °C, so colder water sits "
                     "above it",
             "correct": True},
            {"text": "Because the bottom of a pond is warmed by the ground",
             "correct": False,
             "why": "Some warmth comes from below, but the layering follows "
                    "from water's density curve."},
            {"text": "Because ice at the surface stops the water mixing",
             "correct": False,
             "why": "The layering is there before any ice forms, and density "
                    "is what causes it."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p11-04-h05",
        "band": "harder",
        "text": "A block of ice of volume 1000 cm³ melts completely. What "
                "volume of water does it give?",
        "options": [
            {"text": "1000 cm³, since nothing has been added or taken away",
             "correct": False,
             "why": "The mass is unchanged, but water is denser, so it takes "
                    "up less room."},
            {"text": "920 cm³", "correct": True},
            {"text": "1090 cm³", "correct": False,
             "why": "That is larger than the ice, and melting makes water "
                    "take up LESS space."},
            {"text": "92 cm³", "correct": False,
             "why": "That is ten times too small — a check on the order of "
                    "magnitude catches it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h06",
        "band": "harder",
        "text": "Why is it wrong to treat water expanding on freezing and "
                "water expanding on heating as the same effect?",
        "options": [
            {"text": "Because water does not expand on heating at all",
             "correct": False,
             "why": "It does, above 4 °C, which is why the two are easy to "
                    "run together."},
            {"text": "Because the freezing expansion comes from the open "
                     "structure the molecules lock into",
             "correct": True},
            {"text": "Because only the freezing one is real; the other is a "
                     "measurement error",
             "correct": False,
             "why": "Both are real and both are measured routinely."},
            {"text": "Because the molecules themselves get bigger in one case "
                     "and not the other",
             "correct": False,
             "why": "The molecules never change size; only their arrangement "
                    "and spacing do."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h07",
        "band": "harder",
        "text": "Why does a British pond almost never freeze solid to the "
                "bottom?",
        "options": [
            {"text": "Because the water below the ice is warmed by the fish "
                     "in it",
             "correct": False,
             "why": "Fish add a negligible amount; the ice layer and the "
                    "layering of the water do the work."},
            {"text": "Because the ice layer insulates the water below, which "
                     "stays near 4 °C",
             "correct": True},
            {"text": "Because moving water cannot freeze", "correct": False,
             "why": "Still ponds freeze at the surface readily; movement is "
                    "not what saves the depths."},
            {"text": "Because ice forms at the bottom first and stops the "
                     "rest",
             "correct": False,
             "why": "Ice floats, so it forms at the top — which is the "
                    "starting point of the whole answer."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h08",
        "band": "harder",
        "text": "Why does an iceberg sit slightly higher in sea water than in "
                "fresh water?",
        "options": [
            {"text": "Because salt water is denser, so less of the berg has "
                     "to be submerged",
             "correct": True},
            {"text": "Because salt water is colder, so the ice expands",
             "correct": False,
             "why": "Temperature is not what sets the fraction; the two "
                    "densities are."},
            {"text": "Because salt makes the ice lighter", "correct": False,
             "why": "The berg is unchanged; it is the water round it that is "
                    "denser."},
            {"text": "Because salt water pushes upwards with a fixed force "
                     "whatever floats in it",
             "correct": False,
             "why": "The upward push always matches the berg's weight; what "
                    "changes is how much water that takes."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h09",
        "band": "harder",
        "text": "Freeze–thaw weathering shapes mountains but does little in a "
                "hot dry desert. Why?",
        "options": [
            {"text": "Because desert rock is harder", "correct": False,
             "why": "Rock hardness varies everywhere; what is missing is one "
                    "of the ingredients."},
            {"text": "Because there is little water to get into cracks and "
                     "freeze",
             "correct": True},
            {"text": "Because deserts never get cold enough at night",
             "correct": False,
             "why": "Many deserts drop below freezing; it is the water that "
                    "is absent."},
            {"text": "Because blown sand fills up the cracks and holds them "
                     "tightly shut",
             "correct": False,
             "why": "Sand in a crack does not stop ice forming; the lack of "
                    "water does."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h10",
        "band": "harder",
        "text": "A student says the water molecules themselves expand when "
                "water freezes. Correct them.",
        "options": [
            {"text": "They are right — that is exactly why the ice takes up "
                     "more room than water",
             "correct": False,
             "why": "A molecule keeps its size through every change of state; "
                    "only the arrangement alters."},
            {"text": "The molecules are unchanged; they lock into an open "
                     "arrangement",
             "correct": True},
            {"text": "The molecules shrink, which is why there are gaps",
             "correct": False,
             "why": "They do not shrink either; the gaps come from how they "
                    "are arranged."},
            {"text": "The molecules split apart into atoms as ice forms",
             "correct": False,
             "why": "Freezing is a physical change; no molecule is broken "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h11",
        "band": "harder",
        "text": "A sealed bottle only half full of water does not split in a "
                "freezer. Why not?",
        "options": [
            {"text": "Because half as much water expands by half as much, "
                     "which the glass can take",
             "correct": False,
             "why": "Even a small expansion would burst a full sealed bottle; "
                    "the empty space is what saves it."},
            {"text": "Because there is space above the water for the ice to "
                     "expand into",
             "correct": True},
            {"text": "Because water only expands when a container is "
                     "completely full",
             "correct": False,
             "why": "It expands by the same fraction either way; the room to "
                    "do it is what differs."},
            {"text": "Because the air above the water keeps it from freezing",
             "correct": False,
             "why": "It freezes perfectly well; the air simply gets out of "
                    "the way."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h12",
        "band": "harder",
        "text": "If ice were denser than liquid water, what would happen to a "
                "pond over a hard winter?",
        "options": [
            {"text": "Nothing would change, since the surface would still "
                     "freeze first",
             "correct": False,
             "why": "The ice would sink as it formed, so fresh water would "
                    "keep being exposed at the top."},
            {"text": "It would freeze from the bottom up and could freeze "
                     "solid",
             "correct": True},
            {"text": "It would never freeze at all", "correct": False,
             "why": "It would freeze readily; where the ice went is what "
                    "would differ."},
            {"text": "The ice would form in the middle and stay there",
             "correct": False,
             "why": "Denser ice would sink all the way to the bottom rather "
                    "than hanging in the water."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h13",
        "band": "harder",
        "text": "Why is water's behaviour on freezing called an exception?",
        "options": [
            {"text": "Because it is the only substance that freezes at all",
             "correct": False,
             "why": "Almost everything freezes; it is what happens to the "
                    "density that is unusual."},
            {"text": "Because almost every other substance is denser as a "
                     "solid",
             "correct": True},
            {"text": "Because water is the only substance that has a solid "
                     "form at all",
             "correct": False,
             "why": "Every substance has one; iron, wax and lead all do."},
            {"text": "Because water freezes at 0 °C and nothing else does",
             "correct": False,
             "why": "The freezing temperature is not what makes it "
                    "exceptional; the density change is."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p11-04-e14",
        "band": "easier",
        "text": "Solid candle wax has a density of about 0.93 g/cm³. Dropped "
                "into plain water (1.00 g/cm³), what does it do?",
        "options": [
            {"text": "Floats", "correct": True},
            {"text": "Sinks", "correct": False,
             "why": "Wax's density is below water's, so it floats rather "
                    "than sinking."},
            {"text": "Dissolves", "correct": False,
             "why": "Wax does not dissolve in water; it simply floats or "
                    "sinks depending on density."},
            {"text": "Neither — it hangs in the middle", "correct": False,
             "why": "That only happens at exactly matching densities, and "
                    "wax and water do not match."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e15",
        "band": "easier",
        "text": "Aluminium and iron both sink in their own melted liquid. "
                "What do wax, aluminium and iron all have in common, that "
                "water does NOT?",
        "options": [
            {"text": "They are all metals", "correct": False,
             "why": "Wax is not a metal at all."},
            {"text": "Their solid form is denser than their own liquid form",
             "correct": True},
            {"text": "They all float on water", "correct": False,
             "why": "Only wax, at 0.93 g/cm³, floats on water; aluminium and "
                    "iron both sink in it."},
            {"text": "They all expand quite noticeably in volume when they freeze solid", "correct": False,
             "why": "It is the opposite — all three contract on freezing, "
                    "unlike water."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e16",
        "band": "easier",
        "text": "Which is denser: water at 2 °C, or water at 4 °C?",
        "options": [
            {"text": "Water at 2 °C", "correct": False,
             "why": "Cooling from 4 °C down towards 0 °C makes water "
                    "slightly LESS dense, not more."},
            {"text": "They are exactly the same density", "correct": False,
             "why": "4 °C is specifically the temperature of water's "
                    "maximum density; other temperatures are very slightly "
                    "less dense."},
            {"text": "Water at 4 °C", "correct": True},
            {"text": "It cannot be told without a measuring cylinder",
             "correct": False,
             "why": "It is a known fact that 4 °C is where liquid water is "
                    "at its densest."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e17",
        "band": "easier",
        "text": "500 cm³ of liquid water is completely frozen. Is the "
                "resulting ice's volume bigger, smaller, or the same as "
                "500 cm³?",
        "options": [
            {"text": "Smaller", "correct": False,
             "why": "Freezing water expands it; the ice takes up more room, "
                    "not less."},
            {"text": "Exactly the same", "correct": False,
             "why": "Water is the exception that changes volume on "
                    "freezing, by about 9%."},
            {"text": "It cannot be told without weighing the ice",
             "correct": False,
             "why": "The direction of the change can be told without "
                    "weighing anything — water always expands on freezing."},
            {"text": "Bigger", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e18",
        "band": "easier",
        "text": "A block of solid wax and a block of solid aluminium are "
                "both dropped into their OWN melted liquid. What happens to "
                "both?",
        "options": [
            {"text": "Both sink", "correct": True},
            {"text": "Both float", "correct": False,
             "why": "Only ice floats on its own melt among common "
                    "substances; wax and aluminium both sink in theirs."},
            {"text": "The wax floats and the aluminium sinks",
             "correct": False,
             "why": "Wax's solid form is also denser than its own melt, so "
                    "it sinks too."},
            {"text": "The aluminium floats and the wax sinks",
             "correct": False,
             "why": "Aluminium's solid form is denser than its own melt, so "
                    "it sinks rather than floating."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e19",
        "band": "easier",
        "text": "What happens to the space inside a water pipe when the "
                "water inside it freezes solid?",
        "options": [
            {"text": "The ice needs quite a bit less space than the water "
                     "did", "correct": False,
             "why": "Freezing expands water; the ice needs more space, not "
                    "less."},
            {"text": "The ice always needs more space than the water did",
             "correct": True},
            {"text": "The space needed stays exactly the same as before "
                     "the water froze",
             "correct": False,
             "why": "The volume changes by about 9% on freezing, which is "
                    "exactly why pipes can split."},
            {"text": "It depends on how cold the pipe gets", "correct": False,
             "why": "The expansion happens as soon as the water freezes, "
                    "whatever temperature it then reaches."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e20",
        "band": "easier",
        "text": "Which of these substances is the ODD ONE OUT for becoming "
                "LESS dense when it freezes: water, wax, aluminium or iron?",
        "options": [
            {"text": "Wax", "correct": False,
             "why": "Wax follows the ordinary rule and becomes denser when "
                    "it freezes."},
            {"text": "Aluminium", "correct": False,
             "why": "Aluminium follows the ordinary rule and becomes denser "
                    "when it freezes."},
            {"text": "Water", "correct": True},
            {"text": "Iron", "correct": False,
             "why": "Iron follows the ordinary rule and becomes denser when "
                    "it freezes."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e21",
        "band": "easier",
        "text": "A crack in a rock fills with water, which then freezes. What "
                "does the freezing do to the crack?",
        "options": [
            {"text": "Nothing, since ice and water take up the same space",
             "correct": False,
             "why": "Ice takes up about 9% more space than the water it "
                    "froze from."},
            {"text": "Seals it shut, since the ice fills the gap",
             "correct": False,
             "why": "The ice does more than fill the gap — it expands and "
                    "pushes outward, widening the crack."},
            {"text": "Shrinks it, since freezing contracts most things",
             "correct": False,
             "why": "Water is the exception; freezing it expands rather "
                    "than contracts it."},
            {"text": "Widens it, because the freezing water expands",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e22",
        "band": "easier",
        "text": "Why do cryobiologists, scientists who freeze living cells "
                "and tissue, add antifreeze compounds before freezing?",
        "options": [
            {"text": "To stop the water inside the cells expanding into "
                     "damaging ice crystals", "correct": True},
            {"text": "To make the cells taste noticeably better once they are thawed out "
            "again",
             "correct": False,
             "why": "Taste plays no part in preserving cells for later "
                    "use."},
            {"text": "To speed up how quickly the cells freeze",
             "correct": False,
             "why": "The antifreeze is there to change how the freezing "
                    "happens, not simply to speed it up."},
            {"text": "To stop the cells from melting later on",
             "correct": False,
             "why": "The concern is damage during freezing, from expanding "
                    "ice, not damage on melting."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e23",
        "band": "easier",
        "text": "Why does frozen fruit often go soft and mushy once it has "
                "thawed?",
        "options": [
            {"text": "The fruit loses mass while it is frozen",
             "correct": False,
             "why": "Freezing does not remove any mass from the fruit at "
                    "all."},
            {"text": "The water inside its cells expanded on freezing and "
                     "damaged them", "correct": True},
            {"text": "Freezing destroys the vitamins in the fruit",
             "correct": False,
             "why": "Softening is a physical, structural change, not "
                    "chemically about vitamins."},
            {"text": "Cold temperatures slowly dissolve away the fruit's own cell walls",
             "correct": False,
             "why": "Cold does not dissolve anything; the cell walls are "
                    "damaged by the expanding ice inside."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e24",
        "band": "easier",
        "text": "A liquid has a density of 0.80 g/cm³. Roughly what fraction "
                "of a lump of it would be BELOW the surface of water "
                "(1.00 g/cm³) if it floated?",
        "options": [
            {"text": "About 20%", "correct": False,
             "why": "That is the fraction ABOVE the surface, not below it."},
            {"text": "About 50%", "correct": False,
             "why": "Half and half would need the liquid's density to be "
                    "half of water's, and 0.80 is not half of 1.00."},
            {"text": "About 80%", "correct": True},
            {"text": "All of it", "correct": False,
             "why": "Something with a density below water's must have some "
                    "part showing above the surface to be floating at all."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e25",
        "band": "easier",
        "text": "Real seasoned oak has a density that varies a little "
                "between individual pieces of wood. Why is a single figure of "
                "0.65 g/cm³ still quoted for it in a density table?",
        "options": [
            {"text": "Because every piece of oak has exactly this density",
             "correct": False,
             "why": "Real timber varies with the species and how much "
                    "moisture it holds."},
            {"text": "Because oak has no measurable density as a material",
             "correct": False,
             "why": "Oak's density can be measured perfectly well; it "
                    "simply varies a little between samples."},
            {"text": "Because the figure is only a rough guess with no real scientific "
            "basis behind it", "correct": False,
             "why": "It is a genuine typical value for seasoned oak, not an "
                    "arbitrary guess."},
            {"text": "It is a typical value, useful for comparing oak "
                     "against other materials", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e26",
        "band": "easier",
        "text": "A solid block of iron is dropped into a pool of molten "
                "(melted) iron. What happens?",
        "options": [
            {"text": "It sinks", "correct": True},
            {"text": "It floats", "correct": False,
             "why": "Only ice floats on its own melt among common "
                    "substances; iron sinks in molten iron."},
            {"text": "It stays exactly where it is placed", "correct": False,
             "why": "That would need the two densities to match exactly, "
                    "and solid iron is denser than molten iron."},
            {"text": "It melts before it can sink or float", "correct": False,
             "why": "Whether it eventually melts is a separate matter; "
                    "being placed into the melt, it sinks straight away."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e27",
        "band": "easier",
        "text": "Below what temperature does water start to expand as it is "
                "cooled further?",
        "options": [
            {"text": "0 °C", "correct": False,
             "why": "0 °C is where water freezes; the anomalous expansion "
                    "on cooling begins a little above that, at 4 °C."},
            {"text": "4 °C", "correct": True},
            {"text": "10 °C", "correct": False,
             "why": "Water is still contracting as it cools right down to "
                    "4 °C; the odd expansion begins below that point."},
            {"text": "100 °C", "correct": False,
             "why": "That is water's boiling point, unrelated to this "
                    "anomalous cooling behaviour."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e28",
        "band": "easier",
        "text": "A tub of margarine is left in a freezer and does not crack, "
                "while a full, sealed bottle of water in the same freezer "
                "does. What is the key difference between the two as they "
                "solidify?",
        "options": [
            {"text": "Margarine does not get cold enough to set solid",
             "correct": False,
             "why": "Margarine does thicken and set solid in a freezer; "
                    "what matters is what happens to its volume as it "
                    "does."},
            {"text": "Margarine is less dense than water to begin with",
             "correct": False,
             "why": "That is true but is not why one container splits and "
                    "the other does not; it is about the volume change on "
                    "freezing."},
            {"text": "Margarine contracts as it solidifies, taking up less "
                     "room rather than more", "correct": True},
            {"text": "Margarine tubs are generally made of stronger plastic "
                     "than glass bottles", "correct": False,
             "why": "The difference is in what the substance does on "
                    "freezing, not in the strength of the container."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e29",
        "band": "easier",
        "text": "A chunk of a certain plastic has a density of 0.95 g/cm³. "
                "Roughly what fraction of it floats ABOVE the surface of "
                "water?",
        "options": [
            {"text": "About 95%", "correct": False,
             "why": "That is the fraction BELOW the surface, not above it."},
            {"text": "About 50%", "correct": False,
             "why": "Half and half would need a density roughly half of "
                    "water's, and 0.95 is very close to water's own "
                    "density."},
            {"text": "None of it", "correct": False,
             "why": "Anything less dense than water must show some part "
                    "above the surface while floating."},
            {"text": "About 5%", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-e30",
        "band": "easier",
        "text": "Which of these correctly ranks candle wax's TWO given "
                "densities?",
        "options": [
            {"text": "Solid wax (0.93) is denser than liquid wax (0.90)",
             "correct": True},
            {"text": "Liquid wax (0.90) is denser than solid wax (0.93)",
             "correct": False,
             "why": "That has the two densities the wrong way round."},
            {"text": "The two densities are exactly equal", "correct": False,
             "why": "The two figures given, 0.93 and 0.90, are not equal."},
            {"text": "Wax has no measurable density as a solid",
             "correct": False,
             "why": "Wax's solid density is measured and quoted just as its "
                    "liquid density is."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p11-04-s14",
        "band": "standard",
        "text": "1200 cm³ of molten aluminium (2.38 g/cm³) is cooled until it "
                "solidifies completely (2.70 g/cm³). What is the new solid "
                "volume?",
        "options": [
            {"text": "1200 cm³, unchanged", "correct": False,
             "why": "The volume changes as the density changes; it does not "
                    "stay the same."},
            {"text": "About 1058 cm³", "correct": True},
            {"text": "About 1364 cm³", "correct": False,
             "why": "That is bigger than the starting volume, but "
                    "solidifying aluminium makes it smaller, not bigger."},
            {"text": "932 cm³", "correct": False,
             "why": "That divides the mass by the wrong density in the "
                    "calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s15",
        "band": "standard",
        "text": "1000 cm³ of molten iron (6.98 g/cm³) is cooled until it "
                "solidifies completely (7.87 g/cm³). What is the new solid "
                "volume?",
        "options": [
            {"text": "1000 cm³, unchanged", "correct": False,
             "why": "The volume changes as the density changes; it does not "
                    "stay the same."},
            {"text": "1129 cm³", "correct": False,
             "why": "That is bigger than the starting volume, but "
                    "solidifying iron makes it smaller, not bigger."},
            {"text": "About 887 cm³", "correct": True},
            {"text": "798 cm³", "correct": False,
             "why": "That divides the mass by the wrong density in the "
                    "calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s16",
        "band": "standard",
        "text": "A chunk of solid wax (0.93 g/cm³) floats in water "
                "(1.00 g/cm³). Roughly what fraction of it sits below the "
                "surface?",
        "options": [
            {"text": "7%", "correct": False,
             "why": "That is the fraction ABOVE the surface, not below it."},
            {"text": "50%", "correct": False,
             "why": "Half and half would need wax to be half as dense as "
                    "water, and 0.93 is much closer to 1.00 than that."},
            {"text": "90%", "correct": False,
             "why": "That rounds too far; the figures given give a fraction "
                    "closer to 93%."},
            {"text": "93%", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s17",
        "band": "standard",
        "text": "500 cm³ of liquid water freezes solid. What is the new "
                "volume of the ice, given ice is 0.92 g/cm³ and water is "
                "1.00 g/cm³?",
        "options": [
            {"text": "About 543 cm³", "correct": True},
            {"text": "500 cm³, unchanged", "correct": False,
             "why": "Water is the exception that changes volume on "
                    "freezing; the ice does not stay at 500 cm³."},
            {"text": "460 cm³", "correct": False,
             "why": "That divides the mass by the wrong density, giving a "
                    "smaller volume when a bigger one is expected."},
            {"text": "580 cm³", "correct": False,
             "why": "That overshoots the figure the given densities "
                    "actually produce."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s18",
        "band": "standard",
        "text": "Why does a lake's water column typically end up with 4 °C "
                "water at the bottom and colder water above it in winter, "
                "once ice has formed?",
        "options": [
            {"text": "Because 4 °C water is the least dense, so it rises to "
                     "the top", "correct": False,
             "why": "It is the opposite: 4 °C water is the MOST dense, "
                    "which is why it sinks rather than rising."},
            {"text": "Because 4 °C water is the densest, so it sinks to the "
                     "bottom", "correct": True},
            {"text": "Because the ground beneath the lake heats the water "
                     "to exactly 4 °C", "correct": False,
             "why": "The ground contributes a little warmth, but the "
                    "layering itself comes from water's density curve, not "
                    "from ground heating alone."},
            {"text": "Because ice typically melts first at 4 °C",
             "correct": False,
             "why": "Ice melts at 0 °C; the 4 °C figure here is about where "
                    "liquid water is densest, not about melting."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s19",
        "band": "standard",
        "text": "A litre of water freezes solid inside a sealed metal "
                "canister with no room to expand. What is most likely to "
                "happen?",
        "options": [
            {"text": "Nothing, since metal is much stronger than ice",
             "correct": False,
             "why": "Strength alone does not save a sealed rigid container "
                    "from an expanding solid with nowhere to go."},
            {"text": "The canister shrinks to fit the ice", "correct": False,
             "why": "Metal does not shrink to accommodate an expanding "
                    "solid inside it."},
            {"text": "The canister deforms or splits under the pressure of "
                     "the expanding ice", "correct": True},
            {"text": "The water simply refuses to freeze inside a sealed "
                     "container", "correct": False,
             "why": "Being sealed does not stop water from freezing; it "
                    "only stops the ice from expanding freely."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s20",
        "band": "standard",
        "text": "A liquid has a density of 0.70 g/cm³. Compare the fraction "
                "of a floating lump of it that sits above the surface with a "
                "lump of ice (0.92 g/cm³) floating in the same water.",
        "options": [
            {"text": "The 0.70 g/cm³ lump shows less above the surface than "
                     "the ice", "correct": False,
             "why": "A lower density leaves a bigger fraction above the "
                    "surface, not a smaller one."},
            {"text": "Both show exactly the same fraction above the surface, whatever "
            "their two densities happen to be", "correct": False,
             "why": "The two densities are different, so the fractions "
                    "above the surface are different too."},
            {"text": "The ice shows more above the surface than the "
                     "0.70 g/cm³ lump", "correct": False,
             "why": "Ice, being closer to water's own density, actually "
                    "shows LESS above the surface, not more."},
            {"text": "The 0.70 g/cm³ lump shows more above the surface than "
                     "the ice", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s21",
        "band": "standard",
        "text": "Why does an ice cube in a fizzy drink rise slightly as "
                "bubbles cling to it, then sink back down as the bubbles "
                "pop?",
        "options": [
            {"text": "The bubbles briefly reduce the ice's overall, average "
                     "density enough to lift it further", "correct": True},
            {"text": "The ice briefly becomes less dense than water on its own, for as "
            "long as the bubbles stay attached to it", "correct": False,
             "why": "The ice's own density does not change; it is the "
                    "attached bubbles that briefly change the whole object's "
                    "average density."},
            {"text": "The fizzy drink is less dense than plain water",
             "correct": False,
             "why": "The rise and fall is about the bubbles clinging to and "
                    "leaving the ice, not about the drink's own density."},
            {"text": "The bubbles make the ice colder, so it floats higher",
             "correct": False,
             "why": "Temperature is not what is changing here; the "
                    "attached bubbles are what briefly lift the ice."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s22",
        "band": "standard",
        "text": "Why is candle wax's quoted density given as 'about 0.93' "
                "rather than an exact figure?",
        "options": [
            {"text": "Because wax has no real density until it is weighed",
             "correct": False,
             "why": "Wax has a real density whether or not it has just been "
                    "weighed."},
            {"text": "Because wax is a mixture, and its density varies a "
                     "little between blends", "correct": True},
            {"text": "Because density cannot be measured for a solid",
             "correct": False,
             "why": "Density is measured for solids all the time, wax "
                    "included."},
            {"text": "Because 0.93 is simply a much easier number to remember than an "
            "exact value", "correct": False,
             "why": "The figure is approximate because of real variation in "
                    "the material, not for ease of memory."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s23",
        "band": "standard",
        "text": "A pure sample of ice at 0 °C sits in a glass of pure water "
                "at 0 °C. Does the ice's density change while it slowly "
                "melts?",
        "options": [
            {"text": "Yes, it rises gradually to 1.00 g/cm³ as it melts, a "
                     "little more with each passing minute",
             "correct": False,
             "why": "The solid ice keeps its own density right up until it "
                    "has fully turned to liquid; it does not creep upward "
                    "gradually."},
            {"text": "Yes, it falls gradually towards 0", "correct": False,
             "why": "Density does not fall towards zero during melting; the "
                    "solid ice keeps its density until it has fully "
                    "melted."},
            {"text": "No — the solid ice stays at 0.92 g/cm³ right up until "
                     "it has fully melted", "correct": True},
            {"text": "It cannot be known without weighing the glass",
             "correct": False,
             "why": "The solid ice's density is already known to stay fixed "
                    "throughout the melting, without needing to weigh "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s24",
        "band": "standard",
        "text": "A fish tank is left outdoors and a layer of ice forms on "
                "top in freezing weather. What protects the fish living in "
                "the water below?",
        "options": [
            {"text": "The fish generate enough body heat to stop it all "
                     "freezing", "correct": False,
             "why": "Fish generate very little heat; the protection comes "
                    "from the ice layer itself."},
            {"text": "The ice sinks to the bottom, keeping the top layer "
                     "liquid", "correct": False,
             "why": "Ice floats rather than sinking, which is exactly what "
                    "lets it protect the water underneath."},
            {"text": "The tank's glass alone insulates the water from the cold air "
            "directly", "correct": False,
             "why": "It is the floating ice on top of the water, not the "
                    "glass, that mainly insulates the water below."},
            {"text": "The floating ice layer insulates the water below from "
                     "the freezing air", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s25",
        "band": "standard",
        "text": "A hiker leaves a full water bottle outside overnight in "
                "freezing temperatures. Which detail would make the bottle "
                "LESS likely to split?",
        "options": [
            {"text": "Leaving some empty air space at the top of the "
                     "bottle before sealing it", "correct": True},
            {"text": "Filling the bottle completely to the very brim before sealing the "
            "cap tightly shut",
             "correct": False,
             "why": "A completely full, sealed bottle gives the expanding "
                    "ice nowhere at all to go."},
            {"text": "Using a bottle made of thinner plastic",
             "correct": False,
             "why": "A thinner bottle resists the pressure of expanding ice "
                    "less well, not more."},
            {"text": "Freezing the water as quickly as possible",
             "correct": False,
             "why": "How quickly it freezes does not change how much the "
                    "ice ultimately expands."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s26",
        "band": "standard",
        "text": "Two identical glass bottles are both filled completely with "
                "liquid and frozen solid: one with water, one with cooking "
                "oil. Which is more likely to split, and why?",
        "options": [
            {"text": "The oil bottle, since oil expands more than water on "
                     "freezing", "correct": False,
             "why": "Oil actually contracts as it solidifies, unlike "
                    "water."},
            {"text": "The water bottle, since water expands on freezing "
                     "while oil contracts", "correct": True},
            {"text": "Neither, since glass never splits from freezing "
                     "liquid inside it", "correct": False,
             "why": "A fully sealed, completely full bottle of freezing "
                    "water very much can split."},
            {"text": "Both equally, since freezing always expands a "
                     "liquid", "correct": False,
             "why": "Freezing does not always expand a liquid; most "
                    "substances, oil included, contract instead."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s27",
        "band": "standard",
        "text": "A scientist compares aluminium (solid 2.70, liquid "
                "2.38 g/cm³) with iron (solid 7.87, liquid 6.98 g/cm³). "
                "Which metal contracts by the BIGGER fraction of its own "
                "volume on freezing?",
        "options": [
            {"text": "Iron, since its density numbers are bigger overall",
             "correct": False,
             "why": "The size of the raw numbers is not what decides the "
                    "fraction of contraction; the RATIO between the two "
                    "figures is."},
            {"text": "Neither — both contract by exactly the same fraction",
             "correct": False,
             "why": "Working out each fraction from the figures given shows "
                    "they are not quite equal."},
            {"text": "Aluminium, by a very slightly bigger fraction",
             "correct": True},
            {"text": "It cannot be compared using density figures alone",
             "correct": False,
             "why": "The density figures given are exactly enough to "
                    "compare the two fractions."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s28",
        "band": "standard",
        "text": "Why does a pond's fish population usually survive a hard "
                "winter, while a shallow puddle freezes solid?",
        "options": [
            {"text": "Fish keep the pond's water constantly moving around, which stops it "
            "from fully freezing over", "correct": False,
             "why": "Fish movement is far too small an effect; the real "
                    "protection comes from the pond's depth and its floating "
                    "ice layer."},
            {"text": "Puddles are made of a different kind of water",
             "correct": False,
             "why": "Puddle water and pond water are the same substance; "
                    "depth is what differs."},
            {"text": "Ponds are always warmed slightly by the fish and "
                     "other animals living inside them, all year round",
             "correct": False,
             "why": "Fish add a negligible amount of warmth; the real "
                    "protection is the pond's depth and its ice layer."},
            {"text": "A pond is deep enough that its floating ice layer "
                     "never reaches all the way to the bottom", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s29",
        "band": "standard",
        "text": "A liquid has a density of 0.99 g/cm³, very close to "
                "water's 1.00. Roughly what fraction of a floating lump of "
                "it would show above the surface?",
        "options": [
            {"text": "About 1%", "correct": True},
            {"text": "About 10%", "correct": False,
             "why": "That is far too big for a density this close to "
                    "water's own."},
            {"text": "About 50%", "correct": False,
             "why": "Half and half would need a density around half of "
                    "water's, not 0.99."},
            {"text": "About 99%", "correct": False,
             "why": "That is the fraction BELOW the surface, not above it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-s30",
        "band": "standard",
        "text": "Why does the fraction of an iceberg above the surface "
                "change very slightly between fresh water and salty sea "
                "water?",
        "options": [
            {"text": "Because ice itself is a slightly different density once it forms in "
            "salt water", "correct": False,
             "why": "The ice's own density stays essentially the same; it "
                    "is the surrounding water's density that changes."},
            {"text": "Because sea water is slightly denser than fresh "
                     "water, changing the ratio used", "correct": True},
            {"text": "Because icebergs melt faster in salt water",
             "correct": False,
             "why": "Melting speed is a separate matter from what fraction "
                    "shows above the surface while it floats."},
            {"text": "Because salt water freezes at a different "
                     "temperature", "correct": False,
             "why": "The freezing temperature of the surrounding sea water "
                    "does not decide what fraction of a floating iceberg "
                    "shows above it."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p11-04-h14",
        "band": "harder",
        "text": "A 2000 cm³ block of ice melts completely into water. What "
                "volume of water results, given ice is 0.92 g/cm³ and water "
                "is 1.00 g/cm³?",
        "options": [
            {"text": "2000 cm³", "correct": False,
             "why": "Melting ice takes up LESS space as water, not the same "
                    "amount."},
            {"text": "2174 cm³", "correct": False,
             "why": "That is bigger than the ice's own volume, but melting "
                    "ice shrinks in volume, not grows."},
            {"text": "1840 cm³", "correct": True},
            {"text": "1680 cm³", "correct": False,
             "why": "That undershoots the figure the given densities "
                    "actually produce."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h15",
        "band": "harder",
        "text": "800 cm³ of liquid water is frozen completely. What volume "
                "does the resulting ice occupy?",
        "options": [
            {"text": "800 cm³", "correct": False,
             "why": "Water is the exception that expands on freezing; the "
                    "ice does not stay at 800 cm³."},
            {"text": "736 cm³", "correct": False,
             "why": "That is smaller than the starting volume, but freezing "
                    "water makes it bigger, not smaller."},
            {"text": "About 928 cm³", "correct": False,
             "why": "That overshoots the figure the given densities "
                    "actually produce."},
            {"text": "About 870 cm³", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h16",
        "band": "harder",
        "text": "A liquid of density 0.60 g/cm³ floats on water. A second "
                "liquid of density 0.85 g/cm³ also floats on the same "
                "water, in a separate container. Compare how much of each "
                "shows above the surface.",
        "options": [
            {"text": "The 0.60 g/cm³ liquid shows more above the surface "
                     "than the 0.85 g/cm³ one", "correct": True},
            {"text": "The 0.85 g/cm³ liquid shows more above the surface",
             "correct": False,
             "why": "Being closer to water's own density leaves LESS above "
                    "the surface, not more."},
            {"text": "Both show exactly the same fraction above the surface, whatever "
            "their two densities happen to be", "correct": False,
             "why": "The two densities are different, so the fractions "
                    "above the surface are different too."},
            {"text": "Neither shows anything above the surface",
             "correct": False,
             "why": "Both liquids are less dense than water, so both must "
                    "show some part above the surface while floating."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h17",
        "band": "harder",
        "text": "Explain, using density, why a lump of ice sitting in a "
                "glass of water does NOT noticeably change the water level "
                "once it has fully melted.",
        "options": [
            {"text": "Because ice weighs nothing extra compared with the "
                     "water", "correct": False,
             "why": "Ice does have a real weight; the reasoning needs to "
                    "involve displacement, not zero weight."},
            {"text": "Because a floating object pushes aside a weight of "
                     "water exactly equal to its own weight, which matches "
                     "the meltwater it produces", "correct": True},
            {"text": "Because melting ice always evaporates into the air instead of "
            "turning into liquid water at all, the same way steam leaves a "
            "boiling kettle", "correct": False,
             "why": "Melting ice turns into liquid water, not vapour; "
                    "evaporation is a separate process."},
            {"text": "Because the glass expands slightly to compensate",
             "correct": False,
             "why": "Glass does not meaningfully expand to compensate for "
                    "anything happening inside it."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h18",
        "band": "harder",
        "text": "A block of an unknown solid floats in water with 35% of "
                "its volume above the surface. What is its approximate "
                "density?",
        "options": [
            {"text": "About 0.35 g/cm³", "correct": False,
             "why": "That uses the fraction ABOVE the surface directly as "
                    "the density, rather than the fraction BELOW it."},
            {"text": "1.35 g/cm³", "correct": False,
             "why": "A density above 1.00 g/cm³ would sink rather than "
                    "float at all."},
            {"text": "About 0.65 g/cm³", "correct": True},
            {"text": "About 0.5 g/cm³, since roughly a third floats and "
                     "roughly two thirds sink", "correct": False,
             "why": "That rounds too roughly; the 35% figure given leads "
                    "more precisely to about 0.65 g/cm³."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h19",
        "band": "harder",
        "text": "Two identical glass bottles are completely filled with "
                "liquid and sealed, then left in a freezer: one with water, "
                "one with molten wax that is then allowed to solidify "
                "inside. Which is more likely to crack the glass?",
        "options": [
            {"text": "The wax bottle, since wax also expands on freezing",
             "correct": False,
             "why": "Wax actually contracts as it solidifies, unlike "
                    "water."},
            {"text": "Neither — sealed glass bottles do not crack from "
                     "freezing liquid of any kind", "correct": False,
             "why": "A fully sealed, completely full bottle of freezing "
                    "water very much can crack."},
            {"text": "Both equally, since both liquids freeze at some "
                     "point", "correct": False,
             "why": "Freezing alone does not decide it; what matters is "
                    "whether the substance expands or contracts as it "
                    "solidifies."},
            {"text": "The water bottle, since wax contracts on solidifying "
                     "while water expands", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h20",
        "band": "harder",
        "text": "A scientist wants to identify an unknown clear liquid that "
                "does not mix with water. It floats in water with about "
                "10% of its volume above the surface. Which of the bench's "
                "substances does this most closely match?",
        "options": [
            {"text": "Liquid wax, at 0.90 g/cm³", "correct": True},
            {"text": "Solid wax, at about 0.93 g/cm³", "correct": False,
             "why": "That density would leave only about 7% above the "
                    "surface, not 10%."},
            {"text": "Ice, at 0.92 g/cm³", "correct": False,
             "why": "That density would leave only about 8% above the "
                    "surface, not 10%."},
            {"text": "Water itself, at 1.00 g/cm³", "correct": False,
             "why": "Something at exactly water's own density would show "
                    "0% above the surface, hanging level instead."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h21",
        "band": "harder",
        "text": "A pond's water column sits at 4 °C at the bottom, 2 °C in "
                "the middle and 0 °C, as ice, at the top. Rank the three "
                "layers from MOST dense to LEAST dense.",
        "options": [
            {"text": "0 °C, then 2 °C, then 4 °C", "correct": False,
             "why": "That ranks them backwards; 4 °C is the densest of the "
                    "three, not the least dense."},
            {"text": "4 °C, then 2 °C, then 0 °C, as ice", "correct": True},
            {"text": "2 °C, then 4 °C, then 0 °C, as ice", "correct": False,
             "why": "4 °C is the single densest point on the whole curve, "
                    "so it must rank first, not second."},
            {"text": "All three layers are equally dense", "correct": False,
             "why": "The three layers sit at different points on water's "
                    "density curve, so they are not equally dense."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h22",
        "band": "harder",
        "text": "A 300 cm³ lump of solid wax (0.93 g/cm³) is melted "
                "completely into liquid wax (0.90 g/cm³). What is the new "
                "liquid volume?",
        "options": [
            {"text": "300 cm³, unchanged", "correct": False,
             "why": "The volume changes as the density changes on "
                    "melting; it does not stay the same."},
            {"text": "290 cm³", "correct": False,
             "why": "That is smaller than the starting volume, but melting "
                    "wax makes it bigger, not smaller."},
            {"text": "310 cm³", "correct": True},
            {"text": "325 cm³", "correct": False,
             "why": "That overshoots the figure the given densities "
                    "actually produce."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h23",
        "band": "harder",
        "text": "Why is it misleading to say 'freezing always makes a "
                "substance denser'?",
        "options": [
            {"text": "Because freezing never actually changes a "
                     "substance's density", "correct": False,
             "why": "Freezing very much does change density for almost "
                    "every substance, wax, aluminium and iron included."},
            {"text": "Because most substances get LESS dense when they "
                     "freeze", "correct": False,
             "why": "It is the other way round: almost every substance "
                    "gets MORE dense when it freezes."},
            {"text": "Because 'always' is generally too strong a word to use about any "
            "melting point", "correct": False,
             "why": "Melting points are not what this statement is even "
                    "about; it is about density."},
            {"text": "Because water is a well-known exception that becomes "
                     "LESS dense on freezing", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h24",
        "band": "harder",
        "text": "A lump of solid material floats in water with exactly half "
                "its volume above the surface. What must be true of its "
                "density?",
        "options": [
            {"text": "It is about 0.50 g/cm³", "correct": True},
            {"text": "It is about 1.00 g/cm³", "correct": False,
             "why": "Something at exactly water's own density would hang "
                    "level with the surface, showing nothing above it."},
            {"text": "It is about 0.92 g/cm³, the same as ice",
             "correct": False,
             "why": "Ice shows only about 8% above the surface, nowhere "
                    "near half."},
            {"text": "It cannot be worked out from this information",
             "correct": False,
             "why": "The fraction showing above the surface is exactly "
                    "enough information to work out the density."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h25",
        "band": "harder",
        "text": "A liquid of density 1.02 g/cm³ is poured onto water "
                "(1.00 g/cm³) in a jar. Sometime later, a lump of ice "
                "(0.92 g/cm³) is dropped in. Describe the final "
                "arrangement, top to bottom.",
        "options": [
            {"text": "The dense liquid, then water, then ice",
             "correct": False,
             "why": "That has the whole order upside down; the LEAST dense "
                    "material ends up on top, not the densest."},
            {"text": "Ice on top, then water, then the dense liquid at the "
                     "bottom", "correct": True},
            {"text": "Water on top, then the ice, then the dense liquid last",
             "correct": False,
             "why": "Ice is less dense than water, so ice ends up above the "
                    "water, not below it."},
            {"text": "All three mix into one single layer", "correct": False,
             "why": "The dense liquid and water do not mix, and the ice "
                    "stays solid and separate; three distinct layers form."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h26",
        "band": "harder",
        "text": "A foundry worker needs to know how much room to leave in a "
                "crucible before melting a 150 cm³ aluminium casting (solid "
                "2.70 g/cm³) down into liquid metal (2.38 g/cm³). What "
                "final volume should they plan for?",
        "options": [
            {"text": "150 cm³, unchanged", "correct": False,
             "why": "The volume changes as the density changes on melting; "
                    "it does not stay the same."},
            {"text": "132 cm³", "correct": False,
             "why": "That is smaller than the starting volume, but melting "
                    "aluminium makes it bigger, not smaller."},
            {"text": "About 170 cm³", "correct": True},
            {"text": "192 cm³", "correct": False,
             "why": "That overshoots the figure the given densities "
                    "actually produce."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h27",
        "band": "harder",
        "text": "Why does a floating iceberg not simply keep sinking lower "
                "and lower as more of it melts?",
        "options": [
            {"text": "Because ice simply stops melting once some of it has "
                     "gone", "correct": False,
             "why": "Melting does not stop partway through; a melting "
                    "iceberg keeps melting until it is gone."},
            {"text": "Because the melted water refreezes onto the bottom of the berg as "
            "fast as it melts from the top, keeping the whole shape steady", "correct": False,
             "why": "Nothing here is refreezing; the berg is simply "
                    "shrinking as it melts."},
            {"text": "Because icebergs are anchored to the sea floor",
             "correct": False,
             "why": "Floating icebergs are not anchored; they drift freely "
                    "on the surface."},
            {"text": "Because at every moment it settles to the depth "
                     "where the weight of water displaced still matches its "
                     "own weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h28",
        "band": "harder",
        "text": "A liquid of unknown density floats in water with 22% of "
                "its volume above the surface. What is its approximate "
                "density, and is it denser or less dense than ice?",
        "options": [
            {"text": "About 0.78 g/cm³, less dense than ice", "correct": True},
            {"text": "About 0.78 g/cm³, denser than ice", "correct": False,
             "why": "0.78 g/cm³ is below ice's 0.92 g/cm³, so it is LESS "
                    "dense than ice, not denser."},
            {"text": "About 1.22 g/cm³, denser than ice", "correct": False,
             "why": "A density above 1.00 g/cm³ would sink in water rather "
                    "than float with any fraction showing above it."},
            {"text": "About 0.22 g/cm³, far less dense than ice",
             "correct": False,
             "why": "That treats the fraction ABOVE the surface as the "
                    "density itself, rather than working from the fraction "
                    "below."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h29",
        "band": "harder",
        "text": "Two rocks with identical cracks are left through a "
                "winter: one in a region with many freeze–thaw cycles, one "
                "in a region that freezes solid once and stays frozen all "
                "winter. Which rock is likely to show MORE damage by "
                "spring?",
        "options": [
            {"text": "The one that stays frozen solid all winter, since "
                     "ice is denser overall", "correct": False,
             "why": "Staying frozen once does not repeat the "
                    "expand-and-contract cycle that actually widens a "
                    "crack."},
            {"text": "The one exposed to many freeze–thaw cycles, since "
                     "each cycle re-expands the crack", "correct": True},
            {"text": "Neither — freeze–thaw weathering always needs a chemical reaction "
            "happening, not just ice", "correct": False,
             "why": "Freeze–thaw weathering is a purely physical process; "
                    "no chemical reaction is needed."},
            {"text": "Both equally, since either way the water freezes "
                     "once", "correct": False,
             "why": "Repeated freezing and thawing does far more damage "
                    "than freezing just the once."},
        ],
        "figure": None,
    },
    {
        "id": "p11-04-h30",
        "band": "harder",
        "text": "A 250 cm³ sample of an unknown liquid solidifies into "
                "268 cm³ of solid. Is this liquid more likely to be water, "
                "or an ORDINARY substance like wax?",
        "options": [
            {"text": "An ordinary substance like wax, since solids are "
                     "usually smaller than their liquid", "correct": False,
             "why": "This solid is BIGGER than its liquid, which is not "
                    "what an ordinary substance like wax does."},
            {"text": "It cannot be told from a volume change alone",
             "correct": False,
             "why": "The direction of the volume change alone is exactly "
                    "what distinguishes water's odd behaviour from the "
                    "ordinary rule."},
            {"text": "Water, since its volume increased on freezing rather "
                     "than decreasing", "correct": True},
            {"text": "Neither is possible, since solids can never take up "
                     "more room than their liquid", "correct": False,
             "why": "Water is exactly the well-known exception where the "
                    "solid does take up more room than the liquid."},
        ],
        "figure": None,
    },
]
