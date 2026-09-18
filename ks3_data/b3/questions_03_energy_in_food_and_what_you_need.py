"""B3 lesson 03 — Energy in food and what you need: twelve questions (MRB-269).

The lesson's one claim is that a requirement belongs to the PERSON and never to
the food, so a plate of food means nothing until you say whose day it is. These
twelve probe that: the unit itself (kJ, and what a kilojoule is), what a
requirement is set by, the ordering of the five eaters on the bench, the
ledger's own experiment (switch the person, keep the food), the surplus /
shortfall comparison as arithmetic, and — in the harder band — the same rule
carried into contexts the lesson does not draw: an injured bricklayer at a desk,
a rower who cannot eat enough, a smaller person who needs more than a bigger
one, and a bomb calorimeter that reads high.

The distractors are built from the lesson's two declared misconceptions —
DIET-07 "everyone needs about the same amount of food in a day" (which reappears
as "9000 kJ is 9000 kJ, whoever is eating it", "everyone is given the same daily
figure", and "the figures must be wrong, a bigger body always needs more") and
DIET-06 "the energy in food gets used up and disappears" (as "it no longer
exists", "anything left over was destroyed", and "training destroys energy") —
plus the hook's own wager options (better digestion, an old body that stores
instead of using, and "11 000 kJ is the wrong amount for both"), and the error
the confrontation names: that the requirement can somehow belong to the packet.
"""

UNIT = "B3"
LESSON = "energy-in-food-and-what-you-need"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-03-e01",
        "band": "easier",
        "text": "A packet of biscuits sits on the table and a person picks it "
                "up. Which of those two does an energy requirement belong to?",
        "options": [
            {"text": "The person — set by their size, age, growth and how "
                     "much they move",
             "correct": True},
            {"text": "The packet — the requirement is the figure printed on "
                     "the side of it",
             "correct": False,
             "why": "That figure is the food's energy value: how much energy "
                    "is in it. A requirement is what a body needs over a day, "
                    "and a packet cannot know who is holding it."},
            {"text": "Both — the food has a requirement and so does the "
                     "person eating it",
             "correct": False,
             "why": "Only the person has a requirement. Food has an energy "
                    "value, and the two numbers are compared against each "
                    "other; they are not the same kind of number."},
            {"text": "Neither — everyone is given the same daily figure to "
                     "eat to",
             "correct": False,
             "why": "That is the 2000-calorie idea. It is a labelling "
                    "convention — a rounded average for one kind of adult — "
                    "not a figure that belongs to you."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e02",
        "band": "easier",
        "text": "Energy in food is measured in kilojoules, written kJ. What "
                "is one kilojoule?",
        "options": [
            {"text": "One thousandth of a joule, which is why packet figures "
                     "run so high",
             "correct": False,
             "why": "Kilo- means a thousand times bigger, not smaller. A "
                    "chocolate bar is 1050 kJ, which is over a million "
                    "joules — the figures are high because the unit is big."},
            {"text": "The energy in one gram of food, whichever food it "
                     "happens to be",
             "correct": False,
             "why": "A kilojoule measures energy, not mass. The same gram of "
                    "different foods carries very different energy, which is "
                    "why packets do not all print the same number."},
            {"text": "A thousand joules — a unit of energy, the same one "
                     "physics uses",
             "correct": True},
            {"text": "The energy one person needs each hour, so a day comes "
                     "to 24 kJ",
             "correct": False,
             "why": "A kilojoule is a fixed amount of energy and has nothing "
                    "to do with a person or an hour. A day's requirement runs "
                    "to thousands of kJ, not tens."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e03",
        "band": "easier",
        "text": "Of the five people on the bench, which one has the largest "
                "daily energy requirement?",
        "options": [
            {"text": "The adult doing heavy manual work, at 13 500 kJ a day",
             "correct": False,
             "why": "13 500 kJ is a lot, but the rower's 25 000 kJ is nearly "
                    "double it — six hours of hard training on top of a large "
                    "muscular body."},
            {"text": "The Olympic rower in training, at 25 000 kJ a day",
             "correct": True},
            {"text": "The 13-year-old, because adolescent growth is the most "
                     "expensive stage",
             "correct": False,
             "why": "Adolescent growth is expensive — 9500 kJ, almost an "
                    "adult's — but it still sits below an adult doing heavy "
                    "manual work, and well below the rower."},
            {"text": "The 4-year-old, because a small child grows fastest of "
                     "all five",
             "correct": False,
             "why": "Growing fastest does not mean needing most. The "
                    "4-year-old's 5800 kJ is the smallest of the five, "
                    "because there is so little body to fuel and keep warm."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e04",
        "band": "easier",
        "text": "A question asks what a person's daily energy requirement "
                "depends on. Which list is the right one?",
        "options": [
            {"text": "Their body mass alone — a heavier person always needs "
                     "more energy",
             "correct": False,
             "why": "Size is one term, not the whole answer. The office "
                    "worker and the bricklayer are the same size and differ "
                    "by 4500 kJ a day, and that difference is activity."},
            {"text": "How much they enjoy their food, and how quickly they "
                     "eat it",
             "correct": False,
             "why": "Neither changes how much energy the body transfers in a "
                    "day. A requirement is set by the work the body is doing, "
                    "not by how appealing the meal was."},
            {"text": "The energy values printed on the packets they happen to "
                     "choose",
             "correct": False,
             "why": "That is intake — what goes in. The requirement is fixed "
                    "by the person before any food is chosen, and the two are "
                    "then compared."},
            {"text": "Their age, size, sex, rate of growth and level of "
                     "activity",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-03-s01",
        "band": "standard",
        "text": "Two people eat identical meals for a month, about 11 000 kJ "
                "a day each. The 68-year-old who reads all day gains mass; "
                "the cyclist covering 120 km a day loses it. What explains "
                "the split?",
        "options": [
            {"text": "The cyclist's gut is more efficient, so much less of "
                     "the food ever reaches his stores",
             "correct": False,
             "why": "Digestion is not what differs here. Both take in about "
                    "11 000 kJ; what differs is how much energy each body "
                    "transfers over the day."},
            {"text": "Their bodies transfer very different amounts each day, "
                     "so one is in surplus and one short",
             "correct": True},
            {"text": "The older man's body simply stores food instead of "
                     "using it, whatever he happens to eat",
             "correct": False,
             "why": "No body stores food instead of transferring energy. He "
                    "stores the surplus because his requirement is low, not "
                    "because storing is what age does."},
            {"text": "11 000 kJ is simply the wrong amount of food for both "
                     "of these people",
             "correct": False,
             "why": "There is no right amount. 11 000 kJ is a surplus for one "
                    "of these two and a shortfall for the other — the number "
                    "means nothing until you say whose day it is."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s02",
        "band": "standard",
        "text": "You build a day on the bench that totals 9000 kJ and it "
                "balances for the office worker. Without changing a single "
                "item of food, you switch the person to the bricklayer. What "
                "is that same plate now?",
        "options": [
            {"text": "A shortfall of 4500 kJ — the requirement changed and "
                     "the food did not",
             "correct": True},
            {"text": "Still balanced, because 9000 kJ is 9000 kJ whoever "
                     "happens to be eating it",
             "correct": False,
             "why": "The intake is unchanged, but balance is a comparison. "
                    "The bricklayer needs 13 500 kJ, so the same plate now "
                    "falls 4500 kJ short of him."},
            {"text": "A surplus of 4500 kJ, because a working body burns "
                     "through food faster",
             "correct": False,
             "why": "Working harder raises what he needs, so the same food "
                    "gets further from meeting it, not closer. That is a "
                    "shortfall, not a surplus."},
            {"text": "The same food, now carrying more energy because he "
                     "works harder for it",
             "correct": False,
             "why": "A food's energy value is fixed before anyone eats it. "
                    "Nothing about the eater changes the kJ in a plate of "
                    "pasta — only the requirement it is measured against."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s03",
        "band": "standard",
        "text": "You eat a 1100 kJ bowl of cereal in the morning. By bedtime, "
                "where has that energy got to?",
        "options": [
            {"text": "It was used up during the day, so by bedtime it no "
                     "longer exists",
             "correct": False,
             "why": "Nothing about using energy destroys it. It has been "
                    "transferred somewhere else — mostly to the thermal store "
                    "of your surroundings, which is why a small room warms."},
            {"text": "Movement burned off what it could, and the rest was "
                     "destroyed by digestion",
             "correct": False,
             "why": "Movement takes a share, but nothing destroys the rest. "
                    "Most of it ends up warming your surroundings — you are "
                    "roughly a 70-watt heater."},
            {"text": "All of it is still stored in your body until you next "
                     "exercise hard",
             "correct": False,
             "why": "Only a surplus is stored. Most of that cereal's energy "
                    "was transferred as the day went on, a great deal of it "
                    "warming the air around you."},
            {"text": "Transferred — some to movement, some to new tissue, "
                     "most to your surroundings",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s04",
        "band": "standard",
        "text": "A bricklayer needs 13 500 kJ a day. He eats two bowls of "
                "cereal (1100 kJ each), jollof rice and chicken (2100 kJ), "
                "pasta and sauce (2400 kJ) and a glass of water. How does his "
                "day compare with what he needs?",
        "options": [
            {"text": "5600 kJ, which leaves a shortfall of 7900 kJ against "
                     "his daily requirement",
             "correct": False,
             "why": "You have counted one bowl of cereal where there are two. "
                    "Check the portion counts before you add — it is the "
                    "commonest slip in this kind of question."},
            {"text": "6700 kJ, which is a surplus of 6800 kJ, so the extra is "
                     "stored",
             "correct": False,
             "why": "The arithmetic is right and the comparison is upside "
                    "down. 6700 kJ is less than 13 500 kJ, so it is a "
                    "shortfall, not a surplus."},
            {"text": "6700 kJ, a shortfall of 6800 kJ, so his stores are "
                     "drawn on",
             "correct": True},
            {"text": "6700 kJ plus whatever the water adds, so a little more "
                     "than 6700 kJ",
             "correct": False,
             "why": "A glass of water carries no energy at all — 0 kJ. It "
                    "matters to the body for other reasons, but it adds "
                    "nothing to a day's energy total."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-03-h01",
        "band": "harder",
        "text": "An Olympic rower says the hardest part of training is not "
                "the training — it is eating enough. Why is that a real "
                "problem for him and not for most people?",
        "options": [
            {"text": "An athlete's body stops taking energy in once a daily "
                     "limit has been reached",
             "correct": False,
             "why": "There is no such limit. The difficulty is on the eating "
                    "side: 25 000 kJ is an enormous quantity of food to get "
                    "through, not an amount the body refuses."},
            {"text": "He needs a different kind of food rather than more of "
                     "it, and that is hard to find",
             "correct": False,
             "why": "It is quantity, not kind. His requirement is 25 000 kJ — "
                    "more than four times a 4-year-old's day — and that has "
                    "to be met with sheer volume of food."},
            {"text": "His requirement is 25 000 kJ, so matching it takes more "
                     "food than appetite easily allows",
             "correct": True},
            {"text": "Hard training destroys energy, so no amount of eating "
                     "can ever replace it",
             "correct": False,
             "why": "Nothing destroys energy. Training transfers it, to "
                    "movement and to warming his surroundings, and eating "
                    "replaces exactly that — which is why the total is so "
                    "large."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h02",
        "band": "harder",
        "text": "A bricklayer breaks his arm and spends six weeks at a desk. "
                "He eats exactly what he ate before, portion for portion. "
                "Predict what happens.",
        "options": [
            {"text": "Nothing changes — it is the same body at the same size, "
                     "so the same requirement",
             "correct": False,
             "why": "Size is only one term. This is one body doing two "
                    "different jobs, and activity alone separates 13 500 kJ a "
                    "day from about 9000 kJ."},
            {"text": "His requirement drops by about 4500 kJ a day, so the "
                     "same food becomes a surplus and is stored",
             "correct": True},
            {"text": "He runs short of energy, because he is no longer moving "
                     "enough to release it from his food each day",
             "correct": False,
             "why": "Moving does not release energy from food; it spends it. "
                    "Moving less means needing less, so the same food leaves "
                    "him with more than he needs, not less."},
            {"text": "His food carries less energy now, because a resting "
                     "body gets less out of it",
             "correct": False,
             "why": "The kJ in his lunch is fixed before he eats it. What has "
                    "changed is the requirement it is being compared with, "
                    "not the food."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h03",
        "band": "harder",
        "text": "A sample of bran is burned in a bomb calorimeter and gives "
                "900 kJ. The figure a food packet prints for that same sample "
                "is lower. Why?",
        "options": [
            {"text": "The calorimeter burns fibre your gut cannot digest, so "
                     "it measures more than a body gets",
             "correct": True},
            {"text": "Some energy escaped as heat during the burn, so the "
                     "packet corrects for what was lost",
             "correct": False,
             "why": "The heat is what the calorimeter measures — the rise in "
                    "the water's temperature is the reading. Nothing escapes "
                    "it; the gap is about digestion, not loss."},
            {"text": "Burning destroys part of the sample's energy, so the "
                     "instrument can only record what is left",
             "correct": False,
             "why": "Burning does not destroy energy, it transfers it, which "
                    "is exactly how the instrument works. The gap is that a "
                    "gut cannot do to fibre what a flame can."},
            {"text": "Packet figures are rounded down by law, so they always "
                     "read lower than the truth",
             "correct": False,
             "why": "The correction was a scientific one, not a legal "
                    "rounding. The fibre figure had to come down because a "
                    "calorimeter happily burns cellulose and you cannot "
                    "digest a gram of it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h04",
        "band": "harder",
        "text": "A 13-year-old needs 9500 kJ a day. A fully grown adult with "
                "a desk job needs 9000 kJ. The adult is the bigger of the "
                "two. How can the smaller person need more?",
        "options": [
            {"text": "The figures must be wrong, because a bigger body always "
                     "needs more energy than a smaller one",
             "correct": False,
             "why": "Size is one term among several. Growth is another, and "
                    "in adolescence it is large enough to more than close a "
                    "gap in body size."},
            {"text": "Teenagers digest their food less efficiently, so they "
                     "have to eat more of it",
             "correct": False,
             "why": "Digestion is not the difference. The teenager's "
                    "requirement is genuinely higher, because their body is "
                    "still building tissue and the adult's is not."},
            {"text": "Teenagers move about more, and activity is the only "
                     "thing that changes a requirement",
             "correct": False,
             "why": "Activity is one term, not the only one — and a desk job "
                    "is named here deliberately. What separates this pair is "
                    "growth."},
            {"text": "Adolescent growth costs energy, and building tissue is "
                     "work the adult no longer pays for",
             "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Nine further rows, three per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window. The harder band is
    # where this lesson's calculation rows belong; all three state units.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-03-e05",
        "band": "easier",
        "text": "A recipe book gives energy in kilocalories and a food packet "
                "gives it in kilojoules. How do those two units compare?",
        "options": [
            {"text": "They are the same size, so the two words are simply "
                     "different names for one unit.", "correct": False,
             "why": "They are different sizes. One kilocalorie is about "
                    "4.2 kJ, so the same food carries a much larger number of "
                    "kilojoules than of kilocalories."},
            {"text": "One kilocalorie is about 4.2 kJ, so it is the larger of "
                     "the two units.", "correct": True},
            {"text": "One kilocalorie is about a thousandth of a kilojoule, "
                     "so it is much the smaller.", "correct": False,
             "why": "That is the wrong way round, and by a long way. A "
                    "kilocalorie is bigger than a kilojoule, not a thousand "
                    "times smaller."},
            {"text": "A kilocalorie measures heat, and a kilojoule measures "
                     "the energy in food.", "correct": False,
             "why": "Both measure energy, and it is the same quantity. A "
                    "kilojoule is used for heat, movement and food alike."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e06",
        "band": "easier",
        "text": "Someone takes in more energy in a day than they transfer. "
                "What is the extra called, and what happens to it?",
        "options": [
            {"text": "A shortfall, and stores are broken down to make up the "
                     "difference.", "correct": False,
             "why": "That is what happens when intake is less than what is "
                    "transferred. This person is taking in more, not less."},
            {"text": "An intake, and the extra is passed out of the body as "
                     "waste.", "correct": False,
             "why": "Intake is the total of everything eaten and drunk, not "
                    "the extra. Extra energy is stored rather than passed "
                    "out."},
            {"text": "A requirement, and it raises the amount that person "
                     "needs the next day.", "correct": False,
             "why": "A requirement belongs to the person and is set by their "
                    "size, age, growth and activity. Eating more does not "
                    "raise it."},
            {"text": "A surplus, and the extra is stored rather than lost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e07",
        "band": "easier",
        "text": "A glass of water is listed at 0 kJ. Why is water on a list of "
                "things a body needs if it carries no energy?",
        "options": [
            {"text": "It is one of the seven nutrients, and a day needs about "
                     "2000 g of it.", "correct": True},
            {"text": "It is a mistake in the list — something carrying no "
                     "energy is not really food.", "correct": False,
             "why": "Water is one of the seven nutrients and the largest "
                    "requirement of all of them. Carrying no energy is not "
                    "the same as not being needed."},
            {"text": "It does carry energy, but too little for a list like "
                     "this one to print a figure for.", "correct": False,
             "why": "The energy in water is zero rather than small, which is "
                    "why the label reads 0 kJ and not a small number."},
            {"text": "It is there so a day can be made to add up to the "
                     "requirement exactly.", "correct": False,
             "why": "Adding water changes a day's energy total by nothing at "
                    "all, so it can never close a gap."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-03-s05",
        "band": "standard",
        "text": "A 4-year-old needing 5800 kJ and an Olympic rower needing "
                "25 000 kJ are each given the same day's food, totalling "
                "9500 kJ. What is that day for each of them?",
        "options": [
            {"text": "A shortfall of about 3700 kJ for the child and a "
                     "surplus for the rower.", "correct": False,
             "why": "That is the right arithmetic on the wrong people. 9500 "
                    "is above the child's 5800 and far below the rower's "
                    "25 000."},
            {"text": "Balanced for both of them, because 9500 kJ is a normal "
                     "day's food for anybody.", "correct": False,
             "why": "9500 kJ is the 13-year-old's requirement and nobody "
                    "else's. A requirement belongs to the person, so there is "
                    "no normal day."},
            {"text": "A surplus of about 3700 kJ for the child and a large "
                     "shortfall for the rower.", "correct": True},
            {"text": "The same for both, because the food carries the same "
                     "energy whoever happens to eat it.", "correct": False,
             "why": "The food does carry the same energy — that is why it is "
                    "the same 9500 kJ. What differs is the requirement it is "
                    "being compared with."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s06",
        "band": "standard",
        "text": "A person's intake matches their requirement exactly, every "
                "day for a month. What happens to their body mass?",
        "options": [
            {"text": "It stays about the same — nothing is stored, and no "
                     "stores are drawn on.", "correct": True},
            {"text": "It falls, because energy is used up by the body as the "
                     "month goes on.", "correct": False,
             "why": "Energy is transferred rather than used up, and with "
                    "intake matching requirement nothing has to come out of "
                    "store to pay for it."},
            {"text": "It rises, because everything eaten over a month has to "
                     "be stored somewhere.", "correct": False,
             "why": "Only a surplus is stored. Energy that matches the "
                    "requirement is transferred as it arrives, so there is "
                    "nothing left over to keep."},
            {"text": "You cannot say, because it depends which foods made up "
                     "the intake.", "correct": False,
             "why": "The comparison is between total energy in and total "
                    "energy transferred. Which foods supplied the total does "
                    "not change that sum."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s07",
        "band": "standard",
        "text": "A day built for the 4-year-old totals 5800 kJ and balances "
                "exactly. Without taking anything away, a handful of nuts "
                "(1250 kJ) is added. What is that day now?",
        "options": [
            {"text": "Still balanced — a handful is far too small a portion "
                     "to change a whole day.", "correct": False,
             "why": "1250 kJ is more than a fifth of this child's entire day. "
                    "A small mass is not a small amount of energy — nuts are "
                    "mostly lipid."},
            {"text": "A shortfall of 1250 kJ, because the extra food has to "
                     "be digested first.", "correct": False,
             "why": "Digesting food does not cost a day 1250 kJ. Adding "
                    "energy to a balanced day makes a surplus, not a "
                    "shortfall."},
            {"text": "Balanced again, once the requirement rises to 7050 kJ "
                     "to match the food.", "correct": False,
             "why": "A requirement is set by the person's size, age, growth "
                    "and activity. Eating more does not move it up to meet "
                    "what was eaten."},
            {"text": "A surplus of 1250 kJ over the child's requirement, and "
                     "the extra is stored.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-03-h05",
        "band": "harder",
        "text": "A pot of yoghurt is 520 kJ. A 4-year-old's requirement is "
                "5800 kJ a day. What share of that child's day is one pot, to "
                "the nearest whole per cent?",
        "options": [
            {"text": "About 6%", "correct": False,
             "why": "That is 520 divided by 9000, an adult desk worker's "
                    "requirement. Use the requirement of the person actually "
                    "eating it: 520 ÷ 5800 × 100."},
            {"text": "About 9%", "correct": True},
            {"text": "About 11%", "correct": False,
             "why": "That is 5800 divided by 520 — the division the wrong way "
                    "round. The share is the portion divided by the "
                    "requirement, not the other way about."},
            {"text": "About 0.09%", "correct": False,
             "why": "That is 520 ÷ 5800 with the × 100 left off. A share as a "
                    "percentage always needs that last step."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h06",
        "band": "harder",
        "text": "A 4-year-old needs 5800 kJ. So far today they have had "
                "cereal (1100 kJ), a banana (450 kJ), two chapatis with dal "
                "(1750 kJ) and an apple (320 kJ). What is left, and which "
                "single item comes closest to filling it — pasta and sauce at "
                "2400 kJ, or jollof rice and chicken at 2100 kJ?",
        "options": [
            {"text": "2180 kJ still to find, and the pasta at 2400 kJ comes "
                     "closest.", "correct": False,
             "why": "The total is right and the choice is not. 2400 kJ "
                    "overshoots by 220 kJ, while 2100 kJ is only 80 kJ "
                    "away."},
            {"text": "3620 kJ still to find, and the pasta at 2400 kJ comes "
                     "closest.", "correct": False,
             "why": "3620 kJ is what has already been eaten, not what is "
                    "left. Subtract it from 5800 kJ to get the gap."},
            {"text": "2180 kJ still to find, and the jollof rice and chicken "
                     "at 2100 kJ comes closest.", "correct": True},
            {"text": "A surplus of 2180 kJ, so nothing more should be added "
                     "at all.", "correct": False,
             "why": "3620 kJ is well below 5800 kJ, so the day is short "
                    "rather than over. A surplus needs intake above "
                    "requirement."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h07",
        "band": "harder",
        "text": "A label prints “2000 kcal — your daily needs” as a reference "
                "figure. Take 1 kcal as 4.2 kJ. What is that reference in kJ, "
                "and what does it say about a bricklayer needing 13 500 kJ?",
        "options": [
            {"text": "About 8400 kJ — well below his 13 500 kJ, so the "
                     "reference does not describe him.", "correct": True},
            {"text": "About 8400 kJ, which is close enough to 13 500 kJ to be "
                     "a fair guide for him.", "correct": False,
             "why": "The conversion is right and the judgement is not. He "
                    "would be about 5100 kJ short, which is more than a third "
                    "of his day."},
            {"text": "About 480 kJ, which is far below anything a person "
                     "could live on for a day.", "correct": False,
             "why": "That is 2000 divided by 4.2 instead of multiplied. A "
                    "kilocalorie is the bigger unit, so the number of "
                    "kilojoules must come out larger."},
            {"text": "About 2000 kJ, because a kilocalorie and a kilojoule "
                     "are two names for one unit.", "correct": False,
             "why": "They are different sizes: one kilocalorie is about "
                    "4.2 kJ, so 2000 kcal is about 8400 kJ."},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b3-03-e08",
        "band": "easier",
        "text": "What does a person's intake mean?",
        "options": [
            {"text": "The total energy in everything they eat and drink over "
                     "a day.", "correct": True},
            {"text": "The energy their body transfers over the course of a "
                     "whole day of work and rest.", "correct": False,
             "why": "That is the requirement side of the sum. Intake is what "
                    "goes in, not what is transferred."},
            {"text": "The mass of food they eat in a day, added up across "
                     "every meal and snack.", "correct": False,
             "why": "Intake is counted in kilojoules, not grams. A heavy meal "
                    "can carry little energy."},
            {"text": "The share of their food that the gut manages to absorb "
                     "rather than pass through.", "correct": False,
             "why": "Intake is what is eaten. How much is absorbed is a "
                    "separate question the sum does not ask."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e09",
        "band": "easier",
        "text": "In this lesson's bookkeeping, what is a shortfall?",
        "options": [
            {"text": "Taking in less energy than you transfer, so stores are "
                     "broken down.", "correct": True},
            {"text": "Taking in less food by mass than the day before, "
                     "whatever the energy in it was.", "correct": False,
             "why": "Mass is not what is compared. The sum is energy in "
                    "against energy transferred."},
            {"text": "Eating a meal that is missing one of the seven "
                     "nutrients a diet has to contain.", "correct": False,
             "why": "That is a deficiency. A shortfall is about energy and "
                    "nothing else."},
            {"text": "Taking in more energy than you transfer, so the extra "
                     "goes into the body's stores.", "correct": False,
             "why": "That is a surplus — the same sum with the sign the other "
                    "way round."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e10",
        "band": "easier",
        "text": "A person takes in less energy than they transfer, every day "
                "for a month. What happens to their body mass?",
        "options": [
            {"text": "It rises, because the body holds on to what little food "
                     "it is given.", "correct": False,
             "why": "Stores are being broken down to make up the difference, "
                    "so mass goes the other way."},
            {"text": "It falls, because stores are broken down to make up the "
                     "difference.", "correct": True},
            {"text": "It stays the same, because the body lowers what it "
                     "transfers to match whatever arrives.", "correct": False,
             "why": "A body cannot simply match its transfer to its intake, "
                    "which is why a month of shortfall shows."},
            {"text": "It rises and then falls, because stores are laid down "
                     "first and used afterwards.", "correct": False,
             "why": "Nothing is being laid down. There is no surplus at any "
                    "point in the month."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e11",
        "band": "easier",
        "text": "Two adults are the same age, size and sex, and neither is "
                "growing. What could still make their energy requirements "
                "differ?",
        "options": [
            {"text": "One of them prefers food with more kilojoules in it "
                     "than the other one does.", "correct": False,
             "why": "What they choose to eat is intake. The requirement is "
                    "set before any food is chosen."},
            {"text": "One of them has eaten a larger breakfast than the other "
                     "on the day in question.", "correct": False,
             "why": "Breakfast changes intake for the day. It does not change "
                    "how much the body transfers."},
            {"text": "One of them moves far more than the other.",
             "correct": True},
            {"text": "One of them was measured in kilojoules and the other in "
                     "kilocalories, which are different sizes.",
             "correct": False,
             "why": "Changing the unit changes the number, not the "
                    "requirement. The two convert exactly."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e12",
        "band": "easier",
        "text": "A day's food comes to 9000 kJ, and the person eating it has "
                "a requirement of 9000 kJ. What is that day?",
        "options": [
            {"text": "A surplus, because a full day's food has been eaten in "
                     "one day.", "correct": False,
             "why": "A surplus means intake above requirement. Here the two "
                    "are the same."},
            {"text": "A shortfall, because some of the energy is lost as heat "
                     "before it can be used.", "correct": False,
             "why": "The energy transferred to the surroundings is already "
                    "part of the 9000 kJ requirement."},
            {"text": "Impossible to say without knowing which foods made up "
                     "the day.", "correct": False,
             "why": "The energy sum only needs the totals. Which foods "
                    "supplied them is a separate question."},
            {"text": "Balanced — intake matches requirement.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e13",
        "band": "easier",
        "text": "Toast and butter is listed at 780 kJ a slice. How much "
                "energy is in three slices?",
        "options": [
            {"text": "2340 kJ", "correct": True},
            {"text": "1560 kJ", "correct": False,
             "why": "That is two slices. Read the number of portions before "
                    "multiplying."},
            {"text": "780 kJ", "correct": False,
             "why": "That is one slice, which is the figure the list gives "
                    "before any multiplying."},
            {"text": "260 kJ", "correct": False,
             "why": "That divides by three instead of multiplying. Three "
                    "slices carry more energy than one, not less."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e14",
        "band": "easier",
        "text": "A glass of orange juice is 380 kJ and an apple is 320 kJ. "
                "What do the two together come to?",
        "options": [
            {"text": "60 kJ", "correct": False,
             "why": "That is the difference between them. The question asks "
                    "for the total."},
            {"text": "700 kJ", "correct": True},
            {"text": "620 kJ", "correct": False,
             "why": "That is two apples. One of each is wanted here."},
            {"text": "760 kJ", "correct": False,
             "why": "That is two glasses of juice rather than one of each."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e15",
        "band": "easier",
        "text": "Scientists say the energy in food is transferred rather than "
                "used up. What does that wording mean?",
        "options": [
            {"text": "The energy is still there afterwards, just somewhere "
                     "else.", "correct": True},
            {"text": "The energy is destroyed slowly rather than all at once "
                     "as soon as the food is eaten.", "correct": False,
             "why": "Nothing about eating destroys energy at any rate at all, "
                    "fast or slow."},
            {"text": "Only some of the energy is real, and the rest is a way "
                     "of keeping the bookkeeping tidy.", "correct": False,
             "why": "All of it is real, and all of it can be found afterwards "
                    "in some store or other."},
            {"text": "The energy moves from one food to another inside the "
                     "gut before it is absorbed.", "correct": False,
             "why": "The transfer is out of the food's chemical store into "
                    "movement, tissue and the surroundings."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e16",
        "band": "easier",
        "text": "Of the energy in a day's food, where does most of it end up?",
        "options": [
            {"text": "In new tissue, since the body is rebuilt continuously "
                     "throughout life.", "correct": False,
             "why": "New tissue takes a share, and in an adult it is a small "
                    "one."},
            {"text": "In the thermal store of the surroundings.",
             "correct": True},
            {"text": "In movement, since walking about is what most of a day "
                     "is spent doing.", "correct": False,
             "why": "Movement takes a share. Rather more of the total ends up "
                    "warming the room."},
            {"text": "Nowhere — it is used up, which is why more food is "
                     "needed the next day.", "correct": False,
             "why": "Energy is never used up. It ends up somewhere, and here "
                    "that is mostly the surroundings."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e17",
        "band": "easier",
        "text": "A person is described as a 70-watt heater. What is that "
                "describing?",
        "options": [
            {"text": "The temperature a body settles at, which is about "
                     "37 °C in a healthy person.", "correct": False,
             "why": "A watt is not a temperature. Body temperature is a "
                    "separate quantity in degrees."},
            {"text": "The energy in a day's food, converted into a smaller "
                     "unit for comparison.", "correct": False,
             "why": "A day's food is counted in kilojoules. Watts describe a "
                    "rate rather than a total."},
            {"text": "The rate at which a person warms their surroundings.",
             "correct": True},
            {"text": "The share of a person's food that ends up as movement "
                     "rather than as warmth.", "correct": False,
             "why": "It is not a share of anything. It describes how fast "
                    "energy leaves the body as warmth."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e18",
        "band": "easier",
        "text": "A packet prints a figure as a percentage of 'your daily "
                "needs'. Whose requirement is that a percentage of?",
        "options": [
            {"text": "The requirement of whoever happens to be holding the "
                     "packet at the time.", "correct": False,
             "why": "The packet cannot know that, which is exactly why the "
                    "figure is a fixed one."},
            {"text": "A standard reference figure, which belongs to nobody in "
                     "particular.", "correct": True},
            {"text": "The requirement of the average child of secondary "
                     "school age in this country.", "correct": False,
             "why": "The reference is an adult figure, and it is not chosen "
                    "to fit a child at all."},
            {"text": "The largest requirement anyone is likely to have, so "
                     "that nobody is under-fed by it.", "correct": False,
             "why": "It sits nowhere near the largest — an athlete's day is "
                    "far above any reference figure."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e19",
        "band": "easier",
        "text": "Intake minus requirement comes out positive for someone's "
                "day. What does that tell you?",
        "options": [
            {"text": "They are short, and stores will be broken down to make "
                     "up the difference.", "correct": False,
             "why": "A positive answer means intake was the larger of the "
                    "two, so nothing is being drawn on."},
            {"text": "They are in surplus, and the extra is stored.",
             "correct": True},
            {"text": "Their day was balanced, since a positive answer means "
                     "the two sides agree.", "correct": False,
             "why": "A balanced day gives zero. Positive means intake ran "
                    "above the requirement."},
            {"text": "They have eaten a larger mass of food than they did the "
                     "day before.", "correct": False,
             "why": "The sum compares energy against a requirement, and says "
                    "nothing about yesterday."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e20",
        "band": "easier",
        "text": "What does a bomb calorimeter measure?",
        "options": [
            {"text": "The total chemical energy released when a sample is "
                     "burned.", "correct": True},
            {"text": "The mass of a food sample before and after it has been "
                     "digested by an animal.", "correct": False,
             "why": "No digestion happens in a calorimeter. The sample is "
                    "burned in oxygen instead."},
            {"text": "The energy a person's body would actually get from "
                     "eating that sample.", "correct": False,
             "why": "It measures more than the body gets, because it burns "
                    "material a gut cannot digest."},
            {"text": "The temperature a food has to reach before it will "
                     "catch fire on its own.", "correct": False,
             "why": "The sample is ignited electrically. What is measured is "
                    "the energy released, not an ignition point."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e21",
        "band": "easier",
        "text": "In a bomb calorimeter, which measurement gives the energy "
                "released by the sample?",
        "options": [
            {"text": "The mass of ash left in the vessel once the sample has "
                     "finished burning.", "correct": False,
             "why": "The ash is what is left over. It says nothing about the "
                    "energy that came out."},
            {"text": "The pressure of the oxygen packed into the vessel "
                     "before the sample is lit.", "correct": False,
             "why": "The oxygen is there so the sample burns completely; its "
                    "pressure is not the measurement."},
            {"text": "The time the sample takes to burn from one end to the "
                     "other.", "correct": False,
             "why": "How long it burns for is not measured. The energy is "
                    "read from the water instead."},
            {"text": "The temperature rise of a known mass of water.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e22",
        "band": "easier",
        "text": "Two chapatis with dal are listed at 1750 kJ. What do two "
                "such servings come to?",
        "options": [
            {"text": "3500 kJ", "correct": True},
            {"text": "1750 kJ", "correct": False,
             "why": "That is one serving, which is the figure before the "
                    "portions are counted."},
            {"text": "875 kJ", "correct": False,
             "why": "That halves the figure instead of doubling it. Two "
                    "servings carry more, not less."},
            {"text": "5250 kJ", "correct": False,
             "why": "That is three servings. The question asks about two of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e23",
        "band": "easier",
        "text": "Two pots of yoghurt at 520 kJ each are eaten with an apple "
                "at 320 kJ. What is the total?",
        "options": [
            {"text": "840 kJ", "correct": False,
             "why": "That is one pot and the apple. There are two pots to "
                    "count."},
            {"text": "1360 kJ", "correct": True},
            {"text": "1040 kJ", "correct": False,
             "why": "That is the two pots with the apple left out of the "
                    "total."},
            {"text": "1880 kJ", "correct": False,
             "why": "That counts three pots. Only two were eaten."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e24",
        "band": "easier",
        "text": "A chocolate bar is listed at 1050 kJ. What is that in "
                "joules?",
        "options": [
            {"text": "1050 J", "correct": False,
             "why": "That treats a kilojoule and a joule as the same size, "
                    "and one kilojoule is a thousand joules."},
            {"text": "10 500 J", "correct": False,
             "why": "That multiplies by ten. The step from kJ to J is a "
                    "factor of a thousand."},
            {"text": "1 050 000 J", "correct": True},
            {"text": "1.05 J", "correct": False,
             "why": "That divides by a thousand instead of multiplying, so "
                    "the answer comes out far too small."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e25",
        "band": "easier",
        "text": "Someone with a requirement of 9000 kJ eats a day totalling "
                "10 500 kJ. What is that day?",
        "options": [
            {"text": "A shortfall of 1500 kJ", "correct": False,
             "why": "Intake is the larger of the two here, so nothing is "
                    "being drawn on."},
            {"text": "A surplus of 19 500 kJ", "correct": False,
             "why": "That adds the two figures. The sum wanted is the "
                    "difference between them."},
            {"text": "A surplus of 1500 kJ", "correct": True},
            {"text": "Balanced, since 10 500 kJ is close to 9000 kJ",
             "correct": False,
             "why": "A gap of 1500 kJ is a sixth of the requirement, which is "
                    "not a match."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e26",
        "band": "easier",
        "text": "For someone whose day needs to add up to 9500 kJ, an "
                "actual day comes to only 7000 kJ. Is that a surplus or a "
                "shortfall, and by how much?",
        "options": [
            {"text": "A shortfall of 2500 kJ", "correct": True},
            {"text": "A surplus of 2500 kJ", "correct": False,
             "why": "Intake is the smaller of the two, so the day runs short "
                    "rather than over."},
            {"text": "A shortfall of 16 500 kJ", "correct": False,
             "why": "That adds the two figures together instead of taking one "
                    "from the other."},
            {"text": "A shortfall of 3500 kJ", "correct": False,
             "why": "Check the subtraction: 9500 take away 7000 leaves 2500, "
                    "not 3500."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e27",
        "band": "easier",
        "text": "Besides moving about and staying alive, what else does a "
                "growing child's body spend energy on?",
        "options": [
            {"text": "Building new tissue", "correct": True},
            {"text": "Storing the vitamins in their food", "correct": False,
             "why": "Vitamins are needed in milligrams and storing them is "
                    "not a noticeable part of a day's energy."},
            {"text": "Cooling the body down to room temperature",
             "correct": False,
             "why": "A body is warmer than the room and loses warmth without "
                    "having to spend energy doing it."},
            {"text": "Breaking down the fibre that passes through the gut",
             "correct": False,
             "why": "Fibre is not digested at all, so no energy goes into "
                    "breaking it down."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e28",
        "band": "easier",
        "text": "For an adult with a desk job, roughly what share of the "
                "day's energy goes on simply staying alive and at 37 °C?",
        "options": [
            {"text": "About a tenth", "correct": False,
             "why": "Staying alive is the largest claim on the day, not a "
                    "small corner of it."},
            {"text": "About a quarter", "correct": False,
             "why": "That is roughly what is left over for everything else, "
                    "not what staying alive takes."},
            {"text": "About three quarters", "correct": True},
            {"text": "Almost none, since a body at rest transfers very little "
                     "energy at all", "correct": False,
             "why": "A resting body is still warming the room continuously, "
                    "which is most of the day's total."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e29",
        "band": "easier",
        "text": "Why is there no single correct amount of food for everybody?",
        "options": [
            {"text": "Because food packets are printed in different units in "
                     "different countries.", "correct": False,
             "why": "Units convert exactly. The spread in requirements is "
                    "there whichever unit is used."},
            {"text": "Because a requirement belongs to a person, and people "
                     "differ in size, age, growth and activity.",
             "correct": True},
            {"text": "Because different foods carry different amounts of "
                     "energy per gram.", "correct": False,
             "why": "That is true and is about the food. The spread in "
                    "requirements is about the people."},
            {"text": "Because nobody has ever measured how much energy a "
                     "person transfers in a day.", "correct": False,
             "why": "These figures come from measurement. They differ because "
                    "the people do."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-e30",
        "band": "easier",
        "text": "A handful of nuts is 1250 kJ and a banana is 450 kJ. How "
                "much more energy is in the nuts?",
        "options": [
            {"text": "1700 kJ", "correct": False,
             "why": "That adds the two together. A difference calls for a "
                    "subtraction."},
            {"text": "800 kJ", "correct": True},
            {"text": "450 kJ", "correct": False,
             "why": "That is the banana on its own rather than the gap "
                    "between the two."},
            {"text": "1250 kJ", "correct": False,
             "why": "That is the nuts on their own, with the banana not taken "
                    "off."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 expansion ────────────────────────────
    {
        "id": "b3-03-s08",
        "band": "standard",
        "text": "An office worker (requirement 9000 kJ) eats two slices of "
                "toast and butter, a glass of orange juice, a plate of jollof "
                "rice and chicken, and a pot of yoghurt. What is the day, and "
                "how does it compare with the requirement?",
        "options": [
            {"text": "4560 kJ, a shortfall of 4440 kJ against the "
                     "requirement.", "correct": True},
            {"text": "4560 kJ, a surplus of 4440 kJ over the requirement.",
             "correct": False,
             "why": "Intake is the smaller figure here, so the day runs "
                    "short of the requirement rather than over it."},
            {"text": "3780 kJ, a shortfall of 5220 kJ against the "
                     "requirement.", "correct": False,
             "why": "That treats one slice of toast as two. Two slices are "
                    "listed, so double 780 before adding the rest."},
            {"text": "Balanced, because the day was built around this "
                     "person's requirement.", "correct": False,
             "why": "Being built for this person doesn't make a day balance "
                    "on its own; the four items still have to be added and "
                    "compared, and this one comes short."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s09",
        "band": "standard",
        "text": "A bricklayer (requirement 13 500 kJ) eats three slices of "
                "toast and butter, a banana, two pots of yoghurt and a glass "
                "of orange juice. What is the day, and how does it compare?",
        "options": [
            {"text": "3690 kJ, a shortfall of 9810 kJ against the "
                     "requirement.", "correct": False,
             "why": "Two pots of yoghurt are listed; only one was counted "
                    "here."},
            {"text": "4210 kJ, a shortfall of 9290 kJ against the "
                     "requirement.", "correct": True},
            {"text": "4210 kJ, a surplus of 9290 kJ over the requirement.",
             "correct": False,
             "why": "Intake here is far below the requirement, so the day "
                    "runs short rather than over."},
            {"text": "3430 kJ, a shortfall of 10 070 kJ against the "
                     "requirement.", "correct": False,
             "why": "That counts two slices of toast rather than three; "
                    "recheck the portions before adding."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s10",
        "band": "standard",
        "text": "An Olympic rower (requirement 25 000 kJ) eats three plates of "
                "pasta and sauce, three plates of jollof rice and chicken, "
                "two servings of chapatis with dal and two handfuls of nuts. "
                "What is the day, and how does it compare?",
        "options": [
            {"text": "17 100 kJ, a shortfall of 7900 kJ against the "
                     "requirement.", "correct": False,
             "why": "Three plates of pasta are listed; this counts only "
                    "two."},
            {"text": "19 500 kJ, a surplus of 5500 kJ over the requirement.",
             "correct": False,
             "why": "Intake here is below the requirement, so it is a "
                    "shortfall, not a surplus."},
            {"text": "19 500 kJ, a shortfall of 5500 kJ against the "
                     "requirement.", "correct": True},
            {"text": "44 500 kJ, comfortably over the requirement once both "
                     "figures are added together.", "correct": False,
             "why": "That adds the intake and the requirement together "
                    "rather than comparing them; the comparison needed is a "
                    "subtraction."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s11",
        "band": "standard",
        "text": "A 13-year-old (requirement 9500 kJ) eats a plate of pasta "
                "and sauce, a plate of jollof rice and chicken, two servings "
                "of chapatis with dal, a handful of nuts, two chocolate bars "
                "and a bowl of cereal. What is the day, and how does it "
                "compare?",
        "options": [
            {"text": "12 450 kJ, a shortfall of 2950 kJ against the "
                     "requirement.", "correct": False,
             "why": "Intake is above the requirement here, so the extra is a "
                    "surplus, not a shortfall."},
            {"text": "11 350 kJ, a surplus of 1850 kJ.", "correct": False,
             "why": "That leaves the bowl of cereal out of the total; six "
                    "items are listed, not five."},
            {"text": "10 700 kJ, a surplus of 1200 kJ.", "correct": False,
             "why": "That counts only one serving of chapatis with dal where "
                    "two are listed."},
            {"text": "12 450 kJ, a surplus of 2950 kJ over the requirement.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s12",
        "band": "standard",
        "text": "A 4-year-old needs 5800 kJ a day and a 13-year-old needs "
                "9500 kJ a day. Both bodies are growing. Why is the "
                "difference so large?",
        "options": [
            {"text": "Adolescent growth is the most energy-expensive stage "
                     "of life, in a body that is already bigger than the "
                     "4-year-old's.", "correct": True},
            {"text": "Growth stops almost completely before the age of ten, "
                     "so the 4-year-old's total reflects size alone.",
             "correct": False,
             "why": "Growth is happening at both ages; the 4-year-old's "
                    "total already includes a real cost for building new "
                    "tissue, and it is still the smallest of the two because "
                    "there is so much less body to fuel and to grow."},
            {"text": "The two figures are about the same once age is taken "
                     "into account, and the gap must be a rounding "
                     "difference.", "correct": False,
             "why": "3700 kJ is a substantial, real gap — well over half the "
                    "smaller figure — not a rounding error."},
            {"text": "A teenager moves around more than a young child does, "
                     "and physical activity alone explains the whole "
                     "difference.", "correct": False,
             "why": "Activity is part of it, but adolescent growth itself is "
                    "the biggest single driver of this gap, not movement "
                    "alone."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s13",
        "band": "standard",
        "text": "The bricklayer and the rower both do hard physical work, yet "
                "the rower's requirement is nearly double the bricklayer's. "
                "Explain the gap.",
        "options": [
            {"text": "Rowing burns more energy per movement than lifting "
                     "bricks does, whatever the duration.", "correct": False,
             "why": "The lesson gives no such per-movement comparison; what "
                    "is given is the rower's roughly six hours of hard "
                    "training, which is the real driver here."},
            {"text": "The rower trains for about six hours a day on top of "
                     "an already large, muscular body.", "correct": True},
            {"text": "The bricklayer's figure must be measured wrong, since "
                     "manual labour is the harder of the two jobs.",
             "correct": False,
             "why": "Nothing says manual labour is harder; the figures are "
                    "for two different amounts and intensities of activity, "
                    "and both are given as measured."},
            {"text": "Muscle size is what sets a requirement, and the two "
                     "bodies here are roughly the same size and build.",
             "correct": False,
             "why": "Body size is one term, but the lesson attributes the "
                    "rower's total mainly to the sheer training time, not to "
                    "a size difference between the two."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s14",
        "band": "standard",
        "text": "A person runs a small shortfall for one day only, then "
                "returns to a balanced day for the rest of the month. What "
                "does that single day do to their mass over the month?",
        "options": [
            {"text": "It draws a little from stores on that one day, and "
                     "nothing more — a small, one-off effect.",
             "correct": True},
            {"text": "Nothing at all — a single day is much too short a "
                     "time for the body to ever draw on its stores.",
             "correct": False,
             "why": "Even one day can draw on stores; if intake was "
                    "genuinely below what was transferred that day, "
                    "something had to make up the difference."},
            {"text": "The same as a whole month of shortfall, because a "
                     "shortfall triggers the same drop whatever its length.",
             "correct": False,
             "why": "The size of the effect depends on how much and for how "
                    "long; one day is nowhere near a month's worth."},
            {"text": "It cannot really be answered without knowing exactly "
                     "how many grams the person weighs to begin with.",
             "correct": False,
             "why": "The direction of the effect — a small draw on stores — "
                    "follows from the sizes given, without needing a "
                    "starting mass."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s15",
        "band": "standard",
        "text": "A shopping list is put together to feed the bricklayer for a "
                "day and it balances exactly. The bricklayer is unavailable, "
                "so an office worker eats it instead, portion for portion. "
                "What does that plate become for the office worker?",
        "options": [
            {"text": "Still balanced, since exactly the same portions were "
                     "eaten by someone, just a different person.",
             "correct": False,
             "why": "Balance is measured against the eater's own "
                    "requirement; the office worker needs 9000 kJ, and this "
                    "plate carries 13 500 kJ."},
            {"text": "A shortfall of 4500 kJ, because the office worker does "
                     "less physical work.", "correct": False,
             "why": "Doing less work lowers what a body needs, so the same "
                    "food goes further, not less far — that makes a "
                    "surplus, not a shortfall."},
            {"text": "The food itself now carries less energy, since it "
                     "goes further for a smaller body.", "correct": False,
             "why": "A food's energy value doesn't depend on who eats it; "
                    "only the requirement being compared against has "
                    "changed."},
            {"text": "A surplus of 4500 kJ — the same food against a "
                     "smaller requirement.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s16",
        "band": "standard",
        "text": "A pot of yoghurt is 520 kJ. A 4-year-old's requirement is "
                "5800 kJ. Roughly, is that pot closer to a tenth of the day "
                "or a quarter of the day?",
        "options": [
            {"text": "Closer to a tenth — 520 is a little under 580, which "
                     "is a tenth of 5800.", "correct": True},
            {"text": "Closer to a quarter — 520 kJ feels like a fairly big "
                     "share of any child's day.", "correct": False,
             "why": "A quarter of 5800 is 1450 kJ, well above 520; 520 sits "
                    "much nearer a tenth of the day."},
            {"text": "Exactly a quarter, because a pot of yoghurt is a "
                     "fairly substantial food.", "correct": False,
             "why": "A food's richness doesn't fix its share of a day; work "
                    "it out from the two numbers — a quarter would be "
                    "1450 kJ, not 520."},
            {"text": "Neither — 520 kJ is too small a number to compare "
                     "with a whole day.", "correct": False,
             "why": "Comparing a small figure with a larger one is exactly "
                    "how a share is worked out; 520 against 5800 gives a "
                    "clear answer."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s17",
        "band": "standard",
        "text": "One day is built from six small items: a banana, an apple, "
                "a pot of yoghurt, a glass of juice, a slice of toast and a "
                "glass of water (450 + 320 + 520 + 380 + 780 + 0 = "
                "2450 kJ). Another day is built from two large items: a "
                "plate of pasta and a plate of jollof rice and chicken "
                "(2400 + 2100 = 4500 kJ). Which day is closer to a "
                "4-year-old's requirement of 5800 kJ?",
        "options": [
            {"text": "The six-item day, because six items feels closer to a "
                     "full day than two.", "correct": False,
             "why": "The size of a day is set by its total kJ, not by how "
                    "many separate things were eaten — 2450 kJ is further "
                    "from 5800 kJ than 4500 kJ is."},
            {"text": "The two-item day, at 4500 kJ — it is closer to "
                     "5800 kJ even though it has far fewer items.",
             "correct": True},
            {"text": "Both are the same distance from the requirement, "
                     "since they were built from the same twelve foods.",
             "correct": False,
             "why": "5800 minus 2450 is 3350, while 5800 minus 4500 is "
                    "1300; the two days are not the same distance at all."},
            {"text": "Neither is close enough to say — both are surpluses "
                     "over an already large requirement.", "correct": False,
             "why": "Both totals are below 5800 kJ, not above it, so "
                    "neither is a surplus; the question only asks which is "
                    "closer."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s18",
        "band": "standard",
        "text": "About three quarters of an office worker's 9000 kJ day "
                "goes on simply staying alive at rest. Roughly how many kJ "
                "is that?",
        "options": [
            {"text": "About 2250 kJ.", "correct": False,
             "why": "That is the remaining quarter — everything apart from "
                    "simply staying alive — not the three-quarter share "
                    "itself."},
            {"text": "About 9000 kJ.", "correct": False,
             "why": "That is the whole day's requirement. Three quarters of "
                    "it is smaller than the full total."},
            {"text": "About 6750 kJ.", "correct": True},
            {"text": "About 4500 kJ.", "correct": False,
             "why": "That is half of 9000 kJ, not three quarters. Three "
                    "quarters is bigger than a half."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s19",
        "band": "standard",
        "text": "About three quarters of an office worker's 9000 kJ day "
                "goes on simply staying alive, and the rest is activity. A "
                "bricklayer with the same body needs 13 500 kJ a day, but "
                "pays the same 'staying alive' cost as the office worker. "
                "Roughly what share of the bricklayer's day is activity?",
        "options": [
            {"text": "About a quarter — most of the bricklayer's day is "
                     "still the same baseline as the office worker's.",
             "correct": False,
             "why": "13 500 minus the 6750 kJ baseline leaves 6750 kJ for "
                    "activity, which is half the total, not a quarter."},
            {"text": "None of it — heavy manual work still counts as part "
                     "of simply staying alive.", "correct": False,
             "why": "The staying-alive baseline is fixed by body size and "
                    "stays at 6750 kJ; everything the bricklayer needs above "
                    "that is activity."},
            {"text": "Almost all of it — a body doing manual labour spends "
                     "very little on simply staying alive.", "correct": False,
             "why": "The baseline does not shrink with activity; it stays "
                    "at 6750 kJ for this body, exactly as it was for the "
                    "office worker."},
            {"text": "About half — the activity share comes to 6750 kJ, the "
                     "same size as the baseline itself.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s20",
        "band": "standard",
        "text": "A magazine matches a reader to the '9000 kJ office "
                "worker' row of a table like the one on the bench, and "
                "tells them to eat exactly that much every day for good "
                "health. What is the flaw in treating a bench figure as "
                "personal advice?",
        "options": [
            {"text": "A bench figure is a rounded example for teaching the "
                     "idea, not a measurement of this particular reader's "
                     "own requirement.", "correct": True},
            {"text": "There is no flaw — matching yourself to the closest "
                     "job title on a table is exactly how a requirement "
                     "should be found.", "correct": False,
             "why": "A real requirement is set by an individual's own "
                    "size, age, growth and activity, not by which row of a "
                    "table happens to share a job title."},
            {"text": "The flaw is that 9000 kJ is too low a figure for "
                     "anybody to use as daily advice.", "correct": False,
             "why": "9000 kJ is a perfectly reasonable requirement for many "
                    "people; the problem is treating one example figure as "
                    "though it applied to a specific reader."},
            {"text": "There is no flaw, provided the reader also has a "
                     "desk job like the person in the example.",
             "correct": False,
             "why": "Even a shared job title does not guarantee a shared "
                    "body size, age or activity level; a bench figure was "
                    "never a personal measurement to begin with."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s21",
        "band": "standard",
        "text": "An injured rower stops training for a week but keeps "
                "eating a full 25 000 kJ day, same as always. What happens "
                "to their energy balance that week?",
        "options": [
            {"text": "Nothing changes — 25 000 kJ was already their usual "
                     "day before the injury, so it should stay balanced.",
             "correct": False,
             "why": "The day of food is unchanged, but the injury has "
                    "lowered what they need; the same intake now sits "
                    "against a lower requirement."},
            {"text": "They move into a large surplus, because the training "
                     "that used to justify all that food has stopped.",
             "correct": True},
            {"text": "They run a shortfall instead, since resting the body "
                     "slows down how well it is able to use food.",
             "correct": False,
             "why": "Resting lowers the amount of energy needed, not the "
                    "body's ability to use what it eats; less need "
                    "alongside the same intake gives a surplus, not a "
                    "shortfall."},
            {"text": "Their requirement stays fixed at 25 000 kJ, since "
                     "that figure was set once and for all by their body "
                     "size.", "correct": False,
             "why": "25 000 kJ was set by training as well as by size; take "
                    "the training away and the requirement drops, even "
                    "though the body itself is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s22",
        "band": "standard",
        "text": "A retired grandparent who does gentle gardening and a "
                "delivery cyclist doing 150 km a day eat identical meals for "
                "a month, both around 12 000 kJ. After a month, one has "
                "gained mass and one has lost it. Which is which, and why?",
        "options": [
            {"text": "The cyclist gains mass, because all that cycling "
                     "somehow makes his body better at storing energy.",
             "correct": False,
             "why": "Harder activity raises the amount of energy "
                    "transferred, which uses up more of the day's food "
                    "rather than storing more of it."},
            {"text": "Neither of them gains or loses mass, since they ate "
                     "exactly the same meals as each other every day.",
             "correct": False,
             "why": "Eating the same intake does not guarantee the same "
                    "outcome; what matters is how that intake compares with "
                    "each person's own requirement."},
            {"text": "The grandparent gains mass, the cyclist loses it — "
                     "their bodies transfer very different daily amounts.",
             "correct": True},
            {"text": "The grandparent loses mass instead, because older "
                     "bodies generally burn through food faster.",
             "correct": False,
             "why": "An older, less active body generally transfers less "
                    "energy in a day, not more, which is why the surplus "
                    "goes to the more sedentary person here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s23",
        "band": "standard",
        "text": "A label's reference figure works out to about 8400 kJ. An "
                "office worker's own requirement is 9000 kJ. How does the "
                "office worker compare with the reference figure?",
        "options": [
            {"text": "A very large gap — the office worker needs far more "
                     "than the reference figure allows.", "correct": False,
             "why": "9000 minus 8400 is only 600 kJ, a small fraction of "
                    "either total, not a large gap."},
            {"text": "Exactly the same — office work is the activity level "
                     "the reference figure describes.", "correct": False,
             "why": "8400 kJ and 9000 kJ are not the same number; there is "
                    "a real, if modest, gap between them."},
            {"text": "Below it — the reference figure is higher than an "
                     "office worker actually needs.", "correct": False,
             "why": "9000 kJ is above 8400 kJ, not below it, so the office "
                    "worker's requirement is the larger of the two."},
            {"text": "Fairly close — about 600 kJ above it, a small gap "
                     "next to a 9000 kJ day.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s24",
        "band": "standard",
        "text": "A 4-year-old's day totals 4550 kJ against their 5800 kJ "
                "requirement — a shortfall of 1250 kJ. Which single "
                "addition exactly closes it: a banana (450 kJ), a handful "
                "of nuts (1250 kJ), or a chocolate bar (1050 kJ)?",
        "options": [
            {"text": "The handful of nuts — 1250 kJ exactly matches the "
                     "shortfall.", "correct": True},
            {"text": "The banana — since any addition moves the day closer "
                     "to balance.", "correct": False,
             "why": "Moving closer is not the same as closing the gap "
                    "exactly; 450 kJ still leaves 800 kJ short."},
            {"text": "The chocolate bar — its energy is closest to a "
                     "normal snack size.", "correct": False,
             "why": "Snack size isn't what is being asked; 1050 kJ still "
                    "leaves 200 kJ short of the exact shortfall."},
            {"text": "None of them — closing a shortfall exactly needs "
                     "several items added together, not one.",
             "correct": False,
             "why": "The nuts alone are 1250 kJ, precisely the size of "
                    "this shortfall, so one item is enough here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s25",
        "band": "standard",
        "text": "During eight hours of sleep, roughly what happens to the "
                "energy in the evening meal that has not yet gone to "
                "movement?",
        "options": [
            {"text": "It is transferred to new tissue and to the thermal "
                     "store of the surroundings, even at rest.",
             "correct": True},
            {"text": "Nothing is transferred overnight, since a sleeping "
                     "body is neither moving nor eating anything.",
             "correct": False,
             "why": "A resting body still keeps warm and still repairs "
                    "tissue, both of which transfer energy; movement "
                    "stopping does not stop transfer."},
            {"text": "It is used up by the brain overnight and is gone "
                     "completely by morning.", "correct": False,
             "why": "Nothing about being used up destroys energy; "
                    "overnight, most of it still ends up warming the "
                    "surroundings."},
            {"text": "It stays completely in the body's fat stores until "
                     "the next proper meal arrives.", "correct": False,
             "why": "Only a surplus is stored; a resting body is still "
                    "transferring energy to warmth and repair through the "
                    "night, not banking all of it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s26",
        "band": "standard",
        "text": "A canteen offers two lunch options with the same total "
                "energy: a plate of pasta and sauce (2400 kJ), or a bowl of "
                "cereal, a pot of yoghurt and a slice of toast and butter "
                "together (1100 + 520 + 780 = 2400 kJ). Does the choice "
                "between them change how the lunch compares with a diner's "
                "requirement?",
        "options": [
            {"text": "Yes — three separate items add up faster in the body "
                     "than one large plate.", "correct": False,
             "why": "The body compares total energy against requirement, "
                    "and three items totalling 2400 kJ add exactly the same "
                    "amount as one plate at 2400 kJ."},
            {"text": "Yes — the three-item option is more filling, so it "
                     "counts for more of the day.", "correct": False,
             "why": "Feeling full is not what the comparison runs on; both "
                    "options are worth the same 2400 kJ regardless of how "
                    "filling either feels."},
            {"text": "No — both options add 2400 kJ to the day, whichever "
                     "foods make up that total.", "correct": True},
            {"text": "It depends which person eats it, since the two "
                     "options suit different bodies.", "correct": False,
             "why": "The two options are equal in energy before anyone is "
                    "even named; which suits a given body is the same "
                    "question either way, because the totals match."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s27",
        "band": "standard",
        "text": "A rower runs a 2000 kJ surplus on Monday and a 2000 kJ "
                "shortfall on Tuesday, same body both days. What is the "
                "two-day net effect on their stores?",
        "options": [
            {"text": "A 4000 kJ surplus, since two large energy events add "
                     "together regardless of sign.", "correct": False,
             "why": "A surplus and a shortfall move stores in opposite "
                    "directions; they do not add together as if both went "
                    "the same way."},
            {"text": "A 4000 kJ shortfall, because the second day "
                     "outweighs the first.", "correct": False,
             "why": "Nothing here gives the second day more weight; the two "
                    "figures are equal and opposite, so together they "
                    "cancel."},
            {"text": "It cannot be worked out without knowing exactly what "
                     "was eaten each day.", "correct": False,
             "why": "The two figures given are already the surplus and the "
                    "shortfall; nothing further is needed to see that they "
                    "are equal and opposite."},
            {"text": "None overall — the surplus on Monday and the "
                     "shortfall on Tuesday cancel out.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s28",
        "band": "standard",
        "text": "Two people with different requirements each buy from the "
                "same vending machine, choosing whatever they like. Does "
                "the machine decide either person's requirement?",
        "options": [
            {"text": "No — a machine only supplies intake; the requirement "
                     "is already fixed by size, age, growth and activity.",
             "correct": True},
            {"text": "Yes — whichever machine a person happens to use ends "
                     "up setting how much energy they need that particular "
                     "day.", "correct": False,
             "why": "A machine can only supply food; it has no way of "
                    "setting what a body needs, which is fixed by the "
                    "person rather than by where the food came from."},
            {"text": "Only for the person who happens to buy more items "
                     "than the other one does.", "correct": False,
             "why": "Buying more changes intake, not requirement; the "
                    "person's own size, age, growth and activity are what "
                    "set the requirement, however much or little they buy."},
            {"text": "It depends on the prices charged, since a cheaper "
                     "item is much easier to buy in bulk.", "correct": False,
             "why": "Price has nothing to do with either intake or "
                    "requirement — only the energy value of what is bought "
                    "and eaten matters."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s29",
        "band": "standard",
        "text": "Two office workers both need 9000 kJ. One eats a 9500 kJ "
                "day, the other eats an 8200 kJ day. Are their days the "
                "same kind?",
        "options": [
            {"text": "Yes — since they share the same requirement, they "
                     "must share the same kind of day.", "correct": False,
             "why": "Sharing a requirement does not fix the outcome; what "
                    "decides surplus or shortfall is each person's own "
                    "intake against that shared requirement."},
            {"text": "No — one runs a small surplus, the other a "
                     "shortfall, despite an identical requirement.",
             "correct": True},
            {"text": "Yes — both intakes are close enough to 9000 kJ that "
                     "they ought to count as balanced.", "correct": False,
             "why": "9500 kJ is above the requirement and 8200 kJ is below "
                    "it; being close is not the same as being on the same "
                    "side of it."},
            {"text": "It cannot really be decided without first knowing "
                     "exactly what foods each of them ate.", "correct": False,
             "why": "The two intakes are already given; comparing each to "
                    "the shared 9000 kJ requirement is enough to answer."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-s30",
        "band": "standard",
        "text": "A 4-year-old already fed 3600 kJ at home tops up with a "
                "2200 kJ school lunch, reaching 5800 kJ — their full "
                "requirement. A 13-year-old, also already fed 3600 kJ at "
                "home, gets the same 2200 kJ lunch and reaches 5800 kJ too "
                "— but their requirement is 9500 kJ. What does the "
                "comparison show?",
        "options": [
            {"text": "The same lunch works equally well for both, since "
                     "they ate identical amounts all day.", "correct": False,
             "why": "Eating identical totals does not mean identical "
                    "outcomes; the two have very different requirements, "
                    "and only one of the two totals matches its own."},
            {"text": "The 13-year-old is fine, since 5800 kJ is still a "
                     "substantial day's food.", "correct": False,
             "why": "Substantial is not the same as sufficient; 5800 kJ is "
                    "3700 kJ below what a 13-year-old actually needs."},
            {"text": "The lunch balances the 4-year-old's day but leaves "
                     "the 13-year-old 3700 kJ short.", "correct": True},
            {"text": "The 4-year-old is short, since children need "
                     "proportionally more relative to their size.",
             "correct": False,
             "why": "The 4-year-old's day comes to exactly 5800 kJ, which "
                    "is exactly their own requirement — not a shortfall at "
                    "all."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 expansion ──────────────────────────────
    {
        "id": "b3-03-h08",
        "band": "harder",
        "text": "A protein bar company prints 'one bar = 5% of your daily "
                "needs' based on the standard 8400 kJ reference figure, "
                "which puts the bar itself at 420 kJ. What percentage of an "
                "Olympic rower's actual 25 000 kJ day does that same bar "
                "really represent, to the nearest whole per cent?",
        "options": [
            {"text": "About 2%.", "correct": True},
            {"text": "About 5%.", "correct": False,
             "why": "5% was calculated against the 8400 kJ reference, not "
                    "against the rower's 25 000 kJ; against his own "
                    "requirement the same bar comes to under 2%."},
            {"text": "About 98%.", "correct": False,
             "why": "That is the share of the day left after the bar, not "
                    "the share the bar itself represents; the working "
                    "wanted is the bar divided by the requirement."},
            {"text": "About 12%.", "correct": False,
             "why": "The rower's requirement is far larger than the "
                    "reference figure, not smaller, so a fixed bar counts "
                    "for far less of his day, not more."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h09",
        "band": "harder",
        "text": "A parent feeds both a 4-year-old and a 13-year-old from one "
                "shopping list. The list totals 14 000 kJ, split evenly "
                "between the two children. Is that enough for each of "
                "them?",
        "options": [
            {"text": "Yes for both — 7000 kJ each is a fairly generous "
                     "amount of food by any measure.",
             "correct": False,
             "why": "7000 kJ is indeed above the 4-year-old's requirement, "
                    "but it falls 2500 kJ below the 13-year-old's — an even "
                    "split does not mean an equal fit."},
            {"text": "It gives the 4-year-old a surplus of 1200 kJ but "
                     "leaves the 13-year-old 2500 kJ short.", "correct": True},
            {"text": "No for both — 14 000 kJ is nowhere near enough to "
                     "feed two growing children.", "correct": False,
             "why": "Split evenly it comfortably covers the smaller "
                    "requirement; the shortfall belongs to the 13-year-old "
                    "alone."},
            {"text": "It is impossible to say without knowing exactly what "
                     "foods made up the 14 000 kJ.", "correct": False,
             "why": "The two requirements and the split are already given; "
                    "comparing 7000 kJ against each is enough, whatever "
                    "foods supplied it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h10",
        "band": "harder",
        "text": "A 4-year-old's requirement is 5800 kJ. If it were exactly a "
                "quarter of the office worker's requirement instead of what "
                "it actually is, what would the office worker need?",
        "options": [
            {"text": "1450 kJ — a quarter of 5800, since the relationship "
                     "works the other way round.", "correct": False,
             "why": "The question sets the child's figure as the quarter, "
                    "so the office worker's figure — the whole — is four "
                    "times bigger than 5800, not a quarter of it."},
            {"text": "9000 kJ — that already is the relationship between "
                     "the two real figures.", "correct": False,
             "why": "5800 is not actually a quarter of 9000; 9000 divided "
                    "by 4 is 2250, not 5800, so this hypothetical is not "
                    "the real relationship at all."},
            {"text": "23 200 kJ — four times 5800, really far more than "
                     "the office worker's real 9000 kJ.", "correct": True},
            {"text": "14 500 kJ — five times 5800 minus the child's own "
                     "requirement.", "correct": False,
             "why": "The relationship asked for is simple multiplication by "
                    "four; there is no reason to subtract the child's "
                    "figure back out."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h11",
        "band": "harder",
        "text": "Which pair of the five eaters on the bench has the "
                "smallest gap between their daily requirements?",
        "options": [
            {"text": "The 4-year-old and the office worker, since both of "
                     "them are far from the rower's total.",
             "correct": False,
             "why": "Being far from a third figure says nothing about the "
                    "gap between these two; 4-year-old to office worker is "
                    "3200 kJ, much larger than 500 kJ."},
            {"text": "The bricklayer and the rower, since both do hard "
                     "physical work.", "correct": False,
             "why": "Doing similar kinds of work does not make two "
                    "requirements close; these two are 11 500 kJ apart, the "
                    "largest gap of any pair here."},
            {"text": "The 4-year-old and the 13-year-old, since both are "
                     "still growing.", "correct": False,
             "why": "Sharing a stage of growth doesn't set the size of the "
                    "gap; these two are 3700 kJ apart, well above the true "
                    "smallest gap."},
            {"text": "The office worker and the 13-year-old — only 500 kJ "
                     "apart, the smallest gap of any pair here.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h12",
        "band": "harder",
        "text": "A company wants one reference figure that fits all five "
                "eaters on the bench reasonably well. Explain why that "
                "reference cannot exist, using the actual range.",
        "options": [
            {"text": "Because the five requirements span 5800 kJ to "
                     "25 000 kJ — over a fourfold range — so no single "
                     "figure fits.", "correct": True},
            {"text": "It could exist, as long as the figure chosen sits "
                     "exactly halfway between the smallest and the largest "
                     "of the five.", "correct": False,
             "why": "The midpoint of 5800 and 25 000 is over 15 000 kJ — a "
                    "huge surplus for the 4-year-old and still short for "
                    "the rower; the spread is too wide for any single "
                    "number to fit."},
            {"text": "It cannot exist, because the five people's figures "
                     "were never actually measured accurately enough.",
             "correct": False,
             "why": "The figures are given as measured; the problem is not "
                    "their accuracy but the sheer size of the spread "
                    "between the smallest and the largest."},
            {"text": "It already exists — the reference figure printed on "
                     "a label is exactly built for this very purpose.",
             "correct": False,
             "why": "The reference figure is a rounded average for one "
                    "kind of adult; it was never built to fit a 4-year-old "
                    "or an athlete in training at the same time."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h13",
        "band": "harder",
        "text": "A nutritionist claims that because the bricklayer and "
                "office worker are the same age, size and sex, one single "
                "'adult' figure should describe them both. Using their "
                "actual requirements, evaluate that claim.",
        "options": [
            {"text": "The claim holds, because age, size and sex are the "
                     "only things a requirement depends on.", "correct": False,
             "why": "Activity is also part of what sets a requirement, and "
                    "it is the one thing that differs between this exact "
                    "pair."},
            {"text": "The claim fails — despite matching on all three, "
                     "their requirements still differ by 4500 kJ.",
             "correct": True},
            {"text": "The claim holds for this particular pair, but only "
                     "because both of them happen to be male.",
             "correct": False,
             "why": "Sex being the same is not what makes requirements "
                    "match; these two are the same sex and still differ by "
                    "4500 kJ."},
            {"text": "The claim fails, but only because one of the two "
                     "figures must have been measured wrongly.",
             "correct": False,
             "why": "Nothing points to an error; both figures are genuine, "
                    "and the gap between them is explained by activity, not "
                    "by a mistake."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h14",
        "band": "harder",
        "text": "A 4-year-old's day is scaled down from a rower's day in "
                "the same proportion as their requirements compare (that "
                "is, at 5800 : 25 000). If the rower's day includes a "
                "2400 kJ plate of pasta, what would the equivalent plate be "
                "for the 4-year-old, to the nearest 10 kJ?",
        "options": [
            {"text": "About 2400 kJ.", "correct": False,
             "why": "The question asks for a plate scaled to a much "
                    "smaller requirement, not one the same size at all."},
            {"text": "About 10 340 kJ.", "correct": False,
             "why": "That comes from multiplying by 25 000 over 5800 "
                    "rather than 5800 over 25 000; the child's share should "
                    "come out smaller, not larger."},
            {"text": "About 560 kJ.", "correct": True},
            {"text": "About 5800 kJ.", "correct": False,
             "why": "5800 kJ is the child's full daily requirement, not one "
                    "scaled portion within it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h15",
        "band": "harder",
        "text": "A slimming magazine claims 'eat less than 9000 kJ a day "
                "and you will lose mass, whoever you are.' Using the bench "
                "figures, what is wrong with 'whoever you are'?",
        "options": [
            {"text": "Nothing — 9000 kJ is below every single one of the "
                     "five requirements, so the claim holds for all of "
                     "them.", "correct": False,
             "why": "9000 kJ is well above the 4-year-old's 5800 kJ "
                    "requirement, so for that person it is a surplus, not a "
                    "shortfall."},
            {"text": "The claim only fails for the rower, since 9000 kJ "
                     "really is a shortfall for everyone else on the "
                     "bench.", "correct": False,
             "why": "It also fails for the 4-year-old — 9000 kJ is above "
                    "their requirement, so it would cause a surplus for "
                    "them too."},
            {"text": "The claim is right regardless, since losing mass is "
                     "generally thought of as a healthy outcome.",
             "correct": False,
             "why": "Whether 9000 kJ causes a loss depends entirely on the "
                    "person's own requirement; for the smallest person here "
                    "it does the opposite."},
            {"text": "9000 kJ is a shortfall for four of the five people "
                     "here, but a large surplus for the 4-year-old.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h16",
        "band": "harder",
        "text": "A hypothetical day for the bricklayer is built entirely "
                "from bananas at 450 kJ each. How many would be needed to "
                "reach his 13 500 kJ requirement exactly?",
        "options": [
            {"text": "30.", "correct": True},
            {"text": "13.5.",
             "correct": False,
             "why": "That divides by the wrong number entirely; the "
                    "working needed is the requirement divided by the size "
                    "of one banana, 450 kJ."},
            {"text": "6.", "correct": False,
             "why": "6 bananas would total only 2700 kJ, a long way short "
                    "of 13 500 kJ; nothing limits how many are used in this "
                    "calculation."},
            {"text": "300.",
             "correct": False,
             "why": "Dropping a zero from 450 gives ten times too many "
                    "bananas; divide by the true 450 kJ value."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h17",
        "band": "harder",
        "text": "A rower's day is built from six plates of pasta and sauce "
                "(6 × 2400 kJ) plus six plates of jollof rice and chicken "
                "(6 × 2100 kJ). Does that day meet, fall short of, or "
                "exceed the 25 000 kJ requirement, and by how much?",
        "options": [
            {"text": "It falls short, by 2000 kJ.", "correct": False,
             "why": "27 000 kJ is above 25 000 kJ, not below it, so this is "
                    "a surplus rather than a shortfall."},
            {"text": "It exceeds the requirement, by 2000 kJ.",
             "correct": True},
            {"text": "It exactly meets the requirement, since twelve large "
                     "portions is clearly a full day's food.", "correct": False,
             "why": "The two totals add to 27 000 kJ, not 25 000 kJ; a "
                    "full-looking day does not automatically match a "
                    "number exactly."},
            {"text": "It exceeds the requirement, by 4600 kJ.",
             "correct": False,
             "why": "That comes from adding one plate too many into the "
                    "pasta total; six plates of pasta come to 14 400 kJ, "
                    "not a higher figure."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h18",
        "band": "harder",
        "text": "The office worker's requirement is 9000 kJ, of which about "
                "three quarters goes on simply staying alive. A new job "
                "halves that person's activity but leaves the "
                "staying-alive baseline unchanged. Estimate the new "
                "requirement.",
        "options": [
            {"text": "About 4500 kJ.", "correct": False,
             "why": "Halving activity only affects the activity share, not "
                    "the whole requirement; the staying-alive baseline of "
                    "6750 kJ does not change at all."},
            {"text": "About 6750 kJ.", "correct": False,
             "why": "Activity was halved, not removed altogether; a "
                    "smaller activity share still has to be added back "
                    "onto the baseline."},
            {"text": "About 7875 kJ.", "correct": True},
            {"text": "About 9000 kJ.", "correct": False,
             "why": "The body being the same fixes the baseline, but the "
                    "requirement is baseline plus activity, and the "
                    "activity half has fallen."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h19",
        "band": "harder",
        "text": "A packaging company wants to justify printing 2000 kcal as "
                "'a fair reference for everyone.' Using the bench, name the "
                "two eaters for whom that figure is the least fair, and say "
                "why.",
        "options": [
            {"text": "The bricklayer and the office worker — their two "
                     "figures happen to be the closest to a round number.",
             "correct": False,
             "why": "Being close to a round number is not what fairness "
                    "means here; their figures, 13 500 and 9000, are not "
                    "unusually far from the reference either way, unlike "
                    "the rower's and the child's."},
            {"text": "The 13-year-old and the office worker — both of them "
                     "are teenagers or young working adults.",
             "correct": False,
             "why": "The office worker is a full adult, not a teenager, "
                    "and neither of these two is where the reference figure "
                    "is furthest out; 9000 and 9500 sit closest to the "
                    "reference of all five."},
            {"text": "None of them — the reference figure was supposedly "
                     "designed to fit everybody equally well regardless.",
             "correct": False,
             "why": "A single figure cannot fit a fourfold spread of "
                    "requirements equally; it was built as an average for "
                    "one kind of adult, not a fit for all five."},
            {"text": "The rower and the 4-year-old — the reference is "
                     "roughly a third of the rower's real figure.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h20",
        "band": "harder",
        "text": "Two days are built for the same 13-year-old (requirement "
                "9500 kJ). Day A is three servings of chapatis with dal "
                "plus two chocolate bars. Day B is two plates of pasta and "
                "sauce, a plate of jollof rice and chicken, and a banana. "
                "Which day comes closer to the requirement?",
        "options": [
            {"text": "Neither — the two days come to exactly the same "
                     "total, 7350 kJ, both 2150 kJ short.", "correct": True},
            {"text": "Day A, because three large servings usually add up "
                     "to more than a mixed plate.", "correct": False,
             "why": "Adding both days up gives exactly the same total, "
                    "7350 kJ; the number of items eaten does not decide "
                    "which total is bigger."},
            {"text": "Day B, because it includes a wider variety of "
                     "different kinds of food altogether.", "correct": False,
             "why": "Variety of food items has no bearing on the kJ total; "
                    "both days come to precisely 7350 kJ."},
            {"text": "It cannot really be compared, since the two days "
                     "share none of the same foods in common.",
             "correct": False,
             "why": "Sharing no foods does not stop each day being added "
                    "up and compared; both totals turn out to be the same "
                    "number, 7350 kJ."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h21",
        "band": "harder",
        "text": "A dietitian says: 'if two people's daily shortfalls are "
                "the same size in kJ, the effect on their bodies must be "
                "the same.' Using the bench, explain why that reasoning is "
                "weak — compare a 500 kJ shortfall for the 4-year-old with "
                "a 500 kJ shortfall for the rower.",
        "options": [
            {"text": "The reasoning is sound, because a kilojoule is the "
                     "same size of unit whoever is short of it.",
             "correct": False,
             "why": "The unit being fixed is exactly why the comparison "
                    "misleads — the same fixed unit is a far larger share "
                    "of a small requirement than of a large one."},
            {"text": "The same 500 kJ is a far bigger fraction of the "
                     "4-year-old's day than of the rower's day.",
             "correct": True},
            {"text": "The 4-year-old's shortfall matters less, because "
                     "children's bodies recover from a shortfall faster.",
             "correct": False,
             "why": "Nothing here supports children recovering faster; the "
                    "point is about the size of the shortfall relative to "
                    "each person's own day, not about recovery speed."},
            {"text": "The rower's shortfall matters more, because athletes "
                     "cannot afford to miss any energy.", "correct": False,
             "why": "Importance is not what is being compared here; in "
                    "proportion to each person's own requirement, the "
                    "child's 500 kJ gap is the larger of the two, not the "
                    "rower's."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h22",
        "band": "harder",
        "text": "A label states a food is '15% of a 9000 kJ reference "
                "figure.' Work out the food's energy in kJ, then say what "
                "percentage that same food represents of a 4-year-old's "
                "actual 5800 kJ requirement, to the nearest whole per "
                "cent.",
        "options": [
            {"text": "1350 kJ, and about 15% of the 4-year-old's day too, "
                     "since the percentage does not change.", "correct": False,
             "why": "15% was worked out against the 9000 kJ reference; "
                    "against the smaller 5800 kJ requirement the same "
                    "1350 kJ is a bigger share, about 23%."},
            {"text": "900 kJ, and about 16% of the 4-year-old's day.",
             "correct": False,
             "why": "That comes from 10% of 9000 rather than 15%; multiply "
                    "9000 by 0.15, not 0.10."},
            {"text": "1350 kJ, and about 23% of the 4-year-old's day.",
             "correct": True},
            {"text": "1350 kJ, and about 33% of the 4-year-old's day.",
             "correct": False,
             "why": "That treats the child's requirement as about "
                    "4000 kJ; their real requirement is 5800 kJ, which "
                    "gives a smaller share, about 23%."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h23",
        "band": "harder",
        "text": "A school trip pack gives every pupil the same 3000 kJ "
                "lunch regardless of age. Using the five bench figures, "
                "which pupil-type does it fit best, and which worst?",
        "options": [
            {"text": "It fits the office worker best, since 3000 kJ is "
                     "closest to an average adult figure.", "correct": False,
             "why": "3000 kJ is 6000 kJ below the office worker's "
                    "requirement; the 4-year-old's gap of 2800 kJ is "
                    "smaller than that."},
            {"text": "It fits everybody equally badly, since not one of "
                     "the five requirements is met.", "correct": False,
             "why": "Every one of the five does run a shortfall, but the "
                    "size of that shortfall is very different — from "
                    "2800 kJ for the smallest person to 22 000 kJ for the "
                    "largest."},
            {"text": "It fits the rower best, since a big appetite makes "
                     "any lunch feel small by comparison.", "correct": False,
             "why": "Feeling small is not the measure used; in kJ terms "
                    "the rower's gap of 22 000 kJ is the largest of all "
                    "five, not the smallest."},
            {"text": "It fits the 4-year-old best (still 2800 kJ short) "
                     "and the rower worst (22 000 kJ short).",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h24",
        "band": "harder",
        "text": "If the bricklayer eats five full plates of jollof rice and "
                "chicken (2100 kJ each) plus one more, smaller portion to "
                "reach exactly 13 500 kJ, how big does that last portion "
                "need to be?",
        "options": [
            {"text": "3000 kJ.", "correct": True},
            {"text": "2100 kJ.",
             "correct": False,
             "why": "Five portions of 2100 kJ already total 10 500 kJ; a "
                    "sixth identical portion would overshoot 13 500 kJ, not "
                    "land on it."},
            {"text": "300 kJ.",
             "correct": False,
             "why": "13 500 minus 10 500 is 3000 kJ, not a tenth of that; "
                    "check the subtraction rather than the multiplication."},
            {"text": "13 500 kJ.", "correct": False,
             "why": "That ignores the 10 500 kJ already accounted for by "
                    "the five plates; only the remaining gap is wanted."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h25",
        "band": "harder",
        "text": "Between the 4-year-old and the 13-year-old, the "
                "requirement rises by 3700 kJ. Between the 13-year-old and "
                "the office worker, it falls by 500 kJ, even though the "
                "office worker is an adult and stops growing. Explain why "
                "growth does not simply keep adding as a person ages.",
        "options": [
            {"text": "It is a mistake in the figures — a fully grown adult "
                     "cannot possibly need less than a teenager.",
             "correct": False,
             "why": "The figures are as given; adolescent growth is a "
                    "real, large cost that a fully grown adult with a desk "
                    "job no longer pays."},
            {"text": "Growth is a cost only while the body is still being "
                     "built, and it disappears once growth stops.",
             "correct": True},
            {"text": "The office worker must be smaller than the "
                     "13-year-old, which is why the figure drops.",
             "correct": False,
             "why": "Adults are the larger of the two; the drop is "
                    "explained by growth stopping, not by the adult being "
                    "physically smaller."},
            {"text": "Growth adds a fixed 3700 kJ at every age, so the "
                     "pattern should carry on upward with age.",
             "correct": False,
             "why": "Growth is not a fixed add-on that carries on "
                    "indefinitely; it is large during adolescence and "
                    "drops away once a body stops growing, which is "
                    "exactly why the total falls here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h26",
        "band": "harder",
        "text": "The rower's requirement is described as a large muscular "
                "body plus six hours of hard training. If the training "
                "alone accounts for about 15 000 kJ of the 25 000 kJ "
                "total, roughly what share of the day is the training, to "
                "the nearest 5%?",
        "options": [
            {"text": "About 15%.", "correct": False,
             "why": "That treats the 15 000 kJ figure itself as the "
                    "percentage rather than dividing it by the 25 000 kJ "
                    "total first."},
            {"text": "About 40%.", "correct": False,
             "why": "That is the share left over once the training is "
                    "taken out, not the training's own share."},
            {"text": "About 60%.", "correct": True},
            {"text": "About 167%.", "correct": False,
             "why": "That divides the total by the training figure instead "
                    "of the training figure by the total."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h27",
        "band": "harder",
        "text": "A packet claims '25% less energy than a standard product' "
                "and is aimed at people wanting to lose mass. A rower buys "
                "it instead of his usual food, portion for portion. "
                "Evaluate whether that claim is good advice for him "
                "specifically.",
        "options": [
            {"text": "It is good advice for him, because reducing energy "
                     "anywhere in a diet is a sensible goal.", "correct": False,
             "why": "Whether reducing energy helps depends on the person's "
                    "own requirement; for someone needing 25 000 kJ a day, "
                    "cutting food further can create a serious shortfall "
                    "rather than a healthy change."},
            {"text": "It makes no difference to him, since 25% of any food "
                     "is too small an amount to matter.", "correct": False,
             "why": "25% off a rower's already large food intake could be "
                    "a substantial number of kilojoules, not a small one, "
                    "given the size of his day."},
            {"text": "It is bad advice for absolutely everyone who buys "
                     "the product, no matter what their own requirement "
                     "happens to be.", "correct": False,
             "why": "The same 25% reduction could suit someone whose "
                    "intake was previously a surplus; the question is "
                    "specifically about whether it suits the rower, not "
                    "everybody."},
            {"text": "Not necessarily good advice — a 25% cut could create "
                     "a real shortfall for someone needing this much.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h28",
        "band": "harder",
        "text": "A 4-year-old's day is rebuilt using only pots of yoghurt "
                "(520 kJ) and glasses of juice (380 kJ). Using four "
                "yoghurts and the rest in juice, how many glasses of juice "
                "are needed to reach 5800 kJ, and is that a whole number?",
        "options": [
            {"text": "Just under 10 glasses (9.8), so whole glasses of "
                     "juice cannot land on 5800 kJ exactly.",
             "correct": True},
            {"text": "Exactly 10 whole glasses, which is meant to land "
                     "precisely on the 5800 kJ target.", "correct": False,
             "why": "Ten glasses of juice is 3800 kJ, which added to the "
                    "2080 kJ from yoghurt gives 5880 kJ, not exactly "
                    "5800 kJ."},
            {"text": "Exactly 9 whole glasses, which is meant to land "
                     "precisely on the 5800 kJ target too.", "correct": False,
             "why": "Nine glasses of juice is 3420 kJ, which added to "
                    "2080 kJ gives 5500 kJ, short of 5800 kJ, not exact."},
            {"text": "It cannot be worked out, because juice and yoghurt "
                     "were never compared with each other before.",
             "correct": False,
             "why": "Both are foods on the bench with a stated kJ figure "
                    "each; nothing stops adding them up the same way as any "
                    "other combination."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h29",
        "band": "harder",
        "text": "Consider two claims: (1) 'A rower's diet is unhealthy "
                "because it is so much bigger than everyone else's.' (2) "
                "'A rower's diet is exactly as healthy as anyone else's, "
                "provided it matches his own requirement.' Using the "
                "lesson's own idea of a requirement, which claim does the "
                "evidence support?",
        "options": [
            {"text": "The first — any diet over about 15 000 kJ counts as "
                     "excessive, whoever eats it.", "correct": False,
             "why": "There is no fixed excessive threshold in this lesson; "
                    "a requirement belongs to the person, and the rower's "
                    "genuinely is 25 000 kJ."},
            {"text": "The second — size alone says nothing about health; "
                     "what matters is matching intake to the person's "
                     "requirement.", "correct": True},
            {"text": "Both, in different ways — a very large diet is "
                     "somewhat unhealthy even when it matches a genuine "
                     "requirement.", "correct": False,
             "why": "The lesson's whole argument is that matching a "
                    "genuine requirement is what balance means, regardless "
                    "of how large that requirement happens to be."},
            {"text": "Neither — health cannot really be judged just from "
                     "the size of a diet.", "correct": False,
             "why": "That overstates the point; the lesson does connect "
                    "balance to health by comparing intake with "
                    "requirement — it only refuses to judge health from "
                    "size on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b3-03-h30",
        "band": "harder",
        "text": "A school buys a bulk supply of identical ready meals, each "
                "2200 kJ, intending to give two meals a day to every pupil "
                "regardless of age. For which of the five bench eaters "
                "would two meals (4400 kJ) come closest to balancing the "
                "day, and by how much would it miss for the rower?",
        "options": [
            {"text": "Closest for the office worker, 4600 kJ short; for "
                     "the rower it misses by 20 600 kJ.", "correct": False,
             "why": "4600 kJ is not the smallest gap here — the "
                    "4-year-old's gap of 1400 kJ is smaller still."},
            {"text": "Closest for the 4-year-old, 1400 kJ short; for the "
                     "rower it misses by 25 000 kJ.", "correct": False,
             "why": "25 000 kJ would mean the two meals supplied nothing at "
                    "all; 4400 kJ has to be subtracted from the rower's "
                    "requirement first, leaving 20 600 kJ."},
            {"text": "Closest for the 4-year-old, 1400 kJ short; for the "
                     "rower it misses by 20 600 kJ.", "correct": True},
            {"text": "Closest for the 13-year-old, 5100 kJ short; for the "
                     "rower it misses by 20 600 kJ.", "correct": False,
             "why": "5100 kJ is larger than the 4-year-old's 1400 kJ gap, "
                    "so the 13-year-old's day is not actually the closest "
                    "of the five."},
        ],
        "figure": None,
    },
]
