"""P1 lesson 07 — Keeping energy in: insulation: twelve questions.

These probe the two things a student has to hold at once: that an insulator
is a source of nothing, and that a fair test is what settles which one is
best. The distractors are built from ENER-15 — insulation makes heat — and
from the two habits the bench is aimed at: reading a comparison across two
changed variables as if it were across one, and expecting a good insulator to
stop a transfer rather than slow it.

⚠️ Answer positions are 3 zeros, 2 ones, 3 twos and 4 threes here and in
lesson 8, which brings the unit's ninety-six to exactly twenty-four of each
(MRB-278). No figures.
"""

UNIT = "P1"
LESSON = "insulation"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-07-e01",
        "band": "easier",
        "text": "What does an insulator do?",
        "options": [
            {"text": "Slows a thermal transfer down by being bad at carrying "
                     "it",
             "correct": True},
            {"text": "Adds warmth to whatever it is wrapped around",
             "correct": False,
             "why": "It has no energy of its own to add. Wrap it round "
                    "something cold and the cold thing stays cold."},
            {"text": "Stops a thermal transfer completely",
             "correct": False,
             "why": "Every beaker on the bench cooled, including the best "
                    "one. Slowing and stopping are different claims."},
            {"text": "Keeps the cold out of whatever it surrounds",
             "correct": False,
             "why": "There is nothing called cold to keep out. What moves is "
                    "energy, and it moves outwards."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e02",
        "band": "easier",
        "text": "What does most of the insulating in a woollen jumper?",
        "options": [
            {"text": "The wool fibres themselves",
             "correct": False,
             "why": "The fibres hold the air in place. Squash the same wool "
                    "flat and it works far worse with exactly the same "
                    "fibres in it."},
            {"text": "The thickness of the thread it is knitted from",
             "correct": False,
             "why": "A thick thread packed tight holds LESS air than a fine "
                    "one knitted loosely, and it insulates worse."},
            {"text": "The dye, which reflects warmth back inwards",
             "correct": False,
             "why": "A white jumper and a black one of the same thickness "
                    "keep you equally warm."},
            {"text": "The air trapped between the fibres",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e03",
        "band": "easier",
        "text": "Why is a bare beaker kept on the bench throughout the test?",
        "options": [
            {"text": "To warm the room up so the other beakers cool more "
                     "slowly",
             "correct": False,
             "why": "One beaker changes a room's temperature by nothing "
                    "measurable, and warming the room would spoil the test "
                    "rather than help it."},
            {"text": "To use up the spare hot water",
             "correct": False,
             "why": "It is doing a job in the experiment, not tidying "
                    "something away."},
            {"text": "So every reading has something to be compared with",
             "correct": True},
            {"text": "To check that the thermometers all agree with each "
                     "other",
             "correct": False,
             "why": "A useful check, and a different one. This beaker is "
                    "there to show what happens with no lagging at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-e04",
        "band": "easier",
        "text": "In the bench test, which one thing is deliberately changed?",
        "options": [
            {"text": "The starting temperature of the water",
             "correct": False,
             "why": "Every beaker starts at 80 °C. If they did not, nothing "
                    "could be concluded from the finishing readings."},
            {"text": "The material and thickness of the lagging",
             "correct": True},
            {"text": "The volume of water in each beaker",
             "correct": False,
             "why": "All eight hold 200 cm³. More water would cool more "
                    "slowly whatever it was wrapped in."},
            {"text": "The temperature of the room",
             "correct": False,
             "why": "The room stays at 20 °C throughout, which is what makes "
                    "the eight readings comparable."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-07-s01",
        "band": "standard",
        "text": "Cotton wool at 3 layers finished at 64.4 °C and bubble wrap "
                "at 1 layer at 59.4 °C. What follows from that pair alone?",
        "options": [
            {"text": "Nothing about which material is better, because two "
                     "things differed",
             "correct": True},
            {"text": "That cotton wool is the better insulator of the two",
             "correct": False,
             "why": "The cotton wool was also three times as thick. You "
                    "cannot tell which of the two changes did it."},
            {"text": "That thickness makes no difference to either material",
             "correct": False,
             "why": "Every material on the bench improved with thickness — "
                    "and this pair does not test that either."},
            {"text": "That bubble wrap is the better insulator of the two",
             "correct": False,
             "why": "It is, at the SAME thickness. This pair cannot show it, "
                    "because this pair changed two things."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s02",
        "band": "standard",
        "text": "Foam finished at 70.3 °C and the bare beaker at 37.9 °C. "
                "What is the most accurate thing to say about the foam?",
        "options": [
            {"text": "It kept the water hot",
             "correct": False,
             "why": "It cooled by nearly ten degrees. Kept hot is doing a lot "
                    "of quiet work in that sentence."},
            {"text": "It stopped the transfer out of the beaker",
             "correct": False,
             "why": "Then the water would still be at 80 °C. It is not."},
            {"text": "It slowed the transfer, and the water still cooled by "
                     "9.7 °C",
             "correct": True},
            {"text": "It added 32.4 °C compared with the bare beaker",
             "correct": False,
             "why": "It added nothing at all. Both beakers cooled; one cooled "
                    "less."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s03",
        "band": "standard",
        "text": "You wrap a jumper tightly round a bottle of fridge-cold "
                "water and leave it an hour. What happens?",
        "options": [
            {"text": "It warms up faster than it would have done bare",
             "correct": False,
             "why": "That is what a jumper would do if it were a source of "
                    "warmth. It is not."},
            {"text": "It warms up to exactly room temperature within the hour",
             "correct": False,
             "why": "Bare, it would still be on its way there after an hour. "
                    "Wrapped, it is further behind still."},
            {"text": "It cools further, because the jumper draws warmth out "
                     "of it",
             "correct": False,
             "why": "The jumper is at room temperature and the bottle is "
                    "colder, so the transfer runs into the bottle, not out "
                    "of it."},
            {"text": "It stays cold longer than it would have done bare",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-s04",
        "band": "standard",
        "text": "Every material on the bench did better at 3 layers than at "
                "1. Why?",
        "options": [
            {"text": "More layers hold more still air in the way",
             "correct": True},
            {"text": "More layers weigh more, so they hold more energy",
             "correct": False,
             "why": "How much the lagging holds is not the point. What "
                    "matters is how slowly it passes a transfer on."},
            {"text": "More layers reflect more of the warmth back inwards",
             "correct": False,
             "why": "True of a shiny layer, and none of these four is shiny. "
                    "Newspaper and cotton wool reflect almost nothing."},
            {"text": "More layers get warmer, so the difference is smaller",
             "correct": False,
             "why": "The outer layer does end up cooler than the inner one. "
                    "But say what it is about the layers that slows things "
                    "down."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-07-h01",
        "band": "harder",
        "text": "A company claims its lagging \"keeps a tank hot for ever\". "
                "What result would falsify that?",
        "options": [
            {"text": "The lagged tank's temperature falling at all, ever",
             "correct": True},
            {"text": "The lagged tank cooling faster than an unlagged one",
             "correct": False,
             "why": "That would falsify a much weaker claim. For ever is "
                    "broken by any drop at all."},
            {"text": "The lagged tank reaching room temperature within a day",
             "correct": False,
             "why": "It would be broken long before that, at the first "
                    "reading that had moved."},
            {"text": "The lagged tank being no better than a cheaper "
                     "material",
             "correct": False,
             "why": "That would be a claim about value. The claim here is "
                    "about physics."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h02",
        "band": "harder",
        "text": "Polystyrene foam is about 95% trapped air by volume. What "
                "does that figure explain?",
        "options": [
            {"text": "Why it is waterproof",
             "correct": False,
             "why": "Sealed cells do keep water out, and that is a separate "
                    "property from the one the bench measured."},
            {"text": "Why it is cheap to make",
             "correct": False,
             "why": "Using little material does help the price. The question "
                    "is about how it performs."},
            {"text": "Why it beat the other three at both thicknesses",
             "correct": True},
            {"text": "Why it is a good conductor of electricity",
             "correct": False,
             "why": "It is an electrical insulator too, and for a different "
                    "reason entirely — nothing in it carries charge."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h03",
        "band": "harder",
        "text": "A snowman is dressed in a coat on a mild day. What happens "
                "compared with an undressed one?",
        "options": [
            {"text": "It melts faster, because the coat traps warmth against "
                     "it",
             "correct": False,
             "why": "The coat traps nothing warm. It is at air temperature "
                    "and so is everything around it."},
            {"text": "It melts at exactly the same rate, because a coat only "
                     "works on people",
             "correct": False,
             "why": "A coat does not know what is inside it. It slows a "
                    "transfer whichever way the transfer is running."},
            {"text": "It melts more slowly, because the coat slows the "
                     "transfer inwards",
             "correct": True},
            {"text": "It melts more slowly, because the coat gives it some of "
                     "its cold",
             "correct": False,
             "why": "Right answer, wrong reason, and the reason matters. "
                    "Nothing gives out cold; the coat slows energy coming in."},
        ],
        "figure": None,
    },
    {
        "id": "p1-07-h04",
        "band": "harder",
        "text": "Why is a thick loose duvet warmer than a thin packed one "
                "made of the same filling?",
        "options": [
            {"text": "Because the thick one weighs more and presses warmth in",
             "correct": False,
             "why": "Weight has nothing to do with it. A very light duvet can "
                    "be one of the warmest there is."},
            {"text": "Because the thick one holds more still air",
             "correct": True},
            {"text": "Because the packed one has been used more and has worn "
                     "out",
             "correct": False,
             "why": "A brand new packed duvet does the same thing. It is "
                    "about the structure, not the age."},
            {"text": "Because the filling in the thick one is a better "
                     "material",
             "correct": False,
             "why": "The question says both are the same filling, which is "
                    "what makes the comparison worth making."},
        ],
        "figure": None,
    },
]
