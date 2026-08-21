"""C8 lesson 04 — Group 1, the alkali metals: twelve questions (MRB-281).

The lesson's argument is one shape: every member of group 1 does the SAME
thing with water — hydroxide plus hydrogen, leaving an alkali — and what
changes down the column is only how hard the reaction is pushed. The page
teaches it by running lithium, sodium and potassium one at a time.

These twelve probe the angles the mastery ladder leaves alone: what stays the
same as well as what changes, where the heat comes from, and how far a trend
can be pushed into elements the student has never seen.

The distractors are built from the lesson's declared misconception.

`PTAB-07` (sodium melted because the water was hot) drives the wrong options
in e03, s01, s03 and h01. Each puts the energy into the trough rather than
into the reaction. s03 is the one that matters: the water is at room
temperature and lithium in the SAME trough does not melt, so the belief has to
explain why one metal melted and the other did not.

A second strand is the trend itself, and it is the one the next lesson exists
to break: e02, s02, h03 and h04 turn on reactivity rising DOWNWARD and on the
reason for it — an outer electron further from the nucleus and more easily
lost.

⚠️ **NO QUESTION HERE STATES A DENSITY TREND** (MRB-281, R4 flag 11). Lithium
0.53, sodium 0.97, potassium 0.86 is not monotonic, so there is no trend to
test and a distractor asserting one would be teaching a falsehood by offering
it. e04 uses floating — which all three do — and says only that.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "group-1-the-alkali-metals"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-04-e01",
        "band": "easier",
        # ⚑ Asks what the LEFTOVER SOLUTION proves, not what the products
        # are — the recall rung already asks for the products, and check 6 is
        # right that a bank restating a rung adds no depth.
        "text": "After a group 1 metal has reacted, the water in the trough "
                "turns universal indicator purple. What does that show?",
        "options": [
            {"text": "The solution is alkaline, because a metal hydroxide has "
                     "dissolved in it",
             "correct": True},
            {"text": "The solution is acidic, because hydrogen was given off "
                     "into it",
             "correct": False,
             "why": "The hydrogen leaves as a gas. What stays behind is the "
                    "hydroxide, and purple is the alkali end of the scale."},
            {"text": "The solution is neutral, because the metal has been "
                     "used up",
             "correct": False,
             "why": "Neutral is green. The metal being used up does not "
                    "remove what it turned into."},
            {"text": "The water was already alkaline before the metal went "
                     "in",
             "correct": False,
             "why": "Tap water is close to neutral. The colour appeared with "
                    "the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e02",
        "band": "easier",
        "text": "Which of lithium, sodium and potassium reacts most "
                "violently with water?",
        "options": [
            {"text": "Lithium, because it is at the top of the group",
             "correct": False,
             "why": "Top of group 1 is the LEAST violent. Lithium fizzes "
                    "steadily for nearly a minute."},
            {"text": "Potassium, because reactivity increases down the group",
             "correct": True},
            {"text": "Sodium, because it is in the middle and best balanced",
             "correct": False,
             "why": "There is nothing special about the middle. Sodium is "
                    "more violent than lithium and less than potassium."},
            {"text": "All three equally, because they are in the same group",
             "correct": False,
             "why": "Same group means the same REACTION, not the same "
                    "vigour."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e03",
        "band": "easier",
        "text": "A piece of sodium melts into a ball as it moves across the "
                "water. Where does the heat come from?",
        "options": [
            {"text": "From the water, which must have been warm to start with",
             "correct": False,
             "why": "The water is at room temperature. Lithium in the same "
                    "trough does not melt."},
            {"text": "From friction as the ball skates across the surface",
             "correct": False,
             "why": "The ball has already melted before it moves. Friction on "
                    "water is nowhere near enough."},
            {"text": "From the reaction, which releases energy as it happens",
             "correct": True},
            {"text": "From the air, which warms the metal once the oil is off",
             "correct": False,
             "why": "Air at room temperature cannot bring a metal to 98 °C."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-e04",
        "band": "easier",
        "text": "Lithium, sodium and potassium all sit on the surface of the "
                "water rather than sinking. What does that show?",
        "options": [
            {"text": "That they get less dense as you go down the group",
             "correct": False,
             "why": "There is no such trend: lithium is 0.53, sodium 0.97 and "
                    "potassium 0.86. All that can be said is that all three "
                    "float."},
            {"text": "That they get more dense as you go down the group",
             "correct": False,
             "why": "The figures do not run that way either, and no trend in "
                    "density is claimed anywhere in this lesson."},
            {"text": "That they are not really metals, since metals sink",
             "correct": False,
             "why": "They are metals — shiny when cut and good conductors. "
                    "Floating is one of the habits they break."},
            {"text": "That all three are less dense than water",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-04-s01",
        "band": "standard",
        "text": "Why does sodium melt during its reaction with water when "
                "lithium does not?",
        "options": [
            {"text": "Sodium releases energy faster and melts at a much lower "
                     "temperature",
             "correct": True},
            {"text": "Sodium is put into warmer water than lithium is",
             "correct": False,
             "why": "Both go into the same trough at the same temperature. "
                    "The metal is the only thing that changed."},
            {"text": "Sodium is softer, so it melts more easily in any "
                     "situation",
             "correct": False,
             "why": "Softness at room temperature and melting point are "
                    "different properties. Lithium is soft too."},
            {"text": "Sodium absorbs heat from the water and so warms up",
             "correct": False,
             "why": "The water gets warmer, not colder. The energy is coming "
                    "OUT of the reaction."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s02",
        "band": "standard",
        "text": "Why does reactivity increase going down group 1?",
        "options": [
            {"text": "Because the atoms get heavier and heavier atoms react "
                     "faster",
             "correct": False,
             "why": "Mass is not the mechanism. Group 7 gets heavier downwards "
                    "and gets LESS reactive."},
            {"text": "Because the outer electron sits further out and is "
                     "lost more easily",
             "correct": True},
            {"text": "Because there are more outer electrons to lose lower "
                     "down",
             "correct": False,
             "why": "Every group 1 atom has exactly one outer electron. That "
                    "is what makes them a group."},
            {"text": "Because the metals lower down are softer to cut",
             "correct": False,
             "why": "Softness runs alongside reactivity; it does not cause "
                    "it. Both come from the same loose outer electron."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s03",
        "band": "standard",
        "text": "A student says the trough water must be hot, because the "
                "sodium melted in it. What one observation would settle it?",
        "options": [
            {"text": "Watch whether the sodium floats, since hot water is "
                     "less dense",
             "correct": False,
             "why": "Sodium floats in cold water too. Floating tells you "
                    "nothing about temperature here."},
            {"text": "Check the indicator, since hot water turns it purple "
                     "faster",
             "correct": False,
             "why": "The indicator responds to the hydroxide formed, not to "
                    "temperature."},
            {"text": "Put a thermometer in the trough before the sodium goes "
                     "in",
             "correct": True},
            {"text": "Try again with a bigger piece to see whether it melts "
                     "sooner",
             "correct": False,
             "why": "A bigger piece is more dangerous and tests the wrong "
                    "thing — it changes the reaction, not the water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-s04",
        "band": "standard",
        "text": "Why are the group 1 metals stored under oil?",
        "options": [
            {"text": "To stop them drying out and crumbling into powder",
             "correct": False,
             "why": "They do not dry out. The problem is what the air DOES to "
                    "them, not what it takes away."},
            {"text": "To keep them cold, since they melt at low temperatures",
             "correct": False,
             "why": "Oil at room temperature keeps nothing cold, and 63 °C is "
                    "still far above a laboratory."},
            {"text": "To make them easier to cut with a knife when needed",
             "correct": False,
             "why": "They cut easily either way. The oil is a barrier, not a "
                    "lubricant."},
            {"text": "To keep air and water away from the metal surface",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-04-h01",
        "band": "harder",
        "text": "A hand warmer and a piece of sodium on water both get hot "
                "without anything being plugged in. What do the two have in "
                "common?",
        "options": [
            {"text": "Both release energy that was already stored in the "
                     "chemicals",
             "correct": True},
            {"text": "Both take heat in from the room and concentrate it",
             "correct": False,
             "why": "Taking heat in would COOL the room. Both of these warm "
                    "their surroundings."},
            {"text": "Both create new energy as the reaction proceeds",
             "correct": False,
             "why": "Energy is never created. It was stored in the "
                    "arrangement of the chemicals beforehand."},
            {"text": "Both need to be heated before anything begins",
             "correct": False,
             "why": "Neither does. A hand warmer starts with a snap and "
                    "sodium starts the moment it touches water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h02",
        "band": "harder",
        "text": "Caesium is two places below potassium in group 1. Which "
                "prediction about its reaction with water is best supported?",
        "options": [
            {"text": "It reacts less violently, since the trend levels off "
                     "lower down",
             "correct": False,
             "why": "Nothing in the group suggests a levelling off, and "
                    "caesium is in fact the most violent of them."},
            {"text": "It reacts more violently and still gives a hydroxide "
                     "and hydrogen",
             "correct": True},
            {"text": "It reacts more violently and gives a different set of "
                     "products",
             "correct": False,
             "why": "The products are what does NOT change down a group. Only "
                    "the vigour does."},
            {"text": "It does not react, because very large atoms are "
                     "unreactive",
             "correct": False,
             "why": "Large atoms in group 1 are the MOST reactive, because "
                    "the outer electron is furthest out."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h03",
        "band": "harder",
        "text": "Group 1 gets more reactive downwards and group 7 gets less "
                "reactive downwards. What single idea explains both?",
        "options": [
            {"text": "That heavier atoms always react more slowly than "
                     "lighter ones",
             "correct": False,
             "why": "That would predict both groups running the same way, and "
                    "they do not."},
            {"text": "That each group happens to follow its own unrelated "
                     "rule",
             "correct": False,
             "why": "Two unrelated rules is what you say when you have not "
                    "found the reason. There is one reason."},
            {"text": "That the outer electron is further from the nucleus in "
                     "a bigger atom",
             "correct": True},
            {"text": "That metals become less metallic further down the "
                     "table",
             "correct": False,
             "why": "Group 1 becomes more strongly metallic downwards, and "
                    "group 7 contains no metals at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-04-h04",
        "band": "harder",
        "text": "Why is a prediction about rubidium more trustworthy than a "
                "prediction about a brand-new element placed in group 1, "
                "period 8?",
        "options": [
            {"text": "Because rubidium is lighter, and light elements are "
                     "easier to predict",
             "correct": False,
             "why": "Mass is not what makes a prediction safe. Evidence is."},
            {"text": "Because rubidium is a metal and the new element might "
                     "not be",
             "correct": False,
             "why": "Anything placed in group 1 is expected to be a metal. "
                    "That part is not in doubt."},
            {"text": "Because group 1 stops at rubidium and goes no further",
             "correct": False,
             "why": "Caesium and francium are both below it. The group does "
                    "not stop there."},
            {"text": "Because rubidium sits inside the range where the trend "
                     "has been tested",
             "correct": True},
        ],
        "figure": None,
    },
]
