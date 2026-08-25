"""P7 lesson 01 — Light travels: twelve questions (MRB-223).

Written against Design's page. The lightning hook, the flash-and-bang
bench, the comparison table and both worked examples are hers.

The discriminations, in the order the lesson builds them:

  · light is FAST, not instant (`LIGHT-01`) — and the numbers are what
    make that concrete rather than a slogan;
  · light needs NO material and is fastest where there is none
    (`LIGHT-02`) — the exact opposite of the pattern for sound;
  · light is TRANSVERSE, like a water wave and unlike sound
    (`LIGHT-03`) — the row of the table that a student skims past;
  · the flash and the bang leave TOGETHER (`LIGHT-04`) — the harder band
    sits here, because "the thunder came later" is a rival explanation
    that fits the observation.

⚠️ POSITION IS AUTHORED — 2,3,0,1 · 0,1,3,2 · 1,0,2,3, three of each.

⚠️ The ladder's own two marked rungs are NOT restated, nor are the
worked examples' figures (500 s to the Sun, 8.0 minutes, 1300 ms to the
Moon).
"""

UNIT = "P7"
LESSON = "light-travels"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p7-01-e01",
        "band": "easier",
        "text": "The speed of light in a vacuum is about…",
        "options": [
            {"text": "340 m/s", "correct": False,
             "why": "That is the speed of sound in air, about a million "
                    "times slower."},
            {"text": "3000 m/s", "correct": False,
             "why": "Far too slow. Light covers the whole length of Britain "
                    "in about three thousandths of a second."},
            {"text": "300 000 000 m/s", "correct": True},
            {"text": "300 000 000 km/s", "correct": False,
             "why": "The number is right and the unit is a thousand times "
                    "too big. It is metres per second, not kilometres."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e02",
        "band": "easier",
        "text": "Which of these can travel through a vacuum?",
        "options": [
            {"text": "Sound only", "correct": False,
             "why": "Sound is the one that cannot: it needs particles to "
                    "pass the disturbance on."},
            {"text": "Both light and sound", "correct": False,
             "why": "Light crosses a vacuum; sound does not cross one at "
                    "all, at any distance."},
            {"text": "Neither light nor sound", "correct": False,
             "why": "Sunlight reaches the Earth across 150 million "
                    "kilometres of near-vacuum, so light plainly does."},
            {"text": "Light only", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e03",
        "band": "easier",
        "text": "Light is a transverse wave. Which of these is also "
                "transverse?",
        "options": [
            {"text": "A wave on water", "correct": True},
            {"text": "Sound in air", "correct": False,
             "why": "Sound is longitudinal: the particles move along the "
                    "direction the wave travels, not across it."},
            {"text": "Sound in steel", "correct": False,
             "why": "Sound is longitudinal in any material, and the "
                    "material does not change that."},
            {"text": "Nothing else — light is the only transverse wave "
                     "there is", "correct": False,
             "why": "Waves on water are transverse too, which is why they "
                    "are the useful comparison for light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e04",
        "band": "easier",
        "text": "A firework explodes high above a field. What do you notice "
                "on the ground?",
        "options": [
            {"text": "The bang first, then the flash a moment later",
             "correct": False,
             "why": "That is the wrong way round. Light is enormously "
                    "faster, so the flash always arrives first."},
            {"text": "The flash first, then the bang a moment later",
             "correct": True},
            {"text": "The two together, because they were made together",
             "correct": False,
             "why": "They leave together and arrive apart, because they "
                    "cross the same distance at wildly different speeds."},
            {"text": "Only the flash, because sound does not travel "
                     "upwards", "correct": False,
             "why": "Sound travels in every direction through air. It is "
                    "simply slower than the light."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p7-01-s01",
        "band": "standard",
        "text": "Light takes about 1.3 s to reach the Earth from the Moon. "
                "What does that tell you about light?",
        "options": [
            {"text": "It is fast but not instant, and over big distances "
                     "the delay can be measured", "correct": True},
            {"text": "It slows down in space, because there is nothing "
                     "there to carry it", "correct": False,
             "why": "A vacuum is where light is fastest. The 1.3 s is the "
                    "distance being enormous, not the light being slowed."},
            {"text": "The Moon reflects light more slowly than the Sun "
                     "gives it out", "correct": False,
             "why": "Reflection does not take time in that sense. The 1.3 s "
                    "is the journey."},
            {"text": "Light must be a longitudinal wave, since it takes "
                     "time to arrive", "correct": False,
             "why": "Every wave takes time to arrive. Being transverse or "
                    "longitudinal is a separate matter altogether."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s02",
        "band": "standard",
        "text": "A camera flash fires 60 m away. About how long does the "
                "light take to reach you?",
        "options": [
            {"text": "About 0.18 s", "correct": False,
             "why": "That is roughly how long SOUND would take over 60 m. "
                    "Light is about a million times faster."},
            {"text": "About 0.2 millionths of a second", "correct": True},
            {"text": "No time at all — light is instant", "correct": False,
             "why": "It is fast, not instant. Over 60 m the delay is "
                    "undetectable, and over 60 million kilometres it is not."},
            {"text": "About 60 seconds", "correct": False,
             "why": "That reads the distance as a time. Dividing 60 m by "
                    "300 000 000 m/s gives a very small number of seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s03",
        "band": "standard",
        "text": "Which row correctly separates light from sound?",
        "options": [
            {"text": "Both carry energy without carrying material, and "
                     "both need a material to travel through",
             "correct": False,
             "why": "The first half is right for both. The second is right "
                    "for sound only."},
            {"text": "Light carries material with it and sound does not",
             "correct": False,
             "why": "Neither carries material. That is what makes both of "
                    "them waves."},
            {"text": "Sound has a wavelength and light does not",
             "correct": False,
             "why": "Both have a wavelength and an amplitude. It is one of "
                    "the rows where they agree."},
            {"text": "Both carry energy without carrying material, but only "
                     "sound needs a material to travel through",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s04",
        "band": "standard",
        "text": "Astronauts on the Moon had to use radio to talk to each "
                "other even standing side by side. Why?",
        "options": [
            {"text": "Because their helmets are too thick for sound to get "
                     "through", "correct": False,
             "why": "Even with the visors open there would be nothing to "
                    "hear: the problem is outside the helmet, not the "
                    "helmet."},
            {"text": "Because the Moon's low gravity lets sound spread out "
                     "so fast that it is too faint to hear",
             "correct": False,
             "why": "Gravity has nothing to do with it, and the sound is "
                    "not faint — it does not exist. There are no particles "
                    "to make one."},
            {"text": "Because there is no air between them to carry sound, "
                     "and radio is a wave that needs none", "correct": True},
            {"text": "Because sound travels too slowly on the Moon to be "
                     "useful over a few metres", "correct": False,
             "why": "Sound does not travel on the Moon's surface at all. "
                    "There is nothing for it to travel in."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p7-01-h01",
        "band": "harder",
        "text": "You count five seconds between a lightning flash and its "
                "thunder. Roughly how far away was the strike, and what "
                "assumption are you making?",
        "options": [
            {"text": "About 1500 km, assuming the sound travelled at the "
                     "speed of light", "correct": False,
             "why": "The sound travelled at the speed of sound. Using the "
                    "speed of light for it gives an answer four hundred "
                    "thousand times too big."},
            {"text": "About 1.7 km, assuming the light arrived in "
                     "effectively no time at all", "correct": True},
            {"text": "About 5 km, assuming sound covers a kilometre a "
                     "second", "correct": False,
             "why": "Sound covers about a third of a kilometre a second, so "
                    "five seconds is nearer 1.7 km than 5 km."},
            {"text": "You cannot tell, because the flash and the bang were "
                     "not made at the same moment", "correct": False,
             "why": "They are one event. The flash and the bang leave the "
                    "strike together, which is exactly what makes the "
                    "counting method work."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h02",
        "band": "harder",
        "text": "A star 400 light years away is seen to explode tonight. "
                "What is actually true?",
        "options": [
            {"text": "The explosion happened about 400 years ago and the "
                     "news has only just arrived", "correct": True},
            {"text": "The explosion is happening now and will be visible "
                     "for 400 years", "correct": False,
             "why": "Nothing beats the speed of light, so the light you see "
                    "tonight set off 400 years ago."},
            {"text": "The explosion will happen in about 400 years, and we "
                     "are seeing a warning of it", "correct": False,
             "why": "Light carries information forwards in time, never "
                    "backwards. What arrives is a record of the past."},
            {"text": "The star is 400 years old, which is what a light year "
                     "measures", "correct": False,
             "why": "A light year is a DISTANCE — how far light travels in "
                    "a year — not an age."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h03",
        "band": "harder",
        "text": "Sound is faster in steel than in air, and light is faster "
                "in a vacuum than in glass. Why are those two patterns "
                "opposite?",
        "options": [
            {"text": "They are not opposite: light is faster in steel than "
                     "in a vacuum too", "correct": False,
             "why": "Light does not travel through steel at all, and it is "
                    "fastest of all in a vacuum. Nothing speeds light up."},
            {"text": "Because steel is a solid and a vacuum is not, and a "
                     "solid always speeds a wave up", "correct": False,
             "why": "A solid speeds sound up and stops light dead. Whether "
                    "a material helps depends on how the wave is carried."},
            {"text": "Sound needs particles to pass it on, so packing them "
                     "closer helps it; light needs none, so a material can "
                     "only slow it down", "correct": True},
            {"text": "Because sound is longitudinal and light is "
                     "transverse, and a longitudinal wave is always the "
                     "faster of the two in any material", "correct": False,
             "why": "The two facts are right and the rule drawn from them "
                    "is invented. Light is transverse and about a million "
                    "times faster than sound in air."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h04",
        "band": "harder",
        "text": "An engineer suggests measuring the length of a room by "
                "timing a light pulse across it with a stopwatch. Why will "
                "this not work?",
        "options": [
            {"text": "Because light does not travel in a straight line "
                     "indoors, so the path length is unknown",
             "correct": False,
             "why": "Light travels in straight lines through still air. The "
                    "problem is the timing, not the path."},
            {"text": "Because a stopwatch cannot measure something as slow "
                     "as light over a few metres", "correct": False,
             "why": "The difficulty is the opposite: the time is far too "
                    "SHORT, not too long."},
            {"text": "Because light in air is slower than in a vacuum, so "
                     "the answer would come out wrong", "correct": False,
             "why": "It is very slightly slower and that difference is "
                    "nothing next to the real problem, which is the size of "
                    "the time."},
            {"text": "Because the crossing takes tens of billionths of a "
                     "second, which no hand-held timer can resolve",
             "correct": True},
        ],
        "figure": None,
    },
]
