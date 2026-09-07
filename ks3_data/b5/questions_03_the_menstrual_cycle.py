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
]
