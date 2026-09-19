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

    # ── MRB-338 night 3 top-up ───────────────────────────────────────────
    # Twenty-three further rows per band, appended at bank_position 12+ so
    # the original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-e08",
        "band": "easier",
        "text": "Which is the best definition of obesity?",
        "options": [
            {"text": "A long-term energy surplus stored as lipid, at a level "
                     "that raises health risks.", "correct": True},
            {"text": "A body mass above the average for your age group.",
             "correct": False,
             "why": "Mass alone says nothing about the cause. The lesson "
                    "reasons from measurements and mechanism, not from a "
                    "number compared to an average."},
            {"text": "A single weekend of eating more than usual.",
             "correct": False,
             "why": "A weekend is not long-term. The surplus has to run for "
                    "months or years before the store becomes a problem."},
            {"text": "Eating noticeably more food than most people your age.",
             "correct": False,
             "why": "Obesity is defined by the size of a stored surplus, not "
                    "by how much food arrives on a plate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e09",
        "band": "easier",
        "text": "What is a deficiency disease?",
        "options": [
            {"text": "Any illness that makes someone lose body mass quickly, "
                     "whatever the reason behind it.", "correct": False,
             "why": "Mass loss can have many causes. A deficiency disease has "
                    "one specific cause: one missing nutrient."},
            {"text": "An illness caused by one nutrient being absent or too "
                     "low in the diet.", "correct": True},
            {"text": "An infection caught from eating spoiled food.",
             "correct": False,
             "why": "That is food poisoning, caused by a microbe. A "
                    "deficiency disease has no infectious cause at all."},
            {"text": "A disease that only affects people who are not eating "
                     "enough food overall.", "correct": False,
             "why": "A deficiency can occur at any level of energy intake. "
                    "Rickets was widespread among children who were fed "
                    "enough."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e10",
        "band": "easier",
        "text": "Someone has been in a long-term energy shortfall for months. "
                "Which is a consequence named for children specifically?",
        "options": [
            {"text": "Their adult height is unaffected as long as food "
                     "arrives again eventually.", "correct": False,
             "why": "The opposite is true. In a child the effect on growth "
                    "may not be recoverable, even once food is available "
                    "again."},
            {"text": "Their teeth stop growing but every other tissue is "
                     "unaffected.", "correct": False,
             "why": "The lesson names growth, immune strength and body "
                    "temperature together, not teeth specifically."},
            {"text": "Growth stops, and in a child the effect may not be "
                     "recoverable.", "correct": True},
            {"text": "Their bones set permanently in the exact shape they "
                     "happened to be in at the time.", "correct": False,
             "why": "Bone shape is not what stops. What stops is growth "
                    "itself, and the lesson names that as the effect that may "
                    "not be recoverable."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e11",
        "band": "easier",
        "text": "Which of these is a genuine consequence of a long-term "
                "energy shortfall?",
        "options": [
            {"text": "The immune system becomes stronger, to fight off "
                     "infection.", "correct": False,
             "why": "It is the reverse. A prolonged shortfall weakens the "
                    "immune system rather than strengthening it."},
            {"text": "Blood pressure and joint health both improve.",
             "correct": False,
             "why": "Those risks are raised by a long-term energy surplus, "
                    "not a shortfall — the opposite imbalance."},
            {"text": "Nothing changes about immunity either way.",
             "correct": False,
             "why": "The lesson names a weakened immune system as one of the "
                    "direct consequences of a prolonged shortfall."},
            {"text": "The immune system weakens.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e12",
        "band": "easier",
        "text": "Someone in a long-term energy shortfall often finds it hard "
                "to do what?",
        "options": [
            {"text": "Maintain their body temperature.", "correct": True},
            {"text": "Absorb water in the large intestine.", "correct": False,
             "why": "Water absorption is not named as affected. The named "
                    "difficulty is keeping body temperature steady."},
            {"text": "Taste sweetness, because saliva production falls.",
             "correct": False,
             "why": "Tasting sweetness is not mentioned here at all. The "
                    "named difficulty in shortfall is body temperature."},
            {"text": "Digest protein, because protease stops working "
                     "without enough energy.", "correct": False,
             "why": "Protease is not disabled by a shortfall. The named "
                    "difficulty is maintaining body temperature."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e13",
        "band": "easier",
        "text": "Someone with iron-deficiency anaemia eats much larger "
                "portions of bread and pasta, hoping it will fix the "
                "anaemia. Will it?",
        "options": [
            {"text": "Yes, because the extra energy converts into iron once "
                     "it is stored.", "correct": False,
             "why": "Energy does not convert into a mineral. Iron has to "
                    "arrive in the diet as iron."},
            {"text": "No — a missing nutrient needs supplying, and bread and "
                     "pasta supply almost none of it.", "correct": True},
            {"text": "No, because bread and pasta actively remove iron from "
                     "the blood.", "correct": False,
             "why": "They do not remove iron. They simply supply very little "
                    "of it, which leaves the anaemia untouched."},
            {"text": "Yes — more food of any kind always corrects a "
                     "deficiency eventually.", "correct": False,
             "why": "Nothing else can substitute for the missing nutrient. "
                    "No amount of carbohydrate replaces the iron that is "
                    "absent."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e14",
        "band": "easier",
        "text": "Once the missing nutrient is supplied, how does a deficiency "
                "disease typically respond?",
        "options": [
            {"text": "Only if the person also increases their total energy "
                     "intake.", "correct": False,
             "why": "Energy intake is a separate question from the missing "
                    "nutrient. Supplying the nutrient is what matters here."},
            {"text": "Slowly, taking years to show any improvement.",
             "correct": False,
             "why": "The lesson describes the opposite — supplying the one "
                    "nutrient is often a fast and complete recovery."},
            {"text": "Often with a fast and complete recovery.",
             "correct": True},
            {"text": "It cannot be reversed once the disease has started.",
             "correct": False,
             "why": "Deficiency diseases are exactly the kind of imbalance "
                    "that responds well once the missing nutrient arrives."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e15",
        "band": "easier",
        "text": "Storing some surplus energy as lipid happens in most people "
                "from time to time. According to the lesson, what actually "
                "makes this a problem?",
        "options": [
            {"text": "The particular food eaten, regardless of the total "
                     "amount of it that ends up being stored.", "correct": False,
             "why": "The lesson's argument is about balance over time, not "
                    "about which specific food supplied the surplus."},
            {"text": "Nothing — storing surplus energy as lipid is never "
                     "described as a problem.", "correct": False,
             "why": "It becomes a problem once the store keeps growing over a "
                    "long period, which is exactly what obesity is."},
            {"text": "Storage itself, since fat should never be laid down at "
                     "all.", "correct": False,
             "why": "Storage is described as a normal, healthy mechanism. "
                    "The problem named is only the size of the store."},
            {"text": "The size of the store, once it keeps growing over "
                     "months or years.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e16",
        "band": "easier",
        "text": "A long-term energy shortfall can be caused by food being "
                "unavailable. What other kind of cause does the lesson name?",
        "options": [
            {"text": "Illness that prevents someone eating or absorbing "
                     "their food.", "correct": True},
            {"text": "Eating too many different food groups at once.",
             "correct": False,
             "why": "Variety is not named as a cause of shortfall anywhere in "
                    "the lesson."},
            {"text": "Choosing low-energy foods that are still perfectly "
                     "balanced.", "correct": False,
             "why": "A balanced low-energy diet is not the cause named here. "
                    "Illness preventing eating or absorption is the other "
                    "named cause."},
            {"text": "Cooking food for too short a time.", "correct": False,
             "why": "Cooking time is never mentioned as a cause of energy "
                    "shortfall in this lesson."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e17",
        "band": "easier",
        "text": "James Lind's 1747 scurvy trial had twelve patients. How were "
                "they divided?",
        "options": [
            {"text": "Into three groups of four, testing three treatments.",
             "correct": False,
             "why": "There were six treatments in total, tested one pair at a "
                    "time, not three groups of four."},
            {"text": "Into six pairs, each pair given a different treatment.",
             "correct": True},
            {"text": "Into two large groups of six, one given citrus and one "
                     "given nothing.", "correct": False,
             "why": "The trial used six different treatments, one pair each, "
                    "not two large groups."},
            {"text": "Into twelve separate groups, one patient testing each "
                     "possible treatment alone.", "correct": False,
             "why": "The patients were paired up — six pairs of two — not "
                    "tested singly."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e18",
        "band": "easier",
        "text": "Which pair of patients in Lind's trial recovered from "
                "scurvy?",
        "options": [
            {"text": "The pair given seawater.", "correct": False,
             "why": "Seawater was one of the six treatments tried, but it was "
                    "not the pair that recovered."},
            {"text": "The pair given cider.", "correct": False,
             "why": "Cider was tried, but the recovery is recorded for the "
                    "citrus pair, not the cider pair."},
            {"text": "The pair given two oranges and a lemon.",
             "correct": True},
            {"text": "The pair given a paste of herbs.", "correct": False,
             "why": "The herb paste was one of six treatments tested, but the "
                    "recorded recovery belongs to the citrus pair."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e19",
        "band": "easier",
        "text": "An adult has tiredness, breathlessness on stairs and pale "
                "skin, with low haemoglobin on a blood test. Their energy "
                "intake is close to requirement. What is most likely missing?",
        "options": [
            {"text": "Vitamin D.", "correct": False,
             "why": "Vitamin D missing gives rickets, affecting bones. Low "
                    "haemoglobin points at iron instead."},
            {"text": "Nothing — the signs are explained by normal tiredness.",
             "correct": False,
             "why": "Low haemoglobin on a blood test is a specific clinical "
                    "finding, not ordinary tiredness."},
            {"text": "Vitamin C.", "correct": False,
             "why": "Vitamin C missing gives scurvy, whose signs are "
                    "different — this pattern points at haemoglobin, which "
                    "needs iron."},
            {"text": "Iron.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e20",
        "band": "easier",
        "text": "A child eats enough food and enough energy, but almost no "
                "vitamin D reaches them. What cannot happen properly as a "
                "result?",
        "options": [
            {"text": "Calcium being absorbed, so the bones stay soft.",
             "correct": True},
            {"text": "Iron being absorbed, so the blood becomes short of "
                     "oxygen.", "correct": False,
             "why": "Iron absorption is not the vitamin D story. Missing "
                    "vitamin D stops calcium being properly absorbed."},
            {"text": "Vitamin C being made in the body.", "correct": False,
             "why": "The body does not make vitamin C from vitamin D — the "
                    "two are entirely separate nutrients."},
            {"text": "Digesting starch, so energy intake falls.",
             "correct": False,
             "why": "Starch digestion needs amylase, not vitamin D, and "
                    "energy intake is described as roughly at requirement "
                    "here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e21",
        "band": "easier",
        "text": "Which vitamin, missing from the diet, causes scurvy?",
        "options": [
            {"text": "Iron.", "correct": False,
             "why": "Iron is a mineral, not a vitamin, and missing iron "
                    "causes anaemia rather than scurvy."},
            {"text": "Vitamin C.", "correct": True},
            {"text": "Vitamin B12.", "correct": False,
             "why": "Vitamin B12 deficiency is common enough to be a routine "
                    "blood test, but it is not the cause of scurvy."},
            {"text": "Vitamin D.", "correct": False,
             "why": "Vitamin D missing causes rickets, a different named "
                    "deficiency disease."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e22",
        "band": "easier",
        "text": "Roughly what timescale turns an energy surplus or shortfall "
                "into the “long-term” kind the lesson is about?",
        "options": [
            {"text": "Both count from the very first day the balance tips "
                     "either way.", "correct": False,
             "why": "A single day of imbalance is not long-term. The lesson "
                    "names weeks, months or years, not one day."},
            {"text": "A surplus over a single week; a shortfall over a single "
                     "day.", "correct": False,
             "why": "Those timescales are far too short. The lesson's own "
                    "figures are months or years for a surplus and weeks or "
                    "months for a shortfall."},
            {"text": "A surplus over months or years; a shortfall over weeks "
                     "or months.", "correct": True},
            {"text": "Both need to run for at least a full decade before "
                     "either counts.", "correct": False,
             "why": "A decade is far longer than the lesson names. A "
                    "shortfall of weeks or months, or a surplus of months or "
                    "years, is already enough."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e23",
        "band": "easier",
        "text": "A footballer eats an unusually large meal after a match, then "
                "returns to their normal diet the next day. Does this single "
                "large meal make them obese?",
        "options": [
            {"text": "Yes — any single meal above requirement is stored as "
                     "lipid immediately and permanently.", "correct": False,
             "why": "One meal is not a long-term surplus. Obesity is defined "
                    "by a surplus that runs for months or years."},
            {"text": "It depends only on how large the meal was, not on how "
                     "often this happens.", "correct": False,
             "why": "Duration is what the lesson's definition turns on, not "
                    "the size of any single meal."},
            {"text": "Yes, because energy taken in can never be balanced out "
                     "by a normal diet afterwards.", "correct": False,
             "why": "A return to a normal diet is exactly what keeps the "
                    "balance from becoming a long-term surplus."},
            {"text": "No — obesity needs a surplus that runs for months or "
                     "years, not one meal.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e24",
        "band": "easier",
        "text": "Name two ways the body can obtain vitamin D.",
        "options": [
            {"text": "From oily fish, or from sunlight on skin.",
             "correct": True},
            {"text": "From red meat, or from drinking plenty of water.",
             "correct": False,
             "why": "Red meat is named for iron and water carries no vitamin "
                    "at all. Vitamin D comes from oily fish or sunlight."},
            {"text": "From bread and pasta, or from any starchy food.",
             "correct": False,
             "why": "Starchy foods supply energy, not vitamin D. The named "
                    "sources are oily fish and sunlight on skin."},
            {"text": "From citrus fruit, or from green leafy vegetables.",
             "correct": False,
             "why": "Citrus fruit supplies vitamin C, and leafy vegetables "
                    "are named for iron, not for vitamin D."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e25",
        "band": "easier",
        "text": "Which deficiency is common enough worldwide that doctors "
                "check for it as a routine blood test?",
        "options": [
            {"text": "None — deficiencies are only tested for when symptoms "
                     "are obvious.", "correct": False,
             "why": "Vitamin B12 deficiency is common enough to be tested "
                    "routinely, precisely because its symptoms are not always "
                    "obvious."},
            {"text": "Vitamin B12 deficiency.", "correct": True},
            {"text": "Rickets, in every patient regardless of symptoms.",
             "correct": False,
             "why": "Rickets is not the example given as a routine screening "
                    "test. Vitamin B12 deficiency is the one named that way."},
            {"text": "Scurvy, checked at every hospital admission.",
             "correct": False,
             "why": "Scurvy still appears in hospitals but is not described "
                    "as a routine screening test the way B12 is."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e26",
        "band": "easier",
        "text": "Early signs of a deficiency — tiredness, aching, slow healing "
                "and low mood — are best described as which of these?",
        "options": [
            {"text": "A pattern unique to iron deficiency alone.",
             "correct": False,
             "why": "The lesson does not tie this pattern to one nutrient — "
                    "it describes them as generally non-specific."},
            {"text": "Certain proof that one particular nutrient is missing.",
             "correct": False,
             "why": "They are not certain proof of anything on their own — "
                    "the lesson calls them some of the least specific signs "
                    "in medicine."},
            {"text": "Some of the least specific symptoms in medicine.",
             "correct": True},
            {"text": "Signs that only ever appear in severe, late-stage "
                     "disease.", "correct": False,
             "why": "The opposite is closer to true — these are early signs, "
                    "which is exactly why a deficiency is easy to miss."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e27",
        "band": "easier",
        "text": "Which situation, kept up for months or years, describes a "
                "long-term energy surplus?",
        "options": [
            {"text": "Energy taken in matches energy transferred almost "
                     "exactly, day after day.", "correct": False,
             "why": "A close match between intake and transfer is a stable "
                    "balance, not a surplus."},
            {"text": "Energy taken in varies a great deal from one day to the "
                     "next, without following any clear pattern.",
             "correct": False,
             "why": "Day-to-day variation on its own is not what defines a "
                    "surplus — the direction of the imbalance is what "
                    "matters."},
            {"text": "Energy taken in is measured once and never checked "
                     "again.", "correct": False,
             "why": "How often intake is measured says nothing about whether "
                    "a surplus exists."},
            {"text": "Energy taken in is greater than energy transferred, day "
                     "after day.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e28",
        "band": "easier",
        "text": "Someone takes in less energy than they transfer, week after "
                "week, for two months. Which imbalance does this describe?",
        "options": [
            {"text": "A long-term energy shortfall.", "correct": True},
            {"text": "A long-term energy surplus.", "correct": False,
             "why": "A surplus is the opposite pattern — more energy in than "
                    "out. This case describes less energy in than out."},
            {"text": "A deficiency disease affecting one nutrient.",
             "correct": False,
             "why": "A deficiency is about one missing nutrient, not about "
                    "the total energy balance described here."},
            {"text": "A single unusually low-energy day.", "correct": False,
             "why": "Two months is far longer than a single day, which is "
                    "exactly why this counts as long-term rather than a "
                    "one-off."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e29",
        "band": "easier",
        "text": "Seven nutrients have to arrive in a diet. How many of them "
                "carry energy?",
        "options": [
            {"text": "All seven of them, in roughly equal amounts.",
             "correct": False,
             "why": "Only some of the seven carry energy at all. Vitamins and "
                    "minerals, for instance, carry none."},
            {"text": "Three — carbohydrate, lipid and protein.",
             "correct": True},
            {"text": "One — carbohydrate is the only nutrient that carries "
                     "energy.", "correct": False,
             "why": "Lipid and protein also carry energy. Carbohydrate is one "
                    "of three, not the only one."},
            {"text": "None — energy comes only from vitamins and minerals.",
             "correct": False,
             "why": "Vitamins and minerals carry no energy at all. The three "
                    "energy-carrying nutrients are carbohydrate, lipid and "
                    "protein."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-e30",
        "band": "easier",
        "text": "In industrial British cities, rickets was once common among "
                "children who were fed enough food. What does this show?",
        "options": [
            {"text": "Rickets is caused by eating too much rather than too "
                     "little.", "correct": False,
             "why": "Rickets is a deficiency disease, caused by a nutrient "
                    "being absent — not by an energy surplus."},
            {"text": "Being fed enough always rules out any deficiency "
                     "disease.", "correct": False,
             "why": "This case is exactly the counterexample — being fed "
                    "enough did not rule out a vitamin D deficiency at all."},
            {"text": "A deficiency can occur regardless of how much food or "
                     "energy a child receives at all.", "correct": True},
            {"text": "Those children must actually have been eating very "
                     "little.", "correct": False,
             "why": "They were fed enough — the case shows a deficiency can "
                    "happen even so, not that the feeding was secretly "
                    "inadequate."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-04-s08",
        "band": "standard",
        "text": "A student says: “Storing any fat as lipid is unhealthy.” "
                "How would the lesson correct this?",
        "options": [
            {"text": "Storing surplus energy as lipid is a normal, healthy "
                     "mechanism — the problem is only when the store keeps "
                     "growing over a long period.", "correct": True},
            {"text": "It is unhealthy the moment any lipid is stored, however "
                     "briefly.", "correct": False,
             "why": "The lesson calls storage itself a normal, healthy "
                    "mechanism. What matters is whether the store keeps "
                    "growing."},
            {"text": "It is only unhealthy if the lipid is stored in the "
                     "liver rather than elsewhere.", "correct": False,
             "why": "The lesson does not distinguish storage sites this way. "
                    "The issue named is the size of the store over time."},
            {"text": "It is unhealthy only for people who already have a "
                     "diagnosed illness.", "correct": False,
             "why": "The health risk is tied to the size and duration of the "
                    "store, not to any pre-existing diagnosis."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s09",
        "band": "standard",
        "text": "A person has an illness that stops them absorbing food "
                "properly, even though food is available and they eat "
                "normal amounts. Are they in a long-term energy shortfall?",
        "options": [
            {"text": "No — a shortfall only counts if food itself is "
                     "unavailable.", "correct": False,
             "why": "The lesson names illness that prevents eating or "
                    "absorbing as a cause of shortfall in its own right, not "
                    "only food scarcity."},
            {"text": "Yes — a shortfall can be caused by illness preventing "
                     "absorption, not only by food being scarce.",
             "correct": True},
            {"text": "No, because eating normal amounts always means enough "
                     "energy is being transferred.", "correct": False,
             "why": "What is eaten and what is absorbed are two different "
                    "steps. Failing to absorb it can still produce a "
                    "shortfall."},
            {"text": "It cannot be answered without knowing their body "
                     "mass.", "correct": False,
             "why": "Body mass is not needed here — the mechanism (illness "
                    "preventing absorption) is itself one of the lesson's "
                    "named causes of shortfall."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s10",
        "band": "standard",
        "text": "A child suffers a long period of stunted growth during a "
                "severe shortfall, then has reliable food access for the "
                "rest of childhood. Predict the outcome for their adult "
                "height, using the lesson's own claim.",
        "options": [
            {"text": "Growth will resume exactly where it left off, with no "
                     "loss at all.", "correct": False,
             "why": "That is the outcome the lesson rules out — the growth "
                    "effect in a child may not be recoverable."},
            {"text": "Full catch-up growth is certain once food access "
                     "improves.", "correct": False,
             "why": "The lesson says the opposite — in a child the effect on "
                    "growth may not be recoverable, even with better food "
                    "later."},
            {"text": "The effect on their growth may not be fully "
                     "recoverable.", "correct": True},
            {"text": "Their height will be unaffected, because growth only "
                     "depends on genetics.", "correct": False,
             "why": "The lesson directly links growth to energy shortfall in "
                    "childhood, not only to genetics."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s11",
        "band": "standard",
        "text": "A well-meaning family gives a severely malnourished relative "
                "a large, normal-sized meal as soon as food becomes "
                "available, rather than small amounts gradually. Predict "
                "the outcome.",
        "options": [
            {"text": "This is safe as long as the meal contains no fat at "
                     "all, because fat is what makes a fast refeed "
                     "dangerous for the heart.", "correct": False,
             "why": "The danger named is the speed and scale of refeeding "
                    "generally, not the presence of fat specifically."},
            {"text": "This is dangerous only if the relative is a young "
                     "child.", "correct": False,
             "why": "The lesson states the danger of fast refeeding for "
                    "anyone recovering from prolonged starvation, not only "
                    "children."},
            {"text": "This is safe, because any food after a long shortfall "
                     "can only help the body recover its strength as "
                     "quickly as possible.", "correct": False,
             "why": "The lesson is explicit that restarting food too fast "
                    "after prolonged starvation is itself dangerous."},
            {"text": "This could be dangerous — refeeding after prolonged "
                     "starvation has to be done carefully and gradually.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s12",
        "band": "standard",
        "text": "A patient with a diagnosed B12 deficiency initially reports "
                "only feeling tired and run down. Why might a doctor take "
                "this seriously rather than dismissing it?",
        "options": [
            {"text": "Because tiredness, aching and low mood are exactly the "
                     "non-specific signs that make a deficiency easy to "
                    "miss.", "correct": True},
            {"text": "Because B12 deficiency only ever causes tiredness and "
                     "nothing else.", "correct": False,
             "why": "The lesson does not say B12 deficiency causes only "
                    "tiredness — it names tiredness as one of several "
                    "non-specific early signs of a deficiency generally."},
            {"text": "Because a B12 deficiency cannot exist without an "
                     "obviously restricted diet, since the vitamin is found "
                     "in almost every ordinary meal a person eats.",
             "correct": False,
             "why": "A B12 deficiency can occur in a diet that looks entirely "
                    "ordinary, which is exactly why it is tested for "
                    "routinely."},
            {"text": "Because tiredness always means a vitamin is missing.",
             "correct": False,
             "why": "Tiredness has many possible causes — the point is that "
                    "these vague signs should not be dismissed, not that they "
                    "always mean a deficiency."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s13",
        "band": "standard",
        "text": "A patient eats the same total energy each day but replaces "
                "most fruit and vegetables with processed snacks of equal "
                "energy value. Could this diet cause a deficiency disease "
                "even though the total energy is unchanged?",
        "options": [
            {"text": "No — matching the total energy always guarantees every "
                     "other nutrient is also matched.", "correct": False,
             "why": "Energy is carried by only three of the seven nutrients. "
                    "Matching the energy total says nothing about vitamins or "
                    "minerals."},
            {"text": "Yes — the total energy can stay the same while a "
                     "specific vitamin or mineral falls away entirely.",
             "correct": True},
            {"text": "No, because processed snacks always contain more "
                     "vitamins than fresh food.", "correct": False,
             "why": "That is not a claim the lesson makes, and it runs the "
                    "wrong way — the change described risks losing nutrients "
                    "fruit and vegetables supplied."},
            {"text": "It depends only on how many meals a day the person "
                     "eats, rather than on which foods those meals actually "
                     "contain.", "correct": False,
             "why": "Meal frequency is not the issue here — it is which "
                    "nutrients the food actually supplies."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s14",
        "band": "standard",
        "text": "A 14-year-old has stopped growing over eighteen months and "
                "bruises easily; their family has struggled to afford "
                "regular meals. Beyond an energy shortfall, what else does "
                "the bruising suggest?",
        "options": [
            {"text": "A vitamin D deficiency, since bruising and rickets are "
                     "believed to share the same underlying cause.",
             "correct": False,
             "why": "Vitamin D deficiency affects bones, not clotting. "
                    "Bruising points instead at vitamin C or K."},
            {"text": "That the family diagnosis must be wrong, since one "
                     "cause cannot produce two kinds of sign.", "correct": False,
             "why": "One person can have more than one imbalance at once — "
                    "that is a case this lesson is built to make clear."},
            {"text": "A possible deficiency in vitamin C or vitamin K "
                     "alongside the shortfall.", "correct": True},
            {"text": "Nothing further — bruising is fully explained by the "
                     "shortfall alone.", "correct": False,
             "why": "The shortfall explains the growth arrest; the bruising "
                    "specifically points at a further, separate deficiency."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s15",
        "band": "standard",
        "text": "Two people are similarly overweight, having eaten well above "
                "requirement for years. Only one of them goes on to develop "
                "type 2 diabetes. What does this show about the risk?",
        "options": [
            {"text": "That the person without diabetes must actually be "
                     "eating less than the other.", "correct": False,
             "why": "Nothing in the case says their intake differs — the "
                    "point is that a raised risk does not fall on everyone "
                    "equally."},
            {"text": "That type 2 diabetes is entirely unrelated to a "
                     "long-term energy surplus.", "correct": False,
             "why": "It is one of the risks a long-term surplus raises — one "
                    "person not developing it does not remove the link."},
            {"text": "That the risk was never real in the first place.",
             "correct": False,
             "why": "One person developing the condition shows the risk was "
                    "real. What the pair together shows is that it is a "
                    "raised risk, not a certainty."},
            {"text": "That obesity only raises the risk of type 2 diabetes "
                     "rather than guaranteeing it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s16",
        "band": "standard",
        "text": "An adult recovering from bowel surgery eats normal, varied "
                "meals but is losing mass and has several low vitamin "
                "levels. Their energy intake measures close to requirement. "
                "What has most likely failed?",
        "options": [
            {"text": "Absorption — enough reaches the mouth, but not enough "
                     "is getting into the blood.", "correct": True},
            {"text": "Appetite — they must actually be eating far less than "
                     "they report.", "correct": False,
             "why": "The case states normal, varied meals. Reasoning from "
                    "appearance or assumption over the stated intake is "
                    "exactly the mistake this lesson warns against."},
            {"text": "The vitamins in the meal, which must have been "
                     "destroyed by cooking.", "correct": False,
             "why": "Cooking loss is not named as the mechanism here — the "
                    "pattern of falling mass alongside low vitamins points at "
                    "a failure of absorption."},
            {"text": "Digestion — nothing in the meal is being broken down "
                     "at all.", "correct": False,
             "why": "The case does not describe undigested food passing "
                    "through. What has failed is what happens after "
                    "digestion — getting the nutrients into the blood."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s17",
        "band": "standard",
        "text": "In 1900, some doctors assumed a child who was clearly being "
                "fed could not be malnourished. Using the lesson, explain "
                "why that assumption is wrong.",
        "options": [
            {"text": "It is not wrong — a fed child genuinely cannot develop "
                     "a deficiency disease.", "correct": False,
             "why": "Rickets in fed children is exactly the case the lesson "
                    "uses to show that a deficiency can occur at any energy "
                    "intake."},
            {"text": "Because malnutrition means the balance of the diet is "
                     "wrong, and a nutrient can be missing at any level of "
                     "energy intake.", "correct": True},
            {"text": "Because being fed only prevents an energy shortfall, "
                     "never a surplus.", "correct": False,
             "why": "The assumption fails for a different reason: a specific "
                    "nutrient can be missing regardless of how much food or "
                    "energy is arriving."},
            {"text": "Because doctors in 1900 had no way of weighing food at "
                     "all.", "correct": False,
             "why": "The error is not about measurement ability — it is the "
                    "belief that being fed rules out a deficiency, which the "
                    "lesson shows is false."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s18",
        "band": "standard",
        "text": "Lind's scurvy trial used only two patients per treatment and "
                "was not blinded. Does that weakness mean the citrus result "
                "should be doubted?",
        "options": [
            {"text": "No, because a trial run in the 1700s cannot have any "
                     "weaknesses worth naming.", "correct": False,
             "why": "The small sample and lack of blinding are real, "
                    "namable weaknesses — the point is that they do not "
                    "overturn what the trial found."},
            {"text": "Yes — with only two patients per treatment, no "
                     "conclusion can ever be drawn from the trial.",
             "correct": False,
             "why": "The small size is a real weakness, but the effect seen "
                    "was clear and has since been confirmed many times over — "
                    "the conclusion still stands."},
            {"text": "No — the design has a real weakness, but the citrus "
                     "result has held up and is not in doubt.", "correct": True},
            {"text": "Yes, because an unblinded trial always produces the "
                     "opposite of the true result.", "correct": False,
             "why": "Being unblinded is a genuine limitation, but it does not "
                    "reverse a result — it raises the chance of bias, which "
                    "here did not occur."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s19",
        "band": "standard",
        "text": "Someone overeats noticeably for a single weekend and then "
                "returns to their usual diet. Are they at meaningful risk of "
                "obesity from this alone?",
        "options": [
            {"text": "Yes, because any surplus at all is stored as lipid "
                     "permanently from that point onwards.", "correct": False,
             "why": "A single weekend is nowhere near the months-or-years "
                    "timescale the lesson gives for a surplus to matter."},
            {"text": "It depends on exactly how many extra kilojoules were "
                     "eaten, regardless of how long it lasted.",
             "correct": False,
             "why": "Duration is the deciding factor in the lesson's own "
                    "definition, not the size of one short episode."},
            {"text": "Yes, but only if the extra food eaten was mostly fat "
                     "rather than carbohydrate.", "correct": False,
             "why": "The lesson's criterion is how long the surplus runs, not "
                    "which nutrient supplied it."},
            {"text": "No — obesity needs a surplus sustained over months or "
                     "years, and a weekend is far too short.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s20",
        "band": "standard",
        "text": "A newspaper claims an overweight public figure “clearly eats "
                "badly” without knowing anything about their health, "
                "medication or activity levels. What is the strongest "
                "criticism of this claim?",
        "options": [
            {"text": "Body mass is affected by many things besides diet, so "
                     "appearance alone is not evidence about what someone "
                     "eats.", "correct": True},
            {"text": "The claim is fine, because body mass is decided almost "
                     "entirely by diet, and diet is the one thing a person "
                     "fully controls.", "correct": False,
             "why": "The lesson lists genetics, illness, medication, "
                    "movement and sleep as also affecting mass — diet is only "
                    "one factor among several."},
            {"text": "The claim would only be wrong if the public figure "
                     "turned out to be unwell.", "correct": False,
             "why": "The claim is unsupported regardless of the actual cause "
                    "— reasoning from appearance to diet is the flaw, not the "
                    "outcome."},
            {"text": "Newspapers are never a reliable source, so the claim "
                     "should be ignored for that reason alone.", "correct": False,
             "why": "The source is not the issue here — the reasoning from "
                    "appearance to diet is what the lesson specifically "
                    "rejects."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s21",
        "band": "standard",
        "text": "A prolonged energy shortfall is named as weakening the "
                "immune system and making it hard to maintain body "
                "temperature. What links these two particular consequences, "
                "rather than them being random?",
        "options": [
            {"text": "Both only appear once a specific deficiency disease has "
                     "also developed.", "correct": False,
             "why": "They are described as consequences of the shortfall "
                    "itself, not conditional on a separate deficiency also "
                    "being present."},
            {"text": "Both come only from the body running short of the "
                     "energy and resources it needs to keep normal "
                     "processes running.", "correct": True},
            {"text": "Nothing links them — they are entirely unconnected "
                     "coincidences with no shared cause between them.",
             "correct": False,
             "why": "Both are consequences of the same underlying shortfall, "
                    "not unrelated coincidences."},
            {"text": "Both are caused specifically by a lack of vitamin D, "
                     "regardless of overall energy intake, since vitamin D "
                     "also helps regulate body temperature directly.",
             "correct": False,
             "why": "These are named as shortfall consequences, tied to "
                    "energy, not to one specific vitamin."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s22",
        "band": "standard",
        "text": "A patient with a fully balanced, varied diet still develops "
                "a deficiency disease. Does this contradict the lesson's own "
                "argument?",
        "options": [
            {"text": "No, but only because the diet must secretly be missing "
                     "one food group.", "correct": False,
             "why": "The case need not involve a missing food group at all — "
                    "a failure of absorption is enough on its own."},
            {"text": "Yes — a genuinely balanced diet should make any "
                     "deficiency disease impossible.", "correct": False,
             "why": "The lesson's own clinic 5 shows the opposite: a plate "
                    "can be entirely adequate while absorption still fails."},
            {"text": "No — even a good diet can never guarantee against a "
                     "deficiency if the nutrient is not being absorbed "
                     "properly.", "correct": True},
            {"text": "Yes, because a balanced diet by definition contains "
                     "every nutrient in a large enough amount for the body "
                     "to use it straight away.", "correct": False,
             "why": "What is on the plate is a separate question from what "
                    "actually reaches the blood — absorption can fail even "
                    "when the diet is adequate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s23",
        "band": "standard",
        "text": "Comparing scurvy and rickets, what do both diseases have in "
                "common once the missing nutrient is identified?",
        "options": [
            {"text": "Both need months of a long-term energy surplus before "
                     "they can be reversed.", "correct": False,
             "why": "Neither is linked to a surplus at all — both are "
                    "deficiency diseases, reversed by supplying the missing "
                    "nutrient."},
            {"text": "Neither can be reversed once the disease has become "
                     "visible.", "correct": False,
             "why": "The lesson describes deficiency diseases as often "
                    "recovering fast and completely once treated, not as "
                    "irreversible."},
            {"text": "Both are caused by the same single nutrient being "
                     "absent.", "correct": False,
             "why": "They are caused by two different nutrients — vitamin C "
                    "for scurvy and vitamin D for rickets."},
            {"text": "Both usually respond quickly once the specific missing "
                     "nutrient is supplied.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s24",
        "band": "standard",
        "text": "An athlete eating well above requirement for years develops "
                "raised blood pressure. A friend says “that has nothing to "
                "do with diet, since athletes are always healthy.” What is "
                "wrong with the friend's reasoning?",
        "options": [
            {"text": "A long-term energy surplus can raise blood pressure "
                     "regardless of someone's general activity or "
                     "reputation.", "correct": True},
            {"text": "The friend is right, because raised blood pressure is "
                     "always caused by stress rather than diet.",
             "correct": False,
             "why": "The lesson names raised blood pressure as one of the "
                    "risks a long-term energy surplus raises — stress is not "
                    "given as the explanation here."},
            {"text": "The friend is right, but only because athletes never "
                     "develop deficiency diseases either.", "correct": False,
             "why": "Whether athletes can develop a deficiency is a separate "
                    "question — the case here concerns a surplus, not a "
                    "missing nutrient."},
            {"text": "Nothing — athletes cannot have a long-term energy "
                     "surplus by definition, whatever their actual food "
                     "intake happens to be.", "correct": False,
             "why": "Being an athlete does not prevent a long-term surplus. "
                    "Years of intake above requirement is exactly the pattern "
                    "the lesson links to raised blood pressure."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s25",
        "band": "standard",
        "text": "A parent worries that giving their child a general "
                "multivitamin guarantees no deficiency disease can ever "
                "develop. Explain why that is not quite right.",
        "options": [
            {"text": "It is not right, because multivitamins only ever "
                     "supply energy, never any of the seven nutrients.",
             "correct": False,
             "why": "Multivitamins are specifically vitamins and minerals, "
                    "not an energy source — the concern is dose, not "
                    "category."},
            {"text": "A multivitamin could still supply too little of one "
                     "specific nutrient the child particularly needs.",
             "correct": True},
            {"text": "Multivitamins actively cause deficiency diseases in "
                     "children.", "correct": False,
             "why": "The lesson gives no reason to think a multivitamin "
                    "causes deficiency — the concern is whether the dose is "
                    "enough, not that it is harmful."},
            {"text": "It is exactly right — any multivitamin removes the "
                     "possibility of a deficiency completely.", "correct": False,
             "why": "Whether a deficiency is prevented depends on the amount "
                    "of each nutrient supplied, which a general multivitamin "
                    "cannot guarantee for every child."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s26",
        "band": "standard",
        "text": "Two patients eat exactly the same daily energy intake. One "
                "eats mostly fresh, varied food; the other eats mostly "
                "processed food of the same energy value. Only the second "
                "develops a deficiency disease. What does this tell you?",
        "options": [
            {"text": "That processed food always contains more energy than "
                     "fresh food.", "correct": False,
             "why": "The energy values are stated as equal. What differs is "
                    "the nutrient content, not the energy."},
            {"text": "That a deficiency disease can only develop if total "
                     "energy intake is also too low, since nutrients and "
                     "energy are assumed to rise and fall together.",
             "correct": False,
             "why": "This case shows the reverse — a deficiency can develop "
                    "at an energy intake that is entirely adequate."},
            {"text": "That matching energy intake tells you nothing about "
                     "whether the other nutrients are also matched.",
             "correct": True},
            {"text": "That the second patient must actually be eating less "
                     "energy than reported.", "correct": False,
             "why": "The case states the energy intakes are equal — the "
                    "difference lies in which other nutrients each diet "
                    "supplies, not in the energy total."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s27",
        "band": "standard",
        "text": "An adult changes from a physically active job to a desk job "
                "and gradually gains mass over several years while eating "
                "the same portions as before. Which imbalance does this "
                "describe, and why?",
        "options": [
            {"text": "A specific nutrient missing — the same portions must "
                     "now be missing something they used to contain.",
             "correct": False,
             "why": "Nothing about a job change alters what the food itself "
                    "contains. The change here is in energy transferred, not "
                    "in nutrient content."},
            {"text": "A long-term energy shortfall — sitting all day uses "
                     "less energy than the body can supply.", "correct": False,
             "why": "Using less energy while intake stays the same points "
                    "towards a surplus, not a shortfall."},
            {"text": "No imbalance at all, since the portions eaten have not "
                     "changed.", "correct": False,
             "why": "Balance depends on intake against activity, not on "
                    "portions alone — falling activity with unchanged intake "
                    "is a surplus."},
            {"text": "A long-term energy surplus — the same intake against "
                     "much less activity now leaves more energy unused.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s28",
        "band": "standard",
        "text": "Case A: an adult eats close to requirement and is diagnosed "
                "with iron-deficiency anaemia alone. Case B: a teenager eats "
                "far below requirement and is diagnosed with anaemia and "
                "growth arrest together. What is the key difference between "
                "the two cases?",
        "options": [
            {"text": "Case A has one imbalance; Case B has an energy "
                     "shortfall alongside the deficiency.", "correct": True},
            {"text": "There is no real difference — both cases describe "
                     "exactly the same imbalance.", "correct": False,
             "why": "Case A shows a deficiency with energy intake near "
                    "requirement; Case B adds a shortfall on top, which is "
                    "the difference worth naming."},
            {"text": "Case B must have been misdiagnosed, since anaemia "
                     "cannot occur alongside a shortfall.", "correct": False,
             "why": "A shortfall and a deficiency can occur together — a "
                    "prolonged shortfall drags specific deficiencies along "
                    "behind it."},
            {"text": "Case A is more serious, because anaemia there has no "
                     "other cause at all to compete against it.",
             "correct": False,
             "why": "Severity is not established by how many imbalances are "
                    "present — the difference to name is which imbalances "
                    "apply, not which case is worse."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s29",
        "band": "standard",
        "text": "A student argues: “If you eat a balanced diet, you can never "
                "develop a deficiency disease.” Is this true?",
        "options": [
            {"text": "Yes — a balanced diet always prevents every deficiency "
                     "disease.", "correct": False,
             "why": "A balanced diet on the plate does not guarantee "
                    "absorption. Clinic 5 shows a deficiency developing "
                    "despite an entirely adequate diet."},
            {"text": "No — a nutrient the plate genuinely supplies can still "
                     "fail to reach the blood if absorption fails.",
             "correct": True},
            {"text": "Yes, as long as the balanced diet also supplies enough "
                     "total energy.", "correct": False,
             "why": "Total energy is a separate question from whether "
                    "absorption is working. Energy alone does not guard "
                    "against a failure to absorb."},
            {"text": "No, but only because no diet can ever truly be called "
                     "balanced.", "correct": False,
             "why": "The reason is not that balance is unattainable — it is "
                    "that a balanced plate can still fail to be absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-s30",
        "band": "standard",
        "text": "Explain why a food that is high in energy is not necessarily "
                "a nutritionally adequate food.",
        "options": [
            {"text": "Because energy content and nutrient content always vary "
                     "in exactly opposite directions, which is why food "
                     "labels give both numbers separately.", "correct": False,
             "why": "There is no such rule linking energy and nutrient "
                    "content — the point is only that energy is one measure "
                    "among seven, not a proxy for all of them."},
            {"text": "It is not true — a high-energy food is always "
                     "nutritionally adequate.", "correct": False,
             "why": "Energy tells you about only three of the seven "
                    "nutrients. A food can be high in energy and still miss "
                    "the other four entirely."},
            {"text": "Because energy is carried by only three of the seven "
                     "nutrients, so a high-energy food can still miss the "
                     "other four.", "correct": True},
            {"text": "Because high-energy foods are always digested more "
                     "slowly than low-energy foods.", "correct": False,
             "why": "Digestion speed is not the issue here — the point is "
                    "which nutrients the food actually supplies, not how "
                    "quickly."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-04-h08",
        "band": "harder",
        "text": "Two children each suffer a severe energy shortfall for a "
                "year: one at age four, the other at age fourteen. Both then "
                "have reliable food access for the rest of their childhood. "
                "Using the lesson's own claim about children, predict which "
                "is more likely to show a lasting effect on height.",
        "options": [
            {"text": "The four-year-old, since a shortfall during a period "
                     "of childhood growth carries the risk the lesson names.",
             "correct": True},
            {"text": "It cannot differ by age at all, since growth stops "
                     "identically in every child during a shortfall.",
             "correct": False,
             "why": "The lesson names childhood specifically as the period "
                    "where the growth effect may not be recoverable, which "
                    "implies age matters, not that it is irrelevant."},
            {"text": "Neither — the lesson guarantees full recovery for any "
                     "child given enough food afterwards, whatever their age "
                     "happened to be at the time.", "correct": False,
             "why": "The lesson states the growth effect in a child may not "
                    "be recoverable — it does not guarantee full catch-up "
                    "once food improves."},
            {"text": "The fourteen-year-old, because older children need "
                     "more energy overall.", "correct": False,
             "why": "Needing more energy is not the same as being more "
                    "vulnerable to a lasting growth effect — the lesson gives "
                    "no basis for that comparison."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h09",
        "band": "harder",
        "text": "A family, desperate to help a severely malnourished relative "
                "recover quickly, offers them three large meals on the very "
                "first day home. A nurse intervenes and insists on small, "
                "frequent amounts instead. Evaluate the family's plan and "
                "the nurse's correction.",
        "options": [
            {"text": "The family's plan is correct — more food, sooner, "
                     "always speeds recovery from a shortfall.", "correct": False,
             "why": "The lesson states the opposite: restarting food too "
                    "fast after prolonged starvation is itself dangerous, "
                    "whatever the intention behind it."},
            {"text": "The nurse is right to intervene: refeeding after "
                     "prolonged starvation is dangerous if it is too fast, "
                    "regardless of good intentions.", "correct": True},
            {"text": "Both are equally reasonable, since the danger the "
                     "lesson names only applies to hospital settings.",
             "correct": False,
             "why": "The danger of fast refeeding is a physiological one, not "
                    "one tied to the setting — it applies wherever refeeding "
                    "happens too quickly."},
            {"text": "The nurse is wrong, because slowing food down after a "
                     "shortfall only prolongs the recovery unnecessarily, "
                     "with no medical benefit to the patient at all.",
             "correct": False,
             "why": "The lesson names the fast route, not the slow one, as "
                    "the dangerous choice — gradual refeeding is the correct "
                    "medical approach."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h10",
        "band": "harder",
        "text": "A cereal is advertised as supplying “100% of every vitamin "
                "and mineral you need.” A patient with an absorption disorder "
                "eats it daily and remains deficient in several vitamins. "
                "Explain why the advert's claim does not protect this "
                "patient.",
        "options": [
            {"text": "The patient must be eating far less cereal than they "
                     "report.", "correct": False,
             "why": "Nothing in the case suggests under-reporting — the "
                    "explanation given is a failure of absorption, as in "
                    "clinic 5's post-surgery patient."},
            {"text": "Vitamins in cereal are destroyed by stomach acid before "
                     "they can ever be used.", "correct": False,
             "why": "The lesson gives no such general claim about cereal "
                    "vitamins and stomach acid — the mechanism at issue is "
                    "this patient's specific absorption disorder."},
            {"text": "The claim guarantees what reaches the plate, but says "
                     "nothing about whether it is absorbed into the blood.",
             "correct": True},
            {"text": "The cereal's claim must be false advertising, since "
                     "eating it should make any deficiency medically "
                     "impossible for anyone who eats it regularly.",
             "correct": False,
             "why": "The claim can be true of what the cereal contains while "
                    "still failing this patient, because absorption is a "
                    "separate step the claim says nothing about."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h11",
        "band": "harder",
        "text": "Lind's trial used one pair of patients per treatment rather "
                "than repeating each treatment on many patients. Explain "
                "why that is a real weakness of the design, and why it does "
                "not by itself overturn the citrus result.",
        "options": [
            {"text": "It is not a weakness at all — two patients is exactly "
                     "as reliable as any larger number.", "correct": False,
             "why": "A pair per treatment is genuinely a small sample, which "
                    "is a real limitation on how confident any single trial "
                    "like this can be."},
            {"text": "It is a fatal weakness, and the citrus result should "
                     "be treated as unproven even today.", "correct": False,
             "why": "The result has since been confirmed far beyond Lind's "
                    "original small trial, so the original weakness no longer "
                    "leaves the conclusion in doubt."},
            {"text": "It is a weakness only because Lind personally did not "
                     "believe his own result.", "correct": False,
             "why": "Lind's own doubt is a separate issue from the sample "
                    "size — the small-sample weakness exists independently of "
                    "what Lind himself believed."},
            {"text": "It is a weakness because two patients cannot rule out "
                     "coincidence as cleanly as a larger group could; it does "
                     "not overturn the result because the effect was clear "
                     "and has since been repeatedly confirmed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h12",
        "band": "harder",
        "text": "An adult has a long-term energy surplus, gaining mass "
                "steadily for years on a diet of processed, low-variety "
                "food, and is also found to have an iron deficiency. "
                "Explain how both can be true of the same person at once.",
        "options": [
            {"text": "Energy intake and a specific nutrient are separate "
                     "questions, so a diet can supply too much energy while "
                     "still missing iron.", "correct": True},
            {"text": "The iron deficiency must be a misdiagnosis, since it "
                     "would need the person to be losing mass instead of "
                     "steadily gaining it over the years described.",
             "correct": False,
             "why": "Anaemia is diagnosed from haemoglobin, not from body "
                    "mass — mass gain and low iron are not contradictory "
                    "findings."},
            {"text": "The energy surplus must have used up the person's iron "
                     "stores directly.", "correct": False,
             "why": "An energy surplus is stored as lipid; it has no "
                    "mechanism for consuming iron. The two are simply "
                    "independent shortfalls in different nutrients."},
            {"text": "They cannot both be true — a surplus of energy always "
                     "rules out any deficiency.", "correct": False,
             "why": "Energy and a specific nutrient are separate questions. "
                    "A diet can supply too much energy and still miss a "
                    "nutrient like iron entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h13",
        "band": "harder",
        "text": "Compare the consequences named for a long-term energy "
                "surplus (raised risk of type 2 diabetes, high blood "
                "pressure, heart disease, joint damage) with those named for "
                "a long-term shortfall (growth arrest, weakened immunity, "
                "difficulty maintaining temperature). What single fact best "
                "explains why the two lists do not overlap?",
        "options": [
            {"text": "The lists differ only because one imbalance affects "
                     "children and the other affects adults exclusively, "
                     "with no overlap ever occurring between the two groups "
                     "at any age.", "correct": False,
             "why": "Neither imbalance is restricted to one age group in the "
                    "lesson — the difference comes from the mechanism, "
                    "excess versus shortage, not from age."},
            {"text": "They are opposite imbalances that never overlap, since "
                     "the body is coping with an excess of stored energy in "
                     "one case and a lack of energy and resources in the "
                     "other.", "correct": True},
            {"text": "The two lists overlap almost completely once minor "
                     "wording differences are ignored.", "correct": False,
             "why": "The two lists name different conditions entirely — "
                    "diabetes and joint damage are not the same thing as "
                    "growth arrest or weakened immunity."},
            {"text": "Only the shortfall list is real; the surplus "
                     "consequences are risks rather than genuine effects.",
             "correct": False,
             "why": "Both lists are genuine consequences of their imbalance — "
                    "the surplus risks are described as probabilities rather "
                    "than certainties, but they are real all the same."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h14",
        "band": "harder",
        "text": "A patient reports feeling tired and achy for weeks and "
                "self-diagnoses “just stress,” delaying a visit to a doctor. "
                "Evaluate the risk in that reasoning, given what the lesson "
                "says about early deficiency signs.",
        "options": [
            {"text": "There is no risk, because a deficiency always produces "
                     "an obvious, unmistakable sign long before it could be "
                     "confused with ordinary stress.", "correct": False,
             "why": "The lesson's point is closer to the reverse — a "
                    "deficiency is easy to miss precisely because its early "
                    "signs are so unspecific."},
            {"text": "There is no risk — tiredness and aching are never "
                     "signs of anything serious.", "correct": False,
             "why": "The lesson names exactly these signs — tiredness, "
                    "aching, slow healing, low mood — as some of the least "
                    "specific symptoms in medicine, which is why they matter."},
            {"text": "The risk is real: these are described as some of the "
                     "least specific symptoms in medicine, so a genuine "
                    "deficiency can be mistaken for stress and go untreated.",
             "correct": True},
            {"text": "The risk only applies to people with an already "
                     "diagnosed illness.", "correct": False,
             "why": "Nothing in the lesson restricts this warning to people "
                    "already diagnosed — the point is that these signs are "
                    "non-specific for anyone."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h15",
        "band": "harder",
        "text": "At what point, precisely, does the normal storage of some "
                "surplus energy as lipid actually become “obesity”?",
        "options": [
            {"text": "The instant any lipid at all is stored, however "
                     "briefly.", "correct": False,
             "why": "Storage on its own is described as a normal, healthy "
                    "mechanism — it is not the moment the lesson calls "
                    "obesity."},
            {"text": "Once a person's body mass passes a fixed number on a "
                     "chart.", "correct": False,
             "why": "The lesson's own argument rejects judging this by a "
                    "fixed appearance or number — it reasons from the "
                    "duration and size of the imbalance instead."},
            {"text": "There is no such moment — the lesson treats storage and "
                     "obesity as exactly the same thing throughout.",
             "correct": False,
             "why": "The lesson distinguishes them clearly: storage itself is "
                    "normal, and the size of the store over a long period is "
                    "what becomes the problem."},
            {"text": "Once the store keeps growing over months or years, "
                     "reaching a size that raises health risks.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h16",
        "band": "harder",
        "text": "A doctor treating obesity considers “supplying a missing "
                "nutrient,” the remedy that works for a deficiency disease. "
                "Explain why that approach cannot treat obesity.",
        "options": [
            {"text": "Because obesity is a stored energy surplus, not a "
                     "missing nutrient, so supplying a nutrient can never "
                     "fix it — the two are different problems.",
             "correct": True},
            {"text": "Because no nutrient exists that could ever be supplied "
                     "to a patient with obesity.", "correct": False,
             "why": "The issue is not that no nutrient exists to give — it is "
                    "that obesity's cause is a surplus, not an absence, so "
                    "supplying something does not address it."},
            {"text": "Because deficiency diseases and obesity are actually "
                     "the same imbalance viewed from two different angles on "
                     "one underlying process the body manages.",
             "correct": False,
             "why": "They are opposite kinds of imbalance — a deficiency is "
                    "one nutrient missing, obesity is a long-term energy "
                    "surplus."},
            {"text": "Because supplying a nutrient always makes an energy "
                     "surplus larger, never smaller.", "correct": False,
             "why": "The lesson does not claim supplying a nutrient worsens a "
                    "surplus — the point is that it targets the wrong kind of "
                    "problem altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h17",
        "band": "harder",
        "text": "Rickets appeared historically in smoke-darkened industrial "
                "cities and can still appear today in children who spend "
                "almost all their time indoors. What single mechanism links "
                "these two very different situations?",
        "options": [
            {"text": "There is no shared mechanism — the two cases are "
                     "unrelated coincidences that happen to share a name.",
             "correct": False,
             "why": "Both trace to the same underlying failure: not enough "
                    "sunlight reaching skin to make vitamin D, whatever the "
                    "reason for that in each case."},
            {"text": "In both cases, skin is not making enough vitamin D "
                     "because sunlight is not reaching it.", "correct": True},
            {"text": "Both situations are actually caused by a shortage of "
                     "iron rather than vitamin D.", "correct": False,
             "why": "Rickets is specifically the vitamin D deficiency disease "
                    "— an iron shortage causes anaemia, a different "
                    "condition."},
            {"text": "Both are caused by a long-term energy shortfall, "
                     "regardless of sunlight exposure.", "correct": False,
             "why": "Rickets is a deficiency disease independent of energy "
                    "intake — the shared mechanism here is a lack of "
                    "sunlight reaching the skin, not an energy shortfall."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h18",
        "band": "harder",
        "text": "An elite athlete eats around 20 000 kJ a day, far above an "
                "average adult's requirement, and is diagnosed with a "
                "vitamin deficiency. Is this surprising, given the lesson's "
                "central argument?",
        "options": [
            {"text": "No, but only because elite athletes always eat "
                     "specially formulated food.", "correct": False,
             "why": "The reasoning does not depend on what kind of food is "
                    "eaten — it rests on the general principle that energy "
                    "and a specific nutrient are separate."},
            {"text": "Yes — an intake that high should make any deficiency "
                     "impossible.", "correct": False,
             "why": "The lesson's whole argument is that energy intake and a "
                    "specific nutrient are separate questions — a very high "
                    "intake does not guarantee every nutrient is covered."},
            {"text": "No — energy intake and a specific nutrient are separate "
                     "questions, so even a very high intake can still miss "
                     "one nutrient.", "correct": True},
            {"text": "Yes, because athletes are described in the lesson as "
                     "immune to deficiency diseases.", "correct": False,
             "why": "The lesson makes no such claim about athletes — the "
                    "general principle it states applies to anyone, whatever "
                    "their energy intake."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h19",
        "band": "harder",
        "text": "Ranking recovery speed once treatment begins, where would "
                "you place a deficiency disease, a long-term energy "
                "surplus and a long-term energy shortfall, and why?",
        "options": [
            {"text": "All three recover at exactly the same rate, since they "
                     "are all just imbalances in the same diet with no real "
                     "differences between how each one is treated.",
             "correct": False,
             "why": "The lesson gives very different remedies for the three — "
                    "supplying one nutrient, a lasting balance change, and "
                    "careful refeeding — which implies different speeds, not "
                    "the same one."},
            {"text": "Surplus fastest, since removing the excess food from "
                     "the diet reverses a stored surplus almost "
                     "immediately.", "correct": False,
             "why": "The lesson describes shifting a surplus as slow, because "
                    "the store took a long time to build — it is not "
                    "reversed quickly."},
            {"text": "Shortfall fastest, since any food at all reverses the "
                     "shortfall the moment it becomes available again.",
             "correct": False,
             "why": "The lesson warns that fast refeeding after a shortfall "
                    "is itself dangerous — recovery has to be gradual, not "
                    "immediate."},
            {"text": "Deficiency fastest, since only one nutrient has to be "
                     "supplied; surplus slowest, since a store built over "
                     "years takes a lasting change to shift; shortfall in "
                     "between, needing careful, gradual refeeding.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h20",
        "band": "harder",
        "text": "Is a patient diagnosed with obesity, by the lesson's own "
                "definition of malnutrition, also malnourished?",
        "options": [
            {"text": "Yes — malnutrition is never limited to going short of "
                     "food; it covers all three imbalances, and obesity is a "
                     "long-term energy surplus.", "correct": True},
            {"text": "It cannot be answered without knowing the patient's "
                     "exact body mass.", "correct": False,
             "why": "Body mass is not what settles this — the definition of "
                    "malnutrition covers the type of imbalance, and obesity "
                    "is named as one of the three."},
            {"text": "No, because malnutrition and obesity are treated as "
                     "two completely separate diagnoses, each requiring its "
                     "own unrelated kind of treatment.", "correct": False,
             "why": "The lesson treats obesity as one of the three forms "
                    "malnutrition can take, not as something separate from "
                    "it."},
            {"text": "No — malnutrition only ever refers to going short of "
                     "food.", "correct": False,
             "why": "That is exactly the misconception the lesson confronts. "
                    "Malnutrition means the balance is wrong, and obesity is "
                    "one of the three ways it can be."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h21",
        "band": "harder",
        "text": "The Navy took another forty years after Lind's trial to "
                "adopt lemon juice as policy. Lind himself doubted his own "
                "result and went on to recommend a boiled concentrate, "
                "which did not work. Suggest the best explanation for the "
                "delay.",
        "options": [
            {"text": "The Navy had already adopted a different, equally "
                     "effective treatment in the meantime, and simply took "
                     "forty years to write the policy down.",
             "correct": False,
             "why": "No effective alternative existed — the boiled "
                    "concentrate Lind recommended is precisely the remedy "
                    "that failed."},
            {"text": "Lind's own doubt, and a failed alternative remedy "
                     "carrying his name, are likely to have undermined "
                     "confidence in the correct conclusion.",
             "correct": True},
            {"text": "Nothing here could explain the delay, so it must have "
                     "been pure chance.", "correct": False,
             "why": "There is a clear clue to work from: the researcher "
                    "doubting his own finding, and publicly backing a "
                    "remedy that failed."},
            {"text": "Citrus fruit was unavailable anywhere in Britain "
                     "until forty years later.", "correct": False,
             "why": "Citrus was reaching British ports throughout that "
                    "period. The delay is better explained by doubt about "
                    "the finding than by any shortage of fruit."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h22",
        "band": "harder",
        "text": "Two patients eat exactly the same daily energy intake. One "
                "eats a diet the lesson would call balanced; the other eats "
                "mostly processed food of equal energy value. Only the "
                "second is later diagnosed with a deficiency disease. What "
                "does identical energy intake tell you about their risk of "
                "deficiency?",
        "options": [
            {"text": "That the second patient's diagnosis must be a "
                     "measurement error, since equal energy intake should "
                     "mean identical outcomes for both people involved.",
             "correct": False,
             "why": "There is no reason to doubt the diagnosis — the case "
                    "illustrates precisely that energy and nutrient adequacy "
                    "are separate."},
            {"text": "That processed food always supplies less energy than "
                     "fresh food of the same size.", "correct": False,
             "why": "The case states the energy values are equal — the "
                    "difference lies in nutrient content, not in energy."},
            {"text": "Nothing on its own — energy intake is a separate "
                     "question from which of the seven nutrients a diet "
                     "actually supplies.", "correct": True},
            {"text": "That both patients must be at exactly equal risk, "
                     "since their energy intakes match.", "correct": False,
             "why": "Matching energy intake does not mean matching nutrient "
                    "content — the second patient's diet supplied less of "
                    "something the first patient's did not."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h23",
        "band": "harder",
        "text": "The lesson says supplying the missing nutrient is “often” a "
                "fast, complete recovery from a deficiency disease. Why does "
                "the word “often” matter here, rather than “always”?",
        "options": [
            {"text": "It does not matter at all — “often” and “always” mean "
                     "exactly the same thing in this sentence.", "correct": False,
             "why": "The two words make different claims: “always” would "
                    "promise a guaranteed outcome, while “often” leaves room "
                    "for exceptions."},
            {"text": "Because deficiency diseases are never actually treated "
                     "successfully at all.", "correct": False,
             "why": "The lesson describes deficiency treatment as often fast "
                    "and complete — the word “often” qualifies how reliably "
                    "that happens, not whether it ever does."},
            {"text": "Because it shows genuine uncertainty about whether "
                     "deficiency diseases are treatable in principle, not "
                     "merely about how quickly they typically respond.",
             "correct": False,
             "why": "The lesson is not expressing doubt about treatability in "
                    "principle — it is being precise that most, not "
                    "necessarily every, case recovers this way."},
            {"text": "Because it leaves room for cases where recovery is "
                     "slower or incomplete, rather than promising a "
                     "guaranteed outcome for every patient.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h24",
        "band": "harder",
        "text": "Two patients have identical body mass. One has a long-term "
                "energy surplus with no deficiency; the other has a normal "
                "energy balance but a hidden vitamin deficiency. Explain why "
                "body mass alone cannot distinguish them.",
        "options": [
            {"text": "Because a deficiency can occur at any level of energy "
                     "intake, so it leaves no reliable mark on body mass at "
                     "all.", "correct": True},
            {"text": "It can distinguish them — the patient with the "
                     "deficiency will always weigh visibly less.",
             "correct": False,
             "why": "The lesson is explicit that a deficiency can occur at "
                    "any level of energy intake, including one that keeps "
                    "mass entirely normal."},
            {"text": "Because both patients must actually have the same "
                     "underlying imbalance, despite the different diagnoses "
                     "each of them has been given by their own doctor.",
             "correct": False,
             "why": "The two diagnoses describe genuinely different "
                    "imbalances — one is an energy surplus, the other a "
                    "missing nutrient — even though the mass reading is the "
                    "same."},
            {"text": "Because body mass measurements are always unreliable "
                     "and should never be used at all.", "correct": False,
             "why": "The issue is not that mass measurement itself is "
                    "unreliable — it is that mass alone cannot reveal which "
                    "kind of imbalance, if any, is present."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h25",
        "band": "harder",
        "text": "A patient takes a general multivitamin daily but the dose of "
                "one particular mineral in it is far below what their body "
                "actually needs, and they remain deficient in that mineral. "
                "Evaluate the claim “taking a supplement guarantees a "
                "deficiency is fixed.”",
        "options": [
            {"text": "The claim cannot be evaluated without knowing the "
                     "patient's total energy intake.", "correct": False,
             "why": "Energy intake is unrelated to whether a supplement's "
                    "dose of one mineral is adequate — the two are separate "
                    "questions."},
            {"text": "The claim is false as stated — supplying some of a "
                     "nutrient is not the same as supplying enough of it.",
             "correct": True},
            {"text": "The claim is true — any supplement containing a "
                     "nutrient removes any deficiency in it completely.",
             "correct": False,
             "why": "This case shows the opposite: the mineral is present in "
                    "the supplement, but the dose is too low to fix the "
                    "deficiency."},
            {"text": "The claim is true, but only because this patient must "
                     "be taking the supplement incorrectly.", "correct": False,
             "why": "Nothing in the case suggests misuse — the stated problem "
                    "is that the dose itself is too low for this patient's "
                    "needs."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h26",
        "band": "harder",
        "text": "Rickets can occur in a fed child in a smoky city, and it can "
                "also occur in a starving child during a famine. Explain how "
                "both routes lead to the same disease.",
        "options": [
            {"text": "Both cases are actually caused by the same energy "
                     "shortfall, whatever the setting.", "correct": False,
             "why": "The fed city child is not in an energy shortfall at "
                    "all — the shared cause is a lack of vitamin D, reached "
                    "by two different routes."},
            {"text": "Only the famine case is a genuine deficiency; the fed "
                     "child's rickets must have a different cause entirely, "
                     "unconnected to vitamin D or sunlight in any way.",
             "correct": False,
             "why": "Both are the same deficiency disease. Being fed does not "
                    "rule out a missing vitamin, which is exactly the case "
                    "the fed city child illustrates."},
            {"text": "Both routes end in too little vitamin D reaching the "
                     "child, whether the cause is blocked sunlight or a lack "
                     "of food supplying it.", "correct": True},
            {"text": "They do not really lead to the same disease — one case "
                     "must actually be a misdiagnosis.", "correct": False,
             "why": "Both are genuinely rickets — a deficiency can arise by "
                    "more than one route, since it is a question of the "
                    "nutrient's supply, not of energy intake."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h27",
        "band": "harder",
        "text": "A patient with obesity tries a strict diet for one week and "
                "is disappointed that their long-term health risks have not "
                "measurably fallen. Using the lesson's own timescale claims, "
                "explain why one week was never likely to be enough.",
        "options": [
            {"text": "Because one week is too short for any diet to reduce "
                     "energy intake at all.", "correct": False,
             "why": "The issue is not whether intake fell in that week — it "
                    "is that the store itself took a long time to build, so "
                    "shifting it takes a comparably long change."},
            {"text": "Because health risks from obesity are permanent and "
                     "cannot be reduced by any change in balance, however "
                     "long that change is kept up for afterwards.",
             "correct": False,
             "why": "The lesson describes the risks as linked to a surplus "
                    "that can be changed — what it takes time is a lasting "
                    "shift in balance, not permanence of the risk."},
            {"text": "Because a week-long diet always increases the size of "
                     "the lipid store instead of reducing it, however strict "
                     "or well-planned that diet happens to be.",
             "correct": False,
             "why": "A genuine reduction in intake would work in the right "
                    "direction — the problem is only that one week is too "
                    "short to measurably shift a store built over years."},
            {"text": "Because the store was built up over months or years, "
                     "so only a lasting change over a comparable timescale "
                     "can shift it — not one week.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h28",
        "band": "harder",
        "text": "A doctor says: “His BMI reading is exactly average, so his "
                "diet must be fine.” Evaluate this reasoning against the "
                "lesson's own argument about appearance and diet.",
        "options": [
            {"text": "It is flawed for the same reason judging diet by "
                     "appearance is flawed — a numeric measure of mass still "
                     "says nothing about whether any specific nutrient is "
                     "missing.", "correct": True},
            {"text": "It is sound reasoning, because BMI is a precise number, "
                     "and precise numbers are exactly what good medical "
                     "judgement is supposed to rely on most.", "correct": False,
             "why": "Being precise about mass does not make it evidence "
                    "about nutrient content — a deficiency can occur at any "
                    "level of energy intake, average BMI included."},
            {"text": "It is flawed only because BMI is calculated "
                     "incorrectly in most patients.", "correct": False,
             "why": "The flaw is not in how BMI is calculated — it is that "
                    "any single mass-based measure cannot reveal a missing "
                    "nutrient."},
            {"text": "It is sound reasoning as long as the patient also "
                     "reports feeling well.", "correct": False,
             "why": "Early deficiency signs are described as some of the "
                    "least specific in medicine — feeling well is not "
                    "reliable evidence against a deficiency either."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h29",
        "band": "harder",
        "text": "One patient with fatigue turns out to have iron-deficiency "
                "anaemia; another patient with the same complaint of fatigue "
                "turns out to have early rickets. What does this pair show "
                "about diagnosing from a single shared symptom like "
                "fatigue?",
        "options": [
            {"text": "That fatigue is not a real symptom of either "
                     "condition.", "correct": False,
             "why": "Fatigue is named among the least specific early signs of "
                    "a deficiency — it is real, just not diagnostic on its "
                    "own."},
            {"text": "That fatigue alone can never identify which nutrient, "
                     "if any, is missing — the full pattern of signs and "
                     "tests is needed.", "correct": True},
            {"text": "That fatigue always means iron is missing, and the "
                     "rickets diagnosis in the second patient must therefore "
                     "be a mistake.", "correct": False,
             "why": "Both diagnoses can be genuine — fatigue is one of the "
                    "least specific signs in medicine, shared by more than "
                    "one deficiency."},
            {"text": "That the two patients must actually have identical "
                     "underlying deficiencies.", "correct": False,
             "why": "They are diagnosed with two different deficiencies — "
                    "iron for one, vitamin D for the other — despite sharing "
                    "one symptom."},
        ],
        "figure": None,
    },
    {
        "id": "b3-04-h30",
        "band": "harder",
        "text": "A food label states its energy value in kJ per portion and "
                "nothing else. Using the three-imbalance framework, explain "
                "why that single number can never tell you whether the food "
                "is “healthy.”",
        "options": [
            {"text": "Because a high-energy food is always the healthier "
                     "choice regardless of its other nutrients, its overall "
                     "balance, or how well the body absorbs any of them.",
             "correct": False,
             "why": "The lesson gives no reason to think higher energy makes "
                    "a food healthier — a food can be high in energy and "
                    "still miss nutrients that carry none."},
            {"text": "It is not true — the energy value on its own is enough "
                     "to judge whether a food is healthy.", "correct": False,
             "why": "Energy value alone cannot show whether the other four "
                    "non-energy-carrying nutrients are adequately supplied."},
            {"text": "Because energy is carried by only three of the seven "
                     "nutrients, so the label says nothing about whether the "
                     "other four are present at all.", "correct": True},
            {"text": "Because the kJ value on a label is usually measured "
                     "incorrectly.", "correct": False,
             "why": "The problem is not accuracy of the number — it is that "
                    "energy alone cannot speak to vitamins, minerals or "
                    "fibre content."},
        ],
        "figure": None,
    },
]
