"""B5 lesson 03 — The menstrual cycle: twelve questions (MRB-269).

The lesson's whole argument is that day 14 is one case rather than the rule:
the fortnight AFTER release is the steady part, the building phase before it
is what stretches, and the cycle is two organs running at once rather than one
event. These twelve probe exactly that — day 1 as a counting convention, the
ovary/uterus pair, the ordinary 21-to-35 range, the egg's day-long window,
where the extra length of a long cycle actually sits, what the uterus is doing
on release day, and in the harder band the arithmetic run backwards (release
observed, cycle length deduced), two cycle lengths compared, a recorded set of
four real lengths against a calendar prediction, and what happens to the lining
when a fertilised egg does implant.

The distractors are built from the lesson's three declared misconceptions —
REPRO-05 "the cycle is 28 days and the egg comes out on day 14" (which
reappears as day 14 for everybody, as release "halfway through", and as a
28-day cycle being the normal case rather than an average), REPRO-06 "a period
is the unfertilised egg leaving the body" (which reappears as the egg being
what is got rid of, and as the ovary shedding), and REPRO-19 "period blood is
waste the body has been storing up" (which reappears as the uterus, and then
the ovaries, as a store) — plus the two beliefs the page confronts without
minting: that the release day is completely unpredictable, and the part flag
18 says is most often left out, that one person's own cycles are all the same
length.

Register follows the lesson's ruled third person: nothing here addresses the
reader as someone who has cycles. `figure` is None throughout — the lesson's
one declared figure, `b5-cycle-timeline`, is `status: "retired"` and no
artwork exists for it, so pointing a question at it would name a diagram the
student cannot see.
"""

UNIT = "B5"
LESSON = "the-menstrual-cycle"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-e01",
        "band": "easier",
        "text": "Day 1 of the menstrual cycle is counted from one particular "
                "event. Which one?",
        "options": [
            {"text": "The first day of bleeding, because it is the easiest "
                     "day to notice", "correct": True},
            {"text": "The day the egg is released from the ovary, because "
                     "that is the main event", "correct": False,
             "why": "Release is not the marker. It lands roughly a fortnight "
                    "before the NEXT period, so its day moves with the length "
                    "of the cycle — and it cannot be seen from outside."},
            {"text": "The day the lining of the uterus starts to thicken "
                     "again, about five days in", "correct": False,
             "why": "The lining does start thickening then, but that is the "
                    "second event of the cycle. Counting starts before it, on "
                    "the first day of bleeding."},
            {"text": "The last day of bleeding, because the new cycle begins "
                     "once the period ends", "correct": False,
             "why": "Nothing new begins on the last day of bleeding. Day 1 is "
                    "the FIRST day of it — a place to start counting, not the "
                    "start of the process."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e02",
        "band": "easier",
        "text": "The menstrual cycle is two things happening at the same "
                "time, in two different organs. Which pair is it?",
        "options": [
            {"text": "An egg cell matures in the uterus while the lining is "
                     "built up inside an ovary", "correct": False,
             "why": "Right pair of organs, wrong way round. Egg cells are "
                    "stored and finish maturing in an ovary; the lining is "
                    "built inside the uterus."},
            {"text": "The lining is built in the uterus while blood is stored "
                     "in the ovaries for the period", "correct": False,
             "why": "The ovaries hold egg cells, not blood, and nothing is "
                    "stored up for a period. What leaves is the lining that "
                    "was built inside the uterus."},
            {"text": "An egg cell matures and is released from an ovary while "
                     "the uterus lining is built up", "correct": True},
            {"text": "An egg cell matures in one ovary while a second egg "
                     "cell is released from the other", "correct": False,
             "why": "Only one egg cell finishes maturing and is released in a "
                    "cycle. The second organ in the pair is the uterus, and "
                    "what happens there is the lining."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e03",
        "band": "easier",
        "text": "Which statement about the length of a menstrual cycle is "
                "correct?",
        "options": [
            {"text": "Every cycle is 28 days long, and any other length means "
                     "something is wrong", "correct": False,
             "why": "Twenty-eight is an average of many people's cycles, not "
                    "a rule. Anything from about 21 to about 35 days is "
                    "entirely ordinary."},
            {"text": "Cycles run from about 21 to about 35 days, and one "
                     "person's own cycles vary", "correct": True},
            {"text": "Cycles vary between people, but any one person's cycles "
                     "are always the same length", "correct": False,
             "why": "That is the part most often left out. The same person's "
                    "cycles vary from month to month, which is exactly why a "
                    "calendar predicts the day badly."},
            {"text": "Cycles can be any length at all, so nothing useful can "
                     "ever be predicted about them", "correct": False,
             "why": "The pattern is not random. About 21 to 35 days is the "
                    "ordinary range, and counting back about a fortnight from "
                    "the next period gets close to release."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e04",
        "band": "easier",
        "text": "An egg cell has just been released into the oviduct. For "
                "roughly how long can it be fertilised?",
        "options": [
            {"text": "For about a fortnight, which is until the next period "
                     "is due", "correct": False,
             "why": "A fortnight is how long the lining is held ready, not "
                    "how long the egg lasts. The egg's window is far shorter "
                    "than that."},
            {"text": "Until the next egg cell is released, about a month "
                     "later", "correct": False,
             "why": "It does not wait. If nothing fertilises it within about "
                    "a day it breaks down, unnoticed, long before the next "
                    "release."},
            {"text": "For about five days, the same length as a period",
             "correct": False,
             "why": "Five days is roughly how long the lining takes to break "
                    "down at the start of a cycle. The egg's fertilisable "
                    "window is about a day."},
            {"text": "For roughly a day, then it breaks down where it is",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-03-s01",
        "band": "standard",
        "text": "A 35-day cycle is a fortnight longer than a 21-day one. "
                "Where does that extra fortnight sit?",
        "options": [
            {"text": "Spread evenly, so every part of the cycle is a little "
                     "longer", "correct": False,
             "why": "The cycle does not stretch evenly. The fortnight after "
                    "release is close to fixed in almost everyone, so only "
                    "the phase before release can change."},
            {"text": "In the building phase before release, while the lining "
                     "thickens", "correct": True},
            {"text": "In the fortnight after release, which is longer in a "
                     "longer cycle", "correct": False,
             "why": "That interval is the steady one — close to a fortnight "
                    "whatever the length of the cycle. It is the part before "
                    "release that stretches."},
            {"text": "In the period, so a longer cycle means many more days "
                     "of bleeding", "correct": False,
             "why": "The bleeding window stays at roughly the first five "
                    "days. A long cycle is long because the lining spends "
                    "longer being built, not because the period drags on."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s02",
        "band": "standard",
        "text": "A student writes: “A period is the body getting rid of "
                "blood it has been storing up all month.” What is wrong "
                "with that?",
        "options": [
            {"text": "Nothing is wrong — the uterus does store blood, and "
                     "releases it once a month", "correct": False,
             "why": "The uterus is not a store. It builds a lining of tissue "
                    "and blood vessels ready to receive a fertilised egg, and "
                    "clears it when none implants."},
            {"text": "The blood is stored up, but it is in the ovaries rather "
                     "than the uterus", "correct": False,
             "why": "The ovaries hold egg cells, not blood — and nothing is "
                    "stored anywhere. The lining is built fresh each cycle "
                    "and cleared each cycle."},
            {"text": "It is the unfertilised egg cell that is got rid of, not "
                     "stored-up blood", "correct": False,
             "why": "An egg cell is about 0.1 mm across and breaks down where "
                    "it is, unnoticed. It is not what you can see, and it is "
                    "not what leaves."},
            {"text": "Nothing is stored up: a lining was built for a job, held "
                     "ready, then cleared", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s03",
        "band": "standard",
        "text": "In one person's cycle the egg is released on about day 16. "
                "Roughly how long is that whole cycle?",
        "options": [
            {"text": "About 30 days — release is about a fortnight before the "
                     "next period", "correct": True},
            {"text": "About 32 days, because the egg is released halfway "
                     "through the cycle", "correct": False,
             "why": "Halfway only lands on the right day by accident. Count "
                    "forwards about a fortnight from release instead, and the "
                    "cycle ends around day 30."},
            {"text": "About 28 days, because the egg is released on day 14 in "
                     "every cycle", "correct": False,
             "why": "Day 14 is release in a 28-day cycle only. This release "
                    "was two days later than that, so the cycle is about two "
                    "days longer."},
            {"text": "About 16 days, because the cycle ends when the egg is "
                     "released", "correct": False,
             "why": "The cycle does not end at release. The lining is then "
                    "held ready for about a fortnight, and day 1 of the next "
                    "cycle is when it breaks down."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s04",
        "band": "standard",
        "text": "It is release day: the mature egg cell is leaving the ovary. "
                "What is happening in the uterus that same day?",
        "options": [
            {"text": "The lining begins to break down, which is why release "
                     "and bleeding happen together", "correct": False,
             "why": "They are about a fortnight apart. The lining only breaks "
                    "down if no fertilised egg implants — and that day "
                    "becomes day 1 of the next cycle."},
            {"text": "The lining starts building from scratch, ready for the "
                     "egg that has just been released", "correct": False,
             "why": "Building started days earlier, from about day 5. By "
                    "release the lining is nearly at its full thickness, not "
                    "starting again."},
            {"text": "The lining is nearly at full thickness, and nothing "
                     "about it changes that day", "correct": True},
            {"text": "A little of the lining is shed to make room for the egg "
                     "cell to arrive", "correct": False,
             "why": "Nothing is shed at release, and the egg cell is drawn "
                    "into the oviduct rather than arriving in the uterus. The "
                    "lining is simply held ready."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-h01",
        "band": "harder",
        "text": "Over four months a person records cycles of 26, 31, 29 and "
                "27 days, then marks day 14 of next month as release day. Why "
                "is that mark wrong twice over?",
        "options": [
            {"text": "Their cycles are all shorter than 28 days, so release "
                     "must always come before day 14", "correct": False,
             "why": "One of the four is 31 days, which releases nearer day "
                    "17. And the day is not found by nudging 14 up or down — "
                    "it is found by counting back a fortnight from the end."},
            {"text": "The bleeding lasts a different number of days each "
                     "month, which moves day 1 about", "correct": False,
             "why": "Day 1 is the first day of bleeding however long the "
                    "bleeding lasts, so the count always starts in the same "
                    "place. What moves release is the length of the cycle."},
            {"text": "Release is counted back from an end that is not known "
                     "yet, and their lengths vary", "correct": True},
            {"text": "A calendar can never say anything useful about when the "
                     "egg will be released", "correct": False,
             "why": "It can get close — counting back about a fortnight from "
                    "the next period is a good estimate. The trouble is that "
                    "the next period's date is itself only a prediction."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h02",
        "band": "harder",
        "text": "One person has a 22-day cycle, another a 34-day cycle. Which "
                "comparison of the two is right?",
        "options": [
            {"text": "The longer cycle releases about 12 days later and holds "
                     "the lining ready 12 days longer", "correct": False,
             "why": "The fortnight after release is the steady part and is "
                    "about the same in both. The whole 12-day difference "
                    "sits in the building phase before release."},
            {"text": "Both release halfway through, so on about day 11 and "
                     "about day 17", "correct": False,
             "why": "Halfway is not the rule. Counting back a fortnight gives "
                    "about day 8 and about day 20 — a far bigger gap than "
                    "halfway would predict."},
            {"text": "Both release on day 14, so only what happens after "
                     "release is different", "correct": False,
             "why": "Day 14 belongs to the 28-day cycle alone. It would leave "
                    "8 days after release in one and 20 in the other — "
                    "nowhere near a fortnight either time."},
            {"text": "The longer cycle releases about 12 days later, and both "
                     "then wait about a fortnight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h03",
        "band": "harder",
        "text": "“Twenty-eight is the average cycle length, so most "
                "people must have 28-day cycles.” Which reply is right?",
        "options": [
            {"text": "The average is wrong — researchers who tracked real cycles "
                     "found that the true average was nearer 30", "correct": False,
             "why": "The average is not the problem, and no replacement "
                    "number is on offer. What the tracking studies found was "
                    "a spread rather than a number."},
            {"text": "An average can be a real fact about a population and "
                     "still describe almost nobody in it", "correct": True},
            {"text": "It is right — 28 is the commonest length, and other "
                     "lengths are unusual ones", "correct": False,
             "why": "Ordinary cycles run from about 21 to about 35 days, and "
                    "the same person varies between months. Twenty-eight is "
                    "an average of many people, not the normal case."},
            {"text": "Averages should never be used in biology, because "
                     "living things vary far too much", "correct": False,
             "why": "The average is a real fact about the population. The "
                    "mistake is using it as a rule about one person, not "
                    "working it out in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h04",
        "band": "harder",
        "text": "A fertilised egg implants in the lining of the uterus. What "
                "happens instead of the next period?",
        "options": [
            {"text": "The lining stays where it is, and the cycle stops "
                     "there", "correct": True},
            {"text": "The lining still breaks down, but is rebuilt much "
                     "faster than usual", "correct": False,
             "why": "If it broke down, the implanted egg would go with it. "
                    "The lining is kept — which is why the cycle stops at "
                    "held ready instead of starting again at event 1."},
            {"text": "The ovary releases a second egg cell straight away to "
                     "keep the cycle going", "correct": False,
             "why": "No further egg cell is released once one has gone that "
                    "cycle, and a second one would not change what the lining "
                    "does. The lining simply stays."},
            {"text": "The period arrives on time, and the lining is rebuilt "
                     "around the implanted egg", "correct": False,
             "why": "The period IS the lining breaking down, so it cannot "
                    "arrive and leave the lining intact. When an egg implants "
                    "the lining is not broken down at all."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-e05",
        "band": "easier",
        "text": "Over roughly which days of a cycle does the lining of the "
                "uterus break down and pass out through the vagina?",
        "options": [
            {"text": "The five days just before the next period",
             "correct": False,
             "why": "Those are days when the lining is still being held at "
                    "its thickest. It breaks down at the start of a cycle, "
                    "not at the end of one."},
            {"text": "The days immediately after the egg is released",
             "correct": False,
             "why": "The lining is nearly at full thickness then, and it is "
                    "held that way for about a fortnight afterwards."},
            {"text": "Roughly the first five days of the cycle",
             "correct": True},
            {"text": "The whole of the second half of the cycle",
             "correct": False,
             "why": "The second half is the fortnight in which the lining is "
                    "held ready. Breaking down is quick, and it is what day 1 "
                    "is counted from."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e06",
        "band": "easier",
        "text": "In which organ is a lining built up and then broken down "
                "each cycle?",
        "options": [
            {"text": "The uterus", "correct": True},
            {"text": "The ovary", "correct": False,
             "why": "The ovary is the other half of the cycle: one egg cell "
                    "finishes maturing there and is released. It builds no "
                    "lining."},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is the tube a released egg is drawn into. "
                    "Nothing is built up inside it."},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is the ring of muscle at the lower end of the "
                    "uterus. The lining is inside the uterus itself."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e07",
        "band": "easier",
        "text": "A mature egg cell has just left the ovary. Where does it go "
                "next?",
        "options": [
            {"text": "Straight into the uterus", "correct": False,
             "why": "The uterus is further on. There is a tube to travel "
                    "along first, and it is in that tube that the egg can be "
                    "fertilised."},
            {"text": "Into the lining of the uterus", "correct": False,
             "why": "Only a fertilised egg embeds in the lining, and that is "
                    "several days later. An unfertilised one never gets that "
                    "far."},
            {"text": "Out through the vagina", "correct": False,
             "why": "What leaves during a period is the lining, not the egg. "
                    "The egg is 0.1 mm across and breaks down where it is."},
            {"text": "Into the oviduct", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-03-s05",
        "band": "standard",
        "text": "After the egg has been released, the lining of the uterus is "
                "held at its thickest for about a fortnight. What is it being "
                "held ready for?",
        "options": [
            {"text": "So the next egg cell has somewhere to finish maturing",
             "correct": False,
             "why": "Egg cells mature inside an ovary, not in the uterus. The "
                    "lining has nothing to do with that half of the cycle."},
            {"text": "In case a fertilised egg arrives and implants in it",
             "correct": True},
            {"text": "So that the next period will be shorter when it comes",
             "correct": False,
             "why": "The lining is built to be used, not to make its own "
                    "removal easier. What breaks down is exactly what was "
                    "built."},
            {"text": "To protect the ovary while it recovers from releasing "
                     "an egg", "correct": False,
             "why": "The two organs are not protecting each other. The lining "
                    "is inside the uterus, and the ovary carries on "
                    "regardless."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s06",
        "band": "standard",
        "text": "Why is day 1 counted from the first day of bleeding rather "
                "than from the day the egg is released?",
        "options": [
            {"text": "Because the lining begins to be built on that day",
             "correct": False,
             "why": "On that day the lining is breaking down, not being "
                    "built. Building starts once the breaking down is over."},
            {"text": "Because release always falls on day 14, so it would be "
                     "the same number anyway", "correct": False,
             "why": "Release moves with the length of the cycle. It is "
                    "precisely the event that cannot be pinned to a fixed "
                    "number."},
            {"text": "Because bleeding is genuinely the first thing that "
                     "happens in a cycle", "correct": False,
             "why": "A cycle is a loop, so nothing in it is genuinely first. "
                    "Day 1 is a place to start counting, not the start of the "
                    "process."},
            {"text": "Because bleeding is something that can be noticed, "
                     "and release is not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s07",
        "band": "standard",
        "text": "Someone’s cycles are 26 days long. Roughly how many days "
                "pass between the egg being released and the start of the "
                "next period?",
        "options": [
            {"text": "About 14 days — close to a fortnight, whatever the "
                     "length of the cycle", "correct": True},
            {"text": "About 12 days, because a 26-day cycle is shorter than a "
                     "28-day one", "correct": False,
             "why": "The shortening does not fall here. It is the building "
                    "phase, before release, that stretches and shrinks with "
                    "the length of the cycle."},
            {"text": "About 13 days, because release happens exactly halfway "
                     "through", "correct": False,
             "why": "Halfway is a guess that happens to be close in a 26-day "
                    "cycle and is wrong in most others. The steady interval "
                    "is the one after release."},
            {"text": "About 26 days, because the next cycle starts from "
                     "release", "correct": False,
             "why": "Day 1 is the first day of bleeding, not the day of "
                    "release. Twenty-six days is the whole cycle, not the "
                    "part after release."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-h05",
        "band": "harder",
        "text": "Someone’s cycles are 31 days long. Working from day 1, "
                "roughly which day of the cycle is the egg released?",
        "options": [
            {"text": "About day 14, the day that applies to every cycle",
             "correct": False,
             "why": "Day 14 is release in a 28-day cycle and in no other. In "
                    "a 31-day cycle it would leave seventeen days before the "
                    "next period."},
            {"text": "About day 17, a fortnight back from the end of the "
                     "cycle", "correct": True},
            {"text": "About day 16, exactly halfway through the 31 days",
             "correct": False,
             "why": "Halfway is the wrong rule, and here it lands close by "
                    "luck rather than by reasoning. Count back a fortnight "
                    "from the end of the cycle instead."},
            {"text": "About day 15, a fortnight forward from day 1",
             "correct": False,
             "why": "The fortnight belongs at the other end. It is the gap "
                    "between release and the next period, so it is counted "
                    "back from day 31."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h06",
        "band": "harder",
        "text": "An egg cell can be fertilised for roughly a day, but the "
                "lining of the uterus is held ready for about a fortnight. "
                "Why are the two windows so different?",
        "options": [
            {"text": "Because the lining takes about a fortnight to break "
                     "down once it starts", "correct": False,
             "why": "The breaking down is the period, and it is over in about "
                    "five days. The fortnight is time spent holding the "
                    "lining, not clearing it."},
            {"text": "Because the next egg cell takes about a fortnight to "
                     "finish maturing", "correct": False,
             "why": "Maturing happens in the ovary during the building phase, "
                    "before release. The fortnight after release is not spent "
                    "on it."},
            {"text": "Because a fertilised egg arrives days later and stays, "
                     "so the lining must be ready throughout", "correct": True},
            {"text": "Because a fertilised egg survives in the oviduct for a "
                     "fortnight before moving on", "correct": False,
             "why": "The fertilised cell divides as it travels and takes "
                    "about five days, not a fortnight. What the lining is "
                    "waiting through is that journey."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h07",
        "band": "harder",
        "text": "In a 21-day cycle the period lasts about five days. Roughly "
                "how many days are there between the end of the period and "
                "the release of the egg?",
        "options": [
            {"text": "About two days", "correct": True},
            {"text": "About seven days", "correct": False,
             "why": "Seven is the day of release itself, counted from day 1. "
                    "The question asks how much of the building phase is left "
                    "once the period has ended."},
            {"text": "About nine days", "correct": False,
             "why": "Nine would be right in a 28-day cycle, where release "
                    "falls near day 14. A 21-day cycle takes its seven days "
                    "off the front of the cycle."},
            {"text": "About fourteen days", "correct": False,
             "why": "Fourteen is the gap after release, not before it. That "
                    "interval is the one part of the cycle that hardly "
                    "changes."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ──────────────────────────────────────────
    #
    # The cycle itself: the four events, the two organs running at once, what
    # stretches and what does not, and why an average is not a rule. No
    # hormone is named anywhere, in line with the statutory exclusion the
    # lesson honours. Rung 1 owns "which day is the egg released" and rung 2
    # owns "what leaves the body during a period", so neither task is
    # rewritten here; the same science is reached from other directions.
    # Register follows the lesson's ruled third person throughout.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-e08",
        "band": "easier",
        "text": "Which organ releases an egg cell each cycle?",
        "options": [
            {"text": "An ovary", "correct": True},
            {"text": "The uterus", "correct": False,
             "why": "The uterus is the other half of the cycle: its lining is "
                    "built up and broken down. It holds no egg cells."},
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct is the tube the released egg is drawn into. "
                    "It receives rather than releases."},
            {"text": "The cervix", "correct": False,
             "why": "The cervix is the ring of muscle at the lower end of the "
                    "uterus, a long way from any egg cell."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e09",
        "band": "easier",
        "text": "From about which day of the cycle does the lining of the "
                "uterus start to thicken again?",
        "options": [
            {"text": "About day 1", "correct": False,
             "why": "Day 1 is the first day of bleeding, when the old lining "
                    "is breaking down. Building starts once that is over."},
            {"text": "About day 5", "correct": True},
            {"text": "About day 14", "correct": False,
             "why": "By day 14 of a 28-day cycle the lining is nearly at full "
                    "thickness. It has been building for over a week."},
            {"text": "About day 21", "correct": False,
             "why": "By then the lining is finished and is being held ready. "
                    "Building happens earlier in the cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e10",
        "band": "easier",
        "text": "What is the lining of the uterus made of?",
        "options": [
            {"text": "Stored blood, kept back for the next period",
             "correct": False,
             "why": "Nothing is stored up. A lining of tissue and blood "
                    "vessels is built fresh each cycle."},
            {"text": "Muscle, which contracts to clear it out",
             "correct": False,
             "why": "The wall of the uterus is muscular, but the lining inside "
                    "it is tissue with blood vessels running through it."},
            {"text": "A layer of egg cells waiting to be released",
             "correct": False,
             "why": "Egg cells are held in the ovaries, never in the uterus, "
                    "and only one is released a cycle."},
            {"text": "Tissue and blood vessels", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e11",
        "band": "easier",
        "text": "What happens to the lining of the uterus if no fertilised egg "
                "implants in it?",
        "options": [
            {"text": "It is kept and used again in the next cycle",
             "correct": False,
             "why": "It is not kept. It breaks down, and then a new one is "
                    "built from the start."},
            {"text": "It breaks down and passes out through the vagina",
             "correct": True},
            {"text": "It is absorbed back into the wall of the uterus",
             "correct": False,
             "why": "It leaves the body rather than being taken back in. That "
                    "is what makes day 1 easy to notice."},
            {"text": "It keeps thickening until the next cycle begins",
             "correct": False,
             "why": "It is held at its thickest for about a fortnight and then "
                    "breaks down. Nothing goes on thickening indefinitely."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e12",
        "band": "easier",
        "text": "How many egg cells finish maturing in one cycle?",
        "options": [
            {"text": "About four hundred", "correct": False,
             "why": "About four hundred is roughly the number across a whole "
                    "lifetime, one cycle at a time."},
            {"text": "Two", "correct": False,
             "why": "A single egg cell finishes maturing, in one ovary. The "
                    "other ovary does nothing that cycle."},
            {"text": "Only one", "correct": True},
            {"text": "One for each day of the building phase",
             "correct": False,
             "why": "The building phase takes days, and one egg cell finishes "
                    "maturing across the whole of it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e13",
        "band": "easier",
        "text": "For about how long is the lining held at its thickest after "
                "the egg has been released?",
        "options": [
            {"text": "About five days", "correct": False,
             "why": "Five days is roughly how long the lining takes to break "
                    "down at the start of a cycle."},
            {"text": "About a day", "correct": False,
             "why": "A day is how long the released egg stays able to be "
                    "fertilised. The lining waits far longer than that."},
            {"text": "About a month", "correct": False,
             "why": "A month is the whole cycle. The holding is the last "
                    "fortnight of it."},
            {"text": "About a fortnight", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e14",
        "band": "easier",
        "text": "What does the figure of 28 days describe?",
        "options": [
            {"text": "An average of many people's cycles", "correct": True},
            {"text": "The length every ordinary cycle has", "correct": False,
             "why": "Anything from about 21 to about 35 days is ordinary, so "
                    "no single length belongs to every cycle."},
            {"text": "The longest a cycle can run", "correct": False,
             "why": "Cycles of 30 and 35 days are entirely ordinary, so 28 is "
                    "nothing like a ceiling."},
            {"text": "The length of one person's cycles, every month",
             "correct": False,
             "why": "One person's own cycles vary from month to month, which "
                    "is the part most often left out."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e15",
        "band": "easier",
        "text": "What are the days at the start of a cycle called, when the "
                "lining breaks down?",
        "options": [
            {"text": "The building phase", "correct": False,
             "why": "Building is what comes next, once the old lining has "
                    "gone. The two are consecutive, not the same."},
            {"text": "The period", "correct": True},
            {"text": "Release", "correct": False,
             "why": "Release is the egg cell leaving an ovary, about a "
                    "fortnight before the NEXT period."},
            {"text": "The holding phase", "correct": False,
             "why": "Holding is the fortnight after release, when the lining "
                    "is at its thickest rather than breaking down."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e16",
        "band": "easier",
        "text": "Why is the menstrual cycle drawn as a circle?",
        "options": [
            {"text": "Because the uterus and the ovary are drawn as circles",
             "correct": False,
             "why": "The shape of the drawing is not the shape of the organs. "
                    "It is the sequence that closes on itself."},
            {"text": "Because it takes about a month, like the moon",
             "correct": False,
             "why": "The lunar month is a coincidence the lesson mentions, not "
                    "a reason for the way the cycle is drawn."},
            {"text": "Because it ends where it starts", "correct": True},
            {"text": "Because it runs at one speed", "correct": False,
             "why": "Cycles run anywhere from about 21 to about 35 days, and "
                    "vary within one person too."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e17",
        "band": "easier",
        "text": "The lining that breaks down passes out of the body through "
                "which structure?",
        "options": [
            {"text": "The oviduct", "correct": False,
             "why": "The oviduct runs between an ovary and the uterus, at the "
                    "top of the system. Nothing leaves the body along it."},
            {"text": "The ovary", "correct": False,
             "why": "The ovary releases an egg cell into the oviduct. It is "
                    "not on the route out at all."},
            {"text": "The urethra", "correct": False,
             "why": "The urethra carries urine, and it is a separate tube from "
                    "the one the lining leaves by."},
            {"text": "The vagina", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e18",
        "band": "easier",
        "text": "Which part of the cycle comes immediately after the period?",
        "options": [
            {"text": "The building phase", "correct": True},
            {"text": "Release", "correct": False,
             "why": "Release comes later, once one egg cell has finished "
                    "maturing and the lining has thickened."},
            {"text": "The fortnight of holding the lining ready",
             "correct": False,
             "why": "Holding is the last part of the cycle, after release "
                    "rather than before it."},
            {"text": "The next period", "correct": False,
             "why": "A whole cycle of building, release and holding comes "
                    "between one period and the next."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e19",
        "band": "easier",
        "text": "Which part of the cycle comes immediately after the egg has "
                "been released?",
        "options": [
            {"text": "The period", "correct": False,
             "why": "The period is about a fortnight further on, and it is day "
                    "1 of the NEXT cycle."},
            {"text": "The building phase", "correct": False,
             "why": "Building happens before release. By release the lining is "
                    "nearly at full thickness."},
            {"text": "The lining is held ready", "correct": True},
            {"text": "A second egg cell is released", "correct": False,
             "why": "No further egg cell is released once one has gone that "
                    "cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e20",
        "band": "easier",
        "text": "What does the length of a cycle measure?",
        "options": [
            {"text": "The days from the first day of one period to the first "
                     "day of the next", "correct": True},
            {"text": "The days from the end of one period to the start of the "
                     "next one", "correct": False,
             "why": "Counting starts on day 1, the FIRST day of bleeding, and "
                    "runs to day 1 of the next cycle."},
            {"text": "The days from the release of one egg to the release of "
                     "the next", "correct": False,
             "why": "Release cannot be seen from outside, which is why the "
                    "count is not taken from it."},
            {"text": "The days the bleeding itself lasts, at the start of a "
                     "cycle", "correct": False,
             "why": "That is the period, roughly the first five days. The "
                    "cycle is the whole loop."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e21",
        "band": "easier",
        "text": "Does the egg cell leave the ovary before or after the lining "
                "has started to thicken?",
        "options": [
            {"text": "Before — the lining only starts once an egg has gone",
             "correct": False,
             "why": "The lining starts thickening from about day 5, well "
                    "before release. The two run alongside each other."},
            {"text": "Before — the lining is built to replace the egg that has "
                     "gone", "correct": False,
             "why": "The lining is built to receive a fertilised egg, not to "
                    "replace one, and it starts before release."},
            {"text": "At the same moment, so the two always happen together",
             "correct": False,
             "why": "Thickening takes days and release is a single moment "
                    "part way through it."},
            {"text": "After — the lining has been thickening for days by then",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e22",
        "band": "easier",
        "text": "Which interval of the cycle is the steadier one from person "
                "to person?",
        "options": [
            {"text": "The days from day 1 to release", "correct": False,
             "why": "That is the stretchy part: longer in a long cycle and "
                    "shorter in a short one."},
            {"text": "The days the period itself lasts", "correct": False,
             "why": "Roughly five days is usual, but it is not the interval "
                    "the counting rule is built on."},
            {"text": "The days from release to the next period",
             "correct": True},
            {"text": "The days from the end of the period to release",
             "correct": False,
             "why": "That sits inside the building phase, so it stretches and "
                    "shrinks with the length of the cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e23",
        "band": "easier",
        "text": "What is the first event of a cycle?",
        "options": [
            {"text": "One egg cell finishes maturing in an ovary",
             "correct": False,
             "why": "That happens during the building phase, which is the "
                    "second event rather than the first."},
            {"text": "The lining of the uterus breaks down", "correct": True},
            {"text": "The lining of the uterus is held at its thickest",
             "correct": False,
             "why": "Holding is the last event of a cycle, in the fortnight "
                    "after release."},
            {"text": "A mature egg cell leaves an ovary", "correct": False,
             "why": "Release is the third event, about a fortnight before the "
                    "next period."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e24",
        "band": "easier",
        "text": "What is the last event of a cycle?",
        "options": [
            {"text": "The lining is held at its thickest", "correct": True},
            {"text": "The lining thickens with tissue and blood vessels",
             "correct": False,
             "why": "Thickening is the second event, between the period and "
                    "release."},
            {"text": "A mature egg cell leaves an ovary", "correct": False,
             "why": "Release is the third event. A fortnight of holding "
                    "follows it."},
            {"text": "The lining breaks down and passes out", "correct": False,
             "why": "That is event 1 — of the NEXT cycle. It is where the loop "
                    "closes rather than where it ends."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e25",
        "band": "easier",
        "text": "Which has the longer building phase: a 35-day cycle or a "
                "21-day cycle?",
        "options": [
            {"text": "The 21-day cycle", "correct": False,
             "why": "The short cycle is short at the front. Its building phase "
                    "is the shorter of the two."},
            {"text": "Neither — building takes five days in both",
             "correct": False,
             "why": "Five days is roughly the period. Building takes whatever "
                    "the cycle has left after the fortnight at the end."},
            {"text": "Neither — building takes a fortnight in both",
             "correct": False,
             "why": "The fortnight belongs to the other end of the cycle, "
                    "after release."},
            {"text": "The 35-day cycle", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e26",
        "band": "easier",
        "text": "How does the gap from release to the next period compare in a "
                "short cycle and a long one?",
        "options": [
            {"text": "It is much shorter in a short cycle", "correct": False,
             "why": "It is the part that hardly changes. What shortens is the "
                    "building phase before release."},
            {"text": "It is exactly half the cycle in both", "correct": False,
             "why": "Half of 21 days is about 10 and half of 35 is about 17. "
                    "The gap is close to 14 in both."},
            {"text": "It is much longer in a short cycle", "correct": False,
             "why": "Nothing about a short cycle lengthens. Its building phase "
                    "is shorter and the rest is unchanged."},
            {"text": "It is about the same in both", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e27",
        "band": "easier",
        "text": "Which two things does the uterus lining do across one cycle?",
        "options": [
            {"text": "It is built up, and then broken down", "correct": True},
            {"text": "It is built up, and then absorbed into the ovary",
             "correct": False,
             "why": "Nothing passes from the uterus to an ovary, and the "
                    "lining leaves the body rather than being taken in."},
            {"text": "It is broken down, and then stored for the next cycle",
             "correct": False,
             "why": "Nothing is stored. A fresh lining is built from the start "
                    "each cycle."},
            {"text": "It is released, and then replaced by a new egg cell",
             "correct": False,
             "why": "Egg cells come from the ovaries and never form a lining. "
                    "The two are separate things in separate organs."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e28",
        "band": "easier",
        "text": "What part does the oviduct play in the cycle?",
        "options": [
            {"text": "Its lining thickens and then breaks down each cycle",
             "correct": False,
             "why": "The lining belongs to the uterus. The oviduct builds "
                    "nothing."},
            {"text": "It holds the egg cells", "correct": False,
             "why": "The egg cells are held in the ovaries. The oviduct only "
                    "receives one after it is released."},
            {"text": "The released egg cell is drawn into it", "correct": True},
            {"text": "It releases one egg cell about every month",
             "correct": False,
             "why": "Releasing is the ovary's part. The oviduct is the tube "
                    "beyond it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e29",
        "band": "easier",
        "text": "How does the lesson describe the building phase of the cycle?",
        "options": [
            {"text": "As the part that is the same length in everybody",
             "correct": False,
             "why": "It is the part that differs most. The fortnight after "
                    "release is the steady one."},
            {"text": "As the stretchy part of the cycle", "correct": True},
            {"text": "As the part that cannot be measured", "correct": False,
             "why": "It can be worked out: it is whatever is left once the "
                    "period and the closing fortnight are taken off."},
            {"text": "As the shortest part", "correct": False,
             "why": "In a 35-day cycle it is the longest part by far. Only in "
                    "a very short cycle is it brief."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-e30",
        "band": "easier",
        "text": "How many days does an ordinary period last?",
        "options": [
            {"text": "About two days", "correct": False,
             "why": "Rather short. The bleeding takes up roughly the first "
                    "five days of a cycle."},
            {"text": "About five days", "correct": True},
            {"text": "About ten days", "correct": False,
             "why": "Twice as long as usual. In a 21-day cycle that would be "
                    "half the cycle gone before building could start."},
            {"text": "About a fortnight", "correct": False,
             "why": "A fortnight is the interval at the OTHER end of the "
                    "cycle, when the lining is held at full thickness."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-03-s08",
        "band": "standard",
        "text": "Which of these gives the four events of the cycle in the "
                "right order?",
        "options": [
            {"text": "Release; the lining breaks down; the lining thickens; "
                     "the lining is held ready", "correct": False,
             "why": "Day 1 is the first day of bleeding, so the breakdown is "
                    "where the count starts."},
            {"text": "The lining breaks down; the lining thickens while an egg "
                     "matures; release; the lining is held ready",
             "correct": True},
            {"text": "The lining thickens; the lining breaks down; release; "
                     "the lining is held ready", "correct": False,
             "why": "Breaking down comes first in the count. Thickening is "
                    "what follows it, from about day 5."},
            {"text": "The lining breaks down; release; the lining thickens "
                     "with tissue and blood vessels; it is held ready",
             "correct": False,
             "why": "The lining is nearly at full thickness by release, so "
                    "the thickening comes before it and not after."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s09",
        "band": "standard",
        "text": "Why is the gap between release and the next period the "
                "interval the counting rule is built on?",
        "options": [
            {"text": "Because it is the longest part of every cycle",
             "correct": False,
             "why": "In a 35-day cycle the building phase is far longer. "
                    "Length is not what makes an interval useful here."},
            {"text": "Because it can be seen from outside, unlike the rest",
             "correct": False,
             "why": "Release cannot be seen at all. What can be seen is the "
                    "bleeding at either end."},
            {"text": "Because it is close to a fortnight in almost everyone",
             "correct": True},
            {"text": "Because it is exactly half of a 28-day cycle",
             "correct": False,
             "why": "It happens to be half of 28, and that is a coincidence of "
                    "one cycle length rather than the reason."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s10",
        "band": "standard",
        "text": "A cycle runs 21 days. Taking off the fortnight at the end "
                "of it, how many days are left for everything before "
                "release?",
        "options": [
            {"text": "About 14", "correct": False,
             "why": "Fourteen is the part at the END. What is left for the "
                    "beginning is 21 take away 14."},
            {"text": "About 35", "correct": False,
             "why": "This adds the fortnight instead of subtracting it. The "
                    "holding is part of the 21 days, not extra to it."},
            {"text": "About 21", "correct": False,
             "why": "That is the whole cycle. The closing fortnight has to be "
                    "taken off it."},
            {"text": "About 7", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s11",
        "band": "standard",
        "text": "Why does a longer cycle not mean more days of bleeding?",
        "options": [
            {"text": "Because the bleeding window stays at roughly the first "
                     "five days", "correct": True},
            {"text": "Because a longer cycle builds a thinner lining, so there "
                     "is less to clear", "correct": False,
             "why": "A longer building phase does not make a thinner lining. "
                    "What changes is how long the building takes."},
            {"text": "Because the bleeding is spread over the whole of the "
                     "extra time instead", "correct": False,
             "why": "It is not spread anywhere. It sits at the start of the "
                    "cycle and lasts about the same time."},
            {"text": "Because the extra days are added after the bleeding has "
                     "already finished, at the very end", "correct": False,
             "why": "The extra days fall in the building phase, before "
                    "release. The end of the cycle is the fixed part."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s12",
        "band": "standard",
        "text": "One person's cycle is 28 days one month and 33 days the next. "
                "Which part of the cycle changed?",
        "options": [
            {"text": "The period, which must have lasted five days longer",
             "correct": False,
             "why": "The bleeding stays at roughly five days. Five extra days "
                    "of it would be a very different claim."},
            {"text": "The fortnight after release, which stretched to nineteen "
                     "days", "correct": False,
             "why": "That interval is the steady one — close to a fortnight in "
                    "almost everyone, and in almost every cycle."},
            {"text": "Every part of it, each by about a fifth", "correct": False,
             "why": "The cycle does not stretch evenly. Only the building "
                    "phase changes length."},
            {"text": "The building phase before release", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s13",
        "band": "standard",
        "text": "The lining is built, then held ready. What decides whether it "
                "stays or breaks down?",
        "options": [
            {"text": "Only whether a fertilised egg implants in it",
             "correct": True},
            {"text": "Whether an egg cell was released that cycle",
             "correct": False,
             "why": "An egg is released either way. What matters is whether a "
                    "fertilised one arrives and embeds."},
            {"text": "Whether the lining reached its full thickness in time",
             "correct": False,
             "why": "It reaches full thickness before release in an ordinary "
                    "cycle, and still breaks down if nothing implants."},
            {"text": "How long the cycle turned out to be", "correct": False,
             "why": "A long cycle and a short one both end the same way if "
                    "nothing implants."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s14",
        "band": "standard",
        "text": "One person's bleeding lasts three days one month and six the "
                "next. Does that change which day is counted as day 1?",
        "options": [
            {"text": "Yes — day 1 moves to the middle of the bleeding",
             "correct": False,
             "why": "Day 1 is the first day of bleeding however long the "
                    "bleeding runs. Nothing about it moves."},
            {"text": "Yes — day 1 is the last day of bleeding, so it moves by "
                     "three days", "correct": False,
             "why": "Day 1 is the FIRST day of bleeding. Nothing new begins on "
                    "the last day of it."},
            {"text": "No — day 1 is always the first day of bleeding",
             "correct": True},
            {"text": "No — day 1 is fixed to the calendar, so it is the same "
                     "date every month", "correct": False,
             "why": "It is fixed to an event rather than to a date, and cycles "
                    "are not a whole number of months long."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s15",
        "band": "standard",
        "text": "Why does counting forwards from day 1 predict the day of "
                "release badly?",
        "options": [
            {"text": "Because the days before release stretch and shrink with "
                     "the cycle", "correct": True},
            {"text": "Because day 1 itself cannot be identified with any "
                     "confidence", "correct": False,
             "why": "Day 1 is the easiest day in the cycle to notice, which is "
                    "exactly why the counting starts there."},
            {"text": "Because release happens at a different point in the "
                     "bleeding each month", "correct": False,
             "why": "Release is nowhere near the bleeding. It falls about a "
                    "fortnight before the NEXT period."},
            {"text": "Because the days after release stretch and shrink with "
                     "the cycle", "correct": False,
             "why": "Those are the steady days. It is the building phase "
                    "before release that varies."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s16",
        "band": "standard",
        "text": "Even used correctly, the counting rule cannot give the day of "
                "release in advance. Why not?",
        "options": [
            {"text": "Because the rule only works for cycles of exactly 28 "
                     "days", "correct": False,
             "why": "It works for any length — that is the point of counting "
                    "back a fortnight rather than forwards to day 14."},
            {"text": "Because it counts back from the next period, whose date "
                     "is itself only a prediction", "correct": True},
            {"text": "Because release happens at random from one cycle to "
                     "the next, so no rule could ever reach it",
             "correct": False,
             "why": "The pattern is not random. Counting back about a "
                    "fortnight gets close, once the end is known."},
            {"text": "Because the fortnight after release is different in "
                     "everybody", "correct": False,
             "why": "That interval is the steady one. The trouble is at the "
                    "other end of the cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s17",
        "band": "standard",
        "text": "What is happening in an ovary during the days of bleeding?",
        "options": [
            {"text": "An egg cell is being released into the oviduct",
             "correct": False,
             "why": "Release comes about a fortnight before the NEXT period, "
                    "not during this one."},
            {"text": "The ovary is shedding a layer of its own, alongside the "
                     "uterus", "correct": False,
             "why": "The ovary sheds nothing. It releases one egg cell a cycle "
                    "and stays as it is."},
            {"text": "Nothing has been released, and one egg cell will begin "
                     "maturing", "correct": True},
            {"text": "The ovary is building a store of egg cells for the "
                     "cycles to come", "correct": False,
             "why": "No new egg cells are made. The stock was complete before "
                    "birth."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s18",
        "band": "standard",
        "text": "On the day of release, what is happening in the ovary?",
        "options": [
            {"text": "A mature egg cell leaves it and is drawn into the "
                     "oviduct", "correct": True},
            {"text": "It begins building a lining of its own, ready for an "
                     "embryo", "correct": False,
             "why": "The lining belongs to the uterus. An ovary builds no "
                    "lining at any point in the cycle."},
            {"text": "Several egg cells leave together", "correct": False,
             "why": "One egg cell finishes maturing and one is released. There "
                    "is no group to choose from."},
            {"text": "It takes back the egg cell it released in the previous "
                     "cycle", "correct": False,
             "why": "Nothing returns to an ovary. A released egg that is not "
                    "fertilised breaks down where it is."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s19",
        "band": "standard",
        "text": "Why is 28 such a familiar number for a cycle length?",
        "options": [
            {"text": "Because a cycle is timed by the moon, which runs on the "
                     "same clock", "correct": False,
             "why": "The closeness to a lunar month is a coincidence. Nothing "
                    "about the moon sets a cycle's length."},
            {"text": "Because it is close to an average of many cycles, and "
                     "close to a lunar month", "correct": True},
            {"text": "Because the great majority of real cycles turn out to "
                     "measure exactly 28 days", "correct": False,
             "why": "Tracking real cycles found a spread rather than a number. "
                    "Most are not 28 days at all."},
            {"text": "Because it is four weeks, and the body works in whole "
                     "weeks", "correct": False,
             "why": "Nothing in the body counts weeks. Four weeks is a "
                    "convenience of the calendar."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s20",
        "band": "standard",
        "text": "Researchers tracked large numbers of real cycles. What did "
                "the results look like?",
        "options": [
            {"text": "A single number, confirming 28 days for almost everyone",
             "correct": False,
             "why": "That is the belief the tracking overturned. What came "
                    "back was a range rather than a figure."},
            {"text": "A spread, with most cycles in the twenties or low "
                     "thirties", "correct": True},
            {"text": "Two clear groups, one at 21 days and one at 35",
             "correct": False,
             "why": "Those are the ends of the ordinary range, not two camps. "
                    "Lengths in between are the commonest of all."},
            {"text": "No pattern at all, with cycles of any length equally "
                     "likely", "correct": False,
             "why": "A spread is still a pattern. Cycles far outside about 21 "
                    "to 35 days are unusual."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s21",
        "band": "standard",
        "text": "Two people both have 28-day cycles, but one bleeds for three "
                "days and the other for six. Does that change when each "
                "releases an egg?",
        "options": [
            {"text": "Yes — the one who bleeds longer releases three days "
                     "later", "correct": False,
             "why": "Release is counted back from the end of the cycle, and "
                    "both cycles end after 28 days."},
            {"text": "Yes — the one who bleeds longer has a shorter cycle "
                     "overall", "correct": False,
             "why": "Both cycles are 28 days, which is given. How long the "
                    "bleeding lasts does not change that."},
            {"text": "No — both release about a fortnight before the next "
                     "period", "correct": True},
            {"text": "No — release is on day 14 for everybody, whatever the "
                     "cycle does", "correct": False,
             "why": "Day 14 is release in a 28-day cycle only. Here both "
                    "cycles happen to be 28 days, which is why the answer "
                    "agrees by accident."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s22",
        "band": "standard",
        "text": "How much longer is the building phase in a 35-day cycle than "
                "in a 21-day cycle?",
        "options": [
            {"text": "About 7 days longer", "correct": False,
             "why": "Half the difference. The whole 14-day difference falls in "
                    "the building phase."},
            {"text": "About 21 days longer", "correct": False,
             "why": "Twenty-one is the whole of the shorter cycle. The "
                    "difference between the two is 14 days."},
            {"text": "It is the same in both", "correct": False,
             "why": "The building phase is the part that stretches. It is the "
                    "closing fortnight that is the same."},
            {"text": "About 14 days longer", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s23",
        "band": "standard",
        "text": "Which two events are about a fortnight apart in every "
                "ordinary cycle?",
        "options": [
            {"text": "The first day of bleeding, and the release of an egg",
             "correct": False,
             "why": "That gap is the stretchy one: about 7 days in a 21-day "
                    "cycle and about 21 in a 35-day one."},
            {"text": "The release of an egg, and the start of the next period",
             "correct": True},
            {"text": "The first day of bleeding, and the end of the bleeding",
             "correct": False,
             "why": "The bleeding lasts roughly five days, not a fortnight."},
            {"text": "The start of the building phase, and the release of an "
                     "egg", "correct": False,
             "why": "That is inside the building phase, so it stretches and "
                    "shrinks with the cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s24",
        "band": "standard",
        "text": "Most cycles end with no fertilised egg arriving. So why is a "
                "lining built every cycle?",
        "options": [
            {"text": "Because it has to be ready in advance — it cannot be "
                     "built once a fertilised egg arrives", "correct": True},
            {"text": "Because building the lining is what triggers an ovary "
                     "into releasing an egg cell that month", "correct": False,
             "why": "The two run alongside each other in two organs. Neither "
                    "sets the other off."},
            {"text": "Because the lining has to be thick enough to bleed",
             "correct": False,
             "why": "The bleeding is what happens when the lining is cleared, "
                    "not something it is built for."},
            {"text": "Because the same lining is built up a little more each "
                     "cycle", "correct": False,
             "why": "Nothing accumulates. A fresh lining is built and cleared "
                    "within each cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s25",
        "band": "standard",
        "text": "One cycle ends and the next begins on the same day. Which day "
                "is that, and what is happening?",
        "options": [
            {"text": "The day of release, when an egg leaves an ovary",
             "correct": False,
             "why": "Release sits in the middle of a cycle rather than at "
                    "either end of it."},
            {"text": "The last day of bleeding, when the lining has all gone",
             "correct": False,
             "why": "Counting starts on the first day of bleeding, not the "
                    "last."},
            {"text": "Day 1, when the lining breaks down", "correct": True},
            {"text": "The day the lining reaches its full thickness",
             "correct": False,
             "why": "That falls around release, a fortnight before the cycle "
                    "ends."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s26",
        "band": "standard",
        "text": "A student says the uterus is “disposing of something” each "
                "period. How would the lesson describe it instead?",
        "options": [
            {"text": "As storing: what is not needed is kept back until the "
                     "next cycle needs it", "correct": False,
             "why": "Nothing is kept back. The lining is cleared and a new one "
                    "is built from the start."},
            {"text": "As resetting: a lining built for a job, held ready, then "
                     "cleared", "correct": True},
            {"text": "As repairing: the uterus mends the damage left by the "
                     "egg that was released", "correct": False,
             "why": "The egg is released from an ovary and never enters the "
                    "uterus, so there is nothing to mend."},
            {"text": "As cleaning: the uterus washes out what has built up "
                     "over the month", "correct": False,
             "why": "What leaves was built on purpose, for a job. It is not "
                    "waste that collected there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s27",
        "band": "standard",
        "text": "Why does the lesson call the building phase the stretchy part "
                "of the cycle?",
        "options": [
            {"text": "Because the lining stretches as it thickens",
             "correct": False,
             "why": "Stretchy describes the TIME the phase takes, not the "
                    "tissue itself."},
            {"text": "Because it is longer in a long cycle and shorter in a "
                     "short one", "correct": True},
            {"text": "Because it can be made longer or shorter to suit a "
                     "calendar", "correct": False,
             "why": "It is not under anyone's control. It simply differs "
                    "between cycles and between people."},
            {"text": "Because it is the only phase that can be missed out "
                     "altogether", "correct": False,
             "why": "It happens in every cycle. Without it there would be no "
                    "lining and no mature egg."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s28",
        "band": "standard",
        "text": "The four events run in a loop. Which event belongs to two "
                "cycles at once?",
        "options": [
            {"text": "Release, which ends one cycle and starts the next",
             "correct": False,
             "why": "Release sits in the middle of a cycle. Nothing starts "
                    "there."},
            {"text": "The holding fortnight, which runs on into the next "
                     "cycle", "correct": False,
             "why": "It ends when the lining breaks down, and that breakdown "
                    "is where the next cycle starts."},
            {"text": "The building phase, which begins before the period is "
                     "over", "correct": False,
             "why": "Building starts once the breakdown is finished, from "
                    "about day 5 of the same cycle."},
            {"text": "The lining breaking down, which is the end of one and "
                     "day 1 of the next", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s29",
        "band": "standard",
        "text": "To work out when someone released an egg, which is more "
                "useful: the length of their last cycle, or of their next?",
        "options": [
            {"text": "The last one, because it is already known", "correct": False,
             "why": "Being known is not the same as being the right one. "
                    "Release is counted back from the END of the cycle it "
                    "belongs to."},
            {"text": "The next one, because release is counted back from its "
                     "end", "correct": True},
            {"text": "The last one, because release always repeats on the same "
                     "day", "correct": False,
             "why": "One person's cycles vary, so the day moves from cycle to "
                    "cycle."},
            {"text": "Neither, because the two are always the same length",
             "correct": False,
             "why": "They very often are not. That variation is the whole "
                    "difficulty."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-s30",
        "band": "standard",
        "text": "An average cycle is about 28 days and a lunar month is about "
                "29.5 days. What does the lesson make of that closeness?",
        "options": [
            {"text": "That the moon sets the length, which is why 28 is the "
                     "usual figure", "correct": False,
             "why": "Nothing in the lesson gives the moon any part in it. The "
                    "closeness is a coincidence."},
            {"text": "That the two numbers are close enough to be treated as "
                     "the same", "correct": False,
             "why": "Treating them as the same is exactly the habit the lesson "
                    "argues against."},
            {"text": "That cycles must once have been 29.5 days and have "
                     "shortened since", "correct": False,
             "why": "No such change is claimed anywhere. Cycles vary between "
                    "people and between months."},
            {"text": "That it is a coincidence which helped 28 keep a grip it "
                     "never earned", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-03-h08",
        "band": "harder",
        "text": "Four recorded cycles measure 27, 29, 26 and 30 days. What is "
                "their mean, and what can it not tell you?",
        "options": [
            {"text": "28 days, and it cannot tell you the length of the next "
                     "cycle", "correct": True},
            {"text": "28 days, and it cannot tell you how long the bleeding "
                     "lasted in any of them", "correct": False,
             "why": "True, but beside the point: the mean is a cycle length, "
                    "and what it fails at is predicting the NEXT one."},
            {"text": "112 days, and it cannot tell you which cycle was which",
             "correct": False,
             "why": "112 is the total. A mean divides that total by the four "
                    "cycles."},
            {"text": "29 days, and it cannot tell you anything useful",
             "correct": False,
             "why": "The four add to 112 and 112 divided by 4 is 28. A mean is "
                    "useful; it is just not a rule about one cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h09",
        "band": "harder",
        "text": "One person's cycles run 24 days and another's 36. How much "
                "longer is the second person's building phase?",
        "options": [
            {"text": "About 6 days, half of the difference between them",
             "correct": False,
             "why": "The difference is not shared out. All of it falls in the "
                    "building phase."},
            {"text": "About 12 days", "correct": True},
            {"text": "About 14 days", "correct": False,
             "why": "The fortnight is the same in both, which is precisely why "
                    "the difference lands elsewhere."},
            {"text": "About 18 days, half of the longer cycle", "correct": False,
             "why": "Halving the cycle is the rule the lesson rejects. The "
                    "difference between 24 and 36 is 12."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h10",
        "band": "harder",
        "text": "A student reasons that because the fortnight after release is "
                "fixed, a 21-day cycle must have a period of only two days. "
                "Evaluate that.",
        "options": [
            {"text": "It is right, and a short cycle always means a short "
                     "period", "correct": False,
             "why": "The bleeding stays at roughly five days whatever the "
                    "cycle length."},
            {"text": "It is wrong: the period stays about five days, and it is "
                     "the building phase that is short", "correct": True},
            {"text": "It is wrong, because the fortnight after release is not "
                     "fixed in the first place", "correct": False,
             "why": "That interval is the steady one. The premise is sound "
                    "even though the conclusion is not."},
            {"text": "It cannot be judged without knowing how thick the lining "
                     "grew", "correct": False,
             "why": "The thickness is not what sets the length of the "
                    "bleeding, and the figures given are enough to answer."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h11",
        "band": "harder",
        "text": "Two people both average 28-day cycles. One varies by a day "
                "either way, the other by six. Whose release day can be "
                "estimated better, and why?",
        "options": [
            {"text": "The second person's, because a wider spread gives more "
                     "cycles to average over", "correct": False,
             "why": "More spread makes an estimate worse, not better. Averages "
                    "do not rescue a number that moves."},
            {"text": "Neither, because release always falls on day 14 in a "
                     "28-day cycle", "correct": False,
             "why": "Neither person has a 28-day cycle every month. That is "
                    "the average, and the average is not a rule."},
            {"text": "The first person's, because the end of the cycle is more "
                     "nearly known in advance", "correct": True},
            {"text": "The first person's, because a short cycle is always "
                     "easier to predict than a long one", "correct": False,
             "why": "Both average 28 days, so neither is the short one. What "
                    "separates them is how much they vary."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h12",
        "band": "harder",
        "text": "Someone describes a person whose cycles run 35 days as "
                "releasing an egg “late”. What is wrong with the word late?",
        "options": [
            {"text": "Nothing is wrong: a 35-day cycle really does release "
                     "later than day 14", "correct": False,
             "why": "Later in the count, yes. But late means behind schedule, "
                    "and there is no schedule to be behind."},
            {"text": "It is wrong because release in a 35-day cycle actually "
                     "falls earlier, around day 7", "correct": False,
             "why": "Day 7 belongs to a 21-day cycle. In a 35-day cycle "
                    "release falls around day 21."},
            {"text": "Release is a fortnight before that cycle's own end, so "
                     "it is on time for it", "correct": True},
            {"text": "It is wrong because nobody can say when release happens "
                     "at all, early or late", "correct": False,
             "why": "It can be estimated closely by counting back from the "
                    "next period. The pattern is not random."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h13",
        "band": "harder",
        "text": "Which of these is the same kind of mistake as treating 28 "
                "days as everybody's cycle length?",
        "options": [
            {"text": "Saying that a coin landed heads because it had landed "
                     "tails the time before", "correct": False,
             "why": "That is a mistake about chance rather than about "
                    "averages. Nothing here is an average being misread."},
            {"text": "Saying that the average family has 1.7 children, so some "
                     "family somewhere has 1.7 children", "correct": True},
            {"text": "Saying that a measurement is wrong because it disagrees "
                     "with what was expected", "correct": False,
             "why": "That is about trusting evidence. The error here is "
                    "reading an average as a rule about individuals."},
            {"text": "Saying that two things which happen together must cause "
                     "each other", "correct": False,
             "why": "A real mistake, and a different one. It is about cause "
                    "rather than about averages."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h14",
        "band": "harder",
        "text": "Daily temperature records, hormone tests and app data from "
                "millions of users all gave the same picture. Why does using "
                "three different methods matter?",
        "options": [
            {"text": "Because three methods take three times as many "
                     "measurements as one would", "correct": False,
             "why": "It is agreement that counts, not the total. Three methods "
                    "with one weakness between them would add nothing."},
            {"text": "Because agreement between different methods makes the "
                     "finding harder to explain away", "correct": True},
            {"text": "Because a result only counts as evidence once three "
                     "methods have been tried", "correct": False,
             "why": "No such rule exists. One good method can be convincing; "
                    "several agreeing are more so."},
            {"text": "Because the average of three methods is closer to the "
                     "truth than any single one", "correct": False,
             "why": "The methods are not averaged together. They are compared, "
                    "and they point the same way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h15",
        "band": "harder",
        "text": "In a 28-day cycle, the lining is found thick and being held "
                "ready. Roughly which days of the cycle could it be?",
        "options": [
            {"text": "Days 1 to 5", "correct": False,
             "why": "Those are the days the old lining is breaking down, which "
                    "is the opposite of being held ready."},
            {"text": "Days 5 to 14", "correct": False,
             "why": "That is the building phase. The lining is thickening "
                    "then, and only reaches full thickness at the end of it."},
            {"text": "Days 14 to 28", "correct": True},
            {"text": "Any day of the cycle", "correct": False,
             "why": "For the first fortnight the lining is either breaking "
                    "down or still being built."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h16",
        "band": "harder",
        "text": "Suppose the interval after release varied as much as the "
                "building phase does. What would happen to the counting rule?",
        "options": [
            {"text": "It would still work, because the cycle length would be "
                     "unchanged", "correct": False,
             "why": "The rule does not use the cycle length on its own. It "
                    "needs one interval inside the cycle to hold still."},
            {"text": "It would work better, because both halves would then "
                     "vary together", "correct": False,
             "why": "Two varying intervals give nothing to count back from. "
                    "The rule needs one of them fixed."},
            {"text": "It would only work for cycles shorter than 28 days",
             "correct": False,
             "why": "Length is not what the rule depends on. It depends on one "
                    "interval being close to the same in everyone."},
            {"text": "It would stop working: there would be nothing steady to "
                     "count back from", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h17",
        "band": "harder",
        "text": "A 35-day cycle and a 21-day cycle both have a five-day "
                "period. Compare the days between the end of the period and "
                "release in each.",
        "options": [
            {"text": "About 16 days against about 2 days", "correct": True},
            {"text": "About 9 days against about 9 days, since the period is "
                     "the same length in both", "correct": False,
             "why": "The period being equal does not make the building phase "
                    "equal. One cycle has 14 more days to fit in."},
            {"text": "About 30 days against about 16 days, counting from day 1 "
                     "rather than from the end of the period", "correct": False,
             "why": "These are whole-cycle figures, and they leave the closing "
                    "fortnight in as well."},
            {"text": "About 21 days against 7 days", "correct": False,
             "why": "Those are the days release falls ON. The five days of "
                    "bleeding still have to be taken off."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h18",
        "band": "harder",
        "text": "Bleeding began on 1 March and again on 27 March. How long was "
                "that cycle, and what else would be needed to say when the "
                "next release will be?",
        "options": [
            {"text": "27 days, and nothing else — release will be on day 13 "
                     "next month too", "correct": False,
             "why": "1 March to 27 March is 26 days, and one person's cycles "
                    "vary, so next month's length is not known."},
            {"text": "26 days, and nothing else — release is always 14 days "
                     "after day 1", "correct": False,
             "why": "The fortnight belongs at the END of a cycle. Counting it "
                    "forwards from day 1 is the error the lesson exists to "
                    "correct."},
            {"text": "28 days, and the length of the period",
             "correct": False,
             "why": "The dates give 26 days, and how long the bleeding lasts "
                    "does not move release."},
            {"text": "26 days, and the length of the NEXT cycle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h19",
        "band": "harder",
        "text": "In a 28-day cycle the lining stays at full thickness for "
                "about a fortnight. What fraction of the cycle is that?",
        "options": [
            {"text": "About a quarter", "correct": False,
             "why": "A quarter of 28 days is 7. The holding runs for about "
                    "twice that."},
            {"text": "About a fifth", "correct": False,
             "why": "A fifth of 28 days is under 6, which is closer to the "
                    "length of the period."},
            {"text": "About a third", "correct": False,
             "why": "A third of 28 days is about 9. Fourteen out of 28 is a "
                    "larger share than that."},
            {"text": "About a half", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h20",
        "band": "harder",
        "text": "Suppose day 1 were counted from the day of release instead of "
                "from the first day of bleeding. What would change?",
        "options": [
            {"text": "The events would happen in a completely different "
                     "order, with the period first and the release of an egg "
                     "last", "correct": False,
             "why": "Renumbering the days changes no event and no order. The "
                    "loop is the same loop."},
            {"text": "Nothing, since release and bleeding happen on the same "
                     "day", "correct": False,
             "why": "They are about a fortnight apart, which is why the choice "
                    "of marker matters."},
            {"text": "The numbering would change, but the events and their "
                     "spacing would not — and release cannot be seen",
             "correct": True},
            {"text": "The cycle would become the same length for everybody, "
                     "because release is fixed", "correct": False,
             "why": "Release is not fixed: it moves with the length of the "
                    "cycle. Renumbering cannot make cycles equal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h21",
        "band": "harder",
        "text": "Which finding would most weaken the claim that release falls "
                "about a fortnight before the next period?",
        "options": [
            {"text": "Finding that cycle lengths vary widely between people",
             "correct": False,
             "why": "The claim already allows for that. It is exactly why the "
                    "counting runs backwards."},
            {"text": "Finding that the gap from release to the next period "
                     "varied widely between cycles", "correct": True},
            {"text": "Finding that some people's cycles are shorter than 21 "
                     "days", "correct": False,
             "why": "An unusual length still has a fortnight at the end of it, "
                    "so far as this claim goes."},
            {"text": "Finding that the bleeding lasts a different number of "
                     "days in different people", "correct": False,
             "why": "The claim says nothing about how long the bleeding lasts. "
                    "It is about the other end of the cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h22",
        "band": "harder",
        "text": "A poster says “the egg is released on day 14”. Give the two "
                "separate reasons the lesson would object.",
        "options": [
            {"text": "Day 14 is an average, and the average is taken from too "
                     "few people to be reliable", "correct": False,
             "why": "The sample is not the problem — app data covers millions. "
                    "The problem is reading an average as a rule."},
            {"text": "28 days is an average rather than a rule, and one "
                     "person's own cycles vary as well", "correct": True},
            {"text": "Release cannot be predicted at all, and day 14 is in any "
                     "case in the wrong half of the cycle", "correct": False,
             "why": "It can be estimated by counting back, and day 14 is "
                    "genuinely right for a 28-day cycle."},
            {"text": "The lining is not ready by day 14, and the egg needs "
                     "longer than that to mature", "correct": False,
             "why": "In a 28-day cycle both are ready by then. The objection "
                    "is about other cycle lengths, not about timing within "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h23",
        "band": "harder",
        "text": "Two organs are running at once through the cycle. Which "
                "single event ties their timings together?",
        "options": [
            {"text": "The period, because the lining breaks down and an egg "
                     "cell is released on the same day", "correct": False,
             "why": "Those two are about a fortnight apart. Nothing is "
                    "released during the bleeding."},
            {"text": "Release, which happens about a fortnight before the "
                     "lining is cleared", "correct": True},
            {"text": "The start of building, because the lining and the egg "
                     "cell both finish on day 5", "correct": False,
             "why": "Day 5 is roughly where building BEGINS, and the egg "
                    "finishes maturing much later."},
            {"text": "Implantation, which is the only event the two organs "
                     "share", "correct": False,
             "why": "Implantation happens in most cycles not at all. The event "
                    "that ties the timings in every cycle is release."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h24",
        "band": "harder",
        "text": "A researcher has only a calendar of recorded bleeding dates. "
                "What is the best they can do about release days, and what is "
                "the limitation?",
        "options": [
            {"text": "Mark day 14 of each cycle; the limitation is that the "
                     "bleeding dates may be wrong", "correct": False,
             "why": "The dates are the reliable part. Day 14 is the assumption "
                    "that fails."},
            {"text": "Count back a fortnight from each period that has already "
                     "happened; it cannot be done in advance", "correct": True},
            {"text": "Count forward a fortnight from each day 1; the "
                     "limitation is that some cycles have no release",
             "correct": False,
             "why": "The fortnight belongs at the end of the cycle, and "
                    "counting it forwards is the error."},
            {"text": "Nothing; a calendar of dates carries no information "
                     "about release", "correct": False,
             "why": "It carries a good deal, once the counting runs backwards. "
                    "What it cannot do is look ahead."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h25",
        "band": "harder",
        "text": "Two cycles are recorded, one of 22 days and one of 40 days. "
                "Which falls outside the ordinary range, and by roughly how "
                "much?",
        "options": [
            {"text": "The 22-day cycle, by about 6 days", "correct": False,
             "why": "About 21 days is the short end of the ordinary range, so "
                    "22 days sits just inside it."},
            {"text": "Both of them, by about 1 day and about 5 days",
             "correct": False,
             "why": "Only one is outside. Twenty-two days is within about 21 "
                    "to 35."},
            {"text": "The 40-day cycle, by about 5 days", "correct": True},
            {"text": "Neither of them, since any length at all is ordinary",
             "correct": False,
             "why": "About 21 to 35 days is the ordinary range. Forty days is "
                    "beyond its upper end."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h26",
        "band": "harder",
        "text": "A poster draws the cycle as a clock face with day 1 at the "
                "top and release at the bottom. Is that drawing fair for a "
                "35-day cycle?",
        "options": [
            {"text": "Yes, because release is always halfway round whatever "
                     "the length", "correct": False,
             "why": "Halfway is the rule the lesson rejects. Release is a "
                    "fortnight from the end, not half way from the start."},
            {"text": "Yes, because a circle has no fixed lengths on it anyway",
             "correct": False,
             "why": "Putting release opposite day 1 is a claim about where it "
                    "falls, circle or not."},
            {"text": "No, because release in a 35-day cycle falls about two "
                     "thirds of the way round", "correct": True},
            {"text": "No, because a cycle should never be drawn as a circle at "
                     "all", "correct": False,
             "why": "A circle is a fair shape for it: the cycle ends where it "
                    "starts. It is the position of the marker that is wrong."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h27",
        "band": "harder",
        "text": "Why can the boundaries between the phases of the cycle not be "
                "written down as fixed day numbers?",
        "options": [
            {"text": "Because nobody has yet measured them accurately enough "
                     "to write down", "correct": False,
             "why": "They have been measured a great deal. The trouble is that "
                    "they genuinely move."},
            {"text": "Because release is worked out from the length of that "
                     "cycle, so the boundaries move with it", "correct": True},
            {"text": "Because the phases overlap, so no boundary between them "
                     "exists", "correct": False,
             "why": "Each phase does follow the one before it. What moves is "
                    "where the joins fall."},
            {"text": "Because the boundaries depend on how long the bleeding "
                     "lasted that month", "correct": False,
             "why": "The bleeding stays at roughly five days. It is the cycle "
                    "length that moves everything else."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h28",
        "band": "harder",
        "text": "Someone's last three cycles were 25, 26 and 25 days. Their "
                "next period arrives 34 days after the last one began. What "
                "can be said about release in that cycle?",
        "options": [
            {"text": "It happened about day 20, later in the count than in "
                     "their other cycles", "correct": True},
            {"text": "It happened about day 11, as it did in the three cycles "
                     "before it", "correct": False,
             "why": "Day 11 belongs to a 25-day cycle. This one ran 34 days, "
                    "so counting back a fortnight lands much later."},
            {"text": "It did not happen at all, because the cycle ran longer "
                     "than usual", "correct": False,
             "why": "Nothing in a longer cycle stops release. The building "
                    "phase simply took longer."},
            {"text": "It happened about day 17, halfway through the 34 days",
             "correct": False,
             "why": "Halfway is the wrong rule. Counting back a fortnight from "
                    "day 34 gives about day 20."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h29",
        "band": "harder",
        "text": "One study followed twenty people and another used app data "
                "from millions. Why is the second the stronger evidence about "
                "how cycle lengths are spread?",
        "options": [
            {"text": "Because app data is collected by machine, so it cannot "
                     "contain any mistakes", "correct": False,
             "why": "It can contain plenty — entries are typed in by people. "
                    "Its strength is the number of them."},
            {"text": "Because a much larger sample shows the spread far more "
                     "reliably", "correct": True},
            {"text": "Because twenty people is too few for an average to be "
                     "worked out", "correct": False,
             "why": "An average of twenty is easy to work out. What is hard is "
                    "trusting it as a picture of everybody."},
            {"text": "Because the larger study is more recent",
             "correct": False,
             "why": "When a study was done says nothing about how good it is. "
                    "The sample size is what is doing the work."},
        ],
        "figure": None,
    },
    {
        "id": "b5-03-h30",
        "band": "harder",
        "text": "In a 35-day cycle, rank these by length: the period, the "
                "building phase, and the fortnight after release.",
        "options": [
            {"text": "The fortnight, then the building phase, then the period",
             "correct": False,
             "why": "The building phase in a 35-day cycle runs about 16 days, "
                    "which is longer than the fortnight."},
            {"text": "All three are about the same length in a 35-day cycle",
             "correct": False,
             "why": "Roughly 16, 14 and 5 days. Two are close; the period is "
                    "nothing like them."},
            {"text": "The period, then the building phase, then the fortnight",
             "correct": False,
             "why": "The period is roughly five days, the shortest of the "
                    "three by a long way."},
            {"text": "The building phase, then the fortnight, then the period",
             "correct": True},
        ],
        "figure": None,
    },
]
