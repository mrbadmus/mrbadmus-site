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
]
