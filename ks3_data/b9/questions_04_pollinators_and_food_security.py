"""B9 lesson 04 — Pollinators and food security: twelve questions (MRB-269).

These probe the gap the lesson is built on — that removing insect pollinators
takes a little from the calorie supply and most of the vitamins and minerals,
so the honest problem is deficiency rather than famine. The distractors are
built from the lesson's two declared misconceptions: ECO-07 (no bees, no food —
we would starve within a few years) and ECO-08 (save the bees, keep a hive of
honeybees). Four more come from the lesson's own careful wording — that many
crops set a reduced crop rather than none, that pollination is not a bee
monopoly, that hand pollination measures the loss rather than replacing it, and
that why the Sichuan orchards started doing it is disputed. Two more are the
confusions the shelf's own labels invite: potatoes grown from tubers read across
onto the cereals, and a food's share of the calorie column read as its share of
the vitamin column. The `harder` band takes the rule somewhere the lesson does
not go: a country that replaces calories and nothing else, a student who thinks
two organisms that do not eat each other are unconnected, and a town council
choosing between hives and habitat.
"""

UNIT = "B9"
LESSON = "pollinators-and-food-security"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-04-e01",
        "band": "easier",
        "text": "A hoverfly moves from flower to flower across a strawberry "
                "field, feeding as it goes. What makes it a pollinator?",
        "options": [
            {"text": "It makes honey out of the nectar it collects, which is "
                     "what pollinators are for.",
             "correct": False,
             "why": "Most pollinators make no honey at all — hoverflies, "
                    "moths, beetles and midges make none. A pollinator is an "
                    "animal that carries pollen between flowers while it "
                    "feeds."},
            {"text": "It carries pollen from one flower to another, so that "
                     "seed or fruit can form.",
             "correct": True},
            {"text": "It carries the plant’s seeds away to new ground where "
                     "they can grow.",
             "correct": False,
             "why": "That is seeds being spread, and it happens later. Pollen "
                    "has to move between flowers first, or there is no seed "
                    "to spread."},
            {"text": "It eats the small insects that would otherwise damage "
                     "the strawberry crop.",
             "correct": False,
             "why": "That would make it a predator of pests, which is a "
                    "different job. Pollination is the moving of pollen from "
                    "one flower to another."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e02",
        "band": "easier",
        "text": "Wheat, rice and maize set their grain without a single "
                "insect visiting them. So how does their pollen get from one "
                "plant to another?",
        "options": [
            {"text": "The wind carries it through the air — the cereals are "
                     "all wind-pollinated.",
             "correct": True},
            {"text": "They are grown from tubers, so no pollen has to move at "
                     "all.",
             "correct": False,
             "why": "Potatoes are the crop on the shelf grown from tubers. "
                    "Wheat, rice and maize are grasses, and their pollen is "
                    "carried by the wind."},
            {"text": "Farmers move the pollen between the plants by hand "
                     "every spring.",
             "correct": False,
             "why": "Hand pollination is done in a few places and it is "
                    "enormously expensive in labour. No cereal needs it — the "
                    "wind does the job for nothing."},
            {"text": "It does not move — cereals grow straight from the seed "
                     "the farmer sows.",
             "correct": False,
             "why": "The seed the farmer sows was itself made after "
                    "pollination. Pollen still has to move between flowers, "
                    "and in a cereal the wind moves it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e03",
        "band": "easier",
        "text": "The lesson pulls apart two groups of insects that are "
                "usually talked about as one. Which group is the one actually "
                "in decline?",
        "options": [
            {"text": "Managed honeybees, whose colony numbers have fallen "
                     "steadily over the last fifty years.",
             "correct": False,
             "why": "The opposite is true — there are more managed honeybee "
                    "colonies in the world now than fifty years ago. The "
                    "honeybee is a farmed animal, like a hen."},
            {"text": "All bees together, because every kind of bee lives and "
                     "works inside a hive.",
             "correct": False,
             "why": "Most bees are not hive insects at all. Britain has "
                    "around 250 solitary bee species, and several of them are "
                    "in serious decline."},
            {"text": "Wild pollinators — solitary bees, bumblebees, "
                     "hoverflies, moths and beetles.",
             "correct": True},
            {"text": "Only the honey-making insects, since the others never "
                     "visit flowers at all.",
             "correct": False,
             "why": "Hoverflies, moths, beetles and midges all visit flowers "
                    "and carry pollen — cocoa depends on midges. Making honey "
                    "has nothing to do with it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e04",
        "band": "easier",
        "text": "A country grows plenty of food and nobody there is short of "
                "calories, yet its scientists say it has a food security "
                "problem. What does food security mean?",
        "options": [
            {"text": "Whether a country grows enough calories to feed "
                     "everybody living in it.",
             "correct": False,
             "why": "Enough calories is only half of it. A population can "
                    "have all the energy it needs and still be badly short of "
                    "vitamins and minerals."},
            {"text": "Whether food is kept safe from theft and contamination "
                     "on its way to the shop.",
             "correct": False,
             "why": "The word is not about guarding food. It is about whether "
                    "a population can reliably get enough food, and food of "
                    "the right kind."},
            {"text": "Whether a country can grow all of its own food without "
                     "importing any.",
             "correct": False,
             "why": "Growing everything yourself is not what the term means. "
                    "Food security is about reliably getting enough food, and "
                    "food of the right kind."},
            {"text": "Whether a population can reliably get enough food, and "
                     "food of the right kind.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-04-s01",
        "band": "standard",
        "text": "On the shelf, chocolate (cocoa) carries 6 of the 100 calorie "
                "points and 15 of the 100 vitamin and mineral points, and it "
                "is entirely insect-pollinated. What does removing every "
                "pollinator do to the two bars?",
        "options": [
            {"text": "The calorie bar loses 6 points and the vitamin bar "
                     "loses 15.",
             "correct": True},
            {"text": "Both bars lose the same amount, because the whole cocoa "
                     "crop has gone.",
             "correct": False,
             "why": "The crop is one thing; its share of each bar is another. "
                    "Cocoa is a small part of the calories and a large part "
                    "of the vitamins, so it pulls the two bars down by "
                    "different amounts."},
            {"text": "The calorie bar loses 15 points and the vitamin bar "
                     "loses 6.",
             "correct": False,
             "why": "That reads the two columns the wrong way round. 6 is "
                    "cocoa’s share of the calories; 15 is its share of the "
                    "vitamins and minerals."},
            {"text": "Neither bar changes, because cocoa is pollinated by "
                     "midges rather than by bees.",
             "correct": False,
             "why": "Midges are pollinators too. Cocoa is entirely "
                    "insect-pollinated, so with no insects at all the crop "
                    "goes."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s02",
        "band": "standard",
        "text": "The shelf’s second button loses half the insect pollinators "
                "instead of all of them. What does it show happening to the "
                "food supply?",
        "options": [
            {"text": "No change at all, because the insects that are left "
                     "would visit every flower anyway.",
             "correct": False,
             "why": "Fewer insects means fewer visits and less pollen moved. "
                    "The crops come out reduced, not maintained."},
            {"text": "Only the cereals suffer, because they are grown in the "
                     "largest fields of all.",
             "correct": False,
             "why": "The cereals are wind-pollinated and are unaffected "
                    "whatever happens to the insects. It is the fruit, nuts "
                    "and vegetables that are hit."},
            {"text": "A partial loss — smaller crops, misshapen fruit and "
                     "higher prices in the shops.",
             "correct": True},
            {"text": "Exactly the same result as losing all of them, because "
                     "a half-pollinated crop still fails.",
             "correct": False,
             "why": "Crops differ in how completely they depend on insects, "
                    "and many set a reduced crop rather than none. Half is a "
                    "partial loss, not a total one."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s03",
        "band": "standard",
        "text": "Milk sits on the shelf with a dependence of 0.15, even "
                "though a dairy cow eats grass and silage rather than fruit. "
                "Why does milk depend on insects at all?",
        "options": [
            {"text": "Because bees pollinate the grass the cattle graze, as "
                     "they do every other plant.",
             "correct": False,
             "why": "Grasses are wind-pollinated — that is exactly why the "
                    "cereals survive. The insect-pollinated part is the rest "
                    "of the feed, not the grass."},
            {"text": "Because the cow herself needs insects in order to "
                     "produce milk at all.",
             "correct": False,
             "why": "Nothing in the cow’s own biology needs an insect. The "
                    "link runs through her feed, part of which is "
                    "insect-pollinated."},
            {"text": "It does not really — 0.15 is put there to make the loss "
                     "look worse than it is.",
             "correct": False,
             "why": "The number is deliberately small, because the route is "
                    "indirect. Milk at 0.15 and potatoes at 0 are what stop "
                    "the shelf overstating the loss."},
            {"text": "Because part of what the cattle are fed is itself "
                     "insect-pollinated.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s04",
        "band": "standard",
        "text": "A grower needs a crop pollinated in cold early-spring "
                "weather, when honeybees stay inside the hive. Which "
                "pollinators is she most likely to be relying on?",
        "options": [
            {"text": "Moths, which do their pollinating at night when it is "
                     "coldest of all.",
             "correct": False,
             "why": "Moths are the night-shift pollinators, and that is about "
                    "the time of day rather than the temperature. Hoverflies "
                    "are the ones that work in the cold."},
            {"text": "Hoverflies, which work in colder weather than bees will "
                     "come out in.",
             "correct": True},
            {"text": "Nobody — honeybees are the only insects that pollinate "
                     "a crop properly.",
             "correct": False,
             "why": "Pollination is not a bee monopoly. Hoverflies, moths, "
                    "beetles and midges all carry pollen between flowers, and "
                    "several do it better than honeybees."},
            {"text": "Midges, which are the pollinators that the cocoa crop "
                     "depends on.",
             "correct": False,
             "why": "Midges do pollinate, but cocoa grows in the warm "
                    "tropics. In a cold British spring it is the hoverflies "
                    "that are flying."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-04-h01",
        "band": "harder",
        "text": "In parts of Sichuan, growers have hand-pollinated their "
                "apple and pear orchards for decades — a person takes a day "
                "to do what a few hundred bees would do in an afternoon. What "
                "does that establish?",
        "options": [
            {"text": "That hand pollination is a working substitute, so "
                     "losing pollinators need not worry anybody.",
             "correct": False,
             "why": "It works, and that is the trap in it. Hand pollination "
                    "is a measure of the loss rather than a solution to it — "
                    "the cost is counted in working days per hectare."},
            {"text": "That pesticide use was what killed off the pollinators "
                     "in that region.",
             "correct": False,
             "why": "Why it started is disputed — pesticide use, habitat loss "
                    "and plentiful cheap labour all appear in different "
                    "accounts. It is not a parable with one cause."},
            {"text": "That fruit pollinated by hand comes out poorer than "
                     "fruit pollinated by insects.",
             "correct": False,
             "why": "The fruit sets perfectly well. What the example "
                    "establishes is the cost of doing the job by hand, not a "
                    "failure to do it."},
            {"text": "That insect pollination is a free service with a real "
                     "price once it has to be replaced.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h02",
        "band": "harder",
        "text": "After a bad harvest a country makes up every lost calorie by "
                "importing extra wheat and rice, so nobody goes hungry. "
                "Doctors there still report more illness than usual. What is "
                "the most likely explanation?",
        "options": [
            {"text": "The imported cereals must have spoiled somewhere on the "
                     "journey to the country.",
             "correct": False,
             "why": "Nothing here is about food going bad. Look instead at "
                    "which nutrients cereals supply and which ones they do "
                    "not."},
            {"text": "The calories were replaced, but the vitamins and "
                     "minerals in them were not.",
             "correct": True},
            {"text": "Nobody is going hungry, so the illness cannot have "
                     "anything to do with the diet.",
             "correct": False,
             "why": "Having enough to eat and having a balanced diet are two "
                    "different things, and that distinction is the whole of "
                    "food security."},
            {"text": "Imported wheat and rice carry fewer calories than the "
                     "same crops grown at home.",
             "correct": False,
             "why": "The calories were matched — the question says so. What "
                    "was not matched is the vitamin and mineral side of the "
                    "diet."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h03",
        "band": "harder",
        "text": "A student argues that insects and crop plants have little to "
                "do with each other, because neither one is food for the "
                "other. Where does that argument fail?",
        "options": [
            {"text": "Pollination is a service the insects provide, and "
                     "the crop depends on it.",
             "correct": True},
            {"text": "It does not fail — a plant with no pollinator at all "
                     "still grows perfectly well.",
             "correct": False,
             "why": "The plant grows, and that is not the issue. Without "
                    "pollination it sets little or no fruit or seed, however "
                    "healthy it looks."},
            {"text": "It fails because bees do feed the plant, carrying "
                     "nectar to it as they visit.",
             "correct": False,
             "why": "Nectar travels the other way — the insect takes it from "
                    "the flower. What the insect carries between flowers is "
                    "pollen."},
            {"text": "It fails because insects eat the pests that would "
                     "otherwise destroy the crop.",
             "correct": False,
             "why": "That is a different relationship altogether. The service "
                    "this lesson is about is the moving of pollen from one "
                    "flower to another."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h04",
        "band": "harder",
        "text": "A town council has money for one pollinator project: twenty "
                "honeybee hives in the park, or wildflower margins and rough "
                "ground along every verge, mown late. Which should it choose?",
        "options": [
            {"text": "The hives, because more bees in the town must mean more "
                     "pollination for everybody.",
             "correct": False,
             "why": "Honeybees are a farmed animal, and a dense hive in a "
                    "poor landscape competes with the wild insects for the "
                    "few flowers there are."},
            {"text": "The hives, because honeybees are the pollinators in "
                     "decline and need topping up.",
             "correct": False,
             "why": "Managed colonies have risen — there are more now than "
                    "fifty years ago. The insects in decline are the wild "
                    "ones, and a hive does not help them."},
            {"text": "The margins, because wild pollinators need flowers all "
                     "season and rough ground to nest in.",
             "correct": True},
            {"text": "Neither, because pollinator numbers are set by the "
                     "weather and nothing on the ground helps.",
             "correct": False,
             "why": "What wild pollinators need is known and can be given to "
                    "them: flowers through the whole season, undisturbed "
                    "ground and hedges, and fewer insecticides."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-04-e05",
        "band": "easier",
        "text": "What does pollination mean?",
        "options": [
            {"text": "An insect feeding on the nectar inside a flower.",
             "correct": False,
             "why": "That is what the insect came for. Pollination is the "
                    "pollen it carries from one flower to another while it "
                    "feeds."},
            {"text": "A plant producing seeds inside its fruit.",
             "correct": False,
             "why": "Seed forms after pollination has happened. Pollination "
                    "is the moving of the pollen that makes the seed "
                    "possible."},
            {"text": "A flower opening so that insects can reach the inside "
                     "of it.", "correct": False,
             "why": "Opening is how a flower makes itself available. "
                    "Pollination is the transfer of pollen between flowers."},
            {"text": "Moving pollen from one flower to another so that seed "
                     "or fruit can form.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e06",
        "band": "easier",
        "text": "Bees are not the only pollinators. Which of these also carry "
                "pollen between flowers?",
        "options": [
            {"text": "Hoverflies, moths, beetles and midges.", "correct": True},
            {"text": "Earthworms, woodlice and slugs.", "correct": False,
             "why": "Those feed on dead material and leaves at ground level. "
                    "A pollinator is an animal that visits flowers and "
                    "carries pollen between them."},
            {"text": "Only honeybees and bumblebees, since no other insect "
                     "visits flowers.", "correct": False,
             "why": "Cocoa is pollinated by midges and moths do the job at "
                    "night. Pollination is not a bee monopoly."},
            {"text": "Ladybirds and lacewings, which live on the same "
                     "plants.", "correct": False,
             "why": "They live on the plants and hunt aphids rather than "
                    "visiting flowers. Feeding at a flower is what puts "
                    "pollen on an insect."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e07",
        "band": "easier",
        "text": "Apart from flowers to feed at, what else does a wild bee need "
                "on farmland?",
        "options": [
            {"text": "A hive, built and looked after by a beekeeper.",
             "correct": False,
             "why": "That is what a honeybee has. Most of Britain's bees are "
                    "solitary and nest on their own, in rough ground or in a "
                    "hedge bank."},
            {"text": "Open ploughed ground, which is the easiest surface to "
                     "nest in.", "correct": False,
             "why": "Ploughed ground is turned over every year, so a nest in "
                    "it does not survive. What they need is ground left "
                    "undisturbed."},
            {"text": "Somewhere to nest — rough ground, a bank or a hedge "
                     "left undisturbed.", "correct": True},
            {"text": "A supply of water, which is the main thing missing from "
                     "farmland.", "correct": False,
             "why": "Water is rarely the limit on farmland. What is usually "
                    "missing is nesting places, and flowers outside the "
                    "crop's few weeks of bloom."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e08",
        "band": "easier",
        "text": "Potatoes are grown by planting pieces of last year's tubers "
                "rather than from seed. Why does that mean the crop needs no "
                "insect?",
        "options": [
            {"text": "Because potato flowers are pollinated by the wind "
                     "instead.", "correct": False,
             "why": "Wind pollination is how the cereals manage. The potato "
                    "crop does not need pollinating at all, because it is not "
                    "grown from seed."},
            {"text": "Because no seed has to be set, so no pollen needs "
                     "moving.", "correct": True},
            {"text": "Because potatoes grow underground, where insects cannot "
                     "reach them.", "correct": False,
             "why": "Where the crop grows is not the point, and the flowers "
                    "are above ground anyway. The point is that the part we "
                    "eat is not a seed or a fruit."},
            {"text": "Because potato plants pollinate their own flowers "
                     "without help.", "correct": False,
             "why": "Some plants do pollinate themselves, and the potato crop "
                    "does not depend on it either way. The tubers are "
                    "planted, so no seed is needed."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e09",
        "band": "easier",
        "text": "A strawberry plant is healthy and well watered, but no "
                "insect visits its flowers. What happens to the crop?",
        "options": [
            {"text": "Little or no fruit forms, and what does form comes out "
                     "small and misshapen.", "correct": True},
            {"text": "The fruit forms as usual, because the plant has "
                     "everything else it needs.", "correct": False,
             "why": "Everything else is not enough. A strawberry cannot set a "
                    "full fruit unless pollen has been moved between its "
                    "flowers."},
            {"text": "The plant produces more fruit, because it puts nothing "
                     "into making nectar.", "correct": False,
             "why": "Nectar is what the plant spends to attract the insect. "
                    "Saving it does not buy fruit — the visit is what the "
                    "fruit depends on."},
            {"text": "The fruit forms normally but has no seeds in it.",
             "correct": False,
             "why": "The seeds and the fruit go together in a strawberry — "
                    "the pips on the outside are the seeds, and the fruit "
                    "swells around them."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-04-s05",
        "band": "standard",
        "text": "An apple grower brings hives into the orchard for three "
                "weeks each spring and takes them away again. Why only three "
                "weeks?",
        "options": [
            {"text": "Because the bees would run out of food if they stayed "
                     "in the orchard any longer.", "correct": False,
             "why": "They might, and that is the beekeeper's problem rather "
                    "than the crop's. The hives are there for as long as the "
                    "blossom is."},
            {"text": "Because the apples need pollinating again just before "
                     "they are picked.", "correct": False,
             "why": "Pollination happens once, at blossom time. After that "
                    "the fruit is simply growing and no insect is needed."},
            {"text": "Because pollen can only be moved while the blossom is "
                     "open, and after that the fruit is set.", "correct": True},
            {"text": "Because three weeks is as long as a hive can be moved "
                     "for without harming it.", "correct": False,
             "why": "Hives are moved for whole seasons in some countries. The "
                    "three weeks are set by the blossom, not by the bees."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s06",
        "band": "standard",
        "text": "Californian almond growers hire more than a million hives "
                "every spring, brought in by lorry from across the country. "
                "What does that tell you about the crop and the place it is "
                "grown?",
        "options": [
            {"text": "That almonds set a better crop when several different "
                     "hives are used.", "correct": False,
             "why": "The hives are hired in numbers because the orchards are "
                    "enormous, not for variety. One hive can only work so "
                    "many trees."},
            {"text": "That honeybees are the only insect able to pollinate an "
                     "almond flower.", "correct": False,
             "why": "Other insects can and do pollinate almonds. What is "
                    "missing locally is enough of them, not the right kind."},
            {"text": "That the crop would set anyway, and the hives only "
                     "raise the yield a little.", "correct": False,
             "why": "Almonds are entirely dependent on insect pollination — "
                    "no visit, no crop. That is why the hives are worth the "
                    "cost of trucking them in."},
            {"text": "That the crop depends completely on insects, and too "
                     "few wild ones live nearby.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s07",
        "band": "standard",
        "text": "A shop wants to stock only foods that would still be "
                "produced if every insect pollinator disappeared. Which set "
                "could it stock?",
        "options": [
            {"text": "Apples, almonds, coffee and chocolate.", "correct": False,
             "why": "Every one of those depends on insects, and almonds and "
                    "cocoa entirely. That is the basket that empties first."},
            {"text": "Bread, rice, sweetcorn and potatoes.", "correct": True},
            {"text": "Strawberries, tomatoes, broccoli and milk.",
             "correct": False,
             "why": "The first three are all insect-pollinated. Milk is only "
                    "slightly affected, through the cattle's feed, so it is "
                    "the odd one out in the wrong direction."},
            {"text": "Bread, rice, apples and broccoli.", "correct": False,
             "why": "Bread and rice would survive, being wind-pollinated. "
                    "Apples and broccoli both need insects, so the shop "
                    "would be stocking two foods out of four."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s08",
        "band": "standard",
        "text": "A farmer finds his oilseed rape yields fall the further a "
                "field is from the nearest hedgerow, although the soil and "
                "the seed are the same throughout. What is the best "
                "explanation?",
        "options": [
            {"text": "The pollinators nest in the hedges and travel only so "
                     "far, so distant parts are visited less.",
             "correct": True},
            {"text": "Hedges shelter the crop from wind, and rape is "
                     "wind-pollinated.", "correct": False,
             "why": "Oilseed rape is insect-pollinated, which is exactly why "
                    "the distance matters. The hedge is supplying insects, "
                    "not shelter for pollen."},
            {"text": "Hedges add minerals to the soil beside them, so the "
                     "crop grows better there.", "correct": False,
             "why": "That would affect a strip a metre or two wide, not a "
                    "gradient across a whole field. Insects travel much "
                    "further than minerals do."},
            {"text": "Fields further from a hedge are larger, and large "
                     "fields always yield less per hectare.", "correct": False,
             "why": "Size on its own does not lower a yield. What falls away "
                    "with distance is the number of pollinators reaching the "
                    "crop."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s09",
        "band": "standard",
        "text": "Coffee is about half dependent on insect pollination. What "
                "would losing every pollinator mean for a coffee crop?",
        "options": [
            {"text": "The crop would fail completely, since half dependent "
                     "still means it needs insects.", "correct": False,
             "why": "Half means half. A partly dependent crop sets a reduced "
                    "yield without insects rather than none at all."},
            {"text": "Nothing would change, because the plant manages the "
                     "other half on its own.", "correct": False,
             "why": "It manages half on its own, so half the crop is what is "
                    "at risk. That is a very large loss to a grower."},
            {"text": "A crop would still be set, but a much smaller one.",
             "correct": True},
            {"text": "The crop would be the same size but poorer in quality.",
             "correct": False,
             "why": "Size is what falls when pollination is short. Quality "
                    "suffers in some crops as well, and here the main loss is "
                    "yield."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-04-h05",
        "band": "harder",
        "text": "A farmer sows a strip of wildflowers along the edge of a "
                "field of insect-pollinated beans, taking that strip out of "
                "production. The field then yields more beans in total than "
                "an identical field with no strip. How?",
        "options": [
            {"text": "The wildflowers put minerals into the soil, which the "
                     "beans then use.", "correct": False,
             "why": "One strip along an edge cannot fertilise a whole field. "
                    "What it supplies is insects, and insects travel."},
            {"text": "The strip shelters the crop from wind, so fewer plants "
                     "are damaged.", "correct": False,
             "why": "A single strip gives little shelter, and this crop's "
                    "yield is limited by pollination. The insects are what "
                    "the strip provides."},
            {"text": "The wildflowers draw pests away from the beans, so less "
                     "of the crop is lost.", "correct": False,
             "why": "Some plantings do work that way, and it is not what is "
                    "happening here. The gain is in how well the beans were "
                    "pollinated."},
            {"text": "The strip feeds pollinators, and better pollinated "
                     "beans repay the lost ground.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h06",
        "band": "harder",
        "text": "Cocoa is pollinated by tiny midges whose young develop in "
                "damp rotting leaf litter on the forest floor. Plantations "
                "that clear their litter and undergrowth to keep the ground "
                "tidy get poorer yields. Explain.",
        "options": [
            {"text": "The litter holds the water the cocoa trees need, so "
                     "clearing it dries the trees out.", "correct": False,
             "why": "Litter does hold moisture, and the trees here are "
                    "healthy while the pods are not being set. What was "
                    "cleared away was the midges' breeding ground."},
            {"text": "The midges have lost the places they breed in, so far "
                     "fewer are there to pollinate the flowers.",
             "correct": True},
            {"text": "Clearing the ground damages the roots of the cocoa "
                     "trees, so they set fewer pods.", "correct": False,
             "why": "Root damage would show as sick trees. These trees flower "
                    "as usual; what fails is the transfer of pollen between "
                    "the flowers."},
            {"text": "Tidy ground reflects more sunlight, so the flowers open "
                     "at the wrong time of day.", "correct": False,
             "why": "Nothing about the flowering has changed. What has gone "
                    "is the insect that carried pollen from one flower to "
                    "another."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h07",
        "band": "harder",
        "text": "A grower is told to spray insecticide at dusk rather than at "
                "midday while the crop is in flower. Why does the timing "
                "help, and which pollinators does it not protect?",
        "options": [
            {"text": "It helps because insecticide works less well in the "
                     "cool of the evening, and it protects every pollinator "
                     "equally.", "correct": False,
             "why": "The aim is not a weaker spray — a weaker spray would not "
                    "control the pest. The aim is to spray when the "
                    "pollinators are not on the crop."},
            {"text": "It helps because bees return to the hive at night, and "
                     "the moths are asleep by dusk as well.", "correct": False,
             "why": "Moths are not asleep at dusk; dusk is when they start. "
                    "They pollinate at night, and an evening spray reaches "
                    "them."},
            {"text": "It helps because bees and hoverflies stop visiting "
                     "flowers at dusk, but moths pollinate at night and are "
                     "still reached.", "correct": True},
            {"text": "It does not help at all, because the spray stays on the "
                     "crop and the insects meet it next morning.",
             "correct": False,
             "why": "Residue is a real problem and it is much reduced by the "
                    "time the bees are out. Spraying onto working insects is "
                    "worse than spraying onto an empty crop."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h08",
        "band": "harder",
        "text": "A trial nets half a field of strawberries so no insect can "
                "reach the flowers. The netted half still fruits, but the "
                "berries are small and misshapen and the crop weighs about "
                "40% of the open half. What does that show about the word "
                "dependence?",
        "options": [
            {"text": "That dependence is not all-or-nothing — some fruit "
                     "sets without insects, and most of the value is lost.",
             "correct": True},
            {"text": "That strawberries do not really depend on insects, "
                     "since fruit formed under the net.", "correct": False,
             "why": "Fruit formed and most of the crop did not. Losing three "
                    "fifths of a harvest is a dependence by any farmer's "
                    "reckoning."},
            {"text": "That the netting itself damaged the plants, since "
                     "healthy plants would have set a full crop.",
             "correct": False,
             "why": "The plants were healthy and the flowers opened. What "
                    "they did not get was pollen moved between them."},
            {"text": "That strawberries depend on insects completely, since "
                     "the fruit came out misshapen.", "correct": False,
             "why": "Completely dependent would mean no fruit at all, as with "
                    "almonds. Strawberries sit between the two, which is what "
                    "the 40% is telling you."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h09",
        "band": "harder",
        "text": "A newspaper reports that Britain has more managed honeybee "
                "colonies than fifty years ago, and concludes that worries "
                "about pollinators are unfounded. Which reply is best?",
        "options": [
            {"text": "The report is right — honeybees do most of the "
                     "pollinating, so their numbers settle the question.",
             "correct": False,
             "why": "A great deal of pollination is done by wild bees, "
                    "hoverflies, moths and beetles, and several of those do "
                    "it better than a honeybee does."},
            {"text": "The report is wrong, because managed colony numbers "
                     "have in fact been falling steadily.", "correct": False,
             "why": "Managed colonies are doing reasonably well, which is why "
                    "the figure can be quoted. The trouble is that it "
                    "describes the wrong group."},
            {"text": "The report is right about the figure, and pollination "
                     "cannot really be measured anyway.", "correct": False,
             "why": "It can be measured — crop yields with and without "
                    "insects, and long-run counts of wild species. The "
                    "evidence exists, and it is about wild pollinators."},
            {"text": "Managed honeybees are livestock and are doing well; the "
                     "pollinators in decline are the wild ones.",
             "correct": True},
        ],
        "figure": None,
    },
]
