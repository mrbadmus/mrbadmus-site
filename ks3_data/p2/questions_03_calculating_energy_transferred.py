"""P2 lesson 03 — Calculating energy transferred: twelve questions (MRB-223).

Written against Design's page. The five appliances, the shower-and-lamp
hook, the two legal unit pairings and the Convert-line habit are hers.

The discriminations:

  · `E = P × t` is a product, and the operation is multiplication;
  · the time is in SECONDS, because a watt is a joule each second
    (`ENER-23`) — this is the lesson's whole misconception and it runs
    through every band;
  · a joule is TINY, which is the check that catches the first error before
    the marking does (`ENER-24`);
  · watts-with-seconds and kilowatts-with-hours are the only two legal
    pairings, and mixing them is a factor of 3600 rather than a small slip.

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 (the 1200 W microwave for 90 s) and Rung 2 (2000 × 3 = 6000 J)
are NOT restated here; check 6 of `verify_questions.py` forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P2"
LESSON = "calculating-energy-transferred"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p2-03-e01",
        "band": "easier",
        "text": "Which formula gives the energy an appliance transfers?",
        "options": [
            {"text": "energy = power ÷ time", "correct": False,
             "why": "Running for longer transfers MORE energy, and dividing "
                    "by a bigger time would give less."},
            {"text": "energy = power × time", "correct": True},
            {"text": "energy = power + time", "correct": False,
             "why": "You cannot add watts to seconds — they are "
                    "different quantities."},
            {"text": "energy = time ÷ power", "correct": False,
             "why": "That would make a low-power appliance transfer more, "
                    "which is backwards."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e02",
        "band": "easier",
        "text": "A 40 W fan runs for 200 seconds. How much energy does it "
                "transfer?",
        "options": [
            {"text": "240 J", "correct": False,
             "why": "That is 40 + 200. The two quantities multiply."},
            {"text": "5 J", "correct": False,
             "why": "That is 200 ÷ 40, the division the wrong way round."},
            {"text": "8000 J", "correct": True},
            {"text": "0.2 J", "correct": False,
             "why": "That is 40 ÷ 200. Longer running means more energy, "
                    "not less."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e03",
        "band": "easier",
        "text": "Before using E = P × t with a power in watts, what "
                "must the time be in?",
        "options": [
            {"text": "Minutes", "correct": False,
             "why": "This is the slip the lesson is built on. Using minutes "
                    "makes the answer sixty times too small."},
            {"text": "Hours", "correct": False,
             "why": "Hours pair with KILOWATTS, not with watts. Mixing them "
                    "is out by 3600."},
            {"text": "Whatever unit the question gives", "correct": False,
             "why": "The formula does not adapt to the question. The "
                    "question has to be converted to suit the formula."},
            {"text": "Seconds", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e04",
        "band": "easier",
        "text": "Roughly how much energy does lifting an apple from the "
                "floor to a table take?",
        "options": [
            {"text": "About 1 joule", "correct": True},
            {"text": "About 1000 joules", "correct": False,
             "why": "A thousand joules is far more — closer to what a "
                    "small torch uses over several minutes."},
            {"text": "About 100 000 joules", "correct": False,
             "why": "That is getting on for a third of what it takes to boil "
                    "a mugful of water."},
            {"text": "About 0.001 joules", "correct": False,
             "why": "That is a thousand times too small — a joule is "
                    "already a very small amount."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p2-03-s01",
        "band": "standard",
        "text": "A 1500 W hairdryer runs for 4 minutes. How much energy does "
                "it transfer?",
        "options": [
            {"text": "6000 J", "correct": False,
             "why": "That is 1500 × 4, with the time left in minutes. "
                    "Convert to 240 s first."},
            {"text": "360 000 J", "correct": True},
            {"text": "375 J", "correct": False,
             "why": "That is 1500 ÷ 4. The two quantities multiply."},
            {"text": "6 000 000 J", "correct": False,
             "why": "That looks like 1500 × 4000. Four minutes is 240 "
                    "seconds, not 4000."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s02",
        "band": "standard",
        "text": "A student calculates that a kettle boiling a litre of water "
                "transfers 4000 J. Before checking any arithmetic, what "
                "should make them suspicious?",
        "options": [
            {"text": "The answer is too large — a kettle would not need "
                     "thousands of joules",
             "correct": False,
             "why": "It is the other way round. A kettle needs hundreds of "
                    "thousands."},
            {"text": "The units are wrong; energy should be in watts",
             "correct": False,
             "why": "Watts are power. Joules are the right unit for energy."},
            {"text": "The answer is far too small for the job it describes",
             "correct": True},
            {"text": "Nothing — 4000 J is a reasonable size",
             "correct": False,
             "why": "It is roughly the energy in a mouthful of bread, and "
                    "could not boil a litre of anything."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s03",
        "band": "standard",
        "text": "Which pairing of units is legal?",
        "options": [
            {"text": "Watts with minutes", "correct": False,
             "why": "The one combination the lesson names as always wrong. "
                    "A watt is defined per second."},
            {"text": "Kilowatts with seconds", "correct": False,
             "why": "This is not one of the two standard pairings; it would "
                    "give kilojoules, and mixing it up with kWh is the usual "
                    "next mistake."},
            {"text": "Watts with hours", "correct": False,
             "why": "Hours go with kilowatts. Watts go with seconds."},
            {"text": "Kilowatts with hours", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s04",
        "band": "standard",
        "text": "Where in the working is the safest place to convert a time "
                "from minutes into seconds?",
        "options": [
            {"text": "On the Convert line, before anything is multiplied",
             "correct": True},
            {"text": "At the very end, on the answer", "correct": False,
             "why": "By then the wrong number has already been multiplied in, "
                    "and dividing the answer by 60 will not undo it "
                    "reliably."},
            {"text": "It does not matter where, as long as it happens",
             "correct": False,
             "why": "It matters a great deal: converting late is how the "
                    "×60 error survives to the end of a page of "
                    "working."},
            {"text": "It should not be converted — write the minutes and "
                     "note the unit",
             "correct": False,
             "why": "The formula takes seconds. A note beside a wrong number "
                    "does not make it the right number."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p2-03-h01",
        "band": "harder",
        "text": "A 90 W fridge motor runs in bursts, about 12 hours a "
                "day in total. A 2000 W kettle runs 3 minutes a day. "
                "Which uses more energy in a day, and why?",
        "options": [
            {"text": "The kettle, because its rating is over twenty times "
                     "higher",
             "correct": False,
             "why": "The kettle gives 2.0 × 0.05 = 0.10 kWh. The fridge "
                    "gives 0.09 × 12 = 1.08 kWh, and wins."},
            {"text": "The fridge, because 12 hours outweighs the higher "
                     "rating",
             "correct": True},
            {"text": "The kettle, because a fridge cools rather than heats",
             "correct": False,
             "why": "A fridge still draws power to run its compressor, and "
                    "what it does with the energy does not change the "
                    "total."},
            {"text": "They are the same, at about 0.10 kWh each",
             "correct": False,
             "why": "The kettle is 0.10 kWh; the fridge is 1.08 kWh. They "
                    "are not equal."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h02",
        "band": "harder",
        "text": "An 8500 W shower for 10 minutes and a 60 W lamp for 24 "
                "hours turn out to transfer almost the same energy. What "
                "does this show about power ratings?",
        "options": [
            {"text": "That ratings are unreliable, so the number printed on "
                     "the label should not be trusted",
             "correct": False,
             "why": "The ratings are perfectly accurate. They simply answer a "
                    "different question from the one about the bill."},
            {"text": "That the lamp must be faulty, because nothing rated "
                     "that small should match a shower",
             "correct": False,
             "why": "The lamp draws exactly its 60 W. It is the 86 400 "
                    "seconds that does the work."},
            {"text": "That a rating cannot tell you the energy without the "
                     "time, however large the difference in rating",
             "correct": True},
            {"text": "That small appliances are generally more wasteful with "
                     "energy than large ones ever are",
             "correct": False,
             "why": "Neither is wasteful here. The comparison is about "
                    "duration, not about waste."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h03",
        "band": "harder",
        "text": "The Mars Climate Orbiter was lost in 1999 because one team "
                "supplied thrust in pound-force seconds and the software "
                "expected newton seconds. What does that failure have in "
                "common with writing 2000 × 3 = 6000 J?",
        "options": [
            {"text": "Both were arithmetic errors that a careful check on a "
                     "calculator would have caught",
             "correct": False,
             "why": "Neither was an arithmetic error. Every multiplication in "
                    "both cases was performed correctly."},
            {"text": "Both involved numbers that were far too large to be "
                     "checked over by hand at all",
             "correct": False,
             "why": "2000 × 3 is easy to check. Size was not the problem in "
                    "either case."},
            {"text": "Both came from software making a mistake rather than "
                     "from the people involved",
             "correct": False,
             "why": "The orbiter's error came from two teams' conventions, "
                    "and the kettle's from a student. Neither is a software "
                    "fault."},
            {"text": "In both, every number was right in its own units and "
                     "the units were never reconciled",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h04",
        "band": "harder",
        "text": "A student writes: “2.2 kW × 45 min = 99, so the "
                "oven uses 99 kWh.” Two things are wrong. Which pair?",
        "options": [
            {"text": "The time must be in hours, and the answer should be "
                     "1.65 kWh",
             "correct": True},
            {"text": "The power must be in watts, and the answer should be "
                     "99 000 J",
             "correct": False,
             "why": "Kilowatts are fine — they are one half of a legal "
                    "pairing. It is the minutes that break it, and the unit "
                    "of the answer is then kWh, not J."},
            {"text": "The operation should be division, and the answer "
                     "should be 0.049 kWh",
             "correct": False,
             "why": "Energy is power multiplied by time. The operation was "
                    "the one thing that was right."},
            {"text": "The time must be in seconds, and the answer should be "
                     "5940 kWh",
             "correct": False,
             "why": "Seconds pair with WATTS. With kilowatts the time goes "
                    "in hours, and 5940 kWh would be more than a house uses "
                    "in a year."},
        ],
        "figure": None,
    },
]
