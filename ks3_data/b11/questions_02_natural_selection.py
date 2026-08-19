"""B11 lesson 02 — Natural selection: twelve questions (MRB-269).

These probe the one claim the lesson is built on — individuals do not change,
populations do — and they probe it from the angles the ladder does not already
occupy. The `easier` band checks the words that carry the misconception on
their own (adaptation as a feature rather than an action, a selection pressure
that chooses nothing) and the two things the five step cards fix in place:
that the variation is there before the conditions change, and that the patchy
bark is a control. The `standard` band works on the bench and on the moth-pair
figure — reading survival rates off a described run, switching bark after a
run to test whether selection has a memory, and diagnosing a sentence that
gives the birds a goal. The `harder` band takes the mechanism to bacteria
(where the only thing that differs is generation time), to a population with
no useful variation at all (which is why extinction is common), to the
Kettlewell–Majerus method story, and to an unfamiliar beetle where the test is
whether a sentence smuggles a purpose in.

The distractors are built from the lesson's two declared misconceptions —
EVOL-03 (animals change themselves to suit their environment and pass the
change on) and EVOL-04 (the population needed to change, so it did) — plus the
three the lesson body and ladder corrections name without registering: that
colour is applied by the environment rather than inherited, that learning is
inherited, and that a drug or a pressure creates the resistance it selects
for. The purpose-smuggling phrases "developed" and "in order to", which
`#s-think` names explicitly, are used as distractor wording rather than
described.
"""

UNIT = "B11"
LESSON = "natural-selection"
LESSON_NUMBER = 2

QUESTIONS = [
    # ── easier ──────────────────────────────────────────────────────────
    {
        "id": "b11-02-e01",
        "band": "easier",
        "text": "This lesson is careful about the word adaptation. What does "
                "it mean?",
        "options": [
            {"text": "Something an organism does during its own life to fit "
                     "in better with its surroundings.",
             "correct": False,
             "why": "This is the wrong idea the whole lesson exists to "
                    "correct. Read adapt as a verb and you have it: no "
                    "individual adapts during its life."},
            {"text": "A feature an organism has that makes it well suited to "
                     "the place it lives.",
             "correct": True},
            {"text": "A change a species makes for itself once the conditions "
                     "turn against it.",
             "correct": False,
             "why": "A species cannot make a change because it needs one. "
                    "Nothing in this process is aiming at anything, and a "
                    "population that lacks the variation simply dies."},
            {"text": "A useful habit an organism learns and then passes on to "
                     "its own offspring.",
             "correct": False,
             "why": "Learning is not inherited. What gets passed on is the "
                    "versions of the genes the parent carried, not anything "
                    "it picked up while alive."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e02",
        "band": "easier",
        "text": "Step 1 of the five puts variation first. So when were there "
                "already dark moths in the British population?",
        "options": [
            {"text": "Long before the factories were built — dark moths "
                     "existed all along, they were simply rare.",
             "correct": True},
            {"text": "As soon as the soot arrived, because bark that has been "
                     "blackened blackens what rests on it.",
             "correct": False,
             "why": "Colour is inherited, not applied by the surface a moth "
                    "sits on. If soot painted them, washing one would turn it "
                    "pale again — and its offspring would be pale anyway."},
            {"text": "Once the pale moths started to struggle, so that the "
                     "population had a form that could cope.",
             "correct": False,
             "why": "A population cannot produce a variation because it needs "
                    "one. The variation has to be there first, or there is "
                    "nothing for selection to work on."},
            {"text": "After several generations of moths each darkening a "
                     "little and passing the darkening on.",
             "correct": False,
             "why": "No moth ever darkened. A moth is the colour it hatched "
                    "and it stays that colour, so there is no darkening for "
                    "it to pass on."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e03",
        "band": "easier",
        "text": "On the patchy bark tab, pale and dark moths have exactly the "
                "same survival rate and the columns barely move. Why is that "
                "setting on the bench at all?",
        "options": [
            {"text": "It is the most realistic bark, so it shows what really "
                     "happened to the moths in Britain.",
             "correct": False,
             "why": "Realism is not what it is for. All three barks are real "
                    "woodland states — this one is on the bench because of "
                    "what it does, not where it is found."},
            {"text": "It shows selection working slowly, because a patchy "
                     "background hides both colours a little.",
             "correct": False,
             "why": "Nothing is happening slowly here — nothing is happening "
                    "at all. The two survival rates are equal, so the "
                    "proportions stay exactly where they were."},
            {"text": "It is the control: with no difference in survival there "
                     "is no selection, so nothing moves.",
             "correct": True},
            {"text": "It lets the population recover in between runs before "
                     "you try a different bark on it.",
             "correct": False,
             "why": "It recovers nothing. Switching to patchy bark freezes "
                    "the population where the last run left it — the reset "
                    "button is the thing that changes the proportions back."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-e04",
        "band": "easier",
        "text": "A bird eats whichever moths it happens to be able to see. In "
                "the language of this lesson, what is that bird?",
        "options": [
            {"text": "An adaptation, because being eaten is the thing that "
                     "shapes the moths over time.",
             "correct": False,
             "why": "An adaptation is a feature of an organism, not an event "
                    "that happens to it. The bird is part of the environment "
                    "the moths are living in."},
            {"text": "A selection pressure: part of the environment that "
                     "makes some variations survive better.",
             "correct": True},
            {"text": "The chooser, because it decides which colour the moth "
                     "population is going to become.",
             "correct": False,
             "why": "Nothing is choosing. The bird is not deciding anything "
                    "about the population's future — it eats what it can see, "
                    "and the proportion follows from that."},
            {"text": "A cause of mutation, because it changes the moths that "
                     "hatch in the next generation.",
             "correct": False,
             "why": "The bird changes no moth and no gene. All it changes is "
                    "which moths are still alive to breed, and that is enough "
                    "on its own."},
        ],
        "figure": None,
    },

    # ── standard ────────────────────────────────────────────────────────
    {
        "id": "b11-02-s01",
        "band": "standard",
        "text": "The drawing shows the same pale moth on both barks: almost "
                "invisible on lichen, obvious on soot. What does that tell "
                "you about being hard to see?",
        "options": [
            {"text": "It belongs to the moth and the background together, "
                     "never to the moth on its own.",
             "correct": True},
            {"text": "Pale is the better colour for a peppered moth, and soot "
                     "is what spoils the advantage.",
             "correct": False,
             "why": "There is no better colour. Which one is better depends "
                    "entirely on the bark — swap the background and the "
                    "advantage swaps with it."},
            {"text": "The moth on the sooty panel has been slightly darkened "
                     "by the bark it is resting on.",
             "correct": False,
             "why": "Look again: it is the same moth in both panels, drawn "
                    "the same colour. Neither moth changed. Only the bark "
                    "did."},
            {"text": "A moth that can see it is on the wrong bark will move "
                     "to a background that suits it.",
             "correct": False,
             "why": "Nothing here is choosing where to rest to stay safe. "
                    "The moth is the colour it hatched, on whatever bark it "
                    "is on, and the bird does the rest."},
        ],
        "figure": "b11-moth-pair",
    },
    {
        "id": "b11-02-s02",
        "band": "standard",
        "text": "You run ten generations on sooty bark until the population "
                "is nearly all dark, then switch the tab to clean lichen bark "
                "and keep going. What happens next?",
        "options": [
            {"text": "Nothing much: the population has already evolved to be "
                     "dark, so that is what it stays.",
             "correct": False,
             "why": "A population does not keep an advantage it no longer "
                    "has. On lichen the pale form survives better, and the "
                    "proportions start moving straight back."},
            {"text": "The dark moths gradually lighten again, now that being "
                     "dark has stopped paying off.",
             "correct": False,
             "why": "No moth lightens. Every moth on the bench dies the "
                    "colour it hatched — what moves is how many of each "
                    "colour get to have offspring."},
            {"text": "The population drifts back towards pale, because on "
                     "lichen the pale form now survives better.",
             "correct": True},
            {"text": "The population goes darker still, because once it has "
                     "started in a direction it carries on.",
             "correct": False,
             "why": "Selection has no memory and no direction. Each "
                    "generation is decided only by which moths survive on the "
                    "bark that is there now."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s03",
        "band": "standard",
        "text": "On clean lichen bark, 85 pale moths in every 100 survive "
                "each generation but only 45 dark ones do. Predict what the "
                "columns do over the next few generations.",
        "options": [
            {"text": "They hold steady, because moths of both colours are "
                     "still being born every generation.",
             "correct": False,
             "why": "Both colours are still born, but fewer dark parents "
                    "survive to breed — so dark is a smaller share of each "
                    "generation than of the one before."},
            {"text": "The dark share falls a little each generation, because "
                     "fewer dark moths survive to breed.",
             "correct": True},
            {"text": "The dark share drops to nothing in a single generation, "
                     "since under half of them survive.",
             "correct": False,
             "why": "45 in 100 surviving is not none surviving. Almost "
                    "nothing happens in one generation on this bench — the "
                    "whole change is in the accumulation."},
            {"text": "The dark moths gradually pale off over a few "
                     "generations until they match the lichen.",
             "correct": False,
             "why": "You are changing the moths again. The bench carries "
                    "nothing but a proportion; no individual in it can change "
                    "colour, and none needs to."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-s04",
        "band": "standard",
        "text": "A student writes: \"The birds picked off the pale moths so "
                "that the population could survive on the sooty bark.\" What "
                "is wrong with that sentence?",
        "options": [
            {"text": "Nothing at all — picking which ones survive is exactly "
                     "what the word selection means.",
             "correct": False,
             "why": "The word selection is the trap in this lesson. Nothing "
                    "is selecting: a bird eats what it can see, and no part "
                    "of the process is aiming at a result."},
            {"text": "Only the colour: on sooty bark it is the dark moths "
                     "that the birds are picking off.",
             "correct": False,
             "why": "On soot the pale ones are the ones that show up, so the "
                    "colour is right. The error is in the words after it, not "
                    "in which moth got eaten."},
            {"text": "Only the birds: it is really the soot that is doing the "
                     "selecting, by staining the moths.",
             "correct": False,
             "why": "Soot stains no moth. And swapping one chooser for "
                    "another leaves the real problem untouched — the sentence "
                    "still gives the process a goal."},
            {"text": "The words \"so that\": they give the birds a goal, when "
                     "nothing here is aiming at anything.",
             "correct": True},
        ],
        "figure": None,
    },

    # ── harder ──────────────────────────────────────────────────────────
    {
        "id": "b11-02-h01",
        "band": "harder",
        "text": "The moths needed many generations to shift. Bacteria divide "
                "roughly every twenty minutes, and a population can be almost "
                "entirely resistant within days. Why so fast?",
        "options": [
            {"text": "The process is unchanged and still needs many "
                     "generations — days simply hold a great many of them.",
             "correct": True},
            {"text": "The antibiotic damages the bacteria that survive it, "
                     "and the damage turns them resistant.",
             "correct": False,
             "why": "The drug creates nothing. The resistant few were already "
                    "in the population before it was ever used, produced by "
                    "ordinary random mutation."},
            {"text": "Bacteria are simple enough to alter themselves quickly "
                     "when their surroundings turn hostile.",
             "correct": False,
             "why": "No bacterium alters itself, however simple it is. This "
                    "is the same wrong idea as a moth darkening to match the "
                    "bark, one organism smaller."},
            {"text": "The threat to bacteria is so severe that resistance "
                     "develops in the population very quickly.",
             "correct": False,
             "why": "Severity changes nothing about what a population can "
                    "produce. A population facing a change it has no "
                    "variation for does not conjure one up — it dies."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h02",
        "band": "harder",
        "text": "Conditions change sharply, and it turns out that not one "
                "individual in the population happens to carry a variation "
                "that helps. What does this lesson say happens?",
        "options": [
            {"text": "The population dies out, because selection can only "
                     "work on variation that is already there.",
             "correct": True},
            {"text": "The pressure of the new conditions brings the useful "
                     "variation out within a few generations.",
             "correct": False,
             "why": "A selection pressure only decides who survives out of "
                    "what already exists. It cannot call up a variation the "
                    "population does not have."},
            {"text": "The individuals under most pressure adjust to the new "
                     "conditions and pass the adjustment on.",
             "correct": False,
             "why": "What an organism does during its life does not rewrite "
                    "the DNA in its gametes, so there is nothing for it to "
                    "pass on, however hard the conditions are."},
            {"text": "The species develops what it needs, because the "
                     "alternative is that it does not survive.",
             "correct": False,
             "why": "Needing something is not a mechanism. This is exactly "
                    "why extinction is common rather than rare — no goal, no "
                    "trying, and no variation to select from."},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h03",
        "band": "harder",
        "text": "Kettlewell's 1950s moth experiment was fairly criticised on "
                "its method. Majerus later re-ran it the way the critics "
                "asked and got the same result, more strongly. What does that "
                "leave the conclusion?",
        "options": [
            {"text": "In doubt, because two experiments on one question "
                     "means nobody can now say which is right.",
             "correct": False,
             "why": "The two did not disagree. The second was run the way the "
                    "critics said it should be and found the same thing, "
                    "which is agreement, not a stalemate."},
            {"text": "Unchanged, because the original criticisms were unfair "
                     "and should have been set aside at the time.",
             "correct": False,
             "why": "The criticisms were fair — moths released by day, at "
                    "unnatural densities, onto trunks they do not rest on. "
                    "Attacking a method is how science works."},
            {"text": "Overturned, because the conclusion falls with the "
                     "method it was first produced by.",
             "correct": False,
             "why": "That is what was reported for a while, and it was wrong. "
                    "A method can be faulty and the conclusion still true — "
                    "which is what the better test then showed."},
            {"text": "On firmer ground than before, because it survived a "
                     "better test than the one that produced it.",
             "correct": True},
        ],
        "figure": None,
    },
    {
        "id": "b11-02-h04",
        "band": "harder",
        "text": "A beetle species living on dark volcanic rock is mostly "
                "dark-shelled. Which sentence explains that without smuggling "
                "a purpose into it?",
        "options": [
            {"text": "The beetles developed dark shells in order to hide "
                     "against the rock they live on.",
             "correct": False,
             "why": "\"Developed\" and \"in order to\" are the two phrases to "
                    "watch for. Together they hand the beetles an aim, and "
                    "nothing in this process aims at anything."},
            {"text": "Shell colour varied, and on dark rock the darker "
                     "beetles were eaten less, so more of them bred.",
             "correct": True},
            {"text": "The beetles needed to be dark to survive on that rock, "
                     "so over time the species became dark.",
             "correct": False,
             "why": "Needing a feature is not what produces it. Say it this "
                    "way and you have given a whole species a want it has no "
                    "way of acting on."},
            {"text": "Each beetle darkened over its life to match the rock, "
                     "and its offspring hatched darker.",
             "correct": False,
             "why": "A beetle that darkens in its own life passes none of it "
                    "on — the darkening never reaches its gametes, so the "
                    "next generation starts where the last one did."},
        ],
        "figure": None,
    },
]
