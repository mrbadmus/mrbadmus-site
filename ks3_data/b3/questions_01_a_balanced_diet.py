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

    # ── easier · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b3-01-e08",
        "band": "easier",
        "text": "Which mineral does the body build into haemoglobin, so that "
                "blood can carry oxygen?",
        "options": [
            {"text": "Iron", "correct": True},
            {"text": "Calcium", "correct": False,
             "why": "Calcium is built into bone. A shortage weakens the "
                    "skeleton; it does not stop blood carrying oxygen."},
            {"text": "Iodine", "correct": False,
             "why": "Iodine is built into thyroid hormone. There is no iodine "
                    "in haemoglobin."},
            {"text": "Sodium", "correct": False,
             "why": "Sodium is a mineral the body uses in its fluids, and it "
                    "is not part of the haemoglobin molecule."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e09",
        "band": "easier",
        "text": "Which mineral does the body build into thyroid hormone?",
        "options": [
            {"text": "Calcium", "correct": False,
             "why": "Calcium goes into bone. A thyroid gland cannot make its "
                    "hormone out of calcium."},
            {"text": "Iodine", "correct": True},
            {"text": "Iron", "correct": False,
             "why": "Iron goes into haemoglobin, which is what lets blood "
                    "carry oxygen round the body."},
            {"text": "Potassium", "correct": False,
             "why": "Potassium is used in the body's fluids and cells, and a "
                    "diet full of it still gives goitre without iodine."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e10",
        "band": "easier",
        "text": "A long shortage of which vitamin causes rickets?",
        "options": [
            {"text": "Vitamin C", "correct": False,
             "why": "A long shortage of vitamin C causes scurvy, which "
                    "damages the protein holding the body together."},
            {"text": "Vitamin B1", "correct": False,
             "why": "A long shortage of vitamin B1 causes beriberi — "
                    "weakness, swelling and heart failure."},
            {"text": "Vitamin D", "correct": True},
            {"text": "Vitamin A", "correct": False,
             "why": "Vitamin A dissolves in fat as vitamin D does, but its "
                    "shortage does not leave bone soft and bent."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e11",
        "band": "easier",
        "text": "Beriberi — weakness, swelling and heart failure — follows a "
                "long shortage of which vitamin?",
        "options": [
            {"text": "Vitamin D", "correct": False,
             "why": "Going short of vitamin D causes rickets, where growing "
                    "bone is laid down soft."},
            {"text": "Vitamin C", "correct": False,
             "why": "Going short of vitamin C causes scurvy, and about 50 mg "
                    "a day is enough to prevent it."},
            {"text": "Vitamin K", "correct": False,
             "why": "Vitamin K is one of the four that dissolve in fat, and "
                    "beriberi is not what its shortage causes."},
            {"text": "Vitamin B1", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e12",
        "band": "easier",
        "text": "How many different vitamins does a person need in their diet?",
        "options": [
            {"text": "Thirteen", "correct": True},
            {"text": "Seven", "correct": False,
             "why": "Seven is the number of nutrient groups. Vitamins are one "
                    "of those groups, and there are thirteen inside it."},
            {"text": "Four", "correct": False,
             "why": "Four is the number that dissolve in fat — A, D, E and K. "
                    "There are nine more besides those."},
            {"text": "Three", "correct": False,
             "why": "Three is the number of nutrients that release energy, "
                    "and no vitamin is one of them."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e13",
        "band": "easier",
        "text": "Wholegrains, pulses and vegetable skins are eaten mainly for "
                "which nutrient?",
        "options": [
            {"text": "Protein", "correct": False,
             "why": "Meat, fish, eggs, beans and lentils are the protein "
                    "foods; skins supply very little of it."},
            {"text": "Dietary fibre", "correct": True},
            {"text": "Lipid (fat and oil)", "correct": False,
             "why": "Oils, butter, nuts and oily fish are the lipid foods, "
                    "and wholegrains carry very little fat."},
            {"text": "Vitamins", "correct": False,
             "why": "Fruit, vegetables, dairy and liver are the usual vitamin "
                    "sources, and skins are eaten for their bulk."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e14",
        "band": "easier",
        "text": "Roughly how much vitamin C does a person need in a day?",
        "options": [
            {"text": "About 14 mg", "correct": False,
             "why": "About 14 mg is the daily iron figure. Iron is a mineral, "
                    "and it does nothing that vitamin C does."},
            {"text": "About 5 g", "correct": False,
             "why": "About 5 g is the whole daily mineral total. No single "
                    "vitamin is needed in grams."},
            {"text": "About 0.2 g", "correct": False,
             "why": "About 0.2 g covers all thirteen vitamins together, so "
                    "one vitamin on its own is a fraction of it."},
            {"text": "About 50 mg", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e15",
        "band": "easier",
        "text": "Water is one of the seven nutrients. What is the body using "
                "it for?",
        "options": [
            {"text": "As the liquid that every reaction in the body happens "
                     "in, and that blood and urine are carried in.",
             "correct": True},
            {"text": "As a fuel it respires whenever the food supply runs "
                     "short and the carbohydrate has all gone.",
             "correct": False,
             "why": "Water releases no energy however short of food someone "
                    "is. Only carbohydrate, lipid and protein do."},
            {"text": "As the material it builds bone and haemoglobin from, "
                     "using the calcium and iron dissolved in it.",
             "correct": False,
             "why": "Bone and haemoglobin are built from minerals. Water is "
                    "the solvent they travel in, not the structure."},
            {"text": "As bulk for the gut muscles to grip, which is what "
                     "keeps food moving along.", "correct": False,
             "why": "That is dietary fibre's job. Water has no bulk of its "
                    "own for a muscle to push against."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e16",
        "band": "easier",
        "text": "How many nutrient groups does a healthy diet have to contain?",
        "options": [
            {"text": "Three", "correct": False,
             "why": "Three release energy, but the other four are needed just "
                    "as absolutely and none of them is optional."},
            {"text": "Five", "correct": False,
             "why": "Leaving out fibre and water gives five, and going "
                    "without either of those makes a person ill."},
            {"text": "Seven", "correct": True},
            {"text": "Thirteen", "correct": False,
             "why": "Thirteen is the number of vitamins, and all thirteen sit "
                    "inside one of the groups."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e17",
        "band": "easier",
        "text": "In this topic, what does the word deficiency mean?",
        "options": [
            {"text": "Eating far more of a nutrient than the body has any "
                     "use for, and for far too long.", "correct": False,
             "why": "That is an excess. A deficiency is the shortage, and it "
                    "is the shortage that carries a named illness."},
            {"text": "Going short of one nutrient, and the illness that "
                     "follows from it.", "correct": True},
            {"text": "Taking in too little energy to get through a day.",
             "correct": False,
             "why": "That is a shortage of fuel, and a deficiency can happen "
                    "in a diet carrying plenty of energy."},
            {"text": "Eating food that has gone off and made someone ill.",
             "correct": False,
             "why": "That is food poisoning, which comes from what is in the "
                    "food rather than from what is missing."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e18",
        "band": "easier",
        "text": "A child's growth stops and their wounds heal slowly. Which "
                "nutrient is their diet short of?",
        "options": [
            {"text": "Water", "correct": False,
             "why": "A water shortage shows within hours, in temperature "
                    "control and concentration, not as slow growth."},
            {"text": "Dietary fibre", "correct": False,
             "why": "Going short of fibre causes constipation. Fibre is never "
                    "absorbed, so it builds no tissue."},
            {"text": "Protein", "correct": True},
            {"text": "Carbohydrate", "correct": False,
             "why": "A carbohydrate shortage makes a person tired, and the "
                    "body then starts burning its own fat for fuel."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e19",
        "band": "easier",
        "text": "Vitamins A, D, E and K can only be absorbed when one other "
                "nutrient is in the meal. Which one?",
        "options": [
            {"text": "Lipid", "correct": True},
            {"text": "Protein", "correct": False,
             "why": "Protein supplies amino acids for building tissue, and "
                    "these four vitamins do not dissolve in it."},
            {"text": "Dietary fibre", "correct": False,
             "why": "Fibre is not absorbed itself, so it cannot carry "
                    "anything else into the body with it."},
            {"text": "Carbohydrate", "correct": False,
             "why": "Carbohydrate is broken to glucose and respired, and "
                    "these four vitamins do not dissolve in it."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e20",
        "band": "easier",
        "text": "Roughly how much protein does a 13-year-old need in a day?",
        "options": [
            {"text": "About 300 g", "correct": False,
             "why": "About 300 g is the carbohydrate figure — the bulk of the "
                    "plate, and nearly seven times the protein."},
            {"text": "About 2000 g", "correct": False,
             "why": "About 2000 g is the water figure, which is by far the "
                    "largest requirement of the seven."},
            {"text": "About 0.2 g", "correct": False,
             "why": "About 0.2 g covers all thirteen vitamins together, not "
                    "the protein a growing body needs."},
            {"text": "About 45 g", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e21",
        "band": "easier",
        "text": "A teenager's food for one day should contain about how much "
                "dietary fibre?",
        "options": [
            {"text": "About 5 g", "correct": False,
             "why": "About 5 g is the figure for all the minerals together, "
                    "and fibre is needed in five times that mass."},
            {"text": "About 25 g", "correct": True},
            {"text": "About 0 g", "correct": False,
             "why": "Fibre is not absorbed and is still needed in tens of "
                    "grams, which is the surprising part of it."},
            {"text": "About 300 g", "correct": False,
             "why": "About 300 g is the carbohydrate figure. Fibre sits in "
                    "the tens of grams, with lipid and protein."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e22",
        "band": "easier",
        "text": "Oils, butter, nuts and oily fish are eaten mainly for which "
                "nutrient?",
        "options": [
            {"text": "Carbohydrate", "correct": False,
             "why": "Bread, rice, pasta and potato are the carbohydrate "
                    "foods, and oil contains no starch or sugar."},
            {"text": "Minerals", "correct": False,
             "why": "Dairy, red meat, leafy greens and salt are where most of "
                    "the minerals in a diet come from."},
            {"text": "Lipid", "correct": True},
            {"text": "Dietary fibre", "correct": False,
             "why": "Wholegrains, pulses and skins supply fibre, and butter "
                    "has no plant bulk in it at all."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e23",
        "band": "easier",
        "text": "Which nutrient group is made of elements the body builds "
                "into structures and carriers, such as bone and haemoglobin?",
        "options": [
            {"text": "Vitamins", "correct": False,
             "why": "Vitamins are small molecules that make particular "
                    "reactions possible; they are not built into bone."},
            {"text": "Dietary fibre", "correct": False,
             "why": "Fibre is plant material that is never absorbed, so it "
                    "cannot become part of any structure."},
            {"text": "Lipid", "correct": False,
             "why": "Lipid builds cell membranes, but it is not an element "
                    "and bone is not built round it."},
            {"text": "Minerals", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e24",
        "band": "easier",
        "text": "How much energy does a vitamin tablet supply?",
        "options": [
            {"text": "None at all, because a vitamin releases no energy when "
                     "the body uses it.", "correct": True},
            {"text": "A little, because vitamins are respired slowly.",
             "correct": False,
             "why": "Vitamins are not respired at any rate. Their job is to "
                    "let other reactions run, not to be fuel."},
            {"text": "More per gram than food, as so little is needed.",
             "correct": False,
             "why": "Needing little of something says nothing about its "
                    "energy, and a vitamin's energy content is zero."},
            {"text": "About the same per gram as carbohydrate.",
             "correct": False,
             "why": "Carbohydrate is one of the three nutrients that do "
                    "release energy, and no vitamin is on that list."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e25",
        "band": "easier",
        "text": "A 13-year-old's daily lipid requirement is closest to which "
                "of these?",
        "options": [
            {"text": "About 300 g", "correct": False,
             "why": "About 300 g is the carbohydrate figure, and lipid sits "
                    "in the tens of grams rather than the hundreds."},
            {"text": "About 70 g", "correct": True},
            {"text": "About 0.2 g", "correct": False,
             "why": "About 0.2 g covers all thirteen vitamins together, which "
                    "is a trace beside the fat in a day's food."},
            {"text": "About 0 g", "correct": False,
             "why": "Lipid feels as though it should be near zero and is "
                    "not — it builds every cell membrane."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e26",
        "band": "easier",
        "text": "What is a nutrient?",
        "options": [
            {"text": "Any substance in food that has a taste of its own.",
             "correct": False,
             "why": "Taste has nothing to do with it. Water is a nutrient and "
                    "tastes of very little."},
            {"text": "Any substance in food that the body can respire.",
             "correct": False,
             "why": "Four of the seven are never respired, and they are "
                    "nutrients all the same."},
            {"text": "A substance in food the body needs in order to work, "
                     "grow or repair itself.", "correct": True},
            {"text": "A substance added to food to keep it fresh for longer.",
             "correct": False,
             "why": "That describes a preservative, which is something the "
                    "food needs rather than something the body does."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e27",
        "band": "easier",
        "text": "Bread, rice, pasta and potato are eaten mainly for which "
                "nutrient?",
        "options": [
            {"text": "Carbohydrate", "correct": True},
            {"text": "Protein", "correct": False,
             "why": "Meat, fish, eggs and lentils are the protein foods, and "
                    "bread supplies only a little of it."},
            {"text": "Vitamins", "correct": False,
             "why": "Fruit, vegetables, dairy and liver are the usual vitamin "
                    "sources rather than starchy staples."},
            {"text": "Lipid (fat and oil)", "correct": False,
             "why": "Oils, butter, nuts and oily fish are the lipid foods. A "
                    "boiled potato carries almost no fat."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e28",
        "band": "easier",
        "text": "Apart from constipation, what does a diet low in fibre raise "
                "the long-term risk of?",
        "options": [
            {"text": "Iron-deficiency anaemia", "correct": False,
             "why": "Anaemia comes from going short of iron, and fibre "
                    "carries no iron into the body."},
            {"text": "Scurvy", "correct": False,
             "why": "Scurvy comes from going short of vitamin C, which a "
                    "high-fibre diet does not guarantee either."},
            {"text": "Goitre", "correct": False,
             "why": "Goitre comes from going short of iodine, a mineral with "
                    "nothing to do with bulk in the gut."},
            {"text": "Bowel disease", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e29",
        "band": "easier",
        "text": "Fruit, vegetables, dairy and liver are eaten mainly for "
                "which nutrient group?",
        "options": [
            {"text": "Dietary fibre", "correct": False,
             "why": "Wholegrains, pulses and skins are the fibre foods, and "
                    "liver and dairy carry none at all."},
            {"text": "Vitamins", "correct": True},
            {"text": "Carbohydrate", "correct": False,
             "why": "Bread, rice, pasta and potato are the carbohydrate "
                    "foods, and liver is not one of them."},
            {"text": "Water", "correct": False,
             "why": "Water comes from drinks and from most foods, so this "
                    "list is no better for it than any other."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-e30",
        "band": "easier",
        "text": "A 13-year-old needs about 2000 g of water a day. Where does "
                "most of it come from?",
        "options": [
            {"text": "From respiring the carbohydrate, lipid and protein in "
                     "their food.", "correct": False,
             "why": "Respiration is not where two kilograms a day come from; "
                    "the diet itself has to supply it."},
            {"text": "From the vitamins and minerals their food carries.",
             "correct": False,
             "why": "Vitamins and minerals together weigh about 5 g a day, "
                    "which is nowhere near 2000 g."},
            {"text": "From their drinks, and from most of the food they eat.",
             "correct": True},
            {"text": "From dietary fibre, which holds water inside the gut.",
             "correct": False,
             "why": "Fibre is about 25 g a day of plant material, and it is "
                    "not where the body's water supply comes from."},
        ],
        "figure": None,
    },

    # ── standard · MRB-338 expansion ────────────────────────────────────
    {
        "id": "b3-01-s08",
        "band": "standard",
        "text": "A village eats well and gets plenty of calcium, iron and "
                "salt, but the water and soil there carry almost no iodine. "
                "Goitre is common. Why does the rest of the diet not cover it?",
        "options": [
            {"text": "Each mineral has its own job, and no other mineral can "
                     "be built into thyroid hormone.", "correct": True},
            {"text": "The other minerals block iodine from being absorbed "
                     "when there is plenty of them about.", "correct": False,
             "why": "Calcium, iron and salt do not shut iodine out. The "
                    "problem is simply that there is none there to absorb."},
            {"text": "Minerals are counted as one group, so a good total mass "
                     "of minerals covers all of them.", "correct": False,
             "why": "The group total of about 5 g says nothing about which "
                    "elements make it up, and iodine is not one of them here."},
            {"text": "The body makes its own iodine once the other minerals "
                     "are all present in the diet.", "correct": False,
             "why": "The body cannot make a chemical element. Every mineral "
                    "in the body arrived in the food or the drink."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s09",
        "band": "standard",
        "text": "For a week someone eats nothing but fruit and vegetables — a "
                "large amount of them, several kilograms a day. Which two "
                "nutrients is that week short of?",
        "options": [
            {"text": "Vitamins and water", "correct": False,
             "why": "Fruit and vegetables are among the best sources of both. "
                    "Those are the two this diet supplies well."},
            {"text": "Dietary fibre and minerals", "correct": False,
             "why": "Plant skins and leaves are exactly where fibre and many "
                    "minerals come from, so neither is the gap."},
            {"text": "Protein and lipid", "correct": True},
            {"text": "Carbohydrate and protein", "correct": False,
             "why": "Fruit sugar is a carbohydrate and is respired like any "
                    "other, so carbohydrate is not short here."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s10",
        "band": "standard",
        "text": "A multivitamin bottle gives its energy content as 0 kJ per "
                "tablet. A student says the label must be a misprint. Is it?",
        "options": [
            {"text": "It is a misprint, because everything a person swallows "
                     "carries some energy.", "correct": False,
             "why": "Water carries none either, and it is swallowed by the "
                    "litre. Being edible is not the same as being fuel."},
            {"text": "It is correct — vitamins release no energy, and only "
                     "three nutrients do.", "correct": True},
            {"text": "It is a misprint, because vitamins are what release the "
                     "energy from a meal.", "correct": False,
             "why": "Vitamins let the reactions run; the energy comes out of "
                    "the glucose, not out of the vitamin."},
            {"text": "It is correct, because the tablet is too small a mass "
                     "for its energy to be worth printing.", "correct": False,
             "why": "The figure is zero, not too small to print. A gram of "
                    "vitamins would still release no energy."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s11",
        "band": "standard",
        "text": "Someone drinks plenty of water for two days but eats "
                "nothing. They are still alive and can think clearly. Which "
                "part of the seven does that show?",
        "options": [
            {"text": "That water alone can meet a person's needs for as long "
                     "as they keep drinking it.", "correct": False,
             "why": "Two days is not a long time. The other six run out "
                    "later, and going without them is fatal too."},
            {"text": "That the body can make the other six nutrients out of "
                     "water when it has to.", "correct": False,
             "why": "The body cannot build protein, vitamins or minerals out "
                    "of water. They have to arrive in food."},
            {"text": "That food is only needed by people who are growing, "
                     "or who are doing hard physical work.",
             "correct": False,
             "why": "An adult sitting still is still respiring, still "
                    "repairing tissue, and still needs all seven."},
            {"text": "That a water shortage bites within hours, while the "
                     "other shortages take longer to show.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s12",
        "band": "standard",
        "text": "A packed lunch is white bread, sliced ham, a bag of crisps "
                "and a fizzy drink, every day for a term. Which two nutrient "
                "groups is it supplying least well?",
        "options": [
            {"text": "Carbohydrate and lipid", "correct": False,
             "why": "Bread, crisps and a sugary drink supply plenty of both. "
                    "Those are the two this lunch is heaviest in."},
            {"text": "Dietary fibre and vitamins", "correct": True},
            {"text": "Protein and water", "correct": False,
             "why": "The ham supplies protein and the drink is mostly water, "
                    "so these two are covered."},
            {"text": "Minerals and protein", "correct": False,
             "why": "Crisps carry a good deal of salt and the ham supplies "
                    "protein, so neither is the weak point."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s13",
        "band": "standard",
        "text": "A cook on a long voyage eats plenty of food but no fruit or "
                "vegetables. For three months they seem perfectly well, and "
                "then they become very ill. Explain the delay.",
        "options": [
            {"text": "The illness needs an infection to start it, and that "
                     "took three months to reach the ship.", "correct": False,
             "why": "No germ is involved. Adding one orange a day prevents "
                    "it, which no infection would respond to."},
            {"text": "Their energy supply was fine, so the deficiency only "
                     "showed once the body ran out of vitamin C.",
             "correct": True},
            {"text": "The other six nutrients kept them well until every "
                     "one of those ran out at the three-month mark too.",
             "correct": False,
             "why": "The other six were still arriving in the food. Only the "
                    "vitamin C supply had stopped."},
            {"text": "Three months of hard work is what caused it, rather "
                     "than anything about the food.", "correct": False,
             "why": "Work does not cause it. Sailors doing the same work with "
                    "fruit in the rations stayed well."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s14",
        "band": "standard",
        "text": "When carbohydrate runs short, the body respires its own fat "
                "before it starts on its own protein. Why is that order the "
                "sensible one?",
        "options": [
            {"text": "Because fat is a store, while protein is the muscle and "
                     "the enzymes doing the work.", "correct": True},
            {"text": "Because fat is easier to reach than protein, which is "
                     "locked deep inside the bones.", "correct": False,
             "why": "How easy tissue is to reach is not the reason. Muscle "
                    "protein is broken down readily once fat runs low."},
            {"text": "Because fat releases less energy per gram, so it is "
                     "spent first and kept for emergencies.", "correct": False,
             "why": "Fat releases more than twice the energy per gram of "
                    "carbohydrate, so this has the science backwards."},
            {"text": "Because protein cannot be respired for energy by the "
                     "body under any conditions.", "correct": False,
             "why": "Protein can be respired, and is — that is exactly why "
                    "muscle is lost in a long shortage."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s15",
        "band": "standard",
        "text": "Carrots are a good source of vitamin A. Why is a plate of "
                "carrots cooked with a little oil better at delivering that "
                "vitamin than the same carrots boiled in water?",
        "options": [
            {"text": "Oil makes carrots easier to chew, so more of the "
                     "vitamin is released from them.", "correct": False,
             "why": "Chewing is not the limit. Boiled carrots are soft and "
                    "still deliver vitamin A poorly without fat."},
            {"text": "Oil is itself a rich source of vitamin A, so the meal "
                     "simply supplies more of it.", "correct": False,
             "why": "Cooking oil is not a vitamin A food. It is the carrot "
                    "supplying the vitamin in both meals."},
            {"text": "Vitamin A dissolves in fat, so without lipid in the "
                     "meal it cannot be absorbed.", "correct": True},
            {"text": "Boiling water destroys vitamin A, and oil protects it "
                     "from the heat of the pan.", "correct": False,
             "why": "The oil is hotter than the water, so protection from "
                    "heat cannot be the explanation."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s16",
        "band": "standard",
        "text": "Someone who is constipated starts taking a multivitamin and "
                "mineral tablet every morning. A month later nothing has "
                "changed. Why would you expect that?",
        "options": [
            {"text": "The tablet supplies no bulk, and bulk is what the gut "
                     "muscles need to push against.", "correct": True},
            {"text": "A month is far too soon for a vitamin tablet to have "
                     "any effect on the gut at all.", "correct": False,
             "why": "Time is not the issue. A tablet of this kind would not "
                    "fix it after a year either."},
            {"text": "Minerals in a tablet cancel out the fibre already in "
                     "the diet, so nothing improves.", "correct": False,
             "why": "Minerals do not cancel fibre. The tablet simply has "
                    "nothing to do with how the gut is loaded."},
            {"text": "Tablets are swallowed whole, so they leave the body "
                     "again without being absorbed.", "correct": False,
             "why": "The vitamins and minerals in the tablet are absorbed "
                    "perfectly well — they are just not what is missing."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s17",
        "band": "standard",
        "text": "A family eats no meat and no fish. Which change would best "
                "cover the nutrient those foods usually supply most of?",
        "options": [
            {"text": "More bread, rice and pasta at every meal of the day.",
             "correct": False,
             "why": "Those are carbohydrate foods. They supply fuel rather "
                    "than the amino acids meat was providing."},
            {"text": "More fruit and salad vegetables alongside every meal.",
             "correct": False,
             "why": "Fruit and salad are good for vitamins and fibre, but "
                    "they carry very little protein."},
            {"text": "A daily multivitamin tablet with added minerals.",
             "correct": False,
             "why": "A tablet supplies neither protein nor energy, so it "
                    "cannot replace what meat and fish were bringing."},
            {"text": "More beans, lentils and eggs at the main meal.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s18",
        "band": "standard",
        "text": "Of the seven nutrients, a shortage of water kills faster "
                "than a shortage of any other. What is the reason?",
        "options": [
            {"text": "Water is needed in the largest mass, so it runs out "
                     "before anything else does.", "correct": False,
             "why": "Mass is not the reason. Carbohydrate is needed in "
                    "hundreds of grams and a person survives weeks without "
                    "it."},
            {"text": "Every reaction in the body happens in solution, so "
                     "losing water stops all of them.", "correct": True},
            {"text": "Water is the only one of the seven the body cannot "
                     "store anywhere at all.", "correct": False,
             "why": "The body carries a great deal of water. What it cannot "
                    "do is keep working once that falls."},
            {"text": "Water is the only nutrient lost in urine, so it drains "
                     "away faster than the rest.", "correct": False,
             "why": "Minerals leave in urine too. What matters is what "
                    "happens to the body's reactions when water goes."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s19",
        "band": "standard",
        "text": "A student works out how much salt they eat in a day, "
                "compares it with the daily figure for minerals as a group, "
                "and concludes their mineral needs are met. What is wrong?",
        "options": [
            {"text": "Salt is one mineral among several, so calcium, iron "
                     "and iodine are all still missing.", "correct": True},
            {"text": "Salt is not a mineral at all, so none of what they eat "
                     "counts towards the group figure.", "correct": False,
             "why": "Salt supplies sodium, which is a mineral and does count. "
                    "The error is treating it as all of them."},
            {"text": "The group figure is a maximum rather than a target, so "
                     "they have already had too much.", "correct": False,
             "why": "The figure is the amount needed, not a ceiling, and the "
                    "argument still ignores which elements make it up."},
            {"text": "Minerals are measured after cooking, so the raw figure "
                     "on the packet cannot be used.", "correct": False,
             "why": "Cooking is not the issue here. The gap is that one "
                    "element has been counted as though it were seven."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s20",
        "band": "standard",
        "text": "Health advice singles out fruit and vegetables for a daily "
                "target rather than singling out bread or meat. Using the "
                "seven nutrients, what is the reasoning?",
        "options": [
            {"text": "Fruit and vegetables are the lowest in energy, and "
                     "energy is what the advice is trying to cut.",
             "correct": False,
             "why": "The advice is a target to reach, not a limit. Its point "
                    "is what those foods bring, not what they lack."},
            {"text": "Bread and meat are harmful, which is why no daily "
                     "target is set for them.", "correct": False,
             "why": "Both are ordinary sources of carbohydrate and protein. "
                    "Nothing about the seven makes either one harmful."},
            {"text": "Fruit and vegetables are the main source of vitamins, "
                     "and they bring fibre as well.", "correct": True},
            {"text": "Fruit and vegetables are the only foods that supply "
                     "any water, which is the largest need.", "correct": False,
             "why": "Drinks and most other foods supply water too, so that "
                    "cannot be why these two are singled out."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s21",
        "band": "standard",
        "text": "A student plans a whole day of meals and gets six of the "
                "seven nutrients right, but forgets to plan any drinks at "
                "all. Which nutrient falls short, and how quickly?",
        "options": [
            {"text": "Carbohydrate, within about two days, once the body has "
                     "used up the glucose in the blood.", "correct": False,
             "why": "The meals were planned properly, so carbohydrate is "
                    "arriving; and its shortage takes far longer than that."},
            {"text": "Dietary fibre, within about a week, once the gut has "
                     "nothing left to push along.", "correct": False,
             "why": "Fibre comes from the food, which is planned. Forgetting "
                    "the drinks does not remove it."},
            {"text": "Minerals, within about a month, once the stores in the "
                     "bones have been used up.", "correct": False,
             "why": "Most minerals arrive in food rather than drink, so the "
                    "plan still supplies them."},
            {"text": "Water, within hours.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s22",
        "band": "standard",
        "text": "After an operation, a patient is advised to eat more of one "
                "particular nutrient while the wound heals. Which one, and "
                "why?",
        "options": [
            {"text": "More lipid, because a wound is sealed with the fat "
                     "stored under the skin.", "correct": False,
             "why": "Fat under the skin insulates and stores energy. New "
                    "tissue across a wound is built from protein."},
            {"text": "More protein, because new tissue is built from amino "
                     "acids.", "correct": True},
            {"text": "More carbohydrate, because healing is powered by "
                     "glucose and needs nothing else.", "correct": False,
             "why": "Glucose supplies the energy, but energy alone builds no "
                    "tissue. The material has to come from protein."},
            {"text": "More dietary fibre, because it gives the new tissue "
                     "something to grow along.", "correct": False,
             "why": "Fibre is never absorbed into the body, so it cannot "
                    "reach a wound, let alone shape one."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s23",
        "band": "standard",
        "text": "A toddler drinks a great deal of milk and eats very little "
                "else. Milk supplies protein, lipid, calcium and water well. "
                "Which of the seven is that diet worst for?",
        "options": [
            {"text": "Protein", "correct": False,
             "why": "Milk is a good protein food, and the question says so. "
                    "Growth is not what fails first here."},
            {"text": "Water", "correct": False,
             "why": "Milk is mostly water, so this is the nutrient a "
                    "milk-only diet is certain to cover."},
            {"text": "Dietary fibre", "correct": True},
            {"text": "Lipid (fat and oil)", "correct": False,
             "why": "Milk carries fat, so a toddler drinking a great deal of "
                    "it is getting lipid."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s24",
        "band": "standard",
        "text": "Two loaves supply about the same mass of carbohydrate per "
                "slice. One is white and one is wholemeal. Which of the seven "
                "does the wholemeal loaf supply more of?",
        "options": [
            {"text": "Water, because wholemeal dough is mixed much wetter "
                     "than white dough is.", "correct": False,
             "why": "Both loaves are baked until most of that water has gone, "
                    "and bread is not where a day's water comes from."},
            {"text": "Dietary fibre, because the whole grain is used rather "
                     "than the starchy part alone.", "correct": True},
            {"text": "Carbohydrate, because whole grains hold more starch "
                     "than refined flour does.", "correct": False,
             "why": "The question says the carbohydrate per slice is about "
                    "the same, so this is not the difference."},
            {"text": "Lipid, because the outer layers of a grain are where "
                     "the oil of the plant is stored.", "correct": False,
             "why": "Bread of either kind carries very little fat; oils, "
                    "nuts and oily fish are the lipid foods."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s25",
        "band": "standard",
        "text": "Someone eats about 3000 g of food and drink a day, which is "
                "more than most people. A doctor still finds a deficiency. "
                "How is that possible?",
        "options": [
            {"text": "Eating a large mass of food stops nutrients from being "
                     "absorbed properly.", "correct": False,
             "why": "A large meal is absorbed. Eating more of the wrong thing "
                    "does not block the right thing."},
            {"text": "The doctor must have measured something else, since "
                     "3000 g covers every requirement.", "correct": False,
             "why": "3000 g of one food covers one nutrient. The seven "
                    "targets have to be met separately."},
            {"text": "Deficiencies happen at low body mass, so a big eater "
                     "cannot have one.", "correct": False,
             "why": "Body mass does not decide it. A heavy person short of "
                    "vitamin C gets scurvy like anyone else."},
            {"text": "A deficiency is about which nutrients arrive, not how "
                     "much food does.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s26",
        "band": "standard",
        "text": "A food label lists, per 100 g: carbohydrate 60 g, protein "
                "8 g, fat 2 g and fibre 9 g. Which of the seven does that "
                "label tell you nothing about?",
        "options": [
            {"text": "Carbohydrate and lipid", "correct": False,
             "why": "Both are printed on the label, at 60 g and 2 g per "
                    "100 g of the food as sold."},
            {"text": "Protein and dietary fibre", "correct": False,
             "why": "Both are printed there too, at 8 g and 9 g, so neither "
                    "is missing from the label."},
            {"text": "Vitamins, minerals and water", "correct": True},
            {"text": "Nothing at all is missing from it", "correct": False,
             "why": "Four nutrients are listed and three are not, and no "
                    "arithmetic on the four recovers the other three."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s27",
        "band": "standard",
        "text": "Someone eats no dairy and no oily fish, spends the winter "
                "mostly indoors, and takes no supplement. Which vitamin is "
                "most at risk?",
        "options": [
            {"text": "Vitamin E", "correct": False,
             "why": "Vitamin E comes mostly from oils, nuts and seeds, none "
                    "of which this description takes away."},
            {"text": "Vitamin B1", "correct": False,
             "why": "Grains are still in this diet, so the vitamin whose "
                    "shortage causes beriberi is not the gap."},
            {"text": "Vitamin D", "correct": True},
            {"text": "Vitamin K", "correct": False,
             "why": "Green leafy vegetables are not excluded by the "
                    "description, so this one is still arriving."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s28",
        "band": "standard",
        "text": "Two people eat completely different foods — one rice, fish "
                "and greens, the other bread, cheese and apples — and both "
                "diets are balanced. How can both be true?",
        "options": [
            {"text": "Balance is about hitting seven nutrient targets, and "
                     "many different food lists can hit them.", "correct": True},
            {"text": "Only one of them can really be balanced, and the other "
                     "person will become ill eventually.", "correct": False,
             "why": "There is no single correct food list. Either set of "
                    "foods can deliver all seven nutrients."},
            {"text": "Balance depends on where a person lives, so each diet "
                     "is balanced only in its own country.", "correct": False,
             "why": "The seven requirements are the same wherever a person "
                    "is; it is the foods available that differ."},
            {"text": "Both are balanced because they contain the same mass of "
                     "food, which is what balance measures.", "correct": False,
             "why": "Total mass is not what balance means. Two meals of equal "
                    "mass can be nothing alike nutritionally."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s29",
        "band": "standard",
        "text": "Someone decides to eat a whole week's worth of protein in "
                "one large Sunday meal, and none at all for the following six "
                "days. Why does that plan fail?",
        "options": [
            {"text": "Because protein eaten in one go is not digested, and "
                     "leaves the body unchanged.", "correct": False,
             "why": "A large protein meal is digested normally. The problem "
                    "is what happens on the six days after it."},
            {"text": "Because growth and repair go on every day, and the body "
                     "has no protein store to draw on.", "correct": True},
            {"text": "Because a week's protein in one meal would be a fatal "
                     "dose for someone of school age.", "correct": False,
             "why": "It would be an unpleasant amount to eat, but the reason "
                    "the plan fails is the six empty days."},
            {"text": "Because protein is only absorbed in the presence of the "
                     "day's carbohydrate and lipid.", "correct": False,
             "why": "Protein does not need the other two present to be "
                    "absorbed. Each nutrient is handled on its own."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-s30",
        "band": "standard",
        "text": "On a day with no exercise at all, someone still needs about "
                "2000 g of water. Why does resting not lower the requirement "
                "to near zero?",
        "options": [
            {"text": "Because water is stored in the muscles, and resting "
                     "muscles hold less of it than working ones.",
             "correct": False,
             "why": "Resting muscle does not dump its water. The need comes "
                    "from what water is doing, not from how hard you work."},
            {"text": "Because water is respired for energy at rest and must "
                     "be replaced as it is used up.", "correct": False,
             "why": "Water is not respired at all. Only carbohydrate, lipid "
                    "and protein release energy."},
            {"text": "Because the reactions that keep a person alive run all "
                     "day, and every one of them happens in solution.",
             "correct": True},
            {"text": "Because the body loses water only through sweat, which "
                     "continues whether or not a person moves.",
             "correct": False,
             "why": "Urine and breath carry water away too, so sweat is not "
                    "the whole of the loss being replaced."},
        ],
        "figure": None,
    },

    # ── harder · MRB-338 expansion ──────────────────────────────────────
    {
        "id": "b3-01-h08",
        "band": "harder",
        "text": "When Takaki changed one ship's rations, a second ship kept "
                "the old rations and sailed the same route at the same time. "
                "Why does having that second ship matter?",
        "options": [
            {"text": "Without it, any fall in illness could have been put "
                     "down to the route or the year rather than the food.",
             "correct": True},
            {"text": "It doubled the number of sailors being studied, and a "
                     "larger total on its own is what makes a conclusion "
                     "sound.", "correct": False,
             "why": "Numbers alone prove nothing here. Two thousand sailors "
                    "all eating barley would still have no comparison."},
            {"text": "It gave the barley crew someone to trade rations with "
                     "if the new diet turned out to be unpalatable.",
             "correct": False,
             "why": "Swapping rations between the ships would have destroyed "
                    "the very comparison the second ship existed to make."},
            {"text": "It showed that beriberi was infectious, since the two "
                     "crews never met during the voyage.", "correct": False,
             "why": "The result pointed the other way: the disease tracked "
                    "the food, which is not how an infection behaves."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h09",
        "band": "harder",
        "text": "A week-long plan replaces all meals with fruit juice, "
                "promising to 'clean out' the body. Judged against the seven "
                "nutrients, what is the strongest criticism?",
        "options": [
            {"text": "It supplies no energy at all, so the body has nothing "
                     "to respire for a week.", "correct": False,
             "why": "Fruit juice is largely sugar, so energy is the one thing "
                    "the plan does deliver."},
            {"text": "It supplies almost no protein, lipid or fibre, so three "
                     "of the seven are missing for the week.", "correct": True},
            {"text": "It supplies too much water, which washes the vitamins "
                     "back out of the body before they can work.",
             "correct": False,
             "why": "Drinking does not flush vitamins out faster than they "
                    "can be used, and water is a nutrient in its own right."},
            {"text": "It supplies no vitamins, because juicing destroys every "
                     "vitamin in the fruit as it is pressed.", "correct": False,
             "why": "Fruit juice is a reasonable vitamin C source. Vitamins "
                    "are not what this plan is short of."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h10",
        "band": "harder",
        "text": "A fibre powder supplies 25 g of fibre in a spoonful, the "
                "same mass a day's wholegrains and vegetables would. Using "
                "the seven, what does the powder not replace?",
        "options": [
            {"text": "The bulk, since a powder cannot give the gut muscles "
                     "anything to push against.", "correct": False,
             "why": "Fibre powder does add bulk in the gut; that part of the "
                    "job it genuinely does."},
            {"text": "The energy, since wholegrains are respired and the "
                     "powder is not.", "correct": False,
             "why": "Fibre is not respired in either form — that is what "
                    "makes it fibre rather than carbohydrate."},
            {"text": "The vitamins and minerals that come with the "
                     "wholegrains and vegetables.", "correct": True},
            {"text": "The water, since a dry powder takes water out of the "
                     "gut instead of adding it.", "correct": False,
             "why": "The powder is taken in a drink. Water intake is not what "
                    "separates it from a plate of vegetables."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h11",
        "band": "harder",
        "text": "A student argues that since water is needed in the largest "
                "amount, it must be the most important nutrient, and vitamins "
                "the least. Evaluate that argument.",
        "options": [
            {"text": "It is sound, because the body would not ask for a full "
                     "2000 g a day of something that did not matter much.",
             "correct": False,
             "why": "The amount reflects what the nutrient is used for, not "
                    "how badly the body needs it to be there."},
            {"text": "It is sound for water but wrong for vitamins, which "
                     "are the second most important group.", "correct": False,
             "why": "The ranking itself is the error. There is no order of "
                    "importance among seven requirements that all have to be "
                    "met."},
            {"text": "It is wrong, because vitamins are actually needed in a "
                     "larger mass than water is.", "correct": False,
             "why": "All thirteen vitamins together come to about 0.2 g "
                    "against water's 2000 g, so the masses are as stated."},
            {"text": "It is wrong, because a shortage of any one of the "
                     "seven is eventually fatal whatever its mass.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h12",
        "band": "harder",
        "text": "A patient is fed for three weeks on a drip carrying only "
                "glucose dissolved in water. Which problem would you expect "
                "to appear first, and why?",
        "options": [
            {"text": "Tissue is lost, because no protein is arriving and the "
                     "body starts breaking down its own.", "correct": True},
            {"text": "Constipation, because the drip supplies no fibre for "
                     "the gut muscles to work against.", "correct": False,
             "why": "There is nothing passing through the gut at all on a "
                    "drip, so this is not the first failure."},
            {"text": "Dehydration, because glucose solution draws water out "
                     "of the body rather than adding it.", "correct": False,
             "why": "The drip is glucose dissolved in water, so water is the "
                    "nutrient it supplies most generously."},
            {"text": "Exhaustion, because glucose cannot be respired unless "
                     "it is eaten rather than injected.", "correct": False,
             "why": "Glucose in the blood is respired whichever way it "
                    "arrived, which is why a drip works at all."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h13",
        "band": "harder",
        "text": "Someone already meeting all seven targets doubles their "
                "protein and doubles their vitamin C. What does the seven-"
                "nutrient picture predict about the benefit?",
        "options": [
            {"text": "Both will help, because more of a nutrient the body "
                     "uses is always better for it.", "correct": False,
             "why": "A target is an amount to reach. Going past it does not "
                    "buy more of what the nutrient was doing."},
            {"text": "Neither target was unmet, so there is no deficiency "
                     "left for the extra to put right.", "correct": True},
            {"text": "Only the vitamin C will help, since vitamins are the "
                     "group that has no upper limit at all.", "correct": False,
             "why": "Vitamins have targets like the rest, and being needed in "
                    "milligrams does not mean more is better."},
            {"text": "Only the protein will help, because protein is the one "
                     "nutrient the body can store for later.", "correct": False,
             "why": "The body keeps no protein store waiting to be used, "
                    "which is why a daily supply is needed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h14",
        "band": "harder",
        "text": "An expedition must carry thirty days of food. Dried rations "
                "weigh a quarter of what tinned food does. What must the "
                "planners check before choosing the dried rations?",
        "options": [
            {"text": "That the dried food has not lost its protein, since "
                     "protein is the nutrient that drying takes out of food.",
             "correct": False,
             "why": "Drying takes out water, not protein. Dried meat and "
                    "pulses are protein-rich."},
            {"text": "That the team can carry enough fuel, since dried food "
                     "supplies less energy per gram.", "correct": False,
             "why": "Removing water concentrates the energy, so dried food "
                    "carries more energy per gram, not less."},
            {"text": "That there is a safe water supply on the route, since "
                     "the mass saved is water the body still needs.",
             "correct": True},
            {"text": "That the dried food still contains fibre, since bulk is "
                     "lost along with the water.", "correct": False,
             "why": "Dried pulses and grains keep their fibre. It is the "
                    "water, not the bulk, that drying removes."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h15",
        "band": "harder",
        "text": "A rice mill advertises its polished white rice as purer "
                "than brown rice because the outer layers have been removed. "
                "Evaluate that claim nutritionally.",
        "options": [
            {"text": "It is fair, since removing the outer layers leaves "
                     "nothing behind but the starch the body actually wants.",
             "correct": False,
             "why": "The outer layers were useful too. Calling what is left "
                    "purer treats the loss as if it were dirt."},
            {"text": "It is fair, since the outer layers hold no nutrients "
                     "the body is able to absorb anyway.", "correct": False,
             "why": "Those layers carry vitamin B1 and fibre, and the vitamin "
                    "is absorbed perfectly well."},
            {"text": "It is unfair, since polished rice cannot be respired "
                     "for energy once the outer layers are gone.",
             "correct": False,
             "why": "White rice is almost entirely starch and is an excellent "
                    "energy food; the loss is elsewhere."},
            {"text": "It is unfair, since polishing removes vitamin B1, and "
                     "crews living on polished rice developed beriberi.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h16",
        "band": "harder",
        "text": "A daily orange clears up one patient's scurvy in weeks. A "
                "second patient with rickets is given the same orange every "
                "day and does not improve. Explain the difference.",
        "options": [
            {"text": "Each deficiency is a shortage of one particular "
                     "nutrient, and an orange supplies vitamin C, not "
                     "vitamin D.", "correct": True},
            {"text": "Rickets is not a deficiency disease, so no change of "
                     "diet could ever have any effect on it.",
             "correct": False,
             "why": "Rickets is a deficiency disease. It answers to vitamin "
                    "D, which an orange does not carry."},
            {"text": "The second patient needed to eat several oranges a day "
                     "rather than one, because bone takes more repairing.",
             "correct": False,
             "why": "A hundred oranges would not help, because the vitamin "
                    "that is missing is not in them at any dose."},
            {"text": "Vitamin C is destroyed by the bone disease, so the "
                     "second patient absorbs none of what the orange brings.",
             "correct": False,
             "why": "Rickets does not destroy vitamin C. The second patient "
                    "absorbs it fine and is short of something else."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h17",
        "band": "harder",
        "text": "A cereal bar is sold as 'high protein — build muscle'. The "
                "buyer eats three a day on top of a diet already meeting its "
                "protein target, and does no training. What follows?",
        "options": [
            {"text": "The muscle is built, because protein is the material "
                     "muscle is made from and more of it means more muscle.",
             "correct": False,
             "why": "Protein is the material, but material alone builds "
                    "nothing. The target was already being met."},
            {"text": "No extra muscle, because the protein target was "
                     "already met and the extra is simply respired.",
             "correct": True},
            {"text": "Muscle is lost, because extra protein blocks the amino "
                     "acids from the rest of the diet being absorbed.",
             "correct": False,
             "why": "Extra protein does not block absorption of the protein "
                    "already in the diet."},
            {"text": "Nothing changes at all, because protein from a "
                     "processed bar cannot be digested by the body.",
             "correct": False,
             "why": "Protein in a cereal bar is digested to amino acids like "
                    "protein in any other food."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h18",
        "band": "harder",
        "text": "A survey of 50 000 adults finds that those eating the most "
                "fibre have the least bowel disease. A newspaper reports that "
                "fibre prevents bowel disease. What is the weakness?",
        "options": [
            {"text": "The sample is far too small for any conclusion about a "
                     "whole population to be drawn from it.", "correct": False,
             "why": "50 000 is a large sample. The difficulty is with what "
                    "the pattern can show, not with how many were asked."},
            {"text": "Bowel disease has no connection with diet, so the "
                     "survey has measured nothing of any use.", "correct": False,
             "why": "Low fibre does raise the long-term risk, so dismissing "
                    "the link entirely goes too far the other way."},
            {"text": "High-fibre eaters may differ in other ways too, so the "
                     "survey shows a link rather than a cause.",
             "correct": True},
            {"text": "Fibre is never absorbed, so it cannot have any effect "
                     "on the body at all.", "correct": False,
             "why": "Fibre works inside the gut without being absorbed, which "
                    "is exactly how it has its effect."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h19",
        "band": "harder",
        "text": "Two students argue about whether dietary fibre should be "
                "called a nutrient at all, since it is neither digested nor "
                "absorbed. Which position is the defensible one?",
        "options": [
            {"text": "It should not, because the word nutrient is reserved "
                     "for substances that release energy when respired.",
             "correct": False,
             "why": "Water, vitamins and minerals release no energy either, "
                    "and all three are nutrients."},
            {"text": "It should not, because anything leaving the body "
                     "unchanged has had no effect while it was inside.",
             "correct": False,
             "why": "It has a large effect on the way the gut works, which is "
                    "why leaving it out causes illness."},
            {"text": "It should, because the body needs it in order to work "
                     "properly, which is what a nutrient is.", "correct": True},
            {"text": "It should, because a small part of the fibre eaten is "
                     "absorbed and built into the gut wall.", "correct": False,
             "why": "None of it is absorbed. The case for calling it a "
                    "nutrient does not rest on that."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h20",
        "band": "harder",
        "text": "A yoghurt is reformulated: the fat is taken out and sugar "
                "is added so that it still tastes good. It is sold as the "
                "healthier choice. What does the seven-nutrient view say?",
        "options": [
            {"text": "Lipid is one of the seven, so removing it is a loss as "
                     "well as a gain, and the sugar adds nothing missing.",
             "correct": True},
            {"text": "It is straightforwardly healthier, because fat is the "
                     "one nutrient a diet is better off without.",
             "correct": False,
             "why": "Lipid builds every cell membrane and carries four "
                    "vitamins, so a diet is not better without it."},
            {"text": "It is straightforwardly worse, because sugar is not a "
                     "nutrient and belongs in no part of a diet.",
             "correct": False,
             "why": "Sugar is a carbohydrate, and carbohydrate is one of the "
                    "seven. The objection is about what was removed."},
            {"text": "Neither version can be judged, because the seven "
                     "nutrients say nothing about processed food.",
             "correct": False,
             "why": "The seven apply to any food at all. A processed yoghurt "
                    "is judged on what it delivers, like anything else."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h21",
        "band": "harder",
        "text": "A patient with goitre moves to a coast where sea fish is "
                "eaten daily, and the swelling slowly goes down. What does "
                "that recovery show about the original problem?",
        "options": [
            {"text": "That the thyroid gland had been damaged by the climate "
                     "inland and healed in the sea air.", "correct": False,
             "why": "Air and climate are not the variable. The diet changed, "
                    "and a mineral that had been missing started arriving."},
            {"text": "That it was a shortage of iodine, which sea fish "
                     "supplies.", "correct": True},
            {"text": "That goitre is infectious and the patient simply left "
                     "the area where the infection was.", "correct": False,
             "why": "No infection is involved. A deficiency disease answers "
                    "to the missing nutrient, not to moving away."},
            {"text": "That the extra protein in fish was what the thyroid "
                     "gland had been short of.", "correct": False,
             "why": "Thyroid hormone is built round iodine. Plenty of protein "
                    "inland had not prevented the goitre."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h22",
        "band": "harder",
        "text": "A company proposes feeding people on tablets supplying "
                "exactly the right mass of all seven nutrients, plus water, "
                "and nothing else. What is the most serious problem?",
        "options": [
            {"text": "It could not work, because tablets are swallowed whole "
                     "and are not digested by the body.", "correct": False,
             "why": "A tablet is broken down and absorbed. That is not where "
                    "the proposal runs into trouble."},
            {"text": "It could not work, because vitamins and minerals must "
                     "be eaten inside food in order to be absorbed at all.",
             "correct": False,
             "why": "A supplement's vitamins and minerals are absorbed, which "
                    "is why supplements do anything at all."},
            {"text": "The water would be enough on its own, so the tablets "
                     "would be unnecessary from the start.", "correct": False,
             "why": "Water supplies none of the other six, and a person on "
                    "water alone dies within weeks."},
            {"text": "The carbohydrate, lipid and protein alone come to "
                     "hundreds of grams a day, which is a meal, not a pill.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h23",
        "band": "harder",
        "text": "Compare four weeks with almost no carbohydrate against four "
                "weeks with almost no protein, everything else being met. "
                "What is the key difference in what happens?",
        "options": [
            {"text": "Neither shows anything in four weeks, because both "
                     "nutrients are stored in quantity for months.",
             "correct": False,
             "why": "There is no protein store to draw on, and the effects of "
                    "both shortages appear well inside four weeks."},
            {"text": "Both weeks are identical, because carbohydrate and "
                     "protein are respired in exactly the same way.",
             "correct": False,
             "why": "Protein can be respired, but its main job is building "
                    "tissue, which carbohydrate cannot do at all."},
            {"text": "Without protein nothing happens for months, while "
                     "without carbohydrate a person collapses within days.",
             "correct": False,
             "why": "The body respires its fat when carbohydrate is short, so "
                    "it does not collapse in days."},
            {"text": "Without carbohydrate the body burns its own fat for "
                     "fuel; without protein it cannot build or repair tissue.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h24",
        "band": "harder",
        "text": "A patient on a fat-free liquid feed develops signs of "
                "vitamin A shortage even though the feed contains vitamin A. "
                "Giving the vitamin by injection works. Why?",
        "options": [
            {"text": "Vitamin A dissolves only in fat, so with no lipid in "
                     "the feed it was never absorbed from the gut.",
             "correct": True},
            {"text": "The vitamin A in the feed had been destroyed by "
                     "processing, and the injected form had not.",
             "correct": False,
             "why": "The feed's vitamin A is intact; the difficulty is that "
                    "it never crosses into the blood."},
            {"text": "An injection carries a much larger dose than the feed "
                     "does, which is why it works where the feed failed.",
             "correct": False,
             "why": "Dose is not the issue. The vitamin in the feed passes "
                    "straight through however much is put in."},
            {"text": "Vitamin A has to reach the blood before the stomach "
                     "acid destroys it, and an injection is faster.",
             "correct": False,
             "why": "Speed is not the problem, and stomach acid is not what "
                    "is stopping this vitamin getting through."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h25",
        "band": "harder",
        "text": "For years, lemon juice was carried on ships as a medicine "
                "that cured scurvy. What does the seven-nutrient picture say "
                "about calling it a medicine?",
        "options": [
            {"text": "The name is fair, since the juice acts on the disease "
                     "exactly as a drug against an infection would.",
             "correct": False,
             "why": "There is no infection to act on. Nothing is being killed "
                    "or blocked; something missing is being replaced."},
            {"text": "It is better described as replacing a missing "
                     "nutrient, since the sailors were short of vitamin C.",
             "correct": True},
            {"text": "The name is fair, since only a medicine can reverse a "
                     "disease once its symptoms have appeared.",
             "correct": False,
             "why": "A diet reverses a deficiency disease routinely. That is "
                    "what happened on the ships."},
            {"text": "It is wrong, because the juice prevented scurvy without "
                     "ever curing anyone who already had it.",
             "correct": False,
             "why": "It did both. Sailors with scurvy recovered once vitamin "
                    "C started arriving again."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h26",
        "band": "harder",
        "text": "Two days of meals supply exactly the same energy, and one "
                "is balanced while the other is not. What must be compared to "
                "tell them apart?",
        "options": [
            {"text": "The total mass of food eaten, since a balanced day is "
                     "always the heavier of the two.", "correct": False,
             "why": "Mass does not decide it. A heavy day of one food is not "
                    "balanced, however much of it there is."},
            {"text": "The proportion of the energy coming from lipid, since "
                     "that is the whole of what balance means.",
             "correct": False,
             "why": "That is one figure out of seven. A day can get its "
                    "lipid right and still be short of four other things."},
            {"text": "The amount of each of the seven nutrients against the "
                     "amount needed of that nutrient.", "correct": True},
            {"text": "The number of separate foods eaten, since variety is "
                     "what the word balanced is measuring.", "correct": False,
             "why": "Variety usually helps, but it is a rough guide. What is "
                    "measured is whether each target is met."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h27",
        "band": "harder",
        "text": "A school wants to test whether a new wholemeal bread raises "
                "its pupils' fibre intake. What is the most important thing "
                "to keep the same between the two groups compared?",
        "options": [
            {"text": "The brand of bread, since two different bakers cannot "
                     "be compared with one another.", "correct": False,
             "why": "Comparing two breads is the point of the test. The brand "
                    "is the thing being changed."},
            {"text": "The energy of each pupil's lunch, since fibre intake "
                     "is worked out from the energy eaten.", "correct": False,
             "why": "Fibre is measured in grams of fibre, not worked back "
                    "from a day's energy."},
            {"text": "The number of pupils in each group, since the groups "
                     "must be identical in size for any comparison.",
             "correct": False,
             "why": "Groups of slightly different sizes can still be "
                    "compared; what matters is what else differs between "
                    "them."},
            {"text": "The rest of the food on offer, so that bread is the "
                     "only thing differing between the groups.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h28",
        "band": "harder",
        "text": "Someone says they cannot be malnourished because they are "
                "never hungry and never short of food. Using the seven "
                "nutrients, explain what is wrong with that reasoning.",
        "options": [
            {"text": "Hunger tracks how much food has been eaten, not "
                     "whether all seven nutrients were in it.",
             "correct": True},
            {"text": "Hunger is felt only when carbohydrate runs short, so a "
                     "shortage of any other nutrient is felt as thirst "
                     "instead.", "correct": False,
             "why": "A shortage of iodine or vitamin C is not felt as thirst. "
                    "Most deficiencies give no warning sensation."},
            {"text": "They are right, since a person eating enough food to "
                     "stop feeling hungry has met every requirement.",
             "correct": False,
             "why": "A large plate of one food stops hunger and still leaves "
                    "six targets unmet."},
            {"text": "Hunger is the body's measure of its vitamin level, so "
                     "it warns of a deficiency long before illness.",
             "correct": False,
             "why": "Hunger is not a vitamin meter. Scurvy develops in people "
                    "who feel perfectly well fed."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h29",
        "band": "harder",
        "text": "Compare six months with no dietary fibre against six months "
                "with no vitamin C, everything else being met. How do the two "
                "outcomes differ?",
        "options": [
            {"text": "Both end the same way, since six months without any "
                     "one of the seven is fatal in every case.",
             "correct": False,
             "why": "A long fibre shortage is serious, but it does not kill "
                    "in six months the way scurvy does."},
            {"text": "The fibre shortage brings constipation and a raised "
                     "bowel risk; the vitamin C shortage kills in about four "
                     "months.", "correct": True},
            {"text": "Neither shows in six months, because both are needed "
                     "in such small amounts that stores last for years.",
             "correct": False,
             "why": "Fibre is needed in tens of grams a day, and scurvy "
                    "appears well inside six months."},
            {"text": "The fibre shortage is the fatal one, since the gut "
                     "stops working altogether without bulk in it.",
             "correct": False,
             "why": "The gut does not stop altogether, and the outcome is "
                    "the less dangerous of the two over this period."},
        ],
        "figure": None,
    },
    {
        "id": "b3-01-h30",
        "band": "harder",
        "text": "A poster claims that you can tell a balanced meal by looking "
                "at the plate: a big pile of one food, a medium pile of "
                "another, a small pile of a third. Evaluate that test.",
        "options": [
            {"text": "It works completely, since the three pile sizes match "
                     "the three amount bands the seven nutrients fall into.",
             "correct": False,
             "why": "There are four bands and seven nutrients, and two of "
                    "the seven cannot be seen on a plate at all."},
            {"text": "It fails entirely, since the amount of a nutrient has "
                     "nothing whatever to do with the mass of the food that "
                     "is supplying it.", "correct": False,
             "why": "Mass and amount are related — 300 g of carbohydrate does "
                    "look like a big pile. The test is rough, not useless."},
            {"text": "It works for everything except water, which is the only "
                     "nutrient a plate cannot show.", "correct": False,
             "why": "A plate shows nothing about its vitamin or mineral "
                    "content either, so water is not the only gap."},
            {"text": "It is a rough guide for the three big ones, but "
                     "vitamins, minerals, fibre and water cannot be judged by "
                     "eye.", "correct": True},
        ],
        "figure": None,
    },
]
