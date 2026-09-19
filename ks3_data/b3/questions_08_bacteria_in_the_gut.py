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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Six further rows, two per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-08-e05",
        "band": "easier",
        "text": "A human gut holds about thirty trillion bacteria. Where in "
                "the digestive system do they live?",
        "options": [
            {"text": "The stomach, because that is where a meal is churned "
                     "and held longest.", "correct": False,
             "why": "The stomach holds acid at about pH 2, which kills most "
                    "of the bacteria that arrive with a meal. Very few live "
                    "there."},
            {"text": "The large intestine, on the fibre and water left after "
                     "absorption.", "correct": True},
            {"text": "The small intestine, because that is where almost all "
                     "the nutrients are.", "correct": False,
             "why": "The nutrients are absorbed there and have gone by the "
                    "time material moves on. The community lives further "
                    "along, on the fibre nobody else can use."},
            {"text": "The mouth, because that is where food and air both come "
                     "in.", "correct": False,
             "why": "Bacteria do live in the mouth, but nothing like thirty "
                    "trillion of them. That community is in the large "
                    "intestine, fermenting fibre."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-e06",
        "band": "easier",
        "text": "What is cellulose, and why does it matter that gut bacteria "
                "can break it down?",
        "options": [
            {"text": "It is the sugar plants store, and bacteria release it "
                     "faster than your own enzymes do.", "correct": False,
             "why": "Cellulose is not a store of sugar. It is the tough "
                    "material plant cell walls are built from, and your own "
                    "enzymes cannot touch it at all."},
            {"text": "It is a vitamin that plants make, and bacteria are how "
                     "you take it in.", "correct": False,
             "why": "Cellulose is not a vitamin. The vitamins your gut "
                    "bacteria supply are vitamin K and several B vitamins."},
            {"text": "It is the material bacteria themselves are built from, "
                     "which is why they can digest it.", "correct": False,
             "why": "Cellulose is plant material. What matters is that your "
                    "own enzymes cannot break it and theirs can."},
            {"text": "It is what plant cell walls are built from, and your "
                     "own enzymes cannot break it.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-08-s05",
        "band": "standard",
        "text": "Why does a developing immune system need to meet harmless "
                "bacteria early on?",
        "options": [
            {"text": "That is how it learns what to attack and what to leave "
                     "alone.", "correct": True},
            {"text": "It needs practice at fighting something before it meets "
                     "a real threat.", "correct": False,
             "why": "The harmless species are not fought. They are what the "
                    "system learns to leave alone, and that half is the one "
                    "most people miss."},
            {"text": "Because bacteria supply the vitamins an immune system "
                     "is built out of.", "correct": False,
             "why": "Gut bacteria do make vitamin K and B vitamins, but that "
                    "is a separate job. This one is about calibration."},
            {"text": "Because a system that meets no bacteria attacks the gut "
                     "lining instead.", "correct": False,
             "why": "The germ-free mouse's immune system is underdeveloped "
                    "rather than turned on its own gut — slower against real "
                    "threats, readier to react to things that are not."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-s06",
        "band": "standard",
        "text": "Your immune system knows the gut bacteria are there and "
                "leaves them alone. Why is that not a failure of the immune "
                "system?",
        "options": [
            {"text": "Because they hide behind the mucus layer where the "
                     "immune system cannot reach them.", "correct": False,
             "why": "This is not a case of the system being unable to reach "
                    "them. It is that attacking them would cost you five jobs "
                    "you cannot do yourself."},
            {"text": "Because there are far too many of them for any immune "
                     "system to deal with.", "correct": False,
             "why": "Numbers are not the reason. Leaving them alone is the "
                    "arrangement, because they are running chemistry your own "
                    "cells have no genes for."},
            {"text": "They are doing five jobs your own cells cannot, so "
                     "attacking them would cost you.", "correct": True},
            {"text": "Because bacteria from the large intestine are harmless "
                     "wherever in the body they end up.", "correct": False,
             "why": "The same species in the blood can kill you. What makes a "
                    "bacterium dangerous is usually its location and "
                    "abundance, not its identity."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-08-h05",
        "band": "harder",
        "text": "Two patients are given the same broad-spectrum antibiotic. "
                "One develops a serious gut infection two weeks later and the "
                "other does not. What is the most likely difference between "
                "them?",
        "options": [
            {"text": "One was given a stronger dose, which made the harmful "
                     "species tougher than before.", "correct": False,
             "why": "An antibiotic does not improve the organism it fails to "
                    "kill. What changes is its situation — whether anything "
                    "is left competing with it."},
            {"text": "How much of each one's gut community survived, and so "
                     "how much space was left.", "correct": True},
            {"text": "One of them swallowed the harmful species afterwards "
                     "and the other did not.", "correct": False,
             "why": "The organism is usually already present in small numbers "
                    "and held in check by everything around it. Nothing has to "
                    "arrive from outside."},
            {"text": "One of them has an immune system that was never trained "
                     "by gut bacteria at all.", "correct": False,
             "why": "Both are patients with established communities, so both "
                    "were trained years ago. What the antibiotic changes is "
                    "space and competition."},
        ],
        "figure": None,
    },
    {
        "id": "b3-08-h06",
        "band": "harder",
        "text": "A study finds that children raised on farms, in daily contact "
                "with many harmless bacteria, have fewer allergies than "
                "children raised in very clean homes. Which of the five jobs "
                "does that point to?",
        "options": [
            {"text": "Fermenting fibre — farm children eat more plants, so "
                     "they get more energy from them.", "correct": False,
             "why": "The study is about contact with bacteria rather than "
                    "about diet, and extracting energy from fibre has nothing "
                    "to do with allergy."},
            {"text": "Making vitamins — vitamin K and the B vitamins protect "
                     "against allergic reactions.", "correct": False,
             "why": "Those vitamins are for clotting and for the body's own "
                    "chemistry. Neither has anything to do with an allergic "
                    "reaction."},
            {"text": "Occupying the space — harmless species crowd out "
                     "whatever it is that causes allergy.", "correct": False,
             "why": "An allergy is the immune system reacting to something "
                    "that is not a threat. There is no harmful species here "
                    "to be crowded out."},
            {"text": "Training the immune system — an untrained one reacts to "
                     "things that are not threats.", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ───────────────────────────────────────────
    # 24 further rows per band, e07-e30 / s07-s30 / h07-h30, appended at
    # bank_position 18+ so bank_position 0-17 (the twelve MRB-269 rows plus
    # the six MRB-335 top-up rows) remain untouched.

    {
        "id": 'b3-08-e07',
        "band": 'easier',
        "text": "What does it mean to say gut bacteria 'ferment' fibre?",
        "options": [
            {"text": 'They break it down without using any oxygen at all.', "correct": True},
            {"text": 'They store it inside themselves for later.', "correct": False,
             "why": 'Fermenting is a chemical breakdown, not storage. The products are released, not kept.'},
            {"text": 'They coat it in mucus to protect the gut wall.', "correct": False,
             "why": 'Fermenting means breaking a substance down, not coating it. Mucus protection is a separate matter.'},
            {"text": 'They pass it straight through unchanged.', "correct": False,
             "why": 'Passing through unchanged is the opposite of fermenting, which changes fibre into fatty acids.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e08',
        "band": 'easier',
        "text": "What is the 'microbiome' that this lesson describes?",
        "options": [
            {"text": 'A single powerful species of bacterium.', "correct": False,
             "why": 'A microbiome is a whole community, not one species. Thousands of species live together in the gut.'},
            {"text": 'The whole community of microorganisms living in one place.', "correct": True},
            {"text": 'A machine used in a lab to study bacteria under a microscope.', "correct": False,
             "why": 'That would be a microscope. A microbiome names a living community, not a piece of equipment.'},
            {"text": 'The lining tissue of the large intestine wall.', "correct": False,
             "why": 'The lining is body tissue. The microbiome is the bacteria living on and among that tissue.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e09',
        "band": 'easier',
        "text": "What does the word 'antibiotic' mean?",
        "options": [
            {"text": 'A food that feeds and strengthens gut bacteria.', "correct": False,
             "why": 'That describes fibre, which bacteria ferment. An antibiotic works against bacteria, not for them.'},
            {"text": 'A vitamin that is made by bacteria in the large intestine.', "correct": False,
             "why": 'Vitamin K and B vitamins are made by bacteria. An antibiotic is a medicine, not something bacteria produce.'},
            {"text": 'A medicine that kills bacteria or stops them multiplying.', "correct": True},
            {"text": 'A test used to count how many bacteria are present.', "correct": False,
             "why": 'Counting bacteria is a laboratory measurement. An antibiotic acts on bacteria, it does not count them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e10',
        "band": 'easier',
        "text": 'Besides vitamin K, what other vitamins does this lesson say gut bacteria make?',
        "options": [
            {"text": 'Vitamin C, which the gut community makes for you out of fibre.', "correct": False,
             "why": 'Vitamin C comes from food, mainly fruit and vegetables. This lesson names a different set of vitamins as bacterial products.'},
            {"text": 'Vitamin D.', "correct": False,
             "why": 'Vitamin D is mostly made in skin exposed to sunlight. Gut bacteria are credited with a different set of vitamins here.'},
            {"text": 'Vitamin A.', "correct": False,
             "why": 'Vitamin A comes from food such as liver and orange vegetables. It is not named as a bacterial product in this lesson.'},
            {"text": 'Several B vitamins.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e11',
        "band": 'easier',
        "text": 'Why do very few of the bacteria arriving with a meal survive in the stomach?',
        "options": [
            {"text": "The stomach's strong acid kills most of them.", "correct": True},
            {"text": 'The stomach is too cold for bacteria to grow in.', "correct": False,
             "why": 'The stomach sits at normal body temperature, which suits bacteria fine. Its strong acid is the barrier, not its temperature.'},
            {"text": 'The stomach has no water for bacteria to live in.', "correct": False,
             "why": 'The stomach holds plenty of liquid from food and digestive juices. Its acidity, not dryness, is what kills most arriving bacteria.'},
            {"text": 'Peristalsis moves food through too fast for bacteria to settle.', "correct": False,
             "why": "Speed of movement is not the barrier described here. The stomach's acid is strong enough to kill most bacteria outright."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e12',
        "band": 'easier',
        "text": "True or false: most of the bacteria living in a healthy person's gut are harmful.",
        "options": [
            {"text": 'True, harmful bacteria simply outnumber the helpful ones.', "correct": False,
             "why": 'The opposite is the case. A healthy gut community is mostly made up of helpful species.'},
            {"text": 'False, most gut bacteria are helpful.', "correct": True},
            {"text": 'True, but the immune system destroys them before they cause damage.', "correct": False,
             "why": 'The immune system leaves the resident bacteria alone rather than destroying them, because most of that community is helpful, not harmful.'},
            {"text": 'False, because a healthy gut actually contains no bacteria at all.', "correct": False,
             "why": 'A healthy gut holds trillions of bacteria. The point is that most of that huge population is helpful, not that none are present.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e13',
        "band": 'easier',
        "text": 'Four of these are among the five jobs this lesson gives to gut bacteria. Which one is not?',
        "options": [
            {"text": 'Fermenting fibre for extra energy.', "correct": False,
             "why": 'That is Job 1, one of the genuine five.'},
            {"text": 'Making vitamin K and some B vitamins.', "correct": False,
             "why": 'That is Job 2, one of the genuine five.'},
            {"text": 'Digesting the protein in a meal.', "correct": True},
            {"text": 'Training the developing immune system.', "correct": False,
             "why": 'That is Job 4, one of the genuine five.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e14',
        "band": 'easier',
        "text": "E. coli lives harmlessly in almost every human's large intestine. Where could that same species become dangerous?",
        "options": [
            {"text": 'Nowhere, since a harmless species stays harmless wherever it goes.', "correct": False,
             "why": "This lesson's whole point is that place changes the risk. The same organism can be dangerous somewhere else in the body."},
            {"text": 'Deeper inside the same large intestine.', "correct": False,
             "why": 'The large intestine is exactly where this species belongs and does no harm. The danger appears once it leaves that organ.'},
            {"text": 'Nowhere, since it would simply die outside the gut.', "correct": False,
             "why": 'The species can survive and cause serious infection elsewhere in the body, in the bloodstream for example.'},
            {"text": 'In the bloodstream.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e15',
        "band": 'easier',
        "text": 'Which cells are fed by the fatty acids released when gut bacteria ferment fibre?',
        "options": [
            {"text": 'The cells lining the large intestine.', "correct": True},
            {"text": 'The red blood cells carrying oxygen.', "correct": False,
             "why": 'Red blood cells are fed by glucose from digestion, not by these fatty acids. The lining cells are the ones described here.'},
            {"text": 'The muscle cells of the stomach wall.', "correct": False,
             "why": "The stomach wall's muscle is not where this lesson places the fatty acids. They feed the large intestine's own lining."},
            {"text": 'The cells of the immune system alone.', "correct": False,
             "why": 'Immune cells are trained by contact with bacteria, which is a separate job from being fuelled by these fatty acids.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e16',
        "band": 'easier',
        "text": 'Roughly how many bacteria does a human gut hold, according to this lesson?',
        "options": [
            {"text": 'About thirty thousand.', "correct": False,
             "why": 'Thirty thousand is far too small. The gut community is described in the trillions, not the thousands.'},
            {"text": 'About thirty trillion.', "correct": True},
            {"text": 'About thirty million.', "correct": False,
             "why": 'Thirty million is still far short of the figure this lesson gives, which is measured in trillions.'},
            {"text": 'About thirty.', "correct": False,
             "why": 'A gut community of only thirty bacteria would be no community at all. The real figure is trillions.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e17',
        "band": 'easier',
        "text": 'In simple terms, what is a faecal microbiota transplant?',
        "options": [
            {"text": 'A course of antibiotics designed to remove every bacterium from the gut.', "correct": False,
             "why": 'That describes clearing bacteria out, the opposite of a transplant, which puts a fresh community back in.'},
            {"text": "A vaccine that trains a patient's own immune system to destroy one named harmful species and nothing else.", "correct": False,
             "why": 'A vaccine targets one threat directly. This treatment restores a whole competing community instead.'},
            {"text": "Bacteria from a healthy donor's gut given to a patient to restore their own community.", "correct": True},
            {"text": 'A supplement of vitamin K given after gut surgery.', "correct": False,
             "why": 'A vitamin supplement replaces one product. This treatment transfers a living bacterial community.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e18',
        "band": 'easier',
        "text": 'Roughly how do the numbers of genes compare: your own cells against your whole gut bacterial community?',
        "options": [
            {"text": 'About the same number on both sides.', "correct": False,
             "why": 'The two figures are wildly different, several million against twenty thousand, not roughly equal.'},
            {"text": 'Several million genes of yours against twenty thousand of theirs.', "correct": False,
             "why": 'That reverses the true comparison. The bacterial community carries the larger number of genes, by far.'},
            {"text": 'About twenty thousand on both sides.', "correct": False,
             "why": 'Twenty thousand describes your own genes only. The bacterial community together carries several million.'},
            {"text": 'About twenty thousand of yours against several million of theirs.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e19',
        "band": 'easier',
        "text": 'In return for the jobs gut bacteria do, what does this lesson say they get from you?',
        "options": [
            {"text": 'Warmth, a steady food supply, and no attack from your immune system.', "correct": True},
            {"text": 'Nothing at all, since the relationship runs one way and the bacteria simply take what they need.', "correct": False,
             "why": 'This lesson describes a two-way deal. Bacteria receive real benefits in exchange for the jobs they do.'},
            {"text": 'A share of the oxygen carried in your blood.', "correct": False,
             "why": 'Oxygen is not what this lesson describes bacteria receiving. Warmth, food and safety are the benefits named.'},
            {"text": 'New genes copied directly from your own cells.', "correct": False,
             "why": "Genes are not exchanged this way. The bacteria's reward is a stable, fed, protected place to live."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e20',
        "band": 'easier',
        "text": 'Which body system does this lesson say gets calibrated by early contact with harmless gut bacteria?',
        "options": [
            {"text": 'The digestive system.', "correct": False,
             "why": 'Digestion is affected by bacteria in other ways, such as fermenting fibre, but calibration here describes the immune system learning what to leave alone.'},
            {"text": 'The immune system.', "correct": True},
            {"text": 'The circulatory system.', "correct": False,
             "why": 'The circulatory system carries blood around the body. It is not the system described as being trained by bacterial contact.'},
            {"text": 'The skeletal system.', "correct": False,
             "why": 'Bones and the skeleton are not affected by early bacterial contact in the way this lesson describes the immune system being trained.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e21',
        "band": 'easier',
        "text": 'True or false: the same bacterial species can be helpful in one place and harmful in another.',
        "options": [
            {"text": 'False, a species is either always helpful or always harmful.', "correct": False,
             "why": "This lesson's key fact is the opposite: which bacteria are helpful depends on species AND on where they are."},
            {"text": 'False, only the amount present ever changes, not the danger.', "correct": False,
             "why": 'Both location and abundance can turn a species dangerous, not amount on its own with location fixed.'},
            {"text": 'True, place matters as much as species.', "correct": True},
            {"text": 'True, but only for bacteria living in the bloodstream.', "correct": False,
             "why": 'The idea applies generally, wherever a resident species ends up outside its usual home, not just the bloodstream.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e22',
        "band": 'easier',
        "text": 'A course of antibiotics clears most of the gut community. What does that leave behind, according to this lesson?',
        "options": [
            {"text": 'A stronger, better-defended gut community than before.', "correct": False,
             "why": 'Clearing the community removes its defence, occupying the space, rather than strengthening it.'},
            {"text": 'No noticeable change, since one antibiotic course is too brief to matter.', "correct": False,
             "why": 'A single course is described as being enough to clear enough competitors for an infection to take hold afterwards.'},
            {"text": 'A gut wall that is instantly thicker and better protected.', "correct": False,
             "why": 'Losing the bacterial community weakens the gut wall over time, since it loses its usual fuel and signals, rather than thickening it.'},
            {"text": 'Free space and food that a harmful species could move into.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e23',
        "band": 'easier',
        "text": 'What is cellulose part of, in the plants people eat?',
        "options": [
            {"text": "The plant's cell walls.", "correct": True},
            {"text": 'The sugar stored inside a fruit.', "correct": False,
             "why": 'Fruit sugar is a soft, soluble carbohydrate. Cellulose is the tough material of the cell wall.'},
            {"text": 'The oil found in seeds and nuts.', "correct": False,
             "why": 'Seed and nut oil is a fat, unrelated to cellulose, which forms the rigid wall around a plant cell.'},
            {"text": 'The green pigment in leaves.', "correct": False,
             "why": 'The green pigment is chlorophyll, involved in photosynthesis. Cellulose is a structural material, not a pigment.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e24',
        "band": 'easier',
        "text": 'Which of these decides how much credit a piece of writing about gut bacteria deserves in an exam: naming a job, or explaining the consequence of losing it?',
        "options": [
            {"text": 'Naming the job alone is always the fuller answer.', "correct": False,
             "why": 'A bare name says what happens, not why it matters. The strongest answer explains the consequence too.'},
            {"text": 'Naming the job AND explaining what its loss causes, together.', "correct": True},
            {"text": 'Neither matters, only the number of jobs listed counts.', "correct": False,
             "why": 'A long list of names with no explanation misses the reasoning a strong answer needs to show.'},
            {"text": 'Explaining a consequence alone, with no job named, is the fuller answer.', "correct": False,
             "why": 'A consequence with nothing named as its cause leaves out half the answer. Both parts are needed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e25',
        "band": 'easier',
        "text": 'What happens to a course of antibiotics once it reaches the bloodstream, that lets it also affect the gut?',
        "options": [
            {"text": 'It stays trapped inside the gut tube and never enters the bloodstream.', "correct": False,
             "why": 'An antibiotic absorbed into the blood is what reaches an infection elsewhere, such as a chest or a throat, and the gut on its way.'},
            {"text": 'It is broken down completely before leaving the stomach.', "correct": False,
             "why": 'If it broke down that quickly it could never treat an infection elsewhere in the body at all.'},
            {"text": 'It is carried in the blood to tissues all over the body, gut included.', "correct": True},
            {"text": 'It evaporates as a gas and is breathed out.', "correct": False,
             "why": 'A swallowed medicine does not turn into a gas. It is absorbed into the blood and carried around the body.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e26',
        "band": 'easier',
        "text": "Why doesn't a healthy immune system attack the resident gut bacteria it lives alongside every day?",
        "options": [
            {"text": 'The bacteria hide where the immune system cannot reach.', "correct": False,
             "why": 'The gut lining is well supplied with immune cells. The bacteria are recognised and tolerated, not hidden.'},
            {"text": 'The immune system is too weak to fight bacteria at all.', "correct": False,
             "why": 'The same immune system deals effectively with genuinely harmful invaders. It simply learns which bacteria are not a threat.'},
            {"text": 'The bacteria are not living organisms, so there is nothing to attack.', "correct": False,
             "why": 'Gut bacteria are living organisms. What matters is that the immune system has learned they are not a threat.'},
            {"text": 'It has learned to recognise them and leaves them alone.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e27',
        "band": 'easier',
        "text": "A doctor says a patient's diet is missing fibre entirely. Which of the five jobs is hit hardest by that, first?",
        "options": [
            {"text": 'Fermenting fibre for extra energy.', "correct": True},
            {"text": 'Training the developing immune system.', "correct": False,
             "why": 'Immune training comes mainly from early contact with bacteria, not directly from the fibre supply in a meal.'},
            {"text": 'Occupying space to keep harmful species out.', "correct": False,
             "why": 'Occupying space depends on bacterial numbers generally, not directly on how much fibre a diet supplies.'},
            {"text": 'Making vitamin K and some B vitamins.', "correct": False,
             "why": "Vitamin production continues from the bacteria's own metabolism. Fermenting fibre is the job that is hit first when fibre runs out."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e28',
        "band": 'easier',
        "text": 'What word describes a bacterium that has been shown to reliably cause disease?',
        "options": [
            {"text": 'Resident.', "correct": False,
             "why": 'Resident describes a bacterium that normally lives somewhere in or on the body, whether it is harmful or not.'},
            {"text": 'Harmful.', "correct": True},
            {"text": 'Fermenting.', "correct": False,
             "why": 'Fermenting describes what some bacteria do to fibre, a chemical process, not whether they cause disease.'},
            {"text": 'Microbial.', "correct": False,
             "why": 'Microbial simply means relating to microorganisms generally, and says nothing about whether one causes disease.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e29',
        "band": 'easier',
        "text": "Which of these best describes 'occupying the space' as a job gut bacteria do?",
        "options": [
            {"text": 'Physically blocking the whole gut tube, so that neither food nor any newcomer can pass along it at all.', "correct": False,
             "why": 'Occupying space is about competition for a niche, not about physically obstructing the passage of food.'},
            {"text": 'Filling the bloodstream so harmful bacteria cannot enter it.', "correct": False,
             "why": 'This job describes the gut community itself, not the bloodstream, which healthy gut bacteria do not normally occupy.'},
            {"text": 'Filling the gut with a settled community so a harmful species finds nowhere at all to establish itself.', "correct": True},
            {"text": 'Producing a gas that pushes newcomers back out of the body.', "correct": False,
             "why": 'No such gas mechanism is described here. Occupying the space means using up the room and food a newcomer would need.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-e30',
        "band": 'easier',
        "text": 'Which vitamin, made by gut bacteria, is needed for normal blood clotting?',
        "options": [
            {"text": 'Vitamin B12.', "correct": False,
             "why": 'B12 is one of the B vitamins bacteria make, but clotting is specifically linked to vitamin K in this lesson.'},
            {"text": 'Vitamin C.', "correct": False,
             "why": 'Vitamin C comes from food rather than gut bacteria, and this lesson does not link it to clotting.'},
            {"text": 'Vitamin D.', "correct": False,
             "why": 'Vitamin D is not named as a bacterial product here, and it is not the vitamin linked to blood clotting in this lesson.'},
            {"text": 'Vitamin K.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s07',
        "band": 'standard',
        "text": 'Imagine only Job 2, making vitamins, were switched off, with the other four jobs left running normally. What would you expect to see first?',
        "options": [
            {"text": 'Poor blood clotting, from a shortage of vitamin K.', "correct": True},
            {"text": 'A gut suddenly overrun by a harmful species, since nothing occupies the space any more.', "correct": False,
             "why": 'Occupying the space is Job 3, still running in this scenario. The gap left here is specifically in vitamin supply.'},
            {"text": 'A thin, poorly developed gut wall, from a shortage of fatty acids.', "correct": False,
             "why": 'Fatty acids come from fermenting fibre, Job 1, which is still running here. Losing vitamin production affects clotting, not the wall.'},
            {"text": 'A weaker, less well trained immune system, from a lack of early bacterial contact.', "correct": False,
             "why": 'Immune training, Job 4, is unaffected in this scenario. Only vitamin production has been switched off.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s08',
        "band": 'standard',
        "text": 'Why is leaving the resident gut bacteria alone not a failure of the immune system?',
        "options": [
            {"text": 'They hide behind the mucus layer where the immune system cannot reach them.', "correct": False,
             "why": 'This is not a case of the system being unable to reach them. Attacking them would cost five jobs the body cannot do itself.'},
            {"text": "They are doing jobs the body's own cells can never do, so attacking them would cost the body.", "correct": True},
            {"text": 'There are far too many of them for any immune system to deal with.', "correct": False,
             "why": "Numbers are not the reason. Leaving them alone is the arrangement, because they run chemistry the body's own cells cannot."},
            {"text": 'Bacteria from the large intestine stay harmless in any organ of the body they happen to reach next.', "correct": False,
             "why": 'The same species in the blood can cause serious illness. What makes a bacterium dangerous is usually location and abundance.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s09',
        "band": 'standard',
        "text": 'A student says gut bacteria are simply passengers, along for the ride with no real job to do. What is the best correction?',
        "options": [
            {"text": 'They are passengers, but harmless ones the body has simply got used to tolerating for no reason.', "correct": False,
             "why": 'Tolerance here has a reason, five jobs the body cannot do for itself. It is not a random tolerance with no cause.'},
            {"text": 'They are passengers only until the immune system eventually clears them out.', "correct": False,
             "why": 'A healthy immune system does not clear the resident community out. It learns to leave a helpful community alone, permanently.'},
            {"text": "They run chemistry the body's own genes can never run, from fermenting fibre to making vitamins.", "correct": True},
            {"text": 'They do have a job, but only inside a laboratory culture dish.', "correct": False,
             "why": 'The five jobs happen inside a living gut, not only in a lab dish. Fermenting fibre and making vitamins happen in the body.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s10',
        "band": 'standard',
        "text": 'A patient takes an antibiotic for a skin infection. Why might their gut community be affected too?',
        "options": [
            {"text": 'Skin bacteria and gut bacteria are, in every case, the same species living in two different places.', "correct": False,
             "why": 'Skin and gut communities are largely different species. The antibiotic reaches both because of where it travels, not because they are identical.'},
            {"text": 'The infection itself spreads down through the body until it reaches the gut.', "correct": False,
             "why": 'Nothing here describes the infection travelling. The antibiotic, carried in the blood, is what reaches the gut community.'},
            {"text": 'A skin infection always triggers a matching infection somewhere inside the gut.', "correct": False,
             "why": "One infection does not automatically cause a second one. The antibiotic's own journey through the blood explains the gut effect."},
            {"text": 'The antibiotic is absorbed into the blood and reaches bacteria all over the body, gut included.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s11',
        "band": 'standard',
        "text": 'Two patients take the same course of antibiotics. Only one develops a gut infection afterwards. What is the most likely explanation?',
        "options": [
            {"text": "How much of each patient's own gut community survived, and how much space was left behind.", "correct": True},
            {"text": "One patient's antibiotic dose was simply stronger than the other's.", "correct": False,
             "why": 'A stronger dose does not by itself explain who develops an infection. Surviving competition for space is the key difference described here.'},
            {"text": 'One patient swallowed a fresh harmful bacterium shortly after finishing treatment.', "correct": False,
             "why": 'The harmful organism is usually already present in small numbers, kept in check. Nothing has to arrive from outside.'},
            {"text": "One patient's immune system had gone without meeting any bacteria before this antibiotic course.", "correct": False,
             "why": 'Both patients are assumed to have had established communities, trained long before. What differs is how much of that community survived.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s12',
        "band": 'standard',
        "text": 'A person eats a normal amount of energy each day but very little fibre. What would you expect in their large intestine, compared with someone eating plenty of fibre?',
        "options": [
            {"text": 'No difference at all, since fibre passes straight through and is never used by anyone.', "correct": False,
             "why": 'Fibre is fermented by bacteria, not simply passed through unused. Less fibre means fewer fatty acids are released.'},
            {"text": 'Fewer fatty acids released, since less fibre is available to ferment.', "correct": True},
            {"text": 'More bacteria overall, since there is more spare room once the fibre supply drops.', "correct": False,
             "why": 'Fibre is food for the community, not something crowding it out. Less fibre arriving tends to mean less to ferment, not more room.'},
            {"text": 'More vitamin K produced, since the bacteria switch their metabolism towards making vitamins instead.', "correct": False,
             "why": 'There is no such swap described here. Starving the community of fibre does not make it produce more of anything else.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s13',
        "band": 'standard',
        "text": 'A newborn baby has almost no gut bacteria yet. Which two consequences follow most directly from that, according to this lesson?',
        "options": [
            {"text": 'Perfect digestion of every food type, and total protection from every possible infection.', "correct": False,
             "why": 'An absent bacterial community is described as a gap to be filled, not as an advantage giving perfect protection.'},
            {"text": 'A fully thickened gut wall, and complete immunity to all bacterial disease.', "correct": False,
             "why": 'A thickened wall and complete immunity both depend on jobs bacteria are described as doing, which a newborn has not yet gained.'},
            {"text": 'Little vitamin K production, and an immune system still waiting to be calibrated.', "correct": True},
            {"text": 'Excess vitamin K in the blood, and an over-sensitive immune system from birth.', "correct": False,
             "why": 'The described consequence of few bacteria is a shortage of vitamin K, not an excess, and an under-trained immune system, not an over-sensitive one.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s14',
        "band": 'standard',
        "text": 'A zoo keeper raises an animal in a completely sterile enclosure from birth. Based on the germ-free mouse, what would you predict about its gut wall over time?',
        "options": [
            {"text": "It would thicken faster than normal, since no bacteria compete for its cells' fuel.", "correct": False,
             "why": 'The lining cells lose their preferred fuel without bacteria, which weakens rather than thickens the wall over time.'},
            {"text": "It would stay exactly the same as a normal animal's, since diet alone controls wall thickness.", "correct": False,
             "why": "The germ-free mouse's thin wall shows that bacteria, not diet alone, are part of what maintains the wall."},
            {"text": 'It would develop extra folds to compensate for the missing bacterial community.', "correct": False,
             "why": 'No such compensating growth is described. The wall is expected to become thinner, not gain extra folding.'},
            {"text": "It would become thinner and less well developed than a normal animal's.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s15',
        "band": 'standard',
        "text": 'A doctor explains that a species living harmlessly in the gut can cause serious illness if it crosses into the bloodstream. What general rule does this illustrate?',
        "options": [
            {"text": "A bacterium's danger depends on where it is, not only on which species it is.", "correct": True},
            {"text": 'Every species becomes equally dangerous once it leaves the gut, without exception.', "correct": False,
             "why": 'Danger depends on the specific species and where it ends up, not on a blanket rule applying equally to every species.'},
            {"text": 'Bacteria in the blood are always weaker than bacteria in the gut, whatever the species.', "correct": False,
             "why": 'Strength is not the issue described. The organism itself does not change; what changes is whether it belongs in that location.'},
            {"text": 'Species identity is the only thing that ever decides whether a bacterium is dangerous.', "correct": False,
             "why": 'This example is chosen precisely to show identity is not the only factor. Location plays a decisive part too.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s16',
        "band": 'standard',
        "text": 'Why can an antibiotic not simply target the harmful species in an infection and leave the rest of the gut community untouched?',
        "options": [
            {"text": 'It is designed to protect useful species but sometimes fails to do so.', "correct": False,
             "why": 'No such protective design is described. An antibiotic is described as acting without regard to which species it meets.'},
            {"text": 'It acts on features common to many bacteria, so it can never tell a useful species from a harmful one.', "correct": True},
            {"text": 'Harmful species are always found mixed physically among the useful ones.', "correct": False,
             "why": "Physical mixing is not the reason given. The antibiotic's lack of selectivity between species is what causes the wider effect."},
            {"text": "The gut community actively shields the harmful species from the drug, since its members protect one another.", "correct": False,
             "why": 'The community does not protect a harmful invader from a drug. Both useful and harmful species are affected together.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s17',
        "band": 'standard',
        "text": 'A school project claims that gut bacteria are entirely separate from human health and simply live their own lives inside the gut. What is the best challenge to that claim?',
        "options": [
            {"text": 'They are separate, but only affect the gut wall and nothing beyond it.', "correct": False,
             "why": 'Effects reach beyond the wall itself, into vitamins absorbed into the blood and an immune system trained for the whole body.'},
            {"text": 'They are separate from health, but useful for medical research all the same.', "correct": False,
             "why": "Being useful for research does not answer the claim. The stronger challenge is that they genuinely affect the body's health directly."},
            {"text": 'They carry out five separate jobs that affect digestion, immunity and the gut wall directly.', "correct": True},
            {"text": 'They are separate from health until a person reaches old age, when their role first begins.', "correct": False,
             "why": 'No such age-based switch is described. The five jobs are described as ongoing throughout life, beginning near birth.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s18',
        "band": 'standard',
        "text": 'A study compares children raised around farm animals with children raised in very clean, low-germ homes. The farm children have fewer allergies. Which job does that point towards?',
        "options": [
            {"text": 'Fermenting fibre, since farm children likely eat more homegrown vegetables.', "correct": False,
             "why": 'This study is about bacterial contact, not diet. Fermenting fibre for energy has no clear link to allergy risk.'},
            {"text": 'Making vitamins, since farm bacteria might produce extra vitamin K for growing farm children.', "correct": False,
             "why": 'Vitamin K is linked to blood clotting, not allergic reactions. This study does not concern vitamin levels.'},
            {"text": 'Occupying space, since farm bacteria crowd out whatever substance triggers an allergy.', "correct": False,
             "why": 'An allergy is an overreaction by the immune system to a harmless substance, not a case of one species crowding another out.'},
            {"text": 'Training the immune system, since more contact with harmless bacteria means better calibration.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s19',
        "band": 'standard',
        "text": "A textbook claims 'bacteria only cause harm, never good, inside the human body.' Using this lesson, how would you correct that claim?",
        "options": [
            {"text": 'Most gut bacteria do useful jobs, and only a minority of species reliably cause disease.', "correct": True},
            {"text": 'The claim is correct, but only for bacteria living outside the large intestine.', "correct": False,
             "why": 'The claim is wrong generally, not just outside one organ. Most bacteria inside the large intestine itself are helpful.'},
            {"text": 'The claim is correct, since every bacterium becomes harmful once it multiplies enough.', "correct": False,
             "why": "Numbers alone do not turn a helpful species harmful in this lesson's account. Location and identity both play a part."},
            {"text": 'The claim is correct for children, but reverses completely once a person becomes an adult.', "correct": False,
             "why": "No age-based reversal like this is described. Most gut bacteria are helpful throughout a person's life."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s20',
        "band": 'standard',
        "text": "Why does the lesson describe the relationship between you and your gut bacteria as a 'deal' rather than simple tolerance?",
        "options": [
            {"text": 'Because bacteria pay rent in the form of extra body heat they generate for you.', "correct": False,
             "why": 'No such heat payment is described. The benefits named are chemical jobs, not warmth generated by the bacteria themselves.'},
            {"text": 'Because both sides genuinely benefit, rather than one side merely being allowed to stay.', "correct": True},
            {"text": "Because the word 'deal' simply sounds friendlier than the word 'tolerance' does.", "correct": False,
             "why": 'The word choice reflects a genuine two-way exchange of benefits, not just a friendlier way of saying the same thing.'},
            {"text": 'Because bacteria can legally be evicted if they fail to perform their side of the arrangement.', "correct": False,
             "why": "No eviction mechanism of this kind exists in the body. The mutual benefit itself is what earns the word 'deal'."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s21',
        "band": 'standard',
        "text": 'A patient with a healthy gut community and a patient whose community has just been wiped out by antibiotics are both exposed to the same harmful bacterium. What would you predict?',
        "options": [
            {"text": 'Both patients face an identical risk, since the harmful bacterium is the same in both cases.', "correct": False,
             "why": 'The surrounding community, present or wiped out, changes how easily that same bacterium can settle in and multiply.'},
            {"text": 'The patient with the healthy community is more at risk, since it already carries so many bacteria.', "correct": False,
             "why": 'A healthy, established community is what leaves a newcomer with nowhere to settle, lowering rather than raising the risk.'},
            {"text": 'The patient with the wiped-out community is far more likely to develop a serious infection.', "correct": True},
            {"text": 'Neither patient faces any risk, since a single exposure is never enough to cause an infection.', "correct": False,
             "why": 'A single exposure into an emptied community is exactly the situation described as risky in this lesson.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s22',
        "band": 'standard',
        "text": 'A student argues that the five jobs must all be equally important, since they are simply listed one after another. What is the best response?',
        "options": [
            {"text": 'The order does show importance, and Job 1 is always the most critical of the five.', "correct": False,
             "why": 'Nothing about list order signals ranking here. Each job addresses a different consequence, unrelated to its position in the list.'},
            {"text": 'The jobs cannot be compared at all, since they belong to entirely separate branches of science.', "correct": False,
             "why": 'All five are gut-bacteria jobs within the same lesson, comparable in principle, even if ranking them by importance is not straightforward.'},
            {"text": 'Only the last job listed matters, since a list usually builds towards its main point.', "correct": False,
             "why": 'No such build-up towards a final, most-important job is intended by this list. All five are presented as genuine functions.'},
            {"text": 'The order of a list never shows relative importance, and each job matters for a different reason.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s23',
        "band": 'standard',
        "text": 'Why might doctors be cautious about giving broad antibiotics to a patient who does not clearly need them?',
        "options": [
            {"text": 'Unnecessary use still disturbs a healthy community and its jobs, for no real benefit.', "correct": True},
            {"text": 'Antibiotics are dangerous only when given in extremely large doses over many years.', "correct": False,
             "why": 'The concern described here is disturbing a healthy community even at ordinary doses, not only at extreme long-term ones.'},
            {"text": "Antibiotics permanently destroy a patient's ability to ever regrow any gut bacteria at all.", "correct": False,
             "why": 'A community can recover over time. The concern is disruption and opportunity for a harmful species, not permanent, total loss.'},
            {"text": 'Antibiotics have no real effect on gut bacteria unless taken for a skin condition.', "correct": False,
             "why": 'An antibiotic reaches gut bacteria whatever infection it is treating, since it travels through the blood to tissues generally.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s24',
        "band": 'standard',
        "text": "A parent worries that letting a toddler play outside and get a little dirty will make them ill. How might this lesson's ideas about the immune system respond?",
        "options": [
            {"text": 'Any dirt at all guarantees a serious infection, regardless of what bacteria are present.', "correct": False,
             "why": 'This lesson links early contact with harmless bacteria to helpful calibration, not automatic serious illness.'},
            {"text": 'Some early contact with harmless bacteria may help the immune system learn what to leave alone.', "correct": True},
            {"text": 'Outdoor play has no connection whatsoever to how the immune system develops.', "correct": False,
             "why": 'Early bacterial contact is described as part of how an immune system learns, so outdoor exposure is not unconnected.'},
            {"text": 'Dirt itself supplies vitamin K directly through the skin, strengthening the child immediately.', "correct": False,
             "why": 'Vitamin K in this lesson comes from bacteria in the large intestine, not from dirt absorbed through the skin.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s25',
        "band": 'standard',
        "text": 'One chemical product released by fermentation links two of the five jobs together. What is that link?',
        "options": [
            {"text": 'The two jobs are unrelated, and no single molecule links them together at all.', "correct": False,
             "why": 'Fatty acids are the direct link described, released by fermentation and then used to fuel and signal the lining cells.'},
            {"text": 'Maintaining the wall happens first, and the repair work it involves is what then triggers the fermenting of fibre.', "correct": False,
             "why": "The order runs the other way, fermentation happens first and its products then feed the wall's maintenance."},
            {"text": "Fermenting fibre releases fatty acids that then become the preferred fuel of the wall's lining cells.", "correct": True},
            {"text": "Fermenting fibre produces vitamin K, which directly strengthens the gut wall's cells.", "correct": False,
             "why": "Vitamin K is linked to blood clotting, made as a separate job. Fatty acids, not vitamin K, are what fuel the wall's cells."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s26',
        "band": 'standard',
        "text": 'A researcher wants to test whether occupying space is really one of the five jobs. Which experiment would best test that specific job?',
        "options": [
            {"text": 'Measure how much vitamin K appears in the blood of two different animals.', "correct": False,
             "why": 'That experiment would test vitamin production, a different job, not whether space is being occupied at all.'},
            {"text": 'Compare how thick the gut wall grows in two animals fed very different daily amounts of fibre.', "correct": False,
             "why": 'That experiment targets fibre fermentation and wall maintenance together, not specifically the job of occupying space.'},
            {"text": 'Test how quickly two animals digest the same meal of protein and starch.', "correct": False,
             "why": "Digesting protein and starch is done by the animal's own enzymes, unrelated to whether bacteria are occupying space in the gut."},
            {"text": 'Compare how easily a harmful species settles in a gut with a full community versus an emptied one.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s27',
        "band": 'standard',
        "text": 'A patient recovering from severe malnutrition is started on food very slowly and carefully. Why might a long-starved gut community make sudden, large meals risky?',
        "options": [
            {"text": 'A community reduced by starvation may struggle to ferment a sudden large amount of fibre at once.', "correct": True},
            {"text": 'Large meals instantly destroy every remaining bacterium left in a starved gut.', "correct": False,
             "why": 'A sudden meal does not wipe the community out. The concern is the mismatch between a reduced community and a large, sudden food load.'},
            {"text": 'A starved gut community always doubles vitamin K output the moment food returns.', "correct": False,
             "why": 'No such automatic doubling of vitamin production is described. The risk lies in fermentation capacity, not vitamin output.'},
            {"text": 'Large meals cause the immune system to suddenly attack the returning gut bacteria as intruders.', "correct": False,
             "why": 'The immune system already recognises resident bacteria and does not treat their return as an intrusion.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s28',
        "band": 'standard',
        "text": "A vet explains that a young animal reared away from its mother and other animals often develops a weaker immune system. How does this lesson's idea of calibration help explain that?",
        "options": [
            {"text": "Isolation directly damages the animal's genes, producing a permanently smaller immune system.", "correct": False,
             "why": 'No genetic damage is described here. The concern is a lack of early bacterial contact needed for training, not gene damage.'},
            {"text": 'Less early contact with harmless bacteria may leave its immune system less well trained.', "correct": True},
            {"text": 'Isolated animals eat less fibre, which starves their immune cells directly of energy.', "correct": False,
             "why": 'Fibre fermentation fuels gut lining cells, not immune cells directly. The calibration idea concerns bacterial contact, not fibre intake.'},
            {"text": "An isolated animal's stomach acid becomes weaker, letting more bacteria through unchecked.", "correct": False,
             "why": 'Stomach acid strength is not linked to isolation here. The explanation offered is reduced early contact with harmless bacteria.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s29',
        "band": 'standard',
        "text": 'A student argues: "Any bacterium found in the large intestine must be one of the good ones, since that is where the good bacteria live." What is the flaw in this reasoning?',
        "options": [
            {"text": 'Location alone does not make a species good, a harmful newcomer could settle there too if space allowed it.', "correct": True},
            {"text": 'There is no flaw, since every species found in that particular organ has proved itself harmless simply by being there.', "correct": False,
             "why": 'Being present is not proof of being helpful. A harmful species could occupy that same space if the resident community were disturbed.'},
            {"text": 'The flaw is that no bacteria of any kind actually live in the large intestine at all.', "correct": False,
             "why": 'Trillions of bacteria live there, most of them helpful. The flaw is in the REASONING linking "there" to "good", not in the numbers.'},
            {"text": 'The flaw is that good bacteria only ever live in the small intestine, never the large one.', "correct": False,
             "why": 'The large intestine is exactly where this lesson places the main bacterial community. The error is the circular reasoning, not the location.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-s30',
        "band": 'standard',
        "text": 'An advert for a yoghurt drink claims its "probiotic" bacteria will permanently take up residence in a customer\'s gut for life. Using this lesson\'s ideas, what is the most likely problem with that claim?',
        "options": [
            {"text": 'An already-established community leaves little space or food for a small daily dose of newcomers to settle in permanently.', "correct": True},
            {"text": 'Yoghurt bacteria cannot survive stomach acid for even a single second, so none of them would ever reach the large intestine in any usable numbers.', "correct": False,
             "why": 'Some bacteria do survive the journey. The bigger issue is competing successfully against an established resident community afterwards.'},
            {"text": 'The gut has no room at all for any bacteria beyond the trillions already living there.', "correct": False,
             "why": 'Room is not fixed at exactly zero. The issue is that a small daily dose faces stiff competition, not that literally no space could ever open up.'},
            {"text": 'Probiotic bacteria are always harmful once they reach the large intestine.', "correct": False,
             "why": 'Nothing here suggests these bacteria are harmful. The problem is one of competing for a permanent place, not of doing harm.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h07',
        "band": 'harder',
        "text": "A researcher removes only Job 3, occupying the space, from a mouse's gut community, keeping the other four jobs fully running. A harmful bacterium is then introduced. What is the most likely outcome?",
        "options": [
            {"text": 'It settles in easily, since nothing is competing with it for room and food.', "correct": True},
            {"text": 'It fails to settle, since the immune system is still fully trained and blocks it outright.', "correct": False,
             "why": 'Immune training alone does not fill physical space. Without competition, the harmful species still finds room to establish itself.'},
            {"text": 'It fails to settle, since the gut wall is still thick enough to physically block it.', "correct": False,
             "why": "Wall thickness does not stop a bacterium from settling in the gut's contents. The missing competition is what leaves it an opening."},
            {"text": 'Nothing changes, since occupying space was never a genuine defence in the first place.', "correct": False,
             "why": 'Occupying space is one of the five real jobs described. Removing it specifically opens a gap for a newcomer.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h08',
        "band": 'harder',
        "text": 'A laboratory raises two germ-free mice. Group A is given bacteria that can ONLY ferment fibre, nothing else. Group B is given bacteria that can ONLY make vitamins, nothing else. Neither group ends up with a fully trained immune system or a fully thickened gut wall. What does this show about the five jobs?',
        "options": [
            {"text": 'Different jobs are carried out by different parts of a community, so a partial community only supplies the jobs its members can do.', "correct": True},
            {"text": 'It shows that fermenting fibre and making vitamins are, in truth, the only two jobs that genuinely matter to a growing mouse.', "correct": False,
             "why": 'The missing immune training and wall maintenance show those two jobs matter too. This result argues for all five, not just two.'},
            {"text": 'It shows the five jobs are entirely random and unconnected to which species happen to be present.', "correct": False,
             "why": 'The opposite is shown, which jobs appear depends directly on which species are present, which is far from random.'},
            {"text": 'It shows any single bacterium, given long enough, will eventually learn to perform every one of the five jobs by itself.', "correct": False,
             "why": 'Neither partial group develops the missing jobs over time in this scenario. The jobs stay tied to whichever species can perform them.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h09',
        "band": 'harder',
        "text": "A patient's recurring C. difficile infection returns each time another course of antibiotics clears it, but a faecal transplant finally cures it. Why does the transplant succeed where repeated antibiotics failed?",
        "options": [
            {"text": 'The donor bacteria hunt down and destroy C. difficile directly, the way a drug does.', "correct": False,
             "why": 'They are not acting as a weapon. They win by occupying the space first, which another antibiotic course cannot do.'},
            {"text": 'Each course of antibiotics had been quietly making C. difficile itself stronger.', "correct": False,
             "why": 'Nothing improves the organism between courses. Each course simply clears its competitors and hands the empty gut back to it.'},
            {"text": 'It refills the empty space with competing bacteria, leaving nowhere for it to reoccupy.', "correct": True},
            {"text": "The donor's own immunity to C. difficile is carried across along with the bacteria.", "correct": False,
             "why": 'Immunity is not what is transplanted here. A community of competitors is, and it works through occupying the vacancy.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h10',
        "band": 'harder',
        "text": "A hospital laboratory follows strict procedures to keep a patient's blood sample free of bacteria, even though the exact same species being excluded live harmlessly in every donor's gut. Why bother with such strict procedures?",
        "options": [
            {"text": 'The species itself changes into something more dangerous the instant it reaches blood.', "correct": False,
             "why": 'Nothing about the organism itself changes on entering blood. It is the same species behaving the same way, in a location it is not adapted to.'},
            {"text": 'A bacterium ordinarily harmless in the gut can cause serious illness once it reaches the bloodstream.', "correct": True},
            {"text": 'Only species that are already known to be harmful could possibly cause a problem this way.', "correct": False,
             "why": "This lesson's point is the reverse, ordinarily useful species can become dangerous once they are somewhere they do not belong."},
            {"text": 'Blood naturally kills every bacterium almost instantly, so contamination could never really matter.', "correct": False,
             "why": 'Blood does not kill bacteria instantly. If it did, there would be no reason for strict procedures against contamination in the first place.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h11',
        "band": 'harder',
        "text": 'A hospital wants to cut its C. difficile cases. One proposal is to isolate infected patients so the organism cannot spread between beds; another is to cut unnecessary antibiotic prescribing across the whole ward. Why would the second help even a patient who never meets an infected person?',
        "options": [
            {"text": 'Because the organism is often already present in small numbers, so the vacancy an antibiotic opens matters most.', "correct": True},
            {"text": 'Because isolating patients has been shown to make no difference to how an organism spreads between hospital beds.', "correct": False,
             "why": 'Isolation does reduce spread and is a sensible measure. The point is that it cannot help a patient whose own gut already holds the organism.'},
            {"text": 'Because antibiotics given on a ward are absorbed by every patient on it, not only the one prescribed them.', "correct": False,
             "why": 'A drug reaches only the patient who swallows it. What the second policy changes is how many patients have their own community cleared out.'},
            {"text": 'Because cutting prescribing makes the organism itself less able to survive inside a human gut at all.', "correct": False,
             "why": 'Nothing about the organism changes. What changes is how often a gut is left with the space and food it would need to multiply in.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h12',
        "band": 'harder',
        "text": 'Two people eat meals carrying the same energy figure on the label. One gets 30 g of fibre a day, the other 8 g. Suggest why the first is likely to take in slightly more energy than their label figure implies.',
        "options": [
            {"text": 'Fibre is broken down by their own enzymes, so a diet with more of it simply digests to more energy.', "correct": False,
             "why": 'No human enzyme can break fibre down at any point in the gut. The extra energy comes from bacteria fermenting it, not from your own digestion.'},
            {"text": 'Their bacteria ferment the extra fibre and release fatty acids the body absorbs, which a label does not count.', "correct": True},
            {"text": 'The extra fibre slows the meal down, giving their small intestine longer to absorb the nutrients that it holds.', "correct": False,
             "why": 'A slower journey does not create energy that was not there to begin with. The extra comes from fibre that bacteria ferment and the body absorbs.'},
            {"text": 'Fibre carries no energy at all, so in fact both people take in exactly what their own labels state.', "correct": False,
             "why": 'Fibre is not digestible by you, but it is fermentable by your bacteria, and the fatty acids they release are absorbed.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h13',
        "band": 'harder',
        "text": 'Four of the five jobs start again as soon as a gut community regrows after a course of antibiotics. Which one does not simply start again, and why?',
        "options": [
            {"text": 'Fermenting fibre, because fatty acids already lost cannot be replaced once that fibre has passed through.', "correct": False,
             "why": 'Fermentation restarts as soon as the bacteria are back and fibre arrives. Nothing about it depends on a window of time having been met.'},
            {"text": 'Making vitamins, because a gut can only ever learn to produce vitamin K once in a whole lifetime.', "correct": False,
             "why": 'Vitamin production resumes along with the community. It is a piece of ongoing chemistry, not something learned once and then fixed.'},
            {"text": 'Occupying the space, because a gap once opened in a gut community stays open from then onwards.', "correct": False,
             "why": 'The gap is exactly what closes as the community regrows, which is why the raised risk after antibiotics is a temporary one.'},
            {"text": 'Training the immune system, because it depends on contact during early development rather than on bacteria being here now.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h14',
        "band": 'harder',
        "text": 'A drug is developed that targets only one harmful species, leaving every other gut bacterium completely untouched. How would giving this drug differ from giving a normal broad-spectrum antibiotic?',
        "options": [
            {"text": 'It would still clear out the whole gut community, exactly the way a broad antibiotic does.', "correct": False,
             "why": 'A drug built to hit one specific species is described as sparing the rest, which is precisely why it differs from a broad antibiotic.'},
            {"text": 'It would behave identically to a broad antibiotic, since every antibiotic targets bacteria the same way.', "correct": False,
             "why": 'A broad antibiotic cannot distinguish between species at all, which is exactly the difference a narrow drug is built to fix.'},
            {"text": 'It would leave the harmful species completely unaffected while removing the useful bacteria instead.', "correct": False,
             "why": 'The drug is described as targeting the harmful species specifically, the reverse of leaving it untouched.'},
            {"text": "It would clear the threat without disturbing the community's other four jobs at the same time.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h15',
        "band": 'harder',
        "text": 'A microbiologist discovers a harmless gut species and a well-known harmful species share almost identical genes for surviving stomach acid. What does that suggest about what actually separates the two?',
        "options": [
            {"text": 'Surviving stomach acid is not what makes a species harmful, some other feature must decide that.', "correct": True},
            {"text": 'Sharing any gene at all means the two species must secretly be the same organism.', "correct": False,
             "why": 'Sharing one useful adaptation does not make two species identical. Many unrelated species can carry the same survival trick.'},
            {"text": 'The harmless species is therefore likely to turn harmful again very soon.', "correct": False,
             "why": 'Sharing a survival gene gives no reason to expect a change. Countless harmless species keep such genes permanently.'},
            {"text": 'Stomach acid survival must therefore be the single biggest cause of disease anywhere in the whole of the gut.', "correct": False,
             "why": 'Surviving the stomach only gets a species as far as the gut. It says nothing about whether it goes on to cause disease there.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h16',
        "band": 'harder',
        "text": "A study finds that people with a particular bowel disease have a far less varied gut community than healthy people do. A newspaper reports this as 'low gut variety causes bowel disease'. Evaluate the headline.",
        "options": [
            {"text": 'It is sound, since a study that finds two things together has established which of them came first.', "correct": False,
             "why": 'Finding two things together shows only that they go together. Which of them came first is a separate question this study has not answered.'},
            {"text": 'It overreaches: the study shows the two go together, but the disease could equally have reduced the variety.', "correct": True},
            {"text": 'It is wrong, because how varied a gut community is has no bearing on health in any circumstance.', "correct": False,
             "why": 'Variety does matter, since different species carry out different jobs. The flaw is the leap from going together to one causing the other.'},
            {"text": 'It is wrong, because only a bacterium already known to be harmful can ever be linked to a disease.', "correct": False,
             "why": "A community's make-up can be linked to health without any single harmful species being involved. The flaw is about cause, not about species."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h17',
        "band": 'harder',
        "text": "A pharmaceutical trial gives one group of patients a narrow-spectrum antibiotic and another group a broad-spectrum one, for the same infection. Both clear the infection equally well. Which group's gut community would you expect to recover faster afterwards?",
        "options": [
            {"text": 'The broad-spectrum group, since a bigger clear-out gives the community more room to regrow quickly.', "correct": False,
             "why": 'A bigger clear-out leaves more damage to repair, not a faster route back to a full, established community.'},
            {"text": 'Both groups recover at exactly the same rate, since curing the infection is what matters most.', "correct": False,
             "why": 'How much of the resident community survived the drug is what governs recovery speed, and that differs sharply between the two drugs.'},
            {"text": 'The narrow-spectrum group, since fewer of their resident bacteria were affected in the first place.', "correct": True},
            {"text": "Neither group's gut community is affected, since both drugs were aimed at a different infection entirely.", "correct": False,
             "why": 'Any antibiotic reaching the bloodstream also reaches the gut. A broad-spectrum drug simply affects more species there.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h18',
        "band": 'harder',
        "text": "A hospital reports that most bloodstream infections after bowel surgery are caused by species that were already living harmlessly in that same patient's gut. Why does this not show those bacteria were harmful all along?",
        "options": [
            {"text": 'It does show it, since only a species that was harmful all along could ever cause a bloodstream infection.', "correct": False,
             "why": 'A species that causes no trouble in the large intestine across a whole lifetime is not harmful there. What makes it dangerous is reaching somewhere else.'},
            {"text": 'The bacteria must have been changed into a genuinely more dangerous form by the surgery itself.', "correct": False,
             "why": 'Nothing about the organism changes. It is the same species doing the same things, in a place with no arrangement for tolerating it.'},
            {"text": 'The infections must really have come from bacteria on the surgical instruments rather than the patient.', "correct": False,
             "why": "The report names species already living in that patient's own gut, which is precisely what rules an outside source out."},
            {"text": 'Surgery gave resident species a route out of the gut, so what changed was the location, not the species.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h19',
        "band": 'harder',
        "text": 'A patient begins a broad-spectrum antibiotic course. Of the five jobs, which is lost almost at once, and which is not really lost at all?',
        "options": [
            {"text": 'Occupying the space goes as soon as the bacteria do; immune training was done in early life and stays.', "correct": True},
            {"text": 'Immune training goes first, since it is the job most sensitive to any change at all in the community.', "correct": False,
             "why": 'Immune calibration was carried out during early development. Losing the community now does not undo training that is already done.'},
            {"text": 'All five are lost at exactly the same moment, since every one of them depends on that same community.', "correct": False,
             "why": 'They depend on it in different ways. Occupying space needs bacteria present right now; immune training does not need them at all.'},
            {"text": 'None of the five is lost, since an antibiotic acts on the one species causing the infection treated.', "correct": False,
             "why": 'A broad-spectrum antibiotic cannot tell one species from another, so it clears useful residents along with whatever it was aimed at.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h20',
        "band": 'harder',
        "text": "Two ecosystems are compared: a rainforest with thousands of competing species, and a bare patch of ground with almost none. Using the 'ecosystem with vacancies' idea from this lesson, which is the easier place for one new, invasive species to establish itself?",
        "options": [
            {"text": 'The rainforest, since its huge variety of species makes it easier for one more to slip in unnoticed.', "correct": False,
             "why": 'A crowded community leaves less spare space and food, making it harder, not easier, for a newcomer to establish itself.'},
            {"text": 'The bare patch of ground, since there is little already there to compete against a newcomer.', "correct": True},
            {"text": 'Both are equally easy to invade, since species number has no bearing on how open a habitat is.', "correct": False,
             "why": "This lesson's whole argument, applied to the gut, is that an empty or reduced community leaves more open space than a full one."},
            {"text": 'Neither can be invaded, since a truly new species can never establish itself anywhere at all.', "correct": False,
             "why": "Invasions of new habitats do happen, and this lesson's gut examples, such as C. difficile, are built around exactly that."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h21',
        "band": 'harder',
        "text": 'A patient is warned that a course of antibiotics may leave them briefly more vulnerable to a gut infection even after the original illness is cured. Which single sentence best explains why the risk outlasts the treatment itself?',
        "options": [
            {"text": 'The antibiotic keeps working in the body for several weeks after the last dose is taken.', "correct": False,
             "why": 'The drug itself clears the body fairly quickly. The lasting risk comes from a community that has not yet regrown, not lingering drug.'},
            {"text": 'The harmful species only becomes dangerous once the antibiotic itself has fully left the gut.', "correct": False,
             "why": 'It is not waiting for the drug to leave; it is waiting for competing bacteria to return and take the space it could otherwise use.'},
            {"text": 'The gut community takes time to regrow, leaving a window where space and food remain available.', "correct": True},
            {"text": 'The immune system remains switched off for a period after any course of antibiotics.', "correct": False,
             "why": 'No such immune shutdown is described. The gap is in the bacterial community itself, not in immune function.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h22',
        "band": 'harder',
        "text": 'Comparing the five jobs, which pair most directly depends on the SAME chemical product being released by fermentation?',
        "options": [
            {"text": 'Making vitamins and training the immune system, linked by the vitamins released during fermentation.', "correct": False,
             "why": 'Vitamin production and immune training are described as running through different mechanisms, not a shared fermentation product.'},
            {"text": 'Occupying the space and making vitamins, linked by the fatty acids fermentation releases.', "correct": False,
             "why": 'Occupying space depends on numbers and competition, not on any specific chemical product released by fermentation.'},
            {"text": 'Training the immune system and occupying the space, linked by the fatty acids fermentation releases.', "correct": False,
             "why": 'Immune training comes from direct bacterial contact, and occupying space comes from sheer numbers, neither hinging on a fermentation product.'},
            {"text": 'Fermenting fibre and maintaining the gut wall, linked by the fatty acids fermentation releases.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h23',
        "band": 'harder',
        "text": "A student argues: 'Since gut bacteria carry several million genes and you carry only twenty thousand, one bacterium must be more complicated than one of your own cells.' What is wrong with that argument?",
        "options": [
            {"text": "The several-million figure is the whole community added together, not one single bacterium's own gene count.", "correct": True},
            {"text": 'The comparison is fair, and a single bacterium really is more complex than a human cell.', "correct": False,
             "why": 'A single bacterial cell has far fewer genes than a human cell. The several million belongs to the whole community together.'},
            {"text": 'Gene counts cannot be compared between two different kinds of organism under any circumstances.', "correct": False,
             "why": "Comparing gene counts across species is done routinely. The specific error here is treating a community total as one organism's count."},
            {"text": 'Human cells, in reality, carry more genes than bacteria do overall, so the argument has the numbers backwards.', "correct": False,
             "why": 'The figures themselves, twenty thousand against several million, are correct. The mistake is attributing the community total to a single cell.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h24',
        "band": 'harder',
        "text": 'A hospital ward reports that patients who receive unnecessary antibiotics for viral infections, which antibiotics cannot treat, still show a rise in gut infections afterwards. Why would this happen even though the drug never fights the virus itself?',
        "options": [
            {"text": 'Viral infections themselves damage the gut wall, independently of any antibiotic given.', "correct": False,
             "why": 'The pattern described tracks the antibiotic use, not the viral infection itself, which the drug cannot even treat.'},
            {"text": 'The antibiotic still acts on gut bacteria regardless of what kind of infection it was prescribed for.', "correct": True},
            {"text": 'Unnecessary antibiotics are always given at a higher dose than necessary ones.', "correct": False,
             "why": 'Dose size is not the mechanism described here. Any antibiotic reaching the blood affects gut bacteria regardless of the reason it was prescribed.'},
            {"text": 'The rise in gut infections is unrelated to the antibiotic and is simply a coincidence in the data.', "correct": False,
             "why": 'A drug that disturbs the gut community whatever infection it targets is a clear mechanism, not something to dismiss as coincidence.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h25',
        "band": 'harder',
        "text": "Explain why a species being 'resident' in the human gut does not, on its own, guarantee that it is harmless.",
        "options": [
            {"text": 'Resident species are harmless by definition, so the question describes a situation that cannot occur.', "correct": False,
             "why": 'This lesson gives cases, such as C. difficile after antibiotics, where a resident species does become harmful once conditions change.'},
            {"text": 'A resident species becomes harmful only once it has lived in the gut for several decades.', "correct": False,
             "why": 'No such time-based switch is described. What changes the risk is location and abundance, not years of residence.'},
            {"text": 'Residence describes where a species normally lives, while harm depends on whether it stays there and stays at a normal level.', "correct": True},
            {"text": 'Residence guarantees harmlessness everywhere in the body, not only inside the gut itself.', "correct": False,
             "why": "This lesson's examples show the opposite, a resident species can become dangerous once it leaves its usual location."},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h26',
        "band": 'harder',
        "text": "A biologist proposes deliberately introducing extra harmless bacteria into a patient's gut before a planned course of strong antibiotics, hoping to protect the community. Based on this lesson, what is the flaw in that plan?",
        "options": [
            {"text": 'Extra bacteria introduced this way would compete with the immune system rather than with harmful species.', "correct": False,
             "why": 'Competition here is described as being for space and food between bacterial species, not between bacteria and the immune system.'},
            {"text": 'Adding more bacteria before treatment would prevent the antibiotic from working on the original infection at all.', "correct": False,
             "why": "Nothing describes extra gut bacteria blocking an antibiotic's action on an unrelated infection elsewhere in the body."},
            {"text": 'The plan would work perfectly, since more bacteria always survive a course of antibiotics better than fewer do.', "correct": False,
             "why": 'An antibiotic cannot tell a useful species from a harmful one, so extra bacteria added beforehand would be cleared along with the rest.'},
            {"text": 'The extra bacteria would be affected by the same antibiotic just as much as the ones already there.', "correct": True},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h27',
        "band": 'harder',
        "text": "A patient is told their gut bacteria and their own cells have been in 'a mutual arrangement' since birth. Which piece of evidence from this lesson best supports describing it that way, rather than as one side simply tolerating the other?",
        "options": [
            {"text": "The body supplies warmth, food and safety, while bacteria supply chemistry the body's own genes can never perform.", "correct": True},
            {"text": "The body's immune system has never once detected the presence of resident gut bacteria.", "correct": False,
             "why": 'The immune system does detect them, it has simply learned not to attack them, which is different from never noticing them.'},
            {"text": 'Gut bacteria pay no cost to the body at all, so tolerating them costs nothing in return.', "correct": False,
             "why": "A steady food supply, constant warmth and no immune attack are real costs to the body, which is part of why calling it a 'deal' fits."},
            {"text": 'Bacteria could survive just as well outside the human body entirely, so the arrangement gives them nothing extra.', "correct": False,
             "why": 'The gut is described as an unusually good habitat for them, constant temperature, steady food and no attack, which is a real benefit to the bacteria.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h28',
        "band": 'harder',
        "text": "Two weeks after a course of antibiotics, a patient's gut holds as many bacteria as it did beforehand, yet they stay unusually prone to gut upsets for months. Suggest why a normal total count is not the same as a normal community.",
        "options": [
            {"text": 'The count must have been measured wrongly, since a full count is exactly what a full recovery means.', "correct": False,
             "why": 'A total count is a real measurement. What it cannot show is whether the same range of species has come back to do the same jobs.'},
            {"text": 'A count says nothing about which species returned, and a community of fewer kinds can leave jobs unfilled.', "correct": True},
            {"text": 'The antibiotic itself must still be present in the gut, months after the very last dose was taken.', "correct": False,
             "why": 'The drug clears from the body within days. What lingers is a community that has regrown in number but not yet in range.'},
            {"text": "The patient's immune system must have been permanently damaged by that course of treatment.", "correct": False,
             "why": 'Immune calibration happened in early life and is not undone by a course of antibiotics. The gap here is in the bacterial community.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h29',
        "band": 'harder',
        "text": "Compare two treatments for a resistant gut infection: Treatment A is a stronger, broader antibiotic; Treatment B is a faecal transplant. Which is more consistent with the 'ecosystem with vacancies' argument this lesson makes, and why?",
        "options": [
            {"text": 'Treatment A, because a stronger drug leaves less vacancy for the harmful species to reoccupy afterwards.', "correct": False,
             "why": 'A stronger antibiotic clears MORE of the community, leaving a bigger vacancy behind, not a smaller one.'},
            {"text": 'Both are equally consistent, since either treatment ultimately removes the harmful species from the gut.', "correct": False,
             "why": "Removing the harmful species is not the argument's point, refilling the vacancy with competitors is what a transplant does and a stronger drug does not."},
            {"text": 'Treatment B, because it refills the vacancy with competitors rather than simply clearing space again.', "correct": True},
            {"text": 'Neither fits the argument, since it concerns ecosystems outside the human body rather than gut treatments.', "correct": False,
             "why": 'This lesson applies the ecosystem-with-vacancies idea directly to the gut, using the faecal transplant as its own worked example.'},
        ],
        "figure": None,
    },
    {
        "id": 'b3-08-h30',
        "band": 'harder',
        "text": "A researcher wants to test whether gut bacteria really supply some of a person's vitamin K, rather than all of it arriving in food. Which comparison would test that specifically?",
        "options": [
            {"text": 'Two groups on identical diets, one of them given extra fibre, with blood vitamin K measured in both.', "correct": False,
             "why": 'That changes the fuel for fermentation rather than whether the bacteria are there, so it cannot separate a bacterial source from a dietary one.'},
            {"text": 'One group given an antibiotic and one group not, with both groups free to eat whatever they choose.', "correct": False,
             "why": 'Letting the diets differ leaves the vitamin K coming from food uncontrolled, so any difference could come from the plate rather than the bacteria.'},
            {"text": 'Two groups that both keep a normal gut community, one fed extra vitamin K and one of them not.', "correct": False,
             "why": 'Both groups keep their bacteria, so this tests the dietary supply alone and says nothing about whether the bacteria contribute any.'},
            {"text": 'Two groups on identical diets with the same vitamin K intake, one with a normal community and one germ-free.', "correct": True},
        ],
        "figure": None,
    },
]
