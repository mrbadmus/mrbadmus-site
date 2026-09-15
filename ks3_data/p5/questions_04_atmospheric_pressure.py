"""P5 lesson 04 — Atmospheric pressure: twelve questions (MRB-223).

Written against Design's page. The crushed can, the mountain bench and the
five-band stack are hers.

The discriminations, in the order the lesson builds them:

  · nothing sucks — air pushes (`PRESS-13`);
  · you do not feel it because it is balanced, not because it is small
    (`PRESS-14`);
  · climbing puts some of the air BELOW you; gravity is unchanged
    (`PRESS-15`);
  · the air thins out and never quite stops (`PRESS-16`) — the harder
    band sits here and on the straw.

⚠️ POSITION IS AUTHORED — index cycles 2, 0, 3, 1, giving three of each.

⚠️ Rung 1 (100 000 Pa on 1.5 m²) and Rung 2 (the crisp bag on a plane) are
NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P5"
LESSON = "atmospheric-pressure"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p5-04-e01",
        "band": "easier",
        "text": "Atmospheric pressure at sea level is roughly…",
        "options": [
            {"text": "100 Pa", "correct": False,
             "why": "A thousand times too small. That would not crush a can "
                    "or hold up a barometer."},
            {"text": "10 000 Pa", "correct": False,
             "why": "Ten times too small. It is about 100 000 Pa, or "
                    "101 kPa."},
            {"text": "100 000 Pa", "correct": True},
            {"text": "1 000 000 Pa", "correct": False,
             "why": "Ten times too big. That is closer to the pressure "
                    "under a stiletto heel."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e02",
        "band": "easier",
        "text": "As you climb a mountain, atmospheric pressure…",
        "options": [
            {"text": "falls, because less air is left above you",
             "correct": True},
            {"text": "rises, because you are closer to the top of the "
                     "atmosphere", "correct": False,
             "why": "Being nearer the top means LESS air above you, and it "
                    "is the air above that presses."},
            {"text": "stays the same, because the air is the same air",
             "correct": False,
             "why": "It is the same air, and there is less of it above you. "
                    "That is the whole difference."},
            {"text": "falls, because gravity gets weaker", "correct": False,
             "why": "The verdict is right and the reason is wrong. Gravity "
                    "is essentially unchanged a few kilometres up."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e03",
        "band": "easier",
        "text": "A sealed can is crushed after the steam inside it cools. "
                "What crushed it?",
        "options": [
            {"text": "The vacuum inside, pulling the walls together",
             "correct": False,
             "why": "A vacuum is nothing, and nothing can pull. The push "
                    "comes from outside."},
            {"text": "The cold water squeezing it", "correct": False,
             "why": "The water is not gripping the can. It cooled the steam, "
                    "which is a different thing."},
            {"text": "The metal shrinking as it cooled", "correct": False,
             "why": "Metal does shrink slightly, nowhere near enough to fold "
                    "a can in a second."},
            {"text": "The air outside, which had been pressing all along",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e04",
        "band": "easier",
        "text": "Why do you not feel the air pressing on you?",
        "options": [
            {"text": "Because it is too small a push to notice against "
                     "everything else pressing on you", "correct": False,
             "why": "It is about 1000 N on each palm. That is not small."},
            {"text": "Because it pushes equally from every side, and your "
                     "insides push out just as hard", "correct": True},
            {"text": "Because your skin blocks it and keeps the push away "
                     "from what is inside you", "correct": False,
             "why": "Skin is not a pressure barrier. The air presses on it "
                    "and it presses back."},
            {"text": "Because air is very light, so a column of it can "
                     "hardly press on anything", "correct": False,
             "why": "A single litre is light. A hundred-kilometre column of "
                    "it is not."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p5-04-s01",
        "band": "standard",
        "text": "Air presses with 100 000 Pa on a skylight of 0.6 m². What "
                "force is that?",
        "options": [
            {"text": "166 667 N — divide the pressure by the area",
             "correct": False,
             "why": "Dividing is how you get a pressure from a force. Here "
                    "the pressure is known, so the two multiply."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "60 000 N — 100 000 × 0.6", "correct": True},
            {"text": "60 000 Pa", "correct": False,
             "why": "The arithmetic is right and the unit is wrong. Pressure "
                    "× area gives a force."},
            {"text": "0.000006 N — divide the area by the pressure",
             "correct": False,
             "why": "That is upside down, and it gives a number far too "
                    "small to be a force on a skylight."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s02",
        "band": "standard",
        "text": "Water boils at about 71 °C on the summit of Everest. Why?",
        "options": [
            {"text": "Because the water up there is colder to start with, "
                     "so it takes much longer to reach its boiling point",
             "correct": False,
             "why": "The starting temperature sets how long it takes, not "
                    "what temperature it boils at."},
            {"text": "Because stoves burn less well in thin air, so the "
                     "water there simply never gets any hotter than that.",
             "correct": False,
             "why": "True and irrelevant — a stronger stove still boils it "
                    "at 71 °C."},
            {"text": "Because water boils when its vapour can push the air "
                     "out of the way, and there is much less air to push.",
             "correct": True},
            {"text": "Because the water is under more pressure up there, "
                     "and more pressure is what brings the boiling on.",
             "correct": False,
             "why": "It is under LESS. More pressure would push the boiling "
                    "point up, which is how a pressure cooker works."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s03",
        "band": "standard",
        "text": "A sealed foil bag swells on an aircraft at cruising height. "
                "Which explanation is right?",
        "options": [
            {"text": "The air inside is still at sea-level pressure and the "
                     "cabin air is lower, so the inside push wins.",
             "correct": True},
            {"text": "There is less gravity that high, so the air inside "
                     "spreads out until it fills whatever it is in", "correct": False,
             "why": "Gravity is essentially unchanged 11 km up. The outside "
                    "pressure is what has changed."},
            {"text": "The low pressure outside sucks the bag outwards.",
             "correct": False,
             "why": "Low pressure cannot pull. The bag swells because the "
                    "inside is pushing harder than the outside."},
            {"text": "The bag leaks slowly and fills with cabin air.",
             "correct": False,
             "why": "A leaking bag would go slack, not tight."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s04",
        "band": "standard",
        "text": "How does a sink plunger stay stuck to a flat surface?",
        "options": [
            {"text": "The rubber glues itself to the surface.",
             "correct": False,
             "why": "There is no glue, and it comes off cleanly when you "
                    "break the seal."},
            {"text": "A vacuum forms inside and holds it on.",
             "correct": False,
             "why": "The low pressure inside is real, but it does not HOLD "
                    "anything. Something has to push."},
            {"text": "The air pressure inside rises and grips the surface, "
                     "holding the cup in place",
             "correct": False,
             "why": "Squeezing air out LOWERS the pressure inside. That is "
                    "the point of squeezing it."},
            {"text": "You squeeze the air out, so the outside air pushes it "
                     "against the surface.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p5-04-h01",
        "band": "harder",
        "text": "Explain a drink coming up a straw without the word suck.",
        "options": [
            {"text": "Your mouth pulls the drink up through the straw, the "
                     "way a rope pulls a bucket.",
             "correct": False,
             "why": "That is the same claim in different words. A mouth "
                    "cannot pull on a liquid across a gap of air."},
            {"text": "You lower the pressure in your mouth, and the "
                     "atmosphere pressing on the drink pushes it up.",
             "correct": True},
            {"text": "The straw draws the liquid up by capillary action, "
                     "the way a paper towel soaks up a spill.",
             "correct": False,
             "why": "Capillary action works in very narrow tubes and would "
                    "lift a drink a millimetre or two, not up a straw."},
            {"text": "The vacuum in the straw pulls the drink into it, the "
                     "way a magnet pulls iron towards it",
             "correct": False,
             "why": "There is no vacuum, and a vacuum could not pull if "
                    "there were."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h02",
        "band": "harder",
        "text": "You try the same straw on the Moon. What happens?",
        "options": [
            {"text": "It works better, because there is less to push "
                     "against and the pump has an easier job", "correct": False,
             "why": "There is nothing to do the pushing. The atmosphere was "
                    "the thing making it work."},
            {"text": "It works the same, because your mouth does the work.",
             "correct": False,
             "why": "Your mouth only lowers the pressure. Something outside "
                    "has to push the drink up."},
            {"text": "It works, but only for very light drinks.",
             "correct": False,
             "why": "Nothing rises at all. There is no outside pressure to "
                    "supply the push, whatever the drink."},
            {"text": "Nothing rises, however hard you breathe in — there is "
                     "no atmosphere to push on the drink.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h03",
        "band": "harder",
        "text": "A pump cannot lift water more than about ten metres up a "
                "pipe, however good the pump is. Why?",
        "options": [
            {"text": "Because water is far too heavy to be pulled that far "
                     "up a pipe of any width at all, whatever kind of pump "
                     "is used on it",
             "correct": False,
             "why": "Nothing is pulling it. The framing is what makes the "
                    "limit look mysterious."},
            {"text": "Because the pipe would collapse first, and no pipe "
                     "can be made strong enough to survive a column that "
                     "tall.",
             "correct": False,
             "why": "A strong pipe hits the same limit. The barrier is not "
                    "the pipe."},
            {"text": "Because ten metres of water is the most the atmosphere "
                     "can push up, and the pump only lowers the pressure "
                     "above it.", "correct": True},
            {"text": "Because the pump runs out of power once the column "
                     "of water standing above it gets that tall and "
                     "heavy.",
             "correct": False,
             "why": "A more powerful pump makes no difference. The ceiling "
                    "is set by the air outside, not by the pump."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h04",
        "band": "harder",
        "text": "The space station orbits at 400 km, well above the usual "
                "100 km 'edge of space'. What does it still meet up there?",
        "options": [
            {"text": "Nothing at all — space begins at 100 km, and "
                     "there is no air above that line.",
             "correct": False,
             "why": "The 100 km line is an agreed boundary for "
                    "record-keeping, not a physical edge."},
            {"text": "Enough air to slow it down, so it needs regular boosts "
                     "to stay up.", "correct": True},
            {"text": "A layer of pure oxygen.", "correct": False,
             "why": "There is no such layer, and what is there is far too "
                    "thin to be called a layer of anything."},
            {"text": "Air at the same pressure as a mountain summit.",
             "correct": False,
             "why": "Far, far thinner than that — but not zero, which is "
                    "the point."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-04-e05",
        "band": "easier",
        "text": "Atmospheric pressure acts…",
        "options": [
            {"text": "downwards only, because the air is above us",
             "correct": False,
             "why": "It pushes on the underside of a shelf as well, so it is "
                    "not downwards only."},
            {"text": "in every direction at once", "correct": True},
            {"text": "upwards only, which is what holds birds up",
             "correct": False,
             "why": "Birds are held up by their wings pushing air down, not "
                    "by an upward-only pressure."},
            {"text": "only on surfaces that are facing the open sky", "correct": False,
             "why": "A vertical window has the same air pressure on it as a "
                    "horizontal one."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e06",
        "band": "easier",
        "text": "What causes atmospheric pressure?",
        "options": [
            {"text": "The weight of the air above pressing down",
             "correct": True},
            {"text": "The wind blowing against surfaces", "correct": False,
             "why": "Air presses just as hard on a still day inside a closed "
                    "room."},
            {"text": "The Sun heating the air each day", "correct": False,
             "why": "Heating shifts the pressure a little with the weather, "
                    "but it is not what creates it."},
            {"text": "The Earth spinning and throwing the air outwards",
             "correct": False,
             "why": "Spinning has a tiny effect; the air's own weight is what "
                    "does the pressing."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e07",
        "band": "easier",
        "text": "Does a vacuum suck?",
        "options": [
            {"text": "Yes — that is why a vacuum cleaner works",
             "correct": False,
             "why": "A vacuum cleaner lowers the pressure inside itself and "
                    "the atmosphere pushes the dust in."},
            {"text": "Yes, but only over short distances", "correct": False,
             "why": "Distance is not the issue; nothing at all is pulling."},
            {"text": "No — air pushes, and a vacuum simply pushes back less",
             "correct": True},
            {"text": "No — a vacuum has no effect on anything around it",
             "correct": False,
             "why": "It has a large effect, by removing the push from one "
                    "side of something."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e08",
        "band": "easier",
        "text": "Sea-level atmospheric pressure written in kilopascals is "
                "about…",
        "options": [
            {"text": "101 kPa", "correct": True},
            {"text": "1.01 kPa", "correct": False,
             "why": "That is a hundred times too small; 100 000 Pa is "
                    "100 kPa, not 1 kPa."},
            {"text": "101 000 kPa", "correct": False,
             "why": "That multiplies by a thousand instead of dividing; a "
                    "kilopascal is the larger unit."},
            {"text": "10.1 kPa", "correct": False,
             "why": "That is ten times too small — a tenth of sea-level "
                    "pressure would be near the top of the atmosphere."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e09",
        "band": "easier",
        "text": "Which instrument reads atmospheric pressure?",
        "options": [
            {"text": "A thermometer", "correct": False,
             "why": "A thermometer reads temperature in degrees Celsius."},
            {"text": "A barometer", "correct": True},
            {"text": "A newtonmeter", "correct": False,
             "why": "A newtonmeter reads a force in newtons, not a pressure."},
            {"text": "An ammeter", "correct": False,
             "why": "An ammeter reads an electric current in amps."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e10",
        "band": "easier",
        "text": "As a climber goes higher up a mountain, atmospheric pressure…",
        "options": [
            {"text": "rises, because the air is colder", "correct": False,
             "why": "Colder air is denser, but there is far less of it left "
                    "above, so the pressure falls."},
            {"text": "stays the same all the way to the summit",
             "correct": False,
             "why": "It falls steadily, which is why breathing is harder high "
                    "up."},
            {"text": "falls, because less air is left above", "correct": True},
            {"text": "falls, because gravity is weaker up there",
             "correct": False,
             "why": "Gravity barely changes over a few kilometres; the amount "
                    "of air above does."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e11",
        "band": "easier",
        "text": "Air at 100 000 Pa presses on a door of area 2 m². What force "
                "is that?",
        "options": [
            {"text": "50 000 N", "correct": False,
             "why": "That is 100 000 ÷ 2. Force is pressure MULTIPLIED by "
                    "area."},
            {"text": "200 000 N", "correct": True},
            {"text": "100 002 N", "correct": False,
             "why": "That adds the two, and a pressure cannot be added to an "
                    "area."},
            {"text": "2 N", "correct": False,
             "why": "That is the area with the unit swapped; the pressure has "
                    "to be multiplied in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e12",
        "band": "easier",
        "text": "Is there a definite height at which the air stops "
                "altogether?",
        "options": [
            {"text": "Yes, at 100 km, which is the edge of space",
             "correct": False,
             "why": "That line is a convention for record-keeping, not a "
                    "surface where the air ends."},
            {"text": "Yes, at the top of the tallest mountain",
             "correct": False,
             "why": "There is plenty of air above Everest — just too little to "
                    "breathe comfortably."},
            {"text": "No — it thins out gradually with height",
             "correct": True},
            {"text": "No — the air is the same thickness all the way up",
             "correct": False,
             "why": "It thins steadily, which is exactly why the pressure "
                    "falls as you climb."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e13",
        "band": "easier",
        "text": "A syringe with its nozzle blocked is very hard to push in. "
                "What is resisting?",
        "options": [
            {"text": "The trapped air inside being squashed", "correct": True},
            {"text": "The atmosphere pulling the plunger back out",
             "correct": False,
             "why": "The atmosphere pushes and never pulls; it is helping "
                    "push the plunger in."},
            {"text": "Friction between the plunger and the barrel",
             "correct": False,
             "why": "There is some friction, but it is the same whether the "
                    "nozzle is blocked or open."},
            {"text": "A vacuum forming behind the plunger", "correct": False,
             "why": "A vacuum would form on a pull, not a push, and it is the "
                    "trapped air that resists here."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-04-s05",
        "band": "standard",
        "text": "Air at 100 000 Pa presses on a shop window of 1.2 m². What "
                "force is that?",
        "options": [
            {"text": "83 333 N", "correct": False,
             "why": "That is 100 000 ÷ 1.2, dividing where the rearrangement "
                    "multiplies."},
            {"text": "120 000 N", "correct": True},
            {"text": "100 001 N", "correct": False,
             "why": "That adds the area on, and an area cannot be added to a "
                    "pressure."},
            {"text": "1.2 N", "correct": False,
             "why": "That is the area with the unit changed; the pressure has "
                    "to be multiplied in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s06",
        "band": "standard",
        "text": "Air at 100 000 Pa produces a force of 50 000 N on a hatch. "
                "What is the hatch's area?",
        "options": [
            {"text": "2 m²", "correct": False,
             "why": "That is 100 000 ÷ 50 000, the division the wrong way "
                    "round."},
            {"text": "0.5 m²", "correct": True},
            {"text": "5 000 000 000 m²", "correct": False,
             "why": "That multiplies the two, which gives a number with no "
                    "meaning here."},
            {"text": "50 000 m²", "correct": False,
             "why": "That is the force with the unit swapped; it still has to "
                    "be divided by the pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s07",
        "band": "standard",
        "text": "A sealed plastic bottle is emptied at the top of a mountain, "
                "capped, and carried down. What happens to it?",
        "options": [
            {"text": "Nothing, because a sealed bottle keeps its own air", "correct": False,
             "why": "Being sealed is what makes it happen: the outside "
                    "pressure changes and the air inside cannot."},
            {"text": "It swells, because the air inside expands as it warms "
                     "on the way down",
             "correct": False,
             "why": "The air inside was at low mountain pressure, so the "
                    "greater outside pressure crushes it."},
            {"text": "It is crushed, because the outside pressure is now "
                     "higher",
             "correct": True},
            {"text": "It is crushed, because gravity is stronger lower down",
             "correct": False,
             "why": "Gravity barely changes; the difference in air pressure "
                    "does the crushing."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s08",
        "band": "standard",
        "text": "Why would a rubber suction cup be useless on the Moon?",
        "options": [
            {"text": "Because the Moon's gravity is far too weak to hold "
                     "the cup against the surface",
             "correct": False,
             "why": "It is not gravity that holds a suction cup on; "
                    "atmospheric pressure is."},
            {"text": "Because there is no air outside to push it against the "
                     "surface",
             "correct": True},
            {"text": "Because rubber becomes brittle in the cold",
             "correct": False,
             "why": "It might well, but even a perfect cup would fail with no "
                    "atmosphere pushing on it."},
            {"text": "Because a vacuum cannot form inside it there",
             "correct": False,
             "why": "There is nothing to remove; the problem is the missing "
                    "push from outside."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s09",
        "band": "standard",
        "text": "Two metal hemispheres are put together and the air is pumped "
                "out. Why are they so hard to pull apart?",
        "options": [
            {"text": "Because the vacuum inside pulls them together",
             "correct": False,
             "why": "A vacuum pulls nothing. What has changed is the push "
                    "from inside, which has gone."},
            {"text": "Because the metal edges weld together when the air is "
                     "pumped out",
             "correct": False,
             "why": "They come apart easily once air is let back in, so "
                    "nothing has welded."},
            {"text": "Because the atmosphere pushes them together from "
                     "outside",
             "correct": True},
            {"text": "Because the pump leaves them magnetised",
             "correct": False,
             "why": "Pumping air out has no magnetic effect at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s10",
        "band": "standard",
        "text": "A straw has a small crack in its side above the level of the "
                "drink. Why does it stop working?",
        "options": [
            {"text": "Because the drink leaks out through the crack",
             "correct": False,
             "why": "The crack is above the drink, so nothing runs out of "
                    "it."},
            {"text": "Because air gets in, so the pressure inside no longer "
                     "falls",
             "correct": True},
            {"text": "Because the crack makes the straw too weak to hold the "
                     "drink",
             "correct": False,
             "why": "The straw is not holding the drink up by strength; the "
                    "atmosphere is pushing it up."},
            {"text": "Because the drink cannot get past the crack",
             "correct": False,
             "why": "There is no blockage; the crack simply lets air in above "
                    "the liquid."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s11",
        "band": "standard",
        "text": "A forecast says the pressure is falling. What is being "
                "measured?",
        "options": [
            {"text": "The push of the atmosphere there, which the weather "
                     "changes",
             "correct": True},
            {"text": "How much rain has fallen at that place since the "
                     "previous reading",
             "correct": False,
             "why": "Rainfall is measured in millimetres by a rain gauge, not "
                    "by a barometer."},
            {"text": "The height of the clouds above the ground",
             "correct": False,
             "why": "Cloud height is a distance; the barometer reads a "
                    "pressure in pascals."},
            {"text": "The strength of the wind at ground level",
             "correct": False,
             "why": "Wind speed is measured in m/s and is a different "
                    "quantity."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s12",
        "band": "standard",
        "text": "Why is an aircraft cabin pressurised at cruising height?",
        "options": [
            {"text": "To stop the fuselage being crushed by the air pressure "
                     "outside",
             "correct": False,
             "why": "The outside pressure is LOWER up there, so the fuselage "
                    "is pushed outwards, not inwards."},
            {"text": "Because the pressure outside is far too low to breathe",
             "correct": True},
            {"text": "To keep the cabin warm at high altitude",
             "correct": False,
             "why": "Warmth comes from the heating system; pressurising is "
                    "about breathing."},
            {"text": "To stop ice forming on the wings up there", "correct": False,
             "why": "De-icing is handled separately and has nothing to do "
                    "with cabin pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s13",
        "band": "standard",
        "text": "Why do your ears pop as an aircraft climbs?",
        "options": [
            {"text": "Because the noise of the engines changes",
             "correct": False,
             "why": "Sound is not what does it; the pressure on either side "
                    "of the eardrum is."},
            {"text": "Because the outside pressure has fallen and the inside "
                     "air must equalise",
             "correct": True},
            {"text": "Because the aircraft is travelling faster than the speed "
                     "of sound",
             "correct": False,
             "why": "Airliners do not, and the popping happens on a slow "
                    "climb in a lift as well."},
            {"text": "Because gravity is weaker higher up", "correct": False,
             "why": "Gravity barely changes over a few kilometres; the air "
                    "pressure changes a great deal."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-04-h05",
        "band": "harder",
        "text": "Air at 100 000 Pa presses on a flat roof of 40 m². What "
                "force is that, and why does the roof hold?",
        "options": [
            {"text": "4 000 000 N, and the air inside pushes up just as hard",
             "correct": True},
            {"text": "4 000 000 N, and the roof is simply strong enough on "
                     "its own",
             "correct": False,
             "why": "No ordinary roof could carry four million newtons; the "
                    "inside push is what balances it."},
            {"text": "2500 N, and the roof is strong enough on its own",
             "correct": False,
             "why": "2500 comes from dividing rather than multiplying, and it "
                    "is far too small."},
            {"text": "40 N, because the pressure acts on each square metre "
                     "once",
             "correct": False,
             "why": "Each square metre takes 100 000 N, so forty of them take "
                    "four million."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h06",
        "band": "harder",
        "text": "A mercury barometer stands about 760 mm tall, but a water "
                "one would need to be over 10 m. Why?",
        "options": [
            {"text": "Because water evaporates out of the tube and mercury "
                     "does not",
             "correct": False,
             "why": "Evaporation is a nuisance in the design, but it is not "
                    "what sets the height."},
            {"text": "Because mercury is a metal and so conducts the pressure "
                     "much better",
             "correct": False,
             "why": "Nothing conducts a pressure; the weight of the column is "
                    "what balances the air."},
            {"text": "Because mercury is far denser, so a shorter column will "
                     "do",
             "correct": True},
            {"text": "Because mercury is a liquid metal and so is heavier "
                     "than air",
             "correct": False,
             "why": "Water is heavier than air too; it is the comparison "
                    "between the two LIQUIDS that matters."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h07",
        "band": "harder",
        "text": "At 5000 m the air is still 21% oxygen, yet a climber gets "
                "far less oxygen per breath. Why?",
        "options": [
            {"text": "Because cold air holds less oxygen than warm air",
             "correct": False,
             "why": "The share of oxygen is stated as unchanged; it is the "
                    "total amount of air that has fallen."},
            {"text": "Because the pressure is lower, so each breath contains "
                     "less air",
             "correct": True},
            {"text": "Because oxygen is heavier than nitrogen and sinks to "
                     "the lower altitudes",
             "correct": False,
             "why": "The atmosphere is well mixed, which is why the "
                    "percentage stays at 21%."},
            {"text": "Because lungs work less well when it is windy",
             "correct": False,
             "why": "Wind is not what changes; the pressure of the air being "
                    "breathed is."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h08",
        "band": "harder",
        "text": "A student says a sealed bag swells at altitude because "
                "gravity is weaker up there. What is wrong?",
        "options": [
            {"text": "Nothing — weaker gravity is exactly why it swells",
             "correct": False,
             "why": "Gravity at 10 km is within a fraction of a per cent of "
                    "its ground value."},
            {"text": "Gravity is stronger up there, so the bag should shrink",
             "correct": False,
             "why": "It is very slightly weaker, but far too little to "
                    "matter either way."},
            {"text": "Gravity barely changes; the air pressure OUTSIDE the "
                     "bag has fallen",
             "correct": True},
            {"text": "The bag does not swell at all — it stays exactly the "
                     "size it was down on the ground",
             "correct": False,
             "why": "It swells noticeably, which is why the question is "
                    "worth asking."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h09",
        "band": "harder",
        "text": "Why must a spacecraft hull withstand a pressure difference "
                "of about 100 000 Pa?",
        "options": [
            {"text": "Because space presses inwards on it with that much",
             "correct": False,
             "why": "Space presses with almost nothing; the difference comes "
                    "from the inside."},
            {"text": "Because the cabin is near sea-level pressure and "
                     "outside is a vacuum",
             "correct": True},
            {"text": "Because the Sun's radiation adds that much pressure",
             "correct": False,
             "why": "Radiation does exert a tiny pressure, millions of times "
                    "smaller than this."},
            {"text": "Because the spacecraft moves so fast through the "
                     "remaining air",
             "correct": False,
             "why": "The air up there is far too thin to press on it that "
                    "hard at any speed."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h10",
        "band": "harder",
        "text": "An airlock door of 1.5 m² has a vacuum on one side and "
                "100 000 Pa on the other. What force is on it?",
        "options": [
            {"text": "66 667 N", "correct": False,
             "why": "That is 100 000 ÷ 1.5, dividing where the rearrangement "
                    "multiplies."},
            {"text": "150 000 N", "correct": True},
            {"text": "1.5 N", "correct": False,
             "why": "That is the area with the unit changed; the pressure has "
                    "to be multiplied in."},
            {"text": "0 N, because a vacuum exerts no force", "correct": False,
             "why": "The vacuum side exerts none, which is exactly why the "
                    "other side's push is unbalanced."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h11",
        "band": "harder",
        "text": "Why does a barometer reading change with the weather as well "
                "as with height?",
        "options": [
            {"text": "Because rain adds weight to the air above",
             "correct": False,
             "why": "Falling rain is on its way down; the change comes from "
                    "the air itself moving."},
            {"text": "Because the barometer's liquid expands when it is warm",
             "correct": False,
             "why": "A good barometer is corrected for that; the real change "
                    "is in the atmosphere."},
            {"text": "Because bodies of air move, so the amount above a "
                     "place changes",
             "correct": True},
            {"text": "Because the wind pushes directly on the instrument",
             "correct": False,
             "why": "A barometer indoors reads the change just as well, with "
                    "no wind on it at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h12",
        "band": "harder",
        "text": "A student says there is no air above 100 km, so the pressure "
                "there is exactly zero. What is right?",
        "options": [
            {"text": "The student is right, which is why it is called the "
                     "edge of space",
             "correct": False,
             "why": "The line is a convention for record-keeping, not a "
                    "boundary where the air ends."},
            {"text": "The air thins gradually, and enough remains at 400 km "
                     "to slow a satellite",
             "correct": True},
            {"text": "The pressure is zero above 100 km but rises again "
                     "further out",
             "correct": False,
             "why": "It keeps falling with height; nothing makes it rise "
                    "again."},
            {"text": "The pressure at 100 km is still about half its "
                     "sea-level value",
             "correct": False,
             "why": "It is a tiny fraction of it — far too little to breathe "
                    "or to hold a wing up."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h13",
        "band": "harder",
        "text": "Explain, without the word suck, why a syringe fills when its "
                "plunger is drawn out.",
        "options": [
            {"text": "The plunger pulls the liquid up the barrel behind it",
             "correct": False,
             "why": "The plunger touches only the air, and a liquid cannot be "
                    "pulled from a distance."},
            {"text": "A vacuum forms inside the barrel and draws the liquid "
                     "up",
             "correct": False,
             "why": "A vacuum draws nothing; it simply stops pushing back."},
            {"text": "The pressure inside falls, so the atmosphere pushes the "
                     "liquid up",
             "correct": True},
            {"text": "The liquid rises because it is lighter than the air "
                     "above it",
             "correct": False,
             "why": "The liquid is far heavier than air, which is why it "
                    "needs the atmosphere to push it."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p5-04-e14",
        "band": "easier",
        "text": "A barometer reads 75 kPa. Written in pascals, that is…",
        "options": [
            {"text": "75 000 Pa", "correct": True},
            {"text": "7500 Pa", "correct": False,
             "why": "That multiplies by a hundred. A kilopascal is a thousand "
                    "pascals."},
            {"text": "0.075 Pa", "correct": False,
             "why": "That divides by a thousand, when the kilopascal is the "
                    "larger unit of the two."},
            {"text": "75 Pa", "correct": False,
             "why": "That drops the kilo altogether, leaving a pressure a "
                    "thousand times too small."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e15",
        "band": "easier",
        "text": "A football is weighed flat, then pumped up hard and weighed "
                "again. What happens to the reading?",
        "options": [
            {"text": "It drops, because the ball is now full of nothing but "
                     "air",
             "correct": False,
             "why": "Air is light, but it is not weightless, so adding it "
                    "cannot take weight away."},
            {"text": "It stays exactly where it was, because air weighs "
                     "nothing", "correct": False,
             "why": "Air has weight, which is the whole reason the atmosphere "
                    "presses on us."},
            {"text": "It rises slightly, because air has weight",
             "correct": True},
            {"text": "It rises sharply, roughly doubling once the ball is "
                     "hard",
             "correct": False,
             "why": "The air squeezed into a ball weighs a few grams, so "
                    "the change is small."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e16",
        "band": "easier",
        "text": "What makes the wind blow?",
        "options": [
            {"text": "The Earth turning underneath the air", "correct": False,
             "why": "The air turns with the Earth, so the spin by itself "
                    "produces no wind."},
            {"text": "Air moving from where the pressure is higher to where "
                     "it is lower", "correct": True},
            {"text": "Clouds pushing the air along in front of them",
             "correct": False,
             "why": "Clouds are carried by the wind rather than being what "
                    "drives it."},
            {"text": "The air being pulled towards whichever place is coldest "
                     "at the time", "correct": False,
             "why": "Temperature shifts the pressure about, and it is the "
                    "pressure difference that moves the air."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e17",
        "band": "easier",
        "text": "The layer of air pressing on you at sea level is roughly…",
        "options": [
            {"text": "1 km deep, with empty space above that", "correct": False,
             "why": "There is plenty of air above 1 km; an airliner cruises "
                    "eleven times higher and still meets some."},
            {"text": "10 km deep, ending sharply at the top", "correct": False,
             "why": "Ten kilometres up is roughly cruising height, and the "
                    "air carries on well above it."},
            {"text": "1000 km deep, and just as thick all the way",
             "correct": False,
             "why": "Nothing like that much air is above us, and what there "
                    "is thins out rather than staying even."},
            {"text": "100 km deep, thinning out towards the top",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p5-04-s14",
        "band": "standard",
        "text": "A walker's watch shows their height above sea level from a "
                "pressure sensor. How can that work?",
        "options": [
            {"text": "The watch counts each step and works the height out "
                     "from that", "correct": False,
             "why": "Counting steps is a separate trick, and it would not "
                    "need a pressure sensor at all."},
            {"text": "Air pressure falls steadily with height, so a reading "
                     "can be turned into a height", "correct": True},
            {"text": "Air pressure rises with height, so the biggest reading "
                     "of the day is the summit itself", "correct": False,
             "why": "The reading falls as a walker climbs, because less air "
                    "is left above them."},
            {"text": "The sensor measures how hard the wind is pressing on "
                     "the watch", "correct": False,
             "why": "Wind is a separate matter, and the reading changes on a "
                    "still day as a walker climbs."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s15",
        "band": "standard",
        "text": "Food cooks faster in a sealed pressure cooker than in an "
                "open pan. Why?",
        "options": [
            {"text": "The lid traps the steam, so no heat can leave the pan "
                     "at all", "correct": False,
             "why": "Heat still leaves through the metal, and a tightly "
                    "lidded ordinary pan does not cook nearly as fast."},
            {"text": "The higher pressure inside forces the food apart from "
                     "the outside in", "correct": False,
             "why": "The pressure is not squeezing the food; it is changing "
                    "the temperature the water reaches."},
            {"text": "The pressure pushes the heat into the food from every "
                     "side of the pan at once", "correct": False,
             "why": "Pressure does not carry heat about. What it changes is "
                    "the point at which the water boils."},
            {"text": "The higher pressure inside raises the temperature at "
                     "which the water boils", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s16",
        "band": "standard",
        "text": "A climber's tent has a flat panel of area 3 m². At 5500 m "
                "the air presses with 50 kPa. What force acts on the panel?",
        "options": [
            {"text": "150 000 N", "correct": True},
            {"text": "150 N", "correct": False,
             "why": "That multiplies 50 by 3 and leaves the pressure in "
                    "kilopascals, so the answer is a thousand times too "
                    "small."},
            {"text": "16 667 N", "correct": False,
             "why": "That divides 50 000 by 3, where the rearrangement "
                    "multiplies."},
            {"text": "50 000 N", "correct": False,
             "why": "That is the converted pressure with the unit swapped, "
                    "before the panel area is multiplied in."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s17",
        "band": "standard",
        "text": "A sink plunger that grips a smooth tile refuses to grip a "
                "rough brick. Why?",
        "options": [
            {"text": "Brick is far too heavy for a plunger to lift off a wall",
             "correct": False,
             "why": "The plunger is not lifting the wall, and it fails on a "
                    "loose rough tile as well."},
            {"text": "Rubber cannot bend far enough to reach into brick",
             "correct": False,
             "why": "The rubber shapes itself readily; the trouble is the "
                    "gaps that are left when it does."},
            {"text": "Air leaks in through the rough surface, so the push "
                     "from inside comes back", "correct": True},
            {"text": "Brick soaks up the air squeezed out of the cup, so "
                     "there is nothing to hold on to", "correct": False,
             "why": "Nothing soaks up air. It simply seeps back in through "
                    "the gaps under the rim."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p5-04-h14",
        "band": "harder",
        "text": "Air pressure drops by about 11 kPa over the first kilometre "
                "of a climb, but by 8 kPa between 8.85 km and 11 km. Why?",
        "options": [
            {"text": "Gravity weakens with height, so the upper air presses "
                     "less than it would", "correct": False,
             "why": "Gravity is within a fraction of a per cent of its ground "
                    "value at these heights."},
            {"text": "The upper air is colder, and cold air presses less "
                     "whatever else is true", "correct": False,
             "why": "Cold air is denser for its volume, so on its own that "
                    "would work the other way."},
            {"text": "Air is squashable, so most of its mass is packed into "
                     "the lowest few kilometres", "correct": True},
            {"text": "The atmosphere comes to an end at about 11 km, so there "
                     "is very little left to lose", "correct": False,
             "why": "The air carries on far above 11 km, thinning out without "
                    "stopping."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h15",
        "band": "harder",
        "text": "A mercury barometer standing 760 mm tall at a beach is "
                "carried to a mountain hut. What does the column do?",
        "options": [
            {"text": "It falls, because less air is pushing down on the dish",
             "correct": True},
            {"text": "It rises, because the thinner air lets the mercury "
                     "climb further", "correct": False,
             "why": "Thin air gives a weaker push on the dish, so it holds up "
                    "a shorter column."},
            {"text": "It stays at 760 mm, because the instrument is sealed",
             "correct": False,
             "why": "The dish at the bottom is open to the air, which is what "
                    "the instrument is weighing."},
            {"text": "It rises, because the mercury weighs less higher up",
             "correct": False,
             "why": "Mercury weighs practically the same on a summit as on a "
                    "beach."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h16",
        "band": "harder",
        "text": "Sealing an empty can at room temperature leaves it in one "
                "piece, yet sealing it full of steam and cooling it crushes "
                "it. What is the difference?",
        "options": [
            {"text": "Cooling makes thin metal weak, so a chilled can gives "
                     "way under its own weight", "correct": False,
             "why": "A can in a fridge does not fold, so cooling the metal is "
                    "not what does it."},
            {"text": "Sealing warm air in leaves a partial vacuum that grips "
                     "the can's walls from inside", "correct": False,
             "why": "There is nothing to grip with: a vacuum has no pull of "
                    "any kind."},
            {"text": "Steam is heavier than air, so as it cools it drags the "
                     "can's walls inwards with it", "correct": False,
             "why": "Steam is lighter than air for its volume, and a gas "
                    "cannot drag a wall anywhere."},
            {"text": "The sealed air presses out as hard as the air outside, "
                     "and cooled steam does not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h17",
        "band": "harder",
        "text": "Atmospheric pressure at sea level is about 100 000 Pa. "
                "Roughly what does the air above one square metre of ground "
                "weigh?",
        "options": [
            {"text": "About 100 N, since a column of air is light",
             "correct": False,
             "why": "A column of air a hundred kilometres tall is not light, "
                    "and 100 N would be a small bag of shopping."},
            {"text": "About 100 000 N", "correct": True},
            {"text": "About 1 N, because the air is spread so thinly",
             "correct": False,
             "why": "Thin at the top, thick at the bottom, and the whole "
                    "column comes to far more than a newton."},
            {"text": "Nothing at all, because a gas has no weight",
             "correct": False,
             "why": "A gas has weight, and this weight is exactly what the "
                    "pressure is measuring."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · easier ─────────────────────────────
    {
        "id": "p5-04-e18",
        "band": "easier",
        "text": "A pressure of 50 000 Pa written in kilopascals is…",
        "options": [
            {"text": "50 kPa", "correct": True},
            {"text": "500 kPa", "correct": False,
             "why": "That divides by a hundred; a kilopascal is a thousand "
                    "pascals."},
            {"text": "5 kPa", "correct": False,
             "why": "That divides by ten thousand, which is an area "
                    "conversion rather than a prefix."},
            {"text": "50 000 000 kPa", "correct": False,
             "why": "That multiplies by a thousand, when going to the larger "
                    "unit makes the number smaller."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e19",
        "band": "easier",
        "text": "At about 2500 m up a mountain, water in an open pan boils "
                "at roughly…",
        "options": [
            {"text": "100 °C", "correct": False,
             "why": "100 °C is the sea-level figure, and it is a fact about "
                    "sea level rather than about water."},
            {"text": "92 °C", "correct": True},
            {"text": "108 °C", "correct": False,
             "why": "A boiling point above 100 °C needs a pressure higher "
                    "than sea level's, not lower."},
            {"text": "71 °C", "correct": False,
             "why": "71 °C is roughly the figure at the summit of Everest, "
                    "three times as high up."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e20",
        "band": "easier",
        "text": "At sea level the atmosphere can hold up a column of mercury "
                "about…",
        "options": [
            {"text": "76 mm tall", "correct": False,
             "why": "That is a tenth of the real height, which would be about "
                    "the length of a thumb."},
            {"text": "76 m tall", "correct": False,
             "why": "That is a hundred times too tall; water is the liquid "
                    "that needs metres rather than millimetres."},
            {"text": "760 mm tall", "correct": True},
            {"text": "7600 mm tall", "correct": False,
             "why": "That is ten times too tall, and a barometer that size "
                    "would not fit in a room."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e21",
        "band": "easier",
        "text": "On a weather map, a place marked as a 'low' is one where…",
        "options": [
            {"text": "the ground is lower than the land around it",
             "correct": False,
             "why": "A weather map marks pressure rather than the shape of "
                    "the land."},
            {"text": "the air is colder than usual", "correct": False,
             "why": "Temperature is shown separately; a low is named for its "
                    "pressure."},
            {"text": "the cloud is lower than usual", "correct": False,
             "why": "Cloud height is a different measurement, and the map "
                    "lines are pressure lines."},
            {"text": "the air pressure at the ground is below normal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e22",
        "band": "easier",
        "text": "How does a vacuum cleaner pick up dust?",
        "options": [
            {"text": "It sucks the dust in through the nozzle",
             "correct": False,
             "why": "Nothing sucks. The cleaner lowers a pressure and the "
                    "outside air does the pushing."},
            {"text": "It lowers the pressure inside, so the outside air "
                     "pushes air and dust in", "correct": True},
            {"text": "It charges the dust so that the bag attracts it",
             "correct": False,
             "why": "Some air cleaners do use charge, and an ordinary vacuum "
                    "cleaner works by moving air."},
            {"text": "It blows air out of the nozzle to lift the dust",
             "correct": False,
             "why": "Air is drawn in at the nozzle; blowing out would scatter "
                    "the dust instead."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e23",
        "band": "easier",
        "text": "A tied party balloon is put inside a jar and the air is "
                "pumped out of the jar. What does the balloon do?",
        "options": [
            {"text": "It shrinks, because there is less to hold it up",
             "correct": False,
             "why": "It was the outside air that held it in, and there is "
                    "less of that now."},
            {"text": "It swells", "correct": True},
            {"text": "It stays exactly as it was, because it is tied",
             "correct": False,
             "why": "Being tied keeps the air in; it does not stop the skin "
                    "stretching when the outside push falls."},
            {"text": "It floats to the top of the jar", "correct": False,
             "why": "Removing the air removes the upthrust as well, so it "
                    "will not float."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e24",
        "band": "easier",
        "text": "At the bottom of a deep mine shaft, the air pressure is…",
        "options": [
            {"text": "lower than at the surface", "correct": False,
             "why": "Going down puts more air above you, and it is the air "
                    "above that presses."},
            {"text": "the same as at the surface", "correct": False,
             "why": "The extra depth of air above makes a real, measurable "
                    "difference."},
            {"text": "higher than at the surface", "correct": True},
            {"text": "zero, because the shaft is sealed from the sky",
             "correct": False,
             "why": "A mine shaft is open to the air above it, and the "
                    "atmosphere reaches all the way down."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e25",
        "band": "easier",
        "text": "An airliner's cabin at cruising height is held at roughly the "
                "air pressure found at…",
        "options": [
            {"text": "sea level", "correct": False,
             "why": "Holding a full sea-level pressure would make the hull "
                    "fight a much larger difference than it need."},
            {"text": "2000 to 2400 m", "correct": True},
            {"text": "8850 m, the summit of Everest", "correct": False,
             "why": "Summit pressure is about a third of sea level's, far too "
                    "little for passengers to be comfortable."},
            {"text": "11 000 m, the height it is flying at", "correct": False,
             "why": "The air at cruising height is about 23 kPa, too little "
                    "to keep anyone conscious."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e26",
        "band": "easier",
        "text": "As a weather balloon climbs, the gas sealed inside it…",
        "options": [
            {"text": "shrinks, because the cold squeezes it", "correct": False,
             "why": "Cold does shrink a gas a little, and the fall in outside "
                    "pressure more than outweighs it."},
            {"text": "stays exactly the same size, because it is sealed",
             "correct": False,
             "why": "Being sealed keeps the gas in; it does not stop the skin "
                    "stretching as the outside push falls."},
            {"text": "expands, because the air outside presses less",
             "correct": True},
            {"text": "leaks away, because low pressure pulls it out",
             "correct": False,
             "why": "Low pressure pulls on nothing, and a sealed balloon has "
                    "nowhere for the gas to go."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e27",
        "band": "easier",
        "text": "What would a barometer read if it were set down on the "
                "surface of the Moon?",
        "options": [
            {"text": "About 101 kPa, the same as on Earth", "correct": False,
             "why": "101 kPa is the push of Earth's atmosphere, and the Moon "
                    "has none to speak of."},
            {"text": "About half of its Earth reading", "correct": False,
             "why": "Half would still need a substantial atmosphere, which "
                    "the Moon does not have."},
            {"text": "Almost nothing", "correct": True},
            {"text": "More than on Earth, because there is no air in the way",
             "correct": False,
             "why": "It is air in the way that a barometer measures, so no "
                    "air means no reading."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e28",
        "band": "easier",
        "text": "The air pressure at the summit of Everest is roughly what "
                "share of the sea-level value?",
        "options": [
            {"text": "About nine tenths", "correct": False,
             "why": "Nine tenths would be reached after about a kilometre of "
                    "climbing, not nine."},
            {"text": "About a half", "correct": False,
             "why": "Half is reached at about 5500 m, which is Everest base "
                    "camp rather than the summit."},
            {"text": "About a hundredth", "correct": False,
             "why": "A hundredth is far higher still, well above anywhere a "
                    "person can climb."},
            {"text": "About a third", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e29",
        "band": "easier",
        "text": "Tightly packed pressure lines on a weather map mean…",
        "options": [
            {"text": "a strong wind", "correct": True},
            {"text": "still air", "correct": False,
             "why": "Still air sits where the pressure hardly changes from "
                    "place to place, so the lines are far apart."},
            {"text": "heavy rain", "correct": False,
             "why": "Rain is shown separately; the lines themselves are about "
                    "pressure and wind."},
            {"text": "high ground", "correct": False,
             "why": "Height is marked on a different kind of map altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-e30",
        "band": "easier",
        "text": "Where on Earth is atmospheric pressure greatest?",
        "options": [
            {"text": "At the top of the highest mountains", "correct": False,
             "why": "That is where it is least, because most of the air is "
                    "below you there."},
            {"text": "At sea level", "correct": True},
            {"text": "Halfway up a mountain", "correct": False,
             "why": "Halfway up, some of the air is already below you, so the "
                    "reading has fallen."},
            {"text": "At the top of the atmosphere", "correct": False,
             "why": "Almost nothing is left above you up there, so almost "
                    "nothing is pressing."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · standard ───────────────────────────
    {
        "id": "p5-04-s18",
        "band": "standard",
        "text": "Two metal hemispheres are pumped empty and held together "
                "across a flat circle of 0.05 m². Air presses with "
                "100 000 Pa. What force is needed to part them?",
        "options": [
            {"text": "2 000 000 N", "correct": False,
             "why": "That divides by the area, where force = pressure × area "
                    "multiplies."},
            {"text": "5000 N", "correct": True},
            {"text": "100 000 N", "correct": False,
             "why": "That is the pressure with the unit swapped, before the "
                    "circle's area is multiplied in."},
            {"text": "0.05 N", "correct": False,
             "why": "That is the area with a newton written after it, with no "
                    "pressure used at all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s19",
        "band": "standard",
        "text": "An egg takes longer to boil soft at an Alpine village 2500 m "
                "up than it does at the coast. Why?",
        "options": [
            {"text": "Stoves burn less strongly in thin air, so a pan of "
                     "water up there takes far longer to heat up", "correct": False,
             "why": "A stronger stove makes no difference: the water still "
                    "cannot get past its boiling point."},
            {"text": "The water boils at about 92 °C there, so the egg cooks "
                     "at a lower temperature", "correct": True},
            {"text": "The water starts out colder up a mountain, so it has "
                     "further to go", "correct": False,
             "why": "The starting temperature changes how long the heating "
                    "takes, not how hot the boiling water gets."},
            {"text": "The lower pressure squeezes the shell, so heat gets in "
                     "more slowly", "correct": False,
             "why": "Lower pressure squeezes less, not more, and a shell is "
                    "not what limits the cooking."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s20",
        "band": "standard",
        "text": "A weather balloon released at sea level has burst by the time "
                "it reaches 30 km. Why?",
        "options": [
            {"text": "The air up there is so cold that the rubber freezes "
                     "hard and shatters like thin glass",
             "correct": False,
             "why": "Rubber does not shatter at altitude, and the balloon "
                    "is stretched far past its limit whatever the "
                    "temperature."},
            {"text": "The air outside thins, so the gas inside expands until "
                     "the skin splits", "correct": True},
            {"text": "The balloon is struck by something at that height",
             "correct": False,
             "why": "There is nothing to strike it, and every such balloon "
                    "bursts at a similar height."},
            {"text": "The low pressure outside pulls the skin apart",
             "correct": False,
             "why": "Low pressure pulls on nothing; the push from inside is "
                    "what stretches the skin."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s21",
        "band": "standard",
        "text": "A cabin door on an airliner is almost impossible to open "
                "during a flight. Why?",
        "options": [
            {"text": "The cabin is at a higher pressure than the air outside, "
                     "so a large force presses the door into its frame",
             "correct": True},
            {"text": "The air rushing past the aircraft holds the door shut",
             "correct": False,
             "why": "The airflow outside is not what holds it; a parked "
                    "aircraft with a pressurised cabin behaves the same way."},
            {"text": "The door is locked mechanically and cannot be moved at "
                     "all", "correct": False,
             "why": "It is locked as well, and the pressure difference alone "
                    "would make it immovable."},
            {"text": "The air outside presses harder at cruising height "
                     "than it does down on the ground, and that push holds "
                     "the door firmly shut", "correct": False,
             "why": "The outside air presses far less at cruising height; "
                    "the cabin is the high-pressure side."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s22",
        "band": "standard",
        "text": "Water in a flask can be made to boil at room temperature by "
                "pumping the air out above it. Why?",
        "options": [
            {"text": "The pump heats the water as it works", "correct": False,
             "why": "The water stays at room temperature throughout, which is "
                    "the point of the demonstration."},
            {"text": "Water boils whenever it is disturbed enough, and a "
                     "working pump shakes the flask hard",
             "correct": False,
             "why": "Stirring or shaking water does not boil it; the "
                    "pressure above it is what has changed."},
            {"text": "The vapour can push the thin air away at a much lower "
                     "temperature", "correct": True},
            {"text": "The vacuum pulls the water apart into a gas",
             "correct": False,
             "why": "A vacuum pulls on nothing; what has gone is the push "
                    "that was holding the vapour back."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s23",
        "band": "standard",
        "text": "A sealed rigid tin and a sealed foil bag are both carried "
                "from sea level up to 5500 m. What happens to each?",
        "options": [
            {"text": "Both swell up until they split open", "correct": False,
             "why": "A rigid tin holds its shape; only something that can "
                    "stretch shows the change."},
            {"text": "The bag swells while the tin keeps its shape",
             "correct": True},
            {"text": "The tin swells while the bag stays flat", "correct": False,
             "why": "That is the wrong way round: the bag is the one that can "
                    "stretch."},
            {"text": "Both are crushed inwards by the thin air",
             "correct": False,
             "why": "Thin air presses less, so anything sealed at sea level "
                    "is pushed outwards rather than inwards."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s24",
        "band": "standard",
        "text": "A window in a mountain hut is 0.8 m². The air outside presses "
                "with 75 kPa and the air inside with 75 kPa. What is the net "
                "force on the glass?",
        "options": [
            {"text": "60 000 N, pushing inwards", "correct": False,
             "why": "60 000 N is the push from one side alone, and the other "
                    "side pushes back just as hard."},
            {"text": "120 000 N, pushing inwards", "correct": False,
             "why": "That adds the two pushes, when they act against each "
                    "other."},
            {"text": "Zero", "correct": True},
            {"text": "60 000 N, pushing outwards", "correct": False,
             "why": "The inside push is real, and so is the outside one; "
                    "neither wins when the two pressures match."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s25",
        "band": "standard",
        "text": "A straw still works at the top of a mountain, where the air "
                "presses far less. Why?",
        "options": [
            {"text": "Because a straw does not need air pressure to work at "
                     "all", "correct": False,
             "why": "It needs it entirely: on the Moon nothing would rise up "
                    "the straw."},
            {"text": "Because the drink is closer to the top of the straw up "
                     "there", "correct": False,
             "why": "The drink sits in its glass exactly as it does at sea "
                    "level."},
            {"text": "Because breathing in harder makes up for the thinner "
                     "air", "correct": False,
             "why": "How hard you breathe in sets the pressure in your mouth, "
                    "and it is the outside air that has to do the pushing."},
            {"text": "Because there is still air pressing on the drink, just "
                     "less of it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s26",
        "band": "standard",
        "text": "At 5500 m a barometer reads about half its sea-level value. "
                "What does that tell you about the atmosphere?",
        "options": [
            {"text": "That about half its weight is below that height",
             "correct": True},
            {"text": "That the atmosphere ends at about 11 000 m",
             "correct": False,
             "why": "It thins out gradually and does not end; it is only half "
                    "gone by 5500 m."},
            {"text": "That the air up there is half as cold", "correct": False,
             "why": "A barometer reads a pressure, and temperature is a "
                    "separate measurement."},
            {"text": "That half the oxygen has been used up by that height",
             "correct": False,
             "why": "The share of oxygen stays at about 21% all the way up; "
                    "it is the total amount of air that has halved."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s27",
        "band": "standard",
        "text": "At the bottom of a 1 km mine shaft a barometer reads about "
                "113 kPa, against 101 kPa at the surface. Explain the "
                "difference.",
        "options": [
            {"text": "The rock around the shaft presses on the air",
             "correct": False,
             "why": "Rock presses on rock; the air in the shaft is pressed by "
                    "the air standing above it."},
            {"text": "There is an extra kilometre of air standing above you "
                     "down there", "correct": True},
            {"text": "The air down at the bottom is warmer, and warmer air "
                     "presses harder than cool air", "correct": False,
             "why": "It is warmer, and warm air is thinner for its volume, "
                    "so on its own that would lower the reading."},
            {"text": "Gravity is stronger at the bottom of a shaft",
             "correct": False,
             "why": "Gravity changes far too little over a kilometre to "
                    "explain a 12 kPa difference."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s28",
        "band": "standard",
        "text": "A rubber sucker that holds a towel rail firmly at the coast "
                "keeps dropping off at an Alpine hut. What has changed?",
        "options": [
            {"text": "The rubber has gone hard in the mountain cold", "correct": False,
             "why": "It fails indoors in a warm hut as well, so the rubber "
                    "is not the difference."},
            {"text": "The air pressing it against the tile is weaker up "
                     "there", "correct": True},
            {"text": "Gravity pulls the rail down harder at altitude",
             "correct": False,
             "why": "Gravity is very slightly weaker higher up, and far too "
                    "little to matter either way."},
            {"text": "There is more vacuum behind the sucker up there",
             "correct": False,
             "why": "What holds a sucker on is the push from outside, and "
                    "that is what has fallen."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s29",
        "band": "standard",
        "text": "A car tyre is pumped up to about 200 kPa. How does that "
                "compare with the air around it?",
        "options": [
            {"text": "About twice as much", "correct": True},
            {"text": "About the same", "correct": False,
             "why": "The air around it is about 101 kPa, so the tyre holds "
                    "roughly twice that."},
            {"text": "About half as much", "correct": False,
             "why": "A tyre at half the outside pressure would be squashed "
                    "flat by the air."},
            {"text": "About two hundred times as much", "correct": False,
             "why": "That would be true only if the outside air were about "
                    "1 kPa, which it is not."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-s30",
        "band": "standard",
        "text": "A sensitive barometer is carried up in the lift of a tall "
                "office block. What does it do, and why?",
        "options": [
            {"text": "It rises, because the lift pushes upwards as it "
                     "climbs",
             "correct": False,
             "why": "The lift's push acts on the floor of the car, not on "
                    "the air above the instrument."},
            {"text": "It stays exactly the same, because the building is "
                     "indoors", "correct": False,
             "why": "The air inside a building is open to the air outside and "
                    "thins with height in just the same way."},
            {"text": "It falls slightly, because there is a little less air "
                     "above at the top", "correct": True},
            {"text": "It falls sharply, because lifts are sealed against the "
                     "air", "correct": False,
             "why": "A lift car is not airtight, and the change over a few "
                    "tens of metres is small."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up, second pass · harder ─────────────────────────────
    {
        "id": "p5-04-h18",
        "band": "harder",
        "text": "Mercury is held up 760 mm by the air, while water would be "
                "pushed up more than 10 m. What does that say about the two "
                "liquids?",
        "options": [
            {"text": "Mercury is about thirteen times denser than water",
             "correct": True},
            {"text": "Mercury is about thirteen times lighter than water",
             "correct": False,
             "why": "A lighter liquid needs a taller column to press as hard, "
                    "so it would be the one measured in metres."},
            {"text": "Mercury conducts the air's push better than water does",
             "correct": False,
             "why": "Nothing conducts a pressure; the weight of the column is "
                    "what balances the air."},
            {"text": "Mercury boils at a lower temperature than water does",
             "correct": False,
             "why": "Mercury boils far higher than water, and boiling point "
                    "is not what sets the height."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h19",
        "band": "harder",
        "text": "A sealed syringe of trapped air is carried from sea level to "
                "5500 m, where the outside pressure is about half. What does "
                "the plunger do?",
        "options": [
            {"text": "It is pulled in, because the thin air outside the "
                     "syringe draws the plunger towards it",
             "correct": False,
             "why": "Thin air draws on nothing; it simply pushes back less "
                    "than the trapped air pushes out."},
            {"text": "It stays put, because the syringe is sealed",
             "correct": False,
             "why": "Sealing keeps the air in and does not stop the plunger "
                    "sliding when the two pushes stop matching."},
            {"text": "It slides out until the air inside fills about twice "
                     "its old volume", "correct": True},
            {"text": "It slides out a little and then springs back",
             "correct": False,
             "why": "There is nothing to spring it back; the outside pressure "
                    "stays low while the syringe is up there."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h20",
        "band": "harder",
        "text": "A pump at the top of a pipe cannot raise water more than "
                "about 10 m, yet a pump at the bottom can send it up a tower "
                "block. Why the difference?",
        "options": [
            {"text": "A pump at the bottom supplies the push itself, while "
                     "one at the top can only let the atmosphere push",
             "correct": True},
            {"text": "A pump at the bottom is always a more powerful machine",
             "correct": False,
             "why": "Power is not the limit: however powerful a top pump is, "
                    "the ceiling stays at about 10 m."},
            {"text": "Water flows more easily upwards than downwards in a "
                     "narrow pipe", "correct": False,
             "why": "Water runs downhill readily and has to be forced up, "
                    "whichever end the pump sits at."},
            {"text": "A pump at the top makes a stronger vacuum, and strong "
                     "vacuums leak", "correct": False,
             "why": "The best possible vacuum still leaves the atmosphere "
                    "doing the lifting, and it can manage only about 10 m."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h21",
        "band": "harder",
        "text": "A barometer falls by about 3.5 kPa when carried up a 300 m "
                "tower, and it can move that much in a day without leaving "
                "the ground. What does that mean for using one as an "
                "altimeter?",
        "options": [
            {"text": "It cannot measure height at all, since the readings "
                     "overlap", "correct": False,
             "why": "It measures height perfectly well over a short time; it "
                    "is drift across a day that has to be handled."},
            {"text": "It must be reset against the local pressure, or the "
                     "height it shows will drift", "correct": True},
            {"text": "It will read too low in the morning and too high in the "
                     "evening", "correct": False,
             "why": "Pressure does not follow a fixed daily pattern; it "
                    "follows the weather."},
            {"text": "It only works indoors, where the weather cannot reach "
                     "it", "correct": False,
             "why": "Indoor air is at the same pressure as outdoor air, so "
                    "moving inside changes nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h22",
        "band": "harder",
        "text": "If nothing lies above the top of the atmosphere to hold it "
                "down, why has the air not drifted away into space?",
        "options": [
            {"text": "Because the air is sealed in by a layer of cloud",
             "correct": False,
             "why": "Cloud is patchy, thin and made of the same atmosphere; "
                    "it seals nothing."},
            {"text": "Because space presses inwards on the atmosphere from "
                     "above", "correct": False,
             "why": "Space is very nearly empty and presses with almost "
                    "nothing."},
            {"text": "Because gravity pulls every part of it towards the "
                     "Earth", "correct": True},
            {"text": "Because the Earth's spin holds the air against the "
                     "ground", "correct": False,
             "why": "Spinning tends to throw things outwards, so on its own "
                    "it would work the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h23",
        "band": "harder",
        "text": "A student argues that because the atmosphere is about 100 km "
                "deep and the deepest ocean only 11 km, the air must press "
                "harder than the sea. What is wrong?",
        "options": [
            {"text": "The ocean is deeper than 100 km in places, so the "
                     "comparison is the wrong way round", "correct": False,
             "why": "Nowhere in the ocean is anything like that deep; the "
                    "depths quoted are right."},
            {"text": "Depth has nothing whatever to do with the pressure "
                     "inside either a liquid or a gas", "correct": False,
             "why": "Depth is exactly what sets the pressure in both; the "
                    "student has left out the other half."},
            {"text": "The atmosphere thins with height, so all the air "
                     "above the first few kilometres is too thin to press "
                     "on anything below it", "correct": False,
             "why": "It does thin, and every part of it still presses on "
                    "what lies below."},
            {"text": "Air weighs far less per cubic metre, so 100 km of it "
                     "presses about a thousand times less than 11 km of "
                     "water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h24",
        "band": "harder",
        "text": "At 11 km an aircraft cabin is held at 75 kPa while the air "
                "outside is 23 kPa. What force acts on a window of 0.09 m²?",
        "options": [
            {"text": "4680 N", "correct": True},
            {"text": "6750 N", "correct": False,
             "why": "That uses the cabin pressure alone and forgets that the "
                    "outside air pushes back."},
            {"text": "8820 N", "correct": False,
             "why": "That adds the two pressures, when they act against each "
                    "other."},
            {"text": "578 N", "correct": False,
             "why": "That divides the difference by the area, where force = "
                    "pressure × area multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h25",
        "band": "harder",
        "text": "Two barometers stand at the foot and the top of a 500 m "
                "hill, reading 101 kPa and 95 kPa. What does the 6 kPa "
                "difference measure?",
        "options": [
            {"text": "How much colder the air is at the top of the hill",
             "correct": False,
             "why": "A barometer reads a pressure; temperature is measured on "
                    "a separate instrument."},
            {"text": "The weight of the air between the two, spread over each "
                     "square metre", "correct": True},
            {"text": "The weight of the hill itself, spread over its base",
             "correct": False,
             "why": "The rock is not being weighed; the instruments read the "
                    "air standing above them."},
            {"text": "How much faster the wind blows at the top",
             "correct": False,
             "why": "Wind speed is a different quantity, and both readings "
                    "would hold on a still day."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h26",
        "band": "harder",
        "text": "A climber gets about half the oxygen per breath at 5500 m "
                "and about a third at 8850 m, though the air is 21% oxygen at "
                "both. Explain both figures from one quantity.",
        "options": [
            {"text": "The share of oxygen in the air falls off with height, "
                     "from 21% at the coast down towards 7% at the summit", "correct": False,
             "why": "The question states the share stays at 21%; the "
                    "atmosphere stays well mixed all the way up."},
            {"text": "The air pressure there is about a half and about a "
                     "third of the sea-level value", "correct": True},
            {"text": "The lungs work less well the colder the air gets",
             "correct": False,
             "why": "Cold air is uncomfortable, and it is the amount of air "
                    "per breath that has changed."},
            {"text": "Oxygen is heavier than nitrogen, so it settles low down",
             "correct": False,
             "why": "The atmosphere is stirred far too well for the gases to "
                    "separate out by weight."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h27",
        "band": "harder",
        "text": "A student predicts that a sink plunger would grip even better "
                "inside a vacuum chamber, since there is 'more vacuum'. What "
                "would really happen?",
        "options": [
            {"text": "It would grip harder, as the student says",
             "correct": False,
             "why": "The grip comes from the outside air, and inside a "
                    "chamber there is none left to supply it."},
            {"text": "It would grip exactly as well, since the vacuum inside "
                     "the cup is unchanged", "correct": False,
             "why": "The cup's own low pressure holds nothing on; the push "
                    "from outside does, and that has gone."},
            {"text": "It would fall off, because no outside air is left to "
                     "push it on", "correct": True},
            {"text": "It would be crushed flat by the chamber's vacuum",
             "correct": False,
             "why": "A vacuum crushes nothing, since it does no pushing at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h28",
        "band": "harder",
        "text": "Why would a barometric altimeter be useless for a rover "
                "measuring its height on the Moon?",
        "options": [
            {"text": "Because the Moon's gravity is too weak for the "
                     "instrument to work", "correct": False,
             "why": "Weak gravity would change the readings a little, and the "
                    "real trouble is that there is nothing to read."},
            {"text": "Because the Moon has almost no atmosphere, so there is "
                     "no pressure to fall with height", "correct": True},
            {"text": "Because the Moon's mountains are too low to measure",
             "correct": False,
             "why": "The Moon has mountains of thousands of metres, easily "
                    "big enough to measure."},
            {"text": "Because the Moon has no weather to change the pressure",
             "correct": False,
             "why": "Steady pressure would make an altimeter easier to use, "
                    "not impossible."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h29",
        "band": "harder",
        "text": "A foil bag holding 200 cm³ of air is sealed at sea level and "
                "carried to 5500 m, where the pressure is about half. Roughly "
                "what volume does it hold there?",
        "options": [
            {"text": "100 cm³", "correct": False,
             "why": "That halves the volume, when it is the outside push that "
                    "has halved and the bag that swells."},
            {"text": "200 cm³", "correct": False,
             "why": "A sealed bag can stretch, and the outside push on it has "
                    "fallen by half."},
            {"text": "400 cm³", "correct": True},
            {"text": "2000 cm³", "correct": False,
             "why": "That is ten times the starting volume, far more than a "
                    "halving of the outside pressure gives."},
        ],
        "figure": None,
    },
    {
        "id": "p5-04-h30",
        "band": "harder",
        "text": "One sealed can is filled and closed at a mountain summit and "
                "brought down; a second is closed at the beach and carried "
                "up. Predict what each does.",
        "options": [
            {"text": "Both are crushed, because sealed cans cannot cope with "
                     "a change", "correct": False,
             "why": "Crushing needs the outside push to win, and for one of "
                    "these two the inside push is the winner."},
            {"text": "The summit can swells and the beach can is crushed",
             "correct": False,
             "why": "That is the wrong way round: the can sealed high up has "
                    "the weaker air inside it."},
            {"text": "Both swell, because the air inside each is trapped",
             "correct": False,
             "why": "Trapped air swells only where the outside push has "
                    "fallen, which is true of just one of them."},
            {"text": "The summit can is crushed and the beach can swells",
             "correct": True},
        ],
        "figure": None,
    },
]
