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
]
