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
            {"text": "Very fast, and hard to follow",
             "correct": False,
             "why": "Speed has nothing to do with it. A slow movement can be "
                    "just as random"},
            {"text": "With no pattern and no set direction",
             "correct": True},
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
            {"text": "About a hundredth of a second",
             "correct": True},
            {"text": "About a minute, once the spreading gets going",
             "correct": False,
             "why": "Far too slow. Over distances this small diffusion is "
                    "quick enough that a cell needs no delivery system at "
                    "all"},
            {"text": "About three hours",
             "correct": False,
             "why": "That is the figure for a fingertip, about a thousand "
                    "times further"},
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
            {"text": "Someone to waft it, or a draught to carry it",
             "correct": True},
            {"text": "Space between the particles to move through",
             "correct": False,
             "why": "It needs this. Pack the space solid and nothing can go "
                    "anywhere"},
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
            {"text": "The heat rising through the mug and carrying the colour "
                     "with it",
             "correct": False,
             "why": "Warmth speeds diffusion up, but the spreading happens in "
                    "cold water too. Nothing is being carried"},
            {"text": "The tea particles' own random movement, from where they "
                     "are crowded to where they are not",
             "correct": True},
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
            {"text": "The smell travels through the air as a signal rather "
                     "than as particles actually arriving",
             "correct": False,
             "why": "A smell IS particles arriving at your nose. There is no "
                    "signal to send"},
            {"text": "Draughts and convection carry it most of the way, and "
                     "diffusion covers the last stretch",
             "correct": True},
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
            {"text": "No — and it also means the still tank will never even "
                     "out",
             "correct": False,
             "why": "The still tank does even out, given time. Stirring "
                    "changes how long it takes, not whether it happens"},
            {"text": "No — stirring moves whole regions of liquid, while "
                     "diffusion carries on in both tanks",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-05-s08",
        "band": "standard",
        "text": "A smell spreads through air far faster than a dye spreads "
                "through water. Why?",
        "options": [
            {"text": "Gas particles move faster and travel further between "
                     "collisions",
             "correct": True},
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
            {"text": "Because the particles slow down as they get further "
                     "from the start",
             "correct": False,
             "why": "Nothing slows them. Their speed is set by temperature "
                    "and does not change with distance travelled"},
            {"text": "Because the time goes up with the SQUARE of the "
                     "distance, and a thousand squared is a million",
             "correct": True},
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
            {"text": "Diffusion needs a current, and the folds create one",
             "correct": False,
             "why": "Diffusion needs no current at all. The folds are about "
                    "distance, not about stirring the air"},
            {"text": "Diffusion is fast only over a fraction of a millimetre, "
                     "so the air must be brought very close to the blood",
             "correct": True},
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
            {"text": "Because the jitter stopped once it was explained",
             "correct": False,
             "why": "The jitter has never stopped, and would not be evidence "
                    "for anything if it had"},
            {"text": "Because a number predicted in advance and then measured "
                     "can decide between rival ideas, and a description "
                     "cannot",
             "correct": True},
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
            {"text": "Because oxygen reaches a cell's middle by diffusion, "
                     "and diffusion is hopeless over more than a fraction of "
                     "a millimetre",
             "correct": True},
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
        ],
        "figure": None,
    },
]
