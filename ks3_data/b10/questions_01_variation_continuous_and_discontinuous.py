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
]
