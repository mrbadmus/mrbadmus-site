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
]
