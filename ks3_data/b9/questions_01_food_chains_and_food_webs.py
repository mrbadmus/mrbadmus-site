# -*- coding: utf-8 -*-
"""B9 lesson 01 — Food chains and food webs: twelve questions (MRB-269).

The lesson has two halves and this bank works both. *Who eats whom* is the
four job titles, the arrow rule, and the drawn oak wood web; *what happens to
the energy* is the bench, where ten thousand kilojoules of grass becomes ten
kilojoules of eagle four levels later. The bank probes the roles (what makes
an organism a producer, where decomposers actually sit, what a web is that a
chain is not), the arithmetic in both directions (two steps up the field
chain, the extra step that costs the orca a tenth again, and an eight-link
claim that fails on a ten-millionth), and the honest size of the ratio itself.

Distractors are built from the lesson's two declared misconceptions.
**ECO-01** ("the arrow points at what the animal eats") supplies every option
that reads an arrow backwards — the ladybirds "eaten by" the aphids, the
mice-to-sparrowhawk link redrawn the other way, and the producer picked out as
the organism with the most arrows pointing INTO it. **ECO-02** ("ninety per
cent of the energy is lost at each level") supplies the arithmetic errors:
9,000 kJ reaching the foxes because a tenth was read as the loss rather than
the survival, and the belief that a bigger animal at the top must mean more
energy arriving there.

Four further errors the lesson exists to correct are worked as well: that
decomposers are the last link of a chain rather than underneath every level of
it (the fourth role card is the only place on the page that says otherwise);
that what eats an organism decides its trophic level, rather than what it
eats; that a producer is whatever supplies the level above it; and that the
tenth is a measurement, which the convention note and rung 4's fifth criterion
both refuse — worked here as a real 18% efficiency that a student has to
decide is inside the range rather than a refutation.

No question restates a ladder rung. The rungs own arrow direction on a stated
chain, the fate of the other 90%, the pyramid shape, and the beef-to-wheat
land argument, so the bank goes round all four: arrow direction appears only
as a way of READING an unlabelled web, the fate of the energy appears only
inside distractor corrections, the pyramid is left entirely to rung 3, and the
land-use argument is replaced by the whale-and-krill case from the stretch
layer, which is the same arithmetic pointed somewhere else.

`figure` is `b9-oak-wood-web-thread` on two questions — the drawn web is the
only place in the lesson where a student can practise reading arrow direction
off a picture rather than off a sentence, and both stems need the wood in
front of them. Every other stem is self-contained.
"""

UNIT = "B9"
LESSON = "food-chains-and-food-webs"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-01-e01",
        "band": "easier",
        "text": "A field chain runs: grass, rabbits, foxes, golden eagle. "
                "Which organism is the producer, and what makes it one?",
        "options": [
            {"text": "The rabbits — they turn grass into the food that the "
                     "rest of the chain lives on.", "correct": False,
             "why": "Every level feeds the one above it, so that cannot be "
                    "the test. Rabbits eat, which makes them consumers — "
                    "primary consumers, the first level that does."},
            {"text": "The grass — it builds its own food from sunlight "
                     "instead of eating, so energy enters here.",
             "correct": True},
            {"text": "The golden eagle — everything below it in the chain "
                     "produces the energy that it needs.", "correct": False,
             "why": "The eagle eats, so it is a consumer — the tertiary one, "
                    "at the top. A chain is not built to supply its top "
                    "predator; the energy travels up, not to order."},
            {"text": "The grass — it is the only organism in the chain that "
                     "does not hunt anything at all.", "correct": False,
             "why": "Right organism, wrong reason. A caterpillar hunts "
                    "nothing either and is still a consumer. What makes a "
                    "producer is building its own food rather than eating."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e02",
        "band": "easier",
        "text": "A student says a food chain and a food web are two names for "
                "the same picture. What is the difference between them?",
        "options": [
            {"text": "A web shows all the feeding routes in an ecosystem at "
                     "once; a chain is one route pulled out of it.",
             "correct": True},
            {"text": "A web is used for large ecosystems and a chain for "
                     "small ones, but both show the same thing.",
             "correct": False,
             "why": "Size of the place does not decide it. What decides it is "
                    "how many routes are drawn — a pond web and an ocean web "
                    "are both webs because both draw every route."},
            {"text": "A chain shows where the energy goes; a web shows which "
                     "organisms live in the same place.", "correct": False,
             "why": "Both are energy pictures. Every solid arrow in a web "
                    "means energy passing from the eaten to the eater, "
                    "exactly as in a chain. A web just draws many at once."},
            {"text": "A web is a food chain with the decomposers added on to "
                     "the end of it.", "correct": False,
             "why": "Decomposers are not on the end of anything — they feed "
                    "on dead material from every level, underneath the whole "
                    "picture. A web is many feeding routes drawn together."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e03",
        "band": "easier",
        "text": "In the oak wood web, exactly one arrow touches the "
                "ladybirds: it runs from the aphids to the ladybirds. What "
                "does that tell you?",
        "options": [
            {"text": "The ladybirds are eaten by the aphids, and by nothing "
                     "else in the wood.", "correct": False,
             "why": "That is the arrow read backwards, and it is the most "
                    "marked error in this topic. An arrow runs from the eaten "
                    "towards the eater, so here the ladybirds are eating."},
            {"text": "Only one animal in the whole wood eats ladybirds.",
             "correct": False,
             "why": "That would be an arrow LEAVING the ladybirds, and there "
                    "is none. Arrows going in are what an organism eats; "
                    "arrows coming out are what eats it."},
            {"text": "The ladybirds feed on aphids and on nothing else in "
                     "this wood.", "correct": True},
            {"text": "The ladybirds are producers, since only one thing feeds "
                     "into them.", "correct": False,
             "why": "A producer has nothing feeding into it at all, because "
                    "it builds its own food. One arrow in means one food "
                    "source, which makes the ladybirds a consumer."},
        ],
        "figure": "b9-oak-wood-web-thread",
    },
    {
        "id": "b9-01-e04",
        "band": "easier",
        "text": "Where do decomposers belong on the picture of a food chain?",
        "options": [
            {"text": "On the very end, after the top predator, because they "
                     "are the last thing to feed.", "correct": False,
             "why": "This is the usual way of drawing them and it is wrong. "
                    "Bacteria and fungi feed on dead material and droppings "
                    "from every level, not only from the top one."},
            {"text": "At the bottom, below the producers, because they put "
                     "minerals back into the soil.", "correct": False,
             "why": "They do return the minerals, but that does not make them "
                    "producers. A producer builds its own food from sunlight; "
                    "a decomposer feeds on what was already alive."},
            {"text": "Nowhere on it at all, because they only feed on things "
                     "that are already dead.", "correct": False,
             "why": "Feeding on dead material is still feeding, and the "
                    "energy in it came up the chain the same way. They belong "
                    "on the picture — just not on the end of it."},
            {"text": "Underneath every level, feeding on dead material and "
                     "droppings from all of them.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-01-s01",
        "band": "standard",
        "text": "On the bench, the grass holds 10,000 kJ and about a tenth "
                "passes on at each step. How much reaches the foxes?",
        "options": [
            {"text": "1,000 kJ, because a tenth of 10,000 kJ is 1,000 kJ, "
                     "and the foxes eat rabbits.",
             "correct": False,
             "why": "That is what reaches the rabbits. The foxes are one step "
                    "further up, so take a tenth again: 100 kJ."},
            {"text": "9,000 kJ, because only a tenth of the energy is lost at "
                     "each step.", "correct": False,
             "why": "It is the other way round. About a tenth is passed ON, "
                    "and the other nine tenths leave the chain — mostly "
                    "warming the surroundings through respiration."},
            {"text": "100 kJ, because it takes two steps: grass to "
                     "rabbits, then rabbits to foxes.", "correct": True},
            {"text": "10 kJ, because the field chain has four levels in it "
                     "altogether.", "correct": False,
             "why": "10 kJ is what reaches the golden eagle, at the top. "
                    "Count the steps between the grass and the foxes, not the "
                    "levels in the whole chain."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s02",
        "band": "standard",
        "text": "Both chains start with 10,000 kJ. The field chain has four "
                "levels and ends at a golden eagle; the open-sea chain has "
                "five and ends at an orca. What arrives at each top?",
        "options": [
            {"text": "10 kJ at the eagle and 1 kJ at the orca — the extra "
                     "level costs a tenth again.", "correct": True},
            {"text": "10 kJ at both, because the two chains started with "
                     "exactly the same 10,000 kJ.", "correct": False,
             "why": "The starting amount is the same, but the sea chain has "
                    "one more step and every step keeps only about a tenth. "
                    "One kilojoule arrives at the orca."},
            {"text": "More at the orca, because an orca is far larger than an "
                     "eagle and needs more energy.", "correct": False,
             "why": "How much arrives is decided by the number of steps, not "
                    "by the size of the animal at the top. It is exactly why "
                    "an orca has to hunt across whole oceans."},
            {"text": "1 kJ at both, because five levels is the limit for any "
                     "chain anywhere on Earth.", "correct": False,
             "why": "Four or five levels is about the limit, but the eagle "
                    "sits at the fourth level and 10 kJ reaches it. Only a "
                    "fifth level is down to one kilojoule."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s03",
        "band": "standard",
        "text": "In the oak wood web, one arrow runs from the mice all the "
                "way up to the sparrowhawk, crossing a whole row. What does "
                "that arrow show?",
        "options": [
            {"text": "That the mice must really be secondary consumers, since "
                     "they feed a tertiary consumer like the hawk.",
             "correct": False,
             "why": "What an organism EATS decides its level, not what eats "
                    "it. Mice eat acorns and seeds, so they are primary "
                    "consumers however many predators they have."},
            {"text": "That a sparrowhawk feeds at more than one level, on "
                     "blue tits and mice — a web is not a ladder.",
             "correct": True},
            {"text": "That the arrow is drawn the wrong way and should run "
                     "from the sparrowhawk down to the mice.",
             "correct": False,
             "why": "The arrow follows the energy, from the eaten towards the "
                    "eater. The mice are eaten, so it leaves them. Nothing "
                    "travels from a hawk down into a mouse."},
            {"text": "That mice and blue tits are the same kind of consumer, "
                     "since one predator eats both of them.", "correct": False,
             "why": "They are not. Blue tits eat caterpillars and aphids, so "
                    "they are secondary; mice eat acorns and seeds, so they "
                    "are primary. Sharing a predator says nothing about it."},
        ],
        "figure": "b9-oak-wood-web-thread",
    },
    {
        "id": "b9-01-s04",
        "band": "standard",
        "text": "Every chain in this lesson begins with a plant or an alga. "
                "Why can no food chain begin with an animal?",
        "options": [
            {"text": "Because animals move around, so they cannot stay in one "
                     "place at the bottom of a chain.", "correct": False,
             "why": "Staying still is not what makes a producer. Algae drift "
                    "across whole oceans and are producers all the same, "
                    "because they build their own food rather than eating."},
            {"text": "Because a chain that began with an animal would be too "
                     "short to be worth drawing at all.", "correct": False,
             "why": "Length is not the problem — where the energy came from "
                    "is. An animal cannot make its own, so something has to "
                    "have captured it from sunlight first."},
            {"text": "Because animals are always eaten by something else, so "
                     "they can never be the first link.", "correct": False,
             "why": "Plenty of animals are eaten by nothing at all — a golden "
                    "eagle is the top of its chain. Being eaten is not what "
                    "decides where an organism sits."},
            {"text": "Because energy enters the living world only through "
                     "producers, and an animal has to eat.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-01-h01",
        "band": "harder",
        "text": "Baleen whales are the largest animals that have ever lived, "
                "and they feed on krill, which graze phytoplankton — only two "
                "steps above the producers. Why so far down a chain?",
        "options": [
            {"text": "Because krill are slow and easy to catch, so a whale "
                     "can gather them without wasting much effort.",
             "correct": False,
             "why": "Ease of catching is not the limit. Even if a fifth-level "
                    "food were easy to catch, that level would not hold "
                    "enough energy to run an animal of that size."},
            {"text": "Because a whale is too large and slow to hunt fish, so "
                     "it has to take the smallest prey there is.",
             "correct": False,
             "why": "The size is the consequence, not the cause. The "
                    "arithmetic comes first: only the bottom of a chain holds "
                    "enough energy to build that much animal at all."},
            {"text": "Because krill hold more energy per mouthful than fish "
                     "do, which is why a whale prefers them.", "correct": False,
             "why": "Energy per mouthful is not the point — what the whole "
                    "LEVEL holds is. Two steps up still holds about a "
                    "hundredth of the original; four steps up, a "
                    "ten-thousandth."},
            {"text": "Because each step up leaves about a tenth as much "
                     "energy, so only the bottom holds enough.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h02",
        "band": "harder",
        "text": "A study of one lake measures 18% of the energy at one level "
                "reaching the next. Does that show the tenth-of-the-energy "
                "rule is wrong?",
        "options": [
            {"text": "Yes — the measurement is real and the rule is not, so "
                     "the rule ought to be dropped.", "correct": False,
             "why": "The rule was never a measurement of one place. It is a "
                    "teaching average across many ecosystems, and 18% sits "
                    "inside the range that real ones give."},
            {"text": "No — a tenth is a teaching average, and real "
                     "efficiencies run from a few per cent to around twenty.",
             "correct": True},
            {"text": "Yes — but only for lakes, because water carries energy "
                     "differently from the way land does.", "correct": False,
             "why": "The spread is wide everywhere, in water and on land. "
                    "This lesson's own open-sea chain uses exactly the same "
                    "tenth that the field chain uses."},
            {"text": "No — 18% is close enough to 10% that the difference "
                     "does not really matter here.", "correct": False,
             "why": "Nearly right, for the wrong reason. 18% is not close to "
                    "10% — it is almost double. The point is that a tenth is "
                    "an average with a real spread around it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h03",
        "band": "harder",
        "text": "Someone claims to have found a food chain in a rainforest "
                "with eight links in it. What does this lesson's arithmetic "
                "say about that claim?",
        "options": [
            {"text": "Seven steps at a tenth each leave a ten-millionth "
                     "of the plants' energy — too little to live on.",
             "correct": True},
            {"text": "It is possible in a rainforest, because rainforests "
                     "capture far more sunlight than other ecosystems do.",
             "correct": False,
             "why": "More energy at the bottom does not buy more levels. Each "
                    "step still keeps only a tenth, so an eighth level holds "
                    "a ten-millionth of it however large the start was."},
            {"text": "It is possible if every organism in the chain is very "
                     "small, since each one then needs less energy.",
             "correct": False,
             "why": "The limit holds whether the organisms are enormous or "
                    "microscopic. The open-sea chain here is microscopic at "
                    "the bottom and it still stops at five levels."},
            {"text": "It is impossible, because a food chain can never have "
                     "more than four links in any ecosystem.", "correct": False,
             "why": "Four or five is about the limit, not a fixed four — the "
                    "open-sea chain in this lesson runs to five. Eight fails "
                    "on the arithmetic, not on a hard rule."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h04",
        "band": "harder",
        "text": "You are handed a food web from an ecosystem you have never "
                "seen, with the organisms unnamed. Using the arrows alone, "
                "how do you pick out the producers?",
        "options": [
            {"text": "They are the ones with the most arrows pointing into "
                     "them, because energy collects at the bottom.",
             "correct": False,
             "why": "That reads the arrows backwards. An arrow pointing into "
                    "an organism means it is eating something, and a producer "
                    "eats nothing at all."},
            {"text": "They are the ones with no arrows leaving them, because "
                     "nothing takes energy out of a producer.",
             "correct": False,
             "why": "That describes the top predator, which nothing eats. "
                    "Energy leaves a producer constantly — everything above "
                    "it in the web is living on what left."},
            {"text": "They are the only ones with no feeding arrow pointing "
                     "into them, because they eat nothing.", "correct": True},
            {"text": "They are the ones with the most arrows leaving them, "
                     "because the whole web depends on them.",
             "correct": False,
             "why": "A heavily eaten plant eater can have several arrows out "
                    "too. Counting arrows is not the test — the direction is, "
                    "and nothing feeds into a producer."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-01-e05",
        "band": "easier",
        "text": "A food chain runs: oak leaves, caterpillars, blue tits, "
                "sparrowhawk. Which organism is the primary consumer?",
        "options": [
            {"text": "The oak leaves, because the whole chain is built out of "
                     "what they capture.", "correct": False,
             "why": "The oak is the producer. Primary consumer means the "
                    "first level that eats, and a producer eats nothing at "
                    "all."},
            {"text": "The caterpillars, because they are the first organisms "
                     "in the chain that eat.", "correct": True},
            {"text": "The blue tits, because they are the first animals that "
                     "hunt for their food.", "correct": False,
             "why": "Blue tits eat caterpillars, which are consumers "
                    "themselves, so the blue tits are secondary. Primary "
                    "means feeding on the producer."},
            {"text": "The sparrowhawk, because everything below it in the "
                     "chain feeds it.", "correct": False,
             "why": "The sparrowhawk is at the top, which makes it a tertiary "
                    "consumer. The levels are counted upwards from the "
                    "producers, not downwards from the top."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e06",
        "band": "easier",
        "text": "What does the word consumer mean in a food chain?",
        "options": [
            {"text": "An organism that uses up energy, so that less of it is "
                     "left for the level above.", "correct": False,
             "why": "Every organism uses energy, producers included. A "
                    "consumer is named for how it gets its energy, which is "
                    "by eating."},
            {"text": "An organism that is eaten by the level above it in the "
                     "chain.", "correct": False,
             "why": "Almost everything is eaten by something, including the "
                    "producers. What makes an organism a consumer is that it "
                    "eats, not that it is eaten."},
            {"text": "An animal that hunts and kills other animals for its "
                     "food.", "correct": False,
             "why": "That describes a predator. A rabbit hunts nothing and is "
                    "still a consumer, because it gets its energy by eating a "
                    "plant."},
            {"text": "An organism that gets its energy by eating other "
                     "organisms.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e07",
        "band": "easier",
        "text": "A food chain begins with grass, which is eaten by rabbits. "
                "Where did the energy in the grass come from in the first "
                "place?",
        "options": [
            {"text": "From sunlight, which the grass captured and built into "
                     "plant material.", "correct": True},
            {"text": "From the soil, which holds the minerals the grass grew "
                     "out of.", "correct": False,
             "why": "The grass does take minerals from the soil, and minerals "
                    "are not energy. The energy came from light."},
            {"text": "From the decomposers, which return it to the soil when "
                     "they break down dead material.", "correct": False,
             "why": "Decomposers return minerals to the soil, not energy. The "
                    "energy in dead material is released to the surroundings "
                    "and does not go back into a plant."},
            {"text": "From the rabbits, whose droppings fertilise the field "
                     "the grass grows in.", "correct": False,
             "why": "Droppings return minerals, and the energy in them came "
                    "out of the grass to begin with. Nothing further up a "
                    "chain supplies the energy at the bottom of it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e08",
        "band": "easier",
        "text": "About how much of the energy at one level of a food chain "
                "reaches the level above it?",
        "options": [
            {"text": "About nine tenths of it.", "correct": False,
             "why": "Nine tenths is the share that leaves the chain, not the "
                    "share that arrives. It is the commonest way round to get "
                    "this one wrong."},
            {"text": "About half of it.", "correct": False,
             "why": "Half would allow far longer chains than any that exist. "
                    "The figure is roughly a tenth, which is why four or five "
                    "links is the limit."},
            {"text": "About a tenth of it.", "correct": True},
            {"text": "Almost all of it, because energy cannot be destroyed.",
             "correct": False,
             "why": "Energy is not destroyed, and it still leaves the chain — "
                    "most of it warms the surroundings through respiration. "
                    "Only about a tenth is passed on."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e09",
        "band": "easier",
        "text": "Ecologists call each feeding level in a chain a trophic "
                "level. What does that mean?",
        "options": [
            {"text": "The number of different foods an organism eats.",
             "correct": False,
             "why": "That is how varied its diet is, which is what a web "
                    "shows. A trophic level is a feeding position, counted "
                    "upwards from the producers."},
            {"text": "The amount of energy an organism holds in its body.",
             "correct": False,
             "why": "Energy falls as you go up the levels, and the level "
                    "itself is a position in the chain rather than a "
                    "quantity."},
            {"text": "The position an organism is drawn in, reading the web "
                     "from left to right.", "correct": False,
             "why": "Where something is drawn is a matter of layout. A "
                    "trophic level is counted from the producers upwards, "
                    "however the organisms are arranged."},
            {"text": "A feeding level in a chain, counted from the producers "
                     "upwards.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-01-s05",
        "band": "standard",
        "text": "In each of these chains the arrows would run from left to "
                "right. Which one has been written correctly?",
        "options": [
            {"text": "Fox, rabbit, grass — because the fox is the most "
                     "important animal in the field.", "correct": False,
             "why": "Importance never decides the direction. The arrows "
                    "follow the energy, and the energy runs from the grass to "
                    "the rabbit to the fox."},
            {"text": "Rabbit, grass, fox — because the rabbit turns grass "
                     "into the food the fox eats.", "correct": False,
             "why": "The rabbit does not feed the grass. A chain starts where "
                    "energy enters the living world, which is always the "
                    "producer."},
            {"text": "Phytoplankton, zooplankton, herring, seal — because "
                     "energy enters at the plankton and passes up.",
             "correct": True},
            {"text": "Herring, zooplankton, phytoplankton, seal — because the "
                     "seal is the last thing to feed.", "correct": False,
             "why": "Written that way the chain says herring feed the "
                    "zooplankton and plankton feed the seal, and neither "
                    "happens. Start at the producer and follow the energy."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s06",
        "band": "standard",
        "text": "A golden eagle holds a territory of many square kilometres, "
                "while a rabbit lives its whole life in a few square metres. "
                "Why does the eagle need so much more ground?",
        "options": [
            {"text": "Because only about a tenth passes on at each step, so "
                     "an eagle's food is spread very thinly.", "correct": True},
            {"text": "Because an eagle is much larger than a rabbit, and a "
                     "large animal needs more room to move.", "correct": False,
             "why": "Body size is not the reason. A cow is larger than an "
                    "eagle and grazes one field, because it feeds one step "
                    "above the producers where the energy still is."},
            {"text": "Because eagles hunt by flying, and flying uses far more "
                     "energy than sitting still.", "correct": False,
             "why": "Flight is expensive, and that is part of why so little "
                    "of what an eagle eats becomes eagle. It does not explain "
                    "why the food itself is so thinly spread."},
            {"text": "Because eagles will not tolerate each other, so each "
                     "one drives the others away.", "correct": False,
             "why": "They do defend a territory, and the question is why it "
                    "has to be that large. There is very little energy left "
                    "at the fourth level to feed a bird from."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s07",
        "band": "standard",
        "text": "Every bacterium and fungus in a field is killed. What "
                "happens over the years that follow?",
        "options": [
            {"text": "The grass grows better, because the bacteria and fungi "
                     "were competing with it for minerals.", "correct": False,
             "why": "Decomposers are what put those minerals into the soil in "
                    "the first place. Removing them starves the grass rather "
                    "than freeing it."},
            {"text": "The animals at the top of the chain are affected first, "
                     "being furthest from the soil.", "correct": False,
             "why": "The bottom goes first here. The producers lose the "
                    "minerals they need, and everything above them is living "
                    "on the producers."},
            {"text": "Nothing changes, because decomposers only feed on "
                     "things that are already dead.", "correct": False,
             "why": "Feeding on dead material is the job that returns "
                    "minerals to the soil. Stop it and dead material piles up "
                    "while the soil runs down."},
            {"text": "Dead material builds up, the soil runs short of "
                     "minerals, and the plants grow less.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s08",
        "band": "standard",
        "text": "A caterpillar passes on a larger share of the energy it eats "
                "than a fox does. Which explanation fits?",
        "options": [
            {"text": "A caterpillar is smaller, and small animals always "
                     "waste less energy than large ones.", "correct": False,
             "why": "Size is not the rule. A caterpillar keeps more because "
                    "it does almost nothing but eat, while a fox spends most "
                    "of its food on hunting and on staying warm."},
            {"text": "A caterpillar does little but eat, while a fox is warm "
                     "and active and spends far more on living.",
             "correct": True},
            {"text": "A caterpillar eats leaves, and leaves hold more energy "
                     "per gram than meat does.", "correct": False,
             "why": "Meat holds more energy per gram than a leaf. What "
                    "matters is how much of the food is spent on living "
                    "rather than on growing."},
            {"text": "A fox eats less often than a caterpillar, so less "
                     "energy reaches it in the first place.", "correct": False,
             "why": "How often an animal eats is not the share it passes on. "
                    "A fox spends a great deal of what it eats on hunting and "
                    "on keeping warm, and that energy leaves the chain."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s09",
        "band": "standard",
        "text": "A student says the heron at the top of a pond chain is a "
                "producer for the pond, because its droppings feed the algae. "
                "Why is that wrong?",
        "options": [
            {"text": "Because droppings are waste, and waste holds no energy "
                     "at all.", "correct": False,
             "why": "Droppings do hold energy — it is what the decomposers "
                    "live on. The mistake is in what the word producer "
                    "means."},
            {"text": "Because the heron is an animal, and only plants can be "
                     "producers.", "correct": False,
             "why": "Right conclusion, wrong reason. Algae are not plants and "
                    "are producers, because they build their own food from "
                    "sunlight."},
            {"text": "Because a producer builds its own food from sunlight, "
                     "and a heron has to eat.", "correct": True},
            {"text": "Because the algae take their minerals from the water "
                     "rather than from droppings.", "correct": False,
             "why": "Minerals from droppings do reach the water and the algae "
                    "do use them. Returning minerals is not producing food, "
                    "and it puts no energy back into the chain."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-01-h05",
        "band": "harder",
        "text": "A tawny owl at the fourth level of a chain receives about "
                "8 kJ. Taking a tenth as the share passed on at each step, "
                "roughly how much did the producers capture?",
        "options": [
            {"text": "About 80 kJ, because there is one step between the owl "
                     "and the producers.", "correct": False,
             "why": "There are three steps between the first level and the "
                    "fourth, not one, and each of them multiplies by ten as "
                    "you work back down."},
            {"text": "About 8,000 kJ, because working back down three steps "
                     "multiplies by ten each time.", "correct": True},
            {"text": "About 80,000 kJ, because the owl sits at the fourth "
                     "level of the chain.", "correct": False,
             "why": "That is four steps rather than three. The producers are "
                    "the first level and the owl the fourth, so three "
                    "transfers separate them."},
            {"text": "About 0.008 kJ, because a tenth is lost at every step "
                     "down the chain.", "correct": False,
             "why": "Working downwards you multiply rather than divide. There "
                    "is far more energy at the bottom of a chain than at the "
                    "top, not less."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h06",
        "band": "harder",
        "text": "Two woods capture the same amount of energy in their plants "
                "each year. In the first, the longest chain has three levels; "
                "in the second, five. Which supports more top predators?",
        "options": [
            {"text": "The second, because a longer chain means more levels "
                     "feeding the top of it.", "correct": False,
             "why": "The levels below do not add together at the top. Each "
                    "step passes on about a tenth, so a longer chain arrives "
                    "with less rather than more."},
            {"text": "The second, because a wood able to support five levels "
                     "must be the richer of the two.", "correct": False,
             "why": "Both woods capture the same energy, which is what the "
                    "question fixes. The difference is how many steps that "
                    "energy has to pass through."},
            {"text": "Neither, because the number of top predators depends "
                     "only on how much the plants capture.", "correct": False,
             "why": "Both things matter. The same capture spread over five "
                    "levels leaves about a hundredth as much at the top as "
                    "three levels would."},
            {"text": "The first, because the energy passes through fewer "
                     "steps before it reaches the top.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h07",
        "band": "harder",
        "text": "A group wants more sparrowhawks in a wood. Sparrowhawks eat "
                "blue tits, blue tits eat caterpillars, and caterpillars eat "
                "oak leaves. Which action is most likely to work?",
        "options": [
            {"text": "Plant more oaks, so more energy enters the wood and "
                     "more of it reaches every level above.", "correct": True},
            {"text": "Release more sparrowhawks, so that the population "
                     "starts from a larger number.", "correct": False,
             "why": "The wood can only feed as many hawks as the energy "
                    "reaching that level allows. Extra birds would starve or "
                    "leave, and the number would settle back."},
            {"text": "Remove the owls, so that the sparrowhawks have less "
                     "competition for food.", "correct": False,
             "why": "Owls eat mice, which are not a sparrowhawk's main food. "
                    "Removing one species to help another usually moves a "
                    "problem rather than solving it."},
            {"text": "Cut back the brambles and undergrowth, so that the "
                     "hawks can hunt more easily.", "correct": False,
             "why": "Sparrowhawks hunt by surprise among cover, so this may "
                    "make hunting harder. Either way it adds no energy to the "
                    "wood, and the energy is what sets the number."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h08",
        "band": "harder",
        "text": "An owl dies in a wood and fungi feed on the body. Does the "
                "energy in the owl return to the oak the chain began with?",
        "options": [
            {"text": "Yes — the fungi return it to the soil, and the oak "
                     "takes it up through its roots.", "correct": False,
             "why": "What returns to the soil is minerals, not energy. A "
                    "plant takes up minerals and water through its roots; the "
                    "energy it uses comes from light."},
            {"text": "Yes, but slowly, because the energy has to pass back "
                     "down every level of the chain.", "correct": False,
             "why": "Energy never travels back down a chain. There is no "
                    "route from a dead owl to an oak leaf for it to take."},
            {"text": "No — the minerals return to the soil, but the energy is "
                     "released to the surroundings.", "correct": True},
            {"text": "No, because the fungi keep all of the energy in the "
                     "owl's body for themselves.", "correct": False,
             "why": "The fungi use it, and using it means respiring it, so "
                    "most of it warms the surroundings. Nothing is kept for "
                    "ever, and none of it travels back up."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h09",
        "band": "harder",
        "text": "A zoo finds that feeding one snow leopard costs far more "
                "than feeding a group of goats of the same total mass. "
                "Explain that using the food chain.",
        "options": [
            {"text": "Because a wild animal eats more for its size than a "
                     "farm animal does.", "correct": False,
             "why": "Wildness is not the cost. Meat is expensive because "
                    "growing it took roughly ten times its own mass of plant "
                    "food first."},
            {"text": "Because the meat it eats had to be grown by feeding "
                     "plants to another animal first.", "correct": True},
            {"text": "Because meat holds far more energy per kilogram than "
                     "plants do, so it costs more to buy.", "correct": False,
             "why": "Meat does hold more energy per kilogram, and that is not "
                    "what makes it expensive. The cost is the level it comes "
                    "from — an animal ate about ten kilograms of plants to "
                    "add one of itself."},
            {"text": "Because a predator has to be fed every day, while goats "
                     "can be left to graze.", "correct": False,
             "why": "Both animals eat every day. The difference is that the "
                    "goats feed one step above the producers and the leopard "
                    "feeds one step above the goats."},
        ],
        "figure": None,
    },
]
