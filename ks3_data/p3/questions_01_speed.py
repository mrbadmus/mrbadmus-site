"""P3 lesson 01 — Speed: twelve questions (MRB-223).

Written against Design's page. The fly and the plane, the three ramps and
the three compare pairs are hers.

The discriminations, in the order the lesson builds them:

  · how fast something LOOKS depends on how far away it is (`FORCE-02`);
  · finishing first is not travelling fastest (`FORCE-01`);
  · the division goes distance-over-time and not the order you were given
    the numbers in (`FORCE-04`);
  · average speed is total distance ÷ total time, never the average of
    the speeds (`FORCE-03`) — the lesson's hardest idea, and where the
    harder band sits;
  · a camera measures over the stretch it measures over (`FORCE-05`).

⚠️ POSITION IS AUTHORED — index cycles 1, 2, 3, 0, giving three of each.

⚠️ Rung 1 (the trolley over 1.5 m in 0.60 s) and Rung 2 (200 m in 40 s
then 200 m in 60 s) are NOT restated; check 6 of `verify_questions.py`
forbids it.

The lesson carries no figures, so every question is figure=None.
"""

UNIT = "P3"
LESSON = "speed"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p3-01-e01",
        "band": "easier",
        "text": "Speed is worked out by…",
        "options": [
            {"text": "multiplying distance by time", "correct": False,
             "why": "That gives you neither — multiplying a distance by "
                    "a time does not produce a speed."},
            {"text": "dividing distance by time", "correct": True},
            {"text": "dividing time by distance", "correct": False,
             "why": "That is the triangle upside down. Distance goes on "
                    "top."},
            {"text": "adding distance and time", "correct": False,
             "why": "Metres and seconds are different quantities and cannot "
                    "be added."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e02",
        "band": "easier",
        "text": "A runner covers 60 m in 12 s. What is their speed?",
        "options": [
            {"text": "720 m/s", "correct": False,
             "why": "That is 60 × 12. Multiplying gives a distance, "
                    "not a speed."},
            {"text": "0.2 m/s", "correct": False,
             "why": "That is 12 ÷ 60 — time divided by distance, the "
                    "wrong way round."},
            {"text": "5 m/s", "correct": True},
            {"text": "48 m/s", "correct": False,
             "why": "That is 60 − 12. Nothing in the formula subtracts."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e03",
        "band": "easier",
        "text": "What does m/s mean?",
        "options": [
            {"text": "Metres multiplied by the number of seconds taken",
             "correct": False,
             "why": "The slash means divided by, not multiplied by."},
            {"text": "The number of minutes passing in each second",
             "correct": False,
             "why": "The m is metres. Minutes would make the unit a ratio of "
                    "two times."},
            {"text": "The number of metres travelled each minute",
             "correct": False,
             "why": "The s is seconds. Metres per minute would be written "
                    "m/min."},
            {"text": "The number of metres travelled each second",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e04",
        "band": "easier",
        "text": "A trolley crosses two light gates 0.80 m apart. What else "
                "do you need before you can work out its speed?",
        "options": [
            {"text": "The time it took to cross between them",
             "correct": True},
            {"text": "The mass of the trolley", "correct": False,
             "why": "Nothing in speed = distance ÷ time uses a mass."},
            {"text": "The height of the ramp", "correct": False,
             "why": "The ramp decides how fast it goes, but the speed is "
                    "worked out from the distance and the time, not from the "
                    "ramp."},
            {"text": "How far the trolley travelled after the second gate",
             "correct": False,
             "why": "The measurement is between the gates. What happens "
                    "afterwards is not part of it."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p3-01-s01",
        "band": "standard",
        "text": "A sprinter runs 100 m in 10.5 s. A cyclist rides 400 m in "
                "32 s. Who is travelling faster?",
        "options": [
            {"text": "The sprinter, because they finish sooner",
             "correct": False,
             "why": "Finishing sooner only means the distance was shorter. "
                    "100 ÷ 10.5 = 9.52 m/s against 400 ÷ 32 = "
                    "12.50 m/s."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "The cyclist, going at 12.5 m/s", "correct": True},
            {"text": "They are the same", "correct": False,
             "why": "Work both divisions out — 9.52 m/s against "
                    "12.50 m/s is not a dead heat."},
            {"text": "It cannot be decided without knowing the route",
             "correct": False,
             "why": "Speed = distance ÷ time. Both numbers are given "
                    "for both."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s02",
        "band": "standard",
        "text": "A car travels at 72 km/h and a cyclist at 20 m/s. Which is "
                "faster?",
        "options": [
            {"text": "The car, because 72 is a much bigger number",
             "correct": False,
             "why": "The numbers are in different units, so they cannot be "
                    "compared as they stand."},
            {"text": "The cyclist, because m/s is the scientific unit",
             "correct": False,
             "why": "Which unit is scientific has nothing to do with which "
                    "speed is larger."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "They are the same: 72 km/h ÷ 3.6 = 20 m/s",
             "correct": True},
            {"text": "It cannot be worked out from these numbers",
             "correct": False,
             "why": "It can: dividing km/h by 3.6 gives m/s, because there "
                    "are 1000 m in a km and 3600 s in an hour."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s03",
        "band": "standard",
        "text": "A student times the same trolley over the same distance "
                "three times and gets three different times. What should "
                "they do?",
        "options": [
            {"text": "Use the fastest run, because the other two must have "
                     "had errors",
             "correct": False,
             "why": "Nothing marks one run as the right one. Picking the "
                    "fastest is a choice, not a measurement."},
            {"text": "Keep repeating the timing until two of the runs agree "
                     "exactly",
             "correct": False,
             "why": "Two runs agreeing exactly would be luck, and waiting for "
                    "it throws away the readings you have."},
            {"text": "Use the first run, because it was the one done most "
                     "carefully",
             "correct": False,
             "why": "There is no reason the first is better than the others, "
                    "and it makes the answer depend on which run came first."},
            {"text": "Take the mean of the three times, then divide the "
                     "distance by it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s04",
        "band": "standard",
        "text": "A fly crosses your view in 0.8 s and a plane takes a full "
                "minute to cross the sky. Why does the fly look faster?",
        "options": [
            {"text": "Because it is much closer to your eye",
             "correct": True},
            {"text": "Because it really is travelling faster",
             "correct": False,
             "why": "The plane covers 250 m every second; the fly manages "
                    "about 1.9. It is not close."},
            {"text": "Because small things travel faster than large ones",
             "correct": False,
             "why": "Size has nothing to do with speed."},
            {"text": "Because the plane is slowed down by the air",
             "correct": False,
             "why": "The plane's 250 m/s is its actual speed through the "
                    "air, not a reduced one."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p3-01-h01",
        "band": "harder",
        "text": "Someone walks 100 m at 1 m/s, then runs 100 m at 5 m/s. "
                "What is their average speed for the whole journey?",
        "options": [
            {"text": "3 m/s, halfway between the two", "correct": False,
             "why": "Averaging the speeds ignores that the walk took 100 s "
                    "and the run took 20 s. Time spent slowly counts for "
                    "more."},
            {"text": "About 1.67 m/s", "correct": True},
            {"text": "6 m/s, the two speeds added", "correct": False,
             "why": "Adding speeds is for relative motion, not for two legs "
                    "of one journey."},
            {"text": "5 m/s, the faster of the two", "correct": False,
             "why": "That is the second leg only, and the journey includes "
                    "the first."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h02",
        "band": "harder",
        "text": "Why does the light-gate bench show a distance and a time "
                "but refuse to show a speed?",
        "options": [
            {"text": "Because the apparatus is not accurate enough to work "
                     "out a speed you could trust from the two readings",
             "correct": False,
             "why": "It has both numbers it would need. Accuracy is not what "
                    "is stopping it."},
            {"text": "Because a speed can only be measured over long "
                     "distances, and a metre of bench is nowhere near enough",
             "correct": False,
             "why": "Speed can be measured over any distance you can time. "
                    "That is what the gates do."},
            {"text": "Because a speed is something you work out from two "
                     "measurements, and doing it for you would remove the "
                     "step",
             "correct": True},
            {"text": "Because the gates only measure time, and the distance "
                     "on the display was never measured",
             "correct": False,
             "why": "You set the gate separation yourself, so the distance is "
                    "measured too — by you."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h03",
        "band": "harder",
        "text": "A driver passes a roadside camera at exactly 30 mph and is "
                "later fined by an average-speed check on the same road. How "
                "is that possible?",
        "options": [
            {"text": "The roadside camera must have been faulty, because two "
                     "honest measurements of one journey cannot disagree",
             "correct": False,
             "why": "Both readings can be perfectly accurate. They are "
                    "measurements of different things."},
            {"text": "Average-speed cameras are set to a lower limit than "
                     "roadside ones, so the same driving fails one of them",
             "correct": False,
             "why": "The limit is the same. What differs is the stretch each "
                    "one divides by."},
            {"text": "The average-speed check measured a different vehicle, "
                     "because the plates are read from a long way off",
             "correct": False,
             "why": "The point of the pair of gantries is that they identify "
                    "the same vehicle at both ends."},
            {"text": "The camera measured over a few metres; the check "
                     "measured over two kilometres, and the driver was faster "
                     "in between",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h04",
        "band": "harder",
        "text": "A student measures a walk down a corridor with a tape and a "
                "stopwatch and gets 1.4 m/s. What is the biggest source of "
                "error, and what would reduce it most?",
        "options": [
            {"text": "Reaction time at the stopwatch — use a longer "
                     "corridor",
             "correct": True},
            {"text": "Reaction time at the stopwatch — use a faster "
                     "walker",
             "correct": False,
             "why": "A faster walk makes the timed interval SHORTER, so the "
                    "same reaction error becomes a bigger share of it."},
            {"text": "The tape measure — measure to the nearest metre "
                     "instead",
             "correct": False,
             "why": "A tape is accurate to a centimetre or so, and rounding "
                    "to the nearest metre would make it worse rather than "
                    "better."},
            {"text": "The walker's stride length — ask them to take "
                     "even steps",
             "correct": False,
             "why": "Nothing in distance ÷ time uses a stride length. "
                    "The distance is measured with the tape."},
        ],
        "figure": None,
    },


    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p3-01-e05",
        "band": "easier",
        "text": "Which of these is a unit of speed?",
        "options": [
            {"text": "s/m", "correct": False,
             "why": "That is the unit you get from time ÷ distance — the "
                    "division the wrong way round."},
            {"text": "m/s", "correct": True},
            {"text": "m", "correct": False,
             "why": "A metre is a distance on its own. A speed needs a time "
                    "as well."},
            {"text": "ms", "correct": False,
             "why": "Written together that is a millisecond, which is a time, "
                    "not a speed."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e06",
        "band": "easier",
        "text": "A bus travels 240 m in 30 s. What is its speed?",
        "options": [
            {"text": "8 m/s", "correct": True},
            {"text": "7200 m/s", "correct": False,
             "why": "That is 240 × 30. Multiplying a distance by a time does "
                    "not give a speed."},
            {"text": "0.125 m/s", "correct": False,
             "why": "That is 30 ÷ 240 — time divided by distance, the "
                    "triangle upside down."},
            {"text": "210 m/s", "correct": False,
             "why": "That is 240 − 30. Nothing in speed = distance ÷ time "
                    "subtracts."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e07",
        "band": "easier",
        "text": "You know a car's speed and how long it travelled for. How do "
                "you find the distance?",
        "options": [
            {"text": "Divide the speed by the time", "correct": False,
             "why": "That leaves metres per second per second, which is not a "
                    "distance."},
            {"text": "Divide the time by the speed", "correct": False,
             "why": "That is the same division upside down, and it does not "
                    "give a distance either."},
            {"text": "Multiply the speed by the time", "correct": True},
            {"text": "Add the speed and the time", "correct": False,
             "why": "Metres per second and seconds are different quantities "
                    "and cannot be added."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e08",
        "band": "easier",
        "text": "You know how far a train has to go and how fast it travels. "
                "How do you find the time it will take?",
        "options": [
            {"text": "Divide the distance by the speed", "correct": True},
            {"text": "Multiply the distance by the speed", "correct": False,
             "why": "That gives a far bigger number, and the seconds never "
                    "appear on their own."},
            {"text": "Divide the speed by the distance", "correct": False,
             "why": "That is the division the wrong way round; the distance "
                    "goes on top when you want a time."},
            {"text": "Subtract the speed from the distance", "correct": False,
             "why": "Metres and metres per second are different quantities, "
                    "so they cannot be subtracted."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e09",
        "band": "easier",
        "text": "Four objects each travel for 10 s. One covers 40 m, one "
                "25 m, one 60 m and one 15 m. Which is travelling fastest?",
        "options": [
            {"text": "The one that covers 15 m", "correct": False,
             "why": "Covering the least ground in the same time makes it the "
                    "slowest of the four, not the fastest."},
            {"text": "The one that covers 25 m", "correct": False,
             "why": "25 m in 10 s is 2.5 m/s, and 60 m in 10 s is 6 m/s."},
            {"text": "The one that covers 60 m", "correct": True},
            {"text": "They are all the same, as the times are equal",
             "correct": False,
             "why": "Equal times are what lets you compare them: the one "
                    "going furthest in that time is fastest."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e10",
        "band": "easier",
        "text": "What is meant by the average speed of a journey?",
        "options": [
            {"text": "The average of the speeds travelled at",
             "correct": False,
             "why": "Adding the speeds and halving ignores how long was spent "
                    "at each one."},
            {"text": "The total distance divided by the total time",
             "correct": True},
            {"text": "The speed reached halfway through the journey",
             "correct": False,
             "why": "That is one instant, and it need not be typical of the "
                    "whole journey."},
            {"text": "The fastest speed reached during the journey",
             "correct": False,
             "why": "That is the top speed. An average has to take the slow "
                    "parts in as well."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e11",
        "band": "easier",
        "text": "A cyclist is travelling at 3 m/s. What does that tell you?",
        "options": [
            {"text": "She travels 3 metres in the whole journey",
             "correct": False,
             "why": "3 m/s is a rate: 3 metres in each second, not 3 metres "
                    "altogether."},
            {"text": "She takes 3 seconds to travel one metre",
             "correct": False,
             "why": "That would be a speed of about 0.33 m/s — the unit read "
                    "upside down."},
            {"text": "She has been cycling for 3 seconds", "correct": False,
             "why": "The 3 counts metres in each second; it is not how long "
                    "she has been going."},
            {"text": "She travels 3 metres every second", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e12",
        "band": "easier",
        "text": "A car is parked at the roadside. Relative to the ground, its "
                "speed is…",
        "options": [
            {"text": "0 m/s, because it is not moving at all",
             "correct": True},
            {"text": "1 m/s, because it is still on the road",
             "correct": False,
             "why": "Sitting on the road is not moving. Its distance from any "
                    "starting point is not changing at all."},
            {"text": "not a speed that can be written down", "correct": False,
             "why": "Not moving is a perfectly good speed, and it is written "
                    "0 m/s."},
            {"text": "impossible to give without knowing how far it has come",
             "correct": False,
             "why": "It covers no distance in any time, so the division gives "
                    "zero whatever it did earlier."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e13",
        "band": "easier",
        "text": "Which piece of apparatus times a trolley over a set distance "
                "in the lab?",
        "options": [
            {"text": "A metre rule on its own", "correct": False,
             "why": "A metre rule gives you the distance. You still need a "
                    "time before you have a speed."},
            {"text": "A pair of light gates", "correct": True},
            {"text": "A newtonmeter", "correct": False,
             "why": "A newtonmeter measures a force in newtons, and no force "
                    "appears in speed = distance ÷ time."},
            {"text": "A balance", "correct": False,
             "why": "A balance measures mass in kilograms, and mass does not "
                    "appear in the speed equation."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e14",
        "band": "easier",
        "text": "A cyclist rides at a steady 5 m/s for 10 s. How far does she "
                "travel?",
        "options": [
            {"text": "0.5 m", "correct": False,
             "why": "That is 5 ÷ 10. To get a distance you multiply the speed "
                    "by the time."},
            {"text": "2 m", "correct": False,
             "why": "That is 10 ÷ 5, which gives a time in seconds, not a "
                    "distance."},
            {"text": "50 m", "correct": True},
            {"text": "15 m", "correct": False,
             "why": "That is 5 + 10, and a speed and a time cannot be "
                    "added."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e15",
        "band": "easier",
        "text": "In speed = distance ÷ time, which measurement goes on top of "
                "the division?",
        "options": [
            {"text": "The time", "correct": False,
             "why": "That is the triangle upside down and gives seconds per "
                    "metre instead of metres per second."},
            {"text": "Whichever number the question gave you first",
             "correct": False,
             "why": "The order the numbers appear in does not change the "
                    "equation."},
            {"text": "The larger of the two numbers", "correct": False,
             "why": "Which number is bigger is irrelevant; the distance "
                    "always goes on top."},
            {"text": "The distance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e16",
        "band": "easier",
        "text": "A snail crawls 0.6 m in 60 s. What is its speed?",
        "options": [
            {"text": "36 m/s", "correct": False,
             "why": "That is 0.6 × 60, and multiplying a distance by a time "
                    "does not give a speed."},
            {"text": "0.01 m/s", "correct": True},
            {"text": "100 m/s", "correct": False,
             "why": "That is 60 ÷ 0.6 — time divided by distance, the wrong "
                    "way round."},
            {"text": "0.6 m/s", "correct": False,
             "why": "That is the distance with the unit swapped. The 60 s has "
                    "not been used at all."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-e17",
        "band": "easier",
        "text": "A car's speedometer reads 13 m/s. What is it telling the "
                "driver?",
        "options": [
            {"text": "How far the car has travelled so far", "correct": False,
             "why": "That is the odometer. A speedometer reads a speed, not a "
                    "distance."},
            {"text": "How fast the car is going at that moment",
             "correct": True},
            {"text": "The average speed for the whole journey",
             "correct": False,
             "why": "A speedometer reads the speed right now; an average has "
                    "to be worked out from the whole journey."},
            {"text": "How long the journey has taken so far", "correct": False,
             "why": "That would be a time. The unit m/s tells you the reading "
                    "is a speed."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p3-01-s05",
        "band": "standard",
        "text": "Runner A covers 200 m in 25 s. Runner B covers 150 m in "
                "20 s. Who is travelling faster?",
        "options": [
            {"text": "Runner B, because they took less time",
             "correct": False,
             "why": "Less time only means a shorter distance: 150 ÷ 20 = "
                    "7.5 m/s against 200 ÷ 25 = 8 m/s."},
            {"text": "Runner A, at 8 m/s", "correct": True},
            {"text": "Runner B, because 150 ÷ 20 is the bigger division",
             "correct": False,
             "why": "150 ÷ 20 is 7.5, which is smaller than 8, not bigger."},
            {"text": "They are the same, at 8 m each second",
             "correct": False,
             "why": "Only runner A covers 8 m each second. Runner B covers "
                    "7.5 m."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s06",
        "band": "standard",
        "text": "A car travels at 15 m/s. What is that speed in km/h?",
        "options": [
            {"text": "4.17 km/h", "correct": False,
             "why": "That is 15 ÷ 3.6, the conversion the wrong way round — "
                    "dividing by 3.6 turns km/h into m/s."},
            {"text": "15 000 km/h", "correct": False,
             "why": "Only the metres have been turned into kilometres; the "
                    "seconds still have to become hours."},
            {"text": "54 km/h", "correct": True},
            {"text": "900 km/h", "correct": False,
             "why": "That is 15 × 60, which gives metres per minute, not "
                    "kilometres per hour."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s07",
        "band": "standard",
        "text": "A train travels at a steady 45 m/s for 200 s. How far does "
                "it go, in kilometres?",
        "options": [
            {"text": "9 km", "correct": True},
            {"text": "9000 km", "correct": False,
             "why": "9000 is the answer in metres, and there are 1000 m in a "
                    "kilometre."},
            {"text": "90 km", "correct": False,
             "why": "That divides the 9000 m by 100. A kilometre is 1000 m, "
                    "not 100 m."},
            {"text": "0.225 km", "correct": False,
             "why": "That is 45 ÷ 200. To find a distance you multiply the "
                    "speed by the time."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s08",
        "band": "standard",
        "text": "A cyclist rides 1200 m at a steady 8 m/s. How long does the "
                "ride take?",
        "options": [
            {"text": "9600 s", "correct": False,
             "why": "That is 1200 × 8. Multiplying a distance by a speed does "
                    "not give a time."},
            {"text": "150 s", "correct": True},
            {"text": "0.0067 s", "correct": False,
             "why": "That is 8 ÷ 1200 — the division upside down, and far too "
                    "short to be believable."},
            {"text": "1192 s", "correct": False,
             "why": "That is 1200 − 8, and a distance and a speed cannot be "
                    "subtracted."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s09",
        "band": "standard",
        "text": "A trolley crosses two light gates 0.50 m apart in 0.25 s. "
                "What is its speed?",
        "options": [
            {"text": "0.125 m/s", "correct": False,
             "why": "That is 0.50 × 0.25. Multiplying gives neither a "
                    "distance nor a speed."},
            {"text": "0.5 m/s", "correct": False,
             "why": "That is 0.25 ÷ 0.50 — time divided by distance, the "
                    "wrong way round."},
            {"text": "2.0 m/s", "correct": True},
            {"text": "0.75 m/s", "correct": False,
             "why": "That is 0.50 + 0.25, and a distance and a time cannot be "
                    "added."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s10",
        "band": "standard",
        "text": "A trolley runs at the same steady speed, but the light gates "
                "are moved from 0.50 m apart to 1.00 m apart. What happens to "
                "the readings?",
        "options": [
            {"text": "The time doubles and the speed comes out the same",
             "correct": True},
            {"text": "The time doubles and so does the speed",
             "correct": False,
             "why": "Both the distance and the time double, so the division "
                    "gives exactly the same answer."},
            {"text": "The time stays the same and the speed halves",
             "correct": False,
             "why": "Twice the distance at the same speed must take twice as "
                    "long, so the time cannot stay the same."},
            {"text": "The speed doubles because it travels further",
             "correct": False,
             "why": "Travelling further does not make it faster; it simply "
                    "takes longer."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s11",
        "band": "standard",
        "text": "Which pair of readings would let you work out a car's "
                "average speed along a motorway?",
        "options": [
            {"text": "Its mass and the time taken between the two bridges",
             "correct": False,
             "why": "Nothing in speed = distance ÷ time uses a mass."},
            {"text": "The distance between the two bridges and the fuel it "
                     "used",
             "correct": False,
             "why": "Fuel used is not a time, so there is nothing to divide "
                    "the distance by."},
            {"text": "The speedometer reading as it passes each of the two "
                     "bridges",
             "correct": False,
             "why": "Those are two instant speeds; an average needs the "
                    "distance and the time for the whole stretch."},
            {"text": "The distance between two bridges and the time to travel "
                     "between them",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s12",
        "band": "standard",
        "text": "Four journeys are recorded. Which one has the greatest "
                "average speed?",
        "options": [
            {"text": "120 m in 20 s", "correct": False,
             "why": "That is 6 m/s, and one of the other three is faster."},
            {"text": "150 m in 30 s", "correct": False,
             "why": "That is 5 m/s — the same time as the fastest, but less "
                    "ground covered."},
            {"text": "210 m in 30 s", "correct": True},
            {"text": "160 m in 40 s", "correct": False,
             "why": "That is 4 m/s, the slowest of the four, even though it "
                    "is not the shortest distance."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s13",
        "band": "standard",
        "text": "A student times a 10.0 m walk three times and gets 8.2 s, "
                "8.6 s and 8.4 s. What speed should be reported?",
        "options": [
            {"text": "About 1.2 m/s", "correct": True},
            {"text": "About 1.22 m/s, worked out from the quickest run",
             "correct": False,
             "why": "Picking the quickest run throws away two perfectly good "
                    "readings."},
            {"text": "About 0.84 m/s", "correct": False,
             "why": "That is 8.4 ÷ 10.0 — time divided by distance, the wrong "
                    "way round."},
            {"text": "About 3.6 m/s, worked out from 30.0 m",
             "correct": False,
             "why": "The walk was 10.0 m each time. The three runs are "
                    "repeats, not three legs of one journey."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s14",
        "band": "standard",
        "text": "A hare runs at 20 m/s for 5 s, then sits still for 15 s. "
                "What is its average speed over the whole 20 s?",
        "options": [
            {"text": "20 m/s, because that is how fast it ran",
             "correct": False,
             "why": "The 15 s spent sitting still counts in the average as "
                    "well."},
            {"text": "10 m/s, halfway between 20 m/s and 0 m/s",
             "correct": False,
             "why": "Averaging the two speeds ignores that it spent three "
                    "times as long stopped as running."},
            {"text": "100 m/s", "correct": False,
             "why": "100 m is the distance covered. It still has to be "
                    "divided by the 20 s."},
            {"text": "5 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s15",
        "band": "standard",
        "text": "A lorry is limited to 25 m/s. It covers 1500 m of motorway "
                "in 50 s. Has it kept to the limit?",
        "options": [
            {"text": "No — its average speed over that stretch was 30 m/s",
             "correct": True},
            {"text": "Yes, because 1500 m is only a short stretch of road",
             "correct": False,
             "why": "The length of the stretch does not matter: 1500 ÷ 50 is "
                    "30 m/s either way."},
            {"text": "Yes, because 25 m/s is smaller than 50 s",
             "correct": False,
             "why": "A speed and a time are different quantities and cannot "
                    "be compared like that."},
            {"text": "It cannot be decided without the lorry's top speed",
             "correct": False,
             "why": "The check measures the average over the stretch, and "
                    "both numbers for it are given."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s16",
        "band": "standard",
        "text": "Why is a hand-held stopwatch a poor way to time a trolley "
                "over 0.20 m of bench?",
        "options": [
            {"text": "A stopwatch cannot measure times shorter than one "
                     "second",
             "correct": False,
             "why": "A stopwatch reads hundredths of a second. The problem is "
                    "the person pressing it."},
            {"text": "The trolley crosses in less time than a person can "
                     "react",
             "correct": True},
            {"text": "The trolley is too light for the stopwatch to detect",
             "correct": False,
             "why": "A stopwatch does not detect the trolley at all — a "
                    "person starts and stops it."},
            {"text": "A distance of 0.20 m is too short to have a speed",
             "correct": False,
             "why": "Any distance you can time has a speed. It is the timing "
                    "that is the difficulty, not the distance."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-s17",
        "band": "standard",
        "text": "A runner keeps up a steady 4 m/s. How long does she take to "
                "run 1 km?",
        "options": [
            {"text": "4000 s", "correct": False,
             "why": "That is 4 × 1000. Multiplying a speed by a distance does "
                    "not give a time."},
            {"text": "0.25 s", "correct": False,
             "why": "That is 1 ÷ 4, with the kilometre never turned into "
                    "metres."},
            {"text": "25 s", "correct": False,
             "why": "That is 100 ÷ 4. A kilometre is 1000 m, not 100 m."},
            {"text": "250 s", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p3-01-h05",
        "band": "harder",
        "text": "A cheetah runs at 20 m/s for 30 s, then walks at 5 m/s for "
                "20 s. What is its average speed for the whole 50 s?",
        "options": [
            {"text": "12.5 m/s, halfway between the two speeds",
             "correct": False,
             "why": "Averaging the speeds ignores that it ran for 30 s and "
                    "only walked for 20 s."},
            {"text": "14 m/s", "correct": True},
            {"text": "25 m/s, the two speeds added", "correct": False,
             "why": "Adding speeds is for relative motion, not for two legs "
                    "of one journey."},
            {"text": "700 m/s", "correct": False,
             "why": "700 m is the total distance. It still has to be divided "
                    "by the total time of 50 s."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h06",
        "band": "harder",
        "text": "A coach must cover 45 km in 30 minutes. What average speed "
                "does it need, in m/s?",
        "options": [
            {"text": "1.5 m/s", "correct": False,
             "why": "That is 45 ÷ 30 with neither unit converted — kilometres "
                    "over minutes, not metres over seconds."},
            {"text": "1500 m/s", "correct": False,
             "why": "That is 45 000 ÷ 30, which divides by minutes instead of "
                    "by the 1800 seconds."},
            {"text": "25 m/s", "correct": True},
            {"text": "90 m/s", "correct": False,
             "why": "That is 90 km/h, which is the right speed written in the "
                    "wrong unit."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h07",
        "band": "harder",
        "text": "A ferry crosses a strait at a steady 8 m/s and the crossing "
                "takes 25 minutes. How wide is the strait?",
        "options": [
            {"text": "12 km", "correct": True},
            {"text": "200 m", "correct": False,
             "why": "That is 8 × 25, treating the minutes as if they were "
                    "seconds."},
            {"text": "3.1 km", "correct": False,
             "why": "That is 25 ÷ 8, a division where the question needs a "
                    "multiplication."},
            {"text": "12 000 km", "correct": False,
             "why": "12 000 is the answer in metres, and there are 1000 m in "
                    "a kilometre."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h08",
        "band": "harder",
        "text": "Sound travels through air at about 330 m/s. A firework is "
                "seen, and the bang arrives 3 s later. How far away was it?",
        "options": [
            {"text": "110 m", "correct": False,
             "why": "That is 330 ÷ 3. To get a distance you multiply the "
                    "speed by the time."},
            {"text": "333 m", "correct": False,
             "why": "That is 330 + 3, and a speed and a time cannot be "
                    "added."},
            {"text": "0.009 m", "correct": False,
             "why": "That is 3 ÷ 330 — the division upside down, and it does "
                    "not give a distance."},
            {"text": "990 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h09",
        "band": "harder",
        "text": "A satellite travels at 7.8 km/s. How far does it go in one "
                "minute?",
        "options": [
            {"text": "468 km", "correct": True},
            {"text": "7.8 km", "correct": False,
             "why": "That is one second's worth of travel, and a minute is 60 "
                    "of them."},
            {"text": "0.13 km", "correct": False,
             "why": "That is 7.8 ÷ 60, a division where a multiplication is "
                    "needed."},
            {"text": "28 080 km", "correct": False,
             "why": "That is 7.8 × 3600, which is how far it goes in an hour, "
                    "not in a minute."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h10",
        "band": "harder",
        "text": "Two students hand-time the same 100 m sprint and get 12.0 s "
                "and 12.6 s. Why would a 0.6 s disagreement matter far less "
                "when timing a marathon?",
        "options": [
            {"text": "Because a sprinter changes speed far more often than "
                     "a marathon runner does",
             "correct": False,
             "why": "The speed changing is not the issue; the length of the "
                    "interval being timed is."},
            {"text": "Because hand timing only works for events lasting "
                     "many minutes",
             "correct": False,
             "why": "Hand timing works for both. What differs is the size of "
                    "the error next to the time measured."},
            {"text": "Because 0.6 s is a big share of 12 s but a tiny share "
                     "of hours",
             "correct": True},
            {"text": "Because a marathon is timed with a more accurate kind "
                     "of stopwatch",
             "correct": False,
             "why": "The same stopwatch would do. It is how long the event "
                    "lasts that changes."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h11",
        "band": "harder",
        "text": "A runner says she averaged 5 m/s over a 10 km race, and her "
                "watch shows 45 minutes. Is she right?",
        "options": [
            {"text": "Yes — 10 ÷ 45 is close enough to 5", "correct": False,
             "why": "10 km ÷ 45 min is neither in metres nor in seconds, so "
                    "it cannot be compared with 5 m/s."},
            {"text": "No — 10 000 m in 2700 s is about 3.7 m/s",
             "correct": True},
            {"text": "No — she actually averaged about 13.5 m/s",
             "correct": False,
             "why": "13 500 m is how far 5 m/s would have carried her in "
                    "2700 s, not her speed."},
            {"text": "It cannot be decided without knowing the course",
             "correct": False,
             "why": "Average speed is total distance ÷ total time, and both "
                    "of those are given."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h12",
        "band": "harder",
        "text": "A trolley speeds up down a ramp. It is timed once over the "
                "top 0.60 m and once over the bottom 0.60 m, and the two "
                "speeds differ. Which statement is correct?",
        "options": [
            {"text": "The lower stretch is quicker, and that reading is still "
                     "only an average",
             "correct": True},
            {"text": "The lower stretch is quicker because the ramp is "
                     "steeper towards the bottom",
             "correct": False,
             "why": "The ramp has one slope all the way down. It is quicker "
                    "because it has been speeding up."},
            {"text": "The two should be equal, so the difference is a timing "
                     "error",
             "correct": False,
             "why": "A trolley released from rest really is faster lower "
                    "down, so the difference is genuine."},
            {"text": "The lower reading is the exact speed at the bottom of "
                     "the ramp",
             "correct": False,
             "why": "It is an average over 0.60 m, and the trolley is still "
                    "speeding up across that stretch."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h13",
        "band": "harder",
        "text": "A car covers the first 50 km at 50 km/h and the next 50 km "
                "at 100 km/h. A student says the average is 75 km/h. Why is "
                "that wrong?",
        "options": [
            {"text": "The two speeds should be multiplied, not averaged",
             "correct": False,
             "why": "Multiplying two speeds gives nothing usable; average "
                    "speed is total distance ÷ total time."},
            {"text": "Equal distances mean the average of the two speeds is "
                     "fine here",
             "correct": False,
             "why": "Equal distances are not equal times, and it is the times "
                    "the average depends on."},
            {"text": "The hour at 50 km/h outweighs the half-hour at "
                     "100 km/h, giving about 67 km/h",
             "correct": True},
            {"text": "It is wrong only because the speeds are in km/h rather "
                     "than m/s",
             "correct": False,
             "why": "Both speeds are in the same unit; the mistake is "
                    "averaging them instead of dividing the totals."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h14",
        "band": "harder",
        "text": "A student writes in their book: the trolley's speed was 1.5. "
                "What is wrong with that answer?",
        "options": [
            {"text": "Nothing — a speed is always in m/s anyway",
             "correct": False,
             "why": "It is not. The same journey is 1.5 m/s or 5.4 km/h, and "
                    "the number alone does not say which."},
            {"text": "The number should have been rounded to a whole number",
             "correct": False,
             "why": "Speeds are very often not whole numbers, so that is not "
                    "what is missing."},
            {"text": "It has no unit, so the number could mean several "
                     "different speeds",
             "correct": True},
            {"text": "The answer should always be given to two decimal "
                     "places",
             "correct": False,
             "why": "How many decimal places to give is a separate decision. "
                    "The unit is what is missing."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h15",
        "band": "harder",
        "text": "A cyclist rides 3.6 km in 30 minutes. What is her average "
                "speed in m/s?",
        "options": [
            {"text": "0.12 m/s", "correct": False,
             "why": "That is 3.6 ÷ 30 — kilometres over minutes, with neither "
                    "unit converted."},
            {"text": "2 m/s", "correct": True},
            {"text": "7.2 m/s", "correct": False,
             "why": "7.2 is the speed in km/h, which is the right journey in "
                    "the wrong unit."},
            {"text": "120 m/s", "correct": False,
             "why": "That is 3600 ÷ 30, dividing by minutes instead of by the "
                    "1800 seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h16",
        "band": "harder",
        "text": "Two students measure the same person walking the same "
                "corridor and get 1.3 m/s and 1.5 m/s. Neither has made a "
                "mistake. What is the most likely reason?",
        "options": [
            {"text": "One of them must have measured the corridor length "
                     "wrongly",
             "correct": False,
             "why": "The corridor is the same length for both. It is the walk "
                    "that changed."},
            {"text": "They timed two different walks — nobody walks at the "
                     "same speed twice",
             "correct": True},
            {"text": "Speed cannot be measured accurately with a hand-held "
                     "stopwatch",
             "correct": False,
             "why": "It can, and both readings are usable; they simply "
                    "describe two different walks."},
            {"text": "One of them divided the two numbers the wrong way "
                     "round",
             "correct": False,
             "why": "Dividing the wrong way round would give about 0.7, "
                    "nowhere near the other reading."},
        ],
        "figure": None,
    },
    {
        "id": "p3-01-h17",
        "band": "harder",
        "text": "An athlete runs 400 m in 60 s. Her coach wants the time cut "
                "to 50 s. What average speed does the new target need?",
        "options": [
            {"text": "6.67 m/s", "correct": False,
             "why": "That is 400 ÷ 60, which is her present speed, not the "
                    "target."},
            {"text": "80 m/s", "correct": False,
             "why": "That is 400 ÷ 5, dividing by the time saved instead of "
                    "by the new total time."},
            {"text": "8 m/s", "correct": True},
            {"text": "1.33 m/s", "correct": False,
             "why": "That is the difference between the old and new speeds, "
                    "not the speed she needs."},
        ],
        "figure": None,
    },
]
