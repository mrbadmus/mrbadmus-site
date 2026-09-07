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
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Every reading is about a third of the true mass — "
                     "g is 3.7", "correct": True},
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
            {"text": "Because a newton is a much larger unit than a "
                     "kilogram", "correct": False,
             "why": "Size is not the issue. A metre is larger than a foot and "
                    "they still measure the same quantity."},
            {"text": "Because the number connecting them is a property of the "
                     "place, not a fixed conversion", "correct": True},
            {"text": "Because kilograms are used by scientists and newtons "
                     "are used in everyday life", "correct": False,
             "why": "It is the other way round in ordinary speech, and in any "
                    "case who uses a unit says nothing about what it "
                    "measures."},
            {"text": "Because newtons only apply to objects that are "
                     "actually moving", "correct": False,
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-02-e05",
        "band": "easier",
        "text": "Which quantity is measured in newtons?",
        "options": [            {"text": "Mass", "correct": False,
             "why": "Mass is measured in kilograms and never changes with "
                    "location."},
            {"text": "Density", "correct": False,
             "why": "Density is in g/cm³ or kg/m³."},
            {"text": "Gravitational field strength", "correct": False,
             "why": "That is measured in newtons per kilogram, not in newtons "
                    "alone."},
            {"text": "Weight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e06",
        "band": "easier",
        "text": "A pan balance measures…",
        "options": [            {"text": "weight, in newtons", "correct": False,
             "why": "It compares one mass against another, and gives the same "
                    "answer wherever it is used."},
            {"text": "density", "correct": False,
             "why": "Density needs a volume as well, which a balance does not "
                    "measure."},
            {"text": "gravitational field strength", "correct": False,
             "why": "It cannot measure the field at all; it cancels the "
                    "field out by comparing."},
            {"text": "mass, in kilograms", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e07",
        "band": "easier",
        "text": "A 6 kg object is carried to the Moon. What is its mass "
                "there?",
        "options": [            {"text": "1 kg, a sixth of its Earth value", "correct": False,
             "why": "It is the WEIGHT that falls to about a sixth; the mass "
                    "is unchanged."},
            {"text": "9.6 kg", "correct": False,
             "why": "That multiplies by 1.6, which is a field strength, not a "
                    "conversion for mass."},
            {"text": "0 kg, because it is weightless", "correct": False,
             "why": "It is not weightless on the Moon, and even in orbit its "
                    "mass would be 6 kg."},
            {"text": "6 kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e08",
        "band": "easier",
        "text": "A spring balance measures…",
        "options": [
            {"text": "a force", "correct": True},
            {"text": "an amount of matter", "correct": False,
             "why": "That is mass, which a pan balance measures by "
                    "comparison."},
            {"text": "a volume", "correct": False,
             "why": "Volume is measured with a cylinder or by displacement."},
            {"text": "an energy", "correct": False,
             "why": "Energy is measured in joules and is a different quantity "
                    "entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e09",
        "band": "easier",
        "text": "Which quantity decides how hard an object is to get moving?",
        "options": [            {"text": "Its mass", "correct": True},
            {"text": "Its weight", "correct": False,
             "why": "Weight is the pull downwards; getting something moving "
                    "sideways depends on its mass."},
            {"text": "The gravitational field strength where it is",
             "correct": False,
             "why": "That sets its weight; it does not change how hard the "
                    "object is to accelerate."},
            {"text": "Its density", "correct": False,
             "why": "Density says how tightly packed it is, not how much "
                    "matter there is altogether."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-02-s05",
        "band": "standard",
        "text": "A crate weighs 200 N on the Moon, where g = 1.6 N/kg. What "
                "is its mass?",
        "options": [            {"text": "320 kg", "correct": False,
             "why": "That is 200 × 1.6; to find a mass you divide the weight "
                    "by the field strength."},
            {"text": "200 kg", "correct": False,
             "why": "That is the weight with the unit swapped; the field "
                    "strength has not been used."},
            {"text": "20 kg", "correct": False,
             "why": "That uses Earth's 10 N/kg rather than the Moon's 1.6."},
            {"text": "125 kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s06",
        "band": "standard",
        "text": "Why is a heavy hammer just as hard to swing on the Moon as "
                "on Earth?",
        "options": [            {"text": "Because its mass is unchanged, and mass is what resists "
                     "a change of motion",
             "correct": True},
            {"text": "Because its weight is unchanged there", "correct": False,
             "why": "Its weight is about a sixth; it is the mass that has not "
                    "changed."},
            {"text": "Because there is no air on the Moon to swing it "
                     "through",
             "correct": False,
             "why": "Less air would make swinging slightly EASIER, not "
                    "harder."},
            {"text": "Because the astronaut is weaker in a spacesuit",
             "correct": False,
             "why": "A suit is awkward, but the physics point is that the "
                    "hammer's mass is the same."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s07",
        "band": "standard",
        "text": "Which instrument would still give a correct mass on Mars?",
        "options": [            {"text": "A spring balance calibrated on Earth", "correct": False,
             "why": "It reads the pull, which is much smaller on Mars, so its "
                    "kilogram scale would be wrong."},
            {"text": "Bathroom scales", "correct": False,
             "why": "They assume Earth's field strength, so they would "
                    "under-read badly."},
            {"text": "A pan balance with known masses", "correct": True},
            {"text": "A newtonmeter", "correct": False,
             "why": "A newtonmeter reads a force; it would give the Mars "
                    "weight, not the mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s08",
        "band": "standard",
        "text": "A 10 kg object is taken to the Moon, where g = 1.6 N/kg. "
                "Which row is right?",
        "options": [            {"text": "Mass 10 kg on Earth and 1.6 kg on the Moon",
             "correct": False,
             "why": "Mass does not change with location at all."},
            {"text": "Mass 10 kg everywhere; weight 100 N on both",
             "correct": False,
             "why": "The Moon pulls with 1.6 N on each kilogram, so the "
                    "weight there is 16 N."},
            {"text": "Weight 10 N everywhere; mass 100 kg on Earth",
             "correct": False,
             "why": "The two quantities have been swapped and neither figure "
                    "is right."},
            {"text": "Mass 10 kg; weight 100 N on Earth and 16 N on the "
                     "Moon",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s09",
        "band": "standard",
        "text": "A spring balance on Earth reads 60 N. What mass is hanging "
                "from it, taking g = 10 N/kg?",
        "options": [
            {"text": "600 kg", "correct": False,
             "why": "That multiplies by 10; to get a mass you divide the "
                    "force by the field strength."},
            {"text": "60 kg", "correct": False,
             "why": "That is the reading with the unit swapped, which is "
                    "exactly the confusion to avoid."},
            {"text": "6 kg", "correct": True},
            {"text": "70 kg", "correct": False,
             "why": "That adds the two, and newtons cannot be added to "
                    "N/kg."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-02-h05",
        "band": "harder",
        "text": "Why is weightless not the same as massless for an object in "
                "orbit?",
        "options": [            {"text": "Because it keeps all its mass, and could still crush "
                     "you",
             "correct": True},
            {"text": "Because a weightless object has no mass either",
             "correct": False,
             "why": "It keeps every kilogram it had; only the reading on a "
                    "balance has gone."},
            {"text": "Because weightless objects have negative mass",
             "correct": False,
             "why": "There is no such thing as negative mass; the mass is "
                    "simply unchanged."},
            {"text": "Because the two words mean the same thing in orbit",
             "correct": False,
             "why": "They come apart precisely there, which is why the "
                    "distinction matters."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h06",
        "band": "harder",
        "text": "Why would a spring balance calibrated on Earth OVER-read on "
                "Jupiter?",
        "options": [            {"text": "Because objects gain mass on a larger planet",
             "correct": False,
             "why": "Mass never changes; the pull on it does."},
            {"text": "Because springs stretch more in a thicker atmosphere",
             "correct": False,
             "why": "Atmosphere has nothing to do with how far the spring is "
                    "pulled."},
            {"text": "Because the same mass is pulled harder, so the spring "
                     "stretches further",
             "correct": True},
            {"text": "Because Jupiter spins faster, which adds to the "
                     "reading",
             "correct": False,
             "why": "Spin has a small effect; the 24.8 N/kg field strength is "
                    "what dominates."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h07",
        "band": "harder",
        "text": "On the Moon, which becomes easier: LIFTING a heavy toolbox, "
                "or shaking it from side to side?",
        "options": [
            {"text": "Both, because everything is easier on the Moon",
             "correct": False,
             "why": "Shaking it sideways is just as hard, because its mass is "
                    "unchanged."},
            {"text": "Neither, because its mass is unchanged", "correct": False,
             "why": "Lifting really is easier: the toolbox weighs about a "
                    "sixth of what it did."},
            {"text": "Lifting only", "correct": True},
            {"text": "Shaking only", "correct": False,
             "why": "Shaking is the one that does NOT get easier, since it "
                    "depends on the mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h08",
        "band": "harder",
        "text": "A 2 kg object weighs 3.2 N on one world and 20 N on another. "
                "What are the two field strengths?",
        "options": [            {"text": "3.2 N/kg and 20 N/kg", "correct": False,
             "why": "Those are the weights; each must be divided by the 2 kg "
                    "mass."},
            {"text": "0.63 N/kg and 0.1 N/kg", "correct": False,
             "why": "Those are the divisions upside down — mass over weight "
                    "instead of weight over mass."},
            {"text": "6.4 N/kg and 40 N/kg", "correct": False,
             "why": "That multiplies by the mass where the calculation "
                    "divides."},
            {"text": "1.6 N/kg and 10 N/kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h09",
        "band": "harder",
        "text": "Why does an object's weight change from world to world while "
                "its mass does not?",
        "options": [            {"text": "Because weight is the pull on the object, which depends "
                     "on where it is",
             "correct": True},
            {"text": "Because matter is squashed by a stronger field",
             "correct": False,
             "why": "Nothing about the matter changes; the pull on it does."},
            {"text": "Because kilograms are defined differently on each "
                     "world",
             "correct": False,
             "why": "A kilogram is the same everywhere, which is why mass is "
                    "the reliable one."},
            {"text": "Because weight is measured with a different instrument "
                     "on each world",
             "correct": False,
             "why": "The same spring balance gives different readings, which "
                    "is the effect rather than the cause."},
        ],
        "figure": None,
    },
]
