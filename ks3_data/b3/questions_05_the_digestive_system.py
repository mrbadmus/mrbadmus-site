"""B3 lesson 05 — The digestive system: twelve questions (MRB-269).

The lesson's whole argument is that smaller pieces is not smaller molecules,
and that the organ everybody names holds the meal for four hours while the one
that does the work holds it for sixteen. These twelve probe exactly that: the
seven stops and what each one does and does not do (peristalsis without
gravity, the three secreting organs no food passes through, the large
intestine taking back water rather than food, egestion as removal of what was
never absorbed), then the mechanical/chemical split applied to chewing, and in
the harder band the same rule carried somewhere the lesson does not go — a
swallowed coin, feeding into a vein, a stomach removed, and starch finished in
a different organ from the one that started it.

The distractors are built from the lesson's two declared misconceptions —
DIET-11 "digestion is food being squashed into smaller and smaller pieces"
(which reappears as chewing making molecules smaller, tasting sweetness from
broken pieces, chewing longer finishing starch, and fewer enzymes being needed)
and DIET-12 "food sits in your stomach until it is digested, then goes to the
intestine" (which reappears as the stomach finishing digestion, absorbing the
meal, working four times faster, and keeping back the food while leftovers
travel on) — plus the hook's own wrong option that a liquid with no lumps in it
must be digested, and the everyday belief that gravity, not muscle, moves a
swallowed mouthful down.
"""

UNIT = "B3"
LESSON = "the-digestive-system"
LESSON_NUMBER = 5

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-e01",
        "band": "easier",
        "text": "Swallow a mouthful and it reaches your stomach in about "
                "eight seconds. What moves it down the oesophagus?",
        "options": [
            {"text": "Gravity, pulling the food down the tube towards the "
                     "stomach below", "correct": False,
             "why": "Gravity is not doing it. The wave of muscle works just "
                    "as well upside down, and an astronaut in orbit can "
                    "swallow with no gravity at all."},
            {"text": "Saliva, which makes the mouthful slippery enough to "
                     "slide down on its own", "correct": False,
             "why": "Saliva does lubricate the food so it can be swallowed, "
                    "but slippery is not the same as pushed. The squeeze from "
                    "the muscle wall is what moves it."},
            {"text": "Rings of muscle contracting behind the food and "
                     "relaxing in front of it", "correct": True},
            {"text": "The stomach, which pulls the food down by sucking it "
                     "in from below", "correct": False,
             "why": "The stomach churns whatever arrives; it does not pull "
                    "food towards it. The squeeze comes from the oesophagus "
                    "wall itself, and it is called peristalsis."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e02",
        "band": "easier",
        "text": "Which organs are part of the digestive system even though "
                "food never passes through them?",
        "options": [
            {"text": "The pancreas, liver and gall bladder", "correct": True},
            {"text": "The stomach and the small intestine", "correct": False,
             "why": "Both sit directly on the food's route — the meal spends "
                    "about four hours inside the stomach and about sixteen "
                    "inside the small intestine."},
            {"text": "The mouth and the oesophagus", "correct": False,
             "why": "Food starts in the mouth and travels the oesophagus in "
                    "about eight seconds. They are the first two stops on the "
                    "journey, not organs it misses."},
            {"text": "The large intestine and the rectum", "correct": False,
             "why": "Material still passes through both. The large intestine "
                    "takes the water back out of it, and the rectum stores "
                    "what is left until egestion."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e03",
        "band": "easier",
        "text": "The solid material that leaves through the anus is fibre, "
                "bacteria and water that were never absorbed into your blood. "
                "What is getting rid of it called?",
        "options": [
            {"text": "Excretion", "correct": False,
             "why": "Excretion is getting rid of waste your own cells "
                    "produced, such as urea and carbon dioxide. This material "
                    "never got into you in the first place, and examiners "
                    "care about the difference."},
            {"text": "Egestion", "correct": True},
            {"text": "Absorption", "correct": False,
             "why": "Absorption runs the other way — small soluble molecules "
                    "crossing the gut wall into the blood. This material is "
                    "leaving without ever having crossed it."},
            {"text": "Digestion", "correct": False,
             "why": "Digestion is the breaking of large insoluble molecules "
                    "into small soluble ones. Removing what is left at the "
                    "end of the tube is a separate job."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e04",
        "band": "easier",
        "text": "Hold a plain cracker on your tongue without chewing it and "
                "after about ninety seconds it tastes faintly sweet. What has "
                "happened?",
        "options": [
            {"text": "The warmth of your mouth has melted sugar that was "
                     "already in the cracker", "correct": False,
             "why": "A plain cracker is made of starch, not sugar, and "
                    "nothing melts at mouth temperature. The sweetness is "
                    "made in your mouth, not released from the cracker."},
            {"text": "Saliva contains sugar, and it has soaked into the dry "
                     "cracker on your tongue", "correct": False,
             "why": "Saliva is water, mucus and enzyme — there is no sugar in "
                    "it. What you taste was a starch molecule ninety seconds "
                    "earlier."},
            {"text": "Your teeth have broken the cracker into pieces small "
                     "enough for you to taste", "correct": False,
             "why": "You did not chew, and smaller pieces would taste no "
                    "sweeter anyway. Breaking something up never changes what "
                    "its molecules are."},
            {"text": "Amylase in your saliva has cut starch chains into "
                     "sugar you can taste", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-05-s01",
        "band": "standard",
        "text": "A student writes: “Food stays in the stomach until it is "
                "completely digested, and then it moves on to the intestine.” "
                "Which correction is right?",
        "options": [
            {"text": "The stomach finishes digestion and absorbs the food, "
                     "then passes on what is left", "correct": False,
             "why": "Almost nothing is absorbed through the stomach wall — no "
                    "glucose, no amino acids, no fatty acids. Absorption is "
                    "the small intestine's job, not the stomach's."},
            {"text": "The stomach starts protein digestion and releases the "
                     "meal into the small intestine bit by bit",
             "correct": True},
            {"text": "Nothing is wrong — the small intestine only receives "
                     "food the stomach has already finished with",
             "correct": False,
             "why": "This is exactly the idea the lesson exists to correct. "
                    "The stomach holds the meal for about four hours and only "
                    "begins on protein; every nutrient is finished further "
                    "along."},
            {"text": "The stomach digests nothing at all — it only stores the "
                     "meal and kills the bacteria", "correct": False,
             "why": "The acid does kill most of the bacteria swallowed with a "
                    "meal, but the stomach also adds protease, which begins "
                    "cutting protein into shorter chains. That is real "
                    "chemical digestion."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s02",
        "band": "standard",
        "text": "Two people eat the same sandwich. One chews it thoroughly, "
                "the other swallows almost at once. Both meals end up fully "
                "digested. What did the thorough chewing change?",
        "options": [
            {"text": "It made the food molecules smaller, so fewer enzymes "
                     "were needed further along", "correct": False,
             "why": "Chewing makes pieces smaller, never molecules. A crumb a "
                    "thousand times smaller is built from exactly the same "
                    "starch and protein molecules the slice was."},
            {"text": "It digested part of the sandwich, so there was less "
                     "left for the stomach to do", "correct": False,
             "why": "Teeth digest nothing on their own. Saliva starts on "
                    "starch chemically, but the cutting and grinding is "
                    "mechanical digestion and changes no molecule at all."},
            {"text": "Nothing at all — chewing only makes the mouthful easier "
                     "for you to swallow", "correct": False,
             "why": "Swallowing is one reason to chew, but not the only one. "
                    "More, smaller pieces means far more surface for the "
                    "enzymes to attack."},
            {"text": "It exposed more surface for the enzymes, so the "
                     "chemical breakdown happens faster", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s03",
        "band": "standard",
        "text": "By the time material reaches the large intestine the "
                "nutrients have already gone. What does the large intestine "
                "take out of what arrives?",
        "options": [
            {"text": "Most of the water, plus some minerals and vitamins",
             "correct": True},
            {"text": "The last of the glucose and the amino acids in the "
                     "meal", "correct": False,
             "why": "Those were absorbed in the small intestine, which "
                    "absorbs almost everything. What arrives here is water, "
                    "fibre and bacteria."},
            {"text": "Nothing — it only stores the material until it is "
                     "egested", "correct": False,
             "why": "Storing it is the rectum's job. The large intestine "
                    "absorbs most of the water back, which is what turns what "
                    "arrives into a solid mass."},
            {"text": "The fibre, which its own enzymes break down into "
                     "sugars", "correct": False,
             "why": "Your enzymes cannot break fibre at all. The gut bacteria "
                    "living there digest some of it, but those are their "
                    "enzymes, not yours."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s04",
        "band": "standard",
        "text": "The chart puts the stomach at about four hours and the small "
                "intestine at about sixteen. What does that comparison tell "
                "you about the two organs?",
        "options": [
            {"text": "The stomach works four times faster than the small "
                     "intestine, so it does most of the digesting",
             "correct": False,
             "why": "A shorter stay is not faster work. The stomach only "
                    "begins on protein; the small intestine needs sixteen "
                    "hours because it finishes every nutrient off."},
            {"text": "Most of the meal is stored in the stomach and only the "
                     "leftovers travel any further", "correct": False,
             "why": "The stomach passes the whole meal on, a little at a "
                    "time. Nothing is kept back, and almost nothing is "
                    "absorbed through its wall."},
            {"text": "The small intestine holds the meal four times as long, "
                     "because that is where the work happens",
             "correct": True},
            {"text": "The small intestine is slower only because it is much "
                     "longer and much narrower than the stomach",
             "correct": False,
             "why": "It is six or seven metres of narrow tube, but its length "
                    "is not the reason for the time. The meal is held there "
                    "because that is where digestion is completed and "
                    "absorption happens."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-h01",
        "band": "harder",
        "text": "A child swallows a small smooth coin and it comes out "
                "unchanged three days later. In what sense was the coin never "
                "actually inside the child?",
        "options": [
            {"text": "It was inside — it entered at the mouth and left again "
                     "at the anus, unchanged", "correct": False,
             "why": "Swallowing is not entering. The gut is one continuous "
                    "tube from mouth to anus, so its contents are still "
                    "outside you until they cross the wall."},
            {"text": "Stomach acid cannot dissolve metal, so the coin was "
                     "egested instead of being absorbed", "correct": False,
             "why": "True, but not the reason. A fully digested meal is also "
                    "still outside you while it is in the gut — what counts "
                    "is crossing the wall, not being dissolved."},
            {"text": "The coin was too heavy for peristalsis, so gravity "
                     "carried it straight through the gut", "correct": False,
             "why": "Peristalsis moves everything along, coin included, and "
                    "it works without gravity — you can swallow upside down. "
                    "The coin was carried, not dropped."},
            {"text": "It stayed inside a tube open at both ends — nothing "
                     "enters you until it is absorbed", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h02",
        "band": "harder",
        "text": "A patient too ill to eat is fed through a vein. The liquid "
                "contains glucose and amino acids rather than starch and "
                "protein. Why must it?",
        "options": [
            {"text": "Blood carries food only as small soluble molecules, and "
                     "this feed skips the gut entirely", "correct": True},
            {"text": "Enzymes in the blood would digest starch and protein "
                     "far too slowly to be any use", "correct": False,
             "why": "The digestive enzymes work along the gut, not in the "
                    "blood. Food put straight into a vein has skipped "
                    "digestion, so it has to arrive already cut up."},
            {"text": "Starch and protein are solids, and only a liquid can be "
                     "put into a vein safely", "correct": False,
             "why": "The blended sandwich was a smooth liquid and it was "
                    "still full of whole starch molecules. Being liquid and "
                    "being digested are two different things."},
            {"text": "Glucose and amino acids release far more energy than "
                     "starch and protein do", "correct": False,
             "why": "Energy is not the problem — size is. Starch and protein "
                    "molecules are far too large to cross a cell membrane, "
                    "which is the whole reason digestion exists."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h03",
        "band": "harder",
        "text": "Someone has their whole stomach removed after illness, and "
                "is told they can still digest and absorb meals if they eat "
                "small amounts often. Which explanation fits?",
        "options": [
            {"text": "Without a stomach, protein cannot be digested at all "
                     "and has to be avoided", "correct": False,
             "why": "The pancreas supplies protease into the small intestine, "
                    "where every nutrient is broken down to completion. The "
                    "stomach only ever began the job."},
            {"text": "Without a stomach, a meal would pass straight out of "
                     "the body undigested", "correct": False,
             "why": "The meal still spends about sixteen hours in the small "
                    "intestine, and that is where nearly all digestion is "
                    "completed and nearly all absorption happens."},
            {"text": "The small intestine does the digesting and absorbing — "
                     "what is lost is a holding tank", "correct": True},
            {"text": "The large intestine takes over the stomach's job of "
                     "digesting and absorbing the meal", "correct": False,
             "why": "The large intestine breaks down nothing your own enzymes "
                    "can touch, and it absorbs water rather than food. It "
                    "cannot stand in for anything."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h04",
        "band": "harder",
        "text": "Salivary amylase gets about one minute on the starch before "
                "the mouthful is swallowed, yet starch is broken down "
                "completely. Where is that job finished, and how?",
        "options": [
            {"text": "In the mouth — chewing for longer would break the "
                     "starch down completely", "correct": False,
             "why": "Chewing longer makes more, smaller pieces and never a "
                    "shorter molecule. Only an enzyme can cut a starch chain, "
                    "and one minute is nowhere near long enough."},
            {"text": "In the small intestine, by amylase from the pancreas, "
                     "over about sixteen hours", "correct": True},
            {"text": "In the stomach, where salivary amylase carries on "
                     "working for about four hours", "correct": False,
             "why": "The stomach's chemical job is protein — acid at about "
                    "pH 2 and protease. Starch is finished further along, "
                    "using amylase the pancreas supplies."},
            {"text": "In the large intestine, where whatever starch is left "
                     "is finally absorbed", "correct": False,
             "why": "Nothing your own enzymes can break is broken there, and "
                    "the nutrients have gone before material arrives. It "
                    "takes water back, not food."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Six further rows, two per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-e05",
        "band": "easier",
        "text": "What does the stomach add to a meal, and what does it begin "
                "to break down?",
        "options": [
            {"text": "Bile from the gall bladder, and it begins to break down "
                     "lipid.", "correct": False,
             "why": "Bile is made by the liver, stored in the gall bladder and "
                    "released into the small intestine. None of it is added in "
                    "the stomach."},
            {"text": "Hydrochloric acid at about pH 2, and it begins to break "
                     "down protein.", "correct": True},
            {"text": "Amylase from the salivary glands, and it begins to "
                     "break down starch.", "correct": False,
             "why": "Amylase comes from the salivary glands and the pancreas. "
                    "Stomach acid is what stops the mouth's amylase working."},
            {"text": "An alkali at about pH 8, and it finishes breaking down "
                     "every nutrient.", "correct": False,
             "why": "The alkali comes from the pancreas, into the small "
                    "intestine, and it is the small intestine that finishes "
                    "every nutrient."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e06",
        "band": "easier",
        "text": "What does the word digestion mean?",
        "options": [
            {"text": "Breaking food into smaller and smaller pieces.",
             "correct": False,
             "why": "That is mechanical breakdown, and it changes no "
                    "molecules. A crumb a thousand times smaller is still made "
                    "of the same molecules."},
            {"text": "Small soluble molecules moving out of the gut into the "
                     "blood.", "correct": False,
             "why": "That is absorption. It happens after digestion, and it "
                    "needs digestion to have happened first."},
            {"text": "Removing material that passed through the gut and was "
                     "never absorbed.", "correct": False,
             "why": "That is egestion — the last stop of the system rather "
                    "than the whole process."},
            {"text": "Breaking large insoluble molecules into small soluble "
                     "ones.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-05-s05",
        "band": "standard",
        "text": "The pancreas sends an alkali into the small intestine "
                "alongside its enzymes. Why is the alkali needed?",
        "options": [
            {"text": "The meal arrives acidic, and the enzymes here work at "
                     "about pH 8.", "correct": True},
            {"text": "It kills any bacteria that the stomach acid did not.",
             "correct": False,
             "why": "Killing swallowed bacteria is the stomach acid's own "
                    "job. The alkali is there to change the pH for the "
                    "enzymes."},
            {"text": "It digests the fat that the stomach could not break "
                     "down.", "correct": False,
             "why": "An alkali is not an enzyme and digests nothing. Fat is "
                    "broken down by lipase, with bile spreading it into small "
                    "droplets first."},
            {"text": "It neutralises the food so that it can cross the gut "
                     "wall into the blood.", "correct": False,
             "why": "What crosses the wall is decided by molecule size and "
                    "solubility, not by pH. The pH matters to the enzymes "
                    "doing the cutting."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s06",
        "band": "standard",
        "text": "A meal spends about 4 hours in the stomach, about 16 in the "
                "small intestine and 12 to 30 hours in the large intestine. "
                "Why does the large intestine hold it longest of all, when it "
                "breaks nothing down?",
        "options": [
            {"text": "Because the nutrients are still being absorbed there, "
                     "and that takes a long time.", "correct": False,
             "why": "By the time material arrives the nutrients have already "
                    "gone. What the large intestine takes back is water."},
            {"text": "Because it is the longest part of the gut, so the "
                     "journey through it takes longer.", "correct": False,
             "why": "It is wider and shorter than the small intestine, not "
                    "longer. Six or seven metres of narrow tube comes before "
                    "it."},
            {"text": "Because it is absorbing water back out of what is left, "
                     "and that is slow work.", "correct": True},
            {"text": "Because peristalsis stops there, so material moves only "
                     "when something pushes it.", "correct": False,
             "why": "Peristalsis happens the whole length of the gut. Nothing "
                    "about the muscle wave stops at the large intestine."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-h05",
        "band": "harder",
        "text": "Carbon dioxide breathed out and the solid material leaving "
                "the anus are both being got rid of. Only one of them is "
                "excretion. Which, and why?",
        "options": [
            {"text": "The solid material, because it leaves as waste at the "
                     "end of the gut.", "correct": False,
             "why": "It was never absorbed, so your own chemistry never made "
                    "it. Getting rid of what you never took in is egestion."},
            {"text": "The carbon dioxide — your own cells made it, so it is "
                     "your own waste.", "correct": True},
            {"text": "Both of them, because excretion is any waste leaving "
                     "the body at all.", "correct": False,
             "why": "Excretion is specifically waste your own cells produced. "
                    "Material that passed straight through is egested "
                    "instead."},
            {"text": "Neither, because excretion covers only urine leaving "
                     "the kidneys.", "correct": False,
             "why": "Urea in urine is excretion, and so is the carbon dioxide "
                    "you breathe out. Both were made by your own cells."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h06",
        "band": "harder",
        "text": "A person's pancreas stops producing its secretions "
                "altogether. Predict what changes about digestion, and name "
                "something that does not change.",
        "options": [
            {"text": "Nothing changes, because the small intestine makes all "
                     "its own enzymes.", "correct": False,
             "why": "The intestine wall supplies some enzymes, but the "
                    "pancreas supplies amylase, protease and lipase into it, "
                    "along with the alkali."},
            {"text": "Nothing is digested at all, and chewing stops working "
                     "as well.", "correct": False,
             "why": "Chewing and the stomach are untouched — the pancreas "
                    "sits off the tube. Digestion becomes far less complete "
                    "rather than stopping."},
            {"text": "Absorption stops but digestion carries on, because the "
                     "villi are unaffected.", "correct": False,
             "why": "That is the wrong way round. The villi are intact, so "
                    "the absorbing surface is fine; what is lost is what cuts "
                    "molecules small enough to cross it."},
            {"text": "Digestion becomes far less complete, while chewing, "
                     "swallowing and stomach acid carry on.", "correct": True},
        ],
        "figure": None,
    },
]
