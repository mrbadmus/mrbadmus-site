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
]
