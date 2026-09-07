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

    # ── easier · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-01-e05",
        "band": "easier",
        "text": "On the cutting bench the sugar cube starts one centimetre "
                "across and is halved again and again. About how many halvings "
                "does it take to reach a single particle?",
        "options": [
            {"text": "About two dozen.",
             "correct": True},
            {"text": "About two hundred.",
             "correct": False,
             "why": "Far too many. Each cut halves the piece, and halving is "
                    "brutal — two dozen halvings is already down to one "
                    "particle."},
            {"text": "About two million.",
             "correct": False,
             "why": "Far too many, and the number is wrong for a count of "
                    "particles too. Halving is brutal: each cut throws away "
                    "half of what is left."},
            {"text": "There is no fixed number — it depends how sharp the "
                     "knife is.",
             "correct": False,
             "why": "The knife on the bench never blunts, and the floor is in "
                    "the same place every time you run it. The limit is the "
                    "sugar, not the tool."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e06",
        "band": "easier",
        "text": "This unit uses the word matter. What does matter mean?",
        "options": [
            {"text": "Anything you can see or touch.",
             "correct": False,
             "why": "Air is matter and you can do neither. What counts is "
                    "having mass and taking up space."},
            {"text": "Anything that has mass and takes up space.",
             "correct": True},
            {"text": "Anything that is solid rather than liquid or gas.",
             "correct": False,
             "why": "All three states are matter. Matter is not one of the "
                    "states — the states are ways matter can be arranged."},
            {"text": "Anything that is made by a chemical reaction.",
             "correct": False,
             "why": "Matter does not have to be made by anything. Rock, air "
                    "and water are all matter and no reaction produced "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e07",
        "band": "easier",
        "text": "A single sugar particle is about 0.6 nm across — roughly a "
                "millionth of a millimetre. How does that compare with the "
                "width of a human hair?",
        "options": [
            {"text": "A hair is about ten times wider.",
             "correct": False,
             "why": "Nowhere near enough. Ten sugar particles side by side "
                    "would still be a millionth of a centimetre across."},
            {"text": "A hair is about a hundred times wider than a sugar "
                     "particle.",
             "correct": False,
             "why": "Still far too small a gap. The lesson gives the figure as "
                    "a hundred thousand times, not a hundred."},
            {"text": "A hair is about a hundred thousand times wider.",
             "correct": True},
            {"text": "A hair is about the same width.",
             "correct": False,
             "why": "You can see a hair. You cannot see a particle under any "
                    "microscope, which already tells you they are nothing "
                    "like the same size."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e08",
        "band": "easier",
        "text": "The vocabulary says that in this unit the word particle means "
                "something more exact. What does it mean?",
        "options": [
            {"text": "Any small piece of a substance, such as a grain of "
                     "sugar.",
             "correct": False,
             "why": "A grain is a lump holding billions of particles. A "
                    "particle here is the piece you cannot cut past."},
            {"text": "A speck of dust floating in the air.",
             "correct": False,
             "why": "Dust is matter, made of particles itself, and easily "
                    "big enough to see. A particle is far smaller than "
                    "that."},
            {"text": "A drop of liquid too small to see with your eyes.",
             "correct": False,
             "why": "A drop that small still holds a huge number of "
                    "particles. Being invisible is not the same as being one "
                    "particle."},
            {"text": "Atoms or molecules — the names come properly in the "
                     "next unit.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e09",
        "band": "easier",
        "text": "Democritus gave the last piece — the one that cannot be cut "
                "— a name. What did the name mean?",
        "options": [
            {"text": "Uncuttable.",
             "correct": True},
            {"text": "Invisible.",
             "correct": False,
             "why": "Being too small to see is true of a particle, but it is "
                    "not what he named it for. He named it for the cutting "
                    "stopping."},
            {"text": "Unchanging.",
             "correct": False,
             "why": "That is a different claim. His point was that halving "
                    "matter has to stop somewhere, not that nothing ever "
                    "changes."},
            {"text": "Weightless.",
             "correct": False,
             "why": "Particles have mass — that is part of being matter. The "
                    "name is about cutting, not about weight."},
        ],
        "figure": None,
    },

    # ── standard · MRB-335 top-up ───────────────────────────────────────
    {
        "id": "c1-01-s05",
        "band": "standard",
        "text": "A student says the cutting stopped at two dozen halvings "
                "because the knife had gone blunt. Which fact about the bench "
                "deals with that best?",
        "options": [
            {"text": "The knife has a perfect edge and never blunts, so "
                     "nothing about it changed at the last cut.",
             "correct": True},
            {"text": "The piece was already too small to see, so nobody could "
                     "check the edge.",
             "correct": False,
             "why": "Being unable to see it does not settle anything. What "
                    "settles it is that the knife is stated never to blunt."},
            {"text": "The sugar had turned into a liquid by then, and a "
                     "liquid cannot be cut cleanly by any blade.",
             "correct": False,
             "why": "Nothing was heated and nothing melted. The piece is "
                    "solid sugar right down to the last particle."},
            {"text": "The particle is too hard for any knife to cut through.",
             "correct": False,
             "why": "A sharp enough tool does split a particle — you get "
                    "carbon, hydrogen and oxygen. What is impossible is a "
                    "smaller piece that is still sugar."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s06",
        "band": "standard",
        "text": "The mixed water and alcohol is left in its cylinder "
                "overnight, sealed, and read again the next morning. What does "
                "the model predict?",
        "options": [
            {"text": "Back to 100 ml, because the particles settle apart "
                     "again overnight.",
             "correct": False,
             "why": "Nothing pulls them back apart. The closer packing is a "
                    "stable arrangement, not a temporary squeeze."},
            {"text": "97 ml, exactly as it read the night before.",
             "correct": True},
            {"text": "Below 97 ml, because more small particles keep dropping "
                     "into gaps.",
             "correct": False,
             "why": "The gaps that could be filled were filled as you poured. "
                    "The reading settles and then stays where it is."},
            {"text": "Less than 50 ml, because the alcohol evaporates "
                     "overnight.",
             "correct": False,
             "why": "The cylinder is sealed, so nothing can leave it. Even "
                    "unsealed, the 97 ml reading appears the moment you pour, "
                    "long before anything could evaporate."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s07",
        "band": "standard",
        "text": "The gap rig says that if you fill the gaps, the "
                "spreading-smell test fails. What exactly would go wrong with "
                "it?",
        "options": [
            {"text": "The smell would spread, but only along the draught, so "
                     "a still room would need stirring.",
             "correct": False,
             "why": "No draught is involved. Filling the gaps does not make a "
                    "particle need a draught — it leaves it with nowhere to "
                    "go at all."},
            {"text": "The smell would spread faster than it really does, "
                     "because the filling would carry it.",
             "correct": False,
             "why": "Filling the space cannot carry anything. It blocks "
                    "movement rather than helping it."},
            {"text": "A moving particle would have nowhere to go, so a smell "
                     "could never cross a still room — and it does.",
             "correct": True},
            {"text": "The smell would reach you instantly, because the "
                     "filling already touches both ends of the room.",
             "correct": False,
             "why": "A smell is particles arriving, not a signal passing "
                    "along. Those particles have to travel, and packed space "
                    "leaves them nowhere to travel through."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s08",
        "band": "standard",
        "text": "Someone still holds the old idea that matter is continuous "
                "— all one piece, with no separate bits. Which observation "
                "would that idea find hardest to explain?",
        "options": [
            {"text": "That a sugar cube has mass and takes up the space you "
                     "can see.",
             "correct": False,
             "why": "Continuous matter would have mass and take up space "
                    "too. An observation both ideas explain cannot choose "
                    "between them."},
            {"text": "That a knife can cut a sugar cube in half.",
             "correct": False,
             "why": "Continuous matter would cut perfectly well. It is where "
                    "the cutting STOPS that the two ideas disagree."},
            {"text": "That sugar tastes sweet and salt does not.",
             "correct": False,
             "why": "Both ideas allow different substances to be different. "
                    "This does not test either one."},
            {"text": "That air can be squashed into a fifth of the space it "
                     "was in.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s09",
        "band": "standard",
        "text": "A student objects that nobody has ever seen a particle, so "
                "the model cannot be trusted. Which reply is strongest?",
        "options": [
            {"text": "A model earns its place by explaining measurements, and "
                     "the 97 ml reading is one of them.",
             "correct": True},
            {"text": "Microscopes can see particles now, so the objection is "
                     "out of date.",
             "correct": False,
             "why": "No microscope shows a particle in the way this reply "
                    "suggests. The model was never resting on someone seeing "
                    "one."},
            {"text": "You have to take some things in science on trust.",
             "correct": False,
             "why": "That gives away the strongest point. The model is not "
                    "trusted blindly — it is trusted because measurements "
                    "keep coming out the way it predicts."},
            {"text": "It does not matter whether particles are real, as long "
                     "as the model keeps giving useful answers.",
             "correct": False,
             "why": "That concedes too much. The measurements are evidence "
                    "that particles are real, not just that the picture is "
                    "handy."},
        ],
        "figure": None,
    },

    # ── harder · MRB-335 top-up ─────────────────────────────────────────
    {
        "id": "c1-01-h05",
        "band": "harder",
        "text": "Both ideas — matter is continuous, and matter is particles "
                "— explain why a sugar cube looks perfectly smooth. Why is "
                "that observation no help in deciding between them?",
        "options": [
            {"text": "Because an observation both ideas predict cannot tell "
                     "you which one is right.",
             "correct": True},
            {"text": "Because looking at something is never scientific "
                     "evidence.",
             "correct": False,
             "why": "Observation is evidence. The trouble here is that this "
                    "particular observation is predicted by both ideas, so it "
                    "separates nothing."},
            {"text": "Because a sugar cube is too small to judge by eye.",
             "correct": False,
             "why": "You can see a sugar cube perfectly well. The problem is "
                    "not the seeing — it is that smoothness follows from "
                    "either idea."},
            {"text": "Because the particle model was not invented until long "
                     "after sugar cubes were.",
             "correct": False,
             "why": "When an idea was thought of has nothing to do with what "
                    "counts as evidence for it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h06",
        "band": "harder",
        "text": "50 ml of water is mixed with 50 ml of a liquid whose "
                "particles are much LARGER than water's. What does the model "
                "predict for the reading?",
        "options": [
            {"text": "Exactly 100 ml, because only small particles leave gaps "
                     "behind.",
             "correct": False,
             "why": "Large particles leave large gaps. It is the SIZE "
                    "DIFFERENCE that lets one liquid settle into the other, "
                    "and there is a big one here."},
            {"text": "Under 100 ml, because the small water particles drop "
                     "into the gaps between the large ones.",
             "correct": True},
            {"text": "More than 100 ml, because the large particles need more "
                     "room once the two liquids are mixed.",
             "correct": False,
             "why": "Nothing grows on mixing. Each particle takes exactly the "
                    "room it always did, and the packing can only improve."},
            {"text": "It cannot be predicted, because the model says nothing "
                     "about how big a particle is.",
             "correct": False,
             "why": "Particle size is central to this model — it is the whole "
                    "reason 50 and 50 make 97 rather than 100."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h07",
        "band": "harder",
        "text": "Squashing air into a fifth of its space is offered as "
                "evidence that the gaps hold nothing. Why would that squash be "
                "impossible if the gaps were packed with dust?",
        "options": [
            {"text": "Because dust would make the air too heavy to move.",
             "correct": False,
             "why": "Weight is not what resists a squash. What resists it is "
                    "having no empty space left to remove."},
            {"text": "Because the dust would block the pump before the air "
                     "could move.",
             "correct": False,
             "why": "This is not about a pump jamming. The claim is about the "
                    "gas itself: filled space cannot be shrunk."},
            {"text": "Because the space would already be occupied, so there "
                     "would be nothing left to remove.",
             "correct": True},
            {"text": "Because dust would turn the air into a solid, and a "
                     "solid cannot be squashed at all.",
             "correct": False,
             "why": "Adding dust does not change the state of the air. The "
                    "point is simpler — filled space has nothing left to give "
                    "up."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h08",
        "band": "harder",
        "text": "The lesson says a model need not be an exact copy to be "
                "useful, and also that this model has limits. Which statement "
                "follows from both?",
        "options": [
            {"text": "A model should be replaced as soon as anyone finds a "
                     "limit in it.",
             "correct": False,
             "why": "Every model has limits, so that rule would leave you "
                    "with nothing at all to think with."},
            {"text": "A model is only a guess until someone proves it is an "
                     "exact copy.",
             "correct": False,
             "why": "No model is ever an exact copy, and this one is far past "
                    "guesswork — measurements have tested it."},
            {"text": "A model with limits explains less than one without, so "
                     "the aim should be a model with none at all.",
             "correct": False,
             "why": "There is no model without limits to aim for. Knowing "
                    "where the edges are is part of understanding a model, "
                    "not a defect in it."},
            {"text": "A model can be relied on where it gives right answers, "
                     "and still be expected to fail somewhere.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h09",
        "band": "harder",
        "text": "Doubling a number two dozen times multiplies it by about 17 "
                "million. Given that the bench needs two dozen halvings to get "
                "from a centimetre of sugar to one particle, what does that "
                "number tell you?",
        "options": [
            {"text": "That about 17 million particles lie along one "
                     "centimetre of sugar.",
             "correct": True},
            {"text": "That a sugar particle is about 17 million times heavier "
                     "than a sugar cube.",
             "correct": False,
             "why": "The wrong way round, and the wrong quantity. The cube is "
                    "the heavier one, and the count here is about how many "
                    "particles fit along a length."},
            {"text": "That a sugar cube holds exactly 17 million particles "
                     "altogether.",
             "correct": False,
             "why": "17 million is the count along ONE edge. A cube holds "
                    "that many along each of three directions, which is a far "
                    "larger number again."},
            {"text": "That it would take 17 million knives to make the last "
                     "cut.",
             "correct": False,
             "why": "No number of knives makes the last cut. The number "
                    "counts particles along the edge, not tools."},
        ],
        "figure": None,
    },
]
