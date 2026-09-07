"""Physics · Waves — wave types, sound, detection, wave properties, EM spectrum, refraction.

Part A of the `waves` topic: the first six subtopics of AQA 8463 §6.6 —
`transverse-longitudinal-waves`, `sound-waves-hearing`,
`waves-detection-exploration`, `properties-of-waves`, `types-of-em-waves` and
`properties-em-waves-1`. Part B (`waves__b.py`) carries the remaining six.

The distractors are built from the misconceptions the briefs declare and the
ones a physics teacher meets every year: that a wave carries the medium
forward with it; that amplitude runs crest-to-trough; that frequency and
period are the same thing; that sound and light behave alike when they enter a
denser material (sound speeds up, light slows down); that the EM spectrum runs
in some other order; that a sonar or ultrasound time is a one-way time; and
that S-waves are stopped by distance rather than by liquid.

Two subtopics here are TRIPLE + HIGHER (`sound-waves-hearing`,
`waves-detection-exploration`) and four are BASE. The four BASE subtopics are
deliberately free of Higher-only material: `properties-em-waves-1` carries an
HT extension on total internal reflection and the critical angle in its lesson
prose, and none of it appears below, because a Foundation Combined class sits
these questions.
"""

TOPIC = "waves"
SUBJECT = "physics"

QUESTIONS = [
    # ── transverse-longitudinal-waves ───────────────────────────────────
    # BASE (foundation, not triple). Spec 6.6.1.1.
    {
        "id": "ks4-transverse-longitudinal-waves-e01",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what all waves transfer from one place to another.",
        "options": [
            "Energy, without transferring matter",
            "Matter, without transferring any energy",
            "Energy and matter together, because the medium moves forward "
            "with the wave",
            "Matter when the wave is longitudinal, and energy when it is "
            "transverse",
        ],
        "correct_index": 0,
        "why": "A wave transfers energy from a source to an absorber; the "
               "particles of the medium oscillate about fixed positions and "
               "are not carried along.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-e02",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A cork floats on the surface of a pond as ripples travel "
                "past it. Describe the motion of the cork.",
        "options": [
            "It travels forward with the ripples towards the far bank",
            "It stays completely still, because water waves are transverse",
            "It bobs up and down about one position without moving forward",
            "It slides back and forth horizontally in the direction the "
            "ripples travel",
        ],
        "correct_index": 2,
        "why": "The ripple carries energy across the pond, but each part of "
               "the water surface only oscillates up and down about its "
               "undisturbed position.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-e03",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Identify which of the following is a transverse wave.",
        "options": [
            "Sound travelling through the air in a room",
            "Ripples on the surface of water",
            "Ultrasound travelling through soft tissue",
            "A compression pulse sent along a stretched slinky spring",
        ],
        "correct_index": 1,
        "why": "In a water ripple the surface moves up and down while the "
               "wave travels horizontally, so the oscillation is "
               "perpendicular to the direction of travel.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-e04",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name given to the regions of a longitudinal wave "
                "where the particles are pushed closest together.",
        "options": [
            "Crests",
            "Rarefactions",
            "Troughs",
            "Compressions",
        ],
        "correct_index": 3,
        "why": "Compressions are the high-pressure regions where particles "
               "are bunched together; rarefactions are the low-pressure "
               "regions where they are pulled apart.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-s01",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student stretches a slinky spring along a bench and moves "
                "one end sharply from side to side, at right angles to the "
                "spring. Describe the wave that travels along the spring.",
        "options": [
            "A longitudinal wave, because the energy travels along the "
            "spring",
            "A transverse wave, because the coils oscillate at right angles "
            "to the direction the wave travels",
            "A longitudinal wave, because compressions form where the coils "
            "bunch together and rarefactions where they spread apart",
            "A transverse wave, because the coils travel along the spring "
            "with the wave",
        ],
        "correct_index": 1,
        "why": "The wave is transverse because the coils are displaced "
               "perpendicular to the direction in which the energy is "
               "transferred, and they stay where they are.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-s02",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A loudspeaker cone vibrates back and forth and produces a "
                "sound wave in the air. Explain how the sound reaches a "
                "listener on the far side of the room.",
        "options": [
            "The cone pushes a stream of air molecules across the room and "
            "into the listener's ear",
            "The cone makes the air molecules oscillate at right angles to "
            "the direction in which the sound travels, in the way a rope "
            "carries a wave",
            "The cone releases sound particles, which spread out through the "
            "room in every direction",
            "The cone pushes air molecules together and apart, and this "
            "pattern of compressions and rarefactions travels outwards",
        ],
        "correct_index": 3,
        "why": "Sound is longitudinal: the pattern of compressions and "
               "rarefactions travels across the room while each air molecule "
               "only vibrates back and forth about its own position.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-s03",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sea waves gradually erode a cliff over many years. Explain "
                "what the waves deliver to the rock.",
        "options": [
            "Energy, transferred to the rock without the water itself "
            "travelling in from the open sea",
            "Water, which is carried the whole way from the open ocean and "
            "piles up against the base of the cliff",
            "Matter and energy in equal shares, because the water and the "
            "wave pattern move forward together",
            "Force but not energy, because a wave can push on a cliff "
            "without transferring anything to it",
        ],
        "correct_index": 0,
        "why": "The wave transfers energy to the cliff; the water oscillates "
               "in place, which is why a floating object out at sea is not "
               "carried to the shore.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-s04",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A transverse wave and a longitudinal wave both travel along "
                "the same steel rail. Compare how the steel is displaced by "
                "each of them.",
        "options": [
            "Both produce compressions and rarefactions, but only the "
            "transverse wave also has crests",
            "Both displace the steel along the rail, and they differ only in "
            "the speed at which they travel",
            "The transverse wave displaces the steel across the rail; the "
            "longitudinal wave displaces it along the rail",
            "The transverse wave transfers energy along the rail while the "
            "longitudinal wave transfers matter",
        ],
        "correct_index": 2,
        "why": "The two wave types are defined by the direction of the "
               "oscillation relative to the direction of travel: "
               "perpendicular for transverse, parallel for longitudinal.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-h01",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Sound must carry air from a singer to my "
                "ear, because I can feel the air moving when someone sings "
                "close to my face.' Identify the error in this reasoning.",
        "options": [
            "There is no error: sound does carry air forward, which is why a "
            "draught can be felt",
            "The error is calling sound a wave at all, since a sung note is "
            "a stream of particles rather than a wave",
            "The air molecules only oscillate about fixed positions; the "
            "draught felt is the singer's breath, not the sound wave",
            "The error is that sound is transverse, so the air moves up and "
            "down rather than towards the listener",
        ],
        "correct_index": 2,
        "why": "A longitudinal wave passes a disturbance from particle to "
               "particle without any net movement of the medium, so no air "
               "is transported from the singer to the ear.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-h02",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a longitudinal wave cannot be described using "
                "crests and troughs.",
        "options": [
            "The oscillation is along the direction of travel, so the wave "
            "has regions of high and low pressure instead of points of "
            "maximum upward and downward displacement",
            "Crests and troughs describe only those waves that are able to "
            "travel through a vacuum, such as light",
            "A longitudinal wave has no amplitude at all, and so there is no "
            "maximum displacement anywhere along its length that could be "
            "marked on a diagram as either a crest or a trough",
            "Crests and troughs are used only for waves the human eye can "
            "actually see, such as ripples on water",
        ],
        "correct_index": 0,
        "why": "A crest is a maximum displacement perpendicular to the "
               "direction of travel, and a longitudinal wave has no such "
               "displacement — it has compressions and rarefactions instead.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-h03",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wave machine at one end of a swimming pool makes a line of "
                "floats bob up and down. The floats nearest the machine start "
                "moving before those further away. Explain what this shows.",
        "options": [
            "The floats are being pushed along the pool by water that is "
            "travelling towards the far end",
            "The wave must be longitudinal, because the disturbance reaches "
            "each float in turn rather than all at once",
            "The wave slows down as it crosses the pool, which is why the "
            "furthest floats start moving last",
            "Energy is being transferred along the pool, while each float "
            "only oscillates about its own position",
        ],
        "correct_index": 3,
        "why": "The delay shows the disturbance travelling along the pool at "
               "a finite speed; each float stays where it is, so what moves "
               "along the pool is energy, not water.",
    },
    {
        "id": "ks4-transverse-longitudinal-waves-h04",
        "subtopic_slug": "transverse-longitudinal-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student claims that because light is a transverse wave, it "
                "must make the air oscillate up and down as it crosses a "
                "room. Evaluate this claim.",
        "options": [
            "The claim is correct: light makes the air particles oscillate "
            "at right angles to its own direction of travel",
            "The claim is wrong: in light it is electric and magnetic fields "
            "that oscillate, not the particles of a medium",
            "The claim is wrong: light is longitudinal, so any oscillation "
            "would be along its direction of travel",
            "The claim is right in air but wrong in a vacuum, where light "
            "becomes longitudinal instead",
        ],
        "correct_index": 1,
        "why": "Light is transverse because its electric and magnetic fields "
               "oscillate perpendicular to its direction of travel — which "
               "is also why it needs no medium at all.",
    },

    # ── sound-waves-hearing ─────────────────────────────────────────────
    # TRIPLE ONLY, higher tier. Spec 6.6.1.4 (HT only, physics only).
    {
        "id": "ks4-sound-waves-hearing-e01",
        "subtopic_slug": "sound-waves-hearing",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the approximate range of frequencies that a healthy "
                "young person can hear.",
        "options": [
            "2 Hz to 2000 Hz",
            "20 Hz to 20 000 Hz",
            "20 Hz to 2000 Hz",
            "200 Hz to 200 000 Hz",
        ],
        "correct_index": 1,
        "why": "Human hearing runs from about 20 Hz up to about 20 kHz; "
               "below that is infrasound and above it is ultrasound.",
    },
    {
        "id": "ks4-sound-waves-hearing-e02",
        "subtopic_slug": "sound-waves-hearing",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "A large earthquake produces sound waves of frequency 15 Hz. "
                "State the name given to sound of this frequency.",
        "options": [
            "Ultrasound",
            "Audible sound",
            "Supersonic sound",
            "Infrasound",
        ],
        "correct_index": 3,
        "why": "Infrasound is sound below about 20 Hz, which is below the "
               "lower limit of human hearing.",
    },
    {
        "id": "ks4-sound-waves-hearing-e03",
        "subtopic_slug": "sound-waves-hearing",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which property of a sound wave determines how loud the "
                "sound is.",
        "options": [
            "The amplitude of the wave",
            "The frequency of the wave",
            "The wavelength of the wave",
            "The speed of the wave",
        ],
        "correct_index": 0,
        "why": "Loudness depends on amplitude — a larger amplitude carries "
               "more energy; frequency sets the pitch instead.",
    },
    {
        "id": "ks4-sound-waves-hearing-e04",
        "subtopic_slug": "sound-waves-hearing",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State the approximate speed of sound in air at room "
                "temperature.",
        "options": [
            "34 m/s",
            "1500 m/s",
            "340 m/s",
            "3 × 10⁸ m/s",
        ],
        "correct_index": 2,
        "why": "Sound travels at about 340 m/s in air; 1500 m/s is its speed "
               "in water and 3 × 10⁸ m/s is the speed of light in a vacuum.",
    },
    {
        "id": "ks4-sound-waves-hearing-s01",
        "subtopic_slug": "sound-waves-hearing",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A dog whistle produces a sound of frequency 30 kHz. Explain "
                "why a dog reacts to it but a person standing beside the dog "
                "hears nothing.",
        "options": [
            "30 kHz lies below the human hearing range but within the range "
            "a dog can hear",
            "The whistle is simply too quiet for a person, while a dog's "
            "ears respond to much quieter sounds",
            "30 kHz is above the upper limit of human hearing, about 20 kHz, "
            "but is within the range a dog can hear",
            "The whistle produces infrasound, which only animals with large "
            "ears are able to detect",
        ],
        "correct_index": 2,
        "why": "30 kHz is ultrasound — above the roughly 20 kHz upper limit "
               "of human hearing — but dogs can hear well beyond that limit.",
    },
    {
        "id": "ks4-sound-waves-hearing-s02",
        "subtopic_slug": "sound-waves-hearing",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A sound wave passes from air into a steel rail. Describe "
                "what happens to the speed of the sound, and explain why.",
        "options": [
            "It increases, because the particles in steel are much closer "
            "together and pass the vibration on more quickly",
            "It decreases, because steel is denser and so resists the "
            "vibration of its particles more strongly",
            "It stays the same, because the speed of a wave is fixed by its "
            "frequency and nothing else",
            "It decreases, in the same way that light slows down when it "
            "enters a denser material such as glass",
        ],
        "correct_index": 0,
        "why": "Sound travels fastest where particles are closest together, "
               "so solid > liquid > gas — the opposite of the pattern for "
               "electromagnetic waves.",
    },
    {
        "id": "ks4-sound-waves-hearing-s03",
        "subtopic_slug": "sound-waves-hearing",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A fishing boat's echo sounder detects a shoal of fish 75 m "
                "directly below it. The speed of sound in the water is "
                "1500 m/s. Calculate the time between sending the pulse and "
                "receiving the echo.",
        "options": [
            "0.050 s",
            "20 s",
            "0.20 s",
            "0.10 s",
        ],
        "correct_index": 3,
        "why": "The pulse covers 2 × 75 m = 150 m in total, so "
               "t = 150 ÷ 1500 = 0.10 s.",
    },
    {
        "id": "ks4-sound-waves-hearing-s04",
        "subtopic_slug": "sound-waves-hearing",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "A student stands 40 m from a large flat wall and claps once. "
                "The speed of sound in air is 340 m/s. Calculate the time "
                "between the clap and the echo being heard.",
        "options": [
            "0.12 s",
            "0.24 s",
            "0.47 s",
            "4.3 s",
        ],
        "correct_index": 1,
        "why": "The sound travels 40 m to the wall and 40 m back, so "
               "t = 80 ÷ 340 = 0.24 s.",
    },
    {
        "id": "ks4-sound-waves-hearing-h01",
        "subtopic_slug": "sound-waves-hearing",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "An ultrasound pulse is sent into a patient, reflects from a "
                "boundary between two tissues, and returns 60 microseconds "
                "(60 × 10⁻⁶ s) later. The speed of ultrasound in the tissue "
                "is 1540 m/s. Calculate the depth of the boundary.",
        "options": [
            "0.046 m",
            "0.092 m",
            "0.023 m",
            "46 m",
        ],
        "correct_index": 0,
        "why": "d = v × t ÷ 2 = 1540 × 60 × 10⁻⁶ ÷ 2 = 0.046 m, once the "
               "time is converted from microseconds into seconds.",
    },
    {
        "id": "ks4-sound-waves-hearing-h02",
        "subtopic_slug": "sound-waves-hearing",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A ship sends a sonar pulse straight down and the echo from "
                "the seabed returns after 0.16 s. At a second point the echo "
                "returns after 0.20 s. The speed of sound in seawater is "
                "1500 m/s. Calculate the difference in depth between the two "
                "points.",
        "options": [
            "60 m",
            "30 m",
            "15 m",
            "270 m",
        ],
        "correct_index": 1,
        "why": "The depths are 1500 × 0.16 ÷ 2 = 120 m and "
               "1500 × 0.20 ÷ 2 = 150 m, a difference of 30 m.",
    },
    {
        "id": "ks4-sound-waves-hearing-h03",
        "subtopic_slug": "sound-waves-hearing",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why an ultrasound scan shows the boundary between "
                "two different soft tissues clearly, while an X-ray image of "
                "the same region shows almost no detail.",
        "options": [
            "Ultrasound has a much shorter wavelength than X-rays do, so it is "
            "able to resolve far finer detail in the soft tissues of the "
            "body than an X-ray image ever can",
            "Ultrasound is absorbed strongly by soft tissue, while X-rays "
            "pass through soft tissue completely unchanged",
            "Ultrasound is partly reflected at a boundary between tissues of "
            "different density, whereas X-rays are absorbed almost equally "
            "by both soft tissues",
            "X-rays are ionising, and ionising radiation is unable to form "
            "an image of living tissue at all",
        ],
        "correct_index": 2,
        "why": "An ultrasound image is built from the partial reflections at "
               "tissue boundaries, so a boundary shows up even when the two "
               "tissues absorb X-rays equally and give no X-ray contrast.",
    },
    {
        "id": "ks4-sound-waves-hearing-h04",
        "subtopic_slug": "sound-waves-hearing",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A student states: 'A person's hearing range narrows as they "
                "age, so an older person cannot hear a low-pitched hum that a "
                "child can hear.' Evaluate this statement.",
        "options": [
            "Correct — the hearing range narrows by the same amount at both "
            "ends as a person gets older",
            "Correct — the whole of the hearing range shifts steadily to higher "
            "frequencies as a person ages, so the very lowest sounds are "
            "always the first ones to be lost",
            "Incorrect — the range of frequencies a person can hear does not "
            "change at all as they get older",
            "The first part is right but the conclusion is wrong: it is the "
            "upper limit that falls, so high-pitched sounds are lost, not "
            "low-pitched ones",
        ],
        "correct_index": 3,
        "why": "Ageing lowers the upper limit of hearing from about 20 kHz, "
               "so it is high frequencies that become inaudible; the 20 Hz "
               "lower limit is essentially unchanged.",
    },

    # ── waves-detection-exploration ─────────────────────────────────────
    # TRIPLE ONLY, higher tier. Spec 6.6.1.5 (HT only, physics only).
    {
        "id": "ks4-waves-detection-exploration-e01",
        "subtopic_slug": "waves-detection-exploration",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which type of seismic wave is longitudinal.",
        "options": [
            "S-waves, because they are the slower of the two types",
            "Both P-waves and S-waves are longitudinal",
            "P-waves, which travel as compressions and rarefactions",
            "Neither — all seismic waves are transverse",
        ],
        "correct_index": 2,
        "why": "P-waves are pressure waves: the rock is compressed and "
               "rarefied along the direction of travel, which is what makes "
               "a wave longitudinal.",
    },
    {
        "id": "ks4-waves-detection-exploration-e02",
        "subtopic_slug": "waves-detection-exploration",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "State which seismic wave arrives first at a seismograph "
                "after a distant earthquake.",
        "options": [
            "The P-wave, because it is the faster of the two",
            "The S-wave, because it is the faster of the two",
            "They arrive together, because both are produced at the same "
            "instant",
            "The S-wave, because a transverse wave takes a more direct path "
            "through rock",
        ],
        "correct_index": 0,
        "why": "P stands for primary: P-waves travel faster than S-waves "
               "through the same rock, so they always arrive first.",
    },
    {
        "id": "ks4-waves-detection-exploration-e03",
        "subtopic_slug": "waves-detection-exploration",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Echo sounding is used to map the seabed. State what must be "
                "measured in order to find the depth.",
        "options": [
            "The loudness of the returning echo",
            "The wavelength of the pulse sent into the water",
            "The change in frequency between the pulse and its echo",
            "The time taken for the pulse to return after it is sent out",
        ],
        "correct_index": 3,
        "why": "The depth comes from the return time and the known speed of "
               "sound in the water, using d = v × t ÷ 2.",
    },
    {
        "id": "ks4-waves-detection-exploration-e04",
        "subtopic_slug": "waves-detection-exploration",
        "band": "easier",
        "tier": "higher",
        "triple_only": True,
        "text": "Name the process by which a wave changes direction when its "
                "speed changes at a boundary between two materials.",
        "options": [
            "Reflection",
            "Refraction",
            "Absorption",
            "Transmission",
        ],
        "correct_index": 1,
        "why": "Refraction is a change of direction caused by a change of "
               "wave speed as the wave crosses into a different material.",
    },
    {
        "id": "ks4-waves-detection-exploration-s01",
        "subtopic_slug": "waves-detection-exploration",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Geologists set off a small explosion at the surface and "
                "record the waves that return. Explain how this helps them "
                "locate a layer of oil-bearing rock.",
        "options": [
            "The explosion heats the ground, and oil-bearing layers then "
            "glow strongly in the infrared",
            "The waves are absorbed completely by any oil that they meet, so "
            "the depth at which the returning signal disappears altogether "
            "is the depth at which the oil lies",
            "Oil-bearing rock emits seismic waves of its own, which the "
            "detectors at the surface pick up",
            "Seismic waves reflect from the boundaries between rock layers, "
            "and the arrival times of those reflections show how deep each "
            "boundary lies",
        ],
        "correct_index": 3,
        "why": "Each boundary between rock types reflects part of the wave, "
               "so the time each reflection takes to return gives the depth "
               "of that boundary and builds a picture of the structure.",
    },
    {
        "id": "ks4-waves-detection-exploration-s02",
        "subtopic_slug": "waves-detection-exploration",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why seismic waves follow curved paths through the "
                "mantle rather than travelling in straight lines.",
        "options": [
            "Gravity pulls the waves downwards as they travel, bending their "
            "path towards the centre",
            "Their speed changes gradually with depth, so they are "
            "continuously refracted",
            "They are repeatedly reflected from the underside of the crust "
            "as they travel",
            "They lose energy as they travel, and a slower wave always bends "
            "towards the core",
        ],
        "correct_index": 1,
        "why": "Rock properties change gradually with depth, so the wave "
               "speed changes continuously and the wave is refracted at "
               "every step, giving a smooth curve rather than a straight "
               "line.",
    },
    {
        "id": "ks4-waves-detection-exploration-s03",
        "subtopic_slug": "waves-detection-exploration",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "An echo sounder on a ship sends a pulse down to a seabed "
                "known to be 240 m below. The echo returns 0.30 s later. "
                "Calculate the speed of sound in this water.",
        "options": [
            "1600 m/s",
            "800 m/s",
            "3200 m/s",
            "80 m/s",
        ],
        "correct_index": 0,
        "why": "The pulse makes the journey twice, covering 2 × 240 m = "
               "480 m in 0.30 s, so v = 480 ÷ 0.30 = 1600 m/s.",
    },
    {
        "id": "ks4-waves-detection-exploration-s04",
        "subtopic_slug": "waves-detection-exploration",
        "band": "standard",
        "tier": "higher",
        "triple_only": True,
        "text": "Radar pulses are used to measure the thickness of an ice "
                "sheet, but ocean depth is measured with sound pulses "
                "instead. Suggest why radio waves are not used at sea.",
        "options": [
            "Radio waves travel too quickly through water for the return "
            "time to be measured at all",
            "Sound cannot pass through ice, so radio waves are the only "
            "option available on a glacier",
            "Radio waves are strongly absorbed by water, so they would not "
            "return from the seabed, whereas they pass through ice",
            "Radio waves are transverse, and a transverse wave of any kind "
            "cannot be reflected from the surface of a liquid such as "
            "seawater",
        ],
        "correct_index": 2,
        "why": "Water absorbs radio waves over a short distance, so no echo "
               "comes back from the seabed; ice transmits them well enough "
               "for a reflection from the rock beneath to be detected.",
    },
    {
        "id": "ks4-waves-detection-exploration-h01",
        "subtopic_slug": "waves-detection-exploration",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "P-waves and S-waves leave an earthquake focus at the same "
                "instant. A seismograph 2000 km away records the P-wave 60 s "
                "before the S-wave. The average speed of the P-wave along "
                "this path is 8.0 km/s. Calculate the average speed of the "
                "S-wave.",
        "options": [
            "8.0 km/s",
            "6.5 km/s",
            "11 km/s",
            "33 km/s",
        ],
        "correct_index": 1,
        "why": "The P-wave takes 2000 ÷ 8.0 = 250 s, so the S-wave takes "
               "310 s and travels at 2000 ÷ 310 = 6.5 km/s.",
    },
    {
        "id": "ks4-waves-detection-exploration-h02",
        "subtopic_slug": "waves-detection-exploration",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Explain why a P-wave shadow zone exists on the Earth's "
                "surface even though P-waves are able to pass through the "
                "liquid outer core.",
        "options": [
            "P-waves are absorbed by the liquid outer core, so a band of the "
            "surface receives none of them",
            "P-waves are converted into S-waves at the core boundary and are "
            "then blocked by the liquid",
            "P-waves refract sharply where they enter and leave the core, "
            "which deflects them away from a band of the surface",
            "P-waves lose so much energy in crossing the core that they are "
            "too weak to detect anywhere beyond it",
        ],
        "correct_index": 2,
        "why": "The large change in speed at the core boundary refracts "
               "P-waves strongly, bending them away from a ring of the "
               "surface that then receives none.",
    },
    {
        "id": "ks4-waves-detection-exploration-h03",
        "subtopic_slug": "waves-detection-exploration",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "Compare what P-waves and S-waves each reveal about the "
                "material they travel through.",
        "options": [
            "P-waves show that a material can transmit compressions, so they "
            "cross solids and liquids; S-waves need a material that resists "
            "shearing, so they cross solids only",
            "P-waves cross only solids while S-waves are able to cross both "
            "solids and liquids, which is the reason that P-waves are "
            "always the first of the two to reach a seismograph",
            "Both cross solids and liquids, but P-waves are slowed much more "
            "by a liquid than S-waves are",
            "P-waves reveal the density of a layer, while S-waves reveal its "
            "temperature",
        ],
        "correct_index": 0,
        "why": "A liquid has no rigidity, so it cannot carry the sideways "
               "shearing motion of an S-wave, but it can be compressed and "
               "so carries a P-wave.",
    },
    {
        "id": "ks4-waves-detection-exploration-h04",
        "subtopic_slug": "waves-detection-exploration",
        "band": "harder",
        "tier": "higher",
        "triple_only": True,
        "text": "A survey pulse travels down through 750 m of seawater at "
                "1500 m/s and then through 90 m of soft mud at 1800 m/s "
                "before reflecting from bedrock. Calculate the total time "
                "between sending the pulse and receiving the echo.",
        "options": [
            "0.55 s",
            "0.47 s",
            "0.56 s",
            "1.10 s",
        ],
        "correct_index": 3,
        "why": "One way takes 750 ÷ 1500 + 90 ÷ 1800 = 0.50 + 0.05 = 0.55 s, "
               "and the pulse makes the journey twice, so the echo returns "
               "after 1.10 s.",
    },

    # ── properties-of-waves ─────────────────────────────────────────────
    # BASE (foundation, not triple). Spec 6.6.1.2.
    {
        "id": "ks4-properties-of-waves-e01",
        "subtopic_slug": "properties-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Define the amplitude of a wave.",
        "options": [
            "The distance from one crest to the next crest along the wave",
            "The total vertical distance measured from a crest right down to "
            "the trough below it",
            "The number of complete waves that pass a point each second",
            "The maximum displacement of a point on the wave from its "
            "undisturbed position",
        ],
        "correct_index": 3,
        "why": "Amplitude is measured from the equilibrium line to a crest, "
               "so a crest-to-trough measurement is twice the amplitude.",
    },
    {
        "id": "ks4-properties-of-waves-e02",
        "subtopic_slug": "properties-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the period of a wave.",
        "options": [
            "The number of complete waves produced each second",
            "The time taken for one complete wave to pass a point",
            "The distance the wave travels in one second",
            "The length of one complete wave, from crest to crest",
        ],
        "correct_index": 1,
        "why": "The period is a time, in seconds, for one full cycle; "
               "frequency is the number of cycles per second, and the two "
               "are reciprocals.",
    },
    {
        "id": "ks4-properties-of-waves-e03",
        "subtopic_slug": "properties-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wave travels at 12 m/s and has a wavelength of 3.0 m. "
                "Calculate its frequency.",
        "options": [
            "4.0 Hz",
            "36 Hz",
            "0.25 Hz",
            "9.0 Hz",
        ],
        "correct_index": 0,
        "why": "Rearranging v = fλ gives f = v ÷ λ = 12 ÷ 3.0 = 4.0 Hz.",
    },
    {
        "id": "ks4-properties-of-waves-e04",
        "subtopic_slug": "properties-of-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Water waves in a ripple tank have a wavelength of 0.020 m "
                "and a frequency of 15 Hz. Calculate the wave speed.",
        "options": [
            "750 m/s",
            "0.0013 m/s",
            "0.30 m/s",
            "3.0 m/s",
        ],
        "correct_index": 2,
        "why": "v = fλ = 15 × 0.020 = 0.30 m/s.",
    },
    {
        "id": "ks4-properties-of-waves-s01",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An oscilloscope shows a sound wave in which one complete "
                "cycle takes 0.0025 s. The speed of sound in air is 340 m/s. "
                "Calculate the wavelength of the sound.",
        "options": [
            "0.85 m",
            "1.2 m",
            "136 000 m",
            "0.0074 m",
        ],
        "correct_index": 0,
        "why": "f = 1 ÷ T = 1 ÷ 0.0025 = 400 Hz, so λ = v ÷ f = "
               "340 ÷ 400 = 0.85 m.",
    },
    {
        "id": "ks4-properties-of-waves-s02",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student says that doubling the amplitude of a wave also "
                "doubles its frequency. Explain whether this is correct.",
        "options": [
            "Correct — amplitude and frequency always increase together",
            "Correct — a taller wave must pass a given point more often",
            "Incorrect — amplitude and frequency are independent; changing "
            "how far the wave oscillates does not change how many waves pass "
            "each second",
            "Incorrect — doubling the amplitude halves the frequency instead, "
            "because the total energy the wave carries past a point each "
            "second cannot change",
        ],
        "correct_index": 2,
        "why": "Amplitude describes how far each point is displaced and "
               "frequency describes how often it repeats; the source can "
               "change one without changing the other.",
    },
    {
        "id": "ks4-properties-of-waves-s03",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "In a ripple tank, 30 complete waves pass a fixed point in "
                "6.0 s, and the distance from one crest to the next is "
                "0.040 m. Calculate the speed of the waves.",
        "options": [
            "1.2 m/s",
            "0.20 m/s",
            "0.24 m/s",
            "0.0080 m/s",
        ],
        "correct_index": 1,
        "why": "f = 30 ÷ 6.0 = 5.0 Hz, so v = fλ = 5.0 × 0.040 = 0.20 m/s.",
    },
    {
        "id": "ks4-properties-of-waves-s04",
        "subtopic_slug": "properties-of-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Describe how a stroboscope is used to measure the wavelength "
                "of the waves in a ripple tank.",
        "options": [
            "It changes the frequency of the vibrating bar until the "
            "wavelength is a whole number of centimetres",
            "It measures the time that one single wave takes to cross the whole "
            "of the tank, and this time is then divided by the carefully "
            "measured length of the tank",
            "It counts the number of waves that pass a point each second, "
            "which gives the wavelength directly",
            "It flashes at the wave frequency so the pattern appears frozen, "
            "and the distance across several waves is then measured and "
            "divided by the number of waves",
        ],
        "correct_index": 3,
        "why": "Freezing the pattern makes the crests stand still long "
               "enough to measure, and measuring across several waves and "
               "dividing reduces the percentage uncertainty.",
    },
    {
        "id": "ks4-properties-of-waves-h01",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A wave of frequency 50 Hz travels at 300 m/s in one material "
                "and at 200 m/s in a second material. Determine its "
                "wavelength in each material.",
        "options": [
            "4.0 m in the first material and 6.0 m in the second",
            "6.0 m in both, because the wavelength is fixed by the source",
            "6.0 m in the first material and 4.0 m in the second",
            "0.17 m in the first material and 0.25 m in the second",
        ],
        "correct_index": 2,
        "why": "λ = v ÷ f, so the wavelengths are 300 ÷ 50 = 6.0 m and "
               "200 ÷ 50 = 4.0 m — the slower material gives the shorter "
               "wavelength.",
    },
    {
        "id": "ks4-properties-of-waves-h02",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student measures 5 complete waves along 40 cm of a "
                "vibrating rope, and counts 20 waves passing a point in "
                "4.0 s. Determine the speed of the wave along the rope.",
        "options": [
            "2.0 m/s",
            "40 m/s",
            "1.6 m/s",
            "0.40 m/s",
        ],
        "correct_index": 3,
        "why": "λ = 0.40 ÷ 5 = 0.080 m and f = 20 ÷ 4.0 = 5.0 Hz, so "
               "v = fλ = 5.0 × 0.080 = 0.40 m/s.",
    },
    {
        "id": "ks4-properties-of-waves-h03",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'The amplitude of this wave is 8 cm, "
                "because the trace rises 4 cm above the centre line and falls "
                "4 cm below it.' Identify the error.",
        "options": [
            "There is no error — the amplitude is the full height of the "
            "trace from top to bottom",
            "The amplitude is 4 cm: it is measured from the centre line to a "
            "crest, not from a trough to a crest",
            "The amplitude is 16 cm, because the measurement has to be taken "
            "over one whole cycle of the wave",
            "The amplitude cannot be found from a trace of this kind; only "
            "the wavelength can be measured from it",
        ],
        "correct_index": 1,
        "why": "Amplitude is the maximum displacement from the undisturbed "
               "position, so it is half the crest-to-trough height: 4 cm.",
    },
    {
        "id": "ks4-properties-of-waves-h04",
        "subtopic_slug": "properties-of-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sound travels at 340 m/s in air and at 1500 m/s in water. A "
                "sound of frequency 100 Hz passes from air into water. "
                "Determine what happens to its wavelength.",
        "options": [
            "It increases from 3.4 m to 15 m, because the speed rises while "
            "the frequency stays at 100 Hz",
            "It decreases from 15 m to 3.4 m, because water is denser than "
            "air",
            "It stays at 3.4 m, because the wavelength is set by the source "
            "and cannot change",
            "It increases from 3.4 m to 15 m, because the frequency rises in "
            "the denser water as well as the speed",
        ],
        "correct_index": 0,
        "why": "The source sets the frequency and it does not change, so "
               "λ = v ÷ f rises with the speed: 340 ÷ 100 = 3.4 m becomes "
               "1500 ÷ 100 = 15 m.",
    },

    # ── types-of-em-waves ───────────────────────────────────────────────
    # BASE (foundation, not triple). Spec 6.6.2.1.
    {
        "id": "ks4-types-of-em-waves-e01",
        "subtopic_slug": "types-of-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the type of wave that every electromagnetic wave is.",
        "options": [
            "Longitudinal, in the same way as sound",
            "Transverse",
            "Longitudinal in a vacuum and transverse in a material",
            "Transverse for visible light only; the rest are longitudinal",
        ],
        "correct_index": 1,
        "why": "All electromagnetic waves are transverse — the electric and "
               "magnetic fields oscillate perpendicular to the direction the "
               "energy travels.",
    },
    {
        "id": "ks4-types-of-em-waves-e02",
        "subtopic_slug": "types-of-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "Place these three parts of the electromagnetic spectrum in "
                "order of increasing wavelength: ultraviolet, microwaves, "
                "infrared.",
        "options": [
            "Microwaves, infrared, ultraviolet",
            "Infrared, ultraviolet, microwaves",
            "Ultraviolet, microwaves, infrared",
            "Ultraviolet, infrared, microwaves",
        ],
        "correct_index": 3,
        "why": "Wavelength increases from gamma towards radio, so of these "
               "three ultraviolet is shortest, then infrared, then "
               "microwaves.",
    },
    {
        "id": "ks4-types-of-em-waves-e03",
        "subtopic_slug": "types-of-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State which colour of visible light has the shortest "
                "wavelength.",
        "options": [
            "Red",
            "Green",
            "Violet",
            "Yellow",
        ],
        "correct_index": 2,
        "why": "The visible spectrum runs from red at about 700 nm to violet "
               "at about 400 nm, so violet has the shortest wavelength and "
               "the highest frequency.",
    },
    {
        "id": "ks4-types-of-em-waves-e04",
        "subtopic_slug": "types-of-em-waves",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the two parts of the electromagnetic spectrum that lie "
                "on either side of visible light.",
        "options": [
            "Infrared on the long-wavelength side and ultraviolet on the "
            "short-wavelength side",
            "Ultraviolet on the long-wavelength side and infrared on the "
            "short-wavelength side",
            "Microwaves on the long-wavelength side and X-rays on the "
            "short-wavelength side",
            "Radio waves on the long-wavelength side and gamma rays on the "
            "short-wavelength side",
        ],
        "correct_index": 0,
        "why": "The spectrum runs radio, microwave, infrared, visible, "
               "ultraviolet, X-ray, gamma, so visible light has infrared "
               "immediately below it and ultraviolet immediately above it.",
    },
    {
        "id": "ks4-types-of-em-waves-s01",
        "subtopic_slug": "types-of-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "An X-ray has a wavelength of 1.0 × 10⁻¹⁰ m. Calculate its "
                "frequency in a vacuum. The speed of electromagnetic waves "
                "in a vacuum is 3.0 × 10⁸ m/s.",
        "options": [
            "3.0 × 10⁻² Hz",
            "3.3 × 10⁻¹⁹ Hz",
            "3.0 × 10⁸ Hz",
            "3.0 × 10¹⁸ Hz",
        ],
        "correct_index": 3,
        "why": "f = c ÷ λ = 3.0 × 10⁸ ÷ 1.0 × 10⁻¹⁰ = 3.0 × 10¹⁸ Hz.",
    },
    {
        "id": "ks4-types-of-em-waves-s02",
        "subtopic_slug": "types-of-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why a gamma ray transfers more energy than a radio "
                "wave.",
        "options": [
            "It has a much higher frequency, and the energy carried "
            "increases with frequency",
            "It travels much faster than a radio wave does through a vacuum",
            "It has a much longer wavelength, and the energy carried "
            "increases with wavelength",
            "It has a much larger amplitude than a radio wave has",
        ],
        "correct_index": 0,
        "why": "Across the electromagnetic spectrum, energy rises with "
               "frequency, and gamma rays sit at the highest-frequency end "
               "of it.",
    },
    {
        "id": "ks4-types-of-em-waves-s03",
        "subtopic_slug": "types-of-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Suggest why the electromagnetic spectrum is described as "
                "continuous, even though it is drawn as seven named groups.",
        "options": [
            "Because the seven groups repeat themselves over and over again at "
            "higher and higher frequencies, without ever coming to an end",
            "Because the groups are only convenient labels — the wavelengths "
            "run smoothly from one group into the next, with no gaps",
            "Because each group contains exactly one wavelength, and "
            "together the seven cover every possible value",
            "Because all seven of the groups have the same wavelength when "
            "they travel through a vacuum",
        ],
        "correct_index": 1,
        "why": "Every wavelength exists somewhere in the spectrum; the seven "
               "names mark useful regions rather than real boundaries, which "
               "is why X-rays and gamma rays can overlap.",
    },
    {
        "id": "ks4-types-of-em-waves-s04",
        "subtopic_slug": "types-of-em-waves",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A beam of visible light and a beam of gamma rays each cross "
                "the same 1.0 m gap in a vacuum. Compare the time each takes "
                "and the energy each transfers.",
        "options": [
            "The gamma rays cross in less time and transfer more energy",
            "The gamma rays cross in less time but transfer the same energy",
            "Both cross in the same time, but the gamma rays transfer more "
            "energy",
            "Both cross in the same time and transfer the same energy",
        ],
        "correct_index": 2,
        "why": "Speed in a vacuum is the same for every electromagnetic "
               "wave, so the crossing times match, but energy rises with "
               "frequency and gamma rays have far the higher frequency.",
    },
    {
        "id": "ks4-types-of-em-waves-h01",
        "subtopic_slug": "types-of-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Ultraviolet light has a wavelength of 3.0 × 10⁻⁷ m. A radio "
                "wave has a wavelength of 1.5 × 10² m. Determine how many "
                "times greater the frequency of the ultraviolet is.",
        "options": [
            "5.0 × 10⁸ times greater",
            "5.0 × 10⁸ times smaller",
            "2.0 × 10⁻⁹ times greater",
            "4.5 × 10⁻⁵ times greater",
        ],
        "correct_index": 0,
        "why": "Both travel at the same speed, so frequency is inversely "
               "proportional to wavelength: the ratio is "
               "1.5 × 10² ÷ 3.0 × 10⁻⁷ = 5.0 × 10⁸.",
    },
    {
        "id": "ks4-types-of-em-waves-h02",
        "subtopic_slug": "types-of-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "An electromagnetic wave in a vacuum has a frequency of "
                "6.0 × 10¹² Hz. The speed of electromagnetic waves in a "
                "vacuum is 3.0 × 10⁸ m/s. Determine which part of the "
                "spectrum it belongs to.",
        "options": [
            "Radio waves",
            "Visible light",
            "Infrared",
            "Ultraviolet",
        ],
        "correct_index": 2,
        "why": "λ = c ÷ f = 3.0 × 10⁸ ÷ 6.0 × 10¹² = 5.0 × 10⁻⁵ m, which "
               "lies between 700 nm and 1 mm — the infrared region.",
    },
    {
        "id": "ks4-types-of-em-waves-h03",
        "subtopic_slug": "types-of-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Explain why an object at room temperature emits infrared "
                "radiation but does not glow with visible light.",
        "options": [
            "An object at room temperature is not hot enough to produce any "
            "electromagnetic radiation at all",
            "Visible light is produced only by objects that are actually "
            "burning, while infrared is produced by every kind of matter "
            "there is",
            "Infrared can pass through air while visible light is absorbed "
            "by the air around the object",
            "Every object above absolute zero emits infrared; producing "
            "visible light needs the far higher energies of a very hot "
            "object",
        ],
        "correct_index": 3,
        "why": "Emission depends on temperature: a room-temperature object "
               "radiates mainly in the infrared, and only at much higher "
               "temperatures does the emission reach visible frequencies.",
    },
    {
        "id": "ks4-types-of-em-waves-h04",
        "subtopic_slug": "types-of-em-waves",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Compare how X-rays and gamma rays are produced, and hence "
                "suggest why a hospital can switch an X-ray machine off but "
                "cannot switch off a gamma source.",
        "options": [
            "X-rays come from the nucleus, so they stop as soon as the current "
            "is switched off, while gamma rays come from decelerating "
            "electrons and simply carry on regardless",
            "X-rays are produced by firing fast electrons at a metal target, "
            "which stops with the current; gamma rays come from nuclear "
            "decay, which cannot be turned off",
            "Both come from nuclear decay, but the X-ray source has a much "
            "shorter half-life and dies away quickly",
            "X-rays are produced by heating a filament and gamma rays by "
            "cooling one, so only the heating can be stopped",
        ],
        "correct_index": 1,
        "why": "X-ray production depends on an electron beam supplied by the "
               "machine, while gamma emission comes from unstable nuclei "
               "decaying at their own rate, which no switch can change.",
    },

    # ── properties-em-waves-1 ───────────────────────────────────────────
    # BASE (foundation, not triple). Spec 6.6.2.2.
    # ⚠️ No total internal reflection or critical angle here — that is the
    # lesson's HT extension, and these questions are sat by Foundation
    # Combined classes.
    {
        "id": "ks4-properties-em-waves-1-e01",
        "subtopic_slug": "properties-em-waves-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what causes a wave to refract at a boundary between "
                "two materials.",
        "options": [
            "A change in the frequency of the wave at the boundary",
            "A change in the amplitude of the wave at the boundary",
            "A change in the speed of the wave at the boundary",
            "A change in the colour of the wave at the boundary",
        ],
        "correct_index": 2,
        "why": "Refraction happens because the wave travels at a different "
               "speed in the second material, which swings its direction "
               "round at the boundary.",
    },
    {
        "id": "ks4-properties-em-waves-1-e02",
        "subtopic_slug": "properties-em-waves-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State the name of the line drawn at right angles to a "
                "boundary at the point where a ray meets it.",
        "options": [
            "The normal",
            "The incident ray",
            "The refracted ray",
            "The boundary line",
        ],
        "correct_index": 0,
        "why": "The normal is the construction line perpendicular to the "
               "surface, and both the angle of incidence and the angle of "
               "refraction are measured from it.",
    },
    {
        "id": "ks4-properties-em-waves-1-e03",
        "subtopic_slug": "properties-em-waves-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what is meant by the angle of incidence when a ray "
                "meets a boundary between two materials.",
        "options": [
            "The angle between the incoming ray and the surface of the "
            "boundary",
            "The angle between the incoming ray and the normal",
            "The angle between the incoming ray and the refracted ray",
            "The angle between the normal and the surface of the boundary",
        ],
        "correct_index": 1,
        "why": "Both the angle of incidence and the angle of refraction are "
               "measured from the normal, never from the surface — measuring "
               "from the surface gives a different angle altogether.",
    },
    {
        "id": "ks4-properties-em-waves-1-e04",
        "subtopic_slug": "properties-em-waves-1",
        "band": "easier",
        "tier": "foundation",
        "triple_only": False,
        "text": "State what happens to microwaves when they reach the water "
                "in a bowl of soup inside a microwave oven.",
        "options": [
            "They are reflected from the surface of the water without "
            "heating it",
            "They pass straight through the water and heat only the bowl",
            "They are refracted by the water and pass back out of the oven",
            "They are absorbed by the water molecules, which heats the soup",
        ],
        "correct_index": 3,
        "why": "Water molecules absorb microwaves strongly, and the absorbed "
               "energy is transferred to the store of thermal energy of the "
               "food.",
    },
    {
        "id": "ks4-properties-em-waves-1-s01",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ray of light travels from water into air. The angle of "
                "incidence in the water is 30°. Predict the angle of "
                "refraction in the air.",
        "options": [
            "Exactly 30°, since a ray does not bend at a water-to-air "
            "boundary",
            "Greater than 30°, because the light speeds up and bends away "
            "from the normal",
            "Less than 30°, because the light speeds up and bends towards "
            "the normal",
            "Less than 30°, because air is less dense and always bends light "
            "towards the normal",
        ],
        "correct_index": 1,
        "why": "Light travels faster in air than in water, and a wave "
               "entering a faster material always bends away from the "
               "normal.",
    },
    {
        "id": "ks4-properties-em-waves-1-s02",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Sunscreen protects skin from the Sun. Explain, in terms of "
                "what happens to waves at a boundary, how it does so.",
        "options": [
            "It reflects all electromagnetic radiation equally, so less of "
            "every kind reaches the skin below",
            "It refracts ultraviolet away from the skin while letting "
            "visible light through unchanged",
            "It absorbs visible light, which is the part of ordinary sunlight "
            "that actually damages the living cells of the skin",
            "It absorbs ultraviolet while transmitting visible light, so the "
            "harmful shorter wavelengths do not reach the skin",
        ],
        "correct_index": 3,
        "why": "Materials absorb, transmit or reflect different wavelengths "
               "differently, and sunscreen is chosen because it absorbs in "
               "the ultraviolet while staying clear to visible light.",
    },
    {
        "id": "ks4-properties-em-waves-1-s03",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "A radiographer takes an X-ray image of a broken arm. Explain "
                "how the bone shows up on the image.",
        "options": [
            "Bone reflects X-rays back towards the source while soft tissue "
            "absorbs them completely",
            "Bone refracts X-rays, bending them away from the detector so "
            "that a shadow is formed",
            "Bone absorbs X-rays far more strongly than soft tissue does, so "
            "fewer reach the detector behind it",
            "Bone emits X-rays of its own, which the detector records as a "
            "bright region on the image",
        ],
        "correct_index": 2,
        "why": "The image is a map of how much radiation was transmitted: "
               "bone absorbs X-rays much more than soft tissue, so it leaves "
               "a light region on the film.",
    },
    {
        "id": "ks4-properties-em-waves-1-s04",
        "subtopic_slug": "properties-em-waves-1",
        "band": "standard",
        "tier": "foundation",
        "triple_only": False,
        "text": "Waves in a ripple tank travel from deep water into shallow "
                "water, where they move more slowly. The wavefronts meet the "
                "boundary at an angle to it. Describe what happens to them.",
        "options": [
            "They change direction, bending towards the normal, and their "
            "wavelength decreases",
            "They change direction, bending away from the normal, and their "
            "wavelength increases",
            "They keep the same direction, but their frequency decreases in "
            "the shallow water",
            "They are reflected at the boundary and travel back into the "
            "deep water",
        ],
        "correct_index": 0,
        "why": "Slowing down at a boundary bends a wave towards the normal, "
               "and since λ = v ÷ f with the frequency unchanged, a smaller "
               "speed means a shorter wavelength.",
    },
    {
        "id": "ks4-properties-em-waves-1-h01",
        "subtopic_slug": "properties-em-waves-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A ray of light passes through a rectangular glass block, "
                "entering one face and leaving the opposite face. Explain why "
                "the ray that leaves is parallel to the ray that entered.",
        "options": [
            "Because a ray does not bend at all while it is inside a "
            "rectangular block of glass",
            "Because the two refractions cancel each other out, but only "
            "when the block is very thin",
            "Because the light gradually returns to its original speed while it "
            "is still inside the block, some way before it ever reaches the "
            "second face",
            "Because the ray bends towards the normal on entering and away "
            "from the normal by the same angle on leaving, and the two faces "
            "are parallel",
        ],
        "correct_index": 3,
        "why": "The two boundaries are parallel and the speed change is "
               "reversed at the second one, so the second refraction undoes "
               "the first and only a sideways shift remains.",
    },
    {
        "id": "ks4-properties-em-waves-1-h02",
        "subtopic_slug": "properties-em-waves-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "A student writes: 'Light bends when it enters glass because "
                "the glass pushes it sideways.' Identify what is wrong with "
                "this explanation and give the correct one.",
        "options": [
            "Nothing is wrong: the glass does exert a sideways force on the "
            "light as it enters",
            "There is no sideways push: light travels more slowly in glass "
            "than in air, and it is that change of speed at the boundary "
            "which changes its direction",
            "Light does not bend on entering glass at all; it only bends "
            "when it leaves the glass again",
            "The glass reflects part of the light at its front surface, and it "
            "is that reflected part which appears to a viewer standing "
            "nearby to have been bent",
        ],
        "correct_index": 1,
        "why": "Refraction is caused by the change of wave speed at the "
               "boundary, not by any sideways force acting on the light.",
    },
    {
        "id": "ks4-properties-em-waves-1-h03",
        "subtopic_slug": "properties-em-waves-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Light travels at 3.0 × 10⁸ m/s in air and at 2.0 × 10⁸ m/s "
                "in a plastic block. A beam of light of wavelength "
                "6.0 × 10⁻⁷ m in air enters the plastic. Calculate its "
                "wavelength inside the plastic.",
        "options": [
            "4.0 × 10⁻⁷ m",
            "9.0 × 10⁻⁷ m",
            "6.0 × 10⁻⁷ m",
            "3.0 × 10⁻⁷ m",
        ],
        "correct_index": 0,
        "why": "f = 3.0 × 10⁸ ÷ 6.0 × 10⁻⁷ = 5.0 × 10¹⁴ Hz and does not "
               "change, so in the plastic λ = 2.0 × 10⁸ ÷ 5.0 × 10¹⁴ = "
               "4.0 × 10⁻⁷ m.",
    },
    {
        "id": "ks4-properties-em-waves-1-h04",
        "subtopic_slug": "properties-em-waves-1",
        "band": "harder",
        "tier": "foundation",
        "triple_only": False,
        "text": "Glass transmits visible light but is opaque to ultraviolet. "
                "Suggest why a person sitting behind a closed car window can "
                "still see clearly but does not become sunburnt.",
        "options": [
            "Visible light is refracted straight through the glass, while the "
            "ultraviolet is refracted away from the inside of the car",
            "Ultraviolet travels more slowly than visible light, so it has "
            "not yet reached the passenger",
            "The glass transmits visible light but absorbs ultraviolet, so "
            "the wavelengths that cause sunburn do not get through",
            "The glass reflects visible light into the car and transmits the "
            "ultraviolet back out of it",
        ],
        "correct_index": 2,
        "why": "A material can treat two wavelengths completely differently: "
               "car glass transmits the visible light needed to see and "
               "absorbs the ultraviolet that damages skin.",
    },
]
