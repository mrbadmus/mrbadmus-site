# -*- coding: utf-8 -*-
"""C1 lesson 01 — The particle model: twelve questions (MRB-269).

The lesson is two attempts to break one claim — matter is not continuous — so
the bank probes both attempts and then the claim itself. The cutting bench
supplies the floor (twenty-four halvings, and what you get if you cut past it);
the gap rig supplies the emptiness (fill the gap and every test fails); the hook
supplies the arithmetic (50 and 50 make 97 because small particles settle into
gaps between large ones).

The distractors are built from the lesson's two declared misconceptions.
PART-01 ("the knife was not sharp enough — a better knife would keep going")
supplies every option that blames the tool: the knife that tears rather than
cuts, the particle that "cannot be cut by anything", the sugar dust one grade
finer. PART-02 ("there is air, or dust, or something, in the gaps") supplies the
infinite regress in the bike-pump question, the filled-gap prediction of 100 ml,
and the ink that "fills the gaps in the water". Two further errors the lesson
exists to correct are worked as well: that squashing a gas makes the particles
themselves smaller, and that a model has to be an exact copy to be worth
anything.

No question restates a ladder rung. The rungs already own what is between the
particles of a gas, why the twenty-fifth cut fails, the 50/50 explanation and
the vacuum-in-the-room reply, so the bank works around all four — the cut-floor
questions go to what you actually get when you split a particle and to why the
piece turns grainy four cuts early, and the transfer questions go to Democritus,
to two liquids with same-sized particles, and to ink spreading through still
water.

`figure` is `None` throughout: this lesson holds no figures at all — both
instruments draw themselves on canvas — so every stem here is self-contained.
"""

UNIT = "C1"
LESSON = "particle-model"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "c1-01-e01",
        "band": "easier",
        "text": "The lesson opens by saying that matter is not continuous. "
                "What does continuous mean?",
        "options": [
            {"text": "Made of separate pieces, each far too small for you to "
                     "see, with gaps in between.",
             "correct": False,
             "why": "That is the particle model itself — the idea that "
                    "replaces continuous. Continuous means the opposite: no "
                    "separate pieces at all."},
            {"text": "All one piece, with no gaps and no separate bits, "
                     "however closely you look.",
             "correct": True},
            {"text": "Always moving, and never stopping even for a moment.",
             "correct": False,
             "why": "Constant motion is one of the model's three claims, not "
                    "what continuous means. Continuous is about having no gaps "
                    "and no separate bits."},
            {"text": "Joined so tightly together that nothing can cut a piece "
                     "off.",
             "correct": False,
             "why": "Continuous is not about strength. It says there are no "
                    "separate bits there in the first place, however closely "
                    "you look."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e02",
        "band": "easier",
        "text": "The key fact makes three claims about matter. Alongside "
                "“made of particles” and “nothing between "
                "them”, what is the third?",
        "options": [
            {"text": "The particles are all the same size.",
             "correct": False,
             "why": "They are not. The whole 50 and 50 makes 97 result depends "
                    "on one liquid's particles being smaller than the "
                    "other's."},
            {"text": "The particles move only when you heat them.",
             "correct": False,
             "why": "Heating changes how fast they move, not whether they "
                    "move. The model says they never stop."},
            {"text": "The particles are too hard for anything to break.",
             "correct": False,
             "why": "Hardness belongs to a lump of a substance, not to one "
                    "particle — and the third claim is about motion, not "
                    "strength."},
            {"text": "The particles are always moving.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e03",
        "band": "easier",
        "text": "The cutting bench stops at one particle of sugar. Cut that "
                "particle in half anyway and you do get something. What?",
        "options": [
            {"text": "Carbon, hydrogen and oxygen — and not one of them "
                     "is sweet.",
             "correct": True},
            {"text": "Nothing at all, because a particle cannot be cut by "
                     "anything.",
             "correct": False,
             "why": "A sharp enough tool can split a particle. What is "
                    "impossible is a smaller piece that is still sugar, not "
                    "the cut itself."},
            {"text": "Two smaller sugar particles, each one half as sweet as "
                     "before.",
             "correct": False,
             "why": "There is no such thing as half a sugar particle. Below "
                    "the floor the substance stops existing — you get "
                    "carbon, hydrogen and oxygen."},
            {"text": "Sugar dust, too fine to see and much too fine to taste.",
             "correct": False,
             "why": "Dust is still sugar, just in small lumps. Past the floor "
                    "what you get is not sugar at all."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e04",
        "band": "easier",
        "text": "This lesson calls the particle picture a model. What is a "
                "model?",
        "options": [
            {"text": "An exact copy of the real thing, shrunk down small "
                     "enough for you to see it.",
             "correct": False,
             "why": "A model does not have to be a perfect copy to be useful. "
                    "Nobody has ever seen a particle; this model earns its "
                    "place by explaining what you can see."},
            {"text": "A guess that nobody has got round to testing yet.",
             "correct": False,
             "why": "A guess is where a model starts. This one has been "
                    "tested — the 97 ml reading and the squashed gas are "
                    "it being tested."},
            {"text": "A simple picture or idea that helps explain something we "
                     "cannot see.",
             "correct": True},
            {"text": "A rule that has been shown to hold everywhere, always, "
                     "with no exceptions.",
             "correct": False,
             "why": "Every model has limits, and later in this unit you find "
                    "where this one runs out. A model is a useful picture, not "
                    "a rule that can never fail."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "c1-01-s01",
        "band": "standard",
        "text": "50 ml of water poured into 50 ml of alcohol reads 97 ml. "
                "Which fact about the two liquids does the explanation "
                "depend on?",
        "options": [
            {"text": "That alcohol is lighter than water, so it sinks down "
                     "into it and takes up less room.",
             "correct": False,
             "why": "Weight has nothing to do with it. What matters is that "
                    "the particles are different sizes."},
            {"text": "That the two liquids react together, and the product "
                     "they make takes up less room.",
             "correct": False,
             "why": "Nothing reacts and nothing is lost. The volume drops "
                    "because the particles pack more closely, not because the "
                    "matter changed."},
            {"text": "That their particles are different sizes, so small ones "
                     "fit gaps between big ones.",
             "correct": True},
            {"text": "That some alcohol evaporates as you pour, so less of it "
                     "arrives.",
             "correct": False,
             "why": "Pour it again tomorrow and you get 97 ml again. Nothing "
                    "escaped — every drop you poured is still in the "
                    "cylinder."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s02",
        "band": "standard",
        "text": "A student answers that the gaps between particles are full of "
                "air. If they were right, what would 50 ml of water poured "
                "into 50 ml of alcohol read?",
        "options": [
            {"text": "100 ml — with the gaps already full, the volumes "
                     "would simply add.",
             "correct": True},
            {"text": "97 ml, exactly as before, because air weighs almost "
                     "nothing.",
             "correct": False,
             "why": "Weight is not the point. If the gaps already held air, "
                    "the water particles would have nowhere to go and the "
                    "total would have to be 100 ml."},
            {"text": "More than 100 ml, because the air in both liquids adds "
                     "volume too.",
             "correct": False,
             "why": "The air would not be extra — it would fill space you "
                    "have already counted. Filled gaps give exactly 100 ml, "
                    "and the cylinder says 97."},
            {"text": "Less than 97 ml, because the air is squeezed out as you "
                     "pour.",
             "correct": False,
             "why": "Nothing is squeezed out; the reading is steady and it "
                    "repeats. Filled gaps would give 100 ml, and the real "
                    "answer is 97."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s03",
        "band": "standard",
        "text": "A bike pump squashes air into a fifth of the space it "
                "started in. What has got smaller?",
        "options": [
            {"text": "The particles themselves, squeezed down by the "
                     "pressure.",
             "correct": False,
             "why": "Particles do not change size. You are pushing them closer "
                    "together, and it is the empty space between them that "
                    "shrinks."},
            {"text": "The empty space between the particles, as they are "
                     "pushed closer.",
             "correct": True},
            {"text": "The amount of air, because some of it is destroyed by "
                     "the pressure.",
             "correct": False,
             "why": "Every particle you started with is still inside the pump. "
                    "Nothing is destroyed — they are just closer "
                    "together."},
            {"text": "The gaps in the air that fills the gaps between the "
                     "particles.",
             "correct": False,
             "why": "That is the answer that never ends: air filling gaps "
                    "needs gaps of its own, and so does that air, forever. The "
                    "gaps hold nothing."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s04",
        "band": "standard",
        "text": "Four cuts before the floor, the edge of the piece stops "
                "looking smooth. Why?",
        "options": [
            {"text": "The knife has started tearing the sugar instead of "
                     "cutting it.",
             "correct": False,
             "why": "The knife is doing nothing different — it has a "
                    "perfect edge and never blunts. What has changed is the "
                    "piece, not the tool."},
            {"text": "The sugar has begun breaking down into a different "
                     "substance.",
             "correct": False,
             "why": "It is still sugar right down to the last particle. Only "
                    "cutting past that particle gives you something else."},
            {"text": "The piece has got too small for the drawing to show it "
                     "accurately.",
             "correct": False,
             "why": "The drawing is not failing you. The piece really has "
                    "stopped being smooth, because there is so little of it "
                    "left."},
            {"text": "So few particles are left that you could count them, so "
                     "the edge is bumpy.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "c1-01-h01",
        "band": "harder",
        "text": "Democritus argued around 400 BC that cutting must stop "
                "somewhere. Why did his idea not count as science for two "
                "thousand years?",
        "options": [
            {"text": "He was wrong about the details, so it all had to be "
                     "worked out again.",
             "correct": False,
             "why": "His idea was right in outline. What it lacked was not "
                    "correctness but evidence — nothing measured could "
                    "separate it from the rival idea."},
            {"text": "Nobody could imagine matter being made of pieces before "
                     "microscopes existed.",
             "correct": False,
             "why": "No microscope has ever shown a particle. It was numbers "
                    "that settled it — combining ratios, balanced masses, "
                    "and 97 ml."},
            {"text": "The Greeks had no way of writing the idea down clearly "
                     "enough.",
             "correct": False,
             "why": "The idea was written down and argued over for centuries. "
                    "Argument was exactly the problem: it could not choose "
                    "between two reasonable ideas."},
            {"text": "He had an argument but no measurement, so nothing ruled "
                     "out matter being continuous.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h02",
        "band": "harder",
        "text": "The key note names three claims: a floor you cannot cut past, "
                "nothing at all between the particles, and constant motion. "
                "Which one has this lesson not put to the test?",
        "options": [
            {"text": "That the particles are always moving and never stop.",
             "correct": True},
            {"text": "That there is a floor you cannot cut past.",
             "correct": False,
             "why": "That was attempt one, the cutting bench: twenty-four "
                    "halvings, and no smaller piece of sugar exists."},
            {"text": "That there is nothing at all between the particles.",
             "correct": False,
             "why": "That was attempt two, the gap rig: put anything in the "
                    "gap and every test you run fails."},
            {"text": "That the particles are far too small to see.",
             "correct": False,
             "why": "That is part of the picture, not one of the three claims "
                    "— and the piece vanished from sight long before cut "
                    "twenty-four."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h03",
        "band": "harder",
        "text": "Two different liquids are mixed, 50 ml of each, but this time "
                "their particles are all about the same size. What does the "
                "model predict?",
        "options": [
            {"text": "97 ml again, because mixing two liquids always loses "
                     "three millilitres.",
             "correct": False,
             "why": "97 is not a magic number. Those three millilitres came "
                    "from small particles dropping into gaps between large "
                    "ones, so change the sizes and you change the result."},
            {"text": "Exactly 100 ml, because liquids with same-sized "
                     "particles have no gaps.",
             "correct": False,
             "why": "Every liquid has gaps between its particles. What has "
                    "changed is not whether there are gaps but how well the "
                    "other liquid's particles fit into them."},
            {"text": "Closer to 100 ml, because same-sized particles do not "
                     "drop into gaps so easily.",
             "correct": True},
            {"text": "More than 100 ml, because same-sized particles push each "
                     "other apart.",
             "correct": False,
             "why": "Mixing does not push particles apart. Same-sized "
                    "particles pack about as well mixed as they did separately, "
                    "so the volume barely moves."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h04",
        "band": "harder",
        "text": "A drop of ink in a beaker of still water spreads until the "
                "whole beaker is coloured, and nobody stirs it. Which two "
                "claims of the model does that need?",
        "options": [
            {"text": "That particles are far too small to see, and that ink is "
                     "made of particles.",
             "correct": False,
             "why": "Both are true, and neither one explains the spreading. "
                    "What moves the ink is its particles' own motion, into the "
                    "empty space between the water particles."},
            {"text": "That particles move on their own, and that there is "
                     "empty space to move into.",
             "correct": True},
            {"text": "That ink particles dissolve and become part of the water "
                     "particles.",
             "correct": False,
             "why": "Particles do not merge into one another. The ink "
                    "particles are still ink — they have worked their way "
                    "between the water particles."},
            {"text": "That the water pushes the ink about, and that ink is "
                     "lighter than water.",
             "correct": False,
             "why": "Nothing is pushing: the water is still. The ink spreads "
                    "because its own particles are moving and there is space "
                    "for them to move into."},
        ],
        "figure": None,
    },
]
