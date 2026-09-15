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
            {"text": "To keep the food completely dry for as long as it "
                     "burns",
             "correct": False,
             "why": "The water is above the flame, and how dry the food is "
                    "was fixed before the run."},
            {"text": "To stop the flame going out", "correct": False,
             "why": "A shield helps a little there, but the reason it is used "
                    "is the energy escaping sideways."},
            {"text": "To make the food burn faster", "correct": False,
             "why": "How fast it burns does not change how much energy it "
                    "holds altogether."},
            {"text": "To cut the energy escaping to the surroundings",
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
            {"text": "Because the loss is systematic, shifting every reading "
                     "the same way",
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
            {"text": "Because the thermometer becomes less accurate with "
                     "every run that is done",
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
                     "packet, not one portion",
             "correct": False,
             "why": "Whether it is per packet or per 100 g is stated "
                    "separately; the capital is about the unit."},
            {"text": "Because capital letters are used for every unit in "
                     "science",
             "correct": False,
             "why": "Most are lower case — the metre, the second and the gram "
                    "among them."},
            {"text": "Because it is a kilocalorie — a thousand of the smaller "
                     "calories",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p2-01-e12",
        "band": "easier",
        "text": "A snack is labelled 418 kJ. About how many kilocalories is "
                "that?",
        "options": [
            {"text": "About 100 kcal", "correct": True},
            {"text": "About 1747 kcal", "correct": False,
             "why": "That multiplies by 4.18 where the conversion divides, so "
                    "it lands far too high."},
            {"text": "About 414 kcal", "correct": False,
             "why": "That subtracts 4.18 rather than dividing by it, which is "
                    "not what a unit change does."},
            {"text": "About 42 kcal", "correct": False,
             "why": "That divides by ten, and ten is not the factor between "
                    "these two units."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e13",
        "band": "easier",
        "text": "Which piece of safety equipment must everyone in the room "
                "wear while food is burned?",
        "options": [
            {"text": "Heatproof gloves", "correct": False,
             "why": "Gloves are not needed for a demonstration nobody is "
                    "handling."},
            {"text": "Eye protection", "correct": True},
            {"text": "A face mask", "correct": False,
             "why": "No mask is required; the sample is burned in a fume-free "
                    "open lab."},
            {"text": "A laboratory apron", "correct": False,
             "why": "An apron is sensible clothing but is not the item the "
                    "safety note names."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e14",
        "band": "easier",
        "text": "A boiling tube has just come off the flame. Why is it "
                "dangerous to pick up?",
        "options": [
            {"text": "Heated glass turns brittle and shatters",
             "correct": False,
             "why": "Lifting it does not shatter it. The danger is the "
                    "temperature, not the strength."},
            {"text": "The water inside it keeps boiling for several minutes "
                     "after the flame is out",
             "correct": False,
             "why": "The water stops boiling almost at once. The tube itself "
                    "stays hot for far longer."},
            {"text": "A hot tube looks exactly the same as a cold one",
             "correct": True},
            {"text": "The burnt sample gives off a gas that is harmful to "
                     "breathe in close up",
             "correct": False,
             "why": "The smoke is unpleasant rather than harmful, and it is "
                    "not why the tube is left alone."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e15",
        "band": "easier",
        "text": "Which two food groups hold roughly the same energy as each "
                "other in every gram?",
        "options": [
            {"text": "Fat and carbohydrate", "correct": False,
             "why": "Fat holds about twice what carbohydrate does, at roughly "
                    "37 against 17 kJ/g."},
            {"text": "Fat and protein", "correct": False,
             "why": "Fat is about double protein as well — the two low figures "
                    "are the ones that match."},
            {"text": "Fat and fibre", "correct": False,
             "why": "Fibre passes through largely undigested and is not one of "
                    "the three energy figures."},
            {"text": "Carbohydrate and protein", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e16",
        "band": "easier",
        "text": "Dry pasta gives 15 kJ for each gram burnt. Calculate the "
                "energy held by a 20 g serving.",
        "options": [
            {"text": "300 kJ", "correct": True},
            {"text": "35 kJ", "correct": False,
             "why": "That adds the two numbers, and an energy per gram cannot "
                    "be added to a mass."},
            {"text": "1.33 kJ", "correct": False,
             "why": "That is 20 ÷ 15, a division where the working needs a "
                    "multiplication."},
            {"text": "0.75 kJ", "correct": False,
             "why": "That is 15 ÷ 20, upside down as well as the wrong "
                    "operation altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e17",
        "band": "easier",
        "text": "Which unit is the scientific one for measuring energy?",
        "options": [
            {"text": "The kilocalorie", "correct": False,
             "why": "It survives on labels because shoppers are used to it, "
                    "not because science uses it."},
            {"text": "The joule", "correct": True},
            {"text": "The gram", "correct": False,
             "why": "A gram measures mass. Energy needs a unit of its own."},
            {"text": "The degree Celsius", "correct": False,
             "why": "That measures temperature, which is what the thermometer "
                    "reads rather than the energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e18",
        "band": "easier",
        "text": "Compared with the figure on the packet, how does a school "
                "calorimeter's value come out?",
        "options": [
            {"text": "Higher, every time",
             "correct": False,
             "why": "The flame releases the food's energy; it adds nothing "
                    "from anywhere else."},
            {"text": "Sometimes higher, at random",
             "correct": False,
             "why": "Every error on this bench runs one way, so the reading "
                    "never comes out high."},
            {"text": "Lower, every time", "correct": True},
            {"text": "Exactly equal",
             "correct": False,
             "why": "Careful setting-up helps a little, and a school bench "
                    "still cannot reach the label."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e19",
        "band": "easier",
        "text": "The Calorie written on a food packet is the same thing as "
                "one…",
        "options": [
            {"text": "joule", "correct": False,
             "why": "A joule is far smaller — a label Calorie is thousands of "
                    "them."},
            {"text": "kilojoule", "correct": False,
             "why": "Close in size but not the same unit: one is 4.18 times "
                    "the other."},
            {"text": "gram of fat", "correct": False,
             "why": "That is a mass, and the Calorie measures energy rather "
                    "than how much food there is."},
            {"text": "kilocalorie", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e20",
        "band": "easier",
        "text": "A packet gives only the food's energy figure. Which question "
                "can that figure answer?",
        "options": [
            {"text": "How many kilojoules a portion holds", "correct": True},
            {"text": "How much vitamin C the food contains", "correct": False,
             "why": "Vitamins are listed separately; an energy figure says "
                    "nothing at all about them."},
            {"text": "How much fibre is in each portion", "correct": False,
             "why": "Fibre carries almost no energy, so the figure cannot "
                    "reveal how much there is."},
            {"text": "How healthy the food is overall", "correct": False,
             "why": "Two foods with equal energy can differ hugely in how "
                    "useful they are to a body."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e21",
        "band": "easier",
        "text": "Pure fat holds about 37 kJ in each gram. How much is held by "
                "10 g of it?",
        "options": [
            {"text": "47 kJ", "correct": False,
             "why": "That adds the mass to the energy density instead of "
                    "multiplying them together."},
            {"text": "370 kJ", "correct": True},
            {"text": "3.7 kJ", "correct": False,
             "why": "That is 37 ÷ 10, which would mean more food held less "
                    "energy."},
            {"text": "0.27 kJ", "correct": False,
             "why": "That is 10 ÷ 37, the division the wrong way up as well as "
                    "the wrong operation."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e22",
        "band": "easier",
        "text": "Burning food samples is done as a teacher demonstration. "
                "Which reason is given for that?",
        "options": [
            {"text": "The apparatus is too expensive for a class set to be "
                     "bought",
             "correct": False,
             "why": "A boiling tube and a needle cost very little. Cost is not "
                    "the reason."},
            {"text": "The results only work when one person does every run "
                     "the same way",
             "correct": False,
             "why": "Repeating runs is encouraged. Who holds the apparatus is "
                    "not the issue."},
            {"text": "The sample has to be weighed on a balance too delicate "
                     "for a class",
             "correct": False,
             "why": "An ordinary school balance weighs these samples "
                    "perfectly well."},
            {"text": "Burning food spits, and the tube gets hot enough to "
                     "burn", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e23",
        "band": "easier",
        "text": "What is a calorimeter?",
        "options": [
            {"text": "A balance that weighs a food sample before and after it "
                     "is burnt",
             "correct": False,
             "why": "The sample is weighed, but on an ordinary balance — that "
                    "is not what the word names."},
            {"text": "A label printed on food packaging giving the energy in "
                     "each portion",
             "correct": False,
             "why": "The label reports a result. A calorimeter is the "
                    "apparatus that produces one."},
            {"text": "A thermometer designed to be read while it sits in a "
                     "burning flame",
             "correct": False,
             "why": "The thermometer goes in the water, never the flame, and "
                    "it is only one part of the apparatus."},
            {"text": "Apparatus that measures energy released from the "
                     "temperature rise of water",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e24",
        "band": "easier",
        "text": "What does it mean to call an error systematic?",
        "options": [
            {"text": "It pushes every reading the same way", "correct": True},
            {"text": "It happens whenever the apparatus is set up in a hurry",
             "correct": False,
             "why": "A careful set-up does not remove it; the leak is built "
                    "into the apparatus."},
            {"text": "It makes readings scatter above and below the true "
                     "value",
             "correct": False,
             "why": "That is random error, and it is the sort that averaging "
                    "does help with."},
            {"text": "It shows up on one run in every set",
             "correct": False,
             "why": "It is there on every run, which is exactly why repeating "
                    "does not remove it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e25",
        "band": "easier",
        "text": "How many joules make one kilojoule?",
        "options": [
            {"text": "100", "correct": False,
             "why": "A kilo always means a thousand, in every unit it is "
                    "attached to."},
            {"text": "1000", "correct": True},
            {"text": "4.18", "correct": False,
             "why": "That is the factor between a kilocalorie and a kilojoule, "
                    "not between a joule and a kilojoule."},
            {"text": "1 000 000", "correct": False,
             "why": "A million joules is a megajoule, which is a thousand "
                    "kilojoules."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e26",
        "band": "easier",
        "text": "A cheese puff is mostly fat and air. Which property makes it "
                "suit the burning demonstration?",
        "options": [
            {"text": "It holds more energy per gram than any other food a "
                     "school could use",
             "correct": False,
             "why": "Crisps beat it on the bench, and the choice is about how "
                    "it burns rather than how much it holds."},
            {"text": "It contains enough water to keep the flame from going "
                     "out too quickly",
             "correct": False,
             "why": "It is a dry snack. Water in a sample makes a reading "
                    "worse, not better."},
            {"text": "It lights at once and then burns steadily",
             "correct": True},
            {"text": "It leaves no ash behind once it has burnt",
             "correct": False,
             "why": "There is always some residue, and the mass is found by "
                    "weighing rather than by assuming."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e27",
        "band": "easier",
        "text": "A student records a biscuit's energy density as “20 kJ”. "
                "What is missing?",
        "options": [
            {"text": "The name of the food it was measured from",
             "correct": False,
             "why": "The food is already known. What is missing is part of the "
                    "unit itself."},
            {"text": "The temperature the measurement was taken at",
             "correct": False,
             "why": "No energy density is quoted with a temperature, so "
                    "nothing is missing there."},
            {"text": "The mass of water that was used in the tube",
             "correct": False,
             "why": "The water is part of the method, not part of the quantity "
                    "being reported."},
            {"text": "The “per gram” — the unit is kJ/g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e28",
        "band": "easier",
        "text": "Some of the energy from the flame goes sideways into the "
                "room. What becomes of it?",
        "options": [
            {"text": "It warms the air and never reaches the water",
             "correct": True},
            {"text": "It is destroyed as soon as it leaves the flame",
             "correct": False,
             "why": "Nothing destroys energy. It ends up somewhere, just not "
                    "somewhere the thermometer can see."},
            {"text": "It returns to the sample and is burnt a second time",
             "correct": False,
             "why": "Energy does not return to a store it has left, and the "
                    "sample is not reheated by it."},
            {"text": "It is counted by the thermometer a few seconds later",
             "correct": False,
             "why": "The thermometer only ever reads the water, so energy in "
                    "the room is never counted."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e29",
        "band": "easier",
        "text": "Which of these bench samples is mostly carbohydrate?",
        "options": [
            {"text": "Crisps", "correct": False,
             "why": "Crisps are largely fat, which is why they top the bench "
                    "on energy per gram."},
            {"text": "Dry pasta", "correct": True},
            {"text": "Cheese", "correct": False,
             "why": "Cheese is fatty and wet, and neither of those makes it "
                    "a carbohydrate."},
            {"text": "A cheese puff", "correct": False,
             "why": "A puff is mostly fat and air, which is what lets it light "
                    "so readily."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-e30",
        "band": "easier",
        "text": "A packet gives 2156 kJ per 100 g. How much energy is that in "
                "each gram?",
        "options": [
            {"text": "215.6 kJ", "correct": False,
             "why": "That divides by ten. There are a hundred grams in the "
                    "figure quoted."},
            {"text": "2156 kJ", "correct": False,
             "why": "That is the whole 100 g, which no single gram could "
                    "possibly hold."},
            {"text": "21.6 kJ", "correct": True},
            {"text": "2.16 kJ", "correct": False,
             "why": "That divides by a thousand, and the label is quoted per "
                    "hundred grams."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p2-01-s12",
        "band": "standard",
        "text": "A bench gives 8.2 kJ/g where the packet says 21.6 kJ/g. "
                "Roughly what percentage of the packet figure is that?",
        "options": [
            {"text": "About 8 per cent", "correct": False,
             "why": "That reads the measured figure itself as a percentage "
                    "rather than comparing the two."},
            {"text": "About 38 per cent", "correct": True},
            {"text": "About 62 per cent", "correct": False,
             "why": "That is the size of the gap, not the size of the reading "
                    "against the label."},
            {"text": "About 260 per cent", "correct": False,
             "why": "That divides the larger by the smaller; a low reading "
                    "cannot be more than the label."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s13",
        "band": "standard",
        "text": "A portion holds 740 kJ, and the food gives 37 kJ for each "
                "gram. What is the mass of the portion?",
        "options": [
            {"text": "27 380 g", "correct": False,
             "why": "That multiplies the two, and multiplying would give an "
                    "energy rather than a mass."},
            {"text": "703 g", "correct": False,
             "why": "That subtracts, and an energy density cannot be taken "
                    "away from an energy."},
            {"text": "20 g", "correct": True},
            {"text": "0.05 g", "correct": False,
             "why": "That is 37 ÷ 740, the division the wrong way up; a "
                    "twentieth of a gram holds almost nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s14",
        "band": "standard",
        "text": "Which change to a run would leave the energy per gram "
                "unchanged?",
        "options": [
            {"text": "Letting the sample go out before it has finished "
                     "burning",
             "correct": False,
             "why": "Part of the store is then never released, so the figure "
                    "comes out lower still."},
            {"text": "Holding the burning sample further below the tube",
             "correct": False,
             "why": "More energy escapes sideways on the way up, which drops "
                    "the reading."},
            {"text": "Using a food with a higher fat content",
             "correct": False,
             "why": "More fat means more energy in every gram, so the figure "
                    "would rise."},
            {"text": "Burning a larger sample of the same food",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s15",
        "band": "standard",
        "text": "Why do packets give an energy figure for every 100 g as well "
                "as for one portion?",
        "options": [
            {"text": "So that two foods can be compared on the same amount",
             "correct": True},
            {"text": "Because a portion is too small a mass to measure "
                     "reliably",
             "correct": False,
             "why": "Portions are weighed perfectly well; the second figure is "
                    "there for comparison."},
            {"text": "Because the law requires an energy figure to appear "
                     "twice",
             "correct": False,
             "why": "What the rules want is a comparable figure, not the same "
                    "number printed again."},
            {"text": "So that the kcal and the kJ figures can be checked "
                     "against each other",
             "correct": False,
             "why": "Both units appear against both amounts, so this is not "
                    "what the 100 g column is for."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s16",
        "band": "standard",
        "text": "Respiration and burning release nearly the same energy from a "
                "food. What is different about respiration?",
        "options": [
            {"text": "It releases the energy without oxygen",
             "correct": False,
             "why": "Oxygen is used in both. The difference is in how the "
                    "release is managed."},
            {"text": "It happens in many small steps at about 37 °C",
             "correct": True},
            {"text": "It creates extra energy that was not in the food to "
                     "begin with",
             "correct": False,
             "why": "Nothing creates energy. Both routes empty a store that "
                    "was already there."},
            {"text": "It leaves the chemical store in the food almost "
                     "untouched",
             "correct": False,
             "why": "The store is emptied either way — that is why the two "
                    "figures are so close."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s17",
        "band": "standard",
        "text": "Why do packets carry a kilojoule figure as well as a "
                "kilocalorie one?",
        "options": [
            {"text": "Because the two figures are worked out by different "
                     "laboratories",
             "correct": False,
             "why": "One figure is converted from the other; no second "
                    "measurement is made."},
            {"text": "Because one counts the fat and the other counts "
                     "everything else",
             "correct": False,
             "why": "Neither unit belongs to a food group. Both describe the "
                    "whole of the energy."},
            {"text": "Because the kJ is the scientific unit and the kcal is "
                     "the familiar one",
             "correct": True},
            {"text": "Because shops abroad are not allowed to print "
                     "kilocalories at all",
             "correct": False,
             "why": "Both units appear on labels in many countries; "
                    "familiarity is the reason, not a ban."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s18",
        "band": "standard",
        "text": "A bench reads 6.5 kJ/g for a food whose packet says "
                "17 kJ/g. Is that a believable school result?",
        "options": [
            {"text": "No — a reading below half the packet figure means the "
                     "sample was the wrong one",
             "correct": False,
             "why": "Readings well below half are normal here, whatever "
                    "sample is used."},
            {"text": "No — a school bench should agree with the packet to "
                     "within a kilojoule",
             "correct": False,
             "why": "No school calorimeter comes that close. The leaks are far "
                    "too large."},
            {"text": "Yes — but only if the sample was a fatty one rather "
                     "than a dry one",
             "correct": False,
             "why": "How fatty the food is changes the packet figure, not "
                    "whether the bench reads low."},
            {"text": "Yes — a school bench typically reads about a third of "
                     "the packet figure", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s19",
        "band": "standard",
        "text": "How does the glass of the boiling tube push the measured "
                "value down?",
        "options": [
            {"text": "It absorbs some of the energy, which the thermometer "
                     "never sees", "correct": True},
            {"text": "It reflects some of the flame back down onto the "
                     "sample",
             "correct": False,
             "why": "Glass does not send the flame back, and doing so would "
                    "raise the reading rather than lower it."},
            {"text": "It stops the water above it from being warmed at all",
             "correct": False,
             "why": "The water certainly warms — that rise is the whole "
                    "measurement."},
            {"text": "It adds mass to the sample, so the per-gram figure comes "
                     "out small",
             "correct": False,
             "why": "The tube is never weighed with the sample, so it cannot "
                    "enter the calculation."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s20",
        "band": "standard",
        "text": "Five runs on one food give 7.1, 8.6, 6.4, 9.0 and 7.8 kJ/g. "
                "What does that spread show?",
        "options": [
            {"text": "That the apparatus has no systematic error left in it",
             "correct": False,
             "why": "The leak is still there. Scatter and a one-way loss can "
                    "sit in the same set of results."},
            {"text": "That random error is affecting the runs", "correct": True},
            {"text": "That the packet figure must itself be unreliable",
             "correct": False,
             "why": "Nothing here tests the packet. The spread is evidence "
                    "about the bench."},
            {"text": "That the food's energy density changes from sample to "
                     "sample",
             "correct": False,
             "why": "The food is the same throughout; it is the measuring that "
                    "varies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s21",
        "band": "standard",
        "text": "Cheese gives 17 kJ for each gram. Calculate the energy held "
                "by a 60 g wedge.",
        "options": [
            {"text": "77 kJ", "correct": False,
             "why": "That adds the two figures, which cannot be done to a mass "
                    "and an energy density."},
            {"text": "3.53 kJ", "correct": False,
             "why": "That is 60 ÷ 17, a division where the working needs a "
                    "multiplication."},
            {"text": "1020 kJ", "correct": True},
            {"text": "0.28 kJ", "correct": False,
             "why": "That is 17 ÷ 60, upside down as well as the wrong "
                    "operation entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s22",
        "band": "standard",
        "text": "A bar is labelled 1050 kJ. Roughly what kilocalorie figure "
                "will the same label show?",
        "options": [
            {"text": "About 4389 kcal", "correct": False,
             "why": "That multiplies by 4.18, and a kcal figure is always "
                    "smaller than the kJ one beside it."},
            {"text": "About 1050 kcal", "correct": False,
             "why": "The two numbers on a label are never equal, because the "
                    "units are different sizes."},
            {"text": "About 105 kcal", "correct": False,
             "why": "That divides by ten, and the factor between these units "
                    "is 4.18."},
            {"text": "About 250 kcal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s23",
        "band": "standard",
        "text": "Which quantity does the calorimeter measure directly, and "
                "which one has to be worked out?",
        "options": [
            {"text": "The temperature rise is measured; the energy is "
                     "calculated", "correct": True},
            {"text": "The energy is measured; the temperature rise is "
                     "calculated",
             "correct": False,
             "why": "Nothing on the bench reads joules. The thermometer is "
                    "what gives a number."},
            {"text": "Both are measured, and the mass is the only calculated "
                     "figure",
             "correct": False,
             "why": "The mass is weighed on a balance, so it is measured "
                    "rather than worked out."},
            {"text": "Both are calculated, from the mass of the sample that "
                     "burnt away",
             "correct": False,
             "why": "A mass alone cannot give either. The water's rise has to "
                    "be read."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s24",
        "band": "standard",
        "text": "A sample goes out before it is fully burnt. Why does the "
                "reading come out low?",
        "options": [
            {"text": "Because the balance recorded a mass that had already "
                     "changed",
             "correct": False,
             "why": "The sample is weighed before the run, so the mass "
                    "recorded is the right one."},
            {"text": "Because part of its chemical store was never released",
             "correct": True},
            {"text": "Because a dying flame warms the room rather than the "
                     "tube",
             "correct": False,
             "why": "A flame warms the room throughout. What matters here is "
                    "the energy still locked in the sample."},
            {"text": "Because the water cools again once the flame has gone "
                     "out",
             "correct": False,
             "why": "The highest reading is taken, so later cooling does not "
                    "enter the figure."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s25",
        "band": "standard",
        "text": "Why is a laboratory calorimeter filled with pure oxygen?",
        "options": [
            {"text": "To keep the sample from catching light until it is "
                     "wanted",
             "correct": False,
             "why": "Pure oxygen does the opposite: it makes burning easier "
                    "and fiercer."},
            {"text": "To add energy of its own to the reaction",
             "correct": False,
             "why": "Oxygen supplies no store. The energy released comes from "
                    "the food."},
            {"text": "To make sure the sample burns completely",
             "correct": True},
            {"text": "To stop the steel vessel from warming while the sample "
                     "burns",
             "correct": False,
             "why": "The vessel warms whatever is inside it, and the water "
                    "bath around it accounts for that."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s26",
        "band": "standard",
        "text": "A puffed snack gives 21.6 kJ/g and a cheese gives 17.0 kJ/g. "
                "Which claim follows from that?",
        "options": [
            {"text": "A 10 g piece of the cheese holds more than a 10 g piece "
                     "of the snack",
             "correct": False,
             "why": "At equal masses the higher figure wins, so it is the "
                    "snack that holds more."},
            {"text": "The cheese must contain no fat at all",
             "correct": False,
             "why": "Cheese is genuinely fatty; it is the water in it that "
                    "drags the per-gram figure down."},
            {"text": "The snack would warm the water by more, whatever mass "
                     "is burnt",
             "correct": False,
             "why": "Burn a large enough piece of cheese and the rise is "
                    "bigger. The mass has to be equal for the comparison."},
            {"text": "Each gram of the snack holds more energy than each gram "
                     "of the cheese", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s27",
        "band": "standard",
        "text": "Why is a packet's energy figure closer to what a body can use "
                "than to what a fire releases?",
        "options": [
            {"text": "The figure already allows for what a body cannot get "
                     "out of the food", "correct": True},
            {"text": "A fire releases less energy than a body does from the "
                     "same food",
             "correct": False,
             "why": "It is the other way round: a fire can release everything, "
                    "and a body cannot."},
            {"text": "The figure is measured by feeding the food to volunteers "
                     "and weighing them",
             "correct": False,
             "why": "It comes from a sealed calorimeter, then is adjusted "
                    "before it is printed."},
            {"text": "A body and a fire release exactly the same energy, so no "
                     "adjustment is needed",
             "correct": False,
             "why": "They are close but not identical, and the label is the "
                    "adjusted figure."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s28",
        "band": "standard",
        "text": "A student explains a reading that is too HIGH by saying "
                "energy escaped to the room. What is wrong with that?",
        "options": [
            {"text": "Energy escaping is too small an effect to change a "
                     "reading at all",
             "correct": False,
             "why": "It is the largest loss on the bench, and it changes the "
                    "reading a great deal."},
            {"text": "Escaping energy can only ever push a reading down",
             "correct": True},
            {"text": "Energy cannot escape once the tube is in place",
             "correct": False,
             "why": "It escapes on every run — the tube covers only a small "
                    "part of the flame."},
            {"text": "Escaping energy warms the glass, so it is counted after "
                     "all",
             "correct": False,
             "why": "The glass is not what the thermometer reads, so that "
                    "energy is still lost to the measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s29",
        "band": "standard",
        "text": "A burning sample warms 20 g of water by 15 °C. Water needs "
                "4.18 J for each gram for each degree. How much energy reached "
                "the water?",
        "options": [
            {"text": "84 J", "correct": False,
             "why": "That leaves the mass of water out, using only the rise "
                    "and the constant."},
            {"text": "313 J", "correct": False,
             "why": "That multiplies the mass by the rise and forgets the "
                    "4.18 altogether."},
            {"text": "1254 J", "correct": True},
            {"text": "12 540 J", "correct": False,
             "why": "That is ten times too large; 20 × 4.18 × 15 comes to just "
                    "over twelve hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-s30",
        "band": "standard",
        "text": "Why is energy per gram a fairer way to compare two foods than "
                "energy per portion?",
        "options": [
            {"text": "Because a portion of one food can be a completely "
                     "different mass from a portion of the other",
             "correct": True},
            {"text": "Because a per-gram figure includes the water in a food "
                     "and a portion figure does not",
             "correct": False,
             "why": "Water is in both figures. What differs between them is "
                    "the amount being described."},
            {"text": "Because portions are quoted in kilocalories while "
                     "per-gram figures are quoted in kilojoules",
             "correct": False,
             "why": "Both units appear against both amounts on a UK label."},
            {"text": "Because a per-gram figure is measured and a portion "
                     "figure is only ever estimated",
             "correct": False,
             "why": "Both come from the same measurement; one is simply "
                    "multiplied by the portion mass."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p2-01-h12",
        "band": "harder",
        "text": "Burning 0.50 g of a snack warms 20 g of water by 50 °C. Water "
                "needs 4.18 J per gram per degree. What is the measured energy "
                "per gram?",
        "options": [
            {"text": "About 0.21 kJ/g", "correct": False,
             "why": "That uses the sample's mass in place of the water's, "
                    "which is not what the thermometer measured."},
            {"text": "About 2.0 kJ/g", "correct": False,
             "why": "That leaves the 4.18 out, so the water is treated as "
                    "though a joule warmed a gram by a degree."},
            {"text": "About 8.4 kJ/g", "correct": True},
            {"text": "About 4.2 kJ/g", "correct": False,
             "why": "That is the energy for the whole sample, with the final "
                    "division by 0.50 g never done."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h13",
        "band": "harder",
        "text": "Two students get 8.1 and 8.3 kJ/g for one food; a third gets "
                "2.1 kJ/g with the same apparatus. What fits best?",
        "options": [
            {"text": "The third student used a food with a far lower energy "
                     "density than the others",
             "correct": False,
             "why": "The food is stated to be the same, so its energy density "
                    "cannot be the difference."},
            {"text": "The third student's thermometer was reading far more "
                     "accurately than the other two",
             "correct": False,
             "why": "A more accurate thermometer would move the value towards "
                    "the label, not away from it."},
            {"text": "The first two results must both be wrong, because two "
                     "readings cannot agree by chance",
             "correct": False,
             "why": "Agreement between repeats is ordinary. It is the outlier "
                    "that wants explaining."},
            {"text": "The third student's sample went out early, so part of "
                     "its store was never released", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h14",
        "band": "harder",
        "text": "Which sort of food would you expect to show the biggest gap "
                "between a bench reading and its packet figure?",
        "options": [
            {"text": "A wet, fatty food such as cheese", "correct": True},
            {"text": "A dry, puffed snack that lights straight away",
             "correct": False,
             "why": "It burns quickly and completely and carries little water, "
                    "so it comes closest to its label."},
            {"text": "A dry carbohydrate such as pasta", "correct": False,
             "why": "Dry food loses nothing to warming its own water, so the "
                    "gap is smaller than cheese's."},
            {"text": "Any food with a high energy density, whatever else is in "
                     "it",
             "correct": False,
             "why": "Crisps are the densest on the bench and come closest of "
                    "all to their label."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h15",
        "band": "harder",
        "text": "A student wraps foil round the boiling tube to shield it. "
                "Predict the effect on the reading.",
        "options": [
            {"text": "It rises above the packet figure, because the energy is "
                     "now trapped",
             "correct": False,
             "why": "No shield can capture more than the sample released, so "
                    "the packet figure is still a ceiling."},
            {"text": "It rises, but still stays below the packet figure",
             "correct": True},
            {"text": "It falls, because the foil absorbs energy",
             "correct": False,
             "why": "The foil keeps draughts off and returns energy towards "
                    "the tube; the reading improves."},
            {"text": "It is unchanged, whether the foil is there or not",
             "correct": False,
             "why": "A systematic error can be reduced by changing the "
                    "apparatus — that is exactly what a shield does."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h16",
        "band": "harder",
        "text": "A sealed laboratory calorimeter and a school one burn "
                "identical 1.0 g samples. Which statement is true?",
        "options": [
            {"text": "The sealed one releases more energy, because pure oxygen "
                     "adds to the reaction",
             "correct": False,
             "why": "Oxygen holds no store of its own; it only lets the "
                    "sample finish burning."},
            {"text": "The school one releases more, because its flame is "
                      "hotter",
             "correct": False,
             "why": "A hotter flame does not mean a bigger store. The store is "
                    "a property of the sample."},
            {"text": "The same store is released; only the energy captured "
                     "differs", "correct": True},
            {"text": "The two release different amounts, because energy "
                     "depends on the apparatus used",
             "correct": False,
             "why": "The energy in a sample is fixed before any apparatus "
                    "touches it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h17",
        "band": "harder",
        "text": "One snack is 40 g at 25 kJ/g; another is 70 g at 14 kJ/g. "
                "Which holds more, and by how much?",
        "options": [
            {"text": "The second, by 20 kJ",
             "correct": False,
             "why": "Being heavier is not enough: 70 × 14 comes to 980, which "
                    "is the smaller total."},
            {"text": "The second, by 940 kJ",
             "correct": False,
             "why": "70 × 14 is 980, not 1940, so this compares a figure that "
                    "was never produced."},
            {"text": "Neither — both come to 1000 kJ",
             "correct": False,
             "why": "Only the first comes to 1000. The second falls 20 kJ "
                    "short of it."},
            {"text": "The first, by 20 kJ", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h18",
        "band": "harder",
        "text": "A packet gives 1700 kJ per 100 g. How much energy is in a "
                "35 g bag of it?",
        "options": [
            {"text": "595 kJ", "correct": True},
            {"text": "59 500 kJ", "correct": False,
             "why": "That multiplies 1700 by 35 without ever dividing by the "
                    "hundred grams the figure is quoted for."},
            {"text": "48.6 kJ", "correct": False,
             "why": "That is 1700 ÷ 35, a division where the working needs a "
                    "per-gram figure first."},
            {"text": "1735 kJ", "correct": False,
             "why": "That adds the mass to the energy, which cannot be done to "
                    "two different quantities."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h19",
        "band": "harder",
        "text": "Fibre passes through a body almost untouched, yet it burns "
                "and warms the water on the bench. Why?",
        "options": [
            {"text": "The flame is hotter than a body, so it destroys "
                     "particles a body can only move around",
             "correct": False,
             "why": "Nothing destroys particles in either case. Both routes "
                    "rearrange them."},
            {"text": "Burning rearranges the particles anyway, while a body "
                     "lacks what it needs to break fibre down",
             "correct": True},
            {"text": "Fibre takes in energy from the flame and gives it back "
                     "to the water unchanged",
             "correct": False,
             "why": "The energy that warms the water comes out of the fibre's "
                    "own chemical store."},
            {"text": "The mass of fibre is so small that the reading comes "
                     "from the rest of the sample",
             "correct": False,
             "why": "A sample of pure fibre burns and warms the water on its "
                    "own, whatever else is absent."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h20",
        "band": "harder",
        "text": "A student reads 250 Calories off a packet and writes 250 "
                "calories into a physics calculation. By what factor is the "
                "figure wrong?",
        "options": [
            {"text": "It is 4.18 times too small", "correct": False,
             "why": "That is the factor between a kilocalorie and a kilojoule, "
                    "which is a different conversion."},
            {"text": "It is 100 times too small", "correct": False,
             "why": "A kilo means a thousand, in this unit as in every other."},
            {"text": "It is 1000 times too small", "correct": True},
            {"text": "It is not wrong, because the two calories are the same "
                     "size",
             "correct": False,
             "why": "The label's Calorie warms a kilogram of water; the "
                    "physicist's warms a gram."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h21",
        "band": "harder",
        "text": "How could a run be changed to give a bigger temperature rise "
                "without changing the energy per gram?",
        "options": [
            {"text": "Burn a food with more fat in it than the last one had",
             "correct": False,
             "why": "That changes the energy per gram itself, which is the one "
                    "thing being held fixed."},
            {"text": "Hold the flame further away so it burns for longer",
             "correct": False,
             "why": "More energy escapes on the way up, so the rise falls "
                    "rather than grows."},
            {"text": "Stir the water as it warms",
             "correct": False,
             "why": "Stirring evens the temperature out; it does not put more "
                    "energy into the water."},
            {"text": "Put less water in the tube", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h22",
        "band": "harder",
        "text": "A packet figure is produced by a sealed calorimeter and then "
                "adjusted before it is printed. What is the adjustment for?",
        "options": [
            {"text": "A body cannot release everything a fire can",
             "correct": True},
            {"text": "The sealed apparatus also reads low",
             "correct": False,
             "why": "A sealed calorimeter closes those escape routes, so it "
                    "does not read low."},
            {"text": "Food loses energy while it sits on a shelf, so the "
                     "figure is reduced to allow for it",
             "correct": False,
             "why": "A sealed packet's chemical store does not drain away on a "
                    "shelf."},
            {"text": "The kilocalorie figure has to be rounded before the "
                     "kilojoule figure can be printed",
             "correct": False,
             "why": "Rounding changes the last digit. The adjustment here is "
                    "about what a body can use."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h23",
        "band": "harder",
        "text": "Compare the errors in a school calorimeter with those in a "
                "sealed laboratory one. Which statement is correct?",
        "options": [
            {"text": "Both have errors that run in both directions, so both "
                     "need repeating",
             "correct": False,
             "why": "The school bench's errors all run one way, which is what "
                    "makes repeating useless there."},
            {"text": "The school version's losses all run one way; the sealed "
                     "version closes those routes", "correct": True},
            {"text": "The sealed version has larger errors, because the "
                     "pressure inside it is so high",
             "correct": False,
             "why": "Pressure is what makes the burn complete. It is not a "
                    "source of error."},
            {"text": "Neither has any error, because both burn the whole "
                     "sample in the end",
             "correct": False,
             "why": "Burning the whole sample is only one of the school "
                    "bench's problems, and it still loses energy sideways."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h24",
        "band": "harder",
        "text": "Which result would be impossible on a school bench, and why?",
        "options": [
            {"text": "A value a long way below the packet figure, because the "
                     "losses are never that large",
             "correct": False,
             "why": "Values well below half the packet are the ordinary "
                    "result here."},
            {"text": "Two repeats agreeing closely",
             "correct": False,
             "why": "Repeats often agree closely. That is precision, and it "
                    "comes easily."},
            {"text": "A value above the packet figure", "correct": True},
            {"text": "A value exactly equal to another group's, because no two "
                     "samples burn alike",
             "correct": False,
             "why": "Two groups can certainly land on the same figure; nothing "
                    "prevents it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h25",
        "band": "harder",
        "text": "One set of repeats is 8.1, 8.2, 8.3 kJ/g and another is 6.0, "
                "9.5, 11.0 kJ/g, both well below the packet. What differs?",
        "options": [
            {"text": "The first set has a systematic error and the second has "
                     "none at all",
             "correct": False,
             "why": "Both sit well below the packet, so both carry the same "
                    "one-way loss."},
            {"text": "The second set is more accurate, because its highest "
                     "reading is nearer the packet",
             "correct": False,
             "why": "One reading drifting upwards is scatter, not accuracy."},
            {"text": "The first set is closer to the packet figure than the "
                     "second one is",
             "correct": False,
             "why": "Their averages are much the same; it is the spread that "
                    "separates them."},
            {"text": "The second set carries far more random scatter on top of "
                     "the same one-way loss", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h26",
        "band": "harder",
        "text": "A bench reads 6.8 kJ/g and captures roughly a third of what "
                "is released. Estimate the packet figure.",
        "options": [
            {"text": "About 20 kJ/g", "correct": True},
            {"text": "About 2.3 kJ/g", "correct": False,
             "why": "That divides by three, which would make the packet figure "
                    "smaller than the bench reading."},
            {"text": "About 6.8 kJ/g", "correct": False,
             "why": "That is the reading itself, and the whole point is that "
                    "the packet figure sits above it."},
            {"text": "About 68 kJ/g", "correct": False,
             "why": "That is above the figure for pure fat, which no food can "
                    "exceed."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h27",
        "band": "harder",
        "text": "Why does one gram of fat hold more energy than one gram of "
                "carbohydrate?",
        "options": [
            {"text": "Because fat is denser, so a gram of it takes up less "
                     "room",
             "correct": False,
             "why": "Fat is actually the less dense of the two by volume, and "
                    "volume is not what the figure describes."},
            {"text": "Because its particles are arranged so that more is "
                     "released when they rearrange", "correct": True},
            {"text": "Because fat burns at a higher temperature than "
                     "carbohydrate does",
             "correct": False,
             "why": "How hot the flame gets is not the same as how much "
                    "energy the store holds."},
            {"text": "Because fat takes longer to digest, so more energy comes "
                     "out of it",
             "correct": False,
             "why": "Digestion time changes how fast it arrives, never how "
                    "much there was."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h28",
        "band": "harder",
        "text": "A bag is labelled 180 kcal and a bar is labelled 800 kJ. "
                "Which holds more energy?",
        "options": [
            {"text": "The bag, because 180 kcal converts to about 4400 kJ",
             "correct": False,
             "why": "That multiplies by more than twenty. The factor between "
                    "the units is 4.18."},
            {"text": "The bar, because kilojoules are always the larger unit "
                     "of the two",
             "correct": False,
             "why": "The bar does win, but not for that reason — the figures "
                    "have to be converted and compared."},
            {"text": "The bar, because 180 kcal is only about 750 kJ",
             "correct": True},
            {"text": "Neither — the two units cannot be compared without the "
                     "masses as well",
             "correct": False,
             "why": "Both are totals in energy units, so converting one is all "
                    "that is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h29",
        "band": "harder",
        "text": "A puffed snack's bench reading sits closer to its packet "
                "figure than a wet cheese's does. Suggest why.",
        "options": [
            {"text": "The snack holds more energy in every gram, so a larger "
                     "share of it survives the journey",
             "correct": False,
             "why": "A bigger store does not mean a larger fraction reaches "
                    "the water; those are separate things."},
            {"text": "The cheese is the heavier sample, so the balance reads "
                     "it less precisely",
             "correct": False,
             "why": "Both are weighed on the same balance, and the per-gram "
                    "figure divides the mass back out."},
            {"text": "The packet figure for a cheese is measured in a "
                     "different way from a snack's",
             "correct": False,
             "why": "Every packet figure comes from the same sort of sealed "
                    "apparatus."},
            {"text": "The snack burns quickly and completely and carries "
                     "almost no water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-01-h30",
        "band": "harder",
        "text": "Two foods are to be compared fairly on the bench. Which "
                "control matters most?",
        "options": [
            {"text": "The same mass of water and the same distance below the "
                     "tube each time", "correct": True},
            {"text": "The same mass of food, so that both runs release the "
                     "same energy",
             "correct": False,
             "why": "Equal masses do not release equal energy, and the "
                    "per-gram figure divides the mass out anyway."},
            {"text": "The same room temperature, so that both samples start "
                     "from the same point",
             "correct": False,
             "why": "It is the rise that is measured, and a rise is already a "
                    "difference between two readings."},
            {"text": "The same burning time, so that neither sample is given "
                     "longer than the other",
             "correct": False,
             "why": "A sample is burnt until it stops; timing it would cut one "
                    "run short."},
        ],
        "figure": None,
    },
]
