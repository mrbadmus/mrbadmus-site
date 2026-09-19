"""B3 lesson 06 — Enzymes in digestion: twelve questions (MRB-269).

These probe the two things this lesson exists to fix and the one thing it is
easiest to half-learn: that a catalyst comes out of its reaction unchanged,
that heat ruins an enzyme permanently and does not kill it, and that each of
the three named enzymes has one substrate, one product set and one pH it works
at. The distractors are built from the lesson's two declared misconceptions —
DIET-13 (enzymes are killed by heat) and DIET-14 (the enzyme gets used up as
the food is digested) — together with four errors the page's own bench and
cards are drawn to catch: that cold damages an enzyme the way heat does, that
protease works only in stomach acid, that an enzyme moves on to a second
substrate once the first runs out, and that bile helps lipase chemically or by
supplying energy rather than by multiplying the surface it works on. The lesson
carries no figures, so every question is figure=None.
"""

UNIT = "B3"
LESSON = "enzymes-in-digestion"
LESSON_NUMBER = 6

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-e01",
        "band": "easier",
        "text": "An enzyme is called a biological catalyst. What does calling "
                "it a catalyst tell you?",
        "options": [
            {"text": "It breaks large food molecules into pieces small enough "
                     "to be absorbed.",
             "correct": False,
             "why": "That is what digestion does, not what the word catalyst "
                    "means. A catalyst is defined by what does not happen to "
                    "it — it comes out of the reaction unchanged."},
            {"text": "It makes a reaction go faster without being used up by "
                     "it.",
             "correct": True},
            {"text": "It supplies the energy that the reaction needs in order "
                     "to happen.",
             "correct": False,
             "why": "An enzyme adds nothing to the reaction, energy included. "
                    "It only makes a reaction that would happen anyway happen "
                    "very much faster."},
            {"text": "It is slowly used up while the reaction it controls is "
                     "going on.",
             "correct": False,
             "why": "Weigh the amylase before and after and it has not gone "
                    "down. Filter it out at the end and it digests the next "
                    "kilogram of starch just as well."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e02",
        "band": "easier",
        "text": "Lipase has finished working on a fat droplet. Which pair of "
                "products has it made?",
        "options": [
            {"text": "Glucose and starch",
             "correct": False,
             "why": "Neither has anything to do with lipid. Starch is a "
                    "substrate rather than a product, and the enzyme that "
                    "turns starch into glucose is carbohydrase."},
            {"text": "Amino acids and protein",
             "correct": False,
             "why": "The same mistake the other way round: protein is "
                    "protease's substrate and amino acids are its products. A "
                    "list of products never contains its own substrate."},
            {"text": "Fatty acids and glycerol",
             "correct": True},
            {"text": "Glucose and glycerol",
             "correct": False,
             "why": "Glycerol is right and glucose is not. Lipid gives fatty "
                    "acids and glycerol; glucose comes only from a "
                    "carbohydrate such as starch."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e03",
        "band": "easier",
        "text": "A tube of protease is described as denatured. What has "
                "happened to it?",
        "options": [
            {"text": "Its shape has been destroyed, so it no longer fits its "
                     "substrate.",
             "correct": True},
            {"text": "It has been killed, so it can no longer carry out its "
                     "reaction.",
             "correct": False,
             "why": "An enzyme cannot be killed, because it was never alive — "
                    "no cell, no membrane, nothing that could die. The word is "
                    "denatured, and examiners take the difference seriously."},
            {"text": "It has been used up by all the protein it has already "
                     "digested.",
             "correct": False,
             "why": "That is a different wrong idea. An enzyme finishes every "
                    "cycle unchanged, and a denatured one is still sitting in "
                    "the tube — ruined, but not gone."},
            {"text": "It has been broken apart into the amino acids it was "
                     "built from.",
             "correct": False,
             "why": "Nothing has been cut up. The molecule is all still there; "
                    "heat has shaken its folds loose so the shape no longer "
                    "fits, which is not the same as being taken apart."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e04",
        "band": "easier",
        "text": "The bench is set to pH 2 — stomach. Which enzyme is in "
                "conditions it works well in?",
        "options": [
            {"text": "Carbohydrase, because it follows the food the whole way "
                     "down.",
             "correct": False,
             "why": "Carbohydrase is best at pH 7. Salivary amylase starts in "
                    "the mouth and stops in the acid of the stomach; it does "
                    "not carry on through."},
            {"text": "None of them, because pH 2 would denature any protein "
                     "you added.",
             "correct": False,
             "why": "That is exactly why the stomach protease is worth "
                    "noticing. Most proteins would denature at pH 2, but this "
                    "one is built to work there — it is unusual, not "
                    "impossible."},
            {"text": "Lipase, because it is the one built for the harshest "
                     "conditions.",
             "correct": False,
             "why": "Lipase is best at pH 8, slightly alkaline. pH 2 is at the "
                    "opposite end of the scale from the small intestine, where "
                    "lipase does its work."},
            {"text": "Protease, because the stomach version is built to work "
                     "in acid.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-06-s01",
        "band": "standard",
        "text": "Your pancreas makes only a few grams of enzyme a day, and yet "
                "you digest around a kilogram of food. Which fact explains "
                "that?",
        "options": [
            {"text": "Most of the food is broken down by stomach acid, with "
                     "enzymes doing little.",
             "correct": False,
             "why": "Acid on its own does not digest a meal. Carbohydrase, "
                    "protease and lipase do the cutting, and a few grams of "
                    "them genuinely is enough."},
            {"text": "A few grams is plenty because each molecule handles one "
                     "very large piece.",
             "correct": False,
             "why": "One molecule does not take one big piece — it takes piece "
                    "after piece. A single amylase molecule can bind, cut and "
                    "release thousands of times a second."},
            {"text": "Each molecule catalyses the reaction over and over, "
                     "unchanged every time.",
             "correct": True},
            {"text": "The pancreas makes far more than that whenever a large "
                     "meal arrives.",
             "correct": False,
             "why": "How much is made is not the answer. Even if the pancreas "
                    "doubled its output, a few grams could not cover a "
                    "kilogram unless each molecule were reused."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s02",
        "band": "standard",
        "text": "A tube of amylase is left in a fridge at 4 °C overnight and "
                "then warmed back to 37 °C. What happens when starch is added?",
        "options": [
            {"text": "It is digested normally — the cold slowed the enzyme but "
                     "damaged nothing.",
             "correct": True},
            {"text": "Nothing is digested: the cold destroyed the enzyme's "
                     "shape while it sat there.",
             "correct": False,
             "why": "Cold does not destroy shape. Molecules simply collide "
                    "less often, so the rate is low; warm it up and it "
                    "recovers completely. Only heat above about 50 °C is "
                    "permanent."},
            {"text": "Nothing is digested until the tube has been heated above "
                     "50 °C to restart it.",
             "correct": False,
             "why": "50 °C is the temperature that ruins an enzyme, not the "
                    "one that wakes it up. At 37 °C amylase is already about "
                    "as fast as it goes."},
            {"text": "Nothing is digested, because a night in the cold has "
                     "killed the enzyme.",
             "correct": False,
             "why": "Nothing was killed — an enzyme is a molecule and was "
                    "never alive. Nothing was damaged either, which is why a "
                    "fridge only slows food spoiling rather than stopping it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s03",
        "band": "standard",
        "text": "A student writes: “Stomach acid kills the amylase that came "
                "down from your mouth.” What is wrong with that sentence?",
        "options": [
            {"text": "Nothing — killed is a fair way of saying an enzyme has "
                     "stopped working.",
             "correct": False,
             "why": "It is not fair, and it costs marks. Killed suggests "
                    "something alive that could be replaced by growing more, "
                    "whereas a denatured enzyme is a permanently ruined "
                    "molecule."},
            {"text": "The amylase is not affected by acid at all — it keeps "
                     "working the whole way down.",
             "correct": False,
             "why": "It does stop. Amylase is best at pH 7 and the stomach is "
                    "about pH 2, which is why starch digestion only resumes "
                    "further along the gut."},
            {"text": "The acid uses the amylase up, which is not quite the "
                     "same as killing it.",
             "correct": False,
             "why": "Neither word fits. Nothing uses an enzyme up, and nothing "
                    "kills it — the acid changes its shape so that it no "
                    "longer fits starch."},
            {"text": "Killed is the wrong word: the amylase is denatured, and "
                     "it was never alive.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s04",
        "band": "standard",
        "text": "On the bench you put protease in the tube, set the pH to 8 — "
                "small intestine, and set the temperature to 37 °C. Predict "
                "the run.",
        "options": [
            {"text": "Almost nothing happens: protease works only in the acid "
                     "the stomach provides.",
             "correct": False,
             "why": "This is the trap the card is drawn to catch. Protease is "
                    "best at pH 2 in the stomach and at pH 8 in the small "
                    "intestine — two versions, two optima."},
            {"text": "Protein falls and amino acids climb, because pH 8 suits "
                     "protease too.",
             "correct": True},
            {"text": "Nothing happens: pH 8 denatures protease the way heat "
                     "above 50 °C would.",
             "correct": False,
             "why": "Alkali does not denature this enzyme. The pancreatic "
                    "protease is at home at pH 8 — the small intestine is "
                    "where it does most of its work."},
            {"text": "A little happens, but only once the pH has drifted back "
                     "down towards 2.",
             "correct": False,
             "why": "The pH does not drift back, and it does not need to. At "
                    "pH 8 the protease is already at one of the two pH values "
                    "it works best at."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-h01",
        "band": "harder",
        "text": "Jelly made with fresh pineapple never sets, but the same "
                "jelly made with tinned pineapple sets perfectly. Explain the "
                "difference.",
        "options": [
            {"text": "Tinned pineapple is sweeter, and the extra sugar helps "
                     "the gelatin set firmly.",
             "correct": False,
             "why": "Sugar is not what differs here. What differs is an "
                    "enzyme: fresh pineapple carries a working protease and "
                    "tinned pineapple does not."},
            {"text": "Fresh pineapple is more acidic, and acid stops gelatin "
                     "from setting properly.",
             "correct": False,
             "why": "Both are acidic — canning does not neutralise fruit. What "
                    "canning does is heat it, and heat is what stops an enzyme "
                    "permanently."},
            {"text": "Tinned pineapple has had its enzyme rinsed away by the "
                     "syrup it is canned in.",
             "correct": False,
             "why": "The enzyme is not washed out, it is ruined where it sits. "
                    "Canning heats the fruit, and above about 50 °C the "
                    "protease's shape is destroyed for good."},
            {"text": "Fresh pineapple holds a protease that cuts gelatin "
                     "apart; canning denatures it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h02",
        "band": "harder",
        "text": "Bile is not an enzyme — all it does is break one large fat "
                "drop into many tiny droplets. Lipase works on the surface of "
                "a droplet. So why does bile speed fat digestion up so much?",
        "options": [
            {"text": "Bile acts as a second catalyst, speeding the same "
                     "reaction up alongside the lipase.",
             "correct": False,
             "why": "Bile changes nothing chemically, as the question says. It "
                    "changes the shape the fat is in, not the reaction, and it "
                    "is not a catalyst at all."},
            {"text": "Tiny droplets have far more surface in total, so more "
                     "lipase can work at once.",
             "correct": True},
            {"text": "Bile cuts the lipid into fatty acids, and the lipase "
                     "then finishes off the glycerol.",
             "correct": False,
             "why": "Lipase makes both products itself — fatty acids and "
                    "glycerol. Bile makes no products at all; it only makes "
                    "the droplets smaller."},
            {"text": "Bile supplies the lipase with the energy it needs to "
                     "break the lipid apart.",
             "correct": False,
             "why": "Nothing supplies an enzyme with energy. A catalyst speeds "
                    "a reaction up without adding anything to it, and bile is "
                    "not even an enzyme."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h03",
        "band": "harder",
        "text": "Enzymes are not used up, so why does the pancreas have to "
                "release fresh amylase into the small intestine instead of "
                "reusing the amylase you made in your mouth?",
        "options": [
            {"text": "The amylase from the mouth is denatured by stomach acid "
                     "and never recovers.",
             "correct": True},
            {"text": "Each amylase molecule can only cut so many starch chains "
                     "before it stops.",
             "correct": False,
             "why": "There is no quota. A catalyst finishes every cycle in the "
                    "state it started in and is free to begin again — that is "
                    "the whole of what catalyst means."},
            {"text": "Salivary amylase is used up in the mouth, so none of it "
                     "ever travels further.",
             "correct": False,
             "why": "It is not used up; it is swallowed along with the food, "
                    "still intact. What stops it is the pH it meets in the "
                    "stomach, not the work it did."},
            {"text": "A different enzyme is needed there, because glucose is "
                     "only made further down.",
             "correct": False,
             "why": "It is the same reaction and the same kind of enzyme — "
                    "starch to glucose. The only thing that has changed is "
                    "that the first batch no longer works."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h04",
        "band": "harder",
        "text": "A tube holds starch, protein and lipid together, with "
                "carbohydrase as the only enzyme, at 37 °C and pH 7. What do "
                "the counters read at the end of the run?",
        "options": [
            {"text": "All three substrates fall — a catalyst speeds up "
                     "whichever reaction it meets.",
             "correct": False,
             "why": "An enzyme is not a general-purpose tool. Each one has a "
                    "shape that fits one substrate, so carbohydrase cannot "
                    "touch the protein or the lipid at all."},
            {"text": "Starch falls, and the carbohydrase count falls with it "
                     "as the work gets done.",
             "correct": False,
             "why": "The third counter never moves. Watch it on the bench: "
                    "substrate down, product up, enzyme still reading forty at "
                    "the end."},
            {"text": "Starch falls to nothing; protein and lipid are "
                     "untouched, and the enzyme is unchanged.",
             "correct": True},
            {"text": "Starch falls first, then the carbohydrase starts on the "
                     "protein once starch runs out.",
             "correct": False,
             "why": "It has nothing to start on. The shape that fits starch "
                    "does not fit protein, so once the starch is gone this "
                    "enzyme simply stops."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Six further rows, two per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-e05",
        "band": "easier",
        "text": "Carbohydrase, also called amylase, fits one substrate. Which "
                "reaction does it speed up?",
        "options": [
            {"text": "Starch to glucose.", "correct": True},
            {"text": "Protein to amino acids.", "correct": False,
             "why": "That reaction belongs to protease. One enzyme has a "
                    "shape that fits one substrate, and carbohydrase cannot "
                    "touch protein."},
            {"text": "Lipid to fatty acids and glycerol.", "correct": False,
             "why": "That reaction belongs to lipase, made in the pancreas. "
                    "Carbohydrase has no effect on lipid at all."},
            {"text": "Glucose to starch.", "correct": False,
             "why": "Digestion runs the other way. Long chains are cut into "
                    "short molecules so that they can be absorbed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e06",
        "band": "easier",
        "text": "Which of the three digestive enzymes is made in the stomach "
                "as well as in the pancreas?",
        "options": [
            {"text": "Carbohydrase — it follows the food the whole way down.",
             "correct": False,
             "why": "Carbohydrase is made in the salivary glands and the "
                    "pancreas, and stomach acid is what stops the mouth's "
                    "supply working."},
            {"text": "Lipase — the stomach is where fat digestion begins.",
             "correct": False,
             "why": "Lipase is made in the pancreas only, and fat digestion "
                    "is done in the small intestine."},
            {"text": "Protease — the stomach version is built to work in "
                     "acid.", "correct": True},
            {"text": "None of them — the stomach makes acid and no enzymes at "
                     "all.", "correct": False,
             "why": "The stomach makes protease as well as acid, which is why "
                    "protein digestion begins there."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-06-s05",
        "band": "standard",
        "text": "A tube holds lipase and lipid at 37 °C, with the pH set to "
                "2. What would the counters show, and what one change would "
                "put it right?",
        "options": [
            {"text": "Full rate, because 37 °C is the temperature every "
                     "enzyme works fastest at.", "correct": False,
             "why": "Temperature is only half of it. Lipase works best at "
                    "about pH 8, and pH 2 is a long way from that."},
            {"text": "Nothing made, and nothing will fix it, because the acid "
                     "has ruined the enzyme.", "correct": False,
             "why": "Ruining an enzyme permanently is what heat above about "
                    "50 °C does. Here every lipase molecule is intact and "
                    "would work at pH 8."},
            {"text": "A little made, put right by raising the temperature to "
                     "50 °C instead.", "correct": False,
             "why": "50 °C is the threshold above which the shape is "
                    "destroyed for good. The problem in this tube is the pH, "
                    "not the temperature."},
            {"text": "Little or nothing made, put right by moving the pH to "
                     "8.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s06",
        "band": "standard",
        "text": "The same food spoils far more slowly in a fridge than in a "
                "warm room, and nothing has been added to either sample. "
                "Explain that using enzymes.",
        "options": [
            {"text": "The cold has denatured the enzymes in the food, so "
                     "spoiling has stopped altogether.", "correct": False,
             "why": "Cold damages nothing. Denaturing is what heat above "
                    "about 50 °C does, and it would be permanent — food out of "
                    "a fridge spoils perfectly well."},
            {"text": "Cold slows the reactions without damaging anything, so "
                     "spoiling is slower rather than stopped.", "correct": True},
            {"text": "The fridge kills the enzymes, and a dead enzyme cannot "
                     "spoil food.", "correct": False,
             "why": "An enzyme is a molecule and was never alive, so nothing "
                    "about it can be killed. It is slowed, and it recovers "
                    "completely on warming."},
            {"text": "Cold makes the enzymes work faster, so the spoiling is "
                     "over before anybody notices it.", "correct": False,
             "why": "Molecules collide less often when they are cold, so the "
                    "rate is low. That is why the fridge buys you time."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-h05",
        "band": "harder",
        "text": "The same mass of amylase goes into two identical tubes of "
                "starch solution, one held at 20 °C and one at 37 °C. Both are "
                "left until no starch remains. What differs, and what does "
                "not?",
        "options": [
            {"text": "The 20 °C tube ends with less glucose, because a cold "
                     "enzyme makes less product.", "correct": False,
             "why": "Both tubes started with the same starch and both "
                    "finished it, so both made the same glucose. What differs "
                    "is how long it took."},
            {"text": "The 20 °C tube ends with less amylase, because a slow "
                     "reaction consumes more of it.", "correct": False,
             "why": "An enzyme is not used up by the reaction it catalyses, "
                    "at any temperature. Both tubes end with all their "
                    "amylase."},
            {"text": "The 20 °C tube takes far longer, and both end with the "
                     "starch gone and the amylase unchanged.", "correct": True},
            {"text": "Nothing differs — both are below 50 °C, so both run at "
                     "exactly the same rate.", "correct": False,
             "why": "Below the optimum the rate falls as it gets colder. "
                    "50 °C is where the damage begins, not where temperature "
                    "starts to matter."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h06",
        "band": "harder",
        "text": "A student argues that stomach acid must be what digests "
                "protein, since protein digestion begins in the stomach and "
                "the stomach is full of acid. What is the strongest "
                "correction?",
        "options": [
            {"text": "Protease does the digesting; the acid supplies the pH "
                     "protease works best at.", "correct": True},
            {"text": "The acid does digest the protein, and protease only "
                     "finishes off what is left.", "correct": False,
             "why": "The acid digests nothing. What it does is hold the "
                    "stomach at about pH 2 and kill most of the bacteria that "
                    "arrived with the meal."},
            {"text": "Protein digestion does not begin in the stomach, so the "
                     "whole argument falls.", "correct": False,
             "why": "It does begin there, and that is the one part of the "
                    "reasoning that is right. What is wrong is which molecule "
                    "does the cutting."},
            {"text": "Acid denatures any protein, so no protein digestion can "
                     "happen in the stomach at all.", "correct": False,
             "why": "Stomach protease is a genuinely specialised molecule "
                    "built to work at pH 2, which is unusual for a protein. "
                    "Digestion happens there."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up ───────────────────────────────────────────
    # Twenty-four further rows per band, appended at bank_position 12+ so
    # the original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-e07",
        "band": "easier",
        "text": "What is the substrate of an enzyme?",
        "options": [
            {"text": "The substance an enzyme works on.", "correct": True},
            {"text": "The tube or container an enzyme is dissolved in for a "
                     "reaction.", "correct": False,
             "why": "The container is not part of the biology at all — a "
                    "substrate is a substance, the one the enzyme acts on."},
            {"text": "Whatever the enzyme reaction eventually produces.",
             "correct": False,
             "why": "That is the product, not the substrate. The substrate "
                    "is what goes in; the product is what comes out."},
            {"text": "Another name for the enzyme molecule itself.",
             "correct": False,
             "why": "The substrate is a separate molecule the enzyme acts "
                    "on, not another name for the enzyme."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e08",
        "band": "easier",
        "text": "When an enzyme is denatured, what actually happens to it?",
        "options": [
            {"text": "It shrinks to a much smaller size than before.",
             "correct": False,
             "why": "Denaturing is about the shape unfolding, not the "
                    "molecule shrinking."},
            {"text": "The folds holding its shape come apart, so it no "
                     "longer fits its substrate.", "correct": True},
            {"text": "It is cut apart into smaller pieces by the heat.",
             "correct": False,
             "why": "Nothing is cut apart — the molecule is all still there, "
                    "just with its shape unfolded."},
            {"text": "It turns into a completely different type of "
                     "molecule entirely, made of different atoms.",
             "correct": False,
             "why": "It stays the same kind of molecule throughout — what "
                    "changes is its shape, not what it is made of."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e09",
        "band": "easier",
        "text": "Which is the best description of an enzyme?",
        "options": [
            {"text": "A type of food that supplies energy to the body.",
             "correct": False,
             "why": "An enzyme is not a food or a nutrient — it speeds up a "
                    "reaction rather than being eaten for energy."},
            {"text": "A general term for any chemical found in the gut.",
             "correct": False,
             "why": "Not every chemical in the gut is an enzyme — stomach "
                    "acid, for instance, is not one."},
            {"text": "A protein that speeds up one particular reaction.",
             "correct": True},
            {"text": "A living cell that carries out digestion.",
             "correct": False,
             "why": "An enzyme is a molecule, not a cell, and it was never "
                    "alive in the first place."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e10",
        "band": "easier",
        "text": "Which enzyme works best at pH 7, roughly neutral?",
        "options": [
            {"text": "Protease, at both of its optima.", "correct": False,
             "why": "Protease's two optima are pH 2 and pH 8 — neither of "
                    "them is neutral."},
            {"text": "Lipase.", "correct": False,
             "why": "Lipase is best at pH 8, slightly alkaline, not pH 7."},
            {"text": "None of the three named enzymes.", "correct": False,
             "why": "Carbohydrase's optimum is pH 7, so one of the three "
                    "does work best there."},
            {"text": "Carbohydrase.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e11",
        "band": "easier",
        "text": "Which enzyme works best at pH 8, slightly alkaline?",
        "options": [
            {"text": "Lipase.", "correct": True},
            {"text": "Only the mouth's version of protease.", "correct": False,
             "why": "The mouth has no protease at all. Protease's alkaline "
                    "optimum belongs to the pancreatic version, in the small "
                    "intestine."},
            {"text": "None of the three named enzymes.", "correct": False,
             "why": "Lipase's optimum is pH 8, so one of the three does work "
                    "best there."},
            {"text": "Carbohydrase.", "correct": False,
             "why": "Carbohydrase's optimum is pH 7, neutral, not pH 8."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e12",
        "band": "easier",
        "text": "Protease is unusual among the three named enzymes because it "
                "has how many optimum pH values?",
        "options": [
            {"text": "None — protease works equally well at any pH.",
             "correct": False,
             "why": "Protease is far from indifferent to pH — it has two "
                    "specific optima where it works best."},
            {"text": "Two — pH 2 in the stomach and pH 8 in the small "
                     "intestine.", "correct": True},
            {"text": "One, the same as carbohydrase and lipase.",
             "correct": False,
             "why": "Protease is unusual precisely because it has two "
                    "optima, not one like the other two named enzymes."},
            {"text": "Three, one for each stop along the digestive system "
                     "that food actually passes through.", "correct": False,
             "why": "Protease is made in only two places — the stomach and "
                    "the pancreas — giving it two optima, not three."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e13",
        "band": "easier",
        "text": "Roughly what temperature do human digestive enzymes work "
                "fastest at?",
        "options": [
            {"text": "About 100 °C.", "correct": False,
             "why": "That is far above the point where an enzyme's shape is "
                    "permanently destroyed."},
            {"text": "About 70 °C.", "correct": False,
             "why": "That is well past the temperature where digestive "
                    "enzymes are denatured, not their fastest point."},
            {"text": "About 37 °C.", "correct": True},
            {"text": "About 0 °C.", "correct": False,
             "why": "That is far too cold — enzymes work very slowly near "
                    "freezing, not at their fastest."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e14",
        "band": "easier",
        "text": "Above roughly what temperature is a digestive enzyme "
                "permanently destroyed?",
        "options": [
            {"text": "About 10 °C.", "correct": False,
             "why": "That is well below the enzyme's optimum, not the "
                    "temperature that damages it."},
            {"text": "About 37 °C.", "correct": False,
             "why": "That is the temperature the enzyme works fastest at, "
                    "not the one that destroys it."},
            {"text": "There is no such temperature — enzymes cannot be "
                     "damaged by heat.", "correct": False,
             "why": "Heat above about 50 °C genuinely does destroy an "
                    "enzyme's shape, permanently."},
            {"text": "About 50 °C.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e15",
        "band": "easier",
        "text": "Once an enzyme has been denatured, can cooling it back to "
                "37 °C undo the damage?",
        "options": [
            {"text": "No — the damage is permanent.", "correct": True},
            {"text": "Yes, since 37 °C is the enzyme's own optimum "
                     "temperature.", "correct": False,
             "why": "Being at the right temperature again does not restore "
                    "a shape that heat has already destroyed."},
            {"text": "Yes, but only if it is cooled very slowly.",
             "correct": False,
             "why": "Speed of cooling makes no difference — once denatured, "
                    "the shape does not come back at any cooling rate."},
            {"text": "It depends on which of the three named enzymes it is.",
             "correct": False,
             "why": "The permanence of denaturing applies to all of them "
                    "alike, not to some more than others."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e16",
        "band": "easier",
        "text": "What does an enzyme do to its substrate?",
        "options": [
            {"text": "Destroys it completely, leaving nothing behind.",
             "correct": False,
             "why": "The substrate is converted into product, not destroyed "
                    "with nothing left — the atoms end up in the product."},
            {"text": "Speeds up its conversion into product, without being "
                     "changed itself.", "correct": True},
            {"text": "Stores it inside its own structure until enough has "
                     "built up to react with it all at once.", "correct": False,
             "why": "An enzyme does not store its substrate — it speeds up "
                    "the conversion straight away."},
            {"text": "Absorbs it directly into the enzyme's own structure.",
             "correct": False,
             "why": "The substrate is converted into product and released — "
                    "it does not become part of the enzyme."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e17",
        "band": "easier",
        "text": "Lipid is the substrate of which named digestive enzyme?",
        "options": [
            {"text": "Protease.", "correct": False,
             "why": "Protease acts on protein, not lipid."},
            {"text": "All three act equally on lipid.", "correct": False,
             "why": "Each of the three enzymes has its own single "
                    "substrate — only lipase acts on lipid."},
            {"text": "Lipase.", "correct": True},
            {"text": "Carbohydrase.", "correct": False,
             "why": "Carbohydrase acts on starch, not lipid."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e18",
        "band": "easier",
        "text": "A meal's protein is cut into amino acids by which named "
                "enzyme?",
        "options": [
            {"text": "Lipase.", "correct": False,
             "why": "Lipase acts on lipid, not protein."},
            {"text": "Carbohydrase.", "correct": False,
             "why": "Carbohydrase acts on starch, not protein."},
            {"text": "None of the three — protein is not broken down by an "
                     "enzyme at all.", "correct": False,
             "why": "Protease is specifically the enzyme that breaks protein "
                    "down into amino acids."},
            {"text": "Protease.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e19",
        "band": "easier",
        "text": "Which enzyme is responsible for cutting starch into "
                "glucose?",
        "options": [
            {"text": "Carbohydrase.", "correct": True},
            {"text": "Protease.", "correct": False,
             "why": "Protease acts on protein, not starch."},
            {"text": "Lipase.", "correct": False,
             "why": "Lipase acts on lipid, not starch."},
            {"text": "Bile.", "correct": False,
             "why": "Bile is not an enzyme at all, and it has no effect on "
                    "starch."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e20",
        "band": "easier",
        "text": "While a reaction is running, what happens to the number of "
                "enzyme molecules present?",
        "options": [
            {"text": "It falls to zero once all the substrate is gone.",
             "correct": False,
             "why": "The enzyme molecules remain present even once the "
                    "substrate has run out — none of them are used up."},
            {"text": "It stays the same throughout.", "correct": True},
            {"text": "It falls steadily as the substrate is used up.",
             "correct": False,
             "why": "The substrate count falls, not the enzyme count — the "
                    "enzyme is not consumed by the reaction."},
            {"text": "It rises as more enzyme is produced to keep up.",
             "correct": False,
             "why": "No new enzyme is produced during a single reaction — "
                    "the same molecules simply keep working."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e21",
        "band": "easier",
        "text": "An enzyme is cooled well below its optimum temperature but "
                "stays below the point that denatures it. What happens to "
                "its shape?",
        "options": [
            {"text": "It folds into a different, more compact shape.",
             "correct": False,
             "why": "Cold does not reshape the enzyme at all — it simply "
                    "slows down how often it meets its substrate."},
            {"text": "It becomes more effective than it is at its "
                     "optimum.", "correct": False,
             "why": "Being colder than the optimum lowers the rate, rather "
                    "than making the enzyme more effective."},
            {"text": "Nothing — the shape is undamaged, only the rate is "
                     "low.", "correct": True},
            {"text": "It is destroyed in exactly the same way heat destroys "
                     "it.", "correct": False,
             "why": "Cold does not destroy an enzyme's shape — only heat "
                    "above about 50 °C does that."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e22",
        "band": "easier",
        "text": "How does an enzyme's rate at 37 °C compare with its rate "
                "just above 50 °C?",
        "options": [
            {"text": "Roughly the same at both temperatures.",
             "correct": False,
             "why": "The two temperatures give very different results — "
                    "fast at 37 °C, ruined above 50 °C."},
            {"text": "Slower at 37 °C than it runs just above 50 °C, where "
                     "it is supposedly working even harder.", "correct": False,
             "why": "It is the other way round — 37 °C is near the "
                    "optimum, and above 50 °C the enzyme is destroyed."},
            {"text": "Zero at both temperatures.", "correct": False,
             "why": "37 °C is close to the optimum, where the rate is high, "
                    "not zero."},
            {"text": "Near its fastest at 37 °C; ruined and near zero above "
                     "50 °C.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e23",
        "band": "easier",
        "text": "Which word do examiners want instead of “killed” for an "
                "enzyme ruined by heat?",
        "options": [
            {"text": "Denatured.", "correct": True},
            {"text": "Extinct.", "correct": False,
             "why": "Extinct describes a species dying out, not a single "
                    "molecule losing its shape."},
            {"text": "Digested.", "correct": False,
             "why": "Digested describes an enzyme's own substrate being cut "
                    "up, not the enzyme losing its own shape."},
            {"text": "Absorbed.", "correct": False,
             "why": "Absorbed describes crossing the gut wall into the "
                    "blood, unrelated to an enzyme losing its shape."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e24",
        "band": "easier",
        "text": "Was an enzyme ever alive before it was denatured?",
        "options": [
            {"text": "Yes, but only while it was still inside the body.",
             "correct": False,
             "why": "Location does not make a molecule alive — an enzyme is "
                    "never alive, inside the body or out of it."},
            {"text": "No — it is a molecule, and molecules are never "
                     "alive.", "correct": True},
            {"text": "Yes, until the heat killed it.", "correct": False,
             "why": "An enzyme has no cell, no membrane and nothing that "
                    "could be alive in the first place."},
            {"text": "Only the enzymes made in the pancreas were ever "
                     "alive.", "correct": False,
             "why": "Where an enzyme is made makes no difference — none of "
                    "them are alive, whichever organ produced them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e25",
        "band": "easier",
        "text": "What does calling something a catalyst mean?",
        "options": [
            {"text": "It is the name for any molecule made in a gland.",
             "correct": False,
             "why": "Plenty of molecules made in glands are not catalysts — "
                    "the word specifically means speeding a reaction up."},
            {"text": "It reacts once and then has to be replaced.",
             "correct": False,
             "why": "A catalyst is defined by not needing to be replaced — "
                    "it comes out of the reaction unchanged, ready to react "
                    "again."},
            {"text": "It speeds a reaction up without being used up by "
                     "it.", "correct": True},
            {"text": "It is a substance the body absorbs for energy.",
             "correct": False,
             "why": "A catalyst is not a nutrient absorbed for energy — it "
                    "speeds up a reaction instead."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e26",
        "band": "easier",
        "text": "As a reaction proceeds, what happens to the amount of "
                "substrate and the amount of product?",
        "options": [
            {"text": "Substrate rises; product falls.", "correct": False,
             "why": "That is the reverse of what happens — substrate is "
                    "being used up, so it falls, while product builds up."},
            {"text": "Both rise together throughout the reaction.",
             "correct": False,
             "why": "Substrate cannot rise while it is being converted — it "
                    "falls as the product it turns into rises."},
            {"text": "Both stay constant the whole time.", "correct": False,
             "why": "A reaction that is actually happening changes both "
                    "amounts — substrate down, product up."},
            {"text": "Substrate falls; product rises.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e27",
        "band": "easier",
        "text": "A single amylase molecule can be reused how often?",
        "options": [
            {"text": "Thousands of times a second, in some cases.",
             "correct": True},
            {"text": "Exactly once, before it has to be replaced.",
             "correct": False,
             "why": "An enzyme is not used up after one use — it is free to "
                    "bind and cut again immediately."},
            {"text": "Only a handful of times before it wears out.",
             "correct": False,
             "why": "There is no wearing out described — a catalyst "
                    "finishes each cycle unchanged and keeps going."},
            {"text": "Once per meal, and then it rests until the next one.",
             "correct": False,
             "why": "An enzyme does not rest between meals — while it is "
                    "working, it cuts far more than once per meal."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e28",
        "band": "easier",
        "text": "What gives an enzyme its specificity for one particular "
                "substrate?",
        "options": [
            {"text": "How much of it is present.", "correct": False,
             "why": "Amount affects the rate, not which substrate the "
                    "enzyme is able to work on."},
            {"text": "Its shape.", "correct": True},
            {"text": "Its colour.", "correct": False,
             "why": "Enzymes are not identified or matched to a substrate "
                    "by colour — shape is what decides the fit."},
            {"text": "Which organ happens to release it.", "correct": False,
             "why": "The releasing organ does not decide specificity — the "
                    "molecule's own shape is what fits one substrate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e29",
        "band": "easier",
        "text": "What does an enzyme's “optimum pH” mean?",
        "options": [
            {"text": "The pH that permanently destroys its shape.",
             "correct": False,
             "why": "That describes a damaging pH, the opposite of the one "
                    "an enzyme works best at."},
            {"text": "The pH of the organ that stores the enzyme before "
                     "release.", "correct": False,
             "why": "Optimum pH is about where the enzyme works fastest, "
                    "not about storage conditions."},
            {"text": "The pH at which it works fastest.", "correct": True},
            {"text": "The only pH at which it works at all.",
             "correct": False,
             "why": "Many enzymes still work, more slowly, away from their "
                    "optimum — it is not the only pH that produces any "
                    "activity."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-e30",
        "band": "easier",
        "text": "Match each named enzyme to what it breaks down: "
                "carbohydrase, protease, lipase.",
        "options": [
            {"text": "Protein; lipid; starch.", "correct": False,
             "why": "That shuffles the pairings. Carbohydrase acts on "
                    "starch, protease on protein and lipase on lipid."},
            {"text": "Lipid; starch; protein.", "correct": False,
             "why": "That shuffles the pairings the other way. Carbohydrase "
                    "is starch, protease is protein and lipase is lipid."},
            {"text": "Starch; lipid; protein.", "correct": False,
             "why": "Protease and lipase are swapped here — protease acts "
                    "on protein, and lipase on lipid."},
            {"text": "Starch; protein; lipid.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-06-s07",
        "band": "standard",
        "text": "A tube has a fixed amount of enzyme and plenty of "
                "substrate. Predict what happens to the rate if you add "
                "even more substrate, with the enzyme amount unchanged.",
        "options": [
            {"text": "The rate stays about the same, since the enzyme "
                     "amount is what is now limiting it.", "correct": True},
            {"text": "The rate keeps rising without limit as more substrate "
                     "is added.", "correct": False,
             "why": "With a fixed number of enzyme molecules, there are "
                    "only so many reactions that can happen at once — extra "
                    "substrate beyond that point changes little."},
            {"text": "The rate falls, since the enzyme becomes diluted by "
                     "the extra substrate flooding into the tube.",
             "correct": False,
             "why": "Adding substrate does not dilute the enzyme in the "
                    "way this suggests — the enzyme count itself is what "
                    "caps the rate here."},
            {"text": "The reaction stops completely once too much substrate "
                     "is present.", "correct": False,
             "why": "Extra substrate does not stop the reaction — it simply "
                    "waits its turn, since the enzyme amount is already the "
                    "limiting factor."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s08",
        "band": "standard",
        "text": "A meal contains starch and protein. Once all the starch has "
                "been cut into glucose, what does the carbohydrase in the "
                "tube do next?",
        "options": [
            {"text": "It breaks down into smaller enzyme fragments that can "
                     "work on protein.", "correct": False,
             "why": "The carbohydrase molecule stays whole and unchanged — "
                    "it does not break apart into new enzymes."},
            {"text": "Nothing — its shape only fits starch, so it cannot "
                     "start on the protein.", "correct": True},
            {"text": "It switches to working on the protein instead.",
             "correct": False,
             "why": "An enzyme's shape fits one substrate only — "
                    "carbohydrase cannot switch to protein once starch runs "
                    "out."},
            {"text": "It changes its own shape to match whatever substrate "
                     "remains.", "correct": False,
             "why": "An enzyme's shape is fixed, not something it reshapes "
                    "to fit a new substrate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s09",
        "band": "standard",
        "text": "A tube has plenty of substrate and a small amount of "
                "enzyme. Predict the effect of doubling the amount of "
                "enzyme, keeping the substrate the same.",
        "options": [
            {"text": "The rate falls, since more enzyme molecules get in "
                     "each other's way.", "correct": False,
             "why": "There is no such crowding effect described — more "
                    "enzyme with plenty of substrate raises the rate rather "
                    "than lowering it."},
            {"text": "The reaction finishes with less total product than "
                     "before.", "correct": False,
             "why": "The total product made depends on how much substrate "
                    "there is, not on how much enzyme — doubling enzyme "
                    "changes speed, not the eventual total."},
            {"text": "The rate roughly doubles, since twice as many "
                     "molecules can react at once.", "correct": True},
            {"text": "The rate stays exactly the same, since substrate "
                     "amount is all that matters.", "correct": False,
             "why": "With plenty of substrate available, adding more "
                    "enzyme lets more reactions happen at the same time, "
                    "raising the rate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s10",
        "band": "standard",
        "text": "A factory manager suggests heating an enzyme solution to "
                "60 °C to make it work faster. Explain why this is a "
                "mistake.",
        "options": [
            {"text": "60 °C is too cold to have any effect on the "
                     "enzyme.", "correct": False,
             "why": "60 °C is far hotter than the enzyme's optimum, not too "
                    "cold — it is well past the point of permanent damage."},
            {"text": "Heat only affects the substrate, never the enzyme "
                     "itself.", "correct": False,
             "why": "Heat above about 50 °C directly destroys the enzyme's "
                    "own shape, not only the substrate."},
            {"text": "It is not a mistake — higher temperature always makes "
                     "an enzyme work faster.", "correct": False,
             "why": "That is only true below the optimum. Above about "
                    "50 °C the enzyme is destroyed rather than sped up."},
            {"text": "60 °C is well above the point where the enzyme's "
                     "shape is permanently destroyed.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s11",
        "band": "standard",
        "text": "While amylase cuts a starch chain into shorter sugars, does "
                "the amylase molecule's own shape change during that "
                "cycle?",
        "options": [
            {"text": "No — it finishes the cycle in the same shape it "
                     "started in.", "correct": True},
            {"text": "Yes, slightly, and this gradually wears the molecule "
                     "down over time.", "correct": False,
             "why": "A catalyst finishes each cycle unchanged — there is no "
                    "gradual wearing down described anywhere."},
            {"text": "Yes, it reshapes itself to become the finished sugar "
                     "product.", "correct": False,
             "why": "The enzyme and the product are two separate molecules "
                    "— the enzyme is not converted into its own product."},
            {"text": "It cannot be answered without knowing how much starch "
                     "is present.", "correct": False,
             "why": "The amount of substrate present does not change "
                    "whether the enzyme itself stays the same shape each "
                    "cycle — it always does."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s12",
        "band": "standard",
        "text": "A technician needs to stop an amylase reaction at an exact "
                "moment, for good, so the product made up to that point "
                "can be measured. Which action would do that?",
        "options": [
            {"text": "Simply wait, since an amylase molecule wears out "
                     "after a few minutes.", "correct": False,
             "why": "An enzyme is not worn out by the reaction it "
                    "catalyses. Left alone, it keeps working for as long "
                    "as substrate remains."},
            {"text": "Heat the tube well above 50 °C, destroying the "
                     "enzyme's shape.", "correct": True},
            {"text": "Stand the tube in ice, which halts the reaction "
                     "for good.", "correct": False,
             "why": "Ice slows the reaction almost to a stop, but the "
                    "enzyme is undamaged and starts working again as soon "
                    "as the tube warms up."},
            {"text": "Add a large amount of extra starch, crowding the "
                     "enzyme out.", "correct": False,
             "why": "Extra substrate gives the enzyme more to do, not "
                    "less. The reaction would carry on rather than stop."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s13",
        "band": "standard",
        "text": "Salivary amylase meets stomach acid and stops working. If "
                "that same sample is later returned to a neutral pH, does "
                "it start working again?",
        "options": [
            {"text": "Yes, but it takes several hours to recover fully.",
             "correct": False,
             "why": "There is no recovery over time described — the change "
                    "the acid causes does not reverse at all."},
            {"text": "It cannot be answered, since amylase never actually "
                     "meets stomach acid.", "correct": False,
             "why": "Amylase from saliva is swallowed along with the food "
                    "and does meet the stomach's acid directly."},
            {"text": "No — the acid has already changed its shape "
                     "permanently.", "correct": True},
            {"text": "Yes, since returning to neutral pH restores its "
                     "original shape.", "correct": False,
             "why": "The change caused by the acid is described as "
                    "permanent — reaching a friendlier pH afterwards does "
                    "not reverse it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s14",
        "band": "standard",
        "text": "Explain why “denatured” is a more accurate word than "
                "“dead” for a ruined enzyme.",
        "options": [
            {"text": "Denatured means exactly the same thing as dead, so "
                     "either word is equally accurate.", "correct": False,
             "why": "The words carry different, and importantly different, "
                    "implications — dead wrongly suggests the molecule was "
                    "once alive."},
            {"text": "Dead is more accurate, since the enzyme genuinely "
                     "stops functioning altogether.", "correct": False,
             "why": "Stopping is real, but “dead” is still the wrong word — "
                    "an enzyme has no life to lose in the first place."},
            {"text": "Neither word applies, since a ruined enzyme can "
                     "always be replaced with a fresh one.", "correct": False,
             "why": "Being replaceable does not decide which word is "
                    "accurate — “denatured” is right because the molecule "
                    "was never alive to begin with."},
            {"text": "Dead implies something that was once alive, and an "
                     "enzyme never was.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s15",
        "band": "standard",
        "text": "Protease's rate is measured at pH 2 (its optimum), then at "
                "pH 4, then at pH 6. Predict the general trend, without "
                "using exact numbers.",
        "options": [
            {"text": "The rate falls as the pH moves further from the "
                     "optimum.", "correct": True},
            {"text": "The rate rises steadily as the pH moves away from "
                     "the optimum.", "correct": False,
             "why": "Moving away from an optimum lowers a reaction's rate — "
                    "it does not raise it further from that point."},
            {"text": "The rate stays exactly the same at all three pH "
                     "values.", "correct": False,
             "why": "An optimum being an optimum means the rate is "
                    "specifically highest there and lower elsewhere."},
            {"text": "The rate becomes zero immediately at any pH other "
                     "than 2.", "correct": False,
             "why": "The rate falls gradually as pH moves away from the "
                    "optimum, rather than dropping to zero the instant it "
                    "changes."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s16",
        "band": "standard",
        "text": "Raising the temperature from 20 °C to 37 °C speeds an "
                "enzyme's reaction up. Raising it further, past 50 °C, "
                "ruins it. Explain why the same action — raising the "
                "temperature — has such different effects.",
        "options": [
            {"text": "The enzyme actually works fastest at both low and "
                     "high temperatures, with a dip in the middle.",
             "correct": False,
             "why": "The pattern runs the other way — the rate rises "
                    "towards the optimum and then collapses once "
                    "denaturing sets in, not a dip in the middle."},
            {"text": "Below the optimum, warmth speeds molecules up; above "
                     "the denaturing point, heat destroys the enzyme's "
                     "shape instead.", "correct": True},
            {"text": "It is not really the same action — raising "
                     "temperature by a small amount and a large amount are "
                     "two unrelated processes.", "correct": False,
             "why": "It genuinely is the same variable, temperature, being "
                    "raised throughout — what changes is which effect "
                    "dominates at each range."},
            {"text": "Warmth always speeds an enzyme up, and the ruined "
                     "state at high temperature is a separate, unrelated "
                     "effect.", "correct": False,
             "why": "The two effects are directly connected — the same "
                    "rising heat that speeds molecules up below the "
                    "optimum eventually destroys the enzyme's shape above "
                    "it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s17",
        "band": "standard",
        "text": "A tube is set up with double the usual enzyme AND double "
                "the usual substrate. Predict what happens to how long the "
                "reaction takes to finish, compared with the usual amounts.",
        "options": [
            {"text": "It takes twice as long, since there is more of "
                     "everything to process.", "correct": False,
             "why": "More enzyme is available too, matching the extra "
                    "substrate, so the time need not lengthen."},
            {"text": "It cannot finish at all, since doubling both amounts "
                     "overloads the reaction.", "correct": False,
             "why": "Nothing about doubling both amounts together stops "
                    "the reaction — it simply scales up."},
            {"text": "It finishes in roughly the same time, since both "
                     "amounts have grown together.", "correct": True},
            {"text": "It finishes twice as fast, since only the enzyme "
                     "amount matters.", "correct": False,
             "why": "Substrate has also doubled here, so there is twice as "
                    "much for the doubled enzyme to get through — the "
                    "timing stays roughly the same."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s18",
        "band": "standard",
        "text": "Explain how a single amylase molecule being reused "
                "thousands of times a second connects to only a few grams "
                "of enzyme handling a whole meal.",
        "options": [
            {"text": "It does not connect — the few grams figure and the "
                     "reuse rate describe two separate, unrelated things.",
             "correct": False,
             "why": "They are directly connected — rapid reuse is exactly "
                    "what lets a small mass of enzyme handle a large meal."},
            {"text": "The few grams figure only applies because most of a "
                     "meal is never actually digested.", "correct": False,
             "why": "Most of a meal genuinely is digested — the small mass "
                    "of enzyme is enough precisely because each molecule "
                    "works repeatedly."},
            {"text": "Each gram of enzyme somehow turns into more enzyme as "
                     "the meal is digested.", "correct": False,
             "why": "No new enzyme is created during digestion — the same "
                    "molecules are simply reused many times over."},
            {"text": "Because each molecule keeps working over and over, a "
                     "small number of them can process a large amount of "
                     "substrate.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s19",
        "band": "standard",
        "text": "An enzyme sample is kept at 25 °C, below its 37 °C "
                "optimum but nowhere near the temperature that denatures "
                "it. Predict its condition.",
        "options": [
            {"text": "Working, but more slowly than at its optimum.",
             "correct": True},
            {"text": "Permanently ruined, in exactly the same way heat "
                     "above 50 °C ruins it.", "correct": False,
             "why": "25 °C causes no permanent damage — only heat above "
                    "about 50 °C does that."},
            {"text": "Working exactly as fast as it does at 37 °C.",
             "correct": False,
             "why": "25 °C is below the optimum, so the rate is genuinely "
                    "lower there, not identical to the rate at 37 °C."},
            {"text": "Completely inactive, doing nothing at all.",
             "correct": False,
             "why": "A temperature below the optimum slows an enzyme down — "
                    "it does not stop it working altogether."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s20",
        "band": "standard",
        "text": "Carbohydrase works best at pH 7 in the mouth, protease at "
                "pH 2 in the stomach and pH 8 in the small intestine, and "
                "lipase at pH 8 in the small intestine. What generalisation "
                "do these examples support?",
        "options": [
            {"text": "Enzymes made in the stomach always work fastest in "
                     "the small intestine instead.", "correct": False,
             "why": "The stomach's own protease works best at the "
                    "stomach's own pH 2 — the small intestine is where a "
                    "second, different-optimum protease works."},
            {"text": "An enzyme's optimum pH tends to match the pH of the "
                     "organ where it is meant to work.", "correct": True},
            {"text": "Every digestive enzyme has exactly the same optimum "
                     "pH.", "correct": False,
             "why": "The three named enzymes clearly have different optima "
                    "— pH 7, pH 2 and 8, and pH 8."},
            {"text": "pH makes no real difference to how well any of these "
                     "three enzymes work.", "correct": False,
             "why": "Each enzyme's rate depends heavily on being close to "
                    "its own particular optimum pH."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s21",
        "band": "standard",
        "text": "Almost all the substrate in a working tube has already "
                "reacted, with barely a trace left, while a generous "
                "supply of enzyme is still sitting there unused. What "
                "happens if even more enzyme is tipped in at this point?",
        "options": [
            {"text": "The reaction produces more total product than the "
                     "substrate could ever supply.", "correct": False,
             "why": "The total product possible is capped by how much "
                    "substrate is present — extra enzyme cannot exceed "
                    "that."},
            {"text": "The extra enzyme starts converting itself into "
                     "product instead.", "correct": False,
             "why": "An enzyme is never converted into its own product — "
                    "only the substrate is."},
            {"text": "Little change — the small amount of substrate is "
                     "now what limits the rate.", "correct": True},
            {"text": "The rate rises sharply, since more enzyme always "
                     "means a faster reaction.", "correct": False,
             "why": "With so little substrate available, extra enzyme "
                    "molecules have nothing more to work on — substrate, "
                    "not enzyme, is limiting here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s22",
        "band": "standard",
        "text": "Two students disagree about why an enzyme has stopped "
                "working: one says “it has been used up,” the other says "
                "“it has been denatured.” How do these two explanations "
                "differ?",
        "options": [
            {"text": "They are two names for exactly the same underlying "
                     "process.", "correct": False,
             "why": "They describe genuinely different situations — one "
                    "claims the enzyme has disappeared, the other that it "
                    "is present but damaged."},
            {"text": "Being used up is permanent, while being denatured "
                     "can be reversed by cooling.", "correct": False,
             "why": "It is the other way round for permanence — denaturing "
                    "is permanent, and being used up is not what happens to "
                    "a catalyst at all."},
            {"text": "Being denatured only applies to carbohydrase, and "
                     "being used up only applies to protease and lipase.",
             "correct": False,
             "why": "Neither explanation is tied to one specific named "
                    "enzyme — both are general claims about how enzymes "
                    "behave."},
            {"text": "Being used up would mean the enzyme is gone; being "
                     "denatured means it is still there but ruined.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s23",
        "band": "standard",
        "text": "A tube digests 2 g of starch in ten minutes using 0.1 g of "
                "amylase. The amylase is left in place and a further 2 g "
                "of starch is added, with conditions unchanged. Predict "
                "how long the second 2 g takes.",
        "options": [
            {"text": "About ten minutes again, since the amylase was not "
                     "used up by the first batch.", "correct": True},
            {"text": "Twice as long, since half the amylase was consumed "
                     "digesting the first batch.", "correct": False,
             "why": "No amylase is consumed by the reaction. A catalyst "
                    "finishes each cycle unchanged, so the whole 0.1 g is "
                    "still there for the second batch."},
            {"text": "It will not be digested, since the amylase has "
                     "already done its one job.", "correct": False,
             "why": "An enzyme is not spent after a single use. The same "
                    "molecules are free to bind and cut the new starch "
                    "straight away."},
            {"text": "Half as long, since the tube is warmer after the "
                     "first reaction.", "correct": False,
             "why": "Conditions are stated as unchanged. What the first "
                    "reaction leaves behind is the same amount of intact "
                    "amylase, not a warmer tube."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s24",
        "band": "standard",
        "text": "Explain why the pancreas has to keep supplying fresh "
                "amylase into the small intestine with every meal, rather "
                "than the body somehow recycling amylase used earlier that "
                "day.",
        "options": [
            {"text": "The pancreas actually reuses the same amylase all "
                     "day, just moving it back and forth.", "correct": False,
             "why": "The amylase from an earlier meal is ruined by stomach "
                    "acid, so the pancreas genuinely supplies fresh enzyme "
                    "each time."},
            {"text": "Amylase swallowed with an earlier meal was denatured "
                     "by stomach acid and cannot be recovered.", "correct": True},
            {"text": "Amylase is used up completely by the time it reaches "
                     "the stomach, so none is left to recycle.", "correct": False,
             "why": "It is not used up — a catalyst is never consumed by "
                    "its own reaction. What stops it is the acid changing "
                    "its shape."},
            {"text": "The body has no way of transporting amylase back "
                     "from the stomach to the pancreas.", "correct": False,
             "why": "Transport back is not the barrier described — even if "
                    "it were returned, the amylase would already be "
                    "permanently denatured."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s25",
        "band": "standard",
        "text": "A tube holds only lipase and lipid, at pH 7 rather than "
                "lipase's optimum of pH 8. Predict the rate compared with "
                "running the same tube at pH 8.",
        "options": [
            {"text": "Completely zero, since pH 7 is not lipase's optimum.",
             "correct": False,
             "why": "Being off the optimum slows a reaction rather than "
                    "stopping it outright, unless the pH is far more "
                    "extreme."},
            {"text": "Faster than at pH 8, since pH 7 is closer to "
                     "neutral.", "correct": False,
             "why": "Closer to neutral is not the same as closer to "
                    "lipase's own optimum, which is pH 8, not pH 7."},
            {"text": "Slower than at pH 8, though not necessarily zero.",
             "correct": True},
            {"text": "Exactly the same as at pH 8, since pH 7 and pH 8 are "
                     "close together.", "correct": False,
             "why": "Being away from the optimum, even slightly, lowers "
                    "the rate below what it would be exactly at pH 8."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s26",
        "band": "standard",
        "text": "Protease's two optima are pH 2 and pH 8. Predict its rate "
                "at pH 5, roughly halfway between them.",
        "options": [
            {"text": "Exactly halfway between the two optimum rates, as a "
                     "simple average.", "correct": False,
             "why": "Nothing establishes a simple averaging rule here — "
                    "the point is that being far from both optima lowers "
                    "the rate."},
            {"text": "As high as at either optimum, since pH 5 sits "
                     "between two working values.", "correct": False,
             "why": "Sitting between two optima does not itself guarantee "
                    "a high rate — pH 5 is genuinely distant from both."},
            {"text": "Zero, since pH 5 is not one of protease's two named "
                     "optima.", "correct": False,
             "why": "Being away from the optimum lowers the rate rather "
                    "than reducing it straight to zero."},
            {"text": "Lower than at either optimum, since pH 5 is far from "
                     "both.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s27",
        "band": "standard",
        "text": "Carbohydrase and lipase are both tested at pH 7. Explain "
                "why carbohydrase runs fast there while lipase runs more "
                "slowly.",
        "options": [
            {"text": "pH 7 is carbohydrase's own optimum, but it is not "
                     "lipase's, whose optimum is pH 8.", "correct": True},
            {"text": "Carbohydrase is simply a stronger enzyme than "
                     "lipase overall.", "correct": False,
             "why": "Strength in general is not the issue — the difference "
                    "comes specifically from how close pH 7 is to each "
                    "enzyme's own optimum."},
            {"text": "Lipase only works inside the small intestine, "
                     "wherever the test tube itself happens to be placed.",
             "correct": False,
             "why": "Location is not what the bench tests — what matters "
                    "is the pH set in the tube, and pH 7 is simply not "
                    "lipase's optimum."},
            {"text": "Carbohydrase is not affected by pH at all, unlike "
                     "lipase.", "correct": False,
             "why": "Carbohydrase is affected by pH just as much as any "
                    "enzyme — pH 7 happens to be exactly where it works "
                    "best."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s28",
        "band": "standard",
        "text": "A person's pancreas produces only half its usual amount of "
                "lipase, though everything else works normally. Predict "
                "the effect on fat digestion.",
        "options": [
            {"text": "Starch and protein digestion also fail, since all "
                     "three enzymes come from the same organ.", "correct": False,
             "why": "The case describes only lipase falling, not the "
                    "pancreas's other secretions — those are not affected "
                    "here."},
            {"text": "Fat digestion becomes slower and less complete, "
                     "rather than stopping altogether.", "correct": True},
            {"text": "Fat digestion stops entirely, since lipase is now "
                     "missing.", "correct": False,
             "why": "Lipase is reduced, not absent — some fat digestion "
                    "can still happen, just more slowly."},
            {"text": "Fat digestion is unaffected, since bile can take over "
                     "lipase's job.", "correct": False,
             "why": "Bile is not an enzyme and cannot substitute for "
                    "lipase's chemical role — it only emulsifies fat "
                    "droplets."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s29",
        "band": "standard",
        "text": "A tube contains amylase and a sample of pure protein, with "
                "no starch present at all. Predict the outcome.",
        "options": [
            {"text": "The amylase changes shape to start working on the "
                     "protein instead.", "correct": False,
             "why": "An enzyme's shape is fixed — it does not reshape "
                    "itself to fit a substrate it was not built for."},
            {"text": "The protein is converted into starch, which the "
                     "amylase then digests.", "correct": False,
             "why": "Protein cannot be converted into starch, and amylase "
                    "has no role in any such conversion."},
            {"text": "Nothing happens — amylase's shape does not fit "
                     "protein.", "correct": True},
            {"text": "The protein is slowly broken down, just more slowly "
                     "than protease would manage.", "correct": False,
             "why": "Amylase has no effect on protein at all, however "
                    "slowly — its shape simply does not fit that "
                    "substrate."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-s30",
        "band": "standard",
        "text": "An enzyme is held at its optimum temperature and pH the "
                "whole time, but no more substrate is added once the first "
                "batch is used up. Predict what happens next.",
        "options": [
            {"text": "The enzyme starts breaking down its own structure "
                     "instead.", "correct": False,
             "why": "An enzyme's shape fits its one substrate, not itself — "
                    "with none of that substrate left, it simply has "
                    "nothing to act on."},
            {"text": "The reaction keeps running anyway, since conditions "
                     "are otherwise perfect for it to continue.",
             "correct": False,
             "why": "Perfect conditions cannot make a reaction continue "
                    "once the substrate itself has run out."},
            {"text": "The enzyme becomes denatured from having nothing to "
                     "do.", "correct": False,
             "why": "Denaturing is caused by heat, not by a lack of "
                    "substrate — an idle enzyme at its optimum stays "
                    "perfectly intact."},
            {"text": "The reaction simply stops — there is nothing left "
                     "for the enzyme to act on.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-06-h07",
        "band": "harder",
        "text": "A student claims: “Raising the temperature always makes an "
                "enzyme reaction go faster.” Evaluate this using both the "
                "below-optimum and above-denaturing regions.",
        "options": [
            {"text": "It is false — raising temperature helps up to the "
                     "optimum, but past the denaturing point it ruins the "
                     "enzyme instead.", "correct": True},
            {"text": "It is true, since heat always adds energy to a "
                     "reaction regardless of the temperature it starts "
                     "from or how high it eventually reaches.",
             "correct": False,
             "why": "Above about 50 °C, added heat destroys the enzyme's "
                    "shape rather than speeding the reaction further."},
            {"text": "It is false, but only because temperature has no "
                     "effect on enzymes at all below the optimum.",
             "correct": False,
             "why": "Temperature genuinely does raise the rate below the "
                    "optimum — the claim only breaks down once denaturing "
                    "begins."},
            {"text": "It is true only for lipase, and false for the other "
                     "two named enzymes.", "correct": False,
             "why": "The same rise-then-collapse pattern with temperature "
                    "applies to all enzymes, not only to one of the three."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h08",
        "band": "harder",
        "text": "A student argues: “Since more substrate always makes a "
                "reaction faster, doubling the starch in a tube will double "
                "the rate of glucose production.” Evaluate this, given a "
                "fixed amount of amylase.",
        "options": [
            {"text": "It is true only if the substrate is starch rather "
                     "than protein or lipid.", "correct": False,
             "why": "The limiting-factor reasoning applies regardless of "
                    "which substrate is involved — it is not specific to "
                    "starch."},
            {"text": "It depends on whether the enzyme was already the "
                     "limiting factor — if so, doubling substrate would not "
                     "double the rate.", "correct": True},
            {"text": "It is definitely true — substrate amount is the only "
                     "thing that ever affects rate.", "correct": False,
             "why": "With enzyme amount fixed, there is a limit to how many "
                    "reactions can happen at once, whatever the substrate "
                    "level."},
            {"text": "It is definitely false — substrate amount never "
                     "affects the rate of an enzyme reaction.", "correct": False,
             "why": "Substrate amount does matter when it is the scarce "
                    "one — the claim only breaks down once enzyme becomes "
                    "the limiting factor instead."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h09",
        "band": "harder",
        "text": "Sample A of amylase is heated briefly to 55 °C and then "
                "cooled back to 37 °C. Sample B is kept at 37 °C the whole "
                "time. Compare their activity now, and their potential for "
                "the future.",
        "options": [
            {"text": "Sample A will slowly recover its activity over the "
                     "next few hours at 37 °C.", "correct": False,
             "why": "There is no gradual recovery from denaturing — Sample "
                    "A's damage at 55 °C is permanent, whatever happens "
                    "afterwards."},
            {"text": "Sample B is now damaged too, since it was exposed to "
                     "the same room as Sample A during the brief heating.",
             "correct": False,
             "why": "Only the sample that was actually heated to 55 °C is "
                    "affected — being nearby does not transfer any damage."},
            {"text": "Sample A is permanently ruined and will never "
                     "recover; Sample B is fully active and stays that "
                     "way.", "correct": True},
            {"text": "Both samples are equally active now, since both are "
                     "currently at 37 °C.", "correct": False,
             "why": "Current temperature is not what decides this — "
                    "Sample A's shape was already destroyed during the "
                    "brief spike to 55 °C."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h10",
        "band": "harder",
        "text": "A student argues: “Stomach acid denatures every enzyme it "
                "touches, since it denatured the mouth's amylase.” "
                "Evaluate this using the stomach's own protease.",
        "options": [
            {"text": "It is true, and the stomach's protease must actually "
                     "be denatured too, even though digestion still "
                     "happens.", "correct": False,
             "why": "The stomach's protease genuinely does work there — "
                    "digestion happening is direct evidence it is not "
                    "denatured by the acid."},
            {"text": "It is true only because protease is made in the "
                     "pancreas rather than the stomach.", "correct": False,
             "why": "Protease that works at pH 2 is made in the stomach "
                    "itself — it is a genuinely acid-tolerant molecule, not "
                    "an import from elsewhere."},
            {"text": "It cannot be evaluated, since amylase and protease "
                     "are actually the same enzyme.", "correct": False,
             "why": "They are two entirely different enzymes with "
                    "different substrates and different shapes, which is "
                    "exactly why acid affects them differently."},
            {"text": "It is false — the stomach's protease is specifically "
                     "built to work in that same acid without being "
                     "denatured.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h11",
        "band": "harder",
        "text": "An industrial process needs an enzyme to keep working at "
                "70 °C. Explain why a typical human digestive enzyme could "
                "not be used, and what property a substitute would need.",
        "options": [
            {"text": "A typical enzyme denatures above about 50 °C, so a "
                     "substitute would need a shape that stays folded at "
                     "far higher temperatures.", "correct": True},
            {"text": "A typical enzyme would simply work faster at 70 °C, "
                     "so no substitute is actually needed.", "correct": False,
             "why": "70 °C is well past the point where a typical digestive "
                    "enzyme's shape is permanently destroyed, not a "
                    "temperature it thrives at."},
            {"text": "No enzyme of any kind, anywhere in nature, could "
                     "ever function above 50 °C, so the process being asked "
                     "for is flatly impossible to build.", "correct": False,
             "why": "The claim here is only that a TYPICAL human digestive "
                    "enzyme denatures there — it does not establish that no "
                    "enzyme anywhere could tolerate higher heat."},
            {"text": "The substitute enzyme would need to be a different "
                     "colour to withstand the heat.", "correct": False,
             "why": "Colour has nothing to do with heat tolerance — what "
                    "would matter is the stability of the molecule's own "
                    "folded shape."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h12",
        "band": "harder",
        "text": "A student argues: “Mixing carbohydrase and protease into "
                "one tube with only starch present should digest twice as "
                "much as carbohydrase alone.” Evaluate this.",
        "options": [
            {"text": "It is false, but only because carbohydrase alone "
                     "already digests all the starch completely and "
                     "instantly.", "correct": False,
             "why": "Carbohydrase does not act instantly — the real reason "
                    "the claim fails is that protease simply has no "
                    "substrate to work on here."},
            {"text": "It is false — protease has nothing to act on when "
                     "only starch is present, so it contributes nothing.",
             "correct": True},
            {"text": "It is true, since having two enzymes present always "
                     "means twice the digestion.", "correct": False,
             "why": "Protease's shape does not fit starch at all — adding "
                    "it changes nothing when starch is the only substrate "
                    "present."},
            {"text": "It is true, but only because protease can slowly "
                     "adapt to fit starch over time.", "correct": False,
             "why": "An enzyme's shape does not adapt to a new substrate — "
                    "protease remains entirely inactive on starch, however "
                    "long it is given."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h13",
        "band": "harder",
        "text": "Tube A has limited enzyme and plenty of substrate. Tube B "
                "has plenty of enzyme and limited substrate. Predict which "
                "tube's rate rises more if its enzyme amount is doubled.",
        "options": [
            {"text": "Both rise by exactly the same amount, since both "
                     "gained the same extra enzyme.", "correct": False,
             "why": "The two tubes are limited by different things — only "
                    "the one where enzyme is the bottleneck benefits much "
                    "from more of it."},
            {"text": "Neither rises at all, since substrate amount is all "
                     "that ever controls rate.", "correct": False,
             "why": "Tube A's rate does rise here, precisely because "
                    "enzyme, not substrate, was holding it back."},
            {"text": "Tube A's rate rises more, since enzyme is what is "
                     "actually limiting it there.", "correct": True},
            {"text": "Tube B's rate rises more, since it already has more "
                     "enzyme to begin with.", "correct": False,
             "why": "Tube B's rate is already capped by its limited "
                    "substrate — adding more enzyme there changes little."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h14",
        "band": "harder",
        "text": "A student claims: “An enzyme's optimum pH always tells you "
                "exactly where in the body it is found.” Evaluate this "
                "using protease as a test case.",
        "options": [
            {"text": "It is completely true, and protease is no "
                     "exception, since it only has one true home.",
             "correct": False,
             "why": "Protease genuinely works in two different places, the "
                    "stomach and the small intestine, each with its own "
                    "optimum pH."},
            {"text": "It is false for every enzyme, since none of them "
                     "have any link at all between optimum pH and "
                     "location, whatever organ they are made in or "
                     "released from.", "correct": False,
             "why": "Carbohydrase and lipase each do have one optimum "
                    "linked to one organ — protease is the exception with "
                    "two, not the rule that none exists."},
            {"text": "It cannot be evaluated, since protease's optimum pH "
                     "has never actually been measured.", "correct": False,
             "why": "Protease's two optima, pH 2 and pH 8, are exactly the "
                    "measured values that let this claim be tested."},
            {"text": "It is an oversimplification — protease has two "
                     "optima, so a single optimum pH does not always point "
                     "to a single place.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h15",
        "band": "harder",
        "text": "Protease is described as having two optimum pH values, 2 "
                "and 8. A student reads this as meaning one single "
                "protease molecule works equally well in the stomach and "
                "in the small intestine. Evaluate that reading.",
        "options": [
            {"text": "It is the wrong reading — the two optima belong to "
                     "two different proteases, one made by the stomach and "
                     "one by the pancreas.", "correct": True},
            {"text": "It is the right reading, since the stomach's "
                     "protease is carried onward with the meal and goes on "
                     "working in the small intestine too.", "correct": False,
             "why": "The stomach's protease is built for strong acid. The "
                    "alkaline conditions further along are the working "
                    "conditions of a separate protease, supplied by the "
                    "pancreas."},
            {"text": "It is the right reading, since an optimum pH is a "
                     "property of the substrate rather than of the "
                     "enzyme.", "correct": False,
             "why": "An optimum belongs to the enzyme's own shape, not to "
                    "the substrate. Protein is digested by two proteases, "
                    "each with its own optimum."},
            {"text": "It is the wrong reading, but only because no enzyme "
                     "ever has more than one optimum pH.", "correct": False,
             "why": "The pair of optima is real. What the reading gets "
                    "wrong is attributing both of them to one and the "
                    "same molecule."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h16",
        "band": "harder",
        "text": "A student argues: “Since amylase works in the mouth and "
                "again in the small intestine, it must be the same "
                "molecules travelling all the way through.” Evaluate this.",
        "options": [
            {"text": "It cannot be evaluated, since amylase is never "
                     "actually swallowed along with food.", "correct": False,
             "why": "Amylase from saliva genuinely is swallowed with the "
                    "food and does travel into the stomach, where it meets "
                    "the acid."},
            {"text": "It is false — the mouth's amylase is denatured by "
                     "stomach acid, so the small intestine's supply is "
                     "fresh amylase from the pancreas.", "correct": True},
            {"text": "It is true, since a catalyst is never used up and so "
                     "can always keep travelling onward unchanged.",
             "correct": False,
             "why": "Not being used up is different from surviving the "
                    "stomach's acid — the mouth's amylase is denatured "
                    "there, not merely passed through unchanged."},
            {"text": "It is true, because the stomach's acid only affects "
                     "protease, not amylase.", "correct": False,
             "why": "The acid does affect amylase — it is exactly why "
                    "starch digestion pauses in the stomach and only "
                    "resumes once fresh amylase arrives later."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h17",
        "band": "harder",
        "text": "A reaction running well at 37 °C has its temperature "
                "slowly raised to 45 °C — past the optimum, but still below "
                "the point that denatures the enzyme. Predict and explain "
                "the change in rate.",
        "options": [
            {"text": "The rate stays exactly the same as at 37 °C, since "
                     "45 °C is still a safe temperature.", "correct": False,
             "why": "Being safe from permanent damage is not the same as "
                    "being at the optimum — the rate does fall once past "
                    "37 °C."},
            {"text": "The enzyme is already permanently denatured at "
                     "45 °C.", "correct": False,
             "why": "45 °C is below the roughly 50 °C threshold for "
                    "permanent damage — the enzyme is slowed, not yet "
                    "ruined."},
            {"text": "The rate falls from its peak, since the molecule is "
                     "moving away from its optimum, though it is not yet "
                     "permanently damaged.", "correct": True},
            {"text": "The rate keeps rising, since any temperature below "
                     "the denaturing point must still be speeding the "
                     "enzyme up.", "correct": False,
             "why": "The rate peaks at the optimum and falls beyond it, "
                    "even before the temperature reaches the point of "
                    "permanent damage."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h18",
        "band": "harder",
        "text": "Compare cooling an enzyme sample to 0 °C with heating "
                "another sample to 60 °C. Which, if either, permanently "
                "ends the reaction, and which allows recovery?",
        "options": [
            {"text": "Both permanently end the reaction, with no recovery "
                     "possible from either.", "correct": False,
             "why": "Cold causes no lasting damage at all — warming a "
                    "chilled sample back up restores it completely."},
            {"text": "Both allow full recovery, since neither temperature "
                     "is extreme enough to matter.", "correct": False,
             "why": "60 °C is well past the point of permanent damage — "
                    "that sample will not recover, unlike the cooled one."},
            {"text": "Cooling permanently ends it, while heating to 60 °C "
                     "allows recovery once cooled back down.",
             "correct": False,
             "why": "This is the reverse of what happens — cold is safe "
                    "and reversible, while 60 °C causes the permanent "
                    "damage."},
            {"text": "Cooling allows full recovery on warming; heating to "
                     "60 °C permanently ends it.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h19",
        "band": "harder",
        "text": "A tube contains carbohydrase, protease and lipase together "
                "with starch, protein and lipid, all at pH 7 and 37 °C. "
                "Predict which reaction runs fastest, which runs slower, "
                "and which runs slowest.",
        "options": [
            {"text": "Starch fastest, since pH 7 is carbohydrase's own "
                     "optimum; protein and lipid slower, since pH 7 is "
                     "away from protease's and lipase's optima.",
             "correct": True},
            {"text": "All three run at exactly the same rate, since the "
                     "temperature is identical for each.", "correct": False,
             "why": "Temperature being equal does not make the rates "
                    "equal — pH 7 suits carbohydrase far better than it "
                    "suits protease or lipase."},
            {"text": "None of the three reactions run at all, since a "
                     "mixture of three different enzymes always jams and "
                     "interferes with every one of its own members.", "correct": False,
             "why": "Each enzyme still fits its own substrate regardless of "
                    "what else is in the tube — mixing them does not stop "
                    "any of the three reactions."},
            {"text": "Protein fastest, since protease has two optima and "
                     "so is generally the strongest of the three enzymes.",
             "correct": False,
             "why": "Having two optima does not make protease faster at a "
                    "pH that is neither of them — pH 7 is far from both "
                    "pH 2 and pH 8."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h20",
        "band": "harder",
        "text": "A student says: “Boiling always destroys any protein-based "
                "molecule inside it, so boiling destroys every enzyme.” The "
                "conclusion about enzymes is broadly right — evaluate "
                "whether the reasoning given is precise.",
        "options": [
            {"text": "No, because boiling only affects carbohydrate-based "
                     "molecules, not proteins.", "correct": False,
             "why": "Enzymes are proteins, and heat above about 50 °C does "
                    "affect protein-based molecules — that part of the "
                    "reasoning is not the issue."},
            {"text": "Not quite — boiling changes the enzyme's shape "
                     "rather than destroying the molecule itself, which is "
                     "a more precise description of denaturing.",
             "correct": True},
            {"text": "Yes, the reasoning is exactly right in every "
                     "respect.", "correct": False,
             "why": "Denaturing changes shape rather than annihilating the "
                    "molecule — “destroys” overstates what actually "
                    "happens."},
            {"text": "No, and the conclusion is also wrong — boiling does "
                     "not actually affect enzymes at all.", "correct": False,
             "why": "The conclusion that boiling ruins enzymes is broadly "
                    "correct — the issue is only with how the reasoning is "
                    "phrased."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h21",
        "band": "harder",
        "text": "A student wants to store a batch of enzyme for future use "
                "and considers three options: keeping it in a fridge, "
                "leaving it at room temperature, or briefly boiling it for "
                "“sterility.” Rank these for preserving enzyme activity.",
        "options": [
            {"text": "All three options preserve activity equally well.",
             "correct": False,
             "why": "Boiling causes permanent damage that the other two "
                    "options do not — the three are not equivalent."},
            {"text": "Room temperature is best, since the fridge would "
                     "denature the enzyme through cold.", "correct": False,
             "why": "Cold does not denature an enzyme — only heat above "
                    "about 50 °C does. The fridge is a safe, reversible "
                    "slowdown."},
            {"text": "Fridge best, room temperature next, boiling worst — "
                     "boiling permanently ruins it.", "correct": True},
            {"text": "Boiling is best, since sterilising it protects the "
                     "enzyme from contamination.", "correct": False,
             "why": "Boiling denatures the enzyme itself — protecting it "
                    "from contamination does no good if the enzyme's own "
                    "shape is destroyed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h22",
        "band": "harder",
        "text": "A student argues: “An enzyme that works at pH 7 must work "
                "badly at every other pH.” Evaluate this using protease.",
        "options": [
            {"text": "It is definitely true for every enzyme, protease "
                     "included, with no exceptions at all.", "correct": False,
             "why": "Protease is a direct counterexample: it works well at "
                    "two quite different pH values, pH 2 and pH 8."},
            {"text": "It is true only for enzymes made in the pancreas.",
             "correct": False,
             "why": "Where an enzyme is made does not decide how many "
                    "optima it has — protease's two optima come from the "
                    "two organs it works in, stomach and pancreas."},
            {"text": "It cannot be evaluated, since no enzyme has ever "
                     "been tested at more than one pH.", "correct": False,
             "why": "Protease's behaviour at both pH 2 and pH 8 is exactly "
                    "the kind of comparison that tests this claim."},
            {"text": "It is not a safe generalisation — protease shows an "
                     "enzyme can have a wide working range or even two "
                     "separate optima.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h23",
        "band": "harder",
        "text": "Protease is tested at pH 2 and at pH 8, both at 37 °C, and "
                "works well at both. A student concludes: “pH does not "
                "matter for protease, since it worked at both settings "
                "tried.” Evaluate this conclusion.",
        "options": [
            {"text": "It overgeneralises — protease works at those two "
                     "specific optima, not at every pH, as a test at pH 5 "
                     "would show.", "correct": True},
            {"text": "The conclusion is correct — working at two different "
                     "pH values proves pH has no effect at all.",
             "correct": False,
             "why": "Working at exactly its two named optima is not the "
                    "same as working everywhere — a pH far from both, such "
                    "as pH 5, would show a real drop."},
            {"text": "The conclusion is correct, but only because protease "
                     "is a uniquely pH-independent enzyme.", "correct": False,
             "why": "Protease is not pH-independent — it has two SPECIFIC "
                    "optima, which is a different and more precise claim "
                    "than “pH does not matter.”"},
            {"text": "The conclusion cannot be evaluated without testing "
                     "carbohydrase and lipase at the same two pH values as "
                     "well, since only one of the three has actually been "
                     "checked.", "correct": False,
             "why": "The other two enzymes are not needed to see the flaw "
                    "— protease's own behaviour at a pH away from both "
                    "optima, such as pH 5, is what tests the claim."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h24",
        "band": "harder",
        "text": "Using the three named enzymes' optima — carbohydrase pH 7, "
                "protease pH 2 and pH 8, lipase pH 8 — evaluate the claim "
                "“digestive enzymes generally prefer acidic conditions.”",
        "options": [
            {"text": "It cannot be evaluated without also knowing the "
                     "optimum pH of bile.", "correct": False,
             "why": "Bile is not an enzyme and has no optimum pH of its "
                    "own — the three named enzymes' own optima are enough "
                    "to test this claim."},
            {"text": "It is not well supported — only one of protease's "
                     "two optima is acidic, and the other two enzymes "
                     "prefer neutral or alkaline conditions.", "correct": True},
            {"text": "It is well supported, since all three enzymes work "
                     "best in acid.", "correct": False,
             "why": "Only one of protease's two optima, pH 2, is acidic — "
                    "carbohydrase and lipase both prefer neutral or "
                    "alkaline conditions instead."},
            {"text": "It is well supported, because the stomach is the "
                     "most important digestive organ.", "correct": False,
             "why": "The claim is about pH preference across the enzymes, "
                    "not about which organ matters most, and most of the "
                    "listed optima are not acidic."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h25",
        "band": "harder",
        "text": "Suppose a patient's stomach protease worked perfectly at "
                "pH 2 but, for some reason, failed completely at pH 8. "
                "Predict the specific consequence for their protein "
                "digestion.",
        "options": [
            {"text": "Carbohydrase would automatically take over protein "
                     "digestion in the small intestine instead, since it "
                     "is already present there.", "correct": False,
             "why": "Carbohydrase's shape fits starch only — it has no "
                    "ability to substitute for protease on protein."},
            {"text": "The patient's stomach acid would simply become "
                     "alkaline to compensate.", "correct": False,
             "why": "Nothing in the case suggests the stomach's own acid "
                    "changes — the fault described is specific to the "
                    "pH 8 form of protease."},
            {"text": "Protein digestion would begin normally in the "
                     "stomach but stall once material reached the alkaline "
                     "small intestine.", "correct": True},
            {"text": "Protein digestion would fail everywhere, since "
                     "protease is protease wherever it is found.",
             "correct": False,
             "why": "The stomach stage, at pH 2, would still work fine — "
                    "only the pH 8 stage in the small intestine is affected "
                    "by this hypothetical fault."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h26",
        "band": "harder",
        "text": "A student argues: “Since lipase's optimum is pH 8, and the "
                "small intestine is pH 8, lipase must be working at its "
                "absolute fastest the instant bile has emulsified the "
                "fat.” Evaluate this.",
        "options": [
            {"text": "It is entirely correct, since pH is the only thing "
                     "that ever affects an enzyme's rate.", "correct": False,
             "why": "Temperature matters just as much as pH — being at the "
                    "right pH alone does not guarantee the fastest possible "
                    "rate."},
            {"text": "It is wrong, because lipase's optimum pH is actually "
                     "pH 7, not pH 8.", "correct": False,
             "why": "Lipase's optimum genuinely is pH 8 — the flaw in the "
                    "claim is about assuming pH alone decides the rate, not "
                    "about the pH value itself."},
            {"text": "It cannot be evaluated, since bile's own pH is "
                     "unknown.", "correct": False,
             "why": "Bile's own pH is not what the claim depends on — the "
                    "issue is treating pH as the only factor deciding "
                    "lipase's rate."},
            {"text": "It overreaches — correct pH is necessary but not "
                     "enough on its own; temperature also has to be right "
                     "for the fastest possible rate.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h27",
        "band": "harder",
        "text": "A protease sample sits at pH 5, well away from either of "
                "its optima, and is running slowly. It is then warmed "
                "towards 37 °C, its optimum temperature. Predict whether "
                "this warming fixes the slow rate.",
        "options": [
            {"text": "No — pH and temperature are independent; only "
                     "changing the pH would fix a problem caused by the "
                     "pH.", "correct": True},
            {"text": "Yes — reaching the optimum temperature always "
                     "restores an enzyme to its fastest possible rate.",
             "correct": False,
             "why": "Temperature and pH act as two separate factors — "
                    "being at the right temperature does not correct a "
                    "problem coming from the wrong pH."},
            {"text": "Yes, because temperature always matters more than "
                     "pH for any enzyme's rate.", "correct": False,
             "why": "Neither factor is described as more important than "
                    "the other — both need to be favourable for the "
                    "fastest rate."},
            {"text": "It cannot be predicted, since pH and temperature "
                     "always change together in a real enzyme.",
             "correct": False,
             "why": "The two are genuinely separate variables that can be "
                    "set independently, as the bench itself does with "
                    "separate dials."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h28",
        "band": "harder",
        "text": "An enzyme sample shows 0% activity in a test. A student "
                "concludes: “It must be denatured.” Evaluate this "
                "conclusion.",
        "options": [
            {"text": "It cannot be evaluated without knowing which of the "
                     "three named enzymes is being tested.", "correct": False,
             "why": "The reasoning flaw applies to any enzyme — zero "
                    "activity has more than one possible cause regardless "
                    "of which one is being tested."},
            {"text": "It is not the only explanation — the sample could "
                     "simply be at the wrong pH or temperature without "
                     "being permanently damaged at all.", "correct": True},
            {"text": "It is the only possible explanation for zero "
                     "activity.", "correct": False,
             "why": "Being at the wrong pH or a cold temperature also gives "
                    "zero or near-zero activity, without any permanent "
                    "damage having occurred."},
            {"text": "It is wrong, since a denatured enzyme would still "
                     "show some activity, just reduced.", "correct": False,
             "why": "A genuinely denatured enzyme can show zero activity — "
                    "the flaw is assuming zero activity always MEANS "
                    "denaturing, not that denaturing is impossible here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h29",
        "band": "harder",
        "text": "Compare three cases: (a) a brief cold snap, (b) a "
                "temporary pH shock away from the optimum but not extreme, "
                "and (c) genuine heat-denaturing above 50 °C. Which "
                "recover once normal conditions return, and which does "
                "not?",
        "options": [
            {"text": "None of the three recover, since any disturbance to "
                     "an enzyme's conditions causes lasting damage.",
             "correct": False,
             "why": "Cold and a moderate pH shock cause no lasting damage "
                    "at all — only heat above about 50 °C is described as "
                    "permanent."},
            {"text": "Only (c) recovers, since heat-denaturing is "
                     "described as temporary in nature.", "correct": False,
             "why": "Heat-denaturing is exactly the case described as "
                    "permanent — it is the cold and pH cases that recover, "
                    "not this one."},
            {"text": "Both (a) and (b) recover fully once conditions "
                     "return to normal; (c) never recovers.", "correct": True},
            {"text": "All three recover fully once normal conditions "
                     "return, including the heat-denatured case.",
             "correct": False,
             "why": "Heat-denaturing above 50 °C is specifically described "
                    "as permanent — returning to normal conditions "
                    "afterwards does not undo it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-06-h30",
        "band": "harder",
        "text": "A student suggests: “Enzymes being ‘used up’ would explain "
                "why a stomach eventually runs out of digestive power on a "
                "huge meal — that idea deserves serious consideration.” "
                "Evaluate this suggestion.",
        "options": [
            {"text": "It deserves serious consideration, since a huge "
                     "meal genuinely could use up all the available "
                     "enzyme.", "correct": False,
             "why": "An enzyme is never consumed by its own reaction — a "
                    "huge meal simply takes longer to process, rather than "
                    "exhausting a fixed supply."},
            {"text": "It is correct, and explains why the pancreas has to "
                     "keep making completely new types of enzyme for "
                     "larger meals.", "correct": False,
             "why": "The same three named enzymes handle a meal of any "
                    "size — no new type is required, since none of them "
                    "are consumed by use."},
            {"text": "It cannot be evaluated without knowing exactly how "
                     "large the meal is.", "correct": False,
             "why": "Meal size does not change the underlying principle — "
                    "a catalyst is not used up regardless of how much "
                    "substrate it is given."},
            {"text": "It does not hold up — a catalyst is not consumed by "
                     "the reaction, so a huge meal is handled by reuse "
                     "taking proportionally longer, not by enzyme running "
                     "out.", "correct": True},
        ],
        "figure": None,
    },
]
