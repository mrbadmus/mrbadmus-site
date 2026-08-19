"""B6 lesson 03 — Substance misuse and decisions: twelve questions (MRB-269).

The lesson teaches one definition and one habit of mind: a claim about a drug
is only as good as the evidence behind it, and the four questions that test it
are how many and who, compared with what, who is telling me, and together or
because. The bank probes both. The easier band checks the definition itself and
the three words the rest of the lesson runs on — what natural and synthetic
actually tell you, what a dummy is, and what a correlation licenses. The
standard band puts the student back in front of the arguments the bench already
handled — the vaping count, the energy-drink study, a supplement with nothing
to compare it against, a herbal capsule of unknown strength — and asks what is
wrong with the evidence rather than what is wrong with the substance. The
harder band takes the ideas somewhere the page did not go: a school's revision
app, a company-funded trial whose design survives the question, the one real
study on the page set against the objection it was built to answer, and why an
inaccurate estimate of what everyone else does is itself a cause.

All three declared misconceptions supply distractors. DRUG-05 ("if it's
natural, it's safe — it's the chemicals that hurt you") drives the
factory-chemical option in e01, all three distractors in e02, the "cannot be
measured" and "broken down more slowly" options in s04, and the strength
confusion in s04's first option. DRUG-06 ("everyone my age is doing it") drives
the "too few people" and dishonest-answer options in s01 and the "surveys must
have sampled badly" option in h04. NOS-05 ("one person who came to no harm
disproves a risk") drives s02's single-student option, where a lone case is
offered as a way of settling an average.

Two errors the lesson exists to correct supply the rest, and both are the same
error in different clothes: that a bigger study fixes a study that chose
itself (s01, s02, h01, h03 — "size fixes noise, not confusion"), and that
anyone who profits from an answer is disqualified rather than in need of
checking (h02).

`figure` is None throughout: this lesson declares no figures, and the
instrument is the visual.
"""

UNIT = "B6"
LESSON = "substance-misuse-and-decisions"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-03-e01",
        "band": "easier",
        "text": "A pupil says substance misuse means taking illegal drugs. "
                "What does it actually mean?",
        "options": [
            {"text": "Taking a substance that is against the law to buy, sell "
                     "or carry.",
             "correct": False,
             "why": "That is a fact about what a shop is allowed to sell, not "
                    "about what a substance does to a body. Alcohol is legal "
                    "and is misused every day; so are prescription "
                    "medicines."},
            {"text": "Using a substance in a way that damages health, legal "
                     "ones and medicines included.",
             "correct": True},
            {"text": "Taking a substance so often that the body becomes "
                     "addicted to it and needs it to function.",
             "correct": False,
             "why": "Addiction is one way misuse can end up, not what the "
                    "word means. One dose of a medicine taken wrongly damages "
                    "health without anyone being addicted to anything."},
            {"text": "Taking a chemical that was made in a factory rather "
                     "than grown in the ground.",
             "correct": False,
             "why": "Where a molecule came from tells you nothing about what "
                    "it does. The paracetamol in the pharmacy is factory-made "
                    "to a known dose, and the known dose is what makes it "
                    "safe to use."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e02",
        "band": "easier",
        "text": "Nicotine, digitalis and ricin are all made by plants. The "
                "paracetamol in a pharmacy is made in a factory. What do the "
                "words natural and synthetic tell you about a substance?",
        "options": [
            {"text": "That a natural one works with the body, while a "
                     "factory one forces it.",
             "correct": False,
             "why": "A plant does not manufacture its molecules for your "
                    "benefit. Several of them are made specifically to poison "
                    "whatever tries to eat the plant, which is why nicotine "
                    "exists at all."},
            {"text": "That a natural one is gentler, because bodies have met "
                     "it for far longer.",
             "correct": False,
             "why": "Bodies have met deadly nightshade for just as long. How "
                    "long a substance has been around changes nothing about "
                    "what a dose of it does once it is inside you."},
            {"text": "Only where the molecule came from, and nothing about "
                     "what it does in a body.",
             "correct": True},
            {"text": "That a factory one is purer, so a factory one is always "
                     "the safer choice.",
             "correct": False,
             "why": "Right about the purity, wrong about what follows. A "
                    "known dose is what makes the pharmacy tablet safe, not "
                    "the factory — plenty of factory-made substances will "
                    "kill you."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e03",
        "band": "easier",
        "text": "In a drug trial one group is given a dummy, which is called "
                "a placebo at GCSE. What is a dummy?",
        "options": [
            {"text": "A version that looks and tastes identical, with the "
                     "active ingredient left out.",
             "correct": True},
            {"text": "A much smaller dose of the same drug, given to the "
                     "second group instead.",
             "correct": False,
             "why": "Then both groups are taking the drug, and any difference "
                    "between them is a difference of dose. It cannot tell you "
                    "whether the drug does anything at all."},
            {"text": "A different medicine that is already known to work, "
                     "used for comparison.",
             "correct": False,
             "why": "That compares one medicine against another, which is a "
                    "different question. To find out whether this one works, "
                    "the other group has to take nothing active."},
            {"text": "Nothing at all — the second group simply takes no "
                     "tablet and is watched.",
             "correct": False,
             "why": "Close, but people who know they have been given nothing "
                    "report differently. The dummy exists so that the only "
                    "difference between the two groups is the ingredient."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e04",
        "band": "easier",
        "text": "A newspaper reports that pupils who eat breakfast get better "
                "grades, under the headline 'Breakfast raises grades'. What "
                "has the study actually found?",
        "options": [
            {"text": "A cause: eating breakfast is what produces the higher "
                     "grades.",
             "correct": False,
             "why": "Nothing here says which way the arrow points, or whether "
                    "something else produces both — an earlier bedtime and a "
                    "settled morning would give you the same table."},
            {"text": "An anomaly: the result does not fit what would be "
                     "expected.",
             "correct": False,
             "why": "The result fits perfectly well; nothing about it is odd. "
                    "What is missing is any reason to call the pattern a "
                    "cause."},
            {"text": "A fair test: two groups were compared, and one of them "
                     "did better.",
             "correct": False,
             "why": "Nobody split the pupils into groups. They sorted "
                    "themselves by whether they eat breakfast, and a fair "
                    "test changes one thing on purpose."},
            {"text": "A correlation: two things changing together, with no "
                     "cause shown.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-03-s01",
        "band": "standard",
        "text": "Someone argues that most people their age vape: 22 of the 30 "
                "people in their form and friendship group have tried it, and "
                "they see people vaping outside school every day. What is the "
                "main fault in that evidence?",
        "options": [
            {"text": "Twenty-two out of thirty is too few people to say "
                     "anything about a whole year group.",
             "correct": False,
             "why": "The number is not the problem. Ask three hundred people "
                    "from the same form and the same street corner and you "
                    "get the same wrong answer, because they were chosen the "
                    "same way. Size fixes noise, not confusion."},
            {"text": "People asked about vaping in front of their friends are "
                     "unlikely to answer honestly.",
             "correct": False,
             "why": "They might not, but that is a guess about lying. The "
                    "fault is there even if every single answer is true: the "
                    "people counted were never a fair sample of the age "
                    "group."},
            {"text": "The people counted are not a fair sample — vapers are "
                     "visible, and non-vapers are not.",
             "correct": True},
            {"text": "Seeing people outside school every day is not evidence, "
                     "because nobody actually counted them.",
             "correct": False,
             "why": "Counting them would not save it. Everyone standing "
                    "outside school is easy to see and everyone who never "
                    "vapes is doing nothing you would notice, so the count "
                    "would be wrong in the same direction."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s02",
        "band": "standard",
        "text": "A study of 500 sixth-formers found that those who drank "
                "energy drinks during study leave scored four marks higher on "
                "average. A classmate says 500 is plenty of people, so the "
                "drink works. What is wrong with that?",
        "options": [
            {"text": "The two groups chose themselves, so their revision "
                     "habits could produce the whole difference.",
             "correct": True},
            {"text": "Four marks is too small a difference to be worth "
                     "anything, whatever the study found.",
             "correct": False,
             "why": "A small difference found in 500 people is still a real "
                    "difference. The trouble is not how big it is but what "
                    "produced it."},
            {"text": "One student who drank them daily and still did badly "
                     "would settle the question.",
             "correct": False,
             "why": "A single case cannot contradict an average, any more "
                    "than one grandad can contradict a risk. An average is a "
                    "claim about many people at once."},
            {"text": "Nothing is wrong — five hundred people is a large "
                     "enough sample to trust the result.",
             "correct": False,
             "why": "Size fixes noise, not confusion. A larger study of two "
                    "groups that chose themselves gives you the same wrong "
                    "answer, measured more precisely."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s03",
        "band": "standard",
        "text": "A trial of a new hay-fever tablet gives half the patients "
                "the tablet and half an identical dummy. Why is the dummy "
                "group there, rather than just measuring everyone before and "
                "after the real tablet?",
        "options": [
            {"text": "To double the number of people studied, which makes any "
                     "result more reliable.",
             "correct": False,
             "why": "It does not add anybody — it splits the same people in "
                    "two. Two groups of fifty beat one group of a hundred "
                    "here because only a comparison shows what the tablet "
                    "added."},
            {"text": "To check that the real tablet tastes no worse than an "
                     "ordinary sugar tablet.",
             "correct": False,
             "why": "The dummy is made to taste identical so that nobody can "
                    "tell which one they took. That is how it works, not what "
                    "it is for."},
            {"text": "Because no measurement counts as a result until it has "
                     "been taken at least twice.",
             "correct": False,
             "why": "Repeating a measurement checks for noise. It cannot tell "
                    "you whether the improvement would have happened anyway, "
                    "and that is the question the dummy group answers."},
            {"text": "Hay fever comes and goes anyway, so people improve with "
                     "no active ingredient.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s04",
        "band": "standard",
        "text": "A herbal capsule and a pharmacy tablet both contain a plant "
                "chemical that genuinely works. Why is the herbal capsule "
                "harder to use safely?",
        "options": [
            {"text": "The plant chemical in it is weaker, so a much larger "
                     "amount has to be taken.",
             "correct": False,
             "why": "Nothing about growing in a field makes a chemical weak — "
                    "the digitalis in foxglove leaves stops a heart at the "
                    "wrong amount. Strength is not the problem; knowing the "
                    "strength is."},
            {"text": "The amount in a leaf varies with plant, season and "
                     "soil, so the dose is unknown.",
             "correct": True},
            {"text": "The capsule is natural, so its effects cannot be "
                     "measured properly in a laboratory.",
             "correct": False,
             "why": "They can be, and they are. Where a molecule grew changes "
                    "nothing about whether it can be studied — it is tested "
                    "the same way as anything else."},
            {"text": "The body breaks a natural chemical down more slowly "
                     "than a factory-made one.",
             "correct": False,
             "why": "The body has no way of telling where a molecule came "
                    "from. It responds to the molecule, and an identical "
                    "molecule behaves identically whether it grew or was "
                    "made."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-03-h01",
        "band": "harder",
        "text": "A school reports that pupils who downloaded its new revision "
                "app scored higher in the summer exams than pupils who did "
                "not. Which single change would let the school say the app "
                "caused the improvement?",
        "options": [
            {"text": "Run the whole thing again with ten times as many pupils "
                     "across the trust.",
             "correct": False,
             "why": "The pupils would still be choosing for themselves, and "
                    "the ones who download a revision app are the ones "
                    "already revising. A bigger study repeats the same "
                    "confusion on a larger scale."},
            {"text": "Split one group of pupils at random into app users and "
                     "non-users, then compare.",
             "correct": True},
            {"text": "Compare the results with a nearby school where the app "
                     "was never offered.",
             "correct": False,
             "why": "That gives you a comparison group, but two schools "
                    "differ in far more than the app. Randomising within one "
                    "group is what strips out the other differences."},
            {"text": "Ask the pupils who downloaded it whether they felt it "
                     "improved their revision.",
             "correct": False,
             "why": "The pupils who chose the app are the likeliest to say "
                    "yes, and how something feels is not the outcome being "
                    "claimed. The claim was about exam scores."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h02",
        "band": "harder",
        "text": "A company pays for a study of its own sports drink. "
                "Volunteers are split at random, the second group gets an "
                "identical drink with the active ingredient left out, the "
                "people measuring the results are not told who drank what, "
                "and the study is published where anyone can read it. Should "
                "you throw the result out because the company paid?",
        "options": [
            {"text": "Yes — evidence from anyone who profits from the answer "
                     "has to be thrown out.",
             "correct": False,
             "why": "Someone who profits from the answer is not disqualified. "
                    "Their evidence needs checking by someone who does not, "
                    "which is a different and much more useful response."},
            {"text": "Yes — a company would never publish a study that went "
                     "against its own product.",
             "correct": False,
             "why": "It might well not, and that is worth knowing. But it is "
                    "a reason to ask what else they measured and never "
                    "published, not a reason to ignore a design you can read "
                    "for yourself."},
            {"text": "No — the design is all that matters, so who paid is "
                     "never worth asking about.",
             "correct": False,
             "why": "Who is telling me is one of the four questions, and it "
                    "is always worth asking. The answer here is that the "
                    "design survives the question, not that the question was "
                    "pointless."},
            {"text": "No — but check the design, and want it repeated by "
                     "someone with nothing to sell.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h03",
        "band": "harder",
        "text": "In 1950 tobacco companies pointed out, correctly, that a "
                "correlation between smoking and lung cancer is not a cause. "
                "Which feature of Doll and Hill's study of around 40,000 "
                "doctors answers that objection?",
        "options": [
            {"text": "Smoking was recorded before anyone fell ill, and the "
                     "same people were followed for decades.",
             "correct": True},
            {"text": "Forty thousand people is a very large number, so the "
                     "result cannot be down to chance.",
             "correct": False,
             "why": "Size fixes noise, not confusion. An enormous study of a "
                    "correlation is still a study of a correlation, and that "
                    "was exactly the objection."},
            {"text": "The doctors were medically trained, so their answers "
                     "about their own health were accurate.",
             "correct": False,
             "why": "Accurate answers help, but a group that chose its own "
                    "smoking still only gives you two things happening "
                    "together. The order in which they were recorded is what "
                    "did the work."},
            {"text": "Smokers died at a higher rate than non-smokers, which "
                     "is what the objection denied.",
             "correct": False,
             "why": "That is the correlation itself, said again. The "
                    "objection never denied the pattern — it said the pattern "
                    "alone cannot name a cause."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h04",
        "band": "harder",
        "text": "Ask a year group to estimate what fraction of them drinks, "
                "smokes or vapes regularly and the average guess comes out "
                "far above the real figure. Beyond simply being wrong, why "
                "does that overestimate matter?",
        "options": [
            {"text": "It does not matter much, because what people believe "
                     "about others cannot change what they do.",
             "correct": False,
             "why": "It can, and this is one of the clearest examples. "
                    "Believing something is normal is one of the strongest "
                    "predictors of starting it."},
            {"text": "It matters because it shows the national surveys of "
                     "pupils must have sampled the wrong people.",
             "correct": False,
             "why": "The national surveys ask tens of thousands of pupils "
                    "chosen at random. The faulty sample is the one in the "
                    "corridor around you — the loud end of the room."},
            {"text": "Believing something is normal predicts starting it, so "
                     "an inaccurate estimate is itself a cause.",
             "correct": True},
            {"text": "It matters because a guess that high shows the real "
                     "figure must be rising quickly.",
             "correct": False,
             "why": "The gap is between the guess and today's figure, not "
                    "between this year's figure and last year's. Every time "
                    "this is measured, in every country, the guess comes out "
                    "too high."},
        ],
        "figure": None,
    },
]
