"""P12 lesson 01 — Gravity and weight: twelve questions (MRB-223).

Written against Design's page. The five places to stand, the W = m × g
triangle and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · weight is a FORCE in newtons; mass is an amount of matter in kilograms;
  · W = m × g, and the g is the one for the place you are standing;
  · a mass in grams has to become kilograms BEFORE it multiplies;
  · weightless is not massless — free fall is the pull continuing while
    nothing pushes back. The harder band sits here.

⚠️ POSITION IS AUTHORED — 2,0,3,1 · 1,3,0,2 · 3,2,1,0, three of each.

⚠️ Neither marked rung is restated: the 24 kg crate and the astronaut in
the station are the ladder's, and nothing here reuses either. Nor does
anything reuse a worked example — the 6 kg toolbox, the 450 g bag of
flour and the 185 kg rover are all off limits.
"""

UNIT = "P12"
LESSON = "gravity-and-weight"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-01-e01",
        "band": "easier",
        "text": "What unit is weight measured in?",
        "options": [
            {"text": "Kilograms", "correct": False,
             "why": "Kilograms measure mass — the amount of matter. Weight "
                    "is a force, and forces are not measured in kilograms."},
            {"text": "Metres", "correct": False,
             "why": "Metres measure length. Weight is a pull, so it needs a "
                    "unit of force."},
            {"text": "Newtons", "correct": True},
            {"text": "Newtons per kilogram", "correct": False,
             "why": "N/kg is the unit of gravitational field strength — the "
                    "pull on EACH kilogram, not the total pull."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e02",
        "band": "easier",
        "text": "On Earth the gravitational field strength is about "
                "10 N/kg. What does that number mean?",
        "options": [
            {"text": "Every kilogram of matter is pulled with about 10 N",
             "correct": True},
            {"text": "Everything on Earth weighs about 10 N", "correct": False,
             "why": "The pull is 10 N on each kilogram, so a heavier object "
                    "is pulled harder. A 50 kg person is pulled with about "
                    "500 N."},
            {"text": "Everything on Earth has a mass of about 10 kg",
             "correct": False,
             "why": "Field strength says nothing about how much matter an "
                    "object has. It says how hard each kilogram of it is "
                    "pulled."},
            {"text": "Gravity makes things fall 10 metres every second",
             "correct": False,
             "why": "N/kg is a force for each kilogram, not a distance. How "
                    "far something falls depends on how long it has been "
                    "falling."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e03",
        "band": "easier",
        "text": "A box has a mass of 8 kg. What is its weight on Earth, "
                "where g = 10 N/kg?",
        "options": [
            {"text": "0.8 N", "correct": False,
             "why": "That is 8 divided by 10. Cover W on the triangle and m "
                    "sits beside g, so the two multiply."},
            {"text": "8 N", "correct": False,
             "why": "That would be right only if each kilogram were pulled "
                    "with 1 N. On Earth each kilogram is pulled with about "
                    "10 N."},
            {"text": "18 N", "correct": False,
             "why": "The mass and the field strength multiply; they are "
                    "never added. Adding two quantities with different units "
                    "gives nothing meaningful."},
            {"text": "80 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e04",
        "band": "easier",
        "text": "Which of these changes when you take an object from Earth "
                "to the Moon?",
        "options": [
            {"text": "Its mass", "correct": False,
             "why": "Mass is the amount of matter in the object, and the "
                    "journey does not remove any of it."},
            {"text": "Its weight", "correct": True},
            {"text": "Both its mass and its weight", "correct": False,
             "why": "Only one of the two changes. The Moon's weaker field "
                    "pulls less hard on exactly the same amount of matter."},
            {"text": "Neither, because it is the same object", "correct": False,
             "why": "It is the same object, and the pull on it is not the "
                    "same. Weight belongs to the object and the place "
                    "together."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-01-s01",
        "band": "standard",
        "text": "A tin has a mass of 2500 g. What is its weight on Earth, "
                "where g = 10 N/kg?",
        "options": [
            {"text": "250 N", "correct": False,
             "why": "That is 2500 divided by 10. The conversion from grams "
                    "to kilograms is the division; the field strength is a "
                    "multiplication."},
            {"text": "25 N", "correct": True},
            {"text": "25 000 N", "correct": False,
             "why": "That is 2500 multiplied by 10 with no conversion. The "
                    "2500 is in grams and N/kg needs kilograms."},
            {"text": "2500 N", "correct": False,
             "why": "The number has not been through the formula at all. "
                    "Convert to 2.5 kg first, then multiply by 10 N/kg."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s02",
        "band": "standard",
        "text": "An object weighs 96 N on a planet where g = 3.2 N/kg. What "
                "is its mass?",
        "options": [
            {"text": "9.6 kg", "correct": False,
             "why": "That divides by 10 rather than by the field strength "
                    "given. Use the g for the planet the reading was taken "
                    "on."},
            {"text": "307 kg", "correct": False,
             "why": "That multiplies where the triangle says divide. Cover m "
                    "and W sits over g."},
            {"text": "96 kg", "correct": False,
             "why": "The number in newtons is not the mass in kilograms. "
                    "They only look similar on Earth, where g happens to be "
                    "about 10."},
            {"text": "30 kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s03",
        "band": "standard",
        "text": "A 60 kg astronaut is on Mars, where g = 3.7 N/kg. What is "
                "their weight there, and what is their mass?",
        "options": [
            {"text": "222 N and 60 kg", "correct": True},
            {"text": "600 N and 60 kg", "correct": False,
             "why": "600 N is the Earth figure. The whole point of the "
                    "question is that the field strength on Mars is 3.7 N/kg, "
                    "not 10."},
            {"text": "222 N and 22.2 kg", "correct": False,
             "why": "The weight is right and the mass is not. Mass is "
                    "unchanged by the journey — it is still 60 kg."},
            {"text": "60 N and 222 kg", "correct": False,
             "why": "The two have been swapped. Weight is the force in "
                    "newtons, and it is the larger number here."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s04",
        "band": "standard",
        "text": "Why do bathroom scales give a reading that is wrong on the "
                "Moon?",
        "options": [
            {"text": "Because a person's mass falls on the Moon and the "
                     "scales cannot detect the change", "correct": False,
             "why": "Mass does not fall. What falls is the force the person "
                    "presses down with."},
            {"text": "Because the spring inside them stretches differently "
                     "in the Moon's weaker field", "correct": False,
             "why": "The spring behaves normally. It stretches less because "
                    "it is being pulled on less, which is exactly what it is "
                    "supposed to do."},
            {"text": "Because the scales measure a force and then divide by "
                     "Earth's field strength to print a mass", "correct": True},
            {"text": "Because the scales are calibrated for the Moon rather "
                     "than for the Earth's field", "correct": False,
             "why": "They are calibrated for the Earth. That is precisely why "
                    "they mislead anywhere else."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-01-h01",
        "band": "harder",
        "text": "An object weighs 45 N on the Moon, where g = 1.6 N/kg. What "
                "would it weigh on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "7.2 N", "correct": False,
             "why": "That multiplies the Moon weight by the Moon's field "
                    "strength. Divide by 1.6 first to get the mass, then "
                    "multiply by 10."},
            {"text": "45 N", "correct": False,
             "why": "Weight changes with field strength. Only the mass is "
                    "the same in both places."},
            {"text": "450 N", "correct": False,
             "why": "That multiplies the Moon WEIGHT by 10. The 10 N/kg "
                    "multiplies a MASS, so the Moon reading has to be turned "
                    "into a mass first."},
            {"text": "281 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h02",
        "band": "harder",
        "text": "A lift cable snaps and the lift falls freely. A passenger "
                "standing on bathroom scales inside it watches the reading. "
                "What happens, and why?",
        "options": [
            {"text": "It stays exactly the same, because the Earth's gravity "
                     "has not changed at all", "correct": False,
             "why": "Gravity has not changed, and the reading still drops. "
                    "The scales measure the push between the person and the "
                    "floor, and there is none."},
            {"text": "It rises, because falling adds to the force the person "
                     "presses down with", "correct": False,
             "why": "Falling removes the push rather than adding to it. "
                    "Nothing is holding the person up any more."},
            {"text": "It drops to zero, because the person and the floor are "
                     "falling together and nothing presses", "correct": True},
            {"text": "It drops to zero, because gravity stops acting on "
                     "anything that is falling freely", "correct": False,
             "why": "Gravity is the reason they are falling. It is acting the "
                    "whole time, which is what makes the fall speed up."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h03",
        "band": "harder",
        "text": "Two students argue about a sack of grain. One says it "
                "'weighs 40 kg'. The other says that is a mistake. What is "
                "the most accurate correction?",
        "options": [
            {"text": "The sack weighs 40 N, not 40 kg", "correct": False,
             "why": "The unit is now a force, but the number has not been "
                    "converted. 40 kg on Earth weighs about 400 N."},
            {"text": "The sack has a mass of 40 kg and weighs about 400 N on "
                     "Earth", "correct": True},
            {"text": "The sack has a weight of 40 kg and a mass of about "
                     "400 N", "correct": False,
             "why": "The units are the wrong way round. Kilograms are for "
                    "mass and newtons are for weight."},
            {"text": "Nothing is wrong, because on Earth the two are the same "
                     "thing", "correct": False,
             "why": "On Earth they are reliably linked, which is not the same "
                    "as being the same thing. One is matter and one is a "
                    "force."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h04",
        "band": "harder",
        "text": "A rock is drifting far from any star, where the field "
                "strength is effectively zero. An astronaut pushes it. What "
                "do they find?",
        "options": [
            {"text": "It resists the push exactly as it would on Earth, "
                     "because its mass is unchanged", "correct": True},
            {"text": "It moves away with almost no effort, because it weighs "
                     "nothing", "correct": False,
             "why": "Weight is what a support has to hold up. Getting "
                    "something moving is set by its mass, and that has not "
                    "changed."},
            {"text": "It cannot be pushed at all, because there is nothing to "
                     "push against", "correct": False,
             "why": "The astronaut pushes the rock and the rock pushes back "
                    "on the astronaut. Both move; neither needs a floor."},
            {"text": "It resists less than on Earth, in proportion to how "
                     "much its weight has fallen", "correct": False,
             "why": "Resistance to being moved tracks mass, not weight, so it "
                    "does not fall at all when the weight does."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-01-e05",
        "band": "easier",
        "text": "What unit is mass measured in?",
        "options": [            {"text": "Newtons", "correct": False,
             "why": "Newtons measure a force, which is what weight is."},
            {"text": "Joules", "correct": False,
             "why": "Joules measure energy, not the amount of matter in "
                    "something."},
            {"text": "Newtons per kilogram", "correct": False,
             "why": "That is the unit of gravitational field strength."},
            {"text": "Kilograms", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e06",
        "band": "easier",
        "text": "Which formula gives an object's weight?",
        "options": [
            {"text": "W = m ÷ g", "correct": False,
             "why": "Dividing would make weight smaller where gravity is "
                    "stronger, which is backwards."},
            {"text": "W = m + g", "correct": False,
             "why": "A mass in kilograms cannot be added to a field strength "
                    "in N/kg."},
            {"text": "W = m × g", "correct": True},
            {"text": "W = g ÷ m", "correct": False,
             "why": "That would make a heavier object weigh less, which "
                    "cannot be right."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e07",
        "band": "easier",
        "text": "A bag has a mass of 5 kg. What is its weight on Earth, where "
                "g = 10 N/kg?",
        "options": [
            {"text": "50 N", "correct": True},
            {"text": "5 N", "correct": False,
             "why": "That is the mass with the unit changed; it still has to "
                    "be multiplied by 10 N/kg."},
            {"text": "0.5 N", "correct": False,
             "why": "That is 5 ÷ 10, dividing where the formula multiplies."},
            {"text": "15 N", "correct": False,
             "why": "That is 5 + 10, and a mass cannot be added to a field "
                    "strength."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e08",
        "band": "easier",
        "text": "The gravitational field strength on the Moon is about…",
        "options": [            {"text": "10 N/kg, the same as Earth", "correct": False,
             "why": "If it were the same, astronauts would not have bounced "
                    "about the way they did."},
            {"text": "24.8 N/kg", "correct": False,
             "why": "That is Jupiter's figure, and it is far stronger than "
                    "Earth's rather than weaker."},
            {"text": "0 N/kg", "correct": False,
             "why": "There is real gravity on the Moon — things fall there, "
                    "just more slowly."},
            {"text": "1.6 N/kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e09",
        "band": "easier",
        "text": "Which of these does NOT change when an object is taken to "
                "the Moon?",
        "options": [
            {"text": "Its weight", "correct": False,
             "why": "Weight is the pull of gravity on it, and the Moon pulls "
                    "far less than the Earth."},
            {"text": "The reading on a spring balance", "correct": False,
             "why": "A spring balance measures the pull, which is much "
                    "smaller there."},
            {"text": "Its mass", "correct": True},
            {"text": "The force needed to lift it", "correct": False,
             "why": "Lifting means overcoming the weight, and the weight has "
                    "fallen."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-01-s05",
        "band": "standard",
        "text": "A case has a mass of 12 kg. What is its weight on the Moon, "
                "where g = 1.6 N/kg?",
        "options": [
            {"text": "19.2 N", "correct": True},
            {"text": "7.5 N", "correct": False,
             "why": "That is 12 ÷ 1.6, dividing where the formula "
                    "multiplies."},
            {"text": "120 N", "correct": False,
             "why": "That uses Earth's 10 N/kg rather than the Moon's 1.6."},
            {"text": "13.6 N", "correct": False,
             "why": "That adds the two, and kilograms cannot be added to "
                    "N/kg."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s06",
        "band": "standard",
        "text": "An object weighs 120 N on a world where g = 4.0 N/kg. What "
                "is its mass?",
        "options": [            {"text": "480 kg", "correct": False,
             "why": "That is 120 × 4.0; to find a mass you divide the weight "
                    "by the field strength."},
            {"text": "116 kg", "correct": False,
             "why": "That subtracts, and a field strength cannot be taken "
                    "from a force."},
            {"text": "12 kg", "correct": False,
             "why": "That uses Earth's 10 N/kg rather than the 4.0 N/kg "
                    "given."},
            {"text": "30 kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s07",
        "band": "standard",
        "text": "A book has a mass of 0.50 kg. What is its weight on Earth, "
                "where g = 10 N/kg?",
        "options": [            {"text": "0.05 N", "correct": False,
             "why": "That is 0.50 ÷ 10, a division where the formula "
                    "multiplies."},
            {"text": "10.5 N", "correct": False,
             "why": "That adds the two quantities, which cannot be done."},
            {"text": "0.50 N", "correct": False,
             "why": "That is the mass with the unit swapped; the 10 N/kg has "
                    "not been used."},
            {"text": "5.0 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s08",
        "band": "standard",
        "text": "Bathroom scales measure a force but display a mass in "
                "kilograms. How?",
        "options": [            {"text": "They measure the mass directly and show it",
             "correct": False,
             "why": "What presses on them is a force; the mass is worked out "
                    "from it."},
            {"text": "They compare you with a known mass inside them",
             "correct": False,
             "why": "That is what a pan balance does, and it would work "
                    "anywhere."},
            {"text": "They multiply the force by Earth's field strength",
             "correct": False,
             "why": "Multiplying would give a far larger number and the wrong "
                    "unit."},
            {"text": "They divide the force by Earth's field strength, which "
                     "they assume",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s09",
        "band": "standard",
        "text": "A 70 kg astronaut stands on Jupiter, where g = 24.8 N/kg. "
                "What is their weight?",
        "options": [
            {"text": "1736 N", "correct": True},
            {"text": "700 N", "correct": False,
             "why": "That uses Earth's 10 N/kg instead of Jupiter's 24.8."},
            {"text": "2.8 N", "correct": False,
             "why": "That is 70 ÷ 24.8, dividing where the formula "
                    "multiplies."},
            {"text": "94.8 N", "correct": False,
             "why": "That adds the two, and kilograms cannot be added to "
                    "N/kg."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-01-h05",
        "band": "harder",
        "text": "An object weighs 37 N on Mars, where g = 3.7 N/kg. What "
                "would it weigh on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "37 N, because weight is a property of the object",
             "correct": False,
             "why": "Weight changes with where you are; only the mass stays "
                    "put."},
            {"text": "3.7 N", "correct": False,
             "why": "That is the field strength read as a weight, with no "
                    "calculation done."},
            {"text": "100 N", "correct": True},
            {"text": "370 N", "correct": False,
             "why": "That multiplies the Mars weight by 10 instead of finding "
                    "the mass first."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h06",
        "band": "harder",
        "text": "A sack is described as weighing 40 kg. What are the two "
                "correct statements about it on Earth?",
        "options": [            {"text": "Its mass is 40 N and its weight is 400 kg",
             "correct": False,
             "why": "The units are the wrong way round: mass is in kilograms "
                    "and weight in newtons."},
            {"text": "Its mass is 4 kg and its weight is 40 N",
             "correct": False,
             "why": "The 40 in the everyday phrase is the mass in kilograms, "
                    "not a tenth of it."},
            {"text": "Its mass and its weight are both 40, in different "
                     "units",
             "correct": False,
             "why": "Each kilogram weighs about 10 N, so the two numbers "
                    "cannot match."},
            {"text": "Its mass is 40 kg and its weight is about 400 N",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h07",
        "band": "harder",
        "text": "Why would a spring balance calibrated on Earth read too "
                "little on Mars?",
        "options": [            {"text": "Because the object loses mass on the way there",
             "correct": False,
             "why": "Mass never changes; it is the pull on it that does."},
            {"text": "Because Mars is further from the Sun", "correct": False,
             "why": "The Sun's pull on a hand-held object is negligible; "
                    "Mars's own field is what matters."},
            {"text": "Because springs are weaker in the cold of Mars",
             "correct": False,
             "why": "Temperature effects are tiny next to the difference in "
                    "gravity."},
            {"text": "Because Mars pulls less hard, so the spring stretches "
                     "less",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h08",
        "band": "harder",
        "text": "Can two objects on Earth have the same weight but different "
                "masses?",
        "options": [
            {"text": "Yes, if one is denser than the other", "correct": False,
             "why": "Density changes the size of an object, not the "
                    "relationship between its mass and its weight."},
            {"text": "Yes, if one is higher above the ground", "correct": False,
             "why": "The change over any everyday height is far too small to "
                    "matter."},
            {"text": "No — in the same field, weight is always mass × g",
             "correct": True},
            {"text": "No, because weight and mass are the same quantity",
             "correct": False,
             "why": "They are different quantities in different units; they "
                    "are simply linked by g."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h09",
        "band": "harder",
        "text": "A 1 kg mass is taken to a planet where it weighs 25 N. What "
                "is the field strength there?",
        "options": [
            {"text": "25 N/kg", "correct": True},
            {"text": "10 N/kg, as on Earth", "correct": False,
             "why": "On Earth that mass would weigh 10 N, and here it weighs "
                    "25 N."},
            {"text": "0.04 N/kg", "correct": False,
             "why": "That is 1 ÷ 25, the division the wrong way round."},
            {"text": "26 N/kg", "correct": False,
             "why": "That adds the mass on, and kilograms cannot be added to "
                    "newtons."},
        ],
        "figure": None,
    },
]
