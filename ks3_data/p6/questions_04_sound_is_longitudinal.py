"""P6 lesson 04 — Sound is longitudinal: twelve questions (MRB-223).

Written against Design's page. The two slinkies, the compare table and the
side-by-side drawing are hers.

The discriminations, in the order the lesson builds them:

  · the drawn wavy line is a GRAPH of pressure, not a picture of the air
    (`WAVE-13`);
  · a compression travels; the air in it does not (`WAVE-14`);
  · a longitudinal wave has an amplitude, measured as how far each bit of
    air shifts (`WAVE-15`);
  · a compression is a place where the air is CROWDED, not hot
    (`WAVE-16`) — the harder band sits here.

⚠️ POSITION IS AUTHORED — 3,1,2,0 · 1,2,0,3 · 0,3,2,1, three of each.

⚠️ The ladder's own two marked rungs are NOT restated.
"""

UNIT = "P6"
LESSON = "sound-is-longitudinal"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "p6-04-e01",
        "band": "easier",
        "text": "In a longitudinal wave, the particles move…",
        "options": [
            {"text": "at right angles to the direction the wave travels",
             "correct": False,
             "why": "That is a transverse wave, which is what water waves "
                    "do."},
            {"text": "in circles around their resting place", "correct": False,
             "why": "Circular motion is closer to what water waves do. In a "
                    "longitudinal wave the movement is along one line."},
            {"text": "not at all — only the wave moves", "correct": False,
             "why": "The particles have to move, or there would be nothing "
                    "to pass the disturbance on."},
            {"text": "backwards and forwards along the direction the wave "
                     "travels", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e02",
        "band": "easier",
        "text": "A place in a sound wave where the air is squeezed closer "
                "together is called a…",
        "options": [
            {"text": "crest", "correct": False,
             "why": "Crest belongs to transverse waves, where there is a "
                    "hump to be at the top of."},
            {"text": "compression", "correct": True},
            {"text": "rarefaction", "correct": False,
             "why": "A rarefaction is the opposite — a place where the air "
                    "is more spread out."},
            {"text": "trough", "correct": False,
             "why": "Trough also belongs to transverse waves."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e03",
        "band": "easier",
        "text": "A slinky is pushed and pulled along its own length. What "
                "travels down it?",
        "options": [
            {"text": "the coils themselves, from one end to the other",
             "correct": False,
             "why": "Each coil ends up back where it started. Nothing "
                    "reaches the far end except the disturbance."},
            {"text": "nothing — a slinky pushed that way just stretches",
             "correct": False,
             "why": "A clear pulse can be seen running down it, and it "
                    "arrives at the far end."},
            {"text": "a squeezed-up region, followed by a spread-out one",
             "correct": True},
            {"text": "a sideways hump", "correct": False,
             "why": "That is what happens if you flick the slinky sideways "
                    "instead — the transverse case."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e04",
        "band": "easier",
        "text": "The wavelength of a sound wave is the distance…",
        "options": [
            {"text": "from one compression to the next compression",
             "correct": True},
            {"text": "from a compression to the rarefaction beside it",
             "correct": False,
             "why": "That is half a wavelength — the equivalent of crest to "
                    "trough."},
            {"text": "the sound travels in one second", "correct": False,
             "why": "That is the speed of sound, which is a different "
                    "quantity."},
            {"text": "the air moves backwards and forwards", "correct": False,
             "why": "That is the amplitude of the wave, not its length."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "p6-04-s01",
        "band": "standard",
        "text": "Sound is often drawn as a wavy line. What is that line "
                "actually showing?",
        "options": [
            {"text": "The path the air takes as the sound goes past",
             "correct": False,
             "why": "The air does not travel a wavy path. It shuffles "
                    "backwards and forwards along one line."},
            {"text": "How crowded the air is at each place, plotted as a "
                     "graph", "correct": True},
            {"text": "The shape a sound wave has as it moves through the "
                     "air", "correct": False,
             "why": "A sound wave has no humps to have a shape. The picture "
                    "is a graph, not a photograph."},
            {"text": "The sideways vibration of the air particles",
             "correct": False,
             "why": "There is no sideways vibration in a sound wave. That is "
                    "the transverse case."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s02",
        "band": "standard",
        "text": "A loudspeaker plays a note across a room. What reaches the "
                "listener?",
        "options": [
            {"text": "Air that was next to the cone, pushed all the way "
                     "across the room and arriving at the listener's ear", "correct": False,
             "why": "That air moves a fraction of a millimetre and stays "
                    "near the speaker. Nothing is delivered across the room."},
            {"text": "A steady breeze from the speaker", "correct": False,
             "why": "There is no breeze. Hold a candle in front of a "
                    "speaker and the flame is undisturbed."},
            {"text": "A travelling pattern of squeezed and spread-out air, "
                     "handed on from one bit of air to the next",
             "correct": True},
            {"text": "The vibration of the cone itself, carried through the "
                     "air", "correct": False,
             "why": "The cone stays in the speaker. What travels is the "
                    "disturbance it set going."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s03",
        "band": "standard",
        "text": "What is the amplitude of a sound wave a measurement of?",
        "options": [
            {"text": "How far each bit of air shifts from its resting place "
                     "as the wave passes", "correct": True},
            {"text": "How far apart the compressions are", "correct": False,
             "why": "That is the wavelength."},
            {"text": "How high the wavy line is drawn on the page",
             "correct": False,
             "why": "The height on the page represents the amplitude, but "
                    "the amplitude itself is a real distance in the air."},
            {"text": "Sound waves have no amplitude, because there is no "
                     "hump to measure", "correct": False,
             "why": "There is a real quantity to measure: how far the air is "
                    "shifted, and how much the pressure changes with it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s04",
        "band": "standard",
        "text": "Which of these is a genuine difference between a water wave "
                "and a sound wave in air?",
        "options": [
            {"text": "Only one of them carries energy", "correct": False,
             "why": "Both carry energy. That is what a wave does."},
            {"text": "Only one of them needs a material to travel through, "
                     "and the other can cross a gap with nothing in it",
             "correct": False,
             "why": "Both do. A water wave obviously needs water, and a "
                    "sound wave needs a medium too."},
            {"text": "Only one of them can be reflected", "correct": False,
             "why": "Both reflect. A ripple bounces off a tank wall and a "
                    "shout bounces off a cliff."},
            {"text": "In one, the material moves at right angles to the "
                     "travel; in the other, along it", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "p6-04-h01",
        "band": "harder",
        "text": "A student says a compression is a place where the air is "
                "hotter. What is the best correction?",
        "options": [
            {"text": "A compression is a place where the air is crowded "
                     "together and the pressure is higher; temperature is "
                     "not what defines it", "correct": True},
            {"text": "A compression is where the air is colder, not hotter",
             "correct": False,
             "why": "Swapping hot for cold keeps the same mistake. "
                    "Temperature is not the defining property either way."},
            {"text": "A compression is a place where the air is moving "
                     "fastest, and how quickly it is moving is what the "
                     "word records", "correct": False,
             "why": "Air speed and air crowding are different things, and "
                    "the crowding is what the word means."},
            {"text": "A compression is where the sound is loudest",
             "correct": False,
             "why": "Loudness belongs to the whole wave, not to one part of "
                    "it. Every wave has compressions, loud or quiet."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h02",
        "band": "harder",
        "text": "Both a slinky pushed along its length and a slinky flicked "
                "sideways send a pulse to the far end. Why is only one of "
                "them a model of sound?",
        "options": [
            {"text": "Because only one of them carries energy",
             "correct": False,
             "why": "Both carry energy to the far end, and both can knock "
                    "something over when they arrive."},
            {"text": "Because only one of them travels", "correct": False,
             "why": "Both travel. The difference is in what the coils do, "
                    "not in whether the pulse gets there."},
            {"text": "Because the sideways one is easier to see, and a "
                     "model has to be watchable before it can be a model of "
                     "anything",
             "correct": False,
             "why": "How easy something is to see does not decide what it is "
                    "a model of."},
            {"text": "Because sound moves the air along the direction it "
                     "travels, which is what the pushed slinky does and the "
                     "flicked one does not", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h03",
        "band": "harder",
        "text": "A microphone is placed in front of a speaker playing a "
                "steady note. Its diaphragm moves backwards and forwards. "
                "What is pushing it?",
        "options": [
            {"text": "A stream of air arriving from the speaker",
             "correct": False,
             "why": "No stream arrives. The diaphragm goes backwards as well "
                    "as forwards, which a one-way stream could not do."},
            {"text": "The magnetic field of the speaker reaching across the "
                     "room and pulling the diaphragm to and fro at a "
                     "distance", "correct": False,
             "why": "The magnet's field does not reach that far, and the "
                    "microphone works just as well behind a screen."},
            {"text": "Air pressure that rises above and falls below normal "
                     "in turn as compressions and rarefactions arrive",
             "correct": True},
            {"text": "The vibration of the floor between them",
             "correct": False,
             "why": "The microphone works with the speaker held in the air, "
                    "touching nothing."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h04",
        "band": "harder",
        "text": "Why can a water wave be photographed and a sound wave "
                "cannot?",
        "options": [
            {"text": "Because a sound wave moves too fast for a camera to "
                     "freeze, and anything moving that quickly cannot be "
                     "photographed however short the exposure is",
             "correct": False,
             "why": "Cameras freeze far faster things than sound. Speed is "
                    "not the obstacle."},
            {"text": "Because a water wave changes the SHAPE of a surface "
                     "you can see, while a sound wave only changes how "
                     "crowded invisible air is", "correct": True},
            {"text": "Because sound waves are too small to see",
             "correct": False,
             "why": "Sound wavelengths are often around a metre — far from "
                    "small. It is the air being invisible that matters."},
            {"text": "Because sound waves do not exist until they are heard",
             "correct": False,
             "why": "A microphone with nobody in the room records them "
                    "perfectly well."},
        ],
        "figure": None,
    },
]
