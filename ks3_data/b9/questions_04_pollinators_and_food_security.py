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

    # ── MRB-338 night 3 expansion ───────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-04-e10",
        "band": "easier",
        "text": "What does it mean to say that a crop is wind-pollinated?",
        "options": [
            {"text": "Its seeds are blown away from the parent plant onto new "
                     "ground.", "correct": False,
             "why": "That is seed dispersal, and it comes later. Pollination "
                    "has to happen first or there is no seed to blow "
                    "anywhere."},
            {"text": "It sets a crop only in a year when there is enough wind "
                     "at flowering time to shake the plants.",
             "correct": False,
             "why": "The wind is doing a job rather than setting a condition. "
                    "Enough pollen moves in ordinary weather for a cereal to "
                    "set its grain."},
            {"text": "Its pollen is carried between flowers by moving air "
                     "rather than by an animal.", "correct": True},
            {"text": "It is pollinated by insects that the wind blows into the "
                     "crop from nearby fields.", "correct": False,
             "why": "That would still leave the crop depending on insects. A "
                    "wind-pollinated plant needs no animal at all."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e11",
        "band": "easier",
        "text": "Most of the energy in the world's diet comes from a small "
                "group of crops. Which group?",
        "options": [
            {"text": "The cereals, such as wheat, rice, maize, barley and "
                     "oats.", "correct": True},
            {"text": "The fruit and nuts, such as apples, strawberries and "
                     "almonds.", "correct": False,
             "why": "Those carry a great deal of the vitamins and minerals in "
                    "a diet, and very little of its energy."},
            {"text": "The green vegetables, such as broccoli, cabbage and "
                     "beans.", "correct": False,
             "why": "Green vegetables are a small part of the energy anyone "
                    "eats. What they supply is the vitamins and the "
                    "minerals."},
            {"text": "The crops that need an insect visit before they will set "
                     "seed.", "correct": False,
             "why": "Those crops matter enormously and they are not where the "
                    "energy comes from. The staples are all pollinated by the "
                    "wind."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e12",
        "band": "easier",
        "text": "Insect-pollinated crops are only a small slice of what people "
                "eat by weight. What are they a large share of?",
        "options": [
            {"text": "The salt and the sugar, which are what make a meal taste "
                     "of anything.", "correct": False,
             "why": "Neither comes from an insect-pollinated crop, and neither "
                    "is a nutrient a diet is short of."},
            {"text": "The vitamins, the minerals and most of the variety in a "
                     "diet.", "correct": True},
            {"text": "The starch, which is the main fuel a body runs on.",
             "correct": False,
             "why": "Starch comes mostly from the cereals and from potatoes, "
                    "and none of those depends on an insect."},
            {"text": "The water, since fruit and vegetables are mostly water.",
             "correct": False,
             "why": "They are, and nobody is short of water in a diet. What "
                    "they are valued for is the vitamins and minerals."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e13",
        "band": "easier",
        "text": "Almonds and cocoa set nothing at all if no insect visits "
                "them. Which phrase describes a crop like that?",
        "options": [
            {"text": "Wind-pollinated.", "correct": False,
             "why": "A wind-pollinated crop needs no animal at all, so losing "
                    "the insects would leave it untouched."},
            {"text": "Partly insect-pollinated.", "correct": False,
             "why": "A partly dependent crop sets a reduced crop without "
                    "insects. These two set none."},
            {"text": "Grown from tubers.", "correct": False,
             "why": "A crop grown from tubers sets no seed at all, so "
                    "pollination never arises. Almonds and cocoa are both "
                    "grown from pollinated flowers."},
            {"text": "Entirely dependent on insect pollination.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e14",
        "band": "easier",
        "text": "Cocoa flowers are pollinated by one particular kind of very "
                "small fly. Which?",
        "options": [
            {"text": "Midges.", "correct": True},
            {"text": "Mosquitoes.", "correct": False,
             "why": "Mosquitoes feed on plant sugars and blood rather than "
                    "working flowers. Cocoa depends on tiny midges."},
            {"text": "Houseflies.", "correct": False,
             "why": "Houseflies feed on spilt and rotting food. The cocoa "
                    "flower is worked by midges."},
            {"text": "Greenflies.", "correct": False,
             "why": "Greenfly feed by sucking sap out of a plant, which is the "
                    "opposite of a service. Cocoa is pollinated by midges."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e15",
        "band": "easier",
        "text": "Moths visit flowers and carry pollen between them, as bees "
                "do. When do they do their work?",
        "options": [
            {"text": "In the middle of the day, working alongside the bees.",
             "correct": False,
             "why": "That is when the bees and hoverflies are out. Moths fly "
                    "once the light has gone."},
            {"text": "In cold early spring weather, before any bee will come "
                     "out of the hive to feed.", "correct": False,
             "why": "Hoverflies are the ones that work in the cold. Moths are "
                    "the night shift, whatever the season."},
            {"text": "Only during the few weeks that a crop is in blossom.",
             "correct": False,
             "why": "Every pollinator works while a crop is in flower. What "
                    "marks the moths out is the time of day."},
            {"text": "At night, when almost every other pollinator has stopped "
                     "flying.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e16",
        "band": "easier",
        "text": "What is a managed honeybee colony?",
        "options": [
            {"text": "A hive of bees kept and looked after by a beekeeper.",
             "correct": True},
            {"text": "A wild nest of bees that a farmer has decided to leave "
                     "alone.", "correct": False,
             "why": "Leaving something alone is not managing it. A managed "
                    "colony lives in a hive somebody owns."},
            {"text": "A group of solitary bees that have nested together in "
                     "one bank.", "correct": False,
             "why": "Solitary bees sometimes nest close together and each "
                    "female still works alone. Nobody keeps them."},
            {"text": "Any colony of insects that has been brought in to "
                     "pollinate a crop.", "correct": False,
             "why": "The word names the honeybee in particular, because the "
                    "honeybee is the pollinator people farm."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e17",
        "band": "easier",
        "text": "Roughly how many species of solitary bee live in Britain?",
        "options": [
            {"text": "About 5.", "correct": False,
             "why": "That is nearer the number of bumblebee species anyone "
                    "sees in a garden. The solitary bees are far more "
                    "numerous."},
            {"text": "About 25.", "correct": False,
             "why": "Ten times too few. Britain has around 250 species of "
                    "solitary bee, which is why losing some of them is easy "
                    "to miss."},
            {"text": "About 250.", "correct": True},
            {"text": "About 25,000.", "correct": False,
             "why": "That is closer to the number of bee species known in the "
                    "whole world. Britain holds about 250 solitary ones."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e18",
        "band": "easier",
        "text": "Fruit, nuts and vegetables are the main source of several "
                "things the body needs. Which list is right?",
        "options": [
            {"text": "Starch, fat, and most of the energy in a day's meals.",
             "correct": False,
             "why": "Energy comes mostly from the cereals and from potatoes, "
                    "and none of those needs an insect."},
            {"text": "Vitamin C, vitamin A, folate, iron and calcium.",
             "correct": True},
            {"text": "Protein, and nothing else that a diet would miss.",
             "correct": False,
             "why": "Most protein comes from meat, fish, eggs, dairy and "
                    "pulses. Fruit and vegetables are valued for their "
                    "vitamins and minerals."},
            {"text": "Water and fibre, but no vitamins or minerals at all.",
             "correct": False,
             "why": "They do supply water and fibre, and the vitamins and "
                    "minerals are the reason a diet without them makes people "
                    "ill."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e19",
        "band": "easier",
        "text": "A population eats plenty of bread and rice and almost no "
                "fruit or vegetables. What kind of illness would you expect?",
        "options": [
            {"text": "Starvation, because bread and rice carry almost none of "
                     "the energy a body needs each day.", "correct": False,
             "why": "Cereals are where most of the world's energy comes from. "
                    "Nobody eating plenty of bread and rice is starving."},
            {"text": "No illness at all, since a population getting enough to "
                     "eat is a healthy one.", "correct": False,
             "why": "Enough to eat and enough of the right things are two "
                    "different questions, and that gap is the whole of food "
                    "security."},
            {"text": "Deficiency diseases, from the vitamins and minerals the "
                     "diet is missing.", "correct": True},
            {"text": "Food poisoning, because cereals go bad more easily than "
                     "fruit.", "correct": False,
             "why": "Dry grain keeps for years — better than fruit does. The "
                    "problem here is what the diet lacks."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e20",
        "band": "easier",
        "text": "Pollen has arrived on the flower it needed to reach. What "
                "forms next?",
        "options": [
            {"text": "More pollen, which the plant sends on to the next "
                     "flower.", "correct": False,
             "why": "A plant makes pollen before any of this, and the pollen "
                    "does not travel on. What follows a successful visit is "
                    "seed."},
            {"text": "Nectar, which the flower makes to reward the insect that "
                     "came.", "correct": False,
             "why": "Nectar is there before the insect arrives — it is the "
                    "advertisement, not the result."},
            {"text": "A fresh flower, opening from the same bud a few days "
                     "later.", "correct": False,
             "why": "A flower that has been pollinated is finished; it does "
                    "not open again. What grows from it is seed."},
            {"text": "Seed, and in many plants a fruit that swells around it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e21",
        "band": "easier",
        "text": "Why does a flower produce nectar?",
        "options": [
            {"text": "To attract animals, which then carry its pollen to other "
                     "flowers.", "correct": True},
            {"text": "To feed the seeds while they are growing inside the "
                     "fruit.", "correct": False,
             "why": "A seed is fed by the parent plant through the fruit, not "
                    "by nectar. Nectar is spent on attracting visitors."},
            {"text": "To keep its pollen damp and heavy so that the wind "
                     "cannot lift it out of the flower.", "correct": False,
             "why": "A wind-pollinated plant wants its pollen blown away, and "
                    "makes no nectar at all."},
            {"text": "To drive off the insects that would otherwise eat the "
                     "flower.", "correct": False,
             "why": "Nectar draws insects in rather than driving them off. "
                    "That is exactly what it is for."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e22",
        "band": "easier",
        "text": "What is the difference between a honeybee and a solitary "
                "bee?",
        "options": [
            {"text": "A solitary bee is simply a young honeybee that has not "
                     "yet been accepted into a hive of its own.",
             "correct": False,
             "why": "They are different species altogether, not different "
                    "ages of one. A solitary bee never joins anything."},
            {"text": "A honeybee lives in a hive with thousands of others; a "
                     "solitary bee nests alone.", "correct": True},
            {"text": "A honeybee pollinates crops, and a solitary bee only "
                     "visits garden flowers.", "correct": False,
             "why": "Solitary bees pollinate crops, and several of them do it "
                    "better than a honeybee does."},
            {"text": "A solitary bee makes honey but keeps all of it for "
                     "herself.", "correct": False,
             "why": "Solitary bees make no honey. Honey is a honeybee "
                    "colony's winter store, and most pollinators make none."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e23",
        "band": "easier",
        "text": "Which of these would leave a farm with fewer wild "
                "pollinators on it?",
        "options": [
            {"text": "Sowing a strip of wildflowers along the edge of each "
                     "field.", "correct": False,
             "why": "A flower strip gives pollinators food outside the crop's "
                    "own few weeks of bloom, so it raises their numbers."},
            {"text": "Mowing the verges late in the year, once the flowers "
                     "have set their seed.", "correct": False,
             "why": "Late mowing lets the verge flower and seed, which is one "
                    "of the cheapest things a landowner can do for them."},
            {"text": "Ploughing every bank and hedge bottom, leaving no rough "
                     "ground.", "correct": True},
            {"text": "Spraying insecticide at dusk rather than in the middle "
                     "of the day, when the bees are out.", "correct": False,
             "why": "Spraying when the bees and hoverflies have stopped flying "
                    "kills fewer of them, so it helps rather than harms."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e24",
        "band": "easier",
        "text": "A family buys a beehive because they have read that "
                "pollinators are in trouble. Does the hive help those "
                "pollinators?",
        "options": [
            {"text": "Yes, because honeybees are the pollinator whose numbers "
                     "have fallen furthest.", "correct": False,
             "why": "Managed honeybee colonies have risen rather than fallen. "
                    "The insects in trouble are the wild ones."},
            {"text": "Yes, because every extra bee in a landscape is another "
                     "pollinator at work.", "correct": False,
             "why": "A dense hive in a flower-poor landscape competes with the "
                    "wild insects for what little there is."},
            {"text": "No, because honeybees do not visit crop flowers at "
                     "all.", "correct": False,
             "why": "Honeybees visit crops constantly, which is why growers "
                    "hire them. The trouble is that they are not the group in "
                    "decline."},
            {"text": "No — honeybees are a farmed animal, and the decline is "
                     "in the wild pollinators.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e25",
        "band": "easier",
        "text": "Which statement about insecticides and pollinators is "
                "right?",
        "options": [
            {"text": "Used sparingly, they leave more pollinating insects "
                     "alive on a farm.", "correct": True},
            {"text": "They are harmless to bees, because they are made to kill "
                     "crop pests.", "correct": False,
             "why": "A chemical made to kill insects rarely tells one insect "
                    "from another. Bees and hoverflies are insects too."},
            {"text": "They kill only the insects that are actually feeding on "
                     "the crop.", "correct": False,
             "why": "A spray settles on the whole crop, flowers included, and "
                    "reaches anything that lands on it."},
            {"text": "They make flowers produce more nectar, so more insects "
                     "come.", "correct": False,
             "why": "Nothing in an insecticide feeds a flower. It is there to "
                    "kill insects, and it does."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e26",
        "band": "easier",
        "text": "In parts of Sichuan in China, how are the apple and pear "
                "orchards pollinated?",
        "options": [
            {"text": "By hives of honeybees, brought in on lorries for the "
                     "three weeks the blossom lasts.", "correct": False,
             "why": "That is how a Californian almond orchard is pollinated. "
                    "In Sichuan the work is done by people."},
            {"text": "By people, who carry pots of pollen and brush it onto "
                     "the flowers.", "correct": True},
            {"text": "By the wind, because the orchards stand on open "
                     "hillsides.", "correct": False,
             "why": "Apple and pear flowers are built for insects and their "
                    "pollen is heavy and sticky. Wind will not move it."},
            {"text": "By wild bumblebees, encouraged by strips of wildflowers "
                     "along the rows.", "correct": False,
             "why": "Flower strips are one real way of supporting wild "
                    "pollinators, and it is not what those growers do. They "
                    "pollinate by hand."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e27",
        "band": "easier",
        "text": "A bee lands on a flower and pollen sticks to her. What has "
                "she come to the flower for?",
        "options": [
            {"text": "To carry pollen to the next flower, which is what she is "
                     "for.", "correct": False,
             "why": "Moving pollen is what happens, not what she came for. The "
                    "flower gets its pollination as a side effect of her "
                    "meal."},
            {"text": "To lay her eggs somewhere inside it where the young "
                     "will be safe from predators.", "correct": False,
             "why": "Bees provision a nest rather than laying in a flower. The "
                    "flower is a feeding stop."},
            {"text": "Food — the nectar and the pollen the flower is "
                     "offering.", "correct": True},
            {"text": "To gather the seeds that the flower has already made.",
             "correct": False,
             "why": "No seed exists yet; the flower has not been pollinated. "
                    "Nectar and pollen are what is on offer."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e28",
        "band": "easier",
        "text": "Which of these is a food security problem?",
        "options": [
            {"text": "A corner shop that has run out of one particular brand "
                     "of biscuit for the past week.", "correct": False,
             "why": "One product being unavailable is not a problem with the "
                    "food supply. Food security is about a population getting "
                    "enough, and enough of the right kind."},
            {"text": "A family that dislikes vegetables and chooses not to buy "
                     "any.", "correct": False,
             "why": "That is a choice rather than a supply problem. Food "
                    "security is about what a population can reliably get."},
            {"text": "A country where people get enough energy but many are "
                     "short of vitamins.", "correct": True},
            {"text": "A warehouse where stored grain has been stolen twice "
                     "this year.", "correct": False,
             "why": "The word is not about guarding food from theft. It is "
                    "about a population being able to rely on enough of it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e29",
        "band": "easier",
        "text": "Which of these animals is working as a pollinator?",
        "options": [
            {"text": "A blackbird pulling the ripe apples apart in autumn.",
             "correct": False,
             "why": "The fruit is already made, so the pollination happened "
                    "months earlier. The bird is eating, not pollinating."},
            {"text": "A hoverfly feeding at an apple blossom in spring.",
             "correct": True},
            {"text": "An earthworm dragging dead leaves down into the soil.",
             "correct": False,
             "why": "Earthworms never visit a flower. They feed on dead plant "
                    "material at ground level."},
            {"text": "A woodlouse feeding on the rotten wood of an old "
                     "branch.", "correct": False,
             "why": "Woodlice feed on dead and decaying material. A "
                    "pollinator is an animal that visits flowers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-e30",
        "band": "easier",
        "text": "Poor pollination leaves a fruit grower with a much smaller "
                "harvest than usual. What happens to the price in the shops?",
        "options": [
            {"text": "It falls, because each fruit is smaller and so worth "
                     "less.", "correct": False,
             "why": "Size affects what one fruit fetches, and the shelf price "
                    "is set by how much there is. Less fruit means a higher "
                    "price."},
            {"text": "It stays the same, because prices are fixed long before "
                     "the harvest.", "correct": False,
             "why": "Prices for fresh produce move with the size of the crop, "
                    "which is why a bad year is expensive."},
            {"text": "It falls, because growers sell everything quickly before "
                     "it spoils.", "correct": False,
             "why": "A short crop sells easily without cutting the price. It "
                    "is plenty that makes things cheap."},
            {"text": "It rises, because there is less of that fruit to go "
                     "round.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-04-s10",
        "band": "standard",
        "text": "Apples are about 0.9 dependent on insect pollination. If no "
                "insect visited an orchard at all, roughly how much of the "
                "usual crop would still be picked?",
        "options": [
            {"text": "About a tenth of it.", "correct": True},
            {"text": "About nine tenths of it, because 0.9 is the share that "
                     "survives without insects.", "correct": False,
             "why": "The figure is the share that depends on insects, so it is "
                    "the share that is lost. What is left is the other "
                    "tenth."},
            {"text": "None of it, because a crop that depends on insects sets "
                     "nothing without them.", "correct": False,
             "why": "That would be a dependence of 1, as with almonds and "
                    "cocoa. At 0.9 a small crop still sets."},
            {"text": "About half of it, because a partly dependent crop always "
                     "loses roughly half.", "correct": False,
             "why": "There is no standard loss. The figure differs from crop "
                    "to crop, and for apples it is nine tenths."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s11",
        "band": "standard",
        "text": "On a shelf of a hundred calorie points, milk carries 8 of "
                "them and is 0.15 dependent on insects. How many calorie "
                "points does milk lose if every pollinator goes?",
        "options": [
            {"text": "8 points, because the whole of the milk supply depends "
                     "on the insects in some way.", "correct": False,
             "why": "Only 0.15 of it does. Multiply the share of the shelf by "
                    "the dependence, which gives 1.2."},
            {"text": "0.15 points, reading the dependence straight off as a "
                     "number of points.", "correct": False,
             "why": "The dependence is a fraction rather than a count. It has "
                    "to multiply the 8 points milk holds."},
            {"text": "1.2 points.", "correct": True},
            {"text": "6.8 points, which is what is left once the loss has been "
                     "taken away.", "correct": False,
             "why": "That is the surviving part, not the loss. The loss is the "
                    "other piece: 8 multiplied by 0.15."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s12",
        "band": "standard",
        "text": "An orchard of 400 trees has to be pollinated by hand, and one "
                "worker can do 10 trees in a day. How many working days does "
                "the orchard need?",
        "options": [
            {"text": "4,000 working days, multiplying the trees by the rate.",
             "correct": False,
             "why": "Multiplying gives a far larger number than there are "
                    "trees. Divide the 400 trees by the 10 a worker does."},
            {"text": "40 working days.", "correct": True},
            {"text": "410 working days, adding the trees and the daily rate "
                     "together.", "correct": False,
             "why": "Adding two quantities of different kinds gives a number "
                    "that means nothing. The trees divide by the rate."},
            {"text": "10 working days, since 10 trees are done in each of "
                     "them.", "correct": False,
             "why": "10 is the rate rather than the answer. Four hundred trees "
                    "at ten a day takes forty days."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s13",
        "band": "standard",
        "text": "A farm normally harvests 200 tonnes of a crop, 40% of which "
                "depends on insect pollination. What harvest would you expect "
                "in a year with no pollinators at all?",
        "options": [
            {"text": "80 tonnes, which is the part of the harvest that "
                     "depended on the insects.", "correct": False,
             "why": "80 tonnes is what is LOST. What is harvested is the rest "
                    "of the 200, which is 120."},
            {"text": "160 tonnes, taking 40% to mean a fifth of the crop is at "
                     "risk.", "correct": False,
             "why": "40% is two fifths, not one. Two fifths of 200 tonnes is "
                    "80, leaving 120 tonnes."},
            {"text": "200 tonnes, because the plants still grow and flower "
                     "whatever the insects do.", "correct": False,
             "why": "Growing and flowering is not the same as setting a crop. "
                    "Without pollination those flowers set nothing."},
            {"text": "120 tonnes.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s14",
        "band": "standard",
        "text": "A government wants to protect the vitamins and minerals in "
                "its population's diet. Which crops should it be most careful "
                "about?",
        "options": [
            {"text": "The insect-pollinated ones — the fruit, the nuts and the "
                     "vegetables.", "correct": True},
            {"text": "The cereals, since bread and rice are eaten at almost "
                     "every meal in the country.", "correct": False,
             "why": "Cereals are the energy supply, and they carry little of "
                    "the vitamin and mineral load. They are also the crops "
                    "least at risk."},
            {"text": "The potato crop, because potatoes are grown in larger "
                     "quantities than any fruit.", "correct": False,
             "why": "Potatoes supply useful vitamin C and a great deal of "
                    "energy, and they are grown from tubers, so no pollinator "
                    "decline reaches them."},
            {"text": "Whichever crops are grown on the largest area of land in "
                     "the country.", "correct": False,
             "why": "Area says how much land a crop takes, not what it "
                    "contributes to a diet. The largest areas are usually "
                    "cereals."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s15",
        "band": "standard",
        "text": "Two fields of insect-pollinated beans are farmed the same "
                "way. One is bordered by a wood and rough grassy banks; the "
                "other lies in the middle of bare arable land. Which yields "
                "more, and why?",
        "options": [
            {"text": "The bare one, because there is nothing beside it "
                     "competing with the beans for water and light.",
             "correct": False,
             "why": "A hedge takes a little water and light from its own edge, "
                    "and what it gives back across the whole field is "
                    "pollinators."},
            {"text": "Neither — a bean crop sets the same yield wherever it is "
                     "grown, as long as the soil is the same.", "correct":
             False,
             "why": "Soil is not the only thing a crop needs. An "
                    "insect-pollinated crop also needs the insects, and they "
                    "have to live somewhere."},
            {"text": "The one beside the wood, because the wood and banks give "
                     "pollinators somewhere to nest and feed.", "correct":
             True},
            {"text": "The one beside the wood, because the trees shelter the "
                     "crop from the wind.", "correct": False,
             "why": "Shelter helps a little and beans are not "
                    "wind-pollinated. The gain here is in how well the flowers "
                    "were visited."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s16",
        "band": "standard",
        "text": "After a cold, wet spring in which very few insects were "
                "flying, a grower's strawberries are small and lumpy. Explain "
                "the link.",
        "options": [
            {"text": "The cold slowed the plants down, so the fruit had less "
                     "time to swell before picking.", "correct": False,
             "why": "Cold does slow a plant, and it would give small fruit of "
                    "the usual shape. Lumpy fruit points at pollination."},
            {"text": "Few visits means little pollen moved, and a partly "
                     "pollinated flower sets a poor fruit.", "correct": True},
            {"text": "The rain washed the nectar out of the flowers, so the "
                     "fruit had nothing to grow from.", "correct": False,
             "why": "Nectar feeds the insect rather than the fruit. What the "
                    "fruit needed was pollen, and few insects were there to "
                    "carry it."},
            {"text": "Wet weather spread a disease through the crop, which is "
                     "what misshapes a berry.", "correct": False,
             "why": "Disease is a real risk in a wet spring and it marks or "
                    "rots the fruit rather than misshaping it. Poor "
                    "pollination is the simpler explanation here."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s17",
        "band": "standard",
        "text": "One garden has something in flower from March to October. The "
                "garden next door has a single shrub that flowers for a "
                "fortnight in June. Why does the first hold more kinds of "
                "bee?",
        "options": [
            {"text": "Because a bigger garden always supports more species "
                     "than a smaller one does.", "correct": False,
             "why": "Nothing here says either garden is bigger. What differs "
                    "is how long there is food in it."},
            {"text": "Because different bees fly at different times of year "
                     "and all of them need feeding.", "correct": True},
            {"text": "Because shrubs produce no nectar, so no bee will visit "
                     "one at all.", "correct": False,
             "why": "Many shrubs are excellent for bees while they are out. "
                    "The trouble is the fortnight, not the shrub."},
            {"text": "Because bees can only feed on small flowers, and a shrub "
                     "carries large ones.", "correct": False,
             "why": "Bees work flowers of every size. What limits them here is "
                    "how much of the year the garden offers anything."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s18",
        "band": "standard",
        "text": "A council changes its rule and mows the road verges in late "
                "summer instead of early June. Why does that help "
                "pollinators?",
        "options": [
            {"text": "Because a late cut leaves the grass longer, which keeps "
                     "the ground warmer through the winter for them.",
             "correct": False,
             "why": "The verge is cut either way, so neither rule leaves cover "
                    "standing all winter. What the late cut protects is the "
                    "flowering."},
            {"text": "Because the mower kills fewer insects in August than it "
                     "does in June.", "correct": False,
             "why": "A mower is as dangerous in one month as another. The gain "
                    "is that the flowers were allowed to bloom."},
            {"text": "Because mowing in June cuts the verge flowers down "
                     "before they have bloomed and seeded.", "correct": True},
            {"text": "Because insects are asleep in late summer and so are not "
                     "disturbed by the work.", "correct": False,
             "why": "Late summer is one of the busiest times of an insect "
                    "year. The reason the timing matters is the flowers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s19",
        "band": "standard",
        "text": "A student says that pollinators matter because without them "
                "there would be no honey. What is the better answer?",
        "options": [
            {"text": "He is right, and honey is also the main food that wild "
                     "bees live on through the winter months.", "correct":
             False,
             "why": "Wild bees make no honey at all. Honey is a honeybee "
                    "colony's own winter store and nothing else depends on "
                    "it."},
            {"text": "They matter because most of our fruit, nuts and "
                     "vegetables need an insect visit to set.", "correct":
             True},
            {"text": "He is right, because honey is the only food that comes "
                     "to us directly from an insect.", "correct": False,
             "why": "Honey does come from an insect, and losing it would cost "
                    "a diet almost nothing. What would be lost is the fruit "
                    "and vegetables."},
            {"text": "They matter because bees eat the pests that would "
                     "otherwise destroy a crop.", "correct": False,
             "why": "Bees eat nectar and pollen, not pests. The service they "
                    "give a crop is the moving of pollen."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s20",
        "band": "standard",
        "text": "An insecticide label says: do not apply to a crop that is in "
                "flower. Why is that instruction there?",
        "options": [
            {"text": "Because a crop in flower is growing fast and the "
                     "chemical would burn the open petals.", "correct": False,
             "why": "Damage to the petals is not the concern. The concern is "
                    "the insects that come to them."},
            {"text": "Because the chemical would be carried into the fruit by "
                     "the pollen and reach the shopper.", "correct": False,
             "why": "Residues are a real matter and they are controlled by "
                    "how long before harvest a spray is used. The flowering "
                    "rule is there for the pollinators."},
            {"text": "Because an open flower is where the pollinators are, and "
                     "the spray would kill them.", "correct": True},
            {"text": "Because the pests the spray is aimed at hide inside the "
                     "flowers and cannot be reached.", "correct": False,
             "why": "A spray reaches a flower easily. What it reaches there "
                    "are the bees and hoverflies working it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s21",
        "band": "standard",
        "text": "A grower of glasshouse tomatoes buys in boxes of bumblebees "
                "every season and releases them inside. Why?",
        "options": [
            {"text": "Because the bumblebees eat the whitefly and other pests "
                     "that live on a tomato plant.", "correct": False,
             "why": "Bumblebees feed on nectar and pollen. Growers do buy "
                    "predatory insects for pests, and these are not them."},
            {"text": "Because the glasshouse is warm enough for bumblebees but "
                     "too warm for any other insect.", "correct": False,
             "why": "Plenty of insects thrive in a glasshouse. The point is "
                    "that a closed one keeps wild pollinators out."},
            {"text": "Because bumblebees make the flowers open earlier, which "
                     "brings the harvest forward.", "correct": False,
             "why": "An insect does not control when a flower opens. It moves "
                    "the pollen once the flower is open."},
            {"text": "Because tomatoes need an insect to set fruit, and a "
                     "closed glasshouse has no wild ones in it.", "correct":
             True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s22",
        "band": "standard",
        "text": "A supermarket buyer wants to know which of her fruit and "
                "vegetable lines are at risk from a decline in pollinators. "
                "What should she check for each one?",
        "options": [
            {"text": "Whether the part that is sold grew from a flower that "
                     "had to be pollinated.", "correct": True},
            {"text": "Whether the crop is grown in Britain or brought in from "
                     "another country.", "correct": False,
             "why": "Pollinators are declining in many countries, so where a "
                    "crop is grown does not settle it. What settles it is how "
                    "the crop sets."},
            {"text": "Whether beehives are kept anywhere near the farm the "
                     "crop comes from.", "correct": False,
             "why": "Hives nearby say something about honeybees and nothing "
                    "about the wild insects. First ask whether the crop needs "
                    "pollinating at all."},
            {"text": "Whether the crop is sold fresh or is frozen or tinned "
                     "before it reaches her.", "correct": False,
             "why": "What happens after harvest cannot change whether the crop "
                    "was set. The question is how the flower was pollinated."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s23",
        "band": "standard",
        "text": "Coffee and cocoa are grown in warm countries a long way from "
                "Britain. Explain why a decline of pollinators there is a food "
                "security matter here.",
        "options": [
            {"text": "Because the insects that pollinate them would move to "
                     "Britain and upset the crops grown here.", "correct":
             False,
             "why": "Tropical midges do not arrive in a British orchard. The "
                    "link is the trade, not the insects."},
            {"text": "Because Britain eats those crops, and what a country "
                     "eats need not be what it grows.", "correct": True},
            {"text": "Because losing them would leave Britain short of "
                     "calories, which is what food security means.",
             "correct": False,
             "why": "Coffee and cocoa carry very few of anybody's calories. "
                    "Food security is about food of the right kind as well as "
                    "enough of it."},
            {"text": "It is not a matter for Britain at all, since neither "
                     "crop can be grown in this climate.", "correct": False,
             "why": "Not growing something is exactly why it has to be bought "
                    "in. A supply that fails abroad fails here too."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s24",
        "band": "standard",
        "text": "A potato plant produces flowers, yet the potato crop would be "
                "completely unaffected by losing every pollinator. Explain.",
        "options": [
            {"text": "The flowers are pollinated by the wind, so no insect is "
                     "needed at any point.", "correct": False,
             "why": "Wind pollination is how the cereals manage. A potato crop "
                    "does not need pollinating by anything."},
            {"text": "The part we eat is a swollen underground stem, and new "
                     "plants are grown from it.", "correct": True},
            {"text": "Potato flowers pollinate themselves before they have "
                     "even opened.", "correct": False,
             "why": "Some plants do that, and it makes no difference here. The "
                    "crop is planted from tubers, so no seed is wanted."},
            {"text": "The flowers are removed by the farmer so that the plant "
                     "puts its energy into the tubers.", "correct": False,
             "why": "Nobody picks the flowers off a field of potatoes. The "
                    "crop is unaffected because it is grown from tubers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s25",
        "band": "standard",
        "text": "The pips on the outside of a strawberry are its seeds. Use "
                "that to explain why a poorly visited flower gives a lumpy "
                "berry rather than a small round one.",
        "options": [
            {"text": "The flesh swells only beside a pip that received pollen, "
                     "so the berry grows unevenly.", "correct": True},
            {"text": "The pips that got no pollen fall off, leaving hollows in "
                     "the surface of the berry.", "correct": False,
             "why": "The pips stay where they are. What differs is how much "
                    "the flesh under each one swells."},
            {"text": "A flower visited only a few times makes less sugar, and "
                     "sugar is what gives a berry its shape.", "correct":
             False,
             "why": "Sugar is what makes it sweet rather than what shapes it. "
                    "The shape follows which parts were pollinated."},
            {"text": "Insects that land on the young fruit bruise it, and a "
                     "bruised berry grows lumpy.", "correct": False,
             "why": "The trouble came from too few insect visits, not too "
                    "many. Nothing here bruised the fruit."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s26",
        "band": "standard",
        "text": "A country counts its beehives every year and the number keeps "
                "rising. Why is that a poor guide to how well its crops are "
                "being pollinated?",
        "options": [
            {"text": "Because hives are counted by beekeepers, who have a "
                     "reason to report more of them than they keep.",
             "correct": False,
             "why": "Nothing suggests the count is dishonest. The trouble is "
                    "that it describes one farmed species."},
            {"text": "Because a hive count says nothing about the wild insects "
                     "that do much of the pollinating.", "correct": True},
            {"text": "Because honeybees carry pollen only between flowers of "
                     "the same plant, so they pollinate nothing.",
             "correct": False,
             "why": "Honeybees are real and useful pollinators, which is why "
                    "growers hire them. They are simply not the whole of the "
                    "picture."},
            {"text": "Because the number of hives has in fact been falling for "
                     "fifty years.", "correct": False,
             "why": "Managed colonies have risen over that period. The "
                    "question is what the rise leaves out."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s27",
        "band": "standard",
        "text": "A charity asks people to plant lavender, which flowers in "
                "July and August, to help bees. What does that do, and what "
                "does it miss?",
        "options": [
            {"text": "It feeds bees in high summer, and leaves the rest of "
                     "their year unprovided for.", "correct": True},
            {"text": "It helps all year, because bees store lavender nectar "
                     "and live on it through the winter.", "correct": False,
             "why": "Only honeybees store food, and wild bees have to find "
                    "something in flower whenever they are flying."},
            {"text": "It does nothing at all, because bees will not feed on a "
                     "garden plant.", "correct": False,
             "why": "Lavender is one of the better garden plants for bees. The "
                    "gap is in the months it does not cover."},
            {"text": "It misses nothing, since July and August are the only "
                     "months bees are flying in Britain.", "correct": False,
             "why": "Bumblebee queens are out in March and some bees are still "
                    "flying in October. The flying season is far longer than "
                    "two months."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s28",
        "band": "standard",
        "text": "Predict what a total loss of insect pollinators would do to "
                "the price of chocolate and to the price of bread, and say "
                "why.",
        "options": [
            {"text": "Both would rise by about the same amount, because a "
                     "shock to farming raises every food price together.",
             "correct": False,
             "why": "Prices follow supply, and the two supplies are not "
                    "affected alike. Wheat would be untouched."},
            {"text": "Bread would rise far more, because wheat is the crop "
                     "grown on the most land.", "correct": False,
             "why": "Area does not decide it. Wheat is wind-pollinated, so its "
                    "supply would not change at all."},
            {"text": "Chocolate would rise enormously and bread hardly at all, "
                     "because cocoa depends on insects and wheat does not.",
             "correct": True},
            {"text": "Neither would change, because both are made from crops "
                     "that are harvested by machine.", "correct": False,
             "why": "How a crop is harvested has nothing to do with how it was "
                    "pollinated. Cocoa is entirely insect-pollinated."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s29",
        "band": "standard",
        "text": "Explain how a diet can be cheap, filling and still leave the "
                "people eating it unhealthy.",
        "options": [
            {"text": "Filling food is always low in energy, so the body never "
                     "gets what it needs from it.", "correct": False,
             "why": "Filling food is usually rich in energy — that is why it "
                    "fills. What it can lack is vitamins and minerals."},
            {"text": "Cheap food is always old food, and old food has lost "
                     "everything of value in it.", "correct": False,
             "why": "Price is not a measure of age, and dry staples keep for a "
                    "long time. The gap is in what they contain."},
            {"text": "Staples supply energy but few vitamins and minerals, and "
                     "a body needs both.", "correct": True},
            {"text": "Eating a large amount of anything makes a person "
                     "unhealthy, whatever the food is.", "correct": False,
             "why": "Someone doing heavy work needs a large amount. What "
                    "matters is whether the diet contains everything the body "
                    "needs."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-s30",
        "band": "standard",
        "text": "A country doubles its wheat harvest over twenty years, and "
                "over the same period the number of people with iron "
                "deficiency rises. Suggest how both can be true.",
        "options": [
            {"text": "Land that grew vegetables and pulses has been turned "
                     "over to wheat, so the diet has narrowed.", "correct":
             True},
            {"text": "Wheat draws iron out of the soil, so the other crops "
                     "grown near it contain less of it.", "correct": False,
             "why": "Crops do take minerals from soil, and that is not what "
                    "has happened here. What changed is what people are "
                    "eating."},
            {"text": "Eating more bread uses up the iron already stored in the "
                     "body.", "correct": False,
             "why": "Bread does not remove iron from a body. The shortage "
                    "comes from eating less of the foods that supply it."},
            {"text": "A larger harvest means more people, and a larger "
                     "population is always less healthy.", "correct": False,
             "why": "Population size does not decide whether a diet is "
                    "balanced. The question is what is on the plate."},
        ],
        "figure": None,
    },
    # ── harder ────────────────────────────────────────────────────────────
    {
        "id": "b9-04-h10",
        "band": "harder",
        "text": "A shelf carries 100 calorie points. Almonds hold 6 of "
                "them and are completely dependent on insects, apples hold "
                "4 and are half dependent, and coffee holds 2 and is half "
                "dependent. How many calorie points do the three lose "
                "between them if every insect pollinator goes?",
        "options": [
            {"text": "12 points, because all three of these crops are "
                     "visited by insects out in the field.",
             "correct": False,
             "why": "Only a crop that depends entirely on insects loses "
                    "all of its points. Two of these three keep half of "
                    "theirs."},
            {"text": "9 points, because each crop loses only the share "
                     "that depends on insects.",
             "correct": True},
            {"text": "6 points, because a crop that depends completely on "
                     "insects is the one that is lost.",
             "correct": False,
             "why": "A half-dependent crop loses half of its points rather "
                    "than none, so the apples and the coffee lose three "
                    "between them."},
            {"text": "3 points, because the two part-dependent crops are "
                     "the ones that lose.",
             "correct": False,
             "why": "The almonds lose all six of their points as well, "
                    "which is the largest single loss on the list."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h11",
        "band": "harder",
        "text": "On land where almost all the wild pollinators have gone, "
                "a grower sows flower-rich margins around his bean fields. "
                "In the first year the yield barely changes. By the third "
                "year it is clearly higher. Explain the delay.",
        "options": [
            {"text": "The crop itself needs three years to recover from "
                     "having that land taken out of production.",
             "correct": False,
             "why": "Taking a strip out of production lowers the area "
                    "sown; it does not injure the crop growing on the rest "
                    "of the field."},
            {"text": "Wild pollinator numbers take several seasons to "
                     "build up once the flowers and the nesting places are "
                     "there.",
             "correct": True},
            {"text": "Pollinators use a margin once it is old enough to "
                     "have hedgerow trees growing along it.",
             "correct": False,
             "why": "Solitary bees and bumblebees use young flower-rich "
                    "margins at once. What is missing in year one is the "
                    "insects, not the trees."},
            {"text": "The first two harvests were pollinated by insects "
                     "brought in from elsewhere, so the margins changed "
                     "nothing.",
             "correct": False,
             "why": "Nothing here says insects were brought in, and the "
                    "yield rose on the land where the margins were sown."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h12",
        "band": "harder",
        "text": "A grower wants to know whether poor fruit set in her bean "
                "field is caused by a shortage of pollinators. She leaves "
                "one plot open to insects, nets a second so that no insect "
                "can reach the flowers, and hand-pollinates every flower "
                "in a third. What does the hand-pollinated plot tell her "
                "that neither of the others can?",
        "options": [
            {"text": "How many insects visit each flower, which is what "
                     "the trial sets out to measure.",
             "correct": False,
             "why": "Nothing in the trial counts insects. It compares "
                    "yields under different amounts of pollination."},
            {"text": "Whether the beans would set any fruit without "
                     "insects, which the open plot by itself could not "
                     "show her.",
             "correct": False,
             "why": "That is what the netted plot is for. The "
                    "hand-pollinated plot is the opposite case: "
                    "pollination with no shortage at all."},
            {"text": "What the crop yields when pollination is not the "
                     "limit, so she can see what the open plot is losing.",
             "correct": True},
            {"text": "Whether the soil in that plot is as good as the soil "
                     "in the other two plots.",
             "correct": False,
             "why": "Hand-pollinating flowers says nothing about soil. It "
                    "changes how much pollen the flowers receive and "
                    "nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h13",
        "band": "harder",
        "text": "Apple trees flower earlier after a warm winter. A "
                "solitary bee that pollinates them emerges on a date set "
                "mostly by day length rather than by temperature. What "
                "problem does a run of warm winters create?",
        "options": [
            {"text": "The bees emerge earlier too, so the two shift "
                     "together and nothing about the orchard changes.",
             "correct": False,
             "why": "Day length is the same every year whatever the "
                    "temperature, so the bees do not shift with the "
                    "blossom."},
            {"text": "The blossom can be over before the bees emerge, so "
                     "the flowers go unvisited.",
             "correct": True},
            {"text": "The warmth itself kills the bees off, so far fewer "
                     "of them survive through to the spring.",
             "correct": False,
             "why": "Nothing here says the warmth harms the bees. The "
                    "problem is when they appear, not whether they "
                    "survive."},
            {"text": "The trees make weaker pollen in a warm year, so each "
                     "visit a bee makes carries less of it.",
             "correct": False,
             "why": "Pollen quality is not what has changed. What has "
                    "changed is the timing of the flowers against the "
                    "timing of the insects."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h14",
        "band": "harder",
        "text": "A nature reserve refuses a beekeeper permission to place "
                "fifty hives on its land, even though the reserve wants "
                "its wild flowers pollinated. Suggest why.",
        "options": [
            {"text": "Fifty colonies would compete with the reserve's own "
                     "wild pollinators for the flowers there are.",
             "correct": True},
            {"text": "Honeybees do not visit wild flowers, so the hives "
                     "would do the reserve no good.",
             "correct": False,
             "why": "Honeybees visit wild flowers readily. The objection "
                    "is not that they do nothing, it is that there would "
                    "be too many of them."},
            {"text": "Honeybees are falling faster than the wild bees are, "
                     "so the reserve has to protect them somewhere else "
                     "instead.",
             "correct": False,
             "why": "It is the other way round. Managed colonies are more "
                    "numerous than they were fifty years ago; the wild "
                    "insects are the ones declining."},
            {"text": "Hives produce honey, and selling anything taken off "
                     "protected land is not allowed.",
             "correct": False,
             "why": "This is a question about the insects, not about "
                    "honey. A reserve that wanted the pollination would "
                    "not be stopped by the honey."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h15",
        "band": "harder",
        "text": "Two farms grow the same insect-pollinated crop. One is "
                "visited by a single managed bee species; the other by "
                "bumblebees, solitary bees, hoverflies and beetles. A "
                "cold, wet spring keeps honeybees inside the hive for most "
                "of the flowering period. Which farm's crop is better "
                "protected, and why?",
        "options": [
            {"text": "The first, because one well-managed species does the "
                     "work of several wild ones put together.",
             "correct": False,
             "why": "A managed species is easier to move and to count, but "
                    "it cannot work in weather that grounds it, and "
                    "nothing else on that farm can."},
            {"text": "Neither, because no insect of any kind flies in cold "
                     "and wet weather.",
             "correct": False,
             "why": "Hoverflies work in colder weather than bees will, "
                    "which is exactly what makes a mixture useful."},
            {"text": "The second, because a mixture of insects makes each "
                     "flower produce more nectar for them.",
             "correct": False,
             "why": "The insects do not change what the flower produces. "
                    "What a mixture changes is how many of them can fly on "
                    "a bad day."},
            {"text": "The second, because some of its pollinators fly in "
                     "weather the bees will never fly in.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h16",
        "band": "harder",
        "text": "Tomato flowers release their pollen only when a visiting "
                "insect vibrates them, which a bumblebee can do and a "
                "honeybee cannot. A glasshouse grower who hires honeybee "
                "hives instead gets a poor set of fruit. What does that "
                "show about replacing one pollinator with another?",
        "options": [
            {"text": "Any insect will do the job, as long as enough of "
                     "them are released into the glasshouse.",
             "correct": False,
             "why": "This grower released plenty and still got a poor set. "
                    "Numbers are not what was missing."},
            {"text": "Honeybees must be worse than bumblebees at every "
                     "crop there is, not just at this one.",
             "correct": False,
             "why": "Honeybees pollinate a great many crops perfectly "
                    "well. It is this particular flower they cannot work."},
            {"text": "A pollinator can only be replaced by one that can "
                     "work that particular flower.",
             "correct": True},
            {"text": "Tomatoes turn out to be wind-pollinated, so no "
                     "insect was ever going to make a difference.",
             "correct": False,
             "why": "The question says the flowers need an insect to "
                    "vibrate them, which is the opposite of wind "
                    "pollination."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h17",
        "band": "harder",
        "text": "Published figures for how much of the world's food supply "
                "depends on animal pollination range from under a tenth to "
                "more than a third. Why do careful estimates disagree so "
                "widely?",
        "options": [
            {"text": "Because nobody has ever measured how far any "
                     "individual crop depends on insects.",
             "correct": False,
             "why": "Crop by crop the dependence has been measured, which "
                    "is where figures like 0.9 for apples come from. The "
                    "disagreement is about how to add them up."},
            {"text": "Because the answer depends on whether food is "
                     "counted by weight, by what it costs, or by the "
                     "nutrients it carries.",
             "correct": True},
            {"text": "Because the figure changes so quickly from one "
                     "season to the next that any published estimate is "
                     "out of date within a year.",
             "correct": False,
             "why": "Crops and their pollinators do not change that fast. "
                    "The estimates differ because the question is asked in "
                    "different ways."},
            {"text": "Because every country grows a different set of "
                     "crops, so a single world figure cannot honestly be "
                     "worked out.",
             "correct": False,
             "why": "A world figure can be worked out, and several have "
                    "been. What has to be decided first is what counts as "
                    "a share of the food supply."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h18",
        "band": "harder",
        "text": "A long decline in pollinators makes fruit and vegetables "
                "scarcer and dearer, while bread and rice stay cheap. "
                "Which health effect would you expect to appear first, and "
                "in whom?",
        "options": [
            {"text": "Starvation, in the people who can least afford to "
                     "buy food.",
             "correct": False,
             "why": "The cheap foods are the ones that supply the "
                    "calories, and they are the ones that are unaffected."},
            {"text": "Vitamin and mineral deficiencies, in the people who "
                     "can least afford the dearer foods.",
             "correct": True},
            {"text": "Deficiencies, spread evenly through the whole "
                     "population however much people earn.",
             "correct": False,
             "why": "A price rise does not fall evenly. It reaches the "
                    "people with the least to spend first."},
            {"text": "No effect on health, because people would simply go "
                     "on to eat rather more bread and rice instead.",
             "correct": False,
             "why": "Bread and rice supply energy and very little vitamin "
                    "C, vitamin A or folate, so eating more of them does "
                    "not replace what was lost."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h19",
        "band": "harder",
        "text": "Some insecticides are put on the seed and taken up by the "
                "growing plant, so they are present in its tissues — "
                "including the pollen and nectar of its flowers. Why does "
                "the usual instruction, do not spray a crop that is in "
                "flower, not protect pollinators from these?",
        "options": [
            {"text": "Because the instruction covers crops that honeybees "
                     "visit and no others.",
             "correct": False,
             "why": "The instruction is about when to spray, not about "
                    "which insect visits. Here nothing is sprayed at "
                    "flowering time at all."},
            {"text": "Because these chemicals do no harm to insects, so no "
                     "instruction is needed.",
             "correct": False,
             "why": "They are insecticides, and an insecticide in the "
                    "nectar is reaching the insect that drinks it."},
            {"text": "Because the treatment is washed off the seed before "
                     "the plant grows, so the flowers are clean.",
             "correct": False,
             "why": "The question says the plant takes the chemical up, "
                    "which is the opposite of it being washed away."},
            {"text": "Because nothing is sprayed at flowering time at all; "
                     "the chemical is already inside the flower.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h20",
        "band": "harder",
        "text": "A trial reports that a pesticide is safe for bees, "
                "because no more bees died in the treated field than in an "
                "untreated one. Ecologists say the trial has missed "
                "something. What?",
        "options": [
            {"text": "A dose too small to kill can still leave a bee "
                     "feeding or finding its way home badly.",
             "correct": True},
            {"text": "The dead bees should have been counted in the "
                     "untreated field instead.",
             "correct": False,
             "why": "Both fields were counted, which is what makes it a "
                    "comparison. The gap is in what was counted, not "
                    "where."},
            {"text": "A pesticide harms bees that are already ill and no "
                     "others, so this colony proves nothing.",
             "correct": False,
             "why": "Pesticides are not limited to sick insects, and "
                    "nothing in the trial suggests the colony was unusual."},
            {"text": "A bee cannot be harmed by a pesticide unless it eats "
                     "the leaves of the crop itself.",
             "correct": False,
             "why": "Bees take in pesticide from nectar, pollen and spray "
                    "on their bodies. They do not have to eat leaves."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h21",
        "band": "harder",
        "text": "Orchards visited by both wild bees and honeybees set more "
                "fruit than orchards visited by either group alone, even "
                "when the total number of insect visits is the same. "
                "Suggest why.",
        "options": [
            {"text": "The two groups feed at different times and on "
                     "different parts of the tree, so flowers one group "
                     "never reaches are reached by the other.",
             "correct": True},
            {"text": "A flower that is visited twice over sets twice as "
                     "much fruit, so any two insects would have exactly "
                     "the same effect on the size of the crop.",
             "correct": False,
             "why": "The total number of visits is the same in both cases, "
                    "so the number of visits is not what differs here."},
            {"text": "Wild bees and honeybees carry different kinds of "
                     "pollen, so the flowers are given a wider choice.",
             "correct": False,
             "why": "They carry pollen from the same apple trees. What "
                    "differs is which flowers they reach, not what they "
                    "are carrying."},
            {"text": "Honeybees visit just the flowers that wild bees have "
                     "opened for them earlier in the day.",
             "correct": False,
             "why": "Apple flowers open on their own. No insect opens them "
                    "for another."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h22",
        "band": "harder",
        "text": "Carrots and onions are eaten as roots and bulbs, and the "
                "plants are lifted before they ever flower. Even so, a "
                "grower says that losing insect pollinators would "
                "eventually end both crops. Explain.",
        "options": [
            {"text": "The roots and bulbs would stop swelling without "
                     "insects visiting the leaves of the plant.",
             "correct": False,
             "why": "Insects visit flowers, not leaves, and the swelling "
                    "of a root is done by the plant's own photosynthesis."},
            {"text": "The crop is lifted before it flowers, so nothing "
                     "would change for these two.",
             "correct": False,
             "why": "This year's crop is safe. The seed that next year's "
                    "crop is grown from is not, because it comes from "
                    "flowers."},
            {"text": "Carrots and onions would simply have to be grown "
                     "from tubers instead, in much the way that potatoes "
                     "already are.",
             "correct": False,
             "why": "Neither plant produces a tuber. Both are grown from "
                    "seed, and the seed is the part that needs "
                    "pollinating."},
            {"text": "The seed for next year's crop comes from flowering "
                     "plants, and those flowers are only ever pollinated "
                     "by insects.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h23",
        "band": "harder",
        "text": "A crop is 0.8 dependent on insect pollination. Losing "
                "half of the pollinators cuts the insect-pollinated part "
                "of the harvest in half. What fraction of the usual "
                "harvest would you expect?",
        "options": [
            {"text": "About 40%, because losing half of the pollinators "
                     "halves the whole harvest.",
             "correct": False,
             "why": "Only the four fifths that depends on insects is "
                    "affected. The other fifth is untouched, so more than "
                    "half survives."},
            {"text": "About 80%, because that is the share of the crop "
                     "that depends on insects.",
             "correct": False,
             "why": "The 80% is the dependence, not the answer. Half of "
                    "that share is what is lost."},
            {"text": "About 20%, because the fifth of it that needs no "
                     "insect is what is left.",
             "correct": False,
             "why": "That is the answer for losing every pollinator, not "
                    "half of them."},
            {"text": "About 60%, because half of the 80% that depends on "
                     "insects is lost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h24",
        "band": "harder",
        "text": "A 100 hectare farm grows insect-pollinated fruit on 20 "
                "hectares, worth £4,000 a hectare, and wheat on the other "
                "80 hectares, worth £1,000 a hectare. What share of the "
                "farm's income comes from the fruit?",
        "options": [
            {"text": "Half of it, because the fruit earns £80,000 and the "
                     "wheat earns £80,000.",
             "correct": True},
            {"text": "A fifth of it, because the fruit is grown on a fifth "
                     "of the land.",
             "correct": False,
             "why": "Land and income are not the same thing. The fruit "
                    "earns four times as much per hectare as the wheat "
                    "does."},
            {"text": "Four fifths of it, because the fruit is worth four "
                     "times as much per hectare.",
             "correct": False,
             "why": "Four times as much per hectare, on a quarter of the "
                    "area, comes out level rather than four times ahead."},
            {"text": "Three quarters of it, because the fruit is far the "
                     "more valuable of the two crops.",
             "correct": False,
             "why": "Per hectare it is, but there is four times as much "
                    "wheat land. The two totals come out equal."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h25",
        "band": "harder",
        "text": "Over fifty years a farming region removed most of its "
                "hedgerows to make larger fields. Cereal yields rose. "
                "Yields of the region's insect-pollinated bean and oilseed "
                "crops became less reliable. Explain both changes.",
        "options": [
            {"text": "Cereals are insect-pollinated as well, so the two "
                     "kinds of crop should have moved together.",
             "correct": False,
             "why": "Cereals are wind-pollinated, which is exactly why "
                    "removing insect habitat left them alone."},
            {"text": "Hedges take nutrients out of the soil beside them, "
                     "so removing them helped every crop equally.",
             "correct": False,
             "why": "If removal helped everything equally the bean and "
                    "oilseed yields would have risen too, and they did "
                    "not."},
            {"text": "Larger fields suit machinery, but the hedges were "
                     "where the wild pollinators nested.",
             "correct": True},
            {"text": "The bean and oilseed crops were simply being sown "
                     "later in the year than they used to be.",
             "correct": False,
             "why": "Nothing here says the sowing date changed, and it "
                    "would not explain why the cereals did better at the "
                    "same time."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h26",
        "band": "harder",
        "text": "A student reads that the four-years-to-live quotation is "
                "false and concludes that a decline of pollinators is not "
                "a real problem. What is wrong with that conclusion?",
        "options": [
            {"text": "Nothing is wrong: a claim shown to be false should "
                     "be dropped.",
             "correct": False,
             "why": "What was shown false was one exaggerated version. The "
                    "measured losses of fruit, nuts and vegetables are a "
                    "separate claim."},
            {"text": "The quotation is true, so the source was simply "
                     "mistaken.",
             "correct": False,
             "why": "The quotation is false, and the page says so. That is "
                    "not where the reasoning goes wrong."},
            {"text": "An exaggerated version of a claim being false says "
                     "nothing at all about the real claim behind it.",
             "correct": True},
            {"text": "The problem is real because the number of honeybee "
                     "colonies is falling fast.",
             "correct": False,
             "why": "Managed colonies are more numerous than they were "
                    "fifty years ago. The decline is in the wild "
                    "pollinators."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h27",
        "band": "harder",
        "text": "An almond grower finds that his yield rises steeply when "
                "he goes from one hive per hectare to two, rises a little "
                "from two to three, and hardly at all from three to four. "
                "What is the most useful conclusion?",
        "options": [
            {"text": "Beyond about three hives a hectare, something other "
                     "than pollination is limiting the crop.",
             "correct": True},
            {"text": "Yield would keep on rising if he added hives, so he "
                     "should be hiring a great many more of them.",
             "correct": False,
             "why": "His own figures show the rise flattening off, which "
                    "is the opposite of what this predicts."},
            {"text": "Hives are useless on this crop, since the last ones "
                     "changed nothing.",
             "correct": False,
             "why": "The first hive made a large difference. What flattens "
                    "off is the benefit of adding more, not the benefit of "
                    "any."},
            {"text": "The bees in the later hives must have been weaker "
                     "than the first.",
             "correct": False,
             "why": "Nothing suggests the colonies differed. A crop only "
                    "needs so much pollen, and past that point more bees "
                    "add little."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h28",
        "band": "harder",
        "text": "Advisers to a government model a halving of pollinator "
                "numbers rather than their complete disappearance. Why is "
                "the partial loss the more useful scenario to model?",
        "options": [
            {"text": "A partial loss is easier to calculate, although it "
                     "describes nothing that is happening.",
             "correct": False,
             "why": "A partial loss is exactly what is happening, which is "
                    "why it is worth modelling. Ease of arithmetic is not "
                    "the reason."},
            {"text": "Halving the pollinators halves every crop, which "
                     "keeps the arithmetic simple for the advisers.",
             "correct": False,
             "why": "Crops differ in how far they depend on insects, so "
                    "halving the pollinators does not halve them all."},
            {"text": "A complete loss would leave the food supply almost "
                     "untouched, so there would be nothing very much worth "
                     "modelling.",
             "correct": False,
             "why": "A complete loss would take away most of the fruit, "
                    "nuts and vegetables. It is not a scenario with no "
                    "effect."},
            {"text": "It is closer to what is happening, and it gives "
                     "smaller crops and dearer food rather than empty "
                     "shelves.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h29",
        "band": "harder",
        "text": "Poorly pollinated strawberries and apples come out small "
                "and misshapen rather than absent. A supermarket that "
                "refuses misshapen fruit reports a far bigger loss of "
                "saleable crop than the farm's weight figures suggest. "
                "Explain.",
        "options": [
            {"text": "The farm's weighing equipment must be wrong, because "
                     "a small fruit weighs exactly as much as a large one "
                     "does.",
             "correct": False,
             "why": "A small fruit weighs less, which is why the weight "
                    "figures fall at all. The gap between the two figures "
                    "is about grading, not scales."},
            {"text": "The fruit still grows, but a crop that fails a "
                     "grading standard never reaches the shop, even though "
                     "it exists.",
             "correct": True},
            {"text": "Misshapen fruit is caused by a shortage of water "
                     "rather than by poor pollination.",
             "correct": False,
             "why": "The question states that poor pollination is what "
                    "produced it, and a strawberry's shape follows from "
                    "how many of its seeds were set."},
            {"text": "The supermarket must be measuring a different crop "
                     "altogether from the one the farm grew and harvested.",
             "correct": False,
             "why": "Both are describing the same harvest. They differ in "
                    "what each one counts as a crop worth having."},
        ],
        "figure": None,
    },
    {
        "id": "b9-04-h30",
        "band": "harder",
        "text": "A government can afford one measure: paying farmers to "
                "leave flower-rich margins, or banning one widely used "
                "insecticide. What is the strongest reason for thinking "
                "the margins would help wild pollinators more?",
        "options": [
            {"text": "Insecticides have no effect on pollinators, so "
                     "banning one of them would change nothing much.",
             "correct": False,
             "why": "Insecticides do reach pollinators, which is why "
                    "sparing use is one of the things wild insects need."},
            {"text": "Margins raise the yield straight away, so the money "
                     "spent comes back within the same season.",
             "correct": False,
             "why": "Margins take a few years to establish and are not a "
                    "same-season return. That is not the argument for "
                    "them."},
            {"text": "Wild pollinators are not in decline anywhere, so of "
                     "the two it is the margins alone that would be worth "
                     "paying anything for.",
             "correct": False,
             "why": "Wild pollinators are the group in decline. That is "
                    "the whole reason either measure is being considered."},
            {"text": "Pollinators need somewhere to feed and to nest "
                     "across the whole season, which a ban on its own "
                     "never provides.",
             "correct": True},
        ],
        "figure": None,
    },
]
