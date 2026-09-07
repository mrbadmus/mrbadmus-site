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
]
