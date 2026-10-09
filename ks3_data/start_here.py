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
            ("It can swim about",
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
            ("Yes, it is empty",
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
            ("It burnt away",
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
