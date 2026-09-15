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

    # ── easier · MRB-338 night 3 top-up ─────────────────────────────────
    {
        "id": "c1-01-e10",
        "band": "easier",
        "text": "Two 50 ml volumes are poured together and the cylinder reads "
                "97 ml. What does that reading show?",
        "options": [
            {"text": "That the two liquids take up less room mixed than apart.",
             "correct": True},
            {"text": "That one of the two liquids has partly disappeared.",
             "correct": False,
             "why": "Nothing has gone. The same liquid is in the cylinder, "
                    "packed into less room than before."},
            {"text": "That the measuring cylinder is not accurate enough.",
             "correct": False,
             "why": "The reading repeats, and it repeats in other cylinders. "
                    "A faulty cylinder would not behave like that."},
            {"text": "That alcohol is lighter than water and floats on it.",
             "correct": False,
             "why": "Weight and floating are not measured here, and neither "
                    "would change the total volume."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e11",
        "band": "easier",
        "text": "A piece of sugar is halved twelve times. It is now far too "
                "small for you to see. Is it still sugar?",
        "options": [
            {"text": "No — a piece you cannot see has stopped being a "
                     "substance.",
             "correct": False,
             "why": "Being invisible is a fact about your eyes, not about the "
                    "sugar. Nothing in the piece has changed."},
            {"text": "Yes — and it stays sugar right down to the single "
                     "particle.",
             "correct": True},
            {"text": "No — below a grain's size it turns into ordinary dust.",
             "correct": False,
             "why": "Dust is a word for small lumps, not for a different "
                    "substance. Small sugar is still sugar."},
            {"text": "Only if you can still taste it, since taste is what "
                     "makes it sugar.",
             "correct": False,
             "why": "A piece this small is far too little to taste, and it "
                    "goes on being sugar all the same."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e12",
        "band": "easier",
        "text": "On the cutting bench each cut leaves a piece half as wide as "
                "the one before. After three cuts, what fraction of the "
                "starting width is left?",
        "options": [
            {"text": "One third.",
             "correct": False,
             "why": "Each cut halves the width. It does not divide it by the "
                    "number of cuts you have made."},
            {"text": "One sixth.",
             "correct": False,
             "why": "Three halvings divide the width by eight. Multiplying "
                    "three by two gives six, which is a different sum."},
            {"text": "One eighth.",
             "correct": True},
            {"text": "One half.",
             "correct": False,
             "why": "That is the width after the first cut alone. Two more "
                    "cuts follow, and each one halves it again."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e13",
        "band": "easier",
        "text": "About how long ago did Democritus argue that cutting matter "
                "must stop somewhere?",
        "options": [
            {"text": "About two thousand four hundred years ago.",
             "correct": True},
            {"text": "About one hundred and fifty years ago.",
             "correct": False,
             "why": "Far too recent. Chemists were weighing gases carefully "
                    "by then, and he had no measurements to work from."},
            {"text": "About four hundred years ago.",
             "correct": False,
             "why": "That would place him in the 1600s. He argued in about "
                    "400 BC, two thousand years earlier than that."},
            {"text": "About eight thousand years ago.",
             "correct": False,
             "why": "Far too long ago. That is before writing, let alone "
                    "before Greek argument about matter."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e14",
        "band": "easier",
        "text": "Cutting a piece of sugar in half leaves smaller sugar. "
                "Splitting one sugar particle leaves substances that are not "
                "sugar. What kind of change is the second one?",
        "options": [
            {"text": "A physical change, because the piece has only been made "
                     "smaller.",
             "correct": False,
             "why": "Nothing here has merely got smaller. The sugar has gone "
                    "and different substances are there instead."},
            {"text": "A chemical change, because different substances have "
                     "been made.",
             "correct": True},
            {"text": "A change of state, like melting or freezing.",
             "correct": False,
             "why": "A change of state leaves the same substance behind in a "
                    "new arrangement. Here the sugar itself has gone."},
            {"text": "No change worth the name, since the mass is the same.",
             "correct": False,
             "why": "Mass staying the same does not mean nothing happened. "
                    "What is present has changed."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e15",
        "band": "easier",
        "text": "Fifty millilitres of one liquid is added to fifty "
                "millilitres of another and the level reads 97 ml. How much "
                "liquid has been lost?",
        "options": [
            {"text": "Three millilitres, which evaporate while you are "
                     "pouring.",
             "correct": False,
             "why": "Evaporation would not give the same reading every time, "
                    "and a covered cylinder reads 97 ml as well."},
            {"text": "Three millilitres, which soak into the walls of the "
                     "glass.",
             "correct": False,
             "why": "Glass takes up no liquid. Nothing has left the cylinder "
                    "by that route or any other."},
            {"text": "None at all — every drop you poured is still in there.",
             "correct": True},
            {"text": "Three millilitres, which are lost in the froth on top.",
             "correct": False,
             "why": "The froth settles back into the liquid before you read "
                    "the level, so nothing leaves with it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e16",
        "band": "easier",
        "text": "The opening explainer says the model's claim is worth nothing "
                "to you until you have tried to break it. What does the rest "
                "of the page consist of?",
        "options": [
            {"text": "Two attempts to break the claim.",
             "correct": True},
            {"text": "A list of facts to learn by heart.",
             "correct": False,
             "why": "Nothing here is offered to be taken on trust. Each claim "
                    "is put to a test you run yourself."},
            {"text": "A history of who thought of the idea first.",
             "correct": False,
             "why": "The history is here, but as a footnote at the end. The "
                    "body of the work is two tests."},
            {"text": "Three worked examples of the same calculation.",
             "correct": False,
             "why": "There is arithmetic here, but it is built out of tests "
                    "rather than out of worked examples."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e17",
        "band": "easier",
        "text": "Which of these is being used as a model, in the sense this "
                "unit gives the word?",
        "options": [
            {"text": "Weighing a sugar cube on a balance.",
             "correct": False,
             "why": "That is a measurement. It records something you can see "
                    "rather than picturing something you cannot."},
            {"text": "Reading the level in a measuring cylinder.",
             "correct": False,
             "why": "That is a measurement too — a number read off the glass, "
                    "not a picture of anything hidden."},
            {"text": "Drawing matter as small round balls with spaces between "
                     "them.",
             "correct": True},
            {"text": "Timing how long a smell takes to cross a still room "
                     "with a stopwatch.",
             "correct": False,
             "why": "Another measurement. A model is the picture you use to "
                    "explain what a measurement like that shows."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e18",
        "band": "easier",
        "text": "A jeweller's magnifier shows a spoonful of sugar to be a heap "
                "of tiny clear crystals. Have you now seen a particle?",
        "options": [
            {"text": "Yes — a crystal is one particle, which is why it looks "
                     "clear.",
             "correct": False,
             "why": "A crystal you can see holds an enormous number of "
                    "particles. Clearness has nothing to do with it."},
            {"text": "No — every crystal still holds a huge number of "
                     "particles.",
             "correct": True},
            {"text": "Yes, but only the ones on the surface can be seen.",
             "correct": False,
             "why": "No part of a crystal is a single visible particle, on "
                    "the surface or anywhere else in it."},
            {"text": "No — sugar crystals are not made of particles.",
             "correct": False,
             "why": "They are, like all matter. The mistake is treating a "
                    "crystal you can see as one of them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e19",
        "band": "easier",
        "text": "What does the particle model say about the particles of two "
                "different substances?",
        "options": [
            {"text": "They may be different sizes from one another.",
             "correct": True},
            {"text": "They are the same size, no matter what the substance.",
             "correct": False,
             "why": "If that were so, two liquids could not mix to less than "
                    "their volumes added together, and they do."},
            {"text": "The particles of a liquid are larger than those of a "
                     "solid.",
             "correct": False,
             "why": "Size belongs to the substance, not to the state it "
                    "happens to be in at the time."},
            {"text": "The heavier substance has the larger particles.",
             "correct": False,
             "why": "Mass and size are separate things, and the model does "
                    "not tie one of them to the other."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e20",
        "band": "easier",
        "text": "The cutting bench talks about reaching a floor. What does the "
                "floor mean here?",
        "options": [
            {"text": "The point past which no smaller piece of that substance "
                     "exists.",
             "correct": True},
            {"text": "The point at which the knife finally becomes too blunt "
                     "to cut.",
             "correct": False,
             "why": "The knife never blunts on this bench. The limit belongs "
                    "to the sugar and not to the tool."},
            {"text": "The point at which the piece becomes too small to see.",
             "correct": False,
             "why": "The piece left sight long before the end, and went on "
                    "being sugar for many cuts after that."},
            {"text": "The number of cuts before the edge stops looking "
                     "smooth.",
             "correct": False,
             "why": "That comes four cuts earlier, and the cutting carries on "
                    "past it to the end."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e21",
        "band": "easier",
        "text": "A sugar cube is halved over and over on the bench. Which of "
                "these is unchanged at every cut until the very last one?",
        "options": [
            {"text": "The substance — it is sugar all the way down.",
             "correct": True},
            {"text": "The width of the piece.",
             "correct": False,
             "why": "Halving the width is what a cut does, so this changes at "
                    "every single one of them."},
            {"text": "The number of particles the piece still contains.",
             "correct": False,
             "why": "Half the particles go with the half you throw away, cut "
                    "after cut after cut."},
            {"text": "The mass of the piece.",
             "correct": False,
             "why": "Half the piece is discarded each time, so the mass "
                    "halves along with it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e22",
        "band": "easier",
        "text": "The gap rig runs three tests to find out what is in the space "
                "between particles. Which of these is one of the three?",
        "options": [
            {"text": "Weighing the sugar before and after it is cut.",
             "correct": False,
             "why": "Mass is not what the rig looks at. It asks whether there "
                    "is room for anything to move into."},
            {"text": "Squashing a gas into a smaller space.",
             "correct": True},
            {"text": "Heating the sugar until it melts and runs.",
             "correct": False,
             "why": "Melting comes later in the unit and says nothing about "
                    "what is in the gap."},
            {"text": "Shining a light through a beaker of liquid.",
             "correct": False,
             "why": "Light passing through tells you nothing about whether "
                    "that space is occupied."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e23",
        "band": "easier",
        "text": "A pump squashes 250 cm³ of air into a fifth of the space it "
                "started in. What volume does the air end up in?",
        "options": [
            {"text": "5 cm³",
             "correct": False,
             "why": "That divides 250 by fifty. A fifth of 250 cm³ is "
                    "50 cm³."},
            {"text": "125 cm³",
             "correct": False,
             "why": "That is half the starting volume. A fifth is a far "
                    "bigger squash than a half."},
            {"text": "50 cm³",
             "correct": True},
            {"text": "1250 cm³",
             "correct": False,
             "why": "That multiplies by five instead of dividing. Squashing "
                    "makes the volume smaller."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e24",
        "band": "easier",
        "text": "A single grain of sugar is broken into two smaller pieces. "
                "Which of these is true of the two pieces?",
        "options": [
            {"text": "One of them keeps the sweetness and the other one "
                     "loses it.",
             "correct": False,
             "why": "Sweetness belongs to the substance, and both pieces are "
                    "the same substance as before."},
            {"text": "Each piece is now a single particle of sugar.",
             "correct": False,
             "why": "A grain holds billions of particles, so breaking it in "
                    "two leaves billions in each piece."},
            {"text": "Both are sugar, and each still holds countless "
                     "particles.",
             "correct": True},
            {"text": "Neither is sugar any more, because the grain has been "
                     "broken.",
             "correct": False,
             "why": "Breaking a lump changes its size and nothing else about "
                    "what it is made of."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e25",
        "band": "easier",
        "text": "A student expects 100 ml and measures 97 ml. How many "
                "millilitres short is the measurement?",
        "options": [
            {"text": "3 ml",
             "correct": True},
            {"text": "7 ml",
             "correct": False,
             "why": "That is the gap between 97 and 90. The expected total "
                    "here is 100 ml."},
            {"text": "6 ml",
             "correct": False,
             "why": "That doubles the shortfall. The two volumes give one "
                    "expected total of 100 ml, not two."},
            {"text": "47 ml",
             "correct": False,
             "why": "That subtracts 50 from 97. The expected total is 100 ml, "
                    "which is both volumes added."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e26",
        "band": "easier",
        "text": "A student writes that matter means anything you can pick up "
                "and hold. Which everyday example shows that the rule is "
                "wrong?",
        "options": [
            {"text": "A sugar cube, which you can hold easily.",
             "correct": False,
             "why": "That fits the student's rule, so it cannot be the "
                    "example that breaks it."},
            {"text": "Air, which you cannot hold and is matter all the same.",
             "correct": True},
            {"text": "Sound, which you cannot hold and is not matter.",
             "correct": False,
             "why": "True on both counts, so it agrees with the rule rather "
                    "than breaking it."},
            {"text": "Light, which you cannot hold and is not matter either.",
             "correct": False,
             "why": "The rule and the science agree here as well, so it is no "
                    "test of the rule."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e27",
        "band": "easier",
        "text": "How many separate claims about matter does the key fact "
                "make?",
        "options": [
            {"text": "Two.",
             "correct": False,
             "why": "One more than that. Count them in the key fact and there "
                    "are three."},
            {"text": "Seven.",
             "correct": False,
             "why": "Far too many. The key fact is a single sentence and it "
                    "carries three."},
            {"text": "Five.",
             "correct": False,
             "why": "Too many. Count them in the key fact and there are "
                    "three."},
            {"text": "Three.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e28",
        "band": "easier",
        "text": "According to the model, which things are made of particles?",
        "options": [
            {"text": "Solids and liquids, but not a gas such as air.",
             "correct": False,
             "why": "All three states are matter, and the model covers matter "
                    "without exception."},
            {"text": "Everything that has mass and takes up space.",
             "correct": True},
            {"text": "Substances you can see, but not air.",
             "correct": False,
             "why": "Air has mass and takes up space, so the model covers it "
                    "like anything else."},
            {"text": "Pure substances, but not mixtures.",
             "correct": False,
             "why": "A mixture is made of substances, and each of those is "
                    "made of particles."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e29",
        "band": "easier",
        "text": "A student answers that the gaps between particles hold dust, "
                "then runs all three of the rig's tests. What happens?",
        "options": [
            {"text": "Every test gives a result that does not match what "
                     "really happens.",
             "correct": True},
            {"text": "One test fails and the other two work normally.",
             "correct": False,
             "why": "Filling the gap breaks all three at once, because all "
                    "three need space for something to move into."},
            {"text": "The tests cannot be run until a different answer is "
                     "chosen.",
             "correct": False,
             "why": "The rig runs them whatever you pick; that is how it "
                    "shows an answer failing."},
            {"text": "The tests agree with the answer, since dust is too "
                     "small to matter.",
             "correct": False,
             "why": "Size is not the point. Anything in the gap fills it, and "
                    "a filled gap leaves nothing to squash."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-e30",
        "band": "easier",
        "text": "50 ml of water is poured into another 50 ml of the same "
                "water. What does the model predict the level will read?",
        "options": [
            {"text": "100 ml, because particles of the same size cannot "
                     "settle into one another's gaps.",
             "correct": True},
            {"text": "Less than 97 ml, because there is twice as much water "
                     "for the particles to pack into.",
             "correct": False,
             "why": "How much liquid there is does not change how well it "
                    "packs. The particles are identical here."},
            {"text": "97 ml, exactly as it did for the water and alcohol.",
             "correct": False,
             "why": "Those three millilitres came from a difference in "
                    "particle size, and there is none here."},
            {"text": "More than 100 ml, because pouring adds bubbles to the "
                     "water.",
             "correct": False,
             "why": "Bubbles rise out as the liquid settles, and the "
                    "prediction is about the liquid itself."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 night 3 top-up ───────────────────────────────
    {
        "id": "c1-01-s10",
        "band": "standard",
        "text": "A sugar cube one centimetre across is halved four times, each "
                "cut leaving a piece half as wide. How wide is the piece now?",
        "options": [
            {"text": "2.5 mm",
             "correct": False,
             "why": "That is the width after two cuts. Two more halvings "
                    "follow before you stop."},
            {"text": "0.625 mm",
             "correct": True},
            {"text": "0.4 mm",
             "correct": False,
             "why": "That divides 10 mm by 25 rather than halving it four "
                    "times, which divides by 16."},
            {"text": "0.0625 mm",
             "correct": False,
             "why": "A factor of ten out. Halving 10 mm four times gives "
                    "0.625 mm."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s11",
        "band": "standard",
        "text": "The bench gives you a knife with a perfect edge that never "
                "blunts, and no limit on your patience. What does that setup "
                "rule out?",
        "options": [
            {"text": "That the tool or your effort is why the cutting stops.",
             "correct": True},
            {"text": "That sugar is the one substance with a floor.",
             "correct": False,
             "why": "The bench says nothing about other substances. It is "
                    "built to remove excuses about the knife."},
            {"text": "That the piece could ever become too small to see.",
             "correct": False,
             "why": "The piece does leave sight, long before the end. A "
                    "perfect knife is about cutting, not seeing."},
            {"text": "That the sugar might change into another substance.",
             "correct": False,
             "why": "It does change past the floor. What the perfect knife "
                    "removes is any blame on the tool."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s12",
        "band": "standard",
        "text": "The piece stops looking like a smooth block four cuts before "
                "the floor, and the floor is reached at cut twenty-four. At "
                "which cut does the edge first look grainy?",
        "options": [
            {"text": "Cut twenty.",
             "correct": True},
            {"text": "Cut four.",
             "correct": False,
             "why": "That counts four cuts from the start rather than four "
                    "back from the floor."},
            {"text": "Cut twenty-eight, four beyond the floor.",
             "correct": False,
             "why": "That adds the four instead of subtracting them, and the "
                    "bench stops at twenty-four."},
            {"text": "Cut twelve.",
             "correct": False,
             "why": "That is halfway. The change comes much nearer the end, "
                    "four cuts before it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s13",
        "band": "standard",
        "text": "100 ml of water is mixed with 100 ml of the alcohol from the "
                "demonstration, where 50 ml and 50 ml gave 97 ml. What reading "
                "does the model predict?",
        "options": [
            {"text": "Exactly 200 ml, because a shortfall only shows up when "
                     "the volumes are small enough.",
             "correct": False,
             "why": "Nothing about the packing depends on how much you pour. "
                    "Doubling both doubles the loss."},
            {"text": "About 194 ml, because twice as much of each liquid "
                     "loses twice as much volume.",
             "correct": True},
            {"text": "About 197 ml, because the same three millilitres go "
                     "missing.",
             "correct": False,
             "why": "The three millilitres were not a fixed toll. Twice the "
                    "liquid gives about twice the drop."},
            {"text": "About 97 ml, because that is the reading these two "
                     "liquids give.",
             "correct": False,
             "why": "97 ml was the reading for two 50 ml volumes. Pour twice "
                    "as much and you get about twice as much."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s14",
        "band": "standard",
        "text": "The demonstration is repeated the next day, with fresh liquid "
                "and a different measuring cylinder, and reads 97 ml again. "
                "What do those two changes rule out?",
        "options": [
            {"text": "That the first reading was a slip in the pouring or a "
                     "fault in one cylinder.",
             "correct": True},
            {"text": "That the particles of the two liquids are different "
                     "sizes.",
             "correct": False,
             "why": "Repeating cannot test that. What repeating tests is "
                    "whether the reading itself can be trusted."},
            {"text": "That the two liquids are pure rather than mixtures.",
             "correct": False,
             "why": "Using the same liquids again cannot show they are pure. "
                    "It shows the reading repeats."},
            {"text": "That the model is right about there being nothing "
                     "between the particles.",
             "correct": False,
             "why": "One repeated reading does not settle the model. It "
                    "settles whether the reading is reliable."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s15",
        "band": "standard",
        "text": "A student answers that the space between particles holds a "
                "gas nobody has discovered yet. Why does that answer not "
                "help?",
        "options": [
            {"text": "Because that gas would be particles with gaps of its "
                     "own, so the question starts again.",
             "correct": True},
            {"text": "Because an undiscovered gas could not be weighed, and a "
                     "model has to rest on weighing.",
             "correct": False,
             "why": "A model rests on measurements of many kinds. The trouble "
                    "here is that the answer never ends."},
            {"text": "Because a gas cannot exist inside a liquid.",
             "correct": False,
             "why": "Gases do dissolve in liquids. The trouble with the "
                    "answer is that it comes to no end."},
            {"text": "Because the gaps are far too small for any gas to fit.",
             "correct": False,
             "why": "Size is not the objection. Put any matter in the gap and "
                    "the same question asks itself again."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s16",
        "band": "standard",
        "text": "A second cube is cut from the same sugar, two centimetres on "
                "each side instead of one. How many halvings does it take to "
                "reach a single particle?",
        "options": [
            {"text": "Forty-eight, because the cube is twice the size.",
             "correct": False,
             "why": "Doubling the width adds one halving, not twice as many. "
                    "Each cut halves what is left."},
            {"text": "Twenty-three, because a bigger piece breaks more "
                     "easily.",
             "correct": False,
             "why": "How easily something breaks does not come into it. A "
                    "wider start needs one more halving."},
            {"text": "Twenty-five, one more than the smaller cube needed.",
             "correct": True},
            {"text": "Twenty-four, exactly as before, because the particle is "
                     "the same size.",
             "correct": False,
             "why": "The particle is the same, but you are starting from "
                    "twice the width, so one more cut is needed."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s17",
        "band": "standard",
        "text": "The mixed liquids read 97 ml instead of 100 ml. What has "
                "happened to the mass of the liquid in the cylinder?",
        "options": [
            {"text": "It has fallen by three per cent, in step with the "
                     "volume.",
             "correct": False,
             "why": "Mass does not follow volume here. No particles left, so "
                    "the two masses still add."},
            {"text": "It is the sum of the two masses, unchanged by the "
                     "packing.",
             "correct": True},
            {"text": "It has risen, because the liquid is now more tightly "
                     "packed.",
             "correct": False,
             "why": "Packing changes how much room the particles take up, not "
                    "how much matter is there."},
            {"text": "It cannot be worked out without weighing the mixture.",
             "correct": False,
             "why": "The model settles it: every particle you poured is still "
                    "there, so the masses add."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s18",
        "band": "standard",
        "text": "A student says the cutting bench shows that a sugar particle "
                "is the smallest thing there is. What is wrong with that?",
        "options": [
            {"text": "It is the smallest piece of sugar; smaller things "
                     "exist, but none of them is sugar.",
             "correct": True},
            {"text": "Nothing is wrong — the bench does show it is the "
                     "smallest thing.",
             "correct": False,
             "why": "The bench is about sugar. Split the particle and you get "
                    "smaller things that are not sugar."},
            {"text": "The bench shows nothing about how small anything is, "
                     "only about how sharp a knife can be.",
             "correct": False,
             "why": "The knife never blunts on this bench, so what it shows "
                    "is a limit belonging to the sugar."},
            {"text": "A sugar particle is not the smallest piece of sugar "
                     "either.",
             "correct": False,
             "why": "It is. The floor is exactly the point where no smaller "
                    "piece of sugar exists."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s19",
        "band": "standard",
        "text": "The three tests in the gap rig all probe one claim. Which "
                "claim is it?",
        "options": [
            {"text": "That particles are far too small to see.",
             "correct": False,
             "why": "Their size is taken for granted by the tests rather than "
                    "probed by any of them."},
            {"text": "That every substance has a cutting floor.",
             "correct": False,
             "why": "That is what the bench probed. The rig asks a different "
                    "question about the space."},
            {"text": "That the gaps between particles hold nothing.",
             "correct": True},
            {"text": "That the particles of a substance keep moving.",
             "correct": False,
             "why": "Motion is the claim this page leaves for the lessons "
                    "that follow it."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s20",
        "band": "standard",
        "text": "At every cut on the bench, half the piece is thrown away. "
                "Would keeping both halves move the floor?",
        "options": [
            {"text": "No — the floor is about how small one piece can be, not "
                     "how much sugar you have.",
             "correct": True},
            {"text": "Yes — with twice as much sugar you could go on halving "
                     "for twice as long.",
             "correct": False,
             "why": "Halving works on a single piece. More pieces give you "
                    "more to halve, not smaller ones."},
            {"text": "Yes — the discarded halves are what runs out first.",
             "correct": False,
             "why": "Nothing runs out. The cutting stops because a piece of "
                    "sugar cannot be smaller than one particle."},
            {"text": "No — but that is because the pieces would be too "
                     "awkward to hold.",
             "correct": False,
             "why": "Handling is not what stops the bench. The limit is in "
                    "the sugar itself."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s21",
        "band": "standard",
        "text": "Two volumes that should add to 100 ml give a reading of "
                "97 ml. What percentage of the expected total is missing from "
                "the reading?",
        "options": [
            {"text": "3%",
             "correct": True},
            {"text": "0.3%",
             "correct": False,
             "why": "A factor of ten out. Three parts in a hundred is three "
                    "per cent."},
            {"text": "30%",
             "correct": False,
             "why": "That would be thirty millilitres missing, ten times the "
                    "real shortfall."},
            {"text": "97%",
             "correct": False,
             "why": "That is the share of the expected total still in the "
                    "cylinder, not the share missing."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s22",
        "band": "standard",
        "text": "The demonstration is done the other way round: the alcohol is "
                "poured into the water instead. What does the model predict?",
        "options": [
            {"text": "97 ml, because the same particles pack the same way "
                     "whichever is poured first.",
             "correct": True},
            {"text": "100 ml, because pouring the smaller particles first "
                     "fills the gaps sooner.",
             "correct": False,
             "why": "The order of pouring does not change which particles are "
                    "small or where the gaps are."},
            {"text": "More than 100 ml, because the water has to make room "
                     "for the alcohol.",
             "correct": False,
             "why": "Nothing has to make room. The particles end up in the "
                    "same arrangement either way."},
            {"text": "Less than 97 ml, because the alcohol settles further "
                     "down the cylinder.",
             "correct": False,
             "why": "Where a liquid settles does not change how the particles "
                    "pack together."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s23",
        "band": "standard",
        "text": "Instead of a cube one centimetre across, the bench is given a "
                "single grain of sugar about half a millimetre across. What "
                "changes?",
        "options": [
            {"text": "More halvings are needed, because a grain is harder to "
                     "cut cleanly and squarely.",
             "correct": False,
             "why": "How hard a piece is to handle does not change the count. "
                    "A smaller start means fewer halvings."},
            {"text": "Fewer halvings are needed, because the piece starts "
                     "much nearer the floor.",
             "correct": True},
            {"text": "The same number, because the floor sits at twenty-four "
                     "halvings for sugar.",
             "correct": False,
             "why": "Twenty-four is the count from one centimetre. Start "
                    "smaller and you need fewer."},
            {"text": "No halvings are needed, because a grain is already one "
                     "particle.",
             "correct": False,
             "why": "A grain holds billions of particles. It is smaller than "
                    "a cube and still far from the floor."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s24",
        "band": "standard",
        "text": "Ten halvings take a centimetre of sugar down to about a "
                "hundredth of a millimetre, already far too small to see, and "
                "fourteen halvings are still to come. Roughly how much smaller "
                "again is a single particle?",
        "options": [
            {"text": "About fourteen times smaller.",
             "correct": False,
             "why": "Fourteen is the number of cuts, not the factor. Each one "
                    "halves the piece again."},
            {"text": "About sixteen thousand times smaller.",
             "correct": True},
            {"text": "About twenty-eight times smaller.",
             "correct": False,
             "why": "That doubles the number of cuts. Fourteen halvings "
                    "divide by two, fourteen times over."},
            {"text": "About a hundred times smaller.",
             "correct": False,
             "why": "Far too small a factor. Halving fourteen times divides "
                    "by about sixteen thousand."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s25",
        "band": "standard",
        "text": "A student explains the 97 ml by saying the alcohol particles "
                "shrink when they meet the water. Which part of the model does "
                "that contradict?",
        "options": [
            {"text": "That a particle keeps its size, and only the spacing "
                     "between particles changes.",
             "correct": True},
            {"text": "That particles are far too small for anyone to watch "
                     "one of them shrinking.",
             "correct": False,
             "why": "Whether you could watch it is beside the point. The "
                    "model says a particle does not change size."},
            {"text": "That the two liquids have particles of different sizes.",
             "correct": False,
             "why": "Different sizes are part of the explanation. What the "
                    "model refuses is a particle changing size."},
            {"text": "That nothing is lost when two liquids are mixed.",
             "correct": False,
             "why": "Nothing is lost on this student's story either, so this "
                    "is not where it goes wrong."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s26",
        "band": "standard",
        "text": "A student writes that the three millilitres were squeezed out "
                "of the cylinder as the liquids packed together. What is wrong "
                "with that?",
        "options": [
            {"text": "Three millilitres is far too small an amount to be "
                     "squeezed out of a cylinder.",
             "correct": False,
             "why": "The amount is not the trouble. The trouble is that "
                    "nothing left the cylinder at all."},
            {"text": "Liquids cannot be squeezed, so the packing could not "
                     "have happened either.",
             "correct": False,
             "why": "The packing does happen — that is what the reading "
                    "shows. What did not happen is anything leaving."},
            {"text": "Nothing came out. The same liquid is there, in less "
                     "room than before.",
             "correct": True},
            {"text": "It was the water, not the alcohol, that was squeezed "
                     "out of the glass.",
             "correct": False,
             "why": "Neither was. Every drop poured in is still in the "
                    "cylinder when you read the level."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s27",
        "band": "standard",
        "text": "Suggest one change to the mixing demonstration that would "
                "test whether particle size is what matters.",
        "options": [
            {"text": "Repeat it with twice as much of both liquids and see "
                     "whether the missing volume doubles as well.",
             "correct": False,
             "why": "That tests whether the effect scales with the amount, "
                    "not whether size is the reason for it."},
            {"text": "Repeat it with two liquids whose particles are the same "
                     "size and see whether the drop happens.",
             "correct": True},
            {"text": "Repeat it in a colder room and see whether the reading "
                     "changes.",
             "correct": False,
             "why": "Temperature is a different question. It would not tell "
                    "you whether size is what matters."},
            {"text": "Repeat it in a wider cylinder and see whether the "
                     "reading changes.",
             "correct": False,
             "why": "That tests the apparatus rather than the liquids, and "
                    "particle size is not what would change."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s28",
        "band": "standard",
        "text": "On the bench the width of the piece is given first in "
                "millimetres, then in micrometres, then in nanometres. Why "
                "does the unit keep changing?",
        "options": [
            {"text": "Because each unit belongs to a different substance.",
             "correct": False,
             "why": "The substance never changes on the bench. What changes "
                    "is how small the piece has become."},
            {"text": "Because using a smaller unit makes the piece sound "
                     "smaller than it really is, which flatters the bench.",
             "correct": False,
             "why": "The unit does not change the size, only how it is "
                    "written down for you to read."},
            {"text": "Because the ruler on the bench is replaced at every "
                     "cut.",
             "correct": False,
             "why": "There is one scale throughout. The unit changes because "
                    "the numbers would otherwise be unreadable."},
            {"text": "Because the piece shrinks by a factor of about sixteen "
                     "million, and one unit cannot show both ends.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s29",
        "band": "standard",
        "text": "The reveal says that melting, pressure and diffusion later in "
                "the unit are all one idea doing its work. Which idea?",
        "options": [
            {"text": "That matter comes in units with a floor, and below it "
                     "the substance stops existing.",
             "correct": True},
            {"text": "That particles are far too small for any microscope in "
                     "the world to show you properly.",
             "correct": False,
             "why": "They are, but that on its own explains none of melting, "
                    "pressure or diffusion."},
            {"text": "That every measurement made in science has to be "
                     "repeated by somebody else before it can count.",
             "correct": False,
             "why": "Repeating a measurement is good practice, not the idea "
                    "those three lessons rest on."},
            {"text": "That liquids take up less room when they are mixed "
                     "together.",
             "correct": False,
             "why": "That is one result of the model, not the idea the rest "
                    "of the unit is built on."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-s30",
        "band": "standard",
        "text": "The rig makes you commit to an answer before you run a test. "
                "Why does committing first make the test worth more?",
        "options": [
            {"text": "Because the answer you choose first is the one that the "
                     "rig then sets out to prove right.",
             "correct": False,
             "why": "A test that sets out to prove one answer is no test at "
                    "all. Committing is what lets a result defeat you."},
            {"text": "Because a prediction made in advance can be shown "
                     "wrong; one made afterwards cannot.",
             "correct": True},
            {"text": "Because choosing an answer first is what makes the "
                     "result of the test easier to remember later.",
             "correct": False,
             "why": "Remembering is not the point. A prediction made first is "
                    "one the result can defeat."},
            {"text": "Because a test gives a clearer result when you already "
                     "expect it.",
             "correct": False,
             "why": "The result is the same whether you expected it or not. "
                    "What changes is what it can prove."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 night 3 top-up ─────────────────────────────────
    {
        "id": "c1-01-h10",
        "band": "harder",
        "text": "A single sugar particle is about 0.6 nm across, and there are "
                "a million nanometres in a millimetre. About how many "
                "particles would lie along one millimetre?",
        "options": [
            {"text": "About 1.7 million.",
             "correct": True},
            {"text": "About 600,000.",
             "correct": False,
             "why": "That multiplies a million by 0.6 instead of dividing by "
                    "it. Smaller particles mean more of them fit."},
            {"text": "About 1,700.",
             "correct": False,
             "why": "A factor of a thousand out, as though a millimetre held "
                    "a thousand nanometres rather than a million."},
            {"text": "About 600 million.",
             "correct": False,
             "why": "Multiplying a million by 600 rather than dividing a "
                    "million by 0.6."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h11",
        "band": "harder",
        "text": "Suppose the bench started from a cube one metre on each side "
                "rather than one centimetre, and one metre is a hundred "
                "centimetres. About how many halvings would reach a single "
                "particle?",
        "options": [
            {"text": "About one hundred and twenty-four halvings.",
             "correct": False,
             "why": "That adds one halving for every centimetre. Each halving "
                    "covers a factor of two, so a hundredfold is about seven "
                    "of them."},
            {"text": "About thirty-one.",
             "correct": True},
            {"text": "About two thousand four hundred.",
             "correct": False,
             "why": "That multiplies the count by a hundred. Halvings add up "
                    "far more slowly than that."},
            {"text": "About forty-eight halvings.",
             "correct": False,
             "why": "That doubles the original count. Widening by a hundred "
                    "adds about seven halvings, not twenty-four."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h12",
        "band": "harder",
        "text": "Which result, had it come out that way, would have counted "
                "against the particle model?",
        "options": [
            {"text": "Two liquids mixing to exactly the sum of their volumes, "
                     "every time.",
             "correct": True},
            {"text": "A gas squashing into a fifth of the space it started "
                     "in.",
             "correct": False,
             "why": "That is what a gas does, and the model predicts it. A "
                    "result a model predicts cannot count against it."},
            {"text": "A sugar cube looking perfectly smooth to the naked eye.",
             "correct": False,
             "why": "Both the particle idea and the continuous idea predict "
                    "that, so it counts for neither."},
            {"text": "A smell crossing a still room with nobody stirring "
                     "it.",
             "correct": False,
             "why": "The model predicts that too. Evidence against it would "
                    "have to be something it forbids."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h13",
        "band": "harder",
        "text": "Put these four in order, smallest first: a grain of sugar, a "
                "single sugar particle, the width of a human hair, a sugar "
                "cube.",
        "options": [
            {"text": "Particle, grain, hair, cube.",
             "correct": False,
             "why": "A grain of sugar is several times wider than a hair, not "
                    "narrower than one."},
            {"text": "Hair, particle, grain, cube.",
             "correct": False,
             "why": "A particle is a hundred thousand times narrower than a "
                    "hair, so it has to come first."},
            {"text": "Particle, hair, cube, grain.",
             "correct": False,
             "why": "A cube is built from a great many grains, so the grain "
                    "comes before it and not after."},
            {"text": "Particle, hair, grain, cube.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h14",
        "band": "harder",
        "text": "Two pairs of liquids are mixed, 50 ml with 50 ml each time. "
                "In the first pair the particle sizes are very different; in "
                "the second they differ only slightly. Which mixture loses "
                "more volume?",
        "options": [
            {"text": "The second, because particles of a similar size pack "
                     "more neatly together.",
             "correct": False,
             "why": "Similar sizes pack no better into one another's gaps, "
                    "which is why the volume barely falls."},
            {"text": "The first, because a bigger size difference lets more "
                     "particles settle into gaps.",
             "correct": True},
            {"text": "Both lose the same, because the volumes poured are the "
                     "same.",
             "correct": False,
             "why": "The volumes poured set the starting point, not the loss. "
                    "The loss comes from the size difference."},
            {"text": "Neither loses any, because the particles are all far "
                     "too small to make a difference.",
             "correct": False,
             "why": "Their size is exactly what makes the difference. Small "
                    "particles fit gaps that large ones leave."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h15",
        "band": "harder",
        "text": "The two mistakes this page sets out to correct are blaming a "
                "blunt knife and putting something in the gaps. What do the "
                "two have in common?",
        "options": [
            {"text": "Both assume matter is made of particles, but of the "
                     "wrong kind.",
             "correct": False,
             "why": "Neither accepts particles as the model describes them. "
                    "Both are ways of keeping matter continuous."},
            {"text": "Both avoid accepting a limit, one on cutting and one on "
                     "empty space.",
             "correct": True},
            {"text": "Both come from careless measuring rather than from an "
                     "idea.",
             "correct": False,
             "why": "Neither is a measuring error. Both are reasonable ideas "
                    "that a test then defeats."},
            {"text": "Both are true of a solid but wrong for a liquid or a "
                     "gas.",
             "correct": False,
             "why": "Neither is true of any state. The bench and the rig "
                    "defeat them wherever they are tried."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h16",
        "band": "harder",
        "text": "The reveal says the model makes a far stronger claim than "
                "“things are small”. Which statement is that stronger claim?",
        "options": [
            {"text": "Matter is made of pieces far too small for any "
                     "microscope in the world to show.",
             "correct": False,
             "why": "That is the weaker claim about size. The strong one is "
                    "that there is a limit below which the substance is "
                    "gone."},
            {"text": "Matter can be divided as many times as your tools "
                     "allow.",
             "correct": False,
             "why": "That is the claim the model denies. Halving runs out "
                    "whatever tool you are given."},
            {"text": "Matter comes in units, and below one unit the substance "
                     "stops existing.",
             "correct": True},
            {"text": "Matter is mostly empty space, whatever state of matter "
                     "it happens to be in at the time.",
             "correct": False,
             "why": "A gas is mostly space and a solid is not — and this is a "
                    "claim about gaps, not about a floor."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h17",
        "band": "harder",
        "text": "The same bench is set up with a cube of salt instead of "
                "sugar, the same one centimetre across. Would it also reach "
                "its floor after twenty-four halvings?",
        "options": [
            {"text": "Yes — twenty-four is the number of halvings any "
                     "substance allows.",
             "correct": False,
             "why": "Twenty-four comes from one centimetre and the width of a "
                    "sugar particle. A different particle gives a different "
                    "count."},
            {"text": "No — salt has no floor, because it dissolves instead of "
                     "breaking.",
             "correct": False,
             "why": "Dissolving is a separate matter. Salt is made of "
                    "particles and has a floor like anything else."},
            {"text": "Yes — but only if the cube is cut with the same perfect "
                     "knife.",
             "correct": False,
             "why": "The knife is perfect in both cases. What could differ is "
                    "the width of one particle."},
            {"text": "Not necessarily — the count depends on how wide one "
                     "salt particle is.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h18",
        "band": "harder",
        "text": "Suppose two rival ideas about matter explained every "
                "observation anyone had made, and disagreed about nothing you "
                "could measure. How could a scientist decide between them?",
        "options": [
            {"text": "By choosing whichever of the two ideas is the simpler "
                     "one to picture in your head.",
             "correct": False,
             "why": "Being easy to picture is a convenience. It is not "
                    "evidence about which of them is true."},
            {"text": "By choosing whichever of the two was thought of first.",
             "correct": False,
             "why": "When an idea was thought of says nothing at all about "
                    "whether it is right."},
            {"text": "They could not, until someone found an observation the "
                     "two disagree about.",
             "correct": True},
            {"text": "By counting up how many well-known scientists support "
                     "each of the two rival ideas today.",
             "correct": False,
             "why": "A vote is not a measurement. Only an observation they "
                    "disagree about can separate them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h19",
        "band": "harder",
        "text": "A pupil concludes that the 97 ml reading proves the particle "
                "model. Evaluate that conclusion.",
        "options": [
            {"text": "It is right: a single measurement that fits the model "
                     "is enough on its own to settle it for us.",
             "correct": False,
             "why": "One fit can happen for other reasons. A model earns its "
                    "place across many different tests."},
            {"text": "It is wrong: measurements say nothing about particles "
                     "nobody can see.",
             "correct": False,
             "why": "Measurements are exactly how an invisible thing is "
                    "tested, and this one is good evidence."},
            {"text": "It is wrong: the reading is a measurement of volume, "
                     "which has nothing whatever to do with particles.",
             "correct": False,
             "why": "Volume is where the packing of particles shows up, which "
                    "is why the reading counts for anything."},
            {"text": "It is too strong: one reading supports the model, and "
                     "many measurements are what it rests on.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h20",
        "band": "harder",
        "text": "Which prediction does the particle idea make that the idea of "
                "continuous matter does not?",
        "options": [
            {"text": "That two liquids can mix to less than their volumes "
                     "added together.",
             "correct": True},
            {"text": "That a lump of sugar has a mass you can weigh on a "
                     "balance.",
             "correct": False,
             "why": "Continuous matter would weigh the same. Weight does not "
                    "choose between the two ideas."},
            {"text": "That a sugar cube keeps its shape until something "
                     "breaks it.",
             "correct": False,
             "why": "Continuous matter would keep its shape too, so neither "
                    "idea is picked out by that."},
            {"text": "That warm sugar and cold sugar taste the same as each "
                     "other.",
             "correct": False,
             "why": "Neither idea says anything about taste and temperature, "
                    "so it tests neither of them."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h21",
        "band": "harder",
        "text": "A gas squashing into a fifth of its space, and two liquids "
                "mixing to 97 ml, support the same claim. How do the two "
                "differ in what they do to the space between particles?",
        "options": [
            {"text": "One works on a gas and the other on a liquid, and "
                     "nothing else about the two differs.",
             "correct": False,
             "why": "The states differ, but so does the method: one squeezes "
                    "the space out, the other fills it."},
            {"text": "One is a measurement and the other is a demonstration "
                     "with no number in it.",
             "correct": False,
             "why": "Both are measurements, and both give a number you can "
                    "check for yourself."},
            {"text": "One removes the space by force; the other fills it with "
                     "another liquid's particles.",
             "correct": True},
            {"text": "One of them tests the cutting floor and the other tests "
                     "the space between particles.",
             "correct": False,
             "why": "Both test the space. The floor was the cutting bench's "
                    "business, not theirs."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h22",
        "band": "harder",
        "text": "Three things are offered in support of the claim that the "
                "gaps hold nothing: a gas squashing, the 97 ml reading, and "
                "the model being simple to picture. Which is not evidence?",
        "options": [
            {"text": "The gas squashing, because a bicycle pump is a machine "
                     "rather than a scientific experiment.",
             "correct": False,
             "why": "A pump gives a result you can measure and repeat, which "
                    "is what makes it evidence."},
            {"text": "The 97 ml reading, because one single reading of a "
                     "cylinder is far too little to prove anything much.",
             "correct": False,
             "why": "One reading is limited, but it is still evidence. Being "
                    "simple to picture is not evidence at all."},
            {"text": "The model being simple to picture, because being easy "
                     "to imagine is not a measurement.",
             "correct": True},
            {"text": "All three count equally, since each one makes the claim "
                     "easier to believe.",
             "correct": False,
             "why": "Being easier to believe is not the test. Two of the "
                    "three are measurements and one is not."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h23",
        "band": "harder",
        "text": "A pupil objects that the cutting bench is only a drawing on a "
                "screen, so it cannot show anything about real sugar. Evaluate "
                "the objection.",
        "options": [
            {"text": "The objection holds: nothing that is drawn on a "
                     "computer screen can support a scientific claim.",
             "correct": False,
             "why": "Drawings and models are used throughout science. What "
                    "they cannot do alone is settle a question."},
            {"text": "The objection fails: the bench is a recording of a real "
                     "cube being cut up.",
             "correct": False,
             "why": "No real knife could make those cuts. The bench shows the "
                    "arithmetic, not a filmed experiment."},
            {"text": "The objection fails: a drawing on a screen counts as "
                     "evidence so long as it has been drawn out accurately.",
             "correct": False,
             "why": "Accuracy in a drawing is not evidence. Evidence is a "
                    "measurement that could have come out otherwise."},
            {"text": "The bench sets out the arithmetic of halving; real "
                     "measurements are what make the claim stick.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h24",
        "band": "harder",
        "text": "The stretch passage says an idea becomes science when a "
                "number forces it. Which numbers forced the particle idea?",
        "options": [
            {"text": "The number of scientists who came round to agreeing "
                     "with Democritus.",
             "correct": False,
             "why": "Agreement is not a measurement. What settled it was "
                    "results that could have come out otherwise."},
            {"text": "Readings from combining gases, balanced masses and "
                     "mixed volumes.",
             "correct": True},
            {"text": "The two thousand years the idea waited before anyone "
                     "accepted it.",
             "correct": False,
             "why": "Time settles nothing. The idea waited precisely because "
                    "no measurement had separated it from its rival."},
            {"text": "The number of different substances the Greeks had "
                     "already named.",
             "correct": False,
             "why": "Naming substances is not measuring them. The tie was "
                    "broken by numbers from experiments."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h25",
        "band": "harder",
        "text": "The same two liquids are mixed again, but this time 10 ml "
                "with 10 ml. By about how much would the model expect the "
                "reading to fall short of 20 ml?",
        "options": [
            {"text": "About 3 ml, the same shortfall as before.",
             "correct": False,
             "why": "The shortfall scales with how much you pour. A fifth of "
                    "the liquid gives about a fifth of the drop."},
            {"text": "About 1.5 ml, half of the original shortfall.",
             "correct": False,
             "why": "These volumes are a fifth of the originals, not a half, "
                    "so the drop is a fifth as big."},
            {"text": "About 0.6 ml.",
             "correct": True},
            {"text": "None — a shortfall this small would not appear.",
             "correct": False,
             "why": "It is the same effect, simply a fifth of the size, which "
                    "comes to about 0.6 ml."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h26",
        "band": "harder",
        "text": "Suppose someone halved a substance ten thousand times and "
                "found it unchanged at every step. Which claim of the model "
                "would be in trouble?",
        "options": [
            {"text": "That there is a floor you cannot cut past.",
             "correct": True},
            {"text": "That the particles are far too small to see.",
             "correct": False,
             "why": "Nobody would have seen anything at any step, so their "
                    "size is not what the result challenges."},
            {"text": "That there is nothing between the particles.",
             "correct": False,
             "why": "Cutting says nothing about what lies between. That claim "
                    "is tested by squashing and by mixing."},
            {"text": "That different substances have differently sized "
                     "particles.",
             "correct": False,
             "why": "One substance is being cut here, so nothing is being "
                    "compared with anything else."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h27",
        "band": "harder",
        "text": "The opening says a claim is worth nothing to you until you "
                "have tried to break it. What does trying to break a claim "
                "give you that being told it does not?",
        "options": [
            {"text": "A claim you have tested is easier to remember "
                     "afterwards.",
             "correct": False,
             "why": "It may well be, but that is about memory rather than "
                    "about whether the claim is sound."},
            {"text": "A claim you have tested could have failed, so passing "
                     "means something.",
             "correct": True},
            {"text": "A claim you have tested cannot be questioned again "
                     "later on.",
             "correct": False,
             "why": "It can, and later lessons do exactly that. Testing "
                    "strengthens a claim; it does not close it."},
            {"text": "A claim you have tested has been proved once and for "
                     "all.",
             "correct": False,
             "why": "A test that is passed is support, not proof. This model "
                    "has limits that turn up later in the unit."},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h28",
        "band": "harder",
        "text": "A pupil insists the model must be wrong, because 50 and 50 "
                "make 100. Evaluate the argument.",
        "options": [
            {"text": "The argument holds, and the 97 ml reading must simply "
                     "be a mistake made in the measuring.",
             "correct": False,
             "why": "The reading repeats with fresh liquid and other "
                    "cylinders, so it is not a slip."},
            {"text": "The argument holds for volumes but not for masses, "
                     "which do add.",
             "correct": False,
             "why": "Masses do add, but that does not rescue the argument. "
                    "Volumes are under no such obligation."},
            {"text": "The argument fails, because 50 ml and 50 ml make 97 ml "
                     "for every possible pair of liquids there is.",
             "correct": False,
             "why": "They do not. Two liquids with same-sized particles come "
                    "out very near 100 ml."},
            {"text": "Volumes add when nothing settles into a gap, and the "
                     "cylinder shows that something does.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h29",
        "band": "harder",
        "text": "This page makes two separate attempts on the model's claims. "
                "What does each attempt establish?",
        "options": [
            {"text": "The cutting establishes that particles are small; the "
                     "gap tests establish that they move.",
             "correct": False,
             "why": "The bench is about a limit to cutting rather than mere "
                    "smallness, and the rig is about the space."},
            {"text": "Both establish the same thing from two directions.",
             "correct": False,
             "why": "They test two different claims: one about a limit to "
                    "cutting, one about what lies between."},
            {"text": "The cutting establishes the gaps; the gap tests "
                     "establish the floor.",
             "correct": False,
             "why": "It is the other way round: cutting finds the floor, and "
                    "the rig probes the space."},
            {"text": "The cutting establishes a floor; the gap tests "
                     "establish that the space holds nothing.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "c1-01-h30",
        "band": "harder",
        "text": "A pupil suggests testing the floor by halving a real sugar "
                "cube with a real knife on a real bench. Explain why that "
                "would settle nothing.",
        "options": [
            {"text": "A real sugar cube would be far too small to be halved "
                     "even once without losing some of it.",
             "correct": False,
             "why": "A centimetre cube halves easily by hand. The trouble "
                    "comes many cuts later, with the tool."},
            {"text": "A real experiment can never test an idea about "
                     "something that is far too small for anyone to see.",
             "correct": False,
             "why": "Real experiments are how this model is tested. The "
                    "mixing demonstration is one of them."},
            {"text": "A real cube would melt from the heat of your hands "
                     "before you finished.",
             "correct": False,
             "why": "Sugar does not melt in the hand. What defeats the "
                    "attempt is the knife, not the temperature."},
            {"text": "A real knife stops working long before the floor, so "
                     "the result would be about the knife.",
             "correct": True},
        ],
        "figure": None,
    },
]
