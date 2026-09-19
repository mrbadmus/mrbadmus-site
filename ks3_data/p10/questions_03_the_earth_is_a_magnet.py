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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p10-03-e05",
        "band": "easier",
        "text": "The magnetic pole in the Arctic is a magnetic…",
        "options": [            {"text": "north pole", "correct": False,
             "why": "The needle's north-seeking end turns towards it, and "
                    "unlike poles attract — so it must be a south pole."},
            {"text": "north pole in summer and south in winter",
             "correct": False,
             "why": "It drifts slowly over years, but it does not swap "
                    "with the seasons."},
            {"text": "neither, because the Earth has no poles",
             "correct": False,
             "why": "The Earth has a field shaped like a bar magnet's, with "
                    "two magnetic poles."},
            {"text": "south pole", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e06",
        "band": "easier",
        "text": "The Earth's magnetic field is produced by…",
        "options": [            {"text": "moving liquid iron in the core", "correct": True},
            {"text": "a huge bar magnet buried in the core", "correct": False,
             "why": "The core is far too hot to stay magnetised, so no solid "
                    "magnet could survive there."},
            {"text": "the Earth's spin alone", "correct": False,
             "why": "Spin helps stir the core, but the field comes from the "
                    "moving iron and its currents."},
            {"text": "iron ore near the surface", "correct": False,
             "why": "Surface rocks can nudge a compass locally, but the "
                    "planet-wide field comes from far deeper."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e07",
        "band": "easier",
        "text": "Does a compass needle point exactly at true north?",
        "options": [
            {"text": "Yes, everywhere on Earth", "correct": False,
             "why": "The magnetic pole is some way from the geographic one, "
                    "so the two rarely agree."},
            {"text": "Yes, but only in Britain", "correct": False,
             "why": "Britain has a declination of its own; nowhere is exempt "
                    "by default."},
            {"text": "No — it lines up with the magnetic field instead",
             "correct": True},
            {"text": "No — it points at whatever iron is nearest",
             "correct": False,
             "why": "Nearby iron does disturb it, but out in the open it "
                    "follows the Earth's own field."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e08",
        "band": "easier",
        "text": "A compass needle is…",
        "options": [
            {"text": "a small magnet, free to turn", "correct": True},
            {"text": "a piece of plain steel with no poles", "correct": False,
             "why": "Plain steel would be attracted both ways and could not "
                    "settle pointing one way."},
            {"text": "a piece of copper wire", "correct": False,
             "why": "Copper is not magnetic and would be unaffected by the "
                    "Earth's field."},
            {"text": "an electromagnet powered by the Earth", "correct": False,
             "why": "No current runs through it; it is a permanent magnet."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e09",
        "band": "easier",
        "text": "Why does a compass needle settle in one direction rather "
                "than spinning?",
        "options": [
            {"text": "Because friction on the pivot stops it", "correct": False,
             "why": "Friction slows it down, but something has to turn it to "
                    "one particular direction first."},
            {"text": "Because it is heavier at one end", "correct": False,
             "why": "It is balanced on its pivot; weight would tip it, not "
                    "aim it north."},
            {"text": "Because the Earth's spin slowly drags the needle round "
                     "with it", "correct": False,
             "why": "Spin does not act on a needle; the magnetic field "
                    "does."},
            {"text": "Because it lines up with the Earth's magnetic field",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e10",
        "band": "easier",
        "text": "Does the Earth's magnetic pole stay in the same place?",
        "options": [
            {"text": "Yes, it has never moved", "correct": False,
             "why": "It has moved hundreds of kilometres within living "
                    "memory, which is why maps carry a date."},
            {"text": "Yes, because it is fixed to the Earth's spin axis",
             "correct": False,
             "why": "It is tilted away from the spin axis and is not attached "
                    "to it."},
            {"text": "No — it drifts, so a bearing needs a date",
             "correct": True},
            {"text": "No — it moves back and forth every day",
             "correct": False,
             "why": "The drift is slow, over years, not something that "
                    "happens daily."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p10-03-s05",
        "band": "standard",
        "text": "Why does the north-seeking end of a needle turn towards the "
                "Arctic?",
        "options": [            {"text": "Because a magnetic south pole lies that way, and unlike "
                     "poles attract",
             "correct": True},
            {"text": "Because it is attracted to the geographic North Pole",
             "correct": False,
             "why": "Geography does not attract anything; the magnetic pole "
                    "is elsewhere and is what acts on it."},
            {"text": "Because a magnetic north pole lies that way, and like "
                     "poles attract",
             "correct": False,
             "why": "Like poles repel, so a north pole up there would push "
                    "the needle away."},
            {"text": "Because the Earth spins that way", "correct": False,
             "why": "Spin has nothing to do with which way a magnet points."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s06",
        "band": "standard",
        "text": "Why is a compass unreliable on a bench covered in steel "
                "clamp stands?",
        "options": [            {"text": "Because steel blocks the Earth's field completely",
             "correct": False,
             "why": "It does not block it; it adds a field of its own that "
                    "the needle also responds to."},
            {"text": "Because a compass only works out of doors",
             "correct": False,
             "why": "It works indoors perfectly well, away from iron and "
                    "steel."},
            {"text": "Because steel makes the needle heavier", "correct": False,
             "why": "Nothing is added to the needle; it is the field around "
                    "it that has changed."},
            {"text": "Because the needle lines up with the steel's field as "
                     "well",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s07",
        "band": "standard",
        "text": "A walker follows a bearing from a map printed forty years "
                "ago and drifts off course. Why?",
        "options": [
            {"text": "Because the magnetic pole has moved since the map was "
                     "printed",
             "correct": True},
            {"text": "Because the ground has shifted since the map was made",
             "correct": False,
             "why": "The landscape has barely changed; it is the magnetic "
                    "direction that has."},
            {"text": "Because compasses get weaker with age", "correct": False,
             "why": "The walker's compass is modern, and the map is what is "
                    "out of date."},
            {"text": "Because the Earth's spin has slowed since then",
             "correct": False,
             "why": "The tiny change in spin has no effect on a bearing."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s08",
        "band": "standard",
        "text": "Why can there be no solid bar magnet inside the Earth's "
                "core?",
        "options": [
            {"text": "Because the core is liquid all the way through",
             "correct": False,
             "why": "The inner core is solid; it is the temperature that "
                    "rules a permanent magnet out."},
            {"text": "Because iron is not magnetic at that depth",
             "correct": False,
             "why": "Iron is magnetic wherever it is cool enough; heat is "
                    "what destroys the alignment."},
            {"text": "Because the core is far too hot to stay magnetised",
             "correct": True},
            {"text": "Because the pressure would crush any magnet",
             "correct": False,
             "why": "Pressure does not remove magnetism; temperature does."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s09",
        "band": "standard",
        "text": "A compass is carried into a lift with steel walls. What "
                "happens to the reading?",
        "options": [            {"text": "It is disturbed, because the steel changes the field "
                     "around the needle",
             "correct": True},
            {"text": "It becomes more accurate, because the steel focuses the "
                     "field",
             "correct": False,
             "why": "Steel disturbs the field around the needle rather than "
                    "sharpening it."},
            {"text": "Nothing changes, because steel is not magnetic",
             "correct": False,
             "why": "Steel is one of the magnetic materials, which is exactly "
                    "why it interferes."},
            {"text": "The needle spins continuously", "correct": False,
             "why": "It still settles; it simply settles pointing the wrong "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s10",
        "band": "standard",
        "text": "What does a magnetic bearing need alongside it to be worth "
                "trusting?",
        "options": [
            {"text": "The temperature at the time it was taken",
             "correct": False,
             "why": "Temperature does not shift a compass bearing "
                    "measurably."},
            {"text": "The height above sea level", "correct": False,
             "why": "Altitude makes no practical difference to the direction "
                    "the needle takes."},
            {"text": "A declination and the date it applies to", "correct": True},
            {"text": "The make of compass used", "correct": False,
             "why": "Any well-made compass gives the same reading in the same "
                    "place."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p10-03-h05",
        "band": "harder",
        "text": "Why is a compass of little use very close to the magnetic "
                "pole?",
        "options": [
            {"text": "Because the field there is so strong that the needle "
                     "simply sticks",
             "correct": False,
             "why": "A strong field would make it settle more firmly, not "
                    "less."},
            {"text": "Because the pole moves too fast to follow",
             "correct": False,
             "why": "It drifts over years, far too slowly to matter on a "
                    "single flight."},
            {"text": "Because the field disappears at the pole itself",
             "correct": False,
             "why": "It is at its strongest there; the problem is its "
                    "direction, not its size."},
            {"text": "Because the field points almost straight down, not "
                     "sideways",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h06",
        "band": "harder",
        "text": "A student says the Earth's field must come from a magnet, "
                "because it is shaped like one. What is right?",
        "options": [            {"text": "The shape is the same, but moving currents in the "
                     "liquid core make it",
             "correct": True},
            {"text": "They are right — only a magnet can make that shape",
             "correct": False,
             "why": "A coil of wire carrying a current makes the same shape, "
                    "with no magnet anywhere."},
            {"text": "The shape is different from a bar magnet's, so the "
                     "claim fails at once",
             "correct": False,
             "why": "The shape really is very close, which is what makes the "
                    "argument tempting."},
            {"text": "The Earth's field has no shape that can be mapped",
             "correct": False,
             "why": "It is mapped in detail all over the world, and used for "
                    "navigation."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h07",
        "band": "harder",
        "text": "Two compasses, one in Britain and one in New Zealand, both "
                "settle and both are said to point north. Are they parallel?",
        "options": [            {"text": "Yes — north is one fixed direction everywhere",
             "correct": False,
             "why": "The field curves round the planet, so two needles on "
                    "opposite sides are not parallel at all."},
            {"text": "Yes, provided both are the same make", "correct": False,
             "why": "The make is irrelevant; the shape of the Earth's field "
                    "is what settles it."},
            {"text": "No — the New Zealand one points south instead",
             "correct": False,
             "why": "Its north-seeking end still turns towards the Arctic "
                    "magnetic pole, as every compass does."},
            {"text": "No — each lines up with the curving field where it is",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h08",
        "band": "harder",
        "text": "Rocks on the sea floor record the Earth's field frozen in as "
                "they cooled, and stripes of it run in opposite directions. "
                "What does that show?",
        "options": [
            {"text": "That the rocks were laid down by two different volcanoes",
             "correct": False,
             "why": "The stripes are symmetrical and repeat, which no pair of "
                    "sources would produce."},
            {"text": "That the Earth's field has reversed direction in the "
                     "past",
             "correct": True},
            {"text": "That the compass was invented after the rocks formed",
             "correct": False,
             "why": "The rocks record the field whether or not anyone was "
                    "measuring it."},
            {"text": "That the rocks have been turned over since they formed",
             "correct": False,
             "why": "Whole stripes of ocean floor have not been flipped; the "
                    "field itself changed."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h09",
        "band": "harder",
        "text": "Why does a freely hung needle tip downwards at one end in "
                "Britain and the other end in New Zealand?",
        "options": [
            {"text": "Because gravity pulls harder at higher latitudes",
             "correct": False,
             "why": "The tiny change in gravity would tip both ends the same "
                    "way, not opposite ways."},
            {"text": "Because the field runs into the ground in one "
                     "hemisphere and out the other",
             "correct": True},
            {"text": "Because the needle is made differently in each country",
             "correct": False,
             "why": "The same needle carried between them behaves this way, "
                    "so it is not the instrument."},
            {"text": "Because the Earth spins the other way in the southern "
                     "hemisphere",
             "correct": False,
             "why": "The Earth spins one way; only the appearance from the "
                    "ground differs."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h10",
        "band": "harder",
        "text": "A ship's compass sits between two large iron spheres bolted "
                "either side of it. What are they for?",
        "options": [
            {"text": "To make the compass heavier so it does not swing in a "
                     "storm",
             "correct": False,
             "why": "Damping the swing is done in the compass bowl, not with "
                    "iron spheres outside it."},
            {"text": "To shield the compass from the Earth's field entirely",
             "correct": False,
             "why": "Shielding it would leave nothing for the needle to line "
                    "up with."},
            {"text": "To cancel the effect of the ship's own steel hull",
             "correct": True},
            {"text": "To make the Earth's field stronger at the needle",
             "correct": False,
             "why": "Nothing can strengthen the Earth's own field; the "
                    "spheres correct a local disturbance."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e11",
        "band": "easier",
        "text": "What is declination?",
        "options": [
            {"text": "The angle between the way a compass needle points and true "
             "north", "correct": True},
            {"text": "How fast the compass needle spins before settling", "correct": False,
             "why": "Speed of settling is not what declination measures. It is an "
                    "angle, not a speed."},
            {"text": "The distance between the magnetic pole and the equator", "correct": False,
             "why": "That is a distance, not the angle between a needle and true "
                    "north, which is what declination actually is."},
            {"text": "How far a compass needle tips away from level", "correct": False,
             "why": "That is the angle of dip, a different measurement from "
                    "declination."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e12",
        "band": "easier",
        "text": "What is true north?",
        "options": [
            {"text": "The direction a compass needle happens to point today", "correct": False,
             "why": "That direction is magnetic north, which moves. True north is "
                    "fixed by the Earth's spin, not by a compass reading."},
            {"text": "The end of the axis the Earth spins on, where lines of "
             "longitude meet", "correct": True},
            {"text": "The place where the Earth's magnetic field is strongest "
                     "on the surface", "correct": False,
             "why": "True north is a geographic fact about the spin axis. It has "
                    "nothing to do with where the field is strongest."},
            {"text": "Wherever a map happens to print north at the top", "correct": False,
             "why": "A map's own printed direction is grid north, a third, "
                    "separate idea from true north."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e13",
        "band": "easier",
        "text": "At the equator, what is the angle of dip?",
        "options": [
            {"text": "It cannot be measured at the equator", "correct": False,
             "why": "It can be measured anywhere on Earth, and at the equator it "
                    "comes out as 0°."},
            {"text": "90°", "correct": False,
             "why": "90° is the dip directly over the magnetic pole, not at the "
                    "equator."},
            {"text": "0°", "correct": True},
            {"text": "45°, exactly half way between the two extremes", "correct": False,
             "why": "The equator is where the field runs level, giving a dip of "
                    "0°, not a value half way to the pole's 90°."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e14",
        "band": "easier",
        "text": "Directly above the magnetic pole, what is the angle of dip?",
        "options": [
            {"text": "It depends on the time of year", "correct": False,
             "why": "Dip at the pole does not change with the seasons. It is set "
                    "by the field's direction there, which is straight down."},
            {"text": "0°, since the pole is where the field runs level", "correct": False,
             "why": "0° dip is what happens at the equator, not at the magnetic "
                    "pole."},
            {"text": "45°, half way between level and straight down", "correct": False,
             "why": "45° would be some way between the equator and the pole, not "
                    "directly over the pole itself."},
            {"text": "90°", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e15",
        "band": "easier",
        "text": "Which of these two places sits closer to the Earth's magnetic "
                "pole: Madrid, or northern Norway?",
        "options": [
            {"text": "Northern Norway", "correct": True},
            {"text": "They are exactly the same distance from it", "correct": False,
             "why": "The two places are at very different latitudes, so one is "
                    "genuinely much closer to the pole than the other."},
            {"text": "Distance to the pole cannot be compared between two places", "correct": False,
             "why": "It can be compared directly from how far north each place "
                    "sits."},
            {"text": "Madrid", "correct": False,
             "why": "Madrid is much closer to the equator than to the magnetic "
                    "pole, while northern Norway sits well to the north of it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e16",
        "band": "easier",
        "text": "Is the Earth's MAGNETIC equator in exactly the same place as the "
                "geographic equator?",
        "options": [
            {"text": "Yes, always exactly the same line", "correct": False,
             "why": "The magnetic axis is tilted from the spin axis, so the two "
                    "equators are not exactly the same line."},
            {"text": "No — the magnetic axis is tilted from the spin axis, so "
                     "they do not line up exactly", "correct": True},
            {"text": "No, they are on completely opposite sides of the planet "
                     "from one another, pole for pole", "correct": False,
             "why": "They are close to each other, not on opposite sides — only "
                    "tilted slightly apart, not far away."},
            {"text": "There is no such thing as a magnetic equator", "correct": False,
             "why": "There is a magnetic equator: it is where the field runs "
                    "level, giving zero dip, close to but not exactly on the "
                    "geographic equator."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e17",
        "band": "easier",
        "text": "Which of these animals is known to navigate using the Earth's "
                "magnetic field?",
        "options": [
            {"text": "Snails", "correct": False,
             "why": "Snails are not known to navigate this way. Robins are a "
                    "well-known example of an animal that does."},
            {"text": "Woodlice", "correct": False,
             "why": "Woodlice are not one of the examples known for this. Robins "
                    "are."},
            {"text": "Robins", "correct": True},
            {"text": "Earthworms", "correct": False,
             "why": "Earthworms are not among the animals known for this kind of "
                    "navigation. Robins are a well-known example."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e18",
        "band": "easier",
        "text": "Some bacteria grow a chain of tiny magnetic crystals inside "
                "themselves. What does this chain do?",
        "options": [
            {"text": "It stores food for the bacterium, a supply of iron it can "
                     "draw on when it needs it", "correct": False,
             "why": "The crystals are not a food store. Their role is lining the "
                    "bacterium up with the field."},
            {"text": "It protects the bacterium from being eaten, giving it a "
                     "hard spine a predator cannot swallow", "correct": False,
             "why": "The crystals are not a defence. They line the bacterium up "
                    "with the field, which is a navigation role, not protection."},
            {"text": "It lets the bacteria swim faster through water, the same way a "
             "streamlined shape would cut through the water more easily", "correct": False,
             "why": "The chain does not add speed. It swings the bacterium into "
                    "line with the field, like a tiny compass needle."},
            {"text": "It swings the bacterium into line with the field, like a "
             "compass needle", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e19",
        "band": "easier",
        "text": "Roughly how long ago did the Earth's magnetic field last reverse "
                "direction?",
        "options": [
            {"text": "About 780,000 years ago", "correct": True},
            {"text": "About 780 years ago", "correct": False,
             "why": "That is far too recent. The last reversal happened hundreds "
                    "of thousands of years ago, not centuries."},
            {"text": "It has never reversed", "correct": False,
             "why": "The field has reversed many times, recorded in stacks of old "
                    "lava flows around the world."},
            {"text": "It reverses every single year", "correct": False,
             "why": "Reversals are hugely rare events, hundreds of thousands of "
                    "years apart, not an annual occurrence."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e20",
        "band": "easier",
        "text": "During a magnetic reversal, does the Earth's field simply vanish "
                "for a while?",
        "options": [
            {"text": "Yes, it disappears completely until the reversal finishes "
                     "and the new poles have settled into place", "correct": False,
             "why": "It does not vanish. It becomes tangled, with several poles "
                    "existing at once for a while, rather than switching off."},
            {"text": "No — it becomes tangled, with several poles existing at once "
             "for a while", "correct": True},
            {"text": "Yes, and the Earth becomes non-magnetic for millions of "
                     "years, until the core starts turning the other way", "correct": False,
             "why": "The tangled period lasts a few thousand years, not millions, "
                    "and the field does not switch off during it."},
            {"text": "No, nothing changes about the field during a reversal", "correct": False,
             "why": "Something does change — the field becomes tangled and more "
                    "complicated for a while before settling into its new, "
                    "reversed direction."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e21",
        "band": "easier",
        "text": "The sideways pull is reported on a scale where the strongest "
                "value, at the equator, is set to 100. What does a reading of 50 "
                "somewhere else tell you?",
        "options": [
            {"text": "The sideways pull there is fifty times stronger than at the "
             "equator", "correct": False,
             "why": "A reading of 50 is HALF of 100, not fifty times bigger. The "
                    "scale runs the other way."},
            {"text": "The dip there must be exactly 50°", "correct": False,
             "why": "This reading is about the sideways pull, a separate "
                    "measurement from the angle of dip."},
            {"text": "The sideways pull there is half as strong as at the equator", "correct": True},
            {"text": "The sideways pull there is fifty newtons, which is the "
                     "force it puts on a compass needle", "correct": False,
             "why": "The scale is a comparison against the equator's 100, not a "
                    "force: no reading here is given in newtons at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e22",
        "band": "easier",
        "text": "At a given place, are the angle of dip and the sideways pull the "
                "SAME reading, or two separate ones?",
        "options": [
            {"text": "The sideways pull is simply the dip measured in a different "
             "unit", "correct": False,
             "why": "They are not the same quantity in different units. One is a "
                    "tipping angle; the other is a strength."},
            {"text": "Neither reading can be taken at the same place as the other", "correct": False,
             "why": "Both can be read at the same spot, one after the other — "
                    "they are simply two different things about the field "
                    "there."},
            {"text": "The same reading, just given two different names", "correct": False,
             "why": "They are genuinely different measurements: one is an angle "
                    "from level, the other is how strong the sideways part of the "
                    "field is."},
            {"text": "Two separate readings, taken at the same spot", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e23",
        "band": "easier",
        "text": "Is the Earth's magnetic axis lined up exactly with the axis it "
                "spins on?",
        "options": [
            {"text": "No — the magnetic axis is tilted by around eleven degrees "
                     "from the spin axis", "correct": True},
            {"text": "No, the two axes are at right angles to each other", "correct": False,
             "why": "The tilt is a modest one, around eleven degrees, not a full "
                    "right angle."},
            {"text": "The Earth does not have a spin axis at all, only a "
                     "magnetic one for the poles to sit on", "correct": False,
             "why": "The Earth spins on its own axis, which is a separate, "
                    "geographic fact from its magnetic axis."},
            {"text": "Yes, they are exactly the same line", "correct": False,
             "why": "The magnetic axis is tilted by around eleven degrees from the "
                    "spin axis, so the two are not exactly the same."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e24",
        "band": "easier",
        "text": "Which of these moves noticeably from year to year: true north, or "
                "the magnetic pole?",
        "options": [
            {"text": "True north", "correct": False,
             "why": "True north is set by the spin axis and does not wander. It is "
                    "the magnetic pole that drifts."},
            {"text": "The magnetic pole", "correct": True},
            {"text": "Both move by the same amount each year", "correct": False,
             "why": "True north stays fixed; only the magnetic pole drifts "
                    "noticeably year on year."},
            {"text": "Neither of them moves", "correct": False,
             "why": "The magnetic pole does move, by tens of kilometres a year, "
                    "even though true north does not."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e25",
        "band": "easier",
        "text": "Why is one end of a compass needle called its north-seeking end?",
        "options": [
            {"text": "Because that end was made from iron mined in the far north",
             "correct": False,
             "why": "Where the metal came from makes no difference to which way "
                    "it points. The name describes what the end DOES."},
            {"text": "Because that end is the only part of the needle that has "
                     "been magnetised", "correct": False,
             "why": "Both ends are magnetised: a magnet cannot have one end "
                    "without the other. The two ends simply seek opposite ways."},
            {"text": "Because that is the end that turns to face north when the "
                     "needle settles", "correct": True},
            {"text": "Because that end is a magnetic south pole, and south poles "
                     "are drawn pointing north", "correct": False,
             "why": "The north-seeking end is itself a magnetic north pole. The "
                    "pole it turns towards is the opposite kind to it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e26",
        "band": "easier",
        "text": "Why does a serious map for navigation print a date next to its "
                "declination value?",
        "options": [
            {"text": "Because true north itself changes from year to year as "
                     "the Earth's axis slowly shifts round", "correct": False,
             "why": "True north does not change. It is the magnetic pole's "
                    "position that drifts, which is why the date matters."},
            {"text": "Because the paper the map is printed on fades over time, "
                     "so the printed angle grows harder to read accurately", "correct": False,
             "why": "Fading paper is not the reason. The date matters because the "
                    "magnetic pole itself has moved since the value was measured."},
            {"text": "Because compasses wear out and need replacing after a few "
             "years, the same way any mechanical instrument gradually loses "
             "its accuracy with age", "correct": False,
             "why": "The compass instrument is not the issue — the PRINTED "
                    "declination value becomes out of date as the pole drifts."},
            {"text": "Because the magnetic pole drifts, so an old declination value "
             "can become out of date", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e27",
        "band": "easier",
        "text": "How does the Earth's magnetic field at a compass needle compare "
                "with the field of a small bar magnet held right beside it?",
        "options": [
            {"text": "Much weaker, which is why a magnet held nearby easily "
                     "overrides it", "correct": True},
            {"text": "Much stronger, because the Earth is far bigger than any "
                     "piece of magnetised steel", "correct": False,
             "why": "The size of the source is not the same as the strength at "
                    "the needle. The Earth's field is made thousands of "
                    "kilometres down, and it is very weak by the time it "
                    "reaches the surface."},
            {"text": "Exactly the same, which is why a compass can be used right "
                     "beside a magnet", "correct": False,
             "why": "A magnet held beside a compass swamps the Earth's field "
                    "completely, which is why a bearing taken there is useless."},
            {"text": "Weaker outdoors but stronger indoors, where there is less "
                     "open air for it to cross", "correct": False,
             "why": "Air neither carries nor blocks a magnetic field, so being "
                    "indoors or outdoors makes no difference to the Earth's "
                    "field at the needle."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e28",
        "band": "easier",
        "text": "The angle of dip is measured from which reference line?",
        "options": [
            {"text": "From whichever way the wind is blowing", "correct": False,
             "why": "Wind direction has nothing to do with a magnetic measurement "
                    "like dip."},
            {"text": "From level (the horizontal)", "correct": True},
            {"text": "From true north", "correct": False,
             "why": "The angle from true north is declination, a different "
                    "measurement from dip."},
            {"text": "From the vertical, straight up", "correct": False,
             "why": "Dip is measured from level (horizontal), not from straight "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e29",
        "band": "easier",
        "text": "Why is an ordinary walking compass built with a flat card rather "
                "than left free to tip?",
        "options": [
            {"text": "So that it needs no pivot, since a flat card can slide "
                     "round on the fluid inside the case instead", "correct": False,
             "why": "A walking compass still has a pivot to let the card turn — "
                    "being flat is about which part of the field it responds to."},
            {"text": "So it can be read equally well upside down, which matters on a "
             "device that might be knocked about while being carried in a "
             "pocket or bag", "correct": False,
             "why": "Being flat is not about reading it upside down. It is about "
                    "isolating the sideways part of the field."},
            {"text": "So it only responds to the sideways part of the field, which "
             "is what gives a useful bearing", "correct": True},
            {"text": "So it looks neater when packed away", "correct": False,
             "why": "Appearance is not the reason. It is built flat so that only "
                    "the useful, sideways part of the field turns it."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-e30",
        "band": "easier",
        "text": "Why is a compass needle balanced on an almost frictionless pivot?",
        "options": [
            {"text": "So that it never needs to be replaced, since a pivot that "
                     "does not rub will not wear down", "correct": False,
             "why": "Durability is not the reason for a low-friction pivot. It is "
                    "there so the needle can turn freely to follow the field."},
            {"text": "So that it spins continuously once it is set going, "
                     "keeping the needle loose for the next reading", "correct": False,
             "why": "A working compass needle settles to a direction and stops; a "
                    "low-friction pivot lets it reach that direction freely, not "
                    "spin forever."},
            {"text": "So that it can be read from any angle without being picked up, "
             "the same way a wall clock is designed to be read from across a "
             "room", "correct": False,
             "why": "Being readable from any angle is not what the pivot is for. "
                    "It lets the needle turn with as little resistance as "
                    "possible."},
            {"text": "So it can turn freely to follow the field, rather than being "
             "held in a wrong direction by friction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s11",
        "band": "standard",
        "text": "20° north (southern Egypt) and 70° north (northern Norway) are "
                "compared. Which place has the STEEPER angle of dip?",
        "options": [
            {"text": "70° north — dip grows steeper the further you go from the "
             "equator", "correct": True},
            {"text": "20° north — dip is steeper nearer the equator", "correct": False,
             "why": "Dip is closest to zero (least steep) near the equator. It "
                    "grows steeper further away, not nearer."},
            {"text": "Both are exactly the same, since both are in the northern "
             "hemisphere", "correct": False,
             "why": "Being in the same hemisphere does not make the dip equal. "
                    "Distance from the equator is what decides how steep it is."},
            {"text": "Neither has a meaningful dip, since both are far from the pole "
             "itself", "correct": False,
             "why": "Dip is meaningful and measurable everywhere, not only very "
                    "close to the pole."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s12",
        "band": "standard",
        "text": "Compare the sideways pull at the equator with the sideways pull at "
                "70° north. Which is bigger?",
        "options": [
            {"text": "Sideways pull cannot be compared between two different "
             "latitudes", "correct": False,
             "why": "It can be compared directly, since both places are read on "
                    "the same relative scale."},
            {"text": "The equator's sideways pull is bigger", "correct": True},
            {"text": "70° north's sideways pull is bigger", "correct": False,
             "why": "The sideways pull falls away the further you go from the "
                    "equator, so 70° north reads lower, not higher."},
            {"text": "They are exactly the same everywhere on Earth", "correct": False,
             "why": "The sideways pull genuinely varies with latitude — it is "
                    "largest at the equator and smallest near the pole."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s13",
        "band": "standard",
        "text": "A ship sits exactly on the GEOGRAPHIC equator. Would you "
                "expect its compass to show EXACTLY 0° dip?",
        "options": [
            {"text": "No, it would read close to 90°, the same as at a pole, "
                     "because the tilt of the magnetic axis throws the reading "
                     "right over", "correct": False,
             "why": "The geographic equator is nowhere near the magnetic pole, so "
                    "a reading anywhere near 90° would not be expected there."},
            {"text": "The compass would give no reading on the equator, the "
                     "same way it gives none anywhere far from a magnet or a "
                     "planetary field", "correct": False,
             "why": "A compass reads perfectly well on the equator — it is simply "
                    "not guaranteed to read EXACTLY zero, since the two equators "
                    "are not identical."},
            {"text": "Not necessarily — the magnetic equator is not exactly the same "
             "line as the geographic one, so the dip there may be slightly "
             "off zero", "correct": True},
            {"text": "Yes, always exactly 0°, since it is on the equator", "correct": False,
             "why": "Zero dip happens on the MAGNETIC equator specifically, which "
                    "is tilted slightly away from the geographic one."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s14",
        "band": "standard",
        "text": "A robin is thought to sense the Earth's magnetic field directly, "
                "with no separate instrument. How is this different from how a "
                "human finds a bearing?",
        "options": [
            {"text": "There is no real difference — humans also sense the field "
                     "directly, which is how people find their way in the dark", "correct": False,
             "why": "Humans have no known direct sense for the field and rely on a "
                    "separate instrument, unlike the robin."},
            {"text": "The robin uses a compass carried inside its body, "
                     "identical to a human's, with a tiny needle on a pivot of "
                     "its own", "correct": False,
             "why": "The robin is not thought to carry anything like a "
                    "manufactured compass — it appears to sense the field with its "
                    "own body some other way."},
            {"text": "Robins do not use the Earth's field, and find their way "
                     "south by the position of the Sun and the stars alone", "correct": False,
             "why": "Robins are one of the animals thought to navigate using the "
                    "Earth's field, even though exactly how is still argued about."},
            {"text": "A human normally needs a separate device, a compass, while the "
             "robin's own body appears to sense the field", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s15",
        "band": "standard",
        "text": "Reversals of the Earth's field are known from the record kept "
                "in old rocks. Do they happen at regular, evenly spaced "
                "intervals?",
        "options": [
            {"text": "No — reversals happen at irregular intervals, not on a fixed, "
             "predictable schedule", "correct": True},
            {"text": "Yes, every reversal is exactly the same number of years apart", "correct": False,
             "why": "The record shows the timing between reversals varies; it is "
                    "not a fixed, evenly spaced schedule."},
            {"text": "Reversals happen once and once alone, so there is no "
                     "timing to compare", "correct": False,
             "why": "The record shows many reversals throughout Earth's history, "
                    "not a single one-off event."},
            {"text": "The timing can only be found by asking when the next one will "
             "happen", "correct": False,
             "why": "The timing between PAST reversals is read directly from the "
                    "rock record; predicting the NEXT one is a separate, much "
                    "harder question."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s16",
        "band": "standard",
        "text": "One place reads 25 on the sideways-pull scale, where the equator "
                "reads 100. How does its sideways pull compare with the equator's?",
        "options": [
            {"text": "Exactly the same strength, just measured differently", "correct": False,
             "why": "A reading of 25 against 100 is a real, smaller value — not "
                    "the same strength read a different way."},
            {"text": "A quarter as strong", "correct": True},
            {"text": "Four times as strong", "correct": False,
             "why": "25 is a QUARTER of 100, not four times as much — the reading "
                    "is smaller than the equator's, not bigger."},
            {"text": "Twenty-five times as strong", "correct": False,
             "why": "The scale is a direct comparison out of 100, not a multiplier "
                    "of 25 on top of the equator's value."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s17",
        "band": "standard",
        "text": "A mystery location gives a LARGE angle of dip and a SMALL "
                "sideways-pull reading. What kind of latitude does this suggest?",
        "options": [
            {"text": "It tells you nothing about the latitude, since both "
                     "readings depend on the rocks underfoot", "correct": False,
             "why": "Both dip and sideways pull change in a clear pattern with "
                    "latitude, so together they do point towards a particular kind "
                    "of location."},
            {"text": "It could be measured at sea but not on land, because a "
                     "ship's compass is the one free to tip", "correct": False,
             "why": "These readings are about latitude, not about whether the "
                    "ground beneath is sea or land."},
            {"text": "One well away from the equator, closer to a magnetic pole", "correct": True},
            {"text": "One right on the equator", "correct": False,
             "why": "The equator gives a small dip and the LARGEST sideways pull, "
                    "the opposite pattern from this reading."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s18",
        "band": "standard",
        "text": "Does the tilt of the Earth's magnetic axis cause a problem "
                "only in the NORTHERN hemisphere, or does it affect the "
                "southern hemisphere's readings too?",
        "options": [
            {"text": "It affects the Arctic alone, since that is where the tilt "
                     "was measured and where the two norths sit furthest apart", "correct": False,
             "why": "The axis runs all the way through the planet, so a tilt at "
                    "one end is the same tilt at the other end too."},
            {"text": "It cancels out by the time it reaches the southern "
                     "hemisphere, halfway round the planet from where the tilt "
                     "begins", "correct": False,
             "why": "Tilt does not cancel out over distance. Both ends of one "
                    "tilted axis are offset from true north and south."},
            {"text": "The southern hemisphere has its own separate, untilted "
                     "magnetic axis, lined up neatly with the axis it spins on", "correct": False,
             "why": "There is only one magnetic axis for the whole planet, and it "
                    "is tilted throughout its length."},
            {"text": "It affects the southern hemisphere too — the tilt is a "
                     "property of the whole axis, not just one end", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s19",
        "band": "standard",
        "text": "Declination in Britain is close to zero at the moment, but in "
                "parts of Canada it is more than twenty degrees. What does this "
                "difference mainly depend on?",
        "options": [
            {"text": "How that particular place sits relative to where the magnetic "
             "pole actually is", "correct": True},
            {"text": "How advanced the country's own compass-making industry "
                     "happens to be at the moment", "correct": False,
             "why": "Declination is a property of a PLACE relative to the pole. It "
                    "has nothing to do with who manufactures compasses there."},
            {"text": "How close the country is to the geographic equator", "correct": False,
             "why": "Distance to the equator affects dip more directly. "
                    "Declination depends on direction to the magnetic pole from "
                    "that spot."},
            {"text": "The average temperature of the country", "correct": False,
             "why": "Climate has no bearing on declination, which comes purely "
                    "from the geometry between a place and the magnetic pole."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s20",
        "band": "standard",
        "text": "Declination and dip are both angles read from a compass set-up, "
                "but they answer different questions. Which question does "
                "DECLINATION answer?",
        "options": [
            {"text": "How fast does the needle settle once released?", "correct": False,
             "why": "Settling speed is not one of the standard readings this "
                    "lesson describes at all."},
            {"text": "How far off true north does the needle point?", "correct": True},
            {"text": "How far does the needle tip away from level?", "correct": False,
             "why": "That question is answered by the angle of dip, not "
                    "declination."},
            {"text": "How strong is the sideways part of the field?", "correct": False,
             "why": "Sideways strength is a separate reading again, not what "
                    "declination measures."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s21",
        "band": "standard",
        "text": "Aircraft near the magnetic pole in the Arctic switch away from a "
                "magnetic compass. Would you expect the SAME problem to occur "
                "flying close to the magnetic pole in the far south?",
        "options": [
            {"text": "No — the southern magnetic pole has no sideways field "
                     "problem, because the field runs level across the "
                     "Antarctic", "correct": False,
             "why": "The southern pole behaves the same way as the northern one: "
                    "the field points steeply down there too, leaving little "
                    "sideways pull."},
            {"text": "It is impossible to say without a real flight test", "correct": False,
             "why": "The behaviour follows directly from how the field works near "
                    "ANY magnetic pole, which can be reasoned out without a fresh "
                    "flight test."},
            {"text": "Yes — the sideways part of the field shrinks close to EITHER "
             "magnetic pole, north or south", "correct": True},
            {"text": "No — the Arctic pole is the only one that troubles a "
                     "compass, since it is the pole the needle's north end "
                     "seeks", "correct": False,
             "why": "The same shrinking of the sideways field happens near the "
                    "southern magnetic pole too, for the same reason."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s22",
        "band": "standard",
        "text": "Why does a walking compass need a counterweight built under its "
                "card at higher latitudes?",
        "options": [
            {"text": "To make the compass heavier so that wind cannot blow it "
                     "off course out on an exposed hillside", "correct": False,
             "why": "Wind resistance is not the purpose. The counterweight "
                    "balances the tipping effect of the field, which is stronger "
                    "at higher latitudes."},
            {"text": "To stop the needle spinning too fast when it is first "
                     "released and overshooting the bearing wanted", "correct": False,
             "why": "Spin speed is not the issue being solved. The counterweight "
                    "is there to counter the field's tipping effect."},
            {"text": "To make the compass card float properly in the fluid that "
                     "fills its case", "correct": False,
             "why": "Floating is a separate design detail. The counterweight "
                    "specifically balances the tipping caused by dip."},
            {"text": "To balance out the field's tendency to tip the needle, keeping "
             "the card level", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s23",
        "band": "standard",
        "text": "52° north (southern England) has a dip of about 69°, and 70° north "
                "(northern Norway) has a dip of about 80°. Does this fit the "
                "general trend for how dip changes with latitude?",
        "options": [
            {"text": "Yes — dip keeps growing steeper as you go further from the "
             "equator", "correct": True},
            {"text": "No — dip should be smaller at the higher latitude, not bigger", "correct": False,
             "why": "The general trend is the opposite: dip grows steeper, not "
                    "smaller, further from the equator, which is exactly what "
                    "these two figures show."},
            {"text": "No — the two values should be identical if the trend were real", "correct": False,
             "why": "The trend is a steady change with latitude, not a flat, "
                    "identical value everywhere — these two figures are exactly "
                    "what a steady change looks like."},
            {"text": "It cannot be judged without knowing the exact longitude of "
             "each place", "correct": False,
             "why": "Dip's general trend is judged from latitude. Longitude is not "
                    "needed to see that it fits the pattern here."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s24",
        "band": "standard",
        "text": "A single lava sample shows a reversed field direction. Why is one "
                "sample alone not enough to prove a global reversal happened?",
        "options": [
            {"text": "A reversal can be confirmed with a compass alone, and not "
                     "from rock", "correct": False,
             "why": "Reversals from the deep past are confirmed using exactly this "
                    "kind of rock evidence, since no compass existed then."},
            {"text": "A single sample could reflect a local disturbance; the same "
             "reversed pattern needs to show up in many samples worldwide, "
             "in the same order", "correct": True},
            {"text": "One sample is too small to measure accurately", "correct": False,
             "why": "Size of the sample is not the issue here — the point is "
                    "confirming the pattern is GLOBAL, not just local, using many "
                    "samples."},
            {"text": "Lava cannot record a magnetic field, so a single sample "
                     "proves nothing about which way the field was pointing "
                     "while the rock was still molten", "correct": False,
             "why": "Lava genuinely does record the field as it cools. The issue "
                    "is confirming the pattern globally, not whether recording "
                    "happens at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s25",
        "band": "standard",
        "text": "A submarine plans to surface very close to the southern magnetic "
                "pole. Based on what happens to aircraft near the northern one, "
                "what problem should the crew expect with their magnetic compass?",
        "options": [
            {"text": "It will point reliably at true south instead of magnetic south", "correct": False,
             "why": "A compass never points at true anything — it lies along the "
                    "field, and near a pole that field gives it little sideways "
                    "direction to follow."},
            {"text": "It will be completely unaffected, since the problem "
                     "happens in the Arctic", "correct": False,
             "why": "The same field pattern occurs near the southern magnetic "
                    "pole, for the same reason as the northern one."},
            {"text": "It will settle slowly or fail to give a useful bearing, since "
             "the sideways field is very weak there", "correct": True},
            {"text": "It will work better than usual, since polar regions have "
                     "the strongest total field for a needle to lock on to", "correct": False,
             "why": "A strong TOTAL field there is mostly pointing straight down, "
                    "not sideways, which is what actually gives a compass a "
                    "bearing to use."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s26",
        "band": "standard",
        "text": "A freely hung compass needle is carried from Britain (northern "
                "hemisphere) down to New Zealand (southern hemisphere). Which end "
                "of the needle tips downward changes along the way. At roughly what "
                "point does this switch happen?",
        "options": [
            {"text": "Only once the needle reaches New Zealand, where the "
                     "ground below it finally changes over", "correct": False,
             "why": "The switch happens where the field itself changes from "
                    "tipping one way to tipping the other, which is around the "
                    "magnetic equator, not at the destination."},
            {"text": "It never switches — the same end always tips down everywhere", "correct": False,
             "why": "The tipping direction genuinely reverses between hemispheres, "
                    "which is exactly why the switch point matters."},
            {"text": "Exactly at the international date line, where one side of "
                     "the world is handed over to the other", "correct": False,
             "why": "The date line is about time zones, not about the Earth's "
                    "magnetic field, so it has no bearing on where the tipping "
                    "switches."},
            {"text": "Around the magnetic equator, where the field runs level", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s27",
        "band": "standard",
        "text": "20° south (northern Australia) reads 94.0 on the sideways -pull "
                "scale, where the equator reads 100.0. What does this closeness in "
                "value show about 20° south?",
        "options": [
            {"text": "It is still fairly close to level there, not far from the "
             "equator's own behaviour", "correct": True},
            {"text": "It must actually be exactly on the magnetic equator itself", "correct": False,
             "why": "A reading close to 100 does not mean exactly on the equator — "
                    "it means fairly close to level, which is consistent with "
                    "being a modest distance from it."},
            {"text": "It shows the dip there must be close to 90°", "correct": False,
             "why": "A HIGH sideways reading goes with a SMALL dip, not a large "
                    "one — the two move in opposite directions."},
            {"text": "The reading tells you nothing about how level the field "
                     "is there", "correct": False,
             "why": "The sideways-pull reading is exactly the measurement that "
                    "reflects how level or steep the field is at that spot."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s28",
        "band": "standard",
        "text": "A claim is made: \"True north and magnetic north are the same thing "
                "everywhere on Earth, because in Britain they are almost the same.\" "
                "What is wrong with generalising from the British case like this?",
        "options": [
            {"text": "Magnetic north does not exist anywhere on Earth", "correct": False,
             "why": "Magnetic north is also real — it is simply not always close "
                    "to true north, as Britain's current small declination might "
                    "suggest."},
            {"text": "Britain's declination happens to be small at the moment, but "
             "declination is much larger elsewhere, such as parts of Canada", "correct": True},
            {"text": "Nothing is wrong — the claim is correct for the whole "
                     "planet, since the two norths are set by the same axis and "
                     "cannot drift apart", "correct": False,
             "why": "The claim only looks right because Britain currently has an "
                    "unusually small declination; other places show a large gap "
                    "between the two norths."},
            {"text": "True north does not exist as a real direction anywhere on "
                     "Earth, since every direction drawn on a globe is a matter "
                     "of convention", "correct": False,
             "why": "True north is a real, fixed geographic direction — the issue "
                    "is only that it does not always coincide closely with "
                    "magnetic north."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s29",
        "band": "standard",
        "text": "The magnetic pole drifts by tens of kilometres a year. After ten "
                "years, would a declination value from an old map necessarily still "
                "be trustworthy?",
        "options": [
            {"text": "No, a map's declination value never changes once it is printed", "correct": False,
             "why": "The PRINTED value is fixed, but the REAL declination keeps "
                    "changing as the pole drifts, which is exactly the problem "
                    "with using it unchanged."},
            {"text": "It depends on the paper quality of the map rather than on "
                     "how much time has passed since it was surveyed", "correct": False,
             "why": "Paper quality is irrelevant. What matters is how much the "
                    "real magnetic pole has drifted since the value was measured."},
            {"text": "Not necessarily — ten years of drift can add up to a "
             "noticeable shift in declination in some places", "correct": True},
            {"text": "Yes, since ten years is far too short a time for the pole "
                     "to drift far enough to matter to anyone on foot with a "
                     "map", "correct": False,
             "why": "Tens of kilometres a year, over ten years, can add up to a "
                    "genuinely noticeable shift, depending on the place."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-s30",
        "band": "standard",
        "text": "A student claims a compass would be completely useless anywhere "
                "the dip is large, even far from any pole, because the needle would "
                "be tipping so much. What is the flaw in this claim?",
        "options": [
            {"text": "There is no flaw — dip does make every kind of compass "
                     "useless wherever it is large, since a tipped needle drags "
                     "badly on its pivot", "correct": False,
             "why": "A flat, walking-style compass is specifically designed to "
                    "avoid this problem by responding only to the sideways part of "
                    "the field."},
            {"text": "Dip stays small everywhere except directly over a pole, "
                     "so nowhere else could be affected by it in the first "
                     "place", "correct": False,
             "why": "Dip grows gradually with distance from the equator; it can be "
                    "fairly large well before reaching a pole, not only exactly at "
                    "one."},
            {"text": "A large dip makes a compass MORE accurate, not less, "
                     "because a steeper field pulls the needle onto its bearing "
                     "harder", "correct": False,
             "why": "A large dip does not improve accuracy — it is the SIDEWAYS "
                    "pull, not the dip, that a walking compass relies on for a "
                    "useful bearing."},
            {"text": "An ordinary walking compass is built flat, so it only responds "
             "to the sideways part of the field regardless of how large the "
             "dip is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h11",
        "band": "harder",
        "text": "If the Earth's magnetic poles fully reversed overnight, what would "
                "change about a compass needle's behaviour in Britain the next "
                "morning?",
        "options": [
            {"text": "The needle's north-seeking end would now turn towards the "
             "Antarctic instead of the Arctic", "correct": True},
            {"text": "Nothing would change about how the needle behaves, "
                     "because a needle is drawn to the geographic north pole "
                     "itself", "correct": False,
             "why": "Reversing the poles would reverse which direction the "
                    "needle's north-seeking end turns towards — a real, noticeable "
                    "change."},
            {"text": "The needle would stop working completely and never settle "
                     "again, because it was magnetised to suit the old field "
                     "and cannot follow a new one", "correct": False,
             "why": "The needle would still settle along the field — it would "
                    "simply settle pointing the opposite way from before."},
            {"text": "The needle would start spinning continuously forever", "correct": False,
             "why": "A reversed field still gives the needle a definite direction "
                    "to settle along; there is no reason for it to spin "
                    "continuously."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h12",
        "band": "harder",
        "text": "During a reversal, the field is described as tangled, with several "
                "poles existing at once for a few thousand years. Explain why "
                "navigation by compass would be harder DURING this period than "
                "either before or after it.",
        "options": [
            {"text": "There is no extra difficulty — a tangled field still "
                     "gives one clear, consistent direction everywhere, because "
                     "the several poles average out into one", "correct": False,
             "why": "A tangled field with several poles at once is specifically "
                    "LESS consistent from place to place than the normal, settled "
                    "two-pole pattern."},
            {"text": "With several poles active at once, a compass would no longer "
             "reliably settle towards one consistent direction across a wide "
             "area", "correct": True},
            {"text": "The compass needle itself would physically melt during a "
             "reversal", "correct": False,
             "why": "Nothing about a reversal directly heats a compass needle. The "
                    "problem is the field's own tangled, inconsistent direction "
                    "during that period."},
            {"text": "Compasses would be banned by law during a reversal", "correct": False,
             "why": "This is a physical difficulty with the field itself, not a "
                    "legal restriction on using a compass."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h13",
        "band": "harder",
        "text": "A geologist finds a lava layer whose frozen-in field direction is "
                "neither clearly \"normal\" nor cleanly \"reversed\", but somewhere "
                "confused in between. What does this most likely suggest about when "
                "the lava cooled?",
        "options": [
            {"text": "The lava must have cooled extremely slowly, over millions "
                     "of years, so the minerals kept swinging round as it set", "correct": False,
             "why": "Cooling speed is not what produces a confused direction — "
                    "cooling during the tangled, mid-reversal period does."},
            {"text": "This kind of reading is impossible and would not be "
                     "found, since rock records one direction or the other", "correct": False,
             "why": "Such in-between readings genuinely are found in real rock "
                    "records, exactly where a reversal is thought to have been "
                    "under way."},
            {"text": "It cooled during a reversal itself, while the field was "
             "tangled with several poles at once", "correct": True},
            {"text": "The rock must have been measured using broken equipment", "correct": False,
             "why": "A confused reading is exactly what is expected from rock that "
                    "cooled DURING a reversal, not necessarily a sign of faulty "
                    "equipment."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h14",
        "band": "harder",
        "text": "Since every magnet must have a matching pair of poles, what does "
                "the Arctic's magnetic SOUTH pole imply about Antarctica?",
        "options": [
            {"text": "Antarctica must have no magnetic pole of any kind, since "
                     "the one pole in the Arctic serves the whole planet", "correct": False,
             "why": "A magnet's poles always come as a matching pair — having a "
                    "south pole at one end requires a north pole at the other."},
            {"text": "Antarctica must have its own separate south pole, unconnected "
             "to the Arctic one", "correct": False,
             "why": "The Earth's field behaves as ONE magnet with two ends, so "
                    "Antarctica's pole is the matching NORTH end of the same "
                    "field, not an unconnected second south."},
            {"text": "The pairing rule for ordinary magnets does not apply to the "
             "whole Earth", "correct": False,
             "why": "The Earth's field is treated as behaving like a giant bar "
                    "magnet, so the same pairing rule applies to it as to any "
                    "other magnet."},
            {"text": "Antarctica must hold the Earth's matching magnetic NORTH "
                     "pole", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h15",
        "band": "harder",
        "text": "A student says: \"Since the Arctic pole attracts the needle's north "
                "end, and the Antarctic pole is the matching north pole, the "
                "needle's SOUTH end must be attracted towards Antarctica too.\" Is "
                "this reasoning sound?",
        "options": [
            {"text": "Yes — the needle's south-seeking end is attracted towards the "
             "magnetic north pole in Antarctica, by the same "
             "unlike-poles-attract rule", "correct": True},
            {"text": "No — only the north-seeking end of a needle is ever attracted "
             "to anything", "correct": False,
             "why": "Both ends of a magnet interact with a field; the "
                    "south-seeking end is genuinely drawn towards a north pole, by "
                    "the same rule as the other end."},
            {"text": "No — the Antarctic pole has no effect on a compass needle", "correct": False,
             "why": "It is a real magnetic pole and does act on a compass needle, "
                    "attracting the needle's south-seeking end."},
            {"text": "No — a needle responds to the CLOSER of the two poles and "
                     "not to the far one, so a needle used in Britain could not "
                     "feel Antarctica at all", "correct": False,
             "why": "A needle lies along the whole field it sits in, which is "
                    "shaped by both poles together, not only by whichever one "
                    "happens to be nearer."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h16",
        "band": "harder",
        "text": "A walker in northern Norway finds their compass needle sluggish "
                "to settle, and the bearing it gives several degrees away from "
                "true north. Say which of dip and declination is behind each of "
                "those two problems.",
        "options": [
            {"text": "Both come from the declination, which grows larger the "
                     "further north you go and slows the needle as it does",
             "correct": False,
             "why": "Declination is the angle between two norths; it cannot slow "
                    "a needle down. The sluggishness comes from the steep dip "
                    "leaving very little sideways pull to turn it."},
            {"text": "The sluggish needle comes from the steep dip leaving little "
                     "sideways pull; the bearing being out comes from the "
                     "declination there", "correct": True},
            {"text": "Both come from the dip, which swings the needle away from "
                     "true north as well as tipping it downwards", "correct": False,
             "why": "Dip tips the needle but does not swing it away from true "
                    "north. That offset is the declination, which is a separate "
                    "reading taken at the same place."},
            {"text": "Neither is to blame — a modern compass corrects for both "
                     "dip and declination before the needle settles, wherever in "
                     "the world it is being used", "correct": False,
             "why": "A compass is a magnet on a pivot and corrects nothing at "
                    "all. Both the steep dip and the local declination act on it "
                    "exactly as they would on any other needle."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h17",
        "band": "harder",
        "text": "Declination changes noticeably over a decade in parts of Canada, "
                "but stays nearly the same in Britain over the same period. What "
                "does this difference imply about how often navigation charts "
                "should be reprinted in each place?",
        "options": [
            {"text": "Neither needs reprinting, since a declination value is "
                     "printed once and holds good for as long as the map stays "
                     "in print", "correct": False,
             "why": "Declination does change in both places, just much faster in "
                    "parts of Canada than in Britain at the moment."},
            {"text": "British charts need reprinting more often, since Britain is "
             "closer to the pole", "correct": False,
             "why": "It is the CANADIAN charts that need more frequent updating "
                    "here, since their declination is changing faster, not "
                    "Britain's."},
            {"text": "Canadian charts need reprinting with updated declination more "
             "often than British ones do", "correct": True},
            {"text": "Both should be reprinted at exactly the same frequency, since "
             "declination changes at the same rate everywhere", "correct": False,
             "why": "The rate of change is NOT the same everywhere — parts of "
                    "Canada change much faster than Britain currently does, so the "
                    "reprinting need differs too."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h18",
        "band": "harder",
        "text": "Scientists observe that the magnetic pole drifts but cannot "
                "predict its exact future position very far ahead. Explain why this "
                "is different from predicting, say, the position of true north in "
                "ten years' time.",
        "options": [
            {"text": "True north's position is equally hard to predict, since "
                     "the spin axis wanders as much as the magnetic pole does", "correct": False,
             "why": "True north does not drift at all — it stays fixed, which is "
                    "exactly why it is trivial to state its future position, "
                    "unlike the magnetic pole."},
            {"text": "The magnetic pole's future position can be predicted with "
                     "complete confidence, in the same way that a short-term "
                     "trend can be extended indefinitely into the distant "
                     "future", "correct": False,
             "why": "Its drift is observed to be irregular, which is exactly why "
                    "scientists cannot state its exact future position with full "
                    "confidence."},
            {"text": "Neither position can be known, even for right now, since "
                     "both are worked out from models rather than measured", "correct": False,
             "why": "Both positions ARE known right now, from direct observation — "
                    "the difficulty is specifically about predicting the magnetic "
                    "pole's FUTURE position."},
            {"text": "True north is fixed by the spin axis and never moves, while "
             "the magnetic pole's drift is observed but not perfectly "
             "regular, so it cannot be projected with full confidence", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h19",
        "band": "harder",
        "text": "A student reasons: \"Standing exactly at the magnetic pole, the "
                "field pulls straight down on my compass needle, so it must be "
                "adding to the pull of gravity on my own body too.\" What is wrong "
                "with this reasoning?",
        "options": [
            {"text": "The magnetic field acts on magnetic materials, not on a "
             "person's body, which is not magnetic; gravity and the magnetic "
             "pull are two entirely separate forces", "correct": True},
            {"text": "Nothing is wrong — standing at the pole really does make a "
             "person heavier", "correct": False,
             "why": "A magnetic field has no effect on an ordinary non-magnetic "
                    "body. The needle responds because it is a magnet; a person is "
                    "not."},
            {"text": "The field pulls down on metal objects heavier than a "
                     "certain weight", "correct": False,
             "why": "The field's downward pull at the pole acts on magnetic "
                    "materials because of their magnetism, not because of how "
                    "heavy they are."},
            {"text": "Gravity and magnetism are really the same force wearing "
                     "two different names, so of course they would add together "
                     "at any place where both of them point the same way", "correct": False,
             "why": "Gravity and magnetism are two distinct forces with different "
                    "causes; they do not combine into one effect."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h20",
        "band": "harder",
        "text": "A magnetotactic bacterium orients using an internal chain of "
                "magnetic crystals; a ship near the pole switches to a gyroscopic "
                "compass, which needs no magnetic field at all. Explain why the "
                "BACTERIUM's method would also fail near a magnetic pole, in a way "
                "the SHIP's new method would not.",
        "options": [
            {"text": "The bacterium's method fails because bacteria cannot survive "
             "in polar regions", "correct": False,
             "why": "Survival is not the issue being asked about — the question is "
                    "about why the ORIENTING mechanism itself would fail there, "
                    "based on the field's shape."},
            {"text": "The bacterium still relies on the sideways part of the field "
             "to orient itself, which is exactly what shrinks to almost "
             "nothing near a pole; the gyroscopic compass does not use the "
             "field at all", "correct": True},
            {"text": "The bacterium's crystals melt at the low temperatures found "
             "near the poles", "correct": False,
             "why": "Temperature is not the reason given here. The bacterium's "
                    "method fails for the same field-geometry reason a magnetic "
                    "compass does — it still needs a sideways field to align with."},
            {"text": "Both methods work perfectly well near a pole, with no "
                     "difference between them, because a spinning gyroscope and "
                     "a chain of magnetic crystals both take their direction "
                     "from the same steeply dipping field", "correct": False,
             "why": "The two methods behave very differently near a pole: one "
                    "still depends on the (vanishing) sideways field, and the "
                    "other does not use the field at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h21",
        "band": "harder",
        "text": "A student claims the Earth's field must be WEAK near the magnetic "
                "pole, because the dip there is nearly 90°. Explain the flaw in "
                "this reasoning.",
        "options": [
            {"text": "Dip and total field strength are the exact same "
                     "measurement", "correct": False,
             "why": "They are two different things: dip is an angle describing "
                    "direction, while total strength is a separate quantity "
                    "altogether."},
            {"text": "The field switches off completely right at the magnetic "
                     "pole, which is why a needle there has nothing left to "
                     "line up with", "correct": False,
             "why": "The field does not switch off at the pole — it simply points "
                    "straight down there rather than sideways."},
            {"text": "A large dip means the field points steeply down there, "
                     "not that its TOTAL strength is small — the SIDEWAYS part "
                     "usable by a compass is what shrinks", "correct": True},
            {"text": "There is no flaw — a dip of 90° means the field there is "
                     "as weak as it can get, since a field pointing straight "
                     "down has nothing left over to give in any sideways "
                     "direction", "correct": False,
             "why": "A dip of 90° describes DIRECTION, straight down, not overall "
                    "strength — the total field there is not necessarily weak at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h22",
        "band": "harder",
        "text": "Given that dip increases and sideways pull decreases together as "
                "you move away from the equator, explain why these two trends are "
                "linked rather than independent.",
        "options": [
            {"text": "They are linked by coincidence, and could in principle "
                     "vary completely independently of each other from one "
                     "place to the next", "correct": False,
             "why": "The link is not a coincidence — both come from splitting the "
                    "SAME total field into a downward part and a sideways part, "
                    "which trade off against each other."},
            {"text": "Sideways pull causes the dip to increase, as a side "
                     "effect of the needle being dragged round towards the pole", "correct": False,
             "why": "Neither reading causes the other. Both are simply two "
                    "different components of the one underlying field at that "
                    "place."},
            {"text": "The two trends are not linked — the pattern is a "
                     "coincidence of the handful of latitudes that happen to "
                     "have been measured so far, and would not hold anywhere "
                     "else", "correct": False,
             "why": "The pattern follows directly from splitting one tilting field "
                    "into a downward part and a sideways part; it is not an "
                    "arbitrary coincidence of the numbers."},
            {"text": "They are two different readings of the SAME total field, which "
             "is simply tilting more steeply downward, so more of it goes "
             "into dip and less stays sideways", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h23",
        "band": "harder",
        "text": "Real compasses are sometimes balanced slightly differently for the "
                "northern and southern hemisphere markets, using a counterweight "
                "matched to which way dip tips the needle there. Would a compass "
                "balanced for the SOUTHERN hemisphere be expected to work correctly "
                "if used in Britain?",
        "options": [
            {"text": "Not reliably — its counterweight is matched to tipping the "
             "OTHER way, so it may jam or read badly in the northern "
             "hemisphere", "correct": True},
            {"text": "Yes, perfectly, since a counterweight has nothing to do with "
             "which hemisphere a compass is used in", "correct": False,
             "why": "The counterweight is specifically matched to the DIRECTION "
                    "the field tips the needle, which is opposite in the two "
                    "hemispheres."},
            {"text": "Yes, because dip is identical in both hemispheres at the same "
             "latitude number", "correct": False,
             "why": "Dip TIPS THE NEEDLE IN OPPOSITE DIRECTIONS in the two "
                    "hemispheres, even at matching latitude numbers, which is "
                    "exactly why the balancing differs."},
            {"text": "It would work better than a British-balanced one, since "
             "southern-balanced compasses are more advanced", "correct": False,
             "why": "One balancing is not simply \"more advanced\" than the other — "
                    "each is matched to the tipping direction of its own "
                    "hemisphere."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h24",
        "band": "harder",
        "text": "A walker reasons that because their compass instrument is brand "
                "new, any bearing it gives today must automatically match true "
                "north perfectly. Explain the error, referring to what a compass "
                "actually measures.",
        "options": [
            {"text": "The error is that compasses cannot be manufactured "
                     "accurately enough to be trusted", "correct": False,
             "why": "Manufacturing accuracy is not the issue — a perfectly "
                    "accurate compass would still read magnetic north, not true "
                    "north, wherever declination is not zero."},
            {"text": "Even a perfectly working new compass lies along magnetic "
             "north, which is offset from true north by the local "
             "declination — the instrument's condition does not remove that "
             "offset", "correct": True},
            {"text": "There is no error — a new compass genuinely does read true "
             "north exactly, everywhere", "correct": False,
             "why": "A compass, new or old, follows the magnetic field, which is "
                    "offset from true north by the local declination wherever that "
                    "declination is not zero."},
            {"text": "New compasses are set to read true north, but older ones "
                     "drift across towards magnetic north as their pivot wears "
                     "down and the needle slowly loses the fine balance it was "
                     "given in the factory", "correct": False,
             "why": "Wear and age are not the mechanism here — declination is a "
                    "property of the PLACE and the field, not of how worn the "
                    "instrument is."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h25",
        "band": "harder",
        "text": "Two places, X and Y, sit at exactly the same latitude but on "
                "opposite sides of the planet in longitude. Would you expect them "
                "to have the SAME declination?",
        "options": [
            {"text": "Yes, because the magnetic pole forms a full ring around "
                     "the Earth at each latitude, so every place along a single "
                     "latitude line faces it in exactly the same way", "correct": False,
             "why": "The magnetic pole is a single location, not a ring circling "
                    "the planet, so direction to it changes with longitude."},
            {"text": "No comparison is possible unless the two places are in "
                     "the same country, since each country measures declination "
                     "against its own national grid", "correct": False,
             "why": "Declination can be compared between any two places on Earth, "
                    "in any countries, based purely on their position relative to "
                    "the magnetic pole."},
            {"text": "Not necessarily — the magnetic pole is a single point, so "
             "places at the same latitude but different longitude sit at "
             "different angles and distances from it", "correct": True},
            {"text": "Yes, always — declination depends only on latitude, never on "
             "longitude", "correct": False,
             "why": "Declination depends on the DIRECTION to a single point, the "
                    "magnetic pole, which varies with longitude even at fixed "
                    "latitude."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h26",
        "band": "harder",
        "text": "This lesson's model treats the Earth's field as a single bar "
                "magnet at the centre, aligned with the spin axis. Give ONE way "
                "this simplified model is known to give a slightly wrong prediction "
                "in real life.",
        "options": [
            {"text": "The model wrongly predicts that the field reverses once a "
                     "year, once for each full circuit the Earth makes round "
                     "the Sun", "correct": False,
             "why": "Reversal timing is not part of what this centred-dipole model "
                    "gets wrong — the known gap is the tilt between the magnetic "
                    "and spin axes."},
            {"text": "The model wrongly predicts that a compass would work "
                     "underwater, where sea water is supposed to soak the field "
                     "up before it arrives", "correct": False,
             "why": "Compasses do work underwater; that is not a prediction this "
                    "simplified model gets wrong."},
            {"text": "The model wrongly predicts that the Earth has no magnetic "
                     "field, since a bar magnet at the centre would be buried "
                     "far too deep to reach the surface", "correct": False,
             "why": "The model does predict a field — the known limitation is the "
                    "small tilt between the magnetic and spin axes, not the "
                    "field's existence."},
            {"text": "The real magnetic axis is tilted about eleven degrees from the "
             "spin axis, so real dip differs from the model's figure by "
             "several degrees in most places", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h27",
        "band": "harder",
        "text": "GPS satellites let ships and aircraft navigate without using a "
                "magnetic compass at all. Explain why GPS is immune to the problems "
                "this lesson describes: declination, dip, and the pole's drift.",
        "options": [
            {"text": "GPS uses timed radio signals from satellites to calculate "
             "position directly, with no reliance on the Earth's magnetic "
             "field whatsoever", "correct": True},
            {"text": "GPS satellites carry their own compasses that are immune to "
             "declination", "correct": False,
             "why": "GPS positioning does not work by reading a compass anywhere "
                    "in the system — it uses timed radio signals, with no magnetic "
                    "field involved at all."},
            {"text": "GPS corrects for declination automatically using a "
                     "built-in magnetic sensor, which is brought up to date "
                     "every time the satellites pass overhead above it", "correct": False,
             "why": "Basic GPS positioning needs no magnetic sensor at all; it "
                    "works from satellite signals alone, independent of the "
                    "Earth's field."},
            {"text": "GPS is affected by all the same problems, just less severely "
             "than a compass", "correct": False,
             "why": "GPS positioning does not depend on the Earth's magnetic field "
                    "in the first place, so declination, dip and pole drift do not "
                    "affect it at all."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h28",
        "band": "harder",
        "text": "A hypothetical planet is solid rock all the way through, with no "
                "churning liquid metal core of any kind. Based on what causes the "
                "Earth's field, would an ordinary compass be expected to work there "
                "in the same way?",
        "options": [
            {"text": "It is impossible to say anything at all without visiting the "
             "planet in person", "correct": False,
             "why": "The reasoning can be worked out from what is known about how "
                    "the Earth's own field is made, without needing to visit "
                    "anywhere new."},
            {"text": "No — without moving conductive fluid to generate a field, an "
             "ordinary compass would have nothing reliable to align with", "correct": True},
            {"text": "Yes — every planet automatically has a magnetic field "
                     "regardless of what its core is made of, since spinning on "
                     "an axis is enough to produce one", "correct": False,
             "why": "The Earth's field is generated specifically by currents in "
                    "its churning liquid core; a solid planet with no such core "
                    "has no reason to produce one the same way."},
            {"text": "Yes, because a compass needle makes its own magnetic "
                     "field to line up with, and needs no help from the planet "
                     "that it stands on", "correct": False,
             "why": "A compass needle is a small magnet that must ALIGN with an "
                    "outside field to be useful — it does not supply its own "
                    "planet-wide field to work with."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h29",
        "band": "harder",
        "text": "A student says: \"Once we know how strong the sideways pull is at "
                "the equator and at 70° north, we can work out the exact strength "
                "at every other latitude by simple linear interpolation between "
                "those two numbers.\" Why is this not a safe assumption?",
        "options": [
            {"text": "Sideways pull cannot be numerically compared between "
                     "different latitudes", "correct": False,
             "why": "It genuinely can be compared numerically on the relative "
                    "scale used throughout this lesson — the issue is only with "
                    "assuming a straight-line relationship."},
            {"text": "Only dip can be estimated this way; sideways pull has no "
                     "relationship with latitude whatsoever, and changes only "
                     "with the rocks underfoot", "correct": False,
             "why": "Sideways pull does have a clear relationship with latitude — "
                    "it is simply not a straight-line one, so interpolating "
                    "between two points is not safe."},
            {"text": "The relationship between latitude and sideways pull is "
                     "not a straight line, so simply interpolating between two "
                     "end points would not reliably match the values in between", "correct": True},
            {"text": "The assumption is entirely safe, and interpolating in "
                     "this way always gives the exact right answer for every "
                     "single latitude that happens to lie between the two that "
                     "were measured", "correct": False,
             "why": "The real relationship curves rather than following a straight "
                    "line, so a simple interpolation between just two points would "
                    "not be reliable."},
        ],
        "figure": None,
    },
    {
        "id": "p10-03-h30",
        "band": "harder",
        "text": "A student proposes: \"Because Earth's field comes from moving "
                "liquid iron, a planet made ENTIRELY of liquid iron, with no solid "
                "part at all, would have the strongest possible magnetic field.\" "
                "Evaluate this claim using what the lesson says the field actually "
                "needs.",
        "options": [
            {"text": "The claim is definitely correct, since more liquid iron "
                     "means more of the moving metal that makes the field, and "
                     "a bigger share of the planet doing the work", "correct": False,
             "why": "Volume of liquid iron alone is not what the lesson describes "
                    "as the cause — it is the CHURNING and the currents that "
                    "matter, not sheer quantity."},
            {"text": "The claim is wrong because liquid iron cannot produce a "
                     "magnetic field until it has cooled and set solid", "correct": False,
             "why": "Moving liquid iron is exactly what the lesson says does "
                    "produce the Earth's field — the flaw in the claim is assuming "
                    "more volume alone guarantees a stronger one, not that liquid "
                    "iron cannot work at all."},
            {"text": "The claim is right, because a completely solid planet "
                     "would have an even stronger field instead, with nothing "
                     "sloshing about inside to disturb it", "correct": False,
             "why": "A completely solid planet, with no moving conductive fluid, "
                    "would have LESS reason to generate a field this way, not "
                    "more."},
            {"text": "Not necessarily — what matters is ORGANISED churning and "
             "moving CURRENTS, not simply having a large volume of liquid "
             "iron present", "correct": True},
        ],
        "figure": None,
    },
]
