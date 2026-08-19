# -*- coding: utf-8 -*-
"""B3 lesson 08 — Bacteria in the gut: twelve questions (MRB-269).

The lesson makes one argument: the thirty trillion bacteria in your large
intestine are not tolerated, they are part of the system. It proves it by
subtraction — the germ-free mouse, and the switch-it-off instrument that
rebuilds that mouse one job at a time. Five jobs: fermenting fibre, making
vitamin K and B vitamins, occupying the space a harmful species would take,
training the immune system, and maintaining the gut wall. Then it turns the
argument over: what the bacteria get out of the deal, and what happens when
the balance shifts.

The bank probes the two halves the lesson cares about most and that a student
can most easily half-learn. First, job discrimination — the five jobs are easy
to list and hard to tell apart, so several questions switch one job off and ask
which consequence follows, with the other four jobs' consequences sitting there
as distractors. Second, location — the key fact says which bacteria are helpful
depends on species and on where they are, and that is the idea the lesson's
own confrontation spends most of its words on.

Distractors are built from the lesson's two declared misconceptions.
**DIET-17** ("bacteria are germs; having bacteria inside you means you are
ill") supplies every option that treats bacteria as contamination — the
newborn injection read as something that kills bacteria, "any bacterium inside
you is a problem", the species alone deciding harm, the mouse with a gut
community being the one at risk, and the surgeon's worry being only the few
genuinely harmful species. **CELL-08** ("one cell means simple") supplies the
options that shrink what bacteria do to helping with chemistry you already
run, or that read several million genes as one bacterium being cleverer than
one of your cells rather than as a community carrying reactions you have no
genes for.

Two further errors the lesson exists to correct are worked as well: that an
antibiotic can pick out the harmful species, and that fibre "passes straight
through and does nothing" — the second joined to job 5, because the fatty
acids released by fermenting fibre are the same fatty acids that feed the
cells lining the large intestine.

No question restates a ladder rung. The rungs already own what bacteria can do
that your cells cannot, the C. difficile competition case, the germ-free
mouse's food and infection, and the cow. So the bank works around all four:
the mouse appears only through its gut wall and through a matched-growth
comparison the lesson does not run, C. difficile appears only as the faecal
transplant from the stretch layer, and no question mentions a cow.

`figure` is `None` throughout — the lesson declares no figures, and NOTES-B3's
two B3 figure slots belong to other lessons. Every stem is self-contained.
"""

UNIT = "B3"
LESSON = "bacteria-in-the-gut"
LESSON_NUMBER = 8

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-08-e01",
        "band": "easier",
        "text": "Newborn babies are given a vitamin K injection at birth. "
                "What reason does this lesson give?",
        "options": [
            {"text": "Newborn milk does not contain any vitamin K, so it "
                     "must be injected.", "correct": False,
             "why": "The lesson does not blame the milk. Vitamin K is made "
                    "inside you, by bacteria in the large intestine — and a "
                    "newborn has not got that community yet."},
            {"text": "They have almost no gut bacteria yet, and bacteria are "
                     "what make vitamin K.", "correct": True},
            {"text": "Their liver is still too immature to make any vitamin K "
                     "of its own.", "correct": False,
             "why": "Your own organs never make vitamin K, at any age. It is "
                    "made by gut bacteria as a by-product of their metabolism, "
                    "and you absorb it."},
            {"text": "The injection kills any harmful bacteria a newborn "
                     "picks up at birth.", "correct": False,
             "why": "That is an antibiotic, not a vitamin — and it is the "
                    "germ reflex again. The injection replaces something "
                    "missing bacteria would have made."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-e02",
        "band": "easier",
        "text": "Gut bacteria ferment the fibre your own enzymes cannot "
                "digest. What happens to the fatty acids they release?",
        "options": [
            {"text": "You absorb them through the large intestine wall and "
                     "your cells use them.", "correct": True},
            {"text": "They leave the body in the waste; you cannot use them "
                     "at all.", "correct": False,
             "why": "Then fibre would be worth nothing to you. Up to about a "
                    "tenth of the energy some people get from food arrives "
                    "this way, absorbed through the large intestine wall."},
            {"text": "The bacteria keep them all — they are the bacteria's "
                     "own food.", "correct": False,
             "why": "The deal runs both ways. The fatty acids are released "
                    "into your gut, absorbed by you, and they also feed the "
                    "cells lining the wall."},
            {"text": "They are absorbed in the stomach, before the food "
                     "reaches the bacteria.", "correct": False,
             "why": "Nothing can be absorbed before it is made. The bacteria "
                    "are in the large intestine, so the fatty acids only "
                    "exist once the food has got that far."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-e03",
        "band": "easier",
        "text": "Which of these decides whether a bacterium in your body is "
                "helpful or harmful?",
        "options": [
            {"text": "The species alone — some bacteria are germs and all the "
                     "rest are harmless.", "correct": False,
             "why": "Species is part of it, but not on its own. E. coli is a "
                    "harmless resident of almost every large intestine and "
                    "the same species in your blood can kill you."},
            {"text": "Whether it is inside you at all: bacteria in the body "
                     "mean illness.", "correct": False,
             "why": "You are carrying about thirty trillion right now and you "
                    "are not ill. Most gut bacteria are helpful, and your "
                    "immune system leaves them alone on purpose."},
            {"text": "Where it is and how many there are, more than which "
                     "species it is.", "correct": True},
            {"text": "Whether your immune system has met that species "
                     "before or not.", "correct": False,
             "why": "Your immune system has met your gut bacteria — that is "
                    "how it learned to leave them alone. What turns one "
                    "dangerous is moving to the wrong place."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-e04",
        "band": "easier",
        "text": "Antibiotics are given for an infection somewhere else in "
                "the body. Why does the gut community get hit as well?",
        "options": [
            {"text": "The antibiotic is swallowed, so it only ever acts "
                     "inside the gut.", "correct": False,
             "why": "It is absorbed and carried in the blood, which is how it "
                    "reaches a chest or a throat. Passing through the gut is "
                    "not the point — reaching everywhere is."},
            {"text": "Antibiotics deliberately target gut bacteria first, "
                     "then move to the infection.", "correct": False,
             "why": "Nothing is being aimed. The drug simply acts on bacteria "
                    "wherever it finds them, and your large intestine is "
                    "where most of them are."},
            {"text": "An antibiotic cannot tell a useful species from a "
                     "harmful one, so it kills both.", "correct": True},
            {"text": "They do not — the gut community is protected behind its "
                     "own thick mucus layer.", "correct": False,
             "why": "If the gut community were protected, a course of "
                    "antibiotics could not be followed by an infection that "
                    "moves into the space it cleared."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-08-s01",
        "band": "standard",
        "text": "You switch off Job 3, occupying the space, and leave the "
                "other four jobs running. What should you expect?",
        "options": [
            {"text": "A share of the energy in your food leaves the body "
                     "undigested.", "correct": False,
             "why": "That is Job 1 switched off, not Job 3. Fermenting fibre "
                    "is still running here, so that energy is still being "
                    "released and absorbed."},
            {"text": "Your blood clots poorly, because vitamin K is no "
                     "longer being made.", "correct": False,
             "why": "That is Job 2. The vitamin makers are still working in "
                    "this version — it is the competition for space that has "
                    "gone."},
            {"text": "The lining of your large intestine becomes thin and "
                     "poorly developed over time.", "correct": False,
             "why": "That is Job 5. The wall is still being fed and signalled "
                    "here; what is missing is anything occupying the space a "
                    "newcomer would want."},
            {"text": "A harmful species that arrives finds free space and "
                     "food waiting for it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-s02",
        "band": "standard",
        "text": "The germ-free mouse has a thin, poorly developed gut wall. "
                "Why does having no bacteria do that?",
        "options": [
            {"text": "Its lining cells have lost their preferred fuel, the "
                     "fatty acids from bacteria.", "correct": True},
            {"text": "The extra food it eats scrapes the lining away as it "
                     "passes through.", "correct": False,
             "why": "Food does not sand the gut down. The mouse eats more "
                    "because energy from fibre is lost; the wall is thin "
                    "because its cells are unfed and unsignalled."},
            {"text": "Bacteria normally line the wall in a layer, and that "
                     "layer is much of its thickness.", "correct": False,
             "why": "The thickness is the wall's own cells, not a layer of "
                    "bacteria sitting on it. Bacteria feed and signal those "
                    "cells; they are not the wall."},
            {"text": "Sterile food contains no fibre, so nothing presses "
                     "against the wall.", "correct": False,
             "why": "Sterile means no bacteria, not no fibre. And fibre does "
                    "not build the wall by pressing on it — it is fermented, "
                    "and the products feed the lining cells."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-s03",
        "band": "standard",
        "text": "A student writes: “Gut bacteria are parasites — "
                "they take our food and give nothing back.” What is the "
                "best correction?",
        "options": [
            {"text": "They are not parasites, because they take nothing from "
                     "you in the first place.", "correct": False,
             "why": "They do take. A steady food supply, a constant 37 °C "
                    "and no immune attack are real costs to you. The error is "
                    "“give nothing back”, not “take”."},
            {"text": "They are parasites, but harmless ones, because your "
                     "immune system keeps them controlled.", "correct": False,
             "why": "Your immune system is not fighting a holding action — it "
                    "knows they are there and leaves them alone. That is the "
                    "arrangement, not a stalemate."},
            {"text": "They are paid in warmth, food and shelter, and they "
                     "pay in chemistry you lack.", "correct": True},
            {"text": "They are only parasites when too many of them build up "
                     "in the large intestine.", "correct": False,
             "why": "Abundance and place do decide when a species turns "
                    "harmful, but a normal gut community is not a parasite at "
                    "any size. Both sides are getting something."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-s04",
        "band": "standard",
        "text": "Your own cells carry about twenty thousand genes; your gut "
                "bacteria together carry several million. What does the "
                "lesson conclude from that?",
        "options": [
            {"text": "They help your own cells carry out your own chemical "
                     "reactions faster.", "correct": False,
             "why": "Not helping with your chemistry — running chemistry "
                    "you do not have. No human cell can break down cellulose "
                    "or make vitamin K at any speed."},
            {"text": "They run chemical reactions your own cells have no "
                     "genes for at all.", "correct": True},
            {"text": "One bacterium is therefore more complicated than one "
                     "of your body cells.", "correct": False,
             "why": "The several million is the whole community added up, not "
                    "one cell. The point is the range of chemistry the "
                    "community carries, not one cell beating one of yours."},
            {"text": "Most of those genes are copies of yours, which is why "
                     "they fit in.", "correct": False,
             "why": "The opposite is what matters. They carry enzymes your "
                    "genome does not code for, which is exactly why they can "
                    "do jobs you cannot."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-08-h01",
        "band": "harder",
        "text": "A patient's C. difficile infection comes back every time "
                "another course of antibiotics clears it. A faecal "
                "transplant cures it. Why does the transplant work where the "
                "antibiotics did not?",
        "options": [
            {"text": "The donor bacteria hunt down and kill C. difficile the "
                     "way a drug does.", "correct": False,
             "why": "They are not a weapon. They win by being there first — "
                    "taking the space and the food, which is the one thing "
                    "another antibiotic cannot do."},
            {"text": "The donor's immunity to C. difficile is carried across "
                     "with the bacteria.", "correct": False,
             "why": "Immunity is not what is being transplanted. A community "
                    "of competitors is, and it works by occupying the "
                    "vacancy."},
            {"text": "Each course of antibiotics had been making C. "
                     "difficile itself steadily stronger.", "correct": False,
             "why": "Nothing improved the organism. Each course cleared its "
                    "competitors again and handed it the empty gut back — "
                    "which is why repeating the drug keeps failing."},
            {"text": "It refills the empty space with competitors, so there "
                     "is nowhere left to reoccupy.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-h02",
        "band": "harder",
        "text": "Two groups of germ-free mice. Group A is given a full gut "
                "community at birth. Group B stays germ-free but is fed "
                "extra food, so both grow at the same rate. Both are then "
                "exposed to a harmful bacterium. What would you predict?",
        "options": [
            {"text": "Both are equally at risk now, because they are the "
                     "same size and weight.", "correct": False,
             "why": "Extra food replaces one job — the energy from "
                    "fibre. Group B still has no competitors in the gut, an "
                    "untrained immune system and a thin wall."},
            {"text": "Group B is far more likely to fall seriously ill, "
                     "despite matching Group A's growth.", "correct": True},
            {"text": "Group B is safer, because a harmful species has no gut "
                     "bacteria to feed on.", "correct": False,
             "why": "An arriving species does not eat the residents — it "
                    "competes with them. An empty gut is the easiest gut to "
                    "settle in, not the hardest."},
            {"text": "Group A is more at risk, because it is the group "
                     "carrying bacteria.", "correct": False,
             "why": "Carrying bacteria is not being ill. Group A's community "
                    "is what occupies the space, trains its immune system and "
                    "keeps its gut wall thick."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-h03",
        "band": "harder",
        "text": "A surgeon repairing a damaged intestine works hard to stop "
                "gut contents leaking into the abdomen — even though "
                "those same bacteria live in the patient harmlessly every "
                "day. Why the care?",
        "options": [
            {"text": "Those species are dangerous outside the large "
                     "intestine; place decides, not identity.", "correct": True},
            {"text": "The bacteria change into harmful species as soon as "
                     "they leave the gut.", "correct": False,
             "why": "Nothing about the bacterium changes. E. coli in the "
                    "large intestine and E. coli in the blood are the same "
                    "organism in two different places."},
            {"text": "Only the few harmful species would escape; the useful "
                     "ones are safe anywhere.", "correct": False,
             "why": "The useful ones are the danger here. A resident that "
                    "does five jobs for you in the large intestine causes "
                    "serious infection in tissue where it does not belong."},
            {"text": "The patient's immune system has never encountered any "
                     "of those bacteria before.", "correct": False,
             "why": "It has met them, and leaves them alone in the gut. The "
                    "problem is the same familiar organisms arriving "
                    "somewhere they were never meant to be."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-h04",
        "band": "harder",
        "text": "Two people take in the same amount of energy each day, but "
                "one eats almost no fibre. What would you expect in the "
                "low-fibre person's large intestine?",
        "options": [
            {"text": "No difference at all — fibre passes straight "
                     "through and does nothing.", "correct": False,
             "why": "It passes your enzymes, not your bacteria. Fermenting it "
                    "is what releases the fatty acids you absorb and your "
                    "lining cells burn."},
            {"text": "More bacteria, because there is more room once the "
                     "fibre is gone.", "correct": False,
             "why": "Fibre is the community's food, not something crowding it "
                    "out. Less fibre arriving means less to ferment, not more "
                    "space to grow in."},
            {"text": "Fewer fatty acids released, so the lining cells lose "
                     "their preferred fuel.", "correct": True},
            {"text": "More vitamin K, because the bacteria switch to making "
                     "vitamins instead.", "correct": False,
             "why": "There is no swap. Vitamins come out of the bacteria's "
                    "own metabolism, so starving them of fibre does not make "
                    "them produce more of anything."},
        ],
        "figure": None,
    },
]
