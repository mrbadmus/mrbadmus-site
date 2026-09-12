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

    # ── MRB-338 expansion ───────────
    {
        "id": "c6-02-e09",
        "band": "easier",
        "text": "What is an indicator?",
        "options": [
            {"text": "A dye whose colour depends on how acidic a solution is", "correct": True},
            {"text": "A chemical that neutralises an acid and makes it safe", "correct": False,
             "why": "An indicator reports on a solution. It changes nothing about "
                    "how the solution behaves."},
            {"text": "A powder that dissolves only in alkalis", "correct": False,
             "why": "Indicators are used in solution and work on both sides of the "
                    "scale."},
            {"text": "An instrument that measures pH electrically", "correct": False,
             "why": "That describes a pH meter. An indicator is a dye, with no "
                    "electrical part at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e10",
        "band": "easier",
        "text": "Litmus is not manufactured. Which living things is it squeezed out "
                "of?",
        "options": [
            {"text": "Seaweeds", "correct": False,
             "why": "Seaweeds are coloured, but litmus is taken from a different "
                    "group of organisms."},
            {"text": "Lichens", "correct": True},
            {"text": "Mosses", "correct": False,
             "why": "Mosses grow in the same damp places, but the dye is not taken "
                    "from them. Litmus comes from the crusty growths on walls and "
                    "gravestones."},
            {"text": "Bacteria", "correct": False,
             "why": "Litmus was in use for centuries before anyone could grow "
                    "bacteria on purpose."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e11",
        "band": "easier",
        "text": "A solution reads pH 5. Which band of the scale is that?",
        "options": [
            {"text": "Strongly acidic", "correct": False,
             "why": "Strongly acidic is 0 to 2. A reading of 5 is much closer to "
                    "neutral than that."},
            {"text": "Weakly alkaline", "correct": False,
             "why": "Anything below 7 is acidic. A reading of 5 is on the acid side,"
                    " not the alkaline one."},
            {"text": "Neutral", "correct": False,
             "why": "Neutral is 7 and only 7. Two whole steps below it is a hundred "
                    "times more acidic."},
            {"text": "Weakly acidic", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e12",
        "band": "easier",
        "text": "Which range of pH values is described as strongly acidic?",
        "options": [
            {"text": "0 to 2", "correct": True},
            {"text": "3 up to 6", "correct": False,
             "why": "That range is weakly acidic. The strong end of the scale stops "
                    "well short of 6."},
            {"text": "0 up to 6", "correct": False,
             "why": "The acid half is split in two, and a reading of 5 behaves "
                    "nothing like a reading of 0."},
            {"text": "11 to 14", "correct": False,
             "why": "That is the strongly alkaline end. It is as far from neutral as"
                    " the acids, in the other direction."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e13",
        "band": "easier",
        "text": "How does a pH meter produce its number?",
        "options": [
            {"text": "It weighs the solution and works the pH out from the mass", "correct": False,
             "why": "Acidic and alkaline solutions of the same strength weigh almost"
                    " exactly the same."},
            {"text": "It photographs the colour of the solution and matches it to a "
                      "chart", "correct": False,
             "why": "A meter needs no colour at all, which is exactly why it works "
                    "on a colourless liquid."},
            {"text": "It measures a voltage across a thin glass bulb dipped in the "
                      "solution", "correct": True},
            {"text": "It counts the bubbles given off when the probe goes in", "correct": False,
             "why": "Nothing fizzes. A meter can be put into pure water and will "
                    "read 7 with no reaction at all."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e14",
        "band": "easier",
        "text": "What colour is universal indicator at pH 7?",
        "options": [
            {"text": "Bright red", "correct": False,
             "why": "Red is the far acid end of the chart, around 0 to 1, not the "
                    "middle of it."},
            {"text": "Green", "correct": True},
            {"text": "Purple", "correct": False,
             "why": "Purple is the far alkaline end, around 13 and 14. The middle of"
                    " the chart is nothing like it."},
            {"text": "Colourless", "correct": False,
             "why": "The dye always has a colour. At 7 it sits in the middle of its "
                    "range rather than disappearing."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e15",
        "band": "easier",
        "text": "A bottle of distilled water is left open on the bench all afternoon."
                " What happens to its reading?",
        "options": [
            {"text": "It climbs towards 8", "correct": False,
             "why": "It moves the other way. What dissolves out of the air is "
                    "acidic, not alkaline."},
            {"text": "It stays at exactly 7", "correct": False,
             "why": "Gas from the air dissolves in without anyone adding it, and "
                    "that is enough to move the reading."},
            {"text": "It drifts down towards 6", "correct": True},
            {"text": "It falls to about 2", "correct": False,
             "why": "The drift is slight. Nothing in ordinary air can drive water "
                    "anywhere near the strong acid end."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e16",
        "band": "easier",
        "text": "Red cabbage water, beetroot juice and blackberry juice all change "
                "colour in acid. What are they acting as?",
        "options": [
            {"text": "Neutralisers", "correct": False,
             "why": "They report on the acid without reacting it away. A drop of dye"
                    " changes nothing about the beaker."},
            {"text": "Catalysts", "correct": False,
             "why": "Nothing is being sped up. The colour is a reading, not a change"
                    " to the reaction."},
            {"text": "Solvents", "correct": False,
             "why": "The acid is already dissolved in water. The juice is there to "
                    "be looked at, not to dissolve anything."},
            {"text": "Indicators", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e17",
        "band": "easier",
        "text": "Which of these would give a reading closest to pH 0?",
        "options": [
            {"text": "Battery acid", "correct": True},
            {"text": "Clean rainwater", "correct": False,
             "why": "Clean rainwater reads about 6 — on the acid side, but only "
                    "just."},
            {"text": "Baking soda solution", "correct": False,
             "why": "That is a mild alkali at about 9, on the other side of neutral "
                    "altogether."},
            {"text": "Distilled water", "correct": False,
             "why": "Sealed distilled water is the definition of neutral, at exactly"
                    " 7."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e18",
        "band": "easier",
        "text": "Why is universal indicator called universal?",
        "options": [
            {"text": "Because it can be used on solids as well as solutions", "correct": False,
             "why": "Like every indicator it needs the substance in solution. A dry "
                    "powder changes nothing."},
            {"text": "Because it changes all the way along the scale rather than at "
                      "one point", "correct": True},
            {"text": "Because every laboratory keeps a bottle of it", "correct": False,
             "why": "The name describes what the dye does, not how widely it happens"
                    " to be stocked."},
            {"text": "Because it works on every liquid, even a dry one", "correct": False,
             "why": "pH is a property of a water-based solution. There is nothing "
                    "for the dye to report in a dry liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e19",
        "band": "easier",
        "text": "Why is an indicator strip never dipped straight into the stock "
                "bottle of a solution?",
        "options": [
            {"text": "Because the strip would soak up too much of the liquid", "correct": False,
             "why": "A strip takes a drop. The objection is what it leaves behind, "
                    "not what it takes away."},
            {"text": "Because the dye only works on a warmed sample", "correct": False,
             "why": "Indicators work perfectly well at room temperature. Nothing "
                    "needs heating."},
            {"text": "Because it contaminates whatever is left in the bottle", "correct": True},
            {"text": "Because a reading taken inside a bottle always reads low", "correct": False,
             "why": "The container does not change the pH. The same solution reads "
                    "the same wherever it is."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e20",
        "band": "easier",
        "text": "What colour is universal indicator in a strongly alkaline solution?",
        "options": [
            {"text": "Dark orange", "correct": False,
             "why": "Orange sits on the acid side, a little way below neutral, not "
                    "at the alkaline end."},
            {"text": "Pale yellow", "correct": False,
             "why": "The chart runs through green and blue above 7. Yellow is on the"
                    " acid side of it."},
            {"text": "Bright red", "correct": False,
             "why": "If both ends were the same colour the chart would be useless. "
                    "Red is the acid end only."},
            {"text": "Purple", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e21",
        "band": "easier",
        "text": "A soil-testing kit holds a small bottle of liquid and a printed "
                "colour card. What is the card for?",
        "options": [
            {"text": "Matching the colour against it to read a pH number off", "correct": True},
            {"text": "Colouring the sample so the change is easier to see", "correct": False,
             "why": "The card is never put in the sample. The dye in the bottle does"
                    " all the colouring."},
            {"text": "Wiping the tester clean between one sample and the next", "correct": False,
             "why": "A card is not a cloth. It carries the scale the reading is "
                    "matched against."},
            {"text": "Recording the results of each test in ink", "correct": False,
             "why": "It is a reference rather than a record sheet, and it is used "
                    "before anything is written down."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e22",
        "band": "easier",
        "text": "Which of these turns litmus blue?",
        "options": [
            {"text": "Lemon juice squeezed from the fruit", "correct": False,
             "why": "Lemon juice reads about 2, and litmus goes red in it."},
            {"text": "Baking soda stirred into water", "correct": True},
            {"text": "Vinegar poured straight from a bottle", "correct": False,
             "why": "Vinegar is an acid at about 3, so litmus comes out red rather "
                    "than blue."},
            {"text": "Distilled water kept sealed in a bottle", "correct": False,
             "why": "Neutral water leaves litmus alone. Only an alkali turns it "
                    "blue."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e23",
        "band": "easier",
        "text": "Of battery acid, lemon juice and rainwater, which is the least "
                "acidic?",
        "options": [
            {"text": "Battery acid", "correct": False,
             "why": "It is the most acidic of the three, at about 0. Thickness has "
                    "nothing to do with pH."},
            {"text": "Lemon juice", "correct": False,
             "why": "Lemon juice reads about 2, which is well down the acid half of "
                    "the scale."},
            {"text": "Rainwater", "correct": True},
            {"text": "All three equally", "correct": False,
             "why": "Below 7 covers an enormous range. There are six whole steps "
                    "between battery acid and rainwater."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e24",
        "band": "easier",
        "text": "Why does a chemist who cannot tell green from yellow-green use a pH "
                "meter?",
        "options": [
            {"text": "Because a meter reports a number instead of a colour to be "
                      "judged", "correct": True},
            {"text": "Because universal indicator shows no colour at all to some "
                      "people", "correct": False,
             "why": "The dye is coloured for everybody. The difficulty is telling "
                    "two of its colours apart."},
            {"text": "Because a meter measures a different property altogether", "correct": False,
             "why": "Both report the same pH. What differs is how the answer is "
                    "presented."},
            {"text": "Because colour charts are banned from laboratories", "correct": False,
             "why": "Charts are still in daily use. The meter is chosen because it "
                    "suits the person using it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e25",
        "band": "easier",
        "text": "Universal indicator added to a sample turns orange. What is the "
                "sample?",
        "options": [
            {"text": "Alkaline", "correct": False,
             "why": "Orange is below green. The chart runs red and orange for acids "
                    "and blue and purple for alkalis."},
            {"text": "Neutral", "correct": False,
             "why": "Close is not the same. Orange is several whole steps below "
                    "neutral, which is a large difference."},
            {"text": "Acidic", "correct": True},
            {"text": "Impossible to say", "correct": False,
             "why": "Orange is one of the chart's own colours, in the lower half of "
                    "the acid range."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e26",
        "band": "easier",
        "text": "Litmus has turned blue in a beaker. What still cannot be said about "
                "the solution?",
        "options": [
            {"text": "Whether it is alkaline at all", "correct": False,
             "why": "Blue is exactly what litmus says for an alkali, so that much is"
                    " settled."},
            {"text": "Whether it contains any water", "correct": False,
             "why": "Litmus only works in solution, so the presence of water is "
                    "already established."},
            {"text": "Whether the beaker holds a liquid", "correct": False,
             "why": "The test was carried out in solution, so this is not the "
                    "question left open."},
            {"text": "How far above 7 it is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s09",
        "band": "standard",
        "text": "A student presses universal indicator paper against a dry white "
                "powder and nothing happens. What is the flaw?",
        "options": [
            {"text": "The paper has to be warmed before it will respond to anything "
                      "at all", "correct": False,
             "why": "Indicator paper works cold. Heating it would only damage the "
                    "dye on it."},
            {"text": "Indicator paper only works on alkalis, so an acidic powder "
                      "shows nothing", "correct": False,
             "why": "It reports both sides of the scale. That is not what has gone "
                    "wrong here."},
            {"text": "The powder has to be dissolved in water before there is a pH to"
                      " read", "correct": True},
            {"text": "The paper must be pressed harder, since a dry contact does not "
                      "transfer the substance", "correct": False,
             "why": "No amount of pressure helps. Without water there is nothing for"
                    " the dye to respond to."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s10",
        "band": "standard",
        "text": "Universal indicator is a mixture of dyes. Explain why a mixture "
                "gives a gradual change when one dye would not.",
        "options": [
            {"text": "Each dye in the mixture changes at a different point, so the "
                      "blend shifts colour all along the scale", "correct": True},
            {"text": "The dyes react with one another, and the product of that "
                      "reaction is what carries the colour", "correct": False,
             "why": "The dyes do not react together. Each one responds to the "
                    "solution on its own."},
            {"text": "A mixture is more concentrated than a single dye, so its colour"
                      " shows up over a wider range", "correct": False,
             "why": "Concentration changes how strong the colour looks, not the pH "
                    "at which it changes."},
            {"text": "The dyes cancel each other out except at one pH, which is the "
                      "one the chart reports", "correct": False,
             "why": "If only one pH showed a colour the indicator would report a "
                    "single point, like litmus."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s11",
        "band": "standard",
        "text": "Battery acid reads 0 and oven cleaner reads 13. Which is further "
                "from neutral, and by how much?",
        "options": [
            {"text": "Oven cleaner, by six steps against the battery acid's seven "
                      "steps", "correct": False,
             "why": "Seven is the larger number of steps, and that is the battery "
                    "acid's distance rather than the cleaner's."},
            {"text": "Battery acid, by seven steps against the oven cleaner's six", "correct": True},
            {"text": "Neither, because both sit at the far end of the scale", "correct": False,
             "why": "The scale runs 0 to 14 with neutral at 7, so the two ends are "
                    "not the same distance from it."},
            {"text": "Oven cleaner, because 13 is a bigger number than 0", "correct": False,
             "why": "Distance is measured from 7, not from zero, so the bigger "
                    "number is not automatically the further out."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s12",
        "band": "standard",
        "text": "Two beakers both turn universal indicator green. One holds pure "
                "water and one holds salt solution. What does the reading settle?",
        "options": [
            {"text": "That both beakers hold pure water, since only water reads "
                      "exactly 7 on the chart", "correct": False,
             "why": "Plenty of dissolved substances leave a solution neutral. The "
                    "reading cannot pick water out."},
            {"text": "That neither beaker holds anything dissolved at all", "correct": False,
             "why": "Salt is dissolved in one of them and the reading is still 7, "
                    "which disproves that rule."},
            {"text": "That both are neutral, and nothing about what is dissolved in "
                      "them", "correct": True},
            {"text": "That the two beakers hold the same substance", "correct": False,
             "why": "A pH reading is one measurement. Two different solutions can "
                    "easily share it."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s13",
        "band": "standard",
        "text": "A soil-testing kit says to shake the soil with distilled water "
                "rather than tap water. Why does that matter?",
        "options": [
            {"text": "Tap water carries dissolved substances and a pH of its own, "
                      "which would shift the reading", "correct": True},
            {"text": "Tap water contains chlorine, which destroys the dye", "correct": False,
             "why": "The dye still works. The objection is that tap water brings its"
                    " own pH to the test."},
            {"text": "Tap water is too warm, and a warm sample always reads low", "correct": False,
             "why": "Temperature is not the issue here, and the sample is not read "
                    "straight from the tap."},
            {"text": "Tap water will not dissolve anything out of soil at all", "correct": False,
             "why": "It dissolves the same substances distilled water would. It "
                    "simply adds some of its own."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s14",
        "band": "standard",
        "text": "Why does the pH scale report a number rather than leaving the result"
                " as a colour?",
        "options": [
            {"text": "Because a colour fades within minutes while a number written "
                      "down does not", "correct": False,
             "why": "Fading is a practical nuisance. The real gain is that a number "
                    "does not depend on who is looking."},
            {"text": "Because two people can disagree about a colour and cannot "
                      "disagree about a number", "correct": True},
            {"text": "Because a colour is a physical property and a number is a "
                      "chemical one, which is what is wanted", "correct": False,
             "why": "The number is simply a way of reporting the same thing the "
                    "colour showed."},
            {"text": "Because colours cannot be compared between one laboratory and "
                      "the next under different lamps", "correct": False,
             "why": "True as far as it goes, but two people at the same bench under "
                    "one lamp can still disagree."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s15",
        "band": "standard",
        "text": "Oven cleaner is tested by spraying a little into a beaker rather "
                "than by dipping a strip into the can. Why?",
        "options": [
            {"text": "Because the can is under pressure and a strip pushed into it "
                      "would release the whole contents at once", "correct": False,
             "why": "The reason is not the pressure. It is keeping the stock clean "
                    "and keeping the corrosive product off you."},
            {"text": "Because a reading taken inside the can comes out too high", "correct": False,
             "why": "The container does not change the pH. The same cleaner reads "
                    "the same in a beaker."},
            {"text": "Because the dye needs air, and a sealed can has none", "correct": False,
             "why": "Indicators do not need air. They need the solution, and a few "
                    "drops of it is plenty."},
            {"text": "Because it keeps the stock uncontaminated and keeps a corrosive"
                      " alkali off your hands", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s16",
        "band": "standard",
        "text": "A pH meter that has not been checked against a known solution for "
                "months is used for an important reading. What is the risk?",
        "options": [
            {"text": "It will refuse to give any reading at all until it has been "
                      "checked", "correct": False,
             "why": "It reads perfectly happily. That is precisely the danger."},
            {"text": "Its reading will drift, so it gives a confident number that is "
                      "wrong", "correct": True},
            {"text": "It will report the reading as a colour instead of a number "
                      "until it is reset", "correct": False,
             "why": "A meter has no colour output. What it loses over time is "
                    "accuracy, not its display."},
            {"text": "It will only work on acids, since the alkaline half of its "
                      "range is the first to fail", "correct": False,
             "why": "There is no such split. Drift affects the whole range at once."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s17",
        "band": "standard",
        "text": "A solution reading pH 11 is diluted with an equal volume of pure "
                "water. Predict which way the reading moves.",
        "options": [
            {"text": "Up, away from 7", "correct": False,
             "why": "Spreading it out makes it less alkaline, not more. The reading "
                    "falls towards neutral."},
            {"text": "It stays at 11", "correct": False,
             "why": "The kind of substance is unchanged, but pH reports how the "
                    "solution behaves, and that has changed."},
            {"text": "Down past 7 into the acid half", "correct": False,
             "why": "Water on its own cannot push an alkali across neutral. It can "
                    "only move the reading towards 7."},
            {"text": "Down, towards 7", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s18",
        "band": "standard",
        "text": "What is actually happening to an indicator molecule when the colour "
                "changes?",
        "options": [
            {"text": "It changes shape depending on the acid around it, and a "
                      "different shape reflects a different colour", "correct": True},
            {"text": "It breaks apart completely, and the fragments happen to be a "
                      "different colour from the whole", "correct": False,
             "why": "The change reverses when the solution changes back, which a "
                    "broken molecule could not do."},
            {"text": "It is used up by the acid, and the colour that remains belongs "
                      "to whatever is left over", "correct": False,
             "why": "The dye is not consumed. A drop reports the beaker for as long "
                    "as you care to look."},
            {"text": "It heats up slightly, and the warmth is what shifts the colour "
                      "it reflects", "correct": False,
             "why": "There is no measurable warming, and cooling the beaker does not"
                    " change the reading."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s19",
        "band": "standard",
        "text": "A pH has to be recorded to two decimal places for a legal report. "
                "Which method is used, and why?",
        "options": [
            {"text": "Litmus, because a colour is the most direct evidence there is "
                      "and needs no instrument", "correct": False,
             "why": "Litmus gives one of two colours. It cannot supply even one "
                    "decimal place."},
            {"text": "A meter, because a colour chart cannot be read that finely", "correct": True},
            {"text": "Universal indicator, because its chart shows decimals", "correct": False,
             "why": "The chart is printed in whole numbers, which is as fine as a "
                    "colour match can be."},
            {"text": "Either, because both report the same pH anyway", "correct": False,
             "why": "They report the same quantity to very different precision, and "
                    "here the precision is the whole point."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s20",
        "band": "standard",
        "text": "A student wants to compare how much acid is in vinegar and in lemon "
                "juice. No indicator can answer it. What would?",
        "options": [
            {"text": "Weighing equal volumes of each and comparing the two masses on "
                      "a balance", "correct": False,
             "why": "Both are mostly water and weigh almost the same. The balance "
                    "cannot separate them."},
            {"text": "Measuring how much alkali each one takes to neutralise", "correct": True},
            {"text": "Boiling equal volumes and timing how long each takes", "correct": False,
             "why": "That compares the water in them rather than the acid dissolved "
                    "in it."},
            {"text": "Testing both with a meter and taking the lower reading", "correct": False,
             "why": "A meter reports how acidic each is, which is the same question "
                    "an indicator answers."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s21",
        "band": "standard",
        "text": "Universal indicator is added to a glass of blackcurrant squash. What"
                " makes the result hard to use?",
        "options": [
            {"text": "The squash is too thick for the dye to spread through it evenly", "correct": False,
             "why": "It spreads readily enough. The trouble is seeing the result "
                    "once it has."},
            {"text": "The squash is already strongly coloured, so the dye's own "
                      "colour cannot be judged", "correct": True},
            {"text": "The sugar in the squash reacts with the dye and destroys it "
                      "before a reading can be taken", "correct": False,
             "why": "Sugar does not attack the dye. What defeats the test is the "
                    "colour already in the glass."},
            {"text": "Squash has no pH at all, because it is a mixture rather than a "
                      "single substance", "correct": False,
             "why": "Every water-based solution has a pH, mixtures very much "
                    "included."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s22",
        "band": "standard",
        "text": "The same pond sample is tested twice, once with litmus and once with"
                " universal indicator. Which pair of results could both be right?",
        "options": [
            {"text": "Litmus red, universal indicator pH 9", "correct": False,
             "why": "Red means acidic, and 9 is alkaline. The two reports contradict"
                    " each other."},
            {"text": "Litmus blue, universal indicator pH 4", "correct": False,
             "why": "Blue means alkaline, and 4 is acidic. Only one of the two can "
                    "be describing this sample."},
            {"text": "Litmus blue, universal indicator pH 8", "correct": True},
            {"text": "Litmus red, universal indicator pH 7", "correct": False,
             "why": "A reading of exactly 7 is neutral, and litmus does not go red "
                    "in a neutral solution."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h09",
        "band": "harder",
        "text": "Explain why a scale that squashes an enormous range of acidity into "
                "fifteen whole numbers is useful rather than clumsy.",
        "options": [
            {"text": "Because the acidity of real solutions varies over an enormous "
                      "range, and fifteen steps make it writable", "correct": True},
            {"text": "Because fifteen is the number of different colours a mixture of"
                      " dyes is able to show at once", "correct": False,
             "why": "The scale was not designed around a dye. The dye was matched to"
                    " the scale afterwards."},
            {"text": "Because every solution that exists sits somewhere between 0 and"
                      " 14, with nothing beyond either end", "correct": False,
             "why": "Readings outside the range are possible. The scale is useful "
                    "because it covers the ordinary cases."},
            {"text": "Because whole numbers are easier for pupils to learn than the "
                      "decimals a meter reports", "correct": False,
             "why": "Meters report decimals on this same scale. Ease of learning is "
                    "not what the scale was built for."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h10",
        "band": "harder",
        "text": "Universal indicator reports a sample as green while a meter reports "
                "7.4. Which should be trusted, and why?",
        "options": [
            {"text": "The indicator, because a colour comes straight from the "
                      "solution and a meter is only an instrument", "correct": False,
             "why": "Both come from the solution. The meter simply resolves it far "
                    "more finely."},
            {"text": "The meter, because a colour match cannot separate 7.0 from 7.4", "correct": True},
            {"text": "Neither, because the two disagree and both may be wrong", "correct": False,
             "why": "They do not disagree. Green covers 7.4, so the two results are "
                    "consistent and one is sharper."},
            {"text": "The indicator, because a decimal cannot be right on a whole-"
                      "number scale", "correct": False,
             "why": "The whole numbers are the chart's limit, not the scale's. Real "
                    "values fall between them."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h11",
        "band": "harder",
        "text": "A pond keeper has used a colour chart for a year, then buys a meter "
                "and finds readings a whole unit different. Suggest the most likely "
                "explanation.",
        "options": [
            {"text": "The pond changed on the day the meter arrived, which is why the"
                      " two methods never agreed", "correct": False,
             "why": "A coincidence of that kind explains nothing. The methods "
                    "themselves are the place to look."},
            {"text": "A meter and a chart measure two different properties, so their "
                      "numbers were never meant to match", "correct": False,
             "why": "Both report pH. If they disagree, one of them is being used "
                    "badly."},
            {"text": "The chart readings were judgements of colour by eye, and the "
                      "meter may not have been checked", "correct": True},
            {"text": "Meters always read a unit higher than charts, so the difference"
                      " is built into the instrument", "correct": False,
             "why": "There is no fixed offset. A properly checked meter and a "
                    "careful chart reading agree."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h12",
        "band": "harder",
        "text": "Litmus was in use for centuries before anyone could put a number on "
                "acidity. What does that show?",
        "options": [
            {"text": "That acidity did not exist as a property until the scale was "
                      "invented to describe it", "correct": False,
             "why": "The property was there all along. What arrived late was a way "
                    "of measuring it."},
            {"text": "That early chemists had no way of telling an acid from an "
                      "alkali before the scale existed", "correct": False,
             "why": "Litmus told them exactly that, which is why it stayed in use "
                    "for so long."},
            {"text": "That a colour change is a more reliable result than a number, "
                      "since it came first", "correct": False,
             "why": "Coming first says nothing about reliability. The number carries"
                    " much more information."},
            {"text": "That you can observe which side of neutral something is long "
                      "before you can measure how far", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h13",
        "band": "harder",
        "text": "An acid at pH 3 is diluted tenfold and reads 4. Predict the reading "
                "after another tenfold dilution, and say when the prediction stops "
                "working.",
        "options": [
            {"text": "5, and the prediction stops working as the reading approaches "
                      "7, which water cannot push it past", "correct": True},
            {"text": "5, and the prediction keeps working for ever, so enough water "
                      "would take the reading to 14", "correct": False,
             "why": "Adding water can never make a solution alkaline. The reading "
                    "closes on 7 and stops."},
            {"text": "40, because a tenfold dilution multiplies the reading on the "
                      "scale by ten each time", "correct": False,
             "why": "Each tenfold dilution adds one to the reading. It does not "
                    "multiply it."},
            {"text": "3.1, because a second dilution has far less effect than the "
                      "first one did", "correct": False,
             "why": "Each tenfold step is worth the same one unit, whether it is the"
                    " first or the tenth."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h14",
        "band": "harder",
        "text": "Compare litmus and universal indicator as instruments: what does "
                "each one buy, and what does each one cost?",
        "options": [
            {"text": "Litmus buys a number and costs speed, while universal indicator"
                      " buys speed and costs detail", "correct": False,
             "why": "This has the two exactly the wrong way round. Litmus is the "
                    "fast one with no number."},
            {"text": "Litmus buys speed and costs detail, while universal indicator "
                      "buys a number and costs time", "correct": True},
            {"text": "Litmus buys accuracy and costs nothing, while universal "
                      "indicator costs it", "correct": False,
             "why": "Litmus is the less informative of the two. It cannot be the "
                    "more accurate."},
            {"text": "Both buy the same information, and only the price differs", "correct": False,
             "why": "One reports a side and the other a number. That is a real "
                    "difference in what you learn."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h15",
        "band": "harder",
        "text": "A student argues that because universal indicator is a mixture it "
                "must be less accurate than a single pure dye. Evaluate that.",
        "options": [
            {"text": "Correct, because a mixture always gives a muddier colour than "
                      "any one of its parts on its own", "correct": False,
             "why": "The blend is chosen so that each colour is distinct. Muddiness "
                    "is not the problem here."},
            {"text": "Correct, because impurities in a mixture shift every reading it"
                      " gives by the same amount", "correct": False,
             "why": "The other dyes are not impurities. They are the working parts "
                    "of the instrument."},
            {"text": "Wrong, because the mixture is what lets it report all along the"
                      " scale rather than at one point", "correct": True},
            {"text": "Wrong, because a pure dye cannot change colour at all unless "
                      "something is mixed in with it", "correct": False,
             "why": "A single dye changes colour perfectly well. It just does so "
                    "over one narrow part of the scale."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h16",
        "band": "harder",
        "text": "Explain what a pH reading is a property of, and why that makes an "
                "indicator useless on a dry crystal.",
        "options": [
            {"text": "It is a property of the crystal itself, so the crystal has to "
                      "be crushed before a reading can be taken", "correct": False,
             "why": "Crushing changes nothing. What is missing is water, not surface"
                    " area."},
            {"text": "It is a property of the dye, so a fresh bottle of indicator is "
                      "needed for every solid tested", "correct": False,
             "why": "The dye reports; it is not the thing being measured. Its own pH"
                    " is beside the point."},
            {"text": "It is a property of a solution, so there is nothing to read "
                      "until the substance has dissolved", "correct": True},
            {"text": "It is a property of the container, so a reading can only be "
                      "taken in a glass beaker", "correct": False,
             "why": "The same solution reads the same in glass or plastic. The "
                    "container plays no part."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h17",
        "band": "harder",
        "text": "Two meters give 6.8 and 7.1 for the same sample. What is the best "
                "next step?",
        "options": [
            {"text": "Take the average of the two and report 6.95 as the measurement", "correct": False,
             "why": "Averaging a good reading with a bad one buries the problem "
                    "instead of finding it."},
            {"text": "Report both and let whoever reads the result decide which they "
                      "prefer", "correct": False,
             "why": "That hands the problem on. The disagreement can be settled at "
                    "the bench."},
            {"text": "Discard the lower one, since a reading below 7 is the less "
                      "likely of the two", "correct": False,
             "why": "Nothing makes one side of neutral more likely. There is no "
                    "reason to prefer either reading."},
            {"text": "Check both against a solution of known pH before trusting "
                      "either", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h18",
        "band": "harder",
        "text": "A soil pH is reported as 6.5 from a colour chart printed in whole "
                "numbers. Evaluate that report.",
        "options": [
            {"text": "Sound, because a colour halfway between two printed patches "
                      "genuinely means halfway between the numbers", "correct": False,
             "why": "Judging a colour as exactly halfway is the very thing eyes are "
                    "unreliable at."},
            {"text": "Unsound, because the method cannot resolve half a unit, so the "
                      "report claims more precision than it has", "correct": True},
            {"text": "Unsound, because soil has no single pH and a reading from it "
                      "can never be reported at all", "correct": False,
             "why": "A sample shaken with distilled water gives a perfectly usable "
                    "reading. The problem is the decimal."},
            {"text": "Sound, because the chart is only a guide and any value between "
                      "its numbers may be quoted freely", "correct": False,
             "why": "A value quoted more finely than the method allows is a claim "
                    "the measurement does not support."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h19",
        "band": "harder",
        "text": "One student tests lake water with litmus and reports acidic; another"
                " uses a meter and reports 6.8. Are the two reports consistent?",
        "options": [
            {"text": "No, because 6.8 rounds to 7 and a neutral sample would leave "
                      "litmus unchanged", "correct": False,
             "why": "Rounding is not what the litmus responds to. The sample really "
                    "is below 7."},
            {"text": "No, because litmus and a meter measure different things", "correct": False,
             "why": "Both report where the sample sits relative to neutral, so they "
                    "can certainly be compared."},
            {"text": "Yes, because 6.8 is below 7, which is exactly what litmus going"
                      " red reports", "correct": True},
            {"text": "Yes, because litmus is unreliable and any reading will agree", "correct": False,
             "why": "Agreement has to be earned by the numbers. Litmus is limited "
                    "rather than unreliable."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e27",
        "band": "easier",
        "text": "Litmus is added to a sample and its colour does not change at all."
                " What does that suggest about the sample?",
        "options": [
            {"text": "It is strongly acidic", "correct": False,
             "why": "An acid turns litmus red, which is a change anyone can see."},
            {"text": "It is neutral", "correct": True},
            {"text": "It is strongly alkaline", "correct": False,
             "why": "An alkali turns litmus blue, so a strong one would change it "
                    "plainly."},
            {"text": "It is too dilute for litmus to work", "correct": False,
             "why": "Litmus responds to very dilute acids and alkalis perfectly "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e28",
        "band": "easier",
        "text": "Sodium hydrogencarbonate is stirred into water on the testing bench."
                " What is that substance usually called in a kitchen?",
        "options": [
            {"text": "Table salt", "correct": False,
             "why": "Table salt is sodium chloride, and its solution reads "
                    "neutral rather than alkaline."},
            {"text": "Caustic soda", "correct": False,
             "why": "Caustic soda is sodium hydroxide, a strong alkali that is "
                    "nowhere near mild enough to eat."},
            {"text": "Baking soda", "correct": True},
            {"text": "Washing-up liquid", "correct": False,
             "why": "Washing-up liquid is a mixture sold as a liquid, not a "
                    "single named solid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e29",
        "band": "easier",
        "text": "Rainwater is collected cleanly, in the open and well away from any"
                " road. What does it read?",
        "options": [
            {"text": "About pH 6", "correct": True},
            {"text": "About pH 2, the same as lemon juice", "correct": False,
             "why": "Rain is only slightly acidic; pH 2 is the sharply acidic end "
                    "of the scale."},
            {"text": "Exactly pH 7, because it has fallen from the sky",
             "correct": False,
             "why": "Falling through air is what makes it slightly acidic rather "
                    "than neutral."},
            {"text": "About pH 9, because it washes dust out of the air",
             "correct": False,
             "why": "Clean rain is on the acid side of 7, not the alkaline side."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e30",
        "band": "easier",
        "text": "A pH meter has just been used on one sample and is about to be used on"
                " the next. What should be done to the probe first?",
        "options": [
            {"text": "Warm it gently over a flame", "correct": False,
             "why": "Heating the glass bulb would damage the probe and change "
                    "nothing about the next reading."},
            {"text": "Wipe it on a dry paper towel and nothing more",
             "correct": False,
             "why": "Wiping leaves traces behind, and the bulb should not be "
                    "rubbed dry."},
            {"text": "Leave it exactly as it is, to save time", "correct": False,
             "why": "Liquid carried over from the last sample would shift the "
                    "next reading."},
            {"text": "Rinse it with distilled water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e31",
        "band": "easier",
        "text": "Litmus turns red in a sample. Which of these could the sample's pH be?",
        "options": [
            {"text": "pH 4", "correct": True},
            {"text": "pH 7", "correct": False,
             "why": "A neutral sample leaves litmus as it was rather than turning "
                    "it red."},
            {"text": "pH 9", "correct": False,
             "why": "Anything above 7 is alkaline and turns litmus blue."},
            {"text": "pH 12", "correct": False,
             "why": "That is strongly alkaline, which is the far end from red "
                    "litmus."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-e32",
        "band": "easier",
        "text": "The printed pH scale is drawn as a row of coloured cells, one for each"
                " whole number. How many cells are there?",
        "options": [
            {"text": "Ten", "correct": False,
             "why": "Ten would leave the scale ending at 9, with the alkaline end "
                    "cut off."},
            {"text": "Fourteen", "correct": False,
             "why": "That forgets the cell for 0, which is where the strongest "
                    "acids sit."},
            {"text": "Fifteen", "correct": True},
            {"text": "Seven", "correct": False,
             "why": "Seven is the neutral point in the middle, not the number of "
                    "cells."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s23",
        "band": "standard",
        "text": "The colours of universal indicator always appear in the same order,"
                " from red at one end to purple at the other. Explain why that order"
                " matters.",
        "options": [
            {"text": "Because it makes the colours pleasant to look at on a chart",
             "correct": False,
             "why": "The chart is an instrument rather than a decoration, and "
                    "appearance is not what it is for."},
            {"text": "Because a fixed order lets a colour be read as a position on "
                      "the scale", "correct": True},
            {"text": "Because the dye would stop working if the order were "
                      "different", "correct": False,
             "why": "The order is a consequence of how the dyes change, not a "
                    "condition for them working."},
            {"text": "Because the order shows how much acid is dissolved in each sample tested", "correct": False,
             "why": "No indicator reports how much acid there is, in any order of "
                    "colours."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s24",
        "band": "standard",
        "text": "Battery acid and clean rainwater both turn litmus red. Explain what"
                " that shows about litmus.",
        "options": [
            {"text": "That litmus only ever responds to acids that are very strong indeed",
             "correct": False,
             "why": "It turned red for rainwater too, which is barely acidic at "
                    "all."},
            {"text": "That litmus reports which side of 7 a sample is on and no "
                      "more", "correct": True},
            {"text": "That the two samples are equally acidic as each other",
             "correct": False,
             "why": "They are enormously far apart; litmus simply cannot show "
                    "that."},
            {"text": "That litmus has been contaminated by something and needs replacing",
             "correct": False,
             "why": "Both results are exactly what working litmus gives for an "
                    "acid."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s25",
        "band": "standard",
        "text": "Some toothpastes contain baking soda, which gives a solution at about"
                " pH 9. Explain how that helps teeth.",
        "options": [
            {"text": "It coats the tooth in a layer that acid cannot pass through",
             "correct": False,
             "why": "It acts on the acid itself rather than building a barrier "
                    "over the enamel."},
            {"text": "It works against the acid in the mouth that attacks enamel",
             "correct": True},
            {"text": "It makes the mouth more acidic, which hardens the enamel",
             "correct": False,
             "why": "Acid is what dissolves enamel, so more of it would make "
                    "matters worse."},
            {"text": "It kills the bacteria that make teeth look yellow",
             "correct": False,
             "why": "Colour is a different matter, and pH 9 is not there for "
                    "appearance."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s26",
        "band": "standard",
        "text": "Red cabbage water is added to two liquids. It goes pink in the first"
                " and green in the second. What can be concluded?",
        "options": [
            {"text": "Both are acidic, and one is more acidic than the other",
             "correct": False,
             "why": "Two acids would push the same dye the same way, not to "
                    "opposite colours."},
            {"text": "Nothing, because cabbage water is a food and not an "
                      "indicator", "correct": False,
             "why": "A dye that changes colour with acidity is an indicator, "
                    "whatever it was boiled out of."},
            {"text": "One liquid is acidic and the other is alkaline",
             "correct": True},
            {"text": "Both are neutral, and the colours come from the cabbage "
                      "itself", "correct": False,
             "why": "A neutral liquid would leave the dye at one colour, and here "
                    "it took two."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s27",
        "band": "standard",
        "text": "Two ponds are measured at pH 6 and pH 8. A student says they are"
                " basically the same water. Evaluate.",
        "options": [
            {"text": "Sound, because both readings are one step from neutral",
             "correct": False,
             "why": "Being the same distance from 7 does not put them on the same "
                    "side of it."},
            {"text": "Sound, because neither pond is strongly acidic or alkaline",
             "correct": False,
             "why": "Neither is extreme, and they are still opposite kinds of "
                    "water."},
            {"text": "Unsound, because one pond is acidic and the other is "
                      "alkaline", "correct": True},
            {"text": "Unsound, because pH 8 is a hundred times more alkaline than "
                      "pH 6", "correct": False,
             "why": "Two steps is a hundredfold, but the two readings are on "
                    "opposite sides of neutral rather than both alkaline."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s28",
        "band": "standard",
        "text": "A fish farmer measures the pond every morning rather than once a"
                " season. Explain why.",
        "options": [
            {"text": "Because a pH meter gives a different answer each time it is "
                      "used", "correct": False,
             "why": "A checked meter repeats its readings; it is the pond that "
                    "moves."},
            {"text": "Because the pH drifts, and the fish need it held in a narrow "
                      "range", "correct": True},
            {"text": "Because pond water becomes more acidic every time it is "
                      "tested", "correct": False,
             "why": "Taking a reading does not change the water it was taken "
                    "from."},
            {"text": "Because one reading a season would be cheaper but less "
                      "interesting", "correct": False,
             "why": "The reason is the fish rather than interest; a pond outside "
                    "its range kills them."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s29",
        "band": "standard",
        "text": "A laboratory keeps litmus on the shelf as well as universal"
                " indicator, although universal indicator reports more. Suggest why.",
        "options": [
            {"text": "Because litmus works on solids and universal indicator does "
                      "not", "correct": False,
             "why": "Neither works on a dry solid; both need the substance in "
                    "solution."},
            {"text": "Because litmus lasts for years and universal indicator goes "
                      "off in weeks", "correct": False,
             "why": "Both keep perfectly well, so shelf life is not the reason to "
                    "hold both."},
            {"text": "Because some jobs need only the side of neutral, answered at "
                      "once", "correct": True},
            {"text": "Because universal indicator cannot be used on an alkali at "
                      "all", "correct": False,
             "why": "It reports the alkaline half of the scale as readily as the "
                    "acid half."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s30",
        "band": "standard",
        "text": "A student argues that universal indicator should be used for every"
                " test, because more information is always better. Evaluate.",
        "options": [
            {"text": "Sound, because a number can be used for any decision at all",
             "correct": False,
             "why": "A number that takes longer to read is worse for a decision "
                    "that has to be made at once."},
            {"text": "Unsound, because the right tool is the one that answers the "
                      "question asked", "correct": True},
            {"text": "Sound, because litmus is less reliable than universal "
                      "indicator", "correct": False,
             "why": "Litmus is entirely reliable for the question it answers."},
            {"text": "Unsound, because universal indicator cannot be trusted anywhere near neutral", "correct": False,
             "why": "It reads near neutral perfectly well; matching the colour "
                    "finely is the limit, not trust."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s31",
        "band": "standard",
        "text": "Distilled water is needed as a neutral standard, and the bottle has"
                " been left open on the bench all afternoon. Explain the problem.",
        "options": [
            {"text": "Dust has settled in it, which makes it alkaline",
             "correct": False,
             "why": "It is what dissolves out of the air rather than dust that "
                    "shifts the reading, and it shifts it the other way."},
            {"text": "It has evaporated, so what is left is more concentrated",
             "correct": False,
             "why": "Pure water has nothing dissolved in it to concentrate."},
            {"text": "It has warmed up, so it can no longer be called distilled",
             "correct": False,
             "why": "Warming does not undo distilling, and the trouble is "
                    "chemical rather than thermal."},
            {"text": "It has drifted below 7, so it is no longer neutral",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-s32",
        "band": "standard",
        "text": "The printed chart runs smoothly from red through green to purple"
                " rather than showing five separate blocks of colour. Explain why.",
        "options": [
            {"text": "Because the printing would smudge if blocks were used",
             "correct": False,
             "why": "How the chart is printed is not what decides the colours on "
                    "it."},
            {"text": "Because universal indicator changes gradually rather than in "
                      "jumps", "correct": True},
            {"text": "Because every solution sits between two of the five bands",
             "correct": False,
             "why": "Plenty of solutions sit squarely in a band, and the chart "
                    "still runs smoothly."},
            {"text": "Because a smooth chart is easier to match by eye than blocks "
                      "are", "correct": False,
             "why": "Blocks would be easier to match; the smoothness reports what "
                    "the dye really does."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h20",
        "band": "harder",
        "text": "A fish farmer must hold a pond between pH 6.5 and pH 8. Explain why"
                " litmus cannot do that job at all.",
        "options": [
            {"text": "Because litmus only gives a colour in solutions that are strongly coloured already", "correct": False,
             "why": "It works on colourless solutions, which is most of them."},
            {"text": "Because both ends of the range are close to neutral and "
                      "litmus reports a side", "correct": True},
            {"text": "Because litmus cannot be used on water taken from outdoors",
             "correct": False,
             "why": "Pond water is a solution like any other and litmus responds "
                    "to it."},
            {"text": "Because litmus reports only alkalis, and half the range is "
                      "acidic", "correct": False,
             "why": "Litmus reports acids as red just as it reports alkalis as "
                    "blue."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h21",
        "band": "harder",
        "text": "A deeply coloured blackcurrant drink cannot be tested usefully with"
                " universal indicator. Suggest how its pH could still be found.",
        "options": [
            {"text": "Dilute it with tap water until the colour fades, then add "
                      "indicator", "correct": False,
             "why": "Diluting changes the reading being looked for, and tap water "
                    "brings a pH of its own."},
            {"text": "Use a pH meter, which reports a number rather than a colour",
             "correct": True},
            {"text": "Filter the colour out through filter paper, then add "
                      "indicator", "correct": False,
             "why": "The colour is dissolved, so it runs straight through the "
                    "paper with the drink."},
            {"text": "Use litmus instead, because litmus is unaffected by other "
                      "colours", "correct": False,
             "why": "Litmus is judged by eye as well, so a dark drink hides its "
                    "colour too."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h22",
        "band": "harder",
        "text": "Cuttings from one hydrangea flower blue in one garden and pink in the"
                " next. Suggest what a gardener could do to change the colour of"
                " their own plant.",
        "options": [
            {"text": "Change the pH of the soil the plant is growing in",
             "correct": True},
            {"text": "Water it with a stronger fertiliser every week",
             "correct": False,
             "why": "Feeding a plant changes its growth rather than the colour "
                    "these flowers report."},
            {"text": "Move it into a pot so the roots are held in the same soil",
             "correct": False,
             "why": "Keeping the soil the same is what holds the colour where it "
                    "is."},
            {"text": "Cut it back hard, so the new flowers come out differently",
             "correct": False,
             "why": "Pruning changes when a plant flowers, not the chemistry of "
                    "its ground."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h23",
        "band": "harder",
        "text": "A gardener needs soil pH only to the nearest whole number. Evaluate"
                " the claim that a meter is essential for the job.",
        "options": [
            {"text": "Sound, because a colour chart cannot separate one whole "
                      "number from the next", "correct": False,
             "why": "Whole numbers are exactly what a printed chart can separate."},
            {"text": "Sound, because a meter is more accurate and accuracy is "
                      "always required", "correct": False,
             "why": "Accuracy beyond what a job needs is not a requirement."},
            {"text": "Unsound, because the chart already resolves what this job "
                      "asks for", "correct": True},
            {"text": "Unsound, because a meter cannot be used on soil at all",
             "correct": False,
             "why": "A meter reads a soil sample shaken with water perfectly "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h24",
        "band": "harder",
        "text": "Clean rainwater turns litmus red, and so does battery acid. A student"
                " concludes that rainwater is dangerous. Evaluate.",
        "options": [
            {"text": "Sound, because anything that turns litmus red attacks "
                      "materials", "correct": False,
             "why": "Every acid turns litmus red, including the ones people "
                    "drink."},
            {"text": "Unsound, because litmus reports a side and not how fiercely "
                      "it acts", "correct": True},
            {"text": "Sound, because rainwater and battery acid gave the same "
                      "result", "correct": False,
             "why": "The same result from a tool that reports two outcomes cannot "
                    "make two liquids alike."},
            {"text": "Unsound, because rainwater is alkaline and the litmus was "
                      "faulty", "correct": False,
             "why": "Clean rain really is slightly acidic, so the litmus was "
                    "right."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h25",
        "band": "harder",
        "text": "A student designs a dye that is red below pH 7 and blue above it,"
                " changing in a single step. Evaluate it against universal indicator.",
        "options": [
            {"text": "Better, because one clear step is easier to judge than a "
                      "gradual change", "correct": False,
             "why": "Easier to judge, and it answers a smaller question: no "
                    "number comes out of it."},
            {"text": "Better, because it would report a pH without a printed "
                      "chart", "correct": False,
             "why": "Two colours cannot report fifteen numbers, chart or no "
                    "chart."},
            {"text": "Worse for any job needing a number, because it reports only "
                      "a side", "correct": True},
            {"text": "Worse, because a dye that changes at one point cannot exist",
             "correct": False,
             "why": "Litmus is exactly such a dye and has been used for "
                    "centuries."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h26",
        "band": "harder",
        "text": "A meter is checked against a bottle of known pH rather than against"
                " distilled water. Explain why distilled water is the poorer choice.",
        "options": [
            {"text": "Because distilled water damages the glass bulb on a probe",
             "correct": False,
             "why": "A probe is rinsed in distilled water routinely and comes to "
                    "no harm."},
            {"text": "Because distilled water does not stay at 7 once it is open",
             "correct": True},
            {"text": "Because distilled water has never been at pH 7 in the first "
                      "place", "correct": False,
             "why": "Straight from the still and sealed it is the definition of "
                    "neutral."},
            {"text": "Because a meter cannot be checked at 7, only at the ends of "
                      "the scale", "correct": False,
             "why": "The middle of the scale is a perfectly good place to check a "
                    "meter."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h27",
        "band": "harder",
        "text": "A pond keeper is aiming for pH 7. The pond reads 8, so acid is added"
                " until it reads 6, and the keeper says that is close enough."
                " Evaluate.",
        "options": [
            {"text": "Sound, because 6 is nearer to 7 than 8 was", "correct": False,
             "why": "Both readings are one step from 7, so nothing has been "
                    "gained."},
            {"text": "Unsound, because the pond is now as far from neutral as "
                      "before", "correct": True},
            {"text": "Sound, because acid always improves alkaline water", "correct": False,
             "why": "Acid moves the reading down; whether that improves anything "
                    "depends on where it stops."},
            {"text": "Unsound, because acid cannot lower a pH reading",
             "correct": False,
             "why": "Adding acid does lower it, which is why the pond moved from "
                    "8 to 6."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h28",
        "band": "harder",
        "text": "Universal indicator gives a colour that sits between two cells on the"
                " printed chart. Describe how the result should be reported.",
        "options": [
            {"text": "As a value between the two, with a meter used if it matters",
             "correct": True},
            {"text": "As the lower of the two numbers, since acids matter more",
             "correct": False,
             "why": "Choosing the lower number is a habit rather than a reading, "
                    "and it is wrong half the time."},
            {"text": "As neutral, because a colour between two cells shows no "
                      "clear result", "correct": False,
             "why": "A colour between two cells is a perfectly clear result "
                    "somewhere between them."},
            {"text": "As a failed test, with the sample thrown away and repeated",
             "correct": False,
             "why": "Nothing failed; the chart simply resolves whole numbers and "
                    "the sample sat between two."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h29",
        "band": "harder",
        "text": "Every cell on the printed scale is the same width as every other."
                " Explain what that drawing hides.",
        "options": [
            {"text": "That the cells at the ends of the scale are used far less "
                      "often", "correct": False,
             "why": "How often a reading occurs is not what the widths would be "
                    "showing."},
            {"text": "That one step of the scale stands for a tenfold change",
             "correct": True},
            {"text": "That the colours in the middle are harder to tell apart",
             "correct": False,
             "why": "Judging the middle colours is a difficulty of reading, not "
                    "something the equal widths conceal."},
            {"text": "That the acid half of the scale is larger than the alkaline "
                      "half", "correct": False,
             "why": "Both halves carry seven steps, so neither is larger than the "
                    "other."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h30",
        "band": "harder",
        "text": "A sample reads pH 7. It is then diluted with an equal volume of"
                " freshly distilled water and reads pH 7 again. Explain why the"
                " reading did not move.",
        "options": [
            {"text": "Because a sample can only be diluted once before the "
                      "reading changes", "correct": False,
             "why": "There is no limit of that kind; each dilution acts on "
                    "whatever is there."},
            {"text": "Because diluting a neutral sample with neutral water leaves "
                      "it neutral", "correct": True},
            {"text": "Because universal indicator cannot report any change near "
                      "the middle", "correct": False,
             "why": "It reports changes near the middle perfectly well; there was "
                    "no change to report."},
            {"text": "Because adding water always raises a reading back to 7 "
                      "again", "correct": False,
             "why": "Water moves a reading towards 7 from either side, and this "
                    "one was already there."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h31",
        "band": "harder",
        "text": "A student tests six samples one after another using the same strip of"
                " indicator paper. Evaluate the method.",
        "options": [
            {"text": "Sound, because the paper changes colour afresh in each "
                      "sample", "correct": False,
             "why": "The strip keeps the colour it has already taken and carries "
                    "liquid with it."},
            {"text": "Sound, because one strip keeps the comparison fair between "
                      "samples", "correct": False,
             "why": "Carrying one sample into the next is the opposite of a fair "
                    "comparison."},
            {"text": "Unsound, because each sample is contaminated by the one "
                      "before", "correct": True},
            {"text": "Unsound, because indicator paper can only be used on "
                      "alkalis", "correct": False,
             "why": "Indicator paper reports acids just as readily as alkalis."},
        ],
        "figure": None,
    },
    {
        "id": "c6-02-h32",
        "band": "harder",
        "text": "A lake reads pH 4 and a river reads pH 6. A student says the lake will"
                " therefore need a hundred times as much alkali to correct."
                " Evaluate.",
        "options": [
            {"text": "Sound, because two steps on the scale is a hundredfold",
             "correct": False,
             "why": "Two steps is a hundredfold in acidity, which is not the same "
                    "as a hundredfold in what it takes to fix."},
            {"text": "Sound, because the amount of alkali is read straight off the "
                      "pH", "correct": False,
             "why": "No amount can be read off a pH, which describes each cm³ "
                    "rather than the whole body of water."},
            {"text": "Unsound, because the volume of water matters as well as the "
                      "reading", "correct": True},
            {"text": "Unsound, because a lake at pH 4 is less acidic than a river "
                      "at pH 6", "correct": False,
             "why": "A lower reading is the more acidic one, so the lake is the "
                    "further from neutral."},
        ],
        "figure": None,
    },
]
