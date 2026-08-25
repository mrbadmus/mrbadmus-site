"""P6 lesson 01 — Waves on water: twelve questions (MRB-223).

Written against Design's page. The harbour buoy, the wave anatomy panel and
the ripple tank are hers.

The discriminations, in the order the lesson builds them:

  · the WATER stays put and the DISTURBANCE travels (`WAVE-01`);
  · amplitude is measured from the REST LINE, not trough to crest
    (`WAVE-03`);
  · bigger and longer are two different measurements (`WAVE-02`);
  · a wave whose water only rises and falls is still travelling, and
    carrying energy while it does (`WAVE-04`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — the twelve indices are 1,3,0,2 · 2,0,3,1 ·
3,1,2,0, giving three of each.

⚠️ EVERY DISTRACTOR STATES A COMPLETE WRONG RULE, and that is MRB-177's
remedy rather than a style. Three sets here had the correct answer as the
longest option by the gate's own threshold — four words clear, or 1.4× —
which lets a student score them without reading them. The correct answers
are untouched; the short distractors were finished.

⚠️ The ladder's own two marked rungs are NOT restated; check 6 of
`verify_questions.py` forbids it.
"""

UNIT = "P6"
LESSON = "waves-on-water"
LESSON_NUMBER = 1

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-01-e01",
        "band": "easier",
        "text": "The highest point of a wave is called the…",
        "options": [
            {"text": "trough", "correct": False,
             "why": "The trough is the lowest point, not the highest."},
            {"text": "crest", "correct": True},
            {"text": "amplitude", "correct": False,
             "why": "The amplitude is a distance, not a place on the wave."},
            {"text": "wavelength", "correct": False,
             "why": "The wavelength is a distance along the wave, not a "
                    "point on it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e02",
        "band": "easier",
        "text": "The wavelength of a water wave is measured…",
        "options": [
            {"text": "from the rest line up to a crest", "correct": False,
             "why": "That is the amplitude — how far the water moves, not "
                    "how long the wave is."},
            {"text": "from a crest down to the trough beside it",
             "correct": False,
             "why": "That is a height, and it is twice the amplitude. The "
                    "wavelength runs along the wave, not up and down it."},
            {"text": "from the front of the wave to the back of the whole "
                     "set of waves", "correct": False,
             "why": "That would measure the whole train of waves. A "
                    "wavelength is the length of one of them."},
            {"text": "from one crest to the very next crest",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e03",
        "band": "easier",
        "text": "A wave passes under a floating buoy. What does the buoy "
                "mostly do?",
        "options": [
            {"text": "It rises and falls, and stays roughly where it was",
             "correct": True},
            {"text": "It is carried along with the wave towards the shore",
             "correct": False,
             "why": "If the water travelled with the wave, every floating "
                    "thing would be swept along and the sea would empty "
                    "itself onto the beach."},
            {"text": "It is pushed downwards and held under", "correct": False,
             "why": "The buoy goes both up and down as the wave passes; "
                    "nothing holds it under."},
            {"text": "It stays perfectly still, because only the water "
                     "moves", "correct": False,
             "why": "The water does move — up and down — and the buoy moves "
                    "with it. What it does not do is travel along."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e04",
        "band": "easier",
        "text": "A water wave is described as transverse. That means the "
                "water moves…",
        "options": [
            {"text": "in the same direction as the wave travels",
             "correct": False,
             "why": "That describes a longitudinal wave, which is how sound "
                    "behaves. Water waves are not like that."},
            {"text": "in circles that carry it steadily forwards",
             "correct": False,
             "why": "Water particles do move in small loops, but they end up "
                    "where they started. Nothing is carried steadily "
                    "forwards."},
            {"text": "at right angles to the direction the wave travels",
             "correct": True},
            {"text": "faster than the wave itself does", "correct": False,
             "why": "The water is not racing the wave. It is going up and "
                    "down while the wave goes along."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-01-s01",
        "band": "standard",
        "text": "A wave has an amplitude of 12 cm. How far is it from the "
                "bottom of a trough to the top of a crest?",
        "options": [
            {"text": "6 cm", "correct": False,
             "why": "That is half the amplitude. The amplitude is already "
                    "the distance from the rest line to a crest."},
            {"text": "12 cm", "correct": False,
             "why": "12 cm is rest line to crest. Trough to crest goes the "
                    "same distance again on the other side."},
            {"text": "24 cm", "correct": True},
            {"text": "It cannot be worked out without the wavelength",
             "correct": False,
             "why": "The wavelength is a length along the wave and has "
                    "nothing to do with how high or low the water goes."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s02",
        "band": "standard",
        "text": "Two waves have the same wavelength, but one has twice the "
                "amplitude of the other. How do they differ?",
        "options": [
            {"text": "One moves the water twice as far up and down, and the "
                     "crests are the same distance apart", "correct": True},
            {"text": "One has crests twice as far apart, and moves the water "
                     "the same distance, so the two are the same height and "
                     "one of them is simply longer", "correct": False,
             "why": "Crests being further apart is a longer wavelength, and "
                    "the question says the wavelengths are equal."},
            {"text": "One travels twice as fast as the other",
             "correct": False,
             "why": "Amplitude says how far the water moves, not how quickly "
                    "the wave gets along."},
            {"text": "One is transverse and the other is longitudinal",
             "correct": False,
             "why": "Both are water waves, so both are transverse. Amplitude "
                    "does not change what kind of wave something is."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s03",
        "band": "standard",
        "text": "A duck sits on a pond. A stone is dropped some way off and "
                "ripples reach the duck. Which is the best description of "
                "what has arrived?",
        "options": [
            {"text": "Water from the place the stone landed",
             "correct": False,
             "why": "The water at the duck was already there. Nothing has "
                    "been delivered from the splash."},
            {"text": "A push of air travelling just above the surface",
             "correct": False,
             "why": "The ripples are in the water, not the air, and they "
                    "would still arrive under a lid."},
            {"text": "Nothing has arrived — the duck is simply bobbing on "
                     "its own", "correct": False,
             "why": "Something certainly arrived: the duck was still until "
                    "the stone was dropped, and it started moving afterwards."},
            {"text": "Energy, carried by a disturbance passing through water "
                     "that stays where it is", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s04",
        "band": "standard",
        "text": "In a ripple tank the dipper is made to bob up and down more "
                "often, and nothing else is changed. What happens to the "
                "pattern on the water?",
        "options": [
            {"text": "The waves become taller", "correct": False,
             "why": "How high the waves are is set by how far the dipper "
                    "moves each time, not by how often it moves."},
            {"text": "The crests get closer together", "correct": True},
            {"text": "The waves stop travelling outwards", "correct": False,
             "why": "They keep travelling outwards; bobbing more often does "
                    "not stop the disturbance spreading."},
            {"text": "The water starts moving along with the waves",
             "correct": False,
             "why": "The water goes on rising and falling wherever it is. "
                    "Nothing about the dipper changes that."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-01-h01",
        "band": "harder",
        "text": "A storm a thousand kilometres out at sea sends waves that "
                "arrive on a beach two days later. What has crossed the "
                "ocean?",
        "options": [
            {"text": "Water pushed all the way from under the storm",
             "correct": False,
             "why": "For that to be true the sea would have to be a "
                    "thousand kilometres emptier where the storm was, and it "
                    "is not."},
            {"text": "Wind that was made by the storm and has been blowing "
                     "ever since", "correct": False,
             "why": "The swell arrives on days with no wind at all, which is "
                    "how surfers know a distant storm has happened."},
            {"text": "Nothing crossed — the beach makes its own waves and "
                     "the timing is a coincidence", "correct": False,
             "why": "The size and spacing of the arriving swell match the "
                    "storm that made it, and it can be predicted days ahead."},
            {"text": "A disturbance, carrying energy through water that "
                     "only ever rose and fell in place", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h02",
        "band": "harder",
        "text": "A student says a big wave must be a long wave, because it "
                "is bigger. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — height and length always go "
                     "together on water", "correct": False,
             "why": "They can go together and they need not. Steep, short "
                    "waves in a gale and low, very long ocean swell are both "
                    "ordinary."},
            {"text": "Big and long are two different measurements: "
                     "amplitude is how far the water moves, wavelength is "
                     "how far apart the crests are", "correct": True},
            {"text": "Nothing can be big and long at the same time, because "
                     "the water would run out — a wave can be tall or "
                     "widely spaced, and taking one always costs the other",
             "correct": False,
             "why": "A very large ocean swell is both. There is no rule "
                    "stopping one wave being tall and widely spaced."},
            {"text": "Waves have no length, only height", "correct": False,
             "why": "Wavelength is the distance from one crest to the next, "
                    "and it is a perfectly real measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h03",
        "band": "harder",
        "text": "A line of corks floats on a pond as ripples pass. Which "
                "observation would show that the wave, and not the water, is "
                "what travels?",
        "options": [
            {"text": "The corks all bunch up at the far side of the pond",
             "correct": False,
             "why": "That is what you would see if the water DID travel, so "
                    "it would show the opposite of what is wanted."},
            {"text": "The corks stop moving as soon as the ripples pass",
             "correct": False,
             "why": "True, but it only shows the disturbance has gone by. It "
                    "says nothing about whether the water moved along."},
            {"text": "Each cork rises and falls in turn and every one ends "
                     "up where it started", "correct": True},
            {"text": "The corks nearest the splash move first",
             "correct": False,
             "why": "That shows the disturbance spreads outwards, which is "
                    "not in doubt. It does not show whether the water "
                    "travelled with it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h04",
        "band": "harder",
        "text": "Why is amplitude measured from the rest line rather than "
                "from the bottom of a trough?",
        "options": [
            {"text": "Because the rest line is where the water sits when "
                     "nothing is disturbing it, so the amplitude says how "
                     "far the disturbance moves it", "correct": True},
            {"text": "Because troughs are harder to see than crests, and a "
                     "measurement should always start from the part of the "
                     "wave that is easiest to find", "correct": False,
             "why": "Both are equally visible. The reason is about what the "
                    "measurement means, not about how easy it is to spot."},
            {"text": "Because the trough is below the water and cannot be "
                     "measured", "correct": False,
             "why": "The trough is part of the surface and can be measured "
                    "perfectly well."},
            {"text": "Because measuring from the trough would give a number "
                     "that changes with wavelength, and a measurement that "
                     "moves when a different quantity moves is no "
                     "measurement at all", "correct": False,
             "why": "Trough-to-crest is simply twice the amplitude, whatever "
                    "the wavelength. The problem is meaning, not arithmetic."},
        ],
        "figure": None,
    },
]
