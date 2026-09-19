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

    # ── MRB-338 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-e09",
        "band": "easier",
        "text": "Which unit is normally used to measure the area of a "
                "quadrat?",
        "options": [
            {"text": "Square metres, since a quadrat marks out a flat "
                     "area on the ground.", "correct": True},
            {"text": "Metres, the length along one side of the frame "
                     "alone.", "correct": False,
             "why": "A plain metre measures a length, one side of the "
                    "frame. The quadrat's AREA needs a squared unit, not a "
                    "single side."},
            {"text": "Litres, since a quadrat encloses a volume of "
                     "habitat above the ground.", "correct": False,
             "why": "Litres measure volume, and a quadrat is a flat frame "
                    "laid on the ground rather than a three-dimensional "
                    "container of any kind."},
            {"text": "Kilograms, since the figure depends on how much "
                     "lives inside the frame.", "correct": False,
             "why": "Kilograms measure mass, not the amount of ground the "
                    "frame encloses. What lives inside does not decide "
                    "the quadrat's own fixed area."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e10",
        "band": "easier",
        "text": "A survey counts daisies in ten 1 m² quadrats out of a "
                "500 m² field. What do the ten quadrats together make up?",
        "options": [
            {"text": "The population of daisies in the field, meaning every single daisy growing anywhere within its boundary.",
             "correct": False,
             "why": "The population is every daisy in the whole 500 m², "
                    "not just the ten squares actually counted."},
            {"text": "The sample — a small part of the population used to "
                     "estimate the whole.", "correct": True},
            {"text": "The census of the field's daisies.", "correct": False,
             "why": "A census would mean every daisy in the field was "
                    "counted. Ten squares out of five hundred is far short "
                    "of that."},
            {"text": "The control group for the survey.", "correct": False,
             "why": "Nothing here is being compared against a control. All "
                    "ten squares are simply the counted part of one "
                    "survey."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e11",
        "band": "easier",
        "text": "Why should the quadrats in one survey never be allowed to "
                "overlap each other?",
        "options": [
            {"text": "Because overlapping squares would be too heavy to "
                     "carry between positions.", "correct": False,
             "why": "Weight has nothing to do with it. A quadrat frame is "
                    "picked up and moved between positions — overlap is "
                    "about position, not weight."},
            {"text": "Because overlapping squares always land in the most "
                     "crowded part of the site.", "correct": False,
             "why": "Where squares land is decided by the random "
                    "coordinates, not by whether two happen to touch. "
                    "Overlap and bias are different problems."},
            {"text": "Because any organism counted twice would inflate the "
                     "mean per quadrat.", "correct": True},
            {"text": "Because the total area covered would then be too "
                     "large to scale up.", "correct": False,
             "why": "Overlap makes the counted area smaller than it looks, "
                    "not larger, because some ground gets counted twice "
                    "over."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e12",
        "band": "easier",
        "text": "A quadrat that is too small for the organism being counted "
                "causes one particular problem. What is it?",
        "options": [
            {"text": "The estimate becomes biased towards a lower figure "
                     "every time.", "correct": False,
             "why": "A quadrat too small does not lean the answer one "
                    "particular way. It makes the count swing about, "
                    "sometimes high and sometimes low."},
            {"text": "The quadrat frame becomes impossible to lay flat on "
                     "the ground.", "correct": False,
             "why": "Nothing about a frame's size stops it lying flat. The "
                    "problem is what happens to the COUNT once it is "
                    "placed."},
            {"text": "The organism is always missed completely, however many quadrats are taken across the whole of the site.", "correct": False,
             "why": "Some quadrats will still catch it — that is exactly "
                    "why the count varies from none to several. It is not "
                    "missed every single time."},
            {"text": "The count in each square swings about "
                     "unpredictably, rather than settling near a steady "
                     "value.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e13",
        "band": "easier",
        "text": "Six quadrats give six different counts of a plant. Why is "
                "the mean of those six counts used, rather than just one "
                "quadrat's count?",
        "options": [
            {"text": "Because a single quadrat could easily have landed "
                     "somewhere unusually rich or unusually bare.",
             "correct": True},
            {"text": "Because the highest count is usually wrong and "
                     "should be thrown away.", "correct": False,
             "why": "Nothing says the highest count is wrong. The mean "
                    "uses every count, high and low together, rather than "
                    "discarding any of them."},
            {"text": "Because a mean is always going to be a larger number than any single one quadrat's count could be.", "correct": False,
             "why": "A mean sits somewhere between the smallest and "
                    "largest counts, not above all of them. Size is not "
                    "the reason it is used."},
            {"text": "Because only the mean, and never a single quadrat's count, can properly be multiplied to scale up to the whole field.", "correct": False,
             "why": "Any single number could technically be multiplied. "
                    "The mean is used because it represents all six "
                    "squares fairly, not because of the arithmetic alone."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e14",
        "band": "easier",
        "text": "One quadrat in a survey of six contains no plants at all. "
                "How should that quadrat's count be treated?",
        "options": [
            {"text": "Left out of the mean, since it adds nothing to the "
                     "total.", "correct": False,
             "why": "Leaving it out drops the number of quadrats divided "
                    "by, which quietly raises the mean. A zero counts as a "
                    "real result."},
            {"text": "Counted as a zero, exactly like any other result — "
                     "never simply left out.",
             "correct": True},
            {"text": "Replaced with the average of the other five counts.",
             "correct": False,
             "why": "Replacing a real result with an invented one hides "
                    "what was actually found. A true zero has to stay a "
                    "zero."},
            {"text": "Reported separately, since a zero cannot be part of "
                     "a mean.", "correct": False,
             "why": "A zero is an ordinary number and adds perfectly well "
                    "into a total. There is no reason it cannot take part "
                    "in a mean."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e15",
        "band": "easier",
        "text": "Before a population estimate can be scaled up from a "
                "sample, what has to be known about the site?",
        "options": [
            {"text": "The exact number of species living there.",
             "correct": False,
             "why": "The whole point of sampling is that this is NOT "
                    "already known. What is needed is the site's area, not "
                    "a list of its species."},
            {"text": "The names of every organism that might be found "
                     "there.", "correct": False,
             "why": "A survey is usually counting one named organism, not "
                    "identifying every species present. Area is what the "
                    "scaling calculation needs."},
            {"text": "The total area of the site, in the same units as "
                     "the quadrat.", "correct": True},
            {"text": "How many years the site has existed in its current "
                     "form.", "correct": False,
             "why": "Nothing about the calculation uses the site's age. It "
                    "uses the site's area and the quadrat's area."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e16",
        "band": "easier",
        "text": "In capture–mark–recapture, animals are caught, marked, "
                "released, and then caught again later. Why release them at "
                "all, rather than counting the marked ones directly?",
        "options": [
            {"text": "Because keeping the marked animals in captivity for any length of time would be against the law in every single country.", "correct": False,
             "why": "Laws on handling wildlife vary and are not the reason "
                    "given by the method itself. The method needs the "
                    "marked animals mixing freely back in."},
            {"text": "Because a second catch is always larger than the "
                     "first one taken.", "correct": False,
             "why": "Nothing requires the second catch to be larger. What "
                    "matters is the fraction of it that turns out to be "
                    "marked."},
            {"text": "Because marking an animal only ever takes effect after it has been free again for a while.", "correct": False,
             "why": "The marking itself happens at the moment of the "
                    "first catch. Release is about letting the population "
                    "mix, not about the mark taking effect."},
            {"text": "Because releasing them lets the marked animals mix "
                     "back in with the rest of the population.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e17",
        "band": "easier",
        "text": "Which of these is a genuine way of generating random "
                "numbers for placing quadrats?",
        "options": [
            {"text": "Rolling dice, or using a calculator's random number "
                     "function.", "correct": True},
            {"text": "Guessing a number that simply feels fair before looking closely at the site.", "correct": False,
             "why": "A guess is still a choice, made by a person with "
                    "preferences. Feeling fair does not remove that."},
            {"text": "Counting the letters in the name of the field being "
                     "surveyed.", "correct": False,
             "why": "A field's name never changes, so this gives exactly "
                    "the same numbers on every single visit — which is not "
                    "what randomness means."},
            {"text": "Asking a different member of the group to pick a "
                     "number they like.", "correct": False,
             "why": "A liked number is still a preference, just somebody "
                    "else's. The process still has a favourite, which is "
                    "exactly what randomness rules out."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e18",
        "band": "easier",
        "text": "A team spaces its quadrats evenly, one every five metres in "
                "a straight line across a field. Is that a random sample?",
        "options": [
            {"text": "Yes — the positions are decided by a rule, not "
                     "chosen by eye.", "correct": False,
             "why": "Being decided by a rule is not the same as being "
                    "random. An even five-metre spacing is a pattern the "
                    "team chose, not one chance produced."},
            {"text": "No — the positions always follow a fixed pattern "
                     "rather than being chosen by chance.", "correct": True},
            {"text": "Yes, as long as the five-metre gap is measured "
                     "accurately with a tape.", "correct": False,
             "why": "Accurate measuring makes the pattern precise, not "
                    "random. A precisely measured pattern is still a "
                    "pattern."},
            {"text": "It cannot be judged without knowing how many "
                     "quadrats were placed in total.", "correct": False,
             "why": "The number of quadrats does not decide whether the "
                    "pattern is random. An evenly spaced line stays a "
                    "fixed pattern whatever its length."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e19",
        "band": "easier",
        "text": "A wildlife survey is carried out only between nine and "
                "five during the day. Which organisms might it miss almost "
                "entirely?",
        "options": [
            {"text": "Any organism that is particularly small in size.",
             "correct": False,
             "why": "Time of day and size are different things. A "
                    "daytime-only survey misses night activity, regardless "
                    "of how large or small an organism is."},
            {"text": "Any organism that lives underground for part of its "
                     "life.", "correct": False,
             "why": "Living underground is about where an organism is, "
                    "not when it is active. Plenty of daytime creatures "
                    "also spend time below ground."},
            {"text": "Any organism that is active mainly at night.",
             "correct": True},
            {"text": "Any organism that feeds on more than one kind of "
                     "food.", "correct": False,
             "why": "What an organism eats has no bearing on when a "
                    "survey is run. A daytime survey misses night-time "
                    "activity specifically."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e20",
        "band": "easier",
        "text": "A quadrat sized for counting daisies is used, unchanged, "
                "to try to count a much larger plant such as gorse bushes. "
                "What goes wrong?",
        "options": [
            {"text": "The gorse bushes are too prickly to count safely "
                     "with a small frame.", "correct": False,
             "why": "Safety with a prickly plant is not what this "
                    "question is about. The problem is the size mismatch "
                    "between the frame and the plant."},
            {"text": "The daisies underneath the gorse get counted by "
                     "mistake instead.", "correct": False,
             "why": "Nothing forces a mix-up between the two plants. The "
                    "problem is that the frame does not suit the larger "
                    "plant's size."},
            {"text": "The mean calculation stops working correctly once the organism being counted gets any larger than the frame itself.", "correct": False,
             "why": "The arithmetic of the mean still works on whatever "
                    "numbers are recorded. What breaks down is how "
                    "meaningful those numbers are for a plant this size."},
            {"text": "The frame is too small to hold a whole bush, so "
                     "most squares catch none or only part of one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e21",
        "band": "easier",
        "text": "A student places a single quadrat in a field, scales its "
                "count up by the field's area, and reports that as the "
                "population. What is wrong with that?",
        "options": [
            {"text": "One quadrat cannot show how much the count varies "
                     "from place to place across the site.", "correct": True},
            {"text": "Nothing — one single square is a perfectly good sample, provided it is placed completely randomly.", "correct": False,
             "why": "One square is far too small a sample on its own, "
                    "randomly placed or not. A single result cannot show "
                    "how much the count varies across a whole field."},
            {"text": "A single quadrat always happens to land in the "
                     "richest part of a field.", "correct": False,
             "why": "There is no reason a single square always lands "
                    "somewhere rich. It might just as easily land "
                    "somewhere bare — which is exactly the problem."},
            {"text": "The calculation cannot ever be scaled up properly unless at least ten separate quadrats have been used.", "correct": False,
             "why": "The scaling arithmetic works with any number of "
                    "quadrats, even one. The trouble is not the "
                    "arithmetic, but how little a single square can tell "
                    "you."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e22",
        "band": "easier",
        "text": "A survey records some quadrat areas in square metres and "
                "others, by mistake, in square feet. What problem does that "
                "cause?",
        "options": [
            {"text": "None, as long as every quadrat was placed at "
                     "random.", "correct": False,
             "why": "Random placement fixes bias, not mismatched units. "
                    "Mixing units means the counts cannot be honestly "
                    "compared or added together."},
            {"text": "The counts from the two kinds of quadrat can never "
                     "be combined or compared fairly.", "correct": True},
            {"text": "The mean will always come out larger than it "
                     "should.", "correct": False,
             "why": "Mixed units make the whole calculation unreliable, "
                    "not reliably too large. The direction of the error "
                    "cannot even be predicted."},
            {"text": "The problem disappears completely once the final population estimate has actually been calculated.", "correct": False,
             "why": "The mistake is built into the numbers the estimate "
                    "comes from. Doing the arithmetic cannot undo units "
                    "that never matched in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e23",
        "band": "easier",
        "text": "A group walks around a field first and picks out the "
                "squares that 'look about average' for the plant they are "
                "counting. Why does that fail to be a fair sample?",
        "options": [
            {"text": "Because 'about average' squares are always "
                     "slightly too small to count properly.", "correct": False,
             "why": "Size of the square is not the issue here — the group "
                    "is choosing existing ground, not choosing a frame "
                    "size. The problem is how the SQUARES were picked."},
            {"text": "Because average-looking ground is rarer than either "
                     "rich or bare ground.", "correct": False,
             "why": "How common average-looking ground is does not "
                    "matter. The problem is that a person picked it by "
                    "eye, which a fair sample cannot rely on."},
            {"text": "Because judging what looks average is still a "
                     "choice made by the surveyor, not by chance.",
             "correct": True},
            {"text": "Because the word 'average' has no proper meaning "
                     "until the mean has been worked out.", "correct": False,
             "why": "The mean is indeed calculated afterwards, and that "
                    "is not why this method fails. It fails because the "
                    "squares were never placed by chance in the first "
                    "place."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e24",
        "band": "easier",
        "text": "A large nature reserve is surveyed by placing every "
                "quadrat within a few paces of the car park, for "
                "convenience. What is wrong with that?",
        "options": [
            {"text": "Nothing — as long as the number of quadrats taken "
                     "there is large enough.", "correct": False,
             "why": "However many quadrats are taken, they are all drawn "
                    "from the same small patch near the car park. More "
                    "squares there just repeat the same narrow view."},
            {"text": "Car parks always support fewer plants than any "
                     "other part of a reserve.", "correct": False,
             "why": "There is no rule that ground near a car park is "
                    "always the poorest. The problem is simply that it "
                    "may not be typical of the reserve as a whole."},
            {"text": "Quadrats placed near a car park cannot be measured "
                     "accurately with a tape.", "correct": False,
             "why": "A tape measure works exactly the same near a car "
                    "park as anywhere else. The issue is where the "
                    "squares were chosen, not how they are measured."},
            {"text": "The car park area may not represent the rest of the "
                     "reserve at all.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e25",
        "band": "easier",
        "text": "What is the difference between an 'estimate' of a "
                "population and an exact count of it?",
        "options": [
            {"text": "An estimate is worked out from a sample; an exact "
                     "count means every individual has been found.",
             "correct": True},
            {"text": "An estimate is always higher than an exact count "
                     "would be.", "correct": False,
             "why": "An estimate can come out higher OR lower than the "
                    "truth — that is exactly why it is called an estimate "
                    "rather than a fact."},
            {"text": "An estimate applies only to counting plants, and an exact count applies only to counting animals instead.", "correct": False,
             "why": "Both plants and animals can be estimated or exactly "
                    "counted. The difference is about method, not about "
                    "which kingdom is studied."},
            {"text": "An estimate uses metres and an exact count uses "
                     "individual organisms.", "correct": False,
             "why": "Both an estimate and an exact count are numbers of "
                    "organisms in the end. Units of area help scale an "
                    "estimate up, not define it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e26",
        "band": "easier",
        "text": "A conservation charity wants to know whether a rare orchid "
                "is increasing or decreasing on a reserve. Why does it need "
                "a population estimate rather than a guess?",
        "options": [
            {"text": "Because a guess would break wildlife protection "
                     "laws covering rare species.", "correct": False,
             "why": "No law is broken by guessing a number — it is simply "
                    "unreliable. A guess gives nothing to compare against "
                    "next year's figure."},
            {"text": "Because only a properly worked-out estimate gives a "
                     "number that can be compared honestly from year to "
                     "year.", "correct": True},
            {"text": "Because a guess would still need every single orchid to be found and counted one at a time anyway regardless.", "correct": False,
             "why": "A guess needs no counting at all, which is exactly "
                    "its weakness. An estimate is built from real counts "
                    "in real quadrats."},
            {"text": "Because rare species always need larger quadrats "
                     "than common ones do.", "correct": False,
             "why": "Rarity does not by itself decide the size of quadrat "
                    "needed. What matters for tracking a population is a "
                    "repeatable, comparable method."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e27",
        "band": "easier",
        "text": "A quadrat frame is meant to be laid flat on the ground at "
                "each chosen position. Why does that matter?",
        "options": [
            {"text": "So that the frame does not blow away in windy "
                     "weather.", "correct": False,
             "why": "Wind is a nuisance for the surveyor, not a reason "
                    "the method needs a flat frame. The reason is keeping "
                    "the enclosed area consistent."},
            {"text": "So that the plants growing inside it can be identified much more easily from directly above.", "correct": False,
             "why": "Identifying plants is about looking closely, not "
                    "about the frame's angle. A tilted frame can still be "
                    "looked into perfectly well."},
            {"text": "So that every quadrat encloses the same area, "
                     "whatever the ground looks like.", "correct": True},
            {"text": "So that the same frame can be reused on a "
                     "different kind of organism afterwards.",
             "correct": False,
             "why": "Reusing the frame elsewhere has nothing to do with "
                    "laying it flat. Flatness is about the area the frame "
                    "marks out at each position."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e28",
        "band": "easier",
        "text": "In capture–mark–recapture, why must the mark used on an "
                "animal be harmless and easy to see, but not something that "
                "changes its behaviour?",
        "options": [
            {"text": "Because a harmful mark would need the study to be "
                     "approved by more people.", "correct": False,
             "why": "Approval processes are not what this question is "
                    "asking about. The reason is keeping the animal's "
                    "chances the same as an unmarked one's."},
            {"text": "Because a highly visible mark always attracts noticeably more predators to the whole surrounding area.", "correct": False,
             "why": "That is not a general rule, and it is not the reason "
                    "a mark must be harmless. The reason is keeping a "
                    "marked animal's odds unchanged."},
            {"text": "So that the second catch always ends up containing more marked animals overall than unmarked ones do.", "correct": False,
             "why": "Nothing requires marked animals to outnumber "
                    "unmarked ones in the second catch — usually the "
                    "opposite is true. The mark must simply not tip the "
                    "odds either way."},
            {"text": "So that a marked animal is exactly as likely to "
                     "survive and be caught again as an unmarked one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e29",
        "band": "easier",
        "text": "Why do scientists publishing a population estimate always "
                "state how many quadrats or how many animals were "
                "sampled?",
        "options": [
            {"text": "So that anyone reading the report can judge how "
                     "reliable the estimate is likely to be.",
             "correct": True},
            {"text": "Because a bigger sample number always looks far more impressive in any published report.", "correct": False,
             "why": "Impressiveness is not the reason. Stating the sample "
                    "size lets other scientists judge how much confidence "
                    "to place in the figure."},
            {"text": "Because it is required by law in every single country that funds any ecological research at all.", "correct": False,
             "why": "This is a scientific convention rather than a "
                    "universal legal requirement. It is reported because "
                    "it matters for judging the result."},
            {"text": "Because the sample size has to be added to the "
                     "final population figure.", "correct": False,
             "why": "Sample size and the final estimate are two separate "
                    "numbers, never added together. One is reported "
                    "alongside the other, not folded into it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-e30",
        "band": "easier",
        "text": "Two students argue about a quadrat survey. One says 'the "
                "bigger the sample, the better, full stop.' What is the "
                "flaw in stating it that way?",
        "options": [
            {"text": "A bigger sample fixes bias as well as chance, so "
                     "the statement is completely correct.", "correct": False,
             "why": "A bigger sample does nothing for bias — a larger "
                    "biased sample is still just as wrong, only more "
                    "confidently so."},
            {"text": "A bigger sample only helps with the chance part of "
                     "the error, not with bias.", "correct": True},
            {"text": "A bigger sample is worse than a smaller one, "
                     "because it takes longer to complete.", "correct": False,
             "why": "Taking longer is a practical cost, not a reason a "
                    "larger sample gives a worse answer. Time spent is "
                    "not what this statement gets wrong."},
            {"text": "Sample size makes no difference of any kind to a "
                     "population estimate.", "correct": False,
             "why": "It makes a real difference to how much an estimate "
                    "wobbles from one attempt to the next. What it does "
                    "not touch is bias."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-06-s09",
        "band": "standard",
        "text": "Eight 1 m² quadrats survey a 640 m² meadow and give a mean "
                "of 3.5 buttercups per quadrat. What is the estimated "
                "population?",
        "options": [
            {"text": "About 22.4, using a hundredth of the field's true "
                     "area.", "correct": False,
             "why": "A hundredth of the field is 6.4 m². The field holds "
                    "640 separate quadrat-sized areas, and using all of "
                    "them gives 2,240."},
            {"text": "About 224.", "correct": False,
             "why": "That uses only a tenth of the field's true area. The "
                    "full 640 m² has to be used, which gives 2,240."},
            {"text": "About 2,240.", "correct": True},
            {"text": "About 1,120, using half of the field's area instead "
                     "of the whole of it.", "correct": False,
             "why": "The whole 640 m² has to be scaled by, not half of "
                    "it. Using the full area gives twice this figure."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s10",
        "band": "standard",
        "text": "A student is told a field is 600 m² and the estimated "
                "population of a plant on it is 3,000. What was the mean "
                "count per 1 m² quadrat?",
        "options": [
            {"text": "500, reading the field's area as 6 m² rather than "
                     "600 m².", "correct": False,
             "why": "A 600 m² field holds 600 quadrat-sized areas, not "
                    "six. Dividing 3,000 by 600 gives a mean of 5."},
            {"text": "50.", "correct": False,
             "why": "That is 3,000 divided by 60 rather than by 600 — the "
                    "decimal point one place out. The field holds 600 "
                    "quadrat-sized areas."},
            {"text": "1,800,000, multiplying the estimate by the field's "
                     "area.", "correct": False,
             "why": "Multiplying makes the mean far larger than any "
                    "quadrat could hold. The mean is the estimate divided "
                    "by the field's area, not multiplied by it."},
            {"text": "5.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s11",
        "band": "standard",
        "text": "An ecologist marks 30 red squirrels and releases them. A "
                "month later she catches 45, of which 9 are marked. What is "
                "the estimated population?",
        "options": [
            {"text": "150.", "correct": True},
            {"text": "9, the number of marked squirrels caught again.",
             "correct": False,
             "why": "That is a count used inside the calculation, not the "
                    "answer to it. The nine marked ones caught again show "
                    "what fraction of the population is marked."},
            {"text": "75.", "correct": False,
             "why": "That is the two catches added together, 30 and 45. "
                    "Adding them ignores what fraction of the second catch "
                    "was marked, which is the whole basis of the method."},
            {"text": "1,350, multiplying the two catches together.",
             "correct": False,
             "why": "Multiplying the catches together does not represent "
                    "anything in this method. The marked fraction of the "
                    "second catch is what scales the first catch up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s12",
        "band": "standard",
        "text": "A survey reports a population estimate to the nearest "
                "single daisy, such as '3,417 daisies'. Why is that level "
                "of precision misleading?",
        "options": [
            {"text": "Because a computer, not a person, must have done "
                     "the arithmetic to get such an exact-looking number.",
             "correct": False,
             "why": "Who or what did the arithmetic makes no difference. "
                    "The problem is that the sample cannot support that "
                    "much precision, whoever calculated it."},
            {"text": "Because a sample of a few quadrats cannot pin the "
                     "true total down to one exact daisy.", "correct": True},
            {"text": "Because population estimates always have to be rounded down somehow, and never given exactly at all.", "correct": False,
             "why": "There is no rule that estimates round down "
                    "specifically. The issue is precision, not which "
                    "direction any rounding goes."},
            {"text": "Because daisies are too small a plant to be counted "
                     "to an exact number.", "correct": False,
             "why": "Size of the organism is not the reason. Even large, "
                    "easily counted organisms cannot be pinned to an "
                    "exact figure from a small sample."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s13",
        "band": "standard",
        "text": "Two fields are surveyed with the same method and the same "
                "number of quadrats. Field A gives a steady estimate on "
                "repeat surveys; Field B's estimate swings wildly each "
                "time. What does that difference most likely show?",
        "options": [
            {"text": "Field A's survey must have been biased, since a "
                     "biased answer looks the same every time.",
             "correct": False,
             "why": "Both fields used the same fair method, so bias is "
                    "not the difference between them. A steady result is "
                    "not itself proof of bias."},
            {"text": "Field A simply has fewer plants overall than Field "
                     "B does.", "correct": False,
             "why": "How many plants a field holds does not decide how "
                    "steady repeat estimates are. Evenness of spread is "
                    "what does."},
            {"text": "Field B's plant is probably spread far less evenly "
                     "across the site than Field A's.", "correct": True},
            {"text": "Field B's quadrats must simply have been placed by eye rather than genuinely at random.", "correct": False,
             "why": "Nothing here says the method differed between the "
                    "two fields. An uneven spread of the plant is enough "
                    "to explain the swings, method aside."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s14",
        "band": "standard",
        "text": "An ecologist's mark-recapture estimate for a woodland "
                "beetle comes out far too low compared with a careful "
                "hand-search of the whole plot. Mixing back in was normal, "
                "and nothing died between the two catches. What could "
                "explain the low figure?",
        "options": [
            {"text": "Some unmarked beetles must have been accidentally "
                     "marked during the second catch.", "correct": False,
             "why": "There is no route for that to happen — marking only "
                    "happens at the first catch. An error like this would "
                    "not explain a low estimate anyway."},
            {"text": "The population must simply be smaller than the "
                     "hand-search suggested.", "correct": False,
             "why": "The hand-search is described as the more careful, "
                    "reliable count here. The mismatch is being explained "
                    "by a flaw in the mark-recapture method, not by "
                    "doubting the hand-search."},
            {"text": "The marked beetles must have bred rapidly before the second catch, adding many more marked individuals to the whole population.",
             "correct": False,
             "why": "A marked beetle's offspring are not themselves "
                    "marked. New unmarked young would if anything dilute "
                    "the marked fraction, not raise it."},
            {"text": "The marked beetles were drawn back to a baited "
                     "trap, so they made up an unusually large share of "
                     "the second catch.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s15",
        "band": "standard",
        "text": "One group samples only the shaded edge of a field for a "
                "sun-loving plant and gets a very low estimate. Another "
                "group samples only the sunniest centre and gets a very "
                "high one. What do both mistakes have in common?",
        "options": [
            {"text": "Both chose where to look rather than letting chance "
                     "decide.", "correct": True},
            {"text": "Both used too few quadrats to get a reliable "
                     "answer.", "correct": False,
             "why": "Sample size is not named as a problem in either "
                    "case. The shared fault is where each group chose to "
                    "sample, not how many quadrats they used."},
            {"text": "Both forgot to record a quadrat that held zero "
                     "plants.", "correct": False,
             "why": "Nothing here says a zero result was dropped. The "
                    "shared problem is that each group picked which "
                    "ground to sample by eye."},
            {"text": "Both used quadrats of the wrong size for this "
                     "plant.", "correct": False,
             "why": "Quadrat size is not mentioned as an issue for either "
                    "group. The shared fault is in where the quadrats "
                    "were placed, not their size."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s16",
        "band": "standard",
        "text": "A group wants to compare bumblebee numbers on a farm's "
                "wildflower strip against its neighbouring crop field. What "
                "must stay the same between the two surveys for the "
                "comparison to be fair?",
        "options": [
            {"text": "The species of plant growing in each area.",
             "correct": False,
             "why": "The plants are expected to differ — that is the "
                    "whole point of the comparison. What must match is "
                    "the method used to sample each one."},
            {"text": "The number of quadrats, the quadrat size, and the "
                     "time of day, in both places.", "correct": True},
            {"text": "The name of the particular person carrying the quadrat frame around during each survey.", "correct": False,
             "why": "Who is physically carrying the frame does not "
                    "affect the result, provided both follow the same "
                    "method. Consistency of method is what matters."},
            {"text": "The total area of each of the two sites.",
             "correct": False,
             "why": "The two sites can be different sizes; the scale-up "
                    "arithmetic accounts for that. What has to match is "
                    "the sampling method itself."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s17",
        "band": "standard",
        "text": "A survey of 12 quadrats, each 0.5 m × 0.5 m, on a "
                "900 m² meadow gives a mean of 2 plants per quadrat. What "
                "is the estimated population?",
        "options": [
            {"text": "1,800, treating each quadrat as one square metre.",
             "correct": False,
             "why": "Each quadrat is 0.25 m², not 1 m². Four of them fit "
                    "into every square metre, which changes the "
                    "scale-up."},
            {"text": "3,600, using a mean of one rather than two.",
             "correct": False,
             "why": "The mean here really is two plants per quadrat, not "
                    "one. Halving it by mistake halves the final answer "
                    "too."},
            {"text": "7,200.", "correct": True},
            {"text": "24.", "correct": False,
             "why": "Twenty-four is the total found in the twelve small "
                    "squares actually surveyed. It still has to be scaled "
                    "up to the whole meadow."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s18",
        "band": "standard",
        "text": "A student says quadrat surveys are 'basically guessing "
                "with extra steps.' How would you respond, using what this "
                "method actually controls for?",
        "options": [
            {"text": "The student is right — every single step in a quadrat survey still comes down to guesswork in the end, whatever is claimed.",
             "correct": False,
             "why": "Random placement is not a guess — it deliberately "
                    "removes the surveyor's preferences from where the "
                    "squares land. What remains is an honest estimate, "
                    "not a guess."},
            {"text": "The student is wrong, because a quadrat survey "
                     "always gives the exact true population.",
             "correct": False,
             "why": "A quadrat survey never claims to give the exact true "
                    "population — it gives an estimate, with real "
                    "uncertainty in it. What it removes is bias, not "
                    "uncertainty altogether."},
            {"text": "The student is right, since nobody can ever know "
                     "if an estimate is correct.", "correct": False,
             "why": "Not being able to check the exact answer does not "
                    "make the method a guess. A method that removes bias "
                    "and reduces chance error is doing real work, not "
                    "guessing."},
            {"text": "The method removes guessing about where to look, "
                     "by using chance, even though the final number is "
                     "still an estimate.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s19",
        "band": "standard",
        "text": "A patchy plant like gorse and an evenly spread plant like "
                "daisies grow in the same field. For a given number of "
                "quadrats, whose estimate is likely to be less reliable?",
        "options": [
            {"text": "The gorse's, because a patchy spread makes the "
                     "count vary wildly between quadrats.", "correct": True},
            {"text": "The daisies', because an even spread is actually "
                     "harder to detect with a small frame.", "correct": False,
             "why": "An even spread is the easier case for a small "
                    "sample — nearly every quadrat gives a similar count. "
                    "Patchiness is what causes the trouble."},
            {"text": "Both equally, since the same number of quadrats "
                     "was used for each.", "correct": False,
             "why": "Using the same number of quadrats does not equalise "
                    "reliability if the two plants are spread very "
                    "differently across the ground."},
            {"text": "Neither — reliability depends only on the total area of the field being surveyed each time.", "correct": False,
             "why": "Field area does not by itself decide reliability "
                    "here. How evenly a plant is spread across that area "
                    "is what does."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s20",
        "band": "standard",
        "text": "A month passes between the two catches in a mark-recapture "
                "study, and the population breeds heavily in that time. "
                "What effect does that have on the population estimate?",
        "options": [
            {"text": "It has no effect at all, since only fully grown adult animals are ever marked or recaptured in this particular kind of study.", "correct": False,
             "why": "The new young are still caught in the second catch "
                    "and counted as unmarked, whether or not only adults "
                    "were marked. They still affect the arithmetic."},
            {"text": "It tends to overestimate the original population, "
                     "since new unmarked young are counted as if they "
                     "were already there.", "correct": True},
            {"text": "It always underestimates the population, whatever "
                     "else is true.", "correct": False,
             "why": "New unmarked young raise the second catch without "
                    "raising the marked count, which pushes the estimate "
                    "up, not down."},
            {"text": "It only matters if the young are marked before "
                     "being released again.", "correct": False,
             "why": "The young were never part of the first catch, so "
                    "they cannot be marked in this study. Their presence "
                    "in the second catch is what changes the arithmetic."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s21",
        "band": "standard",
        "text": "A newspaper reports 'a new survey shows twice as many "
                "hedgehogs as last year's survey.' What would you want to "
                "know before accepting that as a real increase?",
        "options": [
            {"text": "Whether hedgehogs are nocturnal or active during "
                     "the day.", "correct": False,
             "why": "Hedgehogs being nocturnal is a fixed fact about the "
                    "species, not something that changed between the two "
                    "surveys. It cannot explain a difference between "
                    "them."},
            {"text": "Whether hedgehogs are considered a protected "
                     "species this year.", "correct": False,
             "why": "Legal protection status has no bearing on how many "
                    "hedgehogs a survey actually finds. What matters is "
                    "whether the two surveys are comparable."},
            {"text": "Whether both surveys used the same method, in the "
                     "same season, with a comparable amount of effort.",
             "correct": True},
            {"text": "Whether the newspaper printed the story on its front page or somewhere further inside the whole publication.", "correct": False,
             "why": "Where a story appears in a newspaper says nothing "
                    "about the reliability of the survey behind it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s22",
        "band": "standard",
        "text": "A meadow's daisies are spread fairly evenly; a "
                "hedge-bottom's nettles grow in a few dense clumps. To get "
                "equally reliable estimates of each, would the same "
                "number of quadrats do the job for both?",
        "options": [
            {"text": "Yes — the same number of quadrats always gives the "
                     "same reliability, whatever the plant.", "correct": False,
             "why": "Reliability depends on how much the count varies "
                    "between quadrats, and an unevenly spread plant "
                    "varies far more than an evenly spread one."},
            {"text": "No — the evenly spread daisies would need far more "
                     "quadrats than the nettles.", "correct": False,
             "why": "It is the opposite way round. An even spread gives "
                    "similar counts everywhere, so fewer quadrats are "
                    "needed to get a steady figure."},
            {"text": "Yes, provided both surveys use exactly the same "
                     "size of quadrat.", "correct": False,
             "why": "Matching the quadrat size does not equalise how "
                    "unevenly each plant is spread across the ground, "
                    "which is what drives the difference in reliability."},
            {"text": "No — the clumped nettles are likely to need more "
                     "quadrats to settle on a steady estimate.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s23",
        "band": "standard",
        "text": "A survey meant to use 1 m² quadrats accidentally uses "
                "2 m² ones throughout, and still records a mean of 8 plants "
                "per quadrat, on a 400 m² field. What must be corrected "
                "before scaling up?",
        "options": [
            {"text": "The number of quadrat-sized areas in the field, "
                     "since each one is now 2 m² rather than 1 m².",
             "correct": True},
            {"text": "Nothing — the mean of 8 can simply be scaled directly using the field's stated 400 m² area as it stands.", "correct": False,
             "why": "Scaling directly like this would treat each quadrat "
                    "as 1 m², which it was not. The 2 m² size has to be "
                    "accounted for first."},
            {"text": "The mean itself, which needs to be doubled before "
                     "anything else is done.", "correct": False,
             "why": "The mean of 8 was correctly measured for a 2 m² "
                    "quadrat — it does not need doubling. What changes is "
                    "how many quadrat-sized areas fit into the field."},
            {"text": "The field's total area, which must now be treated as a full 800 m² instead of the original 400 m².", "correct": False,
             "why": "The field's real area has not changed. What changes "
                    "is how many 2 m² areas fit inside that real, "
                    "unchanged 400 m²."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s24",
        "band": "standard",
        "text": "A group only samples plants that are easy to identify, "
                "skipping any they are unsure about. What kind of error "
                "does that introduce?",
        "options": [
            {"text": "A chance error, since which plants are hard to "
                     "identify varies from day to day.", "correct": False,
             "why": "This error does not vary randomly — the same kinds "
                    "of plant are skipped every time because the group "
                    "cannot identify them, in every quadrat, every day."},
            {"text": "A bias, because certain plants are being left out "
                     "of every count on purpose.", "correct": True},
            {"text": "No error at all, since only genuinely real observations are ever being recorded here.", "correct": False,
             "why": "Recording only what is easy to identify quietly "
                    "leaves out a whole category of plant from every "
                    "count. That is still an error, and a systematic "
                    "one."},
            {"text": "A quadrat-size error, since harder plants tend to "
                     "be smaller.", "correct": False,
             "why": "This is not about the size of the frame at all. It "
                    "is about which plants are consistently excluded from "
                    "being counted, regardless of size."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s25",
        "band": "standard",
        "text": "Why is capture–mark–recapture used for animals like "
                "woodmice, rather than the quadrat method used for "
                "daisies?",
        "options": [
            {"text": "Because animals are always rarer than plants in "
                     "any habitat.", "correct": False,
             "why": "Rarity is not the deciding factor — some plants are "
                    "far rarer than common animals. The issue is that "
                    "animals move and plants do not."},
            {"text": "Because quadrats can only ever be square in shape, and animals always need a proper round trap instead.", "correct": False,
             "why": "The shape of the frame is not the reason. A moving "
                    "animal will not stay inside a fixed square to be "
                    "counted, whatever its shape."},
            {"text": "Because a quadrat cannot hold a moving animal "
                     "still long enough to be counted where it was "
                     "placed.", "correct": True},
            {"text": "Because capture–mark–recapture always gives a far more exact answer than any ordinary quadrat survey ever could.",
             "correct": False,
             "why": "Both methods produce an estimate, with their own "
                    "sources of error. Neither is claimed to be exact."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s26",
        "band": "standard",
        "text": "A group samples a field using random coordinates, but "
                "throws back any quadrat that lands on the muddy path "
                "running through it, choosing a new random position "
                "instead. Is this still a fair, random sample?",
        "options": [
            {"text": "Yes — throwing back an inconvenient result and simply drawing another random one in its place keeps everything fair.",
             "correct": False,
             "why": "Deliberately rejecting positions on the path means "
                    "the path is never sampled, which is a choice about "
                    "where to look, however random the replacement "
                    "position is."},
            {"text": "Yes, as long as the brand new replacement position is still chosen properly using random numbers each time.", "correct": False,
             "why": "Even a randomly chosen replacement cannot undo the "
                    "fact that the path itself is systematically excluded "
                    "from ever being picked."},
            {"text": "It cannot be judged without knowing how wide the "
                     "path is.", "correct": False,
             "why": "The width of the path does not change the "
                    "principle. Excluding it on purpose removes part of "
                    "the field from the sample, whatever its size."},
            {"text": "No — deliberately avoiding the path means part of "
                     "the field is never given a chance of being "
                     "sampled.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s27",
        "band": "standard",
        "text": "A survey using 1 m² quadrats gives a mean of 4 daisies "
                "per quadrat and a population estimate of 3,200. What is "
                "the area of the field?",
        "options": [
            {"text": "800 m².", "correct": True},
            {"text": "12,800 m², multiplying the estimate by the mean.",
             "correct": False,
             "why": "Multiplying makes the field far too large. Dividing "
                    "the estimate by the mean gives the number of "
                    "quadrat-sized areas, which is the field's area here."},
            {"text": "3,196 m².", "correct": False,
             "why": "That subtracts the mean from the estimate, and "
                    "subtraction has no place in this calculation. The "
                    "field's area comes from dividing the estimate by the "
                    "mean count."},
            {"text": "80 m², dividing by forty instead of four.",
             "correct": False,
             "why": "The mean here is four, not forty. Dividing 3,200 by "
                    "the correct mean of four gives 800 m², not 80 m²."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s28",
        "band": "standard",
        "text": "A survey is carried out on a single sunny afternoon in "
                "July. A second, otherwise identical survey is carried out "
                "on a cold, wet morning in November. Would you expect the "
                "two population estimates for an insect to be directly "
                "comparable?",
        "options": [
            {"text": "Yes — as long as exactly the same method was used both times, the season and the weather make no real difference.", "correct": False,
             "why": "Method being identical does not cancel out the "
                    "effect of season on an insect's activity and "
                    "numbers, which genuinely differ between July and "
                    "November."},
            {"text": "No — season and weather can change how active or "
                     "abundant the insect is, not just how well it is "
                     "sampled.", "correct": True},
            {"text": "Yes, because insects are counted the same way "
                     "whatever the temperature.", "correct": False,
             "why": "Being counted the same way is not the issue. The "
                    "insect's own numbers and behaviour are likely to be "
                    "genuinely different in November."},
            {"text": "No, because quadrat surveys can only be carried out "
                     "in summer.", "correct": False,
             "why": "Quadrat surveys can be carried out in any season — "
                    "the method itself is not seasonal. The problem is "
                    "comparing an insect's summer and winter numbers as "
                    "if they were the same thing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s29",
        "band": "standard",
        "text": "A survey's random number generator is later found to have "
                "been broken, always producing numbers between 1 and 20 "
                "instead of the full range up to 100. What has actually "
                "happened to the sample?",
        "options": [
            {"text": "It is still random, just drawn from a smaller "
                     "range of numbers.", "correct": False,
             "why": "Randomness is not rescued by staying random within "
                    "a narrow range. Restricting every position to one "
                    "corner of the site is exactly a form of bias."},
            {"text": "Nothing has changed, since the numbers were still "
                     "generated by a machine rather than a person.",
             "correct": False,
             "why": "A machine can produce a biased sample just as "
                    "easily as a person can, if the numbers it gives only "
                    "ever cover part of the site."},
            {"text": "It has become biased towards one part of the site, "
                     "even though numbers were still drawn by chance.",
             "correct": True},
            {"text": "The sample has become more reliable, since a "
                     "narrower range of numbers is easier to work with.",
             "correct": False,
             "why": "Ease of arithmetic has nothing to do with whether "
                    "the sample fairly represents the site. Restricting "
                    "the range has introduced a bias, not an improvement."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-s30",
        "band": "standard",
        "text": "A survey of a 1,000 m² field uses 5 quadrats of 1 m² and "
                "reports a confident, precise-looking estimate. A second "
                "survey of an identical field uses 40 quadrats and reports "
                "an estimate with a visibly wider stated range of "
                "uncertainty. Which survey should be trusted more?",
        "options": [
            {"text": "The first, since it gives one single, more "
                     "precise-looking number.", "correct": False,
             "why": "Looking precise is not the same as being reliable. "
                    "A confident number from only five quadrats hides how "
                    "little evidence it is built on."},
            {"text": "Neither can really be trusted at all, since population estimates of any kind are never properly reliable to begin with, whatever the sample size.", "correct": False,
             "why": "Estimates from a well-designed random sample are "
                    "genuinely useful, which is the whole basis of this "
                    "method. The two surveys are not equally good, "
                    "though."},
            {"text": "Both equally, since they surveyed identical "
                     "fields.", "correct": False,
             "why": "The fields being identical does not make the two "
                    "surveys equally reliable. The size of the sample "
                    "taken from each field is what differs, and that "
                    "matters."},
            {"text": "The second — more quadrats give a better basis for "
                     "the estimate, even reported with a stated range "
                     "rather than one sharp figure.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-06-h09",
        "band": "harder",
        "text": "An ecologist marks 80 voles and later catches 100, of "
                "which 16 are marked. The study area is 4 hectares "
                "(40,000 m²). What is the estimated density of voles, in "
                "voles per m²?",
        "options": [
            {"text": "0.0125 voles per m².", "correct": True},
            {"text": "500 voles per m², since that is the estimated "
                     "population.", "correct": False,
             "why": "500 is the estimated total population of the whole "
                    "area, not a density. Density is the population "
                    "divided by the area."},
            {"text": "0.02 voles per m², dividing the population by "
                     "25,000.", "correct": False,
             "why": "The area given is 40,000 m², not 25,000 m². "
                    "Dividing 500 by the correct area gives 0.0125, not "
                    "0.02."},
            {"text": "125 voles per m².", "correct": False,
             "why": "That multiplies the population by the area instead "
                    "of dividing, which makes the density far too large. "
                    "Density is the population divided by the area."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h10",
        "band": "harder",
        "text": "A group takes 3 quadrats, all near a gate where the "
                "ground is heavily trampled, and gets a low estimate. "
                "Another group takes 3 quadrats at genuinely random "
                "positions and also gets a low estimate, purely by chance. "
                "Both report the same low figure. Are both errors the same "
                "kind?",
        "options": [
            {"text": "Yes — since both figures came out equally low, both surveys must clearly be affected by the very same kind of error.", "correct": False,
             "why": "Two errors can look identical in size and still "
                    "differ in kind. One is a fixed direction that "
                    "repeating will not fix; the other is not."},
            {"text": "No — the first is bias, which more quadrats will "
                     "not fix; the second is chance, which more quadrats "
                     "would fix.", "correct": True},
            {"text": "No — the first is chance and the second is bias, "
                     "the reverse of what you might expect.", "correct": False,
             "why": "The gate-side group chose where to sample, which is "
                    "bias by definition. The randomly placed group's low "
                    "figure is simply an unlucky draw — that is chance."},
            {"text": "Yes, because both groups took exactly three "
                     "quadrats.", "correct": False,
             "why": "Matching sample sizes does not make the underlying "
                    "errors the same kind. One group chose where to look; "
                    "the other did not."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h11",
        "band": "harder",
        "text": "A patchy plant gives wildly different counts between "
                "quadrats. Would doubling the size of each quadrat, while "
                "keeping the same total number of quadrats, fix the "
                "problem the way taking more quadrats of the original "
                "size would?",
        "options": [
            {"text": "Yes — either change works in exactly the same way as the other, since both of them simply increase the total area of ground being sampled overall.",
             "correct": False,
             "why": "Both do increase the total ground sampled, and that "
                    "alone does not make them interchangeable — a few "
                    "large squares can behave quite differently from many "
                    "small ones."},
            {"text": "No — quadrat size can never be changed once a "
                     "survey has begun.", "correct": False,
             "why": "Nothing here is about changing a size mid-survey; "
                    "the question compares two different survey designs "
                    "decided in advance."},
            {"text": "Not necessarily the same way — larger quadrats may "
                     "average out a patch within each square, while more "
                     "quadrats average across many separate results.",
             "correct": True},
            {"text": "No — larger quadrats always introduce bias that "
                     "smaller ones do not.", "correct": False,
             "why": "Quadrat size on its own does not create bias — bias "
                    "comes from how positions are chosen, not from the "
                    "size of the frame used at each one."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h12",
        "band": "harder",
        "text": "In a mark-recapture study, 120 fish are marked. Later, 80 "
                "are caught, and a quarter of that second catch are "
                "carrying a mark. What is the estimated population?",
        "options": [
            {"text": "20.", "correct": False,
             "why": "Twenty is the number of marked fish found in the "
                    "second catch — a figure used inside the calculation, "
                    "not the final population estimate."},
            {"text": "320, scaling up the second catch of 80 rather than "
                     "the 120 that were marked.", "correct": False,
             "why": "The marked quarter scales up the number that was "
                    "marked, not the size of the second catch. The method "
                    "is (first catch × second catch) ÷ number recaptured "
                    "marked: (120 × 80) ÷ 20 = 480."},
            {"text": "9,600, multiplying the two catches together and "
                     "stopping there.", "correct": False,
             "why": "Multiplying the two catches is only the first half "
                    "of the method. The calculation is (first catch × "
                    "second catch) ÷ number recaptured marked."},
            {"text": "480.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h13",
        "band": "harder",
        "text": "A professional ecological survey reports its population "
                "estimate together with a range, such as '2,000 to 2,600 "
                "daisies', rather than one single number. Why is giving a "
                "range more honest than giving one figure?",
        "options": [
            {"text": "Because it shows how much the true figure could "
                     "plausibly vary, given that only a sample was "
                     "taken.", "correct": True},
            {"text": "Because a range is always going to be a considerably bigger-looking number than any single estimate would be.", "correct": False,
             "why": "Size is not the point of giving a range. A range "
                    "communicates how uncertain the estimate is, which "
                    "one number alone cannot."},
            {"text": "Because a single number would break scientific "
                     "reporting rules everywhere.", "correct": False,
             "why": "There is no such universal rule being broken by a "
                    "single figure. A range is preferred because it is "
                    "more informative, not because a single number is "
                    "forbidden."},
            {"text": "Because ranges are easier to calculate than an "
                     "exact mean.", "correct": False,
             "why": "A range is not simpler to calculate — if anything "
                    "it takes more information to produce. It is used "
                    "because it is honest about uncertainty."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h14",
        "band": "harder",
        "text": "A survey of nettles is both biased, because every "
                "quadrat was placed along one hedge, and uses quadrats too "
                "small for how clumped nettles grow. The team can only "
                "afford to fix ONE of the two problems this year. Which "
                "fix would make the bigger difference to how trustworthy "
                "the final figure is?",
        "options": [
            {"text": "Fixing the quadrat size, since an unsteady "
                     "estimate is worse than a biased one.", "correct": False,
             "why": "An unsteady estimate is at least honestly "
                    "unreliable and would improve with more or larger "
                    "quadrats next time. A biased one looks confident "
                    "while being systematically wrong."},
            {"text": "Fixing the bias, by placing quadrats randomly "
                     "across the whole site rather than along one hedge.",
             "correct": True},
            {"text": "Neither — both of the two problems have to be fixed together, or fixing either one on its own is pointless.", "correct": False,
             "why": "Fixing either problem alone genuinely improves the "
                    "survey somewhat; it is not all-or-nothing here."},
            {"text": "It makes no real difference which is fixed first at all, since both errors are assumed to be the same size.", "correct": False,
             "why": "Nothing in the case says the two errors are the "
                    "same size, and bias and unsteadiness behave "
                    "completely differently under repetition regardless."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h15",
        "band": "harder",
        "text": "A long-running UK garden bird survey reports that a "
                "common species has declined by roughly a third since the "
                "1970s, based on tens of thousands of gardens surveyed the "
                "same way every year. Why does the large number of gardens "
                "matter here, beyond simply reducing chance error?",
        "options": [
            {"text": "It guarantees the survey cannot be biased in any "
                     "way.", "correct": False,
             "why": "No number of gardens, however large, guarantees the "
                    "absence of bias — if every garden were the same "
                    "type, the same bias could still run through all of "
                    "them."},
            {"text": "It means the birds themselves must genuinely be less common now than they were fifty years ago, regardless of absolutely anything else that could be considered.",
             "correct": False,
             "why": "The number of gardens sampled does not by itself "
                    "prove anything about the bird's real numbers. It is "
                    "the comparability of the method that supports the "
                    "claim."},
            {"text": "It also means the survey reaches many different "
                     "kinds of garden and area, reducing the risk that "
                     "one region's bias is mistaken for a national "
                     "trend.", "correct": True},
            {"text": "It removes the need to repeat the survey using the "
                     "same method each year.", "correct": False,
             "why": "Repeating the same method every year is exactly "
                    "what makes a fifty-year trend claim possible in the "
                    "first place — a large one-off count could not do "
                    "that."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h16",
        "band": "harder",
        "text": "A routine yearly butterfly count on a reserve suddenly "
                "reports triple the usual number, using the same method as "
                "every previous year. What is the most sensible next step, "
                "rather than simply accepting or rejecting the figure?",
        "options": [
            {"text": "Reject the new figure automatically and without any further question, since it is so wildly different from every single previous year's count on record.",
             "correct": False,
             "why": "A real, unusually good breeding year could "
                    "genuinely triple a population — rejecting it "
                    "outright assumes the answer before checking "
                    "anything."},
            {"text": "Accept the figure without question, since the same "
                     "method was used as before.", "correct": False,
             "why": "Using the same named method does not rule out "
                    "something going wrong in this particular year's "
                    "execution of it — a warm, sunny count day can itself "
                    "triple a butterfly count."},
            {"text": "Average this year's figure with several previous "
                     "years' figures and report that instead.",
             "correct": False,
             "why": "Quietly averaging away an unusual result hides a "
                    "genuine finding just as much as blindly accepting or "
                    "rejecting it does. The sensible step is to "
                    "investigate the figure."},
            {"text": "Check whether anything about the count itself "
                     "changed — weather, timing, observer — before "
                     "concluding the population has really tripled.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h17",
        "band": "harder",
        "text": "A survey of 15 quadrats of 2 m² each, on a 750 m² "
                "meadow, gives individual counts of 4, 6, 5, 3, 7, 4, 5, "
                "6, 4, 5, 3, 6, 5, 4 and 8 clover plants. What is the "
                "estimated population, to the nearest hundred?",
        "options": [
            {"text": "About 1,900.", "correct": True},
            {"text": "About 3,750, treating each quadrat as 1 m².",
             "correct": False,
             "why": "Each quadrat here is 2 m², not 1 m². Using the "
                    "correct area gives roughly half this figure."},
            {"text": "About 75.", "correct": False,
             "why": "Seventy-five is the total count across all fifteen "
                    "quadrats — what was actually found in the thirty "
                    "square metres surveyed. It still needs scaling up to "
                    "the whole 750 m² meadow."},
            {"text": "About 5, reporting the mean per quadrat rather "
                     "than the whole-field estimate.", "correct": False,
             "why": "Five is the mean count per quadrat, a genuinely "
                    "useful figure on the way to the answer, but it is "
                    "not itself the population of the whole meadow."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h18",
        "band": "harder",
        "text": "A mark-recapture study is repeated a full year after the "
                "marking, rather than a few days later. Even with careful "
                "technique, why would this estimate be far less "
                "trustworthy than a quicker one?",
        "options": [
            {"text": "Because marks always fade completely from an "
                     "animal's body within a few weeks.", "correct": False,
             "why": "Some marks do fade eventually, and that is not the "
                    "deepest problem here — even a mark lasting the whole "
                    "year would not fix the fact that the population has "
                    "likely changed shape over that time."},
            {"text": "Because the population is unlikely to be the same "
                     "closed group a year later — animals will have been "
                     "born, died, and moved in or out.", "correct": True},
            {"text": "Because the second catch would always be smaller "
                     "after such a long gap.", "correct": False,
             "why": "There is no reason the second catch must be smaller "
                    "after a year — it could be larger or smaller. The "
                    "real issue is whether the population is still "
                    "comparable at all."},
            {"text": "Because scientists are formally not permitted, under any circumstances whatsoever, to run a mark-recapture study for longer than a few days at most.", "correct": False,
             "why": "There is no such rule against longer studies. The "
                    "genuine problem is a scientific one about the "
                    "population no longer being fixed."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h19",
        "band": "harder",
        "text": "A charity estimates a rare beetle's numbers on one small "
                "nature reserve very carefully, then multiplies that "
                "figure up to estimate the beetle's total population "
                "across the whole country. What is the flaw in doing "
                "that?",
        "options": [
            {"text": "Multiplying is mathematically impossible once "
                     "decimal numbers are involved.", "correct": False,
             "why": "Multiplying decimal figures is ordinary arithmetic "
                    "and causes no problem here. The flaw is a scientific "
                    "one about what the reserve's figure can represent."},
            {"text": "A single reserve can never be surveyed accurately, "
                     "however carefully it is done.", "correct": False,
             "why": "The reserve's own survey can be done very well, and "
                    "the case says it was. The problem is treating that "
                    "one careful result as if it applied everywhere."},
            {"text": "The reserve may never be a fair sample of habitat "
                     "conditions across the whole country.", "correct": True},
            {"text": "Rare species cannot be estimated by any "
                     "quadrat-based method.", "correct": False,
             "why": "Quadrat and mark-recapture methods work for rare "
                    "species just as they do for common ones — rarity "
                    "affects the effort needed, not whether the method "
                    "works."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h20",
        "band": "harder",
        "text": "Counting every daisy in a 10,000 m² field by hand would "
                "take a class about 40 hours. A random sample of 30 "
                "quadrats, each 1 m², takes about 45 minutes and gives an "
                "estimate expected to be within roughly 10% of the true "
                "figure. Is the trade-off generally considered "
                "worthwhile?",
        "options": [
            {"text": "No — any error at all makes an estimate worthless "
                     "compared with an exact count.", "correct": False,
             "why": "A small, known, honestly reported error is far more "
                    "useful in practice than a task nobody has 40 hours "
                    "for. Worthless overstates what a 10% margin costs."},
            {"text": "No — a 45-minute survey can never be trusted for "
                     "any scientific purpose.", "correct": False,
             "why": "Plenty of trustworthy ecological science is built "
                    "on samples taking far less time than a full count "
                    "would. Trustworthiness comes from the method, not "
                    "the time spent."},
            {"text": "Yes, because a full hand count of every single daisy in the field would actually give a less accurate answer than a random sample would.", "correct": False,
             "why": "A full, accurate count would in principle be the "
                    "most accurate answer possible, not less accurate "
                    "than a sample. The trade-off is about effort, not "
                    "accuracy."},
            {"text": "Yes — the huge saving in time for a small, known "
                     "margin of error is exactly the trade-off ecological "
                     "sampling exists to make.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h21",
        "band": "harder",
        "text": "A mark used in a vole study is later found to make "
                "marked voles very slightly more visible to owls than "
                "unmarked ones. Which direction would this push the final "
                "population estimate?",
        "options": [
            {"text": "It would push the estimate up, since predation on "
                     "marked voles lowers the marked fraction found in "
                     "the second catch.", "correct": True},
            {"text": "It would push the estimate down, since fewer "
                     "marked voles would survive to be caught again, "
                     "raising the marked fraction of survivors.",
             "correct": False,
             "why": "Fewer surviving marked voles LOWERS the marked "
                    "fraction of the second catch, not raises it — and a "
                    "lower marked fraction pushes the estimate up, not "
                    "down."},
            {"text": "It would have no effect, since predation removes "
                     "marked and unmarked voles equally.", "correct": False,
             "why": "The case specifically says marked voles are more "
                    "visible to owls, so predation here does not remove "
                    "both groups equally — that is exactly what breaks "
                    "the assumption."},
            {"text": "It cannot be predicted, since predation is always "
                     "completely random.", "correct": False,
             "why": "This predation is not random here — it specifically "
                    "targets marked voles more than unmarked ones, which "
                    "is precisely why it has a predictable effect."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h22",
        "band": "harder",
        "text": "In one mark-recapture study, some marked animals emigrate "
                "out of the study area before the second catch (lowering "
                "the marked fraction found), while at the same time a few "
                "new unmarked animals immigrate in (also lowering the "
                "marked fraction). What would you expect the resulting "
                "population estimate to be?",
        "options": [
            {"text": "Too low, since both effects cancel each other out "
                     "perfectly.", "correct": False,
             "why": "Both effects push the marked fraction the same "
                    "way — down — rather than cancelling. Two effects "
                    "reinforcing each other cannot be expected to cancel "
                    "to zero."},
            {"text": "Too high, since both changes lower the marked "
                     "fraction found in the second catch.", "correct": True},
            {"text": "Exactly correct, since emigration and immigration "
                     "are opposite processes that balance.", "correct": False,
             "why": "Being opposite kinds of movement does not mean "
                    "their effect on this calculation cancels — both act "
                    "here to lower the marked fraction, in the same "
                    "direction."},
            {"text": "Impossible to reason about at all, without knowing the exact numbers involved in each catch.", "correct": False,
             "why": "The direction of the effect can be reasoned about "
                    "without exact numbers — both changes lower the "
                    "marked fraction, and a lower marked fraction always "
                    "raises the estimate."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h23",
        "band": "harder",
        "text": "A survey of an annual wildflower is carried out in early "
                "spring, while many seedlings are too small to identify "
                "confidently and are left uncounted. What effect is this "
                "likely to have on the population estimate?",
        "options": [
            {"text": "It would have no effect at all, since tiny seedlings are not fully grown adult plants and should never be counted anyway.",
             "correct": False,
             "why": "The case does not say seedlings are being excluded "
                    "on purpose — it says they are being missed because "
                    "they are hard to identify, which is a sampling flaw."},
            {"text": "It would overestimate the population instead, since spring counts are always thought to be higher than summer ones.",
             "correct": False,
             "why": "Missing a category of the plant can only push a "
                    "count down, not up. There is also no general rule "
                    "that spring counts run higher than summer ones."},
            {"text": "It would tend to underestimate the true "
                     "population, since a real category of the plant is "
                     "being missed.", "correct": True},
            {"text": "It would make the estimate more precise, since "
                     "fewer individuals need to be told apart.",
             "correct": False,
             "why": "Missing individuals does not improve precision — it "
                    "introduces a systematic gap in what is being "
                    "counted, which is a bias, not an improvement."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h24",
        "band": "harder",
        "text": "A charity with limited funding for one season's survey "
                "must choose between (A) 100 quadrats placed randomly "
                "across one representative-looking corner of a large "
                "reserve, or (B) 20 quadrats placed randomly across the "
                "whole reserve. Which is more likely to give a "
                "trustworthy estimate of the reserve's total population, "
                "and why?",
        "options": [
            {"text": "Option A, because a hundred quadrats is a much "
                     "larger sample than twenty.", "correct": False,
             "why": "A large sample confined to one corner still only "
                    "describes that corner. Sample size does not rescue a "
                    "sample never spread across the area being estimated."},
            {"text": "Neither, because both survey designs use genuinely random placement and so must therefore be equally reliable overall.", "correct": False,
             "why": "Random placement within a chosen area removes bias "
                    "inside that area — it does not fix the deeper "
                    "problem of only ever choosing one small area."},
            {"text": "Option A, because more quadrats always beats a "
                     "wider spread, whatever the design.", "correct": False,
             "why": "More quadrats fixes chance error, not the risk that "
                    "an entire chosen area fails to represent the wider "
                    "reserve."},
            {"text": "Option B, because covering the whole reserve "
                     "avoids the risk that one corner is not "
                     "representative of the rest.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h25",
        "band": "harder",
        "text": "Site X is estimated at 500 plants (which could plausibly "
                "be anywhere from 400 to 600), and Site Y is estimated at "
                "550 plants (which could plausibly be anywhere from 450 "
                "to 650). Can you confidently say Site Y has more plants "
                "than Site X?",
        "options": [
            {"text": "Not confidently — the two plausible ranges overlap "
                     "so much that the real difference could easily be "
                     "zero or even reversed.", "correct": True},
            {"text": "Yes — 550 is quite simply a larger number than 500 is, so Site Y must therefore clearly have more plants growing there than Site X does.", "correct": False,
             "why": "The two ranges overlap heavily — a real value of "
                    "500 for both sites is entirely possible within the "
                    "stated uncertainty."},
            {"text": "Yes, because Site Y's range extends higher than "
                     "Site X's does.", "correct": False,
             "why": "Both ranges extend to similarly high and similarly "
                    "low values, and they overlap across most of their "
                    "length. A higher top end alone does not settle it."},
            {"text": "No comparison is possible at all between two "
                     "different estimates.", "correct": False,
             "why": "A comparison is possible — it is just not a "
                    "confident one, given how much the two plausible "
                    "ranges overlap."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h26",
        "band": "harder",
        "text": "Going from 5 to 20 quadrats sharply narrows a population "
                "estimate's likely range of error. Going from 100 to 400 "
                "quadrats narrows it by a similar proportion, but for four "
                "times the extra fieldwork. What general pattern does "
                "this illustrate about sample size?",
        "options": [
            {"text": "That larger samples always give proportionally bigger improvements in overall reliability for exactly the same amount of extra fieldwork effort.", "correct": False,
             "why": "This is the opposite of the pattern described — "
                    "going from 100 to 400 costs far more effort for a "
                    "similar proportional gain."},
            {"text": "That there are diminishing returns — each further "
                     "batch of extra quadrats buys progressively less "
                     "improvement for the effort spent.", "correct": True},
            {"text": "That bias becomes a bigger problem once the sample "
                     "size passes about 100 quadrats.", "correct": False,
             "why": "Nothing in the case is about bias at all — both "
                    "comparisons describe random, unbiased sampling at "
                    "different sizes."},
            {"text": "That population estimates stop improving "
                     "completely once more than 20 quadrats are used.",
             "correct": False,
             "why": "The estimate does keep improving further, from 100 "
                    "to 400 quadrats — just by a smaller amount for the "
                    "effort involved, not by nothing at all."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h27",
        "band": "harder",
        "text": "A reserve manager wants to know whether a new mowing "
                "regime has increased the number of orchids on a meadow. "
                "What would make the 'before' and 'after' surveys a fair "
                "comparison?",
        "options": [
            {"text": "Making sure more quadrats are used in the 'after' "
                     "survey, since the orchids are expected to have "
                     "increased.", "correct": False,
             "why": "Deliberately using more effort in the survey you "
                    "expect to show a rise stacks the comparison in "
                    "favour of finding one, rather than testing it "
                    "fairly."},
            {"text": "Surveying the 'after' meadow in a different season "
                     "from the 'before' one, to catch the orchids at "
                     "their best.", "correct": False,
             "why": "Comparing different seasons compares two different "
                    "things — orchid numbers naturally change across a "
                    "year regardless of any mowing change."},
            {"text": "Using the same sampling method, the same time of "
                     "year, and ideally the same quadrat positions or a "
                     "comparably random set, in both years.", "correct": True},
            {"text": "Counting every single orchid in the 'after' survey, rather than sampling it at all, since a full and complete count is supposedly always available anyway.", "correct": False,
             "why": "A full count is not simply available whenever "
                    "wanted — it faces the same practical limits as any "
                    "other count. The comparison also needs a matching "
                    "method on both occasions."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h28",
        "band": "harder",
        "text": "A council uses a large, 200-quadrat survey to argue that "
                "a wetland's rare orchid population is healthy and "
                "building permission should be granted nearby. All 200 "
                "quadrats were placed along the single, easily accessible "
                "boardwalk through the site. What is the strongest "
                "scientific objection to this evidence?",
        "options": [
            {"text": "Two hundred quadrats is not a large enough sample "
                     "to draw any conclusion from.", "correct": False,
             "why": "Two hundred is a genuinely large number of "
                    "quadrats — sample size is not the weak point in this "
                    "survey. Where they were all placed is."},
            {"text": "Quadrat surveys can never be used to support a "
                     "planning decision of any kind.", "correct": False,
             "why": "Quadrat surveys are routinely used to inform real "
                    "planning and conservation decisions when properly "
                    "designed. The objection here is to this survey's "
                    "design."},
            {"text": "The orchid population must actually be unhealthy in reality, since the council clearly has a financial interest in this particular outcome.",
             "correct": False,
             "why": "Who commissioned a survey does not by itself tell "
                    "you whether its findings are correct. The objection "
                    "is about the survey's design, not assumed bad "
                    "faith."},
            {"text": "However large the sample, confining every quadrat "
                     "to the boardwalk means the survey may not represent "
                     "the rest of the wetland at all.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h29",
        "band": "harder",
        "text": "A group insists their sample is trustworthy because 'we "
                "took loads of quadrats, and we were really careful about "
                "exactly where we put each one so it looked fair.' What is "
                "the flaw in that reasoning?",
        "options": [
            {"text": "Choosing each position carefully, even with good "
                     "intentions, is not the same as choosing them by "
                     "chance — and no sample size can fix that.",
             "correct": True},
            {"text": "There is no flaw whatsoever here — a large, carefully and deliberately placed sample is exactly what genuinely good sampling is always supposed to look like.",
             "correct": False,
             "why": "Careful placement by the surveyor is precisely what "
                    "makes a sample biased, however fair it looks to "
                    "them — and no sample size fixes that."},
            {"text": "The problem is only that they did not use quite "
                     "enough quadrats.", "correct": False,
             "why": "The stated problem is not the number of quadrats, "
                    "which the group describes as large — it is that "
                    "every position was chosen deliberately."},
            {"text": "There is no way to know if a sample is "
                     "trustworthy, whatever method is used.", "correct": False,
             "why": "A truly random, appropriately sized sample is a "
                    "trustworthy basis for an estimate. This sample fails "
                    "because its positions were chosen by eye, not "
                    "because trustworthiness is unknowable."},
        ],
        "figure": None,
    },
    {
        "id": "b9-06-h30",
        "band": "harder",
        "text": "Rank these four surveys of the same field, from LEAST to "
                "MOST trustworthy as a basis for a population estimate: "
                "(1) 5 quadrats placed by eye, sized correctly; (2) 5 "
                "quadrats placed randomly, but far too small for the "
                "plant; (3) 40 quadrats placed by eye, sized correctly; "
                "(4) 40 quadrats placed randomly, sized correctly.",
        "options": [
            {"text": "1, 2, 3, 4 — since each survey in this order "
                     "simply uses more effort than the last.",
             "correct": False,
             "why": "Effort spent is not what should order these — "
                    "survey 3 uses forty quadrats but is still biased, "
                    "which no amount of extra effort fixes."},
            {"text": "2, 1, 3, 4 — small-but-random beats any biased "
                     "survey, however many quadrats the biased ones use; "
                     "and full random sampling with enough, correctly "
                     "sized quadrats is best of all.", "correct": True},
            {"text": "1, 3, 2, 4 — more quadrats always beats fewer regardless of anything else, so the two biased surveys should simply rank by their quadrat count first, ahead of the unsteady one.", "correct": False,
             "why": "Ranking the two biased surveys by quadrat count "
                    "alone ignores that survey 2, though small and "
                    "unsteady, is not systematically wrong in one fixed "
                    "direction the way both biased surveys are."},
            {"text": "4, 3, 2, 1 — since larger sample sizes should "
                     "always be trusted over smaller ones, regardless of "
                     "anything else.", "correct": False,
             "why": "This puts survey 3, which is biased despite its "
                    "forty quadrats, above the honestly small-but-random "
                    "survey 2 — sample size alone cannot make a biased "
                    "survey more trustworthy than an unbiased one."},
        ],
        "figure": None,
    },
]
