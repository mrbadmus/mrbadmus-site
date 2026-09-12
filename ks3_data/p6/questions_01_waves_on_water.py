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
]
