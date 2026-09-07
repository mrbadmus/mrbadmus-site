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
                     "— count two sides, not all four.",
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
            {"text": "Lay two tapes at right angles and place quadrats "
                     "where random number pairs land.",
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
            {"text": "No — the area was chosen by eye, so the sample is "
                     "biased whatever fell inside it.",
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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-e05",
        "band": "easier",
        "text": "What is a quadrat?",
        "options": [
            {"text": "Any small patch of ground a surveyor decides to count.",
             "correct": False,
             "why": "The size has to be known and the same every time, or the "
                    "counts cannot be averaged or scaled up to the whole "
                    "site."},
            {"text": "A square drawn on a map to show where a survey took "
                     "place.", "correct": False,
             "why": "It is a real frame laid on the ground rather than a mark "
                    "on a map. What is inside it is counted."},
            {"text": "A square frame of a known size, laid down so that what "
                     "is inside it can be counted.", "correct": True},
            {"text": "A frame whose size is chosen to fit whatever happens to "
                     "be inside each square.", "correct": False,
             "why": "The size does have to suit the organism, and it is "
                    "settled once for the whole survey. Changing it between "
                    "squares would make the counts useless."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e06",
        "band": "easier",
        "text": "What does bias mean in a survey?",
        "options": [
            {"text": "A mistake in the arithmetic when the mean is worked "
                     "out.", "correct": False,
             "why": "That is a slip you can find and correct. Bias is in the "
                    "sampling itself, before any arithmetic happens."},
            {"text": "The natural variation between one quadrat and the "
                     "next.", "correct": False,
             "why": "That variation is why an estimate wobbles, and it is "
                    "chance rather than bias. Chance shrinks as you take more "
                    "quadrats; bias does not."},
            {"text": "The difference between an estimate and the real total.",
             "correct": False,
             "why": "That is the error, whatever caused it. Bias is one "
                    "particular cause of it — where you chose to look."},
            {"text": "An error that comes from where you chose to look.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e07",
        "band": "easier",
        "text": "How is the mean number per quadrat worked out?",
        "options": [
            {"text": "Add up the counts and divide by the number of "
                     "quadrats.", "correct": True},
            {"text": "Add up the counts and divide by the area of the whole "
                     "site.", "correct": False,
             "why": "That runs two steps together. The mean is per quadrat; "
                    "the site's area comes in afterwards, when the mean is "
                    "scaled up."},
            {"text": "Put the counts in order and take the middle one.",
             "correct": False,
             "why": "That is the median. The method here uses the mean, which "
                    "uses every count including the zeros."},
            {"text": "Add up the counts and multiply by the number of "
                     "quadrats.", "correct": False,
             "why": "Multiplying makes the figure larger, and a mean is "
                    "smaller than the total. Divide by how many quadrats were "
                    "counted."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e08",
        "band": "easier",
        "text": "Why do ecologists estimate a population rather than count "
                "it?",
        "options": [
            {"text": "Because a full count would be less accurate than an "
                     "estimate from a sample.", "correct": False,
             "why": "A full count would be the more accurate of the two. It "
                    "is simply not possible in the time anyone has."},
            {"text": "Because counting every individual on a site would take "
                     "far longer than anyone has.", "correct": True},
            {"text": "Because the number changes every day, so no figure can "
                     "ever be right.", "correct": False,
             "why": "Numbers do change, and a count would still be the best "
                    "figure for that day. What rules a count out is the time "
                    "it would take."},
            {"text": "Because an estimate is close enough that a count would "
                     "add nothing.", "correct": False,
             "why": "A count would give the answer, which is more than an "
                    "estimate can. It is the labour that rules it out, not "
                    "the value."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-06-s05",
        "band": "standard",
        "text": "A group takes six quadrats on a field, works out its "
                "estimate and reports “about 1,637 daisies”. What is wrong "
                "with reporting it that way?",
        "options": [
            {"text": "Nothing — that is what the arithmetic gave, so that is "
                     "the honest figure to report.", "correct": False,
             "why": "The arithmetic is exact and the sample is not. Six "
                    "squares out of a whole field cannot pin a number down to "
                    "the nearest daisy."},
            {"text": "The figure should have been rounded up to 1,700, since "
                     "an estimate should never come out too low.",
             "correct": False,
             "why": "There is no reason to lean either way. Rounding is about "
                    "not claiming more precision than you have, not about "
                    "being generous."},
            {"text": "They should not have used a mean, because the daisies "
                     "are not spread evenly.", "correct": False,
             "why": "The mean is right for exactly that reason — it averages "
                    "across squares that differ. What is wrong is how "
                    "precisely the answer is written."},
            {"text": "It claims more precision than six quadrats can support; "
                     "about 1,600 would be honest.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s06",
        "band": "standard",
        "text": "Two classes survey the same field on the same afternoon, "
                "both placing ten quadrats by random coordinates. One reports "
                "about 1,400 daisies and the other about 1,750. Has one of "
                "them made a mistake?",
        "options": [
            {"text": "Not necessarily — random placement still leaves chance, "
                     "and ten quadrats is a small sample.", "correct": True},
            {"text": "Yes — two correct surveys of the same field must give "
                     "the same answer as each other.", "correct": False,
             "why": "Two samples are two different sets of squares. Even a "
                    "perfect method gives a different answer each time it is "
                    "run."},
            {"text": "Yes — one of them must have counted the plants on the "
                     "lines wrongly.", "correct": False,
             "why": "An edge rule shifts a count a little and would not open "
                    "a gap this wide. Different squares is the ordinary "
                    "explanation."},
            {"text": "No — the difference proves that both surveys were "
                     "biased.", "correct": False,
             "why": "Bias makes surveys agree with each other and disagree "
                    "with the field. Disagreement between them is the "
                    "signature of chance, not of bias."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s07",
        "band": "standard",
        "text": "Daisies are scattered fairly evenly across a field. Nettles "
                "in the same field grow in a few dense clumps. Which needs "
                "more quadrats for an estimate you can trust?",
        "options": [
            {"text": "The daisies, because there are far more of them to "
                     "count.", "correct": False,
             "why": "How many there are does not decide it. What decides it "
                    "is how much the count varies from one square to the "
                    "next."},
            {"text": "Neither — the number of quadrats depends on the size of "
                     "the field, not on the plant.", "correct": False,
             "why": "The site's size matters when you scale up. How many "
                    "quadrats you need depends on how unevenly the organism "
                    "is spread."},
            {"text": "The nettles, because a clumped plant makes the count "
                     "swing wildly from one quadrat to the next.",
             "correct": True},
            {"text": "The nettles, because a dense clump is harder to count "
                     "accurately inside the frame.", "correct": False,
             "why": "Counting a dense clump is fiddly, and that is not the "
                    "problem. The problem is that most squares hold none and "
                    "a few hold a great many."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s08",
        "band": "standard",
        "text": "A class estimates the daisies on their field at about 4,000. "
                "The next summer, with the same method and the same number of "
                "quadrats, they get about 6,500. What can they conclude?",
        "options": [
            {"text": "That the daisies have increased by about 2,500, since "
                     "the method was the same both times.", "correct": False,
             "why": "The method being the same rules out one explanation, not "
                    "the other. Part of that gap could be the ordinary wobble "
                    "of a small sample."},
            {"text": "That the daisies may well have increased, but part of "
                     "the difference could be chance.", "correct": True},
            {"text": "Nothing at all, because two estimates cannot be "
                     "compared with each other.", "correct": False,
             "why": "They can be compared, and keeping the method the same is "
                    "what makes it possible. What you cannot do is treat the "
                    "whole difference as real without checking."},
            {"text": "That one of the two surveys must have been biased, "
                     "since a field does not change that much.",
             "correct": False,
             "why": "A field really can change that much between summers — "
                    "mowing, weather and grazing all move a plant population. "
                    "Nothing here points to bias."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-h05",
        "band": "harder",
        "text": "Twelve quadrats, each 0.5 m by 0.5 m, are placed at random "
                "on a 600 m² field. The mean count is 3 buttercups per "
                "quadrat. What is the estimated population?",
        "options": [
            {"text": "36 buttercups, which is the total found in the twelve "
                     "quadrats.", "correct": False,
             "why": "That is what was counted, not what the field holds. The "
                    "mean still has to be scaled up to the whole site."},
            {"text": "1,800 buttercups, taking each quadrat as one square "
                     "metre.", "correct": False,
             "why": "Each quadrat is 0.5 m by 0.5 m, so its area is 0.25 m². "
                    "Four of them fit in every square metre, not one."},
            {"text": "7,200 buttercups, because 600 m² holds 2,400 areas of "
                     "0.25 m².", "correct": True},
            {"text": "3,600 buttercups, taking the quadrat's area as 0.5 m².",
             "correct": False,
             "why": "0.5 m is the length of a side. The area is 0.5 m "
                    "multiplied by 0.5 m, which is 0.25 m²."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h06",
        "band": "harder",
        "text": "A group takes 8 quadrats of 1 m² on a 320 m² field and gets "
                "a mean of 5.5 plants, giving 1,760. They take 8 more; across "
                "all 16 the mean is 4.75, giving 1,520. Which figure should "
                "they report?",
        "options": [
            {"text": "1,760, because the first eight were counted before "
                     "anyone knew what answer to expect.", "correct": False,
             "why": "Nothing makes the first eight purer. They are simply "
                    "half as much evidence as all sixteen are."},
            {"text": "The average of the two figures, 1,640, since both "
                     "surveys were done properly.", "correct": False,
             "why": "The second figure already contains the first eight "
                    "quadrats, so averaging counts them twice. Use the mean "
                    "of all sixteen counts."},
            {"text": "1,760, because a small sample of a fair method is less "
                     "likely to include an odd square.", "correct": False,
             "why": "It is the other way round: a small sample is more easily "
                    "thrown by one odd square, which is exactly what more "
                    "quadrats fixes."},
            {"text": "1,520, because sixteen quadrats leave less room for "
                     "chance than eight do.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h07",
        "band": "harder",
        "text": "An ecologist marks 60 ground beetles and releases them. Some "
                "days later she catches 90 beetles, of which 15 are marked. "
                "What is the estimated population?",
        "options": [
            {"text": "About 360, because 15 marked in 90 means the 60 are "
                     "about a sixth of the population.", "correct": True},
            {"text": "About 150, by adding the beetles caught on the two "
                     "occasions.", "correct": False,
             "why": "Adding the two catches counts beetles handled, not "
                    "beetles present. The method uses the fraction of the "
                    "second catch that carried a mark."},
            {"text": "About 900, by multiplying the 60 marked beetles by the "
                     "15 recaptured.", "correct": False,
             "why": "The 15 belong underneath rather than on top — they are "
                    "the share of the second catch that was marked. Marking "
                    "more beetles cannot raise the population."},
            {"text": "About 90, since the second catch is a fair sample of "
                     "the beetles present.", "correct": False,
             "why": "The second catch is a sample of the population, not the "
                    "whole of it. It is the marked share within it that "
                    "scales the 60 up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h08",
        "band": "harder",
        "text": "A charity reports that Britain has lost about 60% of its "
                "farmland butterflies since 1976. Nobody has ever counted "
                "them. What must have been done to make a statement like that "
                "possible?",
        "options": [
            {"text": "One very large count in 1976, which later years have "
                     "been compared against.", "correct": False,
             "why": "One count, however large, gives one figure. A trend "
                    "needs the same measurement repeated, year after year."},
            {"text": "The same sampling method repeated every year, so that "
                     "the counts can be compared.", "correct": True},
            {"text": "A count of every butterfly on a few farms, scaled up to "
                     "the whole country.", "correct": False,
             "why": "Scaling up gives a total for one year. Claiming a fall "
                    "needs comparable figures from the start of the period "
                    "and from now."},
            {"text": "An estimate of how many there ought to be, compared "
                     "with how many are seen now.", "correct": False,
             "why": "How many there ought to be is not something anyone can "
                    "measure. The claim rests on real counts taken the same "
                    "way over time."},
        ],
        "figure": None,
    },
]
