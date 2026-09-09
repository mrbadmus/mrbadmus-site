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
            {"text": "To travel slowly from one side of the substance to the "
                     "other.",
             "correct": False,
             "why": "That is travelling, not vibrating. A vibrating particle "
                    "always comes back to the same place."},
            {"text": "To move quickly back and forth about a fixed position.",
             "correct": True},
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
            {"text": "Gas is what you burn; air is what you breathe.",
             "correct": False,
             "why": "That is one use of one gas. Helium and steam are gases "
                    "and neither is a fuel."},
            {"text": "Gas is a state of matter; air is one particular mixture "
                     "of gases.",
             "correct": True},
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
            {"text": "All three, at different speeds",
             "correct": False,
             "why": "Only a gas has its particles far apart. That spacing is "
                    "exactly what makes it a gas rather than a liquid."},
            {"text": "Gas",
             "correct": True},
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
            {"text": "Plasma",
             "correct": True},
            {"text": "Liquid crystal",
             "correct": False,
             "why": "Liquid crystals are a curiosity of a few materials, "
                    "including screens. They are nowhere near most of the "
                    "universe."},
            {"text": "Ice",
             "correct": False,
             "why": "Ice is water in the solid state. It is one substance, "
                    "not a fourth state."},
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
            {"text": "Nothing is wrong; heating a particle does make it "
                     "lighter.",
             "correct": False,
             "why": "Heating changes how fast a particle moves and nothing "
                    "else. Its mass and size are untouched."},
            {"text": "The particles are identical — the same substance in a "
                     "different state, spread far further apart.",
             "correct": True},
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
            {"text": "Because a liquid is lighter than a solid, so gravity "
                     "moves it more easily.",
             "correct": False,
             "why": "Mercury is a liquid and far heavier than most solids, "
                    "and it still pours. Weight is not what decides it."},
            {"text": "Because a liquid's particles are jumbled and can slide "
                     "past each other; a solid's are locked in a pattern.",
             "correct": True},
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
            {"text": "The volume the substance takes up",
             "correct": False,
             "why": "Steam fills a room where the water filled a beaker. The "
                    "volume changes enormously."},
            {"text": "The size of each particle",
             "correct": True},
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
            {"text": "Neither — identical particles, and the same number of "
                     "them.",
             "correct": True},
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
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s09",
        "band": "standard",
        "text": "You can stand on a frozen pond but not on the water "
                "underneath it. Which fact from the table explains that?",
        "options": [
            {"text": "A solid's particles are heavier, so they can carry more "
                     "weight.",
             "correct": False,
             "why": "Ice and water are the same particles. Nothing has got "
                    "heavier by freezing."},
            {"text": "A solid's particles are held in fixed positions in a "
                     "regular pattern, so it keeps its own shape.",
             "correct": True},
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
            {"text": "That it cannot be turned into a solid, a liquid or a "
                     "gas.",
             "correct": False,
             "why": "Many substances move freely between the states, and "
                    "plasma comes from heating a gas. Being reachable does "
                    "not disqualify a state."},
            {"text": "That its particles are arranged and move in a way none "
                     "of the three known states does.",
             "correct": True},
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
            {"text": "Mercury's particles hold each other less strongly, so "
                     "room temperature is enough for them to slide.",
             "correct": True},
            {"text": "Mercury's particles must be far smaller than iron's, so "
                     "they slide past each other more easily.",
             "correct": False,
             "why": "Size is not what sets a state — a substance keeps the "
                    "same particles in all three of them."},
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
            {"text": "The particles should be larger than before, and still "
                     "touching.",
             "correct": False,
             "why": "Half right at best. Particles never change size in "
                    "either direction, and a gas's are certainly not "
                    "touching."},
            {"text": "The particles should be the same size as before, and "
                     "far apart rather than touching.",
             "correct": True},
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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-02-e10",
        "band": "easier",
        "text": "Describe how the particles are arranged in a solid.",
        "options": [
            {"text": "Far apart from one another, with no pattern at all.",
             "correct": False,
             "why": "Far apart is a gas. In a solid every particle is in "
                    "contact with the neighbours around it."},
            {"text": "Touching one another, in a regular repeating pattern.",
             "correct": True},
            {"text": "Touching one another, but jumbled up.",
             "correct": False,
             "why": "Touching is right, but jumbled describes a liquid. A "
                    "solid's particles are also in a regular pattern."},
            {"text": "In a regular pattern, with wide gaps left between them.",
             "correct": False,
             "why": "The pattern is right and the gaps are not. A solid's "
                    "particles are packed hard against one another."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e11",
        "band": "easier",
        "text": "In a liquid, are the particles touching or far apart, and "
                "are they ordered or jumbled?",
        "options": [
            {"text": "Touching, and jumbled with no pattern.",
             "correct": True},
            {"text": "Touching, and lined up in neat regular rows.",
             "correct": False,
             "why": "Neat rows are a solid. A liquid's particles stay in "
                    "contact but the pattern has gone."},
            {"text": "Far apart, and jumbled with nothing holding them.",
             "correct": False,
             "why": "Far apart is a gas. A liquid's particles are still "
                    "pressed against one another, which is why a liquid "
                    "cannot be squashed."},
            {"text": "Far apart, and lined up in neat rows.",
             "correct": False,
             "why": "No state looks like that. Nothing is both spread out "
                    "and ordered."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e12",
        "band": "easier",
        "text": "State how the particles in a liquid move.",
        "options": [
            {"text": "They stay still until the liquid is poured.",
             "correct": False,
             "why": "Nothing waits to be poured. A liquid's particles are "
                    "moving whether the jug is tipped or left alone."},
            {"text": "They vibrate about fixed positions and never travel.",
             "correct": False,
             "why": "That is a solid. In a liquid a particle really does "
                    "leave its place."},
            {"text": "They slide over one another, so a particle keeps "
                     "changing which particles it is next to.",
             "correct": True},
            {"text": "They fly in long straight lines, with nothing at all "
                     "standing in their way.",
             "correct": False,
             "why": "Long straight runs belong to a gas, where the particles "
                    "are far apart. A liquid's particle is always in contact "
                    "with others."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e13",
        "band": "easier",
        "text": "State how fast the particles in a gas move, and in which "
                "directions.",
        "options": [
            {"text": "Slowly, and always downwards.",
             "correct": False,
             "why": "Gravity does not sort a gas out. Its particles move far "
                    "too fast for that, which is why a gas fills a container "
                    "upwards as well as down."},
            {"text": "Slowly, and round the edge of the container.",
             "correct": False,
             "why": "Nothing steers a gas particle round a circuit. Every "
                    "bend in its path is a collision."},
            {"text": "Quickly, but all in the same direction as each other.",
             "correct": False,
             "why": "If they all went one way the gas would pile up at one "
                    "end of the container. The directions are random."},
            {"text": "Quickly, and in all directions, with no pattern.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e14",
        "band": "easier",
        "text": "What shape does a gas take?",
        "options": [
            {"text": "It fills its container.",
             "correct": True},
            {"text": "It keeps whatever shape it was given at the start.",
             "correct": False,
             "why": "Keeping its own shape is what a solid does. A gas has "
                    "no shape of its own at all."},
            {"text": "It settles into a flat layer at the bottom of the "
                     "container.",
             "correct": False,
             "why": "A flat layer with a surface on top is a liquid. A gas "
                    "goes all the way up to the lid."},
            {"text": "It takes the shape of the lower half of the container "
                     "only.",
             "correct": False,
             "why": "There is no half-full for a gas. However little of it "
                    "there is, it spreads out until it fills the whole "
                    "space."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e15",
        "band": "easier",
        "text": "Which state keeps its own shape, whatever container you put "
                "it in?",
        "options": [
            {"text": "A liquid, because its particles are touching one another all "
                     "the time.",
             "correct": False,
             "why": "A liquid's particles are touching, but they are not "
                    "held in place, so a liquid takes the shape of whatever "
                    "is holding it."},
            {"text": "A gas, because its particles move fastest.",
             "correct": False,
             "why": "Speed is not what fixes a shape, and a gas has no shape "
                    "of its own."},
            {"text": "All three, so long as they are kept cold.",
             "correct": False,
             "why": "Cold does not give a substance a shape. Cold water and "
                    "cold air have no shape of their own."},
            {"text": "A solid, because its particles are held in fixed "
                     "positions.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e16",
        "band": "easier",
        "text": "A gas is moved from a small flask into a much larger sealed "
                "jar. State what happens to the volume it takes up.",
        "options": [
            {"text": "It stays exactly the same as it was in the flask, "
                     "because the amount of gas has not changed.",
             "correct": False,
             "why": "Fixed volume belongs to solids and liquids. The amount "
                    "of gas is the same, but the room it takes up is not."},
            {"text": "It increases — a gas fills whatever it is given.",
             "correct": True},
            {"text": "It falls, because the same gas is now more spread out.",
             "correct": False,
             "why": "More spread out means taking up more room, not less. "
                    "Volume goes up, not down."},
            {"text": "It stays the same, unless the jar is heated as well.",
             "correct": False,
             "why": "No heating is needed. A gas fills its container the "
                    "moment it is put in one, at any temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e17",
        "band": "easier",
        "text": "Which state can be squashed easily into a much smaller "
                "space?",
        "options": [
            {"text": "A solid",
             "correct": False,
             "why": "A solid's particles are already touching, so there is "
                    "no space to remove."},
            {"text": "A liquid",
             "correct": False,
             "why": "A liquid's particles are touching too, which is why a "
                    "sealed syringe of water will not push in."},
            {"text": "A gas",
             "correct": True},
            {"text": "None of the three, if the container is strong enough",
             "correct": False,
             "why": "A strong container is exactly where you squash a gas. "
                    "It gives way easily because most of it is empty space."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e18",
        "band": "easier",
        "text": "The contrast table asks whether each state can be poured. "
                "What does it say for a gas?",
        "options": [
            {"text": "Yes, in exactly the same way that a liquid is poured.",
             "correct": False,
             "why": "Pouring means the substance stays in the new container. "
                    "A gas does not stay put."},
            {"text": "Yes, but only very slowly indeed.",
             "correct": False,
             "why": "Speed is not the problem. However slowly you tip it, a "
                    "gas will not settle in the bottom of a jug."},
            {"text": "No, because a gas is too light to fall out of the "
                     "container.",
             "correct": False,
             "why": "It is not about weight. A gas has mass, and it leaves "
                    "the container because nothing holds its particles "
                    "together."},
            {"text": "It escapes instead.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e19",
        "band": "easier",
        "text": "Mercury is the metal used in old thermometers. What state "
                "is it in at room temperature?",
        "options": [
            {"text": "Solid, because every metal is a solid.",
             "correct": False,
             "why": "Most metals are solids at room temperature, but mercury "
                    "is not. Being a metal does not fix the state."},
            {"text": "Gas, because it rises up the tube of a thermometer.",
             "correct": False,
             "why": "It is pushed up the tube as a liquid. You can see its "
                    "surface, and a gas has no surface."},
            {"text": "Liquid.",
             "correct": True},
            {"text": "Solid, because it has a shiny surface you can see.",
             "correct": False,
             "why": "Plenty of liquids are shiny. Shine tells you nothing "
                    "about how the particles are arranged."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e20",
        "band": "easier",
        "text": "What state is the oxygen in the room around you in?",
        "options": [
            {"text": "Gas.",
             "correct": True},
            {"text": "Liquid, because you cannot see it.",
             "correct": False,
             "why": "Being invisible does not make something a liquid — you "
                    "can see through water perfectly well."},
            {"text": "Solid, because there is a fixed amount of it in the "
                     "room.",
             "correct": False,
             "why": "A fixed amount is not the same as a fixed volume or a "
                    "fixed shape. The oxygen fills the whole room."},
            {"text": "None of the three — oxygen is not a substance you can "
                     "give a state to.",
             "correct": False,
             "why": "Oxygen is an ordinary substance made of particles, and "
                    "like any substance it has a state."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e21",
        "band": "easier",
        "text": "Ice, liquid water and steam are all the same substance. "
                "Which of them is water in the solid state?",
        "options": [
            {"text": "Steam, because you cannot pour it.",
             "correct": False,
             "why": "Steam escapes rather than pours, which is what a gas "
                    "does, not a solid."},
            {"text": "Ice.",
             "correct": True},
            {"text": "None of them — water is only ever a liquid.",
             "correct": False,
             "why": "One substance can take all three states. Water is the "
                    "clearest example there is."},
            {"text": "Liquid water, if it is cold enough to feel cold.",
             "correct": False,
             "why": "Cold water is still a liquid. It pours, and it takes "
                    "the shape of the glass."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e22",
        "band": "easier",
        "text": "A sealed flask holds 1000 particles of a substance as a "
                "liquid. The same sealed flask is later holding that "
                "substance as a gas. How many particles are in it now?",
        "options": [
            {"text": "More than 1000, because a gas takes up more room.",
             "correct": False,
             "why": "Taking up more room is about spacing, not counting. No "
                    "new particles have been made."},
            {"text": "Fewer than 1000, because some are lost as the "
                     "substance spreads out.",
             "correct": False,
             "why": "The flask is sealed, so nothing can leave, and "
                    "particles are not destroyed in any case."},
            {"text": "1000.",
             "correct": True},
            {"text": "It cannot be worked out without knowing the "
                     "temperature.",
             "correct": False,
             "why": "Temperature changes how fast the particles move. It "
                    "never changes how many there are."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e23",
        "band": "easier",
        "text": "One particle of a substance is weighed as part of a solid, "
                "and an identical particle is weighed as part of a gas. "
                "Compare their masses.",
        "options": [
            {"text": "The solid one has more mass, because a solid feels "
                     "heavier in the hand.",
             "correct": False,
             "why": "A solid block feels heavier because its particles are "
                    "packed close together, not because any one of them "
                    "weighs more."},
            {"text": "They are the same.",
             "correct": True},
            {"text": "The gas one has more mass, because it is moving much "
                     "faster.",
             "correct": False,
             "why": "Speed is not mass. A fast particle weighs exactly what "
                    "a slow one weighs."},
            {"text": "The gas one has less mass, because it has spread out "
                     "so thinly.",
             "correct": False,
             "why": "Spreading out changes the spacing between particles and "
                    "leaves each particle exactly as it was."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e24",
        "band": "easier",
        "text": "What does the word state mean in science?",
        "options": [
            {"text": "How hot or cold a substance happens to be at the moment "
                     "you meet it.",
             "correct": False,
             "why": "That is its temperature. Two substances at the same "
                    "temperature can be in different states."},
            {"text": "What a substance is made of, such as water or iron.",
             "correct": False,
             "why": "That is the substance itself. One substance can be in "
                    "any of the three states."},
            {"text": "How pure a sample of a substance is.",
             "correct": False,
             "why": "Purity is about what else is mixed in. A pure sample "
                    "and a dirty one can both be liquids."},
            {"text": "One of the forms a substance can take — solid, liquid "
                     "or gas.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e25",
        "band": "easier",
        "text": "How strongly do the particles in a gas hold on to one "
                "another?",
        "options": [
            {"text": "Hardly at all, which is why they can move apart "
                     "freely.",
             "correct": True},
            {"text": "Very strongly, which is why a gas is so difficult to "
                     "squash.",
             "correct": False,
             "why": "A gas is the easy one to squash, and that is because "
                    "almost nothing holds its particles together."},
            {"text": "Strongly enough to hold them in fixed positions.",
             "correct": False,
             "why": "Fixed positions are a solid. A gas particle is held in "
                    "no position at all."},
            {"text": "Strongly enough to keep them touching, but not in "
                     "rows.",
             "correct": False,
             "why": "Touching but not ordered describes a liquid. A gas's "
                    "particles are far apart."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e26",
        "band": "easier",
        "text": "In which state are the particles held most strongly in "
                "place?",
        "options": [
            {"text": "Solid.",
             "correct": True},
            {"text": "Liquid, because its particles are still touching.",
             "correct": False,
             "why": "Touching is not the same as held in place. A liquid's "
                    "particles slide past one another constantly."},
            {"text": "Gas, because its particles are moving the fastest.",
             "correct": False,
             "why": "Fast movement is the sign of a weak hold, not a strong "
                    "one. A gas's particles are barely held at all."},
            {"text": "They are all held equally, because it is the same "
                     "substance each time.",
             "correct": False,
             "why": "The particles are identical in all three states, but "
                    "how tightly they hold each other is exactly what "
                    "differs."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e27",
        "band": "easier",
        "text": "Complete the sentence. A liquid has a fixed volume "
                "because …",
        "options": [
            {"text": "… its particles are locked into a regular pattern that "
                     "cannot be changed.",
             "correct": False,
             "why": "A liquid has no pattern. A fixed volume comes from the "
                    "particles touching, which they do in a liquid without "
                    "being ordered."},
            {"text": "… it is heavier than the gas above it, so it sinks to "
                     "the bottom.",
             "correct": False,
             "why": "Sinking to the bottom explains where a liquid sits, not "
                    "why the amount of room it takes up never changes."},
            {"text": "… its particles are touching, so there is no space to "
                     "take away or add.",
             "correct": True},
            {"text": "… its particles never move, so the amount of room they "
                     "need stays the same.",
             "correct": False,
             "why": "A liquid's particles move all the time. They keep "
                    "touching while they move, and that is what fixes the "
                    "volume."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e28",
        "band": "easier",
        "text": "A substance takes the shape of the beaker it is poured "
                "into, but it always measures 40 cm³. Name its state.",
        "options": [
            {"text": "Solid, because the volume never changes.",
             "correct": False,
             "why": "A solid's volume is fixed too, but a solid does not "
                    "take the shape of the beaker."},
            {"text": "Liquid.",
             "correct": True},
            {"text": "Gas, because it flowed into the beaker.",
             "correct": False,
             "why": "A gas would not stop at 40 cm³; it would fill the "
                    "beaker and then leave it."},
            {"text": "It could be any of the three from this description.",
             "correct": False,
             "why": "The two facts together pin it down: no shape of its own "
                    "rules out a solid, and a fixed volume rules out a gas."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e29",
        "band": "easier",
        "text": "A substance keeps its own shape and its own volume, "
                "wherever it is put. Name its state.",
        "options": [
            {"text": "Gas.",
             "correct": False,
             "why": "A gas has neither. It fills whatever container it is "
                    "given."},
            {"text": "Liquid.",
             "correct": False,
             "why": "A liquid keeps its volume but not its shape — it takes "
                    "the container's."},
            {"text": "It could be a solid or a liquid.",
             "correct": False,
             "why": "Only one of them keeps its own shape. A liquid takes "
                    "the shape of its container."},
            {"text": "Solid.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e30",
        "band": "easier",
        "text": "A copper pipe is orange-brown, hard and shiny. What colour "
                "is one single copper particle?",
        "options": [
            {"text": "Orange-brown, like the pipe it came from.",
             "correct": False,
             "why": "Colour belongs to the whole pipe, not to one particle. "
                    "A particle is far too small to have a colour."},
            {"text": "Orange-brown only while the copper stays solid.",
             "correct": False,
             "why": "The state makes no difference. A particle has no colour "
                    "in any state."},
            {"text": "Orange-brown, but a much fainter shade, because one "
                     "particle is so very small.",
             "correct": False,
             "why": "Colour does not fade with size, because a single "
                    "particle does not have a colour to fade."},
            {"text": "The question does not apply — a single particle is not "
                     "hard, shiny or coloured at all.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e31",
        "band": "easier",
        "text": "Which of these substances is a solid at room temperature?",
        "options": [
            {"text": "Helium, which is used to fill party balloons.",
             "correct": False,
             "why": "Helium is a gas — it fills the whole balloon rather "
                    "than sitting in the bottom of it."},
            {"text": "Table salt.",
             "correct": True},
            {"text": "Petrol, which is poured into a car at a filling "
                     "station.",
             "correct": False,
             "why": "Being poured from a pump is the giveaway. Petrol is a "
                    "liquid at room temperature."},
            {"text": "Carbon dioxide, which is breathed out by every person "
                     "in the room.",
             "correct": False,
             "why": "Carbon dioxide is a gas at room temperature, which is "
                    "why it leaves your lungs and mixes into the air."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-e32",
        "band": "easier",
        "text": "Compare the spacing of the particles in a solid with the "
                "spacing in a gas of the same substance.",
        "options": [
            {"text": "The spacing is the same; only the speed is "
                     "different.",
             "correct": False,
             "why": "Speed is one of the two things that change. Spacing is "
                    "the other, and it changes enormously."},
            {"text": "The gas's particles are closer together than the "
                     "solid's.",
             "correct": False,
             "why": "That is the wrong way round. A gas is the state with "
                    "the particles furthest apart."},
            {"text": "The gas's particles are much further apart than the "
                     "solid's.",
             "correct": True},
            {"text": "The gas's particles are further apart and also much "
                     "bigger than the solid's.",
             "correct": False,
             "why": "The spacing is right and the size is not. A particle is "
                    "the same size in every state."},
        ],
        "figure": None,
    },
    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c1-02-s10",
        "band": "standard",
        "text": "Explain why a gas can be pushed into a much smaller space "
                "while a liquid cannot.",
        "options": [
            {"text": "A gas is made of much smaller particles than a liquid is, "
                     "so far more of them will fit into the same space.",
             "correct": False,
             "why": "Both are the same particles when it is the same "
                    "substance, and size is never what changes between "
                    "states."},
            {"text": "A gas is lighter, so it needs less push before it "
                     "gives way under the plunger.",
             "correct": False,
             "why": "How heavy it is does not decide it. Mercury is very "
                    "heavy and it still refuses to squash."},
            {"text": "Most of a gas is empty space that can be taken away; a "
                     "liquid's particles are already touching.",
             "correct": True},
            {"text": "A gas is warmer, so its particles move out of the way "
                     "of the plunger more easily.",
             "correct": False,
             "why": "Cold air squashes just as readily as warm air. What "
                    "matters is the empty space, not the temperature."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s11",
        "band": "standard",
        "text": "Explain how a liquid can have a fixed volume and yet no "
                "shape of its own.",
        "options": [
            {"text": "Its particles are ordered, which fixes the volume, and "
                     "light, which lets the shape change.",
             "correct": False,
             "why": "A liquid's particles are not ordered at all, and "
                    "lightness has nothing to do with either property."},
            {"text": "Its volume is fixed only while it is standing still, and "
                     "the shape changes the moment that it is poured out.",
             "correct": False,
             "why": "The volume is fixed while it is being poured as well. "
                    "Standing still is not what fixes it."},
            {"text": "Its particles shrink to fit a narrow container and "
                     "swell again in a wide one.",
             "correct": False,
             "why": "Particles never change size. The same particles fill "
                    "the same volume in whatever shape of container."},
            {"text": "Its particles stay touching, which fixes the volume, "
                     "but are not held in fixed positions, so they flow into "
                     "any shape.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s12",
        "band": "standard",
        "text": "A small amount of gas is released into a large empty sealed "
                "box. Explain why it ends up occupying the whole box.",
        "options": [
            {"text": "Its particles move fast in random directions and "
                     "nothing holds them back, so they end up everywhere.",
             "correct": True},
            {"text": "The walls of the box pull the particles towards them, until "
                     "every corner of the box has some gas in it.",
             "correct": False,
             "why": "Nothing pulls a gas particle to a wall. It simply "
                    "travels until something stops it."},
            {"text": "The empty space in the box sucks the gas outwards to "
                     "fill it.",
             "correct": False,
             "why": "Empty space cannot suck. It is the particles' own "
                    "movement that takes them across the box."},
            {"text": "Each particle grows steadily larger until there is no empty "
                     "space left anywhere inside the box at all.",
             "correct": False,
             "why": "No particle grows. There are just as many, just as big, "
                    "sharing far more room."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s13",
        "band": "standard",
        "text": "A student writes: “A copper particle must be hard, because "
                "you cannot dent a copper coin.” What is wrong with that?",
        "options": [
            {"text": "Nothing — a hard material has to be built from hard "
                     "particles.",
             "correct": False,
             "why": "Hardness comes from how strongly the particles hold on "
                    "to one another, not from any hardness in a single "
                    "particle."},
            {"text": "Hardness belongs to the whole coin. One particle is "
                     "not hard or soft at all.",
             "correct": True},
            {"text": "The coin is hard because its particles have stopped "
                     "moving completely.",
             "correct": False,
             "why": "The particles in the coin vibrate constantly. Hardness "
                    "does not come from stillness."},
            {"text": "The particles are hard, but only while the copper is "
                     "kept in the solid state.",
             "correct": False,
             "why": "A particle is not hard in any state. The state changes "
                    "the arrangement, never the particle."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s14",
        "band": "standard",
        "text": "A student says there must be air in the tiny gaps between "
                "the particles of a solid brick. Explain why that cannot be "
                "right.",
        "options": [
            {"text": "There is air in the gaps, but far too little of it to "
                     "measure.",
             "correct": False,
             "why": "There is none at all. A solid's particles are already "
                    "touching, so there are no gaps for it to be in."},
            {"text": "The air was squeezed out of the gaps when the brick was "
                     "made, and it would come back into them if the brick "
                     "were crushed.",
             "correct": False,
             "why": "It was never there to be squeezed out. Air cannot fit "
                    "between particles that are in contact."},
            {"text": "A solid's particles are touching, so there are no gaps "
                     "— and air is itself made of particles, which would need "
                     "room of their own.",
             "correct": True},
            {"text": "Air only exists outdoors, so there can be none inside "
                     "a brick.",
             "correct": False,
             "why": "Air is indoors as well as out. The reason is the "
                    "particles being in contact, not where the brick is."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s15",
        "band": "standard",
        "text": "A steel girder is measurably longer in summer than in "
                "winter. Explain what has actually got bigger.",
        "options": [
            {"text": "Each iron particle, which swells when it is heated.",
             "correct": False,
             "why": "A particle is the same size at every temperature. "
                    "Heating changes how hard it vibrates, not how big it "
                    "is."},
            {"text": "Nothing — the girder only looks longer because the "
                     "warm air bends the light.",
             "correct": False,
             "why": "The change is real and large enough that bridges are "
                    "built with gaps to allow for it."},
            {"text": "The spaces between the particles, because harder "
                     "vibration needs more room.",
             "correct": True},
            {"text": "The number of particles, because heat adds more of "
                     "them to the steel.",
             "correct": False,
             "why": "Heat is not a substance and adds nothing. The same "
                    "particles are there in August as in January."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s16",
        "band": "standard",
        "text": "250 cm³ of orange juice is poured from a tall bottle into a "
                "wide glass. State what has changed and what has not.",
        "options": [
            {"text": "The volume has changed to fit the glass; the shape is "
                     "unchanged.",
             "correct": False,
             "why": "That is the wrong way round. It is the shape a liquid "
                    "borrows from its container, never the volume."},
            {"text": "The shape has changed; the volume is still 250 cm³.",
             "correct": True},
            {"text": "Both have changed, because the juice is spread out "
                     "over a much wider base.",
             "correct": False,
             "why": "A wider base with a shallower depth is the shape "
                    "changing. The particles are still touching, so 250 cm³ "
                    "stays 250 cm³."},
            {"text": "Neither has changed, because the juice is the same "
                     "substance in both containers.",
             "correct": False,
             "why": "The substance is the same, but the shape is plainly "
                    "not — a tall column has become a wide pool."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s17",
        "band": "standard",
        "text": "A syringe is filled with water and its nozzle is sealed. "
                "The plunger will barely move, however hard it is pushed. "
                "Explain why.",
        "options": [
            {"text": "The particles are touching already, so there is no "
                     "space left to remove.",
             "correct": True},
            {"text": "Water is too heavy for the force of one hand to move "
                     "it any distance.",
             "correct": False,
             "why": "A few grams of water is not heavy. The plunger stops "
                    "because there is nothing to squash out."},
            {"text": "The particles are locked in a regular pattern that "
                     "cannot be pressed any tighter together.",
             "correct": False,
             "why": "A liquid has no pattern to lock. It resists because "
                    "its particles are in contact, which needs no order at "
                    "all."},
            {"text": "The water particles push back harder than they are "
                     "pushed, so nothing can ever compress them.",
             "correct": False,
             "why": "Nothing pushes back harder than it is pushed. The "
                    "plunger stops because the particles are already "
                    "touching."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s18",
        "band": "standard",
        "text": "An unknown substance fills every corner of its sealed "
                "container, and can then be pressed into a quarter of that "
                "space. Deduce its state.",
        "options": [
            {"text": "Gas.",
             "correct": True},
            {"text": "Liquid, because it moved to fill the container.",
             "correct": False,
             "why": "A liquid takes the shape of the bottom of a container "
                    "but does not fill the corners at the top, and it will "
                    "not press into a quarter of the space."},
            {"text": "Solid, because it was strong enough to hold together "
                     "under the pressing.",
             "correct": False,
             "why": "A solid would not fill the container in the first "
                    "place, and it barely squashes at all."},
            {"text": "Either a liquid or a gas, since both of them flow.",
             "correct": False,
             "why": "Being squashed to a quarter separates them. A liquid's "
                    "particles are touching and will not give way like "
                    "that."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s19",
        "band": "standard",
        "text": "At room temperature bromine is a liquid and iodine is a "
                "solid. What does that tell you about the two substances?",
        "options": [
            {"text": "Iodine particles are much bigger, which is why they "
                     "cannot slide.",
             "correct": False,
             "why": "Size is not what sets a state. The comparison is about "
                    "how tightly each substance holds its own particles."},
            {"text": "Iodine's particles hold on to one another strongly "
                     "enough to stay in fixed positions at room temperature; "
                     "bromine's do not.",
             "correct": True},
            {"text": "Iodine is kept at a lower temperature than the bromine "
                     "standing next to it on the bench, which is what keeps "
                     "it solid.",
             "correct": False,
             "why": "Both are at room temperature — that is the point of "
                    "the comparison. The difference is inside the "
                    "substances."},
            {"text": "Bromine's particles have stopped vibrating, so they "
                     "are free to flow.",
             "correct": False,
             "why": "Flowing needs more movement, not less. A liquid's "
                    "particles are moving at least as much as a solid's."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s20",
        "band": "standard",
        "text": "The same number of particles of one substance is held once "
                "as a liquid and once as a gas. Compare the room each takes "
                "up, and explain the difference.",
        "options": [
            {"text": "The same, because the number of particles is the same "
                     "in both.",
             "correct": False,
             "why": "The count is the same but the spacing is not, and it is "
                    "the spacing that sets the volume."},
            {"text": "The liquid takes far more room, because its particles are "
                     "much heavier and sink down into a bigger pile.",
             "correct": False,
             "why": "The particles are identical, and the liquid is the "
                    "compact one — its particles are in contact."},
            {"text": "The gas takes only slightly more room, because each of its "
                     "particles has grown a little larger than before.",
             "correct": False,
             "why": "Particles do not grow, and the difference is not "
                    "slight — a gas takes hundreds of times more room."},
            {"text": "The gas takes far more room, because its particles are "
                     "spread out with empty space between them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s21",
        "band": "standard",
        "text": "A student draws a liquid as particles touching in neat "
                "regular rows. Explain the error.",
        "options": [
            {"text": "The particles should be drawn much smaller than in the "
                     "solid drawing.",
             "correct": False,
             "why": "Size is never the error. The particles are identical in "
                    "all three states."},
            {"text": "The particles should have gaps between them, as they "
                     "do in a solid.",
             "correct": False,
             "why": "There are no gaps in a solid either. Both states have "
                    "their particles in contact."},
            {"text": "The rows are wrong: a liquid's particles touch but are "
                     "jumbled, which is what lets them slide.",
             "correct": True},
            {"text": "The rows are right, but they should be drawn much further "
                     "apart from one another than they are in a solid.",
             "correct": False,
             "why": "Both parts are wrong. A liquid has no rows, and its "
                    "particles are as close together as a solid's."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s22",
        "band": "standard",
        "text": "A student draws a solid as neat rows of particles with wide "
                "gaps between them. Explain the error.",
        "options": [
            {"text": "The rows should be jumbled up instead, and the gaps between "
                     "the particles are correct as drawn.",
             "correct": False,
             "why": "Both halves are wrong. The rows are the one part the "
                    "student got right, and the gaps are the mistake."},
            {"text": "The rows are right, but the particles should be "
                     "touching, with nothing between them.",
             "correct": True},
            {"text": "The gaps are right, but they should be filled in with "
                     "air.",
             "correct": False,
             "why": "There are no gaps, and if there were, air could not sit "
                    "in them — air is itself made of particles needing room "
                    "of their own."},
            {"text": "The particles should be drawn very much larger, so that "
                     "they fill in the gaps left between the rows.",
             "correct": False,
             "why": "Growing the particles is not the fix. They should be "
                    "drawn the same size, moved together until they touch."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s23",
        "band": "standard",
        "text": "Explain why the volume of a solid does not change when it "
                "is moved from a small box into a large one.",
        "options": [
            {"text": "Its particles are in fixed positions and touching, so "
                     "the room they need cannot change.",
             "correct": True},
            {"text": "Its particles cannot move at all, so nothing about it "
                     "can change.",
             "correct": False,
             "why": "They move constantly — they vibrate. What they cannot "
                    "do is leave their positions."},
            {"text": "It has no room to expand into inside the small box, "
                     "and forgets to expand in the large one.",
             "correct": False,
             "why": "A solid does not expand into whatever room it is "
                    "given. That is a gas."},
            {"text": "The larger box is colder, so the solid stays the size "
                     "it was.",
             "correct": False,
             "why": "Nothing was said about temperature, and a solid keeps "
                    "its volume in a warm box as well as a cold one."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s24",
        "band": "standard",
        "text": "A drawing shows particles touching one another in a jumble. "
                "What single change would turn it into a drawing of the same "
                "substance as a solid?",
        "options": [
            {"text": "Draw the particles smaller, keeping them touching.",
             "correct": False,
             "why": "Size is never the difference between two states. The "
                    "particles are identical."},
            {"text": "Move the particles much further apart from one "
                     "another.",
             "correct": False,
             "why": "That turns the jumble into a gas. A solid's particles "
                    "are as close together as a liquid's."},
            {"text": "Tidy them into a regular repeating pattern, still "
                     "touching.",
             "correct": True},
            {"text": "Add more particles until the box is completely full of "
                     "them.",
             "correct": False,
             "why": "The number of particles does not change between states, "
                    "and the box is already full — the change needed is the "
                    "arrangement."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s25",
        "band": "standard",
        "text": "Explain why you can walk straight through the air in a room "
                "but not through the wall at the end of it.",
        "options": [
            {"text": "Air particles are far smaller than the particles in the "
                     "wall are, so they simply slip out of your way as you "
                     "walk through.",
             "correct": False,
             "why": "It is not about particle size. What matters is that a "
                    "gas's particles are far apart and free to move."},
            {"text": "Air has no particles in it at all, so there is nothing "
                     "there to stop you.",
             "correct": False,
             "why": "Air is a gas made of particles. There are simply very "
                    "few of them in your way, and none of them is held in "
                    "place."},
            {"text": "The wall is colder, so its particles have stopped and "
                     "cannot get out of the way.",
             "correct": False,
             "why": "The wall's particles vibrate whatever its temperature. "
                    "They stay in fixed positions, which is what stops you."},
            {"text": "Air is mostly empty space and nothing holds its particles "
                     "in place; the wall's particles are touching and held in "
                     "fixed positions.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s26",
        "band": "standard",
        "text": "Explain why a gas has no fixed volume of its own.",
        "options": [
            {"text": "Because a gas is far lighter than the liquid it came from, "
                     "so it drifts about instead of settling anywhere.",
             "correct": False,
             "why": "Weight does not set a volume. Even a heavy gas fills "
                    "the whole of its container."},
            {"text": "Because its particles are constantly being made and "
                     "destroyed as it moves about.",
             "correct": False,
             "why": "Particles are not made or destroyed. The same ones "
                    "simply take up whatever room they are given."},
            {"text": "Because nothing holds its particles together, so they "
                     "keep moving until the container stops them.",
             "correct": True},
            {"text": "Because each particle expands to fill any container it "
                     "is put into.",
             "correct": False,
             "why": "A particle never changes size. The gas fills the "
                    "container by spreading its particles out, not by "
                    "growing them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s27",
        "band": "standard",
        "text": "As a gas, a substance can take up around a thousand times "
                "the room it takes up as a liquid, with the same particles. "
                "Explain how that is possible.",
        "options": [
            {"text": "Nearly all of the gas is empty space between "
                     "particles, and there is almost none in the liquid.",
             "correct": True},
            {"text": "The particles have each grown about a thousand times "
                     "bigger.",
             "correct": False,
             "why": "A particle is the same size in both states. What has "
                    "grown is the space between them."},
            {"text": "About a thousand times more particles are present in "
                     "the gas.",
             "correct": False,
             "why": "The question says the particles are the same ones. The "
                    "count has not changed at all."},
            {"text": "The gas particles are moving so fast that they blur "
                     "and appear to take up more space than they do.",
             "correct": False,
             "why": "The extra volume is real, not an appearance. You can "
                    "measure it with a syringe."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s28",
        "band": "standard",
        "text": "A student argues that a gas must have no mass, because "
                "nearly all of it is empty space. Evaluate that argument.",
        "options": [
            {"text": "It is correct: empty space has no mass, so neither "
                     "does the gas as a whole.",
             "correct": False,
             "why": "The space contributes nothing, but the particles in it "
                    "still do. A sealed flask of air weighs more than the "
                    "same flask emptied."},
            {"text": "It is correct, because a gas floats upwards instead of ever "
                     "pressing down on the pan of a balance.",
             "correct": False,
             "why": "Not every gas rises, and rising is not the same as "
                    "having no mass."},
            {"text": "It is wrong, because a gas is not really mostly empty space "
                     "at all once you look at it closely.",
             "correct": False,
             "why": "The conclusion is right but the reason is not. A gas "
                    "really is almost entirely empty space — that space "
                    "simply weighs nothing, while the particles in it do."},
            {"text": "It is wrong: the empty space adds nothing, but the "
                     "particles have mass, so the gas has mass.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s29",
        "band": "standard",
        "text": "The Volume row of the contrast table gives the same answer "
                "for two of the three states. Which two, and why?",
        "options": [
            {"text": "Liquid and gas, because both of them flow.",
             "correct": False,
             "why": "Flowing is about shape, not volume. A gas has no fixed "
                    "volume at all."},
            {"text": "Solid and liquid, because in both the particles are "
                     "touching, so the room needed cannot change.",
             "correct": True},
            {"text": "Solid and gas, because both of them are usually kept stored "
                     "inside sealed containers of one kind or another.",
             "correct": False,
             "why": "Where a substance is kept is not a property of its "
                    "state, and a gas has no fixed volume."},
            {"text": "Solid and liquid, because in both of them the particles are "
                     "held in one regular repeating pattern.",
             "correct": False,
             "why": "The pair is right but the reason is not. A liquid has "
                    "no pattern; what the two share is their particles being "
                    "in contact."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s30",
        "band": "standard",
        "text": "A student says the particles in a brick must be still, "
                "because the brick has not moved all morning. Explain what "
                "the student has confused.",
        "options": [
            {"text": "Whether the whole brick moves and whether its "
                     "particles move are different questions: the particles "
                     "vibrate about fixed positions.",
             "correct": True},
            {"text": "Nothing — the brick is not moving, so nothing inside "
                     "it is moving either.",
             "correct": False,
             "why": "A still brick is full of vibrating particles. Stillness "
                    "on the outside says nothing about the inside."},
            {"text": "The particles are still now, but they would start to move "
                     "about inside the brick the moment somebody picked the "
                     "whole brick up.",
             "correct": False,
             "why": "They were moving all along. Picking the brick up "
                    "changes nothing about the vibration."},
            {"text": "The particles are still in the middle of the brick but "
                     "moving at its surface.",
             "correct": False,
             "why": "Every particle in the brick vibrates, wherever it "
                    "sits."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s31",
        "band": "standard",
        "text": "Compare what the forces between particles are doing in a "
                "solid and in a gas.",
        "options": [
            {"text": "In a solid they hold the particles still; in a gas "
                     "they push the particles apart.",
             "correct": False,
             "why": "Nothing is held still in a solid — the particles "
                    "vibrate — and nothing pushes a gas apart. Its particles "
                    "simply keep moving."},
            {"text": "In both they hold the particles in contact, but only "
                     "the solid's are ordered.",
             "correct": False,
             "why": "That compares a solid with a liquid. A gas's particles "
                    "are not in contact at all."},
            {"text": "In a gas they hold the particles together tightly; in a "
                     "solid they are weak enough to let the particles pass "
                     "by.",
             "correct": False,
             "why": "This has the two states swapped. The strong hold is the "
                    "solid's."},
            {"text": "In a solid they are strong enough to keep every "
                     "particle in its own position; in a gas they are far too "
                     "weak to hold anything.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-s32",
        "band": "standard",
        "text": "Describe what one particular particle in a glass of water "
                "is doing over the next second.",
        "options": [
            {"text": "Sitting quite still in one place, waiting for the water to "
                     "be poured out or stirred round with a spoon.",
             "correct": False,
             "why": "It does not wait. A liquid's particles are moving "
                    "whether the glass is disturbed or not."},
            {"text": "Vibrating about one fixed position and never leaving "
                     "it.",
             "correct": False,
             "why": "That is what a particle in ice does. In liquid water a "
                    "particle changes place."},
            {"text": "Moving among its neighbours, staying in contact with "
                     "others but not staying next to the same ones.",
             "correct": True},
            {"text": "Flying right across the glass in long straight lines, and "
                     "bouncing off the sides whenever it arrives.",
             "correct": False,
             "why": "Long free flights belong to a gas. In a liquid a "
                    "particle is hemmed in by the ones touching it."},
        ],
        "figure": None,
    },
    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-02-h10",
        "band": "harder",
        "text": "1 cm³ of liquid water contains the same particles as about "
                "1700 cm³ of steam. Roughly what fraction of that steam is "
                "actually particle rather than empty space?",
        "options": [
            {"text": "About a half of it, since the particles are still "
                     "quite crowded.",
             "correct": False,
             "why": "A half would make steam about twice the volume of the "
                    "water, not seventeen hundred times."},
            {"text": "All of it, because the particles have swollen to fill "
                     "the larger volume.",
             "correct": False,
             "why": "Particles do not swell. The extra volume is empty "
                    "space, not bigger particles."},
            {"text": "About a tenth of it.",
             "correct": False,
             "why": "A tenth would give only ten times the volume. The "
                    "figure of 1700 tells you the particles occupy far less "
                    "than that."},
            {"text": "About one part in 1700.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h11",
        "band": "harder",
        "text": "A foam sponge keeps its own shape yet can be squeezed into "
                "a fraction of its size. Does that disprove the rule that a "
                "solid cannot be squashed?",
        "options": [
            {"text": "Yes — the rule only works for hard solids such as "
                     "metals and stone.",
             "correct": False,
             "why": "It works for the foam as well. The rule is about the "
                    "particles, and the foam's particles do not compress "
                    "either."},
            {"text": "No — what is squashed is the air in the holes; the solid "
                     "parts of the foam squash no more than any other "
                     "solid.",
             "correct": True},
            {"text": "Yes — the foam is built from unusually soft particles, so "
                     "each of them flattens under the pressure of a hand.",
             "correct": False,
             "why": "No particle is soft, in any material. Softness belongs "
                    "to the structure, not to the particle."},
            {"text": "No — the foam is really a gas held inside a shape, because "
                     "nothing but a gas can be squashed as far as that.",
             "correct": False,
             "why": "The foam keeps its own shape and springs back, which no "
                    "gas does. It is a solid with gas trapped inside it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h12",
        "band": "harder",
        "text": "A diamond cannot be scratched and a rubber band stretches "
                "easily, yet both are solids. Explain how the model allows "
                "that.",
        "options": [
            {"text": "The rubber is partly liquid, which is what lets it "
                     "stretch out of shape.",
             "correct": False,
             "why": "A stretched band still keeps its own shape and springs "
                    "back to it. Nothing in it is flowing."},
            {"text": "The rubber's particles have escaped their fixed positions "
                     "and slide past one another, so the band is on its way "
                     "to becoming a liquid as you pull on it.",
             "correct": False,
             "why": "If they had escaped, the band would flow into the shape "
                    "of whatever held it and stay there."},
            {"text": "Being a solid says the particles keep fixed positions "
                     "in the material; how strongly they are held, and in "
                     "what structure, still varies between substances.",
             "correct": True},
            {"text": "Diamond particles are much larger than rubber "
                     "particles, so they cannot be pushed past each other.",
             "correct": False,
             "why": "Particle size never explains a state or a property like "
                    "this. Both materials keep their particles in place."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h13",
        "band": "harder",
        "text": "A balloon is weighed empty, then blown up with air and "
                "weighed again on a sensitive balance. The second reading is "
                "higher. What does that show?",
        "options": [
            {"text": "A gas is made of real particles, each with mass, even "
                     "though most of the balloon is empty space.",
             "correct": True},
            {"text": "The balloon's rubber gained mass as it was stretched "
                     "out.",
             "correct": False,
             "why": "Stretching rearranges the rubber's particles and adds "
                    "none. The extra mass came in through the neck."},
            {"text": "The air particles inside grew larger than the ones "
                     "outside.",
             "correct": False,
             "why": "Particles are the same size inside and out. There are "
                    "simply more of them inside than there were."},
            {"text": "Warm breath is heavier than the ordinary air it pushed out "
                     "of the balloon, so the balance reads higher.",
             "correct": False,
             "why": "The reading rises for a balloon filled from a pump as "
                    "well. It is the particles added that weigh, not their "
                    "warmth."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h14",
        "band": "harder",
        "text": "A student explains that a liquid takes the shape of its "
                "container because its particles are soft and mould "
                "themselves to the walls. Evaluate that explanation.",
        "options": [
            {"text": "It is sound, because something has to change shape for "
                     "the liquid to fit.",
             "correct": False,
             "why": "Something does change shape — the arrangement of the "
                    "crowd. No individual particle changes at all."},
            {"text": "It is wrong: the particles keep their shape and size, "
                     "and it is the crowd that reshapes as they slide over "
                     "one another.",
             "correct": True},
            {"text": "It is wrong, because a liquid does not take the shape of "
                     "the container it is poured into in the first place.",
             "correct": False,
             "why": "It certainly does — that is the row the table gives for "
                    "a liquid. The fault is in the reason, not the "
                    "observation."},
            {"text": "It is sound for thick liquids such as honey, but not "
                     "for thin ones such as water.",
             "correct": False,
             "why": "No liquid has soft particles. Thick and thin describe "
                    "how easily the particles slide, not how squashy they "
                    "are."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h15",
        "band": "harder",
        "text": "A 10-litre steel cylinder can be filled with far more "
                "oxygen than a 10-litre bottle can be filled with water, "
                "counted in particles. Explain why.",
        "options": [
            {"text": "Oxygen particles are far smaller than the particles in "
                     "water, so a great many more of them will fit into the "
                     "cylinder.",
             "correct": False,
             "why": "Particle size is not the reason, and it would be a "
                    "small effect at best. The gas is compressible and the "
                    "liquid is not."},
            {"text": "The cylinder is kept under far more pressure than the "
                     "bottle, and that pressure makes each oxygen particle "
                     "shrink.",
             "correct": False,
             "why": "No particle shrinks under any pressure. What is removed "
                    "is the space between them."},
            {"text": "Gas particles start far apart, so more can be pushed "
                     "in; water's are already touching, so the bottle is full "
                     "at once.",
             "correct": True},
            {"text": "The steel walls attract oxygen particles and hold "
                     "extra ones against them.",
             "correct": False,
             "why": "The steel does no attracting. The room is made by "
                    "removing empty space, which a liquid does not have."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h16",
        "band": "harder",
        "text": "A classroom holds about 30 m³ of air. If every particle in "
                "that air were pushed together until they touched, they would "
                "fill roughly 0.03 m³. Calculate the fraction of the room's "
                "air that is particle.",
        "options": [
            {"text": "About a third of it, which would be about 10 m³.",
             "correct": False,
             "why": "A third of 30 m³ would be 10 m³, not 0.03 m³. Check "
                    "where the decimal point sits."},
            {"text": "About a hundredth of it, which would be 0.3 m³.",
             "correct": False,
             "why": "A hundredth of 30 m³ is 0.3 m³. The figure given is ten "
                    "times smaller than that."},
            {"text": "About a tenth of it, which would be about 3 m³.",
             "correct": False,
             "why": "A tenth of 30 m³ is 3 m³, a hundred times too large. "
                    "Divide 0.03 by 30 to get the fraction."},
            {"text": "About a thousandth of it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h17",
        "band": "harder",
        "text": "Evaluate this proposed definition: “A liquid is any "
                "substance that flows.”",
        "options": [
            {"text": "It is a poor definition, because a gas flows as well, "
                     "and a poured powder flows without being a liquid.",
             "correct": True},
            {"text": "It is a good definition, because no other state of matter is "
                     "able to flow from one container into another.",
             "correct": False,
             "why": "A gas flows out of a container readily, and a powder "
                    "pours as well. Flowing alone does not pick out a "
                    "liquid."},
            {"text": "It is a poor definition, because a liquid does not "
                     "really flow at all.",
             "correct": False,
             "why": "A liquid does flow — that is the one part of the "
                    "definition that is true. The fault is that other things "
                    "flow too."},
            {"text": "It is a good definition, so long as the substance being "
                     "described is at room temperature when it is tested.",
             "correct": False,
             "why": "Temperature does not repair it. Air flows at room "
                    "temperature and is not a liquid."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h18",
        "band": "harder",
        "text": "Three sealed jars are described. A keeps its own shape; B "
                "settles flat with a surface and measures 60 cm³ wherever it "
                "is poured; C fills every corner of its jar. Name the states "
                "of A, B and C.",
        "options": [
            {"text": "A solid, B gas, C liquid.",
             "correct": False,
             "why": "B has a fixed volume and a surface, which no gas has, "
                    "and C fills the corners, which no liquid does. B and C "
                    "are the wrong way round."},
            {"text": "A liquid, B solid, C gas.",
             "correct": False,
             "why": "Keeping its own shape is a solid, not a liquid, and B's "
                    "pouring rules a solid out."},
            {"text": "A solid, B liquid, C gas.",
             "correct": True},
            {"text": "All three could be solids, since a powder can be "
                     "poured and can fill a jar.",
             "correct": False,
             "why": "A poured powder does fill the bottom of a jar, but it "
                    "does not fill the corners at the top, and A keeps a "
                    "shape a powder would lose."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h19",
        "band": "harder",
        "text": "For the same substance, which state needs the stronger hold "
                "between its particles, solid or liquid, and why?",
        "options": [
            {"text": "The solid, because a hold that only keeps particles "
                     "touching is not enough — it must also keep each one in "
                     "its own position.",
             "correct": True},
            {"text": "The liquid, because its particles are moving about and "
                     "need holding back.",
             "correct": False,
             "why": "The solid's particles are held far more tightly, which "
                    "is exactly why they cannot move about."},
            {"text": "Neither, because the hold is a property of the "
                     "substance and cannot change.",
             "correct": False,
             "why": "The particles are identical, but how firmly they are "
                    "held depends on how much energy they have — and that "
                    "is what separates the two states."},
            {"text": "The liquid, because it is the denser of the two states and "
                     "so it needs a stronger hold to keep all of that mass "
                     "together.",
             "correct": False,
             "why": "For nearly every substance the solid is the denser one, "
                    "and density is not what the hold is measured by."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h20",
        "band": "harder",
        "text": "A student writes that steam differs from liquid water in "
                "two ways: its particles have more space around them, and "
                "each particle is larger. Which part is right?",
        "options": [
            {"text": "Both parts are right, and together they are why steam takes "
                     "up so much more room than water does.",
             "correct": False,
             "why": "Only the spacing is right, and the spacing alone is "
                    "enough to account for all of the extra volume."},
            {"text": "Only the first part. The spacing changes; the "
                     "particles are identical in both.",
             "correct": True},
            {"text": "Only the second part. The size changes; the spacing "
                     "stays the same.",
             "correct": False,
             "why": "This is the wrong way round twice over. Particles never "
                    "change size, and the spacing changes enormously."},
            {"text": "Neither part. What changes between the two is the "
                     "number of particles present.",
             "correct": False,
             "why": "The number is unchanged, and the spacing certainly does "
                    "change — the first part of the student's answer was "
                    "sound."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h21",
        "band": "harder",
        "text": "A rigid sealed steel can holds air. The can is warmed, so "
                "the air particles move faster. Has the gas inside expanded?",
        "options": [
            {"text": "Yes, because each particle has expanded in the heat.",
             "correct": False,
             "why": "Heating never enlarges a particle. It only makes it "
                    "move faster."},
            {"text": "Yes, because a gas always expands when it is heated, "
                     "whatever container it happens to be shut inside.",
             "correct": False,
             "why": "A gas expands when it is heated only if it has room to "
                    "expand into. This can gives it none."},
            {"text": "No, because heating a gas has no effect at all on what its "
                     "particles are doing inside the can.",
             "correct": False,
             "why": "It has a large effect: the particles move considerably "
                    "faster. What cannot change is the volume they are shut "
                    "inside."},
            {"text": "No — the can's volume is fixed, so the same particles "
                     "occupy the same space, moving faster.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h22",
        "band": "harder",
        "text": "A student's table gives a liquid's shape as “takes the "
                "container's” and its volume as “takes the container's” too. "
                "Identify the error and give the correction.",
        "options": [
            {"text": "The volume is wrong: a liquid's volume is fixed, "
                     "because its particles stay in contact.",
             "correct": True},
            {"text": "The shape is wrong: a liquid keeps its own shape wherever "
                     "it is put, because its particles are touching.",
             "correct": False,
             "why": "Keeping its own shape is a solid. The shape entry was "
                    "the half the student got right."},
            {"text": "Neither is wrong, because a liquid poured into a wider "
                     "dish covers a larger area.",
             "correct": False,
             "why": "Covering a larger area more thinly is the shape "
                    "changing. Measure the liquid and the volume is what it "
                    "always was."},
            {"text": "Both are wrong: a liquid keeps its own shape and its "
                     "volume grows to fit the container.",
             "correct": False,
             "why": "This swaps the two entries rather than fixing one. The "
                    "shape entry was already correct."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h23",
        "band": "harder",
        "text": "Granite cannot be dented with a thumb and butter can, and "
                "both are solids at room temperature. Does butter belong in a "
                "different state?",
        "options": [
            {"text": "Yes, butter is really a very thick liquid, because it "
                     "gives way when pressed.",
             "correct": False,
             "why": "Take the thumb away and the dent stays. A liquid would "
                    "flow back level and take the dish's shape."},
            {"text": "Yes, butter is between two states, because its particles "
                     "are half held in their positions and half free to "
                     "slide, which is why a thumb dents it.",
             "correct": False,
             "why": "There is no halfway box in this model, and butter "
                    "behaves as a solid: it keeps whatever shape it is "
                    "given."},
            {"text": "No, because butter has a fixed volume, and only "
                     "volume decides a state.",
             "correct": False,
             "why": "The conclusion is right but the reason is not — a "
                    "liquid has a fixed volume too. It is keeping its own "
                    "shape that settles it."},
            {"text": "No — butter keeps its own shape, including the dent, "
                     "so its particles are in fixed positions; a weaker hold "
                     "makes a softer solid, not another state.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h24",
        "band": "harder",
        "text": "500 cm³ of air has a mass of about 0.6 g. Calculate the "
                "mass of 5 litres of the same air.",
        "options": [
            {"text": "0.6 g, because a gas spread through a larger space "
                     "still weighs what it did.",
             "correct": False,
             "why": "That would be true for the same air moved into a bigger "
                    "jar. Here there is ten times as much air, so ten times "
                    "the mass."},
            {"text": "6 g.",
             "correct": True},
            {"text": "0.06 g, because the air is more thinly spread in the "
                     "larger volume.",
             "correct": False,
             "why": "This divides where it should multiply. Five litres is "
                    "5000 cm³, which is ten times 500 cm³."},
            {"text": "300 g, taking 5 litres as 5000 cm³ and multiplying by "
                     "0.6 g for every 10 cm³.",
             "correct": False,
             "why": "The 0.6 g belongs to 500 cm³, not to 10 cm³. Divide "
                    "5000 by 500 to get the factor of ten."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h25",
        "band": "harder",
        "text": "Predict which state of a given substance would have the "
                "greatest number of particles in 1 cm³, and by roughly how "
                "much compared with its gas.",
        "options": [
            {"text": "The gas, and by a very large margin indeed, because its "
                     "particles are the ones that are free to move about.",
             "correct": False,
             "why": "Free movement needs room. The gas is the state with "
                    "fewest particles in a given volume, not most."},
            {"text": "All three would be about equal, since the particles "
                     "are identical in every state.",
             "correct": False,
             "why": "Identical particles can still be packed very "
                    "differently, and that is the whole point of the three "
                    "states."},
            {"text": "The solid, by a factor of roughly a thousand, because "
                     "its particles are touching rather than spread out.",
             "correct": True},
            {"text": "The solid, but only by a few per cent, because a liquid and "
                     "a gas are packed nearly as tightly as it is.",
             "correct": False,
             "why": "The solid and the liquid are within a few per cent of "
                    "each other. It is the gas that is out by a factor of "
                    "about a thousand."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h26",
        "band": "harder",
        "text": "An unknown substance pours from one beaker to another and "
                "always measures 40 cm³. Put into a sealed syringe, the "
                "plunger will not move. Deduce its state, giving two reasons.",
        "options": [
            {"text": "A gas: it flowed freely from one beaker into the other, and "
                     "a gas will not squash any further once the syringe has "
                     "been sealed up tight.",
             "correct": False,
             "why": "Both halves are wrong. A gas has no fixed volume, and a "
                    "sealed syringe of gas squashes readily."},
            {"text": "A solid: the volume is fixed, and the plunger will not "
                     "move.",
             "correct": False,
             "why": "Those two facts fit a solid, but a solid does not pour "
                    "from beaker to beaker keeping a measured volume."},
            {"text": "Not enough evidence: those observations fit both a "
                     "liquid and a solid equally.",
             "correct": False,
             "why": "The pouring separates them. A solid keeps its own "
                    "shape, so it would not settle to 40 cm³ in each "
                    "beaker."},
            {"text": "A liquid: it takes the shape of each beaker, so it is "
                     "not a solid, and it keeps a fixed volume and will not "
                     "compress, so it is not a gas.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h27",
        "band": "harder",
        "text": "Compare a liquid and a gas by how much of the space they "
                "occupy is actually filled by particles.",
        "options": [
            {"text": "In a liquid nearly all of it is particle; in a gas "
                     "nearly all of it is empty space.",
             "correct": True},
            {"text": "In both of them, about half is particle and the other half "
                     "is empty space between the particles.",
             "correct": False,
             "why": "A liquid's particles are touching, leaving next to "
                    "nothing empty, and a gas is emptier still than half."},
            {"text": "In a liquid nearly all of it is empty space, and in a gas "
                     "nearly all of it is solid particle.",
             "correct": False,
             "why": "This has the two states swapped. The gas is the one "
                    "that is almost entirely empty."},
            {"text": "In both of them nearly all is particle, but only the gas's "
                     "particles are moving about.",
             "correct": False,
             "why": "The movement is right, but the packing is not. Almost "
                    "all of a gas is empty space, which is why it squashes."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h28",
        "band": "harder",
        "text": "You are given three drawings of the same amount of one "
                "substance, one for each state. State what must be identical "
                "in all three.",
        "options": [
            {"text": "The total area that each of the three drawings covers on "
                     "the page.",
             "correct": False,
             "why": "The gas drawing should cover far more room than the "
                    "solid one. It is the particles that must match, not the "
                    "box."},
            {"text": "The pattern that the particles have been drawn in.",
             "correct": False,
             "why": "The pattern is one of the two things that must differ. "
                    "Only the solid is drawn in regular rows."},
            {"text": "The size of each particle and the number of them.",
             "correct": True},
            {"text": "The spacing left between one particle and its neighbours.",
             "correct": False,
             "why": "The spacing is the other thing that must differ — it is "
                    "what makes the gas drawing look so empty."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h29",
        "band": "harder",
        "text": "Suggest why a liquid in a beaker has a flat surface you can "
                "point to, while a gas in the same beaker has none.",
        "options": [
            {"text": "The gas has no surface because it is invisible, so "
                     "there is nothing there to point at.",
             "correct": False,
             "why": "A coloured gas is visible and still has no surface. "
                    "Being seen is not the issue."},
            {"text": "The liquid's particles are held in contact, so the "
                     "crowd ends somewhere; the gas's are not held at all, so "
                     "they carry on to the walls.",
             "correct": True},
            {"text": "The liquid's particles are heavier, so they fall to "
                     "the bottom and stack up neatly.",
             "correct": False,
             "why": "The particles have the same mass in both states. What "
                    "differs is whether anything holds them together."},
            {"text": "The gas has a surface of its own as well, but it sits right "
                     "up at the very top of the beaker, where nobody can see "
                     "it.",
             "correct": False,
             "why": "There is no boundary there. The gas simply continues to "
                    "the walls and out of the top."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h30",
        "band": "harder",
        "text": "Evaluate this test for whether a sample is a gas: put it "
                "into a larger sealed container and see whether it fills the "
                "new space.",
        "options": [
            {"text": "It is a poor test, because a liquid would fill the "
                     "larger container too.",
             "correct": False,
             "why": "A liquid would not. It would settle in the bottom, "
                    "keeping the volume it had."},
            {"text": "It is a sound test, because only a gas fills whatever "
                     "space it is given.",
             "correct": True},
            {"text": "It is a poor test, because a gas would stay the "
                     "volume it was and leave the rest of the container "
                     "empty.",
             "correct": False,
             "why": "That describes a liquid. A gas has no volume of its own "
                    "to keep."},
            {"text": "It is a sound test, but only for gases that can be "
                     "seen, since otherwise you cannot tell.",
             "correct": False,
             "why": "The test does not depend on seeing anything — you can "
                    "measure or detect the substance at the far end of the "
                    "container."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h31",
        "band": "harder",
        "text": "Explain, in terms of the hold between particles, why the "
                "same substance has a fixed volume as a liquid but not as a "
                "gas.",
        "options": [
            {"text": "As a liquid the hold is strong enough to keep the "
                     "particles touching each other; as a gas it is too weak "
                     "to keep them together at all.",
             "correct": True},
            {"text": "As a liquid the hold fixes each particle in a "
                     "position; as a gas the hold fixes nothing.",
             "correct": False,
             "why": "A liquid's particles are not fixed in position — they "
                    "slide. The hold keeps them in contact, which is enough "
                    "to fix the volume."},
            {"text": "As a liquid the particles are far too heavy to escape from "
                     "one another; as a gas they have somehow become much "
                     "lighter.",
             "correct": False,
             "why": "Mass does not change between the states. The same "
                    "particles are held differently."},
            {"text": "As a liquid there is no hold, so the particles pack "
                     "down; as a gas the hold pushes them apart.",
             "correct": False,
             "why": "This inverts both. The liquid is the state with the "
                    "stronger hold, and nothing pushes a gas apart."},
        ],
        "figure": None,
    },
    {
        "id": "c1-02-h32",
        "band": "harder",
        "text": "Two sealed flasks each hold the same substance, one as a "
                "solid and one as a gas, and a balance shows exactly the same "
                "mass for both. Compare the number of particles in each.",
        "options": [
            {"text": "The gas flask holds far fewer particles, and each one of "
                     "them must therefore have a much greater mass.",
             "correct": False,
             "why": "The first half is right and the second is not. A "
                    "particle has the same mass in both flasks, so equal "
                    "masses mean equal numbers."},
            {"text": "The solid flask holds far more particles, because a solid "
                     "packs its particles tightly into the space.",
             "correct": False,
             "why": "A solid does pack its particles more tightly into a "
                    "given space, but nothing here says the flasks are the "
                    "same size. Equal masses of identical particles means "
                    "equal numbers."},
            {"text": "It cannot be decided at all without first being told the "
                     "temperature inside each of the two flasks.",
             "correct": False,
             "why": "Temperature changes how fast the particles move. It "
                    "changes neither their mass nor their number."},
            {"text": "The numbers are equal, because the particles are "
                     "identical in both states and the masses match.",
             "correct": True},
        ],
        "figure": None,
    },
]
