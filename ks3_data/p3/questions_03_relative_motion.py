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
    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p3-03-e19",
        "band": "easier",
        "text": "A cyclist rides at 5 m/s and a car comes the other way at "
                "15 m/s. How fast are the two moving apart?",
        "options": [
            {"text": "10 m/s", "correct": False,
             "why": "That subtracts the speeds, which is what you do when "
                    "both are going the same way."},
            {"text": "15 m/s", "correct": False,
             "why": "That is the car's speed over the ground, and the cyclist "
                    "is moving too."},
            {"text": "20 m/s", "correct": True},
            {"text": "5 m/s", "correct": False,
             "why": "That is the cyclist's speed over the ground, not the "
                    "speed between the two."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e20",
        "band": "easier",
        "text": "Two aircraft fly side by side at 200 m/s in the same "
                "direction. One pilot looks across at the other. What does "
                "she see it doing?",
        "options": [
            {"text": "Pulling ahead at 200 m/s", "correct": False,
             "why": "Pulling ahead needs the other aircraft to be the faster, "
                    "and the two speeds match."},
            {"text": "Falling steadily behind at 200 m/s", "correct": False,
             "why": "Falling behind needs the other aircraft to be the "
                    "slower, and the two speeds match."},
            {"text": "Holding station beside her", "correct": True},
            {"text": "Pulling ahead at 400 m/s", "correct": False,
             "why": "400 adds the two speeds, and adding is for aircraft "
                    "flying towards each other."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e21",
        "band": "easier",
        "text": "Two lifts in the same shaft both rise at 2 m/s. What does a "
                "person in one see the other doing?",
        "options": [
            {"text": "Rising steadily at 2 m/s", "correct": False,
             "why": "That is its speed measured from the building, not from "
                    "the other lift."},
            {"text": "Rising steadily at 4 m/s", "correct": False,
             "why": "Speeds are added when two things move in opposite "
                    "directions, and these two move together."},
            {"text": "Falling steadily at 2 m/s", "correct": False,
             "why": "A lift appears to fall past another only when the other "
                    "is rising faster than it."},
            {"text": "Staying level with them", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e22",
        "band": "easier",
        "text": "A skater glides at 4 m/s beside a friend going the same way "
                "at 4 m/s. The friend then speeds up to 6 m/s. What is the "
                "friend's new speed relative to the skater?",
        "options": [
            {"text": "2 m/s", "correct": True},
            {"text": "6 m/s", "correct": False,
             "why": "That is the friend's speed over the ice, not the speed "
                    "between the two skaters."},
            {"text": "10 m/s", "correct": False,
             "why": "Speeds are added when two things move in opposite "
                    "directions, and these go the same way."},
            {"text": "0 m/s", "correct": False,
             "why": "They matched at first, but one has sped up, so the gap "
                    "between them now grows."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e23",
        "band": "easier",
        "text": "Every object is stationary when it is measured from "
                "something. From what is a moving train stationary?",
        "options": [
            {"text": "The platform it has just pulled away from",
             "correct": False,
             "why": "From the platform the train is moving away, at whatever "
                    "speed the driver was given."},
            {"text": "A passenger sitting in one of its seats",
             "correct": True},
            {"text": "The ground beneath the track", "correct": False,
             "why": "The ground is what a train's ordinary speed is measured "
                    "against in the first place."},
            {"text": "Nothing at all: a moving train is moving",
             "correct": False,
             "why": "Moving is not something an object holds on its own. It "
                    "is measured from something."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e24",
        "band": "easier",
        "text": "A police car is following a van along a motorway, and the "
                "two have a relative speed of 20 m/s. What is that 20 m/s "
                "telling you?",
        "options": [
            {"text": "How fast the gap between them changes", "correct": True},
            {"text": "How fast each car is going over the ground",
             "correct": False,
             "why": "Two cars at 60 and 40 m/s have the same relative speed "
                    "as two at 30 and 10 m/s."},
            {"text": "How far apart the two cars are at the moment",
             "correct": False,
             "why": "A relative speed says how the gap changes, not how big "
                    "the gap is."},
            {"text": "How fast the faster of the two is going",
             "correct": False,
             "why": "The relative speed is the difference or the sum, and not "
                    "one car's own reading."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e25",
        "band": "easier",
        "text": "A boat's speed is given as 8 m/s relative to the water. What "
                "does that phrase add that 8 m/s on its own would not?",
        "options": [
            {"text": "How long the boat's journey took", "correct": False,
             "why": "A time is a separate measurement and cannot be read out "
                    "of a speed."},
            {"text": "Which direction along the river the boat was going",
             "correct": False,
             "why": "A direction is not carried by naming what the speed was "
                    "measured against."},
            {"text": "How fast the water itself was flowing", "correct": False,
             "why": "The water's own speed is a further thing you would have "
                    "to be told."},
            {"text": "What the speed was measured against", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e26",
        "band": "easier",
        "text": "A seagull flies alongside a ferry, staying exactly level "
                "with the deck rail. The ferry is doing 9 m/s over the water. "
                "How fast is the seagull moving relative to the water?",
        "options": [
            {"text": "0 m/s", "correct": False,
             "why": "0 m/s is the seagull's speed relative to the ferry, "
                    "which is what staying level means."},
            {"text": "18 m/s", "correct": False,
             "why": "Doubling is for two things flying towards each other, "
                    "and these two travel together."},
            {"text": "9 m/s", "correct": True},
            {"text": "4.5 m/s", "correct": False,
             "why": "Halving a speed has no place in a relative-speed "
                    "question."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e27",
        "band": "easier",
        "text": "Two friends ride escalators side by side, one going up at "
                "0.6 m/s and one coming down at 0.6 m/s. How fast do they "
                "pass each other?",
        "options": [
            {"text": "0.6 m/s", "correct": False,
             "why": "That is one escalator's own speed, and the other friend "
                    "is moving as well."},
            {"text": "1.2 m/s", "correct": True},
            {"text": "0 m/s", "correct": False,
             "why": "A relative speed of zero needs both to move the same way "
                    "at the same speed."},
            {"text": "0.36 m/s", "correct": False,
             "why": "That multiplies the two speeds, and relative speeds are "
                    "added or subtracted."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e28",
        "band": "easier",
        "text": "A car travels at 20 m/s. A second car, 100 m behind it, also "
                "travels at 20 m/s. What happens to the gap between them?",
        "options": [
            {"text": "It stays at 100 m, because their relative speed is "
                     "0 m/s",
             "correct": True},
            {"text": "It closes in 5 s, because the gap closes at the speed "
                     "of the car behind",
             "correct": False,
             "why": "The gap closes at the relative speed, and 20 − 20 is 0."},
            {"text": "It grows, because the car behind is losing ground",
             "correct": False,
             "why": "Neither car is gaining on the other, so the gap does not "
                    "grow any more than it shrinks."},
            {"text": "It closes in 50 s, because the gap closes at 2 m/s",
             "correct": False,
             "why": "Subtracting 20 from 20 gives 0, not 2."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e29",
        "band": "easier",
        "text": "Two trains stand side by side in a station. One begins to "
                "move, and a passenger in the other feels certain it is their "
                "own train that has set off. Why?",
        "options": [
            {"text": "Because their own train has begun to move backwards "
                     "down the line",
             "correct": False,
             "why": "Their train has not moved. Nothing about it has "
                    "changed."},
            {"text": "Because the brakes on their own train have just been "
                     "released",
             "correct": False,
             "why": "A released brake does not make a stationary train appear "
                    "to move."},
            {"text": "Because the two trains are coupled together",
             "correct": False,
             "why": "Coupled trains move together, and these two do not."},
            {"text": "Because all they can see is one train moving past the "
                     "other",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-e30",
        "band": "easier",
        "text": "Which of these pairs has a relative speed of 0 m/s?",
        "options": [
            {"text": "A car and a lamp post it drives past", "correct": False,
             "why": "The lamp post stays put while the car moves, so there is "
                    "a speed between them."},
            {"text": "A lorry and its own trailer on the motorway",
             "correct": True},
            {"text": "Two trains passing in opposite directions on parallel "
                     "tracks",
             "correct": False,
             "why": "Opposite directions add, giving the biggest relative "
                    "speed of the four."},
            {"text": "A cyclist and a bus overtaking her", "correct": False,
             "why": "The bus is gaining on the cyclist, so their relative "
                    "speed is the difference between them."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p3-03-s19",
        "band": "standard",
        "text": "A 180 m train passes a person standing on a platform at "
                "30 m/s. How long does it take from the front reaching them "
                "to the back clearing them?",
        "options": [
            {"text": "6 s", "correct": True},
            {"text": "180 s", "correct": False,
             "why": "That is the train's length used as a time. It has to be "
                    "divided by the speed."},
            {"text": "30 s", "correct": False,
             "why": "That is the train's speed used as a time, which is not "
                    "what was asked for."},
            {"text": "5400 s", "correct": False,
             "why": "That multiplies the length by the speed instead of "
                    "dividing."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s20",
        "band": "standard",
        "text": "Two cars each travel at 15 m/s. Compare the speed at which "
                "they meet head-on with the speed at which one follows the "
                "other.",
        "options": [
            {"text": "15 m/s head-on, and 15 m/s following", "correct": False,
             "why": "Head-on adds the two speeds and following subtracts "
                    "them. Neither leaves 15."},
            {"text": "30 m/s head-on, and 0 m/s following", "correct": True},
            {"text": "30 m/s head-on, and 30 m/s following", "correct": False,
             "why": "Following subtracts the two speeds, and 15 − 15 is 0, "
                    "not 30."},
            {"text": "0 m/s head-on, and 30 m/s following", "correct": False,
             "why": "That is the right pair of numbers put the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s21",
        "band": "standard",
        "text": "A parcel rides a conveyor belt at 0.8 m/s. A worker walks "
                "beside the belt at 1.2 m/s the same way. How does the parcel "
                "move relative to the worker?",
        "options": [
            {"text": "At 0.4 m/s, forwards past her", "correct": False,
             "why": "She is the faster of the two, so she gains on the parcel "
                    "rather than losing ground to it."},
            {"text": "At 2.0 m/s, backwards past her", "correct": False,
             "why": "2.0 adds the two speeds, and adding is for things going "
                    "opposite ways."},
            {"text": "At 0.4 m/s, backwards past her", "correct": True},
            {"text": "At 0.8 m/s, the belt's own speed", "correct": False,
             "why": "0.8 m/s is the parcel's speed over the floor, not "
                    "relative to a moving worker."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s22",
        "band": "standard",
        "text": "An escalator 24 m long carries people up at 0.5 m/s. A man "
                "walks up it at 0.7 m/s relative to the steps. How long does "
                "he take to reach the top?",
        "options": [
            {"text": "48 s", "correct": False,
             "why": "That uses the escalator's speed alone and leaves the "
                    "walking out."},
            {"text": "34 s", "correct": False,
             "why": "That uses the walking speed alone and leaves the "
                    "escalator out."},
            {"text": "12 s", "correct": False,
             "why": "That doubles the combined speed: 0.5 and 0.7 make 1.2, "
                    "not 2.0."},
            {"text": "20 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s23",
        "band": "standard",
        "text": "The driver of car A measures car B going past at 9 m/s. What "
                "does the driver of car B measure for car A?",
        "options": [
            {"text": "9 m/s, the same size", "correct": True},
            {"text": "0 m/s, because A is the one moving", "correct": False,
             "why": "Both readings are made between the same two cars, so "
                    "neither of them can be zero here."},
            {"text": "18 m/s, twice as much", "correct": False,
             "why": "The two are not added. The same gap is closing for both "
                    "drivers."},
            {"text": "It depends which car is faster over the ground",
             "correct": False,
             "why": "The ground speeds can be anything; only the difference "
                    "between them settles this."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s24",
        "band": "standard",
        "text": "On a 400 m track, one runner holds 5 m/s and another holds "
                "4 m/s, both the same way round. How long after the start "
                "does the faster runner lead by a whole lap?",
        "options": [
            {"text": "80 s", "correct": False,
             "why": "That divides the lap by 5 m/s, using one runner's speed "
                    "rather than the difference."},
            {"text": "44 s", "correct": False,
             "why": "That divides the lap by 9 m/s, adding the speeds as "
                    "though they ran towards each other."},
            {"text": "100 s", "correct": False,
             "why": "That divides the lap by 4 m/s, using the slower runner's "
                    "speed."},
            {"text": "400 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s25",
        "band": "standard",
        "text": "Whatever you choose to measure speeds from, one speed always "
                "comes out as zero. Which one?",
        "options": [
            {"text": "The speed of the ground", "correct": False,
             "why": "The ground reads zero when you stand on it, and not when "
                    "you measure from a moving car."},
            {"text": "The speed of the slowest object in sight",
             "correct": False,
             "why": "The slowest thing still has a speed unless you happen to "
                    "be travelling with it."},
            {"text": "The speed of whatever you are measuring from",
             "correct": True},
            {"text": "The speed of anything that is not moving at all",
             "correct": False,
             "why": "Whether something is moving is the very thing that has "
                    "to be settled, by naming a frame."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s26",
        "band": "standard",
        "text": "A plane approaches an aircraft carrier at 70 m/s over the "
                "water. The carrier is sailing at 10 m/s in the same "
                "direction. What is the plane's speed relative to the deck?",
        "options": [
            {"text": "80 m/s", "correct": False,
             "why": "Speeds are added when the two move in opposite "
                    "directions, and these move the same way."},
            {"text": "70 m/s", "correct": False,
             "why": "70 m/s is the plane's speed over the water, and the deck "
                    "is moving too."},
            {"text": "60 m/s", "correct": True},
            {"text": "10 m/s", "correct": False,
             "why": "10 m/s is the carrier's own speed over the water."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s27",
        "band": "standard",
        "text": "One student says a train is doing 0 m/s and another says it "
                "is doing 50 m/s. Both are right. How?",
        "options": [
            {"text": "One gave the average speed and the other the top speed",
             "correct": False,
             "why": "Both numbers describe the same moment. It is the "
                    "viewpoint that differs, not the kind of speed."},
            {"text": "They measured from different things — one from inside "
                     "the train, one from the ground",
             "correct": True},
            {"text": "One used kilometres per hour and the other metres per "
                     "second",
             "correct": False,
             "why": "50 km/h and 50 m/s are different numbers, and neither of "
                    "them is zero."},
            {"text": "The train changed speed between the two measurements",
             "correct": False,
             "why": "Nothing says the train changed. The two readings are of "
                    "one moment."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s28",
        "band": "standard",
        "text": "A lorry does 18 m/s and a car ahead of it does 24 m/s, both "
                "the same way. The gap between them is 25 m now. What is it "
                "10 s later?",
        "options": [
            {"text": "25 m", "correct": False,
             "why": "The gap stays the same only when the two speeds match, "
                    "and these differ by 6 m/s."},
            {"text": "60 m", "correct": False,
             "why": "That is the growth in the gap; the 25 m it started at "
                    "still has to be added on."},
            {"text": "445 m", "correct": False,
             "why": "That uses 42 m/s, the sum of the speeds, instead of the "
                    "difference between them."},
            {"text": "85 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s29",
        "band": "standard",
        "text": "A ship sails at 9 m/s relative to the water, straight down a "
                "channel where the water flows at 2 m/s the same way. How "
                "long does it take to cover 3300 m over the ground?",
        "options": [
            {"text": "300 s", "correct": True},
            {"text": "367 s", "correct": False,
             "why": "That uses 9 m/s and ignores the water carrying the ship "
                    "along with it."},
            {"text": "471 s", "correct": False,
             "why": "That uses 7 m/s, taking the flow off instead of adding "
                    "it on."},
            {"text": "1650 s", "correct": False,
             "why": "That uses 2 m/s, the water's speed on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-s30",
        "band": "standard",
        "text": "A satellite's speed is given as 7800 m/s. Relative to what "
                "is that measured, and what is its speed relative to the "
                "astronaut riding in it?",
        "options": [
            {"text": "Relative to the astronaut, and 7800 m/s relative to the "
                     "ground",
             "correct": False,
             "why": "A speed measured from the astronaut would be zero, since "
                    "she travels with the satellite."},
            {"text": "Relative to the ground below, and 0 m/s relative to the "
                     "astronaut",
             "correct": True},
            {"text": "Relative to the Sun, and 7800 m/s relative to the "
                     "astronaut",
             "correct": False,
             "why": "Orbit speeds are quoted against the Earth, and the "
                    "astronaut moves with the satellite."},
            {"text": "Relative to the ground below, and 7800 m/s relative to "
                     "the astronaut",
             "correct": False,
             "why": "The first half is right, but the astronaut sits still "
                    "inside, so her reading is zero."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p3-03-h19",
        "band": "harder",
        "text": "A 120 m train travelling at 35 m/s overtakes a 180 m train "
                "travelling at 25 m/s on the next track, both going the same "
                "way. How long from its front reaching the slower train's "
                "back to its own back clearing the slower train's front?",
        "options": [
            {"text": "5 s", "correct": False,
             "why": "That divides 300 m by 60 m/s, adding the speeds as "
                    "though the trains met head-on."},
            {"text": "12 s", "correct": False,
             "why": "That divides 120 m by 10 m/s, using the overtaking "
                    "train's length on its own."},
            {"text": "30 s", "correct": True},
            {"text": "18 s", "correct": False,
             "why": "That divides 180 m by 10 m/s, using the slower train's "
                    "length on its own."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h20",
        "band": "harder",
        "text": "A canoeist paddles at 5 m/s in still water. She goes 1200 m "
                "downstream on a 1 m/s current, then 1200 m back up. What is "
                "her average speed over the whole trip, relative to the bank?",
        "options": [
            {"text": "5 m/s", "correct": False,
             "why": "5 m/s is her paddling speed through the water, and the "
                    "current changes what the bank sees."},
            {"text": "6 m/s", "correct": False,
             "why": "6 m/s is her speed on the downstream leg only."},
            {"text": "2.4 m/s", "correct": False,
             "why": "That divides one leg's distance by the whole trip's "
                    "time."},
            {"text": "4.8 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h21",
        "band": "harder",
        "text": "Two cars, each doing 20 m/s, meet head-on. A student says "
                "that is the same closing speed as one car doing 40 m/s "
                "meeting a parked car. In terms of relative speed, is the "
                "student right?",
        "options": [
            {"text": "No — the closing speed head-on is 20 m/s",
             "correct": False,
             "why": "Opposite directions add, so the two cars close on each "
                    "other at 40 m/s."},
            {"text": "Yes — the closing speed is 40 m/s either way",
             "correct": True},
            {"text": "No — the closing speed head-on is 80 m/s",
             "correct": False,
             "why": "Adding 20 and 20 gives 40, and 80 doubles it a second "
                    "time."},
            {"text": "Yes, but only because both cars have the same mass",
             "correct": False,
             "why": "A relative speed is worked out from speeds and "
                    "directions, and mass plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h22",
        "band": "harder",
        "text": "Why does the speed of the vehicle you are sitting in come "
                "out as 0 m/s however fast it is going?",
        "options": [
            {"text": "Because a vehicle cannot measure its own speed",
             "correct": False,
             "why": "It can — a speedometer does — but that reading is made "
                    "against the road, not against itself."},
            {"text": "Because the speedometer is switched off at the time",
             "correct": False,
             "why": "Nothing has been switched off. The answer comes from "
                    "what the speed is measured against."},
            {"text": "Because the road is moving instead of the vehicle",
             "correct": False,
             "why": "From that seat the road does move, but the zero belongs "
                    "to the vehicle itself."},
            {"text": "Because its speed is being measured against itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h23",
        "band": "harder",
        "text": "A lorry 16 m long takes 32 s to overtake a cyclist, from its "
                "front reaching her to its back clearing her. The cyclist "
                "rides at 6 m/s. How fast is the lorry going?",
        "options": [
            {"text": "0.5 m/s", "correct": False,
             "why": "0.5 m/s is the lorry's speed relative to the cyclist, "
                    "not its speed over the road."},
            {"text": "5.5 m/s", "correct": False,
             "why": "That takes the relative speed off instead of adding it, "
                    "and an overtaking lorry is the faster."},
            {"text": "6.5 m/s", "correct": True},
            {"text": "6 m/s", "correct": False,
             "why": "At the cyclist's own speed the lorry would sit beside "
                    "her rather than pass her."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h24",
        "band": "harder",
        "text": "A traveller walks at 1.4 m/s. A 70 m moving walkway runs at "
                "0.6 m/s. How much time does walking along the walkway save "
                "compared with walking beside it?",
        "options": [
            {"text": "35 s", "correct": False,
             "why": "35 s is the time taken on the walkway, not the time "
                    "saved by using it."},
            {"text": "15 s", "correct": True},
            {"text": "50 s", "correct": False,
             "why": "50 s is the time taken walking beside the walkway, not "
                    "the saving."},
            {"text": "117 s", "correct": False,
             "why": "That divides 70 m by 0.6 m/s, leaving the walking out "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h25",
        "band": "harder",
        "text": "Two cars travel the same way at 30 m/s and 22 m/s. How fast "
                "does one move relative to the other, worked out by a "
                "roadside observer, by the faster driver, and by the slower "
                "driver?",
        "options": [
            {"text": "52 m/s from the roadside, and 8 m/s from each car",
             "correct": False,
             "why": "52 adds the two speeds, and adding is for cars going "
                    "opposite ways."},
            {"text": "0 m/s from the roadside, and 8 m/s from each car",
             "correct": False,
             "why": "A roadside observer works out the same 8 m/s difference "
                    "that each driver sees."},
            {"text": "8 m/s from the faster car, and 52 m/s from the slower",
             "correct": False,
             "why": "Both drivers see the same gap closing, so both get "
                    "8 m/s."},
            {"text": "8 m/s from the roadside, and 8 m/s from each car",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h26",
        "band": "harder",
        "text": "A river ferry is advertised as doing 6 m/s. Going upstream "
                "against a 2 m/s current it takes twice as long to cover a "
                "stretch as it does coming back down. Which frame was the "
                "6 m/s measured in?",
        "options": [
            {"text": "Relative to the water", "correct": True},
            {"text": "Relative to the bank, going upstream", "correct": False,
             "why": "Upstream over the bank it makes 4 m/s, and 4 against 8 "
                    "coming back is what gives the doubling."},
            {"text": "Relative to the bank, going downstream",
             "correct": False,
             "why": "Downstream over the bank it makes 8 m/s, which is not "
                    "the figure advertised."},
            {"text": "Relative to the ferry itself", "correct": False,
             "why": "Measured from the ferry, the ferry's own speed is "
                    "zero."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h27",
        "band": "harder",
        "text": "A runner sets off at 4 m/s. Thirty seconds later a cyclist "
                "sets off from the same place at 7 m/s, the same way. How "
                "long after the CYCLIST starts does she draw level?",
        "options": [
            {"text": "30 s", "correct": False,
             "why": "30 s is the runner's head start in time, not the time "
                    "the catching takes."},
            {"text": "40 s", "correct": True},
            {"text": "17 s", "correct": False,
             "why": "That divides the 120 m head start by 7 m/s rather than "
                    "by the 3 m/s difference."},
            {"text": "70 s", "correct": False,
             "why": "That divides the head start by 1.7 m/s, and the "
                    "difference between the speeds is 3 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h28",
        "band": "harder",
        "text": "A pilot reports 250 m/s while the aircraft flying alongside "
                "reports 900 km/h. Are the two keeping station with each "
                "other?",
        "options": [
            {"text": "No — the second aircraft is faster, at 900 m/s",
             "correct": False,
             "why": "900 km/h is not 900 m/s. Dividing by 3.6 turns it into "
                    "250 m/s."},
            {"text": "No — the second aircraft is slower, at 90 m/s",
             "correct": False,
             "why": "Dividing by 10 is not the conversion; km/h becomes m/s "
                    "on dividing by 3.6."},
            {"text": "Yes — 900 km/h is 250 m/s, so neither gains",
             "correct": True},
            {"text": "No — two speeds in different units cannot be compared",
             "correct": False,
             "why": "They can, once one is converted, and comparing is "
                    "exactly what the conversion is for."},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h29",
        "band": "harder",
        "text": "A passenger walks at 1.2 m/s towards the front of a bus "
                "doing 14 m/s. A cyclist rides the other way along the road "
                "at 5 m/s. How fast is the passenger moving relative to the "
                "cyclist?",
        "options": [
            {"text": "9 m/s", "correct": False,
             "why": "That subtracts the cyclist's speed, and the two are "
                    "moving in opposite directions."},
            {"text": "6.2 m/s", "correct": False,
             "why": "That combines the walking and the cycling and leaves the "
                    "bus out."},
            {"text": "10.2 m/s", "correct": False,
             "why": "That adds the walking to the bus and then subtracts the "
                    "cyclist instead of adding."},
            {"text": "20.2 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-03-h30",
        "band": "harder",
        "text": "A train pulls alongside yours at the same speed and appears "
                "parked in your window. A moment later it edges ahead. What "
                "has changed?",
        "options": [
            {"text": "Its speed relative to your train is no longer zero",
             "correct": True},
            {"text": "Both trains again have the same speed over the ground",
             "correct": False,
             "why": "Equal ground speeds are what made it appear parked, and "
                    "it is edging ahead now."},
            {"text": "The gap between the two trains has changed their "
                     "relative speed",
             "correct": False,
             "why": "How far apart two things are does not enter a relative "
                    "speed."},
            {"text": "Its speed relative to the platform has become zero",
             "correct": False,
             "why": "A train with zero speed over the ground would be left "
                    "behind, not edging ahead."},
        ],
        "figure": None,
    },
]

