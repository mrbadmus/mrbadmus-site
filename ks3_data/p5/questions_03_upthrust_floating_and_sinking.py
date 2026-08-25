"""P5 lesson 03 — Upthrust, floating and sinking: twelve questions
(MRB-223).

Written against Design's page. The beach ball, the five one-litre blocks
and the two-panel beam are hers.

The discriminations, in the order the lesson builds them:

  · upthrust comes from the pressure DIFFERENCE across the object;
  · everything in a liquid gets it, sinkers included (`PRESS-10`);
  · it equals the weight of what is pushed out of the way, so it depends
    on VOLUME and not on weight (`PRESS-11`);
  · weight alone decides nothing (`PRESS-09`) — the harder band sits
    here and on the submarine;
  · hollowness is not the rule (`PRESS-12`).

⚠️ POSITION IS AUTHORED — index cycles 0, 1, 2, 3, giving three of each.

⚠️ Rung 1 (45 N in air, 37 N in water) and Rung 2 (the bolt and the ship)
are NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P5"
LESSON = "upthrust-floating-and-sinking"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p5-03-e01",
        "band": "easier",
        "text": "Upthrust acts…",
        "options": [
            {"text": "upwards", "correct": True},
            {"text": "downwards", "correct": False,
             "why": "That is the weight. Upthrust is what opposes it."},
            {"text": "sideways", "correct": False,
             "why": "The sideways pushes on an object cancel each other. It "
                    "is the up-and-down difference that is left over."},
            {"text": "in the direction the object is moving", "correct": False,
             "why": "It acts upwards whether the object is rising, sinking "
                    "or still."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e02",
        "band": "easier",
        "text": "Upthrust on an object is equal to…",
        "options": [
            {"text": "the weight of the object", "correct": False,
             "why": "Only when it floats. A sinker's upthrust is less than "
                    "its weight, which is why it sinks."},
            {"text": "the weight of the liquid it pushes out of the way",
             "correct": True},
            {"text": "the depth it is at", "correct": False,
             "why": "A depth is not a force. A block gets the same upthrust "
                    "at 1 m and at 10 m, once it is fully under."},
            {"text": "the pressure at the bottom of the object",
             "correct": False,
             "why": "That is a pressure, not a force — and it is only half "
                    "the story. The push on the top counts too."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e03",
        "band": "easier",
        "text": "A stone weighs 20 N in air and 14 N when hanging fully "
                "under water. What is the upthrust?",
        "options": [
            {"text": "34 N", "correct": False,
             "why": "Adding gives a force bigger than the stone's own "
                    "weight. The water takes weight OFF the balance."},
            {"text": "6 N", "correct": True},
            {"text": "14 N", "correct": False,
             "why": "That is the reading in the water, which is what is LEFT "
                    "after the upthrust has been taken off."},
            {"text": "1.4 N", "correct": False,
             "why": "That is 20 ÷ 14, a ratio rather than a force."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-e04",
        "band": "easier",
        "text": "An object floats when…",
        "options": [
            {"text": "it is lighter than water, whatever shape it is in", "correct": False,
             "why": "A ship is not lighter than water. What matters is the "
                    "water it pushes aside."},
            {"text": "it has air inside it", "correct": False,
             "why": "A sealed tin full of air sinks if it is heavy enough. "
                    "Air only helps by changing what is pushed aside."},
            {"text": "the upthrust on it equals its weight, so nothing is "
                     "left over", "correct": True},
            {"text": "it is at the surface", "correct": False,
             "why": "That is the result, not the reason. Something held at "
                    "the surface by a hand is not floating."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p5-03-s01",
        "band": "standard",
        "text": "Two one-litre blocks, one cork and one steel, are both held "
                "completely under water. Which gets the bigger upthrust?",
        "options": [
            {"text": "The steel, because it is heavier.", "correct": False,
             "why": "Upthrust does not depend on the object's weight. It "
                    "depends on what the object pushes aside."},
            {"text": "The same on both — each pushes aside one litre.",
             "correct": True},
            {"text": "The cork, because it is trying to rise.",
             "correct": False,
             "why": "Trying to rise is the RESULT of its small weight, not "
                    "a bigger upthrust."},
            {"text": "The steel, because it goes deeper.", "correct": False,
             "why": "Once fully under, going deeper changes nothing: the "
                    "pushes on top and bottom both rise by the same amount."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s02",
        "band": "standard",
        "text": "A one-litre block of ice weighs 9.2 N. One litre of water "
                "weighs 10 N. How much of the ice sits below the surface?",
        "options": [
            {"text": "All of it — ice is only just lighter.",
             "correct": False,
             "why": "Fully under it would get 10 N of upthrust against 9.2 N "
                    "of weight, and 0.8 N would push it back up."},
            {"text": "About 92 per cent of it.", "correct": True},
            {"text": "About 8 per cent of it.", "correct": False,
             "why": "That is the fraction that shows ABOVE the surface, "
                    "which is why an iceberg looks so small."},
            {"text": "Exactly half.", "correct": False,
             "why": "Half would push aside 5 N of water, nowhere near enough "
                    "to hold up 9.2 N."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s03",
        "band": "standard",
        "text": "A heavy rock feels easier to lift while it is still under "
                "water and suddenly heavier as it breaks the surface. Why?",
        "options": [
            {"text": "The water makes the rock lighter.", "correct": False,
             "why": "Its weight is unchanged throughout. What changes is "
                    "how much of it you have to supply."},
            {"text": "Water reduces the pull of gravity on it, so the "
                     "object genuinely weighs less while it is under",
             "correct": False,
             "why": "Gravity is unchanged. Something else is helping you "
                    "while the rock is submerged."},
            {"text": "Under water the upthrust is taking part of the weight, "
                     "and it stops as soon as the rock leaves the water.",
             "correct": True},
            {"text": "You get more grip on a wet rock.", "correct": False,
             "why": "Grip is a separate matter, and a wet rock is usually "
                    "harder to hold, not easier."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-s04",
        "band": "standard",
        "text": "A ship's steel is melted down and cast into one solid "
                "block. The block sinks. What changed?",
        "options": [
            {"text": "The weight of the steel went up.", "correct": False,
             "why": "It is the same steel and the same weight. Nothing was "
                    "added."},
            {"text": "Steel became denser when it was melted.",
             "correct": False,
             "why": "The steel is unchanged. What changed is the SHAPE it "
                    "is in."},
            {"text": "Gravity acts more strongly on a solid shape than on a "
                     "hollow one of the same weight",
             "correct": False,
             "why": "Gravity does not care about shape. Neither does the "
                    "weight."},
            {"text": "The volume of water it can push aside collapsed, so "
                     "the upthrust can no longer match the weight.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p5-03-h01",
        "band": "harder",
        "text": "Where does upthrust actually come from?",
        "options": [
            {"text": "From the liquid trying to get back to where the "
                     "object is, and shoving it out of the way as it does", "correct": False,
             "why": "A liquid does not try to do anything. The force has a "
                    "mechanical origin."},
            {"text": "From the pressure being greater on the bottom of the "
                     "object than on the top, because the bottom is deeper.",
             "correct": True},
            {"text": "From the object being lighter than the liquid.",
             "correct": False,
             "why": "A sinker is heavier than its own volume of water and "
                    "still gets upthrust."},
            {"text": "From the surface of the liquid pushing down "
                     "everywhere.", "correct": False,
             "why": "The surface presses down on the top of the object. It "
                    "is the DIFFERENCE with the bottom that is left over."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h02",
        "band": "harder",
        "text": "A submarine dives by flooding its ballast tanks. What "
                "happens to the upthrust on it?",
        "options": [
            {"text": "It falls, because the submarine is heavier.",
             "correct": False,
             "why": "Upthrust does not depend on the submarine's weight. It "
                    "depends on the water it pushes aside."},
            {"text": "It rises, because the submarine is deeper.",
             "correct": False,
             "why": "Once fully submerged, depth changes nothing: the pushes "
                    "on top and bottom rise together."},
            {"text": "It stays the same — the shape and volume have not "
                     "changed.", "correct": True},
            {"text": "It becomes zero, which is why the submarine sinks.",
             "correct": False,
             "why": "It is still fully supported by the same upthrust. What "
                    "changed is that the weight now exceeds it."},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h03",
        "band": "harder",
        "text": "A hot-air balloon rises. Which sentence describes it in the "
                "same terms as a cork in water?",
        "options": [
            {"text": "Hot air rises because heat travels upwards.",
             "correct": False,
             "why": "That describes nothing about the forces, and heat "
                    "travelling upwards is a separate idea."},
            {"text": "The envelope is sealed, so it cannot sink.",
             "correct": False,
             "why": "Sealed things sink all the time. What matters is what "
                    "is pushed aside."},
            {"text": "The balloon is lighter than air, so gravity misses it "
                     "and there is nothing to pull it down", "correct": False,
             "why": "Gravity pulls on it exactly as on anything else. The "
                    "upthrust simply beats it."},
            {"text": "The hot air inside weighs less than the cold air the "
                     "envelope pushes out of the way, so the upthrust wins.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p5-03-h04",
        "band": "harder",
        "text": "A ship's Plimsoll line has different marks for fresh water "
                "and salt water. Why?",
        "options": [
            {"text": "Salt water is more corrosive, so the hull must sit "
                     "higher to keep the paint out of it", "correct": False,
             "why": "Corrosion is a real problem and a separate one. The "
                    "marks are about how deep the hull may legally sit."},
            {"text": "A cubic metre of salt water weighs more, so the same "
                     "hull pushes aside more weight and floats higher.",
             "correct": True},
            {"text": "Salt water is denser, so ships sink deeper in it.",
             "correct": False,
             "why": "The premise is right and the conclusion is backwards. "
                    "Denser water gives MORE upthrust, so the hull rides "
                    "higher."},
            {"text": "The ship's weight changes between fresh and salt "
                     "water.", "correct": False,
             "why": "The ship's weight is whatever it is loaded to. It is "
                    "the water that has changed."},
        ],
        "figure": None,
    },
]
