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
            ("It stays black",
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
            ("It is pumped across",
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
