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
]
