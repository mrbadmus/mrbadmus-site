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

    # ── MRB-335 top-up ──────────────────────────────────────────────────
    #
    # Thirty-nine rows spread across this lesson's separate ideas rather than
    # across one of them five times: the definition and the three words the
    # lesson runs on, each of the five faults, each of the four questions,
    # the parts of a fair test (comparison group, dummy, randomising,
    # blinding, measuring both groups the same way), the four features of
    # Doll and Hill's design, and the norm-misperception argument. The
    # calculation row is a percentage of a year group, in PUPILS.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b6-03-e05",
        "band": "easier",
        "text": "In a study, what is meant by the sample?",
        "options": [
            {"text": "The result the study is hoping to find.",
             "correct": False,
             "why": "A study does not choose its result in advance. The sample "
                    "is the group of people it actually studied."},
            {"text": "The people actually studied, standing in for the larger "
                     "group being described.",
             "correct": True},
            {"text": "The part of a substance that is tested in a laboratory.",
             "correct": False,
             "why": "That is a sample in a chemistry sense. In a study of "
                    "people, the sample is the people who were studied."},
            {"text": "The number of times the measurement was repeated.",
             "correct": False,
             "why": "Repeating a measurement checks for noise. The sample is "
                    "who was measured, not how often."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e06",
        "band": "easier",
        "text": "What is a comparison group?",
        "options": [
            {"text": "A second study, run by different people, to see whether "
                     "the result repeats.",
             "correct": False,
             "why": "Repeating a study elsewhere is worth doing, but it is not "
                    "what the words mean. A comparison group is inside the "
                    "same study."},
            {"text": "The people who agreed to take part, compared with those "
                     "who refused.",
             "correct": False,
             "why": "Those two groups differ in far more than the thing being "
                    "tested. A comparison group is one that did not get the "
                    "thing, measured the same way."},
            {"text": "The group that reported the strongest effect.",
             "correct": False,
             "why": "Picking out the group with the biggest effect is the "
                    "opposite of comparing fairly. The comparison group is the "
                    "one that did not get the thing."},
            {"text": "The group that did not get the thing being tested, "
                     "measured the same way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e07",
        "band": "easier",
        "text": "One of the four questions to ask about a claim is Compared "
                "with what? What is it asking you to look for?",
        "options": [
            {"text": "The group that did not get the thing.", "correct": True},
            {"text": "Whether a similar product is cheaper elsewhere.",
             "correct": False,
             "why": "The question is about the shape of the evidence, not "
                    "about price. It asks who the study compared its result "
                    "against."},
            {"text": "How the result compares with what people expected.",
             "correct": False,
             "why": "What people expected is not a measurement. The question "
                    "asks for a group that was measured the same way and did "
                    "not get the thing."},
            {"text": "Whether the same claim has been made about another "
                     "substance.",
             "correct": False,
             "why": "Other claims elsewhere do not test this one. The question "
                    "asks what this study's result was compared against."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e08",
        "band": "easier",
        "text": "What do ricin, cyanide and the digitalis in foxglove leaves "
                "have in common?",
        "options": [
            {"text": "All three are made in factories.", "correct": False,
             "why": "All three come from living things rather than from a "
                    "factory. Being natural did not make any of them "
                    "gentle."},
            {"text": "All three are safe in the small amounts found in "
                     "nature.", "correct": False,
             "why": "Amount is what decides, and these are dangerous well "
                    "below the amounts a plant can supply. Being natural says "
                    "nothing about safety."},
            {"text": "All three are natural, and all three are dangerous.",
             "correct": True},
            {"text": "All three are medicines that doctors prescribe today.",
             "correct": False,
             "why": "Digitalis is used as a medicine at a carefully chosen "
                    "amount; ricin and cyanide are not medicines at all. What "
                    "the three share is that they are natural and "
                    "dangerous."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e09",
        "band": "easier",
        "text": "Roughly how many British doctors did Doll and Hill recruit "
                "for their study of smoking?",
        "options": [
            {"text": "Around 400.", "correct": False,
             "why": "Four hundred would be a small study. They recruited "
                    "around 40,000 doctors and followed them for decades."},
            {"text": "Around 40,000.", "correct": True},
            {"text": "Around 400,000.", "correct": False,
             "why": "That is ten times too many. The figure is around 40,000, "
                    "and what made the study powerful was following the same "
                    "people forward."},
            {"text": "Around 40.", "correct": False,
             "why": "Forty people could not have shown a death rate at all. "
                    "The study followed around 40,000 doctors."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e10",
        "band": "easier",
        "text": "One of the four questions to ask about a claim is Who is "
                "telling me? How should evidence from somebody who profits "
                "from the answer be treated?",
        "options": [
            {"text": "Their evidence should be ignored entirely, because "
                     "somebody who profits cannot be trusted.", "correct": False,
             "why": "Ignoring it is too strong. They are not disqualified — "
                    "their evidence needs checking by somebody who does not "
                    "profit."},
            {"text": "Their evidence counts double, because they know the "
                     "product best.", "correct": False,
             "why": "Knowing a product well is not the same as testing it "
                    "fairly. Their evidence needs checking by somebody with "
                    "nothing to sell."},
            {"text": "It makes no difference at all who is telling you the "
                     "answer.", "correct": False,
             "why": "It makes enough difference to be one of the four "
                    "questions. It is a reason to check, rather than a reason "
                    "to dismiss."},
            {"text": "They are not disqualified, but their evidence needs "
                     "checking by someone who does not.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e11",
        "band": "easier",
        "text": "Two things are found to rise at the same time. What is "
                "that pattern worth?",
        "options": [
            {"text": "It is where an investigation starts, not where it "
                     "finishes.", "correct": True},
            {"text": "It proves that one of the two is causing the other.",
             "correct": False,
             "why": "It shows no such thing on its own. Something else may be "
                    "causing both, or the arrow may point the other way."},
            {"text": "It shows the two measurements were taken wrongly.",
             "correct": False,
             "why": "There is nothing faulty about finding a pattern. The "
                    "pattern is a starting point that has still to be "
                    "explained."},
            {"text": "It can safely be ignored, because patterns happen by "
                     "chance.", "correct": False,
             "why": "Chance can produce a pattern, which is one reason to look "
                    "further. Ignoring it is not what a scientist does with "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e12",
        "band": "easier",
        "text": "The paracetamol in a pharmacy is made in a factory. What "
                "makes it safe to use?",
        "options": [
            {"text": "That a factory-made molecule is purer than a natural "
                     "one.", "correct": False,
             "why": "It is purer, but purity is not what makes it safe. Plenty "
                    "of pure factory-made substances will kill you."},
            {"text": "That it comes from a pharmacy rather than from a "
                     "shop.", "correct": False,
             "why": "Where it is sold is not the reason. The reason is that "
                    "every tablet is made to a known dose."},
            {"text": "That it is made to a known dose.", "correct": True},
            {"text": "That a doctor has decided each person may have it.",
             "correct": False,
             "why": "It is sold without a prescription. What makes it safe to "
                    "use is that the amount in each tablet is known."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e13",
        "band": "easier",
        "text": "Which of these counts as substance misuse?",
        "options": [
            {"text": "Being given a medicine in hospital by a nurse.",
             "correct": False,
             "why": "That is a medicine being used to treat somebody, which is "
                    "the ordinary use of a drug. Misuse is use that damages "
                    "health."},
            {"text": "Taking a medicine that was prescribed for somebody "
                     "else.", "correct": True},
            {"text": "Taking a prescribed medicine exactly as the label says.",
             "correct": False,
             "why": "Following the label is the medicine being used as it was "
                    "meant to be. Misuse is use that damages health, whatever "
                    "the substance."},
            {"text": "Buying a medicine from a pharmacy without a "
                     "prescription.", "correct": False,
             "why": "Many medicines are sold that way, with a dose limit on "
                    "the box. Buying one is not misuse; using one in a way "
                    "that damages health is."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e14",
        "band": "easier",
        "text": "When scientists talk about the risk from a substance, what "
                "is a risk a statement about?",
        "options": [
            {"text": "What will certainly happen to anyone who uses it.",
             "correct": False,
             "why": "A risk is not a certainty. It says how often something "
                    "happens, which is why some people are unharmed and the "
                    "risk is still real."},
            {"text": "How dangerous a substance feels to the person taking "
                     "it.", "correct": False,
             "why": "How something feels is not a measurement. A risk is "
                    "counted across many people."},
            {"text": "Whether a substance is legal to buy in this country.",
             "correct": False,
             "why": "Legality is a decision a parliament makes. A risk is a "
                    "number about how often harm happens."},
            {"text": "How often something happens across many people.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e15",
        "band": "easier",
        "text": "National surveys ask tens of thousands of pupils about "
                "regular drinking, smoking and vaping. What do they "
                "consistently find at this age?",
        "options": [
            {"text": "That regular use is in a clear minority.",
             "correct": True},
            {"text": "That regular use is what most pupils do.",
             "correct": False,
             "why": "That is the guess pupils make, not the figure the surveys "
                    "find. Regular use is in a clear minority."},
            {"text": "That the figure is exactly what pupils themselves "
                     "estimate.", "correct": False,
             "why": "The average guess comes out far above the real figure, "
                    "every time it is measured. The two do not agree."},
            {"text": "That the figure cannot be measured, because pupils will "
                     "not answer.", "correct": False,
             "why": "It is measured, in tens of thousands of pupils chosen at "
                    "random. What it shows is that regular use is a clear "
                    "minority."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e16",
        "band": "easier",
        "text": "The word safe is incomplete on its own. What has to be "
                "attached to it before it means anything?",
        "options": [
            {"text": "The name of the country where it is legal.",
             "correct": False,
             "why": "What a shop may sell is a fact about the law, not about a "
                    "body. Safe needs an amount attached to it."},
            {"text": "The name of the company that tested it.",
             "correct": False,
             "why": "Who tested it is worth knowing, and it is one of the four "
                    "questions. But the word safe itself needs an amount."},
            {"text": "An amount — safe at what dose, for how long, for whom.",
             "correct": True},
            {"text": "The number of people who have used it without harm.",
             "correct": False,
             "why": "People survive dangerous things all the time, so a count "
                    "of them settles nothing. Safe needs an amount attached."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-e17",
        "band": "easier",
        "text": "In a trial, what does splitting people into two groups at "
                "random achieve?",
        "options": [
            {"text": "It makes the study larger, which makes any result more "
                     "reliable.", "correct": False,
             "why": "Splitting adds nobody — it divides the same people in "
                    "two. What randomising does is stop the groups differing "
                    "in other ways."},
            {"text": "It breaks the link between the thing being tested and "
                     "everything else about the person.", "correct": True},
            {"text": "It makes sure the two groups contain exactly the same "
                     "people.", "correct": False,
             "why": "They are different people, necessarily. Randomising means "
                    "the differences between them are not lined up with the "
                    "thing being tested."},
            {"text": "It lets the researchers put the keenest volunteers in "
                     "the treatment group.", "correct": False,
             "why": "Choosing who goes where is exactly what randomising "
                    "prevents. If the keen ones are all in one group, that is "
                    "what the study ends up measuring."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b6-03-s05",
        "band": "standard",
        "text": "A report finds that towns with more vape shops have more "
                "young people who vape. A councillor says the shops are "
                "causing it. How good is that reasoning?",
        "options": [
            {"text": "Sound enough — a shop cannot sell a vape to somebody who "
                     "never walks into it.", "correct": False,
             "why": "That is an argument for the shops mattering, not "
                    "evidence that they do. The figures on their own cannot "
                    "say which way the arrow points."},
            {"text": "The figures must be wrong, because vaping happens "
                     "everywhere equally.", "correct": False,
             "why": "There is no reason to doubt the counting. The fault is in "
                    "what is being read into it."},
            {"text": "Two things happening together does not show which "
                     "caused which, or whether something else caused both.",
             "correct": True},
            {"text": "The study is too small to be worth anything.",
             "correct": False,
             "why": "Nothing here says how many towns were counted, and more "
                    "towns would not settle it. Size fixes noise, not "
                    "confusion."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s06",
        "band": "standard",
        "text": "A company tests its new energy gel only on people who "
                "volunteered because they already used and liked it. Why is "
                "that a problem?",
        "options": [
            {"text": "The people tested chose themselves, so the result "
                     "describes them rather than anyone else.",
             "correct": True},
            {"text": "Volunteers cannot be trusted to report accurately what "
                     "they actually felt.", "correct": False,
             "why": "Assume every one of them answered honestly. The fault is "
                    "still there, because of how they came to be in the study "
                    "at all."},
            {"text": "The company should have tested more people before "
                     "publishing anything.", "correct": False,
             "why": "More people chosen the same way gives the same wrong "
                    "answer, measured more precisely. Size fixes noise, not "
                    "confusion."},
            {"text": "A company is not allowed to test its own product.",
             "correct": False,
             "why": "It is allowed to, and often does. Somebody who profits "
                    "from the answer is not disqualified — the design is what "
                    "has to be checked."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s07",
        "band": "standard",
        "text": "In a good trial, the people measuring the results are not "
                "told which patients took the real tablet. Why does that "
                "matter?",
        "options": [
            {"text": "Because they might tell the patients, who would then "
                     "improve on their own.", "correct": False,
             "why": "Keeping it from the patients matters too, and that is why "
                    "the dummy is identical. This rule is about the person "
                    "doing the measuring."},
            {"text": "Because a measurement takes longer when the measurer "
                     "knows what to expect.", "correct": False,
             "why": "Speed is not the issue. The issue is that expecting an "
                    "improvement can change how a borderline result is "
                    "recorded."},
            {"text": "Because otherwise they would have to be paid more for "
                     "the extra responsibility.", "correct": False,
             "why": "This is a question about the design of the study, not "
                    "about who is paid. Not knowing keeps expectation out of "
                    "the measurement."},
            {"text": "Because somebody expecting an improvement can read one "
                     "into a borderline measurement.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s08",
        "band": "standard",
        "text": "Someone argues that a substance must be safe because people "
                "have used it for thousands of years. What does long use "
                "actually tell you?",
        "options": [
            {"text": "That it must be safe, since a dangerous substance would "
                     "have been abandoned.", "correct": False,
             "why": "Tobacco has been used for centuries and is not safe. "
                    "Long use is a fact about people's habits, not about a "
                    "body."},
            {"text": "That it does not kill most people quickly — a much "
                     "weaker claim than safe.", "correct": True},
            {"text": "Nothing whatever, because nobody kept records that far "
                     "back.", "correct": False,
             "why": "It does tell you something, just far less than is being "
                    "claimed: harm that is slow or uncommon would go unnoticed "
                    "for centuries."},
            {"text": "That the harms it causes must be natural ones, which the "
                     "body can handle.", "correct": False,
             "why": "The body has no way of telling where a molecule came "
                    "from. Deadly nightshade has been known for centuries and "
                    "the body handles it no better for that."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s09",
        "band": "standard",
        "text": "Why do you hear far more often from people who used something "
                "risky and came to no harm than from those who did not?",
        "options": [
            {"text": "Because harm from most substances is extremely rare.",
             "correct": False,
             "why": "How rare the harm is has not been established here, and "
                    "it is not the reason. The people who were harmed are not "
                    "the ones telling you their story."},
            {"text": "Because people who were harmed are less likely to be "
                     "believed.", "correct": False,
             "why": "It is not about belief. Many of them are simply not there "
                    "to tell you, which is why the stories you hear are "
                    "one-sided."},
            {"text": "Because those who came to no harm are the ones still "
                     "around to tell you.", "correct": True},
            {"text": "Because a story about being unharmed is more "
                     "interesting to listen to.", "correct": False,
             "why": "How interesting a story is does not decide which stories "
                    "exist. The survivors are the ones available to be "
                    "asked."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s10",
        "band": "standard",
        "text": "A headline reads: Study links energy drinks to poor sleep. "
                "Which word tells you no cause has been shown?",
        "options": [
            {"text": "Links — it says the two go together and nothing more.",
             "correct": True},
            {"text": "Study — a study is only ever somebody's opinion.",
             "correct": False,
             "why": "A study is a measurement, not an opinion. It is the word "
                    "links that stops short of naming a cause."},
            {"text": "Poor — because poor sleep is a feeling rather than a "
                     "measurement.", "correct": False,
             "why": "Sleep can be measured, in a laboratory or with a diary. "
                    "The word that avoids claiming a cause is links."},
            {"text": "Energy — because the drinks do not really supply any "
                     "energy.", "correct": False,
             "why": "What is in the tin is a separate question. The word "
                    "carrying the caution in this headline is links."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s11",
        "band": "standard",
        "text": "Two studies disagree about a drink. One surveyed 20,000 "
                "customers who chose to answer. The other split 60 volunteers "
                "at random into two groups. Which is better evidence?",
        "options": [
            {"text": "The survey, because 20,000 people cannot all be "
                     "wrong.", "correct": False,
             "why": "They can all be unrepresentative in the same direction, "
                    "because they chose themselves. Size fixes noise, not "
                    "confusion."},
            {"text": "The survey, because customers have actually used the "
                     "product.", "correct": False,
             "why": "Being a customer is exactly what makes them an unfair "
                    "sample. It is the people who never bought it who are "
                    "missing."},
            {"text": "Neither, because a result can only be trusted when "
                     "both kinds of study agree.", "correct": False,
             "why": "Studies disagreeing is ordinary, and the way through is "
                    "to judge the designs. Sixty people split at random can "
                    "show a real difference."},
            {"text": "The trial of 60, because randomising removes the "
                     "differences that the survey cannot.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s12",
        "band": "standard",
        "text": "A study measured 40,000 people who all took a supplement, and "
                "found that most of them felt better. Which of the four "
                "questions does it most obviously fail?",
        "options": [
            {"text": "How many, and who? — 40,000 is too few for a claim about "
                     "everybody.", "correct": False,
             "why": "Forty thousand is a large number of people. What is "
                    "missing is anybody to compare them against."},
            {"text": "Compared with what? — nobody in the study went "
                     "without, so there is nothing to compare.",
             "correct": True},
            {"text": "Who is telling me? — a study this large must have been "
                     "paid for by somebody.", "correct": False,
             "why": "That is worth asking, and the answer is not given here. "
                    "The fault you can see from what you are told is the "
                    "missing comparison group."},
            {"text": "Together, or because? — feeling better and taking a "
                     "supplement are two separate things.", "correct": False,
             "why": "You cannot even reach that question yet. With no group "
                    "that went without, there is nothing to say the "
                    "supplement did anything at all."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s13",
        "band": "standard",
        "text": "You want to know what fraction of a year group of 240 pupils "
                "vapes. Which of these is the fairest sample?",
        "options": [
            {"text": "Everybody standing outside the gate at the end of the "
                     "day.", "correct": False,
             "why": "That group chose itself, and vapers are far more likely "
                    "to be in it. It is the loud end of the room, not a "
                    "sample."},
            {"text": "The 30 people in your form and friendship group.",
             "correct": False,
             "why": "Friends are like one another, which is what makes them "
                    "friends. A friendship group is not a random slice of a "
                    "year."},
            {"text": "Fifty pupils picked at random from the whole year "
                     "register.", "correct": True},
            {"text": "Everybody who volunteers to fill in the survey.",
             "correct": False,
             "why": "The people who volunteer differ from those who do not, "
                    "and on this question they may differ in exactly the way "
                    "being measured."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s14",
        "band": "standard",
        "text": "A painkilling chemical was first found in tree bark and is "
                "now made in a factory. A pupil says the factory version must "
                "be a different, harsher substance. Is that right?",
        "options": [
            {"text": "No — an identical molecule behaves identically, however "
                     "it was produced.", "correct": True},
            {"text": "Yes — the factory version is stronger, because it has "
                     "been concentrated.", "correct": False,
             "why": "A known amount per tablet is not the same as a harsher "
                    "molecule. The molecule is the same one, and the amount is "
                    "the part that is now known."},
            {"text": "Yes — the body recognises a molecule that grew and "
                     "treats it more gently.", "correct": False,
             "why": "The body has no way of telling where a molecule came "
                    "from. It responds to the molecule in front of it."},
            {"text": "No — but only because the bark version was too weak to "
                     "do anything.", "correct": False,
             "why": "The bark version worked, which is how the chemical was "
                    "found. The point is that the same molecule does the same "
                    "thing either way."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s15",
        "band": "standard",
        "text": "One study asks people with poor sleep to remember how many "
                "energy drinks they had last year. Another records what people "
                "drink now and follows them forward. Why is the second "
                "better?",
        "options": [
            {"text": "Because following people forward always takes more "
                     "people, and more people is better.", "correct": False,
             "why": "It need not take more people at all. What it changes is "
                    "when the information was recorded."},
            {"text": "Because people who already have a problem look for "
                     "something to blame it on.", "correct": False,
             "why": "Nobody has to be dishonest for the first study to fail. "
                    "Remembering a year of habits is simply unreliable, "
                    "whoever is doing it."},
            {"text": "Because the first study measures sleep and the second "
                     "measures drinks.", "correct": False,
             "why": "Both measure both. The difference is that one records the "
                    "drinking before anything has gone wrong."},
            {"text": "Because what people drank was recorded before anyone "
                     "became unwell, rather than remembered afterwards.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s16",
        "band": "standard",
        "text": "In a trial of a reaction-time drink, one group is tested "
                "first thing in the morning and the other at the end of the "
                "school day. How good is that design?",
        "options": [
            {"text": "Sound, so long as both groups were the same size.",
             "correct": False,
             "why": "Equal sizes do not help when the two groups were "
                    "measured under different conditions. Tiredness alone "
                    "could produce the whole difference."},
            {"text": "More than one thing now differs between the groups, so "
                     "the drink cannot be blamed for the result.",
             "correct": True},
            {"text": "Reaction time cannot be measured in a school, so neither "
                     "result counts.", "correct": False,
             "why": "It can be measured perfectly well in a school. The fault "
                    "is that the two groups were not measured under the same "
                    "conditions."},
            {"text": "The morning group will always do worse, so the result is "
                     "the wrong way round.", "correct": False,
             "why": "Which group does better is not the point, and it is not "
                    "known. The point is that time of day and the drink are "
                    "now tangled together."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-s17",
        "band": "standard",
        "text": "A label says the product contains no chemicals, only natural "
                "ingredients. Judge that sentence.",
        "options": [
            {"text": "It is right: natural ingredients and chemicals really "
                     "are different things.", "correct": False,
             "why": "They are not. Every substance in the world is a "
                    "chemical, including the water you drank at break."},
            {"text": "It is wrong only if the product turns out to contain "
                     "something factory-made.", "correct": False,
             "why": "The sentence fails whatever is inside. Natural "
                    "ingredients are chemicals too."},
            {"text": "Everything is a chemical, so the claim says nothing "
                     "about what the product does.", "correct": True},
            {"text": "It is wrong because natural ingredients are usually more "
                     "dangerous than factory-made ones.", "correct": False,
             "why": "Neither origin is more dangerous as a rule. Origin tells "
                    "you nothing at all about effect, in either direction."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b6-03-h05",
        "band": "harder",
        "text": "In Doll and Hill's study the death rate climbed with the "
                "number of cigarettes, and fell in the doctors who stopped. "
                "Why do those two findings strengthen the case beyond a "
                "pattern?",
        "options": [
            {"text": "Because they show the study was large enough for the "
                     "result to be reliable.", "correct": False,
             "why": "Size is a separate matter, and it was never the "
                    "objection. These two findings are about the shape of the "
                    "result rather than the number of people."},
            {"text": "More of the suspected cause gives more of the effect, "
                     "and removing it reduces the effect.", "correct": True},
            {"text": "Because they show that doctors are more honest about "
                     "smoking than other people.", "correct": False,
             "why": "Honesty was not what made the study work. What made it "
                    "work was the pattern responding to how much was smoked "
                    "and to stopping."},
            {"text": "Because they rule out the possibility that anybody "
                     "misremembered what they smoked.", "correct": False,
             "why": "Recording the smoking beforehand is what dealt with "
                    "memory. These two findings do something different: they "
                    "show the effect tracking the cause."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h06",
        "band": "harder",
        "text": "A year group of 240 pupils guesses that 60% of them vape "
                "regularly. A national survey puts the real figure at 5%. How "
                "many pupils does each figure mean, and how big is the gap?",
        "options": [
            {"text": "60 pupils against 5 pupils — a gap of 55 pupils.",
             "correct": False,
             "why": "A percentage is not a count. Sixty per cent of 240 is "
                    "144 pupils, and 5% of 240 is 12."},
            {"text": "144 pupils against 12 pupils — a gap of 156 pupils.",
             "correct": False,
             "why": "Both figures are right, but the gap between them is found "
                    "by subtracting: 144 − 12 = 132 pupils."},
            {"text": "144 pupils against 12 pupils — a gap of 132 pupils.",
             "correct": True},
            {"text": "144 pupils against 5 pupils — a gap of 139 pupils.",
             "correct": False,
             "why": "The first figure was converted to pupils and the second "
                    "was left as a percentage. Five per cent of 240 is 12 "
                    "pupils."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h07",
        "band": "harder",
        "text": "A trial is large, splits people at random, and uses an "
                "identical dummy — but the staff measuring the results were "
                "told who took which. How much does that one fault cost?",
        "options": [
            {"text": "Enough to weaken the result, because expectation can "
                     "shape a borderline measurement.", "correct": True},
            {"text": "Nothing, because randomising has already removed every "
                     "difference between the groups.", "correct": False,
             "why": "Randomising deals with differences between the people, "
                    "not with the person recording the outcome. That is a "
                    "separate hole."},
            {"text": "Nothing, provided the patients themselves did not "
                     "know.", "correct": False,
             "why": "Keeping it from the patients handles their expectations. "
                    "It does nothing about the expectations of the person "
                    "writing the result down."},
            {"text": "Everything — a study with any fault at all tells you "
                     "nothing whatever.", "correct": False,
             "why": "That is too strong. A study is judged by its design, and "
                    "one weakness makes a result less secure rather than "
                    "worthless."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h08",
        "band": "harder",
        "text": "A supplement company answers its critics by pointing out that "
                "those critics are paid by a rival company. How should you "
                "treat the two sides?",
        "options": [
            {"text": "Believe the critics, because attacking a product is "
                     "harder than defending one.", "correct": False,
             "why": "Which side is harder to argue is not evidence. Both sides "
                    "have something to gain, so both designs need reading."},
            {"text": "Believe the company, because it knows its own product "
                     "best.", "correct": False,
             "why": "Knowing a product is not the same as testing it fairly. "
                    "The company profits from one answer, which is a reason to "
                    "check its evidence."},
            {"text": "Ignore both, because everybody involved has something to "
                     "gain.", "correct": False,
             "why": "Ignoring evidence you can read is not the scientific "
                    "move. Somebody who profits is not disqualified — their "
                    "evidence needs checking."},
            {"text": "Read both designs, and look for the question settled by "
                     "somebody with nothing to sell.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h09",
        "band": "harder",
        "text": "Someone argues that a legal substance must be safer than an "
                "illegal one, because a country would not allow the dangerous "
                "one to be sold. What is wrong with that?",
        "options": [
            {"text": "Nothing — a government would not permit something known "
                     "to be harmful.", "correct": False,
             "why": "Alcohol and tobacco are legal here and between them cause "
                    "more illness than every illegal drug combined. Legality "
                    "is not a measure of harm."},
            {"text": "Legality says what a shop may sell; it is not evidence "
                     "about what a substance does.", "correct": True},
            {"text": "It is wrong because illegal substances are always the "
                     "safer of the two.", "correct": False,
             "why": "That is the same mistake stood on its head. Neither "
                    "legality nor illegality tells you what a substance does "
                    "to a body."},
            {"text": "It is wrong only for substances that were legal in the "
                     "past and are not now.", "correct": False,
             "why": "The argument fails whatever the law has done. What a "
                    "molecule does to a body does not change when a "
                    "parliament votes."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h10",
        "band": "harder",
        "text": "A school surveys its former pupils, asking how useful its "
                "revision advice was. Almost all say it was excellent. Who is "
                "missing from that survey?",
        "options": [
            {"text": "Nobody — every former pupil had the chance to "
                     "answer.", "correct": False,
             "why": "Having the chance and taking it are different things. The "
                    "people who answer a school's survey are the ones who "
                    "stayed in touch and got on well."},
            {"text": "The pupils who are still at the school and have not sat "
                     "the exams.", "correct": False,
             "why": "They are not part of the claim, which is about former "
                    "pupils. The gap is among the former pupils who did not "
                    "reply."},
            {"text": "Those who did badly, left early or lost touch — the ones "
                     "least likely to reply.", "correct": True},
            {"text": "The teachers, whose view of the advice was never "
                     "asked.", "correct": False,
             "why": "The claim is about pupils, so teachers are not the "
                    "missing group. The people missing are the pupils who did "
                    "not answer."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h11",
        "band": "harder",
        "text": "A survey finds that pupils with a part-time job are more "
                "likely to smoke. A newspaper says part-time work leads to "
                "smoking. What is the most likely fault?",
        "options": [
            {"text": "Something else, such as being older, could raise both "
                     "the job and the smoking.", "correct": True},
            {"text": "The survey must have asked too few pupils to say "
                     "anything.", "correct": False,
             "why": "Nothing here says how many were asked, and a bigger "
                    "survey would repeat the same confusion. Size fixes noise, "
                    "not confusion."},
            {"text": "Pupils with jobs would not admit to smoking, so the "
                     "figure is too low.", "correct": False,
             "why": "That would make the pattern weaker, not explain it. The "
                    "fault is that a third thing may be behind both."},
            {"text": "The survey should have asked adults as well, to see "
                     "whether the pattern holds.", "correct": False,
             "why": "Adults are not who the claim is about. The fault is that "
                    "two things going together does not name a cause."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h12",
        "band": "harder",
        "text": "A claim survives all four questions: a fair sample, a "
                "comparison group, no seller involved, and a design that "
                "shows a cause. Does that make it true?",
        "options": [
            {"text": "Yes — a claim that passes every test cannot later turn "
                     "out to be wrong.", "correct": False,
             "why": "Evidence can be overturned by better evidence, which is "
                    "how science works. Passing the four questions makes a "
                    "claim worth believing, not permanent."},
            {"text": "No — passing the tests tells you nothing, because the "
                     "next study may disagree.", "correct": False,
             "why": "That is too far the other way. A well-designed study is "
                    "much better evidence than a badly designed one, even "
                    "though it is not the last word."},
            {"text": "Yes, provided the study was large enough as well as well "
                     "designed.", "correct": False,
             "why": "Size helps with noise, and it is worth having. It still "
                    "does not turn a well-supported claim into a permanent "
                    "one."},
            {"text": "It makes it the best answer available, and worth "
                     "repeating by somebody else.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h13",
        "band": "harder",
        "text": "Nobody could test whether smoking causes lung cancer by "
                "splitting people at random and asking half of them to smoke. "
                "How did Doll and Hill answer the question without doing "
                "that?",
        "options": [
            {"text": "They asked people who already had lung cancer what they "
                     "had smoked.", "correct": False,
             "why": "That study would depend on memory and on ill people "
                    "looking for a cause. They recorded the smoking first "
                    "instead."},
            {"text": "They recorded what people already smoked, then followed "
                     "the same people forward for decades.", "correct": True},
            {"text": "They compared one country where smoking was common with "
                     "another where it was rare.", "correct": False,
             "why": "Two countries differ in far more than their smoking. "
                    "Following the same people forward is what removed those "
                    "differences."},
            {"text": "They tested tobacco smoke on cells in a laboratory "
                     "instead of on people.", "correct": False,
             "why": "Laboratory work supports the case, but it was not their "
                    "study. Theirs followed around 40,000 doctors forward for "
                    "decades."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h14",
        "band": "harder",
        "text": "Adding more people to a study genuinely fixes one kind of "
                "problem and not another. Which is which?",
        "options": [
            {"text": "It fixes a seller choosing the reviews, but not a small "
                     "difference between the groups.", "correct": False,
             "why": "Adding more people chosen by the seller adds more of the "
                    "same bias. Numbers do nothing about who was allowed into "
                    "the study."},
            {"text": "It fixes a missing comparison group, because a large "
                     "enough group compares with itself.", "correct": False,
             "why": "No group compares with itself. Without people who went "
                    "without, there is nothing to measure the effect "
                    "against."},
            {"text": "It fixes random variation between people, but not "
                     "groups that chose themselves.", "correct": True},
            {"text": "It fixes nothing at all, which is why the size of a "
                     "study never matters.", "correct": False,
             "why": "Size does matter: a small study can show a difference "
                    "that was only chance. What it cannot repair is a sample "
                    "that chose itself."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h15",
        "band": "harder",
        "text": "Somebody takes a medicine exactly as the label says and is "
                "still harmed by an effect on another organ. Is that substance "
                "misuse?",
        "options": [
            {"text": "No — the medicine was used as intended; that harm is a "
                     "side effect.", "correct": True},
            {"text": "Yes, because misuse means any use that ends in harm.",
             "correct": False,
             "why": "Misuse is using a substance in a way that damages health. "
                    "Following the label is not that, even when an unwanted "
                    "effect follows."},
            {"text": "Yes, because the person should have known their own body "
                     "better.", "correct": False,
             "why": "Nothing about the person's judgement is at issue. The "
                    "blood carries a drug to every organ, so effects "
                    "elsewhere are expected."},
            {"text": "No, because a licensed medicine cannot cause harm at "
                     "all.", "correct": False,
             "why": "It can — every drug that works has effects elsewhere. "
                    "The reason this is not misuse is that the medicine was "
                    "used as intended."},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h16",
        "band": "harder",
        "text": "In a trial of a hay-fever tablet, a good number of the dummy "
                "group improved as well. What does that show?",
        "options": [
            {"text": "That the dummy must have contained some of the active "
                     "ingredient by mistake.", "correct": False,
             "why": "A dummy has the active ingredient left out; that is what "
                    "makes it a dummy. People improve without it because the "
                    "condition varies anyway."},
            {"text": "That the trial has failed and will have to be run "
                     "again.", "correct": False,
             "why": "It has not failed — it has done its job. The dummy group "
                    "improving is exactly the information the comparison "
                    "exists to supply."},
            {"text": "That hay fever cannot be treated, since people get "
                     "better either way.", "correct": False,
             "why": "Some improved without treatment, which is not the same "
                    "as nobody being helped. The question is how much more "
                    "the tablet group improved."},
            {"text": "That improvement happens anyway, which is why the "
                     "comparison was needed at all.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b6-03-h17",
        "band": "harder",
        "text": "An advert claims a product is safe because it comes from a "
                "plant eaten for centuries, and because nine in ten of the "
                "people it asked said they felt better. How many separate "
                "faults is that?",
        "options": [
            {"text": "One — the reviews are the only real evidence offered, "
                     "and they are weak.", "correct": False,
             "why": "The plant half is offered as evidence too, and it fails "
                    "on its own account: where a molecule came from says "
                    "nothing about what it does."},
            {"text": "One — both halves are the same mistake of trusting the "
                     "seller.", "correct": False,
             "why": "Only the reviews come from the seller. The claim about "
                    "the plant is a different fault: origin is not evidence "
                    "about effect."},
            {"text": "Two — origin is not evidence about effect, and the "
                     "reviews have nobody to compare against.", "correct": True},
            {"text": "None — long use and satisfied customers are two "
                     "independent kinds of evidence.", "correct": False,
             "why": "Two weak arguments do not add up to a strong one. Neither "
                    "half tells you what the product does to a body."},
        ],
        "figure": None,
    },
]
