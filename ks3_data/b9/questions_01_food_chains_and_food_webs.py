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
            {"text": "1,000 kJ, because a tenth of 10,000 kJ is 1,000 kJ.",
             "correct": False,
             "why": "That is what reaches the rabbits. The foxes are one step "
                    "further up, so take a tenth again: 100 kJ."},
            {"text": "9,000 kJ, because only a tenth of the energy is lost at "
                     "each step.", "correct": False,
             "why": "It is the other way round. About a tenth is passed ON, "
                    "and the other nine tenths leave the chain — mostly "
                    "warming the surroundings through respiration."},
            {"text": "100 kJ, because the energy takes two steps: grass to "
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
            {"text": "Seven steps at a tenth each leave about a "
                     "ten-millionth of what the plants captured — too little "
                     "to feed an animal.", "correct": True},
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
]
