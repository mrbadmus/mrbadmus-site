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
    # ── MRB-335 top-up ──────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b9-02-e05",
        "band": "easier",
        "text": "A stoat hunts and eats voles. Which words describe the two "
                "animals?",
        "options": [
            {"text": "The stoat is the prey and the vole is the predator.",
             "correct": False,
             "why": "The two words are the wrong way round. A predator hunts "
                    "and eats; the prey is what is hunted."},
            {"text": "Both are predators, because both are wild animals that "
                     "have to find their own food.", "correct": False,
             "why": "A vole eats plants, so it hunts nothing. Being wild does "
                    "not make an animal a predator."},
            {"text": "The stoat is the predator and the vole is the prey.",
             "correct": True},
            {"text": "The stoat is the predator and the vole is a producer.",
             "correct": False,
             "why": "A producer builds its own food from sunlight. A vole "
                    "eats plants, so it is a consumer, and here it is prey as "
                    "well."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e06",
        "band": "easier",
        "text": "What does the word population mean in biology?",
        "options": [
            {"text": "All the individuals of one species living in the same "
                     "place.", "correct": True},
            {"text": "All the animals of every kind living in the same "
                     "place.", "correct": False,
             "why": "That is the whole community. A population is one species "
                    "— the rabbits of a field, counted on their own."},
            {"text": "The number of animals an environment is able to "
                     "support.", "correct": False,
             "why": "That is the carrying capacity, the ceiling. A population "
                    "is the animals themselves, and it can sit well below the "
                    "ceiling."},
            {"text": "A group of animals that live and hunt together, such as "
                     "a pack.", "correct": False,
             "why": "A pack is one group inside a population. Every rabbit in "
                    "the field belongs to the population whether or not it "
                    "lives alongside the others."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e07",
        "band": "easier",
        "text": "A blue tit eats caterpillars and is eaten by a sparrowhawk. "
                "What does that show?",
        "options": [
            {"text": "That the blue tit is neither predator nor prey, since "
                     "it sits in the middle of the chain.", "correct": False,
             "why": "It is both at once rather than neither. It hunts "
                    "caterpillars, which makes it a predator, and a "
                    "sparrowhawk hunts it, which makes it prey."},
            {"text": "That the blue tit is a predator only, because a bird "
                     "cannot be prey.", "correct": False,
             "why": "Plenty of birds are prey — a sparrowhawk makes its "
                    "living on them. What decides it is what an animal does "
                    "and what is done to it."},
            {"text": "That the caterpillar must be a predator too, since "
                     "something eats it.", "correct": False,
             "why": "Being eaten makes an organism prey, not a predator. A "
                    "caterpillar eats leaves, so it hunts nothing at all."},
            {"text": "That the same animal can be a predator to one species "
                     "and prey to another.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e08",
        "band": "easier",
        "text": "A field has no foxes in it at all. Why can the rabbit "
                "population still not go on rising for ever?",
        "options": [
            {"text": "Because a population always stops growing once it has "
                     "been rising for about ten years.", "correct": False,
             "why": "It is not the passing of time that stops it. What stops "
                    "it is running out of food and space."},
            {"text": "Because the food, water and space the field holds set a "
                     "limit on how many it can support.", "correct": True},
            {"text": "Because rabbits stop breeding once they notice the "
                     "field is becoming crowded.", "correct": False,
             "why": "Nothing is noticed or decided. Crowded rabbits are short "
                    "of food and more likely to fall ill, and that is what "
                    "brings the rise to a stop."},
            {"text": "Because another predator would always move in and take "
                     "the foxes' place.", "correct": False,
             "why": "One might, and the ceiling is there either way. Remove "
                    "every predator and the grass still runs out."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e09",
        "band": "easier",
        "text": "A rabbit population has reached the ceiling its field can "
                "support. What is that population likely to be like?",
        "options": [
            {"text": "Healthy and well fed, because the field is supporting "
                     "as many rabbits as it possibly can.", "correct": False,
             "why": "Supporting the most it can is not the same as supporting "
                    "them well. At the ceiling the food is stretched as far "
                    "as it will go."},
            {"text": "Falling steadily, because a population at its limit "
                     "always begins to die out.", "correct": False,
             "why": "It does not have to fall. It can sit at the ceiling for "
                    "years, held there by the food supply rather than pushed "
                    "below it."},
            {"text": "Crowded and short of food, and more vulnerable to "
                     "disease and to a hard winter.", "correct": True},
            {"text": "Still rising, because reaching the ceiling only slows a "
                     "population down.", "correct": False,
             "why": "The ceiling is where the rise stops, not where it slows. "
                    "There is no more food with which to support any more "
                    "rabbits."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b9-02-s05",
        "band": "standard",
        "text": "A farmer removes every fox from her land. Two years later "
                "there are far more rabbits, the grass is thin, and the "
                "rabbits are in poor condition. Explain.",
        "options": [
            {"text": "The rabbits are in poor condition because they miss the "
                     "foxes, which used to remove the weakest of them.",
             "correct": False,
             "why": "Predators do often take the weakest, and that is not "
                    "what is happening here. There are simply more rabbits "
                    "than the grass can feed."},
            {"text": "The grass is thin because rabbits stop eating grass "
                     "once their numbers are high.", "correct": False,
             "why": "They eat more grass, not less, because there are far "
                    "more of them. Thin grass is a result of the rise rather "
                    "than a cause of it."},
            {"text": "Something has gone wrong with the removal, because "
                     "rabbits with no predators should thrive.",
             "correct": False,
             "why": "Removing every predator is exactly what lets the rabbits "
                    "reach the ceiling, and the ceiling is not a comfortable "
                    "place to be. Nothing has gone wrong."},
            {"text": "With nothing hunting them the rabbits rose to the limit "
                     "the grass sets, and there is not enough to go round.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s06",
        "band": "standard",
        "text": "A cold wet spring kills most of the young voles in a wood. "
                "The owls there eat voles and nothing else. What happens to "
                "owl numbers this year and next?",
        "options": [
            {"text": "Little change this year, then a fall, because the owls "
                     "alive now must raise young on short rations.",
             "correct": True},
            {"text": "A fall this year and a recovery next year, because owls "
                     "breed quickly when food is short.", "correct": False,
             "why": "Breeding needs food, so short rations mean fewer owlets "
                    "rather than more. A population cannot answer within the "
                    "same season either."},
            {"text": "A rise this year, because the surviving voles are "
                     "weaker and easier to catch.", "correct": False,
             "why": "Easier hunting for a few weeks does not add owls. Owl "
                    "numbers can only rise by owls being born and surviving, "
                    "which takes a year."},
            {"text": "No change in either year, because owls live for several "
                     "years and one bad spring is nothing.", "correct": False,
             "why": "One bad spring shows up a year later, in how many young "
                    "survived it. That delay is exactly what makes the two "
                    "lines swing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s07",
        "band": "standard",
        "text": "A wet summer and better soil leave a field with twice as "
                "much grass. A student says the rabbits will now rise without "
                "limit. What is wrong with that?",
        "options": [
            {"text": "Nothing is wrong — with more food there is nothing left "
                     "to hold the rabbits back.", "correct": False,
             "why": "Something still holds them back. A larger food supply "
                    "raises the ceiling rather than removing it, and space "
                    "and disease are limits too."},
            {"text": "More food raises the ceiling, so the rabbits settle at "
                     "a higher number rather than climbing for ever.",
             "correct": True},
            {"text": "More grass makes no difference, because it is the foxes "
                     "that decide how many rabbits there are.",
             "correct": False,
             "why": "Foxes hold the rabbits below the ceiling; the grass "
                    "decides where the ceiling is. Both are at work, and only "
                    "one of them is food."},
            {"text": "More grass would lower rabbit numbers, because the "
                     "foxes would breed on the extra food.", "correct": False,
             "why": "Foxes do not eat grass. More rabbits does mean more "
                    "foxes eventually, and that takes years and still leaves "
                    "more rabbits than before."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s08",
        "band": "standard",
        "text": "Which of these would lower the carrying capacity of a field "
                "for rabbits?",
        "options": [
            {"text": "A pair of foxes moving in from the farm next door.",
             "correct": False,
             "why": "Foxes lower the number of rabbits without moving the "
                    "ceiling. Remove the foxes again and the rabbits climb "
                    "back to the limit the grass sets."},
            {"text": "A mild winter, so that more of last year's young "
                     "survive.", "correct": False,
             "why": "That raises the number of rabbits, at least for a while. "
                    "The ceiling is set by what the field can supply, not by "
                    "how many made it through."},
            {"text": "A long drought that leaves the grass thin and brown all "
                     "summer.", "correct": True},
            {"text": "A wet summer that keeps the grass growing well into the "
                     "autumn.", "correct": False,
             "why": "That raises the ceiling rather than lowering it. More "
                    "food means the field can support more rabbits than "
                    "before."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s09",
        "band": "standard",
        "text": "Looking at twenty years of fox and rabbit numbers, a student "
                "writes: “the foxes control the rabbits”. What is missing "
                "from that?",
        "options": [
            {"text": "Nothing — the foxes eat the rabbits, so the foxes are "
                     "in control.", "correct": False,
             "why": "That is half the story. The rabbits decide how many "
                    "foxes there can be, because rabbits are what the foxes "
                    "eat."},
            {"text": "That the foxes do not control the rabbits at all, since "
                     "only the grass does.", "correct": False,
             "why": "The grass sets the ceiling and the foxes hold the "
                    "rabbits below it. Both are acting, which is why the "
                    "numbers swing rather than settling."},
            {"text": "That the rabbits control the grass, which is the real "
                     "cause of the cycle.", "correct": False,
             "why": "Grazing does affect the grass, and it is not the missing "
                    "half. What is missing is that the control runs both ways "
                    "between the two animals."},
            {"text": "That the rabbits control the foxes as well — each "
                     "population limits the other.", "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b9-02-h05",
        "band": "harder",
        "text": "Twenty-nine reindeer were released on an island of deep "
                "lichen with no predators. The herd reached about six "
                "thousand in under twenty years, then crashed to fewer than "
                "fifty in two winters. Which explanation fits?",
        "options": [
            {"text": "They bred until they ran out of space, and the "
                     "crowding itself killed them.", "correct": False,
             "why": "Space alone did not do it. What ran out was the lichen, "
                    "and a herd that has eaten its food supply starves "
                    "whatever room it has."},
            {"text": "A predator must have reached the island, because a "
                     "population does not crash without one.", "correct": False,
             "why": "Nothing hunted them. A population that overshoots what "
                    "its food can support crashes on its own, and a hard "
                    "winter finishes it."},
            {"text": "The herd grew past what the lichen could support and "
                     "stripped it, so the ceiling itself fell.",
             "correct": True},
            {"text": "The herd reached the island's carrying capacity and "
                     "settled there, and a hard winter then killed most of "
                     "them.", "correct": False,
             "why": "A herd at the ceiling stops climbing; this one climbed "
                    "straight past it. Overshooting is why there was no food "
                    "left when the winter came."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h06",
        "band": "harder",
        "text": "One biologist says a moose population is limited by the "
                "wolves that hunt it. Another says it is limited by how much "
                "willow there is to browse. Both study the same herd. How can "
                "both be right?",
        "options": [
            {"text": "Both limits act at once — the wolves hold the herd "
                     "below a ceiling that the willow sets.", "correct": True},
            {"text": "They cannot both be right, so one of them has measured "
                     "the herd wrongly.", "correct": False,
             "why": "Nothing here needs a wrong measurement. A population can "
                    "be pressed down by predators and capped by food at the "
                    "same time."},
            {"text": "Both are right because moose eat willow and wolves eat "
                     "moose, so the willow limits the wolves too.",
             "correct": False,
             "why": "Willow does reach the wolves through the moose, and that "
                    "is a different claim. The question is what limits the "
                    "moose, and two things do."},
            {"text": "Only the wolves limit the herd, since a hunted "
                     "population never reaches its food limit.",
             "correct": False,
             "why": "Hunted populations do run short of food, especially in a "
                    "hard winter. Which limit bites hardest changes from year "
                    "to year."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h07",
        "band": "harder",
        "text": "Cod eat capelin, a small shoaling fish. Heavy fishing "
                "crashes the cod. Capelin numbers rise, and yet the cod do "
                "not recover for decades. Why does the usual cycle not bring "
                "them back?",
        "options": [
            {"text": "Because the capelin have taken the cod's place at the "
                     "top of the chain.", "correct": False,
             "why": "Capelin eat plankton and are eaten themselves, and "
                    "nothing about where they feed has changed. Taking a "
                    "place in a chain is not something a prey fish can do."},
            {"text": "Because a population that has crashed can never rebuild "
                     "itself.", "correct": False,
             "why": "A crashed population usually can rebuild — that is step "
                    "four of the cycle. What is different here is that "
                    "something outside the cycle is still removing cod."},
            {"text": "Because there is now too much food, and a population "
                     "cannot grow when its food is too plentiful.",
             "correct": False,
             "why": "Plenty of food is the condition under which a predator "
                    "population grows. Too much food is not something that "
                    "holds numbers down."},
            {"text": "Because the fishing goes on whatever the cod numbers "
                     "are, so the pressure never eases as a predator's "
                     "would.", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h08",
        "band": "harder",
        "text": "A student says that because predator and prey numbers always "
                "recover, no predator can ever wipe out its prey. What is the "
                "best reply?",
        "options": [
            {"text": "That is right, and it is why foxes and rabbits are both "
                     "still here after thousands of years.", "correct": False,
             "why": "It holds where one predator depends on one prey and "
                    "nothing else. Change that and the recovery can fail."},
            {"text": "A predator with other food to fall back on does not go "
                     "hungry as its prey runs out.", "correct": True},
            {"text": "It is true of wild animals but not of people, who can "
                     "decide to hunt something to extinction.",
             "correct": False,
             "why": "People are the clearest case and not the only one. Any "
                    "predator with an alternative food can go on hunting a "
                    "scarce prey without starving."},
            {"text": "It is wrong, because a prey population that falls low "
                     "enough always dies out.", "correct": False,
             "why": "Low numbers are dangerous and not fatal in themselves — "
                    "the rabbits recover from very few. What breaks the "
                    "recovery is hunting that does not ease off."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h09",
        "band": "harder",
        "text": "A long record shows hare numbers peaking in 1985, 1995 and "
                "2005, and lynx numbers peaking in 1987, 1997 and 2007. What "
                "do those dates show?",
        "options": [
            {"text": "A cycle of about ten years, with the lynx peak two "
                     "years behind because breeding takes time.",
             "correct": True},
            {"text": "A cycle of about two years, since that is the gap "
                     "between a hare peak and a lynx peak.", "correct": False,
             "why": "Two years is the lag between the two lines, not the "
                    "length of the cycle. The cycle is the gap between one "
                    "hare peak and the next."},
            {"text": "A cycle of about ten years, with the hares following "
                     "the lynx, since predators drive the numbers.",
             "correct": False,
             "why": "Read the dates: each hare peak comes first and each lynx "
                    "peak follows it. Predators cannot increase before there "
                    "has been plenty to eat."},
            {"text": "No cycle at all, because three peaks in twenty years is "
                     "too few to show a pattern.", "correct": False,
             "why": "Three peaks evenly spaced ten years apart, in two "
                    "species at once, is a pattern — and it is the one that "
                    "made these records famous."},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · easier ─────────────────────────────────────────
    {
        "id": "b9-02-e10",
        "band": "easier",
        "text": "In biology, which of these is what the word predator "
                "means?",
        "options": [
            {"text": "An animal that hunts and eats other animals",
             "correct": True},
            {"text": "An animal that eats more than its fair share of the food supply",
             "correct": False,
             "why": "Appetite is not the test. A predator is named for "
                    "hunting other animals, not for how much it eats."},
            {"text": "The largest animal living in an ecosystem",
             "correct": False,
             "why": "Size decides nothing. A ladybird hunts aphids and is one "
                    "of the smallest animals in a wood."},
            {"text": "An animal with no natural enemies of its own",
             "correct": False,
             "why": "That describes a top predator. A stoat is hunted by owls "
                    "and is still a predator of voles."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e11",
        "band": "easier",
        "text": "Rabbits in a field are unusually plentiful this year. What "
                "happens to the fox population over the next few years?",
        "options": [
            {"text": "It falls, because so many rabbits crowd the foxes out "
                     "of the best ground", "correct": False,
             "why": "Rabbits do not crowd foxes out. Plenty of prey is the "
                    "easiest time a fox population ever has."},
            {"text": "It rises, because well-fed foxes raise more cubs that "
                     "survive", "correct": True},
            {"text": "It stays the same, since fox numbers are fixed by the "
                     "size of the field they live in", "correct": False,
             "why": "Area does not fix a predator's numbers. The food supply "
                    "does, and it has just improved."},
            {"text": "It doubles within the year", "correct": False,
             "why": "Nothing happens within the year. Cubs have to be born "
                    "and survive a winter first."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e12",
        "band": "easier",
        "text": "Several things together set how large a rabbit population a "
                "field can support. Which list is right?",
        "options": [
            {"text": "The number of foxes and nothing else", "correct": False,
             "why": "Predators hold a population below its limit. The limit "
                    "itself is set by what the field supplies."},
            {"text": "The weather in the year the rabbits were born",
             "correct": False,
             "why": "One year's weather changes the numbers, and the ceiling "
                    "is set by what the land can supply year after year."},
            {"text": "Food, water, space and disease", "correct": True},
            {"text": "The area of the field, measured in hectares",
             "correct": False,
             "why": "Two fields of equal area can support quite different "
                    "numbers, depending on what grows on them."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e13",
        "band": "easier",
        "text": "Which of these pairs names a predator and then its prey?",
        "options": [
            {"text": "A rabbit and the grass it grazes", "correct": False,
             "why": "Grass is a plant, so the rabbit is a plant-eater rather "
                    "than a predator."},
            {"text": "An aphid and the oak sap it drinks", "correct": False,
             "why": "Sap comes from a producer. An aphid is a primary "
                    "consumer, not a hunter."},
            {"text": "A fungus and the dead leaf it feeds on", "correct": False,
             "why": "A dead leaf is not prey and a fungus does not hunt. That "
                    "is a decomposer at work."},
            {"text": "A barn owl and the mouse it catches", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e14",
        "band": "easier",
        "text": "Lynx and snowshoe hare numbers in Canada rise and fall on a "
                "regular cycle. About how long is one full turn of it?",
        "options": [
            {"text": "About ten years", "correct": True},
            {"text": "About one year", "correct": False,
             "why": "A year is one breeding season. A full turn takes many "
                    "breeding seasons to work through."},
            {"text": "About a hundred years", "correct": False,
             "why": "The records cover two centuries and show about twenty "
                    "turns in them, not two."},
            {"text": "About three months", "correct": False,
             "why": "Populations cannot change that fast. Animals have to be "
                    "born and raised before numbers move."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e15",
        "band": "easier",
        "text": "The famous Canadian lynx and hare records come from a fur "
                "company's account books. What did those books actually count?",
        "options": [
            {"text": "Animals counted by scientists walking the forest",
             "correct": False,
             "why": "No scientist collected these. They are a company's "
                    "trading records, kept for business."},
            {"text": "Pelts brought in by trappers each year", "correct": True},
            {"text": "Lynx and hares photographed at feeding stations",
             "correct": False,
             "why": "The records are two centuries old and are written "
                    "trading figures, not observations of live animals."},
            {"text": "Every animal born in the forest that year",
             "correct": False,
             "why": "Nobody could count births across Canada. What was "
                    "counted was what came in for sale."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e16",
        "band": "easier",
        "text": "Two populations rise and fall, over and over, in the same "
                "order each time. What is that pattern called?",
        "options": [
            {"text": "A migration", "correct": False,
             "why": "Migration is animals moving from place to place. Nothing "
                    "here has moved anywhere."},
            {"text": "An extinction", "correct": False,
             "why": "Extinction is a population reaching zero and staying "
                    "there. These populations recover each time."},
            {"text": "A cycle", "correct": True},
            {"text": "A ceiling", "correct": False,
             "why": "A ceiling is the largest number an environment can "
                    "support. It is a limit, not a repeating pattern."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e17",
        "band": "easier",
        "text": "A farmer sows extra clover across his pasture and puts in a "
                "second water trough. What effect does that have on the "
                "number of rabbits the land can support?",
        "options": [
            {"text": "It falls, because clover is poor food for a rabbit",
             "correct": False,
             "why": "Clover is good rabbit food. More of it means more "
                    "rabbits can be fed, not fewer."},
            {"text": "Nothing changes, because rabbit numbers are set by the "
                     "foxes", "correct": False,
             "why": "Predators hold a population below its limit. Improving "
                    "the food and water moves the limit itself."},
            {"text": "The number rises, because more food and water raises "
                     "the limit", "correct": True},
            {"text": "It rises without limit from now on", "correct": False,
             "why": "There is still a limit — it is simply a higher one. "
                    "Space and disease have not gone away."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e18",
        "band": "easier",
        "text": "Rabbits are plentiful in a field one spring. What is the "
                "most likely effect on the fox cubs born that year?",
        "options": [
            {"text": "More of them survive their first winter", "correct": True},
            {"text": "Fewer are born, because the vixens are too well fed to "
                     "breed", "correct": False,
             "why": "Good feeding makes breeding more likely, not less. A "
                    "well-fed vixen raises more cubs, not fewer."},
            {"text": "They leave the field to hunt somewhere with less "
                     "competition", "correct": False,
             "why": "Animals move away from shortage, not from plenty. A "
                    "field full of rabbits is where a fox wants to be."},
            {"text": "They become hunters only in their second year",
             "correct": False,
             "why": "Cubs hunt from their first year. What takes time is the "
                    "POPULATION growing, not one animal learning."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e19",
        "band": "easier",
        "text": "A model of one field runs on two rules only: rabbits breed "
                "and are eaten, foxes eat and die. It has no weather, disease "
                "or migration in it. What does that make it?",
        "options": [
            {"text": "A record of a real field, measured over many years",
             "correct": False,
             "why": "Nothing here has been measured. Two rules were chosen "
                    "and the arithmetic was run forward."},
            {"text": "A simplified model, built to show one idea clearly",
             "correct": True},
            {"text": "A wrong model, since anything left out makes it false",
             "correct": False,
             "why": "Every model leaves things out. That is what makes it a "
                    "model rather than the world."},
            {"text": "A prediction of what a real field will do next year",
             "correct": False,
             "why": "It predicts no real field. It shows why a delay produces "
                    "a cycle, which is a different job."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e20",
        "band": "easier",
        "text": "Fox numbers in a wood fall to just a few animals. Why can "
                "the population still recover?",
        "options": [
            {"text": "Foxes can live on plants until prey returns",
             "correct": False,
             "why": "What lets them recover is the prey becoming plentiful, "
                    "not a change of diet."},
            {"text": "New foxes appear once the rabbits are numerous enough", "correct": False,
             "why": "Animals do not appear. The few foxes still there breed, "
                    "and more of their cubs now survive."},
            {"text": "A few breeding pairs are left, and prey is now "
                     "plentiful", "correct": True},
            {"text": "Rabbits turn into foxes as the years go on",
             "correct": False,
             "why": "One species never becomes another. The rabbits are the "
                    "food that lets fox cubs survive."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e21",
        "band": "easier",
        "text": "Rabbits can raise several litters in a year, while a vixen "
                "raises one. What does that difference mean for the two "
                "populations?",
        "options": [
            {"text": "Rabbit numbers end up higher but change more slowly",
             "correct": False,
             "why": "Fast breeding makes numbers change FASTER. That is the "
                    "whole point of the difference."},
            {"text": "Fox numbers change faster, because there are fewer of "
                     "them to count", "correct": False,
             "why": "Having fewer animals does not make a population quicker "
                    "to respond. Breeding rate does."},
            {"text": "The two populations change at exactly the same speed",
             "correct": False,
             "why": "They plainly do not. One can multiply several times in a "
                    "season and the other once."},
            {"text": "The rabbit population responds to a change more quickly",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e22",
        "band": "easier",
        "text": "Rabbit numbers in a field have climbed to the ceiling the "
                "land can support. What is the grass in that field like?",
        "options": [
            {"text": "Grazed short, with not enough to go round",
             "correct": True},
            {"text": "Long and thick, because the rabbits cannot keep up",
             "correct": False,
             "why": "The ceiling is reached precisely when the grazing "
                    "catches up with the growth."},
            {"text": "Unchanged, because grass regrows as fast as it is eaten",
             "correct": False,
             "why": "Grass regrows at a limited rate, and that rate is what "
                    "sets the ceiling in the first place."},
            {"text": "Replaced by other plants the rabbits prefer",
             "correct": False,
             "why": "Heavy grazing removes what the rabbits prefer. It does "
                    "not summon better food."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e23",
        "band": "easier",
        "text": "Two things have to be true together before a predator "
                "population can grow. Which pair is right?",
        "options": [
            {"text": "Warm weather, and prey that cannot run fast",
             "correct": False,
             "why": "Neither is needed. Predator numbers climb whenever prey "
                    "is plentiful and there has been time to breed."},
            {"text": "Plenty of prey, and time for the young to be raised",
             "correct": True},
            {"text": "Plenty of prey, and no other predator in the area",
             "correct": False,
             "why": "Several predators share prey in most ecosystems and all "
                    "of their populations still rise in a good year."},
            {"text": "A large area, and prey that breeds slowly",
             "correct": False,
             "why": "Slow-breeding prey is a worse food supply, not a better "
                    "one. Area alone supplies no food."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e24",
        "band": "easier",
        "text": "Fox numbers in a field have just reached their highest "
                "point. What are the rabbits doing at that moment?",
        "options": [
            {"text": "Climbing, because there are now plenty of foxes to feed "
                     "on", "correct": False,
             "why": "The arrows run the other way. Foxes eat rabbits, so more "
                    "foxes is bad news for rabbits."},
            {"text": "Peaking as well, since the two populations move "
                     "together", "correct": False,
             "why": "The two peaks never coincide. The predator's peak comes "
                    "after the prey's has passed."},
            {"text": "They are scarce, and still falling", "correct": True},
            {"text": "Holding steady at their ceiling", "correct": False,
             "why": "A population under the heaviest hunting pressure of the "
                    "cycle is nowhere near its ceiling."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e25",
        "band": "easier",
        "text": "A chart of a field draws its rabbit numbers and its fox "
                "numbers on two separate scales. Why is that done?",
        "options": [
            {"text": "Because rabbits and foxes are counted in different "
                     "units", "correct": False,
             "why": "Both are counted as animals. Only the sizes of the two "
                    "numbers differ."},
            {"text": "Because the chart would otherwise take up too much room "
                     "on the page", "correct": False,
             "why": "The chart is the same size either way. What changes is "
                    "whether the smaller line can be read."},
            {"text": "Because the rabbits are counted yearly and the foxes "
                     "monthly", "correct": False,
             "why": "Both are counted once a year. It is the size of the "
                    "numbers, not their timing, that differs."},
            {"text": "Because the foxes are so few that one scale would "
                     "flatten their line", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e26",
        "band": "easier",
        "text": "Snowshoe hares feed on shoots and twigs. What happens to "
                "that food in the years just after a hare peak?",
        "options": [
            {"text": "It is stripped bare and takes years to grow back",
             "correct": True},
            {"text": "It grows back thicker, because grazing encourages it",
             "correct": False,
             "why": "Light grazing can, and the stripping that follows a peak "
                    "is far heavier than that."},
            {"text": "It is unaffected, because hares eat only what falls",
             "correct": False,
             "why": "Hares browse living shoots and twigs directly from the "
                    "plants, which is why the plants suffer."},
            {"text": "It is replaced by grass within a season", "correct": False,
             "why": "Shrubs do not become grass. The shoots regrow slowly on "
                    "the same plants."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e27",
        "band": "easier",
        "text": "A model of one field with two species and no weather in it "
                "is built for a particular purpose. What is that purpose?",
        "options": [
            {"text": "To replace the need for anyone to study a real field",
             "correct": False,
             "why": "Models point at what to look for in real fields. They "
                    "never stand in for the looking."},
            {"text": "To show why a delay between the two produces a cycle",
             "correct": True},
            {"text": "To predict how many rabbits a named farm will be holding "
                     "next spring", "correct": False,
             "why": "No model this simple can do that. The things it leaves "
                    "out are exactly the ones a real farm has."},
            {"text": "To prove that foxes control rabbit numbers by "
                     "themselves", "correct": False,
             "why": "It shows the opposite as well — the grass sets a ceiling "
                    "even with every fox removed."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e28",
        "band": "easier",
        "text": "Hares living under heavy pressure from lynx raise fewer "
                "young than hares that are not. What does that add to the "
                "picture of a predator and its prey?",
        "options": [
            {"text": "It shows the lynx are not really hunting the hares",
             "correct": False,
             "why": "They hunt them and they always did. This is an effect "
                    "ON TOP of the hunting."},
            {"text": "It shows hares choose when to breed and when not",
             "correct": False,
             "why": "Nothing is chosen. Animals under pressure and short of "
                    "food simply raise fewer young."},
            {"text": "A predator changes prey numbers by more than the ones "
                     "it catches", "correct": True},
            {"text": "It shows the hare cycle has nothing to do with lynx",
             "correct": False,
             "why": "This is one more way the lynx affect the hares, not a "
                    "reason to say they do not."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e29",
        "band": "easier",
        "text": "At every point of a predator and prey cycle, one of the two "
                "populations is much larger than the other. Which?",
        "options": [
            {"text": "The predators, because they live longer than their prey",
             "correct": False,
             "why": "Length of life does not decide numbers. The food supply "
                    "does, and there is far less of it higher up."},
            {"text": "It changes from one part of the cycle to the other",
             "correct": False,
             "why": "Both rise and fall, and the prey stay far the more "
                    "numerous throughout."},
            {"text": "Neither — they are about equal all the way round",
             "correct": False,
             "why": "A field with as many foxes as rabbits could not feed the "
                    "foxes for a week."},
            {"text": "The prey", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-e30",
        "band": "easier",
        "text": "A student asks whether anything is managing the rise and "
                "fall of the foxes and rabbits in a field. What is the answer?",
        "options": [
            {"text": "The foxes manage it, by leaving enough rabbits to breed",
             "correct": False,
             "why": "No animal holds back for the future. A fox takes what it "
                    "can catch."},
            {"text": "The rabbits manage it, by breeding harder when foxes "
                     "are many", "correct": False,
             "why": "Rabbits under heavy pressure raise fewer young, not "
                    "more. Nothing about this is planned."},
            {"text": "Nothing is — it follows from how each affects the other",
             "correct": True},
            {"text": "The weather manages it, by killing the surplus each "
                     "winter", "correct": False,
             "why": "Weather disturbs the pattern; it does not create it. The "
                    "cycle appears in a model with no weather in it."},
        ],
        "figure": None,
    },

    # ── MRB-338 top-up · standard ───────────────────────────────────────
    {
        "id": "b9-02-s10",
        "band": "standard",
        "text": "Two fields hold the same grass and the same number of foxes. "
                "One has thick bramble the rabbits can shelter in and the "
                "other is bare. Which field holds more rabbits, and why?",
        "options": [
            {"text": "The bare field, because rabbits can see the foxes "
                     "coming across it", "correct": False,
             "why": "Seeing a fox is little help with nowhere to go. Cover is "
                    "what turns a chase into an escape."},
            {"text": "The bramble field, because fewer are caught, so the "
                     "population sits higher", "correct": True},
            {"text": "The bare field, because bramble takes up space that "
                     "would otherwise be growing grass", "correct": False,
             "why": "A little lost grazing is a small price beside the "
                    "hunting pressure the cover removes."},
            {"text": "Both hold the same, because the grass is the same",
             "correct": False,
             "why": "Grass sets the ceiling. How close a population sits to "
                    "that ceiling depends on how hard it is hunted."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s11",
        "band": "standard",
        "text": "A reserve wants more of a rare bird of prey. Which action is "
                "most likely to raise its numbers over the next few years?",
        "options": [
            {"text": "Releasing more of the birds into it every spring, year "
                     "after year", "correct": False,
             "why": "Released birds need feeding too. Without more prey the "
                    "reserve simply cannot hold more of them."},
            {"text": "Fencing the reserve so that no bird can leave it",
             "correct": False,
             "why": "A fence keeps nothing in for a bird, and would not "
                    "change how much food there is."},
            {"text": "Managing the land so that its prey animals become more "
                     "numerous", "correct": True},
            {"text": "Feeding the adult birds through the winter each year",
             "correct": False,
             "why": "Winter feeding helps individuals through one season. "
                    "Numbers still settle at what the land can supply."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s12",
        "band": "standard",
        "text": "Explain why a predator and prey cycle keeps swinging instead "
                "of quickly settling at two steady numbers.",
        "options": [
            {"text": "Because the predators deliberately leave some prey "
                     "uneaten each year", "correct": False,
             "why": "Nothing is deliberate. The swing comes out of the "
                    "arithmetic on its own."},
            {"text": "Because the prey population grows faster than any "
                     "arithmetic could settle", "correct": False,
             "why": "Fast growth is part of it; the swing needs the DELAY in "
                    "the predator's response as well."},
            {"text": "Because each population answers the other only after a "
                     "delay, so it overshoots", "correct": True},
            {"text": "Because the weather changes every year", "correct": False,
             "why": "The swing appears in a model with no weather in it at "
                    "all, so weather cannot be the cause."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s13",
        "band": "standard",
        "text": "A student drew this graph of the owl and vole populations in "
                "a wood. What is wrong with it?",
        "options": [
            {"text": "Owls should be far fewer than the voles they live on",
             "correct": True},
            {"text": "The two lines ought to cross at least once every year of "
                     "the record", "correct": False,
             "why": "Nothing says the lines must cross. On one scale the "
                    "predator line simply stays lower."},
            {"text": "The owl line should be flat, because owls do not cycle",
             "correct": False,
             "why": "Owl numbers follow their prey up and down like any "
                    "predator's, and this graph is right to show that."},
            {"text": "The vole line should be above only in summer",
             "correct": False,
             "why": "Voles outnumber owls in every season. This is not a "
                    "seasonal effect."},
        ],
        "figure": "b9-owl-vole-graph-wrong",
    },
    {
        "id": "b9-02-s14",
        "band": "standard",
        "text": "In a model where foxes eat rabbits and nothing else, fox "
                "numbers crash when rabbits become scarce. Explain why a real "
                "fox population would fall less steeply.",
        "options": [
            {"text": "Real foxes hibernate through a shortage and lose "
                     "nothing", "correct": False,
             "why": "Foxes do not hibernate. They go on needing food all "
                    "winter."},
            {"text": "Real foxes have other food — voles, birds, beetles, "
                     "fruit — to turn to", "correct": True},
            {"text": "Real foxes breed faster when their food runs short",
             "correct": False,
             "why": "Hungry animals raise fewer young, not more. Breeding "
                    "falls away with the food."},
            {"text": "Real rabbits never become as scarce as a model makes "
                     "them", "correct": False,
             "why": "Real rabbit populations crash hard after disease. The "
                    "difference is on the fox's side of the pair."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s15",
        "band": "standard",
        "text": "Two identical fields are stocked differently: one starts "
                "with 40 foxes and the other with 200. After twenty years "
                "both hold about the same numbers. What does that show?",
        "options": [
            {"text": "That the starting numbers were miscounted",
             "correct": False,
             "why": "Nothing was miscounted. A population that starts too "
                    "high simply eats its way down to what the field holds."},
            {"text": "That foxes move between the two fields until the "
                     "numbers match", "correct": False,
             "why": "The fields are separate, and the result appears in a "
                    "model with no movement in it at all."},
            {"text": "The numbers settle at what the field supports, not at "
                     "where they started", "correct": True},
            {"text": "That twenty years is too long a period to measure "
                     "anything useful over", "correct": False,
             "why": "Twenty years is two full turns of a cycle, which is what "
                    "makes the comparison possible."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s16",
        "band": "standard",
        "text": "Two islands hold the same rabbits and foxes, but one "
                "island's grass grows twice as fast. Predict how the two "
                "cycles differ.",
        "options": [
            {"text": "The grassier island's cycle disappears, because there "
                     "is always plenty for them to eat", "correct": False,
             "why": "More grass raises the ceiling. It does nothing to the "
                    "delay in the fox's response, which is what cycles."},
            {"text": "The grassier island's foxes die out, because the "
                     "rabbits can always escape", "correct": False,
             "why": "More rabbits is more fox food. A better-fed rabbit "
                    "population supports more foxes, not fewer."},
            {"text": "The two cycles are identical, since the grass is not one "
                     "of the pair", "correct": False,
             "why": "Grass sets the ceiling the rabbits climb towards, so it "
                    "sets the height of the whole cycle."},
            {"text": "The grassier island cycles around higher numbers of "
                     "both", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s17",
        "band": "standard",
        "text": "In one year a wood holds the most owls it has had for a "
                "decade, while the vole population has already been falling "
                "for a year. Explain how both can be true at once.",
        "options": [
            {"text": "The owls born in the good years are still alive and "
                     "breeding", "correct": True},
            {"text": "The owls must have moved in from a neighbouring wood "
                     "that year", "correct": False,
             "why": "Movement is not needed. The same pattern appears in a "
                    "model where nothing can move in or out."},
            {"text": "Owls stop eating voles once vole numbers begin to fall",
             "correct": False,
             "why": "They hunt harder, not less. It is the number of OWLS "
                    "that takes time to respond."},
            {"text": "The vole count for that year must be wrong",
             "correct": False,
             "why": "It fits the cycle exactly. A predator's peak arriving "
                    "after its prey's is the ordinary pattern."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s18",
        "band": "standard",
        "text": "Lime is spread on poor pasture and the grass grows much "
                "thicker from the following spring. What happens to the "
                "number of foxes the land can carry, and when?",
        "options": [
            {"text": "It falls, because thick grass hides the rabbits from "
                     "the foxes", "correct": False,
             "why": "Cover helps rabbits a little, and far more rabbits "
                    "overall is a much larger gain for the foxes."},
            {"text": "It rises within the same spring, as soon as the grass "
                     "is thicker", "correct": False,
             "why": "Grass does not feed foxes. The rabbits have to become "
                    "numerous first, and then the cubs have to survive."},
            {"text": "It rises, but only after the rabbit population has "
                     "grown", "correct": True},
            {"text": "It does not change, because foxes do not eat grass",
             "correct": False,
             "why": "They do not, and their food does. Everything a fox eats "
                    "was grass a step earlier."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s19",
        "band": "standard",
        "text": "Rabbits can raise several litters a year and foxes one. "
                "Explain what that difference does to the shape of the cycle.",
        "options": [
            {"text": "It flattens the cycle, because one population can "
                     "always keep up with the other", "correct": False,
             "why": "It is the MISMATCH in speed that makes the swing. Equal "
                    "speeds would damp it, not sharpen it."},
            {"text": "It removes the cycle, because the rabbits can outbreed "
                     "any number of foxes", "correct": False,
             "why": "They cannot outbreed a peak fox population — that is "
                    "exactly when rabbit numbers turn downwards."},
            {"text": "The rabbits turn quickly and the foxes slowly, which "
                     "creates the lag", "correct": True},
            {"text": "It makes the fox peak arrive before the rabbit peak",
             "correct": False,
             "why": "Slow breeding puts the fox peak LATER, never earlier. "
                    "The food has to come first."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s20",
        "band": "standard",
        "text": "A farmer counts foxes every January. His count rises for "
                "three years and then falls for three, and then begins to "
                "rise again. What is he most likely watching?",
        "options": [
            {"text": "A steady decline, interrupted by one good spell",
             "correct": False,
             "why": "A decline does not return to where it began. These "
                    "numbers have come back round."},
            {"text": "A counting error of his that repeats itself every three "
                     "years", "correct": False,
             "why": "An error that rises and falls smoothly over six years is "
                    "not an error, it is a pattern."},
            {"text": "The foxes slowly running out of space on his land",
             "correct": False,
             "why": "Running out of space would hold the numbers at a limit, "
                    "not bring them back down and up again."},
            {"text": "One turn of a predator and prey cycle", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s21",
        "band": "standard",
        "text": "A computer model of a field will not let the fox number fall "
                "below one animal. Suggest why that limit is built in.",
        "options": [
            {"text": "Below one animal there is no pair left to breed from",
             "correct": True},
            {"text": "A model cannot work with numbers smaller than one", "correct": False,
             "why": "A model handles fractions perfectly well. The reason is "
                    "biological, not arithmetical."},
            {"text": "Foxes are protected and may not be removed from a model "
                         "like this", "correct": False,
             "why": "Protection is a law about real animals. It has no "
                    "bearing on what a model may calculate."},
            {"text": "The rabbits would otherwise rise for ever",
             "correct": False,
             "why": "The grass ceiling stops the rabbits, with or without a "
                    "single fox left."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s22",
        "band": "standard",
        "text": "A chart shows rabbits and foxes on separate scales. A "
                "student says that hides how few foxes there really are. Is "
                "he right?",
        "options": [
            {"text": "No — the scales are the same, and he has misread the "
                     "axis", "correct": False,
             "why": "The scales genuinely do differ, and the chart says so. "
                    "His observation is correct as far as it goes."},
            {"text": "Yes in that sense, and separate scales are what make "
                     "the timing readable", "correct": True},
            {"text": "Yes, and the chart should therefore be redrawn on one "
                     "scale", "correct": False,
             "why": "On one scale the fox line flattens into the axis and the "
                    "lag — the point of the chart — cannot be seen."},
            {"text": "No, because the numbers are printed beside each bar",
             "correct": False,
             "why": "Printed numbers would not change what the picture "
                    "suggests at a glance, which is his real point."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s23",
        "band": "standard",
        "text": "A model of a field is altered so that the grass supply is "
                "unlimited. Every fox is then removed. Predict what the "
                "rabbit line does.",
        "options": [
            {"text": "It falls, because the rabbits have nothing to compete "
                     "against", "correct": False,
             "why": "Competition does not keep a population up. Removing the "
                    "predator and the food limit removes both brakes."},
            {"text": "It rises and then levels off at a ceiling",
             "correct": False,
             "why": "The ceiling was the grass, and the grass is now "
                    "unlimited. Nothing is left to level it off."},
            {"text": "It climbs and goes on climbing without limit",
             "correct": True},
            {"text": "It stays exactly where it was when the foxes went",
             "correct": False,
             "why": "With nothing eating them and food to spare, rabbits "
                    "breed and the number moves."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s24",
        "band": "standard",
        "text": "A lynx and hare cycle takes about ten years to come round. "
                "Suggest why such a cycle is measured in years rather than in "
                "weeks.",
        "options": [
            {"text": "Because trappers only visited the forest once a year",
             "correct": False,
             "why": "The record's timing is not the cycle's. A weekly record "
                    "would show the same ten-year pattern."},
            {"text": "Because snow makes the forest impossible to work in for "
                     "much of the year", "correct": False,
             "why": "Access affects the record, not the animals. The "
                    "populations move at the speed they breed."},
            {"text": "Because a population can only change as fast as its "
                     "animals can breed", "correct": True},
            {"text": "Because ecologists agreed to use years for every "
                     "population study", "correct": False,
             "why": "The unit is not a convention. Some populations really do "
                    "cycle in weeks — those of animals that breed in days."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s25",
        "band": "standard",
        "text": "A student says predators and prey 'balance each other "
                "perfectly'. Suggest a better description of what the numbers "
                "actually do.",
        "options": [
            {"text": "They overshoot and undershoot, chasing each other round",
             "correct": True},
            {"text": "They hold steady, apart from the years when the weather "
                     "interferes with them", "correct": False,
             "why": "The swing appears in a model with no weather. Steadiness "
                    "is not the resting state."},
            {"text": "They rise together and fall together, in step",
             "correct": False,
             "why": "They rise and fall in the same ORDER every time, one "
                    "behind the other, which is not in step."},
            {"text": "They drift apart until one of the two dies out",
             "correct": False,
             "why": "Neither dies out. Each shortage eases the pressure on "
                    "the other and the pattern comes round again."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s26",
        "band": "standard",
        "text": "A hard winter kills most of a field's rabbits, and fox "
                "numbers that year are unchanged. A student says this proves "
                "the cycle model wrong. Evaluate that.",
        "options": [
            {"text": "It does prove it wrong, because the foxes should have "
                     "fallen at once", "correct": False,
             "why": "The model says the opposite: a predator's numbers "
                    "respond a year or more after its food does."},
            {"text": "It does not — the model leaves weather out, and says so",
             "correct": True},
            {"text": "It does prove it wrong, because weather cannot affect a "
                     "population", "correct": False,
             "why": "Weather affects populations heavily. That is exactly why "
                    "leaving it out is a stated limit of the model."},
            {"text": "It cannot be judged without knowing the grass yield "
                     "that year", "correct": False,
             "why": "The grass would matter for the ceiling. What settles "
                    "this is that the model never claimed to cover weather."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s27",
        "band": "standard",
        "text": "Hares living where lynx are numerous raise fewer young than "
                "hares living where lynx are scarce. What does that add to a "
                "picture in which predators simply catch prey?",
        "options": [
            {"text": "It shows the hares are choosing to breed less until the "
                     "danger passes", "correct": False,
             "why": "Nothing is chosen. Animals that are short of food and "
                    "under stress raise fewer young."},
            {"text": "A predator can lower prey numbers without catching "
                     "those animals at all", "correct": True},
            {"text": "It shows that the lynx must be eating the young hares "
                     "before anyone can count them", "correct": False,
             "why": "That would be catching them. The point here is that "
                    "fewer are BORN in the first place."},
            {"text": "It shows the hare cycle is really about the weather",
             "correct": False,
             "why": "The effect is measured against how many lynx there are, "
                    "which is not a weather measurement."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s28",
        "band": "standard",
        "text": "An ecologist studying a population cycle says she would "
                "rather have fifty years of counts than five. Suggest why.",
        "options": [
            {"text": "Counts become more accurate the longer they go on for", "correct": False,
             "why": "A count is as accurate as the method. Length gives you "
                    "more turns of the pattern, not better counting."},
            {"text": "A fifty-year record is easier to publish than a short one", "correct": False,
             "why": "Publication is not the reason. Five years cannot show "
                    "whether a rise comes round again."},
            {"text": "One turn takes about ten years, so five cannot show a "
                     "pattern", "correct": True},
            {"text": "Populations only begin to cycle after a few decades of "
                         "being watched", "correct": False,
             "why": "Watching changes nothing. The cycle runs whether anyone "
                    "is counting or not."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s29",
        "band": "standard",
        "text": "A field's rabbit peak is twice as high one decade as it was "
                "the last, but the fox peak that follows is only slightly "
                "higher. Suggest why.",
        "options": [
            {"text": "Foxes can only breed so fast, whatever the food supply",
             "correct": True},
            {"text": "The extra rabbits were of a kind foxes do not eat",
             "correct": False,
             "why": "A rabbit is a rabbit. Nothing about a larger population "
                    "changes what it is made of."},
            {"text": "The foxes must have been counted in a different way "
                     "that decade", "correct": False,
             "why": "A change of method would be an odd coincidence. A limit "
                    "on breeding explains it without one."},
            {"text": "Twice the food always gives exactly twice the predators "
                     "again in the end", "correct": False,
             "why": "That is what the figures refuse. Breeding rate puts a "
                    "ceiling on how fast a peak can be answered."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-s30",
        "band": "standard",
        "text": "A long drought kills much of the grass on a hillside "
                "where rabbits graze and foxes hunt them. Predict what "
                "happens to the foxes, and say roughly when.",
        "options": [
            {"text": "Fox numbers fall in the same summer as the grass does",
             "correct": False,
             "why": "Foxes do not eat grass. The shortage has to reach them "
                    "through the rabbits first."},
            {"text": "Fox numbers rise, because weakened rabbits are easier "
                     "to catch", "correct": False,
             "why": "Easy hunting for one season does not outweigh there "
                    "being far fewer rabbits to catch."},
            {"text": "Fox numbers are unchanged, because a drought does not "
                     "reach as far as a predator", "correct": False,
             "why": "It reaches every level, one step at a time. A predator "
                    "is simply the last to feel it."},
            {"text": "Rabbit numbers fall first, and fox numbers follow a "
                     "year or more later", "correct": True},
        ],
        "figure": None,
    },
    # ── MRB-338 top-up · harder ─────────────────────────────────────────
    {
        "id": "b9-02-h10",
        "band": "harder",
        "text": "A forest record shows snowshoe hare numbers cycling "
                "strongly while the lynx line stays almost flat. Suggest the "
                "best explanation.",
        "options": [
            {"text": "The lynx must have been counted by some different method "
                     "in that particular forest", "correct": False,
             "why": "A flat line from a working method is a finding. Blaming "
                    "the method is the last explanation to reach for."},
            {"text": "The lynx have other prey to fall back on, so they track "
                     "the hares less closely", "correct": True},
            {"text": "The hares are not the lynx's prey in that forest",
             "correct": False,
             "why": "Lynx hunt hares wherever both live. Other prey does not "
                    "mean no hares are taken."},
            {"text": "Lynx cannot cycle", "correct": False,
             "why": "They cycle strongly in most of Canada. What varies is "
                    "how tightly they are tied to one food."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h11",
        "band": "harder",
        "text": "In a model of one field the swings get smaller each turn "
                "until the two lines go flat. A student argues that the real "
                "lynx and hare cycle should therefore have flattened "
                "centuries ago. Evaluate that.",
        "options": [
            {"text": "The student is right, and the ten-year record must be "
                     "measuring something quite different from a cycle",
             "correct": False,
             "why": "Two species rising and falling in a fixed order for two "
                    "centuries is a cycle by any reading."},
            {"text": "Real populations are disturbed constantly, and each "
                     "disturbance restarts the swing", "correct": True},
            {"text": "The student is right, and the record must have been "
                     "smoothed by whoever drew it", "correct": False,
             "why": "The ledgers are raw yearly totals. Nothing was smoothed "
                    "into a shape."},
            {"text": "The model is simply wrong, since nothing real ever "
                     "settles", "correct": False,
             "why": "The model is not wrong; it is undisturbed. Its settling "
                    "is a true consequence of leaving weather out."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h12",
        "band": "harder",
        "text": "An ecologist sees owl numbers fall in one year and concludes "
                "that voles must be scarce that year. What is the weakest "
                "part of that reasoning?",
        "options": [
            {"text": "Owl numbers cannot be counted accurately enough to draw "
                     "any firm conclusion from them", "correct": False,
             "why": "Owls are counted well by nest surveys. The trouble is "
                    "with the inference, not the count."},
            {"text": "Voles and owls have nothing to do with one another",
             "correct": False,
             "why": "They have a great deal to do with one another. That is "
                    "what makes the inference tempting."},
            {"text": "A predator's numbers answer its food a year or more "
                     "late, and weather can move them too", "correct": True},
            {"text": "That one year is far too short a time", "correct": False,
             "why": "A year is long enough to see a fall. What it is not long "
                    "enough to do is tell you what caused it."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h13",
        "band": "harder",
        "text": "Snowshoe hares strip the shoots they browse after a peak, "
                "and those shoots take several years to grow back. Explain "
                "how that alone could produce a cycle in a forest with no "
                "lynx in it.",
        "options": [
            {"text": "The food acts like a predator with a delay: it runs out "
                     "after a peak and recovers slowly", "correct": True},
            {"text": "The hares would eat one another once the shoots had "
                     "gone", "correct": False,
             "why": "Hares are plant-eaters. A shortage kills and stops "
                    "breeding; it does not turn them into predators."},
            {"text": "The shoots would grow back faster each time, so the "
                     "hares would rise for ever", "correct": False,
             "why": "Heavy browsing leaves plants weaker, not stronger. "
                    "Nothing here can rise without limit."},
            {"text": "No cycle is possible without a predator to drive it",
             "correct": False,
             "why": "Any delayed limit will do it. A food supply that "
                    "recovers slowly is exactly such a limit."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h14",
        "band": "harder",
        "text": "A model of a field is run again with the foxes able to breed "
                "twice as fast as before, and nothing else changed. Predict "
                "how the cycle differs.",
        "options": [
            {"text": "The cycle disappears, because the foxes can now keep up "
                     "with the rabbits exactly", "correct": False,
             "why": "Faster is not instant. So long as any delay remains, the "
                    "numbers still overshoot."},
            {"text": "The rabbit peaks arrive after the fox peaks from this "
                     "point on", "correct": False,
             "why": "The order never reverses. A predator's rise still has to "
                    "wait for prey to become plentiful."},
            {"text": "The swings become larger and the cycle takes longer to "
                     "come round", "correct": False,
             "why": "A faster answer means a shorter lag, and a shorter lag "
                    "means a quicker, gentler cycle."},
            {"text": "The lag shortens, so the swings come round more "
                     "quickly", "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h15",
        "band": "harder",
        "text": "Twenty years of counts show rabbit peaks every four years "
                "and fox peaks every four years, but with no consistent gap "
                "between the two. What should an ecologist conclude?",
        "options": [
            {"text": "That the foxes are driving the rabbit cycle, exactly as "
                     "the textbook pattern would have it", "correct": False,
             "why": "If the foxes were driving it, the fox peak would follow "
                    "the rabbit peak every time. It does not."},
            {"text": "That something other than the foxes is driving the "
                     "rabbit cycle", "correct": True},
            {"text": "That twenty years is not enough data to say anything "
                     "about a four-year cycle", "correct": False,
             "why": "Twenty years holds five turns of a four-year cycle, "
                    "which is plenty to see a missing lag."},
            {"text": "That the rabbits must be driving the fox cycle from "
                     "behind", "correct": False,
             "why": "That would still put the fox peak in a fixed place after "
                    "the rabbit peak, and no fixed place is there."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h16",
        "band": "harder",
        "text": "A model gives a field one fixed ceiling for its rabbits. "
                "Suggest why a real field's ceiling moves from year to year.",
        "options": [
            {"text": "The rabbits change how many young each pair chooses to "
                         "raise", "correct": False,
             "why": "Breeding responds to the food and the crowding. It is "
                    "not a separate lever the rabbits pull."},
            {"text": "A ceiling is a rule of thumb that ecologists adjust to "
                         "fit whatever they counted", "correct": False,
             "why": "It is a real limit set by real supplies, not a figure "
                    "fitted after the event."},
            {"text": "The foxes happen to eat a different number every year", "correct": False,
             "why": "Predators hold a population below its ceiling. They do "
                    "not move where the ceiling is."},
            {"text": "Rain and temperature change how much grass grows",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h17",
        "band": "harder",
        "text": "A model is changed so that the foxes can also eat beetles, "
                "which stay plentiful whatever happens. Predict the effect on "
                "the rabbit population.",
        "options": [
            {"text": "Rabbit numbers rise, because the foxes would now spend "
                     "almost all of their time hunting beetles instead of "
                     "rabbits", "correct": False,
             "why": "The foxes take both. Beetles add to their food rather "
                    "than replacing what they hunt."},
            {"text": "Rabbit numbers can be pushed far lower, because the fox "
                     "population no longer falls when rabbits are scarce",
             "correct": True},
            {"text": "Rabbit numbers are unchanged, since beetles are not "
                     "part of the pair being modelled", "correct": False,
             "why": "Anything that feeds the foxes changes what the rabbits "
                    "face. The pair is no longer a pair."},
            {"text": "Rabbit numbers cycle exactly as before, only faster",
             "correct": False,
             "why": "The cycle depends on the foxes going hungry. Remove "
                    "that and the cycle is what changes most."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h18",
        "band": "harder",
        "text": "Two explanations are offered for a vole cycle on a moor: the "
                "owls that hunt them, or the plants they feed on. Which "
                "observation would best tell the two apart?",
        "options": [
            {"text": "Whether the vole peaks are higher in some decades than "
                     "in others", "correct": False,
             "why": "Peak height varies under either explanation. It "
                    "separates nothing."},
            {"text": "Whether the plants are stripped at each vole peak and "
                     "then take years to recover", "correct": True},
            {"text": "Whether the owls are present on the moor every year",
             "correct": False,
             "why": "Owls being present is consistent with both. What matters "
                    "is whether their numbers explain the timing."},
            {"text": "Whether the voles breed more than once a year",
             "correct": False,
             "why": "How fast voles breed shapes the speed of any cycle, "
                    "under either explanation."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h19",
        "band": "harder",
        "text": "A student says a model of a field proves that foxes control "
                "rabbit numbers. Which result from that same model is the "
                "strongest evidence against him?",
        "options": [
            {"text": "That fox numbers rise whenever the rabbits become "
                     "plentiful", "correct": False,
             "why": "That supports his case if anything. It shows the foxes "
                    "answering the rabbits, not controlling them."},
            {"text": "That the two lines both rise and fall across every one of "
                         "the years modelled", "correct": False,
             "why": "Both cycling is what the model is for. It settles "
                    "nothing about which one is in charge."},
            {"text": "That removing every fox still leaves the rabbits "
                     "stopping at a ceiling", "correct": True},
            {"text": "That the fox peak comes after the rabbit peak, in every "
                     "turn of the cycle the model runs", "correct": False,
             "why": "The order of the peaks shows the delay. It does not show "
                    "what sets the rabbits' upper limit."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h20",
        "band": "harder",
        "text": "An estate shoots rabbits every year so that the population "
                "is held at about half the number the land could support. "
                "Compare the condition of those rabbits with rabbits in a "
                "population sitting at its ceiling.",
        "options": [
            {"text": "They are in worse condition, because a hunted "
                     "population is always a stressed one", "correct": False,
             "why": "Stress is real and food is the larger effect here. Twice "
                    "the grass per rabbit is a better living."},
            {"text": "They are in the same condition, because a rabbit needs "
                     "the same food wherever it lives", "correct": False,
             "why": "Each rabbit needs the same; the question is whether it "
                    "gets it. At the ceiling, it does not."},
            {"text": "It cannot be compared, because the two populations are "
                     "different sizes", "correct": False,
             "why": "Different sizes is exactly what makes them comparable — "
                    "the food is shared between fewer animals."},
            {"text": "They are in better condition, with more food each",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h21",
        "band": "harder",
        "text": "A record shows lynx numbers falling for three years while "
                "hare numbers are already rising. Give the best explanation.",
        "options": [
            {"text": "The lynx have stopped hunting hares and taken to "
                     "smaller prey, which this particular record does not "
                     "show", "correct": False,
             "why": "Nothing suggests a change of diet, and the pattern "
                    "repeats every turn, which a one-off change would not."},
            {"text": "The record must be wrong, since the two lines should "
                     "move together", "correct": False,
             "why": "They never move together. A trailing predator line is "
                    "what this record is famous for."},
            {"text": "The lynx are still answering the scarcity of two years "
                     "ago, and their rise will follow", "correct": True},
            {"text": "The hares have become too quick for the lynx to catch "
                     "in the space of three years", "correct": False,
             "why": "Populations do not change like that in three years, and "
                    "the same pattern repeats each cycle."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h22",
        "band": "harder",
        "text": "A student uses a two-species model to predict how many "
                "rabbits a named farm will hold next spring. Name the "
                "strongest reason that prediction will fail.",
        "options": [
            {"text": "The model has no weather, disease, migration or other "
                     "prey in it, and a real farm has all four",
             "correct": True},
            {"text": "The model's arithmetic is far too simple to give a whole "
                     "number of animals at the end", "correct": False,
             "why": "Rounding is trivial to handle. What is missing is half "
                    "of what acts on a real population."},
            {"text": "A year is too short a period for any model to say "
                     "anything about", "correct": False,
             "why": "Models forecast over a year routinely. It is what this "
                    "one leaves out that stops it."},
            {"text": "Models can never predict anything", "correct": False,
             "why": "Models predict a great deal. This one was built to "
                    "explain a pattern rather than to forecast a field."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h23",
        "band": "harder",
        "text": "A charity proposes protecting a large predator in order to "
                "protect a valley's plants from overgrazing. Which statement "
                "best evaluates that plan?",
        "options": [
            {"text": "It is sound, and the grazers would also be limited by "
                     "their food in the end", "correct": True},
            {"text": "It is unsound, because a predator cannot affect a plant "
                     "it has never touched", "correct": False,
             "why": "It reaches the plants through the grazers, which is "
                    "exactly the mechanism the plan relies on."},
            {"text": "It is sound, and it removes any need to think about the "
                     "grazers' own food supply as well", "correct": False,
             "why": "The food supply is still the ceiling. The predator holds "
                    "the grazers below it rather than replacing it."},
            {"text": "It is unsound in every case", "correct": False,
             "why": "Predators do hold grazing populations down, and valleys "
                    "have recovered when predators returned."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h24",
        "band": "harder",
        "text": "A model that steps forward one year at a time is given a cap "
                "just above the prey ceiling and a floor of one predator. "
                "Explain why a model like that needs limits of that kind.",
        "options": [
            {"text": "Because a model must always be given a starting and a "
                     "finishing number before it will run at all",
             "correct": False,
             "why": "It has a starting number already. These limits act every "
                    "year, not at the ends."},
            {"text": "Without them the numbers could overshoot into "
                     "impossible values, or fall below zero", "correct": True},
            {"text": "Because the cap and the floor are what create the cycle "
                     "in the first place", "correct": False,
             "why": "The cycle comes from the delay. Removing the cap would "
                    "leave a wilder cycle, not a flat line."},
            {"text": "Because ecologists have agreed those two figures for "
                     "rabbits and foxes", "correct": False,
             "why": "No such figures are agreed. They are housekeeping for "
                    "the arithmetic, not measurements."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h25",
        "band": "harder",
        "text": "A student plots predator numbers against prey numbers, one "
                "point for each year, and joins the points in order. What "
                "does the loop show?",
        "options": [
            {"text": "That the counts contain too much error to give a clean "
                     "relationship", "correct": False,
             "why": "A tidy loop is not error. Error scatters points; it does "
                    "not walk them round in order."},
            {"text": "That predator and prey numbers are unrelated to one "
                     "another in this wood", "correct": False,
             "why": "Unrelated numbers give a shapeless cloud. A loop is "
                    "strong evidence of a relationship."},
            {"text": "That the predators reach each point of the cycle after "
                     "the prey do", "correct": True},
            {"text": "That the prey population has been counted twice",
             "correct": False,
             "why": "Each year gives one point. The loop comes from the "
                    "timing, not from a repeated count."},
        ],
        "figure": "b9-predator-prey-loop",
    },
    {
        "id": "b9-02-h26",
        "band": "harder",
        "text": "An island's rabbits sit at their ceiling for decades and "
                "barely cycle, although a few foxes live there throughout. "
                "Suggest why.",
        "options": [
            {"text": "The foxes are too few to push the rabbits below what "
                     "the food allows", "correct": True},
            {"text": "Island rabbits breed too slowly for a cycle to build up "
                     "over the years", "correct": False,
             "why": "Slow breeding would deepen a crash, not prevent one. The "
                    "rabbits here are not being pushed down at all."},
            {"text": "A cycle needs at least two predator species before it "
                     "can appear", "correct": False,
             "why": "One predator and one prey is enough, as the model shows. "
                    "What matters is how hard the predator presses."},
            {"text": "Foxes and rabbits never cycle on islands",
             "correct": False,
             "why": "They cycle on islands readily. This island's foxes are "
                    "simply too scarce to matter."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h27",
        "band": "harder",
        "text": "Compare what sets the size of a rabbit population in a field "
                "with foxes in it and in a field with none.",
        "options": [
            {"text": "With foxes the grass sets it, and without foxes the "
                     "weather does", "correct": False,
             "why": "The grass sets the ceiling either way. Weather moves "
                    "that ceiling up and down in both fields."},
            {"text": "With foxes, hunting holds it below the ceiling; "
                     "without, food and space set it", "correct": True},
            {"text": "It is set by the foxes in one field, and nothing whatever "
                     "sets it in the other", "correct": False,
             "why": "A field with no predator still has a limit. Rabbits stop "
                    "climbing when the grass runs short."},
            {"text": "It ends up at the same number either way",
             "correct": False,
             "why": "A hunted population sits below its ceiling; an unhunted "
                    "one climbs to it. Those are different numbers."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h28",
        "band": "harder",
        "text": "Fur records are used to argue that heavy trapping caused a "
                "lynx decline in the 1890s. What would you most want to know "
                "before accepting that argument?",
        "options": [
            {"text": "How many trappers were working in Canada in the decade "
                     "before the 1890s began", "correct": False,
             "why": "Trapper numbers matter for reading the line, and they "
                    "cannot separate trapping from a hare shortage."},
            {"text": "Whether the hare numbers were falling in the same "
                     "years", "correct": True},
            {"text": "Whether the price of lynx fur was high or low during "
                     "those particular years", "correct": False,
             "why": "Price changes how many pelts come in, and a hare crash "
                    "would explain the decline just as well."},
            {"text": "Whether lynx live anywhere outside Canada",
             "correct": False,
             "why": "Their range elsewhere says nothing about what happened "
                    "to this population in this decade."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h29",
        "band": "harder",
        "text": "A model is built in which each population answers a change "
                "in the other instantly, with no delay at all. Explain why no "
                "cycle appears in it.",
        "options": [
            {"text": "Each population corrects itself the moment the other "
                     "moves, so nothing overshoots", "correct": True},
            {"text": "Without a delay the two populations must both die out "
                     "within a very few years", "correct": False,
             "why": "They settle rather than die. Instant correction is "
                    "stabilising, not fatal."},
            {"text": "A cycle needs three species, and this model has two",
             "correct": False,
             "why": "Two is enough for a cycle, as the delayed model shows. "
                    "The delay is what was removed here."},
            {"text": "The arithmetic cannot be done", "correct": False,
             "why": "The arithmetic runs perfectly well. It simply produces "
                    "two steady numbers instead of a swing."},
        ],
        "figure": None,
    },
    {
        "id": "b9-02-h30",
        "band": "harder",
        "text": "An ecologist writes that the foxes of a field are limited by "
                "the rabbits, while the rabbits are limited by the foxes AND "
                "by the grass. Explain why the two halves are not "
                "symmetrical.",
        "options": [
            {"text": "The rabbits have a food limit as well as a predator, "
                     "while the foxes have only their food", "correct": True},
            {"text": "The foxes are larger animals, so they are limited by "
                     "space rather than by anything they eat", "correct": False,
             "why": "Size is not the point. A fox's numbers still rest on how "
                    "much prey there is."},
            {"text": "The rabbits are limited by the grass alone, and the "
                     "foxes are what the ecologist has miscounted",
             "correct": False,
             "why": "Both limits act on the rabbits. Predation holds them "
                    "below a ceiling that the grass sets."},
            {"text": "Because the foxes are at the top, and nothing there can "
                     "be limited", "correct": False,
             "why": "Top predators are limited severely — by how little food "
                    "reaches them."},
        ],
        "figure": None,
    },
]
