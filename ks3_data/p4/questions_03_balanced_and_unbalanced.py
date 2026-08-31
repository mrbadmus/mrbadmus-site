"""P4 lesson 03 — Balanced and unbalanced: twelve questions (MRB-223).

Written against Design's page. The two identical books, the support rig
and the two-panel beam are hers.

The discriminations, in the order the lesson builds them:

  · weight in newtons is mass in kilograms × 10 N/kg, and it is NOT the
    same number as the mass (`FORCE-22`);
  · a resultant of 0 N is not the same as no forces (`FORCE-20`);
  · a support pushes back with exactly what is needed, up to the point it
    gives way (`FORCE-23`);
  · balanced means NO CHANGE, not no motion (`FORCE-21`) — the harder
    band sits here.

⚠️ POSITION IS AUTHORED — index cycles 3, 2, 1, 0, giving three of each.

⚠️ Rung 1 (the 4 kg box on a bench) and Rung 2 (the lorry at 25 m/s) are
NOT restated; check 6 of `verify_questions.py` forbids it.
"""

UNIT = "P4"
LESSON = "balanced-and-unbalanced"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p4-03-e01",
        "band": "easier",
        "text": "What is the weight of a 6 kg bag, taking 10 N/kg?",
        "options": [
            {"text": "0.6 N", "correct": False,
             "why": "That is 6 ÷ 10. The mass is MULTIPLIED by 10 N/kg."},
            {"text": "16 N", "correct": False,
             "why": "That is 6 + 10. Nothing in weight = mass × 10 N/kg "
                    "adds."},
            {"text": "6 N", "correct": False,
             "why": "That is the mass in kilograms with the wrong unit "
                    "written after it. Weight and mass are different "
                    "quantities."},
            {"text": "60 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e02",
        "band": "easier",
        "text": "Balanced forces means…",
        "options": [
            {"text": "the object is stationary", "correct": False,
             "why": "Balanced means no CHANGE. A car at a steady 70 mph has "
                    "balanced forces and is not stationary."},
            {"text": "there are no forces on the object at all, which is "
                     "what being still means", "correct": False,
             "why": "There are forces; they cancel. Remove them and the "
                    "situation is completely different."},
            {"text": "the forces cancel to a resultant of 0 N, so nothing "
                     "about the motion changes", "correct": True},
            {"text": "the forces are all the same size", "correct": False,
             "why": "Three forces of different sizes can balance perfectly "
                    "well, as long as they cancel."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e03",
        "band": "easier",
        "text": "A 3 kg box rests on a table. How hard does the table push "
                "up?",
        "options": [
            {"text": "0 N — nothing is moving", "correct": False,
             "why": "Remove the table and the box falls, so the table must "
                    "have been doing something."},
            {"text": "30 N upwards", "correct": True},
            {"text": "3 N upwards", "correct": False,
             "why": "That is the mass, not the weight. Multiply by 10 N/kg."},
            {"text": "It depends how strong the table is", "correct": False,
             "why": "Not while it is holding. A surface pushes back with "
                    "exactly what is needed, right up to the point it gives "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e04",
        "band": "easier",
        "text": "Which of these describes UNBALANCED forces?",
        "options": [
            {"text": "A parked car", "correct": False,
             "why": "Nothing about its motion is changing, so the forces on "
                    "it cancel."},
            {"text": "A skydiver at terminal velocity", "correct": False,
             "why": "A steady speed is no change at all. Terminal velocity "
                    "is a balance."},
            {"text": "A book lying on a shelf", "correct": False,
             "why": "It stays exactly where it was put, so the shelf's push "
                    "matches its weight."},
            {"text": "A ball speeding up as it falls", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p4-03-s01",
        "band": "standard",
        "text": "A 250 g mug sits still on a shelf. How hard does the shelf "
                "push up?",
        "options": [
            {"text": "2 500 N", "correct": False,
             "why": "That multiplies the GRAMS by 10. Convert to kilograms "
                    "first: 250 g is 0.250 kg."},
            {"text": "250 N", "correct": False,
             "why": "That is the mass in grams with a newton written after "
                    "it. Grams are not kilograms."},
            {"text": "2.5 N", "correct": True},
            {"text": "0.25 N", "correct": False,
             "why": "That is the mass in kilograms. It still has to be "
                    "multiplied by 10 N/kg."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s02",
        "band": "standard",
        "text": "A 0.5 kg apple rests on a sheet of paper that gives way at "
                "about 2 N. What happens?",
        "options": [
            {"text": "The paper tears, because 5 N is more than 2 N.",
             "correct": True},
            {"text": "The paper holds, because 0.5 is less than 2.",
             "correct": False,
             "why": "That compares the MASS with a force. The weight is "
                    "0.5 × 10 = 5 N, which is what the paper has to hold."},
            {"text": "The paper holds, because paper always pushes back with "
                     "whatever is needed.", "correct": False,
             "why": "Only up to its limit. Beyond that it cannot supply the "
                    "force and the load goes through."},
            {"text": "The paper tears, because paper cannot hold anything at "
                     "all.", "correct": False,
             "why": "It can — a 0.1 kg load weighs 1 N and the sheet holds "
                    "that comfortably."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s03",
        "band": "standard",
        "text": "A 4 kg mass hangs from a spring and does not move. What is "
                "the resultant force on it, and what is the spring's pull?",
        "options": [
            {"text": "Resultant 40 N down; spring pull 0 N.",
             "correct": False,
             "why": "Then it would be falling. It is not moving, so nothing "
                    "is left over."},
            {"text": "Resultant 40 N up; spring pull 80 N.", "correct": False,
             "why": "That would lift it off. The spring stops stretching "
                    "when its pull matches the weight."},
            {"text": "Resultant 0 N; spring pull 40 N up.", "correct": True},
            {"text": "Resultant 0 N; spring pull 4 N up.", "correct": False,
             "why": "That is the mass in kilograms. The weight it has to "
                    "match is 4 × 10 = 40 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s04",
        "band": "standard",
        "text": "Why does a shelf hold a book with exactly the book's weight "
                "and not more?",
        "options": [
            {"text": "Because shelves are designed to match common book "
                     "weights.", "correct": False,
             "why": "The same shelf does the same thing for a mug, a plant "
                    "or a brick. Nothing was designed for the book."},
            {"text": "Because the surface is squashed very slightly, and it "
                     "stops squashing at the point where its push equals the "
                     "load.", "correct": True},
            {"text": "Because the book pulls the shelf down and the two "
                     "cancel by chance, which is why a shelf can hold "
                     "anything at all", "correct": False,
             "why": "It is not chance. The mechanism settles at equality "
                    "every time, which is why the answer is always exact."},
            {"text": "Because a shelf can only push with a fixed amount.",
             "correct": False,
             "why": "Then a light object would be flung off it. The push "
                    "changes with the load."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p4-03-h01",
        "band": "harder",
        "text": "A skydiver falls at a constant 55 m/s with the parachute "
                "still packed. What is true of the forces on them?",
        "options": [
            {"text": "They are unbalanced downwards, because the skydiver is "
                     "going down.", "correct": False,
             "why": "Going down is not a change. Balanced or not depends on "
                    "whether the motion is CHANGING."},
            {"text": "They are balanced, because the speed is not changing.",
             "correct": True},
            {"text": "There is no air resistance yet, because the parachute "
                     "is packed.", "correct": False,
             "why": "The air resistance is 750 N — the whole reason the "
                    "fall has stopped speeding up."},
            {"text": "They must be balanced, because balanced always means "
                     "not moving.", "correct": False,
             "why": "The verdict is right and the reason is wrong. Balanced "
                    "means no change, and this skydiver is moving fast."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h02",
        "band": "harder",
        "text": "A 900 kg lift hangs from a cable that can pull with up to "
                "12 000 N. It is at rest. How much spare pull does the cable "
                "have?",
        "options": [
            {"text": "3 000 N", "correct": True},
            {"text": "11 100 N", "correct": False,
             "why": "That is 12 000 − 900, subtracting the MASS from a "
                    "force. The weight is 900 × 10 = 9 000 N."},
            {"text": "None — at rest the cable is already at its limit.",
             "correct": False,
             "why": "At rest it only needs to supply the weight, 9 000 N. "
                    "Its limit is well above that."},
            {"text": "12 000 N, because at rest the cable is not pulling at "
                     "all.", "correct": False,
             "why": "At rest it is pulling with exactly the weight, or the "
                    "lift would fall."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h03",
        "band": "harder",
        "text": "A rope holding a heavy load snaps. Which statement best "
                "explains what happened in terms of forces?",
        "options": [
            {"text": "The load's weight suddenly increased past what the "
                     "rope could hold, so the rope gave way.",
             "correct": False,
             "why": "The weight never changed. What ran out was the rope's "
                    "ability to match it."},
            {"text": "The rope stopped being able to supply the force "
                     "needed, so the forces stopped being balanced.",
             "correct": True},
            {"text": "There were no forces on the rope until the moment it "
                     "snapped, when they all arrived at once.",
             "correct": False,
             "why": "It was holding the whole weight the entire time. That "
                    "is what eventually broke it."},
            {"text": "The rope's pull and the weight added together until "
                     "the total was more than the rope could bear.",
             "correct": False,
             "why": "They act in opposite directions, so they subtract. "
                    "Nothing accumulated."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h04",
        "band": "harder",
        "text": "An engineer says a bridge is designed so that its heaviest "
                "expected load still leaves it in balance, with a margin. "
                "What does the margin actually buy?",
        "options": [
            {"text": "It makes the resultant force on the bridge negative.",
             "correct": False,
             "why": "A resultant is 0 N or it is not. There is no negative "
                    "balance."},
            {"text": "It means the bridge pushes back harder than the load "
                     "presses down, which is how it stops the load sinking", "correct": False,
             "why": "It cannot: a support supplies exactly what is needed. "
                    "If it pushed harder the bridge would rise."},
            {"text": "It means an unexpected extra load still leaves the "
                     "bridge able to supply the force needed.",
             "correct": True},
            {"text": "It removes the forces on the bridge entirely.",
             "correct": False,
             "why": "The forces are there whatever the design. The margin is "
                    "about how far past the expected load they can go."},
        ],
        "figure": None,
    },
]
