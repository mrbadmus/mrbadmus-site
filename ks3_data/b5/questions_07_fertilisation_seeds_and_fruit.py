"""B5 lesson 07 — Fertilisation, seeds and fruit: twelve questions (MRB-269).

These probe the two separations the lesson exists to make: delivery from
fusion, and a kitchen word from a biological one. The distractors are built
from the lesson's two declared misconceptions — REPRO-14 (pollination and
fertilisation are the same thing) and REPRO-13 (a tomato is a vegetable) — and
from the errors those two drag along with them: that fusion happens on the
stigma or partway down the style, that the whole pollen grain travels down the
tube, that the female nucleus comes up to meet it, that the ovule and the ovary
swap what they become, that a seed was already sitting in the ovary waiting to
grow, that one pollen grain can fertilise a whole ovary, that a fruit is
decided by sweetness, fleshiness or growing above ground, and that a swelling
ovary is what causes fertilisation rather than what follows it. The `harder`
band takes the lesson somewhere new each time: reading a cut cucumber backwards
to the flower it used to be, counting pollen tubes off a poppy's hundreds of
seeds, holding two plants apart on a timeline when one tube takes hours and the
other months, and settling the wheat grain — the case Design's own note calls
the one most likely to be challenged.
"""

UNIT = "B5"
LESSON = "fertilisation-seeds-and-fruit"
LESSON_NUMBER = 7

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-07-e01",
        "band": "easier",
        "text": "A pollen grain lands on the stigma of a flower of its own "
                "species. What does it do next?",
        "options": [
            {"text": "It is absorbed by the stigma and carried down to the "
                     "ovary in sap.",
             "correct": False,
             "why": "Nothing carries the grain anywhere. The grain itself "
                    "grows — it extends a tube of its own down through the "
                    "style."},
            {"text": "It grows a pollen tube down through the style towards "
                     "the ovary.",
             "correct": True},
            {"text": "It fuses with the ovule straight away, there on the "
                     "stigma.",
             "correct": False,
             "why": "There is no ovule on the stigma. The ovules are "
                    "centimetres away at the base of the carpel, and nothing "
                    "fuses until the tube reaches one."},
            {"text": "It splits open and the male gamete nucleus swims down "
                     "the style.",
             "correct": False,
             "why": "Nothing swims in a flowering plant. The nucleus travels "
                    "down inside the pollen tube, which is exactly why the "
                    "tube has to be grown first."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e02",
        "band": "easier",
        "text": "After fertilisation, two parts of the flower turn into two "
                "familiar things. Which pairing is right?",
        "options": [
            {"text": "The ovule becomes the seed and the ovary becomes the "
                     "fruit.",
             "correct": True},
            {"text": "The ovule becomes the fruit and the ovary becomes the "
                     "seed.",
             "correct": False,
             "why": "You have them the wrong way round. The ovary is the "
                    "chamber the ovules sit inside, so it ends up around "
                    "them — the fruit around the seeds."},
            {"text": "The ovule becomes the seed and the ovary withers away "
                     "afterwards.",
             "correct": False,
             "why": "It is the petals and stamens that wither. The ovary is "
                    "the one part that stays and swells."},
            {"text": "The ovule becomes the embryo and the ovary becomes the "
                     "seed.",
             "correct": False,
             "why": "The embryo comes from the two fused nuclei inside the "
                    "ovule. The whole ovule — embryo, food store and tough "
                    "coat — is the seed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e03",
        "band": "easier",
        "text": "The pollen tube has grown all the way down through the "
                "style. What has travelled down inside it?",
        "options": [
            {"text": "The whole pollen grain, moving along the tube it made.",
             "correct": False,
             "why": "The grain stays where it landed, on the stigma. The tube "
                    "is an extension of it, and only the nucleus makes the "
                    "journey."},
            {"text": "The female gamete nucleus, which has come up to meet it.",
             "correct": False,
             "why": "The female gamete nucleus does not move. It sits inside "
                    "an ovule, and everything that travels in this process "
                    "travels downwards to reach it."},
            {"text": "The male gamete nucleus, carried down from the grain.",
             "correct": True},
            {"text": "A tiny seed, ready to be released from the ovary.",
             "correct": False,
             "why": "No seed exists yet. A seed is what a fertilised ovule "
                    "becomes, so it turns up at the end of this process, not "
                    "at the start."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e04",
        "band": "easier",
        "text": "In a flowering plant, whereabouts does fertilisation "
                "actually happen?",
        "options": [
            {"text": "On the stigma, the moment a pollen grain lands on it.",
             "correct": False,
             "why": "That is pollination — delivery, and nothing more. "
                    "Nothing has fused while the grain is still sitting on "
                    "the stigma."},
            {"text": "In the style, about halfway down the pollen tube.",
             "correct": False,
             "why": "The male gamete nucleus only travels through the style. "
                    "The fusion happens at the end of that journey, not "
                    "partway along it."},
            {"text": "In the anther, where the pollen grains are made.",
             "correct": False,
             "why": "The anther makes and releases pollen. It is the wrong "
                    "end of the flower entirely, and it is not part of the "
                    "carpel at all."},
            {"text": "Inside an ovule, at the base of the carpel.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-07-s01",
        "band": "standard",
        "text": "A student writes: “A bee lands on the flower and "
                "fertilises it.” What is wrong with that sentence?",
        "options": [
            {"text": "Nothing — carrying pollen from one flower to another "
                     "is fertilisation.",
             "correct": False,
             "why": "This is the commonest error in the whole of plant "
                    "reproduction. A bee delivers pollen to a stigma, which "
                    "is pollination; fertilisation is a fusion that happens "
                    "later, somewhere else."},
            {"text": "Bees can pollinate a flower, but only wind-blown pollen "
                     "causes fertilisation.",
             "correct": False,
             "why": "How the pollen arrives makes no difference at all. "
                    "Insect or wind, the grain still has to grow a tube down "
                    "the style before anything fuses."},
            {"text": "The bee pollinates the flower; fertilisation happens "
                     "later, inside an ovule.",
             "correct": True},
            {"text": "The bee fertilises the stigma rather than the whole "
                     "flower.",
             "correct": False,
             "why": "Nothing is fertilised on the stigma. Fertilisation is "
                    "two gamete nuclei fusing, and both of them are at the "
                    "bottom of the style."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s02",
        "band": "standard",
        "text": "In a kitchen a pea pod is a vegetable. Why does a biologist "
                "call it a fruit?",
        "options": [
            {"text": "It developed from the ovary of the flower, and the peas "
                     "inside it are the seeds.",
             "correct": True},
            {"text": "It splits open by itself to let the peas out once they "
                     "are ready to go.",
             "correct": False,
             "why": "How a fruit opens, and how its seeds get away, is "
                    "dispersal — the next lesson. What makes something a "
                    "fruit is where it came from."},
            {"text": "The peas are sweet, and sweetness is what separates a "
                     "fruit from a vegetable.",
             "correct": False,
             "why": "Sweetness is a kitchen test, not a biological one. A "
                    "hazelnut is not sweet and is still a fruit; a carrot is "
                    "quite sweet and is still a root."},
            {"text": "It grows above the ground, and vegetables are the parts "
                     "that grow below it.",
             "correct": False,
             "why": "Celery and courgettes both grow above ground and only "
                    "one of them is a fruit. Height settles nothing; the "
                    "ovary settles it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s03",
        "band": "standard",
        "text": "Look at the top of a strawberry and there is a little green "
                "star. Which claim about it is right?",
        "options": [
            {"text": "It is the stigma, left behind after the pollen tubes "
                     "grew through it.",
             "correct": False,
             "why": "The stigma withers along with the petals and the "
                    "stamens. What is still there is lower down — the ring "
                    "that enclosed the bud."},
            {"text": "It is the petals, which dried out and turned green once "
                     "the fruit formed.",
             "correct": False,
             "why": "Petals do not turn green and stay; they are the first "
                    "parts abandoned. That star was green from the "
                    "beginning, because it is the sepals."},
            {"text": "It is a small leaf that grew up beside the fruit after "
                     "the flower had gone.",
             "correct": False,
             "why": "Nothing new grows there. Every part of that star was "
                    "already on the flower — they are the sepals that "
                    "enclosed the bud."},
            {"text": "It is the sepals, which enclosed the bud and are still "
                     "there.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s04",
        "band": "standard",
        "text": "A grain of pollen from a completely different species lands "
                "on a flower's stigma. What usually happens next?",
        "options": [
            {"text": "The stigma swells and the ovary begins to form a fruit "
                     "anyway.",
             "correct": False,
             "why": "An ovary swells because its ovules have been fertilised. "
                    "With no tube and no fusion there is nothing to set that "
                    "off."},
            {"text": "Nothing much: the stigma usually does not respond, and "
                     "no pollen tube grows.",
             "correct": True},
            {"text": "A tube grows and fertilises an ovule, giving a mixture "
                     "of the two species.",
             "correct": False,
             "why": "The stigma has to respond before the grain grows at all, "
                    "and for the wrong species it usually does not — so "
                    "nothing ever gets down the style."},
            {"text": "The flower counts as pollinated, so it will go on to "
                     "make seeds.",
             "correct": False,
             "why": "A grain has arrived, but arriving is not fusing. Seeds "
                    "form only from ovules that have actually been "
                    "fertilised, and nothing here reaches one."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-07-h01",
        "band": "harder",
        "text": "You cut a cucumber in half and find seeds in neat rows down "
                "the middle. Reading backwards, what does that tell you about "
                "the flower it came from?",
        "options": [
            {"text": "Its ovary held rows of seeds, which simply grew larger "
                     "as the cucumber grew.",
             "correct": False,
             "why": "An ovary holds ovules, not seeds. A seed does not exist "
                    "until an ovule has been fertilised — those rows were "
                    "rows of ovules first."},
            {"text": "Its ovary held rows of ovules, and each fertilised one "
                     "became a seed.",
             "correct": True},
            {"text": "The seeds formed from the pollen grains that landed on "
                     "its stigma.",
             "correct": False,
             "why": "A pollen grain supplies one thing: the male gamete "
                    "nucleus. The seed is the fertilised ovule, and the ovule "
                    "was inside the ovary all along."},
            {"text": "Each seed came from a separate small flower, and the "
                     "flowers fused together.",
             "correct": False,
             "why": "One flower, one ovary, one fruit. Everything inside that "
                    "cucumber came from the single ovary at the base of one "
                    "carpel."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h02",
        "band": "harder",
        "text": "A single poppy fruit can hold hundreds of seeds. What must "
                "have happened at that one flower?",
        "options": [
            {"text": "One pollen grain grew one tube and fertilised every "
                     "ovule in the ovary.",
             "correct": False,
             "why": "A pollen tube delivers one male gamete nucleus to one "
                    "ovule. Every ovule that is going to become a seed needs "
                    "a pollen tube of its own."},
            {"text": "One ovule was fertilised, then divided hundreds of "
                     "times to make the seeds.",
             "correct": False,
             "why": "The fertilised cell does divide — into the embryo inside "
                    "a single seed. One ovule is one seed, however many times "
                    "it divides."},
            {"text": "Hundreds of grains landed and fused with each other "
                     "there on the stigma.",
             "correct": False,
             "why": "Pollen grains do not fuse with one another, and nothing "
                    "at all fuses on the stigma. Fusion happens at an ovule, "
                    "at the bottom of the style."},
            {"text": "Hundreds of pollen grains landed and grew hundreds of "
                     "tubes down the style.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h03",
        "band": "harder",
        "text": "Two plants are pollinated on the same morning. In one the "
                "pollen tube reaches an ovule within hours; in an oak it can "
                "take months. A week later, what is true?",
        "options": [
            {"text": "The first has been fertilised; the oak has been "
                     "pollinated but not yet fertilised.",
             "correct": True},
            {"text": "Both have been fertilised, because both received pollen "
                     "on the same morning.",
             "correct": False,
             "why": "Receiving pollen is pollination, and that is only the "
                    "start. Fertilisation is a separate event at the far end "
                    "of the tube's journey, and the oak's tube is still "
                    "growing."},
            {"text": "Neither has been fertilised, because neither has a seed "
                     "you can see yet.",
             "correct": False,
             "why": "Fertilisation is two nuclei fusing inside an ovule — far "
                    "too small to see. The seed turns up afterwards, as a "
                    "result of it."},
            {"text": "Neither has been fertilised, because that only starts "
                     "once the ovary swells.",
             "correct": False,
             "why": "The ovary swells because fertilisation has already "
                    "happened. You are reading the effect as though it were "
                    "the event."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h04",
        "band": "harder",
        "text": "A grain of wheat looks like a single seed, but a biologist "
                "calls it a fruit. What makes it one?",
        "options": [
            {"text": "It is dry and hard rather than fleshy, and dry "
                     "structures are the fruits.",
             "correct": False,
             "why": "Fleshy or dry decides nothing — a plum is fleshy, a pea "
                    "pod is dry, and both are fruits. Where it came from is "
                    "the only test."},
            {"text": "The whole grain is the embryo plant, and an embryo "
                     "plant counts as a fruit.",
             "correct": False,
             "why": "The embryo is only one part of what is in there, packed "
                    "with a food store inside a coat. That package is the "
                    "seed; the fruit is the layer outside it."},
            {"text": "Its tough outer case developed from the ovary of the "
                     "flower, with the seed inside.",
             "correct": True},
            {"text": "A wheat plant makes hundreds of them, and only fruits "
                     "are produced in those numbers.",
             "correct": False,
             "why": "A poppy makes hundreds of seeds inside one fruit, so "
                    "numbers settle nothing. Only having come from an ovary "
                    "settles it."},
        ],
        "figure": None,
    },
]
