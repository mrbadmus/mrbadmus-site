"""P2 lesson 01 — Energy in food: twelve questions (MRB-223).

Written against Design's delivered page, not against a summary of it: the
four foods, the 20 g of water, the 4.18 constant, the capture fractions and
the systematic-error argument are all hers, and every question below probes
something that page actually teaches.

The discriminations these are built on, in the order the lesson builds them:

  · a kcal and a kJ are the same energy in different units (`ENER-20`);
  · `E = e × m` is a PRODUCT, so more mass means more energy — the
    distractors are the three other things a student does with two numbers;
  · the calorimeter reads LOW, every error runs one way, and repeating a
    measurement does nothing about that (this is the one the lesson exists
    for, and it is the hardest band);
  · energy is not destroyed by exercise (`ENER-09`, re-confronted here).

⚠️ POSITION IS AUTHORED, NOT LEFT TO CHANCE. The correct option's index
cycles 1, 2, 3, 0 through the twelve, so the lesson contributes exactly
three of each and no button beats reading. Matches P1's eight banks.

⚠️ The bank and the ladder are SEPARATE corpora. Check 6 of
`verify_questions.py` forbids a question whose text matches a rung's, so
none of these restates Rung 1's cheddar or Rung 2's 229/958 label.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P2"
LESSON = "energy-in-food"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p2-01-e01",
        "band": "easier",
        "text": "Which store does food hold its energy in?",
        "options": [
            {"text": "A thermal store", "correct": False,
             "why": "Food is not hot. A thermal store is energy held because "
                    "something is warm."},
            {"text": "A chemical store", "correct": True},
            {"text": "A kinetic store", "correct": False,
             "why": "Kinetic means moving. A sandwich on a plate is not "
                    "moving and still holds the energy."},
            {"text": "An elastic store", "correct": False,
             "why": "Elastic means stretched or squashed. Nothing about food "
                    "is under tension."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e02",
        "band": "easier",
        "text": "A food holds 15 kJ of energy in every gram. How much energy "
                "is in a 40 g portion?",
        "options": [
            {"text": "55 kJ", "correct": False,
             "why": "That is 15 + 40. You cannot add a per-gram figure to a "
                    "mass — they are different quantities."},
            {"text": "0.375 kJ", "correct": False,
             "why": "That is 15 ÷ 40, which is the division the wrong way "
                    "round."},
            {"text": "600 kJ", "correct": True},
            {"text": "2.67 kJ", "correct": False,
             "why": "That is 40 ÷ 15. More food means more energy, so this "
                    "has to be a multiplication."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e03",
        "band": "easier",
        "text": "In the calorimeter, what is actually measured to work out "
                "how much energy the food released?",
        "options": [
            {"text": "How long the sample burns for before it goes out",
             "correct": False,
             "why": "Burning time depends on the shape of the sample as much "
                    "as its energy. Nothing is calculated from it."},
            {"text": "How much smoke comes off the flame as it burns",
             "correct": False,
             "why": "Nothing on the bench measures smoke, and it would not "
                    "tell you a number of joules."},
            {"text": "How much the sample shrinks as it burns away",
             "correct": False,
             "why": "The mass burned is recorded, but it is not what the "
                    "energy is calculated from — the water is."},
            {"text": "The temperature rise of the water above it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e04",
        "band": "easier",
        "text": "One kilocalorie is equal to about…",
        "options": [
            {"text": "4.18 kilojoules", "correct": True},
            {"text": "1 kilojoule", "correct": False,
             "why": "If they were equal, labels would not need to print both "
                    "numbers — and 229 kcal would read as 229 kJ, not "
                    "958."},
            {"text": "1000 kilojoules", "correct": False,
             "why": "That is out by a factor of about 240. A 250 kcal "
                    "chocolate bar would then hold 250 000 kJ."},
            {"text": "0.24 kilojoules", "correct": False,
             "why": "That is the conversion upside down — it is how many "
                    "kilocalories are in one kilojoule."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p2-01-s01",
        "band": "standard",
        "text": "A student measures 8 kJ per gram for a peanut. The packet "
                "says 24 kJ per gram. What is the most likely reason?",
        "options": [
            {"text": "The packet figure is an exaggeration by the "
                     "manufacturer",
             "correct": False,
             "why": "Label figures come from sealed bomb calorimeters and "
                    "are close to right. It is the school apparatus that "
                    "loses energy, not the label that inflates it."},
            {"text": "Much of the energy released never reached the water",
             "correct": True},
            {"text": "The peanut was a smaller one than the packet assumed",
             "correct": False,
             "why": "Both figures are PER GRAM, so the size of the sample "
                    "has already been divided out of each."},
            {"text": "The thermometer was reading too low",
             "correct": False,
             "why": "A faulty thermometer would be one possible error among "
                    "many, and would not account for a gap this large or "
                    "one that appears on every run."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s02",
        "band": "standard",
        "text": "Which of these would make a school calorimeter read HIGHER "
                "than it does?",
        "options": [
            {"text": "Holding the flame further from the tube",
             "correct": False,
             "why": "That gives the energy more room to escape into the air, "
                    "so the reading falls."},
            {"text": "Using more water in the boiling tube",
             "correct": False,
             "why": "More water rises less for the same energy. The "
                    "calculated energy per gram is unchanged, and the "
                    "temperature rise itself is smaller."},
            {"text": "Shielding the apparatus from draughts",
             "correct": True},
            {"text": "Repeating the run three times and taking a mean",
             "correct": False,
             "why": "A mean removes scatter. Every error here runs the same "
                    "way, so averaging leaves the whole gap exactly where "
                    "it was."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s03",
        "band": "standard",
        "text": "Two snacks both hold 900 kJ. One is 25 g and the other is "
                "60 g. What can you say about them?",
        "options": [
            {"text": "The 60 g snack must contain more fat",
             "correct": False,
             "why": "It is the other way round. Holding the same energy in "
                    "more grams means a LOWER energy density, so less fat."},
            {"text": "They must contain the same ingredients",
             "correct": False,
             "why": "Equal totals say nothing about ingredients — that "
                    "is the whole reason energy per gram is quoted "
                    "separately."},
            {"text": "The 25 g snack must be less useful to the body",
             "correct": False,
             "why": "Energy figures say nothing about vitamins, minerals, "
                    "protein or fibre, in either direction."},
            {"text": "The 25 g snack holds more energy per gram",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s04",
        "band": "standard",
        "text": "Why does burning a food in air release almost the same "
                "energy as the body gets from eating it?",
        "options": [
            {"text": "Both rearrange the same chemical store into the same "
                     "products",
             "correct": True},
            {"text": "Because the body burns food with a flame, just a very "
                     "small one",
             "correct": False,
             "why": "Nothing in the body burns. Respiration runs in dozens "
                    "of small controlled steps at about 37 °C."},
            {"text": "Because the calorimeter is designed to match the human "
                     "body",
             "correct": False,
             "why": "A calorimeter is designed to catch energy in water. "
                    "That the two figures agree is a fact about the "
                    "chemistry, not about the apparatus."},
            {"text": "Because energy is created in both processes",
             "correct": False,
             "why": "Energy is never created. Both processes empty a store "
                    "that was already there."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p2-01-h01",
        "band": "harder",
        "text": "A student repeats a calorimeter run five times and gets "
                "9.1, 9.0, 9.2, 8.9 and 9.1 kJ per gram against a label of "
                "24. What does the closeness of those five tell you?",
        "options": [
            {"text": "That the measurement is accurate, because the readings "
                     "agree",
             "correct": False,
             "why": "Agreeing with each other is precision, not accuracy. "
                    "Five readings can agree closely and all be wrong in the "
                    "same direction."},
            {"text": "That the error is systematic rather than random",
             "correct": True},
            {"text": "That the label must be wrong by about 15 kJ per gram",
             "correct": False,
             "why": "The consistency is evidence about the APPARATUS. There "
                    "is no reading here that tests the label."},
            {"text": "That more repeats would bring the value up towards 24",
             "correct": False,
             "why": "Repeating averages out scatter, and there is barely any "
                    "scatter here. Nothing about repetition closes a leak."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h02",
        "band": "harder",
        "text": "A gym poster says “this class burns off 2000 kJ”. "
                "Which statement describes what actually happens to those "
                "2000 kJ?",
        "options": [
            {"text": "They are destroyed by the muscles doing work",
             "correct": False,
             "why": "Nothing destroys energy. The word “burns off” is "
                    "everyday language for emptying a store, not a "
                    "description of the physics."},
            {"text": "They are stored in the muscles as strength for later",
             "correct": False,
             "why": "Muscles do grow, but that is a tiny fraction. Almost "
                    "all of it leaves as a thermal store."},
            {"text": "A chemical store empties and almost all of it ends up "
                     "as a thermal store",
             "correct": True},
            {"text": "They are converted into the kinetic energy of the "
                     "exercise and stay there",
             "correct": False,
             "why": "A kinetic store only holds energy while you are "
                    "moving. Stop, and it has gone somewhere — the room "
                    "and you, both warmer."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h03",
        "band": "harder",
        "text": "A cheese sample is fatty but wet, and reads lower per gram "
                "than a drier food with a similar fat content. Why does the "
                "water in it matter?",
        "options": [
            {"text": "Water in the sample soaks up energy without ever "
                     "reaching the thermometer",
             "correct": True},
            {"text": "Water reacts with the fat and lowers the energy the "
                     "food itself holds",
             "correct": False,
             "why": "The chemical store in the fat is unchanged by being wet. "
                    "It is the MEASUREMENT that suffers, not the food."},
            {"text": "Wet food cannot be weighed accurately, so the per-gram "
                     "figure is wrong",
             "correct": False,
             "why": "It weighs perfectly well, and the balance is not "
                    "troubled by water. The mass is not the problem."},
            {"text": "Water makes the flame burn hotter, so more of the "
                     "energy escapes the can",
             "correct": False,
             "why": "Water does not make a flame hotter. It takes energy to "
                    "warm and to evaporate, which is where the loss is."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h04",
        "band": "harder",
        "text": "A professional bomb calorimeter is a sealed steel vessel "
                "filled with pure oxygen and sitting in a weighed water "
                "bath. Which problem with the school version does each of "
                "those features fix?",
        "options": [
            {"text": "The sealing stops the sample from being weighed "
                     "wrongly, and the oxygen speeds the reaction up",
             "correct": False,
             "why": "Weighing was never the problem, and speed is not what is "
                    "wrong with the school version either."},
            {"text": "The steel absorbs the escaping energy, and the water "
                     "bath measures the sample's mass for you",
             "correct": False,
             "why": "The water bath measures a temperature rise. Nothing "
                    "there measures mass."},
            {"text": "The oxygen prevents the sample burning at all until the "
                     "moment it is measured",
             "correct": False,
             "why": "Pure oxygen does the opposite — it makes combustion more "
                    "complete, which is the point."},
            {"text": "The seal stops energy escaping to the room, and the "
                     "oxygen makes sure the sample burns completely",
             "correct": True},
        ],
        "figure": None,
    },
]
