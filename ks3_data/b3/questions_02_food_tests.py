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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b3-02-e08",
        "band": "easier",
        "text": "Which reagent detects reducing sugar?",
        "options": [
            {"text": "Benedict's solution", "correct": True},
            {"text": "Iodine solution", "correct": False,
             "why": "Iodine solution is the starch test. It is dropped "
                    "straight onto the food and is never heated."},
            {"text": "Biuret solution", "correct": False,
             "why": "Biuret solution is the protein test, and it goes lilac "
                    "purple rather than brick red."},
            {"text": "Ethanol, then water", "correct": False,
             "why": "Ethanol followed by water is the lipid test, and it "
                    "gives a cloudy white rather than a colour change."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e09",
        "band": "easier",
        "text": "A tube of iodine solution has been added to a food and "
                "nothing has been detected. What colour is the tube?",
        "options": [
            {"text": "Blue, unchanged", "correct": False,
             "why": "Blue unchanged is the negative for Benedict's and for "
                    "Biuret, both of which start blue."},
            {"text": "Orange-brown, unchanged", "correct": True},
            {"text": "Cloudy white", "correct": False,
             "why": "A cloudy white is the positive result of the ethanol "
                    "emulsion test, and iodine never gives it."},
            {"text": "Lilac purple", "correct": False,
             "why": "Lilac purple is the positive Biuret result, so it "
                    "reports protein rather than starch."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e10",
        "band": "easier",
        "text": "In the ethanol emulsion test, what do you see when lipid is "
                "detected?",
        "options": [
            {"text": "A brick red", "correct": False,
             "why": "Brick red is the positive Benedict's result, and it "
                    "reports reducing sugar rather than lipid."},
            {"text": "A blue-black colour", "correct": False,
             "why": "Blue-black is the positive iodine result, so it reports "
                    "starch rather than lipid."},
            {"text": "A cloudy white", "correct": True},
            {"text": "A lilac purple colour", "correct": False,
             "why": "Lilac purple is the positive Biuret result, so it "
                    "reports protein rather than lipid."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e11",
        "band": "easier",
        "text": "Biuret solution has been shaken with a food solution and no "
                "protein has been detected. What does the tube look like?",
        "options": [
            {"text": "Clear, unchanged", "correct": False,
             "why": "Clear and unchanged is the negative for the ethanol "
                    "emulsion test, which is looking for lipid."},
            {"text": "Orange-brown, unchanged", "correct": False,
             "why": "Orange-brown unchanged is the negative iodine result, "
                    "which is about starch."},
            {"text": "Brick red", "correct": False,
             "why": "Brick red is a positive Benedict's result. Biuret never "
                    "goes red at all."},
            {"text": "Blue, unchanged", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e12",
        "band": "easier",
        "text": "Which of the four food tests is carried out in a water bath?",
        "options": [
            {"text": "Benedict's", "correct": True},
            {"text": "Iodine", "correct": False,
             "why": "Iodine is a few drops straight onto the food, with no "
                    "heating of any kind."},
            {"text": "Biuret", "correct": False,
             "why": "Biuret is equal volumes shaken together, and the method "
                    "calls for no heating."},
            {"text": "The ethanol emulsion test", "correct": False,
             "why": "Heating is the last thing this one wants — ethanol is "
                    "highly flammable and the tube is never warmed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e13",
        "band": "easier",
        "text": "A food test is described as qualitative. What does that mean?",
        "options": [
            {"text": "It answers present or not detected, and never how much.",
             "correct": True},
            {"text": "It gives an amount in grams once the colour is matched "
                     "to a chart.", "correct": False,
             "why": "That would be a quantitative test, and it needs fixed "
                    "conditions and tubes of known concentration."},
            {"text": "It shows how good the food is for you.", "correct": False,
             "why": "No food test is a judgement about health. It reports one "
                    "nutrient and nothing else."},
            {"text": "It can be trusted without repeating it.", "correct": False,
             "why": "Qualitative says nothing about reliability. It describes "
                    "the kind of answer the test gives."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e14",
        "band": "easier",
        "text": "What is an emulsion?",
        "options": [
            {"text": "A solid that has fully dissolved to give a clear "
                     "solution.", "correct": False,
             "why": "A solution is clear. An emulsion is cloudy precisely "
                    "because nothing has dissolved."},
            {"text": "A cloudy mixture of tiny droplets of one liquid spread "
                     "through another.", "correct": True},
            {"text": "A gas that has been bubbled through a liquid until it "
                     "froths.", "correct": False,
             "why": "That is a foam. An emulsion is one liquid in droplets "
                    "inside another liquid."},
            {"text": "A liquid that has been heated until it separates into "
                     "layers.", "correct": False,
             "why": "Separating into layers is the opposite of an emulsion, "
                    "in which the droplets stay spread through."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e15",
        "band": "easier",
        "text": "What is a false negative?",
        "options": [
            {"text": "A test that shows a colour change when the nutrient is "
                     "not there at all.", "correct": False,
             "why": "That would be a false positive. A false negative is the "
                    "test showing nothing when something is there."},
            {"text": "A test that has been carried out wrongly, so its result "
                     "must be thrown away.", "correct": False,
             "why": "A false negative can follow a method carried out "
                    "perfectly. Too little of the nutrient is enough."},
            {"text": "A test that shows nothing even though the substance "
                     "really is in the food.", "correct": True},
            {"text": "A test whose reagent has gone off, so no colour can "
                     "appear whatever is in the tube.", "correct": False,
             "why": "Old reagent is one cause among several, and the term "
                    "describes the result rather than the cause."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e16",
        "band": "easier",
        "text": "Which two sugars are reducing sugars, the kind Benedict's "
                "solution detects?",
        "options": [
            {"text": "Glucose and fructose", "correct": True},
            {"text": "Sucrose and starch", "correct": False,
             "why": "Sucrose cannot hand an electron to copper, and starch is "
                    "not a sugar at all."},
            {"text": "Sucrose and lactose", "correct": False,
             "why": "Lactose is a reducing sugar, but sucrose is not, so this "
                    "pair is only half right."},
            {"text": "Starch and cellulose", "correct": False,
             "why": "Neither is a sugar. Both are long chains that Benedict's "
                    "does not respond to."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e17",
        "band": "easier",
        "text": "Which nutrient does the ethanol emulsion test detect?",
        "options": [
            {"text": "Starch", "correct": False,
             "why": "Starch is what iodine solution is for, and it gives a "
                    "blue-black rather than a cloud."},
            {"text": "Lipid", "correct": True},
            {"text": "Protein", "correct": False,
             "why": "Protein is what Biuret solution is for, and it gives a "
                    "lilac purple."},
            {"text": "Reducing sugar", "correct": False,
             "why": "Reducing sugar is what Benedict's is for, and it needs "
                    "five minutes in a water bath."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e18",
        "band": "easier",
        "text": "Which food on the bench gives the clearest Biuret positive, "
                "being almost pure protein in water?",
        "options": [
            {"text": "Olive oil", "correct": False,
             "why": "Olive oil has no protein at all, so its Biuret tube "
                    "stays blue."},
            {"text": "Apple juice", "correct": False,
             "why": "Apple juice is under 0.3% protein, which is too little "
                    "for the bench test to show."},
            {"text": "Potato", "correct": False,
             "why": "A potato is about 2% protein — present, but far too "
                    "dilute for a clear lilac."},
            {"text": "Egg white", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e19",
        "band": "easier",
        "text": "Biuret solution contains sodium hydroxide. What does that "
                "mean for how it is handled?",
        "options": [
            {"text": "Eye protection is worn, because it is an irritant.",
             "correct": True},
            {"text": "It is kept away from any flame, because it catches fire "
                     "easily.", "correct": False,
             "why": "Ethanol is the flammable one on this bench. Biuret is a "
                    "hazard because it attacks skin and eyes."},
            {"text": "It is used in a fume cupboard, because it gives off a "
                     "poisonous gas.", "correct": False,
             "why": "Biuret gives off no gas. The danger is contact, which is "
                    "why eye protection is the precaution."},
            {"text": "It is warmed before use, because it works better when "
                     "hot.", "correct": False,
             "why": "The Biuret method calls for no heating at all, and "
                    "heating does nothing about the hazard."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e20",
        "band": "easier",
        "text": "Which test is run by shaking equal volumes of food solution "
                "and reagent together, with no heating?",
        "options": [
            {"text": "Benedict's", "correct": False,
             "why": "Benedict's does use equal volumes, but it then needs "
                    "five minutes in a water bath."},
            {"text": "Biuret", "correct": True},
            {"text": "Iodine", "correct": False,
             "why": "Iodine is a few drops straight onto the food, so no food "
                    "solution and no equal volumes are involved."},
            {"text": "Ethanol and water", "correct": False,
             "why": "That one shakes the food with ethanol and then pours the "
                    "ethanol into water, which is a different method."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e21",
        "band": "easier",
        "text": "Egg white is about 90% water. What is nearly all of the "
                "remaining tenth?",
        "options": [
            {"text": "Starch", "correct": False,
             "why": "Egg white has essentially no carbohydrate, which is why "
                    "its iodine tube stays orange-brown."},
            {"text": "Lipid", "correct": False,
             "why": "The lipid in an egg is in the yolk, so a separated white "
                    "gives a clean emulsion negative."},
            {"text": "Protein", "correct": True},
            {"text": "Minerals", "correct": False,
             "why": "The shell is where most of an egg's mineral sits, and it "
                    "is not part of the white."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e22",
        "band": "easier",
        "text": "Which food on the bench is positive with iodine and "
                "negative on the other three tests?",
        "options": [
            {"text": "Potato", "correct": True},
            {"text": "Milk", "correct": False,
             "why": "Milk has no starch at all, and is positive on three of "
                    "the other tests."},
            {"text": "Olive oil", "correct": False,
             "why": "Olive oil is the emulsion positive, and it carries no "
                    "starch for iodine to find."},
            {"text": "Apple juice", "correct": False,
             "why": "A ripe apple has converted its starch to sugar, so apple "
                    "juice is the Benedict's positive instead."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e23",
        "band": "easier",
        "text": "Which food on the bench is a suspension of fat droplets in "
                "water, and so gives a strong cloud on the emulsion test?",
        "options": [
            {"text": "Potato", "correct": False,
             "why": "Potato holds under a hundredth of its mass as lipid, so "
                    "it gives no cloud worth seeing."},
            {"text": "Egg white", "correct": False,
             "why": "The lipid in an egg is in the yolk, so a separated white "
                    "gives a clean negative."},
            {"text": "Apple juice", "correct": False,
             "why": "Fruit juice is sugar and water, with nothing for the "
                    "ethanol to carry across into the water."},
            {"text": "Milk", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e24",
        "band": "easier",
        "text": "In the emulsion test, the food is shaken with ethanol and "
                "the ethanol is then poured into what?",
        "options": [
            {"text": "Ethanol", "correct": False,
             "why": "Adding ethanol to ethanol changes nothing. The cloud "
                    "needs the second liquid to be water."},
            {"text": "Iodine", "correct": False,
             "why": "Iodine is the starch test, and it plays no part in the "
                    "lipid method."},
            {"text": "Benedict's", "correct": False,
             "why": "Benedict's is the reducing-sugar test, and it is not "
                    "used in the lipid method."},
            {"text": "Water", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e25",
        "band": "easier",
        "text": "What colour is Benedict's solution before it is heated with "
                "a food solution?",
        "options": [
            {"text": "Blue", "correct": True},
            {"text": "Orange-brown", "correct": False,
             "why": "Orange-brown is the colour iodine solution starts at, "
                    "before any food is added to it."},
            {"text": "Clear", "correct": False,
             "why": "Clear and colourless is the negative of the ethanol "
                    "emulsion test; Benedict's is never clear."},
            {"text": "Brick red", "correct": False,
             "why": "Brick red is where Benedict's ends up when a reducing "
                    "sugar is detected, not where it starts."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e26",
        "band": "easier",
        "text": "Milk tested with iodine stays orange-brown, and milk really "
                "does contain no starch. What is a result like that called?",
        "options": [
            {"text": "A false negative", "correct": False,
             "why": "A false negative is a tube showing nothing when the "
                    "nutrient really is there, which is not this case."},
            {"text": "A true negative", "correct": True},
            {"text": "A false positive", "correct": False,
             "why": "A false positive is a colour change with nothing there. "
                    "This tube did not change colour."},
            {"text": "An anomalous result", "correct": False,
             "why": "Nothing here is out of line with the rest. The test did "
                    "exactly what it should."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e27",
        "band": "easier",
        "text": "An egg is separated before the emulsion test. Which part of "
                "the egg holds the lipid?",
        "options": [
            {"text": "The shell", "correct": False,
             "why": "The shell is a hard mineral case and is not part of the "
                    "food being tested."},
            {"text": "The white", "correct": False,
             "why": "Egg white is about 90% water and 10% protein, and gives "
                    "a clean negative on this test."},
            {"text": "The yolk", "correct": True},
            {"text": "Both equally", "correct": False,
             "why": "They are not alike at all — separating them is what "
                    "makes a clean negative possible."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e28",
        "band": "easier",
        "text": "A reducing sugar is one that can hand an electron to a "
                "particular metal in Benedict's solution. Which metal?",
        "options": [
            {"text": "Copper", "correct": True},
            {"text": "Iron", "correct": False,
             "why": "Iron is the mineral built into haemoglobin, and it plays "
                    "no part in this reagent."},
            {"text": "Sodium", "correct": False,
             "why": "Sodium hydroxide is in Biuret solution, and sodium is "
                    "not what a reducing sugar hands its electron to."},
            {"text": "Calcium", "correct": False,
             "why": "Calcium is the mineral built into bone, and it is not "
                    "part of Benedict's solution."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e29",
        "band": "easier",
        "text": "The safety note says never to taste anything on the bench. "
                "Why does that rule apply even to the foods?",
        "options": [
            {"text": "Tasting would use up the sample, leaving too little for "
                     "the test.", "correct": False,
             "why": "There is plenty of food for the test. The rule is about "
                    "what has been spilled on it."},
            {"text": "The reagents are irritants, and a food on this bench may "
                     "have reagent on it.", "correct": True},
            {"text": "The foods have been left out too long and will have "
                     "gone off.", "correct": False,
             "why": "Fresh samples are put out for the lesson. The hazard is "
                    "the chemicals beside them."},
            {"text": "Tasting is a test of its own and would make the results "
                     "unfair.", "correct": False,
             "why": "Taste is not one of the four tests, and the rule is a "
                    "safety rule rather than a fair-test rule."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-e30",
        "band": "easier",
        "text": "Apple juice is heated with Benedict's solution in a water "
                "bath, following the method exactly. What would you see?",
        "options": [
            {"text": "Blue, unchanged", "correct": False,
             "why": "Apple juice carries fructose and glucose, both reducing "
                    "sugars, so this tube does change."},
            {"text": "Clear", "correct": False,
             "why": "Clear belongs to the ethanol emulsion test's negative, "
                    "and a Benedict's tube is never clear."},
            {"text": "Lilac purple", "correct": False,
             "why": "Lilac purple belongs to Biuret and reports protein, "
                    "which apple juice has very little of."},
            {"text": "Brick red", "correct": True},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "b3-02-s08",
        "band": "standard",
        "text": "Iodine solution is dropped straight onto a piece of food, "
                "but Benedict's and Biuret are run on a food solution. Why "
                "the difference?",
        "options": [
            {"text": "Iodine reports a colour on the surface it touches, "
                     "while the other two need the reagent mixed right "
                     "through the sample.", "correct": True},
            {"text": "Iodine would be destroyed by the water in a food "
                     "solution, so the sample has to be kept completely dry "
                     "for that test to work at all.", "correct": False,
             "why": "The standard starch test is often run on starch "
                    "solution, so water does not destroy iodine."},
            {"text": "Iodine is the only reagent strong enough to get inside "
                     "a solid piece of food on its own.", "correct": False,
             "why": "Iodine does not get far inside either, which is why a "
                    "whole lump can give a weak result."},
            {"text": "Benedict's and Biuret are too dangerous to put directly "
                     "onto food that might be eaten later.", "correct": False,
             "why": "Nothing on this bench is eaten at all. The reason is "
                    "about the reagent reaching the sample."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s09",
        "band": "standard",
        "text": "An unripe apple gives a blue-black with iodine, and a ripe "
                "one from the same tree gives orange-brown. What has happened "
                "as the apple ripened?",
        "options": [
            {"text": "The skin has thickened, so the iodine no longer reaches "
                     "the inside of the fruit.", "correct": False,
             "why": "The flesh is tested, not the skin, and a ripe apple is "
                    "softer rather than harder to get into."},
            {"text": "The apple has lost water, so everything in it is now "
                     "too concentrated for the test to read.",
             "correct": False,
             "why": "A more concentrated sample makes a positive more likely, "
                    "not less, so this has it backwards."},
            {"text": "Its starch has been converted into sugar, so there is "
                     "no starch left for iodine to find.", "correct": True},
            {"text": "Iodine stops working on fruit once the fruit is sweet "
                     "enough to eat.", "correct": False,
             "why": "Iodine responds to starch wherever it is. Sweetness does "
                    "not switch the reagent off."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s10",
        "band": "standard",
        "text": "The Biuret method says to shake the tube. A group adds the "
                "reagent, leaves it standing, and reads a blue tube on a food "
                "they know is high in protein. What has gone wrong?",
        "options": [
            {"text": "The reagent has not mixed through the sample, so most "
                     "of the protein never met it.", "correct": True},
            {"text": "Standing turns Biuret back to blue after it has gone "
                     "lilac, so the colour was missed.", "correct": False,
             "why": "A lilac does not fade back to blue on standing. The "
                    "colour never appeared in the first place."},
            {"text": "Biuret needs to be shaken because shaking warms it, and "
                     "the test will not run cold.", "correct": False,
             "why": "Biuret needs no heating at all, and shaking a tube does "
                    "not warm it appreciably."},
            {"text": "The protein has settled to the bottom, which stops it "
                     "reacting with any reagent at all.", "correct": False,
             "why": "Protein in solution does not settle out, and reagent "
                    "reaching it is what matters."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s11",
        "band": "standard",
        "text": "Milk is run through all four tests and gives three "
                "positives. Which test is the negative one, and is it a true "
                "negative?",
        "options": [
            {"text": "Benedict's, and it is a false negative caused by the "
                     "lactose being too dilute.", "correct": False,
             "why": "Lactose is a reducing sugar and milk goes brick red on "
                    "Benedict's if it is heated long enough."},
            {"text": "Biuret, and it is a true negative because milk carries "
                     "no protein.", "correct": False,
             "why": "Milk is rich in casein and whey protein, and gives a "
                    "clear lilac."},
            {"text": "Iodine, and it is a true negative because milk really "
                     "has no starch.", "correct": True},
            {"text": "The emulsion test, and it is a true negative because "
                     "milk fat is dissolved rather than in droplets.",
             "correct": False,
             "why": "Whole milk is fat droplets suspended in water, and gives "
                    "a strong cloudiness."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s12",
        "band": "standard",
        "text": "A drink is labelled 'no added sugar'. You run Benedict's on "
                "it and the tube stays blue. What does that entitle you to "
                "write?",
        "options": [
            {"text": "That the label is proved correct, since a blue tube "
                     "rules sugar out.", "correct": False,
             "why": "A blue tube rules nothing out. Sucrose gives a blue tube "
                    "and is sugar."},
            {"text": "That no reducing sugar was detected in this drink under "
                     "these conditions.", "correct": True},
            {"text": "That the drink contains no carbohydrate of any kind.",
             "correct": False,
             "why": "Starch is a carbohydrate and Benedict's says nothing "
                    "about it; that would need the iodine test."},
            {"text": "That the drink is a healthier choice than one that goes "
                     "brick red.", "correct": False,
             "why": "No food test is a judgement about health, and a colour "
                    "does not rank two drinks."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s13",
        "band": "standard",
        "text": "A teacher asks for results written as 'starch detected' "
                "rather than 'starch present'. What does that wording "
                "protect against?",
        "options": [
            {"text": "It stops a student claiming the amount, which the "
                     "colour cannot give.", "correct": False,
             "why": "Neither wording mentions an amount, so this is not what "
                    "the change is guarding."},
            {"text": "It stops a student writing up a result before the tube "
                     "has finished changing colour.", "correct": False,
             "why": "Timing is handled by the method. The wording is about "
                    "what a finished result means."},
            {"text": "It makes the write-up sound more scientific without "
                     "changing what is actually being claimed.",
             "correct": False,
             "why": "The two do claim different things, which is the whole "
                    "point of asking for one of them."},
            {"text": "It keeps the claim to what was observed, so a negative "
                     "cannot be read as proof of absence.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s14",
        "band": "standard",
        "text": "A group heats milk with Benedict's for thirty seconds, sees "
                "a pale green, and records milk as negative for reducing "
                "sugar. What should they change?",
        "options": [
            {"text": "Use twice as much Benedict's, since the reagent must "
                     "have run out.", "correct": False,
             "why": "Nothing ran out in thirty seconds. The tube simply had "
                    "not been heated long enough."},
            {"text": "Heat the tube in the bath for the full five minutes and "
                     "read it again.", "correct": True},
            {"text": "Record the green as a positive, since any change at all "
                     "counts as a detection.", "correct": False,
             "why": "Reading a half-finished tube is what caused the problem. "
                    "The method is run to the end first."},
            {"text": "Switch to Biuret, which gives a clearer answer on milk "
                     "than Benedict's does.", "correct": False,
             "why": "Biuret answers a different question — protein — so it "
                    "cannot settle the sugar one."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s15",
        "band": "standard",
        "text": "In the emulsion test the cloud appears only once the ethanol "
                "is poured into water. What is the cloudiness made of?",
        "options": [
            {"text": "Bubbles of air trapped as the two liquids are poured "
                     "together.", "correct": False,
             "why": "Bubbles rise and clear within seconds. The cloud stays "
                    "and is made of lipid."},
            {"text": "Tiny droplets of lipid, which the water cannot keep "
                     "dissolved.", "correct": True},
            {"text": "Solid crystals of food that the ethanol has dried out.",
             "correct": False,
             "why": "Nothing crystallises here, and a food with no lipid in "
                    "it gives no cloud at all."},
            {"text": "Ethanol itself, which turns white as soon as it meets "
                     "water.", "correct": False,
             "why": "Ethanol and water mix to a clear liquid, which is why a "
                    "negative tube stays clear."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s16",
        "band": "standard",
        "text": "Two foods both give a lilac with Biuret. A student wants to "
                "say which has more protein. Why can this test not settle "
                "that?",
        "options": [
            {"text": "Because the colour is only produced by protein that has "
                     "already been digested.", "correct": False,
             "why": "Biuret responds to the protein in the food as it is; no "
                    "digestion is involved."},
            {"text": "Because Biuret detects some proteins and not others, so "
                     "the two tubes are not comparable.", "correct": False,
             "why": "Biuret responds to protein generally. The limit is that "
                    "it reports presence, not amount."},
            {"text": "Because lilac fades at different rates, so whichever is "
                     "read first always looks stronger.", "correct": False,
             "why": "Reading order is not the difficulty. The test gives no "
                    "quantity however carefully it is read."},
            {"text": "Because a positive says protein was detected and "
                     "nothing about how much was there.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s17",
        "band": "standard",
        "text": "A crisp gives a thick white cloud on the emulsion test; a "
                "boiled potato gives none. What may be written down about the "
                "two foods?",
        "options": [
            {"text": "Lipid was detected in the crisp and not detected in the "
                     "boiled potato.", "correct": True},
            {"text": "The crisp contains more lipid than the boiled potato "
                     "does.", "correct": False,
             "why": "The test gives no amount, so it cannot rank two foods "
                    "against each other."},
            {"text": "The crisp is the less healthy of the two foods, since "
                     "it holds fat and the potato does not.", "correct": False,
             "why": "No food test is a judgement about health, and lipid is "
                    "one of the seven required nutrients."},
            {"text": "The boiled potato contains no lipid whatever, since "
                     "nothing at all appeared in its tube.", "correct": False,
             "why": "A negative means not detected. Potato carries a very "
                    "small amount of lipid, below what the test shows."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s18",
        "band": "standard",
        "text": "Plain flour and icing sugar are both white powders. A "
                "student drops iodine solution on each. What would they see, "
                "and what does it show?",
        "options": [
            {"text": "Both go blue-black, showing that a white powder always "
                     "contains starch.", "correct": False,
             "why": "Icing sugar is sugar, not starch, and it leaves the "
                    "iodine orange-brown."},
            {"text": "Neither of them changes colour, showing that iodine "
                     "solution cannot be used on a dry powder at all.",
             "correct": False,
             "why": "Iodine works perfectly well on a dry powder, and the "
                    "flour goes blue-black."},
            {"text": "The icing sugar goes blue-black, showing that sugar is "
                     "what iodine detects.", "correct": False,
             "why": "Iodine detects starch, not sugar, so this has the two "
                    "powders the wrong way round."},
            {"text": "The flour goes blue-black and the icing sugar does "
                     "not, showing the test separates them.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s19",
        "band": "standard",
        "text": "A group tests a cereal with Biuret and sees no change. "
                "Which of these write-ups could they defend?",
        "options": [
            {"text": "This cereal has no protein in it.", "correct": False,
             "why": "The tube shows that none was detected, which is a "
                    "weaker claim than none being there."},
            {"text": "Protein is present but the test failed.", "correct": False,
             "why": "The result gives no reason to say the test failed, and "
                    "no evidence that protein is present."},
            {"text": "No protein was detected in this cereal under these "
                     "conditions.", "correct": True},
            {"text": "This cereal is a poor source of protein compared with "
                     "egg white.", "correct": False,
             "why": "That is a comparison of amounts, which a qualitative "
                    "test cannot support."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s20",
        "band": "standard",
        "text": "The Benedict's method says equal volumes of food solution "
                "and reagent. Why does the volume matter if the test does not "
                "measure an amount?",
        "options": [
            {"text": "Because the colour that comes up depends on the volumes "
                     "as well as the sugar, so groups can only be compared if "
                     "they match.", "correct": True},
            {"text": "Because unequal volumes would make the reagent stop "
                     "working altogether, whatever was in the food solution "
                     "and however long the tube was heated.", "correct": False,
             "why": "The reagent still works. What changes is how far the "
                    "colour travels, and so what a tube looks like."},
            {"text": "Because a tube that is too full boils over in the water "
                     "bath and the sample is lost.", "correct": False,
             "why": "That is a practical nuisance rather than the reason the "
                    "method fixes the volumes."},
            {"text": "Because the food solution would be too dilute to "
                     "detect anything at all.", "correct": False,
             "why": "The dilution of the food is set when it is made up, not "
                    "by how much reagent is added to it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s21",
        "band": "standard",
        "text": "A bottle of iodine solution has been left open and is now "
                "much paler than the fresh bottle. What effect would using it "
                "have on results?",
        "options": [
            {"text": "Results would be unaffected, because iodine either "
                     "detects starch or it does not.", "correct": False,
             "why": "A weaker reagent gives a weaker colour, which is exactly "
                    "how a positive gets recorded as a negative."},
            {"text": "Every food would give a positive, because pale iodine "
                     "darkens on contact with anything.", "correct": False,
             "why": "Pale iodine does not darken on just anything; it needs "
                    "starch, and it responds less strongly."},
            {"text": "Weak positives could be missed, giving false negatives.",
             "correct": True},
            {"text": "Only the negatives would change, because a true "
                     "negative needs strong reagent to be trusted.",
             "correct": False,
             "why": "It is the weak positives that are at risk. A food with "
                    "no starch stays orange-brown either way."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s22",
        "band": "standard",
        "text": "A laboratory calls its version of the sugar test "
                "quantitative, while the school bench version is called "
                "qualitative. What is the difference?",
        "options": [
            {"text": "The laboratory uses a different reagent altogether, one "
                     "that changes colour more reliably and more strongly "
                     "than the school bench version does.", "correct": False,
             "why": "It is the same chemistry. What differs is how tightly "
                    "the conditions are held and what it is compared with."},
            {"text": "The laboratory fixes every condition and compares "
                     "against tubes of known concentration, so its colour "
                     "means an amount.", "correct": True},
            {"text": "The laboratory repeats the test more times, and "
                     "repeating a test is what makes it quantitative.",
             "correct": False,
             "why": "Repeats improve reliability, but repeating a test that "
                    "gives no amount still gives no amount."},
            {"text": "The laboratory reads the tube by eye more carefully "
                     "than a school class can.", "correct": False,
             "why": "Care in reading does not create a number. Something to "
                    "compare against is what does."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s23",
        "band": "standard",
        "text": "When a clean lipid negative is wanted, egg white is used "
                "rather than whole egg. Why does that choice matter?",
        "options": [
            {"text": "Whole egg would be too thick to shake with ethanol, so "
                     "no result could be read at all.", "correct": False,
             "why": "Whole egg can be shaken with ethanol perfectly well. The "
                    "problem is what is in it."},
            {"text": "Whole egg contains the yolk, and the yolk holds the "
                     "lipid, so the test would come out positive.",
             "correct": True},
            {"text": "Whole egg would give a false positive, because its "
                     "protein clouds the water on its own.", "correct": False,
             "why": "Protein does not cloud the water in this test. The "
                    "positive from a whole egg is a true one."},
            {"text": "Whole egg has been beaten, and beating destroys the "
                     "lipid that would otherwise show up.", "correct": False,
             "why": "Beating changes nothing about the lipid. It is still "
                    "there and still detected."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s24",
        "band": "standard",
        "text": "A student wants to know whether a drink contains vitamin C. "
                "Can the four bench tests answer that?",
        "options": [
            {"text": "Yes — Benedict's detects vitamin C along with the "
                     "reducing sugars.", "correct": False,
             "why": "Benedict's reports reducing sugar. Its result says "
                    "nothing at all about a vitamin."},
            {"text": "Yes — a food that goes lilac with Biuret has vitamins "
                     "in it too.", "correct": False,
             "why": "Biuret reports protein. Protein and vitamins are "
                    "different nutrients."},
            {"text": "No — vitamin C can only be detected once the drink has "
                     "been heated to 80 °C first.", "correct": False,
             "why": "Heating does not bring a vitamin within reach of these "
                    "reagents. None of them responds to it."},
            {"text": "No — the four tests report starch, reducing sugar, "
                     "lipid and protein only.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s25",
        "band": "standard",
        "text": "One bench runs Benedict's at 80 °C and the emulsion test "
                "with ethanol on the same afternoon. How can both be done "
                "safely together?",
        "options": [
            {"text": "By using a water bath rather than a flame, so there is "
                     "no naked flame near the open ethanol.", "correct": True},
            {"text": "By running the ethanol test first, since ethanol is "
                     "only flammable once it has been warmed.",
             "correct": False,
             "why": "Ethanol is highly flammable cold. The order of the tests "
                    "is not what makes it safe."},
            {"text": "By keeping the ethanol in a stoppered bottle at all "
                     "times, including while it is being used.",
             "correct": False,
             "why": "It has to be open to be poured. The precaution that "
                    "works is removing the flame."},
            {"text": "By heating the Benedict's tube over a low Bunsen flame "
                     "rather than a roaring one.", "correct": False,
             "why": "A low flame is still a naked flame beside open ethanol, "
                    "which is what the safety note forbids."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s26",
        "band": "standard",
        "text": "Group A crushes 1 g of food into 100 cm3 of water; group B "
                "crushes 1 g into 10 cm3. Both then run Biuret. Whose tube is "
                "more likely to show a colour, and why?",
        "options": [
            {"text": "Group A, because more water gives the reagent more room "
                     "to work in.", "correct": False,
             "why": "Room to work is not the limit. Spreading the same "
                    "protein through more water makes it harder to detect."},
            {"text": "Group B, because their solution is ten times more "
                     "concentrated.", "correct": True},
            {"text": "Neither, because the mass of food is the same and that "
                     "is what the test responds to.", "correct": False,
             "why": "The test responds to concentration in the tube, not to "
                    "the mass that was weighed out."},
            {"text": "Group A, because a thinner solution mixes with the "
                     "reagent faster.", "correct": False,
             "why": "Speed of mixing does not decide it. A dilute sample can "
                    "mix perfectly and still show nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s27",
        "band": "standard",
        "text": "Biuret leaves apple juice blue, and leaves olive oil blue. "
                "Only one of those tubes is hiding some protein. Which, and "
                "how do you know?",
        "options": [
            {"text": "The olive oil, because a film of oil coats the inside "
                     "of the tube and stops the reagent working on whatever "
                     "is underneath it.", "correct": False,
             "why": "Olive oil genuinely has no protein, so its blue tube is "
                    "an honest result."},
            {"text": "Neither, because a blue Biuret tube means the same "
                     "thing whatever was put in it.", "correct": False,
             "why": "The tubes look the same, but one food has protein in it "
                    "and the other does not."},
            {"text": "The apple juice, because it is under 0.3% protein — "
                     "present, but below what the test can show.",
             "correct": True},
            {"text": "Both, because every negative result in this lesson "
                     "turns out to be a false one.", "correct": False,
             "why": "Plenty of the negatives are true. Olive oil really has "
                    "no protein in it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s28",
        "band": "standard",
        "text": "Milk and apple juice both go brick red with Benedict's. "
                "Which single further test would separate them, and what "
                "would you see?",
        "options": [
            {"text": "Iodine — the milk goes blue-black and the apple juice "
                     "stays orange-brown.", "correct": False,
             "why": "Neither carries starch, so both tubes stay orange-brown "
                    "and nothing is separated."},
            {"text": "Biuret — the milk goes lilac and the apple juice stays "
                     "blue.", "correct": True},
            {"text": "A second Benedict's test, heated for twice as long, "
                     "since the redder tube is the milk.", "correct": False,
             "why": "Heating longer changes the colour of both and reports no "
                    "difference between the foods."},
            {"text": "Iodine — the apple juice goes blue-black because its "
                     "sugar came from starch.", "correct": False,
             "why": "The starch in a ripening apple has already been "
                    "converted, so there is none left to detect."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s29",
        "band": "standard",
        "text": "In the emulsion test the food is shaken with ethanol before "
                "anything meets water. Why can the food not simply be added "
                "to water on its own?",
        "options": [
            {"text": "Because the water would wash the lipid out of the food "
                     "and down the sink long before any of it could be seen "
                     "in the tube.", "correct": False,
             "why": "The lipid is not washed away; it simply sits there "
                    "without forming the cloud that reports it."},
            {"text": "Because the ethanol has to dissolve the lipid out of "
                     "the food first, so that it can come out as droplets in "
                     "the water.", "correct": True},
            {"text": "Because ethanol makes the water clearer, so a cloud is "
                     "easier to see against it.", "correct": False,
             "why": "Plain water is already clear. The ethanol's job is to "
                    "carry the lipid, not to improve the view."},
            {"text": "Because water and food would react and give a false "
                     "positive cloud.", "correct": False,
             "why": "Food in water does not produce this cloud. It takes "
                    "lipid coming out of ethanol."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-s30",
        "band": "standard",
        "text": "A class runs all four tests on every food rather than only "
                "the test each food is expected to pass. What does that "
                "extra work buy them?",
        "options": [
            {"text": "It proves that each reagent is working properly before "
                     "the real test is run.", "correct": False,
             "why": "A reagent check would need a food of known content, "
                    "which is a different plan from testing everything."},
            {"text": "It makes each result more reliable, because four tests "
                     "agreeing is stronger evidence than one.",
             "correct": False,
             "why": "The four do not agree or disagree — they answer four "
                    "separate questions about four nutrients."},
            {"text": "It shows which food is the most nutritious of the five "
                     "on the bench.", "correct": False,
             "why": "Counting positives is not a measure of nutrition, and no "
                    "food test judges how good a food is."},
            {"text": "It gives the negatives as well as the positives, which "
                     "is where the false negatives show up.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b3-02-h08",
        "band": "harder",
        "text": "A food gives a blue-black with iodine and a brick red with "
                "Benedict's. What is the strongest statement those two "
                "results together support?",
        "options": [
            {"text": "Starch and reducing sugar were both detected in this "
                     "food.", "correct": True},
            {"text": "The food is mostly starch, with a smaller amount of "
                     "sugar alongside it.", "correct": False,
             "why": "Neither test gives an amount, so nothing here ranks the "
                    "two against each other."},
            {"text": "Some of the starch in the food has already been broken "
                     "down into sugar.", "correct": False,
             "why": "That is one way a food could come to hold both, but the "
                    "results do not show it happened."},
            {"text": "The food is a good source of energy and a poor source "
                     "of protein.", "correct": False,
             "why": "Energy is not what either test reports, and protein "
                    "would need a Biuret tube."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h09",
        "band": "harder",
        "text": "A student suspects the emulsion test would go cloudy with "
                "ethanol and water alone, whatever food was used. What is the "
                "cleanest way to find out?",
        "options": [
            {"text": "Run the test on five different foods and see whether "
                     "any of them stays clear.", "correct": False,
             "why": "That tells you foods differ, but never separates the "
                    "ethanol's own behaviour from the food's."},
            {"text": "Pour ethanol that has been shaken with nothing at all "
                     "into water, and see what happens.", "correct": True},
            {"text": "Use twice as much ethanol on the same food and compare "
                     "how thick the two clouds are.", "correct": False,
             "why": "Both tubes still contain food, so neither one can show "
                    "what ethanol does on its own."},
            {"text": "Ask a second group to repeat the same test on the same "
                     "food and compare the results.", "correct": False,
             "why": "A repeat checks reliability. It cannot answer a question "
                    "about what the ethanol contributes."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h10",
        "band": "harder",
        "text": "A group tests a fruit juice with Benedict's, gets a strong "
                "brick red, and writes that the juice is unhealthy. Where "
                "does that go wrong, and where does it not?",
        "options": [
            {"text": "It is wrong throughout, since a brick red tells you "
                     "nothing about what is in the juice.", "correct": False,
             "why": "The tube does tell you something real: reducing sugar "
                    "was detected. The claim goes beyond that."},
            {"text": "It is right about the sugar but wrong to call a food "
                     "unhealthy on a colour, since no food test judges "
                     "health.", "correct": True},
            {"text": "It is right throughout, since a strong colour is good "
                     "evidence of a large amount of sugar being present in "
                     "the juice.", "correct": False,
             "why": "Colour strength depends on heating time and volumes too, "
                    "so it is not a measure of amount."},
            {"text": "It is wrong about the sugar but right about the health, "
                     "since fruit juice is known to be sugary.",
             "correct": False,
             "why": "The sugar part is the bit the test supports. What it "
                    "cannot support is the health judgement."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h11",
        "band": "harder",
        "text": "Whole milk and skimmed milk are put through all four tests. "
                "Which test would most likely tell them apart, and how?",
        "options": [
            {"text": "Biuret, because removing the fat takes the protein out "
                     "with it and the skimmed tube stays blue.",
             "correct": False,
             "why": "Skimming removes fat and leaves the protein behind, so "
                    "both tubes go lilac."},
            {"text": "Iodine, because skimmed milk has had starch added to "
                     "it to thicken it back up after the fat was taken out.",
             "correct": False,
             "why": "Neither milk contains starch, so both tubes stay "
                    "orange-brown and nothing is separated."},
            {"text": "The emulsion test, because whole milk clouds strongly "
                     "and skimmed milk has had most of its fat taken out.",
             "correct": True},
            {"text": "Benedict's, because taking the fat out concentrates the "
                     "lactose and only the skimmed tube goes red.",
             "correct": False,
             "why": "Both milks carry lactose and both go brick red, so this "
                    "test does not separate them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h12",
        "band": "harder",
        "text": "A sucrose solution gives a blue Benedict's tube. Boiled "
                "with a little acid first, the same solution then goes brick "
                "red. What does that pair of results establish?",
        "options": [
            {"text": "That the first tube was a mistake, since the sugar was "
                     "there all along and should have shown.",
             "correct": False,
             "why": "The first tube was correct. Benedict's is not asking "
                    "whether there is sugar, but whether there is a reducing "
                    "one."},
            {"text": "That boiling the solution with acid creates fresh "
                     "sugar out of the water that was already in the tube.",
             "correct": False,
             "why": "Nothing is created. The sucrose already present has been "
                    "split into two smaller sugars."},
            {"text": "That the acid, not the sugar, is what Benedict's "
                     "responds to.", "correct": False,
             "why": "Acid alone gives no red. It is the glucose and fructose "
                    "released from the sucrose that do."},
            {"text": "That Benedict's answers a narrower question than 'is "
                     "there sugar here', and sucrose falls outside it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h13",
        "band": "harder",
        "text": "A group reports: 'Potato contains starch, and contains no "
                "protein, no sugar and no lipid.' Which part of that report "
                "can they defend?",
        "options": [
            {"text": "The starch part alone — the other three should say "
                     "'not detected' rather than 'none'.", "correct": True},
            {"text": "All four parts, since each one is exactly what the four "
                     "tubes showed on the day.", "correct": False,
             "why": "Three of the tubes showed nothing detected, which is a "
                    "weaker claim than nothing being there."},
            {"text": "None of it, since a single set of tests can never "
                     "support any claim about a food.", "correct": False,
             "why": "A positive is a real observation. The blue-black "
                    "genuinely supports starch being detected."},
            {"text": "The three negatives alone, since a negative result is "
                     "the more certain kind.", "correct": False,
             "why": "It is the other way round: a negative is the result that "
                    "needs the most care, because it has several causes."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h14",
        "band": "harder",
        "text": "A company sells a new reagent it says turns pink with "
                "vitamin C. Before trusting a negative result from it, what "
                "would you most want to know?",
        "options": [
            {"text": "Whether it is sold in the same size bottle as the other "
                     "reagents on the bench.", "correct": False,
             "why": "Bottle size says nothing about what a result from it "
                    "means."},
            {"text": "Whether it is safe enough for a school laboratory to "
                     "keep on an open shelf.", "correct": False,
             "why": "That matters for handling it, but not for what a blue "
                    "or pink tube licenses you to claim."},
            {"text": "How little vitamin C it can still detect, since below "
                     "that a negative would be false.", "correct": True},
            {"text": "Whether it changes colour faster than Benedict's does "
                     "when the two are run side by side on a comparable "
                     "sample.", "correct": False,
             "why": "Speed is a convenience. It does not tell you what a "
                    "negative from the new reagent is worth."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h15",
        "band": "harder",
        "text": "Two blue Biuret tubes sit side by side: one is a true "
                "negative and one is a false negative. As evidence, how do "
                "the two differ?",
        "options": [
            {"text": "They do not differ as evidence — the tubes look the "
                     "same, and only other knowledge separates them.",
             "correct": True},
            {"text": "The false negative is a paler blue, which is how a "
                     "careful reader tells them apart.", "correct": False,
             "why": "Both are simply unchanged blue. There is no shade that "
                    "marks one out."},
            {"text": "The true negative was produced by a correct method and "
                     "the false one by a mistake in the method.",
             "correct": False,
             "why": "A false negative follows a method carried out perfectly, "
                    "when there is too little of the nutrient."},
            {"text": "The false negative would turn lilac if it were left "
                     "standing for long enough on the bench.", "correct": False,
             "why": "Standing changes nothing. The protein is below what the "
                    "test can show, however long it waits."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h16",
        "band": "harder",
        "text": "A group makes their food solution with water straight from a "
                "boiling kettle, then runs Biuret on it. Why might that "
                "weaken their conclusion?",
        "options": [
            {"text": "Because hot water cannot dissolve protein at all, so "
                     "nothing would be in the solution to detect.",
             "correct": False,
             "why": "Hot water dissolves a good deal. The worry is what the "
                    "heat does to the protein, not whether it dissolves."},
            {"text": "Because Biuret only works at 80 °C, and a cooling "
                     "solution would fall below that.", "correct": False,
             "why": "Biuret needs no heating at all, so temperature is not a "
                    "requirement of the method."},
            {"text": "Because very hot water changes protein, so a negative "
                     "would be hard to interpret.", "correct": True},
            {"text": "Because hot water would make the Biuret go lilac on its "
                     "own, giving a false positive.", "correct": False,
             "why": "Biuret in hot water stays blue. A false positive is not "
                    "the risk being run here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h17",
        "band": "harder",
        "text": "Two tubes of the same juice are heated identically, but one "
                "is given twice as much Benedict's solution and comes out a "
                "deeper red. What does that show?",
        "options": [
            {"text": "That the juice in the second tube must have held twice "
                     "as much reducing sugar as the juice that went into the "
                     "first one.", "correct": False,
             "why": "Both tubes came from the same juice, so the sugar in "
                    "them is identical."},
            {"text": "That the colour depends on the method as well as the "
                     "food, so a deeper red is not evidence of more sugar.",
             "correct": True},
            {"text": "That the second tube was heated for longer without "
                     "anyone noticing it.", "correct": False,
             "why": "The question says the heating was identical. The "
                    "difference is the volume of reagent."},
            {"text": "That Benedict's stops working once it runs short, so "
                     "the first tube under-reported the sugar.",
             "correct": False,
             "why": "Neither tube under-reports anything, because neither "
                    "tube was reporting an amount to begin with."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h18",
        "band": "harder",
        "text": "A student suggests replacing the ethanol test with rubbing "
                "the food on paper and looking for a translucent mark. What "
                "is the strongest objection?",
        "options": [
            {"text": "Paper cannot be used in a school laboratory for a food "
                     "test of any kind, whatever the food happens to be.",
             "correct": False,
             "why": "There is no such rule. The objection has to be about "
                    "what the mark would prove."},
            {"text": "The mark would appear for a food that is simply wet, so "
                     "water and lipid could not be told apart.",
             "correct": True},
            {"text": "The mark would take several days to appear, which is "
                     "longer than a lesson allows.", "correct": False,
             "why": "A grease mark shows quickly. Time is not what makes the "
                    "method weak."},
            {"text": "Paper would absorb the protein as well, giving a "
                     "positive on foods with no lipid in them.",
             "correct": False,
             "why": "Protein is not what leaves a translucent mark, so this "
                    "is not the confusion to worry about."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h19",
        "band": "harder",
        "text": "A student objects that the emulsion test 'must be wrong' "
                "because the cloud forms in the water rather than in the "
                "food. How would you answer?",
        "options": [
            {"text": "The objection holds, and the test only works on foods "
                     "that are liquid to begin with.", "correct": False,
             "why": "Solid foods are tested this way routinely, by shaking "
                    "them with ethanol first."},
            {"text": "The objection holds, because a result that is read "
                     "outside the original sample cannot be trusted as "
                     "evidence about that sample.", "correct": False,
             "why": "Plenty of tests read a result elsewhere. What matters is "
                    "whether the lipid came from the food."},
            {"text": "The cloud is the food's own lipid, carried into the "
                     "water by the ethanol, so where it appears is not the "
                     "point.", "correct": True},
            {"text": "The cloud is made by the water and the ethanol mixing, "
                     "so the objection is right about the cause.",
             "correct": False,
             "why": "Ethanol and water mix clear. Without lipid there is no "
                    "cloud at all."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h20",
        "band": "harder",
        "text": "A crushed multivitamin tablet is put through all four tests "
                "and every tube is negative. What can be concluded?",
        "options": [
            {"text": "That the tablet is useless, since nothing was found in "
                     "it by any of the four tests.", "correct": False,
             "why": "The tablet's vitamins and minerals are real; these four "
                    "tests simply do not look for them."},
            {"text": "That starch, reducing sugar, lipid and protein were "
                     "each not detected, and nothing about vitamins.",
             "correct": True},
            {"text": "That the tablet contains only vitamins, since "
                     "everything else has been ruled out.", "correct": False,
             "why": "Nothing has been ruled out. A negative means not "
                    "detected, not absent."},
            {"text": "That all four reagents must have gone off, since a "
                     "tablet of nutrients cannot give four negatives.",
             "correct": False,
             "why": "Four negatives are exactly what you would expect here, "
                    "because none of the four nutrients is in the tablet."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h21",
        "band": "harder",
        "text": "Across these four food tests, why is a positive result a "
                "stronger piece of evidence than a negative one?",
        "options": [
            {"text": "Because a positive uses more reagent, and more reagent "
                     "makes any result more certain.", "correct": False,
             "why": "The same volumes are used either way. Quantity of "
                    "reagent is not what decides it."},
            {"text": "Because a positive is read at the end of the method "
                     "while a negative is read at the start.",
             "correct": False,
             "why": "Both are read at the same point. The difference is in "
                    "what each one can be caused by."},
            {"text": "Because a colour change has one cause, while nothing "
                     "happening has several.", "correct": True},
            {"text": "Because a negative can be checked again and a positive "
                     "cannot be repeated once the tube has changed.",
             "correct": False,
             "why": "Either can be repeated on a fresh sample, so this is not "
                    "the difference between them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h22",
        "band": "harder",
        "text": "With only the school kit, what is the most a student can "
                "honestly say when comparing the sugar in two different "
                "drinks?",
        "options": [
            {"text": "That whichever tube is redder came from the drink with "
                     "more sugar in it.", "correct": False,
             "why": "Colour depends on the method as well as the drink, so "
                    "redder does not mean more."},
            {"text": "That reducing sugar was detected in one, the other, "
                     "both or neither.", "correct": True},
            {"text": "That the two drinks contain the same sugar if the tubes "
                     "end up the same colour.", "correct": False,
             "why": "Two tubes of the same colour could hold different "
                    "sugars, and the test does not identify which."},
            {"text": "That neither drink contains sugar if both tubes stay "
                     "blue at the end of the five minutes.", "correct": False,
             "why": "Sucrose gives a blue tube and is sugar, so a blue pair "
                    "rules nothing out."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h23",
        "band": "harder",
        "text": "A reagent is developed that detects protein at a hundredth "
                "of the concentration Biuret needs. What new difficulty could "
                "that create?",
        "options": [
            {"text": "It would give false negatives more often, because a "
                     "weaker colour is harder to see.", "correct": False,
             "why": "A more sensitive test gives fewer false negatives, which "
                    "is the point of making it."},
            {"text": "It would stop working on foods rich in protein, because "
                     "the colour would be too strong to read.",
             "correct": False,
             "why": "A strong colour is easy to read as a positive. Nothing "
                    "stops working."},
            {"text": "It would report traces that make no difference to a "
                     "diet, so a positive would mean less.", "correct": True},
            {"text": "It would need a water bath, and the extra heating would "
                     "destroy the protein it is looking for.",
             "correct": False,
             "why": "Nothing in the description says it needs heating, and "
                    "sensitivity is not a matter of temperature."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h24",
        "band": "harder",
        "text": "A technician accidentally fills the iodine bottle with "
                "water. The class tests five foods. What would they see, and "
                "how could they catch the mistake?",
        "options": [
            {"text": "Every food goes blue-black, and the error shows because "
                     "nothing comes out negative.", "correct": False,
             "why": "Water produces no colour at all, so nothing would go "
                    "blue-black."},
            {"text": "Only the potato changes, and the error shows because "
                     "the colour is paler than usual.", "correct": False,
             "why": "Water cannot make the potato change at all, however pale "
                    "the result might be."},
            {"text": "The results are random, and the error shows because the "
                     "class disagrees with one another.", "correct": False,
             "why": "There is nothing random about it; plain water gives the "
                    "same nothing on every food."},
            {"text": "Nothing changes on any food, and testing a known starch "
                     "such as flour would expose it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h25",
        "band": "harder",
        "text": "A student argues that milk is a better food than olive oil "
                "because milk gives three positives and olive oil gives one. "
                "Evaluate that argument.",
        "options": [
            {"text": "It is sound, because a food that comes out positive on "
                     "more of the tests is supplying more of what a body "
                     "needs from its diet.", "correct": False,
             "why": "Counting tests is not counting nutrition, and the tests "
                    "cover only four of the seven nutrients."},
            {"text": "It is sound for these two foods, though it would not "
                     "work for foods that are more alike.", "correct": False,
             "why": "The reasoning is wrong in every case, not just in close "
                    "ones, because a count is not a measure."},
            {"text": "It is wrong, because the number of positives is not a "
                     "measure of anything, and olive oil's lipid is a "
                     "required nutrient.", "correct": True},
            {"text": "It is wrong, because olive oil actually gives three "
                     "positives and milk only one.", "correct": False,
             "why": "The counts in the question are right: olive oil is "
                    "positive on the emulsion test alone."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h26",
        "band": "harder",
        "text": "Two foods both go blue-black with iodine, one within "
                "seconds and one after a full minute. What may and may not be "
                "said about them?",
        "options": [
            {"text": "Both contain starch that was detected; how fast the "
                     "colour came is not a measurement.", "correct": True},
            {"text": "The faster one contains more starch, since a stronger "
                     "sample reacts sooner.", "correct": False,
             "why": "Speed depends on how finely the food was crushed and how "
                    "the drops were placed as well."},
            {"text": "The slower one is a false positive, since a genuine "
                     "result appears straight away.", "correct": False,
             "why": "A slow colour is a real colour. Nothing about the delay "
                    "makes it false."},
            {"text": "Neither result counts, because the method does not say "
                     "how long to wait.", "correct": False,
             "why": "A blue-black is a detection whenever it appears, and "
                    "both foods gave one."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h27",
        "band": "harder",
        "text": "A class wants to find out whether bananas gain reducing "
                "sugar as they ripen, using Benedict's. What must they hold "
                "the same across the samples?",
        "options": [
            {"text": "Nothing in particular, since the test reports a "
                     "detection and detections cannot be unfair.",
             "correct": False,
             "why": "They want to compare, and comparing needs everything but "
                    "the ripeness held steady."},
            {"text": "The colour of the banana skin, so that every sample "
                     "looks alike before it is crushed.", "correct": False,
             "why": "Skin colour is the very thing that changes with "
                    "ripeness, so it cannot be held the same."},
            {"text": "The mass of banana, the volume of water, the volume of "
                     "Benedict's, the bath temperature and the time.",
             "correct": True},
            {"text": "Only the temperature of the water bath, since that is "
                     "the one condition the printed method actually names by "
                     "number.", "correct": False,
             "why": "The method names the volumes and the time as well, and "
                    "all of them change the colour."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h28",
        "band": "harder",
        "text": "A textbook says the four food tests 'show what a food is "
                "made of'. How fair is that description?",
        "options": [
            {"text": "Fair, since between them the four tests cover "
                     "everything a food can contain.", "correct": False,
             "why": "They cover four things. Vitamins, minerals, fibre and "
                    "water are all outside their reach."},
            {"text": "Unfair, since a test that reports a detection cannot "
                     "support any claim about a food at all.", "correct": False,
             "why": "A positive does support a claim — that the nutrient was "
                    "detected. The overreach is elsewhere."},
            {"text": "Fair for the positive results and unfair for the "
                     "negative ones, which is the only real weakness in the "
                     "description.", "correct": False,
             "why": "The bigger weakness is the four nutrients themselves: "
                    "three of the seven are never looked for."},
            {"text": "Unfair, since the tests report four nutrients, give no "
                     "amounts, and say nothing about the other three.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h29",
        "band": "harder",
        "text": "Laboratory reports use the phrase 'not detected' rather "
                "than 'absent'. What is being protected by that choice of "
                "words?",
        "options": [
            {"text": "The claim is held to what the method can show, since "
                     "every test has a level below which it sees nothing.",
             "correct": True},
            {"text": "The laboratory is protected from blame if the test was "
                     "carried out badly on the day.", "correct": False,
             "why": "The wording is not about blame. A perfectly run test "
                    "still cannot see below its own limit."},
            {"text": "The reader is being warned that the reagents used on "
                     "the day may well have been past their best by then.",
             "correct": False,
             "why": "Reagent quality would be reported separately. This "
                    "wording applies even to fresh reagent."},
            {"text": "The report avoids saying anything at all, so that no "
                     "conclusion can be challenged later.", "correct": False,
             "why": "It says something precise: this method found none. That "
                    "is a real result, not an evasion."},
        ],
        "figure": None,
    },
    {
        "id": "b3-02-h30",
        "band": "harder",
        "text": "Cooking oil is tested with Benedict's, iodine and Biuret, "
                "gives three negatives, and is declared 'pure fat'. What is "
                "wrong with that conclusion?",
        "options": [
            {"text": "The lipid was never confirmed, and three negatives "
                     "cannot establish purity in any case.", "correct": True},
            {"text": "Nothing is wrong, since ruling out the other three "
                     "nutrients leaves lipid as the only possibility.",
             "correct": False,
             "why": "The three negatives rule nothing out, and no test here "
                    "has actually looked for lipid."},
            {"text": "The three tests were run in the wrong order, and lipid "
                     "must always be tested for first.", "correct": False,
             "why": "There is no required order. The gap is the missing "
                    "emulsion test and the word 'pure'."},
            {"text": "Cooking oil cannot be tested with any of these "
                     "reagents, so all three results are meaningless.",
             "correct": False,
             "why": "All three can be run on oil, and all three gave honest "
                    "negatives."},
        ],
        "figure": None,
    },
]
