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
]
