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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-02-e05",
        "band": "easier",
        "text": "What does litmus tell you?",
        "options": [
            {"text": "Which side of neutral a solution is on",
             "correct": True},
            {"text": "A pH number, read off a printed chart by matching the "
                     "colour it turns against the shades along the scale",
             "correct": False,
             "why": "That is universal indicator. Litmus gives a side, not a "
                    "number"},
            {"text": "How dangerous a solution is",
             "correct": False,
             "why": "No indicator measures danger. Lemon juice turns litmus "
                    "red and is safe to drink"},
            {"text": "How much acid is dissolved in a solution",
             "correct": False,
             "why": "Neither indicator measures how much. Litmus answers one "
                    "question: acid or alkali"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e06",
        "band": "easier",
        "text": "What is a pH meter?",
        "options": [
            {"text": "A printed card of colours that the indicator is matched "
                     "against, so that a number can be read off by eye",
             "correct": False,
             "why": "That is the colour chart, and judging it by eye is "
                    "exactly what a meter avoids"},
            {"text": "An instrument that measures pH electrically and reads "
                     "out a number",
             "correct": True},
            {"text": "A dye that changes colour in acid",
             "correct": False,
             "why": "That is an indicator. A meter has no colour in it at "
                    "all"},
            {"text": "A tube for measuring out exact volumes of acid",
             "correct": False,
             "why": "That is a burette or a pipette. A meter measures pH"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e07",
        "band": "easier",
        "text": "What colour does universal indicator turn in a strong acid?",
        "options": [
            {"text": "Purple, which is the colour it turns at both ends of "
                     "the scale because both extremes are equally far from "
                     "neutral",
             "correct": False,
             "why": "Purple is the strong-alkali end. The two ends look "
                    "different, which is how the chart works"},
            {"text": "Green",
             "correct": False,
             "why": "Green is neutral, pH 7 — the middle of the scale"},
            {"text": "Red",
             "correct": True},
            {"text": "It does not change at all in a strong acid",
             "correct": False,
             "why": "It changes most strongly at the ends. A dye that did "
                    "nothing would be no use as an indicator"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e08",
        "band": "easier",
        "text": "What numbers does the pH scale run between?",
        "options": [
            {"text": "1 to 10",
             "correct": False,
             "why": "That would leave no room for the strongest acids and "
                    "alkalis, and it would put neutral in the wrong place"},
            {"text": "0 to 100, in the same way as a percentage, so that a pH "
                     "of 50 is exactly halfway and counts as neutral",
             "correct": False,
             "why": "It is not a percentage. The scale runs 0 to 14 and "
                    "neutral is 7"},
            {"text": "7 to 14, with acids given negative numbers",
             "correct": False,
             "why": "Acids have ordinary numbers below 7. Nothing on the "
                    "school scale is negative"},
            {"text": "0 to 14",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c6-02-s05",
        "band": "standard",
        "text": "A technician has to know at once whether a spill is acid or "
                "alkali, before choosing what to clean it up with. Which tool "
                "should they use?",
        "options": [
            {"text": "Litmus",
             "correct": True},
            {"text": "Universal indicator, because a pH number is always "
                     "better evidence than a colour and the chart takes only "
                     "a moment to consult",
             "correct": False,
             "why": "More information than the decision needs, and slower. "
                    "The question is one of two answers"},
            {"text": "A pH meter, calibrated first",
             "correct": False,
             "why": "Calibrating takes minutes, and there is a spill on the "
                    "floor. Litmus answers in seconds"},
            {"text": "Neither — wait for the spill to be identified",
             "correct": False,
             "why": "The whole point is to act now. Litmus gives the answer "
                    "the decision actually needs"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s06",
        "band": "standard",
        "text": "Litmus comes out of lichens, and red cabbage, beetroot and "
                "blackberries all work as indicators too. Why do so many "
                "plants do this?",
        "options": [
            {"text": "Because plants take acid up out of the soil, so their "
                     "colour is already a record of how acidic the ground "
                     "they grew in happened to be",
             "correct": False,
             "why": "A hydrangea does read the soil, and that is not why the "
                    "juice works in a test tube. The pigment itself changes"},
            {"text": "Because the pigment that colours them is a molecule "
                     "that changes shape in acid",
             "correct": True},
            {"text": "Because all plant juices are slightly acidic to start "
                     "with",
             "correct": False,
             "why": "Being acidic does not make something an indicator. "
                    "Vinegar is acidic and shows no colour change"},
            {"text": "Because boiling a plant releases litmus from it",
             "correct": False,
             "why": "Litmus comes from lichens specifically. The other plants "
                    "have pigments of their own"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s07",
        "band": "standard",
        "text": "A hydrangea flowers blue in one garden and pink in the "
                "garden next door, from cuttings off the same plant. What is "
                "the difference between the gardens?",
        "options": [
            {"text": "One gets more sunlight, and the pigment in the petals "
                     "is bleached to a paler shade by strong light over the "
                     "course of a summer",
             "correct": False,
             "why": "Blue and pink are not paler and darker versions of one "
                    "colour. The pigment is reading something chemical"},
            {"text": "How much water each plant is given",
             "correct": False,
             "why": "Water changes how well a plant grows, not what colour "
                    "its pigment turns"},
            {"text": "The pH of the soil",
             "correct": True},
            {"text": "The temperature of the two gardens",
             "correct": False,
             "why": "They are next door to each other. What differs "
                    "underground is the acidity"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s08",
        "band": "standard",
        "text": "Meters are more accurate than colour charts, and school "
                "laboratories still use charts. Give the best reason.",
        "options": [
            {"text": "Charts are more accurate than meters over the middle of "
                     "the scale, which is the part a school most often needs "
                     "to read",
             "correct": False,
             "why": "A meter is more accurate everywhere. Charts survive for "
                    "practical reasons rather than accurate ones"},
            {"text": "A meter cannot be used on a coloured solution",
             "correct": False,
             "why": "A meter works on any solution, and a COLOUR CHART is the "
                    "one that struggles with a coloured sample"},
            {"text": "Colour is easier to remember than a number",
             "correct": False,
             "why": "Remembering is not the issue. Cost and reliability "
                    "are"},
            {"text": "They are cheap, need no power, and cannot go out of "
                     "calibration halfway through a lesson",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c6-02-h05",
        "band": "harder",
        "text": "Vinegar reads pH 3, and battery acid is about a thousand "
                "times more acidic than vinegar. What is battery acid's pH?",
        "options": [
            {"text": "0",
             "correct": True},
            {"text": "2, because a thousand is a large number and one step is "
                     "as far as the scale can be pushed by any real solution "
                     "you would meet",
             "correct": False,
             "why": "One step is ten times. A thousand is ten times ten times "
                    "ten, so it is three steps"},
            {"text": "1",
             "correct": False,
             "why": "That is two steps, which is a hundred times. Three steps "
                    "down from 3 lands on 0"},
            {"text": "3000",
             "correct": False,
             "why": "The scale runs 0 to 14. You divide the acidity by ten "
                    "per step rather than multiplying the pH"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h06",
        "band": "harder",
        "text": "The lesson calls neutral a single point rather than a "
                "region. What does that mean in practice?",
        "options": [
            {"text": "That a solution has to be tested three times before it "
                     "can be called neutral, since a single reading of 7 "
                     "could always be a mistake",
             "correct": False,
             "why": "Repeats are good practice and are not what the phrase "
                    "means. It is about the scale, not the method"},
            {"text": "That only pH 7 exactly is neutral — 6.8 is acidic and "
                     "7.2 is alkaline",
             "correct": True},
            {"text": "That anything between 6 and 8 counts as neutral for "
                     "practical purposes",
             "correct": False,
             "why": "That is the region reading the phrase rules out. "
                    "Neutral is one value"},
            {"text": "That neutral solutions are rare",
             "correct": False,
             "why": "Pure water is neutral and is not rare. The point is "
                    "about where on the scale the word applies"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h07",
        "band": "harder",
        "text": "Enamel starts to dissolve below about pH 5.5. A new drink "
                "reads pH 5.8. Does that settle the claim that it is gentle on "
                "teeth?",
        "options": [
            {"text": "Yes — 5.8 is above 5.5, so the drink cannot damage "
                     "enamel",
             "correct": False,
             "why": "The number supports the claim and does not close it. How "
                    "long the drink sits on the teeth matters too"},
            {"text": "No — 5.8 is below 7, so the drink is acidic and will "
                     "dissolve enamel",
             "correct": False,
             "why": "Almost everything you drink is below 7. The threshold "
                    "that matters for enamel is 5.5"},
            {"text": "No — the pH supports the claim, but how long the drink "
                     "stays on the teeth also matters",
             "correct": True},
            {"text": "Yes, provided the same reading is obtained by a pH "
                     "meter as well",
             "correct": False,
             "why": "A better instrument gives a better number, and the "
                    "number was never the whole question"},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h08",
        "band": "harder",
        "text": "Litmus flips between two colours and universal indicator "
                "changes gradually all the way along. Why does mixing dyes "
                "produce that difference?",
        "options": [
            {"text": "Because a mixture of dyes is more concentrated, so its "
                     "colour is deeper at every point on the scale and more "
                     "shades can be told apart by eye",
             "correct": False,
             "why": "Concentration changes how deep a colour is, not how many "
                    "different colours appear. Each dye flips at its own "
                    "point"},
            {"text": "Because the dyes react with each other as the pH "
                     "changes",
             "correct": False,
             "why": "They do not react together. Each one simply responds to "
                    "the solution it is sitting in"},
            {"text": "Because universal indicator is measured by a meter "
                     "rather than by eye",
             "correct": False,
             "why": "It is matched against a chart by eye. That is why a "
                    "meter is preferred where the number matters"},
            {"text": "Because each dye in the mixture changes at a different "
                     "point, so between them they change all along",
             "correct": True},
        ],
        "figure": None,
    },
]
