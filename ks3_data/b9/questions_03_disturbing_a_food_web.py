"""B9 lesson 03 — Disturbing a food web: twelve questions (MRB-269).

The lesson makes one claim and makes it six times at the bench: an effect
travels along every route out of a missing species, the routes that matter are
often sideways, and they arrive late. These twelve probe that claim rather than
the wood's cast list — the four words the page adds (specialist, generalist,
top predator, interdependence), the removals the ladder does not already own
(the caterpillars, the bees, the oak), the three rule cards applied rather than
recited, and, in the harder band, the same rules carried into Yellowstone, a
heath under monitoring and a grassland the lesson never draws.

Distractors are built from the lesson's two declared misconceptions — `ECO-05`
"removing a species only affects the things directly above and below it", which
supplies the sparrowhawks-never-touched-a-caterpillar option, the
no-animal-eats-bees option and the effects-travel-upwards option, and `ECO-06`
"if it goes wrong, you just put the species back", which supplies the
always-works and no-check-needed options — plus three beliefs the page argues
against without filing: that a species nothing eats has no connections, that a
web with more connections is more fragile rather than steadier, and that
pollination is what keeps a grown plant alive.

Rungs 1 and 2 own the ladybird removal's immediate effect and the owl removal's
unpredicted species; rungs 3 and 4 own the blue-tit trace and the insecticide
prediction. None of the four is restated here. ⛔ Nothing below introduces a
river, a stream or an aquatic example — that is the NOTES-B9 flag 8 ruling and
it binds the questions as much as the page.
"""

UNIT = "B9"
LESSON = "disturbing-a-food-web"
LESSON_NUMBER = 3

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-03-e01",
        "band": "easier",
        "text": "Ladybirds in this wood eat aphids, and nothing else. Which "
                "word describes an organism like that?",
        "options": [
            {"text": "A generalist", "correct": False,
             "why": "A generalist feeds on many different things — a blue tit "
                    "here takes both caterpillars and aphids. Losing one food "
                    "barely registers for it. That is the opposite of a "
                    "ladybird."},
            {"text": "A specialist", "correct": True},
            {"text": "A top predator", "correct": False,
             "why": "A top predator is an animal with nothing that hunts it, "
                    "like the sparrowhawk. Ladybirds are eaten, and the word "
                    "describes what hunts an animal rather than what it eats."},
            {"text": "A decomposer", "correct": False,
             "why": "The decomposers here are the fungi and bacteria that "
                    "break down everything that dies. A ladybird hunts living "
                    "aphids."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e02",
        "band": "easier",
        "text": "Use the web. Which animal in this wood feeds on only one "
                "thing?",
        "options": [
            {"text": "The ladybirds", "correct": True},
            {"text": "The blue tits", "correct": False,
             "why": "Blue tits eat caterpillars and aphids — two arrows into "
                    "them. Having a second route is exactly what lets them "
                    "switch when one food runs short."},
            {"text": "The mice", "correct": False,
             "why": "Mice eat acorns and seeds from the wildflowers, so they "
                    "have two food sources. That is why both the oak and the "
                    "bees can reach them."},
            {"text": "The sparrowhawks", "correct": False,
             "why": "Sparrowhawks eat blue tits mainly and mice when they "
                    "must. That second route is what squeezes the owls out "
                    "when blue tits go."},
        ],
        "figure": "b9-oak-wood-web",
    },
    {
        "id": "b9-03-e03",
        "band": "easier",
        "text": "Rule three says effects are delayed. What does that mean for "
                "anyone watching a wood after a removal?",
        "options": [
            {"text": "Populations bounce back once a single season has "
                     "passed, so a year is plenty",
             "correct": False,
             "why": "That is the rule turned upside down. A year is often "
                    "before the effect has arrived, not after it has cleared."},
            {"text": "Only the fastest-breeding species change, so the rest "
                     "of the wood stays as it was",
             "correct": False,
             "why": "Aphids do respond fastest, but the rule is about timing, "
                    "not about which species respond. The owls change too — "
                    "several seasons later."},
            {"text": "The effect turns up in a different part of the wood "
                     "rather than later in time",
             "correct": False,
             "why": "That is rule one, effects travelling sideways. Rule "
                    "three is about time: the same effect, arriving long "
                    "after the removal."},
            {"text": "The response takes seasons or years, so damage "
                     "appears once people stop watching",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e04",
        "band": "easier",
        "text": "The bench has a button labelled “Put it back”. In a "
                "real ecosystem, how well does putting a species back work?",
        "options": [
            {"text": "It always works, because it is the same species going "
                     "back into the same wood",
             "correct": False,
             "why": "The wood you put it back into is not the wood it left. "
                    "While it was gone another organism may have moved into "
                    "the space, or the plants it fed on may have died out."},
            {"text": "It never works, so no removal anywhere can ever be "
                     "undone",
             "correct": False,
             "why": "Too strong the other way. Reintroduction sometimes "
                    "succeeds — Yellowstone's wolves did. The point is that "
                    "it is unreliable, not that it is impossible."},
            {"text": "Sometimes it works, but it is slow, costly and often "
                     "incomplete",
             "correct": True},
            {"text": "It works as long as you do it before the next breeding "
                     "season",
             "correct": False,
             "why": "There is no safe window. What decides it is whether the "
                    "ecosystem has rearranged itself and whether a source "
                    "population still exists at all."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-03-s01",
        "band": "standard",
        "text": "A gardener removes every caterpillar from the wood. The oak "
                "grows better for one season. What happens after that?",
        "options": [
            {"text": "The oak keeps improving, because the insect eating its "
                     "leaves has gone for good",
             "correct": False,
             "why": "That one season is the whole of the gain. Removing a "
                    "pest is not the same as solving a problem — the tree "
                    "then loses the birds that were protecting it from "
                    "something else."},
            {"text": "Ladybirds die out, because caterpillars were the food "
                     "they depended on",
             "correct": False,
             "why": "Ladybirds eat aphids, and nothing else. With fewer blue "
                    "tits about, aphids increase and the ladybirds do rather "
                    "well."},
            {"text": "Blue tits lose what they feed their chicks on, their "
                     "numbers fall, and aphids increase",
             "correct": True},
            {"text": "Sparrowhawks are unaffected, because they eat blue tits "
                     "and never touched a caterpillar",
             "correct": False,
             "why": "That is the chain talking. Fewer blue tits means "
                    "sparrowhawks turn to mice, and the owls lose out — three "
                    "species away from a caterpillar."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s02",
        "band": "standard",
        "text": "Two woods. In one, the owls eat mice only. In the other, "
                "owls eat mice, voles, shrews and young rabbits. A disease "
                "wipes out the mice in both. Which owls are in more trouble?",
        "options": [
            {"text": "The first wood's owls, because a specialist has nothing "
                     "to fall back on",
             "correct": True},
            {"text": "The second wood's owls, because more feeding routes "
                     "means more ways to be affected",
             "correct": False,
             "why": "That is the connected-means-fragile idea, and rule two "
                    "says the opposite. Alternative routes absorb a shock: a "
                    "predator that eats four things barely notices losing "
                    "one."},
            {"text": "Both equally, because each wood has lost exactly one "
                     "species out of its web",
             "correct": False,
             "why": "Counting the species lost is not the measure. What "
                    "matters is how many routes to food the survivors still "
                    "have."},
            {"text": "Neither, because owls are top predators and nothing can "
                     "reach them",
             "correct": False,
             "why": "Nothing hunts an owl, but plenty holds one up. A top "
                    "predator is reached from below, through what it eats."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s03",
        "band": "standard",
        "text": "The bees are removed in spring. A year later a student sees "
                "the wildflowers still standing and writes: “No change — "
                "the bees clearly did not matter.” What is wrong with "
                "that?",
        "options": [
            {"text": "Nothing is wrong — an insect with no feeding line "
                     "cannot affect a web",
             "correct": False,
             "why": "The bees are in no food chain here and their removal "
                    "still empties the web. Feeding is not the only kind of "
                    "dependence."},
            {"text": "The flowers are grown already, but they set almost "
                     "no seed, so few will follow",
             "correct": True},
            {"text": "The wildflowers should have wilted within days, so the "
                     "student has misread the wood",
             "correct": False,
             "why": "Pollination is how the flowers make seed, not how a "
                    "grown plant stays alive. The plants standing there are "
                    "fine; their offspring are the problem."},
            {"text": "The blue tits would have gone hungry at once, having "
                     "lost the bees they eat",
             "correct": False,
             "why": "Nothing in this wood eats the bees. That is exactly what "
                    "makes them the sharpest case on the page."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s04",
        "band": "standard",
        "text": "Kill every ladybird and the oak comes under attack from two "
                "directions at once. Which two?",
        "options": [
            {"text": "Caterpillars eating leaves and mice stripping the "
                     "acorns",
             "correct": False,
             "why": "Mice eat acorns that have already fallen, so they are "
                    "not what damages a growing tree — and in this story "
                    "mouse numbers fall, because the stressed oak makes fewer "
                    "acorns."},
            {"text": "Aphids draining sap and bees no longer pollinating the "
                     "oak",
             "correct": False,
             "why": "The bees pollinate the wildflowers. That is the only "
                    "line they have in this web, and it does not run to the "
                    "oak."},
            {"text": "Blue tits stripping the leaves while aphids drain the "
                     "sap",
             "correct": False,
             "why": "Blue tits eat insects, not leaves. They are in the story "
                    "because they switch to the easy aphids and stop taking "
                    "caterpillars."},
            {"text": "Aphids draining sap and caterpillars eating leaves",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-03-h01",
        "band": "harder",
        "text": "Wolves were returned to Yellowstone in 1995 and willow began "
                "growing back. A wolf has never eaten willow. What joined the "
                "two?",
        "options": [
            {"text": "The wolves fertilised the ground where they made their "
                     "kills, and willow grew on it",
             "correct": False,
             "why": "The route runs through what the elk did, not through "
                    "what the wolves left behind. A web joins organisms by "
                    "feeding and by behaviour, not by fertiliser."},
            {"text": "Elk numbers fell and elk stopped feeding in the open, "
                     "so willow was browsed less",
             "correct": True},
            {"text": "The wolves drove out the beavers, which had been "
                     "felling all the willow",
             "correct": False,
             "why": "The beavers came back after the willow recovered, not "
                    "before it. You have the chain running the wrong way "
                    "along its last link."},
            {"text": "The elk were wiped out completely, so nothing was left "
                     "to browse the willow",
             "correct": False,
             "why": "Elk numbers fell and elk behaviour changed; they were "
                    "not eliminated. A predator changes where its prey feeds "
                    "as much as how many of them there are."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h02",
        "band": "harder",
        "text": "A team removes an invasive species from a heath, watches for "
                "a year, sees no other change, and calls the job safe. What "
                "is the strongest reason to doubt them?",
        "options": [
            {"text": "There is nothing to doubt — a year with no change means "
                     "the removal was clean",
             "correct": False,
             "why": "Populations take seasons or years to respond. A year of "
                    "watching can easily end before the effect has arrived at "
                    "all."},
            {"text": "The removal was safe anyway, because nothing on the "
                     "heath ate the invader, so no link broke",
             "correct": False,
             "why": "What eats a species is only half of its connections. The "
                    "bees in the oak wood are eaten by nothing, and removing "
                    "them still empties it."},
            {"text": "There is nothing to doubt, and anything that does go "
                     "wrong can be put right later",
             "correct": False,
             "why": "That is the second wrong idea on this page. Putting a "
                    "species back is expensive, slow and often only partly "
                    "successful — and the heath has moved on meanwhile."},
            {"text": "A year may end before the effect arrives, and in a part "
                     "of the web nobody was watching",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h03",
        "band": "harder",
        "text": "Five of the removals left the wood reorganised. Removing the "
                "oak did something different in kind. What?",
        "options": [
            {"text": "Removing the producer removes the energy itself, and "
                     "no other producer replaces it",
             "correct": True},
            {"text": "The oak is the largest organism there, so more "
                     "organisms fall with it",
             "correct": False,
             "why": "Size is not what makes a producer different. The "
                    "wildflowers are small and do the same job — there is "
                    "simply not enough of them to hold a wood up."},
            {"text": "Nothing is different — every removal leaves the wood "
                     "one species short",
             "correct": False,
             "why": "Counting species misses it. The other five moved the "
                    "wood's energy around; this one took the supply away, so "
                    "the web empties instead of reorganising."},
            {"text": "The oak had the most feeding lines, so the web had "
                     "the most alternative routes to absorb the shock",
             "correct": False,
             "why": "Alternative routes belong to the survivors, not to the "
                    "species that has gone. Losing the thing everything runs "
                    "on is the one loss a web cannot absorb."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h04",
        "band": "harder",
        "text": "A grassland: hawks eat voles, voles eat wildflower seed, and "
                "bees pollinate the wildflowers. Nothing eats the bees. The "
                "bees are removed. What should you predict?",
        "options": [
            {"text": "Nothing changes, because no animal in this grassland "
                     "feeds on bees",
             "correct": False,
             "why": "The oak wood already answered this. Its bees were eaten "
                    "by nothing and their removal still emptied the web — a "
                    "service is a dependence too."},
            {"text": "The wildflowers die within weeks, and the voles starve "
                     "the same summer",
             "correct": False,
             "why": "Two errors of timing. Pollination sets seed rather than "
                    "keeping grown plants alive, and effects like this take "
                    "seasons rather than weeks."},
            {"text": "Fewer seeds are set, so vole numbers fall later and the "
                     "hawks with them",
             "correct": True},
            {"text": "The hawks are hit first, because effects in a web "
                     "always travel upwards",
             "correct": False,
             "why": "Effects travel along every route out of the gap, and "
                    "this one starts at the plants. The hawks come last in "
                    "the story, not first."},
        ],
        "figure": None,
    },
]
