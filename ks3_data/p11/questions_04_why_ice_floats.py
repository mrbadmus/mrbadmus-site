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
]
