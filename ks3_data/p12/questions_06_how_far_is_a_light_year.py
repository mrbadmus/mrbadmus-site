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
]
