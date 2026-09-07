# -*- coding: utf-8 -*-
"""B5 lesson 08 — Seed dispersal: twelve questions (MRB-269).

The lesson is a classifying instrument with one argument underneath it: every
dispersal structure answers the same problem, and you read a specimen by the
structure in front of you rather than by the plant's name. The bank probes both
halves — the eight specimens' mechanisms (how a coconut husk works, what
actually empties a poppy capsule, where the energy in a gorse pod comes from),
the five methods' cost column, the key fact about competing with the parent,
and the stretch note's long tail.

The distractors are built from the lesson's three declared misconceptions.
REPRO-15 ("plants disperse their seeds so the species can spread to new
places") supplies the spreading option in s01 and the whole of h03, where the
fault a student has to find is the phrase "so that" rather than any error of
structure — two of h03's distractors are true statements that are not the
fault, which is what makes the discrimination worth asking for. REPRO-16
("fruit is food the plant provides for animals") supplies the birds-need-food
option in s02 and the husk-is-the-reward option in e02. REPRO-24 ("a seed with
no wing and no parachute cannot be dispersed by wind") is named almost verbatim
as h01's strongest distractor, put to an unfamiliar seed head rather than to
the poppy the student already met.

The rest come from the instrument's own errors of confusion: the gorse
mechanism offered for a poppy and the poppy mechanism for a coconut, buoyant
read as light, hooks read as expensive, and "cheap to build" offered as the
reason a wind-dispersed plant makes very large numbers when the real reason is
how many land somewhere useless.

No question restates a rung. Rung 1 owns the hooked-and-flesh-less fruit, rung
2 owns picking the wind-dispersed one out of four named specimens, rungs 3 and
4 own the written explanation and the red fleshy fruit. So the bank works
around all four: hooks are approached through the goosegrass-against-blackberry
trade-off rather than through identification, and REPRO-24 is put as an
unfamiliar specimen whose mechanism has to be explained, not as a choice
between four names.

`figure` is `None` throughout. The lesson's one figure, `b5-dispersal-specimens`,
is declared at `status: "needed"` and no artwork exists for it, so no question
leans on a plate a student cannot see.
"""

UNIT = "B5"
LESSON = "seed-dispersal"
LESSON_NUMBER = 8

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-08-e01",
        "band": "easier",
        "text": "What does dispersal mean?",
        "options": [
            {"text": "Pollen moving from an anther to a stigma",
             "correct": False,
             "why": "That is pollination, and it happens before a seed "
                    "exists. Dispersal moves the finished seed away from the "
                    "plant that made it."},
            {"text": "A seed beginning to grow into a young plant",
             "correct": False,
             "why": "That is germinating. Dispersal is the journey; "
                    "germinating is what happens afterwards, wherever the "
                    "seed has landed."},
            {"text": "The movement of seeds away from the plant that made "
                     "them",
             "correct": True},
            {"text": "The joining of a pollen nucleus with an egg cell "
                     "nucleus",
             "correct": False,
             "why": "That is fertilisation, which is what makes the seed in "
                    "the first place. Dispersal is what happens to that seed "
                    "next."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e02",
        "band": "easier",
        "text": "A coconut's husk is thick and fibrous, keeps water out, and "
                "is full of air spaces. What does that structure tell you?",
        "options": [
            {"text": "It floats and stays sealed, so the coconut is dispersed "
                     "by water",
             "correct": True},
            {"text": "The air spaces make it light, so it is dispersed by "
                     "wind",
             "correct": False,
             "why": "Buoyant is not the same as light. A coconut is far too "
                    "heavy for wind — wind dispersal needs a very light seed "
                    "with a parachute or a wing."},
            {"text": "The husk is the reward, so an animal eats it and "
                     "carries the seed",
             "correct": False,
             "why": "Nothing about a husk is edible. A fruit dispersed inside "
                    "an animal pays with sweet flesh; this one pays nothing, "
                    "and it is far too big to be carried."},
            {"text": "The husk dries and splits, flinging the seed clear of "
                     "the parent",
             "correct": False,
             "why": "That is a gorse pod. A coconut husk does not tear itself "
                    "open — staying sealed is exactly what keeps the salt "
                    "water out for months at sea."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e03",
        "band": "easier",
        "text": "A poppy capsule is a dry pepper-pot on a long thin stem, "
                "with small holes under the rim. What actually gets the seeds "
                "out of it?",
        "options": [
            {"text": "The capsule dries until it twists and tears itself open",
             "correct": False,
             "why": "That is a gorse pod, which splits with an audible crack. "
                    "A poppy capsule stays whole — its holes are already "
                    "open, waiting for something to shake it."},
            {"text": "A bird pecks the capsule apart to reach the seeds inside",
             "correct": False,
             "why": "There is nothing edible on a dry capsule. It offers no "
                    "reward at all, and it empties perfectly well with no "
                    "animal anywhere near it."},
            {"text": "The seeds are heavy enough to fall out through the "
                     "holes on their own",
             "correct": False,
             "why": "Then a poppy would empty on a still day and drop "
                    "everything underneath itself. The holes sit near the top "
                    "for that reason: seeds leave only while the capsule is "
                    "being moved."},
            {"text": "The stem sways in the wind and the seeds are shaken out "
                     "through the holes",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e04",
        "band": "easier",
        "text": "One of the five methods needs no wind, no water and no "
                "animal. Which is it, and what supplies the movement?",
        "options": [
            {"text": "Wind — the parachute of hairs lifts a light seed up off "
                     "the plant",
             "correct": False,
             "why": "Wind dispersal needs wind, which is the point here. And "
                    "hairs lift nothing: they slow the fall, so the wind has "
                    "longer to carry the seed sideways."},
            {"text": "Flung by the plant — a drying pod twists until the seam "
                     "tears open",
             "correct": True},
            {"text": "On an animal — the hooks spring open and throw the "
                     "fruit clear",
             "correct": False,
             "why": "Hooks do not spring. They catch and hold, and the fruit "
                    "goes nowhere at all until an animal brushes past — so "
                    "this method needs an animal."},
            {"text": "Inside an animal — the ripening flesh pushes the seed "
                     "out of the fruit",
             "correct": False,
             "why": "Nothing pushes the seed out. The flesh is the fee that "
                    "gets the whole fruit eaten, so this method needs an "
                    "animal too."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-08-s01",
        "band": "standard",
        "text": "A dandelion seed lands directly beneath the plant that made "
                "it and germinates there. What is the problem for that "
                "seedling?",
        "options": [
            {"text": "Nothing can germinate in the shade of the plant that "
                     "made it",
             "correct": False,
             "why": "It germinates perfectly well — that is why this is a "
                    "problem at all. It comes up, and then loses the contest "
                    "for light rather than never starting."},
            {"text": "The species will not be able to spread into any new "
                     "areas",
             "correct": False,
             "why": "Spreading is a consequence of dispersal, not the reason "
                    "for it. The immediate problem is much closer to home: "
                    "the seedling's own parent."},
            {"text": "Animals already feeding on the parent plant will find "
                     "the seedling and eat it too",
             "correct": False,
             "why": "Being eaten is not the problem dispersal structures "
                    "answer. The opponent here is the parent itself, not an "
                    "animal."},
            {"text": "It competes with an established plant for light, "
                     "water and minerals, and loses",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s02",
        "band": "standard",
        "text": "A blackberry is green, hard and sour for a fortnight, then "
                "turns black and sweet. Why does the change come when it "
                "does?",
        "options": [
            {"text": "Making sugar takes a fortnight, so the fruit sweetens "
                     "as soon as the plant can manage it",
             "correct": False,
             "why": "The plant could sweeten it sooner. It does not, because "
                    "an animal that ate the fruit early would carry off seeds "
                    "that were not finished and could not grow."},
            {"text": "The seeds inside are finished, and the colour change is "
                     "the signal",
             "correct": True},
            {"text": "The plant is providing ripe food for birds at the time "
                     "of year they need it",
             "correct": False,
             "why": "The flesh is a fee, not a gift. It buys the seed a "
                    "journey — the plant is paying an animal to be a courier, "
                    "not feeding it."},
            {"text": "The sour flesh keeps insects out until the seeds inside "
                     "have germinated",
             "correct": False,
             "why": "Seeds do not germinate inside the fruit. The green stage "
                    "protects seeds that are not ready; once they are, the "
                    "fruit starts advertising."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s03",
        "band": "standard",
        "text": "Wind-dispersed plants make very large numbers of seeds. What "
                "is the reason?",
        "options": [
            {"text": "Wind seeds are cheap to build, so a plant can afford to "
                     "make plenty of them",
             "correct": False,
             "why": "Cheapness is why it can, not why it must. The number is "
                    "a response to how many are wasted: almost every one "
                    "lands somewhere useless."},
            {"text": "The seeds are so light that more are needed to reach "
                     "the same total mass",
             "correct": False,
             "why": "Nothing about dispersal is counted in total mass. What "
                    "counts is how many seeds land somewhere they can grow, "
                    "and by wind very few do."},
            {"text": "Almost every wind-blown seed lands somewhere useless, "
                     "so very many are needed",
             "correct": True},
            {"text": "Wind seeds have no tough coat, so most are eaten before "
                     "they germinate",
             "correct": False,
             "why": "Landing badly is the wind method's weakness, not being "
                    "eaten. The very tough coat belongs to the seeds that "
                    "travel inside an animal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s04",
        "band": "standard",
        "text": "Goosegrass offers an animal nothing at all, and still gets "
                "carried. Set against a blackberry, what is the trade-off?",
        "options": [
            {"text": "Hooks cost far less than flesh, but nothing controls "
                     "where the animal goes",
             "correct": True},
            {"text": "Hooks are cheaper and more reliable too, because fur "
                     "holds a fruit better than a gut",
             "correct": False,
             "why": "Cheaper, yes; more reliable, no. A hooked fruit drops "
                    "wherever the animal happens to groom, while an eaten "
                    "seed travels a long way and is left with fertiliser."},
            {"text": "The two cost about the same, since building hooks uses "
                     "sugar the plant made itself",
             "correct": False,
             "why": "They are nowhere near the same. Hooks cost almost "
                    "nothing next to a fruit full of sugar — which is the "
                    "whole reason a freeloader like goosegrass works."},
            {"text": "Hooks are the expensive option, because the animal "
                     "throws the fruit away unused",
             "correct": False,
             "why": "Hooks are the cheap option. And nothing is wasted when "
                    "the animal grooms: that is exactly how the seed gets put "
                    "down somewhere new."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-08-h01",
        "band": "harder",
        "text": "An unfamiliar plant holds hundreds of dust-fine seeds in a "
                "dry head on a tall springy stem, with narrow slits just "
                "under its top. There is no wing, no parachute, no flesh and "
                "no hooks. How is it most likely dispersed?",
        "options": [
            {"text": "Flung by the plant — with no wing or parachute, the "
                     "head must throw its own seeds",
             "correct": False,
             "why": "Nothing here twists, dries or splits: the slits are "
                    "already open. A flung fruit tears itself apart, and this "
                    "head stays whole."},
            {"text": "By wind — the stem sways and the seeds are shaken out "
                     "through the slits",
             "correct": True},
            {"text": "Not by wind — a seed with no wing and no parachute "
                     "cannot be wind-dispersed",
             "correct": False,
             "why": "This is the one that catches people. A poppy has "
                    "neither and is still wind-dispersed: here the wind moves "
                    "the stem rather than the seed."},
            {"text": "By gravity — the seeds are small enough to drop out on "
                     "their own and scatter",
             "correct": False,
             "why": "Seeds that drop out on their own land under the parent, "
                    "which is the worst place for them. High slits on a long "
                    "stem mean the head empties only while something is "
                    "moving it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h02",
        "band": "harder",
        "text": "Fingerprinting adult trees and the seedlings around them "
                "shows most seeds land within a few metres, with a thin tail "
                "reaching hundreds of metres. Why does that small tail matter "
                "more than the average?",
        "options": [
            {"text": "It does not — most seedlings come from seeds near the "
                     "parent, so those matter most",
             "correct": False,
             "why": "Counting is not the same as mattering. Seeds near the "
                    "parent land where the species already is; only the rare "
                    "far ones put it somewhere new."},
            {"text": "The far seeds are the strongest ones, so they are the "
                     "seedlings that survive",
             "correct": False,
             "why": "Travelling far does not make a seed stronger. What the "
                    "tail does is arrive where the species is not, which is a "
                    "different kind of advantage."},
            {"text": "The tail is probably measurement error, so it is the "
                     "average that should be trusted",
             "correct": False,
             "why": "The tail is real: every one of those seedlings was "
                    "matched to a parent tree by its DNA. Rare is not the "
                    "same as doubtful."},
            {"text": "Those rare seeds reach a new wood, recolonise after a "
                     "fire and shift a species' range",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h03",
        "band": "harder",
        "text": "A student writes: 'The dandelion grew parachutes so that its "
                "seeds could travel further from the parent.' What is the "
                "fault in that sentence?",
        "options": [
            {"text": "'So that' claims a plan. Plants whose seeds travelled "
                     "further left more descendants",
             "correct": True},
            {"text": "There is no fault — parachutes are exactly what "
                     "dandelion seeds have",
             "correct": False,
             "why": "The structure is right and the reasoning is not. 'So "
                    "that' says the plant arranged its own hairs, and nothing "
                    "in a plant intends anything."},
            {"text": "A parachute slows the seed's fall rather than carrying "
                     "it along",
             "correct": False,
             "why": "True, and worth knowing — but it is not the fault here. "
                    "The sentence would still claim a plan with the mechanism "
                    "described perfectly."},
            {"text": "A dandelion 'seed' is really a single-seeded fruit, so "
                     "the sentence uses the wrong word",
             "correct": False,
             "why": "Also true, and the lesson says so — but a naming slip is "
                    "not the fault. Swap in 'fruit' and the sentence still "
                    "credits the plant with a purpose."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h04",
        "band": "harder",
        "text": "A plant on a forested river bank has corky, air-filled "
                "fruits with no flesh and no hooks. A botanist predicts you "
                "will not find it on a dry hilltop nearby. Is that a "
                "reasonable prediction?",
        "options": [
            {"text": "No — a corky fruit is light, so the wind will carry it "
                     "up the hill",
             "correct": False,
             "why": "Buoyant is not light. Wind dispersal needs a very light "
                    "seed with a parachute or a wing; a corky case is built "
                    "to float, and floating needs water."},
            {"text": "No — an animal will pick the fruit up and carry it "
                     "uphill anyway",
             "correct": False,
             "why": "Nothing would make it. No flesh means no reward, and no "
                    "hooks means nothing catches in fur — this fruit gives an "
                    "animal no reason to move it."},
            {"text": "Yes — a buoyant case only works where there is water to "
                     "carry it",
             "correct": True},
            {"text": "Yes — corky fruits cannot germinate in the dry soil on "
                     "a hilltop",
             "correct": False,
             "why": "The prediction is about how a seed arrives, not whether "
                    "it grows once there. Nothing in a husk decides what the "
                    "soil is like where it lands."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-08-e05",
        "band": "easier",
        "text": "A sycamore key is a hard seed at one end of a stiff papery "
                "blade. What does that blade make the key do as it falls?",
        "options": [
            {"text": "Float on the surface of water until it reaches a bank",
             "correct": False,
             "why": "A papery blade is not a buoyant case. Floating belongs "
                    "to fruits such as the coconut, with a thick fibrous "
                    "husk."},
            {"text": "Spin, so that it falls slowly and the wind has time to "
                     "carry it sideways", "correct": True},
            {"text": "Catch in the fur of any animal that brushes past it",
             "correct": False,
             "why": "Catching needs hooks, and a sycamore key has none. There "
                    "is nothing on it to hold on with."},
            {"text": "Drop straight down, so the seed lands clear of the "
                     "tree’s own canopy", "correct": False,
             "why": "Landing directly below the parent is the one outcome "
                    "every dispersal structure exists to avoid. The blade "
                    "slows the fall rather than hurrying it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e06",
        "band": "easier",
        "text": "In which method of seed dispersal does the plant pay with "
                "sugar it made itself?",
        "options": [
            {"text": "Wind, using a parachute of fine hairs", "correct": False,
             "why": "Hairs are built from ordinary plant material and cost "
                    "very little. What wind dispersal costs is the vast "
                    "number of seeds that land nowhere useful."},
            {"text": "On an animal, caught by hooks in its fur",
             "correct": False,
             "why": "Hooks are the cheapest method of all. No reward is "
                    "offered, and the animal gets nothing out of it."},
            {"text": "Flung by the plant itself, from a pod that dries and "
                     "splits", "correct": False,
             "why": "The energy for that comes from the pod drying in the "
                    "sun. Nothing is handed over to anybody."},
            {"text": "Inside an animal, in the flesh of a fruit it eats",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-08-s05",
        "band": "standard",
        "text": "A goosegrass fruit is a few millimetres across and a burdock "
                "burr is about two centimetres. Both work the same way. What "
                "is the principle they share?",
        "options": [
            {"text": "Stiff backward-facing hooks that catch in fur or wool, "
                     "with no reward offered", "correct": True},
            {"text": "A body light enough for the wind to lift and carry",
             "correct": False,
             "why": "Neither has a parachute or a wing, and neither is light "
                    "enough to be lifted. They travel by being carried, not "
                    "by drifting."},
            {"text": "Flesh sweet enough to be eaten, around a seed with a "
                     "very tough coat", "correct": False,
             "why": "Neither of them is edible. A fruit dispersed that way "
                    "pays with sugar; these two pay nothing at all."},
            {"text": "A waterproof case full of air spaces, so that they "
                     "float", "correct": False,
             "why": "That is the coconut’s solution, for a seed too heavy for "
                    "anything else to move. These two are carried on the "
                    "outside of an animal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s06",
        "band": "standard",
        "text": "A coconut is far too heavy for the wind to lift and far too "
                "big for an animal to carry off. Why does that same weight "
                "not rule out water as well?",
        "options": [
            {"text": "Coconuts are lighter than they look once the liquid "
                     "inside has been used up", "correct": False,
             "why": "That liquid is a store for the seedling and it is not "
                    "lost at sea. It is the husk, not a change in weight, "
                    "that makes this work."},
            {"text": "Sea water dissolves part of the husk, so the coconut "
                     "gets lighter as it drifts", "correct": False,
             "why": "The husk is waterproof, and keeping salt water out is a "
                    "large part of its job. It is not being worn away."},
            {"text": "The husk is buoyant and waterproof, so the sea carries "
                     "it and weight hardly matters", "correct": True},
            {"text": "The palm flings the coconut clear of the shore, and the "
                     "sea takes it from there", "correct": False,
             "why": "Flinging belongs to plants with a pod that dries and "
                    "splits. A coconut simply falls, and the tide does the "
                    "rest."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-08-h05",
        "band": "harder",
        "text": "A gorse pod flings its seeds a few metres, while a dandelion "
                "parachute can travel a kilometre. Why is the gorse method "
                "still worth having?",
        "options": [
            {"text": "The seeds land more accurately, in soil that the "
                     "plant has already tested for itself", "correct": False,
             "why": "A plant tests nothing and aims at nothing. A splitting "
                    "pod scatters seeds in whatever direction the seam gives "
                    "way."},
            {"text": "It needs no wind, no water and no animal — the plant "
                     "supplies the energy itself", "correct": True},
            {"text": "The seeds are heavier, so they germinate more reliably "
                     "once they land", "correct": False,
             "why": "Weight is not what decides whether a seed germinates, "
                    "and being flung does nothing for a seed after it has "
                    "landed."},
            {"text": "The pod goes on protecting the seeds after they have "
                     "been flung", "correct": False,
             "why": "The pod tears itself apart to release them and its two "
                    "halves stay behind on the plant. Nothing travels with "
                    "the seed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h06",
        "band": "harder",
        "text": "A poppy capsule releases its seeds only while something is "
                "shaking it. Why is that better for the plant than holes that "
                "simply let the seeds fall out?",
        "options": [
            {"text": "It keeps birds from reaching the seeds while they are "
                     "still inside the capsule on its stem", "correct": False,
             "why": "Small holes under the rim are no defence against a bird, "
                    "and the capsule is not built as armour. What the design "
                    "controls is when the seeds leave."},
            {"text": "It keeps rain out of the capsule, so the seeds cannot "
                     "germinate before they ever leave it", "correct": False,
             "why": "The holes are open either way. Shaking changes the "
                    "timing of release, not whether water can get in."},
            {"text": "The seeds leave on windy days, when they can be blown "
                     "along, and stay put on still ones", "correct": True},
            {"text": "It empties the capsule slowly, so the plant does not "
                     "run out of seeds too early in the season",
             "correct": False,
             "why": "The plant has no use for seeds it is still holding. "
                    "Spreading them out in time is worth nothing unless the "
                    "wind is there to move them."},
        ],
        "figure": None,
    },
]
