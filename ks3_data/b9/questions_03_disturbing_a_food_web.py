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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-03-e05",
        "band": "easier",
        "text": "What does interdependence mean?",
        "options": [
            {"text": "Organisms competing with one another for the same food "
                     "in an ecosystem.", "correct": False,
             "why": "Competition is one kind of link between organisms. "
                    "Interdependence is the wider fact that a change in one "
                    "changes the others."},
            {"text": "Organisms depending on one another, so that a change in "
                     "one changes the others.", "correct": True},
            {"text": "Organisms depending on the weather and the soil of the "
                     "place they live in.", "correct": False,
             "why": "Those matter too, and interdependence is about organisms "
                    "depending on each other — including on ones they never "
                    "touch."},
            {"text": "One organism eating another, which is what joins an "
                     "ecosystem together.", "correct": False,
             "why": "Feeding is the commonest link and it is not the only "
                    "one. Bees that eat nothing in a wood can still hold that "
                    "wood up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e06",
        "band": "easier",
        "text": "What does the word generalist mean?",
        "options": [
            {"text": "An organism that eats a very large amount of food each "
                     "day.", "correct": False,
             "why": "How much it eats is not the point. A generalist eats "
                    "many different things, whatever the quantity."},
            {"text": "An organism that lives in many different habitats "
                     "rather than one.", "correct": False,
             "why": "That is a wide range, which is a different idea. A "
                    "generalist is described by the number of foods it "
                    "eats."},
            {"text": "An organism that depends on one food and has nothing to "
                     "fall back on.", "correct": False,
             "why": "That is a specialist, the opposite. A specialist is the "
                    "one with most to lose when a food disappears."},
            {"text": "An organism that feeds on many different things rather "
                     "than on one.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e07",
        "band": "easier",
        "text": "What is a top predator?",
        "options": [
            {"text": "An animal at the top of a web, with nothing that hunts "
                     "it.", "correct": True},
            {"text": "The largest and strongest animal in an ecosystem.",
             "correct": False,
             "why": "Size does not decide it. A ladybird is a predator of "
                    "aphids, and plenty of top predators are smaller than "
                    "animals below them."},
            {"text": "An animal that eats only other predators and never a "
                     "plant eater.", "correct": False,
             "why": "Many top predators take plant eaters — an owl eats mice. "
                    "What puts it at the top is that nothing hunts it."},
            {"text": "An animal that nothing depends on, because it is at the "
                     "end of every chain.", "correct": False,
             "why": "Nothing eats it, and a great deal still depends on it. "
                    "Removing a top predator is often the change that travels "
                    "furthest."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e08",
        "band": "easier",
        "text": "In a wood, ladybirds eat aphids, blue tits eat caterpillars "
                "and aphids, owls eat mice, and bees pollinate the "
                "wildflowers. Which organism is joined to the wood by "
                "something other than a feeding link?",
        "options": [
            {"text": "The owls, because nothing in the wood eats them.",
             "correct": False,
             "why": "Nothing eating them is still a feeding link — the arrow "
                    "running into an owl from a mouse. The owls are in the "
                    "web the ordinary way."},
            {"text": "The ladybirds, because they eat only one thing.",
             "correct": False,
             "why": "One food is still a feeding link, and a narrow one. "
                    "Eating a single thing makes the ladybirds a specialist, "
                    "not an outsider."},
            {"text": "The bees, joined to the wildflowers by pollination "
                     "rather than by eating.", "correct": True},
            {"text": "None of them, because every organism in a web is joined "
                     "to it by feeding.", "correct": False,
             "why": "Pollination is the exception this wood is drawn to show. "
                    "The bees are in no food chain here, and removing them "
                    "would still empty the wood."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e09",
        "band": "easier",
        "text": "Removing one species from a wood changed the numbers of "
                "seven other species, most of which never touched it. Which "
                "statement does that support?",
        "options": [
            {"text": "Only the species directly above and below a removal are "
                     "affected by it.", "correct": False,
             "why": "Seven species changed and most had no direct link. That "
                    "is exactly the belief this result contradicts."},
            {"text": "A food web is really a set of separate chains that do "
                     "not affect one another.", "correct": False,
             "why": "If the chains were separate the effect could not have "
                    "reached seven species. They share their members, which "
                    "is what makes a web a web."},
            {"text": "Removing a species always damages an ecosystem beyond "
                     "repair.", "correct": False,
             "why": "Seven species changed, which is not the same as ruining "
                    "the wood. The point is how far the effect travelled, not "
                    "how bad it was."},
            {"text": "Every organism in a web is connected to every other by "
                     "some route.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-03-s05",
        "band": "standard",
        "text": "Sea otters eat sea urchins, and sea urchins graze the kelp "
                "that forms underwater forests. Otters are hunted out of a "
                "bay. What happens?",
        "options": [
            {"text": "The urchins fall as well, because otters and urchins "
                     "depend on one another.", "correct": False,
             "why": "Depending on one another does not mean rising and "
                    "falling together. With their predator gone, the urchins "
                    "are released and their numbers climb."},
            {"text": "The kelp grows better, because there is one fewer "
                     "animal in the bay.", "correct": False,
             "why": "The animal removed was the one holding the urchins down. "
                    "More urchins means more grazing, so the kelp does "
                    "worse."},
            {"text": "The urchins increase and graze the kelp away, so the "
                     "forest thins.", "correct": True},
            {"text": "Nothing changes, because otters do not eat kelp and are "
                     "not part of that chain.", "correct": False,
             "why": "They are joined to the kelp through the urchins, and two "
                    "links is quite enough. An effect does not stop at the "
                    "organisms you would draw a line to."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s06",
        "band": "standard",
        "text": "In a lake, perch eat sticklebacks, sticklebacks eat water "
                "fleas, and water fleas graze the algae that turn the water "
                "green. Anglers remove most of the perch. What happens to the "
                "algae?",
        "options": [
            {"text": "The algae increase, because more sticklebacks means "
                     "fewer water fleas grazing them.", "correct": True},
            {"text": "The algae decrease, because removing a predator lets "
                     "every level below it rise.", "correct": False,
             "why": "The levels do not all rise together. Each step reverses "
                    "the effect: more sticklebacks, fewer water fleas, and so "
                    "more algae."},
            {"text": "The algae are unaffected, because perch do not eat "
                     "algae.", "correct": False,
             "why": "The perch are joined to the algae through two other "
                    "species. Three links is a long way and the effect still "
                    "arrives."},
            {"text": "The algae increase, because the dead perch rot and feed "
                     "them.", "correct": False,
             "why": "The perch were removed rather than left to rot. The "
                    "route that matters here runs through the sticklebacks "
                    "and the water fleas."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s07",
        "band": "standard",
        "text": "Rats reach an island where seabirds nest on the ground and "
                "have never had a predator. Twenty years later the colony has "
                "collapsed, and the plants that grew on soil enriched by the "
                "birds' droppings are thinner too. What does that show?",
        "options": [
            {"text": "That the rats must have eaten the plants as well as the "
                     "birds' eggs.", "correct": False,
             "why": "They may have taken some seed, and the plants would have "
                    "thinned in any case. Their soil was being fed by the "
                    "seabirds, and the seabirds have gone."},
            {"text": "That an effect travelled from a predator to plants it "
                     "never touched, by way of the birds.", "correct": True},
            {"text": "That plants and seabirds compete, so losing the birds "
                     "should have helped the plants.", "correct": False,
             "why": "The birds were not competing with the plants; they were "
                    "supplying them. Losing them cost the plants their source "
                    "of minerals."},
            {"text": "That this web was unusually fragile, since a healthy "
                     "web is not changed by one new species.", "correct": False,
             "why": "A web with few alternative routes is more easily "
                    "changed, and no web is unaffected. Adding a predator "
                    "where there was none is a large disturbance anywhere."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s08",
        "band": "standard",
        "text": "Beavers fell willow and build dams, and the ponds behind "
                "those dams hold fish, frogs and dragonflies. Trappers remove "
                "every beaver from a valley, the dams break up and the ponds "
                "drain. Which statement describes what has happened?",
        "options": [
            {"text": "Nothing important, since the pond species neither ate "
                     "beavers nor were eaten by them.", "correct": False,
             "why": "Not one of them had a feeding link to a beaver, and all "
                    "of them depended on it. Feeding is not the only kind of "
                    "dependence."},
            {"text": "The willow recovers, so the valley ends up richer than "
                     "it was before.", "correct": False,
             "why": "The willow does grow back and the ponds do not. What the "
                    "valley loses is every species that lived in the water "
                    "those dams held."},
            {"text": "The frogs and dragonflies simply move to the river, so "
                     "nothing is lost.", "correct": False,
             "why": "Still water and running water are not the same habitat. "
                    "The animals that needed ponds have lost them."},
            {"text": "Removing one species removed the habitat several others "
                     "depended on.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s09",
        "band": "standard",
        "text": "Conservation groups usually protect a whole habitat rather "
                "than a single species. Which reason best explains why?",
        "options": [
            {"text": "Because a habitat is easier to fence off and look after "
                     "than an animal is.", "correct": False,
             "why": "It may well be, and that is a practical point rather "
                    "than a biological one. The reason here is that a species "
                    "cannot be kept without what it depends on."},
            {"text": "Because every species depends on others through routes "
                     "that are easy to miss.", "correct": True},
            {"text": "Because a habitat holds more species, so protecting it "
                     "saves a larger number of them.", "correct": False,
             "why": "It does save more, and that is not why a single-species "
                    "plan fails. It fails because the one species still needs "
                    "everything it was joined to."},
            {"text": "Because a species that has been protected can always be "
                     "put back into a habitat later.", "correct": False,
             "why": "Putting a species back is the one thing that cannot be "
                    "relied on. That is an argument for not losing it in the "
                    "first place."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-03-h05",
        "band": "harder",
        "text": "Cane toads were released in Queensland in 1935 to eat a "
                "beetle damaging the sugar cane. The beetles were barely "
                "affected, and the toads spread widely, poisoning the snakes "
                "and lizards that tried to eat them. What does the case "
                "show?",
        "options": [
            {"text": "That a species introduced to control a pest will always "
                     "fail to control it.", "correct": False,
             "why": "Some biological controls work well. What cannot be "
                    "assumed is that the new species will only do the job it "
                    "was brought for."},
            {"text": "That the toads were the wrong choice, and a different "
                     "predator would have worked.", "correct": False,
             "why": "A different predator would also arrive with links of its "
                    "own. The problem is what an introduction does beyond "
                    "its target, not which one you choose."},
            {"text": "That a species added to a web makes its own links, "
                     "including ones nobody predicted.", "correct": True},
            {"text": "That the beetles must already have had another predator "
                     "keeping them in check.", "correct": False,
             "why": "Nothing in the case says so, and the beetles went on "
                    "damaging the crop. What the toads did was make new "
                    "connections of their own."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h06",
        "band": "harder",
        "text": "Krill graze the algae of the Southern Ocean, and whales, "
                "seals, penguins and many fish all feed on them. Why would a "
                "heavy krill fishery worry ecologists more than the loss of "
                "one whale species?",
        "options": [
            {"text": "Because krill are producers, and removing a producer "
                     "empties a web.", "correct": False,
             "why": "Krill eat algae, so they are consumers. What makes them "
                    "matter so much is how many species feed on them, not "
                    "where the energy enters."},
            {"text": "Because krill are small, and small animals are more "
                     "easily fished out than large ones.", "correct": False,
             "why": "How easily they are caught is a fishing question. What "
                    "matters here is how much of the web runs through them."},
            {"text": "Because whales are protected already, so their loss is "
                     "unlikely to happen.", "correct": False,
             "why": "Protection is not the reason. Even if a whale species "
                    "were lost, few species feed on whales, while almost "
                    "everything feeds on krill."},
            {"text": "Because almost everything in that web feeds on krill, "
                     "with little else to switch to.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h07",
        "band": "harder",
        "text": "A farmer takes out the hedges between his fields to make "
                "them larger. Two summers later his crop has a worse aphid "
                "problem than before, although he has changed nothing else. "
                "What is the best explanation?",
        "options": [
            {"text": "The hedges held the ladybirds and birds that ate the "
                     "aphids, so their predators went with them.",
             "correct": True},
            {"text": "Aphids breed faster in a large field than in a small "
                     "one, so the bigger fields suit them.", "correct": False,
             "why": "Field size does not change how fast an aphid breeds. "
                    "What changed is what was living in the hedges and eating "
                    "them."},
            {"text": "The hedges sheltered the crop from wind, and a "
                     "wind-blown crop attracts more aphids.", "correct": False,
             "why": "Shelter affects the crop and does not explain a rise in "
                    "aphids. Something that was eating them has gone."},
            {"text": "The aphids were living in the hedges, so cutting them "
                     "released the aphids into the crop.", "correct": False,
             "why": "Aphids feed on the crop, which is where they already "
                    "were. It was their predators that needed the hedge."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h08",
        "band": "harder",
        "text": "A wood with many alternative feeding routes absorbs the loss "
                "of one species with little visible change. Does that mean it "
                "is safe from disturbance?",
        "options": [
            {"text": "Yes — a web with many routes always has an alternative, "
                     "so little that happens to it matters.", "correct": False,
             "why": "Alternatives help when the loss is one consumer among "
                    "many. They do not help when what is lost is the producer "
                    "everything runs on."},
            {"text": "No — a loss at the bottom, or of something with no "
                     "alternative, still runs right through it.",
             "correct": True},
            {"text": "No, because every removal damages a web equally, "
                     "however many routes it has.", "correct": False,
             "why": "They are not equal, which is the whole point of counting "
                    "routes. A generalist barely notices losing one food; a "
                    "specialist does not survive it."},
            {"text": "Yes, as long as no species in it is a specialist, since "
                     "specialists are the only weak point.", "correct": False,
             "why": "Specialists are one weak point and not the only one. "
                    "Remove the producer and the alternatives above it have "
                    "nothing left to be alternatives to."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h09",
        "band": "harder",
        "text": "On a moor, hen harriers eat voles and also take red grouse. "
                "A wet winter crashes the vole population. What happens to "
                "the grouse, and why is it surprising?",
        "options": [
            {"text": "Grouse numbers rise, because the harriers are weakened "
                     "by losing their main food.", "correct": False,
             "why": "A hungry predator hunts harder rather than less. The "
                    "grouse are what the harriers turn to."},
            {"text": "Grouse numbers are unchanged, because nothing has "
                     "happened to the grouse or to what they eat.",
             "correct": False,
             "why": "Nothing happened to them directly, which is what makes "
                    "it surprising. The effect reaches them through the "
                    "predator they share with the voles."},
            {"text": "Grouse numbers fall, because the harriers switch to "
                     "them — an effect through a shared predator.",
             "correct": True},
            {"text": "Grouse numbers fall, because whatever killed the voles "
                     "must have killed grouse chicks too.", "correct": False,
             "why": "A wet winter may do some of that, and the route that "
                    "matters here is the predator. Losing one prey species "
                    "pushes a predator onto another."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · easier ─────────────────────────────────────────
    {
        "id": "b9-03-e10",
        "band": "easier",
        "text": "A garden web: blackfly feed on the bean plants, ladybirds "
                "eat blackfly, and sparrows eat blackfly and caterpillars. "
                "What do the sparrows feed on?",
        "options": [
            {"text": "Blackfly and caterpillars", "correct": True},
            {"text": "Blackfly and ladybirds", "correct": False,
             "why": "Nothing gives the sparrows ladybirds. The two foods they "
                    "take are named in the question."},
            {"text": "Bean leaves and caterpillars", "correct": False,
             "why": "Sparrows are not given leaves here. Only the blackfly "
                    "feed on the bean plants."},
            {"text": "Ladybirds and bean leaves", "correct": False,
             "why": "Neither is on the sparrows' list. Read the two foods the "
                    "question hands them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e11",
        "band": "easier",
        "text": "In an oak wood, mice eat acorns and wildflower seeds, owls "
                "eat mice, and sparrowhawks eat blue tits and take mice when "
                "they must. What feeds on the mice?",
        "options": [
            {"text": "The blue tits, which take small mammals in early spring",
             "correct": False,
             "why": "Blue tits are named here as prey of the sparrowhawk. "
                    "Nothing gives them mice to eat."},
            {"text": "The owls, and the sparrowhawks when they must",
             "correct": True},
            {"text": "The owls, and nothing whatever besides", "correct": False,
             "why": "The sparrowhawks are given mice too, as a second choice. "
                    "That second link is what makes this a web."},
            {"text": "The acorns and the wildflower seeds", "correct": False,
             "why": "Those are what the mice EAT. The arrows run the other "
                    "way for the question being asked."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e12",
        "band": "easier",
        "text": "One of the rules of disturbing a web says that effects "
                "travel sideways. What does that mean?",
        "options": [
            {"text": "The effect spreads to woods on either side of the one "
                     "it started in", "correct": False,
             "why": "Sideways means sideways through the WEB, not across the "
                    "countryside."},
            {"text": "The species most affected is often a competitor, or "
                     "something that shared a predator", "correct": True},
            {"text": "The effect moves down to the plants and then stops "
                     "there", "correct": False,
             "why": "Reaching the plants is travelling DOWN, and the effect "
                    "does not stop when it gets there."},
            {"text": "The effect is felt by all species at that level",
             "correct": False,
             "why": "It is felt by whatever is linked, at any level. Sharing "
                    "a level does not make two species linked."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e13",
        "band": "easier",
        "text": "A rule of webs says that a web with more connections in it "
                "is steadier. Why should that be?",
        "options": [
            {"text": "Because a predator that eats six things barely notices "
                     "losing one", "correct": True},
            {"text": "Because more connections mean more species, and more "
                         "species will always survive it", "correct": False,
             "why": "Numbers of species do not protect anything by "
                    "themselves. It is the alternatives each one has."},
            {"text": "Because the arrows share the effect out so that nobody "
                     "feels it", "correct": False,
             "why": "Somebody always feels it. What alternatives do is give a "
                    "species somewhere else to turn."},
            {"text": "Because a crowded web leaves no room for a change to "
                     "travel through", "correct": False,
             "why": "Connections are routes, so more of them means more ways "
                    "for an effect to travel, not fewer."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e14",
        "band": "easier",
        "text": "Wildflowers that are never visited by a pollinating insect "
                "still stand through the summer. What do they fail to do?",
        "options": [
            {"text": "Take up water", "correct": False,
             "why": "Roots work whether or not an insect visits. Pollination "
                    "is about the next generation."},
            {"text": "Grow taller", "correct": False,
             "why": "They grow normally. What is missing appears only when "
                    "the next year's plants should come up."},
            {"text": "Set seed", "correct": True},
            {"text": "Photosynthesise", "correct": False,
             "why": "Photosynthesis needs light, not insects. The plants feed "
                    "themselves perfectly well."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e15",
        "band": "easier",
        "text": "In an oak wood, sparrowhawks eat blue tits and mice, owls "
                "eat mice, and nothing hunts the sparrowhawks. Which organism "
                "is the top predator?",
        "options": [
            {"text": "The owls", "correct": False,
             "why": "Owls are hunted by nothing here either, and they are not "
                    "the highest — the question says nothing hunts the hawk."},
            {"text": "The mice",
             "correct": False,
             "why": "Being depended on is not being at the top. Mice are "
                    "prey to two predators."},
            {"text": "The blue tits",
             "correct": False,
             "why": "Blue tits are eaten by sparrowhawks, so something hunts "
                    "them."},
            {"text": "The sparrowhawks", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e16",
        "band": "easier",
        "text": "Wolves were returned to Yellowstone National Park in 1995. "
                "What happened to the elk there?",
        "options": [
            {"text": "Their numbers fell, and they stopped feeding in the "
                     "open valley bottoms", "correct": True},
            {"text": "Their numbers rose, because the wolves kept disease out "
                         "of the elk herds", "correct": False,
             "why": "Numbers fell. A predator that hunts a herd does not "
                    "increase it."},
            {"text": "Nothing changed, because elk are far too large for "
                     "wolves to hunt", "correct": False,
             "why": "Wolves hunt elk in packs, and the elk changed both their "
                    "numbers and their behaviour."},
            {"text": "They left the park entirely within the first year",
             "correct": False,
             "why": "They stayed. What changed was where inside the park they "
                    "would risk feeding."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e17",
        "band": "easier",
        "text": "After the wolves returned to Yellowstone, two kinds of plant "
                "began growing back where the elk had browsed them hardest. "
                "Which plants were they?",
        "options": [
            {"text": "Grasses and mosses", "correct": False,
             "why": "Elk graze grass and it was not the plant that recovered "
                    "notably. The change was in the taller browse."},
            {"text": "Oaks and hawthorns", "correct": False,
             "why": "Those are British woodland trees. Yellowstone's recovery "
                    "was in different species."},
            {"text": "Willow and aspen", "correct": True},
            {"text": "Wheat and barley", "correct": False,
             "why": "Those are farm crops. Nothing was being grown in a "
                    "national park."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e18",
        "band": "easier",
        "text": "Beavers returned to parts of Yellowstone after the wolves "
                "did. What had come back that the beavers needed?",
        "options": [
            {"text": "The elk", "correct": False,
             "why": "Beavers are plant-eaters. An elk is neither their food "
                    "nor their building material."},
            {"text": "The willow", "correct": True},
            {"text": "The wolves", "correct": False,
             "why": "Wolves protect nothing deliberately. What reached the "
                    "beavers was a plant, by way of the elk."},
            {"text": "The grass", "correct": False,
             "why": "Beavers build with wood. It was the willow's return that "
                    "made the difference."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e19",
        "band": "easier",
        "text": "A teaching web of a wood shows eleven organisms. About how "
                "many does a real woodland web contain?",
        "options": [
            {"text": "Hundreds", "correct": True},
            {"text": "Eleven, which is exactly why the teaching web uses that "
                         "number",
             "correct": False,
             "why": "Eleven is chosen so the picture can be read. A real wood "
                    "holds far more than that."},
            {"text": "Two or three, once the rare ones are left out",
             "correct": False,
             "why": "Even the commonest organisms of a wood run into the "
                    "dozens before the rare ones are counted."},
            {"text": "Exactly twenty, in every wood", "correct": False,
             "why": "No two woods hold the same number, and none of them "
                    "holds as few as twenty."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e20",
        "band": "easier",
        "text": "Two of the organisms in an oak wood feed on the oak tree "
                "itself. Which two?",
        "options": [
            {"text": "The blue tits and the ladybird beetles", "correct": False,
             "why": "Both eat insects. Neither of them touches the tree."},
            {"text": "The mice and bees", "correct": False,
             "why": "Mice take acorns from the ground and bees visit the "
                    "wildflowers. Neither feeds on the tree itself."},
            {"text": "The caterpillars and the aphids", "correct": True},
            {"text": "The owls and the sparrowhawk", "correct": False,
             "why": "Both are birds of prey feeding on animals, several steps "
                    "above the tree."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e21",
        "band": "easier",
        "text": "Caterpillars and aphids both damage an oak, but in different "
                "ways. What is the difference?",
        "options": [
            {"text": "Caterpillars eat roots and aphids eat leaves",
             "correct": False,
             "why": "Neither touches the roots. Both feed on the parts of the "
                    "tree above ground."},
            {"text": "Caterpillars eat the leaves and aphids drain sap from "
                     "the shoots", "correct": True},
            {"text": "Caterpillars drain the sap and aphids strip the bark",
             "correct": False,
             "why": "That has the two swapped, and neither of them strips "
                    "bark."},
            {"text": "Caterpillars damage the acorns and the aphids damage the "
                         "flowers", "correct": False,
             "why": "Acorns and flowers are not what either insect takes. "
                    "Leaves and sap are."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e22",
        "band": "easier",
        "text": "In a wood, mice feed on acorns and on wildflower seeds. The "
                "wildflowers thin out badly over several years. What happens "
                "to the mice?",
        "options": [
            {"text": "Their numbers fall, with less seed to feed on",
             "correct": True},
            {"text": "Their numbers rise, because there is more room to move "
                     "about in", "correct": False,
             "why": "Space is not what limits them here. Food is, and one of "
                    "their two foods has gone."},
            {"text": "Nothing changes, because they still have all the acorns",
             "correct": False,
             "why": "Half a food supply is not a whole one. Losing one of two "
                    "foods still means less to eat."},
            {"text": "They begin eating the wildflowers' leaves instead of seed",
             "correct": False,
             "why": "There are fewer plants of every part, leaves included. "
                    "Thinning removes the whole plant."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e23",
        "band": "easier",
        "text": "A teaching web of a wood has two entries that stand for "
                "whole groups rather than for single species. Which two?",
        "options": [
            {"text": "The owls and the sparrowhawks", "correct": False,
             "why": "Each of those names one kind of bird. Neither is "
                    "standing in for a group."},
            {"text": "The caterpillars and the oak's aphids", "correct": False,
             "why": "Both are named insects of the oak. They are not "
                    "shorthand for anything wider."},
            {"text": "The mice and bees", "correct": False,
             "why": "Both are ordinary single entries in the web, with their "
                    "own feeding and pollinating links."},
            {"text": "The wildflowers, and the fungi and bacteria",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e24",
        "band": "easier",
        "text": "One rule of webs says the species that suffers most is often "
                "a competitor. What is a competitor?",
        "options": [
            {"text": "An organism that needs the same food as another one",
             "correct": True},
            {"text": "An organism that hunts exactly the same prey as its own "
                         "predator does", "correct": False,
             "why": "That is one case of competing, and the word is wider "
                    "than that — it covers any shared need."},
            {"text": "An organism that arrives in a web from somewhere else",
             "correct": False,
             "why": "An arrival may or may not compete. The word is about "
                    "needing the same thing, not about coming from away."},
            {"text": "An organism eaten by the same predator",
             "correct": False,
             "why": "Sharing a predator is a real link and it is not "
                    "competition, which is about sharing a need."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e25",
        "band": "easier",
        "text": "The outcomes described for removing a species from a wood "
                "are called plausible directions rather than predictions. "
                "What does that mean?",
        "options": [
            {"text": "They are guesses about the wood, made without looking at "
                         "any of the links in the web",
             "correct": False,
             "why": "They are worked out from the links in the web. That is "
                    "what makes them plausible."},
            {"text": "They show which way things are likely to move, not what "
                     "will certainly happen", "correct": True},
            {"text": "They are certain to happen, but nobody knows when",
             "correct": False,
             "why": "The timing is uncertain AND so is the outcome. Some "
                    "effects never arrive."},
            {"text": "They apply to this wood and to no other", "correct": False,
             "why": "The reasoning transfers to any web. It is the certainty, "
                    "not the place, that is limited."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e26",
        "band": "easier",
        "text": "Before choosing which species to remove from a web on paper, "
                "what is it most useful to look at first?",
        "options": [
            {"text": "Which organism is largest", "correct": False,
             "why": "Size says nothing about how much depends on an "
                    "organism. A microscopic species can hold up a wood."},
            {"text": "Which organism is rarest in the wood", "correct": False,
             "why": "Rarity is a reason to worry about a species, not a "
                    "measure of how much of the wood depends on it."},
            {"text": "How many arrows go into and out of each organism",
             "correct": True},
            {"text": "Which organism is drawn nearest the very top of the "
                         "picture",
             "correct": False,
             "why": "Position on the page is a drawing decision. Removing "
                    "something at the bottom often matters more."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e27",
        "band": "easier",
        "text": "Which of these is an example of a food web being disturbed?",
        "options": [
            {"text": "A new species arriving in a wood that has never held it",
             "correct": True},
            {"text": "A fox eating a rabbit on an autumn evening",
             "correct": False,
             "why": "That is the web working normally. Feeding is what a web "
                    "is made of."},
            {"text": "A caterpillar turning into a moth over the summer",
             "correct": False,
             "why": "An animal growing up changes nothing about who eats "
                    "whom."},
            {"text": "Leaves falling from the oak in the autumn",
             "correct": False,
             "why": "Leaf fall happens every year and feeds the decomposers. "
                    "It is part of the ordinary running of the wood."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e28",
        "band": "easier",
        "text": "In a wood, ladybirds eat aphids and nothing else. A cold "
                "spring kills almost every aphid. Which organism loses a "
                "food?",
        "options": [
            {"text": "The oak", "correct": False,
             "why": "Aphids take sap FROM the oak. Losing them is a relief to "
                    "the tree, not a loss."},
            {"text": "The ladybirds", "correct": True},
            {"text": "The mice",
             "correct": False,
             "why": "Mice eat acorns and seeds. Nothing links them to the "
                    "aphids at all."},
            {"text": "The wildflowers",
             "correct": False,
             "why": "Aphids are sap-suckers, not pollinators. The bees are "
                    "what the flowers depend on."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e29",
        "band": "easier",
        "text": "Blue tits in a wood eat caterpillars and aphids. A disease "
                "wipes out every caterpillar. What can the blue tits do?",
        "options": [
            {"text": "Switch to the aphids, their other food", "correct": True},
            {"text": "Begin eating the oak leaves the caterpillars ate",
             "correct": False,
             "why": "A blue tit cannot digest leaves. Its other food is the "
                    "aphids."},
            {"text": "Nothing — they need caterpillars", "correct": False,
             "why": "They have a second food named in the question, which is "
                    "what makes them less vulnerable than a specialist."},
            {"text": "Hunt the sparrowhawks that used to hunt them",
             "correct": False,
             "why": "A small bird does not turn on a bird of prey. Arrows do "
                    "not reverse when food runs short."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-e30",
        "band": "easier",
        "text": "In an oak wood, mice feed mainly on acorns through the "
                "winter. The oak produces almost no acorns one autumn. Which "
                "organism feels it first?",
        "options": [
            {"text": "The ladybirds", "correct": False,
             "why": "Ladybirds eat aphids. Nothing joins them to the acorn "
                    "crop."},
            {"text": "The bees", "correct": False,
             "why": "Bees work the wildflowers. Acorns are no part of what "
                    "they use."},
            {"text": "The mice", "correct": True},
            {"text": "The owls", "correct": False,
             "why": "The owls do feel it, and only after the mice have. The "
                    "question asks which is first."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · standard ───────────────────────────────────────
    {
        "id": "b9-03-s10",
        "band": "standard",
        "text": "Deer browse the young plants of a wood heavily. A fence is "
                "built to keep them out. Predict what happens to the ground "
                "plants and to the birds that nest in them.",
        "options": [
            {"text": "The ground plants thin out, because the deer spread their "
                         "seed", "correct": False,
             "why": "Deer eat the plants rather than sowing them. Heavy "
                    "browsing is a loss to a plant, not a service."},
            {"text": "Nothing changes: deer feed on trees, not on ground plants", "correct": False,
             "why": "Deer browse whatever is within reach, and young ground "
                    "plants are exactly that."},
            {"text": "The ground plants thicken and the birds lose the open "
                         "ground they need", "correct": False,
             "why": "These birds nest IN the low plants. Thicker cover is "
                    "what they want, not what they lose."},
            {"text": "The ground plants thicken, and the birds that nest in "
                     "them do better", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s11",
        "band": "standard",
        "text": "A stretch of moor is burned off. The voles that lived in the "
                "old heather lose their cover and their food, and buzzards "
                "hunt those voles. Predict what happens.",
        "options": [
            {"text": "Buzzard numbers fall first, and vole numbers follow them "
                         "down later", "correct": False,
             "why": "The order runs the other way. The change reaches the "
                    "voles' food and cover before it reaches the buzzards."},
            {"text": "Vole numbers rise on the open ground, so the buzzards do "
                         "better", "correct": False,
             "why": "Open ground is a danger to a vole, not an opportunity. "
                    "Their cover and their food have both gone."},
            {"text": "Vole numbers fall, and buzzard numbers fall some time "
                     "afterwards", "correct": True},
            {"text": "Neither changes: buzzards hunt burned ground more easily", "correct": False,
             "why": "Easier hunting for a season does not replace the voles "
                    "that are no longer there to hunt."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s12",
        "band": "standard",
        "text": "One species is removed from a wood, and four species later a "
                "bird that never met it declines. Explain how an effect "
                "reaches that far.",
        "options": [
            {"text": "The bird must have been eating the removed species "
                         "unnoticed", "correct": False,
             "why": "No hidden link is needed. The effect travelled along "
                    "links that were already drawn."},
            {"text": "Removing any species lowers the numbers of every other "
                         "one", "correct": False,
             "why": "Most species are unaffected by most removals. The effect "
                    "follows the routes, not the whole wood."},
            {"text": "The wood is small, so every species is in contact with "
                         "every other", "correct": False,
             "why": "Contact is not the mechanism, and the same effect "
                    "appears in webs spread over many square kilometres."},
            {"text": "Each species changes the next along the links, so the "
                     "change passes step by step", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s13",
        "band": "standard",
        "text": "An orchard's owners destroy the wasps' nests because the "
                "wasps sting pickers. The following summer the trees carry "
                "far more caterpillars. Suggest why.",
        "options": [
            {"text": "The wasps had been pollinating the trees, so far fewer "
                         "fruits grew",
             "correct": False,
             "why": "Fewer fruits would not feed caterpillars. What changed "
                    "is that something stopped eating them."},
            {"text": "The wasps had been hunting the caterpillars, and that "
                     "hunting has stopped", "correct": True},
            {"text": "The caterpillars had been feeding on the wasps", "correct": False,
             "why": "That has the arrow backwards. A caterpillar eats leaves, "
                    "not wasps."},
            {"text": "The wasps had been keeping the birds away from the "
                         "orchard",
             "correct": False,
             "why": "More birds would mean FEWER caterpillars. The change "
                    "went the other way."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s14",
        "band": "standard",
        "text": "A wood's wildflowers are mown short every spring to make the "
                "paths tidy. Mice there feed on wildflower seed and on "
                "acorns. Predict the effect on the mice.",
        "options": [
            {"text": "They increase, because mown ground is easier to run about "
                         "on", "correct": False,
             "why": "Open ground is a danger, and it is the lost seed that "
                    "matters more than the running."},
            {"text": "Nothing changes, because the acorns are their main winter "
                         "food", "correct": False,
             "why": "Losing one of two foods still leaves less to eat, and "
                    "acorn crops vary from year to year."},
            {"text": "They increase, since mowing brings the seed within reach", "correct": False,
             "why": "Mowing in spring removes the flowers before they can set "
                    "any seed at all."},
            {"text": "Their numbers fall, because the flowers never set seed",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s15",
        "band": "standard",
        "text": "A park removes its foxes to protect the birds that nest on "
                "the ground. Two years later those birds are doing worse than "
                "before. Suggest the best explanation.",
        "options": [
            {"text": "The birds had come to depend on the foxes for warning "
                     "them of danger", "correct": False,
             "why": "Nothing suggests that, and a predator is not a lookout "
                    "for its own prey."},
            {"text": "The birds left the park when the foxes did, because "
                     "they follow them about", "correct": False,
             "why": "Ground-nesting birds do not follow a predator. They "
                    "nest where the ground suits them."},
            {"text": "Rats and crows, which the foxes had been holding down, "
                     "have increased", "correct": True},
            {"text": "Two years is far too short a time for any change in a "
                         "bird population to begin to show", "correct": False,
             "why": "Two breeding seasons is quite long enough for a "
                    "ground-nesting bird's numbers to move."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s16",
        "band": "standard",
        "text": "A council plants a new wood and finds no change in local "
                "bird numbers after two years. What should it conclude?",
        "options": [
            {"text": "That the planting has failed and should be replaced", "correct": False,
             "why": "Two years is no basis for that. The trees are barely "
                    "established."},
            {"text": "That birds do not respond to new woodland", "correct": False,
             "why": "Birds respond strongly to new woodland. They respond "
                    "when it has grown enough to use."},
            {"text": "That the planting worked and the birds are counted in the "
                         "wrong place", "correct": False,
             "why": "Blaming the count is a leap. The simpler reading is that "
                    "it is far too early."},
            {"text": "That nothing can be concluded yet, because effects are "
                     "delayed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s17",
        "band": "standard",
        "text": "A gardener wants fewer aphids on her roses without spraying "
                "anything. Using what you know about webs, which plan is "
                "most likely to work?",
        "options": [
            {"text": "Encourage the ladybirds and insect-eating birds that "
                     "feed on aphids", "correct": True},
            {"text": "Remove every other plant so the aphids have nowhere else "
                         "to go", "correct": False,
             "why": "That concentrates the aphids on the roses, and removes "
                    "the shelter their predators need."},
            {"text": "Cut the roses back hard so the aphids have less leaf to "
                         "feed on", "correct": False,
             "why": "Fresh growth after hard pruning is exactly what aphids "
                    "prefer, being soft and full of sap."},
            {"text": "Water the roses more, so they outgrow the damage", "correct": False,
             "why": "Lush watered growth feeds more aphids. Nothing in the "
                    "web has been changed."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s18",
        "band": "standard",
        "text": "A team plans to clear an invasive shrub from a heath. What "
                "should they find out first?",
        "options": [
            {"text": "How tall the shrub grows", "correct": False,
             "why": "That is a question about the work. It says nothing about "
                    "what the clearance will do to the heath."},
            {"text": "Whether the shrub was introduced deliberately", "correct": False,
             "why": "How it arrived is history. What matters now is what "
                    "depends on it."},
            {"text": "How quickly the shrub would grow back if only part were "
                         "taken out", "correct": False,
             "why": "Useful for planning the work, and it still does not say "
                    "what else will be affected."},
            {"text": "What in the heath's web currently uses the shrub",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s19",
        "band": "standard",
        "text": "A wood is fenced so completely that no animal can move into "
                "it or out of it. Suggest one effect the fence alone could "
                "have on the wood's web.",
        "options": [
            {"text": "Every species becomes a generalist, unable to go "
                         "elsewhere", "correct": False,
             "why": "A fence does not change what an animal can digest. A "
                    "specialist stays a specialist."},
            {"text": "A species lost from the wood cannot be replaced by one "
                     "moving in", "correct": True},
            {"text": "The web becomes steadier, since nothing new can arrive", "correct": False,
             "why": "Shutting out arrivals also shuts out replacements, which "
                    "is a loss of routes rather than a gain."},
            {"text": "The effects of a removal travel faster inside the fence", "correct": False,
             "why": "Effects travel through feeding links at the speed "
                    "populations respond. A fence does not hurry them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s20",
        "band": "standard",
        "text": "A disease removes one plant species from a meadow. Some "
                "insects there feed on that plant alone; others feed on many "
                "plants. Predict which insects suffer most.",
        "options": [
            {"text": "The many-plant feeders, with more links to lose", "correct": False,
             "why": "More links means more that survive. Losing one of many "
                    "is a smaller loss than losing one of one."},
            {"text": "Neither group, since the meadow holds plenty of other "
                         "plants", "correct": False,
             "why": "Plenty of other plants is no help to an insect that can "
                    "eat only the one that has gone."},
            {"text": "The insects that fed on that plant alone", "correct": True},
            {"text": "Both equally, since meadow insects eat whatever is "
                         "flowering", "correct": False,
             "why": "Many insects are tied to one plant species. That is what "
                    "the word specialist is for."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s21",
        "band": "standard",
        "text": "Before judging which removal from a web would matter most, "
                "ecologists count the arrows going into and out of each "
                "organism. Explain what those two counts tell them.",
        "options": [
            {"text": "Arrows in show its size, and arrows out how long it lives", "correct": False,
             "why": "Neither count says anything about size or lifespan. They "
                    "are feeding links."},
            {"text": "Both counts show the same thing, so one will do", "correct": False,
             "why": "They are different: one is about the organism's food, "
                    "the other about what eats it."},
            {"text": "Arrows out show what it eats, and arrows in show how safe "
                         "it is from its predators", "correct": False,
             "why": "That is both counts the wrong way round. An arrow points "
                    "towards the eater."},
            {"text": "Arrows in show what it depends on; arrows out show what "
                     "depends on it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s22",
        "band": "standard",
        "text": "Grazing animals are removed from a grassland rich in small "
                "flowering plants. The grasses there grow tall. Predict what "
                "happens to the small plants.",
        "options": [
            {"text": "They are shaded out by the tall grass and become "
                     "scarcer", "correct": True},
            {"text": "They spread quickly, with nothing eating them", "correct": False,
             "why": "Grazing removed the grass that would otherwise shade "
                    "them, so losing it costs them more than it saves."},
            {"text": "They are unaffected: grasses and small plants do not "
                         "compete", "correct": False,
             "why": "They compete directly for light, and the taller plant "
                    "wins that competition."},
            {"text": "They grow taller as well, to keep up with the grasses", "correct": False,
             "why": "A plant's height is set by what it is, not by what it "
                    "needs. Small plants stay small."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s23",
        "band": "standard",
        "text": "Two woods each lose one species. The wood with twenty "
                "species recovers with little visible change; the wood with "
                "six does not. Which rule about webs does that show?",
        "options": [
            {"text": "That effects are delayed, so the larger wood's change "
                     "has yet to arrive", "correct": False,
             "why": "Delay is a real rule and it does not explain why the "
                    "smaller wood was hit at once and harder."},
            {"text": "That a web with more alternative routes absorbs a loss "
                     "more easily", "correct": True},
            {"text": "That effects travel sideways, so the wood spread the "
                         "change", "correct": False,
             "why": "Sideways means through the web, not into another wood. "
                    "Neither wood exported anything."},
            {"text": "That a wood with more species is always the healthier "
                     "of two woods", "correct": False,
             "why": "Health is not the point, and a species-rich wood can "
                    "still be destroyed by the right loss."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s24",
        "band": "standard",
        "text": "A species has been lost from a wood and a trust wants to "
                "bring it back. Suggest one practical reason that is harder "
                "than it sounds.",
        "options": [
            {"text": "Species that have gone from one place are never found "
                         "elsewhere", "correct": False,
             "why": "Many can be found elsewhere. The difficulty is whether "
                    "the wood they return to still suits them."},
            {"text": "Putting a species back is against the law in Britain",
             "correct": False,
             "why": "Reintroductions are carried out under licence and "
                    "several have succeeded. The obstacles are practical."},
            {"text": "The wood may have changed in the meantime, so what the "
                     "species needs is gone", "correct": True},
            {"text": "A species that has been away for a few years forgets "
                     "how to feed itself", "correct": False,
             "why": "Animals do not forget what they are. What changes is the "
                    "place they are returning to."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s25",
        "band": "standard",
        "text": "Two insects in a wood feed on the same plant and on nothing "
                "else. A disease wipes out one of the two. Predict the effect "
                "on the other.",
        "options": [
            {"text": "It declines: the two had been helping each other feed", "correct": False,
             "why": "Nothing suggests they helped one another. Two species "
                    "on one food are competitors."},
            {"text": "It declines, since the disease will kill it too", "correct": False,
             "why": "Diseases are usually particular about which species they "
                    "infect. Nothing here says this one spreads."},
            {"text": "Nothing changes: each ate only its own share", "correct": False,
             "why": "Shares are not fixed. Food that one insect no longer "
                    "takes is available to the other."},
            {"text": "It does better, with more of the plant to itself",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s26",
        "band": "standard",
        "text": "Mice are poisoned around a farm to protect stored grain. In "
                "the wood next door, owls eat those mice and the mice eat "
                "wildflower seed. Predict the two effects.",
        "options": [
            {"text": "More owls, and fewer wildflowers", "correct": False,
             "why": "Owls do not eat flowers, and fewer mice means less owl "
                    "food, not more."},
            {"text": "Fewer owls, and more wildflowers", "correct": True},
            {"text": "Fewer owls, and fewer wildflowers", "correct": False,
             "why": "The mice EAT the seed here. Removing a seed-eater leaves "
                    "more seed, not less."},
            {"text": "No change to either", "correct": False,
             "why": "Mice move between the two, and a web does not stop at a "
                    "field boundary."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s27",
        "band": "standard",
        "text": "In a wood, sparrowhawks hunt blue tits and blue tits eat "
                "caterpillars. Gamekeepers shoot out the sparrowhawks. "
                "Predict the effect on the blue tits and then on the "
                "caterpillars.",
        "options": [
            {"text": "More blue tits, and then fewer caterpillars",
             "correct": True},
            {"text": "Fewer blue tits, and then more caterpillars",
             "correct": False,
             "why": "A sparrowhawk hunts blue tits. Removing it takes "
                    "pressure off them rather than protection."},
            {"text": "More blue tits, and more caterpillars too", "correct": False,
             "why": "Populations linked by feeding move in opposite "
                    "directions. More predators means fewer prey."},
            {"text": "No change to either of them", "correct": False,
             "why": "A top predator's removal is usually the change that "
                    "travels furthest, not the least."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s28",
        "band": "standard",
        "text": "Ivy is stripped from a wood's trees because it looks untidy. "
                "Ivy flowers late in the year, when almost nothing else does. "
                "Predict the effect on the wood's insects.",
        "options": [
            {"text": "Insects do better, since ivy had shaded the flowers", "correct": False,
             "why": "Ivy climbs the trunks rather than shading the ground "
                    "flowers, and it supplies food no other plant does."},
            {"text": "Nothing changes: insects feed all summer instead", "correct": False,
             "why": "Insects still flying in late autumn need food then. A "
                    "good summer does not carry them through."},
            {"text": "The insects that feed late in the year lose their food",
             "correct": True},
            {"text": "Only the insects that eat ivy leaves are affected", "correct": False,
             "why": "The flowers are what makes ivy unusual here. The insects "
                    "visiting them are the ones that lose most."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s29",
        "band": "standard",
        "text": "A wood is managed so that dead and dying trees are left "
                "standing rather than cleared. Suggest how that helps the "
                "wood's web.",
        "options": [
            {"text": "It stops the living trees catching disease from the dead "
                         "ones, and keeps the wood healthy", "correct": False,
             "why": "Leaving dead wood does not protect living trees. The "
                    "gain is in what the dead wood supports."},
            {"text": "It holds the insects, fungi and hole-nesting birds that "
                     "need dead wood", "correct": True},
            {"text": "It gives the wood's producers more light, because a "
                     "dead tree carries no leaves", "correct": False,
             "why": "A standing dead tree lets some light through, and the "
                    "reason for leaving it is what lives in it."},
            {"text": "It means the decomposers have nothing left to do, so "
                     "the soil stays richer", "correct": False,
             "why": "Dead wood is exactly what decomposers work on. Leaving "
                    "it gives them more, not less."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-s30",
        "band": "standard",
        "text": "Brambles are cleared from a wood's edges. Brambles flower in "
                "summer and carry fruit in autumn. Predict the effects at "
                "those two times of year.",
        "options": [
            {"text": "Pollinating insects lose summer flowers, and birds lose "
                     "autumn fruit", "correct": True},
            {"text": "Pollinating insects lose autumn flowers and birds lose "
                         "nest sites",
             "correct": False,
             "why": "The two seasons are the wrong way round: brambles flower "
                    "in summer and fruit in autumn."},
            {"text": "Nothing is lost in summer; in autumn the birds move to "
                         "acorns", "correct": False,
             "why": "The summer flowers are a real loss, and acorns suit "
                    "different birds from those that take berries."},
            {"text": "The wood gains in both seasons, with more light for other "
                         "plants",
             "correct": False,
             "why": "More light for some plants is a small gain beside losing "
                    "a food supply in two separate seasons."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · harder ─────────────────────────────────────────
    {
        "id": "b9-03-h10",
        "band": "harder",
        "text": "A team clears an introduced shrub from a heath and a rare "
                "butterfly, which had been increasing, declines sharply. "
                "Suggest the best explanation.",
        "options": [
            {"text": "The butterfly was poisoned by the chemicals used in the "
                     "clearance work", "correct": False,
             "why": "Nothing says chemicals were used, and the decline "
                    "followed the loss of the shrub rather than the work."},
            {"text": "The butterfly had never really been increasing, so the "
                     "earlier counts were wrong", "correct": False,
             "why": "Doubting the record is the last resort. A plain "
                    "explanation from the web is available."},
            {"text": "Butterflies always decline when a heath is managed in "
                     "any way", "correct": False,
             "why": "Many heath butterflies depend on management. It is what "
                    "was removed here that matters."},
            {"text": "The butterfly had come to depend on the introduced "
                     "shrub", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h11",
        "band": "harder",
        "text": "Two removals from the same wood are compared on paper. One "
                "changed the numbers of seven species; the other changed "
                "three. What does that tell you about the two species "
                "removed?",
        "options": [
            {"text": "The first was the larger animal of the two",
             "correct": False,
             "why": "Body size does not decide reach. A microscopic species "
                    "can hold up a whole wood."},
            {"text": "The first was rarer, so its loss was felt more sharply",
             "correct": False,
             "why": "Rarity is not reach. A rare specialist with one link may "
                    "change almost nothing when it goes."},
            {"text": "The first had more links, or sat lower in the web",
             "correct": True},
            {"text": "The second was removed more recently than the first",
             "correct": False,
             "why": "Both were worked through on paper. Timing does not enter "
                    "into it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h12",
        "band": "harder",
        "text": "Two woodland birds eat the same beetle and nothing else "
                "links them. One is removed. Explain how an effect can reach "
                "the plants the beetle feeds on.",
        "options": [
            {"text": "The plants recover, because one fewer bird means less "
                     "trampling of the ground beneath them", "correct": False,
             "why": "Trampling is not a feeding link and is not what "
                    "connects these species."},
            {"text": "Nothing reaches the plants, because a bird and a plant "
                     "are two steps apart in a web", "correct": False,
             "why": "Two steps is nothing. Effects in webs run four and five "
                    "steps routinely."},
            {"text": "The plants are eaten more, because beetles rise and "
                     "nothing eats them", "correct": False,
             "why": "The other bird is still eating beetles, and with less "
                    "competition it takes more, not fewer."},
            {"text": "The remaining bird takes more beetles, so fewer are "
                     "left to eat the plants", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h13",
        "band": "harder",
        "text": "A wood is restored by replanting every plant species that "
                "had been lost from it. Ten years later several animals have "
                "still not returned. Suggest why.",
        "options": [
            {"text": "The plants must have been the wrong species after all",
             "correct": False,
             "why": "Every lost species was replanted. The gap is on the "
                    "animals' side of the problem."},
            {"text": "There may be no population nearby for them to return "
                     "from", "correct": True},
            {"text": "Animals take longer to grow than plants do, so ten "
                     "years is far too short", "correct": False,
             "why": "Most woodland animals breed within a year or two. Ten "
                    "years is many generations."},
            {"text": "Replanting a wood makes it too crowded for animals to "
                     "move about in", "correct": False,
             "why": "A restored wood is the habitat they need. Crowding is "
                    "not what keeps them out."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h14",
        "band": "harder",
        "text": "In Yellowstone the elk changed where they fed as well as how "
                "many there were. Explain why counting elk alone would have "
                "missed part of the story.",
        "options": [
            {"text": "A count is unreliable for a herd animal that moves "
                     "about a large park", "correct": False,
             "why": "Elk are counted well enough. The point is what a number "
                    "cannot record."},
            {"text": "A count of elk would have been too slow to be finished "
                     "in a single season", "correct": False,
             "why": "Speed is not the issue. Even a perfect count records "
                    "only how many, never where."},
            {"text": "The willow recovered where the elk stopped feeding, "
                     "which a number cannot show", "correct": True},
            {"text": "The elk were not the species that mattered, so counting "
                     "them was beside the point", "correct": False,
             "why": "The elk were the link between wolf and willow. Counting "
                    "them mattered; it simply was not enough."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h15",
        "band": "harder",
        "text": "A trust has money to protect one species in a wood. On what "
                "grounds should it choose?",
        "options": [
            {"text": "The rarest species, since it is nearest to being lost",
             "correct": False,
             "why": "Rarity is a reason to act and it says nothing about what "
                    "else would go with it."},
            {"text": "The largest species, since it needs the most ground",
             "correct": False,
             "why": "Ground is a cost, not a measure of what depends on the "
                    "animal."},
            {"text": "The best-known species, since the public will support "
                     "it", "correct": False,
             "why": "Support matters for funding and it is not a fact about "
                    "the web."},
            {"text": "The species that most others in the wood depend on",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h16",
        "band": "harder",
        "text": "Compare the effect of losing a predator that eats six "
                "species with losing one that eats a single species.",
        "options": [
            {"text": "The six-prey predator's loss is felt by fewer species, "
                     "since each one loses less", "correct": False,
             "why": "It is felt by more species, though lightly. Number "
                    "affected and size of effect are different things."},
            {"text": "The generalist's loss spreads thinly over six species; "
                     "the specialist's lands on one", "correct": True},
            {"text": "Both losses are felt by exactly one species, because a "
                     "predator has one main prey", "correct": False,
             "why": "A generalist has no single main prey. That is what makes "
                    "it a generalist."},
            {"text": "Neither loss is felt, because prey do better without a "
                     "predator", "correct": False,
             "why": "Prey rising IS the effect being felt, and what they then "
                    "eat feels it in turn."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h17",
        "band": "harder",
        "text": "An ecologist ranks four species by how many feeding links "
                "each has, and predicts that removing the one with the most "
                "links will change the wood most. Give one reason that could "
                "fail.",
        "options": [
            {"text": "A species with many links is always the easiest one to "
                     "remove from a wood", "correct": False,
             "why": "How easy a removal is has nothing to do with how far its "
                    "effects travel."},
            {"text": "Counting links is guesswork, so no ranking from it can "
                     "ever be trusted", "correct": False,
             "why": "Links can be observed and recorded. The ranking is "
                    "useful; it is simply not the whole story."},
            {"text": "Links can only be counted for animals, never for "
                     "plants", "correct": False,
             "why": "A plant's links are counted the same way — what eats it, "
                    "and what it needs."},
            {"text": "A species with few links may be the only route to "
                     "something", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h18",
        "band": "harder",
        "text": "After a removal, a wood's records show one species risen, "
                "two fallen and eight unchanged. A student says the removal "
                "mostly did not matter. Evaluate that.",
        "options": [
            {"text": "He is right: eight of eleven species were untouched by "
                     "it", "correct": False,
             "why": "Counting the untouched species is the wrong arithmetic. "
                    "Three changed, and more may follow."},
            {"text": "He is wrong, because a removal must always change every "
                     "species in a wood", "correct": False,
             "why": "It need not. Plenty of species genuinely are unaffected "
                    "by a given loss."},
            {"text": "Three species have already changed, and effects are "
                     "delayed", "correct": True},
            {"text": "He is right, since the one species that rose cancels "
                     "out the two that fell", "correct": False,
             "why": "Populations do not cancel one another. Three separate "
                    "species have moved."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h19",
        "band": "harder",
        "text": "A fungus kills most of a wood's oaks slowly, over twenty "
                "years. Compare that with the same oaks being felled in a "
                "single winter.",
        "options": [
            {"text": "The slow loss does more damage, because the fungus "
                     "spreads to other species too", "correct": False,
             "why": "Nothing says the fungus attacks anything else. The "
                    "comparison is about the speed of the loss."},
            {"text": "The slow loss gives other species time to adjust or "
                     "move", "correct": True},
            {"text": "The two are identical, because the same number of oaks "
                     "is lost either way", "correct": False,
             "why": "The total is the same and the rate is not, and "
                    "populations respond to a rate."},
            {"text": "The sudden loss does less damage, because the wood can "
                     "be replanted at once", "correct": False,
             "why": "A replanted oak takes decades to do an oak's job. "
                    "Planting is not replacing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h20",
        "band": "harder",
        "text": "An ecologist calls a wood stable because its list of species "
                "has not changed in ten years. Give the strongest reason to "
                "doubt that.",
        "options": [
            {"text": "Ten years is too short for any wood to be judged on",
             "correct": False,
             "why": "Ten years is a useful record. The trouble is what a "
                    "species LIST leaves out of it."},
            {"text": "A species list cannot be counted accurately in a wood "
                     "of any size", "correct": False,
             "why": "Species lists are among the easier things to record. "
                    "Numbers within each species are the harder part."},
            {"text": "A wood with the same species every year is certain to "
                     "be in trouble", "correct": False,
             "why": "A steady list is not itself a warning. It simply does "
                    "not prove what is claimed from it."},
            {"text": "Numbers can change a great deal while the list stays "
                     "the same", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h21",
        "band": "harder",
        "text": "In wood A, aphids are eaten by ladybirds and by blue tits. "
                "In wood B, only the ladybirds eat them. A disease removes "
                "the ladybirds from both. Compare the effect on the aphids.",
        "options": [
            {"text": "Aphids rise further in wood A, because it holds more "
                     "insects to begin with", "correct": False,
             "why": "Wood A has the extra PREDATOR. More predators means less "
                    "room for aphids, not more."},
            {"text": "Aphids rise by the same amount in both, since the same "
                     "predator was lost", "correct": False,
             "why": "What is left behind differs. Wood A still has a bird "
                    "eating aphids and wood B has nothing."},
            {"text": "Aphids rise less in wood A, where the blue tits still "
                     "eat them", "correct": True},
            {"text": "Aphids fall in wood A, because the blue tits take over "
                     "entirely", "correct": False,
             "why": "Blue tits absorb part of the loss. They do not more than "
                    "make up for a predator that has gone."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h22",
        "band": "harder",
        "text": "A teaching model shows the effects of a removal in three "
                "rounds; in a real wood the same effects take years. Explain "
                "why that difference matters to someone managing woodland.",
        "options": [
            {"text": "They may judge a change safe, or stop watching, long "
                     "before its effects arrive", "correct": True},
            {"text": "They will see effects in the wood sooner than the model "
                     "shows them", "correct": False,
             "why": "The model is faster than the wood, not slower. Real "
                    "effects arrive later than three rounds suggest."},
            {"text": "They cannot use a model at all, since real woods do not "
                     "behave in rounds", "correct": False,
             "why": "The rounds show the ORDER of the effects, which is the "
                    "useful part. Only the timing is compressed."},
            {"text": "They will need to remove more species than the model "
                     "shows to get a result", "correct": False,
             "why": "Nothing about the timing changes how many species a "
                    "manager should remove."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h23",
        "band": "harder",
        "text": "Bees in a wood eat nothing that lives there and nothing "
                "eats them. A student argues that removing them changes the "
                "wood's pollination and not its food web. Evaluate that.",
        "options": [
            {"text": "He is right, because an organism with no feeding link "
                     "is not part of a food web", "correct": False,
             "why": "It is in the web by what it makes possible. The seed "
                    "the flowers set is food for other animals."},
            {"text": "He is right, because pollination and feeding are "
                     "separate systems in a wood", "correct": False,
             "why": "They meet at the seed. Pollination is what puts the food "
                    "into the web in the first place."},
            {"text": "He is wrong, because bees are eaten by birds in every "
                     "real wood", "correct": False,
             "why": "That may be true elsewhere, and it is not true in the "
                    "wood described. The real answer is the seed."},
            {"text": "He is wrong: the seed-eaters and what hunts them all "
                     "depend on that pollination", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h24",
        "band": "harder",
        "text": "An ecologist maps a web and finds one species with eleven "
                "links. State what that predicts, and one thing it does not.",
        "options": [
            {"text": "It predicts how far each effect will travel, but not "
                     "which species feel it", "correct": False,
             "why": "It is the other way about. The links say who is "
                    "connected, not how strongly."},
            {"text": "It predicts nothing useful, since the number of links "
                     "is not a measurement", "correct": False,
             "why": "It is a count of real connections, and it is genuinely "
                    "useful — just not complete."},
            {"text": "It predicts wide effects, but not how strongly each one "
                     "is felt", "correct": True},
            {"text": "It predicts that the species is at the top of the web, "
                     "but not which prey it takes", "correct": False,
             "why": "Many links can belong to a producer at the bottom. The "
                    "count says nothing about the level."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h25",
        "band": "harder",
        "text": "Two woods hold the same list of species and lose the same "
                "one. One wood barely changes and the other is transformed. "
                "Suggest the best explanation.",
        "options": [
            {"text": "One wood is older, so its species are better at coping "
                     "with a loss", "correct": False,
             "why": "Age does not teach a species to cope. What differs is "
                    "how much each one relied on what went."},
            {"text": "How much each species relies on the lost one differs "
                     "between the woods", "correct": True},
            {"text": "The two woods must have been recorded by different "
                     "methods", "correct": False,
             "why": "Doubting the record explains nothing. Two real woods "
                    "with one species list can still differ."},
            {"text": "One wood is larger, so the effect is spread out over "
                     "more ground", "correct": False,
             "why": "Area does not dilute a feeding link. A large wood with "
                    "one route is as vulnerable as a small one."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h26",
        "band": "harder",
        "text": "A student says nothing depends on an animal at the top of a "
                "web, because nothing eats it. Explain why that is wrong.",
        "options": [
            {"text": "It is wrong, because every animal is eaten by something "
                     "larger than itself", "correct": False,
             "why": "Nothing hunts a top predator — that is what the words "
                    "mean. What the student missed is what DEPENDS on it."},
            {"text": "Nothing does depend on it, so the student is right",
             "correct": False,
             "why": "Its prey depend on it to hold their numbers down, and "
                    "what they eat depends on that in turn."},
            {"text": "It is wrong only for very large webs with many species "
                     "in them", "correct": False,
             "why": "It is wrong in any web. Every predator presses on its "
                    "prey, whatever the size of the web."},
            {"text": "What it eats depends on it, and so does whatever that "
                     "in turn eats", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h27",
        "band": "harder",
        "text": "A reserve is managed for one valued butterfly by removing "
                "the plants that compete with its foodplant. Suggest a risk "
                "that the plan carries.",
        "options": [
            {"text": "The removed plants were food or shelter for other "
                     "species", "correct": True},
            {"text": "The butterfly will become a generalist once its "
                     "foodplant is common", "correct": False,
             "why": "A specialist does not change what it can eat because "
                    "more of it is available."},
            {"text": "The foodplant will be eaten faster than it can grow "
                     "back again", "correct": False,
             "why": "More foodplant is the point of the plan. Over-eating it "
                    "is not the risk being created."},
            {"text": "Removing plants is never allowed on a nature reserve",
             "correct": False,
             "why": "Reserves are managed by removing plants routinely. The "
                    "risk is ecological, not legal."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h28",
        "band": "harder",
        "text": "A species declines ten years after another was removed from "
                "the same wood. A student says the gap is too long for the "
                "removal to be the cause. Evaluate that.",
        "options": [
            {"text": "He is right, because an effect that has not appeared "
                     "within a year will never appear", "correct": False,
             "why": "Effects routinely take seasons or years. A year proves "
                    "nothing either way."},
            {"text": "He is right, because ten years is long enough for the "
                     "wood to have replaced what it lost", "correct": False,
             "why": "Replacement is possible and it is not automatic. A long "
                    "gap does not rule the removal out."},
            {"text": "A long gap is expected, so it is not evidence against "
                     "the removal", "correct": True},
            {"text": "He is wrong, because every effect of a removal takes "
                     "exactly ten years to arrive", "correct": False,
             "why": "There is no fixed time. Some effects come in a season "
                    "and some never come at all."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h29",
        "band": "harder",
        "text": "A bird has declined in a wood. It could be the species "
                "removed three years ago, or a run of bad weather. Suggest "
                "the evidence that would best favour the removal.",
        "options": [
            {"text": "That the decline began in the same year the species was "
                     "removed from the wood", "correct": False,
             "why": "Timing alone is weak: the weather of that year would fit "
                    "just as well."},
            {"text": "That only the species linked to what was removed have "
                     "changed", "correct": True},
            {"text": "That the bird has declined in several other woods over "
                     "the same three years", "correct": False,
             "why": "A decline everywhere points AWAY from one wood's "
                    "removal and towards the weather."},
            {"text": "That the removed species was the largest animal in the "
                     "wood at the time", "correct": False,
             "why": "Size is not evidence of a link. What matters is which "
                    "species are connected to it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-03-h30",
        "band": "harder",
        "text": "After a removal, one species in a wood rose sharply for "
                "three years and then fell back over the next seven. Suggest "
                "an explanation.",
        "options": [
            {"text": "It rose with its predator gone, then ran short of food "
                     "or met a new competitor", "correct": True},
            {"text": "The removed species came back and began eating it "
                     "again", "correct": False,
             "why": "Nothing says it returned, and the record would show a "
                    "sharper fall than a seven-year decline."},
            {"text": "Its numbers were miscounted in the first three years of "
                     "the record", "correct": False,
             "why": "A rise and fall over ten years is a pattern. Doubting "
                    "the count explains nothing about its shape."},
            {"text": "Populations always return to their starting numbers "
                     "after ten years", "correct": False,
             "why": "There is no such rule. Many populations settle "
                    "somewhere quite new after a change."},
        ],
        "figure": None,
    },
]
