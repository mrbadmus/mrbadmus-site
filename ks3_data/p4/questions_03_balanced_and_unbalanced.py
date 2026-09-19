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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "3 000 N — 12 000 minus 9 000", "correct": True},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-03-e05",
        "band": "easier",
        "text": "What is the weight of a 12 kg suitcase, taking gravity as "
                "10 N/kg?",
        "options": [
            {"text": "1.2 N", "correct": False,
             "why": "That is 12 ÷ 10. Weight is the mass MULTIPLIED by "
                    "10 N/kg."},
            {"text": "12 N", "correct": False,
             "why": "That is the mass with the unit swapped. A kilogram is "
                    "not a newton."},
            {"text": "120 N", "correct": True},
            {"text": "22 N", "correct": False,
             "why": "That is 12 + 10, and a mass and a gravitational field "
                    "strength cannot be added."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e06",
        "band": "easier",
        "text": "A car is driving along a straight road at a steady speed. "
                "The forces on it are…",
        "options": [
            {"text": "balanced, with a resultant of 0 N", "correct": True},
            {"text": "unbalanced, pointing forwards", "correct": False,
             "why": "A forward resultant would make it speed up, and the "
                    "speed is steady."},
            {"text": "unbalanced, pointing backwards", "correct": False,
             "why": "A backward resultant would slow it down, and the speed "
                    "is not falling."},
            {"text": "zero, because nothing is touching it", "correct": False,
             "why": "Plenty is touching it — the road and the air. Their "
                    "forces cancel rather than being absent."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-03-s05",
        "band": "standard",
        "text": "A 60 kg student stands still on a floor. How hard does the "
                "floor push up, taking gravity as 10 N/kg?",
        "options": [
            {"text": "60 N", "correct": False,
             "why": "That is the mass in kilograms, not a force. Multiply by "
                    "10 N/kg first."},
            {"text": "600 N", "correct": True},
            {"text": "6 N", "correct": False,
             "why": "That is 60 ÷ 10, the division the wrong way round."},
            {"text": "As hard as the floor is able to push", "correct": False,
             "why": "A support pushes back as hard as it NEEDS to, which here "
                    "is exactly the student's weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s06",
        "band": "standard",
        "text": "A 5 kg box hangs at rest from a rope. What is the tension in "
                "the rope, and the resultant force on the box?",
        "options": [
            {"text": "50 N and a resultant of 0 N", "correct": True},
            {"text": "50 N and a resultant of 50 N", "correct": False,
             "why": "The box is at rest, so the two 50 N forces must cancel "
                    "to nothing."},
            {"text": "5 N and a resultant of 0 N", "correct": False,
             "why": "5 is the mass in kilograms. The weight is 5 × 10 N/kg."},
            {"text": "100 N and a resultant of 0 N", "correct": False,
             "why": "That doubles the weight; the rope pulls up with exactly "
                    "as much as gravity pulls down."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-03-h05",
        "band": "harder",
        "text": "A 700 kg lift hangs at rest from a cable rated to pull with "
                "up to 9000 N. How much spare pull has the cable, taking "
                "gravity as 10 N/kg?",
        "options": [
            {"text": "8300 N, the rating minus the mass", "correct": False,
             "why": "700 is a mass in kilograms and cannot be subtracted from "
                    "a force in newtons."},
            {"text": "None — a cable at rest is already at its limit",
             "correct": False,
             "why": "At rest it only pulls with the weight, which is well "
                    "below what it can manage."},
            {"text": "2000 N of pull to spare", "correct": True},
            {"text": "9000 N, because the lift is not moving", "correct": False,
             "why": "It is already pulling with 7000 N to hold the lift up, "
                    "so not all of the rating is spare."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h06",
        "band": "harder",
        "text": "A student says balanced forces mean an object is stopped. "
                "Which example shows that is wrong?",
        "options": [
            {"text": "A book on a table, pushed up with exactly its weight",
             "correct": False,
             "why": "The book IS stopped, so it fits the student's claim "
                    "rather than testing it."},
            {"text": "A lorry at a steady 25 m/s with 4000 N of drive and "
                     "drag",
             "correct": True},
            {"text": "A ball at the top of its flight, momentarily at rest",
             "correct": False,
             "why": "Its forces are unbalanced there — gravity still pulls "
                    "down — so it is not a balanced case."},
            {"text": "A car speeding up with more drive than drag",
             "correct": False,
             "why": "That is unbalanced by definition, so it says nothing "
                    "about what balanced means."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p4-03-e07",
        "band": "easier",
        "text": "A tin has a mass of 2 kg. Using 10 N/kg, how heavy is it in "
                "newtons?",
        "options": [
            {"text": "0.2 N", "correct": False,
             "why": "That is 2 ÷ 10. The mass is multiplied by 10 N/kg, not "
                    "divided by it."},
            {"text": "12 N", "correct": False,
             "why": "That is 2 + 10, and a mass cannot be added to a "
                    "gravitational field strength."},
            {"text": "2 N", "correct": False,
             "why": "That is the mass with a newton written after it. A "
                    "kilogram is not a newton."},
            {"text": "20 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e08",
        "band": "easier",
        "text": "Which unit is weight measured in?",
        "options": [
            {"text": "Kilograms", "correct": False,
             "why": "Kilograms measure mass. Weight is a force, so it is in "
                    "newtons."},
            {"text": "Newtons", "correct": True},
            {"text": "Grams", "correct": False,
             "why": "Grams measure mass as well, just in smaller amounts."},
            {"text": "Joules", "correct": False,
             "why": "Joules measure energy, which is a different quantity "
                    "altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e09",
        "band": "easier",
        "text": "A 0.5 kg book lies on a table. What is its weight?",
        "options": [
            {"text": "5 N", "correct": True},
            {"text": "0.5 N", "correct": False,
             "why": "That is the mass with a newton after it. Multiply by "
                    "10 N/kg first."},
            {"text": "50 N", "correct": False,
             "why": "That multiplies by 100 rather than by 10 N/kg."},
            {"text": "0.05 N", "correct": False,
             "why": "That is 0.5 ÷ 10, dividing where the rule multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e10",
        "band": "easier",
        "text": "Unbalanced forces on an object mean that...",
        "options": [
            {"text": "something is left over, and the motion changes",
             "correct": True},
            {"text": "the object must already be moving quickly",
             "correct": False,
             "why": "A still object can have unbalanced forces, and it then "
                    "starts to move."},
            {"text": "a single force is acting on the object",
             "correct": False,
             "why": "Any number can be acting. What matters is that they do "
                    "not cancel."},
            {"text": "the forces are all different sizes from one another",
             "correct": False,
             "why": "Forces of different sizes can still cancel, and equal "
                    "ones need not."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e11",
        "band": "easier",
        "text": "A 7 kg box sits still on a bench. What is the upward force "
                "from the bench?",
        "options": [
            {"text": "7 N upwards", "correct": False,
             "why": "That is the mass in kilograms. Multiply by 10 N/kg to get "
                    "the force."},
            {"text": "0 N", "correct": False,
             "why": "Take the bench away and the box falls, so the bench must "
                    "be pushing."},
            {"text": "70 N upwards", "correct": True},
            {"text": "140 N upwards", "correct": False,
             "why": "That would leave 70 N over upwards, and the box would "
                    "lift off the bench."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e12",
        "band": "easier",
        "text": "A parked lorry has balanced forces acting on it. What is the "
                "resultant force?",
        "options": [
            {"text": "0 N", "correct": True},
            {"text": "The same as its weight", "correct": False,
             "why": "The weight is cancelled by the push of the road, so "
                    "nothing is left over."},
            {"text": "Half its weight", "correct": False,
             "why": "Nothing is halved. Balanced means the forces cancel "
                    "completely."},
            {"text": "It cannot be worked out", "correct": False,
             "why": "Balanced always means a resultant of 0 N, whatever the "
                    "object is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e13",
        "band": "easier",
        "text": "Which of these is a balanced situation?",
        "options": [
            {"text": "A stone gathering speed as it falls", "correct": False,
             "why": "Its speed is changing, so something is left over."},
            {"text": "A car pulling away from traffic lights",
             "correct": False,
             "why": "It is speeding up, which needs a resultant force."},
            {"text": "A ball curving through the air", "correct": False,
             "why": "Its direction is changing, which is a change of motion "
                    "like any other."},
            {"text": "A book lying still on a shelf", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e14",
        "band": "easier",
        "text": "A 900 g bag of sugar rests on a table. What is its weight?",
        "options": [
            {"text": "9 000 N", "correct": False,
             "why": "That multiplies the grams by 10. Convert to kilograms "
                    "first."},
            {"text": "900 N", "correct": False,
             "why": "That is the mass in grams with a newton written after "
                    "it."},
            {"text": "9 N", "correct": True},
            {"text": "0.9 N", "correct": False,
             "why": "That is the mass in kilograms, before the × 10 N/kg."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e15",
        "band": "easier",
        "text": "A ball gathers speed as it falls. The forces on it are...",
        "options": [
            {"text": "balanced, because it is falling steadily",
             "correct": False,
             "why": "It is not falling steadily. Its speed is rising every "
                    "second."},
            {"text": "balanced, because gravity acts on everything",
             "correct": False,
             "why": "Gravity acting is not the same as the forces cancelling."},
            {"text": "unbalanced, with more force upwards", "correct": False,
             "why": "An upward resultant would slow the fall rather than "
                    "speeding it up."},
            {"text": "unbalanced, with more force downwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e16",
        "band": "easier",
        "text": "A 3 kg mass hangs at rest from a spring. How hard is the "
                "spring pulling?",
        "options": [
            {"text": "3 N upwards", "correct": False,
             "why": "That is the mass in kilograms rather than the weight in "
                    "newtons."},
            {"text": "0 N, as nothing is moving", "correct": False,
             "why": "Cut the spring and the mass falls, so the spring was "
                    "certainly pulling."},
            {"text": "60 N upwards", "correct": False,
             "why": "That is twice the weight, and the mass would be dragged "
                    "upwards."},
            {"text": "30 N upwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e17",
        "band": "easier",
        "text": "Which of these tells you the forces on an object are "
                "unbalanced?",
        "options": [
            {"text": "It is changing speed", "correct": True},
            {"text": "It is moving quickly", "correct": False,
             "why": "Speed on its own says nothing. A steady speed means "
                    "balanced forces."},
            {"text": "It is standing still", "correct": False,
             "why": "Standing still and staying still is the most common "
                    "balanced case there is."},
            {"text": "It is heavy", "correct": False,
             "why": "Weight is only one of the forces. A heavy object can sit "
                    "in perfect balance."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e18",
        "band": "easier",
        "text": "A load is hung on a spring. What happens as the spring "
                "stretches?",
        "options": [
            {"text": "Its pull gets weaker the further it stretches",
             "correct": False,
             "why": "It pulls harder as it stretches, which is why the "
                    "stretching stops."},
            {"text": "Its pull stays the same however far it stretches",
             "correct": False,
             "why": "If the pull never changed, the spring would stretch "
                    "without ever stopping."},
            {"text": "Its pull rises until it matches the weight",
             "correct": True},
            {"text": "Its pull rises until it is twice the weight",
             "correct": False,
             "why": "It stops at equality. Twice the weight would haul the "
                    "load upwards."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e19",
        "band": "easier",
        "text": "A sheet of paper gives way at about 2 N. Which load will it "
                "hold?",
        "options": [
            {"text": "A 0.1 kg object", "correct": True},
            {"text": "A 0.5 kg object", "correct": False,
             "why": "That weighs 5 N, which is well over the 2 N limit."},
            {"text": "A 2 kg object", "correct": False,
             "why": "That weighs 20 N, ten times what the sheet can supply."},
            {"text": "A 5 kg object", "correct": False,
             "why": "That weighs 50 N and would go straight through."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e20",
        "band": "easier",
        "text": "Weight is...",
        "options": [
            {"text": "the amount of stuff in an object, in kilograms",
             "correct": False,
             "why": "That is mass. Weight is the force gravity puts on that "
                    "mass."},
            {"text": "the force of gravity on an object, in newtons",
             "correct": True},
            {"text": "how hard an object is to lift, in kilograms",
             "correct": False,
             "why": "The unit is wrong: a force is always in newtons."},
            {"text": "the space an object takes up, in centimetres",
             "correct": False,
             "why": "That is a volume, which has nothing to do with a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e21",
        "band": "easier",
        "text": "One of two identical books rests on a table and the other is "
                "falling. Which has the greater weight?",
        "options": [
            {"text": "The falling one", "correct": False,
             "why": "Moving does not change the pull of gravity on it."},
            {"text": "The resting one", "correct": False,
             "why": "The table's push is a separate force, and it does not add "
                    "to the weight."},
            {"text": "Neither: they always weigh the same", "correct": True},
            {"text": "The falling one, once it speeds up", "correct": False,
             "why": "Weight does not build up over time. It is the same the "
                    "whole way down."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e22",
        "band": "easier",
        "text": "A 1.5 kg tin rests on a shelf. How hard does the shelf push "
                "up?",
        "options": [
            {"text": "1.5 N", "correct": False,
             "why": "That is the mass in kilograms, not the weight in "
                    "newtons."},
            {"text": "0.15 N", "correct": False,
             "why": "That divides by 10 where the rule multiplies."},
            {"text": "150 N", "correct": False,
             "why": "That multiplies by 100 instead of by 10 N/kg."},
            {"text": "15 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e23",
        "band": "easier",
        "text": "An aeroplane flies straight and level at a constant speed. "
                "The forces on it are...",
        "options": [
            {"text": "unbalanced forwards, because it is moving forwards",
             "correct": False,
             "why": "Moving forwards needs no resultant. Changing its motion "
                    "would."},
            {"text": "unbalanced upwards, because it is up in the air",
             "correct": False,
             "why": "An upward resultant would make it climb, and it is "
                    "flying level."},
            {"text": "balanced", "correct": True},
            {"text": "changing all the time as it flies", "correct": False,
             "why": "Something left over would change the speed or the "
                    "direction, and neither is changing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e24",
        "band": "easier",
        "text": "A 0.2 kg apple rests on an open hand. How hard does the hand "
                "push up?",
        "options": [
            {"text": "0.2 N", "correct": False,
             "why": "That is the mass in kilograms. It still has to be "
                    "multiplied by 10 N/kg."},
            {"text": "20 N", "correct": False,
             "why": "That multiplies by 100 rather than by 10 N/kg."},
            {"text": "2 N", "correct": True},
            {"text": "0 N", "correct": False,
             "why": "Take the hand away and the apple falls, so the hand is "
                    "certainly pushing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e25",
        "band": "easier",
        "text": "A mug is sitting still on a table. What would make the "
                "forces on it unbalanced?",
        "options": [
            {"text": "Sliding the table out from under it", "correct": True},
            {"text": "Painting the table a different colour", "correct": False,
             "why": "Colour changes nothing about the forces on the mug."},
            {"text": "Moving the mug to the other end of the table",
             "correct": False,
             "why": "The table pushes up in the same way wherever the mug is "
                    "put down."},
            {"text": "Leaving the mug where it is overnight", "correct": False,
             "why": "Time changes nothing. The forces stay in balance for as "
                    "long as it sits there."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e26",
        "band": "easier",
        "text": "A crate is being lowered by a crane at a steady speed. The "
                "forces on it are...",
        "options": [
            {"text": "unbalanced downwards, because it is going down",
             "correct": False,
             "why": "Going down is not a change of motion. Speeding up or "
                    "slowing down would be."},
            {"text": "balanced", "correct": True},
            {"text": "unbalanced upwards, because a cable is holding it",
             "correct": False,
             "why": "An upward resultant would slow it, and its speed is "
                    "steady."},
            {"text": "different at each moment of the descent", "correct": False,
             "why": "A steady speed in a straight line is no change of motion, "
                    "so the forces stay in balance throughout."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e27",
        "band": "easier",
        "text": "A 40 kg child stands on a floor. What is the child's "
                "weight?",
        "options": [
            {"text": "40 N", "correct": False,
             "why": "That is the mass in kilograms with the wrong unit after "
                    "it."},
            {"text": "4 N", "correct": False,
             "why": "That is 40 ÷ 10, dividing where the rule multiplies."},
            {"text": "4 000 N", "correct": False,
             "why": "That multiplies by 100 rather than by 10 N/kg."},
            {"text": "400 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e28",
        "band": "easier",
        "text": "Why is a mass given in grams changed into kilograms before "
                "the weight is worked out?",
        "options": [
            {"text": "Because grams are an old unit no longer used",
             "correct": False,
             "why": "Grams are used constantly. They are simply not what this "
                    "rule takes."},
            {"text": "Because × 10 N/kg needs the mass in kilograms",
             "correct": True},
            {"text": "Because grams measure weight and kilograms measure mass",
             "correct": False,
             "why": "Both measure mass. Weight is measured in newtons."},
            {"text": "Because weight is worked out for heavy things alone",
             "correct": False,
             "why": "Every mass has a weight, however small it is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e29",
        "band": "easier",
        "text": "A car slows down as the brakes are applied. The forces on it "
                "are...",
        "options": [
            {"text": "balanced, because it is still moving", "correct": False,
             "why": "Its speed is falling, and a change of motion needs a "
                    "resultant."},
            {"text": "balanced, because the brakes match the engine",
             "correct": False,
             "why": "If they matched exactly the speed would stay the same, "
                    "and it is dropping."},
            {"text": "unbalanced, acting forwards", "correct": False,
             "why": "A forward resultant would speed the car up rather than "
                    "slowing it."},
            {"text": "unbalanced, acting backwards", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-e30",
        "band": "easier",
        "text": "A book is moved from a table to the floor. Which of these "
                "does NOT change?",
        "options": [
            {"text": "Its weight", "correct": True},
            {"text": "How far it is from the ceiling", "correct": False,
             "why": "That is a distance, and it plainly changes."},
            {"text": "Which surface is pushing up on it", "correct": False,
             "why": "The floor takes over from the table, so the second object "
                    "is a different one."},
            {"text": "Its height", "correct": False,
             "why": "Its height changes, though nothing about the pull of "
                    "gravity on it does."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p4-03-s07",
        "band": "standard",
        "text": "A tin of mass 750 g is left on a shelf and stays there. What "
                "upward force comes from the shelf?",
        "options": [
            {"text": "7 500 N", "correct": False,
             "why": "That multiplies the grams by 10. Convert to kilograms "
                    "first: 750 g is 0.750 kg."},
            {"text": "750 N", "correct": False,
             "why": "That is the mass in grams with a newton written after "
                    "it."},
            {"text": "0.75 N", "correct": False,
             "why": "That is the mass in kilograms, before the × 10 N/kg."},
            {"text": "7.5 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s08",
        "band": "standard",
        "text": "A 0.8 kg book is lowered onto a sheet that tears at roughly "
                "2 N. What happens to the sheet?",
        "options": [
            {"text": "The paper tears, because 8 N is more than 2 N",
             "correct": True},
            {"text": "The paper holds, because 0.8 is less than 2",
             "correct": False,
             "why": "That compares a mass with a force. The weight is "
                    "0.8 × 10 = 8 N."},
            {"text": "The paper holds, because it supplies whatever is asked "
                     "of it", "correct": False,
             "why": "Only up to its limit. Past that it cannot supply the "
                    "force and the load goes through."},
            {"text": "The paper tears, because paper holds nothing",
             "correct": False,
             "why": "A 0.1 kg load weighs 1 N and the sheet holds that "
                    "comfortably."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s09",
        "band": "standard",
        "text": "A 12 kg suitcase hangs at rest from a handle. What is the "
                "upward pull, and the resultant force?",
        "options": [
            {"text": "120 N up, and a resultant of 120 N", "correct": False,
             "why": "If 120 N were left over the case would fly upwards. At "
                    "rest the resultant is zero."},
            {"text": "12 N up, and a resultant of 0 N", "correct": False,
             "why": "12 is the mass in kilograms. The weight to be matched is "
                    "120 N."},
            {"text": "120 N up, and a resultant of 0 N", "correct": True},
            {"text": "0 N up, and a resultant of 120 N down", "correct": False,
             "why": "That is a case in free fall. This one is hanging still."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s10",
        "band": "standard",
        "text": "A skydiver's speed is still rising a few seconds after "
                "jumping. What does that say about the forces?",
        "options": [
            {"text": "They are balanced, because falling is a steady thing to "
                     "do", "correct": False,
             "why": "The speed is still changing, so something is left over."},
            {"text": "There is no air resistance until the parachute opens",
             "correct": False,
             "why": "Air resistance acts from the first moment and grows as "
                    "the speed rises."},
            {"text": "They are unbalanced, with the air resistance bigger than "
                     "the weight", "correct": False,
             "why": "That would slow the fall rather than letting it speed "
                    "up."},
            {"text": "They are unbalanced, with the weight bigger than the air "
                     "resistance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s11",
        "band": "standard",
        "text": "One train stands still in a station; an identical train runs along a straight track at a steady 30 m/s. Compare the forces acting on the two.",
        "options": [
            {"text": "Both are balanced, because neither train's motion is changing",
             "correct": True},
            {"text": "Only the standing train is balanced, since balance means staying still", "correct": False,
             "why": "Balance is about the motion not changing, and a steady 30 m/s is not changing either."},
            {"text": "Only the moving train is balanced, since its engine matches the drag on it",
             "correct": False,
             "why": "The engine does match the drag, but the standing train is in balance as well, with its weight matched by the track."},
            {"text": "Neither is balanced, because a train has an engine running in both cases", "correct": False,
             "why": "A running engine does not decide it. What matters is whether anything is left over to change the motion, and here nothing is."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s12",
        "band": "standard",
        "text": "A 2 kg load and a 4 kg load are hung in turn from the same spring. Why does the heavier load bring it to rest at a longer length?",
        "options": [
            {"text": "Because a heavier load squashes the coils together and makes the spring itself longer", "correct": False,
             "why": "Hanging a load stretches the coils apart rather than squashing them, and the spring's own length is unchanged."},
            {"text": "Because the spring must stretch further before its pull has grown to 40 N rather than 20 N", "correct": True},
            {"text": "Because the 4 kg load gets lighter as it descends, so the spring can hold it lower down",
             "correct": False,
             "why": "The weight of a load never changes on the way down; it is 40 N at the top of the stretch and 40 N at the bottom."},
            {"text": "Because the spring stops pulling once the load has settled, and a heavier load takes longer to settle", "correct": False,
             "why": "The spring pulls the whole time, on both loads. If it stopped pulling, either load would simply fall."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s13",
        "band": "standard",
        "text": "A 1.2 kg jar rests on a shelf. A student says the shelf "
                "pushes up with 1.2 N. What is the error?",
        "options": [
            {"text": "The mass was never multiplied by 10 N/kg",
             "correct": True},
            {"text": "The shelf pushes with rather more than the weight",
             "correct": False,
             "why": "A support supplies exactly what is needed, not more."},
            {"text": "The answer should be given in kilograms",
             "correct": False,
             "why": "A force is always in newtons; kilograms measure mass."},
            {"text": "The shelf does not push while the jar is still",
             "correct": False,
             "why": "Remove the shelf and the jar falls, so it was certainly "
                    "pushing."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s14",
        "band": "standard",
        "text": "A 25 kg crate is stacked on a pallet that gives way at "
                "200 N. What happens?",
        "options": [
            {"text": "It holds, because 25 is smaller than 200",
             "correct": False,
             "why": "That compares a mass with a force. The weight is 250 N."},
            {"text": "It holds, because a pallet supplies whatever is needed",
             "correct": False,
             "why": "Only up to its limit, and 250 N is past it."},
            {"text": "It goes through, because 250 N is more than 200 N",
             "correct": True},
            {"text": "It goes through, because pallets fail under any crate",
             "correct": False,
             "why": "A 15 kg crate weighs 150 N and the pallet holds that "
                    "easily."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s15",
        "band": "standard",
        "text": "A ball thrown straight up is at rest for an instant at the "
                "top of its flight. Are the forces on it balanced?",
        "options": [
            {"text": "Yes, because it is not moving at that instant",
             "correct": False,
             "why": "Being at rest is not enough. It has to be at rest and "
                    "STAYING at rest."},
            {"text": "Yes, because gravity stops at the top of a throw",
             "correct": False,
             "why": "Gravity pulls all the way up, all the way down and at the "
                    "top as well."},
            {"text": "No, because gravity never stops pulling and nothing "
                     "balances it", "correct": True},
            {"text": "No, because the ball is still travelling upwards there",
             "correct": False,
             "why": "It is not travelling at that instant. The reason is the "
                    "unbalanced pull, not the motion."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s16",
        "band": "standard",
        "text": "A 300 g phone lies on a desk. What is the upward push from "
                "the desk?",
        "options": [
            {"text": "3 000 N", "correct": False,
             "why": "That multiplies the grams by 10 instead of converting "
                    "first."},
            {"text": "300 N", "correct": False,
             "why": "That is the mass in grams with a newton written after "
                    "it."},
            {"text": "3 N", "correct": True},
            {"text": "0.3 N", "correct": False,
             "why": "That is the mass in kilograms, before the × 10 N/kg."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s17",
        "band": "standard",
        "text": "Why does a table hold a 5 N object with 5 N and a 50 N "
                "object with 50 N?",
        "options": [
            {"text": "Because it is squashed further by the heavier load until "
                     "its push matches", "correct": True},
            {"text": "Because tables are manufactured to suit the objects put "
                     "on them", "correct": False,
             "why": "The same table does it for a mug, a brick or a plant. "
                    "Nothing was made to suit them."},
            {"text": "Because the table shares its push out between whatever "
                     "is on it", "correct": False,
             "why": "There is nothing to share. Each load gets its own push, "
                    "of exactly its own size."},
            {"text": "Because the table pushes with a fixed amount, and the "
                     "rest is friction", "correct": False,
             "why": "A fixed push would fling the lighter object off. Friction "
                    "acts sideways, not upwards."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s18",
        "band": "standard",
        "text": "A 0.6 kg mug hangs from a hook and does not move. How hard "
                "does the hook pull?",
        "options": [
            {"text": "0.6 N", "correct": False,
             "why": "That is the mass in kilograms rather than the weight in "
                    "newtons."},
            {"text": "60 N", "correct": False,
             "why": "That multiplies by 100 instead of by 10 N/kg."},
            {"text": "0 N", "correct": False,
             "why": "Unhook the mug and it falls, so the hook was certainly "
                    "pulling."},
            {"text": "6 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s19",
        "band": "standard",
        "text": "A cyclist stops pedalling on a flat road and gradually slows "
                "down. What is true of the forces?",
        "options": [
            {"text": "They are balanced, because the cyclist is still moving",
             "correct": False,
             "why": "The speed is dropping, and a change of motion needs a "
                    "resultant."},
            {"text": "They are unbalanced, acting backwards", "correct": True},
            {"text": "There are no forces left once the pedalling stops",
             "correct": False,
             "why": "Friction and air resistance carry on acting, which is "
                    "exactly why the bicycle slows."},
            {"text": "They are unbalanced, acting forwards", "correct": False,
             "why": "A forward resultant would make the cyclist speed up."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s20",
        "band": "standard",
        "text": "A 4 kg box rests on a table. Someone then presses down on "
                "the box with an extra 20 N. What does the table push up "
                "with?",
        "options": [
            {"text": "40 N, which is the weight of the box on its own", "correct": False,
             "why": "The press goes through the box into the table, and the "
                    "table answers all of it."},
            {"text": "20 N", "correct": False,
             "why": "The weight of the box is still there as well and still "
                    "has to be matched."},
            {"text": "60 N", "correct": True},
            {"text": "0 N, as the box is still not moving", "correct": False,
             "why": "Not moving is what balance looks like, and balance needs "
                    "a push from the table."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s21",
        "band": "standard",
        "text": "Why is 'the object is not moving' not quite enough to say "
                "the forces on it are balanced?",
        "options": [
            {"text": "Because a heavy object can be still without any support",
             "correct": False,
             "why": "Nothing stays still in mid-air with no support, however "
                    "heavy it is."},
            {"text": "Because balance is about direction rather than about "
                     "motion", "correct": False,
             "why": "Balance is about whether the motion CHANGES, and "
                    "direction is part of the motion."},
            {"text": "Because a still object has no forces acting on it",
             "correct": False,
             "why": "It usually has several, and they cancel. That is what "
                    "balance is."},
            {"text": "Because an object can be at rest for an instant with the "
                     "forces unbalanced", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s22",
        "band": "standard",
        "text": "A 2.5 kg tin hangs at rest from a spring balance. What does "
                "the balance read?",
        "options": [
            {"text": "2.5 N", "correct": False,
             "why": "That is the mass in kilograms rather than the weight it "
                    "is holding."},
            {"text": "25 N", "correct": True},
            {"text": "250 N", "correct": False,
             "why": "That multiplies by 100 instead of by 10 N/kg."},
            {"text": "0.25 N", "correct": False,
             "why": "That divides by 10 where the rule multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s23",
        "band": "standard",
        "text": "A lift is travelling downwards at a constant speed. What is "
                "the resultant force on it?",
        "options": [
            {"text": "Equal to its weight, downwards", "correct": False,
             "why": "That is a lift in free fall. This one is moving at a "
                    "steady speed."},
            {"text": "0 N", "correct": True},
            {"text": "Equal to the cable's pull, upwards", "correct": False,
             "why": "The cable's pull is cancelled by the weight, so nothing "
                    "is left over."},
            {"text": "Small and downwards, because it is going down",
             "correct": False,
             "why": "Going down at a steady speed is no change of motion at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s24",
        "band": "standard",
        "text": "A 150 g mouse sits still on a shelf. What is the upward "
                "force on it?",
        "options": [
            {"text": "1 500 N", "correct": False,
             "why": "That multiplies the grams by 10 without converting."},
            {"text": "150 N", "correct": False,
             "why": "That is the mass in grams with a newton written after "
                    "it."},
            {"text": "0.15 N", "correct": False,
             "why": "That is the mass in kilograms, before the × 10 N/kg."},
            {"text": "1.5 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s25",
        "band": "standard",
        "text": "A rope rated to pull with up to 400 N is used to hang a "
                "30 kg load at rest. Is that safe?",
        "options": [
            {"text": "No, because 400 is bigger than 30", "correct": False,
             "why": "That compares a force with a mass. The weight to be held "
                    "is 300 N."},
            {"text": "Yes, because a rope pulls with whatever is asked of it",
             "correct": False,
             "why": "It is safe here, but not for that reason: past 400 N the "
                    "rope cannot supply what is needed."},
            {"text": "No, because a rope at rest is always at its limit",
             "correct": False,
             "why": "At rest it supplies only the weight, which here is well "
                    "inside its rating."},
            {"text": "Yes, because the weight is only 300 N and the rope can "
                     "supply 400 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s26",
        "band": "standard",
        "text": "What is the difference between the mass of an object and its "
                "weight?",
        "options": [
            {"text": "Mass is in kilograms; weight is the force of gravity, in "
                     "newtons", "correct": True},
            {"text": "Mass is what a heavy thing has; weight is what a light "
                     "thing has", "correct": False,
             "why": "Every object has both, whatever size it is."},
            {"text": "Mass is measured on Earth; weight is measured in space",
             "correct": False,
             "why": "Both are measured anywhere. They are different "
                    "quantities, not different places."},
            {"text": "Mass is the same as weight, written in a different unit",
             "correct": False,
             "why": "They are different quantities: one is an amount of "
                    "matter, the other is a force."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s27",
        "band": "standard",
        "text": "A student says an object standing still has no forces on it. "
                "Which observation disproves that?",
        "options": [
            {"text": "A still object can be picked up and moved",
             "correct": False,
             "why": "Picking it up adds a new force; it says nothing about "
                    "what was acting before."},
            {"text": "A rope holding a still load can snap", "correct": True},
            {"text": "A still object gets warmer if it is left in the sun",
             "correct": False,
             "why": "Warming is about energy arriving, not about the forces on "
                    "the object."},
            {"text": "A still object can be seen and touched", "correct": False,
             "why": "Being visible has nothing to do with whether forces are "
                    "acting on it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s28",
        "band": "standard",
        "text": "A box slides across a floor and gradually comes to a stop. "
                "What is true of the forces along its line of travel?",
        "options": [
            {"text": "They are balanced, which is why it ends up still",
             "correct": False,
             "why": "It only ends up still because its speed changed, and that "
                    "needs a resultant."},
            {"text": "They are unbalanced, acting against the motion",
             "correct": True},
            {"text": "They are unbalanced, acting along the motion",
             "correct": False,
             "why": "A resultant along the motion would speed the box up."},
            {"text": "There are none, because nothing is pushing it now",
             "correct": False,
             "why": "Friction from the floor pushes on it the whole time it is "
                    "sliding."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s29",
        "band": "standard",
        "text": "A sheet fails at roughly 2 N. Will it take a 0.05 kg ball "
                "placed gently on top?",
        "options": [
            {"text": "It goes through, because paper cannot hold a ball",
             "correct": False,
             "why": "The sheet holds anything weighing under about 2 N, ball "
                    "or not."},
            {"text": "It holds, because paper always supplies what is asked",
             "correct": False,
             "why": "It holds here, but only because the load is inside the "
                    "sheet's limit."},
            {"text": "It goes through, because 0.05 is less than 2",
             "correct": False,
             "why": "That compares a mass with a force, and it gets the "
                    "verdict the wrong way round as well."},
            {"text": "It holds, because 0.5 N is well under 2 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-s30",
        "band": "standard",
        "text": "A 20 kg bag hangs from a cable that pulls up with 200 N. "
                "What is the resultant, and what is the bag doing?",
        "options": [
            {"text": "200 N upwards, and the bag is rising", "correct": False,
             "why": "The weight of 200 N cancels the pull, so nothing is left "
                    "over to lift it."},
            {"text": "0 N, and the bag stays where it is", "correct": True},
            {"text": "200 N downwards, and the bag is falling",
             "correct": False,
             "why": "That is a bag with nothing holding it. The cable is "
                    "supplying 200 N."},
            {"text": "400 N upwards, and the bag is rising", "correct": False,
             "why": "The two forces oppose each other, so they subtract rather "
                    "than adding."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p4-03-h07",
        "band": "harder",
        "text": "A 60 kg diver stands still on a board rated to hold 800 N. "
                "How much spare capacity has the board?",
        "options": [
            {"text": "740 N", "correct": False,
             "why": "A mass in kilograms cannot be taken away from a force in "
                    "newtons."},
            {"text": "800 N", "correct": False,
             "why": "It is already supplying 600 N to hold the diver up, so "
                    "not all of it is spare."},
            {"text": "None", "correct": False,
             "why": "At rest it supplies only the 600 N weight, which is well "
                    "inside the rating."},
            {"text": "200 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h08",
        "band": "harder",
        "text": "A 1 200 kg lift hangs at rest from a cable that fails at "
                "15 000 N. How much spare pull has the cable?",
        "options": [
            {"text": "13 800 N", "correct": False,
             "why": "1 200 is a mass in kilograms and cannot be subtracted "
                    "from a force."},
            {"text": "15 000 N", "correct": False,
             "why": "At rest it is already pulling with the full 12 000 N "
                    "weight."},
            {"text": "3 000 N", "correct": True},
            {"text": "None to spare", "correct": False,
             "why": "It supplies 12 000 N at rest, which leaves a real margin "
                    "below the failure load."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h09",
        "band": "harder",
        "text": "A parachutist falls at a steady speed, then pulls the canopy "
                "in a little and the fall speeds up. What changed?",
        "options": [
            {"text": "The weight rose, because the fall got faster",
             "correct": False,
             "why": "Weight does not change with speed. It is the upward force "
                    "that fell."},
            {"text": "The upward force fell below the weight, so the forces "
                     "became unbalanced", "correct": True},
            {"text": "The upward force rose above the weight, which is what "
                     "made the fall quicken", "correct": False,
             "why": "An upward resultant would slow the fall rather than "
                    "speeding it up."},
            {"text": "Nothing changed: the forces stayed balanced all the way "
                     "down", "correct": False,
             "why": "A change of speed cannot happen with balanced forces."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h10",
        "band": "harder",
        "text": "Why is the upward force from a table EXACTLY the weight of "
                "what is on it, rather than a little more?",
        "options": [
            {"text": "Because a table is built to push with the weight of an "
                     "average object", "correct": False,
             "why": "The same table does it for anything put on it, whatever "
                    "the weight."},
            {"text": "Because the surface stops squashing at the point where "
                     "the two are equal", "correct": True},
            {"text": "Because the extra push leaks away into the floor below "
                     "the table", "correct": False,
             "why": "There is no extra push to leak. The squashing settles at "
                    "equality."},
            {"text": "Because a table can only ever supply a small amount of "
                     "force", "correct": False,
             "why": "A table supplies whatever is needed until it breaks, "
                    "which can be a great deal."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h11",
        "band": "harder",
        "text": "A student says a bridge is designed to be strong. How would "
                "an engineer put it more precisely?",
        "options": [
            {"text": "It is designed so nothing at all presses down on it",
             "correct": False,
             "why": "Every bridge carries loads all day. That is what it is "
                    "for."},
            {"text": "It is designed so it can push back with more than any "
                     "load ever presses", "correct": False,
             "why": "A support supplies exactly what is needed; pushing harder "
                    "would raise the load."},
            {"text": "It is designed so the resultant force on it is always "
                     "upwards", "correct": False,
             "why": "An upward resultant would lift the bridge off its "
                    "supports."},
            {"text": "It is designed so the heaviest expected load still "
                     "leaves it in balance, with a margin", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h12",
        "band": "harder",
        "text": "Cards of 0.08 kg each are stacked on a sheet of paper that "
                "gives way at about 2 N. How many will it hold?",
        "options": [
            {"text": "Two", "correct": True},
            {"text": "Three", "correct": False,
             "why": "Three cards weigh 2.4 N, not 0.24 N, and that is past the "
                    "limit."},
            {"text": "None", "correct": False,
             "why": "One card weighs 0.8 N, comfortably inside the sheet's "
                    "limit."},
            {"text": "Twenty-five", "correct": False,
             "why": "That divides the force by a mass. Each card weighs 0.8 N, "
                    "so only two fit inside 2 N."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h13",
        "band": "harder",
        "text": "A lift rises at a constant speed. A student says the cable "
                "must be pulling harder than the weight. Is that right?",
        "options": [
            {"text": "Yes, or the lift could not be going upwards",
             "correct": False,
             "why": "Going up needs no resultant; starting to go up did, and "
                    "that moment has passed."},
            {"text": "Yes, because moving always needs a resultant force",
             "correct": False,
             "why": "Moving steadily needs none. Changing the motion is what "
                    "needs one."},
            {"text": "No, because at a constant speed the forces are always "
                     "balanced and the pull equals the weight", "correct": True},
            {"text": "No, because the cable's pull is always less than the "
                     "weight while the lift moves", "correct": False,
             "why": "A smaller pull would leave a downward resultant and the "
                    "lift would slow."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h14",
        "band": "harder",
        "text": "A 15 kg load hangs at rest from a spring, which has "
                "stretched by 6 cm. How hard is the spring pulling?",
        "options": [
            {"text": "6 N", "correct": False,
             "why": "A length in centimetres is not a force. The stretch is "
                    "not what is being asked for."},
            {"text": "90 N", "correct": False,
             "why": "The stretch plays no part in the sum. The pull matches "
                    "the weight."},
            {"text": "15 N", "correct": False,
             "why": "That is the mass in kilograms rather than the weight in "
                    "newtons."},
            {"text": "150 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h15",
        "band": "harder",
        "text": "Two identical crates: one at rest on a floor, one sliding "
                "across it at a steady speed. Compare the upward forces from "
                "the floor.",
        "options": [
            {"text": "The sliding crate gets more, because it moves",
             "correct": False,
             "why": "Sideways motion does not change the vertical balance."},
            {"text": "The resting crate gets a bigger push, because it presses "
                     "down for longer", "correct": False,
             "why": "How long a load sits there changes nothing about how hard "
                    "the floor pushes."},
            {"text": "The floor pushes up with the same force on both",
             "correct": True},
            {"text": "The sliding crate gets no upward push, because friction "
                     "takes its place", "correct": False,
             "why": "Friction acts along the floor. The upward push is still "
                    "there, matching the weight."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h16",
        "band": "harder",
        "text": "Why can a resultant of 0 N and no forces at all not be told "
                "apart just by watching an object?",
        "options": [
            {"text": "Because in both cases nothing about the motion changes",
             "correct": True},
            {"text": "Because a resultant of 0 N means the forces really have "
                     "gone", "correct": False,
             "why": "They are still acting, and a rope under tension can snap "
                    "to prove it."},
            {"text": "Because both cases leave the object with no weight at all",
             "correct": False,
             "why": "The object has its weight in both cases. A resultant of "
                    "0 N means the weight is cancelled, not removed."},
            {"text": "Because forces are invisible and cannot be detected",
             "correct": False,
             "why": "They are detected constantly, with a newtonmeter or by "
                    "what they break."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h17",
        "band": "harder",
        "text": "A 900 kg car stands on a level road. What is the total "
                "upward force the road gives the tyres?",
        "options": [
            {"text": "900 N", "correct": False,
             "why": "That is the mass in kilograms rather than the weight in "
                    "newtons."},
            {"text": "2 250 N, a quarter of the weight for each tyre",
             "correct": False,
             "why": "That is the share on one tyre, and the question asks for "
                    "the total."},
            {"text": "9 000 N", "correct": True},
            {"text": "0 N, because the car is not moving", "correct": False,
             "why": "Not moving is what balance looks like, and balance needs "
                    "the road to push."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h18",
        "band": "harder",
        "text": "A 0.25 kg mass hangs at rest on a spring. Another 0.25 kg is "
                "added. What is the spring's pull once everything is still "
                "again?",
        "options": [
            {"text": "It stays at 2.5 N, because the spring has not changed",
             "correct": False,
             "why": "The spring stretches further and pulls harder until it "
                    "matches the new weight."},
            {"text": "It rises from 2.5 N to 5 N", "correct": True},
            {"text": "It rises from 0.25 N to 0.5 N", "correct": False,
             "why": "Those are masses in kilograms. Each 0.25 kg weighs "
                    "2.5 N."},
            {"text": "It rises from 2.5 N to 25 N", "correct": False,
             "why": "The load has doubled, not gone up ten times."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h19",
        "band": "harder",
        "text": "A shelf is holding a 3 kg box in balance. A 2 kg box is put "
                "on top. What is the shelf's push now, and what has the shelf "
                "done?",
        "options": [
            {"text": "50 N, and it has squashed a little further",
             "correct": True},
            {"text": "30 N, and it has done nothing different", "correct": False,
             "why": "The load is now 50 N, so the push has to rise to match "
                    "it."},
            {"text": "5 N, and it has squashed a little further",
             "correct": False,
             "why": "5 is the total mass in kilograms. The weight is 50 N."},
            {"text": "50 N, and it has become stiffer to take the extra load",
             "correct": False,
             "why": "The shelf's stiffness is unchanged. It simply squashes "
                    "further and so pushes harder."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h20",
        "band": "harder",
        "text": "A skydiver falling at a steady speed opens the parachute. "
                "What is true in the moments straight afterwards?",
        "options": [
            {"text": "The forces stay balanced, so nothing about the speed of the fall changes once the canopy opens", "correct": False,
             "why": "The fall slows sharply, and a change of motion needs a "
                    "resultant."},
            {"text": "The upward force is bigger than the weight, so the "
                     "forces are unbalanced upwards", "correct": True},
            {"text": "The weight rises sharply, which is what slows the "
                     "skydiver", "correct": False,
             "why": "Weight is unchanged by the canopy. It is the upward force "
                    "that jumps."},
            {"text": "The upward force becomes bigger than the weight, so the "
                     "skydiver starts travelling back up towards the plane",
             "correct": False,
             "why": "The fall slows but continues downwards; slowing is not "
                    "the same as going back up."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h21",
        "band": "harder",
        "text": "A 320 kg pallet of bricks is to hang at rest from a hoist chain rated to pull with up to 3 000 N. Is that safe?",
        "options": [
            {"text": "Yes, because 3 000 N is more than 320 kg",
             "correct": False,
             "why": "A force cannot be compared with a mass. The weight is 3 200 N."},
            {"text": "Yes, because a chain at rest hardly pulls",
             "correct": False,
             "why": "At rest it has to supply the whole weight, which is 3 200 N."},
            {"text": "No, because the weight is 3 200 N and the chain can only give 3 000 N", "correct": True},
            {"text": "No, because a chain must be rated at twice the weight of anything it lifts", "correct": False,
             "why": "There is no such rule here. It fails simply because it "
                    "cannot supply what is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h22",
        "band": "harder",
        "text": "A student takes a mass in grams and multiplies it straight "
                "by 10 N/kg. Why does the answer come out a thousand times "
                "too big?",
        "options": [
            {"text": "Because the rule needs kilograms, and a gram is a "
                     "thousandth of one", "correct": True},
            {"text": "Because grams have to be multiplied by 10 twice over",
             "correct": False,
             "why": "Nothing is multiplied twice. The mass simply has to be "
                    "converted first."},
            {"text": "Because 10 N/kg becomes 10 000 N/g when grams are used",
             "correct": False,
             "why": "The field strength does not change with the unit chosen "
                    "for the mass."},
            {"text": "Because grams measure weight already, so the rule is not "
                     "needed", "correct": False,
             "why": "Grams measure mass, and the weight still has to be worked "
                    "out from it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h23",
        "band": "harder",
        "text": "A sheet of ice holds a 40 kg skater but gives way under a "
                "70 kg one. Roughly what force can it supply?",
        "options": [
            {"text": "Between 40 N and 70 N", "correct": False,
             "why": "Those are masses in kilograms. Their weights are 400 N "
                    "and 700 N."},
            {"text": "Exactly 700 N, the weight it failed under",
             "correct": False,
             "why": "It failed somewhere below 700 N, so that is an upper "
                    "limit rather than the answer."},
            {"text": "Less than 400 N, since it gave way in the end",
             "correct": False,
             "why": "It held 400 N successfully, so its limit is above that."},
            {"text": "Between 400 N and 700 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h24",
        "band": "harder",
        "text": "A helicopter hovers at a fixed height above a field. What is "
                "true of the vertical forces on it?",
        "options": [
            {"text": "They are unbalanced upwards, or it would come down",
             "correct": False,
             "why": "An upward resultant would make it climb, and its height "
                    "is fixed."},
            {"text": "They are unbalanced downwards", "correct": False,
             "why": "A downward resultant would bring it down, and it is "
                    "holding its height."},
            {"text": "Only its weight acts, because nothing is holding it up",
             "correct": False,
             "why": "The air it drives downwards pushes back up on it the "
                    "whole time."},
            {"text": "They are balanced, so the resultant is 0 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h25",
        "band": "harder",
        "text": "A crane lowers a girder at a steady speed and then slows it "
                "to a stop. Compare the forces in the two stages.",
        "options": [
            {"text": "Balanced while the speed is steady, then unbalanced "
                     "upwards while it slows", "correct": True},
            {"text": "Unbalanced downwards throughout, because the girder is "
                     "going down the whole time", "correct": False,
             "why": "Going down is not a change of motion. Only the slowing "
                    "stage needs a resultant."},
            {"text": "Balanced in both stages, because the cable never lets "
                     "go", "correct": False,
             "why": "Slowing down is a change of motion, and that cannot "
                    "happen with balanced forces."},
            {"text": "Unbalanced upwards throughout, because the cable is "
                     "holding the girder up", "correct": False,
             "why": "At a steady speed the cable's pull exactly matches the "
                    "weight, leaving nothing over."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h26",
        "band": "harder",
        "text": "One student says an object's mass is 4 kg; another says its "
                "weight is 4 kg. Who is wrong, and why?",
        "options": [
            {"text": "The second: weight is a force, so it is 40 N",
             "correct": True},
            {"text": "The first: mass should have been given in newtons "
                     "instead", "correct": False,
             "why": "Mass is measured in kilograms, so the first statement is "
                    "fine as it stands."},
            {"text": "Both: mass and weight are each measured in grams",
             "correct": False,
             "why": "Mass is in kilograms or grams and weight is in newtons, "
                    "so neither is in grams here."},
            {"text": "Neither: 4 kg and 4 kg describe the same thing twice "
                     "over", "correct": False,
             "why": "They are different quantities, and weight is never "
                    "measured in kilograms."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h27",
        "band": "harder",
        "text": "A 250 kg load hangs at rest from two cables, and each takes "
                "half of it. How hard does each cable pull?",
        "options": [
            {"text": "125 N", "correct": False,
             "why": "That halves the mass in kilograms rather than the weight "
                    "in newtons."},
            {"text": "2 500 N", "correct": False,
             "why": "Each takes half, and together they supply the 2 500 N "
                    "weight."},
            {"text": "1 250 N", "correct": True},
            {"text": "250 N", "correct": False,
             "why": "That is the mass in kilograms, with the wrong unit after "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h28",
        "band": "harder",
        "text": "A 10 kg table stands on a floor with a 2 kg book left on top "
                "of it. What upward force does the floor supply?",
        "options": [
            {"text": "100 N", "correct": False,
             "why": "The book's weight passes through the table, so the floor "
                    "has to take that as well."},
            {"text": "12 N", "correct": False,
             "why": "That is the total mass in kilograms rather than the "
                    "weight in newtons."},
            {"text": "20 N", "correct": False,
             "why": "The table's own weight is there too and also has to be "
                    "matched."},
            {"text": "120 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h29",
        "band": "harder",
        "text": "Why is 'at rest' not quite the same as 'at rest and staying "
                "at rest'?",
        "options": [
            {"text": "Because an object can be at rest for an instant with "
                     "unbalanced forces on it", "correct": True},
            {"text": "Because an object at rest always has unbalanced forces "
                     "acting on it", "correct": False,
             "why": "Most objects at rest are in perfect balance — a book on a "
                    "shelf, for instance."},
            {"text": "Because staying at rest means no forces act, while being "
                     "at rest means some do", "correct": False,
             "why": "Forces act in both cases; what differs is whether they "
                    "cancel."},
            {"text": "Because an object at rest has already stopped moving for "
                     "good", "correct": False,
             "why": "Plenty of objects at rest start moving a moment later, "
                    "which is exactly what the phrase is guarding against."},
        ],
        "figure": None,
    },
    {
        "id": "p4-03-h30",
        "band": "harder",
        "text": "A shelf gives way at 50 N and is holding a 4 kg box. A "
                "1.5 kg tin is put on top. What happens?",
        "options": [
            {"text": "It holds, because 5.5 kg is less than 50", "correct": False,
             "why": "That compares a mass with a force. The load is now 55 N."},
            {"text": "It gives way, because 55 N is more than 50 N",
             "correct": True},
            {"text": "It holds, because the shelf supplies whatever is asked "
                     "of it", "correct": False,
             "why": "Only up to its limit, and 55 N is past it."},
            {"text": "It gives way, because any extra load breaks a shelf that "
                     "is already loaded", "correct": False,
             "why": "The box alone weighs 40 N, so the shelf could have taken "
                    "another 10 N without trouble."},
        ],
        "figure": None,
    },
]
