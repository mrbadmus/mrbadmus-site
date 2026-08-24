"""P1 lesson 04 — Heating and thermal equilibrium: twelve questions.

These probe the one driver: a temperature DIFFERENCE, and the fact that
running the transfer destroys it. The distractors are built from ENER-12 —
that cold moves into a warm object — and from the two habits the bench is
aimed at: deciding the direction from how much energy something holds rather
than from its temperature, and expecting a settled pair to carry on or swap
back.

No figures. Three of each answer index.
"""

UNIT = "P1"
LESSON = "heating-and-thermal-equilibrium"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-04-e01",
        "band": "easier",
        "text": "Two objects at different temperatures are put in contact. "
                "Which way does energy go?",
        "options": [
            {"text": "From the hotter one to the cooler one",
             "correct": True},
            {"text": "From the cooler one to the hotter one",
             "correct": False,
             "why": "That never happens on its own. Making it happen is what "
                    "a fridge is for, and a fridge has to be plugged in."},
            {"text": "In both directions equally, until one of them runs out",
             "correct": False,
             "why": "Nothing runs out. The transfer stops when the "
                    "temperatures match, with both objects still holding "
                    "plenty."},
            {"text": "From the larger object to the smaller one",
             "correct": False,
             "why": "Size does not decide it. A lit match heats a whole bath, "
                    "very slightly."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e02",
        "band": "easier",
        "text": "Two identical blocks at 80 °C and 20 °C are pushed together "
                "and left. What do they end up at?",
        "options": [
            {"text": "Both at 20 °C, because the cooler one wins",
             "correct": False,
             "why": "Nothing wins. Both change, and they meet in the middle."},
            {"text": "Both at 50 °C",
             "correct": True},
            {"text": "Both at 80 °C, because heat rises to the higher value",
             "correct": False,
             "why": "The hot block cools as the cool one warms. Neither can "
                    "end up hotter than it started."},
            {"text": "The hot one at 50 °C and the cool one at 30 °C",
             "correct": False,
             "why": "That would leave a difference between them, and a "
                    "difference is exactly what keeps the transfer going."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e03",
        "band": "easier",
        "text": "What does thermal equilibrium mean?",
        "options": [
            {"text": "Both objects have the same amount of energy in them",
             "correct": False,
             "why": "A teaspoon and a bath at the same temperature hold "
                    "wildly different amounts. It is the temperatures that "
                    "match."},
            {"text": "One object has stopped giving out any energy at all",
             "correct": False,
             "why": "Both are still radiating and both are still touching. "
                    "What has stopped is any NET transfer."},
            {"text": "Two objects are at the same temperature and nothing is "
                     "going either way",
             "correct": True},
            {"text": "Both objects have reached room temperature",
             "correct": False,
             "why": "Often true, and not what the word means. Two blocks can "
                    "reach equilibrium with each other at 50 °C in a room at "
                    "20 °C, on their way down."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-e04",
        "band": "easier",
        "text": "A fridge makes a bottle of milk cold. What is it actually "
                "doing?",
        "options": [
            {"text": "Pushing cold into the milk until it is full of it",
             "correct": False,
             "why": "There is no such substance as cold, so there is nothing "
                    "to push anywhere."},
            {"text": "Replacing the warm air around the bottle with cold air",
             "correct": False,
             "why": "The air does not get replaced. Something is being moved, "
                    "and it is not the air."},
            {"text": "Stopping energy from reaching the milk from outside",
             "correct": False,
             "why": "That is what the insulation in the door does. The "
                    "cooling itself is something more active."},
            {"text": "Taking energy out of the milk and dumping it outside "
                     "the fridge",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-04-s01",
        "band": "standard",
        "text": "A cup of coffee cools quickly at first and much more slowly "
                "later, in a room whose temperature never changes. Why?",
        "options": [
            {"text": "The coffee runs out of energy to give away",
             "correct": False,
             "why": "It still holds plenty at room temperature. What has run "
                    "out is the difference."},
            {"text": "The temperature difference shrinks, so the transfer "
                     "slows",
             "correct": True},
            {"text": "The room gradually stops being able to accept any more",
             "correct": False,
             "why": "A room is enormous compared with a cup and its "
                    "temperature barely moves. The change is at the coffee's "
                    "end."},
            {"text": "A skin forms on the surface and insulates it",
             "correct": False,
             "why": "That happens to some drinks and it is not the general "
                    "reason. Black coffee in a glass does the same thing."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s02",
        "band": "standard",
        "text": "A lit match at 800 °C is dropped into a bath at 40 °C. Which "
                "way does energy go, and why?",
        "options": [
            {"text": "From the bath to the match, because the bath holds far "
                     "more",
             "correct": False,
             "why": "How much is held does not decide it. Temperature does, "
                    "and the match is hotter by 760 degrees."},
            {"text": "Neither way, because the two are too different to "
                     "compare",
             "correct": False,
             "why": "Any temperature difference at all drives a transfer, "
                    "however different the two objects are."},
            {"text": "From the match to the bath, because the match is hotter",
             "correct": True},
            {"text": "From the match to the bath, because the match is "
                     "smaller",
             "correct": False,
             "why": "The right answer for the wrong reason. Swap the sizes "
                    "and the direction would not change."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s03",
        "band": "standard",
        "text": "Two blocks reach 60 °C together and are left for another ten "
                "minutes. What happens between them?",
        "options": [
            {"text": "They slowly drift back towards their starting "
                     "temperatures",
             "correct": False,
             "why": "That would need energy to move from cooler to hotter on "
                    "its own, which never happens."},
            {"text": "The one that started hotter goes on cooling a little",
             "correct": False,
             "why": "It has nothing to cool INTO. The other block is at the "
                    "same temperature."},
            {"text": "Both drift down together, because everything cools",
             "correct": False,
             "why": "True of the room, and the question is about the two "
                    "blocks. Between THEM, nothing more happens."},
            {"text": "Nothing, because there is no longer a difference",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-s04",
        "band": "standard",
        "text": "Why does the back of a working fridge feel warm?",
        "options": [
            {"text": "Because the energy taken out of the food has to go "
                     "somewhere",
             "correct": True},
            {"text": "Because the motor is inefficient and gets hot",
             "correct": False,
             "why": "The motor does warm up, and it is the smaller part. Most "
                    "of that warmth used to be inside the fridge."},
            {"text": "Because cold air sinks and warm air is pushed round the "
                     "back",
             "correct": False,
             "why": "The pipes at the back are warm to the touch, which is "
                    "not something moving air explains."},
            {"text": "Because the cold inside pushes the warmth outwards",
             "correct": False,
             "why": "Cold is not a thing and cannot push. What moves is "
                    "energy, and it moves the way the pump makes it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-04-h01",
        "band": "harder",
        "text": "A block at 45 °C and one at 15 °C settle at 30 °C. A "
                "different pair at 70 °C and 30 °C settles at 50 °C. What do "
                "these two runs together show?",
        "options": [
            {"text": "That how hot the pair is decides where they settle",
             "correct": False,
             "why": "Both pairs settle in the middle of their own two "
                    "numbers. Being hot or cool did not change that."},
            {"text": "That a bigger gap makes a hotter finish",
             "correct": False,
             "why": "The 45/15 pair has a 30-degree gap and finishes at 30; "
                    "the 70/30 pair has a 40-degree gap and finishes at 50. "
                    "The gap is not what set either finish."},
            {"text": "That identical blocks always settle at the middle of "
                     "the two temperatures",
             "correct": True},
            {"text": "That the cooler block always gains more than the hotter "
                     "one loses",
             "correct": False,
             "why": "In the first pair each block moves 15 degrees, and in "
                    "the second each moves 20. The gain and the loss are "
                    "equal every time, because the blocks are identical."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h02",
        "band": "harder",
        "text": "A student says \"the cold got into the house through the "
                "window\". Which rewrite keeps every word accurate?",
        "options": [
            {"text": "The cold outside pulled the warmth out through the "
                     "window",
             "correct": False,
             "why": "Still treats cold as a thing that can act. It cannot "
                    "pull anything, because it is not there."},
            {"text": "The house's thermal store emptied through the window "
                     "into the cooler air outside",
             "correct": True},
            {"text": "The window let cold air in and warm air out at the same "
                     "time",
             "correct": False,
             "why": "That describes a draught through an open window. A "
                    "closed one still loses energy, and the sentence has to "
                    "cover that."},
            {"text": "The window had no energy of its own, so it could not "
                     "keep the house warm",
             "correct": False,
             "why": "No window has energy of its own and that is true of a "
                    "good one too. It does not explain the difference."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h03",
        "band": "harder",
        "text": "Sparks from a sparkler at 1500 °C land on your hand and do "
                "not hurt. Why not?",
        "options": [
            {"text": "Because each spark carries almost no energy, being "
                     "almost weightless",
             "correct": True},
            {"text": "Because the sparks cool to room temperature before they "
                     "land",
             "correct": False,
             "why": "They are still glowing when they land, so they are still "
                    "very hot. Temperature is not the missing piece."},
            {"text": "Because skin is a good insulator and blocks the "
                     "transfer",
             "correct": False,
             "why": "Skin is a fair insulator and a 1500 °C object with any "
                    "mass behind it would burn straight through the "
                    "argument."},
            {"text": "Because the sparks are moving so fast they do not touch "
                     "for long",
             "correct": False,
             "why": "They land and sit there. Contact time is not what "
                    "saves you."},
        ],
        "figure": None,
    },
    {
        "id": "p1-04-h04",
        "band": "harder",
        "text": "Design the one experiment that most cleanly shows that "
                "insulation is nothing to do with keeping cold out.",
        "options": [
            {"text": "Wrap two hot beakers, one thickly and one thinly, and "
                     "compare",
             "correct": False,
             "why": "A good test of thickness. It says nothing about "
                    "direction, because both objects are hot."},
            {"text": "Wrap a hot object and a cold object identically and "
                     "time both",
             "correct": True},
            {"text": "Wrap one hot beaker and leave one bare, and compare "
                     "them",
             "correct": False,
             "why": "The standard test, and it is exactly the one a "
                    "keeps-cold-out explanation also predicts. It cannot "
                    "separate the two ideas."},
            {"text": "Put a wrapped beaker in a fridge and one in a warm room",
             "correct": False,
             "why": "Two things changed at once — the wrapping and the "
                    "surroundings — so nothing can be concluded from the "
                    "difference."},
        ],
        "figure": None,
    },
]
