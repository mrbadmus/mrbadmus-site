"""B9 lesson 02 — Predator and prey: twelve questions (MRB-269).

These probe the two things this lesson is built to fix and the one thing it is
easiest to half-learn: that the predator peak comes second because breeding
takes time, that food and space set a ceiling whether or not anything is
hunting, and that the bench is a model of a field rather than a field. The
distractors are built from the lesson's two declared misconceptions — ECO-03
(the two peaks happen at the same time) and ECO-04 (remove the predators and
the prey do brilliantly) — together with the beliefs the hook and the bench
notes are drawn to catch: that predators hold back deliberately or take only
the weak, that fast breeding alone is what saves the prey, that a population
that has crashed cannot rebuild, that a swing must go on for ever, and that
bar heights rather than the readouts are what the chart is saying. The harder
band works outside the field: the Hudson's Bay pelt ledgers as a record rather
than a census, stripped hare browse as a carrying capacity, a greenhouse of
aphids and ladybirds, and a delayed feedback with no animals in it at all. The
lesson carries no figures — every string on the page is drawn by an instrument
— so every question is figure=None.
"""

UNIT = "B9"
LESSON = "predator-and-prey"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-02-e01",
        "band": "easier",
        "text": "The page calls it the ceiling. What does carrying capacity "
                "mean?",
        "options": [
            {"text": "The largest population an environment can support, set "
                     "by food, water, space and disease.",
             "correct": True},
            {"text": "The size a population reaches once its predators have "
                     "all been removed from it.",
             "correct": False,
             "why": "Removing the foxes does not create the ceiling — it only "
                    "lets the rabbits reach it. The grass sets that limit "
                    "whether or not anything is hunting them."},
            {"text": "The number of prey one predator needs to catch in order "
                     "to survive a whole year.",
             "correct": False,
             "why": "That is one predator's appetite. Carrying capacity is a "
                    "limit the environment puts on a population, and it "
                    "applies to the rabbits with no foxes present at all."},
            {"text": "The largest number of new young a population is able to "
                     "add in a single year.",
             "correct": False,
             "why": "Carrying capacity limits how large a population becomes, "
                    "not how fast it grows. A population can breed quickly and "
                    "still stop dead at the ceiling."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e02",
        "band": "easier",
        "text": "Only a handful of foxes are left in the field. What happens "
                "to the rabbit population over the next few years?",
        "options": [
            {"text": "It falls as well, because rabbit and fox numbers rise "
                     "and fall in the same years.",
             "correct": False,
             "why": "That is the peaks-together idea. Look at the chart again: "
                    "when the foxes are at their lowest the rabbits are "
                    "already climbing, which is the opposite of moving "
                    "together."},
            {"text": "It stays low, because a population that has crashed can "
                     "never build itself back up.",
             "correct": False,
             "why": "Nothing stops it. Rabbits breed fast, and with the "
                    "hunting pressure off, the survivors are enough to rebuild "
                    "the population — that is step 4 of the cycle."},
            {"text": "It recovers, because so few foxes are left that far "
                     "fewer rabbits are being eaten.",
             "correct": True},
            {"text": "It rises without limit, because nothing is holding the "
                     "rabbit numbers back any more.",
             "correct": False,
             "why": "A few foxes are still hunting, and even with none at all "
                    "the grass sets a ceiling. The rabbits climb steeply and "
                    "then stop."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e03",
        "band": "easier",
        "text": "A field has a bumper year for rabbits. Why does the fox "
                "population not rise in that same year?",
        "options": [
            {"text": "Because foxes only begin breeding once the rabbits have "
                     "become scarce again the following year.",
             "correct": False,
             "why": "Foxes breed when food is plentiful, not when it runs "
                    "out. What takes the time is the cubs — being born, and "
                    "surviving their first winter."},
            {"text": "Because foxes turn to other prey in a good rabbit year "
                     "and leave the rabbits alone.",
             "correct": False,
             "why": "In this model rabbits are the only food, and even in a "
                    "real field a fox catches more rabbits when there are more "
                    "to catch. The delay is in the breeding, not in the "
                    "hunting."},
            {"text": "Because a bumper year produces young rabbits, and foxes "
                     "cannot catch rabbits that young.",
             "correct": False,
             "why": "Young rabbits are the easiest thing in the field to "
                    "catch. The hold-up is on the fox side: a well-fed fox "
                    "this spring shows up as extra foxes a year or more "
                    "later."},
            {"text": "Because breeding takes time: extra food now becomes "
                     "extra foxes only once cubs are born and survive.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e04",
        "band": "easier",
        "text": "The bench runs a model of one field. Which of these is "
                "actually built into it?",
        "options": [
            {"text": "Weather that varies from one year to the next.",
             "correct": False,
             "why": "There is no weather in the model — every year is the "
                    "same. That is one of the limitations you can name when "
                    "you are asked what the model leaves out."},
            {"text": "A fixed grass supply, which limits rabbit numbers.",
             "correct": True},
            {"text": "Foxes moving in from the farmland next door.",
             "correct": False,
             "why": "No animal enters or leaves. The field is closed, which is "
                    "why removing every fox holds the foxes at zero until you "
                    "let them back in."},
            {"text": "Disease spreading through a crowded population.",
             "correct": False,
             "why": "No disease either. Crowding makes a real population "
                    "vulnerable to it, but the model's only limit on the "
                    "rabbits is the grass."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-02-s01",
        "band": "standard",
        "text": "You press Remove every fox and then run the years on. The "
                "rabbits climb steeply and then stop climbing. Why do they "
                "stop?",
        "options": [
            {"text": "A few foxes must have survived and started hunting the "
                     "rabbits again.",
             "correct": False,
             "why": "The button removes every one, and the fox readout stays "
                    "at zero until you press it again. Nothing is hunting "
                    "them; what stops them is food."},
            {"text": "The chart has run out of height, so the bars cannot get "
                     "any taller.",
             "correct": False,
             "why": "Read the numbers above the chart, not the height of the "
                    "bars. The rabbit count itself stops rising, and the chart "
                    "rescales as the numbers grow."},
            {"text": "They have reached the ceiling the grass sets, so the "
                     "field cannot feed any more.",
             "correct": True},
            {"text": "Rabbit numbers always level off after ten years, "
                     "whatever else is going on.",
             "correct": False,
             "why": "It is not the passing of time that stops them, it is "
                    "running out of food and space. Give the field more grass "
                    "and they would stop somewhere else."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s02",
        "band": "standard",
        "text": "Foxes have hunted rabbits for thousands of years and there "
                "are still rabbits. What keeps the rabbits from being wiped "
                "out?",
        "options": [
            {"text": "As rabbits get scarce foxes go hungry, so fox "
                     "numbers fall and pressure eases.",
             "correct": True},
            {"text": "Foxes leave enough rabbits alive to breed, so that there "
                     "will be food next year.",
             "correct": False,
             "why": "Nothing is managing this. No fox is capable of holding "
                    "back for next year — the pattern falls out of the "
                    "arithmetic, not out of a decision."},
            {"text": "Foxes take only the old and the sick, so the healthy "
                     "rabbits are never touched.",
             "correct": False,
             "why": "Predators do often catch the weakest, but that is not "
                    "what saves the rabbits. A fox that took only healthy "
                    "adults would still starve once the rabbits ran short."},
            {"text": "Rabbits breed so fast that foxes could never eat them "
                     "faster than they are born.",
             "correct": False,
             "why": "They do breed fast, and on its own that is not enough — "
                    "the fox population would simply grow until it matched. "
                    "What turns the numbers is the foxes going hungry."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s03",
        "band": "standard",
        "text": "A student writes: “a wet summer means plenty of grass, so "
                "plenty of rabbits, so plenty of foxes that same summer.” "
                "What is wrong with the last step?",
        "options": [
            {"text": "Nothing is wrong — more rabbits really does mean more "
                     "foxes.",
             "correct": False,
             "why": "More rabbits does eventually mean more foxes, and "
                    "eventually is the whole lesson. Packed into one summer it "
                    "is the peaks-together idea, and on the bench the green "
                    "peak is always to the right."},
            {"text": "The foxes cannot answer that fast; this summer's rabbits "
                     "become extra foxes years later.",
             "correct": True},
            {"text": "It is back to front — plenty of rabbits actually means "
                     "fewer foxes in the field.",
             "correct": False,
             "why": "Plenty of rabbits is good news for foxes; it is the start "
                    "of the climb, not the fall. The fall comes later, once so "
                    "many foxes are hunting that the rabbits run short."},
            {"text": "Grass has nothing to do with it, since foxes do not eat "
                     "grass at any point.",
             "correct": False,
             "why": "Foxes do not eat grass, but grass is exactly what sets "
                    "the ceiling on the rabbits, and rabbits are what the "
                    "foxes eat. The mistake is in the timing, not in the "
                    "grass."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s04",
        "band": "standard",
        "text": "A student presses Ten years four times. The swings get "
                "smaller and smaller, until the bars barely change from one "
                "year to the next. What has happened?",
        "options": [
            {"text": "The foxes have eaten every rabbit, so there is nothing "
                     "left to change.",
             "correct": False,
             "why": "Read the two readouts: both numbers are well above zero "
                    "and steady. If the rabbits had gone, the foxes would "
                    "starve straight after and both would sit at zero."},
            {"text": "The model has broken, because a predator-prey cycle "
                     "should go on for ever.",
             "correct": False,
             "why": "Each swing here is smaller than the last, and real "
                    "populations cycle less tidily still — sometimes not at "
                    "all. A cycle that never fades would be the odd one out."},
            {"text": "The rabbits have reached the ceiling the grass sets, so "
                     "nothing can move.",
             "correct": False,
             "why": "The rabbits settle well below the ceiling, because the "
                    "foxes are still eating them. The ceiling is what they "
                    "reach when every fox is removed, which is a different "
                    "result."},
            {"text": "The populations have settled at numbers that hold "
                     "each other in place.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-02-h01",
        "band": "harder",
        "text": "The ten-year lynx and hare cycle was recovered from the "
                "Hudson's Bay Company's fur ledgers, which record pelts "
                "brought in by trappers. Why does that matter when you read "
                "the graph?",
        "options": [
            {"text": "It does not — one pelt is one hare, so the ledger is an "
                     "exact count.",
             "correct": False,
             "why": "One pelt is one hare that was caught, which is not the "
                    "same as one hare alive in the forest. How many are caught "
                    "depends on how many people are out catching them."},
            {"text": "It means the ten-year cycle in the data is not a real "
                     "pattern at all.",
             "correct": False,
             "why": "The opposite. A ten-year rhythm that survives all that "
                    "noise is a real rhythm — what the ledger is not is a "
                    "census."},
            {"text": "It means the trapping itself, rather than the lynx, "
                     "produced the hare cycle.",
             "correct": False,
             "why": "Trapping is in the line, but it is not a ten-year rhythm "
                    "shared with the lynx and it does not explain why the lynx "
                    "peak trails the hare peak. The record is imperfect, not "
                    "invented."},
            {"text": "Fur prices and the number of trappers are in the "
                     "line too, not just hares.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h02",
        "band": "harder",
        "text": "After a hare peak, the shoots and twigs the hares feed on are "
                "stripped bare and take years to grow back. Which part of the "
                "bench model does that behave like?",
        "options": [
            {"text": "The fixed grass supply — food setting a ceiling on how "
                     "many the land can hold.",
             "correct": True},
            {"text": "The lag — the delay that puts the predator peak after "
                     "the prey peak.",
             "correct": False,
             "why": "The lag sits on the predator's side and is about how long "
                    "breeding takes. Stripped shoots are food running out, "
                    "which is the other limit the model carries."},
            {"text": "The cull — something that takes a whole population out "
                     "at a stroke.",
             "correct": False,
             "why": "Nothing has been removed. The hares are all still there; "
                    "what has gone is the food, which lowers the number the "
                    "land can support rather than emptying it."},
            {"text": "Nothing in it, because the model's rabbits are limited "
                     "only by foxes.",
             "correct": False,
             "why": "They are not, and that is half the lesson. The grass "
                    "supply is in the model on purpose — it is why the rabbits "
                    "stop climbing once every fox is gone."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h03",
        "band": "harder",
        "text": "A gardener releases ladybirds into a greenhouse full of "
                "aphids. The aphids crash within weeks, and a month later the "
                "ladybirds crash too. If nothing else is changed, what should "
                "happen next?",
        "options": [
            {"text": "Both stay near zero, because once a predator has crashed "
                     "neither can recover.",
             "correct": False,
             "why": "That is not what the cycle does. With the predators down, "
                    "the survivors on the prey side face very little hunting, "
                    "and their numbers are the first to turn."},
            {"text": "The ladybirds recover first, since they were the ones "
                     "doing well most recently.",
             "correct": False,
             "why": "A predator cannot recover before its food does — there is "
                    "nothing for the extra ladybirds to eat. That is exactly "
                    "why the predator peak comes second."},
            {"text": "The aphids recover first, because so few ladybirds are "
                     "left to eat them.",
             "correct": True},
            {"text": "The aphids climb without limit, now that almost nothing "
                     "is eating them.",
             "correct": False,
             "why": "The plants in the greenhouse set a ceiling, just as the "
                    "grass does in the field. And as the aphids climb the "
                    "surviving ladybirds have plenty to eat, so they climb "
                    "after them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h04",
        "band": "harder",
        "text": "A country trains more vets whenever there is a shortage, and "
                "training takes five years. Vet numbers overshoot what is "
                "needed, then dip below it, over and over. Which feature of "
                "the fox and rabbit model explains that?",
        "options": [
            {"text": "The ceiling — there is a limit to how many vets a "
                     "country is able to support.",
             "correct": False,
             "why": "A ceiling limits how high a number climbs; on its own it "
                    "produces a levelling off, not a swing. Something has to "
                    "make the number overshoot in the first place."},
            {"text": "The delay — by the time the new vets arrive the shortage "
                     "they answered is over.",
             "correct": True},
            {"text": "Competition — the vets are all after the same jobs, "
                     "which pushes the numbers down.",
             "correct": False,
             "why": "Competition can set the level the numbers settle at, but "
                    "it does not make them swing past it and back. The "
                    "swinging comes from the response arriving late."},
            {"text": "Nothing — animal populations cycle for biological "
                     "reasons that do not apply to people.",
             "correct": False,
             "why": "Delayed feedback producing a swing is not a biology fact. "
                    "It is why a shower runs hot then cold when the tap is "
                    "slow to answer, and the same shape turns up wherever a "
                    "response arrives late."},
        ],
        "figure": None,
    },
]
