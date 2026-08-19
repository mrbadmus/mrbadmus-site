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
        "text": "The lesson gives the time diffusion alone needs to cross "
                "three distances. About how long does it take to cross a "
                "fingertip, roughly 10 mm?",
        "options": [
            {"text": "Under a millisecond", "correct": False,
             "why": "That is the time across a single cell, 0.01 mm — a "
                    "thousand times shorter. Diffusion falls apart as the "
                    "distance grows."},
            {"text": "About two minutes", "correct": False,
             "why": "Two minutes is a smell crossing a whole room, and a gas "
                    "manages that only because its particles move far faster "
                    "and travel further between collisions."},
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
            {"text": "Nothing attracts a particle — each steps at random, and "
                     "more cross right because more start left", "correct":
             True},
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
            {"text": "The particles take bigger steps so the tank evens out "
                     "sooner; the directions stay just as random", "correct":
             True},
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
            {"text": "Water is made of invisible particles that are always "
                     "moving, hitting the grain unevenly", "correct": True},
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
]
