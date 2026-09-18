"""B5 lesson 06 — Flowers and pollination: twelve questions (MRB-269).

These probe the three things this lesson exists to sort out: which parts are
male, which are female and which are neither; what pollination is and where it
stops; and why two completely different-looking flowers are both solving one
delivery problem. The distractors are built from the lesson's three declared
misconceptions — REPRO-11 (flowers are the pretty part of the plant), REPRO-12
(all flowers are pollinated by insects) and REPRO-22 (the ovule and the ovary
are the same thing) — and from the errors that travel with them: that the
stigma and the anther are the same kind of part because both sit on a stalk,
that pollination and fertilisation are one event, that a fruit grows from the
petals, that a feathery stigma works by being stickier, and that a wind-
pollinated plant makes vast amounts of pollen because its grains are small
rather than because most of them are wasted. The `harder` band puts the ideas
somewhere the lesson never goes: Darwin's Madagascan orchid, a sealed
greenhouse of courgettes, a grains-per-seed count, and a flower photographed in
ultraviolet.

No question carries a `figure`. Both of this lesson's figures are declared at
`status: "needed"` — no artwork exists for either yet — so a question resting
on one would be a question resting on nothing.
"""

UNIT = "B5"
LESSON = "flowers-and-pollination"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-06-e01",
        "band": "easier",
        "text": "The stamen is the male part of a flower. Which two parts "
                "make it up?",
        "options": [
            {"text": "The stigma and the style.",
             "correct": False,
             "why": "Both of those are female, and both belong to the carpel. "
                    "The style is the stalk under the stigma, not the stalk "
                    "under the anther."},
            {"text": "The anther and the stigma.",
             "correct": False,
             "why": "The stigma is female. It is easy to confuse with the "
                    "anther because both sit at the top of a stalk, but one "
                    "makes pollen and the other catches it."},
            {"text": "The anther and the filament.",
             "correct": True},
            {"text": "The petal and the nectary.",
             "correct": False,
             "why": "Neither of those is male or female. Both are about "
                    "attracting an insect and paying it, not about making or "
                    "receiving gametes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e02",
        "band": "easier",
        "text": "After fertilisation, one part of the flower becomes a seed. "
                "Which part?",
        "options": [
            {"text": "The ovule — one ovule becomes one seed.",
             "correct": True},
            {"text": "The ovary, because it is where the seeds are held.",
             "correct": False,
             "why": "The ovary becomes the fruit. It contains the ovules, and "
                    "the container and the thing inside it are two different "
                    "parts."},
            {"text": "The pollen grain, once it has landed on a stigma.",
             "correct": False,
             "why": "A pollen grain carries the male gamete nucleus to the "
                    "stigma. It makes the delivery; it does not become the "
                    "seed."},
            {"text": "The stigma, which swells after pollen lands on it.",
             "correct": False,
             "why": "The stigma is a catching surface and stays one. What "
                    "swells after fertilisation is the ovary, lower down."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e03",
        "band": "easier",
        "text": "What were the small green flaps under a flower's petals "
                "doing before the flower opened?",
        "options": [
            {"text": "Holding the anthers up until the petals took over.",
             "correct": False,
             "why": "The filament holds the anther, before and after opening. "
                    "A petal never holds an anther at all."},
            {"text": "Making the nectar the flower would later offer.",
             "correct": False,
             "why": "Nectar is made in the nectary, at the base of the "
                    "flower. Sepals are protection, not payment."},
            {"text": "Catching the first pollen grains to arrive.",
             "correct": False,
             "why": "Catching pollen is the stigma's job, and it only starts "
                    "once the flower is open. Sepals catch nothing."},
            {"text": "Enclosing the bud, with everything delicate folded "
                     "inside.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e04",
        "band": "easier",
        "text": "A wind-pollinated plant makes far more pollen than an "
                "insect-pollinated one. Why?",
        "options": [
            {"text": "Its grains are smaller, so many more of them fit inside "
                     "an anther.",
             "correct": False,
             "why": "Wind-borne grains are light and smooth, but size is not "
                    "what sets the number. The number follows from how much "
                    "is wasted."},
            {"text": "Almost all of it lands nowhere useful, so quantity "
                     "makes up for that.",
             "correct": True},
            {"text": "The wind damages the grains, so spares are needed to "
                     "replace them.",
             "correct": False,
             "why": "Moving air does not break pollen. It simply carries most "
                    "of it to places where there is no stigma waiting."},
            {"text": "It flowers only once a year, so a whole year's pollen "
                     "goes at once.",
             "correct": False,
             "why": "Timing is not the issue. Whenever a wind-pollinated "
                    "plant flowers, it releases enormous amounts, because "
                    "delivery is untargeted."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-06-s01",
        "band": "standard",
        "text": "Why is a wind-pollinated stigma large and feathery rather "
                "than small and sticky?",
        "options": [
            {"text": "A feathery surface is stickier than a smooth one, so "
                     "grains hold better.",
             "correct": False,
             "why": "Feathery is not the same as sticky. A wind-pollinated "
                    "stigma works by holding a large area open to the air, "
                    "like a net, not by gluing grains down."},
            {"text": "It has to give the pollen tube a wider route down to "
                     "the ovary.",
             "correct": False,
             "why": "The route down is the style's job, and it is the same in "
                    "both kinds of flower. The stigma is the catching surface, "
                    "nothing more."},
            {"text": "It has to take the weight of much heavier pollen grains "
                     "landing on it.",
             "correct": False,
             "why": "Wind-borne pollen is the lighter kind — smooth, light "
                    "and dry, so that it drifts. Weight is not what the shape "
                    "is about."},
            {"text": "It is fishing pollen out of moving air, so what it needs "
                     "is area.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s02",
        "band": "standard",
        "text": "Nectar costs a plant real sugar, made by photosynthesis and "
                "then given away. What comes back for it?",
        "options": [
            {"text": "An insect visiting flower after flower of the same "
                     "species, carrying pollen.",
             "correct": True},
            {"text": "Energy, because the feeding insect warms the flower "
                     "while it is there.",
             "correct": False,
             "why": "No energy comes back. The sugar goes out and stays out — "
                    "what returns is delivery, not fuel."},
            {"text": "Pollen, because the insect brings in grains that it has "
                     "made itself.",
             "correct": False,
             "why": "Insects make no pollen. Pollen is made in anthers, and "
                    "the insect only carries what it picked up in the last "
                    "flower."},
            {"text": "Protection, because the insects feeding there drive "
                     "other animals away.",
             "correct": False,
             "why": "Nectar buys transport, not defence. A feeding insect is "
                    "a paid courier, not a guard."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s03",
        "band": "standard",
        "text": "A student writes: “A bee lands on a flower, so the "
                "flower is fertilised.” What is wrong with that?",
        "options": [
            {"text": "Bees only take nectar, so a bee visit never moves any "
                     "pollen at all.",
             "correct": False,
             "why": "The bee is there for the nectar, but pollen sticks to it "
                    "on the way in and comes off in the next flower. That is "
                    "exactly how insect pollination works."},
            {"text": "The bee pollinates it — fertilisation is a later step, "
                     "after the pollen lands.",
             "correct": True},
            {"text": "Nothing is wrong: pollination and fertilisation are two "
                     "names for one event.",
             "correct": False,
             "why": "They are two events in order. Pollination is the "
                    "transfer of pollen to a stigma; fertilisation is the "
                    "fusing that can follow it."},
            {"text": "The bee would have to reach the ovary itself for the "
                     "flower to be fertilised.",
             "correct": False,
             "why": "No insect ever reaches the ovary. Pollen lands on the "
                    "stigma and a tube grows down from there — the bee's part "
                    "ends at the stigma."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s04",
        "band": "standard",
        "text": "You split open a pea pod and count nine peas. What does that "
                "tell you about the flower it grew from?",
        "options": [
            {"text": "Nine pollen grains landed on its stigma, and nothing "
                     "else did.",
             "correct": False,
             "why": "Far more grains than that can land, and landing is not "
                    "fertilising. The count that matches the peas is the "
                    "count of ovules fertilised."},
            {"text": "It had nine separate carpels, each one producing a "
                     "single seed.",
             "correct": False,
             "why": "The carpel is the whole female part — stigma, style, "
                    "ovary and ovules. All nine peas came from ovules inside "
                    "one ovary."},
            {"text": "Nine of its ovules were fertilised, because one ovule "
                     "becomes one seed.",
             "correct": True},
            {"text": "It had nine ovaries, one of them for each of the peas "
                     "in the pod.",
             "correct": False,
             "why": "The pod is the ovary — one ovary, swollen after "
                    "fertilisation. The peas inside it were its ovules."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-06-h01",
        "band": "harder",
        "text": "Darwin was sent an orchid whose nectar sat at the bottom of "
                "a spur nearly thirty centimetres long, and concluded that a "
                "moth with a tongue that long must exist. What made the "
                "length of the spur the key to his reasoning?",
        "options": [
            {"text": "Only a tongue that long could carry pollen from one "
                     "orchid across to the next.",
             "correct": False,
             "why": "A tongue does not have to be the thing that carries the "
                    "pollen. What the depth forces is contact between the "
                    "insect's body and the anthers."},
            {"text": "The pollen is made at the bottom of the spur, so a "
                     "shorter tongue would miss it.",
             "correct": False,
             "why": "Pollen is made in anthers, never in a nectar spur. The "
                    "spur holds the payment; the pollen is picked up on the "
                    "way in to it."},
            {"text": "A spur that deep could only be filled with nectar by a "
                     "very large visiting insect.",
             "correct": False,
             "why": "The plant makes its own nectar out of sugar from "
                    "photosynthesis. Nothing fills the spur from outside."},
            {"text": "Anything reaching that far in would be pressed against "
                     "the flower's anthers on the way.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h02",
        "band": "harder",
        "text": "A gardener grows courgettes in a sealed greenhouse that no "
                "insect can get into. The plants flower well, but almost no "
                "courgettes form. What has gone wrong?",
        "options": [
            {"text": "No pollen is reaching any stigma, so the flowers are "
                     "never pollinated.",
             "correct": True},
            {"text": "The flowers are making no pollen, because there is "
                     "nobody there to take it.",
             "correct": False,
             "why": "The anthers make pollen whether or not anything comes "
                    "for it. What is missing is the carrier, not the pollen."},
            {"text": "The courgette grows from the petals, and the petals are "
                     "dying back too early.",
             "correct": False,
             "why": "A courgette is the ovary of the flower, swollen after "
                    "fertilisation. No part of a fruit comes from a petal."},
            {"text": "There is no wind inside, and courgettes are "
                     "wind-pollinated in the way grass is.",
             "correct": False,
             "why": "A courgette flower is large, bright orange-yellow and "
                    "full of nectar. Everything about it says the carrier is "
                    "an animal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h03",
        "band": "harder",
        "text": "A researcher counts how much pollen two plants release for "
                "every seed they end up setting: plant A about thirty grains "
                "per seed, plant B about a million. What can you say?",
        "options": [
            {"text": "B is insect-pollinated, because every visiting insect "
                     "has to be loaded heavily.",
             "correct": False,
             "why": "An insect takes pollen straight to another flower of the "
                    "same species. That targeting is exactly why an "
                    "insect-pollinated plant can get away with so little."},
            {"text": "B is wind-pollinated, because untargeted delivery "
                     "wastes nearly everything released.",
             "correct": True},
            {"text": "A is wind-pollinated, because its grains are lighter "
                     "and so far fewer are needed.",
             "correct": False,
             "why": "Light grains drift, and drifting is precisely why huge "
                    "numbers are needed — the air takes them nowhere in "
                    "particular. Wasteful delivery means big numbers."},
            {"text": "Neither, because a count like that depends on flower "
                     "size rather than on the carrier.",
             "correct": False,
             "why": "A big insect-pollinated flower still makes modest "
                    "amounts. What sets the number is how much of the pollen "
                    "is wasted on the way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h04",
        "band": "harder",
        "text": "Photographed in ultraviolet light, a plain yellow flower "
                "turns out to have a dark bullseye around its centre. Bees "
                "see ultraviolet and we do not. What is that pattern most "
                "likely doing?",
        "options": [
            {"text": "Warning insects off, the way ultraviolet markings warn "
                     "that something is toxic.",
             "correct": False,
             "why": "This flower is paying insects to come. Nectar and a "
                    "landing platform are an invitation, not a warning."},
            {"text": "Showing which flowers a bee has already visited and "
                     "emptied of nectar.",
             "correct": False,
             "why": "The pattern is pigment in the petal. It is there before "
                    "any bee arrives and it is still there afterwards."},
            {"text": "Marking the centre for a bee, where the nectar and "
                     "anthers are.",
             "correct": True},
            {"text": "Helping us tell the species apart, which is why the "
                     "photograph was taken.",
             "correct": False,
             "why": "The pattern is not aimed at us — we cannot see it "
                    "without a camera. Its audience is the visitor that can."},
        ],
        "figure": None,
    },

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-06-e05",
        "band": "easier",
        "text": "In which part of a flower are pollen grains made?",
        "options": [
            {"text": "The stigma", "correct": False,
             "why": "The stigma is the surface at the top of the carpel where "
                    "pollen lands. It receives grains rather than making "
                    "them."},
            {"text": "The anther", "correct": True},
            {"text": "The ovule", "correct": False,
             "why": "An ovule sits inside the ovary and holds the female "
                    "gamete nucleus. It is the other half of the pairing."},
            {"text": "The nectary", "correct": False,
             "why": "The nectary makes nectar, the sugary liquid that pays a "
                    "visiting insect. It makes no gametes at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e06",
        "band": "easier",
        "text": "After fertilisation, what does the ovary of a flower "
                "become?",
        "options": [
            {"text": "The seed", "correct": False,
             "why": "One ovule becomes one seed. The ovary is the chamber "
                    "those ovules sat in, so it becomes what surrounds them."},
            {"text": "The stigma", "correct": False,
             "why": "The stigma is already there, at the top of the carpel, "
                    "and its job is finished once pollen has landed. It "
                    "withers rather than growing into anything."},
            {"text": "A new flower", "correct": False,
             "why": "Nothing turns into a new flower. The next flower is "
                    "grown separately by the plant, from a bud."},
            {"text": "The fruit", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-06-s05",
        "band": "standard",
        "text": "An insect-pollinated flower holds its anthers inside the "
                "flower, while a wind-pollinated one dangles them outside on "
                "long thin filaments. Explain the two positions.",
        "options": [
            {"text": "Inside keeps the pollen dry, and outside lets it warm "
                     "in the sun", "correct": False,
             "why": "Neither position is about the weather. Both are about "
                    "putting the pollen where whatever is going to carry it "
                    "will actually reach it."},
            {"text": "Inside protects the pollen from insects, and outside "
                     "lets the wind take it", "correct": False,
             "why": "An insect-pollinated flower needs the insect to touch "
                    "its anthers. It is not protecting the pollen from its "
                    "own courier."},
            {"text": "Inside, an insect must brush past them; outside, the "
                     "wind shakes the pollen loose", "correct": True},
            {"text": "Wind-pollinated anthers are too heavy to be held up "
                     "inside the flower", "correct": False,
             "why": "Wind-carried pollen is the lighter of the two, not the "
                    "heavier. The position is chosen for exposure, not forced "
                    "by weight."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s06",
        "band": "standard",
        "text": "A student labels the stigma as a male part of a flower, "
                "because pollen is found on it. What is wrong with that?",
        "options": [
            {"text": "The stigma is the female surface that catches pollen, "
                     "and the grains have only landed there", "correct": True},
            {"text": "Nothing is wrong — a part carrying pollen counts as "
                     "male", "correct": False,
             "why": "Then a bee’s back would be a male part too. What decides "
                    "it is the part’s own job, not what is temporarily stuck "
                    "to it."},
            {"text": "The stigma is neither male nor female, like the petals "
                     "and the sepals", "correct": False,
             "why": "Petals and sepals are neither. The stigma is the top of "
                    "the carpel, and the carpel is the female part of the "
                    "flower."},
            {"text": "The stigma is male only in wind-pollinated flowers, "
                     "where it catches the plant’s own pollen", "correct": False,
             "why": "A stigma is female in every flower. Its texture changes "
                    "with how the pollen is delivered; its job does not."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-06-h05",
        "band": "harder",
        "text": "A plant breeder wants to be certain that one particular "
                "flower is not pollinated by any other plant. Which single "
                "part should be covered, and why?",
        "options": [
            {"text": "The anthers, because that is the part of the flower "
                     "where pollen is made", "correct": False,
             "why": "Covering the anthers stops this flower’s own pollen "
                    "leaving. It does nothing to stop another plant’s pollen "
                    "arriving."},
            {"text": "The stigma, because pollination has happened only once "
                     "pollen lands on it", "correct": True},
            {"text": "The ovary, because that is the part where the seeds "
                     "will eventually form", "correct": False,
             "why": "The ovary is already enclosed at the base of the carpel, "
                    "and pollen never reaches it directly. The grain lands "
                    "higher up, on the stigma."},
            {"text": "The petals, because they are what attracts the insects",
             "correct": False,
             "why": "That would reduce insect visits and stop no wind-carried "
                    "grain at all. Only covering the receiving surface is "
                    "certain."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h06",
        "band": "harder",
        "text": "Many wind-pollinated trees flower in early spring, before "
                "their leaves have opened. Suggest why that timing helps "
                "them.",
        "options": [
            {"text": "Because insects are not yet active, so there is less "
                     "competition for them", "correct": False,
             "why": "A wind-pollinated tree is not competing for insects at "
                    "all — it attracts none and pays none. Nothing about its "
                    "pollination involves them."},
            {"text": "Because pollen is heavier later in the year and would "
                     "not travel so well", "correct": False,
             "why": "A species’ pollen does not change weight with the "
                    "season. What changes is what stands in its way."},
            {"text": "Because the flowers need direct sunlight in order to "
                     "open at all", "correct": False,
             "why": "Flowers open when the plant is ready to release or "
                    "receive pollen, not because light reaches them. Plenty "
                    "of flowers open in full shade."},
            {"text": "Because pollen drifts more freely through bare branches "
                     "than through a canopy of leaves", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · easier ─────────────────────────────────────────
    {
        "id": "b5-06-e07",
        "band": "easier",
        "text": "Which part of a flower catches pollen grains?",
        "options": [
            {"text": "The stigma", "correct": True},
            {"text": "The anther", "correct": False,
             "why": "The anther is where pollen grains are made and released. "
                    "Catching them is the other half of the journey."},
            {"text": "The sepal", "correct": False,
             "why": "The sepals enclosed the bud before it opened, and are "
                    "neither male nor female."},
            {"text": "The nectary", "correct": False,
             "why": "The nectary makes the sugary liquid that pays a visiting "
                    "insect. Nothing lands on it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e08",
        "band": "easier",
        "text": "Which four parts make up the carpel?",
        "options": [
            {"text": "Anther, filament, petal and sepal", "correct": False,
             "why": "The anther and filament are the male stamen; petals and "
                    "sepals are neither male nor female."},
            {"text": "Stigma, style, ovary and ovules", "correct": True},
            {"text": "Stigma, anther, ovary and nectary", "correct": False,
             "why": "The anther is male and the nectary is neither. The "
                    "missing pair are the style and the ovules."},
            {"text": "Petal, sepal, nectary and ovary", "correct": False,
             "why": "Only the ovary in that list is part of the carpel. The "
                    "other three are not reproductive parts at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e09",
        "band": "easier",
        "text": "Which part of a flower holds the anther up and out?",
        "options": [
            {"text": "The style", "correct": False,
             "why": "The style is the stalk that holds the stigma up. It "
                    "belongs to the female carpel, not to the stamen."},
            {"text": "The nectary", "correct": False,
             "why": "A nectary produces the sugary reward, deep in the "
                    "flower. It holds nothing up."},
            {"text": "The petal", "correct": False,
             "why": "A petal is an advertisement, and in some flowers it gives "
                    "an insect a platform. It carries no anther."},
            {"text": "The filament", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e10",
        "band": "easier",
        "text": "Down which part of a flower does the pollen tube grow?",
        "options": [
            {"text": "The filament", "correct": False,
             "why": "The filament is the male stalk carrying the anther. "
                    "Nothing grows down it."},
            {"text": "The style", "correct": True},
            {"text": "The sepal", "correct": False,
             "why": "A sepal is a small green flap under the petals, with no "
                    "route through it to anywhere."},
            {"text": "The petal", "correct": False,
             "why": "Petals attract visitors and no part of the journey to the "
                    "ovary passes through one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e11",
        "band": "easier",
        "text": "In which part of a flower is nectar made?",
        "options": [
            {"text": "The ovary", "correct": False,
             "why": "The ovary holds the ovules and becomes the fruit. It "
                    "makes no nectar."},
            {"text": "The anther", "correct": False,
             "why": "The anther makes pollen grains. Nectar is made in a "
                    "separate part at the base of the flower."},
            {"text": "The nectary", "correct": True},
            {"text": "The stigma", "correct": False,
             "why": "The stigma is the catching surface for pollen. Nothing is "
                    "manufactured there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e12",
        "band": "easier",
        "text": "What is the job of a petal?",
        "options": [
            {"text": "To attract insects by colour and scent, and give them "
                     "somewhere to land", "correct": True},
            {"text": "To make the pollen grains that an insect will carry "
                     "away", "correct": False,
             "why": "Pollen is made in the anthers. A petal makes nothing at "
                    "all."},
            {"text": "To catch the pollen grains that a visiting insect brings "
                     "in", "correct": False,
             "why": "Catching pollen is the stigma's job. A petal is the "
                    "advertisement that gets the insect there."},
            {"text": "To enclose and protect the whole of the flower while "
                     "it is still just a bud", "correct": False,
             "why": "That is what the sepals did. By the time the petals are "
                    "on show, the bud has already opened."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e13",
        "band": "easier",
        "text": "Which parts of a flower are neither male nor female?",
        "options": [
            {"text": "The stigma, style and ovary", "correct": False,
             "why": "All three of those are female — they make up most of the "
                    "carpel."},
            {"text": "The anther and the filament", "correct": False,
             "why": "Those two are the male stamen. Between them they make "
                    "pollen and hold it in position."},
            {"text": "The ovules and the pollen grains", "correct": False,
             "why": "Those are the two that carry the gametes, so they are as "
                    "female and male as anything on the flower."},
            {"text": "The petals, sepals and nectary", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e14",
        "band": "easier",
        "text": "What does a pollen grain carry inside its tough case?",
        "options": [
            {"text": "A nucleus that will become the male gamete",
             "correct": True},
            {"text": "A female gamete nucleus, ready to be fertilised",
             "correct": False,
             "why": "The female gamete nucleus is in an ovule, inside the "
                    "ovary. A pollen grain carries the other half."},
            {"text": "A tiny seed, which grows once the grain lands",
             "correct": False,
             "why": "A seed is what a fertilised ovule becomes, much later. "
                    "Nothing inside a pollen grain is a seed."},
            {"text": "A drop of nectar, to pay the insect carrying it",
             "correct": False,
             "why": "Nectar is made in the nectary and taken by the insect "
                    "while it is there. Pollen carries no payment."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e15",
        "band": "easier",
        "text": "Whereabouts in a flower are the ovules?",
        "options": [
            {"text": "On the surface of the stigma", "correct": False,
             "why": "The stigma is the surface pollen lands on, at the top of "
                    "the carpel. The ovules are at the bottom of it."},
            {"text": "Inside the ovary", "correct": True},
            {"text": "Inside the anther, beside the pollen", "correct": False,
             "why": "The anther is male and holds pollen only. Ovules belong "
                    "to the female carpel."},
            {"text": "At the base of each petal", "correct": False,
             "why": "Petals carry no reproductive parts. The ovules are "
                    "enclosed in the chamber at the base of the carpel."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e16",
        "band": "easier",
        "text": "How many seeds does one fertilised ovule become?",
        "options": [
            {"text": "One", "correct": True},
            {"text": "Two", "correct": False,
             "why": "An ovule does not split into a pair. Counting the seeds "
                    "in a fruit counts the ovules that were fertilised, one "
                    "for one."},
            {"text": "Ten", "correct": False,
             "why": "A fruit with ten seeds had ten ovules fertilised, not "
                    "one. The relationship is one to one."},
            {"text": "None", "correct": False,
             "why": "A fertilised ovule is precisely what a seed grows from. "
                    "An ovule that is never fertilised is the one that becomes "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e17",
        "band": "easier",
        "text": "What are the petals of a wind-pollinated flower like?",
        "options": [
            {"text": "Large, brightly coloured and scented", "correct": False,
             "why": "That describes an insect-pollinated flower. A "
                    "wind-pollinated one has nobody to impress."},
            {"text": "Small, green, or missing altogether", "correct": True},
            {"text": "Broad and flat, to catch the pollen", "correct": False,
             "why": "Catching pollen is the stigma's job, and a "
                    "wind-pollinated stigma is feathery rather than flat."},
            {"text": "Thick and waxy, to hold the nectar", "correct": False,
             "why": "Nectar is held in a nectary, and a wind-pollinated flower "
                    "makes none at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e18",
        "band": "easier",
        "text": "Does a wind-pollinated flower produce nectar?",
        "options": [
            {"text": "Yes, but much less than an insect-pollinated one",
             "correct": False,
             "why": "It makes none. Nectar is a payment, and there is nothing "
                    "there to pay."},
            {"text": "Yes, and more than an insect-pollinated one",
             "correct": False,
             "why": "Nectar is expensive sugar, and a wind-pollinated flower "
                    "would get nothing back for it."},
            {"text": "No — the wind cannot be paid", "correct": True},
            {"text": "No, because its nectar is stored in the seeds instead",
             "correct": False,
             "why": "Nothing is stored anywhere. A wind-pollinated flower has "
                    "no nectary and makes no nectar."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e19",
        "band": "easier",
        "text": "What is wind-carried pollen like?",
        "options": [
            {"text": "Sticky, so that it holds together in the air",
             "correct": False,
             "why": "Sticky pollen clings to an insect. Grains that travel on "
                    "the air have to come apart and drift."},
            {"text": "Heavy, so that it drops onto a stigma below",
             "correct": False,
             "why": "A heavy grain falls straight down under the parent "
                    "flower. Wind-carried pollen is light enough to drift."},
            {"text": "Spiky, so that it catches on passing plants",
             "correct": False,
             "why": "Spikes are for clinging to an animal. What the wind needs "
                    "is a smooth grain that moves easily through air."},
            {"text": "Smooth, light and dry, so that it drifts",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e20",
        "band": "easier",
        "text": "What is insect-carried pollen like?",
        "options": [
            {"text": "Sticky or spiky, so that it clings", "correct": True},
            {"text": "Smooth and dry, so that it drifts", "correct": False,
             "why": "A smooth dry grain is built to be taken by moving air. On "
                    "an insect it would simply fall off."},
            {"text": "Made in enormous amounts, because most is lost",
             "correct": False,
             "why": "Enormous amounts belong to wind pollination. Delivery by "
                    "insect is targeted, so far less is needed."},
            {"text": "Made of nectar, so that the insect eats it",
             "correct": False,
             "why": "Nectar and pollen are two different things. The insect "
                    "takes the nectar and carries the pollen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e21",
        "band": "easier",
        "text": "What shape is the stigma of a wind-pollinated flower?",
        "options": [
            {"text": "Small and sticky", "correct": False,
             "why": "That is the insect-pollinated shape, built for a grain "
                    "that is placed on it by an animal."},
            {"text": "Large and feathery", "correct": True},
            {"text": "Long and hollow", "correct": False,
             "why": "Nothing on a flower is a hollow tube waiting for pollen. "
                    "The tube is grown afterwards, by the grain itself."},
            {"text": "Flat and waxy", "correct": False,
             "why": "A smooth waxy surface would hold nothing. What catches "
                    "grains out of the air is a large fringed one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e22",
        "band": "easier",
        "text": "A bee brushes past a flower's stigma on its way to the "
                "nectar. What shape does that stigma need to be, to catch "
                "the pollen stuck to the bee?",
        "options": [
            {"text": "Large and feathery", "correct": False,
             "why": "A feathery stigma is a net held out in moving air. An "
                    "insect-pollinated flower does not need one."},
            {"text": "Small and sticky", "correct": True},
            {"text": "Broad and papery", "correct": False,
             "why": "There is no papery catching surface. Sticky is what holds "
                    "a grain that an insect brushes against it."},
            {"text": "Hooked and stiff", "correct": False,
             "why": "Hooks belong to fruits that catch in fur, in a later "
                    "lesson. A stigma holds pollen by being sticky."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e23",
        "band": "easier",
        "text": "Which of these food crops are wind-pollinated?",
        "options": [
            {"text": "Apples, pears, plums and cherries", "correct": False,
             "why": "Those all come from trees with large scented flowers, and "
                    "every one of them is insect-pollinated."},
            {"text": "Strawberries, raspberries and blackcurrants",
             "correct": False,
             "why": "Those flowers offer petals and nectar, which is the "
                    "signature of a plant paying an animal."},
            {"text": "Wheat, rice, maize, barley and oats", "correct": True},
            {"text": "Beans, peas, courgettes and tomatoes", "correct": False,
             "why": "All four have showy flowers that attract insects. The "
                    "wind-pollinated staples are the grasses."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e24",
        "band": "easier",
        "text": "Which of these trees are wind-pollinated?",
        "options": [
            {"text": "Oak, beech, birch and hazel", "correct": True},
            {"text": "Apple, cherry, almond and lime", "correct": False,
             "why": "Those carry large scented flowers full of nectar, which "
                    "is how a plant pays an animal."},
            {"text": "Only trees that grow beside rivers", "correct": False,
             "why": "Where a tree grows does not decide it. What decides it is "
                    "whether the flower advertises."},
            {"text": "No trees at all are wind-pollinated", "correct": False,
             "why": "Most of the big trees in Britain are. Their flowers are "
                    "so plain that most people have never recognised one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e25",
        "band": "easier",
        "text": "What is nectar made from, and where does that material come "
                "from?",
        "options": [
            {"text": "Water, drawn straight up from the roots",
             "correct": False,
             "why": "Water costs the plant almost nothing. Nectar is a sugar "
                    "solution, and the sugar is expensive."},
            {"text": "Pollen, dissolved in sap inside the flower",
             "correct": False,
             "why": "Pollen is not dissolved into anything. Nectar is made "
                    "from sugar the plant produced by photosynthesis."},
            {"text": "Sugar, made by the plant itself in photosynthesis",
             "correct": True},
            {"text": "Sap, taken from a neighbouring plant of the same kind",
             "correct": False,
             "why": "Plants do not take sap from one another. The sugar in "
                    "nectar is the plant's own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e26",
        "band": "easier",
        "text": "Which part of a flower splits open when its pollen is ready?",
        "options": [
            {"text": "The ovary", "correct": False,
             "why": "The ovary stays closed around the ovules, and becomes the "
                    "fruit later on."},
            {"text": "The stigma", "correct": False,
             "why": "The stigma is a receiving surface and does not open. It "
                    "is the anther that releases pollen."},
            {"text": "The sepal", "correct": False,
             "why": "Sepals open when the bud does, which is before any pollen "
                    "is ready to leave."},
            {"text": "The anther", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e27",
        "band": "easier",
        "text": "Which part of a flower is an advertisement rather than a "
                "reproductive organ?",
        "options": [
            {"text": "The petal", "correct": True},
            {"text": "The anther", "correct": False,
             "why": "The anther makes pollen, so it is as reproductive as a "
                    "part can be."},
            {"text": "The ovule", "correct": False,
             "why": "An ovule holds a female gamete nucleus and becomes a "
                    "seed. Nothing about it is advertising."},
            {"text": "The stigma", "correct": False,
             "why": "The stigma receives pollen. It is part of the female "
                    "carpel, not part of the display."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e28",
        "band": "easier",
        "text": "Which two structures of a flower carry the gametes?",
        "options": [
            {"text": "The petals and the sepals", "correct": False,
             "why": "Neither carries a gamete. One advertises and the other "
                    "protected the bud."},
            {"text": "The stigma and the style", "correct": False,
             "why": "Those two receive pollen and give it a route down. The "
                    "gametes themselves are elsewhere."},
            {"text": "The pollen grains and the ovules", "correct": True},
            {"text": "The nectary and the ovary", "correct": False,
             "why": "The nectary makes payment and the ovary is the chamber "
                    "holding the ovules. The ovules are what carry a gamete "
                    "nucleus."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e29",
        "band": "easier",
        "text": "What does an insect get in return for visiting a flower?",
        "options": [
            {"text": "A seed, which it carries away", "correct": False,
             "why": "No seed exists yet at pollination, and an insect carries "
                    "pollen rather than seeds."},
            {"text": "Water, taken from the ovary", "correct": False,
             "why": "The ovary is a closed chamber holding ovules. Nothing is "
                    "drunk from it."},
            {"text": "Nectar, a sugary liquid", "correct": True},
            {"text": "Shelter for the winter", "correct": False,
             "why": "A flower lasts days rather than months. What it offers is "
                    "a sugar solution made in the nectary."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-e30",
        "band": "easier",
        "text": "What is an ovule?",
        "options": [
            {"text": "The chamber that contains the seeds after "
                     "fertilisation", "correct": False,
             "why": "That is the ovary. The ovule is one of the structures "
                    "inside it."},
            {"text": "A grain that carries a male gamete nucleus",
             "correct": False,
             "why": "That is a pollen grain, made in the anther. An ovule "
                    "holds the female half of the pairing."},
            {"text": "The stalk of tissue between the stigma and the ovary",
             "correct": False,
             "why": "That is the style. An ovule is not a stalk and does not "
                    "carry anything up or down."},
            {"text": "A structure inside the ovary holding a female gamete "
                     "nucleus", "correct": True},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · standard ───────────────────────────────────────
    {
        "id": "b5-06-s07",
        "band": "standard",
        "text": "Why can a flower that pays an insect get away with producing "
                "so little pollen?",
        "options": [
            {"text": "Because the insect carries it straight to another flower "
                     "of the same kind", "correct": True},
            {"text": "Because insect-carried grains are larger, so fewer of "
                     "them are needed", "correct": False,
             "why": "Size does not set the number. What sets it is how much of "
                    "the pollen ends up somewhere useful."},
            {"text": "Because the insect brings back any grains that fail to "
                     "arrive", "correct": False,
             "why": "Nothing is brought back. What makes the difference is "
                    "that far less is lost on the way in the first place."},
            {"text": "Because a flower with petals has less room inside it for "
                     "anthers", "correct": False,
             "why": "There is plenty of room. The modest amount is a "
                    "consequence of targeted delivery, not of space."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s08",
        "band": "standard",
        "text": "Why does a paid courier deliver pollen more reliably than "
                "moving air does?",
        "options": [
            {"text": "It is heavier, so it holds more grains at once than air "
                     "can", "correct": False,
             "why": "Load is not the point. What matters is where the load "
                    "ends up, and an insect goes somewhere useful."},
            {"text": "It visits flower after flower of the same species",
             "correct": True},
            {"text": "It takes the pollen straight down to the ovary itself",
             "correct": False,
             "why": "No insect reaches an ovary. An insect's part ends at the "
                    "stigma of the next flower."},
            {"text": "It can fly on days when there is not enough wind to "
                     "help", "correct": False,
             "why": "Flying on a still day is useful, but the real gain is "
                    "that the insect chooses flowers of one species."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s09",
        "band": "standard",
        "text": "Why do wind-pollinated flowers have no scent?",
        "options": [
            {"text": "Scent would be blown away too quickly to be any use",
             "correct": False,
             "why": "Scent carries perfectly well on moving air. The reason it "
                    "is absent is that there is nobody to smell it."},
            {"text": "Scent would attract insects that would eat the pollen",
             "correct": False,
             "why": "These flowers are not defending their pollen. They simply "
                    "have no use for a signal aimed at an animal."},
            {"text": "Scent is a signal to an animal, and no animal is "
                     "involved", "correct": True},
            {"text": "Scent is made in the petals, and these flowers have "
                     "green ones", "correct": False,
             "why": "A green petal could carry scent as easily as a coloured "
                    "one. The signal is dropped because nothing receives it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s10",
        "band": "standard",
        "text": "A flower is pale, heavily scented, and opens after dark. "
                "Suggest what carries its pollen.",
        "options": [
            {"text": "The wind, since colour would be wasted in the dark",
             "correct": False,
             "why": "A wind-pollinated flower does not bother with scent "
                    "either. Strong scent is a signal aimed at something "
                    "alive."},
            {"text": "An animal that hunts by smell rather than by sight",
             "correct": True},
            {"text": "An insect that finds flowers by their colour",
             "correct": False,
             "why": "Colour is no use at night, which is why this flower is "
                    "pale and relies on scent instead."},
            {"text": "Nothing — a flower that opens at night pollinates "
                     "itself", "correct": False,
             "why": "Opening is what a flower does to receive a visitor. "
                    "Scent and paleness are both signals for one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s11",
        "band": "standard",
        "text": "The style is described as doing two jobs. What are they?",
        "options": [
            {"text": "It makes pollen, and holds it where an insect will brush "
                     "past", "correct": False,
             "why": "Both of those belong to the stamen — the anther and the "
                    "filament. The style is female."},
            {"text": "It catches pollen, and feeds the grain once it has "
                     "landed", "correct": False,
             "why": "Catching is the stigma's job, and nothing feeds a grain. "
                    "The style raises the stigma and carries the tube."},
            {"text": "It protects the bud, and then holds the petals apart",
             "correct": False,
             "why": "Protecting the bud was the sepals' job. The style is "
                    "inside the flower and holds nothing apart."},
            {"text": "It raises the stigma, and gives the pollen tube its "
                     "route down", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s12",
        "band": "standard",
        "text": "Why does a wind-pollinated plant hold its stigmas outside the "
                "flower?",
        "options": [
            {"text": "Because they have to be in the moving air that carries "
                     "the pollen", "correct": True},
            {"text": "Because the petals would crush them if they were to "
                     "stay inside the flower", "correct": False,
             "why": "These flowers have almost no petals to crush anything. "
                    "The stigmas are outside because the pollen is outside."},
            {"text": "Because pollen lands on them only when it is raining",
             "correct": False,
             "why": "Rain washes pollen out of the air rather than delivering "
                    "it. What brings a grain to the stigma is wind."},
            {"text": "Because that keeps them away from the plant's own "
                     "anthers", "correct": False,
             "why": "The anthers hang outside too, on long filaments. Both are "
                    "out in the air for the same reason."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s13",
        "band": "standard",
        "text": "A grass floret has no petals at all. What does it carry "
                "instead?",
        "options": [
            {"text": "A thick waxy coat over the whole flower", "correct": False,
             "why": "Nothing is sealed over. What a grass has instead of "
                    "petals is exposure — its parts are out in the air."},
            {"text": "A ring of sepals doing the petals' job instead",
             "correct": False,
             "why": "Sepals protect a bud; they do not advertise. A grass "
                    "advertises to nothing at all."},
            {"text": "Anthers hanging outside on long filaments and large "
                     "feathery stigmas", "correct": True},
            {"text": "A single very large anther on a short stalk, to make "
                     "up for the missing petals", "correct": False,
             "why": "Grass flowers usually carry three ordinary anthers. What "
                    "is unusual is where they hang, not how big they are."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s14",
        "band": "standard",
        "text": "Why is hay fever described as a side effect of one "
                "pollination strategy?",
        "options": [
            {"text": "Because insect-carried pollen is stickier and so "
                     "irritates more", "correct": False,
             "why": "Sticky pollen stays on an insect and hardly ever gets "
                    "into the air at all. It is the airborne kind that is "
                    "breathed in."},
            {"text": "Because wind-pollinated plants release huge amounts of "
                     "loose pollen into the air", "correct": True},
            {"text": "Because pollen from a flower with petals is more likely "
                     "to be breathed in", "correct": False,
             "why": "A flower with petals hands its pollen to an animal. Very "
                    "little of it is ever loose in the air."},
            {"text": "Because grass pollen is larger than pollen from other "
                     "plants", "correct": False,
             "why": "Wind-carried grains are the small light ones. What "
                    "matters is the quantity that ends up in the air."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s15",
        "band": "standard",
        "text": "A pod is opened and forty seeds are counted inside. What is "
                "the least number of ovules the flower's ovary must have "
                "held?",
        "options": [
            {"text": "Forty", "correct": True},
            {"text": "One", "correct": False,
             "why": "An ovule does not divide into a row of seeds. One ovule "
                    "becomes one seed."},
            {"text": "Eighty", "correct": False,
             "why": "Seeds are not made in pairs. Each one comes from a single "
                    "fertilised ovule."},
            {"text": "None", "correct": False,
             "why": "A pollen grain supplies a male gamete nucleus. The seed "
                    "is the ovule, after fertilisation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s16",
        "band": "standard",
        "text": "Why would nectar be a waste of sugar for a wind-pollinated "
                "plant?",
        "options": [
            {"text": "Because rain would wash the nectar away before anything "
                     "drank it", "correct": False,
             "why": "Rain is not the problem. The problem is that there is "
                    "nobody there to be paid in the first place."},
            {"text": "Because nectar would make its pollen too sticky to "
                     "drift", "correct": False,
             "why": "Nectar is held in a nectary, well away from the anthers. "
                    "It would not touch the pollen."},
            {"text": "Because its pollen is too heavy for an insect to lift",
             "correct": False,
             "why": "Wind-carried pollen is the lighter of the two kinds. "
                    "Weight is not what rules the insect out."},
            {"text": "Because payment only works if there is somebody to pay",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s17",
        "band": "standard",
        "text": "Why are a petal's colour, pattern and scent described as "
                "aimed at a particular kind of visitor?",
        "options": [
            {"text": "Because different animals see and smell differently, so "
                     "a signal suits one of them", "correct": True},
            {"text": "Because all insects respond to exactly the same colours "
                     "and scents", "correct": False,
             "why": "They do not, which is why flowers differ so much. Some "
                    "patterns are in ultraviolet, which bees see and we do "
                    "not."},
            {"text": "Because the pattern is aimed at the people who have "
                     "chosen to grow the plant in a garden", "correct": False,
             "why": "None of it is aimed at us. Some of it we cannot even see "
                    "without a camera."},
            {"text": "Because colour and scent are produced by accident as the "
                     "petal grows", "correct": False,
             "why": "Both are costly and specific. A plant that needs no "
                    "advertising produces neither."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s18",
        "band": "standard",
        "text": "In many insect-pollinated flowers the anthers sit inside the "
                "cup of the petals, below the rim. Why does that position "
                "matter?",
        "options": [
            {"text": "It lets the pollen fall straight down onto the flower's "
                     "own stigma", "correct": False,
             "why": "Pollen falling onto its own flower travels nowhere. The "
                    "position puts it onto the insect instead."},
            {"text": "An insect going in for the nectar has to brush past "
                     "them", "correct": True},
            {"text": "It keeps the anthers dry when it rains on the open "
                     "flower", "correct": False,
             "why": "Shelter is a side effect at most. The arrangement is "
                    "about where the insect must pass."},
            {"text": "It lets the wind reach the anthers before the insects "
                     "do", "correct": False,
             "why": "Inside the cup is the one place the wind does not reach. "
                    "A wind-pollinated flower hangs its anthers outside."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s19",
        "band": "standard",
        "text": "Why is a flower called a reproductive organ rather than a "
                "decoration?",
        "options": [
            {"text": "Because it is the largest and most obvious part of most "
                     "plants", "correct": False,
             "why": "Plenty of flowers are tiny and plain — every grass has "
                    "them. What makes a flower a flower is what it does."},
            {"text": "Because it contains the chlorophyll that the plant "
                     "uses for making its own food", "correct": False,
             "why": "Food is made in the leaves. A flower makes and receives "
                    "gametes."},
            {"text": "Because it grows at the top of the stem, where it can be "
                     "seen", "correct": False,
             "why": "Position is not the test. A wind-pollinated flower may be "
                    "high up and still have nothing on show."},
            {"text": "Because every attractive feature is a signal or a "
                     "payment aimed at an animal", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s20",
        "band": "standard",
        "text": "Why have most people never noticed that grasses and oak trees "
                "have flowers?",
        "options": [
            {"text": "Because those flowers stay hidden underground until "
                     "the moment they are ready", "correct": False,
             "why": "They are in full view, often high up. They are simply not "
                    "shaped like the flowers most people picture."},
            {"text": "Because those plants flower once every several years",
             "correct": False,
             "why": "They flower every year, which is why hay fever comes "
                    "round every year with them."},
            {"text": "Because those flowers have nothing to attract with, so "
                     "they carry no display", "correct": True},
            {"text": "Because those plants flower only in the middle of the "
                     "night", "correct": False,
             "why": "Grasses and oaks flower by day. What they lack is not a "
                    "convenient time but a reason to advertise."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s21",
        "band": "standard",
        "text": "The stigma of an insect-pollinated flower has a sticky "
                "coating. What does it do?",
        "options": [
            {"text": "It traps the insect until it has been dusted with "
                     "pollen", "correct": False,
             "why": "Nothing is trapped. A flower that held its courier "
                    "captive would get no second delivery."},
            {"text": "It dissolves each grain so that its nucleus can be taken "
                     "in", "correct": False,
             "why": "The grain is not dissolved. It grows a tube of its own "
                    "down through the style."},
            {"text": "It feeds the insect standing on it", "correct": False,
             "why": "Payment is nectar, made in the nectary. The stigma offers "
                    "nothing to eat."},
            {"text": "It holds on to grains brushed against it", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s22",
        "band": "standard",
        "text": "Why does a wind-pollinated flower spend nothing on a landing "
                "platform?",
        "options": [
            {"text": "Because nothing lands on it — its pollen arrives on the "
                     "air", "correct": True},
            {"text": "Because a platform would collect rain and rot the flower "
                     "beneath it", "correct": False,
             "why": "Insect-pollinated flowers manage platforms in the rain "
                    "perfectly well. The reason is that no visitor arrives."},
            {"text": "Because its pollen is far too heavy to settle on a "
                     "platform", "correct": False,
             "why": "Wind-carried pollen is the light kind. Weight is not what "
                    "makes a platform pointless."},
            {"text": "Because it flowers before any insects are about in the "
                     "year", "correct": False,
             "why": "Some do flower early, but a summer grass does not. None "
                    "of them offers a platform at any time of year."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s23",
        "band": "standard",
        "text": "Why are the anthers of a grass carried on long, thin, "
                "flexible filaments?",
        "options": [
            {"text": "So that they are lifted out of reach of grazing "
                     "animals", "correct": False,
             "why": "A grazing animal eats the whole plant, filament and all. "
                    "The length puts the anther into the moving air."},
            {"text": "So that the slightest wind shakes the pollen loose",
             "correct": True},
            {"text": "So that they stay above the rain that falls on the "
                     "flower", "correct": False,
             "why": "A dangling anther is more exposed to rain, not less. It "
                    "hangs there to be shaken."},
            {"text": "So that they can hold more pollen than a short filament "
                     "would", "correct": False,
             "why": "A filament is a stalk and carries no pollen itself. The "
                    "pollen is in the anther at its end."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s24",
        "band": "standard",
        "text": "What has to be true of a pollen grain before an insect can "
                "carry it anywhere?",
        "options": [
            {"text": "It has to be lighter than the air around it",
             "correct": False,
             "why": "Nothing a plant makes is lighter than air. That is not "
                    "how even wind-carried pollen travels."},
            {"text": "It has to stick to the insect", "correct": True},
            {"text": "It has to be smooth and completely dry", "correct": False,
             "why": "Smooth and dry is built for drifting on air. On an insect "
                    "such a grain would fall straight off."},
            {"text": "It has to contain some nectar for the insect",
             "correct": False,
             "why": "Nectar is made separately, in the nectary. A pollen grain "
                    "carries a nucleus and nothing else."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s25",
        "band": "standard",
        "text": "A gardener strips every petal from a flower but leaves the "
                "rest of it untouched. What is most likely to follow?",
        "options": [
            {"text": "The flower stops making pollen, since the petals fed the "
                     "anthers", "correct": False,
             "why": "Petals feed nothing. The anthers go on making pollen "
                    "exactly as before."},
            {"text": "The ovary withers at once, because it needs the petals "
                     "around it", "correct": False,
             "why": "The ovary is untouched by the loss of petals. What "
                    "changes is how many insects come."},
            {"text": "Fewer insects visit, so less pollen is delivered",
             "correct": True},
            {"text": "The flower becomes wind-pollinated instead",
             "correct": False,
             "why": "Losing petals does not give a flower feathery stigmas or "
                    "dangling anthers. Its whole design still expects an "
                    "animal."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s26",
        "band": "standard",
        "text": "Why is a flower described as having a delivery problem?",
        "options": [
            {"text": "Its seeds cannot reach open soil without help",
             "correct": False,
             "why": "That is a problem about seeds, and it comes two steps "
                    "later. The delivery problem here is about pollen."},
            {"text": "Its pollen is too heavy to travel at all", "correct": False,
             "why": "Pollen travels perfectly well, by air or on an animal. "
                    "The difficulty is that the plant cannot take it there."},
            {"text": "Its gametes are in two places and the plant cannot move",
             "correct": True},
            {"text": "Its ovules have to be carried across to another flower",
             "correct": False,
             "why": "Ovules stay where they are, inside the ovary. It is the "
                    "pollen that has to make the journey."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s27",
        "band": "standard",
        "text": "Some plants carry male parts on one individual and female "
                "parts on another. What must be true for such a plant to set "
                "seed?",
        "options": [
            {"text": "It makes both pollen and ovules in every one of its "
                     "flowers", "correct": False,
             "why": "That is the arrangement this question rules out. Here the "
                    "two are on separate plants."},
            {"text": "Pollen has to travel from one plant across to another",
             "correct": True},
            {"text": "It sets seed without any pollination happening at all",
             "correct": False,
             "why": "No pollen, no seed. The ovules have to be reached before "
                    "anything becomes a seed."},
            {"text": "It has to be wind-pollinated rather than "
                     "insect-pollinated", "correct": False,
             "why": "Either carrier will do the job. What matters is that the "
                    "pollen crosses from one plant to the other."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s28",
        "band": "standard",
        "text": "Why does pollen have to arrive at a stigma rather than at an "
                "ovule?",
        "options": [
            {"text": "Because a grain is too large to fit inside an ovule",
             "correct": False,
             "why": "Size is not the obstacle. The ovules are shut inside the "
                    "ovary, where nothing lands."},
            {"text": "Because the ovules are enclosed in the ovary, and the "
                     "stigma is the receiving surface", "correct": True},
            {"text": "Because an ovule can only take one grain at a time",
             "correct": False,
             "why": "How many grains an ovule could take is beside the point. "
                    "No grain reaches one directly."},
            {"text": "Because the wall of the ovary would destroy any "
                     "pollen grain that happened to touch it",
             "correct": False,
             "why": "Nothing is destroyed. The grain never gets there — it "
                    "lands higher up, on the stigma."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s29",
        "band": "standard",
        "text": "A sticky microscope slide is left out in a field of grass "
                "beside a bed of roses. Whose pollen will be on it?",
        "options": [
            {"text": "The roses', because their grains are stickier",
             "correct": False,
             "why": "Sticky grains cling to an insect and hardly ever get into "
                    "the air. Very little rose pollen is ever loose."},
            {"text": "Both, in roughly equal amounts", "correct": False,
             "why": "Nothing like equal. One plant throws its pollen into the "
                    "air and the other hands it over."},
            {"text": "Neither of them, since pollen is carried directly "
                     "from one flower to another", "correct": False,
             "why": "Wind pollination is not direct at all. Grass pollen "
                    "drifts, which is exactly why it is on the slide."},
            {"text": "Mostly the grass's, because it is released into the air "
                     "in enormous amounts", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-s30",
        "band": "standard",
        "text": "The lesson closes by saying that both designs work. What does "
                "that mean?",
        "options": [
            {"text": "Both kinds of flower attract insects in the end",
             "correct": False,
             "why": "A wind-pollinated flower attracts nothing at all, and "
                    "still gets its pollen delivered."},
            {"text": "Each pays for delivery in its own currency — sugar, or "
                     "sheer numbers of grains", "correct": True},
            {"text": "Both kinds of flower produce the same number of seeds",
             "correct": False,
             "why": "Seed numbers vary enormously between species. The claim "
                    "is about the two ways of getting pollen delivered."},
            {"text": "Neither of the two designs costs the plant anything "
                     "that is really worth counting", "correct": False,
             "why": "Both cost a great deal: one in sugar given away, the "
                    "other in pollen thrown away."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 · harder ─────────────────────────────────────────
    {
        "id": "b5-06-h07",
        "band": "harder",
        "text": "A flower is found that carries stamens but no carpel at all. "
                "What follows about it?",
        "options": [
            {"text": "It can supply pollen, but it cannot produce seeds of its "
                     "own", "correct": True},
            {"text": "It can produce seeds, but supplies no pollen",
             "correct": False,
             "why": "That is the arrangement the other way round. Seeds come "
                    "from ovules, and the ovules are in the carpel this flower "
                    "does not have."},
            {"text": "It is not really a flower at all, since a flower needs "
                     "both kinds of part", "correct": False,
             "why": "Plenty of real flowers carry only one kind. Some species "
                    "even keep the two on separate plants."},
            {"text": "It must be wind-pollinated, since only wind-pollinated "
                     "flowers are built that way", "correct": False,
             "why": "Male-only and female-only flowers occur among "
                    "insect-pollinated species too. The missing carpel says "
                    "nothing about the carrier."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h08",
        "band": "harder",
        "text": "Darwin published the claim that a moth with a tongue about "
                "thirty centimetres long must exist. What made that a strong "
                "scientific claim rather than a guess?",
        "options": [
            {"text": "It fitted everything that had already been observed "
                     "about orchids in Madagascar", "correct": False,
             "why": "Fitting what is already known is the weak kind of claim. "
                    "This one said in advance what had yet to be found."},
            {"text": "It came from somebody whose other work had already "
                     "turned out to be correct", "correct": False,
             "why": "Who makes a claim does not make it strong. What made this "
                    "one strong is that anyone could go and look."},
            {"text": "It said in advance what must be found, and could be "
                     "shown wrong by looking", "correct": True},
            {"text": "It was so surprising that no other explanation of the "
                     "flower could be offered", "correct": False,
             "why": "Being surprising is not evidence. One reviewer treated it "
                    "as an absurdity, and it was still a good claim."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h09",
        "band": "harder",
        "text": "A hawkmoth with a proboscis of the right length was collected "
                "in 1903 and named praedicta. Why did naming it not finish the "
                "job?",
        "options": [
            {"text": "Because the moth had to be shown to be the very "
                     "species that Darwin himself had in mind",
             "correct": False,
             "why": "Darwin named no species at all. He said only that one "
                    "with a tongue of that length had to exist."},
            {"text": "Because the length of a tongue can only be measured on a "
                     "living animal", "correct": False,
             "why": "A collected specimen can be measured perfectly well. What "
                    "was missing was the feeding, not the measurement."},
            {"text": "Because a moth of the right length had still not been "
                     "seen feeding at the flower", "correct": True},
            {"text": "Because a prediction cannot be confirmed by a single "
                     "specimen of anything", "correct": False,
             "why": "One specimen of the right kind would settle the existence "
                    "claim. The open question was the mechanism."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h10",
        "band": "harder",
        "text": "A wind-pollinated crop is grown in a sealed glasshouse where "
                "the air is completely still, and it sets almost no grain. "
                "Explain that result.",
        "options": [
            {"text": "Without moving air the pollen never leaves the anthers "
                     "or reaches a stigma", "correct": True},
            {"text": "Without insects the flowers have nothing to attract, so "
                     "they never open", "correct": False,
             "why": "These flowers attract nothing in the first place, and "
                    "they open whether or not an insect is anywhere near."},
            {"text": "The glass blocks the light the flowers need in order to "
                     "make any pollen", "correct": False,
             "why": "A glasshouse is built to let light in. The missing "
                    "ingredient is movement of the air."},
            {"text": "Still air makes the pollen grains heavier, so they fall "
                     "before arriving", "correct": False,
             "why": "A grain's mass does not change with the weather. Nothing "
                    "shakes it loose or carries it in still air."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h11",
        "band": "harder",
        "text": "In one species the anthers of a flower ripen and shed their "
                "pollen a week before that same flower's stigma is ready. What "
                "does that timing achieve?",
        "options": [
            {"text": "It lets the flower fertilise itself far more reliably "
                     "than it otherwise could", "correct": False,
             "why": "It does the opposite. By the time its own stigma is "
                    "ready, its own pollen has gone."},
            {"text": "Its pollen leaves before its own stigma can receive it, "
                     "so it goes to other plants", "correct": True},
            {"text": "It doubles the amount of pollen the flower manages to "
                     "make in a season", "correct": False,
             "why": "Spreading two events apart in time makes no extra pollen. "
                    "What changes is where the pollen can end up."},
            {"text": "It lets the flower be pollinated by wind and by insects "
                     "at the same time", "correct": False,
             "why": "The carrier is decided by the flower's structure, not by "
                    "its timetable. Timing decides whose pollen arrives."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h12",
        "band": "harder",
        "text": "A thousand pollen grains of species A weigh 0.02 mg, and a "
                "thousand of species B weigh 0.30 mg. Which is more likely to "
                "be wind-pollinated?",
        "options": [
            {"text": "B, because a heavier grain carries further once it is "
                     "moving through the air", "correct": False,
             "why": "A heavy grain falls out of the air quickly. Staying up is "
                    "what gives the wind time to move it."},
            {"text": "Neither — mass says nothing about how a grain travels",
             "correct": False,
             "why": "Mass says a great deal here. Wind-carried grains are "
                    "smooth, dry and light, precisely so that they drift."},
            {"text": "B, because a wind-pollinated plant has to make "
                     "everything on a larger scale", "correct": False,
             "why": "It makes a larger NUMBER of grains, not larger grains. "
                    "Each one is light."},
            {"text": "A, because its grains are far lighter and so drift more "
                     "readily", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h13",
        "band": "harder",
        "text": "Counting the seeds in a fruit counts the ovules that were "
                "fertilised. Why does it not count the pollen grains that "
                "landed?",
        "options": [
            {"text": "Because pollen grains are destroyed as soon as they land "
                     "on a stigma", "correct": False,
             "why": "The grain is not destroyed. The reason the counts differ "
                    "is that the number landing is not fixed."},
            {"text": "Because one ovule becomes one seed, while the number of "
                     "grains landing varies", "correct": True},
            {"text": "Because every pollen grain that lands goes on to "
                     "become two seeds rather than one", "correct": False,
             "why": "No grain becomes a seed at all. A seed is a fertilised "
                    "ovule."},
            {"text": "Because pollen grains never land on a stigma in "
                     "countable numbers", "correct": False,
             "why": "They can be counted under a microscope quite easily. The "
                    "point is that the number is not fixed by the seeds."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h14",
        "band": "harder",
        "text": "Which single change to a flower would a bee notice first, and "
                "why?",
        "options": [
            {"text": "Losing its style, because that is the part a bee lands "
                     "on when it arrives", "correct": False,
             "why": "A bee lands on the petals, not on the style. The style is "
                    "inside, holding the stigma up."},
            {"text": "Losing its anthers, because a bee is looking for pollen "
                     "before anything else", "correct": False,
             "why": "Anthers are small and inside the flower. Nothing about "
                    "them is visible from any distance."},
            {"text": "Losing its ovary, because that is the largest part of "
                     "the whole flower", "correct": False,
             "why": "The ovary is enclosed at the base of the carpel and "
                    "cannot be seen from outside at all."},
            {"text": "Losing its petals, because those are the signal that "
                     "reaches a bee at a distance", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h15",
        "band": "harder",
        "text": "Some flowers offer no nectar and are still visited regularly "
                "by insects. What does that show about the rule “no nectar "
                "means wind-pollinated”?",
        "options": [
            {"text": "That the rule is perfectly sound, and those insects "
                     "are simply visiting it by mistake", "correct": False,
             "why": "Regular visits are not mistakes. A flower can pay in "
                    "other ways, or advertise without paying at all."},
            {"text": "That one feature on its own is not enough — the whole "
                     "set has to be read together", "correct": True},
            {"text": "That nectar has nothing to do with how a flower is "
                     "pollinated", "correct": False,
             "why": "Nectar is one of the strongest signs there is. It is just "
                    "not a test that works on its own."},
            {"text": "That every flower is insect-pollinated once you look "
                     "closely enough", "correct": False,
             "why": "Every grass and most large trees are wind-pollinated, and "
                    "no amount of looking changes that."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h16",
        "band": "harder",
        "text": "Compare what a grass spends on reproduction with what an "
                "apple tree spends.",
        "options": [
            {"text": "Both spend chiefly on sugar, since both have to feed "
                     "something that visits", "correct": False,
             "why": "A grass feeds nothing. Its whole expenditure goes on "
                    "grains that are thrown into the air."},
            {"text": "Both spend chiefly on quantity, since both lose most of "
                     "what they release", "correct": False,
             "why": "An apple tree loses very little, because its pollen is "
                    "handed from flower to flower by an animal."},
            {"text": "The grass spends on quantity of grains; the tree spends "
                     "sugar it made itself", "correct": True},
            {"text": "The grass spends more overall, because wind pollination "
                     "is the expensive method", "correct": False,
             "why": "Neither is simply the expensive one. They pay in "
                    "different currencies, and both designs work."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h17",
        "band": "harder",
        "text": "A newly described plant has large feathery stigmas and also "
                "bright petals with nectar. What should follow from that "
                "combination?",
        "options": [
            {"text": "Conclude at once that it is wind-pollinated, since the "
                     "stigmas settle it", "correct": False,
             "why": "One feature does not settle it against another. Two "
                    "features pointing opposite ways is a reason to look "
                    "further."},
            {"text": "Conclude at once that it is insect-pollinated, since the "
                     "petals settle it", "correct": False,
             "why": "The feathery stigmas point the other way, and ignoring "
                    "the evidence that does not fit is not a method."},
            {"text": "Conclude that it has no method of pollination at all, "
                     "given that the two signs disagree", "correct": False,
             "why": "Every flowering plant is pollinated somehow. Disagreeing "
                    "signs mean more observation is needed."},
            {"text": "Treat it as a case to be investigated, since the two "
                     "features point different ways", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h18",
        "band": "harder",
        "text": "The only insect that pollinates a particular plant disappears "
                "from an area. Predict what happens to that plant's seed "
                "production.",
        "options": [
            {"text": "It falls sharply, unless another animal takes the same "
                     "route through the flower", "correct": True},
            {"text": "It rises, because no nectar is being taken away from "
                     "any of the flowers any more", "correct": False,
             "why": "Nectar that nobody drinks buys nothing. Without a "
                    "carrier, the pollen stays where it was made."},
            {"text": "It is unaffected, because the wind will carry the pollen "
                     "instead", "correct": False,
             "why": "Sticky pollen and a small sticky stigma are useless in "
                    "moving air. This flower is built for an animal."},
            {"text": "It stops altogether and the plants themselves die within "
                     "the year", "correct": False,
             "why": "The plants go on growing. What is lost is the next "
                    "generation, not this one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h19",
        "band": "harder",
        "text": "What share of a wind-pollinated plant's pollen is likely to "
                "reach a stigma of its own species, and how can you tell?",
        "options": [
            {"text": "About half, since roughly half of the air moves in a "
                     "useful direction", "correct": False,
             "why": "Air does not divide neatly into useful and useless "
                    "halves. The plant's own output is the clue."},
            {"text": "A very small share — a plant has to release enormous "
                     "amounts for a few seeds", "correct": True},
            {"text": "Almost all of it, because the grains are so light that "
                     "they travel a long way", "correct": False,
             "why": "Travelling a long way is not the same as arriving "
                    "anywhere useful. Most of it lands where no stigma is."},
            {"text": "Most of it, simply because such a large number of grains "
                     "is released", "correct": False,
             "why": "The large number is a response to the waste, not "
                    "evidence against it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h20",
        "band": "harder",
        "text": "A grower plants a species that carries male and female "
                "flowers on separate individuals. What has to be arranged for "
                "any fruit to form?",
        "options": [
            {"text": "Every plant in the plot has to be a female one",
             "correct": False,
             "why": "Female plants alone supply no pollen. Nothing would be "
                    "fertilised at all."},
            {"text": "The two kinds have to flower at different times of the "
                     "year", "correct": False,
             "why": "Different times would mean no pollen was about when a "
                    "stigma was ready. They have to overlap."},
            {"text": "Both kinds have to be grown near enough for pollen to "
                     "move between them", "correct": True},
            {"text": "Insects have to be kept away, so that the pollen is not "
                     "taken off site", "correct": False,
             "why": "An insect is the carrier this plant may depend on. "
                    "Excluding it removes the delivery."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h21",
        "band": "harder",
        "text": "A grass floret is enclosed by two small papery bracts, and "
                "its anthers hang outside them. Explain why the anthers are on "
                "the outside.",
        "options": [
            {"text": "Anything inside the floret is out of the moving air that "
                     "shakes the pollen loose", "correct": True},
            {"text": "The papery bracts would soak up all the pollen if the "
                     "anthers were to stay inside them", "correct": False,
             "why": "Papery bracts absorb nothing. What matters is that no "
                    "wind reaches inside them."},
            {"text": "The anthers are too heavy to be supported inside so "
                     "small a floret", "correct": False,
             "why": "A grass anther weighs almost nothing. It hangs outside "
                    "for the wind, not for want of support."},
            {"text": "Being outside lets insects reach the anthers more "
                     "easily", "correct": False,
             "why": "A grass attracts no insects and offers them nothing. The "
                    "carrier here is moving air."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h22",
        "band": "harder",
        "text": "A student groups the petals with the carpel, on the grounds "
                "that both are involved in reproduction. Evaluate that "
                "grouping.",
        "options": [
            {"text": "It is sound, because a flower without petals sets no "
                     "seed at all", "correct": False,
             "why": "Every grass sets seed with no petals worth the name. "
                    "Petals help delivery; they are not part of it."},
            {"text": "It is sound, because the petals hold the pollen until an "
                     "insect arrives", "correct": False,
             "why": "Pollen is held in the anthers, which belong to the "
                    "stamen. A petal holds none of it."},
            {"text": "It is wrong: the carpel makes and receives gametes and "
                     "the petals do neither", "correct": True},
            {"text": "It is wrong, because the petals belong with the sepals "
                     "and the stamens instead", "correct": False,
             "why": "Petals do belong with the sepals as parts that are "
                    "neither male nor female. The stamens are male."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h23",
        "band": "harder",
        "text": "A flower has a nectar spur three centimetres deep, and every "
                "insect in the area has a tongue about one centimetre long. "
                "Predict what happens.",
        "options": [
            {"text": "Little of its pollen is moved, unless an insect with a "
                     "longer tongue arrives", "correct": True},
            {"text": "The insects take the nectar easily, since a spur holds "
                     "its nectar at the top", "correct": False,
             "why": "The nectar sits at the bottom of the spur. That is what "
                    "makes the depth matter at all."},
            {"text": "The flower fills its spur less deeply, so the local "
                     "insects can reach it", "correct": False,
             "why": "A flower does not adjust its own spur to its visitors. "
                    "The structure is what it is."},
            {"text": "The insects tear the spur open, which pollinates the "
                     "flower anyway", "correct": False,
             "why": "An insect that cuts in from the side never passes the "
                    "anthers, so no pollen is picked up."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h24",
        "band": "harder",
        "text": "One reviewer treated Darwin's long-tongued moth as an "
                "absurdity. Why does that reaction not count against the "
                "claim?",
        "options": [
            {"text": "Because a claim is judged by whether it can be tested, "
                     "not by how surprising it is", "correct": True},
            {"text": "Because the reviewer had not seen the orchid that "
                     "Darwin had been sent", "correct": False,
             "why": "What the reviewer had seen is beside the point. The claim "
                    "was testable by anyone who went and looked."},
            {"text": "Because a claim is judged by who makes it, and Darwin "
                     "had already been proved right", "correct": False,
             "why": "Authority settles nothing. The strength of the claim was "
                    "that it said in advance what must be found."},
            {"text": "Because it turned out to be right, which is what makes a "
                     "claim scientific", "correct": False,
             "why": "Being right afterwards is not what makes a claim "
                    "scientific. Being testable beforehand is."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h25",
        "band": "harder",
        "text": "Wheat, rice, maize, barley and oats are all grasses. What "
                "does that mean for the field they are grown in?",
        "options": [
            {"text": "Bees have to be brought in, or no grain is set at all",
             "correct": False,
             "why": "A grass offers a bee nothing and needs nothing from one. "
                    "Its pollen travels on the air."},
            {"text": "The crop must be pollinated by hand if the yield is to "
                     "be reliable", "correct": False,
             "why": "Nobody hand-pollinates a wheat field. Moving air does the "
                    "whole job."},
            {"text": "The crop sets grain without any pollination happening at "
                     "all", "correct": False,
             "why": "Pollination still happens — it is simply done by wind "
                    "rather than by an animal."},
            {"text": "Pollen moves between the plants on the air, with no "
                     "animal involved", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h26",
        "band": "harder",
        "text": "An insect-pollinated flower has a stigma only a millimetre or "
                "two across. Why is so small a catching surface enough?",
        "options": [
            {"text": "Because its pollen grains are much larger than "
                     "wind-carried ones", "correct": False,
             "why": "Grain size is not what decides it. What decides it is "
                    "that an animal puts the pollen exactly where it has to "
                    "go."},
            {"text": "Because the pollen is placed on it by an animal rather "
                     "than caught out of the air", "correct": True},
            {"text": "Because a small surface holds pollen more firmly than a "
                     "large one does", "correct": False,
             "why": "It is the sticky coating that holds a grain, not the "
                    "size. A large feathery stigma holds pollen perfectly "
                    "well."},
            {"text": "Because only a few grains are ever needed, however "
                     "they happen to arrive at the flower", "correct": False,
             "why": "Every ovule that becomes a seed has to be reached. A "
                    "wind-pollinated flower needs its grains just as much, and "
                    "still has a huge stigma."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h27",
        "band": "harder",
        "text": "A wind-pollinated plant spends nothing on colour, scent or "
                "nectar. What does it invest in instead?",
        "options": [
            {"text": "A thicker stem, so that the flowers are held higher "
                     "above the ground", "correct": False,
             "why": "Height helps a little, but the real spending is on "
                    "exposure and on grains — vast numbers of them."},
            {"text": "Larger seeds, since fewer of its flowers will be "
                     "pollinated in the end", "correct": False,
             "why": "Seed size is a separate question. What this plant spends "
                    "on is the pollen itself and the parts that expose it."},
            {"text": "Exposure and catching area, and enormous numbers of "
                     "grains", "correct": True},
            {"text": "A tougher stigma, so that grains arriving at speed do no "
                     "damage", "correct": False,
             "why": "A drifting grain arrives at no speed worth mentioning. "
                    "The feathery stigma is about area, not toughness."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h28",
        "band": "harder",
        "text": "Petals are usually coloured and sepals are usually green. "
                "Explain why the difference makes sense.",
        "options": [
            {"text": "Petals form later than sepals, and colour develops with "
                     "age in a plant", "correct": False,
             "why": "Colour is not a matter of age. It is a signal, and only "
                    "one of the two has anything to signal to."},
            {"text": "Sepals are green because they sit in the shade under the "
                     "petals", "correct": False,
             "why": "Shade does not make a structure green. Sepals protected "
                    "the bud, and a protective flap gains nothing from "
                    "colour."},
            {"text": "Petals signal to an animal, while sepals protected a bud "
                     "and had nothing to signal to", "correct": True},
            {"text": "Sepals are green because they carry out most of the "
                     "photosynthesis that the whole plant does",
             "correct": False,
             "why": "The leaves do almost all of it. A ring of small flaps "
                    "round one flower contributes very little."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h29",
        "band": "harder",
        "text": "A student writes that the anther is the male gamete. Correct "
                "that in two steps.",
        "options": [
            {"text": "The anther is the male gamete's stalk, and the filament "
                     "holds it in place", "correct": False,
             "why": "The filament is the stalk. The anther is where pollen is "
                    "made, and neither of them is a gamete."},
            {"text": "The anther makes pollen, and each grain carries a "
                     "nucleus that becomes the male gamete", "correct": True},
            {"text": "The anther is a single male gamete, and the ovule is "
                     "the female gamete that it has to match",
             "correct": False,
             "why": "An anther is an organ made of many cells. A gamete is a "
                    "single nucleus inside a pollen grain."},
            {"text": "The anther receives the male gamete, and the stigma "
                     "sends it out", "correct": False,
             "why": "That reverses the two. The anther releases pollen and the "
                    "stigma receives it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-06-h30",
        "band": "harder",
        "text": "Turn the claim “a wind-pollinated plant compensates with "
                "quantity” into something that could be tested.",
        "options": [
            {"text": "Weigh a whole wind-pollinated flower and a whole "
                     "insect-pollinated one, and then compare the two figures "
                     "obtained", "correct": False,
             "why": "Whole-flower mass mixes in petals, stalks and everything "
                    "else. The claim is about how much pollen is released."},
            {"text": "Count how many insects visit each kind of flower over a "
                     "fixed period of time", "correct": False,
             "why": "That tests who the visitors are. The claim is about the "
                    "number of grains a plant releases."},
            {"text": "Count the grains released for every seed set, and expect "
                     "a far larger figure for the wind-pollinated one",
             "correct": True},
            {"text": "Measure how far pollen travels from each kind of plant "
                     "on a windy afternoon", "correct": False,
             "why": "Distance is a different claim. Quantity is about how many "
                    "grains have to be made for each seed."},
        ],
        "figure": None,
    },
]
