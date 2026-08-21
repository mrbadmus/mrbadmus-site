"""C9 lesson 01 — The reactivity series: twelve questions (MRB-281).

The lesson's argument is one shape: reactivity is a property of the element,
it is settled by evidence rather than by how a metal looks or feels, and the
order it produces holds for every reaction and not just the test that made it.
The page teaches it with twelve tubes — six metals against cold water and
dilute acid — and a bench that sorts them into three bands.

These twelve probe the angles the mastery ladder leaves alone: what a null
result is worth, why two tests are needed rather than one, and what carbon is
doing in a list of metals.

The distractors are built from the lesson's declared misconceptions.

`MATL-01` (a metal that does nothing in cold water is unreactive) drives the
wrong options in e02, s01 and h01. Each treats one liquid as a verdict. s01 is
the one that matters: it gives a metal that fails the water test and passes the
acid one, so the belief has to account for a result it has already seen.

`MATL-02` (reactivity is strength or hardness) drives e03, s03 and h02, where
a physical property is read as a chemical one.

`MATL-03` (carbon cannot belong in an order of metals) drives e04 and h04.

⚠️ **NO QUESTION ASKS A STUDENT TO PUT POTASSIUM IN ACID.** The lesson's own
bench declines that cell on safety grounds (§5 flag 2) and a question that
asked for the result would undo the decline.

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — `easier`, `standard`, `harder`, never the
letters.
"""

UNIT = "C9"
LESSON = "the-reactivity-series"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c9-01-e01",
        "band": "easier",
        "text": "What does a metal's position in the reactivity series tell "
                "you?",
        "options": [
            {"text": "How readily it takes part in a chemical reaction",
             "correct": True},
            {"text": "How hard it is to scratch or cut with a knife",
             "correct": False,
             "why": "Sodium is soft enough to cut and near the top; steel is "
                    "hard and low down."},
            {"text": "How much one cubic centimetre of it weighs",
             "correct": False,
             "why": "Density is a separate property. Lithium floats and is "
                    "highly reactive."},
            {"text": "How long ago it was first discovered by chemists",
             "correct": False,
             "why": "Gold has been known for millennia and is the least "
                    "reactive metal on the list."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e02",
        "band": "easier",
        "text": "Iron granules sit unchanged in cold water but fizz gently in "
                "dilute acid. What does that tell you?",
        "options": [
            {"text": "Iron is unreactive, because the water test showed "
                     "nothing",
             "correct": False,
             "why": "One liquid is not a verdict. The acid test shows iron "
                    "reacting perfectly well."},
            {"text": "Iron is in the middle of the series — below the metals "
                     "that manage water",
             "correct": True},
            {"text": "Iron is at the top of the series, because it reacted at "
                     "all",
             "correct": False,
             "why": "The top of the series reacts with cold water alone. Iron "
                    "needs acid."},
            {"text": "The water must have been contaminated in some way",
             "correct": False,
             "why": "Iron genuinely does almost nothing in cold water. The "
                    "result is real."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e03",
        "band": "easier",
        "text": "Magnesium ribbon bends between your fingers. A steel nail "
                "does not. Which is higher in the reactivity series?",
        "options": [
            {"text": "Steel, because a stiffer metal holds itself together "
                     "better",
             "correct": False,
             "why": "Stiffness is a physical property. It says nothing about "
                    "reactions."},
            {"text": "Neither — bending has nothing to do with the series at "
                     "all",
             "correct": False,
             "why": "True that bending is irrelevant, but one of them IS "
                    "higher: magnesium is."},
            {"text": "Magnesium, and its softness is beside the point",
             "correct": True},
            {"text": "Steel, because iron is a stronger element than "
                     "magnesium",
             "correct": False,
             "why": "Strength and reactivity are different properties, and "
                    "magnesium is above iron."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-e04",
        "band": "easier",
        "text": "Carbon is a non-metal. Why is it in the reactivity series at "
                "all?",
        "options": [
            {"text": "Because it is found in the same rocks as many metals "
                     "are",
             "correct": False,
             "why": "Where an element is found does not put it in an order "
                    "of reactivity."},
            {"text": "Because it was discovered at the same time as the "
                     "metals were",
             "correct": False,
             "why": "Discovery dates have nothing to do with the order."},
            {"text": "Because it is a solid at room temperature, like most "
                     "metals",
             "correct": False,
             "why": "So is sulfur, and sulfur is not in the series."},
            {"text": "Because it can take oxygen away from the oxides of "
                     "metals below it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c9-01-s01",
        "band": "standard",
        "text": "A student concludes that zinc is unreactive because it does "
                "nothing in cold water. What is the flaw?",
        "options": [
            {"text": "Doing nothing in one liquid only rules out the top of "
                     "the series",
             "correct": True},
            {"text": "The zinc was probably coated and needed cleaning first",
             "correct": False,
             "why": "Even clean zinc does nothing in cold water. The result "
                    "is real and it is informative."},
            {"text": "There is no flaw — nothing happened, so zinc is "
                     "unreactive",
             "correct": False,
             "why": "Zinc fizzes steadily in dilute acid, which an unreactive "
                    "metal would not do."},
            {"text": "Cold water is not a valid test for any metal",
             "correct": False,
             "why": "It is the test that separates the top three of the "
                    "series from everything else."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s02",
        "band": "standard",
        "text": "Why does the reactivity series need two tests rather than "
                "one?",
        "options": [
            {"text": "Because a single test might have been done incorrectly "
                     "the first time",
             "correct": False,
             "why": "Repeating a test checks the test. A DIFFERENT test is "
                    "what separates a different part of the list."},
            {"text": "Because water separates the top and acid separates the "
                     "middle",
             "correct": True},
            {"text": "Because acids react with every metal and water reacts "
                     "with none",
             "correct": False,
             "why": "Copper does nothing in acid, and potassium is violent in "
                    "water. Neither half is true."},
            {"text": "Because two results always give a more accurate average",
             "correct": False,
             "why": "These are not measurements being averaged. They are two "
                    "different questions."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s03",
        "band": "standard",
        "text": "Gold is used for jewellery that is worn every day for "
                "decades. Which property makes it suitable?",
        "options": [
            {"text": "It is the hardest metal, so it resists scratching",
             "correct": False,
             "why": "Gold is notably soft — soft enough that it is usually "
                    "alloyed before use."},
            {"text": "It is the heaviest metal, so it feels substantial",
             "correct": False,
             "why": "It is dense, and that is not why it survives being "
                    "worn."},
            {"text": "It is at the bottom of the reactivity series and does "
                     "not react",
             "correct": True},
            {"text": "It conducts heat well, so it warms to the skin quickly",
             "correct": False,
             "why": "Every metal conducts heat well. That is not what keeps "
                    "it looking new."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-s04",
        "band": "standard",
        "text": "Potassium is not put into dilute acid on the bench in this "
                "lesson. Why not?",
        "options": [
            {"text": "Because potassium does not react with acids at all",
             "correct": False,
             "why": "It would react — far too fast. That is the reason it is "
                    "not done."},
            {"text": "Because the acid would be neutralised before anything "
                     "happened",
             "correct": False,
             "why": "Nothing here neutralises the acid, and the reaction "
                    "would begin at once."},
            {"text": "Because acid results cannot be compared with water "
                     "results",
             "correct": False,
             "why": "They are compared throughout — that is how the bands are "
                    "built."},
            {"text": "Because dilute acid is mostly water and potassium is "
                     "violent with water alone",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c9-01-h01",
        "band": "harder",
        "text": "An unknown metal does nothing in cold water, does nothing in "
                "dilute acid, and is displaced from its sulfate by iron. "
                "Where does it sit?",
        "options": [
            {"text": "Below iron and near the bottom of the series",
             "correct": True},
            {"text": "Above iron, because it survived both liquid tests "
                     "unchanged",
             "correct": False,
             "why": "Surviving both tests puts it BELOW the metals that "
                    "react, not above them."},
            {"text": "At the very top, because nothing was able to change it",
             "correct": False,
             "why": "The top of the series is the most reactive part of it. "
                    "This metal reacted with nothing."},
            {"text": "Nowhere — three results that disagree cannot place a "
                     "metal",
             "correct": False,
             "why": "The three results agree perfectly. All of them put it "
                    "low."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h02",
        "band": "harder",
        "text": "Aluminium is high in the reactivity series, yet an aluminium "
                "pan can be filled with water and boiled with nothing "
                "happening. Why?",
        "options": [
            {"text": "The series is wrong about aluminium and should place it "
                     "lower",
             "correct": False,
             "why": "The position is right and is confirmed by how hard "
                    "aluminium is to extract."},
            {"text": "An oxide layer forms in air and keeps the water off the "
                     "metal",
             "correct": True},
            {"text": "Aluminium only reacts once it has been heated well "
                     "above boiling",
             "correct": False,
             "why": "Fresh aluminium reacts at room temperature. The coating "
                    "is what prevents it."},
            {"text": "Pans are made from an alloy that contains no aluminium "
                     "at all",
             "correct": False,
             "why": "They are aluminium. The coating is the explanation, not "
                    "the composition."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h03",
        "band": "harder",
        "text": "Why is “nothing happened” treated as evidence in "
                "this lesson rather than as a failed experiment?",
        "options": [
            {"text": "Because every experiment must be recorded whether it "
                     "worked or not",
             "correct": False,
             "why": "True as a habit, and it is not why this particular null "
                    "result is useful."},
            {"text": "Because a result that is repeated becomes reliable over "
                     "time",
             "correct": False,
             "why": "Repetition checks a result. It does not turn a null one "
                    "into information."},
            {"text": "Because it rules out part of the series and narrows "
                     "where the metal can be",
             "correct": True},
            {"text": "Because it shows the apparatus was working correctly "
                     "throughout",
             "correct": False,
             "why": "It shows nothing about the apparatus. It shows something "
                    "about the metal."},
        ],
        "figure": None,
    },
    {
        "id": "c9-01-h04",
        "band": "harder",
        "text": "Where does carbon's position in the series come from, given "
                "that it does not react with water or acid the way the metals "
                "do?",
        "options": [
            {"text": "From its atomic mass, which falls between magnesium's "
                     "and zinc's",
             "correct": False,
             "why": "Mass has no bearing on the order. Carbon is far lighter "
                    "than both."},
            {"text": "From an average of the metals on either side of it in "
                     "the list",
             "correct": False,
             "why": "A position cannot be averaged into existence. It has to "
                    "be earned by a result."},
            {"text": "From the fact that it is a solid, like the metals "
                     "around it",
             "correct": False,
             "why": "Sulfur is a solid too and has no place in the series."},
            {"text": "From which metal oxides it can and cannot take the "
                     "oxygen from",
             "correct": True},
        ],
        "figure": None,
    },
]
