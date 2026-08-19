"""B9 lesson 06 — Sampling an ecosystem: twelve questions (MRB-269).

These probe the one sentence the lesson exists to establish: that bias and
sample size are independent problems, and only one of them yields to more
work. The distractors are built from the lesson's two declared misconceptions
— ECO-11 (throwing the quadrat over your shoulder makes the placement random)
and NOS-04 (a large sample is an accurate sample) — and from the beliefs the
bench's three settings exist to break: that a bigger sample rescues a crooked
one, that two biased surveys in opposite directions average out, that
agreement between surveys is evidence of accuracy, and that using random
numbers inside an area you chose by eye makes the sample random. Three more
come from the lesson's own careful wording: that random means chosen by a
process with no preferences rather than chosen without thinking, that a zero
count is a result and not a missing measurement, and that a quadrat too small
for the organism gives an unsteady estimate rather than a leaning one. The
`harder` band takes the rule somewhere the page never goes — a
capture–mark–recapture estimate pushed the wrong way by trap-shy mice, a
council counting trees beside the car parks, oaks counted in a daisy quadrat,
and the honest question of what you can check when there is no real total to
press for.
"""

UNIT = "B9"
LESSON = "sampling-an-ecosystem"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-e01",
        "band": "easier",
        "text": "The lesson is careful about what the word random means in "
                "science. Which of these is a random sample?",
        "options": [
            {"text": "One where nobody planned the positions, so nothing "
                     "about the choice was deliberate.",
             "correct": False,
             "why": "Random means chosen by a process with no preferences, "
                    "not chosen without thinking. Someone not thinking still "
                    "avoids the brambles and drifts away from the hedge."},
            {"text": "One where the positions came from a process with no "
                     "preferences, such as pairs of random numbers.",
             "correct": True},
            {"text": "One where the quadrats are spaced evenly across the "
                     "site so that no part of it is missed.",
             "correct": False,
             "why": "Even spacing is a pattern you chose, so it is not a "
                    "random sample. The positions came from your rule rather "
                    "than from chance."},
            {"text": "One where the person holding the quadrat decides each "
                     "position on the spot, quickly.",
             "correct": False,
             "why": "You are still choosing, and a human trying to be random "
                    "is one of the more reliably biased instruments "
                    "available."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e02",
        "band": "easier",
        "text": "Two things can go wrong with a quadrat survey, and only one "
                "of them gets better if you take more quadrats. Which one?",
        "options": [
            {"text": "Placing every quadrat in the part of the field where "
                     "the flowers look best.",
             "correct": False,
             "why": "That is bias. Every extra quadrat is drawn the same "
                    "crooked way, so it repeats the error instead of diluting "
                    "it."},
            {"text": "Deciding which part of the field to sample after "
                     "walking round and looking at it.",
             "correct": False,
             "why": "Also bias — the area was chosen by eye, so random "
                    "numbers used inside it cannot rescue the sample. More "
                    "quadrats simply repeat it."},
            {"text": "Three quadrats happening to land on bare ground, so "
                     "the mean per quadrat comes out low.",
             "correct": True},
            {"text": "Using a quadrat far too small for the organism you "
                     "have been asked to count.",
             "correct": False,
             "why": "The size has to suit the organism, and that is settled "
                    "before you start. Taking more quadrats does not make a "
                    "frame the right size."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e03",
        "band": "easier",
        "text": "Halfway through a survey, two students disagree about a "
                "daisy lying half inside and half outside the frame. What "
                "should the class have done?",
        "options": [
            {"text": "Agreed one rule for plants on the line before starting "
                     "— usually count two sides and not the others.",
             "correct": True},
            {"text": "Let each person decide as they go, because over a whole "
                     "survey the differences even out.",
             "correct": False,
             "why": "They do not even out. Different people using different "
                    "rules is a difference in method, not chance, and the "
                    "counts stop being comparable."},
            {"text": "Counted every plant the frame touches, so that nothing "
                     "inside the square gets missed.",
             "correct": False,
             "why": "Counting all four edges adds every boundary plant to the "
                    "count. That inflates each quadrat, and the mean is then "
                    "scaled up across the whole site."},
            {"text": "Moved the frame slightly so that no plant was left "
                     "lying on the line.",
             "correct": False,
             "why": "Moving the frame to make counting easier is choosing "
                    "where to look, which is exactly the preference random "
                    "placement exists to remove."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e04",
        "band": "easier",
        "text": "Which of these actually gives a random placement of quadrats "
                "on a school field?",
        "options": [
            {"text": "Throw the quadrat over your shoulder and count whatever "
                     "ends up inside it.",
             "correct": False,
             "why": "Throwing is unpredictable, which is not the same thing. "
                    "You throw further on open grass, away from the hedge and "
                    "downhill more easily than up — and it is unsafe with a "
                    "metal frame."},
            {"text": "Walk out across the field and put the quadrat down "
                     "whenever you feel like stopping.",
             "correct": False,
             "why": "You are choosing every position, and every one of those "
                    "choices carries a preference — open ground over "
                    "brambles, flat over steep."},
            {"text": "Look for the squares that seem typical of the field as "
                     "a whole and count those.",
             "correct": False,
             "why": "Typical is a judgement you made by eye, so the sample is "
                    "only as good as your guess about the field — which is "
                    "the thing you set out to measure."},
            {"text": "Lay two tape measures at right angles and place a "
                     "quadrat wherever each random number pair lands.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-06-s01",
        "band": "standard",
        "text": "Turning the bench's dial from three quadrats up to "
                "twenty-five improves the estimate on one setting only. "
                "Which setting, and why?",
        "options": [
            {"text": "The flowery corner, because twenty-five is a large "
                     "enough sample to be accurate.",
             "correct": False,
             "why": "Sample size does nothing to bias. All twenty-five "
                    "squares still come from the richest part of the field, "
                    "so the mean still describes that corner."},
            {"text": "The path edge, because the extra quadrats reach out "
                     "beyond the trampled ground.",
             "correct": False,
             "why": "The path-edge setting keeps drawing from the same "
                    "trampled strip however many quadrats you take. The dial "
                    "does not send them anywhere else."},
            {"text": "Random coordinates, because the placement is already "
                     "fair, so the only error left is chance.",
             "correct": True},
            {"text": "All three, because more quadrats always bring an "
                     "estimate closer to the true total.",
             "correct": False,
             "why": "That is the belief this bench exists to break. More "
                    "quadrats shrink chance error and leave bias exactly "
                    "where it was."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s02",
        "band": "standard",
        "text": "One group surveys only the flowery corner and estimates "
                "1,900 daisies. Another surveys only the path edge and "
                "estimates 700. They average the two and report 1,300. What "
                "is wrong with that?",
        "options": [
            {"text": "Nothing made the two errors equal and opposite, so the "
                     "average is just a third wrong number.",
             "correct": True},
            {"text": "Nothing is wrong — averaging two estimates cancels out "
                     "the bias in each of them.",
             "correct": False,
             "why": "Bias would only cancel if the two errors happened to be "
                    "the same size in opposite directions, and nothing "
                    "arranged that. Both surveys are still crooked."},
            {"text": "They should have added the two estimates, since each "
                     "group covered a different part of the field.",
             "correct": False,
             "why": "Each group already scaled its mean up to the whole "
                    "field, so each number is a whole-field estimate. Adding "
                    "them gives you roughly two fields."},
            {"text": "They should report 1,900, because the corner shows how "
                     "many daisies the field can hold.",
             "correct": False,
             "why": "The corner's mean describes the corner, not the field. "
                    "That is exactly why the corner setting comes out far too "
                    "high."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s03",
        "band": "standard",
        "text": "A group walks the whole field first, decides one end looks "
                "most representative, then uses random numbers to place ten "
                "quadrats inside that end. Is their sample random?",
        "options": [
            {"text": "Yes — they used random numbers, and that is what makes "
                     "a placement random.",
             "correct": False,
             "why": "The random numbers only made the placement fair inside "
                    "an area you had already chosen by eye. The choosing "
                    "happened one step earlier, and that is where the bias "
                    "got in."},
            {"text": "Yes, as long as they take enough quadrats to cover that "
                     "end of the field properly.",
             "correct": False,
             "why": "More quadrats inside a chosen area repeat the same "
                    "error. Sample size never touches bias, wherever in the "
                    "method the bias came from."},
            {"text": "No — ten quadrats is far too few to say anything about "
                     "a whole school field.",
             "correct": False,
             "why": "Too few quadrats is a real problem, but a different one: "
                    "it makes an estimate wobble rather than lean. Here the "
                    "error is where they chose to look."},
            {"text": "No — the area was chosen by looking, so the sample is "
                     "biased however the quadrats fell inside it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s04",
        "band": "standard",
        "text": "Six 1 m² quadrats are placed at random on a 400 m² field. "
                "The counts are 4, 0, 7, 2, 9 and 2 daisies. What should the "
                "group report?",
        "options": [
            {"text": "A mean of 4 daisies per quadrat, and about 24 daisies "
                     "in the field.",
             "correct": False,
             "why": "Twenty-four is what you found inside six square metres "
                    "of a four hundred square metre field. It still has to be "
                    "scaled up."},
            {"text": "A mean of 4 daisies per quadrat, and about 1600 daisies "
                     "in the field.",
             "correct": True},
            {"text": "A mean of 4.8 daisies per quadrat, and about 1920 "
                     "daisies in the field.",
             "correct": False,
             "why": "Dividing by five leaves out the quadrat that held "
                    "nothing. A zero is a result, not a missing measurement, "
                    "and dropping it pushes the estimate up."},
            {"text": "A mean of 4 daisies per quadrat, and about 100 daisies "
                     "in the field.",
             "correct": False,
             "why": "That divides the field area by the mean. The scale-up "
                    "multiplies: 400 quadrat-sized areas, each holding about "
                    "4 daisies."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-h01",
        "band": "harder",
        "text": "An ecologist marks 40 woodmice and releases them. A week "
                "later she catches 50, of which 10 are marked, and puts the "
                "population at about 200. Which of these would have made her "
                "figure too high?",
        "options": [
            {"text": "The marked mice found free food in the traps and went "
                     "straight back into them.",
             "correct": False,
             "why": "Trap-happy mice raise the marked share of the second "
                    "catch, so the 40 look like a bigger slice of the "
                    "population. That pushes the estimate too low, not too "
                    "high."},
            {"text": "She waited a week, giving the marked mice time to mix "
                     "back into the population.",
             "correct": False,
             "why": "Mixing back in is one of the things the method needs. "
                    "Without it the second catch would not represent the "
                    "population at all."},
            {"text": "She caught her second sample in the same field she had "
                     "marked the first one in.",
             "correct": False,
             "why": "It has to be the same population, or the marked mice and "
                    "the recaptured ones are not describing the same thing."},
            {"text": "The marked mice grew wary of the traps, so fewer of "
                     "them were caught the second time.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h02",
        "band": "harder",
        "text": "A council estimates the trees in a large park by counting "
                "those around the ten car parks and picnic lawns, then "
                "scaling up by area. Repeating it with a hundred such spots "
                "gives almost the same number. What has that agreement "
                "shown?",
        "options": [
            {"text": "That the estimate is sound, because a hundred sampling "
                     "spots is a very large sample.",
             "correct": False,
             "why": "Two samples taken the same crooked way agree with each "
                    "other, not with the park. Agreement is stability, and "
                    "stability is not accuracy."},
            {"text": "Nothing about whether the figure is right — only that "
                     "the chance part of the error has gone.",
             "correct": True},
            {"text": "That the trees are spread evenly, since sampling more "
                     "places changed nothing.",
             "correct": False,
             "why": "Both surveys drew from the same kind of ground — mown, "
                    "open, beside a path. Agreeing about that ground says "
                    "nothing about the rest of the park."},
            {"text": "That any error still left must be small, since the two "
                     "surveys did not disagree.",
             "correct": False,
             "why": "Only the chance part of an error shows up as "
                    "disagreement. Bias makes every survey wrong in the same "
                    "direction, so it never appears as a difference between "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h03",
        "band": "harder",
        "text": "An ecologist tries to estimate the oak trees in a wood using "
                "the same 1 m² quadrat she used for daisies, placed at "
                "random. What goes wrong?",
        "options": [
            {"text": "Almost every quadrat is empty, so the mean rests on a "
                     "handful of lucky squares.",
             "correct": True},
            {"text": "The estimate comes out too low, because most quadrats "
                     "land in the gaps between the trunks.",
             "correct": False,
             "why": "The gaps are part of the wood and a fair sample should "
                    "land on them. Nothing is pulling the answer one way — it "
                    "is the wobble that is the problem."},
            {"text": "The estimate comes out too high, because one trunk gets "
                     "scaled up across the whole wood.",
             "correct": False,
             "why": "The empty quadrats are in the mean too, and they pull it "
                    "back down. The error here has no favourite direction; it "
                    "is simply very unsteady."},
            {"text": "Nothing, since a random placement gives a fair sample "
                     "whatever size the frame is.",
             "correct": False,
             "why": "Fair is not enough. The size has to suit the organism, "
                    "and a frame that catches a tree once in fifty tries "
                    "gives an answer that swings from survey to survey."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h04",
        "band": "harder",
        "text": "The bench lets you press “Show the real total”. No "
                "one surveying an actual field ever can. So what can a class "
                "check about their own estimate?",
        "options": [
            {"text": "Whether it is right, by comparing it with another "
                     "group's estimate of the same field.",
             "correct": False,
             "why": "If both groups sampled the same convenient strip they "
                    "will agree and both be wrong. Agreement between surveys "
                    "tests chance, not bias."},
            {"text": "Nothing useful — without the real total, an estimate is "
                     "only a dressed-up guess.",
             "correct": False,
             "why": "An estimate from randomly placed quadrats is not a "
                    "guess. You cannot check the answer, but you can check "
                    "the method, and the method is what makes it "
                    "trustworthy."},
            {"text": "How steady it is when repeated, which tests chance — "
                     "bias is ruled out by the placement.",
             "correct": True},
            {"text": "Whether it is right, by adding quadrats until the "
                     "answer stops changing.",
             "correct": False,
             "why": "An answer that has stopped changing has run out of "
                    "chance error. The flowery corner stops changing too, and "
                    "it stops at the wrong number."},
        ],
        "figure": None,
    },
]
