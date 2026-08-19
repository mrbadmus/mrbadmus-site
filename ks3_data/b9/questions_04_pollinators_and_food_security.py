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
]
