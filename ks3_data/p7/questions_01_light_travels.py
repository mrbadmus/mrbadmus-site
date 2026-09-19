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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p7-01-e05",
        "band": "easier",
        "text": "Light is a…",
        "options": [            {"text": "longitudinal wave, like sound", "correct": False,
             "why": "Sound is longitudinal; light is not. Light is displaced "
                    "at right angles to its direction of travel."},
            {"text": "kind of sound too fast for the ear", "correct": False,
             "why": "Sound needs a material and light does not, so they are "
                    "different kinds of wave entirely."},
            {"text": "stream of air particles", "correct": False,
             "why": "It crosses a vacuum, where there are no particles at "
                    "all."},
            {"text": "transverse wave, like a ripple", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e06",
        "band": "easier",
        "text": "Which travels faster: light in a vacuum, or sound in air?",
        "options": [            {"text": "Light, by about a million times", "correct": True},
            {"text": "They travel at the same speed", "correct": False,
             "why": "If they did, thunder would arrive with the flash rather "
                    "than seconds later."},
            {"text": "Sound, because air carries it along", "correct": False,
             "why": "Air carries sound at about 340 m/s, which light beats by "
                    "close to a million times."},
            {"text": "Light, but only by about twice", "correct": False,
             "why": "The gap is enormous: 300 000 000 m/s against about "
                    "340 m/s."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e07",
        "band": "easier",
        "text": "Does light need a material to travel through?",
        "options": [            {"text": "No — it crosses a vacuum", "correct": True},
            {"text": "Yes, but only over long distances", "correct": False,
             "why": "Distance makes no difference; it crosses the emptiness "
                    "between stars perfectly well."},
            {"text": "Yes, which is why it travels best through air",
             "correct": False,
             "why": "It travels FASTEST through a vacuum, where there is no "
                    "material at all."},
            {"text": "No, but it travels much more slowly in a vacuum",
             "correct": False,
             "why": "A vacuum is where it is quickest; materials slow it "
                    "down."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e08",
        "band": "easier",
        "text": "In a vacuum, light travels 300 000 000 m in…",
        "options": [            {"text": "one hour", "correct": False,
             "why": "In an hour it covers about a thousand billion metres; a "
                    "second is the right unit here."},
            {"text": "one minute", "correct": False,
             "why": "In a minute it covers sixty times that distance."},
            {"text": "no time at all", "correct": False,
             "why": "Light is fast but not instant — that is why sunlight "
                    "takes about eight minutes to arrive."},
            {"text": "one second", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p7-01-s05",
        "band": "standard",
        "text": "Light from the Sun takes about eight minutes to reach the "
                "Earth. What does that show?",
        "options": [            {"text": "That light takes time to travel, and the Sun is very "
                     "far away",
             "correct": True},
            {"text": "That light is slowed down by the emptiness of space",
             "correct": False,
             "why": "Empty space is where light goes fastest; the eight "
                    "minutes is a matter of distance."},
            {"text": "That the Sun only shines every eight minutes",
             "correct": False,
             "why": "It shines continuously; the eight minutes is how long "
                    "the journey takes."},
            {"text": "That sunlight has to pass through the atmosphere first",
             "correct": False,
             "why": "The atmosphere is crossed in a fraction of a "
                    "millisecond; almost all the time is spent in space."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s06",
        "band": "standard",
        "text": "A laser is fired at a wall 900 m away. About how long does "
                "the light take to get there?",
        "options": [
            {"text": "About 2.6 s", "correct": False,
             "why": "That uses the speed of sound. Light covers 900 m in a "
                    "few millionths of a second."},
            {"text": "About 0.003 s", "correct": False,
             "why": "That is a thousand times too long — check the powers of "
                    "ten in 300 000 000."},
            {"text": "No time at all", "correct": False,
             "why": "It is extremely quick but not instant; the journey has a "
                    "real, if tiny, duration."},
            {"text": "About 0.000003 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s07",
        "band": "standard",
        "text": "Sound travels at about 340 m/s and light at 300 000 000 m/s. "
                "Roughly how many times faster is light?",
        "options": [            {"text": "About a thousand times", "correct": False,
             "why": "That is a thousand times too small; divide the two "
                    "figures and check the zeros."},
            {"text": "About a billion times", "correct": False,
             "why": "That is a thousand times too large."},
            {"text": "About a hundred times", "correct": False,
             "why": "A hundred times 340 is 34 000, nowhere near "
                    "300 000 000."},
            {"text": "About a million times", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s08",
        "band": "standard",
        "text": "Why can light cross the space between the Sun and the Earth "
                "when sound cannot?",
        "options": [            {"text": "Because light needs no particles, while sound is passed "
                     "from particle to particle",
             "correct": True},
            {"text": "Because sound is absorbed by the Sun's atmosphere",
             "correct": False,
             "why": "Even with a clear path, sound needs particles all the "
                    "way, and space has almost none."},
            {"text": "Because light is much faster, so it gets across before "
                     "it fades",
             "correct": False,
             "why": "Speed is not the issue. Sound would not cross at any "
                    "speed, because there is nothing to carry it."},
            {"text": "Because light is a longitudinal wave and sound is "
                     "transverse",
             "correct": False,
             "why": "The two are the other way round, and it is not what "
                    "decides this in any case."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p7-01-h05",
        "band": "harder",
        "text": "The Sun is about 150 000 000 000 m away. How long does its "
                "light take to reach us?",
        "options": [            {"text": "About 50 s, well under a minute", "correct": False,
             "why": "That is ten times too short — check the zeros in the "
                    "division."},
            {"text": "About 0.5 s, almost instant", "correct": False,
             "why": "That is roughly the time for light to reach the Moon and "
                    "back, not to cross to the Sun."},
            {"text": "About 5000 s, nearly an hour and a half", "correct": False,
             "why": "That is ten times too long, and would make sunrise "
                    "arrive nearly an hour and a half late."},
            {"text": "About 500 s, or eight minutes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h06",
        "band": "harder",
        "text": "A radio signal travels at the speed of light to a satellite "
                "36 000 000 m up and back again. How long is the round trip?",
        "options": [            {"text": "0.24 s", "correct": True},
            {"text": "0.12 s", "correct": False,
             "why": "That is the one-way time; the signal has to come back as "
                    "well."},
            {"text": "0.0012 s", "correct": False,
             "why": "That is a hundred times too short — check the powers of "
                    "ten before writing it down."},
            {"text": "8.3 s", "correct": False,
             "why": "That divides by 8 600 000 rather than by 300 000 000."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h07",
        "band": "harder",
        "text": "Why is a light year a distance rather than a length of time?",
        "options": [            {"text": "Because it is how long a star takes to become visible",
             "correct": False,
             "why": "That would be a time. The unit measures how far the "
                    "light gets."},
            {"text": "Because it counts the years light has already been "
                     "travelling",
             "correct": False,
             "why": "It is not a count of anything's age; it is a fixed "
                    "distance."},
            {"text": "Because a year is too long to be used as a time in "
                     "astronomy",
             "correct": False,
             "why": "Years are used as times constantly; the unit is defined "
                    "as a distance because of what it multiplies."},
            {"text": "Because it is how far light travels in a year",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h08",
        "band": "harder",
        "text": "Two students argue about whether torchlight reaches a wall "
                "3 m away instantly. Who is right?",
        "options": [
            {"text": "It is instant, because light has no speed to slow it "
                     "down",
             "correct": False,
             "why": "Light has a definite speed of 300 000 000 m/s, so every "
                    "journey takes some time."},
            {"text": "It takes about 0.01 s, which is why a torch seems to "
                     "flicker on",
             "correct": False,
             "why": "That is a million times too long, and nothing about a "
                    "torch flickers for that reason."},
            {"text": "It takes about 0.00000001 s — very quick, but not "
                     "instant",
             "correct": True},
            {"text": "It cannot be worked out, because light has no fixed "
                     "speed in air",
             "correct": False,
             "why": "Its speed in air is very close to its vacuum value, and "
                    "the sum is straightforward."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ───────────────────────────────────────
    {
        "id": "p7-01-e09",
        "band": "easier",
        "text": "A transverse wave is one where the vibration is…",
        "options": [
            {"text": "at right angles to the direction the wave travels",
             "correct": True},
            {"text": "along the same direction the wave travels, exactly "
                     "like a sound wave", "correct": False,
             "why": "That describes a longitudinal wave, like sound, not a "
                    "transverse one."},
            {"text": "only up and down, never side to side", "correct": False,
             "why": "The vibration can be in any direction across the wave, "
                    "as long as it is at right angles to the travel."},
            {"text": "random, changing direction unpredictably from one "
                     "moment to the next", "correct": False,
             "why": "A transverse wave has a definite direction of vibration "
                    "— across the travel direction — not a random one."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e10",
        "band": "easier",
        "text": "A vacuum is…",
        "options": [
            {"text": "any material light cannot pass through", "correct": False,
             "why": "A vacuum is the opposite: light crosses it at full "
                    "speed. Some materials do block light, but that is not "
                    "what a vacuum is."},
            {"text": "a space with no particles in it at all", "correct": True},
            {"text": "a space filled with a very thin gas", "correct": False,
             "why": "A thin gas still has particles in it. A true vacuum has "
                    "none at all."},
            {"text": "the material that makes up glass and water",
             "correct": False,
             "why": "Glass and water are dense materials full of particles — "
                    "close to the opposite of a vacuum."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e11",
        "band": "easier",
        "text": "Which property does light share with sound and with waves on "
                "water?",
        "options": [
            {"text": "It needs a material to travel through", "correct": False,
             "why": "That is exactly where light differs from the other "
                    "two: it needs none at all."},
            {"text": "It is always transverse", "correct": False,
             "why": "Sound is not transverse, so this is not something all "
                    "three share."},
            {"text": "It has a wavelength and an amplitude", "correct": True},
            {"text": "It carries no energy from place to place",
             "correct": False,
             "why": "Every wave here carries energy without carrying "
                    "material — that includes light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e12",
        "band": "easier",
        "text": "The speed of light in a vacuum, in kilometres per second, is "
                "about…",
        "options": [
            {"text": "300 km/s", "correct": False,
             "why": "That is a thousand times too slow — check the zeros "
                    "against the metres-per-second figure."},
            {"text": "3000 km/s", "correct": False,
             "why": "That is a hundred times too slow."},
            {"text": "300 000 000 km/s", "correct": False,
             "why": "That is the metres-per-second figure with the wrong "
                    "unit stuck on it — a thousand times too big."},
            {"text": "300 000 km/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e13",
        "band": "easier",
        "text": "The speed of sound in air is about…",
        "options": [
            {"text": "340 m/s", "correct": True},
            {"text": "3400 m/s", "correct": False,
             "why": "That is ten times too fast for sound in air."},
            {"text": "34 m/s", "correct": False,
             "why": "That is ten times too slow — barely a jog."},
            {"text": "340 km/s", "correct": False,
             "why": "That unit makes it faster than light, which nothing "
                    "in air comes close to."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e14",
        "band": "easier",
        "text": "About how long does light take to travel from the Moon to "
                "the Earth?",
        "options": [
            {"text": "13 s", "correct": False,
             "why": "That is ten times too long."},
            {"text": "1.3 s", "correct": True},
            {"text": "1.3 minutes", "correct": False,
             "why": "That is about sixty times too long."},
            {"text": "1.3 hours", "correct": False,
             "why": "That would put the Moon far further away than it is."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e15",
        "band": "easier",
        "text": "A light year measures…",
        "options": [
            {"text": "a time", "correct": False,
             "why": "Despite the word 'year' in its name, it is not a time "
                    "at all."},
            {"text": "a speed", "correct": False,
             "why": "The speed involved is fixed; what a light year gives "
                    "is how far that speed covers in a year."},
            {"text": "a distance", "correct": True},
            {"text": "a brightness", "correct": False,
             "why": "It says nothing about how bright a star looks, only how "
                    "far its light has come."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e16",
        "band": "easier",
        "text": "Which statement is correct?",
        "options": [
            {"text": "Some radio signals travel faster than light",
             "correct": False,
             "why": "Radio waves travel at the speed of light in a vacuum, "
                    "never faster."},
            {"text": "Sound is the fastest thing there is", "correct": False,
             "why": "Sound is roughly a million times slower than light in "
                    "a vacuum."},
            {"text": "Light can be outrun by a fast enough rocket",
             "correct": False,
             "why": "No rocket comes remotely close to the speed of light, "
                    "and nothing outruns it."},
            {"text": "Nothing travels faster than light in a vacuum",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e17",
        "band": "easier",
        "text": "Looking at a distant star is really…",
        "options": [
            {"text": "looking into the past, because its light took time to "
                     "arrive", "correct": True},
            {"text": "looking at how the star is at this exact moment",
             "correct": False,
             "why": "What arrives is old light. The star's condition right "
                    "now is not what you are seeing."},
            {"text": "looking into the future, since the light has not "
                     "yet reached this particular location", "correct": False,
             "why": "The light you see HAS arrived — it is simply old by "
                    "the time it gets here."},
            {"text": "impossible without a telescope powerful enough to "
                     "slow the light down", "correct": False,
             "why": "No telescope slows light down. It works by gathering "
                    "more of it, not by changing its speed."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e18",
        "band": "easier",
        "text": "Like sound, light can be…",
        "options": [
            {"text": "slowed down by a vacuum", "correct": False,
             "why": "A vacuum is where light is fastest, not slowed."},
            {"text": "reflected and absorbed", "correct": True},
            {"text": "stopped completely by air", "correct": False,
             "why": "Air lets almost all light straight through, which is "
                    "why it is transparent."},
            {"text": "turned into sound at a boundary", "correct": False,
             "why": "Light and sound do not convert into one another at a "
                    "surface."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e19",
        "band": "easier",
        "text": "Since 1983, the metre has been defined using…",
        "options": [
            {"text": "the length of a metal bar kept in France",
             "correct": False,
             "why": "That was the old definition, replaced in 1983."},
            {"text": "the wavelength of red light", "correct": False,
             "why": "The modern definition is built from the speed of "
                    "light and a fraction of a second, not a wavelength."},
            {"text": "the distance light travels in a fixed fraction of a "
                     "second", "correct": True},
            {"text": "the distance sound travels through open air in "
                     "exactly one second", "correct": False,
             "why": "Sound's speed changes with the material and the "
                    "weather, which would make a poor standard."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e20",
        "band": "easier",
        "text": "Sunlight can warm a planet across the empty space between "
                "them because light…",
        "options": [
            {"text": "carries warm air with it from the Sun", "correct": False,
             "why": "There is no air in space for light to carry. It "
                    "carries energy, not material."},
            {"text": "is heated by passing through the vacuum",
             "correct": False,
             "why": "A vacuum does nothing to light passing through it. "
                    "Nothing warms the light itself."},
            {"text": "reflects off nearby planets to reach us",
             "correct": False,
             "why": "Sunlight reaches Earth directly, in a straight line "
                    "from the Sun."},
            {"text": "needs no material to travel through", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e21",
        "band": "easier",
        "text": "Some stars visible in the night sky tonight may have "
                "already died. Why can we still see them?",
        "options": [
            {"text": "Their light set off long ago and is only now "
                     "arriving", "correct": True},
            {"text": "Dead stars glow brighter than living ones",
             "correct": False,
             "why": "A dead star gives out no new light at all. What you "
                    "see is old light from before it died."},
            {"text": "Old starlight travels through space faster than "
                     "newly emitted starlight does", "correct": False,
             "why": "All light travels at the same speed in a vacuum, "
                    "whenever it set off."},
            {"text": "The night sky somehow stores up starlight and "
                     "releases it again slowly", "correct": False,
             "why": "Nothing stores light. It simply keeps travelling until "
                    "it reaches an eye or a detector."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e22",
        "band": "easier",
        "text": "Sound travels faster in steel than in air. What does this "
                "tell you about sound?",
        "options": [
            {"text": "It travels fastest in a vacuum, like light",
             "correct": False,
             "why": "Sound cannot cross a vacuum at all, so it has no speed "
                    "there whatsoever."},
            {"text": "It needs particles to travel, and how they are "
                     "arranged affects its speed", "correct": True},
            {"text": "It does not travel through solids in any "
                     "noticeable way", "correct": False,
             "why": "It travels through solids very well — faster than "
                    "through air, in fact."},
            {"text": "Its speed never changes, whatever material or "
                     "temperature it happens to be travelling through",
             "correct": False,
             "why": "The steel-versus-air comparison shows the opposite: "
                    "its speed depends on the material."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e23",
        "band": "easier",
        "text": "300 000 000 m is the same distance as…",
        "options": [
            {"text": "300 km", "correct": False,
             "why": "That is a thousand times too small."},
            {"text": "3000 km", "correct": False,
             "why": "That is a hundred times too small."},
            {"text": "300 000 km", "correct": True},
            {"text": "30 000 000 km", "correct": False,
             "why": "That is a hundred times too big."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e24",
        "band": "easier",
        "text": "Light travels fastest through…",
        "options": [
            {"text": "glass", "correct": False,
             "why": "Glass slows light down. It is not the fastest option "
                    "here."},
            {"text": "water", "correct": False,
             "why": "Water slows light less than glass does, but it still "
                    "slows it."},
            {"text": "air, faster than through a vacuum", "correct": False,
             "why": "Nothing is faster than a vacuum for light, including "
                    "air."},
            {"text": "a vacuum", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e25",
        "band": "easier",
        "text": "In a thunderstorm, when are the flash and the bang actually "
                "made?",
        "options": [
            {"text": "At the same moment", "correct": True},
            {"text": "The bang a few seconds before the flash",
             "correct": False,
             "why": "The order given here is backwards, as well as the "
                    "timing."},
            {"text": "The bang a few seconds after the flash",
             "correct": False,
             "why": "They are made together. The gap you notice is the "
                    "sound arriving late, not being made late."},
            {"text": "The flash alone, because thunder makes no real sound",
             "correct": False,
             "why": "Thunder is a genuine sound, made at the same moment as "
                    "the flash — it simply takes longer to arrive."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e26",
        "band": "easier",
        "text": "To use light's speed in metres per second with a time given "
                "in minutes, you must first…",
        "options": [
            {"text": "leave the minutes as they are, since light is very "
                     "fast", "correct": False,
             "why": "Mixing minutes with metres per second gives an answer "
                    "sixty times too small."},
            {"text": "convert the minutes into seconds", "correct": True},
            {"text": "convert the metres into kilometres", "correct": False,
             "why": "The speed is already in metres per second; it is the "
                    "TIME unit that clashes."},
            {"text": "convert the speed into minutes per metre",
             "correct": False,
             "why": "That flips the whole calculation the wrong way round, "
                    "rather than fixing the mismatched unit."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e27",
        "band": "easier",
        "text": "In d = c × t, what does t stand for?",
        "options": [
            {"text": "The total distance travelled by light", "correct": False,
             "why": "That is what d stands for, not t."},
            {"text": "The temperature of the material", "correct": False,
             "why": "Temperature plays no part in this formula at all."},
            {"text": "The time the light takes to travel", "correct": True},
            {"text": "The type of material the light passes through",
             "correct": False,
             "why": "The formula uses c for a vacuum and does not include a "
                    "term for the material."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e28",
        "band": "easier",
        "text": "The unit of the speed of light, 300 000 000 m/s, means…",
        "options": [
            {"text": "300 000 000 seconds needed to travel one metre",
             "correct": False,
             "why": "That reads the unit backwards — it would make light "
                    "extraordinarily slow."},
            {"text": "300 000 000 metres travelled every single calendar "
                     "year", "correct": False,
             "why": "The unit is metres per SECOND, not per year."},
            {"text": "a speed that changes every second", "correct": False,
             "why": "The speed is constant in a vacuum; the unit just "
                    "states how far it covers in each second."},
            {"text": "300 000 000 metres travelled every second",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e29",
        "band": "easier",
        "text": "The rounded figure 300 000 000 m/s for the speed of light in "
                "a vacuum…",
        "options": [
            {"text": "is close to the exact value, which is "
                     "299 792 458 m/s", "correct": True},
            {"text": "is far too small, and the true value is far higher",
             "correct": False,
             "why": "The true value is extremely close to it, not far "
                    "higher."},
            {"text": "is exactly right, with no rounding involved",
             "correct": False,
             "why": "It has been rounded — the exact value is a little "
                    "less, at 299 792 458 m/s."},
            {"text": "applies just to light travelling through air",
             "correct": False,
             "why": "It is the vacuum value. Light in air is very close to "
                    "it but not travelling through air itself."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-e30",
        "band": "easier",
        "text": "Does the speed of light in a vacuum change with distance "
                "from the Sun?",
        "options": [
            {"text": "Yes — it slows down far from the Sun", "correct": False,
             "why": "The speed of light in a vacuum does not depend on "
                    "where it is."},
            {"text": "No — it is the same everywhere in a vacuum",
             "correct": True},
            {"text": "Yes — it speeds up far from the Sun", "correct": False,
             "why": "Nothing about distance from the Sun changes it; it is "
                    "the same value everywhere in a vacuum."},
            {"text": "It stays constant close to a star alone",
             "correct": False,
             "why": "It stays constant everywhere in a vacuum, near a star "
                    "or far from every star."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ──────────────────────────────────────
    {
        "id": "p7-01-s09",
        "band": "standard",
        "text": "The International Space Station orbits about 400 000 m "
                "above the ground. About how long does light take to reach "
                "it from the ground?",
        "options": [
            {"text": "About 0.0013 s", "correct": True},
            {"text": "About 0.013 s", "correct": False,
             "why": "That is ten times too long — check the position of "
                    "the decimal point."},
            {"text": "About 1.3 s", "correct": False,
             "why": "That is the time to the MOON, a thousand times "
                    "further away."},
            {"text": "About 0.00013 s", "correct": False,
             "why": "That is ten times too short."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s10",
        "band": "standard",
        "text": "Earth's diameter is about 12 800 000 m. About how long "
                "would light take to cross it?",
        "options": [
            {"text": "About 4.3 s", "correct": False,
             "why": "That is a hundred times too long — check the powers "
                    "of ten in the division."},
            {"text": "About 0.043 s", "correct": True},
            {"text": "About 0.43 s", "correct": False,
             "why": "That is ten times too long."},
            {"text": "About 0.0043 s", "correct": False,
             "why": "That is ten times too short."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s11",
        "band": "standard",
        "text": "A race starter's pistol is fired 100 m from the timing "
                "officials. Should they start the clock on the flash or the "
                "bang?",
        "options": [
            {"text": "The bang — sound is more reliable to detect than "
                     "light", "correct": False,
             "why": "Reliability is not the issue here. The bang simply "
                    "arrives late, which throws the timing off."},
            {"text": "Either — the two arrive at effectively the same time "
                     "once you are only 100 m from the starting shot",
             "correct": False,
             "why": "The bang would be about 0.3 s late over that "
                    "distance, which is far too much for accurate timing."},
            {"text": "The flash — the bang would arrive about 0.3 s late, "
                     "at 100 m ÷ 340 m/s", "correct": True},
            {"text": "The bang — light genuinely takes far too long to "
                     "notice from as little as 100 m away", "correct": False,
             "why": "Light over 100 m arrives in a fraction of a "
                    "millionth of a second — effectively unnoticeable."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s12",
        "band": "standard",
        "text": "Roughly how many hours does a radio signal take to reach "
                "Voyager 1, currently about 24 000 000 000 000 m away?",
        "options": [
            {"text": "About 2.2 hours", "correct": False,
             "why": "That is ten times too short."},
            {"text": "About 80 seconds", "correct": False,
             "why": "That leaves out several powers of ten in the "
                    "distance."},
            {"text": "About 220 hours", "correct": False,
             "why": "That is ten times too long."},
            {"text": "About 22 hours", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s13",
        "band": "standard",
        "text": "You count 9 seconds between a lightning flash and the "
                "thunder. About how far away did the strike happen?",
        "options": [
            {"text": "About 3 km", "correct": True},
            {"text": "About 9 km", "correct": False,
             "why": "That treats each second as a kilometre, when sound "
                    "covers about a third of a kilometre a second."},
            {"text": "About 30 km", "correct": False,
             "why": "That is ten times too far."},
            {"text": "About 0.3 km", "correct": False,
             "why": "That is ten times too close — check 9 × 340 in "
                    "metres."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s14",
        "band": "standard",
        "text": "Moonlight is sunlight reflected off the Moon. Roughly how "
                "much later does moonlight reach us than sunlight leaving "
                "the Sun at the same instant, and why?",
        "options": [
            {"text": "About 500 seconds later, because moonlight has to "
                     "cross the whole Sun-Earth distance twice",
             "correct": False,
             "why": "That double-counts the Sun-to-Earth leg, which "
                    "moonlight and direct sunlight both share."},
            {"text": "About 1.3 seconds later — the extra time is the "
                     "final hop from the Moon to the Earth", "correct": True},
            {"text": "No later, because reflection happens instantly",
             "correct": False,
             "why": "The reflected light still has to cross the extra "
                    "gap from the Moon to the Earth, which takes real "
                    "time."},
            {"text": "About 8 minutes later, because moonlight makes the "
                     "same journey as sunlight all over again from the "
                     "Moon", "correct": False,
             "why": "Only the short final Moon-to-Earth hop is extra, not "
                    "the whole Sun-to-Earth journey again."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s15",
        "band": "standard",
        "text": "A spacecraft sends a photo of Jupiter from about "
                "600 000 000 000 m away. Roughly how many minutes does the "
                "signal take to arrive?",
        "options": [
            {"text": "About 3.3 minutes", "correct": False,
             "why": "That is ten times too short."},
            {"text": "About 333 minutes", "correct": False,
             "why": "That is ten times too long."},
            {"text": "About 33 minutes", "correct": True},
            {"text": "About 2000 minutes", "correct": False,
             "why": "That treats the answer in seconds as if it were "
                    "already minutes, without dividing by 60."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s16",
        "band": "standard",
        "text": "Suppose light travelled at only twice the speed of sound, "
                "instead of the enormous margin it really has. What would "
                "change about watching a distant thunderstorm?",
        "options": [
            {"text": "Thunder would arrive before the lightning",
             "correct": False,
             "why": "Light would still be faster than sound, just not by "
                    "nearly as much, so the order would not reverse."},
            {"text": "There would be no noticeable gap between them",
             "correct": False,
             "why": "A speed difference, even a small one, still produces "
                    "a gap over any real distance."},
            {"text": "The thunder would become completely silent to every "
                     "listener, because sound cannot exist at all once "
                     "light slows down", "correct": False,
             "why": "Sound and light are independent of one another; "
                    "changing light's speed does nothing to sound."},
            {"text": "You would notice a short gap between the flash and "
                     "the bang too, instead of the flash appearing instant",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s17",
        "band": "standard",
        "text": "A torch is flashed across a 3 km gap between two hilltop "
                "stations. About how long does the flash take to cross?",
        "options": [
            {"text": "About 0.00001 s (10 millionths of a second)",
             "correct": True},
            {"text": "No time at all — the gap is small enough to be "
                     "instant", "correct": False,
             "why": "It is very fast but never truly instant, over any "
                    "distance."},
            {"text": "About 0.01 s", "correct": False,
             "why": "That is a thousand times too long."},
            {"text": "About 0.0000001 s", "correct": False,
             "why": "That is a hundred times too short."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s18",
        "band": "standard",
        "text": "Which of these light journeys takes the longest time to "
                "complete?",
        "options": [
            {"text": "From the Sun to the Earth", "correct": False,
             "why": "That takes about 500 s, far less than the longest of "
                    "these journeys."},
            {"text": "From Voyager 1 to the Earth", "correct": True},
            {"text": "From the ground to the International Space Station",
             "correct": False,
             "why": "That is the shortest of the four, at about 0.0013 s."},
            {"text": "From the Earth all the way to the Moon",
             "correct": False,
             "why": "That takes only about 1.3 s."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s19",
        "band": "standard",
        "text": "A star 4 light years away explodes right now. When will we "
                "see it explode?",
        "options": [
            {"text": "In 4 minutes", "correct": False,
             "why": "4 minutes is closer to a journey across a small part "
                    "of the Solar System, not to a nearby star."},
            {"text": "Immediately, because it is close enough",
             "correct": False,
             "why": "Even 4 light years is a huge distance — the light "
                    "still takes 4 years to arrive."},
            {"text": "In 4 years' time", "correct": True},
            {"text": "The light will fade away before it ever arrives",
             "correct": False,
             "why": "Light from an exploding star does not simply fade "
                    "away before arriving; it keeps travelling until it "
                    "reaches us."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s20",
        "band": "standard",
        "text": "Two torches are flashed at the same instant, one 1 km away "
                "and one 2 km away from an observer. Which flash is seen "
                "first, and by about how much?",
        "options": [
            {"text": "The 2 km torch, because a longer journey warms the "
                     "light up and speeds it slightly", "correct": False,
             "why": "Distance does not change the speed of light in air. "
                    "Nothing warms it up."},
            {"text": "Both at once — light does not take a measurable time "
                     "over a few kilometres", "correct": False,
             "why": "There is a real, calculable gap of a few millionths "
                    "of a second, even if it is too small to notice by "
                    "eye."},
            {"text": "The 1 km torch, by about 1 second", "correct": False,
             "why": "That is millions of times too large a gap for these "
                    "distances."},
            {"text": "The 1 km torch, by about 0.0000033 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s21",
        "band": "standard",
        "text": "Which pair correctly gives the approximate speed of light "
                "and the approximate speed of sound in air?",
        "options": [
            {"text": "300 000 000 m/s and 340 m/s", "correct": True},
            {"text": "340 m/s and 300 000 000 m/s", "correct": False,
             "why": "The two figures are the right way round the wrong "
                    "way — swap light and sound back over."},
            {"text": "300 000 m/s and 34 m/s", "correct": False,
             "why": "Both figures here are a thousand and ten times too "
                    "small respectively."},
            {"text": "3 000 000 m/s and 3400 m/s", "correct": False,
             "why": "Both figures are wrong by a factor of a hundred and "
                    "ten."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s22",
        "band": "standard",
        "text": "Why do astronomers usually give the distance to a star in "
                "light years rather than in kilometres?",
        "options": [
            {"text": "Because kilometres cannot properly be used to "
                     "measure anything outside our own Solar System",
             "correct": False,
             "why": "Kilometres would work fine; the numbers would just be "
                    "extremely unwieldy."},
            {"text": "Because the distances are so enormous that the "
                     "numbers in kilometres would be unwieldy",
             "correct": True},
            {"text": "Because light years are more accurate than "
                     "kilometres", "correct": False,
             "why": "A light year is not a more accurate measurement, "
                    "just a more convenient-sized one for huge distances."},
            {"text": "Because a kilometre is too large a unit for "
                     "astronomy", "correct": False,
             "why": "A kilometre is far too SMALL a unit for these "
                    "distances, not too large."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s23",
        "band": "standard",
        "text": "A radio pulse takes 0.0002 s to reach a weather balloon. "
                "How far away is the balloon?",
        "options": [
            {"text": "6000 m (6 km)", "correct": False,
             "why": "That is ten times too small — check the calculation "
                    "again."},
            {"text": "600 000 m (600 km)", "correct": False,
             "why": "That is ten times too large."},
            {"text": "60 000 m (60 km)", "correct": True},
            {"text": "0.0002 m", "correct": False,
             "why": "That confuses the given time with the answer, and "
                    "leaves the speed of light out of the sum entirely."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s24",
        "band": "standard",
        "text": "If the Earth-Sun distance were doubled, with the speed of "
                "light unchanged, what would happen to the 500 s light "
                "travel time?",
        "options": [
            {"text": "It would halve", "correct": False,
             "why": "Doubling the distance does the opposite of halving "
                    "the time it takes to cross it."},
            {"text": "It would stay the same, because the speed of light "
                     "is constant", "correct": False,
             "why": "The speed staying constant is exactly why the time "
                    "changes: the same speed over double the distance "
                    "takes double the time."},
            {"text": "It would quadruple instead, reaching about 2000 s",
             "correct": False,
             "why": "Time is directly proportional to distance here, not "
                    "to distance squared."},
            {"text": "It would double too, to about 1000 s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s25",
        "band": "standard",
        "text": "A student measures light's speed through open air over a "
                "very long distance and gets a value very slightly below "
                "300 000 000 m/s. What is the best explanation?",
        "options": [
            {"text": "Air is not quite a vacuum, so light travels through "
                     "it very slightly more slowly than its vacuum value",
             "correct": True},
            {"text": "The student's instrument must be faulty, since "
                     "light travels at exactly the same speed through "
                     "every material", "correct": False,
             "why": "Light genuinely does travel more slowly through air "
                    "than through a vacuum, so the instrument need not be "
                    "at fault at all."},
            {"text": "Light slows down permanently the further it has "
                     "travelled from its source", "correct": False,
             "why": "Light does not keep slowing down as it goes; its "
                    "speed depends only on the material it is in at that "
                    "moment."},
            {"text": "The measurement must include time lost reflecting "
                     "off dust in the air, rather than a genuine change "
                     "of speed", "correct": False,
             "why": "Air itself, not stray dust, is what genuinely slows "
                    "light very slightly compared with a vacuum."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s26",
        "band": "standard",
        "text": "A signal is sent from Earth to the Moon and echoed straight "
                "back. About how long is the round trip?",
        "options": [
            {"text": "About 1.3 s", "correct": False,
             "why": "That is only the one-way trip; the echo has to come "
                    "back as well."},
            {"text": "About 2.6 s", "correct": True},
            {"text": "About 0.65 s", "correct": False,
             "why": "That halves the one-way time instead of doubling "
                    "it."},
            {"text": "About 5.2 s", "correct": False,
             "why": "That doubles the round trip a second time by "
                    "mistake."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s27",
        "band": "standard",
        "text": "A conversation between Mission Control and an astronaut on "
                "the Moon has a noticeable lag in it. Why can't this be "
                "fixed by using a faster radio system?",
        "options": [
            {"text": "Because the Moon's low gravity slows electronics "
                     "down", "correct": False,
             "why": "Gravity does not affect how fast electronic signals "
                    "travel."},
            {"text": "It can be fixed — a stronger transmitter would "
                     "remove the delay", "correct": False,
             "why": "A stronger signal arrives more clearly, not sooner. "
                    "The travel time is unchanged."},
            {"text": "Because the lag is caused by the travel time of the "
                     "signal itself, which no radio equipment can shorten",
             "correct": True},
            {"text": "The lag is ordinary radio static in Earth's "
                     "atmosphere, not the distance", "correct": False,
             "why": "The lag is the light-speed travel time across a real "
                    "distance, not interference along the way."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s28",
        "band": "standard",
        "text": "The 'count the seconds, divide by three' rule for judging "
                "thunderstorm distance in kilometres works because…",
        "options": [
            {"text": "sound and light travel at the same average speed "
                     "over any distance", "correct": False,
             "why": "The two speeds are wildly different; the rule works "
                    "for a different reason."},
            {"text": "thunder is exactly three seconds long every time",
             "correct": False,
             "why": "How long the thunder rumbles has nothing to do with "
                    "how far away the strike was."},
            {"text": "lightning strikes exactly one kilometre away "
                     "every time", "correct": False,
             "why": "The distance is whatever the counted seconds work "
                    "out to, not a fixed one kilometre."},
            {"text": "the light arrives so quickly that essentially all "
                     "the delay you time is the sound's travel time",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s29",
        "band": "standard",
        "text": "A signal travelling at the speed of light takes 0.5 s to "
                "reach a robot, and its acknowledgement takes another "
                "0.5 s to return. How far away is the robot?",
        "options": [
            {"text": "150 000 000 m", "correct": True},
            {"text": "300 000 000 m", "correct": False,
             "why": "That uses the full 1 s round trip as though it were "
                    "the one-way distance."},
            {"text": "75 000 000 m", "correct": False,
             "why": "That halves the one-way time again by mistake."},
            {"text": "1 500 000 000 m", "correct": False,
             "why": "That is ten times too far for a 0.5 s one-way "
                    "journey."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-s30",
        "band": "standard",
        "text": "A camera flash used indoors seems to light every part of a "
                "large room at once. What is the best explanation?",
        "options": [
            {"text": "Light does not travel across a room; it already "
                     "fills every corner", "correct": False,
             "why": "Light does travel across the room; it just does so "
                    "far too quickly to notice."},
            {"text": "Even across a large room, the light's travel time is "
                     "far too small for the eye to detect", "correct": True},
            {"text": "The flash bounces off the walls instantly, "
                     "cancelling any delay", "correct": False,
             "why": "Reflecting off a wall takes time too, and adds to the "
                    "journey rather than cancelling it."},
            {"text": "The eye can only detect light delay outdoors",
             "correct": False,
             "why": "The eye works the same way indoors or outdoors; the "
                    "delay is simply too small either way over a room's "
                    "width."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "p7-01-h09",
        "band": "harder",
        "text": "Since 1983 the metre has not been a separate standard of "
                "its own: it is fixed by the speed of light together with "
                "the second. Why can the speed of light in a vacuum never "
                "be measured more precisely than it already is?",
        "options": [
            {"text": "Because measuring it more precisely would only "
                     "measure the metre more precisely, not the speed",
             "correct": True},
            {"text": "Because no instrument is fast enough to time light "
                     "over short distances", "correct": False,
             "why": "Modern clocks time light over short distances "
                    "extremely precisely; that is not the limit here."},
            {"text": "Because light's speed fluctuates slightly between "
                     "careful measurements", "correct": False,
             "why": "The speed of light in a vacuum is a fixed constant, "
                    "not one that fluctuates."},
            {"text": "Because the metre is defined independently of the "
                     "speed of light", "correct": False,
             "why": "It is the opposite: the metre is defined IN TERMS OF "
                    "the speed of light."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h10",
        "band": "harder",
        "text": "A radio signal takes 4 hours to reach a space probe. How "
                "far away is the probe?",
        "options": [
            {"text": "1 200 000 000 000 m", "correct": False,
             "why": "That comes from converting the hours incorrectly — "
                    "check how many seconds are in 4 hours."},
            {"text": "4 320 000 000 000 m", "correct": True},
            {"text": "43 200 000 000 000 m", "correct": False,
             "why": "That is ten times too far — a power of ten has gone "
                    "astray."},
            {"text": "12 000 000 000 m", "correct": False,
             "why": "That treats the 4 hours as 4 minutes instead of "
                    "converting properly to seconds."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h11",
        "band": "harder",
        "text": "A laser pulse crosses a 900 000 000 m gap in 3 s. What "
                "speed does this give, and does it match the speed of "
                "light in a vacuum?",
        "options": [
            {"text": "2 700 000 000 m/s — no, that is far too fast to be "
                     "light", "correct": False,
             "why": "That comes from multiplying the two figures instead "
                    "of dividing distance by time."},
            {"text": "300 000 000 m/s — no, real light travels far faster "
                     "than this", "correct": False,
             "why": "300 000 000 m/s IS the accepted speed of light in a "
                    "vacuum; nothing travels faster."},
            {"text": "300 000 000 m/s — yes, that matches the accepted "
                     "value", "correct": True},
            {"text": "3 m/s — no, that is far too slow", "correct": False,
             "why": "That misplaces a decimal point badly during the "
                    "division."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h12",
        "band": "harder",
        "text": "A student says: 'Because nothing travels faster than "
                "light, nothing can ever communicate instantly across any "
                "distance.' Is this a fair conclusion?",
        "options": [
            {"text": "No — over sufficiently small distances between two "
                     "points, communication genuinely becomes completely "
                     "instant", "correct": False,
             "why": "Even over a few metres the travel time is real, just "
                    "too small to detect — never truly zero."},
            {"text": "No — radio waves travel faster than light",
             "correct": False,
             "why": "Radio waves are light too, in a different part of "
                    "the spectrum, and travel at exactly the same speed in "
                    "a vacuum."},
            {"text": "Yes, but only within the Solar System",
             "correct": False,
             "why": "The reasoning holds at any distance at all, not just "
                    "within the Solar System."},
            {"text": "Yes — even the fastest possible signal takes a "
                     "real, calculable time over any distance",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h13",
        "band": "harder",
        "text": "A GPS receiver works out its distance from a satellite by "
                "timing how long a radio signal takes to arrive. Why does "
                "a tiny timing error cause a large position error?",
        "options": [
            {"text": "Because a small error in time, multiplied by the "
                     "huge speed of light, becomes a large error in "
                     "distance", "correct": True},
            {"text": "Because GPS satellites move so incredibly fast "
                     "through space that the ordinary light-speed limit "
                     "does not really apply to them", "correct": False,
             "why": "Nothing exceeds the light-speed limit, however fast "
                    "it is moving."},
            {"text": "Because radio signals from satellites are exempt "
                     "from the light-speed limit, since they carry data "
                     "rather than light", "correct": False,
             "why": "A radio signal is light, and obeys the same speed "
                    "limit as any other kind."},
            {"text": "Because GPS actually uses sound signals, which are "
                     "more affected by weather than by timing",
             "correct": False,
             "why": "GPS uses radio signals, not sound, and sound could "
                    "not cross the vacuum between a satellite and the "
                    "ground at all."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h14",
        "band": "harder",
        "text": "A probe is 360 000 000 000 m from Earth. What is the "
                "round-trip time for a radio command and its "
                "acknowledgement, in minutes?",
        "options": [
            {"text": "20 minutes", "correct": False,
             "why": "That is the one-way time only; the acknowledgement "
                    "has to travel back as well."},
            {"text": "40 minutes", "correct": True},
            {"text": "80 minutes", "correct": False,
             "why": "That doubles the round trip a second time by "
                    "mistake."},
            {"text": "1200 minutes", "correct": False,
             "why": "That leaves the answer in seconds rather than "
                    "converting it to minutes."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h15",
        "band": "harder",
        "text": "A textbook says: 'a radio signal takes about 3 minutes to "
                "reach probe A and about 15 minutes to reach probe B, so "
                "probe B must be about five times further from Earth than "
                "probe A is.' Check this reasoning.",
        "options": [
            {"text": "The reasoning is flawed, because a signal genuinely "
                     "travels at a different, measurable speed on the "
                     "longer journey than it does on the shorter one",
             "correct": False,
             "why": "Light travels at the same speed in a vacuum "
                    "everywhere; the speed is not what differs here."},
            {"text": "The reasoning is flawed, because time and distance "
                     "are unrelated for light", "correct": False,
             "why": "Time and distance are directly related for light at "
                    "a fixed speed — that is exactly why this reasoning "
                    "works."},
            {"text": "The reasoning is sound: since light travels at one "
                     "speed, the ratio of the times equals the ratio of "
                     "the distances", "correct": True},
            {"text": "The reasoning is sound, but only because the two "
                     "probes happen to lie in exactly the same direction "
                     "from the Earth as each other",
             "correct": False,
             "why": "Their directions from the Earth make no difference "
                    "to this ratio argument, which compares two separate "
                    "journeys."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h16",
        "band": "harder",
        "text": "A light pulse crosses 1200 km in 4 ms. What speed does "
                "this give, in m/s?",
        "options": [
            {"text": "0.0000000033 m/s", "correct": False,
             "why": "That divides the time by the distance rather than "
                    "the distance by the time."},
            {"text": "300 000 m/s", "correct": False,
             "why": "That is a thousand times too slow — one of the two "
                    "unit conversions has been missed."},
            {"text": "3 000 000 000 m/s", "correct": False,
             "why": "That is ten times too fast for light in a vacuum."},
            {"text": "300 000 000 m/s", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h17",
        "band": "harder",
        "text": "A student says any distance calculated using "
                "300 000 000 m/s must be wrong, since the real speed of "
                "light in a vacuum is 299 792 458 m/s. Evaluate this.",
        "options": [
            {"text": "The rounding error is tiny — less than 0.1% — so it "
                     "makes no meaningful difference to a school-level "
                     "answer", "correct": True},
            {"text": "The error is about 10%, which is too large to "
                     "ignore", "correct": False,
             "why": "The two figures differ by well under 1%, nowhere "
                    "near 10%."},
            {"text": "The rounding only matters for calculations involving "
                     "the Moon, not the Sun", "correct": False,
             "why": "The size of the rounding error does not depend on "
                    "which object is involved."},
            {"text": "The student is completely right: any rounded "
                     "figure at all makes a calculation entirely invalid "
                     "from the start", "correct": False,
             "why": "A tiny rounding error does not invalidate a "
                    "calculation; it just makes the answer slightly "
                    "approximate."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h18",
        "band": "harder",
        "text": "Light takes 2.5 minutes to cross a gap. What distance is "
                "that?",
        "options": [
            {"text": "112 500 000 000 m", "correct": False,
             "why": "That does not follow from either converting the time "
                    "correctly or leaving it in minutes."},
            {"text": "45 000 000 000 m", "correct": True},
            {"text": "750 000 000 m", "correct": False,
             "why": "That treats 2.5 as if it were already in seconds, "
                    "without converting the minutes first."},
            {"text": "4 500 000 000 m", "correct": False,
             "why": "That is ten times too small — check the conversion "
                    "of minutes to seconds again."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h19",
        "band": "harder",
        "text": "Sunlight reaches Mars by travelling about 228 000 000 000 "
                "m from the Sun, and is then reflected on to the Earth, a "
                "further 78 000 000 000 m. How long after leaving the Sun "
                "does that reflected light reach the Earth?",
        "options": [
            {"text": "About 4.3 minutes, the Mars-to-Earth leg",
             "correct": False,
             "why": "That is only the second leg. The light has already "
                    "crossed from the Sun to Mars before it starts it."},
            {"text": "About 12.7 minutes, the Sun-to-Mars leg",
             "correct": False,
             "why": "That is only the first leg, and it stops the clock "
                    "at Mars rather than at the Earth."},
            {"text": "About 17 minutes", "correct": True},
            {"text": "About 34 minutes, for the whole journey",
             "correct": False,
             "why": "That doubles the journey, as though the light had to "
                    "come back again. It only travels out once."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h20",
        "band": "harder",
        "text": "The nearest star beyond the Sun is about "
                "40 000 000 000 000 000 m away. Given that one light "
                "year is about 9 500 000 000 000 000 m, roughly how many "
                "years does its light take to reach Earth?",
        "options": [
            {"text": "About 40 years", "correct": False,
             "why": "That skips the division by the light-year distance "
                    "altogether."},
            {"text": "About 400 years", "correct": False,
             "why": "That uses a light-year figure a hundred times too "
                    "small."},
            {"text": "About 0.4 years", "correct": False,
             "why": "That divides the two figures the wrong way round."},
            {"text": "About 4 years", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h21",
        "band": "harder",
        "text": "A signal is sent to a probe near Mars, 78 000 000 000 m "
                "away, and the reply is sent back the instant it is "
                "received. What is the total round-trip time, in minutes?",
        "options": [
            {"text": "About 8.7 minutes", "correct": True},
            {"text": "About 4.3 minutes", "correct": False,
             "why": "That is the one-way time only, with the return leg "
                    "left out."},
            {"text": "About 17.3 minutes", "correct": False,
             "why": "That doubles the round trip a second time by "
                    "mistake."},
            {"text": "About 520 minutes", "correct": False,
             "why": "That leaves the answer in seconds instead of "
                    "converting it to minutes."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h22",
        "band": "harder",
        "text": "A science-fiction film shows two spaceships, 10 light-"
                "minutes apart, having a real-time video call with no "
                "lag at all. What is wrong with this?",
        "options": [
            {"text": "Nothing is wrong here — video calls are carried "
                     "electronically rather than by light, so the "
                     "light-speed limit simply does not apply to them",
             "correct": False,
             "why": "A video signal is carried by light or radio waves, "
                    "which are the same thing, and both obey the limit."},
            {"text": "Any signal, including light itself, would take "
                     "10 minutes to cross that distance, so a real-time "
                     "conversation is impossible", "correct": True},
            {"text": "The lag would be far smaller than 10 minutes, "
                     "because video signals travel faster than light",
             "correct": False,
             "why": "Nothing travels faster than light in a vacuum, "
                    "video signals included."},
            {"text": "The lag would only appear on very old equipment",
             "correct": False,
             "why": "The lag comes from the distance itself, not from how "
                    "modern the equipment is."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h23",
        "band": "harder",
        "text": "Star A is 10 light years away and Star B is 100 light "
                "years away. Which statement is correct?",
        "options": [
            {"text": "We are seeing both stars as they are right now, "
                     "since starlight is so bright it arrives instantly",
             "correct": False,
             "why": "Brightness has nothing to do with speed; the light "
                    "from both still takes years to arrive."},
            {"text": "We are seeing Star B more recently than Star A, "
                     "simply because it happens to look brighter overall",
             "correct": False,
             "why": "Which star looks brighter has no bearing on which "
                    "one's light is more recent — Star B's light is "
                    "actually the OLDER of the two."},
            {"text": "We are seeing Star A as it was 10 years ago, and "
                     "Star B as it was 100 years ago", "correct": True},
            {"text": "The stars themselves are 10 and 100 years old",
             "correct": False,
             "why": "A light year measures a distance, not an age. It "
                    "says nothing about how old either star is."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h24",
        "band": "harder",
        "text": "A fibre-optic chip processes a signal in about "
                "1 nanosecond (0.000000001 s). Roughly what distance "
                "would light in a vacuum cross in that time?",
        "options": [
            {"text": "About 3 m", "correct": False,
             "why": "That is ten times too far."},
            {"text": "About 300 m", "correct": False,
             "why": "That is a thousand times too far."},
            {"text": "About 0.0003 m", "correct": False,
             "why": "That is a thousand times too short."},
            {"text": "About 0.3 m (30 cm)", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h25",
        "band": "harder",
        "text": "A student calculates the time for light to cross "
                "150 000 000 000 m (the Sun's distance) as 500 seconds, "
                "then argues the Sun must be extremely close because "
                "'500 is a small number.' What is wrong with this "
                "reasoning?",
        "options": [
            {"text": "500 seconds is not a small amount of time — it is "
                     "over eight minutes, and a small number of seconds "
                     "does not mean a small distance", "correct": True},
            {"text": "The error is in the distance figure, which should "
                     "be far smaller than 150 000 000 000 m",
             "correct": False,
             "why": "The distance to the Sun really is about that large; "
                    "it is not the mistake here."},
            {"text": "Nothing is wrong — 500 is indeed a small number, "
                     "so the reasoning is valid", "correct": False,
             "why": "500 seconds is over eight minutes, which is not a "
                    "small amount of time by everyday standards."},
            {"text": "The error is that seconds cannot be used to judge "
                     "distance at all", "correct": False,
             "why": "Seconds combined with a known speed give exactly the "
                    "distance — that part of the method is sound."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h26",
        "band": "harder",
        "text": "A pulse of light is measured crossing a 60 000 000 000 m "
                "gap in 200 s. Does this match the accepted speed of "
                "light in a vacuum?",
        "options": [
            {"text": "No — dividing gives 3 000 000 000 m/s, ten times "
                     "too fast", "correct": False,
             "why": "That comes from a slip of one decimal place in the "
                    "division, not the true result."},
            {"text": "Yes — dividing gives 300 000 000 m/s, matching the "
                     "accepted value", "correct": True},
            {"text": "No — dividing gives 30 000 000 m/s, which is ten "
                     "times too slow to be right", "correct": False,
             "why": "That is a decimal-place slip in the other direction; "
                    "the true division gives a different figure."},
            {"text": "It cannot be checked, because speed cannot be "
                     "worked out from a distance and a time",
             "correct": False,
             "why": "Speed is exactly distance divided by time — that is "
                    "precisely how it is checked."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h27",
        "band": "harder",
        "text": "Which correctly ranks these three delays from shortest to "
                "longest: light crossing a 5 m room, light reaching us "
                "from the Moon, and light reaching us from the Sun?",
        "options": [
            {"text": "Moon, then room, then Sun", "correct": False,
             "why": "The room is by far the shortest of the three, not "
                    "the Moon."},
            {"text": "Sun, then Moon, then room", "correct": False,
             "why": "That is the exact reverse of the correct order."},
            {"text": "Room, then Moon, then Sun", "correct": True},
            {"text": "Room, then Sun, then Moon", "correct": False,
             "why": "The Sun's journey takes far longer than the Moon's, "
                    "so the last two are swapped."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h28",
        "band": "harder",
        "text": "A radio message is sent from Earth and its reply arrives "
                "2 minutes and 30 seconds later, having bounced off a "
                "spacecraft and returned. How far away was the spacecraft "
                "when the signal reflected?",
        "options": [
            {"text": "45 000 000 000 m", "correct": False,
             "why": "That treats the whole 150 s as a one-way trip, "
                    "rather than halving it first for the round trip."},
            {"text": "11 250 000 000 m", "correct": False,
             "why": "That halves the one-way time a second time by "
                    "mistake."},
            {"text": "3 375 000 000 000 m", "correct": False,
             "why": "That treats the full 150 s as the time for the "
                    "whole calculation without first finding the one-way "
                    "leg."},
            {"text": "22 500 000 000 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h29",
        "band": "harder",
        "text": "Which is the best reason astronomers say 'looking at a "
                "distant galaxy is like looking back in time', rather "
                "than simply 'far away things are old'?",
        "options": [
            {"text": "Because what we actually see is old light, "
                     "whatever the galaxy itself is doing right now",
             "correct": True},
            {"text": "Because telescopes slow light down as it enters "
                     "the lens", "correct": False,
             "why": "A telescope gathers light; it does not slow it down "
                    "in any lasting way."},
            {"text": "Because galaxies genuinely travel backwards through "
                     "time as they age", "correct": False,
             "why": "Nothing travels backwards through time. The galaxy "
                    "itself ages forwards, as usual."},
            {"text": "Because distant galaxies are literally built from "
                     "older material than any of the nearby ones",
             "correct": False,
             "why": "The AGE of the material is not the point — the "
                    "OLDNESS of the light arriving is."},
        ],
        "figure": None,
    },
    {
        "id": "p7-01-h30",
        "band": "harder",
        "text": "A student claims the 'flash before bang' rule for "
                "lightning would work exactly the same on the Moon as on "
                "Earth. Are they right?",
        "options": [
            {"text": "Yes — the light from the strike would still arrive "
                     "first, by the very same huge margin as on Earth",
             "correct": False,
             "why": "There would be no sound at all to compare it "
                    "against, since the Moon has no air to carry one."},
            {"text": "No — on the Moon there is no air, so there would be "
                     "no bang to time at all", "correct": True},
            {"text": "Yes — the Moon's lower gravity makes sound travel "
                     "faster there", "correct": False,
             "why": "Sound cannot travel on the Moon at all; there is no "
                    "air for it to travel through."},
            {"text": "No — sound actually travels faster on the Moon, so "
                     "the bang would arrive there first", "correct": False,
             "why": "Sound does not travel on the Moon's surface at all, "
                    "whatever its speed would be elsewhere."},
        ],
        "figure": None,
    },
]
