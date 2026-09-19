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

    # ── MRB-335 top-up ──────────────────────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b5-07-e05",
        "band": "easier",
        "text": "A seed has a tough coat around it. What two things are "
                "inside that coat?",
        "options": [
            {"text": "An ovule and an ovary", "correct": False,
             "why": "Those are parts of the flower, and both have already "
                    "become something else: the ovule became this seed, and "
                    "the ovary became the fruit around it."},
            {"text": "A pollen grain and a stigma", "correct": False,
             "why": "Both finished their work before fertilisation, and "
                    "neither ends up inside a seed. The grain grew a tube and "
                    "the stigma withered."},
            {"text": "An embryo plant and a food store", "correct": True},
            {"text": "A root and a flower, both already formed",
             "correct": False,
             "why": "The embryo has the beginnings of a root and a shoot, "
                    "folded up. A flower is built far later, by a plant that "
                    "has already grown."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e06",
        "band": "easier",
        "text": "Once the ovules of a flower have been fertilised, what "
                "happens to its petals and stamens?",
        "options": [
            {"text": "They wither and fall off the plant", "correct": True},
            {"text": "They swell and become the fruit", "correct": False,
             "why": "The fruit forms from the ovary. The petals and stamens "
                    "are no part of it and are abandoned."},
            {"text": "They close over the developing seeds to protect them",
             "correct": False,
             "why": "The sepals often stay and go on protecting — that is the "
                    "little green star on top of a strawberry. The petals do "
                    "not."},
            {"text": "They turn green and make food for the seeds",
             "correct": False,
             "why": "Each seed’s food store is built inside the seed itself. "
                    "The petals were an advertisement, and the advertising "
                    "stops."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b5-07-s05",
        "band": "standard",
        "text": "The food store inside a seed is called the endosperm. Most "
                "of a grain of wheat is endosperm, and white flour is very "
                "nearly pure endosperm. What is that tissue for?",
        "options": [
            {"text": "It attracts the animal that will carry the seed away",
             "correct": False,
             "why": "What attracts an animal is flesh on the outside of a "
                    "fruit. The endosperm is inside the seed coat, where "
                    "nothing can taste it."},
            {"text": "It protects the embryo from being crushed or eaten",
             "correct": False,
             "why": "Protection is the tough coat’s job. The store is food, "
                    "and a great deal of it is eaten every day."},
            {"text": "It makes the seed heavy enough to fall straight to the "
                     "ground", "correct": False,
             "why": "Plenty of seeds are built to be carried as far as "
                    "possible. Weight is a cost of carrying a store, not the "
                    "reason for having one."},
            {"text": "It feeds the young plant until it can make food for "
                     "itself", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s06",
        "band": "standard",
        "text": "A tomato flower is pollinated, but not one pollen tube ever "
                "reaches an ovule. Predict what the plant produces.",
        "options": [
            {"text": "Seeds, but no fruit around them", "correct": False,
             "why": "A seed is a fertilised ovule, so no fertilisation means "
                    "no seed either. Both depend on the same event."},
            {"text": "Neither seeds nor a fruit, because no fertilisation has "
                     "happened", "correct": True},
            {"text": "Seeds anyway, because the ovules were already in place "
                     "inside the ovary", "correct": False,
             "why": "An ovule holds a female gamete nucleus and nothing more "
                    "until a male nucleus fuses with it. Being in place is "
                    "not being fertilised."},
            {"text": "A fruit, because pollination alone is enough to start "
                     "the ovary swelling", "correct": False,
             "why": "Pollination is only delivery to the stigma. The ovary "
                    "swells after the ovules inside it have been fertilised, "
                    "not before."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b5-07-h05",
        "band": "harder",
        "text": "A pea pod is opened and holds nine full peas and three "
                "shrivelled empty spaces. Every ovule that becomes a seed "
                "needs its own pollen tube. What does that tell you?",
        "options": [
            {"text": "Nine ovules were present, and three peas were eaten "
                     "later", "correct": False,
             "why": "The empty spaces are where ovules sat. Nothing was "
                    "removed — three of the twelve simply never became "
                    "seeds."},
            {"text": "Twelve pollen grains landed, and nine of them were of "
                     "the right species", "correct": False,
             "why": "Far more than twelve grains land on a stigma, and one of "
                    "the wrong species usually gets no response at all. What "
                    "is counted here is tubes that arrived."},
            {"text": "The ovary held twelve ovules, and nine of them were "
                     "reached by a pollen tube", "correct": True},
            {"text": "One pollen tube arrived and fertilised nine of the "
                     "twelve ovules", "correct": False,
             "why": "One tube carries one male gamete nucleus and fertilises "
                    "one ovule. Nine seeds means nine tubes reached their "
                    "target."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h06",
        "band": "harder",
        "text": "Two nuclei travel down one pollen tube: one fuses with the "
                "egg nucleus and becomes the embryo, and the second helps "
                "build the seed’s food store. Why is it useful that the store "
                "is not started until then?",
        "options": [
            {"text": "A store is expensive, so an ovule that is never "
                     "fertilised costs the plant almost nothing",
             "correct": True},
            {"text": "The store would rot if it were built before the seed "
                     "coat existed", "correct": False,
             "why": "Plant tissue inside an ovary is not sitting there "
                    "rotting. The saving is in what never has to be built at "
                    "all."},
            {"text": "The store is made from the pollen grain, so it cannot "
                     "exist until the grain arrives", "correct": False,
             "why": "The store is built from the plant’s own materials. What "
                    "the pollen brings is a nucleus, not a food supply."},
            {"text": "The embryo needs the store at once, so the two have to "
                     "be made at the same moment", "correct": False,
             "why": "The embryo lives on the store later, when the seed "
                    "germinates. Timing the build to fertilisation is about "
                    "cost, not about urgency."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ─────────────────────────────────

    # ── easier ──────────────────────────────────────────────────────
    {
        "id": "b5-07-e07",
        "band": "easier",
        "text": "What is the function of the style in a flower?",
        "options": [
            {"text": "It is the stalk of tissue between the stigma and the "
                    "ovary, and the pollen tube grows down through it.", "correct": True},
            {"text": "It is the swollen part of a stamen where pollen grains "
                    "are produced and then released into the air or onto a "
                    "visiting insect.", "correct": False,
             "why": "That is the anther's job. The style holds no pollen at "
                    "all — it is purely the passage the tube grows through."},
            {"text": "It is the sticky pad that catches an arriving pollen "
                    "grain.", "correct": False,
             "why": "That is the stigma, at the very top of the style. The "
                    "style itself is not sticky and catches nothing."},
            {"text": "It is the chamber holding the ovules that will become "
                    "seeds.", "correct": False,
             "why": "That is the ovary, at the base of the style. The style "
                    "is a stalk with no ovules inside it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e08",
        "band": "easier",
        "text": "Once a pollen tube has delivered its nucleus to an ovule, "
                "what becomes of the tube itself?",
        "options": [
            {"text": "It becomes part of the developing embryo.",
             "correct": False,
             "why": "The embryo comes from the fused nuclei, not from the "
                    "tube's own tissue. The tube's job ends once delivery is "
                    "complete."},
            {"text": "It has done its job; it plays no further part in what "
                    "happens next.", "correct": True},
            {"text": "It grows on to fertilise a second ovule.",
             "correct": False,
             "why": "A single pollen tube delivers its one nucleus to one "
                    "ovule and stops there. Reaching a second ovule needs an "
                    "entirely separate tube."},
            {"text": "It turns into the tough coat around the new seed.",
             "correct": False,
             "why": "The seed coat forms from the ovule's own outer tissue. "
                    "The tube itself takes no further part once its nucleus "
                    "has arrived."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e09",
        "band": "easier",
        "text": "What is the ovary of a flower?",
        "options": [
            {"text": "The sticky pad at the top of the carpel that catches "
                    "pollen.", "correct": False,
             "why": "That is the stigma, at the opposite end of the carpel "
                    "from the ovary."},
            {"text": "The stalk of tissue that a pollen tube grows down "
                    "through.", "correct": False,
             "why": "That is the style. The ovary sits below the style and "
                    "holds the ovules, rather than being a stalk itself."},
            {"text": "The chamber at the base of the carpel that contains the "
                    "ovules.", "correct": True},
            {"text": "The tough coat that forms around a fertilised ovule.", "correct": False,
             "why": "That is the seed coat, and it forms around each "
                    "individual ovule, not around the ovary as a whole."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e10",
        "band": "easier",
        "text": "Immediately after a pollen grain lands on a stigma, roughly how "
                "far apart are the two gametes that must eventually fuse?",
        "options": [
            {"text": "Several centimetres.", "correct": True},
            {"text": "A fraction of a millimetre.", "correct": False,
             "why": "That badly understates the distance. The two gametes "
                    "start a whole style's length apart, which is "
                    "centimetres, not a fraction of a millimetre."},
            {"text": "Several metres.", "correct": False,
             "why": "That overstates it considerably for a single flower. A "
                    "style spans centimetres, not metres."},
            {"text": "They start already touching, on the stigma itself.", "correct": False,
             "why": "Nothing is touching at this point. The female gamete "
                    "sits inside an ovule, a whole style's length away from "
                    "the stigma."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e11",
        "band": "easier",
        "text": "What is a fruit, biologically?",
        "options": [
            {"text": "The structure that develops from the ovary of a flower "
                    "and contains the seeds.", "correct": True},
            {"text": "Any part of a plant that tastes sweet.", "correct": False,
             "why": "Sweetness is a kitchen test. A dry pea pod is not sweet "
                    "at all and is still, biologically, a fruit."},
            {"text": "The part of the flower that makes and releases pollen.", "correct": False,
             "why": "That is the anther. A fruit forms later, from the ovary, "
                    "and has nothing to do with pollen production."},
            {"text": "Whatever grows above ground once the flower has "
                    "finished.", "correct": False,
             "why": "Height decides nothing. What matters is whether the "
                    "structure developed from an ovary, wherever it happens "
                    "to grow."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e12",
        "band": "easier",
        "text": "Once the male and female gamete nuclei have fused, what do they "
                "become?",
        "options": [
            {"text": "The endosperm, the seed's food store.", "correct": False,
             "why": "The fused nuclei become the embryo. The endosperm forms "
                    "separately, from a second fusion involving other nuclei "
                    "in the ovule."},
            {"text": "The embryo plant, inside the developing seed.", "correct": True},
            {"text": "A second pollen tube, ready to fertilise another ovule.", "correct": False,
             "why": "A pollen tube is used up reaching one ovule and does not "
                    "turn into anything afterwards. The fused nuclei are the "
                    "start of a new plant."},
            {"text": "The tough coat around the outside of the seed.", "correct": False,
             "why": "The coat forms from tissue around the ovule, not from "
                    "the fused nuclei themselves."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e13",
        "band": "easier",
        "text": "Compared with the adult plant that produced it, what is true of a "
                "seed's ability to survive harsh conditions?",
        "options": [
            {"text": "A seed can often survive conditions that would kill "
                    "the parent plant.", "correct": True},
            {"text": "A seed is generally far more fragile than the parent "
                    "plant that produced it.", "correct": False,
             "why": "This is the wrong way round. A seed's tough coat "
                    "typically lets it survive conditions the adult plant "
                    "could not."},
            {"text": "A seed and its parent plant tolerate harsh conditions "
                    "equally well.", "correct": False,
             "why": "The seed's coat gives it a real advantage the adult "
                    "plant does not have — the two are not equally "
                    "tolerant."},
            {"text": "A seed can survive being boiled or frozen for as long "
                    "as anyone likes.", "correct": False,
             "why": "A seed's toughness has real limits. It is hardier than "
                    "the parent plant, not indestructible under any "
                    "treatment."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e14",
        "band": "easier",
        "text": "The little green points still attached under a ripe tomato are which "
                "flower part?",
        "options": [
            {"text": "The stigma, dried out after the pollen tubes grew "
                    "through it.", "correct": False,
             "why": "The stigma withers away along with the petals and "
                    "stamens. What remains on the tomato is lower down on the "
                    "flower — the sepals that enclosed the bud."},
            {"text": "Leftover petals that turned green as the fruit ripened.", "correct": False,
             "why": "Petals do not turn green — they are abandoned early and "
                    "drop off. Those points were green from the start."},
            {"text": "New leaves that grew once the flower had finished.", "correct": False,
             "why": "Nothing new grows there. Every part of that green star "
                    "was already present on the flower, before fertilisation "
                    "ever happened."},
            {"text": "The sepals.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e15",
        "band": "easier",
        "text": "A pollen tube may extend several centimetres from the stigma "
                "down to an ovule. Structurally, what is that tube?",
        "options": [
            {"text": "A single cell of the pollen grain, drawn out into a "
                     "long tube.", "correct": True},
            {"text": "A chain of many small cells, joined end to end down "
                     "the style.", "correct": False,
             "why": "It is not a chain of cells at all. One cell of the "
                    "grain simply extends, which is why the nucleus inside "
                    "never has to cross from one cell into another."},
            {"text": "A channel the style opens up for the grain to travel "
                     "along.", "correct": False,
             "why": "The style opens nothing. The tube is built by the "
                    "grain and has to force its own way through the style's "
                    "tissue to get anywhere."},
            {"text": "A thread of the stigma's tissue, pushed down ahead of "
                     "the grain.", "correct": False,
             "why": "The stigma contributes no tissue to the tube. Everything "
                    "the tube is made of came from the pollen grain sitting "
                    "on top of it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e16",
        "band": "easier",
        "text": "How many separate fusions of nuclei happen inside one ovule during "
                "fertilisation in a flowering plant?",
        "options": [
            {"text": "One.", "correct": False,
             "why": "A flowering plant fertilises twice with the same pollen "
                    "tube — one fusion makes the embryo, a second makes the "
                    "food-store tissue."},
            {"text": "Two.", "correct": True},
            {"text": "Three.", "correct": False,
             "why": "Only two nuclei travel down the pollen tube to fuse "
                    "inside the ovule, not three."},
            {"text": "None — the nuclei only need to touch, not fuse.", "correct": False,
             "why": "Fertilisation is defined as fusion. Touching without "
                    "fusing would not count as fertilisation at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e17",
        "band": "easier",
        "text": "What is the pollen tube's destination once it has grown down through "
                "the style?",
        "options": [
            {"text": "The stigma, back the way it came.", "correct": False,
             "why": "The tube grows away from the stigma, downward, not back "
                    "towards it."},
            {"text": "The anther of the same flower.", "correct": False,
             "why": "The anther is where the pollen grain started out. The "
                    "tube grows towards the ovary, in the opposite direction."},
            {"text": "An ovule, inside the ovary.", "correct": True},
            {"text": "The petals, to trigger them to wither.", "correct": False,
             "why": "Petals wither as a result of fertilisation happening "
                    "elsewhere. The tube itself never reaches them."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e18",
        "band": "easier",
        "text": "Which happens first in a flowering plant: pollination or "
                "fertilisation?",
        "options": [
            {"text": "Fertilisation.", "correct": False,
             "why": "Fertilisation cannot happen until a pollen grain has "
                    "already arrived on a stigma. Pollination has to come "
                    "first."},
            {"text": "They always happen at exactly the same moment.", "correct": False,
             "why": "They are separated by a delay — the time it takes a "
                    "pollen tube to grow down the style, which can be hours "
                    "or months."},
            {"text": "Neither comes first; a fruit forms independently of "
                    "both.", "correct": False,
             "why": "A fruit forms only after fertilisation, which in turn "
                    "only happens after pollination. Both events have to "
                    "occur, in that order."},
            {"text": "Pollination.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e19",
        "band": "easier",
        "text": "A flower's ovary has three ovules. How many separate pollen tubes "
                "are needed to fertilise all three?",
        "options": [
            {"text": "Three — one tube per ovule.", "correct": True},
            {"text": "One tube, which fertilises every ovule it passes.", "correct": False,
             "why": "A single pollen tube delivers one male gamete nucleus to "
                    "one ovule only. Fertilising three ovules needs three "
                    "tubes."},
            {"text": "Two tubes, since ovules can share.", "correct": False,
             "why": "An ovule does not share a fertilisation event with "
                    "another ovule. Each one needs its own tube."},
            {"text": "None — the ovary swells regardless of how many tubes "
                    "arrive.", "correct": False,
             "why": "The ovary only swells because ovules inside it have been "
                    "fertilised. With no tubes arriving, nothing would happen "
                    "at all."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e20",
        "band": "easier",
        "text": "A hazelnut is hard, dry and not at all sweet. Applying the "
                "biological definition, is it a fruit?",
        "options": [
            {"text": "No — a fruit has to be sweet or fleshy.", "correct": False,
             "why": "Sweetness and fleshiness are kitchen ideas. The "
                    "biological test is only where the structure came from."},
            {"text": "Yes — it developed from an ovary and contains a seed.", "correct": True},
            {"text": "No — nuts are a separate category from fruits.", "correct": False,
             "why": "A nut is simply a dry, hard fruit. It is not a separate "
                    "category from fruits at all."},
            {"text": "It cannot be decided without knowing how the hazelnut "
                    "tastes.", "correct": False,
             "why": "Taste settles nothing biologically. Only whether the "
                    "structure developed from an ovary and holds a seed "
                    "decides it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e21",
        "band": "easier",
        "text": "During fertilisation and seed formation, does the ovule itself "
                "physically travel anywhere?",
        "options": [
            {"text": "Yes — it moves down through the style to meet the "
                    "pollen tube halfway.", "correct": False,
             "why": "The ovule never leaves the ovary. It is the male "
                    "gamete nucleus that travels, all the way down to the "
                    "ovule."},
            {"text": "Yes — once fertilised, it travels out of the ovary "
                    "and into the base of the style.", "correct": False,
             "why": "A fertilised ovule stays exactly where it was. It "
                    "develops into a seed in place, without leaving the "
                    "ovary."},
            {"text": "No — it stays exactly where it was, and its own "
                    "tissue develops into the seed.", "correct": True},
            {"text": "Yes — it is carried to the tip of the ovary wall as "
                    "the fruit forms around it.", "correct": False,
             "why": "Nothing carries the ovule anywhere. The ovary wall "
                    "swells around it while the ovule stays fixed in its "
                    "own position."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e22",
        "band": "easier",
        "text": "Beyond simply forming from the ovary, what two jobs does a "
                "fruit do for the plant?",
        "options": [
            {"text": "It attracts pollinating insects to the flower and "
                    "holds pollen until they arrive.", "correct": False,
             "why": "A fruit only exists once the pollinating is over. "
                    "Attracting insects was the petals' job, and they have "
                    "withered by the time a fruit has formed."},
            {"text": "It makes the gametes and brings them together so that "
                    "fertilisation can happen.", "correct": False,
             "why": "Both gametes were made, and fused, before the fruit "
                    "existed. A fruit is what the ovary becomes afterwards, "
                    "not a structure fertilisation happens inside."},
            {"text": "It draws water up out of the soil and passes it in to "
                    "the ripening seeds.", "correct": False,
             "why": "Water is taken up by the roots. No part of a fruit "
                    "reaches the soil, and a picked fruit goes on ripening "
                    "with no soil anywhere near it."},
            {"text": "It protects the seeds inside it, and it gets them "
                    "carried away from the parent.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e23",
        "band": "easier",
        "text": "The peas found inside a pea pod developed from which flower "
                "structure?",
        "options": [
            {"text": "Ovules, inside the ovary.", "correct": True},
            {"text": "Pollen grains that landed on the pod's surface.", "correct": False,
             "why": "A pollen grain supplies only a male gamete nucleus. The "
                    "pea itself is a fertilised ovule, not a grain of pollen."},
            {"text": "The petals of the pea flower, rolled up small.", "correct": False,
             "why": "Petals wither and fall away. They play no part in "
                    "becoming the peas inside the pod."},
            {"text": "The stigma, once it had finished catching pollen.", "correct": False,
             "why": "The stigma is far from where the peas form. Peas develop "
                    "from ovules, deep inside the ovary."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e24",
        "band": "easier",
        "text": "A seed is cut open and the embryo plant inside it is examined "
                "closely. What is actually there?",
        "options": [
            {"text": "A single undivided cell, which only begins dividing "
                    "once the seed has germinated.", "correct": False,
             "why": "The dividing started long before the seed was ripe. By "
                    "the time a seed is shed the embryo is already many "
                    "cells, not one."},
            {"text": "A miniature plant with the beginnings of a root and a "
                    "shoot, folded up and waiting.", "correct": True},
            {"text": "A store of sugar, with no plant tissue in it at all "
                    "until germination begins.", "correct": False,
             "why": "That describes the food store beside the embryo, not "
                    "the embryo. The embryo is plant tissue, and it is "
                    "already built."},
            {"text": "A copy of the parent flower in miniature, with petals "
                    "and stamens already formed.", "correct": False,
             "why": "No flower parts are present. The embryo has a root end "
                    "and a shoot end and nothing else; flowers come much "
                    "later, from the grown plant."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e25",
        "band": "easier",
        "text": "If you count how many seeds are inside a ripe fruit, what are you "
                "actually counting?",
        "options": [
            {"text": "How many separate pollen grains landed on the "
                    "stigma in total.", "correct": False,
             "why": "Far more grains usually land than ever succeed. The "
                    "seed count reflects ovules fertilised, not grains that "
                    "simply arrived."},
            {"text": "How many ovules inside the original ovary were "
                    "fertilised.", "correct": True},
            {"text": "How many times the ovary itself divided as it "
                    "grew.", "correct": False,
             "why": "An ovary does not divide as it swells — it is one "
                    "structure enlarging around the ovules it already "
                    "held."},
            {"text": "How many pollen tubes failed to complete their "
                    "journey.", "correct": False,
             "why": "A failed tube leaves no seed behind at all. What you "
                    "are counting is the tubes that succeeded, not the ones "
                    "that failed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e26",
        "band": "easier",
        "text": "A flower's ovary contains four ovules and every one is fertilised. "
                "How many seeds will the resulting fruit contain?",
        "options": [
            {"text": "One, since the whole ovary becomes a single seed.", "correct": False,
             "why": "The ovary becomes the fruit, not a seed. Each individual "
                    "fertilised ovule becomes its own separate seed."},
            {"text": "Eight, because each ovule needs two pollen tubes.", "correct": False,
             "why": "One pollen tube fertilises one ovule. Four ovules need "
                    "four tubes and produce four seeds, not eight."},
            {"text": "It cannot be known without counting the pollen grains "
                    "that landed.", "correct": False,
             "why": "What decides the seed count is how many ovules were "
                    "actually fertilised, not how many grains simply arrived "
                    "on the stigma."},
            {"text": "Four.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e27",
        "band": "easier",
        "text": "Before fertilisation happens, what protects the ovules inside a "
                "flower?",
        "options": [
            {"text": "The wall of the ovary around them.", "correct": True},
            {"text": "The petals, which close over the top of the flower.", "correct": False,
             "why": "Petals are for attracting a pollinator and are not built "
                    "as protection. The ovules sit safely inside the ovary's "
                    "own wall."},
            {"text": "The pollen grains resting on the stigma.", "correct": False,
             "why": "Pollen grains have not even reached the ovary yet at "
                    "this stage, and offer no protection to anything inside "
                    "it."},
            {"text": "The seed coat, formed early to shield them.", "correct": False,
             "why": "A seed coat only forms after fertilisation. Before that, "
                    "the ovary wall is what encloses the ovules."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e28",
        "band": "easier",
        "text": "A seed's embryo plant and its food store are both wrapped in a "
                "tough outer coat. What is that coat there to do?",
        "options": [
            {"text": "Absorb minerals from the soil and pass them in to the "
                    "embryo before it grows.", "correct": False,
             "why": "Nothing is taken in through the coat. A seed lives on "
                    "the store packed inside it until it has roots of its "
                    "own to feed with."},
            {"text": "Protect the embryo and its food store until conditions "
                    "are right for growing.", "correct": True},
            {"text": "Hold the embryo and the food store apart so that the "
                    "two cannot mix together.", "correct": False,
             "why": "The coat is around both of them, not between them. "
                    "Keeping them apart would defeat the point, since the "
                    "embryo has to draw on the store."},
            {"text": "Feed the embryo while it waits, which is why the coat "
                    "is the thickest part.", "correct": False,
             "why": "The feeding is the food store's job. The coat is not "
                    "food at all, and in most seeds it is a thin layer "
                    "rather than the thickest part."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e29",
        "band": "easier",
        "text": "Precisely, what does the term 'pollination' mean?",
        "options": [
            {"text": "The fusion of a male gamete nucleus with a female "
                    "gamete nucleus.", "correct": False,
             "why": "That is fertilisation, a separate and later event. "
                    "Pollination is only the delivery that comes before it."},
            {"text": "The growth of a tube from a pollen grain down "
                    "through the style.", "correct": False,
             "why": "That is the second step of the process, which happens "
                    "after pollination is already complete."},
            {"text": "The transfer of pollen from an anther to a stigma.", "correct": True},
            {"text": "The development of a fertilised ovule into a seed.", "correct": False,
             "why": "That is a much later stage, happening well after both "
                    "pollination and fertilisation have already taken "
                    "place."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-e30",
        "band": "easier",
        "text": "An ovary has had every one of its ovules fertilised. What does its "
                "outer wall then turn into?",
        "options": [
            {"text": "It hardens into the seed coat around each embryo.", "correct": False,
             "why": "A seed's tough coat forms from the ovule's own outer "
                    "layer, not from the ovary wall around it."},
            {"text": "It shrinks and falls away with the petals.", "correct": False,
             "why": "The ovary wall is the one part of the flower that stays "
                    "and grows. Petals are what shrink and fall."},
            {"text": "It turns into new sepals to protect the flower.", "correct": False,
             "why": "Sepals were already present before fertilisation. The "
                    "ovary wall does not turn into a different structure — it "
                    "swells into the fruit."},
            {"text": "It swells and becomes the fruit.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────
    {
        "id": "b5-07-s07",
        "band": "standard",
        "text": "A pollen tube does not simply push its way between the style's cells "
                "— it visibly consumes tissue as it goes. What is happening?",
        "options": [
            {"text": "The tube secretes enzymes that digest a path through the "
                    "style's tissue as it grows.", "correct": True},
            {"text": "The style's own cells sense the approaching tube and "
                    "actively rearrange themselves out of its way as it "
                    "advances.", "correct": False,
             "why": "Style cells are stationary. The tube advances by "
                    "breaking a path through them, not by them stepping out "
                    "of its way."},
            {"text": "The tube grows through hollow channels the style already "
                    "has.", "correct": False,
             "why": "There is no ready-made channel. The tube has to make its "
                    "own way by digesting through solid tissue."},
            {"text": "The tube is simply much stronger than the surrounding "
                    "cells.", "correct": False,
             "why": "Strength alone would not get it through. It is digesting "
                    "the tissue chemically as it advances, not forcing "
                    "through it mechanically."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s08",
        "band": "standard",
        "text": "In a human, a whole sperm cell swims to an egg cell. In a flowering "
                "plant, what makes the equivalent journey to an ovule?",
        "options": [
            {"text": "A whole pollen grain, which detaches from the stigma and "
                    "travels down.", "correct": False,
             "why": "The grain itself stays put on the stigma. It extends a "
                    "tube, and only the nucleus inside that tube makes the "
                    "journey."},
            {"text": "Only the male gamete nucleus, carried inside a pollen "
                    "tube that grows to reach it.", "correct": True},
            {"text": "A single cell identical in structure to an animal sperm "
                    "cell.", "correct": False,
             "why": "Nothing swims in a flowering plant. What travels is a "
                    "bare nucleus, inside a tube the plant itself grows, not "
                    "a swimming cell."},
            {"text": "Nothing travels — the ovule's own nucleus moves to meet "
                    "the pollen instead.", "correct": False,
             "why": "The ovule's nucleus stays exactly where it is. "
                    "Everything that moves in this process moves downward, "
                    "towards it."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s09",
        "band": "standard",
        "text": "A student says the ovule's female nucleus moves up the style to meet "
                "the arriving pollen tube halfway. Why is this wrong?",
        "options": [
            {"text": "It is not wrong — an ovule meeting the pollen tube "
                    "halfway would let the whole process finish in half the "
                    "time it currently takes.", "correct": False,
             "why": "Nothing about this process is arranged to save effort. "
                    "The tube grows the full length of the style; the ovule's "
                    "nucleus never moves."},
            {"text": "It is wrong only because the tube is faster than the "
                    "nucleus could be.", "correct": False,
             "why": "Speed has nothing to do with it. The female nucleus is "
                    "fixed inside the ovule and simply never travels, "
                    "regardless of how fast anything else moves."},
            {"text": "The female nucleus does not move at all; the pollen tube "
                    "grows the entire distance down to it.", "correct": True},
            {"text": "It is wrong because nuclei cannot move through plant "
                    "tissue.", "correct": False,
             "why": "The male gamete nucleus does move, carried inside the "
                    "pollen tube. It is specifically the female nucleus that "
                    "stays put."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s10",
        "band": "standard",
        "text": "An ovary contains several ovules. Explain why the fruit that "
                "eventually forms is larger than any single seed inside it.",
        "options": [
            {"text": "The fruit continues absorbing extra nutrients and bulk "
                    "from the withering petals and stamens as they fall away "
                    "from the flower.", "correct": False,
             "why": "Withering petals and stamens are abandoned, not "
                    "absorbed. The fruit's size comes from the ovary wall "
                    "swelling around the ovules it already contained."},
            {"text": "Fruits simply grow faster than the seeds inside them do.", "correct": False,
             "why": "Growth rate is not the reason. The fruit is larger "
                    "because it is one structure built to contain several "
                    "separate seeds at once."},
            {"text": "Each seed contributes its own coat to build the "
                    "surrounding fruit.", "correct": False,
             "why": "A seed's coat stays around that one seed. The fruit wall "
                    "develops separately, from the ovary itself."},
            {"text": "The ovary, which becomes the fruit, is the chamber that "
                    "holds every one of the ovules that each become a seed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s11",
        "band": "standard",
        "text": "A gardener notices a tomato flower's ovary has already begun to "
                "swell, although no bee has been seen visiting it. What is the most "
                "likely explanation?",
        "options": [
            {"text": "A pollinator visited earlier without being noticed, and "
                    "fertilisation has already happened.", "correct": True},
            {"text": "The ovary has begun preparing itself in advance, ready "
                    "to swell rapidly the moment pollination eventually "
                    "happens.", "correct": False,
             "why": "An ovary does not swell in preparation. Swelling is a "
                    "response to ovules already having been fertilised, not "
                    "to an expectation."},
            {"text": "Watering the plant is enough to make the ovary swell on "
                    "its own.", "correct": False,
             "why": "Water supports growth generally, but it does not cause "
                    "an ovary specifically to swell into a fruit. Only "
                    "fertilisation does that."},
            {"text": "The petals must have already caused the swelling by "
                    "falling early.", "correct": False,
             "why": "Petals falling is itself a consequence of fertilisation, "
                    "not a cause of the ovary swelling. Both effects share "
                    "the same underlying cause."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s12",
        "band": "standard",
        "text": "An aubergine develops from a flower's ovary and contains many small "
                "seeds inside its flesh. Applying the biological definition, what is "
                "it?",
        "options": [
            {"text": "A vegetable, since it is usually cooked in savoury "
                    "dishes.", "correct": False,
             "why": "How a food is cooked settles nothing biologically. The "
                    "definition only asks where the structure came from."},
            {"text": "A fruit.", "correct": True},
            {"text": "A root, storing food for the plant underground.", "correct": False,
             "why": "An aubergine grows above ground from a flower's ovary. A "
                    "root has never been part of a flower at all."},
            {"text": "Neither, since it is too large to have come from one "
                    "small ovary.", "correct": False,
             "why": "Size is not part of the test. An ovary can swell a very "
                    "long way once its ovules have been fertilised."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s13",
        "band": "standard",
        "text": "A courgette is mostly water and is eaten savoury, like a vegetable. "
                "Why is it still, biologically, a fruit?",
        "options": [
            {"text": "Because anything that is mostly made of water "
                    "automatically counts as a fruit rather than a vegetable.", "correct": False,
             "why": "Water content decides nothing biologically. Plenty of "
                    "true vegetables, such as celery, are also mostly water."},
            {"text": "Because it is picked and eaten while still growing on "
                    "the plant.", "correct": False,
             "why": "When something is picked makes no difference to what it "
                    "is. The test is only whether it developed from an ovary."},
            {"text": "It developed from the ovary of a courgette flower, and "
                    "it contains seeds.", "correct": True},
            {"text": "It is not really a fruit — the classification is only a "
                    "technicality for cooks.", "correct": False,
             "why": "It is a genuine biological fruit, by the same test as a "
                    "tomato or a pea pod. The word simply means something "
                    "different to a cook than to a biologist."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s14",
        "band": "standard",
        "text": "Rhubarb is cooked with sugar and eaten sweet, much like a fruit. Why "
                "is it not one, biologically?",
        "options": [
            {"text": "It is not sweet enough on its own to count as a fruit.", "correct": False,
             "why": "Sweetness plays no part in the biological test. Plenty "
                    "of dry, unsweet structures — a pea pod, a hazelnut — are "
                    "still genuine fruits."},
            {"text": "It grows too quickly to have gone through fertilisation "
                    "first.", "correct": False,
             "why": "Growth speed is irrelevant. Rhubarb is excluded because "
                    "it is a stalk that never had a flower's ovary behind it "
                    "at all."},
            {"text": "It clearly contains no seeds that are visible to the "
                    "eye, so it cannot possibly be a fruit.", "correct": False,
             "why": "A lack of visible seeds is not the reason here, though "
                    "it is also true. The decisive fact is that rhubarb was "
                    "never part of a flower's ovary."},
            {"text": "It is a leaf stalk, and it never developed from an "
                    "ovary.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s15",
        "band": "standard",
        "text": "Broccoli is harvested and eaten as tightly closed flower buds, "
                "before they ever open. Why is it not classified as a fruit?",
        "options": [
            {"text": "No ovary in those buds has been fertilised yet, so no "
                    "fruit has had the chance to form.", "correct": True},
            {"text": "Flower buds are structures the plant builds only for "
                    "display, and are never actually connected to the "
                    "fruit-forming process.", "correct": False,
             "why": "A flower bud contains the very ovary that would become a "
                    "fruit — broccoli is simply eaten before that process "
                    "gets underway."},
            {"text": "Broccoli plants do not produce ovaries, only buds.", "correct": False,
             "why": "Every one of those buds is a tiny unopened flower, and "
                    "every flower has an ovary inside it, whether or not it "
                    "is ever fertilised."},
            {"text": "It is a vegetable because it grows above ground, unlike "
                    "a root.", "correct": False,
             "why": "Growing above ground settles nothing. The reason "
                    "broccoli is not a fruit is that fertilisation has not "
                    "happened, not where it grows."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s16",
        "band": "standard",
        "text": "A style is 8 mm long. A pollen tube grows down it at an average rate "
                "of 2 mm per hour. How long after pollination does fertilisation "
                "occur?",
        "options": [
            {"text": "2 hours.", "correct": False,
             "why": "That divides the rate by the length instead of the "
                    "length by the rate. 8 mm at 2 mm per hour takes four "
                    "hours, not two."},
            {"text": "4 hours.", "correct": True},
            {"text": "16 hours.", "correct": False,
             "why": "That multiplies the two numbers together instead of "
                    "dividing. 8 mm ÷ 2 mm per hour gives 4 hours."},
            {"text": "6 hours.", "correct": False,
             "why": "That does not match either number given. Dividing the 8 "
                    "mm style by the 2 mm-per-hour rate gives exactly 4 "
                    "hours."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s17",
        "band": "standard",
        "text": "An orange normally develops from an ovary with ten ovules, but a "
                "particular orange contains only six pips. How many of its ovules "
                "were not fertilised?",
        "options": [
            {"text": "Six.", "correct": False,
             "why": "Six is the number of pips that were fertilised, not the "
                    "number that failed. Ten minus six leaves four "
                    "unfertilised."},
            {"text": "Ten.", "correct": False,
             "why": "Ten is the total number of ovules the flower started "
                    "with, not the number that failed to be fertilised."},
            {"text": "Four.", "correct": True},
            {"text": "Sixteen.", "correct": False,
             "why": "That adds the two numbers instead of subtracting. Ten "
                    "ovules minus six fertilised ones leaves four, not "
                    "sixteen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s18",
        "band": "standard",
        "text": "Both a hazelnut shell and a pea pod are dry and hard rather than "
                "fleshy, yet both are classed as fruits. What test do they both pass?",
        "options": [
            {"text": "Both protect a seed from being eaten by birds.", "correct": False,
             "why": "Protection from being eaten is a side-effect, true of "
                    "many structures. It is not the test that decides whether "
                    "something is a fruit."},
            {"text": "Both were once soft and fleshy before drying out.", "correct": False,
             "why": "Neither one goes through a fleshy stage. A pea pod and a "
                    "hazelnut shell are dry throughout their development."},
            {"text": "Both grow directly from a stem rather than from a "
                    "flower.", "correct": False,
             "why": "Both grow from a flower's ovary specifically, not "
                    "directly from a stem. That shared origin is exactly why "
                    "both count as fruits."},
            {"text": "Both developed from the ovary of a flower and contain at "
                    "least one seed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s19",
        "band": "standard",
        "text": "Why does the male gamete nucleus need to travel inside a pollen "
                "tube, rather than moving through the style on its own?",
        "options": [
            {"text": "A bare nucleus could not survive or make its own way "
                    "through solid plant tissue; the tube grows the path and "
                    "carries it.", "correct": True},
            {"text": "A bare nucleus would simply be too heavy and too large "
                    "to push its own way through the dense, solid tissue of "
                    "the style unaided.", "correct": False,
             "why": "Weight is not the obstacle. A nucleus alone has no means "
                    "of moving through tissue or surviving the journey "
                    "without the tube around it."},
            {"text": "The tube exists only to stop the nucleus dividing too "
                    "early.", "correct": False,
             "why": "Preventing early division is not the tube's role. Its "
                    "role is making and protecting the physical path down to "
                    "an ovule."},
            {"text": "A pollen tube is needed only in species with an "
                    "unusually long style.", "correct": False,
             "why": "Every flowering plant grows a pollen tube, whatever the "
                    "length of its style, because the nucleus has no way to "
                    "travel without one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s20",
        "band": "standard",
        "text": "Petals and stamens wither after fertilisation, but sepals often do "
                "not. Suggest why sepals are more likely to stay useful afterwards.",
        "options": [
            {"text": "Sepals are built from a noticeably tougher tissue than "
                    "petals, which is simply too resistant to wither in the "
                    "same way.", "correct": False,
             "why": "Toughness is not the reason given. Sepals persist "
                    "because they still have a job protecting the fruit, not "
                    "because they are physically harder to wither."},
            {"text": "Sepals go on protecting the developing fruit, while "
                    "petals and stamens have already completed their roles.", "correct": True},
            {"text": "Sepals continue attracting insects even after "
                    "fertilisation.", "correct": False,
             "why": "Attracting insects is the petals' job, and it stops the "
                    "moment fertilisation happens. Sepals were never built to "
                    "attract anything."},
            {"text": "Petals and stamens fall to give the sepals more light to "
                    "grow in.", "correct": False,
             "why": "Nothing about this is arranged for the sepals' benefit. "
                    "Petals and stamens fall because their own jobs are "
                    "finished."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s21",
        "band": "standard",
        "text": "An oak flower's ovary usually contains six ovules, yet a ripe acorn "
                "contains only a single seed. What does this most likely mean?",
        "options": [
            {"text": "All six ovules were fertilised, but five of the "
                    "resulting seeds were later eaten.", "correct": False,
             "why": "Nothing about the acorn shows any evidence of seeds "
                    "having been removed. The simplest explanation is that "
                    "only one ovule was ever fertilised in the first place."},
            {"text": "The oak's ovary always contains only a single ovule, "
                    "whatever the usual figure suggests.", "correct": False,
             "why": "The question states the ovary usually holds six ovules. "
                    "An acorn with one seed means most of those six were not "
                    "fertilised, not that the ovary only ever had one."},
            {"text": "Only one of the six ovules was fertilised; the rest "
                    "failed to be fertilised at all.", "correct": True},
            {"text": "The six ovules fused together during fertilisation to "
                    "make one large seed.", "correct": False,
             "why": "Ovules do not fuse together. One seed from an ovary of "
                    "six ovules means five were never fertilised, not that "
                    "six of them combined into one."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s22",
        "band": "standard",
        "text": "Put these events into the order they actually happen: (1) the fruit "
                "forms, (2) pollen lands on the stigma, (3) the pollen tube grows "
                "down the style, (4) fertilisation occurs inside an ovule.",
        "options": [
            {"text": "2, 4, 3, 1.", "correct": False,
             "why": "This puts fertilisation before the tube has finished "
                    "growing. The tube must reach the ovule before anything "
                    "can fuse."},
            {"text": "1, 2, 3, 4.", "correct": False,
             "why": "This puts the fruit forming first, before pollination "
                    "has even happened, which reverses the true order "
                    "completely."},
            {"text": "3, 2, 4, 1.", "correct": False,
             "why": "This has the tube growing before any pollen has landed "
                    "on the stigma, which is impossible — landing has to come "
                    "first."},
            {"text": "2, 3, 4, 1.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s23",
        "band": "standard",
        "text": "Read this description: 'The ovary wall swells and the rest of the "
                "flower withers away.' Which named step of the process is being "
                "described?",
        "options": [
            {"text": "The fruit forms.", "correct": True},
            {"text": "Fertilisation.", "correct": False,
             "why": "Fertilisation is the fusion of the two nuclei, an "
                    "earlier and much smaller-scale event than the ovary "
                    "visibly swelling."},
            {"text": "Seeds form.", "correct": False,
             "why": "Seeds forming describes what happens to the individual "
                    "fertilised ovules, not to the ovary wall around all of "
                    "them."},
            {"text": "Pollen lands.", "correct": False,
             "why": "Pollen landing is the very first step, long before any "
                    "swelling of the ovary could possibly happen."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s24",
        "band": "standard",
        "text": "You cut open a plum and find just one large stone at its centre, "
                "surrounded by flesh. What can you conclude about the ovary it "
                "developed from?",
        "options": [
            {"text": "That ovary must have contained many ovules that fused "
                    "together into one stone.", "correct": False,
             "why": "Ovules do not fuse together. One stone means one ovule "
                    "was fertilised, not several combining into one."},
            {"text": "That ovary contained a single ovule, which was "
                    "fertilised to produce the one seed.", "correct": True},
            {"text": "That the plum's ovary was unusually small compared with "
                    "a pea pod's.", "correct": False,
             "why": "Size is not what a single stone tells you. It tells you "
                    "how many ovules were inside, not how large the ovary "
                    "itself was."},
            {"text": "That the stone's number is unrelated to how many ovules "
                    "were present.", "correct": False,
             "why": "The stone is directly the result of however many ovules "
                    "were fertilised. One stone means one ovule, not an "
                    "unrelated number."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s25",
        "band": "standard",
        "text": "A pea pod contains several peas in a row; a plum contains just one "
                "stone. What does that difference tell you about the two flowers' "
                "ovaries?",
        "options": [
            {"text": "The pea pod simply grew for longer than the plum did.", "correct": False,
             "why": "Growing time is not what decides seed number. It is set "
                    "by how many ovules the ovary contained in the first "
                    "place."},
            {"text": "The plum's single stone must be several fused seeds.", "correct": False,
             "why": "Seeds do not fuse together. A single stone means a "
                    "single ovule was fertilised, not several combined into "
                    "one."},
            {"text": "The pea flower's ovary held several ovules; the plum "
                    "flower's ovary held only one.", "correct": True},
            {"text": "Both ovaries held the same number of ovules, and only "
                    "one plum ovule survived.", "correct": False,
             "why": "There is no reason to assume the numbers started equal. "
                    "The simplest explanation is that the two ovaries "
                    "genuinely held different numbers of ovules."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s26",
        "band": "standard",
        "text": "A pollen tube grows 12 mm down a style in exactly 3 hours, at a "
                "constant rate. At that same rate, how long would a style twice "
                "as long take to be crossed?",
        "options": [
            {"text": "3 hours.", "correct": False,
             "why": "That assumes doubling the length changes nothing. At a "
                    "constant rate, doubling the distance doubles the time "
                    "needed."},
            {"text": "1.5 hours.", "correct": False,
             "why": "That halves the time instead of doubling it. A longer "
                    "style at the same rate takes more time, not less."},
            {"text": "6 hours.", "correct": True},
            {"text": "24 hours.", "correct": False,
             "why": "That treats the new length in millimetres as a number "
                    "of hours directly. The rate is 4 mm per hour, so 24 mm "
                    "takes 6 hours."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s27",
        "band": "standard",
        "text": "Two flowers of different species are pollinated at the same time. In "
                "one, fertilisation follows within two hours; in the other, not for "
                "three months. What does this variation depend on?",
        "options": [
            {"text": "How long each species' pollen tube takes to grow down "
                    "its own style to an ovule.", "correct": True},
            {"text": "How many ovules happen to be sitting inside each "
                    "flower's ovary, waiting to be reached by an arriving "
                    "pollen tube.", "correct": False,
             "why": "Ovule number changes how many seeds eventually form, not "
                    "how quickly any single tube grows down to one."},
            {"text": "How large each flower's petals are.", "correct": False,
             "why": "Petal size affects attracting a pollinator, before "
                    "pollination even happens. It plays no part in how fast a "
                    "tube grows afterwards."},
            {"text": "Whether the flower is pollinated by an insect or by "
                    "wind.", "correct": False,
             "why": "How the pollen arrived makes no difference once it has "
                    "landed — the timing depends on the tube's own growth "
                    "down that species' style."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s28",
        "band": "standard",
        "text": "A student sketches a whole pollen grain sliding down inside the "
                "style to reach an ovule. What is the actual mechanism?",
        "options": [
            {"text": "The whole grain does travel, just more slowly than the "
                    "sketch suggests.", "correct": False,
             "why": "The grain never leaves the stigma at all. It is the tube "
                    "it grows, and the nucleus inside that tube, that make "
                    "the journey."},
            {"text": "The grain stays on the stigma and extends a tube; only "
                    "the nucleus inside that tube travels.", "correct": True},
            {"text": "The grain dissolves and reforms once it reaches the "
                    "ovule.", "correct": False,
             "why": "Nothing about the grain dissolves. It stays intact on "
                    "the stigma while growing a tube, and only the nucleus is "
                    "delivered."},
            {"text": "The grain splits into several smaller grains that each "
                    "travel separately.", "correct": False,
             "why": "One grain grows one tube, carrying one nucleus to one "
                    "ovule. It does not split apart into multiple travelling "
                    "pieces."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s29",
        "band": "standard",
        "text": "Double fertilisation — one pollen tube delivering two nuclei that "
                "fuse separately, building both the embryo and its food store — "
                "is described as unusual in the living world. What makes it so "
                "distinctive?",
        "options": [
            {"text": "It is a rare case of two separate sperm cells "
                    "combining before either one reaches an egg.", "correct": False,
             "why": "That is not what double fertilisation is. Two nuclei "
                    "from one pollen tube fuse with different targets inside "
                    "one ovule, not two sperm cells combining with each "
                    "other."},
            {"text": "No other organism is known to fertilise in this "
                    "particular double way.", "correct": True},
            {"text": "It is a trait limited to wheat and its very close "
                    "relatives.", "correct": False,
             "why": "Every flowering plant does this, from a dandelion to "
                    "an oak, not wheat and its relatives alone."},
            {"text": "It happens in exactly the same way in animals, just "
                    "using different names for the same structures.", "correct": False,
             "why": "Animal fertilisation involves one sperm and one egg "
                    "fusing once. Nothing in an animal builds a food store "
                    "this way."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-s30",
        "band": "standard",
        "text": "A tomato's ovary swells into soft flesh; a hazelnut's ovary swells "
                "into a hard shell. Both processes start from exactly the same "
                "kind of flower structure. Explain what determines the very "
                "different textures that result.",
        "options": [
            {"text": "The number of ovules the ovary originally contained "
                    "decides whether the result is fleshy or hard.", "correct": False,
             "why": "Ovule number affects how many seeds form, not the "
                    "texture the surrounding ovary wall develops into."},
            {"text": "Fleshy fruits come from ovaries that were fertilised "
                    "far more thoroughly than ones that turn hard.", "correct": False,
             "why": "How thoroughly an ovary was fertilised affects seed "
                    "count, not whether the surrounding wall ends up fleshy "
                    "or hard."},
            {"text": "Ovaries pollinated by insects are the ones that "
                    "become fleshy; wind-pollinated ones turn hard or dry "
                    "instead.", "correct": False,
             "why": "How pollen arrived plays no part in what the ovary "
                    "wall later develops into. That depends on the species, "
                    "not the pollination method."},
            {"text": "The species itself: the same starting structure "
                    "develops differently depending on what kind of plant "
                    "it belongs to.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────
    {
        "id": "b5-07-h07",
        "band": "harder",
        "text": "A pollen tube has grown 5 mm down a style that is 14 mm long "
                "overall, growing steadily at 1.5 mm per hour. How much longer until "
                "it reaches the ovary?",
        "options": [
            {"text": "6 hours.", "correct": True},
            {"text": "9.3 hours.", "correct": False,
             "why": "That divides the whole style length by the rate, "
                    "ignoring the 5 mm the tube has already grown. Only the "
                    "remaining 9 mm needs dividing."},
            {"text": "3.3 hours.", "correct": False,
             "why": "That divides the 5 mm the tube has already grown by the "
                    "rate, which gives how long the FIRST part of the journey "
                    "took, not how much longer remains."},
            {"text": "13.5 hours.", "correct": False,
             "why": "That multiplies the remaining distance by the rate "
                    "instead of dividing. 9 mm ÷ 1.5 mm per hour is 6 hours."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h08",
        "band": "harder",
        "text": "In some orchid species, a pollen tube can take up to a year to reach "
                "an ovule after pollination. A student argues this means the flower "
                "must still be 'in the process of being pollinated' throughout that "
                "year. Evaluate this claim.",
        "options": [
            {"text": "The claim is correct, since pollination and "
                    "fertilisation in a species like this one are best "
                    "understood as one long, continuous event stretching "
                    "across the whole year.", "correct": False,
             "why": "They are two separate, clearly defined events — arrival "
                    "on the stigma, then fusion at an ovule — however long "
                    "the gap between them stretches."},
            {"text": "The claim is wrong: pollination finished the moment the "
                    "grain landed on the stigma; the year-long wait is "
                    "fertilisation still in progress.", "correct": True},
            {"text": "The claim is correct only for orchids, whose pollen "
                    "tubes behave differently from other plants'.", "correct": False,
             "why": "Every flowering plant's pollination finishes the instant "
                    "a grain lands. What varies between species is only how "
                    "long the following fertilisation stage takes."},
            {"text": "The claim cannot be evaluated without knowing exactly "
                    "how the orchid was pollinated.", "correct": False,
             "why": "The method of arrival — insect, wind or otherwise — "
                    "makes no difference to this claim. Pollination ends at "
                    "landing regardless of how the grain got there."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h09",
        "band": "harder",
        "text": "A sunflower head is not one flower but hundreds of tiny flowers "
                "packed together, each with its own ovary. A 'sunflower seed' from "
                "the edge of the head and one from the centre are each single fruits. "
                "What does this tell you about how they formed?",
        "options": [
            {"text": "All the sunflower seeds in one head formed from a single "
                    "shared ovary.", "correct": False,
             "why": "A sunflower head has hundreds of separate flowers, each "
                    "with its own ovary — there is no single shared ovary "
                    "producing them all."},
            {"text": "Only the flowers at the centre of the head are capable "
                    "of producing a seed.", "correct": False,
             "why": "Every one of the hundreds of tiny flowers in the head "
                    "has its own ovary and can be fertilised, wherever it "
                    "sits in the head."},
            {"text": "Each one formed from a separate flower's ovary, "
                    "fertilised independently of all the others in the head.", "correct": True},
            {"text": "The seeds all developed from ovules inside one enormous "
                    "flower.", "correct": False,
             "why": "A sunflower head only looks like one flower. It is "
                    "actually hundreds of separate small flowers, each "
                    "contributing one fruit of its own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h10",
        "band": "harder",
        "text": "A student claims that after fertilisation, 'a completely new fruit "
                "and a completely new set of seed coats grow from nothing, "
                "replacing the old flower.' Evaluate this claim against what "
                "actually becomes of the ovary and the ovules.",
        "options": [
            {"text": "The claim is correct: the ovary and ovules are shed "
                    "along with the petals and stamens, and the fruit and "
                    "seeds are freshly built to replace them.", "correct": False,
             "why": "The ovary and ovules are never shed. They are exactly "
                    "the structures that persist and develop into the fruit "
                    "and the seeds."},
            {"text": "The claim is wrong: the fruit and seed coats are the "
                    "ovary's and ovules' own existing tissue developing "
                    "further, not new growth from nothing.", "correct": True},
            {"text": "The claim is correct only for fleshy fruits like "
                    "tomatoes, not for dry ones like pea pods.", "correct": False,
             "why": "The same principle applies whatever the texture. A "
                    "dry pea pod's wall is just as much the ovary's own "
                    "existing tissue as a tomato's fleshy one."},
            {"text": "The claim is correct, since the fused nuclei that "
                    "form the embryo also build the fruit and seed coat "
                    "from scratch.", "correct": False,
             "why": "The fused nuclei build only the embryo. The fruit and "
                    "seed coat come from tissue the ovary and ovule already "
                    "had."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h11",
        "band": "harder",
        "text": "A gardener removes all the petals from a flower just before a bee "
                "would normally visit, but leaves the stamens, stigma and ovary "
                "untouched. Predict what happens to fruit formation, and why.",
        "options": [
            {"text": "Little changes for fruiting: petals only attract a "
                    "pollinator, so if pollen still reaches the stigma some "
                    "other way, fertilisation and fruit formation can still "
                    "occur.", "correct": True},
            {"text": "No fruit can possibly form, because the petals "
                    "themselves are needed to physically pick up and carry "
                    "each grain of pollen across to the stigma.", "correct": False,
             "why": "Petals never carry pollen. An insect, or the wind, does "
                    "that job — petals exist only to attract a pollinator in "
                    "the first place."},
            {"text": "No fruit can form, because petals themselves become part "
                    "of the ovary wall.", "correct": False,
             "why": "Petals are never incorporated into the ovary wall. "
                    "Removing them changes nothing about the ovary's own "
                    "ability to be fertilised."},
            {"text": "Fruit formation speeds up, since resources are freed "
                    "from building petals.", "correct": False,
             "why": "Timing of fertilisation depends on the pollen tube's "
                    "growth, not on resources saved elsewhere in the flower."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h12",
        "band": "harder",
        "text": "A sunflower head has 800 individual flowers, and 640 of them are "
                "successfully fertilised. Each fertilised flower produces exactly one "
                "fruit. How many of the 800 flowers failed to produce a fruit?",
        "options": [
            {"text": "640.", "correct": False,
             "why": "640 is the number that succeeded, not the number that "
                    "failed. 800 minus 640 leaves 160 unsuccessful."},
            {"text": "160.", "correct": True},
            {"text": "800.", "correct": False,
             "why": "800 is the total number of flowers in the head, not the "
                    "number that failed to be fertilised."},
            {"text": "1440.", "correct": False,
             "why": "That adds the two numbers together instead of "
                    "subtracting. 800 minus 640 gives 160, not 1440."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h13",
        "band": "harder",
        "text": "A student claims that a flower with larger petals will always "
                "produce more seeds than one with smaller petals. Evaluate this "
                "claim.",
        "options": [
            {"text": "The claim is correct, since flowers with noticeably "
                    "larger and more colourful petals reliably attract far "
                    "more pollinators, and therefore many more pollen tubes.", "correct": False,
             "why": "More visits could mean more grains land, but seed number "
                    "is still capped by how many ovules the ovary actually "
                    "contains, whatever the petal size."},
            {"text": "The claim is correct, because larger petals grow into a "
                    "larger ovary.", "correct": False,
             "why": "Petals and the ovary are separate structures that "
                    "develop independently. Petal size has no effect on how "
                    "many ovules an ovary holds."},
            {"text": "The claim is unsupported: seed number depends on how "
                    "many ovules are in the ovary and how many are "
                    "fertilised, not on petal size.", "correct": True},
            {"text": "The claim cannot be assessed without knowing the exact "
                    "species involved.", "correct": False,
             "why": "The reasoning fails for any species: seed number is set "
                    "by ovule number and fertilisation success, never by "
                    "petal size, whichever plant is being discussed."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h14",
        "band": "harder",
        "text": "A flower's ovary starts with 900 ovules. Of these, 720 are reached "
                "in time by their own pollen tube and go on to be fertilised. What "
                "percentage of the ovary's ovules failed to be fertilised?",
        "options": [
            {"text": "80%.", "correct": False,
             "why": "That is the success rate, not the failure rate. 720 "
                    "out of 900 succeeded, leaving 20% that failed."},
            {"text": "2%.", "correct": False,
             "why": "That has the decimal point in the wrong place. 180 "
                    "out of 900 is 0.2, which is 20%, not 2%."},
            {"text": "20%.", "correct": True},
            {"text": "180%.", "correct": False,
             "why": "That uses the raw count of 180 directly as a "
                    "percentage, without ever dividing it by the total of "
                    "900."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h15",
        "band": "harder",
        "text": "A plum is fleshy and takes considerable resources to build around "
                "its single seed; a pea pod is dry and papery around several. Both "
                "are fruits, developed the same way. What is the one thing both "
                "processes have in common, whatever the fruit's eventual texture?",
        "options": [
            {"text": "In both cases the ovary wall swells around the "
                    "fertilised ovule or ovules, after fertilisation and not "
                    "before.", "correct": True},
            {"text": "Both fruits are built using exactly the same overall "
                    "amount of the plant's stored resources, whatever their "
                    "eventual size or texture turns out to be.", "correct": False,
             "why": "A fleshy fruit and a dry one clearly cost different "
                    "amounts to build. What they share is not resource cost "
                    "but the timing and origin of the swelling."},
            {"text": "Both fruits form directly from the stigma rather than "
                    "from the ovary.", "correct": False,
             "why": "Neither forms from the stigma. Both, fleshy or dry, form "
                    "from the ovary wall around the fertilised ovule or "
                    "ovules."},
            {"text": "Both fruits are fully formed before fertilisation even "
                    "takes place.", "correct": False,
             "why": "Neither is. In both cases the ovary only begins swelling "
                    "once its ovules have actually been fertilised."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h16",
        "band": "harder",
        "text": "A researcher finds a swollen, fruit-like structure on a plant whose "
                "flowers were never visited by any pollinator and were kept isolated "
                "under fine mesh throughout. What does the swelling most likely "
                "indicate?",
        "options": [
            {"text": "That pollination on its own, entirely without any "
                    "accompanying fertilisation ever taking place, is "
                    "apparently enough by itself to cause this kind of "
                    "swelling.", "correct": False,
             "why": "In the ordinary process, swelling follows "
                    "fertilisation specifically, not "
                    "pollination alone — and here pollination could not even "
                    "have occurred."},
            {"text": "That fertilisation has, unusually, not been the cause "
                    "here — some other explanation is needed, since normal "
                    "fruit formation requires it.", "correct": True},
            {"text": "That wind must have carried pollen through the mesh "
                    "unnoticed, causing fertilisation as normal.", "correct": False,
             "why": "Fine mesh is specifically used to rule this out. The "
                    "swelling has to be explained some other way, not by "
                    "assuming an undetected pollination event."},
            {"text": "That the plant's petals caused the swelling by "
                    "themselves as they withered.", "correct": False,
             "why": "Withering petals are a separate effect of fertilisation, "
                    "not a cause of the ovary swelling. They could not "
                    "produce this result on their own."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h17",
        "band": "harder",
        "text": "Two students explain why a fertilised ovule becomes a seed rather "
                "than staying an ovule. Student A says it is because the pollen tube "
                "physically becomes part of it. Student B says it is because the "
                "fused nuclei inside it divide to build an embryo, food store and "
                "coat. Who is right?",
        "options": [
            {"text": "Student A — without the tube's tissue, nothing new could "
                    "be built inside the ovule.", "correct": False,
             "why": "The tube's role ends once it has delivered the male "
                    "nucleus. Everything built afterwards comes from the "
                    "ovule's own tissue and the fused nuclei, not from the "
                    "tube."},
            {"text": "Both are right, since the tube and the fused nuclei work "
                    "together afterwards.", "correct": False,
             "why": "The tube plays no further part after delivery. Building "
                    "the seed is entirely the fused nuclei's and the ovule's "
                    "own doing."},
            {"text": "Student B — the pollen tube is used up delivering the "
                    "nucleus and takes no further part.", "correct": True},
            {"text": "Neither is right, since a seed forms from the ovary "
                    "rather than the ovule.", "correct": False,
             "why": "The ovary becomes the fruit, not the seed. Each "
                    "individual seed forms from its own fertilised ovule, "
                    "exactly as Student B describes."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h18",
        "band": "harder",
        "text": "In some plant species, a pollen tube stops growing partway down the "
                "style if it detects that the pollen came from the same plant. "
                "Predict what happens to that flower's ovules as a result.",
        "options": [
            {"text": "The ovules fertilise themselves without needing a pollen "
                    "tube at all.", "correct": False,
             "why": "Nothing in this process allows an ovule to fertilise "
                    "itself. Without a tube reaching it, an ovule simply "
                    "remains unfertilised."},
            {"text": "The stigma absorbs the stalled pollen tube directly, "
                    "achieving fertilisation anyway.", "correct": False,
             "why": "A stalled tube delivers nothing. Fertilisation can only "
                    "happen at the far end of a tube that actually completes "
                    "its journey to an ovule."},
            {"text": "Fertilisation still happens, just after a longer delay "
                    "than usual.", "correct": False,
             "why": "A tube that has stopped growing permanently will never "
                    "reach an ovule. This is prevention, not merely a longer "
                    "wait."},
            {"text": "Those ovules are not reached by any tube and so are "
                    "never fertilised, whatever pollen originally landed on "
                    "the stigma.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h19",
        "band": "harder",
        "text": "A pollen tube grows 3 mm per hour through the first 6 mm of a style, "
                "then slows to 1 mm per hour for the remaining 4 mm. How long does "
                "the whole journey down the style take?",
        "options": [
            {"text": "6 hours.", "correct": True},
            {"text": "3.3 hours.", "correct": False,
             "why": "That treats the whole 10 mm style as growing at the "
                    "faster rate throughout, ignoring that the second half is "
                    "slower."},
            {"text": "10 hours.", "correct": False,
             "why": "The correct method is 6 mm ÷ 3 mm/h (2 h) plus 4 mm ÷ 1 "
                    "mm/h (4 h), giving 6 hours total, not 10."},
            {"text": "2 hours.", "correct": False,
             "why": "That accounts for only the first, faster segment of the "
                    "journey and ignores the remaining 4 mm travelled at the "
                    "slower rate."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h20",
        "band": "harder",
        "text": "Species A's pollen tube grows at 4 mm per hour through a 20 mm "
                "style. Species B's pollen tube grows at 2.5 mm per hour through a "
                "15 mm style. Which species completes fertilisation faster after "
                "pollination, and by how much?",
        "options": [
            {"text": "Species A, by 1 hour.", "correct": True},
            {"text": "Species B, by 1 hour.", "correct": False,
             "why": "That has the two species swapped. Species A takes 5 "
                    "hours and species B takes 6 hours, so A finishes "
                    "first."},
            {"text": "Species A, by 5 hours.", "correct": False,
             "why": "That uses species A's own total time as the gap "
                    "between them. The actual difference between 5 hours "
                    "and 6 hours is 1 hour."},
            {"text": "They finish at exactly the same time.", "correct": False,
             "why": "The two times are not equal: 20 mm at 4 mm per hour "
                    "is 5 hours, while 15 mm at 2.5 mm per hour is 6 "
                    "hours."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h21",
        "band": "harder",
        "text": "Imagine a mutant flowering plant that could not perform the second "
                "fusion of double fertilisation, so no endosperm ever formed. Predict "
                "the most likely consequence for its seeds.",
        "options": [
            {"text": "The seeds would still form in a perfectly normal way "
                    "overall, since it is really only the first of the two "
                    "fusions that actually matters for making a seed at all.", "correct": False,
             "why": "The endosperm is the seed's food store, built by the "
                    "second fusion. Losing it would seriously harm the "
                    "embryo's chances, not leave the seed unaffected."},
            {"text": "The seed coat would fail to form, since it depends on "
                    "the second fusion too.", "correct": False,
             "why": "The coat forms from the ovule's outer tissue, "
                    "independent of either fusion. It is specifically the "
                    "food store that the second fusion builds."},
            {"text": "The embryo inside each seed would have no food store to "
                    "draw on, and would be far less likely to survive until "
                    "it could feed itself.", "correct": True},
            {"text": "The plant would simply produce more ovules to compensate "
                    "for the missing endosperm.", "correct": False,
             "why": "Ovule number is set well before fertilisation and would "
                    "not respond to a missing food store. The consequence "
                    "falls on the embryos already forming."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h22",
        "band": "harder",
        "text": "A student claims that a plant with a longer style will always take "
                "longer to be fertilised than one with a shorter style. Evaluate this "
                "claim.",
        "options": [
            {"text": "The claim is definitely correct, since distance is the "
                    "only factor that affects timing.", "correct": False,
             "why": "Distance is one factor, but the tube's growth rate "
                    "matters just as much — a longer style can still be "
                    "crossed faster if the tube grows quickly enough."},
            {"text": "The claim is definitely wrong, since style length makes "
                    "no difference to timing at all.", "correct": False,
             "why": "Length does affect timing, all else being equal. The "
                    "claim's error is treating length as the only factor, not "
                    "that it is irrelevant."},
            {"text": "The claim can only be tested by comparing two flowers of "
                    "the same species.", "correct": False,
             "why": "The claim is a general one about style length and growth "
                    "rate together, and can be evaluated in principle without "
                    "needing two specific flowers to compare."},
            {"text": "It is not necessarily true: fertilisation time depends "
                    "on both the style's length and the pollen tube's growth "
                    "rate, and a longer style with a fast tube could still "
                    "finish sooner than a short style with a very slow one.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h23",
        "band": "harder",
        "text": "A tomato keeps its sepals attached as a green star long after the "
                "fruit ripens; many other fruiting plants shed their sepals along "
                "with the petals. What does this variation suggest about the sepals' "
                "role?",
        "options": [
            {"text": "Sepals' usefulness after fertilisation differs between "
                    "species, so whether they are kept or shed depends on "
                    "what continued protection is worth to that plant.", "correct": True},
            {"text": "It suggests that sepals must only ever have one single "
                    "fixed role that stays exactly the same across every "
                    "flowering species there is, whatever that species needs.", "correct": False,
             "why": "The variation itself is evidence against one fixed "
                    "universal role — different species clearly get different "
                    "value out of keeping their sepals."},
            {"text": "It suggests the tomato's sepals are a leftover mistake "
                    "with no remaining function.", "correct": False,
             "why": "A structure this consistently retained across so many "
                    "tomato fruits is more plausibly still doing a job than "
                    "simply being a leftover error."},
            {"text": "It suggests only fleshy fruits ever keep their sepals, "
                    "and dry fruits never do.", "correct": False,
             "why": "This is too broad a rule to draw from one comparison, "
                    "and plenty of dry fruits also retain sepals or other bud "
                    "coverings after fertilisation."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h24",
        "band": "harder",
        "text": "An unfamiliar fruit is cut open and shows five separate chambers "
                "arranged around its centre, each containing exactly two seeds. What "
                "does this tell you about the flower's ovary?",
        "options": [
            {"text": "That this fruit actually began life as ten completely "
                    "separate small ovaries, which somehow fused together "
                    "only after fertilisation to make one single fruit.", "correct": False,
             "why": "Ovaries do not fuse together after the fact. The "
                    "simplest explanation is one ovary that was already "
                    "divided into five sections before fertilisation."},
            {"text": "That ovary was divided into five sections, each holding "
                    "two ovules that were separately fertilised.", "correct": True},
            {"text": "That only one ovule was originally present, and it "
                    "divided into ten seeds.", "correct": False,
             "why": "A single fertilised ovule produces a single seed. Ten "
                    "seeds mean ten separately fertilised ovules were present "
                    "from the start."},
            {"text": "That the fruit is not a true fruit, since it has more "
                    "than one chamber.", "correct": False,
             "why": "Having several internal chambers is common in genuine "
                    "fruits — it reflects how many sections the original "
                    "ovary was divided into, nothing more."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h25",
        "band": "harder",
        "text": "A botanist finds a fruit still carrying its sepals, its stamens "
                "already fallen, and its ovary wall clearly swollen. Put these three "
                "observations in the order the underlying events must have happened.",
        "options": [
            {"text": "The sepals fell first, then the stamens, and finally the "
                    "ovary swelled without fertilisation.", "correct": False,
             "why": "This fruit's sepals have not fallen — they are still "
                    "attached. The ovary's swelling also depends on "
                    "fertilisation, which cannot be skipped."},
            {"text": "The ovary swelled first, which caused the stamens to "
                    "fall and the sepals to be released.", "correct": False,
             "why": "Swelling is an effect of fertilisation, not a cause of "
                    "anything else. The stamens fall because their own job is "
                    "finished, not because the ovary swelled."},
            {"text": "Pollen landed and grew a tube; fertilisation then "
                    "happened, triggering both the stamens to fall and the "
                    "ovary to swell, while the sepals simply stayed in place "
                    "throughout.", "correct": True},
            {"text": "All three observations happened at exactly the same "
                    "instant.", "correct": False,
             "why": "These are linked outcomes of one underlying event — "
                    "fertilisation — but nothing here demonstrates that they "
                    "occurred at literally the same instant."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h26",
        "band": "harder",
        "text": "A gardener removes every stamen from a flower before any pollen is "
                "released, and no other flower nearby can supply pollen either. "
                "The petals, stigma and ovary are left untouched. Predict what "
                "happens to fruit formation, and why.",
        "options": [
            {"text": "Fruit formation is unaffected: the ovary and stigma "
                    "are the only two structures a flower needs for "
                    "fertilisation to succeed.", "correct": False,
             "why": "Without an anther anywhere to supply it, the stigma "
                    "has no pollen to receive at all. Fertilisation cannot "
                    "begin."},
            {"text": "The flower will pollinate itself automatically, "
                    "since the stigma and ovary are both still present and "
                    "undamaged.", "correct": False,
             "why": "Self-pollination still needs pollen from a stamen "
                    "somewhere. Removing every stamen removes that source "
                    "completely."},
            {"text": "Fruit formation will be delayed but will still "
                    "eventually succeed once the plant regrows its "
                    "stamens.", "correct": False,
             "why": "A flower does not regrow stamens once they are "
                    "removed. That flower's one chance at pollination is "
                    "gone for good."},
            {"text": "No fruit will form: with no pollen source left, the "
                    "stigma never receives any pollen, so pollination "
                    "cannot happen.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h27",
        "band": "harder",
        "text": "A student concludes 'a structure can only be called a fruit if at "
                "least some part of it could plausibly be eaten sweet.' Evaluate this "
                "rule against a gorse pod, a wheat grain and a hazelnut.",
        "options": [
            {"text": "The rule fails all three: none of them is remotely "
                    "sweet, yet all three developed from an ovary and are "
                    "genuine fruits.", "correct": True},
            {"text": "The rule holds for the wheat grain and the hazelnut, but "
                    "not the gorse pod.", "correct": False,
             "why": "None of the three is sweet in any part. The wheat grain "
                    "and hazelnut fail the rule exactly as the gorse pod "
                    "does."},
            {"text": "The rule holds for all three, since each contains a "
                    "trace of natural sugar somewhere inside it.", "correct": False,
             "why": "A trace of sugar is not what the rule is testing, and "
                    "dry fruits like these are not classed as fruits for any "
                    "sweetness reason — only for developing from an ovary."},
            {"text": "The rule cannot be tested on any of the three, since "
                    "none is normally eaten by humans.", "correct": False,
             "why": "Whether humans eat something has no bearing on testing "
                    "this rule. The three specimens can be judged against it "
                    "directly, by taste and origin alone."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h28",
        "band": "harder",
        "text": "A style is 10 mm long. Pollination happens at 9:00 am and the pollen "
                "tube grows at a constant 2.5 mm per hour. At what time does "
                "fertilisation occur?",
        "options": [
            {"text": "11:30 am.", "correct": False,
             "why": "That uses half the correct travel time. 10 mm at 2.5 mm "
                    "per hour takes 4 hours, reaching 1:00 pm, not 11:30 am."},
            {"text": "1:00 pm.", "correct": True},
            {"text": "9:25 am.", "correct": False,
             "why": "That treats 2.5 mm per hour as a total time in minutes "
                    "rather than a rate. The correct working is 10 ÷ 2.5 = 4 "
                    "hours added to 9:00 am."},
            {"text": "7:00 pm.", "correct": False,
             "why": "That adds 10 hours instead of 4. Dividing the 10 mm "
                    "style by the 2.5 mm-per-hour rate gives 4 hours, "
                    "reaching 1:00 pm."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h29",
        "band": "harder",
        "text": "A student proposes redefining a fruit as 'anything containing more "
                "than one seed', to avoid counting a single-seeded plum as a fruit by "
                "mistake. Evaluate this proposed definition.",
        "options": [
            {"text": "It works reasonably well overall, since the great "
                    "majority of fruits that exist genuinely do contain "
                    "several separate seeds rather than only one.", "correct": False,
             "why": "That most fruits happen to have several seeds does not "
                    "make seed count the correct test — the proposal would "
                    "wrongly exclude every single-seeded fruit."},
            {"text": "It is an improvement, because seed count is easier to "
                    "check than tracing an ovary.", "correct": False,
             "why": "Ease of checking does not make a definition correct. A "
                    "definition that misclassifies plums, acorns and wheat "
                    "grains has failed, however convenient it seems."},
            {"text": "It fails immediately: a plum, an acorn and a wheat grain "
                    "each contain only one seed and are all genuine fruits by "
                    "the real definition.", "correct": True},
            {"text": "It only fails for fleshy fruits like the plum, not for "
                    "dry ones like an acorn.", "correct": False,
             "why": "It fails for both. An acorn and a wheat grain are just "
                    "as single-seeded as a plum, and the proposed rule would "
                    "wrongly exclude all three."},
        ],
        "figure": None,
    },
    {
        "id": "b5-07-h30",
        "band": "harder",
        "text": "Explain why a biologist studying an ovary that has already swollen "
                "into a fruit can be completely certain that pollination also "
                "happened earlier, without needing to have observed either event "
                "directly.",
        "options": [
            {"text": "Swelling and pollination are really the same event, "
                    "described at two different scales.", "correct": False,
             "why": "They are two clearly distinct events separated by "
                    "however long the pollen tube takes to grow. Swelling is "
                    "a much later consequence, not another name for "
                    "pollination."},
            {"text": "Fruit formation could equally well have happened without "
                    "any pollination at all.", "correct": False,
             "why": "Fruit formation depends on fertilisation, which itself "
                    "depends on pollination having already delivered the "
                    "pollen. It cannot be skipped."},
            {"text": "The biologist would need to check the seeds inside "
                    "before concluding pollination happened.", "correct": False,
             "why": "The swollen ovary alone is already sufficient evidence, "
                    "given the causal chain, without needing to open it and "
                    "inspect any seeds."},
            {"text": "An ovary only swells into a fruit as a result of "
                    "fertilisation, and fertilisation itself cannot happen "
                    "without pollination having occurred first, so the fruit "
                    "is evidence for both.", "correct": True},
        ],
        "figure": None,
    },
]
