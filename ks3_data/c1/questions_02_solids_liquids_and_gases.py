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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-02-e05",
        "band": "easier",
        "text": "The bench says the particles in a solid vibrate. What does "
                "vibrate mean?",
        "options": [
            {"text": "To move quickly back and forth about a fixed position.",
             "correct": True},
            {"text": "To travel slowly from one side of the substance to the "
                     "other.",
             "correct": False,
             "why": "That is travelling, not vibrating. A vibrating particle "
                    "always comes back to the same place."},
            {"text": "To get slightly larger and then smaller again.",
             "correct": False,
             "why": "Particles never change size. Vibrating is about movement "
                    "about a fixed point, not swelling."},
            {"text": "To spin on the spot without moving anywhere.",
             "correct": False,
             "why": "Close, but the movement here is back and forth rather "
                    "than round. The particle rocks about its home position."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e06",
        "band": "easier",
        "text": "The vocabulary warns that gas and air are not the same word. "
                "What is the difference?",
        "options": [
            {"text": "Gas means a substance that has been heated; air means "
                     "one that has not.",
             "correct": False,
             "why": "Temperature has nothing to do with it. A gas can be as "
                    "cold as you like and still be a gas."},
            {"text": "Gas is a state of matter; air is one particular mixture "
                     "of gases.",
             "correct": True},
            {"text": "Gas is what you burn; air is what you breathe.",
             "correct": False,
             "why": "That is one use of one gas. Helium and steam are gases "
                    "and neither is a fuel."},
            {"text": "Gas is invisible; air can be seen when it moves.",
             "correct": False,
             "why": "You cannot see air moving either — you see what it "
                    "carries. The difference is state against mixture."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e07",
        "band": "easier",
        "text": "In which state are the particles far apart, jumbled, and "
                "moving fast in all directions?",
        "options": [
            {"text": "Solid",
             "correct": False,
             "why": "A solid's particles are touching, in a regular pattern, "
                    "and vibrate on the spot without going anywhere."},
            {"text": "Liquid",
             "correct": False,
             "why": "A liquid's particles are jumbled and moving, but they "
                    "are touching — not far apart."},
            {"text": "Gas",
             "correct": True},
            {"text": "All three, at different speeds",
             "correct": False,
             "why": "Only a gas has its particles far apart. That spacing is "
                    "exactly what makes it a gas rather than a liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e08",
        "band": "easier",
        "text": "The contrast table's Volume row says a solid's volume is "
                "fixed and a gas fills whatever it is given. What does it say "
                "for a liquid?",
        "options": [
            {"text": "Fixed, like a solid's.",
             "correct": True},
            {"text": "It fills whatever it is given, like a gas.",
             "correct": False,
             "why": "A litre of water stays a litre in any container. It is "
                    "the SHAPE a liquid takes from its container, not the "
                    "volume."},
            {"text": "It grows slowly as the liquid is left standing.",
             "correct": False,
             "why": "Nothing is added or created by standing still. The "
                    "volume of a liquid does not drift."},
            {"text": "It depends on how wide the container is.",
             "correct": False,
             "why": "A wide dish spreads the liquid out thinly, but the "
                    "amount of liquid — the volume — is unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e09",
        "band": "easier",
        "text": "Most of the matter in the universe is not in any of the "
                "three states this lesson covers. Which state is it in?",
        "options": [
            {"text": "Glass",
             "correct": False,
             "why": "Glass is a single awkward material, not a state, and "
                    "there is very little of it in the universe."},
            {"text": "Liquid crystal",
             "correct": False,
             "why": "Liquid crystals are a curiosity of a few materials, "
                    "including screens. They are nowhere near most of the "
                    "universe."},
            {"text": "Ice",
             "correct": False,
             "why": "Ice is water in the solid state. It is one substance, "
                    "not a fourth state."},
            {"text": "Plasma",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-02-s05",
        "band": "standard",
        "text": "A student says steam rises above a kettle because steam "
                "particles are lighter than the particles in the water below. "
                "What is wrong with that?",
        "options": [
            {"text": "The particles are identical — the same substance in a "
                     "different state, spread far further apart.",
             "correct": True},
            {"text": "Nothing is wrong; heating a particle does make it "
                     "lighter.",
             "correct": False,
             "why": "Heating changes how fast a particle moves and nothing "
                    "else. Its mass and size are untouched."},
            {"text": "Steam does not rise at all — it only looks as though it "
                     "does.",
             "correct": False,
             "why": "It genuinely does rise. The reason is the spacing, not "
                    "a change in the particles."},
            {"text": "Steam is a different substance from the water below it, "
                     "so the two cannot sensibly be compared.",
             "correct": False,
             "why": "Ice, water and steam are one substance in three states. "
                    "That is this lesson's whole point."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s06",
        "band": "standard",
        "text": "In both a solid and a liquid the particles are touching. So "
                "why can a liquid be poured and a solid cannot?",
        "options": [
            {"text": "Because a liquid's particles are smaller than a "
                     "solid's, so they can slip past each other more easily.",
             "correct": False,
             "why": "Same substance, same particles, same size. Melting ice "
                    "does not shrink anything."},
            {"text": "Because a liquid's particles are jumbled and can slide "
                     "past each other; a solid's are locked in a pattern.",
             "correct": True},
            {"text": "Because a liquid is lighter than a solid, so gravity "
                     "moves it more easily.",
             "correct": False,
             "why": "Mercury is a liquid and far heavier than most solids, "
                    "and it still pours. Weight is not what decides it."},
            {"text": "Because a liquid has gaps between its particles and a "
                     "solid does not.",
             "correct": False,
             "why": "Both have their particles touching, which is why "
                    "neither squashes. What differs is the pattern, not the "
                    "spacing."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s07",
        "band": "standard",
        "text": "A beaker of water is heated until all of it has become "
                "steam. Which one of these has NOT changed?",
        "options": [
            {"text": "The space between the particles",
             "correct": False,
             "why": "This is the biggest change of all. Gas particles sit far "
                    "further apart than liquid ones."},
            {"text": "The average speed of the particles",
             "correct": False,
             "why": "Heating is exactly what speeds particles up, so this has "
                    "certainly changed."},
            {"text": "The size of each particle",
             "correct": True},
            {"text": "The volume the substance takes up",
             "correct": False,
             "why": "Steam fills a room where the water filled a beaker. The "
                    "volume changes enormously."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s08",
        "band": "standard",
        "text": "Two sealed boxes hold the same substance and the same number "
                "of particles — one as a liquid, one as a gas. Which box is "
                "heavier?",
        "options": [
            {"text": "The liquid one, because a liquid is denser.",
             "correct": False,
             "why": "Denser means the same mass packed into less room. With "
                    "the same particles counted out, the mass is the same."},
            {"text": "The gas one, because its particles are moving faster.",
             "correct": False,
             "why": "Speed is not mass. A fast particle weighs exactly what a "
                    "slow one weighs."},
            {"text": "The liquid one, because a gas is nearly all empty "
                     "space.",
             "correct": False,
             "why": "Empty space has no mass, so it takes nothing away. The "
                    "same particles are in both boxes."},
            {"text": "Neither — identical particles, and the same number of "
                     "them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s09",
        "band": "standard",
        "text": "You can stand on a frozen pond but not on the water "
                "underneath it. Which fact from the table explains that?",
        "options": [
            {"text": "A solid's particles are held in fixed positions in a "
                     "regular pattern, so it keeps its own shape.",
             "correct": True},
            {"text": "A solid's particles are heavier, so they can carry more "
                     "weight.",
             "correct": False,
             "why": "Ice and water are the same particles. Nothing has got "
                    "heavier by freezing."},
            {"text": "A solid has no gaps at all, while a liquid does.",
             "correct": False,
             "why": "Neither has space to spare — that is why neither "
                    "squashes. It is the fixed pattern that holds you up."},
            {"text": "A solid's particles have stopped moving altogether, so "
                     "they cannot get out of the way of your foot.",
             "correct": False,
             "why": "They have not stopped — they vibrate on the spot. What "
                    "matters is that they never leave their positions."},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-02-h05",
        "band": "harder",
        "text": "Liquid crystals flow like a liquid while their particles "
                "stay lined up like a solid's. Which two rows of the contrast "
                "table disagree about them?",
        "options": [
            {"text": "Shape and volume — one of them says the container's, "
                     "the other says fixed for ever.",
             "correct": False,
             "why": "Those two rows are consequences, not causes. The "
                    "disagreement is higher up the table, in the rows they "
                    "come from."},
            {"text": "Arrangement and movement — the arrangement is a "
                     "solid's, the movement is a liquid's.",
             "correct": True},
            {"text": "Squashing and pouring — it can do both, and no state "
                     "can.",
             "correct": False,
             "why": "A liquid crystal is no easier to squash than any other "
                    "liquid. Its oddity is being ordered and mobile at "
                    "once."},
            {"text": "Volume and squashing — its volume changes as it is "
                     "pressed.",
             "correct": False,
             "why": "Its particles are touching, so it resists a squash like "
                    "any liquid. The awkward pair is arrangement against "
                    "movement."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h06",
        "band": "harder",
        "text": "A sealed syringe holding 20 cm³ of air is pushed hard and "
                "the air ends up in 5 cm³. What is the smallest fraction of "
                "the original 20 cm³ that must have been empty space?",
        "options": [
            {"text": "About one quarter of it",
             "correct": False,
             "why": "One quarter is what is LEFT at the end. The space you "
                    "removed is the other three quarters."},
            {"text": "About one half of it",
             "correct": False,
             "why": "Halving would have stopped the plunger at 10 cm³. It "
                    "reached 5 cm³, so far more space than that was "
                    "removed."},
            {"text": "About three quarters of it",
             "correct": True},
            {"text": "None of it — the particles were squashed instead",
             "correct": False,
             "why": "Particles do not squash. Every cubic centimetre the "
                    "plunger travelled was empty space being removed."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h07",
        "band": "harder",
        "text": "Someone claims to have found a genuinely new state of "
                "matter. Using this lesson, what would you need to be shown "
                "before you agreed?",
        "options": [
            {"text": "That it looks and feels quite different from any solid, "
                     "liquid or gas you have seen.",
             "correct": False,
             "why": "Appearance is not what defines a state. Mercury looks "
                    "unlike water and both are liquids."},
            {"text": "That it is made of a substance nobody has ever met.",
             "correct": False,
             "why": "A state is not a substance. Ice, water and steam are one "
                    "substance in three states."},
            {"text": "That its particles are arranged and move in a way none "
                     "of the three known states does.",
             "correct": True},
            {"text": "That it cannot be turned into a solid, a liquid or a "
                     "gas.",
             "correct": False,
             "why": "Many substances move freely between the states, and "
                    "plasma comes from heating a gas. Being reachable does "
                    "not disqualify a state."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h08",
        "band": "harder",
        "text": "Iron is a solid at room temperature and mercury is a liquid, "
                "yet both are metals made of particles. What must be different "
                "about them?",
        "options": [
            {"text": "Mercury's particles must be far smaller than iron's, so "
                     "they slide past each other more easily.",
             "correct": False,
             "why": "Size is not what sets a state — a substance keeps the "
                    "same particles in all three of them."},
            {"text": "Mercury's particles hold each other less strongly, so "
                     "room temperature is enough for them to slide.",
             "correct": True},
            {"text": "Mercury's particles are moving and iron's are "
                     "completely still.",
             "correct": False,
             "why": "Iron's particles vibrate constantly. Nothing in a solid "
                    "is still; the particles simply never leave their "
                    "positions."},
            {"text": "Mercury is at a higher temperature than the iron beside "
                     "it.",
             "correct": False,
             "why": "Both are at room temperature — that is what makes the "
                    "comparison interesting. The difference is inside the "
                    "substances."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h09",
        "band": "harder",
        "text": "A student draws a gas by taking their solid drawing, "
                "shrinking every particle, and leaving them touching. Name the "
                "two things the drawing gets wrong.",
        "options": [
            {"text": "The particles should be the same size as before, and "
                     "far apart rather than touching.",
             "correct": True},
            {"text": "The particles should be larger than before, and still "
                     "touching.",
             "correct": False,
             "why": "Half right at best. Particles never change size in "
                    "either direction, and a gas's are certainly not "
                    "touching."},
            {"text": "The particles should be the same size as before, and "
                     "arranged in neat regular rows.",
             "correct": False,
             "why": "The size is right, but neat rows are a solid. A gas is "
                    "jumbled as well as spread out."},
            {"text": "The particles should be fewer in number, and further "
                     "apart.",
             "correct": False,
             "why": "The spacing is right, but the number does not change — "
                    "melting and boiling never destroy a particle."},
        ],
        "figure": None,
    },
]
