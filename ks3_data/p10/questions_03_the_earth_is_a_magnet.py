"""P10 lesson 03 — The Earth is a magnet: twelve questions (MRB-223).

Written against Design's page. The nine latitudes, the three bench objects,
the two mountings, the three norths and the four rungs are hers.

The discriminations, in the order the lesson builds them:

  · a needle is a MAGNET, and a magnet lines up with a field;
  · the planet has one, made by moving liquid iron and not by a buried bar
    (`MAG-11`);
  · the pole in the Arctic is magnetically a SOUTH pole (`MAG-09`), and the
    needle lies along a line rather than aiming at a place (`MAG-10`);
  · the field runs into the ground, steeply near the poles, so a compass gets
    worse there rather than better (`MAG-12`) — the harder band sits here.

⚠️ NO VALUE IN TESLA APPEARS IN ANY QUESTION. Ruled for the whole unit: every
angle here is a real angle in degrees and every strength is relative or in
words.

⚠️ POSITION IS AUTHORED — 2,3,0,1 · 3,0,1,2 · 0,1,2,3, three of each.

⚠️ NO RUNG IS RESTATED. The ladder owns the naming of the Arctic pole, the
forty-year-old map, the explanation of why a compass works and the polar
aircraft; nothing here reuses any of the four.
"""

UNIT = "P10"
LESSON = "the-earth-is-a-magnet"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p10-03-e01",
        "band": "easier",
        "text": "What is a compass needle?",
        "options": [
            {"text": "A piece of iron that has been shaped into an arrow",
             "correct": False,
             "why": "The shape is not what makes it work. A plain arrow of "
                    "unmagnetised iron would sit wherever you left it."},
            {"text": "A pointer driven round by a tiny motor inside the case",
             "correct": False,
             "why": "There is nothing driving it. A compass has no power "
                    "source of any kind."},
            {"text": "A small magnet, balanced so that it can turn freely",
             "correct": True},
            {"text": "A strip of metal that always points downhill",
             "correct": False,
             "why": "It settles the same way on a level table as on a slope. "
                    "What it responds to is the field, not the ground."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e02",
        "band": "easier",
        "text": "What makes the Earth's magnetic field?",
        "options": [
            {"text": "The Sun, which magnetises the whole planet as it "
                     "passes overhead",
             "correct": False,
             "why": "The field is there at night and in the middle of winter. "
                    "It is made inside the Earth."},
            {"text": "The Earth spinning, which drags the air around with it "
                     "as it turns",
             "correct": False,
             "why": "Spinning on its own makes no magnetic field, and the air "
                    "has nothing to do with it."},
            {"text": "Layers of magnetic rock in the crust, close beneath "
                     "the surface",
             "correct": False,
             "why": "Rocks near the surface do change the field locally, but "
                    "the field covering the whole planet is made far deeper."},
            {"text": "Electric currents carried by the churning liquid iron "
                     "in the core", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e03",
        "band": "easier",
        "text": "How does the Earth's magnetic pole compare with true north?",
        "options": [
            {"text": "It sits some way from true north, and it moves from "
                     "year to year", "correct": True},
            {"text": "It is exactly at true north, which is why a compass "
                     "works", "correct": False,
             "why": "They are hundreds of kilometres apart. A compass works "
                    "because it lies along the field, not because the two "
                    "places coincide."},
            {"text": "It is at the south of the planet, on the other side",
             "correct": False,
             "why": "The pole a needle's north-seeking end turns towards is "
                    "in the Arctic. What is confusing is its magnetic name, "
                    "not its location."},
            {"text": "It is fixed in place, and true north is the one that "
                     "wanders", "correct": False,
             "why": "It is the other way round. True north is set by the spin "
                    "axis and does not wander; the magnetic pole does."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e04",
        "band": "easier",
        "text": "What does the angle of dip measure?",
        "options": [
            {"text": "How far the compass has been tilted by the person "
                     "holding it", "correct": False,
             "why": "It is a fact about the field, not about the hand. A "
                    "compass hung properly gives the same dip however you "
                    "hold the case."},
            {"text": "How far the Earth's field runs into the ground rather "
                     "than along it", "correct": True},
            {"text": "How far magnetic north is from true north at that place",
             "correct": False,
             "why": "That angle has its own name — the declination. Dip is "
                    "the tipping, measured from level."},
            {"text": "How much the field has weakened since the last "
                     "measurement", "correct": False,
             "why": "Dip is a direction, not a strength. It can be steep "
                    "where the field is weak and shallow where it is strong."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p10-03-s01",
        "band": "standard",
        "text": "Why can there not be a solid bar magnet sitting inside the "
                "Earth's core?",
        "options": [
            {"text": "It would have been pulled apart by the Earth spinning "
                     "long ago", "correct": False,
             "why": "Spinning is not the problem. The core is under enormous "
                    "pressure and holds together perfectly well."},
            {"text": "A magnet that big would have pulled every ship on the "
                     "planet to the Arctic", "correct": False,
             "why": "The field really does reach every ship, and it turns "
                    "their compasses without dragging them anywhere."},
            {"text": "There is no iron down there for a magnet to be made of",
             "correct": False,
             "why": "The core is mostly iron. What it cannot be is "
                    "magnetised."},
            {"text": "The core is far too hot — above a few hundred degrees a "
                     "magnet loses its magnetism", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s02",
        "band": "standard",
        "text": "A compass is put down on a bench right beside a heavy steel "
                "clamp stand. What is likely to happen?",
        "options": [
            {"text": "The needle turns towards the stand, which the Earth's "
                     "own field has magnetised", "correct": True},
            {"text": "Nothing changes, because steel is not magnetised until "
                     "somebody magnetises it on purpose", "correct": False,
             "why": "The Earth's field magnetises it, slowly and by itself. "
                    "Steel left standing in one place for years is often a "
                    "weak magnet."},
            {"text": "The needle stops moving altogether, because the steel "
                     "blocks the Earth's field", "correct": False,
             "why": "Nothing blocks a magnetic field. The steel adds its own "
                    "instead, and the needle lines up with the total."},
            {"text": "The needle points at true north instead of magnetic "
                     "north, because steel corrects it", "correct": False,
             "why": "Nothing about steel knows where true north is. It makes "
                    "the reading worse, not better."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s03",
        "band": "standard",
        "text": "A compass that is free to tip is used at the equator. What "
                "does the needle do?",
        "options": [
            {"text": "It tips steeply, with its north-seeking end down",
             "correct": False,
             "why": "That is what happens far to the north. At the equator "
                    "there is nothing tipping it either way."},
            {"text": "It hangs level, because the field runs along the ground "
                     "there", "correct": True},
            {"text": "It stands vertical, because the equator is half way "
                     "between the two poles", "correct": False,
             "why": "Vertical is what happens ON a magnetic pole. Half way "
                    "between them the field is at its most level."},
            {"text": "It spins slowly, because the two poles pull it equally "
                     "hard", "correct": False,
             "why": "The sideways pull is at its strongest at the equator, so "
                    "the needle settles more firmly there than anywhere else."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s04",
        "band": "standard",
        "text": "An ordinary walking compass has a flat card that cannot tip "
                "at all. Why is it built that way?",
        "options": [
            {"text": "So that it can be read while it is lying in a pocket",
             "correct": False,
             "why": "It has to be held level to be read either way. The "
                    "reason is about the field, not about pockets."},
            {"text": "So that dropping it does not knock the needle off its "
                     "pivot", "correct": False,
             "why": "A tipping needle is no more fragile than a flat one. The "
                    "reason is which part of the field you want it to answer "
                    "to."},
            {"text": "So that only the sideways part of the field turns it, "
                     "which is the part you navigate by", "correct": True},
            {"text": "So that it works at the magnetic pole, where a tipping "
                     "needle would stand upright", "correct": False,
             "why": "Held flat at the pole it simply drifts and settles "
                    "nowhere, because there is no sideways part left at all."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p10-03-h01",
        "band": "harder",
        "text": "One compass is used in Britain and another in New Zealand. "
                "Both settle, and both are said to point north. Are the two "
                "needles pointing the same way in space?",
        "options": [
            {"text": "No — each one lies along the Earth's field where it "
                     "happens to be standing", "correct": True},
            {"text": "Yes — both are aiming at the same place, so both point "
                     "the same way", "correct": False,
             "why": "Neither is aiming at a place. Each lies along a line, "
                    "and the lines run differently at the two ends of the "
                    "planet."},
            {"text": "Yes, but only because both countries print the same "
                     "declination on their maps", "correct": False,
             "why": "The declination in the two places differs by a great "
                    "deal, which is part of why the needles differ."},
            {"text": "No — the New Zealand needle points south, because it is "
                     "in the southern half", "correct": False,
             "why": "Its north-seeking end still turns towards the Arctic. "
                    "What changes below the equator is which way it TIPS."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h02",
        "band": "harder",
        "text": "Iron minerals in lava set with the direction of the Earth's "
                "field frozen into them as it cools. Reading down a thick "
                "stack of old lava flows shows the direction flipping over "
                "and over. What does that tell you?",
        "options": [
            {"text": "The lava flowed in a different direction each time",
             "correct": False,
             "why": "Which way the lava ran does not set the direction. The "
                    "minerals line up with the field, not with the flow."},
            {"text": "The Earth's magnetic field has swapped ends many times "
                     "in the past", "correct": True},
            {"text": "The rock has been turned over by earthquakes since it "
                     "cooled", "correct": False,
             "why": "The layers are still in order, one on top of the next. "
                    "Turning a whole stack over repeatedly would show up in "
                    "other ways."},
            {"text": "The measurement is unreliable, because rock cannot "
                     "record a direction", "correct": False,
             "why": "It records it well, and the same pattern is found in the "
                    "same order all over the world, which is what makes it "
                    "convincing."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h03",
        "band": "harder",
        "text": "A freely hung needle tips with its north-seeking end "
                "downwards in Britain and upwards in New Zealand. Why?",
        "options": [
            {"text": "Gravity pulls harder on the north end in the north and "
                     "on the south end in the south", "correct": False,
             "why": "Gravity pulls on both ends equally and does not care "
                    "which is which. This is a magnetic effect."},
            {"text": "The needle is made differently for each half of the "
                     "world", "correct": False,
             "why": "The same needle carried from one to the other does both. "
                    "Nothing about the needle changed on the way."},
            {"text": "The field goes into the ground in the far north and "
                     "comes out of it in the far south", "correct": True},
            {"text": "The needle is trying to point at the closer of the two "
                     "poles, which is below the horizon", "correct": False,
             "why": "It is not aiming at a pole at all. It lies along the "
                    "field where it is, and near the equator that field is "
                    "level even though both poles are far away."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h04",
        "band": "harder",
        "text": "A ship with a steel hull carries its compass on a stand with "
                "large iron spheres bolted either side of it, adjusted when "
                "the ship is first fitted out. What problem are the spheres "
                "there to solve?",
        "options": [
            {"text": "The steel hull blocks the Earth's field, and the "
                     "spheres are there to let some of it back through",
             "correct": False,
             "why": "Nothing blocks a magnetic field. The hull adds one of "
                    "its own instead."},
            {"text": "The spheres are heavy enough to hold the compass steady "
                     "when the ship rolls about in rough weather",
             "correct": False,
             "why": "Steadying is done by the fluid the card floats in. Iron "
                    "would be a strange choice of ballast."},
            {"text": "The spheres pull the needle round so that the compass "
                     "points at true north instead of magnetic north",
             "correct": False,
             "why": "No arrangement of iron knows where true north is. That "
                    "correction is done on the chart, using the declination."},
            {"text": "The hull has been magnetised by the Earth's field and "
                     "pulls the needle off, and the spheres cancel that",
             "correct": True},
        ],
        "figure": None,
    },
]
