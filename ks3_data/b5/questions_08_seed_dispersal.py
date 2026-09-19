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

    # ── MRB-338 night 3 top-up ─────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "b5-08-e07",
        "band": "easier",
        "text": "What is the difference between dispersal and germination?",
        "options": [
            {"text": "Dispersal moves a seed away from its parent; germination "
                    "is the seed then beginning to grow into a young plant.", "correct": True},
            {"text": "Dispersal is simply the seed beginning to grow into a "
                    "young plant; germination is what carries it away from "
                    "its parent.", "correct": False,
             "why": "This has the two swapped round. Dispersal is the journey "
                    "away from the parent; germination is the growth that can "
                    "follow it."},
            {"text": "Both words describe exactly the same event, just at two "
                    "different points in a plant's life.", "correct": False,
             "why": "They are two clearly separate events, often separated by "
                    "a long wait. A dispersed seed can sit dormant for a long "
                    "time before it ever germinates."},
            {"text": "Dispersal happens inside the fruit; germination happens "
                    "only once the fruit has rotted away completely, however "
                    "many weeks that decomposition takes.", "correct": False,
             "why": "Dispersal is the seed's journey away from the parent, "
                    "wherever that ends up. Rotting fruit plays no necessary "
                    "part in either event."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e08",
        "band": "easier",
        "text": "A coconut carries a store of liquid sealed inside its shell, "
                "separate from the thick fibrous husk around it. What is that "
                "liquid actually for?",
        "options": [
            {"text": "It is what makes the whole husk buoyant enough to "
                    "float on the sea.", "correct": False,
             "why": "Buoyancy comes from the fibrous husk itself, trapping "
                    "air, not from the liquid held further inside the shell."},
            {"text": "It is seawater that has slowly seeped in during the "
                    "voyage.", "correct": False,
             "why": "The husk stays waterproof for the whole crossing. "
                    "Letting seawater in would ruin the very store this "
                    "question is asking about."},
            {"text": "It is a food store the young plant will use once it "
                    "starts to grow.", "correct": True},
            {"text": "It is a scent that draws a hungry animal in to eat the "
                    "whole fruit.", "correct": False,
             "why": "A coconut offers no reward to any animal at all — it "
                    "travels by floating, not by being eaten and carried."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e09",
        "band": "easier",
        "text": "A gorse pod dries out in hot sun until it suddenly splits with an "
                "audible crack. What supplies the energy that flings its seeds clear?",
        "options": [
            {"text": "A single gust of wind arriving at exactly the right "
                    "moment, just when the pod happens to be ready to open.", "correct": False,
             "why": "Nothing about this method depends on wind arriving. The "
                    "pod supplies its own energy by drying and twisting, "
                    "whatever the weather is doing."},
            {"text": "An animal brushing past and disturbing the pod enough to "
                    "trigger it.", "correct": False,
             "why": "No animal is needed to set this off. A gorse bank can be "
                    "heard crackling on a still, empty afternoon with nothing "
                    "moving near it."},
            {"text": "The pod's own drying and twisting, stored up as it dries "
                    "and released all at once.", "correct": True},
            {"text": "Rainwater gradually soaking into the pod over several "
                    "days and swelling it until the seam eventually gives "
                    "way.", "correct": False,
             "why": "It is drying out in hot sun that builds the tension, not "
                    "water soaking in. Wet weather would if anything delay "
                    "the pod splitting."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e10",
        "band": "easier",
        "text": "A blackberry is not built around one single seed. What is its "
                "actual structure?",
        "options": [
            {"text": "Many small segments clustered together, each holding "
                    "its own separate hard pip.", "correct": True},
            {"text": "A dry, pepper-pot-shaped capsule packed with hundreds "
                    "of tiny dust-fine seeds.", "correct": False,
             "why": "That describes a poppy capsule. A blackberry is soft "
                    "flesh in clustered segments, not a dry capsule of tiny "
                    "seeds."},
            {"text": "A thick, fibrous husk wrapped tightly around a "
                    "single very large seed inside.", "correct": False,
             "why": "That describes a coconut. A blackberry's segments are "
                    "soft and each one holds its own small pip, not one big "
                    "seed."},
            {"text": "A single stiff, papery wing fixed along one edge of "
                    "a hard seed at its side.", "correct": False,
             "why": "That describes a sycamore key. A blackberry has no "
                    "wing at all — it is made of several soft segments, "
                    "each with its own pip."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e11",
        "band": "easier",
        "text": "A burdock burr is a single round structure about two centimetres "
                "across. Structurally, what is it actually built from?",
        "options": [
            {"text": "One solid curved thorn, grown as a single continuous "
                    "piece.", "correct": False,
             "why": "A burdock burr is not one thorn. It is built from many "
                    "separate bracts, each ending in its own hook."},
            {"text": "Many stiff bracts, each ending in its own "
                    "backward-facing hook.", "correct": True},
            {"text": "A soft mat of fine hairs, similar to a dandelion's "
                    "parachute.", "correct": False,
             "why": "A burdock burr is stiff, not soft, and has nothing in "
                    "common with a dandelion's fine hairs — it is made of "
                    "many separate hooked bracts."},
            {"text": "A ring of small holes cut into hardened plant tissue.", "correct": False,
             "why": "That describes a poppy capsule. A burdock burr is built "
                    "from many stiff bracts, each tipped with a hook, not a "
                    "capsule with holes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e12",
        "band": "easier",
        "text": "A pair of goosegrass fruits measures 9 mm across in real life. "
                "Drawn at four times life size, how wide would that pair be?",
        "options": [
            {"text": "13 mm.", "correct": False,
             "why": "That adds the four instead of multiplying by it. Four "
                    "times life size means every measurement is multiplied "
                    "by four, so 9 mm becomes 36 mm."},
            {"text": "36 mm.", "correct": True},
            {"text": "2.25 mm.", "correct": False,
             "why": "That divides by four, which would be a drawing at a "
                    "quarter of life size. Magnifying makes the drawing "
                    "larger, so 9 mm becomes 36 mm."},
            {"text": "9 mm.", "correct": False,
             "why": "That is the real width, not the drawn one. The real "
                    "fruits stay 9 mm whatever the drawing does; at four "
                    "times life size the drawing is 36 mm."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e13",
        "band": "easier",
        "text": "Fingerprinting parent trees and their seedlings shows that most "
                "seedlings grow within a few metres of their parent. What method does "
                "this rely on?",
        "options": [
            {"text": "Watching seeds fall from the tree and timing how long "
                    "each one takes.", "correct": False,
             "why": "Nobody follows an individual falling seed. The distances "
                    "are worked out afterwards, by matching each seedling's "
                    "DNA back to a parent tree."},
            {"text": "Counting how many seeds a single tree produces in one "
                    "year.", "correct": False,
             "why": "A seed count on its own says nothing about how far any "
                    "of those seeds actually travelled. Genetic matching is "
                    "what measures the distance."},
            {"text": "Matching each seedling's genetic fingerprint to the "
                    "parent tree it must have come from.", "correct": True},
            {"text": "Measuring how heavy each species' seed is on average, "
                    "and using that figure alone to calculate its likely "
                    "dispersal range.", "correct": False,
             "why": "Weight alone cannot tell you where an actual seed "
                    "landed. The real distances come from matching seedlings "
                    "to parent trees by their DNA."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e14",
        "band": "easier",
        "text": "Most seeds from a parent tree land within a few metres of it, but a "
                "genuinely important few travel hundreds of metres. What is that rare "
                "long-distance group called?",
        "options": [
            {"text": "Measurement error, since real seeds could not travel "
                    "that far.", "correct": False,
             "why": "Every one of those distant seedlings has been matched to "
                    "its parent tree by DNA. It is a real, if rare, part of "
                    "the pattern, not an error in the measurement."},
            {"text": "The average distance a seed from that species travels.", "correct": False,
             "why": "The average is set mostly by the many seeds landing "
                    "close to the parent. The rare distant ones are a "
                    "separate, much smaller part of the pattern."},
            {"text": "Proof that the species is not really dispersed by wind "
                    "at all.", "correct": False,
             "why": "A long tail of rare, far-travelling seeds is exactly "
                    "what you would expect from a wind-dispersed species, not "
                    "evidence against it."},
            {"text": "The long tail of the distribution.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e15",
        "band": "easier",
        "text": "A dandelion parachute and a sycamore's spinning wing both slow a "
                "falling seed down. Why does slowing the fall matter for wind "
                "dispersal?",
        "options": [
            {"text": "It gives the wind longer to carry the seed sideways "
                    "before it reaches the ground.", "correct": True},
            {"text": "It lets the seed choose a good moment to land, rather "
                    "than falling straight away.", "correct": False,
             "why": "A seed makes no choices about when or where it lands. "
                    "Falling slowly simply gives the wind more time to act on "
                    "it, nothing more deliberate than that."},
            {"text": "It stops the seed from being damaged by hitting the "
                    "ground too hard.", "correct": False,
             "why": "Damage on landing is not what these structures are "
                    "solving. Their whole purpose is to extend the time the "
                    "wind has to carry the seed away."},
            {"text": "It allows the seed to keep growing bigger while it is "
                    "still falling.", "correct": False,
             "why": "A seed does not grow while falling through the air. "
                    "Slowing the fall is entirely about giving the wind time "
                    "to carry it further."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e16",
        "band": "easier",
        "text": "What is the identifying, visible structure that marks out a seed as "
                "likely to be wind-dispersed?",
        "options": [
            {"text": "Sweet, brightly coloured flesh wrapped around a hard "
                    "central seed.", "correct": False,
             "why": "That is the identifying structure for a seed dispersed "
                    "inside an animal, not one dispersed by wind. "
                    "Wind-dispersed seeds carry no reward at all."},
            {"text": "A parachute of fine hairs, a stiff wing, or a shaker "
                    "capsule on a long stem — and always a very light seed.", "correct": True},
            {"text": "Stiff backward-facing hooks, with nothing edible "
                    "anywhere on the fruit, built purely to catch onto a "
                    "passing animal's fur.", "correct": False,
             "why": "Hooks identify a seed carried on the outside of an "
                    "animal, not one relying on wind. A wind-dispersed seed "
                    "has neither hooks nor any reward."},
            {"text": "A thick, buoyant, waterproof case built around a very "
                    "heavy seed.", "correct": False,
             "why": "That structure identifies water dispersal. A "
                    "wind-dispersed seed is the opposite of heavy — it has to "
                    "be very light to be carried at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e17",
        "band": "easier",
        "text": "Besides carrying a seed away, what else does an animal typically "
                "leave behind at the spot where it drops it?",
        "options": [
            {"text": "A store of extra food, ready for the seedling to use "
                    "when it germinates.", "correct": False,
             "why": "A seed already carries its own food store, built before "
                    "it was ever eaten. What an animal adds is left in its "
                    "own droppings, not a second food store."},
            {"text": "A small heap of natural fertiliser, from its own "
                    "droppings.", "correct": True},
            {"text": "A protective hard shell, grown fresh around the seed "
                    "during digestion.", "correct": False,
             "why": "A seed's tough coat is built before dispersal even "
                    "begins, and nothing grows a new shell during a trip "
                    "through a gut."},
            {"text": "Nothing else is left behind, since digestion "
                    "supposedly leaves no trace.", "correct": False,
             "why": "Digestion does leave a trace: the animal's own "
                    "droppings, deposited in a heap right where the seed "
                    "lands."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e18",
        "band": "easier",
        "text": "Hooks and barbs are usually described as the cheapest of the five "
                "dispersal methods to build. What is the trade-off that comes with "
                "that low cost?",
        "options": [
            {"text": "Hooked seeds are heavier than seeds dispersed by any "
                    "other method.", "correct": False,
             "why": "Weight is not the particular trade-off here. Hooked "
                    "fruits can be very light — the cost is losing any "
                    "control over where the carrying animal takes them."},
            {"text": "Hooked fruits take far longer to develop on the plant "
                    "than other kinds.", "correct": False,
             "why": "Development time is not what is being traded off for the "
                    "low building cost. The real cost is having no say over "
                    "the animal's route or timing."},
            {"text": "Hooked seeds are far more likely to be eaten before they "
                    "can be carried anywhere.", "correct": False,
             "why": "Being eaten is not the particular risk here, since "
                    "hooked fruits usually offer nothing edible in the first "
                    "place. The trade-off is a total lack of control over the "
                    "journey."},
            {"text": "The plant has no control at all over where the animal "
                    "carrying the seed goes, or when it lets go.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e19",
        "band": "easier",
        "text": "What identifying feature marks out a fruit as very likely to be "
                "dispersed by water?",
        "options": [
            {"text": "A buoyant, waterproof case — fibrous, corky or full of "
                    "air spaces.", "correct": True},
            {"text": "A single asymmetric wing that makes the whole seed spin "
                    "as it falls.", "correct": False,
             "why": "A spinning wing identifies a wind-dispersed seed, such "
                    "as a sycamore key. Water dispersal instead needs a case "
                    "built to float."},
            {"text": "Sweet flesh around a seed with an unusually tough coat.", "correct": False,
             "why": "Sweet flesh identifies a seed dispersed inside an animal "
                    "that eats it. Water dispersal instead relies on a "
                    "buoyant, waterproof case."},
            {"text": "A dry pod that slowly twists as it dries and eventually "
                    "splits wide apart.", "correct": False,
             "why": "A twisting, splitting pod identifies a seed flung by the "
                    "plant itself. Water dispersal needs a case that floats, "
                    "not one that tears open."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e20",
        "band": "easier",
        "text": "Georges de Mestral examined burdock burrs stuck in his dog's fur "
                "under a microscope in 1941. What did that lead him to invent, over "
                "the following decade?",
        "options": [
            {"text": "The modern zip fastener.", "correct": False,
             "why": "The zip was already a well-established fastening long "
                    "before 1941. What de Mestral went on to invent, copying "
                    "the burr's hooks, was Velcro."},
            {"text": "Velcro.", "correct": True},
            {"text": "A new variety of burdock bred to have softer, less "
                    "irritating burrs.", "correct": False,
             "why": "He was not breeding plants at all. He was copying the "
                    "hooked structure he had found, mechanically, to invent "
                    "Velcro."},
            {"text": "A shampoo formulated specifically to remove burrs from "
                    "an animal's fur.", "correct": False,
             "why": "Nothing about his invention involved removing burrs from "
                    "fur. He copied the hook mechanism itself, to invent "
                    "Velcro."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e21",
        "band": "easier",
        "text": "On a dandelion, where are the parachute's fine white hairs "
                "actually attached, relative to the seed itself?",
        "options": [
            {"text": "Wrapped directly around the surface of the seed.", "correct": False,
             "why": "The hairs are not wrapped around the seed. They sit "
                    "raised above it, on their own thin stalk."},
            {"text": "On a thin stalk held above the seed.", "correct": True},
            {"text": "Hanging on a thread below the seed.", "correct": False,
             "why": "The stalk carrying the hairs rises above the seed, not "
                    "below it. Nothing here hangs beneath the seed on a "
                    "thread."},
            {"text": "Fused flat along one side of the seed, like a wing.", "correct": False,
             "why": "A wing fused along one side describes a sycamore key, "
                    "not a dandelion. The dandelion's hairs sit on a stalk "
                    "above the seed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e22",
        "band": "easier",
        "text": "You are handed an unlabelled fruit from a plant you have never "
                "heard of, and asked how its seeds travel. What should you go on?",
        "options": [
            {"text": "The number of seeds it holds, since each method has its "
                     "own fixed number.", "correct": False,
             "why": "Seed number varies within every method. A poppy and a "
                    "dandelion are both wind-dispersed and one holds "
                    "hundreds of seeds while the other holds one."},
            {"text": "The colour of the fruit, since each method of travel "
                     "has a colour of its own.", "correct": False,
             "why": "Colour only carries a meaning in one method, where "
                    "ripeness is being signalled to an animal. A dry pod and "
                    "a sycamore key are both brown and travel differently."},
            {"text": "The structures you can see on it, since the plant's "
                     "name tells you nothing.", "correct": True},
            {"text": "Nothing at all, since without the plant's name the "
                     "method cannot be settled.", "correct": False,
             "why": "The name is the one thing that would not help. Hooks, "
                    "hairs, a wing, flesh, holes or a buoyant case each give "
                    "the method away on their own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e23",
        "band": "easier",
        "text": "After a walk through goosegrass, an entire plant is often found "
                "stuck to someone's clothing, not just its fruit. What does that "
                "tell you about where its hooked bristles grow?",
        "options": [
            {"text": "They cover the whole plant, well beyond just the "
                    "fruit.", "correct": True},
            {"text": "They grow on the fruit alone, exactly as on a burdock "
                    "burr.", "correct": False,
             "why": "If the hooks were on the fruit alone, the rest of the "
                    "plant would not stick to clothing at all. They cover "
                    "the whole plant."},
            {"text": "They grow underground, on the plant's roots alone.", "correct": False,
             "why": "Roots buried in soil could never catch on passing "
                    "clothing. The hooks are on the visible parts of the "
                    "plant, above ground."},
            {"text": "They appear once the fruit has fully ripened and "
                    "dried, not before.", "correct": False,
             "why": "The whole plant sticks to clothing, not just a ripened "
                    "fruit — the hooked bristles are not limited to one "
                    "ripening stage."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e24",
        "band": "easier",
        "text": "About how long is a typical sycamore key's papery blade?",
        "options": [
            {"text": "About four millimetres.", "correct": False,
             "why": "That is far too short — a blade that size would give a "
                    "seed almost nothing to spin on. The real length is "
                    "closer to four centimetres."},
            {"text": "About four centimetres.", "correct": True},
            {"text": "About forty centimetres.", "correct": False,
             "why": "That is far too long for a single sycamore key. The "
                    "blade is closer to four centimetres, ten times "
                    "shorter."},
            {"text": "About the same length as a poppy capsule's stem.", "correct": False,
             "why": "A poppy's stem is a long, thin support many times "
                    "longer than a sycamore's blade, which measures about "
                    "four centimetres."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e25",
        "band": "easier",
        "text": "Why is a buoyant, waterproof case an expensive structure for a plant "
                "to build, compared with a hooked fruit?",
        "options": [
            {"text": "It has to be built from sugar, exactly like the flesh of "
                    "a fruit eaten by an animal.", "correct": False,
             "why": "A buoyant case is not built from sugar. Its expense "
                    "comes from the bulk of fibrous or corky material needed "
                    "to trap enough air to float."},
            {"text": "It needs to be replaced every year, unlike a hook, which "
                    "lasts for the plant's whole life.", "correct": False,
             "why": "Neither structure is described as being replaced or "
                    "reused across years — each fruit is built once. The "
                    "expense is in the amount of material the buoyant case "
                    "needs."},
            {"text": "It needs a thick fibrous or corky layer full of air "
                    "spaces, using far more material than a simple hook.", "correct": True},
            {"text": "It has to be waterproofed using the same chemicals a "
                    "stigma uses to catch pollen.", "correct": False,
             "why": "A stigma's stickiness and a seed case's waterproofing "
                    "are unrelated structures built for entirely different "
                    "jobs. The case's cost is simply its bulk."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e26",
        "band": "easier",
        "text": "Strictly, what are a dandelion 'seed' and a sycamore 'key' both "
                "actually classed as?",
        "options": [
            {"text": "Seeds that have not yet been fertilised.", "correct": False,
             "why": "Both are fully formed and ready to disperse — being "
                    "unfertilised is not what the word 'seed' is being "
                    "corrected for here."},
            {"text": "Seeds fused together with pollen grains still "
                    "attached.", "correct": False,
             "why": "Neither carries any attached pollen by this stage. The "
                    "correction is about what kind of structure each one is, "
                    "not about pollen."},
            {"text": "Empty seed cases, with nothing growing inside them.", "correct": False,
             "why": "Both contain a genuine living seed inside. Calling "
                    "them empty cases would be wrong in the opposite "
                    "direction."},
            {"text": "Single-seeded fruits, not true seeds.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e27",
        "band": "easier",
        "text": "On a hot, still afternoon a gorse bank can be heard crackling "
                "continuously, with no wind and no animals anywhere nearby. What "
                "does that tell you about how the pods are opening?",
        "options": [
            {"text": "Each pod dries and splits independently, not "
                    "triggered by any single outside event.", "correct": True},
            {"text": "One pod splitting sets off a chain reaction that "
                    "opens all the other pods nearby too.", "correct": False,
             "why": "Nothing links one pod's splitting to another's. Each "
                    "pod is drying and tearing itself apart on its own "
                    "separate timetable."},
            {"text": "The crackling is caused by insects moving around "
                    "among the pods.", "correct": False,
             "why": "No animal is needed for this method to work at all. "
                    "The sound comes from the pods themselves splitting "
                    "open."},
            {"text": "A single sudden overnight drop in temperature is "
                    "what makes all the pods burst open.", "correct": False,
             "why": "It is drying out in hot sun that builds up the "
                    "tension in a pod, not a falling temperature "
                    "overnight."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e28",
        "band": "easier",
        "text": "Which structure identifies a fruit as dispersed by being flung, "
                "rather than by any of the other four methods?",
        "options": [
            {"text": "A ring of small holes positioned just under the rim of a "
                    "dry capsule.", "correct": False,
             "why": "Small holes under a rim identify a capsule shaken open "
                    "by the wind, such as a poppy. A flung fruit instead "
                    "twists and splits itself apart."},
            {"text": "A dry pod that visibly twists as it dries, before "
                    "splitting open, often with an audible crack.", "correct": True},
            {"text": "A single wing set off to one side of a hard seed.", "correct": False,
             "why": "An off-centre wing identifies a wind-dispersed seed, "
                    "such as a sycamore key. A flung fruit is a pod that "
                    "dries, twists and splits."},
            {"text": "Sweet flesh surrounding a seed with an unusually tough "
                    "coat, built to survive a full trip through an animal's "
                    "gut.", "correct": False,
             "why": "Sweet flesh identifies a fruit dispersed inside an "
                    "animal. A flung fruit instead relies on a dry pod "
                    "tearing itself open."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e29",
        "band": "easier",
        "text": "A goosegrass plant's tiny hooked fruits are typically found growing "
                "arranged how?",
        "options": [
            {"text": "Singly, one at a time spaced out along the stem.", "correct": False,
             "why": "Goosegrass fruits are not spaced singly along the stem "
                    "— they are found growing together, in pairs."},
            {"text": "In large clusters of a dozen or more at once.", "correct": False,
             "why": "That is far more than are actually found together. "
                    "Goosegrass fruits grow in pairs, not large clusters."},
            {"text": "Fused together into one long continuous chain.", "correct": False,
             "why": "The fruits stay as separate pairs rather than joining "
                    "into a chain. Each pair is a distinct, separate unit."},
            {"text": "In pairs.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-e30",
        "band": "easier",
        "text": "On a dry, breezy day, roughly how far can a single dandelion seed "
                "be carried?",
        "options": [
            {"text": "No more than a few centimetres.", "correct": False,
             "why": "That badly understates it. A parachute that slows the "
                    "fall this much can carry a seed far further than a few "
                    "centimetres on a breezy day."},
            {"text": "Around ten metres at most.", "correct": False,
             "why": "Ten metres is still far too short. On a good breezy "
                    "day a dandelion seed can travel a great deal further "
                    "than that."},
            {"text": "As much as a kilometre.", "correct": True},
            {"text": "Many hundreds of kilometres.", "correct": False,
             "why": "That is wildly too far for a seed this light and "
                    "short-lived in the air. A kilometre is closer to its "
                    "best case."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "b5-08-s07",
        "band": "standard",
        "text": "A sycamore key weighs many times more than a dandelion seed, yet "
                "both are dispersed by wind. Explain how the sycamore manages this "
                "despite being so much heavier.",
        "options": [
            {"text": "Its single wing makes it spin as it falls, which slows "
                    "the fall enough for wind to carry a heavier seed at "
                    "least clear of the parent tree.", "correct": True},
            {"text": "It is not really dispersed by wind — a sycamore key "
                    "mostly rolls away across the ground instead.", "correct": False,
             "why": "A sycamore key is a genuine wind-dispersed specimen. Its "
                    "spinning wing slows its fall enough for wind to move it, "
                    "even though it is much heavier than a dandelion seed."},
            {"text": "Wind exerts a stronger force on a heavier object, which "
                    "balances out the extra weight.", "correct": False,
             "why": "Wind does not push harder on something simply because it "
                    "is heavier. What actually helps the sycamore is its "
                    "spinning wing slowing its fall, giving wind more time to "
                    "act."},
            {"text": "A sycamore key produces so many more seeds than a "
                    "dandelion that a few unusually heavy ones are bound to "
                    "travel far purely by chance.", "correct": False,
             "why": "Numbers alone would not overcome the seed's weight. It "
                    "is specifically the spinning wing slowing the fall that "
                    "lets wind move it any real distance at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s08",
        "band": "standard",
        "text": "A blackberry stays green, hard and sour for about two weeks before "
                "ripening. Explain why an early-ripening mutant blackberry plant "
                "would likely leave fewer descendants.",
        "options": [
            {"text": "Early ripening would use up too much of the plant's own "
                    "energy reserves.", "correct": False,
             "why": "Energy cost is not the reason given for the timing. The "
                    "problem with ripening early is that the seeds inside "
                    "would not yet be ready to grow when carried away."},
            {"text": "An animal eating its fruit early would carry off seeds "
                    "that were not yet ready and could not grow.", "correct": True},
            {"text": "An early-ripening fruit would simply taste less sweet to "
                    "any animal that found it.", "correct": False,
             "why": "Sweetness is not really the issue here. The real problem "
                    "is that any seeds eaten before they are ready cannot go "
                    "on to germinate successfully."},
            {"text": "Birds would ignore an early-ripening fruit entirely and "
                    "simply wait for it to ripen properly before ever going "
                    "near it.", "correct": False,
             "why": "Birds are not described as being able to tell a fruit's "
                    "readiness from a distance. The real risk of early "
                    "ripening is seeds being carried away before they can "
                    "grow."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s09",
        "band": "standard",
        "text": "Water dispersal and dispersal inside an animal are both described "
                "as expensive strategies for a plant. What is the key difference "
                "in what that cost is spent on?",
        "options": [
            {"text": "There is no real difference — both methods spend "
                    "exactly the same resource, water itself, just at a "
                    "different point in the process.", "correct": False,
             "why": "Water dispersal spends material building a case; "
                    "dispersal inside an animal spends sugar. Neither is "
                    "paid for in water."},
            {"text": "Water dispersal spends bulk material on a floating "
                    "case; dispersal inside an animal spends sugar the plant "
                    "made itself.", "correct": True},
            {"text": "Both methods spend their cost on bright colouring, in "
                    "slightly different amounts.", "correct": False,
             "why": "A buoyant case is not coloured for attention at all — "
                    "colour signals belong to fleshy fruit, not to a "
                    "floating seed case."},
            {"text": "Water dispersal costs the plant nothing to build in "
                    "the first place; the animal-eaten method alone "
                    "carries the real expense.", "correct": False,
             "why": "A thick, buoyant, waterproof case takes real material "
                    "to build. Water dispersal is expensive too, just in a "
                    "different currency."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s10",
        "band": "standard",
        "text": "Explain why a plant relying on water dispersal is restricted to "
                "growing near rivers, lakes or coastlines, while a wind-dispersed "
                "plant is not restricted in the same way.",
        "options": [
            {"text": "Water-dispersed seeds cannot survive being planted "
                    "anywhere except very wet soil.", "correct": False,
             "why": "Where a seed can germinate is a separate question from "
                    "how it travels. The restriction on water dispersal is "
                    "about needing water to carry the seed there in the first "
                    "place."},
            {"text": "Wind-dispersed seeds are always lighter than "
                    "water-dispersed ones, wherever in the world each kind of "
                    "plant happens to grow, whatever the local climate is "
                    "like.", "correct": False,
             "why": "Weight differences are a side-effect, not the reason for "
                    "the restriction. What matters is that a buoyant case is "
                    "useless without water actually present to carry it."},
            {"text": "Rivers and coastlines simply have stronger winds than "
                    "other habitats do.", "correct": False,
             "why": "Wind strength near water is not the point being made "
                    "here. The restriction is that a floating case needs "
                    "water present at all, which wind dispersal does not."},
            {"text": "A buoyant seed case only does its job where there is "
                    "water available to carry it; wind is available almost "
                    "everywhere a plant grows.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s11",
        "band": "standard",
        "text": "A hooked fruit and a wind-blown seed both end up scattered in "
                "essentially random locations. Explain the one important difference "
                "in HOW that randomness comes about.",
        "options": [
            {"text": "A hooked fruit's landing spot depends on an animal's own "
                    "unpredictable movements, while a wind-blown seed's "
                    "depends on the unpredictable movement of air.", "correct": True},
            {"text": "There is no real difference — both are equally random in "
                    "exactly the same way.", "correct": False,
             "why": "The mechanisms are genuinely different, even though both "
                    "outcomes are unpredictable: one follows an animal's "
                    "path, the other follows moving air."},
            {"text": "A hooked fruit's landing spot is actually fairly "
                    "predictable, since animals in a given area tend to "
                    "follow broadly similar, well-worn paths day after day.", "correct": False,
             "why": "An individual animal's exact route and grooming moment "
                    "are not predictable in practice, which is precisely why "
                    "this method offers the plant no control at all."},
            {"text": "Wind-blown seeds are not random at all, since wind "
                    "always blows in one fixed direction.", "correct": False,
             "why": "Wind direction varies constantly with the weather, which "
                    "is exactly why a wind-blown seed's landing spot cannot "
                    "be predicted in advance."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s12",
        "band": "standard",
        "text": "A plant produces both a few large, well-provisioned seeds and, "
                "separately, many small, poorly-provisioned ones. Suggest which of "
                "the two is more likely to be the wind-dispersed batch, and why.",
        "options": [
            {"text": "The large, well-provisioned ones — a bigger food store "
                    "helps a seed survive an unusually long flight through "
                    "the air before it eventually lands.", "correct": False,
             "why": "A long flight is not really the challenge here; being "
                    "light enough to be carried at all is. A large food store "
                    "would make a seed far too heavy for wind to move."},
            {"text": "The small, poorly-provisioned ones — wind dispersal "
                    "needs a very light seed, so a large food store would be "
                    "too costly to include.", "correct": True},
            {"text": "Neither — wind-dispersed seeds are always exactly the "
                    "same size as every other seed a plant produces.", "correct": False,
             "why": "Plants vary considerably in seed size depending on "
                    "dispersal strategy. Wind specifically favours very light "
                    "seeds, which rules out a large well-provisioned one."},
            {"text": "It cannot be decided without knowing which habitat the "
                    "plant grows in.", "correct": False,
             "why": "Habitat is not the deciding factor for this particular "
                    "question. The seed's own weight is what determines "
                    "whether wind can move it at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s13",
        "band": "standard",
        "text": "The five dispersal methods differ enormously in how much control the "
                "plant has over the SPECIFIC place its seeds end up. Rank wind and "
                "'flung by the plant' by that control, and justify the order.",
        "options": [
            {"text": "Wind offers more control, since the plant can choose "
                    "which direction to release its seeds into.", "correct": False,
             "why": "A plant has no mechanism for choosing wind direction. "
                    "Being flung actually gives slightly more control, since "
                    "the range is fixed and short."},
            {"text": "Both offer identical control, since neither method "
                    "involves any living creature making a conscious decision "
                    "about precisely where any seed ends up.", "correct": False,
             "why": "The two methods differ in how far and unpredictably "
                    "seeds can travel, even though neither involves a "
                    "decision-making animal — flung is more contained than "
                    "wind."},
            {"text": "Flung offers slightly more control, since seeds land "
                    "within a fixed short range around the plant, whereas "
                    "wind can carry a seed almost anywhere.", "correct": True},
            {"text": "Neither offers any control at all, so the two cannot "
                    "meaningfully be ranked against each other.", "correct": False,
             "why": "They can be compared by the range and unpredictability "
                    "of where seeds land — flung stays within a short, fixed "
                    "range, while wind can scatter a seed far more widely."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s14",
        "band": "standard",
        "text": "A dandelion parachute can carry a seed a kilometre on a breezy day, "
                "but most dandelion seedlings are found within a few metres of the "
                "parent plant. Reconcile these two facts.",
        "options": [
            {"text": "One of the two facts must be some kind of measurement "
                    "error, since a whole kilometre and a few metres clearly "
                    "contradict each other outright.", "correct": False,
             "why": "The two facts do not actually contradict — most seeds "
                    "landing close by, and a rare few travelling very far, "
                    "are both parts of the same real pattern."},
            {"text": "The kilometre figure only applies to a completely "
                    "different species of dandelion.", "correct": False,
             "why": "Both figures are reported for the same species. They "
                    "describe two different parts of one distribution: the "
                    "common short journeys and the rare long ones."},
            {"text": "Seedlings found close to the parent must have blown back "
                    "afterwards on a returning wind.", "correct": False,
             "why": "There is no need to invent a returning wind. Most seeds "
                    "simply never travel far in the first place; only a rare "
                    "few reach a kilometre."},
            {"text": "Both are true at once: most seeds land close by, but a "
                    "small proportion genuinely do travel much further, given "
                    "the right conditions.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s15",
        "band": "standard",
        "text": "Explain why 'the flesh is a fee, not a gift' is a more "
                "scientifically accurate way to describe a fleshy fruit than saying "
                "the plant is being generous to animals.",
        "options": [
            {"text": "The flesh is built specifically to get the seed carried "
                    "and dropped somewhere useful, which is a transaction "
                    "with a clear benefit to the plant, not an act of "
                    "generosity.", "correct": True},
            {"text": "Because animals never actually benefit at all from "
                    "eating fleshy fruit.", "correct": False,
             "why": "Animals genuinely do gain food value from eating the "
                    "fruit. The point is that the plant is not simply giving "
                    "without expecting anything back — it is buying transport "
                    "for its seeds."},
            {"text": "Because fleshy fruit is always poisonous to at least "
                    "some animal species.", "correct": False,
             "why": "Toxicity to some species is not the reason 'fee' is the "
                    "better word here. The key point is that the flesh buys "
                    "the seed a journey, rather than being a selfless gift."},
            {"text": "Because the plant could, in principle, produce exactly "
                    "the same sweet, brightly coloured fruit without ever "
                    "needing any animal to be involved in the process at all.", "correct": False,
             "why": "The whole point of this dispersal method is that it does "
                    "depend on an animal eating the fruit. That dependence is "
                    "exactly why 'fee' captures the relationship better than "
                    "'gift'."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s16",
        "band": "standard",
        "text": "A dry, papery pod splits open along its length as it dries, "
                "revealing four seeds inside that then simply fall to the ground "
                "directly below it. Is this genuinely an effective dispersal "
                "structure? Justify your answer.",
        "options": [
            {"text": "Yes — splitting open on its own, without needing wind, "
                    "water or an animal, makes it efficient by definition.", "correct": False,
             "why": "Needing no outside help is only useful if the seeds "
                    "actually end up somewhere new. Simply falling straight "
                    "down defeats the purpose of dispersing at all."},
            {"text": "No — seeds only falling straight down land directly "
                    "under the parent, which every other dispersal structure "
                    "exists to avoid.", "correct": True},
            {"text": "Yes — a papery pod is cheap to build, so this method "
                    "costs the plant almost nothing.", "correct": False,
             "why": "Low cost does not make a method effective if the seeds "
                    "end up exactly where they started. Landing under the "
                    "parent is the one outcome dispersal is meant to prevent."},
            {"text": "It cannot be judged without knowing how many seeds are "
                    "inside the pod.", "correct": False,
             "why": "The number of seeds does not change the basic problem "
                    "here. Landing directly under the parent is ineffective "
                    "regardless of how many seeds fall that way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s17",
        "band": "standard",
        "text": "Two plants of the same species are compared: one disperses its seeds "
                "effectively, the other's seeds nearly all land under the parent "
                "plant. Predict which is more likely to have more surviving "
                "grandchildren, and explain why.",
        "options": [
            {"text": "The one whose seeds land under the parent, since they "
                    "are guaranteed the same good growing conditions the "
                    "parent already enjoys.", "correct": False,
             "why": "Landing where the parent already grows means competing "
                    "directly with it for light, water and minerals — a "
                    "contest a small seedling usually loses."},
            {"text": "Neither is more likely to succeed, since both plants "
                    "produce exactly the same number of seeds.", "correct": False,
             "why": "Producing the same number of seeds does not guarantee "
                    "the same number of survivors. Where those seeds land "
                    "makes a real difference to how many actually grow to "
                    "reproduce."},
            {"text": "The one with effective dispersal, because its seedlings "
                    "avoid competing directly with the large, "
                    "already-established parent plant.", "correct": True},
            {"text": "The one whose seeds land under the parent, because "
                    "staying close keeps the whole population concentrated "
                    "and easier to defend.", "correct": False,
             "why": "Nothing about seed dispersal involves any kind of "
                    "collective defence. Seedlings under the parent simply "
                    "lose a competition for light, water and minerals."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s18",
        "band": "standard",
        "text": "A wind-dispersed plant and a plant dispersed inside animals are "
                "compared for the NUMBER of seeds each typically produces. Explain "
                "the pattern you would expect, and why.",
        "options": [
            {"text": "Both typically produce about the same number of seeds, "
                    "since seed number depends only on the size of the plant.", "correct": False,
             "why": "Seed number varies enormously with dispersal strategy, "
                    "not simply with plant size. Wind dispersal in particular "
                    "is wasteful enough to demand very large numbers."},
            {"text": "The animal-dispersed plant typically makes far more "
                    "seeds, since fruit is cheap to build compared with a "
                    "parachute.", "correct": False,
             "why": "Fleshy fruit is usually described as the most expensive "
                    "dispersal structure to build, not the cheapest, which "
                    "pushes numbers down rather than up."},
            {"text": "Neither pattern can be predicted at all, since seed "
                    "number depends entirely on the local climate and "
                    "rainfall in a given year rather than on the dispersal "
                    "method a plant happens to use.", "correct": False,
             "why": "Climate plays some role, but the method itself has a "
                    "clear general effect: wind dispersal's wastefulness "
                    "pushes seed numbers up far more than animal dispersal's "
                    "does."},
            {"text": "The wind-dispersed plant typically makes far more seeds, "
                    "because so many of them land somewhere useless; the "
                    "animal-dispersed one can make fewer, more reliably "
                    "placed ones.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s19",
        "band": "standard",
        "text": "A seed is found with an unusually thick, chemically resistant coat, "
                "far tougher than most seeds of similar size. Suggest which dispersal "
                "method it most likely belongs to, and why.",
        "options": [
            {"text": "Inside an animal — the coat has to survive being "
                    "swallowed, digested and passed through a gut without "
                    "being destroyed.", "correct": True},
            {"text": "Wind — a thick coat protects the seed from being damaged "
                    "as it spins through the air.", "correct": False,
             "why": "Spinning through the air does not typically damage a "
                    "seed enough to need an unusually tough coat. That level "
                    "of toughness is far more associated with surviving "
                    "digestion."},
            {"text": "Flung by the plant — the coat has to survive the shock "
                    "of being thrown clear of the pod.", "correct": False,
             "why": "Being flung a short distance does not usually demand an "
                    "especially chemically resistant coat. That kind of "
                    "toughness points instead to surviving a trip through an "
                    "animal's gut."},
            {"text": "On an animal — the coat has to resist being worn away by "
                    "rubbing against an animal's fur for a long period while "
                    "it is being carried.", "correct": False,
             "why": "A hooked fruit is not usually described as needing "
                    "special chemical resistance, since it is not exposed to "
                    "digestive processes. That level of toughness fits "
                    "surviving digestion instead."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s20",
        "band": "standard",
        "text": "Suggest one reason a plant might combine two dispersal methods — for "
                "example, a fruit with both a light structure AND small hooks — "
                "rather than relying on just one.",
        "options": [
            {"text": "Combining methods always roughly doubles how far every "
                    "single seed will eventually travel.", "correct": False,
             "why": "Combining structures does not guarantee a longer journey "
                    "for any individual seed. It instead offers a second "
                    "chance if the first method's conditions do not occur."},
            {"text": "It hedges its bets: if wind conditions are poor, a "
                    "passing animal might still carry the seed away instead.", "correct": True},
            {"text": "It halves the number of seeds the plant needs to produce "
                    "overall.", "correct": False,
             "why": "Nothing about combining structures is described as "
                    "reducing how many seeds are needed. If anything, "
                    "building two structures could cost more, not less."},
            {"text": "It stops the plant's seeds from ever landing under its "
                    "own shade.", "correct": False,
             "why": "Combining methods does not guarantee a seed avoids "
                    "landing under the parent. It simply offers a second "
                    "possible route for a seed to be moved."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s21",
        "band": "standard",
        "text": "A researcher wants to know whether a newly discovered plant "
                "disperses its seeds mainly by wind or mainly by water. Suggest the "
                "single most useful piece of evidence to look for on the seed itself.",
        "options": [
            {"text": "The colour of the seed case, since wind-dispersed seeds "
                    "are always duller in colour than water-dispersed ones.", "correct": False,
             "why": "Colour is not a reliable indicator between these two "
                    "methods — bright colour is far more relevant to "
                    "distinguishing animal-dispersed fruit from either of "
                    "these."},
            {"text": "How many seeds the plant produces in a single season.", "correct": False,
             "why": "Seed number varies for other reasons too and does not by "
                    "itself distinguish wind from water dispersal. The seed "
                    "case's own structure is the more direct evidence."},
            {"text": "Whether the seed case is light with a wing or parachute, "
                    "or heavy and buoyant with a waterproof coating.", "correct": True},
            {"text": "The exact time of year the plant releases its seeds.", "correct": False,
             "why": "Release timing can vary for many reasons unrelated to "
                    "the dispersal method itself. The seed case's weight and "
                    "structure is much more directly diagnostic."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s22",
        "band": "standard",
        "text": "Explain why a very heavy seed like a coconut could never "
                "realistically evolve a parachute of fine hairs as its dispersal "
                "structure.",
        "options": [
            {"text": "Coconut palms do not grow tall enough for a parachute to "
                    "have time to work.", "correct": False,
             "why": "Height is not the limiting factor here. The real problem "
                    "is that a parachute cannot meaningfully slow the fall of "
                    "something as heavy as a coconut, whatever the drop "
                    "height."},
            {"text": "Hairs cannot grow on a surface as fibrous as a coconut "
                    "husk.", "correct": False,
             "why": "There is no described physical barrier to hairs growing "
                    "on a fibrous surface. The real reason a parachute would "
                    "not work is the seed's own great weight."},
            {"text": "A coconut already has so many other structures built "
                    "into its thick, fibrous husk that there would be no "
                    "physical room left anywhere for a parachute of fine "
                    "hairs to grow as well.", "correct": False,
             "why": "Space on the seed's surface is not the limiting issue. A "
                    "parachute simply cannot overcome the sheer weight of a "
                    "seed this heavy."},
            {"text": "A parachute only slows a fall enough to matter if the "
                    "seed is already extremely light; adding hairs to "
                    "something as heavy as a coconut would make almost no "
                    "difference to its fall.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s23",
        "band": "standard",
        "text": "A plant disperses its seeds inside animals, but a drought kills off "
                "most of the local animal population for several years. Predict the "
                "most likely effect on that plant's population, and explain your "
                "reasoning.",
        "options": [
            {"text": "Its seeds are likely to be dispersed far less "
                    "effectively, since fewer animals are available to eat "
                    "the fruit and carry the seeds away.", "correct": True},
            {"text": "There would be no effect at all, since seed dispersal "
                    "does not depend on animals being present.", "correct": False,
             "why": "This particular plant's whole strategy depends on an "
                    "animal eating its fruit. A shortage of animals directly "
                    "reduces how many of its seeds get carried anywhere."},
            {"text": "The plant would automatically switch to wind dispersal "
                    "instead until animal numbers recovered.", "correct": False,
             "why": "A plant cannot switch dispersal strategy on demand — its "
                    "fruit structure is fixed. A shortage of animals simply "
                    "means fewer of its seeds get moved at all."},
            {"text": "The plant's seeds would simply begin dispersing by water "
                    "instead, since a nearby river or lake would be entirely "
                    "unaffected by the drought.", "correct": False,
             "why": "This plant's fruit has no buoyant structure suited to "
                    "water dispersal. Fewer animals available simply means "
                    "less effective dispersal overall, not a switch to a "
                    "different method."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s24",
        "band": "standard",
        "text": "A plant makes both large fleshy fruits AND small dry pods that fling "
                "their seeds. Suggest why producing two very different kinds of "
                "dispersal structure might benefit it.",
        "options": [
            {"text": "It is simply a wasteful mistake, since a plant should "
                    "only ever specialise in one dispersal method.", "correct": False,
             "why": "Real plants that combine strategies are not generally "
                    "described as making an error. Having two different "
                    "structures spreads the risk rather than wasting "
                    "resources."},
            {"text": "Each method has a different weakness, so having both "
                    "increases the chance that at least some seeds are "
                    "dispersed successfully whatever conditions occur.", "correct": True},
            {"text": "The two structures are actually identical in function "
                    "and differ only in appearance.", "correct": False,
             "why": "Fleshy fruit and a flinging pod work by completely "
                    "different mechanisms, needing an animal versus needing "
                    "nothing but the plant's own drying tissue."},
            {"text": "It allows the plant to control precisely which method "
                    "disperses which proportion of its seeds.", "correct": False,
             "why": "A plant has no way to direct which of its seeds ends up "
                    "dispersed by which method. Having both simply improves "
                    "the overall odds, not the control over the outcome."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s25",
        "band": "standard",
        "text": "A plant's fruit ripens gradually over several weeks rather than all "
                "at once. Suggest one advantage this staggered ripening might give "
                "the plant, in terms of dispersal.",
        "options": [
            {"text": "It lets the plant grow a noticeably larger total number "
                    "of seeds than ripening every fruit all at once, in one "
                    "narrow window, would ever practically allow.", "correct": False,
             "why": "Total seed number is set well before ripening begins and "
                    "is not increased simply by spreading ripening out over "
                    "time."},
            {"text": "It prevents the seeds inside from being able to "
                    "germinate too early.", "correct": False,
             "why": "Preventing early germination is the tough seed coat's "
                    "job throughout development, not something staggered "
                    "ripening specifically achieves."},
            {"text": "It spreads the plant's chances across a longer period, "
                    "rather than depending on one narrow window when an "
                    "animal happens to be nearby.", "correct": True},
            {"text": "It means every single fruit on the plant ends up exactly "
                    "the same size.", "correct": False,
             "why": "Fruit size is not the issue staggered ripening "
                    "addresses. The advantage is about timing dispersal "
                    "across a longer window, not about uniform size."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s26",
        "band": "standard",
        "text": "Compare a gorse pod's typical dispersal range with a dandelion's. "
                "Explain the one structural reason for the large difference.",
        "options": [
            {"text": "The gorse pod is simply a much older, less evolved "
                    "structure than the dandelion's parachute.", "correct": False,
             "why": "Age of a structure is not given as the explanation here. "
                    "The real difference is that flinging uses the plant's "
                    "own limited energy, while wind can carry a light "
                    "parachuting seed much further."},
            {"text": "Dandelions simply grow in noticeably windier places than "
                    "gorse typically does, and that difference in local "
                    "climate alone fully explains the whole size of the "
                    "difference in range.", "correct": False,
             "why": "Location is not the structural reason given. The key "
                    "difference is in the two seeds' own structures: one is "
                    "flung with limited energy, the other is carried a great "
                    "distance by wind."},
            {"text": "Gorse seeds are dispersed by animals rather than being "
                    "flung at all.", "correct": False,
             "why": "A gorse pod flings its own seeds by drying and "
                    "splitting; no animal is involved. The range difference "
                    "comes from that method compared with a wind-carried "
                    "parachute."},
            {"text": "A gorse pod only flings seeds a few metres using its own "
                    "stored energy, while a dandelion's very light seed and "
                    "parachute let wind carry it up to a kilometre.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s27",
        "band": "standard",
        "text": "A plant relies on a single species of bird to disperse its seeds, "
                "and that bird's population then collapses. Suggest the biggest "
                "disadvantage of relying on only one disperser, illustrated by this "
                "example.",
        "options": [
            {"text": "The plant's whole dispersal strategy fails at once if "
                    "that one species disappears, with no other route for its "
                    "seeds to travel.", "correct": True},
            {"text": "The plant would need to grow noticeably taller than "
                    "before, simply in order to attract some kind of "
                    "replacement disperser.", "correct": False,
             "why": "Height is not identified as the relevant factor here. "
                    "The disadvantage is having no alternative route for "
                    "seeds at all once the one disperser is gone."},
            {"text": "The seeds themselves would become too tough for any "
                    "other animal to digest.", "correct": False,
             "why": "Seed toughness does not change because a disperser's "
                    "population collapses. The real disadvantage is simply "
                    "having no back-up method of dispersal."},
            {"text": "The plant's fruit would automatically become less "
                    "colourful over just a few years.", "correct": False,
             "why": "Fruit colouring does not change automatically in "
                    "response to a disperser's population. The disadvantage "
                    "illustrated is the total loss of a dispersal route with "
                    "no alternative."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s28",
        "band": "standard",
        "text": "The explanation for dandelion parachutes says some ancestral seeds "
                "'happened to have a slightly better wing, a stickier hook, "
                "sweeter flesh' already, before any selection acted on them. Why "
                "is that detail scientifically important?",
        "options": [
            {"text": "It shows the variation existed first, by chance, and "
                    "selection then acted on differences that were already "
                    "there.", "correct": True},
            {"text": "It shows that wings vary between individual seeds, "
                    "while hooks and flesh stay fixed.", "correct": False,
             "why": "The explanation names variation in wings, hooks and "
                    "flesh alike. Nothing here singles out wings as the "
                    "structure that can vary."},
            {"text": "It shows that natural selection creates brand-new "
                    "variation directly, rather than acting on differences "
                    "that already exist.", "correct": False,
             "why": "This gets the order backwards. Selection acts on "
                    "variation that is already present; it does not create "
                    "that variation itself."},
            {"text": "It shows the improvement happened suddenly, within "
                    "one whole generation, rather than building up "
                    "gradually across many.", "correct": False,
             "why": "The change described takes many generations of seeds "
                    "landing further and surviving more often — nothing "
                    "about it happens inside one whole generation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s29",
        "band": "standard",
        "text": "A seed's coat is unusually thin and fragile compared with most seeds "
                "dispersed inside an animal. Suggest what this tells you about how "
                "that particular seed is most likely dispersed instead.",
        "options": [
            {"text": "It confirms the seed is dispersed inside an animal, "
                    "since a noticeably thinner coat would digest a good deal "
                    "more easily and quickly.", "correct": False,
             "why": "Easy digestion is exactly the problem for this dispersal "
                    "method: the coat has to SURVIVE digestion, not be broken "
                    "down by it, for the seed to grow afterwards."},
            {"text": "It tells you nothing useful at all, since coat thickness "
                    "has no connection to dispersal method.", "correct": False,
             "why": "Coat thickness is actually a useful clue: seeds that "
                    "must survive a trip through a gut typically need an "
                    "unusually tough coat, which this one lacks."},
            {"text": "Probably not inside an animal — a thin, fragile coat "
                    "would be destroyed during digestion, so some other "
                    "method is more likely.", "correct": True},
            {"text": "It suggests the seed must be dispersed by being flung, "
                    "since flung seeds need the thinnest coats of all.", "correct": False,
             "why": "Coat thinness is not specifically linked to being flung "
                    "in this way. What a thin, fragile coat rules out most "
                    "strongly is survival through an animal's digestive "
                    "system."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-s30",
        "band": "standard",
        "text": "Some fruits are poisonous to humans while being perfectly good, "
                "edible food for the bird species that normally disperses them. "
                "Explain what this tells you about a fruit's bright colour and "
                "sweetness.",
        "options": [
            {"text": "It proves the fruit cannot really be dispersed by "
                    "any animal, since no creature would want to eat "
                    "something poisonous.", "correct": False,
             "why": "The fruit clearly is dispersed by an animal — the "
                    "bird species it targets. Being unsafe for humans does "
                    "not change that."},
            {"text": "It shows the colour and sweetness serve no real "
                    "dispersal purpose and are simply decorative "
                    "leftovers from the flower.", "correct": False,
             "why": "Colour and sweetness are the whole advertising system "
                    "that attracts the fruit's disperser — they are doing "
                    "real work, not decoration."},
            {"text": "They are a signal aimed at whichever animal disperses "
                    "that species, not at every animal that might come "
                    "across it.", "correct": True},
            {"text": "It means the plant is specifically trying to poison "
                    "human beings.", "correct": False,
             "why": "A plant is not aiming its chemistry at humans at all. "
                    "Its signal is built for the animal it depends on for "
                    "dispersal."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "b5-08-h07",
        "band": "harder",
        "text": "A researcher genetically fingerprints 500 seedlings around a single "
                "parent tree. 470 are found within 10 metres, but the remaining 30 "
                "are scattered between 200 and 900 metres away. Calculate what "
                "percentage of seedlings made up this long-distance group.",
        "options": [
            {"text": "6%.", "correct": True},
            {"text": "30%.", "correct": False,
             "why": "That treats 30 as a percentage directly rather than as a "
                    "fraction of the total 500. 30 out of 500 is 6%, not 30%."},
            {"text": "94%.", "correct": False,
             "why": "That is the percentage found close to the parent "
                    "(470/500), not the long-distance group being asked for, "
                    "which is 30/500 = 6%."},
            {"text": "16%.", "correct": False,
             "why": "That does not match the numbers given. 30 out of 500 "
                    "works out at exactly 6%."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h08",
        "band": "harder",
        "text": "A wind-dispersed plant produces 3,000 seeds every year. Long-term "
                "monitoring shows that 6 in every 1,000 of those seeds go on to "
                "survive as adult plants. At that same rate, how many years would "
                "it take to produce a total of 90 surviving adult plants?",
        "options": [
            {"text": "15 years.", "correct": False,
             "why": "That uses only 6 survivors a year, forgetting to scale "
                    "the rate up to the full 3,000 seeds produced annually. "
                    "The true yearly figure is 18, not 6."},
            {"text": "0.5 years.", "correct": False,
             "why": "That mistakes 6 in every 1,000 for 6%, giving 180 "
                    "survivors a year instead of the correct 18."},
            {"text": "5 years.", "correct": True},
            {"text": "1,620 years.", "correct": False,
             "why": "That multiplies the years by the yearly survivors "
                    "instead of dividing. 90 divided by 18 gives 5 years, "
                    "not 90 times 18."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h09",
        "band": "harder",
        "text": "A dandelion, a sycamore and a poppy are all wind-dispersed, yet only "
                "two of the three have a wing or a parachute. Explain what this tells "
                "you about testing an unfamiliar wind-dispersed specimen.",
        "options": [
            {"text": "It tells you that exactly two out of every three "
                    "wind-dispersed plant species will always lack any kind "
                    "of wing or parachute structure whatsoever, according to "
                    "this reasoning.", "correct": False,
             "why": "This is a general point about testing, not a fixed ratio "
                    "that applies to every group of wind-dispersed plants. "
                    "The poppy is simply proof that absence of a wing or "
                    "parachute does not rule wind out."},
            {"text": "It tells you that poppies must actually be dispersed by "
                    "a completely different, undiscovered method.", "correct": False,
             "why": "The poppy's own capsule and stem mechanism is well "
                    "understood and genuinely wind-based, just without a wing "
                    "or parachute — there is no need to invent another "
                    "method."},
            {"text": "A wing or parachute is sufficient evidence of wind "
                    "dispersal, but its absence is not sufficient evidence "
                    "AGAINST it — some other mechanism, like shaking, might "
                    "still be at work.", "correct": True},
            {"text": "It tells you that wings and parachutes are, in fact, "
                    "unnecessary for every wind-dispersed species.", "correct": False,
             "why": "Wings and parachutes clearly do help many wind-dispersed "
                    "species, including the dandelion and sycamore. The poppy "
                    "is the exception that shows their absence does not rule "
                    "wind out, not proof they are never needed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h10",
        "band": "harder",
        "text": "A plant is discovered whose fruit is bright red, fleshy and sweet, "
                "but whose seed coat is thin and fragile rather than especially "
                "tough. Assess whether this combination is likely, and suggest what "
                "might be missing from the description.",
        "options": [
            {"text": "Perfectly likely — bright colour and sweetness are the "
                    "only features that matter for this dispersal method.", "correct": False,
             "why": "Colour and sweetness attract an animal, but the seed "
                    "still has to physically survive being swallowed and "
                    "digested, which a thin, fragile coat is unlikely to "
                    "manage."},
            {"text": "Perfectly likely — a fragile coat actually helps the "
                    "seed digest more easily and grow faster afterwards.", "correct": False,
             "why": "Easy digestion is the opposite of what this dispersal "
                    "method needs: the coat has to resist digestion, not "
                    "assist it, for the seed to survive the journey."},
            {"text": "Unlikely, but only because bright red fruits are always "
                    "dispersed by wind rather than by animals.", "correct": False,
             "why": "Bright colour is in fact a classic signal used to "
                    "attract animals to a fruit, not a feature associated "
                    "with wind dispersal. The real inconsistency is the "
                    "fragile coat."},
            {"text": "Unlikely as described — a seed dispersed by being eaten "
                    "normally needs an unusually tough coat to survive "
                    "digestion, so either the coat is tougher than stated or "
                    "another mechanism protects the seed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h11",
        "band": "harder",
        "text": "A plant produces seeds with BOTH a thick waterproof case and small "
                "hooks on the outside. It grows on a riverbank that occasionally "
                "floods and is also visited by grazing animals. Explain why this "
                "combination of structures makes sense there.",
        "options": [
            {"text": "Either route can succeed depending on conditions — "
                    "floodwater can carry the buoyant case away, or a grazing "
                    "animal can pick up a hooked seed, whichever happens "
                    "first.", "correct": True},
            {"text": "The two structures actually cancel each other out, so "
                    "the seed ends up dispersed by neither method.", "correct": False,
             "why": "There is no mechanism by which a waterproof case and "
                    "hooks would interfere with each other. Each can work "
                    "independently, giving the seed two possible routes "
                    "rather than none."},
            {"text": "The hooks are only there to help the seed cling onto the "
                    "riverbank itself, so that it does not get swept away "
                    "downstream by the current before an animal finds it.", "correct": False,
             "why": "Hooks are a device for catching onto a passing animal, "
                    "not for anchoring a seed in place against water."},
            {"text": "The waterproof case is only useful for keeping the seed "
                    "dry between floods, not for dispersal itself.", "correct": False,
             "why": "A waterproof, buoyant case is specifically a dispersal "
                    "structure for travelling on water, not simply a way of "
                    "staying dry between one flood and the next."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h12",
        "band": "harder",
        "text": "A wind-dispersed plant makes 2,000 seeds a year, of which studies "
                "suggest only about 4 in 1,000 ever land somewhere they can grow into "
                "an adult plant. Calculate how many of the 2,000 seeds that "
                "represents.",
        "options": [
            {"text": "4.", "correct": False,
             "why": "That treats 4 as the final answer without scaling it up "
                    "to the actual 2,000 seeds produced. 4 in 1,000 of 2,000 "
                    "is 8, not 4."},
            {"text": "8.", "correct": True},
            {"text": "80.", "correct": False,
             "why": "That is ten times too many. 4 per 1,000 of 2,000 seeds "
                    "gives 8, since 2,000 is only twice 1,000, not twenty "
                    "times it."},
            {"text": "500.", "correct": False,
             "why": "That divides 2,000 by 4 rather than applying the given "
                    "rate. 4 in 1,000 of 2,000 seeds is 8."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h13",
        "band": "harder",
        "text": "A wind-dispersed plant's seeds succeed only very rarely — a handful "
                "out of every few thousand grow into adult plants. Explain why "
                "this does not mean wind dispersal is a poor strategy for the species "
                "as a whole.",
        "options": [
            {"text": "It does mean wind dispersal is a poor strategy, and "
                    "species using it are gradually dying out as a result.", "correct": False,
             "why": "A low per-seed success rate is not the same as the whole "
                    "population declining. Many wind-dispersed species have "
                    "persisted successfully for a very long time on exactly "
                    "this strategy."},
            {"text": "The low success rate is fully compensated for by each "
                    "surviving seed growing into an unusually large plant.", "correct": False,
             "why": "There is no described connection between how few seeds "
                    "succeed and how large the survivors then grow. What "
                    "compensates is simply the very large number of seeds "
                    "produced."},
            {"text": "As long as enough seeds are made that at least a few "
                    "succeed each generation, the population can persist even "
                    "with a very low individual success rate.", "correct": True},
            {"text": "It does not really matter at all, because the vast "
                    "majority of a wind-dispersed plant's total energy "
                    "actually goes into growing leaves and roots rather than "
                    "seeds.", "correct": False,
             "why": "Where the plant's energy mostly goes is not the point "
                    "here. The strategy works because producing very large "
                    "numbers of cheap seeds makes up for the low success rate "
                    "of any individual one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h14",
        "band": "harder",
        "text": "A plant is found to disperse seeds using a mechanism that costs it "
                "very little energy per seed, is completely unaffected by weather, "
                "but only ever moves seeds a few metres. Identify the method, and "
                "explain the one situation where this combination of features would "
                "be a poor strategy.",
        "options": [
            {"text": "Being flung by the plant — it would be a poor strategy "
                    "in a species that has plenty of energy to spare for "
                    "dispersal.", "correct": False,
             "why": "Having spare energy would make an expensive strategy "
                    "MORE affordable, not make this cheap, "
                    "weather-independent one a poor choice. The real weakness "
                    "is its short range."},
            {"text": "Wind dispersal — it would be a poor strategy for a plant "
                    "growing somewhere with no wind at all.", "correct": False,
             "why": "A method unaffected by weather is specifically NOT wind "
                    "dispersal, since wind dispersal depends entirely on wind "
                    "being present. This description matches being flung by "
                    "the plant instead."},
            {"text": "Water dispersal — it would be a particularly poor "
                    "strategy for a plant growing a very long way inland, "
                    "somewhere far from any river, lake or stretch of "
                    "coastline at all.", "correct": False,
             "why": "Water dispersal is heavily affected by weather and "
                    "location, unlike the method described here, which is "
                    "unaffected by weather. The description matches being "
                    "flung by the plant."},
            {"text": "Being flung by the plant — it would be a poor strategy "
                    "for a species needing to colonise new, distant habitats "
                    "quickly, since it cannot move seeds far enough.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h15",
        "band": "harder",
        "text": "Two related plant species produce seeds of identical size and "
                "weight. One has evolved hooks; the other has evolved a fleshy, sweet "
                "coating. Predict which species is likely to spend more total energy "
                "per seed on its dispersal structure, and justify your prediction.",
        "options": [
            {"text": "The fleshy-coated species, since building sugar-rich "
                    "flesh is consistently described as far more costly than "
                    "building simple hooks.", "correct": True},
            {"text": "The hooked species, since hooks need to be extremely "
                    "hard and durable to survive repeated use.", "correct": False,
             "why": "Durability of the hook material is not described as "
                    "making it the more expensive structure. Sugar-rich flesh "
                    "is consistently the more costly build of the two."},
            {"text": "Both species spend exactly the same amount of energy, "
                    "since the seeds themselves are identical in size and "
                    "weight.", "correct": False,
             "why": "Seed size and weight are a separate matter from the cost "
                    "of the surrounding dispersal structure — a hook and a "
                    "sugary coating are not equally cheap to build."},
            {"text": "It cannot be predicted without first knowing which of "
                    "the two seeds germinates more successfully.", "correct": False,
             "why": "Germination success afterwards is unrelated to which "
                    "structure was more costly to build in the first place. "
                    "The flesh-versus-hook cost difference is what decides "
                    "this."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h16",
        "band": "harder",
        "text": "A plant is observed dispersing seeds successfully in most years, but "
                "in a year with an unusually calm, windless summer, almost none of "
                "its seeds travel more than a metre. Identify the plant's likely "
                "dispersal method from this evidence, and explain your reasoning.",
        "options": [
            {"text": "Being flung by the plant — a calm summer would stop the "
                    "pods from drying out properly.", "correct": False,
             "why": "Being flung depends on the plant's own drying and "
                    "splitting, which does not require any wind at all, so a "
                    "windless summer should not affect it this way."},
            {"text": "Wind — its success varying so strongly with how windy "
                    "the summer is points directly to a method that depends "
                    "on wind being present.", "correct": True},
            {"text": "Water — a calm summer usually also brings noticeably "
                    "less rainfall with it, which would neatly explain the "
                    "unusually poor dispersal that year.", "correct": False,
             "why": "Wind calmness and rainfall are not linked in this "
                    "description, and water dispersal depends on a river, "
                    "lake or coastline being present, not on how windy the "
                    "summer was."},
            {"text": "Inside an animal — a calm summer might mean fewer "
                    "animals are active and eating fruit that year.", "correct": False,
             "why": "There is nothing in the evidence connecting animal "
                    "activity to how windy a summer is. The clue that success "
                    "tracks wind so closely points to wind dispersal "
                    "specifically."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h17",
        "band": "harder",
        "text": "A plant disperses seeds inside birds. Analysis shows the birds that "
                "eat its fruit typically fly for 20 minutes before excreting the "
                "seeds, at an average speed of 30 km per hour. Calculate the typical "
                "dispersal distance this represents.",
        "options": [
            {"text": "600 km.", "correct": False,
             "why": "That multiplies 20 (minutes) by 30 without converting "
                    "minutes to hours first. Twenty minutes is a third of an "
                    "hour, so the distance is 30 × (1/3) = 10 km, not 600."},
            {"text": "1.5 km.", "correct": False,
             "why": "That divides 30 by 20 rather than multiplying speed by "
                    "time. Twenty minutes at 30 km per hour covers 10 km."},
            {"text": "10 km.", "correct": True},
            {"text": "50 km.", "correct": False,
             "why": "That does not correspond to either number given "
                    "correctly. Twenty minutes is one third of an hour, and "
                    "one third of 30 km per hour is 10 km."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h18",
        "band": "harder",
        "text": "A bird carries a swallowed seed about 15 km before excreting it. A "
                "wind-dispersed dandelion's best case is about a kilometre. "
                "Evaluate the claim that 'inside an animal' is always the "
                "longest-range dispersal method.",
        "options": [
            {"text": "The claim is true, since being carried inside an animal "
                    "is by definition always the fastest possible method.", "correct": False,
             "why": "Speed of travel and total distance are not automatically "
                    "the greatest for every animal-dispersal case — a short "
                    "flight or a slow-moving animal could easily be beaten by "
                    "a strong wind."},
            {"text": "The claim is true, because animals can choose to travel "
                    "exactly as far as would benefit the plant most.", "correct": False,
             "why": "An animal does not choose its route or flight time based "
                    "on what would benefit the plant. Distance in this method "
                    "depends on the animal's own unrelated behaviour."},
            {"text": "The claim cannot really be evaluated at all, since two "
                    "such different dispersal methods — one a bird's flight, "
                    "the other a gust of wind — cannot meaningfully be "
                    "compared to each other in the first place.", "correct": False,
             "why": "The two distances given can be compared directly, and in "
                    "this particular case the bird did travel further — "
                    "though that would not always be true for every instance "
                    "of either method."},
            {"text": "False here: the bird carried the seed roughly fifteen times "
                    "further than the dandelion's best case — though a different bird "
                    "species or a shorter flight could easily reverse that.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h19",
        "band": "harder",
        "text": "A seed has evolved to be dispersed by a single species of large "
                "mammal that swallows the fruit whole. Predict what would most likely "
                "happen to the seed's coat over many generations if that mammal "
                "species were gradually replaced by a much smaller one with a "
                "shorter, faster gut passage.",
        "options": [
            {"text": "Selection would likely favour a coat that survives the "
                    "shorter, faster digestion of the new, smaller disperser, "
                    "whatever that specifically requires.", "correct": True},
            {"text": "The seed's coat would stay exactly the same, since coat "
                    "toughness has nothing to do with which animal disperses "
                    "it.", "correct": False,
             "why": "Coat toughness is directly linked to surviving a "
                    "particular animal's digestive process, so a change in "
                    "disperser would plausibly select for a coat suited to "
                    "the new gut."},
            {"text": "The plant would immediately stop being dispersed by any "
                    "animal and switch permanently to wind instead.", "correct": False,
             "why": "A plant cannot switch dispersal method on demand across "
                    "generations just because one disperser changes. "
                    "Selection instead favours whatever coat suits the seeds "
                    "actually being eaten."},
            {"text": "The seed would evolve to be swallowed whole by the "
                    "smaller mammal without ever being digested at all.", "correct": False,
             "why": "Avoiding digestion completely is not how this dispersal "
                    "method is described as working — the coat surviving "
                    "digestion, not escaping it, is the relevant adaptation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h20",
        "band": "harder",
        "text": "A hooked fruit and a fleshy fruit are compared for RELIABILITY of "
                "dispersal — meaning how likely a typical fruit is to actually get "
                "carried somewhere useful. Evaluate which is likely to be more "
                "reliable, and why.",
        "options": [
            {"text": "The hooked fruit, since hooks are a physically stronger "
                    "attachment than simply being swallowed.", "correct": False,
             "why": "Physical grip strength is not what determines "
                    "reliability here. An animal can groom off a hooked fruit "
                    "almost immediately, while a swallowed seed usually "
                    "travels with the animal for some time."},
            {"text": "The fleshy fruit, since an animal that has swallowed it "
                    "is far more likely to travel a meaningful distance "
                    "before releasing the seed than one that merely brushes "
                    "past a hook.", "correct": True},
            {"text": "Both are equally reliable, since both ultimately depend "
                    "on an animal being involved in some way.", "correct": False,
             "why": "Involving an animal in some way is not the same as being "
                    "equally reliable — how long and how far that animal "
                    "carries the seed differs sharply between the two "
                    "methods."},
            {"text": "The hooked fruit, because it costs the plant "
                    "considerably less energy and fewer resources to build in "
                    "the first place, which surely makes it more likely to "
                    "succeed in the end.", "correct": False,
             "why": "Cost to build is a separate issue from reliability of "
                    "the outcome. A cheap hook can still fall off very "
                    "quickly, unlike a swallowed seed that usually travels "
                    "much further first."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h21",
        "band": "harder",
        "text": "A student proposes that dispersal distance alone is the best measure "
                "of how 'successful' a dispersal method is. Using the distinction "
                "between the average distance and the long tail of a distribution, "
                "evaluate this proposal.",
        "options": [
            {"text": "The proposal is correct, since a longer average distance "
                    "always means more seedlings survive to adulthood.", "correct": False,
             "why": "Average distance travelled is not directly linked to how "
                    "many seedlings then survive — survival depends on where "
                    "those seeds land, not simply how far they moved."},
            {"text": "The proposal is correct, because the long tail of a "
                    "distribution is just noise that should be ignored when "
                    "judging success.", "correct": False,
             "why": "The long tail is specifically identified as the part of "
                    "the pattern that matters most for a species reaching new "
                    "territory — it is not noise to be dismissed."},
            {"text": "The proposal is too simple: a method's success also "
                    "depends on rare long-distance events that let a species "
                    "reach new territory, which a single average distance "
                    "figure hides.", "correct": True},
            {"text": "The proposal cannot be evaluated at all without "
                    "measuring the exact number of seeds each plant produces.", "correct": False,
             "why": "Seed number is a separate factor from what this proposal "
                    "is actually claiming, which is about distance alone "
                    "being the best measure of success — that claim can be "
                    "assessed using the average-versus-tail distinction "
                    "directly."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h22",
        "band": "harder",
        "text": "A gorse-like plant is found on a remote, permanently windless "
                "island. Predict what would most likely happen to its 'flinging' "
                "dispersal method over many generations, compared with a related "
                "gorse population living somewhere windy.",
        "options": [
            {"text": "The flinging method would gradually stop working "
                    "altogether over many generations, since every dispersal "
                    "method ultimately depends on some wind being present.", "correct": False,
             "why": "Flinging is specifically described as needing no wind, "
                    "water or animal at all — it relies entirely on the "
                    "plant's own stored energy from drying out."},
            {"text": "The plant would evolve a much longer flinging range "
                    "specifically to make up for the total lack of wind on "
                    "the island.", "correct": False,
             "why": "There is no mechanism described by which lacking wind "
                    "would directly push flinging range further. Flinging's "
                    "range is set by the plant's own stored energy, not by "
                    "compensating for wind."},
            {"text": "The plant would be completely unaffected in every way, "
                    "since wind plays no part in any dispersal method at all.", "correct": False,
             "why": "Wind is central to a different dispersal method "
                    "entirely. It is specifically flinging that does not "
                    "depend on wind, not every method equally."},
            {"text": "Little would change directly, since flinging does not "
                    "depend on wind at all — its short range would remain a "
                    "limitation on that island regardless of the wind.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h23",
        "band": "harder",
        "text": "Two dispersal structures are compared: a parachute of hairs (very "
                "cheap, very unreliable placement) and a hooked burr (very cheap, "
                "still fairly unreliable placement, but a longer average carrying "
                "time). Explain why 'cheap' alone does not make these two structures "
                "interchangeable strategies.",
        "options": [
            {"text": "Even at similar cost, the two differ in their SPREAD of "
                    "outcomes: a parachute can occasionally travel very far "
                    "on the wind, while a burr's range stays capped by its "
                    "carrying animal's own roaming.", "correct": True},
            {"text": "They actually are entirely interchangeable strategies, "
                    "since being 'cheap' to build is really the only factor "
                    "that ultimately matters at all when comparing any two "
                    "dispersal structures against one another.", "correct": False,
             "why": "Cost is only one factor among several — how far and how "
                    "reliably a structure typically moves a seed is a "
                    "separate and equally important consideration."},
            {"text": "They are not interchangeable only because hooks are "
                    "slightly more expensive to build than hairs are.", "correct": False,
             "why": "The comparison specifically states both structures are "
                    "similarly cheap. The real difference described is in "
                    "their likely range and reliability, not a hidden cost "
                    "gap."},
            {"text": "They are not interchangeable because parachutes can only "
                    "be used by plants that flower in spring.", "correct": False,
             "why": "Flowering season is not mentioned as a factor "
                    "distinguishing these two structures. The relevant "
                    "difference is in how far and how reliably each one "
                    "typically carries a seed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h24",
        "band": "harder",
        "text": "A plant's seeds are dispersed by a bird species that has recently "
                "started avoiding the plant's fruit because a new, more attractive "
                "food source has appeared nearby. Predict the most likely long-term "
                "evolutionary pressure this creates on the plant's fruit.",
        "options": [
            {"text": "None at all, since a plant's fruit cannot change in "
                    "response to what a bird happens to prefer eating.", "correct": False,
             "why": "A fruit's attractiveness — colour, sweetness, size — is "
                    "a trait that can be acted on by selection over "
                    "generations, just as any other dispersal structure "
                    "can."},
            {"text": "Selection favouring fruit that becomes more attractive "
                    "again to that bird, or to a different disperser, since "
                    "fruit nobody eats is dispersed by nobody at all.", "correct": True},
            {"text": "Selection favouring a fruit that gradually becomes toxic "
                    "to that one particular bird species, effectively "
                    "punishing it for having started to ignore the plant's "
                    "fruit.", "correct": False,
             "why": "Selection does not act to punish an animal's behaviour. "
                    "A fruit nobody eats is simply never dispersed, which "
                    "favours whatever variation makes it attractive again, "
                    "not toxic."},
            {"text": "Selection favouring the plant switching entirely to wind "
                    "dispersal within a single generation.", "correct": False,
             "why": "A plant cannot switch its whole dispersal structure "
                    "within one generation. Change of this kind happens "
                    "gradually, over many generations, in the direction of "
                    "whatever restores successful dispersal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h25",
        "band": "harder",
        "text": "A specimen combines an unusually large, heavy seed with a thin "
                "papery wing far too small to meaningfully slow its fall. Assess "
                "whether 'wind-dispersed' is a reasonable classification for this "
                "specimen.",
        "options": [
            {"text": "Reasonable — any seed with a wing of any size at all "
                    "counts as wind-dispersed by definition.", "correct": False,
             "why": "Having a wing structure is not sufficient on its own; "
                    "the wing has to actually be effective at slowing the "
                    "seed's particular weight, which this one is described as "
                    "failing to do."},
            {"text": "Reasonable — heavy seeds are, in fact, considerably "
                    "easier for wind to carry than lighter ones are, once "
                    "they have been given any wing structure at all, however "
                    "small that wing might be.", "correct": False,
             "why": "Heavier seeds are consistently harder, not easier, for "
                    "wind to move — which is exactly why an effective wing "
                    "needs to be large relative to the seed's own weight."},
            {"text": "Not reasonable as described — a wing only helps if it is "
                    "large enough, relative to the seed's weight, to "
                    "meaningfully slow the fall; a wing too small to do that "
                    "gives wind nothing to act on.", "correct": True},
            {"text": "Not reasonable, but only because papery wings are always "
                    "too fragile to survive a fall from any height.", "correct": False,
             "why": "Fragility of the material is not the issue raised here. "
                    "The problem described is the wing being too small "
                    "relative to the seed's weight to slow the fall at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h26",
        "band": "harder",
        "text": "A plant is found to disperse its seeds using two structures that "
                "both belong, structurally, to the SAME general method — for example, "
                "a fleshy layer around one seed and a slightly different fleshy layer "
                "around a second seed on the same fruit. Explain why this would NOT "
                "count as an example of a plant 'hedging its bets' across two "
                "different methods.",
        "options": [
            {"text": "It would still count as hedging bets, since any two "
                    "dispersal structures that merely look physically "
                    "different are automatically two different methods.", "correct": False,
             "why": "Looking different is not the same as working differently "
                    "— what matters is the underlying mechanism, and here "
                    "both rely on exactly the same one: an animal eating "
                    "flesh."},
            {"text": "It would still count, because the plant is clearly "
                    "spending extra resources building two separate "
                    "structures.", "correct": False,
             "why": "Extra resource spending on its own does not create a "
                    "genuine hedge against risk if both structures fail under "
                    "exactly the same conditions, as these two would."},
            {"text": "It would not count, but only because a single fruit "
                    "cannot physically hold two separate fleshy layers at "
                    "once.", "correct": False,
             "why": "The physical possibility of the arrangement is not the "
                    "reason given here. The real point is that both layers "
                    "share one underlying mechanism, so they do not spread "
                    "the plant's risk the way two different methods would."},
            {"text": "Both rely on the identical mechanism — an animal eating "
                    "flesh — so one failure would take out both, unlike "
                    "genuinely combining two different methods.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h27",
        "band": "harder",
        "text": "A researcher wants to test the claim that seed dispersal structures "
                "arose through natural selection rather than through a plant "
                "'choosing' to grow them. Suggest the single strongest type of "
                "evidence that would support natural selection over the alternative.",
        "options": [
            {"text": "Evidence of gradual variation in dispersal structures "
                    "across many generations, with better-dispersed variants "
                    "leaving more descendants over time.", "correct": True},
            {"text": "Evidence that a single individual plant grew a brand new "
                    "dispersal structure within its own lifetime.", "correct": False,
             "why": "A structure changing within one individual's lifetime "
                    "would not distinguish selection from any other process — "
                    "natural selection specifically acts across many "
                    "generations, on variation that already exists."},
            {"text": "Evidence that every individual of a species has always "
                    "had exactly the identical dispersal structure, with no "
                    "variation at all.", "correct": False,
             "why": "A total lack of variation would make it hard to show "
                    "selection acting at all, since selection needs different "
                    "variants to act upon and compare over time."},
            {"text": "Evidence that plants can sense which direction the wind "
                    "is blowing before releasing their seeds.", "correct": False,
             "why": "Sensing wind direction would not distinguish natural "
                    "selection from any alternative explanation — it says "
                    "nothing about how the structure arose across generations "
                    "in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h28",
        "band": "harder",
        "text": "A plant disperses seeds using flesh eaten by animals. A mutation "
                "makes its fruit ripen bright red a full month before the seeds "
                "inside are actually ready. Predict the most likely consequence for "
                "that mutant lineage over time.",
        "options": [
            {"text": "It would likely be strongly favoured by selection, since "
                    "ripening a full month earlier than usual lets a much "
                    "greater number of animals find and eat the fruit before "
                    "any rival plant's fruit is ready.", "correct": False,
             "why": "More animals finding the fruit does not help if the "
                    "seeds they carry away cannot then grow. Losing viable "
                    "offspring this way would count against the lineage, not "
                    "for it."},
            {"text": "It would likely be selected against, since animals "
                    "eating the unripe fruit would carry away seeds unable to "
                    "grow, reducing how many descendants that lineage leaves.", "correct": True},
            {"text": "It would have no effect at all, since ripening colour is "
                    "unrelated to whether the seeds inside can grow.", "correct": False,
             "why": "Ripening colour is a signal tied to seed "
                    "readiness — an "
                    "early, false signal would mean seeds are taken before "
                    "they are actually able to grow."},
            {"text": "It would only matter in years when animal numbers happen "
                    "to be unusually low.", "correct": False,
             "why": "The problem with an early false signal does not depend "
                    "on how many animals are around — it happens whenever an "
                    "animal is drawn to eat the fruit before the seeds are "
                    "ready, in any year."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h29",
        "band": "harder",
        "text": "Explain why comparing dispersal methods purely by average seed "
                "number produced is a weaker test of 'success' than comparing the "
                "number of seeds that survive to become adult plants.",
        "options": [
            {"text": "It is weaker only because counting seeds is technically "
                    "much harder to do accurately than counting adult plants.", "correct": False,
             "why": "Practical difficulty of counting is not the reason given "
                    "here. The issue is that raw seed number does not tell "
                    "you how many of those seeds actually succeed."},
            {"text": "It is weaker because plants that produce fewer seeds "
                    "always turn out to be more successful in every case.", "correct": False,
             "why": "There is no general rule that fewer seeds always means "
                    "more success — the point is that seed number alone, "
                    "whether high or low, does not by itself measure the "
                    "outcome that matters."},
            {"text": "A method that produces huge numbers of seeds could still "
                    "be failing badly if almost none of them ever grow into "
                    "adults, so seed number alone hides the outcome that "
                    "actually matters.", "correct": True},
            {"text": "It is weaker only for wind-dispersed plants, since every "
                    "other method already reports adult survival directly.", "correct": False,
             "why": "The problem with using raw seed number applies "
                    "generally, to any dispersal method being compared, not "
                    "specifically to wind dispersal alone."},
        ],
        "figure": None,
    },
    {
        "id": "b5-08-h30",
        "band": "harder",
        "text": "Draw together the ideas of cost, reliability and the long tail of a "
                "distribution to explain why 'inside an animal' can be the most "
                "expensive dispersal method to build and still be widespread among "
                "plants.",
        "options": [
            {"text": "It is widespread purely because animals are extremely "
                    "common in almost every habitat on Earth.", "correct": False,
             "why": "Animal abundance alone does not explain why plants would "
                    "evolve such an expensive structure — the method has to "
                    "actually pay for itself through the quality, not just "
                    "the availability, of the dispersal it achieves."},
            {"text": "It is widespread because it is actually the cheapest "
                    "method of all, once the full cost of building an "
                    "equivalent parachute or wing is properly and fairly "
                    "accounted for.", "correct": False,
             "why": "Building sugar-rich flesh is consistently described as "
                    "more expensive than a parachute or wing, not cheaper. "
                    "Its widespread use is explained by what that cost buys, "
                    "not by it being secretly cheap."},
            {"text": "It is widespread only in species that have stopped using "
                    "any other dispersal method entirely.", "correct": False,
             "why": "Many species combine this method with others rather than "
                    "relying on it exclusively. Its being widespread is "
                    "explained by the reliability it buys for its cost, not "
                    "by other methods being abandoned."},
            {"text": "Its high cost is repaid by unusually reliable delivery — "
                    "a real chance of landing in the valuable long tail — "
                    "rather than existing despite being expensive.", "correct": True},
        ],
        "figure": None,
    },
]
