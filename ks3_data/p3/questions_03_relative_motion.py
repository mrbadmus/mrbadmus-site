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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p3-03-e05",
        "band": "easier",
        "text": "When two objects travel in OPPOSITE directions, their "
                "relative speed is found by…",
        "options": [
            {"text": "adding the two speeds", "correct": True},
            {"text": "subtracting the smaller speed from the larger",
             "correct": False,
             "why": "Subtracting is for two objects going the same way. "
                    "Coming together, the gap closes faster."},
            {"text": "multiplying the two speeds", "correct": False,
             "why": "Multiplying two speeds gives nothing that can be "
                    "measured in m/s."},
            {"text": "taking whichever speed is larger", "correct": False,
             "why": "Both objects are moving, so both contribute to how fast "
                    "they close on each other."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e06",
        "band": "easier",
        "text": "A car drives past a parked van at 25 m/s. What is the car's "
                "speed relative to the van?",
        "options": [
            {"text": "0 m/s", "correct": False,
             "why": "Zero would mean the car stayed level with the van. It "
                    "goes straight past it."},
            {"text": "50 m/s", "correct": False,
             "why": "Doubling is for two objects approaching. The van is not "
                    "moving at all."},
            {"text": "25 m/s", "correct": True},
            {"text": "12.5 m/s", "correct": False,
             "why": "Halving is not one of the rules. A parked van adds and "
                    "takes away nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e07",
        "band": "easier",
        "text": "In physics, what does it mean to say an object is "
                "stationary?",
        "options": [
            {"text": "It is not moving relative to something you have named",
             "correct": True},
            {"text": "It is not moving in any way at all", "correct": False,
             "why": "Nothing is still in every frame at once — the Earth "
                    "carries everything on it around the Sun."},
            {"text": "It is resting on the ground", "correct": False,
             "why": "Touching the ground is not the test. A passenger "
                    "stationary in a train is not on the ground."},
            {"text": "It has no speed that can be measured", "correct": False,
             "why": "Its speed can be measured perfectly well. Relative to "
                    "the named thing, it is 0 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e08",
        "band": "easier",
        "text": "A train travels at 40 m/s. A passenger walks along the aisle "
                "at 1 m/s. What is the passenger's speed relative to the "
                "train?",
        "options": [
            {"text": "41 m/s", "correct": False,
             "why": "41 m/s is the speed relative to the GROUND. Relative to "
                    "the train, only the walking counts."},
            {"text": "1 m/s", "correct": True},
            {"text": "40 m/s", "correct": False,
             "why": "That is the train's own speed relative to the ground, "
                    "not the passenger's relative to the train."},
            {"text": "39 m/s", "correct": False,
             "why": "That would be the ground speed of someone walking "
                    "backwards along the aisle."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e09",
        "band": "easier",
        "text": "What is a frame of reference?",
        "options": [
            {"text": "The equipment used to measure a speed", "correct": False,
             "why": "The stopwatch and tape are apparatus. A frame is the "
                    "thing the speed is measured against."},
            {"text": "The fastest speed anything can travel at",
             "correct": False,
             "why": "That is a limit on speeds, not the thing a speed is "
                    "compared with."},
            {"text": "The thing a speed is measured against", "correct": True},
            {"text": "The direction in which an object is travelling",
             "correct": False,
             "why": "Direction is part of describing motion, but the frame is "
                    "what you measure it from."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e10",
        "band": "easier",
        "text": "A bus travels at 12 m/s. A car going the same way overtakes "
                "it at 20 m/s. What is the car's speed relative to the bus?",
        "options": [
            {"text": "32 m/s", "correct": False,
             "why": "Adding is for objects travelling in opposite "
                    "directions. These two are going the same way."},
            {"text": "20 m/s", "correct": False,
             "why": "That is the car's speed relative to the ground, not "
                    "relative to the moving bus."},
            {"text": "8 m/s", "correct": True},
            {"text": "12 m/s", "correct": False,
             "why": "That is the bus's own speed relative to the ground, not "
                    "the difference between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e11",
        "band": "easier",
        "text": "Two cars drive towards each other, each at 15 m/s. How fast "
                "do they approach each other?",
        "options": [
            {"text": "30 m/s", "correct": True},
            {"text": "15 m/s", "correct": False,
             "why": "That is one car's speed alone, and both are closing the "
                    "gap at the same time."},
            {"text": "0 m/s", "correct": False,
             "why": "Subtracting is for two objects going the same way. These "
                    "two are heading towards each other."},
            {"text": "7.5 m/s", "correct": False,
             "why": "Halving is not one of the rules; the two speeds add when "
                    "the directions are opposite."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e12",
        "band": "easier",
        "text": "You are sitting still on a chair at home. Relative to the "
                "Sun, are you moving?",
        "options": [
            {"text": "No, because you are not moving at all",
             "correct": False,
             "why": "You are still relative to the room only. The Earth "
                    "carries you around the Sun the whole time."},
            {"text": "Yes, because the Earth carries you around the Sun",
             "correct": True},
            {"text": "No, because you cannot feel any movement",
             "correct": False,
             "why": "Steady motion cannot be felt, which is exactly why the "
                    "answer is not obvious."},
            {"text": "Only if the chair itself is being moved",
             "correct": False,
             "why": "The chair's motion in the room is a separate question "
                    "from the Earth's motion around the Sun."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e13",
        "band": "easier",
        "text": "Which of these has to be known before a speed means "
                "anything?",
        "options": [
            {"text": "The mass of the moving object", "correct": False,
             "why": "Mass has no part in speed = distance ÷ time, or in "
                    "relative speed."},
            {"text": "The colour of the moving object", "correct": False,
             "why": "Nothing about how an object looks changes what its speed "
                    "is measured against."},
            {"text": "How long the object has been moving", "correct": False,
             "why": "That would tell you the distance covered, not what the "
                    "speed is compared with."},
            {"text": "What the speed is being measured relative to",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e14",
        "band": "easier",
        "text": "A boat travels at 6 m/s through the water. The river flows "
                "at 2 m/s the same way. How fast does the boat move relative "
                "to the bank?",
        "options": [
            {"text": "8 m/s", "correct": True},
            {"text": "6 m/s", "correct": False,
             "why": "6 m/s is its speed through the water. The bank sees the "
                    "current carrying it along as well."},
            {"text": "4 m/s", "correct": False,
             "why": "Subtracting is for going against the flow. Here the "
                    "current is helping."},
            {"text": "12 m/s", "correct": False,
             "why": "That is 6 × 2. Relative speeds are added or subtracted, "
                    "never multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e15",
        "band": "easier",
        "text": "The same boat turns and travels at 6 m/s through the water "
                "against a 2 m/s flow. How fast does it move relative to the "
                "bank?",
        "options": [
            {"text": "8 m/s", "correct": False,
             "why": "Adding is for going with the flow. Against it, the "
                    "current takes speed away."},
            {"text": "4 m/s", "correct": True},
            {"text": "6 m/s", "correct": False,
             "why": "6 m/s is its speed through the water, and the bank sees "
                    "the current holding it back."},
            {"text": "3 m/s", "correct": False,
             "why": "That is 6 ÷ 2. Relative speeds are added or subtracted, "
                    "never divided."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e16",
        "band": "easier",
        "text": "A plane flies at 200 m/s. A book lies on the tray in front "
                "of a passenger. How fast is the book moving relative to that "
                "passenger?",
        "options": [
            {"text": "200 m/s", "correct": False,
             "why": "That is the book's speed relative to the ground. The "
                    "passenger is carried along with it."},
            {"text": "400 m/s", "correct": False,
             "why": "Adding is for objects moving in opposite directions, and "
                    "these two move together."},
            {"text": "It cannot be given without the plane's direction",
             "correct": False,
             "why": "Whatever direction the plane takes, book and passenger "
                    "go the same way at the same speed."},
            {"text": "0 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e17",
        "band": "easier",
        "text": "Two objects have a relative speed of 0 m/s. What does that "
                "tell you?",
        "options": [
            {"text": "Neither of them is moving at all", "correct": False,
             "why": "They may both be moving quickly — as long as they move "
                    "together, the gap does not change."},
            {"text": "They are moving at the same speed in the same "
                     "direction",
             "correct": True},
            {"text": "They are moving at the same speed in opposite "
                     "directions",
             "correct": False,
             "why": "Opposite directions make the speeds ADD, giving the "
                    "largest relative speed, not zero."},
            {"text": "They are both travelling at their top speed",
             "correct": False,
             "why": "Top speed does not come into it; what matters is that "
                    "the two speeds match."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e18",
        "band": "easier",
        "text": "A cyclist rides past a bus stop at 5 m/s. Relative to the "
                "cyclist, how is the bus stop moving?",
        "options": [
            {"text": "At 5 m/s, backwards past her", "correct": True},
            {"text": "At 0 m/s, because it is fixed to the pavement",
             "correct": False,
             "why": "It is fixed relative to the ground, but the cyclist is "
                    "not the ground."},
            {"text": "At 10 m/s, backwards past her", "correct": False,
             "why": "Doubling is for two objects approaching. Only the "
                    "cyclist is actually moving."},
            {"text": "At 5 m/s, forwards ahead of her", "correct": False,
             "why": "She is catching it up and passing it, so from her seat "
                    "it goes past her the other way."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p3-03-s05",
        "band": "standard",
        "text": "A car at 32 m/s is gaining on a lorry at 22 m/s ahead of it "
                "on the same road. How long does the car take to close a gap "
                "of 50 m?",
        "options": [
            {"text": "5 s", "correct": True},
            {"text": "1.6 s", "correct": False,
             "why": "That is 50 ÷ 32, using the car's ground speed instead of "
                    "the speed it gains at."},
            {"text": "2.3 s", "correct": False,
             "why": "That is 50 ÷ 22, using the lorry's speed rather than the "
                    "difference."},
            {"text": "0.9 s", "correct": False,
             "why": "That is 50 ÷ 54, adding the speeds — which is the rule "
                    "for opposite directions."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s06",
        "band": "standard",
        "text": "Two trains approach each other on parallel tracks at 25 m/s "
                "and 35 m/s. How fast is the gap between them closing?",
        "options": [
            {"text": "10 m/s", "correct": False,
             "why": "Subtracting is the rule for two trains going the SAME "
                    "way. These are closing on each other."},
            {"text": "35 m/s", "correct": False,
             "why": "That is the faster train alone, and the other is closing "
                    "the gap as well."},
            {"text": "60 m/s", "correct": True},
            {"text": "30 m/s", "correct": False,
             "why": "That is the average of the two speeds, which is not one "
                    "of the relative-speed rules."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s07",
        "band": "standard",
        "text": "A swimmer swims at 1.5 m/s in still water. She swims "
                "downstream in a river flowing at 0.5 m/s. What is her speed "
                "relative to the bank?",
        "options": [
            {"text": "1.5 m/s", "correct": False,
             "why": "1.5 m/s is her speed through the water; the bank sees "
                    "the current carrying her too."},
            {"text": "2.0 m/s", "correct": True},
            {"text": "1.0 m/s", "correct": False,
             "why": "Subtracting is for swimming against the flow. Going "
                    "downstream, the current helps."},
            {"text": "0.75 m/s", "correct": False,
             "why": "That is 1.5 × 0.5. Relative speeds are added or "
                    "subtracted, never multiplied."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s08",
        "band": "standard",
        "text": "The same swimmer turns and swims upstream at 1.5 m/s through "
                "the water. How long does she take to cover 30 m along the "
                "bank?",
        "options": [
            {"text": "15 s", "correct": False,
             "why": "That uses 2.0 m/s, the downstream speed. Going upstream "
                    "the current is against her."},
            {"text": "20 s", "correct": False,
             "why": "That uses her 1.5 m/s through the water, ignoring the "
                    "current pushing her back."},
            {"text": "60 s", "correct": False,
             "why": "That uses 0.5 m/s, the current alone, rather than her "
                    "speed relative to the bank."},
            {"text": "30 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s09",
        "band": "standard",
        "text": "A passenger walks towards the FRONT of a train at 1.5 m/s "
                "while the train does 30 m/s. What is her speed relative to "
                "the ground?",
        "options": [
            {"text": "31.5 m/s", "correct": True},
            {"text": "28.5 m/s", "correct": False,
             "why": "Subtracting is for walking towards the back. Walking "
                    "forwards adds to the train's speed."},
            {"text": "1.5 m/s", "correct": False,
             "why": "That is her speed relative to the TRAIN. The ground sees "
                    "the train's motion as well."},
            {"text": "30 m/s", "correct": False,
             "why": "That is the train's speed, which would be her answer "
                    "only if she stayed in her seat."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s10",
        "band": "standard",
        "text": "Why does the ground appear to rush backwards when you look "
                "out of a train window?",
        "options": [
            {"text": "Because the ground really is moving under the train",
             "correct": False,
             "why": "The ground is still relative to itself. It is the train "
                    "that is moving along it."},
            {"text": "Because your eyes cannot follow objects that are close "
                     "to you",
             "correct": False,
             "why": "Nearby things do sweep past faster, but the motion you "
                    "see is real, not an eye problem."},
            {"text": "Because relative to you, the ground is moving at the "
                     "train's speed",
             "correct": True},
            {"text": "Because the train is slowing down as you look",
             "correct": False,
             "why": "It happens at a perfectly steady speed, and slowing "
                    "would change what you see, not cause it."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s11",
        "band": "standard",
        "text": "Two cars are 20 m apart on a motorway and both hold a steady "
                "25 m/s. What happens to the gap?",
        "options": [
            {"text": "It stays at 20 m, because their relative speed is "
                     "0 m/s",
             "correct": True},
            {"text": "It closes at 50 m/s, because both are moving",
             "correct": False,
             "why": "Adding is the rule for opposite directions. These two "
                    "travel the same way."},
            {"text": "It closes slowly, because the car behind has less air "
                     "in its way",
             "correct": False,
             "why": "Both hold the same speed, so nothing is gaining on "
                    "anything."},
            {"text": "It grows at 25 m/s, the speed of the car in front",
             "correct": False,
             "why": "The car behind travels at 25 m/s too, so the gap is left "
                    "exactly as it was."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s12",
        "band": "standard",
        "text": "A cyclist sets off north at 6 m/s and a runner sets off "
                "south at 4 m/s from the same gate. How far apart are they "
                "after 20 s?",
        "options": [
            {"text": "40 m", "correct": False,
             "why": "That is 2 × 20, the difference in their speeds — the "
                    "rule for two people going the same way."},
            {"text": "200 m", "correct": True},
            {"text": "120 m", "correct": False,
             "why": "That is the cyclist's distance alone; the runner has "
                    "gone the other way as well."},
            {"text": "80 m", "correct": False,
             "why": "That is the runner's distance alone, and the cyclist has "
                    "moved in the opposite direction."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s13",
        "band": "standard",
        "text": "A helicopter hovers over the deck of a ship that is sailing "
                "at 8 m/s. What must the helicopter be doing?",
        "options": [
            {"text": "Standing completely still relative to the sea",
             "correct": False,
             "why": "If it stood still over the sea, the ship would sail out "
                    "from under it at 8 m/s."},
            {"text": "Travelling at 8 m/s in the same direction as the ship",
             "correct": True},
            {"text": "Travelling at 16 m/s to keep up with the deck",
             "correct": False,
             "why": "Doubling would carry it past the bow. Matching means the "
                    "same speed, not twice it."},
            {"text": "Travelling at 8 m/s in the opposite direction",
             "correct": False,
             "why": "That gives a relative speed of 16 m/s, so it would "
                    "sweep backwards over the deck."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s14",
        "band": "standard",
        "text": "An airport walkway moves at 1 m/s. A traveller walks along "
                "it in the same direction at 1.5 m/s. How fast is he moving "
                "relative to the floor of the terminal?",
        "options": [
            {"text": "1.5 m/s", "correct": False,
             "why": "That is his speed relative to the walkway, and the "
                    "walkway is carrying him too."},
            {"text": "0.5 m/s", "correct": False,
             "why": "Subtracting is for walking against the walkway's "
                    "motion, not with it."},
            {"text": "2.5 m/s", "correct": True},
            {"text": "1 m/s", "correct": False,
             "why": "That is the walkway alone, which would be his speed only "
                    "if he stood still on it."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s15",
        "band": "standard",
        "text": "The same traveller walks back along the walkway at 1.5 m/s "
                "against its 1 m/s motion. How fast is he moving relative to "
                "the floor?",
        "options": [
            {"text": "0.5 m/s", "correct": True},
            {"text": "2.5 m/s", "correct": False,
             "why": "Adding is for walking with the walkway. Against it, the "
                    "walkway takes speed away."},
            {"text": "0 m/s", "correct": False,
             "why": "He would stand still only if he walked at exactly "
                    "1 m/s, and he walks faster than that."},
            {"text": "1.5 m/s", "correct": False,
             "why": "That is his speed relative to the walkway, which is "
                    "itself sliding the other way."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s16",
        "band": "standard",
        "text": "A passenger on a train travelling steadily at 30 m/s drops a "
                "coin. Where does it land?",
        "options": [
            {"text": "Well behind her, because the train moves on while it "
                     "falls",
             "correct": False,
             "why": "The coin is travelling at 30 m/s too, so it keeps up "
                    "with her all the way down."},
            {"text": "Straight down at her feet, because the coin travels "
                     "with her",
             "correct": True},
            {"text": "Well in front of her, because the coin keeps its own "
                     "speed",
             "correct": False,
             "why": "It does keep its speed — the same 30 m/s as the "
                    "passenger, so neither gains on the other."},
            {"text": "It cannot be said without knowing the height of the "
                     "drop",
             "correct": False,
             "why": "The height changes how long it falls for, not where it "
                    "lands relative to her."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s17",
        "band": "standard",
        "text": "A bus travels at 15 m/s and a car behind it also travels at "
                "15 m/s. What does the driver of the car see the bus doing?",
        "options": [
            {"text": "Pulling away from her at 15 m/s", "correct": False,
             "why": "It pulls away only if it is faster, and both are doing "
                    "15 m/s."},
            {"text": "Coming towards her at 30 m/s", "correct": False,
             "why": "Speeds add when the two travel in opposite directions, "
                    "and these travel the same way."},
            {"text": "Staying the same distance ahead of her", "correct": True},
            {"text": "Falling back towards her at 15 m/s", "correct": False,
             "why": "It falls back only if it is slower, and their speeds "
                    "match exactly."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s18",
        "band": "standard",
        "text": "A forecast says the wind is blowing at 10 m/s and never says "
                "what that is measured against. What is meant?",
        "options": [
            {"text": "10 m/s relative to the ground", "correct": True},
            {"text": "10 m/s relative to the clouds above it",
             "correct": False,
             "why": "Clouds are carried by the wind themselves, so they would "
                    "give a much smaller number."},
            {"text": "10 m/s relative to a car driving through it",
             "correct": False,
             "why": "That reading would change with every car's speed, so it "
                    "could not be forecast."},
            {"text": "10 m/s relative to the Sun", "correct": False,
             "why": "That would be tens of thousands of metres per second, "
                    "and no use to anybody."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p3-03-h05",
        "band": "harder",
        "text": "A car at 28 m/s overtakes a lorry at 22 m/s, and must gain "
                "90 m on it to complete the move. How long does the overtake "
                "take?",
        "options": [
            {"text": "15 s", "correct": True},
            {"text": "3.2 s", "correct": False,
             "why": "That is 90 ÷ 28, using the car's ground speed rather "
                    "than the speed it gains at."},
            {"text": "1.8 s", "correct": False,
             "why": "That is 90 ÷ 50, adding the speeds — the rule for "
                    "opposite directions."},
            {"text": "4.1 s", "correct": False,
             "why": "That is 90 ÷ 22, using the lorry's speed rather than the "
                    "difference between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h06",
        "band": "harder",
        "text": "A boat does 2 m/s through still water. It travels 600 m "
                "downstream on a 1 m/s current, then 600 m back up. What is "
                "the total time?",
        "options": [
            {"text": "600 s, because the current cancels out",
             "correct": False,
             "why": "It does not cancel: the slow leg lasts far longer than "
                    "the fast one, so time is lost overall."},
            {"text": "400 s", "correct": False,
             "why": "That uses 3 m/s both ways, as though the current helped "
                    "on the return as well."},
            {"text": "800 s", "correct": True},
            {"text": "1200 s", "correct": False,
             "why": "That uses 1 m/s both ways, as though the current fought "
                    "the boat on the downstream leg too."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h07",
        "band": "harder",
        "text": "Why does a relative speed of 0 m/s not mean that nothing is "
                "moving?",
        "options": [
            {"text": "Because both objects may be moving quickly, but "
                     "together",
             "correct": True},
            {"text": "Because a relative speed of zero is always a "
                     "measurement error",
             "correct": False,
             "why": "It is a perfectly good reading — two cars matching "
                    "speeds give it every time."},
            {"text": "Because relative speed only works for objects that are "
                     "at rest",
             "correct": False,
             "why": "It works for any pair; the zero comes from the two "
                    "speeds being equal."},
            {"text": "Because speeds cannot be measured from a moving object",
             "correct": False,
             "why": "They can, and doing so is what a relative speed is."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h08",
        "band": "harder",
        "text": "Two trains, each 200 m long, pass in opposite directions at "
                "20 m/s and 30 m/s. How long from the fronts meeting to the "
                "backs clearing?",
        "options": [
            {"text": "20 s", "correct": False,
             "why": "That uses 400 m ÷ 20 m/s, taking one train's speed "
                    "instead of the speed they close at."},
            {"text": "8 s", "correct": True},
            {"text": "4 s", "correct": False,
             "why": "That uses only one train's 200 m; both lengths have to "
                    "pass each other."},
            {"text": "40 s", "correct": False,
             "why": "That uses 400 m ÷ 10 m/s, subtracting the speeds — the "
                    "rule for the same direction."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h09",
        "band": "harder",
        "text": "A plane's speed through the air is 240 m/s. It flies 630 km "
                "into a 30 m/s headwind. How long does the flight take?",
        "options": [
            {"text": "2625 s", "correct": False,
             "why": "That uses 240 m/s, as though the headwind made no "
                    "difference to the speed over the ground."},
            {"text": "3000 s", "correct": True},
            {"text": "2333 s", "correct": False,
             "why": "That uses 270 m/s, adding the wind — which is the rule "
                    "for a tailwind, not a headwind."},
            {"text": "21 000 s", "correct": False,
             "why": "That divides 630 000 m by the 30 m/s wind rather than by "
                    "the plane's speed over the ground."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h10",
        "band": "harder",
        "text": "A passenger on a coach travelling at 25 m/s throws a ball "
                "forwards at 5 m/s. How fast is the ball moving relative to "
                "the road?",
        "options": [
            {"text": "5 m/s", "correct": False,
             "why": "That is its speed relative to the coach; the road sees "
                    "the coach's motion as well."},
            {"text": "20 m/s", "correct": False,
             "why": "Subtracting is for a ball thrown backwards. Thrown "
                    "forwards, the two speeds add."},
            {"text": "125 m/s", "correct": False,
             "why": "That is 25 × 5. Relative speeds are added or subtracted, "
                    "never multiplied."},
            {"text": "30 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h11",
        "band": "harder",
        "text": "The same passenger throws the ball backwards at 5 m/s "
                "instead. What do the passenger and someone at the roadside "
                "each measure?",
        "options": [
            {"text": "The passenger 5 m/s, the roadside 20 m/s",
             "correct": True},
            {"text": "The passenger 5 m/s, the roadside 30 m/s",
             "correct": False,
             "why": "30 m/s is the forwards throw. Thrown backwards, the "
                    "throw takes away from the coach's speed."},
            {"text": "The passenger 20 m/s, the roadside 5 m/s",
             "correct": False,
             "why": "The two readings are the wrong way round: the passenger "
                    "moves with the coach."},
            {"text": "Both of them 20 m/s", "correct": False,
             "why": "They cannot agree — the passenger is carried along with "
                    "the coach and the roadside observer is not."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h12",
        "band": "harder",
        "text": "The Earth carries us around the Sun at about 30 km every "
                "second. Why does that not blow us off our feet?",
        "options": [
            {"text": "Because the air and the ground move with us at the "
                     "same speed",
             "correct": True},
            {"text": "Because the atmosphere shields us from the motion",
             "correct": False,
             "why": "The atmosphere is travelling with the Earth as well; it "
                    "is not holding anything back."},
            {"text": "Because 30 km per second is too small a speed to feel",
             "correct": False,
             "why": "It is enormous. What makes it unnoticed is that "
                    "everything around us shares it."},
            {"text": "Because gravity holds us down hard enough to resist it",
             "correct": False,
             "why": "Gravity holds us to the ground, but the ground is moving "
                    "with us, so there is nothing to resist."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h13",
        "band": "harder",
        "text": "A cyclist rides at 8 m/s straight into a wind blowing at "
                "3 m/s towards her. How fast is the air moving relative to "
                "her face?",
        "options": [
            {"text": "5 m/s", "correct": False,
             "why": "Subtracting is for a wind from behind. A headwind and "
                    "the rider close on each other."},
            {"text": "11 m/s", "correct": True},
            {"text": "8 m/s", "correct": False,
             "why": "That is what she would feel in still air; the wind adds "
                    "to it."},
            {"text": "3 m/s", "correct": False,
             "why": "That is the wind's speed over the ground, which a "
                    "standing person would feel."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h14",
        "band": "harder",
        "text": "A train travels at 30 m/s. A guard walks the 120 m length of "
                "a carriage from back to front in 60 s. What is his speed "
                "relative to the ground?",
        "options": [
            {"text": "2 m/s", "correct": False,
             "why": "That is his speed relative to the TRAIN, worked out from "
                    "120 m in 60 s."},
            {"text": "28 m/s", "correct": False,
             "why": "Subtracting is for walking towards the back, and he is "
                    "walking towards the front."},
            {"text": "32 m/s", "correct": True},
            {"text": "150 m/s", "correct": False,
             "why": "That adds 120 m to 30 m/s. A distance and a speed cannot "
                    "be added."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h15",
        "band": "harder",
        "text": "Inside a smoothly moving train with the blinds down, why can "
                "you not tell how fast you are going?",
        "options": [
            {"text": "Because the windows are the only instrument a train "
                     "carries",
             "correct": False,
             "why": "A train carries plenty of instruments. The point is that "
                    "none of them can be felt to read."},
            {"text": "Because no experiment done inside can detect steady "
                     "motion",
             "correct": True},
            {"text": "Because your senses are too weak to notice small "
                     "movements",
             "correct": False,
             "why": "The motion is not small — it is steady, and steady "
                    "motion leaves nothing to detect."},
            {"text": "Because the train is not really moving until it stops",
             "correct": False,
             "why": "It is genuinely moving relative to the ground; what is "
                    "missing is any way to sense it from inside."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h16",
        "band": "harder",
        "text": "A runner runs at 4 m/s on a treadmill whose belt moves "
                "backwards at 4 m/s. What are her two speeds — relative to "
                "the room, and relative to the belt?",
        "options": [
            {"text": "4 m/s relative to the room, 0 m/s relative to the belt",
             "correct": False,
             "why": "The two are the wrong way round: she stays put in the "
                    "room and moves along the belt."},
            {"text": "0 m/s relative to the room, 4 m/s relative to the belt",
             "correct": True},
            {"text": "0 m/s relative to both", "correct": False,
             "why": "Relative to the belt she is genuinely running: that is "
                    "why it is exercise."},
            {"text": "8 m/s relative to the room, 4 m/s relative to the belt",
             "correct": False,
             "why": "Adding is for two objects moving apart. She and the belt "
                    "cancel, leaving her in the same place."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h17",
        "band": "harder",
        "text": "Two ships sail the same course, the faster at 12 m/s and the "
                "slower at 9 m/s, starting 600 m apart with the faster "
                "behind. How long until it draws level?",
        "options": [
            {"text": "50 s", "correct": False,
             "why": "That is 600 ÷ 12, using its own speed rather than the "
                    "speed it gains at."},
            {"text": "28.6 s", "correct": False,
             "why": "That is 600 ÷ 21, adding the speeds — which is the rule "
                    "for ships closing head-on."},
            {"text": "200 s", "correct": True},
            {"text": "66.7 s", "correct": False,
             "why": "That is 600 ÷ 9, using the slower ship's speed instead "
                    "of the difference."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h18",
        "band": "harder",
        "text": "A person sitting still has a speed of 0 m/s relative to the "
                "ground and about 30 000 m/s relative to the Sun. Which of "
                "these is the true speed?",
        "options": [
            {"text": "The 0 m/s, because that is what a stopwatch would "
                     "measure",
             "correct": False,
             "why": "A stopwatch on the Sun would measure the other one. "
                    "Neither instrument is more honest."},
            {"text": "The 30 000 m/s, because the Sun is the larger object",
             "correct": False,
             "why": "Size does not decide which frame counts; nothing makes "
                    "the Sun the correct one to measure from."},
            {"text": "Both, because a speed only means anything once its "
                     "frame is named",
             "correct": True},
            {"text": "Neither, because a real speed cannot depend on who "
                     "measures it",
             "correct": False,
             "why": "Every speed depends on the frame. That is what makes "
                    "naming it part of the answer."},
        ],
        "figure": None,
    },
]
