"""P2 lesson 01 — Energy in food: twelve questions (MRB-223).

Written against Design's delivered page, not against a summary of it: the
four foods, the 20 g of water, the 4.18 constant, the capture fractions and
the systematic-error argument are all hers, and every question below probes
something that page actually teaches.

⊕ AMENDED MRB-297, 31 Aug 2026 — one of the four is no longer hers. Mide
ruled the peanut out of the burning-food practical on 30 Aug 2026 and a
cheese puff replaces it, at 21.6 kJ/g with a capture of 0.38. Two questions
below quoted the peanut or a number derived from it — `p2-01-s01` and
`p2-01-h01` — and both are re-derived from the new sample rather than
carried across. No option was reordered and no answer moved.

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
        # ⚖️ MRB-297 · re-derived, not carried across. The bench's measured
        # value is `kj_per_g × capture`, so the cheese puff that replaced
        # Design's peanut reads 21.6 × 0.38 = 8.208, and the packet figure
        # is the label itself, 21.6. Design's pair was 8 against 24.
        "text": "A student measures 8.2 kJ per gram for a cheese puff. The "
                "packet says 21.6 kJ per gram. What is the most likely "
                "reason?",
        "options": [
            {"text": "The packet figure is an exaggeration by the "
                     "manufacturer",
             "correct": False,
             "why": "Label figures come from sealed bomb calorimeters and "
                    "are close to right. It is the school apparatus that "
                    "loses energy, not the label that inflates it."},
            {"text": "Much of the energy released never reached the water",
             "correct": True},
            {"text": "The puff was a smaller one than the packet assumed",
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
        # ⚖️ MRB-297 · the five readings and the label were the peanut's.
        # Design's spread is kept exactly — +0.1, 0.0, +0.2, -0.1, +0.1 —
        # and shifted onto the cheese puff's 21.6 × 0.38 = 8.2, against
        # the 21.6 label. No food on this bench carries a 24 any more.
        "text": "A student repeats a calorimeter run five times and gets "
                "8.3, 8.2, 8.4, 8.1 and 8.3 kJ per gram against a label of "
                "21.6. What does the closeness of those five tell you?",
        "options": [
            {"text": "That the measurement is accurate, because the readings "
                     "agree",
             "correct": False,
             "why": "Agreeing with each other is precision, not accuracy. "
                    "Five readings can agree closely and all be wrong in the "
                    "same direction."},
            {"text": "That the error is systematic rather than random",
             "correct": True},
            {"text": "That the label must be wrong by about 13 kJ per gram",
             "correct": False,
             "why": "The consistency is evidence about the APPARATUS. There "
                    "is no reading here that tests the label."},
            {"text": "That more repeats would bring the value up towards "
                     "21.6",
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-01-e05",
        "band": "easier",
        "text": "A biscuit holds 20 kJ in every gram. How much energy is in a "
                "25 g biscuit?",
        "options": [
            {"text": "500 kJ", "correct": True},
            {"text": "0.8 kJ", "correct": False,
             "why": "That is 20 ÷ 25. Energy in a portion is energy per gram "
                    "MULTIPLIED by the mass."},
            {"text": "45 kJ", "correct": False,
             "why": "That is 20 + 25, and a kJ/g cannot be added to a mass in "
                    "grams."},
            {"text": "1.25 kJ", "correct": False,
             "why": "That is 25 ÷ 20, the division upside down as well as the "
                    "wrong operation."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e06",
        "band": "easier",
        "text": "Which food type holds roughly twice as much energy per gram "
                "as the other two?",
        "options": [            {"text": "Protein", "correct": False,
             "why": "Protein holds about 17 kJ/g, the same as carbohydrate "
                    "and about half of fat."},
            {"text": "Fibre", "correct": False,
             "why": "Fibre passes through largely undigested and is not one "
                    "of the three energy figures."},
            {"text": "Carbohydrate", "correct": False,
             "why": "Carbohydrate is about 17 kJ/g — the lower of the two "
                    "figures, not the higher."},
            {"text": "Fat", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e07",
        "band": "easier",
        "text": "Energy density of a food is measured in…",
        "options": [            {"text": "grams per kilojoule (g/kJ)", "correct": False,
             "why": "That is the unit upside down. Energy density is energy "
                    "per gram, not grams per unit of energy."},
            {"text": "kilojoules (kJ)", "correct": False,
             "why": "Kilojoules alone give the energy in the whole portion, "
                    "not the amount in each gram."},
            {"text": "watts (W)", "correct": False,
             "why": "A watt is a rate of transfer in joules per second, which "
                    "has nothing to do with mass."},
            {"text": "kilojoules per gram (kJ/g)", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e08",
        "band": "easier",
        "text": "About how much energy does one gram of carbohydrate hold?",
        "options": [
            {"text": "About 1.7 kJ", "correct": False,
             "why": "That is ten times too small — the figure is about "
                    "17 kJ/g."},
            {"text": "About 37 kJ", "correct": False,
             "why": "37 kJ/g is fat, which holds roughly twice as much as "
                    "carbohydrate."},
            {"text": "About 170 kJ", "correct": False,
             "why": "That is ten times too large; a single gram does not hold "
                    "that much."},
            {"text": "About 17 kJ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e09",
        "band": "easier",
        "text": "A label prints 250 kcal. Roughly how many kilojoules is "
                "that?",
        "options": [
            {"text": "About 1045 kJ", "correct": True},
            {"text": "About 250 kJ", "correct": False,
             "why": "A kilocalorie and a kilojoule are different sizes: one "
                    "kcal is 4.18 kJ."},
            {"text": "About 60 kJ", "correct": False,
             "why": "That is 250 ÷ 4.18, the conversion the wrong way round."},
            {"text": "About 254 kJ", "correct": False,
             "why": "That adds 4.18 rather than multiplying by it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e10",
        "band": "easier",
        "text": "In a school calorimeter, what does the burning food heat?",
        "options": [            {"text": "The air above the flame", "correct": False,
             "why": "Some air is warmed, but nothing measures it — that is "
                    "one reason the reading comes out low."},
            {"text": "The thermometer itself", "correct": False,
             "why": "The thermometer reads the water's temperature; it is an "
                    "instrument, not the thing being heated."},
            {"text": "The mounted needle the food sits on", "correct": False,
             "why": "The needle warms a little, and again nothing measures "
                    "it. The water is what is read."},
            {"text": "A known mass of water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e11",
        "band": "easier",
        "text": "Where in a food is its chemical store held?",
        "options": [            {"text": "In the warmth the food gives off as it is eaten",
             "correct": False,
             "why": "Warmth is energy leaving by a pathway, not the store "
                    "that held it."},
            {"text": "In the water the food contains", "correct": False,
             "why": "Water carries no chemical store at all — a wet food "
                    "holds less per gram, not more."},
            {"text": "In the mass of the food, which is why heavier foods "
                     "hold more",
             "correct": False,
             "why": "Mass matters, but a gram of fat and a gram of "
                    "carbohydrate hold very different amounts."},
            {"text": "In the arrangement of the particles it is made from",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-01-s05",
        "band": "standard",
        "text": "A 45 g portion of a food holds 37 kJ in every gram. How much "
                "energy does the portion hold?",
        "options": [
            {"text": "1665 kJ", "correct": True},
            {"text": "82 kJ", "correct": False,
             "why": "That is 37 + 45, and an energy density cannot be added "
                    "to a mass."},
            {"text": "1.2 kJ", "correct": False,
             "why": "That is 45 ÷ 37, a division where the calculation needs "
                    "a multiplication."},
            {"text": "0.82 kJ", "correct": False,
             "why": "That is 37 ÷ 45, the division upside down as well as the "
                    "wrong operation."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s06",
        "band": "standard",
        "text": "A label reads 500 kcal. A student writes that this is "
                "500 kJ. What is wrong?",
        "options": [            {"text": "Nothing — a kilocalorie and a kilojoule are the same "
                     "size",
             "correct": False,
             "why": "They are not: one kilocalorie is 4.18 kilojoules."},
            {"text": "The label is wrong, because food energy is only ever in "
                     "kJ",
             "correct": False,
             "why": "Labels legally print both. The student's conversion is "
                    "what is wrong."},
            {"text": "One kilocalorie is 4.18 kJ, so it is about 120 kJ",
             "correct": False,
             "why": "That divides by 4.18 instead of multiplying, making the "
                    "figure smaller rather than larger."},
            {"text": "One kilocalorie is 4.18 kJ, so it is about 2090 kJ",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s07",
        "band": "standard",
        "text": "Two foods are measured at 17 kJ/g and 37 kJ/g. Which is "
                "mostly fat, and how do you know?",
        "options": [            {"text": "The 17 kJ/g one, because fat is the lighter of the two",
             "correct": False,
             "why": "How heavy a food is does not set its energy density; fat "
                    "is the higher figure."},
            {"text": "Neither can be told from these figures alone",
             "correct": False,
             "why": "17 and 37 kJ/g are exactly the two standard figures for "
                    "carbohydrate and fat."},
            {"text": "The 37 kJ/g one, because fat burns more easily in air",
             "correct": False,
             "why": "How easily it burns is not the measurement. The figure "
                    "is energy per gram."},
            {"text": "The 37 kJ/g one, because fat holds about twice as much "
                     "per gram",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s08",
        "band": "standard",
        "text": "A calorimeter run gives a temperature rise for a known mass "
                "of water. What else must be measured before an energy per "
                "gram can be given?",
        "options": [
            {"text": "The mass of food that was burnt", "correct": True},
            {"text": "The temperature of the room", "correct": False,
             "why": "The rise is what counts, and it is already the "
                    "difference between two readings."},
            {"text": "The height of the flame", "correct": False,
             "why": "Nothing in the calculation uses the flame's size."},
            {"text": "The time the food took to burn", "correct": False,
             "why": "Time would give a power in watts, not an energy per "
                    "gram."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s09",
        "band": "standard",
        "text": "Why is a shield or screen put around the calorimeter?",
        "options": [
            {"text": "To keep the food dry while it burns", "correct": False,
             "why": "The water is above the flame, and how dry the food is "
                    "was fixed before the run."},
            {"text": "To stop the flame going out", "correct": False,
             "why": "A shield helps a little there, but the reason it is used "
                    "is the energy escaping sideways."},
            {"text": "To make the food burn faster", "correct": False,
             "why": "How fast it burns does not change how much energy it "
                    "holds altogether."},
            {"text": "To cut down the energy escaping to the surroundings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s10",
        "band": "standard",
        "text": "A 30 g cereal bar is found to hold 630 kJ. What is its "
                "energy density?",
        "options": [            {"text": "18 900 kJ/g", "correct": False,
             "why": "That is 630 × 30. Energy density is the energy DIVIDED "
                    "by the mass."},
            {"text": "660 kJ/g", "correct": False,
             "why": "That is 630 + 30, and the two quantities cannot be "
                    "added."},
            {"text": "0.048 kJ/g", "correct": False,
             "why": "That is 30 ÷ 630, the division the wrong way round."},
            {"text": "21 kJ/g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s11",
        "band": "standard",
        "text": "A student says exercise destroys the energy that was in the "
                "food. Which correction is right?",
        "options": [
            {"text": "Exercise moves it into kinetic and thermal stores; none "
                     "of it is destroyed",
             "correct": True},
            {"text": "Exercise turns it into a new kind of energy the body "
                     "makes",
             "correct": False,
             "why": "There are no new kinds. The same energy simply moves "
                    "into different stores."},
            {"text": "Nothing is wrong — that is what burning it off means",
             "correct": False,
             "why": "Burning off is everyday language for emptying the "
                    "chemical store, not for destroying anything."},
            {"text": "Exercise sends the energy back into the food that has "
                     "not been eaten",
             "correct": False,
             "why": "Energy never returns to a store it has left; it ends up "
                    "warming the body and the air."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-01-h05",
        "band": "harder",
        "text": "Snack A is 80 g at 22 kJ/g. Snack B is 40 g at 37 kJ/g. "
                "Which holds more energy altogether?",
        "options": [            {"text": "B, because it has the higher energy density",
             "correct": False,
             "why": "Per gram it does, but there is only half as much of it: "
                    "1480 kJ against 1760 kJ."},
            {"text": "B, with 2960 kJ against 1760 kJ", "correct": False,
             "why": "That doubles B's mass. It is 40 g, so its total is "
                    "1480 kJ."},
            {"text": "They are the same, because the figures balance out",
             "correct": False,
             "why": "They do not balance: 80 × 22 is 1760 and 40 × 37 is "
                    "1480."},
            {"text": "A, with 1760 kJ against 1480 kJ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h06",
        "band": "harder",
        "text": "A bag is labelled 958 kJ and 229 kcal. Do the two figures "
                "agree?",
        "options": [            {"text": "No — 229 kcal should be about 229 kJ", "correct": False,
             "why": "A kilocalorie is 4.18 times a kilojoule, so the two "
                    "numbers cannot be equal."},
            {"text": "No — the kJ figure should be about 55", "correct": False,
             "why": "That divides by 4.18 instead of multiplying; the kJ "
                    "figure is always the larger one."},
            {"text": "It cannot be decided without knowing the mass of the "
                     "bag",
             "correct": False,
             "why": "The conversion between the two units does not use a mass "
                    "at all."},
            {"text": "Yes — 229 × 4.18 is about 957", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h07",
        "band": "harder",
        "text": "A calorimeter reads about 8 kJ/g where the label says "
                "21.6 kJ/g, run after run. Why does repeating it not fix the "
                "gap?",
        "options": [
            {"text": "Because the loss pushes every reading the same way — it "
                     "is a systematic error",
             "correct": True},
            {"text": "Because five runs is not enough to average out a "
                     "random error",
             "correct": False,
             "why": "Averaging removes scatter, and the readings are already "
                    "tightly grouped. The gap is not scatter."},
            {"text": "Because the label is simply wrong and cannot be "
                     "reached",
             "correct": False,
             "why": "A bomb calorimeter reaches it routinely, so the label is "
                    "not the problem."},
            {"text": "Because the thermometer becomes less accurate with each "
                     "run",
             "correct": False,
             "why": "It reads the same each time, which is why the results "
                    "agree with one another so closely."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h08",
        "band": "harder",
        "text": "Burning 1.0 g of food raises 100 g of water by 12 °C. Water "
                "needs 4.2 J for each gram for each degree. What energy was "
                "measured?",
        "options": [
            {"text": "5040 J", "correct": True},
            {"text": "504 J", "correct": False,
             "why": "That is ten times too small — 100 × 4.2 × 12 is 5040."},
            {"text": "420 J", "correct": False,
             "why": "That is 100 × 4.2, leaving the 12 °C rise out "
                    "altogether."},
            {"text": "50 400 J", "correct": False,
             "why": "That is ten times too large; check the order of "
                    "magnitude before writing it down."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h09",
        "band": "harder",
        "text": "A poster says a 400 kJ snack will be burnt off in twenty "
                "minutes of running. What does burnt off actually mean?",
        "options": [            {"text": "The 400 kJ has been destroyed by the muscles",
             "correct": False,
             "why": "Nothing destroys energy. It has moved rather than "
                    "vanished."},
            {"text": "The 400 kJ has been stored as heat inside the muscles "
                     "for later",
             "correct": False,
             "why": "That thermal store drains away into the surroundings; "
                    "nothing gets it back."},
            {"text": "The snack has been removed from the body without being "
                     "digested",
             "correct": False,
             "why": "The food was digested; what changed is where its energy "
                    "now sits."},
            {"text": "The chemical store has emptied into kinetic and thermal "
                     "stores",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h10",
        "band": "harder",
        "text": "A 50 g snack and a 120 g snack both hold 1800 kJ. Which has "
                "the higher energy density, and by how much?",
        "options": [            {"text": "The 120 g one, at 15 kJ/g against 36 kJ/g",
             "correct": False,
             "why": "The figures are right but attached to the wrong snacks: "
                    "36 kJ/g belongs to the smaller one."},
            {"text": "Neither — equal energy means equal energy density",
             "correct": False,
             "why": "Density is energy per gram, so spreading the same energy "
                    "over more grams lowers it."},
            {"text": "The 50 g one, at 90 kJ/g against 21 kJ/g",
             "correct": False,
             "why": "Those come from multiplying rather than dividing; "
                    "1800 ÷ 50 is 36."},
            {"text": "The 50 g one, at 36 kJ/g against 15 kJ/g",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h11",
        "band": "harder",
        "text": "Why is the Calorie printed on a food label written with a "
                "capital C?",
        "options": [
            {"text": "Because it is the brand name a manufacturer chooses to "
                     "use",
             "correct": False,
             "why": "It is a unit, fixed by law on the label, not a name a "
                    "company picks."},
            {"text": "Because a capital C means the figure is for the whole "
                     "packet",
             "correct": False,
             "why": "Whether it is per packet or per 100 g is stated "
                    "separately; the capital is about the unit."},
            {"text": "Because capital letters are used for every unit in "
                     "science",
             "correct": False,
             "why": "Most are lower case — the metre, the second and the gram "
                    "among them."},
            {"text": "Because it is a kilocalorie — a thousand of the "
                     "calories a scientist means",
             "correct": True},
        ],
        "figure": None,
    },
]
