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
            {"text": "at right angles to the direction in which the wave "
                     "travels", "correct": False,
             "why": "That is a transverse wave, which is what water waves "
                    "do."},
            {"text": "in small circles around the place where they were "
                     "resting", "correct": False,
             "why": "Circular motion is closer to what water waves do. In a "
                    "longitudinal wave the movement is along one line."},
            {"text": "not at all — the wave moves and the particles all "
                     "stay put", "correct": False,
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
            {"text": "A steady breeze from the speaker, blowing gently "
                     "against the listener the whole time the note lasts",
             "correct": False,
             "why": "There is no breeze. Hold a candle in front of a "
                    "speaker and the flame is undisturbed."},
            {"text": "A travelling pattern of squeezed and spread-out air, "
                     "handed on from one bit of air to the next",
             "correct": True},
            {"text": "The vibration of the cone itself, carried across the "
                     "room and arriving intact at the listener",
             "correct": False,
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
            {"text": "How far apart the compressions are spaced out along "
                     "the wave", "correct": False,
             "why": "That is the wavelength."},
            {"text": "How high the wavy line is drawn on the page it is "
                     "printed on", "correct": False,
             "why": "The height on the page represents the amplitude, but "
                    "the amplitude itself is a real distance in the air."},
            {"text": "Sound waves have no amplitude at all, because there "
                     "is no hump to measure", "correct": False,
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
            {"text": "Only one of them carries energy, and the other "
                     "simply passes a shape along without any energy at "
                     "all", "correct": False,
             "why": "Both carry energy. That is what a wave does."},
            {"text": "Only one of them needs a material to travel through, "
                     "and the other can cross a gap with nothing in it",
             "correct": False,
             "why": "Both do. A water wave obviously needs water, and a "
                    "sound wave needs a medium too."},
            {"text": "Only one of them can be reflected, and the other is "
                     "soaked up by whatever surface it happens to meet",
             "correct": False,
             "why": "Both reflect. A ripple bounces off a tank wall and a "
                    "shout bounces off a cliff."},
            {"text": "In one, the material moves at right angles to the "
                     "travel; in the other, along the line of it",
             "correct": True},
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
            {"text": "A compression is a place where the air is colder "
                     "rather than hotter, and it is the drop in "
                     "temperature that the word records", "correct": False,
             "why": "Swapping hot for cold keeps the same mistake. "
                    "Temperature is not the defining property either way."},
            {"text": "A compression is a place where the air is moving "
                     "fastest, and how quickly it is moving is what the "
                     "word actually records", "correct": False,
             "why": "Air speed and air crowding are different things, and "
                    "the crowding is what the word means."},
            {"text": "A compression is a place where the sound happens to "
                     "be at its loudest, and that loudness is what the "
                     "word records", "correct": False,
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
            {"text": "Because only one of them carries energy along to the "
                     "far end, and carrying energy from place to place is "
                     "what sound does", "correct": False,
             "why": "Both carry energy to the far end, and both can knock "
                    "something over when they arrive."},
            {"text": "Because only one of them actually travels from one "
                     "end of the slinky to the other, and sound has to "
                     "travel to reach you", "correct": False,
             "why": "Both travel. The difference is in what the coils do, "
                    "not in whether the pulse gets there."},
            {"text": "Because the sideways one is easier to see, and a "
                     "model has to be watchable before it can be a model "
                     "of anything at all",
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
            {"text": "A stream of air arriving from the speaker and "
                     "blowing steadily against the front face of the "
                     "diaphragm", "correct": False,
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
            {"text": "The vibration of the floor between them, passed up "
                     "through the bench and the stand the microphone sits "
                     "on", "correct": False,
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
                     "crowded the invisible air is", "correct": True},
            {"text": "Because sound waves are far too small to see, being "
                     "well below the size of anything that a camera lens "
                     "could ever hope to resolve", "correct": False,
             "why": "Sound wavelengths are often around a metre — far from "
                    "small. It is the air being invisible that matters."},
            {"text": "Because sound waves do not exist until they are "
                     "heard, so there is nothing there for a camera to "
                     "record until somebody is in the room to listen",
             "correct": False,
             "why": "A microphone with nobody in the room records them "
                    "perfectly well."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-04-e05",
        "band": "easier",
        "text": "A place in a sound wave where the air is pulled further "
                "apart is called a…",
        "options": [            {"text": "compression", "correct": False,
             "why": "A compression is the opposite: a place where the air is "
                    "bunched together."},
            {"text": "vacuum", "correct": False,
             "why": "A vacuum has no particles at all; a rarefaction still "
                    "has air, just more spread out."},
            {"text": "trough", "correct": False,
             "why": "Troughs belong to transverse waves, where the surface "
                    "dips below its rest level."},
            {"text": "rarefaction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e06",
        "band": "easier",
        "text": "Sound travelling through a steel bar is…",
        "options": [
            {"text": "transverse, because steel is solid", "correct": False,
             "why": "Being solid does not change it: sound is longitudinal in "
                    "solids, liquids and gases alike."},
            {"text": "longitudinal, as it is in air", "correct": True},
            {"text": "neither, because sound cannot pass through metal",
             "correct": False,
             "why": "It passes very well, and faster than through air."},
            {"text": "transverse in the steel and longitudinal in the air",
             "correct": False,
             "why": "It is longitudinal in both; the material changes the "
                    "speed, not the kind of wave."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-04-s05",
        "band": "standard",
        "text": "Which is a longitudinal wave: a rope flicked sideways, or a "
                "slinky pushed along its own length?",
        "options": [
            {"text": "The rope, because the pulse travels along it",
             "correct": False,
             "why": "The pulse travels along both. What matters is which way "
                    "the material itself moves."},
            {"text": "The slinky, because its coils move along the direction "
                     "of travel",
             "correct": True},
            {"text": "Both, because both send a pulse to the far end",
             "correct": False,
             "why": "Sending a pulse is what makes them waves; the rope's "
                    "material moves at right angles, so it is transverse."},
            {"text": "Neither — only sound in air is longitudinal",
             "correct": False,
             "why": "A pushed slinky is the standard model of a longitudinal "
                    "wave precisely because it behaves like sound."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s06",
        "band": "standard",
        "text": "Each patch of air in a sound wave finishes where it started. "
                "What does that tell you?",
        "options": [            {"text": "That the sound has not really travelled anywhere",
             "correct": False,
             "why": "The disturbance travels the whole way; it is the air "
                    "that stays put."},
            {"text": "That the wave must be transverse after all",
             "correct": False,
             "why": "Returning to the starting place happens in both kinds; "
                    "the DIRECTION of the movement is what decides."},
            {"text": "That sound can only travel a short distance",
             "correct": False,
             "why": "Thunder is heard kilometres away, with no air making the "
                    "journey."},
            {"text": "That no air travels from the source to the listener",
             "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-04-h05",
        "band": "harder",
        "text": "A longitudinal wave has no humps to measure. What is its "
                "amplitude?",
        "options": [
            {"text": "It has none, because there is nothing to measure",
             "correct": False,
             "why": "It certainly has one — that is what makes a sound loud "
                    "or quiet."},
            {"text": "The distance between one compression and the next",
             "correct": False,
             "why": "That is the wavelength, which is a different measurement "
                    "altogether."},
            {"text": "How far each patch of air moves from its rest place",
             "correct": True},
            {"text": "How many compressions pass each second",
             "correct": False,
             "why": "That is the frequency, which sets the pitch rather than "
                    "the loudness."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h06",
        "band": "harder",
        "text": "In a compression the air is bunched together. Why does that "
                "not mean air is travelling to your ear?",
        "options": [
            {"text": "Because the bunching is too small to notice",
             "correct": False,
             "why": "Size is not the point: even a very loud sound moves no "
                    "air from the source to the listener."},
            {"text": "Because the air is bunched only near the source",
             "correct": False,
             "why": "Compressions form all the way along; each one is passed "
                    "on to the next patch of air."},
            {"text": "Because each patch shuffles to and fro, while the "
                     "bunching travels on",
             "correct": True},
            {"text": "Because the compression is made of a different gas",
             "correct": False,
             "why": "It is the same air, momentarily closer together than "
                    "usual."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · easier ──────────────────────────────────────────
    {
        "id": "p6-04-e07",
        "band": "easier",
        "text": 'As a sound wave passes one fixed point in the air, what '
                'happens to the pressure there?',
        "options": [
            {"text": 'It rises and falls repeatedly, above and below the normal '
                     'pressure', "correct": True},
            {"text": 'It rises and then stays high for as long as the sound '
                     'lasts', "correct": False,
             "why": 'The pressure does not hold at one high value; compressions '
                    'and rarefactions pass the point one after another.'},
            {"text": 'It stays the same throughout, and only the particles move', "correct": False,
             "why": 'The particles moving back and forth is exactly what '
                    'bunches them up and spreads them out, so the pressure '
                    'there does change.'},
            {"text": 'It falls to nothing in the gap between one compression '
                     'and the next',
             "correct": False,
             "why": 'A rarefaction is air spread thinner than usual, not air '
                    'removed; the pressure dips below normal rather than to '
                    'nothing.'},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e08",
        "band": "easier",
        "text": "A rarefaction in a sound wave is best described as…",
        "options": [
            {"text": "a gap where the air is more spread out than usual",
             "correct": True},
            {"text": "a downward dip where the air presses down harder "
                     "than usual", "correct": False,
             "why": "A rarefaction is a spreading-out of the particles, not "
                    "a downward dip."},
            {"text": "a place with no air at all", "correct": False,
             "why": "The air is thinner there, not completely absent."},
            {"text": "the same thing as a compression", "correct": False,
             "why": "A rarefaction and a compression are opposites: one is "
                    "bunched up, the other spread out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e09",
        "band": "easier",
        "text": "Sound travelling through air, through water, and through "
                "steel is, in every one of those materials, a…",
        "options": [
            {"text": "transverse wave", "correct": False,
             "why": "Sound moves the particles along its own direction of "
                    "travel, which makes it longitudinal, not transverse."},
            {"text": "standing wave", "correct": False,
             "why": "A standing wave is a special pattern from two waves "
                    "overlapping, not simply how sound normally travels."},
            {"text": "wave with no fixed type — it depends on the "
                     "material", "correct": False,
             "why": "Sound is longitudinal in every material it travels "
                    "through, whatever that material is."},
            {"text": "longitudinal wave", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e10",
        "band": "easier",
        "text": "For a sound wave, the wavelength is the distance from…",
        "options": [
            {"text": "one compression to the next compression",
             "correct": True},
            {"text": 'from one compression to the next rarefaction along the '
                     'wave', "correct": False,
             "why": "That distance is only half a wavelength."},
            {"text": "the speaker to the ear", "correct": False,
             "why": "That is simply how far the sound has to travel, not "
                    "the length of one wave."},
            {"text": "start to stop", "correct": False,
             "why": "That is a measure of time, not a distance along the "
                    "wave."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e11",
        "band": "easier",
        "text": "Does a longitudinal sound wave have an amplitude?",
        "options": [
            {"text": "No — only transverse waves have an amplitude",
             "correct": False,
             "why": "A longitudinal wave has an amplitude too; it is just "
                    "measured differently from a transverse wave's."},
            {"text": "No — a longitudinal wave only has a wavelength",
             "correct": False,
             "why": "It has both a wavelength and an amplitude, just like "
                    "a transverse wave does."},
            {"text": "Yes — it is a measure of how far the air itself "
                     "moves up and down as the sound wave passes by",
             "correct": False,
             "why": "Sound does not move the air up and down; the "
                    "amplitude is about how much the pressure changes, not "
                    "an up-and-down movement."},
            {"text": "Yes — it is the size of the pressure change at a "
                     "compression or rarefaction", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ────────────────────────────────────────
    {
        "id": "p6-04-s07",
        "band": "standard",
        "text": "A sound wave has compressions 34 cm apart. What is the "
                "distance between one rarefaction and the next?",
        "options": [
            {"text": "17 cm", "correct": False,
             "why": "That is compression to rarefaction, which is half a "
                    "wavelength."},
            {"text": "34 cm", "correct": True},
            {"text": "68 cm", "correct": False,
             "why": "That doubles the wavelength rather than finding the "
                    "rarefaction-to-rarefaction spacing, which matches the "
                    "compression-to-compression spacing."},
            {"text": "It cannot be found without knowing the amplitude",
             "correct": False,
             "why": "Amplitude is about the size of the pressure change, "
                    "not the spacing between rarefactions."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s08",
        "band": "standard",
        "text": "A student says a compression must be hotter than the "
                "surrounding air, since it is where the air is squeezed "
                "together. What is wrong with this?",
        "options": [
            {"text": 'Nothing is wrong — squeezing air together always heats it '
                     'up, which is why a compression is the warmer part of a '
                     'sound wave', "correct": False,
             "why": "A compression is described by how bunched the "
                    "particles are, not by any noticeable change in "
                    "temperature."},
            {"text": "A compression is a region of higher pressure and "
                     "density, not a region of higher temperature",
             "correct": True},
            {"text": "It is colder, not hotter", "correct": False,
             "why": "Temperature is not what a compression describes "
                    "either way — it is about pressure and density."},
            {"text": 'It is wrong because sound cannot create compressions in '
                     'air at all; only a pump squeezing air into a cylinder can '
                     'do that', "correct": False,
             "why": "Sound genuinely does create compressions in air; "
                    "that is exactly how a longitudinal wave is built."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s09",
        "band": "standard",
        "text": "At a compression, does any single particle of air travel "
                "all the way from the speaker to your ear?",
        "options": [
            {"text": "Yes — the compression is a lump of air that moves "
                     "the whole distance", "correct": False,
             "why": "A compression is a pattern that travels; the "
                    "individual particles only shift back and forth a "
                    "short distance."},
            {"text": 'Yes, but only right at a compression — everywhere else, a '
                     'rarefaction included, the particles stay still, because '
                     'nothing there is pushing them along', "correct": False,
             "why": "Particles keep moving back and forth throughout the "
                    "wave, in both compressions and rarefactions."},
            {"text": "No — nothing at all moves anywhere in a sound wave",
             "correct": False,
             "why": "The particles do move, just not all the way from the "
                    "speaker to the ear; only the pattern travels that "
                    "far."},
            {"text": "No — each particle moves back and forth a short "
                     "distance, and the compression pattern is what "
                     "travels the whole way", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s10",
        "band": "standard",
        "text": "A textbook draws a sound wave as a graph of pressure "
                "against distance, which looks like a wavy line going up "
                "and down. Does this mean the air itself moves up and "
                "down as sound passes through it?",
        "options": [
            {"text": "Yes — the rising and falling shape of the graph "
                     "shows that the air itself is genuinely rising and "
                     "falling as the sound passes through it", "correct": False,
             "why": "The graph plots pressure, not height; the air itself "
                    "moves along the direction of travel, not up and "
                    "down."},
            {"text": "No — the graph plots pressure against distance, and "
                     "the air itself moves back and forth along the "
                     "direction of travel", "correct": True},
            {"text": "It depends on how loud the sound is", "correct": False,
             "why": "Loudness changes the size of the pressure change, not "
                    "which direction the air particles move in."},
            {"text": 'Yes, but only for very low-pitched sounds, whose long '
                     'wavelengths give the air time to rise and fall before the '
                     'next wave arrives',
             "correct": False,
             "why": "Pitch does not change the direction air particles "
                    "move in; sound is longitudinal at every pitch."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ──────────────────────────────────────────
    {
        "id": "p6-04-h07",
        "band": "harder",
        "text": "An earthquake sends out longitudinal P waves and "
                "transverse S waves through the Earth at once. Seismometers "
                "on the far side of the planet detect the P waves but "
                "record no S waves at all. What does this suggest about "
                "the material the S waves would have had to cross?",
        "options": [
            {"text": "That material must be a solid, since solids block S "
                     "waves completely", "correct": False,
             "why": "It is the opposite — solids CAN carry S waves; it is "
                    "a liquid that an S wave cannot cross."},
            {"text": "That material must be liquid, since a transverse "
                     "wave needs the material to resist being sheared "
                     "sideways, and a liquid does not", "correct": True},
            {"text": 'That material must be moving faster than the P waves '
                     'themselves, which is why the S waves never catch up and '
                     'reach the far side of the planet', "correct": False,
             "why": "Nothing here is about relative speed catching up; S "
                    "waves are missing entirely, not simply delayed."},
            {"text": 'The missing S waves show nothing about the material, '
                     'since P and S waves travel identical paths through the '
                     'Earth', "correct": False,
             "why": "P and S waves behave differently in different "
                    "materials, which is exactly why the missing S waves "
                    "are meaningful evidence."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h08",
        "band": "harder",
        "text": "On deep water, a floating patch actually travels round a "
                "small circle rather than straight up and down as a wave "
                "passes. A student says this proves a water wave cannot "
                "really be transverse at all. Assess this.",
        "options": [
            {"text": "The student is right — a water wave must actually "
                     "be purely longitudinal, and calling it transverse is "
                     "simply a mistake", "correct": False,
             "why": "A water wave is not purely longitudinal either; the "
                    "circular motion mixes both kinds of movement."},
            {"text": 'The student is right, and this shows the transverse and '
                     'longitudinal idea never applied to water, or to any wave '
                     'on a liquid surface', "correct": False,
             "why": "The transverse/longitudinal distinction still "
                    "applies to water waves — it is just that a real one "
                    "is a mixture of both rather than purely one or the "
                    "other."},
            {"text": 'The student is wrong, but only because the circular '
                     'motion is too small to matter in a real wave', "correct": False,
             "why": "The circular motion is a genuine, measurable feature "
                    "of a real water wave, not something too small to "
                    "matter."},
            {"text": "The student is wrong — the simple straight up-and-"
                     "down picture is close enough for most purposes, "
                     "even though a real surface wave is partly transverse "
                     "and partly longitudinal at once", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ───────────────────────────────────
    {
        "id": "p6-04-e12",
        "band": "easier",
        "text": "Which pair of terms belongs to a transverse wave, "
                "not a longitudinal one?",
        "options": [
            {"text": "Crest and trough", "correct": True},
            {"text": "Compression and rarefaction", "correct": False,
             "why": "Compression and rarefaction are the longitudinal "
                    "pair — crest and trough belong to a transverse wave "
                    "instead."},
            {"text": "Push and pull", "correct": False,
             "why": "Push and pull describe an action on a slinky, "
                    "not the proper names for the two regions a longitudinal "
                    "wave forms."},
            {"text": "Squeeze and stretch", "correct": False,
             "why": "Squeeze and stretch describe what happens to the "
                    "coils, but the proper names are compression and "
                    "rarefaction."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e13",
        "band": "easier",
        "text": "In a compression, is the pressure of the air higher "
                "or lower than normal?",
        "options": [
            {"text": "Lower than normal", "correct": False,
             "why": "Lower than normal describes a rarefaction. A "
                    "compression is the opposite: the air is squeezed, so "
                    "the pressure rises."},
            {"text": "Higher than normal", "correct": True},
            {"text": "Exactly the same as normal", "correct": False,
             "why": "If the pressure stayed unchanged there would be "
                    "nothing to call a compression; the point is that it is "
                    "squeezed above normal."},
            {"text": "There is simply no pressure there", "correct": False,
             "why": "A compression still has air in it, just more "
                    "crowded than usual, so it still has a pressure."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e14",
        "band": "easier",
        "text": "Which best describes what has happened to the air "
                "in a rarefaction?",
        "options": [
            {"text": "It has been pulled further apart than its "
                     "resting spacing, so its pressure has dropped below "
                     "normal", "correct": True},
            {"text": "It has been squeezed closer together than its "
                     "resting spacing, so its pressure has risen above "
                     "normal", "correct": False,
             "why": "That describes a compression, the opposite "
                    "region to a rarefaction."},
            {"text": "It has stayed at exactly its resting spacing, "
                     "with no change in pressure", "correct": False,
             "why": "A rarefaction is defined by a real change from "
                    "the resting spacing; if nothing changed there would be "
                    "no rarefaction to speak of."},
            {"text": "It has been removed completely, leaving a "
                     "small pocket with no air in it", "correct": False,
             "why": "The air has spread out, not vanished; a "
                    "rarefaction still contains air, simply thinned out."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e15",
        "band": "easier",
        "text": "A struck tuning fork sets a longitudinal wave going "
                "in the air around it. What is the name for the squeezed "
                "regions of air next to it?",
        "options": [
            {"text": "Crests", "correct": False,
             "why": "Crests belong to a transverse wave. The squeezed "
                    "regions of a longitudinal wave have their own name."},
            {"text": "Rarefactions", "correct": False,
             "why": "A rarefaction is the spread-out region, the "
                    "opposite of a squeezed one."},
            {"text": "Compressions", "correct": True},
            {"text": "Troughs", "correct": False,
             "why": "Troughs also belong to a transverse wave, not a "
                    "longitudinal one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e16",
        "band": "easier",
        "text": "A cymbal vibrates rapidly, and the air next to it "
                "is squeezed together and pulled apart over and over. What "
                "kind of wave is this?",
        "options": [
            {"text": "A longitudinal wave", "correct": True},
            {"text": "A transverse wave", "correct": False,
             "why": "A transverse wave shows crests and troughs, not "
                    "the squeezed and spread-out regions described here."},
            {"text": "A standing wave", "correct": False,
             "why": "A standing wave is a special pattern made by two "
                    "waves overlapping, not what a single vibrating cymbal "
                    "produces in the air."},
            {"text": "An electromagnetic wave", "correct": False,
             "why": "Electromagnetic waves like light need no "
                    "particles at all. This wave is made of moving air "
                    "particles."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e17",
        "band": "easier",
        "text": "A wave is described using the words 'compression' "
                "and 'rarefaction' rather than 'crest' and 'trough'. What "
                "must be true of the wave?",
        "options": [
            {"text": "It must be a water wave", "correct": False,
             "why": "Water waves are usually described with crests "
                    "and troughs, since they behave as transverse waves."},
            {"text": "It must be longitudinal", "correct": True},
            {"text": "It must be too quiet to hear", "correct": False,
             "why": "The choice of words describes the type of wave, "
                    "and says nothing about how loud it is."},
            {"text": "It must be reflecting off a surface", "correct": False,
             "why": "Compression and rarefaction describe the wave "
                    "itself, not what happens when it meets a surface."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e18",
        "band": "easier",
        "text": "A compression of a sound wave passes a fixed "
                "particle of air. Once it has gone by, where is that "
                "particle?",
        "options": [
            {"text": "Further along, in the direction the wave was "
                     "travelling", "correct": False,
             "why": "The particle only shuffles a short distance and "
                    "returns; it does not travel onward with the wave."},
            {"text": "Further back, the way the wave came from", "correct": False,
             "why": "The particle ends up back where it started, not "
                    "shifted backwards."},
            {"text": "At a new position that cannot be predicted", "correct": False,
             "why": "The particle's motion is not unpredictable — it "
                    "moves in one line and returns to its starting place."},
            {"text": "Back where it started", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e19",
        "band": "easier",
        "text": "A sound wave crosses a room from a speaker to a "
                "listener 5 m away. How many times does a single particle of "
                "air travel the whole 5 m?",
        "options": [
            {"text": "Once, arriving exactly when the sound is "
                     "heard", "correct": False,
             "why": "No single particle makes that journey. Each one "
                    "only shuffles a short distance near where it started."},
            {"text": "Many times, back and forth across the room", "correct": False,
             "why": "A particle shuffles back and forth over a tiny "
                    "distance, not across the whole room."},
            {"text": "Zero times — no particle makes that journey", "correct": True},
            {"text": "Half the distance, with the pattern "
                     "completing the rest", "correct": False,
             "why": "The pattern completes the whole distance; no "
                    "particle contributes even part of that journey."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e20",
        "band": "easier",
        "text": "A slinky is squeezed at one end and let go, sending "
                "a squeezed group of coils travelling down its length. What "
                "is this squeezed group an example of?",
        "options": [
            {"text": "A compression", "correct": True},
            {"text": "A crest", "correct": False,
             "why": "A crest is the top of a hump in a transverse "
                    "wave. This slinky is not making any humps."},
            {"text": "A trough", "correct": False,
             "why": "A trough is the bottom of a dip in a transverse "
                    "wave, which this longitudinal motion does not have."},
            {"text": "A rarefaction", "correct": False,
             "why": "A rarefaction is the spread-out region, the "
                    "opposite of a squeezed one."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e21",
        "band": "easier",
        "text": "Besides one compression to the next compression, "
                "which other pair of points on a sound wave is exactly one "
                "wavelength apart?",
        "options": [
            {"text": "A compression and the rarefaction right next "
                     "to it", "correct": False,
             "why": "That gap is only half a wavelength, the same as "
                    "crest to trough in a transverse wave."},
            {"text": "One rarefaction to the very next rarefaction", "correct": True},
            {"text": "The very start of the wave to its very end", "correct": False,
             "why": "That distance depends on how long the wave "
                    "lasts, not on the length of one repeat."},
            {"text": "Any two points chosen along the wave", "correct": False,
             "why": "Only points that repeat the same part of the "
                    "pattern, like rarefaction to rarefaction, are one "
                    "wavelength apart."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e22",
        "band": "easier",
        "text": "For a sound wave, a bigger amplitude means…",
        "options": [
            {"text": "a bigger wavelength, with the compressions "
                     "spread further apart along the wave", "correct": False,
             "why": "Wavelength and amplitude are separate "
                    "measurements; a bigger amplitude does not require a "
                    "bigger wavelength."},
            {"text": "more compressions passing each second", "correct": False,
             "why": "That describes frequency, a different "
                    "measurement from amplitude."},
            {"text": "a bigger change in pressure at the "
                     "compressions and rarefactions", "correct": True},
            {"text": "a higher-pitched note", "correct": False,
             "why": "Pitch is set by frequency. Amplitude changing "
                    "does not change the pitch."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e23",
        "band": "easier",
        "text": "A drum skin moves outward as it vibrates, pushing "
                "the air next to it. What is the crowded region that results "
                "called?",
        "options": [
            {"text": "A rarefaction", "correct": False,
             "why": "A rarefaction is a spread-out region, made when "
                    "the skin pulls back, not when it pushes out."},
            {"text": "A crest, as in a transverse wave", "correct": False,
             "why": "A crest belongs to a transverse wave; this is "
                    "the longitudinal case."},
            {"text": "A compression", "correct": True},
            {"text": "A trough, as in a transverse wave", "correct": False,
             "why": "A trough belongs to a transverse wave, and this "
                    "is a squeezing together, the opposite of a dip."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e24",
        "band": "easier",
        "text": "The same drum skin then moves back past its resting "
                "position, leaving a spread-out region of air behind it. "
                "What is this spread-out region called?",
        "options": [
            {"text": "A rarefaction", "correct": True},
            {"text": "A compression", "correct": False,
             "why": "A compression is made by the skin pushing out, "
                    "not by it moving back."},
            {"text": "A crest, from a transverse wave", "correct": False,
             "why": "Crests belong to a transverse wave, not this "
                    "longitudinal one."},
            {"text": "A trough, from a transverse wave", "correct": False,
             "why": "Troughs belong to a transverse wave too."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e25",
        "band": "easier",
        "text": "A human vocal cord vibrates rapidly to make speech. "
                "The sound wave this sets up in the air is…",
        "options": [
            {"text": "transverse, since sound is drawn as a wavy "
                     "line", "correct": False,
             "why": "The wavy line is a graph, not a picture. The air "
                    "itself moves along the direction the sound is going."},
            {"text": "longitudinal", "correct": True},
            {"text": "a standing wave that stays in one place", "correct": False,
             "why": "The sound travels away from the speaker to a "
                    "listener; it is not a fixed standing pattern."},
            {"text": "too quiet for the air to be disturbed much", "correct": False,
             "why": "Vocal cords are exactly what starts speech "
                    "sounds; their vibration disturbs the air well enough to "
                    "be heard."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e26",
        "band": "easier",
        "text": "A wave shows no crests or troughs at all when you "
                "look at how the material itself is moving. What could you "
                "conclude?",
        "options": [
            {"text": "The wave carries no energy", "correct": False,
             "why": "It still carries energy; the absence of crests "
                    "and troughs is about the direction of movement, not "
                    "about energy."},
            {"text": "The wave must be standing still", "correct": False,
             "why": "A wave can travel perfectly well without ever "
                    "forming a crest or a trough."},
            {"text": "The wave cannot have a wavelength", "correct": False,
             "why": "It still has a wavelength — the distance from "
                    "one compression to the next, for example."},
            {"text": "The wave is more likely to be longitudinal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e27",
        "band": "easier",
        "text": "Which of these is a real difference between what a "
                "compression is and what a crest is?",
        "options": [
            {"text": "A compression is particles bunched together; "
                     "a crest is particles displaced sideways to their "
                     "highest point", "correct": True},
            {"text": "A compression belongs to water and a crest "
                     "belongs to air, and swapping the two round would mean "
                     "swapping which wave each material is able to carry", "correct": False,
             "why": "Neither is tied to one material. Compressions "
                    "happen in sound in any medium; crests happen in "
                    "transverse waves such as light or water waves."},
            {"text": "A compression is silent and a crest makes a "
                     "sound", "correct": False,
             "why": "Neither term says anything about loudness on its "
                    "own."},
            {"text": "There is no real difference between the two "
                     "words — a compression and a crest simply mean the same "
                     "physical thing described in two different ways", "correct": False,
             "why": "They describe different kinds of disturbance, in "
                    "different kinds of wave, and are not interchangeable."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e28",
        "band": "easier",
        "text": "A loudspeaker is playing a single steady note. "
                "Somewhere in the room, at one instant, the air is at a "
                "rarefaction. What is happening to the air there?",
        "options": [
            {"text": "It is being pushed towards the listener", "correct": False,
             "why": "The air at a rarefaction has just been pulled "
                    "back, not pushed forward."},
            {"text": "It is completely still", "correct": False,
             "why": "The air there is mid-motion, part of the ongoing "
                    "back-and-forth, rather than frozen still."},
            {"text": "It has been pulled further apart than its "
                     "resting spacing", "correct": True},
            {"text": "It has stopped existing until the next "
                     "compression arrives", "correct": False,
             "why": "The air is still there the whole time — just "
                    "spread out rather than removed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e29",
        "band": "easier",
        "text": "A pupil says a longitudinal wave 'has no shape, so "
                "it cannot be drawn at all'. What is the best response?",
        "options": [
            {"text": "They are right — a longitudinal wave has no "
                     "shape a pencil could trace out on paper, so no drawing "
                     "of any kind could ever capture what it is doing", "correct": False,
             "why": "It can be drawn, for example as a row of dots "
                    "bunched and spread out, or as a graph of pressure "
                    "against distance."},
            {"text": "It can be drawn as a graph of pressure "
                     "against distance, even though the air itself has no "
                     "hump-shape", "correct": True},
            {"text": "It can be understood by listening to it, but "
                     "not properly by drawing it", "correct": False,
             "why": "Physicists routinely draw longitudinal waves as "
                    "graphs; hearing is not the sole way to represent one."},
            {"text": "It can be drawn, but first needs to be "
                     "redrawn as a transverse wave", "correct": False,
             "why": "Turning it into a transverse picture would "
                    "misrepresent it; a longitudinal wave is drawn directly "
                    "as a graph of pressure or displacement."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-e30",
        "band": "easier",
        "text": "A wave has compressions spaced 25 cm apart. What "
                "can you say about the rarefactions?",
        "options": [
            {"text": "They are also spaced 25 cm apart, each one "
                     "sitting midway between two compressions", "correct": True},
            {"text": "They are spaced 12.5 cm apart from each "
                     "other, matching the gap from a compression across to "
                     "its neighbouring rarefaction", "correct": False,
             "why": "12.5 cm is the gap from a compression to the "
                    "next rarefaction, not rarefaction to rarefaction, which "
                    "matches the compression spacing."},
            {"text": "They are spaced 50 cm apart", "correct": False,
             "why": "That doubles the spacing rather than matching it "
                    "to the compressions."},
            {"text": "Their spacing cannot be found without knowing "
                     "the amplitude", "correct": False,
             "why": "Amplitude is a separate measurement about "
                    "pressure change, not about spacing along the wave."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · standard ─────────────────────────────────
    {
        "id": "p6-04-s11",
        "band": "standard",
        "text": "A whistle blows and a sound wave travels away from "
                "it. As one compression moves 2 m further from the whistle, "
                "how far does a single particle of air at that point move?",
        "options": [
            {"text": "2 m, since the particle moves with the "
                     "compression", "correct": False,
             "why": "The particle does not travel with the "
                    "compression; it shuffles back and forth a small amount "
                    "near its resting place."},
            {"text": "1 m, half the distance the compression "
                     "travelled", "correct": False,
             "why": "There is no fixed fraction linking a particle's "
                    "own movement to how far the compression has travelled."},
            {"text": "A tiny fraction of a millimetre, far less "
                     "than 2 m", "correct": True},
            {"text": "It cannot move, since it is energy that "
                     "travels in a wave", "correct": False,
             "why": "The particle does move a small amount, to and "
                    "fro; it is just that it does not travel the whole "
                    "distance the compression does."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s12",
        "band": "standard",
        "text": "Two sound waves have the same wavelength, but one "
                "has a bigger amplitude than the other. Which statement "
                "compares them correctly?",
        "options": [
            {"text": "They have compressions the same distance "
                     "apart, but the bigger-amplitude wave has a larger "
                     "pressure change at each one", "correct": True},
            {"text": "The bigger-amplitude wave has its "
                     "compressions closer together", "correct": False,
             "why": "Wavelength, not amplitude, decides the spacing "
                    "of the compressions. Equal wavelengths mean equal "
                    "spacing."},
            {"text": "They must have different wavelengths in this "
                     "case, since a change in one wave's amplitude and its "
                     "wavelength tends to show up together in real "
                     "recordings of an instrument", "correct": False,
             "why": "Amplitude and wavelength are independent "
                    "measurements; either can change without the other."},
            {"text": "There is no way to compare the two waves "
                     "properly without first knowing the frequency that each "
                     "one is being driven at, since that is treated as the "
                     "missing piece of information here", "correct": False,
             "why": "Wavelength and amplitude alone are enough to "
                    "compare the spacing and the size of the pressure "
                    "change."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s13",
        "band": "standard",
        "text": "A sound wave and a water wave both travel across a "
                "room and a pond. Which of these is true of both?",
        "options": [
            {"text": "Both show crests and troughs when drawn", "correct": False,
             "why": "Only the water wave, a transverse wave, shows "
                    "crests and troughs. The sound wave shows compressions "
                    "and rarefactions instead."},
            {"text": "Both carry energy away from their source "
                     "without carrying any material along with them", "correct": True},
            {"text": "Both need the particles to move at right "
                     "angles to the direction of travel", "correct": False,
             "why": "That is only true of the water wave. In the "
                    "sound wave the particles move along the direction of "
                    "travel."},
            {"text": "Both are longitudinal waves", "correct": False,
             "why": "The water wave behaves as a transverse wave; "
                    "only the sound wave is longitudinal."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s14",
        "band": "standard",
        "text": "A sound wave in air has an amplitude much bigger "
                "than a whisper's. Which single feature of the wave pattern "
                "does 'bigger amplitude' directly describe?",
        "options": [
            {"text": "How far apart the compressions are", "correct": False,
             "why": "That distance is the wavelength, a separate "
                    "measurement from amplitude."},
            {"text": "How many compressions pass a point each "
                     "second", "correct": False,
             "why": "That is frequency, again a separate measurement "
                    "from amplitude."},
            {"text": "How fast the wave travels through whatever "
                     "material it happens to be moving through at the time", "correct": False,
             "why": "Speed depends on the material the wave is "
                    "travelling through, not on the wave's amplitude."},
            {"text": "How far each particle is displaced from its "
                     "resting position at a compression or rarefaction", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s15",
        "band": "standard",
        "text": "A sound wave passes a single fixed point in the "
                "air. Over one full wavelength's worth of time, how many "
                "compressions pass that point?",
        "options": [
            {"text": "One", "correct": True},
            {"text": "Two", "correct": False,
             "why": "Two compressions passing marks two full "
                    "wavelengths, not one."},
            {"text": "Half", "correct": False,
             "why": "A compression is a whole event; half of one "
                    "passing does not make sense here."},
            {"text": "It depends on the amplitude", "correct": False,
             "why": "How many compressions pass in one wavelength's "
                    "worth of time is fixed by the definition of wavelength; "
                    "amplitude does not change it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s16",
        "band": "standard",
        "text": "A student says: 'A longitudinal wave has no "
                "amplitude, because there's no hump to measure the height "
                "of.' What is the best reply?",
        "options": [
            {"text": "They are right — longitudinal waves have no "
                     "amplitude, since there is no crest whose height could "
                     "ever be measured on a page", "correct": False,
             "why": "A longitudinal wave has an amplitude too; it is "
                    "measured differently from a transverse wave's."},
            {"text": "They are right, but this is true for quiet "
                     "sounds alone, since a small movement is too small to "
                     "count as a real amplitude", "correct": False,
             "why": "Every longitudinal wave, loud or quiet, has an "
                    "amplitude; it is not zero unless there is no sound at "
                    "all."},
            {"text": "They are wrong — the amplitude is how far "
                     "each particle shifts from its resting place, or "
                     "equally how big the pressure change is", "correct": True},
            {"text": "They are wrong, because a longitudinal wave "
                     "has a hump that cannot be seen", "correct": False,
             "why": "There is no hidden hump. The amplitude is a real "
                    "distance the particles shift and a real change in "
                    "pressure, not a disguised height."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s17",
        "band": "standard",
        "text": "A loudspeaker cone moves forward, pushing the air "
                "in front of it, then moves back past its resting point. Put "
                "these two actions in order with what they create.",
        "options": [
            {"text": "Forward creates a rarefaction, then back "
                     "creates a compression", "correct": False,
             "why": "The order is reversed: moving forward pushes air "
                    "together, making a compression."},
            {"text": "Forward creates a compression, then back "
                     "creates a rarefaction", "correct": True},
            {"text": "Both movements create compressions, one after "
                     "the other", "correct": False,
             "why": "Only the forward movement squeezes the air. The "
                    "backward movement spreads it out instead."},
            {"text": "Neither movement creates anything until the "
                     "cone comes to a complete stop", "correct": False,
             "why": "Each movement of the cone acts on the air "
                    "immediately; nothing waits for the cone to stop."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s18",
        "band": "standard",
        "text": "Which of these correctly compares a compression and "
                "a rarefaction?",
        "options": [
            {"text": "A compression has a higher pressure and a "
                     "lower density than normal", "correct": False,
             "why": "A compression has both a higher pressure and a "
                    "higher density — the particles are squeezed closer "
                    "together, not spread out."},
            {"text": "A rarefaction has a higher density than "
                     "normal, and a compression has a lower density", "correct": False,
             "why": "This reverses the truth: a rarefaction is where "
                    "the density drops, and a compression is where it rises."},
            {"text": "Both have exactly the same pressure and "
                     "density as normal air", "correct": False,
             "why": "Both are defined by a real change from normal — "
                    "one up, one down — not by being unchanged."},
            {"text": "A compression has both a higher pressure and "
                     "a higher density than normal; a rarefaction has both "
                     "lower", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s19",
        "band": "standard",
        "text": "A microphone sits at one fixed point while a steady "
                "note plays. What happens to the air pressure at that exact "
                "point while the sound is passing?",
        "options": [
            {"text": "It rises above normal and stays there for as "
                     "long as the note plays, since compressions keep "
                     "arriving one after another", "correct": False,
             "why": "The rarefactions arrive in between, so the pressure "
                    "drops below normal just as often as it rises above it."},
            {"text": "It holds steady at normal, since the air is only "
                     "shuffling to and fro and is never actually squeezed", "correct": False,
             "why": "The shuffling is exactly what crowds the air at one "
                    "moment and thins it at the next, so the pressure does "
                    "change."},
            {"text": "It rises above normal, falls below normal and "
                     "repeats, as compressions and rarefactions arrive in "
                     "turn", "correct": True},
            {"text": "It falls below normal and stays there, since "
                     "each swing of the source pulls air away from the "
                     "microphone", "correct": False,
             "why": "Each swing of the source pushes air towards the "
                    "microphone as well as pulling it away, so the pressure "
                    "does not simply sit low."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s20",
        "band": "standard",
        "text": "A sound source vibrates and sets up a longitudinal "
                "wave. A student says: 'since the particles don't travel "
                "anywhere, the wave can't be carrying anything anywhere.' "
                "What is wrong with this?",
        "options": [
            {"text": "Nothing — the wave carries nothing from place "
                     "to place", "correct": False,
             "why": "The wave carries energy from place to place, "
                    "even though the particles themselves stay near where "
                    "they started."},
            {"text": "It confuses the particles not travelling with "
                     "the wave not carrying energy — the two are different "
                     "things", "correct": True},
            {"text": "It is wrong because the particles genuinely "
                     "do travel with the wave, all the way from the source "
                     "to wherever the wave is heard", "correct": False,
             "why": "The particles do not travel with the wave; what "
                    "is wrong is treating that as meaning nothing is "
                    "carried."},
            {"text": "It is wrong because sound waves have no "
                     "energy to carry", "correct": False,
             "why": "Sound waves do carry energy — enough, for "
                    "example, to make a microphone diaphragm move."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s21",
        "band": "standard",
        "text": "A sound wave has a wavelength of 68 cm. What is the "
                "distance from a compression to the rarefaction right next "
                "to it?",
        "options": [
            {"text": "68 cm", "correct": False,
             "why": "That is the full wavelength, compression to the "
                    "next compression, not to the nearest rarefaction."},
            {"text": "136 cm", "correct": False,
             "why": "That doubles the wavelength instead of halving "
                    "it."},
            {"text": "34 cm", "correct": True},
            {"text": "17 cm", "correct": False,
             "why": "That is a quarter of the wavelength; the gap to "
                    "the nearest rarefaction is half of it, not a quarter."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s22",
        "band": "standard",
        "text": "A wave diagram is redrawn with every distance "
                "measurement doubled, but nothing else about the wave is "
                "changed. What happens to the spacing between compressions?",
        "options": [
            {"text": "It also doubles, since that spacing is a "
                     "distance on the same diagram", "correct": True},
            {"text": "It stays the same, since it is the amplitude "
                     "that is affected by a change in distance", "correct": False,
             "why": "The compression spacing is itself a distance on "
                    "the diagram, so doubling every distance doubles it too."},
            {"text": "It halves", "correct": False,
             "why": "Doubling every distance cannot halve one "
                    "particular distance on the same diagram."},
            {"text": "It becomes impossible to tell without knowing "
                     "the frequency", "correct": False,
             "why": "The new spacing can be read directly off the "
                    "redrawn diagram; frequency is not needed to double a "
                    "distance."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s23",
        "band": "standard",
        "text": "A sound wave's amplitude is increased while its "
                "wavelength is kept exactly the same. What happens to the "
                "spacing of the compressions?",
        "options": [
            {"text": "They move further apart", "correct": False,
             "why": "Spacing is set by wavelength. With the "
                    "wavelength unchanged, the spacing does not change."},
            {"text": "They move closer together", "correct": False,
             "why": "Amplitude and spacing are different properties; "
                    "changing one does not move the compressions closer."},
            {"text": "They disappear, replaced by one very large "
                     "compression", "correct": False,
             "why": "The wave keeps its usual repeating pattern of "
                    "compressions and rarefactions; a bigger amplitude does "
                    "not merge them into one."},
            {"text": "Their spacing stays exactly the same", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s24",
        "band": "standard",
        "text": "Why can a longitudinal wave and a transverse wave "
                "both be reflected off a wall, even though their particles "
                "move in different directions?",
        "options": [
            {"text": "Because transverse waves are the kind that "
                     "can reflect, and longitudinal waves are absorbed "
                     "instead whenever they meet a hard surface", "correct": False,
             "why": "Both kinds of wave reflect off a suitable "
                    "surface; a sound wave reflecting is what makes an echo."},
            {"text": "Because reflection changes the direction the "
                     "whole pattern travels, not the direction the particles "
                     "inside it move", "correct": True},
            {"text": "Because both waves stop being longitudinal or "
                     "transverse the moment they reflect", "correct": False,
             "why": "A wave keeps its type after reflecting; a "
                    "reflected sound wave is still longitudinal."},
            {"text": "Because the wall converts the particle motion "
                     "into the opposite type before sending the wave back", "correct": False,
             "why": "Nothing converts the particles' direction of "
                    "motion; the wave's type does not change on reflection."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s25",
        "band": "standard",
        "text": "A recording engineer needs to check that a signal "
                "really is a longitudinal sound wave and not a transverse "
                "one. Which feature would settle it?",
        "options": [
            {"text": "Whether the material's particles move along "
                     "the line of travel or across it", "correct": True},
            {"text": "Whether the wave is loud or quiet", "correct": False,
             "why": "Loudness comes from the amplitude, and both "
                    "longitudinal and transverse waves can be loud or quiet."},
            {"text": "Whether the wave has a measurable wavelength "
                     "or not, however that wavelength happens to be defined", "correct": False,
             "why": "Both kinds of wave have a wavelength; having one "
                    "does not tell you which kind it is."},
            {"text": "Whether the wave can be reflected", "correct": False,
             "why": "Both kinds of wave can reflect, so reflecting "
                    "does not distinguish between them."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s26",
        "band": "standard",
        "text": "A guitar string vibrates and sets the surrounding "
                "air into a longitudinal wave. Compare the string's own "
                "motion with the air's motion.",
        "options": [
            {"text": "Both move along the direction the sound "
                     "travels", "correct": False,
             "why": "The string mostly moves at right angles to its "
                    "own length, which is not the direction the sound wave "
                    "in the air travels."},
            {"text": "Neither the string nor the air moves at any "
                     "point; it is the sound alone that travels all the way "
                     "across the room from the guitar to a listener", "correct": False,
             "why": "Both the string and the air genuinely move; a "
                    "wave still needs something moving to carry it."},
            {"text": "The string moves largely across its own "
                     "length, while the air particles it disturbs move along "
                     "the sound's direction of travel", "correct": True},
            {"text": "The string's motion and the air's motion are "
                     "identical in direction, both moving along the exact "
                     "same line that the sound wave itself travels through "
                     "the room", "correct": False,
             "why": "The string's own vibration and the air's "
                    "longitudinal motion are in different directions from "
                    "each other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s27",
        "band": "standard",
        "text": "A wave's compressions are measured 15 cm apart at "
                "one moment, and the whole wave pattern has moved 45 cm to "
                "the right a short time later. How many whole wavelengths "
                "has the pattern moved?",
        "options": [
            {"text": "Two", "correct": False,
             "why": "Two wavelengths would be 30 cm, short of the 45 "
                    "cm given."},
            {"text": "Three", "correct": True},
            {"text": "Four", "correct": False,
             "why": "Four wavelengths would be 60 cm, more than the "
                    "45 cm the pattern actually moved."},
            {"text": "It cannot be found without the amplitude", "correct": False,
             "why": "The number of wavelengths moved comes from "
                    "dividing the distance travelled by the wavelength; "
                    "amplitude plays no part in it."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s28",
        "band": "standard",
        "text": "A speaker plays a note, and a student marks where a "
                "compression is at one instant. A short time later, is that "
                "same compression still in the same place?",
        "options": [
            {"text": "Yes — compressions are fixed points that stay "
                     "in one place", "correct": False,
             "why": "A compression is not fixed in place. The whole "
                    "pattern, including that compression, travels onward."},
            {"text": "No — it has been destroyed and replaced by a "
                     "new one", "correct": False,
             "why": "The same compression persists and moves along; "
                    "it is not destroyed and remade."},
            {"text": "It depends on how loud the note is", "correct": False,
             "why": "Whether a compression moves on is about wave "
                    "motion, not about how loud the note is."},
            {"text": "No — it has moved onward, in the direction "
                     "the wave is travelling", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s29",
        "band": "standard",
        "text": "A tuning fork prong swings from its leftmost point, "
                "through the middle, to its rightmost point, and back again "
                "— one full swing. How many compressions does it push out "
                "into the air during that one full swing?",
        "options": [
            {"text": "One", "correct": True},
            {"text": "Two", "correct": False,
             "why": "One full back-and-forth swing produces one "
                    "compression, and one rarefaction, not two compressions."},
            {"text": "Half", "correct": False,
             "why": "A full swing is a whole cycle, and a whole cycle "
                    "produces one whole compression, not half of one."},
            {"text": "None, until the prong comes to rest", "correct": False,
             "why": "The prong pushes out a compression as it moves, "
                    "well before it ever stops."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-s30",
        "band": "standard",
        "text": "A sound wave has a wavelength of 12 cm. Over a "
                "length of 60 cm of this wave, how many complete wavelengths "
                "fit?",
        "options": [
            {"text": "12", "correct": False,
             "why": "That divides 60 by 5 backwards; dividing the "
                    "length by the wavelength gives the count of complete "
                    "waves."},
            {"text": "5", "correct": True},
            {"text": "48", "correct": False,
             "why": "That subtracts the wavelength from the length "
                    "rather than dividing one by the other."},
            {"text": "720", "correct": False,
             "why": "That multiplies the two values, which does not "
                    "give a count of how many wavelengths fit into the "
                    "length."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · harder ───────────────────────────────────
    {
        "id": "p6-04-h09",
        "band": "harder",
        "text": "A student claims: 'A longitudinal wave has no "
                "crests, so it cannot really have a wavelength at all.' What "
                "is the best evaluation of this claim?",
        "options": [
            {"text": "The claim is wrong: a wavelength can be "
                     "measured from one compression to the next, with no "
                     "crest needed at all", "correct": True},
            {"text": "The claim is correct — the very idea of a "
                     "wavelength was invented specifically to describe the "
                     "spacing of crests in a transverse wave, and transverse "
                     "waves alone", "correct": False,
             "why": "A longitudinal wave has a wavelength too, "
                    "measured from one compression to the next; crests are "
                    "not needed for a wavelength to exist."},
            {"text": "The claim is correct for very high-pitched "
                     "sounds specifically", "correct": False,
             "why": "Pitch makes no difference; every longitudinal "
                    "wave has a measurable wavelength, high-pitched or low."},
            {"text": "The claim is correct, because the very "
                     "definition of a wavelength is written in terms of the "
                     "height reached by a crest on a transverse wave", "correct": False,
             "why": "Wavelength is defined as the distance between "
                    "two repeating points, such as compression to "
                    "compression — no crest height is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h10",
        "band": "harder",
        "text": "A wave diagram marks 6 consecutive compressions, "
                "evenly spaced 30 cm apart from each other. What is the "
                "distance from the first marked compression to the last?",
        "options": [
            {"text": "180 cm", "correct": False,
             "why": "That multiplies the spacing by 6, one gap too "
                    "many — there are only 5 gaps between 6 points."},
            {"text": "150 cm", "correct": True},
            {"text": "210 cm", "correct": False,
             "why": "This overshoots even the 6-gap total; there are "
                    "only 5 gaps between 6 marked points."},
            {"text": "30 cm", "correct": False,
             "why": "That is only the gap between two neighbouring "
                    "compressions, not the span across all six."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h11",
        "band": "harder",
        "text": "A student says: 'Because a sound wave's particles "
                "return to where they started, no energy can have been "
                "transferred.' Evaluate this.",
        "options": [
            {"text": "Correct — if the particles end up back where "
                     "they started, nothing has been transferred", "correct": False,
             "why": "Energy is transferred by the wave itself "
                    "travelling onward, which does not require the particles "
                    "to end up anywhere new."},
            {"text": "Wrong, because the particles do travel onward "
                     "with the wave, all the way from the source to wherever "
                     "it is heard", "correct": False,
             "why": "The particles do not travel onward; what is "
                    "wrong is the idea that this means no energy is "
                    "transferred."},
            {"text": "Correct, but this applies to very "
                     "low-amplitude waves alone, since a bigger wave is what "
                     "really counts as carrying energy", "correct": False,
             "why": "The reasoning is wrong at any amplitude; the "
                    "particles returning to their start is normal for every "
                    "sound wave, loud or quiet."},
            {"text": "Wrong — energy is transferred by the "
                     "travelling pattern of compressions and rarefactions, "
                     "regardless of where the particles finish", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h12",
        "band": "harder",
        "text": "Two identical loudspeakers play the same note, but "
                "speaker B is driven with a bigger amplitude than speaker A. "
                "A student says: 'since both send out the same type of wave, "
                "they must be transferring the same amount of energy.' "
                "Evaluate.",
        "options": [
            {"text": "Agree — wave type alone decides how much "
                     "energy is carried", "correct": False,
             "why": "Wave type says which direction the particles "
                    "move, not how far they move or how much the air is "
                    "squeezed."},
            {"text": "Agree, because energy transfer depends on the "
                     "note being played and nothing about how far the cone "
                     "itself is driven back and forth", "correct": False,
             "why": "The note being the same fixes the frequency, but "
                    "the amplitude has been stated to differ, and that also "
                    "affects the energy carried."},
            {"text": "Disagree — a bigger amplitude generally means "
                     "more energy is being transferred, even though both "
                     "waves are the same type", "correct": True},
            {"text": "Disagree, but simply because speaker B must "
                     "be a physically bigger speaker than speaker A", "correct": False,
             "why": "The physical size of the equipment is not what "
                    "is being compared — it is the amplitude each one is "
                    "driven at."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h13",
        "band": "harder",
        "text": "A sound wave has a wavelength of 24 cm. A "
                "microphone sits at a fixed point. In the time it takes for "
                "3 full wavelengths to pass the microphone, how many "
                "compressions pass it?",
        "options": [
            {"text": "3", "correct": True},
            {"text": "6", "correct": False,
             "why": "Doubling the wavelength count overcounts; each "
                    "wavelength brings exactly one compression, not two."},
            {"text": "1", "correct": False,
             "why": "Undercounting to one ignores that three full "
                    "wavelengths bring three separate compressions."},
            {"text": "It cannot be found without knowing the "
                     "frequency", "correct": False,
             "why": "The number of compressions in a stated number of "
                    "wavelengths is fixed by definition — one compression "
                    "per wavelength — no frequency is needed."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h14",
        "band": "harder",
        "text": "In a sports stadium 'Mexican wave', each spectator "
                "stands briefly then sits again, in sequence round the "
                "stadium, and the wave of standing travels around the "
                "stands. Is this best modelled as transverse or "
                "longitudinal, and why?",
        "options": [
            {"text": "Longitudinal, because each spectator finishes "
                     "back in exactly the seat they started in, in the same "
                     "way a particle of air in a sound wave ends up back at "
                     "its own resting place", "correct": False,
             "why": "Returning to where you started happens in both "
                    "kinds of wave; it does not by itself decide which one "
                    "this is."},
            {"text": "Neither, because a stadium wave made of "
                     "people cannot properly be modelled as a physical wave "
                     "in the way a slinky or a sound wave in air can be", "correct": False,
             "why": "It is a widely used example of a transverse "
                    "wave: something disturbs, the disturbance passes along, "
                    "and the material — here, the spectators — returns to "
                    "where it started."},
            {"text": "Longitudinal, because the spectators are "
                     "squeezed together as the wave passes", "correct": False,
             "why": "Nobody is squeezed together; each spectator "
                    "simply stands and sits in their own seat."},
            {"text": "Transverse, because each spectator moves up "
                     "and down, at right angles to the sideways direction "
                     "the wave itself travels round the stadium", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h15",
        "band": "harder",
        "text": "A seismometer shows the ground moving at right "
                "angles to the direction a wave from a distant earthquake is "
                "travelling. What type of wave must this be?",
        "options": [
            {"text": "A P wave, because P waves are the particular "
                     "type of earthquake wave that is responsible for "
                     "shaking buildings during a large earthquake", "correct": False,
             "why": "P waves are longitudinal — their ground motion "
                    "is along the direction of travel, not at right angles "
                    "to it."},
            {"text": "Neither — earthquake waves do not have a "
                     "fixed type", "correct": False,
             "why": "Earthquake waves do have a fixed type: P waves "
                    "are longitudinal and S waves are transverse."},
            {"text": "An S wave, because its ground motion is "
                     "transverse — at right angles to its direction of "
                     "travel", "correct": True},
            {"text": "A P wave, because P waves are the particular "
                     "kind of earthquake wave that arrives at a distant "
                     "seismometer well before any other kind does", "correct": False,
             "why": "Arriving first is true of P waves, but it has "
                    "nothing to do with the direction the ground moves, "
                    "which is what this question is about."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h16",
        "band": "harder",
        "text": "A phone speaker and a subwoofer both make "
                "longitudinal sound waves in air. A student argues that "
                "because both are longitudinal, they must squeeze the air by "
                "exactly the same amount. Evaluate.",
        "options": [
            {"text": "Agree — being the same type of wave, both "
                     "longitudinal, fixes the amount of squeezing each one "
                     "produces in the air around it, regardless of how each "
                     "device is driven", "correct": False,
             "why": "Wave type says which direction the particles "
                    "move, not how far they move or how much the air is "
                    "squeezed."},
            {"text": "Disagree — the amount of squeezing (the "
                     "amplitude) can differ between two longitudinal waves; "
                     "the type only fixes the direction of motion", "correct": True},
            {"text": "Agree, because a longitudinal wave squeezes "
                     "air by a fixed, standard amount", "correct": False,
             "why": "There is no fixed standard amount; a "
                    "longitudinal wave's amplitude can be anything from very "
                    "small to very large."},
            {"text": "Disagree, but simply because a subwoofer is a "
                     "noticeably bigger and heavier piece of equipment than "
                     "a small phone speaker could ever be built as", "correct": False,
             "why": "The physical size of the equipment is not the "
                    "reason; it is the amplitude of the wave each one "
                    "produces that can differ."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h17",
        "band": "harder",
        "text": "A student claims: 'If you shorten a sound wave's "
                "wavelength enough, it eventually becomes a transverse wave "
                "instead.' Evaluate this claim.",
        "options": [
            {"text": "Correct — shortening a wavelength enough "
                     "eventually makes the particles start moving across the "
                     "direction of travel instead of along it, turning the "
                     "wave transverse", "correct": False,
             "why": "Wavelength has nothing to do with which type a "
                    "wave is; shortening it does not change the direction "
                    "the particles move in."},
            {"text": "It cannot properly be evaluated without first "
                     "measuring the exact frequency the wave is being driven "
                     "at, since frequency is the missing piece of "
                     "information here", "correct": False,
             "why": "No frequency measurement is needed; the claim is "
                    "wrong, because a wave's type is not linked to its "
                    "wavelength."},
            {"text": "Correct, but this applies to very loud sounds "
                     "alone", "correct": False,
             "why": "Loudness (amplitude) is unrelated to this too; "
                    "type is decided by particle-motion direction, not by "
                    "wavelength or amplitude."},
            {"text": "Wrong — a wave's type is set by how the "
                     "particles move relative to the direction of travel, "
                     "and is not changed by the wavelength getting shorter "
                     "or longer", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h18",
        "band": "harder",
        "text": "A student says: 'If a wave shows no crests when "
                "drawn, it must have zero energy.' Evaluate this claim using "
                "what you know about longitudinal waves.",
        "options": [
            {"text": "The claim is correct, since a wave's whole "
                     "store of energy has to live somewhere inside the "
                     "height of a crest, and a longitudinal wave has no "
                     "crest to hold it in", "correct": False,
             "why": "Energy in a wave does not need a crest to be "
                    "'stored in'; a longitudinal wave carries energy in its "
                    "pattern of compressions and rarefactions instead."},
            {"text": "The claim is wrong: a longitudinal wave shows "
                     "no crests and still carries energy, for instance "
                     "enough to move a microphone diaphragm", "correct": True},
            {"text": "The claim is correct just when the wave is "
                     "travelling through a solid", "correct": False,
             "why": "The material does not change this; a "
                    "longitudinal wave with no crests carries energy in a "
                    "solid, a liquid or a gas."},
            {"text": "The claim cannot properly be judged without "
                     "first knowing the exact speed the wave happens to be "
                     "travelling at through whatever material it is moving "
                     "through", "correct": False,
             "why": "The wave's speed is not needed to judge this; "
                    "the claim is wrong regardless of speed, because absence "
                    "of a crest does not mean absence of energy."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h19",
        "band": "harder",
        "text": "A sound source vibrates at a steady rate, and the "
                "wave it produces travels into a wall and reflects straight "
                "back. Which of these is true about the reflected wave?",
        "options": [
            {"text": "It has become a transverse wave, since "
                     "reflection swaps the wave type", "correct": False,
             "why": "Reflection does not change a wave's type; sound "
                    "reflecting off a wall is still longitudinal."},
            {"text": "It keeps the same direction of travel as the "
                     "original wave, just reflected in volume", "correct": False,
             "why": "A reflected wave travels in a different "
                    "direction from the original; only its type stays the "
                    "same, not its direction."},
            {"text": "It has stopped being a wave, and is now just "
                     "still air", "correct": False,
             "why": "The reflected sound is still a genuine "
                    "travelling wave — it is what you hear back as an echo."},
            {"text": "It is still longitudinal, with the particles "
                     "still moving along the (now-reversed) direction of "
                     "travel", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h20",
        "band": "harder",
        "text": "A diagram marks 4 consecutive compressions, 22 cm "
                "apart from each other. What is the total span from the "
                "first to the last?",
        "options": [
            {"text": "88 cm", "correct": False,
             "why": "That is one gap too many for 4 marked points, "
                    "which have only 3 gaps between them."},
            {"text": "22 cm", "correct": False,
             "why": "That is only a single gap, not the span across "
                    "all four points."},
            {"text": "66 cm", "correct": True},
            {"text": "44 cm", "correct": False,
             "why": "That covers only 2 gaps, one short of the 3 gaps "
                    "between 4 points."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h21",
        "band": "harder",
        "text": "A student says: 'A rarefaction has less air in it "
                "than a compression, so a rarefaction weighs less.' What is "
                "the most accurate response?",
        "options": [
            {"text": "They are right: at that instant, a "
                     "rarefaction genuinely has fewer particles, and so a "
                     "lower density, in that region than a compression does", "correct": True},
            {"text": "They are wrong: a rarefaction and a "
                     "compression contain the same total amount of air, "
                     "because nothing has been added or removed from the "
                     "gas, just rearranged into a different pattern of "
                     "spacing", "correct": False,
             "why": "The whole point of a rarefaction is that the air "
                    "has spread out, leaving less of it in that particular "
                    "region at that instant."},
            {"text": "They are wrong: a rarefaction contains "
                     "noticeably more air squeezed into that same region "
                     "than a compression does, which is the reverse of how "
                     "the two are properly defined", "correct": False,
             "why": "That reverses the definitions — a compression is "
                    "the crowded region and a rarefaction is the spread-out "
                    "one."},
            {"text": "They are wrong: 'weighs less' has no meaning "
                     "for a moving gas", "correct": False,
             "why": "A smaller amount of air in a region does have a "
                    "smaller mass at that moment, so the idea is meaningful, "
                    "even though the effect is tiny and constantly shifting."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h22",
        "band": "harder",
        "text": "A trumpet and a whisper both make longitudinal "
                "sound waves of a similar shape, but the trumpet's amplitude "
                "is far bigger. A student argues: 'since the trumpet's wave "
                "has a bigger amplitude, it must also have a longer "
                "wavelength.' Evaluate.",
        "options": [
            {"text": "Correct — a bigger amplitude needs more room "
                     "for the particles to swing through, and the way to fit "
                     "that extra swing in is to spread the compressions "
                     "further apart, giving a longer wavelength", "correct": False,
             "why": "Amplitude and wavelength are independent "
                    "measurements; a big-amplitude wave can have any "
                    "wavelength."},
            {"text": "Wrong — amplitude, how far the particles "
                     "shift, and wavelength, the spacing of the pattern, are "
                     "independent of each other", "correct": True},
            {"text": "Correct, but this holds when comparing a "
                     "trumpet with a whisper specifically", "correct": False,
             "why": "The independence of amplitude and wavelength "
                    "holds generally, not only for this particular "
                    "comparison."},
            {"text": "It cannot properly be evaluated without first "
                     "knowing exactly which material the sound wave happens "
                     "to be travelling through at the time", "correct": False,
             "why": "The material affects the speed of the wave, not "
                    "whether amplitude and wavelength are linked to each "
                    "other."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h23",
        "band": "harder",
        "text": "Wave A has a bigger pressure change at its "
                "compressions than Wave B. A student concludes Wave A must "
                "have more compressions passing a point each second than "
                "Wave B. Evaluate.",
        "options": [
            {"text": "Correct — a bigger pressure change means the "
                     "source is pushing harder each time, and pushing harder "
                     "is exactly what makes it complete more compressions in "
                     "every second that passes", "correct": False,
             "why": "How big the pressure change is (which is about "
                    "amplitude) is separate from how often compressions "
                    "occur, a different property of the wave."},
            {"text": "It cannot be evaluated properly without first "
                     "knowing the exact wavelength of each of the two waves "
                     "being compared", "correct": False,
             "why": "Wavelength is not needed to see the flaw — the "
                    "claim wrongly links two separate properties of the wave "
                    "regardless of its wavelength."},
            {"text": "Correct, but this holds just when both waves "
                     "are in the same material", "correct": False,
             "why": "Being in the same material does not create this "
                    "link either; amplitude and how often compressions "
                    "arrive remain separate properties."},
            {"text": "Wrong — the size of the pressure change tells "
                     "you about amplitude, not about how often compressions "
                     "arrive", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h24",
        "band": "harder",
        "text": "One slinky is driven two ways in turn: sideways "
                "across its length, and back and forth along it. Both drives "
                "use the same 60 mm movement and the same 300 mm spacing "
                "between repeats. Why deliberately keep those two numbers "
                "identical between the two drives?",
        "options": [
            {"text": "So that only the direction of the movement "
                     "differs between the two drives, letting a student "
                     "compare the two wave types fairly without any size "
                     "difference getting in the way", "correct": True},
            {"text": "Because 60 mm and 300 mm are simply the two "
                     "particular values a real slinky happens to be driven "
                     "at, and nothing about a slinky forces those two "
                     "numbers to be used", "correct": False,
             "why": "These are simply the values chosen for this "
                    "demonstration; a real slinky is not restricted to these "
                    "numbers."},
            {"text": "So that the longitudinal drive ends up faster "
                     "than the transverse one", "correct": False,
             "why": "Matching the size of the movement does not make "
                    "one drive faster; speed is not what is being compared "
                    "here."},
            {"text": "Because a slinky, like any piece of apparatus, "
                     "can be driven at one single fixed amplitude and one "
                     "single fixed wavelength at any one time, and not more "
                     "than one of each at once", "correct": False,
             "why": "A slinky can be driven at many different "
                    "amplitudes and wavelengths; both are simply held the "
                    "same across the two drives for a fair comparison."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h25",
        "band": "harder",
        "text": "A microphone diaphragm moves back and forth as a "
                "sound wave from a nearby speaker arrives. If the "
                "loudspeaker were replaced with one producing exactly the "
                "same wave but travelling in the opposite direction, how "
                "would the diaphragm's motion differ?",
        "options": [
            {"text": "The diaphragm would stay completely still in "
                     "that case, since a wave has to arrive from one "
                     "particular direction before the diaphragm can properly "
                     "respond to the pressure changes reaching it", "correct": False,
             "why": "A wave arriving from either direction still "
                    "pushes the diaphragm to and fro; the direction of "
                    "arrival does not switch the motion off."},
            {"text": "The diaphragm's motion would not be "
                     "noticeably different, since it responds to the "
                     "pressure changes arriving at it, whichever direction "
                     "they came from", "correct": True},
            {"text": "The diaphragm would move sideways instead of "
                     "back and forth, tracing out a completely different "
                     "kind of motion from the one it shows for a wave "
                     "arriving from the front", "correct": False,
             "why": "The diaphragm always moves back and forth along "
                    "the direction the sound reaches it, from whichever "
                    "direction that is."},
            {"text": "The diaphragm would stop working, because "
                     "sound can travel through air in one single direction", "correct": False,
             "why": "Sound can travel in any direction through air; "
                    "there is nothing special about one direction over "
                    "another."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h26",
        "band": "harder",
        "text": "A sound wave has an amplitude twice as big as "
                "another sound wave of the same wavelength. A student says "
                "the bigger-amplitude wave must have compressions twice as "
                "far apart. Evaluate.",
        "options": [
            {"text": "Correct — bigger amplitude always pushes the "
                     "particles further apart along the slinky, which "
                     "doubles the spacing between one compression and the "
                     "next", "correct": False,
             "why": "Compression spacing is the wavelength, which the "
                    "question states is the same for both waves; amplitude "
                    "changing does not alter it."},
            {"text": "It cannot be judged without knowing which "
                     "material the waves are travelling through", "correct": False,
             "why": "The material would affect the speed of the "
                    "waves, not whether their compression spacing depends on "
                    "amplitude rather than wavelength."},
            {"text": "Correct, but this is true simply because "
                     "bigger waves carry more energy", "correct": False,
             "why": "How much energy a wave carries is not what is "
                    "being asked about; the claim is about spacing, which is "
                    "fixed by wavelength, not amplitude."},
            {"text": "Wrong — the spacing of the compressions is "
                     "set by the wavelength, and the question states both "
                     "waves share the same wavelength, so the spacing must "
                     "be the same", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h27",
        "band": "harder",
        "text": "A sound wave's compressions are spaced 0.75 m "
                "apart. What is this spacing in centimetres?",
        "options": [
            {"text": "0.75 cm", "correct": False,
             "why": "That keeps the same number instead of "
                    "converting; a metre is 100 times a centimetre."},
            {"text": "7.5 cm", "correct": False,
             "why": "That multiplies by only 10, not the 100 needed "
                    "to convert metres to centimetres."},
            {"text": "75 cm", "correct": True},
            {"text": "750 cm", "correct": False,
             "why": "That multiplies by 1000, which converts metres "
                    "to millimetres, not to centimetres."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h28",
        "band": "harder",
        "text": "A longitudinal wave and a transverse wave both "
                "travel at the same speed through the same length of "
                "material. A student says: 'since they arrive at the far end "
                "at the same time, they must be exactly the same type of "
                "wave.' Evaluate.",
        "options": [
            {"text": "Correct — arriving at the far end at exactly "
                     "the same time proves beyond doubt that the two waves "
                     "must be moving their particles in the same direction", "correct": False,
             "why": "Arrival time depends on speed and distance, not "
                    "on whether the particles move along or across the line "
                    "of travel; two different types can share a speed."},
            {"text": "Wrong — two waves can travel at the same "
                     "speed over the same distance and arrive together while "
                     "still being different types, since speed does not "
                     "decide type", "correct": True},
            {"text": "Correct, but this holds just when the "
                     "material is a solid", "correct": False,
             "why": "The material being a solid does not create this "
                    "link either; speed and type remain unconnected in every "
                    "material."},
            {"text": "It cannot be judged, since two different wave "
                     "types cannot travel at the same speed", "correct": False,
             "why": "There is no such rule; different types of wave "
                    "can genuinely travel at equal speeds through the same "
                    "material."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h29",
        "band": "harder",
        "text": "A diagram shows 3 evenly spaced compressions, "
                "marked from left to right, with nothing shown before the "
                "first or after the last. How many complete wavelengths are "
                "shown between the marked compressions?",
        "options": [
            {"text": "3", "correct": False,
             "why": "Counting the compressions themselves gives 3, "
                    "but the complete wavelengths lie in the gaps between "
                    "them, and 3 points have only 2 gaps."},
            {"text": "1", "correct": False,
             "why": "That undercounts; there are 2 gaps between 3 "
                    "evenly spaced points, not 1."},
            {"text": "2", "correct": True},
            {"text": "4", "correct": False,
             "why": "That overcounts; 3 points give only 2 gaps "
                    "between them, not 4."},
        ],
        "figure": None,
    },
    {
        "id": "p6-04-h30",
        "band": "harder",
        "text": "A sound wave's compressions are measured 40 cm "
                "apart in a length of 2.0 m of the wave. How many complete "
                "wavelengths fit into that 2.0 m length?",
        "options": [
            {"text": "5", "correct": True},
            {"text": "0.05", "correct": False,
             "why": "That divides 2.0, left in metres and not "
                    "converted, by 40, mixing metres with centimetres."},
            {"text": "50", "correct": False,
             "why": "That divides 200 by 4 instead of by 40 — a "
                    "slipped decimal point."},
            {"text": "20", "correct": False,
             "why": "That divides 200 by 10 rather than by the actual "
                    "wavelength of 40 cm."},
        ],
        "figure": None,
    },
]
