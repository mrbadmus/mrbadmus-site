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
            {"text": "from the rest line up to the highest point of the "
                     "crest above it", "correct": False,
             "why": "That is the amplitude — how far the water moves, not "
                    "how long the wave is."},
            {"text": "from the top of a crest down to the bottom of the "
                     "trough beside it", "correct": False,
             "why": "That is a height, and it is twice the amplitude. The "
                    "wavelength runs along the wave, not up and down it."},
            {"text": "from the front of the wave to the back of the whole "
                     "set of waves", "correct": False,
             "why": "That would measure the whole train of waves. A "
                    "wavelength is the length of one of them."},
            {"text": "from the top of one crest along to the top of the "
                     "next crest", "correct": True},
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
            {"text": "in the same direction as the wave itself travels",
             "correct": False,
             "why": "That describes a longitudinal wave, which is how sound "
                    "behaves. Water waves are not like that."},
            {"text": "in circles that carry it steadily forwards with the "
                     "wave", "correct": False,
             "why": "Water particles do move in small loops, but they end up "
                    "where they started. Nothing is carried steadily "
                    "forwards."},
            {"text": "at right angles to the direction the wave travels",
             "correct": True},
            {"text": "faster than the wave itself does across the surface",
             "correct": False,
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
            {"text": "One moves the water twice as far up and down, and "
                     "the crests stay the same distance apart, so one is "
                     "taller and both are the same length", "correct": True},
            {"text": "One has crests twice as far apart, and moves the water "
                     "the same distance, so the two are the same height and "
                     "one of them is simply longer", "correct": False,
             "why": "Crests being further apart is a longer wavelength, and "
                    "the question says the wavelengths are equal."},
            {"text": "One travels twice as fast as the other, because a "
                     "wave that moves the water further must also be "
                     "getting along the tank more quickly", "correct": False,
             "why": "Amplitude says how far the water moves, not how quickly "
                    "the wave gets along."},
            {"text": "One is transverse and the other is longitudinal, "
                     "because doubling how far the water moves changes the "
                     "direction in which it moves", "correct": False,
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
            {"text": "Water carried across the pond all the way from the "
                     "place the stone landed", "correct": False,
             "why": "The water at the duck was already there. Nothing has "
                    "been delivered from the splash."},
            {"text": "A push of air travelling just above the surface of "
                     "the water, ahead of it", "correct": False,
             "why": "The ripples are in the water, not the air, and they "
                    "would still arrive under a lid."},
            {"text": "Nothing has arrived — the duck is simply bobbing "
                     "about on its own account", "correct": False,
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
            {"text": "The waves become taller, but no closer together",
             "correct": False,
             "why": "How high the waves are is set by how far the dipper "
                    "moves each time, not by how often it moves."},
            {"text": "The crests get closer together, but no taller",
             "correct": True},
            {"text": "The waves stop spreading outwards from the dipper",
             "correct": False,
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
            {"text": "Nothing is wrong at all — height and length always "
                     "go together on water, so any wave that is bigger in "
                     "the one way must be bigger in the other way as well",
             "correct": False,
             "why": "They can go together and they need not. Steep, short "
                    "waves in a gale and low, very long ocean swell are both "
                    "ordinary."},
            {"text": "Big and long are two different measurements: "
                     "amplitude is how far the water moves up and down, "
                     "and wavelength is how far apart the crests are",
             "correct": True},
            {"text": "Nothing can be big and long at the same time, because "
                     "the water would run out — a wave can be tall or "
                     "widely spaced, and taking one always costs the other",
             "correct": False,
             "why": "A very large ocean swell is both. There is no rule "
                    "stopping one wave being tall and widely spaced."},
            {"text": "Waves have no length at all, only height, so the "
                     "only measurement there is to make on one is how tall "
                     "it stands above the rest line", "correct": False,
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
            {"text": "The corks all bunch up together at the far side of "
                     "the pond in the end", "correct": False,
             "why": "That is what you would see if the water DID travel, so "
                    "it would show the opposite of what is wanted."},
            {"text": "The corks all stop moving as soon as the ripples "
                     "have passed them by", "correct": False,
             "why": "True, but it only shows the disturbance has gone by. It "
                    "says nothing about whether the water moved along."},
            {"text": "Each cork rises and falls in turn and every one ends "
                     "up where it started", "correct": True},
            {"text": "The corks nearest the splash are always the first "
                     "ones to start moving", "correct": False,
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
                     "far the disturbance has moved it from there",
             "correct": True},
            {"text": "Because troughs are harder to see than crests, and a "
                     "measurement should always start from the part of the "
                     "wave that is easiest to find and to read off against "
                     "a ruler", "correct": False,
             "why": "Both are equally visible. The reason is about what the "
                    "measurement means, not about how easy it is to spot."},
            {"text": "Because the trough is below the level of the water "
                     "and cannot be measured, so the only place left to "
                     "start a measurement from is the rest line above it",
             "correct": False,
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

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-01-e05",
        "band": "easier",
        "text": "What does a wave carry from place to place?",
        "options": [            {"text": "Air trapped under the surface", "correct": False,
             "why": "Waves cross deep open water where no air is trapped "
                    "beneath them."},
            {"text": "The water itself, from one end of the tank to the other",
             "correct": False,
             "why": "A float bobs and stays put, so the water is not "
                    "travelling along with the wave."},
            {"text": "Nothing — a wave is only a shape on the surface",
             "correct": False,
             "why": "It certainly carries something: a distant storm can send "
                    "energy right across an ocean."},
            {"text": "Energy, without carrying the material with it",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e06",
        "band": "easier",
        "text": "The lowest point of a water wave is called the…",
        "options": [            {"text": "trough", "correct": True},
            {"text": "crest", "correct": False,
             "why": "The crest is the highest point, at the top of the wave."},
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is a distance measured from the still level, "
                    "not a place on the wave."},
            {"text": "wavelength", "correct": False,
             "why": "Wavelength is the distance from one crest to the next, "
                    "not a point."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-01-s05",
        "band": "standard",
        "text": "A wave has a wavelength of 0.80 m. How far is it from one "
                "trough to the next?",
        "options": [
            {"text": "0.40 m, because a trough is halfway along",
             "correct": False,
             "why": "Trough to CREST is half a wavelength; trough to trough is "
                    "a whole one."},
            {"text": "1.60 m", "correct": False,
             "why": "That doubles it. One full wave takes you from a trough to "
                    "the next trough."},
            {"text": "0.80 m", "correct": True},
            {"text": "It cannot be told without the amplitude",
             "correct": False,
             "why": "Amplitude is how far the surface rises, and it does not "
                    "affect the spacing at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s06",
        "band": "standard",
        "text": "A ripple-tank dipper is made to move further up and down, at "
                "the same rate as before. What changes?",
        "options": [
            {"text": "The wavelength gets longer and the amplitude stays the "
                     "same",
             "correct": False,
             "why": "The two are the wrong way round: it is how FAR it moves "
                    "that has changed, not how often."},
            {"text": "Both the amplitude and the wavelength get bigger",
             "correct": False,
             "why": "Wavelength is set by how often the dipper bobs, and that "
                    "has not changed."},
            {"text": "Neither changes, because the dipper is the same dipper",
             "correct": False,
             "why": "Moving further each time is a real change, and the waves "
                    "show it."},
            {"text": "The amplitude gets bigger and the wavelength stays the "
                     "same",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-01-h05",
        "band": "harder",
        "text": "Two wave trains cross the same tank, one with twice the "
                "amplitude of the other. Compare their energy and their "
                "wavelengths.",
        "options": [
            {"text": "The taller one carries more energy, and the wavelengths "
                     "need not differ",
             "correct": True},
            {"text": "The taller one carries more energy, so its wavelength "
                     "must be longer too",
             "correct": False,
             "why": "Amplitude and wavelength are independent — a tall wave "
                    "can be closely spaced."},
            {"text": "They carry the same energy, because the tank is the "
                     "same",
             "correct": False,
             "why": "A bigger disturbance carries more energy; that is why a "
                    "storm swell does damage."},
            {"text": "The shorter one carries more energy, because it is "
                     "packed tighter",
             "correct": False,
             "why": "Nothing about the height of these waves is set by how "
                    "tightly they are packed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h06",
        "band": "harder",
        "text": "A cork bobs up and down twenty times as a wave train passes "
                "and finishes where it began. What has crossed the tank?",
        "options": [
            {"text": "The water, which is why the cork moved", "correct": False,
             "why": "The cork ends where it started, so the water beneath it "
                    "has gone nowhere either."},
            {"text": "Nothing has crossed it — the surface simply moved up "
                     "and down",
             "correct": False,
             "why": "Something reached the far end: the disturbance arrived "
                    "there and could do work on a float."},
            {"text": "The disturbance, carrying energy with it", "correct": True},
            {"text": "Air pushed along above the surface", "correct": False,
             "why": "The wave travels just as well in still air, so moving "
                    "air is not what crossed."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-01-e07",
        "band": "easier",
        "text": "In a water wave, the amplitude is measured from…",
        "options": [
            {"text": "the bottom of a trough up to the top of the next crest",
             "correct": False,
             "why": "That distance is twice the amplitude, not the "
                    "amplitude itself."},
            {"text": "one crest along to the next crest", "correct": False,
             "why": "That is the wavelength, a distance along the wave, not "
                    "a height above it."},
            {"text": "the still water level up to the top of a crest",
             "correct": True},
            {"text": "one edge of the ripple tank to the other",
             "correct": False,
             "why": "The size of the tank has nothing to do with how far "
                    "the water itself rises."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e08",
        "band": "easier",
        "text": "Before any wave has reached it, the level the water sits at "
                "is called the…",
        "options": [
            {"text": "trough", "correct": False,
             "why": "A trough only exists once a wave is passing through; "
                    "it is a low point on a moving wave."},
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is a distance measured from this level, not "
                    "the level itself."},
            {"text": "crest", "correct": False,
             "why": "A crest is a high point on a moving wave, not the "
                    "undisturbed water."},
            {"text": "still level", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e09",
        "band": "easier",
        "text": "A wave's crest stands 6 cm above the still water level. What "
                "is the amplitude of this wave?",
        "options": [
            {"text": "3 cm", "correct": False,
             "why": "Halving isn't needed here — 6 cm above the still "
                    "level already is the amplitude."},
            {"text": "12 cm", "correct": False,
             "why": "That would be trough to crest. Only one crest height "
                    "above still level is given."},
            {"text": "6 cm", "correct": True},
            {"text": "It cannot be found without the wavelength",
             "correct": False,
             "why": "Amplitude only needs the height above the still "
                    "level; the wavelength plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e10",
        "band": "easier",
        "text": "In science, a water wave is best described as…",
        "options": [
            {"text": "a single lump of water that gets carried steadily "
                     "along, moving all the way from one place to another "
                     "as the wave itself travels forward", "correct": False,
             "why": "The water itself does not travel along; only the "
                    "disturbance does."},
            {"text": "a fixed shape that always stays over the same patch "
                     "of water", "correct": False,
             "why": "A wave's whole point is that the shape moves onward "
                    "across the water, not that it stays put."},
            {"text": "a gust of wind blowing just above the surface",
             "correct": False,
             "why": "Wind can start waves, but the wave itself is a "
                    "disturbance in the water, not moving air."},
            {"text": "a disturbance that carries energy from place to "
                     "place without carrying the water itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e11",
        "band": "easier",
        "text": "Which pair correctly matches a wave measurement to what it "
                "tells you?",
        "options": [
            {"text": "Wavelength tells you how far the water rises "
                     "above the still level with each wave that passes; "
                     "amplitude tells you the spacing between one crest "
                     "and the next crest along the wave",
             "correct": False,
             "why": "The two are swapped: amplitude is the rise, "
                    "wavelength is the spacing."},
            {"text": "Both amplitude and wavelength tell you exactly the "
                     "same thing about a wave", "correct": False,
             "why": "They measure two different things — a height and a "
                    "length — and one can change without the other."},
            {"text": "Amplitude tells you how fast the wave is travelling",
             "correct": False,
             "why": "How far the water rises says nothing about the "
                    "wave's speed across the tank."},
            {"text": "Amplitude tells you how far the water rises above "
                     "still level; wavelength tells you the spacing "
                     "between one crest and the next", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e12",
        "band": "easier",
        "text": "Two points on a wave are exactly one wavelength apart. "
                "Which pair could they be?",
        "options": [
            {"text": "A crest, and the trough right next to it",
             "correct": False,
             "why": "A crest and its neighbouring trough are only half a "
                    "wavelength apart."},
            {"text": "A crest, and the still level directly beneath it",
             "correct": False,
             "why": "That is a height above the water, not a distance "
                    "along the wave."},
            {"text": "A crest, and the very next crest along",
             "correct": True},
            {"text": "The top and the bottom of a single crest",
             "correct": False,
             "why": "A single crest does not have a 'bottom' of its own — "
                    "that phrase does not describe a real distance on the "
                    "wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e13",
        "band": "easier",
        "text": "A stone is dropped into one corner of a large, still pond. "
                "Half a second later, has the water at the far corner of "
                "the pond moved yet?",
        "options": [
            {"text": "Yes, the whole pond starts moving the instant the "
                     "stone lands", "correct": False,
             "why": "The disturbance has to travel across the pond first; "
                    "it cannot act on distant water straight away."},
            {"text": "Yes, but only right at the very edge",
             "correct": False,
             "why": "Edges are not special; the disturbance reaches every "
                    "part of the pond in the order it travels, starting "
                    "nearest the stone."},
            {"text": "It depends only on how big the pond is",
             "correct": False,
             "why": "Size sets the distance to cross, but it is still the "
                    "travel time that decides whether the disturbance has "
                    "arrived yet."},
            {"text": "No — the water there stays still until the "
                     "disturbance has had time to reach it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e14",
        "band": "easier",
        "text": "A stone is dropped into a still pond and ripples spread "
                "outward from where it landed. Where did the energy "
                "carried by those ripples originally come from?",
        "options": [
            {"text": "The stone, as it fell and struck the water",
             "correct": True},
            {"text": "The water, which already held the energy before the "
                     "stone arrived", "correct": False,
             "why": "The pond was still beforehand, so it had no wave "
                    "energy of its own to give up."},
            {"text": "The air pressing down on the surface of the pond",
             "correct": False,
             "why": "Nothing about still air pressing on the water starts "
                    "a ripple; the stone's impact does."},
            {"text": "The waves generate their own energy as they spread "
                     "outward", "correct": False,
             "why": "Energy cannot appear from nothing; it has to come "
                    "from somewhere, and here that is the falling stone."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-01-s07",
        "band": "standard",
        "text": "Wave A and Wave B both have an amplitude of 8 cm, but "
                "Wave A has a wavelength of 2 m and Wave B has a "
                "wavelength of 0.5 m. How do they compare?",
        "options": [
            {"text": "They rise the same height above the still level, "
                     "but Wave B's crests are closer together",
             "correct": True},
            {"text": "Wave B rises higher above the still level, because "
                     "its crests are packed closer together",
             "correct": False,
             "why": "Amplitude is stated as equal for both — wavelength "
                    "does not change how high either one rises."},
            {"text": "Wave A must be travelling faster, since it has the "
                     "longer wavelength", "correct": False,
             "why": "Nothing about either wave's speed has been given; "
                    "amplitude and wavelength alone don't decide it."},
            {"text": "The two waves cannot really have the same amplitude "
                     "if their wavelengths are different",
             "correct": False,
             "why": "Amplitude and wavelength are independent — either one "
                    "can be set without changing the other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s08",
        "band": "standard",
        "text": "A garden pond ripple has a wavelength of about 5 cm. An "
                "ocean swell has a wavelength of over 100 m. To say the "
                "swell is definitely a 'bigger' wave than the ripple in "
                "every sense, what extra information would you need?",
        "options": [
            {"text": "Nothing else — a much longer wavelength always means "
                     "a bigger wave in every way", "correct": False,
             "why": "That treats wavelength and amplitude as the same "
                    "thing, and they are two separate measurements."},
            {"text": "The depth of water each wave was measured in",
             "correct": False,
             "why": "Water depth isn't one of the two measurements that "
                    "decide whether a wave counts as 'bigger'."},
            {"text": "The direction each wave happens to be travelling in",
             "correct": False,
             "why": "Which way a wave travels says nothing about how tall "
                    "or how spread out it is."},
            {"text": "The amplitude of each wave", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s09",
        "band": "standard",
        "text": "A ripple 2 cm high and a storm wave 3 m high cross the same "
                "stretch of open water. Which correctly compares the "
                "energy they carry?",
        "options": [
            {"text": "They carry the same energy, because energy does not "
                     "depend on the size of a wave", "correct": False,
             "why": "A wave's amplitude is directly linked to how much "
                    "energy it carries, so equal energy isn't right here."},
            {"text": "The ripple carries more energy, because smaller "
                     "waves always travel faster", "correct": False,
             "why": "Nothing here says the ripple is faster, and even a "
                    "fast small wave would not out-carry a much taller "
                    "one."},
            {"text": "Neither carries any energy unless their wavelengths "
                     "are also known", "correct": False,
             "why": "Amplitude alone is enough to say the taller wave "
                    "carries more energy here."},
            {"text": "The storm wave carries far more energy, because it "
                     "has a much larger amplitude", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s10",
        "band": "standard",
        "text": "Three floating buoys are anchored 4 m apart in a line, "
                "with Buoy 1 nearest a distant wave source. Which buoy "
                "starts bobbing first as the waves arrive?",
        "options": [
            {"text": "All three bob at exactly the same instant",
             "correct": False,
             "why": "The disturbance takes time to travel between them, so "
                    "it cannot reach all three at once."},
            {"text": "Buoy 1, because the disturbance reaches the nearest "
                     "buoy first", "correct": True},
            {"text": "Buoy 2, because it sits between the other two",
             "correct": False,
             "why": "Being in the middle of the line does not make the "
                    "disturbance arrive there first."},
            {"text": "Buoy 3, because waves speed up the further they "
                     "travel", "correct": False,
             "why": "A travelling wave does not simply speed up on its "
                    "own; nothing here changes its speed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s11",
        "band": "standard",
        "text": "A wave of amplitude 3 cm travels 2 m across a pond in five "
                "seconds. In that time, how far sideways — in the "
                "direction the wave travels — does a floating cork end up "
                "moving?",
        "options": [
            {"text": "Roughly 2 m, the same as the wave", "correct": False,
             "why": "The cork rises and falls; it does not get carried "
                    "sideways along with the wave."},
            {"text": "About 3 cm, matching the amplitude", "correct": False,
             "why": "3 cm is a height the cork rises by, not a sideways "
                    "distance it travels."},
            {"text": "Close to 0 m — it finishes almost where it started",
             "correct": True},
            {"text": "It moves 2 m in the opposite direction to the wave",
             "correct": False,
             "why": "There is no reason for the cork to be pushed "
                    "backwards; it simply returns to about where it "
                    "began."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s12",
        "band": "standard",
        "text": "A splash sends ripples 10 m to a floating duck, and the "
                "same disturbance then carries on another 15 m to the far "
                "bank. How far in total has the disturbance itself "
                "travelled by the time it reaches the far bank?",
        "options": [
            {"text": "10 m", "correct": False,
             "why": "That only counts the first stretch, up to the duck."},
            {"text": "15 m", "correct": False,
             "why": "That only counts the second stretch, from the duck to "
                    "the bank."},
            {"text": "25 m", "correct": True},
            {"text": "It cannot have travelled the full distance, because "
                     "the duck absorbs some of the disturbance",
             "correct": False,
             "why": "A floating duck does not soak up the disturbance — it "
                    "simply bobs and lets it carry on."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s13",
        "band": "standard",
        "text": "The simple picture of a wave shows a floating object moving "
                "straight up and down as the wave passes. A closer look "
                "shows the water actually moves in small loops — forward "
                "near the crest, backward in the trough — before ending up "
                "close to where it began. Which statement fits both "
                "pictures?",
        "options": [
            {"text": "The closer look proves the simple picture is "
                     "completely wrong, and the water really is carried "
                     "along by the wave", "correct": False,
             "why": "The water still ends up close to where it began, so "
                    "it is not being carried along."},
            {"text": "The straight up-and-down picture is a simplified "
                     "version; the looping picture is more detailed, but "
                     "the water still finishes where it started either way",
             "correct": True},
            {"text": "The two pictures must describe two different kinds "
                     "of wave, not the same swell seen in two ways",
             "correct": False,
             "why": "Both pictures are describing the very same water "
                    "wave, just at different levels of detail."},
            {"text": 'The looping picture shows the water travelling forward '
                     'with the wave from one end of the pond to the other, only '
                     'more slowly than it first looks', "correct": False,
             "why": "The water in the loops still ends up close to its "
                    "starting point, so it is not travelling forward with "
                    "the wave."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-01-h07",
        "band": "harder",
        "text": "A student argues: 'Since a wave transfers energy without "
                "transferring matter, nothing physical ever actually moves "
                "when a wave passes.' What is wrong with this claim?",
        "options": [
            {"text": "Nothing is wrong — 'wave' just means a pattern, and "
                     "no real movement happens anywhere", "correct": False,
             "why": "The water genuinely rises and falls as the "
                    "disturbance passes; that is real physical movement."},
            {"text": "The water itself does physically move — rising and "
                     "falling — while what does NOT happen is the water "
                     "being carried onward with the wave", "correct": True},
            {"text": "The claim is true for water waves only, and false "
                     "for every other kind of wave, because only water is "
                     "heavy enough to carry energy without moving along "
                     "with it", "correct": False,
             "why": "The same distinction — energy moves on, matter stays "
                    "roughly put — is exactly what applies here too."},
            {"text": "The water actually does flow steadily along with the "
                     "wave from one end of the pond to the other, which "
                     "would mean energy cannot travel without matter "
                     "travelling too", "correct": False,
             "why": "The water does not flow along with the wave; it rises "
                    "and falls and returns to about where it started."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h08",
        "band": "harder",
        "text": "Wave A has amplitude 0.5 m and wavelength 20 m. Wave B has "
                "amplitude 1.5 m and wavelength 8 m. A student claims Wave "
                "A must carry more energy, because it has the longer "
                "wavelength. Assess this claim.",
        "options": [
            {"text": "The claim is correct, since a longer wavelength "
                     "always means more energy", "correct": False,
             "why": "Wavelength on its own does not decide how much "
                    "energy a wave carries; amplitude is the key "
                    "measurement here."},
            {"text": "The claim does not hold up — energy relates to "
                     "amplitude, and Wave B's much larger amplitude means "
                     "it is the one more likely carrying more energy",
             "correct": True},
            {"text": "Both waves must carry exactly identical energy, since "
                     "the sea as a whole fixes the total energy, whatever "
                     "amplitude or wavelength any one wave happens to "
                     "have", "correct": False,
             "why": "Different waves on the same sea can carry very "
                    "different amounts of energy; nothing fixes them to be "
                    "equal."},
            {"text": "The claim is only correct if the two waves also "
                     "happen to be travelling at different speeds, since "
                     "otherwise neither one could carry more energy than "
                     "the other",
             "correct": False,
             "why": "Speed is not part of what makes the claim true or "
                    "false here — amplitude is the deciding factor either "
                    "way."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h09",
        "band": "harder",
        "text": "A cork bobs on a pond as waves pass beneath it, always "
                "returning to the same height between waves. A student "
                "says: 'because the cork keeps returning to the same "
                "height, the water underneath it must never really move "
                "at all — it only looks like it moves.' What is wrong "
                "with this reasoning?",
        "options": [
            {"text": "Nothing is wrong — the water only appears to move "
                     "because of the way light reflects off a rippling "
                     "surface", "correct": False,
             "why": "The water is genuinely rising and falling; that is "
                    "not a trick of the light."},
            {"text": "It is wrong because corks float in such an "
                     "unnaturally light way that a cork could never truly "
                     "show what the real water underneath it is actually "
                     "doing", "correct": False,
             "why": "The cork's lightness isn't the issue — it faithfully "
                    "follows the water's real up-and-down motion."},
            {"text": "It is wrong because the water genuinely does rise "
                     "and fall as the disturbance passes; only its "
                     "average position over time stays the same",
             "correct": True},
            {"text": "It is wrong because the premise is false — the cork "
                     "actually is carried steadily forward with each "
                     "wave, ending up further along the pond every time "
                     "one passes",
             "correct": False,
             "why": "The premise given is true: the cork really does "
                    "return to the same height each time, so this option "
                    "denies something that is correct."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h10",
        "band": "harder",
        "text": "A sailor claims a wave only counts as 'rough' when its "
                "wavelength is short, whatever its amplitude happens to "
                "be. Assess this using amplitude and wavelength as two "
                "separate measurements.",
        "options": [
            {"text": 'The sailor is correct — wavelength alone decides how '
                     'rough a wave feels, and amplitude makes no difference to '
                     'how choppy the water seems', "correct": False,
             "why": "A long-wavelength wave can still have a large "
                    "amplitude and feel rough; wavelength alone doesn't "
                    "settle it."},
            {"text": "Roughness is really about amplitude — a long-"
                     "wavelength swell can still feel rough if it has a "
                     "large amplitude, and a short ripple can feel calm if "
                     "its amplitude is tiny", "correct": True},
            {"text": 'Roughness depends only on how fast the wave is '
                     'travelling, and neither amplitude nor wavelength has '
                     'anything to do with how rough it feels', "correct": False,
             "why": "Speed is not one of the two measurements given, and "
                    "the question asks about amplitude and wavelength "
                    "specifically."},
            {"text": "Roughness cannot be linked to any single property of a "
                     "wave, so the sailor's claim and one resting on amplitude "
                     "are equally meaningless", "correct": False,
             "why": "Roughness clearly tracks amplitude — how far the "
                    "water is displaced up and down — so it is not "
                    "meaningless."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h11",
        "band": "harder",
        "text": "A becalmed sea has no waves at all. A single passing boat "
                "sends out one wave that lifts a distant gull once and "
                "then dies away, leaving the sea calm again. A student "
                "says: 'since only one wave passed, no real energy "
                "transfer happened — you need a whole train of waves for "
                "that.' Assess this claim.",
        "options": [
            {"text": "The claim is correct, since one single wave alone "
                     "has amplitude but no wavelength of its own to carry "
                     "any real energy along with it as it travels forward",
             "correct": False,
             "why": "A single wave still has both a height and a length; "
                    "it is not missing a wavelength."},
            {"text": "The claim is correct, because energy can only ever "
                     "be transferred continuously over many repeated "
                     "waves, and never delivered in a single one-off "
                     "pulse of disturbance",
             "correct": False,
             "why": "There is no such rule — a single pulse of "
                    "disturbance is perfectly able to carry energy."},
            {"text": "The claim is wrong — a single wave is still a real "
                     "disturbance carrying energy, and lifting the gull is "
                     "itself evidence that energy reached it", "correct": True},
            {"text": "The claim is wrong, but only because the boat's own "
                     "engine happened to still be running loudly at the "
                     "exact moment that the wave itself was made", "correct": False,
             "why": "The boat's engine has nothing to do with whether the "
                    "single wave itself carried energy to the gull."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h12",
        "band": "harder",
        "text": "Out in the deep ocean, a tsunami can have an amplitude of "
                "well under 1 m spread over a wavelength of about 200 km, "
                "so a ship crossing it notices nothing unusual. As the "
                "same tsunami reaches shallow water near a coast, it slows "
                "and becomes a far shorter, far taller wave. What has "
                "happened to its energy?",
        "options": [
            {"text": "It is the same energy as before, now repacked into "
                     "a shorter, taller wave instead of a long, low one",
             "correct": True},
            {"text": "The energy has increased hugely near the coast, "
                     "which is why the wave becomes dangerous",
             "correct": False,
             "why": "No new energy is added near the coast; the same "
                    "energy is simply reshaped."},
            {"text": "The energy has spread out even further as the wave "
                     "nears the coast, which is why it grows taller",
             "correct": False,
             "why": "Spreading the same energy over more space would make "
                    "a wave lower, not taller."},
            {"text": "It used its energy on the way, and the shallow water "
                     "tops it back up", "correct": False,
             "why": "Shallow water does not supply the wave with fresh "
                    "energy from below."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h13",
        "band": "harder",
        "text": "A deep-ocean tsunami can have a steepness (amplitude "
                "compared with wavelength) of roughly 1 in 200,000, "
                "flatter than an ordinary ripple, and yet it can be one of "
                "the most destructive waves there is. What does this show "
                "about steepness and the energy a wave carries?",
        "options": [
            {"text": 'It shows that only steep waves are dangerous, so a wave '
                     'as flat as this one cannot be a real tsunami',
             "correct": False,
             "why": "This directly contradicts the fact given — the flat, "
                    "low tsunami really is dangerous once it reaches "
                    "shallow water."},
            {"text": "It shows that a wave's steepness alone does not tell "
                     "you how much energy it carries — a very flat-"
                     "looking wave can still carry enormous energy",
             "correct": True},
            {"text": 'It shows that steepness and energy are the same '
                     'underlying quantity, measured in two different ways',
             "correct": False,
             "why": "Steepness compares two lengths on the wave; energy is "
                    "a completely different quantity from either of them."},
            {"text": 'It shows the figure must be a mistake, since a wave of '
                     'such tiny amplitude could not be a tsunami', "correct": False,
             "why": "The tiny deep-ocean amplitude is a genuine, well-"
                    "measured feature of real tsunamis, not an error."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-01-e15",
        "band": "easier",
        "text": "The up-and-down shape that a water wave's surface makes is "
                "called an…",
        "options": [
            {"text": "undulation", "correct": True},
            {"text": "current", "correct": False,
             "why": "A current is water flowing steadily in one direction, "
                    "not the repeating shape a wave's surface makes."},
            {"text": "splash", "correct": False,
             "why": "A splash is a single brief event, not the repeating "
                    "shape of a travelling wave."},
            {"text": "tide", "correct": False,
             "why": "A tide is a much slower, much larger rise and fall of "
                    "sea level, caused by a different mechanism."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e16",
        "band": "easier",
        "text": "A trough dips 0.07 m below the still level. What is the "
                "amplitude of this wave?",
        "options": [
            {"text": "0.14 m", "correct": False,
             "why": "That would be trough to crest, twice the amplitude. "
                    "Amplitude is measured from the still level to one "
                    "crest or trough, not across both."},
            {"text": "0.07 m", "correct": True},
            {"text": "0.035 m", "correct": False,
             "why": "Halving isn't needed here — 0.07 m below the still "
                    "level already is the amplitude."},
            {"text": "It cannot be found without the wavelength",
             "correct": False,
             "why": "Amplitude only needs the distance from the still "
                    "level; the wavelength plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e17",
        "band": "easier",
        "text": "The leading edge of one crest is marked, and the matching "
                "leading edge of the very next crest is marked 0.45 m "
                "further along. What is the wavelength?",
        "options": [
            {"text": "0.225 m", "correct": False,
             "why": "Halving would give the distance to only part of the "
                    "way through the wave, not to the matching point on "
                    "the next one."},
            {"text": "0.90 m", "correct": False,
             "why": "Doubling would be two whole wavelengths. Two matching "
                    "points on neighbouring crests are one wavelength "
                    "apart."},
            {"text": "0.45 m", "correct": True},
            {"text": "It cannot be told without the amplitude",
             "correct": False,
             "why": "Wavelength is a distance along the wave and does not "
                    "depend on how high the wave rises."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e18",
        "band": "easier",
        "text": "A sealed bottle floats far out at sea. Waves pass beneath "
                "it for an hour. Where does the bottle end up?",
        "options": [
            {"text": "Carried a long way in the direction the waves are "
                     "travelling", "correct": False,
             "why": "If the water travelled along like this, the whole sea "
                    "would eventually pile up on one shore."},
            {"text": "Pushed backwards, against the direction the waves "
                     "are travelling", "correct": False,
             "why": "Nothing pushes a floating object backwards; it simply "
                    "rises and falls in place as each wave passes."},
            {"text": "Pulled under the surface and held there",
             "correct": False,
             "why": "A floating bottle stays on the surface; nothing about "
                    "a passing wave pulls it under."},
            {"text": "Roughly where it started, rising and falling as each "
                     "wave passes", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e19",
        "band": "easier",
        "text": "Which word names how far the water surface rises above "
                "the still level?",
        "options": [
            {"text": "amplitude", "correct": True},
            {"text": "wavelength", "correct": False,
             "why": "Wavelength is a distance along the wave, from one "
                    "crest to the next, not a height above the still "
                    "level."},
            {"text": "transverse", "correct": False,
             "why": "Transverse describes the direction the water moves "
                    "in, not a measurement of how far it moves."},
            {"text": "disturbance", "correct": False,
             "why": "Disturbance names the travelling wave itself, not a "
                    "measurement of its size."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e20",
        "band": "easier",
        "text": "A cork floats on a water wave. As a crest passes under "
                "it, which way does the cork move?",
        "options": [
            {"text": "Sideways, in the same direction the wave travels", "correct": False,
             "why": "That is how a longitudinal wave's particles move. "
                    "Water waves are transverse, and the cork does not travel "
                    "sideways with the wave."},
            {"text": "Straight up, then straight down again", "correct": True},
            {"text": "Straight down first, then straight back up once "
                     "the crest has gone past", "correct": False,
             "why": "A crest is a raised patch of water, so it lifts "
                    "the cork first. The dip comes later, when the trough "
                    "arrives."},
            {"text": "It stays completely still", "correct": False,
             "why": "The cork does move — up and down — as each wave "
                    "passes beneath it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e21",
        "band": "easier",
        "text": "A stone is dropped into a still pond. From which point do "
                "the ripples spread outward?",
        "options": [
            {"text": "From the edges of the pond inward, towards the "
                     "splash", "correct": False,
             "why": "Ripples spread away from where the stone landed, not "
                    "inward from the edges of the pond."},
            {"text": "From directly below the splash, spreading only "
                     "downward through the water", "correct": False,
             "why": "The ripples spread across the surface in every "
                    "direction, not downward into the water."},
            {"text": "From the point where the stone hit the water, "
                     "spreading outward in all directions", "correct": True},
            {"text": "Ripples appear at random points scattered across "
                     "the whole pond at exactly the same moment, with no "
                     "clear starting point at all", "correct": False,
             "why": "The ripples begin at one place — the splash — and "
                    "spread out from there; they do not appear randomly."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e22",
        "band": "easier",
        "text": "Which measurement is a distance ALONG the wave, rather "
                "than a height above it?",
        "options": [
            {"text": "amplitude", "correct": False,
             "why": "Amplitude is a height, measured up from the still "
                    "level, not a distance along the wave."},
            {"text": "transverse", "correct": False,
             "why": "Transverse describes a direction of motion, not a "
                    "measurement of length."},
            {"text": "still level", "correct": False,
             "why": "The still level is a reference height, not a "
                    "distance along the wave."},
            {"text": "wavelength", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e23",
        "band": "easier",
        "text": "Which position is used as the fixed reference for "
                "measuring a wave's amplitude?",
        "options": [
            {"text": "the still level, where the water sits when nothing "
                     "is disturbing it", "correct": True},
            {"text": "the deepest part of the trough", "correct": False,
             "why": "The trough is where the water reaches its lowest — "
                    "it is what gets measured, not the reference point "
                    "measured from."},
            {"text": "the exact centre of the ripple tank", "correct": False,
             "why": "Where the tank is measured has nothing to do with "
                    "how amplitude is defined."},
            {"text": "the top of the highest crest ever recorded",
             "correct": False,
             "why": "Amplitude is measured from the still level for every "
                    "wave, not from some record height."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e24",
        "band": "easier",
        "text": "A wave's shape is fully described using two independent "
                "measurements. Which pair are they?",
        "options": [
            {"text": "crest and trough", "correct": False,
             "why": "Crest and trough are points on the wave, not "
                    "measurements of its size."},
            {"text": "amplitude and wavelength", "correct": True},
            {"text": "still level and crest", "correct": False,
             "why": "The still level is where measuring starts from, not "
                    "a measurement of the wave's shape."},
            {"text": "trough and still level", "correct": False,
             "why": "Neither of those is a measurement — they are places "
                    "on or near the wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e25",
        "band": "easier",
        "text": "A wave that is unusually tall for how closely packed its "
                "crests are is described as…",
        "options": [
            {"text": "shallow", "correct": False,
             "why": "Shallow describes how deep the water is, not the "
                    "shape of the wave itself."},
            {"text": "long", "correct": False,
             "why": "A long wave is one with a large wavelength; "
                    "steepness compares the height to the wavelength "
                    "together."},
            {"text": "steep", "correct": True},
            {"text": "loud", "correct": False,
             "why": "Loudness describes sound, a completely different "
                    "kind of wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e26",
        "band": "easier",
        "text": "If a water wave's surface moved back and forth ALONG the "
                "same direction the wave travels, rather than up and "
                "down, what type of wave would that be instead?",
        "options": [
            {"text": "transverse", "correct": False,
             "why": "Transverse is what a water wave already is — the "
                    "surface moves at right angles to the direction of "
                    "travel, not along it."},
            {"text": "reflected", "correct": False,
             "why": "Reflected describes a wave bouncing back off a "
                    "barrier, not the direction the water moves in."},
            {"text": "refracted", "correct": False,
             "why": "Refracted describes a wave changing direction "
                    "between materials, not the direction the water "
                    "moves in."},
            {"text": "longitudinal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e27",
        "band": "easier",
        "text": "The wavelength of a wave is the distance from one crest "
                "to the next. What is the distance from a crest to the "
                "trough immediately following it?",
        "options": [
            {"text": "half a wavelength", "correct": True},
            {"text": "a whole wavelength", "correct": False,
             "why": "A whole wavelength is crest to the next crest, which "
                    "is a longer distance than crest to the very next "
                    "trough."},
            {"text": "twice the wavelength", "correct": False,
             "why": "The distance to the very next trough is shorter than "
                    "one wavelength, not longer."},
            {"text": "the same as the amplitude", "correct": False,
             "why": "Amplitude is a height above the still level; this "
                    "distance runs along the wave instead."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e28",
        "band": "easier",
        "text": "A crest is measured 0.20 m above the still level. If the "
                "wave's amplitude were doubled, how high above the still "
                "level would the new crest be?",
        "options": [
            {"text": "0.20 m", "correct": False,
             "why": "That leaves the height unchanged. Doubling the "
                    "amplitude has to change the crest height."},
            {"text": "0.40 m", "correct": True},
            {"text": "0.10 m", "correct": False,
             "why": "That halves the height instead of doubling it."},
            {"text": "It cannot be told without the wavelength",
             "correct": False,
             "why": "Amplitude and crest height do not depend on the "
                    "wavelength at all."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e29",
        "band": "easier",
        "text": "A wave's crests are measured 1.4 m apart. How far "
                "apart are its troughs?",
        "options": [
            {"text": "0.7 m", "correct": False,
             "why": "0.4 m is the crest-to-trough distance, half a "
                    "wave. Trough to trough is a whole wave, the same as crest "
                    "to crest."},
            {"text": "2.8 m", "correct": False,
             "why": "Doubling would be two whole waves. One trough to "
                    "the next is one wave, the same distance as one crest to "
                    "the next."},
            {"text": "1.4 m", "correct": True},
            {"text": "It cannot be told without the amplitude", "correct": False,
             "why": "How far apart the troughs sit is a distance along "
                    "the wave; how far the water rises plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-e30",
        "band": "easier",
        "text": "A student says amplitude and wavelength are just two "
                "different names for the same measurement. Which observation "
                "shows this is wrong?",
        "options": [
            {"text": "Both are measured in metres", "correct": False,
             "why": "Sharing a unit does not show two measurements are "
                    "different — it only shows they are both lengths."},
            {"text": "There is no practical way to test in a ripple "
                     "tank whether they are really the same single measurement "
                     "or not", "correct": False,
             "why": "A ripple tank does exactly that: it has one "
                    "control for each, and they can be moved separately."},
            {"text": "Both increase together whenever either one is "
                     "changed, since the paddle that sets one of them sets the "
                     "other at the same time", "correct": False,
             "why": "A ripple tank's two controls work independently — "
                    "changing one leaves the other's reading exactly where it "
                    "was."},
            {"text": "You can change how far the water rises without "
                     "changing how far apart the crests are", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-01-s14",
        "band": "standard",
        "text": "A ripple tank 2.0 m across shows exactly 4 complete "
                "waves laid evenly along it. What is the wavelength?",
        "options": [
            {"text": "8.0 m", "correct": False,
             "why": "That multiplies the two numbers together. Dividing "
                    "the length by the number of waves gives the wavelength."},
            {"text": "0.25 m", "correct": False,
             "why": "That divides the length by 8, not by the 4 "
                    "complete waves that were counted."},
            {"text": "It cannot be found without the amplitude", "correct": False,
             "why": "Wavelength comes from the length and the number of "
                    "waves alone; amplitude plays no part in it."},
            {"text": "0.5 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s15",
        "band": "standard",
        "text": "Wave A has wavelength 0.4 m and amplitude 0.03 m. Wave "
                "B has wavelength 0.8 m and amplitude 0.06 m. Which wave rises "
                "higher above the still level, and by how much?",
        "options": [
            {"text": "Wave B, by 0.03 m", "correct": True},
            {"text": "Wave A, by 0.03 m", "correct": False,
             "why": "0.06 m is larger than 0.03 m, so Wave B is the one "
                    "that rises higher, not Wave A."},
            {"text": "Wave B, by 0.4 m", "correct": False,
             "why": "That uses Wave A's wavelength instead of comparing "
                    "the two amplitudes."},
            {"text": "Neither — both rise the same height, since their "
                     "wavelengths are in the same ratio as their amplitudes", "correct": False,
             "why": "The ratio of the wavelengths is not what decides "
                    "height above still level; only the amplitude values "
                    "themselves do, and they differ."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s16",
        "band": "standard",
        "text": "A wave has amplitude 0.10 m and wavelength 2.0 m. A "
                "second wave in the same tank has amplitude 0.10 m and "
                "wavelength 0.50 m. Which wave looks steeper, and why?",
        "options": [
            {"text": "The first, because its wavelength is the larger "
                     "number", "correct": False,
             "why": "A larger wavelength spreads the same rise over a "
                    "longer distance, which makes a wave LESS steep, not more."},
            {"text": "The second, because the same rise happens over a "
                     "shorter distance along the water", "correct": True},
            {"text": "They are equally steep, because the amplitudes "
                     "are equal, and steepness is decided by the amplitude alone", "correct": False,
             "why": "Steepness compares the rise to the spacing between "
                    "crests, and the spacing is different for these two waves."},
            {"text": "Steepness cannot be compared at all without first "
                     "measuring the exact depth of the water inside the tank "
                     "itself", "correct": False,
             "why": "Steepness only needs the amplitude and the "
                    "wavelength; the depth of the tank plays no part in it "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s17",
        "band": "standard",
        "text": "A canal boat rocks gently as a small wash from a "
                "passing barge reaches it, then rocks much harder when a "
                "second, taller wash arrives shortly after. Both washes have "
                "about the same wavelength. Which wash carried more energy?",
        "options": [
            {"text": "The first, gentler wash, since it arrived first "
                     "and used up the water's energy", "correct": False,
             "why": "Water has no fixed store of energy that gets used "
                    "up in this way. Each wash carries its own energy, set by "
                    "its own amplitude."},
            {"text": "Neither — both washes carry the same energy, "
                     "since they share the same wavelength", "correct": False,
             "why": "Energy relates to amplitude, not to wavelength, "
                    "and the two washes have different amplitudes."},
            {"text": "The taller wash, since a bigger amplitude always "
                     "means more energy", "correct": True},
            {"text": "It cannot be judged without knowing how far the "
                     "barge was from the boat", "correct": False,
             "why": "Distance to the barge is not needed here — the "
                    "amplitudes described are already enough to compare the "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s18",
        "band": "standard",
        "text": "A duck floats 3 m from a point where a ripple is "
                "created, and a second identical duck floats 3 m from that same "
                "point in the opposite direction. The ripple spreads out evenly "
                "in all directions. Which duck starts bobbing first?",
        "options": [
            {"text": "The duck on the side the ripple happens to be "
                     "travelling towards first", "correct": False,
             "why": "The ripple spreads outward evenly in every "
                    "direction at once, not favouring one side over the other."},
            {"text": "Whichever duck is heavier, since a heavier duck "
                     "responds to a disturbance sooner", "correct": False,
             "why": "How heavy a duck is does not change when the "
                    "disturbance reaches it — that depends only on distance "
                    "from the splash."},
            {"text": "Neither duck ever starts bobbing, since they are "
                     "on opposite sides of the splash", "correct": False,
             "why": "The ripple reaches every direction from the "
                    "splash, so both ducks are reached and both start bobbing."},
            {"text": "Both start at the same moment, since they are "
                     "equally far from where the ripple began", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s19",
        "band": "standard",
        "text": "A wave train crosses a 0.90 m stretch of channel and "
                "exactly 3 complete waves fit into it. The paddle is then "
                "adjusted so exactly 6 complete waves fit into the very same "
                "0.90 m stretch. What is the new wavelength?",
        "options": [
            {"text": "0.15 m", "correct": True},
            {"text": "0.30 m", "correct": False,
             "why": "That is the ORIGINAL wavelength, from 0.90 m "
                    "divided by 3. The question asks for the new one, with 6 "
                    "waves fitted in."},
            {"text": "0.45 m", "correct": False,
             "why": "That is half of 0.90 m, not 0.90 m divided by the "
                    "new count of 6."},
            {"text": "0.60 m", "correct": False,
             "why": "That doubles the original 0.30 m instead of "
                    "dividing again. 0.90 m divided by the new count of 6 "
                    "gives the new wavelength."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s20",
        "band": "standard",
        "text": "A wave has amplitude 0.08 m. A student says doubling "
                "the wavelength will also double the amplitude. Using the "
                "ripple tank's two separate controls, explain why the student "
                "is wrong.",
        "options": [
            {"text": "The student is right, because both readings on a "
                     "ripple tank always rise and fall together automatically as "
                     "soon as the paddle is adjusted at all", "correct": False,
             "why": "A ripple tank shows the opposite: the two controls "
                    "can be moved one at a time, without the other reading "
                    "changing."},
            {"text": "A ripple tank has one control for amplitude and a "
                     "separate control for wavelength; changing one leaves the "
                     "other's reading unchanged", "correct": True},
            {"text": "The student is right, but only for amplitudes "
                     "smaller than about 0.08 m", "correct": False,
             "why": "There is no such size limit — the two controls are "
                    "independent of each other whatever the amplitude happens "
                    "to be."},
            {"text": "Amplitude cannot be doubled at all once a wave "
                     "has been created", "correct": False,
             "why": "Amplitude can be changed at any time by moving the "
                    "depth control; nothing fixes it once a wave starts."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s21",
        "band": "standard",
        "text": "Two ripple tanks are set up identically except tank "
                "B's paddle dips twice as deep as tank A's. Both paddles lay "
                "their crests the same distance apart. Which tank shows the "
                "larger amplitude, and which shows the longer wavelength?",
        "options": [
            {"text": "Tank B has the larger amplitude AND the longer "
                     "wavelength", "correct": False,
             "why": "The crests are stated to be laid the same distance "
                    "apart in both tanks, so the wavelengths match."},
            {"text": "Tank A has the larger amplitude, since it is "
                     "mentioned first", "correct": False,
             "why": "The order the tanks are described in has nothing "
                    "to do with which one has the deeper-dipping paddle."},
            {"text": "Tank B has the larger amplitude; both tanks have "
                     "the same wavelength", "correct": True},
            {"text": "Both tanks have the same amplitude, since only "
                     "the spacing of the crests was said to be equal", "correct": False,
             "why": "Tank B's paddle dips twice as deep, so its "
                    "amplitude is larger, not equal to tank A's."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s22",
        "band": "standard",
        "text": "A weather buoy's readout shows a wave's amplitude "
                "increasing from 0.10 m to 0.15 m while its wavelength stays "
                "fixed at 40 m. What has changed about this sea state, and what "
                "has not?",
        "options": [
            {"text": "The waves are getting longer for the same height", "correct": False,
             "why": "That swaps the two readings around — it is the "
                    "amplitude, not the wavelength, that the readout shows "
                    "changing."},
            {"text": "Both properties have increased together", "correct": False,
             "why": "The wavelength is stated to stay fixed at 40 m — "
                    "only the amplitude reading has changed."},
            {"text": "Nothing meaningful has changed, since 0.10 m and "
                     "0.15 m are both small numbers", "correct": False,
             "why": "A 50% rise in amplitude is a real change in how "
                    "tall the waves are, whatever the absolute size of the "
                    "numbers."},
            {"text": "The waves are getting taller for the same "
                     "spacing; how far apart the crests are has not changed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s23",
        "band": "standard",
        "text": "A wave train has amplitude 0.06 m and wavelength 1.2 m. A "
                "second wave train in the same tank has amplitude 0.12 m "
                "and the same wavelength. Which statement correctly "
                "compares their energy?",
        "options": [
            {"text": "The second carries more energy, since it has the "
                     "larger amplitude", "correct": True},
            {"text": "The first carries more energy, since smaller "
                     "amplitudes move less water and so waste less "
                     "energy", "correct": False,
             "why": "A smaller amplitude means less energy is being "
                    "carried, not more — nothing about the wave is "
                    "\"wasted\"."},
            {"text": "They carry the same energy, since they share the "
                     "same wavelength", "correct": False,
             "why": "Energy relates to amplitude in this lesson, not to "
                    "wavelength, and the two amplitudes are different."},
            {"text": "It cannot be judged without knowing the depth of "
                     "the tank", "correct": False,
             "why": "The two amplitudes already give enough information "
                    "to compare the energy the waves carry."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s24",
        "band": "standard",
        "text": "A floating marker sits exactly half a wavelength along "
                "the wave from a crest. What is the water doing directly "
                "beneath the marker at that same instant?",
        "options": [
            {"text": "another crest", "correct": False,
             "why": "A point one whole wavelength away would show "
                    "another crest; half a wavelength away shows something "
                    "else."},
            {"text": "a trough", "correct": True},
            {"text": "the still level, rising", "correct": False,
             "why": "A point a QUARTER of a wavelength away sits at the "
                    "still level; half a wavelength away is a full trough."},
            {"text": "the still level, falling", "correct": False,
             "why": "Half a wavelength from a crest is a trough, not a "
                    "point crossing the still level."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s25",
        "band": "standard",
        "text": "A ripple tank shows waves with amplitude 0.03 m and "
                "wavelength 0.6 m, at a steepness that looks moderate. "
                "The paddle is then changed so the amplitude stays 0.03 m "
                "but the wavelength becomes 0.2 m. What happens to the "
                "steepness?",
        "options": [
            {"text": "It decreases", "correct": False,
             "why": "The rise is unchanged and the crests are now closer "
                    "together, which makes the wave MORE steep, not "
                    "less."},
            {"text": "It stays exactly the same", "correct": False,
             "why": "Steepness compares the amplitude to the wavelength, "
                    "and the wavelength has changed even though the "
                    "amplitude has not."},
            {"text": "It increases", "correct": True},
            {"text": "Steepness cannot change unless the amplitude "
                     "changes too", "correct": False,
             "why": "Steepness depends on both measurements together, so "
                    "changing the wavelength alone is enough to change "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s26",
        "band": "standard",
        "text": "A harbour wave gauge records amplitude 0.4 m and "
                "wavelength 3 m in the morning. By afternoon it records "
                "amplitude 0.2 m and wavelength 3 m. What has most likely "
                "happened to the wave's energy?",
        "options": [
            {"text": "It has increased", "correct": False,
             "why": "The amplitude has fallen from 0.4 m to 0.2 m, and "
                    "energy relates to amplitude — a fall in amplitude points "
                    "to less energy, not more."},
            {"text": "It has stayed the same, since the wavelength is "
                     "unchanged", "correct": False,
             "why": "Energy relates to amplitude, and the amplitude has "
                    "clearly changed between morning and afternoon."},
            {"text": "It cannot be said at all without first knowing "
                     "the exact depth of the water inside the harbour itself", "correct": False,
             "why": "The two amplitude readings already give enough to "
                    "judge the change; harbour depth is not needed here."},
            {"text": "It has decreased, since amplitude has fallen "
                     "while wavelength is unchanged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s27",
        "band": "standard",
        "text": "A wave train in a long channel has a wavelength of 0.5 "
                "m. A marker is placed at the position of one crest. Exactly "
                "3.5 wavelengths further along the channel, is the water at a "
                "crest, a trough, or somewhere else?",
        "options": [
            {"text": "At a trough", "correct": True},
            {"text": "At another crest", "correct": False,
             "why": "A whole number of wavelengths further along would "
                    "land on another crest; 3.5 is not a whole number."},
            {"text": "Exactly at the still level, rising", "correct": False,
             "why": "A quarter-wavelength offset lands at the still "
                    "level; a half-wavelength offset — like the 0.5 left over "
                    "here — lands at a trough."},
            {"text": "It cannot be told without the amplitude", "correct": False,
             "why": "Where you land along a wave depends only on how "
                    "many wavelengths you have moved, not on the amplitude."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s28",
        "band": "standard",
        "text": "A student adjusts a ripple tank so the wavelength "
                "doubles while the amplitude is halved. Compared with the "
                "original wave, is the new wave steeper, less steep, or the "
                "same steepness?",
        "options": [
            {"text": "Steeper, because doubling a measurement always "
                     "makes a wave more dramatic", "correct": False,
             "why": "Doubling the wavelength spreads the same rise over "
                    "more distance, which makes a wave LESS steep, not more."},
            {"text": "Less steep, because the height has fallen while "
                     "the crests have spread further apart, and that combination "
                     "always reduces steepness", "correct": True},
            {"text": "The same steepness, since one measurement went up "
                     "and the other went down by the same factor", "correct": False,
             "why": "Steepness is amplitude compared with wavelength; "
                    "halving one and doubling the other both push steepness "
                    "the same way, down, not to a standstill."},
            {"text": "It cannot be judged without knowing the depth of "
                     "the tank", "correct": False,
             "why": "Steepness only needs the amplitude and wavelength "
                    "values given; tank depth plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s29",
        "band": "standard",
        "text": "Two floating leaves sit on the same pond in the path "
                "of ripples spreading from a single splash. The near leaf "
                "starts bobbing at a certain moment. How long after that does a "
                "leaf 2.0 m away start bobbing, compared with a leaf only 1.0 m "
                "away?",
        "options": [
            {"text": "The same amount of time, because the ripple "
                     "reaches every leaf at once, whatever the distance", "correct": False,
             "why": "The disturbance has to travel across the pond, so "
                    "a further leaf is reached later, not at the same moment."},
            {"text": "Shorter, because ripples travel faster the "
                     "further they have already gone", "correct": False,
             "why": "Nothing about this wave speeds up as it travels; a "
                    "greater distance simply takes more time to cross."},
            {"text": "Longer, because the disturbance takes more time "
                     "to cross the extra distance", "correct": True},
            {"text": "It cannot be compared without knowing the "
                     "amplitude of the ripples", "correct": False,
             "why": "How long the disturbance takes to arrive depends "
                    "on distance, not on how tall the ripples are."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-s30",
        "band": "standard",
        "text": "A wave gauge reports a wavelength of 0.9 m. Over a 4.5 "
                "m stretch of water, how many COMPLETE wavelengths fit?",
        "options": [
            {"text": "4", "correct": False,
             "why": "4.5 divided by 0.9 works out exactly to 5, not 4."},
            {"text": "6", "correct": False,
             "why": "6 wavelengths of 0.9 m would need 5.4 m, more than "
                    "the 4.5 m stretch given."},
            {"text": "It cannot be found without the amplitude", "correct": False,
             "why": "Fitting wavelengths into a length only needs the "
                    "wavelength and the length; amplitude is not needed."},
            {"text": "5", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-01-h14",
        "band": "harder",
        "text": "A photograph of a ripple tank shows 6 evenly spaced "
                "crests along a 1.5 m stretch of water, with one crest at each "
                "end of the stretch. What is the wavelength?",
        "options": [
            {"text": "0.25 m", "correct": False,
             "why": "That divides 1.5 m by all 6 crests. Six crests "
                    "with one at each end mark out only 5 gaps between them."},
            {"text": "0.375 m", "correct": False,
             "why": "That divides 1.5 m by 4, which is neither the "
                    "number of crests nor the number of gaps between them."},
            {"text": "It cannot be found without the amplitude", "correct": False,
             "why": "Wavelength comes from the length and the number of "
                    "gaps between crests; amplitude plays no part in it."},
            {"text": "0.3 m", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h15",
        "band": "harder",
        "text": "Two wave trains cross the same 1.0 m stretch of tank. "
                "Train A shows 4 wavelengths fitting exactly into it; Train B "
                "shows 5. A student says Train B must have the larger "
                "amplitude, since its wave count is higher. Assess this claim.",
        "options": [
            {"text": "The claim is wrong: wave count in a fixed "
                     "distance tells you about wavelength, not amplitude, which "
                     "is a separate, independent measurement", "correct": True},
            {"text": "The claim is right, because more wavelengths "
                     "fitting in the same space always means a taller wave", "correct": False,
             "why": "Fitting more wavelengths into the same space means "
                    "a shorter wavelength, and says nothing about the "
                    "amplitude, which is a separate measurement."},
            {"text": "The claim is only right if both trains started at "
                     "the same moment", "correct": False,
             "why": "When each train started makes no difference to "
                    "whether wave count says anything about amplitude — it "
                    "does not, whatever the timing."},
            {"text": "The claim is right, because a wave that gets "
                     "squeezed into a much shorter wavelength must always rise "
                     "higher in order to make room for the extra waves packed in", "correct": False,
             "why": "Amplitude is set by the paddle's own depth "
                    "control, not by how many waves happen to fit in a stretch "
                    "of tank."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h16",
        "band": "harder",
        "text": "A wave's steepness is its amplitude divided by its "
                "wavelength. A wave has steepness 1 in 20 and wavelength "
                "4.0 m. What is its amplitude?",
        "options": [
            {"text": "5.0 m", "correct": False,
             "why": "That divides 20 by 4.0 rather than dividing 4.0 by "
                    "20 — the steepness ratio is amplitude over "
                    "wavelength, not the other way round."},
            {"text": "0.20 m", "correct": True},
            {"text": "80 m", "correct": False,
             "why": "That multiplies the two numbers together instead of "
                    "dividing the wavelength by 20."},
            {"text": "0.008 m", "correct": False,
             "why": "That divides 4.0 by 500, not by the 20 the "
                    "steepness ratio actually gives."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h17",
        "band": "harder",
        "text": "A deep-water wave has steepness close to the breaking "
                "limit of about 1 in 7. Its wavelength is 3.5 m. Roughly what "
                "amplitude would put it at this limit?",
        "options": [
            {"text": "2.0 m", "correct": False,
             "why": "That divides 7 by 3.5, the wrong way round — "
                    "steepness is amplitude over wavelength."},
            {"text": "24.5 m", "correct": False,
             "why": "That multiplies 3.5 by 7 instead of dividing it."},
            {"text": "0.5 m", "correct": True},
            {"text": "0.05 m", "correct": False,
             "why": "That is ten times too small — 3.5 m divided by 7 "
                    "gives 0.5 m, not 0.05 m."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h18",
        "band": "harder",
        "text": "A student claims: 'a wave with twice the amplitude of "
                "another must always look twice as steep.' Wave X has amplitude "
                "0.10 m and wavelength 2.0 m; Wave Y has amplitude 0.20 m and "
                "wavelength 8.0 m. Assess the claim.",
        "options": [
            {"text": "The claim is right, since Y's amplitude really is "
                     "twice X's", "correct": False,
             "why": "Steepness compares amplitude with wavelength "
                    "together, not amplitude on its own — Y's much longer "
                    "wavelength has not been accounted for."},
            {"text": "The claim is right, because steepness only "
                     "depends on amplitude, and Y's is larger", "correct": False,
             "why": "Steepness is amplitude divided by wavelength, not "
                    "amplitude alone — wavelength matters just as much."},
            {"text": "Steepness cannot be found without knowing the "
                     "depth of the water in each case", "correct": False,
             "why": "Steepness only needs the amplitude and the "
                    "wavelength, both of which are already given here."},
            {"text": "The claim is wrong: amplitude ÷ wavelength gives "
                     "0.05 for X and 0.025 for Y, so Y is actually LESS steep "
                     "despite the larger amplitude", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h19",
        "band": "harder",
        "text": "A wave train shows 12 complete wavelengths spread "
                "evenly across a 3.6 m stretch of tank. The paddle is adjusted "
                "so only 6 wavelengths now fit in the same 3.6 m stretch, with "
                "the amplitude unchanged throughout. A student says the wave "
                "now carries less energy because it has 'lost half its waves.' "
                "Having found the new wavelength, assess this claim.",
        "options": [
            {"text": "The claim is wrong: the wavelength has doubled, "
                     "but the amplitude — which is what is linked to energy — "
                     "has not changed, so there's no reason to think the energy "
                     "has fallen", "correct": True},
            {"text": "The claim is right, since fewer waves obviously "
                     "means less energy overall", "correct": False,
             "why": "The wavelength has changed from 0.3 m to 0.6 m, "
                    "but wavelength is not what this lesson links to energy — "
                    "amplitude is."},
            {"text": "It cannot be judged, because wavelength and "
                     "energy are always linked to each other", "correct": False,
             "why": "This lesson links energy to amplitude, not to "
                    "wavelength; the wavelength changing here says nothing "
                    "about the energy."},
            {"text": "The claim is right, but only because 6 happens to "
                     "divide evenly into 12, and the fit of the waves across the "
                     "whole stretch of tank would otherwise have come out "
                     "looking noticeably more awkward and far less even than it "
                     "actually does here", "correct": False,
             "why": "How evenly the wave count divides has no bearing "
                    "on energy at all — only the amplitude does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h20",
        "band": "harder",
        "text": "A student says: 'the biggest possible ripple tank wave "
                "is one with the largest amplitude AND the largest "
                "wavelength at the same time.' Using the independence of "
                "amplitude and wavelength, evaluate this statement.",
        "options": [
            {"text": "The statement is correct — the biggest wave is "
                     "always the one single combination of both "
                     "measurements set together to their own absolute "
                     "maximum, reached at exactly the same moment on "
                     "the very same wave", "correct": False,
             "why": "Because the two are independent, there is no single "
                    "combination that counts as the one 'biggest' wave — "
                    "the two controls can be set to any combination."},
            {"text": "The statement conflates two separate properties: a "
                     "wave can have a large amplitude with a short "
                     "wavelength, a long wavelength with a small "
                     "amplitude, or many other combinations, since the "
                     "two are never linked to each other",
             "correct": True},
            {"text": "The statement is correct only for tsunamis, which "
                     "are the one kind of wave where both measurements "
                     "are forced to be large together", "correct": False,
             "why": "A tsunami actually has a very SMALL amplitude "
                    "alongside its huge wavelength out at sea, which is "
                    "the opposite of both being large together."},
            {"text": "Neither measurement can ever reach its largest "
                     "value in a real ripple tank, so the question does "
                     "not apply", "correct": False,
             "why": "The tank's sliders genuinely do reach their maximum "
                    "settings; the flaw in the student's claim is about "
                    "combining the two, not about either one being "
                    "unreachable."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h21",
        "band": "harder",
        "text": "A wave's steepness is amplitude ÷ wavelength. A wave "
                "with steepness 1 in 25 has an amplitude of 0.08 m. What is its "
                "wavelength?",
        "options": [
            {"text": "0.0032 m", "correct": False,
             "why": "That divides 0.08 by 25 the wrong way round — "
                    "wavelength is found by multiplying the amplitude by 25, "
                    "not dividing by it."},
            {"text": "312.5 m", "correct": False,
             "why": "That divides 25 by 0.08, the wrong way round for "
                    "this steepness ratio."},
            {"text": "2.0 m", "correct": True},
            {"text": "25.08 m", "correct": False,
             "why": "That adds 0.08 and 25 together rather than "
                    "multiplying them."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h22",
        "band": "harder",
        "text": "A researcher records a wave's amplitude as 0.12 m "
                "using a ruler held at a crest, and 0.09 m using a ruler held "
                "at a trough of the very same wave a moment later. Explain why "
                "these two values might not agree, even though amplitude should "
                "be a single fixed number for a given wave.",
        "options": [
            {"text": "Amplitude genuinely is a different number at a "
                     "crest than at a trough of the same wave", "correct": False,
             "why": "In the regular wave this lesson studies, the rise "
                    "to a crest and the dip to a trough should match — a "
                    "difference points to something else."},
            {"text": "The wave must have sped up between the two "
                     "readings, and a faster wave always reads taller at a crest", "correct": False,
             "why": "How fast a wave travels is a separate matter from "
                    "how far it rises; speeding up would not by itself make "
                    "the crest reading the larger of the two."},
            {"text": "Amplitude cannot be measured at a trough at all, "
                     "on any wave whatsoever, only ever at a crest, no matter "
                     "which instrument or which ruler is used to carry out the "
                     "measuring", "correct": False,
             "why": "This lesson measures amplitude from the still "
                    "level to a trough just as validly as to a crest."},
            {"text": "In a perfectly regular wave the two should match; "
                     "a difference like this most likely comes from measurement "
                     "error, or the wave's shape changing slightly as it travels", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h23",
        "band": "harder",
        "text": "Wave X crosses a 1.0 m stretch of tank showing 5 "
                "evenly spaced crests, with one crest at each end. Wave Y "
                "crosses a 2.0 m stretch showing 6 evenly spaced crests, also "
                "with one at each end. Which wave has the shorter wavelength?",
        "options": [
            {"text": "Wave X: its wavelength works out at 0.25 m, "
                     "against Wave Y's 0.40 m", "correct": True},
            {"text": "Wave Y, since more crests must mean a shorter "
                     "wavelength", "correct": False,
             "why": "Wave Y's crests are spread over a much longer "
                    "stretch of tank, so its wavelength is actually longer, "
                    "not shorter."},
            {"text": "They must be equal, since both have a crest at "
                     "each end of their stretch", "correct": False,
             "why": "Having a crest at each end fixes the pattern, but "
                    "the two stretches and crest counts are different, which "
                    "gives different wavelengths."},
            {"text": "It cannot be judged without knowing the amplitude "
                     "of each wave", "correct": False,
             "why": "Wavelength comes entirely from the length and the "
                    "number of gaps between crests; amplitude is not needed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h24",
        "band": "harder",
        "text": "A wave's amplitude is measured as one quarter of its "
                "wavelength. The wavelength is 0.8 m. Is this wave close to the "
                "breaking steepness of roughly 1 in 7, or well short of it?",
        "options": [
            {"text": "Well short of it, since one quarter is a small "
                     "fraction, and a wave only approaches breaking once its "
                     "amplitude exceeds its whole wavelength", "correct": False,
             "why": "One quarter (1 in 4) is actually a much STEEPER "
                    "ratio than 1 in 7, not a smaller one."},
            {"text": "Far past it — a steepness of 1 in 4 is steeper "
                     "than the roughly 1 in 7 limit, so a real wave this steep "
                     "would already be breaking", "correct": True},
            {"text": "Exactly at the limit, since both are simple "
                     "fractions", "correct": False,
             "why": "1 in 4 and 1 in 7 are different fractions, and 1 "
                    "in 4 describes a much steeper wave than 1 in 7."},
            {"text": "It cannot be compared at all without first "
                     "knowing the exact depth setting of the paddle that was "
                     "originally used to make this particular wave in the tank", "correct": False,
             "why": "The amplitude-to-wavelength ratio alone is enough "
                    "to compare against the breaking limit; the paddle depth "
                    "is not needed separately."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h25",
        "band": "harder",
        "text": "A student says: 'because energy relates to amplitude "
                "and not wavelength, wavelength must be a completely useless "
                "measurement.' Using what wavelength actually tells you, assess "
                "this claim.",
        "options": [
            {"text": "The claim is right — since wavelength has nothing "
                     "to do with energy, it has nothing useful to say at all", "correct": False,
             "why": "Wavelength still tells you something real: how "
                    "closely packed the crests are, which matters for counting "
                    "waves or spacing measurements."},
            {"text": "The claim is right, but only until wavelength is "
                     "also linked to energy in a later stage of school", "correct": False,
             "why": "Whether energy gets linked to wavelength later "
                    "does not change what wavelength tells you now — it "
                    "already describes crest spacing."},
            {"text": "The claim is wrong: wavelength is not about "
                     "energy — it only tells you something else useful, how "
                     "closely packed the crests are", "correct": True},
            {"text": "Wavelength is only genuinely useful once you also "
                     "already know the exact energy carried by the wave in every "
                     "single part of the tank it happens to be crossing at that "
                     "moment", "correct": False,
             "why": "Wavelength describes crest spacing on its own; it "
                    "needs no energy value to be a useful measurement."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h26",
        "band": "harder",
        "text": "Wave X has amplitude 0.05 m and wavelength 1.0 m. Wave "
                "Y has amplitude 0.05 m and wavelength 4.0 m. A student claims "
                "the two carry the same energy because they share the same "
                "amplitude, and that Y's extra wavelength 'doesn't matter for "
                "energy, only for spacing.' Assess this claim.",
        "options": [
            {"text": "The claim is wrong, because a longer wavelength "
                     "on its own always carries noticeably less energy than a "
                     "shorter one, whatever the amplitude happens to be set to "
                     "on either wave being compared", "correct": False,
             "why": "This lesson links energy to amplitude, not to "
                    "wavelength — a longer wavelength on its own says nothing "
                    "about energy."},
            {"text": "The claim is wrong, because energy depends on "
                     "both measurements equally", "correct": False,
             "why": "Only amplitude has been linked to energy in this "
                    "lesson; wavelength is treated as a separate, independent "
                    "measurement."},
            {"text": "The claim cannot be judged without knowing which "
                     "wave arrived at the tank's end first, since the wave that "
                     "arrives first always gives up the larger share of its "
                     "energy", "correct": False,
             "why": "Which wave arrives first has no bearing on how "
                    "much energy either one carries."},
            {"text": "The claim is right: amplitude is what is linked "
                     "to a wave's energy, and wavelength genuinely does describe "
                     "only the spacing between crests", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h27",
        "band": "harder",
        "text": "A harbour engineer notes storm waves with amplitude "
                "1.5 m and wavelength 60 m, against ordinary waves with "
                "amplitude 0.3 m and wavelength 15 m, then says the storm waves "
                "are 'about 20 times more dangerous' by multiplying the "
                "amplitude ratio by the wavelength ratio. What is the flaw in "
                "reasoning this way?",
        "options": [
            {"text": "There is no rule that multiplies amplitude and "
                     "wavelength ratios together into an overall energy or "
                     "danger figure — only amplitude, on its own, has been "
                     "linked to how much energy a wave carries", "correct": True},
            {"text": "The engineer is right to multiply the two ratios "
                     "together like this, since both properties ought to always "
                     "count equally toward how dangerous any wave turns out to "
                     "be for a boat or a harbour wall", "correct": False,
             "why": "This lesson only links amplitude to how much "
                    "energy a wave carries — it gives no rule for combining "
                    "wavelength into a single overall figure."},
            {"text": "The flaw is that wavelength should have been "
                     "divided into the amplitude ratio instead of multiplied", "correct": False,
             "why": "Changing the arithmetic still assumes a combined "
                    "figure exists at all, which is exactly the unsupported "
                    "step — no such formula has been taught."},
            {"text": "There is no flaw — engineers always combine "
                     "amplitude and wavelength this way to judge how dangerous a "
                     "wave is", "correct": False,
             "why": "Nothing in this lesson supports combining the two "
                    "ratios into one number; only amplitude is linked to "
                    "energy here."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h28",
        "band": "harder",
        "text": "A model of a wave shows amplitude and wavelength as "
                "two separate sliders that can be moved independently, just "
                "like a ripple tank's own controls. A student says such a model "
                "must be 'unrealistic, because real ocean waves cannot have "
                "their height and spacing changed separately in nature.' Assess "
                "this claim, using real waves as evidence.",
        "options": [
            {"text": "The claim is right, because tank models are "
                     "always far too simple to reflect anything real, whatever "
                     "real-world example anyone might choose to compare them "
                     "against afterwards", "correct": False,
             "why": "The independence shown on a ripple tank matches "
                    "real waves too, such as a tsunami's tiny amplitude "
                    "alongside its huge wavelength."},
            {"text": "The claim is wrong: a calm garden ripple, an "
                     "ordinary sea wave, and an enormous long tsunami all have "
                     "their own separate combinations of amplitude and "
                     "wavelength", "correct": True},
            {"text": "The claim is right, because only artificial waves "
                     "made by a paddle can have amplitude and wavelength changed "
                     "separately", "correct": False,
             "why": "The tsunami and ordinary sea-wave examples are "
                    "natural waves, and they show the same independence as the "
                    "tank."},
            {"text": "It cannot be judged without far more real-world "
                     "examples than a garden ripple, a sea wave and a tsunami "
                     "between them", "correct": False,
             "why": "A garden ripple, an ordinary sea wave and a "
                    "tsunami already give enough real examples to settle the "
                    "claim."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h29",
        "band": "harder",
        "text": "A wave gauge records amplitude readings from a buoy "
                "every hour: 0.2 m, 0.2 m, 0.2 m, 0.4 m, 0.2 m, 0.2 m. The "
                "wavelength stays at 25 m throughout. What is the most "
                "reasonable conclusion about the hour when 0.4 m was recorded?",
        "options": [
            {"text": "The wavelength must have secretly changed too, "
                     "since amplitude and wavelength always move together in "
                     "exactly the same direction as each other", "correct": False,
             "why": "The gauge reports the wavelength staying fixed at "
                    "25 m throughout — nothing in the data suggests it "
                    "changed."},
            {"text": "The buoy must have malfunctioned, since amplitude "
                     "should never change from hour to hour", "correct": False,
             "why": "Amplitude changing from hour to hour is exactly "
                    "what this lesson would predict for a rougher sea — it is "
                    "not evidence of a fault."},
            {"text": "A taller, more energetic set of waves passed "
                     "during that hour, while the spacing between crests stayed "
                     "the same", "correct": True},
            {"text": "Nothing meaningful can be concluded from a single "
                     "unusual reading", "correct": False,
             "why": "A clear rise in amplitude for one hour, with "
                    "wavelength unchanged, is exactly the kind of change this "
                    "lesson equips you to interpret."},
        ],
        "figure": None,
    },
    {
        "id": "p6-01-h30",
        "band": "harder",
        "text": "A student sketches a water wave whose crests and "
                "troughs get progressively closer together from left to right, "
                "all with the same height. A second student says this cannot be "
                "a real single wave, because 'a wave's wavelength has to stay "
                "constant all the way along.' Assess this second claim, and "
                "suggest what such a changing spacing might show instead.",
        "options": [
            {"text": "The second claim is right, and the drawing must "
                     "simply be a mistake", "correct": False,
             "why": "A changing wavelength along one wave is not ruled "
                    "out by anything in this lesson — the fixed-wavelength "
                    "tank is a simple case, not a universal rule."},
            {"text": "The second claim is right, because amplitude and "
                     "wavelength are actually one and the same measurement "
                     "underneath everything else, so of course both would always "
                     "have to stay perfectly fixed together the entire way along "
                     "any wave", "correct": False,
             "why": "Amplitude and wavelength are independent "
                    "measurements in this lesson, not the same thing, and "
                    "neither is forced to stay fixed by the other."},
            {"text": "Real waves can never have their spacing measured "
                     "more than once, so the second claim cannot be tested", "correct": False,
             "why": "Spacing between crests can be measured at any "
                    "point along a wave train — nothing prevents measuring it "
                    "more than once."},
            {"text": "The second claim goes too far: a fixed wavelength "
                     "is only a feature of the simple, steady case, not a rule "
                     "every real wave obeys — changing spacing more likely shows "
                     "the wave slowing down or speeding up", "correct": True},
        ],
        "figure": None,
    },
]
