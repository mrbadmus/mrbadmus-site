"""P3 lesson 03 — Relative motion: twelve questions (MRB-223).

Written against Design's page. The two trains, the car and lorry, and the
walk down the carriage are hers.

The discriminations:

  · every speed is measured relative to SOMETHING, usually the ground and
    usually unsaid (`FORCE-09`, `FORCE-11`);
  · for how fast one passes the other: same way, SUBTRACT; opposite
    ways, ADD (`FORCE-10`) — and nothing here is ever a multiplication,
    which is why the lesson has no formula triangle. ⚠️ The rule is
    SCOPED (P3-20): a walk inside a moving frame, or a plane in moving
    air, is a composition and adds when the two go the same way;
  · changing who measures changes the number and never the object;
  · a relative speed decides how long a pass TAKES, which is why
    overtaking feels slow and a head-on pass is a blur.

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 (the cyclist at 6 m/s and the bus at 14 m/s) and Rung 2 (the
passenger sitting still) are NOT restated; check 6 of
`verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P3"
LESSON = "relative-motion"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p3-03-e01",
        "band": "easier",
        "text": "Two cars both travel at 20 m/s in the same direction, side "
                "by side. How fast is one moving relative to the other?",
        "options": [
            {"text": "20 m/s", "correct": False,
             "why": "That is each car's speed relative to the GROUND, not to "
                    "the other car."},
            {"text": "0 m/s", "correct": True},
            {"text": "40 m/s", "correct": False,
             "why": "Adding is for objects going opposite ways. These two "
                    "are going the same way."},
            {"text": "10 m/s", "correct": False,
             "why": "Nothing in relative motion halves a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e02",
        "band": "easier",
        "text": "Two trains each travel at 30 m/s, towards each other. How "
                "fast does one pass the other?",
        "options": [
            {"text": "0 m/s", "correct": False,
             "why": "That is what you get for two trains going the SAME way "
                    "at the same speed."},
            {"text": "30 m/s", "correct": False,
             "why": "That is one train's speed relative to the ground. Both "
                    "are moving, and towards each other."},
            {"text": "60 m/s", "correct": True},
            {"text": "900 m/s", "correct": False,
             "why": "That is 30 × 30. Relative speeds are added or "
                    "subtracted, never multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e03",
        "band": "easier",
        "text": "When two objects travel in the SAME direction, their "
                "relative speed is found by…",
        "options": [
            {"text": "adding the two speeds together", "correct": False,
             "why": "Adding is for opposite directions, where the gap closes "
                    "from both ends."},
            {"text": "multiplying the two speeds together", "correct": False,
             "why": "Nothing in this lesson multiplies — which is why it "
                    "carries no formula triangle."},
            {"text": "taking the average of the two speeds", "correct": False,
             "why": "An average of the two would sit between them, and a "
                    "relative speed can be zero."},
            {"text": "subtracting one speed from the other", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e04",
        "band": "easier",
        "text": "When a question gives a speed and does not say what it is "
                "measured against, what is normally meant?",
        "options": [
            {"text": "Relative to the ground", "correct": True},
            {"text": "Relative to the Sun", "correct": False,
             "why": "True speeds relative to the Sun run to about 30 km per "
                    "second, and nobody means that."},
            {"text": "Relative to the fastest object mentioned",
             "correct": False,
             "why": "There is no such convention, and it would change with "
                    "every question."},
            {"text": "Nothing — the question is unanswerable",
             "correct": False,
             "why": "The frame is usually left unsaid rather than missing. "
                    "The convention is the ground."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p3-03-s01",
        "band": "standard",
        "text": "A car at 30 m/s overtakes a lorry doing 24 m/s. How fast "
                "does the car pass the lorry?",
        "options": [
            {"text": "54 m/s", "correct": False,
             "why": "That is 30 + 24. Adding is for opposite directions; "
                    "an overtake is the same direction."},
            {"text": "6 m/s", "correct": True},
            {"text": "30 m/s", "correct": False,
             "why": "That is the car relative to the ground. The lorry is "
                    "moving too."},
            {"text": "24 m/s", "correct": False,
             "why": "That is the lorry relative to the ground, which is not "
                    "what was asked."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s02",
        "band": "standard",
        "text": "Why does overtaking on a motorway seem to take so long?",
        "options": [
            {"text": "Because cars slow down while they are overtaking each "
                     "other",
             "correct": False,
             "why": "An overtaking car usually speeds up. The feeling is not "
                    "about either car's own speed."},
            {"text": "Because the road is moving underneath both of the "
                     "vehicles",
             "correct": False,
             "why": "The road is not moving relative to the ground. The "
                    "relevant comparison is between the two vehicles."},
            {"text": "Because the relative speed is small, often only walking "
                     "pace",
             "correct": True},
            {"text": "Because both of the vehicles are travelling very fast "
                     "indeed",
             "correct": False,
             "why": "Both being fast is exactly why the DIFFERENCE is small — "
                    "but it is the difference that decides the time."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s03",
        "band": "standard",
        "text": "You walk at 1.2 m/s towards the back of a train that is "
                "doing 28 m/s. How fast are you moving relative to the "
                "ground?",
        "options": [
            {"text": "29.2 m/s", "correct": False,
             "why": "That is walking towards the FRONT. Towards the back, "
                    "your walk works against the train's motion."},
            {"text": "1.2 m/s", "correct": False,
             "why": "That is your speed relative to the train, not to the "
                    "ground."},
            {"text": "28 m/s", "correct": False,
             "why": "That is the train's speed, which would be your answer "
                    "only if you were sitting still."},
            {"text": "26.8 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s04",
        "band": "standard",
        "text": "A passenger sits still in her seat on a train doing 30 m/s. "
                "Which is true?",
        "options": [
            {"text": "She is doing 30 m/s relative to the ground and 0 m/s "
                     "relative to the train",
             "correct": True},
            {"text": "She is not moving at all, because it is only the train "
                     "that is moving",
             "correct": False,
             "why": "Relative to the ground she covers 30 m every second, "
                    "seat and all."},
            {"text": "She is doing 30 m/s, and the train's viewpoint is "
                     "simply an illusion",
             "correct": False,
             "why": "The train's viewpoint is as good as the ground's — which "
                    "is why she can read a book."},
            {"text": "She is doing 30 m/s relative to the train and 0 m/s "
                     "relative to the ground",
             "correct": False,
             "why": "That is the pair the wrong way round. Relative to the "
                    "train she is not moving at all."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p3-03-h01",
        "band": "harder",
        "text": "Two trains at 100 km/h each take a fraction of a second to "
                "pass head-on, but ten seconds when one overtakes the other "
                "on the next line. What changed?",
        "options": [
            {"text": "One of the two trains must have been going a good deal "
                     "faster in the second case",
             "correct": False,
             "why": "Neither train's own speed changed. Both are still doing "
                    "100 km/h."},
            {"text": "Nothing about either train — only the relative speed, "
                     "from 200 km/h to nearly zero",
             "correct": True},
            {"text": "The overtaking train was on a much longer stretch of "
                     "track than the other one",
             "correct": False,
             "why": "The length of track has nothing to do with how long one "
                    "train takes to pass another."},
            {"text": "A head-on pass only looks faster because of the noise "
                     "and the sudden rush of air",
             "correct": False,
             "why": "The difference is measurable, not an impression: 200 "
                    "km/h against a few km/h."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h02",
        "band": "harder",
        "text": "A plane flies at 250 m/s relative to the air, with a 50 m/s "
                "wind behind it. What is its speed relative to the ground?",
        "options": [
            {"text": "200 m/s", "correct": False,
             "why": "That is the wind subtracted, which is the leg flown "
                    "AGAINST it."},
            {"text": "250 m/s", "correct": False,
             "why": "That is its speed relative to the air, which is not "
                    "what the ground sees when the air is itself moving."},
            {"text": "300 m/s", "correct": True},
            {"text": "It cannot be worked out without the distance",
             "correct": False,
             "why": "Distance decides the time taken, not the speed. Two "
                    "speeds in the same direction are enough."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h03",
        "band": "harder",
        "text": "A plane flies out with a 50 m/s tailwind at 300 m/s and "
                "back against it at 200 m/s. Why does the round trip take "
                "LONGER than in still air?",
        "options": [
            {"text": "Because the headwind holds the plane's engines back on "
                     "the whole return leg",
             "correct": False,
             "why": "The plane still does 250 m/s through the air both ways. "
                    "The engines are unaffected."},
            {"text": "Because 300 m/s out and 200 m/s back do not average out "
                     "to 250 m/s at all",
             "correct": False,
             "why": "They do average to 250 — which is exactly why averaging "
                    "the SPEEDS is the wrong move here."},
            {"text": "Because the plane has a longer way to travel on the "
                     "return leg against the wind",
             "correct": False,
             "why": "It is the same distance each way. Only the time "
                    "differs."},
            {"text": "Because the slow leg lasts longer, so it costs more "
                     "time than the fast leg saves",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h04",
        "band": "harder",
        "text": "Why does physics not simply pick one truly stationary thing "
                "and measure every speed against it?",
        "options": [
            {"text": "Because no experiment inside a smoothly moving room can "
                     "tell you how fast the room is going, so there is no way "
                     "to identify one",
             "correct": True},
            {"text": "Because the ground is already that thing: it holds "
                     "still while everything else moves, so every speed can "
                     "be measured against it",
             "correct": False,
             "why": "The ground is a convenient choice, not a stationary one "
                    "— it is orbiting the Sun at about 30 km per second."},
            {"text": "Because instruments are not yet accurate enough to find "
                     "it, though better ones may well settle the question one "
                     "day",
             "correct": False,
             "why": "Accuracy is not the obstacle. People searched for two "
                    "hundred years with steadily better instruments."},
            {"text": "Because every speed would then come out far too large "
                     "to work with, and the numbers would be useless in "
                     "everyday life",
             "correct": False,
             "why": "Awkward numbers would be a nuisance, not a reason. The "
                    "reason is that no such frame can be identified at all."},
        ],
        "figure": None,
    },
]
