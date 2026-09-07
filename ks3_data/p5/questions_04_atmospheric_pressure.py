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
            {"text": "only on surfaces facing the sky", "correct": False,
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
            {"text": "Nothing, because it is sealed", "correct": False,
             "why": "Being sealed is what makes it happen: the outside "
                    "pressure changes and the inside cannot."},
            {"text": "It swells, because the air inside expands as it warms",
             "correct": False,
             "why": "The air inside was at low mountain pressure, so the "
                    "greater outside pressure crushes it."},
            {"text": "It is crushed, because the outside pressure is now "
                     "higher than the inside",
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
            {"text": "Because the Moon's gravity is too weak to hold it on",
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
            {"text": "Because the metal edges weld together when the air "
                     "leaves",
             "correct": False,
             "why": "They come apart easily once air is let back in, so "
                    "nothing has welded."},
            {"text": "Because the atmosphere pushes them together and nothing "
                     "pushes back from inside",
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
            {"text": "The push of the atmosphere there, which changes with "
                     "the weather",
             "correct": True},
            {"text": "How much rain has fallen since the last reading",
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
            {"text": "To stop the fuselage being crushed by the air outside",
             "correct": False,
             "why": "The outside pressure is LOWER up there, so the fuselage "
                    "is pushed outwards, not inwards."},
            {"text": "Because the pressure outside is far too low to breathe "
                     "comfortably",
             "correct": True},
            {"text": "To keep the cabin warm at high altitude",
             "correct": False,
             "why": "Warmth comes from the heating system; pressurising is "
                    "about breathing."},
            {"text": "To stop the wings icing up", "correct": False,
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
            {"text": "Because water evaporates and mercury does not",
             "correct": False,
             "why": "Evaporation is a nuisance in the design, but it is not "
                    "what sets the height."},
            {"text": "Because mercury is a metal and conducts the pressure "
                     "better",
             "correct": False,
             "why": "Nothing conducts a pressure; the weight of the column is "
                    "what balances the air."},
            {"text": "Because mercury is far denser, so a much shorter column "
                     "weighs the same",
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
                     "less air altogether",
             "correct": True},
            {"text": "Because oxygen is heavier and sinks to lower altitudes",
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
            {"text": "The bag does not swell at all — it stays exactly as it "
                     "was",
             "correct": False,
             "why": "It swells noticeably, which is why the question is worth "
                    "asking."},
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
            {"text": "A vacuum forms and draws the liquid up",
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
]
