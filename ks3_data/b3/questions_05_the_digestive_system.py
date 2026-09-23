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
        "text": "The chart shows the typical time food spends in each part "
                "of the gut. What mainly happens to food in the part where "
                "it spends the longest?",
        "options": [
            {"text": "Most of the digested food is absorbed into the blood",
             "correct": False,
             "why": "That happens in the small intestine, and food passes "
                    "through it in a few hours. The tallest bar is the large "
                    "intestine."},
            {"text": "Protein digestion begins, helped by stomach acid",
             "correct": False,
             "why": "That happens in the stomach, where food stays for only "
                    "a few hours. The tallest bar is the large intestine."},
            {"text": "Water is absorbed from the undigested food",
             "correct": True},
            {"text": "Food is broken up by chewing and mixed with saliva",
             "correct": False,
             "why": "That happens in the mouth, where food stays for about a "
                    "minute — the shortest bar on the chart."},
        ],
        "figure": "b3-gut-transit-times",
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

    # ── MRB-338 night 3 top-up ───────────────────────────────────────────
    # Twenty-four further rows per band, appended at bank_position 12+ so
    # the original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-e07",
        "band": "easier",
        "text": "What is peristalsis?",
        "options": [
            {"text": "The wave of muscle contraction that squeezes food "
                     "along the gut.", "correct": True},
            {"text": "The layer of mucus that protects the stomach lining "
                     "from its own acid.", "correct": False,
             "why": "That is a separate defence in the stomach wall, not the "
                    "muscle wave that moves food along the tube."},
            {"text": "The chemical process that cuts starch into shorter "
                     "sugar chains using an enzyme.", "correct": False,
             "why": "That describes an enzyme's job. Peristalsis is muscular "
                    "movement, not a chemical reaction."},
            {"text": "The folding of the gut wall that gives it extra "
                     "surface.", "correct": False,
             "why": "Folding is about surface area for absorption. "
                    "Peristalsis is the squeeze of muscle that moves food."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e08",
        "band": "easier",
        "text": "Saliva does two separate jobs on a mouthful of food. What "
                "are they?",
        "options": [
            {"text": "Absorbing glucose and moving the food along the tube.",
             "correct": False,
             "why": "Absorption happens far along in the small intestine, "
                    "and moving food is peristalsis, not saliva."},
            {"text": "Lubricating the food and starting to digest starch "
                     "chemically.", "correct": True},
            {"text": "Killing bacteria and neutralising stomach acid.",
             "correct": False,
             "why": "Killing swallowed bacteria is stomach acid's job, and "
                    "neutralising the acid is the pancreas's alkali, later "
                    "on."},
            {"text": "Breaking protein into amino acids and storing the "
                     "meal.", "correct": False,
             "why": "Protease breaks protein, and storage is the stomach's "
                    "job — saliva does neither."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e09",
        "band": "easier",
        "text": "What stops stomach acid from digesting the stomach's own "
                "lining?",
        "options": [
            {"text": "The acid only ever touches the food, never the "
                     "stomach wall itself.", "correct": False,
             "why": "The acid fills the stomach and would reach the wall — "
                    "the mucus layer is the actual barrier."},
            {"text": "Protease neutralises the acid before it can cause any "
                     "damage.", "correct": False,
             "why": "Protease is an enzyme, not a neutraliser, and it works "
                    "alongside the acid rather than cancelling it."},
            {"text": "A layer of mucus that the lining secretes and "
                     "replaces every few days.", "correct": True},
            {"text": "The stomach lining is simply immune to acid of any "
                     "strength.", "correct": False,
             "why": "It is not immune — the acid genuinely could dissolve the "
                    "stomach. A mucus layer is what protects it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e10",
        "band": "easier",
        "text": "Most stomach ulcers are actually caused by what?",
        "options": [
            {"text": "Stress alone, with no bacterium involved at all.",
             "correct": False,
             "why": "Stress can make symptoms worse, but the usual cause "
                    "named is a bacterium breaking down the stomach's "
                    "defences."},
            {"text": "Chewing food too quickly before swallowing it down.",
             "correct": False,
             "why": "Chewing speed is not linked to ulcers — the cause is "
                    "usually a bacterium that damages the protective lining."},
            {"text": "Eating spicy food too often.", "correct": False,
             "why": "Spicy food can irritate an existing ulcer, but it is not "
                    "the usual underlying cause."},
            {"text": "A bacterium, rather than stress or spicy food.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e11",
        "band": "easier",
        "text": "Which organ makes bile?",
        "options": [
            {"text": "The liver.", "correct": True},
            {"text": "The small intestine wall.", "correct": False,
             "why": "The small intestine wall supplies some enzymes, but "
                    "bile itself is made in the liver."},
            {"text": "The gall bladder.", "correct": False,
             "why": "The gall bladder stores bile and releases it — the "
                    "liver is the organ that makes it."},
            {"text": "The pancreas.", "correct": False,
             "why": "The pancreas makes enzymes and an alkali, not bile. "
                    "Bile is made by the liver."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e12",
        "band": "easier",
        "text": "What does the gall bladder do with the bile the liver "
                "makes?",
        "options": [
            {"text": "It absorbs the bile into the bloodstream for the body "
                     "to use.", "correct": False,
             "why": "Bile is released into the gut to work on fat, not "
                    "absorbed into the blood by the gall bladder."},
            {"text": "It stores the bile and releases it onto fatty food.",
             "correct": True},
            {"text": "It digests the bile so the liver can use it again.",
             "correct": False,
             "why": "Bile is not digested or reused this way — the gall "
                    "bladder simply stores it until it is needed."},
            {"text": "It makes the bile from raw materials the liver "
                     "supplies.", "correct": False,
             "why": "The liver makes the finished bile itself. The gall "
                    "bladder's job is storing and releasing it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e13",
        "band": "easier",
        "text": "What job does the oesophagus do?",
        "options": [
            {"text": "It absorbs some of the meal's water on the way down.",
             "correct": False,
             "why": "No absorption happens in the oesophagus — its only job "
                    "is transport."},
            {"text": "It stores the food briefly before releasing it into "
                     "the stomach.", "correct": False,
             "why": "There is no storage stage here — food passes straight "
                    "through in about eight seconds."},
            {"text": "It transports food to the stomach and breaks nothing "
                     "down.", "correct": True},
            {"text": "It begins digesting protein before the stomach even "
                     "has a chance to take over the job.", "correct": False,
             "why": "The oesophagus adds no enzyme at all — that is the "
                    "stomach's job, further along."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e14",
        "band": "easier",
        "text": "What is the rectum's job in digestion?",
        "options": [
            {"text": "Absorbing the last of the glucose from the meal.",
             "correct": False,
             "why": "Glucose absorption is finished long before material "
                    "reaches the rectum, in the small intestine."},
            {"text": "Breaking down whatever fibre is left in the waste.",
             "correct": False,
             "why": "Nothing is broken down in the rectum — its job is "
                    "storage before egestion."},
            {"text": "Neutralising the last of the stomach acid.",
             "correct": False,
             "why": "Stomach acid is neutralised by pancreatic alkali far "
                    "earlier, in the small intestine."},
            {"text": "Storing the remaining solid material until it is "
                     "egested.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e15",
        "band": "easier",
        "text": "Compared with the small intestine, how does the large "
                "intestine look?",
        "options": [
            {"text": "Wider and shorter.", "correct": True},
            {"text": "Narrower and longer.", "correct": False,
             "why": "That describes the small intestine, not the large "
                    "intestine, which is wider and shorter."},
            {"text": "The same width, but much longer.", "correct": False,
             "why": "The two organs differ in width as well as length — the "
                    "large intestine is visibly wider."},
            {"text": "Narrower, but exactly the same length.", "correct": False,
             "why": "Neither the width nor the length matches — the large "
                    "intestine is wider and considerably shorter."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e16",
        "band": "easier",
        "text": "Mechanical digestion, such as chewing, changes food in what "
                "way?",
        "options": [
            {"text": "Into a form the body can use directly for energy.",
             "correct": False,
             "why": "Only chemical digestion produces molecules the body can "
                    "actually use — mechanical breakdown alone does not."},
            {"text": "Into smaller pieces, without changing the molecules "
                     "at all.", "correct": True},
            {"text": "Into shorter molecules that can cross into the "
                     "blood.", "correct": False,
             "why": "Shortening molecules is chemical digestion's job. "
                    "Mechanical digestion changes size, not molecules."},
            {"text": "Into a liquid that is automatically absorbed.",
             "correct": False,
             "why": "Being a liquid is not the same as being digested — a "
                    "blended meal is still full of large molecules."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e17",
        "band": "easier",
        "text": "What does chemical digestion always require?",
        "options": [
            {"text": "Muscle contractions.", "correct": False,
             "why": "Muscle contractions move food along — they are "
                    "peristalsis, not the chemical cutting of molecules."},
            {"text": "Stomach acid alone, with nothing else needed.",
             "correct": False,
             "why": "Acid changes pH, but the actual cutting of molecules "
                    "still needs an enzyme such as protease."},
            {"text": "Enzymes.", "correct": True},
            {"text": "Teeth.", "correct": False,
             "why": "Teeth carry out mechanical digestion. Only an enzyme can "
                    "carry out chemical digestion."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e18",
        "band": "easier",
        "text": "What is the difference between egestion and excretion?",
        "options": [
            {"text": "They are two names for exactly the same process.",
             "correct": False,
             "why": "They are genuinely different — one is material that "
                    "never entered you, the other is your own cells' waste."},
            {"text": "Egestion happens in the kidneys; excretion happens in "
                     "the gut.", "correct": False,
             "why": "It is the other way round for the gut — egestion is a "
                    "gut process. Excretion also includes carbon dioxide, not "
                    "only urine."},
            {"text": "Excretion only ever means removing solid waste from "
                     "the gut.", "correct": False,
             "why": "Excretion covers waste your own cells produced, such as "
                    "urea and carbon dioxide — solid gut waste is egestion."},
            {"text": "Egestion removes material never absorbed; excretion "
                     "removes waste your own cells made.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e19",
        "band": "easier",
        "text": "Which organ holds material for the longest total time?",
        "options": [
            {"text": "The large intestine.", "correct": True},
            {"text": "The small intestine.", "correct": False,
             "why": "The small intestine holds a meal for about sixteen "
                    "hours, less than the large intestine's twelve to thirty."},
            {"text": "The stomach.", "correct": False,
             "why": "The stomach holds a meal for only about four hours, far "
                    "less than the large intestine."},
            {"text": "The rectum.", "correct": False,
             "why": "The rectum holds material for a few hours at the very "
                    "end, less than the large intestine above it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e20",
        "band": "easier",
        "text": "Roughly how long does a mouthful spend in the mouth before "
                "being swallowed?",
        "options": [
            {"text": "About one day.", "correct": False,
             "why": "Food does not stay in the mouth anywhere near that "
                    "long — swallowing happens after roughly a minute."},
            {"text": "About one minute.", "correct": True},
            {"text": "About one second.", "correct": False,
             "why": "That is far too short for chewing and mixing with "
                    "saliva to happen — about a minute is nearer the mark."},
            {"text": "About one hour.", "correct": False,
             "why": "A mouthful is swallowed long before an hour passes — "
                    "around a minute is typical."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e21",
        "band": "easier",
        "text": "Roughly how long does a swallowed mouthful take to reach the "
                "stomach?",
        "options": [
            {"text": "About eight hours.", "correct": False,
             "why": "The oesophagus is a short, fast route — a mouthful "
                    "reaches the stomach in seconds, not hours."},
            {"text": "About eighty seconds.", "correct": False,
             "why": "That overstates it by a factor of ten — around eight "
                    "seconds is the figure for the oesophagus."},
            {"text": "About eight seconds.", "correct": True},
            {"text": "About eight minutes, roughly the same time food "
                     "spends in the mouth.", "correct": False,
             "why": "That is far too slow for peristalsis in the "
                    "oesophagus — the real figure is about eight seconds."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e22",
        "band": "easier",
        "text": "Which of these gives the correct order for a meal's journey "
                "through the gut?",
        "options": [
            {"text": "Mouth, stomach, oesophagus, small intestine, large "
                     "intestine, rectum.", "correct": False,
             "why": "The oesophagus comes before the stomach — it is the "
                    "tube that carries a swallowed mouthful down to it."},
            {"text": "Mouth, oesophagus, stomach, large intestine, small "
                     "intestine, rectum.", "correct": False,
             "why": "The small intestine comes first of the two. Material "
                    "reaches the large intestine only once the small "
                    "intestine has finished with it."},
            {"text": "Mouth, oesophagus, small intestine, stomach, large "
                     "intestine, rectum.", "correct": False,
             "why": "The stomach receives the meal straight from the "
                    "oesophagus, well before any of it reaches the small "
                    "intestine."},
            {"text": "Mouth, oesophagus, stomach, small intestine, large "
                     "intestine, rectum.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e23",
        "band": "easier",
        "text": "Is bile an enzyme?",
        "options": [
            {"text": "No — it breaks fat droplets apart physically and "
                     "digests nothing itself.", "correct": True},
            {"text": "Yes — it is the enzyme that breaks lipid into fatty "
                     "acids and glycerol.", "correct": False,
             "why": "That job belongs to lipase. Bile is not an enzyme and "
                    "digests nothing on its own."},
            {"text": "Yes, but only a weak one compared with lipase.",
             "correct": False,
             "why": "Bile is not an enzyme at all, weak or strong — it works "
                    "physically, splitting droplets rather than cutting "
                    "molecules."},
            {"text": "No, because it is made in the pancreas rather than the "
                     "liver.", "correct": False,
             "why": "It is right that bile is not an enzyme, but it is made "
                    "in the liver, not the pancreas."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e24",
        "band": "easier",
        "text": "An enzyme in saliva begins cutting which substance?",
        "options": [
            {"text": "Dietary fibre.", "correct": False,
             "why": "No enzyme of yours can break down fibre at any stage of "
                    "the gut, including in the mouth."},
            {"text": "Starch.", "correct": True},
            {"text": "Protein.", "correct": False,
             "why": "Protein digestion begins later, in the stomach, using "
                    "protease rather than the enzyme in saliva."},
            {"text": "Lipid.", "correct": False,
             "why": "Lipid digestion happens in the small intestine, using "
                    "lipase — not the enzyme found in saliva."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e25",
        "band": "easier",
        "text": "The gut is often described as one continuous tube. What does "
                "that mean about its two ends?",
        "options": [
            {"text": "It forms a closed loop with no opening at either end.",
             "correct": False,
             "why": "The tube is open at both ends — the mouth and the anus "
                    "— not sealed into a loop."},
            {"text": "It branches into two separate tubes partway along.",
             "correct": False,
             "why": "The gut is a single unbranched tube from one end to the "
                    "other."},
            {"text": "It runs unbroken from the mouth to the anus.",
             "correct": True},
            {"text": "It runs from the mouth to the stomach and stops "
                     "there.", "correct": False,
             "why": "The tube continues well beyond the stomach, all the way "
                    "to the anus."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e26",
        "band": "easier",
        "text": "Which of these organs does food actually travel through?",
        "options": [
            {"text": "The pancreas.", "correct": False,
             "why": "The pancreas feeds its juices into the tube but food "
                    "never enters it directly."},
            {"text": "The liver.", "correct": False,
             "why": "The liver sends bile into the tube through a duct, but "
                    "food itself never passes through the liver."},
            {"text": "The gall bladder.", "correct": False,
             "why": "The gall bladder releases stored bile into the tube — "
                    "food never enters the gall bladder itself."},
            {"text": "The stomach.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e27",
        "band": "easier",
        "text": "Which enzyme does the stomach add to a meal?",
        "options": [
            {"text": "Protease.", "correct": True},
            {"text": "Amylase.", "correct": False,
             "why": "Amylase comes from the salivary glands and pancreas — "
                    "stomach acid actually stops the mouth's amylase working."},
            {"text": "Lipase.", "correct": False,
             "why": "Lipase is added later, by the pancreas, into the small "
                    "intestine — not by the stomach."},
            {"text": "Bile.", "correct": False,
             "why": "Bile is not an enzyme and is not made by the stomach — "
                    "it comes from the liver."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e28",
        "band": "easier",
        "text": "Almost none of what reaches the rectum is a nutrient. Why "
                "is that?",
        "options": [
            {"text": "The nutrients leave the body through the kidneys "
                     "instead.", "correct": False,
             "why": "The kidneys remove waste your own cells made, not "
                    "nutrients from a meal. Nutrients are taken into the "
                    "blood in the small intestine."},
            {"text": "The nutrients were taken into the blood far earlier, "
                     "in the small intestine.", "correct": True},
            {"text": "The rectum digests the last of the nutrients itself "
                     "before storing anything.", "correct": False,
             "why": "Nothing is digested in the rectum. Its job is storage, "
                    "and the nutrients were taken up long before material "
                    "arrives there."},
            {"text": "The large intestine turns any nutrients that reach "
                     "it into water.", "correct": False,
             "why": "No such conversion happens. The nutrients had already "
                    "crossed into the blood in the small intestine, well "
                    "before this point."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e29",
        "band": "easier",
        "text": "Which organ supplies the alkali that neutralises stomach "
                "acid in the small intestine?",
        "options": [
            {"text": "The gall bladder.", "correct": False,
             "why": "The gall bladder stores and releases bile, not the "
                    "alkali that neutralises stomach acid."},
            {"text": "The large intestine.", "correct": False,
             "why": "The large intestine comes much later in the journey — "
                    "the alkali is supplied earlier, by the pancreas."},
            {"text": "The pancreas.", "correct": True},
            {"text": "The liver.", "correct": False,
             "why": "The liver's job here is making bile, not supplying the "
                    "alkali — that comes from the pancreas."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-e30",
        "band": "easier",
        "text": "Roughly how long does a typical meal take to travel the "
                "whole way from mouth to anus?",
        "options": [
            {"text": "About four hours, start to finish.", "correct": False,
             "why": "Four hours is roughly the stay in the stomach alone. "
                    "The whole journey is far longer than any single stop "
                    "along it."},
            {"text": "About an hour, since the gut moves food quickly.",
             "correct": False,
             "why": "An hour barely covers the stomach, let alone either "
                    "intestine. The full journey runs into a day or more."},
            {"text": "About a month, since the intestines are so long.",
             "correct": False,
             "why": "A month is vastly longer than the usual journey, which "
                    "is measured in hours adding up to a day or two."},
            {"text": "Somewhere between about a day and two days.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-05-s07",
        "band": "standard",
        "text": "A patient develops a stomach ulcer. Their doctor prescribes "
                "an antibiotic rather than simply telling them to avoid spicy "
                "food. Why?",
        "options": [
            {"text": "Most ulcers are caused by a bacterium, which an "
                     "antibiotic can treat directly.", "correct": True},
            {"text": "Spicy food is always the real cause, and the "
                     "antibiotic only masks the pain.", "correct": False,
             "why": "Spicy food can irritate an ulcer, but it is not "
                    "described as the underlying cause — a bacterium usually "
                    "is."},
            {"text": "Antibiotics are given for every stomach complaint as a "
                     "precaution.", "correct": False,
             "why": "The antibiotic is targeted at the specific bacterium "
                    "linked to most ulcers, not given as a general "
                    "precaution."},
            {"text": "Stress causes ulcers, and antibiotics reduce the "
                     "body's stress response.", "correct": False,
             "why": "Antibiotics act on bacteria, not on stress. The doctor "
                    "is treating the bacterial cause directly."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s08",
        "band": "standard",
        "text": "A student says the liver and the gall bladder “basically do "
                "the same job, since both are about bile.” Correct this.",
        "options": [
            {"text": "Neither organ actually makes bile — it is made in the "
                     "small intestine itself.", "correct": False,
             "why": "Bile is made in the liver, not the small intestine, "
                    "which only receives it once released."},
            {"text": "The liver makes the bile continuously; the gall "
                     "bladder stores it and releases it onto fatty food.",
             "correct": True},
            {"text": "The gall bladder makes the bile; the liver only "
                     "stores what is left over.", "correct": False,
             "why": "That reverses the roles. The liver is the organ that "
                    "makes bile; the gall bladder stores and releases it."},
            {"text": "Both organs make bile independently, and both release "
                     "it at the same time.", "correct": False,
             "why": "Only the liver makes bile. The gall bladder's separate "
                    "job is storing it and releasing it when needed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s09",
        "band": "standard",
        "text": "A doctor explains that the pancreas's role and the liver's "
                "role are different, even though both send secretions into "
                "the small intestine. What is the difference?",
        "options": [
            {"text": "Both supply exactly the same mixture, so there is no "
                     "real difference.", "correct": False,
             "why": "Their secretions are chemically different — one "
                    "supplies enzymes and alkali, the other supplies bile, "
                    "which digests nothing."},
            {"text": "The pancreas supplies enzymes only; the liver supplies "
                     "the alkali only, with neither organ ever contributing "
                     "both substances at once.", "correct": False,
             "why": "The pancreas supplies both the enzymes and the alkali "
                    "together — the liver's contribution is bile."},
            {"text": "The pancreas supplies enzymes and an alkali; the liver "
                     "supplies bile, which is not an enzyme at all.",
             "correct": True},
            {"text": "The pancreas supplies bile; the liver supplies "
                     "enzymes and the alkali.", "correct": False,
             "why": "That swaps the two organs' jobs. Bile comes from the "
                    "liver, and the enzymes and alkali come from the "
                    "pancreas."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s10",
        "band": "standard",
        "text": "A food processor purées a meal into a completely smooth "
                "paste. A student argues this paste must now be “pre-"
                "digested.” Explain what is wrong with that claim.",
        "options": [
            {"text": "Nothing is wrong — a smooth paste is digested by "
                     "definition.", "correct": False,
             "why": "Smoothness is not digestion. The starch and protein "
                    "molecules in the paste are exactly as long as they were "
                    "before it was puréed."},
            {"text": "The claim is wrong only because a food processor "
                     "cannot reach every part of the meal evenly, leaving "
                     "some larger lumps of food behind.",
             "correct": False,
             "why": "Even a perfectly even purée would still be undigested — "
                    "the issue is that blades cannot shorten a molecule at "
                    "all."},
            {"text": "The claim is right for starch, but wrong for protein.",
             "correct": False,
             "why": "It is wrong for both. Neither starch nor protein "
                    "molecules are shortened by mechanical breakdown of any "
                    "kind."},
            {"text": "The paste's molecules are exactly the same size as "
                     "before — only an enzyme, not a blade, can shorten "
                     "them.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s11",
        "band": "standard",
        "text": "Holding a plain cracker on the tongue produces a faintly "
                "sweet taste after about ninety seconds, but the starch is "
                "not fully broken down in that time. Explain both parts.",
        "options": [
            {"text": "Amylase has started cutting some starch into sugar, "
                     "but ninety seconds is not long enough to finish the "
                     "whole job.", "correct": True},
            {"text": "All the starch is fully broken down in ninety "
                     "seconds; the taste is simply delayed.", "correct": False,
             "why": "The starch is only partly broken down at this point — "
                    "the process finishes much later, in the small "
                    "intestine."},
            {"text": "The sweetness comes from sugar already present in the "
                     "cracker, unrelated to any enzyme, since crackers are "
                     "baked with a little sugar mixed into the dough.",
             "correct": False,
             "why": "A plain cracker is made of starch, not sugar — the "
                    "sweetness is produced by amylase, not released from "
                    "anything already there."},
            {"text": "Saliva itself is sweet, which is why the cracker "
                     "tastes different after a while.", "correct": False,
             "why": "Saliva is water, mucus and enzyme, with no sugar in it "
                    "— the taste comes from amylase acting on the starch."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s12",
        "band": "standard",
        "text": "The large intestine holds material for longer than any other "
                "organ, yet the small intestine is described as “the organ "
                "that actually does the work.” Are these two claims in "
                "conflict?",
        "options": [
            {"text": "No, but only because the large intestine secretly "
                     "digests some nutrients too.", "correct": False,
             "why": "The large intestine breaks down nothing your own "
                    "enzymes can touch — its long hold is about absorbing "
                    "water, not digesting anything."},
            {"text": "No — holding material longest and doing the most "
                     "chemical work are two different things.", "correct": True},
            {"text": "Yes — whichever organ holds material longest must be "
                     "doing the most work.", "correct": False,
             "why": "Time held and chemical work done are separate "
                    "measures. The large intestine's long hold is mostly "
                    "slow water absorption, not digestion."},
            {"text": "Yes, so one of the two claims about the large "
                     "intestine or small intestine must be false.",
             "correct": False,
             "why": "Both claims can be true at once — length of stay does "
                    "not decide how much chemical work an organ is doing."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s13",
        "band": "standard",
        "text": "Suppose the pancreas released its enzymes into the small "
                "intestine but stopped supplying the alkali. Predict the "
                "effect.",
        "options": [
            {"text": "The enzymes would simply move faster without the "
                     "alkali slowing them down.", "correct": False,
             "why": "The alkali does not slow enzymes — it creates the pH "
                    "they need to work well in the first place."},
            {"text": "Digestion would stop completely, since the alkali is "
                     "itself an enzyme.", "correct": False,
             "why": "The alkali is not an enzyme, so it cannot itself stop "
                    "digestion — but conditions would be far from ideal for "
                    "the ones present."},
            {"text": "The enzymes would arrive in acidic conditions and work "
                     "far less effectively.", "correct": True},
            {"text": "Nothing would change, since the alkali has no effect "
                     "on enzymes.", "correct": False,
             "why": "The alkali sets the pH the enzymes need — without it, "
                    "the arriving acid would leave conditions wrong for "
                    "them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s14",
        "band": "standard",
        "text": "A vitamin tablet is swallowed whole and travels the length "
                "of the gut before dissolving in the small intestine. At "
                "what point does it actually enter the body?",
        "options": [
            {"text": "The moment it is swallowed at the mouth.",
             "correct": False,
             "why": "Swallowing places it inside the tube, which is "
                    "topologically still outside the body until something "
                    "crosses the wall."},
            {"text": "As soon as it reaches the stomach and is churned.",
             "correct": False,
             "why": "Churning changes its position and shape, not whether it "
                    "has crossed into the blood — that happens later, if at "
                    "all."},
            {"text": "As soon as it dissolves, wherever in the gut that "
                     "happens.", "correct": False,
             "why": "Dissolving is not the same as crossing the gut wall — "
                    "the contents still have to be absorbed to enter the "
                    "body."},
            {"text": "Only once its contents cross the gut wall into the "
                     "blood.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s15",
        "band": "standard",
        "text": "Starch is digested into glucose in the small intestine, but "
                "the glucose does not immediately count as “inside” the "
                "body. Explain why not.",
        "options": [
            {"text": "The glucose is still inside the gut tube until it "
                     "crosses the wall into the blood by absorption.",
             "correct": True},
            {"text": "It does count as inside the body the instant it is "
                     "made, since digestion has already finished.",
             "correct": False,
             "why": "Being digested and being absorbed are two separate "
                    "steps — the glucose is still in the gut until it "
                    "crosses into the blood."},
            {"text": "Glucose only becomes real once it has been carried to "
                     "the liver.", "correct": False,
             "why": "The liver is not what makes it count as inside the "
                    "body — crossing the gut wall by absorption is the "
                    "step that matters."},
            {"text": "It never counts as inside the body, even after "
                     "absorption.", "correct": False,
             "why": "Once absorbed into the blood, it genuinely is inside "
                    "the body — the gut itself is the part that is "
                    "topologically outside."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s16",
        "band": "standard",
        "text": "Protease is present in the stomach, and protease breaks down "
                "protein. The stomach lining itself is made of protein. Why "
                "does the protease not digest the stomach lining?",
        "options": [
            {"text": "The acid destroys the protease before it can reach "
                     "the lining.", "correct": False,
             "why": "The stomach's protease is specifically built to work in "
                    "that acid — the mucus layer, not acid destroying the "
                    "enzyme, is the real protection."},
            {"text": "A mucus layer protects the lining from the protease "
                     "and acid alike.", "correct": True},
            {"text": "Protease only works on protein that has already been "
                     "swallowed as food.", "correct": False,
             "why": "Protease has no way of telling swallowed protein apart "
                    "from the lining's own protein — the protection is "
                    "physical, the mucus layer."},
            {"text": "The stomach lining is not actually made of protein.",
             "correct": False,
             "why": "The lining is protein-based like other body tissue — "
                    "what protects it is the mucus layer, not a different "
                    "composition."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s17",
        "band": "standard",
        "text": "Explain why the oesophagus adds no enzyme to a swallowed "
                "mouthful.",
        "options": [
            {"text": "Enzymes cannot survive the speed food travels through "
                     "the oesophagus.", "correct": False,
             "why": "Speed is not the reason — the oesophagus simply has no "
                    "digestive role beyond moving the food along."},
            {"text": "The food has already been fully digested by the time "
                     "it is swallowed.", "correct": False,
             "why": "Digestion has barely begun by the time food is "
                    "swallowed — the oesophagus's job is purely to transport "
                    "it onward."},
            {"text": "Its only job is transporting food, so there is "
                     "nothing there for an enzyme to do.", "correct": True},
            {"text": "It does add an enzyme, but only a very weak one "
                     "compared with the stomach's.", "correct": False,
             "why": "No enzyme is added in the oesophagus at all — it is "
                    "described purely as a transport stage."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s18",
        "band": "standard",
        "text": "A capsule is designed to pass through the stomach unopened "
                "and only dissolve once it reaches the small intestine. "
                "While it sits, unopened, in the stomach, has it entered the "
                "body?",
        "options": [
            {"text": "Yes — being inside the stomach already counts as "
                     "being inside the body.", "correct": False,
             "why": "The stomach is part of the continuous tube running "
                    "from mouth to anus, which is topologically outside the "
                    "body until absorption happens."},
            {"text": "It depends on how strong the stomach acid is at the "
                     "time.", "correct": False,
             "why": "Acid strength decides whether the capsule dissolves "
                    "there, not whether its unopened contents have entered "
                    "the body."},
            {"text": "Yes, because the stomach wall is thin enough for gases "
                     "to pass through it.", "correct": False,
             "why": "This is about the capsule's solid contents, not gas "
                    "exchange — nothing has crossed the wall while it stays "
                    "unopened."},
            {"text": "No — it is still inside the tube, and nothing has "
                     "crossed the gut wall yet.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s19",
        "band": "standard",
        "text": "Peristalsis in a short section of the small intestine stops "
                "working, though the muscle either side of it is fine. "
                "Predict what happens to the meal at that point.",
        "options": [
            {"text": "The meal would back up behind the affected section, "
                     "since nothing is pushing it through.", "correct": True},
            {"text": "The meal would pass through that section just as "
                     "fast, carried by gravity instead, since gravity alone "
                     "is normally enough to move food through the gut.",
             "correct": False,
             "why": "Gravity is not what normally moves food along — "
                    "peristalsis works even upside down, so its failure is "
                    "not made up for by gravity."},
            {"text": "Digestion would simply skip that section and continue "
                     "further along as normal.", "correct": False,
             "why": "The meal cannot skip ahead — it has to physically pass "
                    "through the affected section, which peristalsis is "
                    "what normally achieves."},
            {"text": "Nothing would change, since peristalsis only matters "
                     "in the oesophagus.", "correct": False,
             "why": "Peristalsis happens along the whole gut, not only the "
                    "oesophagus — its failure anywhere would slow or block "
                    "the meal there."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s20",
        "band": "standard",
        "text": "Digestion and absorption are essentially finished by the "
                "time material leaves the small intestine, yet it is stored "
                "in the rectum before being egested rather than leaving "
                "straight away. Suggest why.",
        "options": [
            {"text": "There is no real reason — the delay is simply how "
                     "long the material happens to take to arrive.",
             "correct": False,
             "why": "The rectum's storage is a distinct function, letting "
                    "egestion be controlled rather than continuous, not "
                    "merely a side effect of travel time."},
            {"text": "Storage lets the body control when egestion happens, "
                     "rather than it occurring continuously.",
             "correct": True},
            {"text": "The rectum needs time to digest what is left before "
                     "it can be egested.", "correct": False,
             "why": "Nothing is digested in the rectum — its role is "
                    "storage, not further chemical breakdown."},
            {"text": "The material has to wait for the large intestine to "
                     "finish absorbing the last of the nutrients.",
             "correct": False,
             "why": "Nutrients were absorbed earlier, in the small "
                    "intestine — what the large intestine still takes is "
                    "water, not nutrients."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s21",
        "band": "standard",
        "text": "A steak is cut into small pieces with a knife and fork "
                "before being eaten. Has any chemical digestion happened at "
                "that point?",
        "options": [
            {"text": "Yes, but only a small amount, proportional to how "
                     "finely it is cut, since finer cutting is assumed to "
                     "release trace amounts of amino acids.", "correct": False,
             "why": "No amount of cutting produces any chemical change at "
                    "all — the protein molecules stay exactly as they were."},
            {"text": "It cannot be answered without knowing how sharp the "
                     "knife is.", "correct": False,
             "why": "Sharpness affects how small the pieces get, not "
                    "whether any chemical digestion has occurred — cutting "
                    "alone never produces it."},
            {"text": "No — cutting only makes pieces smaller; only an "
                     "enzyme can change the protein molecules themselves.",
             "correct": True},
            {"text": "Yes — cutting the steak breaks its protein down into "
                     "amino acids.", "correct": False,
             "why": "Cutting changes size, never molecules. Amino acids are "
                    "only produced by an enzyme such as protease."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s22",
        "band": "standard",
        "text": "Someone has an unusually dry mouth and produces very little "
                "saliva. Predict two effects this would have on a meal of "
                "bread.",
        "options": [
            {"text": "Swallowing would be harder, but starch digestion "
                     "would be unaffected since it happens later anyway.",
             "correct": False,
             "why": "Starch digestion does begin in the mouth, using "
                    "amylase in saliva — less saliva means less of that "
                    "happens."},
            {"text": "Starch digestion would fail completely and never "
                     "happen at any stage.", "correct": False,
             "why": "The pancreas supplies fresh amylase into the small "
                    "intestine later on, so starch digestion is delayed, not "
                    "abolished."},
            {"text": "Nothing would change, since saliva plays no real part "
                     "in either swallowing or digestion.", "correct": False,
             "why": "Saliva does two real jobs — lubricating for swallowing "
                    "and starting starch digestion — so a shortage affects "
                    "both."},
            {"text": "Swallowing would be harder, and starch digestion in "
                     "the mouth would barely start.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s23",
        "band": "standard",
        "text": "A fruit juice has all its pulp strained out, leaving a clear "
                "liquid with no visible lumps. A student says this juice "
                "must already be digested. Is that right?",
        "options": [
            {"text": "No — the sugars in it may already be small molecules, "
                     "but straining alone cannot chemically change "
                     "anything.", "correct": True},
            {"text": "Yes — removing the pulp is exactly what digestion "
                     "does to a food.", "correct": False,
             "why": "Straining is mechanical separation, not digestion. "
                    "Whether the juice needs digesting depends on the "
                    "molecules in it, not on its smoothness."},
            {"text": "Yes, because a liquid can always pass straight into "
                     "the blood without any further change, since only "
                     "solids ever need chemical breakdown first.",
             "correct": False,
             "why": "Being a liquid does not guarantee small enough, "
                    "soluble molecules — that depends on chemical digestion, "
                    "not texture."},
            {"text": "No, because straining actually makes the sugar "
                     "molecules larger.", "correct": False,
             "why": "Straining does not change any molecule's size at all — "
                    "it only removes solid pulp, leaving the liquid's own "
                    "molecules unchanged."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s24",
        "band": "standard",
        "text": "Someone has diarrhoea, and material moves through the large "
                "intestine far faster than usual. Predict the effect on the "
                "stool that results.",
        "options": [
            {"text": "The nutrients absorbed fall, since the large "
                     "intestine normally absorbs most of the meal's "
                     "glucose.", "correct": False,
             "why": "Glucose absorption happens earlier, in the small "
                    "intestine — the large intestine's job here is water, "
                    "not nutrients."},
            {"text": "It stays far more watery, since less time means less "
                     "water is absorbed back out of it.", "correct": True},
            {"text": "It becomes drier than usual, since faster movement "
                     "means more water is squeezed out.", "correct": False,
             "why": "Faster movement gives the large intestine less time to "
                    "absorb water, which makes the result wetter, not "
                    "drier."},
            {"text": "There is no effect on water content, since the "
                     "small intestine has already absorbed everything "
                     "needed.", "correct": False,
             "why": "Water absorption is specifically the large intestine's "
                    "job — less time there means less water taken back out."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s25",
        "band": "standard",
        "text": "Two identical apples are given to two people. One chews "
                "theirs thoroughly; the other swallows large chunks almost "
                "whole. Which apple is chemically digested more, assuming "
                "both are given plenty of time?",
        "options": [
            {"text": "The unchewed apple, because larger pieces hold onto "
                     "more of their own nutrients, which are assumed to "
                     "leak away once a piece is broken up.", "correct": False,
             "why": "Piece size affects how quickly enzymes can act, not how "
                    "many nutrients a piece contains — nothing is lost by "
                    "being in smaller pieces."},
            {"text": "It cannot be answered without knowing exactly how "
                     "ripe each apple is.", "correct": False,
             "why": "Ripeness is not the deciding factor here — given "
                    "enough time, chewing changes the speed of digestion, "
                    "not its eventual completeness."},
            {"text": "Neither — chewing changes how fast digestion happens, "
                     "not how completely it eventually finishes.",
             "correct": True},
            {"text": "The chewed apple, because chewing itself chemically "
                     "digests some of it.", "correct": False,
             "why": "Chewing is mechanical, not chemical — it exposes more "
                    "surface for enzymes but breaks no molecules itself."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s26",
        "band": "standard",
        "text": "The pancreas has two separate jobs feeding into the small "
                "intestine: supplying enzymes, and supplying an alkali. "
                "Suppose only the alkali-making part failed. What would "
                "still work normally?",
        "options": [
            {"text": "Nothing would still work, since the two jobs cannot "
                     "be separated from one another, as though they came "
                     "from a single combined process.", "correct": False,
             "why": "They are two distinct secretions — losing one does not "
                    "automatically stop the other from being released."},
            {"text": "The enzymes would simply switch to working in acidic "
                     "conditions instead.", "correct": False,
             "why": "Enzymes do not switch their working conditions — "
                    "without the alkali, they would be released into "
                    "conditions that suited them poorly."},
            {"text": "Bile production would take over the alkali's job "
                     "automatically.", "correct": False,
             "why": "Bile comes from the liver and has an entirely "
                    "different job — emulsifying fat, not neutralising "
                    "acid."},
            {"text": "The enzymes themselves would still be released, just "
                     "into conditions that suited them less well.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s27",
        "band": "standard",
        "text": "Suppose the stomach's acid were far weaker than normal, "
                "closer to neutral. Predict the effect on protein digestion "
                "there.",
        "options": [
            {"text": "The stomach's protease would work far less well, "
                     "since it needs strongly acidic conditions.",
             "correct": True},
            {"text": "Protein digestion would speed up, since most enzymes "
                     "are assumed to prefer neutral conditions over any "
                     "other pH.", "correct": False,
             "why": "The stomach's protease is specifically built to work "
                    "in strong acid — weaker acid would suit it worse, not "
                    "better."},
            {"text": "Nothing would change, because protease works equally "
                     "well at any pH.", "correct": False,
             "why": "The stomach's protease is unusual precisely because it "
                    "needs strong acid — a weaker acid would leave it far "
                    "from its working conditions."},
            {"text": "Protein digestion would move entirely into the mouth "
                     "instead.", "correct": False,
             "why": "The mouth has no protease at all — weaker stomach acid "
                    "would not shift protein digestion there."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s28",
        "band": "standard",
        "text": "A person eats a snack while lying flat on their back. "
                "Explain why the food still reaches their stomach.",
        "options": [
            {"text": "Lying flat makes no real difference because food "
                     "barely moves through the oesophagus at all.",
             "correct": False,
             "why": "Food does travel the oesophagus's length in either "
                    "position — what changes is nothing, since peristalsis "
                    "works the same way regardless."},
            {"text": "Peristalsis squeezes the food along regardless of "
                     "the body's position, since it does not rely on "
                     "gravity.", "correct": True},
            {"text": "Gravity still pulls the food towards the stomach even "
                     "when lying down, just more slowly.", "correct": False,
             "why": "The oesophagus's muscle wave, not gravity, is what "
                    "moves food — it works even when someone is upside "
                    "down."},
            {"text": "The stomach actively pulls food towards it by "
                     "suction.", "correct": False,
             "why": "The stomach does not suck food in — the squeeze comes "
                    "from the oesophagus wall itself, moving food along "
                    "regardless of position."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s29",
        "band": "standard",
        "text": "By roughly twenty hours after a meal, digestion of its "
                "nutrients is essentially complete, yet material can still "
                "sit in the large intestine for well over a day afterwards. "
                "Explain why this is not a contradiction.",
        "options": [
            {"text": "The large intestine must actually still be digesting "
                     "nutrients during that extra time.", "correct": False,
             "why": "By this stage the nutrients are long gone — what the "
                    "large intestine is doing in that time is absorbing "
                    "water, not digesting food."},
            {"text": "It is not a contradiction, but only because the "
                     "twenty-hour figure is measured incorrectly.",
             "correct": False,
             "why": "Both figures can be accurate together — they simply "
                    "describe two different processes running on two "
                    "different timescales."},
            {"text": "Digestion of nutrients and the slow absorption of "
                     "water afterwards are two separate processes.",
             "correct": True},
            {"text": "It is a contradiction — one of the two timings must "
                     "be wrong.", "correct": False,
             "why": "Both figures can be correct at once: nutrient digestion "
                    "finishes early, while water absorption in the large "
                    "intestine continues on its own separate, slower "
                    "timescale."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-s30",
        "band": "standard",
        "text": "A small plastic bead is accidentally swallowed and passes "
                "out unchanged a few days later. Using the idea that the gut "
                "is a tube open at both ends, explain why the bead was never "
                "truly inside the body.",
        "options": [
            {"text": "It was inside the body the whole time it sat in the "
                     "stomach, since that organ is deep within the body.",
             "correct": False,
             "why": "Being physically deep inside the body's outline is not "
                    "the same as crossing the gut wall — the bead never did "
                    "that."},
            {"text": "It only became part of the body once it reached the "
                     "large intestine.", "correct": False,
             "why": "Nothing about reaching the large intestine crosses the "
                    "gut wall — the bead stays outside the body the whole "
                    "way through."},
            {"text": "Plastic is a special case, because only digestible "
                     "materials can ever be considered outside the body.",
             "correct": False,
             "why": "The topology argument applies to anything travelling "
                    "the gut, digestible or not — what matters is crossing "
                    "the wall, not what the object is made of."},
            {"text": "It travelled the length of a continuous tube without "
                     "ever crossing the gut wall into the blood.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-05-h07",
        "band": "harder",
        "text": "A student claims the stomach must be “the main digestive "
                "organ” because it is the one everybody names first. "
                "Evaluate this claim against the actual roles of the "
                "stomach and the small intestine.",
        "options": [
            {"text": "The claim does not hold up — the small intestine "
                     "finishes every nutrient and does almost all "
                     "absorption, holding the meal four times as long.",
             "correct": True},
            {"text": "The claim is correct, since the stomach is the first "
                     "organ to add any digestive juice at all.",
             "correct": False,
             "why": "Being first is not the same as doing the most — the "
                    "small intestine's sixteen hours of work far exceeds the "
                    "stomach's four."},
            {"text": "The claim is correct, because the stomach absorbs "
                     "most of the meal's nutrients.", "correct": False,
             "why": "Almost nothing is absorbed through the stomach wall — "
                    "absorption is overwhelmingly the small intestine's "
                    "job."},
            {"text": "Neither organ does much work; most digestion happens "
                     "in the mouth.", "correct": False,
             "why": "The mouth only begins on starch for about a minute — "
                    "far less than either the stomach or the small "
                    "intestine achieves."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h08",
        "band": "harder",
        "text": "A gallstone blocks the duct that carries bile from the gall "
                "bladder into the small intestine, though the liver keeps "
                "making bile normally. Predict the effect on fat digestion.",
        "options": [
            {"text": "Lipase would begin working faster to make up for the "
                     "lost bile.", "correct": False,
             "why": "Lipase's rate is not boosted by a bile blockage — with "
                    "less surface exposed on large fat droplets, it actually "
                    "works more slowly overall."},
            {"text": "Fat droplets stay large, giving lipase far less "
                     "surface to work on, so fat digestion becomes far less "
                     "efficient.", "correct": True},
            {"text": "Fat digestion stops completely, because bile is the "
                     "enzyme that actually breaks lipid down.", "correct": False,
             "why": "Bile is not an enzyme — lipase does the actual "
                    "chemical breakdown. A blockage reduces efficiency but "
                    "does not remove the enzyme itself."},
            {"text": "Fat digestion is unaffected, since the liver is still "
                     "making bile even though the duct is blocked.",
             "correct": False,
             "why": "Making bile is not enough on its own — it has to reach "
                    "the small intestine through the duct to have any "
                    "effect on the fat there."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h09",
        "band": "harder",
        "text": "A patient is told their ulcer is “just from stress” and is "
                "advised only to relax more. Evaluate this advice against "
                "what is actually known about most stomach ulcers.",
        "options": [
            {"text": "It is correct only for ulcers in older patients, not "
                     "younger ones.", "correct": False,
             "why": "Age is not the deciding factor here — the bacterial "
                    "cause applies regardless of the patient's age."},
            {"text": "It is incomplete, but only because spicy food should "
                     "have been mentioned as well, alongside the usual "
                     "advice about stress and relaxation.", "correct": False,
             "why": "Adding spicy food to the advice would still miss the "
                    "point — the bacterium is the cause an antibiotic "
                    "actually treats."},
            {"text": "It is likely incomplete — most ulcers are caused by a "
                     "bacterium, which relaxation alone will not treat.",
             "correct": True},
            {"text": "It is entirely correct, since stress is the sole "
                     "cause of every stomach ulcer.", "correct": False,
             "why": "Stress can make symptoms worse, but the underlying "
                    "cause of most ulcers is a bacterium, which relaxation "
                    "does not address."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h10",
        "band": "harder",
        "text": "A rare condition means someone's stomach produces no acid "
                "at all, though the rest of their gut works normally. "
                "Predict two consequences.",
        "options": [
            {"text": "Nothing would change, since acid plays no real part "
                     "in either killing bacteria or aiding digestion, both "
                     "being handled entirely elsewhere in the gut.",
             "correct": False,
             "why": "Acid does two real jobs in the stomach — killing most "
                    "swallowed bacteria and giving the stomach's protease "
                    "the conditions it needs."},
            {"text": "Starch digestion would fail completely, since it "
                     "depends entirely on stomach acid.", "correct": False,
             "why": "Starch digestion depends on amylase, not acid, and it "
                    "is finished later in the small intestine regardless of "
                    "stomach acid."},
            {"text": "The small intestine would also stop working, since it "
                     "depends on receiving acidic material.", "correct": False,
             "why": "The small intestine actually needs the alkali to "
                    "neutralise arriving acid — less acid arriving would not "
                    "stop it working."},
            {"text": "Bacteria in swallowed food would survive more often, "
                     "and the stomach's protease would work far less well.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h11",
        "band": "harder",
        "text": "Boiling an egg changes its texture and chemistry "
                "noticeably. Explain why cooking is not considered "
                "digestion, even though it also changes the food.",
        "options": [
            {"text": "Cooking is a change caused by heat outside the body, "
                     "not by enzymes cutting molecules inside it.",
             "correct": True},
            {"text": "Cooking is not considered digestion only because it "
                     "happens too quickly to count, unlike the many hours "
                     "enzymes typically take inside the body.", "correct": False,
             "why": "Speed is not what defines digestion — the real "
                    "distinction is that digestion specifically means "
                    "enzymes cutting molecules, inside the body."},
            {"text": "Cooking and digestion are actually the same process, "
                     "just under different names.", "correct": False,
             "why": "They are genuinely different processes — one is a heat "
                    "change outside the body, the other is enzyme action "
                    "inside it."},
            {"text": "Cooking is not digestion because it makes food "
                     "harder rather than softer.", "correct": False,
             "why": "Texture change is not the deciding factor — what "
                    "matters is whether enzymes are cutting molecules inside "
                    "the body."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h12",
        "band": "harder",
        "text": "The large intestine holds material longer than the small "
                "intestine, but the small intestine is where “the work "
                "happens.” What does the large intestine's long hold "
                "actually reflect?",
        "options": [
            {"text": "That the large intestine holds material longest "
                     "purely because it comes last in the sequence.",
             "correct": False,
             "why": "Coming last does not explain WHY it takes so long — "
                    "the actual reason given is the slow process of "
                    "absorbing water back out."},
            {"text": "That absorbing water back out of the remaining "
                     "material is a slow process, not that much chemical "
                     "work is being done.", "correct": True},
            {"text": "That the large intestine is secretly finishing off "
                     "digestion the small intestine could not complete, "
                     "quietly continuing where its enzymes left off.",
             "correct": False,
             "why": "The large intestine breaks down nothing your own "
                    "enzymes can touch — its long hold reflects slow water "
                    "absorption, not digestion."},
            {"text": "That material simply travels more slowly there "
                     "because the tube is narrower.", "correct": False,
             "why": "The large intestine is wider, not narrower, than the "
                    "small intestine — its slow hold is about the pace of "
                    "water absorption, not tube width."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h13",
        "band": "harder",
        "text": "A patient has had their gall bladder removed and also takes "
                "a medicine that reduces how much acid their stomach makes. "
                "Which digestive step is affected by each change, and are "
                "the two effects connected?",
        "options": [
            {"text": "The two effects are connected, since bile is what "
                     "neutralises stomach acid.", "correct": False,
             "why": "Bile does not neutralise acid — that is the "
                    "pancreatic alkali's job. Bile's role is fat "
                    "emulsification."},
            {"text": "Losing the gall bladder makes the reduced-acid "
                     "medicine unnecessary, since digestion has already "
                     "slowed enough that reducing acid further changes "
                     "little.", "correct": False,
             "why": "The two changes act on entirely different substrates — "
                    "one slowing does not make the other pointless."},
            {"text": "The gall bladder loss affects fat digestion by "
                     "lipase; the reduced acid affects protein digestion by "
                     "protease — two separate, unconnected effects.",
             "correct": True},
            {"text": "Both changes affect exactly the same step — starch "
                     "digestion by amylase.", "correct": False,
             "why": "Neither change touches amylase or starch at all — one "
                    "concerns fat digestion, the other protein digestion."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h14",
        "band": "harder",
        "text": "Most dietary fibre passes through the gut almost entirely "
                "undigested and is egested. Using the topology idea that "
                "nothing enters you until it crosses the gut wall, was the "
                "fibre ever really “eaten” in the fullest sense?",
        "options": [
            {"text": "No — anything that is egested rather than absorbed "
                     "was never really swallowed at all.", "correct": False,
             "why": "Swallowing and absorption are two different events — "
                    "the fibre genuinely was swallowed, even though it "
                    "never crossed the gut wall."},
            {"text": "Yes, without qualification — fibre enters the body "
                     "the moment it passes the mouth.", "correct": False,
             "why": "Passing the mouth places it in the tube, which is "
                    "topologically outside the body until something is "
                    "absorbed."},
            {"text": "The question cannot be answered, since fibre is "
                     "neither digested nor absorbed at any point, which is "
                     "treated as placing it outside the topology idea "
                     "entirely.", "correct": False,
             "why": "The topology idea still applies cleanly here: fibre "
                    "stays in the tube the whole way and is egested, never "
                    "crossing into the blood."},
            {"text": "It was eaten in the everyday sense of being "
                     "swallowed, but in the topological sense it never "
                     "actually entered the body.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h15",
        "band": "harder",
        "text": "Capsule A dissolves completely in the stomach and its "
                "contents are absorbed there and then. Capsule B passes "
                "through the whole gut unopened and is egested intact. "
                "Compare when, if ever, each one enters the body.",
        "options": [
            {"text": "Capsule A enters the body once its dissolved contents "
                     "cross into the blood; Capsule B never enters the body "
                     "at all.", "correct": True},
            {"text": "Both enter the body the moment they are swallowed, "
                     "regardless of what happens to either capsule "
                     "afterwards or how differently their journeys end.",
             "correct": False,
             "why": "Swallowing places either capsule in the tube, not the "
                    "blood — only crossing the gut wall counts as entering "
                    "the body."},
            {"text": "Neither ever enters the body, since both start as "
                     "solid capsules rather than food.", "correct": False,
             "why": "Being a capsule rather than food makes no difference "
                    "to the topology — Capsule A's dissolved contents do "
                    "cross into the blood and so do enter the body."},
            {"text": "Capsule B enters the body sooner, since it travels "
                     "further along the tube than Capsule A.", "correct": False,
             "why": "Travelling further along the tube is not the same as "
                    "crossing its wall — Capsule B never crosses at all, so "
                    "it never enters the body."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h16",
        "band": "harder",
        "text": "A student argues the pancreas is “basically part of the "
                "small intestine,” since its juices go straight there. "
                "Evaluate this claim.",
        "options": [
            {"text": "The claim is wrong, but only because the pancreas "
                     "also supplies the stomach directly.", "correct": False,
             "why": "The pancreas feeds the small intestine, not the "
                    "stomach — the real reason the claim fails is that food "
                    "never enters the pancreas at all."},
            {"text": "It does not hold up — the pancreas is a separate "
                     "organ that food never enters, feeding juices in "
                     "through a duct rather than being part of the tube.",
             "correct": True},
            {"text": "The claim is correct, since anything supplying "
                     "digestive juices to the small intestine counts as "
                     "part of it, the same way the salivary glands would "
                     "then count as part of the mouth.", "correct": False,
             "why": "By that logic the liver and salivary glands would also "
                    "count — the small intestine is specifically the tube "
                    "food passes through."},
            {"text": "The claim is correct only because the pancreas sits "
                     "physically beside the small intestine.", "correct": False,
             "why": "Physical position is not what decides this — the "
                    "defining feature is that food itself never passes "
                    "through the pancreas."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h17",
        "band": "harder",
        "text": "An experimental drug completely stops a patient's stomach "
                "from producing acid. Explain two separate consequences this "
                "would have, beyond the effect on protease.",
        "options": [
            {"text": "The pancreas would need to supply acid instead, to "
                     "replace what the stomach no longer makes.",
             "correct": False,
             "why": "The pancreas supplies an alkali, not acid, and its job "
                    "is to neutralise arriving acid — it has no role "
                    "replacing missing stomach acid."},
            {"text": "Fat digestion by lipase would stop, since lipase "
                     "needs stomach acid to activate it.", "correct": False,
             "why": "Lipase works in the small intestine at an alkaline pH, "
                    "supplied by the pancreas — it has no dependence on "
                    "stomach acid."},
            {"text": "Bacteria swallowed with food would survive far more "
                     "often, and the mouth's amylase would keep working for "
                     "longer than usual in the stomach.", "correct": True},
            {"text": "Digestion would stop completely at every stage, since "
                     "the whole gut depends on stomach acid to function, "
                     "from the very first stop to the very last.",
             "correct": False,
             "why": "Later stages such as the small intestine have their "
                    "own separate chemistry, including an alkali — they do "
                    "not depend on stomach acid arriving."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h18",
        "band": "harder",
        "text": "A gymnast performs a handstand shortly after taking a sip "
                "of water. Explain why the water still reaches their "
                "stomach rather than staying in the oesophagus.",
        "options": [
            {"text": "It would not reach the stomach — gravity is required "
                     "for anything to travel down the oesophagus, in the "
                     "same way gravity is required for anything to fall.",
             "correct": False,
             "why": "Peristalsis works independently of gravity — an "
                    "astronaut can swallow with no gravity at all, and the "
                    "same muscular action applies here."},
            {"text": "The water reaches the stomach only because liquids "
                     "behave differently from solids in the gut.",
             "correct": False,
             "why": "Peristalsis moves solids and liquids alike — the "
                    "mechanism is the same muscular squeeze regardless of "
                    "what is swallowed."},
            {"text": "The stomach actively draws the water towards it by "
                     "suction through the oesophagus.", "correct": False,
             "why": "The stomach does not suck anything towards it — the "
                    "squeeze comes from the oesophagus wall's own muscle."},
            {"text": "Peristalsis squeezes the water along the oesophagus "
                     "using muscle contraction, not gravity, so orientation "
                     "makes no difference.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h19",
        "band": "harder",
        "text": "A complete blockage of the oesophagus stops all further "
                "digestion immediately, while a complete blockage of the "
                "bile duct leaves most digestion still running. Explain why "
                "blocking these two points has such different severity.",
        "options": [
            {"text": "The oesophagus is the only route food can take to "
                     "reach the rest of the gut at all, while bile is one "
                     "input among several rather than the route itself.",
             "correct": True},
            {"text": "The oesophagus blockage is worse only because it is "
                     "more painful than a bile duct blockage.",
             "correct": False,
             "why": "Pain is not what decides the severity here — the "
                    "oesophagus is the sole route food must travel, while "
                    "bile only feeds into that route."},
            {"text": "Both blockages are equally severe, since both stop "
                     "one form of digestion completely.", "correct": False,
             "why": "An oesophagus blockage stops the whole meal from "
                    "reaching anywhere further along, while a bile duct "
                    "blockage leaves starch and protein digestion "
                    "unaffected."},
            {"text": "A bile duct blockage is actually the more severe one, "
                     "since bile is needed for every kind of digestion, "
                     "from starch and protein through to fat, without "
                     "exception.", "correct": False,
             "why": "Bile is needed only for fat's mechanical breakdown — "
                    "starch and protein digestion carry on without it "
                    "entirely."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h20",
        "band": "harder",
        "text": "Someone has their rectum removed after illness, while the "
                "rest of their gut is left intact. Predict whether their "
                "digestion and absorption of nutrients are affected.",
        "options": [
            {"text": "It cannot be predicted without knowing how much of "
                     "the large intestine was also removed.", "correct": False,
             "why": "Digestion and absorption of nutrients do not depend on "
                    "the rectum at all — its removal alone changes only "
                    "storage and egestion."},
            {"text": "No — digestion and absorption are already complete "
                     "by the time material reaches the rectum, whose only "
                     "job is storage before egestion.", "correct": True},
            {"text": "Yes — digestion cannot finish without the rectum, "
                     "since it is where the last nutrients are absorbed.",
             "correct": False,
             "why": "Absorption is essentially finished in the small "
                    "intestine, long before material reaches the rectum — "
                    "there is nothing left there to absorb."},
            {"text": "Yes, because the rectum supplies enzymes that finish "
                     "off any remaining digestion.", "correct": False,
             "why": "No enzymes are supplied by the rectum — its role is "
                    "storing material, not digesting anything."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h21",
        "band": "harder",
        "text": "A textbook states that a meal spends exactly four hours in "
                "the stomach. Evaluate this as a precise, universal figure.",
        "options": [
            {"text": "It cannot be correct at all, since no two meals ever "
                     "take a similar amount of time.", "correct": False,
             "why": "Four hours is a genuinely useful typical figure — the "
                    "issue is treating it as an exact, universal constant "
                    "rather than a typical one."},
            {"text": "It is only wrong for very large meals, and correct "
                     "for every meal of an average size.", "correct": False,
             "why": "Meal size is only one source of variation — the "
                    "figure varies between people too, not only with meal "
                    "size."},
            {"text": "It should be read as a typical figure only — transit "
                     "times vary widely between people and between meals.",
             "correct": True},
            {"text": "It is exact and universal, since the stomach empties "
                     "at a fixed, unchanging rate for everyone, regardless "
                     "of age, meal size or health.", "correct": False,
             "why": "Transit times are described as typical figures that "
                    "vary widely between people and between meals, not fixed "
                    "constants."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h22",
        "band": "harder",
        "text": "Two people each swallow an identical vitamin tablet whole "
                "with water. One had just eaten a large meal, churning "
                "vigorously in their stomach; the other's stomach was "
                "empty. Predict which tablet is likely to break apart in "
                "the stomach sooner, and why.",
        "options": [
            {"text": "The one in the empty stomach, since there is no food "
                     "competing for the churning action.", "correct": False,
             "why": "Churning is driven by the stomach's own muscle "
                    "activity, which is greater with a full stomach working "
                    "on a meal, not less."},
            {"text": "Neither — a tablet's breakdown in the stomach depends "
                     "only on stomach acid, not on churning at all.",
             "correct": False,
             "why": "Mechanical churning is a real factor in breaking a "
                    "tablet apart, alongside the acid — it is not "
                    "irrelevant."},
            {"text": "It cannot differ, since both stomachs contain the "
                     "same acid at the same strength regardless of a "
                     "meal.", "correct": False,
             "why": "Acid strength is not the only variable — the amount of "
                    "mechanical churning genuinely differs between a full "
                    "and an empty stomach."},
            {"text": "The one in the full, churning stomach, since the "
                     "mechanical action there is far more vigorous.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h23",
        "band": "harder",
        "text": "A student argues: “If your stomach made no protease at "
                "all, you could never digest any protein, ever.” Evaluate "
                "this claim.",
        "options": [
            {"text": "It is false — the pancreas also supplies protease "
                     "into the small intestine, so protein digestion could "
                     "still happen there.", "correct": True},
            {"text": "It is true, since protease is only ever made in the "
                     "stomach.", "correct": False,
             "why": "Protease is also made in the pancreas and supplied to "
                    "the small intestine — the stomach is not its only "
                    "source."},
            {"text": "It is true, because protein can only be digested at "
                     "an acidic pH like the stomach's, since no other part "
                     "of the gut is ever acidic enough.", "correct": False,
             "why": "The pancreatic version of protease works at an "
                    "alkaline pH, in the small intestine — protein digestion "
                    "is not confined to acidic conditions."},
            {"text": "It is false, but only because protein can be absorbed "
                     "without being digested at all.", "correct": False,
             "why": "Protein molecules are too large to be absorbed "
                    "undigested — the real reason the claim fails is that "
                    "the pancreas supplies its own protease."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h24",
        "band": "harder",
        "text": "Chemical digestion of starch in the mouth takes about a "
                "minute, while chemical digestion of protein in the stomach "
                "takes about four hours. Both are described as “chemical "
                "digestion.” Explain why the same kind of process can take "
                "such different lengths of time.",
        "options": [
            {"text": "The stomach's digestion must include some mechanical "
                     "step that slows it down.", "correct": False,
             "why": "Churning does happen in the stomach, but the four-hour "
                    "figure is about how long protease takes on protein, not "
                    "about mechanical delay."},
            {"text": "Different enzymes act on different substrates under "
                     "different conditions, and nothing says every chemical "
                     "digestion step must take the same time.", "correct": True},
            {"text": "It cannot really be the same kind of process, since "
                     "the times differ so much.", "correct": False,
             "why": "Both genuinely are chemical digestion — cutting large "
                    "molecules with an enzyme. Nothing about that definition "
                    "requires a fixed time."},
            {"text": "The mouth's digestion is actually mechanical, not "
                     "chemical, which is why it is faster than any process "
                     "that needs a genuine chemical reaction to occur.",
             "correct": False,
             "why": "Amylase in saliva cuts starch molecules chemically — "
                    "that is genuinely chemical digestion, just a faster "
                    "instance of it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h25",
        "band": "harder",
        "text": "Suppose a person's liver stopped making bile entirely, but "
                "their pancreas kept supplying lipase normally. Compare this "
                "to the reverse: lipase missing but bile still made. Which "
                "failure more directly stops fat digestion, and why?",
        "options": [
            {"text": "Both failures are exactly equally direct, since fat "
                     "digestion needs both in identical measure, with "
                     "neither one ever mattering more in any circumstance.",
             "correct": False,
             "why": "They play different roles — one does the actual "
                    "chemistry, the other only speeds it up by exposing more "
                    "surface, so their loss is not equally direct."},
            {"text": "Neither failure matters much, since fat digestion can "
                     "proceed through carbohydrase instead.", "correct": False,
             "why": "Carbohydrase has no effect on lipid at all — fat "
                    "digestion depends specifically on lipase, aided by "
                    "bile."},
            {"text": "Missing lipase is more direct — it is the actual "
                     "enzyme doing the chemical breakdown, while bile only "
                     "helps by increasing surface area.", "correct": True},
            {"text": "Missing bile is more direct, since bile is the "
                     "enzyme that actually breaks lipid apart.",
             "correct": False,
             "why": "Bile is not an enzyme at all — lipase is what "
                    "chemically breaks lipid down, making its loss the more "
                    "direct failure."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h26",
        "band": "harder",
        "text": "The gall bladder is sometimes called “outside the main "
                "action” of digestion, and so is the large intestine — but "
                "for two quite different reasons. What is the difference "
                "between the two cases?",
        "options": [
            {"text": "There is no real difference, since neither organ "
                     "digests a nutrient.", "correct": False,
             "why": "One is a fact about the route food takes; the other is "
                    "about timing along that route. Those are two different "
                    "kinds of claim."},
            {"text": "The large intestine is the stronger example, since it "
                     "contributes less to digestion than the gall bladder "
                     "does, given how little chemistry is left by the time "
                     "material gets there.", "correct": False,
             "why": "The gall bladder is not on the food's route at all, "
                    "which is a stronger sense of “outside” than simply "
                    "arriving late to a route you are on."},
            {"text": "Neither is really “outside the main action,” since "
                     "the whole system depends on both of them.",
             "correct": False,
             "why": "Being necessary to the system does not stop an organ "
                    "being outside the main chemical action, and these two "
                    "are outside it in their own distinct ways."},
            {"text": "The gall bladder sits off the route food takes "
                     "altogether, while the large intestine is on that "
                     "route but receives material only once the main "
                     "chemistry is done.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h27",
        "band": "harder",
        "text": "Suppose someone's entire small intestine had to be removed, "
                "leaving the rest of the gut intact and reconnected. Would "
                "the large intestine be able to take over its absorbing job?",
        "options": [
            {"text": "No — the large intestine's role is absorbing water "
                     "from what remains after digestion, not absorbing the "
                     "products of digestion themselves.", "correct": True},
            {"text": "Yes — the large intestine already absorbs nutrients, "
                     "so it could simply absorb more of them.", "correct": False,
             "why": "The large intestine absorbs water, some minerals and "
                    "some vitamins — by the time material reaches it, the "
                    "main nutrients are normally already gone."},
            {"text": "Yes, because the large intestine is wider and could "
                     "hold more material for absorption.", "correct": False,
             "why": "Being wider affects how much it can hold, not what "
                    "kind of absorption it is built to carry out."},
            {"text": "It cannot be answered, since the large intestine's "
                     "absorbing ability has never actually been "
                     "described.", "correct": False,
             "why": "Its absorbing role is described clearly — water, some "
                    "minerals and some vitamins — which is a different job "
                    "from absorbing digested nutrients."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h28",
        "band": "harder",
        "text": "A small pebble is accidentally swallowed with a meal, "
                "travels the length of the gut unchanged, and leaves through "
                "the anus a few days later. Using the terms correctly, "
                "describe what has and has not happened to it.",
        "options": [
            {"text": "None of the three terms apply, since a pebble is not "
                     "food.", "correct": False,
             "why": "The terms describe what happens on the journey through "
                    "the gut, not only to food — the pebble is neither "
                    "digested nor absorbed, and leaves by egestion."},
            {"text": "It was never digested or absorbed, and its "
                     "eventual removal is egestion rather than excretion.",
             "correct": True},
            {"text": "It was digested but never absorbed, and its removal "
                     "counts as excretion, in the same way urea leaving the "
                     "kidneys does.", "correct": False,
             "why": "Digestion means an enzyme chemically breaking a "
                    "molecule down — nothing of the kind happens to a "
                    "pebble."},
            {"text": "It was absorbed but never digested, and its removal "
                     "counts as egestion.", "correct": False,
             "why": "Absorption means crossing the gut wall into the blood "
                    "— the pebble never does that, so it was not absorbed "
                    "either."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h29",
        "band": "harder",
        "text": "A student argues: “Peristalsis pushes food along the whole "
                "gut, so food must move at a constant speed from mouth to "
                "anus.” Evaluate this claim using the transit times given "
                "for each organ.",
        "options": [
            {"text": "It is true only for the small intestine and large "
                     "intestine, but false everywhere else.", "correct": False,
             "why": "Even between those two organs the times differ "
                    "considerably — roughly sixteen hours against twelve to "
                    "thirty."},
            {"text": "It cannot be evaluated, since transit times were "
                     "never actually measured for each organ.", "correct": False,
             "why": "Typical transit times are given for every stop, from "
                    "about a minute in the mouth to many hours in the large "
                    "intestine — they clearly are not constant."},
            {"text": "It is false — transit times differ hugely between "
                     "organs, from about eight seconds in the oesophagus to "
                     "many hours in the large intestine.", "correct": True},
            {"text": "It is true, since peristalsis is the same muscular "
                     "action the whole length of the gut.", "correct": False,
             "why": "The mechanism being the same does not mean the speed "
                    "is — the stomach and large intestine hold material far "
                    "longer than the oesophagus does."},
        ],
        "figure": None,
    },
    {
        "id": "b3-05-h30",
        "band": "harder",
        "text": "A student says the pancreas must be a fairly inactive "
                "organ, since a meal never passes through it. Evaluate "
                "this claim.",
        "options": [
            {"text": "It is true, since an organ counts as active only if "
                     "food physically passes through it.", "correct": False,
             "why": "Activity is not decided by the route food takes. The "
                    "pancreas is constantly producing and releasing "
                    "secretions into the small intestine."},
            {"text": "It is false, but only because a small amount of food "
                     "does pass through the pancreas after a large meal.",
             "correct": False,
             "why": "No food enters the pancreas at any point. It is active "
                    "because of what it produces, not because anything "
                    "passes through it."},
            {"text": "It is true of the pancreas but false of the liver, "
                     "since only the liver actually produces anything.",
             "correct": False,
             "why": "Both organs produce continuously — the pancreas "
                    "supplies enzymes and an alkali, the liver supplies "
                    "bile. Neither of them is idle."},
            {"text": "It is false — the pancreas works continuously, "
                     "producing both digestive enzymes and the alkali that "
                     "neutralises stomach acid.", "correct": True},
        ],
        "figure": None,
    },
]
