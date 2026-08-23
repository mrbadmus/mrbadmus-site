"""C8 lesson 07 — Metal and non-metal oxides: twelve questions (MRB-281).

The lesson's argument is one shape: which side of the periodic table an element
came from decides which way its oxide takes the water on the pH scale. The page
teaches it with a six-oxide bench and two beakers, and it spends most of its
length on the two places the famous version of that rule breaks.

These twelve probe the angles the mastery ladder leaves alone: what the word
`oxide` covers, what a pH reading is actually a measurement OF, what the acid
test can find that the water test cannot, and where the two-sided rule runs out.

The distractors are built from the lesson's three declared misconceptions.

`PTAB-11` (alkaline and basic mean the same thing) drives the wrong options in
e02, s01, s03 and h01. Each treats a pH reading as a verdict on what a substance
IS rather than a report on what is dissolved. h01 is the one that matters: it
puts the acid test and the water test side by side on the same solid, so the
belief has to explain why the two disagree and cannot.

`PTAB-12` (if it does not move the pH it is not a base) drives e03, s02 and h03,
where an unmoved reading is read as a negative result. h03 is the register's own
case put as a laboratory decision, which is where a student actually meets it.

`PTAB-13` (all oxides dissolve) drives e04, s04 and h04. The bench holds two
that dissolve completely, one that dissolves a little, one that does not
dissolve at all and two that are not solids in the first place, so the belief is
contradicted six ways on the page and is worth asking about directly.

A fourth strand, on the page and in none of the three register entries, is that
a rule can have a boundary without having a hole: e01 and h02 are built on the
staircase elements and on water, both of which qualify the two-sided rule
without overturning it (MRB-225).

⚠️ MRB-278 · ANSWER POSITION. The correct answer's index cycles 0, 1, 2, 3
through each band, so this file holds three of each.

⚠️ BAND VALUES ARE FULL WORDS — see `questions_01_metals_and_non_metals.py`.
"""

UNIT = "C8"
LESSON = "metal-and-non-metal-oxides"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c8-07-e01",
        "band": "easier",
        "text": "What is an oxide?",
        "options": [
            {"text": "An element that has joined with oxygen",
             "correct": True},
            {"text": "Any substance that turns universal indicator red",
             "correct": False,
             "why": "That describes an acid. Calcium oxide is an oxide and it "
                    "turns the indicator purple."},
            {"text": "A gas given off whenever something is burned",
             "correct": False,
             "why": "Magnesium oxide is a white solid. An oxide can be a "
                    "solid, a liquid or a gas."},
            {"text": "A metal that has been left out in the air too long",
             "correct": False,
             "why": "Non-metals form oxides too — carbon dioxide is one, and "
                    "so is water."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e02",
        "band": "easier",
        "text": "Magnesium oxide is stirred into water and the pH reads 10. "
                "What word describes that solution?",
        "options": [
            {"text": "Acidic, because a solid was added to it",
             "correct": False,
             "why": "Adding a solid says nothing about the direction. It is "
                    "the reading that decides, and 10 is above 7."},
            {"text": "Alkaline, because the reading is above 7",
             "correct": True},
            {"text": "Neutral, because magnesium oxide is a metal oxide",
             "correct": False,
             "why": "Neutral is exactly 7. Metal oxides that dissolve go "
                    "above it."},
            {"text": "Acidic, because every oxide dissolves to give an acid",
             "correct": False,
             "why": "Only non-metal oxides do that. Magnesium is a metal."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e03",
        "band": "easier",
        "text": "What does a base do to an acid?",
        "options": [
            {"text": "It makes the acid stronger",
             "correct": False,
             "why": "It does the opposite — it uses the acid up."},
            {"text": "It dissolves in it without changing at all",
             "correct": False,
             "why": "Something new is made. Copper oxide plus sulfuric acid "
                    "gives blue copper sulfate."},
            {"text": "It reacts with it to make a salt and water",
             "correct": True},
            {"text": "Nothing, unless the base has already dissolved in water",
             "correct": False,
             "why": "Copper oxide will not dissolve and still reacts with "
                    "acid. That is the whole of the lesson."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-e04",
        "band": "easier",
        "text": "Six oxides were put into water. Two dissolved completely, one "
                "dissolved a little, one did not dissolve at all and two were "
                "gases. What does that show about oxides?",
        "options": [
            {"text": "That only gases are really oxides",
             "correct": False,
             "why": "Calcium oxide and copper oxide are solids and both are "
                    "oxides."},
            {"text": "That an oxide has to dissolve before it is an oxide",
             "correct": False,
             "why": "Copper oxide dissolved in none of it and is still an "
                    "oxide."},
            {"text": "That water can only hold a certain number of oxides",
             "correct": False,
             "why": "Each beaker held one oxide. How much dissolves depends on "
                    "the substance, not on a limit."},
            {"text": "That being an oxide says nothing about whether it "
                     "dissolves",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c8-07-s01",
        "band": "standard",
        "text": "What is a pH reading actually a measurement of?",
        "options": [
            {"text": "What is dissolved in the solution being tested",
             "correct": True},
            {"text": "How much solid was tipped into the beaker",
             "correct": False,
             "why": "A whole spatula of copper oxide moves the reading no "
                    "further than a pinch does, because almost none of it "
                    "goes in."},
            {"text": "Whether the substance is a metal or a non-metal",
             "correct": False,
             "why": "Copper oxide and water both read 7 and one is a metal "
                    "oxide."},
            {"text": "How strongly the substance would react with an acid",
             "correct": False,
             "why": "Copper oxide reacts readily with acid and its reading "
                    "never moves at all."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s02",
        "band": "standard",
        "text": "A student says copper oxide cannot be a base because the pH "
                "stayed at 7. What is the one test that settles it?",
        "options": [
            {"text": "Leave it in the water overnight and read the pH again",
             "correct": False,
             "why": "Time does not make an insoluble solid dissolve. The "
                    "reading is the same in the morning."},
            {"text": "Add it to an acid and see whether a salt and water form",
             "correct": True},
            {"text": "Grind it finer, so more of it fits into the same beaker",
             "correct": False,
             "why": "Grinding speeds a reaction up; it does not make an "
                    "insoluble solid soluble."},
            {"text": "Warm the water, because a warm solution reads higher",
             "correct": False,
             "why": "Warming does not turn a solid that will not dissolve "
                    "into one that will."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s03",
        "band": "standard",
        "text": "Copper oxide and water were both put into beakers and both "
                "read pH 7. Why is that the same number for two different "
                "reasons?",
        "options": [
            {"text": "Because the copper oxide beaker had not been stirred "
                     "enough",
             "correct": False,
             "why": "Stirring does not help. Copper oxide is insoluble however "
                    "long you stir it."},
            {"text": "Because both of them are neutral substances",
             "correct": False,
             "why": "Water is neutral. Copper oxide is a base, and the reading "
                    "simply cannot see it."},
            {"text": "Because water is neutral, and the copper oxide never "
                     "dissolved",
             "correct": True},
            {"text": "Because 7 is what any solid gives when it is added to "
                     "water",
             "correct": False,
             "why": "Calcium oxide is a solid and it took the same water to "
                    "12."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-s04",
        "band": "standard",
        "text": "Calcium oxide took the water to pH 12 and magnesium oxide "
                "took it only to pH 10. Both are metal oxides. What explains "
                "the difference?",
        "options": [
            {"text": "Magnesium oxide is an acidic oxide and calcium oxide is "
                     "not",
             "correct": False,
             "why": "Both are metal oxides and both are bases. Neither is "
                    "acidic."},
            {"text": "Calcium is further down group 2, so its oxide is a "
                     "stronger acid",
             "correct": False,
             "why": "Neither oxide is an acid. Position is not what is being "
                    "asked about here."},
            {"text": "Magnesium oxide was tested in colder water than the "
                     "calcium oxide",
             "correct": False,
             "why": "Both beakers held the same water. The difference is in "
                    "the substances."},
            {"text": "Much more of the calcium oxide dissolved, so there was "
                     "more of it in solution",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c8-07-h01",
        "band": "harder",
        "text": "The same black powder leaves the pH at 7 in one test and "
                "produces a blue salt in another. Which pair of words describes "
                "it correctly?",
        "options": [
            {"text": "Basic, but never alkaline",
             "correct": True},
            {"text": "Alkaline, but never basic",
             "correct": False,
             "why": "It is the wrong way round. Alkaline describes a solution, "
                    "and this one never made one."},
            {"text": "Neutral, and therefore also a base",
             "correct": False,
             "why": "Neutral describes the solution the powder sat in, not the "
                    "powder. The two are not the same thing."},
            {"text": "Acidic in water and basic in acid",
             "correct": False,
             "why": "Nothing behaves as an acid in one beaker and a base in "
                    "the next. It was a base in both."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h02",
        "band": "harder",
        "text": "Aluminium oxide reacts with acids the way a metal oxide "
                "should, and with alkalis the way a non-metal oxide should. "
                "What does that tell you about the rule in this lesson?",
        "options": [
            {"text": "That the rule was never supported by any evidence",
             "correct": False,
             "why": "Six oxides on the bench went exactly as the rule "
                    "predicts. That is evidence."},
            {"text": "That the rule has a boundary, where the table has one "
                     "too",
             "correct": True},
            {"text": "That aluminium has been placed in the wrong group",
             "correct": False,
             "why": "Aluminium sits on the staircase between the two sides, "
                    "which is exactly where its oxide behaves as it does."},
            {"text": "That every oxide is really both acidic and basic at once",
             "correct": False,
             "why": "Sulfur dioxide reacts with alkalis and not with acids. "
                    "Most oxides pick a side."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h03",
        "band": "harder",
        "text": "A technician needs to know whether an unlabelled white powder "
                "is a metal oxide, and universal indicator in water gives 7. "
                "What should the technician conclude?",
        "options": [
            {"text": "It is not a metal oxide, because the reading did not "
                     "rise",
             "correct": False,
             "why": "That is the copper-oxide trap. An insoluble metal oxide "
                    "gives exactly this reading."},
            {"text": "It is a non-metal oxide, because only those leave water "
                     "at 7",
             "correct": False,
             "why": "Most non-metal oxides take the water below 7. Water "
                    "itself is the exception, not the rule."},
            {"text": "Nothing yet, and the powder should be tried with a "
                     "dilute acid",
             "correct": True},
            {"text": "It is a metal oxide, because non-metal oxides are all "
                     "gases",
             "correct": False,
             "why": "The reading supports neither answer, and plenty of "
                    "non-metal oxides are not gases."},
        ],
        "figure": None,
    },
    {
        "id": "c8-07-h04",
        "band": "harder",
        "text": "Rain that has fallen through clean country air is already "
                "slightly acidic, at about pH 6, before it touches anything. "
                "Why?",
        "options": [
            {"text": "Because rain water picks up acid from the clouds it "
                     "formed in",
             "correct": False,
             "why": "Cloud droplets are the same water. Something has to "
                    "dissolve in them to change the pH."},
            {"text": "Because sunlight breaks water down into an acid as it "
                     "falls",
             "correct": False,
             "why": "Water is not broken down by sunlight on the way to the "
                    "ground."},
            {"text": "Because dust in the air is acidic and dissolves in the "
                     "drops",
             "correct": False,
             "why": "Country air is not full of acidic dust, and the effect is "
                    "measured everywhere, including over the sea."},
            {"text": "Because carbon dioxide from the air dissolves in it",
             "correct": True},
        ],
        "figure": None,
    },
]
