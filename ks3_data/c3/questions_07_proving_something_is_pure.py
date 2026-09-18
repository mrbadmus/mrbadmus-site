"""C3 lesson 07 — Proving something is pure: twelve questions (MRB-269).

The lesson's argument is that a claim of purity is settled by a measurement
with a known expected value, and by nothing you can see: a pure substance melts
sharply at one temperature, a mixture melts over a range and starts lower, and
neither fact is worth anything from a single run. These twelve probe that
argument from the angles the ladder leaves alone — what the plan's four
observations could and could not have shown, what a fast block does to a table
of readings, what happens to the one run that disagrees, and what the
measurement still cannot tell you once it has caught an impure batch.

The distractors are built from the lesson's two declared misconceptions.
MIX-02 (if it looks the same all the way through, it is pure) drives the wrong
options in e01, e02 and h01 — every one of them offers a LOOK, at higher
magnification or after dissolving, as the evidence. MIX-13 (one measurement is
enough if it is the right answer) drives s01, s02 and h04, where a reading is
trusted because it landed on the expected value, or because three runs done the
same wrong way agreed with each other.

Two further strands run through the lesson and are not in the register. The
first is that an odd result is a mistake to be tidied away — deleted, averaged
in, or promoted to a verdict — and it carries e04, s03 and h02. The second is
that a measurement with no expected value to compare against can still settle
something: e03, s04 and h03 each carry a distractor that weighs, or measures
more precisely, and expects an answer out of it.
"""

UNIT = "C3"
LESSON = "proving-something-is-pure"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c3-07-e01",
        "band": "easier",
        "text": "A white solid starts to melt at 45 °C and has not finished "
                "melting until 52 °C. The pure substance melts at 53 °C. What "
                "does that say about the solid?",
        "options": [
            {"text": "It is impure — a mixture melts over a range, and starts "
                     "lower than the pure substance", "correct": True},
            {"text": "It is pure, because it melted below the expected "
                     "temperature", "correct": False,
             "why": "Melting low is not a sign of purity — it is one of the "
                    "two signs of a mixture, and the seven-degree range is "
                    "the other."},
            {"text": "It is pure, but the thermometer was reading about eight "
                     "degrees low", "correct": False,
             "why": "A thermometer reading low would shift the start and the "
                    "finish down together and would still give a sharp melt. "
                    "Nothing about it turns half a degree into seven."},
            {"text": "Nothing yet — it would have to be looked at under a "
                     "hand lens before anything is decided", "correct": False,
             "why": "Looking is the one test in this lesson that settles "
                    "nothing, and the measurement has already answered the "
                    "question."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e02",
        "band": "easier",
        "text": "A student looks at a white powder under a hand lens, sees "
                "that the crystals all look the same, and writes that the "
                "powder is pure. What is wrong with that?",
        "options": [
            {"text": "Nothing at all — crystals that all look the same is "
                     "exactly what being pure means", "correct": False,
             "why": "Being pure is about what the sample is made of, not what "
                    "it looks like. This is the idea the whole unit exists to "
                    "correct."},
            {"text": "The crystals should have been looked at under a "
                     "microscope instead", "correct": False,
             "why": "More magnification does not rescue it. A closer look at "
                    "two white powders ground together still shows white "
                    "powder."},
            {"text": "Two powders ground together look like one powder, so "
                     "the look settles nothing", "correct": True},
            {"text": "A hand lens shows the shape of the crystals but not "
                     "their colour", "correct": False,
             "why": "Colour is one more thing to look at, and looking is what "
                    "has already failed. Two white solids mixed together are "
                    "still white."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e03",
        "band": "easier",
        "text": "One step of the student's plan was to weigh 10 g of the "
                "powder and check that it weighs 10 g. Why does that settle "
                "nothing?",
        "options": [
            {"text": "Mass tells you how much you have, never what it is",
             "correct": True},
            {"text": "A school balance is not accurate enough to read 10 g",
             "correct": False,
             "why": "A school balance reads 10 g perfectly well. The trouble "
                    "is not the instrument — it is that there is no expected "
                    "value for the reading to be compared against."},
            {"text": "The powder should have been weighed before and after "
                     "heating it", "correct": False,
             "why": "That is a different experiment, about mass being "
                    "conserved in a reaction. Neither weighing says what the "
                    "powder is made of."},
            {"text": "10 g is too small an amount to weigh reliably",
             "correct": False,
             "why": "The amount is not the problem. Weigh a kilogram of a "
                    "mixture and it still weighs exactly what a mixture "
                    "weighs."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e04",
        "band": "easier",
        "text": "Three batches are each melted three times, slowly. Batch 1 "
                "melts within a degree every time. Batch 2 melts over six or "
                "seven degrees, starting around 45 °C. Batch 3 melts within a "
                "degree twice and over four and a half degrees once. Which "
                "batch is the impure one?",
        "options": [
            {"text": "Batch 1, because it melts at the highest temperature",
             "correct": False,
             "why": "Batch 1 melts within a degree, at the temperature the "
                    "pure substance was expected to melt at. That is what a "
                    "pure sample looks like."},
            {"text": "Batch 2, because it melts low and over a wide range",
             "correct": True},
            {"text": "Batch 3, because one of its runs disagrees with the "
                     "other two", "correct": False,
             "why": "One run in three disagreeing is an anomaly, not a "
                    "mixture. Batch 3's other two runs melt within a degree, "
                    "at the expected temperature."},
            {"text": "Batches 2 and 3, because both gave a wide reading",
             "correct": False,
             "why": "Batch 3 gave one wide reading and two sharp ones. A "
                    "mixture melts over a range every time it is run, not "
                    "once in three."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c3-07-s01",
        "band": "standard",
        "text": "A student melts a sample once, gets 53 °C — exactly the "
                "expected value — and stops there. What is missing from that "
                "piece of evidence?",
        "options": [
            {"text": "Nothing, as long as the thermometer had been checked "
                     "beforehand", "correct": False,
             "why": "A checked thermometer still cannot tell you whether that "
                    "particular run was a good one. The reading needs "
                    "something of its own to agree with."},
            {"text": "A second sample from the same bag, weighed on a balance "
                     "first", "correct": False,
             "why": "Weighing adds nothing here. What is missing is another "
                    "melting run, so that the first one has something to be "
                    "checked against."},
            {"text": "Nothing, because the reading landed on exactly the "
                     "value that was expected", "correct": False,
             "why": "Landing on it is what makes it tempting. A fast run on "
                    "an impure sample can land near the expected value too, "
                    "which is why one reading is never the evidence."},
            {"text": "Repeats — one reading cannot tell you whether it was a "
                     "good reading", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s02",
        "band": "standard",
        "text": "The block is heated quickly, to save time. What does that do "
                "to the readings?",
        "options": [
            {"text": "Every reading comes out low, because the sample melts "
                     "before the block has reached that temperature",
             "correct": False,
             "why": "It is the other way round. The thermometer trails behind "
                    "the sample, so the temperature it shows when melting "
                    "starts is higher than the sample's, not lower."},
            {"text": "Every reading comes out higher, and the batches' ranges "
                     "are dragged towards each other", "correct": True},
            {"text": "Nothing, as long as the same fast rate is used on every "
                     "sample", "correct": False,
             "why": "Doing the same wrong thing to all three does not cancel "
                    "out. It shrinks the difference between them, and the "
                    "difference is the thing being measured."},
            {"text": "Nothing to the temperatures — heating rate changes how "
                     "long it takes", "correct": False,
             "why": "That would be true of a thermometer that kept up. Heat "
                    "the block fast and the reading trails the sample, so a "
                    "wide range reads narrower than it really is."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s03",
        "band": "standard",
        "text": "Batch 3 gives two runs that agree with each other and one "
                "that does not. What should be done with the odd run?",
        "options": [
            {"text": "Delete it, because it is obviously a mistake",
             "correct": False,
             "why": "It may well be a mistake, and deleting it hides that it "
                    "happened. A result nobody can see is a result nobody can "
                    "check."},
            {"text": "Average all three runs, so that nothing is thrown away",
             "correct": False,
             "why": "Averaging an anomaly in is worse than deleting it: it "
                    "drags the answer towards a run there is already reason "
                    "to distrust, and buries the fact that it happened."},
            {"text": "Report it, give a likely cause, set it aside and run it "
                     "again", "correct": True},
            {"text": "Keep it in the results and conclude that batch 3 is "
                     "impure after all", "correct": False,
             "why": "A mixture melts over a range every time it is run. Batch "
                    "3's other two runs melt within a degree, at the expected "
                    "temperature, so one wide run is an anomaly."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s04",
        "band": "standard",
        "text": "The melting points show that batch 2 has something else in "
                "it. The buyer now wants to know what has been added. What "
                "will tell them?",
        "options": [
            {"text": "A more careful melting point, measured to a tenth of a "
                     "degree", "correct": False,
             "why": "A more precise melting point still only says that "
                    "something is there. No amount of precision turns it into "
                    "an identification."},
            {"text": "Chromatography — a melting point says that something is "
                     "present, never what", "correct": True},
            {"text": "Weighing batch 2 and comparing it with a batch known to "
                     "be pure", "correct": False,
             "why": "Mass says how much there is, not what it is made of. A "
                    "bulked-out bag weighs exactly what a bulked-out bag "
                    "weighs."},
            {"text": "Melting a known pure sample beside it and comparing the "
                     "ranges", "correct": False,
             "why": "That is a good comparison, and it answers the question "
                    "that has already been answered — whether batch 2 is "
                    "impure, not what is in it."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c3-07-h01",
        "band": "harder",
        "text": "A powder looks uniform under a hand lens and dissolves "
                "completely in water, leaving nothing behind. A student says "
                "the two results together prove it is pure. How far do they "
                "actually get?",
        "options": [
            {"text": "All the way — looking uniform and dissolving completely "
                     "is what pure means", "correct": False,
             "why": "Neither result can carry it. Two white powders ground "
                    "together look uniform, and an impurity that dissolves "
                    "leaves nothing behind to be seen."},
            {"text": "Not far — the look proves nothing, and dissolving rules "
                     "out only an impurity that does not dissolve",
             "correct": True},
            {"text": "Half way — the dissolving settles it, and the look adds "
                     "nothing to it", "correct": False,
             "why": "Dissolving completely rules out sand mixed into salt and "
                    "very little else. Most things mixed into a powder "
                    "dissolve just as the powder does."},
            {"text": "Nowhere — a powder that dissolves completely cannot be "
                     "tested for purity", "correct": False,
             "why": "It can. A melting point works on a soluble solid "
                    "perfectly well, and it is the measurement neither of "
                    "these two tests is."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h02",
        "band": "harder",
        "text": "The pure substance melts at 53 °C. Four samples were each "
                "melted three times, slowly. Which set of runs is the impure "
                "one?",
        "options": [
            {"text": "52.0–53.0 °C, 52.5–53.5 °C and 53.0–53.5 °C",
             "correct": False,
             "why": "Every run melts within a degree and finishes at the "
                    "expected 53 °C. Sharp, every time, is the signature of a "
                    "pure sample."},
            {"text": "52.0–53.0 °C, 47.5–52.0 °C and 52.5–53.5 °C",
             "correct": False,
             "why": "Two runs melt within a degree at the expected value and "
                    "one does not. That is one anomalous run, not a sample "
                    "that melts over a range."},
            {"text": "52.5–53.0 °C, 52.5–53.5 °C and 52.5–53.0 °C",
             "correct": False,
             "why": "Three runs, all within a degree, all finishing at the "
                    "expected value. There is nothing here for an impurity to "
                    "explain."},
            {"text": "45.0–52.0 °C, 44.0–51.0 °C and 46.0–52.5 °C",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h03",
        "band": "harder",
        "text": "A shop compares a suspect bag of sugar with a sample it "
                "knows is pure, using the same apparatus and the same heating "
                "rate for both. Which result would show that the suspect bag "
                "has been bulked out?",
        "options": [
            {"text": "The suspect sample melts over a wider range, starting "
                     "lower than the pure sample", "correct": True},
            {"text": "The suspect sample melts over a wider range, starting "
                     "higher than the pure sample", "correct": False,
             "why": "Something mixed in lowers the temperature at which "
                    "melting starts. A start that is higher points at a "
                    "different substance, not at a bulked-out one."},
            {"text": "The suspect sample melts sharply, half a degree above "
                     "the pure sample", "correct": False,
             "why": "A sharp melt is the signature of purity, and half a "
                    "degree is inside what two runs of the same pure "
                    "substance differ by anyway."},
            {"text": "The suspect sample weighs less per spoonful than the "
                     "pure sample", "correct": False,
             "why": "How much a spoonful weighs depends on how tightly it is "
                    "packed as much as on what is in it, and it says nothing "
                    "about what has been added."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h04",
        "band": "harder",
        "text": "Three runs on one sample, all heated fast, agree with each "
                "other to within half a degree. A student says the agreement "
                "proves the readings are right. What is wrong with that?",
        "options": [
            {"text": "Nothing — three readings that agree are as good as "
                     "evidence gets", "correct": False,
             "why": "Agreement shows the runs were consistent, not that they "
                    "were right. Three runs done the same wrong way agree "
                    "with each other perfectly."},
            {"text": "Three runs are not enough to conclude anything; ten "
                     "would be needed", "correct": False,
             "why": "Three repeats is a reasonable number. The trouble is not "
                    "how many runs there were, but that every one of them was "
                    "heated too fast."},
            {"text": "They agree because the same error happened three times",
             "correct": True},
            {"text": "The three readings should have been averaged before "
                     "concluding anything", "correct": False,
             "why": "Averaging three readings that already agree changes "
                    "almost nothing. They agree, and they are all pushed the "
                    "same way by the fast heating."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-07-e05",
        "band": "easier",
        "text": "What is an anomalous result?",
        "options": [
            {"text": "A reading that disagrees with the others taken the same "
                     "way",
             "correct": True},
            {"text": "A reading that does not match the value the "
                     "investigation was expected to produce, so it has to be "
                     "left out of the conclusion",
             "correct": False,
             "why": "Disagreeing with what you expected is not the test — "
                    "and a real result is never quietly left out"},
            {"text": "A reading taken by a different person",
             "correct": False,
             "why": "Who took it does not make it anomalous. Whether it fits "
                    "the others does"},
            {"text": "A reading you decide to delete",
             "correct": False,
             "why": "It is reported and set aside with a reason. Deleting it "
                    "is the one thing you must not do"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e06",
        "band": "easier",
        "text": "What is an expected value?",
        "options": [
            {"text": "The average of all the readings you have taken so far "
                     "in this investigation, worked out before the last run is "
                     "done",
             "correct": False,
             "why": "That is your own mean. The expected value comes from "
                    "outside your experiment"},
            {"text": "The result you already know a pure sample should give",
             "correct": True},
            {"text": "The result you are hoping for",
             "correct": False,
             "why": "Hoping has no place in it. It is a known figure for a "
                    "known substance"},
            {"text": "The middle of the range a substance melts over",
             "correct": False,
             "why": "A pure substance barely has a range. The expected value "
                    "is its sharp melting point"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e07",
        "band": "easier",
        "text": "Salt spread on an icy road makes the ice melt at a "
                "temperature where pure water would stay solid. Which idea "
                "from this lesson is that?",
        "options": [
            {"text": "Salt gives out heat as it dissolves, and that heat is "
                     "what melts the ice around each grain of it",
             "correct": False,
             "why": "Dissolving salt actually cools the water slightly. The "
                    "melting point is what has moved"},
            {"text": "A mixture melts higher than the pure substance",
             "correct": False,
             "why": "The wrong way round — and if it were true, salt would "
                    "make an icy road worse"},
            {"text": "A mixture melts lower than the pure substance",
             "correct": True},
            {"text": "Salt is insoluble in ice",
             "correct": False,
             "why": "Salt dissolves readily in the thin film of water on the "
                    "ice, which is how it works at all"},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c3-07-s05",
        "band": "standard",
        "text": "A pharmacist rejects a batch of aspirin because its melting "
                "range is wider than a degree. What has that measurement "
                "shown?",
        "options": [
            {"text": "That something else is present, but not what",
             "correct": True},
            {"text": "That the batch has been contaminated with a named "
                     "substance that the melting range has identified for "
                     "them",
             "correct": False,
             "why": "A melting range never names anything. Identifying the "
                    "impurity is a separate job"},
            {"text": "That the aspirin has gone off with age",
             "correct": False,
             "why": "It might have, and the measurement cannot say so. All it "
                    "shows is that the sample is not one substance"},
            {"text": "That the apparatus was heated too fast",
             "correct": False,
             "why": "Heating fast drags the readings up. It does not widen a "
                    "pure sample's range into several degrees"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s06",
        "band": "standard",
        "text": "Which of these is evidence that a white powder is pure?",
        "options": [
            {"text": "It weighs exactly what the label says it should, "
                     "checked three times over on a balance that has been "
                     "properly zeroed",
             "correct": False,
             "why": "Mass tells you how much you have, never what it is. Two "
                    "powders together weigh the same as one"},
            {"text": "It melts within a degree at the expected value, on "
                     "repeated slow runs",
             "correct": True},
            {"text": "It looks the same all the way through under a hand "
                     "lens",
             "correct": False,
             "why": "Two white powders ground together look like one white "
                    "powder. This is the evidence that fails every time"},
            {"text": "It dissolves completely in water, leaving nothing "
                     "behind",
             "correct": False,
             "why": "That rules out an impurity that does not dissolve, and "
                    "nothing else. A soluble impurity would pass it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s07",
        "band": "standard",
        "text": "A shop compares a suspect bag of sugar with a sample it "
                "knows is pure. What must be kept the same for the comparison "
                "to be worth anything?",
        "options": [
            {"text": "The mass of powder put into each tube, weighed out to "
                     "the same figure on the same balance before either of "
                     "them is heated",
             "correct": False,
             "why": "A melting point does not depend on how much you have. It "
                    "is the heating rate that has to match"},
            {"text": "The person watching the tube",
             "correct": False,
             "why": "Helpful for consistency and not the thing that would "
                    "wreck the comparison. Heating rate is"},
            {"text": "The apparatus and the heating rate",
             "correct": True},
            {"text": "The room temperature both samples were stored at",
             "correct": False,
             "why": "Storage temperature does not change a melting point. The "
                    "rate of heating during the run does"},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c3-07-h05",
        "band": "harder",
        "text": "Why does an impurity make a solid start melting LOWER and "
                "over a range, rather than simply melting at a different sharp "
                "temperature?",
        "options": [
            {"text": "Because the impurity gets in the way of the regular "
                     "arrangement, so less energy is needed and different "
                     "regions give way at different temperatures",
             "correct": True},
            {"text": "Because the impurity melts first at its own melting "
                     "point, and the rest follows once it has all turned to "
                     "liquid",
             "correct": False,
             "why": "The impurity's own melting point is often far higher. "
                    "What matters is that the arrangement is interrupted"},
            {"text": "Because a mixture holds more heat than a pure substance "
                     "does",
             "correct": False,
             "why": "Nothing here is about how much heat is stored. It is "
                    "about how neatly the particles fit together"},
            {"text": "Because the thermometer cannot keep up with a mixture",
             "correct": False,
             "why": "The thermometer behaves the same for both. The range is "
                    "real, and it is a property of the sample"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h06",
        "band": "harder",
        "text": "A gritter salting a road and a pharmacist rejecting a batch "
                "are using the same physics. How do the two uses differ?",
        "options": [
            {"text": "The gritter is making a mixture and the pharmacist is "
                     "making a pure substance, so one of them is doing "
                     "chemistry and the other is not",
             "correct": False,
             "why": "Both are doing chemistry, and neither is MAKING "
                    "anything. What differs is whether the effect is wanted"},
            {"text": "The gritter is making a mixture and the pharmacist a "
                     "pure substance",
             "correct": True},
            {"text": "The gritter is raising a melting point and the "
                     "pharmacist is lowering one",
             "correct": False,
             "why": "Both are about a melting point being lowered. Salt on "
                    "ice does not raise anything"},
            {"text": "They are not the same physics at all — one is about "
                     "melting and the other about purity",
             "correct": False,
             "why": "Purity is measured BY melting behaviour. That is what "
                    "makes them the same physics"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h07",
        "band": "harder",
        "text": "One of three runs on a batch disagrees with the other two. A "
                "student averages all three and reports the mean. What is "
                "wrong with that?",
        "options": [
            {"text": "Nothing — averaging is what you do with repeats, and "
                     "taking the mean of three readings is more reliable than "
                     "trusting any one of them",
             "correct": False,
             "why": "Averaging is right for repeats that agree. A reading you "
                    "have reason to distrust must not be folded in"},
            {"text": "Three runs is too few to average at all",
             "correct": False,
             "why": "Three is a reasonable number of repeats. The problem is "
                    "which three, not how many"},
            {"text": "It drags the answer towards a reading they already have "
                     "reason to distrust, and hides the anomaly",
             "correct": True},
            {"text": "The odd run should be deleted from the table before "
                     "averaging the rest",
             "correct": False,
             "why": "It is set aside with a reason written down, never "
                    "deleted. Deleting it hides the same thing averaging "
                    "does"},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-07-e08",
        "band": "easier",
        "text": "What is the melting point of a substance?",
        "options": [
            {"text": "The amount of heat a solid needs to take in before it "
                     "will melt",
             "correct": False,
             "why": "A melting point is a temperature, not a quantity of "
                    "energy. It is read off a thermometer"},
            {"text": "The temperature at which a liquid turns to gas",
             "correct": False,
             "why": "That is the boiling point. Melting is solid to liquid"},
            {"text": "The temperature at which a solid turns to liquid",
             "correct": True},
            {"text": "The time a solid takes to melt on a heated block",
             "correct": False,
             "why": "A time depends on how fast you heat the block. The "
                    "melting point does not"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e09",
        "band": "easier",
        "text": "What is a melting range?",
        "options": [
            {"text": "The spread between the lowest and the highest "
                     "temperature the block reached",
             "correct": False,
             "why": "What the block does is not the measurement. The range "
                    "belongs to the sample"},
            {"text": "The spread between the temperature melting starts at "
                     "and the temperature it finishes at",
             "correct": True},
            {"text": "How finely the thermometer can be read on its scale",
             "correct": False,
             "why": "That is the same whatever you put in the tube, so it "
                    "cannot say anything about the sample"},
            {"text": "The difference between the melting point and the "
                     "boiling point",
             "correct": False,
             "why": "Those are two separate properties. A range is measured "
                    "inside one melt"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e10",
        "band": "easier",
        "text": "A pure substance is melted slowly. How wide is its melting "
                "range?",
        "options": [
            {"text": "Within about a degree",
             "correct": True},
            {"text": "Five to ten degrees",
             "correct": False,
             "why": "That is what a mixture does. A pure solid gives way all "
                    "at once"},
            {"text": "About the same as a mixture's range, but at a higher "
                     "temperature",
             "correct": False,
             "why": "A mixture's range is several degrees wide and a pure "
                    "substance's is not, so they are not the same width"},
            {"text": "Wider the more of it you put in the tube",
             "correct": False,
             "why": "How much you put in the tube does not change the "
                    "temperature the sample melts at"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e11",
        "band": "easier",
        "text": "Something else is mixed into a pure solid. What happens to "
                "the temperature at which it starts to melt?",
        "options": [
            {"text": "It rises above the pure substance's melting point",
             "correct": False,
             "why": "The wrong way round. An impurity lowers the temperature "
                    "melting begins at"},
            {"text": "It stays where it was, and the finish moves instead",
             "correct": False,
             "why": "The start moves too, and it is the start that drops "
                    "furthest below the pure value"},
            {"text": "It becomes impossible to measure with an ordinary "
                     "thermometer",
             "correct": False,
             "why": "A mixture's melt is measured with the same thermometer "
                    "and the same block as a pure one"},
            {"text": "It falls below the pure substance's melting point",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e12",
        "band": "easier",
        "text": "Where does the expected value for a melting point come from?",
        "options": [
            {"text": "The average of the three runs you have just done on "
                     "the sample being tested",
             "correct": False,
             "why": "That is your own result. It cannot be the thing your own "
                    "result is judged against"},
            {"text": "The temperature the block was set to before the sample "
                     "went into it",
             "correct": False,
             "why": "That is a setting on the apparatus, not a property of "
                    "the substance"},
            {"text": "A known figure for that substance, from a data book or "
                     "a sample already known to be pure",
             "correct": True},
            {"text": "Whatever the label on the bag says",
             "correct": False,
             "why": "The label is the claim being tested, so it cannot also "
                    "be the standard"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e13",
        "band": "easier",
        "text": "A melting range shows that a sample is impure. What does the "
                "measurement not tell you?",
        "options": [
            {"text": "Whether the sample finished melting",
             "correct": False,
             "why": "You watched it melt, and that is where the two readings "
                    "came from"},
            {"text": "What the impurity is",
             "correct": True},
            {"text": "How wide the range was",
             "correct": False,
             "why": "The range is the measurement itself — the start "
                    "subtracted from the finish"},
            {"text": "Whether the runs agreed with each other",
             "correct": False,
             "why": "A table of repeats shows that directly"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e14",
        "band": "easier",
        "text": "Why is each sample melted more than once?",
        "options": [
            {"text": "So that a reading has another reading to be checked "
                     "against",
             "correct": True},
            {"text": "So that the sample has time to warm up properly",
             "correct": False,
             "why": "Warming up is what the slow heating rate is for, and it "
                    "happens inside a single run"},
            {"text": "So that a different person can take a turn at reading "
                     "the thermometer",
             "correct": False,
             "why": "Sharing the job out is not why repeats are done, and one "
                    "person doing all three is fine"},
            {"text": "So that the sample is used up before it goes off",
             "correct": False,
             "why": "Using up the sample is not a reason to measure anything "
                    "twice"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e15",
        "band": "easier",
        "text": "How fast should the heated block be taken up in temperature?",
        "options": [
            {"text": "As fast as the block will go",
             "correct": False,
             "why": "Fast heating leaves the thermometer trailing the sample, "
                    "so every reading is wrong"},
            {"text": "Slowly — about one degree a minute",
             "correct": True},
            {"text": "In one jump, straight to the expected value",
             "correct": False,
             "why": "You would never see the temperature melting started at, "
                    "which is half the measurement"},
            {"text": "Fast, and then left to cool slowly afterwards",
             "correct": False,
             "why": "The reading is taken on the way up. What happens while "
                    "it cools is too late to help"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e16",
        "band": "easier",
        "text": "Why does the thermometer disagree with the sample when a "
                "block is heated quickly?",
        "options": [
            {"text": "The thermometer is accurate at low temperatures but "
                     "not at high ones",
             "correct": False,
             "why": "A laboratory thermometer reads correctly across its "
                    "whole scale when it has had time to settle"},
            {"text": "A quickly heated sample melts at a higher temperature "
                     "than it really has",
             "correct": False,
             "why": "The temperature the sample melts at does not change. "
                    "What changes is what the thermometer shows"},
            {"text": "The thermometer lags behind, so it has not reached the "
                     "sample's temperature",
             "correct": True},
            {"text": "The glass of the thermometer expands in the heat and "
                     "shifts its whole scale",
             "correct": False,
             "why": "The scale is fixed to the glass and moves with it, which "
                    "is why a thermometer can be read hot or cold"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e17",
        "band": "easier",
        "text": "What two temperatures are recorded in a melting point run?",
        "options": [
            {"text": "The temperature of the block and the temperature of "
                     "the air",
             "correct": False,
             "why": "Neither of those is about the sample, and the sample is "
                    "what is being tested"},
            {"text": "The temperature before heating and after cooling",
             "correct": False,
             "why": "Both of those are taken with the sample solid. Nothing "
                    "about the melt itself is recorded"},
            {"text": "The expected temperature and the one reached",
             "correct": False,
             "why": "The expected value is known before you start. It is not "
                    "a reading you take"},
            {"text": "The temperature melting starts at and the temperature "
                     "it finishes at",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e18",
        "band": "easier",
        "text": "Melting started at 51.5 °C and finished at 53.0 °C. What was "
                "the melting range?",
        "options": [
            {"text": "1.5 °C",
             "correct": True},
            {"text": "51.5 °C",
             "correct": False,
             "why": "That is where melting started, not the spread between "
                    "start and finish"},
            {"text": "53.0 °C",
             "correct": False,
             "why": "That is where melting finished, not the spread between "
                    "start and finish"},
            {"text": "104.5 °C",
             "correct": False,
             "why": "The two readings are subtracted, not added"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e19",
        "band": "easier",
        "text": "A single pure substance is run on chromatography paper. How "
                "many spots does it give?",
        "options": [
            {"text": "One spot for each solvent it will dissolve in",
             "correct": False,
             "why": "A run uses one solvent, and how many others would "
                    "dissolve it has nothing to do with the spots"},
            {"text": "One",
             "correct": True},
            {"text": "Two",
             "correct": False,
             "why": "Two spots means two substances travelling different "
                    "distances, which is a mixture"},
            {"text": "Three",
             "correct": False,
             "why": "Three spots means at least three substances, which is a "
                    "mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e20",
        "band": "easier",
        "text": "A chromatogram of an ink shows three separate spots. What "
                "does that show?",
        "options": [
            {"text": "The ink was run in the wrong solvent",
             "correct": False,
             "why": "A solvent that separates three substances has worked, "
                    "not failed"},
            {"text": "The paper was not tall enough for the run",
             "correct": False,
             "why": "Three spots on the paper is a finished separation, not a "
                    "run that ran out of room"},
            {"text": "The ink is a mixture of at least three substances",
             "correct": True},
            {"text": "The ink is pure, and the three spots are one dye that "
                     "has been seen three times over",
             "correct": False,
             "why": "One substance travels one distance and stops in one "
                    "place. It cannot appear three times"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e21",
        "band": "easier",
        "text": "A liquid is heated until it boils. What does a pure liquid "
                "do that a mixture does not?",
        "options": [
            {"text": "It boils without any bubbles forming inside it",
             "correct": False,
             "why": "Bubbles form inside any boiling liquid. That is what "
                    "boiling is"},
            {"text": "It boils at a temperature that climbs as the liquid "
                     "boils away",
             "correct": False,
             "why": "A climbing temperature is what a mixture does, which is "
                    "the wrong way round"},
            {"text": "It begins to boil the moment it is put on the heat",
             "correct": False,
             "why": "Every liquid has to reach its boiling temperature first, "
                    "pure or not"},
            {"text": "It boils at one fixed temperature that never climbs as "
                     "it boils",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e22",
        "band": "easier",
        "text": "A bag of powder is labelled pure. Is the label evidence that "
                "it is?",
        "options": [
            {"text": "No — a label is a claim, and only a measurement can "
                     "settle it",
             "correct": True},
            {"text": "Yes, because a supplier has to be able to back a label "
                     "up in court",
             "correct": False,
             "why": "Whether the supplier could back it up is exactly what "
                    "the test is for. The label is not the test"},
            {"text": "Yes, unless the bag has been opened since the supplier "
                     "filled it",
             "correct": False,
             "why": "An unopened bag can have been filled from the wrong "
                    "batch, and the seal says nothing about what is inside"},
            {"text": "No, but weighing the bag would settle it",
             "correct": False,
             "why": "Mass says how much there is. It cannot say what it is"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e23",
        "band": "easier",
        "text": "An odd reading is written into the table rather than rubbed "
                "out. Why?",
        "options": [
            {"text": "So that it can be added into the average with the rest",
             "correct": False,
             "why": "Averaging it in is the other way of hiding it. It is "
                    "kept in the table and left out of the conclusion"},
            {"text": "So that anyone checking the work can see every reading "
                     "that was taken",
             "correct": True},
            {"text": "So that the table has as many rows as the others",
             "correct": False,
             "why": "How the table looks is not a reason to keep a reading. "
                    "Being able to check it is"},
            {"text": "So that the odd reading can be used as the answer",
             "correct": False,
             "why": "It is the one reading there is already reason to "
                    "distrust, so it is the last one to build on"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e24",
        "band": "easier",
        "text": "What is written down beside an anomalous reading when it is "
                "set aside?",
        "options": [
            {"text": "The word 'ignore'",
             "correct": False,
             "why": "That says what was done and not why, so nobody checking "
                    "the work can judge it"},
            {"text": "The average of the other runs",
             "correct": False,
             "why": "The other runs already stand on their own. The odd one "
                    "needs an explanation, not a substitute"},
            {"text": "A likely cause for it",
             "correct": True},
            {"text": "A note to say that the table of results is finished",
             "correct": False,
             "why": "Finishing the table is not an explanation of anything in "
                    "it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e25",
        "band": "easier",
        "text": "A student suggests tasting a little of an unknown white "
                "powder. What is the rule?",
        "options": [
            {"text": "Taste it only if a teacher is watching",
             "correct": False,
             "why": "A teacher watching does not make an unknown powder safe "
                    "to put in your mouth"},
            {"text": "Taste it only after it has been heated",
             "correct": False,
             "why": "Heating does not make an unknown substance safe, and it "
                    "can make it more dangerous"},
            {"text": "Taste it, then rinse your mouth out",
             "correct": False,
             "why": "Rinsing afterwards is far too late. The powder is "
                    "already in your mouth"},
            {"text": "You never taste anything in a laboratory",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e26",
        "band": "easier",
        "text": "Stirring a powder into water and checking it all dissolves "
                "catches one kind of impurity. Which kind?",
        "options": [
            {"text": "One that does not dissolve",
             "correct": True},
            {"text": "One that dissolves quickly",
             "correct": False,
             "why": "Anything that dissolves disappears into the water along "
                    "with the powder, fast or slow"},
            {"text": "One that warms the water as it dissolves",
             "correct": False,
             "why": "A warming is not what the check looks for, and an "
                    "impurity that warms the water has still dissolved"},
            {"text": "One that is present in a very small amount of the powder",
             "correct": False,
             "why": "How much there is does not decide it. Whether it "
                    "dissolves does"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e27",
        "band": "easier",
        "text": "Pure water freezes at 0 °C. What happens to that temperature "
                "when salt is dissolved in the water?",
        "options": [
            {"text": "It rises, so the salt water freezes at a temperature "
                     "above 0 °C",
             "correct": False,
             "why": "The wrong way round, and if it were true salt would make "
                    "an icy road worse"},
            {"text": "It falls, so the salt water stays liquid below 0 °C",
             "correct": True},
            {"text": "It stays at 0 °C, because dissolved salt cannot change "
                     "it",
             "correct": False,
             "why": "Dissolving anything in water moves the temperature it "
                    "freezes at, which is the whole reason roads are salted"},
            {"text": "It disappears, because a solution of salt in water "
                     "cannot freeze",
             "correct": False,
             "why": "Salt water freezes perfectly well. The sea freezes every "
                    "winter at the poles"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e28",
        "band": "easier",
        "text": "Why does a company making medicines measure the melting "
                "point of every batch?",
        "options": [
            {"text": "To find out how much of the medicine there is in every "
                     "batch that is made",
             "correct": False,
             "why": "How much there is comes off a balance, and a melting "
                    "point does not depend on how much you have"},
            {"text": "To work out how long each batch of the medicine will "
                     "take to dissolve",
             "correct": False,
             "why": "Dissolving time is a different measurement, and it is "
                    "not what a melting point tells you"},
            {"text": "To check that each batch is the pure substance before "
                     "it is sold",
             "correct": True},
            {"text": "To set the temperature that the batch of medicine is "
                     "stored at",
             "correct": False,
             "why": "Storage temperature is chosen for keeping the medicine "
                    "safe, not read off a melt"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e29",
        "band": "easier",
        "text": "A sample melts over five degrees. What does that tell you "
                "about what is in it?",
        "options": [
            {"text": "Only that it was heated too quickly",
             "correct": False,
             "why": "Heating fast narrows a wide melt rather than widening a "
                    "sharp one, so it cannot have made five degrees"},
            {"text": "It is one substance, and five degrees is normal for a "
                     "pure solid",
             "correct": False,
             "why": "A pure solid melts within about a degree. Five is "
                    "several times that"},
            {"text": "Nothing, because a range is a property of a liquid",
             "correct": False,
             "why": "The range is measured while the solid turns to liquid, "
                    "which is the melt itself"},
            {"text": "More than one substance is present",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e30",
        "band": "easier",
        "text": "Two slow runs on the same pure sample give 52.8 °C and "
                "53.1 °C. Does that disagreement matter?",
        "options": [
            {"text": "No — two runs of the same sample differ by a little "
                     "anyway",
             "correct": True},
            {"text": "Yes, a pure substance must give exactly the same figure "
                     "every single time",
             "correct": False,
             "why": "No measurement repeats to the last decimal place. Three "
                    "tenths of a degree is the apparatus, not the sample"},
            {"text": "Yes, one of the two readings must have been misread",
             "correct": False,
             "why": "Both readings can be taken correctly and still differ by "
                    "a fraction of a degree"},
            {"text": "No, because the first reading of a pair is the one that "
                     "counts",
             "correct": False,
             "why": "Neither reading outranks the other. They are two runs of "
                    "the same measurement"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c3-07-s08",
        "band": "standard",
        "text": "A sample that melts within half a degree on a slow block "
                "reads as nearly two degrees when the block is driven fast. "
                "Explain why a fast run widens a sharp melt.",
        "options": [
            {"text": "The thermometer trails the sample, so the two readings "
                     "are taken further apart than the melt really was",
             "correct": True},
            {"text": "Fast heating breaks the sample into smaller pieces, and "
                     "small pieces melt over a wider spread of temperatures",
             "correct": False,
             "why": "Nothing breaks the sample up, and piece size is not what "
                    "sets the temperature a solid melts at"},
            {"text": "Fast heating drives some of the sample off as a gas "
                     "before it melts, which leaves an impurity behind",
             "correct": False,
             "why": "A solid heated to its melting point melts. Nothing has "
                    "been added to the tube and nothing has left it"},
            {"text": "The sample really does melt over a wider range when it "
                     "is heated quickly rather than slowly",
             "correct": False,
             "why": "The sample's melting behaviour is a property of what it "
                    "is made of. The heating rate changes the reading, not "
                    "the sample"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s09",
        "band": "standard",
        "text": "A white powder is run on chromatography paper and gives one "
                "spot. A student writes that the powder is proved pure. How "
                "safe is that?",
        "options": [
            {"text": "Safe, because one spot is what a pure substance gives "
                     "and nothing else gives it",
             "correct": False,
             "why": "One spot is what a pure substance gives, and it is not "
                    "the only thing that gives it"},
            {"text": "Not safe — two substances carried the same distance "
                     "would arrive as one spot",
             "correct": True},
            {"text": "Not safe, because chromatography paper cannot separate "
                     "a powder at all",
             "correct": False,
             "why": "A dissolved powder separates on paper exactly as an ink "
                    "does, which is why the run was worth doing"},
            {"text": "Safe, as long as the run was done in water rather than "
                     "in any other solvent",
             "correct": False,
             "why": "Water is one solvent among several, and the choice of "
                    "solvent does not turn one spot into proof"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s10",
        "band": "standard",
        "text": "A batch has turned out to be impure. Why can "
                "chromatography get further with it than a melting point "
                "can?",
        "options": [
            {"text": "Because it separates a sample into a spot for each "
                     "substance and destroys the impurity as it goes",
             "correct": False,
             "why": "Nothing is destroyed. Every substance in the sample ends "
                    "up somewhere on the paper"},
            {"text": "Because it measures the impurity's own melting point "
                     "once the spots have been cut out and dried",
             "correct": False,
             "why": "No melting point is taken during a chromatography run. "
                    "The evidence is how far each substance travelled"},
            {"text": "Each substance travels its own distance, which can be "
                     "compared with known substances run beside it",
             "correct": True},
            {"text": "Because it works on a much smaller sample than a "
                     "melting point apparatus needs to be given",
             "correct": False,
             "why": "Sample size is not the difference. A melting point on a "
                    "smaller sample would still say only that something is "
                    "there"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s11",
        "band": "standard",
        "text": "Pure water boils steadily at 100 °C. Sea water boils at a "
                "temperature that climbs while it is boiling. What does the "
                "difference show?",
        "options": [
            {"text": "That sea water holds more energy than pure water does "
                     "at the same temperature",
             "correct": False,
             "why": "How much energy it holds is a different question. The "
                    "climbing temperature is about what is dissolved in it"},
            {"text": "That the thermometer reads sea water differently "
                     "because of the salt around the bulb",
             "correct": False,
             "why": "A thermometer reads the temperature it is in, whatever "
                    "is dissolved around the bulb"},
            {"text": "That sea water is a mixture and pure water is not",
             "correct": True},
            {"text": "That sea water was heated more quickly",
             "correct": False,
             "why": "Heating rate changes how long boiling takes to reach, "
                    "not whether the temperature holds once it is boiling"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s12",
        "band": "standard",
        "text": "A chemist melts an unknown white powder three times, slowly, "
                "and gets 118.0–118.4 °C every time. She writes that it is the "
                "substance she ordered. What is wrong with that?",
        "options": [
            {"text": "She has no expected value for the substance she "
                     "ordered, so there is nothing to compare 118 °C with",
             "correct": True},
            {"text": "Three runs is not enough to be sure of a melting point, "
                     "so the reading cannot be used for anything yet",
             "correct": False,
             "why": "Three slow runs agreeing to a few tenths is good "
                    "evidence about the reading. The trouble is what it is "
                    "being compared against"},
            {"text": "A melting range of 0.4 °C is too wide for the sample to "
                     "have been a single pure substance",
             "correct": False,
             "why": "Four tenths of a degree is a sharp melt, which is what a "
                    "pure substance gives"},
            {"text": "A melting point should be measured on a fast block "
                     "first and a slow one afterwards",
             "correct": False,
             "why": "A fast block gives readings that trail the sample. There "
                    "is no reason to take one"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s13",
        "band": "standard",
        "text": "Two suppliers send the same substance. On three slow runs "
                "each, A melts from 78.0 °C to 78.5 °C and B melts from "
                "71.5 °C to 78.0 °C. Which is the pure one?",
        "options": [
            {"text": "B, because its melt covers the wider spread of "
                     "temperatures and so contains more of the substance",
             "correct": False,
             "why": "A wide spread is the signature of a mixture, and how "
                    "much substance there is has nothing to do with it"},
            {"text": "A, because it melts within half a degree while B melts "
                     "over six and a half",
             "correct": True},
            {"text": "Neither, because both of them finish at the same "
                     "temperature",
             "correct": False,
             "why": "Where a melt finishes is not the test on its own. The "
                    "spread between start and finish is"},
            {"text": "B, because it starts melting first and so needs less "
                     "energy to break its arrangement apart",
             "correct": False,
             "why": "Starting early is one of the two signs of a mixture, so "
                    "it points at B being the impure one"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s14",
        "band": "standard",
        "text": "One run on a batch goes from 44.0 °C to 51.0 °C and another "
                "goes from 45.0 °C to 52.0 °C. Do the two runs agree with each "
                "other?",
        "options": [
            {"text": "No, because two runs agree only when every reading in "
                     "them is identical",
             "correct": False,
             "why": "No two runs of anything repeat to the last figure. What "
                    "has to agree is what the runs say about the sample"},
            {"text": "No, because the second run finished a whole degree "
                     "higher up than the first one did",
             "correct": False,
             "why": "Both figures shifted by the same degree, so the "
                    "measurement they carry is unchanged"},
            {"text": "Yes — both give a range of 7.0 °C, starting within a "
                     "degree of each other",
             "correct": True},
            {"text": "Yes, because both of them finished below the pure "
                     "value",
             "correct": False,
             "why": "Finishing low is not what makes two runs agree. Their "
                    "ranges agreeing is"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s15",
        "band": "standard",
        "text": "Two runs on a batch melt within a degree at the expected "
                "value and the third melts several degrees lower and wider. "
                "What is the most likely cause of the third?",
        "options": [
            {"text": "The batch is a mixture, which is why one of its three "
                     "runs came out wide",
             "correct": False,
             "why": "A mixture melts wide every time it is run, not once in "
                    "three"},
            {"text": "The block was taken up in temperature more slowly than "
                     "it was for the other two runs",
             "correct": False,
             "why": "Slow heating is the setting that gives the truest "
                    "reading. It cannot drag a start down several degrees"},
            {"text": "The thermometer was reading in the wrong units for that "
                     "one run and the right units for the rest",
             "correct": False,
             "why": "A thermometer does not change units between runs, and a "
                    "change of units would not shift one reading by a few "
                    "degrees"},
            {"text": "The tube was packed loosely, so it did not sit properly "
                     "against the block",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s16",
        "band": "standard",
        "text": "A run has been judged anomalous and left out of the "
                "conclusion. Why does it stay in the results table?",
        "options": [
            {"text": "So that a reader can see it was taken and judge for "
                     "themselves whether leaving it out was fair",
             "correct": True},
            {"text": "So that it can be brought back into the average once "
                     "the rest of the runs have been finished",
             "correct": False,
             "why": "It is left out of the conclusion for a reason, and that "
                    "reason does not expire when the table does"},
            {"text": "So that the batch can be reported as impure on the "
                     "strength of the one wide reading",
             "correct": False,
             "why": "One wide run among sharp ones is an anomaly. A mixture "
                    "melts wide every time"},
            {"text": "So that the same tube is not used again by anybody else "
                     "working on that batch",
             "correct": False,
             "why": "Which tube gets used again is not what a results table "
                    "is for"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s17",
        "band": "standard",
        "text": "Three slow runs agree to within 0.2 °C. The thermometer has "
                "never been checked and in fact reads 3 °C high. What is wrong "
                "with trusting the value the three runs give?",
        "options": [
            {"text": "Nothing is wrong, because three readings agreeing to a "
                     "fifth of a degree is as good as evidence ever gets",
             "correct": False,
             "why": "Agreement shows the runs were consistent. It cannot show "
                    "that a thermometer reading 3 °C high was right"},
            {"text": "All three are pushed the same way by the same "
                     "thermometer, so their agreement proves nothing about "
                     "the value",
             "correct": True},
            {"text": "Three runs that agree that closely must have been "
                     "copied from one another rather than measured",
             "correct": False,
             "why": "Careful repeats on a pure sample agree that closely, and "
                    "accusing the chemist explains nothing about the "
                    "thermometer"},
            {"text": "The 0.2 °C spread is far too wide to be a sharp melt, "
                     "so the sample must be a mixture",
             "correct": False,
             "why": "Two tenths of a degree is sharper than most school "
                    "apparatus can resolve, and nothing about it says mixture"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s18",
        "band": "standard",
        "text": "A shop melts its known pure sugar on Monday with the block "
                "taken up slowly, and the suspect bag on Friday with the block "
                "driven fast. Why can the two results not be compared?",
        "options": [
            {"text": "Because four days is long enough for the sugar in the "
                     "known sample to change what it is made of",
             "correct": False,
             "why": "Dry sugar in a jar is the same substance on Friday as it "
                    "was on Monday"},
            {"text": "Because a melting point apparatus has to be used on the "
                     "same day of the week for every sample",
             "correct": False,
             "why": "Which day it is does not reach the measurement. The "
                    "heating rate does"},
            {"text": "The fast run shifts and squashes the suspect bag's "
                     "readings, so a difference could be the heating rate "
                     "rather than the sugar",
             "correct": True},
            {"text": "Because the suspect bag should have been measured "
                     "before the known pure sample rather than after it",
             "correct": False,
             "why": "The order does not spoil a comparison. Changing the "
                    "heating rate between them does"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s19",
        "band": "standard",
        "text": "A shop wants to test a suspect bag of sugar against a "
                "sample it knows is pure. What does it need from the known "
                "pure sample?",
        "options": [
            {"text": "Its mass, so that the same mass can be weighed into "
                     "each of the two tubes",
             "correct": False,
             "why": "A melting point does not depend on how much is in the "
                    "tube, so matching the masses settles nothing"},
            {"text": "The date it was bought, so that the two samples can be "
                     "shown to be the same age",
             "correct": False,
             "why": "Dry sugar does not change with age, and the ages of the "
                    "two samples are not what is being compared"},
            {"text": "The temperature it has been stored at, so that both "
                     "samples are kept the same way",
             "correct": False,
             "why": "Storage temperature does not move a melting point, so "
                    "matching it proves nothing about either bag"},
            {"text": "The value its own apparatus gives for pure sugar, to "
                     "compare the bag with",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s20",
        "band": "standard",
        "text": "A pure solid and a mixture are heated side by side at the "
                "same slow rate. Describe what a student would see.",
        "options": [
            {"text": "The pure solid turns to liquid over about a degree; the "
                     "mixture starts earlier and takes several degrees",
             "correct": True},
            {"text": "The pure solid turns to liquid instantly while the "
                     "mixture never finishes melting at all",
             "correct": False,
             "why": "A mixture finishes melting perfectly well. It simply "
                    "takes a range of temperatures to do it"},
            {"text": "Both turn to liquid over about a degree, but the "
                     "mixture does it at a higher temperature",
             "correct": False,
             "why": "The mixture melts over a range and starts lower, which "
                    "is the whole of the test"},
            {"text": "Both start turning to liquid at the same temperature, "
                     "but the mixture takes longer to finish",
             "correct": False,
             "why": "The mixture starts lower as well as taking longer. A "
                    "shared starting temperature is the half that is wrong"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s21",
        "band": "standard",
        "text": "A council spreads salt on the roads before a frost. Explain "
                "how that keeps ice off the road.",
        "options": [
            {"text": "The salt reacts with the water and turns it into a new "
                     "substance that cannot freeze at any temperature",
             "correct": False,
             "why": "Salt dissolving in water is not a reaction, and salt "
                    "water freezes if it gets cold enough"},
            {"text": "Salt dissolves in the water on the road, and a mixture "
                     "stays liquid below the temperature pure water freezes at",
             "correct": True},
            {"text": "The salt gives out heat as it dissolves, and that heat "
                     "melts the ice on the road around each grain",
             "correct": False,
             "why": "Salt dissolving in water cools it slightly. It is the "
                    "freezing temperature that has moved"},
            {"text": "The salt grains rub against the ice as cars drive over "
                     "them, and the rubbing warms the road surface",
             "correct": False,
             "why": "Salt works on a road nobody has driven along yet, which "
                    "rules rubbing out"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s22",
        "band": "standard",
        "text": "Pure aspirin melts at 136 °C. On slow repeated runs batch A "
                "melts from 135.5 °C to 136.5 °C and batch B melts from "
                "129.0 °C to 135.0 °C. Which batch may be sold?",
        "options": [
            {"text": "Batch B, because it finishes melting below the "
                     "temperature pure aspirin melts at",
             "correct": False,
             "why": "Finishing low is part of what gives a mixture away, so "
                    "it counts against batch B"},
            {"text": "Both, because both of them melt somewhere near the "
                     "136 °C that was expected",
             "correct": False,
             "why": "Being near the expected value is not enough on its own. "
                    "Batch B takes six degrees to get there"},
            {"text": "Batch A, because it melts within a degree across "
                     "136 °C while batch B melts over six",
             "correct": True},
            {"text": "Neither, because a batch may be sold only if it melts at "
                     "136 °C with no range at all",
             "correct": False,
             "why": "No real melt is a single point. A degree across the "
                    "expected value is what a pure batch gives"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s23",
        "band": "standard",
        "text": "A supplier says none of its bags has failed a purity test in "
                "ten years. Why is that not evidence about the bag in front of "
                "you?",
        "options": [
            {"text": "Because ten years is not long enough for a supplier to "
                     "have built up a record worth anything",
             "correct": False,
             "why": "Ten years is a long record. The trouble is that it is "
                    "about other bags"},
            {"text": "Because a supplier is not allowed to test its own bags "
                     "and report the results itself",
             "correct": False,
             "why": "Suppliers test their own product routinely. That is not "
                    "what is wrong with the claim"},
            {"text": "Because a purity test measures mass, and mass varies "
                     "from bag to bag",
             "correct": False,
             "why": "A purity test is a melting point, not a weighing, and it "
                    "does not depend on how much is in the bag"},
            {"text": "Purity is a property of this sample, so it can only be "
                     "measured on this sample",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s24",
        "band": "standard",
        "text": "Three batches are each melted once, slowly, and one of them "
                "gives a sharp melt at the expected value. Why can that batch "
                "not yet be called pure?",
        "options": [
            {"text": "One run has nothing to be checked against, so a bad run "
                     "and a good one look exactly the same",
             "correct": True},
            {"text": "A batch cannot be called pure until all three of the "
                     "batches have been measured the same number of times",
             "correct": False,
             "why": "Each batch is judged on its own readings. What the "
                    "others did is not the missing piece"},
            {"text": "A single run is always heated too fast to be worth "
                     "reading, whatever the dial was set to",
             "correct": False,
             "why": "The run was slow. How many runs there were and how fast "
                    "they went are two separate decisions"},
            {"text": "A sharp melt at the expected value is what a mixture "
                     "gives when it is measured only once",
             "correct": False,
             "why": "A mixture melts wide and low whether you measure it once "
                    "or ten times"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s25",
        "band": "standard",
        "text": "A run started melting at 46.0 °C and finished at 52.5 °C. "
                "The pure substance melts at 53 °C. Give the range and say "
                "what it shows.",
        "options": [
            {"text": "0.5 °C, so the sample is pure and finished early",
             "correct": False,
             "why": "Half a degree is the gap to the expected value, not the "
                    "spread between the start and the finish of this melt"},
            {"text": "6.5 °C, so the sample is impure",
             "correct": True},
            {"text": "6.5 °C, so the thermometer was reading low",
             "correct": False,
             "why": "A thermometer reading low would move the start and the "
                    "finish down together and still give a sharp melt"},
            {"text": "98.5 °C, so the sample melted far too high",
             "correct": False,
             "why": "The two readings are subtracted, not added, and nothing "
                    "here melted anywhere near 98 °C"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s26",
        "band": "standard",
        "text": "Which change to the method would make an impure batch "
                "hardest to spot?",
        "options": [
            {"text": "Running each sample three times instead of running each "
                     "of them once",
             "correct": False,
             "why": "Repeats make an odd reading visible. They are the "
                    "opposite of a way to hide a batch"},
            {"text": "Using a clean tube for each of the samples instead of "
                     "reusing the first one",
             "correct": False,
             "why": "A clean tube removes a way a sample could be "
                    "contaminated, so it makes the test harder to fool"},
            {"text": "Driving the block up fast instead of at about a degree "
                     "a minute",
             "correct": True},
            {"text": "Measuring a sample known to be pure alongside the "
                     "batches",
             "correct": False,
             "why": "A known sample gives you the expected value, which is "
                    "what makes an impure batch stand out"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s27",
        "band": "standard",
        "text": "The melting point of sugar can be looked up in a data book. "
                "Why does the shop melt a sample it knows is pure as well?",
        "options": [
            {"text": "Because a data book gives the value for one sample of "
                     "sugar, and every other sample of it melts differently",
             "correct": False,
             "why": "Pure sugar is pure sugar wherever it came from. It is "
                    "the apparatus that varies"},
            {"text": "Because a value from a book counts as evidence once a "
                     "teacher has confirmed it",
             "correct": False,
             "why": "Who confirms the book is not the issue. Whether this "
                    "apparatus agrees with it is"},
            {"text": "A book value assumes their thermometer and block read "
                     "the same as the book's did",
             "correct": True},
            {"text": "Because the book value is for sugar that has been "
                     "ground up",
             "correct": False,
             "why": "Grinding changes the size of the grains, not the "
                    "temperature the sugar melts at"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s28",
        "band": "standard",
        "text": "A shop runs each of three bags once, on a fast block. The "
                "widest is about three degrees wider than the others. Can it "
                "accuse the supplier?",
        "options": [
            {"text": "No — the data points the right way, but one fast run "
                     "cannot carry an accusation",
             "correct": True},
            {"text": "Yes, because three degrees is a wide enough difference "
                     "for the measurement to stand on its own",
             "correct": False,
             "why": "A fast run has already dragged the ranges towards each "
                    "other, so the real difference is unknown"},
            {"text": "Yes, because all three bags were measured in exactly "
                     "the same way as each other",
             "correct": False,
             "why": "Measuring all three the same wrong way does not cancel "
                    "out. It shrinks the difference being measured"},
            {"text": "No, because a melting point cannot be used as evidence "
                     "against a supplier under any circumstances",
             "correct": False,
             "why": "It can, and it is: slow runs, repeated, are what the "
                    "accusation would rest on"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s29",
        "band": "standard",
        "text": "A thermometer can be read only to the nearest whole degree. "
                "Why is that a problem for deciding whether a melt is sharp?",
        "options": [
            {"text": "Because a thermometer marked in whole degrees cannot "
                     "reach the temperatures a solid melts at",
             "correct": False,
             "why": "It reaches them perfectly well. What it cannot do is "
                    "split the degree it lands in"},
            {"text": "A sharp melt is about a degree wide altogether, so a "
                     "whole-degree scale cannot resolve it",
             "correct": True},
            {"text": "Because a thermometer marked in whole degrees takes "
                     "longer to settle than one marked in tenths",
             "correct": False,
             "why": "How finely it is marked does not change how fast it "
                    "settles"},
            {"text": "Because the range has to be worked out by subtraction, "
                     "and whole degrees cannot be subtracted",
             "correct": False,
             "why": "Whole degrees subtract as easily as tenths do. The "
                    "trouble is the size of what you are trying to measure"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s30",
        "band": "standard",
        "text": "One student reports a melt as 52.0–53.0 °C. Another reports "
                "the same melt as 52.5 °C. Which report is more useful, and "
                "why?",
        "options": [
            {"text": "The single figure, because a reader wants one number to "
                     "compare with the expected value",
             "correct": False,
             "why": "One number is easier to compare and it throws away the "
                    "spread, which is the evidence about purity"},
            {"text": "The single figure, because the middle of a melt is "
                     "where most of the sample turns to liquid",
             "correct": False,
             "why": "Where most of it melts is not measured, and the middle "
                    "of the range is not a reading anybody took"},
            {"text": "The range, because the spread between start and finish "
                     "is the evidence about purity",
             "correct": True},
            {"text": "Neither, because a melt is reported by the temperature "
                     "the block reached rather than by the sample",
             "correct": False,
             "why": "The sample is what is being tested, so the sample's "
                    "readings are what get reported"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c3-07-h08",
        "band": "harder",
        "text": "A supplier's label says a liquid should boil at exactly "
                "78 °C. A technician runs it three times and gets 100.0 °C "
                "each time, with no drift up or down during any run. The "
                "technician has not opened the bottle to check the label "
                "against anything else. What is the soundest conclusion?",
        "options": [
            {"text": "The liquid is a mixture, because it boils a long way "
                     "from the labelled value",
             "correct": False,
             "why": "A mixture's boiling point drifts upward as it boils, "
                    "because the lower-boiling part leaves first. A steady "
                    "100.0 °C every time is the sharp signature of one pure "
                    "liquid, whichever one it is."},
            {"text": "The label must be wrong about which liquid is inside, "
                     "not wrong about purity",
             "correct": True},
            {"text": "The result cannot be trusted until the boiling point "
                     "is measured a fourth time",
             "correct": False,
             "why": "Three identical, sharp results already rule out a "
                    "mixture. A fourth run at the same value would confirm "
                    "the same thing, not something new."},
            {"text": "The liquid must have picked up an impurity while it "
                     "was being stored in the bottle",
             "correct": False,
             "why": "An impurity would smear the boiling point over a range "
                    "and pull it below the true value, not hold it dead "
                    "steady at a single, different temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h09",
        "band": "harder",
        "text": "A bag of sugar has been bulked out with a cheap powder that "
                "happens to melt at the same temperature as sugar does. What "
                "would a melting point test show?",
        "options": [
            {"text": "A melt over a range, starting below that temperature, "
                     "because a mixture never melts sharply",
             "correct": True},
            {"text": "A sharp melt at the usual temperature, so the test "
                     "would miss it",
             "correct": False,
             "why": "Two substances mixed together interrupt each other's "
                    "arrangement whatever temperature each melts at on its own"},
            {"text": "A sharp melt, but several degrees above the "
                     "temperature that pure sugar itself melts at",
             "correct": False,
             "why": "Nothing here pushes the melt up, and a mixture does not "
                    "give a sharp melt in the first place"},
            {"text": "Two separate melts, one for the sugar and one for the "
                     "powder that was added to it",
             "correct": False,
             "why": "A mixture melts as one sample over one range, not as two "
                    "melts one after the other"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h10",
        "band": "harder",
        "text": "Plan A melts the suspect bag and a known pure sample once "
                "each, slowly. Plan B melts the suspect bag three times, "
                "slowly, and no pure sample. Which plan settles it?",
        "options": [
            {"text": "Plan A, because a comparison with a known pure sample "
                     "is what counts",
             "correct": False,
             "why": "The comparison is necessary and it is not sufficient: "
                    "one run each cannot show whether either was a good run"},
            {"text": "Plan B, because three runs on the bag that matters is "
                     "the stronger piece of evidence",
             "correct": False,
             "why": "Three runs are worth having and they leave nothing to "
                    "compare the answer against"},
            {"text": "Both, because each of them collects enough readings to "
                     "reach a conclusion on its own",
             "correct": False,
             "why": "Each is missing something the other has, so neither "
                    "reaches a conclusion by itself"},
            {"text": "Neither — one has no repeats and the other has nothing "
                     "to compare against",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h11",
        "band": "harder",
        "text": "Two samples of the same substance are measured, one 99% pure "
                "and one 90% pure. Predict how their melting behaviour "
                "differs.",
        "options": [
            {"text": "The 90% sample melts sharply but several degrees below "
                     "the 99% sample",
             "correct": False,
             "why": "More impurity widens the melt as well as lowering it, so "
                    "it cannot stay sharp"},
            {"text": "The 90% sample starts melting lower and takes a wider "
                     "range to finish",
             "correct": True},
            {"text": "The 90% sample melts over a wider range, but it starts "
                     "at the same temperature",
             "correct": False,
             "why": "The start is the reading that moves furthest when more "
                    "is mixed in"},
            {"text": "They melt in the same way, because 10% is too little to "
                     "change anything",
             "correct": False,
             "why": "A few per cent is enough to widen a melt measurably, "
                    "which is why the test is used industrially"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h12",
        "band": "harder",
        "text": "A batch melts over four degrees. Run on chromatography paper "
                "beside a known pure sample, it gives two spots, one level "
                "with the pure sample's. What can now be said?",
        "options": [
            {"text": "The batch is pure, and the second spot came from the "
                     "known sample running across into its lane",
             "correct": False,
             "why": "Two lanes do not run into one another, and a pure sample "
                    "would not have melted over four degrees"},
            {"text": "The batch is a mixture of two substances, and both of "
                     "them have now been identified",
             "correct": False,
             "why": "Only the spot that matches the known sample has been "
                    "identified. The other one is still unknown"},
            {"text": "The wanted substance is missing from the batch, and both "
                     "of the spots must be impurities",
             "correct": False,
             "why": "One spot sits level with the known pure sample, which is "
                    "the wanted substance showing up exactly where it should"},
            {"text": "The batch holds the wanted substance and one other, "
                     "which is present but still unnamed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h13",
        "band": "harder",
        "text": "A powder melts over five degrees but gives a single spot on "
                "chromatography paper. What is the sensible next step?",
        "options": [
            {"text": "Trust the single spot and report the powder as pure, "
                     "since chromatography separates and melting does not",
             "correct": False,
             "why": "A five-degree melt is something a single substance "
                    "cannot do, so the spot is the result to doubt"},
            {"text": "Report the powder as pure but add a note that its "
                     "melting range was unusually wide for a pure solid",
             "correct": False,
             "why": "A wide range is not a footnote to a verdict of pure. It "
                    "contradicts it"},
            {"text": "Run the chromatography again in a different solvent, "
                     "since two substances can travel together in one",
             "correct": True},
            {"text": "Melt the powder again on a faster block to see whether "
                     "the five-degree range shows up a second time",
             "correct": False,
             "why": "A fast block narrows a wide melt, so it would make the "
                    "evidence weaker rather than checking it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h14",
        "band": "harder",
        "text": "A student argues that driving the block fast is harmless, "
                "because every batch is shifted by the same amount and the "
                "comparison still holds. Evaluate that.",
        "options": [
            {"text": "Sound, because a fair test needs every sample treated "
                     "the same way as the others",
             "correct": False,
             "why": "Treating them the same is necessary and does not rescue "
                    "a setting that changes what is being compared"},
            {"text": "Sound, because the gap between a sharp melt and a wide "
                     "one is what the comparison rests on",
             "correct": False,
             "why": "That gap is right, and driving the block fast is exactly "
                    "what shrinks it"},
            {"text": "Wrong, because heating fast affects only the "
                     "temperature a melt starts at and leaves the range alone",
             "correct": False,
             "why": "The range moves too — that is the half of the effect "
                    "that hides an impure batch"},
            {"text": "Wrong — a wide range is squashed and a sharp one "
                     "smeared, so the gap between them shrinks",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h15",
        "band": "harder",
        "text": "An anomalous run is repeated under the same conditions and "
                "gives the same odd reading again. What should be concluded?",
        "options": [
            {"text": "It is not a one-off, so there is something in the "
                     "method or the sample to be found",
             "correct": True},
            {"text": "It is confirmed as an anomaly, so both odd runs can now "
                     "be set aside with a reason",
             "correct": False,
             "why": "A reading that repeats is behaving consistently, which "
                    "is the opposite of an anomaly"},
            {"text": "The first run was right after all, so the runs that "
                     "disagree with it are the anomalous ones",
             "correct": False,
             "why": "Two readings out of four do not outrank the other two "
                    "simply by being repeated. Something is causing them"},
            {"text": "The sample is a mixture, since only a mixture can give "
                     "the same wide reading twice",
             "correct": False,
             "why": "A fault in the method repeats just as reliably as a "
                    "property of the sample does"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h16",
        "band": "harder",
        "text": "A powder melts sharply at the expected value, but stirring "
                "it into water leaves a trace of grit on the bottom. Is it "
                "pure?",
        "options": [
            {"text": "Yes, because the melting point is the measurement with "
                     "an expected value and it passed",
             "correct": False,
             "why": "It is the stronger test of the two and it is not the "
                    "only one, and the grit is something the sample should "
                    "not contain"},
            {"text": "Yes, because grit on the bottom of a beaker comes from "
                     "the beaker rather than from the powder",
             "correct": False,
             "why": "Clean glassware leaves nothing behind. The grit came in "
                    "with the powder"},
            {"text": "No, because a sample that leaves grit behind cannot "
                     "have melted sharply in the first place",
             "correct": False,
             "why": "It did melt sharply. Both results stand, and the job is "
                    "to explain how"},
            {"text": "No — the grit is an impurity, and one that stays solid "
                     "in the melt need not widen the range",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h17",
        "band": "harder",
        "text": "A shop has measured its known pure sugar at 185.0–185.5 °C "
                "on three slow runs. Which result from the suspect bag would "
                "clear the supplier?",
        "options": [
            {"text": "A melt from 178.0 °C to 185.0 °C on three slow runs "
                     "that agree with one another",
             "correct": False,
             "why": "Seven degrees, starting seven degrees low, is the "
                    "signature of a mixture"},
            {"text": "A melt from 185.0 °C to 185.5 °C on three slow runs "
                     "that agree with one another",
             "correct": True},
            {"text": "A melt from 185.0 °C to 185.5 °C on one fast run that "
                     "nothing else was compared with",
             "correct": False,
             "why": "A fast run cannot be trusted and one run has nothing to "
                    "check it against"},
            {"text": "A bag whose contents weigh exactly what the label on "
                     "the outside of it says they weigh",
             "correct": False,
             "why": "Mass says how much is in the bag, and a bulked-out bag "
                    "weighs exactly what the label claims"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h18",
        "band": "harder",
        "text": "A pure sample and a mixture of the same substance both reach "
                "53 °C part-way through melting. Explain how the two are "
                "still told apart.",
        "options": [
            {"text": "The mixture reaches 53 °C sooner, so they are told "
                     "apart by which melts first",
             "correct": False,
             "why": "Which sample gets there first depends on where each tube "
                    "sits, and neither is judged against the clock"},
            {"text": "They cannot be told apart, because both of them are "
                     "liquid at exactly the same temperature",
             "correct": False,
             "why": "Both are liquid at 53 °C, and what happened on the way "
                    "there is different and is what is measured"},
            {"text": "The pure sample is the one that reaches 53 °C at all, "
                     "because a mixture never gets that high",
             "correct": False,
             "why": "A mixture melts across a range that takes it past the "
                    "pure value on its way"},
            {"text": "The pure one starts and finishes within about a degree "
                     "of 53 °C; the mixture only passes through it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h19",
        "band": "harder",
        "text": "When a solid is impure, the temperature melting starts at "
                "moves further from the pure value than the temperature it "
                "finishes at. Why?",
        "options": [
            {"text": "Because the thermometer reads more accurately near the "
                     "end of a melt than it does at the beginning",
             "correct": False,
             "why": "A thermometer reads the same way throughout. The "
                    "difference is in the sample"},
            {"text": "Because a sample is always heated more slowly at the "
                     "start of a run than it is at the end",
             "correct": False,
             "why": "The block is taken up at one steady rate, and the "
                    "difference would not be in the sample's favour anyway"},
            {"text": "The last of the solid to melt is nearly all the wanted "
                     "substance, so it finishes near the pure value",
             "correct": True},
            {"text": "Because the impurity has all melted away by then, so "
                     "there is nothing left in the tube but the pure solid",
             "correct": False,
             "why": "Nothing leaves the tube. The impurity is still there, "
                    "spread through the liquid that has already formed"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h20",
        "band": "harder",
        "text": "Which is the stronger evidence that a powder is a mixture: a "
                "melt spread over five degrees, or a chromatogram showing one "
                "spot?",
        "options": [
            {"text": "The chromatogram, because separating a sample is a "
                     "direct test and melting it is an indirect one",
             "correct": False,
             "why": "One spot is the result that fails to separate anything, "
                    "so it is the weaker evidence here"},
            {"text": "Neither, because a single test of any kind can never "
                     "settle whether a sample is a mixture",
             "correct": False,
             "why": "A five-degree melt settles it on its own. It is not "
                    "something one substance can do"},
            {"text": "The chromatogram, because a single spot rules out "
                     "everything a melting range could have caught",
             "correct": False,
             "why": "One spot rules out very little — two substances "
                    "travelling together arrive as one"},
            {"text": "The melt, because one substance never spreads over five "
                     "degrees while two can share a spot",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h21",
        "band": "harder",
        "text": "Salt water freezes below 0 °C, and salt spread on ice makes "
                "it melt below 0 °C. Explain why those are the same fact.",
        "options": [
            {"text": "A substance freezes and melts at the same temperature, "
                     "and dissolving salt lowers it",
             "correct": True},
            {"text": "Salt gives out heat when it dissolves, which melts ice "
                     "and stops water freezing",
             "correct": False,
             "why": "Salt dissolving cools the water slightly. It is the "
                    "temperature of the change that has moved"},
            {"text": "Freezing and melting are opposite changes, so salt must "
                     "affect them in opposite directions",
             "correct": False,
             "why": "They are opposite changes at one temperature, and salt "
                    "moves that one temperature down"},
            {"text": "Salt water is denser than pure water, and a denser "
                     "liquid is harder to freeze",
             "correct": False,
             "why": "Density is not what sets a freezing temperature. It is "
                    "dissolving something in the water that lowers it, not "
                    "how tightly packed the liquid is"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h22",
        "band": "harder",
        "text": "A car's cooling system is filled with a mixture of water and "
                "antifreeze rather than with pure water. Explain the choice.",
        "options": [
            {"text": "Antifreeze boils at a lower temperature, so it carries "
                     "heat out of the engine faster than water alone",
             "correct": False,
             "why": "A coolant that boiled away sooner would be worse, and "
                    "the reason for the mixture is what happens in the cold"},
            {"text": "Antifreeze is a pure substance, so the mixture freezes "
                     "at one sharp temperature instead of a range",
             "correct": False,
             "why": "Adding it makes a mixture, which is the opposite of "
                    "freezing at one sharp temperature"},
            {"text": "Antifreeze dissolves the rust inside the pipes, which "
                     "stops them splitting",
             "correct": False,
             "why": "Rust is a different problem, and dissolving it would not "
                    "keep the liquid from freezing"},
            {"text": "The mixture stays liquid below 0 °C, so it cannot "
                     "freeze solid and split the pipes overnight",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h23",
        "band": "harder",
        "text": "A school has a melting point apparatus but no data book and "
                "no sample known to be pure. What can it honestly claim about "
                "an unknown white powder?",
        "options": [
            {"text": "Nothing at all, because a melting point without an "
                     "expected value is not a measurement",
             "correct": False,
             "why": "It is a measurement, and it is the comparison with a "
                    "known value that is missing"},
            {"text": "Whether the powder is one substance or a mixture, but "
                     "not which substance it is",
             "correct": True},
            {"text": "Which substance the powder is, because every substance "
                     "melts at a temperature of its own",
             "correct": False,
             "why": "They do, and without a list of those temperatures the "
                    "reading cannot be matched to any of them"},
            {"text": "How much of the impurity is present, from how far the "
                     "melt has been dragged down",
             "correct": False,
             "why": "Dragged down from what? With no expected value there is "
                    "nothing to measure the drop against"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h24",
        "band": "harder",
        "text": "Measured slowly, one batch melts 52.5–53.0 °C and another "
                "45.0–52.0 °C. Driven fast, the same two read 52.8–54.5 °C "
                "and 48.9–53.5 °C. What did the fast block do?",
        "options": [
            {"text": "It warmed both batches so quickly that neither of them "
                     "had melted properly by the time it was read",
             "correct": False,
             "why": "Both did melt, and both were read. The readings are "
                    "shifted, not missing"},
            {"text": "It changed the wider batch into a purer one by driving "
                     "the impurity out of it as a gas",
             "correct": False,
             "why": "Nothing leaves the tube, and the slow run afterwards "
                    "shows the batch is as impure as ever"},
            {"text": "It dragged both ranges towards the same middling "
                     "figures, hiding the difference between them",
             "correct": True},
            {"text": "It made the sharper batch read lower, which is what "
                     "brought the two batches level with each other",
             "correct": False,
             "why": "A fast block pushes readings up rather than down, and it "
                    "smears the sharp batch wider"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h25",
        "band": "harder",
        "text": "A company rejects any batch whose melting range is wider "
                "than 1.0 °C. Batch C melts 135.8–136.9 °C on one run and "
                "135.7–136.9 °C on the next. Does batch C pass?",
        "options": [
            {"text": "Yes, because the two runs agree with each other to "
                     "within a tenth of a degree",
             "correct": False,
             "why": "Agreement between runs is not the rule being applied. "
                    "The width of each melt is"},
            {"text": "Yes, because the average of 1.1 °C and 1.2 °C rounds "
                     "down to the 1.0 °C allowed",
             "correct": False,
             "why": "It rounds to 1.2 °C, and the limit is applied to the "
                    "runs rather than to an average of them"},
            {"text": "It cannot be decided, because a limit of that kind "
                     "needs at least three runs to be applied",
             "correct": False,
             "why": "Two runs both over the limit already answer it. A third "
                    "would not rescue them"},
            {"text": "No — the runs are 1.1 °C and 1.2 °C wide, and both are "
                     "over the limit",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h26",
        "band": "harder",
        "text": "A melting range cannot name what is in a batch. Why is a "
                "pharmacist still entitled to reject the batch on it?",
        "options": [
            {"text": "A medicine has to be the substance on the label and "
                     "nothing else, so evidence of anything else is enough",
             "correct": True},
            {"text": "Because the wide range shows how much of the impurity "
                     "is present, even though it cannot say what it is",
             "correct": False,
             "why": "It does not measure the amount either. All it shows is "
                    "that the sample is not one substance"},
            {"text": "Because a wide melting range is itself harmful to a "
                     "patient taking the medicine",
             "correct": False,
             "why": "The range is a measurement, not a property that could "
                    "hurt anybody. What it reveals is the problem"},
            {"text": "Because a batch may be rejected only once the impurity "
                     "in it has actually been named",
             "correct": False,
             "why": "That is the rule stood on its head. Evidence that "
                    "something else is present is enough on its own"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h27",
        "band": "harder",
        "text": "A student writes: the batch melted over four degrees, so it "
                "is impure, and the impurity must be sugar. Which part of that "
                "is supported by the measurement?",
        "options": [
            {"text": "Neither part, because four degrees is normal for a "
                     "pure sample",
             "correct": False,
             "why": "Four degrees is several times a pure melt, so the first "
                    "half of the conclusion is sound"},
            {"text": "That the batch is impure, but not that the impurity is "
                     "sugar",
             "correct": True},
            {"text": "Both parts, because a four-degree range is wide enough "
                     "to point at a particular impurity",
             "correct": False,
             "why": "How wide a range is does not name anything. Two "
                    "different impurities can widen it the same way"},
            {"text": "That the impurity is sugar, but not that the batch as a "
                     "whole should be called impure",
             "correct": False,
             "why": "That is the half the measurement cannot reach, and "
                    "impure is the half it can"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h28",
        "band": "harder",
        "text": "A known pure sample melts from 122.0 °C to 122.4 °C. A "
                "suspect sample melts from 115.5 °C to 121.8 °C. What do the "
                "two sets of figures show?",
        "options": [
            {"text": "The suspect sample is purer, because it takes longer to "
                     "get through its melt",
             "correct": False,
             "why": "Taking longer is the mixture's signature, and how long a "
                    "melt takes is not what purity is read from"},
            {"text": "The two samples are the same substance at different "
                     "temperatures, so nothing is wrong",
             "correct": False,
             "why": "One substance melts at one temperature. Different "
                    "figures are the finding, not a coincidence"},
            {"text": "The suspect sample is impure, but only because it "
                     "finishes 0.6 °C below the pure sample",
             "correct": False,
             "why": "Six tenths at the finish is a small difference. It is "
                    "the 6.5 °C at the start and the width that matter"},
            {"text": "Melting starts 6.5 °C lower and runs over 6.3 °C "
                     "instead of 0.4 °C, so the suspect sample is impure",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h29",
        "band": "harder",
        "text": "A supplier sends a certificate saying only that the batch "
                "melts at 118 °C. What would you need before that meant "
                "anything?",
        "options": [
            {"text": "A second certificate from a different supplier giving "
                     "the same figure for the same batch",
             "correct": False,
             "why": "Another certificate has the same trouble as the first "
                    "one, whoever wrote it"},
            {"text": "The name of the person who took the reading and the "
                     "date on which they took it",
             "correct": False,
             "why": "Useful for tracing it, and it still says nothing about "
                    "how the measurement was made"},
            {"text": "The start and finish of each run, and how many runs "
                     "were done",
             "correct": True},
            {"text": "A statement that the apparatus was bought this year",
             "correct": False,
             "why": "New apparatus can be used badly, and old apparatus "
                    "carefully. The readings are what settle it"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h30",
        "band": "harder",
        "text": "A sample melts sharply at the expected value on three slow "
                "runs and gives one spot on chromatography paper. How strong "
                "is that evidence together?",
        "options": [
            {"text": "Stronger than either test alone, because the two of "
                     "them miss different things",
             "correct": True},
            {"text": "No stronger than the melting point alone, since one "
                     "spot is what any sample would give",
             "correct": False,
             "why": "A mixture gives more than one spot whenever its "
                    "substances travel different distances"},
            {"text": "Weaker than the melting point alone, because a "
                     "chromatogram cannot be measured against a known value",
             "correct": False,
             "why": "A chromatogram is compared with known substances run "
                    "beside it, and an extra test does not weaken the first"},
            {"text": "Conclusive, because two tests agreeing leaves nothing "
                     "further that could be checked",
             "correct": False,
             "why": "An impurity that melts with the sample and travels with "
                    "it would pass both, so more could always be checked"},
        ],
        "figure": None,
    },

    # ── to the unit's floor of 32 per band ──────────────────────────────
    {
        "id": "c3-07-e31",
        "band": "easier",
        "text": "The sample is put into a thin tube pressed against the "
                "heated block rather than into a beaker. Why?",
        "options": [
            {"text": "So that the sample can be stirred while it is being "
                     "warmed up on the block",
             "correct": False,
             "why": "Nothing is stirred in a melting point run, and a thin "
                    "tube is the hardest place to stir anything"},
            {"text": "So that a bigger sample can be used than a beaker "
                     "would be able to hold for it",
             "correct": False,
             "why": "A tube holds far less than a beaker. A small sample is "
                    "the point, not a problem"},
            {"text": "So that the tube can be weighed on a balance before and "
                     "after the melt has finished",
             "correct": False,
             "why": "No weighing is done, and mass does not change when "
                    "something melts anyway"},
            {"text": "So that the whole of a small sample sits at the block's "
                     "temperature",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-e32",
        "band": "easier",
        "text": "Why is a substance's melting point worth printing in a data "
                "book?",
        "options": [
            {"text": "Because it tells a reader how much of the substance "
                     "will be needed for a melting point run",
             "correct": False,
             "why": "How much you need is decided by the tube. The book value "
                    "is a temperature"},
            {"text": "Because every pure sample of it melts at that "
                     "temperature, so the figure works as an expected value",
             "correct": True},
            {"text": "Because it records the highest temperature the substance "
                     "can be taken to before it burns",
             "correct": False,
             "why": "Burning is a chemical change and a different "
                    "temperature. A melting point is not a safety limit"},
            {"text": "Because it saves a chemist from having to melt the "
                     "substance in the laboratory at all",
             "correct": False,
             "why": "The book value is the thing you melt your sample to "
                    "check against, so the melting still has to be done"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s31",
        "band": "standard",
        "text": "A block of ice taken from a freezer is warmed slowly and "
                "starts turning to water at −4 °C. What does that suggest "
                "about the ice?",
        "options": [
            {"text": "That the freezer was set several degrees colder than a "
                     "freezer normally is",
             "correct": False,
             "why": "How cold the ice was to start with does not change the "
                    "temperature it turns to water at"},
            {"text": "That water from a tap always melts a few degrees below "
                     "the value a book gives",
             "correct": False,
             "why": "Pure water melts at 0 °C wherever it came from, which is "
                    "why 0 °C is the expected value"},
            {"text": "That it is not pure water — something is dissolved in "
                     "it",
             "correct": True},
            {"text": "That ice melts lower when it is warmed slowly than when "
                     "it is warmed quickly",
             "correct": False,
             "why": "Slow warming gives the truest reading of all. It cannot "
                    "drag a melt four degrees down"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-s32",
        "band": "standard",
        "text": "A technician writes the heating rate into the record as well "
                "as the two temperatures. Why does that belong in the record?",
        "options": [
            {"text": "Because anybody repeating or comparing the measurement "
                     "has to match the conditions it was taken under",
             "correct": True},
            {"text": "Because the heating rate is used to work out the "
                     "melting range once the run has finished",
             "correct": False,
             "why": "The range is the finish reading minus the start reading. "
                    "The rate does not enter the sum"},
            {"text": "Because a record of the rate shows how long the "
                     "technician spent on the run",
             "correct": False,
             "why": "How long it took is not what anybody checks the record "
                    "for"},
            {"text": "Because the apparatus will not start a run until a rate "
                     "has been written down for it",
             "correct": False,
             "why": "A dial is set on the apparatus. Writing it down is for "
                    "the people who read the record afterwards"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h31",
        "band": "harder",
        "text": "Two laboratories melt the same batch. One reports "
                "118.0–118.4 °C and the other 121.1–121.5 °C. Both used slow "
                "repeated runs. What is the likely explanation?",
        "options": [
            {"text": "The batch changed what it was made of between the two "
                     "laboratories measuring it",
             "correct": False,
             "why": "A dry solid does not change substance in transit, and it "
                    "would not shift both readings by the same three degrees"},
            {"text": "One laboratory heated its block faster, which is what "
                     "has pushed its readings three degrees up",
             "correct": False,
             "why": "Both used slow runs, and a fast block widens a melt as "
                    "well as shifting it"},
            {"text": "One thermometer reads about three degrees from the "
                     "other; both agree the melt is 0.4 °C wide",
             "correct": True},
            {"text": "The two laboratories were given different batches, "
                     "since two readings this far apart cannot be one sample",
             "correct": False,
             "why": "Two batches would be unlikely to give melts of exactly "
                    "the same width, which is what these two did"},
        ],
        "figure": None,
    },
    {
        "id": "c3-07-h32",
        "band": "harder",
        "text": "Some substances break down chemically before they get hot "
                "enough to melt. What does that do to this purity test?",
        "options": [
            {"text": "Nothing, because the temperature it breaks down at can "
                     "be used in place of a melting point",
             "correct": False,
             "why": "Breaking down is a chemical change, and the temperature "
                    "it happens at is not the property this test compares"},
            {"text": "Nothing, because a substance that breaks down on "
                     "heating was never pure to begin with",
             "correct": False,
             "why": "Plenty of pure substances break down when heated. Sugar "
                    "is one of them"},
            {"text": "It makes the test read low, since the pieces it breaks "
                     "into melt below the whole substance",
             "correct": False,
             "why": "There is no melt to read at all. The sample has become "
                    "different substances before melting could start"},
            {"text": "The test cannot be used, because the substance never "
                     "reaches a melting point to measure",
             "correct": True},
        ],
        "figure": None,
    },
]
