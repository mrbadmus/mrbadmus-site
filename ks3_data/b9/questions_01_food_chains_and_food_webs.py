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
        "text": "Look at the oak wood web. Find the ladybirds, and look at "
                "the arrows touching them. What does that tell you?",
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
        "text": "Look at the oak wood web. Find the arrow that runs from the "
                "mice to the sparrowhawk. What does that arrow show?",
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

    # ── MRB-338 top-up · easier ─────────────────────────────────────────
    {
        "id": "b9-01-e10",
        "band": "easier",
        "text": "Phytoplankton are microscopic algae drifting near the "
                "surface of the open sea. What job do they do in a sea food "
                "chain?",
        "options": [
            {"text": "They are the primary consumers, grazing on the bacteria "
                     "that drift around them.", "correct": False,
             "why": "A primary consumer eats a producer. An alga eats nothing "
                    "— it builds its own food."},
            {"text": "They are the producers, building their own food from "
                     "sunlight.", "correct": True},
            {"text": "They are decomposers, living on what sinks past them.",
             "correct": False,
             "why": "Decomposers feed on dead material. Phytoplankton "
                    "photosynthesise, which is the opposite arrangement."},
            {"text": "They are the smallest hunters in the plankton.",
             "correct": False,
             "why": "Being tiny does not make an organism a hunter. Algae "
                    "capture light, not prey."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e11",
        "band": "easier",
        "text": "In a hedgerow, mice eat hawthorn berries, weasels hunt the "
                "mice, and buzzards hunt the weasels. Which organism is the "
                "secondary consumer?",
        "options": [
            {"text": "The mice", "correct": False,
             "why": "They eat a plant, which makes them the primary consumer "
                    "— the first level that eats."},
            {"text": "The buzzards", "correct": False,
             "why": "A buzzard eats a weasel, which is itself a secondary "
                    "consumer, so the buzzard is one level higher."},
            {"text": "The weasels", "correct": True},
            {"text": "The hawthorn berries", "correct": False,
             "why": "The hawthorn is the producer of this hedgerow. A "
                    "producer consumes nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e12",
        "band": "easier",
        "text": "In the chain grass, rabbits, foxes, golden eagle, what name "
                "is given to the golden eagle's feeding level?",
        "options": [
            {"text": "The secondary consumer level, like the foxes",
             "correct": False,
             "why": "The foxes hold that level. The eagle eats foxes, which "
                    "puts it one step higher again."},
            {"text": "The decomposer level", "correct": False,
             "why": "Decomposers are bacteria and fungi feeding on dead "
                    "material. Having no predator does not make an eagle one."},
            {"text": "The second producer level", "correct": False,
             "why": "A chain has only one producer level and it is at the "
                    "bottom. Everything above it eats."},
            {"text": "The tertiary consumer level", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e13",
        "band": "easier",
        "text": "In a wood, bacteria and fungi feed on fallen leaves, "
                "droppings and dead animals. What are organisms like these "
                "called?",
        "options": [
            {"text": "Decomposers", "correct": True},
            {"text": "Scavengers", "correct": False,
             "why": "A scavenger is an animal eating a carcass it did not "
                    "kill. Bacteria and fungi have a name of their own."},
            {"text": "Producers", "correct": False,
             "why": "They return minerals to the soil, and that is not "
                    "producing. A producer builds its own food from sunlight."},
            {"text": "Tertiary consumers", "correct": False,
             "why": "They are not a level of the chain at all — they feed on "
                    "dead material from every level, including the producers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e14",
        "band": "easier",
        "text": "Decomposers feed on dead material from every level of a food "
                "web. What do they return to the soil as they do it?",
        "options": [
            {"text": "The oxygen the plant roots need", "correct": False,
             "why": "Decomposers use oxygen up as they respire, rather than "
                    "releasing it into the soil."},
            {"text": "The minerals the dead material held", "correct": True},
            {"text": "All the energy the dead organism held", "correct": False,
             "why": "The energy is released to the surroundings as the "
                    "decomposers respire. It does not travel back down."},
            {"text": "The sunlight the plants captured in the first place",
             "correct": False,
             "why": "Sunlight arrives fresh from the Sun and is never stored "
                    "in soil to be handed back."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e15",
        "band": "easier",
        "text": "An oak wood holds oak trees, caterpillars, blue tits and a "
                "sparrowhawk. Which of them builds its own food instead of "
                "eating?",
        "options": [
            {"text": "The caterpillars, which make new caterpillar out of leaves",
             "correct": False,
             "why": "Turning an eaten leaf into caterpillar is still eating. "
                    "Building your own food means not eating at all."},
            {"text": "The oak trees, the only ones that photosynthesise",
             "correct": True},
            {"text": "The sparrowhawk, which nothing supplies with food",
             "correct": False,
             "why": "The birds it hunts supply it. Having no predator is not "
                    "the same as feeding yourself."},
            {"text": "The blue tits, which forage for themselves",
             "correct": False,
             "why": "Gathering is not building. A blue tit takes material "
                    "another organism has already made."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e16",
        "band": "easier",
        "text": "A sea chain runs: phytoplankton, zooplankton, herring, "
                "seals. Which organism is the primary consumer?",
        "options": [
            {"text": "The zooplankton", "correct": True},
            {"text": "The phytoplankton, which come first", "correct": False,
             "why": "Coming first makes them the producer. A consumer has to "
                    "eat, and an alga does not."},
            {"text": "The herring, the first true fish here", "correct": False,
             "why": "Zooplankton are animals too, drifting ones, and the "
                    "herring eat them. That makes herring secondary."},
            {"text": "The seals, which hunt fish", "correct": False,
             "why": "Hunting does not decide a level; what an organism eats "
                    "does. Seals feed three steps above the algae."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e17",
        "band": "easier",
        "text": "Grass in a field captures 10,000 kJ of energy. About how "
                "much of that reaches the rabbits that eat the grass?",
        "options": [
            {"text": "About 1,000 kJ, a tenth of what the grass captured",
             "correct": True},
            {"text": "About 100 kJ, a tenth of a tenth", "correct": False,
             "why": "That is two steps' worth of loss. Grass to rabbits is "
                    "one step, so divide by ten once only."},
            {"text": "About 9,000 kJ, with a tenth lost", "correct": False,
             "why": "This is the tenth read the wrong way round. A tenth "
                    "ARRIVES; the other nine tenths do not."},
            {"text": "About 10,000 kJ, since nothing is lost on the way",
             "correct": False,
             "why": "Most of what a rabbit eats is respired or passes "
                    "through. Only about a tenth becomes rabbit."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e18",
        "band": "easier",
        "text": "An ecologist writes down how much energy each level of a "
                "food chain holds. Which unit does she use?",
        "options": [
            {"text": "Degrees Celsius", "correct": False,
             "why": "Degrees measure temperature. A warm mouse and a warm "
                    "elephant do not hold the same energy."},
            {"text": "Kilojoules", "correct": True},
            {"text": "Kilograms", "correct": False,
             "why": "Kilograms measure mass. Two organisms of equal mass can "
                    "hold quite different amounts of energy."},
            {"text": "The number of organisms at each level", "correct": False,
             "why": "A count is not an energy. One oak and one caterpillar "
                    "each count as one and hold wildly different amounts."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e19",
        "band": "easier",
        "text": "About how many feeding levels does a food chain usually "
                "reach before it stops?",
        "options": [
            {"text": "About ten, which is why long chains are the normal kind",
             "correct": False,
             "why": "No chain that long has ever been found. By the tenth "
                    "level there is almost nothing left to live on."},
            {"text": "Two, one producer and one consumer", "correct": False,
             "why": "Plenty of chains reach four or five. Two is far short of "
                    "what a real ecosystem manages."},
            {"text": "Four or five, on land or at sea", "correct": True},
            {"text": "As many as the ecosystem is large enough to hold",
             "correct": False,
             "why": "Area is not the limit. What runs out is the energy, and "
                    "it runs out after four or five steps whatever the size."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e20",
        "band": "easier",
        "text": "Orcas feed on seals, which are already the tertiary "
                "consumers of their chain. What is the orca's level called?",
        "options": [
            {"text": "A tertiary consumer, the same level as the seals",
             "correct": False,
             "why": "An organism cannot share a level with what it eats. "
                    "Eating a tertiary consumer puts it one step higher."},
            {"text": "A secondary consumer, counting from the seals",
             "correct": False,
             "why": "Counting starts at the producers, not at whichever "
                    "animal you happen to look at first."},
            {"text": "A second producer, starting the chain again",
             "correct": False,
             "why": "A chain never restarts part way up. Producers are only "
                    "ever at the bottom of one."},
            {"text": "A quaternary consumer, one step above the seals",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e21",
        "band": "easier",
        "text": "In almost every ecosystem, one feeding level holds far more "
                "animals than any other. Which level is it?",
        "options": [
            {"text": "The secondary consumers, which can eat plants as well "
                     "as animals", "correct": False,
             "why": "A secondary consumer eats animals, and its level holds "
                    "about a tenth of the energy of the one below it."},
            {"text": "The primary consumers, the animals that eat producers",
             "correct": True},
            {"text": "The top predators, which nothing is hunting",
             "correct": False,
             "why": "Top predators are the rarest animals in an ecosystem — "
                    "very little energy reaches their level."},
            {"text": "All levels hold the same number", "correct": False,
             "why": "Numbers fall sharply at every step up, because the "
                    "energy available falls sharply too."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e22",
        "band": "easier",
        "text": "A whole oak wood supports one pair of sparrowhawks and no "
                "more. What does that tell you about animals at the top of a "
                "chain?",
        "options": [
            {"text": "They breed slowly, which keeps numbers down",
             "correct": False,
             "why": "Breeding rate is not the limit. Even a fast-breeding top "
                    "predator would find no food for the extra young."},
            {"text": "They are rare, because little energy reaches their "
                     "level", "correct": True},
            {"text": "They need a very great deal of open room to fly about in",
             "correct": False,
             "why": "The large range is a consequence, not a cause. They "
                    "range widely because their food is spread so thinly."},
            {"text": "They are the largest animals in the ecosystem",
             "correct": False,
             "why": "Size does not follow the level — plenty of top predators "
                    "are small. What follows the level is rarity."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e23",
        "band": "easier",
        "text": "Which two groups of living things are the producers of the "
                "world's ecosystems?",
        "options": [
            {"text": "Algae and bacteria", "correct": False,
             "why": "Algae do produce, and most bacteria feed on material "
                    "other organisms made. Size is not what decides it."},
            {"text": "Plants and fungi", "correct": False,
             "why": "Fungi feed on dead material rather than building their "
                    "own food, which makes them decomposers."},
            {"text": "Plants and algae", "correct": True},
            {"text": "Plants and plant-eating animals", "correct": False,
             "why": "A herbivore eats plants, which makes it a consumer. Only "
                    "one of the two is at the bottom."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e24",
        "band": "easier",
        "text": "Herring feed on zooplankton, and zooplankton graze on "
                "phytoplankton. Which trophic level are the herring at?",
        "options": [
            {"text": "The fourth level, counting the seawater", "correct": False,
             "why": "Seawater is not an organism and holds no level. The "
                    "count starts at the producers."},
            {"text": "The second level, one step too low", "correct": False,
             "why": "The zooplankton are level two. Eating them puts the "
                    "herring one level higher again."},
            {"text": "The first level", "correct": False,
             "why": "Level one is the producers. The herring feed two steps "
                    "above them."},
            {"text": "The third level", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e25",
        "band": "easier",
        "text": "In one chain the plants capture 20,000 kJ and 20 kJ reaches "
                "the animal at the top. What percentage of the plants' energy "
                "is that?",
        "options": [
            {"text": "0.1%, which is one thousandth of what was captured",
             "correct": True},
            {"text": "1%, the usual share at the top of any chain",
             "correct": False,
             "why": "1% of 20,000 kJ is 200 kJ. The figure given is ten times "
                    "smaller than that."},
            {"text": "10%, the share that passes on at a step",
             "correct": False,
             "why": "A tenth passes on at EACH step, and the tenths multiply, "
                    "so far less than 10% reaches the top."},
            {"text": "20%, the most an ecologist ever measures",
             "correct": False,
             "why": "That figure is the ceiling for one single step, not for "
                    "a whole chain."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e26",
        "band": "easier",
        "text": "What is the difference between a primary consumer and a "
                "secondary consumer?",
        "options": [
            {"text": "A primary consumer eats first, and the secondary consumer "
                     "eats what it leaves", "correct": False,
             "why": "Nothing is left over and shared out. The names say which "
                    "level each one feeds on."},
            {"text": "A primary consumer eats producers; a secondary consumer "
                     "eats primary consumers", "correct": True},
            {"text": "A primary consumer lives there all year; a secondary "
                     "consumer only visits", "correct": False,
             "why": "Neither name says anything about where an organism "
                    "lives. Both are about feeding."},
            {"text": "A primary consumer is small and a secondary consumer is "
                     "larger", "correct": False,
             "why": "Size does not decide a level. A whale is enormous and "
                    "feeds one step above the producers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e27",
        "band": "easier",
        "text": "A student writes the chain: oak, caterpillar, blue tit, "
                "sparrowhawk. How many trophic levels does it have?",
        "options": [
            {"text": "Five", "correct": False,
             "why": "Sunlight is not an organism. The first level is the "
                    "producer that captures it."},
            {"text": "Six", "correct": False,
             "why": "Count the organisms named: there are four, and each one "
                    "feeds at its own level."},
            {"text": "Four", "correct": True},
            {"text": "Three", "correct": False,
             "why": "The producers are level one. They are the level every "
                    "other one is counted from."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e28",
        "band": "easier",
        "text": "One large oak supports its whole food chain and hundreds of "
                "other species besides. What does that show about a producer?",
        "options": [
            {"text": "That a producer must be large", "correct": False,
             "why": "Microscopic algae support the whole of the open sea. "
                    "Size is not what makes a producer important."},
            {"text": "That the wood depends on the oak for shelter more than "
                     "for food", "correct": False,
             "why": "Shelter matters, and this is a food web. What the oak "
                    "supplies here is the energy everything runs on."},
            {"text": "That a producer only supports what eats it directly",
             "correct": False,
             "why": "The energy carries on upwards past those organisms to "
                    "every level above them."},
            {"text": "That the energy every other organism uses entered "
                     "through it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e29",
        "band": "easier",
        "text": "Ecologists number the trophic levels of a chain from the "
                "bottom upwards. Which organisms are at level one?",
        "options": [
            {"text": "The producers, the only level where energy enters",
             "correct": True},
            {"text": "The decomposers, underneath everything else",
             "correct": False,
             "why": "They do sit underneath the whole chain, and they are not "
                    "a numbered level of it."},
            {"text": "The primary consumers, as primary means the first",
             "correct": False,
             "why": "First CONSUMER, not first level. Something must be eaten "
                    "before there can be a consumer at all."},
            {"text": "The smallest organisms, whatever they eat",
             "correct": False,
             "why": "Size does not decide a level. A microscopic animal that "
                    "grazes algae still sits at level two."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-e30",
        "band": "easier",
        "text": "A seal has to eat several kilograms of fish every day. Which "
                "statement best explains why it needs so much?",
        "options": [
            {"text": "Fish hold very little energy for their own mass",
             "correct": False,
             "why": "Fish are an energy-rich food. The difficulty is how "
                    "little of the sea's energy reaches the seal's level."},
            {"text": "A seal wastes most of what it eats", "correct": False,
             "why": "Nothing is wasted — it is used, mostly on respiration. "
                    "The question is why so much is needed at all."},
            {"text": "It feeds three steps up, where little energy is left",
             "correct": True},
            {"text": "Cold water pushes food through it unused",
             "correct": False,
             "why": "A seal digests its food perfectly well. Cold water is a "
                    "reason to eat more, not a reason food goes unused."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ───────────────────────────────────────
    {
        "id": "b9-01-s10",
        "band": "standard",
        "text": "Oak leaves in a wood capture 5,000 kJ of energy in a "
                "season. About how much of it reaches the blue tits, two "
                "steps up the chain?",
        "options": [
            {"text": "About 50 kJ, a tenth of a tenth", "correct": True},
            {"text": "About 4,050 kJ, with a tenth lost twice over",
             "correct": False,
             "why": "This treats the tenth as the LOSS. A tenth is what "
                    "arrives, so most of the 5,000 kJ does not."},
            {"text": "About 5 kJ, three steps up the chain", "correct": False,
             "why": "Oak to caterpillars to blue tits is two steps, so divide "
                    "by ten twice, not three times."},
            {"text": "About 500 kJ, one step's worth", "correct": False,
             "why": "That is the caterpillars' share. The blue tits are one "
                    "step above them again."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s11",
        "band": "standard",
        "text": "A student draws a garden food web. Two arrows point into the "
                "blackbird: one from the earthworms and one from the berry "
                "bush. What does that tell you?",
        "options": [
            {"text": "The blackbird is eaten by both the worms and the bush",
             "correct": False,
             "why": "That is the arrows read backwards. An arrow points "
                    "towards the organism doing the eating."},
            {"text": "The blackbird feeds at two levels, on a producer and on "
                     "a consumer", "correct": True},
            {"text": "The blackbird is the top predator of the garden",
             "correct": False,
             "why": "Nothing in the two arrows says what eats the blackbird. "
                    "Arrows in show its food, not its safety."},
            {"text": "The blackbird is a producer with two sources",
             "correct": False,
             "why": "A producer has no arrows pointing into it at all, "
                    "because it builds its own food."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s12",
        "band": "standard",
        "text": "A pair of blue tits needs about a hundred caterpillars a day "
                "to raise a brood, and they nest so that the chicks hatch at "
                "the caterpillar peak. Why must they?",
        "options": [
            {"text": "Blue tits cannot digest any other food while they are "
                     "nesting, so the timing is fixed", "correct": False,
             "why": "Adult blue tits eat aphids and seeds quite happily. It "
                    "is the quantity the chicks need that fixes the timing."},
            {"text": "The caterpillars would eat the eggs if the timing were "
                     "wrong", "correct": False,
             "why": "Caterpillars eat oak leaves, not eggs. They are the "
                    "food, not a threat to the nest."},
            {"text": "Their chicks need a food supply that is only abundant "
                     "for a short time", "correct": True},
            {"text": "Caterpillars are easier to catch when there are fewer "
                     "of them about", "correct": False,
             "why": "Fewer caterpillars means more hunting for each one. The "
                    "peak is when a hundred a day is possible at all."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s13",
        "band": "standard",
        "text": "A student says herring must be primary consumers, because "
                "they feed on plankton. Why is that wrong?",
        "options": [
            {"text": "Herring feed on algae as well, which puts them lower "
                     "still", "correct": False,
             "why": "Herring are not algae-eaters. And feeding lower would "
                    "not help the argument — it would make it worse."},
            {"text": "Plankton are producers, so anything that eats them must "
                     "be secondary", "correct": False,
             "why": "Only the PHYTOplankton are producers, and something "
                    "eating a producer is primary, not secondary."},
            {"text": "A herring is a fish", "correct": False,
             "why": "What kind of animal it is does not set its level. What "
                    "it eats does."},
            {"text": "Zooplankton are animals, so a herring eats a consumer "
                     "and is secondary", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s14",
        "band": "standard",
        "text": "In an oak wood, ladybirds eat aphids and blue tits eat "
                "caterpillars. Both aphids and caterpillars feed on the oak. "
                "Why are ladybirds and blue tits at the same trophic level?",
        "options": [
            {"text": "Both eat plant-eaters, and a level depends on what an "
                     "organism eats", "correct": True},
            {"text": "Both are animals rather than plants, and every animal "
                     "in a wood sits at level two", "correct": False,
             "why": "Animals are spread across every level above the first. "
                    "A sparrowhawk is an animal and sits at level four."},
            {"text": "Both are hunted by the sparrowhawk, which fixes their "
                     "level for them", "correct": False,
             "why": "Sparrowhawks take blue tits, not ladybirds — and what "
                    "eats an organism never sets its level anyway."},
            {"text": "Both are small enough to be eaten by the same predators "
                     "here", "correct": False,
             "why": "Size decides nothing. A whale feeds one step above the "
                    "producers and a ladybird two."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s15",
        "band": "standard",
        "text": "A shrew and a snake have the same mass and eat the same "
                "amount of food. Which of them passes more of that energy on "
                "to whatever eats it?",
        "options": [
            {"text": "The shrew, because it is warm and active all the time",
             "correct": False,
             "why": "Staying warm is exactly what SPENDS the energy. A warm "
                    "animal has less of it left to pass on."},
            {"text": "The snake, because it does not spend energy keeping "
                     "warm", "correct": True},
            {"text": "Neither — the tenth applies to both", "correct": False,
             "why": "A tenth is an average across many organisms. Real "
                    "efficiencies differ, and this is why they do."},
            {"text": "The shrew, because small animals grow faster than large "
                     "ones", "correct": False,
             "why": "The two have the same mass here, and a shrew's fast "
                    "living is a cost, not a saving."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s16",
        "band": "standard",
        "text": "A sea chain has five levels: phytoplankton, zooplankton, "
                "herring, seals, orcas. About what fraction of the "
                "phytoplankton's energy reaches the orcas?",
        "options": [
            {"text": "About a hundredth, since only two steps lose energy",
             "correct": False,
             "why": "Every step loses about nine tenths, not just two of "
                    "them. There are four steps in this chain."},
            {"text": "About a fiftieth, ten per cent lost five times",
             "correct": False,
             "why": "Ten per cent is what ARRIVES, and the arithmetic is "
                    "repeated multiplying rather than subtracting."},
            {"text": "About a ten-thousandth, four steps of a tenth",
             "correct": True},
            {"text": "About a thousandth, a tenth for each step",
             "correct": False,
             "why": "That is three steps' worth. Five levels have four steps "
                    "between them, not three."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s17",
        "band": "standard",
        "text": "A student says the fox level of a chain must hold more "
                "energy than the rabbit level, because a fox is a much bigger "
                "animal. What is wrong with that?",
        "options": [
            {"text": "Body size decides the level, so the argument has the "
                     "levels the wrong way round", "correct": False,
             "why": "Size decides neither the level nor the energy. What "
                    "decides the energy is how many steps up you are."},
            {"text": "Energy and size are really just the same thing measured "
                     "in two different units", "correct": False,
             "why": "They are not the same thing. A warm active animal holds "
                    "less energy for its size than a cool still one."},
            {"text": "The fox level holds more energy but far fewer animals, "
                     "so both claims are true", "correct": False,
             "why": "It holds fewer animals AND less energy. The two fall "
                    "together as you go up."},
            {"text": "The fox level holds about a tenth of the rabbit level's "
                     "energy", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s18",
        "band": "standard",
        "text": "A compost heap of grass cuttings and dead leaves becomes "
                "noticeably warm in the middle. Where is that warmth coming "
                "from?",
        "options": [
            {"text": "The decomposers in the heap respiring as they feed",
             "correct": True},
            {"text": "Sunlight trapped inside the heap by the cuttings piled "
                     "over it", "correct": False,
             "why": "The middle of a heap is the part sunlight cannot reach, "
                    "and it is the warmest part."},
            {"text": "Chemical energy released as the plant material dries "
                     "out", "correct": False,
             "why": "Drying takes energy in rather than giving it out. A "
                    "compost heap is damp, not dry."},
            {"text": "The dead plants still photosynthesising in the middle",
             "correct": False,
             "why": "Photosynthesis needs light and living cells, and it "
                    "stores energy rather than releasing warmth."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s19",
        "band": "standard",
        "text": "Two woods capture the same energy in their leaves. In one "
                "the leaves are eaten mainly by caterpillars, in the other "
                "mainly by deer. Which wood supports more top predators?",
        "options": [
            {"text": "The deer wood, because one deer holds far more energy in "
                     "it than a caterpillar does", "correct": False,
             "why": "One deer holds more than one caterpillar, and the wood "
                    "grows the same mass of leaf either way."},
            {"text": "The caterpillar wood, because a caterpillar passes on "
                     "more of what it eats than a deer", "correct": True},
            {"text": "Neither — the energy entering is the same, so the tops "
                     "must match", "correct": False,
             "why": "Equal energy in does not mean equal energy at the top. "
                    "How much survives each step matters too."},
            {"text": "The deer wood, because larger prey feeds larger "
                     "predators", "correct": False,
             "why": "Predator size is not the question. What reaches the top "
                    "level is the energy, not the size of the meal."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s20",
        "band": "standard",
        "text": "A student says the Sun is the producer of every food chain, "
                "because all the energy comes from it. Why is that wrong?",
        "options": [
            {"text": "The Sun is the producer only for plants, and not for "
                     "the animals above them", "correct": False,
             "why": "It would still be calling the Sun a producer, and the "
                    "energy reaches the animals through the plants anyway."},
            {"text": "Every chain has two producers, the Sun and the plant "
                     "that uses it", "correct": False,
             "why": "A chain has one producer level. The Sun is the source of "
                    "the energy, not a member of the chain."},
            {"text": "A producer is a living organism that builds its own "
                     "food, and the Sun is not alive", "correct": True},
            {"text": "The plants produce the sunlight", "correct": False,
             "why": "Plants capture sunlight; they do not make it. The Sun "
                    "produces the light and the plants produce the food."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s21",
        "band": "standard",
        "text": "Two chains start from plants holding 30,000 kJ. In one the "
                "top predator is at level three; in the other it is at level "
                "four. How much more energy reaches the first one?",
        "options": [
            {"text": "Twice as much, because one level has been added on",
             "correct": False,
             "why": "A level does not halve the energy — it divides it by "
                    "about ten."},
            {"text": "A hundred times as much — 3,000 kJ against 30 kJ each",
             "correct": False,
             "why": "3,000 kJ is level two's share. Level three gets a tenth "
                    "of that again."},
            {"text": "The same, because both chains start with the same "
                     "energy at the bottom", "correct": False,
             "why": "What they start with is equal; what arrives at the top "
                    "is not, because one chain has an extra step."},
            {"text": "Ten times as much — 300 kJ against 30 kJ",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s22",
        "band": "standard",
        "text": "A student says a food chain could begin with a fungus, "
                "because a fungus does not eat other living things. Why is "
                "that wrong?",
        "options": [
            {"text": "A fungus feeds only on material that other organisms "
                     "built", "correct": True},
            {"text": "A fungus only ever feeds on dead animals, never on "
                     "plants, so it cannot be first", "correct": False,
             "why": "Fungi feed on dead leaves and wood as readily as on dead "
                    "animals. That is not what stops them starting a chain."},
            {"text": "A fungus is a kind of plant, and plants are already the "
                     "start of every chain", "correct": False,
             "why": "Fungi are not plants and do not photosynthesise, which "
                    "is exactly why they cannot start a chain."},
            {"text": "Fungi are too small", "correct": False,
             "why": "Size is irrelevant. Microscopic algae start the largest "
                    "food chains on Earth."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s23",
        "band": "standard",
        "text": "A gardener digs compost into a vegetable bed and the "
                "vegetables grow better. Which part of a natural food web is "
                "she copying?",
        "options": [
            {"text": "The producers, because compost makes the plants "
                     "photosynthesise faster", "correct": False,
             "why": "Compost feeds the soil, not the leaves. The plants still "
                    "have to do the photosynthesis themselves."},
            {"text": "The decomposers, which return minerals to the soil",
             "correct": True},
            {"text": "The primary consumers, which eat plants and pass energy "
                     "on", "correct": False,
             "why": "A primary consumer removes plant material. Compost adds "
                    "to what the plants have to work with."},
            {"text": "The top predators, which keep the soil pests down",
             "correct": False,
             "why": "Compost is dead plant material, not a predator, and it "
                    "does not control anything."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s24",
        "band": "standard",
        "text": "A school pond is covered with a solid lid so that no light "
                "reaches the water. Predict what happens to the animals in it "
                "over the following months.",
        "options": [
            {"text": "They are unaffected, since they eat each other rather "
                     "than the light", "correct": False,
             "why": "Every one of them is living on energy the algae "
                    "captured. Cut that off and the whole web runs down."},
            {"text": "They grow faster, because the algae no longer compete "
                     "with them", "correct": False,
             "why": "Algae are the pond's food supply, not its competitors. "
                    "Losing them is a loss to everything above."},
            {"text": "Their numbers fall, as the algae stop capturing energy",
             "correct": True},
            {"text": "Only the plants die", "correct": False,
             "why": "The plants go first and the animals follow, because "
                    "every animal's food traces back to them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s25",
        "band": "standard",
        "text": "A food web is said to be the truthful picture of an "
                "ecosystem. Suggest why ecologists still draw single food "
                "chains.",
        "options": [
            {"text": "Because a chain shows energy and a web only shows who "
                     "lives there", "correct": False,
             "why": "Both are energy pictures. A web simply draws many "
                    "energy routes at once."},
            {"text": "Because a web can only be drawn for a small ecosystem",
             "correct": False,
             "why": "Webs are drawn for oceans. Size is not what limits "
                    "them."},
            {"text": "Because a chain is more accurate than a web",
             "correct": False,
             "why": "A chain is less complete, not more accurate — it leaves "
                    "out every route but one."},
            {"text": "Because one route is simple enough to follow and talk "
                     "about", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s26",
        "band": "standard",
        "text": "A conservation group wants to bring golden eagles back to a "
                "moor where they have not bred for fifty years. Which should "
                "they check first?",
        "options": [
            {"text": "Whether the moor holds enough prey to support them",
             "correct": True},
            {"text": "Whether the moor is warm enough for eagle chicks to "
                     "survive their first winter", "correct": False,
             "why": "Eagles already breed on cold moorland. What has to be "
                    "there is the energy, which means the prey."},
            {"text": "Whether the moor is large enough to be visible from the "
                     "air", "correct": False,
             "why": "Eagles find land easily enough. Area matters only "
                    "because of how much food it holds."},
            {"text": "Whether another bird of prey is already nesting there",
             "correct": False,
             "why": "Neighbours are not the first question. A moor with no "
                    "prey supports no eagles whoever else is on it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s27",
        "band": "standard",
        "text": "An ecologist measures the energy held at each level of a "
                "four-level chain and wants the ecosystem's total. Why can "
                "she not simply add the four figures together?",
        "options": [
            {"text": "Because the levels are measured in different units",
             "correct": False,
             "why": "They are all in kilojoules. The problem is not the unit, "
                    "it is where each figure came from."},
            {"text": "Because each level's energy came from the level below, "
                     "so adding counts it twice", "correct": True},
            {"text": "Because the decomposers have been left out of every one "
                     "of the four figures", "correct": False,
             "why": "Decomposers are a real gap in a levels-only count, and "
                    "they are not what makes adding the four wrong."},
            {"text": "Because energy cannot be added, only multiplied",
             "correct": False,
             "why": "Energies add perfectly well when they are separate "
                    "amounts. These are not separate."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s28",
        "band": "standard",
        "text": "A grassland is described as capturing 10,000 kJ per square "
                "metre per year. What does that figure describe?",
        "options": [
            {"text": "The energy the grazing animals take from each square "
                     "metre in a year", "correct": False,
             "why": "The grazers get about a tenth of it. This figure is "
                    "measured before anything eats."},
            {"text": "The energy every organism in a square metre holds at "
                     "any moment", "correct": False,
             "why": "That would be a standing total, not a yearly one. This "
                    "figure is a rate — energy captured per year."},
            {"text": "The energy the producers capture in a square metre in a "
                     "year", "correct": True},
            {"text": "The grass's mass", "correct": False,
             "why": "Mass is measured in kilograms. A kilojoule is a unit of "
                    "energy."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s29",
        "band": "standard",
        "text": "A student says the tenth rule means a fox has to eat roughly "
                "ten times its own mass of rabbit to build its body. Is that "
                "a fair way to put it?",
        "options": [
            {"text": "No — the rule applies only to plants and the animals "
                     "that eat them, and never to predators", "correct": False,
             "why": "It applies at every step of a chain, including the step "
                    "from rabbit to fox."},
            {"text": "No — the rule is about energy, and energy has nothing "
                     "to do with mass", "correct": False,
             "why": "Body mass is built out of the food's energy and "
                    "material, so the two track each other closely enough."},
            {"text": "No — it means a fox eats a tenth of its own mass, not "
                     "ten times it", "correct": False,
             "why": "That is the ratio upside down. The fox's level holds a "
                    "tenth of the rabbits', so far more rabbit is needed."},
            {"text": "Roughly, yes — about ten times the mass of prey goes "
                     "into a given mass of predator", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-s30",
        "band": "standard",
        "text": "A caterpillar eats 250 kJ of oak leaf over its life, and 25 "
                "kJ of that becomes caterpillar. What percentage of the leaf "
                "energy has it passed on?",
        "options": [
            {"text": "90%, which is the share that moves up a chain",
             "correct": False,
             "why": "90% is the share that does NOT move up. The two are "
                    "easily swapped and this is the swap."},
            {"text": "1%, a tenth of a tenth of the leaf", "correct": False,
             "why": "That is two steps' worth of loss. Only one step has "
                    "happened here."},
            {"text": "10%, a tenth of what it ate", "correct": True},
            {"text": "25%, one quarter of what it ate", "correct": False,
             "why": "25 kJ is the amount, not the percentage. Divide it by "
                    "the 250 kJ eaten first."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · harder ─────────────────────────────────────────
    {
        "id": "b9-01-h10",
        "band": "harder",
        "text": "A moor's plants capture 2,000 kJ per square metre a year, "
                "and any predator living there needs at least 2 kJ per square "
                "metre. If about a tenth passes on at each step, what is the "
                "highest level a predator could occupy on that moor?",
        "options": [
            {"text": "The fourth level, where 2 kJ arrives", "correct": True},
            {"text": "The fifth level, since a tenth of 2 kJ is still "
                     "something to live on", "correct": False,
             "why": "A tenth of 2 kJ is 0.2 kJ, which is below what the "
                    "question says a predator needs."},
            {"text": "The second level, the highest a moor supports",
             "correct": False,
             "why": "200 kJ arrives at level two, a hundred times more than "
                    "needed. The moor reaches higher than that."},
            {"text": "The third level, where 20 kJ arrives", "correct": False,
             "why": "20 kJ is ten times what a predator needs, so there is "
                    "room for one more level above it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h11",
        "band": "harder",
        "text": "A student weighs all the grass and all the rabbits in a "
                "field on one day and finds fifty times more grass than "
                "rabbit. Does that prove the tenth-of-the-energy rule?",
        "options": [
            {"text": "Yes — fifty times is close enough to ten times for the "
                     "rule to be counted proved", "correct": False,
             "why": "Close enough is not a measurement, and the two figures "
                    "are not measuring the same thing in the first place."},
            {"text": "No — a single day's masses are not the energy that "
                     "flowed through in a year", "correct": True},
            {"text": "No, because the rule is about numbers of organisms "
                     "rather than their mass", "correct": False,
             "why": "The rule is about energy, and mass is a reasonable stand-"
                    "in for it. The trouble is measuring on one day."},
            {"text": "Yes, and it proves it exactly", "correct": False,
             "why": "One field on one day proves nothing exactly. Grass is "
                    "regrown all season while the rabbits are counted once."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h12",
        "band": "harder",
        "text": "Two ecosystems capture the same energy in their producers. "
                "In the first about 5% passes on at each step; in the second "
                "about 20%. Which can support the longer chain?",
        "options": [
            {"text": "The first, because a slower transfer makes the energy "
                     "last through a greater number of levels", "correct": False,
             "why": "Slower transfer means less arriving, not energy eked "
                    "out. The energy runs out sooner, not later."},
            {"text": "Neither — chain length depends only on how much energy "
                     "enters at the bottom", "correct": False,
             "why": "What enters matters, and so does how much survives each "
                    "step. Two ecosystems here differ only in the second."},
            {"text": "The second, because more survives each step, so enough "
                     "is left further up", "correct": True},
            {"text": "Both the same, because the tenth rule fixes the number "
                     "of levels everywhere", "correct": False,
             "why": "A tenth is an average, not a law. Where transfers are "
                    "better than average, chains can run longer."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h13",
        "band": "harder",
        "text": "A cave ecosystem has no producers at all: everything in it "
                "lives on dead leaves and droppings washed in from the "
                "surface. Does that break the rule that energy enters a web "
                "through producers?",
        "options": [
            {"text": "Yes, the cave's bacteria are producers too", "correct": False,
             "why": "Bacteria feeding on dead leaves are decomposers. They "
                    "build nothing from sunlight."},
            {"text": "No, because dead material holds no energy",
             "correct": False,
             "why": "Dead material holds a great deal of energy — that is "
                    "exactly why a cave web can run on it."},
            {"text": "Yes — it shows some webs run without producers",
             "correct": False,
             "why": "The cave has no producers IN it. The energy still came "
                    "from producers, on the surface above."},
            {"text": "No — the dead material was built by producers outside "
                     "the cave", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h14",
        "band": "harder",
        "text": "A fishing fleet switches from catching tuna, which feed at "
                "the fourth level, to catching sardines, which feed at the "
                "second. Predict the effect on the mass it lands each year.",
        "options": [
            {"text": "It can land far more, because sardines feed two levels "
                     "lower down", "correct": True},
            {"text": "It lands about the same, as the sea holds a fixed mass "
                     "of fish", "correct": False,
             "why": "The sea holds far more mass at the lower levels. Which "
                    "level is fished decides how much there is."},
            {"text": "It lands less, because sardines are much smaller than "
                     "tuna", "correct": False,
             "why": "Size of one fish is not the limit. There is a hundred "
                    "times more energy two levels down."},
            {"text": "No change", "correct": False,
             "why": "Two levels is a factor of about a hundred in the energy "
                    "available, which is not nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h15",
        "band": "harder",
        "text": "A pyramid of numbers for an oak wood comes out upside down: "
                "one oak at the bottom supporting thousands of caterpillars "
                "above it. Does that contradict the tenth-of-the-energy rule?",
        "options": [
            {"text": "Yes — the rule says every level must hold fewer "
                     "organisms than the level below it", "correct": False,
             "why": "The rule is about energy, not headcount. It never "
                    "promised that numbers fall at every step."},
            {"text": "No — numbers are not energy, and one oak holds far more "
                     "than they do", "correct": True},
            {"text": "Yes, because a pyramid that does not narrow shows a "
                     "failure", "correct": False,
             "why": "A pyramid of ENERGY always narrows. A pyramid of numbers "
                    "need not, and this is why."},
            {"text": "No, because caterpillars do not count as a trophic "
                     "level", "correct": False,
             "why": "Caterpillars eat the producer, which makes them a real "
                    "level — the primary consumers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h16",
        "band": "harder",
        "text": "A small island has been studied for a century. Plants and "
                "plant-eating insects live there, and predatory insects have "
                "arrived several times but have never established. Suggest "
                "the best explanation.",
        "options": [
            {"text": "The plant-eating insects breed too fast for any "
                     "predator to keep up with them", "correct": False,
             "why": "Fast breeding is a food supply, not a defence. A "
                    "predator with plenty to eat does well."},
            {"text": "Plants on islands hold far less energy than the same "
                     "plants on the mainland", "correct": False,
             "why": "An island plant photosynthesises like any other. The "
                    "island's limit is its area, not its plants."},
            {"text": "The island is too small for enough energy to reach a "
                     "third level", "correct": True},
            {"text": "Predatory insects cannot reach an island",
             "correct": False,
             "why": "They have reached it several times, which is what the "
                    "century of study shows."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h17",
        "band": "harder",
        "text": "A rainforest and a moor each support a top predator at the "
                "fourth level, but the rainforest's plants capture far more "
                "energy per square metre. What does that predict about the "
                "areas the two predators hunt over?",
        "options": [
            {"text": "The rainforest predator needs the larger area, because "
                     "there is far more ground to search through",
             "correct": False,
             "why": "Rich ground means less searching, not more. The energy "
                    "is packed into a smaller area."},
            {"text": "Neither can be predicted from the energy, since hunting "
                     "area depends on the animal", "correct": False,
             "why": "Hunting area tracks how thinly the food is spread, and "
                    "that is exactly what the energy figure gives you."},
            {"text": "The moor predator needs the larger area, with less energy "
                     "reaching each square metre", "correct": True},
            {"text": "The two areas are the same, as both are at level four",
             "correct": False,
             "why": "The level is the same; the energy per square metre is "
                    "not, and that is what sets the area."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h18",
        "band": "harder",
        "text": "A farmer records that his clover field captures 25,000 kJ "
                "per square metre a year, and that his sheep, the only "
                "grazers, hold 2,000 kJ per square metre. Is that consistent "
                "with the tenth-of-the-energy rule?",
        "options": [
            {"text": "Yes — 8% is close to a tenth", "correct": True},
            {"text": "Yes, because the rule allows anything between nothing "
                     "and a fifth", "correct": False,
             "why": "The rule is an average near a tenth, not a licence for "
                    "any figure at all. Here it happens to be close."},
            {"text": "No, because 2,000 kJ is far more than a tenth of 25,000 "
                     "kJ", "correct": False,
             "why": "A tenth of 25,000 kJ is 2,500 kJ. The sheep hold less "
                    "than that, not more."},
            {"text": "No — one step should leave exactly 2,500 kJ, and it has "
                     "not", "correct": False,
             "why": "Nothing about the rule is exact. 2,000 kJ against 2,500 "
                    "kJ is agreement, not a contradiction."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h19",
        "band": "harder",
        "text": "An ecologist finds a chain in which the animal at the third "
                "level is much larger than the animal at the fourth. Does "
                "that break any rule about food chains?",
        "options": [
            {"text": "Yes — each level up must hold a larger animal than the "
                     "level below it, or the chain is drawn wrongly",
             "correct": False,
             "why": "Nothing says that. Blue whales feed at level two and "
                    "many top predators are small."},
            {"text": "No — what falls at each step is the energy, not the "
                     "body size", "correct": True},
            {"text": "Yes, because a predator always has to be bigger than "
                     "whatever it happens to eat", "correct": False,
             "why": "Plenty of predators take prey larger than themselves, "
                    "and many hunt in groups to do it."},
            {"text": "No, because the fourth level of a chain is not counted "
                     "as a real level", "correct": False,
             "why": "It is a real level. Four and five level chains are "
                    "perfectly ordinary."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h20",
        "band": "harder",
        "text": "A student writes that ninety per cent of the energy is lost "
                "at each level, and then calculates that 9,000 kJ of the "
                "grass's 10,000 kJ reaches the rabbits. Where is the error?",
        "options": [
            {"text": "The loss is ninety-nine per cent, so 100 kJ arrives",
             "correct": False,
             "why": "Ninety per cent is the right loss. What has gone wrong "
                    "is which figure was carried forward."},
            {"text": "There is no error — 9,000 kJ really is the amount that "
                     "reaches the rabbits", "correct": False,
             "why": "Ninety per cent lost and ninety per cent arriving cannot "
                    "both be true of the same step."},
            {"text": "The ninety per cent lost has been used as the amount "
                     "arriving, so it should be 1,000 kJ", "correct": True},
            {"text": "Grass does not hold 10,000 kJ", "correct": False,
             "why": "The starting figure is not the problem. The same error "
                    "would appear whatever number the grass held."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h21",
        "band": "harder",
        "text": "A grassland captures 8,000 kJ per square metre each year. "
                "About a tenth passes to its grazers and a tenth again to its "
                "predators. How much reaches the predators of one hectare, "
                "which is 10,000 square metres?",
        "options": [
            {"text": "80,000,000 kJ, the whole hectare's capture", "correct": False,
             "why": "That is what the plants capture across the hectare. The "
                    "predators are two steps above them."},
            {"text": "8,000,000 kJ, a tenth of the hectare's capture",
             "correct": False,
             "why": "That is one step's worth — the grazers' share. The "
                    "predators are one step above them again."},
            {"text": "800 kJ", "correct": False,
             "why": "That is the figure for one square metre, before "
                    "multiplying by the ten thousand in a hectare."},
            {"text": "800,000 kJ, or 80 kJ from each square metre",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h22",
        "band": "harder",
        "text": "A student says decomposers break the tenth-of-the-energy "
                "rule, because they take energy from every level of a web at "
                "once. Evaluate that.",
        "options": [
            {"text": "They do feed from every level, and what reaches them is "
                     "only what did not pass up", "correct": True},
            {"text": "They are right: decomposers are the one group the rule "
                     "was never meant to describe", "correct": False,
             "why": "The rule describes what passes UP a chain. Decomposers "
                    "take what did not, so nothing is double-counted."},
            {"text": "They are right, because decomposers get all the energy "
                     "in the end", "correct": False,
             "why": "Most of the energy is respired away at each level before "
                    "the decomposers ever see it."},
            {"text": "They are wrong, because decomposers take no energy from "
                     "a web", "correct": False,
             "why": "They take a great deal — every dropping and every dead "
                    "body from every level."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h23",
        "band": "harder",
        "text": "Two woods are compared. One gets far more sunlight and its "
                "oaks grow much faster, yet both woods hold the same number "
                "of sparrowhawks. Suggest the best explanation.",
        "options": [
            {"text": "The extra sunlight is used up by the caterpillars "
                     "before it can reach the birds", "correct": False,
             "why": "More caterpillars means more blue tits and more "
                    "sparrowhawk food. Nothing is used up on the way."},
            {"text": "Something other than food limits them, such as nest "
                     "sites", "correct": True},
            {"text": "Sparrowhawk numbers do not depend on energy, only on "
                     "the weather of the year", "correct": False,
             "why": "Food energy is normally what sets a top predator's "
                    "numbers. This wood is the exception, not the rule."},
            {"text": "The sunnier wood's oaks pass on a smaller share of what "
                     "they capture", "correct": False,
             "why": "Nothing makes a fast-growing oak less efficient. The "
                    "extra energy does reach the wood."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h24",
        "band": "harder",
        "text": "A textbook model starts every food chain with 10,000 kJ in "
                "the plants, whatever the ecosystem. What does that choice "
                "make clear, and what does it hide?",
        "options": [
            {"text": "It makes the ten per cent clear and hides that "
                     "transfers are the same in every ecosystem",
             "correct": False,
             "why": "Transfers are NOT the same everywhere — they run from a "
                    "few per cent to about twenty."},
            {"text": "It makes chain length clear and hides that energy is "
                     "never lost from the world", "correct": False,
             "why": "The model hides nothing about that. Energy is not "
                    "destroyed; it is released to the surroundings."},
            {"text": "It shows what chain length alone does, and hides that "
                     "real ecosystems differ", "correct": True},
            {"text": "It makes nothing clear, as the figure is invented",
             "correct": False,
             "why": "A chosen round figure is what lets two chains be "
                    "compared fairly. That is the whole point of it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h25",
        "band": "harder",
        "text": "A student says a food web containing more species must hold "
                "more energy than one containing fewer. Evaluate that.",
        "options": [
            {"text": "It is right, because each extra species adds its own "
                     "energy to the web", "correct": False,
             "why": "A new species brings no energy with it. It takes a share "
                    "of what the producers already captured."},
            {"text": "It is right, because more species means more routes to "
                     "carry energy", "correct": False,
             "why": "More routes divide the same energy differently. They do "
                    "not create any more of it."},
            {"text": "It cannot be judged", "correct": False,
             "why": "It can be judged, and the answer is clear: energy in is "
                    "set by the producers, not by the species list."},
            {"text": "It is wrong — the energy is only ever what the producers "
                     "capture", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h26",
        "band": "harder",
        "text": "An ecologist measuring how much energy a grassland captures "
                "works in kilojoules per square metre per year rather than "
                "per day. Why does the unit of time matter?",
        "options": [
            {"text": "Capture changes with the season, so a year covers a "
                     "whole cycle of growth", "correct": True},
            {"text": "A day is too short a time for any energy to be "
                     "captured", "correct": False,
             "why": "A grassland captures energy on every sunny day. The "
                    "trouble is that days differ from one another."},
            {"text": "Yearly figures are easier to add up than daily ones",
             "correct": False,
             "why": "Convenience is not the reason. A day in June and a day "
                    "in December would give opposite answers."},
            {"text": "Energy can only be measured over a year",
             "correct": False,
             "why": "Energy can be measured over any period. The year is "
                    "chosen because it is one full growing cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h27",
        "band": "harder",
        "text": "Orcas hunt across whole oceans. A student concludes that "
                "feeding at a high trophic level makes an animal a strong "
                "swimmer. What is wrong with that reasoning?",
        "options": [
            {"text": "Orcas are strong swimmers, and so is every other animal "
                     "living in the open ocean with them", "correct": False,
             "why": "Plenty of weak swimmers drift in the open ocean. And "
                    "the claim being tested is about the LEVEL, not the sea."},
            {"text": "The wide range follows from how little energy reaches "
                     "that level", "correct": True},
            {"text": "The level is set by what an animal eats, so it cannot "
                     "affect anything else about the animal",
             "correct": False,
             "why": "The level does affect the animal — through how far it "
                    "must travel to feed. The reasoning ran the wrong way."},
            {"text": "Nothing is wrong — feeding high up is what builds the "
                     "muscle for swimming", "correct": False,
             "why": "Muscle comes from food and use, not from a position in "
                    "a diagram."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h28",
        "band": "harder",
        "text": "A managed pond holds algae, water fleas and small fish. The "
                "owner adds a large predatory fish that eats the small fish. "
                "Predict the effect on the total mass of animal the pond can "
                "hold.",
        "options": [
            {"text": "It stays the same, because the algae still capture the "
                     "same energy", "correct": False,
             "why": "Energy in is unchanged; what changes is how many steps "
                    "it passes through before it stops."},
            {"text": "It rises, because a new species has been added to the "
                     "pond's web", "correct": False,
             "why": "Adding a species adds no energy. The new fish lives on "
                    "energy that was already there."},
            {"text": "It falls, because the energy now passes through one "
                     "more step", "correct": True},
            {"text": "It doubles", "correct": False,
             "why": "Each step up divides the energy by about ten, so a new "
                    "top level makes the total smaller, not larger."},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h29",
        "band": "harder",
        "text": "A brown bear eats berries, salmon and small mammals. "
                "Explain how feeding at more than one level affects the "
                "energy available to it.",
        "options": [
            {"text": "It has more available, because eating three different "
                     "foods means three times the energy", "correct": False,
             "why": "Three foods is not three times the energy. What matters "
                    "is how far up the chain each of them sits."},
            {"text": "It has less available, as the energy is split between "
                     "its routes", "correct": False,
             "why": "Nothing is split by using several routes. The bear takes "
                    "what it can get from each of them."},
            {"text": "It makes no difference, since the tenth applies to the "
                     "bear whatever it happens to eat", "correct": False,
             "why": "The tenth applies at each STEP, so the number of steps "
                    "below the bear is exactly what matters."},
            {"text": "It has more available, because the berries have passed "
                     "through fewer steps", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-01-h30",
        "band": "harder",
        "text": "A student says that because the tenth is only an average, an "
                "ecologist cannot use it for anything. Evaluate that.",
        "options": [
            {"text": "They are right — an average that varies is no use for "
                     "predicting", "correct": False,
             "why": "An average that varies still predicts a pattern. It is "
                    "single measurements it cannot promise."},
            {"text": "They are wrong, because the tenth is exact in every "
                     "ecosystem", "correct": False,
             "why": "It is not exact anywhere. Real transfers run from a few "
                    "per cent to about twenty."},
            {"text": "They are wrong — it still predicts why chains are short "
                     "and top predators rare", "correct": True},
            {"text": "They are right, because ecologists measure each "
                     "ecosystem separately anyway", "correct": False,
             "why": "They do measure, and the average is what tells them what "
                    "to expect before they start."},
        ],
        "figure": None,
    },
]
