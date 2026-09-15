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
            {"text": "The oven, by a wide margin, at 1.1 kWh against just "
                     "0.045 kWh",
             "correct": False,
             "why": "0.045 kWh is the fridge for half an hour. Over 12 hours "
                    "it reaches 1.08 kWh."},
            {"text": "The oven, because 2200 W dwarfs 90 W", "correct": False,
             "why": "The rating dwarfs it, but the fridge runs for "
                    "twenty-four times as long."},
            {"text": "They are within a few per cent, at about 1.1 kWh each",
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

    # ── MRB-338 night 3 top-up · easier ──────────────────────────────────
    {
        "id": "p2-03-e11",
        "band": "easier",
        "text": "How many seconds are there in one hour?",
        "options": [
            {"text": "60", "correct": False,
             "why": "That is the number in one minute. An hour holds sixty of "
                    "those."},
            {"text": "600", "correct": False,
             "why": "That is ten minutes' worth, which is six times short of "
                    "an hour."},
            {"text": "3600", "correct": True},
            {"text": "1000", "correct": False,
             "why": "Time is not counted in thousands; the step from minutes "
                    "to hours is sixty."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e12",
        "band": "easier",
        "text": "A 25 W bulb is switched on for 40 s. Calculate the energy it "
                "transfers.",
        "options": [
            {"text": "1000 J", "correct": True},
            {"text": "65 J", "correct": False,
             "why": "That adds the two figures, and a power cannot be added "
                    "to a time."},
            {"text": "0.625 J", "correct": False,
             "why": "That is 25 ÷ 40, a division where the formula "
                    "multiplies."},
            {"text": "1.6 J", "correct": False,
             "why": "That is 40 ÷ 25, upside down as well as the wrong "
                    "operation."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e13",
        "band": "easier",
        "text": "Which quantity does t stand for in the energy formula, and "
                "what unit does it go in as?",
        "options": [
            {"text": "The temperature, in degrees Celsius", "correct": False,
             "why": "Temperature plays no part here; the letter stands for a "
                    "time."},
            {"text": "The time, in seconds", "correct": True},
            {"text": "The time, in minutes", "correct": False,
             "why": "Minutes are the commonest slip in this lesson, and they "
                    "make the answer sixty times too small."},
            {"text": "The total energy, in joules", "correct": False,
             "why": "The total is E, which sits on the other side of the "
                    "equals sign."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e14",
        "band": "easier",
        "text": "One kilojoule is 1000 joules. How many joules is 18 kJ?",
        "options": [
            {"text": "180 J", "correct": False,
             "why": "That multiplies by ten, and a kilo means a thousand."},
            {"text": "1800 J", "correct": False,
             "why": "That multiplies by a hundred, leaving the answer ten "
                    "times too small."},
            {"text": "18 000 J", "correct": True},
            {"text": "0.018 J", "correct": False,
             "why": "That divides by a thousand, which turns a large energy "
                    "into a tiny one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e15",
        "band": "easier",
        "text": "How much energy does a 2200 W oven transfer in 10 seconds?",
        "options": [
            {"text": "220 J", "correct": False,
             "why": "That is 2200 ÷ 10, a division where the two quantities "
                    "multiply."},
            {"text": "2210 J", "correct": False,
             "why": "That adds the seconds to the watts, which cannot be "
                    "done."},
            {"text": "22 000 J", "correct": True},
            {"text": "220 000 J", "correct": False,
             "why": "That is ten times too large; 2200 × 10 is twenty-two "
                    "thousand."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e16",
        "band": "easier",
        "text": "Watts multiplied by seconds gives an answer in which unit?",
        "options": [
            {"text": "Joules", "correct": True},
            {"text": "Watts", "correct": False,
             "why": "Watts go in as the power. Multiplying by a time turns the "
                    "rate into an amount."},
            {"text": "Kilowatt-hours", "correct": False,
             "why": "That comes from kilowatts multiplied by hours, which is "
                    "the other legal pairing."},
            {"text": "Seconds", "correct": False,
             "why": "Seconds go in as the time. The answer is an energy, not "
                    "another time."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e17",
        "band": "easier",
        "text": "Half an hour is how many seconds?",
        "options": [
            {"text": "30 s", "correct": False,
             "why": "That is half a minute. An hour is sixty times longer than "
                    "a minute."},
            {"text": "1800 s", "correct": True},
            {"text": "360 s", "correct": False,
             "why": "That is six minutes, found by dividing 3600 by ten "
                    "instead of by two."},
            {"text": "3600 s", "correct": False,
             "why": "That is a whole hour, and the question asks for half of "
                    "one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e18",
        "band": "easier",
        "text": "A 9 W LED is left on for 100 s. Work out the energy "
                "transferred.",
        "options": [
            {"text": "109 J", "correct": False,
             "why": "That adds the two, and a rate cannot be added to a "
                    "time."},
            {"text": "11 J", "correct": False,
             "why": "That is 100 ÷ 9, a division where the formula "
                    "multiplies."},
            {"text": "0.09 J", "correct": False,
             "why": "That is 9 ÷ 100, upside down as well as the wrong "
                    "operation."},
            {"text": "900 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e19",
        "band": "easier",
        "text": "About how much energy does a single AA cell hold?",
        "options": [
            {"text": "About 10 J", "correct": False,
             "why": "Ten joules is roughly ten apples lifted onto a table, and "
                    "a cell holds far more."},
            {"text": "About 10 000 J", "correct": True},
            {"text": "About 1 J", "correct": False,
             "why": "One joule is about one apple lifted from the floor to a "
                    "table."},
            {"text": "About 10 000 000 J", "correct": False,
             "why": "That is more than boiling twenty full kettles, which no "
                    "AA cell could manage."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e20",
        "band": "easier",
        "text": "Which of these times could go straight into the formula "
                "beside a power in watts?",
        "options": [
            {"text": "45 minutes", "correct": False,
             "why": "Minutes have to become seconds first, or the answer is "
                    "sixty times too small."},
            {"text": "45 hours", "correct": False,
             "why": "Hours pair with kilowatts. With watts they must be turned "
                    "into seconds."},
            {"text": "45 seconds", "correct": True},
            {"text": "Three-quarters of an hour", "correct": False,
             "why": "That is 45 minutes written another way, and it still has "
                    "to be converted."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e21",
        "band": "easier",
        "text": "A fridge motor rated 90 W runs for 60 s. What energy does it "
                "transfer?",
        "options": [
            {"text": "150 J", "correct": False,
             "why": "That adds the rating to the time, which cannot be done to "
                    "two different quantities."},
            {"text": "1.5 J", "correct": False,
             "why": "That is 90 ÷ 60, a division where the formula "
                    "multiplies."},
            {"text": "5400 J", "correct": True},
            {"text": "54 000 J", "correct": False,
             "why": "That is ten times too large; 90 × 60 is five thousand "
                    "four hundred."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e22",
        "band": "easier",
        "text": "One megajoule is how many joules?",
        "options": [
            {"text": "1000", "correct": False,
             "why": "A thousand joules is a kilojoule, which is a thousand "
                    "times smaller."},
            {"text": "1 000 000", "correct": True},
            {"text": "3600", "correct": False,
             "why": "That is the number of seconds in an hour, not a prefix."},
            {"text": "100", "correct": False,
             "why": "No unit prefix stands for a hundred here; mega means a "
                    "million."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e23",
        "band": "easier",
        "text": "Which calculation finds how long an appliance ran for?",
        "options": [
            {"text": "power multiplied by energy", "correct": False,
             "why": "Multiplying those two gives neither a time nor anything "
                    "else useful."},
            {"text": "energy divided by power", "correct": True},
            {"text": "power divided by energy", "correct": False,
             "why": "That is the division upside down, and it would make a "
                    "powerful appliance run longer."},
            {"text": "energy multiplied by power", "correct": False,
             "why": "The same multiplication written the other way round, and "
                    "still not a time."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e24",
        "band": "easier",
        "text": "A student writes an answer as “360 000” and stops there. Why "
                "is that a problem?",
        "options": [
            {"text": "Because a number on its own does not say what quantity "
                     "it is", "correct": True},
            {"text": "Because an answer that large is certain to be wrong "
                     "somewhere in the working",
             "correct": False,
             "why": "Energies of that size are ordinary here; it is the "
                    "missing unit that is the fault."},
            {"text": "Because it has not been rounded",
             "correct": False,
             "why": "Rounding is a separate matter, and no rounding rule "
                    "supplies a unit."},
            {"text": "Because the formula only works when the answer is "
                     "written as a decimal",
             "correct": False,
             "why": "The form of the number changes nothing. What is missing "
                    "is the unit beside it."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e25",
        "band": "easier",
        "text": "A 60 W lamp transfers 600 J. How long was it on?",
        "options": [
            {"text": "36 000 s", "correct": False,
             "why": "That multiplies the two, and a time comes from dividing "
                    "the energy by the power."},
            {"text": "540 s", "correct": False,
             "why": "That subtracts, and a power cannot be taken away from an "
                    "energy."},
            {"text": "0.1 s", "correct": False,
             "why": "That is 60 ÷ 600, the division the wrong way up."},
            {"text": "10 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e26",
        "band": "easier",
        "text": "Which is the larger amount of energy, one kilojoule or one "
                "megajoule?",
        "options": [
            {"text": "One kilojoule, because kilo comes first in the alphabet "
                     "of prefixes",
             "correct": False,
             "why": "Prefixes are not ordered by their spelling; mega stands "
                    "for a million and kilo for a thousand."},
            {"text": "One megajoule", "correct": True},
            {"text": "They are equal",
             "correct": False,
             "why": "Only the kilojoule is a thousand joules. A megajoule is a "
                    "thousand of those."},
            {"text": "One kilojoule, because a megajoule is a thousandth of "
                     "a joule",
             "correct": False,
             "why": "Mega makes a unit larger, never smaller."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e27",
        "band": "easier",
        "text": "Find the energy a 1000 W heater transfers during 30 s of "
                "use.",
        "options": [
            {"text": "30 000 J", "correct": True},
            {"text": "1030 J", "correct": False,
             "why": "That adds the seconds to the watts, which are different "
                    "quantities."},
            {"text": "33 J", "correct": False,
             "why": "That is 1000 ÷ 30, a division where the two multiply."},
            {"text": "300 000 J", "correct": False,
             "why": "That is ten times too large; 1000 × 30 is thirty "
                    "thousand."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e28",
        "band": "easier",
        "text": "A time is given in hours and the power is in watts. What has "
                "to be done to the time?",
        "options": [
            {"text": "Divide it by 60", "correct": False,
             "why": "Dividing would make the time smaller, and an hour holds "
                    "more seconds than it does minutes."},
            {"text": "Multiply it by 60", "correct": False,
             "why": "That turns hours into minutes, which is only half the "
                    "journey to seconds."},
            {"text": "Multiply it by 3600", "correct": True},
            {"text": "Nothing — hours work with watts as they stand",
             "correct": False,
             "why": "Hours pair with kilowatts. Pairing them with watts is "
                    "wrong by a factor of 3600."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e29",
        "band": "easier",
        "text": "Which of these is a sensible size for the energy needed to "
                "boil a full kettle?",
        "options": [
            {"text": "About 360 J", "correct": False,
             "why": "That is roughly what it takes to lift a school bag onto a "
                    "high shelf a few times."},
            {"text": "About 3600 J", "correct": False,
             "why": "That is about carrying yourself up two flights of stairs, "
                    "and nowhere near boiling water."},
            {"text": "About 36 000 J", "correct": False,
             "why": "Still ten times too small — a full kettle needs hundreds "
                    "of thousands of joules."},
            {"text": "About 360 000 J", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-e30",
        "band": "easier",
        "text": "A 15 W router draws power for 200 s. How many joules is "
                "that?",
        "options": [
            {"text": "3000 J", "correct": True},
            {"text": "215 J", "correct": False,
             "why": "That adds the seconds to the watts rather than "
                    "multiplying them."},
            {"text": "13 J", "correct": False,
             "why": "That is 200 ÷ 15, a division where a multiplication is "
                    "needed."},
            {"text": "0.075 J", "correct": False,
             "why": "That is 15 ÷ 200, upside down as well as the wrong "
                    "operation."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ────────────────────────────────
    {
        "id": "p2-03-s11",
        "band": "standard",
        "text": "A 2 kW kettle is on for 5 minutes. Give the energy "
                "transferred in joules.",
        "options": [
            {"text": "10 J", "correct": False,
             "why": "That multiplies 2 by 5 with neither the kilowatts nor the "
                    "minutes converted."},
            {"text": "600 000 J", "correct": True},
            {"text": "10 000 J", "correct": False,
             "why": "That converts the kilowatts and leaves the time in "
                    "minutes."},
            {"text": "600 J", "correct": False,
             "why": "That converts the minutes and leaves the power in "
                    "kilowatts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s12",
        "band": "standard",
        "text": "An oven rated 2200 W is used for 45 minutes. Give the energy "
                "in joules.",
        "options": [
            {"text": "99 000 J", "correct": False,
             "why": "That is 2200 × 45, with the minutes going into the "
                    "formula as they stand."},
            {"text": "5 940 000 J", "correct": True},
            {"text": "132 000 J", "correct": False,
             "why": "That uses 60 s instead of 2700 s, so it is one minute of "
                    "roasting rather than forty-five."},
            {"text": "49 J", "correct": False,
             "why": "That is 2200 ÷ 45, a division where the formula "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s13",
        "band": "standard",
        "text": "A 1200 W kettle transfers 216 000 J. For how many minutes was "
                "it on?",
        "options": [
            {"text": "180 minutes", "correct": False,
             "why": "180 is the answer in seconds. The question asks for "
                    "minutes, so divide by sixty."},
            {"text": "3 minutes", "correct": True},
            {"text": "3 seconds", "correct": False,
             "why": "The number is right but the unit is not — and three "
                    "seconds could not boil anything."},
            {"text": "0.0056 minutes", "correct": False,
             "why": "That is 1200 ÷ 216 000, the division the wrong way up."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s14",
        "band": "standard",
        "text": "A lamp transfers 72 000 J while it is on for 20 minutes. What "
                "is its rating?",
        "options": [
            {"text": "3600 W", "correct": False,
             "why": "That divides by 20 instead of by 1200 s, leaving the time "
                    "in minutes."},
            {"text": "60 W", "correct": True},
            {"text": "1 440 000 W", "correct": False,
             "why": "That multiplies the two, and a rating comes from dividing "
                    "the energy by the time."},
            {"text": "0.017 W", "correct": False,
             "why": "That is 1200 ÷ 72 000, the division upside down."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s15",
        "band": "standard",
        "text": "Given that one kilowatt-hour is 3 600 000 J, how many joules "
                "is 2.5 kWh?",
        "options": [
            {"text": "9 000 000 J", "correct": True},
            {"text": "1 440 000 J", "correct": False,
             "why": "That divides by 2.5 rather than multiplying, so it makes "
                    "more energy into less."},
            {"text": "3 600 002 J", "correct": False,
             "why": "That adds 2.5 to the conversion figure instead of "
                    "multiplying by it."},
            {"text": "90 000 J", "correct": False,
             "why": "That is a hundred times too small; check the size of the "
                    "answer before writing it down."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s16",
        "band": "standard",
        "text": "A 9 W nightlight stays on from dusk to dusk, a full 24 hours. "
                "How many joules is that?",
        "options": [
            {"text": "216 J", "correct": False,
             "why": "That is 9 × 24, with the hours going in as though they "
                    "were seconds."},
            {"text": "12 960 J", "correct": False,
             "why": "That uses 1440 minutes rather than the 86 400 seconds in "
                    "a day."},
            {"text": "777 600 J", "correct": True},
            {"text": "2.7 J", "correct": False,
             "why": "That is 24 ÷ 9, which is neither the right operation nor "
                    "the right way round."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s17",
        "band": "standard",
        "text": "Convert 7 200 000 J into kilowatt-hours.",
        "options": [
            {"text": "2 kWh", "correct": True},
            {"text": "7200 kWh", "correct": False,
             "why": "That divides by a thousand only, which turns joules into "
                    "kilojoules rather than kilowatt-hours."},
            {"text": "2000 kWh", "correct": False,
             "why": "That is a thousand times too many; one kWh is already "
                    "3 600 000 J."},
            {"text": "0.5 kWh", "correct": False,
             "why": "That divides the wrong way round, making a large energy "
                    "into a fraction of a unit."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s18",
        "band": "standard",
        "text": "A student multiplies 2.5 kW by 30 minutes and labels the "
                "answer 75 kWh. What has gone wrong?",
        "options": [
            {"text": "The power should have been in watts, so the answer "
                     "should be 2500 kWh",
             "correct": False,
             "why": "Kilowatts are half of a legal pairing. It is the minutes "
                    "that break it."},
            {"text": "The operation should have been a division, giving "
                     "0.083 kWh",
             "correct": False,
             "why": "Energy is power multiplied by time; the operation was the "
                    "one part that was right."},
            {"text": "The time must be in hours, so it should be 1.25 kWh",
             "correct": True},
            {"text": "Nothing is wrong, but the answer should be labelled in "
                     "joules instead",
             "correct": False,
             "why": "Relabelling a wrong number does not fix it, and 75 is "
                    "not the energy in any unit."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s19",
        "band": "standard",
        "text": "An electric blanket rated 100 W is left on for 2 hours. Give "
                "the energy in joules.",
        "options": [
            {"text": "200 J", "correct": False,
             "why": "That is 100 × 2, with the hours put in as though they "
                    "were seconds."},
            {"text": "12 000 J", "correct": False,
             "why": "That uses 120 s — two minutes rather than two hours."},
            {"text": "720 000 J", "correct": True},
            {"text": "50 J", "correct": False,
             "why": "That is 100 ÷ 2, a division where the formula "
                    "multiplies."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s20",
        "band": "standard",
        "text": "A 40 W pump transfers 1.44 MJ. How long did it run?",
        "options": [
            {"text": "10 hours", "correct": True},
            {"text": "36 000 hours", "correct": False,
             "why": "36 000 is the answer in seconds. Dividing by 3600 turns "
                    "it into ten hours."},
            {"text": "36 minutes", "correct": False,
             "why": "That treats 1.44 MJ as 1440 J, losing a factor of a "
                    "thousand."},
            {"text": "27.8 hours", "correct": False,
             "why": "That is 40 ÷ 1.44, the division the wrong way round."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s21",
        "band": "standard",
        "text": "Which is larger: the energy a 2000 W kettle transfers in one "
                "minute, or a 60 W lamp in one hour?",
        "options": [
            {"text": "The kettle, because its rating is over thirty times "
                     "higher",
             "correct": False,
             "why": "It is, but the lamp runs for sixty times as long, and "
                    "sixty beats thirty-three."},
            {"text": "The lamp, at 216 000 J against 120 000 J",
             "correct": True},
            {"text": "They are equal, at 120 000 J each", "correct": False,
             "why": "The kettle gives 120 000 J and the lamp 216 000 J, so "
                    "they are not equal."},
            {"text": "The kettle, at 2 000 000 J against 216 000 J",
             "correct": False,
             "why": "2 000 000 J would need the kettle to run for a thousand "
                    "seconds, not sixty."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s22",
        "band": "standard",
        "text": "Why does leaving a time in minutes make an answer sixty times "
                "too small?",
        "options": [
            {"text": "Because the formula was written for seconds and rejects "
                     "minutes",
             "correct": False,
             "why": "The formula takes any consistent pairing. The reason is "
                    "what a watt means."},
            {"text": "Because a watt is a joule every second, and a minute "
                     "holds sixty of them", "correct": True},
            {"text": "Because sixty seconds of running time is lost to the "
                     "surroundings",
             "correct": False,
             "why": "Nothing is lost here. The slip is in the arithmetic, not "
                    "in the physics."},
            {"text": "Because energy is counted in minutes and power in "
                     "seconds",
             "correct": False,
             "why": "Energy is counted in joules and carries no time of its "
                    "own."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s23",
        "band": "standard",
        "text": "A 3 kW heater runs for 20 minutes. Give the energy in "
                "kilowatt-hours.",
        "options": [
            {"text": "60 kWh", "correct": False,
             "why": "That is 3 × 20, with the minutes standing in for hours."},
            {"text": "0.15 kWh", "correct": False,
             "why": "That is 3 ÷ 20, a division where the working "
                    "multiplies."},
            {"text": "1 kWh", "correct": True},
            {"text": "3600 kWh", "correct": False,
             "why": "That uses the seconds in an hour, which belong to the "
                    "joules pairing rather than this one."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s24",
        "band": "standard",
        "text": "An 800 W microwave has to transfer 96 000 J. How long must it "
                "run?",
        "options": [
            {"text": "76 800 000 s", "correct": False,
             "why": "That multiplies the two, and a time comes from a "
                    "division."},
            {"text": "120 s", "correct": True},
            {"text": "2 s", "correct": False,
             "why": "That is the answer in minutes, written as though it were "
                    "seconds."},
            {"text": "0.008 s", "correct": False,
             "why": "That is 800 ÷ 96 000, the division the wrong way up."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s25",
        "band": "standard",
        "text": "One student's answer is 18 kJ and another's is 18 000 J for "
                "the same job. Who is right?",
        "options": [
            {"text": "Neither of them",
             "correct": False,
             "why": "They describe it identically; only the unit written at "
                    "the end differs."},
            {"text": "The first, because energy is properly quoted in "
                     "kilojoules",
             "correct": False,
             "why": "Joules are the standard unit, and kilojoules are simply a "
                    "convenient multiple."},
            {"text": "The second, because joules are the only unit a formula "
                     "may produce",
             "correct": False,
             "why": "A formula produces a quantity, and the same quantity can "
                    "be written in more than one unit."},
            {"text": "Both — a kilojoule is a thousand joules", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s26",
        "band": "standard",
        "text": "Two car headlights rated 55 W each are left on for 90 "
                "minutes. How much energy is transferred altogether?",
        "options": [
            {"text": "297 000 J", "correct": False,
             "why": "That is one headlight's share. Two of them draw 110 W "
                    "between them."},
            {"text": "9900 J", "correct": False,
             "why": "That is 110 × 90, with the minutes never turned into "
                    "seconds."},
            {"text": "594 000 J", "correct": True},
            {"text": "4950 J", "correct": False,
             "why": "That is 55 × 90, using one lamp and leaving the time in "
                    "minutes as well."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s27",
        "band": "standard",
        "text": "An appliance transferred 1 080 000 J over 3 hours. What is "
                "its rating?",
        "options": [
            {"text": "100 W", "correct": True},
            {"text": "360 000 W", "correct": False,
             "why": "That divides by 3 rather than by the 10 800 seconds in "
                    "three hours."},
            {"text": "6000 W", "correct": False,
             "why": "That divides by 180, which is the number of minutes "
                    "rather than seconds."},
            {"text": "3 240 000 W", "correct": False,
             "why": "That multiplies the two, and a rating comes from a "
                    "division."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s28",
        "band": "standard",
        "text": "Which change would exactly double the energy an appliance "
                "transfers?",
        "options": [
            {"text": "Switching it on twice as often over the same total "
                     "running time",
             "correct": False,
             "why": "The total time is what the formula uses, and that has not "
                    "moved."},
            {"text": "Plugging it into a socket on a separate circuit",
             "correct": False,
             "why": "Which socket it uses changes neither the rating nor the "
                    "time."},
            {"text": "Running it for twice as long at the same rating",
             "correct": True},
            {"text": "Halving the rating and running it for twice as long",
             "correct": False,
             "why": "That leaves the product unchanged, so the energy is the "
                    "same rather than double."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s29",
        "band": "standard",
        "text": "A 2 kW heater ran for 1.5 hours. Which pair of figures gives "
                "that energy correctly?",
        "options": [
            {"text": "3 kWh, which is 10 800 000 J", "correct": True},
            {"text": "3 kWh, which is 3000 J", "correct": False,
             "why": "That treats a kilowatt-hour as a kilojoule; one kWh is "
                    "3 600 000 J."},
            {"text": "1.33 kWh, which is 4 800 000 J", "correct": False,
             "why": "1.33 comes from dividing 2 by 1.5, where the working "
                    "multiplies."},
            {"text": "3 kWh, which is 180 000 J", "correct": False,
             "why": "That uses 60 s for an hour rather than 3600 s."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-s30",
        "band": "standard",
        "text": "Why does asking whether an answer is a sensible size catch a "
                "unit slip faster than re-checking the arithmetic?",
        "options": [
            {"text": "Because a wrong unit always produces a number that is "
                     "too large to write down",
             "correct": False,
             "why": "The commonest slip here makes the answer too small, not "
                    "too large."},
            {"text": "Because the arithmetic was right — it was the number "
                     "put into it that was wrong", "correct": True},
            {"text": "Because a calculator cannot multiply two quantities that "
                     "carry different units",
             "correct": False,
             "why": "A calculator handles the numbers happily; it is the "
                    "person who has to supply the units."},
            {"text": "Because checking the size is quicker than doing the "
                     "multiplication in the first place",
             "correct": False,
             "why": "Speed is a side benefit. The point is that re-checking "
                    "cannot find an error that is not in the arithmetic."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ──────────────────────────────────
    {
        "id": "p2-03-h11",
        "band": "harder",
        "text": "A 500 W games console is left on overnight for 9 hours "
                "instead of being switched off after 2. How much extra energy "
                "is transferred?",
        "options": [
            {"text": "3500 J", "correct": False,
             "why": "That is 500 × 7 with the hours treated as seconds, which "
                    "is out by a factor of 3600."},
            {"text": "12 600 000 J", "correct": True},
            {"text": "16 200 000 J", "correct": False,
             "why": "That charges the console for all nine hours; only the "
                    "extra seven are wasted."},
            {"text": "210 000 J", "correct": False,
             "why": "That uses 420 s — seven minutes rather than seven "
                    "hours."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h12",
        "band": "harder",
        "text": "Over a week, which transfers more: a 9 W LED on for 6 hours a "
                "day, or a 2 kW kettle used 5 minutes a day?",
        "options": [
            {"text": "The LED, because six hours a day beats five minutes "
                     "easily",
             "correct": False,
             "why": "The LED reaches 0.378 kWh a week and the kettle about "
                    "1.17 kWh, so the hours are not enough."},
            {"text": "The kettle, by roughly three times", "correct": True},
            {"text": "They are about equal, at roughly 0.4 kWh each",
             "correct": False,
             "why": "Only the LED is near 0.4 kWh; the kettle is nearly three "
                    "times that."},
            {"text": "The kettle, by roughly two hundred times",
             "correct": False,
             "why": "That compares the ratings alone and forgets that the LED "
                    "runs for seventy times as long."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h13",
        "band": "harder",
        "text": "A meter shows that an appliance transferred 2.16 MJ in 30 "
                "minutes. What is its rating?",
        "options": [
            {"text": "72 000 W", "correct": False,
             "why": "That divides by 30 rather than by the 1800 seconds in "
                    "half an hour."},
            {"text": "1200 W", "correct": True},
            {"text": "1.2 W", "correct": False,
             "why": "That treats 2.16 MJ as 2160 J, losing a factor of a "
                    "thousand."},
            {"text": "64 800 000 W", "correct": False,
             "why": "That multiplies the two, and a rating comes from "
                    "dividing."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h14",
        "band": "harder",
        "text": "A student turns 45 minutes into 0.75 hours, multiplies by "
                "2200 W and writes 1650. What unit is that, and is it right?",
        "options": [
            {"text": "Joules, and it is wrong — the time should have been in "
                     "seconds",
             "correct": False,
             "why": "Watts with hours gives watt-hours, and the figure itself "
                    "is sound."},
            {"text": "Kilowatt-hours, and it is wrong by a factor of a "
                     "thousand",
             "correct": False,
             "why": "The unit is watt-hours; as kilowatt-hours it would read "
                    "1.65, which is the same energy."},
            {"text": "Watt-hours, and it is right — the same energy as "
                     "1.65 kWh", "correct": True},
            {"text": "Watts, and it is wrong because a power cannot come out "
                     "of that multiplication",
             "correct": False,
             "why": "A power multiplied by a time gives an energy, so the "
                    "answer cannot be in watts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h15",
        "band": "harder",
        "text": "A 3 kW heater runs for 20 minutes. A 1 kW heater is to "
                "transfer the same energy. How long must it run?",
        "options": [
            {"text": "20 minutes, because the energy is the same either way",
             "correct": False,
             "why": "The same energy at a third of the rate needs three times "
                    "the time."},
            {"text": "About 7 minutes", "correct": False,
             "why": "That divides the time by three, which is the right factor "
                    "in the wrong direction."},
            {"text": "60 minutes", "correct": True},
            {"text": "About 180 minutes", "correct": False,
             "why": "That multiplies by nine rather than by three, treating "
                    "both figures as though they scaled."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h16",
        "band": "harder",
        "text": "Mixing watts with hours is wrong by a factor of 3600. Why is "
                "the number that large?",
        "options": [
            {"text": "Because an hour holds 3600 seconds, and the watt counts "
                     "every one of them", "correct": True},
            {"text": "Because 3600 is the number of minutes in a working day",
             "correct": False,
             "why": "A day holds 1440 minutes, and the figure comes from an "
                    "hour rather than a day."},
            {"text": "Because the error doubles for every minute of running "
                     "time",
             "correct": False,
             "why": "The factor is fixed by the units and does not grow with "
                    "the running time."},
            {"text": "Because kilowatts are a thousand watts and an hour is "
                     "3.6 minutes",
             "correct": False,
             "why": "An hour is sixty minutes, and the thousand belongs to a "
                    "different conversion."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h17",
        "band": "harder",
        "text": "Over a week, how many kilowatt-hours does a 1.5 kW pump use "
                "if it is switched on for 40 minutes each day?",
        "options": [
            {"text": "420 kWh", "correct": False,
             "why": "That is 1.5 × 40 × 7 with the minutes standing in for "
                    "hours."},
            {"text": "60 kWh", "correct": False,
             "why": "That leaves the week out and multiplies by 40 minutes as "
                    "though they were hours."},
            {"text": "1 kWh", "correct": False,
             "why": "That is one day's figure, and the question asks for "
                    "seven of them."},
            {"text": "7 kWh", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h18",
        "band": "harder",
        "text": "Two appliances each transfer 1.8 MJ. A is rated 300 W; B ran "
                "for 600 s. What are A's time and B's rating?",
        "options": [
            {"text": "A ran 6000 s; B is rated 3000 W", "correct": True},
            {"text": "A ran 600 s; B is rated 300 W", "correct": False,
             "why": "That swaps the two figures over rather than working "
                    "either of them out."},
            {"text": "A ran 6 s; B is rated 3 W", "correct": False,
             "why": "Both are a thousand times too small, from reading 1.8 MJ "
                    "as 1800 J."},
            {"text": "A ran 540 000 s; B is rated 1 080 000 000 W",
             "correct": False,
             "why": "Both come from multiplying where the working divides."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h19",
        "band": "harder",
        "text": "A student insists that 5 MJ and 5000 kJ are different "
                "amounts. Are they?",
        "options": [
            {"text": "Yes — a megajoule is a million kilojoules, so 5 MJ is "
                     "far larger",
             "correct": False,
             "why": "A megajoule is a million JOULES, which is a thousand "
                    "kilojoules."},
            {"text": "No — they are the same amount written two ways",
             "correct": True},
            {"text": "Yes — 5000 kJ is the larger, because the number in front "
                     "is bigger",
             "correct": False,
             "why": "The number is bigger because the unit is smaller; the two "
                    "cancel out exactly."},
            {"text": "It cannot be decided",
             "correct": False,
             "why": "A unit conversion does not depend on what produced the "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h20",
        "band": "harder",
        "text": "A car charger delivers 7 kW for 4 hours. Give the energy in "
                "kilowatt-hours and then in megajoules.",
        "options": [
            {"text": "28 kWh, which is 1.75 MJ", "correct": False,
             "why": "That divides by 16 instead of multiplying by 3.6; one kWh "
                    "is 3.6 MJ."},
            {"text": "11 kWh, which is 39.6 MJ", "correct": False,
             "why": "11 comes from adding 7 and 4, where the working "
                    "multiplies."},
            {"text": "28 kWh, which is 100.8 MJ", "correct": True},
            {"text": "28 kWh, which is 28 MJ", "correct": False,
             "why": "That treats a kilowatt-hour as a megajoule; it is 3.6 of "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h21",
        "band": "harder",
        "text": "Two students work out the same oven use. One writes 1.65 and "
                "the other 5 940 000. Can both be right?",
        "options": [
            {"text": "No — two answers this far apart cannot describe one "
                     "job",
             "correct": False,
             "why": "They are the same energy; the gap is entirely the "
                    "difference between the units."},
            {"text": "No — the larger figure must have left a time in "
                     "seconds by mistake",
             "correct": False,
             "why": "Seconds are exactly what the joules pairing wants, so "
                    "nothing there is a mistake."},
            {"text": "Yes — one is in kilowatt-hours and the other in joules",
             "correct": True},
            {"text": "Yes — but the smaller one is an estimate and the larger "
                     "one is exact",
             "correct": False,
             "why": "Both are exact. They are the same quantity in two legal "
                    "pairings."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h22",
        "band": "harder",
        "text": "A 100 W lamp is left on by mistake for a whole week. How much "
                "energy is that, in kilowatt-hours?",
        "options": [
            {"text": "16.8 kWh", "correct": True},
            {"text": "700 kWh", "correct": False,
             "why": "That is 100 × 7 with the watts never turned into "
                    "kilowatts."},
            {"text": "2.4 kWh", "correct": False,
             "why": "That is one day's worth, and a week holds seven of "
                    "them."},
            {"text": "16 800 kWh", "correct": False,
             "why": "That is a thousand times too large, from leaving the "
                    "rating in watts."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h23",
        "band": "harder",
        "text": "An answer comes out sixty times LARGER than it should be. "
                "Which slip would explain that?",
        "options": [
            {"text": "A time already in seconds was multiplied by 60 as well",
             "correct": True},
            {"text": "A time in minutes went into the formula unchanged",
             "correct": False,
             "why": "That makes an answer sixty times too small, which is the "
                    "opposite error."},
            {"text": "Kilowatts were paired with a time in hours",
             "correct": False,
             "why": "That is one of the two legal pairings, so it produces no "
                    "error at all."},
            {"text": "The power was divided by the time, not multiplied",
             "correct": False,
             "why": "That would not give a factor of sixty; it would give a "
                    "completely different sort of answer."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h24",
        "band": "harder",
        "text": "A 2000 W kettle boils a jug in 3 minutes. A 3000 W kettle "
                "boils the same jug. Estimate its time and compare the "
                "energies.",
        "options": [
            {"text": "About 2 minutes, and about the same energy",
             "correct": True},
            {"text": "About 2 minutes, and half the energy", "correct": False,
             "why": "Two-thirds of the time at one and a half times the rate "
                    "leaves the product almost unchanged."},
            {"text": "About 4.5 minutes, and more energy", "correct": False,
             "why": "A higher rating boils the same water faster, not more "
                    "slowly."},
            {"text": "About 3 minutes, and half as much energy again",
             "correct": False,
             "why": "The time falls because the rate has risen; it does not "
                    "stay put while the energy climbs."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h25",
        "band": "harder",
        "text": "An immersion heater transfers 12.6 MJ in one hour. What is "
                "its rating in kilowatts?",
        "options": [
            {"text": "12.6 kW", "correct": False,
             "why": "That reads megajoules as kilowatt-hours; one kWh is "
                    "3.6 MJ, so the figure is 3.6 times too large."},
            {"text": "3.5 kW", "correct": True},
            {"text": "210 kW", "correct": False,
             "why": "That divides by 60 rather than by 3600, using minutes "
                    "instead of seconds."},
            {"text": "0.0035 kW", "correct": False,
             "why": "That divides by a thousand once too often, leaving a "
                    "rating smaller than a lamp's."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h26",
        "band": "harder",
        "text": "Which is the larger amount of energy, 0.5 kWh or "
                "1 500 000 J?",
        "options": [
            {"text": "1 500 000 J, because a joule figure with six digits "
                     "beats a fraction of a unit",
             "correct": False,
             "why": "How many digits a figure has says nothing; 0.5 kWh is "
                    "1 800 000 J."},
            {"text": "They are equal",
             "correct": False,
             "why": "Half of 3 600 000 is 1 800 000, so they are not equal."},
            {"text": "0.5 kWh, because it is 1 800 000 J", "correct": True},
            {"text": "It cannot be decided, because the two units measure "
                     "different quantities",
             "correct": False,
             "why": "Both measure energy, so one can always be converted into "
                    "the other."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h27",
        "band": "harder",
        "text": "A student writes “15 W × 2 h = 30 J”. Which pair of "
                "corrections is needed?",
        "options": [
            {"text": "The rating should be in kilowatts, and the answer is "
                     "0.03 kWh",
             "correct": False,
             "why": "0.015 kW × 2 h is 0.03 kWh, which is right in kWh — but "
                    "the answer as written is labelled in joules."},
            {"text": "The time must be in seconds, and the answer is "
                     "108 000 J", "correct": True},
            {"text": "The operation should be a division, and the answer is "
                     "7.5 J",
             "correct": False,
             "why": "Energy is a product. The operation was the part that was "
                    "already right."},
            {"text": "The time must be in minutes, and the answer is 1800 J",
             "correct": False,
             "why": "Minutes are no better than hours here; a watt is defined "
                    "per second."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h28",
        "band": "harder",
        "text": "A 90 W fridge motor runs in bursts totalling 5 hours a day. "
                "How much energy is that in a day, in joules?",
        "options": [
            {"text": "450 J", "correct": False,
             "why": "That is 90 × 5 with the hours going in as though they "
                    "were seconds."},
            {"text": "27 000 J", "correct": False,
             "why": "That uses 300 s — five minutes rather than five hours."},
            {"text": "1 620 000 J", "correct": True},
            {"text": "7 776 000 J", "correct": False,
             "why": "That charges the motor for all 24 hours, and it runs for "
                    "five of them."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h29",
        "band": "harder",
        "text": "A 2000 W kettle and a 1000 W toaster each run for 4 minutes. "
                "What is the difference in the energy transferred?",
        "options": [
            {"text": "4000 J", "correct": False,
             "why": "That is 1000 × 4 with the minutes left unconverted."},
            {"text": "240 000 J", "correct": True},
            {"text": "720 000 J", "correct": False,
             "why": "That is the sum of the two totals rather than the "
                    "difference between them."},
            {"text": "1000 J", "correct": False,
             "why": "That is the gap between the two ratings, which is a rate "
                    "rather than an energy."},
        ],
        "figure": None,
    },
    {
        "id": "p2-03-h30",
        "band": "harder",
        "text": "What is the strongest reason for writing the unit beside "
                "every number in the working?",
        "options": [
            {"text": "It shows the pairing is legal before the multiplication "
                     "happens", "correct": True},
            {"text": "It makes the working longer for a marker to follow",
             "correct": False,
             "why": "Length is not the point, and a unit takes almost no room "
                    "on the line."},
            {"text": "It is required before a calculator accepts the numbers",
             "correct": False,
             "why": "A calculator takes bare numbers; the units are entirely "
                    "for the person."},
            {"text": "It proves the arithmetic itself has been done correctly",
             "correct": False,
             "why": "Units cannot check a multiplication. They check that the "
                    "right quantities went into it."},
        ],
        "figure": None,
    },
]
