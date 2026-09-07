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
]
