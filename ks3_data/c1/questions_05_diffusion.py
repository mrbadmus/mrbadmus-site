"""C1 lesson 05 — Diffusion: twelve questions (MRB-269).

The lesson's argument is that evenness is not aimed at: particles were
already moving, they step with no pattern and no set direction, and a crowd
on one side is the only reason more of them cross one way than the other.
These twelve probe that argument from the sides the ladder leaves alone —
what the traced path actually looks like, what the gap between the two
crossing counters means, what warming changes and what it does not, and what
the distance-and-time panel forces on a body.

The distractors are built from the lesson's two declared misconceptions.
PART-10 (something must push the particles along — a draught, a current, a
waft) drives the wrong options in e02, e04, s02, s04 and h02: every one of
them hands the job to a carrier, a flow or a push. PART-11 (particles move
in order to spread out, or are drawn towards empty space) drives e01, e04,
s02, s03 and h04, where a particle is given a destination it cannot know
about. A third family runs underneath both and is worth naming because a
class converges on it: treating a finished spread as finished movement, and
treating "warmer" as a change of direction or of particle size rather than
of speed — s03, h01 and h04 each carry one.
"""

UNIT = "C1"
LESSON = "diffusion"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-05-e01",
        "band": "easier",
        "text": "On the bench you can turn on \"Follow one particle\" and "
                "watch a single dye particle. What does its path look like?",
        "options": [
            {"text": "A straight line drifting steadily towards the empty "
                     "right-hand side", "correct": False,
             "why": "Nothing is steering the particle towards the empty side. "
                    "A step one way is no more likely than a step any other "
                    "way, so the path never sets off anywhere."},
            {"text": "A tangled path that doubles back on itself constantly, "
                     "heading nowhere", "correct": True},
            {"text": "A smooth curve that bends away from the crowded part of "
                     "the tank", "correct": False,
             "why": "A particle has no information about where the crowd is, "
                    "so nothing could bend its path away from it. Each step is "
                    "taken with no pattern and no set direction."},
            {"text": "A zigzag that still keeps its overall direction to the "
                     "right", "correct": False,
             "why": "A zigzag with an overall direction is still being "
                    "steered. The traced path doubles back as often as it goes "
                    "on — and that tangle is why crossing a few centimetres "
                    "takes so long when the particle itself is fast."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e02",
        "band": "easier",
        "text": "In the still room, a candle flame at the centre stands "
                "perfectly upright. Why does that detail matter?",
        "options": [
            {"text": "It shows there is no air current, so nothing is carrying "
                     "the perfume", "correct": True},
            {"text": "It shows the air is warm, and warm air is what pushes a "
                     "smell outwards", "correct": False,
             "why": "The candle is there to rule a draught out, not to warm "
                    "the room. In a cold, dead-still room the perfume still "
                    "reaches you."},
            {"text": "It shows warm air is rising, and the rising air carries "
                     "the smell across", "correct": False,
             "why": "If air were rising, or moving at all, the flame would "
                    "lean. An upright flame is the evidence that there is no "
                    "current to do any carrying."},
            {"text": "It gives the perfume particles the energy they need to "
                     "start moving", "correct": False,
             "why": "The perfume particles were already moving before anyone "
                    "lit anything — hundreds of metres per second. Nothing has "
                    "to start them off."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e03",
        "band": "easier",
        "text": "The lesson gives the time diffusion alone needs at "
                "different scales. About how long does it take to cross a "
                "fingertip, roughly 10 mm?",
        "options": [
            {"text": "About a hundredth of a second", "correct": False,
             "why": "That is the time across a single cell, 0.01 mm — a "
                    "thousand times shorter. Diffusion falls apart as the "
                    "distance grows."},
            {"text": "About two minutes", "correct": False,
             "why": "Far too fast. Diffusion alone would take days to cross "
                    "a room — draughts and convection do that work — and "
                    "through 10 mm of tissue it is slower still."},
            {"text": "About three hours", "correct": True},
            {"text": "About three seconds", "correct": False,
             "why": "If 10 mm took three seconds you would not need a "
                    "bloodstream at all. Over that distance diffusion is "
                    "already hopeless — it needs about three hours."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e04",
        "band": "easier",
        "text": "Early in a run, the counter for crossings left to right "
                "climbs much faster than the one for crossings right to left. "
                "What causes the difference?",
        "options": [
            {"text": "The particles can sense the empty space on the right and "
                     "head for it", "correct": False,
             "why": "A particle has no information about the rest of the tank "
                    "and no way to prefer one direction. Nothing is sensed, "
                    "and nothing is aimed at."},
            {"text": "The drop of dye pushes the particles ahead of it as it "
                     "expands", "correct": False,
             "why": "There is no push anywhere in this tank. Each particle "
                    "steps on its own, and a step left is exactly as likely as "
                    "a step right."},
            {"text": "Water flows slowly from the crowded side towards the "
                     "emptier side", "correct": False,
             "why": "The tank is sealed and the water is still — there is no "
                    "flow. Nothing moves here except the particles "
                    "themselves."},
            {"text": "There are simply more particles on the left, so more are "
                     "available to cross", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-05-s01",
        "band": "standard",
        "text": "Partway through a run the bench reads 480 crossings left to "
                "right and 310 crossings right to left. How much net movement "
                "of dye is that?",
        "options": [
            {"text": "790 crossings' worth, to the right", "correct": False,
             "why": "Adding the two counters adds in the crossings that "
                    "cancel. The 310 that came back undo 310 of the 480 that "
                    "went across."},
            {"text": "170 crossings' worth, to the right", "correct": True},
            {"text": "480 crossings' worth, to the right", "correct": False,
             "why": "The left-to-right total on its own ignores the 310 that "
                    "went the other way. Net movement is the gap between the "
                    "two counters, not the bigger one."},
            {"text": "None — the two counters cancel and nothing is spreading",
             "correct": False,
             "why": "They would cancel only if the totals matched. A gap of "
                    "170 is real net movement, and that gap is the whole of "
                    "diffusion."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s02",
        "band": "standard",
        "text": "A student writes: \"The dye moves right because the "
                "right-hand side is empty, and particles are attracted towards "
                "empty space.\" What is wrong with it?",
        "options": [
            {"text": "Nothing — the dye does move towards the empty side, so "
                     "the sentence fits", "correct": False,
             "why": "It matches what you see, which is exactly why it is the "
                    "sentence almost everyone writes. It is still wrong: "
                    "nothing about a particle can respond to where the empty "
                    "space is."},
            {"text": "Only the word 'attracted' — particles actually repel "
                     "each other and push apart", "correct": False,
             "why": "Repelling is just another force doing the pushing, and "
                    "there is no force here at all. Particles that pushed each "
                    "other apart could not sit together as a liquid."},
            {"text": "Nothing attracts a particle — more cross right only "
                     "because more start left", "correct": True},
            {"text": "Only the direction — it is the crowded left-hand side "
                     "that pushes the dye across", "correct": False,
             "why": "Swapping a pull for a push keeps the same mistake. "
                    "Nothing pushes and nothing pulls; the particles were "
                    "already moving before the drop was released."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s03",
        "band": "standard",
        "text": "Halfway through a run you press \"Warm the water\". Which of "
                "these describes what changes and what does not?",
        "options": [
            {"text": "The steps get bigger so the tank evens out sooner; the "
                     "directions stay random", "correct": True},
            {"text": "The particles take bigger steps, and more of them now "
                     "head towards the emptier side", "correct": False,
             "why": "Warming adds speed, not direction. A warm particle is a "
                    "faster random walker, not a better-aimed one."},
            {"text": "The particles swell up, and the bigger particles take up "
                     "more of the tank", "correct": False,
             "why": "Particles do not change size when you warm them. The "
                    "particles are exactly the same; what changes is how fast "
                    "they move."},
            {"text": "The tank evens out sooner, and then the warmed particles "
                     "finally come to rest", "correct": False,
             "why": "Nothing brings a particle to rest, warm or cold. Once the "
                    "tank is even the crossings carry on both ways — faster "
                    "than before, not stopped."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s04",
        "band": "standard",
        "text": "Your blood is never more than a fraction of a millimetre "
                "from any cell in your body. Which fact about diffusion forces "
                "that arrangement?",
        "options": [
            {"text": "Blood has to push the oxygen into the cells, and a push "
                     "does not carry far", "correct": False,
             "why": "Nothing pushes in diffusion. The blood's job is to bring "
                    "oxygen close; the last stretch happens by random movement "
                    "alone."},
            {"text": "Diffusion only works in gases, so oxygen must arrive as "
                     "a gas first", "correct": False,
             "why": "Diffusion works in liquids too — that is the entire dye "
                    "tank. It is slower in a liquid, which is the reason for "
                    "the short distance, not a reason it cannot happen."},
            {"text": "Cells cannot store oxygen, so a fresh supply has to "
                     "arrive continuously", "correct": False,
             "why": "Cells do use oxygen continuously, but that says nothing "
                    "about how far away the supply may sit. What rules here is "
                    "that 10 mm would take about three hours."},
            {"text": "Diffusion is unbeatable over tiny distances and hopeless "
                     "over long ones", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-05-h01",
        "band": "harder",
        "text": "A chemical diffuses across a 0.2 mm layer of jelly in 4 "
                "seconds. Roughly how long would it take across 0.4 mm of the "
                "same jelly?",
        "options": [
            {"text": "About 8 seconds — the distance has doubled",
             "correct": False,
             "why": "This is the trap the lesson warns about. Double the "
                    "distance and diffusion takes four times as long, not "
                    "twice, so 8 seconds is far too quick."},
            {"text": "About 4 seconds — the time does not depend on distance",
             "correct": False,
             "why": "Distance is the one thing diffusion is worst at. Across a "
                    "cell it takes under a millisecond; across a fingertip, "
                    "three hours."},
            {"text": "About 16 seconds — doubling the distance quadruples the "
                     "time", "correct": True},
            {"text": "About 2 seconds — the chemical has spread out, so it "
                     "moves more freely", "correct": False,
             "why": "Spreading out does not speed a particle up; only warming "
                    "does. And a longer journey can never take less time than "
                    "a shorter one."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h02",
        "band": "harder",
        "text": "An insect has no oxygen-carrying blood: air reaches its cells "
                "down tiny tubes, and the last stretch is pure diffusion. Why "
                "could a mouse not manage the same way?",
        "options": [
            {"text": "A mouse's skin is too thick for air to reach the tubes "
                     "at all", "correct": False,
             "why": "Skin thickness is not the obstacle — the tubes would open "
                    "to the air just as an insect's do. The problem is the "
                    "distance left inside the animal."},
            {"text": "A mouse is far thicker, and diffusion over centimetres "
                     "would take hours", "correct": True},
            {"text": "The particles in a mouse move more slowly, because a "
                     "mouse is bigger", "correct": False,
             "why": "Particle speed has nothing to do with the size of the "
                    "animal. A warm mouse's particles move faster if anything "
                    "— it is the distance that defeats them."},
            {"text": "An insect's wings waft air along the tubes, and a mouse "
                     "has no wings", "correct": False,
             "why": "Nothing wafts air down those tubes. Diffusion needs no "
                    "draught at all — what it needs is a short distance, and a "
                    "mouse cannot offer one."},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h03",
        "band": "harder",
        "text": "In 1827 Robert Brown watched pollen grains in water jitter "
                "endlessly, with nothing touching them. What does that jitter "
                "show about the water?",
        "options": [
            {"text": "The pollen grains were alive, and the jitter was them "
                     "swimming about", "correct": False,
             "why": "That is what people suspected at the time, and it is not "
                    "what Einstein found in 1905. The explanation lay in the "
                    "water, not in the grain."},
            {"text": "Tiny currents in the water were stirring the grains "
                     "about", "correct": False,
             "why": "A current would sweep neighbouring grains along together, "
                    "and it would die away. This jitter is random, grain by "
                    "grain, and it never stops."},
            {"text": "The grains were repelling one another and pushing "
                     "themselves apart", "correct": False,
             "why": "A single grain on its own jitters just as much, so the "
                    "other grains cannot be the cause. What surrounds every "
                    "grain is water."},
            {"text": "Invisible water particles are always moving, and "
                     "batter the grain unevenly", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h04",
        "band": "harder",
        "text": "Suppose the drop were released in the middle of the tank "
                "instead of at the left-hand end, with the counters still "
                "counting crossings of the middle line. What would they do?",
        "options": [
            {"text": "Both would climb at about the same rate from the start, "
                     "while the dye still spread outwards", "correct": True},
            {"text": "The left-to-right counter would climb faster, because "
                     "the particles head for the empty ends", "correct": False,
             "why": "Particles never head anywhere. The two counters differ "
                    "only when one side is more crowded than the other, and "
                    "here the sides start equally crowded."},
            {"text": "Neither would climb, because a particle has no reason to "
                     "cross the middle", "correct": False,
             "why": "A particle needs no reason — it is already moving and it "
                    "steps at random, so it crosses the line again and again. "
                    "That is why both counters run away."},
            {"text": "The dye would stay as a blob, because it is already "
                     "evenly placed in the tank", "correct": False,
             "why": "A blob is crowded in the middle and empty at both ends, "
                    "so it spreads — outwards, in both directions. Placed "
                    "evenly is not the same as spread evenly."},
        ],
        "figure": None,
    },

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-05-e05",
        "band": "easier",
        "text": "What does concentration mean?",
        "options": [
            {"text": "How many particles of a substance there are in a given "
                     "space",
             "correct": True},
            {"text": "How fast the particles of a substance happen to be "
                     "moving",
             "correct": False,
             "why": "That is set by temperature. Concentration is about how "
                    "many are packed into a space"},
            {"text": "How strongly a substance smells",
             "correct": False,
             "why": "A strong smell often means a high concentration, but the "
                    "word counts particles rather than describing a smell"},
            {"text": "How heavy one particle of a substance is",
             "correct": False,
             "why": "That is a property of one particle. Concentration is "
                    "about how crowded a space is"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e06",
        "band": "easier",
        "text": "The bench says each particle takes a step in a random "
                "direction. What does random mean in science?",
        "options": [
            {"text": "Strange, or hard to believe",
             "correct": False,
             "why": "That is the everyday use of the word. In science it "
                    "means unpredictable, direction by direction"},
            {"text": "With no pattern and no set direction",
             "correct": True},
            {"text": "Very fast, and hard to follow",
             "correct": False,
             "why": "Speed has nothing to do with it. A slow movement can be "
                    "just as random"},
            {"text": "Chosen by something too small to see",
             "correct": False,
             "why": "Nothing is choosing. That is what random rules out"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e07",
        "band": "easier",
        "text": "The lesson gives the time diffusion needs at different "
                "scales. About how long does it take to cross a single cell, "
                "roughly 0.01 mm?",
        "options": [
            {"text": "About a minute, once the spreading gets going",
             "correct": False,
             "why": "Far too slow. Over distances this small diffusion is "
                    "quick enough that a cell needs no delivery system at "
                    "all"},
            {"text": "About three hours",
             "correct": False,
             "why": "That is the figure for a fingertip, about a thousand "
                    "times further"},
            {"text": "About a hundredth of a second",
             "correct": True},
            {"text": "About a day",
             "correct": False,
             "why": "Nothing like it. Diffusion is unbeatable over distances "
                    "this small"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e08",
        "band": "easier",
        "text": "Which of these does diffusion NOT need?",
        "options": [
            {"text": "Particles that are moving",
             "correct": False,
             "why": "It needs this above everything. The movement of the "
                    "particles is the whole mechanism"},
            {"text": "Somewhere less crowded for particles to move into",
             "correct": False,
             "why": "It needs this too. Without a difference in crowding "
                    "there is no net spreading"},
            {"text": "Space between the particles to move through",
             "correct": False,
             "why": "It needs this. Pack the space solid and nothing can go "
                    "anywhere"},
            {"text": "Someone to waft it, or a draught to carry it",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-05-s05",
        "band": "standard",
        "text": "A teabag is lowered into a mug of still hot water and the "
                "colour spreads through it without anyone stirring. What is "
                "doing the work?",
        "options": [
            {"text": "The tea particles' own random movement, from where they "
                     "are crowded to where they are not",
             "correct": True},
            {"text": "The heat rising through the mug and carrying the colour "
                     "with it",
             "correct": False,
             "why": "Warmth speeds diffusion up, but the spreading happens in "
                    "cold water too. Nothing is being carried"},
            {"text": "The water pushing the tea particles outwards from the "
                     "bag",
             "correct": False,
             "why": "The water is still. Nothing is pushing — the tea "
                    "particles were already moving on their own"},
            {"text": "The tea particles being lighter than the water around "
                     "them, so they float outwards through it",
             "correct": False,
             "why": "Diffusion works in every direction, including "
                    "downwards. Floating cannot explain that"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s06",
        "band": "standard",
        "text": "A smell can reach you across a room in under a minute, yet "
                "diffusion alone would take days over that distance. How does "
                "it get there?",
        "options": [
            {"text": "Diffusion speeds up over long distances once it gets "
                     "going",
             "correct": False,
             "why": "It does the opposite. Double the distance and diffusion "
                    "takes four times as long"},
            {"text": "Draughts and convection carry it most of the way, and "
                     "diffusion covers the last stretch",
             "correct": True},
            {"text": "The smell travels through the air as a signal rather "
                     "than as particles actually arriving",
             "correct": False,
             "why": "A smell IS particles arriving at your nose. There is no "
                    "signal to send"},
            {"text": "The particles are lighter than air, so they are carried "
                     "up and over",
             "correct": False,
             "why": "You can smell something standing above the source as "
                    "easily as below it. Weight is not what moves it across "
                    "the room"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s07",
        "band": "standard",
        "text": "Two tanks get an identical drop of dye. One is left still; "
                "the other is gently stirred and evens out far sooner. Is the "
                "stirring diffusion?",
        "options": [
            {"text": "Yes — stirring is just diffusion done faster",
             "correct": False,
             "why": "Stirring moves whole regions of liquid at once. "
                    "Diffusion moves one particle at a time, by itself"},
            {"text": "Yes — the stirring gives the particles the push that "
                     "diffusion needs in order to begin",
             "correct": False,
             "why": "Diffusion needs no push at all. That is the point of the "
                    "still tank, which evens out on its own"},
            {"text": "No — stirring moves whole regions of liquid, while "
                     "diffusion carries on in both tanks",
             "correct": True},
            {"text": "No — and it also means the still tank will never even "
                     "out",
             "correct": False,
             "why": "The still tank does even out, given time. Stirring "
                    "changes how long it takes, not whether it happens"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s08",
        "band": "standard",
        "text": "A smell spreads through air far faster than a dye spreads "
                "through water. Why?",
        "options": [
            {"text": "Gas particles are smaller, so they slip between the air "
                     "particles",
             "correct": False,
             "why": "Size is not what decides it, and the particles do not "
                    "change size on entering a gas. Speed and free distance "
                    "are what differ"},
            {"text": "Air is a mixture, and mixtures diffuse faster than pure "
                     "substances",
             "correct": False,
             "why": "Being a mixture makes no difference. What matters is how "
                    "far apart the particles are and how fast they move"},
            {"text": "Gravity pulls the dye downwards and holds it back",
             "correct": False,
             "why": "Dye spreads upwards through water as well as downwards. "
                    "Gravity is not what is slowing it"},
            {"text": "Gas particles move faster and travel further between "
                     "collisions",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-05-h05",
        "band": "harder",
        "text": "Diffusion crosses 0.01 mm in about a hundredth of a second "
                "and 10 mm in about three hours. The distance is a thousand "
                "times bigger; the time is about a million times longer. Why "
                "the mismatch?",
        "options": [
            {"text": "Because the time goes up with the SQUARE of the "
                     "distance, and a thousand squared is a million",
             "correct": True},
            {"text": "Because the particles slow down as they get further "
                     "from the start",
             "correct": False,
             "why": "Nothing slows them. Their speed is set by temperature "
                    "and does not change with distance travelled"},
            {"text": "Because there are more particles in the way over a "
                     "longer distance",
             "correct": False,
             "why": "The crowding is the same all the way along. It is the "
                    "wandering path that makes long distances so costly"},
            {"text": "Because the three-hour figure was measured in a liquid "
                     "and the hundredth of a second in a gas",
             "correct": False,
             "why": "Both figures are for the same kind of journey. The "
                    "squaring rule is what accounts for the difference"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h06",
        "band": "harder",
        "text": "A lung is folded into millions of tiny sacs rather than "
                "being two smooth bags. Which fact about diffusion forces that "
                "design?",
        "options": [
            {"text": "Diffusion works only in gases, so the air has to be "
                     "kept well apart from the blood in the vessels below",
             "correct": False,
             "why": "Diffusion works in liquids too — that is how oxygen "
                    "crosses into the blood once it arrives"},
            {"text": "Diffusion is fast only over a fraction of a millimetre, "
                     "so the air must be brought very close to the blood",
             "correct": True},
            {"text": "Diffusion needs a current, and the folds create one",
             "correct": False,
             "why": "Diffusion needs no current at all. The folds are about "
                    "distance, not about stirring the air"},
            {"text": "Diffusion goes faster when there is more surface, "
                     "whatever the distance",
             "correct": False,
             "why": "Surface does help, but the reason a smooth bag fails is "
                    "the distance from its middle to the blood, which no "
                    "amount of surface fixes"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h07",
        "band": "harder",
        "text": "Einstein predicted in 1905 exactly how far a pollen grain "
                "should wander in a given time, and Perrin then measured it. "
                "Why did that settle an argument that eighty years of watching "
                "had not?",
        "options": [
            {"text": "Because Einstein was by then far more famous than any "
                     "of the people who had sat and watched the jitter for "
                     "themselves",
             "correct": False,
             "why": "Reputation settles nothing. What settled it was a number "
                    "fixed in advance and then checked"},
            {"text": "Because a microscope powerful enough had finally been "
                     "built",
             "correct": False,
             "why": "Brown had seen the jitter perfectly well in 1827. Seeing "
                    "it was never the problem"},
            {"text": "Because a number predicted in advance and then measured "
                     "can decide between rival ideas, and a description "
                     "cannot",
             "correct": True},
            {"text": "Because the jitter stopped once it was explained",
             "correct": False,
             "why": "The jitter has never stopped, and would not be evidence "
                    "for anything if it had"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h08",
        "band": "harder",
        "text": "Why must every cell in your body be microscopic?",
        "options": [
            {"text": "Because a bigger cell would be too heavy for the body "
                     "to carry",
             "correct": False,
             "why": "Mass is not the limit. The same matter arranged as many "
                    "small cells weighs exactly the same"},
            {"text": "Because cells have to fit into the narrow spaces "
                     "between the blood vessels, and those vessels are "
                     "themselves very fine",
             "correct": False,
             "why": "The vessels are built around the cells rather than the "
                    "other way round. The limit is set by how far diffusion "
                    "can reach"},
            {"text": "Because a large cell would be too slow to move about "
                     "the body",
             "correct": False,
             "why": "Almost all your cells stay where they are. Size is "
                    "limited by supply, not by travel"},
            {"text": "Because oxygen reaches a cell's middle by diffusion, "
                     "and diffusion is hopeless over more than a fraction of "
                     "a millimetre",
             "correct": True},
        ],
        "figure": None,
    },

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-05-e09",
        "band": "easier",
        "text": "What is diffusion?",
        "options": [
            {"text": "The spreading out of particles from where they are "
                     "crowded to where they are not",
             "correct": True},
            {"text": "The breaking down of a substance into smaller and "
                     "smaller pieces until it disappears",
             "correct": False,
             "why": "That is cutting a substance up. Diffusion moves the "
                    "particles about without changing a single one of them"},
            {"text": "The settling of the heavier particles in a mixture "
                     "towards the bottom of a container",
             "correct": False,
             "why": "Diffusion spreads a substance in every direction, "
                    "upwards as readily as downwards"},
            {"text": "The stirring of one substance through another until "
                     "the mixture is even",
             "correct": False,
             "why": "Stirring moves whole regions of liquid at once. "
                    "Diffusion needs no stirring at all"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e10",
        "band": "easier",
        "text": "In which states of matter does diffusion happen?",
        "options": [
            {"text": "In gases only",
             "correct": False,
             "why": "A dye spreads right through still water, so it happens "
                    "in liquids too"},
            {"text": "In gases and in liquids",
             "correct": True},
            {"text": "In gases, liquids and solids",
             "correct": False,
             "why": "A solid's particles are held in fixed positions, so "
                    "nothing spreads through one"},
            {"text": "In liquids and in solids",
             "correct": False,
             "why": "Gases diffuse fastest of the three, and nothing "
                    "spreads through a solid at all"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e11",
        "band": "easier",
        "text": "A drop of coloured dye is placed on each of these and "
                "everything is left alone for a day. On which one would the "
                "colour stay exactly where it was put?",
        "options": [
            {"text": "A beaker of still water at room temperature",
             "correct": False,
             "why": "The colour spreads right through still water, given "
                    "time. No stirring is needed"},
            {"text": "A glass of orange squash",
             "correct": False,
             "why": "Squash is a liquid, so its particles slide past one "
                    "another and the colour spreads"},
            {"text": "A block of ice, kept in a freezer",
             "correct": True},
            {"text": "A saucer of clear vinegar",
             "correct": False,
             "why": "Vinegar is a liquid, so its particles slide past one "
                    "another and the colour spreads through it"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e12",
        "band": "easier",
        "text": "Does diffusion need someone to stir it or waft it along?",
        "options": [
            {"text": "Yes, because a liquid's particles are packed far too "
                     "tightly to get moving on their own",
             "correct": False,
             "why": "A liquid's particles are moving already, and a dye "
                    "spreads through still water with nobody touching it"},
            {"text": "No, because the particles are already moving",
             "correct": True},
            {"text": "Yes, because otherwise nothing would start the "
                     "particles off on their journey",
             "correct": False,
             "why": "Nothing has to start them off. The particles have never "
                    "stopped moving in the first place"},
            {"text": "No in a gas, but a liquid has to be stirred before "
                     "anything will spread through it",
             "correct": False,
             "why": "A dye spreads through completely still water. Neither "
                    "state needs a stir to get going"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e13",
        "band": "easier",
        "text": "A drop of dye is added to a beaker of still water. Which "
                "change would make the colour spread through it sooner?",
        "options": [
            {"text": "Warming the water",
             "correct": True},
            {"text": "Cooling the water",
             "correct": False,
             "why": "Cooler particles move more slowly, so the colour takes "
                    "longer to spread, not less"},
            {"text": "Adding a second drop",
             "correct": False,
             "why": "Twice the dye colours the water more deeply, but each "
                    "particle still spreads at the same rate"},
            {"text": "Putting a lid on the beaker",
             "correct": False,
             "why": "A lid changes nothing about the water below it. It only "
                    "stops things getting in or out"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e14",
        "band": "easier",
        "text": "In which does diffusion happen faster, a gas or a liquid?",
        "options": [
            {"text": "A liquid, because its particles are packed close "
                     "enough to pass the substance straight on",
             "correct": False,
             "why": "Being packed close is exactly what slows a liquid down. "
                    "A particle is knocked off course almost at once"},
            {"text": "Neither, because the rate is the same in both",
             "correct": False,
             "why": "A smell crosses a small box in seconds while a dye "
                    "takes minutes to cross the same distance in water"},
            {"text": "A gas, because its particles move faster and travel "
                     "further between collisions",
             "correct": True},
            {"text": "A gas, because gravity has far less hold on a gas "
                     "particle than on a liquid one",
             "correct": False,
             "why": "Gravity is not what drives diffusion. A dye spreads "
                    "upwards through water as readily as downwards"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e15",
        "band": "easier",
        "text": "A crystal of potassium manganate(VII) is dropped into a "
                "beaker of still water and left for an hour. What would you "
                "see?",
        "options": [
            {"text": "The purple colour staying in a tight layer at the "
                     "bottom, exactly where the crystal landed",
             "correct": False,
             "why": "The dissolved particles do not stay put. Their own "
                    "movement carries them out through the water"},
            {"text": "The whole beaker turning purple the moment the crystal "
                     "reaches the bottom",
             "correct": False,
             "why": "The colour arrives near the crystal first and reaches "
                    "the top last, because the particles have to travel"},
            {"text": "The purple colour rising straight up and staying as a "
                     "floating layer on the surface",
             "correct": False,
             "why": "Diffusion spreads a substance in every direction, not "
                    "upwards only"},
            {"text": "The purple colour spreading outwards from the crystal",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e16",
        "band": "easier",
        "text": "The smell of a cut onion is strong beside the chopping "
                "board and faint across the kitchen. What is different about "
                "the air in the two places?",
        "options": [
            {"text": "There are far more onion particles in a given space "
                     "beside the board",
             "correct": True},
            {"text": "The onion particles are moving much faster beside the "
                     "board than across the room",
             "correct": False,
             "why": "Their speed is set by temperature, and that is the same "
                    "all through the kitchen"},
            {"text": "The onion particles are bigger beside the board and "
                     "shrink as they travel",
             "correct": False,
             "why": "A particle is exactly the same size wherever it is. "
                    "Only how many are packed into a space changes"},
            {"text": "The air is thinner across the kitchen, so less smell "
                     "will fit into it",
             "correct": False,
             "why": "The air is the same all through the room. What differs "
                    "is how many onion particles have reached each part"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e17",
        "band": "easier",
        "text": "A drop of food colouring has spread evenly through a glass "
                "of still water. Will it ever gather itself back into a drop?",
        "options": [
            {"text": "Yes, once the water has cooled down again",
             "correct": False,
             "why": "Cooling slows the particles down. It gives them no way "
                    "to find one another again"},
            {"text": "Yes, if the glass is left undisturbed for long enough",
             "correct": False,
             "why": "Time is what spread it in the first place. More time "
                    "cannot put a random spread back together"},
            {"text": "No, because random movement spreads a substance and "
                     "cannot gather it up again",
             "correct": True},
            {"text": "No, because the colouring particles have been used up "
                     "in the water",
             "correct": False,
             "why": "Nothing is used up. Every particle is still there, "
                    "simply spread thinly through the glass"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e18",
        "band": "easier",
        "text": "A jar of a brightly coloured gas is opened inside a large "
                "sealed cupboard. What happens to the colour of that gas over "
                "the next few hours?",
        "options": [
            {"text": "It stays exactly as bright, because none of the gas "
                     "has been lost from the cupboard",
             "correct": False,
             "why": "None is lost, but the same particles are now spread far "
                    "more thinly, and thin means faint"},
            {"text": "It gets deeper, because the gas is now mixed with the "
                     "air inside the cupboard",
             "correct": False,
             "why": "Mixing with the air spreads the gas out. Nothing about "
                    "it is being concentrated"},
            {"text": "It gets fainter, as the same particles spread through "
                     "far more space",
             "correct": True},
            {"text": "It stays bright inside the jar, because the gas has no "
                     "reason to leave it",
             "correct": False,
             "why": "A particle needs no reason. It steps at random, so it "
                    "crosses out of the jar sooner or later"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e19",
        "band": "easier",
        "text": "Bromine is a brown gas. A little of it is released at the "
                "bottom of a tall sealed jar of air, which is then left "
                "still. What happens over the next hour?",
        "options": [
            {"text": "The brown colour stays in the bottom of the jar, "
                     "where the bromine was released",
             "correct": False,
             "why": "Heavier particles do diffuse more slowly, but they "
                    "still spread. Given an hour the whole jar goes brown"},
            {"text": "The brown colour spreads through the whole jar",
             "correct": True},
            {"text": "The brown colour rises straight to the top of the jar "
                     "and collects there",
             "correct": False,
             "why": "The particles step at random in every direction, so "
                    "they fill the jar rather than picking one end of it"},
            {"text": "The brown colour fades away as the bromine is used up "
                     "by the air around it",
             "correct": False,
             "why": "Nothing uses it up in a sealed jar. The same particles "
                    "are still there, simply spread out thinly"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e20",
        "band": "easier",
        "text": "When you smell a bottle of vinegar, what has actually "
                "reached your nose?",
        "options": [
            {"text": "A signal sent out by the vinegar",
             "correct": False,
             "why": "Nothing is sent. A smell is the substance's own "
                    "particles landing in your nose"},
            {"text": "Air particles carrying the smell along",
             "correct": False,
             "why": "Air particles cannot pick anything up. The vinegar "
                    "particles travel there themselves"},
            {"text": "Heat given off by the vinegar",
             "correct": False,
             "why": "A cold bottle of vinegar smells just as sharp, so heat "
                    "cannot be what you are detecting"},
            {"text": "Particles of the vinegar itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e21",
        "band": "easier",
        "text": "A dye diffuses through a beaker of water. What is it that "
                "actually moves?",
        "options": [
            {"text": "The whole body of water, from one side to the other",
             "correct": False,
             "why": "The water stays where it is. Only the particles within "
                    "it are on the move"},
            {"text": "The colour, which travels while the particles stay put",
             "correct": False,
             "why": "A colour is not a thing that can travel on its own. It "
                    "is seen wherever the dye particles have got to"},
            {"text": "The dye's own particles, moving out among the water",
             "correct": True},
            {"text": "The beaker's own particles, which pass the dye along "
                     "the glass",
             "correct": False,
             "why": "The glass takes no part at all. Its particles are held "
                    "in fixed positions and go nowhere"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e22",
        "band": "easier",
        "text": "A drop of dye is spreading through a beaker of still water. "
                "What are the water particles doing while that happens?",
        "options": [
            {"text": "Standing still, and letting the dye particles travel "
                     "along between them",
             "correct": False,
             "why": "The water's particles never stop moving. They are what "
                    "knock the dye off course again and again"},
            {"text": "Moving at random too, and mixing in among the dye",
             "correct": True},
            {"text": "Being shoved aside by the dye and gathering against "
                     "the walls of the beaker",
             "correct": False,
             "why": "Nothing is shoved aside. The dye and the water end up "
                    "mixed in among one another"},
            {"text": "Slowly turning into dye particles as the colour "
                     "spreads through the beaker",
             "correct": False,
             "why": "No particle turns into another. The dye is only being "
                    "spread about among the water"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e23",
        "band": "easier",
        "text": "A drop of dye is released in the middle of a beaker of "
                "still water. In which directions does the colour spread?",
        "options": [
            {"text": "In every direction",
             "correct": True},
            {"text": "Downwards only",
             "correct": False,
             "why": "The colour reaches the top of the beaker as well as the "
                    "bottom, which sinking could not explain"},
            {"text": "Along the surface only",
             "correct": False,
             "why": "The water is equally in the way everywhere, and the "
                    "colour spreads through the depth of the beaker too"},
            {"text": "Towards the beaker's walls",
             "correct": False,
             "why": "Nothing draws a particle anywhere. It reaches a wall "
                    "only by stepping at random until it gets there"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e24",
        "band": "easier",
        "text": "Diffusion needs no push and no stir. So where does the "
                "movement that causes it come from?",
        "options": [
            {"text": "From tiny air currents in the room, however small "
                     "those currents happen to be",
             "correct": False,
             "why": "It happens in a sealed, still container where there is "
                    "no current at all"},
            {"text": "From the warmth of the room, which pushes the "
                     "particles outwards from where they are",
             "correct": False,
             "why": "Warmth changes how fast the particles move, but it does "
                    "not push them in any direction"},
            {"text": "From the force with which the substance was poured or "
                     "dropped in at the start",
             "correct": False,
             "why": "A substance placed in gently spreads just as surely as "
                    "one dropped in hard"},
            {"text": "From the particles' own movement, which never stops",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e25",
        "band": "easier",
        "text": "Apart from warming it, state one thing that would make a "
                "substance diffuse faster.",
        "options": [
            {"text": "A bigger difference in crowding between the two places",
             "correct": True},
            {"text": "A larger container for the substance to spread into",
             "correct": False,
             "why": "A bigger container gives further to travel, which makes "
                    "the spreading take longer"},
            {"text": "Particles with a greater mass than the ones it has",
             "correct": False,
             "why": "At the same temperature heavier particles move more "
                    "slowly, so they spread more slowly"},
            {"text": "Adding the substance more slowly and carefully",
             "correct": False,
             "why": "How a substance is added changes nothing about how its "
                    "particles move once they are in"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e26",
        "band": "easier",
        "text": "A bottle of perfume is opened at one end of a still, "
                "sealed room. Where are the perfume particles most crowded a "
                "few seconds later?",
        "options": [
            {"text": "Evenly all through the room already",
             "correct": False,
             "why": "Diffusion across a whole room is desperately slow. A "
                    "few seconds gets the particles nowhere near the far end"},
            {"text": "At the far end of the room, which they set off towards",
             "correct": False,
             "why": "The particles have no way of knowing where the far end "
                    "is, and nothing sets them off towards it"},
            {"text": "Against the ceiling, because a perfume rises",
             "correct": False,
             "why": "The particles step at random in every direction, so "
                    "they do not gather at the top"},
            {"text": "Right beside the open bottle",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e27",
        "band": "easier",
        "text": "In diffusion, what does net movement mean?",
        "options": [
            {"text": "The movement left over once the crossings each way are "
                     "taken off one another",
             "correct": True},
            {"text": "The total number of crossings, counting both "
                     "directions together",
             "correct": False,
             "why": "Adding the two totals adds in the crossings that cancel "
                    "each other out"},
            {"text": "The movement of the particles that never turn back "
                     "once they have set off",
             "correct": False,
             "why": "No particle keeps a direction. Every one of them "
                    "doubles back again and again"},
            {"text": "The movement of the liquid as a whole from one end of "
                     "the container to the other",
             "correct": False,
             "why": "The liquid itself does not go anywhere. Only the "
                    "particles within it move"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e28",
        "band": "easier",
        "text": "Complete the sentence. Diffusion happens because the "
                "particles are ...",
        "options": [
            {"text": "attracted towards the emptier part of the container",
             "correct": False,
             "why": "Nothing attracts a particle. It has no way of knowing "
                    "where the empty space is"},
            {"text": "constantly moving, and each step is taken in a random "
                     "direction",
             "correct": True},
            {"text": "pushed apart by the crowd of particles behind them",
             "correct": False,
             "why": "There is no push anywhere in diffusion. The particles "
                    "were already moving before anything was added"},
            {"text": "trying to spread themselves evenly through the space",
             "correct": False,
             "why": "A particle cannot try to do anything. Evenness is what "
                    "random movement happens to produce"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e29",
        "band": "easier",
        "text": "Which of these is an example of diffusion?",
        "options": [
            {"text": "Sugar being stirred into a mug of tea with a spoon",
             "correct": False,
             "why": "The spoon moves whole regions of liquid at once, which "
                    "is stirring rather than diffusion"},
            {"text": "Smoke being blown across a room by an electric fan",
             "correct": False,
             "why": "The fan makes a current that carries the smoke along. "
                    "Diffusion needs no current at all"},
            {"text": "Water being poured from a jug into a glass",
             "correct": False,
             "why": "Pouring moves the whole liquid together. Diffusion "
                    "moves one particle at a time"},
            {"text": "A smell spreading across a sealed box of still air",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e30",
        "band": "easier",
        "text": "Diffusion still happens inside a sealed container where the "
                "air is completely still. What does that show?",
        "options": [
            {"text": "That the container has to be sealed before diffusion "
                     "can get going inside it",
             "correct": False,
             "why": "Diffusion happens in an open room too. The seal is "
                    "there to rule a draught out, not to make it work"},
            {"text": "That nothing has to carry the particles, because they "
                     "move there themselves",
             "correct": True},
            {"text": "That the air inside must be warmer than the air "
                     "outside the container",
             "correct": False,
             "why": "The two are at the same temperature. Warmth changes the "
                    "speed of spreading, not whether it happens"},
            {"text": "That the particles must be lighter than the air they "
                     "are spreading through",
             "correct": False,
             "why": "Bromine has far heavier particles than air and spreads "
                    "through a sealed jar all the same"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e31",
        "band": "easier",
        "text": "A diffusion demonstration is repeated in a warm laboratory "
                "rather than a cold one, with everything else kept the same. "
                "What difference would you expect?",
        "options": [
            {"text": "The substance spreads the same distance in less time",
             "correct": True},
            {"text": "The substance spreads further and then stops",
             "correct": False,
             "why": "There is no distance at which diffusion stops. Warmth "
                    "changes how long the spreading takes, not how far"},
            {"text": "The substance spreads in one direction instead of in "
                     "all of them",
             "correct": False,
             "why": "Warming adds speed, not direction. The steps stay "
                    "random however hot it gets"},
            {"text": "No difference at all, since warmth cannot change how "
                     "particles move",
             "correct": False,
             "why": "Warmth is exactly what changes how fast particles move, "
                    "and faster particles spread sooner"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-e32",
        "band": "easier",
        "text": "A student compares how fast a dye spreads through water at "
                "20 °C and at 60 °C. Which quantity is the one they "
                "deliberately change?",
        "options": [
            {"text": "The colour of the dye chosen for the test",
             "correct": False,
             "why": "One dye is used throughout, so its colour is not "
                    "something that differs between the two runs"},
            {"text": "The temperature of the water",
             "correct": True},
            {"text": "The time the dye is left to spread through the water",
             "correct": False,
             "why": "The time is what gets measured at the end. It is not "
                    "something the student picks"},
            {"text": "The size of the beaker the water is held in",
             "correct": False,
             "why": "The beaker is kept the same in both, so that only the "
                    "temperature differs between them"},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "c1-05-s09",
        "band": "standard",
        "text": "Explain why a drop of ink spreads right through a beaker of "
                "still water when nobody stirs it.",
        "options": [
            {"text": "The water pushes the ink outwards from the spot where "
                     "the drop landed in it",
             "correct": False,
             "why": "The water is still and nothing in it is pushing. The "
                    "ink particles move on their own"},
            {"text": "The ink particles are drawn towards the clear water "
                     "that surrounds the drop",
             "correct": False,
             "why": "Nothing draws a particle anywhere. It has no way of "
                    "sensing where the clear water is"},
            {"text": "The ink particles are already moving at random, so "
                     "more leave the drop than return to it",
             "correct": True},
            {"text": "The ink is lighter than the water, so it gradually "
                     "floats out through the beaker",
             "correct": False,
             "why": "Ink spreads downwards through water as readily as "
                    "upwards, which floating could not account for"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s10",
        "band": "standard",
        "text": "Explain why nothing spreads noticeably through a block of "
                "solid copper at room temperature.",
        "options": [
            {"text": "Its particles have stopped moving, and diffusion needs "
                     "particles that are on the move",
             "correct": False,
             "why": "The particles are still moving. They vibrate constantly "
                    "on the spot, and never stop"},
            {"text": "Copper particles are far larger than the particles of "
                     "a liquid or of a gas",
             "correct": False,
             "why": "A particle is exactly the same size in every state. "
                    "What changes is how it is held"},
            {"text": "Copper is a metal, and diffusion happens only in "
                     "substances that are not metals",
             "correct": False,
             "why": "Liquid mercury is a metal and things spread through it. "
                    "The state is what matters, not the substance"},
            {"text": "Its particles are held in fixed positions and can only "
                     "vibrate, so they never change places",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s11",
        "band": "standard",
        "text": "Food taken straight from a freezer smells far less strongly "
                "than the same food on a warm plate. Explain why, in terms of "
                "the particles.",
        "options": [
            {"text": "The frozen food's particles are moving far more "
                     "slowly, so fewer of them reach your nose",
             "correct": True},
            {"text": "The frozen food's particles have been destroyed by the "
                     "cold, so there is less smell left to detect",
             "correct": False,
             "why": "Nothing destroys a particle. Warm the food again and "
                    "the smell comes straight back"},
            {"text": "Cold air is lighter than warm air, so it carries the "
                     "smell away before it can reach you",
             "correct": False,
             "why": "Cold air is in fact the denser of the two, and the air "
                    "carries nothing here — it is the food's own particles "
                    "that have been slowed"},
            {"text": "The frozen food's particles have become larger, and "
                     "large particles cannot travel through air",
             "correct": False,
             "why": "Particles do not change size when they are cooled. What "
                    "changes is how fast they move"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s12",
        "band": "standard",
        "text": "Ammonia gas is released at one end of a long sealed tube "
                "and hydrogen chloride gas at the other. A white solid forms "
                "in a ring where they meet. Why does the ring take minutes to "
                "appear rather than forming at once?",
        "options": [
            {"text": "The two gases have to warm up before their particles "
                     "are able to move at all",
             "correct": False,
             "why": "The particles were moving before either gas was "
                    "released. Nothing has to warm up first"},
            {"text": "Each gas has to travel down the tube, and a tangled "
                     "path through the air makes that slow",
             "correct": True},
            {"text": "The solid takes several minutes to form once the two "
                     "gases have reached each other",
             "correct": False,
             "why": "The solid appears the instant the two gases meet. The "
                    "wait is the journey, not the reaction"},
            {"text": "The tube has to fill with each gas completely before "
                     "any of the solid can form",
             "correct": False,
             "why": "The ring forms long before either gas has filled the "
                    "tube, at the place where the two first meet"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s13",
        "band": "standard",
        "text": "A gas jar of ordinary air is placed mouth to mouth on top "
                "of a gas jar of brown bromine, and the cover between them is "
                "removed. Predict what is seen in the upper jar, and explain.",
        "options": [
            {"text": "It stays colourless, because bromine has heavier "
                     "particles than air and cannot climb",
             "correct": False,
             "why": "Heavier particles spread more slowly, not upwards less. "
                    "The upper jar goes brown in the end"},
            {"text": "It turns brown, because the bromine particles step at "
                     "random and so travel upwards too",
             "correct": True},
            {"text": "It turns brown, because the air in the upper jar draws "
                     "the bromine up into the space",
             "correct": False,
             "why": "Nothing draws the bromine anywhere. The upper jar is "
                    "already full of air, not empty"},
            {"text": "It stays colourless, because the two gases have to be "
                     "stirred together before they will mix",
             "correct": False,
             "why": "Gases mix with no stirring at all. That is what makes "
                    "the demonstration worth doing"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s14",
        "band": "standard",
        "text": "A student claims a dye spreads through water only because "
                "footsteps in the corridor keep shaking the bench. Which test "
                "would deal with that claim best?",
        "options": [
            {"text": "Repeating it with a heavier bench, since a bench that "
                     "heavy could not shake at all",
             "correct": False,
             "why": "Any bench shakes a little under a footstep. The shaking "
                    "has to be ruled out, and this only reduces it"},
            {"text": "Repeating it with warmer water, to see whether the "
                     "colour spreads faster than before",
             "correct": False,
             "why": "That tests what temperature does. It says nothing about "
                    "whether the footsteps mattered"},
            {"text": "Repeating it in an empty building overnight, where "
                     "nothing goes past the bench at all",
             "correct": True},
            {"text": "Repeating it with more dye, to see whether the colour "
                     "spreads out any further than before",
             "correct": False,
             "why": "More dye makes a deeper colour. It leaves the question "
                    "of the footsteps exactly where it was"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s15",
        "band": "standard",
        "text": "A jar of a strong-smelling liquid is opened in a sealed "
                "laboratory. Explain why every corner of the room eventually "
                "smells of it, including the corners furthest from the jar.",
        "options": [
            {"text": "The particles are drawn towards the parts of the room "
                     "where there are none of them yet",
             "correct": False,
             "why": "A particle has no information about the rest of the "
                    "room, so nothing could draw it to an empty corner"},
            {"text": "The particles step at random in every direction, so "
                     "given enough time they reach everywhere",
             "correct": True},
            {"text": "The smell gets steadily stronger and larger until it "
                     "has filled the whole of the room",
             "correct": False,
             "why": "A smell is not a thing that grows. It is particles "
                    "arriving, and they get thinner as they spread"},
            {"text": "The air in the room slowly circulates, and it carries "
                     "the particles into every corner",
             "correct": False,
             "why": "The spreading happens in perfectly still air as well. "
                    "No circulation is needed for it"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s16",
        "band": "standard",
        "text": "A few drops of a smelly liquid are put at one end of a long "
                "sealed glass tube of still air. Describe how the smell moves "
                "along the tube, and say what drives it.",
        "options": [
            {"text": "It moves as a sharp front travelling at a steady "
                     "speed, driven by the pressure behind it",
             "correct": False,
             "why": "There is no front and no pressure pushing. The leading "
                    "particles are scattered and thin"},
            {"text": "It moves in a series of jumps whenever the tube is "
                     "disturbed, driven by the knocks it receives",
             "correct": False,
             "why": "An undisturbed tube works just as well. Nothing has to "
                    "knock it along"},
            {"text": "It stays where it is until the far end is warmed, "
                     "driven by the difference in temperature",
             "correct": False,
             "why": "The smell travels along a tube at one temperature "
                    "throughout. No difference is needed"},
            {"text": "It spreads gradually, thinning as it goes, driven by "
                     "the particles' own random movement",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s17",
        "band": "standard",
        "text": "Warming a liquid makes a dye spread through it sooner. "
                "Which statement about temperature explains that?",
        "options": [
            {"text": "Temperature is a measure of the average kinetic energy "
                     "of the particles, so warmer particles move faster",
             "correct": True},
            {"text": "Temperature is a measure of how much heat a substance "
                     "contains, so a warmer liquid holds more of it",
             "correct": False,
             "why": "A bathful of cool water holds far more energy than a "
                    "cupful of hot, yet it is at a lower temperature"},
            {"text": "Temperature is a measure of how big the particles are, "
                     "so warmer particles take up more room",
             "correct": False,
             "why": "Particles do not change size when they are warmed. Only "
                    "their movement changes"},
            {"text": "Temperature is a measure of how close together the "
                     "particles are, so a warm liquid is more crowded",
             "correct": False,
             "why": "Warming a liquid spreads its particles very slightly "
                    "further apart, not closer together"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s18",
        "band": "standard",
        "text": "A sugar cube is dropped into a mug of still tea and nobody "
                "stirs it. Hours later the whole mug tastes sweet. Explain "
                "how the sweetness got to the top.",
        "options": [
            {"text": "The sugar rose to the top of the mug because sweet "
                     "substances are lighter than tea",
             "correct": False,
             "why": "The whole mug tastes sweet, top and bottom alike. "
                    "Something that rose would sweeten only the top"},
            {"text": "The tea slowly circulates around the mug and carries "
                     "the sugar upwards with it",
             "correct": False,
             "why": "The tea is still and has gone cold. There is no "
                    "circulation left to carry anything"},
            {"text": "The sugar particles are pushed upwards by the weight "
                     "of the tea pressing down on the cube",
             "correct": False,
             "why": "Nothing is pushed in diffusion. The sugar particles "
                    "move on their own once they leave the cube"},
            {"text": "The sugar particles that left the cube spread through "
                     "the tea by their own random movement",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s19",
        "band": "standard",
        "text": "A drop of the same blue dye is added at each end of a long "
                "sealed tank of still water. Predict what the tank looks like "
                "a long time later.",
        "options": [
            {"text": "Blue at both ends and clear in the middle, where "
                     "neither drop can reach",
             "correct": False,
             "why": "Neither drop stops halfway. The particles carry on "
                    "stepping until they are spread right through"},
            {"text": "Evenly blue throughout, with the same shade everywhere",
             "correct": True},
            {"text": "Clear at both ends and blue in the middle, where the "
                     "two lots of dye have collected",
             "correct": False,
             "why": "Nothing gathers the dye into the middle. The particles "
                    "spread out from each end rather than meeting and staying"},
            {"text": "Blue at one end only, because the two drops cancel one "
                     "another out where they meet",
             "correct": False,
             "why": "Particles of the same dye cannot cancel each other. "
                    "They simply mix in among one another"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s20",
        "band": "standard",
        "text": "Each particle steps in a random direction, yet the "
                "substance as a whole moves one way. Explain how both can be "
                "true at the same time.",
        "options": [
            {"text": "The particles nearest the crowd are pushed outwards by "
                     "the ones behind them",
             "correct": False,
             "why": "There is no pushing anywhere. Each particle steps alone "
                    "and takes no notice of its neighbours"},
            {"text": "Particles crossing away from the crowd take longer "
                     "steps than the ones crossing back, so they cover more "
                     "ground with every step they take",
             "correct": False,
             "why": "Every step is the same length whichever way it goes. It "
                    "is the number of crossings that differs"},
            {"text": "More particles start on the crowded side, so more are "
                     "available to cross away than to cross back",
             "correct": True},
            {"text": "Once a particle has left the crowd it is unable to "
                     "step back into it again",
             "correct": False,
             "why": "Particles cross back constantly. Both counts climb, and "
                    "it is the gap between them that shows the spreading"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s21",
        "band": "standard",
        "text": "Explain why a smell released in a small sealed box is "
                "noticed all through the box far sooner than the same smell "
                "released in a large sealed room.",
        "options": [
            {"text": "The box holds less air, so there is less air in the "
                     "way of the particles as they travel",
             "correct": False,
             "why": "The air is just as crowded in the box as in the room. "
                    "It is the distance that differs, not the air"},
            {"text": "The particles in the box are moving faster than the "
                     "ones released into the room",
             "correct": False,
             "why": "Their speed is set by temperature, which is the same in "
                    "both. Only the journey is different"},
            {"text": "The particles have a much shorter distance to cross, "
                     "and diffusion is quick over short distances",
             "correct": True},
            {"text": "The walls of the box bounce the particles back "
                     "towards the middle and speed the spreading up",
             "correct": False,
             "why": "A wall sends a particle back at random, like any other "
                    "collision. It speeds nothing up"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s22",
        "band": "standard",
        "text": "A student sets out to show that a dye spreads faster "
                "through hot water than through cold. Which of these choices "
                "would make the comparison unfair?",
        "options": [
            {"text": "Adding the dye to the two beakers at the same moment "
                     "and timing them together",
             "correct": False,
             "why": "Starting both beakers together is good practice, and it "
                    "keeps the timing honest"},
            {"text": "Pouring the same volume of water into each beaker",
             "correct": False,
             "why": "Matching the water is one of the things that makes the "
                    "comparison fair in the first place"},
            {"text": "Using the same dye in both beakers",
             "correct": False,
             "why": "Using one dye throughout is exactly what a fair "
                    "comparison asks for"},
            {"text": "Putting a bigger drop of dye in the hot beaker",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s23",
        "band": "standard",
        "text": "A student claims diffusion needs gravity, because a dye "
                "sinks through water. Describe a test that would settle it.",
        "options": [
            {"text": "Weigh the dye before and after, to see whether gravity "
                     "has pulled any of it down",
             "correct": False,
             "why": "The mass is unchanged either way, so the balance "
                    "settles nothing about the direction of spreading"},
            {"text": "Place the dye at the bottom and see whether the colour "
                     "spreads upwards through the water",
             "correct": True},
            {"text": "Add the dye to two beakers of different depths and "
                     "compare how long each takes",
             "correct": False,
             "why": "That compares distances. Both beakers still have "
                    "gravity acting in them, so the claim survives"},
            {"text": "Use a denser liquid than water, so that gravity has "
                     "more to pull the dye down through",
             "correct": False,
             "why": "Changing the liquid changes the rate for other reasons "
                    "as well, so the result could not be pinned on gravity"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s24",
        "band": "standard",
        "text": "Two gases are mixed evenly in a sealed jar and the jar is "
                "left untouched for a year. Explain why they are still mixed "
                "at the end of it.",
        "options": [
            {"text": "The particles keep moving at random, and random "
                     "movement has no way of sorting them apart",
             "correct": True},
            {"text": "The particles have stopped moving, so the mixture is "
                     "frozen in place exactly as it was left",
             "correct": False,
             "why": "Nothing stops a particle. They are still crossing the "
                    "jar in every direction all year"},
            {"text": "The two gases have joined together to make a single "
                     "new substance that cannot come apart",
             "correct": False,
             "why": "Mixing is not joining. Each gas is still there "
                    "unchanged, and could be separated by other means"},
            {"text": "The jar is sealed, so neither gas has anywhere it "
                     "could go in order to separate out",
             "correct": False,
             "why": "They could separate into layers inside the sealed jar "
                    "if anything sorted them, and nothing does"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s25",
        "band": "standard",
        "text": "A purple crystal is dropped into a tall beaker of still "
                "water. The water just around it is deeply coloured within "
                "minutes, but the top of the beaker takes hours. Explain.",
        "options": [
            {"text": "The purple particles are heavier than water, so they "
                     "have to be lifted all the way to the top",
             "correct": False,
             "why": "Nothing lifts them. They step at random, and upwards is "
                    "as likely as any other direction"},
            {"text": "The water near the top is colder, so the particles "
                     "slow down as they climb through it",
             "correct": False,
             "why": "The beaker is at one temperature throughout. Nothing "
                    "slows the particles as they go"},
            {"text": "Most of the crystal has dissolved before any of it "
                     "gets the chance to start moving upwards",
             "correct": False,
             "why": "The particles start moving the moment they leave the "
                    "crystal. There is no waiting stage"},
            {"text": "The colour spreads outwards from where the particles "
                     "start, and the top is much further away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s26",
        "band": "standard",
        "text": "Two students set out to compare how fast a dye spreads in "
                "two beakers, and one of them stirs their beaker to help it "
                "along. Explain why the comparison is now worthless.",
        "options": [
            {"text": "The stirred beaker has been warmed well above the "
                     "other one by the spoon that stirred it",
             "correct": False,
             "why": "A spoon warms the water far too little to matter. The "
                    "problem is what the stirring itself did"},
            {"text": "The stirred beaker mixed by moving whole regions of "
                     "liquid, so its time is not a diffusion time",
             "correct": True},
            {"text": "The stirred beaker will now take longer, because "
                     "stirring breaks up the path the particles were taking",
             "correct": False,
             "why": "The stirred beaker evens out far sooner, not later. "
                    "Stirring is a fast way of mixing"},
            {"text": "The stirred beaker has lost some of its dye onto the "
                     "spoon, so it holds less than the other one",
             "correct": False,
             "why": "A trace on the spoon changes the shade very slightly "
                    "and does not explain the difference in time"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s27",
        "band": "standard",
        "text": "An open bottle of a smelly liquid is left in a sealed "
                "room. Explain why its particles spread out into the room "
                "rather than staying inside the bottle.",
        "options": [
            {"text": "The room is at a lower pressure than the inside of the "
                     "bottle, which drives the particles out",
             "correct": False,
             "why": "Both are at the same pressure once the bottle is open. "
                    "Nothing is being driven anywhere"},
            {"text": "The particles are attracted out into the room, where "
                     "there is far more space for them",
             "correct": False,
             "why": "Space cannot attract a particle. It has no way of "
                    "knowing the room is there"},
            {"text": "The particles inside the bottle are moving faster than "
                     "the ones that have got out",
             "correct": False,
             "why": "Every particle is at the same temperature and moves at "
                    "the same average speed, in or out"},
            {"text": "They are far more crowded in the bottle, so many more "
                     "are available to leave than to return",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s28",
        "band": "standard",
        "text": "An identical drop of dye is added to a beaker of water and "
                "to a beaker of thick syrup, both at the same temperature. "
                "Predict which spreads faster and explain why.",
        "options": [
            {"text": "The syrup, because its particles are packed together "
                     "and pass the dye along more efficiently",
             "correct": False,
             "why": "Being packed tightly is what gets in the way. Nothing "
                    "is passed along from particle to particle"},
            {"text": "The water, because its particles hold one another far "
                     "less tightly and get in the way less",
             "correct": True},
            {"text": "The syrup, because it is denser and a denser liquid "
                     "carries a substance through itself faster",
             "correct": False,
             "why": "A denser liquid is harder to move through, not easier. "
                    "Syrup is the slower of the two"},
            {"text": "Neither, because they are at the same temperature and "
                     "temperature is what sets the rate",
             "correct": False,
             "why": "Temperature is one thing that sets the rate. What the "
                    "particles have to push past is another"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s29",
        "band": "standard",
        "text": "Two identical beakers are given the same drop of dye. "
                "Beaker A was set up an hour ago and beaker B a minute ago. "
                "In which is the colour spreading faster right now, and why?",
        "options": [
            {"text": "Beaker B, because the difference in crowding is still "
                     "large and shrinks as the spreading goes on",
             "correct": True},
            {"text": "Beaker A, because the dye has had an hour to get going "
                     "and picks up speed as it spreads",
             "correct": False,
             "why": "Nothing speeds a particle up as it travels. Its speed "
                    "is set by temperature alone"},
            {"text": "Neither, because the rate of diffusion stays the same "
                     "from the first minute to the last",
             "correct": False,
             "why": "The spreading is quickest at the very start and slows "
                    "as the two sides even up"},
            {"text": "Beaker A, because the dye particles have spread out "
                     "and have more room to move about in",
             "correct": False,
             "why": "Having room is not what drives the spreading. It is the "
                    "difference in crowding, and A's has shrunk"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s30",
        "band": "standard",
        "text": "A gas is released into a sealed box of ordinary air, and "
                "the same gas is released into an identical box that has been "
                "emptied to a vacuum. Where does it reach the far wall "
                "sooner?",
        "options": [
            {"text": "In the box of air, because the air particles knock the "
                     "gas along towards the wall",
             "correct": False,
             "why": "The knocks send it in every direction, not towards the "
                    "wall. They hold it back rather than helping"},
            {"text": "In the emptied box, because there is nothing for the "
                     "particles to collide with on the way",
             "correct": True},
            {"text": "In the box of air, because a gas cannot travel at all "
                     "unless there is air for it to spread into",
             "correct": False,
             "why": "A gas spreads perfectly well into an empty space. Air "
                    "is not needed for it to travel through"},
            {"text": "In neither, because a gas spreads at exactly the same "
                     "rate whatever it is spreading through",
             "correct": False,
             "why": "The particles do move at the same speed in both, but in "
                    "air they are knocked off course and make slower progress"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s31",
        "band": "standard",
        "text": "A smell can reach you because a draught carries it, or "
                "because it diffuses. Describe the difference between the two.",
        "options": [
            {"text": "A draught moves whole regions of air together, while "
                     "diffusion moves one particle at a time",
             "correct": True},
            {"text": "A draught moves the smell in a straight line, while "
                     "diffusion moves it round corners instead",
             "correct": False,
             "why": "Both get round corners. What differs is whether the air "
                    "itself is on the move"},
            {"text": "A draught works in a gas, while diffusion works only "
                     "in a liquid such as water",
             "correct": False,
             "why": "Diffusion happens in gases too, faster than in any "
                    "liquid. That is why smells spread"},
            {"text": "A draught needs warm air, while diffusion happens only "
                     "when the air is cold and still",
             "correct": False,
             "why": "Diffusion happens at every temperature, and it is "
                    "faster when warm, not slower"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s32",
        "band": "standard",
        "text": "A student adds a drop of dye to a beaker and then carries "
                "the beaker across the laboratory to their desk before "
                "starting the stopwatch. Explain why their result is spoiled.",
        "options": [
            {"text": "The dye was exposed to the air on the way, so some of "
                     "it will have been lost before the timing began",
             "correct": False,
             "why": "Nothing escapes from a beaker of dyed water on a short "
                    "walk. The problem is the movement of the water"},
            {"text": "The walk warmed the water slightly, so the dye spread "
                     "faster than it should have done",
             "correct": False,
             "why": "Carrying a beaker warms it far too little to matter. "
                    "What it does is swirl the water"},
            {"text": "The walk swirled the water and mixed whole regions of "
                     "it, so the timing no longer measures diffusion",
             "correct": True},
            {"text": "The stopwatch was started late, so the measured time "
                     "comes out longer than the true one by the walk",
             "correct": False,
             "why": "A late start makes the measured time shorter, not "
                    "longer — and beside the swirling it is a small error"},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "c1-05-h09",
        "band": "harder",
        "text": "In a sealed tube 100 cm long, ammonia is released at one "
                "end and hydrogen chloride at the other at the same moment. "
                "The white ring forms 60 cm from the ammonia end. What does "
                "that tell you?",
        "options": [
            {"text": "The ammonia particles travelled half as far again in "
                     "the same time, so they move faster",
             "correct": True},
            {"text": "The hydrogen chloride was released a little later, "
                     "which is why it covered less of the tube",
             "correct": False,
             "why": "Both were released at the same moment, so the two "
                    "distances were covered in exactly the same time"},
            {"text": "The ammonia was more crowded at its end, which is what "
                     "pushed it further along the tube",
             "correct": False,
             "why": "Nothing pushes either gas. A more crowded start speeds "
                    "the early spreading but does not settle the ring"},
            {"text": "The hydrogen chloride particles are attracted back "
                     "towards their own end of the tube",
             "correct": False,
             "why": "Nothing attracts a particle towards anywhere. Every "
                    "step is taken with no set direction"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h10",
        "band": "harder",
        "text": "Ammonia and hydrogen chloride are released at opposite ends "
                "of a long sealed tube and a white ring forms where they "
                "meet. The whole tube is now warmed evenly along its length "
                "and the run repeated. Predict what happens to the ring.",
        "options": [
            {"text": "The ring forms sooner and nearer the middle, because "
                     "warming evens the two speeds out",
             "correct": False,
             "why": "Warming raises both speeds in the same proportion, so "
                    "the balance between them does not change"},
            {"text": "The ring forms sooner and in the same place as before",
             "correct": True},
            {"text": "The ring forms sooner and nearer the end the lighter "
                     "gas came from, because it gains the most",
             "correct": False,
             "why": "The lighter gas does not gain more than the other. Both "
                    "are speeded up by the same proportion"},
            {"text": "The ring forms at the same time and in the same place, "
                     "since warming a gas changes nothing",
             "correct": False,
             "why": "Warming makes both gases travel faster, so the ring "
                    "appears sooner than it did before"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h11",
        "band": "harder",
        "text": "Evaluate this definition: \"Diffusion is the movement of a "
                "liquid from where it is concentrated to where it is not.\"",
        "options": [
            {"text": "It is right, because that is exactly what the dye in a "
                     "beaker of water is seen to do",
             "correct": False,
             "why": "It matches what you see, which is why it is written so "
                    "often. The liquid itself stays where it is"},
            {"text": "It is wrong only in the direction, because the "
                     "movement runs the other way",
             "correct": False,
             "why": "The direction is the one part that is right. Particles "
                    "do move away from where they are crowded"},
            {"text": "It is wrong because it is the particles that move, not "
                     "the liquid as a whole",
             "correct": True},
            {"text": "It is wrong because diffusion happens only in gases, "
                     "so a liquid should never be mentioned",
             "correct": False,
             "why": "Diffusion happens in liquids as well as gases, and a "
                    "dye spreading through water is the standard example"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h12",
        "band": "harder",
        "text": "Two gases sit in the same sealed jar at the same "
                "temperature. One has much heavier particles than the other. "
                "Compare their average kinetic energy and their average "
                "speed.",
        "options": [
            {"text": "The heavier gas has the greater average kinetic energy "
                     "and the greater average speed",
             "correct": False,
             "why": "Both are at the same temperature, so their average "
                    "kinetic energy is the same, not greater"},
            {"text": "The heavier gas has the greater average kinetic energy "
                     "and the lower average speed",
             "correct": False,
             "why": "Being heavier does not give a particle more energy. "
                    "Temperature is what sets the average kinetic energy"},
            {"text": "Both have the same average kinetic energy and the same "
                     "average speed as each other",
             "correct": False,
             "why": "Equal energy carried by a heavier particle means a "
                    "lower speed, so the speeds cannot match"},
            {"text": "Both have the same average kinetic energy, and the "
                     "heavier gas has the lower average speed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h13",
        "band": "harder",
        "text": "A purple colour has spread 4 mm out from a crystal after 5 "
                "minutes. Roughly how far will it have spread after 20 "
                "minutes?",
        "options": [
            {"text": "About 16 mm",
             "correct": False,
             "why": "This gives four times the distance for four times the "
                    "time. Four times the time buys only twice the distance, "
                    "so 4 mm becomes 8 mm"},
            {"text": "About 64 mm",
             "correct": False,
             "why": "The spreading slows as it goes on rather than climbing "
                    "away. It can never outrun the time like this"},
            {"text": "About 4 mm",
             "correct": False,
             "why": "There is no distance at which diffusion stops. It goes "
                    "on getting further, just ever more slowly"},
            {"text": "About 8 mm",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h14",
        "band": "harder",
        "text": "Evaluate this explanation: \"A dye spreads out because the "
                "particles at the back of the crowd push the ones in front of "
                "them outwards.\"",
        "options": [
            {"text": "It is right, and the push is what the drop's shape "
                     "shows as it opens out from the middle",
             "correct": False,
             "why": "The shape is what random stepping produces on its own. "
                    "No push is needed to make it"},
            {"text": "It is wrong, because nothing pushes: the particles "
                     "were already moving before the drop was added",
             "correct": True},
            {"text": "It is wrong, because the push comes from the water "
                     "around the drop rather than from the dye behind it",
             "correct": False,
             "why": "Swapping which substance pushes keeps the same mistake. "
                    "There is no push in diffusion at all"},
            {"text": "It is right for a liquid, where the particles touch, "
                     "though not for a gas, where they do not",
             "correct": False,
             "why": "Touching does not make particles push one another "
                    "along. A liquid diffuses by random stepping too"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h15",
        "band": "harder",
        "text": "Two identical tanks of still water are at the same "
                "temperature. Tank A is given a strong drop of dye at one end "
                "and tank B a very weak one. Compare how fast the colour "
                "spreads in each at the start.",
        "options": [
            {"text": "The same in both, because how much dye is added "
                     "cannot change how fast it spreads",
             "correct": False,
             "why": "How many particles start on one side is exactly what "
                    "sets how many are available to cross away from it"},
            {"text": "Faster in B, because its particles have more room "
                     "between them and are held back less",
             "correct": False,
             "why": "The water is equally in the way in both tanks. Room "
                    "between the dye particles is not what sets the rate"},
            {"text": "Faster in A, because the difference in crowding "
                     "between its two ends is greater",
             "correct": True},
            {"text": "Faster in A, because a stronger dye is made of heavier "
                     "particles that carry further",
             "correct": False,
             "why": "It is the same dye in both, so the particles are "
                    "identical. Only how many there are differs"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h16",
        "band": "harder",
        "text": "A drop of cold food colouring is added to a beaker of hot "
                "water and swirling plumes of colour appear within seconds. "
                "Is all of that diffusion?",
        "options": [
            {"text": "Yes, and the swirls are what the paths of the "
                     "individual particles look like when there are enough "
                     "of them",
             "correct": False,
             "why": "A single particle's path is a tangle, not a plume. The "
                    "swirls are whole regions of water on the move"},
            {"text": "Yes, because diffusion is always faster in hot water "
                     "and seconds is what you would expect",
             "correct": False,
             "why": "Hot water does diffuse faster, but not in seconds "
                    "across a beaker. Something else is moving the colour"},
            {"text": "No, because the temperature difference sets currents "
                     "going, and a current moves whole regions of water",
             "correct": True},
            {"text": "No, because diffusion cannot happen at all while the "
                     "water is still being disturbed",
             "correct": False,
             "why": "Diffusion carries on throughout. It is simply far too "
                    "slow to account for what is seen"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h17",
        "band": "harder",
        "text": "A student times how long a crystal takes to colour two "
                "beakers, one warm and one cold, but drops the crystal into "
                "the warm beaker from much higher up. Explain why the result "
                "cannot be trusted.",
        "options": [
            {"text": "The extra drop height disturbs the warm water, so its "
                     "shorter time could be the splash rather than the heat",
             "correct": True},
            {"text": "The extra drop height gives the crystal more energy, "
                     "which warms the water further before it lands",
             "correct": False,
             "why": "A crystal falling a few centimetres warms nothing "
                    "measurably. The trouble is what the splash stirs up"},
            {"text": "The extra drop height makes the crystal break into "
                     "pieces, and broken pieces cannot dissolve",
             "correct": False,
             "why": "Broken pieces dissolve faster if anything, and a "
                    "crystal does not shatter on landing in water"},
            {"text": "The extra drop height means the crystal reaches the "
                     "bottom so much sooner that most of the colouring is "
                     "over before the timing begins",
             "correct": False,
             "why": "The difference in falling time is a fraction of a "
                    "second against a measurement in minutes"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h18",
        "band": "harder",
        "text": "A flask of a brown gas is joined by a closed tap to an "
                "identical flask holding nothing at all. The tap is opened "
                "and both flasks are left still. Predict what is seen in each "
                "flask a long time later.",
        "options": [
            {"text": "The first flask still brown and the second still "
                     "empty, since nothing has driven the gas across",
             "correct": False,
             "why": "Nothing needs to drive it. The particles were already "
                    "moving, and some of them step through the tap"},
            {"text": "The second flask brown and the first now empty, since "
                     "the gas moves into the space available",
             "correct": False,
             "why": "The particles have no reason to gather in the second "
                    "flask. They end up shared between the two"},
            {"text": "The first flask a little browner than the second, "
                     "because a gas never quite leaves where it started",
             "correct": False,
             "why": "Random stepping goes on until the two flasks match. "
                    "Nothing holds a particle near its starting place"},
            {"text": "Both flasks the same shade of brown, each paler than "
                     "the first flask was at the start",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h19",
        "band": "harder",
        "text": "A student argues: \"Each particle is as likely to step one "
                "way as the other, so an evenly spread dye is as likely to "
                "gather back into a drop as it was to spread out.\" Evaluate "
                "that argument.",
        "options": [
            {"text": "It is right, and a dye left long enough really will be "
                     "seen to gather back into a drop",
             "correct": False,
             "why": "No one has ever seen it happen. Spreading is what is "
                    "observed, every time, in every beaker"},
            {"text": "It is wrong, because a particle that has left the drop "
                     "can no longer step back towards it",
             "correct": False,
             "why": "A particle steps back towards the drop as readily as "
                    "away from it. Nothing prevents the return step"},
            {"text": "It is wrong, because there are so many particles that "
                     "the chance of all of them returning at once is "
                     "vanishingly small",
             "correct": True},
            {"text": "It is wrong, because the particles slow down once they "
                     "have spread out, and a slowed particle no longer has "
                     "the speed to get back to the drop",
             "correct": False,
             "why": "Their speed is set by temperature and does not change "
                    "as they spread"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h20",
        "band": "harder",
        "text": "Evaluate this account: \"The dye spread through the beaker "
                "because the water particles shoved it out of the way.\"",
        "options": [
            {"text": "It is right, and the shoving is why warming the water "
                     "makes the dye spread faster, since warm water particles "
                     "shove harder than cold ones can",
             "correct": False,
             "why": "Warming speeds the dye's own particles up as well. It "
                    "is not evidence that the water is doing the work"},
            {"text": "It is wrong, because the water particles do collide "
                     "with the dye but send it off in every direction rather "
                     "than out of the way",
             "correct": True},
            {"text": "It is wrong, because water particles are far too small "
                     "to have any effect on a dye particle",
             "correct": False,
             "why": "Water particles are quite big enough to knock a dye "
                    "particle off course, and constantly do"},
            {"text": "It is wrong, because the water particles are standing "
                     "still and only the dye is on the move",
             "correct": False,
             "why": "The water's particles are moving constantly. That is "
                    "why they collide with the dye at all"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h21",
        "band": "harder",
        "text": "A single drop of dye is released in the middle of a wide, "
                "shallow dish of still water. Predict the shape of the "
                "coloured region ten minutes later.",
        "options": [
            {"text": "A growing circle centred on where the drop was "
                     "released",
             "correct": True},
            {"text": "A narrow streak running from the middle to the nearest "
                     "edge of the dish",
             "correct": False,
             "why": "Nothing picks out one edge. Each step is as likely "
                    "towards one side as towards any other"},
            {"text": "A ring of colour at the rim of the dish with clear "
                     "water in the middle of it",
             "correct": False,
             "why": "The colour is deepest where the drop started and "
                    "thinnest at the edges, which is the other way round"},
            {"text": "A blob of the same size as the drop, with a sharp edge "
                     "that stays where it was",
             "correct": False,
             "why": "Nothing holds an edge in place. Particles cross out of "
                    "the blob constantly, so it blurs and grows"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h22",
        "band": "harder",
        "text": "A purple crystal sits in a tank where the water is made to "
                "flow slowly past it, and the colour reaches the far end far "
                "sooner than in a still tank. Which part of that is diffusion?",
        "options": [
            {"text": "All of it, because a flow is simply diffusion with the "
                     "water helping the particles along in the one direction",
             "correct": False,
             "why": "A flow moves whole regions of water together. That is a "
                    "different process from diffusion, not a faster one"},
            {"text": "None of it, because diffusion cannot happen while the "
                     "water is moving",
             "correct": False,
             "why": "The particles go on stepping at random whatever the "
                    "water does. Diffusion never switches off"},
            {"text": "The spreading of the colour sideways out of the "
                     "stream, and not the journey along the tank",
             "correct": True},
            {"text": "The journey along the tank, and not the spreading "
                     "sideways out of the stream",
             "correct": False,
             "why": "The journey along the tank is the water carrying the "
                    "colour with it, which is a flow rather than diffusion"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h23",
        "band": "harder",
        "text": "A student reads that diffusion is a movement from where "
                "particles are crowded to where they are not, and concludes "
                "that no particle ever travels the other way. Evaluate that "
                "conclusion.",
        "options": [
            {"text": "It is right, because a particle that turned back would "
                     "undo the spreading the others had achieved",
             "correct": False,
             "why": "Particles do turn back constantly, and the spreading "
                    "still happens. The two are not in conflict"},
            {"text": "It is wrong, because particles cross in both "
                     "directions all the time and only the difference "
                     "between the two counts",
             "correct": True},
            {"text": "It is right until the two sides are even, after which "
                     "particles begin to travel both ways",
             "correct": False,
             "why": "Crossings run both ways from the very first second. "
                    "Nothing changes about that when the sides even up"},
            {"text": "It is wrong, because the movement is actually from "
                     "where particles are least crowded to where they are "
                     "most",
             "correct": False,
             "why": "The net movement really does run away from the crowd. "
                    "The error is in ruling out the return crossings"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h24",
        "band": "harder",
        "text": "Two jars of gas are mixed, one by shaking the jar and one "
                "by leaving it alone to diffuse. Once both look evenly mixed "
                "and the shaking has stopped, compare what is still going on "
                "in each.",
        "options": [
            {"text": "The shaken jar is still mixing and the still jar has "
                     "finished, because shaking leaves the gas swirling",
             "correct": False,
             "why": "The swirling dies away within seconds of the shaking "
                    "stopping, and then nothing is left of it"},
            {"text": "Both have finished entirely, because a mixture that "
                     "looks even has nothing left to do",
             "correct": False,
             "why": "Looking even is about the appearance. The particles in "
                    "both jars are still crossing in every direction"},
            {"text": "The still jar is still mixing and the shaken jar has "
                     "finished, because only diffusion carries on",
             "correct": False,
             "why": "The particles in the shaken jar move at random too. "
                    "Diffusion goes on in both of them"},
            {"text": "In both jars the particles carry on crossing at "
                     "random, while the swirling from the shaking has stopped",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h25",
        "band": "harder",
        "text": "Suggest why a laboratory keeps strong-smelling chemicals "
                "in a cupboard with air drawn steadily through it, rather "
                "than relying on a stoppered bottle on an open bench.",
        "options": [
            {"text": "The moving air carries away any particles that escape, "
                     "before they can spread through the room",
             "correct": True},
            {"text": "The moving air cools the chemicals right down, and "
                     "cold particles are quite unable to leave the bottle",
             "correct": False,
             "why": "Cooling slows the particles but does not stop them "
                    "escaping. Some get out at any temperature"},
            {"text": "The moving air stops the escaped particles from moving "
                     "at all, so they cannot spread anywhere",
             "correct": False,
             "why": "Nothing can stop a particle moving. The air removes "
                    "them rather than holding them still"},
            {"text": "The moving air makes the chemicals diffuse much more "
                     "slowly, so less of them reaches the laboratory air",
             "correct": False,
             "why": "The rate of diffusion is unchanged. What changes is "
                    "that the escaped particles are taken away"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h26",
        "band": "harder",
        "text": "Put these four in order, from the fastest spreading to the "
                "slowest: a smell through warm air, a smell through cold air, "
                "a dye through warm water, a dye through cold water.",
        "options": [
            {"text": "Warm air, cold air, warm water, cold water",
             "correct": True},
            {"text": "Warm air, warm water, cold air, cold water",
             "correct": False,
             "why": "Temperature is put ahead of state here. Even cold air "
                    "lets a substance spread faster than warm water does"},
            {"text": "Cold water, warm water, cold air, warm air",
             "correct": False,
             "why": "This is the right order reversed. Gases spread fastest "
                    "and warmth speeds everything up"},
            {"text": "Warm water, cold water, warm air, cold air",
             "correct": False,
             "why": "Liquids are put ahead of gases here. A gas particle "
                    "moves faster and travels further between collisions"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h27",
        "band": "harder",
        "text": "Compare what a rise in temperature does to diffusion with "
                "what a bigger difference in crowding does.",
        "options": [
            {"text": "Warming makes the particles move faster, while more "
                     "crowding on one side gives every one of them a "
                     "stronger push away from it",
             "correct": False,
             "why": "A crowd does not push. It only means more particles are "
                    "there to make the crossing"},
            {"text": "Warming aims more of the particles away from the "
                     "crowd, while more crowding on one side makes each of "
                     "them step further than before",
             "correct": False,
             "why": "Both halves are the wrong way round. Warming changes "
                    "speed and crowding changes numbers"},
            {"text": "Warming changes how far the substance ends up "
                     "spreading, while more crowding changes how quickly it "
                     "gets there",
             "correct": False,
             "why": "Neither changes how far it ends up. Both change how "
                    "long the spreading takes"},
            {"text": "Warming makes the particles move faster, while more "
                     "crowding on one side makes more of them available to "
                     "cross away",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h28",
        "band": "harder",
        "text": "Someone insists that particles spread out because they are "
                "attracted towards empty space. Which observation is the "
                "strongest single argument against that?",
        "options": [
            {"text": "A dye takes far longer to spread through water than a "
                     "smell takes through air, which shows any attraction "
                     "must be far weaker inside a liquid",
             "correct": False,
             "why": "That compares two states. Someone could still claim an "
                    "attraction was at work, more weakly, in the liquid"},
            {"text": "A dye spreads faster when the water it is in has been "
                     "warmed up first",
             "correct": False,
             "why": "An attraction could be claimed to act faster in warm "
                    "water, so this settles nothing"},
            {"text": "Once a tank is evenly coloured the particles go on "
                     "crossing in both directions, with no empty space left "
                     "to be drawn to",
             "correct": True},
            {"text": "A dye stops spreading the very moment the beaker "
                     "looks evenly coloured all through",
             "correct": False,
             "why": "It does not stop — and if it did, stopping when the "
                    "empty space ran out would support the idea rather than "
                    "defeat it"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h29",
        "band": "harder",
        "text": "Two substances are released together at one end of a long "
                "sealed tube of still air. One has much lighter particles "
                "than the other. Predict which is detected at the far end "
                "first, and what happens to the other.",
        "options": [
            {"text": "The lighter one first, and the heavier one never "
                     "arrives at all, because a particle that heavy cannot "
                     "cross a tube of that length",
             "correct": False,
             "why": "Weight does not stop a particle. The heavier substance "
                    "arrives too, simply later"},
            {"text": "The heavier one first, because a heavier particle "
                     "carries more energy and drives itself further along "
                     "the tube with every step",
             "correct": False,
             "why": "Both carry the same average energy at one temperature, "
                    "and the heavier one is therefore the slower"},
            {"text": "The lighter one first, and the heavier one arrives "
                     "later, because it moves more slowly at the same "
                     "temperature",
             "correct": True},
            {"text": "They arrive together, because both are carried along "
                     "the tube by the same still air",
             "correct": False,
             "why": "The air is still and carries nothing. Each substance "
                    "makes its own way along the tube"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h30",
        "band": "harder",
        "text": "A beaker is already coloured evenly with a dye. A further "
                "drop of exactly the same dye is added at one side. Predict "
                "what the extra dye does.",
        "options": [
            {"text": "It stays where it is put, because the beaker is "
                     "already evenly coloured throughout",
             "correct": False,
             "why": "Evenness is about the beaker as it was. The new drop "
                    "makes one side more crowded than the rest"},
            {"text": "It spreads out through the beaker, because it is "
                     "crowded where it was added",
             "correct": True},
            {"text": "It sinks to the bottom, because there is no room left "
                     "for it in the water above",
             "correct": False,
             "why": "There is ample room between the water's particles. "
                    "Nothing forces the new dye downwards"},
            {"text": "It spreads out but only until the colour it makes "
                     "matches the shade the beaker already had",
             "correct": False,
             "why": "The dye spreads until it is even, which leaves the "
                    "whole beaker deeper in colour than before"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h31",
        "band": "harder",
        "text": "A smell crossing a sealed box of still air, and a purple "
                "crystal colouring a beaker of still water, are both offered "
                "as evidence for diffusion. What does each show that the "
                "other does not?",
        "options": [
            {"text": "The smell shows it happens in a gas with nothing "
                     "visible moving; the crystal lets you watch the "
                     "spreading and shows it in a liquid too",
             "correct": True},
            {"text": "The smell shows that particles exist; the crystal "
                     "shows that they are coloured",
             "correct": False,
             "why": "The colour belongs to that one substance. Neither "
                    "demonstration says anything about particles in general "
                    "being coloured"},
            {"text": "The smell shows that diffusion needs a current; the "
                     "crystal shows that it does not",
             "correct": False,
             "why": "Both are set up with nothing moving. Neither shows a "
                    "current is needed for anything"},
            {"text": "The smell shows that diffusion is fast in a gas; the "
                     "crystal shows that it comes to a halt in a liquid once "
                     "the spreading looks finished, and stays halted",
             "correct": False,
             "why": "Nothing stops when the beaker looks even, and the "
                    "crystal could not show it if it did"},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-h32",
        "band": "harder",
        "text": "A student argues that diffusion must involve a force, "
                "because the dye has ended up somewhere it was not before, "
                "and moving something takes a force. Evaluate that argument.",
        "options": [
            {"text": "It is right, and the force comes from the water "
                     "particles pressing in on the drop from every side, "
                     "which squeezes the colour outwards through the beaker",
             "correct": False,
             "why": "Pressing in from all sides would hold the drop "
                    "together, not spread it out through the beaker"},
            {"text": "It is right, and the force is the attraction between "
                     "the dye and the clear water around it, which draws the "
                     "colour out towards the sides",
             "correct": False,
             "why": "There is no such attraction, and the dye would not "
                    "spread evenly if there were"},
            {"text": "It is wrong, because a force is needed only to start "
                     "or change a movement, and the particles were already "
                     "moving",
             "correct": True},
            {"text": "It is wrong, because the dye has not really moved: it "
                     "is the water that has moved around it",
             "correct": False,
             "why": "The dye's particles genuinely travel across the beaker. "
                    "The water as a whole stays put"},
        ],
        "figure": None,
    },
]
