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

⚠️ MRB-338 night 3 top-up (e10–e30, s10–s30, h10–h30): 21 more per band,
continuing each band's id sequence. Coverage, self-checks and content
decisions are in the executor's final report for this run.
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

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p12-01-e10",
        "band": "easier",
        "text": "What does the letter 'W' stand for in the formula "
                "W = m × g?",
        "options": [
            {"text": "Watts, the unit weight is measured in", "correct": False,
             "why": "Weight is measured in newtons, not watts. Watts measure "
                    "power, a completely different quantity."},
            {"text": "Work done in lifting the object", "correct": False,
             "why": "Work needs a distance moved as well as a force; the "
                    "formula W = m × g does not involve any movement at all."},
            {"text": "Weight — the force gravity pulls with", "correct": True},
            {"text": "Width of the object being weighed", "correct": False,
             "why": "The formula has nothing to do with the size or shape of "
                    "the object, only its mass and the field it is in."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e11",
        "band": "easier",
        "text": "What happens, physically, when you multiply an object's "
                "mass by the gravitational field strength it is sitting in?",
        "options": [
            {"text": "You get the distance it would fall in one second",
             "correct": False,
             "why": "A field strength in N/kg is a force for each kilogram, "
                    "not a distance, so multiplying gives a force rather "
                    "than a fall distance."},
            {"text": "You get its mass expressed in a different unit",
             "correct": False,
             "why": "Multiplying by g does not just rescale the same "
                    "quantity — it produces a genuinely different physical "
                    "quantity, a force."},
            {"text": "You get the density of the object", "correct": False,
             "why": "Density needs a volume as well; nothing about "
                    "mass × g involves how much space the object takes up."},
            {"text": "You get its weight, in newtons", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e12",
        "band": "easier",
        "text": "Which of these quantities is measured as a force?",
        "options": [
            {"text": "The volume of a liquid", "correct": False,
             "why": "Volume is measured in cubic centimetres or litres, not "
                    "in a unit of force."},
            {"text": "An object's weight", "correct": True},
            {"text": "An object's mass", "correct": False,
             "why": "Mass is measured in kilograms, a different quantity from "
                    "a force."},
            {"text": "The temperature of a room", "correct": False,
             "why": "Temperature is measured in degrees Celsius and has "
                    "nothing to do with a pull or a push."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e13",
        "band": "easier",
        "text": "Which rearrangement of W = m × g gives the mass on its own?",
        "options": [
            {"text": "m = W × g", "correct": False,
             "why": "Multiplying both sides by g again is not how the "
                    "triangle rearranges the formula."},
            {"text": "m = g ÷ W", "correct": False,
             "why": "That divides the field strength by the weight, which is "
                    "the two the wrong way round."},
            {"text": "m = W + g", "correct": False,
             "why": "A force in newtons and a field strength in N/kg cannot "
                    "be added together."},
            {"text": "m = W ÷ g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e14",
        "band": "easier",
        "text": "A helium balloon floats upward when released indoors. Does "
                "gravity still act on it?",
        "options": [
            {"text": "No — objects that float upward are not affected by "
                     "gravity", "correct": False,
             "why": "Gravity still pulls the balloon down; if it stopped "
                    "acting once the balloon rose, a leaking balloon could "
                    "never sink back down again."},
            {"text": "No — helium cancels out gravity for anything it lifts",
             "correct": False,
             "why": "Helium does not switch gravity off; it simply provides "
                    "an upward push bigger than the balloon's own weight."},
            {"text": "Yes — gravity pulls it down, and something else is "
                     "pushing up harder", "correct": True},
            {"text": "Yes, but only until the balloon leaves the ground",
             "correct": False,
             "why": "Gravity keeps acting on the balloon at every height, "
                    "not only while it is still touching the ground."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e15",
        "band": "easier",
        "text": "Which of these locations has the strongest gravitational "
                "field?",
        "options": [
            {"text": "The Moon, at 1.6 N/kg", "correct": False,
             "why": "That is the weakest of the four figures given here."},
            {"text": "Earth, at 10 N/kg", "correct": False,
             "why": "Jupiter's field is stronger still."},
            {"text": "Mars, at 3.7 N/kg", "correct": False,
             "why": "Both Earth and Jupiter pull harder than this."},
            {"text": "Jupiter, at 24.8 N/kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e16",
        "band": "easier",
        "text": "Which of these has the weakest gravitational field?",
        "options": [
            {"text": "Mars, at 3.7 N/kg, the weakest of the four figures here", "correct": False,
             "why": "Only one of the other three — deep space — pulls less hard "
                    "than Mars."},
            {"text": "Deep space, where the field strength is effectively "
                     "zero", "correct": True},
            {"text": "Earth, at 10 N/kg", "correct": False,
             "why": "This is stronger than every other field given here "
                    "except Jupiter's."},
            {"text": "Jupiter, where the field strength is stronger than "
                     "any other place listed here, at 24.8 N/kg",
             "correct": False,
             "why": "This is the strongest of the four given here."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e17",
        "band": "easier",
        "text": "A 12 kg case is flown from Earth to Mars. What is its mass on "
                "arrival?",
        "options": [
            {"text": "12 kg", "correct": True},
            {"text": "44.4 kg", "correct": False,
             "why": "That multiplies the mass by Mars's field strength, which "
                    "would change the weight, not the mass."},
            {"text": "3.2 kg", "correct": False,
             "why": "Mass does not change at all on the journey — this "
                    "divides by Mars's field strength for no reason."},
            {"text": "1.2 kg", "correct": False,
             "why": "That divides by 10, which is not something the mass "
                    "ever does."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e18",
        "band": "easier",
        "text": "Which of these correctly defines mass?",
        "options": [
            {"text": "The amount of matter something is made of",
             "correct": True},
            {"text": "How heavy something feels when you lift it",
             "correct": False,
             "why": "How heavy something feels is its weight, which changes "
                    "with location; mass does not."},
            {"text": "The force pulling an object towards a planet",
             "correct": False,
             "why": "That describes weight, not mass."},
            {"text": "The space an object takes up", "correct": False,
             "why": "That is volume, a different quantity measured in a "
                    "different unit."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e19",
        "band": "easier",
        "text": "Which of these correctly defines weight?",
        "options": [
            {"text": "The amount of matter in an object", "correct": False,
             "why": "That is mass, measured in kilograms rather than "
                    "newtons."},
            {"text": "How much space an object occupies", "correct": False,
             "why": "That is volume."},
            {"text": "How reluctant an object is to start moving when a "
                     "force is applied to it", "correct": False,
             "why": "That describes mass acting as inertia, not weight."},
            {"text": "The force of gravity pulling on an object's mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e20",
        "band": "easier",
        "text": "Two rocks, one 2 kg and one 200 kg, lie side by side on "
                "the surface of Mars. What gravitational field strength "
                "acts on each of them?",
        "options": [
            {"text": "3.7 N/kg on both, because a field strength belongs "
                     "to the place", "correct": True},
            {"text": "3.7 N/kg on the small rock and a far larger figure "
                     "on the large one", "correct": False,
             "why": "Field strength does not grow with an object's mass. "
                    "The large rock's far greater WEIGHT comes from "
                    "multiplying that same 3.7 N/kg by its bigger mass."},
            {"text": "10 N/kg on both, because that is the figure used "
                     "for every rocky planet there is", "correct": False,
             "why": "10 N/kg is Earth's figure. Mars pulls each kilogram "
                    "with about 3.7 N instead."},
            {"text": "Nothing at all, because a field strength only acts "
                     "on objects that are moving", "correct": False,
             "why": "A field strength acts on a resting object just as "
                    "much as a moving one; both rocks are being pulled "
                    "while they lie still."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e21",
        "band": "easier",
        "text": "Weight = mass × gravitational field strength, or W = m × g. "
                "Which equation gives g?",
        "options": [
            {"text": "g = W × m",
             "correct": False,
             "why": "Multiplying by m makes the number bigger still. To undo "
                    "× m, divide by m."},
            {"text": "g = m ÷ W",
             "correct": False,
             "why": "That has the division the wrong way round. It is W that "
                    "is divided by m."},
            {"text": "g = W + m",
             "correct": False,
             "why": "A force and a mass cannot be added together, and "
                    "nothing in W = m × g is added."},
            {"text": "g = W ÷ m",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e22",
        "band": "easier",
        "text": "A 5 kg toy is taken far out into deep space, where the field "
                "strength is effectively zero. What is its mass there?",
        "options": [
            {"text": "0 kg, because there is no gravity to give it mass",
             "correct": False,
             "why": "Mass is not created by gravity; the toy is made of "
                    "exactly the same matter it always was."},
            {"text": "5 kg", "correct": True},
            {"text": "0.5 kg", "correct": False,
             "why": "That divides by 10 for no reason; mass never depends on "
                    "a field strength."},
            {"text": "50 kg", "correct": False,
             "why": "That multiplies by 10; mass simply does not change with "
                    "location."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e23",
        "band": "easier",
        "text": "A 1 kg mass is weighed on Earth, on the Moon and on Jupiter. "
                "On which of the three is its weight the smallest?",
        "options": [
            {"text": "Jupiter", "correct": False,
             "why": "Jupiter's field is the strongest of the three, so the "
                    "weight there is the largest, not the smallest."},
            {"text": "The Moon", "correct": True},
            {"text": "Earth", "correct": False,
             "why": "Earth's field is stronger than the Moon's, so the "
                    "weight there is bigger."},
            {"text": "It is the same on all three, because the mass never "
                     "changes", "correct": False,
             "why": "The mass is the same on all three, but the weight is "
                    "not — weight also depends on the field strength."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e24",
        "band": "easier",
        "text": "Which statement about units is correct?",
        "options": [
            {"text": "Newtons measure mass and kilograms measure weight",
             "correct": False,
             "why": "The pairing is the wrong way round."},
            {"text": "Newtons per kilogram measures the same thing as "
                     "newtons", "correct": False,
             "why": "N/kg is a field strength, a different quantity from a "
                    "force measured in N."},
            {"text": "Kilograms measure weight and newtons measure "
                     "gravitational field strength", "correct": False,
             "why": "Neither pairing is right: kilograms measure mass and "
                    "newtons measure a force."},
            {"text": "Newtons measure weight and kilograms measure mass",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e25",
        "band": "easier",
        "text": "Which of these is the gravitational field strength at "
                "Earth's surface?",
        "options": [
            {"text": "1.6 N/kg", "correct": False,
             "why": "That is the Moon's figure."},
            {"text": "About 10 N/kg", "correct": True},
            {"text": "24.8 N/kg", "correct": False,
             "why": "That is Jupiter's figure, far stronger than Earth's."},
            {"text": "3.7 N/kg", "correct": False,
             "why": "That is Mars's figure."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e26",
        "band": "easier",
        "text": "What does a gravitational field strength of 24.8 N/kg tell "
                "you?",
        "options": [
            {"text": "Every kilogram of matter there is pulled with about "
                     "24.8 N", "correct": True},
            {"text": "Every object there has a mass of 24.8 kg, whatever it is "
                     "made of",
             "correct": False,
             "why": "Field strength says nothing about how much matter an "
                    "object has."},
            {"text": "Objects there fall a distance of 24.8 metres during "
                     "the first second alone", "correct": False,
             "why": "N/kg is a force for each kilogram, not a distance "
                    "fallen."},
            {"text": "Objects there weigh 24.8 kg", "correct": False,
             "why": "Weight is measured in newtons, not kilograms."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e27",
        "band": "easier",
        "text": "In which direction does an object's weight act?",
        "options": [
            {"text": "Sideways, along the ground", "correct": False,
             "why": "Gravity pulls towards the centre of whatever is doing "
                    "the pulling, not sideways."},
            {"text": "Away from the centre of whatever is pulling on it",
             "correct": False,
             "why": "Gravity is an attraction, so it pulls objects towards "
                    "the centre of the pulling body, not away from it."},
            {"text": "Towards the centre of whatever is pulling on it",
             "correct": True},
            {"text": "In whichever direction the object happens to be "
                     "moving", "correct": False,
             "why": "Weight does not depend on how the object is moving; it "
                    "always points towards the pulling body."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e28",
        "band": "easier",
        "text": "A newton is the unit used to measure which quantity?",
        "options": [
            {"text": "Force", "correct": True},
            {"text": "Mass", "correct": False,
             "why": "Mass is measured in kilograms."},
            {"text": "Distance", "correct": False,
             "why": "Distance is measured in metres."},
            {"text": "Gravitational field strength", "correct": False,
             "why": "Field strength is measured in newtons per kilogram, not "
                    "newtons alone."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e29",
        "band": "easier",
        "text": "Which of these is closest to the gravitational field "
                "strength at Jupiter's cloud tops?",
        "options": [
            {"text": "10 N/kg", "correct": False,
             "why": "That is Earth's figure."},
            {"text": "1.6 N/kg", "correct": False,
             "why": "That is the Moon's figure, far weaker than Jupiter's."},
            {"text": "3.7 N/kg", "correct": False,
             "why": "That is Mars's figure."},
            {"text": "24.8 N/kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-e30",
        "band": "easier",
        "text": "Two identical bags of flour sit on tables — one on Earth, "
                "one on the Moon. Which statement about them is true?",
        "options": [
            {"text": "They have different masses, because the Moon is "
                     "smaller than Earth", "correct": False,
             "why": "Mass is about how much matter each bag contains, not "
                    "about the size of the planet it happens to sit on."},
            {"text": "They have the same weight, because they are identical "
                     "bags", "correct": False,
             "why": "Being identical bags gives them the same mass; their "
                    "weight still depends on the different field strengths "
                    "of the two places."},
            {"text": "They have the same mass but different weights",
             "correct": True},
            {"text": "They have different masses and different weights",
             "correct": False,
             "why": "Only one of the two quantities changes between the "
                    "bags — the mass stays exactly the same."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p12-01-s10",
        "band": "standard",
        "text": "A parcel is weighed on Earth and gives a reading of 40 N. "
                "The same parcel is then weighed on a moon with exactly "
                "half of Earth's field strength. What would the new "
                "reading be?",
        "options": [
            {"text": "20 N", "correct": True},
            {"text": "40 N", "correct": False,
             "why": "Weight changes when the field strength changes; it "
                    "will not stay the same once the field strength halves."},
            {"text": "80 N", "correct": False,
             "why": "Halving the field strength halves the weight; this "
                    "doubles it instead."},
            {"text": "4 N", "correct": False,
             "why": "That divides by ten rather than by two."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s11",
        "band": "standard",
        "text": "A satellite dish has a mass of 45 kg. It is installed on a "
                "research base on Mars, where g = 3.7 N/kg. What is its "
                "weight there?",
        "options": [
            {"text": "450 N", "correct": False,
             "why": "That uses Earth's 10 N/kg rather than Mars's 3.7."},
            {"text": "12.2 kg", "correct": False,
             "why": "That divides instead of multiplying, and gives the "
                    "wrong unit besides."},
            {"text": "166.5 N", "correct": True},
            {"text": "48.7 N", "correct": False,
             "why": "That adds the mass and the field strength, which cannot "
                    "be done because they are different kinds of quantity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s12",
        "band": "standard",
        "text": "A cyclist's helmet has a small enough mass that its weight "
                "on Earth is 4.5 N. Roughly what would you expect its "
                "weight to be on the Moon, where the field is about a "
                "sixth of Earth's?",
        "options": [
            {"text": "About 0.75 N", "correct": True},
            {"text": "About 4.5 N", "correct": False,
             "why": "Weight changes when the field strength changes; a "
                    "sixth of the field will not leave the reading the "
                    "same."},
            {"text": "About 27 N", "correct": False,
             "why": "That multiplies by six instead of dividing by six."},
            {"text": "About 0.075 N", "correct": False,
             "why": "That divides by sixty rather than by six."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s13",
        "band": "standard",
        "text": "A block of ice has a mass of 2 kg. Some of it melts and "
                "evaporates, leaving a mass of 1.5 kg. What happens to its "
                "weight on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "It falls from 20 N to 19.5 N", "correct": False,
             "why": "That subtracts the 0.5 kg of mass lost straight off "
                    "the weight in newtons, rather than multiplying the "
                    "new mass by g."},
            {"text": "It falls from 20 N to 15 N", "correct": True},
            {"text": "It stays at 20 N, because weight does not depend on "
                     "how much has evaporated", "correct": False,
             "why": "Weight is mass × g, so genuinely losing mass reduces "
                    "the weight."},
            {"text": "It rises, because evaporating releases energy",
             "correct": False,
             "why": "Releasing energy does not add matter; losing mass can "
                    "only reduce the weight, never raise it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s14",
        "band": "standard",
        "text": "A 40 kg sack of grain is split exactly in half. What "
                "happens to the total weight of the grain on Earth?",
        "options": [
            {"text": "It falls to a quarter of the original weight",
             "correct": False,
             "why": "Splitting a mass in half removes no matter overall; "
                    "the combined weight of the two halves is unchanged."},
            {"text": "It stays the same, because no matter has been "
                     "removed", "correct": True},
            {"text": "It halves, because each half is lighter on its own",
             "correct": False,
             "why": "Each half does weigh less by itself, but added "
                    "together the two halves still weigh exactly what the "
                    "whole sack did."},
            {"text": "It doubles, because there are now two separate "
                     "objects", "correct": False,
             "why": "Creating two objects out of one does not create any "
                    "new matter, and so cannot create any new weight."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s15",
        "band": "standard",
        "text": "An astronaut's mass is 75 kg on Earth. Which statement "
                "about their mass in orbit, several hundred kilometres up, "
                "is correct?",
        "options": [
            {"text": "Their mass is still 75 kg", "correct": True},
            {"text": "Their mass has fallen to almost nothing, which is why "
                     "they float", "correct": False,
             "why": "Their mass is unchanged; they float because they and "
                    "their spacecraft are falling together, not because "
                    "their mass has changed."},
            {"text": "Their mass has increased slightly because of the "
                     "speed of the orbit", "correct": False,
             "why": "Orbital speeds here are far too slow for any such "
                    "effect to matter, and orbiting adds no matter to a "
                    "person in any case."},
            {"text": "Their mass cannot be measured at all once they leave "
                     "the ground", "correct": False,
             "why": "Mass can still be measured in orbit — for example "
                    "from how hard a known push accelerates them."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s16",
        "band": "standard",
        "text": "Explain why a 20 kg dog has the same mass on Mars as it does "
                "on Earth, even though its weight is different there.",
        "options": [
            {"text": "Because Mars's gravity happens to give the same "
                     "reading", "correct": False,
             "why": "Mass does not depend on gravity at all; it would be "
                    "unchanged even if the field strength there were "
                    "completely different."},
            {"text": "Mass is the amount of matter in the dog, and the "
                     "journey does not add or remove any of it",
             "correct": True},
            {"text": "The dog's weight also stays the same, so its mass "
                     "must too", "correct": False,
             "why": "The dog's weight does change — Mars's field is "
                    "3.7 N/kg, not 10 — so this reasoning starts from "
                    "something false."},
            {"text": "Scales on Mars are calibrated to give exactly the "
                     "same number as scales built for use on Earth",
             "correct": False,
             "why": "That is a coincidence of the instrument, not a physical "
                    "reason connected to what mass actually is."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s17",
        "band": "standard",
        "text": "A 90 kg piece of equipment is moved from Earth to Jupiter, "
                "where g = 24.8 N/kg. By roughly what factor does its weight "
                "increase?",
        "options": [
            {"text": "By ten times", "correct": False,
             "why": "That would be true only if Jupiter's field strength "
                    "were 100 N/kg."},
            {"text": "It does not change, because the equipment is "
                     "unchanged", "correct": False,
             "why": "The equipment's mass is unchanged, but its weight "
                    "depends on the field strength, and Jupiter's is much "
                    "stronger than Earth's."},
            {"text": "By about six times", "correct": False,
             "why": "That is closer to the factor for the Moon's field "
                    "being weaker, not for Jupiter's being stronger."},
            {"text": "By about two and a half times", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s18",
        "band": "standard",
        "text": "A 20 kg crate is lifted from the ground on Earth to the top "
                "of a tall crane, well within the atmosphere. What happens "
                "to its weight?",
        "options": [
            {"text": "It falls to zero, because the crate is no longer "
                     "touching the ground", "correct": False,
             "why": "Weight is the pull of gravity, which does not depend "
                    "on whether the object is touching the ground."},
            {"text": "It roughly doubles, because height always weakens "
                     "gravity by a lot", "correct": False,
             "why": "Gravity does weaken slightly with height, but not by "
                    "anything like a factor of two over the height of a "
                    "crane."},
            {"text": "It falls very slightly, because gravity weakens a "
                     "little further from the Earth's centre",
             "correct": True},
            {"text": "It stays exactly the same, because gravity is "
                     "identical everywhere near the Earth's surface",
             "correct": False,
             "why": "Gravity does weaken, very slightly, with height; it is "
                    "not perfectly identical at every distance from the "
                    "surface."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s19",
        "band": "standard",
        "text": "A 500 kg satellite is assembled on Earth, and engineers "
                "still need to know its mass precisely once it reaches "
                "orbit. Why can they not just use a set of bathroom "
                "scales?",
        "options": [
            {"text": "Because bathroom scales rely on a weight pressing "
                     "down on them, and nothing presses down in orbit",
             "correct": True},
            {"text": "Because bathroom scales only work for masses under "
                     "about 150 kg", "correct": False,
             "why": "The limit on ordinary bathroom scales is about the "
                    "weight range they can read, not about whether they "
                    "are in orbit; the real problem is that nothing "
                    "presses on them there."},
            {"text": "Because a satellite's mass keeps changing slightly as it "
                     "goes round, so no scale could settle", "correct": False,
             "why": "The satellite's mass does not change simply because "
                    "it is going round the Earth."},
            {"text": "Because ordinary bathroom scales can never be "
                     "calibrated properly for use in a region of zero "
                     "gravity out in orbit", "correct": False,
             "why": "There is not zero gravity in orbit — the field is "
                    "still close to 90% of its surface value; what is "
                    "missing is anything pressing down for the scale to "
                    "read."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s20",
        "band": "standard",
        "text": "A cyclist and their bike have a combined mass of 85 kg. "
                "What is their combined weight on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "8.5 N", "correct": False,
             "why": "That divides by 10 where the formula multiplies."},
            {"text": "95 N", "correct": False,
             "why": "That adds the two quantities, which cannot be done."},
            {"text": "8500 N", "correct": False,
             "why": "That is ten times too large — the mass has effectively "
                    "been multiplied by 100 rather than by 10."},
            {"text": "850 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s21",
        "band": "standard",
        "text": "Why does a 2 kg mass weigh less on Mars than it does on "
                "Earth?",
        "options": [
            {"text": "Because 2 kg of matter is less on Mars than it is on "
                     "Earth", "correct": False,
             "why": "Mass is unchanged wherever the object is taken."},
            {"text": "Because Mars is further from the Sun, which weakens "
                     "gravity everywhere", "correct": False,
             "why": "What matters is Mars's own gravitational field, not its "
                    "distance from the Sun."},
            {"text": "Because the mass is measured with a different "
                     "instrument on Mars", "correct": False,
             "why": "The instrument does not change the physics; the field "
                    "strength genuinely is weaker there."},
            {"text": "Because Mars's gravitational field strength is weaker "
                     "than Earth's", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s22",
        "band": "standard",
        "text": "A 10 kg object weighs 50 N on one world, where the field "
                "strength is 5 N/kg. On a second world its weight is "
                "exactly double that. What is the second world's field "
                "strength?",
        "options": [
            {"text": "2.5 N/kg", "correct": False,
             "why": "That would HALVE the weight, not double it."},
            {"text": "20 N/kg", "correct": False,
             "why": "That would give a weight of 200 N — four times the "
                    "original, not double it."},
            {"text": "10 N/kg", "correct": True},
            {"text": "15 N/kg", "correct": False,
             "why": "That gives a weight of 150 N, three times the "
                    "original, not double it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s23",
        "band": "standard",
        "text": "A student says: 'A heavier object always has a bigger mass "
                "than a lighter one.' Is this a safe rule?",
        "options": [
            {"text": "Yes, because weight and mass always increase and "
                     "decrease together, in any two objects you could name",
             "correct": False,
             "why": "They only rise and fall together while comparing "
                    "objects in the SAME place — the rule breaks down "
                    "comparing objects in different fields."},
            {"text": "No — comparing weight only tells you about mass "
                     "reliably when both objects are in the same "
                     "gravitational field", "correct": True},
            {"text": "Yes, because weight is just another name for mass",
             "correct": False,
             "why": "They are different quantities in different units, "
                    "connected by the field strength rather than being "
                    "identical."},
            {"text": "No, because weight and mass are unrelated to each "
                     "other", "correct": False,
             "why": "In a fixed field, weight is exactly proportional to "
                    "mass — they are related, just not identical."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s24",
        "band": "standard",
        "text": "A model rocket has a mass of 3 kg. Its fuel burns away "
                "during flight, leaving a mass of 2 kg by the time it "
                "lands. Which statement about its weight on Earth is "
                "correct?",
        "options": [
            {"text": "Its weight is unchanged at 30 N throughout, because "
                     "weight belongs to the rocket alone", "correct": False,
             "why": "Weight depends on mass as well as field strength; "
                    "losing mass genuinely changes the weight."},
            {"text": "Its weight rises as it burns fuel, because burning "
                     "releases energy", "correct": False,
             "why": "Releasing energy does not add mass; losing mass can "
                    "only reduce weight, never raise it."},
            {"text": "Its weight is 30 N throughout, because mass lost as "
                     "gas does not count", "correct": False,
             "why": "Any mass that leaves the rocket, gas included, is "
                    "mass no longer being pulled on by gravity as part of "
                    "the rocket."},
            {"text": "Its weight falls from 30 N to 20 N as it burns fuel",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s25",
        "band": "standard",
        "text": "A 60 kg diver's mass is unaffected by being underwater. "
                "Which of these is also true about their weight while "
                "fully submerged in a swimming pool on Earth?",
        "options": [
            {"text": "Their weight is still about 600 N — gravity does not "
                     "stop pulling on someone just because they are in "
                     "water", "correct": True},
            {"text": "Their weight falls to zero, because the water "
                     "supports all of it", "correct": False,
             "why": "Water can push up on the diver, but that upthrust is "
                    "a separate force from gravity — gravity is still "
                    "pulling with the full 600 N throughout."},
            {"text": "Their weight becomes negative, because the water "
                     "pushes them upward", "correct": False,
             "why": "Weight is not a quantity that can become negative; "
                    "upthrust is a separate, additional force acting "
                    "alongside it."},
            {"text": "Their weight falls in proportion to how deep under "
                     "the surface of the pool they happen to be swimming",
             "correct": False,
             "why": "Gravity's pull on the diver does not depend "
                    "meaningfully on depth in a swimming pool; what "
                    "changes with depth is water pressure, a different "
                    "quantity."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s26",
        "band": "standard",
        "text": "A 500 g instrument is carried up on a research drone, where "
                "the field strength is still very close to Earth's "
                "10 N/kg. What is its approximate weight there?",
        "options": [
            {"text": "500 N", "correct": False,
             "why": "No conversion from grams to kilograms has been done."},
            {"text": "50 N", "correct": False,
             "why": "That converts 500 g by dividing by 100 instead of "
                    "by 1000, giving 5 kg."},
            {"text": "0.5 N", "correct": False,
             "why": "The mass has been converted correctly to 0.5 kg but "
                    "then divided instead of multiplied."},
            {"text": "5 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s27",
        "band": "standard",
        "text": "A 500 kg weather satellite is steered using small thruster "
                "bursts rather than by pushing against anything. Which "
                "quantity of the satellite decides how much its speed "
                "changes for a given thruster burst?",
        "options": [
            {"text": "Its weight", "correct": False,
             "why": "Weight is the pull of gravity, which plays no part in "
                    "how hard a thruster has to work to change the "
                    "satellite's speed."},
            {"text": "Its volume", "correct": False,
             "why": "How much space the satellite takes up says nothing "
                    "about how reluctant it is to speed up or slow down."},
            {"text": "Its mass", "correct": True},
            {"text": "The gravitational field strength where it currently "
                     "is", "correct": False,
             "why": "Field strength affects weight, not how the satellite "
                    "responds to being pushed by its own engines."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s28",
        "band": "standard",
        "text": "A rock sample weighs 259 N on Jupiter, where g = 24.8 N/kg. "
                "What is its mass, to the nearest kilogram?",
        "options": [
            {"text": "6423 kg", "correct": False,
             "why": "That multiplies instead of dividing."},
            {"text": "234 kg", "correct": False,
             "why": "That subtracts the field strength from the weight, "
                    "which cannot be done."},
            {"text": "26 kg", "correct": False,
             "why": "That uses Earth's 10 N/kg to convert instead of "
                    "Jupiter's 24.8."},
            {"text": "10 kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s29",
        "band": "standard",
        "text": "A 2 kg mass is weighed on Earth and on the Moon using a "
                "spring balance. Which statement is correct?",
        "options": [
            {"text": "The spring balance reads 2 kg in both places",
             "correct": False,
             "why": "A spring balance reads a force in newtons; on the Moon "
                    "that force is far smaller."},
            {"text": "The spring balance reads about 20 N on Earth and "
                     "about 3.2 N on the Moon", "correct": True},
            {"text": "The spring balance reads about 3.2 N on Earth and "
                     "about 20 N on the Moon", "correct": False,
             "why": "The two readings have been swapped — Earth's field is "
                    "the stronger one."},
            {"text": "The spring balance gives the same reading everywhere, "
                     "because it is calibrated in kilograms", "correct": False,
             "why": "Its kilogram scale assumes Earth's field strength, so "
                    "away from Earth the number it shows is wrong."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-s30",
        "band": "standard",
        "text": "A 32 kg sack of sand weighs 320 N on Earth, where g = "
                "10 N/kg. What would the same sack weigh on Mars, where g = "
                "3.7 N/kg?",
        "options": [
            {"text": "320 N", "correct": False,
             "why": "Weight changes with field strength; Mars's is far "
                    "weaker than Earth's."},
            {"text": "86.5 N", "correct": False,
             "why": "That divides the Earth weight by g, rather than finding "
                    "the mass and multiplying by Mars's field strength."},
            {"text": "118.4 N", "correct": True},
            {"text": "32 N", "correct": False,
             "why": "That is the mass with the unit swapped, not a weight "
                    "calculated for Mars."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p12-01-h10",
        "band": "harder",
        "text": "A parcel has a mass of 2400 g. What would it weigh on "
                "Jupiter, where g = 24.8 N/kg?",
        "options": [
            {"text": "59.52 N", "correct": True},
            {"text": "24 N", "correct": False,
             "why": "That uses Earth's 10 N/kg rather than "
                    "Jupiter's, and it treats the mass as 1 kg besides."},
            {"text": "59 520 N", "correct": False,
             "why": "The mass has been left in grams (2400) instead of "
                    "being converted to 2.4 kg first, so the answer is a "
                    "thousand times too large."},
            {"text": "0.097 N", "correct": False,
             "why": "That divides the mass by the field strength instead of "
                    "multiplying."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h11",
        "band": "harder",
        "text": "A student says: 'Jupiter's g is about two and a half times "
                "Earth's, so anything taken there weighs two and a half "
                "kilograms more.' What is wrong with this claim?",
        "options": [
            {"text": "Nothing — the numbers and the units are both correct "
                     "as stated", "correct": False,
             "why": "The claim mixes up a multiplying factor with an adding "
                    "amount, and gives the wrong unit besides."},
            {"text": "The ratio is wrong — Jupiter's field is about ten "
                     "times Earth's field strength, not two and a half "
                     "times it", "correct": False,
             "why": "24.8 ÷ 10 is indeed close to 2.5, so the ratio itself "
                    "is right."},
            {"text": "Weight is multiplied by the ratio, not added to, and "
                     "the result is still in newtons, not kilograms",
             "correct": True},
            {"text": "It is mass that increases on Jupiter, not weight",
             "correct": False,
             "why": "Mass never changes with location; it is weight that "
                    "increases there."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h12",
        "band": "harder",
        "text": "An object weighs three times as much on Planet X as it "
                "does on Earth, where g = 10 N/kg. What is Planet X's "
                "gravitational field strength?",
        "options": [
            {"text": "3.3 N/kg", "correct": False,
             "why": "That divides Earth's g by 3, which would make Planet "
                    "X's field weaker, not three times stronger."},
            {"text": "13 N/kg", "correct": False,
             "why": "That adds 3 to Earth's g rather than multiplying by 3."},
            {"text": "7 N/kg", "correct": False,
             "why": "That subtracts 3 from Earth's g, moving in the wrong "
                    "direction entirely."},
            {"text": "30 N/kg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h13",
        "band": "harder",
        "text": "Two identical 8 kg toolboxes are taken to different places: "
                "one to the Moon (g = 1.6 N/kg), one to Mars (g = 3.7 N/kg). "
                "Which is heavier there, and by how much?",
        "options": [
            {"text": "The one on the Moon, by 16.8 N", "correct": False,
             "why": "Mars's stronger field gives the larger weight; the "
                    "Moon's is the smaller one."},
            {"text": "The one on Mars, by 2.1 N", "correct": False,
             "why": "That finds the difference in the g values "
                    "(3.7 − 1.6 = 2.1) rather than the difference in the "
                    "weights."},
            {"text": "They weigh the same everywhere, because they have the "
                     "same mass", "correct": False,
             "why": "Equal mass gives equal weight only in the same field; "
                    "Mars and the Moon have different field strengths."},
            {"text": "The one on Mars, by 16.8 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h14",
        "band": "harder",
        "text": "A 6 kg mass weighs 60 N on Earth. What would it weigh on a "
                "planet where the field strength is exactly half of "
                "Earth's?",
        "options": [
            {"text": "30 N", "correct": True},
            {"text": "120 N", "correct": False,
             "why": "Halving the field strength halves the weight; this "
                    "doubles it instead."},
            {"text": "6 N", "correct": False,
             "why": "That is the mass in kilograms with a newton sign put "
                    "does not happen — only the weight changes."},
            {"text": "54 N", "correct": False,
             "why": "That subtracts 6 from 60 rather than halving the "
                    "value."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h15",
        "band": "harder",
        "text": "A 25 kg satellite part is tested and found to weigh 92.5 N "
                "somewhere in the solar system. Which location is this most "
                "likely to be?",
        "options": [
            {"text": "The Moon", "correct": False,
             "why": "25 kg on the Moon (g = 1.6 N/kg) weighs 40 N, not "
                    "92.5 N."},
            {"text": "Earth", "correct": False,
             "why": "25 kg on Earth (g = 10 N/kg) weighs 250 N, not "
                    "92.5 N."},
            {"text": "Jupiter", "correct": False,
             "why": "25 kg on Jupiter (g = 24.8 N/kg) weighs 620 N, far more "
                    "than 92.5 N."},
            {"text": "Mars", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h16",
        "band": "harder",
        "text": "A 4 kg toolbox and a 40 kg generator are both weighed on "
                "Earth. Which has the larger weight-to-mass ratio?",
        "options": [
            {"text": "Neither — the ratio is g, and it is the same for "
                     "every object in the same field", "correct": True},
            {"text": "The generator, because it is more massive",
             "correct": False,
             "why": "A bigger mass gives a bigger weight, but the RATIO of "
                    "weight to mass is the same for every object in the "
                    "same field."},
            {"text": "The toolbox, because a smaller and lighter object is "
                     "pulled proportionally harder by any given field",
             "correct": False,
             "why": "Nothing pulls a smaller object proportionally harder; "
                    "the ratio is fixed by the field, not by the object's "
                    "own size."},
            {"text": "The two ratios cannot be compared until each object has "
                     "been weighed on Earth", "correct": False,
             "why": "The ratio is simply g, 10 N/kg, whatever the two objects' "
                    "masses are — no weighing is needed at all."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h17",
        "band": "harder",
        "text": "A cargo pod weighs exactly 10 times as much on Earth as it "
                "does on the Moon, where g = 1.6 N/kg. Is this consistent "
                "with Earth's real field strength of 10 N/kg?",
        "options": [
            {"text": "Yes — the ratio of the weights should equal the ratio "
                     "of the field strengths, and that ratio is 10",
             "correct": False,
             "why": "10 ÷ 1.6 is about 6.25, not 10, so a true ratio of "
                    "exactly 10 is not consistent with the real field "
                    "strengths."},
            {"text": "Yes, because both values were rounded during the "
                     "calculation", "correct": False,
             "why": "Rounding could not stretch a true ratio of 6.25 all "
                    "the way to 10; the figures are simply inconsistent."},
            {"text": "No — the true ratio of Earth's field strength to the "
                     "Moon's is about 6.25, not 10", "correct": True},
            {"text": "It cannot be checked, because weight ratios do not "
                     "depend on field strength", "correct": False,
             "why": "In a fixed comparison the ratio of two weights of the "
                    "SAME mass is exactly the ratio of the two field "
                    "strengths."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h18",
        "band": "harder",
        "text": "A satellite drifts through deep space, far from any star "
                "or planet. Mission control still tracks its mass precisely "
                "by firing a small measured thruster pulse and timing how "
                "much its speed changes. Why does this method work when a "
                "set of bathroom scales would not?",
        "options": [
            {"text": "Because deep space still has a very faint trace of "
                     "gravity that an ordinary set of bathroom scales "
                     "cannot detect", "correct": False,
             "why": "Whatever tiny field is out there is not what the "
                    "thruster method relies on; it works because it "
                    "measures resistance to a push, which needs no gravity "
                    "at all."},
            {"text": "Because the thruster gives the satellite some mass "
                     "temporarily", "correct": False,
             "why": "Firing a thruster does not change how much matter the "
                    "satellite has."},
            {"text": "Because bathroom scales would actually work fine out "
                     "there too", "correct": False,
             "why": "Bathroom scales need something pressing down under "
                    "gravity; with no weight to press with, they would read "
                    "nothing at all."},
            {"text": "Because the thruster method measures how the "
                     "satellite resists a push, which depends on mass and "
                     "nothing else", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h19",
        "band": "harder",
        "text": "Two rockets have masses 500 kg and 2000 kg. Both climb from "
                "Earth to a height where the field strength has dropped by "
                "exactly 1 N/kg. Which experiences the bigger change in "
                "weight?",
        "options": [
            {"text": "The 500 kg rocket, because a lighter object is affected "
                     "by a change in altitude more", "correct": False,
             "why": "This is backwards — a bigger mass loses more weight "
                    "for the same drop in field strength."},
            {"text": "Both change by exactly the same amount, because the "
                     "field strength drop of 1 N/kg applies equally to "
                     "both rockets", "correct": False,
             "why": "The same drop in g does not give the same drop in "
                    "weight; weight change is mass multiplied by the change "
                    "in g, so it scales with the object's own mass."},
            {"text": "The 2000 kg rocket, because weight change is mass "
                     "multiplied by the change in field strength",
             "correct": True},
            {"text": "Neither changes at all, because mass determines "
                     "weight, not altitude", "correct": False,
             "why": "Field strength genuinely falls with altitude, so both "
                    "rockets lose some weight; the 2000 kg one simply loses "
                    "more."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h20",
        "band": "harder",
        "text": "A postal scale reads a parcel's weight as 4.5 N. The scale "
                "is later found to be reading exactly 10% too low across "
                "its whole range. What is the parcel's true weight?",
        "options": [
            {"text": "4.05 N", "correct": False,
             "why": "That reduces the reading further still, in the wrong "
                    "direction for a scale that already reads too low."},
            {"text": "5 N", "correct": True},
            {"text": "4.95 N", "correct": False,
             "why": "That adds 10% of the wrong figure, rather than "
                    "correcting the reading back to what it should have "
                    "been in full."},
            {"text": "40.5 N", "correct": False,
             "why": "That is ten times too large — the decimal point has "
                    "moved by mistake."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h21",
        "band": "harder",
        "text": "A 12 kg case on Mars (g = 3.7 N/kg) is compared with a 4 kg "
                "case on Jupiter (g = 24.8 N/kg). Which weighs more, and by "
                "roughly how much?",
        "options": [
            {"text": "The one on Mars, by about 55 N", "correct": False,
             "why": "The Jupiter case is the heavier one — 4 kg on Jupiter "
                    "weighs far more than 12 kg on Mars."},
            {"text": "The one on Jupiter, by about 21 N", "correct": False,
             "why": "That finds the difference between the two field "
                    "strengths (24.8 − 3.7 = 21.1) rather than the "
                    "difference between the two weights."},
            {"text": "The one on Jupiter, by about 55 N", "correct": True},
            {"text": "They weigh the same, because 12 kg and 4 kg are both "
                     "small", "correct": False,
             "why": "Mass size alone says nothing about which is heavier; "
                    "the calculation depends on both mass and field "
                    "strength together."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h22",
        "band": "harder",
        "text": "A 750 g rock sample is tested on an unfamiliar moon and "
                "found to weigh 3 N. What is the moon's gravitational "
                "field strength?",
        "options": [
            {"text": "4 N/kg", "correct": True},
            {"text": "0.25 N/kg", "correct": False,
             "why": "That divides the mass by the weight instead of the "
                    "weight by the mass."},
            {"text": "2.25 N/kg", "correct": False,
             "why": "That multiplies the two figures instead of dividing "
                    "one by the other."},
            {"text": "3.75 N/kg", "correct": False,
             "why": "That adds the two figures, which cannot be done."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h23",
        "band": "harder",
        "text": "A robot has a mass of 40 kg on Earth. On an unknown moon it "
                "weighs 60 N. What is the moon's field strength, and how "
                "does it compare with Earth's?",
        "options": [
            {"text": "1.5 N/kg — about two-thirds of Earth's",
             "correct": False,
             "why": "1.5 N/kg is correct, but that is nowhere near "
                    "two-thirds of Earth's 10 N/kg."},
            {"text": "1.5 N/kg — about a seventh of Earth's",
             "correct": True},
            {"text": "15 N/kg — stronger than Earth's", "correct": False,
             "why": "60 ÷ 40 is 1.5, not 15 — the decimal point has moved."},
            {"text": "0.67 N/kg — weaker still than the Moon's own "
                     "1.6 N/kg", "correct": False,
             "why": "That divides the mass by the weight instead of the "
                    "weight by the mass."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h24",
        "band": "harder",
        "text": "A spring stretches by 4 cm when a mass hangs from it on "
                "Earth, where the pull on it is 20 N. On a different world "
                "the identical mass produces only 6 N of pull. Assuming the "
                "spring stretches in proportion to the pull on it, roughly "
                "how far would you expect it to stretch there?",
        "options": [
            {"text": "About 4 cm — the same as on Earth", "correct": False,
             "why": "The pull on the spring is smaller there, so a spring "
                    "that stretches in proportion to force must stretch "
                    "less."},
            {"text": "About 0.8 cm", "correct": False,
             "why": "That multiplies the Earth stretch by the stretch "
                    "per newton (4 x 0.2). Find the stretch per newton "
                    "first (0.2 cm/N), then multiply it by the new 6 N "
                    "pull."},
            {"text": "About 1.2 cm", "correct": True},
            {"text": "About 24 cm", "correct": False,
             "why": "That multiplies rather than working out the "
                    "stretch-per-newton first."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h25",
        "band": "harder",
        "text": "Two students disagree about why an astronaut's weight is "
                "not zero at the height the International Space Station "
                "orbits. Which explanation is correct?",
        "options": [
            {"text": "Their weight really is zero there, because Earth's "
                     "gravitational pull switches off completely the "
                     "moment a spacecraft leaves the planet's atmosphere "
                     "and enters open space", "correct": False,
             "why": "Gravity does not depend on the atmosphere at all, and "
                    "it has not switched off at only a few hundred "
                    "kilometres up."},
            {"text": "Earth's gravitational field still reaches that height "
                     "at close to 90% of its surface strength; the "
                     "astronaut only appears weightless because they are "
                     "falling with the station", "correct": True},
            {"text": "Their weight is zero because the station's speed "
                     "cancels gravity out completely", "correct": False,
             "why": "Speed does not cancel a force; the station's speed is "
                    "what curves its path into an orbit rather than what "
                    "removes gravity's pull."},
            {"text": "Their weight is reduced but not zero, because the "
                     "station blocks some of the pull", "correct": False,
             "why": "The station is far too small and far too light to "
                    "block the Earth's gravitational field in any way."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h26",
        "band": "harder",
        "text": "A 55 kg diver in an aircraft performing a steep dive "
                "experiences 4 seconds of free fall before the pilot pulls "
                "out. What does a set of bathroom scales fixed to the "
                "cabin floor read during those 4 seconds, and why?",
        "options": [
            {"text": "0 N — the diver and the floor are falling together, "
                     "so nothing presses between them", "correct": True},
            {"text": "550 N, exactly as on the ground, because gravity has "
                     "not changed", "correct": False,
             "why": "The reading depends on the push between the diver and "
                    "the floor, not directly on gravity; in free fall that "
                    "push disappears even though gravity is still acting."},
            {"text": "It falls slowly to zero across the whole 4 seconds, "
                     "as gravity gradually switches off during the dive",
             "correct": False,
             "why": "Gravity does not switch off gradually or at all; the "
                    "reading drops to zero as soon as the dive begins, "
                    "because the floor and the diver are already falling "
                    "together."},
            {"text": "It rises above 550 N, because falling downward adds extra "
                     "force to the reading", "correct": False,
             "why": "Falling removes the push rather than adding to it — "
                    "nothing is left to hold the diver up against the "
                    "floor."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h27",
        "band": "harder",
        "text": "Explain why a 1 kg mass and a 1000 kg mass, dropped "
                "together from the same height with no air resistance, hit "
                "the ground at the same moment.",
        "options": [
            {"text": "Because both masses experience zero weight the "
                     "instant they are released and continue to fall with "
                     "no weight acting on either of them at all",
             "correct": False,
             "why": "Both are being pulled by their full weight throughout "
                    "the fall; neither becomes weightless."},
            {"text": "Because air resistance affects both masses in exactly "
                     "the same way", "correct": False,
             "why": "The question specifies no air resistance, so this "
                    "cannot be the reason."},
            {"text": "Because gravity only ever pulls with a fixed force, "
                     "whatever the mass", "correct": False,
             "why": "Gravity pulls harder on a bigger mass — weight is mass "
                    "× field strength, so the two forces are different "
                    "sizes."},
            {"text": "The heavier mass is pulled with more force, but it "
                     "also needs proportionally more force to accelerate it "
                     "at all — the two effects cancel exactly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h28",
        "band": "harder",
        "text": "A 9 kg toolbox is weighed on a spring balance and reads "
                "33.3 N. Which world is this most consistent with?",
        "options": [
            {"text": "The Moon, where g = 1.6 N/kg", "correct": False,
             "why": "9 kg there weighs 14.4 N, not 33.3 N."},
            {"text": "Mars, where g = 3.7 N/kg", "correct": True},
            {"text": "Earth, where g = 10 N/kg", "correct": False,
             "why": "9 kg there weighs 90 N, not 33.3 N."},
            {"text": "Jupiter, where g = 24.8 N/kg", "correct": False,
             "why": "9 kg there weighs 223.2 N, far more than 33.3 N."},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h29",
        "band": "harder",
        "text": "A cargo module has an unknown mass. Its weight is 148.8 N "
                "on Jupiter, where g = 24.8 N/kg. What would the same "
                "module weigh on Earth, where g = 10 N/kg?",
        "options": [
            {"text": "148.8 N", "correct": False,
             "why": "Weight changes with field strength; only the mass — "
                    "6 kg — would carry over unchanged."},
            {"text": "3690.24 N", "correct": False,
             "why": "That multiplies the Jupiter weight directly by "
                    "Jupiter's own field strength, using the same number "
                    "twice instead of finding the mass first."},
            {"text": "6 N", "correct": False,
             "why": "That is the mass, correctly found, but then left with "
                    "the wrong unit instead of being multiplied by Earth's "
                    "10 N/kg."},
            {"text": "60 N", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-01-h30",
        "band": "harder",
        "text": "A 1.5 tonne vehicle (1 tonne = 1000 kg) is designed for use "
                "on Mars, where g = 3.7 N/kg. What is its weight there?",
        "options": [
            {"text": "555 N", "correct": False,
             "why": "That treats the vehicle's mass as 150 kg, ten times "
                    "too small."},
            {"text": "5550 N", "correct": True},
            {"text": "15 000 N", "correct": False,
             "why": "That uses Earth's 10 N/kg instead of Mars's 3.7."},
            {"text": "1500 N", "correct": False,
             "why": "No field strength has been used at all; that is just "
                    "the mass with the unit swapped to newtons."},
        ],
        "figure": None,
    },
]
