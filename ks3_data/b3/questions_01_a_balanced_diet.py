# -*- coding: utf-8 -*-
"""B3 lesson 01 — A balanced diet: twelve questions (MRB-269).

The lesson makes one argument: balanced means seven separate targets met at
once, and those targets run from about 2000 g of water down to about 50 mg of
vitamin C. Every question here probes some part of that — the seven jobs, the
seven deficiencies, the four amount bands at the bench, the two plates in the
hook, and Takaki's barley ship in the stretch note.

The distractors are built from the lesson's three declared misconceptions.
DIET-01 ("a balanced diet means equal amounts of each food group") supplies the
options that keep the seven similar — "only water is unusual", "the amounts only
need to differ over a week", "equal if you count energy rather than mass".
DIET-02 ("vitamins give you energy") supplies the options that credit vitamins
with fuel — B1 as "the one vitamin that does carry energy", vitamins releasing
energy "only in milligram amounts", fibre being "respired slowly". DIET-03
("fat is bad for you, so a healthy diet has none in it") supplies the options
that treat lipid as optional or as harm rather than as quantity. Three further
errors the lesson's own table exists to correct are worked as well: that any
mineral shortage gives anaemia, that a nutrient you never absorb cannot matter,
and that protein is never respired.

No question restates a ladder rung. The rungs already own the three
energy-releasing nutrients, the tired student who is short of iron, the
300 g / 14 mg explanation and the sports-drink claim, so the bank works around
all four: iron and anaemia appear only as distractors, the vitamin-energy idea
is taken through vitamin B1 and a mechanism rather than through an advert, and
the two-ends argument is put to the student as the two plates instead of as two
numbers.

`figure` is `None` throughout — the lesson declares no figures, and every stem
here is self-contained.
"""

UNIT = "B3"
LESSON = "a-balanced-diet"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-01-e01",
        "band": "easier",
        "text": "Which nutrient does the body break down into amino acids and "
                "rebuild into muscle, enzymes and antibodies?",
        "options": [
            {"text": "Carbohydrate", "correct": False,
             "why": "Carbohydrate is broken down to glucose and respired for "
                    "energy. It supplies no amino acids at all."},
            {"text": "Lipid", "correct": False,
             "why": "Lipid is an energy store, an insulator and the material "
                    "of every cell membrane. It is not broken into amino "
                    "acids."},
            {"text": "Protein", "correct": True},
            {"text": "Minerals", "correct": False,
             "why": "Minerals are elements built into structures and carriers "
                    "— calcium into bone, iron into haemoglobin. They are not "
                    "broken down into anything."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e02",
        "band": "easier",
        "text": "At the bench you set the amounts a 13-year-old needs in one "
                "day. Which of the seven has by far the biggest requirement?",
        "options": [
            {"text": "Water — about 2000 g a day", "correct": True},
            {"text": "Carbohydrate — about 300 g a day", "correct": False,
             "why": "300 g is the biggest of the solid foods, which is why it "
                    "feels like the answer. It is still under a sixth of the "
                    "water, which is about 2000 g."},
            {"text": "Lipid — about 70 g a day", "correct": False,
             "why": "Lipid is tens of grams, not hundreds. It carries more "
                    "than twice the energy per gram of carbohydrate, so a "
                    "small mass goes a long way."},
            {"text": "Protein — about 45 g a day", "correct": False,
             "why": "Protein is tens of grams. A growing 13-year-old needs a "
                    "steady supply of it rather than a large one."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e03",
        "band": "easier",
        "text": "Someone's diet is short of calcium for a long time. What is "
                "most likely to follow?",
        "options": [
            {"text": "Anaemia — the blood cannot carry oxygen properly",
             "correct": False,
             "why": "That is what going short of iron does. Iron is built "
                    "into haemoglobin; calcium is built into bone."},
            {"text": "Goitre — a swelling in the neck", "correct": False,
             "why": "Goitre follows a shortage of iodine, the mineral built "
                    "into thyroid hormone. Every mineral has its own job and "
                    "its own deficiency."},
            {"text": "Constipation, because the gut slows down",
             "correct": False,
             "why": "That follows a shortage of dietary fibre, not of a "
                    "mineral. Calcium is the one built into bone."},
            {"text": "Weak bones, because calcium is built into bone",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e04",
        "band": "easier",
        "text": "Dietary fibre counts as one of the seven nutrients even "
                "though your body never digests or absorbs it. What is it "
                "doing?",
        "options": [
            {"text": "It is respired slowly, releasing energy over a long "
                     "period.", "correct": False,
             "why": "Fibre is never respired. Only carbohydrate, lipid and "
                    "protein release energy, and fibre is not even digested."},
            {"text": "It adds bulk for the gut muscles to grip and push "
                     "against.", "correct": True},
            {"text": "It coats the gut wall and stops harmful bacteria "
                     "getting in.", "correct": False,
             "why": "Fibre does nothing of the kind. It adds bulk, and the "
                    "gut muscles need bulk to have something to push."},
            {"text": "It soaks up water, so the body loses less of it each "
                     "day.", "correct": False,
             "why": "Water is a nutrient in its own right, at about 2000 g a "
                    "day. Fibre's job is bulk for the gut muscles to push."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-01-s01",
        "band": "standard",
        "text": "At the bench a student puts all seven nutrients in the same "
                "band, because to them balanced means equal amounts. Which "
                "reply puts them right?",
        "options": [
            {"text": "They are nearly right — only water is unusual, and the "
                     "other six really are similar.", "correct": False,
             "why": "Water is not the only outlier. Carbohydrate is about "
                    "300 g, protein about 45 g and all thirteen vitamins "
                    "about 0.2 g — the seven are spread across four bands."},
            {"text": "They are right for one day, and the amounts only need "
                     "to differ across a week.", "correct": False,
             "why": "These are daily targets. A 13-year-old needs about "
                    "2000 g of water and about 0.2 g of vitamins on the same "
                    "day, not in different weeks."},
            {"text": "Balanced means seven separate targets, of very "
                     "different sizes, all met at once.",
             "correct": True},
            {"text": "Balanced does mean equal amounts, as long as you count "
                     "energy rather than mass.", "correct": False,
             "why": "No measure makes them equal. Fibre, water, vitamins and "
                    "minerals release no energy at all, so counting energy "
                    "makes the spread worse rather than better."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s02",
        "band": "standard",
        "text": "Someone eating plenty of bread and rice is exhausted, and a "
                "doctor finds they are short of vitamin B1. Their friend says "
                "this proves vitamins give you energy. Why is the friend "
                "wrong?",
        "options": [
            {"text": "B1 releases no energy itself — it is part of the "
                     "machinery that gets glucose into respiration.",
             "correct": True},
            {"text": "B1 is the one vitamin that does carry energy, so the "
                     "friend is right about that one.", "correct": False,
             "why": "No vitamin carries energy, B1 included. Its energy "
                    "content is zero. What B1 does is let the glucose already "
                    "in the diet be respired."},
            {"text": "The tiredness comes from eating too little "
                     "carbohydrate, so the B1 is beside the point.",
             "correct": False,
             "why": "They are eating plenty of bread and rice. The fuel is "
                    "there — what is missing is what lets the body use it."},
            {"text": "Vitamins do release energy, but only in milligram "
                     "amounts, so the effect is small.", "correct": False,
             "why": "The energy content of a vitamin is zero, not small. The "
                    "amount is not what settles this."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s03",
        "band": "standard",
        "text": "Lipid carries more than twice the energy per gram that "
                "carbohydrate does. Which conclusion actually follows from "
                "that?",
        "options": [
            {"text": "So lipid is harmful, and a healthy diet keeps it as "
                     "close to zero as it can.", "correct": False,
             "why": "That turns a statement about quantity into one about "
                    "harm. Lipid builds every cell membrane and is the only "
                    "way vitamins A, D, E and K are absorbed."},
            {"text": "So the body respires lipid before it respires "
                     "carbohydrate.", "correct": False,
             "why": "Carbohydrate is the store the body reaches for first. "
                    "Energy per gram says nothing about the order fuels are "
                    "used in."},
            {"text": "So a 13-year-old needs more than twice as much lipid as "
                     "carbohydrate.", "correct": False,
             "why": "The opposite: about 70 g of lipid against about 300 g of "
                    "carbohydrate. More energy per gram means less mass is "
                    "needed."},
            {"text": "So a small mass of lipid brings in a lot of energy, and "
                     "is easy to overeat.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s04",
        "band": "standard",
        "text": "Plate A — rice, chicken, oil, water and salt in roughly the "
                "right amounts — kills in about four months. Plate B is the "
                "same food plus one orange, and does not. What does the pair "
                "show?",
        "options": [
            {"text": "Plate A must be short of energy too, because no diet "
                     "that kills in four months is meeting its needs.",
             "correct": False,
             "why": "Plate A has carbohydrate, lipid and protein in roughly "
                    "the right amounts, so the energy is there. What is "
                    "missing weighs about 50 mg."},
            {"text": "A nutrient needed in milligrams is as essential as one "
                     "needed in hundreds of grams.",
             "correct": True},
            {"text": "Fresh food is always healthier than cooked food, "
                     "whatever nutrients it holds.", "correct": False,
             "why": "Nothing here turns on fresh against cooked. The orange "
                    "supplies about 50 mg of vitamin C, and that one "
                    "substance is the whole difference."},
            {"text": "The five nutrients on Plate A cannot really have been "
                     "in the right amounts.", "correct": False,
             "why": "They were. Getting five of the seven right is not "
                    "enough — leave one out and the diet fails, however good "
                    "the rest of it is."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-01-h01",
        "band": "harder",
        "text": "A meal-replacement bar lists per bar: carbohydrate 40 g, "
                "protein 12 g, fat 9 g, fibre 0 g, plus all thirteen vitamins "
                "and every mineral. Someone lives on these bars and plenty of "
                "water for a month. Which problem shows up?",
        "options": [
            {"text": "Scurvy — bleeding gums and wounds that heal slowly",
             "correct": False,
             "why": "Scurvy is a shortage of vitamin C, and the label says "
                    "all thirteen vitamins are there. Look for the row that "
                    "reads zero."},
            {"text": "Anaemia — the blood cannot carry oxygen properly",
             "correct": False,
             "why": "Anaemia is a shortage of iron, and the label says every "
                    "mineral is there. The nutrient reading zero is dietary "
                    "fibre."},
            {"text": "Nothing — every nutrient a body needs is on that label",
             "correct": False,
             "why": "Read it again: fibre is 0 g, and fibre is one of the "
                    "seven. A nutrient you never absorb is still a nutrient "
                    "you cannot do without."},
            {"text": "Constipation — the gut muscles have nothing to push "
                     "against", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h02",
        "band": "harder",
        "text": "A slimming plan takes all the lipid out of a diet and "
                "replaces it with the same mass of carbohydrate, claiming "
                "nothing is lost but energy. What is the strongest objection?",
        "options": [
            {"text": "Vitamins A, D, E and K dissolve only in fat, so with no "
                     "lipid they cannot be absorbed at all.", "correct": True},
            {"text": "Carbohydrate carries more energy per gram than lipid, "
                     "so the plan adds energy instead.", "correct": False,
             "why": "It is the other way round — lipid carries more than "
                    "twice the energy per gram. Swapping equal masses lowers "
                    "the energy, which is the one thing the plan got right."},
            {"text": "There is no objection: lipid is the one nutrient a "
                     "healthy diet can do without.", "correct": False,
             "why": "None of the seven is optional. Lipid builds every cell "
                    "membrane you have and carries four of the vitamins into "
                    "you."},
            {"text": "The body cannot respire carbohydrate at all unless some "
                     "lipid is present too.", "correct": False,
             "why": "Carbohydrate is respired on its own, and it is the fuel "
                    "the body reaches for first. The problem is everything "
                    "lipid does apart from fuel."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h03",
        "band": "harder",
        "text": "In the 1880s Takaki added barley and vegetables to one navy "
                "ship's rations and beriberi almost vanished — forty years "
                "before vitamin B1 was identified. What did that result "
                "establish?",
        "options": [
            {"text": "That beriberi is an infection, and something in barley "
                     "kills what causes it.", "correct": False,
             "why": "Everyone at the time assumed it was an infection, and "
                    "that is the assumption his result overturned. The cause "
                    "was something missing from the food."},
            {"text": "That the barley crew stayed well because they were "
                     "simply eating more food.", "correct": False,
             "why": "More of the same ration would not have helped — polished "
                    "rice was not short of energy. What changed was what the "
                    "food contained, not how much there was."},
            {"text": "That something in barley, absent from polished rice, "
                     "prevented the disease.",
             "correct": True},
            {"text": "That vitamin B1 prevents beriberi, which is why he "
                     "added the barley.", "correct": False,
             "why": "He could not have known that: B1 was not identified for "
                    "another forty years. He was right about the fix while "
                    "being wrong about the mechanism."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h04",
        "band": "harder",
        "text": "Someone eats almost no carbohydrate but plenty of protein. "
                "After several weeks they have lost muscle. What has "
                "happened?",
        "options": [
            {"text": "Muscle can only be built while carbohydrate is present, "
                     "so none was built.", "correct": False,
             "why": "Protein is what muscle is built from, and there was "
                    "plenty of it. The question is what the body did with it "
                    "instead."},
            {"text": "With no carbohydrate, the body respired its own fat, "
                     "then its own protein.",
             "correct": True},
            {"text": "Protein cannot be respired, so the extra protein was "
                     "passed out as waste.", "correct": False,
             "why": "Protein can be respired. The body prefers to use it for "
                    "growth and repair, and falls back on burning it when the "
                    "other fuels run short."},
            {"text": "Protein cannot be absorbed unless carbohydrate is eaten "
                     "at the same time.", "correct": False,
             "why": "Nothing stops protein being absorbed on its own. What "
                    "was missing was fuel, so the protein ended up being used "
                    "as fuel."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # Nine further rows, three per band, appended at bank_position 12+ so the
    # original twelve remain the auto-composition window.

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b3-01-e05",
        "band": "easier",
        "text": "Which nutrient is broken down to glucose and respired first "
                "for energy?",
        "options": [
            {"text": "Lipid", "correct": False,
             "why": "Lipid is an energy store, and the body does respire it — "
                    "but only once carbohydrate has run short. Carbohydrate "
                    "is the one it reaches for first."},
            {"text": "Protein", "correct": False,
             "why": "Protein is for growth and repair. The body falls back on "
                    "burning it when the other fuels run out, which is not the "
                    "same as reaching for it first."},
            {"text": "Carbohydrate", "correct": True},
            {"text": "Vitamins", "correct": False,
             "why": "Vitamins release no energy at all. They let the reactions "
                    "that do release energy actually run, which is a different "
                    "job."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e06",
        "band": "easier",
        "text": "For four months a sailor eats salted meat, ship's biscuit and "
                "water — plenty of energy, and no fruit or vegetables at all. "
                "Which deficiency disease follows?",
        "options": [
            {"text": "Scurvy, because the diet supplies no vitamin C",
             "correct": True},
            {"text": "Rickets, because the diet supplies no vitamin D",
             "correct": False,
             "why": "Rickets follows a shortage of vitamin D, which comes from "
                    "oily fish or from sunlight on skin rather than from fruit "
                    "and vegetables."},
            {"text": "Anaemia, because the diet supplies no iron",
             "correct": False,
             "why": "Anaemia follows a shortage of iron, and salted meat "
                    "supplies iron. The nutrient this diet has none of is "
                    "vitamin C."},
            {"text": "Goitre, because the diet supplies no iodine",
             "correct": False,
             "why": "Goitre follows a shortage of iodine, the mineral built "
                    "into thyroid hormone. Every deficiency has its own "
                    "missing nutrient, and this one is vitamin C."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e07",
        "band": "easier",
        "text": "Apart from being an energy store, what else does lipid do in "
                "the body?",
        "options": [
            {"text": "It is broken into amino acids and rebuilt into muscle "
                     "and enzymes.", "correct": False,
             "why": "That is protein's job. Lipid supplies no amino acids at "
                    "all, so nothing can be rebuilt from it."},
            {"text": "It adds bulk so the gut muscles have something to push "
                     "against.", "correct": False,
             "why": "That is dietary fibre, which is never digested and never "
                    "absorbed. Lipid is digested and absorbed."},
            {"text": "It is built into bone and into haemoglobin as the body "
                     "needs it.", "correct": False,
             "why": "Those are minerals — calcium into bone, iron into "
                    "haemoglobin. Lipid is built into neither."},
            {"text": "It builds every cell membrane, and it insulates the "
                     "body.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b3-01-s05",
        "band": "standard",
        "text": "Someone eats plenty of every nutrient except fibre and is "
                "constipated. They decide to drink more water rather than "
                "change what they eat. Will that fix it?",
        "options": [
            {"text": "Yes — water and fibre do the same job, and water is the "
                     "easier of the two to get.", "correct": False,
             "why": "They do different jobs. Water is the solvent every "
                    "reaction happens in; fibre is bulk for the gut muscles to "
                    "grip and push."},
            {"text": "No — the gut muscles need bulk to push against, and "
                     "water is not bulk.", "correct": True},
            {"text": "Yes, because fibre works only by soaking up the water "
                     "you drink alongside it.", "correct": False,
             "why": "Fibre is not a sponge. It is plant material your body "
                    "never digests, and its job is to give the gut muscles "
                    "something solid to move."},
            {"text": "No — the real problem is a shortage of minerals, which "
                     "water cannot supply either.", "correct": False,
             "why": "Nothing here points at minerals. Constipation is what "
                    "follows a shortage of dietary fibre, and no other "
                    "nutrient stands in for it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s06",
        "band": "standard",
        "text": "A teenager's day supplies about 300 g of carbohydrate, 70 g "
                "of lipid, 45 g of protein, 25 g of fibre, 2000 g of water and "
                "all thirteen vitamins. They eat no dairy, no red meat and no "
                "leafy greens. Which of the seven is at risk?",
        "options": [
            {"text": "Protein, because dairy and red meat are the only "
                     "sources of it.", "correct": False,
             "why": "Protein is at 45 g, which is the target, and eggs, fish, "
                    "beans and lentils all supply it. Dairy and meat are not "
                    "the only sources."},
            {"text": "None — six of the seven are met, and six out of seven "
                     "is balanced enough.", "correct": False,
             "why": "Leave one of the seven out and the diet fails, however "
                    "good the rest of it is. Six targets met is still a diet "
                    "with one target missed."},
            {"text": "Vitamins, because they come mainly from dairy and "
                     "liver.", "correct": False,
             "why": "The day supplies all thirteen vitamins, and fruit and "
                    "vegetables supply most of them in any case."},
            {"text": "Minerals — dairy, red meat and leafy greens are where "
                     "most of them come from.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s07",
        "band": "standard",
        "text": "Breakfast A is white toast and jam. Breakfast B is wholegrain "
                "toast, a boiled egg and an orange. Both supply about the same "
                "energy. Using the seven nutrients, why is B the "
                "better-balanced meal?",
        "options": [
            {"text": "Because A supplies far too much energy, and B supplies "
                     "the right amount.", "correct": False,
             "why": "Both supply about the same energy — that is stated. What "
                    "separates them is which of the seven turn up, not how "
                    "much energy does."},
            {"text": "Because B contains no fat, and a healthy diet keeps fat "
                     "as low as it can.", "correct": False,
             "why": "An egg contains lipid, and lipid is one of the seven. A "
                    "meal is not improved by removing one of the targets it "
                    "has to meet."},
            {"text": "Because B adds protein, fibre and vitamin C for the "
                     "same energy.", "correct": True},
            {"text": "Because A is unbalanced — a balanced meal holds equal "
                     "amounts of each nutrient.", "correct": False,
             "why": "Balanced never means equal amounts. A 13-year-old needs "
                    "about 2000 g of water and about 0.2 g of vitamins on the "
                    "same day."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b3-01-h05",
        "band": "harder",
        "text": "A tablet supplies all thirteen vitamins and every mineral, in "
                "the amounts a 13-year-old needs in a day. An advert says one "
                "tablet can replace a meal. What is the strongest objection?",
        "options": [
            {"text": "Vitamins and minerals can only be absorbed from food, "
                     "never from a tablet.", "correct": False,
             "why": "There is nothing wrong with absorbing them from a "
                    "tablet. The objection is about the nutrients the tablet "
                    "contains none of."},
            {"text": "It supplies none of the other five nutrients, including "
                     "all of the energy.", "correct": True},
            {"text": "It supplies too much of the two it does contain, so it "
                     "would do harm.", "correct": False,
             "why": "It supplies the amounts a 13-year-old needs — that is "
                    "stated. The problem is the five nutrients it supplies "
                    "nothing of."},
            {"text": "There is no objection — vitamins and minerals are the "
                     "two that matter most.", "correct": False,
             "why": "None of the seven is optional, and vitamins and minerals "
                    "release no energy at all. A day of tablets supplies no "
                    "fuel, no building material, no bulk and no water."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h06",
        "band": "harder",
        "text": "A child's diet supplies plenty of energy from cassava, which "
                "is almost entirely carbohydrate, and very little protein. The "
                "child stops growing. Why does more cassava not fix it?",
        "options": [
            {"text": "Protein is the only nutrient that supplies the nitrogen "
                     "for building tissue.", "correct": True},
            {"text": "Cassava is not digested, so almost nothing it holds "
                     "ever reaches the child.", "correct": False,
             "why": "Cassava is carbohydrate and is digested and absorbed "
                    "normally. The energy is arriving; the building material "
                    "is not."},
            {"text": "The child is still short of energy, and growth will "
                     "restart once intake rises.", "correct": False,
             "why": "Energy is already plentiful. More of a nutrient the "
                    "child is not short of changes nothing about the one they "
                    "are."},
            {"text": "Carbohydrate can be rebuilt into muscle once enough of "
                     "it has been eaten.", "correct": False,
             "why": "It cannot. Carbohydrate is broken to glucose and "
                    "respired; only protein supplies the amino acids muscle is "
                    "built from."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h07",
        "band": "harder",
        "text": "Going without water kills in days. Going without vitamin C "
                "takes about four months. Both are essential. Why does one "
                "failure show so much faster than the other?",
        "options": [
            {"text": "Vitamin C is not truly essential, since the body "
                     "manages without it for months.", "correct": False,
             "why": "It is essential. Four months without it is fatal, and a "
                    "diet that is right in every other way does not save "
                    "you."},
            {"text": "Water is essential and vitamin C is merely useful, "
                     "which is why one kills faster.", "correct": False,
             "why": "Both are on the list of seven and neither is optional. "
                    "How fast a shortage shows is not a measure of how "
                    "important the nutrient is."},
            {"text": "Every reaction in the body happens in water, so the "
                     "failure starts within hours.", "correct": True},
            {"text": "Vitamin C is needed in milligrams, and a nutrient "
                     "needed in milligrams matters less.", "correct": False,
             "why": "Amount is not what decides it. About 50 mg of vitamin C "
                    "is as essential as about 2000 g of water, and going "
                    "without either one is fatal."},
        ],
        "figure": None,
    },
]
