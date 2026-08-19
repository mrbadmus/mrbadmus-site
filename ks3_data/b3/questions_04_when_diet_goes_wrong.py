"""B3 lesson 04 — When diet goes wrong: twelve questions (MRB-269).

These probe the one thing the lesson is built to establish — that too much
energy, too little energy and a missing nutrient are three separate
imbalances, each with its own mechanism and its own remedy, and that a
deficiency is independent of how much energy a diet supplies. The distractors
are built from the lesson's three declared misconceptions: DIET-08
(malnourished means not having enough to eat), DIET-09 (deficiency diseases
are all in the past) and DIET-10 (you can tell what someone eats by looking at
them). Three more come from the lesson's own careful wording — that obesity
raises risk rather than delivering a verdict, that a long shortfall drags
deficiencies along behind it rather than excluding them, and that refeeding is
medical because speed itself is the danger. The `harder` band takes the rule
where the lesson only gestures: appearance as evidence, a plate that is
adequate at the mouth and a shortfall at the blood, the contrast between a
remedy that is instant and one that is slow, and Lind's correct result read
wrongly by the man who produced it.
"""

UNIT = "B3"
LESSON = "when-diet-goes-wrong"
LESSON_NUMBER = 4

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-e01",
        "band": "easier",
        "text": "A doctor writes “malnutrition” in a patient’s notes. What "
                "does that word tell you about the patient’s diet?",
        "options": [
            {"text": "That its balance is wrong — too much energy, too little "
                     "energy, or a nutrient missing.",
             "correct": True},
            {"text": "That they are not getting enough food, which is what "
                     "the word malnutrition means.",
             "correct": False,
             "why": "Malnourished means badly nourished, not under-nourished. "
                    "Going short of food is only one of the three things the "
                    "word can mean."},
            {"text": "That they are missing a vitamin, because that is the "
                     "only way a diet can go wrong.",
             "correct": False,
             "why": "A missing nutrient is one of the three imbalances. Too "
                    "much energy and too little energy are the other two, and "
                    "neither is a deficiency."},
            {"text": "That they eat very little, and would look thin if you "
                     "saw them standing there.",
             "correct": False,
             "why": "You cannot read a diet off an appearance. A patient "
                    "taking in 13 000 kJ a day can be severely malnourished."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e02",
        "band": "easier",
        "text": "Someone takes in more energy than they transfer, day after "
                "day, for years. What happens to the surplus?",
        "options": [
            {"text": "It is passed out of the body as waste, so none of it is "
                     "kept.",
             "correct": False,
             "why": "Energy the body does not transfer is not thrown away. It "
                    "is stored, as lipid in adipose tissue, and the store "
                    "keeps growing."},
            {"text": "It is built into extra muscle, which is why the body "
                     "mass rises.",
             "correct": False,
             "why": "A surplus is stored as lipid, not as muscle. Adipose "
                    "tissue is the tissue that holds it."},
            {"text": "It is stored as lipid in adipose tissue, and the store "
                     "keeps growing.",
             "correct": True},
            {"text": "It is all lost as heat, so a long surplus makes no "
                     "difference at all.",
             "correct": False,
             "why": "If it made no difference nobody’s mass would change. The "
                    "lipid store grows month after month, and its size is the "
                    "problem."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e03",
        "band": "easier",
        "text": "A person takes in far less energy than they transfer for "
                "several months. What does the body break down, and in what "
                "order?",
        "options": [
            {"text": "Its own protein first, keeping the lipid store back "
                     "until later.",
             "correct": False,
             "why": "It is the other way round. Lipid stores are broken down "
                    "first, and protein only once those are gone."},
            {"text": "Lipid stores first, then its own protein — muscle, "
                     "including heart muscle.",
             "correct": True},
            {"text": "Bone first, because the minerals held in it can be "
                     "released quickly.",
             "correct": False,
             "why": "Bone is not an energy store. The body draws on lipid "
                    "first and then on its own muscle protein."},
            {"text": "Only lipid, however long it lasts, so muscle is never "
                     "touched at all.",
             "correct": False,
             "why": "Once the lipid stores are gone the body breaks down "
                    "muscle — and that includes heart muscle."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e04",
        "band": "easier",
        "text": "A young child’s diet supplies enough energy but almost no "
                "vitamin D. Which condition follows?",
        "options": [
            {"text": "Scurvy, because a diet short of any one vitamin gives "
                     "the same illness.",
             "correct": False,
             "why": "Each missing nutrient has its own disease and its own "
                    "signs. No vitamin C gives scurvy; no vitamin D gives "
                    "rickets."},
            {"text": "Anaemia, with tiredness, breathlessness on stairs and "
                     "pale skin.",
             "correct": False,
             "why": "Anaemia is what follows when iron is missing. Vitamin D "
                    "missing gives rickets instead."},
            {"text": "Nothing at all, as long as the energy intake stays high "
                     "enough.",
             "correct": False,
             "why": "Energy cannot stand in for a nutrient. A deficiency can "
                    "occur at any level of energy intake."},
            {"text": "Rickets — the bones stay soft, because calcium cannot "
                     "be absorbed properly.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-04-s01",
        "band": "standard",
        "text": "“Scurvy and rickets are diseases out of history books. "
                "Nobody gets them now.” Which reply corrects this?",
        "options": [
            {"text": "They have gone from rich countries, and now appear only "
                     "in places where food is scarce.",
             "correct": False,
             "why": "Iron deficiency is the most common nutritional disorder "
                    "in the world, and it is not concentrated where food is "
                    "short. A deficiency is about one nutrient, not about how "
                    "much food there is."},
            {"text": "Both still appear in hospitals: a diet can look "
                     "ordinary and still miss one nutrient.",
             "correct": True},
            {"text": "They have gone, because modern food supplies every "
                     "nutrient that anybody needs.",
             "correct": False,
             "why": "Scurvy, rickets and severe iron deficiency all still "
                    "appear, and vitamin B12 deficiency is common enough to "
                    "be a routine blood test."},
            {"text": "They do still happen, but only in people who are not "
                     "eating enough food.",
             "correct": False,
             "why": "Rickets was widespread among children who were fed "
                    "enough. Quantity is not what a deficiency is about — the "
                    "missing nutrient is."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s02",
        "band": "standard",
        "text": "A student writes: “Obesity means you will get type 2 "
                "diabetes.” What is wrong with that sentence?",
        "options": [
            {"text": "Nothing is wrong with it — a long energy surplus always "
                     "ends in type 2 diabetes.",
             "correct": False,
             "why": "The lesson is careful here. Obesity raises the risk of "
                    "type 2 diabetes; it does not deliver it to everyone."},
            {"text": "Obesity raises the risk of heart disease only, and has "
                     "nothing to do with blood glucose.",
             "correct": False,
             "why": "Type 2 diabetes is one of the risks a long energy "
                    "surplus raises, alongside high blood pressure, heart "
                    "disease and joint damage."},
            {"text": "There is no link at all, because type 2 diabetes is a "
                     "deficiency disease.",
             "correct": False,
             "why": "A deficiency disease is caused by one nutrient being "
                    "missing. Type 2 diabetes is one of the risks raised by a "
                    "long-term energy surplus."},
            {"text": "Obesity raises the risk of type 2 diabetes, and a "
                     "raised risk is a probability, not a verdict.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s03",
        "band": "standard",
        "text": "A group of people have had far too little food for months. "
                "Doctors expect specific deficiency diseases as well as an "
                "energy shortfall. Why?",
        "options": [
            {"text": "Too little food means too little of every nutrient in "
                     "it, so deficiencies follow as well.",
             "correct": True},
            {"text": "Being hungry makes the body use up its vitamins far "
                     "faster than it normally would.",
             "correct": False,
             "why": "The vitamins were never eaten in the first place. What "
                    "is low is the amount arriving in the food."},
            {"text": "Once the lipid stores are gone, the body cannot hold on "
                     "to any nutrient at all.",
             "correct": False,
             "why": "Breaking down lipid is about energy. A deficiency "
                    "happens because a particular nutrient is not arriving in "
                    "the diet."},
            {"text": "They would not — a shortfall and a deficiency are "
                     "separate, and never occur in one person.",
             "correct": False,
             "why": "They occur together often, and being unwilling to name "
                    "both is exactly the mistake this lesson is built to "
                    "catch."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s04",
        "band": "standard",
        "text": "Someone who has been severely short of food for months is "
                "now being helped. Why is food restarted slowly and under "
                "medical supervision?",
        "options": [
            {"text": "Their stomach has shrunk, so a full meal would not "
                     "physically fit inside it.",
             "correct": False,
             "why": "The reason is not the size of the stomach. Restarting "
                    "food too fast after prolonged starvation is dangerous in "
                    "itself."},
            {"text": "Eating a lot quickly would swing them straight into a "
                     "long-term energy surplus.",
             "correct": False,
             "why": "A surplus takes months or years of intake above "
                    "requirement. The danger here is the speed of refeeding, "
                    "not a store of lipid."},
            {"text": "Refeeding too fast after prolonged starvation is itself "
                     "dangerous, so it is done carefully.",
             "correct": True},
            {"text": "Vitamins have to be supplied first, because food cannot "
                     "be digested at all without them.",
             "correct": False,
             "why": "There is no vitamins-first rule here. What matters is "
                    "that refeeding after a long shortfall is done slowly and "
                    "medically."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-h01",
        "band": "harder",
        "text": "Two people stand side by side and one is much larger than "
                "the other. A biologist is asked what this shows about their "
                "diets. What should they say?",
        "options": [
            {"text": "The larger one is taking in more energy than they "
                     "transfer, and the smaller one is not.",
             "correct": False,
             "why": "You cannot read an energy balance off an appearance. Two "
                    "people on the same diet can differ a great deal."},
            {"text": "The smaller one must be short of food, and the larger "
                     "one is eating too much of it.",
             "correct": False,
             "why": "This is the idea the lesson exists to attack. The three "
                    "imbalances are diagnosed from measurements and clinical "
                    "signs, not from how somebody looks."},
            {"text": "Nothing reliable — genetics, illness, medication, "
                     "activity and sleep all affect mass.",
             "correct": True},
            {"text": "The larger one is well nourished, so any deficiency "
                     "here must be in the smaller one.",
             "correct": False,
             "why": "A deficiency can occur at any level of energy intake. "
                    "Rickets was common in children who were fed enough."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h02",
        "band": "harder",
        "text": "A patient eats full, varied meals and their intake measures "
                "9500 kJ a day — right at requirement — yet they are losing "
                "mass and several vitamin levels are low. What has gone "
                "wrong?",
        "options": [
            {"text": "Absorption has failed: enough reaches the mouth, but "
                     "not enough gets into the blood.",
             "correct": True},
            {"text": "The intake figure must have been measured wrongly, "
                     "because mass cannot fall at requirement.",
             "correct": False,
             "why": "The figure measures what was eaten. What the body "
                    "actually receives depends on what is absorbed, and that "
                    "is a separate step."},
            {"text": "The meals must be the wrong kind, because only "
                     "carbohydrate can supply usable energy.",
             "correct": False,
             "why": "Three of the seven nutrients carry energy, not one. The "
                    "problem here is not which nutrients arrived but whether "
                    "they got through."},
            {"text": "A nutrient is missing from the plate, which is a "
                     "separate matter from the mass loss.",
             "correct": False,
             "why": "The plate is fine. Both the low vitamins and the falling "
                    "mass come from the same failure — what is eaten is not "
                    "being absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h03",
        "band": "harder",
        "text": "Treating a deficiency disease is often a fast, complete "
                "recovery. Shifting a long-term energy surplus is slow. What "
                "explains the difference?",
        "options": [
            {"text": "Deficiency diseases are milder illnesses, so they need "
                     "much less treatment to clear.",
             "correct": False,
             "why": "Severity is not the point — rickets and scurvy are "
                    "serious. Supplying the one missing nutrient restores "
                    "whatever it was needed for."},
            {"text": "An energy surplus cannot really be treated, so nothing "
                     "anybody does will shift it.",
             "correct": False,
             "why": "Any lasting change to the balance between intake and "
                    "activity shifts it. It is slow because the store took a "
                    "long time to build."},
            {"text": "Obesity is a moral failure and a deficiency is not, so "
                     "one of the two is easier to fix.",
             "correct": False,
             "why": "Obesity is not a moral failure, and the lesson says so "
                    "plainly. The difference is between supplying a nutrient "
                    "and shifting a store built over years."},
            {"text": "The missing nutrient can be supplied; a store built "
                     "over years needs lasting change.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h04",
        "band": "harder",
        "text": "Lind’s pair of scurvy patients given two oranges and a lemon "
                "recovered, yet he went on to recommend a boiled-down "
                "concentrate that did not work. What does that show?",
        "options": [
            {"text": "The original trial must have been wrong, because his "
                     "own remedy went on to fail.",
             "correct": False,
             "why": "The result stood — the citrus pair did recover. What "
                    "failed was his reading of why, and the boiling destroyed "
                    "the vitamin C."},
            {"text": "Producing a correct result and interpreting it "
                     "correctly are two different achievements.",
             "correct": True},
            {"text": "Boiling a juice down concentrates it, so the remedy "
                     "should have worked even better.",
             "correct": False,
             "why": "Boiling it down destroyed the vitamin C, which was the "
                    "thing doing the work. A concentrate of what is left is "
                    "still a concentrate of nothing."},
            {"text": "Scurvy is not caused by diet after all, since the "
                     "treatment for it proved unreliable.",
             "correct": False,
             "why": "Scurvy is the deficiency disease of missing vitamin C. "
                    "Nothing in Lind’s mistake retracts that."},
        ],
        "figure": None,
    },
]
