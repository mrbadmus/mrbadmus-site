"""B3 lesson 02 — Food tests: twelve questions (MRB-269).

The lesson teaches four reagents and one habit of mind: a colour change
answers exactly one question, and a negative is a fact about the test rather
than about the food. The bank probes both. The easier band checks that the
right reagent is paired with the right method and the right colour, and that a
tube which has not changed is a reported result rather than a broken test. The
standard band puts the student in front of the situations the bench already
showed them — the under-heated milk, the emulsion poured the wrong way round,
the blue tube of olive oil, the orange-brown apple juice — and asks what the
result licenses. The harder band takes the ideas somewhere the lesson did not
go: a tube of caster sugar that is nothing but sugar and still reads negative,
a label that a negative can never confirm, and what a laboratory has to fix
before a colour is allowed to mean an amount.

Both declared misconceptions supply distractors throughout. DIET-04 ("the
deeper the colour, the more of the nutrient there was") drives the "redder
tube, more sugar" option in s01, the "heat every tube longer" and "stronger
Benedict's" options in h04, and the quantity claims in e03 and s03. DIET-05 ("a
negative result proves the nutrient is not there") drives the "true negative"
option in e03, the flat "there is no starch in apple juice" in s04, and both
"yes" options in h03. Two further errors the lesson exists to correct supply
the rest: that an unchanged tube means the test failed or the reagent had gone
off (e02, e03, s04, h01), and that a food test says something about health
(h02). h01's distractors are the false-negative reflex misapplied — the tube is
loaded with sugar, and the problem is the kind of sugar, not the amount.

`figure` is None throughout: this lesson declares no figures.
"""

UNIT = "B3"
LESSON = "food-tests"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-02-e01",
        "band": "easier",
        "text": "You want to find out whether a sample contains starch. Which "
                "reagent do you use, and does the tube need heating?",
        "options": [
            {"text": "Benedict's solution, heated in a water bath at 80 °C.",
             "correct": False,
             "why": "Benedict's is the one test on this bench that needs "
                    "heating, but it detects reducing sugar, not starch. Right "
                    "method, wrong question."},
            {"text": "Iodine solution, a few drops straight on, no heating.",
             "correct": True},
            {"text": "Iodine solution, heated in a water bath at 80 °C.",
             "correct": False,
             "why": "Right reagent, wrong method. Iodine works cold — a few "
                    "drops onto the food and the blue-black comes up within "
                    "seconds. Only Benedict's goes in the water bath."},
            {"text": "Biuret solution, a few drops straight on, no heating.",
             "correct": False,
             "why": "Biuret is cold, which is the half you have right, but it "
                    "detects protein. Each reagent answers one question and no "
                    "others."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e02",
        "band": "easier",
        "text": "Four tubes are lined up on the bench. Which one is showing a "
                "positive result?",
        "options": [
            {"text": "A Benedict's tube that has stayed the blue it started as.",
             "correct": False,
             "why": "Blue is Benedict's own colour before anything happens. A "
                    "tube that has not changed is reporting 'not detected' — a "
                    "positive is brick red."},
            {"text": "An iodine tube that has gone from orange-brown to "
                     "blue-black.",
             "correct": True},
            {"text": "A Biuret tube that has stayed the blue it started as.",
             "correct": False,
             "why": "Biuret starts blue too, which is why an unchanged Biuret "
                    "tube catches people out. A positive is lilac purple."},
            {"text": "An emulsion tube that has stayed clear all the way down.",
             "correct": False,
             "why": "Clear is what ethanol poured into water looks like when "
                    "there is no lipid to come out of it. A positive is a "
                    "cloudy white."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e03",
        "band": "easier",
        "text": "Apple juice contains a little under 0.3% protein. Tested with "
                "Biuret it stays blue. What is a result like that called?",
        "options": [
            {"text": "A false negative — the protein is there, but too little "
                     "to detect.",
             "correct": True},
            {"text": "A true negative — apple juice contains no protein at all.",
             "correct": False,
             "why": "The question tells you the protein is there. A negative "
                    "never proves a nutrient is absent; here you already know "
                    "it is present and the test still cannot see it."},
            {"text": "An anomaly — the test went wrong and should be repeated.",
             "correct": False,
             "why": "Nothing went wrong. The method was followed correctly and "
                    "still showed nothing, and repeating it would give the same "
                    "blue tube. That is exactly what a false negative is."},
            {"text": "A qualitative result — the protein level is below 0.3%.",
             "correct": False,
             "why": "Qualitative means 'present or not detected' and never a "
                    "level. A blue tube reports no number at all, so it cannot "
                    "put the protein below anything."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e04",
        "band": "easier",
        "text": "The safety note says no Bunsen may be alight while ethanol is "
                "open on the bench. Why?",
        "options": [
            {"text": "The flame would heat the ethanol and stop it dissolving "
                     "the lipid.",
             "correct": False,
             "why": "The Bunsen is banned here for safety, not for chemistry. "
                    "Ethanol catches fire easily, and the flame does not have "
                    "to touch it."},
            {"text": "Ethanol is an irritant, and heating it makes the fumes "
                     "worse.",
             "correct": False,
             "why": "Two hazards swapped. The irritants on this bench are "
                    "Benedict's and Biuret, and Biuret contains sodium "
                    "hydroxide. Ethanol's hazard is that it is highly "
                    "flammable."},
            {"text": "Benedict's needs exactly 80 °C, and a Bunsen flame is far "
                     "too hot.",
             "correct": False,
             "why": "True of the water bath, but that is a different tube. The "
                    "Bunsen rule is about the open ethanol, and it applies even "
                    "when nobody is heating anything."},
            {"text": "Ethanol catches fire very easily, and a flame nearby "
                     "could set it alight.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-02-s01",
        "band": "standard",
        "text": "Two tubes are poured from the same bottle of milk. One is "
                "heated with Benedict's for thirty seconds and comes out "
                "orange; the other is heated for five minutes and comes out "
                "brick red. A student writes: 'the second tube had more sugar "
                "in it.' What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — a redder tube always means more sugar "
                     "was present.",
             "correct": False,
             "why": "This is the belief the lesson exists to break. Colour does "
                    "move towards brick red with more sugar, but it moves that "
                    "way with longer heating too, so a redder tube on its own "
                    "is not evidence of more sugar."},
            {"text": "The heat made more sugar form, so the second tube really "
                     "did have more.",
             "correct": False,
             "why": "Heating does not create sugar. The lactose was in the milk "
                    "before either tube went in the bath — what changed is how "
                    "far the reaction was allowed to get."},
            {"text": "Both tubes came from the same milk — the second was "
                     "simply heated for longer.",
             "correct": True},
            {"text": "Orange is not a Benedict's colour, so the first tube must "
                     "have been contaminated.",
             "correct": False,
             "why": "Benedict's moves through green, yellow and orange on its "
                    "way to brick red. An orange tube is a real result, just a "
                    "partly developed one."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s02",
        "band": "standard",
        "text": "You are given a sample of cream and asked to test it for "
                "lipid. Which method is the right one?",
        "options": [
            {"text": "Shake it with ethanol, let it settle, then pour the "
                     "ethanol into water and look for a cloudy white.",
             "correct": True},
            {"text": "Shake it with ethanol, let it settle, and look for the "
                     "ethanol layer itself to turn cloudy white.",
             "correct": False,
             "why": "Nothing shows in the ethanol — the lipid dissolves in it "
                    "and stays clear. The cloud only appears when that ethanol "
                    "is poured into water and the lipid comes back out."},
            {"text": "Shake it with ethanol, then heat the tube in a water bath "
                     "at 80 °C for five minutes.",
             "correct": False,
             "why": "You have borrowed Benedict's method. The emulsion test is "
                    "done cold, and heating open ethanol is the one thing the "
                    "safety note forbids."},
            {"text": "Pour it straight into a test tube of water and look for a "
                     "cloudy white layer.",
             "correct": False,
             "why": "Cream in water goes cloudy on its own, so this would come "
                    "out positive whatever was in the tube. The ethanol step is "
                    "what makes it a test rather than a mixture."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s03",
        "band": "standard",
        "text": "A student tests olive oil with Benedict's, gets a blue tube, "
                "and writes: 'olive oil has no energy in it.' Which correction "
                "is the right one?",
        "options": [
            {"text": "She is right — a blue Benedict's tube means there is no "
                     "energy in olive oil.",
             "correct": False,
             "why": "Olive oil carries more energy per gram than anything else "
                    "on the bench. A blue tube says one thing only: this test "
                    "did not detect reducing sugar."},
            {"text": "She should have heated the tube for longer, because olive "
                     "oil reacts slowly.",
             "correct": False,
             "why": "Heating longer will not conjure a nutrient that is not "
                    "being looked for. There is no reducing sugar in olive oil, "
                    "so the tube is right — her conclusion is not."},
            {"text": "She should write that olive oil holds less energy than "
                     "the other foods on the bench.",
             "correct": False,
             "why": "Softening it to a comparison does not rescue it. The test "
                    "reports no amount and no ranking — it cannot support "
                    "'less' any more than it supports 'none'."},
            {"text": "Benedict's only reports whether reducing sugar was "
                     "detected; it says nothing about energy.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s04",
        "band": "standard",
        "text": "Apple juice is tested with iodine and the tube stays "
                "orange-brown. Which conclusion is the only one this result "
                "supports?",
        "options": [
            {"text": "There is no starch in apple juice.",
             "correct": False,
             "why": "This may even be true — in a ripe apple the starch has all "
                    "been converted to sugar — but the orange tube is not what "
                    "tells you so. The result licenses 'not detected', and "
                    "nothing stronger."},
            {"text": "No starch was detected in apple juice under these "
                     "conditions.",
             "correct": True},
            {"text": "Apple juice contains sugar rather than starch.",
             "correct": False,
             "why": "One test answers one question. Benedict's is what would "
                    "tell you about sugar; the iodine tube on its own says "
                    "nothing whatever about it."},
            {"text": "The iodine solution failed to work on the apple juice.",
             "correct": False,
             "why": "An unchanged orange-brown is the test working and "
                    "reporting a negative. A negative feels like nothing "
                    "happened, but it is a result, not a failure."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-02-h01",
        "band": "harder",
        "text": "A student stirs a spoonful of caster sugar into water — "
                "nothing but sugar and water — and tests it with Benedict's. "
                "The tube stays blue. Why?",
        "options": [
            {"text": "There was too little sugar in the tube for the test to "
                     "detect any of it.",
             "correct": False,
             "why": "The false-negative reflex, used in the one place it does "
                    "not fit. That tube is loaded with sugar. The problem is "
                    "the kind of sugar, not how much of it there is."},
            {"text": "The sugar had dissolved, and Benedict's can only detect "
                     "undissolved sugar.",
             "correct": False,
             "why": "Every food on the bench is tested in solution — "
                    "dissolving is part of the method, not a barrier to it. "
                    "Glucose stirred into water goes brick red."},
            {"text": "Caster sugar is sucrose, a non-reducing sugar, so "
                     "Benedict's stays blue.",
             "correct": True},
            {"text": "The tube was not heated for long enough to reach brick "
                     "red.",
             "correct": False,
             "why": "Longer heating pushes a positive further along, but it "
                    "cannot start one. Sucrose cannot hand an electron to the "
                    "copper, so this tube would stay blue all afternoon."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h02",
        "band": "harder",
        "text": "A student tests protein shake powder with Biuret and gets "
                "lilac; he tests boiled rice with Biuret and gets blue. He "
                "concludes the shake is the healthier food. Where does his "
                "reasoning break down?",
        "options": [
            {"text": "No colour change is a judgement about health — only "
                     "about which nutrient was detected.",
             "correct": True},
            {"text": "His reasoning holds — the food with more nutrients "
                     "detected is the healthier one.",
             "correct": False,
             "why": "Counting positives is not a measure of health. Olive oil "
                    "gives one positive out of four and is a required "
                    "nutrient; a glucose solution gives one positive and is "
                    "nothing but fuel."},
            {"text": "He should have run all four tests on both foods before "
                     "comparing them.",
             "correct": False,
             "why": "Four tests would tell him which nutrients each food "
                    "contains, and still nothing about health. More of an "
                    "answer to the wrong question is not an answer."},
            {"text": "Rice gave a false negative, so the comparison was not a "
                     "fair one.",
             "correct": False,
             "why": "It may well be a false negative — rice does contain some "
                    "protein. But even a lilac rice tube would not make either "
                    "food healthy or unhealthy. That is a question these tests "
                    "cannot answer."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h03",
        "band": "harder",
        "text": "A packet claims the food inside contains no starch. You test "
                "it with iodine and the tube stays orange-brown. Can you "
                "confirm the claim on the packet?",
        "options": [
            {"text": "Yes — an orange-brown tube proves there is no starch in "
                     "the food.",
             "correct": False,
             "why": "A negative is a fact about your test, not about the food. "
                    "It tells you the starch was below what iodine can see "
                    "here, which is not the same as it being absent."},
            {"text": "Yes, provided you repeat the test three times and get "
                     "the same result each time.",
             "correct": False,
             "why": "Repeating a test that cannot see small amounts gives you "
                    "the same invisible amount three times over. Repeats "
                    "improve how reliable a result is, never how sensitive the "
                    "test is."},
            {"text": "No, because iodine only detects starch in solid food and "
                     "not in a solution.",
             "correct": False,
             "why": "Iodine works perfectly well on starch solution — that is "
                    "the standard method. The reason you cannot confirm the "
                    "claim is about what a negative means, not about the "
                    "sample."},
            {"text": "No — a negative shows only that this test did not detect "
                     "starch here.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h04",
        "band": "harder",
        "text": "A laboratory wants a Benedict's result that genuinely does "
                "tell you how much sugar was in the sample. What must they do "
                "that a school bench does not?",
        "options": [
            {"text": "Heat every tube for much longer, so that each colour "
                     "reaches its final shade.",
             "correct": False,
             "why": "Heating everything to the end drives every positive "
                    "towards the same brick red, wiping out the differences "
                    "you were trying to read — and still gives you no shade to "
                    "compare against."},
            {"text": "Use a more concentrated Benedict's solution, so that "
                     "small amounts of sugar still show up.",
             "correct": False,
             "why": "A stronger reagent may catch smaller amounts, but the "
                    "answer is still 'detected' or 'not detected'. Sensitivity "
                    "is not a scale."},
            {"text": "Fix the volume, temperature and time, and compare "
                     "against tubes of known sugar concentration.",
             "correct": True},
            {"text": "Repeat the test three times on each sample and take an "
                     "average of the colours.",
             "correct": False,
             "why": "Averaging three uncontrolled tubes gives an uncontrolled "
                    "average. Without fixed conditions and known standards "
                    "there is nothing for the colour to be measured against."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Nine further rows, three per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-02-e05",
        "band": "easier",
        "text": "Which reagent detects protein, and what colour change shows "
                "a positive result?",
        "options": [
            {"text": "Benedict's solution — blue to brick red.",
             "correct": False,
             "why": "That is the reducing-sugar test. Benedict's says nothing "
                    "about protein, because one test answers one question."},
            {"text": "Iodine solution — orange-brown to blue-black.",
             "correct": False,
             "why": "That is the starch test. A blue-black spot tells you "
                    "starch was detected and nothing at all about protein."},
            {"text": "Biuret solution — blue to lilac purple.",
             "correct": True},
            {"text": "Ethanol then water — clear to cloudy white.",
             "correct": False,
             "why": "That is the emulsion test, which detects lipid. Egg "
                    "white is almost pure protein and gives nothing on it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e06",
        "band": "easier",
        "text": "The four food tests all give their answer as a colour. What "
                "does a colour change tell you, and what does it never tell "
                "you?",
        "options": [
            {"text": "Which nutrient was detected — never how much of it is "
                     "there.", "correct": True},
            {"text": "How much of the nutrient is there — never which "
                     "nutrient it is.", "correct": False,
             "why": "That is the wrong way round. The reagent is chosen "
                    "because it answers about one named nutrient, and it "
                    "reports present or not detected."},
            {"text": "Whether the food is healthy — never which nutrient is "
                     "in it.", "correct": False,
             "why": "Nothing in a colour change is about health. Olive oil is "
                    "one positive out of four and is a required nutrient."},
            {"text": "Which nutrient is there, and roughly how much from the "
                     "depth of the colour.", "correct": False,
             "why": "Depth of colour also changes with heating time, volume "
                    "and concentration, none of which you controlled. A "
                    "deeper colour is not evidence of more nutrient."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e07",
        "band": "easier",
        "text": "Benedict's needs five minutes at 80 °C. Why does the method "
                "say to use a water bath rather than a Bunsen flame?",
        "options": [
            {"text": "A flame would take the tube far past 80 °C and destroy "
                     "the sugar in it.", "correct": False,
             "why": "The sugar is not destroyed by warming. The reason for "
                    "the water bath is a steady temperature and a bench with "
                    "no naked flame on it."},
            {"text": "Benedict's solution only reacts when it is surrounded "
                     "by water rather than air.", "correct": False,
             "why": "The reaction happens inside the tube and does not care "
                    "what is outside it. The water bath is there to hold the "
                    "temperature and to keep a flame off the bench."},
            {"text": "A Bunsen flame heats a test tube far too slowly ever to "
                     "reach 80 °C.", "correct": False,
             "why": "A Bunsen heats a tube quickly, and that is part of the "
                    "problem — it is hard to hold at 80 °C, and it is an open "
                    "flame beside ethanol."},
            {"text": "A water bath holds a steady 80 °C, and a naked flame is "
                     "a hazard on this bench.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-02-s05",
        "band": "standard",
        "text": "Raw potato tested with Benedict's gives a blue tube. The same "
                "potato, left in a warm cupboard for a fortnight, now gives a "
                "brick red. What has changed?",
        "options": [
            {"text": "Nothing about the potato — the second tube must have "
                     "been heated for longer.", "correct": False,
             "why": "Heating longer deepens a colour that was already "
                    "changing. It cannot turn a blue tube red, because it "
                    "cannot create reducing sugar that was not there."},
            {"text": "Some of the potato's starch has been broken down into "
                     "reducing sugar.", "correct": True},
            {"text": "The potato has taken in sugar from the air in the "
                     "cupboard while it sat there.", "correct": False,
             "why": "There is no sugar in air to take in. The sugar came from "
                    "the potato's own starch, which is what a fortnight in the "
                    "warm does to it."},
            {"text": "The first result was a false negative, and the sugar "
                     "was there all along.", "correct": False,
             "why": "A false negative means the substance is present but too "
                    "dilute to show. Here the food itself changed: raw potato "
                    "stores its carbohydrate as starch, not as free sugar."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s06",
        "band": "standard",
        "text": "Egg white tested with Benedict's stays blue. Potato tested "
                "with Biuret stays blue. Only one of those is a true negative. "
                "Which one, and how can you tell?",
        "options": [
            {"text": "The potato one — potato is a solid, and solids give the "
                     "more reliable negatives.", "correct": False,
             "why": "Being solid has nothing to do with it. Potato is about "
                    "2% protein, so its blue tube is a false negative: the "
                    "protein is there and Biuret cannot see it."},
            {"text": "Both of them — each tube was run correctly, so both "
                     "results must be true.", "correct": False,
             "why": "Following the method correctly is exactly how a false "
                    "negative is produced. Whether a negative is true depends "
                    "on the food, not on the care taken."},
            {"text": "Neither of them — a negative result can never be called "
                     "a true one.", "correct": False,
             "why": "True negatives are real: milk genuinely contains no "
                    "starch. A negative is only doubtful when the substance "
                    "is present but too dilute to show."},
            {"text": "The egg white one — it really has no sugar, while "
                     "potato really has protein.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s07",
        "band": "standard",
        "text": "Benedict's and Biuret are both run on a food solution rather "
                "than on the food itself. Why is a solid food crushed and "
                "mixed with water first?",
        "options": [
            {"text": "So the reagent reaches the whole sample — a lump can "
                     "test negative because nothing got inside it.",
             "correct": True},
            {"text": "Because a reagent can only work on a liquid, so a solid "
                     "food cannot be tested at all.", "correct": False,
             "why": "Solids are tested: iodine goes straight onto the food. "
                    "Crushing is about the reagent reaching the inside, not "
                    "about the food having to be liquid."},
            {"text": "Because crushing breaks the food molecules apart, and "
                     "that is what the reagent detects.", "correct": False,
             "why": "Crushing makes pieces smaller and leaves the molecules "
                    "exactly as they were. The reagent detects the molecules "
                    "that were already there."},
            {"text": "Because water dilutes the sample, and a diluted sample "
                     "gives a stronger colour.", "correct": False,
             "why": "Diluting a sample makes a colour weaker, not stronger, "
                    "and can push a real result below what the test can "
                    "detect."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-02-h05",
        "band": "harder",
        "text": "Two unlabelled white powders sit on the bench. One is starch "
                "and one is dried egg white. Which single test separates them, "
                "and what would you see?",
        "options": [
            {"text": "Biuret — the starch goes lilac purple and the egg white "
                     "stays blue.", "correct": False,
             "why": "That is the right test read backwards. Egg white is "
                    "almost pure protein and would go lilac; starch holds no "
                    "protein and would stay blue."},
            {"text": "Benedict's — both go brick red, and the shade tells the "
                     "two apart.", "correct": False,
             "why": "Neither is a reducing sugar, so both tubes stay blue. "
                    "And a shade is never evidence of an amount on a school "
                    "bench."},
            {"text": "Iodine — the starch goes blue-black and the egg white "
                     "stays orange-brown.", "correct": True},
            {"text": "The emulsion test — the starch goes cloudy white and "
                     "the egg white does not.", "correct": False,
             "why": "Neither powder holds lipid, so both would give a clear "
                    "tube. The emulsion test cannot separate two foods that "
                    "are both negative on it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h06",
        "band": "harder",
        "text": "Apple juice is under 0.3% protein. Group A tests it with "
                "Biuret and gets blue. Group B boils it down to a tenth of its "
                "volume first and gets a faint lilac. What has happened?",
        "options": [
            {"text": "Boiling has created protein in the juice, which is why "
                     "the second tube changed colour.", "correct": False,
             "why": "Boiling removes water and creates nothing. The same "
                    "protein is present in both tubes; only its concentration "
                    "differs."},
            {"text": "Concentrating the sample lifted the protein above the "
                     "level Biuret is able to detect.", "correct": True},
            {"text": "Group A must have made a mistake, because the correct "
                     "method always finds what is present.", "correct": False,
             "why": "Group A's method was correct and still gave a negative. "
                    "That is what a false negative is, and it is why a "
                    "negative is a fact about the test."},
            {"text": "The two groups tested different things, so their "
                     "results cannot be compared at all.", "correct": False,
             "why": "It is the same juice in both tubes. What changed is how "
                    "much water was in with the protein, which is the whole "
                    "point of the comparison."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h07",
        "band": "harder",
        "text": "A student runs all four food tests on one sample and every "
                "tube is negative. They conclude the food contains no "
                "nutrients at all. What are the two things wrong with that?",
        "options": [
            {"text": "The tests were run badly, and four negatives in a row "
                     "never happen on a real food.", "correct": False,
             "why": "Four negatives are perfectly possible — a glass of water "
                    "would give them. Nothing here says the method was done "
                    "wrongly."},
            {"text": "The tests measure amounts, and four small amounts can "
                     "still add up to a nutritious food.", "correct": False,
             "why": "These tests measure no amounts at all. They report "
                    "present or not detected, which is the first half of what "
                    "went wrong here."},
            {"text": "The food must contain energy, and energy is the "
                     "nutrient the four tests are looking for.", "correct": False,
             "why": "Energy is not a nutrient, and no test on this bench "
                    "detects it — olive oil gives a blue Benedict's tube and "
                    "carries more energy per gram than anything else here."},
            {"text": "Only four nutrients are tested for at all, and a "
                     "negative means not detected rather than absent.",
             "correct": True},
        ],
        "figure": None,
    },
]
