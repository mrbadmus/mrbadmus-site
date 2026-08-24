"""P1 lesson 06 — Radiation: twelve questions.

These probe the two things that separate radiation from conduction: it needs
nothing in between, and what decides how well a surface handles it is how
SHINY it is rather than what colour. The distractors are built from ENER-14 —
that radiation needs air, like sound — and from the folk version of the
Leslie's cube result, which is that black beats white by a lot. It does not:
the bench measures matt white at 92 against matt black's 100, and two silver
faces of the same metal twenty-two apart.

⚠️ Three questions turn on the colour-versus-shine distinction and one on the
black-car case, which belongs to a different part of the spectrum. That last
one is the commonest objection a class raises and it deserves a question
rather than a footnote.

No figures. Three of each answer index.
"""

UNIT = "P1"
LESSON = "radiation"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p1-06-e01",
        "band": "easier",
        "text": "What does radiation need in order to travel?",
        "options": [
            {"text": "Air",
             "correct": False,
             "why": "The Sun's warmth crosses 150 million kilometres with no "
                    "air anywhere along the way."},
            {"text": "Particles that are touching",
             "correct": False,
             "why": "That is what conduction needs. Radiation works with no "
                    "particles present at all."},
            {"text": "Nothing at all",
             "correct": True},
            {"text": "Any material — solid, liquid or gas",
             "correct": False,
             "why": "It crosses a vacuum with exactly the same reading as it "
                    "crosses air."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e02",
        "band": "easier",
        "text": "Which surface gives off infrared best?",
        "options": [
            {"text": "Polished silver",
             "correct": False,
             "why": "The worst on the bench, at 12 against matt black's 100 — "
                    "and it is the same metal as the dull silver face."},
            {"text": "Dull silver",
             "correct": False,
             "why": "Better than polished, at 34, and still a third of the "
                    "best."},
            {"text": "Clear glass",
             "correct": False,
             "why": "Not one of the four faces on the bench, and not the "
                    "answer either."},
            {"text": "Matt black",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e03",
        "band": "easier",
        "text": "What is infrared?",
        "options": [
            {"text": "The kind of radiation a warm object gives off",
             "correct": True},
            {"text": "A hot gas that rises from a warm object",
             "correct": False,
             "why": "Nothing is rising. Infrared travels in straight lines "
                    "and goes downwards as happily as upwards."},
            {"text": "A very fast vibration of the air near a hot object",
             "correct": False,
             "why": "It crosses a vacuum, where there is no air to vibrate."},
            {"text": "Light that has been slowed down by passing through a "
                     "surface",
             "correct": False,
             "why": "It travels at the speed of light. It is just beyond red "
                    "in the spectrum, and your eyes cannot see it."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-e04",
        "band": "easier",
        "text": "A surface that gives off infrared well also does what?",
        "options": [
            {"text": "Reflects it well",
             "correct": False,
             "why": "The opposite. A surface that reflects it is a poor "
                    "emitter, which is what the polished silver face shows."},
            {"text": "Takes it in well",
             "correct": True},
            {"text": "Stops it passing through",
             "correct": False,
             "why": "Both the shiny and the matt faces are opaque metal. "
                    "Nothing passes through either."},
            {"text": "Conducts it well too",
             "correct": False,
             "why": "The four faces are all the same metal underneath, so "
                    "they all conduct identically. Only the surface differs."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p1-06-s01",
        "band": "standard",
        "text": "Matt white measured 92 and matt black 100. What does that "
                "eight-point gap tell you?",
        "options": [
            {"text": "That colour makes only a small difference to infrared",
             "correct": True},
            {"text": "That matt white is a shiny surface after all",
             "correct": False,
             "why": "Matt means not shiny, and that is what these two share. "
                    "It is what makes them close."},
            {"text": "That the measurement was not accurate enough to trust",
             "correct": False,
             "why": "The two silver faces of the SAME metal came out 22 "
                    "apart, so the instrument can certainly see a real "
                    "difference when there is one."},
            {"text": "That black is a much better emitter than white",
             "correct": False,
             "why": "Eight per cent is not much, especially against the "
                    "eighty-eight between matt black and polished silver."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s02",
        "band": "standard",
        "text": "A hot object is put in a jar and the air is pumped out. A "
                "detector outside was reading infrared. What happens to the "
                "reading?",
        "options": [
            {"text": "It halves, because one of the two routes has gone",
             "correct": False,
             "why": "The conduction through the air was a tiny fraction of "
                    "the total, not half of it."},
            {"text": "It drops to zero, because there is nothing left to "
                     "carry it",
             "correct": False,
             "why": "That is what would happen to a SOUND. Radiation was "
                    "never using the air."},
            {"text": "It rises, because the air was in the way",
             "correct": False,
             "why": "Air is nearly transparent to infrared over ten "
                    "centimetres, so removing it changes almost nothing "
                    "either way."},
            {"text": "It is unchanged",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s03",
        "band": "standard",
        "text": "A vacuum flask has a vacuum between its walls and both "
                "facing surfaces silvered. Which part does which job?",
        "options": [
            {"text": "The vacuum stops conduction; the silvering cuts "
                     "radiation right down",
             "correct": True},
            {"text": "The vacuum stops radiation; the silvering stops "
                     "conduction",
             "correct": False,
             "why": "The wrong way round. A vacuum is exactly what radiation "
                    "is unaffected by."},
            {"text": "Both parts are there to stop conduction",
             "correct": False,
             "why": "A surface finish makes no difference to conduction at "
                    "all — the metal underneath is the same either way."},
            {"text": "Both parts are there to stop radiation",
             "correct": False,
             "why": "A vacuum does nothing to radiation. It is there for the "
                    "other route entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-s04",
        "band": "standard",
        "text": "On the bench, conduction read \"none at all\" across a "
                "vacuum and radiation read the same as through air. What is "
                "the general rule?",
        "options": [
            {"text": "Conduction is faster than radiation in every "
                     "arrangement",
             "correct": False,
             "why": "It is faster when the two objects touch and it is zero "
                    "when they do not. Speed is not what separates them."},
            {"text": "Conduction depends on what is in the gap; radiation "
                     "does not",
             "correct": True},
            {"text": "Radiation only works when there is nothing in the way",
             "correct": False,
             "why": "It worked through air as well. It is simply not "
                    "affected either way."},
            {"text": "Both routes need matter, but conduction needs more of "
                     "it",
             "correct": False,
             "why": "Radiation needs none. That is the whole result."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p1-06-h01",
        "band": "harder",
        "text": "If matt white emits infrared nearly as well as matt black, "
                "why does a black car get hotter in the sun?",
        "options": [
            {"text": "Because sunlight is mostly visible light, and colour "
                     "does decide that",
             "correct": True},
            {"text": "Because the bench measurement is wrong for real "
                     "surfaces outdoors",
             "correct": False,
             "why": "The measurement holds outdoors too. What changes is "
                    "which part of the spectrum is arriving."},
            {"text": "Because car paint behaves differently from the paint on "
                     "the cube",
             "correct": False,
             "why": "Car paint is close enough. The difference is in the "
                    "light, not in the paint."},
            {"text": "Because a black car radiates less of its own warmth "
                     "away",
             "correct": False,
             "why": "Backwards — black is a good emitter, so it radiates "
                    "MORE away. It still ends up hotter because it takes in "
                    "so much more."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h02",
        "band": "harder",
        "text": "A marathon runner is wrapped in shiny foil at the finish. "
                "Which explanation is exact?",
        "options": [
            {"text": "The foil is warm and passes its warmth to the runner",
             "correct": False,
             "why": "The foil comes out of a packet at air temperature. It is "
                    "not a source of anything."},
            {"text": "A shiny surface is a poor emitter, so the runner's own "
                     "infrared is kept in",
             "correct": True},
            {"text": "The foil reflects sunlight away and stops the runner "
                     "overheating",
             "correct": False,
             "why": "They are handed out at night and in the rain as well. "
                    "The problem being solved is losing warmth, not gaining "
                    "it."},
            {"text": "The foil conducts badly, which is why it is used "
                     "instead of a blanket",
             "correct": False,
             "why": "Metal foil conducts very well. It works despite that, "
                    "because it is dealing with a different route."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h03",
        "band": "harder",
        "text": "Two silver faces on the cube read 34 and 12 and are the "
                "same metal. What single change accounts for the difference?",
        "options": [
            {"text": "One of them was at a different temperature",
             "correct": False,
             "why": "All four faces are on one cube filled with the same hot "
                    "water. They are at the same temperature by "
                    "construction."},
            {"text": "One of them is thicker than the other",
             "correct": False,
             "why": "Thickness would matter for conduction through the wall. "
                    "It is the outside that is doing the emitting."},
            {"text": "One has been polished and the other roughened",
             "correct": True},
            {"text": "One has been painted and the other left bare",
             "correct": False,
             "why": "Both are bare metal — that is why the pair is on the "
                    "bench at all."},
        ],
        "figure": None,
    },
    {
        "id": "p1-06-h04",
        "band": "harder",
        "text": "A student says \"radiation is dangerous, so a hot radiator "
                "must be dangerous too\". What has gone wrong?",
        "options": [
            {"text": "A radiator gives off no radiation at all, only warmth",
             "correct": False,
             "why": "Warmth leaving a radiator IS infrared radiation, plus "
                    "some warmed air. That is exactly what the word means "
                    "here."},
            {"text": "The word radiation covers many different things, and "
                     "infrared is the harmless end",
             "correct": True},
            {"text": "Radiators are kept at a safe temperature, so the "
                     "radiation is weakened",
             "correct": False,
             "why": "A hotter radiator would give off more infrared and "
                    "still not be the dangerous kind. The temperature is not "
                    "the point."},
            {"text": "Nothing has gone wrong; radiators do give off a small "
                     "amount of dangerous radiation",
             "correct": False,
             "why": "They give off none of it. Everything above absolute zero "
                    "radiates, and almost none of that is harmful."},
        ],
        "figure": None,
    },
]
