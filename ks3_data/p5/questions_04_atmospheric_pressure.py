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
            {"text": "60 000 N", "correct": True},
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
]
