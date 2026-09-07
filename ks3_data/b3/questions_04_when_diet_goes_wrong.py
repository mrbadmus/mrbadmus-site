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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Nine further rows, three per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-e05",
        "band": "easier",
        "text": "Which of these names a deficiency disease together with the "
                "nutrient behind it?",
        "options": [
            {"text": "Scurvy — vitamin C is missing.", "correct": True},
            {"text": "Obesity — lipid is missing.", "correct": False,
             "why": "Obesity follows a long-term energy surplus, which is too "
                    "much rather than too little. It is not a deficiency "
                    "disease at all."},
            {"text": "Anaemia — vitamin C is missing.", "correct": False,
             "why": "Anaemia is a deficiency disease, but the missing "
                    "nutrient is iron, which is built into haemoglobin."},
            {"text": "Rickets — iron is missing.", "correct": False,
             "why": "Rickets is a deficiency disease, and the missing "
                    "nutrient is vitamin D. Without it calcium cannot be "
                    "absorbed properly and the bones stay soft."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e06",
        "band": "easier",
        "text": "What is adipose tissue?",
        "options": [
            {"text": "The tissue that breaks stored lipid down when energy "
                     "runs short.", "correct": False,
             "why": "Adipose tissue is where the lipid sits. Breaking the "
                    "store down is something that happens to it, not what it "
                    "is."},
            {"text": "The tissue that carries oxygen round the body in the "
                     "blood.", "correct": False,
             "why": "That is the job of haemoglobin in red blood cells, and "
                    "it needs iron. Going short of iron gives anaemia."},
            {"text": "The body tissue in which surplus energy is stored as "
                     "lipid.", "correct": True},
            {"text": "The tissue lining the gut that absorbs nutrients out of "
                     "a meal.", "correct": False,
             "why": "That is the wall of the small intestine. Adipose tissue "
                    "is a store, not an absorbing surface."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e07",
        "band": "easier",
        "text": "Obesity raises the risk of several conditions. Which list is "
                "the right one?",
        "options": [
            {"text": "Scurvy, rickets, anaemia and beriberi — the deficiency "
                     "diseases.", "correct": False,
             "why": "Those are deficiency diseases, each caused by one "
                    "missing nutrient. Obesity is a long-term energy surplus, "
                    "which is a different imbalance altogether."},
            {"text": "Goitre, weak bones, constipation and wounds that heal "
                     "slowly.", "correct": False,
             "why": "Those follow shortages of iodine, calcium, fibre and "
                    "protein. None of them is a consequence of an energy "
                    "surplus."},
            {"text": "Kwashiorkor, severe muscle loss, arrested growth and a "
                     "weakened immune system.", "correct": False,
             "why": "Those follow a shortage of protein and a prolonged "
                    "energy shortfall — the opposite imbalance to this one."},
            {"text": "Type 2 diabetes, high blood pressure, heart disease and "
                     "joint damage.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-04-s05",
        "band": "standard",
        "text": "A student says someone at a healthy body mass cannot be "
                "malnourished. Which reply is right?",
        "options": [
            {"text": "They are right, because malnutrition means not having "
                     "enough to eat.", "correct": False,
             "why": "The word means badly nourished, not under-nourished. A "
                    "diet can be generous in energy and still miss a nutrient "
                    "entirely."},
            {"text": "They are wrong — a nutrient can be missing at any level "
                     "of energy intake.", "correct": True},
            {"text": "They are right, as long as the person is eating three "
                     "meals a day.", "correct": False,
             "why": "How many meals arrive says nothing about which nutrients "
                    "are in them. Rickets was widespread among children who "
                    "were fed enough."},
            {"text": "They are wrong, because a healthy body mass always "
                     "hides an energy surplus.", "correct": False,
             "why": "A healthy mass means intake is matching what is "
                    "transferred. The point is that a deficiency is a "
                    "separate question from energy, not a hidden surplus."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s06",
        "band": "standard",
        "text": "A doctor treating someone who has been severely short of food "
                "for months is particularly worried about their heart. Why?",
        "options": [
            {"text": "The heart needs more energy than any other organ, and "
                     "there is none left to give it.", "correct": False,
             "why": "The worry is about what the body is breaking down, not "
                    "about which organ is hungriest. Prolonged shortfall costs "
                    "the body its own protein."},
            {"text": "A shortfall stops the blood carrying oxygen, and that "
                     "strain falls on the heart.", "correct": False,
             "why": "Blood failing to carry oxygen is anaemia, a shortage of "
                    "iron. This case is an energy shortfall, and the danger to "
                    "the heart comes from elsewhere."},
            {"text": "The heart stores lipid, and lipid stores are the first "
                     "thing to be broken down.", "correct": False,
             "why": "Lipid stores do go first, but they sit in adipose "
                    "tissue. The heart is at risk at the next stage, when "
                    "protein starts to go."},
            {"text": "The body starts breaking down its own protein, and the "
                     "heart is muscle.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s07",
        "band": "standard",
        "text": "An adult has gained mass steadily for ten years, eats large "
                "portions, has a desk job and a car commute, and has just been "
                "diagnosed with type 2 diabetes. Which imbalance is this, and "
                "what would change it?",
        "options": [
            {"text": "A long-term energy surplus, changed by a lasting shift "
                     "in intake and activity.", "correct": True},
            {"text": "A nutrient missing, changed by supplying whichever "
                     "nutrient is absent.", "correct": False,
             "why": "Nothing here names a missing nutrient. The evidence is "
                    "ten years of intake above requirement, which is the "
                    "surplus."},
            {"text": "An energy shortfall, because the raised glucose shows "
                     "energy is not reaching the cells.", "correct": False,
             "why": "Ten years of gaining mass rules a shortfall out. The "
                    "raised blood glucose here is one of the risks that "
                    "follows the surplus."},
            {"text": "Both a surplus and a deficiency, and the deficiency has "
                     "to be treated first.", "correct": False,
             "why": "Only one imbalance is in evidence. Ticking a second with "
                    "no sign of it is as much a mistake as refusing to tick "
                    "two when both are really there."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-h05",
        "band": "harder",
        "text": "Two regions both have widespread rickets. In one, food is "
                "scarce. In the other, there is plenty of food and nobody is "
                "thin. How can the same disease appear in both?",
        "options": [
            {"text": "It cannot — one of the two diagnoses has to be wrong.",
             "correct": False,
             "why": "Both can be right. A deficiency occurs at any level of "
                    "energy intake, which is precisely why it can turn up in "
                    "either region."},
            {"text": "The well-fed region's cases must have some other cause, "
                     "since a fed child cannot be deficient.", "correct": False,
             "why": "A deficiency in a fed child is the classic case of "
                    "rickets: enough food, enough energy, and no vitamin D "
                    "reaching the child at all."},
            {"text": "A missing nutrient is a separate question from energy, "
                     "so it happens at either intake.", "correct": True},
            {"text": "In the well-fed region it will be far milder, because "
                     "energy intake protects against deficiency.",
             "correct": False,
             "why": "No amount of any other nutrient substitutes for vitamin "
                    "D. A generous energy intake does not soften the "
                    "deficiency at all."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h06",
        "band": "harder",
        "text": "A newspaper writes: “Obesity causes type 2 diabetes — anyone "
                "above a healthy weight will get it, and you can see who is at "
                "risk just by looking.” Which pair of corrections is the "
                "right one?",
        "options": [
            {"text": "Both halves are right, and the sentence is a fair "
                     "summary of the science.", "correct": False,
             "why": "Neither half is right. Obesity raises the risk rather "
                    "than making it certain, and body mass alone is not "
                    "evidence about anybody's diet."},
            {"text": "Obesity raises the risk rather than making it certain, "
                     "and appearance is not evidence.", "correct": True},
            {"text": "The disease named is the wrong one, and appearance is "
                     "not evidence.", "correct": False,
             "why": "Type 2 diabetes really is one of the risks obesity "
                    "raises. What is wrong is “will get it” — a raised risk "
                    "is a probability, not a verdict."},
            {"text": "Obesity raises the risk rather than making it certain, "
                     "and the risk is visible on sight.", "correct": False,
             "why": "The first half is right. The second is exactly wrong: "
                    "body mass is affected by genetics, illness, medication, "
                    "movement and sleep as well as by diet."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h07",
        "band": "harder",
        "text": "In 1900 a toddler in a smoky northern city, fed bread, "
                "potatoes, tea and a little meat, develops rickets. A toddler "
                "in a sunny country eating the same diet does not. What "
                "explains the difference?",
        "options": [
            {"text": "The second child's food must supply more calcium, and "
                     "calcium is what prevents rickets.", "correct": False,
             "why": "The diets are the same, so the calcium is the same. And "
                    "without vitamin D calcium cannot be absorbed properly, "
                    "however much of it is eaten."},
            {"text": "The first child is short of energy as well, and the "
                     "second child is not.", "correct": False,
             "why": "The city child is not thin and the intake is roughly at "
                    "requirement. Energy is not what is missing here."},
            {"text": "Vitamin D comes from oily fish or from sunlight on "
                     "skin, and one child has sunlight.", "correct": True},
            {"text": "Rickets is an infection that spreads in crowded cities, "
                     "and sunlight kills what causes it.", "correct": False,
             "why": "Rickets is a deficiency disease rather than an "
                    "infection. Sunlight matters because skin makes vitamin D "
                    "in it, not because it kills anything."},
        ],
        "figure": None,
    },
]
