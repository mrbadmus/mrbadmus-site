# -*- coding: utf-8 -*-
"""KS3 "Start here" — the two-option guess every lesson opens on.

Mide's rule (2 Oct 2026, written for KS4 and applied to KS3 on 9 Oct 2026):

    "Start here" is "If you had to guess, …?" with exactly two options —
    simple everyday wording any Year 7 pupil can answer, not patronising for a
    strong Year 9, the answer not given away in the title, the scene or the big
    question above it, and a friendly reply to each option that leads into the
    teaching.

HOW IT REACHES THE PAGE. Each entry below is merged over its lesson's
`phenomenon` by `ks3_data.build_units()`, so every reader of the lesson — the
generator, the gates, the answer-length audit — sees the same opener. The
lesson modules themselves are NOT edited: they are transcriptions of Design's
approved pages, and their docstrings say so; this file is the one place the
departure from those pages is recorded. A lesson with no entry here keeps its
old hook byte for byte.

`r_hook()` renders an entry as KS3's own `keyed-commit` markup (c1-03, c1-06):
two `.ks3-option` buttons, one reply per option, then the bridge everyone
reads. `shared/ks3.js`'s `wireKeyedCommit` already drives exactly that, so no
shared asset changes. The options stay re-choosable and are never marked
(R3); the reply opens with "Good guess." or "Fair guess.", as KS4's `Ks4Guess`
does.

FIELDS
  question      the whole commit line, starting "If you had to guess, " and
                ending "?".
  options       exactly two (text, reply) pairs, in the order shown.
  answer        0 or 1 — the option the science says is right. Used for the
                "Good guess." / "Fair guess." word and by the answer-length
                audit; never shown as a mark.
  bridge        the paragraph under the reply, read whichever was picked.
  title, scene  optional: replace the hook's heading / prompt, only where the
                old one gave the answer away or no longer fits the guess.
  big_question  optional: replaces the lesson's big question, only where it
                gave the answer away.
"""

PREFIX = "If you had to guess, "

START_HERE = {

    # ── Year 7 · B1 Cells and organisation ──────────────────────────────────────

    # life-processes — brief's example, unchanged (flame fails only respiration;
    # cells settle it).
    "life-processes": dict(
        question="If you had to guess, is a candle flame alive?",
        options=[
            ("Yes, it is alive",
             "It does almost everything on the list of life processes. But a "
             "flame is not made of cells, and every living thing is."),
            ("No, it is not alive",
             "A flame moves, grows, feeds and makes waste, and it is still not"
             " alive. What it is missing is cells."),
        ],
        answer=1,
        bridge="Doing the life processes is not enough on its own. What "
               "settles it is what a thing is <em>made of</em>.",
        big_question="A candle flame moves, grows, feeds and makes waste. What"
                     " decides whether something is alive?",
    ),

    # using-a-microscope — old hook question (which lens first) cut to weakest vs
    # strongest. Correct reply no longer copies the s-think line; neither reply
    # says why (the bench measures field of view). big_question rewritten:
    # "highest magnification and you see almost nothing" gave it away.
    "using-a-microscope": dict(
        question="If you had to guess, which lens should you start with to "
                 "find the cells?",
        options=[
            ("The weakest lens",
             "That is the right start. Find the cells on the weakest lens "
             "first, then move up to a stronger one."),
            ("The strongest lens",
             "The strongest lens does give the most detail. But it makes cells"
             " very hard to find in the first place."),
        ],
        answer=0,
        bridge="Next: look at Sam's method for viewing onion skin and decide "
               "which steps would cost him.",
        big_question="Changing only the lens turned a clear picture into a "
                     "smear. How do you use a microscope so that does not "
                     "happen?",
    ),

    # animal-and-plant-cells — old hook question cut to yes/no on the seven
    # tiles. Title/scene rewritten ("same parts list", "overlap far more than
    # most people guess" gave it away); big_question's second half presupposed an
    # animal-only part. Correct reply no longer gives the 4 + 3 count the bench
    # is built to reveal.
    "animal-and-plant-cells": dict(
        title="A cheek cell and an oak leaf cell.",
        scene="Seven parts in all. Some are found in a cell scraped from your "
              "cheek. Some are found in a cell cut from an oak leaf.",
        question="If you had to guess, does the cheek cell have any of these "
                 "seven parts that the oak leaf cell lacks?",
        options=[
            ("Yes, at least one",
             "Animals and plants do live very differently. But every part in "
             "your cheek cell is in the oak leaf cell too."),
            ("No, not one",
             "Every part in your cheek cell is in the leaf cell too. The leaf "
             "cell just has some extra parts of its own."),
        ],
        answer=1,
        bridge="Next: a bench with both cells on it, so you can check part by "
               "part.",
        big_question="What do plant cells and animal cells have in common, and"
                     " what is different?",
    ),

    # specialised-cells — old hook question cut to room vs speed. Title and scene
    # untouched (pair with unicellular-organisms). Wrong option avoids "narrower
    # vessels", which a sharp pupil could argue is partly right.
    "specialised-cells": dict(
        question="If you had to guess, what does the red blood cell gain by "
                 "throwing its nucleus away?",
        options=[
            ("More room inside",
             "Room is the gain. The space the nucleus leaves is packed with "
             "haemoglobin, the red stuff that carries oxygen."),
            ("A faster trip",
             "Less baggage does sound faster, but blood cells are carried "
             "along by the flow. What the cell gains is room for its cargo."),
        ],
        answer=0,
        bridge="Every specialised cell makes a trade like this. Next: four "
               "cells on one bench, to see what each has given up and gained.",
    ),

    # levels-of-organisation — old hook question cut to layers vs more cells.
    # Title rewritten ("Same cells. Same number." ruled out the wrong option).
    # Correct option avoids "organised" so it does not echo the H1 "Levels of
    # organisation"; order flipped for balance.
    "levels-of-organisation": dict(
        title="Stomach cells in a dish, and a stomach.",
        scene="Scientists can grow real stomach cells in a dish. They live for"
              " weeks, making acid and enzymes. Put a sandwich in the dish and"
              " it sits there. Put it in a stomach and twenty minutes later it"
              " is gone.",
        question="If you had to guess, what lets a real stomach do what the "
                 "dish of cells cannot?",
        options=[
            ("Many more cells",
             "More cells sounds sensible, but a dish with a thousand times "
             "more would still leave the sandwich untouched. It is how they "
             "are arranged that counts."),
            ("Cells arranged in layers",
             "Layers, each with its own job: muscle to churn the food, a "
             "lining to make acid and enzymes. They only work as a team."),
        ],
        answer=1,
        bridge="That gives a ladder of levels, from one cell up to a whole "
               "living thing. Next: zoom from a whole plant down to one cell, "
               "one level at a time.",
    ),

    # unicellular-organisms — old hook question cut to "does every job itself" vs
    # "can swim about". Wrong reply no longer uses the sperm-cell example, which
    # is the answer to mystery cells 1 and 2 in the settles-it task further down.
    # Big question kept (it does not give the answer); its "whole animal" is
    # listed as a lesson-text issue.
    "unicellular-organisms": dict(
        question="If you had to guess, what makes the Paramecium a whole "
                 "living thing and not just a piece of one?",
        options=[
            ("It does every job itself",
             "A Paramecium has nobody to feed it or clean up after it. It has "
             "to feed, grow, move and reproduce all on its own."),
            ("It can swim about freely",
             "Swimming is the eye-catching part. But what makes it a whole "
             "living thing is that it does every job of staying alive by "
             "itself."),
        ],
        answer=0,
        bridge="Next: look at pond water and cheek cells under the microscope,"
               " then work out which facts really settle it.",
    ),


    # ── Year 7 · B2 Movement skeleton and muscles ───────────────────────────────

    # what-the-skeleton-does — old hook question cut to "what relies on it" vs
    # size. Option reworded off "job" so it does not echo the H1 "What the
    # skeleton does"; replies no longer say ribs help you breathe (the ribcage
    # switch-off prediction). big_question rewritten: "a broken rib makes every
    # breath hurt" pointed at the job.
    "what-the-skeleton-does": dict(
        question="If you had to guess, what matters most for how bad a broken "
                 "bone is?",
        options=[
            ("What relies on the bone",
             "A finger bone has little relying on it. A femur holds up your "
             "whole body, so far more fails when it breaks."),
            ("How big the bone is",
             "A femur is huge, so size is tempting. But what counts is how "
             "much else relies on that bone."),
        ],
        answer=0,
        bridge="Next: switch off one part of the skeleton at a time and follow"
               " the damage.",
        big_question="Every break is broken bone, and every break heals. So "
                     "why is one break a nuisance and another a disaster?",
    ),

    # joints — old hook question (why does the shoulder give way?) cut to
    # directions vs weak muscles. Title rewritten (it stated the trade);
    # big_question rewritten ("what is the shoulder buying" gave it away). Rail
    # label "Range or stability" kept in mind: see arguable calls.
    "joints": dict(
        title="Two joints in the same arm.",
        question="If you had to guess, why does the shoulder come out of place"
                 " so much more than the elbow?",
        options=[
            ("It moves in more directions",
             "Every direction a joint can move in is a direction it cannot "
             "hold against. The shoulder swings almost anywhere, so almost "
             "anything can push it out."),
            ("Its muscles are weaker",
             "Strength is not the limit here. It is what the shape of the "
             "joint allows."),
        ],
        answer=0,
        bridge="Next: bend and twist four joint shapes on a bench and see "
               "which ones refuse.",
        big_question="Shoulders dislocate far more often than elbows. What "
                     "makes the two joints different?",
    ),

    # antagonistic-muscle-pairs — ANGLE CHANGED: the H1 "Antagonistic muscle
    # pairs" and the rail label "Only ever a pull" both answer "same muscle or a
    # different one?". New guess: where the straightening muscle sits (front or
    # back), which still takes a moment's reasoning. Old title, scene and big
    # question kept, so the rail label lands.
    "antagonistic-muscle-pairs": dict(
        question="If you had to guess, when you push a door open, where is the"
                 " muscle that straightens your arm?",
        options=[
            ("On the front of your upper arm",
             "The front is where the biceps is, the muscle you flex. But it "
             "can only pull, and a pull from the front bends the arm. "
             "Straightening needs a pull from behind."),
            ("On the back of your upper arm",
             "A muscle on the back of the upper arm, the triceps, pulls on the"
             " bone behind your elbow and swings the forearm straight."),
        ],
        answer=1,
        bridge="One muscle bends the arm and another straightens it, and each "
               "one only ever pulls. Next: drive a model arm with both muscles"
               " and see what each one does.",
    ),

    # biomechanics-forces-in-the-body — ANGLE RESTORED to the old hook's "why":
    # the writer's "same as the weight, or far more?" is answered by the railbar
    # label "Eight times harder". Title rewritten ("losing, badly... on purpose"
    # leaned on the answer); scene keeps the bag of sugar (the vocab note refers
    # to it) and the 10 N / 80 N, but drops the distances, whose "only about 4
    # cm" pointed at the answer. Old big question kept: it asks the same why
    # without answering it.
    "biomechanics-forces-in-the-body": dict(
        title="A bag of sugar in your hand.",
        scene="Hold a bag of sugar on your flat hand, forearm level. It weighs"
              " 10 N. To hold it there, your biceps pulls with about 80 N.",
        question="If you had to guess, why does your biceps have to pull so "
                 "much harder than the bag weighs?",
        options=[
            ("Some of its pull is wasted",
             "Muscles can feel like they waste effort, but none of this pull "
             "is lost. The bag is far from your elbow and the muscle is "
             "attached close to it, so it must pull harder."),
            ("It is attached near the elbow",
             "The bag sits far out along your forearm, but the muscle pulls "
             "close to the elbow. A pull that close in has to be much bigger "
             "to hold the bag up."),
        ],
        answer=1,
        bridge="Next: a forearm rig where you change the load and the "
               "distances, then work out the muscle's force yourself.",
    ),


    # ── Year 7 · B3 Nutrition and digestion ─────────────────────────────────────

    # a-balanced-diet — old hook question (what is the orange doing?) cut to tiny
    # vital substance vs energy. Scene trimmed (the "right amounts" sentence
    # ruled out energy); big_question rewritten (it said tiny amounts are
    # essential).
    "a-balanced-diet": dict(
        scene="Plate A is white rice, chicken, oil, water and salt, every day,"
              " nothing else. Plate B is the same food plus one orange. The "
              "person eating Plate A dies. The person eating Plate B is fine.",
        question="If you had to guess, what in the orange saves the person on "
                 "Plate B?",
        options=[
            ("A tiny vital substance",
             "Just 50 mg of vitamin C, a tiny fraction of the meal. Without it"
             " the body cannot build the protein that holds your body "
             "together."),
            ("A bit more energy",
             "The rice and oil on Plate A are already full of energy. What the"
             " plate lacks is a tiny amount of vitamin C."),
        ],
        answer=0,
        bridge="So balance is not about equal amounts. Next: set seven "
               "nutrients to the amounts you think a day needs, then see the "
               "real ones.",
        big_question="What does “balanced” actually mean for a diet?",
    ),

    # food-tests — back to the old hook's own question ("tube 2 on its own"): the
    # writer's "does a blue tube prove no sugar?" is answered by the scene, since
    # the same milk goes red in tube 1. Scene reworded to drop "Nobody made a
    # mistake, the difference is", which framed the answer.
    "food-tests": dict(
        scene="Same bottle of milk, same Benedict's solution, same water bath."
              " Tube 1 was heated for five minutes and comes out brick red. "
              "Tube 2 was heated for thirty seconds and comes out blue.",
        question="If you had to guess, what does tube 2 on its own tell you "
                 "about the milk?",
        options=[
            ("It has no sugar in it",
             "Blue does look like a clear no. But the same milk goes brick red"
             " in tube 1, after a longer heat. A blue tube only says the test "
             "did not find sugar this time."),
            ("Nothing either way",
             "On its own, a blue tube only says the test did not find sugar "
             "this time. That is a fact about the test, not about the milk."),
        ],
        answer=1,
        bridge="Next: run four tests on five foods, say what you expect each "
               "time, and see what you may write down.",
    ),

    # energy-in-food-and-what-you-need — old hook question (why the different
    # outcome?) cut to energy needed vs digestion. Scene rewritten (reading vs
    # 120 km cyclist gave it away; first sentence no longer repeats the title);
    # "need" not "use", since the lesson teaches energy is transferred, not used
    # up. big_question rewritten ("whose day it is").
    "energy-in-food-and-what-you-need": dict(
        scene="A 68-year-old and a 25-year-old eat the same meals, in the same"
              " portions, at the same times: about 11 000 kJ a day each. After"
              " a month, one has gained mass and one has lost it.",
        question="If you had to guess, what explains the different outcome?",
        options=[
            ("How much energy each body needs",
             "Bodies need very different amounts of energy in a day. The same "
             "food is more than enough for one and not enough for the other."),
            ("How well each body digests food",
             "Digestion does vary a little, but not enough to turn the same "
             "meals into a gain for one and a loss for the other. What differs"
             " is how much energy each body needs."),
        ],
        answer=0,
        bridge="Next: feed five different people for a day and watch the same "
               "plate fit one and not another.",
        big_question="How much food does a body need in a day, and what "
                     "decides it?",
    ),

    # when-diet-goes-wrong — ANGLE CHANGED: the writer's "more food or different
    # food?" was answered by the scene (they already eat more than enough) and
    # not unarguable (a surplus, or a gut that cannot absorb, is not fixed by
    # different food). New guess is the old hook's paradox itself: can someone
    # eating this much be malnourished? Title rewritten (it stated "severely
    # malnourished"); scene drops the diagnosis sentence. Rail "Full plate" still
    # lands. big_question rewritten ("on a full plate").
    "when-diet-goes-wrong": dict(
        title="A patient on 13 000 kJ a day.",
        scene="Not going short of food. Not skipping meals. Taking in more "
              "energy than an adult needs, every day.",
        question="If you had to guess, could this patient be malnourished?",
        options=[
            ("Yes, they could be",
             "Malnourished means badly nourished, not underfed. A big diet can"
             " still be missing something the body needs, such as iron or a "
             "vitamin."),
            ("No, not on that much",
             "Most people think malnourished means underfed. But it means "
             "badly nourished, and a diet can be huge in energy and still be "
             "missing iron or a vitamin."),
        ],
        answer=0,
        bridge="Malnutrition is not one problem but three separate ones. Next:"
               " the three side by side, then five clinics to diagnose.",
        big_question="What can go wrong with a diet, and what does each "
                     "problem do to the body?",
    ),

    # the-digestive-system — old hook question kept as yes/no. Replies reworded
    # so "chains" is tied to starch, not left unexplained. Title, scene and
    # big_question already fine.
    "the-digestive-system": dict(
        question="If you had to guess, could that smooth liquid go straight "
                 "into your blood?",
        options=[
            ("Yes, it is smooth enough",
             "Smooth does feel finished. But blades only make the pieces "
             "smaller. The starch inside is still in long chains, far too big "
             "to cross into your blood."),
            ("No, the bits are too big",
             "Smooth is not the same as small enough. The starch in the liquid"
             " is still in long chains, far too big to cross into your blood."),
        ],
        answer=1,
        bridge="Digestion has to cut the molecules themselves, and enzymes do "
               "that. Next: follow a sandwich through seven stops of the gut.",
    ),

    # enzymes-in-digestion — old hook question (what is an enzyme doing?) cut to
    # still there vs used up. Title rewritten ("a teaspoon digests a kilogram"
    # leaned on reuse; rail "A teaspoon" still lands); scene rewritten (weighing
    # before and after showed it unchanged); big_question rewritten ("still be
    # there at the end").
    "enzymes-in-digestion": dict(
        title="A teaspoon of amylase and a kilogram of starch.",
        scene="Mix a teaspoon of amylase, an enzyme from your spit, with a "
              "kilogram of starch and wait. By the end, the starch is gone.",
        question="If you had to guess, is the amylase still there once the "
                 "starch has gone?",
        options=[
            ("Yes, all of it",
             "All of it is still there. An enzyme is a catalyst: it speeds a "
             "reaction up without being used up, so a teaspoon goes a very "
             "long way."),
            ("No, it gets used up",
             "The starch certainly is used up. But an enzyme ends each job "
             "exactly as it started, ready for the next."),
        ],
        answer=0,
        bridge="Next: run the reaction on a bench and watch three counters, "
               "including one that counts the enzyme.",
        big_question="What is an enzyme, and what can stop it from working?",
    ),

    # absorption-and-the-small-intestine — old hook question cut to coiled vs
    # folded. big_question rewritten (the old one only restated the scene's
    # numbers).
    "absorption-and-the-small-intestine": dict(
        question="If you had to guess, how does the intestine get sixty times "
                 "the surface of a hose?",
        options=[
            ("It is coiled up",
             "The gut is packed in tight. But coiling a tube does not change "
             "its inside surface. The wall itself has to be folded."),
            ("Its wall is folded",
             "Folded, and then folded again. Folds with bumps on them, and "
             "tinier bumps on those, give far more surface than a plain tube "
             "of the same size."),
        ],
        answer=1,
        bridge="Next: switch on each level of folding and watch the absorbing "
               "surface grow.",
        big_question="How can a tube the size of a garden hose absorb a whole "
                     "meal?",
    ),

    # bacteria-in-the-gut — ANGLE CHANGED from "healthier or sicker?": a germ-
    # free mouse in a sterile bubble meets no infections, so "sicker" is
    # arguable. New guess uses the lesson's own headline fact (about 30% more
    # food), where the tempting wrong answer ("bacteria eat your food, so less")
    # is a real intuition. Scene rewritten (it listed every bad outcome);
    # big_question rewritten ("not a failure, it is the arrangement"). Rail
    # "Germ-free mouse" and the all-off "you have just built the germ-free mouse"
    # still land.
    "bacteria-in-the-gut": dict(
        scene="Sterile food, sterile air, sterile water, no bacteria anywhere "
              "in or on it, ever. The mouse lives its whole life in a sealed, "
              "germ-free bubble.",
        question="If you had to guess, does a mouse with no bacteria need more"
                 " food than a normal mouse, or less?",
        options=[
            ("More food",
             "About 30% more. Gut bacteria release energy from parts of the "
             "food the mouse cannot digest itself, so without them that energy"
             " is lost."),
            ("Less food",
             "That makes sense if bacteria just share your food. But this "
             "mouse needs about 30% more, because gut bacteria release energy "
             "from fibre it cannot digest itself."),
        ],
        answer=0,
        bridge="Food is only one of the jobs the bacteria were doing. Next: "
               "switch off their five jobs one at a time and see what breaks.",
        big_question="Your gut is home to trillions of bacteria. What are they"
                     " doing there?",
    ),


    # ── Year 7 · C1 Particles and their behaviour ───────────────────────────────

    # particle-model — old hook question (where did the 3 ml go?) cut to
    # evaporated vs squeezed into gaps. big_question rewritten ("nothing
    # evaporated" ruled out the wrong option).
    "particle-model": dict(
        question="If you had to guess, where did the missing 3 ml go?",
        options=[
            ("It evaporated away",
             "Some alcohol does evaporate, but nowhere near 3 ml, and you get "
             "97 every time. The liquid is all still there, tucked into gaps."),
            ("It squeezed into gaps",
             "Nothing is lost. Every drop is still in the cylinder. Liquids "
             "are not solid all the way through, so the small bits of one "
             "settle into gaps between the big bits of the other."),
        ],
        answer=1,
        bridge="That idea, that matter is made of separate particles with "
               "gaps, is the whole model. Next: try to break it by cutting a "
               "sugar cube in half, again and again.",
        big_question="50 ml of water and 50 ml of alcohol make 97 ml, every "
                     "time. What does that tell us about liquids?",
    ),

    # solids-liquids-and-gases — old hook question (so what got bigger?) cut to
    # particles vs gaps. big_question rewritten ("the same particles" leaned on
    # the particles not changing).
    "solids-liquids-and-gases": dict(
        question="If you had to guess, when steel expands in the heat, what "
                 "gets bigger?",
        options=[
            ("Each particle swells up",
             "Swelling is the natural thing to picture, but the particles stay"
             " exactly the same size. It is the gaps between them that grow."),
            ("The gaps between them",
             "Heat makes the particles jiggle harder, so each needs more room "
             "and the gaps grow. The particles themselves stay exactly the "
             "same size."),
        ],
        answer=1,
        bridge="Same particles, different spacing and movement: that is the "
               "idea behind every state. Next: watch one substance as a solid,"
               " a liquid and a gas.",
        big_question="Ice, water and steam are the same substance. So what "
                     "exactly is different about them?",
    ),

    # changes-of-state — keeps the old sealed-bag commit as a two-way guess (less
    # vs exactly 50 g). Title and scene changed: "Seal it in the bag first" and
    # "nothing can get in or out of" both announce the answer; "sealed" stays so
    # the answer is unarguable and the "Sealed bag" rail stop still lands.
    "changes-of-state": dict(
        title="An ice cube in a bag.",
        scene="An ice cube, 50 g, sealed inside a bag. Weigh it. Leave it on "
              "the bench until it is a puddle of water, then weigh the bag "
              "again.",
        question="If you had to guess, once the ice has melted, will the "
                 "balance read less than 50 g, or exactly 50 g?",
        options=[
            ("A bit less",
             "It can feel as if some of the ice has gone, because a solid has "
             "turned into a puddle. But the bag is sealed, so nothing has left"
             " it. Every particle is still inside."),
            ("Exactly 50 g",
             "Melting moves the particles around but never removes any, and "
             "nothing can leave a sealed bag. The balance has nothing to "
             "report."),
        ],
        answer=1,
        bridge="The same is true of boiling, freezing and condensing: the mass"
               " never changes. Next: heat 50 g of ice steadily and watch the "
               "temperature.",
    ),

    # gas-pressure — old hook asked what bursts the can; two-way version asks
    # whether the "empty" can is really empty. Title and big question changed:
    # "Nothing in it" and "It is empty. What is there to explode?" both push the
    # pupil to the answer. The new big question keeps the warning, because rung
    # 2's feedback says "it is why the warning is on the can". Bridge stops short
    # of the wall-hits mechanism, which the bench gate asks next.
    "gas-pressure": dict(
        title="The can that sounds empty.",
        question="If you had to guess, is that can really empty inside?",
        options=[
            ("No, there is gas inside",
             "The can is full of gas. There is no such thing as a sealed can "
             "with nothing in it, even when it has stopped spraying."),
            ("Yes, it is really empty",
             "Nothing sprays out, so it certainly seems empty. But the space "
             "inside is full of gas that has simply stopped pushing its way "
             "out."),
        ],
        answer=0,
        bridge="Heat that gas and within a minute the steel gives way. Next: "
               "what a gas is actually doing inside a sealed container.",
        big_question="A used-up aerosol can carries a warning: do not put it "
                     "on a fire, it may explode. What would make it burst?",
    ),

    # diffusion — old hook asked what moved the perfume; two-way version asks
    # whether it arrives with no draught at all (PART-10 is elicited by the
    # hook). Title, scene and big question changed: "No draught..." and "The
    # perfume still reaches you" give the result away, and "what covers the last
    # stretch" presupposes a mechanism. "Still room" kept for the rail stop.
    # Replies avoid saying the particles never stop (the bench gate asks that).
    "diffusion": dict(
        title="A bottle of perfume in a still room.",
        scene="A bottle of perfume is opened at the far end of a room. The "
              "windows are shut, the air is dead still, and a candle flame at "
              "the centre of the room stands perfectly upright, so there is no"
              " draught at all.",
        question="If you had to guess, with no draught to carry it, will the "
                 "smell of the perfume ever reach you?",
        options=[
            ("Yes, in the end",
             "The perfume particles spread out by themselves, bouncing off the"
             " air particles on the way. It is slow, but no draught is needed."),
            ("No, it needs a draught",
             "In a real room draughts do carry a smell most of the way. But "
             "even with the air perfectly still, the perfume gets there on its"
             " own."),
        ],
        answer=0,
        bridge="Spreading out with nothing pushing has a name: diffusion. "
               "Next: a drop of dye in still water, followed one particle at a"
               " time.",
        big_question="Someone opens a bottle of perfume at the far end of a "
                     "room. Before long you can smell it. How does it get to "
                     "you?",
    ),

    # testing-the-model — FLAG (science, believed right): relies on solid
    # paraffin wax sinking in its own melt (solid ~0.90 g/cm3, liquid ~0.78;
    # candle wax shrinks as it sets), consistent with the lesson's "Almost every
    # other solid sinks in its own liquid". The old hook ("what does a wrong
    # prediction mean?") is the later #s-verdict commit, so it cannot be reused.
    # Reviewer tried an ice-expansion guess instead, but the first rail stop "Ice
    # floats" sits on screen above the hook and gives that one away; the wax
    # guess survives it, and "Ice floats" actively tempts the wrong answer. Title
    # and scene changed: the old ones state that the model fails; the new title
    # puts ice back in the hook so the rail stop still lands. Old big question
    # kept: it gives nothing away about wax. Bridge leaves the model's verdict on
    # ice to the evidence bench.
    "testing-the-model": dict(
        title="Ice floats. What about wax?",
        scene="Ice floats on water. Now some candle wax is melted in a pan, "
              "and a lump of solid wax is dropped into it.",
        question="If you had to guess, will the lump float on the melted wax, "
                 "or sink in it?",
        options=[
            ("It floats",
             "That is what ice does on water. But ice is the odd one out. For "
             "almost everything else, wax included, the solid sinks."),
            ("It sinks",
             "Almost every solid sinks in its own liquid. Its particles are "
             "packed more tightly, so a lump of it is heavier than the same "
             "amount of liquid."),
        ],
        answer=1,
        bridge="So why does ice float? Next: seven observations, ice among "
               "them, and whether the particle model can explain each one.",
    ),


    # ── Year 7 · C2 Atoms elements and compounds ────────────────────────────────

    # the-atom-daltons-model — old hook asked what explains fifteen centuries of
    # failure; two-way version asks whether modern kit could finally do it
    # (restricted to furnaces, acids and mixing, so nuclear transmutation is not
    # arguable; the stretch draws the same chemistry-only boundary). Title
    # changed: "Fifteen centuries of failure is a result" tells the pupil the
    # failure was inevitable. Big question changed: "what would have to be true
    # for that to be impossible" presupposes impossibility.
    "the-atom-daltons-model": dict(
        title="Fifteen centuries of trying.",
        question="If you had to guess, could modern furnaces, acids and mixing"
                 " finally turn lead into gold?",
        options=[
            ("Yes, with modern kit",
             "Modern kit is far better than a medieval furnace. But heating "
             "and mixing only rearrange atoms. They never change one kind of "
             "atom into another."),
            ("No, however good the kit",
             "Lead atoms and gold atoms are different kinds. Heating, burning "
             "and mixing only rearrange atoms, and no reaction changes one "
             "kind into the other."),
        ],
        answer=1,
        bridge="John Dalton wrote this idea down in 1803, and modern chemistry"
               " starts there. Next: his three claims, and what happens when "
               "you switch one off.",
        big_question="People tried to turn lead into gold for fifteen hundred "
                     "years and never once managed it. Why not?",
    ),

    # elements — old hook asked how to test for an element; two-way version is
    # look at it vs try to break it down, worded as the bench's own test labels.
    # The bench asks for a verdict on each sample, not for the best test, and no
    # sample (brass) is named here, so the think block is not pre-answered.
    "elements": dict(
        question="If you had to guess, how would you tell whether a sample is "
                 "on that list: try to break it down, or look at it closely?",
        options=[
            ("Try to break it down",
             "If anything simpler comes out, it was never on the list. An "
             "element is made of one kind of atom, so there is nothing simpler"
             " inside it."),
            ("Look at it closely",
             "Looking is where everyone starts. But different substances can "
             "look alike, so looks cannot settle it. Breaking it down can."),
        ],
        answer=0,
        bridge="Next: six unlabelled samples and only eight tests to share "
               "between them.",
    ),

    # compounds — old hook asked where the iron went; two-way version is burnt
    # away vs joined the sulfur. The tempting "still there, just coated" option
    # is left out because the think block asks it later. Replies stop short of
    # saying why the magnet ignores it. Big question changed: "Same two elements
    # before and after heating" tells the pupil the iron did not burn away.
    # Bridge changed: the explainer straight after the hook defines a compound,
    # so the draft bridge repeated it.
    "compounds": dict(
        question="If you had to guess, has the iron burnt away, or joined up "
                 "with the sulfur?",
        options=[
            ("It burnt away to nothing",
             "Heating can make things glow and seem to vanish. But the iron "
             "has not left the dish. It has joined the sulfur to make a new "
             "substance."),
            ("It joined the sulfur",
             "Every bit of the iron is still in the dish, now joined to the "
             "sulfur in a new substance."),
        ],
        answer=1,
        bridge="Stirring two elements together and heating them together are "
               "very different things. Next: test the mixture, heat it, and "
               "test it again.",
        big_question="Iron and sulfur in a dish. Heat them, and afterwards the"
                     " magnet is useless. What changed?",
    ),

    # chemical-symbols — REWRITTEN by the reviewer. The old commit ("why
    # symbols?") has "to save time" as an arguable part-truth, and the old scene
    # shows the formulae working. The writer's "could you recognise anything?"
    # was trivially yes (numbers, pictures) and its big question ("Osaka ...
    # write the same thing for salt") gave the answer away. New guess: will the
    # formula for water in a Japanese textbook be H2O or written in Japanese.
    # Everyday, tempting, and it leads straight to the rail stop "Why symbols".
    # Big question changed so it no longer says the chemists all write the same
    # thing.
    "chemical-symbols": dict(
        title="A chemistry book in Japanese.",
        scene="You cannot read a word of Japanese. Someone hands you their "
              "chemistry textbook, open at a page about water.",
        question="If you had to guess, when the book gives the formula for "
                 "water, will it be H2O, or written in Japanese?",
        options=[
            ("H2O, as here",
             "The words around it are all Japanese, but the formula is H2O, "
             "exactly as you would write it."),
            ("Written in Japanese",
             "Everything else on the page is in Japanese. But chemical symbols"
             " are shared by every country, so water is H2O there too."),
        ],
        answer=0,
        bridge="That is what symbols are for: each one means exactly one "
               "element, in every country, with nothing to translate. Next: "
               "where nine symbols come from.",
        big_question="Chemists in Lagos, Osaka and São Paulo all need to write"
                     " down salt. What do they write, and why?",
    ),

    # formulae — REWRITTEN by the reviewer. The first rail stop "One atom apart"
    # sits on screen above the hook, so the draft's "different substance or
    # stronger water?" was given away. Old title and scene kept (they now set up
    # the one-extra-atom fact the rail names). New guess: would bubbling oxygen
    # through water make the dangerous liquid? The rail tempts "yes"; the answer
    # (no: mixing is not joining an atom into each particle) is this lesson's
    # idea that a formula counts the atoms joined in one particle. Old big
    # question kept: it gives nothing away about this guess.
    "formulae": dict(
        question="If you had to guess, would bubbling oxygen gas through water"
                 " turn it into the dangerous liquid?",
        options=[
            ("Yes, it would",
             "The extra atom is oxygen. But bubbling only mixes the gas into "
             "the water. Nothing joins an oxygen atom into each water "
             "particle."),
            ("No, it would not",
             "The oxygen just mixes in with the water. To make the other "
             "liquid, an extra oxygen atom has to be joined into every single "
             "particle."),
        ],
        answer=1,
        bridge="A substance is decided by the atoms joined together in each "
               "particle, not by what is floating around them. Next: build "
               "formulae and find out which ones are real substances.",
    ),

    # conservation-of-mass — old hook asked where the wax went; two-way version
    # is heat and light vs gas in the air (heat and light is the real
    # misconception, ATOM-11). The old hook already answered the think block, so
    # this does not newly pre-answer it. Big question changed: "Neither is"
    # states the result.
    "conservation-of-mass": dict(
        question="If you had to guess, where did the wax go?",
        options=[
            ("Into gas in the air",
             "The wax joined with oxygen from the air and drifted off as "
             "invisible gases. It is still somewhere in the room."),
            ("Into heat and light",
             "A candle does give off heat and light. But heat and light are "
             "not made of anything you can weigh. The wax itself leaves as "
             "gas."),
        ],
        answer=0,
        bridge="Those gases have mass, but in an open room nobody weighs them."
               " Next: a balance, with the flask open and then sealed.",
        big_question="A candle burns down to nothing. A nail rusts and gets "
                     "heavier. What is happening to the mass in each?",
    ),


    # ── Year 7 · C3 Mixtures and separation ─────────────────────────────────────

    # pure-or-mixture — keeps the old hook (juice vs distilled water) as a two-
    # way guess; the carton label is the tempting wrong option (MIX-01 is
    # elicited by the hook). Title, scene and big question changed: "means
    # nothing to a chemist" and "Only one of them is" say which label is empty.
    # The "Pure juice" think block asks the same question again, as it did after
    # the old hook. Wrong reply reworded: "so that is a fair guess" doubled the
    # page's own "Fair guess."
    "pure-or-mixture": dict(
        title="Two honest labels.",
        scene="A carton says <strong>100% pure orange juice</strong>. A bottle"
              " in the lab says <strong>distilled water</strong>. Both labels "
              "are honest.",
        question="If you had to guess, which of these would a chemist call "
                 "pure?",
        options=[
            ("The orange juice",
             "The carton does say 100% pure. But to a chemist, pure means one "
             "substance, and juice is water, sugars, acids and pulp together. "
             "The distilled water is the pure one."),
            ("The distilled water",
             "Distilled water is one substance and nothing else. Juice is "
             "water, sugars, acids, pulp and more all together."),
        ],
        answer=1,
        bridge="Chemists count substances, not labels. Next: eight samples on "
               "the bench, and a decision on each.",
        big_question="A carton of juice, a gold ring and a bottle of lab water"
                     " all claim to be pure. What is the chemist actually "
                     "asking?",
    ),

    # dissolving-and-solutions — keeps the old balance commit as a two-way guess
    # (still 110 g vs less); "more than 110 g" is dropped. Title kept. Big
    # question changed: "vanishes without a trace. Where has it gone" presupposes
    # it has gone somewhere. Bridge changed: the draft's "Next" skipped the two
    # vocabulary explainers that come straight after the hook.
    "dissolving-and-solutions": dict(
        question="If you had to guess, will the balance still read 110 g now, "
                 "or less?",
        options=[
            ("Still 110 g",
             "The sugar has not gone. It has broken up into particles too "
             "small to see and spread through the water, and the balance "
             "counts every gram."),
            ("Less than 110 g",
             "You cannot see any sugar. But nothing has left the beaker. The "
             "sugar is still there, in pieces far too small to see."),
        ],
        answer=0,
        bridge="A substance that dissolves is hidden, not removed. Next: the "
               "names for each part of a solution, then what decides how much "
               "can dissolve.",
        big_question="Sugar stirred into water seems to vanish. What has "
                     "really happened to it, and what decides how much can go "
                     "in?",
    ),

    # filtration — keeps the old sand/salt papers commit as a two-way guess (just
    # the sand vs sand and salt). The steps block asks a close cousin ("where
    # does the salt end up?") before the pour, exactly as it did after the old
    # hook, whose reveal answered it outright. Big question changed: "cannot be
    # done with any paper at all" states the result.
    "filtration": dict(
        question="If you had to guess, will the filter papers catch sand and "
                 "salt, or just the sand?",
        options=[
            ("Just the sand",
             "The sand grains are far too big to fit through the paper. The "
             "dissolved salt goes straight through with the water."),
            ("Sand and salt",
             "Salt is a solid, so you might expect the paper to catch it. But "
             "it has dissolved into the water, and its particles are far too "
             "small to be caught."),
        ],
        answer=0,
        bridge="Filtering only catches a solid that has not dissolved. Next: "
               "watch it done step by step, then put the steps in order "
               "yourself.",
        big_question="Filter paper can take sand out of water. What about "
                     "salt, and why?",
    ),

    # evaporation-and-crystallisation — keeps the old boiled dish vs windowsill
    # dish commit as a two-way guess; fast-is-better is the tempting wrong idea.
    # Title and scene kept. Big question changed: "a question of how much of a
    # hurry you are in" gives the answer away. Bridge changed: the draft repeated
    # the scene's "same mass of salt"; it now answers the old hook's "why would
    # anyone care?" from the old reveal.
    "evaporation-and-crystallisation": dict(
        question="If you had to guess, which dish has the bigger crystals in "
                 "it?",
        options=[
            ("The boiled dish",
             "Heat speeds everything up. But a fast boil starts thousands of "
             "tiny crystals at once, and none of them gets big."),
            ("The windowsill dish",
             "Slow evaporation lets the salt particles join up in an orderly "
             "way. A few crystals start, and they grow big."),
        ],
        answer=1,
        bridge="A big, clean crystal is also good evidence that you have one "
               "substance, not a dried-out puddle of everything. Next: three "
               "ways of removing the water to try for yourself.",
        big_question="The salt is dissolved and invisible. How do you get it "
                     "back, and does the way you do it matter?",
    ),

    # distillation — keeps the old life-raft commit as a two-way guess (boil and
    # catch the steam vs wait for the salt to sink). The still's sea-water gate
    # asks a close cousin, as it did after the old hook, whose reveal answered it
    # outright. Title and scene kept. Big question changed: "Evaporation throws
    # the water away" points at catching it, and the draft replacement restated
    # the hook question; the new one covers the whole lesson (salt water and
    # ethanol).
    "distillation": dict(
        question="If you had to guess, how do you get fresh water out of the "
                 "sea water?",
        options=[
            ("Boil it, catch the steam",
             "Only the water boils off. The salt stays behind, and the steam "
             "turns back into fresh water when it meets a cold surface."),
            ("Wait for the salt to sink",
             "Salt does sink if you tip in more than will dissolve. But salt "
             "that has dissolved stays spread through the water, however long "
             "you wait."),
        ],
        answer=0,
        bridge="That is distillation: boil to separate, cool to collect. Next:"
               " run a still yourself and see what comes out.",
        big_question="Sea water is almost all water, and you still cannot "
                     "drink it. How do you get a pure liquid back out of a "
                     "mixture?",
    ),

    # chromatography — old hook already asked "what happens to a dot of ink?";
    # two-way version is stays black vs splits into colours. Reviewer narrowed it
    # to the NOTE's ink: the lesson's Pen D gives a single blue spot, so "a black
    # dot splits into colours" is not true of every pen on this page, while the
    # note's ink splits into three. Title, scene and big question changed: "Black
    # ink is not black. It is three or four colours pretending" gives the answer
    # away. "Four black pens" kept for the rail stop.
    "chromatography": dict(
        title="Four black pens, one note.",
        scene="A note has been written in black ink, and four black pens have "
              "been collected. All four look identical on paper, and staring "
              "at them will not tell you which pen wrote the note. You put a "
              "dot of the note's ink near the bottom of a strip of paper and "
              "let water creep up through it.",
        question="If you had to guess, as the water creeps up, will the black "
                 "dot stay black, or split into other colours?",
        options=[
            ("It stays plain black",
             "Black does look like a single colour. But this ink is a mix of "
             "dyes, and as the water climbs they come apart into separate "
             "coloured spots."),
            ("It splits into colours",
             "The black is really a mix of dyes. The water carries each dye up"
             " the paper a different distance, so they separate."),
        ],
        answer=1,
        bridge="Pens mix their black from different sets of dyes, so the "
               "patterns can tell them apart. Next: set the paper up and run "
               "it.",
        big_question="Four black inks look identical on paper. How could you "
                     "tell which pen wrote the note?",
    ),

    # proving-something-is-pure — angle changed by the writer and KEPT: a two-way
    # "weigh it or measure when it melts?" would answer the plan-critique block
    # that comes straight after (it rules on weighing, looking, dissolving), so
    # the guess is the melting behaviour itself: does the impure powder start
    # melting lower or higher? Lower is the lesson's own key fact; salt on an icy
    # road is the lesson's own stretch example. Title and scene changed: the old
    # title says one bag is impure. The bench still has to find WHICH batch, from
    # ranges and repeats.
    "proving-something-is-pure": dict(
        title="Three bags of white powder.",
        scene="A supplier has sent three bags of the same white powder, all "
              "labelled pure. One of them has something else mixed in. All "
              "three look identical, and the label is not evidence. You heat a"
              " little of each until it melts.",
        question="If you had to guess, will the powder with something mixed in"
                 " start melting at a lower temperature, or a higher one?",
        options=[
            ("A lower temperature",
             "Something mixed in breaks up the neat pattern of the particles, "
             "so it starts to give way sooner. Salt on an icy road works in "
             "the same way."),
            ("A higher temperature",
             "More stuff might seem to need more heat. But the extra stuff "
             "gets in the way of the neat pattern, so the powder starts "
             "melting at a lower temperature."),
        ],
        answer=0,
        bridge="That gives you something a thermometer can measure, whatever "
               "the label says. Next: judge a student's plan, then measure the"
               " melting points.",
    ),


    # ── Year 7 · P3 Describing motion ───────────────────────────────────────────

    # speed — old hook asked what you need to know to compare the fly and plane;
    # two-way version asks which is really faster (FORCE-02, elicited by the
    # hook). Fly and plane kept: compare-pairs Pair 2 is labelled "the one from
    # the top of the page", and the old title and scene already stated the plane
    # was faster. Title, scene and big question changed: the old title and scene
    # state the answer; the old big question repeated the guess.
    "speed": dict(
        title="A fly and a plane.",
        scene="A fly is 30 cm from your eye and crosses your view in half a "
              "second. A plane is 10 km up and takes a full minute to cross "
              "the same patch of sky.",
        question="If you had to guess, which one is really going faster?",
        options=[
            ("The fly",
             "It does look quicker, and eyes are easy to fool. The fly is "
             "close, so it seems to rush across. The plane is far away, so it "
             "seems to crawl, but it is far faster."),
            ("The plane",
             "Because it is so far away, it looks slow. It really covers about"
             " 250 metres every second."),
        ],
        answer=1,
        bridge="To compare them fairly you need two measurements, not one "
               "look. Next: a trolley, two light gates and a timer.",
        big_question="A fly crosses your view in half a second. A plane takes "
                     "a full minute to cross the same patch of sky. What do "
                     "you need to know to compare how fast they are really "
                     "going?",
    ),

    # distance-time-graphs — REWRITTEN by the reviewer. The lesson's H1
    # "Distance–time graphs" sits on screen above the hook and tells the pupil
    # what the height is, so the draft's "distance from the start or speed?" was
    # given away. New guess: while the walker waits at the door, does the line go
    # flat or drop to the bottom? Dropping to zero is the tempting speed-reading
    # of the line; the answer needs the pupil to work out what the height means,
    # which the bridge then names (rail "What the height means"). Scene changed
    # so it no longer says the line goes flat; title kept. Big question changed:
    # the old one repeats "rises, goes flat".
    "distance-time-graphs": dict(
        scene="Someone walks 6 m down a level corridor, waits at a door, then "
              "runs the last 12 m. A motion sensor at the start draws a graph "
              "of the journey, and as they walk the line climbs. The floor "
              "never changed height.",
        question="If you had to guess, while the walker waits at the door, "
                 "does the line go flat, or drop to the bottom?",
        options=[
            ("It goes flat",
             "The walker stays 6 m from the start the whole time they wait, so"
             " the line stays at that height."),
            ("It drops to the bottom",
             "Stopping can feel like dropping to nothing. But the walker is "
             "still 6 m from the start, and that is what the line shows."),
        ],
        answer=0,
        bridge="The height of the line is the distance from the start, so it "
               "only comes down if the walker comes back. Next: plot seven "
               "readings from a motion sensor and read the whole journey.",
        big_question="What can you read from a graph of a journey?",
    ),

    # relative-motion — REWRITTEN by the reviewer. The first rail stop "Relative
    # to what" and the H1 "Relative motion" sit on screen above the hook, so the
    # draft's "one real speed, or depends who is looking?" was given away. New
    # guess, from the lesson's own stretch ("no experiment done inside a smoothly
    # moving room can tell you how fast the room is going"): with the blinds down
    # on a smooth, silent train, could you tell you were moving? The rail now
    # lands in the bridge. Scene adds "steady" and "perfectly smooth, silent" so
    # the answer is unarguable (bumps and wheel noise are taken away). Title and
    # big question kept.
    "relative-motion": dict(
        scene="Your train is doing a steady 100 km/h on a perfectly smooth, "
              "silent track. A second train pulls alongside, also doing 100 "
              "km/h. Through the window it hangs there, motionless, close "
              "enough to read a book over someone's shoulder.",
        question="If you had to guess, with the blinds pulled down, could you "
                 "tell that your own train was moving at all?",
        options=[
            ("Yes, you would feel it",
             "On a real train you feel bumps and hear the wheels. But take "
             "those away and a steady 100 km/h feels exactly like standing "
             "still."),
            ("No, you could not tell",
             "At a steady speed on a smooth track, everything inside the train"
             " behaves just as it would standing still. Only looking out tells"
             " you."),
        ],
        answer=1,
        bridge="So whether something is moving, and how fast, depends on what "
               "you measure it against. Next: two cars on a road, three "
               "different observers, and a different number for each.",
    ),


    # ── Year 7 · P4 Forces ──────────────────────────────────────────────────────

    # what-a-force-is — the rail label "The wall pushed you" is fixed lesson text
    # and answers "what pushed you?", so the draft's guess was given away on
    # load. Angle changed to the hook's own misconception (FORCE-12, elicited_by
    # s-hook): do you carry the wall's push with you as you roll? Old title,
    # scene and big question kept, so the rail label still names the hook.
    "what-a-force-is": dict(
        question="If you had to guess, as you roll away, are you still "
                 "carrying the wall's push with you?",
        options=[
            ("Yes, until it runs out",
             "That is one of the oldest ideas about forces, and almost "
             "everyone starts with it. But a push is not stuff you can carry. "
             "It stops the moment your hands leave the wall."),
            ("No, it has already stopped",
             "The wall's push lasts only while your hands are on it. You keep "
             "rolling because you are already moving, not because you are "
             "carrying a push."),
        ],
        answer=1,
        bridge="A force is a push or a pull between two objects, and it only "
               "lasts while they act on each other. Next: five forces, and the"
               " object on the other end of each.",
    ),

    # drawing-and-adding-forces — the rail label is "Tug of war", so the hook
    # keeps the tug of war (the draft had dropped it). Old title ("the winner is
    # a subtraction") and scene gave the answer away; both rewritten. Guess is
    # the old 40 N / 25 N question cut to the correct 15 N against the hook's own
    # misconception, "the bigger pull wins" at 40 N (FORCE-16). Big question
    # kept: it states no result.
    "drawing-and-adding-forces": dict(
        title="A tug of war on ice.",
        scene="Two friends play tug of war with a sledge on ice, one rope "
              "each. One pulls it to the right with 40 N. The other pulls it "
              "to the left with 25 N.",
        question="If you had to guess, how hard is the sledge pulled overall?",
        options=[
            ("15 N to the right",
             "The 25 N pull cancels 25 N of the 40 N pull. The 15 N left over "
             "is the only pull the sledge responds to."),
            ("40 N to the right",
             "The 40 N side does win, so the sledge goes right. But the other "
             "rope is still pulling back, and it cancels 25 N of the 40 N. "
             "That leaves 15 N."),
        ],
        answer=0,
        bridge="That one leftover force has a name: the resultant force. Next:"
               " set two pulls on a sledge yourself and read the single arrow "
               "that replaces them.",
    ),

    # balanced-and-unbalanced — old title ("The table is holding up 8 N") gave
    # away the upward push. Guess: is anything pushing up on a resting book?
    # Tempting wrong option is "nothing" (FORCE-20, the hook's misconception).
    # Title and scene rewritten around two identical books so the rail label "Two
    # identical books" still names the hook; the old big question repeated the
    # new scene, so it is replaced with one that does not.
    "balanced-and-unbalanced": dict(
        title="Two identical books.",
        scene="Two identical books. One rests on a table and stays exactly "
              "where it is. The other is held out in mid-air and let go, and "
              "it falls.",
        question="If you had to guess, is anything pushing up on the book that"
                 " rests on the table?",
        options=[
            ("Yes, something is",
             "The table is squashed a tiny bit, too little to see, and it "
             "pushes up on the book. It pushes exactly as hard as gravity "
             "pulls the book down."),
            ("No, nothing is",
             "The table looks as if it is doing nothing, so that is easy to "
             "think. But gravity is still pulling the book down, and something"
             " must push up to stop it falling. The table does."),
        ],
        answer=0,
        bridge="Forces that cancel like this are called balanced, and nothing "
               "about the motion changes. Next: swap the table for other "
               "supports and see when they give way.",
        big_question="Both books are pulled down just as hard. So what decides"
                     " whether something stays put or starts to move?",
    ),

    # what-forces-do-to-motion — old title, scene ("at a steady speed", "nothing
    # pushing it") and big question all gave the answer. Guess: does a sliding
    # stone need something pushing it to keep going? Tempting wrong option is yes
    # (FORCE-24). Rail label "Curling stone" still fits. Reply keeps the lesson's
    # hedge that a little friction remains.
    "what-forces-do-to-motion": dict(
        title="A stone on smooth ice.",
        scene="A curling stone is let go and slides down twenty metres of "
              "smooth ice.",
        question="If you had to guess, does the stone need something pushing "
                 "it forwards to keep going?",
        options=[
            ("No, it keeps going alone",
             "Moving does not need a push. Smooth ice holds the stone back so "
             "little that it carries on at nearly the same speed."),
            ("Yes, something must push it",
             "Most things we slide do stop, which makes it look that way. What"
             " stops them is something rubbing against them, not a missing "
             "push. On smooth ice there is hardly any."),
        ],
        answer=0,
        bridge="A force is only needed to change what something is doing: "
               "speed it up, slow it down or turn it. Next: a trolley that is "
               "already moving, and four different forces to try on it.",
        big_question="Forces and motion seem to go together. So what does a "
                     "force actually do to something that is moving?",
    ),

    # friction — title kept (rail label "The stuck crate"). Old scene said the
    # crate takes "a much gentler push" once moving and the big question named
    # the first centimetre as hardest; both changed (scene trimmed, big question
    # neutral). Angle changed from the draft's "where is the grip strongest" to
    # the hook's own misconception FORCE-28 (starting and keeping it sliding need
    # the same push), which is more everyday for Year 7.
    "friction": dict(
        scene="You lean on a full crate and push harder and harder. Nothing. "
              "Then it gives, and the crate starts to slide.",
        question="If you had to guess, once the crate is sliding, is keeping "
                 "it going easier than starting it, or just as hard?",
        options=[
            ("A little easier",
             "The floor grips the crate hardest just before it moves. Once it "
             "is sliding, the two surfaces never get the chance to settle into"
             " each other, so the grip drops."),
            ("Just as hard",
             "Nothing about the crate has changed. But the grip is at its "
             "biggest just before the crate moves, and it drops a little once "
             "it is sliding."),
        ],
        answer=0,
        bridge="That grip is called friction, and it always acts against the "
               "sliding. Next: drag a block across four surfaces and take two "
               "readings every time.",
        big_question="Push a heavy crate across a floor and something resists "
                     "you. What is it, and what decides how big it is?",
    ),

    # air-and-water-resistance — old title, scene and big question all said the
    # speed stops rising. Guess is the old hook's question cut to two: does the
    # skydiver keep getting faster, or stop? Tempting wrong option is "keeps
    # getting faster" (gravity never stops pulling). Rail label "The skydiver"
    # still fits. Correct reply reworded so the bridge no longer repeats it.
    "air-and-water-resistance": dict(
        title="Jumping out of an aircraft.",
        scene="A skydiver steps out of an aircraft high up and falls for a "
              "full minute with the parachute still shut.",
        question="If you had to guess, what happens to the skydiver's speed "
                 "over the minute?",
        options=[
            ("Stops getting faster",
             "After about ten seconds the speed levels off at around 55 metres"
             " per second, even with nothing underneath them. The air pushes "
             "back harder the faster they fall."),
            ("Keeps getting faster",
             "Gravity does keep pulling the whole way down, so it seems the "
             "speed should keep climbing. But the air pushes back harder the "
             "faster you go, and the speed levels off."),
        ],
        answer=0,
        bridge="Once the air's push has grown to match the weight, nothing is "
               "left over and the speed stops changing. Next: watch the two "
               "arrows close the gap.",
        big_question="Gravity pulls a skydiver down the whole way. So what "
                     "decides how fast they fall?",
    ),

    # moments — the rail label is "The door and the hinge" and ladder rung 2
    # feedback says "that is the door-hinge test at the top of this lesson", so
    # the hook must stay the door (the draft's plank broke both). Old title kept.
    # Old scene ("it opens easily") and big question gave the result, so the
    # scene now only sets up the test and the big question is neutral. Guess is
    # qualitative (does it open just as easily?), and no reply or bridge says how
    # the turning effect scales with distance, so the spanner gate (0.10 m to
    # 0.20 m: doubles?) is not pre-answered.
    "moments": dict(
        scene="Try it on the next door you go through. Push at the handle with"
              " one finger, and the door swings open. Then shut it and push "
              "just as hard with the same finger, a hand's width from the "
              "hinge.",
        question="If you had to guess, does the door swing open just as easily"
                 " this time?",
        options=[
            ("Yes, just as easily",
             "It is the same finger and the same push. But this close to the "
             "hinge the door hardly moves. Where you push matters, not just "
             "how hard."),
            ("No, it hardly moves",
             "The push is just as hard, but this close to the hinge it barely "
             "turns the door. Where you push matters as well as how hard."),
        ],
        answer=1,
        bridge="The hinge is the pivot, the point the door turns about. The "
               "turning effect of a push is called its moment. Next: a spanner"
               " and a tight nut.",
        big_question="A push can turn things as well as move them. What "
                     "decides how much turning a push gives?",
    ),

    # springs-and-hookes-law — old title/scene ("the pattern looks obvious") and
    # big question ("right up until it does not") hinted the answer. Guess keeps
    # the old 10 N prediction (rail label "Predict 10 N") as yes/no on whether
    # the pattern holds. Bridge no longer says "only more readings can show where
    # it stops", which pre-answered the bench gate (which readings to take).
    # FLAG: "No" is right for THIS spring (the lesson's model: limit of
    # proportionality at 6 N, bench runs to 10 N) and for a small lab spring
    # stretched to 200 mm, but a very stiff spring could survive 10 N; the scene
    # names a small school-lab spring and the reply ties the claim to it.
    "springs-and-hookes-law": dict(
        title="A spring and a ruler.",
        scene="A small spring from a school lab hangs beside a ruler. Hang 1 N"
              " on it and it stretches 20 mm. Hang 2 N and it stretches 40 mm.",
        question="If you had to guess, will this spring keep adding 20 mm for "
                 "every extra newton, all the way to 10 N?",
        options=[
            ("Yes, all the way",
             "The first two readings do make it look that way. But a small "
             "spring cannot keep it up for ever: somewhere before 10 N, each "
             "newton starts adding more than the last."),
            ("No, the pattern stops",
             "For the first few newtons the pattern holds exactly. But every "
             "spring has a load where it stops, and a small lab spring reaches"
             " it before 10 N."),
        ],
        answer=1,
        bridge="The load where the pattern stops is called the limit of "
               "proportionality. Next: load the spring yourself and find where"
               " it is.",
        big_question="A spring turns a force into a length you can read with a"
                     " ruler. How does the stretch depend on the load?",
    ),

    # non-contact-forces — the rail label is "Balloon and hair" and the sorter
    # has a balloon-and-hair case, so the hook keeps the balloon (the draft's
    # magnet in a jar broke the rail). Old title and scene ("a clear centimetre
    # of air in between") and the big question ("Three of them do not") gave the
    # answer; all rewritten. Guess: does the balloon have to touch the hair?
    # Tempting wrong option is yes (FORCE-44).
    "non-contact-forces": dict(
        title="A balloon and someone's hair.",
        scene="Rub a balloon on a jumper, then bring it slowly up to someone's"
              " head. Their hair stands up towards the balloon.",
        question="If you had to guess, does the balloon have to touch the hair"
                 " to make it move?",
        options=[
            ("Yes, it has to touch",
             "Most pushes and pulls you know come from touching. But the hair "
             "lifts while there is still a clear centimetre of air between "
             "them."),
            ("No, it works across a gap",
             "The hair lifts while there is still a clear centimetre of air in"
             " between. The balloon pulls on it across the gap, with nothing "
             "touching."),
        ],
        answer=1,
        bridge="Rubbing moved electric charge on to the balloon, and charge "
               "can pull across a gap. Next: eight situations to sort by "
               "whether the two things need to touch.",
        big_question="Think of the pushes and pulls you have met so far. What "
                     "does it take for one object to act on another?",
    ),


    # ── Year 7 · P11 Matter and the particle model ───────────────────────────────

    # density — the rail label is "Which is heavier", so the guess stays on the
    # old hook's question rather than the draft's "which takes up more space".
    # Old scene ("The beam is dead level") gave the answer, so the scene now
    # stops before the beam is let go. Tempting wrong option is the iron
    # (PART-14). The old big question (lead and feathers weigh the same) pointed
    # straight at the answer, so it is replaced.
    "density": dict(
        title="A lump of iron and a block of oak.",
        scene="On a pan balance: a small lump of iron on the left, and on the "
              "right a block of oak about twelve times its size. You let go of"
              " the beam.",
        question="If you had to guess, which is heavier?",
        options=[
            ("The lump of iron",
             "Iron does feel heavy. But the beam stays level: about twelve "
             "times as much oak has the same mass as the lump of iron."),
            ("Neither: they balance",
             "The beam stays level, so they weigh the same. It takes about "
             "twelve times as much oak to match one lump of iron."),
        ],
        answer=1,
        bridge="Heavy is about a particular object. How much mass is packed "
               "into each bit of a material is its density. Next: six "
               "materials on one balance.",
        big_question="Some things feel heavy for their size and others feel "
                     "light. What is the real difference between them?",
    ),

    # brownian-motion — the rail label "Specks that will not settle" is fixed
    # lesson text and answers the draft's "will they settle?" guess on load.
    # Angle changed back to the old hook's question cut to two: draughts
    # (PART-19, elicited_by s-hook) or unseen bits of air hitting them. Old title
    # and scene kept (they state only that the specks never settle). Old big
    # question ("nothing touching them", "atoms") pointed at the answer, so it is
    # replaced.
    "brownian-motion": dict(
        question="If you had to guess, what is moving the specks about?",
        options=[
            ("Unseen bits of air hitting them",
             "The air is made of particles far too small to see, and billions "
             "of them strike each speck every second. The strikes almost "
             "cancel, and the small leftover shoves the speck about."),
            ("Draughts of air blowing them",
             "Moving air does push smoke about. But the air in a sealed cell "
             "is still, and a draught would carry every speck the same way. "
             "Each one jerks off on its own."),
        ],
        answer=0,
        bridge="This jiggling is called Brownian motion. Next: choose what is "
               "under the microscope and how warm it is.",
        big_question="Smoke specks in still air jiggle for hours and never "
                     "settle. What does that tell us about the air?",
    ),

    # temperature-and-internal-energy — title kept (rail label "A spark and a
    # bath"). Old scene ("a faint tick", "properly hot") and big question
    # ("neither is about temperature alone") pointed at the bath; scene now gives
    # only the two temperatures and the big question is neutral. Guess is the old
    # hook's question. Correct reply now uses the lesson's own figure ("something
    # like a hundred million times", not "millions") and reads as a sentence
    # after "Good guess.".
    "temperature-and-internal-energy": dict(
        scene="A grinding wheel throws white-hot sparks at about 1000 °C. A "
              "full bath of water is at 40 °C.",
        question="If you had to guess, which one holds more energy?",
        options=[
            ("The spark",
             "The spark is far hotter. But it is a tiny speck, and a bath is a"
             " huge amount of water. How much there is counts too."),
            ("The bath",
             "The bath holds something like a hundred million times more. The "
             "spark is far hotter, but there is almost nothing of it."),
        ],
        answer=1,
        bridge="Temperature says how much energy one particle has on average. "
               "How much energy an object holds depends on every particle in "
               "it. Next: four amounts of water, all on one thermometer.",
        big_question="How are the temperature of something and the energy it "
                     "holds related?",
    ),

    # why-ice-floats — title and scene kept (they state only that ice floats;
    # rail label "Ice cubes on top"). Old big question ("Solids sink in their own
    # melt... Iron does") gave away both the hook and the bench gate (molten
    # iron), so it is replaced. Guess: freezing makes it take more room (correct)
    # against "weigh less" (PART-20). Bridge no longer says other substances
    # shrink when they freeze, which pre-answered the bench gate (solid iron in
    # molten iron).
    "why-ice-floats": dict(
        question="If you had to guess, why does ice float on the water it came"
                 " from?",
        options=[
            ("Freezing makes it take more room",
             "Water gets about 9% bigger when it freezes, but it weighs the "
             "same. The same mass in more room makes ice less dense than "
             "water, so it floats."),
            ("Freezing makes it weigh less",
             "Ice does feel light, so that is easy to believe. But freezing "
             "does not change how much water there is. What changes is the "
             "room it takes up."),
        ],
        answer=0,
        bridge="Density decides what floats, and freezing changes it. Next: "
               "four substances, each weighed as a solid and as its own "
               "liquid.",
        big_question="A pond freezes from the top down, and fish live on "
                     "underneath. What makes that possible?",
    ),


    # ── Year 8 · B4 Breathing and gas exchange ──────────────────────────────────

    # the-gas-exchange-system — the rail label is "Mouth-to-mouth", so the hook
    # keeps mouth-to-mouth (the draft's bag broke it). Old title ("…works") and
    # scene ("it keeps them alive", "re-oxygenated") gave the answer and the big
    # question stated it outright; all three rewritten. Guess is the old hook's
    # question cut to two: most of the oxygen comes back out, against BREATH-01
    # ("breathe out carbon dioxide").
    "the-gas-exchange-system": dict(
        title="Mouth-to-mouth.",
        scene="Someone has stopped breathing. A first-aider gives "
              "mouth-to-mouth: they breathe their own breath out into the "
              "other person's lungs.",
        question="If you had to guess, how much of the oxygen in a breath is "
                 "still there when you breathe it out?",
        options=[
            ("Most of it",
             "You keep only about a quarter of the oxygen in each breath and "
             "pass the rest straight back out. That is why a first-aider's "
             "breath can help someone else."),
            ("Hardly any of it",
             "We are often told we breathe in oxygen and breathe out carbon "
             "dioxide. But most of the oxygen comes straight back out, which "
             "is why mouth-to-mouth works."),
        ],
        answer=0,
        bridge="Air in and air out are more alike than most people expect. "
               "Next: predict how each of four gases changes between a breath "
               "in and a breath out.",
        big_question="Every breath goes in and comes back out. What actually "
                     "changes in the air while it is inside you?",
    ),

    # how-breathing-works — injury hook kept as Design wrote it (no first-aid
    # wording). The draft's options ("air escaped from it / got in around it")
    # were not cleanly separable: the collapsed lung DOES empty through its
    # airway, so "air escaped from it" is arguably true. Angle changed to the
    # lesson's core idea (BREATH-04): does a lung stretch itself open, or does
    # the chest stretch it open? Scene keeps the word "collapsed" so "the
    # collapsed lung in the hook" (s-think) and rung 3 "Explain the collapsed
    # lung" still land; rail label "Collapsed lung" fits. Old big question ("no
    # muscle at all") gave the answer; replaced.
    "how-breathing-works": dict(
        title="A small wound between two ribs.",
        scene="A narrow wound goes through the chest wall between two ribs. "
              "The lung itself is not touched, and its airway is clear. Within"
              " seconds the lung on that side has collapsed, and it will not "
              "fill again.",
        question="If you had to guess, how does a healthy lung normally fill "
                 "with air?",
        options=[
            ("The chest stretches it open",
             "A lung has no muscle and cannot open itself. As the chest gets "
             "bigger, the lung is stretched open with it. Once air gets in "
             "around the lung, that stops working."),
            ("It stretches itself open",
             "It feels as if your lungs do the breathing. But a lung has no "
             "muscle at all. It fills only when the chest gets bigger and "
             "stretches it open."),
        ],
        answer=0,
        bridge="Making the chest bigger lowers the pressure inside it, and air"
               " flows in from outside. Next: work a model diaphragm and watch"
               " the order in which things change.",
        big_question="Air flows into your lungs with every breath. What makes "
                     "it go in?",
    ),

    # alveoli-built-for-exchange — big question kept (it describes the bench, not
    # the hook). Old title and scene used "alveoli" and "cavity"; reworded in
    # plain words, alveoli named in the bridge. The scene keeps "one smooth bag":
    # the rail label is "One smooth bag" and exercise-asthma-and-smoking rung 4
    # says the emphysema patient "has moved partway towards the smooth bag" from
    # this hook. Question reworded ("live on the bag" read oddly).
    "alveoli-built-for-exchange": dict(
        title="A sponge swapped for a bag.",
        scene="Your lungs are full of tiny air sacs, like a sponge. Imagine "
              "swapping the sponge for one smooth bag that holds exactly the "
              "same amount of air.",
        question="If you had to guess, could you stay alive with the bag "
                 "instead?",
        options=[
            ("Yes, just as well",
             "The air is all still there, so it seems fine. But oxygen can "
             "only cross into the blood through the surface, and a bag has far"
             " too little of it."),
            ("No, not for long",
             "A smooth bag has hardly any surface for oxygen to pass through, "
             "so you would last only minutes. What matters is surface, not the"
             " amount of air."),
        ],
        answer=1,
        bridge="Those tiny air sacs are called alveoli, and there are about "
               "500 million of them. Next: switch breathing and blood flow on "
               "and off, and count oxygen crossing the wall.",
    ),

    # exercise-asthma-and-smoking — tone-gated lesson: factual, no advice, no
    # dose, no warning added. Old title and scene said the air is fine and the
    # inhaler has no oxygen, which is the answer; rewritten. Title now names the
    # inhaler (rail label "The inhaler"). Bridge no longer restates the big
    # question (redundant). The reply naming the airways matches the bench's
    # asthma answer, as the old hook's own question did.
    "exercise-asthma-and-smoking": dict(
        title="The blue inhaler.",
        scene="Someone is having an asthma attack. They are struggling to get "
              "enough air, and a puff from a blue inhaler helps within "
              "minutes.",
        question="If you had to guess, does the puff from the inhaler contain "
                 "extra oxygen?",
        options=[
            ("Yes, extra oxygen",
             "Oxygen sounds like what is missing. But the air around them "
             "already has plenty. The puff relaxes muscle in the walls of the "
             "air tubes, so they widen."),
            ("No oxygen at all",
             "There is no oxygen in it. The air around them already has "
             "plenty; the medicine relaxes muscle in the walls of the air "
             "tubes, so they widen and air gets through."),
        ],
        answer=1,
        bridge="The air was never the problem: something stopped it reaching "
               "the lungs. Next: three cases, and which part of the breathing "
               "system each one hits.",
    ),

    # stomata-and-gas-exchange-in-plants — the bench's balanced verdict says
    # "This is the dawn reading from the hook", the rail label is "Flat line at
    # dawn" and the tutor card asks about "the flat line at dawn", so the hook
    # must stay the sealed jar at dawn (the draft's sunny windowsill broke all
    # three). Old title and scene kept: they describe the readings and do not say
    # what causes the flat line. Old big question ("the two run at once") gave
    # the answer; replaced. Guess: during the flat minutes, is the plant making
    # or using carbon dioxide? Tempting wrong option: a flat line means it is
    # doing neither.
    "stomata-and-gas-exchange-in-plants": dict(
        question="If you had to guess, during those steady minutes, is the "
                 "plant making or using any carbon dioxide at all?",
        options=[
            ("No, it is doing neither",
             "A flat line does look as if nothing is happening. But the plant "
             "is making carbon dioxide and using it up at exactly the same "
             "rate."),
            ("Yes, it is doing both",
             "It is respiring, which makes carbon dioxide, and "
             "photosynthesising, which uses it up. At that light level the two"
             " run at the same rate, so the reading stays flat."),
        ],
        answer=1,
        bridge="A sensor outside the plant only ever shows the difference "
               "between the two. Next: turn the light up and watch both "
               "processes.",
        big_question="A plant in a sealed jar changes the air around it, and "
                     "light changes how. What is going on inside the leaf?",
    ),


    # ── Year 8 · B5 Reproduction ────────────────────────────────────────────────

    # human-reproductive-systems — tone: clinical, third person, about organs.
    # Old title and scene gave both facts (all eggs present at birth; sperm made
    # continuously). Guess: are egg cells made all the time too? Tempting wrong
    # option is yes (REPRO-02). Figures checked against the lesson: "around a
    # million" immature egg cells at birth (hook, confrontation, job row 1),
    # "roughly four hundred" mature and released (job row 1, confrontation),
    # "fifteen hundred per second" (hook, job row 1). Rail label "A million eggs"
    # does not decide the guess. Wrong reply reworded ("cells that start a baby"
    # became "sex cells"). FLAG: Design's own NOTES flag 1 says sources give 1 to
    # 2 million at birth; "about a million" is kept because it is the lesson's
    # figure everywhere.
    "human-reproductive-systems": dict(
        title="Sperm cells every second.",
        scene="Sperm cells are made non-stop from puberty onwards, at "
              "something like fifteen hundred every second.",
        question="If you had to guess, are egg cells made all the time too?",
        options=[
            ("Yes, all the time",
             "Both are sex cells, so it is natural to expect them to match. "
             "But the immature egg cells are all in the ovaries at birth, and "
             "no new ones are made."),
            ("No, only before birth",
             "The ovaries of a newborn already hold every immature egg cell "
             "there will ever be, about a million, and no new ones are made. "
             "Only about four hundred are ever released."),
        ],
        answer=1,
        bridge="That is the first sign that the two systems are not mirror "
               "images. Next: match nine structures to the job each one does.",
        big_question="Two organ systems share one purpose. Learning the names "
                     "is the easy part; the useful question is what each "
                     "structure is for.",
    ),

    # gametes-and-fertilisation — old scene said both cells carry exactly 23
    # chromosomes, which ruled out the tempting option (REPRO-18, elicited_by
    # hook), and the big question said each brought half the instructions. The
    # draft's new scene ended "Each carries instructions for building a new
    # person", which is wrong (each carries half) and hinted at the answer;
    # dropped, and "genetic instructions" moved into the options. Rail label
    # "Unequal sizes" fits.
    "gametes-and-fertilisation": dict(
        title="A big cell and a tiny one.",
        scene="An egg cell is about 0.1 mm across, big enough to just see "
              "without a microscope. A sperm cell's head is about a twentieth "
              "as wide.",
        question="If you had to guess, is most of the egg's extra size more "
                 "genetic instructions, or food and supplies?",
        options=[
            ("Food and supplies",
             "The egg is packed with food and the machinery to build a body, "
             "which the new cell needs for its first days. Both cells bring "
             "the same instructions: 23 chromosomes each."),
            ("More genetic instructions",
             "A bigger cell might well carry more instructions. But both cells"
             " bring exactly 23 chromosomes, half a set each, so the extra "
             "size is something else: supplies."),
        ],
        answer=0,
        bridge="Each cell is built for its own job. Next: open six features of"
               " the two cells and find the reason behind each one.",
        big_question="A sperm cell and an egg cell fuse to make one new cell. "
                     "What does each one bring?",
    ),

    # the-menstrual-cycle — guess: in a longer cycle, is the extra time before or
    # after release (the lesson's fixed fortnight after release). Old title gave
    # the answer, so title and scene rewritten; the new scene mentions day 14 so
    # the hook's rail label "Not day 14" still refers to something. Third person
    # kept.
    "the-menstrual-cycle": dict(
        title="Not every cycle is 28 days.",
        scene="A cycle is counted from the first day of a period. Part-way "
              "through, an egg is released from an ovary, and the next period "
              "starts the cycle again. People often say the egg comes out on "
              "day 14, but ordinary cycles run anywhere from about 21 days to "
              "about 35.",
        question="If you had to guess, in a longer cycle, do the extra days "
                 "come before the egg is released, or after?",
        options=[
            ("Before the egg is released",
             "The time from release to the next period stays close to a "
             "fortnight in almost everyone. So the extra days come before "
             "release, while the egg is still maturing."),
            ("After the egg is released",
             "It is natural to think the end of the cycle stretches. But the "
             "fortnight after release stays about the same in almost everyone,"
             " so the extra days come before it."),
        ],
        answer=0,
        bridge="That is why the release day is not the same number for "
               "everyone. Next: a dial to walk through cycles of 21, 28 and 35"
               " days.",
    ),

    # gestation-placenta-and-birth — guess: does oxygen seep across by itself or
    # get pumped across (the old hook's own question, cut to two). Rail label
    # "Never mix" is visible on load, so a "do the bloods mix?" guess would be
    # given away; the old title, scene and big question are kept and none of them
    # gives away diffusion.
    "gestation-placenta-and-birth": dict(
        question="If you had to guess, does oxygen seep from one blood supply "
                 "to the other by itself, or is it pumped across?",
        options=[
            ("It seeps across by itself",
             "The two blood supplies are brought very close together, and "
             "oxygen moves from where there is more of it to where there is "
             "less. Nothing has to push it."),
            ("Something pumps it across",
             "A heart is the obvious pump. But a heart only moves blood "
             "around. Oxygen crosses the thin gap by itself, from where there "
             "is more of it to less."),
        ],
        answer=0,
        bridge="That is diffusion, the same process as in the lungs and the "
               "small intestine. Next: six substances, and which way each one "
               "crosses.",
    ),

    # lifestyle-and-the-developing-foetus — guess: how soon alcohol reaches the
    # baby (the lesson's "within minutes"). Rail label "Not a filter" is visible
    # on load, so a "does it get through?" guess would be given away; the old
    # title, scene and big question are kept so the label still refers to the
    # hook.
    "lifestyle-and-the-developing-foetus": dict(
        question="If you had to guess, once alcohol is in a mother's blood, "
                 "how soon does it reach the baby?",
        options=[
            ("Within a few minutes",
             "Alcohol is a small molecule that dissolves in blood, so it "
             "crosses the placenta as easily as oxygen does. Within minutes "
             "the baby's blood holds nearly as much as the mother's."),
            ("After several hours",
             "Hours sounds right for something to travel from one body to "
             "another. But the two blood supplies are a fraction of a "
             "millimetre apart, and within minutes the baby's level is close "
             "to the mother's."),
        ],
        answer=0,
        bridge="So the real questions are what else gets through, and what it "
               "does when it arrives. Next: six substances, and whether each "
               "one reaches the foetus.",
    ),

    # flowers-and-pollination — guess: which puts more pollen into the air, grass
    # or a rose (the old hay-fever hook). Title and scene unchanged.
    "flowers-and-pollination": dict(
        question="If you had to guess, which puts far more pollen into the "
                 "air: grass or a rose?",
        options=[
            ("Grass",
             "Grass lets the wind carry its pollen, so it makes huge amounts "
             "and most of it is wasted. That is why grass pollen is the one "
             "that gets into noses."),
            ("A rose",
             "Roses are the flowers people notice. But a rose hands its pollen"
             " to a bee, so it makes far less and very little of it is ever "
             "loose in the air."),
        ],
        answer=0,
        bridge="A plant cannot walk its pollen anywhere, so how it gets moved "
               "shapes the whole flower. Next: nine parts of a flower and the "
               "job of each.",
    ),

    # fertilisation-seeds-and-fruit — guess: does the pollen grow its way down or
    # get carried down. Old title ("growing a tunnel") gave the answer, so title
    # and scene rewritten; both replies say "tunnel" so the rail label "A tunnel"
    # still lands.
    "fertilisation-seeds-and-fruit": dict(
        title="Pollen on the sticky tip.",
        scene="A pollen grain lands on the sticky tip of a stalk in the middle"
              " of a flower. The part it has to reach is a few centimetres "
              "below, deep inside the flower. The grain has no legs, wings or "
              "tail.",
        question="If you had to guess, does the pollen grow its way down the "
                 "stalk, or does something carry it down?",
        options=[
            ("It grows its way down",
             "The grain puts out a thin tube that grows down through the stalk"
             " like a tunnel, and the male nucleus travels along inside it."),
            ("Something carries it down",
             "An insect or the wind carried the pollen to the flower. But once"
             " it lands, the grain does the work itself: it grows a tunnel "
             "down through the stalk."),
        ],
        answer=0,
        bridge="Landing is not the same as joining. Next: what each part of "
               "the flower turns into once fertilisation has happened.",
    ),

    # seed-dispersal — guess: does a seed under its parent do well or badly. Old
    # scene ("must be costing them something") and big question ("the worst
    # place...") gave it away, so both rewritten; title kept.
    "seed-dispersal": dict(
        scene="A plant that has just spent a season building a fruit then "
              "spends even more on getting its seeds away.",
        question="If you had to guess, would a seed that lands right under its"
                 " parent plant do well, or badly?",
        options=[
            ("Do well",
             "The parent grew well there, so the spot looks like a good one. "
             "But that is the problem: the big plant has already taken the "
             "light, water and minerals."),
            ("Do badly",
             "Under the parent it has to compete for light, water and minerals"
             " with a much bigger plant that got there first, and it usually "
             "loses."),
        ],
        answer=1,
        bridge="That is the problem every dispersal structure is solving. "
               "Next: eight fruits and seeds to sort by how they travel.",
        big_question="Plants spend a lot on getting rid of their own seeds. "
                     "Why does it pay?",
    ),


    # ── Year 8 · B7 Photosynthesis ──────────────────────────────────────────────

    # the-photosynthesis-reaction — guess: did van Helmont's soil end up a lot
    # lighter or almost the same (PLANT-01). Old title stated the soil loss and
    # the big question ("a tree is mostly made of air") gave it away, so title,
    # scene and big question rewritten; the willow stays for the rail label "The
    # willow".
    "the-photosynthesis-reaction": dict(
        title="A willow in a pot for five years.",
        scene="In the 1640s Jan van Helmont planted a 2.3 kg willow shoot in "
              "90 kg of dried soil in a pot. He gave it nothing but water for "
              "five years, and the shoot grew into a small tree. Then he "
              "weighed the tree and the soil again.",
        question="If you had to guess, did the soil in the pot end up a lot "
                 "lighter, or almost the same?",
        options=[
            ("A lot lighter",
             "Plants grow in soil. But the soil lost only about 57 grams while"
             " the tree gained about 74 kilograms."),
            ("Almost the same",
             "The soil lost only about 57 grams, while the willow gained about"
             " 74 kilograms. The tree is not made of soil."),
        ],
        answer=1,
        bridge="So the new wood came from somewhere else. Next: take away "
               "light, carbon dioxide, water or chlorophyll, one at a time, "
               "and see what a leaf makes.",
        big_question="A tree grows from a small shoot into tonnes of wood. "
                     "What is it built from, and what does it need to build "
                     "it?",
    ),

    # leaves-built-for-the-job — guess: are most of a leaf's holes on top or
    # underneath. Rail label "Every hole leaks" names the old hook and gives away
    # any "is a change free?" guess, so the old title, scene and big question are
    # kept and the angle moved to where the holes sit (the lesson's stomata-on-
    # the-shaded-underside fact).
    "leaves-built-for-the-job": dict(
        question="If you had to guess, are most of a leaf's holes on its top "
                 "surface, or on its underside?",
        options=[
            ("On the top surface",
             "The top faces the sun and the open air, so it looks like the "
             "natural place. But a hole there would lose water fastest. Most "
             "are on the shaded underside."),
            ("On the underside",
             "The underside is shaded and cooler, so less water evaporates out"
             " of each hole. Carbon dioxide still gets in from below."),
        ],
        answer=1,
        bridge="Even where a hole goes is a deal between letting gas in and "
               "keeping water. Next: build a leaf with four dials and try to "
               "win on both readouts.",
    ),

    # testing-a-leaf-for-starch — guess: is the leaf boiled in alcohol to remove
    # its green or to wash it clean. Old title and scene gave the answer (green
    # hides the change), so rewritten; the new title keeps "straight onto" for
    # the rail label "Straight on".
    "testing-a-leaf-for-starch": dict(
        title="Not straight onto the leaf.",
        scene="Iodine solution is used to test a leaf for starch, but it never"
              " goes straight onto a fresh leaf. Before the iodine goes on, "
              "the leaf is boiled in ethanol, a kind of alcohol.",
        question="If you had to guess, is the leaf boiled in alcohol to remove"
                 " its green, or to wash it clean?",
        options=[
            ("To remove its green",
             "The alcohol dissolves the green chlorophyll out, so the leaf "
             "goes pale and a colour change can be seen."),
            ("To wash it clean",
             "Alcohol does clean things. But nothing in this test depends on "
             "the leaf being germ-free. The problem is its green colour, which"
             " hides any change."),
        ],
        answer=0,
        bridge="A pale leaf, then iodine: blue-black means starch. Next: a "
               "bench where you can leave steps out and see what goes wrong.",
    ),

    # why-almost-all-life-depends-on-it — guess: does a mushroom live on food a
    # plant made, or make its own. Old title ("every meal was once a leaf") gave
    # the rule away, so title and scene rewritten; the new title keeps "every
    # meal" for the rail label "Every meal". Big question kept.
    "why-almost-all-life-depends-on-it": dict(
        title="Every meal you eat started somewhere.",
        scene="A steak is a cow, and the cow ate grass. Bread is made from "
              "wheat. A mushroom is harder: it is not green, has no leaves, "
              "and grows on compost or rotting wood, often where no sunlight "
              "reaches.",
        question="If you had to guess, does a mushroom live on food that a "
                 "plant made, or on food it makes itself?",
        options=[
            ("Food a plant made",
             "A mushroom's threads feed on dead plant material, so its food "
             "was built by a plant, maybe years ago."),
            ("Food it makes itself",
             "It grows without anyone feeding it, so it can look self-made. "
             "But a mushroom has no chlorophyll and cannot make food from "
             "light. It digests what a plant built earlier."),
        ],
        answer=0,
        bridge="Follow almost any food back far enough and you reach something"
               " that makes food from light. Next: pick a food and trace it "
               "back, step by step.",
    ),


    # ── Year 8 · B8 Respiration ─────────────────────────────────────────────────

    # aerobic-respiration — guess: does most lost fat leave through the lungs or
    # in sweat and urine (the old hook, cut to two; rung 2 asks the same, which
    # the old hook already did). Title kept for the rail label "Ten kilograms".
    # Big question ("leaves through your mouth") gave it away, so replaced; scene
    # shortened.
    "aerobic-respiration": dict(
        scene="Ten kilograms of fat leave a person's body over a year. Almost "
              "nobody, including most adults, can say how.",
        question="If you had to guess, does most of that fat leave through the"
                 " lungs, or in sweat and urine?",
        options=[
            ("Out through the lungs",
             "The carbon in fat joins with oxygen and leaves as carbon dioxide"
             " in your breath. Most of the fat you lose is breathed out."),
            ("In sweat and urine",
             "Those are the exits people usually think of, and some water does"
             " leave that way. But most of the fat's mass is carbon, and that "
             "leaves as a gas from the lungs."),
        ],
        answer=0,
        bridge="Nothing vanishes: the atoms in the fat end up somewhere else. "
               "Next: weigh everything that goes in and everything that comes "
               "out.",
        big_question="The reaction that keeps you alive runs in nearly every "
                     "cell, all the time, at body temperature and without a "
                     "flame. What goes in, and what comes out?",
    ),

    # why-every-cell-respires — guess: does the body keep a big spare supply of
    # oxygen, or hardly any (the old hook's "no store" answer). Title, scene and
    # big question unchanged.
    "why-every-cell-respires": dict(
        question="If you had to guess, does the body keep a big spare supply "
                 "of oxygen, or hardly any?",
        options=[
            ("A big spare supply",
             "Lungs full of air do feel like a store. But the body only holds "
             "a few minutes' worth of oxygen, and every cell is using it all "
             "the time."),
            ("Hardly any",
             "There is no oxygen tank in the body, only what the blood is "
             "carrying right now. Fat is a fuel store that lasts weeks, but "
             "oxygen has no store at all."),
        ],
        answer=1,
        bridge="Every cell in your body is using oxygen to release energy, "
               "every second. Next: five cells, and what each one spends its "
               "energy on.",
    ),

    # anaerobic-respiration-in-humans — guess: during a sprint do the muscles
    # stop using oxygen, or keep using it too (RESP-06, which the register says
    # the hook elicits). Angle changed because the H1 "Anaerobic respiration in
    # humans" gives away any "without oxygen" answer. Title, scene and big
    # question unchanged.
    "anaerobic-respiration-in-humans": dict(
        question="If you had to guess, during the sprint, do the muscles stop "
                 "using oxygen, or keep using it too?",
        options=[
            ("They stop using oxygen",
             "Switching over is how it is often described. But nothing "
             "switches: the muscles use all the oxygen that arrives, and break"
             " down extra glucose without oxygen to cover the shortfall."),
            ("They keep using it too",
             "Respiration with oxygen carries on as fast as the supply allows."
             " The shortfall is covered by breaking glucose down without "
             "oxygen, which is quick but leaves lactic acid behind."),
        ],
        answer=1,
        bridge="So the muscles are running two kinds of respiration at once. "
               "Next: run, stop, and watch what your breathing does.",
    ),

    # fermentation — guess: did the holes come from the yeast cells swelling, or
    # from a gas the yeast gave off (old options A and B). Old scene said each
    # hole is "a pocket of gas", so scene rewritten; title kept for the rail
    # label "The holes".
    "fermentation": dict(
        scene="Bread dough is flour, water and a little yeast. It goes into "
              "the oven as a flat lump and comes out twice the size, full of "
              "holes. Nothing was pumped into it.",
        question="If you had to guess, what made the holes: the yeast cells "
                 "swelling up, or a gas the yeast gave off?",
        options=[
            ("The yeast cells swelling up",
             "Yeast does grow in dough. But each cell is far too small to see."
             " The holes are bubbles of carbon dioxide that the yeast gives "
             "off."),
            ("A gas the yeast gave off",
             "Yeast is a living fungus. Short of oxygen in the dough, it "
             "respires and gives off carbon dioxide, which blows bubbles all "
             "through the dough."),
        ],
        answer=1,
        bridge="Bread is risen by a waste gas. Next: a vessel with four dials,"
               " to see what yeast and yoghurt bacteria make under different "
               "conditions.",
    ),

    # aerobic-vs-anaerobic — guess: which route gets energy to a cell faster,
    # with oxygen or without. Old title kept (it says one route gets twenty times
    # more but not which), so the rail label "Twenty times" still refers to it;
    # scene rewritten to name the two routes; big question said which is more and
    # which is faster, so replaced.
    "aerobic-vs-anaerobic": dict(
        scene="Cells have two ways to get energy out of glucose, a sugar: one "
              "uses oxygen and one does not. Every organism in this unit, from"
              " a sprinter to a yeast cell, keeps both available.",
        question="If you had to guess, which route gets energy to a cell "
                 "faster: the one using oxygen, or the one without?",
        options=[
            ("The one using oxygen",
             "It is the better deal, so it feels as if it should win on speed "
             "too. But it has to wait for oxygen to be delivered, so it is the"
             " slower route."),
            ("The one without oxygen",
             "With fewer steps and no oxygen to wait for, energy comes "
             "quicker. The price is much less energy from each glucose."),
        ],
        answer=1,
        bridge="So the two routes win different races. Next: five situations, "
               "and which route is running in each.",
        big_question="Two ways to get energy out of the same sugar molecule, "
                     "and almost everything alive uses both. Which one is "
                     "running, and when?",
    ),


    # ── Year 8 · C4 Chemical reactions ──────────────────────────────────────────

    # chemical-vs-physical-change — guess: what makes frying an egg a chemical
    # change, the colour change or something new being made. The draft's "can it
    # be undone?" foil pre-answered the later "Undo it" commit (s-think), so the
    # foil is now colour. Old scene said "you no longer have egg white", so scene
    # rewritten; title kept for the rail label "Chocolate and egg".
    "chemical-vs-physical-change": dict(
        scene="Both changes were caused by heat. Melting chocolate is a "
              "physical change. Frying an egg is a chemical change.",
        question="If you had to guess, what makes frying an egg a chemical "
                 "change: the change of colour, or that something new is made?",
        options=[
            ("The change of colour",
             "A colour change is often a clue. But food colouring stirred into"
             " water changes colour and makes nothing new. What decides it is "
             "that the egg is now a different substance."),
            ("Something new is made",
             "A chemical change makes at least one new substance. The fried "
             "egg is firm and white where the raw egg white was runny and "
             "clear."),
        ],
        answer=1,
        bridge="So the test is what you end up with, not how it looks along "
               "the way. Next: three pairs of changes that look alike.",
    ),

    # reactions-rearrange-atoms — guess: would hydrogen and oxygen mixed in one
    # balloon turn into water on their own (the lesson's own stretch: the joins
    # must be broken first). Angle changed because the H1 "Reactions rearrange
    # atoms" gives away "where did the water come from?". Title, scene and big
    # question unchanged.
    "reactions-rearrange-atoms": dict(
        question="If you had to guess, would the two gases, mixed in one "
                 "balloon and left alone, turn into water on their own?",
        options=[
            ("Yes, on their own",
             "Mixing sounds like enough for a reaction. But the atoms in each "
             "gas are joined in pairs, and those joins must be broken first. "
             "Without a flame or spark, the mixture just sits there."),
            ("No, they need starting",
             "A mix of hydrogen and oxygen can sit in a balloon for a very "
             "long time. A flame or spark is needed to break the first joins "
             "between its atoms."),
        ],
        answer=1,
        bridge="Once started, the atoms that were in the balloons join up in a"
               " new way, as water. Next: take three reactions apart and count"
               " the atoms.",
    ),

    # word-equations — guess: what a chemist needs added, how long it burned or
    # what the powder is (old options C and B; the temperature foil was dropped
    # because "heat is only a condition" pre-answers the builder's Heat
    # distractor). Old title gave the answer, so rewritten; the quoted sentence
    # is kept so the rail label "Twenty-two words" still points at it. Big
    # question gave the point away, so replaced.
    "word-equations": dict(
        title="Magnesium in a flame.",
        scene="“I held the magnesium ribbon in the flame with tongs and it "
              "burned with a really bright white light and left a white powder"
              " behind.” Every word is true.",
        question="If you had to guess, what would tell a chemist which "
                 "reaction happened: how long it burned, or what the powder "
                 "is?",
        options=[
            ("How long it burned",
             "Timings matter in lots of experiments. But how long it burned "
             "says nothing about what reacted. A chemist needs the name of the"
             " powder, and what the magnesium joined with."),
            ("What the powder is",
             "The powder is a new substance, magnesium oxide, made when the "
             "magnesium joins with oxygen from the air. The sentence never "
             "names either one."),
        ],
        answer=1,
        bridge="A word equation names every reactant and every product in one "
               "line. Next: build three of them from what happened.",
        big_question="How do chemists write down a reaction so that nothing "
                     "important is left out?",
    ),

    # mass-in-a-reaction — guess: is a candle's wax destroyed or does it float
    # off as gases (the candle half of the old hook). Title, scene and big
    # question kept; the bridge leaves the steel wool open rather than handing
    # over the balance-bench rule.
    "mass-in-a-reaction": dict(
        question="If you had to guess, is most of a burning candle's wax "
                 "destroyed in the flame, or does it float off as gases?",
        options=[
            ("Destroyed in the flame",
             "A candle really does seem to vanish. But atoms are never "
             "destroyed: the wax joins with oxygen and becomes invisible gases"
             " that float away."),
            ("Floats off as gases",
             "The wax joins with oxygen and becomes carbon dioxide and water "
             "vapour, which drift away into the air. Nothing is lost."),
        ],
        answer=1,
        bridge="So why does the steel wool get heavier instead? Next: two "
               "reactions on a balance, each in an open flask and a sealed "
               "one.",
    ),

    # symbol-equations-and-balancing — guess: fix it by changing H2O itself or by
    # changing how many react (the old hook, cut to two). Title and scene
    # unchanged (scene keeps its <sub> markup). Big question ("the one number you
    # are allowed to change") replaced. Replies avoid naming hydrogen peroxide
    # and the 2:1:2 answer so the forbidden-move bench and the first balancing
    # tab keep their own reveals.
    "symbol-equations-and-balancing": dict(
        question="If you had to guess, how do you fix it: change H2O itself, "
                 "or change how many of each particle react?",
        options=[
            ("Change H2O itself",
             "Adding an oxygen to H2O does make the counts match. But then the"
             " substance is no longer water, and this reaction makes water."),
            ("Change how many react",
             "You change how many particles take part, using numbers in front."
             " The formula stays as it is, so water stays water."),
        ],
        answer=1,
        bridge="Next: balance four equations yourself, changing only the "
               "numbers in front, and watch the counters.",
        big_question="Written straight out, the equation for making water "
                     "seems to destroy an oxygen atom. How do you fix it?",
    ),


    # ── Year 8 · C5 Types of reaction ───────────────────────────────────────────

    # combustion — guess is the old hook question (gas or air) in plain words;
    # the scene said "Same gas, same tap", which rules out gas, so that sentence
    # is replaced. Reviewer: wrong reply no longer opens "Fair," after the page's
    # own "Fair guess."
    "combustion": dict(
        scene="Same burner, same room. The only thing that changed was a metal"
              " collar at the bottom of the burner. Hold a beaker over the "
              "yellow flame and it comes away black; hold it over the blue one"
              " and it stays clean.",
        question="If you had to guess, what does the hole in the collar let "
                 "into the burner: more gas, or more air?",
        options=[
            ("More gas",
             "Gas is what burns, so that makes sense. But the gas comes in at "
             "the bottom through the tap, and that stayed the same. The collar"
             " opens a hole for air."),
            ("More air",
             "The hole lets air into the burner. Air carries the oxygen the "
             "gas needs to burn properly, and with the hole shut there is too "
             "little of it."),
        ],
        answer=1,
        bridge="Burning needs oxygen, and how much arrives changes what the "
               "flame makes. Next: what combustion is, then a burner where you"
               " open and shut the hole yourself.",
    ),

    # thermal-decomposition — reviewer changed the angle to mass (heavier or
    # lighter after heating). The draft's "air joined in, or the heat alone broke
    # it up?" was given away by the H1 "Thermal decomposition" (heat + breaking
    # up) and the hook's rail label "One in, two out". Title, scene and big
    # question rewritten so none says "one in, two out", "nothing added" or
    # "lighter".
    "thermal-decomposition": dict(
        title="A green powder in a hot tube.",
        scene="A green powder is heated in a test tube. It turns black, and a "
              "gas comes off that turns limewater cloudy.",
        question="If you had to guess, once the heating is over, does what is "
                 "left in the tube weigh more than before, or less?",
        options=[
            ("More than before",
             "When a metal burns it does get heavier, because oxygen from the "
             "air joins it. Here nothing joins in: part of the powder leaves "
             "as a gas, so the tube gets lighter."),
            ("Less than before",
             "Part of the powder left the tube as that gas. The black solid "
             "that stays behind weighs less than the green powder did."),
        ],
        answer=1,
        bridge="The green powder has split into two new substances, and one of"
               " them escaped. Next: what this kind of reaction is called, "
               "then three powders to heat.",
        big_question="A green powder is heated and turns black. What kind of "
                     "reaction is this, and how is it different from burning?",
    ),

    # oxidation — everyday weighing guess (heavier or lighter after burning); the
    # old scene said "both end up heavier", so it is rewritten.
    "oxidation": dict(
        title="Magnesium burns in two seconds. A gate rusts over twenty years.",
        scene="One is a flash of white light and a puff of white powder. The "
              "other is so slow that nobody has ever watched it happen. Both "
              "start as shiny metal and end as a crumbly powder or crust.",
        question="If you had to guess, would all the powder left from burning "
                 "magnesium weigh more than the metal did, or less?",
        options=[
            ("More",
             "The magnesium joins with oxygen from the air, so the powder is "
             "the metal plus the oxygen it picked up."),
            ("Less",
             "Burning wood does leave less, because gases escape. But "
             "magnesium takes oxygen in and keeps it, so the powder weighs "
             "more than the metal did."),
        ],
        answer=0,
        bridge="Rusting does the same thing slowly. Next: what oxidation is, "
               "then four tubes that show what rusting needs.",
    ),

    # displacement — reviewer changed the angle to the colour of the liquid
    # (stays blue, or fades). The draft reused the old hook's "where did the
    # copper come from?", which is word for word the later THINK (rail: "Where
    # the copper came from") and is hinted by the H1 "Displacement". Title and
    # scene rewritten to show only the start and the nail's coat; the old big
    # question ("swapped places") is replaced.
    "displacement": dict(
        title="A grey nail goes into a blue liquid.",
        scene="An iron nail is left in a beaker of blue copper sulfate "
              "solution. Nothing is heated and nothing is added. After a while"
              " the nail is covered in a furry orange-brown layer.",
        question="If you had to guess, what happens to the blue colour of the "
                 "liquid: does it stay just as blue, or fade?",
        options=[
            ("It stays blue",
             "It is the nail you can see changing, so that makes sense. But "
             "the liquid changes too: the blue fades, and a pale green takes "
             "its place."),
            ("It fades",
             "The blue fades, and a pale green takes its place. So the liquid "
             "has changed, not just the nail."),
        ],
        answer=1,
        bridge="Something has left the blue liquid, and something new has gone"
               " into it. Next: what this kind of swap is called, and the rule"
               " for which metal wins.",
        big_question="An iron nail left in a blue solution comes out coated in"
                     " copper. What has happened, and would it work the other "
                     "way round?",
    ),

    # which-reaction-is-this — old question (which clue sorts reactions fastest)
    # cut to looks versus what went in. Old title and scene hinted at appearance,
    # so both are simplified. Reviewer: replies no longer use "rust and a flame
    # are the same kind of reaction", which pre-answered the THINK (can
    # combustion also be oxidation?); "Next:" now names the four questions that
    # actually come next.
    "which-reaction-is-this": dict(
        title="Four kinds of reaction, and no labels.",
        scene="You have met four kinds of reaction. In an exam nobody tells "
              "you which one you are looking at.",
        question="If you had to guess, what is the better clue to the kind of "
                 "reaction: what you can see happening, or what went in?",
        options=[
            ("What went in",
             "Looks can fool you: two powders can both turn black when heated "
             "and still be different kinds of reaction. The substances that go"
             " in give it away."),
            ("What you can see",
             "What you see is where everyone starts, but it can mislead. Two "
             "powders can both turn black when heated and still be different "
             "kinds of reaction. What went in tells you more."),
        ],
        answer=0,
        bridge="So count what went in first and name the reaction second. "
               "Next: four questions to ask, then eight reactions to name.",
    ),


    # ── Year 8 · C6 Acids and alkalis ───────────────────────────────────────────

    # acids-and-alkalis — old hook question cut to scales versus a dye (smell is
    # already ruled out by the scene). Title and scene kept. Reviewer: question
    # now asks "which would show you which is the acid", because "tell them
    # apart" let a sharp pupil argue that two solutions of different density can
    # be told apart on a balance. FLAG: the big question says one liquid is "safe
    # to drink", but the scene says both are dangerous (sodium hydroxide is not
    # safe to drink). Left unchanged because it does not give the answer away;
    # listed for Mide as a lesson-text issue.
    "acids-and-alkalis": dict(
        question="If you had to guess, which would show you which one is the "
                 "acid: weighing each, or adding a few drops of a dye?",
        options=[
            ("Weigh each one",
             "Weighing is how we tell many things apart. But nothing says an "
             "acid must be heavier than an alkali. What shows the difference "
             "is what each does to something."),
            ("Add a dye",
             "Acid and alkali are not things you can see or weigh. A dye "
             "changes colour differently in each, so it shows the difference "
             "in a second."),
        ],
        answer=1,
        bridge="A dye that does this is called an indicator. Next: what acid "
               "and alkali mean, then eight everyday bottles to sort.",
    ),

    # the-ph-scale-and-indicators — reviewer changed the angle to "does
    # blackberry juice do this too?" (the lesson's stretch: red cabbage, beetroot
    # and blackberries all hold the same kind of dye). The draft's "warmth, or
    # acid or alkali?" was given away by the H1 "The pH scale and indicators",
    # read straight after the acids-and-alkalis lesson. Scene keeps the writer's
    # fix (the six beakers hold different liquids).
    "the-ph-scale-and-indicators": dict(
        scene="A few drops of that purple liquid go into six beakers of "
              "different clear liquids. It comes out red in one, pink in "
              "another, purple in the third, then blue, then green, then "
              "yellow. The cabbage water was the same in every beaker.",
        question="If you had to guess, would juice squeezed from blackberries "
                 "change colour like this too, or only the cabbage water?",
        options=[
            ("Blackberry juice would too",
             "The colour in blackberries, beetroot and red cabbage is the same"
             " kind of dye. It changes shape in acids and alkalis, and each "
             "shape shows a different colour."),
            ("Only the cabbage water",
             "It does feel as if red cabbage must be special. But blackberries"
             " and beetroot hold the same kind of dye, and it changes colour "
             "in acids and alkalis in the same way."),
        ],
        answer=0,
        bridge="So the colour is a reading of how acidic or alkaline each "
               "liquid is, and a dye that gives one is called an indicator. "
               "Next: the two main indicators, and a number scale built from "
               "their colours.",
    ),

    # neutralisation — new angle: what is left in the dish after the water boils
    # off (the old title gave away "salty water" and the old scene the crystals).
    # Title and scene rewritten so they stop before the answer. Reviewer: wrong
    # reply no longer opens "That is a fair thought" after the page's "Fair
    # guess."
    "neutralisation": dict(
        title="Hydrochloric acid in one beaker. Sodium hydroxide in the other."
              " Both would burn you.",
        scene="The two are mixed carefully, in just the right amounts. The "
              "mixture warms up, and universal indicator comes out green: pH "
              "7, the same as pure water. Then all the water is boiled off in "
              "a dish.",
        question="If you had to guess, what is left in the dish: nothing at "
                 "all, or something solid?",
        options=[
            ("Nothing at all",
             "The liquid did test like pure water, so that makes sense. But "
             "the acid and alkali did not vanish. They made water and a salt, "
             "which stays behind as white crystals."),
            ("Something solid",
             "It is a salt, made from the acid and the alkali. It was "
             "dissolved in the water, so it only shows once the water has "
             "boiled away."),
        ],
        answer=1,
        bridge="A reaction between an acid and an alkali is called "
               "neutralisation. Next: the rule for what it always makes, then "
               "add the alkali drop by drop.",
    ),

    # acid-plus-metal — old hook question (where did the gas come from), cut to
    # metal versus acid. Title and scene kept. The later THINK ("What the bubbles
    # are") asks the same thing; the old hook already did, which the brief
    # allows.
    "acid-plus-metal": dict(
        question="If you had to guess, did the gas come from the metal, or "
                 "from the acid?",
        options=[
            ("From the metal",
             "It does look that way, because the metal vanishes as the bubbles"
             " appear. But the metal has dissolved into the liquid. The gas "
             "came out of the acid."),
            ("From the acid",
             "Every acid has hydrogen in it. The metal pushes the hydrogen out"
             " as a gas and takes its place in the liquid."),
        ],
        answer=1,
        bridge="The metal and the hydrogen swap places. Next: the rule for "
               "what always forms, then eight tubes to try with different "
               "metals and acids.",
    ),

    # acids-and-carbonates — new angle: rock or acid as the source of the gas
    # (the old scene's limewater result names the gas). Reviewer: the scene keeps
    # the old splint sentence, because the later THINK opens "The splint did go
    # out." and must still land; a splint going out does not name the gas (that
    # is the THINK's own point). Wrong reply no longer opens "Fair,".
    "acids-and-carbonates": dict(
        scene="The chip shrinks and streams bubbles from every surface. The "
              "gas is not hydrogen: a lit splint held to it goes out instead "
              "of squeaking.",
        question="If you had to guess, does the gas come out of the rock, or "
                 "out of the acid?",
        options=[
            ("Out of the rock",
             "The gas is carbon dioxide, and its carbon and oxygen were locked"
             " inside the rock. The acid sets them free."),
            ("Out of the acid",
             "With a metal the gas does come from the acid, so that makes "
             "sense. This time it comes from the rock, which has carbon and "
             "oxygen locked inside it."),
        ],
        answer=0,
        bridge="Marble, chalk and limestone are all carbonates, and all fizz "
               "in acid. Next: the rule for what an acid and a carbonate "
               "always make, and the test for the gas.",
    ),

    # making-a-pure-dry-salt — old hook question (how much oxide to add) in plain
    # words. Title, scene and big question kept. Reviewer: bridge no longer
    # repeats the reply's "filter it off".
    "making-a-pure-dry-salt": dict(
        question="If you had to guess, how much black powder should you add to"
                 " the acid: only just enough, or slightly too much?",
        options=[
            ("Only just enough",
             "Just enough sounds neat, but you cannot see when the acid has "
             "run out. Extra powder is easy to filter off later, and leftover "
             "acid is not."),
            ("Slightly too much",
             "Extra powder does not dissolve, so it sinks and you can filter "
             "it off. That way you know every drop of acid has been used up."),
        ],
        answer=1,
        bridge="After that come more decisions, all about getting clean "
               "crystals out of a blue liquid. Next: how salts get their "
               "names, then the six steps in order.",
    ),

    # catalysts — new angle: total oxygen (more, or the same but sooner). The old
    # scene said the powder "is not a reactant or product" and was weighed
    # afterwards, which pre-empted the later THINK ("used up or blocked?"), so
    # the scene is shortened. Title and big question kept. Reviewer: bridge no
    # longer says "without being used up" (the THINK's answer); it only names the
    # catalyst.
    "catalysts": dict(
        scene="Tip in a spatula of black powder and the same bottle froths "
              "over in seconds, giving off enough oxygen to relight a glowing "
              "splint.",
        question="If you had to guess, does the powder make the bottle give "
                 "off more oxygen in total, or the same amount, only sooner?",
        options=[
            ("More oxygen in total",
             "More froth in less time can look like more gas. But the bottle "
             "holds a fixed amount of hydrogen peroxide, so it gives the same "
             "oxygen in the end, powder or not."),
            ("The same, only sooner",
             "The bottle holds only so much hydrogen peroxide, so it can only "
             "ever make so much oxygen. The powder just gets it done much "
             "sooner."),
        ],
        answer=1,
        bridge="A powder that changes how fast a reaction goes like this is "
               "called a catalyst. Next: what a catalyst can and cannot do, "
               "then five flasks to test.",
    ),


    # ── Year 8 · C8 The periodic table ──────────────────────────────────────────

    # metals-and-non-metals — old hook question (which test separates them) as a
    # hammer guess. Title and scene kept; the later "does it conduct" THINK is
    # not touched. Reviewer: wrong reply no longer says "that is a fair thought"
    # after the page's "Fair guess."; bridge says non-metal SOLIDS shatter (many
    # non-metals are gases).
    "metals-and-non-metals": dict(
        question="If you had to guess, which one flattens when you hit it with"
                 " a hammer: the lead, or the graphite?",
        options=[
            ("The lead",
             "Lead is a metal, and metals change shape without breaking. The "
             "graphite shatters into black dust."),
            ("The graphite",
             "Graphite does feel soft, since it marks paper. But it is brittle"
             " and shatters into black dust, while the lead, a metal, "
             "flattens."),
        ],
        answer=0,
        bridge="Metals bend and non-metal solids shatter, but that is only one"
               " of several properties. Next: the full lists side by side, and"
               " six samples to sort.",
    ),

    # mendeleev — old hook question (leave a gap, or keep every square filled).
    # Reviewer: scene restores the rows-and-columns step (without it "does not
    # fit" has nothing to fit), options made parallel, replies no longer say the
    # gap "turned a problem into a prediction" (the answer to the later "Three
    # decisions" card d1), and the writer's replacement big question
    # ("predictions about elements nobody had ever seen") still pointed at empty
    # squares, so it is replaced with a neutral one.
    "mendeleev": dict(
        scene="Lay the cards in a line and the pattern shows up: a soft "
              "reactive metal, then several ordinary metals, then a violent "
              "gas, and then a soft reactive metal again. Cut the line into "
              "rows so the repeats fall into columns. In a few places, the "
              "next card does not fit the column it lands in.",
        question="If you had to guess, when the next card did not fit, did "
                 "Mendeleev leave a square empty, or keep every square filled?",
        options=[
            ("Left a square empty",
             "He left it empty, sure that an element belonging there had "
             "simply not been found yet."),
            ("Kept every square filled",
             "Moving cards along to avoid a hole looks tidy, but it puts "
             "elements in the wrong families. Mendeleev left the square empty "
             "instead."),
        ],
        answer=0,
        bridge="He even wrote down what each missing element would be like. "
               "Next: how he built the table, then a gap for you to fill.",
        big_question="Mendeleev sorted sixty-three elements into a table that "
                     "chemists still use. What did he do that nobody before "
                     "him had done?",
    ),

    # groups-and-periods — old hook question (row or column) turned into a
    # concrete guess about sodium. Title, scene and big question replaced: all
    # three said potassium is "two rows" from sodium, which is wrong (it is the
    # next row down). Reviewer: the scene now says potassium is "further down,
    # below sodium" rather than "right below it", so the opener stays true
    # without contradicting the THINK reveal's "two rows down" (a lesson-text
    # error listed for Mide); title and scene use the lesson's own group 1
    # description ("melts into a ball and whizzes") instead of "explodes".
    "groups-and-periods": dict(
        title="Drop sodium in water and it fizzes wildly.",
        scene="In the periodic table, magnesium is the square right next to "
              "sodium. Potassium is further down, below sodium.",
        question="If you had to guess, which behaves more like sodium in "
                 "water: magnesium, next to it, or potassium, below it?",
        options=[
            ("Magnesium, next to it",
             "Next door sounds like it should be alike, but magnesium barely "
             "fizzes in water. The element below sodium is the one that "
             "behaves like it."),
            ("Potassium, below it",
             "Potassium does the same as sodium, only more fiercely. Elements "
             "in the same column behave alike, like members of a family."),
        ],
        answer=1,
        bridge="So a column is a family, and a row is something different. "
               "Next: the names for each, and the first twenty elements to "
               "explore.",
        big_question="Which tells you more about an element: the row it sits "
                     "in, or the column?",
    ),

    # group-1-the-alkali-metals — reviewer changed the two options to "would it
    # still go dull in a jar with no air?" The draft's "air, or the metal cooling
    # down?" had a weak distractor (nothing in the scene suggests cooling), so a
    # strong Year 9 would get it for free; "shiny things just dull with time" is
    # the real intuition. Title drops the oil (a clue); old scene "nothing
    # touched it" and big question "what is attacking it" replaced.
    "group-1-the-alkali-metals": dict(
        title="Cut a lump of sodium and the new surface is a mirror, for about"
              " four seconds.",
        scene="Then the shine fades to a dull grey while you watch, in an "
              "ordinary room.",
        question="If you had to guess, would the cut sodium still go dull in a"
                 " sealed jar with no air in it?",
        options=[
            ("Yes, it would still go dull",
             "Lots of shiny things do dull with age, so that makes sense. But "
             "here the air is doing it: sodium reacts with it, and with no air"
             " it stays shiny."),
            ("No, it would stay shiny",
             "With no air there is nothing for it to react with. Sodium is so "
             "reactive that ordinary air dulls it within seconds."),
        ],
        answer=1,
        bridge="That is why sodium is kept under oil, and the rest of its "
               "group is the same. Next: what the group has in common, then "
               "three of them dropped into water.",
        big_question="Sodium loses its shine within seconds of being cut. What"
                     " is going on, and what does it tell you about the whole "
                     "group?",
    ),

    # group-7-the-halogens — new angle: will three very different-looking
    # elements make the same kind of substance with a metal? The old scene and
    # big question said "same group" and "same kind of family", which gives the
    # answer, so the scene names them without the group. Reviewer: title keeps
    # "Three sealed tubes" so the hook's rail label still lands; the question
    # asks about the KIND of substance made, not "the same way" (they react with
    # very different vigour, which the lesson teaches, so "the same way" was
    # arguable); the wrong reply no longer claims colour comes from melting
    # points.
    "group-7-the-halogens": dict(
        title="Three sealed tubes: a green gas, a red-brown liquid and a "
              "grey-black solid.",
        scene="Chlorine is a pale green gas, bromine a red-brown liquid and "
              "iodine a grey-black solid. Warm the iodine gently and it turns "
              "straight into a violet vapour. Now each one is put with the "
              "same metal.",
        question="If you had to guess, will the three make the same kind of "
                 "substance with the metal, or three quite different kinds?",
        options=[
            ("The same kind",
             "All three are in group 7, the halogens, and each one joins with "
             "a metal to make the same kind of salt: a chloride, a bromide or "
             "an iodide."),
            ("Three different kinds",
             "They do look very different. But each one joins with a metal to "
             "make the same kind of salt, because all three are in the same "
             "group."),
        ],
        answer=0,
        bridge="That sameness is what makes them a family. Next: the four you "
               "need to know, and how they change going down.",
        big_question="Group 1 got fiercer the further down you went. Do the "
                     "elements in group 7 follow the same pattern?",
    ),

    # group-0-and-why-groups-exist — old hook question (how do you miss an
    # element this common), cut to unreactive versus too rare. Title, scene and
    # big question kept; none of them gives the answer. Reviewer: correct reply
    # no longer says "with nothing to react with" (argon has plenty to react
    # with; it just does not).
    "group-0-and-why-groups-exist": dict(
        question="If you had to guess, why was argon missed: because it reacts"
                 " with nothing, or because there is too little of it?",
        options=[
            ("It reacts with nothing",
             "Chemists of the time found elements through their compounds, and"
             " argon makes none. Because it reacts with nothing, it left no "
             "trace."),
            ("There is too little",
             "One per cent is plenty: it is far more than the carbon dioxide "
             "they did find. The real problem was that argon reacts with "
             "nothing, so it left no trace."),
        ],
        answer=0,
        bridge="Argon belongs to a whole group of gases that react with almost"
               " nothing. Next: why, and what outer electrons have to do with "
               "it.",
    ),

    # metal-and-non-metal-oxides — new angle: which burnt product gives the acid.
    # The old scene gave the purple/red result and the big question gave the
    # rule, so both are rewritten. Title kept. Reviewer: scene no longer says
    # both products are "left behind" (burnt sulfur gives a gas).
    "metal-and-non-metal-oxides": dict(
        scene="Both catch and burn. What each one makes is collected and put "
              "into its own beaker of water. Then universal indicator goes in.",
        question="If you had to guess, which gives an acid in water: the burnt"
                 " magnesium, or the burnt sulfur?",
        options=[
            ("The burnt magnesium",
             "Magnesium is a metal, and its product makes the water alkaline "
             "instead. It is the burnt sulfur that makes an acid."),
            ("The burnt sulfur",
             "Sulfur burns to a gas that dissolves in water and makes an acid."
             " The burnt magnesium makes the water alkaline instead."),
        ],
        answer=1,
        bridge="It is the side of the periodic table the element comes from "
               "that decides which way the water goes. Next: oxides in "
               "general, and two beakers to test six of them.",
        big_question="Burn a metal and burn a non-metal, then drop each "
                     "product into water. What decides which way the pH goes?",
    ),


    # ── Year 8 · P1 Energy transfers ────────────────────────────────────────────

    # energy-stores — old hook question (used up, or moved somewhere) in plain
    # words. The title ("The energy does not"), scene ("nothing took it away")
    # and big question ("nothing is ever gone") all gave the answer, so all three
    # are rewritten; the ball and carpet stay because the store audit says "This
    # is the hook, with a bigger ball". Reviewer: the writer's big question
    # repeated the guess word for word, so it is replaced with the lesson's whole
    # question (stores and how energy moves).
    "energy-stores": dict(
        title="A ball rolling across a carpet.",
        scene="A ball rolls across a carpet, slows, and stops. While it rolled"
              " it had energy of movement. Now it is still.",
        question="If you had to guess, what happened to the ball's energy: is "
                 "it used up, or did it go somewhere else?",
        options=[
            ("It is used up",
             "It does look used up, as if the roll just ran out. But energy "
             "never disappears. It went into a tiny rise in the warmth of the "
             "ball and the carpet, too small to feel."),
            ("It went somewhere else",
             "Energy is never used up, only moved. Here it went into a tiny "
             "rise in the temperature of the ball and the carpet, too small to"
             " feel."),
        ],
        answer=1,
        bridge="Energy sits in different places, called stores, and moves "
               "between them. Next: the list of stores, and a ledger to fill "
               "in.",
        big_question="A moving ball, a stretched catapult, a battery in a "
                     "drawer: all of them hold energy. Where can energy be, "
                     "and how does it move from one place to another?",
    ),

    # energy-transfers-before-and-after — old hook was "what left the battery?";
    # cut to "is energy a kind of stuff, like water in a bottle?" (the lesson's
    # own ENER-11 picture). Avoids mass-energy (E=mc2) by never asking whether
    # the bank weighs less. Title, scene and big question unchanged.
    "energy-transfers-before-and-after": dict(
        question="If you had to guess, is the energy in a power bank a kind of"
                 " stuff, like water in a bottle?",
        options=[
            ("Yes, it is stuff",
             "A full bank and a flat one do feel like a full bottle and an "
             "empty one. But the balance says nothing was poured out: energy "
             "is not a substance at all."),
            ("No, it is not stuff",
             "Nothing was poured out of the bank, which is why the balance has"
             " nothing to report. Energy is a number you work out, not a "
             "substance."),
        ],
        answer=1,
        bridge="So \"where did it go?\" needs a better method than looking for "
               "something that left. Next: two columns, before and after, with"
               " the same total in each.",
    ),

    # conservation-of-energy — the old hook's answer (the energy is now a tiny
    # temperature rise in the air and pivot), asked as "is anything warmer?". Not
    # "gone or still somewhere": the H1 "Conservation of energy" sits right above
    # the hook and answers that. big_question rewritten: "Energy is supposed to
    # be conserved" hands over the answer.
    "conservation-of-energy": dict(
        question="If you had to guess, once the pendulum has stopped, is "
                 "anything in the room even a tiny bit warmer?",
        options=[
            ("Yes, a tiny bit warmer",
             "The air and the pivot have warmed by far too little to feel. "
             "That is where every joule of the swinging went."),
            ("No, nothing has changed",
             "It looks as if nothing has changed, because the warming is far "
             "too small to feel. But the air and the pivot are a tiny bit "
             "warmer, and that is where the swing's energy went."),
        ],
        answer=0,
        bridge="The pendulum stopped; the energy did not. Next: a running "
               "total that keeps score of every store while it swings.",
        big_question="A pendulum comes back almost as high, but only almost, "
                     "and after a few hundred swings it hangs straight down. "
                     "What happened to its energy?",
    ),

    # heating-and-thermal-equilibrium — old hook's question (which holds more
    # energy), reworded to "one spark or a whole bath". big_question rewritten:
    # "why does the cooler one do more damage" tells the pupil the bath wins; the
    # new one also avoids restating the injury claim.
    "heating-and-thermal-equilibrium": dict(
        question="If you had to guess, which holds more energy: the one spark,"
                 " or the whole bath?",
        options=[
            ("The whole bath",
             "There is so much water in a bath that, even at a gentler "
             "temperature, it holds far more energy than a tiny spark."),
            ("The one spark",
             "The spark is far hotter, so that makes sense. But hotter is not "
             "the same as more energy: a spark is a tiny speck, and a bath is "
             "a huge amount of water."),
        ],
        answer=0,
        bridge="Temperature and energy are two different things. Next: a bench"
               " where you set how much there is and how fast its particles "
               "move, separately.",
        big_question="A sparkler throws sparks at 1500 °C and they barely "
                     "sting. A bath at 40 °C makes you flinch. How can that "
                     "be?",
    ),

    # conduction — old hook's own question ("which is colder?") cut to two
    # options, with "Neither" as the answer. Big question KEPT: the touch test
    # closes on 'why the question "which is colder?" had no answer', which quotes
    # it. It misleads rather than gives away.
    "conduction": dict(
        question="If you had to guess, which spoon is actually colder?",
        options=[
            ("The metal spoon",
             "It certainly feels that way, and everyone agrees. But after a "
             "night in the same drawer both are at room temperature, and a "
             "thermometer would read the same for both."),
            ("Neither of them",
             "After a whole night in the same drawer, both are at room "
             "temperature. The metal only feels colder."),
        ],
        answer=1,
        bridge="So what is your hand actually feeling? It is how fast energy "
               "leaves your fingers, and metal takes it much faster than wood.",
    ),

    # radiation — ANGLE CHANGED (twice). Any "does it need something to carry
    # it?" guess is given away by the rail label "Across empty space", which
    # shows above the H1 on load, and by the old scene ("space is empty"). So the
    # guess is the old reveal's OTHER claim: the warmth is the same family of
    # thing as visible light. Old title, scene and big question are therefore
    # KEPT (none decides that), and the 150 million km / eight minutes rewrite is
    # dropped.
    "radiation": dict(
        question="If you had to guess, is the warmth you feel the same kind of"
                 " thing as the light you see?",
        options=[
            ("Yes, the same kind",
             "Both are waves of the same family. The warmth is infrared, which"
             " is like light at a wavelength your eyes cannot see."),
            ("No, something different",
             "Light and warmth do seem like two separate things, one for your "
             "eyes and one for your skin. But the warmth is the same kind of "
             "wave as light, just one your eyes cannot see."),
        ],
        answer=0,
        bridge="That wave is radiation, and it needs no material at all, which"
               " is how it crosses empty space. Next: take the other two "
               "routes away one at a time and see what is left.",
    ),

    # insulation — old hook (which melts first) reworded as "does the blanket
    # make the ice melt faster or slower". Title, scene and big question
    # unchanged (none gives the answer).
    "insulation": dict(
        question="If you had to guess, does the blanket make the ice melt "
                 "faster or slower?",
        options=[
            ("Slower",
             "The blanket slows the energy coming in from the room, so the "
             "wrapped ice lasts much longer."),
            ("Faster",
             "A blanket does feel warm when you are under it. But that warmth "
             "is your own body: the blanket only slows energy getting out, or "
             "in."),
        ],
        answer=0,
        bridge="A blanket does not make warmth. It slows a flow, whichever way"
               " the energy is going. Next: plan a fair trial before any "
               "readings exist.",
    ),

    # simple-machines — ANGLE CHANGED. The old question "where did the extra 500
    # N come from?" is arguable (the fulcrum really does push up with 700 N), so
    # it is cut to the observable trade underneath it: how far your hand moves
    # compared with the slab. Old title, scene and big question kept; the bridge
    # picks up the 500 N.
    "simple-machines": dict(
        question="If you had to guess, does your hand move further than the "
                 "slab rises, or less far?",
        options=[
            ("Much further",
             "Your end of the bar moves about six times as far as the slab "
             "rises. That is the price of pushing six times less hard."),
            ("Not as far",
             "The slab is the heavy end, so it is easy to think it moves the "
             "most. But your end of the bar travels about six times as far as "
             "the slab rises."),
        ],
        answer=0,
        bridge="So the bar trades force for distance. Next: a lever bench "
               "where you measure both ends and multiply.",
    ),


    # ── Year 8 · P5 Pressure ────────────────────────────────────────────────────

    # pressure-force-over-area — old hook asked why only one end goes in; cut to
    # "does the point push harder than your thumb does?" (PRESS-01). Scene and
    # big question rewritten: "under the same squeeze" and "the two forces are
    # equal" hand over the answer. Title kept: the safety note ("press the pin
    # against your fingertip") refers to its activity.
    "pressure-force-over-area": dict(
        scene="Rest the point of a drawing pin on a piece of wood and press "
              "gently on the flat head with your thumb. The head does nothing "
              "to your thumb. The point goes straight into the wood.",
        question="If you had to guess, does the point push on the wood harder "
                 "than your thumb pushes on the head?",
        options=[
            ("Yes, much harder",
             "Sharp things do seem to push harder. But a force meter would "
             "read the same at both ends: the point just squeezes that push "
             "onto a tiny spot."),
            ("No, just as hard",
             "The push is the same at both ends. At the point it is squeezed "
             "onto a tiny spot, so it digs in."),
        ],
        answer=1,
        bridge="That focusing has a name: pressure. Next: a block on sand, "
               "where you can change the push and the area separately.",
        big_question="A drawing pin is pressed into wood with a thumb. One end"
                     " goes into the wood and the other does not go into the "
                     "thumb. Why?",
    ),

    # pressure-in-liquids — old hook asked why the bottom jet is fastest; cut to
    # its two most tempting answers, "more water above" and "heavier water down
    # there" (PRESS-06). Title, scene and big question unchanged (none gives the
    # answer).
    "pressure-in-liquids": dict(
        question="If you had to guess, what makes the bottom jet fastest: more"
                 " water above it, or heavier water down there?",
        options=[
            ("More water above it",
             "The bottom hole has the most water stacked above it, pressing "
             "down, so the water is pushed out hardest there."),
            ("Heavier water down there",
             "Deep water does seem heavier. But a litre weighs the same "
             "anywhere in the can: what differs is how much water is stacked "
             "above each hole."),
        ],
        answer=0,
        bridge="So the jet depends on how deep the hole is. Next: lower a "
               "pressure probe through a tank and watch the reading.",
    ),

    # upthrust-floating-and-sinking — old hook asked where the upward shove comes
    # from; cut to the one fact it turns on (is the push the same all round?).
    # Title, scene, big question unchanged.
    "upthrust-floating-and-sinking": dict(
        question="If you had to guess, does the water push harder on the "
                 "bottom of the ball than on the top?",
        options=[
            ("No, the same all round",
             "Same water, so equal all round sounds sensible. But the bottom "
             "is deeper than the top, and water pushes harder the deeper it "
             "is."),
            ("Yes, harder underneath",
             "The bottom of the ball is deeper than the top, and water pushes "
             "harder the deeper it is. The difference is the shove you feel."),
        ],
        answer=1,
        bridge="That leftover upward push has a name: upthrust. Next: five "
               "one-litre blocks in a tank, and what decides which float.",
    ),

    # atmospheric-pressure — ANGLE CHANGED. "Pulled in from inside or pushed in
    # from outside?" is answered by the H1 "Atmospheric pressure" right above the
    # hook. The guess is now the old reveal's core claim: the outside air was
    # pressing that hard all along, and only the inside changed. Title and big
    # question rewritten: "Nothing touched the can" / "nothing goes anywhere near
    # it" are false (the air outside does the crushing) and the reply would
    # contradict them.
    "atmospheric-pressure": dict(
        title="A can folds in on itself.",
        question="If you had to guess, was the air outside pressing that hard "
                 "on the can all along, or only once it cooled?",
        options=[
            ("All along",
             "The air outside never changed. What changed was inside: the "
             "steam had been pushing back just as hard, until it cooled to a "
             "few drops of water."),
            ("Only once it cooled",
             "It does look as if something new happened outside. But nothing "
             "changed out there: the steam inside had been pushing back, and "
             "when it cooled and stopped, the outside push won."),
        ],
        answer=0,
        bridge="Air has weight, and it presses on everything, all the time. "
               "Next: take a sealed bag, a pan of water and a barometer up a "
               "mountain.",
        big_question="A little water is boiled in an empty can, which is then "
                     "sealed and cooled. The can is crushed flat. What crushes"
                     " it?",
    ),


    # ── Year 8 · P6 Waves and sound ─────────────────────────────────────────────

    # waves-on-water — the old hook's own question (what travelled across?) cut
    # to two options. Title, scene and big question KEPT: the rail label "The
    # gull that stays put" shows on load, so a guess about where the gull ends up
    # would be given away; this one is not.
    "waves-on-water": dict(
        question="If you had to guess, what crossed the pond: the water "
                 "itself, or only its up-and-down movement?",
        options=[
            ("The water itself",
             "It is easy to picture the water flowing across. But a cork or a "
             "heavy log would stay put just like the gull: the water only "
             "lifts and drops on the spot."),
            ("Only its movement",
             "Each patch of water lifts and drops on the spot and hands the "
             "movement on to the next. That is how the wave crosses while the "
             "gull stays put."),
        ],
        answer=1,
        bridge="That travelling disturbance is what a wave is, and it carries "
               "energy with it. Next: the parts of a wave, then a ripple tank "
               "to change them.",
    ),

    # transverse-waves-and-superposition — the old hook's own question cut to its
    # correct option ("the displacements add") and its most tempting wrong one
    # ("bounce off"). Not "carry on through": the bench gate's answer is "both
    # waves carry on out the far side". Scene and big question rewritten: "heave
    # twice as far", "rings pour through them" and "the surface obeys both at
    # once" gave the answer away. Title kept.
    "transverse-waves-and-superposition": dict(
        scene="Drop two stones into still water at the same moment, a metre "
              "apart. Two sets of rings spread out and run into each other.",
        question="If you had to guess, where two ripples meet, do they add "
                 "together, or bounce off each other?",
        options=[
            ("Add together",
             "Where they overlap, the water rises by what one ripple asks for "
             "plus what the other asks for. Two lifts make a bigger lift."),
            ("Bounce off each other",
             "Balls bounce. But ripples are not objects: where they meet, the "
             "water adds up what each one is asking for."),
        ],
        answer=0,
        bridge="That adding has a name: superposition. Next: two wave trains "
               "in one channel, where you set the height of each.",
        big_question="Two waves arrive at the same patch of water at the same "
                     "moment. What does the surface do?",
    ),

    # how-sound-is-made — old hook: what must happen for there to be a sound. Cut
    # to "air rushing past, or something shaking". Scene and big question
    # rewritten: "something under the skin is buzzing", "air moving is not
    # enough" and "moving to and fro" all hand over the answer.
    "how-sound-is-made": dict(
        scene="Two fingers on the front of your throat, and hum. Now stop "
              "humming and breathe out through an open mouth, so air still "
              "pours past the same place.",
        question="If you had to guess, what makes the humming sound: air "
                 "rushing past, or something shaking?",
        options=[
            ("Air rushing past",
             "Your breath does keep the hum going. But breathing out with no "
             "hum moves even more air and makes no note: air rushing past is "
             "not enough on its own."),
            ("Something shaking",
             "You can feel it under your fingers. Two folds in your throat "
             "shake, and that is what makes the note."),
        ],
        answer=1,
        bridge="Every sound starts with something vibrating, which means "
               "shaking quickly to and fro. Next: the four stages from source "
               "to listener, and a bench where you change what is vibrating.",
        big_question="A guitar string, a loudspeaker cone and two folds of "
                     "tissue in your throat all make sound. What do the three "
                     "have in common?",
    ),

    # sound-is-longitudinal — old hook's question (what does each coil do in the
    # squashed-up wave?) cut to its correct option and its most tempting wrong
    # one ("the coils do not move, only the patch travels"). "Sideways" was not
    # tempting: the scene says there is no hump. Big question unchanged: it does
    # not decide between moving and staying still.
    "sound-is-longitudinal": dict(
        question="If you had to guess, as the squashed-up patch passes, does "
                 "each coil shuffle along and back, or stay where it is?",
        options=[
            ("Shuffle along and back",
             "Each coil shuffles a little way along the slinky and back, then "
             "ends up where it began. Only the squashed patch travels to the "
             "far end."),
            ("Stay where it is",
             "Only the squashed patch reaches the far end, so it is easy to "
             "think the coils stay put. But a coil has to move to get "
             "squashed: it shuffles a little way along and back."),
        ],
        answer=0,
        bridge="Sound works like this second wave, not like the wavy line it "
               "is drawn as. Next: drive the slinky both ways and mark one "
               "coil.",
    ),

    # frequency-pitch-and-loudness — ANGLE CHANGED. Old hook was a loudspeaker
    # question with four technical options; cut to the everyday version: does
    # plucking harder change the pitch? Title, scene and big question rewritten:
    # the scene and big question stated which change does what.
    "frequency-pitch-and-loudness": dict(
        title="Pluck a guitar string.",
        scene="Pluck a guitar string gently and listen. Then pluck the same "
              "string much harder.",
        question="If you had to guess, does plucking harder make the note "
                 "higher as well as louder?",
        options=[
            ("No, only louder",
             "The note stays where it was. A harder pluck makes the string "
             "swing further, and that makes it louder."),
            ("Yes, higher too",
             "When people shout, their voices often go higher too. But on a "
             "string, how high the note is does not change with how hard you "
             "pluck."),
        ],
        answer=0,
        bridge="How far a string swings and how often it swings are two "
               "separate things. Next: two dials on a signal generator, one "
               "for each.",
        big_question="Two things can change about a note: how high it is and "
                     "how loud it is. What sets each one?",
    ),

    # sound-needs-a-medium — ANGLE CHANGED. "Can you still hear it once the air
    # is out?" is answered by the H1 "Sound needs a medium" right above the hook.
    # The guess is now the old hook's other tempting wrong option: does the
    # buzzer itself stop without air? Title, scene and big question rewritten:
    # "The sound is not", "you can still see the hammer beating" and "goes quiet
    # while you watch it still ringing" give that away.
    "sound-needs-a-medium": dict(
        title="A buzzer in a jar.",
        scene="A small buzzer hangs on a thread inside a thick glass jar, "
              "ringing away. A pump starts pulling the air out of the jar.",
        question="If you had to guess, once the air is out, does the little "
                 "hammer keep beating against the bell?",
        options=[
            ("Yes, it keeps beating",
             "The buzzer needs no air to work: through the glass you can see "
             "the hammer beating as fast as ever. What changes is what you "
             "hear."),
            ("No, it stops beating",
             "Plenty of things do need air, like a candle flame. But the "
             "buzzer runs on electricity, and its hammer keeps beating just as"
             " fast with the air gone."),
        ],
        answer=0,
        bridge="The buzzer never stops, yet its sound fades to nothing: there "
               "is no air left to carry it. Next: a hammer and a microphone, "
               "with different materials in the gap.",
        big_question="A buzzer rings inside a thick glass jar while a pump "
                     "takes the air out. What happens to the sound, and why?",
    ),

    # echoes-reflection-and-absorption — ANGLE CHANGED. The old hook was an echo
    # calculation, and the draft's "made by the cliff, or your own shout?" is
    # answered by the H1 ("...reflection..."). The guess is now the lesson's
    # second condition: a hard wall a few steps away gives no separate echo.
    # Title and scene KEPT (neither decides that). Big question rewritten:
    # "...and how far away it is" hands over the answer.
    "echoes-reflection-and-absorption": dict(
        question="If you had to guess, would a hard brick wall a few steps in "
                 "front of you give a clear echo?",
        options=[
            ("Yes, a clear echo",
             "A hard wall does send most of the sound back, so that makes "
             "sense. But from a few steps away it returns too quickly to hear "
             "on its own: it blends with your shout."),
            ("No, not a separate one",
             "The wall sends plenty of sound back, but it returns so fast that"
             " your ear runs it together with your shout. You hear one sound, "
             "a bit fuller."),
        ],
        answer=1,
        bridge="So an echo needs a surface that sends sound back, and enough "
               "distance for it to arrive late. Next: move the wall, change "
               "what it is made of, and time the echo.",
        big_question="The same shout comes straight back at you off a cliff "
                     "and vanishes without trace in a bedroom. What decides "
                     "which happens?",
    ),

    # hearing-and-auditory-range — the old hook's own question cut to its correct
    # option and its most tempting wrong one: too quiet for us, or too high? (The
    # draft's "no sound at all" was weak, since the dog reacts, and its options
    # broke the length rule.) big_question rewritten: "two statements about the
    # ears of one particular animal, and that animal is us" points at the answer.
    "hearing-and-auditory-range": dict(
        question="If you had to guess, is the whistle too quiet for people to "
                 "hear, or too high?",
        options=[
            ("Too quiet",
             "That makes sense, since the dog hears it and we do not. But a "
             "microphone shows the note is loud, not faint: it is too high for"
             " human ears."),
            ("Too high",
             "A microphone picks up a strong, steady note, far higher than any"
             " note you can hear. Turning it up would not help."),
        ],
        answer=1,
        bridge="Every ear has a top and a bottom to what it can hear. Next: "
               "sound one tone and try it on different listeners, from a bat "
               "to an elephant.",
        big_question="The words infrasound and ultrasound sound like names for"
                     " two kinds of sound. What do they really mean?",
    ),

    # ultrasound-at-work — ANGLE CHANGED. Old hook asked how to find a hidden
    # crack (a list of four methods); cut to the one fact it turns on: does a
    # crack send sound back? Title and scene kept. big_question rewritten:
    # "...bring back information" points at the echo.
    "ultrasound-at-work": dict(
        question="If you had to guess, would a short pulse of sound sent into "
                 "the steel bounce back off a hidden crack?",
        options=[
            ("Yes, some of it would",
             "Sound is reflected wherever it meets a different material, and a"
             " crack is steel meeting air. Some of the pulse comes back."),
            ("No, it would all pass through",
             "A crack is tiny and holds nothing but air, so it is easy to "
             "think sound would cross it. But wherever steel meets air, much "
             "of the sound bounces back."),
        ],
        answer=0,
        bridge="Time that echo and you can work out how deep the crack is. "
               "Next: a probe on a block, and the time a pulse takes to come "
               "back.",
        big_question="How can you find a crack hidden inside solid steel "
                     "without cutting it open?",
    ),


    # ── Year 8 · P7 Light ───────────────────────────────────────────────────────

    # light-travels — old hook (which arrives first) is too obvious, so the guess
    # asks whether the flash takes any time at all (LIGHT-01, elicited by the
    # hook in the register). Scene rewritten: it said "the flash is instant",
    # which gave the answer. Review: bridge rewritten (it was ungrammatical and
    # its "Next" skipped the explainers that come first).
    "light-travels": dict(
        scene="Lightning hits a hillside two kilometres away. You see the "
              "flash, then count about six seconds before the thunder arrives."
              " The flash and the bang left the hillside at the same moment.",
        question="If you had to guess, how long does the flash take to reach "
                 "you?",
        options=[
            ("No time at all",
             "It looks instant, and across a room it is far too quick to "
             "notice. But light does take time: sunlight takes over eight "
             "minutes to reach us."),
            ("A tiny amount of time",
             "Light is not instant, but it is so fast that two kilometres "
             "takes it only about seven millionths of a second."),
        ],
        answer=1,
        bridge="Sound in air needs about six seconds for the same trip, which "
               "is why the bang arrives so late. Next: what light shares with "
               "sound, and the two ways it is different.",
    ),

    # reflection-mirrors-and-scattering — guess is "does the mirror send back
    # much more light than paper?" (LIGHT-07, elicited by the hook). Scene and
    # big_question changed because both stated that the two send back about the
    # same amount. Review: bridge "Next" now names the explainer that really
    # comes next.
    "reflection-mirrors-and-scattering": dict(
        scene="Hold a mirror up to a window and the room brightens. Hold up a "
              "sheet of white paper and the room brightens too. Only the "
              "mirror shows you your own face.",
        question="If you had to guess, does the mirror send back much more "
                 "light than the paper?",
        options=[
            ("No, about the same",
             "Paper sends back nearly as much light as a mirror, which is why "
             "a white page looks so bright."),
            ("Yes, much more",
             "A mirror does look more dazzling, so it is easy to think so. But"
             " white paper sends back most of the light that lands on it, "
             "nearly as much as the mirror."),
        ],
        answer=0,
        bridge="So the amount of light is not what lets a mirror show your "
               "face. Something about the surface does. Next: the one rule "
               "every surface obeys.",
        big_question="A mirror and a sheet of paper obey exactly the same rule"
                     " when light lands on them. Only one of them shows you "
                     "your face, and the reason is the surface rather than the"
                     " rule.",
    ),

    # refraction — guess is what really bends, the straw or the light from it
    # (LIGHT-09; this is the old hook's own question). Review: the draft's "does
    # the straw really bend?" is trivially "no" for a strong Year 9, so it asks
    # the old hook's either/or instead. Title, scene and big_question changed:
    # "not broken", "perfectly straight" and "straight and looks broken" all gave
    # it away, and the draft's big_question ("between the straw and your eye")
    # pointed at the light.
    "refraction": dict(
        title="A straw in a glass of water.",
        scene="You stand a straw in a glass of water and look at it from the "
              "side. At the surface it seems to snap, and the part under the "
              "water looks shorter and shifted sideways.",
        question="If you had to guess, what really bends: the straw, or the "
                 "light coming from it?",
        options=[
            ("The straw itself",
             "It really does look bent, so that is easy to believe. But lift "
             "the straw out and it is perfectly straight. What bends is the "
             "light travelling from the straw to your eye."),
            ("The light from it",
             "The straw stays perfectly straight. The light from the part "
             "under the water changes direction as it leaves the water, and "
             "your eye is fooled."),
        ],
        answer=1,
        bridge="Light changes direction like that because its speed changes "
               "between water and air. Next: why light slows down in water and"
               " glass.",
        big_question="A straw stood in a glass of water looks snapped at the "
                     "surface. What is really going on?",
    ),

    # lenses-and-images — guess is which way up the pinhole picture lands
    # (LIGHT-13, elicited by the hook). Title and scene changed: both said
    # "upside down". Review: bridge rewritten (it had no content and its "Next"
    # skipped the explainers); it now keeps the old commit's point that nothing
    # in the box flips the light.
    "lenses-and-images": dict(
        title="A shoebox with a pin-prick in it.",
        scene="Take a shoebox, make one clean pin-prick in one end and stretch"
              " greaseproof paper across the other. Point the pin-prick at a "
              "bright window. A picture of the window appears on the paper, in"
              " colour.",
        question="If you had to guess, is the picture on the paper the right "
                 "way up or upside down?",
        options=[
            ("Right way up",
             "The window is the right way up. But light goes in straight lines"
             " and the rays cross at the hole, so the picture lands upside "
             "down."),
            ("Upside down",
             "Upside down, and swapped left to right too. Light travels in "
             "straight lines, so the rays cross at the hole."),
        ],
        answer=1,
        bridge="Nothing in the box turns the light over: there is no lens, no "
               "glass and no mirror. Next: how straight lines alone make the "
               "picture.",
    ),

    # the-eye-and-the-camera — old hook cut to the two options that matter:
    # pupils alone, or the eye itself becoming more sensitive (LIGHT-18, elicited
    # by the hook). Review: "after a minute" dropped (the retina's gain takes
    # several minutes, so the comparison at one minute is arguable); options
    # given parallel "Your …" wording; bridge given content and a true "Next".
    "the-eye-and-the-camera": dict(
        question="If you had to guess, what does more to help you see as you "
                 "wait?",
        options=[
            ("Your pupils open wider",
             "Pupils do open, and that helps a little. But the bigger change "
             "takes minutes, at the back of the eye, which becomes thousands "
             "of times more sensitive."),
            ("Your eyes get more sensitive",
             "The pupil opens in about a second and lets in perhaps ten times "
             "more light. The big change takes minutes: the back of the eye "
             "becomes thousands of times more sensitive."),
        ],
        answer=1,
        bridge="A camera can copy the first trick, but it has nothing to match"
               " the second. Next: the job an eye and a camera share.",
    ),

    # colour-and-the-spectrum — guess is where the colours came from (LIGHT-21,
    # elicited by the hook; the bench gate repeats the old hook's question, which
    # is allowed). Title and big_question changed: "all of them at once" and "It
    # is not making any of them" gave it away. Review: wrong reply no longer
    # doubles "Fair guess … fair thought"; bridge "Next" now names the explainers
    # that come next.
    "colour-and-the-spectrum": dict(
        title="Sunlight through a block of glass.",
        question="If you had to guess, were the colours already in the "
                 "sunlight, or did the glass add them?",
        options=[
            ("Already in the sunlight",
             "The colours were there all along. The glass just spreads them "
             "out so you can see each one."),
            ("Added by the glass",
             "They only appear after the glass, so it is easy to think so. But"
             " clear glass has no colour to add. It spreads out what was "
             "already in the sunlight."),
        ],
        answer=0,
        bridge="White light is a mixture, and the glass sorts it. Next: what "
               "white light is made of, and why glass bends some colours more "
               "than others.",
        big_question="A plain, colourless block of glass turns a beam of "
                     "sunlight into a band of colours. What is the glass "
                     "really doing to the light?",
    ),

    # why-things-look-coloured — guess is what colour the red jumper looks under
    # the green lamp (LIGHT-27/28; the bench gate asks the same, but the old
    # scene already stated "almost black", so nothing new is pre-answered). Scene
    # and big_question changed: both said it looks almost black. Review: bridge
    # given content and a true "Next" (the explainers come before the bench).
    "why-things-look-coloured": dict(
        scene="A disco lamp fitted with a deep green filter is the only light "
              "in the room. A white shirt looks green and a green bag looks "
              "green. Then someone walks in wearing a bright red jumper.",
        question="If you had to guess, what colour does the red jumper look "
                 "now?",
        options=[
            ("Almost black",
             "A red jumper can only send back red light, and a green lamp has "
             "none to send. So almost nothing reaches your eyes."),
            ("Still red",
             "That is how it looks in daylight. But the green lamp gives no "
             "red light for the jumper to send back, so it looks nearly black."),
        ],
        answer=0,
        bridge="So the colour you see depends on the light as well as on the "
               "jumper. Next: what a surface does with the light that lands on"
               " it.",
        big_question="A red jumper, a white shirt and a green bag look "
                     "different in a room lit by one coloured lamp. What "
                     "decides the colour you see?",
    ),


    # ── Year 8 · P8 Electric circuits ───────────────────────────────────────────

    # current-and-circuits — guess is whether cutting the wire AFTER the bulb
    # also puts it out (CIRC-03, elicited by the hook). Title and scene changed:
    # both said the bulb goes out wherever you cut. The torch stays, so ladder
    # rung 3 and the "gap behind the bulb" explainer still land. Review: bridge
    # given content and a true "Next".
    "current-and-circuits": dict(
        title="A torch with a cut wire.",
        scene="A torch has a cell, a bulb and two strips of metal joining them"
              " into a ring. Cut the ring on the way to the bulb and the bulb "
              "goes dark.",
        question="If you had to guess, what happens if you cut it on the way "
                 "back from the bulb instead?",
        options=[
            ("The bulb still lights",
             "It is easy to think so, since the electricity has already been "
             "through the bulb. But the flow is a ring, so a gap on either "
             "side stops it everywhere."),
            ("The bulb goes dark",
             "Electricity flows all the way round a ring, so a break anywhere "
             "stops the whole flow at once."),
        ],
        answer=1,
        bridge="So a circuit is not a one-way delivery to the bulb. Next: what"
               " is actually moving in the wire, and why it needs the whole "
               "ring.",
    ),

    # series-and-parallel — old hook's correct answer (each light has its own
    # path) against its fuse-box distractor (CIRC-08, which the register says the
    # hook elicits AND confronts). Review: the draft's "one long chain" was not
    # tempting once the scene says the house stays lit, and it dropped CIRC-08.
    # Title and scene kept (they set up the contrast without saying which wiring
    # is which).
    "series-and-parallel": dict(
        question="If you had to guess, why does the rest of the house stay "
                 "lit?",
        options=[
            ("Each light has its own path",
             "Every light has its own branch off the supply, so a broken bulb "
             "breaks only its own branch and the rest carry on."),
            ("The fuse box keeps them on",
             "A fuse box is there to cut the power when something goes wrong, "
             "not to keep lights on. The rest stay lit because each light has "
             "its own path to the supply."),
        ],
        answer=0,
        bridge="A cheap string of decorations has only one path, which is why "
               "one dead bulb darkens the lot. Next: the two ways to join a "
               "second bulb to a battery.",
    ),

    # current-at-a-junction — old hook (water below vs above the island) cut to
    # the right answer and its "left behind" distractor (CIRC-12, elicited and
    # confronted by the hook). Title and scene kept; big_question does not
    # mention the river. Review: question reworded to ask about the flow; bridge
    # "Next" now names the junction explainer that comes next.
    "current-at-a-junction": dict(
        question="If you had to guess, how much water flows below the island, "
                 "compared with above it?",
        options=[
            ("The same amount",
             "The island neither soaks up water nor makes any, so the two "
             "channels together carry exactly what arrived."),
            ("Less than above",
             "It can feel as if some water is lost down the narrow channel. "
             "But that water is still flowing, and the channels rejoin "
             "carrying the full amount."),
        ],
        answer=0,
        bridge="A wire that splits in two behaves the same way, and for the "
               "same reason. Next: what a junction is, and what can and cannot"
               " happen there.",
    ),

    # potential-difference — the old hook's own question, what the number on a
    # bulb means, cut to the right answer and CIRC-16 (which the register says
    # the hook elicits AND confronts). Review: the draft changed the angle to
    # "what happens on 12 V", which dropped CIRC-16 when the old question
    # converts fine. Scene changed: it said the 2.5 V bulb "flares once and dies"
    # on 12 V, which pointed at the answer. Title kept; it matches the rail label
    # "The number on a bulb".
    "potential-difference": dict(
        scene="A torch bulb says 2.5 V. A car headlamp says 12 V. A mains lamp"
              " in your house says 230 V.",
        question="If you had to guess, what is that number telling you?",
        options=[
            ("How much electricity it uses",
             "Lots of people read it that way. But it is not an amount being "
             "used up: it is the voltage the bulb is designed to run on."),
            ("The voltage it is built for",
             "It is the voltage the maker designed it for. Much less and it "
             "glows dimly; much more and the thin wire inside burns out."),
        ],
        answer=1,
        bridge="Volts measure a push, not an amount of electricity. Next: what"
               " that push actually is, and how you measure it.",
    ),

    # resistance — the old hook's own question in everyday words: is the flow
    # smaller only at the bulb, or all the way round? (the "used up on the way"
    # belief against one smaller current). Review: the draft asked "does the bulb
    # dim?", which the H1 "Resistance" next to a thin wire strongly implies, and
    # which a Year 9 finds obvious. Old title and scene restored (they say the
    # bulb dims, which no longer gives anything away).
    "resistance": dict(
        question="If you had to guess, is less electricity flowing only "
                 "through the bulb, or all the way round?",
        options=[
            ("Only through the bulb",
             "It is easy to picture the wire using some up before it reaches "
             "the bulb. But in one loop the flow is the same everywhere, so it"
             " has fallen all the way round."),
            ("All the way round",
             "In one loop the flow is the same at every point. The thin wire "
             "makes the whole loop harder to get through, so less flows "
             "everywhere."),
        ],
        answer=1,
        bridge="How hard something makes it for charge to get through has a "
               "name: resistance. Next: what resistance is, and why measuring "
               "it takes two meters.",
    ),

    # conductors-and-insulators — old hook cut to the tempting near-miss (a
    # million, true of tap water) against the real figure. big_question changed:
    # it stated "more than a million million". Review: bridge "Next" now names
    # the explainer that comes next (the test gap comes after three explainers).
    "conductors-and-insulators": dict(
        question="If you had to guess, how much harder is it to push "
                 "electricity through the plastic than through the copper?",
        options=[
            ("About a million times",
             "That is about right for tap water. Plastic is far beyond it: "
             "over a million million times harder to get through than copper."),
            ("Over a million million times",
             "Copper lets charge through easily and plastic hardly lets any "
             "through at all. That huge gap is what makes a cable work."),
        ],
        answer=1,
        bridge="A gap that size needs a reason. Next: what copper has inside "
               "it that plastic does not.",
        big_question="Conductor and insulator are not two kinds of thing. They"
                     " are the two ends of one scale of resistance. How far "
                     "apart are they?",
    ),

    # building-and-measuring-a-circuit — old hook cut to a loose connection
    # against the "faulty meter" belief (CIRC-25, elicited by the hook). Title,
    # scene and big_question kept. Review: the draft's "Their ammeter reads
    # wrongly" was arguable (an ammeter with a blown internal fuse does break the
    # loop and darken the lamp), so it is now the old option's "reading low",
    # which cannot explain a dark lamp; bridge "Next" fixed.
    "building-and-measuring-a-circuit": dict(
        question="If you had to guess, what is most likely wrong with the pair"
                 " whose lamp stays dark?",
        options=[
            ("A loose connection",
             "A loop only works if every joint in it grips, and a crocodile "
             "clip biting the plastic coating instead of the metal can look "
             "perfectly fine."),
            ("The ammeter reads too low",
             "A meter reading low would give an odd number, but it could not "
             "make the lamp go dark. A dark lamp means the loop is broken, "
             "most often at a clip that is not gripping."),
        ],
        answer=0,
        bridge="Where each meter goes matters just as much as a tight clip. "
               "Next: why an ammeter and a voltmeter go in different places.",
    ),


    # ── Year 9 · B6 Health and drugs ────────────────────────────────────────────

    # what-drugs-do-to-the-body — is the caffeine in coffee a drug? (DRUG-01,
    # "drugs are illegal", elicited by the hook). Review: the draft asked "what
    # makes a substance a drug?", and the H1 "What drugs do to the body" points
    # straight at "changing how your body works"; the draft's big_question also
    # listed caffeine among drugs. Title and scene changed: they said coffee
    # contains a drug. big_question now neutral.
    "what-drugs-do-to-the-body": dict(
        title="A mug of coffee.",
        scene="A mug of coffee has around 90 milligrams of caffeine in it. A "
              "café sells it to anyone, at any age, with no prescription.",
        question="If you had to guess, is the caffeine in coffee a drug?",
        options=[
            ("Yes, it is a drug",
             "A drug is any substance that changes the way the body works. "
             "Caffeine changes how your nerve cells behave, which is why "
             "people drink it."),
            ("No, it is just a drink",
             "It is legal and sold in cafés, so it is easy to think not. But a"
             " drug is any substance that changes how the body works, and "
             "caffeine does: it keeps your nerve cells firing so you feel "
             "alert."),
        ],
        answer=0,
        bridge="Legal or not, prescribed or not, addictive or not: those are "
               "separate questions. Next: follow one dose of a drug round the "
               "body, stage by stage.",
        big_question="What makes a substance a drug, and what does a drug "
                     "actually do once it is in your blood?",
    ),

    # alcohol-and-smoking — guess is whether the famous sobering-up methods work
    # (DRUG-03). Scene changed: it said all three do nothing and that only one
    # organ can remove alcohol. Review: scene kept closer to Design's clinical
    # wording ("far too much to drink" dropped); question no longer calls them
    # "tricks"; bridge says "for someone else", as the bench does, and names the
    # bench, which really is next.
    "alcohol-and-smoking": dict(
        scene="Three things people are certain will sober someone up. Friends "
              "try all three on someone who has been drinking.",
        question="If you had to guess, do any of the three get the alcohol out"
                 " of the blood faster?",
        options=[
            ("No, none of them do",
             "The alcohol is in the blood, and only the liver can clear it, at"
             " a steady rate of roughly one unit an hour."),
            ("Yes, they speed it up",
             "People swear by them, and coffee does make a drunk person feel "
             "more awake. But nothing speeds up the liver, so the alcohol "
             "clears just as slowly."),
        ],
        answer=0,
        bridge="Next: build an evening's drinks for someone else, try each way"
               " of sobering up, and run the clock.",
    ),

    # substance-misuse-and-decisions — does coming from a plant make a substance
    # safer? (DRUG-05, the page's own title claim). Review: the draft's "natural
    # or legal" against "what it does to the body" is near-circular and obvious
    # to a Year 9; this keeps the title's claim as the guess. Scene changed: the
    # old one argued the answer (nightshade, foxglove, "the ground has no
    # opinion"). Old hook's answer is the same point, so claim c1 at the bench is
    # no more pre-answered than before.
    "substance-misuse-and-decisions": dict(
        scene="An advert says a herbal sleep remedy is gentle and safe because"
              " it is made from plants, not chemicals.",
        question="If you had to guess, does coming from a plant make a "
                 "substance safer?",
        options=[
            ("Yes, it is usually safer",
             "Lots of people believe it, so it is easy to think so. But deadly"
             " nightshade and foxglove are both plants and both are poisonous,"
             " while a factory-made medicine comes at a known dose."),
            ("No, it tells you nothing",
             "Deadly nightshade and foxglove are both plants, and both are "
             "poisonous. Where a substance comes from says nothing about what "
             "it does to a body."),
        ],
        answer=1,
        bridge="What a substance does, and in what amount, is a question only "
               "evidence can answer. Next: five claims about drugs, each with "
               "its evidence, and a fault to find in each.",
    ),


    # ── Year 9 · B9 Ecosystems and interdependence ──────────────────────────────

    # food-chains-and-food-webs — old hook cut to energy running out against the
    # tempting "too big to hunt". Title and big_question kept. Review: scene
    # changed, because its last clause ("whether the organisms are enormous or
    # microscopic") ruled out the size option and so gave the answer; options
    # made parallel; wrong reply no longer says energy "runs out" (the page
    # confronts energy being "lost").
    "food-chains-and-food-webs": dict(
        scene="Chains stop. Grass, rabbit, fox, and then nothing. Four or five"
              " links is about the limit anywhere in the world, on land or at "
              "sea.",
        question="If you had to guess, what stops a food chain getting any "
                 "longer?",
        options=[
            ("There is not enough energy left",
             "Only about a tenth of the energy passes up each step, so very "
             "little is left after four steps. There is not enough to feed "
             "another level."),
            ("Top animals are too big to hunt",
             "Some top animals are big, but plenty of chains end with small "
             "ones, like a sparrowhawk. What stops the chain is that too "
             "little energy reaches the top."),
        ],
        answer=0,
        bridge="Next: climb a food chain level by level and watch how much "
               "energy arrives at each one.",
    ),

    # predator-and-prey — old hook cut to "only the weak" against "fewer rabbits,
    # hungrier foxes". Title, scene and big_question kept. Review: OK as drafted.
    "predator-and-prey": dict(
        question="If you had to guess, why do foxes not eat all the rabbits?",
        options=[
            ("Foxes only catch weak rabbits",
             "Foxes do catch weak rabbits, but they take healthy ones too. "
             "What really protects the rabbits is that foxes need them: when "
             "rabbits get scarce, foxes go hungry."),
            ("With fewer rabbits, foxes go hungry",
             "As rabbits get scarce, foxes go hungry and fewer cubs survive. "
             "Then the fox numbers fall and the rabbits recover."),
        ],
        answer=1,
        bridge="Next: run the years on a field of rabbits and foxes, and watch"
               " what happens to the two numbers.",
    ),

    # disturbing-a-food-web — does the oak end up better or worse off without
    # ladybirds? (the old hook's "the oak does better, with one fewer insect"
    # option against its answer). Review: the draft asked "does it change
    # anything for the oak?", and the H1 "Disturbing a food web" (plus the
    # title's "What happens to the oak tree?") strongly implies yes. big_question
    # changed: "pull one thread and the whole thing moves" gave it away. Scene's
    # last sentence ("whether an effect can travel that far") dropped for the
    # same reason.
    "disturbing-a-food-web": dict(
        scene="A ladybird has never touched an oak leaf, and an oak tree has "
              "no opinion about ladybirds. In between them sit three other "
              "kinds of organism.",
        question="If you had to guess, does the oak end up better off or worse"
                 " off?",
        options=[
            ("Better off",
             "One fewer insect sounds good for a tree. But ladybirds eat "
             "aphids, so without them aphids multiply and drain sap from the "
             "oak's young shoots."),
            ("Worse off",
             "Without ladybirds, aphids multiply and drain sap from the oak's "
             "young shoots, so the tree grows less."),
        ],
        answer=1,
        bridge="That is only one route to the oak, and there is a second. "
               "Next: the whole oak wood, and what happens when you take one "
               "species out of it.",
        big_question="What happens to the rest of a food web when one species "
                     "is taken out of it?",
    ),

    # pollinators-and-food-security: the poster's own claim as the guess (would
    # we starve?), so the wrong option is ECO-07, which the lesson records as
    # elicited by the hook. big_question changed: the old one ("you would not
    # starve ... never eat an apple") states the answer. Title and scene kept.
    "pollinators-and-food-security": dict(
        question="If you had to guess, with no bees or other pollinating "
                 "insects, would people starve?",
        options=[
            ("Yes, most crops would fail",
             "That is what the poster says, and it sounds right. But wheat, "
             "rice and maize are pollinated by the wind, so most of the "
             "world's calories would carry on."),
            ("No, but most fruit would go",
             "Wheat, rice and maize are pollinated by the wind, and they give "
             "most of the world's calories. What would go is most of the "
             "fruit, nuts and vegetables."),
        ],
        answer=1,
        bridge="Enough to eat is not the same as a healthy diet. Next: twelve "
               "foods on a supermarket shelf, and what happens to each with no"
               " pollinators.",
        big_question="Bees and other insects carry pollen from flower to "
                     "flower. If they all vanished, what would the world "
                     "actually lose?",
    ),

    # toxic-build-up-in-a-food-chain: what makes the pesticide pile up (very
    # poisonous vs never breaking down), the lesson's own persistence-not-
    # toxicity point. Angle changed from the draft (fish vs water): the H1 "Toxic
    # build-up in a food chain" points straight at the food. Title and scene
    # kept. big_question changed: "Nothing is added along the way. The arithmetic
    # does it." gives the answer away.
    "toxic-build-up-in-a-food-chain": dict(
        question="If you had to guess, what lets the pesticide pile up in the "
                 "birds: being very poisonous, or never breaking down?",
        options=[
            ("Being very poisonous",
             "Being poisonous decides how much harm it does once it arrives. "
             "Whether it piles up depends on whether bodies can break it down "
             "or get rid of it."),
            ("Never breaking down",
             "A chemical that never breaks down stays in every animal that "
             "takes it in, so each predator collects the doses from all the "
             "prey it eats."),
        ],
        answer=1,
        bridge="Nothing more was sprayed along the way: the food chain did the"
               " collecting. Next: follow the pesticide up a lake food chain, "
               "level by level.",
        big_question="A pesticide at a level far too low to harm anything in "
                     "the water can still kill the bird at the top of the food"
                     " chain. How can that happen?",
    ),

    # sampling-an-ecosystem: old hook cut to the key choice, squares picked by
    # chance vs squares that look typical. Question now says what the squares are
    # for; wrong reply no longer claims bias always favours the flowery patches
    # (the lesson says bias has no favourite direction). Title, scene and big
    # question kept: none says which way of choosing is better.
    "sampling-an-ecosystem": dict(
        question="If you had to guess, to estimate from a few small squares, "
                 "which should you count: squares picked by chance, or squares"
                 " that look typical?",
        options=[
            ("Squares picked by chance",
             "Picking by chance means you cannot favour flowery or bare "
             "patches, even by accident, so the squares stand for the whole "
             "field."),
            ("Squares that look typical",
             "That sounds sensible, but the choice is yours, and your own "
             "preferences creep in. Every square can then be off in the same "
             "direction."),
        ],
        answer=0,
        bridge="Choosing fairly is half the job, and how many squares you take"
               " is the other half. Next: survey a field where you can check "
               "your estimate against the real total.",
    ),


    # ── Year 9 · B10 Inheritance and dna ─────────────────────────────────────────

    # variation-continuous-and-discontinuous: is a counted characteristic (number
    # of pets) like height or like blood group? The wrong option is GENE-02's "it
    # is a number, so it is continuous", which the lesson records as elicited by
    # the hook. Title and scene changed: the old ones stated the in-between test
    # outright. The new scene keeps blood group's four piles, because the hook's
    # rail label is "Four piles". big_question changed: "The difference is not
    # what you measured with" points at the answer.
    "variation-continuous-and-discontinuous": dict(
        title="One class, lined up two ways.",
        scene="Line your class up by height and the line runs smoothly from "
              "shortest to tallest. Sort the same class by blood group and you"
              " get four separate piles: A, B, AB and O.",
        question="If you had to guess, is the number of pets each pupil has "
                 "more like height, or more like blood group?",
        options=[
            ("More like height",
             "It is a number. But nobody has two and a half pets: the counts "
             "jump from two to three, so they fall into separate piles."),
            ("More like blood group",
             "Pets are counted, and nobody has two and a half of them. Nothing"
             " sits between two and three, so the counts fall into separate "
             "piles."),
        ],
        answer=1,
        bridge="Being a number is not the test. What matters is whether any "
               "value can sit in between. Next: predict the graph for six "
               "characteristics, then plot the data.",
        big_question="Some differences between people run along a smooth scale"
                     " and others fall into separate groups. What decides "
                     "which kind a characteristic is?",
    ),

    # chromosomes-genes-and-dna: old hook cut to coiled and packed vs most of it
    # kept elsewhere. (The old "cut into pieces" option stays dropped: the 46
    # chromosomes are separate pieces, so it was arguable.) big_question changed:
    # the old one says the four words are "nested inside each other", which
    # previews the packing answer. Title and scene kept.
    "chromosomes-genes-and-dna": dict(
        question="If you had to guess, how does two metres of DNA fit inside "
                 "one tiny nucleus?",
        options=[
            ("Most of it is kept elsewhere",
             "It is a very small space. But the whole two metres is inside the"
             " nucleus. It fits because it is very thin and coiled up tightly."),
            ("It is coiled up tightly",
             "DNA is incredibly thin, and it is wound round proteins, then "
             "coiled again and again. All two metres really are inside the "
             "nucleus."),
        ],
        answer=1,
        bridge="The coiled packages are called chromosomes, and the pieces "
               "inside them have names too. Next: zoom in from a whole person "
               "down to the letters that spell out an instruction.",
        big_question="Nucleus, chromosome, gene, DNA: people often use these "
                     "four words as if they meant the same thing. How do they "
                     "actually fit together?",
    ),

    # how-we-worked-out-dna: one brilliant person vs several teams' work put
    # together (NOS-03, the flash-of-insight story the lesson confronts). Angle
    # changed from the draft (microscope vs X-rays): the hook's rail label "Too
    # small to see" and the H1 "How we worked out DNA's structure" both point
    # away from a microscope. Title and scene kept (the scene's microscope line
    # no longer bears on the guess). big_question changed: the old one lists the
    # X-ray photo, the ratios and the models, which gives the answer.
    "how-we-worked-out-dna": dict(
        question="If you had to guess, was the shape of DNA worked out by one "
                 "brilliant person, or by several teams?",
        options=[
            ("One brilliant person",
             "That is how the story is often told. But it took X-ray pictures "
             "from one lab, chemical measurements from another and model "
             "building in a third."),
            ("Several teams together",
             "X-ray pictures taken in London, chemical measurements made in "
             "New York and models built in Cambridge all had to fit together."),
        ],
        answer=1,
        bridge="Nobody ever saw the molecule: each piece of evidence ruled "
               "some shapes out. Next: use the evidence of 1952 to build a "
               "model of DNA, one decision at a time.",
        big_question="Nobody has ever seen a DNA molecule directly. So how did"
                     " anyone work out its shape?",
    ),

    # passing-it-on-heredity: old hook cut to hidden-but-still-there vs mixed in
    # and watered down (GENE-07, blending, which the lesson records as elicited
    # by the hook). Scene changed: "Not medium plants. Tall ones, every time"
    # rules blending out, and "carrying something that had not shown itself"
    # gives the answer. New scene keeps "come back" for the rail label "It came
    # back". big_question changed: "cannot be a fluid that mixes" states the
    # result.
    "passing-it-on-heredity": dict(
        scene="Then breed those tall plants together, and short plants come "
              "back in about a quarter of the offspring.",
        question="If you had to guess, what happened to the shortness while "
                 "every plant grew tall?",
        options=[
            ("Hidden, but still there",
             "The instruction for short was carried, complete and unchanged, "
             "by plants that looked tall. Nothing was lost along the way."),
            ("Mixed in and watered down",
             "Mixing paint works like that. But the shortness came back at "
             "full strength, so it was never watered down."),
        ],
        answer=0,
        bridge="Inherited information comes in separate units that keep their "
               "identity from one generation to the next. Next: grow pea seeds"
               " from two parent plants and count the flower colours.",
        big_question="A characteristic can vanish for a whole generation and "
                     "then come back. What does that tell us about how it is "
                     "passed on?",
    ),

    # what-makes-a-species: old hook cut to the two tests (can have a baby vs
    # babies can have babies); the wrong option is GENE-10. Scene changed: it
    # said mules almost never have offspring and that the mule is why horses and
    # donkeys are two species, which hands over the fertile test. big_question
    # changed: it says "neither is being able to breed", which gives the answer
    # away.
    "what-makes-a-species": dict(
        scene="Mules are strong, healthy and long-lived, and they have been "
              "bred deliberately for four thousand years.",
        question="If you had to guess, are a horse and a donkey the same "
                 "species?",
        options=[
            ("Yes, the same species",
             "They can have a foal together, so it is easy to think so. But a "
             "mule almost never has young of its own, and that makes a horse "
             "and a donkey two species."),
            ("No, two different species",
             "Their mule is healthy, but it almost never has young of its own."
             " To be one species, the offspring must be able to have young "
             "too."),
        ],
        answer=1,
        bridge="Even this test will not settle every pair. Next: seven tricky "
               "cases to judge, and the last few are ones that biologists "
               "still argue about.",
        big_question="A great dane and a chihuahua look nothing alike, but "
                     "they are one species. What is the test for being the "
                     "same species?",
    ),


    # ── Year 9 · B11 Evolution extinction and biodiversity ───────────────────────

    # variation-and-competitive-success: in a drought, the big strong mouse or
    # the small quick one? The bench's own reversal; the wrong option is EVOL-01
    # (strongest survive), which the lesson records as elicited by the hook.
    # Angle changed from the draft and title/scene restored: the hook's rail
    # label is "Until it is not", which only lands if the title keeps "A thick
    # coat is an advantage. Until it is not." That title gives away the draft's
    # coat question, so the guess moved to size in a drought.
    "variation-and-competitive-success": dict(
        question="If you had to guess, in a long drought, which mouse is more "
                 "likely to survive: a big, strong one, or a small, quick one?",
        options=[
            ("The big, strong one",
             "Strength sounds as if it should win, and in a fight it might. "
             "But a big body needs more water and more food, and in a drought "
             "there is neither."),
            ("The small, quick one",
             "A small body needs little water and cools easily, so it copes "
             "best when the water runs out. Size has become a cost, not an "
             "asset."),
        ],
        answer=1,
        bridge="No difference is best everywhere; it depends on the "
               "conditions. Next: put the same five mice through five "
               "different conditions.",
    ),

    # natural-selection: old hook cut to stretching-and-passing-it-on (EVOL-03)
    # vs long-necked giraffes having more babies. Scene changed: it calls the
    # stretching story "wrong". New scene sets up the puzzle neutrally.
    # big_question changed: "Not one animal in the population changes..." states
    # the mechanism; the draft's replacement repeated the scene.
    "natural-selection": dict(
        scene="A giraffe's neck is about two metres long, which lets it reach "
              "leaves that most other animals cannot. Its ancestors had much "
              "shorter necks.",
        question="If you had to guess, how did giraffes end up with such long "
                 "necks?",
        options=[
            ("Stretching, then passing it on",
             "That was once a leading scientific idea, and it sounds sensible."
             " But stretching changes only that one giraffe's body, and its "
             "babies are not born with the extra length."),
            ("Long-necked giraffes had more babies",
             "Some giraffes were born with longer necks than others. In hard "
             "times they reached more food, so more of them survived to have "
             "babies with long necks too."),
        ],
        answer=1,
        bridge="It is the group that changes, one generation at a time. Next: "
               "watch it happen with pale and dark moths on a tree trunk.",
        big_question="Over many generations, a whole species can change its "
                     "shape. What actually makes that happen?",
    ),

    # when-the-environment-changes-extinction: old hook cut to two everyday
    # survival traits (big and strong vs breeding fast and eating anything).
    # Bridge now ties back to the dormice in the scene instead of repeating the
    # wrong reply. Title, scene and big question kept.
    "when-the-environment-changes-extinction": dict(
        question="If you had to guess, what helps an animal most when its home"
                 " changes?",
        options=[
            ("Breeding fast, eating anything",
             "A fast breeder gets many chances to produce young that suit the "
             "new home, and an unfussy eater can use whatever food is left."),
            ("Being big, strong and fierce",
             "Big and strong helps in a fight, but a change to the home is not"
             " a fight. Slow breeders with fussy diets can run out of options."),
        ],
        answer=0,
        bridge="A dormouse has one small litter a year and eats only a few "
               "foods, which is why it did not come back. Next: try four "
               "species against five kinds of change.",
    ),

    # biodiversity-and-gene-banks: why can one disease wipe out a field of
    # clones? Each clone is weak (the property-of-the-plant error the lesson
    # names) vs they all share one weak spot. Angle changed from the draft's
    # yes/no, which the new scene ("a huge field of identical plants") made
    # obvious to a Year 9. Scene changed: it already said the Gros Michel was
    # wiped out and the same fungus is moving through the Cavendish; that history
    # now sits in the bridge. Title and big question kept.
    "biodiversity-and-gene-banks": dict(
        scene="A clone is an exact genetic copy. Cavendish bananas are grown "
              "from cuttings, never from seed, so a plantation is a huge field"
              " of identical plants.",
        question="If you had to guess, why could one disease wipe out a whole "
                 "field of these bananas?",
        options=[
            ("Each clone is a weak plant",
             "A Cavendish plant is as healthy as any other banana. The danger "
             "is that every plant is the same, so whatever kills one can kill "
             "them all."),
            ("They all share one weak spot",
             "Every plant is the same plant, so whatever can kill one can kill"
             " all of them. There is no different plant left that happens to "
             "resist."),
        ],
        answer=1,
        bridge="The Gros Michel, the banana before the Cavendish, was lost "
               "this way, and a fungus is now attacking the Cavendish. Next: "
               "plant four fields, from identical to mixed, and release a "
               "blight.",
    ),


    # ── Year 9 · C7 Energy changes in reactions ─────────────────────────────────

    # energy-and-changes-of-state: which takes more heat, melting the ice or
    # warming the melted water by ten degrees? Melting (about 334 kJ against
    # about 42 kJ per kg), so the answer is safe. It does not open a new later
    # prediction: the scene already says energy goes in at the same rate, and the
    # old reveal already said melting takes "a great deal" of energy. Bridge
    # changed: "Next: step through a heating curve" was not what comes next (two
    # explainer paragraphs come first), and "-20 °C" used a hyphen. Title, scene
    # and big question kept: none says where the energy goes.
    "energy-and-changes-of-state": dict(
        question="If you had to guess, which takes more heat: melting a lump "
                 "of ice, or then warming the melted water by ten degrees?",
        options=[
            ("Warming the water",
             "Warming feels like where the heat goes, because that is what the"
             " thermometer shows. But melting takes far more, and the "
             "thermometer does not show it."),
            ("Melting the ice",
             "Melting takes far more heat. The flame has to pull the ice's "
             "particles out of their fixed places, and that eats up the energy"
             " while the temperature sits still."),
        ],
        answer=1,
        bridge="So the four still minutes are not a pause: the energy is going"
               " somewhere a thermometer cannot see. Every change of state "
               "works this way, in one direction or the other.",
    ),

    # exothermic-reactions: old hook cut to "your body heat vs the pouch itself";
    # the pouch reaching 50 °C, hotter than a body, is the reasoning the reply
    # uses. Scene changed: "nothing added from outside" rules out the pocket
    # answer. Title kept ("in a pocket, on a cold day" is the tempting clue).
    # big_question changed: the old one points at the answer and pre-answers the
    # later spark prediction. The draft's replacement called the hand warmer a
    # chemical change, which the lesson's own bench says it is not. Bridge:
    # dropped "Next: run five beakers" because two explainer paragraphs come
    # first.
    "exothermic-reactions": dict(
        scene="No battery, no flame, nothing plugged in. The pouch was at the "
              "same temperature as the room a moment before. It stays hot for "
              "about an hour, then goes cold, and it can be reset by boiling "
              "it.",
        question="If you had to guess, does the warmth come from your body "
                 "heat in the pocket, or from inside the pouch?",
        options=[
            ("Your body heat",
             "A pocket is warm. But the pouch started at room temperature, "
             "cooler than you, and it still got hotter than your body."),
            ("Inside the pouch",
             "The pouch heats itself. Snapping the disc starts a change "
             "inside, and energy that was stored in the chemicals comes out as"
             " heat."),
        ],
        answer=1,
        bridge="A change that gives energy out to its surroundings like this "
               "is called <strong>exothermic</strong>.",
        big_question="Some changes make their surroundings hot, from a "
                     "campfire to a hand warmer. Where does that heat come "
                     "from?",
    ),

    # endothermic-reactions: old hook cut to "did the heat that left the water
    # vanish, or did the chemicals take it in?" Deliberately NOT "does the
    # reaction make cold?", because that is the later predict (think-commit-
    # cold). Bridge: dropped "Next: sort eight changes" because two explainer
    # paragraphs come first. Title, scene and big question kept.
    "endothermic-reactions": dict(
        question="If you had to guess, what happened to the heat that left the"
                 " water?",
        options=[
            ("It simply disappeared for good",
             "It looks that way, since the thermometer only reads what is left"
             " in the water. But energy is never destroyed, only moved."),
            ("The chemicals took it in",
             "The reaction needed energy to go ahead, and it took it from the "
             "water, the beaker and the air. They lost energy, so they got "
             "colder."),
        ],
        answer=1,
        bridge="A change that takes energy in from its surroundings like this "
               "is called <strong>endothermic</strong>: last lesson run in "
               "reverse.",
    ),

    # measuring-a-temperature-change: old hook cut to unreliable thermometers vs
    # heat escaping. Wrong reply now answers the option it follows. Bridge:
    # dropped "Next:" because two explainer paragraphs come first. Title, scene
    # and big question kept: the scene rules out different chemicals and made-up
    # numbers but does not say where the difference comes from.
    "measuring-a-temperature-change": dict(
        question="If you had to guess, what mainly caused the different "
                 "answers?",
        options=[
            ("Heat escaping to the room",
             "A beaker is always leaking heat to the bench and the air, so the"
             " later and slower the reading, the more has already escaped."),
            ("The thermometers being unreliable",
             "Thermometers can be a little off, but not by five degrees. What "
             "really differed was how long each beaker was losing heat before "
             "it was read."),
        ],
        answer=0,
        bridge="So the skill is in the set-up as well as in the reading.",
    ),


    # ── Year 9 · C9 Metals and materials ────────────────────────────────────────

    # the-reactivity-series: old hook cut to "size of the piece vs kind of metal"
    # (the scene shows a pea of potassium and a lump of calcium, so size is a
    # fair tempting answer). Deliberately NOT "does a metal that ignores water
    # also ignore acid?", which is the later predict (think-commit-water). Title,
    # scene and big question kept.
    "the-reactivity-series": dict(
        question="If you had to guess, what decides whether a metal fizzes in "
                 "cold water?",
        options=[
            ("The kind of metal",
             "Each metal has its own reactivity, just as each has its own "
             "melting point. A pea of potassium fizzes, but a whole bar of "
             "copper would not."),
            ("The size of the piece",
             "A bigger piece can fizz harder, which is why size feels "
             "important. But a huge lump of copper still does nothing, and a "
             "tiny pea of potassium does."),
        ],
        answer=0,
        bridge="Test metals against the same liquids and they line up in one "
               "order. Next: that order, and a bench of twelve test tubes to "
               "check it.",
    ),

    # predicting-displacement: old hook cut to "out of the liquid vs from inside
    # the iron". Title, scene and big_question changed: they named copper
    # sulfate, said the blue faded and said the nail came out coated in copper,
    # so the liquid was given away as the source. New title keeps the coated nail
    # for the rail label. Bridge rewritten: the draft's bridge repeated the
    # second explainer, and the first explainer opens "That is a displacement
    # reaction", so the bridge has to end on the event itself.
    "predicting-displacement": dict(
        title="An iron nail in a blue liquid, left for ten minutes.",
        scene="The nail comes out coated in a soft, pink-brown metal. Nobody "
              "painted it, and nobody added any metal to it.",
        question="If you had to guess, where did the pink-brown coating come "
                 "from?",
        options=[
            ("From inside the iron",
             "The nail does change colour. But iron has no copper in it, and "
             "one metal never turns into another. The coating came out of the "
             "liquid."),
            ("Out of the blue liquid",
             "The blue liquid is copper sulfate, which has copper in it. The "
             "coating is that copper, come out of the liquid onto the nail."),
        ],
        answer=1,
        bridge="The iron took the copper's place in the liquid, which is why "
               "the blue colour faded as the coating grew.",
        big_question="A nail comes out of a blue liquid wearing a coat of "
                     "metal that nobody added. Where did it come from, and "
                     "could you have said so in advance?",
    ),

    # getting-metals-out-of-rocks: old hook ("why can the copper not simply be
    # melted out?") cut to "mixed in like raisins, or joined into the stone".
    # Scene changed: "no amount of melting the stone will pour any out" gives the
    # result away; the bridge now brings it back after the guess. big_question
    # changed: it repeats the same melting clause (and the draft's replacement
    # repeated the scene). Bridge: the draft's "Next" repeated the second
    # explainer.
    "getting-metals-out-of-rocks": dict(
        scene="The stone is malachite. Roughly half of it, by mass, is copper."
              " But it does not look like copper, bend like copper or conduct "
              "electricity like copper.",
        question="If you had to guess, is the copper mixed into the stone like"
                 " raisins in a cake, or joined into it?",
        options=[
            ("Mixed in like raisins",
             "If bits of copper metal were mixed in, they would still look and"
             " behave like copper. This copper has joined with other elements,"
             " so it no longer looks like a metal."),
            ("Joined into the stone",
             "The copper is chemically joined to other elements, in this stone"
             " to oxygen and carbon. That is why it has lost its copper look."),
        ],
        answer=1,
        bridge="That is why no amount of melting will pour the copper out: "
               "melting cannot pull joined elements apart. Getting it free "
               "takes a chemical reaction.",
        big_question="Most metals come out of the ground in rocks that look "
                     "nothing like metal. How do you get the metal out?",
    ),

    # ceramics-polymers-and-composites: old hook ("which is the stronger
    # material?") cut to which would hold your weight (plate vs beaker), because
    # everyday "stronger" could be argued either way. Scene changed: "you could
    # stand on the plate and it would hold you" gives the answer away.
    # big_question kept as the draft's trimmed version of the lesson's own
    # question. Question reworded: the draft's "if you stood on it flat on the
    # floor" read as if you were flat on the floor. FLAG: the lesson asserts a
    # china plate would hold a person standing on it. That needs the plate fully
    # supported on a hard, flat floor; a plate on a raised foot ring may crack.
    # Mide's science call.
    "ceramics-polymers-and-composites": dict(
        scene="The plate breaks into eleven pieces. The beaker bounces twice "
              "and rolls under a chair.",
        question="If you had to guess, with each one laid on the floor, which "
                 "would hold your weight if you stood on it?",
        options=[
            ("The china plate",
             "The plate takes far more force before it fails, which makes it "
             "the stronger material. It is just that when it does fail, it "
             "fails all at once."),
            ("The plastic beaker",
             "The beaker survived the fall, so it seems the stronger one. But "
             "surviving a knock is toughness: under a steady weight the beaker"
             " gives way long before the plate does."),
        ],
        answer=0,
        bridge="Strong and tough are different properties, so \"which is "
               "better\" depends on the job. Next: three families of material, "
               "and four jobs to match them to.",
        big_question="A china plate shatters on a tiled floor and a plastic "
                     "beaker bounces. So which of the two is the stronger "
                     "material?",
    ),


    # ── Year 9 · C10 The earth and its atmosphere ────────────────────────────────

    # inside-the-earth — old hook question cut to two options: earthquake waves
    # vs volcano lava (the old hook's own tempting option, and the "mantle is
    # molten" family of beliefs). The camera option was ruled out by the scene
    # itself. Title, scene and big question do not give it away.
    "inside-the-earth": dict(
        question="If you had to guess, how do scientists know what is deep "
                 "inside the Earth, right down to the centre?",
        options=[
            ("Listening to earthquakes",
             "Earthquake waves go right through the planet, and the way they "
             "speed up, bend or stop shows what they have passed through."),
            ("Studying volcano lava",
             "Lava does come up from below. But it starts nowhere near the "
             "centre. Earthquake waves are what travel right through the "
             "planet."),
        ],
        answer=0,
        bridge="Hundreds of instruments around the world record those waves, "
               "and each layer leaves its mark on them. Next: the four layers "
               "they reveal.",
    ),

    # three-ways-to-make-a-rock — old question (what does the fizz tell you)
    # reframed as "what did the marble start life as?" (the lesson's own phrase);
    # tempting wrong answer is lava because of the crystals. No
    # title/scene/big_question change.
    "three-ways-to-make-a-rock": dict(
        question="If you had to guess, what did the marble start life as?",
        options=[
            ("Cooled lava",
             "The crystals do look like lava rock, and the granite did start "
             "as melted rock. But marble fizzes in acid because it is a "
             "carbonate: it began as limestone made of sea shells."),
            ("Sea shells",
             "The fizz shows marble is a carbonate, like the shells in "
             "limestone. It began as limestone on a sea floor, then was baked "
             "and squeezed deep underground."),
        ],
        answer=1,
        bridge="Granite and marble look alike but have completely different "
               "life stories. Next: the three ways to make a rock, and the "
               "clues each one leaves.",
    ),

    # the-rock-cycle — old hook question made everyday (how did shells get up
    # Everest). CHANGED scene: the old one said the sea floor itself was lifted,
    # which is the answer. CHANGED big_question: "once sand on a beach, before
    # that a mountain" gives away that rock moves and changes. Title kept, so the
    # rail stop "Fossils on Everest" still lands.
    "the-rock-cycle": dict(
        scene="The rock at the top of the highest mountain on Earth is "
              "limestone, full of the shells of sea creatures. Limestone forms"
              " on a warm shallow sea floor.",
        question="If you had to guess, how did sea shells get to the top of "
                 "Everest?",
        options=[
            ("The sea was once that high",
             "The sea has never been that high; there is not enough water on "
             "Earth. It was the sea floor that moved, pushed up when two "
             "continents collided."),
            ("The ground was pushed up",
             "Two continents collided and shoved an old sea floor up into a "
             "mountain. It is still rising a little today."),
        ],
        answer=1,
        bridge="Rock moves, and over long times it changes. Next: follow a "
               "single grain on its journey through different kinds of rock.",
        big_question="Rock seems permanent. Where has a rock been, and where "
                     "will it go next?",
    ),

    # a-planet-with-limits — old hook cut to "is new aluminium ore still dug up
    # every year?". CHANGED big_question: the old one said the crust is not
    # topped up and recycling returns only some, which hints the answer.
    "a-planet-with-limits": dict(
        question="If you had to guess, is new aluminium ore still dug up every"
                 " year?",
        options=[
            ("Yes, every year",
             "We use more aluminium every year, so the amount in use keeps "
             "growing, and recycled metal alone cannot cover that."),
            ("No, not any more",
             "Recycling aluminium works very well. But demand keeps growing, "
             "so new ore is still dug up every year."),
        ],
        answer=0,
        bridge="Next: run a recycling loop and see how far a kilogram goes "
               "round for different materials.",
        big_question="Everything we make came out of the ground. How much of "
                     "it can go round again?",
    ),

    # whats-in-the-air — the old hook's own question (what fraction is oxygen)
    # cut to its two strongest options. CHANGED title and scene: "most of what
    # went in did nothing" and "great majority came back unchanged" gave away
    # that oxygen is the minority. Rail stop "One breath" still lands.
    "whats-in-the-air": dict(
        title="Take a deep breath.",
        scene="Your lungs just took in about half a litre of air, and your "
              "body used some of it.",
        question="If you had to guess, how much of the air is oxygen?",
        options=[
            ("Most of it",
             "You need oxygen to stay alive. But it is only about a fifth of "
             "the air; nearly four fifths is nitrogen."),
            ("About a fifth",
             "Only about a fifth of the air is oxygen. Nearly four fifths is "
             "nitrogen, which your body breathes straight back out unused."),
        ],
        answer=1,
        bridge="Next: open up each gas in the mix and see what your lungs do "
               "with it.",
    ),

    # carbon-dioxide-humans-and-climate — the old hook question (where do the
    # extra 33 degrees come from) cannot be asked fairly: the H1 "Carbon dioxide,
    # humans and climate" names a gas in the air, which gives "the air" away. So
    # the angle moves one step on, to the mechanism's classic wrong picture
    # (gases trap the sunlight coming in), which the H1 does not answer. Big
    # question kept as Design's verbatim: it no longer gives the answer away.
    "carbon-dioxide-humans-and-climate": dict(
        question="If you had to guess, how do gases in the air keep the Earth "
                 "those 33 degrees warmer?",
        options=[
            ("Trapping sunlight on the way in",
             "That is the picture most people have. But sunlight passes "
             "straight through these gases. What they slow down is the heat "
             "the warmed ground gives off on its way back out."),
            ("Slowing heat on the way out",
             "Sunlight passes straight through these gases and warms the "
             "ground. The ground gives off heat as infrared, and the gases "
             "absorb it, so energy leaves more slowly than it arrives."),
        ],
        answer=1,
        bridge="That is the greenhouse effect, and it is natural: without it "
               "the planet would be frozen. Next: how it works, one step at a "
               "time.",
    ),


    # ── Year 9 · P2 Energy at home ──────────────────────────────────────────────

    # energy-in-food — old hook (why two numbers) as same-thing vs different-
    # things. CHANGED scene: dropped "neither is a mistake and neither is a
    # rounding of the other", which tilts the guess.
    "energy-in-food": dict(
        scene="Every food label in the country carries both. A 50 g bag of "
              "crisps: 229 kcal, 958 kJ.",
        question="If you had to guess, do those two numbers measure the same "
                 "thing, or two different things?",
        options=[
            ("The same thing",
             "Both are the same energy, written in two different units, like 6"
             " feet and 1.83 metres. One kcal is a bit over 4 kJ."),
            ("Two different things",
             "They look too different to match. But both measure the energy in"
             " the crisps; one is in kcal and the other in kJ."),
        ],
        answer=0,
        bridge="Next: burn food and measure its energy yourself with a "
               "calorimeter.",
    ),

    # power-ratings-in-watts — the old hook question, two of its four options. No
    # title/scene/big_question change.
    "power-ratings-in-watts": dict(
        question="If you had to guess, which uses more energy in a day, the "
                 "kettle or the router?",
        options=[
            ("The kettle",
             "The kettle is far more powerful. But it is on for about three "
             "minutes and the router for eight hours, so the router uses more."),
            ("The router",
             "The router's power is tiny, but it runs for eight hours against "
             "the kettle's three minutes, and that adds up to a little more "
             "energy."),
        ],
        answer=1,
        bridge="That is the difference between power and energy. Next: race "
               "the kettle against the router on a bench.",
    ),

    # calculating-energy-transferred — old hook with "about the same"
    # (surprising) vs "the shower, far more" (tempting). No
    # title/scene/big_question change.
    "calculating-energy-transferred": dict(
        question="If you had to guess, how does the shower's energy compare "
                 "with the lamp's?",
        options=[
            ("The shower uses far more",
             "A shower is far more powerful. But the lamp runs for 144 times "
             "as long, and that almost exactly makes up for it."),
            ("They are about the same",
             "They come out almost exactly the same. The shower uses energy "
             "about 140 times faster, but the lamp is on 144 times longer, so "
             "it evens out."),
        ],
        answer=1,
        bridge="Energy comes from power multiplied by time. Next: how to work "
               "it out, and the unit slip that makes answers sixty times "
               "wrong.",
    ),

    # reading-a-fuel-bill — old hook (kilowatt vs kilowatt-hour) put in everyday
    # words: how fast vs how much. No title/scene/big_question change.
    "reading-a-fuel-bill": dict(
        question="If you had to guess, does one unit on a bill measure how "
                 "fast you use electricity, or how much you use?",
        options=[
            ("How fast you use it",
             "A unit is a kilowatt-hour. Kilowatts do measure how fast, but "
             "the hour on the end turns it into a total amount."),
            ("How much you use",
             "A unit is a kilowatt-hour: a 1 kW appliance running for an hour."
             " The hour tells you it counts an amount."),
        ],
        answer=1,
        bridge="Next: see four different ways of using exactly one unit.",
    ),
}


def validate():
    """Fail the build loudly on a malformed entry, never render half of one."""
    for slug, g in START_HERE.items():
        where = "start_here[%r]" % slug
        q = g.get("question", "")
        if not (q.startswith(PREFIX) and q.endswith("?")):
            raise ValueError("%s question must start %r and end '?': %r"
                             % (where, PREFIX, q))
        opts = g.get("options") or []
        if len(opts) != 2 or not all(
                isinstance(o, tuple) and len(o) == 2 and o[0] and o[1]
                for o in opts):
            raise ValueError("%s needs exactly two (text, reply) options."
                             % where)
        if g.get("answer") not in (0, 1):
            raise ValueError("%s answer must be 0 or 1." % where)
        if not g.get("bridge"):
            raise ValueError("%s needs a bridge." % where)
        extra = set(g) - {"question", "options", "answer", "bridge",
                          "title", "scene", "big_question"}
        if extra:
            raise ValueError("%s has unknown field(s) %s." % (where,
                                                              sorted(extra)))


def apply(lesson):
    """The lesson with its opener swapped, or the lesson unchanged."""
    g = START_HERE.get(lesson.get("slug"))
    if g is None:
        return lesson
    lesson = dict(lesson)
    p = dict(lesson.get("phenomenon") or {})
    p["guess"] = True
    p["commit"] = g["question"]
    p["options"] = [o[0] for o in g["options"]]
    p["replies"] = [o[1] for o in g["options"]]
    p["answer"] = g["answer"]
    p["reveal"] = g["bridge"]
    if g.get("title"):
        p["title"] = g["title"]
    if g.get("scene"):
        p["prompt"] = g["scene"]
    lesson["phenomenon"] = p
    if g.get("big_question"):
        lesson["big_question"] = g["big_question"]
    return lesson
