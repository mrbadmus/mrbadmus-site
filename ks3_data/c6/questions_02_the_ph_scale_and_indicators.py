"""C6 lesson 02 — The pH scale and indicators: twelve questions (MRB-269).

The lesson's argument is that a colour is a READING. These twelve probe the
three ways that goes wrong: treating the scale as an ordinary number line,
treating the dye as part of what is being measured, and treating pH as a
measure of how much acid there is.

The distractors are built from the lesson's two declared misconceptions.

`ACID-03` (pH 2 is twice as acidic as pH 4) drives e04, s02, h01 and h04. h01
is the one that matters: it asks for the FACTOR between two readings and every
wrong option is a different arithmetic on the same two numbers — subtract them,
divide them, treat them as ranks — which is the shape of the mistake rather
than the belief stated flat.

`ACID-04` (more indicator gives a different reading) drives s03 and h02, where
the amount of dye, or the depth of the colour, is treated as data.

A third strand, stated in the lesson and in neither register entry, is that pH
measures HOW ACIDIC and not HOW MUCH. e03, s04 and h03 are built on it, and h03
is Design's own third job put as a question: two bottles that read the same can
hold very different amounts of acid.

A fourth strand is that litmus and universal indicator are the same tool at
different resolutions. e01, e02 and s01 separate them by the QUESTION each one
answers rather than by which is better.

Every question here is new prose, and the bar is §13's. No correct answer is
strictly the longest in its set by four words or by 1.4x, and the twelve are
authored level across the four answer positions — three apiece (MRB-278).
"""

UNIT = "C6"
LESSON = "the-ph-scale-and-indicators"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c6-02-e01",
        "band": "easier",
        "text": "What colour is litmus in an alkali?",
        "options": [
            {"text": "Blue", "correct": True},
            {"text": "Red", "correct": False,
             "why": "Red is the acid answer. Litmus has exactly two colours "
                    "and each names one side of 7."},
            {"text": "Green", "correct": False,
             "why": "Green belongs to universal indicator at pH 7. Litmus has "
                    "no green and no middle."},
            {"text": "Purple", "correct": False,
             "why": "Purple is universal indicator at the far alkaline end. "
                    "Litmus reports only which side, not how far."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e02",
        "band": "easier",
        "text": "A solution turns universal indicator green. What is its pH?",
        "options": [
            {"text": "About 2, strongly acidic", "correct": False,
             "why": "The acid end of the chart is red and orange. Green is "
                    "the middle of it."},
            {"text": "7, which is neutral", "correct": True},
            {"text": "About 13, strongly alkaline", "correct": False,
             "why": "The far alkaline end is blue and purple. Green sits "
                    "between the two ends."},
            {"text": "Anywhere at all — green means no result", "correct":
             False,
             "why": "Green is a result and a precise one. Every colour on the "
                    "chart names a number."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e03",
        "band": "easier",
        "text": "Which of these does a pH number NOT tell you?",
        "options": [
            {"text": "Whether the solution is acidic or alkaline",
             "correct": False,
             "why": "That is the first thing it tells you: below 7 acidic, "
                    "above 7 alkaline."},
            {"text": "Which side of neutral the solution sits on",
             "correct": False,
             "why": "Same thing said the other way round, and pH answers it "
                    "immediately."},
            {"text": "How much acid is dissolved in the solution",
             "correct": True},
            {"text": "How acidic the solution is compared with another",
             "correct": False,
             "why": "Comparing two readings is exactly what the scale is "
                    "for — each step of one is a factor of ten."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e04",
        "band": "easier",
        "text": "How much more acidic is pH 3 than pH 4?",
        "options": [
            {"text": "One unit more acidic, since 4 minus 3 is 1",
             "correct": False,
             "why": "Subtracting is what you do on an ordinary number line. "
                    "Each step of one on this scale is a factor of ten."},
            {"text": "About a quarter more acidic, since 3 is close to 4",
             "correct": False,
             "why": "The numbers being close does not mean the liquids are. "
                    "One step apart is ten times apart."},
            {"text": "Slightly less acidic, since 3 is the smaller number",
             "correct": False,
             "why": "The smaller number is the MORE acidic one. The scale "
                    "runs the opposite way to the acidity."},
            {"text": "Ten times more acidic, because each step is a factor of "
                     "ten", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c6-02-s01",
        "band": "standard",
        "text": "A fish farmer must keep pond water between pH 6.5 and 8. "
                "Which tool does the job?",
        "options": [
            {"text": "Litmus, because it gives an instant answer either way",
             "correct": False,
             "why": "Both ends of that range are close to neutral, and litmus "
                    "only says which side of neutral. It cannot see the "
                    "difference."},
            {"text": "Universal indicator, because the job needs a number",
             "correct": True},
            {"text": "Neither, because pH cannot be measured in pond water",
             "correct": False,
             "why": "Pond water is a solution like any other and its pH is "
                    "measured routinely, usually with a meter."},
            {"text": "Litmus twice, once at each end of the acceptable range",
             "correct": False,
             "why": "Litmus gives the same answer at 6.5 and at 8 — one side "
                    "or the other. Running it twice adds nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s02",
        "band": "standard",
        "text": "Lemon juice reads pH 2 and rainwater reads pH 6. How far "
                "apart are they?",
        "options": [
            {"text": "Four steps, which is a small gap on a scale of fifteen",
             "correct": False,
             "why": "Four steps looks small and is not. Each step is a factor "
                    "of ten, so four of them is ten thousand times."},
            {"text": "Three times, because 6 divided by 2 is 3",
             "correct": False,
             "why": "Dividing the numbers is arithmetic on the labels. The "
                    "scale multiplies by ten at every step."},
            {"text": "Ten thousand times, because four steps is ten to the "
                     "fourth", "correct": True},
            {"text": "Twice, because 2 is half of 4 and 6 is close to it",
             "correct": False,
             "why": "Halving the number does not double the acidity. The "
                    "relationship is a factor of ten per step."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s03",
        "band": "standard",
        "text": "A student adds twice as much universal indicator to the same "
                "solution. What happens to the reading?",
        "options": [
            {"text": "It moves towards 7, because the dye dilutes the "
                     "solution", "correct": False,
             "why": "A few drops of dye cannot dilute a beaker, and the "
                    "reading did not move. Only the colour got deeper."},
            {"text": "It goes up, because more dye means more of everything",
             "correct": False,
             "why": "The dye is not the thing being measured. Adding more of "
                    "it makes the same reading easier to see."},
            {"text": "It becomes unreliable, because the sample is now "
                     "contaminated", "correct": False,
             "why": "Indicator is what you are supposed to add. It reports "
                    "the solution rather than changing it."},
            {"text": "Nothing, because the colour got deeper and the pH did "
                     "not change", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s04",
        "band": "standard",
        "text": "Enamel dissolves below about pH 5.5. A drink reads pH 3. "
                "What does that reading settle?",
        "options": [
            {"text": "That the drink is acidic enough to attack enamel",
             "correct": True},
            {"text": "That the drink will definitely rot a tooth in a week",
             "correct": False,
             "why": "How long the drink stays on the teeth matters as much as "
                    "the number. One reading cannot predict a week."},
            {"text": "That the drink contains more acid than one reading 4",
             "correct": False,
             "why": "pH says how acidic, not how much acid. A weak acid at "
                    "high concentration can read the same as a strong one at "
                    "low."},
            {"text": "That the drink is safe, because 3 is above zero",
             "correct": False,
             "why": "Being above zero is not the test. The line the lesson "
                    "gives is 5.5, and 3 is well below it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c6-02-h01",
        "band": "harder",
        "text": "Stomach acid reads pH 2 and vinegar reads pH 3. Which "
                "statement is right?",
        "options": [
            {"text": "Stomach acid is one unit stronger, which is a small "
                     "difference", "correct": False,
             "why": "One unit is a factor of ten, which is not a small "
                    "difference. Subtracting the labels is the wrong "
                    "arithmetic."},
            {"text": "Vinegar is stronger, because 3 is the bigger number "
                     "here", "correct": False,
             "why": "The scale runs the opposite way to the acidity. The "
                    "smaller number is the more acidic one."},
            {"text": "Stomach acid is ten times more acidic than the vinegar",
             "correct": True},
            {"text": "They are about the same, because both are close to the "
                     "acid end", "correct": False,
             "why": "Both are acidic and one is ten times the other. Being on "
                    "the same half of the scale does not make two readings "
                    "equal."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h02",
        "band": "harder",
        "text": "Two students test the same solution. One reads it as "
                "yellow-green and one as green. What settles the argument?",
        "options": [
            {"text": "Taking the average of the two colours they each named",
             "correct": False,
             "why": "Averaging two opinions about a colour produces a third "
                    "opinion. What is missing is a measurement."},
            {"text": "Using a pH meter, which reads a number rather than a "
                     "colour", "correct": True},
            {"text": "Adding more indicator so the colour is easier to judge",
             "correct": False,
             "why": "More dye makes the same colour deeper, not more precise. "
                    "The disagreement is about which colour, and it stays."},
            {"text": "Repeating the test, because one of them must have made "
                     "an error", "correct": False,
             "why": "Both may be reading a genuinely borderline colour. "
                    "Repeating a judgement by eye gives another judgement by "
                    "eye."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h03",
        "band": "harder",
        "text": "Vinegar and lemon juice both read pH 3. A student concludes "
                "they contain the same amount of acid. Why is that wrong?",
        "options": [
            {"text": "Because pH is measured on a scale that is not evenly "
                     "spaced", "correct": False,
             "why": "The scale being logarithmic is true and is a different "
                    "point. Two readings of 3 are the same reading whatever "
                    "the spacing."},
            {"text": "Because the two acids are different, so their readings "
                     "cannot be compared", "correct": False,
             "why": "Readings from different acids compare perfectly well — "
                    "that is what a scale is for. What they do not tell you "
                    "is the quantity."},
            {"text": "Because a pH meter is more accurate than universal "
                     "indicator", "correct": False,
             "why": "Accuracy is not the issue. Even two perfect readings of "
                    "3 would not settle how much acid is dissolved."},
            {"text": "Because pH says how acidic a solution is, not how much "
                     "acid is in it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h04",
        "band": "harder",
        "text": "A lake at pH 4 has to be brought back to 6. A student says "
                "that is a small job. What are they missing?",
        "options": [
            {"text": "That two steps means the lake is a hundred times too "
                     "acidic", "correct": True},
            {"text": "That a lake is too large for anything to be added to it",
             "correct": False,
             "why": "Lakes are limed routinely and it works. The size is a "
                    "practical problem, not the reasoning error."},
            {"text": "That pH 4 and pH 6 are both acidic, so nothing can be "
                     "done", "correct": False,
             "why": "Both being acidic is exactly why an alkali helps. The "
                    "target of 6 is reachable."},
            {"text": "That the pH would have to be pushed all the way to 7 to "
                     "help", "correct": False,
             "why": "A lake at 6 is fine for most fish. The target is not the "
                    "thing being missed."},
        ],
        "figure": None,
    },
]
