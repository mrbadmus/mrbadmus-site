"""C1 lesson 02 — Solids, liquids and gases: twelve questions (MRB-269).

These probe the one claim the lesson is built to defend — a state is set by how
the particles are arranged and how fast they move, never by any change in the
particles themselves. The distractors are built from the lesson's two declared
misconceptions, PART-03 (the particles themselves melt, soften, shrink or
expand) and PART-04 (particles in a solid are completely still), plus the
classic Year 7 belief that the gaps between gas particles are filled with air
or with heat. Several are read off the instruments the lesson actually draws:
the reference particle, the path trails for each state, the piston, and the
freeze toggle. The `harder` band takes the model somewhere the lesson never
goes (a diving cylinder, a bucket of sand), turns the three-state model on the
one material the stretch layer says it cannot hold (glass), and makes the
student notice that freezing the *drawing* removes half of what defines a
state.
"""

UNIT = "C1"
LESSON = "solids-liquids-and-gases"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-02-e01",
        "band": "easier",
        "text": "The state bench draws one extra particle at the side, "
                "labelled “one particle, actual size”, and it is drawn the "
                "same size beside the solid, beside the liquid and beside "
                "the gas. Why is it drawn that way?",
        "options": [
            {"text": "Because three different sizes would make the boxes "
                     "harder to compare with each other.",
             "correct": False,
             "why": "It is not a drawing convenience. The fixed size is the "
                    "lesson's whole argument made visible: a gas particle and "
                    "a solid particle are the same object."},
            {"text": "Because it is drawn for the solid, and the liquid and "
                     "gas particles are a little smaller.",
             "correct": False,
             "why": "Nothing shrinks when a solid melts or boils. Same size, "
                    "same mass, same substance — the particles are identical "
                    "in all three states."},
            {"text": "Because a particle is the same size in every state — "
                     "only spacing and speed change.",
             "correct": True},
            {"text": "Because particles keep the same size only while the "
                     "substance stays cold and solid.",
             "correct": False,
             "why": "Heating changes how fast particles move and how far "
                    "apart they sit. It never changes their size, at any "
                    "temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e02",
        "band": "easier",
        "text": "You press “Show the paths” on the bench with the solid "
                "showing, and every particle leaves a tiny circular trail. "
                "What does that tell you?",
        "options": [
            {"text": "The particles are slowly swapping places with their "
                     "neighbours.",
             "correct": False,
             "why": "Swapping neighbours is what a liquid's trails show — "
                    "they wander off across the box. A solid's trail closes "
                    "on itself because the particle never leaves home."},
            {"text": "Each particle is vibrating about a fixed position and "
                     "never travels anywhere.",
             "correct": True},
            {"text": "The particles are completely still, and the circles are "
                     "just the drawing wobbling.",
             "correct": False,
             "why": "A solid is not still. Every particle is vibrating about "
                    "a fixed point, and that vibration is exactly what the "
                    "trail is showing you."},
            {"text": "The particles are circling the box slowly, one behind "
                     "the other.",
             "correct": False,
             "why": "Follow one trail and it goes nowhere: a tiny loop in one "
                    "spot, not a lap of the box. Vibration is not travel."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e03",
        "band": "easier",
        "text": "100 cm³ of water is poured from a tall measuring cylinder "
                "into a wide flat dish. Which of the contrast table's rows "
                "has changed?",
        "options": [
            {"text": "Its shape has changed; its volume is still 100 cm³.",
             "correct": True},
            {"text": "Both have changed — the water spreads out, so it takes "
                     "up more room than before.",
             "correct": False,
             "why": "Spreading out IS the shape changing. The particles stay "
                    "touching, so 100 cm³ in the cylinder is still 100 cm³ in "
                    "the dish."},
            {"text": "Neither has changed — a liquid keeps its own shape "
                     "wherever you put it.",
             "correct": False,
             "why": "Keeping its own shape is what makes something a solid. A "
                    "liquid takes the shape of whatever is holding it."},
            {"text": "Its volume has changed; its shape is the same as it was "
                     "in the cylinder.",
             "correct": False,
             "why": "That is the wrong way round. A liquid has a fixed volume "
                    "and no shape of its own."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e04",
        "band": "easier",
        "text": "The bench's note for a gas says that almost all of the box "
                "is empty. What is in that space, between the gas particles?",
        "options": [
            {"text": "Air, which fills in around the gas particles.",
             "correct": False,
             "why": "Air is not something separate that fills the gaps — air "
                    "is itself a gas, made of particles just like these. "
                    "Between the particles there is nothing at all."},
            {"text": "Heat, which is what has pushed the particles so far "
                     "apart.",
             "correct": False,
             "why": "Heat is not a substance that sits in the gaps. Heating "
                    "makes the particles move faster, and moving faster is "
                    "what spreads them out."},
            {"text": "Tiny broken pieces of particles, left behind as the gas "
                     "spread out.",
             "correct": False,
             "why": "Particles do not break up when a substance spreads. "
                    "There are exactly as many as before, exactly as big, "
                    "just much further apart."},
            {"text": "Nothing. The space between the particles is genuinely "
                     "empty.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-02-s01",
        "band": "standard",
        "text": "You turn on “Try to squash it” with the gas showing. The "
                "piston pushes right in, and the same gas now sits in half "
                "the space. What has happened to the particles?",
        "options": [
            {"text": "They have been squashed smaller, so they take up less "
                     "room than they did.",
             "correct": False,
             "why": "This is the idea the whole lesson exists to kill. Not "
                    "one particle changed size — what was removed is the "
                    "empty space between them."},
            {"text": "They have been pushed closer together, and each is "
                     "the size it always was.",
             "correct": True},
            {"text": "Half of them have been forced out of the tube through "
                     "the far end of the piston.",
             "correct": False,
             "why": "Nothing escapes — the tube is sealed. The same number of "
                    "particles is now sharing half the room."},
            {"text": "They have been packed into regular rows, so the gas has "
                     "become a solid.",
             "correct": False,
             "why": "Squashing crowds the particles but does not order them. "
                    "No rows, no fixed positions — it is still a gas, just a "
                    "much more crowded one."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s02",
        "band": "standard",
        "text": "A student writes: “When ice melts the particles move much "
                "further apart, and that is why water can be poured.” Where "
                "has the student gone wrong?",
        "options": [
            {"text": "Nowhere — moving much further apart is exactly what "
                     "melting does to the particles.",
             "correct": False,
             "why": "The bench shows otherwise: a liquid's particles are "
                    "still touching, exactly as in the solid. If they had "
                    "moved much further apart you would have a gas."},
            {"text": "The particles do move apart, but pouring happens "
                     "because they get smaller and slip past more easily.",
             "correct": False,
             "why": "Nothing shrinks. Soft, runny and squashy are words about "
                    "a crowd of particles, never about one particle on its "
                    "own."},
            {"text": "They stay touching — melting removes the regular "
                     "pattern, which lets them slide past each other.",
             "correct": True},
            {"text": "Melting does not move the particles at all — it only "
                     "makes each one go soft.",
             "correct": False,
             "why": "A particle cannot go soft. Melting changes how the "
                    "particles are arranged and how they move, and nothing "
                    "else."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s03",
        "band": "standard",
        "text": "With the gas showing, the paths are long straight runs that "
                "bend only where two particles meet. What does that tell you "
                "about how a gas particle moves?",
        "options": [
            {"text": "It is pulled towards the walls of the box, which is "
                     "why a gas ends up filling its container.",
             "correct": False,
             "why": "Nothing pulls a gas particle. It fills the container "
                    "because nothing holds it back — it simply keeps going "
                    "until a wall stops it."},
            {"text": "It is carried along by the air in the gaps between the "
                     "particles.",
             "correct": False,
             "why": "There is no air in the gaps; the gaps are empty, and if "
                    "this gas is air then the particles ARE the air. Nothing "
                    "carries a particle along."},
            {"text": "It repeats the same path round and round the box, over "
                     "and over again.",
             "correct": False,
             "why": "Every bend in a trail is a collision, and collisions do "
                    "not repeat. The directions are random, which is why the "
                    "paths never settle into a pattern."},
            {"text": "It travels in a straight line until it hits "
                     "something — only a collision turns it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s04",
        "band": "standard",
        "text": "The table's top two rows are arrangement and movement, and "
                "every row below is a consequence of them. Which pair of "
                "facts explains why a solid keeps its own shape?",
        "options": [
            {"text": "Its particles sit in fixed positions in a regular "
                     "pattern, and only vibrate there.",
             "correct": True},
            {"text": "Its particles are heavier than the particles in a "
                     "liquid, so they are much harder to move.",
             "correct": False,
             "why": "They are the same particles with the same mass in all "
                    "three states. Mass is not what fixes a shape — fixed "
                    "positions are."},
            {"text": "Its particles are touching, so there is no space left "
                     "for them to move into.",
             "correct": False,
             "why": "A liquid's particles are touching too, and a liquid has "
                    "no shape of its own. Touching explains why neither "
                    "squashes, not why one holds its shape."},
            {"text": "Its particles are completely still, so nothing can "
                     "shift out of place.",
             "correct": False,
             "why": "A solid is not still. Its particles vibrate constantly — "
                    "they just vibrate about a fixed point instead of "
                    "travelling."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-02-h01",
        "band": "harder",
        "text": "The lesson calls glass a genuine embarrassment to the "
                "three-state model. What is so awkward about it?",
        "options": [
            {"text": "It keeps its shape like a solid, but its particles "
                     "are jumbled like a liquid's.",
             "correct": True},
            {"text": "Its particles are a different size from the particles "
                     "in an ordinary solid material.",
             "correct": False,
             "why": "Particle size is never what sets a state. Glass is "
                    "awkward because of how its particles are arranged, not "
                    "because of anything about the particles themselves."},
            {"text": "It is a mixture of a solid and a liquid, so part of it "
                     "is each of them.",
             "correct": False,
             "why": "It is not part one and part the other. All of it keeps "
                    "its shape, and all of it has a liquid's disordered "
                    "arrangement — which is why neither box fits."},
            {"text": "It has no fixed volume, so it takes up whatever space "
                     "it is given.",
             "correct": False,
             "why": "That describes a gas. Glass has a fixed volume and keeps "
                    "its own shape; the trouble is its arrangement, not its "
                    "volume."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h02",
        "band": "harder",
        "text": "A diver's cylinder holds the air from a space many times "
                "its own size, squeezed into one metal bottle. Using this "
                "lesson, how does that much gas fit in?",
        "options": [
            {"text": "The particles are crushed down to a smaller size, which "
                     "is what makes the extra room.",
             "correct": False,
             "why": "No particle has ever been made smaller by squeezing. "
                    "What gets removed is the empty space between them."},
            {"text": "Most of a gas is empty space, so the same particles "
                     "are now far closer together.",
             "correct": True},
            {"text": "The gas has been turned into a solid, which is how it "
                     "takes up so little room.",
             "correct": False,
             "why": "Nothing has ordered the particles into fixed rows. They "
                    "are far more crowded than they were, but still moving "
                    "freely, so it is still a gas."},
            {"text": "The particles are packed so tightly that there is no "
                     "space left between them at all.",
             "correct": False,
             "why": "With no space left it would stop behaving like a gas "
                    "altogether. There is still a great deal of empty space "
                    "in a full cylinder — just far less than there was."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h03",
        "band": "harder",
        "text": "Sand pours out of a bucket and settles into the shape of "
                "whatever it lands in — and yet sand is a solid. What is the "
                "best explanation?",
        "options": [
            {"text": "Sand is really a liquid, because anything that pours "
                     "and takes the shape of its container is one.",
             "correct": False,
             "why": "You are applying the pouring test at the wrong scale. "
                    "Tip one grain and it keeps its own shape exactly, "
                    "because its particles are locked in fixed positions."},
            {"text": "Sand's particles are touching but jumbled, which is "
                     "what lets the sand be poured.",
             "correct": False,
             "why": "That describes a liquid. Inside every grain the "
                    "particles are in regular fixed rows — what is jumbled is "
                    "the pile of grains, not the particles."},
            {"text": "Each grain is itself a solid; what slides over each "
                     "other are the grains, not the particles.",
             "correct": True},
            {"text": "Sand is a solid because its particles stay completely "
                     "still until the bucket is tipped.",
             "correct": False,
             "why": "A solid's particles never stop. They vibrate about fixed "
                    "positions whether the bucket is tipped or left alone."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h04",
        "band": "harder",
        "text": "You press “Freeze the motion” with the liquid showing, and "
                "every particle stops mid-slide. What has the frozen picture "
                "lost?",
        "options": [
            {"text": "Nothing — cooling a liquid really does stop its "
                     "particles, and that is what freezing means.",
             "correct": False,
             "why": "Freezing a substance never stops its particles. In a "
                    "solid they carry on vibrating, endlessly, about fixed "
                    "positions."},
            {"text": "The spacing — the particles should have spread further "
                     "apart the moment they stopped.",
             "correct": False,
             "why": "Stopping does not change the spacing, and a liquid's "
                    "particles stay touching whatever they are doing. It is "
                    "the movement the button took away."},
            {"text": "The movement — and a state is set by arrangement and "
                     "movement, so half is gone.",
             "correct": True},
            {"text": "The regular rows that a liquid's particles fall into "
                     "once they stop moving.",
             "correct": False,
             "why": "A liquid's particles are jumbled, not in rows, and the "
                    "button freezes the drawing rather than cooling the "
                    "substance. The arrangement on screen has not changed."},
        ],
        "figure": None,
    },
]
