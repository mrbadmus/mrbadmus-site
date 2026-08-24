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
            {"text": "Metres multiplied by seconds", "correct": False,
             "why": "The slash means divided by, not multiplied by."},
            {"text": "Minutes per second", "correct": False,
             "why": "The m is metres. Minutes would make the unit a ratio of "
                    "two times."},
            {"text": "Metres per minute", "correct": False,
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
            {"text": "The cyclist", "correct": True},
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
            {"text": "They are the same", "correct": True},
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
            {"text": "Use the fastest run, because the others had errors",
             "correct": False,
             "why": "Nothing marks one run as the right one. Picking the "
                    "fastest is a choice, not a measurement."},
            {"text": "Repeat until two runs agree exactly", "correct": False,
             "why": "Two runs agreeing exactly would be luck, and waiting "
                    "for it throws away the readings you have."},
            {"text": "Use the first run, because it was done most carefully",
             "correct": False,
             "why": "There is no reason the first is better than the others, "
                    "and it makes the answer depend on which run came "
                    "first."},
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
            {"text": "Because the apparatus is not accurate enough to "
                     "calculate one",
             "correct": False,
             "why": "It has both numbers it would need. Accuracy is not what "
                    "is stopping it."},
            {"text": "Because speed can only be measured over long "
                     "distances",
             "correct": False,
             "why": "Speed can be measured over any distance you can time. "
                    "That is what the gates do."},
            {"text": "Because a speed is something you work out from two "
                     "measurements, and doing it for you would remove the "
                     "step",
             "correct": True},
            {"text": "Because the gates only measure time, not distance",
             "correct": False,
             "why": "You set the gate separation yourself, so the distance "
                    "is measured too — by you."},
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
            {"text": "The roadside camera must have been faulty",
             "correct": False,
             "why": "Both readings can be perfectly accurate. They are "
                    "measurements of different things."},
            {"text": "Average-speed cameras are set to a lower limit",
             "correct": False,
             "why": "The limit is the same. What differs is the stretch each "
                    "one divides by."},
            {"text": "The average-speed check measured a different vehicle",
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
]
