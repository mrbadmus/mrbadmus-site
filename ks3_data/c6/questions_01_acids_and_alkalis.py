"""C6 lesson 01 — Acids and alkalis: twelve questions (MRB-269).

The lesson's argument is one shape: acid and alkali are POSITIONS on a scale,
they are read by what a substance does rather than by how it looks, and neither
position is a statement about danger. These twelve probe the angles the mastery
ladder leaves alone.

The distractors are built from the lesson's two declared misconceptions.

`ACID-01` (acids are the dangerous ones; alkalis make things safe) drives the
wrong options in e02, s04, h01 and h03. h01 is the one that matters: it asks
which single observation REFUTES the belief, and three of its four options are
things that are perfectly true and settle nothing — which is the shape of the
mistake, rather than the belief stated flat.

`ACID-02` (a dilute acid is no longer really an acid) drives s01 and h04, where
adding water, or being used up, is treated as ceasing to be an acid. s01 is the
register's own case put as a question about a bottle.

A third strand, everywhere on the page and in neither register entry, is that
NEUTRAL IS A BAND rather than a point. e01 and h02 are built on it: e01 offers
"anything between 6 and 8" as the shape of the wrong idea, and h02 takes clean
rainwater at pH 6 — a number a student expects to be 7 — and asks for the
reason rather than the label.

A fourth strand is that a test is a way of LOOKING. e03 and s02 both offer
weighing, smelling and waiting as alternatives to an indicator, because that is
what a student reaches for when a property has no appearance.

Every question here is new prose, and the bar is §13's: each distractor is a
WRONG RULE in the correct answer's own shape and at its own length, and each is
a mistake a real student actually makes. No correct answer is strictly the
longest in its set by four words or by 1.4x, and the twelve are authored level
across the four answer positions — three apiece — from the start (MRB-278).
"""

UNIT = "C6"
LESSON = "acids-and-alkalis"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-01-e01",
        "band": "easier",
        "text": "What is the pH of a neutral substance?",
        "options": [
            {"text": "Exactly 7, which is what pure water reads",
             "correct": True},
            {"text": "Anything between 6 and 8, near the middle",
             "correct": False,
             "why": "Neutral is a single point, not a band. pH 6 is acidic "
                    "and pH 8 is alkaline, however close to the middle they "
                    "look."},
            {"text": "Below 7, which is where lemon juice sits",
             "correct": False,
             "why": "That is the acid half of the scale. Neutral is the "
                    "middle of it, not the acid end."},
            {"text": "Above 7, which is where oven cleaner sits",
             "correct": False,
             "why": "That is the alkali half. Neutral sits between the two "
                    "halves, at 7 exactly."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e02",
        "band": "easier",
        "text": "Four bottles are on the bench. Which is the most dangerous "
                "to get on your skin?",
        "options": [
            {"text": "Lemon juice, because it is an acid", "correct": False,
             "why": "Citric acid at about pH 2, and people drink it. Being an "
                    "acid says which side of 7 it sits on, not how hard it "
                    "hits."},
            {"text": "Oven cleaner, because it is a strong alkali",
             "correct": True},
            {"text": "Salt solution, because it was made from acid",
             "correct": False,
             "why": "It reads pH 7. What it was made from does not survive "
                    "the reaction — a salt is a new substance."},
            {"text": "Pure water, because it has no pH at all",
             "correct": False,
             "why": "Pure water has a pH and it is 7, the definition of "
                    "neutral. Nothing is without one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e03",
        "band": "easier",
        "text": "A drop of vinegar turns litmus red. What does that tell you?",
        "options": [
            {"text": "It is neutral, because red is the middle colour",
             "correct": False,
             "why": "Litmus has two colours and no middle one. It reports a "
                    "side of the scale rather than a position on it."},
            {"text": "It is an alkali, because alkalis turn litmus red",
             "correct": False,
             "why": "The other way round. Alkalis turn litmus blue; red is "
                    "the acid answer."},
            {"text": "It is an acid, because acids turn litmus red",
             "correct": True},
            {"text": "Nothing, because litmus goes red in every liquid",
             "correct": False,
             "why": "Litmus stays its own colour in a neutral solution and "
                    "goes blue in an alkali. It is a test, not a detector."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-e04",
        "band": "easier",
        "text": "Garden lime is spread on soil that has turned too acidic for "
                "a crop. Why does that help?",
        "options": [
            {"text": "It washes the acid down out of the topsoil",
             "correct": False,
             "why": "Nothing is washed anywhere. The lime reacts with the "
                    "acid and both are used up where they meet."},
            {"text": "It adds more acid, so the two cancel each other",
             "correct": False,
             "why": "Two acids do not cancel. It takes something from the "
                    "other side of 7 to cancel an acid."},
            {"text": "It dries the soil out so the acid cannot work",
             "correct": False,
             "why": "Acid in dry soil is still acid. The lime changes the "
                    "chemistry rather than the water."},
            {"text": "It is an alkali, so it cancels the acid out",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-01-s01",
        "band": "standard",
        "text": "A bottle of concentrated acid is diluted with a very large "
                "amount of water. What is in the bottle now?",
        "options": [
            {"text": "Water, because the acid stopped being acid when it was "
                     "diluted", "correct": False,
             "why": "Diluting makes an acid weaker in effect and leaves it "
                    "unchanged in kind. Every drop of acid in there is still "
                    "acid."},
            {"text": "Acid, weaker in effect, with a pH still below 7",
             "correct": True},
            {"text": "An alkali, because so much neutral water pushed it past "
                     "7", "correct": False,
             "why": "Water is neutral and cannot push anything past 7. It can "
                    "only bring a reading closer to it."},
            {"text": "Acid, with a pH now further below 7 than it was",
             "correct": False,
             "why": "Diluting moves the pH towards 7, not away from it. There "
                    "is less acid in each cm³ afterwards, not more."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s02",
        "band": "standard",
        "text": "Two unlabelled colourless liquids are on the bench: one acid, "
                "one alkali. Which test would tell them apart?",
        "options": [
            {"text": "Weigh equal volumes of each and compare the readings",
             "correct": False,
             "why": "Both are mostly water and both weigh about the same. "
                    "Mass says nothing about which side of 7 a liquid is on."},
            {"text": "Smell each one carefully from a safe distance",
             "correct": False,
             "why": "Neither has to smell of anything, and sodium hydroxide "
                    "does not. Smell is not a test for pH."},
            {"text": "Add a few drops of an indicator to a sample of each",
             "correct": True},
            {"text": "Leave both out and see which one evaporates first",
             "correct": False,
             "why": "Both are water solutions and both evaporate. Waiting "
                    "tells you nothing about which is which."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s03",
        "band": "standard",
        "text": "Copper oxide neutralises acid perfectly well but barely "
                "dissolves in water. What is it?",
        "options": [
            {"text": "An alkali, because neutralising an acid is what alkalis "
                     "do", "correct": False,
             "why": "Every alkali neutralises acid, but not everything that "
                    "neutralises acid is an alkali. An alkali has to dissolve."},
            {"text": "An acid, because it reacts strongly with another acid",
             "correct": False,
             "why": "A substance that reacts WITH acid is the opposite of an "
                    "acid. Two acids do nothing at all to each other."},
            {"text": "Neutral, because it is neither an acid nor an alkali",
             "correct": False,
             "why": "Neutral means it does nothing to an acid. This one does "
                    "— it cancels it out completely."},
            {"text": "A base but not an alkali, because it does not dissolve",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-s04",
        "band": "standard",
        "text": "An indigestion tablet dissolved in water reads pH 9. Why is "
                "something like that sold as a medicine?",
        "options": [
            {"text": "It is a mild alkali, so it cancels out excess stomach "
                     "acid", "correct": True},
            {"text": "It is a strong alkali, so it destroys the acid on "
                     "contact", "correct": False,
             "why": "A strong alkali swallowed would do more damage than the "
                    "acid it was sent to deal with. pH 9 is mild on purpose."},
            {"text": "It is an acid, so it makes the stomach less acidic "
                     "overall", "correct": False,
             "why": "Adding acid to acid does not help. Cancelling an acid "
                    "takes something on the other side of 7."},
            {"text": "It is neutral, so it dilutes the stomach acid "
                     "harmlessly", "correct": False,
             "why": "Diluting would take a great deal of water. pH 9 means it "
                    "reacts with the acid rather than watering it down."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-01-h01",
        "band": "harder",
        "text": "A student says anything corrosive must be an acid. Which "
                "single observation shows that is wrong?",
        "options": [
            {"text": "Battery acid burns cloth and skin the moment it touches "
                     "them", "correct": False,
             "why": "That is an acid being corrosive, which is what the "
                    "student already believes. It supports the claim instead "
                    "of testing it."},
            {"text": "Lemon juice is an acid and is safe enough to drink",
             "correct": False,
             "why": "That shows some acids are harmless, which is a different "
                    "claim. The student said corrosive things are acids."},
            {"text": "Oven cleaner burns skin badly and reads pH 13",
             "correct": True},
            {"text": "Pure water reads pH 7 and is harmless to touch",
             "correct": False,
             "why": "A harmless neutral liquid tests nothing here. The claim "
                    "is about corrosive things, and water is not one."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h02",
        "band": "harder",
        "text": "Rainwater collected cleanly, far from any road, reads pH 6 "
                "rather than 7. What is the best explanation?",
        "options": [
            {"text": "The sample was contaminated by the bottle it was "
                     "collected in", "correct": False,
             "why": "Clean glass changes nothing. A reading of 6 in clean "
                    "rain is normal rather than an error to explain away."},
            {"text": "Rain always picks up acid from the exhausts of passing "
                     "cars", "correct": False,
             "why": "This sample was taken well away from a road, and rain in "
                    "genuinely clean air still reads about 6."},
            {"text": "Pure water is really pH 6 and the figure of 7 is a "
                     "rounding", "correct": False,
             "why": "Pure water is 7 by definition. What has changed here is "
                    "that this water is not pure."},
            {"text": "Carbon dioxide from the air dissolves in it and makes "
                     "it slightly acidic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h03",
        "band": "harder",
        "text": "Sodium hydroxide splashes onto a hand and the person feels "
                "almost nothing. Why is that more dangerous, not less?",
        "options": [
            {"text": "There is no pain to warn them, so it is left on the "
                     "skin for longer", "correct": True},
            {"text": "It only turns corrosive after a few minutes on warm "
                     "skin", "correct": False,
             "why": "It starts attacking straight away. What is delayed is "
                    "the pain, not the damage."},
            {"text": "Feeling nothing means the alkali is too weak to do any "
                     "harm", "correct": False,
             "why": "Strength and sting are two different things. Sodium "
                    "hydroxide is one of the strongest alkalis in any school "
                    "lab."},
            {"text": "It has to be washed off with a weak acid rather than "
                     "water", "correct": False,
             "why": "Water, under a running tap, for a long time. Adding acid "
                    "to a burn releases heat and makes it worse."},
        ],
        "figure": None,
    },
    {
        "id": "c6-01-h04",
        "band": "harder",
        "text": "Sodium chloride solution is made by reacting a strong acid "
                "with a strong alkali. Why does it read pH 7?",
        "options": [
            {"text": "The salt holds a little acid and a little alkali, which "
                     "cancel", "correct": False,
             "why": "Neither survives the reaction. What is left is one new "
                    "compound dissolved in water, and it is not acidic at "
                    "all."},
            {"text": "Both were used up making new substances, and neither "
                     "product is acidic", "correct": True},
            {"text": "The salt formed is neutral and it dilutes both of the "
                     "originals", "correct": False,
             "why": "The salt dilutes nothing — it is what the acid and the "
                    "alkali became."},
            {"text": "The acid and the alkali destroyed each other and left "
                     "only water", "correct": False,
             "why": "The salt is dissolved in that water. Boil the water off "
                    "and the crystals are sitting in the dish."},
        ],
        "figure": None,
    },
]
