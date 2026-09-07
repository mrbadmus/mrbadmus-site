"""P4 lesson 06 — Air and water resistance: twelve questions (MRB-223).

Written against Design's page. The skydiver, the fall bench and the
four-stage strip are hers.

The discriminations, in the order the lesson builds them:

  · resistance acts against the motion and GROWS with speed
    (`FORCE-33`);
  · a bigger area facing the flow means more resistance;
  · terminal velocity is a BALANCE, not a limit (`FORCE-35`);
  · an upward resultant means slowing, not rising (`FORCE-34`) — the
    harder band sits here;
  · what decides which of two objects falls faster is the balance
    between weight and resistance, not the weight (`FORCE-32`).

⚠️ POSITION IS AUTHORED — index cycles 1, 3, 0, 2, giving three of each.

⚠️ Rung 1 (the 1 N hailstone) and Rung 2 (the lead and plastic balls) are
NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "air-and-water-resistance"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-06-e01",
        "band": "easier",
        "text": "Air resistance on a falling object acts…",
        "options": [
            {"text": "downwards, adding to the weight", "correct": False,
             "why": "It acts AGAINST the motion. A falling object is going "
                    "down, so the resistance pushes up."},
            {"text": "upwards, against the motion", "correct": True},
            {"text": "sideways", "correct": False,
             "why": "It acts along the line of travel, opposing it."},
            {"text": "only once the object is falling fast", "correct": False,
             "why": "It acts at any speed above zero. It is simply very "
                    "small at low speed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e02",
        "band": "easier",
        "text": "What happens to air resistance as an object falls faster?",
        "options": [
            {"text": "It stays the same", "correct": False,
             "why": "Then a falling object would never stop speeding up, and "
                    "skydivers would not survive."},
            {"text": "It gets smaller", "correct": False,
             "why": "Faster means more air shoved aside every second, so it "
                    "gets bigger."},
            {"text": "It disappears", "correct": False,
             "why": "The opposite. It grows until it can match the weight."},
            {"text": "It gets bigger", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e03",
        "band": "easier",
        "text": "A skydiver has stopped getting any faster. What is the "
                "resultant force on them?",
        "options": [
            {"text": "0 N", "correct": True},
            {"text": "750 N downwards", "correct": False,
             "why": "That is their weight alone, which would mean the "
                    "resistance was zero and they were still speeding up."},
            {"text": "750 N upwards", "correct": False,
             "why": "That is the resistance alone. The weight is still "
                    "acting and cancels it."},
            {"text": "It cannot be worked out without the speed.",
             "correct": False,
             "why": "“Stopped getting faster” is enough: no change means "
                    "nothing left over."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e04",
        "band": "easier",
        "text": "Why is a parachute made large?",
        "options": [
            {"text": "To make the skydiver weigh less", "correct": False,
             "why": "The weight is unchanged. What changes is the force "
                    "resisting the fall."},
            {"text": "To catch the wind and lift the skydiver upwards, so "
                     "that the fall turns into a rise",
             "correct": False,
             "why": "Nobody goes up. The canopy slows the fall; it does not "
                    "reverse it."},
            {"text": "To present a much bigger area to the air, which gives "
                     "far more resistance", "correct": True},
            {"text": "To make the skydiver more streamlined",
             "correct": False,
             "why": "The opposite — a canopy is designed to be as UN"
                    "streamlined as possible."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-06-s01",
        "band": "standard",
        "text": "A skydiver steps out of the aircraft and is barely moving. "
                "What is the air resistance at that instant?",
        "options": [
            {"text": "The same as their weight", "correct": False,
             "why": "Then the fall would never begin. The resistance has to "
                    "grow first."},
            {"text": "Close to 0 N", "correct": True},
            {"text": "Bigger than their weight", "correct": False,
             "why": "That would push them back up before they had started to "
                    "fall."},
            {"text": "Exactly half their weight", "correct": False,
             "why": "There is no such rule, and at almost no speed almost no "
                    "air is being pushed aside."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s02",
        "band": "standard",
        "text": "A skydiver changes from spread-out to head-down. What "
                "happens to their terminal velocity?",
        "options": [
            {"text": "It falls, because a head-down skydiver weighs less "
                     "than a spread-out one",
             "correct": False,
             "why": "Their weight is exactly the same in either posture."},
            {"text": "It stays the same, because weight is what sets it and "
                     "that has not changed", "correct": False,
             "why": "The weight has not changed, but the AREA facing the "
                    "flow has, so the balance point moves."},
            {"text": "It cannot change without a parachute, because posture "
                     "does not set it",
             "correct": False,
             "why": "Posture alone changes it — from about 55 m/s to "
                    "about 80 m/s."},
            {"text": "It rises, because a smaller area means less resistance "
                     "at any given speed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s03",
        "band": "standard",
        "text": "A car with the accelerator flat to the floor stops speeding "
                "up at its top speed. Why?",
        "options": [
            {"text": "The engine has run out of force.", "correct": False,
             "why": "The engine is still working just as hard. What has "
                    "changed is what it is up against."},
            {"text": "The backwards forces have grown until they match the "
                     "forward force, so the resultant is 0 N.",
             "correct": True},
            {"text": "There is a legal limit built into the car.",
             "correct": False,
             "why": "Some cars have one, but the physics reason is about "
                    "forces, not about a limiter."},
            {"text": "The car has reached the fastest speed anything can "
                     "travel, which is fixed and the same for everything", "correct": False,
             "why": "It is this car's balance point, not a universal limit. "
                    "A more powerful car settles higher."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s04",
        "band": "standard",
        "text": "Why does a swimmer at 2 m/s feel more resistance than a "
                "runner at 4 m/s?",
        "options": [
            {"text": "Because swimming uses more muscles.", "correct": False,
             "why": "The question is about the force from the fluid, not "
                    "about effort."},
            {"text": "Because water is much denser than air — a cubic metre "
                     "of it has around eight hundred times the mass.",
             "correct": True},
            {"text": "Because water resistance does not depend on speed, so "
                     "it is the same however fast you go",
             "correct": False,
             "why": "It does, exactly as air resistance does. The difference "
                    "is what is being shoved aside."},
            {"text": "Because a swimmer is bigger than a runner.",
             "correct": False,
             "why": "They are the same person. Only the fluid has changed."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-06-h01",
        "band": "harder",
        "text": "The moment a parachute opens, the resultant force points "
                "UPWARDS. What is the skydiver doing?",
        "options": [
            {"text": "Rising, because the resultant is upwards.",
             "correct": False,
             "why": "An upward resultant means the DOWNWARD motion is "
                    "changing, which here means slowing. Nobody goes up."},
            {"text": "Falling, and slowing down hard.", "correct": True},
            {"text": "Hanging still in the air.", "correct": False,
             "why": "Still would need a resultant of 0 N. There is a large "
                    "one."},
            {"text": "Falling at exactly the same speed as before.",
             "correct": False,
             "why": "A resultant force always changes the motion. This one "
                    "changes it violently."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h02",
        "band": "harder",
        "text": "An astronaut on the Moon drops a hammer and a feather "
                "together and they land together. Why does the same test "
                "fail on Earth?",
        "options": [
            {"text": "Because the Moon's gravity is weaker.",
             "correct": False,
             "why": "Weaker gravity slows both equally. It is not what makes "
                    "the difference."},
            {"text": "Because the feather is lighter, and weight decides "
                     "how fast things fall, so a heavier thing always wins "
                     "whatever the air is doing to either of them", "correct": False,
             "why": "Then the Moon test would fail too. Weight on its own "
                    "does not decide it."},
            {"text": "Because on Earth the air resists both, and that "
                     "resistance is a large share of the feather's weight "
                     "and a tiny share of the hammer's.", "correct": True},
            {"text": "Because the Moon has no gravity at all.",
             "correct": False,
             "why": "It has about a sixth of Earth's. Without any, nothing "
                    "would have fallen."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h03",
        "band": "harder",
        "text": "Air resistance roughly QUADRUPLES when the speed doubles. "
                "Why?",
        "options": [
            {"text": "Because the object gets heavier as it speeds up, and "
                     "a heavier object needs more to hold it back",
             "correct": False,
             "why": "Its weight is unchanged. Only the resistance grows."},
            {"text": "Because you hit twice as much air per second, and hit "
                     "each bit of it twice as hard.", "correct": True},
            {"text": "Because air gets denser at higher speeds.",
             "correct": False,
             "why": "The air is the same. What changes is how much of it you "
                    "meet and how hard."},
            {"text": "Because the area facing the flow doubles.",
             "correct": False,
             "why": "The area is fixed by the shape. It is the speed that "
                    "has changed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h04",
        "band": "harder",
        "text": "Fish, dolphins, submarines and torpedoes all end up with a "
                "rounded nose and a tapering tail. What is the test of a "
                "good streamlined shape?",
        "options": [
            {"text": "How pointed the front is.", "correct": False,
             "why": "A very sharp nose is not the winner — the tail "
                    "matters more than the nose."},
            {"text": "How heavy the object is.", "correct": False,
             "why": "Weight is a separate question entirely. Streamlining is "
                    "about the shape."},
            {"text": "How smooth the surface feels.", "correct": False,
             "why": "Surface finish helps a little, but a blunt-tailed "
                    "smooth object still churns the water badly."},
            {"text": "How little wake it leaves behind.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-06-e05",
        "band": "easier",
        "text": "Which of these INCREASES the air resistance on a moving car?",
        "options": [
            {"text": "Fitting a large roof box", "correct": True},
            {"text": "Polishing the paintwork until it shines",
             "correct": False,
             "why": "A smoother surface slightly reduces resistance rather "
                    "than adding to it."},
            {"text": "Driving more slowly along the same road",
             "correct": False,
             "why": "Resistance grows with speed, so going slower makes it "
                    "smaller."},
            {"text": "Letting some air out of the tyres", "correct": False,
             "why": "That changes the friction at the road, not how much air "
                    "the car has to push aside."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-e06",
        "band": "easier",
        "text": "What is terminal velocity?",
        "options": [
            {"text": "The fastest speed anything is allowed to fall at",
             "correct": False,
             "why": "It is not a rule or a limit. It is simply where the "
                    "forces happen to balance for that object."},
            {"text": "The speed at which a falling object hits the ground",
             "correct": False,
             "why": "It is reached well before landing, and an object can "
                    "land at other speeds entirely."},
            {"text": "The steady speed reached once resistance has grown to "
                     "match the weight",
             "correct": True},
            {"text": "The speed at which air resistance disappears",
             "correct": False,
             "why": "Air resistance is at its largest there — that is exactly "
                    "why the speed stops rising."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-06-s05",
        "band": "standard",
        "text": "A skydiver of weight 800 N is falling at terminal velocity. "
                "What is the air resistance on them?",
        "options": [
            {"text": "0 N, because the speed is steady", "correct": False,
             "why": "A steady speed means the RESULTANT is zero, which needs "
                    "the resistance to equal the weight."},
            {"text": "More than 800 N, or they would not have stopped "
                     "speeding up",
             "correct": False,
             "why": "More than 800 N would slow them down. Steady means "
                    "exactly equal."},
            {"text": "800 N, acting upwards on them", "correct": True},
            {"text": "It cannot be given without knowing the speed",
             "correct": False,
             "why": "Whatever the speed turns out to be, at terminal velocity "
                    "the resistance equals the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-s06",
        "band": "standard",
        "text": "A flat sheet of paper falls slowly, but the same sheet "
                "screwed into a tight ball falls quickly. Why?",
        "options": [
            {"text": "Because screwing it up makes it heavier",
             "correct": False,
             "why": "The paper is the same paper, so its weight has not "
                    "changed at all."},
            {"text": "Because the flat sheet has a much larger area facing "
                     "the air",
             "correct": True},
            {"text": "Because a ball is a more natural shape for falling",
             "correct": False,
             "why": "Shape matters only through the area meeting the air and "
                    "how smoothly it parts."},
            {"text": "Because gravity pulls harder on compact objects",
             "correct": False,
             "why": "Gravity depends on mass, which is unchanged by folding "
                    "the sheet up."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-06-h05",
        "band": "harder",
        "text": "Two skydivers have the same shape and posture, but one is "
                "heavier. Why does the heavier one reach a higher terminal "
                "velocity?",
        "options": [
            {"text": "Because gravity pulls heavier objects faster from the "
                     "start",
             "correct": False,
             "why": "Both start with the same acceleration; it is where the "
                    "balance point falls that differs."},
            {"text": "Because a heavier body pushes the air out of the way "
                     "rather than being slowed",
             "correct": False,
             "why": "Both push the air aside. The heavier one simply needs "
                    "more resistance before it balances."},
            {"text": "Because heavier objects have less air resistance at any "
                     "speed",
             "correct": False,
             "why": "Resistance depends on speed and area, not on weight, so "
                    "at a given speed it is the same."},
            {"text": "Because the resistance must grow larger to match the "
                     "bigger weight, and that needs more speed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-06-h06",
        "band": "harder",
        "text": "Submarines and aircraft are both streamlined. Why does "
                "streamlining matter more in water than in air at the same "
                "speed?",
        "options": [
            {"text": "Because water is far denser, so far more of it must be "
                     "pushed aside",
             "correct": True},
            {"text": "Because water is colder than air, so it grips the hull "
                     "harder",
             "correct": False,
             "why": "Temperature is not what makes the resistance large; how "
                    "much material is in the way is."},
            {"text": "Because a submarine travels much faster than an "
                     "aircraft",
             "correct": False,
             "why": "It is much slower, and the question compares them at the "
                    "same speed anyway."},
            {"text": "Because water resistance does not grow with speed, so "
                     "shape is all that is left",
             "correct": False,
             "why": "Water resistance grows with speed exactly as air "
                    "resistance does."},
        ],
        "figure": None,
    },
]
