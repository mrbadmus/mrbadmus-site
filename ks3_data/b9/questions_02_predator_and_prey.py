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
]
