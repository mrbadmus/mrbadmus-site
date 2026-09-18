# -*- coding: utf-8 -*-
"""B11 lesson 01 — Variation and competitive success: twelve questions (MRB-269).

The lesson makes one argument and draws it five times: which variation gives
an advantage depends entirely on the conditions, and the conditions change, so
there is no such thing as a generally superior individual. Its instrument is a
bench that runs the SAME five mice through five worlds — a hard winter, a
drought, an owl, an overcrowded year and a new disease — and the column
reshuffles every time.

The bank probes the three things a student most easily half-learns here.
First, reading the bench as a ranking rather than as five rankings: several
questions hand back a row (the small quick mouse, the large heavy mouse, the
bold mouse) and ask why the same animal moves between top and bottom, with
"that one is just the weakest" sitting there as a distractor. Second, what
fitness is counted in — surviving offspring, not strength and not length of
life. Third, the discipline of the word *adapted*: adapted always has to say
what to.

Distractors are built from the lesson's two declared misconceptions.
**EVOL-01** ("survival of the fittest means the strongest survive") supplies
every option that hands the win to strength or to a direct fight — the animal
that drives off the owl, the finches that survived the drought because they
were strongest, bright feathers read as a signal of health, competition read
as fighting. **EVOL-02** ("some individuals are just better than others")
supplies every option that ranks a variation in general — quick mice as "the
weakest of the five", large as "generally the best", thick shells as "the
better shell", a deep beak so obviously better that the 1983 data must be an
error.

Two further errors the lesson exists to correct are worked as well. The
Lamarckian one — the mouse that thickens its own coat, the snail that
thickens its own shell, the finch that grows its own beak — which the lesson
meets here first and b11-02 owns; and the OVER-correction, the student who
learns "it depends" so well that they conclude nothing is ever an advantage,
or that teaching values mean the bench shows nothing at all. That second one
only appears in a class that has understood the lesson, which is why it earns
two slots in the harder band.

No question restates a ladder rung. The rungs already own the pale-fur-on-two-
grounds inference, the definition of "fittest", the thick coat's winter-to-
drought reversal and the disease panel's argument for unused variation, so the
bank works around all four: the thick coat's own reversal is left to rung 3 and
the bench is read through the other four mice instead, the disease panel
appears only through the bold mouse, and the definition of fitness is applied
as a comparison rather than asked for as a definition.

`figure` is `None` throughout — the lesson declares no figures, and the one
B11 diagram ruled (the peppered-moth pair) belongs to b11-02. Every stem is
self-contained.
"""

UNIT = "B11"
LESSON = "variation-and-competitive-success"
LESSON_NUMBER = 1

QUESTIONS = [

    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-01-e01",
        "band": "easier",
        "text": "Three of the four cards in \"What they are competing for\" "
                "are tagged \"Between members of one species\". Why is "
                "competition usually fiercest inside a species?",
        "options": [
            {"text": "Members of the same species are more aggressive towards "
                     "each other than towards other animals.", "correct": False,
             "why": "Competition is not aggression. It is two organisms "
                    "needing the same limited resource, so that one getting "
                    "it means the other does not — no fighting required."},
            {"text": "They need exactly the same things, so one getting a "
                     "resource means another does not.", "correct": True},
            {"text": "There are always more members of one species in a place "
                     "than there are of any other.", "correct": False,
             "why": "Numbers are not the reason. A rare species still competes "
                    "fiercely inside itself, because every member wants the "
                    "same food, the same burrow and the same mates."},
            {"text": "Different species never need the same resources, so they "
                     "cannot compete at all.", "correct": False,
             "why": "Different species do compete, wherever they overlap. The "
                    "point about one species is that its members overlap on "
                    "everything at once."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e02",
        "band": "easier",
        "text": "The lesson puts one sentence in large type: \"More are born "
                "than can possibly survive.\" What does that sentence do for "
                "the rest of the lesson?",
        "options": [
            {"text": "It explains why there is a competition at all — the "
                     "resources cannot support everyone born.", "correct": True},
            {"text": "It shows that most young animals are born too weak to "
                     "survive, whatever the conditions.", "correct": False,
             "why": "That is the belief that some individuals are simply worse "
                    "than others. The bench shows the opposite: the mouse that "
                    "dies in the drought is the one that won the winter."},
            {"text": "It shows that a species will slowly run out of members "
                     "as the years go by.", "correct": False,
             "why": "The population is not shrinking. More offspring are "
                    "produced than the resources can support, so the surplus "
                    "dies and the numbers stay roughly steady."},
            {"text": "It shows that animals have to fight each other directly "
                     "to decide who gets to live.", "correct": False,
             "why": "Competition rarely looks like a fight. In a drought the "
                    "winner is the animal that needs least water, and it never "
                    "meets a rival."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e03",
        "band": "easier",
        "text": "A note under the bench says the survival percentages are "
                "\"teaching values chosen to show how the ranking changes, not "
                "measurements\". What are the numbers there to show you?",
        "options": [
            {"text": "Exactly how likely a real mouse with each variation is "
                     "to survive a real winter.", "correct": False,
             "why": "That is what the note rules out. The figures were chosen "
                    "to make a pattern readable, not collected from mice in a "
                    "field."},
            {"text": "Which of the five variations scores highest once all "
                     "five environments are added up.", "correct": False,
             "why": "Adding the columns would invent a general ranking, which "
                    "is exactly what this lesson denies. Each column is a "
                    "ranking in one set of conditions and nowhere else."},
            {"text": "How the order of the same five mice changes when the "
                     "conditions change.", "correct": True},
            {"text": "How much a mouse's coat and body change as the weather "
                     "changes around it.", "correct": False,
             "why": "Nothing about any mouse changes on this bench. The five "
                    "animals are identical in every panel; only the world "
                    "around them is swapped."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e04",
        "band": "easier",
        "text": "The fourth competition card is tagged \"Against everything "
                "else\" rather than \"Between members of one species\". What "
                "does the lesson say about predators and disease?",
        "options": [
            {"text": "They are the fiercest form of competition between the "
                     "members of one species.", "correct": False,
             "why": "An owl is not competing with a mouse for anything — it is "
                    "eating it. That is precisely why the card carries a "
                    "different tag."},
            {"text": "They have nothing to do with which variations get passed "
                     "on to the next generation.", "correct": False,
             "why": "They have everything to do with it, which is why the card "
                    "is there. Whichever variations happen to help you avoid "
                    "being eaten or infected are the ones passed on."},
            {"text": "They only remove the individuals that were already too "
                     "weak to survive anyway.", "correct": False,
             "why": "On the disease bench the mouse that does worst is the "
                    "bold one — the most active of the five. Weakness is not "
                    "what decides it."},
            {"text": "They are not competition exactly, but they act as the "
                     "same filter on variation.", "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-01-s01",
        "band": "standard",
        "text": "The small quick mouse is the best survivor in the drought at "
                "85%, but manages only 45% in the overcrowded year. What does "
                "the bench give as the reason?",
        "options": [
            {"text": "The mild weather of that year removed the advantage that "
                     "being quick gives in the cold.", "correct": False,
             "why": "Being quick was never an advantage in the cold — the "
                    "small quick mouse is the worst survivor of the hard "
                    "winter, at 45%. Read the winter column again."},
            {"text": "More predators appear once the population doubles, and "
                     "small mice are caught first.", "correct": False,
             "why": "No predator appears in the overcrowded panel; that is the "
                    "owl's panel, where the small quick mouse actually does "
                    "well. Here the problem is other mice."},
            {"text": "It is quick, but larger mice push it off the food. Speed "
                     "does not win an argument.", "correct": True},
            {"text": "Quick mice are the weakest of the five, so they lose out "
                     "wherever there is a crowd.", "correct": False,
             "why": "There is no weakest mouse on this bench. The same animal "
                    "is at the top of the drought column and at the bottom of "
                    "the winter one."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s02",
        "band": "standard",
        "text": "The large, heavy mouse survives at 40% in the drought and at "
                "80% in the year the population doubles. Which explanation "
                "fits the bench?",
        "options": [
            {"text": "Size costs water and food in a drought, and wins "
                     "confrontations over food and burrows in a crowd.",
             "correct": True},
            {"text": "The large mice put on muscle during the mild year, so "
                     "they were stronger by the time it got crowded.",
             "correct": False,
             "why": "No mouse on this bench changes. The animals are identical "
                    "in every panel — what moved is the conditions around "
                    "them."},
            {"text": "Being large is generally the best variation to have, and "
                     "the drought was an unusual exception.", "correct": False,
             "why": "Then the large mouse would top the winter column too, and "
                    "it does not — the thick coat does. No variation is an "
                    "advantage in general."},
            {"text": "There were simply more large mice about in the crowded "
                     "year, so more of them survived.", "correct": False,
             "why": "The figure is the chance for one mouse carrying that "
                    "variation, not a headcount. Doubling the population does "
                    "not raise anybody's odds."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s03",
        "band": "standard",
        "text": "When the owl moves in, the bold and exploratory mouse falls "
                "to 20% — the lowest figure anywhere in that column. Why?",
        "options": [
            {"text": "Bold mice will approach the owl and try to drive it off, "
                     "and are killed doing it.", "correct": False,
             "why": "Bold here means willing to explore, not willing to fight. "
                    "The cost is being out in the open, not picking a "
                    "quarrel with a predator."},
            {"text": "Bold means out in the open more often, which is the "
                     "wrong habit when something is hunting.", "correct": True},
            {"text": "Bold mice tend also to be the largest, so the owl spots "
                     "them before it spots the others.", "correct": False,
             "why": "Each mouse on this bench carries one variation and nothing "
                    "else — bold is not also large. The note under the bench "
                    "says the bench works that way on purpose."},
            {"text": "Boldness is a poor variation, so the bold mouse sits near "
                     "the bottom of every column.", "correct": False,
             "why": "It does not. The bold mouse is the second best survivor of "
                    "the overcrowded year, because it explores past the crowd "
                    "and finds untouched food."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s04",
        "band": "standard",
        "text": "One animal lives fifty years and never breeds. A mayfly lives "
                "one day and lays five hundred eggs. Which of them has the "
                "greater fitness, and why?",
        "options": [
            {"text": "The fifty-year animal, because surviving that long is "
                     "what fitness measures.", "correct": False,
             "why": "Fitness is not length of life. An organism that lives "
                    "fifty years and never breeds leaves nothing behind, so "
                    "its fitness is zero."},
            {"text": "Neither — fitness cannot be compared between two species "
                     "as different as those two.", "correct": False,
             "why": "Fitness is counted the same way in every species: "
                    "surviving offspring. That common measure is exactly what "
                    "lets you compare them."},
            {"text": "The mayfly, because it is smaller and needs far less "
                     "food and water to stay alive.", "correct": False,
             "why": "Needing little is an advantage in a drought, not a "
                    "definition of fitness. What settles this is the five "
                    "hundred eggs."},
            {"text": "The mayfly: fitness is counted in surviving offspring, "
                     "and the other leaves none.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-01-h01",
        "band": "harder",
        "text": "On a hillside, some snails have thick shells and some thin. A "
                "thick shell resists a thrush's beak, but takes more calcium to "
                "build and slows the snail's growth. What does this lesson's "
                "argument predict?",
        "options": [
            {"text": "Thick-shelled snails are the better snails, because "
                     "protection is worth more than growth.", "correct": False,
             "why": "That is the idea of a generally better individual, and the "
                    "bench takes it apart five times over. Better always has to "
                    "say better where."},
            {"text": "The thin-shelled snails will thicken their shells once "
                     "thrushes start hunting the hillside.", "correct": False,
             "why": "An individual cannot rebuild itself to suit its "
                    "conditions. The shell a snail has is the shell it has — "
                    "the environment does the choosing, not the snail."},
            {"text": "Neither shell can really be an advantage, because each "
                     "of them carries a cost that cancels it out.", "correct": False,
             "why": "Every variation carries a cost — a thick coat does, and it "
                    "still wins the winter. An advantage is one that pays for "
                    "itself in the conditions the organism is actually in."},
            {"text": "Where thrushes hunt, the thick shell is the advantage; "
                     "where calcium is scarce, the thin one.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h02",
        "band": "harder",
        "text": "Average beak depth in the Daphne Major finches rose during the "
                "1977 drought and fell again after the 1983 rains. Which "
                "reading of that is right?",
        "options": [
            {"text": "No bird changed its beak — deep-beaked birds survived "
                     "the drought, shallow-beaked ones the wet years.", "correct": True},
            {"text": "The finches grew deeper beaks to deal with the tough "
                     "seeds, then shrank them when soft seeds came back.",
             "correct": False,
             "why": "No individual finch ever changed its beak. What changed "
                    "between one measurement and the next was which birds were "
                    "still alive to be measured."},
            {"text": "The birds that came through the drought were the "
                     "strongest ones, and beak depth is a measure of strength.",
             "correct": False,
             "why": "Strength is one variation among many and is rarely the one "
                    "that matters. What mattered on Daphne Major was being able "
                    "to crack a large, tough seed."},
            {"text": "A deep beak is the better beak, so the fall after 1983 "
                     "must be an error in the measurements.", "correct": False,
             "why": "The 1983 figures are the point of the study, not a "
                    "mistake. A deep beak paid in a drought and cost in a wet "
                    "year — the same reversal the bench draws."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h03",
        "band": "harder",
        "text": "In one wood, males of a bird species with long bright tail "
                "feathers attract far more mates but are spotted more easily by "
                "hawks. There are very few hawks in that wood. Which male has "
                "the greater fitness?",
        "options": [
            {"text": "The plain male, because he is far more likely to stay "
                     "alive, and staying alive is what fitness means.",
             "correct": False,
             "why": "Fitness is not survival on its own. It is counted in "
                    "surviving offspring, and a male that survives without ever "
                    "breeding contributes nothing."},
            {"text": "The bright male, because bright feathers are a sign that "
                     "he is the strongest and healthiest.", "correct": False,
             "why": "Fittest does not mean strongest. What settles it here is "
                    "the number of mates the feathers win him, not what they "
                    "are supposed to advertise."},
            {"text": "The bright male, because he leaves more offspring and the "
                     "hawks that would punish him are rare.", "correct": True},
            {"text": "The plain male, because a variation that makes you easier "
                     "to eat can never be an advantage.", "correct": False,
             "why": "It can, if it pays for itself in the conditions the bird "
                    "is actually in. Move the same bird to a wood full of hawks "
                    "and the answer reverses."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h04",
        "band": "harder",
        "text": "A student writes: \"The bench shows the small quick mouse is "
                "the best adapted of the five, because it comes top in two of "
                "the five environments.\" What is wrong with that?",
        "options": [
            {"text": "Nothing — coming top in two columns out of five is what "
                     "best adapted means.", "correct": False,
             "why": "There is no overall column to come top of. Adapted is "
                    "always adapted to something, and that same mouse is bottom "
                    "of the winter column."},
            {"text": "Adapted has to say what to: that mouse suits a drought "
                     "and is badly suited to a hard winter.", "correct": True},
            {"text": "It is wrong because the large, heavy mouse actually comes "
                     "top in more environments than that.", "correct": False,
             "why": "It does not — the large mouse tops one column, the crowded "
                    "year. Counting wins is itself the error here, not "
                    "miscounting them."},
            {"text": "It is wrong because the percentages are teaching values, "
                     "so the bench shows nothing about being adapted.",
             "correct": False,
             "why": "The note says the numbers were chosen, not that they are "
                    "meaningless. They were chosen precisely to show how the "
                    "ranking moves when the conditions do."},
        ],
        "figure": None,
    },
    # ── MRB-335 top-up ───────────────────────────────────────────────────
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-01-e05",
        "band": "easier",
        "text": "Two mice in the same field both need the same seeds, and "
                "there are not enough seeds for both. Biologists call that "
                "competition. What does the word mean?",
        "options": [
            {"text": "Two organisms attacking each other to decide which of "
                     "them gets to feed, so that the loser goes "
                     "hungry.",
             "correct": False,
             "why": "Competition is not aggression. Most of it never involves "
                    "a fight at all — in a drought the animal that needs least "
                    "water wins without ever meeting a rival."},
            {"text": "Two or more organisms needing the same limited resource, "
                     "so one getting it means another does not.",
             "correct": True},
            {"text": "One organism hunting and eating another organism that "
                     "lives in the same place.",
             "correct": False,
             "why": "That is a predator and its prey, which is a different "
                    "relationship. An owl is not competing with a mouse for "
                    "anything — it is eating it."},
            {"text": "Two organisms of different species being unable to live "
                     "in the same habitat.",
             "correct": False,
             "why": "Species that compete usually live alongside each other "
                    "perfectly well. Competition describes what they are both "
                    "short of, not whether they can share a place."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e06",
        "band": "easier",
        "text": "In a mouse population, food, water, burrows and mates are all "
                "described as resources. What makes something a resource?",
        "options": [
            {"text": "It is something the animals have to work together to "
                     "obtain.",
             "correct": False,
             "why": "Nothing here is worked at together. A resource is simply "
                    "something the animals need, and there is not enough of it "
                    "to go round."},
            {"text": "It is something an organism produces itself and then "
                     "supplies to the rest of its population.",
             "correct": False,
             "why": "Resources are not produced by the population that needs "
                    "them. Food, water and shelter are things the surroundings "
                    "supply, in limited amounts."},
            {"text": "It is something an organism needs, and there is not "
                     "enough to go round.",
             "correct": True},
            {"text": "It is anything around an organism that can harm it if "
                     "there is too much of it.",
             "correct": False,
             "why": "That describes a hazard rather than a resource. A "
                    "resource is something an organism needs and can run short "
                    "of."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e07",
        "band": "easier",
        "text": "A virus sweeps through a population of mice. Size, coat "
                "thickness, speed and fur colour give no protection at all. "
                "The mice that spend most time exploring and meeting other "
                "mice do worst of all. Why?",
        "options": [
            {"text": "They meet more mice, so they have more chance of "
                     "catching the infection.",
             "correct": True},
            {"text": "Exploring uses energy, which leaves them too weak to "
                     "fight the virus off.",
             "correct": False,
             "why": "Surviving a new disease is not a matter of being strong "
                    "or well fed. It depends on whether an animal happens to "
                    "carry a version of a gene that resists it."},
            {"text": "Bold animals are always the least likely to survive, "
                     "whatever the danger is.",
             "correct": False,
             "why": "Boldness is a serious advantage in a crowded year, when a "
                    "bold mouse finds food and space the others have not "
                    "reached. It costs here for one specific reason."},
            {"text": "The virus attacks active animals more strongly than "
                     "resting ones.",
             "correct": False,
             "why": "A virus does not pick its victims by how busy they are. "
                    "What changes for a bold mouse is how many infected mice "
                    "it meets."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e08",
        "band": "easier",
        "text": "Biologists avoid saying that one species is more advanced or "
                "superior to another. Which phrase do they use instead?",
        "options": [
            {"text": "Higher up the tree of life.",
             "correct": False,
             "why": "There is no ladder of advancement in biology. A bacterium "
                    "that thrives where nothing else can is superbly fitted to "
                    "where it lives."},
            {"text": "Stronger than the other species it lives alongside.",
             "correct": False,
             "why": "Strength is one variation among many, and it is often the "
                    "wrong one. It is not a general ranking of species."},
            {"text": "Further along in its evolution than the other species "
                     "around it.",
             "correct": False,
             "why": "Every living species has been evolving for exactly as "
                    "long as every other. There is no further along to be."},
            {"text": "Well adapted to a particular environment.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e09",
        "band": "easier",
        "text": "In a hard winter with eight weeks of snow, mice with a thick "
                "coat survive better than any other kind. What is the reason?",
        "options": [
            {"text": "A thick coat makes a mouse look larger, so the "
                     "predators around it leave it alone.",
             "correct": False,
             "why": "Nothing here is hunting by size. What kills mice in a "
                    "hard winter is the cold itself, and losing heat is the "
                    "danger a thick coat answers."},
            {"text": "Growing a thicker coat is how a mouse answers the cold.",
             "correct": False,
             "why": "The mouse grew nothing to order. It has the coat it was "
                    "born with, and that coat happens to suit the winter it is "
                    "in."},
            {"text": "Insulation is exactly what this winter demands, and it "
                     "costs little.",
             "correct": True},
            {"text": "A thick coat lets the mouse dig deeper and reach the "
                     "food buried under eight weeks of lying snow.",
             "correct": False,
             "why": "A coat is not a digging tool. It works by keeping heat "
                    "in, which is what matters when losing heat is the main "
                    "way to die."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e10",
        "band": "easier",
        "text": "In biology, what does the word environment include?",
        "options": [
            {"text": "The weather and the ground, but not the living things.",
             "correct": False,
             "why": "The living things are half of it. The predators, the food "
                    "and the other members of an organism's own species all "
                    "affect it."},
            {"text": "Everything around an organism that affects it, living "
                     "and non-living.",
             "correct": True},
            {"text": "The habitat a species is best suited to living in, "
                     "whether or not it actually lives there.",
             "correct": False,
             "why": "The environment is where an organism actually is, not "
                    "where it would do well. Change what is around it and the "
                    "ranking of variations changes with it."},
            {"text": "Everything a species has changed about the place it "
                     "lives in since it arrived.",
             "correct": False,
             "why": "That is the organism acting on its surroundings, which is "
                    "a much smaller thing. The environment is everything "
                    "around it that affects it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e11",
        "band": "easier",
        "text": "The same five mice are compared in a hard winter, a long "
                "drought, a year with a new predator, an overcrowded year and "
                "a year with a new disease. Nothing about any mouse is altered "
                "between one comparison and the next. What is the point of "
                "setting it up that way?",
        "options": [
            {"text": "It shows that the ranking of the same five variations "
                     "changes when the conditions change.",
             "correct": True},
            {"text": "It shows which of the five mice is the strongest "
                     "overall.",
             "correct": False,
             "why": "There is no overall. Each set of conditions produces its "
                    "own ranking, and no mouse is at the top of all of them."},
            {"text": "It shows how a mouse's body changes as the weather "
                     "around it changes.",
             "correct": False,
             "why": "No mouse changes at any point. That is the whole reason "
                    "the same five animals are used every time."},
            {"text": "It shows that most variations make no difference to "
                     "whether an animal survives.",
             "correct": False,
             "why": "Most of them make a large difference — just not the same "
                    "difference every time. Only against a new disease do the "
                    "visible variations stop mattering."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e12",
        "band": "easier",
        "text": "Two robins in the same garden both want the same nest site. "
                "Which kind of competition is that?",
        "options": [
            {"text": "Competition for food.",
             "correct": False,
             "why": "A nest site is not something either bird eats. Food is a "
                    "separate resource, and the two birds may have plenty of "
                    "it."},
            {"text": "Competition for mates.",
             "correct": False,
             "why": "Both robins want the site, not each other. Competition "
                    "for mates is about which individuals get to breed at "
                    "all."},
            {"text": "Competition for space and shelter.",
             "correct": True},
            {"text": "It is not competition, because neither bird is harmed.",
             "correct": False,
             "why": "One of them ends up without a nest site, which is the "
                    "harm. Competition does not need a fight or an injury to "
                    "count."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e13",
        "band": "easier",
        "text": "Only some individuals in a population ever breed. Why does "
                "the competition for mates matter more than it might look?",
        "options": [
            {"text": "Because an animal that does not breed will die sooner "
                     "than one that does.",
             "correct": False,
             "why": "It may live a long and comfortable life. What it will not "
                    "do is leave any offspring, and that is what counts here."},
            {"text": "Because animals that do not breed stop competing for "
                     "food and space as well.",
             "correct": False,
             "why": "They go on eating and taking up space for the rest of "
                    "their lives. Breeding is a separate contest with a "
                    "separate result."},
            {"text": "Because the largest and strongest animals are the ones "
                     "that win it.",
             "correct": False,
             "why": "Sometimes, and often not. What matters is not who wins by "
                    "strength but that only the winners leave offspring at "
                    "all."},
            {"text": "Because surviving without reproducing contributes "
                     "nothing to the next generation.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-01-s05",
        "band": "standard",
        "text": "In a long drought with months of no rain, mice with pale "
                "sandy fur do better than most of the population. The ground "
                "they live on is dry and bare. Which explanation fits?",
        "options": [
            {"text": "Pale fur is the best colour to have in any conditions, "
                     "so it wins here as well.",
             "correct": False,
             "why": "Move the same mouse onto dark peaty soil with an owl "
                    "overhead and pale fur becomes the worst thing to have. No "
                    "colour is an advantage in general."},
            {"text": "Pale fur reflects sunlight and matches dry ground, so "
                     "the mouse stays cooler and stays hidden.",
             "correct": True},
            {"text": "The drought bleached the mice paler, which is why the "
                     "pale ones are doing well.",
             "correct": False,
             "why": "A mouse is the colour it was born and stays that colour. "
                    "The sun does not repaint an animal, and a bleaching could "
                    "not be passed on if it did."},
            {"text": "Pale mice need less water than dark ones, because pale "
                     "fur holds less moisture.",
             "correct": False,
             "why": "Fur colour does not set how much water an animal needs — "
                    "body size does. What pale fur does here is reflect heat "
                    "and hide the mouse."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s06",
        "band": "standard",
        "text": "A barn owl moves into a field and hunts the mice at night. "
                "Mice with a thick coat survive at about the same rate as they "
                "did before the owl arrived. What does that tell you?",
        "options": [
            {"text": "A thick coat gives some protection against an owl's "
                     "talons.",
             "correct": False,
             "why": "There is no protection here, which is why the figure does "
                    "not move. Fur thickness is simply not what decides "
                    "whether an owl catches a mouse."},
            {"text": "A thick coat must be an advantage against every danger, "
                     "since it never does badly.",
             "correct": False,
             "why": "It does very badly in a drought, where it traps heat the "
                    "animal cannot lose. Here it neither helps nor harms, "
                    "which is a third possibility."},
            {"text": "A variation can be simply irrelevant to a danger — "
                     "neither an advantage nor a cost.",
             "correct": True},
            {"text": "The owl cannot be a serious danger to the population, "
                     "since one kind of mouse is unaffected.",
             "correct": False,
             "why": "It is a serious danger to the others — a bold mouse or a "
                    "pale one is far more likely to be caught. One variation "
                    "being untouched says nothing about the rest."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s07",
        "band": "standard",
        "text": "In a year when the population doubles and food runs short, "
                "the boldest, most exploratory mice do best of all. In a year "
                "when a virus sweeps through, the same boldness leaves them "
                "worst off. Which explanation covers both?",
        "options": [
            {"text": "Boldness makes an animal stronger in a crowd and weaker "
                     "when it is ill.",
             "correct": False,
             "why": "Boldness is a habit, not a body. It does not change how "
                    "strong a mouse is; it changes where the mouse goes and "
                    "who it meets."},
            {"text": "The bold mice became more cautious once the virus "
                     "arrived, which cost them.",
             "correct": False,
             "why": "No mouse changed its behaviour to suit the year. The same "
                    "habit is being rewarded in one year and punished in the "
                    "next."},
            {"text": "Boldness is a poor variation overall, and the crowded "
                     "year is a lucky exception.",
             "correct": False,
             "why": "There is no overall. Two years, two opposite results, and "
                    "the mouse is the same in both — which is the point rather "
                    "than the exception."},
            {"text": "Exploring finds food beyond the crowd, and meeting more "
                     "mice means meeting more infection.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s08",
        "band": "standard",
        "text": "A virus reaches a mouse population, and none of the "
                "differences you can see — size, coat, speed, boldness, colour "
                "— makes any difference to who survives once infected. What "
                "decides it instead?",
        "options": [
            {"text": "Which versions of certain genes an animal happens to "
                     "carry, which nothing about its appearance shows.",
             "correct": True},
            {"text": "Nothing decides it: survival against a new disease is "
                     "entirely random.",
             "correct": False,
             "why": "It is not random. Resistance is inherited, and an animal "
                    "that carries it is far more likely to come through — you "
                    "simply cannot tell which animals those are by looking."},
            {"text": "The animals that were in the best condition when the "
                     "virus arrived, because a healthy body fights "
                     "infection off.",
             "correct": False,
             "why": "Condition helps with many things and is not what settles "
                    "this. The animal that resists may be the least impressive "
                    "in the group in every other respect."},
            {"text": "How much contact each animal had with the others.",
             "correct": False,
             "why": "Contact affects who catches it, and the question is who "
                    "survives it. Two mice that both catch the virus are "
                    "separated by what their genes happen to be."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s09",
        "band": "standard",
        "text": "A pair of mice produce about thirty young in a year, and the "
                "population in their field stays at roughly the same size year "
                "after year. What follows from those two facts?",
        "options": [
            {"text": "Most of the young must be leaving the field to live "
                     "somewhere else.",
             "correct": False,
             "why": "Some may, and it is nowhere near enough to account for "
                    "thirty young a pair. The great majority simply do not "
                    "survive to breed."},
            {"text": "The mice must be producing far more young than they used "
                     "to.",
             "correct": False,
             "why": "Nothing here says the number has changed. A steady "
                    "population producing thirty young a pair means the "
                    "surplus is dying, not that breeding has increased."},
            {"text": "Most of the young die before they breed, so there is a "
                     "competition to be among those that do not.",
             "correct": True},
            {"text": "The field must be running out of room, so the population "
                     "will crash soon and then stay low for years.",
             "correct": False,
             "why": "It is not filling up, because most of the young never "
                    "reach adulthood. The population is steady precisely "
                    "because so few survive."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s10",
        "band": "standard",
        "text": "Which of these is competition between members of the same "
                "species?",
        "options": [
            {"text": "An owl hunting mice in a field at night.",
             "correct": False,
             "why": "That is a predator and its prey. The owl and the mouse "
                    "are not short of the same thing — one of them is the "
                    "thing."},
            {"text": "Two mice from the same litter both needing the only dry "
                     "burrow.",
             "correct": True},
            {"text": "A single mouse sheltering from a hard frost under a "
                     "hedge at the field edge.",
             "correct": False,
             "why": "Nothing is being competed for here. Competition needs two "
                    "organisms and one limited resource between them."},
            {"text": "A virus spreading through a mouse population during a "
                     "mild year when numbers are high.",
             "correct": False,
             "why": "A disease is not competition either, although it acts as "
                    "the same filter — whichever variations happen to help you "
                    "avoid infection are the ones passed on."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s11",
        "band": "standard",
        "text": "In a crowded year with too many mice and too few burrows, the "
                "largest and heaviest mice do best. A student concludes that "
                "the strongest animals always win in the end. What is wrong "
                "with that conclusion?",
        "options": [
            {"text": "Nothing is wrong with it — winning confrontations is "
                     "what survival comes down to.",
             "correct": False,
             "why": "It comes down to that in a crowded year and to almost "
                    "nothing else in a drought, where a large body is a bill "
                    "the animal cannot pay."},
            {"text": "Large is not the same as strong, so the conclusion is "
                     "about the wrong animals.",
             "correct": False,
             "why": "A larger, heavier mouse really does win confrontations "
                    "over burrows. The error is in the word always, not in "
                    "which mouse won."},
            {"text": "Size wins where the competition is with your own kind, "
                     "and costs the animal dearly in a drought.",
             "correct": True},
            {"text": "The largest mice only win because there happen to be "
                     "more of them in a crowded year.",
             "correct": False,
             "why": "A survival chance is the chance for one animal carrying "
                    "that variation, not a headcount. Doubling the population "
                    "raises nobody's odds."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s12",
        "band": "standard",
        "text": "Small, quick mice are the least likely of all to survive a "
                "hard winter, even though speed helps them a great deal at "
                "other times. Why?",
        "options": [
            {"text": "A small body loses heat quickly for its size, and speed "
                     "is no defence against cold.",
             "correct": True},
            {"text": "Quick mice use up their food reserves faster because "
                     "they never stay still.",
             "correct": False,
             "why": "Activity is not the problem. A small animal loses heat "
                    "fast relative to its mass, which is a matter of its shape "
                    "rather than its habits."},
            {"text": "Small mice are the weakest members of any population, so "
                     "they lose out whenever conditions are hard.",
             "correct": False,
             "why": "The same mice are the best survivors of a long drought, "
                    "where being small and needing little water is exactly "
                    "right. There is no weakest kind."},
            {"text": "Snow makes small animals easier for predators to see.",
             "correct": False,
             "why": "What kills mice in a hard winter is the cold and the "
                    "buried food, not a predator. Being small is a "
                    "disadvantage here for a reason that has nothing to do "
                    "with being seen."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s13",
        "band": "standard",
        "text": "In one mild year there is no weather problem at all, and yet "
                "many mice die. The population has doubled, and there is not "
                "enough food and there are not enough burrows. What is the "
                "part of the environment doing the damage that year?",
        "options": [
            {"text": "The weather, which must have been worse than it "
                     "appeared to the mice living through it.",
             "correct": False,
             "why": "The year is stated to be mild. Nothing about the weather "
                    "is doing the killing, which is what makes this year worth "
                    "looking at."},
            {"text": "Nothing — a mild year cannot be a hard environment.",
             "correct": False,
             "why": "It can, and this one is. An environment is everything "
                    "around an organism that affects it, and in this year that "
                    "is mostly other mice."},
            {"text": "Predators, which always increase when a population "
                     "doubles.",
             "correct": False,
             "why": "No predator has been mentioned, and one is not needed. "
                    "The shortage is of food and burrows, and the competition "
                    "is with the other mice."},
            {"text": "The other mice, because they need exactly the same food "
                     "and the same burrows.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-01-h05",
        "band": "harder",
        "text": "In a hard winter, 45 out of every 100 small quick mice "
                "survive. In a long drought, 85 out of every 100 of the same "
                "kind survive. In a population of 200 such mice, how many more "
                "survive the drought than survive the winter?",
        "options": [
            {"text": "40 mice",
             "correct": False,
             "why": "That is the difference between the two percentages, and a "
                    "percentage is not a number of mice. Each rate has to be "
                    "applied to the 200 animals first."},
            {"text": "80 mice",
             "correct": True},
            {"text": "170 mice",
             "correct": False,
             "why": "That is how many survive the drought. The question asks "
                    "how many more than the winter, so the 90 winter survivors "
                    "have still to be taken off."},
            {"text": "260 mice",
             "correct": False,
             "why": "That is the two sets of survivors added together, which "
                    "is more mice than the population holds. A difference is "
                    "found by subtracting."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h06",
        "band": "harder",
        "text": "Dandelions vary in the height of their flower stalks. On a "
                "lawn mown every week the short-stalked plants flower below "
                "the blade and set seed, while on an unmown meadow the tall "
                "ones reach the light and the short ones are shaded out. Which "
                "statement is correct?",
        "options": [
            {"text": "Short stalks are the better variation, because a mown "
                     "lawn is the harder place to live.",
             "correct": False,
             "why": "Better always has to name conditions. On the meadow the "
                    "short-stalked plants are shaded out, and the mowing that "
                    "saved them is not there."},
            {"text": "The dandelions on the lawn shortened their stalks in "
                     "response to being mown.",
             "correct": False,
             "why": "A plant does not rebuild itself to suit the mower. The "
                    "short-stalked plants were already there; the mowing "
                    "decided which ones set seed."},
            {"text": "Each stalk height is an advantage in one of the two "
                     "places and a disadvantage in the other.",
             "correct": True},
            {"text": "Neither height can be an advantage, because each of them "
                     "fails somewhere.",
             "correct": False,
             "why": "Every variation fails somewhere, and that does not cancel "
                    "it out. An advantage is one that pays for itself in the "
                    "conditions the organism is actually in."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h07",
        "band": "harder",
        "text": "Mountain hares turn white for the winter. In one region the "
                "snow now arrives about a month later than it used to, so "
                "white hares spend four weeks on brown ground with foxes "
                "hunting. Which statement is correct?",
        "options": [
            {"text": "The hares will stop turning white, because the change no "
                     "longer suits them.",
             "correct": False,
             "why": "No hare decides when to turn white or chooses to stop. "
                    "Whether the population's timing shifts depends on which "
                    "hares survive to breed, and that takes generations."},
            {"text": "Turning white was always a poor variation, and the late "
                     "snow has exposed it.",
             "correct": False,
             "why": "It was an excellent one for as long as the snow arrived "
                    "when the coat did. What has changed is the timing of the "
                    "snow, not the quality of the coat."},
            {"text": "Hares whose coats change late are simply better animals "
                     "than the rest.",
             "correct": False,
             "why": "Better in these four weeks and much worse once the snow "
                    "lies deep. Neither timing is better in general — which "
                    "one pays depends on when the snow comes."},
            {"text": "The same variation has become a disadvantage because the "
                     "conditions moved, not because the hares changed.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h08",
        "band": "harder",
        "text": "A student learns that whether a variation helps depends on "
                "the conditions, and concludes that no variation is ever "
                "really an advantage at all. What is wrong with that?",
        "options": [
            {"text": "An advantage is real in the conditions it applies to — "
                     "it is a general advantage that does not exist.",
             "correct": True},
            {"text": "Nothing is wrong: since every variation fails somewhere, "
                     "none of them is worth anything at all to the "
                     "animal that carries it.",
             "correct": False,
             "why": "A thick coat that carries a mouse through eight weeks of "
                    "snow is worth a great deal that winter. What it is not is "
                    "worth something everywhere."},
            {"text": "Some variations really do work everywhere, which is what "
                     "the student has missed.",
             "correct": False,
             "why": "None of the visible ones does. Even a variation that "
                    "helps in four conditions out of five gives no protection "
                    "against a new disease."},
            {"text": "The student is wrong because strength is an advantage in "
                     "every environment.",
             "correct": False,
             "why": "Strength is one variation among many and often the wrong "
                    "one. In a drought the animal that needs least water wins, "
                    "and it never has to fight anything."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h09",
        "band": "harder",
        "text": "A pond receives about two thousand frog eggs each spring and "
                "holds about forty adult frogs each summer. One year the pond "
                "half dries out by early July. Which tadpoles are most likely "
                "to be among the survivors?",
        "options": [
            {"text": "Whichever ones happen to have variations that suit a "
                     "drying pond, such as developing fastest.",
             "correct": True},
            {"text": "The largest ones, since size decides most contests in a "
                     "crowded pond.",
             "correct": False,
             "why": "Size wins where the competition is with your own kind "
                    "over food and space. In a drying pond the question is "
                    "whether an animal completes its development before the "
                    "water goes."},
            {"text": "The ones whose parents survived a drying pond and passed "
                     "that experience on.",
             "correct": False,
             "why": "Experience is not passed on. What a parent went through "
                    "in its own life does not change the genes in its eggs."},
            {"text": "None of them, since a pond that dries in July cannot "
                     "produce any frogs.",
             "correct": False,
             "why": "Some will already be close to leaving the water. Two "
                    "thousand eggs producing a handful of frogs is the "
                    "ordinary state of affairs, not a failure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h10",
        "band": "harder",
        "text": "A wildlife team is moving fifty mice to an island where "
                "nobody has yet recorded the winters, the predators or the "
                "diseases. They can take fifty thick-coated mice, fifty small "
                "quick mice, or fifty mice covering all five kinds of "
                "variation. Which choice is better supported?",
        "options": [
            {"text": "The thick-coated fifty, because a thick coat is the "
                     "strongest variation of the five.",
             "correct": False,
             "why": "It is the best in a hard winter and the worst in a "
                    "drought. Choosing it is a bet on conditions nobody has "
                    "measured."},
            {"text": "It makes no difference which fifty go, since the "
                     "conditions will decide the outcome anyway.",
             "correct": False,
             "why": "The conditions decide which variations pay, and the mice "
                    "decide which variations are there to pay. A group with "
                    "only one kind has nothing else to offer."},
            {"text": "The mixed fifty, because which variation is an advantage "
                     "depends on conditions nobody has measured yet.",
             "correct": True},
            {"text": "The small quick fifty, because being quick helps against "
                     "predators and in a drought.",
             "correct": False,
             "why": "It does, in those two. It is also the worst variation to "
                    "carry through a hard winter, and nobody knows yet what "
                    "the island's winters are like."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h11",
        "band": "harder",
        "text": "One mouse has thirty young, of which three live long enough "
                "to breed. Another has eight young, of which five live long "
                "enough to breed. Which mouse has the greater fitness?",
        "options": [
            {"text": "The first, because thirty young is far more than eight.",
             "correct": False,
             "why": "Fitness counts the offspring that survive to breed, not "
                    "the ones that are born. Three of the thirty got there; "
                    "five of the eight did."},
            {"text": "The second, because five of its young survive to breed "
                     "against three of the other's.",
             "correct": True},
            {"text": "The first, provided it also lives longer than the "
                     "second.",
             "correct": False,
             "why": "Length of life counts for nothing on its own. An animal "
                    "that lives fifty years and never breeds has a fitness of "
                    "zero."},
            {"text": "Neither — fitness is about how well suited an animal is, "
                     "not about counting offspring.",
             "correct": False,
             "why": "Being well suited is what makes surviving offspring more "
                    "likely, and those offspring are how it is counted. The "
                    "count is the measure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h12",
        "band": "harder",
        "text": "A comparison of variations gives each mouse exactly one "
                "difference: one is large, one has a thick coat, one is quick, "
                "one is bold, one is pale. A real mouse carries all of those "
                "at once, in some combination. What does that mean for the "
                "conclusion drawn?",
        "options": [
            {"text": "It makes the conclusion worthless, since no real mouse "
                     "is like any of the five.",
             "correct": False,
             "why": "The conclusion is that which variation pays depends on "
                    "the conditions, and that holds however many variations an "
                    "animal carries. Simplifying is how the point is made "
                    "readable."},
            {"text": "It means a real mouse would survive everything, since "
                     "it carries all five variations at once.",
             "correct": False,
             "why": "It would carry all five costs as well. A large body needs "
                    "more food and water and a thick coat overheats, so the "
                    "bill arrives with the benefit."},
            {"text": "It means real fitness depends only on the strongest of "
                     "an animal's variations.",
             "correct": False,
             "why": "There is no strongest. Different conditions call on "
                    "different variations, and a real animal's chances depend "
                    "on the whole combination at once."},
            {"text": "The conclusion holds; real fitness depends on many "
                     "characteristics at once.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h13",
        "band": "harder",
        "text": "In a seabird colony some birds nest on narrow high ledges and "
                "some on wide low ones. Rats reach the island and take eggs "
                "from the low ledges. A student says this cannot be "
                "competition, so it has nothing to do with which variations "
                "get passed on. What is the correct reply?",
        "options": [
            {"text": "It is competition, because the birds and the rats are "
                     "both after the eggs.",
             "correct": False,
             "why": "The rats eat the eggs and the birds do not, so the two "
                    "are not short of the same thing. That is a predator and "
                    "its prey."},
            {"text": "The student is right: only competition between members "
                     "of one species affects which variations are passed on.",
             "correct": False,
             "why": "Predators and disease are not competition, and they act "
                    "as the same filter. Whichever variations help you avoid "
                    "being eaten are the ones that get passed on."},
            {"text": "It is not competition, and it acts as the same filter — "
                     "the birds on high ledges keep more eggs.",
             "correct": True},
            {"text": "It is not competition, so it will affect how many birds "
                     "there are but not which kinds of bird there are.",
             "correct": False,
             "why": "It affects both. If low-ledge nesters lose more eggs, "
                    "fewer of their young join the colony, and the make-up of "
                    "the colony shifts with it."},
        ],
        "figure": None,
    },

    # ── MRB-338 night 3 top-up · easier ─────────────────────────────────
    {
        "id": "b11-01-e14",
        "band": "easier",
        "text": "In this lesson, what does it mean to call a variation an "
                "advantage?",
        "options": [
            {"text": "That it makes an individual larger, stronger or faster "
                     "than the rest of its population.",
             "correct": False,
             "why": "Strength is one variation among many and is often the "
                    "wrong one. In a drought the animal that needs least "
                    "water wins without ever being strong."},
            {"text": "That it makes an individual more likely to survive and "
                     "reproduce in the conditions it is in.",
             "correct": True},
            {"text": "That no other member of the population happens to "
                     "carry it at that moment.",
             "correct": False,
             "why": "How rare a variation is has nothing to do with whether "
                    "it helps. A common variation can pay handsomely and a "
                    "rare one can do nothing at all."},
            {"text": "That it will help the individual wherever it lives and "
                     "whatever happens to it.",
             "correct": False,
             "why": "No variation does that, which is the whole point of the "
                    "lesson. A thick coat saves a mouse in a hard winter and "
                    "cooks it in a drought."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e15",
        "band": "easier",
        "text": "A biologist describes a species as adapted. What does the "
                "word mean?",
        "options": [
            {"text": "It has changed its own body to suit the place it ended "
                     "up living in.",
             "correct": False,
             "why": "No organism rebuilds itself to order. Adapted describes "
                    "the variations an organism already has, not something "
                    "it did during its life."},
            {"text": "It is further along in its evolution than the species "
                     "living around it.",
             "correct": False,
             "why": "There is no further along to be. Every living species "
                    "has been evolving for exactly as long as every other "
                    "one."},
            {"text": "It is suited to a particular environment by the "
                     "variations it happens to have.",
             "correct": True},
            {"text": "It is able to live successfully in any environment it "
                     "is put into.",
             "correct": False,
             "why": "That would be the opposite of adapted. Being well "
                    "suited to one place is usually what makes an organism "
                    "badly suited to another."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e16",
        "band": "easier",
        "text": "A biologist records an animal's fitness as zero. What does "
                "that tell you about it?",
        "options": [
            {"text": "It died before it was fully grown, so it never "
                     "competed for anything at all.",
             "correct": False,
             "why": "An animal can live a long adult life and still have a "
                    "fitness of zero. What the figure records is offspring, "
                    "not length of life."},
            {"text": "It left no offspring that survived to breed.",
             "correct": True},
            {"text": "It was the weakest animal in its population.",
             "correct": False,
             "why": "Fitness is nothing to do with strength. A large strong "
                    "animal that never breeds has exactly the same figure as "
                    "a small weak one that never breeds."},
            {"text": "It was badly suited to its surroundings.",
             "correct": False,
             "why": "It may have been superbly suited and simply never found "
                    "a mate. Fitness counts the result, not how comfortable "
                    "the animal's life was."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e17",
        "band": "easier",
        "text": "In a hard winter with food scarce and buried, large heavy "
                "mice do fairly well, though not best of all. What are the "
                "two sides of being large in that winter?",
        "options": [
            {"text": "A large body loses heat more slowly, and it needs more "
                     "food, which is scarce.",
             "correct": True},
            {"text": "A large mouse frightens off its rivals, and moves too "
                     "slowly through deep snow to escape anything.",
             "correct": False,
             "why": "Nothing is hunting in this winter and nothing is being "
                    "escaped from. The danger is the cold and the shortage "
                    "of food."},
            {"text": "A large mouse can dig deeper to reach the buried food.",
             "correct": False,
             "why": "Size is not a digging advantage here. What it gives is "
                    "a body that holds its heat, and what it costs is an "
                    "appetite the winter cannot feed."},
            {"text": "A large mouse carries more fat, and is easier to see "
                     "on snow.",
             "correct": False,
             "why": "Being seen is the owl's panel, not the winter's. Here "
                    "the cost of size is the food it takes to keep a large "
                    "body going."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e18",
        "band": "easier",
        "text": "In a hard winter the food is buried and scarce. Bold, "
                "exploratory mice come out middling — neither best nor "
                "worst. Why does boldness both help and cost them here?",
        "options": [
            {"text": "They are the first to reach any food, and the last to "
                     "notice a predator creeping up on them in the snow.",
             "correct": False,
             "why": "No predator is part of this winter. What boldness costs "
                    "here is time spent out in the cold, not attention paid "
                    "to a hunter."},
            {"text": "They eat more than the others do, and they also find "
                     "more than the others find.",
             "correct": False,
             "why": "Boldness is a habit rather than an appetite. It does "
                    "not change how much a mouse needs; it changes where the "
                    "mouse goes looking."},
            {"text": "They search further for buried food, and are exposed "
                     "to the cold while doing it.",
             "correct": True},
            {"text": "They keep moving, which keeps them warm, and it uses "
                     "up the fat they need to last the eight weeks out.",
             "correct": False,
             "why": "The lesson's reason is about where a bold mouse goes, "
                    "not about how warm moving keeps it. Searching further "
                    "finds food and costs exposure."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e19",
        "band": "easier",
        "text": "Snow lies over a field for eight weeks and a barn owl hunts "
                "over it. Why does pale sandy fur help a mouse there?",
        "options": [
            {"text": "Owls hunt by smell, not by sight.",
             "correct": False,
             "why": "A barn owl hunts by sight and by sound, which is why a "
                    "mouse's colour matters to it at all. Fur colour has no "
                    "smell of its own."},
            {"text": "Pale fur reflects the cold away from the mouse's skin, "
                     "so the animal stays warmer than a dark-furred one "
                     "does.",
             "correct": False,
             "why": "Fur keeps heat in by trapping air, and its colour does "
                    "not change that. What pale fur does over snow is make "
                    "the mouse hard to pick out."},
            {"text": "Pale mice are more active in cold weather, so they "
                     "reach what little food there is before the others get "
                     "to it.",
             "correct": False,
             "why": "Colour does not set how active an animal is. Being hard "
                    "to see is the whole of the advantage here."},
            {"text": "Pale fur is difficult for an owl to see against snow.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e20",
        "band": "easier",
        "text": "A barn owl takes up residence in a field. Large, heavy mice "
                "do worse than they did before it arrived. Why?",
        "options": [
            {"text": "Large mice eat more, so they have to spend longer out "
                     "in the field feeding than the small ones do.",
             "correct": False,
             "why": "Time spent feeding is the bold mouse's problem here. "
                    "What size costs against an owl is speed to cover and a "
                    "body that is easy to spot."},
            {"text": "Large mice cannot survive cold weather.",
             "correct": False,
             "why": "Large mice do well in a hard winter, because a big body "
                    "holds its heat. The owl is a separate problem and a "
                    "separate panel."},
            {"text": "The other mice turn on them once a predator is about.",
             "correct": False,
             "why": "The owl changes nothing about how mice treat each "
                    "other. It changes who gets caught, and a big slow mouse "
                    "is caught more easily."},
            {"text": "They are slower to reach cover and make a larger "
                     "target.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e21",
        "band": "easier",
        "text": "A barn owl hunts over a field of dark peaty soil. Mice with "
                "pale sandy fur do very badly. Why?",
        "options": [
            {"text": "Pale fur is the most visible thing in a field of dark "
                     "peat.",
             "correct": True},
            {"text": "Pale mice are smaller than the others, so an owl can "
                     "carry one away more easily than it can carry a heavy "
                     "one.",
             "correct": False,
             "why": "Fur colour says nothing about size. What pale fur does "
                    "over dark ground is make a mouse easy to find, and "
                    "being found is the whole danger."},
            {"text": "Pale fur reflects moonlight and warms the mouse, so it "
                     "moves about more at night than the others do.",
             "correct": False,
             "why": "Fur colour does not change how active a mouse is. It "
                    "changes how well the mouse matches the ground it is "
                    "standing on."},
            {"text": "Pale mice have poorer night vision.",
             "correct": False,
             "why": "Nothing links coat colour to eyesight. The problem is "
                    "that the owl sees the mouse, not that the mouse fails "
                    "to see the owl."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e22",
        "band": "easier",
        "text": "Months pass with no rain. Large, heavy mice now do worse "
                "than almost any other kind. What has gone wrong for them?",
        "options": [
            {"text": "Their size makes them slow, and in dry weather they "
                     "cannot outrun the animals that hunt them.",
             "correct": False,
             "why": "Nothing is hunting in a drought panel. What is killing "
                    "mice is the shortage of water and the heat, and a large "
                    "body is expensive in both."},
            {"text": "Large mice lose heat faster than small ones.",
             "correct": False,
             "why": "A large body loses heat more slowly, not faster, which "
                    "is why size helps in a winter. In a drought the problem "
                    "is getting rid of heat, not keeping it."},
            {"text": "A big body needs more water and more food, and there "
                     "is neither.",
             "correct": True},
            {"text": "The drought has made them too thin to win a fight.",
             "correct": False,
             "why": "No mouse on the bench changes. The animals are the same "
                    "in every panel, and what has moved is the conditions "
                    "around them."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e23",
        "band": "easier",
        "text": "In a drought that has lasted months, bold and exploratory "
                "mice come out a little above the middle. What does boldness "
                "do for them in those conditions?",
        "options": [
            {"text": "It finds the few remaining water sources, and it takes "
                     "risks doing it.",
             "correct": True},
            {"text": "It makes them fight the other mice for a share of what "
                     "water is left, and they usually win those fights.",
             "correct": False,
             "why": "Boldness is a willingness to explore, not a willingness "
                    "to fight. Winning confrontations is what size does, and "
                    "it does it in a crowded year."},
            {"text": "It keeps them moving, so they cool down faster.",
             "correct": False,
             "why": "Moving about in a drought heats an animal and costs it "
                    "water. What boldness buys is finding water, not losing "
                    "heat."},
            {"text": "It makes them dig deeper burrows, where the soil is "
                     "still damp and the air is cooler than it is above "
                     "ground.",
             "correct": False,
             "why": "Nothing on the bench gives a bold mouse a better "
                    "burrow. Its advantage is that it goes further and finds "
                    "water the others have not reached."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e24",
        "band": "easier",
        "text": "In a mild year the population doubles, food runs short and "
                "burrows are fought over. Mice with a thick coat come out "
                "exactly average. Why?",
        "options": [
            {"text": "A thick coat is a small advantage in a mild year, "
                     "which is why the figure is neither high nor low.",
             "correct": False,
             "why": "It is no advantage at all here. The shortage is of food "
                    "and burrows, and a coat does nothing about either of "
                    "them."},
            {"text": "The other mice leave a thick-coated mouse alone, so it "
                     "neither wins nor loses any of the contests over food.",
             "correct": False,
             "why": "A thick coat does not make a mouse harder to push off a "
                    "food pile. It simply has no bearing on this year's "
                    "problem in either direction."},
            {"text": "A thick coat slows a mouse down as much as it warms "
                     "it, so the two effects cancel out over the year.",
             "correct": False,
             "why": "Nothing here is being cancelled out. A coat is neither "
                    "an advantage nor a cost in a mild crowded year — it is "
                    "simply beside the point."},
            {"text": "In a mild year the coat brings no advantage and no "
                     "cost.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e25",
        "band": "easier",
        "text": "Eight weeks of snow lie over a field and the food is "
                "buried. What is the main way a mouse dies in those "
                "conditions?",
        "options": [
            {"text": "By being caught by a predator that can see it more "
                     "easily against the snow than it could before.",
             "correct": False,
             "why": "A predator arriving is a different set of conditions "
                    "altogether. In a hard winter what kills mice is the "
                    "cold and the food it cannot reach."},
            {"text": "By losing heat faster than it can replace it.",
             "correct": True},
            {"text": "By being pushed off the few remaining feeding places "
                     "by the larger and heavier members of the population.",
             "correct": False,
             "why": "Being displaced by bigger mice is what happens in a "
                    "crowded year. In a hard winter the cold is doing the "
                    "killing, not the other mice."},
            {"text": "By drinking snow, which chills the animal from the "
                     "inside and uses energy it cannot spare in a hard "
                     "winter.",
             "correct": False,
             "why": "That is not the danger the lesson names. Losing heat is "
                    "the main way to die in a hard winter, which is why "
                    "insulation is worth so much."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e26",
        "band": "easier",
        "text": "A stag with enormous antlers wins his fights and then "
                "starves in a hard winter carrying them. What does that "
                "example show?",
        "options": [
            {"text": "That antlers are a poor variation for a deer to carry "
                     "at any time of year.",
             "correct": False,
             "why": "They win him his fights, which is exactly what they are "
                    "for. The cost only falls due when the winter turns "
                    "hard."},
            {"text": "That the same variation can win in one set of "
                     "conditions and kill in another.",
             "correct": True},
            {"text": "That a stag should shed its antlers before the winter "
                     "arrives to avoid the cost of carrying them.",
             "correct": False,
             "why": "No animal decides what to grow or when to shed it to "
                    "suit the year ahead. The stag has the antlers it has."},
            {"text": "That fighting is the most important kind of "
                     "competition there is for a large animal.",
             "correct": False,
             "why": "Most competition never involves a fight. In a hard "
                    "winter the stag is not losing a contest with another "
                    "deer — it is losing one with the cold."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e27",
        "band": "easier",
        "text": "Arctic foxes have small ears and thick fur. Desert foxes "
                "have very large ears and thin fur. What does that "
                "difference show?",
        "options": [
            {"text": "That each is suited to the place it lives, because "
                     "losing heat is a danger in one place and a necessity "
                     "in the other.",
             "correct": True},
            {"text": "That the desert fox is the more advanced of the two, "
                     "since large ears are a more complicated structure to "
                     "grow.",
             "correct": False,
             "why": "There is no ranking of advancement in biology. Neither "
                    "fox is further along than the other; they are suited to "
                    "different places."},
            {"text": "That a fox grows the ears it needs for the climate it "
                     "finds itself living in.",
             "correct": False,
             "why": "An animal does not build itself to suit its "
                    "surroundings. Each fox has the ears it was born with."},
            {"text": "That the arctic fox is the tougher animal, because the "
                     "Arctic is the harder of the two places to survive in.",
             "correct": False,
             "why": "Put the arctic fox in the desert and it would be in "
                    "serious trouble. Neither environment is harder in "
                    "general; each is hard for the animal not suited to it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e28",
        "band": "easier",
        "text": "A cactus stores water in a thick stem, which keeps it alive "
                "through months of drought. Why is that same thick stem no "
                "advantage in a wet rainforest?",
        "options": [
            {"text": "Because rainforest plants grow faster, so the cactus "
                     "would be out of date within a few years of arriving "
                     "there.",
             "correct": False,
             "why": "Nothing goes out of date. A stored supply of water is "
                    "simply worth nothing where water is never short."},
            {"text": "Because the cactus would take in so much water that "
                     "its thick stem would split open under the pressure.",
             "correct": False,
             "why": "The reason is much simpler than that. Storing water is "
                    "only worth the effort where there are times when there "
                    "is none to be had."},
            {"text": "Because water is never scarce there, so storing it "
                     "buys the plant nothing.",
             "correct": True},
            {"text": "Because a thick stem is only useful to a plant that is "
                     "growing in full sunlight rather than in shade.",
             "correct": False,
             "why": "Light is a separate problem. What a thick stem does is "
                    "hold water, and holding water pays only where water "
                    "runs out."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e29",
        "band": "easier",
        "text": "Being large and heavy is an advantage to a mouse in some "
                "conditions. What is the cost that comes with it?",
        "options": [
            {"text": "A large mouse needs more food and more water than a "
                     "small one.",
             "correct": True},
            {"text": "A large mouse loses its body heat much more quickly "
                     "than a small one does, so it suffers badly in the "
                     "cold.",
             "correct": False,
             "why": "It is the other way round. A large body loses heat more "
                    "slowly for its mass, which is why size helps in a hard "
                    "winter."},
            {"text": "A large mouse cannot squeeze into a burrow, so it has "
                     "nowhere safe to shelter when the weather turns against "
                     "it.",
             "correct": False,
             "why": "Size does not lock a mouse out of shelter. Its real "
                    "cost is an appetite and a thirst that have to be met "
                    "every day."},
            {"text": "A large mouse produces fewer young than a small one, "
                     "so it leaves less behind it whatever else happens.",
             "correct": False,
             "why": "Nothing in the lesson links body size to litter size. "
                    "The bill a large mouse pays is in food and water."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-e30",
        "band": "easier",
        "text": "Two oak saplings grow a metre apart and both need the same "
                "light, water and minerals from the soil. Are they "
                "competing?",
        "options": [
            {"text": "No, because plants cannot move, and competition needs "
                     "two organisms that can reach the same place at the "
                     "same time.",
             "correct": False,
             "why": "Neither tree has to move anywhere. Their roots and "
                    "branches are already reaching into the same soil and "
                    "the same light."},
            {"text": "No, because competition is something that happens "
                     "between animals rather than between plants.",
             "correct": False,
             "why": "Plants compete as fiercely as anything does. Shading a "
                    "rival out is one of the most common contests in "
                    "biology."},
            {"text": "Yes, but only once one of them grows tall enough to "
                     "put the other completely in its shadow.",
             "correct": False,
             "why": "The competition starts as soon as the supply is shared "
                    "and short. Shading is one way it is settled, not the "
                    "moment it begins."},
            {"text": "Yes, because they need the same limited things, so one "
                     "taking them means the other does not.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-01-s14",
        "band": "standard",
        "text": "A famine reduces the food available to a population of "
                "animals to a fraction of what it was. Which individuals "
                "would you expect to come through it?",
        "options": [
            {"text": "The largest ones, because they carry the most fat to "
                     "live off while the shortage lasts.",
             "correct": False,
             "why": "A large body carries reserves and also demands far more "
                    "food to keep going. In a famine the demand is the side "
                    "that decides it."},
            {"text": "The ones that can survive on the least food.",
             "correct": True},
            {"text": "The strongest ones in the population.",
             "correct": False,
             "why": "Strength settles a contest over a food pile, and a "
                    "famine is a shortage rather than a contest. Winning a "
                    "fight for nothing gains an animal nothing."},
            {"text": "The youngest ones, which need less food.",
             "correct": False,
             "why": "A growing animal needs more food for its size, not "
                    "less. Nothing about being young reduces what an animal "
                    "has to eat."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s15",
        "band": "standard",
        "text": "Rabbits in a field vary in leg length. A fox starts hunting "
                "there, and the field is open grass with cover only at the "
                "hedge. Which rabbits have the advantage, and what would "
                "change the answer?",
        "options": [
            {"text": "The longer-legged ones, and thick cover across the "
                     "whole field would change it.",
             "correct": True},
            {"text": "The longer-legged ones, and nothing would change it, "
                     "because outrunning a predator is always worth having.",
             "correct": False,
             "why": "In thick cover a rabbit that freezes close to the "
                    "ground may do better than one that runs. Which "
                    "variation pays depends on the ground it is standing on."},
            {"text": "The shorter-legged ones, because a small rabbit is "
                     "harder for a fox to see across open grass.",
             "correct": False,
             "why": "On open grass with the hedge a long way off, the "
                    "contest is a chase rather than a search. Speed is what "
                    "decides it."},
            {"text": "Neither, because a fox catches whichever rabbit it "
                     "happens to start after first.",
             "correct": False,
             "why": "A fox starts after many rabbits and catches some of "
                    "them. Which ones it catches is exactly what leg length "
                    "changes."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s16",
        "band": "standard",
        "text": "On a rocky shore, barnacles high up the rock are left dry "
                "for hours by the falling tide, while barnacles low down are "
                "reached and eaten by whelks. Which position is better?",
        "options": [
            {"text": "Low down, because being eaten is a risk while drying "
                     "out is merely uncomfortable for a shelled animal.",
             "correct": False,
             "why": "Drying out kills a barnacle as surely as a whelk does. "
                    "Neither position is safe, which is why neither is "
                    "better in general."},
            {"text": "High up, because a barnacle that avoids predators will "
                     "always leave more offspring in the end.",
             "correct": False,
             "why": "Not if it dries out first. An animal that escapes one "
                    "danger and meets another has not escaped anything."},
            {"text": "Neither: each position carries a different danger, so "
                     "which is better depends on the shore.",
             "correct": True},
            {"text": "Both are equally bad, so barnacles would do better to "
                     "settle somewhere other than a rocky shore.",
             "correct": False,
             "why": "Barnacles do extremely well on rocky shores, which is "
                    "where almost all of them live. Each position carries a "
                    "cost and each supports a great many animals."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s17",
        "band": "standard",
        "text": "Some clover plants make a chemical that tastes bitter to "
                "slugs, and making it uses sugar the plant could have spent "
                "on growth. In which conditions is the bitter kind at an "
                "advantage?",
        "options": [
            {"text": "In any conditions, because a plant that cannot be "
                     "eaten has an advantage over one that can.",
             "correct": False,
             "why": "It pays for that protection in growth every day, slugs "
                    "or no slugs. Where there are no slugs it is spending "
                    "sugar for nothing."},
            {"text": "Only where the soil is poor and growth is slow.",
             "correct": False,
             "why": "Making an extra chemical needs more from the plant, not "
                    "less. Poor soil makes the cost harder to bear rather "
                    "than easier."},
            {"text": "Only in a wet year, when slugs are commonest.",
             "correct": False,
             "why": "Wet weather does make slugs commoner, and the point "
                    "holds in a dry year with slugs too. What matters is "
                    "whether the slugs are there, not the weather that "
                    "brought them."},
            {"text": "Where slugs are common, and it is a cost where they "
                     "are not.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s18",
        "band": "standard",
        "text": "Two mice of the same species are alike in every way except "
                "that one needs about 5 ml of water a day and the other "
                "about 12 ml. Months pass with no rain. What would you "
                "expect?",
        "options": [
            {"text": "The 5 ml mouse is more likely to survive, because it "
                     "can meet its needs from far less water.",
             "correct": True},
            {"text": "The 12 ml mouse is more likely to survive, because "
                     "taking in more water keeps its body cooler through the "
                     "heat of the day.",
             "correct": False,
             "why": "Taking in more water is only possible if there is water "
                    "to take. In a drought the higher requirement is a bill "
                    "the animal cannot pay."},
            {"text": "They are equally likely to survive, because both will "
                     "drink whatever water they can find.",
             "correct": False,
             "why": "Both will drink what they find, and one of them runs "
                    "out of what it needs long before the other does. That "
                    "difference is the whole contest."},
            {"text": "The 12 ml mouse is more likely to survive, because an "
                     "animal that needs more water is the larger and "
                     "stronger of the two.",
             "correct": False,
             "why": "Strength is not what a drought asks for. The animal "
                    "that needs least water wins, and it never has to fight "
                    "anything."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s19",
        "band": "standard",
        "text": "Some plants of one species make many small seeds and others "
                "make a few large ones, each with a store of food. Where "
                "would the large-seeded plants have the advantage?",
        "options": [
            {"text": "On bare ground newly cleared by a fire, where nothing "
                     "is growing and there is light everywhere.",
             "correct": False,
             "why": "Bare open ground is where numbers pay. Many small seeds "
                    "land in many places, and none of them needs a food "
                    "store to reach the light."},
            {"text": "Under deep shade, where a seedling needs a food store "
                     "to reach the light.",
             "correct": True},
            {"text": "In a windy place, because a large seed is carried "
                     "further on the wind than a small one is.",
             "correct": False,
             "why": "Wind carries a small light seed much further. Weight is "
                    "a cost to a seed in the air and a store of food once it "
                    "lands."},
            {"text": "Anywhere at all: a food store is always a better "
                     "start.",
             "correct": False,
             "why": "The parent plant can make a few large seeds or many "
                    "small ones, and not both. Where light is easy, the many "
                    "is the better bet."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s20",
        "band": "standard",
        "text": "In one field the snow lies for eight weeks and then the "
                "ground is bare dark peat for the rest of the year, with an "
                "owl hunting throughout. What can you say about pale sandy "
                "fur in that field?",
        "options": [
            {"text": "It is a cost throughout, because an owl will learn "
                     "what a pale mouse looks like and hunt for it all year.",
             "correct": False,
             "why": "An owl finds what it can see. Over snow a pale mouse is "
                    "the hardest of the lot to see, whatever the owl has "
                    "learned."},
            {"text": "It is an advantage overall, because being hidden for "
                     "eight weeks outweighs being visible at other times.",
             "correct": False,
             "why": "Eight weeks is a small part of a year. The arithmetic "
                    "runs the other way, and in any case it depends on when "
                    "the owl hunts hardest rather than on a count of weeks."},
            {"text": "It is neither an advantage nor a cost, because the two "
                     "halves of the year cancel each other out exactly.",
             "correct": False,
             "why": "Nothing says the two halves are equal. One is eight "
                    "weeks and the other is most of the year, and the "
                    "hunting is not spread evenly across them."},
            {"text": "It is an advantage for the eight snowy weeks and a "
                     "cost for the rest, so whether it pays depends on when "
                     "the hunting is heaviest.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s21",
        "band": "standard",
        "text": "In a mild year the population doubles, so food is short and "
                "burrows are fought over. Both the thick-coated mice and the "
                "pale-furred mice come out right in the middle. What does "
                "that tell you?",
        "options": [
            {"text": "That coat thickness and fur colour are both weak "
                     "variations, which is why neither reaches the top of "
                     "any list.",
             "correct": False,
             "why": "Each of them tops a list somewhere. A thick coat wins a "
                    "hard winter outright, and pale fur is the best thing to "
                    "have over snow."},
            {"text": "That the two variations cancel each other out.",
             "correct": False,
             "why": "Each mouse on the bench carries one variation, so "
                    "nothing is being combined. They are middling for the "
                    "same reason, separately."},
            {"text": "That neither a coat nor a colour has any bearing on a "
                     "shortage of food and burrows.",
             "correct": True},
            {"text": "That the mild weather made it an easy year.",
             "correct": False,
             "why": "The year is anything but easy — the population has "
                    "doubled and there is not enough to go round. Size and "
                    "boldness make a large difference in it."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s22",
        "band": "standard",
        "text": "An owl hunts at night over dark peaty ground with almost no "
                "cover. Which variation would you expect to be worth most to "
                "a mouse there, and why?",
        "options": [
            {"text": "A thick coat, which protects against an owl's talons.",
             "correct": False,
             "why": "No coat saves a mouse that has been caught. What "
                    "decides the night is whether the owl finds and reaches "
                    "it at all."},
            {"text": "A large, heavy body, because an owl will pass over a "
                     "mouse too big for it to carry away.",
             "correct": False,
             "why": "A large mouse is a larger target and slower to reach "
                    "cover, which makes size a serious cost against an owl "
                    "rather than a protection."},
            {"text": "Boldness, because a mouse that keeps moving is harder "
                     "for a hunting bird to follow than one sitting still.",
             "correct": False,
             "why": "Bold means out in the open more often, which is the "
                    "worst habit to have when something is hunting. It is "
                    "the biggest cost of the night."},
            {"text": "Being small and quick, because that means a small "
                     "target and a short run to cover.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s23",
        "band": "standard",
        "text": "Every variation costs an organism something — energy, food, "
                "water or time. How can a variation that costs the animal "
                "anything at all still be an advantage?",
        "options": [
            {"text": "Because in the right conditions what it buys is worth "
                     "more than what it costs.",
             "correct": True},
            {"text": "Because the cost is paid once while the benefit goes "
                     "on for the whole of the animal's life.",
             "correct": False,
             "why": "Most costs are paid continually — a large body has to "
                    "be fed every day. What settles it is whether the return "
                    "covers the bill in those conditions."},
            {"text": "Because a variation that is an advantage costs nothing "
                     "at all to the animal that carries it.",
             "correct": False,
             "why": "The lesson is explicit that every one of them costs "
                    "something. A thick coat costs almost nothing in a "
                    "winter and a great deal in a drought."},
            {"text": "Because the animal can stop paying the cost during the "
                     "seasons when the variation is not needed.",
             "correct": False,
             "why": "It cannot put the variation down. The stag carries his "
                    "antlers into the winter that starves him, because they "
                    "are what he has."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s24",
        "band": "standard",
        "text": "Two kinds of moss grow on walls. One dries out slowly but "
                "grows slowly; the other grows fast but dries out quickly. "
                "On a shaded north wall that stays damp all year, which kind "
                "would you expect to find, and why?",
        "options": [
            {"text": "The slow-drying kind, because resisting drought is the "
                     "harder thing for a plant to do.",
             "correct": False,
             "why": "It is a harder thing to do and it is not needed on a "
                    "wall that never dries. The slow growth that pays for it "
                    "is a cost with nothing bought."},
            {"text": "Neither, because a wall that stays damp suits no moss "
                     "particularly well.",
             "correct": False,
             "why": "A damp shaded wall is excellent moss habitat. The "
                    "question is which of the two kinds does better on it."},
            {"text": "The fast-growing kind, because drying out is not a "
                     "danger there and growth is what wins the space.",
             "correct": True},
            {"text": "Both equally, because the two kinds are of the same "
                     "species and so have the same needs.",
             "correct": False,
             "why": "Members of one species need the same things and do not "
                    "meet them equally well. That difference is exactly what "
                    "decides who holds the wall."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s25",
        "band": "standard",
        "text": "In one set of conditions, four of the five variations being "
                "compared give a mouse the same chance of survival, and the "
                "fifth gives a slightly worse one. What does a result like "
                "that tell you?",
        "options": [
            {"text": "That the conditions cannot have been very severe, "
                     "since almost everything survived them equally well.",
             "correct": False,
             "why": "A threat can be severe and still make no distinction. "
                    "Equal chances mean the danger is indifferent to those "
                    "variations, not that it is mild."},
            {"text": "That the four tied variations are equally good ones "
                     "for a mouse to carry in general.",
             "correct": False,
             "why": "They are tied here and nowhere else. In four other sets "
                    "of conditions the same five spread right out."},
            {"text": "That the comparison was set up wrongly, because a fair "
                     "test always separates the five out.",
             "correct": False,
             "why": "A result in which nothing separates is a real result. "
                    "It is telling you that whatever decides this cannot be "
                    "seen among the five."},
            {"text": "That none of the variations being compared is any help "
                     "against this particular danger.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s26",
        "band": "standard",
        "text": "A student says that competition only happens when food runs "
                "short. What is the strongest objection?",
        "options": [
            {"text": "Competition happens only when a population is growing.",
             "correct": False,
             "why": "A steady population competes just as hard, because more "
                    "are born than the resources support in every year. "
                    "Growth is not the trigger."},
            {"text": "Space, shelter and mates are all competed for, even in "
                     "a year when food is plentiful.",
             "correct": True},
            {"text": "Competition only begins once a shortage is bad enough "
                     "for animals to start fighting each other over what is "
                     "left.",
             "correct": False,
             "why": "Most competition never involves a fight at all. Two "
                    "plants shading each other out are competing without "
                    "either one touching the other."},
            {"text": "Food is the one thing animals never compete for.",
             "correct": False,
             "why": "Food is the commonest thing competed for and the one "
                    "that bites first. Moving elsewhere means arriving where "
                    "something else is already eating."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s27",
        "band": "standard",
        "text": "A gardener sows a row of carrot seed and then pulls up four "
                "seedlings in every five so that the rest have room to grow. "
                "Which idea from this lesson does that illustrate?",
        "options": [
            {"text": "That gardeners can improve a crop by choosing which "
                     "plants to keep.",
             "correct": False,
             "why": "The gardener is not choosing between kinds of carrot — "
                    "he is thinning for room. What this shows is the "
                    "shortage, not a choice."},
            {"text": "That plants do not compete with one another unless "
                     "somebody plants them too close together.",
             "correct": False,
             "why": "Wild plants crowd each other constantly and nobody sows "
                    "them. Sowing thickly makes the shortage easier to see, "
                    "not different in kind."},
            {"text": "That a seedling grows better in soil that has been "
                     "disturbed around its roots.",
             "correct": False,
             "why": "Disturbing the soil is a side effect of the thinning. "
                    "What the row demonstrates is that the bed cannot "
                    "support every seed that was sown."},
            {"text": "That far more are produced than the resources can "
                     "support, so most of them cannot survive.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s28",
        "band": "standard",
        "text": "On one island, two finch species eat seeds of the same size "
                "and a third eats insects. Between which birds would you "
                "expect the fiercest competition?",
        "options": [
            {"text": "Between the two seed-eating species, because they need "
                     "the same limited food.",
             "correct": True},
            {"text": "Between the insect-eater and each seed-eater, because "
                     "species that feed differently get in each other's way "
                     "most.",
             "correct": False,
             "why": "Feeding differently is what keeps two species out of "
                    "each other's way. Competition needs both of them to be "
                    "short of the same thing."},
            {"text": "Between no two of them, because competition happens "
                     "only inside a species and never between species.",
             "correct": False,
             "why": "Different species compete wherever they overlap. What "
                    "is true is that members of one species overlap on "
                    "everything at once."},
            {"text": "Between the insect-eater and both seed-eaters equally, "
                     "since all three live on one small island.",
             "correct": False,
             "why": "Sharing an island is not the same as sharing a food "
                    "supply. The insect-eater is short of something neither "
                    "seed-eater wants."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s29",
        "band": "standard",
        "text": "When a barn owl arrives, boldness and pale sandy fur are "
                "the two worst variations a mouse can carry. Does that make "
                "them poor variations?",
        "options": [
            {"text": "Yes, because being eaten ends everything.",
             "correct": False,
             "why": "It gets an animal eaten in this field and saves it in "
                    "another. Pale fur over snow is the hardest coat of the "
                    "five for an owl to find."},
            {"text": "Yes for boldness, because taking risks is never worth "
                     "it, and no for pale fur, which is only a problem on "
                     "dark ground.",
             "correct": False,
             "why": "Boldness is the best variation to have in a crowded "
                    "year, when a bold mouse finds ground and food the rest "
                    "have not reached. Both of them pay somewhere."},
            {"text": "No: boldness pays in a crowded year and pale fur pays "
                     "over snow.",
             "correct": True},
            {"text": "No, because being eaten by a predator does not affect "
                     "which variations are passed on to the next generation.",
             "correct": False,
             "why": "It affects them a great deal. Whichever variations help "
                    "an animal avoid being eaten are the ones that get "
                    "passed on."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-s30",
        "band": "standard",
        "text": "A mouse is described as the best survivor of a long "
                "drought. What does that description NOT tell you?",
        "options": [
            {"text": "Why it survived the drought better than the others "
                     "did.",
             "correct": False,
             "why": "Being the best survivor of a drought points straight at "
                    "the reason: it needs little water and loses heat "
                    "easily. That much the description does give you."},
            {"text": "That it survived the drought better than the rest of "
                     "the population.",
             "correct": False,
             "why": "That is precisely what the description says. The "
                    "question is what it leaves out."},
            {"text": "How it would do in any other conditions.",
             "correct": True},
            {"text": "That a drought is a set of conditions some animals "
                     "survive and others do not.",
             "correct": False,
             "why": "A best survivor implies worse ones, so the description "
                    "carries that with it. What it cannot carry is a result "
                    "from a different year."},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-01-h14",
        "band": "harder",
        "text": "When an owl hunts a field, 80 of every 100 small quick mice "
                "survive the year and 20 of every 100 bold ones do. A "
                "population holds 150 of each kind. How many more quick mice "
                "than bold mice survive?",
        "options": [
            {"text": "60 mice",
             "correct": False,
             "why": "60 is the difference between the two percentages, and a "
                    "percentage is not a number of animals. Each rate has to "
                    "be applied to the 150 first."},
            {"text": "90 mice",
             "correct": True},
            {"text": "120 mice",
             "correct": False,
             "why": "120 is how many quick mice survive. The 30 surviving "
                    "bold mice still have to be taken off to give a "
                    "difference."},
            {"text": "150 mice",
             "correct": False,
             "why": "150 is how many of each kind there were to begin with. "
                    "The question asks for a difference between two numbers "
                    "of survivors."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h15",
        "band": "harder",
        "text": "Of 400 pale mice living where snow lies, 300 survive a "
                "winter. Of 400 pale mice on bare dark peat with an owl "
                "hunting, 100 survive. How many times more likely is a pale "
                "mouse to survive on the snow?",
        "options": [
            {"text": "Three times as likely.",
             "correct": True},
            {"text": "Twice as likely, because 300 is 200 more survivors "
                     "than 100 and 200 is half of 400.",
             "correct": False,
             "why": "A difference of 200 is not a ratio. How many times more "
                    "likely is found by dividing one chance by the other, "
                    "which gives 75% over 25%."},
            {"text": "Two hundred times as likely, since two hundred more "
                     "mice come through the winter than come through the "
                     "year on peat.",
             "correct": False,
             "why": "200 is again the difference rather than the ratio. "
                    "Dividing 300 by 100 is what answers a how-many-times "
                    "question."},
            {"text": "Fifty times as likely, because the survival rate rises "
                     "by fifty percentage points between the two fields.",
             "correct": False,
             "why": "The rise is indeed 50 percentage points, from 25% to "
                    "75%, and that is still a difference. The ratio of the "
                    "two rates is 3."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h16",
        "band": "harder",
        "text": "A caterpillar species varies from green to brown. In June, "
                "birds hunting among green leaves take mostly the brown "
                "ones; in October, on brown fallen leaves, they take mostly "
                "the green ones. A student concludes that neither colour is "
                "an advantage. What is the correct reply?",
        "options": [
            {"text": "The student is right, because a colour that fails half "
                     "the year cannot be called an advantage at all.",
             "correct": False,
             "why": "Every variation fails somewhere, and that does not "
                    "cancel it. Each colour is a real advantage during the "
                    "months when it matches the leaves."},
            {"text": "The student is wrong: brown is the better colour, "
                     "since brown leaves are on the ground for far longer "
                     "than green ones are on the trees.",
             "correct": False,
             "why": "Counting months does not settle it either. The "
                    "caterpillars are only feeding and being hunted during "
                    "part of the year, and the answer still turns on which "
                    "part."},
            {"text": "The student is wrong: each colour is an advantage "
                     "while it matches the leaves, and the conditions here "
                     "change with the season.",
             "correct": True},
            {"text": "The student is wrong, because being seen has nothing "
                     "to do with whether a caterpillar survives.",
             "correct": False,
             "why": "Being seen is the whole of the danger. The birds are "
                    "taking whichever caterpillars they can pick out against "
                    "the background."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h17",
        "band": "harder",
        "text": "One lake holds weedy shallows near the bank and open deep "
                "water in the middle, and the same fish species lives in "
                "both. Would you expect the same variations to pay in both "
                "parts?",
        "options": [
            {"text": "Yes, because the fish are one species in one lake, so "
                     "they are all in the same environment.",
             "correct": False,
             "why": "An environment is everything around an organism that "
                    "affects it, and weed, light and cover differ sharply "
                    "between the two parts. One lake is two environments."},
            {"text": "Yes, because a variation that suits a fish will suit "
                     "it wherever in the lake it happens to be swimming.",
             "correct": False,
             "why": "That is the belief the whole lesson takes apart. Hiding "
                    "among weed and outswimming a pike in open water ask for "
                    "different things."},
            {"text": "No, because fish in shallow water are always at a "
                     "disadvantage compared with fish in deep water.",
             "correct": False,
             "why": "Neither part is worse in general. Shallow weed gives "
                    "cover and food and costs room to escape; deep water is "
                    "the other way about."},
            {"text": "No, because the conditions differ between the two "
                     "parts, so different variations pay in each.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h18",
        "band": "harder",
        "text": "A student argues that because survival percentages used for "
                "teaching are chosen rather than measured, they could have "
                "been chosen to show the opposite pattern, so they prove "
                "nothing. What is the strongest reply?",
        "options": [
            {"text": "The figures are close enough to real measurements that "
                     "the difference does not matter.",
             "correct": False,
             "why": "Nobody claims they are measurements, and that claim "
                    "would be a weak defence. The real support comes from "
                    "populations where the pattern was measured."},
            {"text": "The same reversal has been measured in real "
                     "populations, such as the Galapagos finches before and "
                     "after the 1977 drought.",
             "correct": True},
            {"text": "Chosen figures are as good as measured ones, provided "
                     "the person choosing them understands the science.",
             "correct": False,
             "why": "They are not as good, which is exactly why the note "
                    "says they are teaching values. Their job is to make a "
                    "measured pattern readable."},
            {"text": "It does not matter what the figures show, because the "
                     "conclusion was already known before they were written "
                     "down.",
             "correct": False,
             "why": "A conclusion that no evidence could test is not worth "
                    "much. The answer to the objection is the evidence, not "
                    "a refusal to be tested."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h19",
        "band": "harder",
        "text": "In one field, mice over 25 g survive a hard winter at 70% "
                "and mice under 15 g at 45%. In a drought in the same field "
                "the figures are 40% and 85%. A farmer asks what size of "
                "mouse he should expect to find there. What is the best "
                "answer?",
        "options": [
            {"text": "Mice over 25 g, because they survive the more "
                     "dangerous of the two kinds of year.",
             "correct": False,
             "why": "Neither year is the more dangerous in general — each is "
                    "lethal to the mice the other suits. A winter figure "
                    "cannot rank a drought."},
            {"text": "Mice under 15 g, because 85% is the highest survival "
                     "figure of the four.",
             "correct": False,
             "why": "It is the highest figure and it belongs to one kind of "
                    "year. Picking the largest number in a table ignores "
                    "which year the field actually has."},
            {"text": "Neither size in particular, because the ranking "
                     "reverses with the weather, so it depends what kind of "
                     "years the field has.",
             "correct": True},
            {"text": "Both sizes in equal numbers, because the two sets of "
                     "figures cancel one another out exactly.",
             "correct": False,
             "why": "They only cancel if hard winters and droughts arrive "
                    "equally often, which nothing here says. The answer "
                    "depends on how often each kind of year comes."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h20",
        "band": "harder",
        "text": "Some individuals in a population clearly do leave more "
                "surviving offspring than others. Why does that not make "
                "them generally superior individuals?",
        "options": [
            {"text": "Because superiority is a word about strength, and the "
                     "animals leaving most offspring are rarely the "
                     "strongest ones.",
             "correct": False,
             "why": "Strength is only one of the variations at stake. Even "
                    "if the strongest did leave most offspring in some year, "
                    "that would still be a result about that year."},
            {"text": "Because the number of offspring an individual leaves "
                     "is settled by chance rather than by any variation it "
                     "carries.",
             "correct": False,
             "why": "Chance plays a part and the variations matter a great "
                    "deal, which is why the numbers differ so consistently "
                    "between kinds. The point is which conditions they are "
                    "differing in."},
            {"text": "Because offspring are counted at the end of a year, "
                     "and a year is too short a period to judge an animal "
                     "on.",
             "correct": False,
             "why": "Nothing here turns on the length of the count. It turns "
                    "on the fact that a longer count would run through "
                    "different conditions and give a different winner."},
            {"text": "Because leaving more offspring is a fact about one set "
                     "of conditions, and a different individual leads once "
                     "the conditions change.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h21",
        "band": "harder",
        "text": "After a severe winter storm, a scientist collected the "
                "sparrows killed and those that had survived, and found the "
                "survivors were more often of middling body size. Which "
                "conclusion does that support?",
        "options": [
            {"text": "That middling sparrows are the best sparrows, so the "
                     "population will go on getting more middling for ever.",
             "correct": False,
             "why": "Middling paid in this storm. A run of mild years, or a "
                    "different danger, would favour a different size, which "
                    "is why no size is best in general."},
            {"text": "That the storm killed sparrows at random.",
             "correct": False,
             "why": "If the killing were random the survivors would match "
                    "the original range of sizes. The survivors being "
                    "narrower in size than the population is the finding."},
            {"text": "That body size affected which sparrows came through "
                     "that particular storm.",
             "correct": True},
            {"text": "That the surviving sparrows shrank towards the middle.",
             "correct": False,
             "why": "No bird changed size during a storm. The measurement "
                    "compares two groups of birds, not one group before and "
                    "after."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h22",
        "band": "harder",
        "text": "A population of 500 mice is 60% thick-coated and 40% small "
                "and quick. In a hard winter thick-coated mice survive at "
                "90% and small quick ones at 45%. How many mice survive the "
                "winter altogether?",
        "options": [
            {"text": "270 mice",
             "correct": False,
             "why": "270 is the thick-coated survivors on their own. The 200 "
                    "small quick mice still contribute 90 more."},
            {"text": "338 mice",
             "correct": False,
             "why": "338 is what you get by averaging the two rates and "
                    "applying 67.5% to all 500. The two groups are different "
                    "sizes, so each has to be worked out separately."},
            {"text": "360 mice",
             "correct": True},
            {"text": "675 mice",
             "correct": False,
             "why": "675 is 90% and 45% of 500 added together, which counts "
                    "every mouse twice. Each rate applies only to its own "
                    "part of the population."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h23",
        "band": "harder",
        "text": "An island has no predators, plenty of food and very little "
                "fresh water. Which variation would you expect to be the "
                "largest advantage to a mouse living there?",
        "options": [
            {"text": "Speed, because a quick animal can cover more of the "
                     "island in a day and so find more of whatever there is.",
             "correct": False,
             "why": "Speed earns its keep against predators and in the heat "
                    "of a drought. With no predators and plenty of food, "
                    "covering ground buys very little."},
            {"text": "A thick coat, since such islands are cold and windy.",
             "correct": False,
             "why": "Nothing here says the island is cold, and a thick coat "
                    "would be a serious cost if it were not. The stated "
                    "shortage is water."},
            {"text": "Size, because with plenty of food a large mouse can "
                     "grow larger still and dominate the others.",
             "correct": False,
             "why": "There is nothing much to dominate where food is "
                    "plentiful, and a large body needs more water — which is "
                    "the one thing in short supply."},
            {"text": "Needing very little water, because water is the one "
                     "thing that runs short there.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h24",
        "band": "harder",
        "text": "Suppose you wanted to test the claim that no variation is "
                "an advantage in general. What result would count as "
                "evidence against it?",
        "options": [
            {"text": "Finding one variation that raised survival in every "
                     "set of conditions tested.",
             "correct": True},
            {"text": "Finding one variation that raised survival in more "
                     "sets of conditions than any of the others did.",
             "correct": False,
             "why": "Coming top most often is not the same as never failing. "
                    "A variation that wins four conditions and loses the "
                    "fifth still is not an advantage in general."},
            {"text": "Finding a population with no variation in it at all.",
             "correct": False,
             "why": "That would be a population with no variation to "
                    "compare, so it could not test the claim either way."},
            {"text": "Finding conditions where no variation made a "
                     "difference.",
             "correct": False,
             "why": "That fits the claim rather than contradicting it. A "
                    "danger that no visible variation answers is exactly "
                    "what a new disease is."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h25",
        "band": "harder",
        "text": "Two mice carry the same variation. One leaves eight young "
                "that survive to breed and the other leaves none. Does that "
                "show the variation was not an advantage?",
        "options": [
            {"text": "Yes, because an advantage that fails one of the two "
                     "animals carrying it cannot be a real advantage.",
             "correct": False,
             "why": "An advantage shifts the odds for the animals carrying "
                    "it. It has never promised a result to any particular "
                    "one of them."},
            {"text": "No, because an advantage raises the chance of "
                     "surviving and breeding, and chance still decides what "
                     "happens to any one animal.",
             "correct": True},
            {"text": "Yes, because two animals with the same variation in "
                     "the same place should do equally well as each other.",
             "correct": False,
             "why": "They will not, because a great deal else differs "
                    "between them and because accidents happen. A variation "
                    "moves the average, not every case."},
            {"text": "No, because the second mouse must have been carrying a "
                     "second variation that cancelled the first one out.",
             "correct": False,
             "why": "No hidden second variation is needed to explain it. Bad "
                    "luck alone accounts for one animal in a pair leaving "
                    "nothing."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h26",
        "band": "harder",
        "text": "A wildlife park keeps a deer herd at a size where food is "
                "never short. A visitor says there is no competition in the "
                "park. What is the strongest objection?",
        "options": [
            {"text": "Food is short in the park too, because the deer eat "
                     "what is put out for them faster than the keepers "
                     "replace it.",
             "correct": False,
             "why": "The question says food is never short, and the "
                    "objection has to work even so. Denying the premise is "
                    "not the strongest reply available."},
            {"text": "Competition cannot be switched off by a keeper.",
             "correct": False,
             "why": "That is an assertion rather than a reason. The reason "
                    "is that particular things — mates, the best shelter — "
                    "are still limited in the park."},
            {"text": "There is no competition: the visitor is right.",
             "correct": False,
             "why": "Food is the commonest thing competed for and not the "
                    "only one. Space, shelter and mates are all limited in a "
                    "park."},
            {"text": "Mates and the best shelter are still limited, so the "
                     "deer are still competing for them.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h27",
        "band": "harder",
        "text": "A population of lizards is moved from an island into a warm "
                "greenhouse with no predators. Ten years later far more of "
                "them survive each year than survive on the island, and the "
                "keepers say the greenhouse lizards are better adapted. What "
                "is wrong with that?",
        "options": [
            {"text": "Nothing is wrong, since surviving better is what being "
                     "better adapted means.",
             "correct": False,
             "why": "Surviving better than what, and where? The two groups "
                    "are not facing the same conditions, so their survival "
                    "rates cannot be set against each other."},
            {"text": "The two groups are in different conditions, so a "
                     "higher survival rate in one says nothing about how "
                     "well adapted it is.",
             "correct": True},
            {"text": "The greenhouse lizards cannot be better adapted, "
                     "because an animal kept by people is not adapted to "
                     "anything at all.",
             "correct": False,
             "why": "A greenhouse is an environment like any other, and a "
                    "lizard can be well or badly suited to it. The fault is "
                    "in the comparison, not in the greenhouse."},
            {"text": "Ten years is far too short a time for a population to "
                     "become better adapted to anywhere.",
             "correct": False,
             "why": "The claim would be wrong after a thousand years as "
                    "well. You cannot rank two groups by survival when each "
                    "is measured somewhere different."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h28",
        "band": "harder",
        "text": "In one winter an owl took 45 of the 300 pale mice in a "
                "field and 60 of the 200 dark mice. Which colour was at "
                "greater risk, and by how much?",
        "options": [
            {"text": "The dark mice, at twice the risk of the pale ones.",
             "correct": True},
            {"text": "The dark mice, at one and a third times the risk, "
                     "since 60 taken is a third more than 45 taken.",
             "correct": False,
             "why": "Comparing the two counts ignores how many of each "
                    "colour there were. 45 out of 300 is 15% and 60 out of "
                    "200 is 30%."},
            {"text": "The pale mice, because 300 of them lived in the field "
                     "and only 200 dark ones did.",
             "correct": False,
             "why": "How common a colour is does not tell you the risk to a "
                    "mouse carrying it. Risk is the share of that group that "
                    "was taken."},
            {"text": "Neither: 45 and 60 are close enough that the "
                     "difference is not worth anything.",
             "correct": False,
             "why": "As shares of their own groups they are not close at all "
                    "— 15% against 30%. The raw counts are the wrong things "
                    "to compare."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h29",
        "band": "harder",
        "text": "In a long drought the largest and heaviest mice in a "
                "population are the first to die. A student calls them the "
                "weakest members of the population. Why is that the wrong "
                "word?",
        "options": [
            {"text": "Because they are the same mice that won the crowded "
                     "year, and size costs water here and pays there.",
             "correct": True},
            {"text": "Because weak is an unkind word to use about an animal "
                     "that has died of thirst.",
             "correct": False,
             "why": "The objection is not about kindness. It is that the "
                    "word names a property of the mouse when what has "
                    "changed is the conditions around it."},
            {"text": "Because the largest animals in any population are by "
                     "definition the strongest ones in it.",
             "correct": False,
             "why": "Large and strong are not the same thing, and neither of "
                    "them is the point. Even a genuinely strong mouse dies "
                    "first where water is short."},
            {"text": "Because dying first in a drought has nothing to do "
                     "with the variations a mouse carries.",
             "correct": False,
             "why": "It has everything to do with them — a large body needs "
                    "more water. The mistake is calling that variation a "
                    "weakness rather than a cost in these conditions."},
        ],
        "figure": None,
    },
    {
        "id": "b11-01-h30",
        "band": "harder",
        "text": "Three students describe the same drought. A writes: the "
                "mice that needed least water were the fittest that year. B "
                "writes: the mice that needed least water are the fittest "
                "kind of mouse. C writes: the strongest mice survived the "
                "drought. Which is right?",
        "options": [
            {"text": "B, because a variation that carries a population "
                     "through a drought is the most valuable one it has.",
             "correct": False,
             "why": "It is the most valuable one that year. B drops the "
                    "year, which turns a result about a drought into a "
                    "ranking of mice in general."},
            {"text": "C, because coming through conditions as hard as a "
                     "drought is what being strong means.",
             "correct": False,
             "why": "Fittest does not mean strongest. In a drought the "
                    "winner is the animal that needs least water, and it may "
                    "be the least impressive of the lot."},
            {"text": "A, because fitness is always fitness in particular "
                     "conditions.",
             "correct": True},
            {"text": "All three: they say the same thing.",
             "correct": False,
             "why": "They make three different claims. Only one of them "
                    "keeps the result attached to the year it came from."},
        ],
        "figure": None,
    },
]
