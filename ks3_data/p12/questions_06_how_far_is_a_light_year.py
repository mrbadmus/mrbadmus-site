"""P12 lesson 06 — How far is a light year: twelve questions (MRB-223).

Written against Design's page. The Proxima Centauri hook, the five light
journeys and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · a light year is a DISTANCE and never a duration (`SPACE-19`,
    `SPACE-22`);
  · nor is it a speed — the speed is the thing the unit is built from
    (`SPACE-21`);
  · d = c × t, with the time in seconds before it multiplies;
  · light takes time to arrive, so every observation is of the past
    (`SPACE-20`). The harder band sits here.

⚠️ POSITION IS AUTHORED — 3,2,0,1 · 0,1,3,2 · 1,0,2,3, three of each.

⚠️ Neither marked rung is restated: the 500 s Sun calculation and the
craft that arrives "in four light years" are the ladder's. Nor is a worked
example reused — the 1.28 s Moon, the 8.3-minute Sun and the 22-minute
Mars probe are all off limits.
"""

UNIT = "P12"
LESSON = "how-far-is-a-light-year"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p12-06-e01",
        "band": "easier",
        "text": "What kind of quantity is a light year?",
        "options": [
            {"text": "A time", "correct": False,
             "why": "The word 'year' is describing the light's journey, not "
                    "yours. What the unit gives you is a distance."},
            {"text": "A speed", "correct": False,
             "why": "The speed of light is a separate quantity, in metres per "
                    "second. A light year is built from it, and is not it."},
            {"text": "A brightness", "correct": False,
             "why": "Brightness is measured in quite different units and has "
                    "nothing to do with the light year."},
            {"text": "A distance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e02",
        "band": "easier",
        "text": "How fast does light travel in a vacuum?",
        "options": [
            {"text": "300 000 m/s", "correct": False,
             "why": "That is a thousand times too slow. The figure is "
                    "300 000 km/s, which is 300 000 000 m/s."},
            {"text": "3000 m/s", "correct": False,
             "why": "That is about the speed of a rifle bullet, not of "
                    "light."},
            {"text": "300 000 000 m/s", "correct": True},
            {"text": "It depends on how bright the source is", "correct": False,
             "why": "The speed does not vary. A dim torch and a star send "
                    "light out at exactly the same speed."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e03",
        "band": "easier",
        "text": "A light year is how far light travels in one year. Roughly "
                "how far is that?",
        "options": [
            {"text": "About 9.5 million million kilometres", "correct": True},
            {"text": "About 300 thousand kilometres", "correct": False,
             "why": "That is how far light travels in one SECOND. A year is "
                    "over thirty million seconds."},
            {"text": "About 150 million kilometres", "correct": False,
             "why": "That is the distance from the Earth to the Sun, which "
                    "light crosses in a little over eight minutes."},
            {"text": "About 9.5 thousand kilometres", "correct": False,
             "why": "That is less than the diameter of the Earth. Light "
                    "covers it in a thirtieth of a second."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e04",
        "band": "easier",
        "text": "A star is 12 light years away. How long has the light "
                "entering your eye been travelling?",
        "options": [
            {"text": "It arrives instantly, because light is so fast",
             "correct": False,
             "why": "Light is fast and not instant. Over astronomical "
                    "distances the delay is enormous."},
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "12 years, one year per light year",
             "correct": True},
            {"text": "12 seconds", "correct": False,
             "why": "In 12 seconds light covers about 3.6 million km, which "
                    "does not even reach the Moon ten times over."},
            {"text": "It cannot be worked out without knowing the star's "
                     "brightness", "correct": False,
             "why": "The travel time follows from the distance alone, because "
                    "the speed of light is fixed."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p12-06-s01",
        "band": "standard",
        "text": "Light takes 2.6 s for the round trip from Earth to a "
                "satellite and back. How far away is the satellite? Take the "
                "speed of light as 3.0 × 10^8 m/s.",
        "options": [
            {"text": "3.9 × 10^8 m", "correct": True},
            {"text": "7.8 × 10^8 m", "correct": False,
             "why": "That is the whole ROUND TRIP. The satellite is half that "
                    "far away, because the light went out and came back."},
            {"text": "1.2 × 10^8 m", "correct": False,
             "why": "That divides the speed by the time. Cover d on the "
                    "triangle and c sits beside t, so they multiply."},
            {"text": "2.6 × 10^8 m", "correct": False,
             "why": "The time has been given the wrong unit rather than put "
                    "through the formula."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s02",
        "band": "standard",
        "text": "A signal takes 3 minutes to reach a spacecraft. How far "
                "away is it? Take the speed of light as 3.0 × 10^8 m/s.",
        "options": [
            {"text": "9.0 × 10^8 m", "correct": False,
             "why": "That multiplies by 3 instead of by 180. The time has to "
                    "become seconds before it multiplies."},
            {"text": "5.4 × 10^10 m", "correct": True},
            {"text": "1.0 × 10^8 m", "correct": False,
             "why": "That divides where the triangle says multiply. Cover d "
                    "and c sits beside t."},
            {"text": "1.8 × 10^2 m", "correct": False,
             "why": "That is just the time in seconds, with metres written "
                    "after it. The speed has not been used."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s03",
        "band": "standard",
        "text": "Why do astronomers measure space in light years rather than "
                "in kilometres?",
        "options": [
            {"text": "Because kilometres cannot be used outside the Earth's "
                     "atmosphere, so a different unit is needed the moment "
                     "you leave", "correct": False,
             "why": "A kilometre is a kilometre anywhere. The problem is how "
                    "many digits it takes."},
            {"text": "Because light years are more accurate than kilometres, "
                     "and an astronomical measurement needs the more accurate "
                     "unit", "correct": False,
             "why": "Neither unit is more accurate than the other. Accuracy "
                    "depends on the measurement, not the unit."},
            {"text": "Because a light year is a round number and a kilometre "
                     "is not, so the arithmetic comes out tidier",
             "correct": False,
             "why": "A light year is about 9 460 000 000 000 km, which is not "
                    "round at all."},
            {"text": "Because the kilometre figures run to unmanageable "
                     "numbers of digits, and a light year also says how old "
                     "the light is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s04",
        "band": "standard",
        "text": "Which of these is a distance?",
        "options": [
            {"text": "3.0 × 10^8 m/s", "correct": False,
             "why": "Metres PER SECOND is a speed. That is the speed of "
                    "light."},
            {"text": "4.24 years", "correct": False,
             "why": "Years on their own are a time. It becomes a distance "
                    "only when the word 'light' is in front of it."},
            {"text": "8.3 light minutes", "correct": True},
            {"text": "499 s", "correct": False,
             "why": "Seconds are a time — this is how long the Sun's light "
                    "takes to arrive, which is not the same as how far it "
                    "came."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p12-06-h01",
        "band": "harder",
        "text": "If the Sun stopped shining at this instant, when would we "
                "find out?",
        "options": [
            {"text": "Immediately, because we would stop feeling its heat",
             "correct": False,
             "why": "The heat is carried by the same light, at the same "
                    "speed, so it arrives on the same delay."},
            {"text": "About 8 minutes later, when the last of its light "
                     "reaches us", "correct": True},
            {"text": "About a year later, because the Sun is one light year "
                     "away", "correct": False,
             "why": "The Sun is about 8 light MINUTES away. A light year "
                    "would put it well past the nearest star."},
            {"text": "Never, because the light already on its way would keep "
                     "arriving for ever", "correct": False,
             "why": "Only the light already in transit keeps coming, and "
                    "there are only about 8 minutes of it."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h02",
        "band": "harder",
        "text": "Two stars are photographed on the same night. Star X is 100 "
                "light years away and star Y is 3000. Which are you seeing "
                "further into the past, and by how much?",
        "options": [
            # ⊕ MRB-297 · 1 Sep 2026 — this was the only one of the four
            # with no reason attached, and so the shortest by a clear margin.
            # The reason is added; the claim itself is unchanged.
            {"text": "Star Y, by about 2900 years — 3000 minus 100",
             "correct": True},
            {"text": "Star X, by about 2900 years", "correct": False,
             "why": "The further star's light has been travelling longer, so "
                    "it shows an older scene. Star Y is the further one."},
            {"text": "Neither — both photographs show the sky as it is "
                     "tonight", "correct": False,
             "why": "Each star is seen as it was when its own light left, and "
                    "those two moments are 2900 years apart."},
            {"text": "Star Y, but only by the few minutes it takes light to "
                     "cross the telescope", "correct": False,
             "why": "The delay is set by the distance to the star, not by "
                    "anything inside the instrument."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h03",
        "band": "harder",
        "text": "A news report says a probe 'travelled two light years in "
                "eighteen months'. What is wrong with the sentence?",
        "options": [
            {"text": "Nothing — a light year is a distance and eighteen "
                     "months is a time, so the sentence is well formed",
             "correct": False,
             "why": "The sentence is well formed and the physics in it is "
                    "impossible: nothing carrying information can beat the "
                    "speed of light."},
            {"text": "Light years cannot be used for probes, only for stars",
             "correct": False,
             "why": "The unit works for any distance. It is simply an "
                    "awkward one for short journeys."},
            {"text": "It claims a speed faster than light, because light "
                     "itself needs two years to cover two light years",
             "correct": True},
            {"text": "Two light years is less than the distance to the "
                     "nearest star, so no probe would bother",
             "correct": False,
             "why": "It is indeed less than 4.24 light years, and that is a "
                    "point about the destination, not about the sentence."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h04",
        "band": "harder",
        "text": "A galaxy is 13 billion light years away and astronomers say "
                "studying it tells them about the early universe. Explain "
                "which statement below captures why.",
        "options": [
            {"text": "The galaxy is older than everything nearer to us, so it "
                     "has had longer to develop", "correct": False,
             "why": "It is not older. It is being SEEN younger, because its "
                    "light left it 13 billion years ago."},
            {"text": "The light arriving now left 13 billion years ago, so "
                     "the galaxy is seen as it was then", "correct": True},
            {"text": "Distant galaxies formed first, so they show what came "
                     "before everything else", "correct": False,
             "why": "Distance from us is not a fact about when a galaxy "
                    "formed. What it fixes is how old the LIGHT is."},
            {"text": "Light slows down over great distances, so it carries "
                     "older information", "correct": False,
             "why": "Light does not slow down. The delay comes from the "
                    "distance, at a speed that never varies."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p12-06-e05",
        "band": "easier",
        "text": "A light year measures…",
        "options": [
            {"text": "a length of time", "correct": False,
             "why": "The word year is misleading: it is how far light gets, "
                    "not how long it takes."},
            {"text": "a distance", "correct": True},
            {"text": "a speed", "correct": False,
             "why": "The speed of light is a separate quantity, in metres per "
                    "second."},
            {"text": "an amount of energy", "correct": False,
             "why": "Energy is in joules and has nothing to do with this "
                    "unit."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e06",
        "band": "easier",
        "text": "A star is 4 light years away. How long has the light "
                "entering your eye been travelling?",
        "options": [
            {"text": "4 seconds", "correct": False,
             "why": "In four seconds light covers about a billion metres, "
                    "nowhere near another star."},
            {"text": "4 years", "correct": True},
            {"text": "No time at all, because light is instant",
             "correct": False,
             "why": "Light is fast but not instant, which is what makes the "
                    "unit useful."},
            {"text": "4 million years", "correct": False,
             "why": "That would be a galaxy's distance, not a nearby star's."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e07",
        "band": "easier",
        "text": "Why are kilometres a poor unit for the distance to a star?",
        "options": [
            {"text": "Because kilometres cannot be used outside the "
                     "atmosphere",
             "correct": False,
             "why": "A kilometre is a kilometre anywhere; the difficulty is "
                    "the size of the numbers."},
            {"text": "Because the numbers become unmanageably large",
             "correct": True},
            {"text": "Because distances in space cannot be measured",
             "correct": False,
             "why": "They are measured routinely; the question is what unit "
                    "to report them in."},
            {"text": "Because light does not travel in kilometres",
             "correct": False,
             "why": "It covers kilometres perfectly well — about 300 000 of "
                    "them every second."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-e08",
        "band": "easier",
        "text": "Roughly how many metres is one light year?",
        "options": [
            {"text": "About 9.5 × 10^15 m", "correct": True},
            {"text": "About 3.0 × 10^8 m", "correct": False,
             "why": "That is how far light travels in one SECOND."},
            {"text": "About 9.5 × 10^9 m", "correct": False,
             "why": "That is about a million times too small — roughly the "
                    "distance to a nearby planet."},
            {"text": "About 300 000 m", "correct": False,
             "why": "That is 300 km, a distance you could drive in a few "
                    "hours."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p12-06-s05",
        "band": "standard",
        "text": "A signal takes 1.2 s to reach the Moon. How far away is it? "
                "Take the speed of light as 3.0 × 10^8 m/s.",
        "options": [
            {"text": "2.5 × 10^8 m", "correct": False,
             "why": "That is 3.0 × 10^8 ÷ 1.2; distance is speed MULTIPLIED "
                    "by time."},
            {"text": "3.6 × 10^8 m", "correct": True},
            {"text": "1.8 × 10^8 m", "correct": False,
             "why": "That halves the answer, as though the signal made a "
                    "round trip, and it does not."},
            {"text": "3.0 × 10^8 m", "correct": False,
             "why": "That is one second's worth, and the journey took 1.2 s."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s06",
        "band": "standard",
        "text": "A probe is 4.5 light hours from Earth. How long does a "
                "command take to reach it?",
        "options": [
            {"text": "4.5 seconds", "correct": False,
             "why": "The unit says light HOURS, so the journey takes hours, "
                    "not seconds."},
            {"text": "4.5 hours", "correct": True},
            {"text": "4.5 years", "correct": False,
             "why": "That would be a light-year distance, thousands of times "
                    "further out."},
            {"text": "No time at all, because radio is instant",
             "correct": False,
             "why": "Radio travels at the speed of light, which is fast but "
                    "not instant."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s07",
        "band": "standard",
        "text": "A star 100 light years away explodes today. When will people "
                "on Earth see it?",
        "options": [
            {"text": "Today, because the explosion is happening now",
             "correct": False,
             "why": "The light has to cross 100 light years before anyone "
                    "here can see it."},
            {"text": "In 100 years from today", "correct": True},
            {"text": "It happened 100 years ago and was seen then",
             "correct": False,
             "why": "The question says it explodes today, so the light has "
                    "not started its journey until now."},
            {"text": "Never, because the light will be too faint",
             "correct": False,
             "why": "An exploding star at that distance is easily bright "
                    "enough to see."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-s08",
        "band": "standard",
        "text": "Why does saying the Sun is eight light minutes away also "
                "tell you a distance?",
        "options": [
            {"text": "Because minutes and metres mean the same thing in "
                     "space",
             "correct": False,
             "why": "They are quite different quantities; what links them is "
                    "a fixed speed."},
            {"text": "Because distance = speed × time, and the speed of light "
                     "is fixed",
             "correct": True},
            {"text": "Because a light minute is a unit of time that "
                     "astronomers reuse",
             "correct": False,
             "why": "A light minute is a distance, which is exactly why the "
                    "statement works."},
            {"text": "Because the Sun's distance never changes",
             "correct": False,
             "why": "It varies a little through the year, and that is not "
                    "what makes the statement a distance."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p12-06-h05",
        "band": "harder",
        "text": "A spacecraft travels at a tenth of the speed of light. How "
                "long would it take to reach a star 4 light years away?",
        "options": [
            {"text": "4 years, because the star is 4 light years away",
             "correct": False,
             "why": "Only light itself covers a light year in a year; this "
                    "craft is ten times slower."},
            {"text": "40 years", "correct": True},
            {"text": "0.4 years", "correct": False,
             "why": "That divides by ten where the calculation multiplies; a "
                    "slower craft takes longer."},
            {"text": "It could never arrive", "correct": False,
             "why": "A tenth of light speed is fast but finite, so the "
                    "journey has a definite length."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h06",
        "band": "harder",
        "text": "Andromeda is 2.5 million light years away. If it vanished "
                "today, when would astronomers here know?",
        "options": [
            {"text": "Immediately, because gravity acts at once",
             "correct": False,
             "why": "Nothing carries the news faster than light, gravity "
                    "included."},
            {"text": "In 2.5 million years", "correct": True},
            {"text": "2.5 million years ago", "correct": False,
             "why": "That is when the light now arriving set out; the "
                    "vanishing has not been seen yet."},
            {"text": "In 2.5 million seconds", "correct": False,
             "why": "That is about a month, and the distance is stated in "
                    "light YEARS."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h07",
        "band": "harder",
        "text": "Why does knowing a star is 4 light years away NOT tell you "
                "how long a journey there would take?",
        "options": [
            {"text": "Because nothing we can build travels anywhere near the "
                     "speed of light",
             "correct": True},
            {"text": "Because a light year is a time, so it cannot give a "
                     "distance",
             "correct": False,
             "why": "It is a distance, which is exactly why a journey time "
                    "needs a speed as well."},
            {"text": "Because the star will have moved by the time you "
                     "arrive",
             "correct": False,
             "why": "It does move, but the reason the four years does not "
                    "apply is the speed of the craft."},
            {"text": "Because distances in space cannot be converted into "
                     "times at all",
             "correct": False,
             "why": "They can, once a speed is known — which is the whole "
                    "point."},
        ],
        "figure": None,
    },
    {
        "id": "p12-06-h08",
        "band": "harder",
        "text": "Why is every observation of a distant object an observation "
                "of the past?",
        "options": [
            {"text": "Because telescopes record images and play them back "
                     "later",
             "correct": False,
             "why": "It is true of the naked eye as well, with no recording "
                    "involved."},
            {"text": "Because light takes time to arrive, and the further "
                     "away the longer",
             "correct": True},
            {"text": "Because distant objects move so slowly that they look "
                     "frozen",
             "correct": False,
             "why": "Their speed is not the issue; the travel time of the "
                    "light is."},
            {"text": "Because the atmosphere delays the light as it arrives",
             "correct": False,
             "why": "The atmosphere adds a fraction of a millisecond, against "
                    "years or millennia of travel."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ─────────────────────────────────────────
    {
            "id": 'p12-06-e09',
            "band": 'easier',
            "text": 'What is the exact speed of light in a vacuum, more precise than the rounded 3.0 × 10^8 m/s used in calculations?',
            "options": [
                {"text": '299 792 458 m/s', "correct": True},
                {"text": '299 000 000 m/s', "correct": False, "why": 'Close, but the true figure has more digits than that rounded form.'},
                {"text": '300 792 458 m/s', "correct": False, "why": 'The first three digits are wrong; the real figure starts 299, not 300.'},
                {"text": '289 792 458 m/s', "correct": False, "why": 'The middle digits are wrong; the real figure starts 299, not 289.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e10',
            "band": 'easier',
            "text": 'Voyager 1, the most distant human-made object, is about 22 light hours from Earth. Proxima Centauri is 4.24 light years away. Which is the greater distance?',
            "options": [
                {"text": 'Proxima Centauri, by an enormous margin', "correct": True},
                {"text": 'Voyager 1, because 22 is the bigger number', "correct": False, "why": 'The number alone settles nothing: a light year is thousands of times larger than a light hour.'},
                {"text": 'They are about the same distance', "correct": False, "why": 'A light year is about 8 800 light hours, so 4.24 light years dwarfs 22 light hours.'},
                {"text": 'Neither, because hours and years cannot be compared', "correct": False, "why": 'Both are distances built from the same fixed speed, so they compare perfectly well.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e11',
            "band": 'easier',
            "text": 'Roughly how long would a full round trip take for a radio signal to Voyager 1 and back, if Voyager is 22 light hours away?',
            "options": [
                {"text": 'About 11 hours', "correct": False, "why": 'That halves the one-way time; a round trip is twice the one-way time, not half.'},
                {"text": 'About 22 hours', "correct": False, "why": 'That is only the one-way time. The signal has to come back too.'},
                {"text": 'About 44 hours', "correct": True},
                {"text": 'About 22 minutes', "correct": False, "why": 'That drops the round trip down to minutes, far too short for a 22-light-hour distance each way.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e12',
            "band": 'easier',
            "text": "A light-time unit is built by taking a length of TIME and asking how far light travels in it. Why is there no such unit as a 'light metre'?",
            "options": [
                {"text": 'Light travels too fast for a metre to be a useful unit', "correct": False, "why": 'Usefulness is not the issue; a light-time unit has to start from a time, and a metre is not one.'},
                {"text": 'A metre is already a distance, not a length of time', "correct": True},
                {"text": 'A metre is far too small a unit for astronomers to work with', "correct": False, "why": 'Astronomers use metres constantly; the reason is that a metre measures distance, not time.'},
                {"text": 'Light cannot cross a distance as short as a single metre', "correct": False, "why": 'Light crosses a metre in a few billionths of a second; the problem is that a metre is not a time.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e13',
            "band": 'easier',
            "text": 'The fastest object humans have ever launched would take about how long to reach Proxima Centauri, 4.24 light years away?',
            "options": [
                {"text": 'About 70 000 years', "correct": True},
                {"text": 'About 70 years', "correct": False, "why": 'That is a thousand times too quick for any spacecraft humans have actually built.'},
                {"text": 'About 4.24 years', "correct": False, "why": 'That is the time light itself takes, and nothing built by humans travels anywhere near that fast.'},
                {"text": 'About 700 000 years', "correct": False, "why": 'That overshoots the real estimate by a factor of ten.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e14',
            "band": 'easier',
            "text": 'Why is the speed of light called a fundamental limit, rather than just a very fast speed nobody has beaten yet?',
            "options": [
                {"text": 'Engineers have simply not tried hard enough to beat it', "correct": False, "why": 'The limit is not a matter of effort; it comes from how space and time themselves are structured.'},
                {"text": 'It is built into the structure of space and time itself', "correct": True},
                {"text": 'It is the fastest speed any animal has been recorded moving at', "correct": False, "why": 'Animal speeds are far below it and have nothing to do with why it is a fundamental limit.'},
                {"text": 'It is simply the current world record for a vehicle', "correct": False, "why": 'A world record can be broken later; this limit cannot be, whatever gets built.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e15',
            "band": 'easier',
            "text": "Neptune's light-travel time of about 15 000 seconds is described as a mean figure. Why a mean, rather than one fixed number?",
            "options": [
                {"text": 'The speed of light itself varies slightly from day to day', "correct": False, "why": 'The speed of light is fixed; it is the DISTANCE that varies here, not the speed.'},
                {"text": 'Neptune keeps changing its own speed of rotation', "correct": False, "why": "Neptune's spin has nothing to do with its distance from Earth."},
                {"text": "Neptune's distance from Earth varies through the year", "correct": True},
                {"text": "Astronomers have not yet measured Neptune's distance precisely", "correct": False, "why": 'The distance is measured very precisely; it genuinely changes because both planets are orbiting.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e16',
            "band": 'easier',
            "text": 'A formula triangle shows d over c and t. Which rearrangement finds the TIME, given a distance and a speed?',
            "options": [
                {"text": 't = c × d ÷ 2', "correct": False, "why": 'There is no halving anywhere in this triangle; the extra division by two does not belong.'},
                {"text": 't = d × c', "correct": False, "why": 'Two things side by side on the triangle multiply; d and c sit apart with a dividing line, so this row divides instead.'},
                {"text": 't = c ÷ d', "correct": False, "why": 'That has the division the wrong way round; d sits on top of the triangle, so it is d that gets divided.'},
                {"text": 't = d ÷ c', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e17',
            "band": 'easier',
            "text": 'You know how far something travelled and how long it took. Which rearrangement of the triangle works out its speed?',
            "options": [
                {"text": 'c = d ÷ t', "correct": True},
                {"text": 'c = d + t', "correct": False, "why": 'A formula triangle never adds two quantities together; it only multiplies or divides.'},
                {"text": 'c = t ÷ d', "correct": False, "why": 'That divides the wrong quantity by the other; d sits on top, so it is d that gets divided by t.'},
                {"text": 'c = d × t', "correct": False, "why": 'Multiplying d and t together gives neither a speed nor anything meaningful here.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e18',
            "band": 'easier',
            "text": "Andromeda's light has been travelling for about 2.5 million years. Roughly how many light years away is Andromeda?",
            "options": [
                {"text": 'About 2.5 light years', "correct": False, "why": "That drops the 'million' entirely, leaving a figure far too small for Andromeda."},
                {"text": 'About 2.5 million light years', "correct": True},
                {"text": 'About 2.5 billion light years', "correct": False, "why": 'That is a thousand times too far for Andromeda, which sits far closer than that.'},
                {"text": 'About 25 000 light years', "correct": False, "why": "That is a hundred times too close, well short of Andromeda's real distance."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e19',
            "band": 'easier',
            "text": 'Which travels faster through a vacuum: a radio signal sent to a spacecraft, or visible light from a star?',
            "options": [
                {"text": 'The radio signal, because it is sent deliberately', "correct": False, "why": 'Being sent on purpose does not change a speed; both are electromagnetic waves.'},
                {"text": 'The visible light, because we can see it', "correct": False, "why": 'Being visible has nothing to do with speed; both cross a vacuum at the same rate.'},
                {"text": 'Neither — both travel at the same speed in a vacuum', "correct": True},
                {"text": 'The radio signal, because radio waves are longer', "correct": False, "why": 'Wavelength differs, but every electromagnetic wave crosses a vacuum at one fixed speed.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e20',
            "band": 'easier',
            "text": 'The Moon, Neptune and Mars are each given a MEAN distance from Earth rather than one fixed value. Why might that be, for objects orbiting the Sun or the Earth?',
            "options": [
                {"text": 'Astronomers round every figure for convenience, whether it varies or not', "correct": False, "why": 'The rounding here reflects a real physical change in distance, not just tidier arithmetic.'},
                {"text": 'Their distances have not yet been measured', "correct": False, "why": 'Their distances are measured very precisely; the issue is that the true value keeps changing.'},
                {"text": 'The speed of light itself changes near each of these objects', "correct": False, "why": 'The speed of light is the same everywhere in a vacuum; it is the distance that varies here.'},
                {"text": 'Orbiting bodies keep changing their separation', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e21',
            "band": 'easier',
            "text": "Why does a stated light-travel time, such as '8.3 light minutes to the Sun', always describe a distance and never just a wait?",
            "options": [
                {"text": 'Because the speed of light is fixed, converting time directly into distance', "correct": True},
                {"text": 'Because the Sun is the object this rule applies to', "correct": False, "why": "The same rule applies to every light-time figure of this kind, not just the Sun's."},
                {"text": 'Because minutes are secretly a unit of distance in astronomy', "correct": False, "why": "A minute is a unit of time; it is the word 'light' in front of it that adds the distance meaning."},
                {"text": 'Because the figure is simply a rounding of the true distance in kilometres', "correct": False, "why": 'It is not a rounding of a kilometre figure; it comes directly from how long light takes, times its speed.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e22',
            "band": 'easier',
            "text": 'A student says light takes exactly the same time to reach every planet in the solar system. Is that correct?',
            "options": [
                {"text": 'Yes — the speed of light makes every distance take the same time to cross', "correct": False, "why": 'The speed is the same everywhere, but the distances differ hugely, so the travel TIMES differ too.'},
                {"text": 'No — closer planets have shorter light-travel times', "correct": True},
                {"text": 'Yes — every planet sits the same distance from Earth at every moment', "correct": False, "why": 'Planets sit at very different distances from Earth, which is exactly why their light-travel times differ.'},
                {"text": 'No — light does not reach some planets', "correct": False, "why": 'Light reaches every planet in the solar system; it simply takes different amounts of time to arrive.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e23',
            "band": 'easier',
            "text": 'Roughly how many light seconds away is the Moon?',
            "options": [
                {"text": 'About 130 light seconds', "correct": False, "why": 'That is a hundred times too far; light takes barely more than a second to reach the Moon.'},
                {"text": 'About 13 light seconds', "correct": False, "why": "That is ten times too far for the Moon's real distance in light-time."},
                {"text": 'About 1.3 light seconds', "correct": True},
                {"text": 'About 0.13 light seconds', "correct": False, "why": "That is ten times too close for the Moon's real light-travel time."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e24',
            "band": 'easier',
            "text": 'Which of these light-time units describes the LARGEST distance?',
            "options": [
                {"text": 'A light second', "correct": False, "why": 'A light second is the smallest of the four listed here.'},
                {"text": 'A light minute', "correct": False, "why": 'A light minute is sixty times a light second, but still far short of the largest option here.'},
                {"text": 'A light hour', "correct": False, "why": 'A light hour is bigger than a light minute, but a light year is bigger still.'},
                {"text": 'A light year', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e25',
            "band": 'easier',
            "text": 'Put these in order, smallest first: a light hour, a light second, a light year, a light minute.',
            "options": [
                {"text": 'Light second, light minute, light hour, light year', "correct": True},
                {"text": 'Light year, light hour, light minute, light second', "correct": False, "why": 'That runs from largest to smallest, the exact reverse of what was asked.'},
                {"text": 'Light minute, light second, light year, light hour', "correct": False, "why": 'A light second is smaller than a light minute, so the first two are the wrong way round.'},
                {"text": 'Light second, light hour, light minute, light year', "correct": False, "why": 'A light hour is bigger than a light minute, so those two are out of order.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e26',
            "band": 'easier',
            "text": 'Does the exact speed of light, 299 792 458 m/s, ever change depending on which direction light travels in a vacuum?',
            "options": [
                {"text": 'Yes — light travels faster moving away from the Sun than towards it', "correct": False, "why": 'The speed of light in a vacuum does not depend on direction relative to the Sun or anything else.'},
                {"text": 'No — the value stays the same whichever way light travels', "correct": True},
                {"text": 'Yes — light slows down whenever it travels towards Earth', "correct": False, "why": 'Approaching Earth makes no difference to the speed of light in a vacuum.'},
                {"text": 'It has not yet been measured in more than one direction', "correct": False, "why": 'It has been measured carefully in many directions, and it comes out the same every time.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e27',
            "band": 'easier',
            "text": 'A spacecraft is sent a command and confirms receiving it some time later. What must have happened to the confirmation signal in between?',
            "options": [
                {"text": 'It travelled back faster than the original command did', "correct": False, "why": 'Both signals are radio waves travelling at the same fixed speed of light.'},
                {"text": 'It arrived back on Earth the same instant it was sent', "correct": False, "why": 'Nothing, including a confirmation signal, arrives instantly across any real distance.'},
                {"text": 'It travelled back to Earth at the speed of light', "correct": True},
                {"text": 'It did not need to travel anywhere', "correct": False, "why": 'A confirmation has to physically cross the distance back to Earth, the same as any other signal.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e28',
            "band": 'easier',
            "text": 'Which statement correctly links distance, speed and time for something travelling at a constant speed?',
            "options": [
                {"text": 'Distance equals time divided by speed', "correct": False, "why": 'Dividing a time by a speed gives no distance at all; a distance needs the speed multiplied by the time.'},
                {"text": 'Distance equals speed divided by time', "correct": False, "why": 'Dividing speed by time does not give a distance; the correct relationship multiplies them instead.'},
                {"text": 'Distance equals speed minus time', "correct": False, "why": 'Speed and time measure different things and cannot simply be subtracted from one another.'},
                {"text": 'Distance equals speed multiplied by time', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e29',
            "band": 'easier',
            "text": 'Which one of these quantities would be given in light years?',
            "options": [
                {"text": 'The distance from Earth out to a distant star', "correct": True},
                {"text": 'The age of a star, in years', "correct": False, "why": 'An age is a length of time and is given in plain years; a light year is a distance.'},
                {"text": 'How bright a star looks', "correct": False, "why": 'Brightness is not a distance, so it is never given in light years.'},
                {"text": 'The temperature of a star', "correct": False, "why": 'A temperature is measured in degrees, never in a unit of distance.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-e30',
            "band": 'easier',
            "text": "Why can a light-time figure such as '4.24 light years' double up as both a distance AND an age for the light?",
            "options": [
                {"text": 'Because 4.24 happens to be both a distance in kilometres and a count of years by coincidence', "correct": False, "why": 'It is not a coincidence of numbers; it follows directly from the fixed speed of light.'},
                {"text": 'Because the fixed speed of light links distance and travel time together', "correct": True},
                {"text": "Because astronomers redefine the word 'year' for each different star", "correct": False, "why": "A year keeps its ordinary meaning; what changes is how the word 'light' is attached in front of it."},
                {"text": 'Because light itself ages differently depending on which star it comes from', "correct": False, "why": 'Light does not age at different rates; every light-year figure works the same fixed way.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s09',
            "band": 'standard',
            "text": 'Voyager 1 is about 22 light hours from Earth. Roughly how many kilometres is that? Take the speed of light as 3.0 × 10^8 m/s.',
            "options": [
                {"text": 'About 2.4 × 10^10 km', "correct": True},
                {"text": 'About 2.4 × 10^7 km', "correct": False, "why": 'That is a thousand times too small — the slip made by converting the metres to kilometres twice over.'},
                {"text": 'About 2.4 × 10^13 km', "correct": False, "why": 'That is a thousand times too large for the distance described here.'},
                {"text": 'About 22 × 3.0 × 10^8 km', "correct": False, "why": 'That multiplies hours directly by a speed given per second, without converting the hours first.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s10',
            "band": 'standard',
            "text": 'A calculation uses the rounded 3.0 × 10^8 m/s in place of the exact 299 792 458 m/s. Roughly how far out will the answer be?',
            "options": [
                {"text": 'About 1% out', "correct": False, "why": 'The two figures agree to three significant figures, so the gap is well under 1%.'},
                {"text": 'About 10% out', "correct": False, "why": '300 000 000 and 299 792 458 differ by about 200 000, nowhere near a tenth of the value.'},
                {"text": 'Less than 0.1% out', "correct": True},
                {"text": 'About 25% out', "correct": False, "why": 'A quarter of the speed of light is some 75 000 000 m/s; the two figures are nothing like that far apart.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s11',
            "band": 'standard',
            "text": 'The Moon is about 1.28 light seconds away and Neptune about 15 000 light seconds away. Roughly how many times further is Neptune?',
            "options": [
                {"text": 'About 1 200 000 times further', "correct": False, "why": 'That overshoots the true ratio by a factor of a hundred.'},
                {"text": 'About 120 times further', "correct": False, "why": 'That divides by a hundred too many, giving a ratio far too small.'},
                {"text": 'About 12 000 times further', "correct": True},
                {"text": 'About 12 times further', "correct": False, "why": 'That divides by a thousand too many, giving a ratio far too small.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s12',
            "band": 'standard',
            "text": "Andromeda's light has travelled for about 2.5 million years. Roughly how many SECONDS is that, given a year is about 3.15 × 10^7 seconds?",
            "options": [
                {"text": 'About 7.9 × 10^16 s', "correct": False, "why": 'That overshoots the correct figure by a factor of a thousand.'},
                {"text": 'About 7.9 × 10^10 s', "correct": False, "why": 'That leaves out a factor of a thousand from the million years being converted.'},
                {"text": 'About 3.15 × 10^7 s', "correct": False, "why": 'That is just the seconds in ONE year, not in 2.5 million of them.'},
                {"text": 'About 7.9 × 10^13 s', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s13',
            "band": 'standard',
            "text": 'At its closest, Mars sits about 4 light minutes from Earth. Roughly how many kilometres is that, using 3.0 × 10^8 m/s for light?',
            "options": [
                {"text": 'About 7.2 × 10^7 km', "correct": True},
                {"text": 'About 7.2 × 10^4 km', "correct": False, "why": 'That is a thousand times too small — the slip made by dividing metres by a thousand twice over.'},
                {"text": 'About 1.2 × 10^7 km', "correct": False, "why": 'That uses 40 seconds rather than the 240 seconds in four minutes, so it comes out six times too small.'},
                {"text": 'About 4 × 3.0 × 10^8 km', "correct": False, "why": 'That multiplies minutes directly by a speed given per second, without converting the minutes first.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s14',
            "band": 'standard',
            "text": 'A student says the exact speed of light, 299 792 458 m/s, must have been rounded from 300 000 000 m/s for tidiness. What is wrong with that idea?',
            "options": [
                {"text": 'The idea is correct — the rounder figure is the true one and the longer figure is a mistake', "correct": False, "why": 'The precise figure is the genuine one; the round number is the simplified version used in class.'},
                {"text": 'The exact figure is the more fundamental one', "correct": True},
                {"text": 'Neither figure is accurate, and the real value is still completely unknown', "correct": False, "why": 'The precise value is very well established; it is not an unknown quantity at all.'},
                {"text": 'The two figures describe two different physical constants entirely', "correct": False, "why": 'Both figures describe the same constant, the speed of light — one exact, one rounded for convenience.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s15',
            "band": 'standard',
            "text": "Why does describing the fastest human-made object's journey to Proxima Centauri as '70 000 years' make the case for interstellar travel being hard, better than just saying 'it is far away'?",
            "options": [
                {"text": 'The two phrases mean exactly the same thing to a reader', "correct": False, "why": 'A concrete number carries far more information than a vague phrase, even about the same underlying fact.'},
                {"text": "Saying 'far away' is more precise than a number of years", "correct": False, "why": "A specific figure of years is more precise and more concrete than a vague phrase like 'far away'."},
                {"text": 'A concrete number of years shows how impractical the journey would be', "correct": True},
                {"text": "The number of years describes the cost, not the journey", "correct": False, "why": '70 000 years is a journey TIME here, unconnected to any cost figure for building the spacecraft.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s16',
            "band": 'standard',
            "text": 'Two spacecraft signals are sent, one crossing 4 light minutes and one crossing 22 light hours. Which takes longer to arrive, and by roughly what factor?',
            "options": [
                {"text": 'It cannot be judged without knowing which spacecraft sent which signal', "correct": False, "why": 'The light-time figures alone already fix which signal takes longer to arrive.'},
                {"text": 'The 4-light-minute signal, by a factor of a few hundred', "correct": False, "why": 'The far LONGER light-time journey is the slower one to arrive, not the shorter one.'},
                {"text": 'Both signals arrive in almost exactly the same time', "correct": False, "why": '22 hours is hundreds of times longer than 4 minutes, so the arrival times differ enormously.'},
                {"text": 'The 22-light-hour signal, by a factor of a few hundred', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s17',
            "band": 'standard',
            "text": "A pupil says the Moon's 1.28-second light-travel time and Neptune's 15 000-second figure cannot really be compared, since one is 'basically instant' and one is not. Why is that framing misleading?",
            "options": [
                {"text": 'Both are still real, measurable delays, just of very different sizes', "correct": True},
                {"text": 'The framing is right — a delay that short is not a delay', "correct": False, "why": "1.28 seconds is a real, measurable delay; it is simply far shorter than Neptune's."},
                {"text": "Neptune's figure is not a delay either, since light seems instant to the naked eye", "correct": False, "why": "Neptune's 15 000-second delay is a genuine, measurable travel time, not an illusion."},
                {"text": 'The two figures use completely different physical processes to travel', "correct": False, "why": 'Both are ordinary light, travelling at the same fixed speed; only the distance differs.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s18',
            "band": 'standard',
            "text": "Explain why Neptune's distance being described as a MEAN does not mean the 15 000-second figure is unreliable.",
            "options": [
                {"text": 'It does mean the figure is unreliable, since a mean is nothing more than a rough guess', "correct": False, "why": 'A mean can be calculated precisely from real measurements; it is not the same as a rough guess.'},
                {"text": 'A mean can still be a well-measured, useful figure', "correct": True},
                {"text": "Neptune's true distance is fixed, so calling it a mean is simply an error", "correct": False, "why": "Neptune's distance genuinely varies as both planets orbit, so a mean is the appropriate figure to give."},
                {"text": "The word 'mean' here refers to the speed of light, not to Neptune's distance", "correct": False, "why": "The speed of light is fixed; it is Neptune's distance that varies and is being averaged."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s19',
            "band": 'standard',
            "text": "A student argues that because light seems instantaneous in everyday life, the 'light takes time' idea must only apply out in space. Why is that argument wrong?",
            "options": [
                {"text": "Light has no fixed speed until it leaves Earth's atmosphere and reaches space", "correct": False, "why": 'The same fixed speed applies everywhere, inside the atmosphere and in space alike.'},
                {"text": 'The argument is correct — light is instantaneous over short, everyday distances', "correct": False, "why": 'Light still takes a real, non-zero time even over short distances; it is simply too brief to notice.'},
                {"text": 'Light takes time everywhere; everyday delays are simply too small to notice', "correct": True},
                {"text": 'Everyday light and starlight are two different kinds of light with different rules', "correct": False, "why": 'It is the same phenomenon, light, following the same fixed speed in both cases.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s20',
            "band": 'standard',
            "text": "Why does saying the speed of light 'is built into the structure of space and time' mean something stronger than saying it is simply the current speed record?",
            "options": [
                {"text": 'It means the figure is a rough estimate, waiting to be refined', "correct": False, "why": 'The figure is extremely precisely known; the stronger claim is about the limit, not its precision.'},
                {"text": 'It means exactly the same thing, just phrased more dramatically for effect', "correct": False, "why": 'The two phrasings describe genuinely different kinds of claim, not the same idea dressed up.'},
                {"text": 'It means the speed of light will eventually be exceeded once engineering improves enough', "correct": False, "why": 'Being built into the structure of space and time is exactly what rules out it ever being exceeded.'},
                {"text": 'A record can be broken later; this limit cannot be broken by any technology', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s21',
            "band": 'standard',
            "text": 'A satellite sends a signal that takes 0.1 s to reach a receiver 3.0 × 10^7 m away. Does this match the speed of light?',
            "options": [
                {"text": 'Yes — dividing the distance by the time gives 3.0 × 10^8 m/s', "correct": True},
                {"text": 'No — dividing gives a speed a hundred times too slow for light', "correct": False, "why": "3.0 × 10^7 divided by 0.1 comes to 3.0 × 10^8 m/s, which does match light's speed."},
                {"text": 'No — the numbers describe a speed far faster than light is able to travel', "correct": False, "why": "The resulting speed is exactly light's own speed, not faster than it."},
                {"text": 'It cannot be checked without knowing the direction of travel', "correct": False, "why": 'Speed here only needs the distance and the time; direction makes no difference to the calculation.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s22',
            "band": 'standard',
            "text": 'A pupil says any light-time figure, such as a distance to a star, could just as well be written in kilometres instead. What would be lost by doing that?',
            "options": [
                {"text": 'Nothing would be lost; the two ways of writing it are interchangeable', "correct": False, "why": 'Writing only kilometres drops the built-in sense of how long ago the light set out.'},
                {"text": 'The instant sense of how old the light is would completely disappear from view', "correct": True},
                {"text": 'The distance itself would become smaller once converted to kilometres', "correct": False, "why": 'Converting units changes how a distance is WRITTEN, not the actual distance itself.'},
                {"text": 'It would become impossible to work out the speed of light afterwards', "correct": False, "why": 'The speed of light is a separate, fixed fact that does not depend on which unit a distance is given in.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s23',
            "band": 'standard',
            "text": "Why is 'the comet will arrive in three light years' a more serious error than simply an awkward choice of words?",
            "options": [
                {"text": 'The mistake is that comets cannot travel three light years in any amount of time', "correct": False, "why": 'A comet could plausibly be three light years away; the error is calling that figure an arrival time.'},
                {"text": 'It is awkward wording, with no actual error in the physics behind it', "correct": False, "why": 'Treating a distance as a time is a genuine mistake, not merely clumsy phrasing.'},
                {"text": 'It quietly turns a distance figure into a false claimed arrival time', "correct": True},
                {"text": "The error is using 'light years' for a comet instead of for a star", "correct": False, "why": 'Light years can describe the distance to any object; the error is treating it as a time.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s24',
            "band": 'standard',
            "text": 'Explain why two objects at very different distances can both be described using a light-time figure, even though one might be a planet and the other a galaxy.',
            "options": [
                {"text": 'A light-time figure works for objects that are themselves shining, not reflecting light', "correct": False, "why": 'A reflecting object like the Moon is measured in light-time exactly as a shining one is.'},
                {"text": 'Planets and galaxies happen to use two different definitions of the light year', "correct": False, "why": 'The light year, and every light-time unit, is defined identically whatever kind of object it measures.'},
                {"text": 'Only objects beyond the solar system can properly be measured in light-time units', "correct": False, "why": 'Nearby objects, like Mars or the Moon, are routinely measured in light-time units too.'},
                {"text": 'The same fixed speed of light links a travel time to a distance for any object', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s25',
            "band": 'standard',
            "text": "A pupil calculates a spacecraft's distance using d = c × t but forgets to convert minutes into seconds first. What happens to their final answer?",
            "options": [
                {"text": 'It comes out sixty times smaller than the correct distance', "correct": True},
                {"text": 'It comes out sixty times larger than the correct distance', "correct": False, "why": 'Leaving minutes unconverted UNDERCOUNTS the time in seconds, which makes the answer too small, not too large.'},
                {"text": 'The final answer is unaffected either way', "correct": False, "why": 'Using the wrong units for time changes the result by a clear, predictable factor.'},
                {"text": 'The calculation becomes impossible to complete', "correct": False, "why": 'The calculation still produces a number; it is simply the wrong one, by a factor of sixty.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s26',
            "band": 'standard',
            "text": "Explain why astronomers give Andromeda's distance in light years rather than switching to light-minute figures like those used for Mars.",
            "options": [
                {"text": 'Light-minute figures are reserved for objects inside the solar system', "correct": False, "why": 'There is no such rule; the real reason is simply which unit keeps the number of digits manageable.'},
                {"text": 'A light-minute count for Andromeda would run to an enormous, unmanageable number of digits', "correct": True},
                {"text": "Andromeda's light does not travel in light-minutes the way Mars's does", "correct": False, "why": 'The same light, at the same fixed speed, could in principle be measured in any of these units.'},
                {"text": 'Light years apply to galaxies alone, not to individual stars or planets', "correct": False, "why": 'Light years are used for stars too, such as Proxima Centauri, not only for galaxies.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s27',
            "band": 'standard',
            "text": 'A pupil says the round-trip time to Voyager 1 (about 44 hours) means Voyager itself takes 44 hours to move anywhere. What is the confusion?',
            "options": [
                {"text": 'The confusion is that Voyager cannot send signals', "correct": False, "why": 'Voyager does send and receive signals; the mix-up is about what the 44 hours actually measures.'},
                {"text": "There is no confusion — the statement correctly describes Voyager's speed", "correct": False, "why": "44 hours times light's own speed describes a signal's round trip, not Voyager's motion at all."},
                {"text": "The 44 hours describes a SIGNAL'S travel time, not how fast Voyager itself moves", "correct": True},
                {"text": 'The confusion is that round trips are always instant for any spacecraft', "correct": False, "why": 'A round trip takes a real amount of time, set by the distance and the fixed speed of light.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s28',
            "band": 'standard',
            "text": "Why would a value of 'the speed of light varies by season' be a far more serious claim than 'Neptune's distance varies by season'?",
            "options": [
                {"text": 'Neither claim would matter much; both are minor details', "correct": False, "why": 'A varying speed of light would overturn a fundamental constant, which is far from minor.'},
                {"text": 'Both claims are equally ordinary in astronomy', "correct": False, "why": 'One describes an ordinary orbital fact; the other would overturn a fixed constant of nature.'},
                {"text": "Neptune's distance is the one figure here that stays fixed", "correct": False, "why": "Neptune's distance is exactly the one that DOES change, as both planets orbit the Sun."},
                {"text": 'The speed of light is fixed; orbital distances are expected to vary', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s29',
            "band": 'standard',
            "text": "Explain why '4 light minutes' and '4 minutes' are not interchangeable phrases, even though both use the word 'minutes'.",
            "options": [
                {"text": "'Light minutes' names a distance; plain minutes names a length of time", "correct": True},
                {"text": "They are interchangeable, and the word 'light' adds nothing extra to the meaning", "correct": False, "why": "Adding 'light' changes the quantity being described entirely, from a time into a distance."},
                {"text": "'4 light minutes' is simply a more formal way of writing '4 minutes'", "correct": False, "why": 'They describe two different kinds of quantity, not two levels of formality for the same one.'},
                {"text": 'The difference matters for professional astronomers, not for ordinary use', "correct": False, "why": 'The distinction matters for correctly understanding any distance given this way, not only for professionals.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-s30',
            "band": 'standard',
            "text": 'A pupil says that because a light-minute is smaller than a light year, distances given in light-minutes must always be less accurate. Why is that reasoning flawed?',
            "options": [
                {"text": 'The reasoning is sound — smaller units are always less accurate than larger ones', "correct": False, "why": "A unit's size and the accuracy of a measurement made in it are two completely separate things."},
                {"text": 'The SIZE of a unit says nothing about how ACCURATELY a distance in that unit has been measured', "correct": True},
                {"text": "Light-minutes are in fact bigger than light years, reversing the pupil's comparison", "correct": False, "why": "A light year is the bigger unit; the pupil's comparison of sizes is correct, only the conclusion about accuracy is wrong."},
                {"text": 'Accuracy is a concept that applies solely to distances measured in kilometres, not in light-time units', "correct": False, "why": 'A distance in any unit, light-time or kilometres, can be measured to a stated accuracy.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h09',
            "band": 'harder',
            "text": "Voyager 1 is about 22 light hours away. A command is sent and Voyager's confirmation is received 44 hours later. What does that confirm about the round trip?",
            "options": [
                {"text": 'The outward and return legs of the signal together took the full 44 hours', "correct": True},
                {"text": 'Voyager must have moved much closer to Earth during the round trip', "correct": False, "why": '44 hours is exactly what two 22-hour crossings predict; no closer approach is needed to explain it.'},
                {"text": 'The confirmation signal must have travelled faster than the original command', "correct": False, "why": 'Both signals travel at the same fixed speed of light; the total time is simply two legs added together.'},
                {"text": 'Something delayed the signal well beyond what light-speed travel alone predicts', "correct": False, "why": '44 hours is exactly what plain light-speed travel over two 22-hour legs predicts, with no extra delay.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h10',
            "band": 'harder',
            "text": "A pupil argues that because light 'seems instant' when a torch is switched on in a dark room, light must actually travel infinitely fast over short distances. Refute this using the fixed speed of light.",
            "options": [
                {"text": 'The pupil is correct; light becomes infinitely fast once a distance is small enough', "correct": False, "why": 'The speed of light does not change with distance; it is the same fixed value at every scale.'},
                {"text": 'Light still takes a real, calculable time to cross the room', "correct": True},
                {"text": 'Torchlight is a special, faster kind of light unlike starlight', "correct": False, "why": 'Torchlight and starlight are the same phenomenon, travelling at the same fixed speed.'},
                {"text": 'The speed of light applies once light leaves a room and reaches open space', "correct": False, "why": 'The same fixed speed applies inside a room exactly as it does out in space.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h11',
            "band": 'harder',
            "text": 'Suppose the exact speed of light were found to be 300 000 000 m/s precisely, with no extra digits at all. What would that mean for the 299 792 458 m/s figure used today?',
            "options": [
                {"text": 'Both figures would become simultaneously correct at once', "correct": False, "why": 'Two different numbers for the same physical constant cannot both be correct together.'},
                {"text": 'It would stay exactly as it is, since the two figures already agree perfectly', "correct": False, "why": '299 792 458 and 300 000 000 are different numbers; a genuine change would force a real revision.'},
                {"text": 'It would have to be revised to match the new measured value', "correct": True},
                {"text": 'No other calculation built on that figure would need to change as a result', "correct": False, "why": 'Every calculation built on the old figure would shift slightly if the true value were different.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h12',
            "band": 'harder',
            "text": "A student claims that since Neptune's distance is only a mean, no single measurement taken on any real day could ever match 15 000 seconds exactly. Assess that claim.",
            "options": [
                {"text": 'The claim cannot be assessed, since a mean carries no useful information', "correct": False, "why": 'A mean is a genuinely useful, well-defined summary figure, even though it will not exactly match every single day.'},
                {"text": "Entirely wrong — every day's measurement must exactly equal the mean figure", "correct": False, "why": "A mean is calculated across many different days' values; individual days can and do differ from it."},
                {"text": "Entirely wrong — Neptune's real distance stays fixed from day to day", "correct": False, "why": "Neptune's distance genuinely changes continuously as both planets orbit the Sun."},
                {"text": 'Broadly right — a real measurement will typically sit close to the mean', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h13',
            "band": 'harder',
            "text": "A pupil argues: 'Since Andromeda is 2.5 million light years away, and the fastest human probe would take 70 000 years just to reach the NEAREST star, humanity could never send anything to Andromeda.' Evaluate this.",
            "options": [
                {"text": "The comparison strongly supports the pupil's conclusion", "correct": True},
                {"text": 'The comparison is meaningless, since the two distances cannot be placed on the same scale', "correct": False, "why": 'Both distances are ordinary lengths and can be compared directly; the comparison is meaningful.'},
                {"text": "The pupil's numbers must be wrong, since 70 000 years already sounds far too long for a nearby star", "correct": False, "why": '70 000 years to the nearest star is a well-established estimate and stands correctly.'},
                {"text": 'The comparison shows Andromeda is easier to reach than the nearest star', "correct": False, "why": 'Andromeda is millions of times further than the nearest star, making it far harder to reach, not easier.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h14',
            "band": 'harder',
            "text": "Two photographs are taken at the same instant: one of Mars (4 light minutes away) and one of Andromeda (2.5 million light years away). Explain why 'the same instant' does not mean 'the same age of light'.",
            "options": [
                {"text": 'Both photographs must show light of exactly the same age, since they were taken at the same instant', "correct": False, "why": "The instant of TAKING the photograph is not the instant the light SET OUT; those differ by each object's own distance."},
                {"text": 'Each photograph shows light from a different point in the past', "correct": True},
                {"text": 'Only the Andromeda photograph shows old light; the Mars photograph shows the present moment', "correct": False, "why": 'The Mars photograph is also old light, just by a far shorter delay of about 4 minutes.'},
                {"text": 'The two photographs cannot be taken at the same instant', "correct": False, "why": "Both can be captured at the same moment on Earth; what differs is how old each image's light is."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h15',
            "band": 'harder',
            "text": "A pupil calculates Andromeda's distance in metres and gets a huge number with fifteen digits. They argue this proves kilometres and light years are 'basically the same idea, just relabelled'. What is wrong with that conclusion?",
            "options": [
                {"text": 'Metres and light years cannot both correctly describe the same distance to Andromeda', "correct": False, "why": 'Both units can validly describe the same real distance; the difference is in what else each one conveys.'},
                {"text": 'The conclusion is correct, since every distance unit ultimately means the same thing', "correct": False, "why": "A light year carries an extra piece of information, the light's age, that a plain length unit does not carry."},
                {"text": "A light year also encodes the light's age", "correct": True},
                {"text": "The fifteen-digit figure shows the pupil's calculation must contain an error somewhere", "correct": False, "why": 'A distance this large genuinely does run to about that many digits when written in metres.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h16',
            "band": 'harder',
            "text": "Explain why describing Voyager 1's distance as '22 light hours' is more informative for a mission engineer than giving the same distance in kilometres alone.",
            "options": [
                {"text": 'Kilometre figures cannot be applied to spacecraft, reserved exclusively for planets', "correct": False, "why": 'Kilometres apply perfectly well to spacecraft distances; the light-hour figure is simply more directly useful here.'},
                {"text": 'It is not more informative; kilometres would serve an engineer equally well', "correct": False, "why": 'Kilometres alone would need an extra calculation to recover the communication delay engineers actually need.'},
                {"text": 'Light hours are simply the sole unit precise enough for engineering purposes', "correct": False, "why": 'Kilometres can be exactly as precise; the advantage of light hours is convenience, not precision.'},
                {"text": 'It directly tells the engineer how long a command will take to arrive, with no extra step', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h17',
            "band": 'harder',
            "text": "A textbook states that the speed of light is 'the same in every direction, for every observer, in a vacuum'. Explain why Neptune's and Andromeda's very different light-travel times do not contradict that statement.",
            "options": [
                {"text": 'The travel times differ because the DISTANCES themselves differ so hugely', "correct": True},
                {"text": "They do contradict it, since light clearly moves faster to cover Andromeda's greater distance", "correct": False, "why": "The speed is identical for both; it is the far greater DISTANCE that produces Andromeda's much longer travel time."},
                {"text": 'Neptune and Andromeda must each have their own separate speed of light', "correct": False, "why": 'There is only one fixed speed of light, used identically for every object, near or far.'},
                {"text": 'The statement applies solely to light travelling inside the solar system', "correct": False, "why": "The statement applies everywhere in a vacuum, Andromeda's light included, not only inside the solar system."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h18',
            "band": 'harder',
            "text": 'Suppose a new type of signal were discovered that travels at twice the speed of light. Explain what would happen to a stated travel time to an object such as Neptune, if astronomers started measuring with it instead.',
            "options": [
                {"text": 'Every DISTANCE to a given object would double, since the signal is faster', "correct": False, "why": 'The real distances to Neptune or Andromeda would not change; only the TIME to cross them would, since distance is a property of the object, not of the signal used to measure it.'},
                {"text": 'Every stated travel TIME to a given object would simply halve in value', "correct": True},
                {"text": 'Nothing would change, since speed has no bearing on measured travel times', "correct": False, "why": 'Travel time depends directly on speed; a faster signal reaching an unchanged distance takes less time to arrive.'},
                {"text": 'The distances would become impossible to measure using any signal', "correct": False, "why": 'A faster signal would still measure the same real distances, just via shorter travel times.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h19',
            "band": 'harder',
            "text": "A pupil argues that because a light-minute and a plain minute share the same base unit, converting between them should need no extra step beyond adding the word 'light'. Explain the flaw in that reasoning.",
            "options": [
                {"text": "The flaw is that 'light-minute' and 'minute' do not share any base unit", "correct": False, "why": 'Both genuinely use the minute as their unit of time; the missing step is the multiplication by speed.'},
                {"text": "There is no flaw — the pupil's shortcut works perfectly for any such calculation", "correct": False, "why": 'Every worked example that does this multiplies by the speed of light; the shortcut skips exactly that step.'},
                {"text": 'Converting a light-minute into a distance needs the speed of light multiplied in', "correct": True},
                {"text": 'The flaw matters solely for units larger than a minute, such as light hours or light years', "correct": False, "why": 'The same missing step, multiplying by the speed of light, applies to every light-time unit, not only the larger ones.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h20',
            "band": 'harder',
            "text": "A pupil says that once a spacecraft is travelling, its own speed should simply be added to the speed of any radio signal it sends back towards Earth. Explain why the fixed speed of light rules that out.",
            "options": [
                {"text": "The spacecraft's own speed is invariably too small to matter, even though it could in principle be added", "correct": False, "why": 'The speed of light is fixed in principle, not merely a case where the addition happens to be too small to notice.'},
                {"text": "The pupil's reasoning is correct, and speeds should indeed be added together this way", "correct": False, "why": 'Every calculation of this kind uses one single fixed value for the speed of light, never an adjusted one.'},
                {"text": 'Radio signals do not obey the speed of light, unlike visible light', "correct": False, "why": 'Radio signals are electromagnetic waves travelling at the very same fixed speed as visible light.'},
                {"text": 'The speed of light is treated as a fixed constant nothing can add to', "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h21',
            "band": 'harder',
            "text": 'Explain why a pupil who has mastered d = c × t for the Moon and the Sun should expect the SAME formula, not a different one, to work for Andromeda.',
            "options": [
                {"text": 'The distance-speed-time relationship does not depend on the object', "correct": True},
                {"text": 'A different formula is needed once distances grow large enough', "correct": False, "why": 'The same d = c × t relationship works from the Moon right out to Andromeda.'},
                {"text": 'The formula is restricted to objects inside the solar system', "correct": False, "why": "The same formula produces Andromeda's distance too, well outside the solar system."},
                {"text": 'Andromeda requires an extra step because its light is millions of years old', "correct": False, "why": "The age of the light does not change the formula used; it is simply a consequence of the same formula's result."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h22',
            "band": 'harder',
            "text": "A pupil says that because the Moon's light-travel time (1.28 s) rounds almost to a whole number, it must be a 'neater', more fundamental fact than Neptune's less tidy 15 000-second figure. Assess that reasoning.",
            "options": [
                {"text": 'Sound — a distance that rounds more neatly is always the physically simpler one', "correct": False, "why": 'Neither figure is simpler physically; both come from the same d = c × t relationship, just with different numbers.'},
                {"text": 'Flawed — how tidily a number happens to round is an accident of arithmetic', "correct": True},
                {"text": "Sound — Neptune's distance must be measured less accurately, which is why it looks untidy", "correct": False, "why": "Neptune's figure is measured with good accuracy; it simply happens not to round to a tidy number."},
                {"text": "The reasoning cannot be judged without knowing each object's exact size", "correct": False, "why": "Each object's size plays no part in how tidily its light-travel time happens to round."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h23',
            "band": 'harder',
            "text": "The speed of light is fixed, while Neptune and Earth both orbit the Sun and so are not always the same distance apart. Predict what happens to Neptune's light-travel time across the year.",
            "options": [
                {"text": 'It varies because the speed of light itself changes slightly across the year', "correct": False, "why": "The speed of light does not change; it is Neptune's varying distance that drives the changing travel time."},
                {"text": 'It stays exactly fixed all year, since the speed used in the calculation stays constant', "correct": False, "why": 'The distance is the part that changes here; a changing distance with a fixed speed still gives a changing travel time.'},
                {"text": "It rises and falls, tracking Neptune's changing distance", "correct": True},
                {"text": 'It cannot be predicted from these two facts alone', "correct": False, "why": 'A varying distance combined with a fixed speed is exactly enough to predict a varying travel time.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h24',
            "band": 'harder',
            "text": "A pupil proposes testing whether light truly takes time to reach the Moon by timing an ordinary desk lamp switch instead, since 'light is light either way'. Explain why this test would not settle the question.",
            "options": [
                {"text": 'Light near a desk lamp travels at a different speed from light out in space', "correct": False, "why": 'The speed of light is the same near a desk lamp as it is out in space; only the distance differs.'},
                {"text": 'A desk lamp does not produce real light, unlike a torch or the Sun', "correct": False, "why": 'A desk lamp produces perfectly ordinary light, travelling at the same fixed speed as any other.'},
                {"text": 'The test would work exactly as well as timing the Moon, and would settle the question just as clearly', "correct": False, "why": "The desk lamp's tiny distance makes its delay far too short to detect with everyday timing, unlike the Moon's."},
                {"text": "The desk lamp's distance is far too short for the delay to be measurable with ordinary timing", "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h25',
            "band": 'harder',
            "text": "Explain why the fact that 'the fastest human probe would take 70 000 years to reach the nearest star' is itself evidence for the speed of light being a genuine limit, rather than a target still being chased.",
            "options": [
                {"text": "The huge gap between achievable speeds and light's own speed shows how far off we are", "correct": True},
                {"text": 'The figure shows humans are getting close to the speed of light already', "correct": False, "why": '70 000 years compared with 4.24 years for light itself shows a vast gap, not a close approach to the limit.'},
                {"text": 'The figure has nothing to do with the speed of light', "correct": False, "why": 'The 70 000-year figure comes directly from comparing an achievable speed against the speed of light.'},
                {"text": 'It shows that the speed of light itself must be far higher than 299 792 458 m/s', "correct": False, "why": 'The speed of light figure is unaffected by how slow human spacecraft happen to be.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h26',
            "band": 'harder',
            "text": "A pupil claims that once astronomers know an object's light-travel time, they automatically know exactly what that object looks like RIGHT NOW. Explain the flaw.",
            "options": [
                {"text": 'The claim is correct, since light-travel time and present appearance are simply two names for the same thing', "correct": False, "why": 'A light-travel time reveals a PAST state of the object, never its present one.'},
                {"text": 'A light-travel time only reveals how the object looked when its light set out, not its present state', "correct": True},
                {"text": 'Light-travel time works this way for planets, not for stars or galaxies', "correct": False, "why": 'The same limitation, seeing only the past, applies to planets, stars and galaxies alike.'},
                {"text": 'Astronomers can correct for this delay and see the present instantly using powerful telescopes', "correct": False, "why": "No telescope, however powerful, can see past the delay set by an object's own distance."},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h27',
            "band": 'harder',
            "text": "A pupil argues that Voyager 1's 22-light-hour distance and Andromeda's 2.5-million-light-year distance are 'really the same kind of fact, just at different sizes'. Evaluate this claim.",
            "options": [
                {"text": 'Wrong — light-time figures apply properly solely outside the solar system', "correct": False, "why": 'Voyager sits well inside a light-time framework too, despite being much closer than Andromeda.'},
                {"text": "Wrong — Voyager's distance is measured in an entirely different way from Andromeda's", "correct": False, "why": 'Both distances are derived from a light-travel time and the fixed speed of light, in exactly the same way.'},
                {"text": 'Broadly right — both distances come from a light-travel time the same way', "correct": True},
                {"text": 'The claim cannot be judged, since Voyager is human-made and Andromeda is not', "correct": False, "why": 'Whether an object is natural or human-made makes no difference to how its light-travel time is worked out.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h28',
            "band": 'harder',
            "text": "Design a one-sentence rule a younger pupil could use to decide, for any quantity written as a number followed by 'light' and a time word, whether it is a distance or a time.",
            "options": [
                {"text": 'If the phrase appears in a science lesson rather than a newspaper, it names a distance', "correct": False, "why": "Where a phrase appears does not change what it means; the word 'light' is what does that."},
                {"text": 'If the number is larger than a hundred, the phrase names a distance rather than a time', "correct": False, "why": "The size of the number plays no part in deciding this; what matters is the presence of the word 'light'."},
                {"text": 'If the object mentioned is a star, the phrase names a distance; otherwise it names a time', "correct": False, "why": 'The same rule applies whatever kind of object is being described, not only for stars.'},
                {"text": "If the word 'light' appears directly before the time word, the whole phrase names a distance", "correct": True},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h29',
            "band": 'harder',
            "text": 'A pupil argues that since d = c × t rearranges to give three different formulae, there must really be three separate physical laws hidden inside a formula triangle. Explain the flaw.',
            "options": [
                {"text": 'All three simply express one single relationship, not three separate laws', "correct": True},
                {"text": 'The pupil is correct — each rearrangement is its own law', "correct": False, "why": 'All three forms come from rearranging the very same single relationship, not from three separate laws.'},
                {"text": 'Only d = c × t is a real law; the other two are wrong', "correct": False, "why": 'All three rearrangements are equally valid; they are the same relationship written three different ways.'},
                {"text": 'The three rearrangements apply to three different kinds of object', "correct": False, "why": 'The same three rearrangements apply to any object at all, from the Moon to Andromeda.'},
            ],
            "figure": None,
        },
        {
            "id": 'p12-06-h30',
            "band": 'harder',
            "text": 'Summarise, using the Moon, Voyager 1 and Andromeda together, why a single idea — a fixed speed of light — can explain distances ranging from just over a second to millions of years.',
            "options": [
                {"text": 'Each of the three objects needs its own separate version of the speed of light', "correct": False, "why": 'One single fixed speed of light is used for the Moon, Voyager and Andromeda alike.'},
                {"text": 'The same relationship scales up unchanged, second or millions of years alike', "correct": True},
                {"text": 'The idea explains the Moon and Voyager; Andromeda needs a completely different explanation', "correct": False, "why": "The very same d = c × t relationship produces Andromeda's distance too, just with a far larger time."},
                {"text": 'The range of distances shows the speed of light must vary with scale', "correct": False, "why": 'One fixed speed, applied to very different times, is exactly what produces this huge range of distances.'},
            ],
            "figure": None,
        },
]
