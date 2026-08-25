"""P12 lesson 02 — Mass vs weight: twelve questions (MRB-223).

Written against Design's page. The hammer on the Moon, the two columns and
both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · which instrument reads which quantity — a pan balance compares masses,
    a spring balance measures a force (`SPACE-07`);
  · mass is also RELUCTANCE TO BE MOVED, which is why the hammer is no
    easier to swing (`SPACE-06`);
  · newtons and kilograms are not two units for one quantity, because the
    number between them is not fixed (`SPACE-05`);
  · weightless is not massless, and a loose crate in orbit is the proof
    (`SPACE-04`). The harder band sits here.

⚠️ POSITION IS AUTHORED — 0,2,1,3 · 3,1,2,0 · 1,0,3,2, three of each.

⚠️ Neither marked rung is restated: the 45 N spring balance and the hammer
on the Moon are the ladder's. Nor is a worked example reused — the 32 N
Moon reading, the 750 g tin and the 900 g Mars sample are all off limits.
"""

UNIT = "P12"
LESSON = "mass-vs-weight"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-02-e01",
        "band": "easier",
        "text": "Which quantity is the same everywhere in the universe?",
        "options": [
            {"text": "Mass", "correct": True},
            {"text": "Weight", "correct": False,
             "why": "Weight is the pull of gravity, and gravity is stronger "
                    "in some places than others."},
            {"text": "Both mass and weight", "correct": False,
             "why": "Only one of them travels unchanged. The other belongs to "
                    "the object and the place together."},
            {"text": "Neither — everything about an object changes when it "
                     "moves", "correct": False,
             "why": "The amount of matter in an object does not change when "
                    "you carry it somewhere."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e02",
        "band": "easier",
        "text": "Which instrument measures a force?",
        "options": [
            {"text": "A pan balance", "correct": False,
             "why": "A pan balance compares an unknown mass against known "
                    "masses. It never reports a force."},
            {"text": "A measuring cylinder", "correct": False,
             "why": "A measuring cylinder gives a volume in cubic "
                    "centimetres."},
            {"text": "A spring balance", "correct": True},
            {"text": "A thermometer", "correct": False,
             "why": "A thermometer gives a temperature in degrees Celsius."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e03",
        "band": "easier",
        "text": "A 3 kg bag of potatoes is taken to Jupiter, where g = "
                "24.8 N/kg. What is its mass there?",
        "options": [
            {"text": "74.4 kg", "correct": False,
             "why": "That is the WEIGHT in newtons, worked out correctly and "
                    "then given the wrong unit."},
            {"text": "3 kg", "correct": True},
            {"text": "0.12 kg", "correct": False,
             "why": "Dividing the mass by the field strength is not something "
                    "the formula ever asks for, and mass does not change "
                    "anyway."},
            {"text": "30 kg", "correct": False,
             "why": "That is the Earth weight in newtons with the wrong unit "
                    "on it. The mass is unchanged at 3 kg."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e04",
        "band": "easier",
        "text": "What does a pan balance actually compare?",
        "options": [
            {"text": "How hard gravity pulls on each side", "correct": False,
             "why": "Gravity does act on both sides, and that is why the "
                    "comparison works anywhere: the pull cancels out of the "
                    "answer."},
            {"text": "How much space each side takes up", "correct": False,
             "why": "That is volume. Two objects of the same volume can have "
                    "very different masses."},
            {"text": "How fast each side falls", "correct": False,
             "why": "Both sides fall at the same rate, on Earth or anywhere "
                    "else, so that could never tell them apart."},
            {"text": "An unknown mass against known masses", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-02-s01",
        "band": "standard",
        "text": "A crate weighs 1240 N on Jupiter, where g = 24.8 N/kg. What "
                "would it weigh on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "1240 N", "correct": False,
             "why": "Weight changes with field strength. Only the mass "
                    "survives the journey unchanged."},
            {"text": "12 400 N", "correct": False,
             "why": "That multiplies the Jupiter WEIGHT by 10. The 10 N/kg "
                    "multiplies a MASS, so divide by 24.8 first."},
            {"text": "30 752 N", "correct": False,
             "why": "That multiplies the weight by Jupiter's own field "
                    "strength, which uses the same number twice."},
            {"text": "500 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s02",
        "band": "standard",
        "text": "Why is a trolley just as hard to get moving on the Moon as "
                "it is on Earth?",
        "options": [
            {"text": "Because the Moon has no air to slow it down",
             "correct": False,
             "why": "Air resistance on a slow trolley is negligible either "
                    "way, and losing it would make things easier rather than "
                    "the same."},
            {"text": "Because getting something moving depends on its mass, "
                     "which has not changed", "correct": True},
            {"text": "Because the Moon's weaker gravity is cancelled out by "
                     "its smaller size", "correct": False,
             "why": "Nothing cancels. The Moon's field really is about a "
                    "sixth of the Earth's, and lifting the trolley really is "
                    "easier."},
            {"text": "Because friction with the ground is higher on the Moon",
             "correct": False,
             "why": "Friction is lower there, because the trolley presses "
                    "down with about a sixth of the force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s03",
        "band": "standard",
        "text": "An object has a mass of 4 kg. Which row is correct for the "
                "Moon, where g = 1.6 N/kg?",
        "options": [
            {"text": "mass 0.64 kg · weight 4 N", "correct": False,
             "why": "The mass has been changed and the weight has not been "
                    "calculated. Mass stays at 4 kg wherever the object "
                    "goes."},
            {"text": "mass 4 N · weight 6.4 kg", "correct": False,
             "why": "The units have been swapped. Mass takes kilograms and "
                    "weight takes newtons."},
            {"text": "mass 4 kg · weight 6.4 N", "correct": True},
            {"text": "mass 4 kg · weight 40 N", "correct": False,
             "why": "40 N is the Earth weight. On the Moon each kilogram is "
                    "pulled with 1.6 N, not 10 N."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s04",
        "band": "standard",
        "text": "A market trader's spring balance is calibrated on Earth and "
                "reads in kilograms. It is taken to a mining base on Mars, "
                "where g = 3.7 N/kg. What happens to its readings?",
        "options": [
            {"text": "Every reading is about a third of the true mass",
             "correct": True},
            {"text": "Every reading is about three times the true mass",
             "correct": False,
             "why": "The pull on Mars is weaker, so the spring stretches "
                    "less and the reading falls rather than rises."},
            {"text": "The readings are correct, because the spring is "
                     "unaffected by gravity", "correct": False,
             "why": "The spring stretches because gravity pulls on the load. "
                    "Weaken the pull and the stretch changes."},
            {"text": "The readings are correct, because kilograms are the "
                     "same everywhere", "correct": False,
             "why": "Kilograms are the same everywhere. The instrument's way "
                    "of arriving at them is not — it divides a force by "
                    "Earth's field strength."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-02-h01",
        "band": "harder",
        "text": "Why is it wrong to say that kilograms and newtons are two "
                "units for the same quantity, like metres and feet?",
        "options": [
            {"text": "Because newtons are much larger than kilograms",
             "correct": False,
             "why": "Size is not the issue. A metre is larger than a foot and "
                    "they still measure the same quantity."},
            {"text": "Because the number connecting them is a property of the "
                     "place, not a fixed conversion", "correct": True},
            {"text": "Because kilograms are used by scientists and newtons "
                     "are used in everyday life", "correct": False,
             "why": "It is the other way round in ordinary speech, and in any "
                    "case who uses a unit says nothing about what it "
                    "measures."},
            {"text": "Because newtons only apply to objects that are moving",
             "correct": False,
             "why": "A book resting on a table has a weight in newtons and is "
                    "not moving at all."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h02",
        "band": "harder",
        "text": "A supply crate floats free inside an orbiting station and "
                "drifts slowly towards an astronaut. Why is that dangerous?",
        "options": [
            {"text": "Because the crate still has all its mass, so stopping "
                     "it takes the full force its mass demands", "correct": True},
            {"text": "Because objects in orbit gain speed continuously until "
                     "something stops them, so any drifting object is always "
                     "accelerating", "correct": False,
             "why": "A drifting crate keeps the speed it was given. Nothing "
                    "inside the station is speeding it up."},
            {"text": "Because the crate's weight returns the moment it "
                     "touches something", "correct": False,
             "why": "Weight is the pull of gravity, and it does not switch "
                    "on at contact. What hurts is the crate's mass having to "
                    "be stopped."},
            {"text": "Because there is no air in the station to slow it down",
             "correct": False,
             "why": "The station is full of air, and air would barely slow a "
                    "crate anyway."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h03",
        "band": "harder",
        "text": "An astronaut needs to compare two rock samples on the Moon "
                "and find out which has the greater MASS. Which method works "
                "and why?",
        "options": [
            {"text": "A spring balance, because it reads directly in "
                     "kilograms", "correct": False,
             "why": "It reads in kilograms only because it was calibrated on "
                    "Earth. On the Moon that conversion is the wrong one."},
            {"text": "Neither method works, because mass cannot be measured "
                     "away from the Earth", "correct": False,
             "why": "A pan balance works perfectly well anywhere there is a "
                    "gravitational field, because the field cancels out of "
                    "the comparison."},
            {"text": "A spring balance, because the Moon's field strength is "
                     "known and can be corrected for", "correct": False,
             "why": "That would give a right answer for a wrong reason: the "
                    "question asks which is GREATER, and a pan balance "
                    "answers it with no correction at all."},
            {"text": "A pan balance, because gravity acts equally on both "
                     "sides and drops out of the comparison", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h04",
        "band": "harder",
        "text": "A 2 kg object is weighed on four worlds and the readings "
                "are 3.2 N, 7.4 N, 20 N and 49.6 N. Which world has the "
                "strongest gravitational field, and what is its g?",
        "options": [
            {"text": "The 3.2 N world, at 1.6 N/kg", "correct": False,
             "why": "That is the weakest of the four. The strongest field "
                    "gives the largest pull on the same mass."},
            {"text": "The 20 N world, at 10 N/kg", "correct": False,
             "why": "That is Earth, and one of the four pulls harder than "
                    "Earth does."},
            {"text": "The 49.6 N world, at 24.8 N/kg", "correct": True},
            {"text": "The 49.6 N world, at 99.2 N/kg", "correct": False,
             "why": "The world is right and the arithmetic is inverted. Cover "
                    "g on the triangle and W sits over m, so divide 49.6 by "
                    "2."},
        ],
        "figure": None,
    },
]
