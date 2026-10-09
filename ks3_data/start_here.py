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
