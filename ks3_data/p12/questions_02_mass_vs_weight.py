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

⚠️ MRB-338 night 3 top-up (e10–e30, s10–s30, h10–h30): 21 more per band,
continuing each band's id sequence. Coverage, self-checks and content
decisions are in the executor's final report for this run.
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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p12-02-e10",
        "band": "easier",
        "text": "Which ONE of these is unaffected by moving an object to a "
                "different planet?",
        "options": [
            {"text": "Its weight", "correct": False,
             "why": "Weight changes with the field strength of wherever "
                    "the object is taken."},
            {"text": "A spring balance's reading for it", "correct": False,
             "why": "A spring balance reads the object's weight, which "
                    "changes from place to place."},
            {"text": "How hard gravity pulls on it", "correct": False,
             "why": "That is another way of describing its weight, which "
                    "does change."},
            {"text": "Its mass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e11",
        "band": "easier",
        "text": "A pan balance is exactly balanced on Earth, comparing a "
                "rock against a 500 g standard mass. Would it stay balanced "
                "if both were carried to the Moon together?",
        "options": [
            {"text": "No — the rock would become heavier there",
             "correct": False,
             "why": "Nothing about the journey adds matter to the rock, so "
                    "its mass relative to the standard does not change."},
            {"text": "No — gravity would pull unevenly on the two sides "
                     "there, tipping the rock's pan down further than the "
                     "standard mass's pan", "correct": False,
             "why": "Gravity pulls on both sides of a pan balance in "
                    "exactly the same proportion, wherever it is used."},
            {"text": "Not until both have been weighed again on the Moon",
             "correct": False,
             "why": "A pan balance's comparison depends only on the two masses, "
                    "which the journey leaves exactly as they were."},
            {"text": "Yes — gravity pulls on both sides equally, wherever "
                     "the balance is used", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e12",
        "band": "easier",
        "text": "Two identical bags of sand — one full, one half-empty — are "
                "compared using a pan balance. Which does the balance show "
                "as heavier?",
        "options": [
            {"text": "Neither — they are identical bags", "correct": False,
             "why": "Being identical bags does not mean they contain the "
                    "same amount of sand."},
            {"text": "The half-empty one", "correct": False,
             "why": "Less sand means less mass, and a pan balance shows the "
                    "side with more mass as heavier."},
            {"text": "The full one", "correct": True},
            {"text": "It depends on which planet the balance is used on",
             "correct": False,
             "why": "A pan balance's comparison of mass gives the same "
                    "result wherever it is used."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e13",
        "band": "easier",
        "text": "Why is it easier to stop a bicycle than a car moving at the "
                "same speed?",
        "options": [
            {"text": "Because the car has a bigger engine", "correct": False,
             "why": "An engine's size affects how the car speeds up, not "
                    "how hard it is to stop once it is already moving."},
            {"text": "Because the car has more mass", "correct": True},
            {"text": "Because the car weighs more, and weight is what "
                     "resists stopping", "correct": False,
             "why": "It is mass, not weight, that resists a change in "
                    "motion — the two happen to be linked on Earth, but it "
                    "is the mass doing the work here."},
            {"text": "Because bicycles have better brakes than cars",
             "correct": False,
             "why": "The question is about the effort needed to stop, not "
                    "about the quality of the brakes fitted."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e14",
        "band": "easier",
        "text": "A brick and a feather sit on a table. Which is harder to "
                "set moving with a short, sharp push?",
        "options": [
            {"text": "The feather, because it is light and easily blown "
                     "about", "correct": False,
             "why": "Being easy to blow about is about air resistance, not "
                    "about how hard a short sharp push has to work."},
            {"text": "The brick", "correct": True},
            {"text": "Neither — a short sharp push moves anything equally "
                     "easily", "correct": False,
             "why": "An object's mass decides how much it resists being "
                    "set moving, and the brick has far more of it."},
            {"text": "It cannot be decided without knowing their weights",
             "correct": False,
             "why": "Their weights are not needed — mass is what decides "
                    "this, and the brick clearly has more matter in it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e15",
        "band": "easier",
        "text": "A spring balance shows a different reading in newtons when "
                "it is taken to another world. What has changed?",
        "options": [
            {"text": "The pull of gravity on the object", "correct": True},
            {"text": "The amount of matter in the object", "correct": False,
             "why": "The object's mass has not changed — only the pull on "
                    "it has."},
            {"text": "The object's size", "correct": False,
             "why": "Nothing about the object's size changes on the "
                    "journey."},
            {"text": "The newton itself has become a bigger or smaller "
                     "unit there", "correct": False,
             "why": "A newton is the same unit everywhere; what changes is "
                    "how many of them the object weighs."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e16",
        "band": "easier",
        "text": "A pan balance gives the same comparison wherever it is "
                "used. Why?",
        "options": [
            {"text": "Gravity pulls on both sides equally, so it cancels "
                     "out of the comparison", "correct": True},
            {"text": "Pan balances do not use gravity at all",
             "correct": False,
             "why": "A pan balance relies on gravity pulling down on both "
                    "pans — it works because gravity acts on both sides, "
                    "not because it avoids gravity."},
            {"text": "The masses on both sides adjust themselves to stay "
                     "equal, however different the two objects being "
                     "compared happen to be", "correct": False,
             "why": "Masses do not change to keep a balance level; the "
                    "comparison works because gravity's pull is identical "
                    "on both sides."},
            {"text": "Pan balances are calibrated separately for each planet "
                     "before use", "correct": False,
             "why": "A pan balance needs no calibration for a particular "
                    "planet — that is exactly why it gives a reliable "
                    "comparison anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e17",
        "band": "easier",
        "text": "A 1 kg block and a 5 kg block sit side by side on a table. "
                "Ignoring friction, which is harder to set sliding with a "
                "short, sharp push?",
        "options": [
            {"text": "The 1 kg block, because smaller objects need more "
                     "force to start them moving", "correct": False,
             "why": "It is the opposite — a smaller mass needs less force "
                    "to give it the same push-off."},
            {"text": "Neither — a short sharp push affects both equally",
             "correct": False,
             "why": "More mass means more resistance to being set moving, "
                    "so the two blocks are not affected equally."},
            {"text": "The 5 kg block", "correct": True},
            {"text": "It cannot be decided without knowing their weights",
             "correct": False,
             "why": "Their weights are not needed here — it is mass that "
                    "decides how hard each is to set moving."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e18",
        "band": "easier",
        "text": "A 1 kg block of modelling clay is squashed flat and then "
                "rolled out into a long sausage. What happens to its mass?",
        "options": [
            {"text": "It stays at 1 kg, because reshaping moves none of "
                     "the clay away", "correct": True},
            {"text": "It falls, because the flattened clay now takes up a "
                     "different amount of space", "correct": False,
             "why": "Mass counts the matter, not the space it occupies, "
                    "and reshaping the clay takes none of it away."},
            {"text": "It rises, because squashing packs the clay's "
                     "particles closer together", "correct": False,
             "why": "Packing particles closer changes the density, not "
                    "the amount of matter — no new clay has been added."},
            {"text": "It changes with every reshaping, because an "
                     "object's mass depends on its shape", "correct": False,
             "why": "Mass depends only on how much matter is present, "
                    "which the shape the clay is pushed into cannot "
                    "alter."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e19",
        "band": "easier",
        "text": "Which of these could a newtonmeter be used to measure "
                "directly?",
        "options": [
            {"text": "The weight of a bag of shopping", "correct": True},
            {"text": "The mass of a bag of shopping", "correct": False,
             "why": "A newtonmeter reads a force, in newtons; mass is "
                    "measured by comparison on a pan balance instead."},
            {"text": "How much space the bag takes up", "correct": False,
             "why": "That is volume, a different quantity from anything a "
                    "newtonmeter reads."},
            {"text": "How many items are inside the bag", "correct": False,
             "why": "A newtonmeter has no way of counting items; it only "
                    "reads the force pulling down on the whole bag."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e20",
        "band": "easier",
        "text": "A shopping bag has a weight of 20 N on Earth. Is 20 N also "
                "its mass?",
        "options": [
            {"text": "Yes — weight and mass are the same number on Earth",
             "correct": False,
             "why": "They are two different quantities, in different "
                    "units, that merely happen to be linked by Earth's "
                    "field strength."},
            {"text": "Yes, but only if the bag is not moving",
             "correct": False,
             "why": "Whether the bag is moving makes no difference to "
                    "which unit its weight or mass is measured in."},
            {"text": "No — mass would be measured in kilograms, not "
                     "newtons", "correct": True},
            {"text": "No, because 20 N is too small a number to be a mass",
             "correct": False,
             "why": "The size of the number is not the issue; 20 is simply "
                    "the wrong quantity entirely, in the wrong unit."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e21",
        "band": "easier",
        "text": "Mass belongs to the object alone. What does weight belong "
                "to?",
        "options": [
            {"text": "The object alone, just like mass", "correct": False,
             "why": "Weight also depends on where the object is, unlike "
                    "mass."},
            {"text": "The object and the place together", "correct": True},
            {"text": "The place alone, regardless of the object",
             "correct": False,
             "why": "A bigger object still weighs more than a smaller one "
                    "in the same place, so the object matters too."},
            {"text": "Neither the object nor the place — it is fixed by "
                     "the unit newton", "correct": False,
             "why": "Newtons are simply the unit weight is measured in; "
                    "the unit itself does not fix how many of them an "
                    "object weighs."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e22",
        "band": "easier",
        "text": "Two identical metal blocks are compared using a pan balance "
                "while both sit inside a lift moving upward at a steady "
                "speed. Does the comparison still work correctly?",
        "options": [
            {"text": "No — moving upward makes both blocks heavier by "
                     "different amounts", "correct": False,
             "why": "Moving at a steady speed changes nothing about the "
                    "pull of gravity on either block."},
            {"text": "Yes", "correct": True},
            {"text": "No — a pan balance only works when perfectly still",
             "correct": False,
             "why": "What matters is that gravity pulls on both sides "
                    "equally, which is still true while moving at a "
                    "steady speed."},
            {"text": "It cannot be known without stopping the lift first",
             "correct": False,
             "why": "The comparison depends only on the two masses and "
                    "gravity acting equally on both, neither of which "
                    "needs the lift to be stopped."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e23",
        "band": "easier",
        "text": "Why do we say weight belongs to the object AND the place, "
                "rather than to the object alone?",
        "options": [
            {"text": "Because weight depends on the object's mass and on "
                     "the gravitational field strength where it is",
             "correct": True},
            {"text": "Because every object has two separate weights, one "
                     "for each place it visits", "correct": False,
             "why": "An object has one weight at a time, wherever it "
                    "currently is — it does not carry several weights "
                    "around with it."},
            {"text": "Because the place decides an object's weight on its "
                     "own, without needing to know the object's mass",
             "correct": False,
             "why": "Two objects of different mass in the same place have "
                    "different weights, so the object's own mass matters "
                    "too."},
            {"text": "Because weight is really just a nickname for the "
                     "place's field strength", "correct": False,
             "why": "Field strength alone is measured in N/kg; weight is "
                    "a force in newtons, which needs the object's mass as "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e24",
        "band": "easier",
        "text": "A toy car (200 g) and a real car (1200 kg) are both "
                "stationary. Which needs a bigger force to get moving at "
                "the same rate?",
        "options": [
            {"text": "The real car", "correct": True},
            {"text": "The toy car, because small objects need more force "
                     "to get started", "correct": False,
             "why": "It is the opposite — the object with less mass needs "
                    "less force to reach the same rate of speeding up."},
            {"text": "Neither — both need the same force", "correct": False,
             "why": "The real car has vastly more mass, so it needs a "
                    "vastly bigger force to speed up at the same rate."},
            {"text": "It depends on their weights, not their masses",
             "correct": False,
             "why": "It is mass, not weight, that decides how much force "
                    "is needed to change an object's motion."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e25",
        "band": "easier",
        "text": "Which of these units belongs to a force rather than to a "
                "mass or a field strength?",
        "options": [
            {"text": "kg", "correct": False,
             "why": "Kilograms measure mass."},
            {"text": "N/kg", "correct": False,
             "why": "That is the unit of gravitational field strength."},
            {"text": "cm", "correct": False,
             "why": "Centimetres measure length, not force."},
            {"text": "N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e26",
        "band": "easier",
        "text": "A trolley with smooth, freely-running wheels is still "
                "hard to push into motion. What does this tell you about "
                "the trolley?",
        "options": [
            {"text": "It has a lot of weight", "correct": False,
             "why": "Weight would only matter if you were trying to LIFT "
                    "the trolley; pushing it sideways is resisted by its "
                    "mass."},
            {"text": "It is made of a dense material", "correct": False,
             "why": "Density describes how tightly packed the material "
                    "is, not how much matter is there overall — a large, "
                    "low-density object can still have a lot of mass."},
            {"text": "It has a lot of mass", "correct": True},
            {"text": "It has a lot of friction with the ground",
             "correct": False,
             "why": "The wheels are described as running freely, so "
                    "friction is not what is resisting the push here; "
                    "what is left is the trolley's own mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e27",
        "band": "easier",
        "text": "A 6 kg rock is taken to the Moon, where g = 1.6 N/kg. "
                "Which pair of values is correct for it there?",
        "options": [
            {"text": "A mass of 9.6 kg and a weight of 6 N",
             "correct": False,
             "why": "The two have been swapped, and the units with them: "
                    "6 kg is the mass and 9.6 N is the weight."},
            {"text": "A mass of 6 kg and a weight of 60 N",
             "correct": False,
             "why": "That uses Earth's 10 N/kg rather than the Moon's "
                    "1.6 N/kg."},
            {"text": "A mass of 6 kg and a weight of 9.6 N",
             "correct": True},
            {"text": "A mass of 1.6 kg and a weight of 6 N",
             "correct": False,
             "why": "1.6 is the Moon's field strength in N/kg, not the "
                    "rock's mass; the mass stays at 6 kg wherever the "
                    "rock goes."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e28",
        "band": "easier",
        "text": "A rock's mass is 4 kg wherever it is weighed. If the rock "
                "is moved to a different planet, what can you conclude "
                "about its weight there from its mass alone?",
        "options": [
            {"text": "That its weight will also stay at exactly 4, whatever the "
                     "planet",
             "correct": False,
             "why": "Weight is measured in newtons, not kilograms, and it "
                    "changes with the field strength of the new planet."},
            {"text": "Nothing — you would also need to know the field "
                     "strength there", "correct": True},
            {"text": "That its weight must have doubled", "correct": False,
             "why": "Nothing about simply changing planets doubles "
                    "anything; the actual change depends on the specific "
                    "field strength there."},
            {"text": "That its weight will be less than 4 N wherever it "
                     "goes, since 4 kg was already a fairly small mass to "
                     "begin with", "correct": False,
             "why": "On a planet with a strong enough field, the rock "
                    "could weigh far more than 4 N."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e29",
        "band": "easier",
        "text": "Two bags of rice, X and Y, feel equally heavy when lifted "
                "by hand on Earth. What can you say about their masses?",
        "options": [
            {"text": "Nothing, without weighing them on a proper "
                     "instrument", "correct": False,
             "why": "On Earth, equal weight in the same place is exactly "
                    "the evidence needed to conclude equal mass."},
            {"text": "Bag X must have slightly more mass, because it was "
                     "mentioned first", "correct": False,
             "why": "The order the bags are named in has no bearing on "
                    "the physics at all."},
            {"text": "Their masses must be different, because no two bags "
                     "are ever identical", "correct": False,
             "why": "The question is about what the equal-weight "
                    "observation tells you, and it tells you their masses "
                    "are equal."},
            {"text": "They have equal mass", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-e30",
        "band": "easier",
        "text": "Which of these is the odd one out, and why: kilogram, "
                "newton, gram, tonne?",
        "options": [
            {"text": "Kilogram, because it is the only one of the four "
                     "that could ever be read directly off a pan balance "
                     "without any conversion at all", "correct": False,
             "why": "A pan balance gives its answer in grams, kilograms "
                    "or tonnes equally readily; none of the three mass "
                    "units has to be converted first."},
            {"text": "Newton — it is the only unit of force; the other "
                     "three are all units of mass", "correct": True},
            {"text": "Gram, because it is the smallest of the four units listed "
                     "here",
             "correct": False,
             "why": "Being the smallest is a fact about size, not about "
                    "what kind of quantity the unit measures, which is "
                    "the odd-one-out here."},
            {"text": "Tonne, because it is used for very large masses",
             "correct": False,
             "why": "A tonne is still a unit of mass, just like kilogram "
                    "and gram — it is not the odd one out by kind."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p12-02-s10",
        "band": "standard",
        "text": "A loaded shipping container (mass 8000 kg) and an empty "
                "one (mass 2000 kg) are both pushed by the same tug with "
                "the same force on a frictionless dock. Which speeds up "
                "faster, and why?",
        "options": [
            {"text": "The loaded one, because a bigger object always wins "
                     "a contest of force", "correct": False,
             "why": "For a given force, MORE mass means LESS speeding up, "
                    "not more — the loaded container has four times the "
                    "mass of the empty one."},
            {"text": "The empty one, because it has less mass to "
                     "accelerate for the same force", "correct": True},
            {"text": "Both speed up at exactly the same rate, because the "
                     "tug applies the same force to each", "correct": False,
             "why": "The same force gives a different rate of speeding up "
                    "depending on how much mass it has to accelerate."},
            {"text": "It cannot be decided without knowing their weights",
             "correct": False,
             "why": "Weight is not needed here — it is the mass of each "
                    "container that decides how it responds to the same "
                    "force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s11",
        "band": "standard",
        "text": "A 250 g apple and a 1.5 kg bag of potatoes are compared on "
                "a pan balance while both are carried up in a lift moving "
                "at a steady speed. Which does the balance show as "
                "heavier, and would the same be true if the lift were "
                "standing still?",
        "options": [
            {"text": "The apple in the lift, but the potatoes once the "
                     "lift stops", "correct": False,
             "why": "A pan balance's comparison of mass does not flip "
                    "depending on whether the lift is moving — the "
                    "potatoes have more mass throughout."},
            {"text": "Neither — the two exactly balance while the lift is "
                     "moving", "correct": False,
             "why": "1.5 kg of potatoes is six times the mass of a 250 g "
                    "apple, so the balance would clearly tip towards the "
                    "potatoes."},
            {"text": "The apple, in both cases", "correct": False,
             "why": "The apple has far less mass than the potatoes, so "
                    "the balance would show the potatoes as heavier, not "
                    "the apple."},
            {"text": "The potatoes, in both cases", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s12",
        "band": "standard",
        "text": "A newtonmeter reads 15 N for an object on Earth. Roughly "
                "what would the same newtonmeter read for the same object "
                "on Mars, where the field strength is a little over a "
                "third of Earth's?",
        "options": [
            {"text": "About 5.5 N", "correct": True},
            {"text": "About 15 N, because a newtonmeter always reads the "
                     "same wherever it is used", "correct": False,
             "why": "A newtonmeter reads the pull of gravity, which is "
                    "genuinely weaker on Mars, so its reading falls "
                    "there."},
            {"text": "About 41 N, because a weaker field means a bigger "
                     "reading", "correct": False,
             "why": "A weaker field pulls LESS hard, giving a SMALLER "
                    "reading, not a bigger one."},
            {"text": "About 1.5 N", "correct": False,
             "why": "That divides by ten instead of scaling by the "
                    "roughly one-third ratio between the two field "
                    "strengths."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s13",
        "band": "standard",
        "text": "Explain why a fully loaded shopping trolley is much "
                "easier to lift off the ground on the Moon than on Earth, "
                "but exactly as hard to bring to a sudden stop once it is "
                "rolling.",
        "options": [
            {"text": "Lifting depends on weight, which is smaller on the "
                     "Moon; stopping depends on mass, which is unchanged",
             "correct": True},
            {"text": "Both lifting and stopping depend on weight, and "
                     "weight happens to be smaller only while it is being "
                     "lifted straight up off the ground",
             "correct": False,
             "why": "Weight does not behave differently depending on the "
                    "task — it is smaller on the Moon throughout; "
                    "stopping is resisted by mass instead, which is why "
                    "it stays hard."},
            {"text": "Both depend on mass, and mass is smaller on the "
                     "Moon while lifting but not while rolling",
             "correct": False,
             "why": "Mass does not change with location at all, whatever "
                    "the trolley happens to be doing."},
            {"text": "Lifting depends on mass and stopping depends on "
                     "weight, the opposite way round", "correct": False,
             "why": "It is lifting that works against weight (the pull of "
                    "gravity) and stopping that works against mass (the "
                    "reluctance to change motion), not the other way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s14",
        "band": "standard",
        "text": "A large gas cylinder (80 kg) and a small one (10 kg) are "
                "both pushed with identical shoves on smooth ice. Which "
                "ends up moving faster?",
        "options": [
            {"text": "The large cylinder, because a bigger push-off comes "
                     "from a bigger object", "correct": False,
             "why": "The push given is identical for both; what differs "
                    "is how much each cylinder resists being sped up, and "
                    "the large one resists more."},
            {"text": "The small cylinder, because it has less mass to "
                     "accelerate for the same shove", "correct": True},
            {"text": "Both end up moving at the same speed, because the "
                     "shove given to each is identical", "correct": False,
             "why": "An identical shove produces a different result "
                    "depending on the mass it has to accelerate."},
            {"text": "Neither moves at all, because ice is frictionless "
                     "rather than completely smooth", "correct": False,
             "why": "A frictionless surface is exactly what lets a shove "
                    "set an object moving with nothing resisting it "
                    "afterwards."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s15",
        "band": "standard",
        "text": "A pupil says: 'A spring balance's reading changes on other "
                "worlds, but a pan balance's readings never do.' Is this "
                "correct?",
        "options": [
            {"text": "No — both instruments give different readings once they "
                     "are taken to another world", "correct": False,
             "why": "A pan balance compares mass, which does not change "
                    "with location, so its readings stay the same."},
            {"text": "No — neither instrument's readings change anywhere",
             "correct": False,
             "why": "A spring balance's reading is a weight, and weight "
                    "genuinely does change from world to world."},
            {"text": "It cannot be judged without knowing the exact field "
                     "strengths of the other worlds involved in the "
                     "comparison", "correct": False,
             "why": "The general rule holds regardless of the exact "
                    "figures: spring balances read weight, which varies; "
                    "pan balances compare mass, which does not."},
            {"text": "Yes — spring balances read weight, which changes, "
                     "and pan balances compare mass, which does not",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s16",
        "band": "standard",
        "text": "Astronauts on the International Space Station measure "
                "their body mass using a special chair that oscillates "
                "back and forth on a spring, rather than an ordinary "
                "weighing method. Explain why an oscillating chair can "
                "find their mass when an ordinary method could not.",
        "options": [
            {"text": "Because springs work better in the cold of space "
                     "than they do on Earth", "correct": False,
             "why": "Temperature is not the reason; the real problem for "
                    "an ordinary weighing method in orbit is that nothing "
                    "presses down on it."},
            {"text": "How quickly something oscillates on a spring "
                     "depends on its mass, and this needs no gravity "
                     "pressing anything down", "correct": True},
            {"text": "The chair actually measures the astronaut's weight, "
                     "and weight happens to stay constant throughout an "
                     "orbit around the Earth", "correct": False,
             "why": "Their weight in orbit is real and close to its "
                    "surface value; what is missing is anything to press "
                    "against, so nothing can read it by being pressed on. "
                    "The chair measures something unrelated to gravity "
                    "altogether."},
            {"text": "Oscillating chairs are simply a far more accurate version "
                     "of the ordinary bathroom scales used on Earth", "correct": False,
             "why": "It is not extra accuracy that matters here — an "
                    "oscillating chair works on a completely different "
                    "principle that does not depend on gravity at all."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s17",
        "band": "standard",
        "text": "Two students disagree about a 3 kg toolbox on a table. "
                "One says it 'weighs 3 kilograms'; the other says it 'has "
                "a mass of 3 kilograms, and weighs about 30 newtons.' Who "
                "is more accurate, and why?",
        "options": [
            {"text": "The second student — kilograms measure mass, and "
                     "the toolbox's weight on Earth would be about "
                     "30 N", "correct": True},
            {"text": "The first student — 'weighs 3 kilograms' is the "
                     "simpler and therefore more correct way to say it",
             "correct": False,
             "why": "Being simpler does not make a statement more "
                    "accurate; kilograms are a unit of mass, not weight, "
                    "however the sentence is phrased."},
            {"text": "Both are equally accurate, because kilograms and "
                     "newtons are just two names for the same unit",
             "correct": False,
             "why": "Kilograms and newtons are units of two different "
                    "quantities, mass and force, not two names for one "
                    "unit."},
            {"text": "Neither is accurate, because the toolbox's true "
                     "weight cannot be found without weighing it directly",
             "correct": False,
             "why": "The toolbox's approximate weight can be estimated "
                    "perfectly well from its mass and Earth's known field "
                    "strength."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s18",
        "band": "standard",
        "text": "Why does a trampoline need to push harder to stop a "
                "heavier adult than a lighter child, when both are "
                "bouncing at exactly the same downward speed?",
        "options": [
            {"text": "Because the adult weighs more, and weight is what "
                     "resists a change in motion", "correct": False,
             "why": "It is mass, not weight, that resists a change in "
                    "motion — weight and mass are linked on Earth, but "
                    "mass is doing the work here."},
            {"text": "Because the adult has more mass, so more force is "
                     "needed to bring them to a stop by the same amount",
             "correct": True},
            {"text": "Because adults bounce with more energy than "
                     "children do", "correct": False,
             "why": "Both are described as moving at the SAME speed, so "
                    "the difference in force needed comes from their "
                    "mass, not from how much energy either has."},
            {"text": "Because a trampoline's springs stretch further "
                     "under an adult, which needs no extra force at all",
             "correct": False,
             "why": "Stretching further under a heavier person is exactly "
                    "why more force is needed — the springs are not "
                    "somehow exempt from needing more force to stop more "
                    "mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s19",
        "band": "standard",
        "text": "A 1 kg mass weighs 10 N on Earth. On a newly discovered "
                "moon, the same 1 kg mass weighs only 2 N. What can you "
                "conclude about a pan balance's reading for this mass on "
                "that moon, compared with a known 1 kg standard mass "
                "there?",
        "options": [
            {"text": "The balance would tip towards the standard mass, "
                     "because 2 N is a smaller reading than 10 N read on "
                     "Earth", "correct": False,
             "why": "A pan balance compares MASS, not the newton reading "
                    "of a spring balance; both objects have exactly 1 kg "
                    "of mass, wherever they are weighed."},
            {"text": "The balance would tip towards the unknown mass "
                     "instead, for the same reason", "correct": False,
             "why": "Nothing here gives either side more mass than the "
                    "other — both are described as having a mass of "
                    "1 kg."},
            {"text": "It cannot be predicted without knowing the moon's "
                     "exact field strength first", "correct": False,
             "why": "The comparison of two equal masses on a pan balance "
                    "does not depend on the field strength at all, "
                    "whatever it happens to be."},
            {"text": "It would still balance exactly, because both "
                     "objects experience the same weaker pull",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s20",
        "band": "standard",
        "text": "A 45 kg suitcase and an empty 5 kg suitcase are lifted "
                "with an identical force by an airport conveyor arm on "
                "Earth. Which accelerates upward faster, and why?",
        "options": [
            {"text": "The 45 kg suitcase, because heavier objects always "
                     "respond more strongly to a lifting force",
             "correct": False,
             "why": "For an identical force, MORE mass means a SMALLER "
                    "acceleration, not a bigger one."},
            {"text": "Neither — an identical force gives an identical "
                     "acceleration to any mass", "correct": False,
             "why": "The same force produces a different acceleration "
                    "depending on how much mass it has to move."},
            {"text": "It cannot be worked out without knowing each "
                     "suitcase's weight", "correct": False,
             "why": "Weight is not needed here — it is each suitcase's "
                    "mass that decides how it responds to the same lifting "
                    "force."},
            {"text": "The empty 5 kg suitcase, because it has less mass "
                     "to accelerate for the same force", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s21",
        "band": "standard",
        "text": "A pan balance shows a rock as more massive than a 200 g "
                "standard mass, both on Earth. The rock is then taken "
                "alone to the Moon; the standard mass stays behind on "
                "Earth. Can you still conclude the rock has more than "
                "200 g of mass?",
        "options": [
            {"text": "Yes — mass never changes with location, so the "
                     "earlier Earth comparison still tells you the rock "
                     "has more than 200 g of mass", "correct": True},
            {"text": "No — the comparison is only valid while both objects are "
                     "sitting together on the same pan balance",
             "correct": False,
             "why": "The comparison established a FACT about the rock's "
                    "mass at the time it was made, and mass does not "
                    "change afterwards simply because the objects are "
                    "later separated."},
            {"text": "No — once the rock leaves Earth, its mass can no "
                     "longer be compared with anything measured there, "
                     "since the two are no longer side by side",
             "correct": False,
             "why": "Mass is the same everywhere, so a comparison made on "
                    "Earth remains true wherever the rock is later taken."},
            {"text": "It depends on whether the Moon's gravity has "
                     "changed the rock's mass since the comparison",
             "correct": False,
             "why": "Gravity, wherever it acts, never changes an object's "
                    "mass — only its weight."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s22",
        "band": "standard",
        "text": "A shopping bag has a weight of 8 N on Earth. Estimate its "
                "mass, and explain how you know your estimate is in the "
                "right unit.",
        "options": [
            {"text": "8 kg, because the number in newtons and the number "
                     "in kilograms are always the same, on Earth and "
                     "everywhere else", "correct": False,
             "why": "The two numbers are only linked through Earth's "
                    "field strength — dividing by 10, not copying the "
                    "figure across, is what gives the mass."},
            {"text": "About 0.8 kg, found by dividing the weight in "
                     "newtons by Earth's field strength in N/kg, since "
                     "N ÷ (N/kg) leaves kg", "correct": True},
            {"text": "80 kg, found by multiplying the weight by Earth's "
                     "field strength", "correct": False,
             "why": "Multiplying goes the wrong way — dividing the weight "
                    "by the field strength is what gives a mass, not "
                    "multiplying."},
            {"text": "8 N, because weight and mass can be written with "
                     "either unit once a value is known", "correct": False,
             "why": "A mass has to be expressed in kilograms; writing it "
                    "in newtons would describe a force, not an amount of "
                    "matter."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s23",
        "band": "standard",
        "text": "A student says two objects with the same mass must always "
                "have the same weight. Give one situation where this is "
                "false.",
        "options": [
            {"text": "When one of the objects is denser than the other",
             "correct": False,
             "why": "Density affects an object's size, not the "
                    "relationship between its mass and its weight in a "
                    "given field."},
            {"text": "Whenever the two objects are placed in different "
                     "gravitational fields", "correct": True},
            {"text": "When one object is moving and the other is "
                     "stationary", "correct": False,
             "why": "Whether an object is moving makes no difference to "
                    "the relationship between its mass and its weight."},
            {"text": "There is no such situation — equal mass always "
                     "means equal weight", "correct": False,
             "why": "Equal mass only guarantees equal weight while both "
                    "objects are in the SAME gravitational field."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s24",
        "band": "standard",
        "text": "A person stands on bathroom scales inside a lift. As "
                "the lift sets off downward and speeds up, the scales "
                "read less than usual. Has the person's mass changed?",
        "options": [
            {"text": "No — their mass is unchanged; the scales read the "
                     "push between the person and the floor, and that "
                     "push is smaller while the lift speeds up downward",
             "correct": True},
            {"text": "Yes — their mass falls while the lift speeds up "
                     "downward, which is exactly what the smaller reading "
                     "is showing", "correct": False,
             "why": "Mass is the amount of matter in the person, and a "
                    "lift journey adds or removes none of it; what has "
                    "changed is only the push on the scales."},
            {"text": "No — their mass is unchanged, and the reading has "
                     "not really fallen either; the dial is simply hard "
                     "to read while the lift is moving",
             "correct": False,
             "why": "The drop in the reading is real: while the lift "
                    "speeds up downward, the floor genuinely pushes up on "
                    "the person less hard."},
            {"text": "Yes — their weight and their mass both fall "
                     "together, because the two always change in step",
             "correct": False,
             "why": "Weight and mass move in step only when the field "
                    "strength is what has changed. Here the field "
                    "strength is the same and only the push on the "
                    "scales has altered."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s25",
        "band": "standard",
        "text": "A 1 kg mass weighs 10 N on Earth. A newtonmeter is used, "
                "unmodified, on a different world and reads 4 N for the "
                "same 1 kg mass. What is that world's field strength?",
        "options": [
            {"text": "40 N/kg", "correct": False,
             "why": "That multiplies the two figures instead of dividing "
                    "the weight by the mass."},
            {"text": "4 N/kg", "correct": True},
            {"text": "6 N/kg", "correct": False,
             "why": "That subtracts the reading from Earth's field "
                    "strength, which is not the calculation needed here."},
            {"text": "0.25 N/kg", "correct": False,
             "why": "That divides the mass by the weight instead of the "
                    "weight by the mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s26",
        "band": "standard",
        "text": "Which correctly completes this: 'A trolley loaded with "
                "bricks needs more force to speed it up than an empty "
                "trolley, because it has more ___, not because it ___.'",
        "options": [
            {"text": "weight … has more mass", "correct": False,
             "why": "The reasoning has been reversed — it is mass, not "
                    "weight, that decides how much force is needed to "
                    "speed something up."},
            {"text": "friction … is heavier", "correct": False,
             "why": "Friction is a separate effect from the force needed "
                    "to change an object's speed in the first place."},
            {"text": "mass … weighs more", "correct": True},
            {"text": "volume … takes up more room", "correct": False,
             "why": "How much space the bricks take up is not what "
                    "decides how hard the loaded trolley is to speed up — "
                    "their mass is."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s27",
        "band": "standard",
        "text": "A 1 tonne (1000 kg) boulder and a 1 kg pebble are both "
                "given an identical hard shove on frictionless ice. Which "
                "moves off faster?",
        "options": [
            {"text": "The pebble, because it has far less mass to "
                     "accelerate", "correct": True},
            {"text": "The boulder, because a bigger shove is needed to "
                     "move a bigger object, and bigger shoves give bigger "
                     "speeds", "correct": False,
             "why": "The shove given to both is described as identical; "
                    "the pebble ends up faster because it has so much "
                    "less mass to accelerate."},
            {"text": "Both move off at the same speed, since the shove "
                     "applied is identical in each case", "correct": False,
             "why": "An identical shove produces a very different result "
                    "depending on how much mass it is accelerating."},
            {"text": "It cannot be decided without knowing their "
                     "weights", "correct": False,
             "why": "Weight is not the relevant quantity here — it is "
                    "each object's mass that decides its response to the "
                    "same shove."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s28",
        "band": "standard",
        "text": "Why would carrying a rucksack up a mountain make it "
                "'feel' very slightly lighter by the time you reach the "
                "top, even though nothing has been taken out of it?",
        "options": [
            {"text": "Because some of its mass is used up climbing the "
                     "mountain", "correct": False,
             "why": "Climbing does not remove any matter from the "
                    "rucksack; its mass stays exactly the same throughout."},
            {"text": "Gravitational field strength weakens very slightly "
                     "with altitude, so the same mass weighs a tiny bit "
                     "less", "correct": True},
            {"text": "The rucksack's mass genuinely falls slightly at "
                     "altitude, because there is less air pressing down "
                     "on it near the top of the mountain",
             "correct": False,
             "why": "Air pressure has no effect on how much matter is in "
                    "the rucksack — its mass is unchanged."},
            {"text": "It is an illusion caused entirely by tiredness, "
                     "with no real change in the rucksack's weight",
             "correct": False,
             "why": "There is a small real change — field strength really "
                    "does weaken slightly with altitude, though the "
                    "effect over a mountain's height is tiny."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s29",
        "band": "standard",
        "text": "A supermarket trolley loaded with 25 kg of shopping is "
                "pushed across a smooth floor. Explain why doubling the "
                "load to 50 kg, while pushing with the same force, "
                "roughly halves how quickly it speeds up.",
        "options": [
            {"text": "Because the force needed for a given change in "
                     "speed is shared out over the object's mass, so "
                     "doubling the mass for the same force roughly halves "
                     "the rate of speeding up", "correct": True},
            {"text": "Because doubling the load doubles the friction "
                     "between the trolley's wheels and the floor, and "
                     "friction is what mainly decides how quickly "
                     "anything heavy can be made to speed up on a real "
                     "floor", "correct": False,
             "why": "The floor is described as smooth, and in any case "
                    "friction is a separate effect from how a fixed force "
                    "shares out over a bigger mass."},
            {"text": "Because a heavier trolley's wheels turn more slowly for a "
                     "mechanical reason unrelated to mass, and it is the "
                     "turning of the wheels rather than the load itself that "
                     "sets how fast a trolley can pick up speed",
             "correct": False,
             "why": "There is no such separate mechanical effect here — "
                    "the slower speeding-up comes directly from the "
                    "trolley now having twice the mass to accelerate."},
            {"text": "Because the shopping itself resists being pushed, "
                     "quite apart from the trolley's own mass",
             "correct": False,
             "why": "The shopping's mass IS part of what needs "
                    "accelerating here — it is not a separate effect on "
                    "top of the trolley's mass, it is added to it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-s30",
        "band": "standard",
        "text": "Explain why two identical-looking bags might have very "
                "different masses, even though they are exactly the same "
                "size.",
        "options": [
            {"text": "Because mass depends on how much matter is packed "
                     "into the bag, not simply on the bag's outer size",
             "correct": True},
            {"text": "Because identical-looking bags always contain "
                     "identical amounts of matter, so this could not "
                     "actually happen", "correct": False,
             "why": "Two bags can look the same on the outside while "
                    "holding very different materials packed inside "
                    "them."},
            {"text": "Because mass is decided by a bag's outer size "
                     "alone, regardless of what is inside it",
             "correct": False,
             "why": "Outer size on its own says nothing about mass — a "
                    "bag of feathers and a same-sized bag of sand have "
                    "very different masses."},
            {"text": "Because one bag must be on a different planet from "
                     "the other", "correct": False,
             "why": "Location plays no part in this — two bags of "
                    "different masses can sit side by side in the same "
                    "room."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p12-02-h10",
        "band": "harder",
        "text": "A 900 g mass weighs 9 N on an unfamiliar moon. What is the "
                "moon's field strength, and what would a 1.5 kg mass "
                "weigh there?",
        "options": [
            {"text": "10 N/kg, so the 1.5 kg mass would weigh 15 N there",
             "correct": True},
            {"text": "8.1 N/kg, so the 1.5 kg mass would weigh 12.15 N "
                     "there", "correct": False,
             "why": "That subtracts the two figures given (9 − 0.9) "
                    "instead of dividing the weight by the mass to find "
                    "the field strength."},
            {"text": "0.1 N/kg, so the 1.5 kg mass would weigh 0.15 N "
                     "there", "correct": False,
             "why": "That divides the mass by the weight instead of the "
                    "weight by the mass."},
            {"text": "9 N/kg, so the 1.5 kg mass would weigh 13.5 N "
                     "there", "correct": False,
             "why": "That reads the field strength straight off the 9 N "
                    "weight as though the mass were exactly 1 kg, rather "
                    "than 0.9 kg."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h11",
        "band": "harder",
        "text": "A 1 kg mass weighs 10 N on Earth. On planet A it weighs "
                "4 N; on planet B it weighs 25 N. Which planet has the "
                "stronger field, and by what factor is planet B's field "
                "stronger than planet A's?",
        "options": [
            {"text": "Planet B, by a factor of 6.25", "correct": True},
            {"text": "Planet A, by a factor of 6.25", "correct": False,
             "why": "25 N/kg is a stronger field than 4 N/kg, so planet B "
                    "is the stronger one, not planet A."},
            {"text": "Planet B, by a factor of 21", "correct": False,
             "why": "That subtracts the two field strengths (25 − 4) "
                    "rather than dividing one by the other to find the "
                    "factor between them."},
            {"text": "Planet B, by a factor of 2.5", "correct": False,
             "why": "That compares planet B's field only with Earth's, "
                    "rather than with planet A's, which is what the "
                    "question asks for."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h12",
        "band": "harder",
        "text": "An astronaut's mass is unchanged whether they are on "
                "Earth, on the Moon, or freely falling in orbit. Which "
                "method of finding their mass would fail while they are "
                "freely falling in orbit, and why?",
        "options": [
            {"text": "An oscillating chair that times how fast a spring "
                     "pushes and pulls them, because springs do not work "
                     "without gravity", "correct": False,
             "why": "A spring's push and pull come from being stretched "
                    "or squashed, not from gravity, so it keeps working "
                    "perfectly well in free fall."},
            {"text": "Neither method would fail — both give the correct "
                     "mass in every situation", "correct": False,
             "why": "Nothing presses on the pans of a pan balance in "
                    "free fall, so it has nothing to compare and cannot "
                    "give a reading at all."},
            {"text": "A pan balance, because nothing presses down on "
                     "either pan when everything is falling together",
             "correct": True},
            {"text": "Both methods would fail, because no mass at all can be "
                     "measured while in orbit", "correct": False,
             "why": "Mass can still be measured in orbit — the "
                    "oscillating-chair method works precisely because it "
                    "needs no gravity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h13",
        "band": "harder",
        "text": "A 500 g toy on Earth is compared with a standard 500 g "
                "mass using a pan balance, and they balance exactly. The "
                "toy is then dropped from a great height with no air "
                "resistance. At the instant just before it lands, is it "
                "still true that the toy's mass equals 500 g?",
        "options": [
            {"text": "No — falling adds extra mass to the toy",
             "correct": False,
             "why": "Falling does not add matter to anything; nothing "
                    "about speeding up under gravity changes what an "
                    "object is made of."},
            {"text": "No — the toy becomes weightless while falling, so "
                     "it has no mass either", "correct": False,
             "why": "Even a genuinely weightless falling object keeps "
                    "every gram of its mass; weightlessness is not the "
                    "same as masslessness."},
            {"text": "It cannot be known without weighing it again on "
                     "the way down", "correct": False,
             "why": "Mass does not change during a fall; there is "
                    "nothing new to find out."},
            {"text": "Yes — the toy's mass is never affected by falling",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h14",
        "band": "harder",
        "text": "A student argues: 'A heavy object needs a lot of force "
                "to get it moving, so heavy objects must also need a lot "
                "of force to keep moving at a steady speed once they are "
                "already going.' What is wrong with the second half of "
                "this claim?",
        "options": [
            {"text": "Nothing is wrong — heavier objects always need "
                     "more force just to keep going, and that force has "
                     "to be supplied continuously for as long as they "
                     "keep moving at all", "correct": False,
             "why": "On a frictionless surface, an object moving at a "
                    "steady speed needs no force to keep going, whatever "
                    "its mass."},
            {"text": "The claim is right for light objects but wrong for "
                     "heavy ones", "correct": False,
             "why": "The rule about steady motion needing no force "
                    "applies equally, regardless of how much mass the "
                    "object has."},
            {"text": "Keeping something moving at a steady speed on a "
                     "frictionless surface needs no force at all — force "
                     "is only needed to change how fast or which way "
                     "something is moving", "correct": True},
            {"text": "The first half is also wrong — heavy objects do "
                     "not need more force to get moving", "correct": False,
             "why": "The first half is correct: more mass genuinely does "
                    "mean more force is needed to set something moving at "
                    "a given rate."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h15",
        "band": "harder",
        "text": "A pan balance and a set of standard masses are sent, "
                "together with a rock sample, to the surface of a newly "
                "discovered moon with an unknown field strength. Can the "
                "astronauts still find the rock's mass accurately?",
        "options": [
            {"text": "Yes — gravity, whatever its strength there, pulls "
                     "on both the rock and the standard masses equally, "
                     "so the comparison still works", "correct": True},
            {"text": "No — the standard masses would need to be "
                     "recalibrated for the new field strength first, "
                     "before they could be trusted to give a reading "
                     "anyone could rely on for anything scientific",
             "correct": False,
             "why": "Standard masses do not need recalibrating; their "
                    "masses do not change, and the balance simply "
                    "compares them directly."},
            {"text": "No — without knowing the field strength, no mass "
                     "can be measured at all", "correct": False,
             "why": "A pan balance's comparison of mass needs no "
                    "knowledge of the field strength — it cancels out of "
                    "the comparison."},
            {"text": "It would depend on whether the field strength there turns "
                     "out to be stronger or weaker than Earth's own", "correct": False,
             "why": "The pan balance's comparison works the same way "
                    "whatever the field strength happens to be, as long "
                    "as it is the same for both pans."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h16",
        "band": "harder",
        "text": "A 1 kg standard mass and an unknown rock exactly balance "
                "on a pan balance while both sit on a table that is "
                "itself on a large turntable spinning very slowly. Does "
                "the spinning affect whether the comparison is "
                "trustworthy?",
        "options": [
            {"text": "Yes — spinning adds extra outward force to "
                     "whichever side of the balance happens to be moving "
                     "faster at that instant", "correct": False,
             "why": "Spinning this slowly adds a negligible force "
                    "compared with gravity, and in any case it would act "
                    "on both sides in essentially the same way."},
            {"text": "Yes — the rock would appear lighter and lighter the "
                     "faster the turntable is spun", "correct": False,
             "why": "The turntable is described as spinning very slowly, "
                    "which has no meaningful effect on the balance's "
                    "comparison."},
            {"text": "No — spinning slowly does not meaningfully change "
                     "the pull of gravity on either side of the balance",
             "correct": True},
            {"text": "It cannot be known without stopping the turntable "
                     "first", "correct": False,
             "why": "At a slow spin the comparison is trustworthy without "
                    "needing to stop anything."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h17",
        "band": "harder",
        "text": "A newtonmeter reads the weight of a 1 kg mass as exactly "
                "10 N on Earth. The same newtonmeter is later found to "
                "read 10.05 N for the same mass at a different point on "
                "Earth's surface. What is the most likely explanation?",
        "options": [
            {"text": "The newtonmeter must be broken, because Earth's "
                     "field strength never varies at all", "correct": False,
             "why": "Earth's field strength genuinely does vary slightly "
                    "across its surface, so this is not evidence of a "
                    "fault."},
            {"text": "The mass of the 1 kg object must have changed "
                     "slightly", "correct": False,
             "why": "Mass does not fluctuate like this; the small change "
                    "in reading is explained by the field strength, not "
                    "by the object."},
            {"text": "Earth's own field strength varies very slightly "
                     "from place to place — for example with altitude "
                     "and latitude", "correct": True},
            {"text": "1 kg objects always read slightly differently on "
                     "different newtonmeters, regardless of location, "
                     "even when both instruments are freshly checked and "
                     "working perfectly well", "correct": False,
             "why": "Two working newtonmeters at the same location would "
                    "agree; the difference here comes from measuring at "
                    "two different places."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h18",
        "band": "harder",
        "text": "A 40 kg cyclist and their 8 kg bicycle are pedalling "
                "together at a steady speed. To increase their speed as "
                "quickly as possible for a given effort, would it help "
                "more to lose 4 kg of body mass or to swap the bicycle "
                "for one that is 4 kg lighter, everything else staying "
                "the same?",
        "options": [
            {"text": "Neither — a 4 kg reduction has the same effect on "
                     "how quickly they speed up, wherever that mass "
                     "comes from", "correct": True},
            {"text": "Losing body mass helps more, because a rider's own mass "
                     "matters more here than the bicycle's does",
             "correct": False,
             "why": "For speeding up under a given force, it is the "
                    "TOTAL mass of rider and bicycle together that "
                    "matters, not where that mass happens to sit."},
            {"text": "Swapping the bicycle helps more, because a lighter "
                     "bicycle is easier to control", "correct": False,
             "why": "Being easier to control is a separate issue from how "
                    "quickly a given force can speed the whole system up, "
                    "which depends only on the total mass removed."},
            {"text": "It cannot be compared without knowing their "
                     "individual weights, since force calculations always "
                     "need a weight figure to work from", "correct": False,
             "why": "Weight is not needed here — it is the total mass "
                    "being removed that decides the effect on how "
                    "quickly they speed up."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h19",
        "band": "harder",
        "text": "Which of these correctly ranks a 2 kg mass's resistance "
                "to being set moving on Earth, on the Moon, and in deep "
                "space, from most resistant to least resistant?",
        "options": [
            {"text": "Earth, then the Moon, then deep space, because "
                     "gravity provides the resistance", "correct": False,
             "why": "Resistance to being set moving comes from mass, not "
                    "from gravity — the 2 kg is unchanged in all three "
                    "places."},
            {"text": "They resist equally in all three places, because "
                     "resistance to being set moving depends on mass "
                     "alone", "correct": True},
            {"text": "Deep space, then the Moon, then Earth, because "
                     "objects are 'stuck' more firmly where gravity is "
                     "weakest", "correct": False,
             "why": "Nothing about weaker gravity makes an object more "
                    "reluctant to be pushed sideways; that reluctance "
                    "depends only on mass."},
            {"text": "It cannot be ranked without knowing the exact field "
                     "strengths involved", "correct": False,
             "why": "Field strength plays no part in how hard an object "
                    "is to set moving — only its mass does, and that is "
                    "given as 2 kg throughout."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h20",
        "band": "harder",
        "text": "A 90 kg satellite weighs 270 N while orbiting Mars at "
                "altitude. Is Mars's field strength in orbit the same as "
                "at its surface (3.7 N/kg)?",
        "options": [
            {"text": "Yes — a planet's field strength is exactly the "
                     "same at every distance from it, all the way out to "
                     "wherever a satellite happens to orbit",
             "correct": False,
             "why": "270 N ÷ 90 kg gives 3.0 N/kg, not 3.7 N/kg, so the "
                    "two are not actually equal here."},
            {"text": "Yes, because both figures were measured on the "
                     "same planet", "correct": False,
             "why": "Being the same planet does not mean the same field "
                    "strength at every distance — the numbers here show a "
                    "real difference."},
            {"text": "It cannot be compared without knowing the "
                     "satellite's exact orbital speed", "correct": False,
             "why": "The two field strengths can be compared directly "
                    "from the weight and mass figures given, without "
                    "needing the orbital speed at all."},
            {"text": "No — 270 N ÷ 90 kg gives 3.0 N/kg there, weaker "
                     "than the 3.7 N/kg at the surface, because a field "
                     "weakens further from a planet's centre",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h21",
        "band": "harder",
        "text": "Two identical drones, each of mass 2 kg, are flown on "
                "Earth and on the Moon. Both are programmed to accelerate "
                "sideways at exactly the same rate. Do they need the "
                "same sideways thrust from their propellers to do this?",
        "options": [
            {"text": "Yes — the sideways thrust needed for a given rate "
                     "of speeding up depends on mass, which is identical "
                     "for both drones", "correct": True},
            {"text": "No — the Moon drone needs less thrust to speed up "
                     "sideways at the same rate, simply because it weighs "
                     "so much less there than it does back on Earth",
             "correct": False,
             "why": "Sideways thrust for a given rate of speeding up "
                    "depends on mass, not weight; the weaker gravity on "
                    "the Moon plays no part in this sideways motion."},
            {"text": "No — the Earth drone needs less thrust, because the "
                     "Earth's stronger gravity helps push it sideways", "correct": False,
             "why": "Gravity pulls straight down, not sideways, so it "
                    "does not help or hinder sideways acceleration on "
                    "either drone."},
            {"text": "It cannot be compared without knowing each drone's "
                     "exact weight", "correct": False,
             "why": "Weight is not the relevant quantity here — mass is, "
                    "and both drones have the same 2 kg mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h22",
        "band": "harder",
        "text": "A 500 g mass and a 2 kg mass are both dropped from the "
                "same height on the Moon, with nothing to resist their "
                "fall. A student predicts the heavier one will hit the "
                "ground first, 'because it is pulled down harder.' "
                "Evaluate this prediction.",
        "options": [
            {"text": "The prediction is right, because a stronger pull "
                     "on the heavier mass always wins the race to the "
                     "ground, whatever the second mass happens to be and "
                     "wherever the drop takes place", "correct": False,
             "why": "The stronger pull on the heavier mass is exactly "
                    "cancelled by that same mass needing more force to "
                    "accelerate it, so it does not actually fall faster."},
            {"text": "The prediction is right on the Moon specifically, "
                     "though not on Earth", "correct": False,
             "why": "This cancellation between a bigger pull and a "
                    "bigger resistance to accelerating happens in any "
                    "steady gravitational field, the Moon included."},
            {"text": "The prediction is wrong, but only because the Moon "
                     "has almost no gravity at all", "correct": False,
             "why": "The Moon does have a real, non-zero gravitational "
                    "field; the reason both land together is the "
                    "cancellation described, not an absence of gravity."},
            {"text": "The prediction is wrong — a bigger mass is pulled "
                     "down harder, but it also needs proportionally more "
                     "force to speed it up, and the two effects cancel, "
                     "so both land together", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h23",
        "band": "harder",
        "text": "A 20 kg suitcase is weighed with a spring balance and "
                "found to weigh 74 N. On which world was it most likely "
                "weighed, and how confident can you be?",
        "options": [
            {"text": "The Moon, since the reading in newtons is a fairly "
                     "small number", "correct": False,
             "why": "The size of the newton reading alone does not "
                    "identify the world — dividing by the mass gives the "
                    "field strength, which points to Mars here, not the "
                    "Moon."},
            {"text": "Mars, since 74 N ÷ 20 kg gives 3.7 N/kg, matching "
                     "Mars's field strength closely", "correct": True},
            {"text": "Earth, since 74 is a fairly familiar-looking number "
                     "to anyone used to working with newtons",
             "correct": False,
             "why": "74 N ÷ 20 kg gives 3.7 N/kg, nowhere near Earth's "
                    "10 N/kg."},
            {"text": "It cannot be identified from a weight and a mass "
                     "alone", "correct": False,
             "why": "Dividing the weight by the mass gives the field "
                    "strength directly, which can then be matched "
                    "against known values."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h24",
        "band": "harder",
        "text": "A pan balance exactly balances a 250 g standard mass "
                "against an unknown object on Earth. The same pan balance "
                "and the same standard mass are then used to compare the "
                "same unknown object on Jupiter, where gravity is far "
                "stronger. Would the balance still show them as equal?",
        "options": [
            {"text": "Yes — a stronger field always pulls harder on both "
                     "sides of the balance by the same proportion, so "
                     "the comparison is unaffected", "correct": True},
            {"text": "No — the unknown object would now weigh a good "
                     "deal more than the standard mass, simply because "
                     "Jupiter's field is so much stronger", "correct": False,
             "why": "Mass is being compared here, not weight — a "
                    "stronger field affects both sides equally, leaving "
                    "the balance's comparison unaffected."},
            {"text": "No — only lighter objects balance correctly in "
                     "strong gravity", "correct": False,
             "why": "There is no such restriction; a pan balance's "
                    "comparison of mass works the same way in any field "
                    "strength."},
            {"text": "It would depend on how many times stronger Jupiter's "
                     "field turns out to be than Earth's", "correct": False,
             "why": "However much stronger Jupiter's field is, it acts "
                    "on both sides of the balance identically, so the "
                    "comparison still holds."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h25",
        "band": "harder",
        "text": "An engineer designs a device that finds an astronaut's "
                "mass by measuring how hard a spring has to push to "
                "accelerate them by a known amount, and uses the same "
                "calculation whether the device is used on Earth, on the "
                "Moon, or in orbit. Explain why this one calculation "
                "works in all three places, when a pan balance's "
                "calculation would not.",
        "options": [
            {"text": "Because springs are completely unaffected by "
                     "temperature, unlike pan balances, which are said "
                     "to drift badly out of calibration in the extreme "
                     "cold found out in space, far from any star",
             "correct": False,
             "why": "Temperature is not the issue here at all; the "
                    "relevant difference is that one method needs gravity "
                    "to work and the other does not."},
            {"text": "Because the spring method uses mass directly, "
                     "through how much force is needed to accelerate a "
                     "given amount of matter — a relationship that has "
                     "nothing to do with gravity", "correct": True},
            {"text": "Because the spring method actually measures weight, and a "
                     "weight measured with a spring comes out the same "
                     "everywhere, which is what lets one calculation cover all "
                     "three places",
             "correct": False,
             "why": "Weight is not the same everywhere — it is the fact "
                    "that the spring method measures something unrelated "
                    "to gravity that makes it work everywhere."},
            {"text": "Because a pan balance's standard masses become "
                     "inaccurate once they leave Earth", "correct": False,
             "why": "Standard masses do not become inaccurate anywhere; a "
                    "pan balance's real limitation is that it needs "
                    "gravity pulling on both pans to make a comparison at "
                    "all."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h26",
        "band": "harder",
        "text": "A 1 kg mass and a 4 kg mass, both resting on a "
                "frictionless surface, are each given a hard, identical "
                "push. Which travels further in the first second "
                "afterwards, and why?",
        "options": [
            {"text": "The 4 kg mass, because it carries more momentum "
                     "forward once it gets going, and momentum is what "
                     "covers the most ground in a race", "correct": False,
             "why": "Momentum is indeed larger for the heavier mass, but "
                    "the question asks how far it travels from a standing "
                    "start, which depends on how much it speeds up — and "
                    "the lighter mass speeds up more for the same push."},
            {"text": "Neither — a push gives the same result to any "
                     "mass", "correct": False,
             "why": "For the same force, the two masses do not speed up "
                    "by the same amount; the lighter one accelerates "
                    "faster."},
            {"text": "The 1 kg mass — for the same force, a smaller mass "
                     "speeds up more, so it reaches a higher speed and "
                     "covers more ground in the same time",
             "correct": True},
            {"text": "It cannot be decided without knowing their "
                     "weights", "correct": False,
             "why": "Weight plays no part in how an identical sideways "
                    "push affects each mass — only their mass does."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h27",
        "band": "harder",
        "text": "A rock sample exactly balances against three 200 g "
                "standard masses on a pan balance. An astronaut then "
                "reports its 'weight' as 600 g in a mission log. What is "
                "wrong with this statement?",
        "options": [
            {"text": "The number is wrong — a pan balance cannot give an "
                     "accurate reading in grams for any rock sample of "
                     "this kind, however carefully the standard masses "
                     "have been made", "correct": False,
             "why": "A pan balance compares mass directly, and grams are "
                    "a perfectly ordinary unit of mass — the number "
                    "itself is not the problem here."},
            {"text": "Nothing is wrong with the number, but 'weight' is "
                     "the wrong word — 600 g is a mass, found by "
                     "comparison, not a weight", "correct": True},
            {"text": "Nothing is wrong at all — 'weight' and 'mass' can "
                     "be used interchangeably", "correct": False,
             "why": "They are different quantities in different units; "
                    "describing a mass in grams as a 'weight' mixes the "
                    "two up."},
            {"text": "The number is wrong — three 200 g standard masses "
                     "together would only balance an object of exactly 200 g",
             "correct": False,
             "why": "Three 200 g masses together make 600 g, which is "
                    "exactly what balances against the rock — the "
                    "arithmetic in the statement is correct."},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h28",
        "band": "harder",
        "text": "A 1 kg mass weighs 10 N on Earth, 1.6 N on the Moon, and "
                "3.7 N on Mars. A student notices that 10, 1.6 and 3.7 "
                "also happen to be the field strengths of those three "
                "worlds, in N/kg. Is this a coincidence?",
        "options": [
            {"text": "Yes — it happens to work out neatly for these "
                     "three particular worlds, but there is no reason to "
                     "expect it would work out the same way for any "
                     "others", "correct": False,
             "why": "This is not a coincidence limited to three worlds; "
                    "for a 1 kg mass, the weight in newtons always equals "
                    "the field strength in N/kg, on any world."},
            {"text": "No — newtons and N/kg are actually the same unit "
                     "written two different ways", "correct": False,
             "why": "They are genuinely different units for different "
                    "quantities; the numbers only match here because the "
                    "mass happens to be exactly 1 kg."},
            {"text": "It can only be checked by trying it on more "
                     "worlds", "correct": False,
             "why": "It follows directly from W = m × g — with m = 1, W "
                    "and g are always numerically equal, which can be "
                    "seen without testing further worlds."},
            {"text": "No — for exactly 1 kg, the weight in newtons and "
                     "the field strength in N/kg are always numerically "
                     "the same, because W = m × g becomes W = g when "
                     "m = 1", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h29",
        "band": "harder",
        "text": "A 1 kg mass on Earth is compared with a 2 kg mass on "
                "the Moon using two separate pan balances, one on each "
                "world, each against its own local set of standard "
                "masses. Can these two separate results tell you which "
                "of the two objects has more mass?",
        "options": [
            {"text": "No — the two results cannot be compared at all "
                     "because they were measured on completely different "
                     "worlds using entirely separate sets of standard "
                     "masses that were never checked against one another",
             "correct": False,
             "why": "Mass measured by a pan balance means the same thing "
                    "wherever it is measured, so results from different "
                    "worlds can be compared directly."},
            {"text": "No — the Moon's weaker gravity means its 'kilogram' "
                     "stands for a smaller amount of matter than an Earth "
                     "kilogram does, so the two figures are in different units "
                     "and cannot be set side by side", "correct": False,
             "why": "A kilogram is exactly the same amount of matter "
                    "everywhere; gravity does not change what a kilogram "
                    "means."},
            {"text": "It depends on which world's standard masses are "
                     "more accurate", "correct": False,
             "why": "As long as both sets of standard masses are "
                    "correctly made, a kilogram is a kilogram on both "
                    "worlds, so no such adjustment is needed."},
            {"text": "Yes — because a pan balance's comparison of mass "
                     "does not depend on location, a result of 1 kg on "
                     "Earth and 2 kg on the Moon can be compared "
                     "directly, and the Moon object has more mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-02-h30",
        "band": "harder",
        "text": "Which of these correctly explains why doubling an "
                "object's mass doubles its weight in a fixed location, "
                "while doubling its weight by moving it to a stronger "
                "field does not double its mass?",
        "options": [
            {"text": "Both changes double the object's mass, because "
                     "mass and weight always rise and fall together in "
                     "exactly the same way, wherever in the universe the "
                     "object happens to be sitting at the time",
             "correct": False,
             "why": "They only rise and fall together while comparing "
                    "the same object at the same location; moving to a "
                    "stronger field changes only the weight, since mass "
                    "never changes with location."},
            {"text": "Weight is mass multiplied by field strength; "
                     "doubling one factor while the other stays fixed "
                     "doubles the result, but a stronger field never "
                     "changes how much matter the object has",
             "correct": True},
            {"text": "Neither change actually doubles anything, because "
                     "mass and weight are the same quantity",
             "correct": False,
             "why": "They are different quantities in different units; "
                    "changing the mass genuinely does double the weight "
                    "at a fixed location."},
            {"text": "Doubling the mass changes the field strength, "
                     "which is what causes the weight to double",
             "correct": False,
             "why": "Field strength belongs to the place, not to the "
                    "object — changing an object's mass has no effect on "
                    "the field strength wherever it happens to be."},
        ],
        "figure": None,
    },
]
