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
            {"text": "It is something an organism produces for the rest of its "
                     "population to use.",
             "correct": False,
             "why": "Resources are not produced by the population that needs "
                    "them. Food, water and shelter are things the surroundings "
                    "supply, in limited amounts."},
            {"text": "It is something an organism needs, and there is not "
                     "enough of it for everyone born.",
             "correct": True},
            {"text": "It is anything nearby that can harm an organism if there "
                     "is too much of it.",
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
            {"text": "Stronger than its competitors.",
             "correct": False,
             "why": "Strength is one variation among many, and it is often the "
                    "wrong one. It is not a general ranking of species."},
            {"text": "Further along in its evolution.",
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
            {"text": "A thick coat makes a mouse look larger, so predators "
                     "leave it alone.",
             "correct": False,
             "why": "Nothing here is hunting by size. What kills mice in a "
                    "hard winter is the cold itself, and losing heat is the "
                    "danger a thick coat answers."},
            {"text": "Growing a thicker coat is how a mouse responds to the "
                     "cold coming.",
             "correct": False,
             "why": "The mouse grew nothing to order. It has the coat it was "
                    "born with, and that coat happens to suit the winter it is "
                    "in."},
            {"text": "Insulation is exactly what this winter demands, and it "
                     "costs the mouse almost nothing to carry.",
             "correct": True},
            {"text": "A thick coat lets the mouse dig deeper for the food "
                     "buried under the snow.",
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
            {"text": "Everything around an organism that affects it, including "
                     "the other members of its own species.",
             "correct": True},
            {"text": "The habitat a species is best suited to, whether or not "
                     "it lives there.",
             "correct": False,
             "why": "The environment is where an organism actually is, not "
                    "where it would do well. Change what is around it and the "
                    "ranking of variations changes with it."},
            {"text": "Everything a species has changed about the place it "
                     "lives in.",
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
            {"text": "Two mice from the same litter both trying to use the "
                     "only dry burrow.",
             "correct": True},
            {"text": "A mouse sheltering from a hard frost under a hedge.",
             "correct": False,
             "why": "Nothing is being competed for here. Competition needs two "
                    "organisms and one limited resource between them."},
            {"text": "A virus spreading through a mouse population in a mild "
                     "year.",
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
            {"text": "It means a real mouse would survive everything, since it "
                     "has all five variations.",
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
            {"text": "The conclusion still holds; what the simplification "
                     "hides is that real fitness depends on many "
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
]
