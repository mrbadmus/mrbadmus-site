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
                    "a full litre of water."},
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
             "why": "It is about what it takes to carry yourself up two "
                    "flights of stairs, and could not boil a litre of "
                    "anything."},
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p2-03-e05",
        "band": "easier",
        "text": "A 60 W lamp runs for 300 seconds. How much energy does it "
                "transfer?",
        "options": [
            {"text": "18 000 J", "correct": True},
            {"text": "5 J", "correct": False,
             "why": "That is 300 ÷ 60, the division upside down as well as "
                    "the wrong operation."},
            {"text": "0.2 J", "correct": False,
             "why": "That is 60 ÷ 300. E = P × t is a multiplication."},
            {"text": "360 J", "correct": False,
             "why": "That is 60 + 300, and a power and a time cannot be "
                    "added."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e06",
        "band": "easier",
        "text": "In E = P × t, what does the P stand for?",
        "options": [
            {"text": "The pressure, in pascals", "correct": False,
             "why": "Pressure has nothing to do with an appliance's energy "
                    "transfer."},
            {"text": "The power, in watts", "correct": True},
            {"text": "The price per unit, in pence", "correct": False,
             "why": "Price appears on a bill, not in this formula."},
            {"text": "The period the appliance runs for", "correct": False,
             "why": "That is the t. The P is the rate the appliance "
                    "transfers at."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e07",
        "band": "easier",
        "text": "How many seconds are there in 4 minutes?",
        "options": [
            {"text": "400 s", "correct": False,
             "why": "That multiplies by 100. A minute is 60 seconds, not "
                    "100."},
            {"text": "64 s", "correct": False,
             "why": "That adds 60 to 4 rather than multiplying by it."},
            {"text": "240 s", "correct": True},
            {"text": "0.067 s", "correct": False,
             "why": "That is 4 ÷ 60, the conversion the wrong way round — "
                    "minutes are bigger than seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e08",
        "band": "easier",
        "text": "A 500 W drill transfers 30 000 J. How long did it run for?",
        "options": [
            {"text": "60 s", "correct": True},
            {"text": "15 000 000 s", "correct": False,
             "why": "That multiplies the two. To find a time you divide the "
                    "energy by the power."},
            {"text": "0.017 s", "correct": False,
             "why": "That is 500 ÷ 30 000, the division the wrong way round."},
            {"text": "29 500 s", "correct": False,
             "why": "That subtracts, and a power cannot be taken away from an "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e09",
        "band": "easier",
        "text": "Which of these is an amount of ENERGY?",
        "options": [
            {"text": "8500 watts", "correct": False,
             "why": "Watts are a rate — joules per second — not an amount."},
            {"text": "600 seconds", "correct": False,
             "why": "Seconds are a time. An energy needs a power multiplied "
                    "by one."},
            {"text": "27 pence per unit", "correct": False,
             "why": "That is a price. It is what an amount of energy is "
                    "charged at, not the energy itself."},
            {"text": "5 100 000 joules", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e10",
        "band": "easier",
        "text": "A 2000 W kettle runs for 90 seconds. How much energy does it "
                "transfer?",
        "options": [
            {"text": "180 000 J", "correct": True},
            {"text": "22 J", "correct": False,
             "why": "That is 2000 ÷ 90, a division where the formula "
                    "multiplies."},
            {"text": "2090 J", "correct": False,
             "why": "That adds the power to the time, which cannot be done."},
            {"text": "3000 J", "correct": False,
             "why": "That uses 1.5 minutes as though it were 1.5 seconds; the "
                    "time must be in seconds."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p2-03-s05",
        "band": "standard",
        "text": "A 750 W blender runs for 2 minutes. How much energy does it "
                "transfer?",
        "options": [
            {"text": "1500 J", "correct": False,
             "why": "That is 750 × 2, with the minutes going into the formula "
                    "as they stand."},
            {"text": "90 000 J", "correct": True},
            {"text": "375 J", "correct": False,
             "why": "That is 750 ÷ 2, a division where a multiplication is "
                    "needed."},
            {"text": "45 000 J", "correct": False,
             "why": "That uses 60 s instead of 120 s — one minute rather than "
                    "two."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s06",
        "band": "standard",
        "text": "An 8500 W shower runs for 6 minutes. How much energy does it "
                "transfer?",
        "options": [
            {"text": "51 000 J", "correct": False,
             "why": "That is 8500 × 6, with the minutes not converted into "
                    "seconds."},
            {"text": "1417 J", "correct": False,
             "why": "That is 8500 ÷ 6, a division where the formula "
                    "multiplies."},
            {"text": "3 060 000 J", "correct": True},
            {"text": "510 000 J", "correct": False,
             "why": "That uses 60 s rather than 360 s, so it is a one-minute "
                    "shower."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s07",
        "band": "standard",
        "text": "A student's answer for boiling a full kettle comes out at "
                "600 J. What should they notice before checking the "
                "arithmetic?",
        "options": [
            {"text": "That the answer is far too small for boiling water",
             "correct": True},
            {"text": "That the answer should have been in watts",
             "correct": False,
             "why": "An energy is properly in joules; the unit is not what is "
                    "wrong here."},
            {"text": "That the answer is far too large for a kettle",
             "correct": False,
             "why": "Boiling a kettle takes hundreds of thousands of joules, "
                    "so 600 J is much too small."},
            {"text": "That a kettle's energy cannot be calculated at all",
             "correct": False,
             "why": "E = P × t handles it perfectly well once the time is in "
                    "seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s08",
        "band": "standard",
        "text": "A 1200 W iron transfers 432 000 J. How long was it on?",
        "options": [
            {"text": "360 s", "correct": True},
            {"text": "6 s", "correct": False,
             "why": "That is 360 seconds read as though it were minutes "
                    "without saying so — and 6 s cannot iron anything."},
            {"text": "518 400 000 s", "correct": False,
             "why": "That multiplies where a division is needed."},
            {"text": "0.0028 s", "correct": False,
             "why": "That is 1200 ÷ 432 000, the division the wrong way "
                    "round."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s09",
        "band": "standard",
        "text": "Which pairing of units gives an energy directly?",
        "options": [
            {"text": "Watts multiplied by minutes", "correct": False,
             "why": "The minutes have to become seconds first, or the answer "
                    "is sixty times too small."},
            {"text": "Kilowatts multiplied by seconds", "correct": False,
             "why": "Mixing the kilo with seconds gives kilojoules, not the "
                    "joules or kWh a question usually wants."},
            {"text": "Kilowatts multiplied by hours", "correct": True},
            {"text": "Watts multiplied by hours", "correct": False,
             "why": "That gives watt-hours, which is a real unit but not one "
                    "a bill or a formula uses."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s10",
        "band": "standard",
        "text": "A 9 W lamp is left on for 5 hours. How much energy does it "
                "transfer, in joules?",
        "options": [
            {"text": "45 J", "correct": False,
             "why": "That is 9 × 5, with the hours put in as they stand."},
            {"text": "2700 J", "correct": False,
             "why": "That uses 300 seconds — five minutes rather than five "
                    "hours."},
            {"text": "162 000 J", "correct": True},
            {"text": "0.045 J", "correct": False,
             "why": "That divides by 1000 as well, treating the watts as "
                    "though they were kilowatts."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p2-03-h05",
        "band": "harder",
        "text": "A 2.5 kW heater runs for 40 minutes. How much energy does it "
                "transfer, in joules?",
        "options": [
            {"text": "100 J", "correct": False,
             "why": "That is 2.5 × 40, with neither the kilowatts nor the "
                    "minutes converted."},
            {"text": "100 000 J", "correct": False,
             "why": "That converts the kilowatts but leaves the time in "
                    "minutes."},
            {"text": "6 000 000 J", "correct": True},
            {"text": "6000 J", "correct": False,
             "why": "That converts the minutes but leaves the power in "
                    "kilowatts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h06",
        "band": "harder",
        "text": "A 100 W lamp on for 10 hours and a 2000 W kettle on for "
                "30 minutes: which transfers more, and by how much?",
        "options": [
            {"text": "The kettle, because 2000 W is twenty times the lamp's "
                     "rating",
             "correct": False,
             "why": "Twenty times the rate, but for a twentieth of the time, "
                    "so the two totals come out the same."},
            {"text": "The lamp, because it is on for twenty times as long",
             "correct": False,
             "why": "Twenty times as long at a twentieth of the rate gives "
                    "exactly the same total."},
            {"text": "They are almost equal, at about 3.6 MJ each",
             "correct": True},
            {"text": "The lamp, at 1000 J against the kettle's 60 000 J",
             "correct": False,
             "why": "Both figures leave the time in hours and minutes rather "
                    "than converting to seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h07",
        "band": "harder",
        "text": "A student writes 2.2 kW × 45 min = 99 kWh for an oven. Which "
                "pair of things is wrong?",
        "options": [
            {"text": "The power should be in watts, and the answer should be "
                     "in joules",
             "correct": False,
             "why": "Kilowatts with hours is a legal pairing; it is the "
                    "minutes and the size of the answer that fail."},
            {"text": "The time is in minutes, and 99 kWh is far too large for "
                     "one oven use",
             "correct": True},
            {"text": "The time is in minutes, and the answer should be in "
                     "kilowatts",
             "correct": False,
             "why": "The time is indeed wrong, but kWh is the right unit for "
                    "an energy — kW would be a power."},
            {"text": "The power should be 22 kW, and the time should be in "
                     "seconds",
             "correct": False,
             "why": "2.2 kW is an ordinary oven rating, and kWh needs hours "
                    "rather than seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h08",
        "band": "harder",
        "text": "A 90 W fridge motor runs for a total of 12 hours a day. A "
                "2200 W oven runs 30 minutes a day. Which transfers more in a "
                "day?",
        "options": [
            {"text": "The oven, by a wide margin, at 1.1 kWh against "
                     "0.045 kWh",
             "correct": False,
             "why": "0.045 kWh is the fridge for half an hour. Over 12 hours "
                    "it reaches 1.08 kWh."},
            {"text": "The oven, because 2200 W dwarfs 90 W", "correct": False,
             "why": "The rating dwarfs it, but the fridge runs for "
                    "twenty-four times as long."},
            {"text": "They are within a few per cent of each other, at about "
                     "1.1 kWh each",
             "correct": True},
            {"text": "The fridge, at 10.8 kWh against 1.1 kWh",
             "correct": False,
             "why": "That is ten times too big: 90 W is 0.09 kW, and "
                    "0.09 × 12 is 1.08."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h09",
        "band": "harder",
        "text": "Why is converting the time written on the Insert line rather "
                "than done at the end?",
        "options": [
            {"text": "Because the formula only works with whole numbers of "
                     "seconds",
             "correct": False,
             "why": "It works with any time in seconds, whole or not. The "
                    "reason is about where the mistake hides."},
            {"text": "Because doing it at the end changes which formula is "
                     "used",
             "correct": False,
             "why": "The formula is the same either way; what changes is "
                    "whether the slip is visible."},
            {"text": "Because a conversion on the line can be checked and "
                     "a mental one cannot",
             "correct": True},
            {"text": "Because the answer would otherwise be in the wrong unit "
                     "of energy",
             "correct": False,
             "why": "The unit comes out as joules either way; the number is "
                    "what goes wrong."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h10",
        "band": "harder",
        "text": "One kilowatt-hour is how many joules?",
        "options": [
            {"text": "1000 J", "correct": False,
             "why": "That is one kilojoule. A kilowatt-hour runs for an hour, "
                    "so the seconds must be counted in."},
            {"text": "3 600 000 J", "correct": True},
            {"text": "3600 J", "correct": False,
             "why": "That is one watt for an hour. A kilowatt is a thousand "
                    "times larger."},
            {"text": "60 000 J", "correct": False,
             "why": "That uses 60 seconds rather than the 3600 seconds in an "
                    "hour."},
        ],
        "figure": None,
    },
]
