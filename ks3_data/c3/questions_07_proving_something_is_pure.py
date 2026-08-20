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
]
