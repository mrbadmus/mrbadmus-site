"""B10 lesson 01 — Variation: continuous and discontinuous: twelve questions (MRB-269).

The lesson holds two questions apart that students collapse into one: what
SHAPE the data has, and what CAUSED it. The bank probes both halves and the
join. The easier band checks the shape half on its own — what touching bars
claim, which of the six bench characteristics has a single cause, and the
counting test applied to a set of petals — plus one straight read off the
sixty-student height data. The standard band puts the student in the
situations the bench already showed them: choosing a graph for a three-category
survey, explaining why the mass curve is the broadest of the three, running the
inference from cause to shape (the direction rung 2 does not go), and predicting
what the plotter does with a wrong prediction. The harder band takes the ideas
somewhere the lesson did not go — a hundred sunflowers split between sun and
shade, a population that gained 20 cm in 150 years, a pulse rate counted in
whole beats, and identical twins raised apart.

Both declared misconceptions supply distractors throughout. GENE-01
("continuous variation is caused by the environment; discontinuous variation is
genetic") drives the inherited-therefore-categories option in s03, the
shape-used-as-cause option in h04, the flat "cannot also be genetic" in h02, and
the wrong-reason options in e01 and s01. GENE-02 ("if you can measure it with a
ruler it is continuous") drives the whole of e03, the instrument option in e01,
the count-per-category option in s01, and the counted-beats option in h03 — the
lesson's own siblings argument transplanted to a place where it does not hold.
Three further errors the lesson exists to correct supply the rest: that sample
size decides what kind of graph you draw (s01, h02), that a graph is drawn from
what you predicted rather than from the data (s04), and that an environmental
effect rewrites genes or rules genes out (h01, h04).

`figure` is None throughout: this lesson declares no figures.
"""

UNIT = "B10"
LESSON = "variation-continuous-and-discontinuous"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-e01",
        "band": "easier",
        "text": "The height graph on the bench is drawn with the bars "
                "touching. What are the touching bars claiming?",
        "options": [
            {"text": "That every value in between exists — the categories are "
                     "ranges that join up.",
             "correct": True},
            {"text": "That height was measured with an instrument rather than "
                     "counted.",
             "correct": False,
             "why": "The instrument is not the test. Number of siblings and UK "
                    "shoe size are counted, and neither is continuous. Bars "
                    "touch because a value exists between any two others."},
            {"text": "That most of the sixty students sit near the middle of "
                     "the range.",
             "correct": False,
             "why": "True of the hump, but that is not what the touching bars "
                    "mean. The bars would still touch if the students were "
                    "spread evenly, because the categories still join up."},
            {"text": "That height is inherited from your parents rather than "
                     "set by diet.",
             "correct": False,
             "why": "You have answered question two with a question about "
                    "question one. Whether the bars touch is a claim about the "
                    "data. What caused the variation is a separate question."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e02",
        "band": "easier",
        "text": "Which characteristic on the bench has one cause only — "
                "nothing you eat, do or experience can change it?",
        "options": [
            {"text": "Body mass",
             "correct": False,
             "why": "Mass has the largest environmental share of the six. Diet "
                    "and activity can move one person a long way, which is why "
                    "its curve is the broadest on the bench."},
            {"text": "Height",
             "correct": False,
             "why": "Height is the counter-example the whole lesson is built "
                    "around: strongly inherited AND shifted by childhood "
                    "nutrition. Two causes at once, so not this one."},
            {"text": "Blood group",
             "correct": True},
            {"text": "Hand span",
             "correct": False,
             "why": "Hand span is mostly genetic, because it is closely "
                    "related to height — but mostly is not only. Blood group "
                    "is the one with a single cause: one gene, and nothing "
                    "else."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e03",
        "band": "easier",
        "text": "You count the petals on fifty flowers of one species. Every "
                "flower has a whole number of petals and never anything "
                "between. Which kind of variation is this, and why?",
        "options": [
            {"text": "Continuous, because you can put a precise number on "
                     "every flower.",
             "correct": False,
             "why": "This is the trap the lesson names. The test is not "
                    "whether you can put a number on it, but whether a value "
                    "can exist between two neighbouring values. Between five "
                    "petals and six there is nothing."},
            {"text": "Discontinuous, because no flower has 5.5 petals — there "
                     "are no values in between.",
             "correct": True},
            {"text": "Continuous, because the mean will come out at something "
                     "like 5.4 petals.",
             "correct": False,
             "why": "An average of 5.4 petals is a fact about the set, not a "
                    "flower you could pick. Nobody has 2.4 siblings either — "
                    "an average existing does not make it a possible value."},
            {"text": "Discontinuous, because petal number is decided by genes "
                     "rather than by soil.",
             "correct": False,
             "why": "Right answer, wrong reason — and the wrong reason is the "
                    "one this lesson exists to break. Petal number is "
                    "discontinuous because the values step, not because of "
                    "what caused them."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e04",
        "band": "easier",
        "text": "The bench height data holds sixty students in 5 cm groups: "
                "145–150 has 3, 150–155 has 7, 155–160 has 13, 160–165 has "
                "16, 165–170 has 12, 170–175 has 6, 175–180 has 3. Which "
                "group is the tallest bar?",
        "options": [
            {"text": "155–160 cm",
             "correct": False,
             "why": "Thirteen students — close, but the group beside it holds "
                    "sixteen. This bar is on the way up the near side of the "
                    "hump."},
            {"text": "160–165 cm",
             "correct": True},
            {"text": "165–170 cm",
             "correct": False,
             "why": "Twelve students, and the far side of the peak. The counts "
                    "climb to sixteen at 160–165 and then fall away again, "
                    "which is the shape almost all continuous data takes."},
            {"text": "170–175 cm",
             "correct": False,
             "why": "Six students. The two ends of a continuous characteristic "
                    "are always thin — three students in each end group here, "
                    "against sixteen in the middle."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-01-s01",
        "band": "standard",
        "text": "Your class surveys eye colour and records brown 34, blue 17, "
                "green or hazel 9. How should the graph be drawn, and why?",
        "options": [
            {"text": "A histogram with touching bars, because you have a count "
                     "for every category.",
             "correct": False,
             "why": "Having a number for each category is not what makes bars "
                    "touch. They touch when the categories are ranges that "
                    "join up. Nobody is partway between brown and blue, so "
                    "these bars stand apart."},
            {"text": "A histogram with touching bars, because sixty students "
                     "is a large enough sample.",
             "correct": False,
             "why": "Sample size changes how much you trust the graph, not "
                    "which graph you draw. Six hundred students in three "
                    "separate categories would still give a bar chart with "
                    "gaps."},
            {"text": "A bar chart with gaps, because eye colour is inherited "
                     "and cannot be changed.",
             "correct": False,
             "why": "Right graph, wrong reason. The gap is a claim about the "
                    "data — that nothing sits between the categories. What "
                    "caused the variation is a separate question with a "
                    "separate answer."},
            {"text": "A bar chart with gaps, because the categories are "
                     "separate with nothing in between.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s02",
        "band": "standard",
        "text": "Body mass gives the broadest curve of the three continuous "
                "characteristics on the bench. What explains the extra width?",
        "options": [
            {"text": "Mass responds more strongly to how someone lives, so "
                     "diet and activity spread people out.",
             "correct": True},
            {"text": "Mass is recorded in kilograms, and a coarser unit always "
                     "produces a wider spread.",
             "correct": False,
             "why": "The unit you record in does not change how varied the "
                    "people are. What widens this curve is the environmental "
                    "share: diet and activity can move one person a long way."},
            {"text": "Mass is influenced by fewer genes than height, so its "
                     "values group less tightly.",
             "correct": False,
             "why": "Fewer genes pushes a characteristic towards separate "
                    "categories, not towards a broader smooth curve. One gene "
                    "gives you blood group. The extra width here comes from "
                    "the environment."},
            {"text": "Mass is partly discontinuous, so some students fall "
                     "outside the smooth range.",
             "correct": False,
             "why": "There is no partly. Any mass between the lightest and "
                    "heaviest student is possible, so the data is continuous "
                    "all the way across — and a broad hump is still one hump."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s03",
        "band": "standard",
        "text": "Blood group is decided by genes alone. A student says that "
                "proves its variation has to be discontinuous. Are they right?",
        "options": [
            {"text": "Yes — anything controlled by genes falls into fixed "
                     "categories.",
             "correct": False,
             "why": "Height is one of the most strongly inherited "
                    "characteristics there is, and its curve is perfectly "
                    "smooth. Genes alone does not mean categories. ONE gene "
                    "tends to."},
            {"text": "Yes — genes are fixed at conception, so they cannot "
                     "produce a range of values.",
             "correct": False,
             "why": "Hundreds of genes, each adding a little, produce a smooth "
                    "range with no gaps — and every one of them was fixed at "
                    "conception. Being fixed does not stop genes giving a "
                    "range."},
            {"text": "No — genes alone does not set the shape. What matters is "
                     "how many genes are involved.",
             "correct": True},
            {"text": "No — the shape depends on whether the environment can "
                     "change the characteristic.",
             "correct": False,
             "why": "This is the swap the lesson exists to break: continuous "
                    "does not mean environmental. Height is continuous and "
                    "strongly inherited. Shape follows the number of genes, "
                    "not the environment."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s04",
        "band": "standard",
        "text": "At the bench you choose hand span, predict separate groups — "
                "discontinuous, and press plot. What comes up?",
        "options": [
            {"text": "Bars with gaps between them, because the graph is drawn "
                     "from the prediction you committed to.",
             "correct": False,
             "why": "The graph is drawn from the data, never from your "
                    "prediction — that is exactly why you have to commit "
                    "before you may plot. Hand span is continuous, so the bars "
                    "touch whatever you said."},
            {"text": "Touching bars, and a verdict saying your prediction was "
                     "wrong: hand span is continuous.",
             "correct": True},
            {"text": "Touching bars, and a verdict saying you were wrong about "
                     "the cause of hand span.",
             "correct": False,
             "why": "The verdict judges one thing only — the shape you "
                    "predicted. The cause line under the rule is information, "
                    "not a mark: hand span is mostly genetic, and nothing "
                    "asked you about that."},
            {"text": "Nothing yet — you have to plot three characteristics "
                     "before the first graph appears.",
             "correct": False,
             "why": "Three plotted is where the rail stops tick, not where "
                    "graphs start. Each characteristic plots the moment you "
                    "have committed to a prediction for it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-h01",
        "band": "harder",
        "text": "A gardener grows a hundred sunflowers from seed of one "
                "variety, half in full sun and half in deep shade, then "
                "measures every stem. What should the graph look like?",
        "options": [
            {"text": "Two separate bars with a gap, one for the sunny plants "
                     "and one for the shaded plants.",
             "correct": False,
             "why": "Sun and shade are two treatments, not two categories of "
                    "height. Every height between the shortest and tallest "
                    "plant still exists, so the data stays continuous and the "
                    "bars touch."},
            {"text": "One smooth hump exactly as narrow as full sun alone "
                     "would give, since height is set by genes.",
             "correct": False,
             "why": "Genes set a range and the environment decides where in it "
                    "a plant lands. Same seed, two very different amounts of "
                    "light, so the shaded plants shift down and the whole "
                    "spread widens."},
            {"text": "One smooth hump of touching bars, spread wider than one "
                     "growing condition alone would give.",
             "correct": True},
            {"text": "Separate bars, because the shade sorts the plants into a "
                     "tall group and a short group.",
             "correct": False,
             "why": "Shade shifts plants down the scale; it does not sort them "
                    "into two piles with nothing between. The shortest sunny "
                    "plants overlap the tallest shaded ones, so intermediate "
                    "heights exist."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h02",
        "band": "harder",
        "text": "Average adult height in one country rose by about 20 cm in a "
                "century and a half. A student says this proves height is not "
                "really inherited. What is the flaw?",
        "options": [
            {"text": "There is no flaw — a characteristic the environment can "
                     "change cannot also be genetic.",
             "correct": False,
             "why": "This is the swap the whole lesson is built to break. "
                    "Height is one of the most strongly inherited "
                    "characteristics there is AND it answers to childhood "
                    "nutrition. Both causes, one curve."},
            {"text": "A century and a half is easily long enough for the gene "
                     "pool to have changed that much.",
             "correct": False,
             "why": "Twenty centimetres that fast is far too quick for the "
                    "gene pool to have moved much — that is the point of the "
                    "example. What changed was nutrition, public health and "
                    "childhood disease."},
            {"text": "The people measured in each century were not a fair "
                     "sample of the whole country.",
             "correct": False,
             "why": "Worth checking, but a shift this large, this steady, and "
                    "repeated in other countries within living memory is not a "
                    "sampling artefact. The environment moved; the genes did "
                    "not."},
            {"text": "Nutrition and health changed, not the gene pool — height "
                     "answers to both, and always did.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h03",
        "band": "harder",
        "text": "A class records resting pulse rate to the nearest whole beat "
                "per minute and gets values from 58 to 94. One student says "
                "that makes it discontinuous, like number of siblings. Right?",
        "options": [
            {"text": "Yes — you counted whole beats, and nobody has 72.4 of a "
                     "beat.",
             "correct": False,
             "why": "You counted in whole beats for convenience, but the rate "
                    "itself does not step: 72.4 beats per minute is a real "
                    "rate someone in the room may have. Between two and three "
                    "siblings there is nothing."},
            {"text": "Yes — the values were sorted into groups to be plotted, "
                     "and groups mean discontinuous.",
             "correct": False,
             "why": "Grouping is something you do when you plot, not a "
                    "property of the data. Continuous data is always grouped "
                    "into ranges — which is exactly why a histogram's bars "
                    "touch."},
            {"text": "No — a rate of 72.4 beats per minute is possible, so "
                     "every value in between exists.",
             "correct": True},
            {"text": "No — pulse rate is continuous because exercise and "
                     "health can change it.",
             "correct": False,
             "why": "Right answer, wrong reason. What the environment can "
                    "reach is question two. Pulse rate is continuous because a "
                    "value exists between any two neighbours, and that would "
                    "hold even if nothing changed it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h04",
        "band": "harder",
        "text": "Identical twins are separated at birth and raised in "
                "different countries. As adults their body masses are 14 kg "
                "apart, but their blood groups are the same. Explain both "
                "facts at once.",
        "options": [
            {"text": "Mass answers to diet and activity as well as genes; "
                     "blood group is fixed at conception.",
             "correct": True},
            {"text": "Mass is continuous and blood group is discontinuous, "
                     "which is why only mass could move.",
             "correct": False,
             "why": "You are using the shape of the data to answer a question "
                    "about cause, and they are separate questions. What "
                    "protects blood group is that one gene decides it and "
                    "nothing you eat can reach it."},
            {"text": "Their genes for body mass changed with their diets, "
                     "while the blood-group gene did not.",
             "correct": False,
             "why": "Diet does not rewrite genes. It moves you within the "
                    "range your genes set — these twins started with the same "
                    "range and ended up in different parts of it."},
            {"text": "One result must be wrong, because identical twins have "
                     "identical characteristics.",
             "correct": False,
             "why": "Identical twins have identical genes, not identical "
                    "lives. Anything the environment can reach — mass most of "
                    "all on this bench — can pull them apart. Anything fixed "
                    "at conception cannot."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-e05",
        "band": "easier",
        "text": "Which of these describes continuous variation?",
        "options": [
            {"text": "The values grade into one another, so any in-between "
                     "value is possible.",
             "correct": True},
            {"text": "The values fall into a few separate groups, with no "
                     "possible value lying anywhere in between them.",
             "correct": False,
             "why": "That is discontinuous variation — blood group, or "
                    "tongue rolling. Continuous variation is the other one, "
                    "where the in-between values all exist."},
            {"text": "The characteristic keeps changing all through a "
                     "person's life rather than settling.",
             "correct": False,
             "why": "Continuous is about the values in the data, not about "
                    "whether one person's value moves. Adult height barely "
                    "changes for decades and is still continuous."},
            {"text": "The characteristic is set by the environment, not by "
                     "genes.",
             "correct": False,
             "why": "That is the swap to avoid. Height is continuous and "
                    "strongly inherited, so continuous cannot mean "
                    "environmental. Shape and cause are two separate "
                    "questions."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e06",
        "band": "easier",
        "text": "In a year group of 60 students, 39 can roll their tongue and "
                "21 cannot. Which kind of variation is this, and why?",
        "options": [
            {"text": "Continuous, because 39 and 21 are numbers you can "
                     "count.",
             "correct": False,
             "why": "Being able to count something never settles it. Number "
                    "of brothers and sisters is counted too, and it is "
                    "discontinuous."},
            {"text": "Continuous, because some people can roll their tongue "
                     "further than others.",
             "correct": False,
             "why": "The survey recorded two answers only — can, or cannot. "
                    "There is no halfway category being recorded, so there is "
                    "nothing between the two columns."},
            {"text": "Discontinuous, because there are two categories and no "
                     "halfway between them.",
             "correct": True},
            {"text": "Discontinuous, because tongue rolling is inherited "
                     "rather than learned.",
             "correct": False,
             "why": "Right answer, wrong reason — and the reason is shaky "
                    "as well. What makes this discontinuous is that there is "
                    "nothing between the two categories, not what caused it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e07",
        "band": "easier",
        "text": "What does the word variation mean?",
        "options": [
            {"text": "The way one individual changes as it grows older.",
             "correct": False,
             "why": "That is growth, and it happens inside one organism. "
                    "Variation is about the differences between individuals, "
                    "not about one of them over time."},
            {"text": "The differences between individuals of the same "
                     "species.",
             "correct": True},
            {"text": "The differences between one species and another "
                     "species.",
             "correct": False,
             "why": "Those differences are real, but variation is the word "
                    "for differences within one species — between the "
                    "students in one year group, for instance."},
            {"text": "Any characteristic that the environment is able to "
                     "change.",
             "correct": False,
             "why": "Blood group cannot be changed by anything you do, and "
                    "blood group still varies between people. Variation "
                    "covers everything that differs, whatever caused it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e08",
        "band": "easier",
        "text": "Hand span was measured for 60 students: 15–16 cm has 4, "
                "16–17 has 9, 17–18 has 15, 18–19 has 17, 19–20 has 10 and "
                "20–21 has 5. How many students had a hand span of 19 cm or "
                "more?",
        "options": [
            {"text": "5 students",
             "correct": False,
             "why": "That is the 20–21 cm group on its own. The 19–20 cm "
                    "group counts as well, because 19 cm or more takes in "
                    "everything from 19 cm upwards."},
            {"text": "10 students",
             "correct": False,
             "why": "That is the 19–20 cm group on its own. You have stopped "
                    "one group too early — the 5 students in the 20–21 cm "
                    "group are also 19 cm or more."},
            {"text": "15 students",
             "correct": True},
            {"text": "45 students",
             "correct": False,
             "why": "That is everybody below 19 cm — the four groups at the "
                    "other end. It is the 60 with the 15 taken off, so you "
                    "have counted the wrong side of the line."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e09",
        "band": "easier",
        "text": "Sixty height measurements have been collected, every one a "
                "different number of centimetres. What has to be done with "
                "them before they can be drawn as a histogram?",
        "options": [
            {"text": "Round every measurement to the nearest whole "
                     "centimetre, so the values step.",
             "correct": False,
             "why": "Rounding does not help and it hides detail. A histogram "
                    "does not need stepped values — its whole point is that "
                    "the values in between exist."},
            {"text": "Sort them into equal ranges, which become the bars.",
             "correct": True},
            {"text": "Put them in order from shortest to tallest and give "
                     "each student one bar.",
             "correct": False,
             "why": "Sixty bars one student wide shows you nothing. Grouping "
                    "into ranges is what turns sixty separate numbers into a "
                    "shape you can read."},
            {"text": "Work out the mean, and draw the bars either side of "
                     "it.",
             "correct": False,
             "why": "The mean is one number about the whole set. A histogram "
                    "is drawn from how many students fall in each range, and "
                    "you need the ranges before you can count anybody."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e10",
        "band": "easier",
        "text": "Which of these would be plotted as a histogram, with the "
                "bars touching?",
        "options": [
            {"text": "Blood group",
             "correct": False,
             "why": "Four separate categories with nothing between them, so "
                    "the bars are drawn apart. Nobody is partway between "
                    "group A and group B."},
            {"text": "Tongue rolling",
             "correct": False,
             "why": "Two categories — can, or cannot — and no halfway. Bars "
                    "with a gap, because the gap is the claim that nothing "
                    "sits between them."},
            {"text": "Body mass",
             "correct": True},
            {"text": "Eye colour",
             "correct": False,
             "why": "Recorded as separate colours, so it is plotted as bars "
                    "with gaps. Touching bars would claim there are values "
                    "between brown and blue that were left out."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e11",
        "band": "easier",
        "text": "What does the word characteristic mean when you are "
                "surveying variation?",
        "options": [
            {"text": "A feature an organism inherited from its parents rather "
                     "than picked up.",
             "correct": False,
             "why": "Body mass is a characteristic and diet moves it a long "
                    "way. Whether something is inherited is a separate "
                    "question you ask about a characteristic afterwards."},
            {"text": "A feature that is the same in every member of a "
                     "species.",
             "correct": False,
             "why": "Then no characteristic could vary, and the whole topic "
                    "would be empty. A characteristic is the thing you "
                    "measure; variation is what you find when you do."},
            {"text": "A feature that puts an organism into one group rather "
                     "than another.",
             "correct": False,
             "why": "That fits blood group but not height, and height is a "
                    "characteristic too. Only some characteristics come in "
                    "groups."},
            {"text": "A feature of an organism that can be measured or "
                     "recorded.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-01-s05",
        "band": "standard",
        "text": "A year group's blood groups come out O 28, A 25, B 5 and "
                "AB 2. A student says the counts are so uneven that the "
                "variation must really be continuous. What is wrong?",
        "options": [
            {"text": "Nothing — a fall from 28 all the way down to 2 is "
                     "exactly what continuous data looks like.",
             "correct": False,
             "why": "Four numbers getting smaller is not a smooth range of "
                    "values. There is still no such thing as a blood group "
                    "between A and B, which is what continuous would need."},
            {"text": "The counts are uneven only because a year group of "
                     "60 is far too small a sample.",
             "correct": False,
             "why": "Those proportions are roughly what any large UK sample "
                    "gives. But even a perfectly even 15, 15, 15, 15 would "
                    "still be discontinuous — how common each group is says "
                    "nothing about the kind of variation."},
            {"text": "Blood group is genetic, and genes always give "
                     "categories.",
             "correct": False,
             "why": "Right conclusion, wrong argument. Height is strongly "
                    "inherited and perfectly smooth. What produces categories "
                    "here is that one gene decides it."},
            {"text": "How common each category is has no bearing — nothing "
                     "lies in between.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s06",
        "band": "standard",
        "text": "A shop measures customers' feet in centimetres and also "
                "records the UK shoe size it sells them. Which of the two "
                "sets of data shows continuous variation?",
        "options": [
            {"text": "Both, because both were arrived at by measuring a "
                     "foot.",
             "correct": False,
             "why": "How the number was arrived at is not the test. Shoe "
                    "sizes step — there is a size 7 and a size 8 and nothing "
                    "at 7.3 — while foot length has every value in between."},
            {"text": "Foot length only, because shoe sizes come in steps with "
                     "nothing between them.",
             "correct": True},
            {"text": "Shoe size only, because it is the one recorded on a "
                     "proper agreed scale.",
             "correct": False,
             "why": "An agreed scale is exactly what makes shoe size step. "
                    "The scale was invented with gaps in it; feet were not."},
            {"text": "Neither, because both were recorded as numbers rather "
                     "than as categories.",
             "correct": False,
             "why": "Continuous data is almost always numbers. What decides "
                    "it is whether a value exists between two others, and for "
                    "foot length it always does."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s07",
        "band": "standard",
        "text": "A class of 12 students plots its own heights and gets a "
                "lumpy graph with two separate peaks rather than one smooth "
                "hump. What is the best explanation?",
        "options": [
            {"text": "Height in this class is discontinuous, because two "
                     "peaks means two groups.",
             "correct": False,
             "why": "Every height between the shortest and tallest student in "
                    "that room is still possible. Two peaks in twelve "
                    "readings is what a small sample looks like, not a new "
                    "kind of variation."},
            {"text": "Twelve is too small a sample for the underlying shape "
                     "to show.",
             "correct": True},
            {"text": "The class must have measured some students wrongly.",
             "correct": False,
             "why": "Careless measuring would blur the graph rather than "
                    "produce two clean peaks. Twelve readings spread across "
                    "seven groups will look lumpy however carefully they were "
                    "taken."},
            {"text": "The 5 cm groups were too wide, and narrower groups would "
                     "have given one smooth hump.",
             "correct": False,
             "why": "Narrower groups make a small sample lumpier, not "
                    "smoother — twelve readings spread across more bars "
                    "leaves most bars empty. Widening them hides the "
                    "lumpiness without curing it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s08",
        "band": "standard",
        "text": "Height and hand span both give a hump with most students "
                "near the middle and few at either end. Why is that shape so "
                "common for continuous characteristics?",
        "options": [
            {"text": "Many genes each add a little, and an extreme total needs "
                     "most to fall the same way.",
             "correct": True},
            {"text": "Most people are near the middle because being very tall "
                     "or very short is unhealthy.",
             "correct": False,
             "why": "Health does not sort the class into a hump. The shape "
                    "comes from many small contributions adding up, which "
                    "lands most people somewhere near the middle."},
            {"text": "The measurements were grouped into ranges, and grouping "
                     "always produces a hump.",
             "correct": False,
             "why": "Grouping lets you see the shape; it does not create it. "
                    "Group blood group data any way you like and you will "
                    "never get a hump out of it."},
            {"text": "The environment pushes everybody towards the average "
                     "value for their year group, leaving few at the ends.",
             "correct": False,
             "why": "The environment spreads people out rather than gathering "
                    "them in — which is why body mass, with the largest "
                    "environmental share, gives the broadest curve of all."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s09",
        "band": "standard",
        "text": "A biologist counts the spots on 200 ladybirds and finds "
                "beetles with 2, 4, 7 and 10 spots and no other numbers at "
                "all. How should the data be plotted, and why?",
        "options": [
            {"text": "A histogram with touching bars, because the numbers run "
                     "from 2 up to 10.",
             "correct": False,
             "why": "A range of numbers is not enough. Touching bars would "
                    "claim that a ladybird with 5 or 6 spots exists, and this "
                    "survey found none."},
            {"text": "A histogram with touching bars, because 200 beetles is "
                     "a large sample.",
             "correct": False,
             "why": "Sample size changes how far you trust the result, not "
                    "which graph you draw. Two thousand ladybirds in four "
                    "spot counts would still give separated bars."},
            {"text": "A bar chart with gaps, because no ladybird has a spot "
                     "count in between.",
             "correct": True},
            {"text": "A bar chart with gaps, because spot number is inherited "
                     "and cannot be altered.",
             "correct": False,
             "why": "Right graph, wrong reason. The gap is a claim about the "
                    "data — that nothing was found in between. What caused "
                    "the variation is a separate question."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s10",
        "band": "standard",
        "text": "A student says that if you can sort every individual into a "
                "category without any arguing, the variation must be "
                "discontinuous. Is that a safe rule?",
        "options": [
            {"text": "Yes — being able to sort everybody into a category "
                     "cleanly is exactly what discontinuous variation "
                     "means.",
             "correct": False,
             "why": "Clean categories can be imposed on anything. Sort sixty "
                    "students into 5 cm height groups and nobody will argue, "
                    "and height is still continuous."},
            {"text": "No — continuous data is sorted into ranges too, and "
                     "in-between values exist.",
             "correct": True},
            {"text": "Yes, as long as there are at least three separate "
                     "categories to sort the individuals into.",
             "correct": False,
             "why": "The number of categories is not the test either. Tongue "
                    "rolling has two and is discontinuous; height put into "
                    "seven groups is still continuous."},
            {"text": "No — continuous measurements can never be sorted "
                     "into categories.",
             "correct": False,
             "why": "You always do, and you have to: a histogram's bars are "
                    "exactly those categories. What matters is that its "
                    "ranges join up, which is why the bars touch."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s11",
        "band": "standard",
        "text": "A student surveys 100 daffodils, recording each stem's "
                "length in centimetres and whether its flower is yellow or "
                "white. She draws one graph with touching bars and one with "
                "gaps. Which is which, and why?",
        "options": [
            {"text": "Stem length gets the gaps, because the lengths had "
                     "to be sorted into separate groups of centimetres "
                     "before being plotted.",
             "correct": False,
             "why": "Sorting into groups is how continuous data is always "
                    "plotted, and the groups join up. It is stem length that "
                    "has every value in between, so its bars touch."},
            {"text": "Flower colour gets the touching bars, because yellow "
                     "and white are both colours of the same kind of "
                     "flower.",
             "correct": False,
             "why": "Sharing a heading does not join two categories up. No "
                    "daffodil is partway between yellow and white, so the "
                    "gap between those bars is the honest drawing."},
            {"text": "Stem length gets the touching bars and colour the "
                     "gaps, since only length has values in between.",
             "correct": True},
            {"text": "It cannot be decided until she knows which is set by "
                     "genes.",
             "correct": False,
             "why": "The shape question is answered from the data alone. What "
                    "caused each characteristic is a second question, and you "
                    "can draw both graphs without ever asking it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-h05",
        "band": "harder",
        "text": "Height is influenced by hundreds of genes and gives a smooth "
                "curve. Eye colour is influenced by several genes and yet "
                "came out as three separate bars. Which explanation fits both "
                "results?",
        "options": [
            {"text": "Eye colour was recorded as agreed categories, although "
                     "real eyes grade into one another.",
             "correct": True},
            {"text": "Several genes is few enough to give categories, while "
                     "hundreds is enough to give a smooth range.",
             "correct": False,
             "why": "There is no threshold like that. Real eye colour does "
                    "grade smoothly — the separation on the graph was put "
                    "there by the survey, not by the number of genes."},
            {"text": "Eye colour cannot be changed by the environment, and "
                     "height can, which is what separates the bars.",
             "correct": False,
             "why": "You are answering the shape question with the cause "
                    "question again. Blood group cannot be changed either and "
                    "that is a genuine set of categories, not a recording "
                    "choice."},
            {"text": "Eye colour is measured by eye and height with an "
                     "instrument, and instruments give smooth data.",
             "correct": False,
             "why": "The instrument has never been the test. Hand span is "
                    "measured with a ruler and number of siblings is counted, "
                    "and only one of the two is continuous."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h06",
        "band": "harder",
        "text": "Sixty students were measured in 5 cm height groups: 145–150 "
                "has 3, 150–155 has 7, 155–160 has 13, 160–165 has 16, "
                "165–170 has 12, 170–175 has 6 and 175–180 has 3. What "
                "percentage of the students are 165 cm or taller?",
        "options": [
            {"text": "15 per cent",
             "correct": False,
             "why": "That is the 6 and the 3 in the top two groups, 9 out of "
                    "60. The 12 students in the 165–170 cm group are 165 cm "
                    "or taller as well."},
            {"text": "20 per cent",
             "correct": False,
             "why": "That is the 165–170 cm group alone, 12 out of 60. You "
                    "have stopped after one group instead of adding the three "
                    "groups above 165 cm together."},
            {"text": "35 per cent",
             "correct": True},
            {"text": "65 per cent",
             "correct": False,
             "why": "That is everybody below 165 cm — 39 out of 60. It is the "
                    "right sum on the wrong side of the line, and the two "
                    "answers add to 100 per cent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h07",
        "band": "harder",
        "text": "Five sunflower stems from one bed measure 168 cm, 152 cm, "
                "181 cm, 174 cm and 160 cm. What is the mean height of the "
                "five?",
        "options": [
            {"text": "29 cm",
             "correct": False,
             "why": "That is the range — the tallest take away the shortest. "
                    "The range says how spread out the plants are; the mean "
                    "says where the middle of them sits."},
            {"text": "167 cm",
             "correct": True},
            {"text": "168 cm",
             "correct": False,
             "why": "That is the middle value once the five are put in order, "
                    "which is the median. The mean needs all five added and "
                    "the total shared out between them."},
            {"text": "835 cm",
             "correct": False,
             "why": "That is the five added up and nothing else. You still "
                    "have to divide by 5 — and 835 cm is taller than any "
                    "sunflower, which is the check that catches it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h08",
        "band": "harder",
        "text": "One nurse records 200 students' heights to the nearest "
                "centimetre and another records the same students to the "
                "nearest millimetre. A student says the second set of data is "
                "more continuous. Is she right?",
        "options": [
            {"text": "Yes — the finer the measurement, the more of the "
                     "in-between values you capture.",
             "correct": False,
             "why": "You capture them more precisely, but they were always "
                    "there. Continuous is a fact about height itself, not "
                    "about how carefully anybody wrote it down."},
            {"text": "Yes — recording to the nearest centimetre makes the "
                     "values step, so that set is discontinuous.",
             "correct": False,
             "why": "By that argument every measurement ever taken would be "
                    "discontinuous, since every instrument stops somewhere. "
                    "Rounding is something the nurse did, not something "
                    "height does."},
            {"text": "No — but only because 200 students is enough for either "
                     "set to look smooth.",
             "correct": False,
             "why": "Sample size is not what is being asked about. Twenty "
                    "students measured to the nearest millimetre would be "
                    "continuous data as well, just a lumpier graph."},
            {"text": "No — height has values in between whatever precision "
                     "you record, so both sets are continuous.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h09",
        "band": "harder",
        "text": "Tongue rolling comes in two categories with no halfway, and "
                "yet identical twins sometimes differ and some people learn "
                "to do it. Does that make tongue rolling continuous?",
        "options": [
            {"text": "No — it stays two categories, and it shows the "
                     "environment can reach a discontinuous characteristic.",
             "correct": True},
            {"text": "Yes — anything the environment can change grades "
                     "smoothly rather than falling into groups.",
             "correct": False,
             "why": "That is the swap running the other way. Being reachable "
                    "by the environment is an answer to the cause question, "
                    "and it puts nothing between can and cannot."},
            {"text": "Yes — if some people learn it, there must be people "
                     "partway through learning.",
             "correct": False,
             "why": "The survey records the two answers, and everyone gives "
                    "one of them on the day. A characteristic that changes "
                    "for one person over time is still recorded in categories."},
            {"text": "No — because identical twins have identical genes, so "
                     "the twins who differ must have been recorded wrongly.",
             "correct": False,
             "why": "Identical genes, different lives. Twins differing is "
                    "evidence about the cause, and explaining it away is how "
                    "the tidy one-gene story survived as long as it did."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h10",
        "band": "harder",
        "text": "A poultry keeper records the mass of 200 eggs and gets one "
                "smooth hump. She records shell colour on the same eggs and "
                "gets two separate columns, white and brown. Same birds, same "
                "feed. Explain the two shapes.",
        "options": [
            {"text": "Mass was measured with a balance while colour was "
                     "only looked at, and measuring always gives a smooth "
                     "curve.",
             "correct": False,
             "why": "The instrument is not the test. What matters is that an "
                    "egg of any mass in between is possible, while no egg is "
                    "partway between the two shell colours."},
            {"text": "The feed was the same for every bird, so any "
                     "difference left in the data must be an inherited "
                     "one.",
             "correct": False,
             "why": "That is an answer to the cause question, and it does not "
                    "give you two different shapes. Both characteristics are "
                    "influenced by genes and only one of them is smooth."},
            {"text": "Egg mass has every value in between; shell colour "
                     "falls into two separate categories.",
             "correct": True},
            {"text": "Two hundred eggs is enough for the mass hump but too "
                     "few for colour.",
             "correct": False,
             "why": "Twenty thousand eggs would still give two columns for "
                    "colour, because there is no shade in between to fill a "
                    "third one. Sample size is not what separates these."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h11",
        "band": "harder",
        "text": "In 1900 the average adult in one country was about 165 cm; "
                "today the average is about 178 cm. In both centuries, the "
                "tallest adults were usually the children of tall parents. "
                "Explain how both facts can be true.",
        "options": [
            {"text": "The gene pool changed a little and nutrition changed "
                     "a little, and the two effects add up to the whole 13 "
                     "cm.",
             "correct": False,
             "why": "A century is far too short for the gene pool to have "
                    "moved 13 cm. Almost all of that rise is nutrition, "
                    "public health and childhood disease."},
            {"text": "Only the second fact is really true — tall parents "
                     "having tall children is just a coincidence that "
                     "people notice and remember.",
             "correct": False,
             "why": "It is one of the strongest inherited patterns there is, "
                    "and explaining it away is not needed. Both facts are "
                    "true at once, which is the whole point."},
            {"text": "Height was continuous in 1900 and discontinuous "
                     "today, because the average moved.",
             "correct": False,
             "why": "An average moving does not change the kind of variation. "
                    "Every height in between existed in 1900 and still does, "
                    "so the data was continuous in both centuries."},
            {"text": "Who is tallest in a generation is inherited; where "
                     "the whole population sits is environmental.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-e12",
        "band": "easier",
        "text": "A teacher records whether each student in the class writes "
                "with the left hand or the right hand. What kind of variation "
                "is this?",
        "options": [
            {"text": "Discontinuous — there are two categories and nothing in "
                     "between them.",
             "correct": True},
            {"text": "Continuous — some students write more neatly with one "
                     "hand than they do with the other.",
             "correct": False,
             "why": "Neatness is not what the survey recorded. The two answers "
                    "it did record have nothing lying between them, which is "
                    "what makes the variation discontinuous."},
            {"text": "Continuous — the count in each category can come out at "
                     "any number up to thirty.",
             "correct": False,
             "why": "How many people land in a category is not the test. What "
                    "matters is whether anything sits between writing with the "
                    "left hand and writing with the right, and nothing does."},
            {"text": "Discontinuous — thirty students is too small a class to "
                     "show a smooth range of values.",
             "correct": False,
             "why": "Right answer, wrong reason. Thirty thousand students "
                    "would still give two separate columns, because there is "
                    "no third way of writing in between the two."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e13",
        "band": "easier",
        "text": "A rescue centre records each cat that arrives as black, "
                "ginger or tabby. Which kind of variation is this, and which "
                "graph fits it?",
        "options": [
            {"text": "Continuous variation, drawn as a histogram with the bars "
                     "touching.",
             "correct": False,
             "why": "Continuous data has values in between, and there is no "
                    "coat that is partway between black and ginger. Touching "
                    "bars would claim that there is."},
            {"text": "Discontinuous variation, drawn as a bar chart with gaps "
                     "between the bars.",
             "correct": True},
            {"text": "Continuous variation, drawn as a bar chart with gaps "
                     "between the bars.",
             "correct": False,
             "why": "The two halves contradict one another. Continuous data is "
                    "drawn with the bars touching, because its categories are "
                    "ranges that join up."},
            {"text": "Discontinuous variation, drawn as a histogram with the "
                     "bars touching.",
             "correct": False,
             "why": "The first half is right and the second undoes it. "
                    "Separate categories are drawn apart, because the gap is "
                    "the claim that nothing sits between them."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e14",
        "band": "easier",
        "text": "Which of these characteristics is decided by the environment "
                "alone?",
        "options": [
            {"text": "Natural hair colour",
             "correct": False,
             "why": "Inherited, and fixed at conception. Dye changes what you "
                    "see; it does not change the colour the hair grows."},
            {"text": "Blood group",
             "correct": False,
             "why": "Decided by one gene and by nothing else at all. Nothing "
                    "you eat, do or experience can move it."},
            {"text": "A scar on the knee",
             "correct": True},
            {"text": "Eye colour",
             "correct": False,
             "why": "Several genes decide it, and nothing in the environment "
                    "changes it. Sunlight tans skin, not irises."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e15",
        "band": "easier",
        "text": "What does it mean to say that a characteristic is inherited?",
        "options": [
            {"text": "It appeared during the person's own lifetime and can "
                     "then be passed on to their children.",
             "correct": False,
             "why": "Something picked up during a life is not inherited and is "
                    "not passed on. A scar does not appear on your children."},
            {"text": "It is exactly the same in every member of the species.",
             "correct": False,
             "why": "Then it could not vary at all, and there would be nothing "
                    "to survey. Blood group is inherited and comes in four "
                    "different groups."},
            {"text": "It can be changed by diet or by exercise, provided a "
                     "person keeps at it for long enough.",
             "correct": False,
             "why": "That describes a characteristic the environment can "
                    "reach, which is the opposite of one fixed at conception."},
            {"text": "It was passed on by the parents and fixed at conception.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e16",
        "band": "easier",
        "text": "Most human characteristics have two causes at once. What does "
                "that mean in practice?",
        "options": [
            {"text": "Genes set a range, and the environment decides where in "
                     "that range you end up.",
             "correct": True},
            {"text": "Half of the characteristic comes from genes and half "
                     "from the way a person lives.",
             "correct": False,
             "why": "There is no fixed half and half. The share differs from "
                    "one characteristic to the next — body mass answers to the "
                    "environment far more than hand span does."},
            {"text": "Genes decide the characteristic at birth and the "
                     "environment takes over afterwards.",
             "correct": False,
             "why": "Genes do not stop acting after birth. They set the range "
                    "a person can reach, and the environment moves them about "
                    "within it the whole time."},
            {"text": "The characteristic is genetic in some people and "
                     "environmental in other people.",
             "correct": False,
             "why": "Both causes act on everybody. Nutrition affects every "
                    "child's height, and every child's height is influenced by "
                    "the genes they inherited."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e17",
        "band": "easier",
        "text": "On a graph of a survey, two bars are drawn with a clear gap "
                "between them. What is the gap claiming?",
        "options": [
            {"text": "That the two categories were counted on two different "
                     "days.",
             "correct": False,
             "why": "When the counting happened has nothing to do with the "
                    "drawing. The gap is a claim about values, not about the "
                    "survey's timetable."},
            {"text": "That nothing exists between the two categories.",
             "correct": True},
            {"text": "That fewer people were found in one category than in the "
                     "other.",
             "correct": False,
             "why": "How many people are in each category is shown by the "
                    "height of the bars. The gap between them says something "
                    "else entirely."},
            {"text": "That the characteristic is inherited rather than shaped "
                     "by the environment.",
             "correct": False,
             "why": "That answers the cause question. Whether the bars have a "
                    "gap is a claim about the data, settled before anybody "
                    "asks what caused it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e18",
        "band": "easier",
        "text": "A year group of 60 students has blood groups O 28, A 25, B 5 "
                "and AB 2. How many more students have group O than group B?",
        "options": [
            {"text": "3 students",
             "correct": False,
             "why": "That is the gap between group B and group AB, the two "
                    "smallest columns. Group O is the tall one, at 28."},
            {"text": "20 students",
             "correct": False,
             "why": "Close, but the subtraction is 28 take away 5, not 25 take "
                    "away 5. The 25 belongs to group A."},
            {"text": "23 students",
             "correct": True},
            {"text": "33 students",
             "correct": False,
             "why": "That is 28 and 5 added together, which is the two groups "
                    "combined. How many more asks for the difference."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e19",
        "band": "easier",
        "text": "Body mass was recorded for 60 students: 35–40 kg has 5, 40–45 "
                "has 11, 45–50 has 16, 50–55 has 14, 55–60 has 9 and 60–65 has "
                "5. How many students were lighter than 45 kg?",
        "options": [
            {"text": "5 students",
             "correct": False,
             "why": "That is the 35–40 kg group on its own. Everybody in the "
                    "40–45 kg group is lighter than 45 kg as well."},
            {"text": "11 students",
             "correct": False,
             "why": "That is the 40–45 kg group alone. The five students in "
                    "the lightest group weigh less than 45 kg too."},
            {"text": "32 students",
             "correct": False,
             "why": "That is the two middle groups added, 16 and 14. Those are "
                    "the students between 45 kg and 55 kg, which is the wrong "
                    "side of the line."},
            {"text": "16 students",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e20",
        "band": "easier",
        "text": "Diet and activity can move one person a long way. Which of "
                "the six characteristics surveyed answers most strongly to how "
                "somebody lives?",
        "options": [
            {"text": "Body mass",
             "correct": True},
            {"text": "Height",
             "correct": False,
             "why": "Nutrition does move height, and it moved a whole "
                    "population over a century. But mass answers to diet and "
                    "activity far more, which is why its curve is the "
                    "broadest."},
            {"text": "Tongue rolling",
             "correct": False,
             "why": "Nothing you eat, do or experience changes whether you can "
                    "roll your tongue. It is one of the characteristics "
                    "surveyed with a single, fixed cause."},
            {"text": "Blood group",
             "correct": False,
             "why": "Nothing you eat, do or experience changes a blood group "
                    "either. It is another of the single-cause "
                    "characteristics surveyed."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e21",
        "band": "easier",
        "text": "What is a histogram?",
        "options": [
            {"text": "A graph whose bars are drawn apart, because the "
                     "categories are separate.",
             "correct": False,
             "why": "That is a bar chart. The gap in it is the claim that "
                    "nothing sits between the categories."},
            {"text": "A graph that shows how one measurement changes as time "
                     "goes by.",
             "correct": False,
             "why": "That is a line graph of one thing over time. A histogram "
                    "shows how many individuals fall into each range."},
            {"text": "A graph whose bars touch, because the categories are "
                     "ranges that join up.",
             "correct": True},
            {"text": "A graph carrying one bar for each individual that was "
                     "measured.",
             "correct": False,
             "why": "Sixty bars one student wide shows no shape at all. A "
                    "histogram's bars are ranges, and each height is how many "
                    "students fell in one."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e22",
        "band": "easier",
        "text": "A gardener measures the length of 100 bean pods in "
                "millimetres. What kind of variation will the data show?",
        "options": [
            {"text": "Discontinuous, because each pod is either a long one or "
                     "a short one.",
             "correct": False,
             "why": "Nobody drew that line and the pods do not fall either "
                    "side of it. The lengths run smoothly from the shortest "
                    "pod to the longest."},
            {"text": "Continuous, because a pod of any length in between is "
                     "possible.",
             "correct": True},
            {"text": "Discontinuous, because the lengths have to be sorted "
                     "into groups before they can be plotted.",
             "correct": False,
             "why": "Grouping is how continuous data is always plotted, and "
                    "the groups join up. That is exactly why a histogram's "
                    "bars touch."},
            {"text": "Continuous, because every pod was measured with the very "
                     "same instrument.",
             "correct": False,
             "why": "Right answer, wrong reason. The instrument has never been "
                    "the test — brothers and sisters are counted with no "
                    "instrument at all, and that is discontinuous."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e23",
        "band": "easier",
        "text": "One characteristic in the survey is controlled by a single "
                "gene with only a few versions of it. Which one?",
        "options": [
            {"text": "Height",
             "correct": False,
             "why": "Hundreds of genes each add a little to height, which is "
                    "what gives it a smooth range rather than a few groups."},
            {"text": "Body mass",
             "correct": False,
             "why": "Many genes, with a large environmental share on top. A "
                    "single gene would give separate columns, and mass gives "
                    "the broadest curve there is."},
            {"text": "Eye colour",
             "correct": False,
             "why": "Genes only, but several of them rather than one — which "
                    "is why the old rule about two blue-eyed parents is not "
                    "reliable."},
            {"text": "Blood group",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e24",
        "band": "easier",
        "text": "A characteristic in a fish is controlled by one gene that "
                "comes in three versions. What shape should its variation "
                "take?",
        "options": [
            {"text": "A smooth range, because every fish is slightly different "
                     "from the next one.",
             "correct": False,
             "why": "A smooth range comes from many genes each adding a "
                    "little. One gene can only sort the fish into a few "
                    "groups."},
            {"text": "Separate groups with nothing in between them.",
             "correct": True},
            {"text": "Three groups of exactly the same size as each other.",
             "correct": False,
             "why": "Separate groups, yes — but how common each one is depends "
                    "on how common each version of the gene is, so the columns "
                    "will rarely come out equal."},
            {"text": "A smooth range at first, becoming separate groups once "
                     "more fish have been caught.",
             "correct": False,
             "why": "A larger sample shows the same shape more clearly. It "
                    "does not turn one shape into the other."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e25",
        "band": "easier",
        "text": "Why can a person's blood group never be changed by what they "
                "eat?",
        "options": [
            {"text": "Because the body replaces blood too quickly for food to "
                     "have any effect on it.",
             "correct": False,
             "why": "Blood is replaced constantly, and every new cell is made "
                    "to the same instructions. Speed is not what protects the "
                    "group."},
            {"text": "Because blood group is discontinuous, and food can only "
                     "change continuous characteristics.",
             "correct": False,
             "why": "That mixes up the two questions. Food cannot reach blood "
                    "group because a gene fixes it, not because of the shape "
                    "the data takes."},
            {"text": "Because it is set by a gene, and food cannot rewrite a "
                     "gene.",
             "correct": True},
            {"text": "Because everybody's diet ends up containing much the "
                     "same things in the end.",
             "correct": False,
             "why": "Diets differ enormously and blood groups still do not "
                    "budge. A person who changes diet completely keeps the "
                    "group they were born with."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e26",
        "band": "easier",
        "text": "Whether variation is continuous is a question about the data. "
                "What is the second question, the one with its own separate "
                "answer?",
        "options": [
            {"text": "What caused the variation — genes, the environment, or "
                     "both.",
             "correct": True},
            {"text": "How many individuals were measured in the survey.",
             "correct": False,
             "why": "Sample size is worth knowing, and it is not the question "
                    "this lesson holds apart from the first one."},
            {"text": "Which of the two graphs the results should be drawn on.",
             "correct": False,
             "why": "That is part of the first question. Once you know whether "
                    "values exist in between, the graph follows from it."},
            {"text": "Whether the characteristic is useful to the organism.",
             "correct": False,
             "why": "An interesting question, and not this one. The pair kept "
                    "apart here is what shape the data has and what caused "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e27",
        "band": "easier",
        "text": "Which characteristic is influenced by hundreds of genes, each "
                "one contributing a small amount?",
        "options": [
            {"text": "Blood group",
             "correct": False,
             "why": "One gene, a few versions, four groups. That is the "
                    "opposite end of the scale from hundreds of genes."},
            {"text": "Tongue rolling",
             "correct": False,
             "why": "Largely genetic, and the textbook version calling it a "
                    "single gene is now known to be too simple. Either way it "
                    "is not hundreds."},
            {"text": "Height",
             "correct": True},
            {"text": "Eye colour",
             "correct": False,
             "why": "Several genes rather than one, which is nowhere near "
                    "hundreds — and it was recorded as three separate "
                    "categories."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e28",
        "band": "easier",
        "text": "A student says variation means only the differences you can "
                "see between people. Why is that wrong?",
        "options": [
            {"text": "Because differences you can see are usually caused by "
                     "the environment.",
             "correct": False,
             "why": "What caused a difference is a separate question, and "
                    "plenty of visible differences are inherited. Eye colour "
                    "is one of them."},
            {"text": "Because blood group cannot be seen and still differs "
                     "from person to person.",
             "correct": True},
            {"text": "Because two people who look alike have all the same "
                     "characteristics.",
             "correct": False,
             "why": "Identical twins look alike and can still differ in mass "
                    "by several kilograms. Looking alike is not being the "
                    "same."},
            {"text": "Because seeing a difference is not the same thing as "
                     "measuring it.",
             "correct": False,
             "why": "Careful measuring matters and it is not the flaw here. "
                    "The flaw is that a characteristic nobody can see varies "
                    "as well."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e29",
        "band": "easier",
        "text": "A class surveys a whole year group of 60 rather than the 6 "
                "students on its own table. What is the main reason?",
        "options": [
            {"text": "Six students would give discontinuous data and sixty "
                     "gives continuous data.",
             "correct": False,
             "why": "Sample size does not change the kind of variation. Height "
                    "has values in between whether you measure six people or "
                    "six thousand."},
            {"text": "Sixty is the smallest number a histogram can be drawn "
                     "from.",
             "correct": False,
             "why": "There is no such rule. A histogram can be drawn from any "
                    "number of readings; a small sample just gives a lumpier "
                    "graph."},
            {"text": "Each student's measurement comes out more accurate when "
                     "more students are measured.",
             "correct": False,
             "why": "Accuracy is about how carefully each student is measured. "
                    "A larger sample buys a clearer view of the shape, not a "
                    "better ruler."},
            {"text": "A larger sample shows the underlying shape of the "
                     "variation more reliably.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-e30",
        "band": "easier",
        "text": "Which pair of characteristics are both continuous?",
        "options": [
            {"text": "Height and body mass",
             "correct": True},
            {"text": "Blood group and eye colour",
             "correct": False,
             "why": "Both fall into separate categories with nothing in "
                    "between, so both are discontinuous and both are drawn "
                    "with gaps."},
            {"text": "Height and blood group",
             "correct": False,
             "why": "Height is continuous, but blood group comes in four "
                    "separate groups. Only one of this pair fits."},
            {"text": "Tongue rolling and hand span",
             "correct": False,
             "why": "Hand span is continuous; tongue rolling is two categories "
                    "with no halfway. Again only one of the pair fits."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b10-01-s12",
        "band": "standard",
        "text": "A gardener takes 50 cuttings from one plant, so every cutting "
                "has the same genes, and grows them with different amounts of "
                "fertiliser. Their heights come out spread across a wide "
                "range. What does that show?",
        "options": [
            {"text": "The cuttings cannot really have had the same genes as "
                     "one another.",
             "correct": False,
             "why": "Cuttings taken from one plant are genetically identical, "
                    "and that is what makes this experiment worth doing. The "
                    "spread has to be explained some other way."},
            {"text": "Height in this plant is decided by the environment, with "
                     "no part played by genes at all.",
             "correct": False,
             "why": "The experiment cannot show that, because the genes were "
                    "held the same throughout. A different variety in the same "
                    "trays would sit at a different average."},
            {"text": "The environment can spread a characteristic out even "
                     "when the genes are identical.",
             "correct": True},
            {"text": "The extra fertiliser changed the genes of the plants "
                     "that were given it.",
             "correct": False,
             "why": "Fertiliser feeds a plant; it does not rewrite the plant's "
                    "genes. It moves each one within the range its genes "
                    "allow."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s13",
        "band": "standard",
        "text": "Two people whose natural skin tone is the same spend a summer "
                "in different countries and end up noticeably different "
                "shades. Explain the difference.",
        "options": [
            {"text": "Their genes set the range their skin can reach, and the "
                     "sunlight decided where in it each one landed.",
             "correct": True},
            {"text": "The sunlight changed the genes controlling skin colour "
                     "in the one who travelled south.",
             "correct": False,
             "why": "Sunlight darkens skin; it does not rewrite genes. The "
                    "change happened inside the range the genes already "
                    "allowed."},
            {"text": "Skin colour must be discontinuous, since the two of them "
                     "ended up in different groups.",
             "correct": False,
             "why": "Two people at different shades is not two categories. "
                    "Every shade between them exists, which is what makes skin "
                    "colour continuous."},
            {"text": "Skin colour is decided by sunlight alone, so their genes "
                     "played no part in the result.",
             "correct": False,
             "why": "Two people with different natural tones in the same "
                    "sunlight end up at different shades. The genes set what "
                    "the sun has to work with."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s14",
        "band": "standard",
        "text": "Two classes survey eye colour in the same year group. One "
                "draws the bars touching and the other leaves gaps. Which "
                "drawing is honest, and what does the other one claim?",
        "options": [
            {"text": "The touching bars are honest; gaps would claim that some "
                     "students had been left out of the survey altogether.",
             "correct": False,
             "why": "A gap says nothing about missing students. It says that "
                    "no value lies between the categories, which for eye "
                    "colour is the honest claim to make."},
            {"text": "Either drawing is honest, because the bars come out the "
                     "same height whichever way they are drawn.",
             "correct": False,
             "why": "The heights are the same and the claim is not. Touching "
                    "bars claim that the categories join up, and recorded eye "
                    "colours do not."},
            {"text": "The touching bars are honest, because every student in "
                     "the year group was recorded.",
             "correct": False,
             "why": "Whether everyone was recorded is a question about the "
                    "survey, not about the bars. Bars touch when the "
                    "categories are ranges that join up."},
            {"text": "The gaps are honest; touching bars would claim that "
                     "shades exist in between.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s15",
        "band": "standard",
        "text": "A student measures her own height every month for a year and "
                "plots the twelve readings. Does that graph show variation?",
        "options": [
            {"text": "Yes, and it is continuous, because her height grades "
                     "smoothly upwards.",
             "correct": False,
             "why": "Her height does change smoothly, and a graph of one "
                    "person over time is a record of growth. Variation is what "
                    "you find between individuals."},
            {"text": "No — it shows one individual changing over time, not "
                     "differences between individuals.",
             "correct": True},
            {"text": "Yes, because every value between her first reading and "
                     "her last one existed at some point.",
             "correct": False,
             "why": "True, and still not variation. The word means the "
                    "differences between members of a species, not the changes "
                    "inside one of them."},
            {"text": "No, because twelve readings is far too few for any kind "
                     "of variation to show up.",
             "correct": False,
             "why": "The number of readings is not the problem here. Twelve "
                    "hundred readings from one person would still be a record "
                    "of her growth."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s16",
        "band": "standard",
        "text": "Of the 60 students surveyed, 39 can roll their tongue. What "
                "percentage cannot?",
        "options": [
            {"text": "21 per cent",
             "correct": False,
             "why": "Twenty-one is the number of students who cannot, not the "
                    "percentage. It has to be compared with the 60 before it "
                    "becomes one."},
            {"text": "39 per cent",
             "correct": False,
             "why": "Thirty-nine is the count of students who can. The "
                    "question asks for the percentage of the year group who "
                    "cannot."},
            {"text": "35 per cent",
             "correct": True},
            {"text": "65 per cent",
             "correct": False,
             "why": "That is the percentage who can roll their tongue, 39 out "
                    "of 60. The two answers add up to 100 per cent."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s17",
        "band": "standard",
        "text": "A student claims that a histogram and a bar chart are the "
                "same graph drawn two different ways. Give the difference that "
                "matters.",
        "options": [
            {"text": "In a histogram the categories are ranges that join up, "
                     "so the bars touch.",
             "correct": True},
            {"text": "A histogram is used for a large sample and a bar chart "
                     "for a small one.",
             "correct": False,
             "why": "Sample size changes how much you trust a graph, not which "
                    "graph you draw. Four blood groups in six thousand people "
                    "still give a bar chart."},
            {"text": "A histogram may only be used when the data was taken "
                     "with an instrument.",
             "correct": False,
             "why": "The instrument has never been the test. Hand span is "
                    "measured with a ruler and shoe size is read off a scale, "
                    "and only one of them is continuous."},
            {"text": "A histogram carries more bars than a bar chart of the "
                     "same data.",
             "correct": False,
             "why": "How many bars there are is chosen by whoever groups the "
                    "data. What matters is whether anything exists between one "
                    "bar and the next."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s18",
        "band": "standard",
        "text": "A student predicts that the wingspan of 120 starlings will "
                "come out as separate columns. What will the data actually "
                "show, and why?",
        "options": [
            {"text": "Separate columns, because birds come in a small number "
                     "of distinct sizes.",
             "correct": False,
             "why": "Birds are not sorted into sizes. Any wingspan between the "
                    "smallest bird and the largest is possible, so there is "
                    "nothing for columns to stand apart for."},
            {"text": "Separate columns, because each bird was measured to the "
                     "nearest centimetre.",
             "correct": False,
             "why": "Rounding is something the student did, not a property of "
                    "the birds. A wingspan of 39.4 cm is a real wingspan "
                    "whether or not anyone wrote it down."},
            {"text": "Touching bars, but only once at least 200 birds have "
                     "been measured.",
             "correct": False,
             "why": "A bigger sample shows the shape more clearly. It does not "
                    "decide whether the bars touch, which was settled by the "
                    "wingspans having values in between."},
            {"text": "Touching bars, because a wingspan of any value in "
                     "between is possible.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s19",
        "band": "standard",
        "text": "Two puppies from one litter are raised in different homes, "
                "one fed well and one poorly, and reach different adult "
                "masses. A student says this proves mass is not inherited. "
                "Respond.",
        "options": [
            {"text": "The student is right — a characteristic the environment "
                     "can change cannot also be inherited.",
             "correct": False,
             "why": "Height is strongly inherited and answers to childhood "
                    "nutrition. Two causes acting at once is the normal case, "
                    "not a contradiction."},
            {"text": "Mass is inherited and also answers to feeding; both "
                     "causes act on the one characteristic.",
             "correct": True},
            {"text": "The student is right, unless the two puppies turn out to "
                     "have had different parents.",
             "correct": False,
             "why": "They are litter-mates, so their parents are the same "
                    "pair. What differed was the feeding, which moves mass "
                    "within the range the genes set."},
            {"text": "The student is wrong, because mass is continuous and "
                     "continuous characteristics are inherited.",
             "correct": False,
             "why": "The shape of the data tells you nothing about the cause. "
                    "Mass is continuous whichever way it was caused."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s20",
        "band": "standard",
        "text": "A histogram of hand span has its tallest bar at 18–19 cm and "
                "falls away on both sides. What does that tell you about the "
                "year group?",
        "options": [
            {"text": "Most of the students have a hand span of exactly 18.5 "
                     "cm.",
             "correct": False,
             "why": "The bar covers every span from 18 cm to 19 cm. It says "
                    "how many students fell inside that range, not that they "
                    "share one value."},
            {"text": "The spans at the two ends were probably measured "
                     "carelessly.",
             "correct": False,
             "why": "Thin bars at the ends are the normal shape for continuous "
                    "data. An extreme value needs many small contributions to "
                    "fall the same way, which is rare."},
            {"text": "Most students are near the middle of the range and few "
                     "are at either end.",
             "correct": True},
            {"text": "The 18–19 cm group is wider than the others, so it "
                     "caught more students.",
             "correct": False,
             "why": "Every group on this graph is 1 cm wide. The bar is tall "
                    "because more students fell in it, not because it covers "
                    "more ground."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s21",
        "band": "standard",
        "text": "Which of these surveys would be drawn as a bar chart with "
                "gaps?",
        "options": [
            {"text": "The colour of 200 tulips in a park, recorded as red, "
                     "yellow or white.",
             "correct": True},
            {"text": "The mass of 200 apples from one orchard, recorded in "
                     "grams.",
             "correct": False,
             "why": "Any mass between the lightest apple and the heaviest is "
                    "possible, so this is continuous and its bars touch."},
            {"text": "The time 200 students take to run 100 m, recorded in "
                     "seconds.",
             "correct": False,
             "why": "Times grade into one another: 14.6 s and 14.7 s both "
                    "exist, and so does everything between them."},
            {"text": "The length of 200 earthworms, recorded in millimetres.",
             "correct": False,
             "why": "Lengths have every value in between, so this is "
                    "continuous. Sorting them into ranges to plot them does "
                    "not change that."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s22",
        "band": "standard",
        "text": "A woman dyes her hair red for twenty years and then has "
                "children. What decides the children's natural hair colour?",
        "options": [
            {"text": "Partly the dye, since a characteristic the environment "
                     "changes can be passed on.",
             "correct": False,
             "why": "The environment changes what she looks like; it does not "
                    "change what she passes on. Only what is in the genes is "
                    "inherited."},
            {"text": "Red, because a characteristic kept up for twenty years "
                     "becomes an inherited one.",
             "correct": False,
             "why": "Time makes no difference to this. Twenty years of dye "
                    "leaves her genes exactly as they were at her own "
                    "conception."},
            {"text": "The genes she and the father pass on; dyeing changes "
                     "nothing that is inherited.",
             "correct": True},
            {"text": "It cannot be worked out, because hair colour is "
                     "continuous rather than in groups.",
             "correct": False,
             "why": "The shape of the variation is the other question "
                    "entirely. Whatever shape hair colour takes, dye is not "
                    "part of what is inherited."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s23",
        "band": "standard",
        "text": "A student surveys eye colour but lets each person choose "
                "their own word for their colour, and ends up with fourteen "
                "different answers. What is the problem?",
        "options": [
            {"text": "Fourteen different answers means eye colour is "
                     "continuous after all.",
             "correct": False,
             "why": "Fourteen words for a colour is a recording problem, not a "
                    "smooth range of values. It is the survey that is grading, "
                    "not the eyes."},
            {"text": "The categories have to be agreed before the survey "
                     "starts, or the results cannot be compared.",
             "correct": True},
            {"text": "Fourteen categories is more than a bar chart is allowed "
                     "to show at once.",
             "correct": False,
             "why": "A bar chart can hold as many bars as there are "
                    "categories. The trouble is that two people may mean the "
                    "same eyes by different words."},
            {"text": "Nothing — the more categories a survey uses, the more "
                     "careful it is.",
             "correct": False,
             "why": "Not when the categories overlap one another. Two students "
                    "with the same eyes may land in different columns, and "
                    "that is worse data rather than better."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s24",
        "band": "standard",
        "text": "A student plots 60 heights in 1 cm groups and gets a jagged "
                "graph with many empty bars. What should she do?",
        "options": [
            {"text": "Draw the data as a bar chart with gaps instead of a "
                     "histogram.",
             "correct": False,
             "why": "The gaps would claim that no student has a height in "
                    "between, which is false. The data is continuous however "
                    "lumpy the graph looks."},
            {"text": "Collect the data again, this time measuring to the "
                     "nearest 5 cm.",
             "correct": False,
             "why": "Throwing away precision is not the fix. The measurements "
                    "are fine; it is the grouping that needs changing."},
            {"text": "Leave the graph, because the jagged shape shows that "
                     "height is discontinuous.",
             "correct": False,
             "why": "Sixty students spread across thirty-five bars will look "
                    "jagged whatever happens. Every height in between still "
                    "exists."},
            {"text": "Use wider groups, such as 5 cm, so each bar holds enough "
                     "students to show the shape.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s25",
        "band": "standard",
        "text": "A year group's eye colours come out brown 34, blue 17 and "
                "green or hazel 9. Roughly what is the ratio of brown-eyed to "
                "blue-eyed students?",
        "options": [
            {"text": "About 2 : 1",
             "correct": True},
            {"text": "About 1 : 2",
             "correct": False,
             "why": "The right pair of numbers the wrong way round. There are "
                    "twice as many brown-eyed students as blue-eyed ones, not "
                    "half as many."},
            {"text": "About 3 : 1",
             "correct": False,
             "why": "Three to one would need about 51 brown-eyed students "
                    "against the 17. The count is 34, which is close to "
                    "double."},
            {"text": "About 4 : 1",
             "correct": False,
             "why": "That is roughly brown against green or hazel, 34 to 9. "
                    "The question asks about the blue-eyed students."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s26",
        "band": "standard",
        "text": "A student plots the four blood groups as a histogram with the "
                "bars touching. Name the thing a reader would wrongly believe.",
        "options": [
            {"text": "That more students were surveyed than really were.",
             "correct": False,
             "why": "The heights of the bars carry the counts, and pushing "
                    "them together changes no height. What changes is the "
                    "claim about what lies between."},
            {"text": "That blood groups exist between group A and group B.",
             "correct": True},
            {"text": "That blood group was measured with an instrument rather "
                     "than recorded.",
             "correct": False,
             "why": "How the data was collected is not what the drawing "
                    "claims. Touching bars claim that the categories are "
                    "ranges joining up."},
            {"text": "That the four groups are equally common in the year "
                     "group.",
             "correct": False,
             "why": "How common each group is can be read off the heights, "
                    "whatever the gaps are doing. The gap is a claim about the "
                    "space between them."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s27",
        "band": "standard",
        "text": "A class works out that the mean number of brothers and "
                "sisters is 2.4. A student says that proves values in between "
                "exist. Respond.",
        "options": [
            {"text": "The student is right — 2.4 is a value, so the data has "
                     "values in between.",
             "correct": False,
             "why": "An average is a fact about the whole class, not a family "
                    "you could visit. No student has 2.4 brothers and "
                    "sisters."},
            {"text": "The student is right, because a mean can only be worked "
                     "out from continuous data.",
             "correct": False,
             "why": "A mean can be worked out from any set of numbers. It is "
                    "worth calculating here, and the data stays "
                    "discontinuous."},
            {"text": "No — an average is a property of the set, and no family "
                     "has 2.4 children.",
             "correct": True},
            {"text": "No, because a mean is worked out from counts rather than "
                     "from measurements.",
             "correct": False,
             "why": "Where the mean came from is not the point. The point is "
                    "that no family sits between two children and three."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s28",
        "band": "standard",
        "text": "Explain why it is fair to say the environment has no effect "
                "at all on blood group, but not fair to say the same about "
                "height.",
        "options": [
            {"text": "Height is continuous and blood group is discontinuous, "
                     "which is what decides the matter.",
             "correct": False,
             "why": "The shape of the data is the first question and this is "
                    "the second. A characteristic's shape does not say what "
                    "can reach it."},
            {"text": "Blood group is decided by one gene, so there is nothing "
                     "left for the environment to change.",
             "correct": False,
             "why": "The number of genes is not what keeps the environment "
                    "out. Tongue rolling is largely down to genes as well, and "
                    "some people still learn it."},
            {"text": "The environment affects both equally, but blood group is "
                     "recorded too coarsely to show it.",
             "correct": False,
             "why": "There is no coarseness to blame. A person's blood group "
                    "is the same at every meal of their life, however finely "
                    "it is recorded."},
            {"text": "Nothing a person eats or does changes a blood group, "
                     "while nutrition changes adult height.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s29",
        "band": "standard",
        "text": "Hand span goes closely with height. A student says that means "
                "hand span must give the same shape of graph as height. Is he "
                "right?",
        "options": [
            {"text": "Yes — both are continuous, because a value exists "
                     "between any two others.",
             "correct": True},
            {"text": "No — hand span was recorded in whole centimetres, so its "
                     "values step from one to the next.",
             "correct": False,
             "why": "Recording in whole centimetres is a choice about writing "
                    "the number down. A span of 17.4 cm is a real span "
                    "whatever the ruler is read to."},
            {"text": "No — height has two causes and hand span is mostly "
                     "genetic, so the two graphs come out differently.",
             "correct": False,
             "why": "You are answering with the cause question again. Both "
                    "characteristics have values in between, which is what "
                    "gives them the same shape."},
            {"text": "Yes — two characteristics that go together always give "
                     "the same graph as one another.",
             "correct": False,
             "why": "Right answer, wrong reason. Blood group goes with the "
                    "gene a person inherited and gives a completely different "
                    "shape from height."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-s30",
        "band": "standard",
        "text": "A school changes its lunches and the average body mass of its "
                "students rises steadily over five years. What does that show "
                "about body mass?",
        "options": [
            {"text": "Body mass is decided by food alone, and genes have "
                     "nothing to do with it.",
             "correct": False,
             "why": "Students eating the same lunches still differ from one "
                    "another, and that spread is largely inherited. Food moved "
                    "the average, not the whole story."},
            {"text": "The environment can move a whole population, so mass has "
                     "an environmental cause as well as a genetic one.",
             "correct": True},
            {"text": "Body mass became continuous once it started to change "
                     "year on year.",
             "correct": False,
             "why": "Mass was continuous before the lunches changed and stayed "
                    "continuous afterwards. An average moving does not change "
                    "the kind of variation."},
            {"text": "The students' genes for body mass changed over the five "
                     "years.",
             "correct": False,
             "why": "Five years cannot shift a gene pool, and nothing on a "
                    "lunch tray rewrites a gene. What moved is where students "
                    "sit inside the range their genes allow."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b10-01-h12",
        "band": "harder",
        "text": "Two blue-eyed parents have a brown-eyed child. A student says "
                "one of them cannot be the biological parent. Evaluate that "
                "claim.",
        "options": [
            {"text": "The student is right: two blue-eyed parents cannot "
                     "produce a brown-eyed child.",
             "correct": False,
             "why": "That old rule is not reliable. It comes from treating eye "
                    "colour as one gene, and several genes are involved."},
            {"text": "The claim fails, because several genes affect eye colour "
                     "and the old blue-eyed rule is unreliable.",
             "correct": True},
            {"text": "The claim fails, because strong sunlight in infancy can "
                     "darken a child's eyes.",
             "correct": False,
             "why": "Eye colour is genes only. Sunlight tans skin; it does not "
                    "reach the colour of an iris, so this defends the family "
                    "with the wrong argument."},
            {"text": "The claim fails, because eye colour is continuous and a "
                     "child can land anywhere.",
             "correct": False,
             "why": "The survey records eye colour in categories, so the data "
                    "is discontinuous. The rule fails on the number of genes, "
                    "not on the shape."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h13",
        "band": "harder",
        "text": "A study finds that adopted children's adult heights match "
                "their birth parents' more closely than their adoptive "
                "parents'. What does that show, and what does it not show?",
        "options": [
            {"text": "Height is strongly inherited; it does not show that "
                     "nutrition has no effect.",
             "correct": True},
            {"text": "Height is entirely genetic, since the adoptive home made "
                     "no difference to the children at all.",
             "correct": False,
             "why": "The study compares children who were all fed reasonably "
                    "well. Change the feeding enough and the whole group "
                    "moves — which is what happened to the Dutch."},
            {"text": "Height is continuous, which is why the birth parents' "
                     "heights predict the children's.",
             "correct": False,
             "why": "The shape of the data is the other question. What this "
                    "study measures is how far height is passed on, not "
                    "whether values in between exist."},
            {"text": "Nothing at all, because adopted children are too few for "
                     "a study of this kind.",
             "correct": False,
             "why": "Adoption studies are one of the standard ways of "
                    "separating the two causes, and this result has been found "
                    "many times over."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h14",
        "band": "harder",
        "text": "In a survey of 240 people, 3 in every 8 could roll their "
                "tongue. How many could not?",
        "options": [
            {"text": "90 people",
             "correct": False,
             "why": "That is the number who could: 240 divided by 8 is 30, and "
                    "3 lots of 30 is 90. The question asks for the rest."},
            {"text": "96 people",
             "correct": False,
             "why": "That is 240 divided by 2.5, which is not what 5 in every "
                    "8 comes to. One eighth of 240 is 30, so five eighths is "
                    "150."},
            {"text": "150 people",
             "correct": True},
            {"text": "144 people",
             "correct": False,
             "why": "That is three fifths of 240. The fraction here has eighths "
                    "in it, not fifths, so the first step is 240 divided by 8."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h15",
        "band": "harder",
        "text": "A sample of 60 students gave blood groups O 28, A 25, B 5 and "
                "AB 2. In a town of 600 people with the same proportions, "
                "roughly how many would be group AB?",
        "options": [
            {"text": "2 people",
             "correct": False,
             "why": "That is the count in the sample of 60. The town is ten "
                    "times larger, so the count scales up with it."},
            {"text": "12 people",
             "correct": False,
             "why": "That is six times the sample count rather than ten. The "
                    "town is 600, which is 60 multiplied by 10."},
            {"text": "200 people",
             "correct": False,
             "why": "That would be one person in three, and group AB was 2 "
                    "students in 60 — about one person in thirty."},
            {"text": "20 people",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h16",
        "band": "harder",
        "text": "Two year groups both give smooth height curves. One is spread "
                "from 145 cm to 180 cm and the other from 155 cm to 170 cm. "
                "Which statement does the data support?",
        "options": [
            {"text": "The first year group is taller on average than the "
                     "second one.",
             "correct": False,
             "why": "The spread says nothing about the average. Both curves "
                    "could peak at the same height, with one reaching further "
                    "in each direction."},
            {"text": "The first year group varies more in height than the "
                     "second one.",
             "correct": True},
            {"text": "The second year group was measured more carefully than "
                     "the first.",
             "correct": False,
             "why": "Careless measuring would widen a curve rather than "
                    "narrowing it, and a 15 cm spread is perfectly ordinary "
                    "for a year group."},
            {"text": "The second year group's data is discontinuous, because "
                     "its range holds fewer groups.",
             "correct": False,
             "why": "Fewer bars is not the same as separate categories. Every "
                    "height between 155 cm and 170 cm still exists, so that "
                    "data stays continuous."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h17",
        "band": "harder",
        "text": "A class of 30 surveys blood group and finds nobody with group "
                "AB. Does that mean group AB is absent from the population "
                "they belong to?",
        "options": [
            {"text": "No — AB is rare, so a class of 30 will often contain "
                     "nobody with it.",
             "correct": True},
            {"text": "Yes — a survey records what is there, so AB is absent "
                     "from this population.",
             "correct": False,
             "why": "A survey records what is in the sample. About 3 people in "
                    "100 are group AB, so missing it in 30 students is what "
                    "you would expect."},
            {"text": "No — the class must have recorded some of its students' "
                     "groups wrongly.",
             "correct": False,
             "why": "Nothing has gone wrong. A rare category can be missing "
                    "from a small sample with every reading taken correctly."},
            {"text": "Yes, for this class, which shows that blood group varies "
                     "between populations.",
             "correct": False,
             "why": "One class of 30 is not a population, and its result is "
                    "not evidence of a difference between populations."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h18",
        "band": "harder",
        "text": "Average adult height in one country rose for a century and "
                "has now stopped rising. A student says the population has "
                "reached its genetic limit. Evaluate that.",
        "options": [
            {"text": "It must be right, because nothing else could stop a rise "
                     "that had gone on so long.",
             "correct": False,
             "why": "A rise driven by improving nutrition stops when nutrition "
                    "stops improving. That explanation has to be ruled out "
                    "before any limit is claimed."},
            {"text": "It is wrong, because the gene pool has changed and "
                     "brought the rise to an end.",
             "correct": False,
             "why": "A century is far too short for the gene pool to have "
                    "moved much in either direction. The genes are not what "
                    "changed here."},
            {"text": "More likely nutrition and health stopped improving, "
                     "which is what had been driving the rise.",
             "correct": True},
            {"text": "It is wrong, because height has become discontinuous now "
                     "that the values have settled down.",
             "correct": False,
             "why": "An average settling changes nothing about the shape. "
                    "Every height in between still exists, so the data is as "
                    "continuous as it ever was."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h19",
        "band": "harder",
        "text": "Identical twins raised in the same house are usually within a "
                "couple of centimetres in height, but can differ by several "
                "kilograms in mass. Explain the difference.",
        "options": [
            {"text": "Height is inherited and body mass is not inherited at "
                     "all.",
             "correct": False,
             "why": "Mass is inherited as well — children of heavy parents "
                    "tend to be heavier. It simply answers to diet and "
                    "activity much more than height does."},
            {"text": "Mass is continuous and height is discontinuous, so mass "
                     "can take more values.",
             "correct": False,
             "why": "Both are continuous. The shape of the data is not what "
                    "decides how far two people with the same genes can drift "
                    "apart."},
            {"text": "The twins' genes for body mass drifted apart as the two "
                     "of them grew older.",
             "correct": False,
             "why": "Identical twins keep identical genes for life. What "
                    "differs is what they eat and do, which mass answers to "
                    "and height barely does."},
            {"text": "Mass answers to diet and activity far more than height "
                     "does, so it moves further.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h20",
        "band": "harder",
        "text": "Snails in one wood have shells with 0, 1, 3 or 5 dark bands "
                "and nothing in between, and shell widths running from 12 mm "
                "to 24 mm. How should each be plotted?",
        "options": [
            {"text": "Both as bar charts with gaps, since both were recorded "
                     "from the same snails.",
             "correct": False,
             "why": "Coming from one animal does not make two characteristics "
                    "the same kind. A shell of 18.4 mm exists; a shell with "
                    "2 bands was never found."},
            {"text": "Band number with gaps and shell width with touching "
                     "bars.",
             "correct": True},
            {"text": "Band number with touching bars, because the counts run "
                     "from 0 up to 5.",
             "correct": False,
             "why": "Touching bars would claim a snail with 2 or 4 bands "
                    "exists, and the survey found none. A range of numbers is "
                    "not the same as a range of values."},
            {"text": "Both as histograms, because every value was recorded as "
                     "a number.",
             "correct": False,
             "why": "Numbers are not the test. Band number steps from one "
                    "whole band to the next, while width has every value in "
                    "between."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h21",
        "band": "harder",
        "text": "A student says that because the environment can change body "
                "mass, mass is useless for studying what is passed from parent "
                "to child. Evaluate that.",
        "options": [
            {"text": "It goes too far — mass is inherited in part, so it is "
                     "useful provided the environment is taken into account.",
             "correct": True},
            {"text": "Correct — a characteristic with two causes can tell you "
                     "nothing about what is inherited.",
             "correct": False,
             "why": "Most characteristics have two causes, so that would rule "
                    "out nearly everything. Height has two causes and is one "
                    "of the best-studied inherited characteristics there is."},
            {"text": "Wrong — the environment cannot reach anything that is "
                     "inherited in the first place.",
             "correct": False,
             "why": "It reaches plenty. Height is inherited and childhood "
                    "nutrition moves it, which is the counter-example the "
                    "whole topic turns on."},
            {"text": "Wrong — mass is continuous, and continuous "
                     "characteristics are the most useful ones to study.",
             "correct": False,
             "why": "Being continuous is a fact about the data and says "
                    "nothing about how useful it is. Blood group is "
                    "discontinuous and extremely useful."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h22",
        "band": "harder",
        "text": "Nine hand spans are measured, in centimetres: 16, 17, 17, 18, "
                "18, 18, 19, 20, 21. Give the modal span and the range.",
        "options": [
            {"text": "Mode 18 cm, range 21 cm",
             "correct": False,
             "why": "The mode is right. The range is the largest take away the "
                    "smallest, not the largest value on its own."},
            {"text": "Mode 3 cm, range 5 cm",
             "correct": False,
             "why": "Three is how many students had the modal span, not the "
                    "span itself. The mode is the value that comes up most "
                    "often."},
            {"text": "Mode 18 cm, range 5 cm",
             "correct": True},
            {"text": "Mode 18.2 cm, range 5 cm",
             "correct": False,
             "why": "18.2 cm is roughly the mean of the nine. The mode is the "
                    "value that appears most often, and 18 cm appears three "
                    "times."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h23",
        "band": "harder",
        "text": "Genetically identical seedlings are split between a room at "
                "15 °C and one at 25 °C. The warm set is taller on average, "
                "and each set still gives a smooth hump. What do the two "
                "results show together?",
        "options": [
            {"text": "The seedlings cannot have been genetically identical, "
                     "since each set still spreads out.",
             "correct": False,
             "why": "Identical plants still meet different light, water and "
                    "neighbours. The spread inside a set is the evidence that "
                    "conditions vary within a room."},
            {"text": "Temperature changed the plants' genes, which is why the "
                     "warm set grew taller.",
             "correct": False,
             "why": "Warmth speeds growth; it does not rewrite genes. The warm "
                    "set reached further inside the range its genes already "
                    "allowed."},
            {"text": "Height in this plant is discontinuous, because two "
                     "temperatures gave two averages.",
             "correct": False,
             "why": "Two treatments are not two categories of height. Both "
                    "sets are humps that overlap, so every height in between "
                    "exists."},
            {"text": "Temperature moved each set along, and the spread left "
                     "inside a set comes from other conditions.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h24",
        "band": "harder",
        "text": "Somebody argues that any data read off a measuring scale "
                "should be plotted with touching bars. Give the case that "
                "disproves it.",
        "options": [
            {"text": "Blood group, which is not read off a scale and still "
                     "needs separate bars.",
             "correct": False,
             "why": "Blood group agrees with the rule rather than breaking it. "
                    "To disprove a rule you need a case that obeys its "
                    "condition and breaks its conclusion."},
            {"text": "UK shoe size, read off a measured foot and still "
                     "stepping from one size to the next.",
             "correct": True},
            {"text": "Height, which is read off a scale and does need touching "
                     "bars.",
             "correct": False,
             "why": "That is an example the rule gets right. An example that "
                    "agrees can never disprove anything."},
            {"text": "Eye colour, which is recorded by looking and needs "
                     "separate bars.",
             "correct": False,
             "why": "No scale was read, so the rule says nothing about eye "
                    "colour and cannot be caught out by it."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h25",
        "band": "harder",
        "text": "A class plots the boys' and the girls' heights as two curves "
                "that overlap heavily. A student says the graph proves height "
                "is discontinuous, since there are two groups. Evaluate.",
        "options": [
            {"text": "The curves overlap, so heights in between exist and "
                     "height stays continuous.",
             "correct": True},
            {"text": "The student is right, because boys and girls are two "
                     "separate categories of student.",
             "correct": False,
             "why": "The categories are of students, not of heights. The "
                    "question is whether a height between two others exists, "
                    "and every one of them does."},
            {"text": "The student is right, because two peaks mean two "
                     "separate sets of genes at work.",
             "correct": False,
             "why": "Two peaks in overlapping curves are two averages, not two "
                    "sets of values. Hundreds of genes are at work in both "
                    "groups."},
            {"text": "It cannot be judged at all until a great many more "
                     "students have been measured.",
             "correct": False,
             "why": "The kind of variation is settled by whether values in "
                    "between exist, which you can answer from the overlap you "
                    "already have."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h26",
        "band": "harder",
        "text": "Body mass for 60 students came out 35–40 kg 5, 40–45 kg 11, "
                "45–50 kg 16, 50–55 kg 14, 55–60 kg 9, 60–65 kg 5. What "
                "fraction of the students are between 45 kg and 55 kg?",
        "options": [
            {"text": "One quarter",
             "correct": False,
             "why": "A quarter of 60 is 15, and the two middle groups hold 30 "
                    "between them. That is twice as many."},
            {"text": "Three tenths",
             "correct": False,
             "why": "Three tenths of 60 is 18. You may have taken 30 as the "
                    "top of the fraction and then divided by the wrong "
                    "number."},
            {"text": "One half",
             "correct": True},
            {"text": "One third",
             "correct": False,
             "why": "A third of 60 is 20, which is neither of the two groups "
                    "nor their total. The two groups add to 30."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h27",
        "band": "harder",
        "text": "A biologist wants to settle whether beak length in a finch "
                "population is continuous. Which single test answers it?",
        "options": [
            {"text": "Check whether the beaks were measured with an instrument "
                     "or judged by eye.",
             "correct": False,
             "why": "The instrument has never been the test. Number of "
                    "brothers and sisters is counted by eye and is "
                    "discontinuous; so is UK shoe size, read off a scale."},
            {"text": "Check whether beak length is inherited from the parent "
                     "birds.",
             "correct": False,
             "why": "That answers the cause question rather than the shape "
                    "one. Height is inherited and smooth; blood group is "
                    "inherited and comes in groups."},
            {"text": "Check whether the lengths sort into more than two groups "
                     "when they are plotted.",
             "correct": False,
             "why": "How many groups you sort data into is a choice made when "
                    "plotting. Continuous data is routinely sorted into seven "
                    "or eight ranges."},
            {"text": "Ask whether a beak of any length between two measured "
                     "birds could exist.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h28",
        "band": "harder",
        "text": "Could one characteristic — coat colour, say — be continuous "
                "in one species and discontinuous in another?",
        "options": [
            {"text": "No — a characteristic keeps one kind of variation "
                     "wherever it is found.",
             "correct": False,
             "why": "Nothing ties a characteristic to one shape across "
                    "species. What sets the shape is how many genes control it "
                    "in that species."},
            {"text": "Yes — the number of genes controlling it can differ "
                     "between species, and so can the shape.",
             "correct": True},
            {"text": "Yes, but only where the two species live in very "
                     "different environments.",
             "correct": False,
             "why": "The environment moves individuals within a range; it does "
                    "not turn separate categories into a smooth one. The "
                    "number of genes does that."},
            {"text": "No — species differ in the values they show, never in "
                     "the kind of variation.",
             "correct": False,
             "why": "They differ in both. One gene in one species and many in "
                    "another gives two genuinely different shapes."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h29",
        "band": "harder",
        "text": "Why are the bars of a histogram normally drawn covering equal "
                "ranges, such as 5 cm each?",
        "options": [
            {"text": "So that the heights of the bars can be compared with one "
                     "another fairly.",
             "correct": True},
            {"text": "So that every bar ends up holding the same number of "
                     "students as the others.",
             "correct": False,
             "why": "Equal ranges give very unequal counts, which is the whole "
                    "point — the tall middle bar is what shows the shape of "
                    "the data."},
            {"text": "So that the bars touch, which is what makes the graph a "
                     "histogram.",
             "correct": False,
             "why": "The bars touch because the ranges join up, whether or not "
                    "they are equal. Equal widths are about comparing heights "
                    "fairly."},
            {"text": "Because unequal ranges would make the data itself "
                     "discontinuous.",
             "correct": False,
             "why": "Nothing you do when plotting changes the data. Heights "
                    "have values in between however the ranges are chosen."},
        ],
        "figure": None,
    },
    {
        "id": "b10-01-h30",
        "band": "harder",
        "text": "Tongue rolling was once taught as the work of a single gene. "
                "Then identical twins were found who differed, and some people "
                "were found who had learned it. What should be done with the "
                "rule?",
        "options": [
            {"text": "Keep the rule, and treat the twins who differ as records "
                     "taken down wrongly.",
             "correct": False,
             "why": "Explaining away the evidence that disagrees is how a tidy "
                    "story survives longer than it should. The twins were "
                    "recorded correctly."},
            {"text": "Drop tongue rolling from surveys, since the rule about "
                     "it turned out to fail.",
             "correct": False,
             "why": "It is still the simplest characteristic to survey in a "
                    "classroom. What needs revising is the explanation, not "
                    "the survey."},
            {"text": "Treat the single-gene account as too simple, and look "
                     "for what else affects it.",
             "correct": True},
            {"text": "Conclude that tongue rolling is really continuous after "
                     "all, since the rule broke down.",
             "correct": False,
             "why": "Still two categories on the day of the survey, and "
                    "nothing in between them. The rule that failed was about "
                    "the cause, not about the shape."},
        ],
        "figure": None,
    },
]
