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
]
